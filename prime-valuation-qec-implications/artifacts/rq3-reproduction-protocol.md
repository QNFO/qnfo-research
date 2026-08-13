# RQ3 Reproduction Protocol — the "83%" Kodaira–Néron Classifier Claim

**Project:** QNFO.RES.006 | **Claim:** NTOF (DOI 10.5281/zenodo.21193487) reports 83%
classification of QEC code families (166/200; per-family 92/78/90/72%) by a rule-based
Kodaira–Néron-fiber classifier (Algorithm 4.4).
**Date:** 2026-08-13 | **Status:** PROTOCOL (not yet executed — see Milestone 0).

## Milestone 0 — Source Feasibility (DONE this session)

The NTOF record ships only: `NUMBER-THEORY-ULTRAMETRIC-FOUNDATIONS-v1.1.pdf`,
`NUMBER-THEORY-ULTRAMETRIC-FOUNDATIONS-v1.0.pdf`, `publication.md` (43,449 chars).
**No dataset, no implementation, no baseline, no leakage-control protocol.** The classifier
is a deterministic rule-based procedure (Algorithm 4.4 in §4.3) — re-implementation from
spec is required; there is nothing to "re-run" as-is.

## Protocol

### M1 — Re-implement Algorithm 4.4 from specification
1. Input: stabilizer generators {g_1,...,g_m} of code C.
2. Step 1: binary symplectic form matrix H from generators.
3. Step 2: Cox ring R_C = C[x_1,...,x_n]/I_C.
4. Step 3: compute Weierstrass coefficients from code invariants (weight enumerator, distance, automorphism group).
5. Step 4: classify degenerate loci → Kodaira–Néron fiber type (I_n, II, III, IV, I_n*, II*, III*, IV*).
Implementation in Python (sympy for the Cox-ring/Weierstrass arithmetic; small n first).
Acceptance: reproduce the NTOF per-family table on **re-implemented** cases with stated parameters.

### M2 — Fresh code-family generation (independent of NTOF)
Generate 50 codes per family with explicit protocols:
- Surface: L×L toric/planar surface codes, L=3..6 (n = L^2 or 2L^2);
- CSS: CSS from classical [n,k,d] codes (Hamming, Golay, BCH where feasible);
- Optimal: known-optimal stabilizer codes (e.g., shortened Reed–Muller, [[2^m-1, 2^m-1-2m, 3]] quantum Hamming, best-known table entries);
- Random: random stabilizer ensembles at matched (n,k).
Generate **fresh** instances (random seed, no instance shared with NTOF — NTOF does not publish instances, so this is inherently fresh; state this in the report).

### M3 — Run + record
Per-family classification rate + Mahler v_p-spectral invariant (v_p^max) computed independently.
Report per-family table matching the NTOF format for direct comparison.

### M4 — Baselines + acceptance (pre-registered)
- Majority-class baseline: max over families of (correct-by-trivial-assignment).
- Random-assignment baseline: 25% for 4 families.
- Acceptance: "83% reproduced within stated confidence" if aggregate ≥ 0.80 with per-family ≥ 0.70
  AND v_p^max(optimal) > v_p^max(random) by ≥ 10; otherwise FAIL reported honestly.
- Leakage statement: no instance sharing possible (no published instances); state generation seeds.

### Deliverables
`notebooks/rq3-classifier-reimpl.ipynb` (or `.py` + results JSON), `artifacts/rq3-reproduction-report.md`,
`artifacts/rq3-results.json`. Any failure is reported honestly (per manuscript §6 falsifiability).

## Risks
- Cox-ring/Weierstrass arithmetic is heavy for n ≳ 20 → start n ≤ 16, 50 codes, scale only if stable.
- The NTOF §13.2 documents a surface-code I_n* boundary mismatch — reproduction may reproduce the
  defect (that is itself a finding: is the 83% aggregate hiding a systematic family-level failure?).

## Status Update (2026-08-13)

M1b (Mahler spectral leg) **EXECUTED** — see `rq3-reproduction-report.md`.
Result: C7.3' NOT reproduced at n ≤ 18 (optimal v_p^max = 4, random median 3, max 6; claimed 28 vs 4).
M1a (Kodaira-Néron Cox-ring leg) **BLOCKED** by source under-specification (ideal I_C undefined).
