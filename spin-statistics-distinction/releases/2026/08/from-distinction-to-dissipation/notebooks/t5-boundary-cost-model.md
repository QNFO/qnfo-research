# T5 Notebook — Boundary-Cost Model: What Does a Boundary Cost? (FQ1)

**WBS:** QNFO.RES.009.P9.T3 · **Date:** 2026-08-14 · **Status:** EXECUTED (H1/H2/H3 PASS)
**Pre-registration:** REG-009-002 (see RESEARCH-CONTINUITY-REGISTRY.md §4)

## Hypothesis (pre-registered)

The deep-inquiry inversion (note `_26226215536`, Layer 1) claims: *drawing a boundary
creates a bit, and therefore costs free energy; hence energy is more primitive than
distinction.* Three pre-registered hypotheses sharpen this:

- **H1 (capacity bound):** with budget B and cost c per maintained distinction, the
  maximum number of simultaneously maintained distinctions is floor(B/c).
- **H2 (write/erase asymmetry):** a reversible *drawing* (writing a known value) costs
  zero; *erasing* a bit costs kT ln 2 (Landauer). The irreducible cost of a
  draw-and-erase cycle is the erasure, not the drawing.
- **H3 (grammar invariance):** a free-energy budget gates how many distinctions are
  *accessible*, never which statistics the exchange algebra allows.

## Implementation

`t5-boundary-cost-model.py` (pure Python, no external dependencies):

1. **Part A (H1).** N cells; drawing a distinction costs c against budget B. Verifies
   the saturation floor(B/c). [DEMONSTRATION — a bookkeeping consequence, not
   empirical evidence.]
2. **Part B (H2).** A one-bit system with reversible `write_known` (cost 0) and
   `erase` (cost kT ln 2, only if a bit was present). The draw+erase cycle costs
   exactly the erasure. A noisy-maintenance run (p=0.1 over 1000 steps) shows the
   boundary bleeding upkeep — the "heat engine" regime of Note 3, correctly scoped.
   [ESTABLISHED — Landauer's principle prices erasure, not writing.]
3. **Part C (H3).** The T4 exchange algebra (S₃ permutation matrices) re-run under
   budgets 0.5 and 100: Yang–Baxter and σ² = I hold identically in both; the budget
   changes only the count of affordable exchanges (0 vs 50). The eigenvalues ±1 follow
   from σ² = I alone — no budget term enters the algebra. [TOY MODEL — SYNTACTIC.]

## Results (run 2026-08-14)

| Hypothesis | Result | Evidence |
|---|---|---|
| H1 | **PASS** | maintained=3 == floor(7.0/2.0)=3 |
| H2 | **PASS** | write cost 0.0, erase cost 1.0 (kT ln2), cycle cost 1.0 |
| H2b | PASS (illustrative) | upkeep 90.0 kT ln2 over 1000 noisy steps at p=0.1 |
| H3 | **PASS** | Yang–Baxter + σ²=I hold at budget 0.5 and 100; affordable exchanges 0 vs 50 |

## Verdict on FQ1

**FQ1 is SHARPENED, not closed.** The inversion "drawing a boundary costs free energy"
is correct ONLY for erasure/maintenance, NOT for the reversible act of drawing.
Consequence for the program: **distinction (grammar) and dissipation (resource) are
dual descriptions, not competitors.** Cost bounds capacity; the exchange algebra is
untouched. The second-law-first inversion does not dethrone the mark — it prices its
upkeep. Note 3's Layer-1 Landauer conflation is demonstrated numerically.

The residual open part of FQ1 — whether the *capacity* bound has physical consequences
(e.g., a bound on sustainable distinctions of a finite system, ΔS / k_B ln 2) — is a
candidate for a future T6 (thermodynamic capacity semantics), not resolved here.

## Disconfirmation conditions (this artifact)

- If `write_known` showed a nonzero minimum cost in the reversible model, H2 fails.
  [Verified: cost 0.]
- If any budget term entered the exchange-eigenvalue computation, H3 fails.
  [Verified: eigenvalues derive from σ² = I only.]
- H1 cannot be disconfirmed (it is a definitional identity) — it is recorded as a
  demonstration only, and carries no evidential weight [KIF-60 discipline].

## Next

- FQ1 formal follow-up (candidate T6): derive the capacity bound ΔS / k_B ln 2 as a
  physical ceiling on maintained distinctions.
- FQ3 (irreversibility mapping): T5's H2 is the seed — erasure is the irreversibility
  gate; the arrow of time enters exactly where the budget does.
