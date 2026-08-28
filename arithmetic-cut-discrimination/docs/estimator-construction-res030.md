# Estimator Construction — QNFO.RES.030 P2 (SPECTRAL-ESTIMATOR-CONSTRUCTION-1 gate artifact)

Date: 2026-08-29. This document is the DESIGN CONTRACT for the P3 verification
suite. Every quantitative statement below is implemented in
`artifacts/verification/` and reproduced by the deposited scripts; no number
may enter the paper except from executed output (VERIFY-IN-CODE-1).

## 1. The six canonical construction rules and their resolutions

- **B1 — pair correlation via k-th-neighbor decomposition, per-order
  normalization; NOT the spacing distribution.** R₂(s) = Σ_{k=1}^{kmax} p_k(s)
  where p_k is the histogram of u_{i+k}−u_i normalized to sum 1 per order k.
  The nearest-neighbor spacing distribution alone is a different object
  (it equals p₁) and must never be reported as the pair correlation.
- **B2 — exact Li unfolding via scipy.special.expi(log x).** For the prime
  levels {ln p}, the smooth staircase is li(x)=Ei(ln x); the asymptotic
  series diverges for small arguments, so only the exact special function is
  used. For Riemann zeros, the smooth count is the Riemann–von Mangoldt
  formula N̄(t) = (t/2π)(log(t/2π)−1) + 7/8 (exact smooth count, no zeros of
  ζ needed).
- **B3 — full Dyson number-variance formula; never rank-unfold.**
  Σ²_GUE(L) = (1/π²)[log(2πL) + 1 + γ − π²/8]; Poisson: Σ² = L. Empirical
  Σ² is the variance of level counts in disjoint windows of length L over the
  unfolded sequence. Rank unfolding (sort order as unfolded position) is a
  tautology and is never used; only smoothed-staircase unfolding.
- **B4 — Montgomery–Odlyzko on Riemann ZEROS; primes = Gallagher Poisson +
  twin-gap hard core.** The GUE pair correlation is validated on the first
  3000 zeros (via mpmath zetazero). For the primes, the expected class is
  Poisson-like beyond the hard core, with the first spacing bin EXACTLY zero:
  the minimum unfolded spacing is 2/ln P_max (minimum prime gap 2), so no
  spacing below it exists — this is reported as a hard-core check, not a
  discovery.
- **B5 — single-realization form factor is report-only at fixed τ.** K(τ) is
  non-self-averaging (K/N fluctuates O(1)); a single realization is reported
  at fixed τ with no universality claim. The ramp/plateau comparison needs
  ensemble or τ-window averaging; RES.030 reports single-realization values
  only, and uses K(τ) solely inside the planted-signal positive control
  (D-3), where the planted peak is deterministic.
- **B6 — statistical nulls at matched (N, unfolding, binning, window).**
  Every comparison cut-vs-null runs at the same effective N, the same smooth
  staircase, the same bins, and the same window; otherwise a spacing artifact
  is mistaken for arithmetic content (seed-cluster verdict 11209).

## 2. Amendments A1–A8 mapped to design rules

- **A1 → D-1 (BLOCKING):** recompute the Dyson number-variance table for the
  first 3000 zeros at L ∈ {5, 10, 15, 20, 25, 30, 50, 100, 500, 1000, 2000,
  3400} with exact RVM unfolding and stated window counts; resolve the
  published 1.044-vs-0.525 gap (0.525 = Dyson at L≈20; the measured value at
  each L is compared to the formula AT THAT SAME L — no window mismatch).
- **A2 → D-2:** true GUE Monte Carlo nulls (Hermitian Gaussian ensemble,
  semicircle unfolding), never a GOE stand-in; validated against the analytic
  GUE curve; used for estimator validation and as the ensemble null for the
  two-point observables.
- **A3 → D-3:** positive control — a planted log-periodic modulation
  (density ∝ 1+ε·cos(2π·ln y/ln λ)) must produce a form-factor peak at
  τ* = 1/ln λ; the pipeline must recover it.
- **A4 → D-4:** the Bost–Connes observable is computed at finite P_max only,
  and reported as a crossover: peak location and width vs P_max, with the
  pole amplitude β²/(β−1)² recovered as the P_max→∞ limit (312.1 at β=1.06).
  No pole language for any finite object.
- **A5 (desymmetrization):** applies to real molecular spectra only; recorded
  as a P5 protocol requirement for the real-data application, not exercised
  on the cut itself.
- **A6 (computed-level caveat):** P5 protocol requirement for ExoMol data.
- **A7: CLOSED 2026-08-29** — POKAZATEL counts verified against the primary
  literature (810,269 states / 5,745,071,340 transitions, MNRAS 480:2597
  (2018); MARVELised .states.bz2 ≈ 6.3 MB). The seed note's "~4.7 M levels /
  12.7 MB" is false; any reuse must carry the corrected counts (evidence:
  UMP.014 red-team gates, session Fgxo-Bv4D7kU5BywLA2U6).
