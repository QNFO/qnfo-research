# External Literature Search — QNFO.RES.006 (Phase 2)

**Date:** 2026-08-13
**Method:** OpenAlex (keyless), Crossref (keyless), arXiv API. Evidence JSON in this directory; manifest at `_search_manifest.json`; deduplicated ranked hits at `_external_top_hits.json`.

## Purpose

Phase 1 due diligence flagged `[CONFIRMATION-BIAS-RISK]`: all QEC/p-adic hits were QNFO-internal. Phase 2 runs the external search to distinguish internal from external corroboration.

## Result: the two bridges have substantial external precedent

The anchor paper's quantum reading rests on two bridges. Both are **established in the external literature**, which this paper now cites and does not claim as original.

### Bridge 1 — no-cloning as categorical (monoidal, non-Cartesian)

External, established:
- Abramsky & Coecke (2004), *A categorical semantics of quantum protocols*.
- Abramsky (2009), *No-Cloning in Categorical Quantum Mechanics* (doi 10.1017/cbo9781139193313.002).
- Coecke (2009), *Quantum Pictorialism* (arXiv:0908.1787).
- Coecke & Duncan (2011), *Interacting Quantum Observables* (doi 10.1088/1367-2630/13/4/043016).

The anchor's "no linear diagonal map / monoidal-not-Cartesian" is this result, re-expressed in branch-depth vocabulary.

### Bridge 2 — p-adic geometry and QEC (holographic)

External, established:
- Heydeman, Marcolli, Saberi & Stoica (2016/2018), *Tensor networks, p-adic fields, and algebraic curves* (arXiv:1605.07639, ATMP 22:93).
- Heydeman, Marcolli, Parikh & Saberi (2018), *Nonarchimedean Holographic Entropy from Networks of Perfect Tensors* (arXiv:1812.04057).
- Bhattacharyya, Hung, Lei & Li (2018), *Tensor network and (p-adic) AdS/CFT* (doi 10.1007/jhep01(2018)139).
- Gubser & Knaute (2017), *p-Adic AdS/CFT* (doi 10.1007/s00220-016-2813-6).

These connect p-adic geometry (Bruhat-Tits trees) to QEC via holographic tensor networks — the genuine external lineage that QNFO's internal corpus parallels.

### Working background

- Bravyi et al. (2019), *Simulation of quantum circuits by low-rank stabilizer decompositions* (doi 10.22331/q-2019-09-02-181).

## OpenAlex volume (raw counts, fuzzy search)

| Query | OpenAlex hits |
|:------|--------------:|
| p-adic quantum error correction | 700 |
| p-adic stabilizer code | 577 |
| no-cloning theorem monoidal category | 391 |
| ultrametric quantum error correction | 246 |

(The counts are fuzzy-search totals, not curated matches; the curated anchor set is the 10 references in references.bib.)

## Consequence for the manuscript

The external search forced a repositioning (§1.3, §5, §8 of the manuscript): the paper's contribution is the narrow **branch-depth vocabulary**, not the categorical no-cloning result and not the p-adic/QEC connection. The honest core is the self-correction (§3): the naive [[n,k,d]] valuation mapping is definitional relabeling, which redirects to the one precise open question (a non-trivial valuation invariant) and the one falsifiable task (a valuation-based overhead bound vs. the Singleton bound).
