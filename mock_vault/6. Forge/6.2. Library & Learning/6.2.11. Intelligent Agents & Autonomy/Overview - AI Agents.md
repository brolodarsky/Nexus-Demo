---
aliases: [AI Agents, Agentic Workflows, Autonomous Agents]
tags: [ai-agents, llms, architecture]
type: concept
---
**Back to:** [[Table of Contents]]

---

An **AI Agent** is a system powered by a Large Language Model (LLM) that can autonomously reason through a problem, create a plan, and execute actions using external tools to achieve a predefined goal. Unlike standard conversational AI (chatbots), agents are proactive and capable of altering their environment.

## The Evolution of LLMs

1.  **Standard LLM (e.g., ChatGPT web interface):** You ask a question, the model generates text, the interaction ends.
2.  **RAG System:** The LLM searches a [[Vector Databases|Vector Database]] for documents *before* answering. It is "data-aware" but still reactive.
3.  **Agentic Workflow:** The LLM follows a predefined, programmatic path to achieve an objective. Optimized for predictability and consistency.
4.  **Autonomous Agent:** The LLM dynamically directs its own processes and tool usage based on environmental feedback. Optimized for flexibility and scale.

## Workflows vs. Agents
According to Anthropic's [[Article - Building Effective Agents|Building Effective Agents]], agentic systems fall into two categories:
- **Workflows:** Systems where LLMs and code follow a predefined path. 
- **Agents:** Systems where LLMs use tools in a loop, determining their own steps based on feedback.
*Rule of thumb:* Start with the simplest workflow possible and only increase complexity/autonomy when needed.

## The Core Components of an Agent

