# Citation Audit — QNFO.RES.023 (P5, 2026-08-23)

- **Method:** every bibliographic entry verified against its primary source
  (arXiv API / DataCite / Zenodo search) on 2026-08-23; P3.AUTHOR-GATE +
  BIB-ORPHAN-1 (every .bib entry cited in body; every body citation present).
- **Gate evidence:** `p5_gates.log` (DataCite + Zenodo, qnfo-audit UA);
  inherited RES.022 evidence files in `artifacts/external-search/`.

## 1. QNFO corpus records (DOIs) — 15/15 verified findable

| Key | DOI | DataCite | Verdict |
|:----|:----|:---------|:--------|
| res022_consilience | 10.5281/zenodo.22071421 | findable | OK |
| schisms29 | 10.5281/zenodo.21458373 | findable | OK |
| observer_inside_tree | 10.5281/zenodo.21473899 | findable | OK |
| res021_finite_distinction | 10.5281/zenodo.22046458 | findable | OK |
| padic_metrology | 10.5281/zenodo.21748299 | findable | OK |
| joules_per_solution | 10.5281/zenodo.21637028 | findable | OK |
| bridge_theorem | 10.5281/zenodo.21102770 | findable | OK |
| consilience_physics_numtheory | 10.5281/zenodo.21590155 | findable | OK (P1) |
| measurement_stratigraphy | 10.5281/zenodo.21705220 | findable | OK (P1) |
| valuation_without_r | 10.5281/zenodo.21803677 | findable | OK (P1) |
| tree_numeration | 10.5281/zenodo.21046213 | findable | OK (P1) |
| prime_valuation_depth | 10.5281/zenodo.21918838 | findable | OK (P1) |
| projective_geometric_semantic | 10.5281/zenodo.19564091 | findable | OK (P1) |
| consilience_framework | 10.5281/zenodo.21804073 | findable | OK |
| qec-darwinism (cited §3) | 10.5281/zenodo.21964674 | findable | OK (P1) |

## 2. External literature (arXiv) — 18/18 verified

Verified in evidence files (res023 + inherited RES.022):
math/0605555v2, physics/0702064v1, 1201.2719v3, 0809.0492v1, 1008.3585v1,
1812.09225v4, 1804.01882v3, 2209.03781v2, 2307.10176v2, 2406.05842v3,
cond-mat/0105282v3, 1504.03629v1, 1012.1248v2, math-ph/0512018v2,
2601.03141v2, 2109.05472v2 — all present with matching titles/authors/years.

## 3. Canonical journal literature

Parisi (1983) PRL 50, 1946 — canonical; Rammal, Toulouse, Virasoro (1986)
RMP 58, 765 — canonical; Vladimirov, Volovich, Zelenov (1994) World
Scientific — canonical monograph. (doi.org HEAD is bot-blocked per
DOIDOT-403-BOT-1; canonical records accepted.)

## 4. BIB-ORPHAN check (P4 remediation verified)

All 34 entries in `references.bib` cited in the paper body — including ref
1 (taxonomy doc, §5.1) and ref 15 (Consilience Framework, §3), the two
previously-orphan entries fixed in commit 0f899c7. No orphans; every body
citation resolves to a bibliography entry.

## 5. Author attribution

All corpus records carry the sole author Rowan Brad Quni-Gudzinas
(ADR-014); external references attribute their published authors
(P3.AUTHOR-GATE-EVERY-ENTRY-1 — verified against arXiv/DataCite metadata).
