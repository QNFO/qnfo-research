---
title: "Terminology Silos and the Consilience Gap: A Quantitative Audit of Cross-Domain Vocabulary"
author: Rowan Brad Quni-Gudzinas
date: 2026-08-24
version: v0.1
license: CC BY 4.0
---

## Abstract

Interdisciplinary consilience is claimed everywhere and measured almost
nowhere. This paper measures one of its basic preconditions: whether
scientific domains share vocabulary. We generalize the keyword-taxonomy
audit of the QNFO research program (a seven-domain organization whose own
canonical taxonomy proved strictly partitional — 334 of 335 keywords occur
in exactly one domain) into a quantitative instrument and apply it to an
external sample of six arXiv disciplines (240 recent abstracts; 466
technical compound terms). The result: terminology silos are the norm, not
an organizational accident. 97.2% of the external technical vocabulary
occurs in exactly one discipline; the shared core (terms in three or more
disciplines) is empty; and the 2.8% of terms that do bridge disciplines are
massively enriched in method-level vocabulary (machine learning, language
models, upper bounds) rather than structural concepts (Fisher exact
p = 1e-6, odds ratio 70). On the QNFO corpus, semantically linked papers
within a program share title vocabulary (mean Jaccard 0.11 vs 0.03 random),
while the cross-domain semantic bridges the program itself cites carry zero
lexical signal unless an author deliberately wrote the bridge into a title.
We conclude that the consilience gap is in part a vocabulary gap: shared
terminology is rare, structurally biased toward methods, and built rather
than emergent. The paper closes with the infrastructure response — bridge
vocabularies as first-class research infrastructure, taxonomy engineering,
and semantic mapping — and states where its premises end.

## 1. Introduction

A researcher in quantum foundations, a researcher in algebraic number
theory, and a researcher in machine learning can work on the same structural
object — a nested, hierarchical partition of a state space — and never
discover each other. The first calls it a measurement hierarchy, the second
calls it a valuation, the third calls it a cluster tree. Their vocabularies
do not overlap; their results do.

This is the terminology silo problem. It is a commonplace complaint of
interdisciplinary research that "we all mean the same thing but use
different words." It is rarely quantified. This paper quantifies it, at two
scales: the internal scale of a single research organization (the QNFO
program, seven research domains sharing one canonical keyword taxonomy) and
the external scale of six scientific disciplines sampled from arXiv.

The motivation is not lexicographic. Large-scale scientific progress is
increasingly bottlenecked at the vocabulary layer: literature search,
citation graphs, knowledge graphs, and AI-assisted synthesis all operate
primarily on lexical matching, and lexical matching systematically misses
cross-domain correspondences. If the shared vocabulary of science is 3% of
its technical terms, then keyword-based discovery is a 3%-recall instrument
for the connections that interdisciplinary consilience depends on. That is
the gap this paper measures and then proposes infrastructure for.

### Why a reader should care

If you search for related work and miss the field that already solved your
problem under a different name, you are paying the terminology silo tax.
This paper tells you the size of the tax (97% of technical vocabulary is
domain-local), its structure (what little is shared is method, not
substance), and what to do about it (build bridge vocabularies; do not wait
for them to emerge).

## 2. The seed audit: a seven-domain organization's own vocabulary

The QNFO research program spans seven domains — ultrametric physics (UMP),
the laws of form (SLB), infomatics (INM), paradigm engineering (CFE),
consilience research (RES), a cloud-native platform (PLT), and interactive
demos (DEM) — and maintains a canonical keyword taxonomy of 335 terms for
GitHub discovery (docs/QNFO-KEYWORD-TAXONOMY.md v1.0, 2026-08-05). The
program's central claim is that the seven domains are seven vocabularies for
one structural object: nested hierarchical partition logic.

