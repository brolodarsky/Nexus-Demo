---
aliases: [Granite-Docling, IBM Docling, SmolDocling]
tags: [ai, document-processing, rag, mlops, ocr, vision-language-model]
type: capture
---
**Back to:** [[Table of Contents]]

---

## Overview

- **Source:** [IBM Think — Granite-Docling: End-to-end document understanding with one tiny model](https://www.ibm.com/think/news/granite-docling)
- **Published:** 2025-09-24
- **Filed:** 2026-04-06

> IBM's **Granite-Docling-258M** is an ultra-compact open-source Vision-Language Model (VLM) that converts documents (PDFs, slides, infographics) to fully structured, machine-readable formats while preserving layout, tables, equations, and code — purpose-built for RAG pipelines.

---

## Key Facts

- **258M parameters** — rivals systems several times its size in accuracy
- Available on [HuggingFace](https://huggingface.co/ibm-granite/granite-docling-258M) under **Apache 2.0 license**
- Successor to SmolDocling-256M-preview (replaces SmolLM-2 backbone with Granite 3 + SigLIP2)
- Addresses instability issues from SmolDocling (loop/repetition bugs fixed via dataset filtering)

---

## Core Innovation: DocTags

- **DocTags** = IBM's universal markup format for documents
  - Captures all page elements: charts, tables, forms, code, equations, footnotes, captions
  - Separates textual content from document structure → minimizes token count and ambiguity
  - Enables Granite-Docling to isolate each element, describe its location, and perform OCR within it
  - Output converts cleanly to **Markdown, JSON, or HTML**
- Conventional OCR (e.g., raw Markdown conversion) is lossy; DocTags preserves structural fidelity

---

## Why It Matters for RAG

- Ideal upstream parser for [[Retrieval Augmented Generation (RAG)]] pipelines
- Handles inline math, floating equations, code blocks — things standard OCR destroys
- Designed to work *within* the [Docling library](https://www.docling.ai/) for ensemble pipelines
- Combining Granite-Docling + Docling library = best of single-pass accuracy + customizable pipeline

---

## Multilingual Support (Experimental)

- Arabic, Chinese, Japanese support added (beyond Latin-script SmolDocling)
- Not yet enterprise-validated for non-Latin scripts — ongoing priority

---

## Roadmap

- Larger models planned: ~512M and ~900M (all <1B parameters)
- DocTags to be added to IBM Granite tokenizer vocabulary
- Integration with IBM watsonx.ai workflows

---

## Resources

- [HuggingFace Model Card](https://huggingface.co/ibm-granite/granite-docling-258M)
- [Docling Library](https://www.docling.ai/)
- [RAG Tutorial with Docling + Granite](https://www.ibm.com/think/tutorials/build-multimodal-rag-langchain-with-docling-granite)
- [SmolDocling Paper (ICCV 2025)](https://arxiv.org/abs/2503.11576)

---

## Connections

- See [[Retrieval Augmented Generation (RAG)]] — this is a key upstream tool
- See [[Vector Databases]] — output feeds directly into embedding pipelines
- Related to [[Prompt Engineering]] — DocTags structured output improves downstream LLM prompting
