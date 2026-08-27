# Citation Audit — QNFO.RES.027 (2026-08-27)

- **Method:** every reference verified against an authoritative source before inclusion in `references.bib`; the rendered reference list is produced by pandoc/citeproc FROM the bib (never hand-typed — REFERENCE-RENDER-FROM-BIB-1); every bib entry is cited in-text (BIB-ORPHAN-1: zero orphans).
- **Totals:** 33 bib entries = 33 in-text citation keys. Rendered `csl-entry` count in the built HTML: 33. Orphans: none. Missing keys: none.

## Verification sources

| Source | Entries | Method |
|---|---|---|
| arXiv API (export.arxiv.org) | 4 | title + author list confirmed (2308.05203 Wang–Hazzard; 2502.02661 Hartnoll–Yang; 2505.17361 Zhou–Chen–Chen–Shen–Zhang–Dai; 2306.05919 Medina Sánchez–Dakić) |
| Crossref | 12 | bibliographic search + targeted DOI checks: Spector 1990 (CMP 127:239–252, 10.1007/bf02096755); Bakas–Bowick 1991 (JMP 32:1881–1884, 10.1063/1.529511); Leinaas–Myrheim 1977 (Nuovo Cimento B 37, 10.1007/BF02727953); Wilczek 1982 (PRL 49:957–959, 10.1103/physrevlett.49.957); Kitaev 2003 (Ann. Phys. 303:2–30); Kitaev 2006 (Ann. Phys. 321:2–111); Nayak et al. 2008 (RMP 80:1083, 10.1103/RevModPhys.80.1083); DHR 1971/1974 (CMP 23:199–230, 35:49–85); Pauli 1940 (Phys. Rev. 58:716, 10.1103/PhysRev.58.716); Duck–Sudarshan 1998 (World Scientific) |
| Crossref (venue-only) | 1 | Julia 1990 chapter "Statistical theory of numbers" in *Number Theory and Physics* (Springer Proc. Phys. 47): the chapter has no Crossref DOI (book-level DOI 404); cited as an incollection with the canonical venue data and an explicit note. |
| Zenodo records API | 17 | title + publication_date fetched per record; DOIs already validated in the round-2 dependency pass (15/15) and the records-API concept checks. |

## Cross-check evidence

- Evidence files: `artifacts/external-search/crossref-verify-2026-08-27.txt`, `artifacts/external-search/doi-check-2026-08-27.txt`.
- In-text citation keys (29 pre-extension → 33 post-extension) cover every bib entry; the canon citations were added at their sections: Leinaas–Myrheim/Wilczek (§6.2, abelian anyons), Kitaev×2/Nayak (§6.2, non-abelian), DHR I/II (§9, locality boundary), Pauli/Duck–Sudarshan (§1, spin-statistics), Hartnoll–Yang/Zhou/Medina Sánchez–Dakić (§1, §6.3), and the corpus-adjacent records (pattern-particle-unification, consilience, p-adic spin, from-distinction-to-dissipation, zbw-majorana/capstone, operationalizing-generalized-symmetries) at their sections.

## Rendering

- pandoc + citeproc + MathJax: HTML built; DOM checks `merrorCount=0`, `U+FFFD=false`, `h1.title=1`, `bodyH1=0`, `refs=33`, `abstractDivs=1`.
- PDF: Edge headless via puppeteer-core with explicit `displayHeaderFooter: false` (PDF-NO-BROWSER-CHROME-1).
- `check_rendering.py`: all 10 gates PASS (odd-$, currency-unescaped, Unicode math glyphs, bare pipe cells, body byline dup, body H1 dup, HTML one-title, HTML no-body-H1, HTML one-abstract, HTML no-FFFD).
