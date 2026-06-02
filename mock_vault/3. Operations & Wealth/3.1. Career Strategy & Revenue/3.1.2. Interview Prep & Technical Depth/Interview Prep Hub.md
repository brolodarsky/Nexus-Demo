---
aliases: [Interview Prep, Tech Interview, Interview Bank]
tags: [career, interview, strategy]
type: overview
---
**Back to:** [[Table of Contents]]

---

> [!NOTE]
> This is the central hub for all interview preparation. Link specific prep notes, practice logs, and question banks here as they are created.

## Coding & Data Structures

### Pattern Cheat Sheet
- **Two Pointers / Sliding Window:** Subarray sums, palindrome checks, container problems.
- **BFS / DFS:** Graph traversal, tree problems, shortest path.
- **Dynamic Programming:** Memoization vs. tabulation, common sub-problems (knapsack, LCS, coin change).
- **Hash Maps & Sets:** Frequency counting, two-sum patterns, anagram detection.
- **Stacks & Queues:** Monotonic stacks, bracket matching, BFS via queue.

### Python-Specific Gotchas
- Default mutable arguments (`def f(x=[])` — never do this).
- `collections` module: `defaultdict`, `Counter`, `deque`.
- List comprehension vs. generator expression performance.
- `heapq` for priority queues (min-heap only — negate for max-heap).

### Practice Platforms
- [LeetCode](https://leetcode.com/) — Primary grinding platform.
- [NeetCode 150](https://neetcode.io/practice) — Curated, pattern-grouped problem set.
- [HackerRank](https://www.hackerrank.com/) — Company-specific assessments.

---

## System Design

### Standard Distributed Systems Checklist
- Load balancing, horizontal scaling, caching (Redis/Memcached).
- Database sharding, replication, CAP theorem trade-offs.
- Message queues (Kafka, RabbitMQ), event-driven architecture.
- API gateway patterns, rate limiting, circuit breakers.

### AI-Specific Design Questions
- **"Design a RAG Pipeline":** Chunking strategy → embedding model → [[Vector Databases|vector store]] → retrieval → re-ranking → generation → evaluation loop.
- **"Design a Multi-Agent System":** Orchestrator pattern, tool routing, memory (short-term vs. long-term), guardrails, human-in-the-loop escalation.
- **"Design a Content Moderation API":** Classifier cascade, confidence thresholds, human review queue, feedback loop for model improvement.
- **"Design an LLM Serving Infrastructure":** Model hosting (vLLM/TGI), batching, KV-cache, autoscaling, cost per token tracking.

---

## Behavioral Q&A Bank (STAR Format)

> [!TIP]
> Pre-write 5–7 stories and map them to multiple question types. One strong story can answer "leadership," "conflict," and "failure" questions with different framing.

### Leadership / Ownership
- **Situation:** Building [[Project Feeder|Feeder]] as a solo full-stack project — nutrition optimization with AI.
- **Task:** Architected the entire system: database, API, LLM integration, and [[Python]] automation.
- **Action:** Designed modular components, set up CI/CD, wrote tests, iterated on UX.
- **Result:** Working application that demonstrates end-to-end engineering ownership.

### Problem Solving Under Ambiguity
- **Situation:** Mother's LCSW billing practice had no digital system — manual claims, lost revenue.
- **Task:** Automate billing without a budget for commercial software.
- **Action:** Built [[Project MEM Billing]] — custom [[Python]] scripts for claim generation and tracking.
- **Result:** Eliminated manual errors, recovered billable hours, and demonstrated real-world automation impact.

### Technical Depth / AI Experience
- **Situation:** Working as an AI Rater at $50/hr — evaluating LLM outputs for quality and safety.
- **Task:** Consistently assess non-deterministic AI outputs with precision and nuance.
- **Action:** Developed personal evaluation frameworks, pattern-matched failure modes across thousands of outputs.
- **Result:** Deep "under-the-hood" understanding of LLM behavior — a rare skill for engineering roles.

### Failure / Learning
- *(Draft a specific failure story — e.g., a project that stalled and what you learned.)*

### Conflict Resolution
- *(Draft a story about navigating disagreement — technical or interpersonal.)*

### The "AI Automation" Question (Why Hire You?)
- **Question:** "With tools like GitHub Copilot and Cursor, why should we hire a junior engineer?"
- **Situation:** The industry is seeing massive wage compression and task displacement for pure execution roles.
- **Task:** Differentiate from a "boilerplate coder."
- **Action:** Frame yourself as an **Agent Orchestrator**. Discuss evaluating non-deterministic outputs from your AI Rating job, designing multi-step agentic workflows in Nexus.0, and solving complex domain problems rather than just churning out syntax.
- **Result:** You bring judgment, human-in-the-loop evaluation, and systems thinking—skills AI cannot currently replicate.

---

## AI/LLM Interview Patterns by Role

### Agentic Architect
- Expect questions on: [[Overview - AI Agents|agent]] loop design (ReAct, Plan-and-Solve), tool orchestration, guardrails, memory systems.
- Demonstrate: Nexus.0 as an agentic workflow system, your AGENTS.md config approach.

### RAG Engineer
- Expect questions on: chunking strategies, embedding model selection, retrieval metrics (MRR, recall@k), re-ranking, hallucination mitigation.
- Demonstrate: Understanding of [[Retrieval Augmented Generation (RAG)]], [[Vector Databases]] experience.

### AI Evaluator / Safety Engineer
- Expect questions on: evaluation benchmarks (SWE-bench, MMLU), prompt injection defense, red-teaming, RLHF pipelines.
- Demonstrate: Hands-on AI rating experience, pattern recognition for LLM failure modes.

---

## Digital Presence & LinkedIn Optimization
*(Source: [[Article - Robert Half Job Search Strategies Guide 2026|Robert Half 2026]])*

### The LinkedIn Profile Checklist
- **Keyword-Rich Headline:** Go beyond your title. (e.g., "Full Stack Engineer | AI Agent Orchestration | Python Specialist").
- **Unique Value Summary:** Don't copy your resume; tell the story of the problems you solve.
- **Featured Section:** Pin your best *deployed* projects (like [[Project Feeder|Feeder]]) or evidence of technical depth.
- **Active Signal:** Like, share, or comment weekly. A "quiet" profile looks stale to recruiters.

### ATS & AI Gatekeeper Optimization
- **Simple Formatting:** No complex tables or multi-column layouts; use standard text-based PDF/Word docs.
- **Semantic Matching:** Mirror the *exact* skills listed in the job post (e.g., if they say "Generative AI" and you have "LLM Experience," list both).
- **AI Interview Pacing:** Practice with simulators to manage response timing and keyword hit-rates.

---

## Resources
- [[Interview Question Bank]] — Repository of pre-written application responses.
- [[Article - Robert Half Job Search Strategies Guide 2026]] — Strategic market insights.
- [[My Skills]] — Source of truth for technical skill claims.
- [[Job Hunt War Room]] — Active hunt strategy and target roles.
- [[Employer Skill Requirements]] — What companies are actually asking for.
