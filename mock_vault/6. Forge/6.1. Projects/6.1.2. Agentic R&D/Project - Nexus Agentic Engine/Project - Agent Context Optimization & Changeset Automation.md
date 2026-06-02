---
aliases: [Context Bloat Mitigation, Changeset Automation, Release Automation]
tags: [projects, engine, devops, pkm]
type: overview
---
[[Table of Contents#6.1.2. Agentic R&D|TOC]] | [[Project - Nexus Agentic Engine]]

# Background & Objective
As the Nexus system scales, autonomous agents read and update files frequently. Files that grow continuously (like `CHANGELOG.md`) create a **context leak**—wasting prompt tokens and increasing the risk of LLM formatting hallucinations and git merge conflicts. 

The objective of this project is to implement a **Changeset-based release compilation system** and define systematic controls to mitigate context bloat across all areas of the agentic operating system.

---

# Core Pillars

## 1. Fragmented Changelog Authoring (Changesets)
*   **The Problem:** Editing the monolithic `CHANGELOG.md` directly on every task requires reading 500+ lines of historical logs, creating context bloat and sync collisions between concurrent agents.
*   **The Solution:**
    *   Agents write change notes to temporary, isolated files in `.changeset/*.md` (e.g., `.changeset/docs-readme-refactor.md`).
    *   Each fragment contains a YAML header specifying the change classification (`type: patch | minor | major`) and scope.
    *   This makes changelog writing an $O(1)$ write operation with zero read overhead and no merge conflicts.

## 2. Tiered Changelog Files
*   **`CHANGELOG-RECENT.md` (Active Context):** Tracks only the last 3–5 releases (~100 lines). Injected or read by agents during startup to provide up-to-date context on the project's evolution.
*   **`CHANGELOG.md` (Monolithic Archive):** The full history of the project. Excluded from routine agent reads to conserve tokens.

## 3. Release Compilation Script (`tools/release.py`)
*   **The Script:** A Python tool run on release to parse `.changeset/*.md` fragments, calculate the appropriate semantic version bump, prepend the new entry to both the master `CHANGELOG.md` and `CHANGELOG-RECENT.md`, and delete the processed fragments.

---

# Vault-Wide Context Bloat Mitigation Rules

| Bloat Source | Cause | Prevention & Mitigation Strategy |
|---|---|---|
| **Changelog History** | Appending entries to a growing list | Implement Changesets and split the log into `CHANGELOG-RECENT.md` and the master archive. |
| **Ingestion Files** | Saving giant raw page scrapes or YouTube transcripts | Scrutinize files in `0. Inbox/` via snippet/metadata reads first (first 500–1,000 chars) before loading full content. |
| **System Rules (`AGENTS.md`)** | Injecting all workflow/skill details into system prompts | Keep `AGENTS.md` minimal (triggers only). Lazy-load specific skill instructions (e.g., `generate_obsidian_note/SKILL.md`) only when active trigger matches. |
| **Project Note Tasks** | Accumulating dozens of completed `[x]` items | Move completed tasks periodically to a collapsed `<details>` section or separate `Project - Archive - [Name].md` files. |
| **Semantic Search Queries** | Dumping large matched documents into context | Constraint search via directory hierarchy (Phase 2 Search) and implement character-limit constraints on `read_note` outputs. |
| **Master Index (`Table of Contents.md`)** | Listing individual notes | Enforce **Rule 5**: TOC is structural-only. Granular logs, articles, and visits must reside in specialized Hubs or Maps of Content (MOC). |

---

# Tasks

### Phase 1: Changelog Refactoring & Changesets
*   [x] Create the `.changeset/` staging directory with a `.gitkeep` file.
*   [x] Write `tools/release.py` compilation script to parse and merge fragments.
*   [x] Create `CHANGELOG-RECENT.md` and populate it with the last 3 releases.
*   [x] Archive old releases in `CHANGELOG.md` (keep it as the master history log).
*   [x] Update the `maintain_project_docs` skill to write a fragment instead of editing the changelog directly.

### Phase 2: Lazy Loading & Prompt Optimization
*   [ ] Audit current system prompts to ensure `AGENTS.md` is tight.
*   [ ] Restructure core engine loop to dynamically read skill files from `.agents/skills/` only upon trigger match.

### Phase 3: Archive & Snippet Sorting
*   [ ] Implement a rollup script/workflow to collapse completed tasks in `Project -` notes.
*   [ ] Update `/audit_inbox` to read snippets of inbox notes rather than loading whole files.
