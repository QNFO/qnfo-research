# WBS: QNFO.RES.007

# Invariant Structural Value — Project Plan

**Project:** Invariant Structural Value — what invariant relations fundamental constants and formulas encode, rather than their numerical magnitudes in human units
**WBS:** QNFO.RES.007
**Program:** QNFO.RES (QNFO Research Archive)
**Repo:** QNFO/qnfo-research
**Branch:** res/paper/invariant-structural-value
**Slug:** invariant-structural-value
**Source note:** Obsidian daily note `D:\Obsidian\notes\v1\2026\08\14\_26226072852.md` (working draft, philosophy of physics)
**Adjacent records (distinct):** The Computable Real Boundary (10.5281/zenodo.21645350, measurable-vs-imaginable, published 2026-07-29) — treats the computable-real boundary; this project treats the invariant content of constants/formulas (complementary, not duplicate)
**Created:** 2026-08-14
**Status:** Phase 0 (scaffold)

---

## §1 Charter

The daily-note working draft develops a structuralist reading of physical law: measured
quantities are **invariants of a larger mathematical structure under redundancy groups**
(unit rescalings, coordinate changes, gauge transformations, Hilbert-space basis changes).
The project makes this reading precise and publishable.

Three threads from the source note:

1. **Invariant content, not magnitudes.** Dimensionful constants (c, ħ, G, k_B) are bridges
   between categories of quantity; their numerical values are unit conventions. The invariant
   structural value is the dimensionless relation: ratios (m_p/m_e, α), angles and phases
   (CKM/PMNS, Jarlskog invariant), topological indices (Chern numbers, winding numbers,
   anomaly coefficients), fixed-point values (RG, universality classes, critical exponents),
   and conservation/symmetry structure (Noether, gauge invariance, diffeomorphism invariance).

2. **Quantum mechanics as invariant structure.** Measurable content is the projective ray,
   spectra, transition probabilities, S-matrix elements, and quantized topological invariants
   (Aharonov–Bohm holonomy, Hall conductance as Chern number, Berry phase). The non-measurable
   scaffolding — complex phases, gauge potentials, path-integral histories, ghost fields/BRST
   cohomology, bare parameters, complexified kinematic spaces — is the total space whose
   invariants are the measured world.

3. **Self-adjoint and self-reference: e and π from mark and distinction.** Self-adjointness
   is a mirror fixed point (A = A†); self-reference produces fixed points. e is the invariant
   of self-application (f′ = f; (1+1/n)^n); π is the invariant of self-closure (periodicity on
   the circle; U(1) exponential map with kernel 2πℤ). Euler identity e^{iπ} + 1 = 0 is the
   joint fixed point of growth, closure, and distinction. Compact closed categories make
   feedback/traces the structural home of these invariants.

The paper will deliver a falsifiable, citation-grounded philosophical-physics analysis in the
QNFO publication pipeline (Zenodo DOI, GitHub provenance, D1/KG/Vectorize indexing).

---

## §2 Core Claim (locked, Phase 0 P6)

**C1 (structural):** Fundamental constants and formulas encode invariant relations —
dimensionless ratios, symmetry-group data, topological indices, and fixed-point values —
not unit-dependent magnitudes. Their invariant structural value is their place in the
network of lawful relations, not their decimal expansion.

**C2 (structural, QM rewrite):** Measurable physics is the invariant quotient of a larger
non-measurable mathematical structure modulo redundancy groups (units, coordinates, gauge,
basis, scale). The non-physical scaffolding is necessary for computing the invariants.

**C3 (generative, e/π):** The constants e and π are fixed points of two canonical
self-referential operations on a primitive mark/distinction: e of self-application
(f′ = f), π of self-closure (e^{2πi} = 1). Euler identity e^{iπ} + 1 = 0 is their joint
fixed point; compact closed structure (traces/feedback) is the categorical setting.

**Falsifiability conditions (per claim):**
- C1 disconfirmed if: a dimensionful constant is shown to carry invariant physical content
  beyond its role as a unit bridge (i.e., a dimensionless combination cannot be formed that
  captures the claimed invariant), OR a claim that a specific "invariant" is scale-dependent
  is demonstrated where the paper asserted scale-invariance.
- C2 disconfirmed if: a measurable quantity is exhibited that is not expressible as an
  invariant under the enumerated redundancy groups (e.g., a gauge-dependent observable that
  is nonetheless measured).