- **A8 (unification-thread exclusion):** RES.030 carries no claim about the
  label/numeric ontology; the two-layer formalism belongs to the future
  SLB/INM record (see dual red-team adjudication §8).

## 3. Thermodynamic formulas (exact, closed form)

Prime modes p ≤ P_max, energies ε_p = ln p, β = 1/k_BT:

- Bose (unrestricted): ln Z_B = −Σ_p ln(1−p^{−β});
  C_V^B = β² Σ_p (ln p)² p^{−β}/(1−p^{−β})².
- Fermi (squarefree): ln Z_F = Σ_p ln(1+p^{−β});
  C_V^F = β² Σ_p (ln p)² p^{−β}/(1+p^{−β})².
- Maxwell–Boltzmann: ln Z_MB = Σ_p p^{−β} = P(β) (the PRIME ZETA function);
  C_V^MB = β² Σ_p (ln p)² p^{−β}.
  (Correction to the provenance chats: "ln Z_MB → Li(e^{−β}) via the PNT" is
  false — Li of an argument in (0,1) is meaningless; the sum is P(β), with
  logarithmic singularity ~ −ln(β−1) near β=1 by Mertens. Verified numerically
  at P3 against the known value P(3/2) ≈ 0.45224742.)

Limits (exact):
- High T (β→0): C_V^B → π(P_max)·k_B (equipartition per mode; the chats'
  "→ P_max" is corrected to the prime count), C_V^F → 0 (Schottky decay),
  C_V^MB → 0.
- Low T (β→∞): all three collapse to β²(ln 2)² 2^{−β} (first-mode freeze-out).
- Bost–Connes pole amplitude: C_V^B ≈ β²/(β−1)² as β→1⁺, P_max→∞;
  312.1 at β = 1.06. Finite-P_max value reported at stated P_max (D-4).

Ideal-gas baseline for the published deviation claim: C_V^ideal = π(P_max)·k_B
flat; relative deviation D(β) = (C_V^ideal − C_V^cut)/C_V^ideal. The published
"up to roughly three quarters at low temperature" is reproduced as the
crossing set {β : D(β) ∈ [0.70, 0.80]}, with the note that D→1 as β→∞
(full freeze-out) — the claim is window-dependent and is reported with its
window (reviewer N1/N2 findings folded in).

## 4. Matched-density null ensembles (the new null class)

For P_max with N = π(P_max) and range [ln 2, ln P_max]:

- **N1 (smooth log-spaced):** ε_j = ln 2 + j·(ln P_max − ln 2)/(N−1),
  j = 0..N−1. Deterministic; the fluctuation-free comparator.
- **N2 (fixed-count random-in-log):** N i.i.d. uniform points on
  [ln 2, ln P_max], sorted; M seeded realizations. Matched count and range;
  no arithmetic structure.
- **N3 (Poisson-on-log-scale):** count ~ Poisson(rate·width) with
  rate = N/(ln P_max − ln 2), positions uniform; M seeded realizations.
  Matched MEAN density with count fluctuations.

Fairness (B6/A2): every null is realized under the SAME statistics as the cut
(option-B mode view): for statistics s ∈ {B, F, MB} and a null level set
{ε_j}, C_V^s_null(β) = β² Σ_j ε_j² e^{−βε_j}/(1 ∓ e^{−βε_j})^{∓2} per the
closed forms above with the level set playing the role of the modes. The
two-point observables use the same li-smooth unfolding for cut and nulls.

## 5. Discrimination statistics (D1/D2/D3 contract)

- Observable curves: C_V(β) on a fixed β-grid (log-spaced, [0.02, 12], 100
  points) and R₂(s) on a fixed s-grid ([0, 4], 240 bins).
- Distance: relative L2, d(a,b) = sqrt( mean_β ((C_a − C_b)/N)² ) for C_V,
  and the analogous mean-square over bins for R₂.
- Null self-distance distribution: d_self = {d(null_i, null_j): 1≤i<j≤M},
  M = 30; mean_self, σ_self. Cut distance: d_cut = mean over realizations
  of d(cut, null_i).
- Separation: z = (d_cut − mean_self)/σ_self; 2σ separation ⇔ z ≥ 2.
- Sweep: P_max ∈ {2⁸, 2¹², 2¹⁶} × statistics {B, F, MB} × nulls {N1, N2, N3}
  → the D3 threshold table.
- D1 verdict: at least one observable separates at ≥2σ beyond a computable
  P_max. D2 verdict: at the largest P_max, does two-point separation persist
  where C_V separation fails? Reported per statistics per null.
- The hard-core signature: s_min(cut) = 2/ln P_max > 0 (first bin exactly
  zero) vs s_min(nulls) → 0 — reported as the structural discriminator in the
  two-point channel.

## 6. Reproducibility contract

Python 3.12.10; NumPy 2.4.4; SciPy 1.17.1; mpmath 1.3.0 (Riemann zeros).
Seed 20260829 everywhere. Outputs written to `artifacts/verification/`
(JSON + text) and read back before any number enters a document. Scripts run
from the REPO ROOT (guardrail inherited from the RES.023 precedent).
