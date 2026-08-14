# WBS: QNFO.RES.008

# Formal Self-Reference Limits — Project Plan

**Project:** Formal Self-Reference Limits — why formal quantitative systems are "uncomfortable" with self-reference despite their anthropocentric origins, and what this implies for self-knowledge
**WBS:** QNFO.RES.008
**Program:** QNFO.RES (QNFO Research Archive)
**Repo:** QNFO/qnfo-research
**Branch:** res/paper/formal-self-reference-limits
**Slug:** formal-self-reference-limits
**Seed note:** D:\Obsidian\notes\v1\2026\08\14\_26226072743.md (70,556-char reasoning draft)
**Created:** 2026-08-14
**Status:** Phase 0 (scaffold)

---

## §1 Charter

### §1.1 Problem

The seed question (2026-08-14 daily note): **"Why are our formal quantitative systems uncomfortable with self-reference when they are also inherently anthropocentric, from base-10 pentadactylity to length of time (heartbeat Hertz) and space? Can we not truly see ourselves?"**

The tension: our formal systems (mathematics, logic, computation) are built by embodied, self-referential agents and carry anthropocentric traces (decimal notation from ten fingers, the second near a heartbeat, the meter from the Earth/body), yet they exhibit systematic *discomfort* with self-reference — the liar paradox, Russell's paradox, Gödel incompleteness, Tarski's undefinability, the halting problem. The naive intuition is that systems built by self-referential beings should be *at home* with self-reference; the observed reality is that unrestricted self-reference destabilizes them.

### §1.2 Locked Core Claim (P6)

**The discomfort of formal quantitative systems with self-reference is a structural consequence of objectification, not a defect of anthropocentric origin: a formal system is a third-person map, and it can represent itself only at the cost of incompleteness or inconsistency (Gödel, Tarski), while its anthropocentric traces (base-10 notation, heartbeat-second, body-meter) are convention-layer residues that never enter the formal core. Consequently, "truly seeing ourselves" is possible only as partial self-representation through meta-levels — true but never total, consistent only when stratified.**

Falsifiability condition: the claim is disconfirmed by exhibiting a sufficiently strong, consistent, recursively axiomatizable formal system that defines its own truth predicate and proves all its own true statements (contradicts Tarski/Gödel, would be a landmark result), OR by demonstrating an anthropocentric convention that changes a formal theorem rather than only its representation (e.g., arithmetic whose theorems depend on base choice).

Distinction from the map–territory canon (KIF-60 / MAP-TERRITORY-1): the seed note's answer is NOT merely "the map is not the territory" — the novel contribution is the *objectification thesis*: formal systems exclude the observer at the foundation by design (third-person stance), so self-reference is not a representational accident but the price of that exclusion; and the *partial-self-knowledge corollary*: we see ourselves truly but never totally, because a total self-model requires an outside.

### §1.3 Scope

- Formal systems: classical first-order arithmetic, set theory (ZF/Russell), lambda calculus/Turing machines, Tarski truth predicates, Gödel numbering.
- Anthropocentric traces: decimal/base-10 notation, SI second vs heartbeat (~1 Hz), meter vs Earth meridian — treated as *convention-layer* residues that are base/unit-independent in the formal core.
- Self-knowledge corollary: partial self-representation via meta-levels (Gödel sentence as self-referential-but-true-from-outside; quines; reflection principles).
- Out of scope (deferred): full philosophy-of-mind treatment of consciousness; formal treatment of paraconsistent logics beyond a survey mention; no new logic systems proposed.

---

## §2 Phases with WBS

| Phase | WBS | Milestone | Gate criteria |
|:------|:----|:----------|:--------------|
| 0 | QNFO.RES.008.P0 | Scaffold | Branch, PROJECT-PLAN.md, P6 locked, committed/tagged/pushed |
| 1 | QNFO.RES.008.P1 | Due diligence | KG + full-corpus + external search, gap analysis, KIF-29 consilience gate, evidence files in artifacts/external-search/ |
| 2 | QNFO.RES.008.P2 | Draft | Seed note distilled into formal paper draft (MD) with references |
| 3 | QNFO.RES.008.P3 | Author gate | Citation integrity (P3.AUTHOR-GATE), no fabrication risks |
| 4 | QNFO.RES.008.P4 | Red-team | 5-adversary + UIA 15Q audit; HARD findings fixed |
| 5 | QNFO.RES.008.P5 | Publication | Zenodo deposit (all source files + GitHub provenance), D1, Vectorize, KG node, papers.qnfo.org |
| 6 | QNFO.RES.008.P6 | Distribution | 4-D: IPFS/Arweave/DNSLink/Internet Archive, R2 archive, IndexNow |
| 7 | QNFO.RES.008.P7 | Closeout | Consolidated verification, memory log, tags |

---

## §3 Milestones with Gate Criteria

