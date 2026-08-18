# WBS: QNFO.RES.015

**Project:** ZX Diagrams at the Seam: Spiders, Pauli Webs, Gadgets, and the Cafeteria Problem of Cross-Silo Imports
**Slug:** zx-diagram-fault-lines
**Repo:** QNFO/qnfo-research · **Branch:** res/paper/zx-diagram-fault-lines
**Status:** Phase 0 — Initialized (2026-08-18)
**Seed:** vault note `_26230100258.md` (2026-08-18)

---

## 1. Charter

Diagrammatic languages — above all the ZX calculus — are the dominant visual interface of
contemporary quantum computing: compilation, circuit optimization, error correction, and
measurement-based computation are all expressed as 2D graphs. The originating note poses the
question directly: are the ZX constructs **spiders**, **Pauli webs**, and **gadgets** fault
lines? The observation behind the question is a "cafeteria problem": each construct is imported
from a different siloed discipline, and the imports are mixed without any demonstrated mutual
compatibility — while the resulting 2D "tube" diagrams are easily mistaken for a picture of the
3+1D physical reality of quantum mechanics.

This project performs a **fault-line audit** of ZX-diagrammatic reasoning:

1. Decompose each construct (spiders, Pauli webs, gadgets) into its import provenance — which
   silo it came from, what it silently carries.
2. Audit the mutual compatibility of the imports, especially the mixing of 2D diagrammatic
   imports with 3+1D particle-physics imports and 1D thermodynamic/entropic imports.
3. Map the seam: where the diagram's internal validity ends and its bearing on physical reality
   is unestablished (the "cone of ignorance" the map does not probe).
4. Generalize: the cafeteria problem as a pervasive failure mode of siloed disciplines that
   remain separate except when mixing is convenient.

The epistemic posture throughout is map-aware use: diagrams are deliberately simplified maps
with internal validity; they are used for understanding and communication; and the map must
never be asserted as the territory.

## 2. Core Claim (LOCKED at P6)

> **The ZX-calculus constructs — spiders, Pauli webs, and gadgets — are cafeteria imports: each
> is drawn from a distinct silo (2D diagrammatic/categorical quantum mechanics, stabilizer and
> quantum-error-correction theory, measurement-based computation) and combined without
> demonstrated mutual-compatibility checks. The resulting 2D "tube" diagrams exhibit strong
> internal validity (soundness, completeness, computational utility) yet unestablished bearing
> on the 3+1D physical reality of quantum mechanics — the seam where the map ends and the
> territory begins is unprobed, and the map's cone of ignorance is unknown because it never
> probes outside its own locality. The cafeteria problem generalizes: siloed disciplines keep
> their imports separate except when mixing is convenient, without regard for mutual
> compatibility or contradiction. The remedy is map-aware use: treat diagrams as maps with
> declared seams, audit each construct's import provenance, and probe beyond the map's
> locality before asserting physical bearing.**

**Locking rule:** this claim is frozen at P6. Any material change to the claim requires a
version bump (tag) and a re-run of the Universal Ignorance Audit.

**Premise-depth disclosure (where the premises END):**

| Class | Items |
|---|---|
| **Imported primitives (unanalyzable here)** | ZX calculus mathematics: spider fusion rules, bialgebra/complementarity, soundness & completeness theorems (Coecke–Duncan; Backens); stabilizer formalism; MBQC gadget construction. Imported as established, not re-derived. |
| **Named imported inputs (QNFO corpus)** | Map/territory + locale framework (UMP.011: "the pedagogical map is not the ontological territory"); load-bearing-assumption critique method (RES.013 Electron Hook Treatise); purpose-grounding standard (RES.012); Universal Ignorance Audit instrument (RES.002, DOI 10.5281/zenodo.21901984). |
| **Derived in this project (own work)** | Import-provenance decomposition of spiders/Pauli webs/gadgets; cross-silo compatibility audit (2D vs 3+1D vs 1D imports); seam mapping; generalization of the cafeteria problem; map-aware-use remedy. |
| **Unanalyzable primitives of the framing itself** | The premise that a formalism can be "about" a physical reality at all (representational stance); the premise that import-mixing without compatibility checks is epistemically risky. These are asserted, not derived — disclosed here as the load-bearing floor. |

## 3. Phases with WBS

| Phase | WBS Step | Content |
|---|---|---|
| P0 | `[QNFO.RES.015.P0]` | Initialization: WBS resolve, branch, PROJECT-PLAN, core-claim lock, UIA on core claim, commit/tag/push, registry row. |
| P1 | `[QNFO.RES.015.P1]` | Due diligence: full-corpus sweep (≥3 query formulations/topic, limit ≥20), cross-system ID validation, ≥2 adjacent WBS domains, external verification (arXiv/Crossref/archive.org). |
| P2 | `[QNFO.RES.015.P2]` | Structure: import-provenance table for spiders/Pauli webs/gadgets; compatibility audit; seam catalog; gap analysis. |
| P3 | `[QNFO.RES.015.P3]` | Citations: extract, verify BibTeX (P3.AUTHOR-GATE), auto-generate missing DOIs, citation-audit.md. |
| P4 | `[QNFO.RES.015.P4]` | Research: fault-line synthesis, premise-depth disclosure finalization, red-team, calibration register. |
| P5 | `[QNFO.RES.015.P5]` | Publish: `<slug>.md` + PDF (pandoc→MathJax→puppeteer) + publication gates (plain scholarly prose — PUBLICATION-PROSE-GATE-1) + Zenodo DOI. |
| P6 | `[QNFO.RES.015.P6]` | Deploy: D1 living-paper, papers-server Worker, MCP-driven verification. Core claim locked. |
| P7 | `[QNFO.RES.015.P7]` | Disseminate: papers.qnfo.org, Internet Archive, social (user-gated). |
| P8 | `[QNFO.RES.015.P8]` | Distribute: GitHub tag, Zenodo newversion as needed, R2 mirror to `qnfo-releases` (R2-MIRROR-AFTER-PUBLISH-1), D1/KG records. |

