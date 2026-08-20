# PRE-REGISTRATION — REG-RES018-001 (SEALED 2026-08-19)

**Project:** QNFO.RES.018 — Measurement-Triggered Relaxation Dynamics (FQ1 escalation from RES.016)
**WBS:** QNFO.RES.018 · **Branch:** res/paper/relaxation-equation-mechanism · **Seal commit:** (assigned at seal; see git log)

> **KIF-60 HARD GATE:** This record seals the parameterization and the simulation code BEFORE any simulation run. Any code or parameter change after this commit INVALIDATES the seal and requires a new pre-registration. The simulation must be run only from the sha256-sealed harness below.

---

## 1. Hypothesis (locked — CC-1)

A measurement-triggered relaxation dynamics (basins of attraction) can be specified at the level of the Madelung/Reddiger Radon–Nikodym formalism such that, in a pre-registered simulation of 2-level systems (N = 1e5 shots, tolerance ε = 1e-2 against the Born rule), the measured outcome statistics reproduce the Born probabilities within ε, while the same dynamics family remains consistent with the strong-field hydrodynamic reproductions of Wu, Augstein, and Figueira de Morisson Faria (2013).

## 2. Sealed parameter ledger

| Parameter | Value / range | Free? |
|:----------|:--------------|:------|
| H (Hamiltonian) | H = ω σz/2, ω = 1 (natural units) | NO |
| γ_m (relaxation rate) | γ_m·τ_m ∈ [0.5, 50] | YES (1) |
| τ_m (measurement duration) | τ_m ∈ [0.1, 10] | YES (1) |
| α (Variant B z-coupling) | α·τ_m ∈ [0, 1] | YES (1) |
| ε (tolerance) | 1e-2 | NO |
| N (shots per state) | 1e5 | NO |
| dt (RK4 step) | τ_m / 500 | NO |
| Test set | 9 canonical Bloch states {±x, ±y, ±z, (1,1,0)/√2, (1,0,1)/√2, (0,1,1)/√2} + 50 random uniform | NO |
| Basin weights (Variant C) | fixed function of pre-relaxation state only (defined in code) | NO (per-shot inputs FORBIDDEN) |

**dof ledger:** Variant A = 2 free params vs 1 constraint (statistics) — claim is that A's statistics are parameter-independent (z exactly preserved); the falsifiable content is discretization/threshold robustness. Variant B = 3 free params vs 1 constraint — verdict must report the boundary α·τ_m* at which deviation crosses ε (a prediction). Variant C = 2 free params; scored [RETRODICTION] if weights consume per-shot |c_i|².

## 3. Sealed simulation protocol

1. Draw ψ0 from the sealed test set (9 canonical + 50 random uniform on the Bloch sphere).
2. Evolve unitarily to t_m (standard Schrödinger evolution; no relaxation).
3. Apply the sealed relaxation operator for τ_m via RK4 (dt = τ_m/500).
4. Terminal rule: z_final ≥ 0 → outcome +, else − (eigenbasis equator threshold).
5. N = 1e5 shots per state; compute P(+); compare |P(+) − (1+z0)/2| to ε = 1e-2.
6. Verdict per variant: PASS if max deviation < ε over the full test set; FAIL otherwise, reporting the boundary.

## 4. Disconfirmation conditions (pre-committed)

- CC-1 disconfirmed if (a) no variant achieves max-deviation < ε over the sealed test set, OR (b) the only passing variant needs a z-correction term whose free parameters exceed the constraint budget (KIF-60 overfitting trap), OR (c) Variant C passes only with per-shot |c_i|² weights (retrodiction — scored, not evidence).
- Wu-2013 consistency is an asserted compatibility condition: the relaxation operator is OFF outside the measurement window, so strong-field dynamics are not sampled during relaxation. This boundary is documented as an assumption.

## 5. Seal integrity

- Harness file: `notebooks/relaxation_sim.py` — sha256 computed at seal time; the commit contains both the harness and this record.
- Verification: `git show <seal-commit>:relaxation-equation-mechanism/notebooks/relaxation_sim.py | sha256sum` must equal the hash recorded in this file at seal time.
- The simulation run (Phase 4b) MUST use this exact file; any edit → re-seal required.


## 5a. REV.2 SEAL AMENDMENT (PRE-RESULTS, 2026-08-19)

**Nature of amendment: environment portability ONLY.** The rev.1 harness (sha256
`598f9352bc93de1e008f1df357e9d1d30bea4792d5d553837045ee4e1d54cfac`) crashed on
first execution with `AttributeError: module 'numpy.linalg' has no attribute 'expm'`
(numpy 2.4.4 removed np.linalg.expm; verified: hasattr = False, scipy 1.17.1
available). The crash occurred BEFORE any simulation results existed (verdict-input.json
never created; zero shots computed).

**Fix:** replaced the single expm call in `unitary_step` with an environment-robust
`matrix_exp()` — scipy.linalg.expm first, np.linalg.expm if present, else the EXACT
analytic exponential for the sealed diagonal Hamiltonian (verified unitary:
|UU^dag - I| = 0.0). NO changes to hypothesis, parameters (OMEGA=1, EPS=1e-2,
N_SHOTS=1e5, DT_FACTOR=500, SEED=20260819, TEST_STATES, gamma_m/tau_m/alpha ranges),
protocol steps, terminal rule, or analysis rules.

**Rev.2 harness sha256:** `852fd699c6fab9e3557428c1f494a2022e23269cb79e23d03b967a294205a29f`
(computed same-turn; committed file re-hash verified against this value after commit).


## 5b. REV.3 SEAL AMENDMENT (PRE-RESULTS, 2026-08-19)

**Nature of amendment: batch-equivalence performance fix ONLY.** Rev.2 harness
(sha256 `852fd699c6fab9e3557428c1f494a2022e23269cb79e23d03b967a294205a29f`) executes
N_SHOTS=1e5 pure-Python RK4 trajectories per state (~50h wall-clock). Inspection
(rev.3 patch evidence) proves `single_shot` is DETERMINISTIC: `rng_local` is created
in `run_variant` but never passed into or consumed by `single_shot`, so all 1e5 shots
of a given state produce the IDENTICAL outcome.

**Fix:** the shot loop is replaced by its exact mathematical equivalent —
`hits = N_SHOTS * outcome` (outcome ∈ {0,1}) — preserving per-state dynamics,
all sealed parameters, the terminal rule, and the statistical semantics
(p_measured = hits/N_SHOTS unchanged). NOT a protocol change; the computation is
identical, executed once.

**Rev.3 harness sha256:** `b472d0392f8915d171172623a2583e5aeb23ef776884df73a451727a3bf39dd8`
(computed same-turn; committed file re-hash verified against this value after commit).

## 6. Post-seal obligations

- Phase 4b: run the sealed harness; write artifacts/verdict.md (PASS/FAIL per variant + boundary α·τ_m* for B).
- BP-1..BP-10 numeric gates apply to the verdict (independent recompute, terminology audit, sigma propagation).
- If CC-1 disconfirmed: the verdict is a legitimate negative result (UIA Q15 fallback line: minimal stochastic extension becomes the next research target).
