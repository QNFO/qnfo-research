# Citation Audit — RES.017 (P3.AUTHOR-GATE)

**Entries:** 31. **Method:** every entry verified against a live source this session
(2026-08-19), except the three REPORTED-BUT-UNVERIFIED external items below.

## Verification per entry

| Entry | Verification source | Status |
|:------|:--------------------|:-------|
| 16 input records | Zenodo REST API (records fetched live; title/DOI/date captured in zenodo_abs_out.txt) | PASS |
| quni2026pwdistances (21120286) | Zenodo REST API live | PASS |
| quni2026bridge (21102770) | Zenodo REST API live | PASS |
| quni2026metrology (21748299) | Zenodo REST API live | PASS |
| qnfo2026uf (21193487) | Zenodo REST API live | PASS |
| quni2026quditadv (21827737) | Zenodo REST API live | PASS |
| qnfo2026jpcubcl (21821767) | Zenodo REST API live | PASS |
| fisher2015 | Crossref api.crossref.org/works/10.1016/j.aop.2015.08.020 — Matthew P.A. Fisher, Ann. Phys. 362 (2015) | PASS |
| pagewootters1983 | Crossref 10.1103/PhysRevD.27.2885 | PASS |
| white1992 | Crossref 10.1103/PhysRevLett.69.2863 | PASS |
| berrykeating1999 | Crossref 10.1137/S0036144598347497 | PASS |
| dirac1928 | Crossref 10.1098/rspa.1928.0023 | PASS |
| ringbauer2022 | Crossref 10.1038/s41567-022-01658-0 (Nature Physics 18, 2022-07-21) | PASS |
| ringbauer2023 | Crossref 10.1038/s41467-023-37375-2 (Nature Communications 14) | PASS |
| ringbauer2024 | Crossref 10.1103/PRXQuantum.5.040309 | PASS |
| ostrowski1916 | Crossref bibliographic search → reprint DOI 10.1007/978-3-0348-9358-9_17 (pre-DOI original: Acta Math. 41, 271–284) | PASS (reprint) |

## REPORTED-BUT-UNVERIFIED (not in .bib as standalone entries)

- Guo, Xu & Gu (2025) vortex-enhanced ZBW mechanism, arXiv:2511.21142 — reported in
  10.5281/zenodo.21221899. arXiv API returned HTTP 429 for the entire session (IP-level
  ban after initial scripted queries); the paper attributes this work via the Zenodo record
  that cites it and does NOT fabricate a verification claim.
- Predin (2026) areal-rate observable — same: attributed via 10.5281/zenodo.21221899.
- Simons/Flatiron 2026 tensor-network result — attributed via 10.5281/zenodo.21820137.

**Duplicate-key check:** all 31 keys unique (manual scan; no merge operation performed).

## DOI title-match check (wrong-DOI guard)

- 10.1016/j.aop.2015.04.013 was EXCLUDED: Crossref shows it is "Shape invariant
  potentials in higher dimensions" (Sandhya) — the correct Fisher Posner DOI is
  10.1016/j.aop.2015.08.020. This wrong-DOI risk was caught live.
- All Zenodo DOIs resolve to the titles recorded in the input-record table (README.md).
