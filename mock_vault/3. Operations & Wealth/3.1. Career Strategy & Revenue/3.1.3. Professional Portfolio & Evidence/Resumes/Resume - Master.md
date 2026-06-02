---
aliases:
  - Master Resume
  - Curriculum Vitae
  - Professional Bio
tags:
  - resume
  - career
  - profile
type: profile
---
# William Volodarsky
Fort Lee, NJ 07024 | [williamvolodarsky@gmail.com](mailto:williamvolodarsky@gmail.com) | [linkedin.com/in/williamvolodarsky](http://linkedin.com/in/williamvolodarsky) | [github.com/brolodarsky](https://github.com/brolodarsky)
## Summary
Agentic AI Engineer (CS, Magna Cum Laude) and creator of **Nexus**, a production-grade Agentic OS featuring a multi-agent **LangGraph** pipeline with deterministic context injection, a full-stack **Next.js + FastAPI** control panel with HITL governance, an LLM-as-a-Judge evaluation framework, and 12 deployed automation tools. Eight years of business operations leadership (2x revenue, HIPAA compliance) provides the judgment to ship robust, compliant AI systems that solve real-world problems.

## Education
#### **Fordham University** | *BS, Computer Science, Magna Cum Laude* | **Sept 2023 – Dec 2025** | GPA: 3.7 | Dean's List

#### **LaGuardia Community College** | *AS, Computer Science* | **Jan 2020 – Dec 2022** | GPA: 3.7 | Dean's List, Phi Theta Kappa

## Projects & Technical R&D
### **Nexus — Agentic Knowledge OS** | [github.com/brolodarsky/Nexus](https://github.com/brolodarsky/Nexus) | **Jan 2025 – Present**
*A publicly available, production-grade agentic system that manages live personal data across health, career, and learning domains.*
- **Multi-Agent Orchestration Pipeline:** Built a **LangGraph** content router that classifies incoming queries and dispatches to domain-specialized agents via conditional edges. The Career Agent implements **Deterministic Pre-flight Hydration** — a zero-cost Python orchestration node injects live vault file listings and declared dependencies into the system prompt before each LLM call, eliminating hallucinated context. Cross-domain queries escalate to the Librarian agent via compiled subgraph tool invocation.
- **Navigate-First Retrieval Architecture:** Replaced chunk-based Vector RAG with a **LangGraph** ReAct agent that traverses 500+ notes via four filesystem tools with tree-based directory injection and YAML frontmatter filtering. Dynamic prompt injection pre-loads the live vault structure at query time, eliminating an LLM round-trip while keeping navigation current.
- **Full-Stack HITL Control Panel:** Engineered a **Next.js + Tailwind CSS** dashboard backed by **FastAPI** for real-time agent fleet monitoring, conversational search, and a **Monaco Editor** side-by-side diff viewer for pre-commit review of autonomous agent writes — backed by a **SQLite** transaction queue with approve/reject governance. Complements **CLI**, **Voice** (Whisper), and **Telegram Bot** interfaces.
- **Evaluation & Observability:** Built an automated **LLM-as-a-Judge** eval framework grading responses on accuracy, groundedness, and hallucination detection via a 12-case golden dataset with structured JSON reports. Append-only JSONL run logs track token usage, tool call traces, and cited sources per query.
- **Domain Automation Pipelines:** Deployed 12 tools including an HL7 CDA medical XML parser, an 11-platform ADB Android screen-scraper with multi-scroll deduplication, a dual-format resume engine (**Playwright** PDF + **python-docx** DOCX) with page-fill metrics, IMAP email ingestion with Google OAuth2, Trafilatura web extraction, and a TTS podcast generator.

## Professional Experience

### **Handshake AI Fellowship** | *AI Training Fellow* | **Nov 2025 – May 2026**
- Performed iterative resampling with corrective feedback across LLMs and latent diffusion models; evaluated outputs across multi-axial quality rubrics, identifying systematic failure modes (hallucination patterns, context degradation) and translating edge cases into actionable fine-tuning constraints.

### **SiliSlick Knives** | *Co-Owner & Operations Lead* | **June 2017 – June 2025**
- **Revenue Growth:** Identified high-margin product opportunities through sales velocity and competitive analysis, deploying new product lines that **doubled private brand revenue** over 18 months.
- **Global Operations:** Managed multi-channel international distribution (Amazon, wholesale, D2C) across US/UK/EU markets, overseeing regulatory compliance, customs logistics, product design, online/offline marketing, customer support and supplier negotiations.

### **Vitreous Retina Macula Consultants** | *Medical Records & Patient Services* | **June 2015 – Feb 2017**
- **HIPAA Compliance:** Co-managed clinical records for a high-volume ophthalmology practice, maintaining **100% HIPAA compliance** across document handling, retrieval, and inter-office transfers.
- **Data & Process Improvement:** Built interactive tracking spreadsheets for patient service quality and staff scheduling, driving measurable improvements in clinical throughput.

## Technical Skills
- **Agentic AI & LLMs:** LangGraph, LangChain, LangSmith, ReAct Agents, Agentic RAG, Tool Calling, Prompt & Context Engineering, Dynamic Prompt Injection, HyDE, LLM Re-Ranking, Structured Outputs, HITL Alignment, LLM-as-a-Judge Evaluation, NLP, Vector Search, Embeddings, OpenAI API, Whisper.
- **Engineering:** Python, TypeScript, JavaScript, React, Next.js, Java, C++, SQL (PostgreSQL/MySQL/SQLite), Node.js, HTML/CSS, Tailwind CSS, PowerShell, NumPy, Pandas, Pytest, YAML/JSON Schema.
- **Infrastructure:** Git/GitHub, Git-Crypt, Syncthing, Playwright, ADB/Android, Telegram Bot API, IMAP/OAuth2, Linux, FastAPI, HL7 CDA, Obsidian/Zettelkasten.