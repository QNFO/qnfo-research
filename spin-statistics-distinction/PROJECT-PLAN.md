# WBS: QNFO.RES.009

# The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant

**Status:** Phase 0 (Init) — 2026-08-14
**Author:** Rowan Brad Quni-Gudzinas (QNFO)
**Branch:** `res/paper/spin-statistics-distinction`
**Repository:** QNFO/qnfo-research
**Genre:** A (epistemic / structural analysis) — due-diligence + formal-derivation sketch
**Seed material:** Obsidian daily-note deep-inquiry cluster 2026-08-14 (`D:\Obsidian\notes\v1\2026\08\14\_2622613*`), parent treatise QNFO.SLB.002 (DOI 10.5281/zenodo.21905186 / 21908818).

---

## Charter

The boson/fermion distinction — encoded by the spin-statistics theorem (integer spin ⇒ symmetric/exterior statistics, half-integer spin ⇒ antisymmetric) — is routinely treated as a primitive dichotomy of nature. This project argues the dichotomy is a **derived, dimension-dependent shadow** of a single structural law, and that a distinction-based foundation (the calculus of re-entrant distinctions) must derive exchange statistics from the act of distinction instead of assuming it. The paper delivers: (1) a due-diligence corpus sweep (internal + external), (2) a formal-analysis sketch showing the invariant is the ribbon-categorical relation R = e^{2πis} (exchange phase = topological spin), and (3) a constructive gap analysis of the treatise's silent choice of the symmetric algebra for the `!` modality (its Appendix A), with a proposal for two modal exponentials `!_S` / `!_Λ` (symmetric/exterior) and the braiding of two marks in a compact closed category.

## §1.2 Core Claim (LOCKED, P6 — 2026-08-14)

**Core claim (locked):** The boson/fermion split is not the fundamental invariant; the invariant is the spin–statistics relation R = e^{2πis} — exchange phase equals topological spin — holding in any dimension, with the 3+1D binary forced only by the permutation-group topology of the configuration space of identical particles. A calculus of re-entrant distinctions (treatise SLB.002) claiming to ground quantum statistics must derive exchange statistics from the act of distinction: construct the braiding of two marks in a compact closed category and derive the symmetric-vs-exterior algebra choice from mark parity, rather than silently assuming the symmetric algebra for `!`.

**Pre-registration (KIF-60, timestamped 2026-08-14):** locked in this PROJECT-PLAN.md, commit `v0.1-phase0`, branch res/paper/spin-statistics-distinction, QNFO.RES.009 registry row.

**Falsifiability conditions (KIF-60):**
- F1: If a stable, local, relativistic excitation in 3+1D is observed with exchange phase ≠ e^{2πis} (e.g., a spin-1/2 boson or spin-0 fermion), the claim that R = e^{2πis} is the universal invariant is DISCONFIRMED.
- F2: If the mark-calculus extension (two modal exponentials !_S / !_Λ, braiding of marks) cannot reproduce the two 1-dimensional representations of S_n (trivial and sign) from the primitive distinction alone without additional physical postulates, the treatise-derivation claim is DISCONFIRMED.

**Surprise accounting:** The existence of anyons in 2+1D is already established and does NOT count as predictive evidence for this paper (P(anyon statistics | random structure) is high). Only F1's precision constraint and F2's derivability constraint carry evidential weight.

## Phases with WBS

| Phase | WBS | Deliverable / Gate |
|---|---|---|
| P0 | QNFO.RES.009.P0 | Branch, PROJECT-PLAN.md, core-claim lock, commit/tag/push (v0.1-phase0) |
| P1 | QNFO.RES.009.P1 | Due diligence (DUE-DILIGENCE-DEPTH-1): KG stats, ≥3 formulations, resolve_paper_id per hit, ≥2 adjacent domains, external verification, artifacts/external-search/* |
| P1b | QNFO.RES.009.P1b | KIF-29 consilience gate + KIF-60 bayesian gate artifacts |
| P2 | QNFO.RES.009.P2 | Literature: 8 sources, classification, Mandatory Symmetry Template (KIF-18) |
| P3 | QNFO.RES.009.P3 | Citations: references.bib, P3.AUTHOR-GATE live verification, citation-audit.md |
| P4 | QNFO.RES.009.P4 | Deep research: formal sketch (braided compact-closed calculus, !_S/!_Λ, ribbon condition, 3+1D reduction), structured forecast + calibration register |
| P5 | QNFO.RES.009.P5 | Publication: `<slug>.md` + CDP PDF + BP-1..10 gates + Zenodo deposit |
| P6 | QNFO.RES.009.P6 | Deployment: D1 living-paper, papers-server, KG node + Vectorize indexing |
| P7 | QNFO.RES.009.P7 | Dissemination: PhilPapers levers, social, outreach |
| P8 | QNFO.RES.009.P8 | Distribution: GitHub tag, Zenodo newversions, R2 archive, corrections |

## Milestones with Gate Criteria

- M0 (P0): branch pushed, registry rows verified (program_registry + wbs_state), PROJECT-PLAN committed, tag v0.1-phase0 exists on origin. 
- M1 (P1): "QNFO Cross-Reference: Found N related papers across M domains (corpus size K)" + external-search evidence files exist.
- M2 (P5): doi.org HEAD 200, DataCite findable, deposited .md sha256 matches local, all source files present (PUBLICATION-SOURCE-COMPLETENESS-1).
- M3 (P6): D1 row re-queried, KG neighbors > 0, Vectorize indexed:true.

## Deliverable Registry

- `<slug>/PROJECT-PLAN.md` (this file)
- `<slug>/README.md`
- `<slug>/<slug>.md` + `.pdf` + `.html` (P5)
- `<slug>/references.bib`, `<slug>/citation-audit.md`
- `<slug>/docs/deep-research.md`, `<slug>/artifacts/consilience-gate.md`, `<slug>/artifacts/bayesian-evidential-weight.md`, `<slug>/artifacts/external-search/*`

## Risk Register

| ID | Risk | Mitigation |
|---|---|---|
| R1 | KIF-60 retrodiction: R = e^{2πis} is established physics; paper framed as new discovery | Frame novelty as derivation-from-distinction (F2), not the relation itself; label known parts [KNOWN] |
| R2 | MAP-TERRITORY: treatise critique overclaims a derivation | Falsifiability conditions F1/F2; map/territory labels mandatory |
| R3 | Duplication: qnfo-photon-audit H1c spin-statistics reconciliation; ZBW P4 anyon bridge | Cite both; position as the structural invariant paper, not a re-audit |
| R4 | External prior art (Duck–Sudarshan, Bain, Joyal–Street braided categories, Deligne) | P1 external verification sweep; P3 AUTHOR-GATE |
| R5 | Scope creep into new physics claims | Genre A epistemic framing; no new numerical predictions beyond F1/F2 |

## Success Criteria

1. P1 finds ≥5 QNFO-internal related records across ≥2 WBS domains + ≥8 verified external references.
2. F2 derivability sketch written with explicit construction or explicit impossibility argument.
3. Publication passes BP-1..BP-10 and 5-layer consolidated closeout verification.
