# Language-Info-Architecture

**Final State — COMPLETE**

**DOI:** [10.5281/zenodo.20137616](https://doi.org/10.5281/zenodo.20137616)
**GitHub:** [github.com/rwnq8/language-info-architecture](https://github.com/rwnq8/language-info-architecture)

---

## What This Project Became

Originally a casual inquiry into word frequencies and the Sapir-Whorf hypothesis, this project transformed across three phases into an investigation of **language as information architecture** — treating human languages as communication channels with different mandatory metadata requirements, analysed through the lenses of Roman Jakobson, Claude Shannon, Paul Grice, and Joseph Greenberg.

## Core Framework

| Theorist | Contribution | Application |
|:---------|:-------------|:------------|
| **Jakobson (1959)** | Languages differ in what they *must* convey | Quantified mandatory vs. optional encoding across 22 languages |
| **Shannon (1948)** | Information is measurable in bits | Computed entropy per word-form and per morpheme |
| **Grice (1975)** | Cooperative communication requires optimal informativeness | Measured Gricean surplus — forced over-informativeness |
| **Greenberg (1963)** | Implicational universals constrain possible languages | Tested mutual exclusion as a candidate universal |

## Key Findings

1. **Entropy gradient:** Isolating (6.48 bits) → polysynthetic (6.80 bits/word) — clear monotonic trend
2. **Compression-tax trade-off:** $r(H, L_{\text{total}}) = -0.48$ — richer morphology substitutes for explicit category marking
3. **Mutual exclusion:** 10 of 28 domain pairs are empty ($p < 0.0001$) — languages specialize in one mandatory cluster
4. **Four mandatory clusters:** Reference-tracking, source-tracking, categorical-judgment, spatial-coordinate — mutually exclusive
5. **Epistemic convergence:** Scientific registers converge to $\sim$2.5% epistemic load across 8 languages (8.8$\times$ increase)
6. **Cross-project bridge:** Shannon entropy as invariant under recoding — structural analogue to the geometric cross-ratio

## Project Arc

| Phase | Framing | Central Question | Status |
|:------|:--------|:-----------------|:------:|
| 1 | Sapir-Whorf | Does frequency cause cognitive effects? | Null result (predetermined by synthetic data independence) |
| 2 | Jakobson/Shannon | What mandatory information do languages force? | 6 coherent findings |
| 3 | Paths A+B+C | Can we deepen, extend, and bridge? | Mutual exclusion principle, science register analysis, cross-project synthesis |

## Status

**COMPLETE.** The project has been executed, documented, and retrospectively assessed. All 13 versioned files and 7 documentation files are committed. The feature branch (`feature/consolidate-cross-ratio-convergence`) is ready for review and merge.

**Important caveat:** All numerical findings depend on synthetic data generated from LLM-informed priors. The methodology is sound; the specific numbers are illustrative. Real-data validation (WALS, real corpora, psycholinguistic meta-analyses) is the necessary next step for anyone who wants to take this further.

## File Inventory

| File | Role |
|:-----|:-----|
| `0.1.md` — `0.4.md` | Phase 1: Sapir-Whorf (original simulation) |
| `0.5.0.md` — `0.6.0.md` | Phase 2: Information Architecture (reframing) |
| `0.7.0.py` — `0.10.0.md` | Phase 3: Paths A+B+C (deepening, extension, bridge) |
| `0.11.0.md` | **Capstone** — Project Retrospective |

## Next Steps (For Real-Data Validation)

1. Cross-reference mutual exclusion against WALS (World Atlas of Language Structures)
2. Compute entropy gradients from real parallel corpora
3. Test compression-tax trade-off with WALS-validated mandatory assignments
4. Compare scientific register entropy using real scientific corpora

## Constraints

All work performed via LLM orchestration with embedded Python execution within a single chat thread. Self-contained. No external data access.