## 4. Milestones with Gate Criteria

| Milestone | Gate criteria (all must pass) |
|---|---|
| M0 Phase-0 close | Branch pushed; PROJECT-PLAN.md with WBS first line; core claim locked; UIA artifact written; tag `v0.1-phase0-res015` on remote; registry row inserted (atomic). |
| M1 Due-diligence close | ≥3 distinct query formulations per topic executed with evidence files; ≥2 adjacent WBS domains swept; external verification evidence saved under `artifacts/external-search/`. |
| M2 Structure close | Import-provenance table complete for all 3 constructs; compatibility audit per import pair; seam catalog non-empty; gap analysis written. |
| M3 Citation close | 100% of bibliography entries verified real/correct/context-appropriate (citation-audit.md clean). |
| M4 Research close | Red-team findings resolved; calibration register populated; premise-depth disclosure final. |
| M5 Publish close | Plain-prose publication text; all source files deposited (PUBLICATION-SOURCE-COMPLETENESS-1); DOI resolves. |
| M6 Deploy close | D1 living-paper row live; Worker serves paper; MCP verification pass. |
| M8 Distribute close | R2 mirror verified in `qnfo-releases/YYYY/MM/zx-diagram-fault-lines/`; KG `distribution_status: distributed`. |

## 5. Deliverable Registry

| Deliverable | Path | Phase |
|---|---|---|
| PROJECT-PLAN.md | `zx-diagram-fault-lines/PROJECT-PLAN.md` | P0 |
| Universal Ignorance Audit on core claim | `zx-diagram-fault-lines/artifacts/universal-ignorance-audit.md` | P0 |
| Deep research + gap analysis | `zx-diagram-fault-lines/docs/deep-research.md` | P1–P2 |
| Import-provenance + seam catalog | `zx-diagram-fault-lines/docs/import-provenance.md` | P2 |
| Main paper (.md/.html/.pdf) | `zx-diagram-fault-lines/zx-diagram-fault-lines.{md,html,pdf}` | P5 |
| references.bib + citation-audit.md | `zx-diagram-fault-lines/references.bib`, `citation-audit.md` | P3 |
| Evidence files | `zx-diagram-fault-lines/artifacts/external-search/*` | P1 |
| Zenodo record | TBD DOI | P5 |

## 6. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| WBS collision with concurrent session (WBS-COLLISION-2) | Medium | Medium | Atomic check-then-insert in one D1 INSERT; renumber on UNIQUE violation. |
| Cafeteria critique becomes cafeteria itself (importing QNFO locale lens without compatibility audit) | Medium | High | UIA Q10 held explicitly; premise-depth disclosure names the framing's own primitives. |
| External literature already contains the compatibility audit (claim pre-empted) | Medium | High | P1 full-corpus sweep + arXiv/Crossref external search; if found, reframe as synthesis/survey with citation. |
| Misreading "internal validity" as "no physical bearing" (straw-manning ZX) | Medium | Medium | Claim is scoped to *unestablished* bearing — an absence claim, falsifiable by finding the compatibility audit. |
| Subagent truncation during red-team | Medium | Low | Direct parent-agent audit fallback (REVIEWER-BOUNDED-WAIT-1). |

## 7. Success Criteria

1. Import-provenance of spiders, Pauli webs, and gadgets is tabled with cited sources per silo.
2. The seam (map ends / territory begins) is stated concretely per construct, not rhetorically.
3. The cafeteria-problem generalization is argued with ≥1 non-QM worked illustration.
4. A reader finishes knowing exactly which claims are derived, which are imported, and where the premises end.
5. Publication passes all pipeline gates and is written in plain scholarly prose (PUBLICATION-PROSE-GATE-1).

## 8. SO-WHAT-GATE

**Why a reader should care:** ZX diagrams are not a niche notation — they are the workhorse
language of modern quantum compilation, optimization, and error correction, and they are taught
as *the* intuitive picture of quantum processes. If the constructs are cafeteria imports with
unprobed seams, then a large practitioner community is conflating a convenient 2D map with 3+1D
physical reality, and the failure mode is silent because the map's internal validity is real.
Naming the seam — and giving an import-provenance audit method — lets practitioners keep using
the diagrams while knowing exactly where the map stops. The generalization (cafeteria imports
across siloed disciplines) matters to every field that borrows tools from neighbors when
convenient.

**Premise-depth disclosure:** see §2 table. The premises END at: (a) the imported ZX/stabilizer/
MBQC mathematics (asserted, not re-derived); (b) the representational stance that formalisms can
be about physical reality; (c) the epistemic-risk premise that unchecked import-mixing is
dangerous. Everything else in the paper is derived or externally verified, and the boundary is
stated in the paper's prose.
