# WBS: QNFO.RES.016

# Post-Quantum Synthesis Critique Adjudication

**Slug:** `pqs-critique-adjudication` — **Branch:** `res/paper/pqs-critique-adjudication` — **Repo:** QNFO/qnfo-research
**Status:** Phase 4 (Adjudication draft v0.1) — **Date:** 2026-08-19

---

## 1. Charter

The QNFO corpus contains the Post-Quantum Synthesis (PQS) program — a critical reconstruction
of von Neumann's quantum axioms on Kolmogorovian, measure-theoretic grounds (hydrodynamic
stability, Radon–Nikodym probability fluids, ultrametric/non-Archimedean syntax). Two Obsidian
seed notes (`_26231071019.md`, `_26231071320.md`, 2026-08-19) present (a) a summary of the PQS
critique of von Neumann and (b) a five-point red-team critique of PQS itself:
chronological fallacy, unexplained measurement mechanism, spectral-divergence contradiction,
non-Archimedean overhaul, and an overall "ambitious but unsubstantiated" verdict.

**This project adjudicates the red-team critique.** Each of the five points is graded
CONFIRMED / PARTIALLY CONFIRMED / UNSUPPORTED / CONTRADICTED against primary literature
(von Neumann 1932, Kolmogorov 1933, Madelung 1926–27, Radon–Nikodym 1913, projection-postulate
analysis, ultrametric/p-adic QFT lineage incl. Vladimirov–Volovich), the PQS source papers
(SSRN 5809662, SSRN 5821702, PhilPapers QUNTCI/QUNANS/QUNTUP), and the QNFO internal corpus
(~1,600 papers; full sweep per DUE-DILIGENCE-DEPTH-1). Symmetric audit (KIF-29/KIF-60) applies
to both the critique and the framework: the critique's own factual premises are verified with
the same standard it demands of PQS.

**Why a reader should care:** the red-team note is an example of a recurring failure mode in
AI-assisted adversarial review — a critique that demands falsifiability from a framework while
asserting its own historical and physical premises without evidence. An adjudication that grades
each point with live primary-source verification shows which criticisms survive scrutiny and
which rest on the same god-of-the-gaps reasoning they accuse PQS of. It is also the standing
enforcement of the publish-then-audit loop: the corpus' own claims get the same adversarial
treatment.

## 2. Core Claim (P6 — LOCKED)

> **CC-1:** The five-point red-team critique of PQS is of *mixed validity*: each point can be
> independently graded against primary sources, and **at least two of the five points fail a
> symmetric evidence standard** — their own premises are historically incomplete, physically
> unverified, or misattribute the burden of proof (e.g., the chronology claim misreads the
> 1929–1933 historical record; the "quantization is real" point conflates spectral discreteness
> with the measurement-dependence of state reduction).

**Premise-depth disclosure (SO-WHAT-GATE):** The adjudication's derived claims rest on two
named imported inputs: (i) the historical record as documented by primary texts and
contemporary secondary scholarship (von Neumann 1932; Kolmogorov 1933; published histories of
probability theory), and (ii) the PQS source texts as deposited (SSRN/PhilPapers records cited
in the seed notes). Claims about what PQS "asserts" go as deep as those texts; claims about
what history "shows" go as deep as the cited primary sources and their archival verification
(archive.org CDX, Crossref/OpenAlex metadata). The adjudication does NOT itself resolve the
measurement problem; it grades whether the critique's objections to a proposed resolution are
factually grounded. That is where the premises END.

**Disconfirmation condition (falsifiability gradient):** CC-1 is disconfirmed if independent
verification shows 4–5 of the five critique points fully confirmed by primary sources with no
material counter-evidence, i.e., the critique's premises all check out. CC-1 is confirmed if
≥2 points fail verification of their own premises.

## 3. Phases with WBS

| WBS | Phase | Deliverable | Gate |
|:----|:------|:------------|:-----|
| QNFO.RES.016.P0 | Init (this file) | Branch, PROJECT-PLAN.md, locked CC-1, registry row, tag v0.1-phase0 | P1–P8 HARD pre-flight |
| QNFO.RES.016.P0.5 | ZENODO-INQUIRY-1 | Universal Ignorance Audit (15 Q) on CC-1 | UIA administered, answers written |
| QNFO.RES.016.P1 | Due diligence | Corpus sweep + external verification + gap analysis | DUE-DILIGENCE-DEPTH-1 (≥3 formulations/topic, resolve_paper_id per hit, ≥2 WBS domains, evidence files) |
| QNFO.RES.016.P1b | Consilience gate | Cross-domain lexicon + silo-cost table + KIF-60 evidential weight | KIF-29 HARD; artifacts/consilience-gate.md |
| QNFO.RES.016.P2 | Literature & triage | 8-source search, classification, Mandatory Symmetry Template (KIF-18) | KIF-18 both sections present |
| QNFO.RES.016.P3 | Citations | references.bib verified live (P3.AUTHOR-GATE) | 0 fabricated entries |
| QNFO.RES.016.P4 | Deep research | Point-by-point adjudication draft + calibration + practitioner section | PRACTITIONER-RELEVANCE-1 |
| QNFO.RES.016.P5 | Publication | `<slug>.md/.html/.pdf` + Zenodo + full source set | PUBLICATION-SOURCE-COMPLETENESS-1, P5.FRESH, language gate |
| QNFO.RES.016.P6 | Deploy | D1 insert, KG node, Vectorize index | PUBLICATION-KG-INDEX-GAP-1 |
| QNFO.RES.016.P7 | Disseminate | papers.qnfo.org, Buffer, communities, archive | Phase 7 protocol |
| QNFO.RES.016.P8 | Distribute | R2 mirror qnfo-releases + closeout verification | R2-MIRROR-AFTER-PUBLISH-1, 7-layer closeout |