A computational audit of that taxonomy (10.5281/zenodo.22071421) found the
claim lexically unsupported. 334 of 335 keywords occur in exactly one
program; exactly one keyword (complexity-measure) occurs in two; none
occurs in three or more. The taxonomy's own bridge subsections — named
bridge concepts inside each program — are program-local anchors: they name
connections without instantiating shared vocabulary. A Fisher exact test of
whether the four bridge families (valuation, hierarchy, distinction, bound)
coincide with load-bearing vocabulary (keywords shared by three or more
programs) gives p = 1.0: no enrichment whatsoever. The consilience, if it
exists, is semantic — carried by corpus-level links between records — not
lexical.

This single-case result invites the general question: is the QNFO taxonomy
an organizational artifact, or a microcosm of science? The rest of this
paper treats it as a hypothesis source and builds an instrument that can be
applied to any domain partition.

## 3. Definitions and instrument

Three quantities, all computed from a domain-keyword partition (a set of
domains, each with a set of technical terms):

1. **Partitionality index** — the fraction of distinct keywords occurring
   in exactly one domain. A partitionality of 1.0 means total vocabulary
   isolation; 0.0 means every term is shared.
2. **Bridge share** — the fraction of distinct keywords occurring in two or
   more domains. The complement of local vocabulary.
3. **Shared core** — keywords occurring in three or more domains (a
   load-bearing shared vocabulary in the sense of the seed audit).

Plus a structural probe: a one-sided Fisher exact test on the
bridge x general-family contingency, where the general family is a curated
list of structurally general method and pattern terms (machine learning,
neural networks, Monte Carlo, phase transitions, upper bounds, and similar
vocabulary that plausibly travels across fields). The test asks whether
bridge terms are drawn preferentially from the general family rather than
uniformly from all vocabulary.

**Vocabulary extraction.** For the external sample, technical vocabulary is
extracted from paper titles and abstracts as compound terms (bigrams of
content words), after removing a large stopword set (function words and
generic science shells such as "model", "system", "theory", "study",
"field", "structure"). Bigrams are used because modern technical vocabulary
is overwhelmingly compound (phase-transition, neural-network, monte-carlo,
p-adic); single tokens are too ambiguous to discriminate domains. Per
domain, the 80 most frequent bigrams (frequency at least 2 in the sample)
form the domain vocabulary. The extraction is deterministic: no randomness,
fixed seed policy for any sampling.

The instrument reproduces the published seed audit exactly (validation 9/9:
335 distinct keywords, 334 local, one shared-by-two, zero core,
53/282 family-bridge contingency, Fisher p = 1.0), so the external numbers
below rest on a validated pipeline.

## 4. Results I: six disciplines, one vocabulary wall

Six arXiv categories were sampled (40 most recent abstracts each, fetched
2026-08-24): quantum physics (quant-ph), number theory (math.NT), machine
learning (cs.LG), genomics (q-bio.GN), materials science
(cond-mat.mtrl-sci), and economic theory (econ.TH). Vocabulary extraction
yielded 466 distinct technical bigrams across the six domains.

| Quantity | Value |
|:---------|------:|
| Distinct technical terms | 466 |
| Domain-local terms (exactly one domain) | 453 |
| **Partitionality index** | **0.9721** |
| Bridge terms (two or more domains) | 13 |
| Bridge share | 0.0279 |
| Shared core (three or more domains) | 0 |

The partitionality hypothesis (H-SILO-1: at least 90% of vocabulary
domain-local) is confirmed: 97.2%. The shared core is empty at the
three-domain threshold. Interdisciplinary rhetoric notwithstanding, six
disciplines share essentially no technical vocabulary beyond chance.

The 13 bridge terms are the interesting residue:

- **Method vocabulary:** machine-learning, language-model, language-models,
  foundation-models, upper-bound (5 of 13).
- **Shared objects:** boron-nitride, quantum-defects, defects-zno,
  double-substitutional, optically-quantum, candidate-quantum,
  candidates-optically (7 of 13 — two disciplines working on the same
  materials).
- **Shared application:** drug-discovery (1 of 13).

