# Citation Audit — QNFO.RES.009

**Date:** 2026-08-14 · **WBS:** QNFO.RES.009.P3 · **Slug:** spin-statistics-distinction

**Entries:** 41 (11 Crossref-verified external + 4 books/chapters + 19 arXiv eprints + 11 internal Zenodo).

## Per-entry verification method

| Group | Entries | Method | Status |
|---|---|---|---|
| External Crossref-verified DOIs | 11 | live `api.crossref.org/works/{doi}` fetch (authors, year, title, container) | VERIFIED 2026-08-14 |
| Books / chapters | 4 | Crossref + OpenAlex record; chapter-author metadata empty on 2 Wilczek-volume entries (volume author credited) | VERIFIED at volume level |
| arXiv eprints | 19 | arXiv API via arxiv-mcp (id, title, authors from authoritative metadata) | VERIFIED 2026-08-14 |
| Internal Zenodo records | 11 | D1 living-paper sweep + resolve_paper_id cross-system validation | VERIFIED 2026-08-14 |

## P3.AUTHOR-GATE record

- All external author lists verified against LIVE Crossref responses (evidence: artifacts/external-search/crossref_author_verified.json) or arXiv API metadata. **No hand-constructed author lists shipped.**
- **Gate catches in this cycle (placeholder authors corrected before commit):**
  - balachandran_1990: placeholder 'da Silva/Teotonio-Sobrinho' -> live Crossref 'Balachandran, Daughton, Gu, Marmo, Sorkin, Srivastava'.
  - bruillard_2009: placeholder 'Bruillard/Ng/Rowell/Wang' -> live Crossref 'Rowell, Stong, Wang' (10.1007/s00220-009-0908-z is the Rowell-Stong-Wang paper).
  - nayak_2015: placeholder 'Nayak/Simon/Stern/...' -> live Crossref 'Das Sarma, Freedman, Nayak' (npj QI 2015).
  - weinberg_proof_2003: resolved live to 'Massimi, Redhead' (Studies in Hist. Phil. Mod. Phys. 34, 441).
  - cambridge_sst_2019 chapter: Crossref returned NO authors -> entry DROPPED (never ship unverified authorship).
  - kong_wen_2014: Crossref 404 on 10.48550 -> re-encoded as arXiv eprint 1405.5858 with authors Kong & Wen (arXiv-verified).
- Internal records: author = Rowan Brad Quni-Gudzinas (canonical corpus name, ORCID 0009-0002-4317-5604).
- DOI resolution: all external DOIs Crossref-confirmed 2026-08-14 (doi.org HEAD 403-on-some-publishers handled per research v2.109 DOI-WAF-403 discipline: Crossref is authoritative).

## Duplicate-key check

- 41 keys, all unique (no copy/merge concatenation was used).
- In-text citation reconciliation pending P4/P5 draft (0 dangling keys in .bib; 0 body citations yet).

## Three-count audit

- queries sent: 4 Crossref batches + 3 arXiv + 2 Zenodo + 1 EuropePMC = 10
- sources received: 12 Crossref records + 40 arXiv results + 20 Zenodo hits + 10 EuropePMC hits = 82
- sources cited: 41 (all verified) — cited <= received: PASS
