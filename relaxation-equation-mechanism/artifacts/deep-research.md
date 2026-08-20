# Deep Research — QNFO.RES.018 Phase 4 (pre-registration package)

**Date:** 2026-08-19 · **Status:** pre-registration package (seal commit follows; no simulation run before seal — KIF-60 HARD)

---

## 1. Cell-verification (Phase 4a — mandatory before the seal)

**Claim under test (CC-1):** a measurement-triggered relaxation dynamics (basins of attraction) specified at the level of the Madelung/Reddiger Radon–Nikodym formalism reproduces Born statistics within ε=1e-2 on 2-level systems, consistent with Wu et al. (2013) strong-field reproductions.

**Cell check — does any verified program occupy this exact cell?**

| Program (Phase 2 evidence) | Formalism | Measurement-triggered? | Basins-of-attraction? | Wu-2013-consistent? | Cell match |
|:---------------------------|:----------|:-----------------------|:----------------------|:--------------------|:-----------|
| Valentini 1991/2005/2010 (subquantum H-theorem) | de Broglie–Bohm config space | No (cosmological/early-universe relaxation) | No (equilibrium in config space) | n/a (dBB strong-field is the Wu anchor itself — different target) | ✗ |
| Nelson-stochastic 2023 | Nelson stochastic dynamics | No (stochastic relaxation) | No | n/a | ✗ |
| Entropy 2021 (Drezet) | dBB + deterministic chaos | No | No | n/a | ✗ |
| Aerts 2014 (hidden measurement) | EBR hidden-measurement algebra | Yes (measurement = hidden measurement) | No (measurement-interaction probabilities, not attractor basins) | n/a | ✗ |
| 't Hooft 2020 | cellular automaton | No | No | n/a | ✗ |
| GRW 1986 / CSL 1989 / QSD | stochastic collapse | Yes | No (random hits, not basins) | n/a | ✗ |
| **This project (CC-1)** | **Madelung/RN-Kolmogorovian** | **Yes (coupling switches relaxation on)** | **Yes (eigenstate basins in Bloch ball)** | **Yes (constraint stated)** | **✓ UNOCCUPIED** |

**Verdict: the exact cell is unoccupied.** The seal proceeds.

## 2. Candidate relaxation family (Phase 4b — the equations)

2-level system, Hamiltonian eigenbasis {|+⟩,|−⟩}, Bloch coordinates (x,y,z), ρ = ½(I + xσx + yσy + zσz).

**Pre-measurement (t < t_m):** unitary evolution dρ/dt = -i[H, ρ] (standard; the RN variables are defined within this dynamics per Reddiger 2026 — Phase 1 evidence).

**Measurement (t ≥ t_m):** relaxation operator added:

dρ/dt = -i[H, ρ] + γ_m · L_c(ρ)

where L_c is one of:

- **Variant A — pure eigenbasis attraction:** L_A(ρ) = -(ρ - diag(ρ)) = -½(x σx + y σy). Drives (x,y) → 0 at rate γ_m, **preserves z exactly**. Outcome threshold at z=0 (eigenbasis equator): P(+) = (1+z0)/2 = |⟨+|ψ0⟩|² — Born rule with **zero free parameters** (γ_m sets only the timescale).
- **Variant B — xy-coupling with z-perturbation:** L_B(ρ) = -(ρ - diag(ρ)) + δ(x,y,z) where the apparatus coupling perturbs z: dz/dt gains a term -α·(x²+y²)·z (generic dissipative coupling). Born deviation scales with α·τ_m — the falsifiable content: find whether ANY (α, γ_m, τ_m) regime keeps deviation < ε while the relaxation completes.
- **Variant C — radial-basis basins:** L_C(ρ) = -(ρ - Σ_i w_i(|c_i|²)·Π_i) with basin weights w_i depending on the instantaneous Born weights — the literal "basins of attraction" version. **This variant is flagged as the KIF-60 overfitting trap candidate**: if w_i = |c_i|² is used as a free per-shot input, the test is vacuous (retrodiction). The pre-registered constraint: w_i must be a FIXED function (no per-shot inputs), or Variant C is scored as [RETRODICTION — not evidence].

## 3. Parameter ledger (REG-RES018-001 — sealed)

| Parameter | Role | Free? | Constraint |
|:----------|:-----|:------|:-----------|
| γ_m | relaxation rate during measurement | YES (1) | γ_m·τ_m ∈ [0.5, 50] (completion window) |
| τ_m | measurement duration | YES (1) | τ_m ∈ [0.1, 10] in natural units |
| α (Variant B only) | z-perturbation coupling | YES (1) | α·τ_m ∈ [0, 1] |
| H | 2-level Hamiltonian | NO | fixed: H = ω σz/2, ω = 1 |
| ε | tolerance | NO | fixed: 1e-2 |
| N | shots | NO | fixed: 1e5 |
| basin weights (Variant C) | attractor structure | NO | fixed function of the PRE-RELAXATION state only, defined in code, sealed |

**Degrees-of-freedom check:** Variant A: 2 free params (γ_m, τ_m) against 1 independent constraint (statistics within ε) → **dof > constraints for A? No: A's statistics are parameter-independent (z preserved exactly), so A is a 0-dof claim — the question is whether the idealization survives the discretization and the threshold rule.** Variant B: 3 free params against 1 constraint → flagged; the verdict must report the boundary α·τ_m* at which deviation exceeds ε (a prediction, not a fit). Variant C: fixed weights → 2 free params; scored as retrodiction if weights use per-shot |c_i|².

## 4. Simulation protocol (sealed)

1. Draw ψ0 uniformly on the Bloch sphere (or a fixed test set: 9 canonical states + random) — **the state distribution is part of the seal**.
2. Evolve unitarily to t_m (no relaxation).
3. Apply the sealed relaxation operator for τ_m (Runge-Kutta 4, dt = τ_m/500).
4. Terminal rule: project the final Bloch state onto {+,−} by z-threshold (z_final ≥ 0 → +). Collect outcome.
5. Repeat N = 1e5 shots; compute |P(+) - (1+z0)/2| per state; compare to ε = 1e-2.
6. Verdict per variant: PASS if max deviation < ε over the test set; FAIL otherwise with the boundary reported.

## 5. Disconfirmation conditions (sealed)

- CC-1 disconfirmed if: (a) no variant achieves max-deviation < ε, OR (b) the only passing variant requires a z-correction term whose free parameters exceed the constraint budget (KIF-60 overfitting), OR (c) Variant C passes only with per-shot weights (retrodiction — scored, not evidence).
- The Wu-2013 consistency constraint is asserted as a compatibility condition (the relaxation is off outside measurement; inside measurement the strong-field dynamics is not sampled) — documented as an assumption with this boundary.

## 6. Practitioner deliverable (unchanged from PROJECT-PLAN §8)

Sealed harness = audit-proof falsification package: any practitioner can reproduce the run from the sha256-sealed code + this ledger; the verdict is binary and pre-committed.
