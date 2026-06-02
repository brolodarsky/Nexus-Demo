---
aliases: [Anthropic Building Effective Agents, Agentic Design Patterns]
tags: [ai-agents, architecture, anthropic, engineering]
type: source
---
# Article - Building Effective Agents (Anthropic Engineering)

**Source:** [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
**Published:** 2024
**Back to:** [[6.2.11. Intelligent Agents & Autonomy]]

## Summary
Anthropic's guide to building production-grade agents, focusing on simple, composable patterns over complex frameworks. It establishes a distinction between **Workflows** and **Agents** and identifies five core design patterns for agentic systems.

## Key Distinctions
- **Workflows:** Systems where LLMs and code follow a predefined path. Optimized for predictability and consistency.
- **Agents:** Systems where LLMs dynamically direct their own processes and tool usage based on environmental feedback. Optimized for flexibility and scale.

## The Foundational Pattern: The Augmented LLM
Every agentic system starts with an LLM enhanced by:
- **Retrieval:** Contextual data.
- **Tools:** External capabilities (APIs, code execution).
- **Memory:** Context retention.

## Core Workflow Patterns
1. **Prompt Chaining:** Decomposing a task into a sequence of steps.
2. **Routing:** Classifying input and directing it to specialized subtasks.
3. **Parallelization:** Running multiple LLM calls simultaneously (Sectioning or Voting/Aggregation).
4. **Orchestrator-Workers:** A central LLM dynamically delegates to specialized workers and synthesizes results.
5. **Evaluator-Optimizer:** An iterative loop where one LLM generates and another critiques/refines.

## The Agent Pattern
- Used for open-ended problems where steps cannot be predicted.
- Relies on **environmental feedback** (tool results, code execution) in a loop.
- **When to use:** When you can't hardcode a fixed path and have high trust in the model's decision-making.

## Engineering Principles
- **Maintain Simplicity:** Start with single prompts; add complexity only when it demonstrably improves outcomes.
- **Transparent Abstractions:** Avoid heavy frameworks that obscure underlying prompts.
- **Agent-Computer Interface (ACI):** Invest in tool design (absolute paths, simple structures, clear documentation) just as much as human interfaces (HCI).
- **Control:** Use Human-in-the-loop (HITL) checkpoints for high-stakes tasks.

## Appendix: Tool Engineering Best Practices
- Prefer absolute file paths over relative ones (avoiding model confusion during navigation).
- Use simple, well-documented tool schemas.
- Optimize the toolset documentation more than the overall prompt.
