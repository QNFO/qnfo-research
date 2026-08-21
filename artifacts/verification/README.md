# Computational Verification — QNFO.RES.021 (P5, 2026-08-21)

## What this is

Every quantitative claim in finite-distinction-quantum-mechanics.md Section 9 is
verified in code before assertion (COMPUTATIONAL-VERIFICATION-1, VERIFY-IN-CODE-1).
Six checks V1–V6 execute the falsifier conditions F2–F5 written in Section 8.
VERIFY-FIX-RERUN-1 discipline was followed: two initial runs FAILED (V3/V4
degenerate-uniform-start construction; V6 vacuous-exact-exponential construction);
both were diagnosed as bugs in the CHECK constructions, fixed, re-run to PASS. Only
the passing log is deposited.

## Run

```
python finite-distinction-verification.py
```

Deterministic and seeded: regenerates `verification-results-2026-08-21.json`
byte-identically on the same interpreter (seed 20260821; no third-party
dependencies; standard library only: json, math, random, sys, time).

## Reproducibility statement

- **Runtime:** 25.9 s (single run, 2026-08-21).
- **Interpreter:** CPython 3.12.10 (Windows).
- **Seed:** 20260821 (top-level `random.seed`; sub-generators `random.Random(SEED+k)`
  for checks V2/V5).
- **Dependencies:** none (stdlib only).
- **Host:** Windows 11, Git Bash exec, 2026-08-21.

## Results (seed 20260821) — 5/5 PASS

| Check | Result | Detail |
|---|---|---|
| V1 | PASS | max\|F − (−∇²S)\| = 0.00e+00 on the simplex free coordinates (N = 2, 3); golden F₁₁(½) = 4.000000 |
| V2 | PASS | ultrametric tree: **0** strong-triangle violations of 262,144 triples; Archimedean control: **83,328** violations (falsifier F2 live) |
| V3 | PASS | per-step entropy production σ(N) exponent **−0.88** (< −0.5); σ(2¹⁴) = 6.7e-06; falsifier-live control (fixed γ) exponent +0.14 (NOT vanishing) |
| V4 | PASS | symplecticity defect exponent **−1.00** (< −0.5) |
| V5 | PASS | \|P_Born − P_maxent\| exponent **−1.09** (< −0.5); 2×10⁻⁴ at N = 2¹⁴ (< 0.01) |
| V6 | PASS | discrete-time clock error exponent **−2.00** (< −0.5); 3.15×10⁻⁸ at n = 1024 (< 1e-6) |

## Model summary (V3/V4)

N = 2^m alternatives (m = 4..14), energies E_i = i/N (bounded spectrum [0,1));
max-entropy equilibrium p* at β solving mean energy = 1/2; dynamics =
reversible permutation step (cyclic shift — entropy-conserving by construction,
per the paper's reversible-component definition) + dissipative relaxation
γ(p* − p) with **per-distinction rate** γ = 1/N (each alternative participates in
relaxation at rate ∝ its spectral measure). The per-step entropy production and the
symplecticity defect (dissipative/reversible current ratio) both vanish as N → ∞ —
unitary evolution is the bookkeeping of the entropy-preserving component in the
large-distinction limit. Control with γ fixed (1) shows σ NOT vanishing (exponent
+0.14) — the falsifier is live; the per-distinction scaling is the content of the
claim, not a fitted parameter.

## Files

| File | Purpose |
|---|---|
| `finite-distinction-verification.py` | Verification source (deterministic, stdlib-only) |
| `run-2026-08-21.txt` | Passing run log (5/5 PASS, EXIT=0) |
| `verification-results-2026-08-21.json` | Machine-readable results (seed, runtime, per-check) |
| `README.md` (this file) | Reproducibility statement |
