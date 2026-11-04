# Universal Ignorance Audit — Beginner's Guide v1.2 core claim

Audit instrument: ZENODO-INQUIRY-1 — *The Universal Ignorance Audit*
(10.5281/zenodo.21901984) and *Knowing What We Do Not Know*
(10.5281/zenodo.21901983), applied 2026-08-20 as the Phase-0 step of the
v1.2 update cycle for 10.5281/zenodo.20391555.

## Target

The core claim pair of the guide:

1. **Negative thesis:** the standard active-QEC paradigm (surface codes on
   Euclidean lattices) faces a thermodynamic wall — a Carnot-limited
   20,000-fold cooling gap that blocks commercially useful scaling.
2. **Positive thesis:** an ultrametric alternative (Bruhat-Tits tree codes)
   achieves classically validated thresholds up to 75× higher than surface
   codes with passive fault tolerance at ~4 K, and makes three falsifiable
   predictions (E1-E3) testable for under $300,000.

Phases 1-4 record answers without resolving; Phase 5 asks the recursive
meta-question. No question may be skipped; stretching is mandatory.

---

## Phase 1 — What we know we do not know (Q1-Q3)

**Q1. What do we know we do not know about this claim?**
- Whether the classically simulated tree-code thresholds survive full quantum
  simulation (the guide's own Objection 6 / open problem 3).
- Whether any of the three falsifiable predictions (E1-E3) will be confirmed
  — none has been executed as of 2026-08-20.
- Whether the 24 W-per-logical-qubit estimate (which drives the 240 kW figure)
  is within even an order of magnitude — the guide admits 10× uncertainty in
  both directions.
- Whether the trapped-ion falsifiability register (10.5281/zenodo.22025544)
  will yield positive or negative results when executed.

**Q2. What do we not know we do not know about this claim?**
- Unknown noise channels that invalidate the tree-code assumptions
  (correlated errors violating subtree independence) in ways we have not
  modeled yet.
- Physical mechanisms that would make 4 K operation of tree codes impossible
  for reasons unrelated to the error model.
- Whether the Carnot argument has a loophole (e.g., reversible computing
  eliminating the heat load entirely) that changes the conclusion rather
  than softening it.

**Q3. What does the claim presuppose that has not been verified?**
- That the Archimedean-vs-ultrametric choice is a *physical* question
  (testable), not only a modeling choice.
- That classical simulation transfers to quantum hardware (the guide tags
  this `[GAP]`).
- That the three predictions are the right tests — they sample three
  domains, but may miss the decisive one.

## Phase 2 — What we do not know how to know (Q4-Q6)

**Q4. What is unmeasurable in principle here?**
- Nothing identified: all three predictions are operationally defined with
  kill-conditions. The residual risk is practical (noise floors), not
  principled.

**Q5. What is unmeasurable in practice now?**
- E3 (tree-topology hardware) — not funded, not built; 18-36 month timeline
  once funded.
- Full quantum simulation of the tree code beyond current classical capacity.

**Q6. What would we need to know it?**
- E1: Planck 2018 data + spectral analysis (computational only).
- E2: cloud quantum hardware noise spectroscopy (access + budget).
- E3: custom tree-topology qubit array (hardware fabrication).

## Phase 3 — What we ignore (Q7-Q9)

**Q7. What are we systematically ignoring?**
- The guide is an argued case for the author's own framework; the strongest
  counterarguments (LDPC codes, higher-T qubits, special-purpose machines)
  are engaged but not resolved in the reader's favor either way.
- The possibility that neither active QEC nor tree codes wins, and quantum
  computing remains specialized (annealers, sensors) — mentioned, not
  developed.

**Q8. What questions are we not asking?**
- What is the *marginal value* of a fault-tolerant gate-model machine if
  specialized quantum devices already deliver advantage? (The guide asserts
  utility, does not price it.)
- Who would verify E1-E3 independently, and what incentive exists?

**Q9. What contradictions are we tolerating?**
- "20,000× gap is Carnot-limited and cannot be engineered away" vs
  "higher-temperature qubits might bypass it" — both asserted; the
  resolution is platform-dependent and unresolved.
- The threshold numbers (75%/50%/17.30%) are advertised in the abstract
  with the "classical simulation only" caveat — the tension between
  headline and caveat is acknowledged but structurally invites
  misreading (mitigated by the `[PROP]` tags).

## Phase 4 — The structure of our not-knowing (Q10-Q14)

**Q10. What type of ignorance dominates?**
- Epistemic-practical: knowable-in-principle, not-yet-known (simulation
  gap, unexecuted experiments). No identified fundamental unknowability.

**Q11. Is our ignorance shrinking?**
- Yes, slowly: since v1.1 (May 2026) the program published the trapped-ion
  falsifiability register (22025544), the QEC-Darwinism tradeoff audit
  (21964674), and the prime-valuation QEC implications correction
  (21979060) — all sharpen or constrain the framework; none yet confirms
  or falsifies the core predictions.

**Q12. Where is the ignorance located — in the claim, the method, or us?**
- Method (classical-only validation), hardware (no tree-topology device),
  and partially in the claim (24 W estimate's 10× band).

**Q13. What is the shape of the boundary between known and unknown?**
- The boundary is drawn explicitly by the confidence tags: `[EST]` is the
  known side; `[PROP]`/`[GAP]`/`[SPEC]`/`[OPEN]` mark the frontier. The
  v1.2 corrections (Landauer, d=11 extrapolation, temperature ratios)
  moved three small errors from the `[EST]` side to correction.

**Q14. (Silence.)** — the audit permits a pause here; no resolution during
phases 1-4. Residual unanswered: whether the *decisive* experiment is in
the E1-E3 set at all.

## Phase 5 — The recursive question (Q15)

**Q15. What does this audit not know about itself?**
- It audits the claim, not the auditor's own selection of which numbers
  count as "key." The verification script (artifacts/verification/
  verify_guide_claims.py) is itself a claim-generator — its formulas are
  first-principles but its *coverage list* was chosen by the same author.
  Independent re-derivation of the coverage list is invited. The audit's
  own blind spot: it was produced by the author of the guide.

## Disposition

- The claim pair survives the audit with its confidence tags intact;
  no tag changes beyond the five numeric corrections verified by
  verify_guide_claims.py (35 PASS / 0 FAIL).
- Deferred to evidence: E1/E2/E3 execution; full quantum simulation.
- Standing posture: audit before asserting; the falsifier register
  (22025544) is the enforcement mechanism for the positive thesis.
