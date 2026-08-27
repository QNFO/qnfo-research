# Phase 4 Results — Hypothesis-Card Reconciliation (QNFO.RES.028, 2026-08-27)

All three adjudication scripts ran to completion with every check passing
(final logs: `artifacts/verification/final_m_anyon.log`,
`final_braid.log`, `final_prime_gap.log`; machine-readable results in the
same-named `.json` files).

## Verdicts

| Card | Verdict | Summary |
|:-----|:--------|:--------|
| C1 — the bounded-occupation family cannot carry braid exchange phases | **CONFIRMED** | The m-family determines no exchange phase: occupation-label swaps give only ±1 eigenvalues; every observable is invariant under arbitrary inserted phases; the canonical symmetric reading is +1 for every m (including m=1, where real fermions carry −1). No m reproduces the Laughlin phase e^{iπ/m} (m ≥ 2). The occupation curve is Gentile, not Haldane, statistics at finite m (endpoints only). |
| C2 — the phase carriers are characters at roots of unity | **CONFIRMED** (abelian test set + Fibonacci data; [RETRODICTION] grade) | Laughlin e^{iπ/m} is a primitive 2m-th root of unity (m = 1,2,3,5,7); Fibonacci braid eigenvalues are q⁴ and −q² at q = e^{iπ/5}; the TL family δ_k = 2cos(π/(k+2)) sits on the root-of-unity locus (√2 Ising, φ Fibonacci, √3 k=4). |
| H2 — prime-gap specific-heat deviation | **CONFIRMED** | ΔC_V ≠ 0 at every sampled temperature in both statistics, quantified across β ∈ [1.1, 6.0] with the Bost–Connes point (β = 1) respected. Internal to the Riemann-gas model; not a laboratory prediction. |

## H2 quantified

| β | ΔC_V bosonic | rel | ΔC_V fermionic | rel |
|:--|:-------------|:----|:---------------|:----|
| 1.1 | −1.3857 | 2.9% | −1.6293 | 3.6% |
| 1.25 | −0.8740 | 4.1% | −1.2207 | 6.4% |
| 1.5 | −0.3579 | 4.2% | −0.7864 | 11.2% |
| 2.0 | +0.1389 | 3.9% | −0.2890 | 10.9% |
| 3.0 | +0.4285 | 27.6% | +0.1734 | 14.4% |
| 4.0 | +0.4279 | 47.7% | +0.3118 | 40.8% |
| 6.0 | +0.2551 | 73.7% | +0.2384 | 72.5% |

Sign structure: negative at high temperature (the smooth staircase over-counts
low-energy mode density at the very bottom of the spectrum — its first mode
sits at Li₂⁻¹(1) ≈ 2.87, above the prime 2), positive at low temperature where
the prime-gap structure dominates C_V (up to ~74% relative at β = 6). Goldens
(primes, β = 3): bosonic 1.550526403, fermionic 1.204541647.

## Hypothesis-card execution parity (HYPOTHESIS-CARD-EXECUTION-PARITY-1)

- **C1** card wording: "for no m does it reproduce the fractional exchange phase e^{iπ/m} … or the Haldane-g thermodynamic signatures outside the regimes where HES is known to coincide with braid statistics." Executed test is *stronger* on the phase leg: phase-indeterminacy (no phase datum exists to match) rather than mere non-match — the Laughlin non-match follows a fortiori. The Haldane leg executed as carded, with both natural mappings g = 1/m and g = 1/(m+1) tested and the endpoints pinned (g = 1/m is the endpoint-correct interpolation). Drift = strengthening, documented, no family-definition change.
- **C2** card: "the character model reproduces the established abelian anyon exchange phase, and the m-family does not." Executed as carded on the abelian test set, extended with the Fibonacci/TL root-of-unity data. No drift.
- **H2** card: "the prime-gap density of states produces a specific-heat deviation from the smooth-DOS ideal gas." Executed as carded; the smooth baseline is the exact PNT staircase (Li₂⁻¹(k), machine precision, strictly increasing). The card's internal-to-model caveat (risk register) is honored in the verdict and here.

## Disconfirmation monitors

- D1 (m-family match to a known anyonic datum): not triggered.
- D2 (established abelian anyon phase not a root of unity): not triggered — monitor armed, no physical model with irrational θ established.
- D3 (ΔC_V ≡ 0 at every temperature): not triggered.

## VERIFY-FIX-RERUN-1 ledger (check-construction corrections during Phase 4)

1. H1 threshold miscalibrated (`s2 > 8`) → replaced with Mertens-law tracking (ln ln x + B, two cutoffs).
2. Asymptotic-series leading term dropped (bracket started at 0 instead of 1) → fixed; the self-check caught the err ~ x/L signature it was designed for.
3. H3 bound miscalibrated against the divergent series' optimal-truncation floor → recalibrated (2.0 envelope), then superseded by the exact construction (item 5).
4. G3 normalization defect (|Σw|² instead of Σ|w|² in the phase-invariance check) → fixed; invariance then exact by construction.
5. Branch-seam non-monotonicity at k = 273 (series/exact boundary; series remainder ≈ 1.9 at x ≈ 1700 pulls S⁻¹(273) below Li₂⁻¹(272)) → root-caused and eliminated: the final construction computes exact Li₂⁻¹(k) for *all* 78,498 modes via an ascending tangent-seeded Newton walk; the asymptotic series is removed entirely.
6. G4 endpoint mapping (g = 1/(m+1) gives g = 1/2 at m = 1, not the Fermi endpoint) → both mappings tested with endpoints pinned on g = 1/m.
7. C1 verdict gate did not require every check (blind_ok, endpoints) → gate now requires all.
8. Print-label staleness (g = 0.01 vs 0.001) → corrected; pristine re-run.

Every correction is a check-construction or presentation fix; no hypothesis-card
wording, family definition, or claim was altered to fit a failing check.

## Evidential weight (KIF-60)

C1's content is an adjudication (boundary claim with disconfirmers) — its weight
is the elimination of the correspondence candidate, not a prediction. C2 is
`[RETRODICTION]` (identity checks of established anyon data). H2 is the only
forward computation — graded `[PREDICTION]`, internal to the Riemann-gas model,
pending independent scrutiny. This distribution is stated in the consilience
gate and the paper will carry the same labels.
