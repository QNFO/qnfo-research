# Phase 2 Literature — Post-Positional Numeracy (QNFO.RES.024)

Date: 2026-08-26 · Evidence: artifacts/external-search/p2-literature/p2-literature-sweep.json (OpenAlex + Crossref, keyless polite pool) + P1 sweep evidence · Deliverable: references.bib (seed)

## 1. Sweep scope

OpenAlex (title.search "hensel codes", "p-adic reconstruction", error-free computation) + Crossref (bibliographic queries + direct DOI lookups). Result: the Hensel-code / exact-arithmetic reference base, verified author lists and bibliographic fields (P3.AUTHOR-GATE-EVERY-ENTRY-1 discipline applied at seed time).

## 2. Verified reference base (canonical records)

| Entry | Canonical record (verified) | Notes |
|---|---|---|
| Ostrowski 1916 | Acta Math. 41, 271–284, DOI 10.1007/BF02422947 | Crossref year 1916; some sources cite 1918 (volume span). The candidate DOI 10.1007/BF02422942 is Hardy–Littlewood — rejected by verification. |
| Krishnamurthy–Rao–Subramanian 1975 | Proc. Indian Acad. Sci. A 81(2), 58–79, DOI 10.1007/BF03051174 | Hensel-code origin |
| Gregory 1978 | BIT 18(3), 282–300, DOI 10.1007/BF01930898 | |
| Wang–Guy–Davenport 1982 | SIGSAM Bull. 16(2), 2–3, DOI 10.1145/1089292.1089293 | **Correction:** the Hensel-framework paper cites 1981, SIGSAM 15(4), 7–10 — imprecise year/volume. Our paper cites the canonical record. |
| Dixon 1982 | Numer. Math. 40(1), 137–141, DOI 10.1007/BF01459082 | |
| Miola 1982 | SIGSAM Bull., DOI 10.1145/1089310.1089316 | |
| Kornerup–Gregory 1983 | BIT, DOI 10.1007/BF01937322 | Two-sided Farey window — direct ancestor of our injectivity window |
| Krishnamurthy 1983 | IEEE Trans. Comput., DOI 10.1109/TC.1983.1676233 | |
| Rao 1984 | Comput. Math. Appl., DOI 10.1016/0898-1221(84)90048-8 | |
| Gregory–Krishnamurthy 1984 | Springer book, DOI 10.1007/978-1-4612-5242-9 | |
| Boehm–Decker–Fieker–Pfister 2015 | Math. Comp. 84(296), 3013–3027, DOI 10.1090/mcom/2951 | Bad primes + CRT/Farey; no product-formula invariant |
| Doris 2021 | J. Symb. Comput. 104, 476–493, DOI 10.1016/j.jsc.2020.08.005 | Magma exact p-adics |
| Abbondati–Guerrini–Lebreton 2026 | J. Symb. Comput. 132, 102481, DOI 10.1016/j.jsc.2025.102481 | **Closest external work** — see §4 |

Plus: Hieronymi–Terry (Ostrowski numeration, terminology disambiguation), Tate 1967 (product formula), Hensel 1908 (book), and the QNFO ancestors (DOIs live-verified in P1).

## 3. KIF-18 symmetry classification (support / complicate / contradict)

- **SUPPORT (foundation):** Krishnamurthy–Rao–Subramanian 1975; Gregory 1978; Wang–Guy–Davenport 1982; Dixon 1982; Miola 1982; Kornerup–Gregory 1983; Krishnamurthy 1983; Rao 1984; Gregory–Krishnamurthy 1984; Boehm et al. 2015; Doris 2021. All establish single-place Hensel-code arithmetic, CRT+Farey reconstruction, and bad-prime handling — the machinery our multi-place encoding extends.
- **SUPPORT (adjacent):** the QNFO ancestors (Hensel framework v1.2.0 single-place implementation; Silent Radix; NUMERATA; Decimal Fingers; Nonlinear Tree-Based; Ultrametric Foundation v2).
- **COMPLICATE (novelty margin):** Abbondati–Guerrini–Lebreton 2026 — "simultaneous rational number codes" occupy the multi-place decoder space (multiplicity decoding, bad primes, beyond-half-minimum-distance). They do NOT use the adelic product formula as a reconstruction invariant; H-PPN-4's adjudicated conjunction (multi-place + product-formula invariant) stands, but the paper must cite and differentiate from this work explicitly.
- **COMPLICATE (terminology):** the "Ostrowski numeration systems" literature (Hieronymi–Terry et al.) — unrelated sense (continued-fraction numeration); the paper's crosswalk disambiguates.
- **CONTRADICT:** none identified. Stated explicitly: no surveyed record contradicts the multi-place encoding or the product-formula invariant claims.

## 4. Novelty-adjacency adjudication (AGL 2026)

Abbondati–Guerrini–Lebreton, "Simultaneous rational number codes" (JSC 132:102481, 2026): multi-prime simultaneous decoding using multiplicity codes and bad-prime detection, decoding beyond half the minimum distance. Overlap with C1′: multi-place (simultaneous) rational encoding + reconstruction. Non-overlap (the delta): (a) the adelic product formula ∏_{v∈S∪{∞}}|x|_v as a machine-checkable round-trip invariant and failure localizer; (b) the explicit numeration framing (post-positional numeracy) with the QNFO ancestor line; (c) the two-sided-window injectivity stated and verified as a numeration theorem with seeded trials + demo. H-PPN-4 updated to name this record; the paper's related-work section leads with it.

## 5. Citation corrections applied to the package (this cycle)

1. Wang–Guy–Davenport year/venue: "1981" → canonical 1982 (SIGSAM 16(2), 2–3) — fixed in PROJECT-PLAN L0 and deep-research §3 (with the ancestor's imprecision flagged, not hidden).
2. Ostrowski: exact citation + DOI 10.1007/BF02422947 added to L0 (1916 per Crossref).
3. L0 Hensel-code construction now names Krishnamurthy–Rao–Subramanian 1975 + Gregory–Krishnamurthy 1984.

## 6. P3-VERIFY flags (Phase 3 full-verification list)

- Hieronymi–Terry published venue (arXiv-only in seed).
- Tate 1967 pages/edition.
- Hensel 1908 book details.
- Ten-Fingered Trap / Explicit Frame Pattern Language (no DOIs — cite via R2 archive key / note).
- Krishnamurthy 1983 IEEE pages; Miola 1982 pages; Kornerup–Gregory 1983 volume/pages.
