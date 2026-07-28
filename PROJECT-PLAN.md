# PROJECT-PLAN: measurable-vs-imaginable

**Project:** The Computable Real Boundary — Physics vs. Mathematics/Creative Fiction  
**Status:** Phase 0 — Initialization  
**Version:** 0.1  
**Date:** 2026-07-28  
**License:** QNFO Unified License Agreement (QNFO-ULA)

---

## §1 Charter

### §1.1 Problem Statement

Contemporary physics operates on the real number field ℝ without questioning whether every element of ℝ is physically meaningful. ℝ is uncountable; all known physical quantities — every number that has ever appeared in a physics paper, every experimental result, every fundamental constant — belongs to a strictly smaller, countable subset: the **computable real numbers** (Turing 1936).

If a physical theory were to REQUIRE a non-computable real number (Chaitin's Ω, or any member of the uncountable non-computable reals), it would make predictions indistinguishable from computable approximations at any finite measurement precision. Such a theory is unfalsifiable — and thus not physics.

This project formalizes the boundary: **physics = computable reals + measurement**. Everything outside the computable closure — the uncountable non-computable reals, non-measurable sets, Banach–Tarski decompositions — belongs to a larger category: internally consistent formal systems (mathematics, creative fiction) that lack the external validation of physical measurement. This boundary is not a limitation on physics. It is a definition of what physics IS.

### §1.2 Core Claim Lock

**Original formulation** (from user prompt):

> The computable real numbers [established] (Turing 1936) form a countable subset of ℝ. Every number that has ever appeared in a physics paper — π, e, √2, the fine-structure constant — is computable. The non-computable reals (Chaitin's Ω, etc.) have never appeared in any physical prediction.  
>   
> **Question:** Could a physical theory REQUIRE a non-computable real number?  
>   
> **Answer:** If such a theory existed, it would be fundamentally untestable — because no finite measurement could distinguish a non-computable real from a computable approximation. A theory that makes untestable predictions fails the falsifiability requirement. We are therefore justified in restricting physical theories to computable (countable, ℚ-approximable) quantities. This is not a limitation — it's a recognition that untestable predictions are not physics.  
>   
> THIS IS WHAT MAY SEPARATE PHYSICAL REALITY IN THIS UNIVERSE AND ITS LAWS FROM AN IMAGINATIVE INFORMATIONAL "COGNITIVE FICTION" (A LARGER SET/DISTINCTION OF WHICH MATH IS A MEMBER). PHYSICS IS GROUNDED BY PHYSICAL REALITY. MATH, LIKE CREATIVE FICTION WRITING, IS NOT (EVEN IF IT APPEARS INTERNALLY CONSISTENT IT LACKS EXTERNAL VALIDATION WITHOUT A PHYSICAL BASIS).

**Reformulated as falsifiable claim:**

**C1 (Closure Claim):** [established] All physical theories that have made testable predictions use only computable real quantities. No physical theory has ever required a non-computable real number to produce a measurement-distinguishable prediction.

**C2 (Boundary Claim):** [speculative] The computable/non-computable boundary coincides with the physics/mathematics-creative-fiction boundary. Any formal system that traffics in non-computable quantities is, by construction, unfalsifiable — and thus definitionally not physics. This is a stronger claim than C1: it asserts that non-computable reals CANNOT enter physics without breaking falsifiability, not merely that they HAVEN'T.

**C3 (Ontological Closure Claim):** [my conjecture] The set of physically real quantities closes under finite distinguishability. What cannot be distinguished by any finite physical procedure cannot be physically real. This maps onto the Autaxys D/R+OC vocabulary: D/R primitives (distinction/relation) are exactly what finite measurement processes can discriminate; ontological closure is the condition that physics never needs or invokes what lies outside this discrimination frontier.

**Falsifiability conditions:**

- C1 would be disconfirmed if a published physics paper were found that makes a nontrivial, verifiable physical prediction dependent on a specific non-computable real number (i.e., the prediction DIFFERS meaningfully from the best computable approximation).
- C2 would be weakened (but not disconfirmed) if a well-formed physical theory were constructed that requires a non-computable real AND produces a falsifiable differential prediction — i.e., a prediction that an experiment could distinguish from all computable approximations.
- C3 would be disconfirmed if a measurement protocol were demonstrated that can distinguish a single bit of Chaitin's Ω beyond what any computable procedure can produce.

### §1.3 Distinction from Existing QNFO Work

Preliminary assessment (to be verified in Phase 1 Due Diligence):

- **Autaxys D/R+OC vocabulary:** Direct overlap — the D/R primitives (distinction/relation) map to "what finite measurement can discriminate," and ontological closure maps to "physics never needs non-computable quantities." The Autaxys deep-dive found zero external matches for this vocabulary across 480 papers (Vidotto 2022 being closest). This project formalizes a specific dimension of that vocabulary.
- **Measure-Theoretic Artifacts (Zenodo 21595214):** Potential overlap — non-measurable sets are another class of "mathematically well-defined but physically inaccessible" objects. This project's computability argument may complement the measure-theoretic one.
- **No known QNFO publication** directly addresses the computable-real boundary as a physics/mathematics demarcation criterion.

---

## §2 Work Breakdown Structure

| Phase | Title | Tag | Key Deliverables | Gate Criteria |
|:------|:------|:----|:-----------------|:-------------|
| 0 | Project Init | `v0.1-phase0` | Scaffold, PROJECT-PLAN.md, core claim lock, git init | All HARD pre-flight gates pass |
| 1 | Due Diligence | `v0.2-phase1-dd` | KG/D1 cross-reference, external lit baseline, gap analysis | KG + 2+ external sources queried; no DUPLICATE-WARNING |
| 2 | Literature Search | `v0.3-phase2-lit` | Classified paper set (core/supporting/background/reject), consilience audit | ≥5 core papers, Mandatory Symmetry Template filled |
| 3 | Citation Mgmt | `v0.4-phase3-cite` | BibTeX file, citation audit report | ≥90% citations matched; all core papers in BibTeX |
| 4 | Deep Research | `v0.5-phase4-deep` | 9-stage Bayesian cascade (if triggered), strategic memo | All 9 stages complete; calibration register populated |
| 5 | Publication | `v1.0` | Paper (markdown + PDF), Zenodo DOI, provenance bundle | PDF zero errors; Pub Language Gate pass; 18-point checklist ≥4.0 avg |
| 6 | Deployment | `v1.1-deploy` | D1 living-paper record, R2 archive, papers-server HTTP 200 | D1 slug + DOI present; R2 round-trip verified |
| 7 | Dissemination | `v1.2-disseminate` | SEO audit, Buffer posts, Internet Archive snapshot | All SEO artifacts present; Buffer posts confirmed |
| 8 | Core Distribution | `v1.3-distribute` | GitHub release, Zenodo new-version, KG seed | All 4 core layers (GitHub/Zenodo/R2/D1-KG) verified |

### §2.1 Phase Milestones

| Milestone | Phase | Success Criterion |
|:----------|:------|:------------------|
| M0: Scaffold locked | 0 | `git tag v0.1-phase0` pushed |
| M1: Landscape mapped | 1 | ≥50 unique papers identified across all sources |
| M2: Core evidence gathered | 2–3 | ≥5 core papers deep-read; all citations verified |
| M3: Claim stress-tested | 4 | Bayesian cascade complete; no blocking contradictions |
| M4: Paper published | 5 | Zenodo DOI resolves; PDF verified error-free |
| M5: Distributed | 6–8 | All 4 core distribution layers live and verified |

---

## §3 Deliverable Registry

| ID | Deliverable | Phase | Format | Local Path | Archival Target | Status |
|---|---|---|---|---|---|---|
| D-0.1 | PROJECT-PLAN.md | 0 | Markdown | `PROJECT-PLAN.md` | GitHub, R2 | in-progress |
| D-0.2 | README.md | 0 | Markdown | `README.md` | GitHub | complete |
| D-0.3 | .gitignore | 0 | Text | `.gitignore` | GitHub | complete |
| D-1.1 | Due Diligence Report | 1 | Markdown | `artifacts/due-diligence.md` | GitHub, R2 | pending |
| D-1.2 | Consilience Audit | 1 | Markdown | `artifacts/consilience-gate.md` | GitHub | pending |
| D-2.1 | Literature Classification | 2 | Markdown | `artifacts/lit-review.md` | GitHub, R2 | pending |
| D-3.1 | Citation Audit | 3 | Markdown | `artifacts/citation-audit.md` | GitHub | pending |
| D-3.2 | BibTeX Database | 3 | BibTeX | `references.bib` | GitHub, Zenodo | pending |
| D-4.1 | Strategic Memo (if triggered) | 4 | Markdown | `artifacts/strategic-memo.md` | GitHub | pending |
| D-5.1 | Paper (source) | 5 | Markdown | `paper.md` | GitHub, Zenodo, R2 | pending |
| D-5.2 | Paper (PDF) | 5 | PDF | `paper.pdf` | GitHub, Zenodo, R2 | pending |
| D-5.3 | Provenance Bundle | 5 | ZIP | `PROVENANCE-BUNDLE.zip` | Zenodo | pending |
| D-6.1 | D1 Living-Paper Record | 6 | SQL row | `living-paper.papers` | Cloudflare D1 | pending |
| D-6.2 | R2 Archive | 6 | Files | `releases/<YYYY>/<MM>/measurable-vs-imaginable/` | Cloudflare R2 | pending |
| D-7.1 | SEO Artifacts | 7 | Various | papers.qnfo.org | papers-server Worker | pending |
| D-7.2 | Social Media Posts | 7 | Buffer drafts | — | Buffer (Twitter/LinkedIn/Bluesky) | pending |
| D-8.1 | Knowledge Graph Node | 8 | KG node | — | QNFO Knowledge Graph | pending |

---

## §4 Risk Register

| ID | Risk | Phase(s) | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|---|---|
| R-01 | Prior QNFO work already covers this argument | 1 | Low | High | Mandatory Due Diligence Gate (KG + D1 + Vectorize + external search) before Phase 2 | open |
| R-02 | No external literature addresses computability-as-physics-boundary (makes lit review sparse) | 2 | Medium | Medium | Broaden search to adjacent domains: constructive mathematics, reverse mathematics, physical Church–Turing thesis, measurement theory | open |
| R-03 | Core claim resists falsifiable formulation (C2/C3 are philosophical, not empirical) | 0, 4 | Medium | High | Lock C1 (empirically verifiable) as primary; treat C2/C3 as philosophical corollaries with explicit [PHILOSOPHY] labeling | open |
| R-04 | "Computable real" definition is not the only notion of computability (Type-2 computability, BSS model, etc.) — ambiguity undermines rigor | 2, 5 | Medium | Medium | Explicitly define "computable" as Turing-computable (Type-1) in paper; acknowledge alternative definitions in a dedicated section | open |
| R-05 | Physical Church–Turing thesis is debated — citing it as a premise invites counterargument | 5 | Medium | Medium | Distinguish between "all physical processes are computable" (strong, debated) and "all known physical theories use computable quantities" (weak, defensible); build on the weak version | open |
| R-06 | PDF rendering errors (Unicode math symbols) | 5 | Medium | High | `build-paper.py` preprocessor + verification gate (KIF-27) | open |
| R-07 | Internal/project language leaking into publication | 5 | Medium | High | Publication Language Gate scan (blocking) before "publication-ready" | open |
| R-08 | Claim overlaps with existing QNFO papers in a way that risks self-plagiarism | 1, 5 | Low | Medium | Cite all prior QNFO work explicitly; position this paper as formalization of a specific dimension | open |

---

## §5 Success Criteria

1. **Core claim is publishable:** C1 (closure claim) is supported by literature review and passes Bayesian cascade without blocking contradictions.
2. **Argument is rigorous:** Definitions of "computable," "falsifiable," and "physical" are operationalized and defended.
3. **Connection to QNFO framework is explicit:** The computable-real boundary is shown to instantiate the Autaxys D/R+OC vocabulary.
4. **Paper meets all QNFO publication standards:** 18-point physics writing checklist, Professional Publication Standards, Publication Language Gate, and PDF verification all pass.
5. **Full distribution stack is live:** Zenodo DOI, R2 archive, D1 living-paper record, KG node, papers-server URL, and Buffer dissemination all verified.

---

## §6 Laws of Form Connection (Phase 0 Synthesis)

### §6.1 Spencer-Brown × Autaxys

Spencer-Brown's _Laws of Form_ (1969) + QNFO's _Quantum Laws of Form_ (2026) provide the formal calculus underlying the D/R+OC vocabulary. The primitives map as:

| LoF Primitive | Autaxys Mapping | Role in This Project |
|---------------|-----------------|---------------------|
| Mark `#` | **D** (Distinction) | Measurement outcome: "this, not that" |
| Enclosure `[ ]` | **R** (Relation) | Physical procedure connecting states |
| Calling `## = #` | Resonance/Coherence | Idempotent measurement repeats |
| Crossing `[#]` = void | **OC** (Ontological Closure) | Finitely undoable distinctions are not physically new |
| Re-entry `f = [f]` | Feedback Dynamics | The math↔physics reflexive loop itself |

### §6.2 Numbers as Built, Not Discovered

Numbers are constructed from distinction operations (LoF Number Builder; Silent Radix):
- ℕ = repeated Calling
- ℚ = nested enclosures
- ℝ_comp = limits of computable enclosure sequences
- ℝ = Monna-map projection (creates non-computable artifacts)
- ℚ_p = alternative enclosure algebras (p-adic valuation)
- 𝔸 = all enclosure algebras simultaneously (adèlic)

### §6.3 The Fixed Point

The reflexive loop "math abstracts from physics, physics is filtered by math" is a Re-entering form. Its fixed point under finite enclosure operations is ℝ_comp — the computable reals. This is the boundary between physics (can reduce to void by finite Calling/Crossing) and Cognitive Fiction (internally consistent but irreducible by any finite sequence).

### §6.4 Cognitive Fiction (Formal Definition)

A **Cognitive Fiction** is a formal system ℱ such that:
1. ℱ is expressible in enclosure algebra (`#`, `[ ]`, Calling, Crossing)
2. ℱ is internally consistent
3. ℱ cannot be reduced to void by any finite Calling/Crossing sequence

This places ℝ\ℝ_comp, non-measurable sets, and creative fiction in the same category.

### §6.5 Synthesis Document

Full synthesis with research architecture, red-team audit, and historical stratigraphy in `SYNTHESIS.md` and `artifacts/red-team-phase0.md`.

---

## §7 Version History

| Version | Date | Phase | Description |
|:--------|:-----|:------|:------------|
| v0.1 | 2026-07-28 | 0 | Project initialization — scaffold, charter, core claim lock, WBS, registers |
| v0.1.1 | 2026-07-28 | 0 | Phase 0 finalization — Laws of Form integration, synthesis, red-team audit complete |
