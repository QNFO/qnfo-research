# T7 Notebook — Second-Law-Gated Braid Implementation (FQ3 full-derivation candidate)

**WBS:** QNFO.RES.009.P9.T5 · **Date:** 2026-08-14 · **Status:** EXECUTED (T7-1/T7-2/T7-3 PASS)
**Pre-registration:** REG-009-004 (see RESEARCH-CONTINUITY-REGISTRY.md §4)
**Question answered:** FQ3 — where does the arrow of time enter the mark calculus?

## Hypothesis (pre-registered, sharpened in execution)

The FQ3 seed (`docs/fq3-irreversibility-mapping.md`) claims the arrow enters at the
*erasure gate*. T7 makes this quantitative by implementing braids as sequences of
maintained distinctions under a power budget:

- **T7-1 (implementability gate):** with ONE shared maintenance channel (refix at rate
  min(P,1) per step), the steady-state probability that both tokens are tracked is
  x11 = 1/(1 + 2a + 2a²), a = p/P; the pair then *persists* with conditional probability
  c = (1−p)² + 2p(1−p)·min(1,P); word success ≈ x11·c^(L−1).
- **T7-2 (capacity-limited length):** L_max(ε) = max L with x11·c^(L−1) ≥ 1−ε; grows
  monotonically with power P/p, shrinks with noise p.
- **T7-3 (the arrow is priced):** implementing the REVERSE braid pays an extra erasure
  toll (2 kT ln 2 — erasing the two tracked tokens); the implementable braid set is NOT
  inversion-closed while the algebra stays symmetric.

## The shared-reservoir Markov chain (derivation)

States (t₀,t₁) ∈ {0,1}²; decay rate p per tracked token; one shared maintenance
channel refixes one lost token per step with probability min(1,P) (from (0,0) it fixes
token 0). Stationary balance:

    11:  2p·x11 = P(x10 + x01)
    10:  p·x11 + P·x00 = (p+P)·x10
    01:  p·x11 = (p+P)·x01
    00:  p(x10 + x01) = P·x00

Solution with a = p/P: x01 = a/(1+a)·x11, x10 = a(1+2a)/(1+a)·x11, x00 = 2a²·x11,
and **x11 = 1/(1 + 2a + 2a²)**. Given both tracked, the pair stays tracked with
probability **c = (1−p)² + 2p(1−p)·min(1,P)** (no decay, or one decay saved by the
channel). Word success = x11·c^(L−1): the pair either enters a "good run" (prob x11)
or fails immediately; runs persist with c. [PROJECT — Markov chain derived for this
program; verified against simulation below.]

## Integrity records (both idealizations caught by the pre-registered tests)

1. **Independent-channel bound rejected.** The pre-registered q = min(1, P/(2p)) assumed
   dedicated maintenance per token; the first run at P/p = 2.0 predicted 1.0 and
   simulated ≈ 0.9. The shared-reservoir chain x11 = 0.400 is exact (L=1: sim 0.392).
2. **Independent-step compounding rejected.** The pre-registered x11^L understated
   persistence: L ≥ 2 simulations stayed near the L=1 value. The run-length formula
   x11·c^(L−1) is exact (P/p=2, L=4: sim 0.320 vs pred 0.303).

Both failures were caught by the pre-registered tests themselves — the pre-registration
discipline worked as designed (same pattern as T6's G2a).

## Results (run 2026-08-14)

| Check | Result | Evidence |
|---|---|---|
| T7-1 (9/9) | **PASS** | sim vs x11·c^(L−1), tol 0.10, all three power regimes |
| T7-2 monotonicity | **PASS** | L_max(0.5) = 0,0,0,3,10,238 for P/p = 1,1.5,2,4,10,20 |
| T7-2 empirical | **PASS** | Lmax(sim)=0 == Lmax(pred)=0 at r=1.5, ε=0.5 |
| T7-3 | **PASS** | inversion toll = 2.00 kT ln2 (exact) |

## Verdict on FQ3

**FQ3: SEEDED → MAPPED at toy-model level.** The implementable braid set is a function
of (p, P, T): per-exchange success x11 = 1/(1+2a+2a²); pair persistence c; L_max grows
with power, shrinks with noise; inversion pays the erasure toll (2 kT ln 2). The arrow
emerges at the ACCESS level while the algebra stays symmetric — "the second law gates
the implementable braids, it does not generate the braid algebra" is now quantitative
at toy-model level. The zero-temperature idealization is the regime where the toll
vanishes (T → 0 ⇒ kT ln 2 → 0) — confirming the FQ3 seed's identification of the
idealization gap with the erasure-cost gap.

[NOT YET EVIDENCE] The physical claim (a real topological-quantum-computing device's
implementable braid set is power-gated; anyon braid fidelity vs. cooling power) requires
experimental input. The model is a syntactic demonstration.

## Disconfirmation conditions (this artifact)

- If simulation deviates from x11·c^(L−1) beyond tolerance, T7-1 fails. [Verified: 9/9.]
- If L_max were non-monotonic in P/p, or the empirical Lmax deviated > 1 from the
  prediction, T7-2 fails. [Verified: both hold.]
- If the inversion toll ≠ 2 kT ln 2, T7-3 fails. [Verified: 2.00 exactly.]

## Next

- **P7 (registry):** publication decision for the T4–T7 toy-model suite (companion essay
  + four notebooks): separate Zenodo deposit vs. attach to v1.1.
- External scrutiny candidate: the x11/c run-length structure as a falsifiable
  experimental prediction (braid fidelity vs. cooling power in anyon systems) —
  [NOT YET EVIDENCE], pre-registered as a future prediction if pursued.
