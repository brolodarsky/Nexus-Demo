---
aliases: [Brain Roadmap, System Improvements, Next Level]
tags: [pkm, meta, projects, strategy]
type: overview
---
**Back to:** [[Table of Contents]]

> [!important] For Any Agent
> This is a prioritized backlog of improvements for the Nexus.0 system. Each item is self-contained with enough context for any agent to pick it up and execute. Work through them in priority order unless the user directs otherwise.

# High Impact
## 1. Dashboard Note -> Dashboard Plugin
**Status:** ⬜ Not Started
**Effort:** Large — Phase 1: Markdown/CSS snippet; Phase 2: TypeScript Plugin
**Why:** The vault has an index ([[Table of Contents]]), a task list ([[To Do List]]), and protocols ([[Protocol - Career Maintenance]], [[Protocol - Brain Maintenance]]) — but no single note that answers "what should I do RIGHT NOW?" Opening Obsidian requires deciding which note to look at first. A dashboard eliminates that decision fatigue. Furthermore, packaging this dashboard into a custom Obsidian Plugin serves as a flagship "Agentic System Architecture" deployed project for the portfolio (proving deployed orchestration engineering).

**What to build:**
	- See [[Workshop - Dashboard Option 1 Gameplan]] for technical specifics on Phase 1.
- **Phase 1:** Create `Dashboard.md` in `Vault/` root (or `1. The Core/`), pin it as the startup note, and use Dataview to pull state data.
- **Phase 2:** Refactor the CSS and backend logic into a formal, installable Obsidian Plugin built with TypeScript and the Obsidian API.
- Should surface at a glance:
	- Today's active focus from [[Current Learning]]
	- Top 3 items from [[To Do List]]
	- Next protocol due (link to [[Protocol - Brain Maintenance]] or [[Protocol - Career Maintenance]])
	- Active project count with links
	- A rotating motivational line from [[Goals]]
