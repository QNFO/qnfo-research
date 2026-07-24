---
created: 2026-07-24
tags: [literature-review, AI-gate-check, LLM-science-evaluation, PQS, Bell-theorem]
---

# Literature Classification: LLM Gate-Check for Fringe Physics Claims

## Classification Matrix

| Class | Count | Criteria |
|:------|:------|:---------|
| **Core** | 7 | Directly addresses LLM scientific claim verification or benchmark |
| **Supporting** | 8 | Adjacent: misinformation detection, scientific NLP, claim extraction |
| **Background** | 12 | Bell's theorem, quantum foundations, hidden variables |
| **Reject** | 5 | Insurance claims, quantum dot entanglement (off-topic) |

---

## Core Papers (7)

### 1. CLAIM-BENCH: "Can AI Validate Science?" (Javaji et al., 2025)
- **arXiv:** 2506.08235v1
- **Relevance:** 🔴 HIGHEST — Directly evaluates LLM ability to reason about scientific claim-evidence relationships. Builds a benchmark for claim → evidence extraction. This is the closest external work to our gate-check convergence finding.
- **Key finding:** LLMs can extract claims but struggle with complex evidence reasoning.
- **Gap vs our work:** Their benchmark tests single-LLM performance; our finding adds cross-model convergence as an independent verification signal.

### 2. SCITAB: Compositional Reasoning on Scientific Tables (Lu et al., 2023)
- **arXiv:** 2305.13186v3
- **Relevance:** 🟠 HIGH — 1.2K expert-verified scientific claims requiring compositional reasoning. Demonstrates that even state-of-the-art LLMs struggle with multi-step scientific fact-checking.
- **Key finding:** GPT-4 achieves only 51% accuracy on compositional scientific claim verification.
- **Gap:** Tests tabular evidence only, not physics-theoretical claims like PQS.

### 3. Climinator: Automated Fact-Checking of Climate Claims (Leippold et al., 2024)
- **arXiv:** 2401.12566v1
- **Relevance:** 🟠 HIGH — Mediator-Advocate framework for LLM-based scientific claim evaluation. Closest methodological analog to our Claude-vs-Gemini convergence finding.
- **Key finding:** Multi-LLM adversarial framework produces robust evaluations. Our finding goes further: convergence emerges WITHOUT adversarial prompting.

### 4. "Can Large Language Models Detect Misinformation in Scientific News Reporting?" (Cao et al., 2024)
- **arXiv:** 2402.14268v2
- **Relevance:** 🟡 MEDIUM-HIGH — Specific to scientific domain misinformation (not general fake news). Tests LLM ability to distinguish accurate vs distorted scientific reporting.
- **Key finding:** LLMs can detect surface-level scientific misinformation but struggle with subtle distortions.

### 5. SciFact / RerrFact: Scientific Claim Verification (Rana et al., 2022)
- **arXiv:** 2202.02646v2
- **Relevance:** 🟡 MEDIUM — Reduced evidence retrieval for scientific claim verification. Demonstrates the retrieval bottleneck in scientific fact-checking.
- **Key finding:** Evidence retrieval is the primary bottleneck, not reasoning per se.

### 6. "Evaluating LLM Performance in Scientific Claim Detection" (Faruk, 2024)
- **arXiv:** 2412.16486v1
- **Relevance:** 🟡 MEDIUM — COVID-19 infodemic context; tests LLM claim detection. Less physics-specific but demonstrates general scientific claim detection capability.

### 7. ClaimFlow: Tracing Evolution of Scientific Claims in NLP (Pramanick et al., 2026)
- **arXiv:** 2603.16073v2
- **Relevance:** 🟡 MEDIUM — 5,689 manually annotated scientific claims across 1,617 ACL papers. Shows that claim tracking is tractable at scale but requires structured knowledge graphs.

---

## Supporting Papers (8)

| Paper | Year | Relevance |
|:------|:-----|:----------|
| "Combating Misinformation in the Age of LLMs" (Chen & Shu) | 2023 | LLMs as double-edged sword for misinformation |
| "Can LLM-Generated Misinformation Be Detected?" (Chen & Shu) | 2023 | Taxonomy of LLM-generated misinformation |
| "Beyond Binary: Fine-Grained LLM-Generated Text Detection" (Cheng et al.) | 2024 | Role recognition in human-LLM collaboration |
| "Fine-Grained Bias Detection in LLM" (Mohanty) | 2025 | Nuanced bias detection framework |
| "CCSBench: Compositional Controllability in Scientific Summarization" (Ding et al.) | 2024 | Scientific document evaluation |
| "Large Language Models to the Rescue" (Sänger et al.) | 2023 | LLM-assisted scientific workflow |
| "Evaluating Hydro-Science Knowledge of LLMs" (Hu et al.) | 2025 | Domain-specific LLM knowledge evaluation |
| "Fact4ac: Financial Misinformation Detection" (Hoang & Nguyen) | 2026 | Domain-specific fact-checking (financial analog) |

