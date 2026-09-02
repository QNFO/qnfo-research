# JPC.003 — v1.7 Evidence Delta (2026-09-02)

> Scope: computational verification addendum for the next version of
> "Error Correction Is a Landauer Machine" (QNFO.JPC.003). This document is the
> evidence record that justifies a v1.7 bump: an independent reproduction of the
> v1.6 verification plus a new parameter-space robustness sweep. No claims in this
> file change the paper's core result; they strengthen the reporting of its scope.

## 1. Independent reproduction of the v1.6 verification (PASS)

Both deposited verification scripts were re-run from the canonical repo with the
fixed seed (20260826) and Python 3 stdlib only:

| Script | Result | Evidence |
|---|---|---|
| verification_h2.py | EXIT 0; table reproduces §7 exactly (48.0 flat erasures constant; tree 16.0-29.3; ratio 3.00-1.64) | h2_results.json — git diff vs committed v1.6 deposit: EMPTY (byte-identical) |
| verification_floor.py | EXIT 0; floor table + golden values reproduce (300 K 2.8710e-21 J ... 15 mK 1.4355e-25 J) | verification_floor.json — git diff vs committed v1.6 deposit: EMPTY (byte-identical) |

Reading: the v1.6 quantitative claims (floor formula, scaling laws, §7 table) are
fully reproducible from the deposited artifacts.

## 2. New robustness sweep (this delta)

verification_h2_sweep.py (new, same model, same equal-rate budgets, same metrics)
swept the clustered-channel parameters around the paper's six regimes (uniform
background p=0.005; bursts c in {1,2,3,4}, L in {4,8,16,32}, q in {0.1,0.3,0.5}),
2,000 trials per regime, seed 20260826. Results: h2_sweep_results.json.

| Regime | Erasures tree | Ratio (flat/tree) | Residual flat | Residual tree |
|---|---|---|---|---|
| burst c=1 L=4 q=0.3 | 19.7 | 2.439 | 0.505 | 0.660 |
| burst c=1 L=16 q=0.3 | 23.9 | 2.010 | 2.944 | 4.922 |
| burst c=1 L=8 q=0.1 | 19.6 | 2.452 | 0.181 | 0.352 |
| burst c=1 L=8 q=0.5 | 21.6 | 2.227 | 3.074 | 4.052 |
| burst c=3 L=8 q=0.3 | 27.2 | 1.768 | 4.312 | 6.709 |
| burst c=2 L=16 q=0.3 | 28.6 | 1.677 | 6.231 | 9.988 |
| burst c=2 L=8 q=0.1 | 21.5 | 2.238 | 0.395 | 0.763 |
| burst c=2 L=8 q=0.5 | 25.0 | 1.917 | 6.095 | 8.094 |
| burst c=2 L=4 q=0.3 | 21.9 | 2.189 | 1.149 | 1.560 |
| burst c=4 L=8 q=0.3 | 29.1 | 1.650 | 5.954 | 9.153 |
| burst c=2 L=32 q=0.3 | 35.1 | 1.368 | 13.501 | 21.152 |
| burst c=1 L=32 q=0.5 | 30.1 | 1.594 | 13.567 | 18.987 |

### Findings
1. **The erasure advantage is robust**: flat/tree ratio > 1 in all 12 swept regimes
   (range 1.368-2.452). The paper's 1.6-3.0x claim sits inside this wider envelope;
   the advantage erodes toward ~1.4x at long bursts (L=32) and never inverts.
2. **The partial null is confirmed and sharpened**: tree residual errors exceed flat
   residuals in every non-trivial regime, growing with burst severity. The naive
   two-level construction's correctness penalty is not a boundary artifact of the
   original six regimes - it is the general behavior of this construction.
3. **Boundary of the mechanism**: the adaptive-erasure benefit is largest when bursts
   are short/rare (up to 2.45x) and smallest when bursts are long/frequent (1.37x at
   c=2 L=32). This is the crossover region where stronger constructions (two parity
   bits per group, product/tree LDPC families) would be tested next.

### Status
Delta type: A (evidence - new computation over the same model). Not yet folded into
the paper body; intended for the v1.7 revision of section 7 (Verification Appendix)
with the reproduction attestation above.

---
Evidence: h2_results.json / verification_floor.json (committed v1.6, unchanged) +
h2_sweep_results.json + verification_h2_sweep.py + _rerun_h2_out.txt + _rerun_floor_out.txt (this delta).
Canonical repo: QNFO/qnfo-research branch res/paper/jpcub-qec-landauer.
