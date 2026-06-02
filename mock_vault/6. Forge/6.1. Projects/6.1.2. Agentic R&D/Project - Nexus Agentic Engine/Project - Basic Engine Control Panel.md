---
aliases:
  - Engine GUI
  - Dashboard
  - HITL Interface
  - Mission Control
tags:
  - projects
  - ai-agents
  - gui
  - dashboard
type: overview
status:
  archived: false
---
**Back to:** [[Table of Contents#6.1.2. Agentic R&D|Table of Contents]] | [[Project - Nexus Agentic Engine]]

## Overview
The Engine Control Panel's primary purpose is not just aesthetics — it is the **human review surface** for an autonomous system that writes to a personal knowledge base. Without it, HITL (Human-in-the-Loop) is just a chat message. 

*Cross-references: Section 5 (Portfolio Demo UI) and Section 6.4 (Dashboard) of the parent project are **views within** this system, not separate applications.*

**Tech Stack Decision:**
We are building a scalable, full-stack application using **Next.js (React)** for the frontend and **FastAPI (Python)** for the backend agent integration. 
- **Next.js + Tailwind CSS:** Provides a robust, deployable framework for building complex interfaces, managing state, and rapidly styling a premium UI for a public SaaS or portfolio piece.
- **FastAPI:** Runs locally to securely interface with the `Vault/` and trigger the LangGraph agents in the `.venv`.
- **SQLite Database:** Used exclusively for **App State** (e.g., HITL pending queues, shopping carts, inventory), while the `Vault/` (Markdown) remains the pure database for **Knowledge**.
- **Vision:** While starting as an Engine Control Panel, this architecture will scale into a full application named **"Nexus"**, encompassing Home Inventory, Shopping, and other scalable domain agents.

---

## Build Objectives

### 1. Change Review & HITL Interface (Core Priority)
*The primary reason the GUI must exist: to safely review autonomous edits before they are committed.*
- [x] **Diff Viewer:** Side-by-side Monaco Editor (`@monaco-editor/react`) diff of every proposed agent write before it touches the Vault. (2026-05-26)
- [x] **Per-Change Approval:** Approve or reject each proposed change individually. Approval writes to disk with PROJECT_ROOT resolution; rejection updates status in SQLite. (2026-05-26)
- [x] **Context Panel:** Displays the agent's reasoning — decision, confidence score, alternatives considered — parsed from structured JSON alongside the diff. (2026-05-26)
- [x] **Pending Queue:** SQLite-backed persistent queue (`engine/core/hitl_queue.py`) of all HITL decisions awaiting review, with sidebar listing in the GUI sorted by agent and timestamp. (2026-05-26)
- [ ] **Pre-Commit Preview:** Render the full note *after* the proposed change — not just the diff — so the human sees the final output, not just the delta.
- [ ] **Batch Operations:** Batch approve/reject for low-stakes bulk operations.
- [ ] **Manual Edit Before Approve:** Allow inline editing of the proposed content before committing.
- [ ] *Cross-reference: Rollback & Undo Infrastructure handles post-commit recovery; this handles pre-commit gating.*

### 2. Mission Control Dashboard
- [x] Status panel for every agent: last run time, current state (idle / running / waiting for HITL), error count, token spend this week. (2026-05-26)
- [x] Pending HITL decision count — always visible, never buried. Now fetched live from `/api/hitl/pending` with "Review Queue" quick-action button. (2026-05-26)
- [ ] Scheduled task calendar — what runs today, this week, this month.
- [ ] **Unified Task View:** Render the Master To Do list and agent-specific To Do lists in the GUI dashboard, highlighting cross-sync status and completed agent tasks.
- [x] Quick-launch buttons for common workflows (`/ask_brain`, `/weekly_review`, `/audit_engine`). (2026-05-26)
- [ ] *This is the interactive implementation of the auto-generated `Dashboard - Engine Status.md` log.*


### 3. Conversational Interface
- [x] Natural language input (text + voice) routed to the correct agent — replaces the IDE (Antigravity) as the daily driver for interacting with the Brain. (2026-05-26 — text only, Librarian agent)
- [ ] Persistent session context: "focus mode" on a single note or domain (e.g., lock to Career Agent for a job hunt session).
- [ ] Voice I/O pipeline: Whisper → intent classification → agent execution → spoken response.

### 4. Brain Explorer & Knowledge Graph
- [x] **Basic Directory Explorer & Note Preview:** Drill down through physical directory structure and display raw Markdown note content. (2026-05-28)
- [x] **Podcast Studio Integration:** Turn notes into audio podcasts using the backend generator (`tools/generate_podcast.py`), regenerate them, and play them directly in the browser. (2026-05-28)
- [ ] Visual graph of note connections (wiki-links rendered as edges), zoomable by domain section.
- [ ] Highlight orphaned notes, broken links, and stale notes (>90 days, referenced by active projects).
- [ ] Domain section drill-down: navigate the Zettelkasten hierarchy visually, not just as a file tree.
- [ ] Filter by domain section and `Demo Mode` — quickly toggle visibility of sensitive directories (e.g. `2. Health/`, `3.2. Finance/`) during live demos.

### 5. Version History & Audit Log Viewer
- [ ] Surfaces the Vault's nested git history as a human-readable timeline — who (which agent or human) changed what, and when.
- [ ] Per-note history: click any note to see its full change log with diffs.
- [ ] **Episodic Memory Browser:** Surfaces `Logs/Agent Decisions/` JSONL entries as a readable decision timeline — what the agent chose, what it considered, and whether the human overrode it.
- [ ] One-click rollback to any prior note state.

### 6. Notification & Alert Center
- [ ] Push alerts for: new HITL decisions pending, agent errors, upcoming deadlines parsed from project notes, vault health warnings.
- [ ] Configurable urgency levels — critical alerts interrupt; informational ones queue for next review session.