The structural probe quantifies the method bias: of the 13 bridges, 5 are
method/pattern terms; of the 453 domain-local terms, only 4 are. The Fisher
exact test on the bridge x general-family contingency gives
p = 1.1e-6 with odds ratio 70.2 — bridge vocabulary is seventy times more
likely to be method vocabulary than domain-local vocabulary is. What
travels between disciplines is not the structural substance (hierarchies,
valuations, measures) but the toolkit (learning, models, bounds).

The QNFO seed case shows the same structure in extremis: bridge share
0.0030, and its own bridge families show zero enrichment against
load-bearing vocabulary (p = 1.0). The seed's bridge vocabulary is
domain-anchored (ostrowski-theorem, idele-class-group) rather than
method-level — an organization whose bridge infrastructure is homegrown, not
imported.

## 5. Results II: the QNFO corpus — semantic links and lexical silence

The external sample measures vocabulary; the QNFO corpus (578 titled
records in the living paper) measures whether semantic relatedness is
lexically visible. Three probes.

**Probe 1 — the knowledge-graph link network is program-local.** The QNFO
knowledge graph's paper-to-paper semantic edges (CITES, DEPENDS_ON,
MOTIVATES, REFINES, BRIDGES, REFERENCES, SUPERSEDES, LINKS_TO, RELATES_TO)
resolve to 40 pairs of corpus records. Classifying each record into its
program by title-vocabulary overlap with the taxonomy, 8 pairs are
same-program and 0 pairs are cross-program (32 pairs involve at least one
unclassifiable endpoint). The graph links papers within programs; it has
not yet built the cross-program network. The link infrastructure is itself
siloed.

**Probe 2 — within-program links are lexically visible.** Same-program
linked pairs share title vocabulary at mean Jaccard 0.115, against 0.028
for random pairs (seeded, same cardinality): a +0.086 elevation. Within a
program, shared vocabulary tracks semantic relatedness. This is the
partitional null: vocabulary signals structure only inside a domain.

**Probe 3 — the cited cross-domain bridges carry zero lexical signal.**
The umbrella program paper (10.5281/zenodo.22073477, section 5.1) cites
three corpus records as the semantic bridges that carry the consilience:
measurement stratigraphy linking epistemology to valuation theory
(10.5281/zenodo.21705220), the valuation-without-reals framework
(10.5281/zenodo.21803677), and ultrametric topology in semantic memory
(10.5281/zenodo.19564091). The first pair (measurement-stratigraphy vs
adelic-shannon-theory) has title-vocabulary Jaccard **0.0000**; the third
pair (silent-radix cryptography vs ultrametric numeration) also 0.0000.
The consilience is lexically invisible where no author built the bridge.

The single visible exception proves the rule: the valuation-without-reals
record shares the token "valuation" with measurement stratigraphy at
Jaccard 0.333 — because its author deliberately wrote the bridge into the
title ("Valuation Without R"). Vocabulary bridges are built, not emergent.

**Summary of hypothesis outcomes.**

| Hypothesis | Prediction | Result |
|:-----------|:-----------|:-------|
| H-SILO-1 | partitionality >= 0.90 | **Confirmed** (0.9721 external; 0.9970 seed) |
| H-SILO-2 | bridge share < 0.10; Fisher p < 0.05 | **Confirmed** (0.0279; p = 1.1e-6, OR 70.2) |
| H-SILO-3 | semantic links carry no lexical signature | **Supported** (0.0 on non-authored bridges; within-program links visible) |

## 6. Why silos persist

The measurement explains the phenomenon; the persistence mechanisms are
incentive and infrastructure. Four evidence-grounded mechanisms:

1. **Field-local prestige economies.** Publication, hiring, and funding
   reward vocabulary mastery within a field; mastery is signaled by using
   the field's terms, not by translating them. The QNFO seed shows the
   organizational version: programs are rewarded for domain depth, and the
   taxonomy's bridge subsections exist precisely because nothing in the
   ordinary keyword flow crosses boundaries.
