# PROJECT PLAN — Terminology Silos and the Consilience Gap

**WBS:** `QNFO.CGS.002` (program: QNFO.CGS — Consilient Gap Synthesis)
**Branch:** `res/paper/terminology-silos-consilience` (repo: QNFO/qnfo-research)
**Created:** 2026-08-24
**Status:** P5 (publication) — v1.0 published 2026-08-24, DOI 10.5281/zenodo.22075544 (concept 22075543)

## 1. Origin and mandate

User directive (2026-08-24): the keyword-taxonomy audit reported in §5.1 of
"The Ultrametric Program: One Structural Object Across Seven Research Domains,
and Its Falsifiable Tests" (10.5281/zenodo.22073477, v2.4) deserves its own
spinoff research. The audit (predecessor record 10.5281/zenodo.22071421) found
that the QNFO program's own keyword taxonomy is strictly partitional — 334 of
335 keywords occur in exactly one of seven research domains, the shared
(load-bearing) vocabulary core is empty, and bridge vocabulary shows no
enrichment (Fisher exact test p = 1.0). The consilience claim is semantic, not
lexical.

The general phenomenon behind that single-case result: **domain-specific
terminology silos**. Scientific fields maintain largely disjoint vocabularies;
shared vocabulary is rare; and the absence of a shared vocabulary is both a
symptom and a reinforcing cause of missing interdisciplinary consilience.
This is an important/critical theme holding back large-scale scientific
progress: connections between fields are discovered despite their vocabularies,
not through them.

This project generalizes the QNFO audit into a quantitative, externally
verified study of terminology silos, and develops the consilience
infrastructure response (bridge vocabularies, taxonomy engineering, semantic
mapping).

## 2. Mission alignment

QNFO.CGS — Consilient Gap Synthesis: identify and close gaps between research
domains. Terminology silos are the lexical layer of every consilience gap.
The QNFO program (seven domains, one structural object) is simultaneously the
worked example and the first testbed: its taxonomy audit is the seed dataset,
and its corpus provides the semantic-bridge evidence (corpus-level links that
carry meaning across program boundaries without shared keywords).

## 3. Research questions

- **RQ1 — How partitioned is scientific vocabulary?** Compute the
  partitionality index (fraction of keywords occurring in exactly one domain),
  the shared-core size (keywords in >=3 domains), and bridge share across an
  external sample of scientific domains with curated keyword sets.
- **RQ2 — What is the structure of bridge vocabulary?** Are shared terms
  concentrated in structurally general families (hierarchy, measure, order,
  transformation) or uniformly distributed? Fisher exact enrichment test on
  the bridge x family contingency.
- **RQ3 — Why do silos persist?** Evidence-based mechanism analysis:
  incentive structures, field-local prestige economies, vocabulary
  gatekeeping by venues, translation costs, path dependence in taxonomy
  formation.
- **RQ4 — What does the silo cost science?** Framework for the cost of missed
  cross-domain connections: duplicated discovery, delayed convergence,
  invisible correspondences. Measurable proxies: lexical overlap of
  semantically linked records, cross-domain citation rates.
- **RQ5 — What consilience infrastructure works?** Bridge vocabularies as
  first-class research infrastructure; taxonomy engineering (the QNFO
  taxonomy's explicit bridge subsections and cross-cutting themes as a worked
  example); semantic mapping between field vocabularies.

## 4. Hypothesis cards (pre-registered)

### H-SILO-1 — Partitionality is the norm in science
- **Claim:** in any sample of >=6 scientific domains with curated keyword
  vocabularies, at least 90% of keywords occur in exactly one domain.
- **Prediction:** partitionality_index >= 0.90 on the external arXiv-domain
  sample.
- **Falsifier:** partitionality_index < 0.90.
- **Surprisal:** moderate — naive expectation from interdisciplinary rhetoric
  would be substantial sharing (>=20% shared).

