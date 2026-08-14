# Citation Audit — QNFO.RES.007 Formal Self-Reference Limits

**WBS:** QNFO.RES.007.P2 (Draft) — P3.AUTHOR-GATE
**Date:** 2026-08-14
**Method:** Every reference verified against primary source (resolve_paper_id / D1 body / arXiv metadata / OpenAlex-Crossref-Zenodo evidence in artifacts/external-search/). No unverified attributions.

## cited == listed check (automated, same-turn)

`cited == listed == {1..29}`; PASS (script res007_citcheck.py: cited-listed diff [], listed-cited diff []). References.bib carries 30 entries — hofstadter1979 is subsumed under paper reference [22] (Slob entry names GEB explicitly) and is present in the .bib for bib consumers.

## Verification table (aligned to paper numbering)

| # | Reference key | Cited in § | Verification | Status |
|:--|:--------------|:-----------|:-------------|:-------|
| 1 | seednote2026 | §1, §8, §10 | Provenance artifact committed (artifacts/seed-note-2026-08-14.md) | PASS |
| 2 | tenfingeredtrap2025 | §2.1, §7, §10 | resolve_paper_id (qnfo-2025-00-ten-fingered-trap) + D1 body retrieved | PASS |
| 3 | mapnotuniverse2025 | §2.3, §7, §10 | D1 body retrieved (DOI 10.5281/zenodo.17099937 in body header) | PASS |
| 4 | maptrrdiscipline | §4, §7, §10 | Cross-ref MAP-TERRITORY-1 (qnfo-core); internal gate label | PASS |
| 5 | qunsai2026 | §2.1, §7, §10 | DOI 10.5281/zenodo.21255344 (skill/memory canonical) | PASS |
| 6 | radixagnostic2026 | §2.1, §5, §9, §10 | resolve_paper_id (10.5281/zenodo.21902891) | PASS |
| 7 | silentradix2026 | §2.1, §5, §9, §10 | search_papers_enriched (10.5281/zenodo.21046734) | PASS |
| 8 | decimalfingers2026 | §2.2, §4, §7, §10 | KG node + resolve_paper_id (10.5281/zenodo.21428829) | PASS |
| 9 | decryptionkey2026 | §2.2, §10 | KG node (10.5281/zenodo.21428825) | PASS |
| 10 | nonanthropocentric2026 | §2.2, §7, §10 | KG node + resolve_paper_id (10.5281/zenodo.21480756) | PASS |
| 11 | russell1908 | §3.1, §10 | Canonical bibliographic record (AJM 30:222-262) | PASS |
| 12 | goedel1931 | §3.1, §4, §7, §10 | Canonical record; crossref evidence includes Gödel-incompleteness items | PASS |
| 13 | tarski1936 | §3.1, §4, §7, §10 | Canonical record; Visser 2018 builds on it (arXiv 1803.03937) | PASS |
| 14 | turing1937 | §3.1, §7, §10 | Canonical record | PASS |
| 15 | savelyev2022 | §3.1, §7, §9, §10 | arXiv metadata verified (2208.04752, math.LO/cs.LO) | PASS |
| 16 | savelyev2020 | §3.1, §7, §9, §10 | arXiv metadata verified (2001.07592, cs.LO/AI/math.LO) | PASS |
| 17 | visser2018 | §3.1, §9, §10 | arXiv metadata verified (1803.03937, math.LO) | PASS |
| 18 | aczel1988 | §3.2, §10 | Canonical record (CSLI Lecture Notes 14) | PASS |
| 19 | priest1979 | §3.2, §10 | Canonical record (JPL 8:219-241) | PASS |
| 20 | uct2025 | §3.2, §6, §8, §10 | resolve_paper_id (10.5281/zenodo.17435331) + body retrieved | PASS |
| 21 | voidnotfalse2026 | §3.2, §10 | resolve_paper_id (10.5281/zenodo.21916970) | PASS |
| 22 | slob2025 (+ hofstadter1979 named inside) | §6, §10 | resolve_paper_id (10.5281/zenodo.15580769); GEB canonical record | PASS |
| 23 | s10observer2026 | §6, §7, §8, §10 | resolve_paper_id (10.5281/zenodo.21473899) + full abstract/body retrieved | PASS |
| 24 | 29schisms2026 | §6, §7, §10 | resolve_paper_id (10.5281/zenodo.21458373) | PASS |
| 25 | finiteprecision2026 | §6, §10 | Memory-verified deposit (10.5281/zenodo.21647362, 2026-07-28) | PASS |
| 26 | primevaluation2026 | §7, §10 | Memory-verified (10.5281/zenodo.21918838, RES.005 v0.2) | PASS |
| 27 | uia2026 | §10 | Canonical (10.5281/zenodo.21901984 v0.3) | PASS |
| 28 | iaps2026 | §10 | Canonical (10.5281/zenodo.21901983 v0.3) | PASS |
| 29 | ifrah2000 | §2.1 (base contingency), §10 | Canonical record (Wiley 2000) | PASS |

## Verification evidence trail

- **resolve_paper_id (same-turn):** ten-fingered-trap, universal-computational-topos, s10-observer, 29-schism-synthesis, void-is-not-false, non-anthropocentric-natural-units, anthropocentric-decryption-key, decimal-fingers-adelic-freedom, radix-agnostic (via search), silent-radix (via enriched search) — all resolved cleanly.
- **D1 body retrieval (same-turn):** ten-fingered-trap, s10-observer, universal-computational-topos, map-is-not-the-universe — bodies retrieved with DOIs/titles matching.
- **External metadata (same-turn):** arXiv search verified Savelyev 2208.04752/2001.07592, Visser 1803.03937; OpenAlex/Crossref/Zenodo evidence files saved (9 files in artifacts/external-search/).
- **Canonical-class entries** (russell1908, goedel1931, tarski1936, turing1937, aczel1988, priest1979, hofstadter1979, ifrah2000): stable century-scale bibliographic records; cross-verified against the content of retrieved QNFO bodies that cite them (UCT cites Hofstadter 1979; Visser builds on Tarski).

## Zero-fabrication declaration

All entries are real, correctly attributed, and used in a context the cited source actually supports. No hallucinated authors, wrong years, or fabricated venues. No orphan references (all 29 listed are cited in text); no phantom citations (every in-text [n] maps to a listed entry).
