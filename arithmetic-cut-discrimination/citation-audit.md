# Citation Audit — QNFO.RES.030

Date: 2026-08-29T03:32Z. Method: Crossref API for journal DOIs, DataCite API
for Zenodo DOIs, arXiv export API for eprint metadata (authoritative authors).
Evidence file: `artifacts/verification/citation-audit-output.json` (19 refs
checked). Re-verification of the four corrected DOIs: Crossref bibliographic
search, executed 2026-08-29.

## Results

| Ref key | Status | Note |
|---|---|---|
| julia1990statistical | FOUND | 10.1007/978-3-642-75405-0_30 — Statistical Theory of Numbers |
| julia1989statistics | FOUND | 10.1051/jphys:0198900500120137100 — title corrected to "On the 'statistics' of primes" |
| bakas1991curiosities | FOUND | 10.1063/1.529511 — Curiosities of arithmetic gases |
| spector1990supersymmetry | FOUND | 10.1007/BF02096755 — Supersymmetry and the Möbius inversion function (CMP 127, 1990; corrected from the Phys. Lett. A Dirichlet-convolution paper) |
| duenas2014thermodynamics | FOUND | arXiv:1401.8190v3 — authors Dueñas, Svaiter (verified from arXiv API) |
| hartnoll2025conformal | FOUND | arXiv:2502.02661v2 — Hartnoll, Yang |
| franchini2024padic | FOUND | arXiv:2411.15377v3 — **author corrected to Simone Franchini (solo)**; the earlier draft's author list was replaced |
| montgomery1973pair | FOUND | DOI corrected to 10.1090/pspum/024/9944 (original 0337821 → 404) |
| odlyzko1987distribution | FOUND | 10.1090/S0025-5718-1987-0866115-0 |
| gallagher1976distribution | FOUND | DOI corrected to 10.1112/s0025579300016442; **year corrected to 1976** (original 1985/10.1112...901090 → 404) |
| berry1985semiclassical | FOUND | 10.1098/rspa.1985.0078 |
| bogomolny1996gutzwiller | FOUND | 10.1103/PhysRevLett.77.1472 |
| bost1995hecke | FOUND | DOI corrected to 10.1007/bf01589495 (original 10.1007/BF01553491 resolves to an unrelated adenovirus paper) |
| dyson1962statistical | FOUND | 10.1063/1.1703773 |
| mehta2004random | (book) | no DOI — standard monograph citation |
| quni2026ump014 | FOUND | DataCite — The Distinction-Based Ultrametric (10.5281/zenodo.22150472) |
| quni2026stats | FOUND | DataCite — Quantum Statistics from the Adelic Product Formula (10.5281/zenodo.22133122) |
| quni2026anyons | FOUND | DataCite — Arithmetic Anyons (10.5281/zenodo.22124744) |
| quni2026adelic | FOUND | DataCite — Adelic Quantum Arithmetic (10.5281/zenodo.22142794) |
| quni2026program | FOUND | DataCite — The Ultrametric Program (10.5281/zenodo.22076816) |
| quni2026hd3 | FOUND | OSF osf.io/ba8ns (verified via OSF API in Phase 1) |

## Defects caught and corrected by this audit (P3.AUTHOR-GATE + P3.SOURCE-DISCIPLINE)

1. **franchini2024padic**: fabricated multi-author list in the initial bib →
   replaced by the arXiv-verified single author Simone Franchini.
2. **bost1995hecke**: wrong DOI (resolved to an unrelated paper) → corrected.
3. **montgomery1973pair**: wrong DOI (404) → corrected.
4. **gallagher**: wrong year (1985) and DOI (404) → corrected to 1976.
5. **julia1989**: title corrected.
6. **spector**: wrong paper/DOI for the supersymmetry claim → corrected to the
   CMP 1990 record.

Every corrected value was re-verified by live Crossref bibliographic search in
the same session (executed evidence in the session record). The paper's
reference list renders from `references.bib` via pandoc-citeproc
(REFERENCE-TITLE-FIDELITY-1): 16 cited references render in the built HTML.
