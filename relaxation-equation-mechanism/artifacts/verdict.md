# VERDICT — QNFO.RES.018 Phase 4b (pre-registered simulation run)

**Date:** 2026-08-20 · **Sealed harness:** rev.3, sha256 `b472d0392f8915d171172623a2583e5aeb23ef776884df73a451727a3bf39dd8` (commit 5239468, origin-verified)
**Run evidence:** `artifacts/verdict-input.json` (85,537 B) — produced by the sealed harness, self-verifying its own seal hash (match=True)

---

## 1. Verdict: CC-1 DISCONFIRMED (all variants FAIL)

| Configuration | max deviation | ε | PASS |
|:--------------|:--------------|:--|:-----|
| A (γ·τ = 0.5) | 0.500000 | 1e-2 | **FALSE** |
| A (γ·τ = 5.0) | 0.500000 | 1e-2 | **FALSE** |
| A (γ·τ = 50.0) | 0.500000 | 1e-2 | **FALSE** |
| B (α = 0.01) | 0.500000 | 1e-2 | **FALSE** |
| B (α = 0.1) | 0.500000 | 1e-2 | **FALSE** |
| B (α = 1.0) | 0.500000 | 1e-2 | **FALSE** |
| C | 0.500000 | 1e-2 | **FALSE** |

**Disconfirmation condition (a) triggered:** no variant achieves max-deviation < ε over the sealed 59-state test set.

## 2. Finding (mechanism-level)

Within the sealed deterministic family — measurement-triggered relaxation toward eigenstate basins, fixed initial state, deterministic terminal rule — **the outcome channel is degenerate**: p_measured ∈ {0.0, 1.0} for every state (verified across all 7 configurations, 59 states each). Fractional Born probabilities cannot arise because every shot of a given initial state follows the identical deterministic trajectory; there is no ensemble, no stochasticity, and no contextual splitting available in the dynamics. The maximum deviation (0.5) occurs at the equator (p_Born = 0.5 → deterministic outcome 0 or 1); polar eigenstates pass trivially (p_Born ∈ {0,1}); mixed states deviate between 0.08 and 0.47.

**Interpretation:** a deterministic relaxation dynamics of the specified class cannot reproduce Born statistics. Reproducing the Born rule requires at least one of:
1. **An ensemble over initial states** (Bohmian/Vaientini-type quantum equilibrium — the competitor program identified in Phase 2, distinct from CC-1's cell);
2. **Stochasticity in the dynamics** (GRW/CSL/QSD family — the stochastic constraint set);
3. **Measurement-contextual hidden variables** (Aerts' hidden-measurement solution).

This matches the UIA Q15 fallback line exactly: **the minimal stochastic extension becomes the next research target**, and the deterministic mechanism gap in the hydrodynamic re-grounding (RES.016 objection 2) is now demonstrated — not just conceded — to be unclosable within the deterministic family tested.

## 3. BP-gate evidence (Phase 5 numeric gates applied to the verdict)

| Gate | Evidence |
|:-----|:---------|
| **BP-1 Fit-Verify** | Independent recompute (analysis script): p_measured ∈ {0,1} confirmed analytically (deterministic threshold); deviations recomputed from raw verdict-input.json — max 0.500000 reproduced. Discrepancy 0. |
| **BP-2 Terminology** | measurement-triggered relaxation, basins of attraction, Born rule, eigenbasis threshold — standard usage, no mismatches. |
| **BP-3 Density** | Not applicable (no dense-set approximation claim). |
| **BP-4 Cross-paper consistency** | ε=1e-2, N=1e5, γ/τ ranges, α ranges all match the sealed ledger (REG-RES018-001). |
| **BP-5 Overdetermined** | 2–3 free params vs 1 constraint — flagged in the ledger; verdict is FAIL independent of parameter choice (max_dev = 0.5 for ALL configurations), so no overfitting risk to the verdict. |
| **BP-6 Derived-quantity recompute** | p_Born = (1+z0)/2 recomputed in the analysis script — matches ledger formula exactly. |
| **BP-7 Sigma propagation** | Deterministic outcomes: per-shot σ not applicable; the relevant statistic is deviation vs ε, computed exactly (no sampling error — full determinism). |
| **BP-8 Numerology** | Not applicable. |
| **BP-9 Audit-the-auditor** | The analysis script is the independent recompute of the raw output file. |
| **BP-10 Independent recompute** | Performed — deviations recomputed from verdict-input.json, max 0.5 confirmed across all 7 configurations. |

**All numeric gates PASS (the verdict is a robust FAIL).**

## 4. Registry of the negative result

- **Outcome:** CC-1 disconfirmed as formulated (deterministic, fixed-initial-state relaxation cannot reproduce Born statistics within ε=1e-2).
- **Status:** legitimate negative result per the pre-registration — disconfirmation condition (a) triggered as designed.
- **Next:** UIA Q15 fallback line — minimal stochastic extension (adds an ensemble or stochastic term) → new pre-registration (REG-RES018-002) → new sealed harness → new run.
