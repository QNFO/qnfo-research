# RESEARCH CONTINUITY REGISTRY — QNFO.RES.009

**Project:** The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant
**DOI:** 10.5281/zenodo.21938971 (concept 10.5281/zenodo.21938970) · **Branch:** res/paper/spin-statistics-distinction
**Last updated:** 2026-08-14 · **Living document** (maintained with version bumps; not a static paper artifact)

This registry tracks frontier questions, falsifiable predictions, and pre-registration scaffolds raised by the published paper and its 2026-08-14 evening deep-inquiry follow-ups. It is the internal continuity instrument; WBS codes and branch names are permitted here (they are not shipped in the published manuscript).

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|---|---|---|---|---|
| FQ1 | **What is the cost of drawing a boundary?** (Landauer) — the mark calculus treats boundary-drawing as free, but creating a distinction may cost free energy; if so, entropy/energy precede distinction. | SHARPENED (T5, 2026-08-14) | T5 boundary-cost model EXECUTED (`artifacts/notebooks/t5-boundary-cost-model.py`, REG-009-002): the cost applies to erasure/maintenance, NOT reversible drawing; distinction (grammar) and dissipation (resource) are dual descriptions, not competitors. Next: T6 capacity bound ΔS/k_B ln 2 as a physical ceiling on maintained distinctions. | YES |
| FQ2 | **Can the spin-statistics *connection* (which exchange eigenvalue maps to which spin) be derived from the mark calculus, and is the minimal extra structure exactly Lorentz + microcausality?** | SHARPENED (paper §5 boundary) | T1/T2 DiLL full check COMPLETE (2026-08-14, `artifacts/notebooks/t1-t2-dill-full-check.md`). Finding: minimal extra structure = {self-duality, abelian-pair, symmetric braiding} for statistics + {Lorentz, microcausality, positive energy} for the connection — one postulate wider than §5 states. Next: v1.1 amendment DRAFTED (`docs/v1.1-amendment-draft.md`, decision YES 2026-08-14); Zenodo newversion publish pending (CMD PUBLISH cycle). | YES |
| FQ3 | **Does the braid-derived framework recover time-irreversibility and measurement?** (the zero-temperature idealization gap; note _26226215159 Q3/Q11) | OPEN | Map the irreversibility wobble; candidate inversion: derive braids from the second law. | YES |

---

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|---|---|---|---|---|
| P1 | A discrete syntactic exchange model (two indistinguishable tokens + "draw boundary" operation) reproduces the braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ and the ±1 collapse (3D semantics) vs fractional phase (2D semantics) *without a hand-imposed sign*. | 2026-08-14 | `artifacts/notebooks/t4-toy-model.py` | If the sign must be hardcoded externally rather than emerging from the syntactic rules. |
| P2 | No stable, local, relativistic 3+1D excitation exists with exchange phase η ≠ e^{2πis} (e.g., a spin-½ boson or spin-0 fermion). | ongoing | any experimental QFT survey | Observation of such a particle. |
| P3 | The mark calculus reproduces the two 1D characters of S_n from distinction + compact closure + involutive braiding alone. | 2026-12-14 | T1/T2 full derivation | Impossibility proof (additional postulate required). **2026-08-14 check result:** holds **iff** the abelian-pair postulate is added; Yang–Baxter forces phase uniformity across pairs (no extra postulate needed for that). Restate P3 postulate set accordingly. |

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

**REG-009-002 — Boundary-cost model (T5, FQ1).**
- **Hypothesis:** H1 capacity bound floor(B/c); H2 write/erase asymmetry (reversible draw costs 0, erasure costs kT ln 2); H3 grammar invariance (budget gates capacity, never statistics).
- **Falsification:** H2 fails if a reversible write shows nonzero minimum cost; H3 fails if a budget term enters the exchange eigenvalues. H1 is definitional — demonstration only, no evidential weight [KIF-60].
- **Data:** `artifacts/notebooks/t5-boundary-cost-model.py` output (run 2026-08-14).
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

- **P0:** T4 toy-model — DONE (§7).
- **P1:** T1/T2 DiLL full check — DONE 2026-08-14 (`artifacts/notebooks/t1-t2-dill-full-check.md`).
- **P2:** Disciplined companion essay — draft committed (`docs/companion-essay-draft.md`); publication decision pending.
- **P3:** v1.1 amendment publish (CMD PUBLISH): apply `docs/v1.1-amendment-draft.md` (abelian-pair in §5/F2), Zenodo newversion per NEWVERSION-FRONTMATTER-CARRYOVER-1.
- **P4:** FQ1 follow-up T6 — capacity bound ΔS/k_B ln 2 as a physical ceiling on maintained distinctions.
- **P5:** FQ3 irreversibility mapping — seed: T5 H2 (erasure is the irreversibility gate).

---

## 7. SESSION LOG

- **2026-08-14 (P9):** Registry created from the red-team audit of the evening deep-inquiry notes (findings S-1..S-10, D-1..D-2). T4 toy-model written and executed (P1 verified: braid relations + ±1 collapse + fractional-phase anyon mode all reproduced syntactically). Companion-essay draft committed with the labeling discipline restored.

- **2026-08-14 (P1 continuation):** T1/T2 DiLL full check COMPLETE — `artifacts/notebooks/t1-t2-dill-full-check.md`. Results: (1) both !_S and !_Λ verified as DiLL exponentials (dereliction/digging/promotion/contraction/weakening/Seely); (2) parity identification Sym_gr(A_odd) ≅ Λ(A_odd) — the two exponentials are two branches of one construction; (3) ribbon identity gives θ_M = η·id for abelian self-dual M; (4) Yang–Baxter forces phase uniformity across pairs (η_1 = η_2 derivation); (5) FINDING: abelian-pair postulate required to exclude parastatistics-class sectors — §5 boundary is one postulate wider than stated; F2/P3 restated accordingly. Self-verification caught + fixed one eigenspace-label error (odd-mark parity swap) and one citation correction (Greenberg–Messiah 1965). Also re-ran t4-toy-model.py this session: all checks True (P1 re-verified). Next: decide v1.1 (amend §5 + F2), then FQ1 boundary-cost term (T5), then FQ3 irreversibility mapping.

- **2026-08-14 (P9 continuation, T5):** FQ1 boundary-cost model EXECUTED — H1/H2/H3 all PASS (REG-009-002). Key result: the Landauer inversion (Note 3 Layer 1) holds ONLY for erasure/maintenance, NOT for reversible drawing → distinction (grammar) and dissipation (resource) are DUAL descriptions; the second law prices the mark's upkeep, it does not dethrone it. v1.1 amendment DRAFTED (decision YES: abelian-pair postulate in §5/F2) — Zenodo newversion publish pending. Next: CMD PUBLISH v1.1; T6 capacity bound; FQ3 irreversibility mapping.

## MAINTENANCE PROTOCOL
Update this file at each phase closeout; bump the date. Any published paper claiming frontier questions or pre-registered predictions must link back here.
