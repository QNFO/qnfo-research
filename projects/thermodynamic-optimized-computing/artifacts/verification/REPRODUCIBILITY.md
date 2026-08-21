# Verification Reproducibility Statement

**Project:** Thermodynamically Optimized (Topological/Quantum) Computing — Phase 3 verification
**Date:** 2026-08-21

## Scripts

| Script | Purpose |
|---|---|
| `thermo_bounds.py` | Golden values: Landauer bound (300/77/4/1 K, 15 mK), Margolus–Levitin bound (1 ns/100 ps/1 ps), Bremermann bound, recomputation of the 8.2×10⁻²⁵ J/gate program anchor, 10²–10³ correction-overhead arithmetic, 55× tree-code/surface-code threshold ratio. |
| `crossover_model.py` | Protection-vs-correction energy crossover surface (T, Δ, decoder efficiency, physical error rate) for a 10⁶-operation benchmark, plus a seeded 1,000-sample Monte Carlo of the winner under log-uniform error-rate uncertainty. |

## Environment

- **Runtime:** Python 3 (any 3.8+; tested 3.12)
- **Dependencies:** standard library only (`math`, `csv`, `os`, `random`)
- **Seeds:** crossover sweep deterministic; Monte Carlo seed `20260821`
- **Runtime:** under 1 second for both scripts
- **Constants:** CODATA/SI-exact — k_B = 1.380649e-23 J/K, h = 6.62607015e-34 J·s, c = 2.99792458e8 m/s

## How to re-run

```
cd projects/thermodynamic-optimized-computing/artifacts/verification
python thermo_bounds.py        # -> outputs/thermo_bounds.csv + self-check console
python crossover_model.py      # -> outputs/crossover_results.csv, outputs/mc_winner_samples.csv
```

## Outputs

- `outputs/thermo_bounds.csv` — every golden value in SI units with a self-check column.
- `outputs/crossover_results.csv` — 32 crossover scenarios (2 decoder efficiencies × 4 temperatures × 4 protection gaps).
- `outputs/mc_winner_samples.csv` — 1,000 Monte Carlo samples at the flagship point (15 mK, 10⁻²² J).

## Model caveats (stated, not hidden)

The crossover model uses heuristic distance scaling for the surface-code family and a single-exponential thermal-activation law for protection. It is a trade-off-surface illustration whose qualitative conclusions (protection wins only at large Δ/k_B T; decoder efficiency shifts the crossover) are robust to parameter choices within plausible ranges. The scorecard's filled-in platform numbers are the authoritative test; the model is the map, not the measurement.