### H-SILO-2 — Bridge vocabulary is rare and structurally biased
- **Claim:** shared keywords are a small fraction of total vocabulary (<10%)
  and are enriched in structurally general concept families (hierarchy,
  measure, order, transformation, information) relative to domain-specific
  constructs.
- **Prediction:** bridge_share < 0.10; Fisher exact enrichment p < 0.05 for
  the general-family contingency.
- **Falsifier:** bridge_share >= 0.10 or p >= 0.05 (bridges uniformly
  distributed).
- **Surprisal:** low-moderate — the QNFO case (bridge share 0.0-0.55 per
  program, 53 bridge terms of 335) suggests the pattern holds.

### H-SILO-3 — Semantic consilience is invisible to lexical matching
- **Claim:** cross-domain correspondences (one structural object, different
  names) carry no keyword-level signature: records that are semantically
  linked across QNFO programs have keyword overlap no higher than unlinked
  pairs.
- **Prediction:** mean pairwise keyword overlap of semantically linked
  cross-program record pairs <= overlap of random pairs (difference < 0.05).
- **Falsifier:** linked pairs show significantly higher keyword overlap.
- **Surprisal:** high — if semantic links were lexically visible, keyword
  search alone would discover cross-domain consilience, which the QNFO audit
  (p = 1.0 enrichment null) contradicts.

## 5. Method

1. **Measurement toolkit (P1):** Python module implementing the partitionality
   index, shared-core size, bridge share, and Fisher exact enrichment test —
   the exact quantities from the QNFO audit (RQ5), generalized to arbitrary
   domain-keyword partitions. Seed: the QNFO taxonomy (335 keywords, 7
   programs).
2. **External evidence (P1):** sample recent abstracts from >=6 arXiv
   categories (quant-ph, math.NT, cs.LG, q-bio.GN, cond-mat.mtrl-sci,
   stat.ML, econ.TH), extract per-category keyword vocabularies (title
   n-grams + author keywords where available), build the domain partition,
   and compute RQ1/RQ2 quantities with the toolkit.
3. **Semantic-link test (P2):** use the QNFO corpus (399 titles) + the
   p2-consilience-map from the predecessor record to test H-SILO-3.
4. **Mechanisms and infrastructure (RQ3-RQ5):** evidence-based synthesis from
   the quantitative results + citation/co-citation proxies + the QNFO taxonomy
   engineering history.
5. **Computational verification (P2, COMPUTATIONAL-VERIFICATION-1):** every
   number in the paper reproduced by deposited scripts with fixed seeds; logs
   in artifacts/verification/.

## 6. Deliverables

| Phase | Deliverable | Status |
|:------|:------------|:-------|
| P0 | Repo branch, PROJECT-PLAN, hypothesis cards, WBS registration | complete |
| P1 | Measurement code (scripts/terminology_silos.py) | complete |
| P1 | External evidence dataset (artifacts/external-search/arxiv_domains_*.json) | complete |
| P2 | Analysis outputs + verification logs (artifacts/verification/) | complete |
| P3 | Paper draft v0.1 (terminology-silos-consilience.md) | complete |
| P4 | Red-team + revision | complete (P3.5-style review embedded; see §4 status log) |
| P5 | Publication (Zenodo, concept 22075543; v1.0 10.5281/zenodo.22075544) | complete |
| P6 | Deployment (D1 living-paper, papers-server, DNS) | in progress |
| P7 | Dissemination (social posting, SEO, Internet Archive) | pending |
| P8 | Core Distribution (R2 archive, KG node, GitHub tag, 4-layer verification) | pending |

## 7. Continuity

- Umbrella paper: "The Ultrametric Program" v2.4 (10.5281/zenodo.22073477) —
  §5.1 rewrite (v2.5) will reference this project.
- Predecessor: "The Consilience of the QNFO Keyword Taxonomy"
  (10.5281/zenodo.22071421) — source of the seed measurement and code.
- Program: QNFO.CGS (Consilient Gap Synthesis), portfolio-state
  program_registry + KG nodes updated at P8.
