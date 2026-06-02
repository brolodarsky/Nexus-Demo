---
aliases: [AI Agents in LangGraph Course, LangGraph Transcript]
tags: [agentic, learning, langgraph, capture, transcript]
type: capture
---
**Back to:** [[Table of Contents#6.1.2. Agentic R&D|TOC]] | [[Course Overview- AI Agents In LangGraph]] | [[Current Learning]]

## DeepLearning.AI: AI Agents in LangGraph Course
**URL:** [AI Agents in LangGraph | DeepLearning.ai](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/qyrpc/introduction)

### Module 1: Introduction
- Agents need predictable formats for results.
- Agentic workflow - iterate to produce a work product. Contrasts with singe LLM chat.
- Key design patterns: Planning, tool use, reflection, multi-agent communication, memory.
- Many capabilities implemented outside LLM, inside framework agents built in.
- Memory comes in many forms.
- Example agent workflows: ReAct agents, Self Refine paper, AlphaCodium (flow engineering). 
	- All defined b cyclical graphs.
	- LangChain to LangGraph.
- Search tools are a major part of most applications. "Agentic search"
- Important capabilities: receiving human input & persistence (store current state of info).

### Module 2: Build an Agent from Scratch
- Some jobs fall to LLM, other around it (the Runtime/the wrapper)
- Building ReAct pattern type of agent. Thinks, then acts, observation returned, LLM repeats.
- "System prompt" includes ReAct protocol instructions. 
- Actual tools (e.g. python scripts) available to agent (and given a list inside system prompt)
- Manual run through first, then automated ReAct loop. Here uses regex to find "Action: method: input" into LLM's response to check if still running actions, otherwise finishes.

### Module 3: LangGraph Components (State, Nodes, Edges)
- Prompt Templates: Reusable prompts, often with injectable variables based on user content.
- Tools
	- Tavily (search)
- Graphs (cyclic, persistence, HIL)
	- LangGraph is extension of LangChain for agent and multi-agent controlled flows
	- Nodes (agents or functions), Edges, Conditional edges (decisions)
	- Data/State (AgentState)
		- Accessible at all parts of graph, local to graph, can be stored in a persistence layer
		- Usually TypedDict
			- Non-annotated/updates overwrite: e.g. input, agent_outcome
			- Intermediate_steps: annotated/updated/appended/tracked overtime

### Module 4: Agentic Search Tools
- Tavily: Web search agentic tool.
- ![[Pasted image 20260511201954.png|317]]
- ![[Pasted image 20260511202030.png|487]]

### Module 5: Persistence & Streaming
- Long running tasks need persistence and streaming.
- Streaming: emit signals to tell what's going on at a given moment.
- LangGraph checkpointer - checks the state at every node. Uses SQLite

### Module 6: Memory & Threading
- 

### Module 7: Human-in-the-Loop
- 


