# Correlated-Error Benchmark Specification

**Pre-registered measurement protocol for the error-structure bet.**
Companion to `industry-brief-2026-08-20.md` and the v1.4 register
(DOI 10.5281/zenodo.22025544). Version 1.0 — 2026-08-20.
Status: pre-registration (decision rules fixed before data collection).

---

## 1. Objective

Determine whether the error structure of real quantum hardware at scale is
dominated by **independent** or **correlated** components, to a pre-registered
statistical standard. The result decides the relevance of the 55× independent-error
threshold comparison: if correlated structure dominates, the comparison is moot for
the regimes that matter.

## 2. Scope

- **Targets:** any ≥50-qubit device (trapped-ion, superconducting, neutral-atom) with
  mid-circuit measurement and calibration access; open to any vendor willing to run a
  pre-registered protocol.
- **Exclusions:** simulation-only claims; vendor internal benchmarks not released with
  the raw protocol logs; anything not reproducible from the published runbook.

## 3. Observables (all from repeated randomized circuits + interleaved calibration)

1. **Pairwise error-correlation function** C(i,j) = P(err_i ∧ err_j) − P(err_i)P(err_j)
   over qubit pairs at physical distance d(i,j) — measured via randomized
   single-qubit benchmarking on pairs (two-qubit RB variants where available).
2. **Spatiotemporal clustering:** distribution of error-event sizes per shot
   (multi-qubit simultaneous errors); burst statistics per unit time.
3. **Non-Markovian memory:** autocorrelation of gate-error rates across repeated
   identical circuits (lag 1..k); spectral density of noise (1/f vs white).
4. **Event-burst population:** rate of cosmic-ray-like multi-qubit events (correlated
   errors across non-interacting qubits); compare with detector-side coincidence
   expectation.
5. **Crosstalk term:** conditional error probability P(err_j | gate on i) vs baseline.
6. **Leakage/reset correlations:** post-measurement state-preparation fidelity drift.

## 4. Metrics

| Metric | Definition | Scale |
|:-------|:-----------|:------|
| ξ (correlation length) | distance at which C(i,j) decays to 1/e of C(i,i+1) | qubit distance units |
| κ (clustering ratio) | fraction of shots with ≥2 simultaneous errors / fraction expected under independence | unitless |
| M (Markovianity violation) | normalized lag-1 autocorrelation of error rates (0 = memoryless) | [0,1] |
| λ_burst | burst event rate per hour (≥3 correlated errors in one shot) | hr⁻¹ |
| p_cond | max over j of P(err_j | gate on i) − P(err_j) | unitless |

## 5. Pre-registered decision rules

Run at minimum 3 device generations/sizes (e.g., 50, 100, 200+ qubits) with ≥10⁴
shots per circuit family.

- **KILL-ULTRAMETRIC:** ξ < 2 qubit distances AND κ within 2σ of the independent
  expectation AND M < 0.05 at all sizes → the independent-error comparison is the
  operative one; the ultrametric qudit path (55× worse threshold) is **not worth
  pursuing**; result published as a null for the program.
- **ENGAGE:** ξ ≥ 4 qubit distances at the largest size OR κ ≥ 2× independent
  expectation OR M ≥ 0.2 → correlated structure is material; the threshold
  comparison must be recomputed under the measured model; ultrametric/hierarchical
  code families earn a threshold-under-measured-noise calculation.
- **INCONCLUSIVE:** anything between → repeat at larger size; the protocol is
  designed so the middle is expensive to stay in.

## 6. Deliverables (open, regardless of outcome)

1. Raw protocol logs + shot data (public bucket, DOI-assigned).
2. The five metrics computed per size, with uncertainty.
3. A one-page verdict citing the decision rules (no post-hoc reframing;
   rule 1's kill is binding on the program).
4. If ENGAGE: the ultrametric-code threshold under the measured noise model
   (computed via the deposited simulation kit, R3) — the missing number that
   decides the 55× question fairly.

## 7. Pre-registration anchors

- Protocol frozen at this revision; changes require a new version, published as such.
- Kill rule (5.1) is binding: the program has already published its own nulls
  (CMB 10.5281/zenodo.21902891; FMO anti-ultrametric 10.5281/zenodo.21651892) and
  will publish this one the same way.
- Any team adopting this protocol may fork it; forked versions must rename decision
  rules (the kill rule is not transferable to another program's claims).

## 8. Relationship to the register

- This spec operationalizes the industry brief's central ask and supplies the
  measurement that Artifacts 4–5 (energy audit, QEC-Darwinism constraint checker)
  consume.
- It does **not** require accepting any ultrametric claim: the correlation metrics
  are theory-neutral; the decision rules are the only theory-dependent part, and they
  are symmetric (rule 1 can kill the program).
