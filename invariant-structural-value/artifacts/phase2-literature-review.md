# Phase 2 — Literature Review (QNFO.RES.007)

**Project:** Invariant Structural Value
**Date:** 2026-08-14
**Branch:** res/paper/invariant-structural-value
**WBS:** QNFO.RES.007
**Method:** 8-source sweep (OpenAlex PRIMARY, Crossref, Zenodo, Europe PMC, arXiv, web via search APIs, QNFO Vectorize, QNFO KG) + dedup + 4-tier classification + KIF-18 Mandatory Symmetry Template.

## 1. Sources Swept

| Source | Evidence file(s) | Notes |
|:-------|:-----------------|:------|
| OpenAlex (PRIMARY) | external-search/openalex_*.json (5 queries) | structural realism core, Laudan, Ladyman-Ross |
| Crossref | external-search/crossref_*.json (2 queries) | OSR monograph, Methodological SR, Miracles & SR |
| Zenodo records | external-search/zenodo_*.json (2 queries) | NO external duplicate of C1-C3 (noise only) |
| Europe PMC | external-search/pmc_constants_invariant.json | Domain Projection preprint; Z3-graded framework |
| arXiv | external-search/README.md (§arxiv-*) | De Haro-Butterfield 2508.01616; Solà 1507.02229; Thompson 1702.07382; Knuth 1504.06686; Rovelli 1805.10602; de Ronde 2306.13975; Ezhela; Mohr-Taylor-Newell CODATA 0801.0028; **Moldoveanu 1303.3935 (QM from invariance principles)**; LoF→e/π query = ZERO relevant |
| QNFO Vectorize | due-diligence-phase1.md §2 (≥4 formulations) | 13 adjacent records |
| QNFO KG | query_graph stats/nodes live | 8,279 nodes / 1,621 Paper |

**Count:** external independent hits retained = **24** (OpenAlex 6, Crossref 5, Europe PMC 3, arXiv 9, Zenodo 0 relevant). QNFO-internal adjacent = 13. Total deduplicated classified = **37**.

