# T6 Notebook — Thermodynamic Capacity Ceiling (FQ1 formal follow-up)

**WBS:** QNFO.RES.009.P9.T4 · **Date:** 2026-08-14 · **Status:** EXECUTED (G1/G2/G3 PASS)
**Pre-registration:** REG-009-003 (see RESEARCH-CONTINUITY-REGISTRY.md §4)

## Hypothesis (pre-registered)

The FQ1 sharpening from T5 ("the second law prices the mark's upkeep, it does not
dethrone it") is made quantitative:

- **G1 (entropy ceiling):** with free-entropy budget ΔS, the maximum number of
  simultaneously maintained distinctions is floor(ΔS / (k_B ln 2)) — the physical
  re-scaling of T5-H1: each maintained distinction costs k_B ln 2 of free entropy.
- **G2 (dynamical steady state):** with per-step noise p and maintenance power budget P
  (kT ln 2 units per step), the sustainable distinct count converges to min(N, P/p) —
  the boundary as a *driven steady state*; environment entropy gain equals total fixes
  (second-law bookkeeping).
- **G3 (ceiling invariance):** at the capacity ceiling the exchange algebra is
  unchanged (eigenvalues ±1 from σ² = I); the ceiling gates how many tokens are
  simultaneously tracked, never which statistics exist.

## Implementation

`t6-capacity-bound.py` (pure Python, no external dependencies):

1. **Part A (G1).** Each maintained distinction costs k_B ln 2 of free entropy; budget
   ΔS. Verifies the ceiling floor(ΔS / k_B ln 2). [DEMONSTRATION — bookkeeping
   consequence, no evidential weight.]
2. **Part B (G2).** N = 50 cells, each decaying to unknown with p = 0.05 per step;
   maintenance re-fixes up to P = 2.0 cells per step at 1 kT ln 2 each. Predicts and
   verifies D* = min(N, P/p) = 40 and the entropy balance (fixes == reservoir gain).
   [TOY MODEL — SYNTACTIC; the steady-state bound is the substantive content.]
3. **Part C (G3).** At the ceiling (ΔS = 5 → 7 distinctions), the S₃ exchange algebra:
   Yang–Baxter and σ² = I hold identically; eigenvalues follow from σ² = I alone.
   [TOY MODEL — SYNTACTIC.]

**Modeling note (integrity record):** the first implementation of Part B had a
state-reset bug (cells rebuilt from scratch each step instead of decaying
stochastically) — the pre-registered test caught it (G2a FAIL, D_avg = 50.00 ≠ 40).
The simulation was corrected to per-cell noise decay + maintenance refix; the test then
passed. The failure mode is recorded here as designed behavior of the pre-registration
discipline.

## Results (run 2026-08-14)

| Hypothesis | Result | Evidence |
|---|---|---|
| G1 | **PASS** | ceiling=7 == floor(5.0/0.6931) |
| G2a | **PASS** | D_avg=40.61 ≈ D*=40 (min(N, P/p)) |
| G2b | **PASS** | fixes=3995 == env gain=3995.0 (≈P per step) |
| G3 | **PASS** | Yang–Baxter + σ²=I hold at the ceiling; eigenvalues from σ²=I |

## Verdict on FQ1 (formal statement, ceiling form)

A finite system with free-entropy budget ΔS can sustain at most floor(ΔS / k_B ln 2)
simultaneously maintained distinctions; under noise p and power P the steady state is
min(N, P/p); every fix is paid to the reservoir (second law). The mark calculus'
grammar is untouched at the ceiling — the capacity bound is a resource constraint on
ACCESS, not a modification of the algebra.

**FQ1 status: CLOSED in ceiling form** (the sharpened formulation of 2026-08-14, T5 →
T6). The inversion question "is energy more primitive than distinction?" receives the
dual-description answer: the grammar is primitive; the *capacity to maintain it* is
thermodynamically priced. No further inversion is supported by the toy models.

## Disconfirmation conditions (this artifact)

- If a maintained distinction cost ≠ k_B ln 2 per bit in the reversible limit, G1's
  unit conversion fails. [Established: Landauer's erasure bound; the ceiling uses the
  same unit as T5 H2.]
- If the steady state differed from min(N, P/p) by more than tolerance, G2a fails.
  [Verified: 40.61 ± 1 tolerance.]
- If a budget term entered the exchange eigenvalues, G3 fails. [Verified: eigenvalues
  derive from σ² = I only.]

## Next

- **P6 (candidate T7):** second-law-gated braid implementation — implement a braid as a
  sequence of maintained distinctions under a power budget; derive the implementable
  braid set as a function of (p, P, T). This is the FQ3 full-derivation candidate
  (see `docs/fq3-irreversibility-mapping.md`).
