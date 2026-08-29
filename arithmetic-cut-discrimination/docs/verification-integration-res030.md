# Verification Integration — QNFO.RES.030 P3

Date: 2026-08-29. Every number below comes from the executed scripts
(`artifacts/verification/sim-*.py`, seed 20260829, Python 3.12.10, NumPy 2.4.4,
SciPy 1.17.1, mpmath 1.3.0 not needed — zeros via the canonical Riemann–Siegel
method of UMP.014's `sim-riemann-zeros-fast.py`). Outputs:
`sim-spectral-estimators-output.json`, `sim-arithmetic-cut-discrimination-output.json`,
run logs in the same directory. Runtime: 3.4 s + 2.5 s.

## 1. Pipeline validation (six construction rules)

| Check | Result | Verdict |
|---|---|---|
| B1/B6 pair correlation, GUE control (n=800, M=8, pooled) vs analytic 1−(sin πs/πs)² | MAD **0.0706** | PASS |
| B4 Montgomery–Odlyzko: first 3000 zeros, RVM unfolding | MAD vs GUE **0.1086**; repulsion R2(0-bin) 0.0200 | PASS (consistent with UMP.014's 0.061 at a different pooling) |
| B4 twin-gap hard core (primes, P=2¹⁴, N=1900) | s_min = 0.206128 vs 2/ln P = 0.206099; count below threshold = **0 exactly** | PASS (4 sig figs) |
| B5 form factor, primes, single realization, report-only | K(0.5)=0.476, K(1.0)=0.412, K(2.0)=1.451 | report-only, no claim |
| A3/D-3 planted control (N=4000, ε=0.2, λ_u=ln 4) | τ̂=0.721407 vs τ*=0.721348 (**8.3×10⁻⁵**); peak 37.7 vs theory ε²N/4=40; plateau 0.7 | **PASS — positive control recovered** |
| Primes pair correlation vs Poisson/GUE (P=2¹⁴) | MAD 0.357 / 0.298 | honest: twin clustering + hard core at low cutoff (Gallagher is asymptotic) |

Estimator bugs found and fixed during P3 (documented for the record): per-order
normalization by in-range histogram count (bias 1/f_k near the window edge)
→ normalized by total per-order count (n−k); planted-peak grid resolution
(peak width ~1/N vs grid step) → dense scan. The GUE control MAD fell
0.415 → 0.0706 after the normalization fix.

## 2. Golden anchors on the cut

- High-T equipartition: C_V^B(β=10⁻³)/N = **0.999992** (exact limit 1; the
  provenance chats' "→ P_max" is corrected to π(P_max)).
- Low-T collapse: C_V^B,F,MB(β=60) / [β²(ln 2)² 2^{−β}] = **1.000** exactly, all
  three statistics.
- Bost–Connes pole amplitude: β²/(β−1)² at β=1.06 = **312.111** reproduced.
- Prime zeta (N2 correction to the chats): Σ_{p≤2¹⁶} p^{−2} = 0.45224615 vs
  known P(2) = 0.45224742 (tail ≈ 1.4×10⁻⁶). The chats' "ln Z_MB → Li(e^{−β})"
  is false; the object is the prime zeta function.

## 3. D-1: the published Dyson anomaly, adjudicated (exact-theory reference)

Measured number variance of the first 3000 zeros vs BOTH the full Dyson
asymptotic AND the exact two-point reduction Σ²(L) = L − 2∫₀^L(L−s)(sinπs/πs)²ds
(evaluated numerically at the same L; windows stated):

| L | measured Σ² | Dyson asymptotic | exact theory | measured/exact | windows |
|---|---|---|---|---|---|
| 5 | 0.690 | 0.384 | 0.509 | 1.35 | 607 |
| 10 | 0.681 | 0.454 | 0.579 | 1.18 | 303 |
| 15 | 0.893 | 0.495 | 0.620 | 1.44 | 202 |
| 20 | **1.206** | 0.525 | **0.650** | **1.86** | 151 |
| 25 | 1.207 | 0.547 | 0.672 | 1.80 | 121 |
| 30 | 1.192 | 0.566 | 0.691 | 1.73 | 101 |
| 50 | 2.078 | 0.617 | 0.742 | 2.80 | 60 |
| 3400 | — (0 windows) | **1.0449** | — | — | 0 |

Two independent findings, both from executed computation:

1. **The Dyson asymptotic mis-fits by 20–33% at L ≤ 50** (it converges from
   below). The GUE control matches the EXACT reduction within 8–13% at
   n = 800–2000, and the estimator passes the uniform-grid (Σ² = 0.0 exact)
   and exact-Poisson (10.63 vs 10.0) sanity checks — so the estimator is
   validated against exact theory, and any use of the Dyson formula at
   L ≤ 50 without the exact-theory correction is a wrong reference.
2. **The published sentence "Dyson number variance 1.044 against the predicted
   0.525" is doubly invalid**: (a) it mixes windows — Dyson(L=3400) = 1.0449
   reproduces the published "measured 1.044" to four digits, while
   0.525 = Dyson(L=20); (b) even at a single L the asymptotic reference is
   ~24% below the exact theory at L=20 (0.6495). After correcting the
   baseline, the zeros' measured values still exceed the exact theory by
   1.2–2.8×, growing with L — the low-height S(t) unfolding residual,
   isolated from the baseline error. Any reuse of the published number must
   state L, the unfolding, the exact-theory reference, and the height.

## 4. D-4: the Bost–Connes observable is a crossover, not a rounding

C_V^B(1.06) = **33.1 (P_max=10⁴), 47.5 (10⁵), 62.7 (10⁶)** vs the pole
amplitude 312.1. The approach to the pole is power-law in the tail
Σ_{p>P} p^{−β} ≈ P^{1−β}/((β−1)ln P) — at β=1.06 the tail is ≈222 at
P_max=10⁶, i.e., the truncation is the DOMINANT term at every feasible P_max.
**The published "C_V(1.06) = 316.3 vs predicted 312.1" cannot come from a
direct truncated-product computation at any plausible cutoff** — either an
unstated tail-corrected construction or an error; the deposited script's
construction must be disclosed before that number is reused. RES.030 reports
the finite-P_max crossover table as the honest observable.

## 5. The "three quarters" claim, located

Relative deviation from the ideal gas D(β) = (N·k_B − C_V^B)/N·k_B is monotone:
D=0.75 at β≈0.42 (T ≈ 2.4·T₀ — intermediate), D→1.0 as β→∞ (full freeze-out).
**"Up to roughly three quarters at low temperature" is mis-located**: the
deviation reaches three quarters at intermediate temperature and approaches
100% at low temperature. The correct statement: exceeds 3/4 for all T ≲ 2.4T₀.

## 6. D1/D2/D3: the discrimination sweep (M=30 null realizations)

C_V channel (z = separation in σ of the null self-distribution; 2σ = separated):

| P_max (N) | stat | z vs N2 | z vs N3 |
|---|---|---|---|
| 2⁸ (54) | B | **4.94** | 0.28 |
| 2⁸ | F | **5.33** | 1.85 |
| 2⁸ | MB | **5.21** | 1.58 |
| 2¹² (564) | B | **26.28** | **4.09** |
| 2¹² | F | **29.21** | **14.62** |
| 2¹² | MB | **28.34** | **12.98** |
| 2¹⁶ (6542) | B | **86.50** | **21.32** |
| 2¹⁶ | F | **102.39** | **63.60** |
| 2¹⁶ | MB | **97.62** | **56.24** |

Two-point channel (R2 curve, uniform L2, per-family unfolding): z_r2 ≈ **−0.8
at every P_max** — no separation. Focused hard-core mass test (fraction of
nearest-neighbor spacings below 2/ln P at P_max=2¹⁶): cut **0.0** vs N2
0.1656 ± 0.0049 → |z| = **33.8**.

**D1 — CONFIRMED.** At least one observable separates at ≥2σ beyond computable
P_max, in every statistics: C_V vs N2 from P_max ≥ 2⁸; C_V vs N3 from
P_max ≥ 2¹²; the two-point hard core at ~34σ.

**D2 — DISCONFIRMED as pre-registered.** The claim was "the specific heat alone
cannot separate; the information resides in the two-point statistics." The
computation gives the opposite under the uniform measure: C_V alone separates
massively at every tested P_max, while the full two-point curve does not
separate at any tested P_max; the two-point information is concentrated in the
small-s hard core (Gallagher's Poisson plus the twin-gap exclusion), which
needs a focused test to resolve. The pre-registered disconfirmation branch
fired exactly as designed.

**D3 — DELIVERED.** Threshold table above; minimal cutoff for 2σ C_V
separation: P_max ≈ 2⁸ (vs N2), ≈ 2¹² (vs N3); hard-core mass test separates
at P_max = 2¹⁶ with 34σ (lower-threshold scan is a P4 extension).

**Null-overlap cross-check (P4).** The deterministic smooth null N1 is judged
against BOTH stochastic nulls' self-distributions (Bose): z_N1-vs-N2 =
5.04 / 26.32 / 86.83 and z_N1-vs-N3 = −0.31 / 4.04 / 21.12 at P_max =
2⁸ / 2¹² / 2¹⁶. At the smallest cutoff the three null families overlap (shared
mean density), as they must; separation grows with P_max. Reporting rule:
every N1 significance is stated against both stochastic families.

## 7. Reproducibility

Seed 20260829 everywhere; zeros cached in
`artifacts/verification/riemann-zeros-3000.npy` (recomputed from the
Riemann–Siegel Z-function when absent); scripts run from the repo root;
outputs are the JSON files in `artifacts/verification/`.
