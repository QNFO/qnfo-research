# T7 Notebook — Second-Law-Gated Braid Implementation (FQ3 full-derivation candidate)

**WBS:** QNFO.RES.009.P9.T5 · **Date:** 2026-08-14 · **Status:** EXECUTED (T7-1/T7-2/T7-3 PASS)
**Pre-registration:** REG-009-004 (see RESEARCH-CONTINUITY-REGISTRY.md §4)
**Question answered:** FQ3 — where does the arrow of time enter the mark calculus?

## Hypothesis (pre-registered, sharpened in execution)

The FQ3 seed (`docs/fq3-irreversibility-mapping.md`) claims the arrow enters at the
*erasure gate*. T7 makes this quantitative by implementing braids as sequences of
maintained distinctions under a power budget:

- **T7-1 (implementability gate):** with ONE shared maintenance channel, the
  steady-state probability that both tokens are tracked is the exact discrete-chain
  value x11 (below); the pair then *persists* with conditional probability
  c = (1−p)² + 2p(1−p)·min(1,P); word success ≈ x11·c^(L−1).
- **T7-2 (capacity-limited length):** L_max(ε) = max L with x11·c^(L−1) ≥ 1−ε; grows
  monotonically with power P/p, shrinks with noise p.
- **T7-3 (the arrow is priced):** implementing the REVERSE braid pays an extra erasure
  toll (2 kT ln 2 — erasing the two tracked tokens); the implementable braid set is NOT
  inversion-closed while the algebra stays symmetric.

## The exact discrete-time Markov chain (derivation)

States (t₀,t₁) ∈ {0,1}²; one step = decay pass + refix pass. Decay: each tracked token
loses tracking with probability p. Refix: a single shared channel refixes one lost token
with probability q = min(1,P) per step (from (0,0) it fixes token 0 first — matching the
implementation). Transitions:

    (1,1) -> (1,1): (1-p)^2 + 2p(1-p)q     (1,1) -> (1,0): p(1-p)(1-q) + p^2 q
    (1,1) -> (0,1): p(1-p)(1-q)            (1,1) -> (0,0): p^2 (1-q)
    (1,0) -> (1,1): (1-p)q                 (1,0) -> (1,0): (1-p)(1-q) + p q
    (1,0) -> (0,0): p(1-q)                 (0,1) -> (1,1): (1-p)q
    (0,1) -> (1,0): p q                    (0,1) -> (0,1): (1-p)(1-q)
    (0,1) -> (0,0): p(1-q)                 (0,0) -> (1,0): q
    (0,0) -> (0,0): 1-q

Stationary solution relative to x11 (balance equations solved in the model code):

    x01 = p(1-p)(1-q) / [1 - (1-p)(1-q)]
    x10 + x01 = [2p(1-p)(1-q) + p^2] / [(1-p) q]
    x00 = p(1-q)/q * (p + (x10+x01)/x11)
    x11 = 1 / (1 + x01 + x10 + x00)

The persistence factor is exact: c = (1−p)² + 2p(1−p)·q = P(both tracked next step |
both tracked now) — no decay, or one same-step decay saved by the channel. Word success
= x11·c^(L−1): the pair either enters a "good run" (prob x11) or fails immediately; runs
persist with c. [PROJECT — Markov chain derived for this program; verified against
simulation below, 15/15 tightness checks within 2.5σ.]

## Integrity records (three idealizations, each caught by the pre-registered tests)

1. **Independent-channel bound rejected.** The pre-registered q = min(1, P/(2p)) assumed
   dedicated maintenance per token; first run at P/p = 2.0 predicted 1.0, simulated ≈ 0.9.
2. **Independent-step compounding rejected.** The pre-registered x11^L understated
   persistence: L ≥ 2 simulations stayed near the L=1 value. The run-length formula
   x11·c^(L−1) is exact.
3. **Rate-equation approximation rejected.** The mid-execution analytic x11 = 1/(1+2a+2a²),
   a = p/P, is NOT the exact stationary value: it treats decay and refix as independent
   rate processes and misses that a same-step decay of one token can be saved by the
   channel (from (1,1), the effective outflow is 2p(1−p)(1−q) + p², not 2p). A 2000-trial
   tightness re-run showed consistent +2.9..+5.0σ deviations across five seeds (e.g.,
   P/p=4: sim 0.656-0.670 vs approximation 0.615). The exact discrete-chain solution
   above reproduces the simulation within ±2.5σ on all 15 seed/regime checks (z range
   −1.62..+1.11). The committed model uses the exact chain.

## Results (run 2026-08-14; exact-chain version)

| Check | Result | Evidence |
|---|---|---|
| T7-1 (9/9) | **PASS** | sim vs x11·c^(L−1), tol 0.10, three power regimes |
| T7-2 monotonicity | **PASS** | L_max(0.5) = 0,0,0,4,12,276 for P/p = 1,1.5,2,4,10,20 |
| T7-2 empirical | **PASS** | Lmax(sim)=0 == Lmax(pred)=0 at r=1.5, ε=0.5 |
| T7-3 | **PASS** | inversion toll = 2.00 kT ln2 (exact) |
| Tightness | **PASS** | 15/15 checks |z| ≤ 2.5 (2000 trials, 5 seeds × 3 regimes) |

## Verdict on FQ3

**FQ3: SEEDED → MAPPED at toy-model level.** The implementable braid set is a function
of (p, P, T): per-exchange success x11 (exact discrete-chain stationary value); pair
persistence c; L_max grows with power, shrinks with noise; inversion pays the erasure
toll (2 kT ln 2). The arrow emerges at the ACCESS level while the algebra stays
symmetric — "the second law gates the implementable braids, it does not generate the
braid algebra" is now quantitative at toy-model level. The zero-temperature idealization
is the regime where the toll vanishes (T → 0 ⇒ kT ln 2 → 0) — confirming the FQ3 seed's
identification of the idealization gap with the erasure-cost gap.

[NOT YET EVIDENCE] The physical claim (a real topological-quantum-computing device's
implementable braid set is power-gated; anyon braid fidelity vs. cooling power) requires
experimental input. The model is a syntactic demonstration.

## Disconfirmation conditions (this artifact)

- If simulation deviates from x11·c^(L−1) beyond tolerance, T7-1 fails. [Verified: 9/9;
  tightness 15/15 within 2.5σ.]
- If L_max were non-monotonic in P/p, or the empirical Lmax deviated > 1 from the
  prediction, T7-2 fails. [Verified: both hold.]
- If the inversion toll ≠ 2 kT ln 2, T7-3 fails. [Verified: 2.00 exactly.]

## Next

- **P7 (registry):** publication decision for the T4–T7 toy-model suite (companion essay
  + four notebooks): separate Zenodo deposit vs. attach to v1.1.
- External scrutiny candidate: the x11/c run-length structure as a falsifiable
  experimental prediction (braid fidelity vs. cooling power in anyon systems) —
  [NOT YET EVIDENCE], pre-registered as a future prediction if pursued.