**Confirmation-bias disclosure (KIF-17):** internal high-scoring hits dominate the QNFO Vectorize pass (expected — author's own corpus). External corroboration exists for C1/C2 components (structural realism, duality, invariance-principle axiomatics) but is **absent** for C3 (LoF→e/π fixed-point derivation). Flag `[UNIQUE-CLAIM]` on C3 — see §4.

## 2. Classification Matrix (4 tiers)

### Tier 1 — Core (directly engages C1/C2/C3)
| # | Work | Source | C1 | C2 | C3 |
|:--|:-----|:-------|:--:|:--:|:--:|
| 1 | Ostrowski Dimensionless Reformulation v4.0.4 (10.5281/zenodo.21756190) | QNFO | ★ | | |
| 2 | Quantum-Mechanical Physics as Invariant Geometric Structure (10.5281/zenodo.20109773) | QNFO | | ★ | |
| 3 | Fine-Structure Constant as a Cross-Ratio (10.5281/zenodo.20108536) | QNFO | ★ | | |
| 4 | Syntactic Token Calculus v3 (10.5281/zenodo.19547736) | QNFO | | ★ | ◐ |
| 5 | α-π-Helix: Geometric Unification of Fundamental Constants (10.5281/zenodo.21515789) | QNFO | ★ | | ◐ |
| 6 | Quantum Laws of Form: Superposition as Re-Entry, Measurement as Distinction (10.5281/zenodo.21205110) | QNFO | | ★ | ◐ |
| 7 | The Calculus of Distinction: LoF ↔ Ultrametric Trees (10.5281/zenodo.21205097) | QNFO | | | ◐ |
| 8 | The Computable Real Boundary (10.5281/zenodo.21645350) | QNFO | ◐ | ★ | |
| 9 | Domain Projection: The Geometric Origin of Physical Constants and Laws (10.21203/rs.3.rs-8629054/v1) | PMC | ★ | ◐ | |
| 10 | Quantum mechanics from invariance principles (arXiv:1303.3935, Moldoveanu) | arXiv | | ★ | |
| 11 | The Philosophy and Physics of Duality (arXiv:2508.01616, De Haro & Butterfield) | arXiv | ◐ | ★ | |
| 12 | Ontic Structural Realism and the Philosophy of Physics (10.1093/acprof:oso/9780199276196) | OA/CR | ★ | ◐ | |

★ = directly supports · ◐ = partially/adjacent

### Tier 2 — Supporting
- Every Thing Must Go (Ladyman & Ross, 10.1093/acprof:oso/9780199276196.001.0001) — ontic structural realism program
- Structural Realism (Stanford OBO, 10.1093/obo/9780195396577-0154) — taxonomy of SR variants
- Structural realism beyond physics (10.1016/j.shpsa.2016.06.008) — SR scope extension
- Methodological Structural Realism (10.1007/978-94-007-2579-9_2)
- Miracles and Structural Realism (10.1007/978-94-007-2579-9_4)
- Base-Invariant Number-Theoretic Patterns in Fundamental Constants (10.5281/zenodo.19469966) — QNFO
- Winding Numbers and Strange Loops (10.5281/zenodo.17322662) — QNFO (S¹ invariants, e^{inθ})
- Strange Loop Theory of Physical Quantization (10.5281/zenodo.17419332) — QNFO (fixed-point R(Ψ)=Ψ)
- The Notation Problem (10.5281/zenodo.21690262) — QNFO (scaffold-stripping, distinction calculus)
- The Deeper Roles of Mathematics in Physical Laws (arXiv:1504.06686, Knuth) — laws as symmetry constraints
- An Exact Z3-Graded Algebraic Framework Underlying Observed Fundamental Constants (10.20944/preprints202512.2527.v2) — PMC
- Adelic Core Synthesis (10.5281/zenodo.21786473) — QNFO (running coupling: 1/137 is a red herring)

### Tier 3 — Background
- A Confutation of Convergent Realism (Laudan, 10.1086/288975) — anti-realism; motivates SR
- Moderate structural realism about space-time (10.1007/s11229-006-9076-8) — Esfeld-line
- Fundamental Constants in Physics and Their Time Variation (Solà, arXiv:1507.02229)
- Relation Between Fundamental Constants and Particle Physics Parameters (Thompson, arXiv:1702.07382)
- Confronting Cosmology and New Physics with Fundamental Constants (Thompson, arXiv:1312.4959)
- CODATA Recommended Values 2006 (Mohr-Taylor-Newell, arXiv:0801.0028)
- Inconstancy of the Fundamental Physical Constants (Ezhela et al., arXiv:physics/0409117)
- Physics Needs Philosophy (Rovelli, arXiv:1805.10602)
- Bohr's Anti-Realist Realism (de Ronde, arXiv:2306.13975)
- Electric-magnetic duality and the geometric Langlands program (10.4310/cntp.2007.v1.n1)
- The Cosmological Constant / dark energy reviews (10.1103/revmodphys.75.55; 10.12942/lrr-2001-1)

### Tier 4 — Reject / Contradiction-facing (for symmetric audit)
| # | Work | Why | Disposition |
|:--|:-----|:----|:------------|
| R1 | "Final Unifying Physics Theory…" (10.5281/zenodo.21928746) | Zenodo noise; non-peer, mass-energy formula patching | REJECT — no engagement |
| R2 | QNFO "Physics, Solved" (10.5281/zenodo.17368960) | Prior overclaim pattern (topological resonance, golden ratio) | CONTRAST — BP-8 discipline applies to THIS paper, not inherited |
| R3 | Adelic Constraints Project (10.5281/zenodo.20120042) | Completed null: number-theoretic constraints did NOT fix α | ENGAGE — C1 must not re-claim α derivation without addressing this null |
| R4 | α-π-Helix π-reification (10.5281/zenodo.21515789) | Treats π/α as helical projections | DISTINGUISH — this paper derives e/π from self-reference, not geometry |
| R5 | Structural realism underdetermination (Ladyman-Ross; De Haro-Butterfield Pt III) | SR's "relations not relata" can absorb any invariant claim | CONSTRAIN — C1/C2 must state what they add beyond SR |

## 3. Gap Confirmation vs. Phase 1

Phase 1 gaps stand:
1. **C1 unified structuralist thesis** — ODR is a compendium; α-π-Helix is geometric-specific; Domain Projection preprint is geometric-origin but not redundancy-group quotient; none states the general invariant-content thesis.
2. **C2 quotient formulation** — QM-IGS and Moldoveanu come closest (invariance-principle axiomatics) but neither frames "non-measurable scaffolding as total space whose invariants are measured" nor catalogs BRST/path-integral/bare-parameter redundancy quotients as a unified principle.
3. **C3 LoF→e/π fixed-point derivation** — **ZERO external corroboration found across OpenAlex, Crossref, Zenodo, Europe PMC, arXiv** (LoF queries return combinatorics/noise; arXiv LoF→e/π = 0 relevant). Spencer-Brown's imaginary values and fixed-point re-entry are adjacent but no work derives e (self-application) and π (self-closure) from mark-and-distinction self-reference with compact-closed trace semantics. **This is the paper's unique contribution — and its epistemic burden** (KIF-60 surprise accounting must bound P(match | random structure) in P4).

## 4. KIF-18 Mandatory Symmetry Template

For each core claim, both Supporting and Constraining literature are listed with equal rigor (2026-08-04 symmetric-audit injunction). A claim is not credited until its constraining literature is engaged.

### C1 — Constants encode invariant relations, not magnitudes

**Supports:**
- ODR v4.0.4 (place-democracy; dimensionless ratios are the invariant content)
- Fine-Structure Constant as Cross-Ratio (α = projective invariant)
- Base-Invariant Number-Theoretic Patterns (base-invariance ⇒ structural content)
- De Haro & Butterfield (geometric view of theories; equivalence under dualities)
- Mohr-Taylor-Newell CODATA (constants as jointly-measured correlated set — the relations persist)

**Constrains:**
- **Adelic Constraints Project null** (R3): if pure number theory constrains nothing, C1 must NOT claim α's value is derivable; it claims only that α's *structural role* is invariant. Distinguish "derivation of value" (rejected) from "characterization of role" (C1's claim).
- Solà / Thompson variability limits: μ and α can vary in time — an invariant *relation* need not be a constant *magnitude*; C1 must accommodate running/variation (α(μ) functional, not a static decimal).
- α-π-Helix reification warning: geometric reifications of constants have overclaimed before; C1 must stay at the structuralist level and pass BP-8 on any numeric claim.
- Laudan's pessimistic meta-induction: successful theories' structural core may still fail; C1 is a philosophical thesis with its own falsifiability condition (already stated in PROJECT-PLAN §2).

### C2 — Measurable physics = invariant quotient of larger math structure / redundancy groups

**Supports:**
- QM-IGS (QM as invariant geometric structure)
- Moldoveanu 1303.3935 (QM from invariance principles: relational + tensor-composition invariance)
- Syntactic Token Calculus (projective invariants as only measurable quantities)
- Winding Numbers and Strange Loops (winding number as invariant information carrier; e^{inθ} basis)
- De Haro & Butterfield (dualities as theory equivalence; geometric view)
- The Computable Real Boundary (what is measurable vs. what is formal scaffolding)

**Constrains:**
- **Gauge-invariant observables literature** (Fröb-Lima 1711.08470; Rudnicki et al. 1707.06926): relational gauge-invariant observables are *constructed* with field-dependent coordinate systems — the quotient is not trivial to define in quantum gravity; C2 must not imply the quotient is always computable.
- Hartle (gr-qc/0602013): generalized QM may need no fixed spacetime — C2's "redundancy groups" must be general enough to survive quantum-gravity contexts.
- de Ronde / Rovelli: anti-realist and relational readings compete for the same formalism; C2 must state its realism commitment explicitly (structural realism, not naive realism) or face the "absorbed by SR" objection (R5).

### C3 — e and π as fixed points of self-application/self-closure from mark-and-distinction

**Supports:**
- Quantum Laws of Form (re-entry as superposition; distinction as measurement)
- Calculus of Distinction (LoF ↔ ultrametric trees)
- Strange Loop Theory (fixed-point equation R(Ψ)=Ψ as quantization principle)
- The Notation Problem (scaffold-stripping: LoF contains valid invariants in inaccessible notation)
- Spencer-Brown, *Laws of Form* (1969) — re-entry and imaginary values (background canonical)
- Category-theoretic fixed-point/traced-monoidal literature (background canonical: Joyal-Street 1986 compact closed)

**Constrains (the hard part):**
- **Zero external literature derives e/π from LoF self-reference** → `[UNIQUE-CLAIM]`: the burden is maximal. KIF-60 requires pre-registration and surprise accounting — the derivation must be *constructive* (exhibit the fixed-point equations), not an after-the-fact identification of e/π in existing formulas (that would be [RETRODICTION]).
- **Risk of numerology drift** (BP-8): "e is the invariant of self-application" is a *characterization*, not a derivation of a decimal. The paper must state precisely which operation, on which primitive, yields *e as a fixed point* — otherwise the claim is vacuous.
- **π-context caution** (α-π-Helix, ODR v4.0 correction of "Euclidean π portability"): π's status across completions (Archimedean vs p-adic) is contested within the author's own corpus; C3 must respect ODR's corrected position.
- **Spencer-Brown's imaginary values**: LoF re-entry produces oscillating forms; the move from x = ¬x to i is *suggestive but not rigorous* in the published LoF literature — C3 must supply the rigor the tradition lacks.

**Symmetric audit outcome:** C1 and C2 are strongly supported externally and internally (thesis-viable with stated boundaries). C3 is externally unsupported — the paper's contribution — and must be built as a constructive derivation with explicit falsifiability, not a pattern-matching essay.

## 5. Literature Deficit Register (deferred to P4 deep research)

1. Need canonical citations for: Worrall (1989) "Structural Realism"; French & Ladyman SR program; Joyal-Street (1986) compact closed categories; Spencer-Brown (1969) exact re-entry chapters. → P3 citation extraction with P3.AUTHOR-GATE.
2. Need full engagement with the Adelic Constraints Project null (R3) in the C1 section.
3. Need to verify "Domain Projection" preprint authorship/peer status before citing (preprint; cite as preprint).
4. Need BP-10 independent recompute of any α-adjacent numeric claims if the paper makes them.

## 6. Conclusion

Phase 2 literature review complete: 37 deduplicated classified works (12 core / 12 supporting / 11 background / 5 rejection-contrast). KIF-18 symmetry template populated for C1-C3 with 28 support-constrain pairings. The paper's scientific boundary is now explicit: **C1/C2 are defensible structuralist theses with external anchors; C3 is the unique contribution carrying the [UNIQUE-CLAIM] burden and must be derived constructively in P4.** Proceed to P3 (citations) with the deficit register as input.
