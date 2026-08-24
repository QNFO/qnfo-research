# README — Terminology Silos and the Consilience Gap

**WBS:** `QNFO.CGS.002` | **Branch:** `res/paper/terminology-silos-consilience`

Spinoff research from the keyword-taxonomy audit of "The Ultrametric Program"
(10.5281/zenodo.22073477, §5.1) and its predecessor record
"The Consilience of the QNFO Keyword Taxonomy" (10.5281/zenodo.22071421).

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

## Contents

- `terminology-silos-consilience.md` — the paper (draft)
- `PROJECT-PLAN.md` — plan, research questions, hypothesis cards
- `scripts/terminology_silos.py` — measurement toolkit
- `scripts/arxiv_domain_sample.py` — external evidence collector
- `artifacts/external-search/` — fetched evidence (arXiv samples)
- `artifacts/verification/` — analysis outputs + verification logs

## Reproduce

```bash
python scripts/arxiv_domain_sample.py --categories quant-ph math.NT cs.LG q-bio.GN cond-mat.mtrl-sci stat.ML --max-abstracts 60
python scripts/terminology_silos.py --domains artifacts/external-search/arxiv_domains.json --seed 42
```

All numbers in the paper are produced by these scripts with fixed seeds;
logs and outputs are deposited in `artifacts/verification/`.

## Status

P0/P1 in progress (2026-08-24). See PROJECT-PLAN.md §6.