2. **Vocabulary gatekeeping by venues.** Journals, conferences, and
   archives curate keyword taxonomies that are field-scoped. A term that
   does not appear in the venue's taxonomy is invisible to its search;
   authors optimize for the venue's vocabulary, deepening the partition.
3. **Translation costs.** Establishing that "valuation" in number theory
   corresponds to "measurement hierarchy" in epistemology costs
   verification effort that the author bears alone and the field does not
   reward. The QNFO corpus demonstrates the result: where an author paid
   the cost (the "Valuation Without R" title), the bridge is visible;
   elsewhere it is not.
4. **Path dependence in taxonomy formation.** Keyword taxonomies grow by
   accretion inside domains; they are rarely audited for cross-domain
   overlap, and no one owns the intersection. The seed audit is itself the
   exception that tests the rule: it took a computational audit to discover
   that an organization's own vocabulary was 99.7% partitional.

## 7. What the silo costs

The measurable proxies from this study bound the cost:

- **Discovery failure.** With a 2.8% bridge share, keyword search for a
  concept outside the searcher's home domain has a recall ceiling of a few
  percent for cross-domain correspondences. The exemplar result (Jaccard
  0.0 between two records the program itself cites as semantically linked)
  shows the failure at record level: the linkage exists in prose, not in
  vocabulary, so it is invisible to lexical retrieval.
- **Duplicated discovery.** Fields that cannot see each other's vocabulary
  cannot see each other's results; the same structural result is
  re-derived under new names. The method-bias finding (bridges are 70x
  enriched in method vocabulary) sharpens this: disciplines import each
  other's tools while remaining blind to each other's structures.
- **Convergence delay.** Cross-domain consilience — the recognition that
  two fields describe one object — is the rate-limiting step for large-scale
  synthesis. If vocabulary is 97% partitional, consilience is never
  discoverable bottom-up; it requires an explicit act of bridge-building.

## 8. Consilience infrastructure: bridges are built, not emergent

The constructive response follows directly from the measurement. If shared
vocabulary is rare, method-biased, and author-made, then consilience needs
deliberate vocabulary infrastructure:

1. **Bridge vocabularies as first-class artifacts.** A bridge vocabulary is
   a maintained, versioned mapping between the terms of two or more
   domains, with verification notes (which terms correspond, at what level
   of structural fidelity). The QNFO taxonomy's bridge subsections are a
   primitive version; the corpus's title-visible bridges are the worked
   examples of the practice.
2. **Taxonomy engineering with an intersection owner.** Every domain
   taxonomy should have a named owner of the intersection: a person or
   process that periodically audits the partition, measures bridge share,
   and curates the cross-domain terms. The instrument in this paper is the
   audit tool; the seed validation shows it can be run continuously at
   organizational scale.
3. **Semantic mapping between field vocabularies.** For the AI-assisted
   synthesis pipeline, the fix is a mapping layer between field-specific
   vocabularies — the semantic analogue of a bilingual dictionary — so that
   retrieval can find "measurement hierarchy" when asked for "valuation".
   The H-SILO-3 result quantifies the need: without the mapping layer,
   cross-domain retrieval operates at zero recall on the program's own
   cited bridges.
4. **Title-visible bridges.** The cheapest infrastructure is authorial:
   when a paper connects domains, name the connection in the title. The
   one visible exemplar (Jaccard 0.333) shows the effect; it is the only
   corpus bridge that lexical retrieval can find.

## 9. Where the premises end

This paper's claims are derived from the measurement pipeline; its premises
end at four named inputs:

- **P1 — the vocabulary model.** Technical vocabulary is modeled as
  stopword-filtered bigrams from titles and abstracts. This is a proxy for
  "the terms a field uses": it excludes single-token technical terms, terms
  below the frequency threshold, and terms that appear only in bodies. The
  QNFO seed, which uses curated keywords, shows the same partitional
  structure, but the two pipelines are not identical instruments.
