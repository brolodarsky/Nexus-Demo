---
aliases: [VALID Framework, LLM EHR Validation, Flatiron Health Framework]
tags: [ai, health-tech, mlops, research, data-quality, oncology]
type: capture
---
**Back to:** [[Table of Contents]]

---

## Overview

- **Source:** [JCO Clinical Cancer Informatics — VALID Framework](https://ascopubs.org/doi/full/10.1200/CCI-25-00215)
- **Authors:** Flatiron Health (Estevez, Singh, Dyson, Adamson, et al.)
- **Filed:** 2026-04-06

> A comprehensive framework (VALID) for evaluating the **accuracy and reliability of LLM-extracted clinical data from EHRs** in oncology — addressing hallucinations, bias, and fitness-for-purpose for research and regulatory use.

---

## The 3 Pillars of VALID

### 1. Variable-Level Performance Metrics
- Compare LLM output vs. **expert human abstraction** on a held-out test set
- Measures: **Recall, Precision, F1 score, Completeness rates**
- Key innovation: measures **relative performance difference** (LLM vs. human) rather than absolute thresholds alone
- End-to-end evaluation of **derived variables** (e.g., line-of-therapy, biomarker status at time points) is critical — compounding errors dramatically reduce accuracy

### 2. Verification Checks
- Assess for **conflicting or erroneous data points** at the patient level
- Three categories: **Conformance, Plausibility, Consistency**
- Examples:
  - Surgery date must be after diagnosis date
  - Patient can't have both positive and negative BRCA1 result
  - Metastatic diagnosis date shouldn't predate initial diagnosis

### 3. Replication & Benchmarking Analyses
- Replicate a real research question using LLM-extracted data vs. reference standard
- Tests whether **model errors compound to distort conclusions at scale**
- Can use internal (human-abstracted) or external (SEER database, published RCTs) benchmarks
- Assessed in both **broad cohorts** and **subcohorts of interest** (biomarker/treatment-based)

---

## Case Study: Real-World Progression (rwP)

- Tested across 14 cancer types (N ~1,000 per type)
- LLM-human F1 agreement within 10% for **11 of 14 cancer types**
- rwPFS survival curves derived from LLM vs. human data were **nearly identical** across all cancer types
- Validated that LLM extraction can match human-level quality in high-stakes oncology contexts

---

## Bias Assessment

- Each pillar can be **stratified by demographic subgroups** (race, age, sex) to detect differential errors
- Verification checks serve as a proxy for quality where subgroup test sets are too small for metric calculations
- Framework is **EHR-agnostic**: validated on OncoEMR, Epic, and Cerner

---

## Key Limitations

- Resource-intensive — requires multidisciplinary team (clinicians, data scientists, engineers)
- Performance measured against EHR documentation — can't recover **missing source data**
- LLM updates require **re-running validation analyses** to ensure stability

---

## Why This Matters

- Sets an **industry standard** for responsible AI use in health data pipelines
- Directly applicable to [[Project - Nexus Non-Engine Functionality Upgrades]] Universal Capture strategy (validating AI-extracted structured data from clinical documents)
- Relevant to MEMBilling's LLM-based medical record processing

---

## Connections

- Related to [[Retrieval Augmented Generation (RAG)]] — downstream quality assurance
- Related to [[Prompt Engineering]] — iterating prompts based on VALID error analysis
- See [[Health Summary]] — personal health data context