---

## Background Papers — Bell's Theorem & Quantum Foundations (12)

| Paper | Year | Key Point |
|:------|:-----|:----------|
| "The Two Bell's Theorems of John Bell" (Wiseman) | 2014 | 1964 vs 1976 theorems distinguished; locality+determinism vs local causality |
| "Causarum Investigatio and Bell's Theorems" (Wiseman & Cavalcanti) | 2015 | Formal clarification of Bell's assumptions |
| "Bell's theorem tells us NOT what QM IS, but what QM IS NOT" (Zukowski) | 2015 | Non-locality buzzword critique; Bell excludes LHV, doesn't prove non-locality |
| "Bringing Bell's theorem back to Particle Physics & Cosmology" (Hiesmayr) | 2015 | Bell in broader physics context |
| "Going Beyond Bell's Theorem" (Greenberger, Horne, Zeilinger) | 2007 | GHZ-type extensions |
| "Bell's theorem as signature of nonlocality: classical counterexample" (Matzkin) | 2007 | Classical model claiming Bell violation — **physics status: refuted by loophole-free tests** |
| "Bell's Theorem Without Hidden Variables" (Stapp) | 2000 | Theoretical critique of hidden-variable framing |
| "On the existence of local quasi hidden variable model" (Loubenets) | 2016 | Mathematical bounds on Bell violations |
| "Single-copy activation of Bell nonlocality" (Bowles et al.) | 2020 | Modern nonlocality research |
| "Kolmogorov probability and quantum phenomena" (Reddiger) | 2024 | Foundation-level probability theory analysis |
| "Reconsidering Local Hidden Variables: When One is Enough" (Schneeloch et al.) | 2016 | Single-LHV models |
| "Quantum computation and hidden variables" (Aristov & Nikulov) | 2010 | Hidden variables in quantum computing context |

---

## Key Gap Identified

**No existing work tests cross-model convergence as a gate-check signal.** The CLAIM-BENCH, SCITAB, and Climinator papers all evaluate single-LLM performance against ground truth. None tests whether two independent AI systems (different architectures, training data, parent organizations) converge on the same evaluation of fringe scientific claims. Our PQS case study fills this gap.

## Bibliography (Core + Key Supporting)

1. Javaji et al. (2025). "Can AI Validate Science? Benchmarking LLMs for Accurate Scientific Claim → Evidence Reasoning." arXiv:2506.08235.
2. Lu et al. (2023). "SCITAB: A Challenging Benchmark for Compositional Reasoning and Claim Verification on Scientific Tables." arXiv:2305.13186.
3. Leippold et al. (2024). "Automated Fact-Checking of Climate Change Claims with Large Language Models." arXiv:2401.12566.
4. Cao et al. (2024). "Can Large Language Models Detect Misinformation in Scientific News Reporting?" arXiv:2402.14268.
5. Rana et al. (2022). "RerrFact: Reduced Evidence Retrieval Representations for Scientific Claim Verification." arXiv:2202.02646.
6. Chen & Shu (2023). "Combating Misinformation in the Age of LLMs." arXiv:2311.05656.
7. Chen & Shu (2023). "Can LLM-Generated Misinformation Be Detected?" arXiv:2309.13788.
8. Faruk (2024). "Evaluating the Performance of Large Language Models in Scientific Claim Detection." arXiv:2412.16486.
9. Pramanick et al. (2026). "ClaimFlow: Tracing the Evolution of Scientific Claims in NLP." arXiv:2603.16073.
10. Wiseman (2014). "The Two Bell's Theorems of John Bell." J. Phys. A 47, 424001.
11. Hensen et al. (2015). "Loophole-free Bell inequality violation using electron spins." Nature 526, 682-686.
12. Aspect, Clauser, Zeilinger (2022 Nobel Prize in Physics). "For experiments with entangled photons, establishing the violation of Bell inequalities."
