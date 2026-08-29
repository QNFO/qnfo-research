# Phase 2 Literature Triage — QNFO.RES.031

- **Date:** 2026-08-29 · **WBS:** QNFO.RES.031.P2
- **Inputs:** the 39-record internal sweep (12 formulations, `artifacts/external-search/corpus-sweep-2026-08-29.json`), the external verification set (`artifacts/external-search/external-verification-2026-08-29.json`), and the corrected-dictionary target (C1–C4 locked at Phase 0).
- **Method:** Phase 1 evidence was re-read, not re-queried (skip re-audit); this document classifies and symmetrizes per KIF-18.

## 1. Classification Matrix

| Class | Criterion | Records |
|---|---|---|
| **S1 — CORE** (directly on the correspondence) | External: Julia 1990 (10.1007/978-3-642-75405-0_30), Spector 1990 (10.1007/bf02096755), Bakas–Bowick 1991 (10.1063/1.529511), Bost–Connes 1995 (10.1007/bf01589495), JHEP 07(2025)281 (arXiv:2502.02661), JHEP 11(2025)160 (arXiv:2507.08788). Internal: RES.027 (10.5281/zenodo.22133122), RES.028 (10.5281/zenodo.22124744), RES.029 (10.5281/zenodo.22142794), RES.030 (10.5281/zenodo.22152967), spectral-schism, prime-numbers-as-spectral-artifacts, consilience-physics-numtheory (10.5281/zenodo.21590155). | Carry the identities and the zeros/primes split; RES.027 already publishes C1's core — cited as source, not repeated as novel. |
| **S2 — METHOD** (estimator construction) | Montgomery 1973 (10.1090/pspum/024/9944), Odlyzko 1987 (10.1090/s0025-5718-1987-0866115-0), Gallagher 1976 (10.1112/s0025579300016442), UMP.014 (10.5281/zenodo.22150472, sim-riemann-zeros-fast.py), RES.030 (sim-spectral-estimators.py). | Six-bug checklist source; RES.030 R-1 exact two-point reduction is the reference for number variance. |
| **S3 — INTERPRETIVE** (ladder, pre-arithmetic) | UMP.014, SLB.001 idempotent-core (10.5281/zenodo.21916939), LoF Number Builder (archive `lof-number-builder-interactive-specification-v10`), ultrametric-program v2.5.1 (10.5281/zenodo.22076816), reentrant-distinctions (10.5281/zenodo.21905186), RES.021 (10.5281/zenodo.22046458). | Prior claimants of L0–L1 (priority credited in PROJECT-PLAN); ladder L2–L4 structure is RES.031's own. |
| **S4 — ADJACENT** (statistics, p-adic QM, thermodynamics) | RES.009/010/011 (spin-statistics, exchange scalar, config-space topology), pattern-particle-unification (UMP.013), ultrametric-foundation (10.5281/zenodo.21993481), ultrametric-quantum-computation-langlands, emergent-number-theory (10.5281/zenodo.17499279), self-referential-scalar-family (RES.020, 10.5281/zenodo.22035210), thermodynamics-of-structural-persistence, kinetic-isomorphism, thermodynamic-genesis-of-the-standard-model. | Constrain the "no exchange phase in the Gentile family" statement (RES.028 already adjudicated) and the C4 negative list framing. |

## 2. KIF-18 Symmetry Template

| Claim | SUPPORTS (external first) | CONSTRAINS / CONTRADICTS |
|---|---|---|
| **C1 exact dictionary** | Julia 1990 (zeta = partition function folklore); Spector 1990 (Fermi squarefree origin); Bakas–Bowick 1991 (arithmetic gases); RES.027 publishes the identities; RES.028 the Gentile family; JHEP 2025 papers use the construction in current research. | Nothing contradicts the identities (theorem-level). Constraint: the correspondence is long-known — novelty claim is thereby excluded; the record's novelty is C2/C3/C4. |
| **C2 five-level ladder (L2 ≠ L4)** | UMP.014 (distinction-based ultrametric as realization-independent structure); ultrametric-program (object = inequality + hierarchy, not arithmetic); RES.021 (finite-distinction QM); SLB.001 (cut to arithmetic is constructed, not discovered). | The pre-arithmetic cut is already claimed (SLB.001, LoF Number Builder) — RES.031 credits, not claims. The ladder's inference rules themselves have no external precedent (gap, not constraint). |
| **C3 correction ledger** | RES.030 D-1 (Dyson window mismatch adjudicated), D-4 (316.3 finite-cutoff crossover), R-1 (exact two-point reduction), 34σ attribution (focused hard-core z ≈ 33.8σ, uniform z ≈ −0.8); UMP.014 real-data nulls. | RES.030's own results bound every row: the fixes must be consistent with D1 CONFIRMED / D2 disconfirmed. The 316.3 value is an adjudication target, not a recoverable anchor (red-team M-1). |
| **C4 negative discipline** | Gallagher 1976 (primes Poisson beyond hard core) — separates zeros (GUE) from primes; Bost–Connes (pole is KMS/infinite-mode, not free-gas BEC) — supports the "no Hilbert–Pólya evidence" negative; JHEP 2025 (external users do not claim physical realization). | The record must not let the "same statistical language" framing re-import an L2→L4 slide (UIA Q1 scaffold; Novelty-slot Defect A). |

## 3. Triage verdicts

- **Classification completeness:** all 39 swept records are classified above; **0 records in Reject** (no swept record contradicts the locked claim set). The S1–S4 shape maps to the canonical matrix as S1 = Core, S2 = Method/Supporting, S3 = Supporting/Interpretive, S4 = Supporting/Background (red-team A2 annotation, 2026-08-29).
- **S1 CORE:** cite all; RES.027–030 as the internal source chain, external 1990–2025 as the correspondence's provenance. The two JHEP 2025 papers are first-class currency evidence (Phase 1 gap analysis).
- **S2 METHOD:** adopt the six-bug checklist wholesale for §V of the corrected dictionary; the exact two-point reduction (RES.030 R-1) replaces the Dyson asymptotic as the number-variance reference.
- **S3 INTERPRETIVE:** cite as prior claimants in Part I; no new claim on L0–L1.
- **S4 ADJACENT:** cite where the negative list touches statistics (RES.028 adjudication of the no-exchange-phase family), p-adic QM (ultrametric-foundation), and thermodynamic framing (RES.020).
- **No record contradicts the locked claim set.** KIF-16 clean; KIF-17: this triage is AI-generated, grounded on re-read evidence files, not on model priors.