- **P2 — the domain partition.** The external sample partitions science by
  arXiv category. Real disciplines overlap and subdivide; the partition
  choice affects the measured quantities (finer partitions raise
  partitionality).
- **P3 — the general-family list.** The Fisher enrichment test depends on
  the curated method/pattern list. The list is conservative (method terms
  only) and published in full with the instrument; re-running with a
  different list changes the odds ratio, not the qualitative result (bridges
  are method-concentrated by inspection of all 13 terms).
- **P4 — the corpus scope.** The QNFO corpus probes are single-organization
  evidence: 578 records, 40 resolvable graph pairs, three cited bridges.
  The external generalization rests on the six-discipline vocabulary
  sample (240 abstracts).

The quantitative claims (partitionality, bridge share, Fisher p, Jaccard
values) are reproduced by the deposited scripts with fixed seeds
(artifacts/verification/). No claim here extends beyond the measured
samples; the mechanisms of Section 6 are explanatory hypotheses grounded in
those measurements plus standard economics of science, not independent
estimates.

## 10. Limitations and next steps

Limitations: sample breadth (six disciplines, 40 abstracts each — a
snapshot, not a census); the single-token blind spot of the bigram model;
the absence of a temporal dimension (vocabulary silos may be widening or
narrowing over time); and the organization-scale corpus probes.

Next steps: (1) scale the external sample to 30+ disciplines and 1,000+
abstracts per discipline, with author-keyword metadata where available;
(2) add the temporal dimension via arXiv date-banded samples to measure
whether bridge share is changing; (3) build and evaluate the semantic
mapping layer (bilingual-dictionary analogue) on the QNFO corpus, testing
whether mapped retrieval recovers the program's own cited bridges; (4)
publish the bridge-vocabulary audit as a recurring instrument for the QNFO
program (the seed case already runs it).

## 11. Reproducibility

- `scripts/arxiv_domain_sample.py` — external evidence collection
  (arXiv API, deterministic extraction; raw evidence in
  artifacts/external-search/arxiv_raw_2026-08-24.json).
- `scripts/build_qnfo_domains.py` — canonical taxonomy parser (method of
  rq5_keyword_load.py).
- `scripts/terminology_silos.py` — measurement toolkit (partitionality,
  bridge share, shared core, Fisher exact).
- `scripts/hsilo3_semantic_links.py` — corpus probes (KG structure,
  same-vs-random, exemplar bridges).
- `scripts/validate_seed_vs_published.py` — 9/9 validation against the
  published audit.
- All outputs and logs: artifacts/verification/. Seeds fixed (42 where
  sampling occurs); the extraction itself is deterministic.

## References

1. Quni-Gudzinas, R. B. (2026). The Consilience of the QNFO Keyword
   Taxonomy: Ultrametric Structure as a Testable Compression Prior.
   Zenodo, 10.5281/zenodo.22071421.
2. Quni-Gudzinas, R. B. (2026). The Ultrametric Program: One Structural
   Object Across Seven Research Domains, and Its Falsifiable Tests.
   Zenodo, 10.5281/zenodo.22073477.
3. Quni-Gudzinas, R. B. (2026). The History and Future of Measurement
   Stratigraphy, Number Theory, and Valuation Theory. Zenodo,
   10.5281/zenodo.21705220.
4. Quni-Gudzinas, R. B. (2026). Valuation Without R: A Category-Theoretic
   Foundation for Finite Measurement. Zenodo, 10.5281/zenodo.21803677.
5. Quni-Gudzinas, R. B. (2026). Ultrametric topology in semantic memory
   with invariant cross-ratio stability. Zenodo, 10.5281/zenodo.19564091.
6. QNFO Keyword Taxonomy v1.0 (2026-08-05). docs/QNFO-KEYWORD-TAXONOMY.md,
   QNFO/qnfo-research; flat rendering
   docs/keyword-taxonomy-source.md.
