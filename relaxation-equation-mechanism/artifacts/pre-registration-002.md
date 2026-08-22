# PRE-REGISTRATION — REG-RES018-002 (SEALED 2026-08-21)

**Project:** QNFO.RES.018 — Measurement-Triggered Relaxation Dynamics (minimal stochastic extension)
**WBS:** QNFO.RES.018 · **Branch:** res/paper/relaxation-equation-mechanism · **Seal commit:** assigned at seal (see git log)

> **KIF-60 HARD GATE:** this record seals the parameterization and the simulation code BEFORE any run. Any code or parameter change after the seal commit invalidates this registration. The simulation must be run only from the sealed harness below.

---

## 1. Hypothesis (locked — CC-2)

A **minimal stochastic extension** of the sealed REG-RES018-001 family — additive, unbiased white noise on the z-coordinate, active only during the measurement window — reproduces Born statistics within ε = 1e-2 on the identical 2-level test protocol, with a minimal noise magnitude σ_min that is strictly positive, reported as the principal result, and consistent with the Wu-2013 strong-field constraint (noise off outside the measurement window, inherited).

## 2. Sealed parameter ledger

| Parameter | Value / range | Free? |
|:----------|:--------------|:------|
| Relaxation family | A/B/C exactly as sealed in REG-RES018-001 (relaxation_sim.py rev.3, unmodified) | NO |
| Noise type | WHITE (Wiener increments per relaxation step) | NO (fixed: minimal choice) |
| Noise coupling | ADDITIVE on z only (x, y noise-free) | NO (fixed: minimal choice) |
| σ grid | logspace(1e-3, 1, 21) | NO |
| σ_min definition | smallest grid σ with max_dev < ε, then log-bisection ×20 to ≥2 significant figures | NO |
| ε | 1e-2 | NO |
| N (shots) | 1e5 per state in the MC validation layer | NO |
| dt (RK4 step) | τ_m / 500 | NO |
| Test set | 9 canonical + 50 random Bloch states, EXACTLY the sealed REG-RES018-001 draw (asserted against verdict-input.json) | NO |
| RNG | fixed seeds (SEED_EXT = 20260821; per-state MC seeds SEED_EXT + state_index) | NO |

**dof ledger:** each config inherits its sealed dof count (A = 2, B = 3, C = 2) PLUS one global parameter σ. The constraint count is unchanged (one: Born statistics). The falsifiable content is the σ_min boundary per config.

## 3. Sealed computation protocol (two layers)

**Layer 1 — analytic (primary).** For variants A/B/C the z-drift is affine in z with deterministic coefficients (x, y are unaffected by z-noise). The discrete relaxation map is therefore z_{k+1} = A_k z_k + b_k, with A_k the exact z-Jacobian of the RK4 update (finite-difference probe, PROBE_DELTA = 1e-7; exact because the map is affine in z). Under additive white noise the final z is Gaussian:

- z_final ~ N(z_det, σ² · V), where V = Σ_j S_j² · dt, S_j = Π_{k>j} A_k (backward accumulation);
- P(+) = Φ(z_det / (σ √V)).

This is the exact N → ∞ limit of the shot estimator; it is a theorem, not a tuning choice, and is stated here pre-run.

**Layer 2 — Monte Carlo validation (implementation + Gaussianity check).** 3 (variant, σ) configs — (A, 0.01), (B, 0.1), (C, 0.1) — × 14 states (9 canonical + 5 spread random indices) × N = 1e5 independent per-shot noise paths propagated through the SAME A_k/b_k discrete map. Assertion: |P_MC − P_analytic| < MC_TOL = 5e-3 (sampling-limited budget: binomial std ≈ 1.6e-3 at p ≈ 0.5). A failed assertion = harness bug, NOT a result; fix requires re-seal.

## 4. Verdict rules (pre-committed)

Per config (A×{γτ ∈ 0.5, 5, 50}, B×{α ∈ 0.01, 0.1, 1}, C):
- PASS if a σ_min > 0 exists in range with max deviation < ε over the full 59-state test set; report σ_min.
- CC-2 DISCONFIRMED if (a) no σ in the grid achieves max_dev < ε for ANY config, OR (b) σ_min = 0 (excluded by REG-RES018-001's degeneracy, checked anyway), OR (c) the σ_min required exceeds a physically meaningful bound (Hacohen-Gourgy & Martin 2020 weak-measurement noise-floor constraint; documented if a passing σ_min exists).

## 5. Seal integrity

- Harness: `notebooks/relaxation_sim_ext.py` — sha256 `136ed27dc976cb9a5ebe3eacbfcd4402ddaf8630d11c7b8db2de763a9a9f9252`.
- The sealed REG-RES018-001 harness (relaxation_sim.py rev.3) is imported UNMODIFIED; its own seal sha is unchanged.
- Verification at run time: `git show <seal-commit>:relaxation-equation-mechanism/notebooks/relaxation_sim_ext.py | sha256sum` must equal the hash above.
- Output: `artifacts/verdict-input-002.json` (harness self-checks its own sha into `_seal_sha256`).

## 6. Analysis pipeline (post-run, separate)

- `notebooks/relaxation_verdict_002.py` reads verdict-input-002.json and writes `artifacts/verdict-002.md` (verdict + deviation tables + σ_min report or disconfirmation evidence). The analysis script is NOT part of the seal (it transforms sealed outputs only); it is committed before running for transparency.
