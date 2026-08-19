# Citation Audit — RES.017 (P3.AUTHOR-GATE)

**Entries:** 39. **Method:** every entry verified against a live source this session
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
| quni2026zbwp1 | Zenodo REST API live (title verified: Zitterbewegung as the Physical Realization of p-Adic Anyon Braiding) | PASS |
| fivepillars2026 | Zenodo REST API live | PASS |
| adeliccore2026 | Zenodo REST API live | PASS |
| quni2026qfund | Zenodo REST API live | PASS |
| quni2026continuum1 | Zenodo REST API live (Continuum Trilogy Papers I–III bundle) | PASS |
| quni2026nonanthro | Zenodo REST API live | PASS |
| uia2026 | Zenodo REST API live | PASS |
| iaps2026 | Zenodo REST API live | PASS |

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

## Input-record rows (16, live-verified 2026-08-19 via Zenodo REST)

| DOI | Title |
|:----|:------|
| 10.5281/zenodo.17794233 | Autonomous Dissipative Stabilization of Gottesman-Kitaev-Preskill States in Room-Temperature Ion Traps |
| 10.5281/zenodo.18522367 | Quantum Architectonics: The Passive Path to Scale |
| 10.5281/zenodo.18606514 | Spectral Analysis of Anomalous Diffusion on p-Adic Fractals |
| 10.5281/zenodo.19605446 | The Meta-Pattern of Reification in Physics |
| 10.5281/zenodo.20411697 | The Spin-Free Substrate (v1.0, PDF record) |
| 10.5281/zenodo.20411734 | The Spin-Free Substrate (md record) |
| 10.5281/zenodo.21120469 | Trapped-Ion Page-Wootters Experiment: Protocol for Testing Ultrametricity |
| 10.5281/zenodo.21221899 | Vortex-Enhanced Zitterbewegung: Trapped-Ion Dirac Simulators |
| 10.5281/zenodo.21336123 | Vortex-Enhanced Zitterbewegung: Trapped-Ion Systems |
| 10.5281/zenodo.21566035 | Auditing the BQNN |
| 10.5281/zenodo.21600628 | Zitterbewegung: From Archimedean Puzzle to Adelic Observable |
| 10.5281/zenodo.21754024 | The Ostrowski Dimensionless Reformulation |
| 10.5281/zenodo.21791457 | The Falsifiability Crisis in Contemporary Physics |
| 10.5281/zenodo.21820137 | Tensor Networks as Bruhat-Tits Tree Computation |
| 10.5281/zenodo.21879231 | Trapped-Ion Qudit Quantum Computing: Ringbauer Due-Diligence |
| 10.5281/zenodo.21993655 | Reassessing the Foundations of Quantum Computation |
