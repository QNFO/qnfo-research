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


## v1.1 amendment (2026-08-14)
Added 8 entries that the manuscript's References section cites but the original .bib omitted: Pauli 1940 (10.1103/PhysRev.58.716), Streater-Wightman 1964, Leinaas-Myrheim 1977 (10.1007/BF02727953), Wilczek 1982 (10.1103/PhysRevLett.49.957), Joyal-Street 1993 (10.1006/aima.1993.1055), Kitaev 2006 (10.1016/j.aop.2005.10.005), Bakalov-Kirillov 2001, Spencer-Brown 1969. All 5 DOI-bearing entries Crossref-verified (evidence: artifacts/external-search/crossref_missing8_verified.json). Total entries now 49; all 24 manuscript-cited works are covered. Findings source: post-publication adversarial review (REDTEAM-QUEUE-STALL-1 late completion).


## v1.4 draft additions (2026-08-15, CMD EXECUTE remediation GAP-3) — NOT PUBLISHED

Six references added for the v1.4 draft (uncommitted as of this note's authoring):
Laidlaw & DeWitt 1971 (Phys. Rev. D 3, 1375 — Crossref-verified), Haldane 1991
(Phys. Rev. Lett. 67, 937 — Crossref-verified), Mekonnen, Galley & Mueller 2025
(arXiv:2502.17576), Wang & Hazzard 2023/2024/2026 (arXiv:2308.05203 / 2412.13360 /
2607.26351 — arXiv-live-verified). Section 5 boundary gains a 2026 note qualifying the
"which again lands on locality" claim: (a) a model-independent quantum-permutation
exclusion of parastatistics exists that does not route through locality (Mekonnen et al.
2025); (b) R-parastatistics — inequivalent to fermions/bosons, any dimension — emerges as
observable quasiparticle statistics in condensed matter (Wang & Hazzard 2023-2026), so the
classical equivalence theorems (Greenberg-Messiah; DHR) do not exhaust the possibilities.
SSRN 6598581 (Li 2026, "The Spin-Statistics Theorem as a Topological Necessity") considered
for Section 7 and deferred (preprint quality bar). Section 2 genealogy gains
Laidlaw & DeWitt 1971 (fundamental-group ancestor) and Haldane 1991 (fractional statistics
beyond 2D).


---

## Addendum 2026-08-16 (v1.6 so-what cycle)

- New Section 2 "So What? Why Should a Reader Care About This Research?" added. Contains no new citations (references to DHR, Temperley-Lieb, ZX/classical structures are program-level mentions without new bib keys; all existing keys unchanged).
- Sections renumbered 2-9 -> 3-10 (So-What = 2); cross-references updated (Section 3/4/5/6 refs -> 4/5/6/7; ledger §5 -> §6). Monograph reference (Quni-Gudzinas 2026a, Section 2.3) is EXTERNAL and untouched.
- Frontmatter license aligned QNFO-ULA -> cc-by-4.0 (record metadata authoritative).
- Zenodo metadata: version v1.6; EuroSciVoc subjects (philosophy, mathematics) added.
