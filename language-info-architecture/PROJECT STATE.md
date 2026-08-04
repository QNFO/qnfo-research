# PROJECT STATE: Language-Info-Architecture

**Last Updated:** 2026-05-12
**Current Branch:** feature/consolidate-cross-ratio-convergence
**Active Phase:** COMPLETE — Capstone written, ready for review and merge

---

## What This Project Is

This project has undergone three major phases:

1. **Phase 1 (Sapir-Whorf):** Original simulation study testing whether frequency of encoding predicts Whorfian cognitive effects. Produced a null result that was predetermined by synthetic data independence. (0.1.md–0.4.md)
2. **Phase 2 (Information Architecture):** Complete reframing as a Jakobson/Shannon/Grice/Greenberg investigation of mandatory information in human communication. Found: entropy gradient across morphological types, compression-tax trade-off ($r = -0.48$), and zero epistemic-ontological intersection. (0.5.0.md–0.6.0.md)
3. **Phase 3 (Paths A+B+C):** Deepened analysis across three connected paths — expanded mutual exclusion testing (8 domains), scientific register comparison, and cross-project synthesis bridging to the parent repo's Cross-Ratio Convergence framework. (0.7.0.py–0.10.0.md)

## File Inventory

| File | Description | Phase |
|:-----|:------------|:------|
| `0.1.md` | Initial inquiry + LLM web search log (~97KB) | 1 |
| `0.1.1.md` | Original Sapir-Whorf research plan (~18K words) | 1 |
| `0.1.2.md` | Refined Sapir-Whorf plan with 13 gaps addressed | 1 |
| `0.3.py` | Sapir-Whorf MCMC simulation pipeline | 1 |
| `0.3_results.json` | Sapir-Whorf results — frequency vectors, loads | 1 |
| `0.4.md` | Sapir-Whorf results writeup | 1 |
| `0.5.0.md` | **Reframed plan** — Jakobson/Shannon/Grice/Greenberg | 2 |
| `0.5.0.py` | **Reframed pipeline** — entropy, mandatory architecture, PCA | 2 |
| `0.5.0_results.json` | **Reframed results** — information architecture data | 2 |
| `0.6.0.md` | **Reframed results writeup** — 6 key findings | 2 |
| `0.7.0.py` | **Path A+B pipeline** — mutual exclusion + science register | 3 |
| `0.7.0_results.json` | **Path A+B results** | 3 |
| `0.8.0.md` | **Path A writeup** — The Mutual Exclusion Principle | 3 |
| `0.9.0.md` | **Path B writeup** — Scientific Register Comparison | 3 |
| `0.10.0.md` | **Path C writeup** — Cross-Project Synthesis (bridge to convergence) | 3 |
| `0.11.0.md` | **Capstone** — Project Retrospective & Close-Out | Final |
| `0.12.0.md` | **Preprint** — Standalone synthesis: Language as Information Architecture | Final |

## Core Findings

1. **Entropy gradient:** Isolating (6.48 bits) $\to$ polysynthetic (6.80 bits/word) — clear, monotonic, predicted
2. **Compression-tax trade-off:** $r(H, L_{\text{total}}) = -0.484$ — richer morphology substitutes for explicit category marking
3. **Mutual exclusion:** 10 of 28 domain pairs are empty ($p < 0.0001$) — languages specialize in one mandatory cluster
4. **Four mandatory clusters:** Reference-tracking, source-tracking, categorical-judgment, spatial-coordinate — mutually exclusive
5. **Epistemic convergence:** Scientific registers in 8 languages converge to ~2.5% epistemic load — universal scientific discourse architecture
6. **Shannon entropy as invariant:** Bridges linguistic information theory to geometric cross-ratio tradition — entropy is invariant under recoding

## Current State

- All three paths executed and documented
- Cross-project bridge to Cross-Ratio Convergence framework established
- Project proposes re-inclusion in convergence synthesis based on Shannon entropy (invariant under recoding) as structural analogue to the geometric cross-ratio (invariant under projective transformation)

## Next Steps

1. **Cross-reference with WALS:** Validate mutual exclusion findings against World Atlas of Language Structures
2. **Real corpus validation:** Compare synthetic entropy gradients to real corpus data
3. **Expand language sample:** 22 languages underrepresents world diversity — aim for 100+
4. **Submit for re-inclusion:** Present 0.10.0.md to Cross-Ratio Convergence project for synthesis integration

## Known Issues

- All frequency data is synthetic (Python-generated from typological priors)
- "Word" is not cross-linguistically valid — entropy gradient partially reflects tokenization conventions
- 22-language sample limits statistical power for individual pair tests
- The mutual exclusion principle needs validation against real typological databases (WALS)
