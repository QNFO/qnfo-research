# Completeness Senses and the Levi-Civita Field

Ordered Non-Archimedean Number Systems Beyond Ostrowski's Classification

**Author:** Rowan Brad Quni-Gudzinas
**Date:** 2026-08-26
**License:** QNFO Unified License Agreement (QNFO-ULA) — https://legal.qnfo.org/

## Abstract

Ostrowski's theorem classifies every nontrivial rank-1 absolute value on the rationals: the Archimedean absolute value and, for each prime p, a p-adic absolute value. Their completions are the real numbers and the p-adic fields. This classification is often read as closing the question of what a complete number system can be. It does not. The theorem governs completions of the rationals under multiplicative sizes; it says nothing about ordered field extensions of the reals that carry infinitesimals, about stronger non-Archimedean notions of completeness, or about valuations of higher rank. This paper separates those questions, distinguishes three senses of completeness — Dedekind, Cauchy, and spherical — and exhibits the Levi-Civita field as a genuine counterexample to the claim that the reals are the unique complete ordered field: it is Cauchy-complete, ordered, real-closed, and non-Archimedean at once. The standard decimal identity 0.999... = 1 survives by transfer in every ordered field containing the reals; the divergent case appears only for nonstandard-indexed decimals. Higher-rank valuations occur only in function fields of transcendence degree at least two. The aim is not to displace the reals, which remain the unique Dedekind-complete ordered field, but to make the completeness question precise enough that "the reals are the complete number system" and "there are many complete number systems" can both be stated without equivocation.

## How to cite

Cite all versions via the concept DOI (always resolves to the latest version):

> Quni-Gudzinas, Rowan Brad. (2026). *Completeness Senses and the Levi-Civita Field: Ordered Non-Archimedean Number Systems Beyond Ostrowski's Classification*. Zenodo. 10.5281/zenodo.22109086

## Files in this deposit

- post-positional-numeracy.md (this document)
- post-positional-numeracy.html
- post-positional-numeracy.pdf
- references.bib
- citation-audit.md
- PROJECT-PLAN.md
- README.md
- README-DEPOSIT.md
- LICENSE-CC-BY-4.0.txt
- docs/deep-research.md
- artifacts/verification/verify_completeness.py
- artifacts/verification/verify_completeness_out.txt

## Reproducibility

Run `python verify_completeness.py` (Python 3, standard library only, deterministic, seed-free). Expected output: `verify_completeness_out.txt`, all checks PASS.
