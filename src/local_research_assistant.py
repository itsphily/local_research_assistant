# imports
#--------------------------------------------------------------------------------------------------
import os
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import json
import operator
from dataclasses import dataclass, field
from typing_extensions import TypedDict, Annotated, Literal
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import START, END, StateGraph
import asyncio


from state import SummaryState, SummaryStateInput, SummaryStateOutput
from prompts import query_writer_instructions, summarizer_instructions, reflection_instructions
from utils import tavily_search, deduplicate_and_format_sources, format_sources, visualize_graph, save_research_results
from configuration import Configuration

### LLM
#--------------------------------------------------------------------------------------------------
#llm = ChatOllama(model=Configuration.local_llm, temperature=0.0)
#llm_json_mode = ChatOllama(model=Configuration.local_llm, temperature=0.0, format="json")
llm = ChatOpenAI(model="gpt-4o", temperature=0.0)
llm_json_mode = ChatOpenAI(model="gpt-4o", temperature=0.0)
llm_json_mode.bind(response_format={"type": "json_object"})

### Functions
#--------------------------------------------------------------------------------------------------
def generate_query(state: SummaryState):
    """ Generate a query for web search"""


    # Log the current state
    print(f"Current research topic: {state.research_topic}")

    # Format the prompt
    query_writer_instructions_formatted = query_writer_instructions.format(research_topic=state.research_topic)

    # Generate the query
    """
    
    
    result = llm_json_mode.invoke([SystemMessage(content=query_writer_instructions_formatted), 
                                   HumanMessage(content="Generate a query for web search")])
    """
    system_message = [SystemMessage(content=query_writer_instructions_formatted)]+ [HumanMessage(content="Generate a query for web search")]
    result = llm_json_mode.invoke(system_message)

    query = json.loads(result.content)

    return {"search_query": query['query']}

def web_search(state: SummaryState):
    """ Perform a web search"""

    #search the web
    search_results = tavily_search(state.search_query, include_raw_content = True, max_results = 10)
    #format the search results
    search_str = deduplicate_and_format_sources(search_results, max_tokens_per_source = 2000)


    return {"sources_gathered": [format_sources(search_results)], 
            "research_loop_count": state.research_loop_count + 1, 
            "web_research_results": [search_str]}


def summarize_sources(state: SummaryState):
    """ Summarize the gathered sources"""

    # Existing summary
    existing_summary = state.running_summary

    # Most recent web research
    most_recent_web_research = state.web_research_results[-1]

    # build the human message
    if existing_summary:
        human_message_content = (
        f"Extend the existing summary: {existing_summary}\n\n"
        f"Include new search results: {most_recent_web_research}"
        f"that address the following topic: {state.research_topic}"
        )
    else:
        human_message_content = (
        f"Generate a summary of these search results: {most_recent_web_research}"
        f"that address the following topic: {state.research_topic}"
        )

    # Run llm
    """

    result = llm.invoke([SystemMessage(content=summarizer_instructions), 
                         HumanMessage(content=human_message_content)])
    """
    system_message = [SystemMessage(content=summarizer_instructions)] + [HumanMessage(content=human_message_content)]
    result = llm_json_mode.invoke(system_message)

    running_summary = result.content
    print("================")
    print(running_summary)
    print("================")
    return {"running_summary": running_summary}


def reflect_on_summary(state: SummaryState):
    """ Reflect on the summary"""

    # Generate a query
    """
    
    
    result = llm_json_mode.invoke(
        [SystemMessage(content=reflection_instructions.format(
            research_topic=state.research_topic,
            running_summary=state.running_summary
        )),
         HumanMessage(content = f"Identify a knowledge gap and generate a follow-up web search query based on our existing knowledge: {state.running_summary}")]
    )
    """
    system_message = [SystemMessage(content=reflection_instructions.format(
            research_topic=state.research_topic,
            running_summary=state.running_summary
        ))] + [HumanMessage(content = f"Identify a knowledge gap and generate a follow-up web search query based on our existing knowledge: {state.running_summary}")]
    result = llm_json_mode.invoke(system_message)
    # Extract the content and remove code block delimiters
    content = result.content.strip()
    if content.startswith("```") and content.endswith("```"):
        content = re.sub(r'^```json|```$', '', content).strip()

    follow_up_query = json.loads(content)


    # Overwrite the search query
    return {"search_query": follow_up_query['follow_up_query']}


def finalize_summary(state: SummaryState):
    """ Finalize the summary"""

    # Format all accumulated sources into a single bulleted list
    all_sources = "\n".join(source for source in state.sources_gathered)

    state.running_summary = f"## Summary\n\n{state.running_summary}\n\n## Sources\n\n{all_sources}"

    return {"running_summary": state.running_summary}

def route_research(state: SummaryState, config: RunnableConfig) -> Literal["finalize_summary", "web_research"]:
    """ Route the research based on the follow-up query"""

    configurable = Configuration.from_runnable_config(config)
    if state.research_loop_count <= configurable.max_web_research_loops:
        print(f"Research loop count: {state.research_loop_count}")
        return "web_research"
    else:
        return "finalize_summary"


# Add nodes and edges 
builder = StateGraph(SummaryState, input=SummaryStateInput, output=SummaryStateOutput, config_schema=Configuration)
builder.add_node("generate_query", generate_query)
builder.add_node("web_research", web_search)
builder.add_node("summarize_sources", summarize_sources)
builder.add_node("reflect_on_summary", reflect_on_summary)
builder.add_node("finalize_summary", finalize_summary)

# Add edges
builder.add_edge(START, "generate_query")
builder.add_edge("generate_query", "web_research")
builder.add_edge("web_research", "summarize_sources")
builder.add_edge("summarize_sources", "reflect_on_summary")
builder.add_conditional_edges("reflect_on_summary", route_research)
builder.add_edge("finalize_summary", END)

graph = builder.compile()


def main():
    # For demonstration, we'll hard-code the research topic.
    # In a production scenario, you might read from command-line arguments or prompt the user.
    research_topic = "DeepSeek-V3 Capabilities"
    research_input = SummaryStateInput(research_topic=research_topic)
    visualize_graph(graph)
    # Run the graph with the given input
    result = graph.invoke(research_input)
    
    # Save the results to a markdown file
    save_research_results(research_topic, result["running_summary"])

if __name__ == "__main__":
    main()