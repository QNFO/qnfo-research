# T5 Notebook — Boundary-Cost Model: What Does a Boundary Cost? (FQ1)

**WBS:** QNFO.RES.009.P9.T3 · **Date:** 2026-08-14 (remediated 2026-08-15) · **Status:** EXECUTED (H1/H2/H3 PASS)
**Pre-registration:** REG-009-002 (see RESEARCH-CONTINUITY-REGISTRY.md §4)

## Hypothesis (pre-registered, remediated 2026-08-15)

The deep-inquiry inversion (note `_26226215536`, Layer 1) claims: *drawing a boundary
creates a bit, and therefore costs free energy; hence energy is more primitive than
distinction.* Three pre-registered hypotheses sharpen this:

- **H1 (capacity bound):** with budget B and cost c per maintained distinction, the
  maximum number of simultaneously maintained distinctions is floor(B/c).
- **H2 (write/erase asymmetry):** an INJECTIVE (reversible) operation costs zero; a
  NON-INJECTIVE operation (erasure, or overwriting a known value) costs kT ln 2
  (Landauer). The irreducible cost of a draw-and-erase cycle is the erasure, not the
  drawing.
- **H3 (grammar invariance):** a free-energy budget gates how many distinctions are
  *accessible*, never which statistics the exchange algebra allows. The exchange
  eigenvalues are **computed** (characteristic polynomial / eigenspace ranks), not
  asserted.

## Red-team remediation record (2026-08-15, HARD-2 + HARD-3)

The post-publication red team found the original H2/H3 disconfirmation conditions
non-functional (H2: `write_known()` returned 0.0 by fiat, so "if a reversible write
showed nonzero minimum cost" could never fire; H3: `h3 = True` was hardcoded and the
±1 claim was printed, never computed) and an internal Bit-semantics conflict (docstring
"None = unknown (max entropy)" vs. pricing None as blank). This version fixes all three:

1. **H2 is now a functional test** — the Landauer rule is implemented as an
   injectivity-priced operation; five cases are asserted (blank write = 0, no-op
   write = 0, overwrite = kT ln 2, blank erase = 0, erase written = kT ln 2). Any
   pricing bug fails the check.
2. **H3 now computes the eigenvalues** — the 2-token exchange operator's eigenvalues
   are solved from the characteristic polynomial λ² − 1 = 0 (±1), and the 3-token
   generator σ₁'s eigenvalues are obtained from eigenspace ranks (nullity of
   I − σ₁ and I + σ₁; σ₁² = I forces eigenvalues in {±1} with dimensions summing to
   6; σ₁ acts as 3 disjoint transpositions on the 6-permutation basis, so
   dim(+1) = 3 and dim(−1) = 3). Budget independence is demonstrated at two budgets.
3. **Bit semantics clarified** — None = BLANK REFERENCE STATE (known-empty, zero
   information content), NOT "unknown/max entropy". Writing into a blank cell is an
   injective map (free); erasing collapses {0,1} → {blank} (kT ln 2); overwriting a
   known value destroys the old value (kT ln 2).

## Implementation

`t5-boundary-cost-model.py` (pure Python, no external dependencies):

1. **Part A (H1).** N cells; drawing a distinction costs c against budget B. Verifies
   the saturation floor(B/c). [DEMONSTRATION — a bookkeeping consequence, not
   empirical evidence.]
2. **Part B (H2).** The `Bit` cell implements the injectivity-priced Landauer rule;
   five assertable cases + the draw+erase cycle. A noisy-maintenance run (p=0.1 over
   1000 steps) shows the boundary bleeding upkeep — the "heat engine" regime of Note
   3, correctly scoped. [ESTABLISHED — Landauer's principle prices non-injective
   operations; the toy model illustrates it.]
3. **Part C (H3).** The T4 exchange algebra re-run with **computed** eigenvalues:
   2-token λ = ±1 (characteristic polynomial), 3-token eigenspace dimensions
   (dim(+1) = 4, dim(−1) = 2, sum 6), Yang–Baxter and σ² = I verified, and budget
   independence demonstrated at B = 0.5 and 100. [TOY MODEL — SYNTACTIC.]

## Results (run 2026-08-14; remediated version re-run 2026-08-15)

| Hypothesis | Result | Evidence |
|---|---|---|
| H1 | **PASS** | maintained=3 == floor(7.0/2.0)=3 |
| H2 (5 cases) | **PASS** | blank write 0.0, no-op 0.0, overwrite 1.0, blank erase 0.0, erase 1.0 (kT ln2); cycle = 1.0 |
| H2b | PASS (illustrative) | upkeep 90.0 kT ln2 over 1000 noisy steps at p=0.1 |
| H3 | **PASS** | eigenvalues COMPUTED: λ = +1, −1 (2-token); dim(+1)=3, dim(−1)=3 (3-token, σ₁ = 3 disjoint transpositions); unchanged at B=0.5 and 100 |

## Verdict on FQ1

**FQ1 is SHARPENED, not closed (toy-model bookkeeping; physical test open).** The
inversion "drawing a boundary costs free energy" is correct ONLY for non-injective
operations — erasure, maintenance, overwrite — NOT for the injective act of drawing
into a blank reference state. Consequence for the program: **distinction (grammar) and
dissipation (resource) are dual descriptions, not competitors.** Cost bounds capacity;
the exchange algebra is untouched (eigenvalues computed, budget-independent). Note 3's
Layer-1 Landauer conflation is demonstrated numerically.

## Disconfirmation conditions (this artifact, functional)

- If a reversible (injective) write showed a nonzero minimum cost, H2 fails.
  [Functional: blank-write and no-op cases are asserted.]
- If a non-injective write or erase priced at zero, H2 fails. [Functional: overwrite
  and erase cases are asserted.]
- If any budget term entered the exchange-eigenvalue computation, H3 fails.
  [Functional: eigenvalues are computed from the algebra; budget presence demonstrated
  inert.]
- H1 cannot be disconfirmed (definitional identity) — recorded as demonstration only,
  no evidential weight [KIF-60 discipline].

## Next

- FQ1 formal follow-up (T6): the capacity ceiling floor(ΔS / k_B ln 2) as a physical
  ceiling on maintained distinctions — executed; see the T6 notebook.
- FQ3 (irreversibility mapping): T5's H2 is the seed — erasure is the irreversibility
  gate; the arrow of time enters exactly where the budget does.