According to the famous [Reason + Act (ReAct) paper](https://arxiv.org/abs/2210.03629), an agent consists of three main mechanisms loop:

1.  **Thought:** The internal reasoning step. The LLM analyzes the user's prompt or the current state of its environment and decides what to do next. (e.g., *"The user wants to know the weather in Tokyo. I need to use the weather API tool."*)
2.  **Act:** The LLM outputs a structured command, usually via [[Function Calling & Structured Outputs]]. The host environment intercepts this JSON, executes the local code (e.g., hitting the `OpenWeatherMap API`), and captures the result.
3.  **Observe:** The result of the API call is fed back into the LLM's context window. (e.g., *"{temp: 72F}"*).
4.  *(The LLM returns to step 1 to decide if the goal is met or if another tool is needed).*

## The Foundational Pattern: The Augmented LLM
Every agentic system (workflow or agent) is an **Augmented LLM**. It consists of a base model enhanced by three core capabilities:
1.  **Retrieval:** Contextual data from a Knowledge Base or AFS.
2.  **Tools:** External capabilities (APIs, web browsers, local CLI).
3.  **Memory:** Persistence of past actions, thoughts, and user preferences.

## Agent Architectures

Beyond basic ReAct loops, complex agents use advanced cognitive architectures.

*   **Plan-and-Solve:** The agent first outputs an explicit, multi-step plan before taking *any* action. Once the plan is finalized, it executes the steps sequentially.
*   **Reflexion:** The agent acts, observes the result, and then explicitly generates a critique of its own performance (*"I failed to find the file because I searched the wrong directory"*). It then updates its internal context and tries again.
*   [[Multi-Agent Systems & Orchestration]]: The most advanced paradigm, where a "Manager" agent delegates discrete tasks to narrowly scoped "Worker" agents (e.g., a Coder, a Reviewer, and a Tester).

## Agentic Prompt Architecture: Context vs. Attention

A critical challenge in agent design is managing the **"Lost in the Middle" phenomenon** (attention degradation).

*   **Context Limit vs. Attention Limit:** While modern LLMs have massive context windows (1M+ tokens) and can physically ingest an entire codebase or instruction manual, their *attention* is finite. If an agent is fed a master system prompt with 100 rules, it will suffer from primacy bias (hyper-focusing on the first 10 rules) and recency bias (focusing on the last 10), often completely ignoring the rules in the middle of the document.
*   **The Solution (Dynamic Prompting / Lazy-Loading):** The industry best practice is a "RAG-like" approach to agentic instructions, but relies on **deterministic file reading** rather than fuzzy vector math.
    *   The **Global System Prompt** (the "Constitution") is kept extremely rigid and short—only containing catastrophic-failure-prevention rules and non-negotiable architectural laws.
    *   **Specific Skills & Workflows** are kept in separate `.md` or `.json` files. The agent is taught the *names* of these skills, but it must use a tool to dynamically read the specific instructions only at the exact moment it needs them.
    *   This forces the highly granular instructions to the very bottom of the context window right before execution, weaponizing recency bias in the developer's favor.

## Agentic Memory: RAG vs. The Agentic File System (AFS)

A critical distinction in agent architecture is deciding *how* an agent reads its environment. The vault acts as both human memory and machine config, turning it into an **Agentic File System (AFS)**, but agents must access data correctly based on intent:

*   **RAG (Fuzzy Search):** Use Vector Databases when the agent is querying *data* where the location is unknown or the query is semantic (e.g., "What patterns exist in my medical logs regarding abdominal pain?"). RAG is probabilistic; it guesses the best chunks.
*   **Direct File Reading (Deterministic Policy):** Use absolute path reads when the agent is accessing *instructions* or *standards* (e.g., an Agent Builder reading `6.2.11 Intelligent Agents.md` to learn how to write a LangGraph node). The agent shouldn't guess what the rules are; it must ingest the whole document perfectly via file I/O tools just before execution.

### The AFS Multi-Agent Loop
By treating the markdown vault as an AFS, agents can communicate asynchronously without ever passing direct context to each other:
1. **The Synthesizer** (e.g., `/distill_learning` agent) parses a new research paper and updates a standard operating procedure (SOP) note in the Vault.
2. **The Implementer** (e.g., an Agent Builder or Coder agent) is run weeks later. Embedded in its prompt is a sequence to use `read_file()` on that specific SOP note.
3. It seamlessly acts on the most bleeding-edge, human-reviewed standard without requiring any hardcoded prompt updates by the developer.

## Instruction Architecture Failure Modes

Beyond attention degradation, a subtler failure mode exists: **conflicting or overlapping rules** — where a positive trigger in one rule and a negative constraint in another rule cover the same action boundary.

### The Prose Rule Problem
When two separate prose rules govern overlapping territory, models exhibit a reliable failure pattern:
1. **Positive trigger wins.** The model latches onto the rule that tells it *what to do* (e.g., "commit TOC changes") and suppresses the negative constraint in a different rule (e.g., "but not for note links").
2. **Subordinate clauses are skipped.** A "do NOT do X" buried mid-paragraph — especially after a comma, em-dash, or "however" — is architecturally weaker than an explicit negative in a parallel structure.
3. **Co-location failure.** If the positive trigger and its exception live in *different rules*, the model may never reconcile them — it simply acts on whichever it matched first.

### Decision Tables as a Solution
For **binary policy decisions** (commit or don't commit, changelog or not), a structured decision table is more robust than prose:

| Why it works | Mechanism |
| :--- | :--- |
| Parallel structure | Every row is evaluated equally; ❌ rows carry the same visual weight as ✅ rows |
| No buried clauses | Negatives are explicit columns, not subordinate phrases |
| Single lookup point | Model reads one table instead of cross-referencing multiple rules |
| Exhaustive enumeration | Edge cases are forced into named rows rather than left implicit |

**Rule of thumb:** Use prose for nuanced reasoning and edge cases. Use decision tables for any policy where ambiguity maps directly to incorrect system behavior.

*Empirically observed in Nexus `AGENTS.md` refactor, 2026-04-12. See [[Journal 2026#2026-04-12 — Agentic Instruction Design: Tables Beat Prose|journal entry]].*

### Context Bloat vs. Portability (The Dual Source of Truth)
When designing agentic systems, there is a natural tension between **Agentic Efficiency** (which prefers auto-loading modular skill files and stripping the main Constitution down to avoid token bloat) and **System Portability** (which prefers a monolithic document so the rules can be copy-pasted into any standard, non-agentic LLM like ChatGPT).

If you prune your Constitution to rely purely on IDE auto-loading, your repo instructions become unreadable outside of that specific IDE. If you lean too heavily on manually maintaining a monolithic `AGENTS.md`, you create a **Dual Source of Truth problem**: you update a specific skill file, but forget to update its summary in the Constitution, causing the LLM to receive conflicting instructions.

**The Solution (The Compiled Portability Architecture):**
Treat the monolithic system prompt (the Constitution) as a **compiled artifact** rather than a manually edited file. 
- **No Manual Edits:** The lists of skills and workflows in the Constitution should be wrapped in strict `<!-- AUTO-COMPILED -->` warnings.
- **The CI/CD Agent Pipeline:** Delegate a specific "documentation maintaining" agentic skill to trigger whenever a workflow or skill is modified. This skill scrapes the YAML frontmatter of the modular files and overwrites the Constitution verbatim.
This ensures that inside the IDE, instructions never drift, and outside the IDE, you still have a perfectly synced, monolithic master document to paste anywhere.

## Agent Tools ("Hands")

Agents interact with the world via defined tools.
*   **Web Browsing:** Using tools like Playwright or Puppeteer to navigate the DOM, click buttons, and scrape text.
*   **Bash / CLI Execution:** Running Python scripts, managing files, and compiling code.
*   **APIs:** Connecting to Slack, GitHub, Jira, or proprietary databases. 
    *   *Note:* The emerging standard for organizing these tools universally is the [[Concept - Model Context Protocol (MCP)]].

## Agent-Computer Interface (ACI)
Success in agentic systems often depends more on the **interface** provided to the model than the prompt itself (See: [[Article - Building Effective Agents#Appendix Tool Engineering Best Practices|Building Effective Agents: ACI]]). 
- **HCI vs. ACI:** Developers should invest as much effort into the Agent-Computer Interface (ACI) as they do into Human-Computer Interfaces (HCI).
- **Optimization:** Anthropic found that optimizing tool schemas and documentation often yields better results than optimizing the master prompt.
- **Absolute Paths:** Models often struggle with relative file paths during multi-step navigation. Forcing absolute paths in tool definitions increases reliability.

## Prototyping & Designing Agentic Workflows

Designing autonomous systems requires moving from "linear prompts" to "graph logic." Industry standards for tinkering and prototyping include:

*   **Conceptual Mapping (Low Fidelity):**
    *   **Whiteboarding & Excalidraw:** Essential for mapping messy state transitions and edge cases.
    *   **[[Concept - Mermaid.js|Mermaid Diagrams]]:** The "Pro" standard for version-controlled logic. Writing graph logic in Mermaid allows the diagram to live alongside the code/notes.
*   **Implementation & Debugging (High Fidelity):**
    *   **[[LangGraph]] + [[LangSmith]]:** The gold standard for state-machine design. LangSmith provides visual traces of every node execution, allowing developers to see exactly where a "reasoning loop" or "tool failure" occurred.
    *   **Playgrounds:** Using LangSmith or OpenAI/Anthropic playgrounds to isolate and tinker with specific node prompts without re-running the entire expensive graph.
*   **Rapid Policy Engineering:**
    *   **Markdown Workflows:** Using structured `.md` files to define agent logic before writing a single line of Python. This allows for "Agent-in-the-loop" testing where a developer has a meta-agent (like Antigravity) execute the markdown steps manually to see if the logic holds.
*   **Iterative Testing:**
    *   **Jupyter Notebooks:** Used to test individual graph nodes (e.g., just the `retrieve` node) in isolation to optimize performance before production deployment.

## Agentic Operations (AgentOps) & Maintenance Debt

Just like RAG systems, autonomous agents suffer from unique forms of "Engine Rot" that require active maintenance:

*   **Tool Schema Drift:** Agents depend entirely on external APIs and CLI tools. If a third-party API changes its response payload structure (even slightly), the agent's parsing logic will break. Active monitoring of all tools in the agent's arsenal is required.
*   **Reasoning Drift (Model Updates):** Agentic workflows are highly coupled to a specific model's reasoning behaviors. An under-the-hood tweak to `gpt-4o` or `Claude 3.5` might make the model more likely to skip a planning step or misuse a tool. Any base model update requires re-running a benchmark suite of expected agent behaviors.
*   **Framework Churn:** Orchestrators like LangGraph and AutoGen evolve rapidly. Breaking changes in state management or edge-routing are common, requiring regular dependency maintenance.
*   **Token Bloat & Infinite Loops:** Agents run in recursive loops. A subtle bug introduced into the prompt can cause an agent to get stuck in an "Action/Observation" loop, burning API credits. Regular audits of token-usage-per-workflow and hard fail-safes (e.g., `recursion_limit=10`) must be maintained.

## Future of Work & Strategy
*   **[[Synthesis - AI Superagency & The Future of Work]]:** Detailed exploration of the "Agentic Leap," four economic scenarios for 2030, and the new skills economy (WEF, IMF, McKinsey research).

## Further Resources
*   [IBM: AI Agents Explained](https://www.ibm.com/think/ai-agents)
*   [Sequoia Capital: AI Agents Landscape](https://www.sequoiacap.com/article/ai-agents/)
*   [The AI Agent Stack](https://www.theaiagentstack.com/)

## Lessons from the Forge (2026)

Empirical observations from building local agentic workflows within Nexus.

### 1. The Model Non-Determinism Trap
Model selection is a development-time architectural decision. During the first ReAct sprint (2026-04-16), a switch from `gpt-5.4-nano` to `gpt-4o-mini` fundamentally changed system reliability.
- **Base/Predictive Models:** Often exhibit "Over-generation"—they predict the next turn of the conversation and try to finish the loop themselves, leading to hallucinated observations.
- **Tuned Chat Models:** More "polite" instruction-followers that respect the "PAUSE" command even without a hard API limit.

### 2. Mandatory Stop Sequences
In a non-deterministic agentic loop, you cannot rely on the model "knowing when to stop."
- **Technique:** Always implement a hard `stop=["PAUSE"]` parameter in the API call.
- **Fail-safe:** If the API provider doesn't support the `stop` parameter (common in experimental variants), implement **Manual Truncation** by slicing the result string at the first instance of the stop keyword: `result.split("PAUSE")[0] + "PAUSE"`.

### 3. Regex vs. Structured Tool Calls
While the ReAct paper uses plain text parsing (`Action: method: input`), modern production agents should pivot to **Native Function Calling**. This eliminates the need for complex regex patterns and prevents the agent from breaking when the model adds a single unexpected space or character to its thought block.

*See [[2026 - Journal#16 — The First Agentic Sprint & The "Freedom Fund" Reality|journal entry]] for the personal context of these builds.*

