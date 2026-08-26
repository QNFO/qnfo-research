# Post-Positional Numeracy: Finite-Adele Encoding and Product-Formula-Verified Exact Rational Arithmetic

**Author:** Rowan Brad Quni-Gudzinas · **DOI:** 10.5281/zenodo.22114495 · **License:** CC BY 4.0 · **Status:** published v1.0.1 (2026-08-26)

## How to cite

Cite all versions (always resolves to the latest one):

> Quni-Gudzinas, Rowan Brad. *Post-Positional Numeracy: Finite-Adele Encoding and Product-Formula-Verified Exact Rational Arithmetic.* QNFO Research Archive, 2026. Zenodo. **https://doi.org/10.5281/zenodo.22114388**

This specific version:

> Quni-Gudzinas, Rowan Brad. *Post-Positional Numeracy: Finite-Adele Encoding and Product-Formula-Verified Exact Rational Arithmetic* (version 1.0.1). QNFO Research Archive, 2026. Zenodo. **https://doi.org/10.5281/zenodo.22114495**

## Abstract

Exact computation on the rationals today inhabits a single completion. This paper develops the multi-place realization that joins the real and the p-adic: a finite-adele encoding of rationals with a proved injectivity window, and the adelic product formula as a machine-checkable invariant of multi-place exact arithmetic. All claims are computationally verified.

## Contents (flat deposit layout)

- post-positional-numeracy.md / .html / .pdf — the paper
- references.bib — bibliography (rendered by citeproc at build time)
- citation-audit.md — 27-entry citation audit (0 orphans)
- PROJECT-PLAN.md — charter, locked core claim, hypothesis cards
- docs_deep-research.md — due-diligence report; docs_universal-ignorance-audit.md — the 15-question audit; docs_literature.md — literature notes
- artifacts_consilience-gate.md — cross-domain lexicon and silo-cost table; artifacts_bayesian-evidential-weight.md — KIF-60 classification
- corpus-sweep-2026-08-26.json, arxiv-sweeps-2026-08-26.json, adjudication-memory-2026-08-26.json — due-diligence evidence
- hensel-audit-z20756222.json / hensel-audit-paper.md / hensel-audit-source.py — Hensel framework deposit audit
- p2-literature-sweep.json / p2-literature-sweep.py — literature sweep evidence
- p5-create-deposit.py, p5-deposit-create.json, p5-deposit-reserve-doi.json, p5-run.log — publication evidence
- verify_ppn.py, ppn-verification-results.json, run-verification.log — the verification suite and its output
- check_rendering.py, render-pdf.cjs — the rendering-gate and PDF-build scripts
- LICENSE — CC BY 4.0 legal code

## Reproducibility

Run `python verify_ppn.py` (Python 3.8+, standard library only, seed 20260826, runtime under one minute). All 20 checks pass; every number in the paper's verification table is reproduced. The paper builds with `pandoc post-positional-numeracy.md --citeproc --bibliography=references.bib --mathjax --standalone -o post-positional-numeracy.html`.