- Consider using Dataview queries (see item #5) to auto-populate sections

---

## 2. Populate `Current Learning.md`
**Status:** ⬜ Not Started
**Effort:** Small — content authoring
**Why:** This note is linked prominently in the TOC under 1.1 but is currently empty. It's supposed to be the bridge between the massive Section 6 learning library and actual daily study. Without it, the library is a museum — impressive but unused.

**What to build:**
- Open [[Current Learning]] and populate it with:
	- **Active Subjects** — What am I studying right now? (e.g., Kubernetes, system design, LeetCode patterns)
	- **Weekly Study Schedule** — Which days/hours are for what subjects
	- **Resources In Progress** — Specific courses, books, or playlists currently being worked through (link to Section 6 notes)
	- **Completed Subjects** — Archive of things finished, with dates
- Cross-link to [[Interview Prep Hub]] for career-relevant study
- Cross-link to [[Employer Skill Requirements]] for gap identification
- Reference: [[Goals]] already mentions "Skill Sharpening" as a priority

---

## 5. Vault Structural Refactor & Friction Reduction
**Status:** 🟩 Completed (2026-04-11)
**Effort:** Medium — Path migrations & TOC refactor
**Why:** Current capture points are nested too deep, causing friction. "Memories" (high-value history) is currently co-mingled with "Inbox" (transient data). Friction is the enemy of a second brain.

**What to build:**
- **Capture Relocation:**
	- Move `Inbox/` to root as `0. Inbox/`
	- Move `Quick Capture.md` to root as `0. Quick Capture.md`
- **Memories Elevation:**
	- Create nested section under **`1.1. Philosophy & Personal North Star / Personal Logs`**
	- Move `Memories Log.md` and `Memories Log Images/` there.
- **Journal Integration:**
	- Decide and implement a `Journal.md` or Daily Note structure within the new Logs section.
- **Engine Coordination:**
	- Update `AGENTS.md`, `README.md`, and `CHANGELOG.md` to reflect the new architecture.
	- Update `/audit_inbox` and `/capture_content` workflows with new hardcoded paths.
	- Update `generate_obsidian_note` skill if it enforces specific folder structures for these items.

---

# Medium Impact

## 6. Install Community Plugins (Dataview, Templater, Calendar)
**Status:** ⬜ Not Started
**Effort:** Small — installation + configuration
**Why:** The vault currently runs on zero community plugins. These three act as the "Operating System" for Obsidian, transforming it from a text editor into a relational database and automation engine.

**Considerations:**
- **Security:** While community plugins are third-party code, these "Big Three" have hundreds of thousands of users and are open-source. They are effectively crowd-audited and considered low-risk.
- **Mobile Compatibility:** Since the vault syncs via Syncthing, the `.obsidian/plugins` folder will sync to your phone. All three plugins are fully compatible with the Obsidian mobile app, though complex Templater scripts should be verified for mobile-safe paths.

**What to install & Key Use Cases:**
- **[Dataview](https://github.com/blacksmithgu/obsidian-dataview):** The database layer.
	- **Project Auto-Indexing:** Dynamically list all `Project -` notes with `status: active`.
	- **Medical Trends:** Create tables to track biomarkers (weight, vitals) across multiple `Visit -` notes chronologically.
	- **Brain Audit:** Find "orphaned" knowledge or notes with missing metadata.
- **[Templater](https://github.com/SilentVoid13/Templater):** The automation layer.
	- **Smart Project Starter:** Prompt for lead, budget, and deadline on file creation, then auto-calculate milestone dates.
	- **Daily Note Integration:** Automatically pull "Tasks Due Today" and "Learning Targets" into each morning's log.
- **[Calendar](https://github.com/liamcain/obsidian-calendar-plugin):** The timeline layer.
	- **Visual Frequency:** See heatmaps of vault activity to identify gaps in study or maintenance protocols.
	- **Flashback Reviews:** Click "this day last year" to review history or psychiatric logs for longitudinal perspective.
- **[Daily Notes](https://help.obsidian.md/Plugins/Daily+notes):** (Core Plugin) The "Journal" layer.
	- **Stream of Consciousness:** Use this as the "Global Journal" (in `1.1. / Personal Logs`) to avoid cluttering human-curated Memory logs.

> [!warning] Agent Note
> Plugin installation requires user action in the Obsidian GUI — agents cannot install plugins directly. Walk the user through: Settings → Community Plugins → Browse → search name → Install → Enable.

---

## 7. Note Type Templates
**Status:** ⬜ Not Started
**Effort:** Small — template file creation
**Why:** Only one template exists ([[Template - New Note or Thought]]). But the vault uses distinct prefixes (`Project -`, `Protocol -`, `Article -`, `Plan -`, `Workshop -`, `Log -`) that each have their own structure. Templates ensure consistency whether a human or agent creates the note.

**What to build:**
- Create templates in the Obsidian templates folder for each type:
	- **Template - Project:** Pre-filled with `## Objective`, `## Scope`, `## Tasks`, `## Materials & Resources`, `## Status Log`
	- **Template - Protocol:** Pre-filled with `## Frequency`, `## Checklist`, `## Last Run`
	- **Template - Article Distillation:** Pre-filled with `## Source`, `## Key Takeaways`, `## Atomic Concepts`, `## Questions Raised`
	- **Template - Plan:** Pre-filled with `## Goal`, `## Steps`, `## Timeline`, `## Dependencies`
	- **Template - Workshop:** Pre-filled with `## Objective`, `## Experiments`, `## Findings`, `## Next Steps`
- Each template must include: YAML frontmatter block, `Back to: [[Table of Contents]]` link, and the type-specific sections
- Update the `generate_obsidian_note` skill to reference these templates when creating notes of each type

---

## 8. Measurable Goals Tracker
**Status:** ⬜ Not Started
**Effort:** Small — content restructuring
**Why:** [[Goals]] is strong on narrative but weak on measurable milestones. "Apply to two roles per weekday" is great — but there's no tracker closing the loop between intent and accountability.

**What to build:**
- Add a tracking table to [[Goals]] or create a companion `Goals Tracker.md`:

| Goal | Metric | Target | Deadline | Current | Status |
|------|--------|--------|----------|---------|--------|
| Job applications | Apps/week | 10 | Ongoing | ? | 🟡 |
| AI Rating income | $/week | $0 | Past | N/A | 🛑 |
| Savings rate | % of income | 30% | Monthly | ? | ⬜ |
| Feeder development | Hours/week | 5 | Ongoing | ? | ⬜ |
| Study time | Hours/week | ? | Ongoing | ? | ⬜ |

- Review and update this table during the `/weekly_review` workflow (item #3)
- Cross-link from [[Dashboard]] (item #1) so you see progress at a glance

---

## 25. Standardize Knowledge Taxonomy (Article vs. Concept vs. Synthesis)
**Status:** ⬜ Not Started
**Effort:** Medium — Global refactor
**Why:** As the vault grows, the distinction between "Raw Input," "Atomic Definitions," and "Strategic Synthesis" is blurring. Standardizing on a prefix-based taxonomy ensures that both humans and agents can navigate the knowledge density correctly and maintain traceability from raw source to final strategy.

**What to build:**
- Create `Protocol - Knowledge Architecture & Naming.md` in `1.2. PKM` to define the "Grammar" of the vault.
- Refactor top-level hubs (e.g., `Overview - AI Agents`) to the `Synthesis -` prefix.
- Ensure all notes have correct `type:` fields in YAML (source, concept, synthesis, architecture).
- Perform a Global Link Update to ensure no wiki-links are broken during renaming.

---

## 26. Condense Section 6.2 Library for AI Engineer Path
**Status:** ⬜ Not Started
**Effort:** Medium — TOC refactor & Hub creation
**Why:** Section 6.2 currently contains 14 sub-sections, many of which (Math, Robotics, CV) are "rarely touched" and contribute to cognitive load ("RAM Tax"). This project collapses the "textbook index" into a "tactical HUD" focused on Agentic AI and Production Engineering.

**What to build:**
- See [[Project - Section 6.2 Library Condensation]] for the full gameplan.
- Collapse 11 sub-sections into a single `6.2.X. Technical Reference Archive` MOC.
- Retain only high-leverage sections (Agents, RAG, MLOps, Python) in the master TOC.

---

# Nice-to-Have

## 9. Vault Health Metrics Script
**Status:** ⬜ Not Started
**Effort:** Medium — Python script
**Why:** No way to measure vault growth or health over time. Is the brain growing or accumulating dead weight?

**What to build:**
- Create `tools/vault_health.py` that reports:
	- Total note count (by section)
	- Orphan note count (no inbound links)
	- Average links per note
	- Most-linked notes (the "hub" notes)
	- Least-touched notes (by modification date)
	- Empty folders (ignoring `.gitkeep`)
- Output as a markdown report that can be pasted into a `Log - Vault Health` note
- Run monthly as part of [[Protocol - Brain Maintenance]]

---

## 20. Create notes for remaining unlinked/non-existent TOC sections/topics

--- 

## 21. Standardize Folder Representation in the TOC

**Status:** ⏳ Workshopping
**Effort:** Small — architectural decision & documentation
**Why:** The `Table of Contents.md` thrives on `[[Wiki Links]]` to actual markdown files. Physical folders (like `Saved Articles/` or `Audio/`) cannot be clicked in the native markdown viewer, causing an inconsistency. If they are just bold, unlinked text, they interrupt the "Map of Content" (MOC) pattern and confuse automated agents mapping the vault.

**Proposed Solutions:**
1. **Approach 1: The "Folder Note" (Most Robust):** Create a physical `.md` file for every major folder (e.g., `Saved Articles.md`). Put a Dataview query inside it to auto-list all files in that path. The TOC then uses a standard link to this setup.
2. **Approach 2: The "Visual Directory" (Fastest):** Adopt a strict prefix convention for unlinked folders in the TOC so they visually differentiate from missing files, e.g., `- 📁 **Saved Articles/**: AI and Job market research...` (Currently being tested).
3. **Approach 3: The "Deep Storage" Rule (Cleanest):** If a folder is only ever accessed via links dynamically stored in *other* notes (e.g., accessing saved articles via links clustered in a `Synthesis` hub), do not list the core folder in the TOC at all. The TOC is a map of *entry points* for humans, not a system file explorer.

**Decision Required:** Pick a standard to adopt globally and formally document it in `README.md` and `AGENTS.md`.

--- 

## 22. Preparation for GitHub Public Release
**Status:** 🟩 Completed
**Effort:** Medium — Audit, Sanitization, Branding
**Why:** Transitioning from a private to a public repository requires careful sanitization to preserve privacy while maximizing professional impact. This project implements the "Radical & Integrated Transparency" strategy to showcase the brain's real-world utility.

**What to build:**
- See [[Project - Public Release Strategy & Radical Transparency]] for the full strategic audit and implementation steps.
- **Audit:** Move intimate metadata (Romance, private Psych logs) to the gitignored `Sensitive/` folder.
- **Documentation:** Author a "Human Context Statement" for the README and sanitize the repository's public-facing metadata.
- **History Management:** Decide between a "Clean Slate" reset or a "Squash & Scrub" to preserve professional longevity.

## 23. Private Git History for Vault (The Nested Heart)
**Status:** 🟩 Completed
**Effort:** Small — CLI configuration
**Why:** Gitignoring the `Vault/` for the public release (Item #22) successfully protected privacy but at the cost of losing version history and diffing for personal notes. This "Nested Heart" architecture restores Git power to the notes without risking a leak to the public repository.

**What to build:**
- **Nested Repo Initialization:** Initialize a separate Git repository inside `Vault/`. Since the root repo ignores this path, the two histories remain completely isolated.
- **CLI Workflow:** Define the "Context Switch" (cd Vault for notes, cd .. for tools).
- **Private Remote:** Set up a private GitHub/GitLab remote for the Vault to ensure personal notes are backed up to the cloud without being public.
- **Dual-Commit Automation:** Create a `tools/` script (e.g., `sync_brain.py`) that can commit and push both repositories in a single command.

--- 

## 24. MCP (Model Context Protocol) Integration
**Status:** ⏳ Workshopping
**Effort:** Medium — Architecture & Implementation
**Why:** Standardizing the vault's tools via MCP allows *any* agentic AI (not just the local engine) to interact with the vault with full context-awareness. This bridges the gap between different AI clients (Claude, VS Code, LangGraph) and ensures a consistent interface for the "Second Brain."

**What to build:**
- See [[Workshop - MCP Additions]] for the roadmap.
- **Vault MCP Server:** Expose core navigation tools (`read_note`, `search_vault`, `get_toc`) via a standardized protocol.
- **External Ingestion MCP:** Refactor existing scripts (`youtube_transcript.py`, etc.) into MCP servers.
- **Integration:** Register the MCP server in the IDE (Antigravity/Cursor) and the local LangGraph engine.

--- 

> [!tip] Recommended Execution Order (Updated)
> Work through the segments in sequence to ensure dependencies are met.
>
> ### Phase 1: Foundations & Quick Wins
> - [x] **#5 (Structure)**: Vault Structural Refactor (Inbox/Memories) to reduce friction.
> - [x] **#12 (Register Projects)**: Register all `Project -` and `Protocol -` notes in To Do List.
> - [x] **#23 (Private History)**: Re-instrument the Vault with a nested private Git repository.
> - [ ] **#6 & #7 (Enablers)**: Install Dataview/Templater/Daily Notes and create Note Templates.
> - [ ] **#20 & #21 (Arch Decisions)**: Fill TOC gaps and standardize how folders are represented.
> - [ ] **#25 (Taxonomy)**: Create the Naming Protocol and refactor Hub notes to `Synthesis -`.
> - [ ] **#26 (Library Condensation)**: Refactor Section 6.2 for AI Engineer focus and reduced RAM tax.
> - [ ] **#2 (Current Learning)**: Populate this note to bridge the library and daily study.
>
> ### Phase 2: Visibility & System Cadence
> - [ ] **#1 (Dashboard)**: Create the centralized command center (Phase 1).
> - [ ] **#8 (Goals)**: Integrate measurable milestone tracking into the weekly cadence.
>
> ### Phase 3: Engine Polish & Automation
> - [x] **#11 (Stale References)**: Fix all stale wiki-links and broken references across the Vault.
> - [ ] **#24 (MCP Integration)**: Standardize vault access via Model Context Protocol.
> - [ ] **#9 (Maintenance Automation)**: Vault health metrics script.
>
> ### Phase 4: Long-Term Architecture
> - [x] **#22 (GitHub Prep)**: Sanitize and prepare the brain for public release.

