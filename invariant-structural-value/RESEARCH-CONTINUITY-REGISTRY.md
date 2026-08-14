# RESEARCH-CONTINUITY-REGISTRY.md — Invariant Structural Value (QNFO.RES.007)

Created: 2026-08-14 · Living document — maintained with version bumps. Branch: res/paper/invariant-structural-value.

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:----------------|
| FQ1 | What is the minimal generative primitive from which the full set of structural constants (e, π, i) follows — can a mark/distinction calculus with self-reference generate them without additional input, and does compact-closed structure supply the trace/feedback semantics that makes the derivation well-posed? | COMPLETE — constructive derivation committed 2026-08-14 (01f4018): e as unique fixed point of T[f]=f′ (Picard iteration → series), π via self-closure (periodic BC; exp: ℝ→U(1) kernel 2πℤ), Euler identity as joint fixed point; compact-closed trace semantics stated (U(1) exponential map) | P5 BP-1..BP-10 gates (fit-verify, independent recompute of e/π/e^{iπ}+1) | YES |
| FQ2 | Is the redundancy-group quotient (C2) definable uniformly across QM, QFT, and quantum gravity, or does quantum-gravity context (no fixed spacetime) require generalizing the enumerated groups? | OPEN | P4: survey gauge-invariant-observables literature (Fröb-Lima; Rudnicki et al.); test C2 against Hartle generalized QM | YES |
| FQ3 | Does the invariant-content thesis (C1) add predictive content beyond structural realism, or is it absorbed by the SR "relations not relata" program? | OPEN | P4: symmetric audit against Ladyman-Ross; define at least one discriminating case | YES |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| P1 | C1: no dimensionful constant carries invariant content beyond its unit-bridge role | Ongoing | Dimensional analysis, unit-system transformations | A dimensionless combination cannot be formed capturing a claimed invariant; or claimed scale-invariance fails where asserted |
| P2 | C2: every measurable quantity is an invariant under the enumerated redundancy groups | Ongoing | QFT/condensed-matter experiments | A gauge-dependent observable that is nonetheless measured |
| P3 | C3: e and π are derivable from mark-and-distinction + self-reference only | Next phase | Formal derivation (P4) | Any additional primitive required; or a self-referential equation with a structurally-uncharacterized fixed point other than e/π |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- FQ1 disconfirmed if: no well-posed derivation of e/π from mark/distinction + self-reference can be exhibited (then C3 downgrades to [RETRODICTION], zero evidential weight).
- FQ2 disconfirmed if: a quantum-gravity observable is exhibited that is not an invariant of any finite redundancy-group quotient.
- FQ3 disconfirmed if: every discriminator between C1 and structural realism collapses (then C1 is absorbed by SR — still true, but not novel).

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|:---|:-----------|:--------------|:-----|:---------|
| REG-RES007-001 | C3 derivation is constructive (fixed-point equations, not pattern-matching) | No constructive derivation; only post-hoc identification of e/π in existing formulas | Formal derivation appendix in P4 draft | 2026-08-31 |
| REG-RES007-002 | C2 quotient covers QFT (BRST, path integral, bare params) | Any QFT observable not expressible as invariant of listed groups | Case catalog in P4 draft §4 | 2026-08-31 |

## 5. CALIBRATION REGISTER

| Date | Prediction | Strength | Status | Review Date |
|:-----|:-----------|:---------|:-------|:------------|
| 2026-08-14 | C1-C3 structural claims carry disconfirmation conditions | Strong (pre-registered) | LOCKED in PROJECT-PLAN §2 | [CHECK: 2026-09-14] |
| 2026-08-14 | C3 has zero external corroboration → [UNIQUE-CLAIM] burden | Strong | DOCUMENTED (phase2-literature-review §4) | [CHECK: 2026-09-14] |

## 6. NEXT ACTIONS (Prioritized)

| Priority | Action | Depends on | Target |
|:---------|:-------|:-----------|:-------|
| P0 | ~~P4 formal derivation of C3 (fixed-point equations from mark/distinction)~~ **DONE 2026-08-14 (01f4018)** — FQ1 closed; verify derivation against BP-1/BP-6/BP-10 in P5 | Draft §5 | 2026-08-31 |
| P0 | P5 BP-1..BP-10 gates (fit-verify, terminology, density, consistency, overdetermined, derived recompute, sigma, numerology classification, audit-the-auditor, independent recompute) | P4 draft | 2026-09-07 |
| P1 | ~~P5 citation re-verification of 5 FLAGGED entries~~ **DONE 2026-08-14** — Abbas 2026 + Zhang 2026 (Crossref-verified preprints), Worrall 1989 (`10.1111/j.1746-8361.1989.tb00933.x`), Joyal-Street 1993 (`10.1006/aima.1993.1055`), Spencer-Brown 1969 (manual canonical, no DOI exists) | citation-audit.md §8 | 2026-09-07 |
| P1 | ~~P5 Zenodo publication + GitHub provenance + D1/KG/Vectorize deployment~~ **DONE 2026-08-14** — v0.1 21929479 + v0.2 newversion 21929590 (post-audit remediation), GitHub provenance `isSupplementTo` verified, D1 living-paper row (body 14,631 chars, v0.2), KG node + BELONGS_TO edge, Vectorize indexed (chunks 0–20+), R2 archive 7 files (rclone check 0 diff), papers-server HTTP 200 | 7-layer closeout verify | 2026-09-14 |

## 7. SESSION LOG + MAINTENANCE PROTOCOL

- 2026-08-14: Registry created at Phase 4 draft (commits f718fae → 24ddee2). FQ1-FQ3 seeded from consilience-gate.md §4 and phase2-literature-review.md §4.
- Maintenance: bump version + log on every P4/P5/P8 change. Registry ships with the publication deposit (PUBLICATION-SOURCE-COMPLETENESS-1). Check calibration entries at [CHECK] dates.
