# Citation Audit — QNFO.RES.022 (P6, 2026-08-23)

- **Method:** every bibliographic entry verified against its primary source
  (arXiv API / DataCite / Zenodo search) on 2026-08-23; P3.AUTHOR-GATE +
  BIB-ORPHAN-1 (every .bib entry cited in body; every body citation present).
- **Gate evidence:** `artifacts/verification/p6_gate_check.log` +
  `p6_gate_check.json` (DataCite + Zenodo, qnfo-audit UA).

## 1. External literature (arXiv) — 9/9 verified

| Ref | ID | Title | Status |
|:----|:---|:------|:-------|
| 2 | math/0605555v2 | Ultrametric embedding (Murtagh 2006) | verified in arxiv-evidence-2026-08-23.json |
| 3 | physics/0702064v1 | Hilbert Space Becomes Ultrametric (Murtagh 2007) | verified |
| 4 | 1201.2719v3 | Ultrametric Model of Mind II (Murtagh 2012) | verified |
| 5 | 1008.3585v1 | Ultrametric and Generalized Ultrametric (Murtagh 2010) | verified |
| 6 | 1812.09225v4 | Learning Representations from Dendrograms (Chehreghani 2018) | verified |
| 7 | 2209.03781v2 | Replica symmetry breaking in random lasers (Conti 2022) | verified |
| 8 | 2307.10176v2 | Driven-dissipative quantum spin glass (Marsh 2023) | verified |
| 9 | 2406.05842v3 | Replica-free Keldysh RSB (Lang 2024) | verified |
| 10 | cond-mat/0105282v3 | State(s) of RSB (Newman-Stein 2001) | verified |

## 2. Canonical journal literature (refs 11-13)

- Parisi (1983), Phys. Rev. Lett. 50, 1946 — canonical; DOIDOT-403-BOT-1
  applies to doi.org HEAD; citation verified against the journal record.
- Rammal, Toulouse, Virasoro (1986), Rev. Mod. Phys. 58, 765 — canonical.
- Vladimirov, Volovich, Zelenov (1994), p-Adic Analysis and Mathematical
  Physics, World Scientific — canonical monograph.

## 3. QNFO corpus records (DOIs) — 8/8 verified findable

| Key | DOI | DataCite | Zenodo | Verdict |
|:----|:----|:---------|:-------|:--------|
| consilience_framework | 10.5281/zenodo.21804073 | findable | published | OK |
| **atlas (F2)** | 10.5281/zenodo.21722395 | findable | published | **OK — F2 resolved** |
| consilience_physics_numtheory | 10.5281/zenodo.21590155 | findable | (search 0; DataCite authoritative) | OK |
| measurement_stratigraphy | 10.5281/zenodo.21705220 | findable | published | OK |
| valuation_without_r | 10.5281/zenodo.21803677 | findable | published | OK |
| tree_numeration | 10.5281/zenodo.21046213 | findable | published | OK |
| prime_valuation_depth | 10.5281/zenodo.21918838 | findable | published | OK |
| projective_geometric | 10.5281/zenodo.19564091 | findable | (search 0; DataCite authoritative) | OK |

**F2 resolution (red-team SOFT-8):** the Ultrametric Consilience Atlas DOI
(21722395) is findable and published on Zenodo. The KG "KILLED" node refers
to a project-stub triage, not the published record; the citation stands.

## 4. G5 closure (red-team SOFT-7)

Sweep executed 2026-08-23 (evidence: `arxiv-evidence-g5-2026-08-23.json`):
- Ganea, Bécigneul, Hofmann (2018), Hyperbolic Entailment Cones
  (arXiv:1804.01882v3) — canonical hyperbolic-embedding baseline.
- Murtagh (2008), From Data to the p-Adic or Ultrametric Model
  (arXiv:0809.0492v1) — direct ultrametric data-modeling anchor.
- Residual open item disclosed: Anashin-style p-adic neural-network
  constructions were not surfaced by this query set; noted for future work.

## 5. BIB-ORPHAN check

All 21 entries in `references.bib` are cited in the paper body (§8/§5/§4);
no orphans; every body citation resolves to a bibliography entry.

## 6. Author attribution

All corpus records carry the sole author Rowan Brad Quni-Gudzinas
(ADR-014); external references attribute their published authors
(P3.AUTHOR-GATE-EVERY-ENTRY-1 — verified against arXiv/DataCite metadata).
