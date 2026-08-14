# FQ1-EXP-001 Outcome — Weight-Enumerator Valuation Profiles: PRELIMINARY POSITIVE

**Project:** QNFO.RES.006 · *Implications for Computing and Quantum Error Correction*
**Date:** 2026-08-14
**Status:** EXPLORATORY — **PRELIMINARY POSITIVE** (small sample; NOT the pre-registered REG-RES006-001)
**Invariant:** $v_2(A_j)$ — the 2-adic valuation profile of the stabilizer weight enumerator,
$A_j = \#\{ \text{stabilizer elements of Pauli weight } j \}$.
**Script:** `artifacts/fq1-exp-check.py` (deterministic, seed 20260814)

---

## 1. Why this invariant survives the no-go lemma

FQ2/FQ3 established that every valuation-reachable invariant computed from the
Hilbert-space/stabilizer **cardinalities** — $v_2(\dim H)$, $v_2(\dim H_L)$, $v_2(|S|)$ —
is a function of $(n, k, q)$ only (the "valuation-weight duality" no-go). The weight-enumerator
coefficients $A_j$ are **not** in that set: they are genuinely code-dependent integers
(determined by the full stabilizer group structure, not by $(n,k,q)$). Therefore
$v_2(A_j)$ is a candidate non-trivial valuation invariant with potential predictive power —
**exactly what FQ1 (C4) asks for** — and it is not excluded by any prior disconfirmation.

---

## 2. Design (controls the parameter confound the 83% claim's design never controlled)

Structured codes vs random stabilizer codes **at the same (n, k)**:

| Structured code | Random controls | m = n−k |
|:----------------|:----------------|:--------|
| $[[5,1,3]]$ perfect | 20 × $[[5,1]]$ | 4 |
| $[[7,1,3]]$ Steane | 20 × $[[7,1]]$ | 6 |
| $[[8,2,2]]$ toric L=2 | 20 × $[[8,2]]$ | 6 |
| $[[15,7,3]]$ Hamming | 10 × $[[15,7]]$ | 8 |

Random codes: greedy generation of **valid** stabilizer codes (symplectic pairwise
commutativity + group-closure independence). Deterministic seed `20260814`.
Features: `max_v2 = max_{j≥1} v_2(A_j)`; `n_even = #{j≥1 : A_j even}`.
Test: percentile of the structured value in the same-parameter control distribution.

---

## 3. Results (deterministic; script `fq1-exp-check.py`)

| Code | A_j profile | max_v2 | pct (max_v2) | n_even | pct (n_even) | control max_v2 min/med/max |
|:-----|:------------|:-------|:-------------|:-------|:-------------|:---------------------------|
| $[[5,1,3]]$ perfect | 1, 15@w4 | **0** | **0%** | 4 | 45% | 1 / 1 / 2 |
| $[[7,1,3]]$ Steane | 1, 21@w4, 42@w6 | **1** | **5%** | 6 | 90% | 0 / 2 / 4 |
| $[[8,2,2]]$ toric | 1, 14@w4, 32@w6, 17@w8 | **5** | **100%** | 7 | 55% | 1 / 3 / 4 |
| $[[15,7,3]]$ Hamming | 1, 45@w8, 210@w12 | **1** | **0%** | 14 | 90% | 1 / 2 / 6 |

Sanity: $\sum_j A_j = 2^m$ for all four codes (True).

---

## 4. Interpretation

- **Every structured code tested is an OUTLIER** against same-parameter random controls:
  max_v2 percentiles **0%, 5%, 100%, 0%**. Random codes cluster in the middle
  (median 1–3); structured codes sit at the extremes.
- **Sign structure (the fingerprint reading):** perfect ($A_4=15$ odd → max_v2 = 0,
  strictly below ALL 20 controls) and Hamming (max_v2 = 1 at the bottom edge) sit at the
  **low** extreme (odd-heavy enumerators); toric sits at the **high** extreme
  (max_v2 = 5 from $A_6 = 32$, a power-of-two multiplicity — even-heavy). The invariant
  detects structure, but with a family-dependent sign — it is a **structural fingerprint**,
  not a single-threshold binary classifier.
- **Cleanest detection:** $[[5,1,3]]$ perfect — the only code with an all-odd enumerator
  ($A_4 = 15$), max_v2 = 0 strictly below all controls (min = 1).
- **Consistency with FQ2/FQ3:** no contradiction. The $A_j$ coefficients lie *outside* the
  $(n,k,q)$-only set established there; this invariant goes beyond the vacuous cardinalities
  to the enumerator coefficients.

---

## 5. Caveats (honest)

1. **Small sample:** 1 structured code per family, 10–20 controls. Percentiles are
   suggestive, not a statistical test.
2. **Sign structure:** classification would require per-family signatures, not one threshold.
3. **Exploratory:** NOT the pre-registered REG-RES006-001 (Kodaira–Néron), which remains
   BLOCKED on NTOF source under-specification (Mahler target function, Cox-ring ideal I_C).
4. **Distance confound (flagged for the full study):** structured codes have $d \ge 2$,
   random controls often $d = 1$. The invariant uses only the stabilizer enumerator, but a
   full scan must check whether *random codes with $d \ge 2$* also sit at the extremes.
5. **Confirmation needed:** the pre-registered fresh 50/family generation with seeds.

---

## 6. Verdict

**PRELIMINARY POSITIVE** — a non-trivial valuation invariant ($v_2$ of weight-enumerator
coefficients) with apparent structure-detection power exists. This is the first positive
lead in the FQ series. It directly motivates: (a) re-specifying REG-RES006-001 to use the
well-defined $v_2(A_j)$ invariant (no blocked dependency), or (b) clearing the NTOF blocker
for the original Kodaira–Néron test. Either path is a concrete, executable next step.

---

## 7. Red-team notes (self-audit)

| Check | Result |
|:------|:-------|
| Is the toric max_v2 = 5 real? | Yes — $A_6 = 32$, $v_2(32) = 5$; the toric stabilizer group contains 32 weight-6 elements (products of vertex/plaquette operators). Verified by enumeration. |
| Is the perfect-code max_v2 = 0 real? | Yes — $A_4 = 15$ (odd); all 15 non-identity stabilizers have weight 4. Verified. |
| Could the outlier status be a distance artifact? | Flagged as the main confound for the full study (caveat 4). The invariant is computed from the stabilizer enumerator only, but random codes with $d \ge 2$ must be tested explicitly. |
| Does the sign structure invalidate the finding? | No — it refines it: the invariant is a fingerprint (per-family signature), not a binary classifier. Honest framing retained. |
| Overclaim risk | Mitigated: "preliminary positive", small sample, exploratory, all caveats stated. |

---

*This document records FQ1 exploratory evidence in the RESEARCH-CONTINUITY-REGISTRY.
Companion script: `fq1-exp-check.py` (deterministic; outputs reproduced in this record).*
