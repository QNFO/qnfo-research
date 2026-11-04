# Infomatics v2 — Evidence-Based Literature Survey

**Status:** Phase 0 — Project Initialization  
**Repository:** [rwnq8/infomatics-v2](https://github.com/rwnq8/infomatics-v2)  
**Protocol:** research v2.4 compliant

---

## What This Is

A systematic, evidence-based audit of claims about "information as fundamental substrate" across physics literature. We search external sources (arXiv, Semantic Scholar, INSPIRE) and cross-reference QNFO-internal work. Every claim receives a transparent classification:

- **[Established]** — Peer-reviewed experimental evidence or mathematical theorems
- **[Open]** — Active research, no consensus
- **[Speculative]** — Theoretical proposal, no experiment
- **[Disconfirmed]** — Contradicted by evidence
- **[QNFO-Internal]** — No external citations or validation

## What This Is NOT

- NOT an axiomatic framework claiming to derive physical constants
- NOT numerology (137 is prime, etc.)
- NOT a source of unverified LLM-recalled citations
- NOT a QNFO self-referential loop

## Why v2

v1 (rwnq8/infomatics) made three errors: (1) Eddington-style numerology claiming α derives from p=137, (2) LLM-generated citations never verified, (3) QNFO-internal claims presented as established physics. v2 starts fresh with evidence-based methodology.

## Quick Start

1. See [PROJECT-PLAN.md](PROJECT-PLAN.md) for full charter and WBS
2. See [notebooks/rubric.md](notebooks/rubric.md) for the classification system
3. See [RISK-REGISTER.md](RISK-REGISTER.md) for identified risks
4. Phase reports in [artifacts/](artifacts/)

## Project Structure

```
infomatics-v2/
├── README.md
├── PROJECT-PLAN.md
├── RISK-REGISTER.md
├── DELIVERABLE-REGISTRY.md
├── .gitignore
├── docs/           # Reference papers, external PDFs
├── artifacts/      # Phase deliverables, search reports
├── notebooks/      # Working notes, classification drafts
└── releases/       # Versioned publication bundles
```
