# Citation Audit — QNFO.RES.020 self-referential-scalar-family

**Date:** 2026-08-20 · **Standard:** P3.AUTHOR-GATE-EVERY-ENTRY-1 (every entry's author
list verified live — never a sample) · **BIB-ORPHAN-1:** every .bib entry cited in-body;
rendered bibliography count == .bib count == 20.

## Verification methods used (2026-08-20; v1.1 updated 2026-08-20)
1. **Crossref API** (`api.crossref.org/works/{doi}`) — external DOIs: title, authors,
   container, year.
2. **D1 living-paper + Vectorize search** — corpus records: title, authors, DOI match.
3. **resolve_paper_id** (slug → DOI → R2 → KG) — corpus records cross-system.
4. **doi.org HEAD** — resolution (14/14 live check performed this cycle).
5. **arXiv live search** — QND records (1811.09613, 1303.2490, quant-ph/0412149).
6. **Crossref journal-ref read-back (v1.1, per P3.AUTHOR-GATE-EVERY-ENTRY-1 extension):**
   for arXiv-cited records with a published journal version, read the `journal-ref`/
   `journal_ref` field from the Crossref record to verify the venue — arXiv metadata
   alone does NOT carry the journal. Canonical: ref [19] Sewell et al. — the arXiv
   listing omits the venue; Crossref confirms Nature Photonics 7, 517–520
   (10.1038/nphoton.2013.100). The v1.0 audit's "arXiv live search" method was a
   false-negative source for this entry; the method is now journal-ref-aware.
7. **Record creator read-back (v1.1):** for corpus records, the cited author name is
   verified against the record's own creators array (canonical: ref [9] — record
   21705220 creators = ["Quni-Gudzinas, Rowan Brad"]; the v1.0 "Quni, R." attribution
   violated NAMING-MANDATE-1 and is corrected in v1.1).

## Per-entry audit ledger

