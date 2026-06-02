# Nexus Agentic Engine Demo

## Overview
This repository contains a demonstration of the Nexus Agentic Engine, fulfilling the requirements for the take-home interview project. It features a system of three specialized agents that collaborate to route user requests, fetch live data, and reason over domain-specific contexts.

## Design Architecture
The system is built around a **Three-Agent Pipeline** using LangGraph, demonstrating cross-domain orchestration and the compiled subgraph pattern:

1. **Content Router Agent (The Entry Point)**
   - Acts as a classifier and dispatcher for incoming user requests.
   - It assesses the intent of the prompt and routes it to the appropriate domain agent.

2. **Email Agent (I/O Subgraph)**
   - A compiled subgraph dedicated to external data ingestion.
   - When the Router detects a need to check emails, it delegates to the Email Agent, which securely interfaces with Gmail (via IMAP/OAuth2) to fetch structured data and returns it to the Router for classification.

3. **Career Agent (Domain Reasoning & Execution)**
   - A highly specialized agent for handling career and professional requests.
   - It utilizes **Deterministic Pre-flight Hydration (DPFH)** to receive relevant local contexts before running.
   - When it requires information outside its domain, it seamlessly delegates to a `Librarian` subgraph to retrieve cross-domain insights without violating boundaries.
   - Writes are governed by a **Human-in-the-Loop (HITL)** SQLite queue to ensure data integrity.

## Evaluation Approach
Ensuring the reliability and groundedness of the agent ecosystem is critical. Our evaluation methodology focuses on verifiable outcomes over raw LLM vibes:

- **Golden Datasets**: We maintain a `dataset.json` comprising representative questions and expected ground-truth answers mapped to specific source files within the Vault structure.
- **LLM-as-a-Judge**: We utilize an automated evaluation runner (`engine/agents/librarian/evals/runner.py`) powered by a strict evaluator LLM (Temperature 0.0). The evaluator grades the agent's final output against the Golden Dataset using three criteria:
  1. **Accuracy**: Does it match the expected answer?
  2. **Groundedness**: Did the agent actually invoke the correct tools to read the targeted source files?
  3. **Hallucination Penalty**: Did the agent fabricate information not present in the files?
- **Execution Tracing**: All evaluations capture full tool-call traces, latency metrics, and token usage to identify regressions and optimize subgraph efficiency.

## Future Improvements
Given more time, here are the key enhancements I would implement:

1. **Vector-Backed Semantic Search**: Currently, the system relies heavily on deterministic file-system traversal. Integrating a localized vector database (like Chroma or FAISS) would significantly improve the Librarian subgraph's ability to perform fuzzy semantic searches across unstructured notes.
2. **Parallel Agent Execution**: The current router dispatches sequentially. For multi-faceted queries (e.g., "Check my emails for jobs and also tell me what my health regimen is"), spinning up the Career Agent and a Health Agent concurrently and merging their outputs would reduce latency.
3. **Streaming Responses**: Implement streaming token outputs from the LangGraph agents to improve perceived latency for the end-user, particularly during deep-reasoning steps in the Career Agent.
4. **Agent Self-Correction Loops**: Incorporate reflection nodes within the domain subgraphs. If an agent fails to find a file or hallucinates, a critique node could catch the error and force the agent to retry its tool calls before returning the final answer to the user.
5. **Richer Mock Vault**: Expand the `mock_vault` to include highly complex, ambiguous edge cases to further stress-test the router's classification bounds.
