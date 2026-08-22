# VERDICT — REG-RES018-002 (minimal stochastic extension)

Sealed harness sha256: `b3627c65975f6101f7f1e3fe1b0ee8d3d22fbebd24863316b32fa876328aae51`

## 1. Per-config result

| Config | σ_min (PASS) | best grid σ | min max_dev | verdict |
|:-------|:-------------|:------------|:------------|:--------|
| A_gamma_tau_0.5 | — | 0.708 | 0.0789 | FAIL |
| A_gamma_tau_5.0 | — | 0.708 | 0.0789 | FAIL |
| A_gamma_tau_50.0 | — | 0.708 | 0.0789 | FAIL |
| B_gamma_tau_5.0_alpha_0.01 | — | 0.708 | 0.0789 | FAIL |
| B_gamma_tau_5.0_alpha_0.1 | — | 0.708 | 0.0789 | FAIL |
| B_gamma_tau_5.0_alpha_1.0 | — | 0.501 | 0.0742 | FAIL |
| C | — | 1 | 0.1864 | FAIL |

## 2. Verdict

**CC-2: DISCONFIRMED** — condition (a): no σ in the grid achieves max deviation < ε for any config. The deterministic degeneracy of REG-RES018-001 (max_dev = 0.5, outcome channel degenerate) therefore does NOT have a minimal white-noise repair within the sealed family: a single global σ cannot simultaneously smear the near-equator states (Born ≈ 0.5) and preserve the near-pole states (Born ≈ 1) to within 1e-2. The evidence is the deviation table in §3.

Interpretation: the missing ingredient is not an unbiased global noise floor but a state-dependent (Born-correlated) mechanism — i.e., the extension family must abandon the 'unbiased white noise' minimality assumption. This is a quantitative anchor for 'how much noise is enough': the answer, within this family, is 'no amount'. Future extensions (colored noise, state-dependent multiplicative noise, measurement-backaction terms) would require new pre-registrations.

## 3. Deviation table (min max_dev per config, σ grid)

| Config | max_dev @ σ=1e-3 | @ 3.2e-3 | @ 1e-2 | @ 3.2e-2 | @ 1e-1 | @ 3.2e-1 | @ 1 |
|:-------|:-----------------|:---------|:-------|:---------|:-------|:---------|:-----|
| A_gamma_tau_0.5 | 0.477 | 0.477 | 0.477 | 0.454 | 0.388 | 0.173 | 0.159 |
| A_gamma_tau_5.0 | 0.477 | 0.477 | 0.477 | 0.454 | 0.388 | 0.173 | 0.159 |
| A_gamma_tau_50.0 | 0.477 | 0.477 | 0.477 | 0.454 | 0.388 | 0.173 | 0.159 |
| B_gamma_tau_5.0_alpha_0.01 | 0.477 | 0.477 | 0.477 | 0.454 | 0.388 | 0.172 | 0.159 |
| B_gamma_tau_5.0_alpha_0.1 | 0.477 | 0.477 | 0.477 | 0.454 | 0.387 | 0.171 | 0.159 |
| B_gamma_tau_5.0_alpha_1.0 | 0.477 | 0.477 | 0.477 | 0.450 | 0.380 | 0.157 | 0.159 |
| C | 0.477 | 0.477 | 0.477 | 0.477 | 0.459 | 0.364 | 0.186 |

## 4. Monte Carlo validation

Configs × states validated: 42 · max |P_MC − P_analytic| = 0.00143 (tolerance 5e-3) · **PASS**

All analytic probabilities are thereby implementation-validated against independent shot noise.

## 5. Project consequences

- REG-RES018-001 (deterministic): DISCONFIRMED (sealed, published 10.5281/zenodo.22026562).
- REG-RES018-002 (minimal stochastic): verdict above. The next registration (if any) targets a non-minimal mechanism — colored/state-dependent noise — or closes FQ1 as falsified at the minimal-extension level.
- Registry + continuity-registry + memory updated at closeout.
