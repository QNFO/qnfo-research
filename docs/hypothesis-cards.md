# Hypothesis Cards — Terminology Silos and the Consilience Gap

Pre-registered testable claims (HYPOTHESIS-CARD-1 pattern). Each card: claim,
prediction, falsifier, surprisal. Re-checked at each phase gate and at the
90-day re-sweep.

## H-SILO-1 — Partitionality is the norm in science

- **Claim:** across a sample of >=6 scientific domains with curated keyword
  vocabularies, at least 90% of keywords occur in exactly one domain.
- **Prediction:** partitionality_index >= 0.90 on the external arXiv-domain
  sample.
- **Falsifier:** partitionality_index < 0.90.
- **Surprisal:** moderate. Interdisciplinary rhetoric implies substantial
  sharing; the null would be >=20% shared vocabulary.

## H-SILO-2 — Bridge vocabulary is rare and structurally biased

- **Claim:** shared keywords are <10% of total vocabulary and are enriched in
  structurally general concept families (hierarchy, measure, order,
  transformation, information) relative to domain-specific constructs.
- **Prediction:** bridge_share < 0.10; Fisher exact enrichment p < 0.05.
- **Falsifier:** bridge_share >= 0.10 or p >= 0.05.
- **Surprisal:** low-moderate. The QNFO seed case (53/335 bridge terms,
  per-program bridge share 0.0-0.55, hierarchy family spanning three
  programs) is consistent.

## H-SILO-3 — Semantic consilience is invisible to lexical matching

- **Claim:** cross-domain correspondences (one structural object, different
  names) carry no keyword-level signature: semantically linked cross-program
  record pairs have keyword overlap no higher than random pairs.
- **Prediction:** mean pairwise keyword overlap of linked pairs <= overlap of
  random pairs (difference < 0.05).
- **Falsifier:** linked pairs show significantly higher keyword overlap.
- **Surprisal:** high. Lexically visible links would mean keyword search
  alone discovers cross-domain consilience — contradicted by the QNFO audit
  (Fisher p = 1.0 enrichment null).

## Status log

| Card | Date | Gate | Verdict |
|:-----|:-----|:-----|:--------|
| all | 2026-08-24 | P0 | registered |
