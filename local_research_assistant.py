# import for local LLM
from langchain_ollama import ChatOllama

import operator
from dataclasses import dataclass, field
from typing_extensions import TypedDict, Annotated, Literal



### LLM
local_llm = "llama3.3"
llm = ChatOllama(model=local_llm, temperature=0.0)
llm_json_mode = ChatOllama(model=local_llm, temperature=0.0, format="json")


@dataclass(kw_only=True)
class SummaryState: 
    research_topic: str = field(default = None) # Report topic
    search_query: str = field(defautl = None) # Search query
    web_search_results: Annotated[list, operator.add] = field(default_factory=list)
    sources_gathered: Annotated[list, operator.add] = field(default_factory=list)
    research_loop_count: int = field(default = 0) # Research loop count
    running_summary:str = field(default = None) # final report

@dataclass(kw_only=True)
class SummaryStateInput(TypedDict):
    research_topic: str = field(default = None) # Report topic

@dataclass(kw_only=True)
class SummaryStateOutput(TypedDict):
    running_summary: str = field(default = None) # Report topic
