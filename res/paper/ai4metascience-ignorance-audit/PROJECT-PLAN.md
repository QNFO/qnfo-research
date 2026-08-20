# PROJECT-PLAN — AI4MetaScience @ NeurIPS 2026 Position Paper

**Slug:** ai4metascience-ignorance-audit · **Branch:** res/paper/ai4metascience-ignorance-audit
**Owner:** Rowan Brad Quni-Gudzinas (QNFO) · **Deadline:** 2026-08-29 AoE (OpenReview)

## Objective

Submit an 8-page position paper to the AI for Meta-Science workshop at NeurIPS 2026
(Paris, December 2026) built from the published QNFO records: Universal Ignorance Audit
(10.5281/zenodo.21901984), Knowing What We Do Not Know (10.5281/zenodo.21901983), and the
flagship case record The Ultrametric Foundation (10.5281/zenodo.21208346). Position:
epistemic legibility (provenance, ignorance, auditor) as the unit of governance for
AI-assisted science; six transferable principles mapped to the workshop agenda.

## Deliverables

1. `position-paper.md` — canonical source (draft v0.1, 2026-08-18)
2. `neurips_2026.tex` + `neurips_2026.sty` — NeurIPS 2026 LaTeX template source (position track)
3. `references.bib` — verified bibliography
4. `position-paper.html` / `position-paper.pdf` — approved-pipeline render (pandoc → MathJax SVG inline → puppeteer; PYMUPDF-FORBIDDEN-1)
5. `citation-audit.md` — this paper's citation audit (2026-08-18)
6. `README.md` — CFP facts + pipeline state

## Milestones

| # | Milestone | State | Date |
|---|---|---|---|
| 1 | CFP verified live (ai4metascience.org) | ✅ | 2026-08-18 |
| 2 | Draft v0.1 (md) | ✅ | 2026-08-18 |
| 3 | LaTeX conversion (.tex/.sty) | ✅ | 2026-08-18 |
| 4 | Citation audit (live APIs) | ✅ | 2026-08-18 |
| 5 | CMD RED TEAM (3 reviewers) + HARD fixes | ✅ | 2026-08-18 |
| 6 | OpenReview submission | ✅ 2026-08-20 (#17, note 6lmtqUoIbj) |
| 7 | Zenodo deposit + R2 mirror + KG update | ✅ 2026-08-20 (DOI 10.5281/zenodo.22026592) |

## Gates (all standing)

- PUBLICATION-PROSE-GATE-1 — no internal pipeline vocabulary in publication text (verified)
- SO-WHAT-GATE-1 — abstract carries why-a-reader-should-care + premise depth (verified)
- PRACTITIONER-RELEVANCE-1 — Section 5 maps principles to practitioner actions (AI reviewers, verification tools, publication criteria) (verified)
- NO-JOURNALS-1 — workshop submission only; Zenodo canonical (verified)
- R2-MIRROR-AFTER-PUBLISH-1 / WRONG-BUCKET-SELECTION-1 — mirror to qnfo-releases after deposit
- ZENODO-PLACEHOLDER-DOI-1 — verify uploaded file free of <RESERVED> before publish
- ZENODO-CONCEPT-DOI-CITE-1 — How-to-Cite uses concept DOI
- POST-PUBLICATION ADVERSARIAL ANALYSIS GATE — post-deposit audit cycle
- QNFO/QWAV NAMING MANDATE-1 — full name "Rowan Brad Quni-Gudzinas" (verified)

## Known decisions

- PDF build uses the QNFO-approved pipeline (pandoc → MathJax SVG inline → puppeteer-core
  page.pdf), NOT pdflatex — PYMUPDF-FORBIDDEN-1 (HARD user gate). The template-compliant
  neurips_2026.tex is shipped as the canonical LaTeX source alongside the rendered PDF.
- Identified (non-anonymous) submission — verified workshop is NOT blinded via OpenReview API.
