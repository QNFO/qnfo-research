# From Distinction to Dissipation

**Companion Essay and Executable Toy-Model Suite for the Boson/Fermion Distinction Program**

Author: Rowan Brad Quni-Gudzinas (QNFO) · ORCID 0009-0002-4317-5604 · 2026-08-15
DOI: 10.5281/zenodo.21940822 · License: CC-BY-4.0 (record) / QNFO-ULA (source)

## What this is

A disciplined companion essay plus four executable toy models answering the
deep-inquiry question *"what is the cost of drawing a boundary?"* for a
distinction-based (Laws-of-Form-style) foundation of physics.

## Contents

| File | Role |
|---|---|
| `from-distinction-to-dissipation.md` / `.html` / `.pdf` | The companion essay (labels: [ESTABLISHED] / [RETRODICTION] / [NOT YET EVIDENCE] / [EXTRAPOLATION]) |
| `notebooks/t1-t2-dill-full-check.md` | T1/T2 DiLL full check — the two exponentials and the abelian-pair finding (v1.1) |
| `notebooks/t4-toy-model.py` (+ `.md`) | Statistics from syntactic exchange — no hand-imposed sign (REG-009-001) |
| `notebooks/t5-boundary-cost-model.py` (+ `.md`) | Boundary cost — the draw is free, the upkeep is not (REG-009-002) |
| `notebooks/t6-capacity-bound.py` (+ `.md`) | Capacity ceiling floor(ΔS / k_B ln 2) (REG-009-003) |
| `notebooks/t7-second-law-gated-braid.py` (+ `.md`) | Second-law-gated braids — exact discrete-chain solution (REG-009-004) |
| `docs/fq3-irreversibility-mapping.md` | Where the arrow of time enters the mark calculus |
| `docs/toy-model-suite-deposit.md` | Publication decision + pre-publish verification record |
| `RESEARCH-CONTINUITY-REGISTRY.md` | Frontier questions, pre-registered predictions, falsifiability ledger |
| `citation-audit.md` | Citation verification record for the essay |
| `references.bib` | BibTeX for the essay's references |
| `PROJECT-PLAN.md` | Project plan of the parent program (QNFO.RES.009) |

## v1.4 (2026-08-15) — essay wording + references remediation

Essay §3 heading corrected from "(pre-registered, unexecuted)" to "(pre-registered;
structural checks executed)" (the T1/T2 check is executed and bundled); Jabs and Lev
added to the essay References; record `language: eng`; bundled registry + deposit doc
refreshed with post-publish snapshots.

## v1.1 (2026-08-15) — post-publication red-team remediation

Corrected `t5-boundary-cost-model` and `t6-capacity-bound`: functional H2/H3/G3
disconfirmation conditions (exchange eigenvalues now computed, not asserted) and
clarified Bit semantics (None = blank reference state). Added the T1/T2 DiLL full-check
notebook (referenced by the registry but previously omitted from the bundle).

## Honest scoping

All toy-model results are labeled **[TOY MODEL — SYNTACTIC]** / **[NOT YET
EVIDENCE]**: they are executable demonstrations of internal consistency, not
physical derivations. The suite complements the published paper *The
Boson/Fermion Distinction: Spin-Statistics as Structural Invariant*
(doi:10.5281/zenodo.21938971) and its frontier follow-ups.

## Running the models

```
python notebooks/t4-toy-model.py
python notebooks/t5-boundary-cost-model.py
python notebooks/t6-capacity-bound.py
python notebooks/t7-second-law-gated-braid.py
```

Pure Python, no external dependencies. Each prints PASS/FAIL verdicts for its
pre-registered hypotheses (all PASS as of 2026-08-14, second pass).

## Provenance

This suite originates from the 2026-08-14 deep-inquiry analysis of the
distinction program (Obsidian notes `_26226214708`, `_26226215159`,
`_26226215536`) and the RES.009 continuity registry maintained on branch
`res/paper/spin-statistics-distinction` of QNFO/qnfo-research.
