# F1 Level-Assignment Sweep — QNFO.RES.032 Phase 1 (M1)

- **Date:** 2026-08-29 · **WBS:** QNFO.RES.032.P1
- **Claim under test:** F1 — the nine-level ladder covers the published lineage without remainder; every published object assigns to at least one level or declared span.
- **Method:** one evidence file per record; each assignment cites a concrete published object (title/DOI), not a family resemblance (UIA Q1 countermeasure). The two provisional rows published with v0.1 are adjudicated on evidence.
- **Instrument:** UIA applied at docs/uia-15q-res032.md.

## Verdict

**F1 CONFIRMED — 7/7 records assign to ≥1 level/span. Two provisional rows adjudicated, both corrected:**

1. **RES.029 — D7 REMOVED.** The provisional measurement-level (D7) assignment fails the DPRF's own D7 definition (finite-resolution application of valuation to observation: protocol, instrument, resolution, noise budget). RES.029's practitioner crosswalk contains no measurement protocol, instrument, or resolution content; it operationalizes the correspondence (what a practitioner does with the map) — that is D6, distinction made operational. Final assignment: **D2, D4, D6**. Provisional flag retired.
2. **RES.021 — "D8-adjacent" is not a level.** The published cell "D0–D2, D8-adjacent" violates R1 (a claim declares its level; intent markers are not levels). The record's formal content is finite-distinction structure: distinctions (D0), their ordering (D1), their counting (D2). Its QM-application intent is a charter statement, not a level assignment. Final assignment: **span D0–D2 with declared bridges D0→D1 (relate cuts), D1→D2 (count)**. Provisional flag retired.

## Per-record evidence

| # | Record | DOI | Final levels | Status |
|:-:|:-------|:----|:-------------|:-------|
| 1 | UMP.014 | 10.5281/zenodo.22150472 | D1, D4, D5 (+D7/D8 benchmark arm) | confirmed |
| 2 | RES.021 | 10.5281/zenodo.22046458 | D0–D2 span (bridges declared) | adjudicated (was provisional) |
| 3 | RES.027 | 10.5281/zenodo.22133122 | D2, D4 | confirmed |
| 4 | RES.028 | 10.5281/zenodo.22124744 | D2, D4 | confirmed |
| 5 | RES.029 | 10.5281/zenodo.22142794 | D2, D4, D6 | adjudicated (D7 removed) |
| 6 | RES.030 | 10.5281/zenodo.22152967 | D3, D6, D7 | confirmed |
| 7 | RES.031 | (in preparation) | D0–D8 span (L0→D0; L1→D1/D4/D5; L2→D2/D3; L3→D6/D7; L4→D7/D8) | confirmed (cross-walk) |

## Gap analysis (SO-WHAT)

- **GAP-1 (closed):** the D7 assignment was generous pre-evidence; adjudicated by the record's own definition.
- **GAP-2 (rule fix needed):** pseudo-level tags ("D8-adjacent") — R1 gains an explicit note in v0.2: intent markers are charter statements, not levels.
- **GAP-3 (CONFIRMATION-BIAS-RISK, external gap):** the full-corpus sweep returned 100% QNFO-internal hits; external prior art for the two boundary rules and the primon-gas construction exists (Korzybski 1933; Ladyman–Ross 2007; Hartmann levels-of-reality; Julia 1990; Spector 1990; Bakas–Bowick 1991; Bost–Connes 1995) and must be cited in v0.2 so the novelty claim is scoped to *operationalization*. External-verification evidence: artifacts/external-search/external-verification-dprf-2026-08-29.json.
- **GAP-4 (cross-links):** same-program precedents for the boundary rules found in the sweep — conditional-truths-locale-framework (map-territory + ontic structural realism import; UMP.011), zx-diagram-fault-lines (the "cafeteria problem" seam), cancellation-rule (Spencer-Brown boundary ontology; SLB). v0.2 cites these as program-internal precedents (BRIDGES edges candidates).
- **Data-quality finding (referred, not DPRF's):** conditional-truths-locale-framework carries three differing Zenodo IDs across papers-table fields (21984929 / 21983659 / 21983324) — DOI-DISCREPANCY-RESOLVE-1 territory for that record's own audit; the sweep cites it via the papers-table doi field.
