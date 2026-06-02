---
aliases: [Career Agent, Agentic Career, Job Hunt Agent]
tags: [ai-agents, projects, career, langgraph, automation]
type: overview
---
**Engine Directory:** `engine/agents/career`

**Back to:** [[Table of Contents#6.1.2. Agentic R&D|TOC]] | [[Project - Nexus Agentic Engine]]

## 1. Overview & Vision
The **Career Agent** is a domain-specialized LangGraph agent responsible for proactive career automation within the **Nexus Agentic Engine**. It autonomously tracks opportunities, updates master materials, manages network connections, and provides high-stakes strategic advice. 

By natively operating on the Agentic File System (AFS), it treats the `Vault/3. Operations & Wealth/3.1. Career Strategy & Revenue/` directory as its local memory and workspace. It migrates legacy agentic instructions (`career_counselor`, `add_job_requirement`, `render_resume`) into a robust, autonomous state machine.

---

## 2. Architectural Integration (Nexus Agentic Engine)
The Career Agent does not operate in a vacuum. It is deeply integrated into the broader multi-agent architecture of the Brain.

- **Deterministic Pre-flight Hydration (DPFH):** Before every LLM node execution, a deterministic Python function (`os.listdir`) scans the Career domain folder. The agent also declares a `required_context` list (e.g., [[My Skills]], [[Employer Skill Requirements]], [[Job Hunt War Room]]) which is injected directly into its system prompt. This ensures zero-cost, hallucination-free awareness of its domain.
- **Librarian Escalation (Cross-Domain Context):** The Career Agent is strictly bounded to the `3.1. Career/` folder. If it needs cross-domain context (e.g., checking energy levels or burnout protocols from `2. Health/` to recommend sustainable job roles), it delegates a query via the `ask_librarian()` tool. It never reads other domains directly.
- **HITL Transaction Queue (Two-Phase Commit):** The agent cannot irreversibly alter the Vault or send emails on its own. All proposed writes (e.g., updating [[Resume - Master]]) or outgoing communications are placed in the `pending_actions` SQLite queue. The user reviews these via the **Engine Control Panel (GUI)** diff-viewer or inline Telegram buttons (`[Approve]` / `[Reject]`) before they are committed to the AFS.
- **Memory Tiers:** 
  - **Working Memory:** Short-term LangGraph state used during a specific job scraping or resume-tailoring run. Wiped after completion.
  - **Episodic Memory:** Timestamped decision logs (e.g., "Agent decided to skip applying to Company X due to skill gap in Y") stored in `Logs/Agent Decisions/`.
  - **Procedural Memory:** Learned preferences. If the user repeatedly rejects the agent's suggestion to include a specific bullet point, the agent writes this preference to `lessons_learned.jsonl` and consults it on future runs.
- **Evaluator-Optimizer & Reflection Loop:** After completing a complex task (like drafting a cover letter), a distinct `reflection` node reviews the output against [[My Skills]] to check for hallucinations or tool misuse before submitting it to the HITL queue.
- **Local Task Management & Master Sync:** The Career Agent maintains its own `To Do - Career Agent.md` within the `3.1. Career/` directory. It registers discovered tasks (e.g., skill gaps to study, target applications to follow up on) locally and syncs them bi-directionally with the master [[To Do List]] under the Career section (running all updates through the HITL queue).

---

## 3. Core Capabilities (Legacy Ports & Enhancements)

### 3.1. Job Ingestion & Market Alignment (`add_job_requirement` port)
- **Multi-modal Job Parsing:** Autonomously extracts required skills, tech stacks, and cultural indicators from job descriptions provided via URL, PDF, or raw text (using vision/scraping tools).
- **Market Knowledge Base Update:** Appends extracted skills to [[Employer Skill Requirements]] and regenerates the high-level AI Summary for Career Strategy.
- **Pipeline Tracking:** Automatically adds the target company and role metadata to the correct industry vertical in [[Job Hunt War Room]] Section 4.
- **Skill Gap Analysis:** Cross-references the extracted requirements against [[My Skills]] to score the fit. It proactively flags gaps and routes actionable study plans to [[Current Learning]] and the [[To Do List]].
- **Archiving:** Saves a complete, structured markdown copy of the raw job posting in `Vault/3. Operations & Wealth/3.3. Career Strategy & Revenue/Saved Job Listings/` to guard against link rot.

### 3.2. Autonomous Document Engineering (`render_resume` port)
- **Dynamic PDF/DOCX Rendering:** Wraps the local `resume-engine` tool to render markdown resumes and cover letters from the [[Portfolio Hub]] into professionally styled, ATS-friendly files.
- **Agentic Formatting Optimization:** The agent receives exact page fill metrics (fill %, verdict, room remaining) directly from the render engine. It runs in an automated loop: if a resume is at 105% fill, the agent will autonomously trim specific bullet points or re-word phrases to achieve an optimal 100% single-page fit.
- **Targeted Generation:** Drafts highly tailored outreach messages, recruiter DMs, and custom cover letters optimized for the specific job description parsed in Step 3.1.
- **Resume Tailoring Protocol:** Given a job description, the agent reads `Resume - Master.md` via the `get_master_resume()` tool, crafts a tailored resume version (reordering bullet points, adjusting the Summary, incorporating ATS keywords), and proposes it via HITL as a new file (e.g., `Resume - Spotify AI Engineer.md`). Never fabricates skills — only rearranges and rewords existing content.

### 3.3. High-Stakes Strategy & Advising (`career_counselor` port)
- **Strategic Architect:** Acts as an on-demand, non-sycophantic career advisor via the Telegram bot or Control Panel chat interface.
- **Portfolio Audits:** Recommends structural or narrative changes to the professional portfolio based on evolving market trends (e.g., "MTEB benchmarks are trending, you should highlight your RAG evaluation pipeline").

---

## 4. Advanced Autonomous Features

### 4.1. Portfolio & Resume Syncer (Daily Telemetry Automation)
- **Telemetry Compilation:** Utilizes `tools/collect_telemetry.py` to compile daily Git commit diffs, Vault updates, and local evaluation test reports into a structured `0. Inbox/Daily Activity Log - YYYY-MM-DD.md`.
- **Asset Updates:** The Career Agent ingests these daily activity logs on a cron schedule, cross-references them with [[My Skills]], and drafts proposed granular updates to [[Portfolio Hub]] and [[Resume - Master]]. 
- **Platform Sync Notifications:** If the agent detects that `Resume - Master` has been updated and approved, it immediately queues a reminder to update external platforms (LinkedIn, Handshake, Wellfound).

### 4.2. Professional CRM & Networking Orchestration
- **Relationship Scanning:** Scans the `0. Inbox/` (fed by `tools/read_email.py` and social capture) for networking conversations.
- **Proactive Prompts:** Maintains the [[Professional CRM]] and queues daily reminders to follow up with recruiters, mentors, or warm leads if communication goes stale.

### 4.3. Voice-Interactive Mock Interviews
- **Contextual Simulation:** Integrates with the engine's Whisper/TTS Voice I/O pipeline. The agent loads a specific job description and the [[Interview Question Bank]], adopting the persona of a technical hiring manager for that exact role.
- **Feedback Loop:** Conducts a conversational mock interview, transcribes the session, and generates a scorecard with areas for improvement.

### 4.4. Auto-Apply & Autonomous Computer Use (Future Capability)
- **Vision-Based GUI Navigation:** Moving beyond brittle DOM-scraping scripts that fail against Enterprise anti-bot walls (Cloudflare/Datadome). 
- **Direct Application:** The agent will eventually utilize Vision-based GUI navigation (e.g., Anthropic Computer Use API) to autonomously drive the OS cursor, log into secured portals (Workday, Greenhouse), visually locate fields, and copy/paste resume data directly from the Vault, bypassing API restrictions entirely.

---

## 5. Roadmap & Execution Checklists

### Phase 1: Foundation & Legacy Porting
- [x] Migrate `career_counselor` prompt logic into the LangGraph agent state machine.
- [ ] Implement the `add_job_requirement` pipeline (scraping, scoring, `Employer Skill Requirements` updating).
- [ ] Wire up the local `resume-engine` tool and implement the formatting optimization loop (Agentic formatting based on page-fill metrics).
- [x] Establish Deterministic Pre-flight Hydration (DPFH) for the `3.1. Career Strategy/` directory.
- [x] Implement the HITL gate integration (`propose_write` tool mapping to `core.hitl_queue`).
- [x] Harden HITL compliance — mandatory trigger rules for interview status changes, learning completions, skill acquisitions, job applications, and resume tailoring (100% pass rate, 8.0/10 avg, 3/3 cases) (2026-06-01).
- [x] Add Known Cross-Domain File Paths — agent can now `propose_write` to `Current Learning.md` and `To Do List.md` without Librarian escalation (2026-06-01).
- [x] Add `get_master_resume()` tool and Resume Tailoring Protocol — reads master resume and crafts tailored versions via HITL (2026-06-01).
- [x] Implement Decentralized Evaluation (`evals/`) to grade agent responses and HITL compliance.
- [x] Upgrade eval runner with `run_career_agent_with_trace()` — grader now inspects actual tool call traces for HITL compliance instead of inferring from response prose (2026-06-01).

### Phase 2: Telemetry & Memory
- [ ] Build `tools/collect_telemetry.py` to aggregate daily git/vault diffs.
- [ ] Implement the Portfolio & Resume Syncer cron job to propose HITL queue updates.
- [x] Connect the agent to the central `ask_librarian()` tool for cross-domain health/energy context.
- [ ] Implement the Evaluator-Optimizer reflection node for drafting tasks.
- [ ] Create `To Do - Career Agent.md` and implement the bi-directional sync with the master [[To Do List]] (pulling user-added tasks and pushing agent-discovered tasks).

### Phase 3: Advanced Autonomy
- [ ] Build the Professional CRM scanner and follow-up orchestrator.
- [ ] Implement Voice I/O Mock Interview capabilities.
- [ ] Research and prototype Anthropic Computer Use API for Workday auto-applying.
