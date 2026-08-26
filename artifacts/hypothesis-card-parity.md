# Hypothesis-Card Parity Note — QNFO.JPC.003

**Gate:** HYPOTHESIS-CARD-EXECUTION-PARITY-1 (reconcile each card's claim/prediction wording with the executed test; document drift in the premises section)
**Date:** 2026-08-26
**Result:** H1 CONFIRMED · H2 REVISED (mechanism demonstrated, correctness claim open) · H3 NOT EXECUTED (qualitative witness only)

| Card | Claim (PROJECT-PLAN §1.4) | Executed test | Verdict | Drift / note |
|---|---|---|---|---|
| **H1** | Measured E_cor per corrected logical error ≥ the erasure-count floor; floor strictly positive per family | §3, verification_floor.py: (n−k)/k · kT·ln2 table at 5 temperatures, 7 families; 6/6 structural checks (linear repetition, quadratic surface, constant-rate constant, all positive, Hamming<repetition, >10⁶ practical gap) | **CONFIRMED (numeric)** | No drift. Golden values match independent kT·ln2 at 300 K / 4 K. |
| **H2** | Nested-ball/tree codes ≥ LDPC/flat baselines (equal rate) on energy-per-corrected-bit incl. P/E endurance | §7, verification_h2.py: 2-level tree vs flat Hamming[7,4], equal rate 4/7, clustered NAND-like channel, seed 20260826, 4,000 trials/regime, 6/6 checks | **REVISED (partial null)** | Original wording claimed match-or-beat on energy-per-corrected-bit. Executed toy: tree cuts erasure count 1.64–3.0× (16→29 vs flat 48, adaptive) but residual data-bit errors are HIGHER in every non-trivial regime (single-parity L1 misses even counts; 1 reconstruction per super-group). Card rewritten to: mechanism (adaptive erasure pricing) demonstrated; correctness claim OPEN pending stronger constructions (2-bit per-group detection, product/tree LDPC) + the industrial protocol in §7. |
| **H3** | E_cor/E_useful lower in structurally protected systems vs active correction at comparable robustness | Qualitative only: §5 biology witness (photosynthesis [5], magnetoreception [7]) + capital/operating crosswalk | **NOT EXECUTED** | Original card implied a measured ratio; executed scope is a comparative-qualitative witness with the instrumentation gap stated. Marked OPEN. |

## Keystone resolution (from audit Q15)
The Universal Ignorance Audit's recursive question asked which card is load-bearing. Resolution: **H1 is load-bearing for the core claim; H2 is not.** A full H2 null at industrial scale leaves Equation (1) and the floor thesis untouched — the floor's existence does not depend on any tree-code construction winning anything. H2 is the paper's *near-term empirical payload* (the anti-poster guarantee), not its foundation. This independence is stated explicitly in §7 of the paper.

## Premises section cross-check
Drift documented in §8 ("What This Paper Does Not Claim") and in the abstract's premise-depth paragraph. No hidden upgrades of H3's status are made anywhere in the draft.
