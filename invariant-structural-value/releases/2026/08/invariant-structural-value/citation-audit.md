# Citation Audit — Phase 3 (QNFO.RES.007)

**Project:** Invariant Structural Value
**Date:** 2026-08-14
**Branch:** res/paper/invariant-structural-value
**WBS:** QNFO.RES.007
**Gate:** P3.AUTHOR-GATE (HARD) — every entry verified against live registry metadata before commit
**Post-publication audit:** reviewer-subagent red-team (2026-08-14) found HARD-1 (duplicate work + synthetic DOI), HARD-2 (work-level accounting), HARD-3 (BP-10 count) — all remediated in this revision (v0.2, newversion 21929480). See §8.

## 1. Summary

| Metric | Value |
|:-------|:------|
| Bibliography entries (`artifacts/references.bib`) | **42** (unique works) |
| Live-verified via Crossref API | 14 (incl. Worrall 1989, French-Ladyman 2003, Joyal-Street 1993) |
| Live-verified via DataCite API (Zenodo records) | 16 |
| Live-verified via arXiv API | 10 |
| Canonical/manual entries (books w/o DOI) | 1 (Spencer-Brown 1969 — no DOI exists; flagged MANUAL) |
| Preprints verified as preprints | 2 (Abbas 2026, Zhang et al. 2026 — Crossref-verified, cited as preprints) |
| DOI corrections applied (P3.AUTHOR-GATE caught) | **6** |
| Duplicate keys | 0 |
| Duplicate works (post-fix) | 0 (1 found + removed: joyal1986) |
| Synthetic DOIs (post-fix) | 0 (1 found + fixed: joyalstreet1986 -> 10.1006/aima.1993.1055) |

## 2. P3.AUTHOR-GATE Findings (DOI corrections — all evidence saved)

| Entry | Review DOI (WRONG) | Verified DOI (CORRECT) | Evidence |
|:------|:-------------------|:-----------------------|:---------|
| Worrall, *Structural Realism: The Best of Both Worlds?* (1989) | 10.1086/289085 (resolved to *Capital, Profits and Prices* by John McMillan — wrong book) | **10.1111/j.1746-8361.1989.tb00933.x** (Dialectica 43:99–124) | phase3-canonical-search.json; phase3-canonical-verification.json |
| French & Ladyman, *Remodelling Structural Realism* (2003) | 10.1016/S0039-3681(03)00021-8 (404) | **10.1023/a:1024156116636** (Synthese 136:31–56) | phase3-canonical-search.json; phase3-canonical-verification.json |
| Esfeld & Lam, *Moderate structural realism about space-time* (2008) | 10.1007/s11229-006-9076-8 (404) | **10.1007/s11229-006-9076-2** (Synthese) | phase3-datacite-verification.json |
| Kapustin & Witten, *Electric-magnetic duality and the geometric Langlands program* (2007) | 10.4310/cntp.2007.v1.n1 (404) | **10.4310/CNTP.2007.v1.n1.a1** | phase3-datacite-verification.json |
| Peebles & Ratra, *The cosmological constant and dark energy* (2003) | 10.1103/revmodphys.75.55 (404) | **10.1103/RevModPhys.75.559** | phase3-datacite-verification.json |
| Joyal & Street, *Braided Tensor Categories* (1993) | `doi = {joyalstreet1986}` (citation key masquerading as DOI — synthetic anchor, 404 both registries) | **10.1006/aima.1993.1055** (Adv. Math. 102:20–78, 1993) | reviewer-subagent live check; phase3-canonical-verification.json |

## 3. Verification Method Per Entry

- **Crossref (14 entries):** live Crossref API — title + author list + journal + volume + year + DOI match. Includes Worrall 1989, French-Ladyman 2003, Joyal-Street 1993 (re-verified after correction).
- **DataCite/Zenodo (16 entries):** live DataCite API — all QNFO-owned records verified (ODR v4.0.4, QM-IGS, α Cross-Ratio, STC, α-π-Helix, QLoF, Calculus of Distinction, Computable Real Boundary, Base-Invariant, Winding Numbers, Strange Loop, Notation Problem, Adelic Core, Adelic Constraints, R1/R2 contrast records with correct real authors).
- **arXiv (10 entries):** live arXiv API — title, authors, raw XML saved.
- **Canonical (1):** Spencer-Brown 1969, *Laws of Form* (Allen & Unwin) — no DOI registered (book predates DOI); flagged MANUAL.
- **Preprints (2):** Abbas 2026 (Research Square), Zhang et al. 2026 (Preprints.org) — Crossref-verified, cited as preprints per deficit register.

## 4. Three-Count Audit (P3.SOURCE-DISCIPLINE)

- Queries sent: 29 (Crossref) + 16 (DataCite) + 10 (arXiv) + 2 (Crossref canonical search) = **57**
- Sources received (verified unique works): **42**
- Sources cited in references.bib: **42**
- Cited > received? **NO** — no fabrication possible.

## 5. Duplicate Check

- Regex key-level scan: **42 unique keys, 0 duplicates**.
- Work-level scan (normalized title+author+year): **42 unique works, 0 duplicates** — 1 duplicate (joyal1986, same work as joyalstreet1986) was found by the reviewer subagent post-publication and **removed** in this revision.
- DOI-format scan: **0 non-DOI strings in doi fields** — the synthetic `doi = {joyalstreet1986}` was fixed to the real DOI.

## 6. Open Items (deferred)

1. **Adelic Constraints Project null (R3)** — full engagement in C1 section (deficit register item 2). P4 manuscript addresses structurally (C1 = role, not derivation).
2. **C3 constructive derivation** — completed in P4 (01f4018): fixed-point equations for e (self-application) and π (self-closure), KIF-60 surprise accounting in BP-8.
3. **BP-10 independent recompute** — completed: fit-verify.txt (e series/limit, Machin/Leibniz π, Euler identity, periodicity, f′=f).

## 7. Conclusion

P3 complete: 42-entry bibliography (unique works), all entries live-verified, 6 wrong/synthetic DOIs corrected (the exact failure class P3.AUTHOR-GATE exists to catch), 0 duplicates, 0 synthetic anchors.

## 8. Post-Publication Audit Remediation (v0.2)

Reviewer subagent (2026-08-14, red-team) returned FAIL on the published v0.1 bibliography:
- HARD-1: duplicate work joyal1986 (doi={joyalstreet1986} synthetic) — FIXED (removed dup; real DOI 10.1006/aima.1993.1055 added).
- HARD-2: accounting double-counted Joyal-Street + Worrall 1989 mislabeled canonical — FIXED (§1, §4 corrected to 42 unique works).
- HARD-3: BP-10 claimed "51/51" and "OpenAlex" — FIXED in bp-gates.md (correct counts, Crossref/DataCite/arXiv only).
- HARD-4: registry year drift "Joyal-Street 1991" vs 1986/1993 — FIXED (bib key joyalstreet1993 referenced).
- SOFT: ladyman2007 "and and", ladyman2013 publisher spacing, landry/worrall entry types — FIXED.
All fixes committed (post-audit commit 09af444); newversion **21929590** (DOI 10.5281/zenodo.21929590, v0.2) carries the corrected artifacts. Original published record 21929479 untouched.
