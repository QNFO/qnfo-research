# Finite-Distinction Quantum Mechanics

Unitary Evolution and Superposition as the Large-Distinction Limit of Stochastic
Thermodynamics

**Author:** Rowan Brad Quni-Gudzinas (QNFO) · **Version:** 1.0.1 (2026-08-21) ·
**License:** CC-BY-4.0 · **DOI:** PENDING-ZENODO

## About this paper

A single real coordinate, taken literally, specifies infinitely many yes/no
distinctions. This paper assembles the consequences of that observation into three
claims, each graded by its strength. First, uncountable precision is unphysical,
while computable depth and p-adic valuation remain physically real — a refinement
of the finite-information principle. Second, the geometry of finite distinctions is
combinatorial: at any fixed resolution two states are either distinct or not, and
the induced distance is ultrametric. Third — the conjecture-grade claim — quantum
mechanics read as thermodynamics is a stochastic thermodynamics of finite
alternatives, in which unitary evolution and superposition emerge as the
large-distinction limit of an entropy-Hessian flow; the Hilbert-space formulation
over the complex numbers is that limit, a map rather than the territory. The first
two claims are derived or inherited; the third is stated with its named obstacles
and with five written falsification conditions that a seeded, deterministic
computational program executes.

## Contents

| File | Purpose |
|---|---|
| `finite-distinction-quantum-mechanics.md` | The paper (source markdown) |
| `finite-distinction-quantum-mechanics.html` | Rendered HTML |
| `finite-distinction-quantum-mechanics.pdf` | Rendered PDF |
| `references.bib` | Bibliography (37 entries, all live-verified) |
| `citation-audit.md` | Per-entry citation verification record |
| `PROJECT-PLAN.md` | Project record: claims, grades, lock records |
| `README.md` | This file |
| `docs/` | Hypothesis cards, due-diligence record, outline, audit reports, seed-note transcriptions |
| `artifacts/` | Ignorance-audit chain and external-search evidence |
| `artifacts/verification/` | The computational verification program, its run log, and results |

## Reproducing the verification

Every quantitative claim in Section 9 of the paper is verified in code before it is
asserted. The verification program is deterministic, standard-library-only, and
re-runnable with a single command:

```
cd artifacts/verification
python finite-distinction-verification.py
```

Reproducibility: seed 20260821, CPython 3.12.10 (Windows), no third-party
dependencies, runtime about 14–16 s. The script regenerates the machine-readable
results file; only the wall-clock field varies between runs. Seven checks execute
the paper's falsification conditions, each with a live falsifier control showing
the test would catch a non-vanishing construction.

## Citation

Please cite the record DOI (see the Zenodo record page for the version-specific
citation string).
