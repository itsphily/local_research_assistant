# Research: How to build good AI research agents?

*Generated on: 2024-12-29 09:35:30*

## Summary

Building trustworthy and effective AI agents requires a multifaceted approach that combines intentional design, system-level controls, and the implementation of trust patterns. Salesforce emphasizes the importance of creating AI systems that enable safe and easy human-AI partnerships. Their approach, exemplified by their Agentforce product, includes designing AI agents with transparency, accountability, and safeguards. Key strategies involve reducing hallucinations through topic classification, limiting the frequency of agent-generated communications, respecting user privacy with opt-out features, ensuring transparency by design, and facilitating smooth AI-human handoffs. These measures are supported by rigorous testing and ethical guidelines to ensure reliability and trustworthiness.

Amazon's Bedrock Agents focus on building robust generative AI applications by collecting high-quality ground truth data, defining clear agent scopes, and architecting solutions with small, focused agents that interact with each other. This method emphasizes the importance of accurate data and clear boundaries to guide development and ensure reliable AI performance.

Addressing AI hallucinations, which occur when AI models generate incorrect or unrelated information, is crucial for maintaining trust. Hallucinations can arise from inadequate training data, overfitting, and model architecture limitations. Techniques to mitigate these include training models with domain-specific data, using external knowledge bases for verification, and employing advanced methods like Retrieval-Augmented Generation (RAG) and chain-of-thought prompting. These strategies help align AI outputs with factual accuracy and context.

Several frameworks are available for building AI agents. LangChain and LangGraph provide tools for developing applications powered by large language models (LLMs), focusing on complex reasoning and multi-agent coordination. CrewAI offers a role-based architecture for orchestrating collaborative AI systems, while Microsoft Semantic Kernel and AutoGen provide frameworks for integrating AI capabilities into existing applications and building advanced multi-agent systems. These frameworks offer pre-built components and best practices to streamline AI agent development, allowing developers to focus on unique application aspects.

LangGraph, an extension of LangChain, is particularly useful for building complex, interactive AI systems involving planning, reflection, and multi-agent coordination. CrewAI simplifies the development of collaborative AI systems with a role-based architecture, while Microsoft Semantic Kernel bridges traditional software development with AI capabilities, emphasizing seamless integration and gradual AI adoption. Microsoft AutoGen, an enterprise-focused framework, excels in code execution and sandbox environments, offering strong error handling and reliability features.

CrewAI is increasingly popular for orchestrating multiple AI agents to work together, though it presents integration challenges, such as the need for explicit LLM provider specification and proper environment setup. LangChain, while flexible, can be complex due to its deep class hierarchies and reliance on abstractions, which can complicate customization and integration.

Overall, the development of AI agents involves a careful balance of technical strategies, ethical considerations, and practical frameworks to ensure they are trustworthy, effective, and aligned with human needs. The choice of framework depends on specific project requirements, with options ranging from rapid prototyping with CrewAI to complex, stateful applications with LangGraph. Each framework offers unique strengths, with CrewAI excelling in multi-agent collaboration and LangChain providing a versatile toolkit for a wide range of LLM applications.

## Sources

* 5 Ways To Build a Trustworthy AI Agent - Salesforce : https://www.salesforce.com/blog/trustworthy-AI-agent/
* Best practices for building robust generative AI applications with ... : https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/
* Top 5 Frameworks for Building AI Agents in 2025 : https://www.analyticsvidhya.com/blog/2024/07/ai-agent-frameworks/
* Causes of AI Hallucinations (and Techniques to Reduce Them) : https://weareshaip.medium.com/causes-of-ai-hallucinations-and-techniques-to-reduce-them-235770366357
* AI Hallucinations: Why LLMs Make Things Up (And How to Fix It) : https://futures.webershandwick.com/2024/12/04/ai-hallucinations-why-llms-make-things-up-and-how-to-fix-it/
* Tackling Hallucination in Large Language Models: A Survey of ... - Unite.AI : https://www.unite.ai/tackling-hallucination-in-large-language-models-a-survey-of-cutting-edge-techniques/
* Top 5 Frameworks for Building AI Agents in 2025 : https://www.analyticsvidhya.com/blog/2024/07/ai-agent-frameworks/
* Learnings Comparing AI Agent Frameworks LangGraph, CrewAI, AG, Semantic ... : https://news.ycombinator.com/item?id=42449741
* Top 3 Trending Agentic AI Frameworks: LangGraph vs AutoGen vs Crew AI : https://www.datagrom.com/data-science-machine-learning-ai-blog/langgraph-vs-autogen-vs-crewai-comparison-agentic-ai-frameworks
* Implementing CrewAI: A Deep Dive into LLM Integration Challenges : https://chiraggarg09.medium.com/implementing-crewai-a-deep-dive-into-llm-integration-challenges-6786e594a968
* Top 5 LangChain Implementation Mistakes & Challenges - Skim AI : https://skimai.com/top-5-langchain-implementation-mistakes-challenges/
* CrewAI vs LangChain: The Clash of AI Titans in the LLM Arena : https://medium.com/@cognidownunder/in-the-ever-evolving-world-of-ai-frameworks-two-contenders-have-risen-to-prominence-each-vying-ee511ca7a366
