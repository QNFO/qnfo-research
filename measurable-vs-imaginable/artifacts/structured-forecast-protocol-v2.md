# Phase 4 — Structured Forecast Protocol v2.27 (Scope-Scaled)
## measurable-vs-imaginable

**Date:** 2026-07-31 | **Status:** Phase 4 COMPLETE (lightweight — single investigation)
**Scope note:** This is a boundary-drawing investigation (what distinguishes physically measurable from mathematically imaginable), not a paradigm forecast. Scope-scaled: assumptions, one calibration prediction, light Stages 9-10.

---

## 1. Core Claim

There exists a principled boundary between physically measurable quantities and mathematically imaginable ones. The boundary is NOT the classical quantum-classical divide but the computability boundary: measurable quantities are those for which a finite Turing-machine protocol exists that approximates the quantity with a computable modulus of convergence. Non-computable reals, uncomputable functions, and undecidable properties are mathematically well-defined but physically inaccessible — they are IMAGINABLE but not MEASURABLE. This is the Ontological Closure (OC) criterion applied as a measurement filter.

## 2. Enabling Assumptions

| # | Assumption | Confidence | Risk if False |
|:--|:-----------|:-----------|:--------------|
| A1 | The Church-Turing thesis holds for physical computation (no physical process computes non-Turing-computable functions) | HIGH [established] | OC boundary collapses — hypercomputation would make "non-computable" measurable |
| A2 | Measurement is operationally defined as "finite protocol with computable error bound" — this definition captures all physically meaningful measurements | HIGH [mainstream interpretation] | OC boundary may exclude measurement protocols that are physically valid but not Turing-machine-describable (e.g., analog quantum simulation with continuous parameters) |
| A3 | The distinction between measurable and imaginable is USEFUL — it prunes theory-space and guides experimental design, not just a philosophical refinement | MODERATE [speculative] | If the boundary has no practical consequence (no experiment distinguishes two theories that differ only in non-computable parameters), then the boundary is philosophically interesting but scientifically inert |
| A4 | Non-computable reals are genuinely inaccessible to any finite physical protocol | HIGH [mainstream interpretation] | A counterexample would be Nobel-worthy — but no candidate protocol has been proposed |

## 3. Qualitative Ranking of Implications

| Rank | Implication | Assessment | Confidence |
|:----:|:------------|:-----------|:-----------|
| 1 | **Theory-space reduction:** Any physical theory whose predictions depend on non-computable parameters is [UNFALSIFIABLE-DEPENDENCY] | Direct consequence of OC. Strong logical case. | HIGH |
| 2 | **Continuum Hypothesis irrelevance:** CH is undecidable in physics because no measurement can distinguish models with different cardinalities of ℝ — this is a PROVEN result of the OC criterion | The strongest single result of the investigation. | HIGH |
| 3 | **QFT regularization:** Standard regularization schemes (dimensional regularization, Pauli-Villars, lattice cutoff) are ways of imposing computability on a formalism that uses non-computable continuum fields — regularization is ALREADY a computability constraint, unrecognized as such | Insightful reframing of known physics. | MODERATE |
| 4 | **Experimental design guidance:** Propose that experiments should report a "computability class" — finite protocol with convergence modulus — alongside error bars | New methodological standard. | LOW [speculative] |

## 4. Judgment Sensitivity

- **Robust:** Implication 1 (theory-space reduction) and Implication 2 (CH irrelevance) hold under all perturbations
- **Conditional:** Implication 3 (QFT regularization = computability constraint) is conditional on acceptance of OC by the QFT community — substantial barrier
- **Fragile:** Implication 4 (computability class reporting) is fragile — adoption requires cultural change in experimental physics

## 5. Calibration Register

```
[CALIBRATION-REGISTER: MV-S5-001]
Check date: 2030-12-31
Prediction: The phrase "computability class" or "computable convergence modulus"
  appears in ≥3 physics papers (arXiv: quant-ph or hep-th) as a reported
  measurement property, independently of QNFO authors.
Likelihood-Anchor: Calibrated Subjective
Strength: WEAK
Status: PENDING

[CALIBRATION-REGISTER: MV-S5-002]
Check date: 2029-12-31
Prediction: The CH-physical-inertness result is cited in ≥1 physics review
  article as a methodological constraint on theory-building.
Likelihood-Anchor: Calibrated Subjective
Strength: WEAK
Status: PENDING
```

---

## 6. Stage 9: Practical Applications Extension

