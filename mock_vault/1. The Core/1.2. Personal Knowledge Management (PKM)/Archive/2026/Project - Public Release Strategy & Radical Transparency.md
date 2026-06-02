---
aliases: [Public Release Plan, Transparency Strategy, GitHub Prep]
tags: [pkm, career, strategy, archive]
type: workshop
updated: 2026-04-28
status: completed
archived: true
---
**Back to:** [[Table of Contents#1.2. Personal Knowledge Management (PKM)|TOC]]

# Public Release Strategy & Radical Transparency

This note documents the strategic decision to transition Nexus from a private repository to a professional, public portfolio. It is a **Personal Brain** release — not a reusable template — and should be framed as such.

---

## 1. The Core Philosophy: Personal Brain, Publicly Owned

The fundamental tension in any public release of a second brain is the conflict between two incompatible goals:

| Goal | Approach | Conflict |
| :--- | :--- | :--- |
| **Portfolio authenticity** | Keep real notes, real context, real usage | Personal details are visible |
| **Reusable framework** | Strip personal specifics, replace with generics | Loses "Human Proof" that proves real usage |

**Resolution:** Nexus is a **Personal Brain release**, not a template. The personal specificity is the point. Anyone who wants to fork it builds their own brain on top of it — they don't expect to inherit a blank slate any more than they'd expect to inherit a clean journal from someone else.

---

## 2. The "Radical Transparency" Case

### 2.1. Why Publish at All? (Career Leverage)
*   **Proof of Orchestration:** The `.agents/` engine and custom tools demonstrate senior-level AI orchestration skills.
*   **Systems Thinking:** Shows the ability to design complex, interlinked cognitive architectures.
*   **Authenticity as Moat:** Differentiates from "demo project" portfolios. This is a real system running a real life — health tracking, career strategy, caregiving coordination, psychological protocols. That is not something you fake.

### 2.2. The Engine Coupling Problem (Resolved)
The agentic skills and workflows explicitly reference personal note paths, personal note names, and personal context (e.g., OCD management protocols, health sections, job search notes). This was initially seen as a privacy risk.

**Revised conclusion: this is a feature, not a bug.**

A recruiter reading `analyze_psych.md` sees a skill that instructs an AI to cross-reference psychological maintenance notes before giving career advice. In context, this signals:
- Clinical-grade self-knowledge encoded as a system design constraint
- Personalized behavioral protocols as engineering decisions
- A system sophisticated enough to integrate real human complexity

The personal specificity *proves* the system is real. Stripping it would gut the evidence.

### 2.3. The Git History Question (Resolved)
The git history contains commits referencing the author's real name and personal context (OCD mentions, health notes, etc.). This was initially seen as a liability.

**Revised conclusion: the history is an asset. Keep it intact.**

- The commit history proves sustained, iterative development over months — not a weekend project
- All vault note *contents* in history are encrypted by git-crypt — only filenames and commit messages are readable
- Vault filenames in history (e.g., `Health Summary.md`, `Job Hunt War Room.md`) serve as proof that the system manages real-world complexity
- A recruiter who digs into git history of a skill file to find a name or OCD mention is doing more work than most will do, and the *context* of that mention is a design decision, not a confession
- Real name attribution is normal; the resume has the same name
- OCD is common (~2–3% of the population) and not a disqualifying condition — especially in the context of someone who built a sophisticated management system around it

---

## 3. What Goes Public vs. Private

### 3.1. The Defense-in-Depth Architecture

Nexus uses a **layered protection model** for managing privacy on a public repo:

| Layer | Mechanism | What It Protects |
| :--- | :--- | :--- |
| **Layer 1: `.gitignore`** | Vault content is untracked entirely | New vault files never enter the repo going forward |
| **Layer 2: `git-crypt`** | `.gitattributes` encrypts all `Vault/**` content | Any vault file that *is* tracked has its contents encrypted — only filenames visible |
| **Layer 3: `git rm --cached`** | One-time untracking of currently tracked vault files | Removes vault files from the repo HEAD, but leaves them in local working directory |

**Why keep all three layers?** Defense in depth. If you accidentally `git add` a vault file in the future, Layer 2 (git-crypt) encrypts it before it reaches GitHub. Layer 1 (gitignore) should prevent the add entirely, but the encryption is a safety net.

### 3.2. What Gets Tracked

| Component | Git Status | Reasoning |
| :--- | :--- | :--- |
| **Engine (`tools/`, `engine/`, `.agents/`)** | ✅ Tracked | Primary technical portfolio evidence |
| **`AGENTS.md`, `README.md`, `CHANGELOG.md`** | ✅ Tracked | Project constitution and history |
| **`Vault/` folder skeleton (directories + `.gitkeep`)** | ✅ Tracked | Shows the cognitive architecture |
| **`Vault/Table of Contents.md`** | ✅ Tracked | Structural map — proves the system's scope |
| **All vault notes (`.md`, except TOC)** | ❌ Gitignored | Content lives locally; engine = the portfolio |
| **All vault binaries (`.pdf`, `.png`, `.jpg`, `.xml`, etc.)** | ❌ Gitignored | Personal documents, medical scans, photos |
| **Obsidian config (`Vault/.obsidian/`)** | ❌ Gitignored | Editor preferences — not portfolio-relevant |
| **Syncthing markers (`Vault/.stfolder/`)** | ❌ Gitignored | Sync infrastructure — not portfolio-relevant |

**Key insight:** The `Vault/Table of Contents.md` is the one note worth keeping public — it shows the full cognitive map of the system (health, career, projects, learning, relationships) without exposing any content. It is the most impressive single file in the vault for a recruiter: *this person mapped their entire life into a structured knowledge graph.*

### 3.3. Why No `Sensitive/` Folder
The `Sensitive/` folder approach (from the original plan) was designed for selective note exclusion. It is now unnecessary because:
- All vault note content is gitignored via `.gitignore` patterns
- The TOC continues to link to all notes locally — links work on disk, cloners just see an empty vault structure
- No per-file decision-making required

### 3.4. The Reusability Question (Resolved)
A cloner gets:
- The full engine (tools, skills, workflows, AGENTS.md)
- The vault folder skeleton
- The TOC as an example of cognitive architecture
- Dead wiki-links in the TOC (expected — they populate their own notes)

This is the correct UX for a "personal brain" release. It's like open-sourcing an operating system without your home directory. The OS is the product; the home directory is yours.

---

## 4. Architectural Methods (Document in README)

The README should explain the following Nexus architectural patterns so public viewers understand the system design:

### 4.1. Git-Crypt Transparent Encryption
- All `Vault/**` content is encrypted at rest on GitHub via `git-crypt`
- File *contents* appear as binary gibberish without the master key
- File and folder *names* remain visible — this is intentional (they serve as the "cognitive map")
- The `.gitattributes` file defines the encryption scope; `.gitkeep` files are explicitly excluded from encryption

### 4.2. Agentic Config Mirror
- `Vault/6. Forge/6.1. Projects/6.1.2. Agentic R&D/Agentic Config/` contains a **mirror** of the root `tools/` directory
- This is an intentional architecture: it allows tinkering with tool scripts *inside Obsidian* using its editor, previewer, and linking features — without touching the production copies at the repo root
- Changes are promoted from the mirror to production manually after testing
- The README should explain this as a deliberate "Obsidian-native development workflow"

### 4.3. Engine + Vault Separation
- The **Engine** (`tools/`, `engine/`, `.agents/`, root docs) is the public portfolio — tracked, readable, version-controlled
- The **Vault** is the private content layer — encrypted and/or gitignored, synced locally via Syncthing
- This separation allows the same repo to serve both as a public technical showcase and a private knowledge store

### 4.4. Syncthing + Git Dual Sync
- Git handles the Engine (code, skills, workflows)
- Syncthing handles the Vault content (notes, audio, large binaries) across devices
- Audio files (MP3s generated by `generate_podcast.py`) are gitignored and sync via Syncthing only
- This avoids bloating the git repo with large binary files while keeping mobile access

---

## 5. The README: Human Context Statement

The README is where the "Radical Transparency" philosophy gets stated explicitly, in the author's voice. It should include:

1. **What this is:** A personal second brain / agentic knowledge OS, not a generic template
2. **Why it's public:** To demonstrate real-world agentic orchestration on a complex, live system
3. **What's in it:** Engine layer (tools, skills, workflows) and vault folder structure — vault note content is local-only
4. **The Table of Contents:** Explain that the TOC is intentionally left public and unencrypted as a showcase of use cases — it demonstrates the *scope* of what a personal cognitive OS can manage (health, career, caregiving, learning, projects, relationships) without exposing any actual content. It serves as both a structural map for cloners and a proof-of-concept for recruiters
5. **The Human Context Statement:** Acknowledge that the skills and AGENTS.md reference real personal context by design — this is the proof that the system runs a real life
6. **Architectural Methods:** Explain the patterns from Section 4 (git-crypt, Agentic Config mirror, Engine/Vault separation, Syncthing dual-sync)
7. **How to fork it:** Replace the vault content with your own notes, adapt the skills to your own domain context, keep the engine

---

## 6. Implementation Gameplan

### 6.1. `.gitignore` Updates (✅ Implemented 2026-04-28)
The original plan used per-extension patterns (`.md`, `.pdf`, `.png`, etc.), but implementation used a **wildcard approach** that is strictly superior — it catches ALL file types (including `.py`, `.js`, `.json` from the Agentic Config mirror that the extension list would have missed) and can never be defeated by an unexpected file type:
```gitignore
# Ignore ALL files inside Vault/ at every nesting level
Vault/**
Vault/*
Vault/*/*
Vault/*/*/*
Vault/*/*/*/*
Vault/*/*/*/*/*

# Un-ignore directories so Git can traverse them for .gitkeep files
!Vault/**/

# Keep the folder skeleton tracked (empty-folder markers)
!Vault/**/.gitkeep

# Keep the Table of Contents — the public cognitive map
!Vault/Table of Contents.md
```
Explicit depth-level rules (`Vault/*` through `Vault/*/*/*/*/*`) added as belt-and-suspenders on top of `**` glob to guard against Git's known quirks with deeply nested negation patterns.

### 6.2. Pre-Release Checklist

**Gitignore & Untrack:**
- [x] Update `.gitignore` with comprehensive vault patterns — wildcard approach (`e00d751`, hardened in `e712f71`)
- [x] Update `.gitattributes` to exclude `Table of Contents.md` from git-crypt encryption so it's readable on GitHub (`e712f71`)
- [x] Run `git rm --cached` on all currently tracked vault files except `Table of Contents.md` and `.gitkeep` files — 202 files untracked
- [x] Verify: `git ls-files "Vault/"` shows only TOC + 23 `.gitkeep` files ✅

**Documentation:**
- [x] Rewrite `README.md` with Human Context Statement, Architectural Methods, and How to Fork section
- [x] Final review of `AGENTS.md` as a public-facing document
- [x] Add `LICENSE` file — AGPL-3.0 added (`327b692`)

**Ship:**
- [x] Final `git add`, commit, push
- [x] Flip repo to public on GitHub

### 6.3. Post-Release
- [ ] Link the GitHub repo from resume and outreach materials
- [ ] Use it as the "Proof of Work" link in Sniper Protocol outreach
- [ ] Frame in applications as: *"A deployed, production agentic system managing real-world cognitive infrastructure"*

---

## 7. Decision Log

| Date | Decision |
| :--- | :--- |
| 2026-04-06 | Decided to proceed with "Radical Transparency" over "Total Reset" to preserve version history as proof of work. |
| 2026-04-06 | Defined the "Intimacy Line" — `Sensitive/` folder approach for selective exclusion. |
| 2026-04-22 | **Revised:** Dropped `Sensitive/` folder in favor of blanket vault gitignore. Simpler, no per-file decisions needed. |
| 2026-04-22 | **Resolved:** Engine coupling (skills referencing personal note names + OCD) is a feature, not a liability. Context makes it a design strength. |
| 2026-04-22 | **Resolved:** Git history with real name and personal mentions — keep intact as proof of sustained development. Vault contents in history are encrypted by git-crypt. |
| 2026-04-22 | **Confirmed:** Personal Brain release framing (not a reusable template). Reusability is a secondary concern; authenticity is the primary value. |
| 2026-04-22 | **Confirmed:** `Vault/Table of Contents.md` is the one note worth tracking publicly — it shows the full cognitive map without exposing any content. |
| 2026-04-22 | **Confirmed:** Agentic Config mirror (`Vault/6.1.2./Agentic R&D/Agentic Config/`) is intentional architecture — Obsidian-native development workflow for tool tinkering. Document in README. |
| 2026-04-22 | **Confirmed:** Git-crypt retained as Layer 2 defense-in-depth. `.gitattributes` stays even with gitignore patterns. |
| 2026-04-22 | **Confirmed:** Comprehensive gitignore patterns covering all binary types (PDF, PNG, JPG, XML, etc.), Obsidian config, and Syncthing markers — not just `.md` files. |
| 2026-04-28 | **Executed:** Baseline commit of dirty working tree (26 files) before release refactor (`90b161b`). |
| 2026-04-28 | **Executed:** Removed orphan `styles.css` from repo root (`c778948`). |
| 2026-04-28 | **Revised:** Replaced per-extension gitignore approach with wildcard `Vault/**` + depth-level belt-and-suspenders. Strictly better — catches all file types including Agentic Config mirror `.py`/`.js`/`.json` files that the original plan missed. |
| 2026-04-28 | **Executed:** Excluded `Table of Contents.md` from git-crypt encryption via `.gitattributes` so it's readable on GitHub as the public cognitive map. |
| 2026-04-28 | **Executed:** Untracked 202 vault content files via `git rm --cached`. Verified only TOC + 23 `.gitkeep` files remain tracked. All local files preserved. |
| 2026-04-28 | **Executed:** Added AGPL-3.0 license (`327b692`). |
| 2026-04-28 | **Confirmed:** Agentic Config mirror correctly untracked — production copies at `.agents/` and `tools/` are the portfolio; mirror is the private Obsidian dev workspace. |

---

**Related:** [[Project - Nexus Non-Engine Functionality Upgrades]], [[Synthesis - AI Superagency & The Future of Work]], [[Job Hunt War Room]]
