# Verification Suite — QNFO.RES.028 (Phase 4)

Reproducibility statement (COMPUTATIONAL-VERIFICATION-1).

## Runtime

- Python 3.12.10, mpmath 1.3.0, standard library only.
- All three scripts are deterministic: no RNG, no network access, no external data files.
- Precision: `verify_m_anyon.py` and `verify_braid_characters.py` at 30 decimal digits (mpmath dps=30); `verify_prime_gap_thermo.py` at 15 digits (sufficient: no claim depends on digits beyond 1e-12).

## Re-run

```
cd artifacts/verification
python verify_m_anyon.py            # C1 — bounded-occupation family adjudication
python verify_braid_characters.py   # C2 — root-of-unity character model
python verify_prime_gap_thermo.py   # H2 — prime-gap specific-heat deviation
```

Each script writes its machine-readable results to a same-named `.json` and prints a
per-check PASS/FAIL line plus the hypothesis verdict. Expected runtime on a laptop:
~1 min, <1 s, ~5–10 min respectively (the H2 smooth-baseline requires 78,498
Newton inversions of the logarithmic integral at 1M prime cutoff).

## Layout note

Scripts resolve no relative file paths; they can be copied anywhere (DEPOSIT-LAYOUT-VERIFY-1).
Run from this directory so the logs and JSONs land beside the sources.

## Check inventory

| Script | Checks | What it verifies |
|:-------|:-------|:-----------------|
| verify_m_anyon.py | G1–G4 | ζ(s)/ζ((m+1)s) identity; golden occupations; phase-blindness of the m-family (±1 permutation eigenvalues, θ-invariance of observables, no Laughlin match); Gentile ≠ Haldane at finite m |
| verify_braid_characters.py | C1–C5 | braid 1-d characters; Laughlin phases = primitive 2m-th roots of unity; Fibonacci eigenvalues q⁴/−q² at q=e^{iπ/5}; TL family δ_k = 2cos(π/(k+2)); corpus-anchor consistency |
| verify_prime_gap_thermo.py | H1–H4 | Bost–Connes divergence boundary (β=1); prime-spectrum C_V goldens; smooth-DOS baseline via li₂⁻¹(k); non-zero ΔC_V in both statistics |

## Hypothesis cards vs executed tests (HYPOTHESIS-CARD-EXECUTION-PARITY-1)

Reconciled in `../results-p4-reconciliation.md` after the runs: C1 executed strictly
stronger than its card's letter (phase-indeterminacy, not merely "no match"); C2 and
H2 executed as carded. No family-definition drift.
