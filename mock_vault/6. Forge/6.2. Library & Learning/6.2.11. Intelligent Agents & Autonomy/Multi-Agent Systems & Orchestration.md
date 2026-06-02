---
aliases: [Multi-Agent Systems, MAS, Agent Orchestration, Frameworks & Multi-Agent Swarms]
tags: [ai-agents, architecture, orchestration, career-strategy]
type: architecture
---

**Back to:** [[Table of Contents#Frameworks & Multi-Agent Swarms|TOC]]

Multi-Agent Systems (MAS) represent the evolution from single, conversational LLMs into distributed problem-solving networks. Instead of one monolithic model trying to do everything, a multi-agent system divides complex tasks among specialized, autonomous "agents" that communicate and collaborate to achieve a goal.

## 1. The Strategic Framework Spectrum

Choosing a framework is a **strategic career decision**. It determines whether you are hired as a low-level architect, a high-level manager, or a rapid-mvp hacker.

| Category | Typical Tools | Persona | Competitive Advantage |
| :--- | :--- | :--- | :--- |
| **Low-Level Control** | **LangGraph**, PydanticAI | **The Architect** | **Precision & Sovereignty.** Complete control over state transitions and persistence. Built for production durability. |
| **High-Level Magic** | **CrewAI**, AutoGen | **The Manager** | **Velocity & Role-Play.** Focuses on "Agents" as employees with roles and goals. Best for complex content pipelines. |
| **No-Code / Low-Code** | **Gumloop**, Zapier | **The Hacker** | **Business ROI.** Fastest path to a working product. Ideal for freelancing and rapid business automation. |

---

## 2. Core Architectures & Roles (The Theory)

Instead of one monolithic model trying to do everything, MAS divides tasks among specialized, autonomous "agents" to solve **Context Degradation** and **Tool Overload**.

### A. The Orchestrator (The Manager)
*   **Role:** The "Boss" agent. It takes the user's initial high-level request, breaks it down into sub-tasks (a plan), and delegates those tasks to subordinate agents. 
*   **Capabilities:** It rarely has tools (like web search) itself. Its only "tool" is routing communication to other agents and synthesizing their final answers for the user.
*   **Example Prompt:** *"You are the Project Manager. Review the user's request, delegate research tasks to the 'Researcher', then send the research to the 'Writer'. Finally, present the Writer's output to the user."*

### B. Specialized Workers
*   **Role:** The specific agents that actually execute tasks. They have very narrow system prompts and a limited set of tools (e.g., a "Researcher" with search tools vs. a "Coder" with terminal access).

### C. Reviewers (The Critics)
*   **Role:** Agents designed purely to critique the work of Worker agents before passing the result back to the Orchestrator. This implements "Reflexion" to ensure quality.

---

## 3. Design Patterns (How They Talk)

*   **Sequential / Waterfall:** Agent A finishes its task completely, then passes the output to Agent B. (E.g., Researcher -> Writer -> Editor).
*   **Hierarchical:** The Orchestrator acts like a router, dynamically sending tasks to workers based on the evolving state of the conversation.
*   **Joint / Swarm:** Peer-to-peer handoffs. Agents hand off tasks directly to more qualified peers based on predefined rules.

---

## 4. Specific Workflow Patterns (Anthropic)
The following patterns are documented by Anthropic in [[Article - Building Effective Agents|Building Effective Agents]] as the building blocks of effective systems:

1.  **Prompt Chaining:** Decomposing a task into a sequence of steps, where each LLM call processes the output of the previous one. (Ideal for fixed subtasks).
2.  **Routing:** Classifying an input and directing it to a specialized followup task. (Separation of concerns).
3.  **Parallelization:** LLMs working simultaneously on a task.
    *   **Sectioning:** Breaking a task into independent subtasks.
    *   **Voting:** Running the same task multiple times for confidence.
4.  **Orchestrator-Workers:** A central LLM dynamically breaks down a task, delegates to workers, and synthesizes results. (Best for unpredictable subtasks).
5.  **Evaluator-Optimizer:** An iterative loop where one LLM generates a response and another provides feedback/critique. (Best for iterative refinement).

---

## 5. Selection Matrix: When to Use What

| If the goal is... | Use... | Reason |
| :--- | :--- | :--- |
| **Enterprise SaaS** | **LangGraph** | Requires strict "Guardrails" and Human-in-the-loop checkpoints. |
| **Complex Research Output** | **CrewAI** | Inherently handles "sequential" tasks with role-based nuance. |
| **Quick Freelance Gigs** | **Gumloop** | Speed of deployment = Higher hourly profit. |
| **Academic Simulations** | **AutoGen** | Best for exploring emergent behaviors in agent conversations. |

---

## 5. Further Insights
- [[Overview - AI Agents]]: The foundational mechanics of the ReAct loop.
- [[Synthesis - AI Superagency & The Future of Work]]: Economic impact and the "Freedom Fund" strategy.
- [[2026 - Journal#16 — The First Agentic Sprint & The "Freedom Fund" Reality|Journal: Choosing LangGraph over the "Unicorn" job offer.]]

