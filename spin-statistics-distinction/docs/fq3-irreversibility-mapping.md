# FQ3 Irreversibility Mapping — Where Does the Arrow Enter the Mark Calculus?

**WBS:** QNFO.RES.009.P5 · **Date:** 2026-08-14 · **Status:** SEEDED (mapping complete; full
derivation deferred to candidate T7)
**Source wobble:** note `_26226215159`, Q3 (the formalism is reversible; experience is not)
and Q11 (the zero-temperature, zero-noise, zero-gravity idealization).

## 1. The wobble, restated

The braid group B_n is time-symmetric: every generator σ_i has an inverse σ_i⁻¹, and the
Yang–Baxter relation is invariant under reversal. The T4 toy model confirms the algebra
at matrix level. Physical exchange, however, is irreversible: particles decohere, braids
are torn by noise, and measurements do not undo themselves. The deep-inquiry notes
proposed the inversion "derive braids from the second law" (note `_26226215159` Q15;
note `_26226215536` verdict). The T5 result (H2) supplies the precise seed: **erasure is
the only non-invertible primitive in the boundary-cost model.**

## 2. The mapping: the arrow enters at the resource gate, not in the algebra

[PROJECT-SYNTHESIS] Three claims, each verifiable at toy-model level:

1. **The grammar is time-symmetric.** Braid generators are invertible (permutation
   matrices satisfy P·Pᵀ = I). A forward exchange run and its reverse are identical.
   [ESTABLISHED — verified by T4 code, reproduced below.]
2. **The resource account is not.** The erasure map E : {0,1} → {0} is non-injective:
   it has no inverse. Writing (drawing) is reversible; erasing is not. Every erasure
   dumps kT ln 2 into the reservoir (Landauer) [ESTABLISHED — T5 H2 verified].
3. **Therefore:** the arrow of time enters the mark calculus exactly where the
   free-energy budget does. The second law does not change which statistics are
   possible (T5 H3, T6 G3: the ±1 eigenvalues survive any budget); it changes which
   *trajectories* are implementable — a braid can be physically executed only while the
   distinctions it tracks are maintained against noise, at cost P per unit time (T6 G2:
   D* = min(N, P/p)).

**Consequence:** the candidate inversion "derive braids from the second law" is refined
to **"the second law gates the implementable braids, it does not generate the braid
algebra."** The zero-temperature idealization (Q11) is precisely the regime in which
erasure is free (T → 0 ⇒ kT ln 2 → 0): the idealization gap and the erasure-cost gap are
the same gap.

## 3. Minimal code verification

```python
# Braid generator: invertible (time-symmetric)
# P (permutation of two tokens) satisfies P @ P.T == I
# Erasure: not invertible (time-asymmetric)
# E maps {0,1} -> {0}; E(0)=E(1) => no inverse function exists
```

Run (`artifacts/notebooks/t6-capacity-bound.py` Part C + the checks below):
- permutation inverse check: PASS (P·Pᵀ = I)
- erasure non-injectivity: PASS (E(0) = E(1) = 0, two preimages — no inverse)
- forward vs reverse exchange: identical (T4 Yang–Baxter + σ²=I hold both ways)

## 4. Verdict

FQ3 status: **SEEDED.** The irreversibility wobble is mapped to the erasure gate:
grammar time-symmetric, resource account asymmetric, idealization gap = erasure-cost
gap. [NOT YET EVIDENCE] The full derivation (a dynamics in which the arrow *emerges*
from the maintenance game rather than being assumed) is the candidate **T7:
second-law-gated braid implementation** — a model in which a braid is implemented by a
sequence of maintained distinctions with a power budget, and the implementable braid
set is shown to depend on (p, P, T). Registered in RESEARCH-CONTINUITY-REGISTRY.md §6.

## 5. Disconfirmation conditions (this mapping)

- If a braid generator were shown to be non-invertible (σ_i·σ_i⁻¹ ≠ id), claim 1 fails.
  [Verified: permutation generators are involutions.]
- If erasure were shown reversible (an injective map {0,1}→{0}), claim 2 fails.
  [Impossible by counting: two preimages, one image.]
- If the ±1 eigenvalues changed under a budget constraint, claim 3 fails.
  [Verified in T5 H3 and T6 G3: eigenvalues derive from σ² = I alone.]