- C3 disconfirmed if: e or π can be shown to require input beyond mark/distinction +
  self-reference (e.g., a derivation needing an additional primitive not derivable from
  the calculus of indications), OR a self-referential equation is exhibited whose fixed
  point is a constant other than e or π with no structural characterization.
- Symmetric audit (KIF-29): incumbent structural-realist accounts (Worrall, Ladyman/Ross,
  French) must be graded with the same kill-criteria as this framework.

---

## §3 Phases (WBS.TAXONOMY mapping)

| Phase | WBS | Deliverable | Gate |
|:------|:----|:------------|:-----|
| P0 Init | RES.007.P0 | Branch, PROJECT-PLAN.md, core claim lock | HARD (this file) |
| P1 Due diligence | RES.007.P1 | artifacts/due-diligence-phase1.md + external-search/ evidence | HARD |
| P1b Consilience | RES.007.P1b | artifacts/consilience-gate.md (KIF-29) | HARD |
| P2 Literature | RES.007.P2 | artifacts/phase2-literature-review.md | HARD |
| P3 Citations | RES.007.P3 | references.bib, artifacts/citation-audit.md | HARD |
| P4 Deep research | RES.007.P4 | docs/invariant-structural-value.md (full draft) | HARD |
| P5 Publication | RES.007.P5 | PDF (CDP pipeline), Zenodo DOI, gates BP-1..BP-10 | HARD |
| P6 Deployment | RES.007.P6 | D1 living-paper, papers-server, Vectorize index | HARD |
| P7 Dissemination | RES.007.P7 | SEO, social, archive.org | SOFT |
| P8 Distribution | RES.007.P8 | GitHub tag, Zenodo newversion, R2, KG node | HARD |

---

## §4 Milestones

| # | Milestone | Gate criteria |
|:--|:----------|:--------------|
| M0 | Phase 0 committed | branch + PROJECT-PLAN + README + .gitignore pushed; tag v0.1-phase0; ls-remote verified |
| M1 | Phase 1 complete | due-diligence-phase1.md + consilience-gate.md + external-search/ evidence committed |
| M2 | Phase 4 draft complete | full draft + BP-1..BP-10 + language gates pass |
| M3 | Publication | DOI resolves via doi.org HEAD 200; DataCite state=findable; GitHub provenance link |

---

## §5 Deliverable Registry

| Deliverable | Path | Status |
|:------------|:-----|:-------|
| Project plan | invariant-structural-value/PROJECT-PLAN.md | ✅ this commit |
| README | invariant-structural-value/README.md | ✅ this commit |
| .gitignore | invariant-structural-value/.gitignore | ✅ this commit |
| Due diligence report | artifacts/due-diligence-phase1.md | ⏳ P1 |
| Consilience gate | artifacts/consilience-gate.md | ⏳ P1b |
| Paper draft | docs/invariant-structural-value.md | ⏳ P4 |
| references.bib | artifacts/references.bib | ⏳ P3 |
| Citation audit | artifacts/citation-audit.md | ⏳ P3 |
| PDF | releases/invariant-structural-value.pdf | ⏳ P5 |
| RESEARCH-CONTINUITY-REGISTRY.md | invariant-structural-value/RESEARCH-CONTINUITY-REGISTRY.md | ⏳ P4 (if frontier items) |

---

## §6 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Numerology drift (fitting e/π to arbitrary patterns) | MED | HIGH | BP-8 numerology classification; KIF-60 Bayesian gate on every correspondence |
| Duplicate of measurable-vs-imaginable | LOW | MED | Explicit differentiation in P1 gap analysis; distinct C1–C3 |
| Overclaiming structural realism | MED | MED | Symmetric audit of incumbents; MAP-TERRITORY-1 labels with falsifiability |
| Retrodiction (claims built around known α values) | MED | HIGH | Pre-registration of any novel prediction; Δlog-odds ≤ 0 → [RETRODICTION] |

---

## §7 Success Criteria

1. C1–C3 each carry a concrete disconfirmation condition (KIF-60 pass).
2. Phase 1 due diligence ≥3 query formulations, ≥2 adjacent WBS domains, external evidence files.
3. Published with full provenance set (PUBLICATION-SOURCE-COMPLETENESS-1): .md/.html/.pdf + references.bib + citation-audit.md + PROJECT-PLAN.md + README.md + docs/deep-research + artifacts + external-search evidence + GitHub related_identifiers.
4. Post-publication adversarial analysis gate (HARD): red-team audit after Zenodo publish; every HARD finding → next-cycle kaizen item.
