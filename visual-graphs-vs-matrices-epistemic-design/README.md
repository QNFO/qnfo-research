# Visual Graphs vs Matrices: Epistemic Limits, Cognitive Preference, and the Design of Understandable Computation

**WBS:** QNFO.RES.019 · **Branch:** res/paper/visual-graphs-vs-matrices-epistemic-design · **2026-08-20**

## Abstract

The ZX calculus and the matrices of linear algebra denote exactly the same maps. A field that knows this has, nonetheless, converged on the pictures. This paper argues that the convergence is not a matter of taste and not a matter of mathematics: it is a fact about bounded cognition. Where comprehension and optimality diverge, the field splits the difference into a two-layer structure — a human-auditable canonical fragment and an automated optimizer over it — and the design principle it licenses is the one the last decade of quantum software has already been practicing: we design systems that design algorithms that optimize themselves and other systems, with legibility as a first-class constraint. All quantitative claims are computationally verified; the verification scripts are deposited with this record.

## Files in this release

| File | Purpose |
|---|---|
| `visual-graphs-vs-matrices-epistemic-design.md` | Paper source (Markdown, external-facing prose) |
| `visual-graphs-vs-matrices-epistemic-design.html` | Paper (HTML, pandoc standalone) |
| `visual-graphs-vs-matrices-epistemic-design.pdf` | Paper (PDF, Chromium CDP render) |
| `references.bib` | 16 verified bibliography entries (P3.AUTHOR-GATE) |
| `citation-audit.md` | Zero-context citation verification ledger |
| `PROJECT-PLAN.md` | Phase plan, locked core claim, H-VISUAL card, risk register |
| `README.md` | This file |
| `docs/deep-research.md` | Gap analysis + SO-WHAT + practitioner section |
| `artifacts/universal-ignorance-audit.md` | UIA (15 questions) on the core claim |
| `artifacts/external-search/corpus-sweep-2026-08-20.md` | Corpus sweep + external verification evidence |
| `artifacts/verification/verify-claims.py` | Computational verification script (COMPUTATIONAL-VERIFICATION-1) |
| `artifacts/verification/verify-claims.log` | Verification output (9/9 checks PASS) |
| `artifacts/verification/verify-claims.json` | Machine-readable verification results |
| `figures/fig1-two-layer-structure.svg` | Figure 1: the two-layer structure |

## Provenance

- GitHub provenance: https://github.com/QNFO/qnfo-research/tree/res/paper/visual-graphs-vs-matrices-epistemic-design (deposited as related_identifier isSupplementTo)
- Seed: vault note `_26232092415` (2026-08-20) + thesis brief `_visual-graphs-vs-matrices-epistemic-design-2026-08-20.md`
- Phase 0 (2026-08-20): WBS claim QNFO.RES.019, PROJECT-PLAN, core-claim lock, UIA
- Phase 1 (2026-08-20): full-corpus sweep (KG 8,317 nodes), Crossref/arXiv external verification, gap analysis
- Phase 2–4 (2026-08-20): bibliography + citation audit, paper draft, computational verification (9/9 PASS), red-team audit (3 HARD + 7 SOFT — all remediated)
- Phase 5 (2026-08-20): publication — Zenodo 10.5281/zenodo.22031417

## How to reproduce the verification

```
python artifacts/verification/verify-claims.py
```

Python 3.12 + numpy only; no randomness; runtime under thirty seconds; all quantitative claims in the paper are the script's output.
