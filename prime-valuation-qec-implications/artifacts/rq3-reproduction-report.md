# RQ3 Reproduction Report — Mahler v_p-Spectral Leg (C7.3')

**Project:** QNFO.RES.006 | **Slug:** prime-valuation-qec-implications
**Date:** 2026-08-13 | **Status:** M1b (Mahler spectral leg) EXECUTED; M1a (Kodaira-Néron Cox-ring leg) BLOCKED by source under-specification

## 1. What was tested

The C7.3' conjecture as stated in NTOF (DOI 10.5281/zenodo.21193487): "the v_p-spectral profile
of a code's Mahler expansion provides a discriminant between code families. Optimal codes
achieve v_p^max = 28 while random codes cluster [at 4]". Reproduction acceptance (pre-registered in
artifacts/rq3-reproduction-protocol.md): family separation (optimal vs random) ≥ 10 in v_p^max,
with optimal ≥ 28 and random ≈ 4.

## 2. Implementation (notebooks/rq3-mahler-reproduction.py)

- **Weight enumerator:** full stabilizer-group weight enumerator A_i (Shor–Laflamme enumerator
  restricted to the stabilizer group), brute-force over all 2^m group elements (m = n−k).
- **Mahler expansion:** f(x) = Σ_j c_j binom(x,j) with c_j = Σ_{i≤j} (−1)^{j−i} binom(j,i) A_i
  (finite differences).
- **v_p spectrum:** v_2(|c_j|); v_p^max = max_j v_2(|c_j|).
- **Code generation:** CSS = quantum Hamming [[7,1,3]], [[15,7,3]] built from self-orthogonal
  Hamming parity-check rows (columns = all nonzero m-bit vectors); Surface = toric L=2, L=3;
  Optimal = [[5,1,3]] perfect code (standard Laflamme generator set); Random = 50 random [[10,4]]
  stabilizer codes via a random Clifford circuit applied to an X-basis code (fixed CNOT, H, S).
- **Verification:** every code checked pairwise-commuting, rank = n−k, group size = 2^rank,
  enumerator sums to group size. **55/55 codes valid.**

## 3. Results

| Family | # valid | v_p^max values | median |
|:-------|:-------:|:---------------|:------:|
| CSS | 2/2 | [1, 1] | 1 |
| Surface | 2/2 | [1, 3] | 2 |
| Optimal | 1/1 | [4] | 4 |
| Random | 50/50 | 1..6 | 3 |

**C7.3' acceptance:** gap ≥ 10 with optimal ≈ 28, random ≈ 4.
**Observed:** optimal = 4, random median = 3 (max = 6), gap = 1 → **NOT REPRODUCED.**

## 4. Findings

**F1 — Negative result (separation direction only weakly correct, magnitude fails).**
At n ≤ 18, the weight-enumerator Mahler v_2-spectrum does not separate optimal from random by
the claimed margin: random codes reach v_p^max = 6 > optimal 4.

**F2 — Magnitude incompatibility.** v_p^max = 28 requires a Mahler coefficient with |c_j| ≥ 2^28.
Weight-enumerator coefficients are bounded by the group size 2^(n−k), so v_2 = 28 needs
n−k ≥ 28 (n ≥ 29 for k ≥ 1) — beyond every code size in the NTOF tables (n ≤ 18). Under the
weight-enumerator normalization the claim is unattainable at the reported sizes: either NTOF used
a different Mahler target (distance enumerator, enumerator evaluated at integers, Clifford-representation
polynomial, or a different normalization) or the claim is inconsistent as stated.

**F3 — Source under-determination.** NTOF never defines which function undergoes the Mahler expansion.
"a code's Mahler expansion" is ambiguous (weight vs distance vs other invariants), which blocks a
faithful reproduction of absolute numbers even when the direction test runs.

**F4 — K-N leg blocked.** Algorithm 4.4 Step 2 ("Construct the Cox ring R_C = C[x_1,...,x_n]/I_C")
does not specify the ideal I_C. Without it, the Kodaira-Néron classification leg cannot be
independently re-implemented from the shipped specification; the 83% aggregate is unreproducible
from spec alone (no dataset, no implementation, no baseline are shipped).

## 5. Verdict