| # | Bib key | DOI / ID | Title (verified) | Authors (verified) | Venue | Year | Method | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | qunigudzinas2026reentrant | 10.5281/zenodo.21964453 | The Calculus of Re-Entrant Distinctions | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | D1/Vectorize + doi.org 200 | ✅ CLEAN |
| 2 | qunigudzinas2026bosonfermion | 10.5281/zenodo.21964598 | The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | D1/Vectorize + doi.org 200 | ✅ CLEAN |
| 3 | qunigudzinas2026exchange | 10.5281/zenodo.21964104 | The Exchange Phase as a Logical Scalar: R = e^{2πis} from the Re-Entrant Calculus | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | D1/Vectorize + doi.org 200 | ✅ CLEAN |
| 4 | qunigudzinas2026planckian | 10.5281/zenodo.18465372 | Structural Mediation of Planckian Dissipation in Strongly Correlated Electron Systems | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | D1/Vectorize + doi.org 200 | ✅ CLEAN |
| 5 | qunigudzinas2026joules | 10.5281/zenodo.21637028 | The Joules-per-Solution Metric | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | D1/Vectorize + doi.org 200 | ✅ CLEAN |
| 6 | qunigudzinas2026falsification | 10.5281/zenodo.22026562 | A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | D1/Vectorize + resolve_paper_id + doi.org 200 | ✅ CLEAN |
| 7 | qunigudzinas2026adelicshannon | 10.5281/zenodo.22024240 | Adelic Shannon Theory: From Problem Statement to Constructive Foundations | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | D1/Vectorize + resolve_paper_id + doi.org 200 | ✅ CLEAN |
| 8 | qunigudzinas2026entropic | 10.5281/zenodo.21698978 | Adelic Entropic Numbers | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | D1/Vectorize + doi.org 200 | ✅ CLEAN |
| 9 | quni2026stratigraphy | 10.5281/zenodo.21705220 | The History and Future of Measurement Stratigraphy, Number Theory, and Valuation Theory | Quni-Gudzinas, Rowan Brad | Zenodo | 2026 | D1/Vectorize + doi.org 200 + **record creator read-back** | ✅ CLEAN (v1.1: author corrected from "Quni, R." to full name per NAMING-MANDATE-1; concept DOI 21698493 verified live) |
| 10 | qunigudzinas2026onetable | 10.5281/zenodo.22024856 | One Table, Two Regimes: Standard-Model Particles and Condensed-Matter Excitations as Patterns on the Bruhat-Tits Tree | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | resolve_paper_id + D1 | ✅ CLEAN |
| 11 | qunigudzinas2026valuation | 10.5281/zenodo.21803677 | Valuation Without R: A Category-Theoretic Foundation for Finite Measurement | QNFO / Rowan Brad Quni-Gudzinas | Zenodo | 2026 | resolve_paper_id + D1 | ✅ CLEAN |
| 12 | qunigudzinas2026dissipation | 10.5281/zenodo.21940822 | From Distinction to Dissipation | Rowan Brad Quni-Gudzinas | Zenodo | 2026 | resolve_paper_id + D1 | ✅ CLEAN |
| 13 | pauli1940 | 10.1103/PhysRev.58.716 | The Connection Between Spin and Statistics | Pauli, W. | Physical Review | 1940 | Crossref | ✅ CLEAN |
| 14 | leinaasmyrheim1977 | 10.1007/BF02727953 | On the theory of identical particles | Leinaas, J.; Myrheim, J. | Il Nuovo Cimento B | 1977 | Crossref | ✅ CLEAN |
| 15 | maldacena2016bound | 10.1007/JHEP08(2016)106 | A bound on chaos | Maldacena, J.; Shenker, S.H.; Stanford, D. | JHEP | 2016 | Crossref + arXiv:1503.01409 | ✅ CLEAN |
| 16 | shannon1948 | 10.1002/j.1538-7305.1948.tb01338.x | A Mathematical Theory of Communication | Shannon, C.E. | Bell Syst. Tech. J. | 1948 | Crossref | ✅ CLEAN |
| 17 | wilczek1982 | 10.1103/PhysRevLett.49.957 | Quantum Mechanics of Fractional-Spin Particles | Wilczek, F. | Phys. Rev. Lett. | 1982 | Crossref | ✅ CLEAN |
| 18 | unnikrishnan2018qnd | arXiv:1811.09613 | Quantum non-demolition measurements: Concepts, theory and practice | Unnikrishnan, C.S. | arXiv | 2018 | arXiv live search | ✅ CLEAN |
| 19 | sewell2013certified | arXiv:1303.2490 | Certified quantum non-demolition measurement of a macroscopic material system | Sewell, R.J. et al. | Nature Photonics 7, 517–520 | 2013 | arXiv live search + **Crossref journal-ref read-back (10.1038/nphoton.2013.100)** | ✅ CLEAN (v1.1: venue corrected from "Phys. Rev. X 3, 041028" — that DOI is an unrelated paper; journal_ref verification added to the audit method) |
| 20 | ralph2004qnd | arXiv:quant-ph/0412149 | Quantum Non-demolition Measurements on Qubits | Ralph, T.C. et al. | arXiv | 2004 | arXiv live search | ✅ CLEAN |

## BIB-ORPHAN-1 check
- `.bib` entries: **20**
- In-body citations in the paper draft: **20** (each key cited at least once:
  [1]–[20] all referenced — see paper sections §2, §3, §3.4, §4, §4.3, §5.1, §5.3,
  §5.4, §9)
- Rendered bibliography expected: **20/20** — no orphans, no uncited entries.

## P3.AUTHOR-GATE confirmation
Every author list above was verified against the live registry (Crossref for 13–17,
arXiv for 18–20, D1/Vectorize/KG for 1–12). **0 fabricated attributions.**
Sample-verification was NOT used: all 20 entries were individually checked.
