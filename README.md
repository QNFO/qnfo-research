# The Consilience of the QNFO Keyword Taxonomy: Ultrametric Structure as a Testable Compression Prior

**Author:** Rowan Brad Quni-Gudzinas
**Affiliation:** QNFO
**Version:** v1.0 — 2026-08-23
**License:** CC BY 4.0
**DOI:** 10.5281/zenodo.22071421

## How to cite

Cite all versions via the concept DOI — it always resolves to the latest version:

> Quni-Gudzinas, Rowan Brad. (2026). *The Consilience of the QNFO Keyword
> Taxonomy: Ultrametric Structure as a Testable Compression Prior* (v1.0).
> QNFO. https://doi.org/10.5281/zenodo.22071420

## Abstract

The QNFO research program spans seven domains — ultrametric physics, the laws
of form, infomatics, paradigm engineering, consilience research, the QWAV
platform, and interactive demos — and maintains a canonical keyword taxonomy
of 335 terms used to scope external discovery. This paper subjects the
program's consilience claim to a computational audit of that vocabulary. The
taxonomy is strictly partitional: 334 of 335 keywords occur in exactly one
program, one keyword occurs in two, and none occurs in three or more. The
consilience claim is therefore not a lexical fact about the taxonomy; it is a
semantic claim carried by bridge families, by the taxonomy's explicit
cross-cutting themes, and by corpus-level links between published records.
The paper states the revised claim, three falsifiable hypotheses with
disconfirmation criteria, three practitioner-facing deliverables, and binds
the strong form of the program to a 2028 decision point. All quantitative
claims are computationally verified by a deterministic, seeded verification
suite deposited with the paper.

## Deposit contents

| File | Description |
|:-----|:------------|
| `keyword-taxonomy-consilience.md` / `.html` / `.pdf` | The paper (v1.0) |
| `references.bib` | Full bibliography (21 entries, citation-audited) |
| `citation-audit.md` | P6 citation audit — every DOI/arXiv ID verified (DataCite + Zenodo) |
| `README.md` | This file |
| `PROJECT-PLAN.md` | Project plan with the locked core claim, premise chain L0–L5, disconfirmation criteria |
| `docs/deep-research.md` | Consolidated due diligence (full-corpus sweep, cross-system ID validation, external verification) |
| `docs/red-team-p5-2026-08-23.md` | P5 red-team aggregate report (4 HARD / 12 SOFT; number chain CLEAN) |
| `docs/QNFO-KEYWORD-TAXONOMY.md` | The audited taxonomy (v1.0, canonical source) |
| `artifacts/universal-ignorance-audit.md` | Universal Ignorance Audit (15 questions) on the core claim |
| `artifacts/due-diligence-phase1.md` | Phase-1 due-diligence + gap analysis |
| `artifacts/p2-consilience-map.md` / `.json` | RQ5 analysis + machine-readable consilience graph (342 nodes, 336 edges) |
| `artifacts/external-search/` | arXiv evidence files (Phase 1 + G5 closure) |
| `artifacts/verification/` | Full verification suite: rq1–rq5 scripts, results, run logs, pinned corpora, gate checks |

## Source & provenance

- **Repository:** https://github.com/QNFO/qnfo-research
- **Branch:** `res/paper/keyword-taxonomy-consilience` (tags
  v0.1-phase0-res022 … v0.5-phase5-res022)
- **Canonical taxonomy:** `docs/QNFO-KEYWORD-TAXONOMY.md` v1.0 (2026-08-05),
  also archived at `artifacts/verification/keyword-taxonomy-source.md`
  (byte-identical at fetch time).
- **Predecessor records:** QNFO.CON.001 (10.5281/zenodo.21547793),
  QNFO.CON.002 (10.5281/zenodo.21804073).

## Reproducibility

Every quantitative claim is produced by deterministic, seeded scripts in
`artifacts/verification/` (pure Python standard library, fixed seed
20260823): `rq5_keyword_load.py` (taxonomy audit), `rq1_retrieval_benchmark.py`
(H1), `rq2_consilience_links.py` (RQ2), `rq3_archimedean_limit.py` (H2),
`rq4_noise_scaling.py` (H3). Re-running from the repository root regenerates
all JSON artifacts byte-identically. Corpus statistics (8,324 nodes; 1,660
papers) were read from the program's knowledge-graph endpoint on 2026-08-23.