1. **M1 (Phase 0 complete):** branch `res/paper/formal-self-reference-limits` on origin; PROJECT-PLAN.md with WBS header + P6; tag `v0.1-phase0` pushed.
2. **M2 (Phase 1 complete):** `query_graph(stats)` evidence; >=3 search_papers formulations (limit 20); search_papers_enriched + recall_facts + KG neighbor walks; >=2 adjacent WBS domains; external search (OpenAlex/Crossref/arXiv) evidence saved; gap analysis states the novel contribution vs prior literature.
3. **M3 (Phase 2 complete):** `<slug>.md` draft that directly answers the seed question with the objectification thesis and partial-self-knowledge corollary; references.bib; citation-audit.md.
4. **M4 (Phases 3-4 complete):** author gate + red-team pass with zero HARD findings.
5. **M5 (Phases 5-6 complete):** Zenodo DOI live; all source files included; D1 row + Vectorize chunks + KG node verified.
6. **M6 (Phase 7 complete):** closeout verification (doi.org HEAD, DataCite findable, GitHub branch/tag, D1 re-query, KG + Vectorize presence) all pass.

---

## §4 Deliverable Registry

| Deliverable | Path | Status |
|:------------|:-----|:-------|
| PROJECT-PLAN.md | formal-self-reference-limits/PROJECT-PLAN.md | DRAFT (this file) |
| Paper draft (MD) | formal-self-reference-limits/formal-self-reference-limits.md | pending |
| HTML render | formal-self-reference-limits/formal-self-reference-limits.html | pending |
| PDF (CDP pipeline only) | formal-self-reference-limits/formal-self-reference-limits.pdf | pending |
| references.bib | formal-self-reference-limits/references.bib | pending |
| citation-audit.md | formal-self-reference-limits/citation-audit.md | pending |
| External search evidence | formal-self-reference-limits/artifacts/external-search/ | pending |
| Deep research doc | formal-self-reference-limits/docs/deep-research.md | pending |

---

## §5 Risk Register

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Novelty gap (topic covered by existing philosophy-of-math literature — self-reference limits are classical) | HIGH | MEDIUM | Phase 1 gap analysis must isolate the *objectification thesis* + *partial-self-knowledge corollary* as the specific contribution; cite Tarski/Gödel/Quine/Priest honestly; if fully covered, narrow to the anthropocentrism link |
| MAP-TERRITORY-1 conflation (paper reads as "map is not territory" truism) | HIGH | MEDIUM | P6 locked with the objectification thesis; Phase 4 red-team checks label discipline; disconfirmation condition stated |
| Citation fabrication (philosophy canon — names/works easily misremembered) | MEDIUM | HIGH | P3.AUTHOR-GATE: every reference verified against primary source (arXiv/OpenAlex/Crossref/PhilPapers); no unverified attributions |
| Seed note verbosity (70K-char reasoning trace) | MEDIUM | LOW | Distill to the final answer's structure (maps vs territory, convention-layer vs formal core, partial self-representation); keep the trace in artifacts/ as provenance |

---

## §6 Success Criteria

1. Core claim P6 (objectification thesis) stated and defended with the classical formal results (Gödel incompleteness, Tarski undefinability, halting problem) and the anthropocentrism analysis.
2. The seed question answered explicitly: yes, we can see ourselves — truly, partially, and only through meta-levels.
3. Zero HARD findings at red-team; citation-audit clean (all references cited, all cited references listed).
4. Published with full source-file completeness (PUBLICATION-SOURCE-COMPLETENESS-1): .md/.html/.pdf + references.bib + citation-audit.md + PROJECT-PLAN.md + README.md + docs/deep-research.md + artifacts/external-search/* + GitHub provenance (related_identifiers isSupplementTo).
5. D1 living-paper row, Vectorize index, KG node with BELONGS_TO edge, R2 archive — all verified same-turn (v2.96 gates).

---

## §7 Cross-References

- **Anchor/adjacent QNFO records:** RES.002 Universal Ignorance Audit (10.5281/zenodo.21901984 — audit-before-asserting methodology applies); RES.003 Knowing What We Do Not Know (10.5281/zenodo.21901983 — AI-assisted pipeline epistemic lessons); QUNSAI Scaffolds and Invariants (10.5281/zenodo.21255344 — epistemic hygiene, pi/number-bases/geometric centers, directly adjacent to base-10 anthropocentrism); RES.005 Prime Valuation Depth (10.5281/zenodo.21918838 — depth/measure vocabulary).
- **Gates:** KIF-29 (consilience), KIF-60 (map–territory labels), MAP-TERRITORY-1, P3.AUTHOR-GATE, DUE-DILIGENCE-DEPTH-1, PUBLICATION-SOURCE-COMPLETENESS-1, CDP-only PDF pipeline.
- **Repo:** QNFO/qnfo-research, branch res/paper/formal-self-reference-limits.
