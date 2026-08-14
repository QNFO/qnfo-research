# RESEARCH CONTINUITY REGISTRY — QNFO.RES.009

**Project:** The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant
**DOI:** 10.5281/zenodo.21938971 (concept 10.5281/zenodo.21938970) · **Branch:** res/paper/spin-statistics-distinction
**Last updated:** 2026-08-14 · **Living document** (maintained with version bumps; not a static paper artifact)

This registry tracks frontier questions, falsifiable predictions, and pre-registration scaffolds raised by the published paper and its 2026-08-14 evening deep-inquiry follow-ups. It is the internal continuity instrument; WBS codes and branch names are permitted here (they are not shipped in the published manuscript).

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|---|---|---|---|---|
| FQ1 | **What is the cost of drawing a boundary?** (Landauer) — the mark calculus treats boundary-drawing as free, but creating a distinction may cost free energy; if so, entropy/energy precede distinction. | OPEN | Extend the T4 toy-model with a boundary-cost term; formalize the second-law-first inversion. | YES |
| FQ2 | **Can the spin-statistics *connection* (which exchange eigenvalue maps to which spin) be derived from the mark calculus, and is the minimal extra structure exactly Lorentz + microcausality?** | OPEN (paper §5 boundary) | Complete T1/T2: full digling/dereliction/promotion check for the two modal exponentials in DiLL. | YES |
| FQ3 | **Does the braid-derived framework recover time-irreversibility and measurement?** (the zero-temperature idealization gap; note _26226215159 Q3/Q11) | OPEN | Map the irreversibility wobble; candidate inversion: derive braids from the second law. | YES |

---

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|---|---|---|---|---|
| P1 | A discrete syntactic exchange model (two indistinguishable tokens + "draw boundary" operation) reproduces the braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ and the ±1 collapse (3D semantics) vs fractional phase (2D semantics) *without a hand-imposed sign*. | 2026-08-14 | `artifacts/notebooks/t4-toy-model.py` | If the sign must be hardcoded externally rather than emerging from the syntactic rules. |
| P2 | No stable, local, relativistic 3+1D excitation exists with exchange phase η ≠ e^{2πis} (e.g., a spin-½ boson or spin-0 fermion). | ongoing | any experimental QFT survey | Observation of such a particle. |
| P3 | The mark calculus reproduces the two 1D characters of S_n from distinction + compact closure + involutive braiding alone. | 2026-12-14 | T1/T2 full derivation | Impossibility proof (additional postulate required). |

---

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- **FQ1 disconfirmed if:** a boundary can be drawn with zero free-energy cost in a physical system (Landauer violated), OR the second-law-first inversion predicts nothing distinguishable.
- **FQ2 disconfirmed if:** the minimal extra structure is shown to be strictly more than Lorentz + microcausality.
- **FQ3 disconfirmed if:** a braid-derived dynamics model recovers a preferred time direction and measurement collapse with no added postulate.

---

## 4. PRE-REGISTRATION SCAFFOLDS

**REG-009-001 — Toy-model (P1).**
- **Hypothesis:** braid relations + dimensional collapse emerge from discrete syntactic exchange with no hand-imposed sign.
- **Falsification:** the sign must be hardcoded.
- **Data:** `artifacts/notebooks/t4-toy-model.py` output (run 2026-08-14).
- **Deadline:** 2026-08-14 (executed same-day; see §7).

---

## 5. CALIBRATION REGISTER

| Prediction | Strength | Status |
|---|---|---|
| [CHECK: 2026-09-14] FQ1 Landauer cost formalized | WEAK | PENDING |
| [CHECK: 2026-12-14] F2 derivation executed or impossibility shown | MEDIUM | PENDING |
| [CHECK: 2027-06-14] ≥1 external citation of the invariant formulation | WEAK | PENDING |

---

## 6. NEXT ACTIONS (Prioritized)

- **P0:** T4 toy-model (this cycle — DONE, §7).
- **P1:** T1/T2 DiLL full check (digling/dereliction/promotion for !_S/!_{Λ}; n-particle character derivation).
- **P2:** Disciplined companion essay — publish with [RETRODICTION]/[NOT YET EVIDENCE]/[EXTRAPOLATION] labels and external constraints (draft: `docs/companion-essay-draft.md`).

---

## 7. SESSION LOG

- **2026-08-14 (P9):** Registry created from the red-team audit of the evening deep-inquiry notes (findings S-1..S-10, D-1..D-2). T4 toy-model written and executed (P1 verified: braid relations + ±1 collapse + fractional-phase anyon mode all reproduced syntactically). Companion-essay draft committed with the labeling discipline restored.

## MAINTENANCE PROTOCOL
Update this file at each phase closeout; bump the date. Any published paper claiming frontier questions or pre-registered predictions must link back here.