## 4. Milestones with gate criteria

| # | Milestone | Gate criteria |
|:--|:----------|:--------------|
| M0 | Phase 0 complete | P1–P8 pre-flight pass; branch pushed; tag `v0.1-phase0` verified via ls-remote; RES.016 row in portfolio-state |
| M1 | Due diligence complete | Stats query + ≥3 formulations × ≥3 topics (limit 20/16), ID validation, ≥2 domains, evidence files in artifacts/external-search/ |
| M2 | Adjudication draft | Each of 5 critique points graded with ≥1 primary source + corpus evidence; KIF-18 symmetry; SO-WHAT + practitioner section |
| M3 | Publication complete | Zenodo DOI live (doi.org 200), R2 mirror, D1/KG/Vectorize verified, post-publication adversarial analysis dispatched |

## 5. Deliverable Registry

| ID | Deliverable | Path | Status |
|:---|:------------|:-----|:-------|
| D1 | PROJECT-PLAN.md (this file) | pqs-critique-adjudication/PROJECT-PLAN.md | ✅ Phase 0 |
| D2 | UIA administration record | artifacts/universal-ignorance-audit.md | ✅ P0.5 |
| D3 | Due-diligence evidence (all API responses + corpus sweep) | artifacts/external-search/*.json (30 files) | ✅ P1+P2 |
| D4 | Cross-system ID validation report | artifacts/cross-system-id-validation.md | ✅ P1 |
| D5 | Consilience gate + KIF-60 evidential weight (folded in) | artifacts/consilience-gate.md | ✅ P1b |
| D6 | Gap analysis + SO-WHAT + premise-depth | artifacts/gap-analysis.md | ✅ P1 |
| D7 | Adjudication paper draft `<slug>.md` (practitioner §10) | pqs-critique-adjudication.md | ✅ P4 draft v0.1 |
| D8 | Published paper `<slug>.md/.html/.pdf` | releases/ | pending P5 |
| D9 | references.bib (22 verified) + citation-audit.md | references/ + artifacts/ | ✅ P3 |
| D10 | RESEARCH-CONTINUITY-REGISTRY.md (FQ/predictions/pre-reg) | pqs-critique-adjudication/RESEARCH-CONTINUITY-REGISTRY.md | ✅ P4 |
| D11 | Outreach/audit evidence log | artifacts/outreach-log.md | pending P7 |

## 6. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Seed notes' citations (SSRN/PhilPapers IDs) unresolvable | Medium | High | External verification via Crossref/OpenAlex/archive.org CDX; label `[UNVERIFIED]` rather than assume |
| Corpus hits all internal → confirmation bias | Medium | Medium | KIF-17 flag; external 8-source search mandatory; Mandatory Symmetry Template |
| Critique/framework dispute over interpretive claims (measurement problem) | Certain | Medium | Grade factual premises vs. interpretive claims separately; KIF-16 neutral epistemic labels |
| WBS collision with concurrent session | Low | High | Atomic check-then-insert; row identity re-verified before writes (WBS-COLLISION-2) |
| Zenodo API 403/bot-filter | Medium | Medium | Browser-context fetch / full Chrome UA per ZENODO-BOT-403-1 |

## 7. Success Criteria

1. Each of the 5 critique points graded CONFIRMED / PARTIALLY CONFIRMED / UNSUPPORTED / CONTRADICTED with live primary-source evidence (a count without its evidence file does not exist).
2. CC-1 adjudicated: ≥2 points fail symmetric evidence standard, or CC-1 explicitly disconfirmed with the evidence shown.
3. Every cited source verified in-session (three-count audit: queried ≥ received ≥ cited).
4. Publication reaches Zenodo + R2 + D1/KG/Vectorize with all source files (PUBLICATION-SOURCE-COMPLETENESS-1).
5. Post-publication adversarial analysis dispatched (Accuracy/Completeness/Dependency) and findings logged.

## 8. Practitioner Relevance (PRACTITIONER-RELEVANCE-1)

**What can a practitioner DO with this result?** A decision tool: a per-claim validity register
(claim → evidence grade → actionable conclusion) usable by (a) AI-assisted research pipelines
that need to distinguish substantive critiques from premise failures before revising frameworks;
(b) grant/patent reviewers screening foundation-level claims; (c) QNFO's own pipeline as the
standing adversarial-validation gate. The grading rubric (CONFIRMED/PARTIALLY/UNSUPPORTED/
CONTRADICTED with required evidence class per grade) is directly reusable as a checklist —
no niche terminology required beyond the four grade labels, each anchored to an evidence
standard defined in the paper within two sentences of first use.

---

## Appendix: Seed notes (input corpus)

- `D:\Obsidian\notes\v1\2026\08\19\_26231071019.md` — PQS summary w/ citations (SSRN 5809662, 5821702; PhilPapers QUNTCI, QUNANS, QUNTUP; arXiv 1112.1507; Cambridge/ScienceDirect/Springer refs)
- `D:\Obsidian\notes\v1\2026\08\19\_26231071320.md` — 5-point red-team critique of PQS
