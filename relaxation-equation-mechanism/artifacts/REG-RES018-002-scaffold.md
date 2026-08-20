# REG-RES018-002 — SCAFFOLD (NOT YET SEALED) — Minimal Stochastic Extension

**Status:** DRAFT SCAFFOLD — **not sealed**. Final parameters + code must be committed with sha256 BEFORE any run (KIF-60 HARD). This document records the hypothesis space and the open parameter decisions only.

---

## 1. Motivation (from the sealed negative result)

REG-RES018-001 (commit d53ba49) DISCONFIRMED the deterministic family: max_dev = 0.5 for all 7 configurations because the outcome channel is degenerate (p_measured ∈ {0,1} — every shot of a fixed initial state follows the identical deterministic trajectory). The disconfirmation identifies the missing ingredient: **any statistical spread**. The minimal repair is a stochastic term active only during the measurement window.

## 2. Hypothesis (draft)

CC-2 (draft): a stochastic extension of the sealed family — adding an unbiased noise term to the z-coordinate during the measurement window, `dz/dt += σ·ξ(t)` with ξ(t) white noise — reproduces Born statistics within ε=1e-2 on the same 2-level test protocol, with a minimal noise magnitude σ_min that is (a) strictly positive, (b) reported as the principal result, and (c) consistent with the Wu-2013 strong-field constraint (noise off outside measurement).

## 3. Protocol (draft — inherits the sealed REG-RES018-001 protocol)

1. Same test set: 9 canonical + 50 random Bloch states.
2. Same unitary evolution to t_m.
3. Measurement window: apply the relaxation family (A/B/C as sealed) PLUS the stochastic z-term.
4. N = 1e5 shots per state (NOW genuinely needed — stochasticity makes shots non-identical; the rev.3 batch-equivalence does NOT apply).
5. Report per σ ∈ {0.001, 0.01, 0.1, 1.0}: max deviation vs ε; find σ_min = inf{σ : max_dev < ε}.
6. Verdict: PASS if σ_min exists and σ_min > 0; report σ_min.

## 4. Open decisions (to be fixed at seal time)

| Decision | Options | Note |
|:---------|:--------|:-----|
| Noise type | white (Wiener) vs colored | White first (minimal) |
| Noise coupling | additive on z vs multiplicative | Additive first |
| σ range | log-spaced 1e-3..1 | To resolve σ_min to one order of magnitude |
| σ_min definition | smallest σ in grid with PASS, then bisect | Bisection to 2 significant figures |
| RNG discipline | fixed seed per shot index | Reproducibility |

## 5. Disconfirmation conditions (draft)

- CC-2 disconfirmed if (a) no σ in range achieves max_dev < ε, OR (b) σ_min = 0 (i.e., deterministic already passes — would contradict REG-RES018-001, so impossible by construction; check anyway), OR (c) the σ_min required violates a physically meaningful bound (e.g., σ_min·τ_m comparable to the apparatus noise floor of real weak-measurement experiments — Hacohen-Gourgy & Martin 2020 constraint).

## 6. Relationship to the literature (Phase 2 anchors)

The stochastic extension is not claimed novel — it is the GRW/CSL/QSD-family mechanism (Bassi–Ghirardi 2003; Pearle 1989; Gisin–Percival/Wiseman 2016) restricted to the measurement window of the Madelung/RN formalism. The project's contribution is the **minimal-σ boundary report** in the exact sealed 2-level protocol — a quantitative anchor for "how much noise is enough" in hydrodynamic re-grounding proposals.
