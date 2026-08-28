# Phase 1 — Cross-System ID Validation + External Verification Evidence (QNFO.RES.030)

Date: 2026-08-29. Method: resolve_paper_id per key hit (slug → Vectorize → KG → DOI).
A mismatch is a data-quality finding, not a footnote.

## Cross-system validation table

| slug | papers-table DOI | KG node DOI | verdict |
|---|---|---|---|
| arithmetic-anyon-contact | 10.5281/zenodo.22124744 | 10.5281/zenodo.22124744 (concept 22124743) | CLEAN |
| adelic-quantum-arithmetic | 10.5281/zenodo.22142794 | doi 22142794, but KG `zenodo_doi`=22133706 | **F1 stale KG zenodo_doi** |
| adelic-quantum-statistics | 10.5281/zenodo.22133122 | doi 10.5281/zenodo.22123068 (concept 22123067) | **F2 dual-version DOI ambiguity** |
| self-referential-scalar-family | 10.5281/zenodo.22035210 | 22035210 (KG zenodo_doi 22031551) | CLEAN (concept vs record) |
| distinction-based-ultrametric | 10.5281/zenodo.22150472 | Paper node named by title, not slug | F5 minor indexing note |
| finite-distinction-quantum-mechanics | 10.5281/zenodo.22046458 (concept 22044217, id 22044379) | 22046458, duplicate_chain_head 22046491 | documented duplicate chain |
| prime-valuation-qec-implications | resolve: 10.5281/zenodo.21979060 | registry RES.006: 10.5281/zenodo.21928947 | **F3 registry vs resolve mismatch** |
| prime-numbers-as-spectral-artifacts | DOI NULL in D1; body carries 10.5281/zenodo.17566147 | internal id only | **F4 DOI not indexed in D1** |
| radix-agnostic-dsi-detection | 10.5281/zenodo.21902891 | matches KG Paper node | CLEAN |
| scientific-validity-assessment-toolkit-svat | no DOI (2025-09 record) | internal id | expected pre-DOI |
| pattern-particle-unification | 10.5281/zenodo.22024856 | match | CLEAN |
| p-adic-anyon-fusion-braiding | 10.5281/zenodo.21208491 | match | CLEAN |
| qwave-qudit-advantage | 10.5281/zenodo.21880104 | match | CLEAN |
| spectral-benchmarking-of-holographic-quantum-simulations | no DOI (2026-01) | internal id | expected |
| spectral-dynamics-on-bruhat-tits-trees | no DOI (2026-02) | internal id | expected |

Findings F1–F4 are registry hygiene items for the QNFO data pipeline (flagged;
not blocking for RES.030, whose citations will use the registry-canonical DOIs
after P3 citation audit).

## External verification probes (independent of the QNFO corpus)

1. **arXiv API** `all:"primon gas" OR all:"Riemann gas"` → 5 results, top 3:
   - Hartnoll & Yang, "The Conformal Primon Gas at the End of Time", arXiv:2502.02661v2 (hep-th, 2025-02; v2 2025-06). L-function partition functions, modular-invariant states, dual primon gas, fermionic primon Witten index. **Directly relevant external literature.**
   - Dueñas & Svaiter, "Thermodynamics of the Bosonic Randomized Riemann Gas", arXiv:1401.8190v3 (math-ph, 2014). Zeta-pole critical temperature; ensemble-over-hamiltonians (randomized gas). **Null-model-adjacent: randomization over an ensemble is the external cousin of the matched-density null.** (Svaiter is already in the RES.028 outreach queue.)
   - "P-adic numbers and kernels", arXiv:2411.15377v3 (cond-mat, 2024). Kernel representation of the primon gas on a finite p-base via large-deviation theory (Derrida GREM).
2. **Crossref** `Bakas+Bowick` → "Curiosities of arithmetic gases", J. Math. Phys. 32(7) 1881–1884 (1991), DOI 10.1063/1.529511, 22 citations. VERIFIED.
3. **Crossref** `Julia statistical theory of numbers` → B. Julia, "Statistical Theory of Numbers", in Number Theory and Physics (Springer Proc. Phys., 1990), pp. 276–293, DOI 10.1007/978-3-642-75405-0_30, 30 citations; cites B.L. Julia, J. Phys. France 50 (1989) 1371, DOI 10.1051/jphys:0198900500120137100. VERIFIED — the primon-gas origin record.
4. **OpenAlex** `search=primon gas specific heat` → HTTP 429 (rate-limited). Retry at P2. (probe evidence)
5. **archive.org CDX** `zenodo.org/records/22124744` → `[]` — RES.028 not yet Wayback-archived. Action item for P7 (Internet Archive submission).
6. **Google Patents** → XHR endpoint HTTP 503; DuckDuckGo router "search engine unreachable" (2 attempts). Documented blocked path; remediation at P7 (retry or local 03-PATENTS archive).

## External lineage (verified, must be cited in RES.030 related work)

Julia 1989/1990 → Bakas & Bowick 1991 → Spector 1990 → Dueñas & Svaiter 2014
→ p-adic kernels 2024 → Hartnoll & Yang 2025.
The QNFO records RES.027–029 cite Montgomery/Odlyzko/Gallagher/Bogomolny but
the visible bodies do not carry this primon-gas lineage; RES.030 will carry it
explicitly (P2/P5 item).