| Domain | Operational Signature | Falsifiable Claim | Horizon |
|:-------|:----------------------|:------------------|:--------|
| **Metrology Standards** | National metrology institutes (NIST, PTB, NPL) add "computability class" to measurement reporting standards — alongside uncertainty and traceability. A measurement of a physical constant must specify: value, uncertainty, AND computability class (finite protocol with specified convergence modulus, or [NON-COMPUTABLE: shown to require uncomputable function]). | NIST includes computability class in ≥1 measurement standard by 2035 | 2030-2035 |
| **Theory Assessment** | Physics journals require authors to identify any non-computable parameters in their theories. A theory with non-computable parameters is not REJECTED (it may still be useful as an effective theory), but it must be labeled [NON-COMPUTABLE PARAMETER: X]. | Physical Review D or Journal of High Energy Physics introduces a "computability disclosure" in author guidelines by 2032 | 2028-2032 |
| **Philosophy of Science** | The measurable-vs-imaginable boundary becomes a standard topic in philosophy of physics curricula — replacing the older "observable vs. unobservable" distinction (van Fraassen 1980) with the more precise "computably measurable vs. mathematically imaginable" distinction. | Stanford Encyclopedia of Philosophy entry "Scientific Realism" references the computability boundary by 2030 | 2028-2030 |

---

## 7. Stage 10: Counterfactual Backcasting

### Target Disciplines

| Discipline | Current State (2026) | Target State |
|:-----------|:---------------------|:-------------|
| **Metrology** | Measurement uncertainty is the gold standard (GUM — Guide to the Expression of Uncertainty in Measurement). No concept of "computability class" exists. | Every measurement includes computability class alongside uncertainty — a "complete" measurement is (value, ±uncertainty, computability-class, convergence-modulus) |
| **Philosophy of Physics** | The realism debate centers on "observable vs. unobservable" (van Fraassen) and "structural realism" (Worrall, Ladyman). No one asks "is this quantity computable?" | Computability is the central concept in scientific realism — a theory is "real" iff its quantities are computably measurable. Structural realism becomes "computable structural realism." |

### Tier 1 Fork: Turing's 1936 Paper is Read by Physicists

**Fork:** Alan Turing's "On Computable Numbers" (1936) is immediately recognized by physicists as having implications for measurement theory. The "Turing machine" is not just a model of computation — it is a model of MEASUREMENT: a measurement is a finite sequence of operations that halts and outputs a result with a specified error bound, exactly like a Turing machine.

**Counterfactual (2026):** The quantum measurement problem is reformulated in 1936 as: "Is the measurement process Turing-computable?" The answer (yes, via decoherence theory) is worked out by the 1970s, not the 1990s. The "observable vs. unobservable" debate in philosophy of science never takes off — it is replaced immediately by "computable vs. non-computable." By 2026, every physics graduate student can state the computability class of their measurements.

**Calibration claim:** If Turing's 1936 paper had been read as a measurement-theory paper, the "measurement problem" would have been recognized as a computability-boundary problem 50 years earlier — resolved by Zurek's decoherence program (1980s) applied to a problem that was correctly formulated in 1936.

### Tier 2 Fork: Constructive Mathematics is the DEFAULT (1900s)

**Fork:** Hilbert's Program (1900) includes not just formalization of mathematics but the requirement that every existence proof in mathematics must be CONSTRUCTIVE — providing an explicit algorithm to construct the object claimed to exist. The Brouwer-Hilbert debate is resolved in favor of constructivism.

**Counterfactual (2026):** All of 20th-century mathematics is constructive. Non-constructive existence proofs (using Axiom of Choice, Zorn's Lemma) are treated as "non-constructive — existence claimed but not demonstrated." Physicists never learn classical analysis with uncountable sets — they learn constructive analysis from the start. The "measurable vs. imaginable" problem never arises because physicists are never taught that non-computable reals "exist" in any physically meaningful sense. The ban on non-constructive proofs in physics is as natural as the ban on perpetual-motion machines.

---

## 8. Recommendations

1. **Metrology engagement:** Draft a white paper for NIST/PTB on "computability class" as a measurement property. Engage through existing metrology working groups.
2. **Philosophy publication:** Submit a condensed version of the measurable-vs-imaginable argument to *Philosophy of Science* or *Studies in History and Philosophy of Modern Physics*.
3. **QFT regularization paper:** Write a separate paper on "Regularization as Computability Constraint: Why QFT Needs Cutoffs" — this reframes known physics terminology in computability language and may be more accessible to physicists than the full OC program.

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| v1.0 | 2026-07-31 | Initial scope-scaled Phase 4: assumptions, qualitative ranking, sensitivity, calibration register, light Stage 9 (3 domains), light Stage 10 (2 fork tiers) |
