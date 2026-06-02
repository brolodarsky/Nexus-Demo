---
aliases:
  - Extended Resume
  - Full CV
tags:
  - resume
  - career
  - profile
type: profile
---
# William Volodarsky
Fort Lee, NJ 07024 | [williamvolodarsky@gmail.com](mailto:williamvolodarsky@gmail.com) | [linkedin.com/in/williamvolodarsky](http://linkedin.com/in/williamvolodarsky) | [github.com/brolodarsky](https://github.com/brolodarsky)
## Summary
Agentic AI Engineer (CS, Magna Cum Laude) and creator of **Nexus**, a production-grade Agentic OS orchestrating 10 workflows, 11 skills, and 12 automation tools — featuring a navigate-first retrieval architecture, an LLM-as-a-Judge evaluation pipeline, JSONL observability, and defense-in-depth security across health, career, and learning domains. Eight years of business operations leadership (2x revenue growth, HIPAA compliance) provides the cross-functional judgment to ship robust, compliant AI systems that solve real-world problems.

## Education
#### **Fordham University** | *BS, Computer Science, Magna Cum Laude* | **Sept 2023 – Dec 2025** | GPA: 3.7 | Dean's List

#### **LaGuardia Community College** | *AS, Computer Science* | **Jan 2020 – Dec 2022** | GPA: 3.7 | Dean's List, Phi Theta Kappa

## Projects & Technical R&D
### **Nexus — Agentic Knowledge OS** | [github.com/brolodarsky/Nexus](https://github.com/brolodarsky/Nexus) | **Jan 2025 – Present**
*A publicly available, production-grade agentic system that manages live personal data across health, career, and learning domains. 17 tracked releases, 500+ interconnected notes, fully version-controlled via a 500+ line changelog.*
- **Navigate-First Agent Architecture:** Replaced chunk-based Vector RAG with a **LangGraph** ReAct agent that traverses 500+ Zettelkasten notes via four filesystem tools (`read_toc`, `read_note`, `search_vault`, `get_vault_structure`) with tree-based directory injection and YAML frontmatter tag filtering. Dynamic prompt injection pre-loads the live vault directory tree into the system prompt at query time, eliminating an LLM round-trip while keeping navigation current after vault restructures. The architecture deliberately prioritizes structural navigation over fuzzy semantic search to preserve document hierarchy and context.
- **Evaluation & Observability Pipeline:** Built an automated **LLM-as-a-Judge** eval framework grading agent responses across accuracy, groundedness, and hallucination detection — backed by a 12-case golden dataset with structured JSON reports including per-case duration, token usage, and pass/fail classification. Append-only JSONL run logs capture execution telemetry (timestamp, tool call sequences, cited sources, token counts, status) for every query across all interfaces, providing production-grade observability without external SaaS dependencies.
- **Multi-Interface Mission Control:** Engineered a persistent coordinator with a unified dispatcher serving **CLI** (argparse-based metadata filters), **Voice** (local PyAudio microphone capture + OpenAI Whisper transcription), and **Telegram Bot** (python-telegram-bot with user-ID allowlist middleware and `.ogg` voice note transcription). The Telegram bot launches as a background daemon thread with live status monitoring from the interactive menu.
- **Domain Automation Pipelines:** Deployed 12 deterministic tools including: an **HL7 CDA medical XML parser** converting structured clinical documents to Obsidian-ready Markdown with table preservation; a universal **ADB Android screen-scraper** (`ingest_phone.py`, 553 lines) supporting 11 messaging platforms (Google Messages, WhatsApp, Signal, Tinder, Hinge, Bumble, Discord, Instagram, Snapchat, Messenger, Telegram) with multi-screen scroll capture, cross-screen deduplication, toolbar contact name detection, and sender alignment heuristics; a **dual-format resume engine** (Node.js/**Playwright** for styled PDFs + **python-docx** for ATS-compatible DOCX) with an interactive document picker; a **TTS podcast generator** (edge-tts); and atomic content ingestion tools for email (IMAP/OAuth2), webpages (Trafilatura), and YouTube transcripts.
- **Security & Self-Governance:** Established a dual-Git "Nested Heart" layout separating public engine code from private Vault content encrypted via **git-crypt**, with **Syncthing** for zero-cloud device sync. The system is governed by a declarative "Agentic Constitution" (`AGENTS.md`) with 11 enforced rules, a compiled portability architecture ensuring rule consistency across AI contexts, and meta-skills (`skill_creator`, `workflow_creator`) that autonomously generate, optimize, and benchmark new skills and workflows — closing the self-improvement loop.
- **Content Ingestion Infrastructure:** Built composable tool primitives for email fetching (IMAP with Google OAuth2), clean webpage extraction (Trafilatura), YouTube transcript download, and vault structure validation — all consumed by agentic workflows (`/capture_content`, `/distill_learning`, `/audit_inbox`) that automate the full ingest-classify-file pipeline.
- **Architectural Evolution (17 Releases):** Progressed from a flat script collection to a modular engine architecture across 17 tracked releases: Vector RAG → Agentic RAG with HyDE + LLM Re-Ranking → Navigate-First Filesystem Agent. Executed three major architectural pivots, each with full eval regression testing, documentation updates, and backward-compatible migration paths.

## Professional Experience

### **Handshake AI Fellowship** | *AI Training Fellow* | **Nov 2025 – Present**
- **Human-Guided Alignment:** Performed iterative resampling with corrective feedback across next-generation LLMs and latent diffusion models to optimize accuracy and instruction adherence.
- **Multi-Axial Evaluation & QA:** Evaluated LLM/diffusion outputs across complex quality rubrics, identifying systematic failure modes (hallucination patterns, context degradation) and translating edge cases into actionable fine-tuning constraints.

### **SiliSlick Knives** | *Co-Owner & Operations Lead* | **June 2017 – June 2025**
- **Revenue Growth:** Identified high-margin product opportunities through sales velocity and competitive analysis, deploying new product lines that **doubled private brand revenue** over 18 months.
- **Global Operations:** Managed multi-channel international distribution (Amazon, wholesale, D2C) across US/UK/EU markets, overseeing regulatory compliance, customs logistics, product design, online/offline marketing, customer support and supplier negotiations.

### **Vitreous Retina Macula Consultants** | *Medical Records & Patient Services* | **June 2015 – Feb 2017**
- **HIPAA Compliance:** Co-managed clinical records for a high-volume ophthalmology practice, maintaining **100% HIPAA compliance** across document handling, retrieval, and inter-office transfers.
- **Data & Process Improvement:** Built interactive tracking spreadsheets for patient service quality and staff scheduling, driving measurable improvements in clinical throughput and reducing retrieval latency.

## Technical Skills
- **Agentic AI & LLMs:** LangGraph, LangChain, LangSmith, ReAct Agents, Agentic RAG, Tool Calling, Prompt & Context Engineering, Dynamic Prompt Injection, HyDE, LLM Re-Ranking, Structured Outputs, HITL Alignment, LLM-as-a-Judge Evaluation, NLP, Vector Search, Embeddings, OpenAI API, Whisper.
- **Engineering:** Python, Java, C++, SQL (PostgreSQL/MySQL), JavaScript, Node.js, HTML/CSS, PowerShell, NumPy, Pandas, Pytest, python-docx, YAML/JSON Schema.
- **Infrastructure:** Git/GitHub, Git-Crypt, Syncthing, Playwright, ADB/Android, Telegram Bot API, IMAP/OAuth2, Linux, FastAPI, HL7 CDA, edge-tts, Obsidian/Zettelkasten.
