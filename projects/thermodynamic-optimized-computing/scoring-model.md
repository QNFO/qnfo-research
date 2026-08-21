# Platform Scorecard and Crossover Model — Specification

**Project:** Thermodynamically Optimized (Topological/Quantum) Computing
**Date:** 2026-08-21 · Working specification for the paper (Section 3 draft material + verification target)

---

## 1. The scorecard quantity

For each platform, the scorecard reports an **energy per correct solution** proxy for a fixed benchmark computation of N logical operations:

> E_per_correct_solution = (E_operation × overhead × N) / P(correct run)

- **E_operation** — energy per elementary operation (gate) at the physical level, including control and cooling amortization when published data allows.
- **overhead** — the correction factor: 1 for hardware-protected qubits; the physical-qubits-per-logical-qubit factor (plus ancilla and measurement factors) for active error correction.
- **P(correct run)** — the probability the whole computation completes correctly, modeled from the logical error rate L as approximately exp(−N·L) for uncorrelated logical failures.

The quantity is deliberately a proxy, not the full joules-per-solution metric: it uses published data that exists today and degrades gracefully where full measurement-protocol data does not. Where a platform's entry relies on an estimate, the cell is marked and the estimate's source is stated.

## 2. Scorecard axes (table skeleton)

| Platform | E_operation [J] | Physical error rate p | Correction overhead | Cooling/system overhead | E_per_correct_solution [J] | Source status |
|---|---|---|---|---|---|---|
| Superconducting transmon | 8.2×10⁻²⁵ (program anchor) | [P4: primary source] | [P4: code table] | [P4: primary source] | computed | anchor + to-fill |
| Trapped ion | [P4] | [P4] | [P4] | [P4] | computed | to-fill |
| Silicon spin | [P4] | [P4] | [P4] | [P4] | computed | to-fill |
| Photonic | [P4] | [P4] | [P4] | [P4] | computed | to-fill |
| Protected (topological/Majorana) | [P4] | exp(−Δ/kT) model | 1 (no active correction) | [P4] | computed | model + to-fill |

Cells marked [P4] are filled at the paper-writing phase from primary literature; every filled cell will carry its source in the paper's reference list. No cell ships with an unsourced number.

## 3. Crossover model

Two competing strategies protect the computation.

**Active correction.** For a platform with physical error rate p and a surface-code family with threshold p_th, the overhead scales with the code distance d, and the logical error rate falls as (p/p_th) raised to a power growing with d. The energy per correct solution is E_operation × overhead × N × exp(N·L). A decoder-efficiency factor δ divides the effective overhead, capturing the constant-overhead QLDPC regime as δ → large.

**Hardware protection.** A protected qubit carries no correction block; its logical error rate is modeled as thermal activation, L = A·exp(−Δ/(k_B T)), where Δ is the protection gap (topological gap or equivalent energy scale) and T the operating temperature. The energy per correct solution is E_operation × N × exp(N·L).

**The crossover** is the surface in (p, T, Δ, δ) space where the two energies are equal. The verification script sweeps this surface for a benchmark of N = 10⁶ logical operations and reports, for each (T, Δ) pair, the best physical error rate available to the correction strategy and which strategy wins. The qualitative expectation — protection wins only when Δ/(k_B T) is large, correction wins at high temperature, and efficient decoders push the crossover in correction's favor — is checked numerically rather than asserted.

## 4. Pre-registered predictions (failure conditions)

Stated before the comparison is completed, in plain language:

1. **Prediction P1.** At operating temperatures of 15 mK and a protection gap of order 10⁻²² J (sub-kelvin energy scale), hardware protection beats active correction for the benchmark unless decoder efficiency is high; at 1 K and above, active correction wins at every physical error rate below threshold. (Checked by the verification script now; re-checkable by anyone with the script.)
2. **Prediction P2.** If no protected platform demonstrates a logical error rate below the best corrected platform's rate at equal measured energy within the scorecard's data window, the quantum-semiconductor thesis fails as stated.
3. **Prediction P3.** If the published platform data filled in at Phase 4 changes the scorecard ranking relative to the model's prediction, the model — not the data — is revised, and the revision is published.

The paper will report which predictions survive and which fail, with the computed numbers attached.

## 5. Computational verification

All quantitative claims in this specification are checked by the scripts in `artifacts/verification/`:

- `thermo_bounds.py` — golden values: Landauer bound at 300/77/4/1 K and 15 mK; Margolus–Levitin bound at 1 ns/100 ps/1 ps operation times; Bremermann bound; recomputation of the 8.2×10⁻²⁵ J per-gate program anchor; the 10²–10³ correction-overhead arithmetic; the 55× tree-code/surface-code threshold ratio.
- `crossover_model.py` — the Section-3 crossover surface with fixed seed, decoder-efficiency sensitivity, and a 1,000-sample Monte Carlo estimate of the probability that protection beats correction under log-uniform physical-error-rate uncertainty at the flagship (T, Δ) point.

Reproducibility notes (runtime, seed, dependencies) live in `artifacts/verification/REPRODUCIBILITY.md`. Scripts use only the Python standard library.
