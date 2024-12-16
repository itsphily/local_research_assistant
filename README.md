# Research Assistant

This repository contains a research assistant that helps with online research. It uses LangGraph to orchestrate a research workflow that:

1. Takes a research topic
2. Performs web searches to gather relevant information
3. Synthesizes information into a coherent summary
4. Identifies follow-up questions to explore
5. Iteratively explores those questions to build a comprehensive understanding

## Usage

First, copy `.env.example` to `.env` and add your API keys.

Then run the notebook to see the research assistant in action.

## Components

The main components are:

- Research workflow orchestrated with LangGraph
- Web search using Tavily
- LLM-based information synthesis and question generation
- State management to track research progress

## License

MIT 