# Citation Audit — QNFO.RES.021 (P3, 2026-08-20)

**Gate:** P3.AUTHOR-GATE-EVERY-ENTRY-1 — EVERY entry's author list verified live
against arXiv API / Crossref / Zenodo API on 2026-08-20. **No sampling.** The RES.016
lesson (3 fabricated attributions missed by spot-checks) is the reason for full
enumeration. Verification evidence: same-turn tool outputs (get_abstract ×14, Crossref
REST ×4, Zenodo records API ×11); script `fetch_authors.py` output archived in the
session tape (temp, deleted at closeout per FILE HYGIENE — re-runnable one-liner in
`artifacts/external-search/evidence-2026-08-20.md` §4–5).

## Per-entry verification table (28 entries)

| Key | Title (abbrev.) | Verified authors | Source | Status |
|---|---|---|---|---|
| gisin2018real | Are Real Numbers Really Real? | Gisin | arXiv API 1803.06824v3 | PASS |
| delsanto2019physics | Physics without Determinism | Del Santo, Gisin | arXiv API 1909.03697v2 | PASS |
| gisin2020indeterminism | Indeterminism & Intuitionistic Math | Gisin | arXiv API 2011.02348v1 | PASS |
| delsanto2022openpast | The open past | Del Santo, Gisin | arXiv API 2205.11547v2 | PASS |
| delsanto2023potentiality | Potentiality realism | Del Santo, Gisin | arXiv API 2305.02429v2 | PASS |
| delsanto2024which | Which features are not quantum | Del Santo, Gisin | arXiv API 2409.10601v3 | PASS |
| pusey2012reality | On the reality of the quantum state | Pusey, Barrett, Rudolph | arXiv API 1111.3328v3 (Nat. Phys. 8:475) | PASS |
| hardy2001quantum | Five Reasonable Axioms | Hardy | arXiv API quant-ph/0101012v4 | PASS |
| aaronson2004quantum | Island in Theoryspace | Aaronson | arXiv API quant-ph/0401062v2 | PASS |
| marletto2017evolution | Evolution w/o evolution, no ambiguities | Marletto, Vedral | arXiv API 1610.04773v2 + Crossref 10.1103/physrevd.95.043510 (PRD 95, 043510, 2017) | PASS |
| vedral2022classical | Classical Evolution Without Evolution | Vedral | arXiv API 2203.03065v1 | PASS |
| knee2016towards | Optimal BCLM tests | Knee | arXiv API 1609.01558v2 | PASS |
| srikanth2017quantum | QBC and reality of the state | Srikanth | arXiv API 1708.04964v3 | PASS |
| cabbolet2018comment | Comment to PBR | Cabbolet | arXiv API 1812.03035v2 | PASS |
| page1983evolution | Evolution without evolution | Page, Wootters | Crossref 10.1103/physrevd.27.2885 (PRD 27, 2885–2892, 1983) | PASS |
| rammal1986ultrametricity | Ultrametricity for physicists | Rammal, Toulouse, Virasoro | Crossref 10.1103/revmodphys.58.765 (RMP 58, 765–788, 1986) | PASS |
| luce1956semiorders | Semiorders & Utility Discrimination | Luce | Crossref 10.2307/1905751 (Econometrica 24, 178–191, 1956) | PASS |
| qunigudzinas2026scalar | Self-Referential Scalar Family (RES.020) | Quni-Gudzinas, Rowan Brad | Zenodo API 22035210 (concept 22031551) | PASS |
| qunigudzinas2026adelic | Adelic Shannon Theory (ADL.001) | Quni-Gudzinas + legacy collective | Zenodo API 22024240 | PASS* |
| qnfo2026clocks | PW-clocks ultrametricity | QNFO Research + Quni-Gudzinas | Zenodo API 21120286 | PASS* |
| qunigudzinas2026finite | Gisin–Del Santo × OC convergence | Quni-Gudzinas, Rowan Brad | Zenodo API 21647362 | PASS |
| qnfo2026continuum | Continuum Trilogy I–III | QNFO Research Collective + Quni-Gudzinas | Zenodo API 21672990 | PASS* |
| qunigudzinas2025entropic | Entropic-Operational Paradigm | Quni-Gudzinas, Rowan Brad | Zenodo API 17687207 | PASS |
| qnfo2026radix | Radix→…→Bruhat-Tits synthesis | QNFO Research + Quni-Gudzinas | Zenodo API 21102764 (concept 21102436) | PASS* |
| qunigudzinas2026monna | Non-Archimedean Projective Perspective (UMP.010) | Quni-Gudzinas, Rowan Brad | Zenodo API 21979032 | PASS |
| qunigudzinas2026relaxation | Measurement-Triggered Relaxation (RES.018) | Quni-Gudzinas, Rowan Brad | Zenodo API 22026562 | PASS |
| qunigudzinas2026locale | Locale Framework (UMP.011) | Quni-Gudzinas, Rowan Brad | Zenodo API 21983659 | PASS |
| qunigudzinas2026valuation | Valuation Without R | Quni-Gudzinas, Rowan Brad | Zenodo API 21803677 | PASS |

\* PASS with ADR-014 note: the RECORD carries a legacy collective creator
("QNFO Research" / "QNFO Research Collective") alongside the sole human author. These
are pre-existing Zenodo records, NOT new content; ADR-014 applies to NEW content.
Remediation (newversion creator correction) is queued in the naming-mandate wave
(NAMING-MANDATE-1 registry, requires user approval for Zenodo newversions).

## Audit verdict

- **28/28 entries PASS author verification** (14 arXiv via arXiv API, 4 Crossref DOIs,
  11 Zenodo records; Marletto–Vedral counted once with dual verification).
- **0 fabricated authors, 0 wrong attributions, 0 version mismatches.**
- Cross-checks against evidence file §4–5: all 28 entries appear in the Phase 1
  evidence ledger with live-verification rows; the 12 primary imports are enumerated
  in PROJECT-PLAN §9 (red-team S-3 remediation).
- 4 Crossref DOIs that the red-team reviewers could not verify with read-only tools
  (physrevd.27.2885, revmodphys.58.765, 10.2307/1905751, physrevd.95.043510) are now
  verified with full author lists (above).

## Data-quality flags (non-blocking)

1. **D1 `entropic-operational-paradigm` row has `doi:null`** while the canonical record
   is 10.5281/zenodo.17687207 — D1 backfill executed this cycle (S-9).
2. **Legacy collective creators on 4 corpus records** (22024240, 21120286, 21672990,
   21102764) — queued for the naming-mandate remediation wave (user approval needed).
3. **`time-from-a-timeless-universe` has no DOI** in D1 (data-quality, S-10 partial);
   not cited in the bib because the DOI is missing — cited in the outline via
   Vectorize id only; add DOI at P4 if the record is confirmed.
