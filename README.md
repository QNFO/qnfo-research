# README — Terminology Silos and the Consilience Gap

**WBS:** `QNFO.CGS.002` | **Branch:** `res/paper/terminology-silos-consilience`
**DOI:** 10.5281/zenodo.22075544

Spinoff research from the keyword-taxonomy audit of "The Ultrametric Program"
(10.5281/zenodo.22073477, §5.1) and its predecessor record
"The Consilience of the QNFO Keyword Taxonomy" (10.5281/zenodo.22071421).

## How to cite

> Quni-Gudzinas, Rowan Brad (2026). Terminology Silos and the Consilience
> Gap: A Quantitative Audit of Cross-Domain Vocabulary. QNFO. Zenodo.
> https://doi.org/10.5281/zenodo.22075543

Cite all versions: 10.5281/zenodo.22075543 (concept DOI — always resolves to
the latest version). This version: 10.5281/zenodo.22075544.

## The question

Scientific fields maintain largely disjoint vocabularies. The QNFO program —
seven research domains, one claimed structural object — is a worked example:
its canonical keyword taxonomy (335 keywords, seven program sections) is
strictly partitional (334/335 keywords occur in exactly one program; shared
vocabulary core: empty; Fisher enrichment p = 1.0). The consilience claim is
semantic, not lexical.

This project asks whether that single-case result is the norm across science,
what the structure of bridge vocabulary is, why silos persist, what they
cost, and what consilience infrastructure (bridge vocabularies, taxonomy
engineering, semantic mapping) can do about it.

## Key results

| Quantity | External (6 arXiv domains) | QNFO seed (7 programs) |
|:---------|:---------------------------|:-----------------------|
| Partitionality index | 0.9721 | 0.9970 |
| Bridge share | 0.0279 | 0.0030 |
| Shared core (>=3 domains) | 0 | 0 |
| Fisher enrichment (bridge x method vocabulary) | p = 8.5e-7, OR 70.2 | p = 1.0 (family x load-bearing) |

Semantically linked papers share vocabulary within a program (Jaccard 0.11
vs 0.03 random) but the program's own cited cross-domain bridges carry zero
lexical signal unless an author wrote the bridge into the title.

## Contents

- `terminology-silos-consilience.md` — the paper
- `PROJECT-PLAN.md` — plan, research questions, hypothesis cards
- `scripts/` — measurement toolkit + evidence collectors + verification
- `artifacts/external-search/` — fetched evidence (arXiv samples, KG edges)
- `artifacts/verification/` — analysis outputs + verification logs

## Reproduce

```bash
python scripts/arxiv_domain_sample.py 40
python scripts/terminology_silos.py --domains artifacts/external-search/arxiv_domains.json
python scripts/terminology_silos.py --domains artifacts/external-search/qnfo_domains.json
python scripts/hsilo3_semantic_links.py
python scripts/validate_seed_vs_published.py
```

All numbers in the paper are produced by these scripts; outputs and logs are
deposited in `artifacts/verification/`.
