# Local Research Assistant

A tool that performs automated research on any topic using LangGraph, LangChain, and local LLMs through Ollama.

## Features

- Automated web research using Tavily API
- Local LLM processing using Ollama
- Multi-step research process:
  - Query generation
  - Web search
  - Source summarization
  - Reflection and follow-up questions
- Results saved as markdown files
- Research graph visualization

## Prerequisites

- Python 3.11+ or 3.12+
- [Ollama](https://ollama.ai/) installed
- Tavily API key

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd local_research_assistant
```

2. Create and activate a virtual environment:
```bash
conda create -n local_research python=3.12
conda activate local_research
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Pull the required Ollama model:
```bash
ollama pull llama3.3:70b-instruct-q2_K
```

5. Create a `.env` file in the project root with your API keys:
```
TAVILY_API_KEY=your_tavily_api_key
```

## Development Setup

1. Install langgraph development dependencies:
```bash
pip install "langgraph-cli[inmem]"
```

2. Start the development server:
```bash
langgraph dev
```

This will:
- Start the langgraph development server
- Enable real-time graph visualization
- Allow interactive debugging of the research process

## Usage

### Basic Usage
Run the research assistant:
```bash
python src/local_research_assistant.py --topic "Your research topic"
```

### Development Usage
Run the langgraph development server:
```bash
langgraph dev
```

The results will be saved in the `outputs` directory as markdown files with timestamps.

## Configuration

- Model: The default model is `llama3.3:70b-instruct-q2_K`
- Research loops: Default is 3 iterations
- These can be modified in `src/configuration.py`

## Output

The tool generates:
- A research graph visualization (`test.png`)
- A markdown file with:
  - Research summary
  - Sources used
  - Timestamp