# Computational Verification — QNFO.RES.021 (P5, 2026-08-21; v1.0.1 P7-remediation)

## What this is

Every quantitative claim in finite-distinction-quantum-mechanics.md Section 9 is
verified in code before assertion (COMPUTATIONAL-VERIFICATION-1, VERIFY-IN-CODE-1).
Seven checks V1–V7 execute the falsifier conditions F2–F5 written in Section 8.
VERIFY-FIX-RERUN-1 discipline was followed across the v1.0.0 and v1.0.1 cycles:
initial failing runs were diagnosed as bugs in the CHECK constructions (V3/V4
degenerate-uniform start; V6 vacuous-exact-exponential step; v1.0.1 V5a Nyquist-mode
instability of the forward relaxation; V7a parity cancellation of the symmetric
spike; V5a exponent gate incompatible with the N-independent e⁻¹⁵ residual), fixed,
re-run to PASS. Only passing logs are deposited. Claims were never tuned to a
failing log.

## Run

```
python finite-distinction-verification.py
```

Deterministic and seeded: regenerates `verification-results-2026-08-21.json` with
identical check results on the same interpreter (seed 20260821; no third-party
dependencies; standard library only: json, math, random, sys, time). The embedded
wall-clock field `runtime_s` is the only run-varying value.

## Reproducibility statement

- **Runtime:** 14.0 s (v1.0.1 run, 2026-08-21).
- **Interpreter:** CPython 3.12.10 (Windows).
- **Seed:** 20260821 (top-level `random.seed`; sub-generators `random.Random(SEED+k)`).
- **Dependencies:** none (stdlib only).

## Results (seed 20260821, v1.0.1) — 6/6 PASS

| Check | Result | Detail |
|---|---|---|
| V1 | PASS | max\|F_def − (−∇²S)\| = 0.00e+00 (uniform + non-uniform p = (0.2, 0.3); Fisher by score-function definition); golden F₁₁(½) = 4.000000 |
| V2 | PASS | ultrametric tree: **0** strong-triangle violations of 262,144 triples; Archimedean control: **83,328** (falsifier F2 live) |
| V3/V4 | PASS | per-step entropy production σ(N) exponent **−0.88** (< −0.5); σ(2¹⁴) = 6.7e-06; symplecticity-defect exponent **−1.00**; falsifier-live control (fixed γ) exponent **+0.14** — NOT vanishing |
| V5 | PASS | V5a: flow equilibrium converges to the max-entropy state at every N — max l1(p_T, p*) = **3.05e-07** (< 1e-6; a wrong equilibrium gives O(1)); V5b: ±2σ band tracking at p* — mean z 0.75, \|z\| ≤ 2 coverage 0.98, max z 2.76 (reported); **falsifier-live control z = 72.6** — outside the band |
| V6 | PASS | finite-resolution clock error exponent **−2.00** (< −0.5); 3.15e-08 at n = 1024 (< 1e-6) |
| V7 | PASS | V7a: max \|ψᵀLψ\| = **2.17e-17** (< 1e-14) — the 2-norm is exactly conserved by the reversible generator; min \|3Σψ\|ψ\|(Lψ)\| = **3.82e-02** (> 1e-6) — the L3 norm drifts, so only p = 2 is selected (asymmetric seed; the symmetric spike cancels by parity — documented trap); V7b: spectrum exactly λ_k = −i·sin(2πk/N) (max\|Re λ\| = 0, max\|Im λ + sin\| = 0) — purely imaginary |

## Model summary (V3/V4, V5)

N = 2^m alternatives, energies E_i = i/N (bounded spectrum [0,1)); max-entropy
equilibrium p* at β solving mean energy = 1/2; reversible step = exact cyclic
permutation (entropy-conserving by construction); dissipative relaxation with
**per-distinction rate** γ = 1/N (V5a uses the implicit-normalized form
p ← (S·p + dt·γ·p*)/(1 + dt·γ) — same fixed point, globally stable, mass-preserving;
the forward form is Nyquist-unstable). The per-distinction rate structure is a MODEL
assumption, not a derived claim (draft §9). The falsifier-live controls (fixed-γ for
V3; concentrated-state band excursion for V5) show the tests are not vacuous.

## v1.0.1 notes (P7-remediation)

- V7 added (H-1): 2-norm invariance + purely imaginary spectrum of the reversible
  generator — the two computational legs of the draft §5 candidate-route statement.
- V5 rewritten (H-2): V5a equilibrium identity + V5b ±2σ band tracking (the criterion
  the pre-remediation code never computed) + falsifier-live control.
- S-1: V1 non-uniform point. S-2: §9 V6 row wording ("finite-resolution clock
  simulation").

## Files

| File | Purpose |
|---|---|
| `finite-distinction-verification.py` | Verification source (deterministic, stdlib-only) |
| `run-2026-08-21.txt` | Passing run log (6/6 PASS, EXIT=0) |
| `verification-results-2026-08-21.json` | Machine-readable results |
| `README.md` (this file) | Reproducibility statement |
