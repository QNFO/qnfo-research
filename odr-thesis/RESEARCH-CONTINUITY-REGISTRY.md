# RESEARCH-CONTINUITY-REGISTRY — ODR Thesis v2.0

> **Canonical DOI:** [10.5281/zenodo.21784489](https://doi.org/10.5281/zenodo.21784489)
> **Project:** QNFO/odr-thesis | **WBS:** QNFO.UMP.001
> **Published:** 2026-08-04 | **Version:** v2.0
> **Registry Last Updated:** 2026-08-04
> **Living Document** — maintained, updated, followed up on.

---

## 1. FRONTIER RESEARCH QUESTIONS (§7.3 — "The Adelic Distinction")

*Status codes: OPEN (no active work), IN_PROGRESS (currently under investigation), SUSPENDED (blocked), ANSWERED (resolved with publication), PREREGISTERED (pre-registration locked).*

| # | Question | Status | Next Action | Pre-Reg Suitable? |
|:--|:---------|:-------|:------------|:-------------------|
| FQ1 | **Adelic Quantum Mechanics** — Can QM be reformulated as wavefunctions on the adele ring, replacing Schrödinger with an adelic harmonic condition? What replaces the Born rule as invariant measure on the idele class group? | OPEN | Derive adelic Laplacian on A_Q^×; identify invariant measure candidates | YES — formal derivation of Born rule from product formula would be preregisterable |
| FQ2 | **Product Formula as Conservation Law** — Does the product formula underlie all known conservation laws? Can Noether's theorem be recast in valuation-theoretic terms? | OPEN | Formal derivation of Noether's theorem in valuation-theoretic language; map product formula terms to conserved charges | YES — derivation of one conserved quantity from product formula |
| FQ3 | **Emergence of Spacetime from Distinction Networks** — How does connected Archimedean spacetime emerge from a purely ultrametric Cantor-set-like adelic base? Is spacetime a real-section of an adelic tensor network? | OPEN | Literature on adelic tensor networks (Gubser et al. 2017, Bhattacharyya et al. 2018); define "real-section" operation mathematically | YES — define computable metric for "degree of spacetime emergence" |
| FQ4 | **Gauge Group from Idele Class Group** — Can SM gauge group SU(3)×SU(2)×U(1) be derived as automorphism group of the idele class group's geometric structure? | OPEN | Map idele class group autmorphisms to known symmetries; check if SM gauge group is a subquotient | YES — pre-register predicted automorphism group |
| FQ5 | **Dimensionless Constants as Idele Invariants** — Is α a period of the motive of a specific adelic quotient? Can coupling constants be calculated from the moduli space of distinction patterns? | OPEN | Compute periods of adelic moduli spaces; compare to known α ~ 1/137.036 | YES — pre-register predicted α from moduli space before computing |
| FQ6 | **Laws of Form and the Origin of Number** — Can Q and the primes be generated from the iterated act of distinction? Does Spencer-Brown's primary algebra contain the seed of Ostrowski's theorem? | OPEN | Formal mapping: Spencer-Brown's cross → prime; re-entry → valuation; identify a LoF structure isomorphic to Ostrowski completions | PARTIAL — structure discovery is exploratory; isomorphism claim is preregisterable |
| FQ7 | **Quantum Logic as p-adic Logic** — Is the lattice of quantum propositions naturally isomorphic to the lattice of clopen sets in a p-adic Cantor set? Does failure of distributivity in quantum logic correspond to non-Archimedean topology's hierarchical structure? | OPEN | Map orthomodular lattice of QM to clopen-set lattice of Q_p; check distributivity violation ↔ ultrametric branching | YES — pre-register predicted lattice isomorphism |
| FQ8 | **Testable Predictions of the Adelic Universe** — What observable signatures does an adelic spacetime leave in CMB, prime-like fluctuations, or UV QFT behavior? | OPEN | Compute predicted CMB correlation structure from adelic network; look for prime-valued angular power spectrum peaks | YES — pre-register CMB prediction before Planck/CMB-S4 data release |
| FQ9 | **Tate's Thesis as a Physical Action Principle** — Can the functional equation of the zeta function be reinterpreted as the condition that the universe is invariant under an adelic version of CPT symmetry? | OPEN | Formal mapping: zeta functional equation ↔ CPT; identify what corresponds to charge, parity, time reversal in the adelic setting | YES — pre-register derived adelic CPT transformation before peer review |
| FQ10 | **Consciousness and the Boundary of Distinction** — If all structure arises from distinction, what is the observer's role in actualizing the classical world? Does the adelic structure imply a participatory universe (Wheeler) grounded in valuation theory? | OPEN | Literature on Wheeler's participatory universe + von Neumann chain; identify where distinction/observer enters the formalism | UNCLEAR — may be unfalsifiable without operationalizing "observer" |

---

## 2. FALSIFIABLE PREDICTIONS (RQ4 — §5)

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition | Status |
|:---|:-----------|:------------|:-----------|:--------------------------|:-------|
| **P1** | Compton-count quantisation in UHECR GZK cutoff — specific rational thresholds in the energy spectrum at E/m_p ratios | Requires further development | Auger/Telescope Array | No rational-threshold structure after N events; smooth continuum preferred | UNFUNDED — needs formal derivation |
| **P2** ⭐ | Lorentz-violation dispersion from tree discreteness: E² = p²c² + m²c⁴ + ξ·E³/m_P with ξ(p) ≠ ξ(q) prime-dependent threshold structure | **2-5 years** | Fermi-LAT (existing 10⁴ GRBs), CTA | ξ < 10⁻²² without a signal OR ξ same at all primes | **PREREGISTERABLE** — register ξ thresholds and prime-dependence signature before data analysis |
| **P3** | BT-tree scattering using Romanov-Rudin 1995 formalism — prime-dependent scattering amplitudes | Requires further development | Theory | Scattering amplitudes indistinguishable from standard QFT to 10σ | UNFUNDED |
| **P4** | Feynman diagrams as tensor network contractions on the BT tree | Requires further development | Theory | No computational advantage over standard Feynman rules | UNFUNDED |
| **P5** | Quasiparticle invariance null test — no host-independent effective mass discovered | **Now** (holds ~90yr) | PDG systematic review | Single quasiparticle with identical m* in two chemically distinct lattices | **HOLDS** — systematic review pending |

⭐ = highest priority; fulcrum for thesis elevation from Philosophy to Physics.

---

## 3. PER-RQ FALSIFIABILITY CONDITIONS (Disconfirmation Checklist)

| RQ | Claim | Disconfirmed If… | Status |
|:---|:------|:-----------------|:-------|
| **RQ1** | Compton count is the only primitive | A quasiparticle with invariant m* across chemically distinct lattices is found (single counterexample sufficient) | **HOLDS** — ~90yr of condensed matter; PDG systematic review pending |
| **RQ2** | Physical number system is Q, not R | A physical quantity demonstrably requires a non-computable real number where the difference between two non-computable candidates is experimentally measurable | **HOLDS** — no such quantity known |
| **RQ3** | BT tree replaces R³ as coordinate system | Lorentz violation detected below Planck scale AND shown to have no tree-geometry structure (smooth, continuous, not prime-structured) | **UNRESOLVED** — consistent with current bounds (ξ < 10⁻²⁰) but no positive evidence |
| **RQ4** | Framework generates testable Planck-scale predictions | All five candidates (P1-P5) eliminated: P2 constrained below ξ < 10⁻²² without signal AND P5 falsified by host-independent quasiparticle AND no P1/P3/P4 development | **PARTIAL** — P5 holds; P2 unmeasured; P1/P3/P4 undeveloped |
| **RQ5** | Five disciplines independently discovered same tree without connecting | A sixth domain using the same tree AND already connected to particle ontology before 2026 is found | **HOLDS** — 8-source literature search found zero connections |

---

## 4. PRE-REGISTRATION SCAFFOLD

> **Protocol:** Per research skill §Phase 4 (Structured Forecast Protocol) and user mandate: forecasts and falsifiable conditions must be pre-registered before data collection.

### REG-ODR-001: Lorentz-Violation Dispersion Prime Structure

- **Hypothesis:** The dispersion relation modified by tree-discreteness produces prime-dependent Lorentz-violation parameter ξ(p), with ξ(2) ≠ ξ(3) ≠ ξ(5) ...
- **Falsification:** ξ measured to be identical across all primes within ±10% tolerance after Fermi-LAT full dataset analysis
- **Data source:** Fermi-LAT GRB photon arrival times, >10⁴ events
- **Pre-registration deadline:** Before initiating GRB time-delay analysis
- **Status:** **NOT YET PREREGISTERED** — requires formal derivation of ξ(p) calculation first
- **Dependency:** FQ8 (Testable Predictions of the Adelic Universe)

### REG-ODR-002: Quasiparticle Invariance Null Test

- **Hypothesis:** No quasiparticle has an effective mass m* invariant across two or more chemically distinct host lattices
- **Falsification:** Discovery of a quasiparticle with identical m* (within ±5%) in two chemically distinct materials (different elements, different crystal structure)
- **Method:** Systematic review of PDG + solid-state databases for m* values
- **Pre-registration deadline:** Before beginning systematic PDG review
- **Status:** **NOT YET PREREGISTERED**
- **Note:** Holds ~90yr since Landau 1957; pre-registration would formalize the null hypothesis

### REG-ODR-003: Adelic Noether Theorem (FQ2)

- **Hypothesis:** Noether's theorem can be reformulated such that the product formula ∏_v |x|_v = 1 emerges as the condition for global conservation
- **Falsification:** Formal proof that no such reformulation is possible without adding assumptions absent from standard Noether
- **Pre-registration deadline:** Before publishing derivation
- **Status:** **NOT YET PREREGISTERED**

---

## 5. CALIBRATION REGISTER (Dated Predictions)

| ID | Prediction | Date | Check Date | Strength | Status |
|:---|:-----------|:-----|:-----------|:---------|:-------|
| CAL-ODR-01 | Fermi-LAT analysis of ξ(p) prime-dependence yields ξ < 10⁻²² (no signal at current precision) | 2026-08-04 | 2028-08-04 | [WEAK] — dependent on someone doing the analysis | PENDING |
| CAL-ODR-02 | No quasiparticle counterexample to RQ1 found by 2030 | 2026-08-04 | 2030-08-04 | [STRONG] — 90yr null result extends | PENDING |
| CAL-ODR-03 | ≥1 external (non-QNFO) citation of p-adic AdS/CFT paper connected to particle ontology by 2030 | 2026-08-04 | 2030-08-04 | [WEAK] | PENDING |
| CAL-ODR-04 | ODR thesis is NOT the last "accidental" silo-bridge discovery; ≥1 more such discovery by 2028 | 2026-08-04 | 2028-08-04 | [MODERATE] | PENDING |
| CAL-ODR-05 | FQ2 (Product Formula → Conservation Law) produces a publishable derivation within 3 years | 2026-08-04 | 2029-08-04 | [WEAK] — depends on researcher time | PENDING |

---

## 6. NEXT ACTIONS (Prioritized)

| Priority | Action | Depends On | Target |
|:---------|:-------|:-----------|:-------|
| **P0** | Formal pre-registration of REG-ODR-001 and REG-ODR-002 | Derivation of ξ(p) (FQ2 dependency) | 2026-Q3 |
| **P1** | FQ2 — formal derivation of Noether's theorem in valuation-theoretic language | None | 2026-Q3 |
| **P2** | P5 — systematic PDG review for quasiparticle invariance | REG-ODR-002 preregistration | 2026-Q3 |
| **P3** | P2 — Fermi-LAT GRB time-delay analysis for ξ(p) | REG-ODR-001 preregistration; ξ(p) derivation | 2026-Q4 |
| **P4** | FQ3 — spacetime emergence from distinction networks: formal definition of "real-section" | Literature on adelic tensor networks | 2027 |
| **P5** | FQ7 — quantum logic / p-adic lattice isomorphism: map orthomodular lattice to Q_p clopen sets | None | 2027 |
| **P6** | FQ4 — gauge group from idele class group: compute Aut(C_K) and compare to SM gauge group | None | 2027-2028 |
| **P7** | FQ6 — Laws of Form → Ostrowski: formal mapping of LoF structures to valuation theory | None | 2028+ |

---

## 7. SESSION LOG

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-04 | hdd6PloLtF_ybqD_CK7EH | Registry created from ODR Thesis v2.0 content (10 frontier questions + 5 predictions + 5 falsifiability conditions extracted from published PDF §5, §7, §8) |

---

## 8. MAINTENANCE PROTOCOL

- **Update on:** publication of any research addressing an OPEN question
- **Update on:** any disconfirmation condition triggered (HARD — must log immediately)
- **Update on:** pre-registration locking (REG-ODR-### status change)
- **Update on:** calibration register [CHECK: YYYY] dates elapsing
- **Minimum review cadence:** quarterly
- **Living document:** this file is the canonical record; no separate database; commit directly to github.com/QNFO/odr-thesis

---

*"These research questions are pathways to the confirmation or refutation of the adelic distinction thesis. They are not the body of this paper but the frontier it opens."* — ODR Thesis v2.0, §7.3

---

## 9. COMPANION PAPER — Quasiparticles as Rational Functions v2.0

> **Canonical DOI:** [10.5281/zenodo.21784490](https://doi.org/10.5281/zenodo.21784490)
> **Published:** 2026-08-04 | **Relation:** Extends ODR RQ1 into condensed matter with cross-ratio formalism
> **Synopsis:** The BT tree has no origin — the electron Compton count is already a cross-ratio against the Planck scale. Quasiparticles are nested cross-ratios; particles and quasiparticles are ontologically identical in the BT tree.

### QP Falsifiability Conditions (5)

| ID | Condition | Test Method | Status |
|:---|:----------|:-----------|:-------|
| **QP-F1** | Quasiparticle found with m* independent of host material, temperature, and external fields | PDG + solid-state review | **HOLDS** (~90yr) — this is the same null test as ODR RQ1 |
| **QP-F2** | Phonon mode with p-adic ord_p(N_C) invariant across lattice constant changes | DFT calculations across crystal structures | **UNTESTED** |
| **QP-F3** | Quasiparticle surviving removal of host medium (free excitation post lattice dissolution) | Condensed matter experiment | **HOLDS** — no known quasiparticle survives host removal |
| **QP-F4** | Experiment isolating Compton count without measurement apparatus/background (cross-ratio-unavoidability) | Fundamental QM test | **HOLDS** — measurement problem in QM; no such experiment exists |
| **QP-F5** | Nested cross-ratio fails for any composite system (not expressible as rational function of fundamental N_C) | Compute ω_excitation/ω_lattice for wide material class | **UNTESTED** — requires DFT computational campaign |

### QP Frontier Question

**Maximum Ontological Distance:** Is there a depth threshold on the BT tree beyond which the rational function approximation for N_C*(α) breaks down? The answer: when the host lattice loses stable prime factorization (disordered/strongly correlated beyond quasiparticle paradigm).

### QP Key Insight (v2.0 — cross-ratio)

> "There are no substances, only cross-ratios at different scales." — The invariant particle IS a relation (cross-ratio against Planck scale). Dualism resolves into geometric fact: the BT tree has no origin, so every coordinate is a ratio of two reference points.

### QP Intersection with ODR RQs

| ODR RQ | QP Extension |
|:-------|:-------------|
| RQ1 (Compton count as primitive) | **Strengthened** — valid for both particles and quasiparticles via cross-ratio |
| RQ4 (Testable predictions) | **Reinforced** — P5 (quasiparticle null test) aligns with QP-F1 |
| FQ10 (Consciousness/observer) | **Precursor** — QP-F4 (cross-ratio unavoidability) touches measurement problem |

### QP Session Log

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-04 | hdd6PloLtF_ybqD_CK7EH | QP v2.0 companion entries added to ODR continuity registry |

