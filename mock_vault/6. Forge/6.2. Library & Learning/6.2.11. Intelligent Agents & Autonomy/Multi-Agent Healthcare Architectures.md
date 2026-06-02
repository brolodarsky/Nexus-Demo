---
aliases: [Virtual Tumor Boards, AMIE, Medical Autonomous Agents]
tags: [agents, healthcare, multi-agent, architecture, ai]
type: concept
---
**Back to:** [[Table of Contents#6.2.11. Intelligent Agents & Autonomy|TOC]]

# Multi-Agent Healthcare Architectures

## Overview
A critical frontier in AI research (2025-2026) is the shift from single-prompt foundational LLMs to specialized, multi-agent panels for clinical reasoning. The goal is to solve LLM hallucination and polypharmacy blind-spots by forcing adversarial debate among specialized instances. 

## Key Industry Developments

### 1. The Big Tech "Virtual Tumor Boards" (Microsoft & Google)
- **Microsoft Research ([AutoGen](https://microsoft.github.io/autogen/)):** Microsoft researchers utilize AutoGen to simulate "Virtual Tumor Boards." Rather than asking one model for a diagnosis, the system spawns discrete specialist agents (e.g., an Oncologist, a Radiologist, a Pathologist). The agents explicitly debate the patient's records against NCCN clinical guidelines, resolving contradictions through consensus.
- **Google DeepMind (AMIE / Med-Gemini):** Google's **AMIE** (Articulate Medical Intelligence Explorer) uses agentic "inner monologues" and critique loops. Prior to outputting a diagnostic recommendation, the agent runs a hidden reasoning step to critique its own differential diagnosis and cross-reference clinical research.

### 2. Specialized Commercial Startups
- **Hippocratic AI:** Valued steeply in the mid-2020s, this startup builds a "constellation" of specialized healthcare agents (dietitians, care coordinators) rather than one general bot. This multi-agent architecture limits the blast radius of any single model's hallucination.
- **Glass Health:** A clinical decision support network that acts as a secure "peer" to human physicians, mapping symptom clusters against live literature to generate falsifiable differential diagnoses.

### 3. Open Source & Academic Frameworks
- **MedGraphRAG:** Research and data pipelines dedicated to fusing medical Knowledge Graphs with LLMs. Instead of vector-chunk retrieval, the LLM traverses established graph edges (e.g., *Gabapentin -> exacerbates -> CNS Depression*), enforcing strict biomedical logic.
- **AgentClinic:** An academic framework that simulates multi-agent interactions between a "Doctor Agent," a "Lab Tech Agent," and a "Patient Agent" to train models on extracting and diagnosing from messy, multi-year clinical histories.

## Relevance to The Brain
These architectures serve as the commercial and academic blueprint for creating the [[Workshop - Agentic Medical Data Architecture - Agentic Doctor Panel]] to automate longitudinal data synthesis for family health tracking.
