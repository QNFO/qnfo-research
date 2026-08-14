# T4 Notebook — Toy Model: Statistics from Syntactic Exchange

**WBS:** QNFO.RES.009.P9.T2 · **Date:** 2026-08-14 · **Status:** EXECUTED (P1 verified)
**Pre-registration:** REG-009-001 (see RESEARCH-CONTINUITY-REGISTRY.md §4)

## Hypothesis (pre-registered, no hand-imposed sign)

A discrete syntactic model — two/three indistinguishable tokens on a lattice, with the
exchange operator as the sole primitive — reproduces (a) the braid/Yang–Baxter relation,
(b) the ±1 collapse of exchange eigenvalues in 3D semantics, and (c) a fractional phase in
2D semantics, without importing the boson/fermion sign by hand.

## Implementation

`t4-toy-model.py` (pure Python, no external dependencies):

1. **Two tokens.** The exchange operator P swaps the basis kets. The symmetric and
   antisymmetric projectors P_sym = (I+P)/2 and P_asym = (I−P)/2 are constructed *from P*.
   The notebook verifies:
   - idempotence P_sym² = P_sym and P_asym² = P_asym (this is the CallING law — the mark
     algebra's idempotence is literally the idempotence of the exchange projectors);
   - complement P_sym + P_asym = I and orthogonality P_sym·P_asym = 0;
   - the eigenvalues of P are +1 and −1 — the two statistics, *derived*, not assumed.

2. **Three tokens.** The permutation representation of S₃ is built; the braid relation
   σ₁σ₂σ₁ = σ₂σ₁σ₂ (Yang–Baxter) is verified, and the 3D involutive collapse σ₁² = I is
   confirmed as the mechanism that restricts exchange phases to ±1.

3. **Anyon mode.** The exchange is multiplied by a fractional phase η = e^{2πi/3} (s = 1/3).
   The notebook confirms η² ≠ 1 (the 2D collapse fails) and η³ = 1 (triple exchange returns
   the identity phase).

## Verdict on P1

The sign (boson vs fermion) emerges from the exchange algebra itself; no sign is
hardcoded. P1 is **confirmed** at the toy-model level. This is a *syntactic* demonstration,
not a physical derivation — the honest boundary (Lorentz/microcausality input for the
spin–statistics *connection*) remains as stated in the paper §5.

## Next

- Extend with a boundary-cost term (FQ1, Landauer) — a "draw boundary" operation that
  carries a free-energy price, to test the second-law-first inversion.
- Generalize to n tokens and verify the two 1D characters of S_n are the only ones
  available without additional postulates (P3 / T1 extension).