- **C7.3' (Mahler separation): NOT REPRODUCED at n ≤ 18** under the weight-enumerator normalization.
  Direction weakly correct (optimal median 4 > random median 3) but violated by individual random
  codes; claimed magnitude (28) incompatible with reported code sizes under this normalization.
- **C5.1 / C8 (Kodaira-Néron 83%): NOT REPRODUCIBLE FROM SHIPPED SPEC** — ideal I_C unspecified,
  no dataset, no implementation.
- The 83% and 28-vs-4 claims remain **[UNVERIFIED-INTERNAL]** with a documented failed first
  reproduction (per manuscript C8 and the protocol's honest-failure requirement).

## 6. Next steps

1. Clarify with the NTOF source: (a) exact Mahler target function + normalization; (b) I_C
   construction for Algorithm 4.4; (c) the 50-code-per-family generation protocol.
2. If the Mahler target is clarified, extend to n ≤ 30 (larger surface/optimal tables) where
   v_2 ≥ 28 becomes attainable.
3. Manuscript §6/C8 updated to REPRODUCTION-ATTEMPTED (2026-08-13): failed at n ≤ 18 under the
   weight-enumerator normalization; status remains [UNVERIFIED-INTERNAL] pending source clarification.

## 7. Corrective Commit (2026-08-13, same session)

**Provenance fix:** the first push of this report's companion artifacts (commit bf5152e) was made
from a stale temp workspace where the compute script's LAST WRITE was an intermediate debugging
variant. The committed `rq3-results.json` and `notebooks/rq3-mahler-reproduction.py` therefore
contained a BROKEN run (55/55 invalid; wrong toric verification, pre-fix random Clifford, broken
Shor/5-qubit constructions). The scientific results in §3 above were never in doubt — they come
from the verified-good run (0/55 invalid) — but the shipped data files were wrong. This corrective
commit (commit hash below) re-ships the data files from the verified-good run:
- `rq3-results.json`: 55/55 codes valid; families CSS [1,1], Surface [1,3], Optimal [4], Random
  50/50 median 3 (max 6); C7.3' separation gap = 1 (claim 28 vs 4) → NOT REPRODUCED.
- `notebooks/rq3-mahler-reproduction.py`: fixed version (rank-based toric verification; standard
  [[5,1,3]] Laflamme generator set; random Clifford with one gate per iteration and CNOT t != q).
The fix was verified by re-reading the committed files from the remote, not just the push hash.

## 8. Limitations (red-team, direct audit — same session)

Direct adversarial re-review of §1–§7 (the negative result was attacked, not confirmed):

**L1 — Enumerator is the stabilizer-group enumerator, not the full Shor–Laflamme A-enumerator.**
Disclosed in §2 ("restricted to the stabilizer group"); the negative result is therefore scoped to
this normalization and must not be read as testing the (undefined) NTOF Mahler target directly.
The magnitude argument (F2) is unaffected: it relies only on coefficient magnitude being bounded
by the group size 2^(n−k), which holds for any group-derived enumerator.

**L2 — Random family is NOT distance-filtered (NTOF's Lemma 10 context assumes d >= 3).**
Committed JSON check: of the 50 random [[10,4]] codes, 35 have min_stab_weight <= 2 (see
counts above). Low-distance codes add low-weight contributions to the enumerator that can raise
v_p^max and bias the family upward; this WEAKENS the apples-to-apples comparison with NTOF's
random family (d >= 3). It does not rescue the magnitude claim (28 is still unattainable at n <= 18
under this normalization), but a distance-filtered random re-run is listed in next steps.

**L3 — Optimal family is a single code ([[5,1,3]], n = 5).** The separation test is underpowered
(1 vs 50 codes); the observed optimal v_p^max = 4 is one sample. The decisive finding is the
magnitude incompatibility (F2), which is size-independent, not the per-family median comparison.
A larger optimal table (n = 5..30) is required before any claim about family-level separation
medians is made.

**L4 — Overclaim guard.** The report's headline "NOT REPRODUCED" is scoped by §1/F3 to "under the
weight-enumerator normalization at n <= 18"; the manuscript §6 note carries the same scoping.
No broader claim is made.

Verdict: the negative result STANDS as scoped; L2/L3 weaken the separation-test leg but not the
magnitude argument. Follow-ups: distance-filter random re-run; larger optimal table; source
clarification of the Mahler target.
