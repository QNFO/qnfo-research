# R2 Mirror & Registry Remediation — 2026-08-16 (G1/G2/G3 + H-1/H-2)

**Session:** pVxPB_ViPCLUkdaDtykwu (CMD RESEARCH continuation, same cycle as the Phase-1R evidence commit 48c42dd)
**Scope:** remediation of the HARD/registry findings from `majorana-lof-due-diligence-2026-08-16.md` + the red-team reviewer's 2 additional HARD findings.
**Red-team verdict on the Phase-1R record (reviewer `NXPYBq_830Lvo8AknMKYu`, completed ~11 min):** ACCEPT — 7/7 claims PASS, independently re-verified live (Crossref ×7, arXiv ×1, KG SQL ×5, resolve_paper_id ×4, git ×3). Zero fabricated citations/DOIs/venues. Review found 2 missed HARD findings (H-1, H-2 below) — folded in here.

## Verified pre-remediation reality (live API evidence)
- Full R2 fleet enumerated (14 buckets: d-drive, deepchat, git-repos, ipatent, palimpsest-research, play-the-ball, qnfo, qnfo-assets, qnfo-audit, qnfo-backups, qnfo-projects, qnfo-releases, qnfo-skills, releases).
- `exchange-phase-logical-scalar` + `from-distinction-to-dissipation`: **ZERO objects** in any bucket at any path (canonical `qnfo-releases/2026/08/<slug>/` AND legacy `releases/...` AND bare-slug probes) — G1 was a full missing-mirror (R2-MIRROR-AFTER-PUBLISH-1), not just a path typo. D1/KG r2 values were phantom paths.
- `consilient-synthesis-v2` (2026/07), `boundary-ultrametricity` (2026/07), `acrp06-vpmax-extension` (2026/08): **ZERO objects** in any bucket (H-1).
- `configuration-space-topology` (RES.011): canonical mirror EXISTS (15 objects at `qnfo-releases/2026/08/configuration-space-topology/`), but KG pointed at bare `releases/...` and D1 `r2_key` was null (H-2).
- `spin-statistics-distinction`: canonical mirror exists (20 objects); D1 `r2_key` was legacy bare-bucket path.

## Remediation executed (all writes tool-verified + read-back verified)
1. **Mirror created** — 40 objects uploaded to `qnfo-releases` (HTTP 200 each):
   - `2026/08/exchange-phase-logical-scalar/` (20 objects: PROJECT-PLAN.md, README.md, md/html/pdf, references.bib, artifacts/×10, docs/, notebooks/p4-half-turn-monodromy.md, releases/) — source: `res/paper/exchange-phase-logical-scalar` @ f69822b.
   - `2026/08/from-distinction-to-dissipation/` (19 objects: full suite incl. notebooks t1/t4/t5/t6/t7 md+py, docs/×2, RESEARCH-CONTINUITY-REGISTRY.md) — source: `res/paper/spin-statistics-distinction` @ b9563b4 `releases/2026/08/from-distinction-to-dissipation/`.
   - Verified via bucket listing (20 + 19 objects, sizes match).
2. **KG node upserts** (graph-api /sync, full-replace properties, read-back verified):
   - `paper:exchange-phase-logical-scalar`: r2_path → `qnfo-releases/2026/08/exchange-phase-logical-scalar/exchange-phase-logical-scalar.md`, r2_readme canonical, `r2_mirror_verified: 2026-08-16` (all other props preserved).
   - `paper:from-distinction-to-dissipation`: DOI chain corrected to live truth (doi=21940822 v1.0, zenodo_doi=21943007 v1.4, versions field, concept 21940821 — live-verified via zenodo.org/api/records), r2_path/r2_readme canonical, distribution_status distributed (was stale v1.3 + "complete").
   - `paper:configuration-space-topology` (H-2): r2_path/r2_readme → canonical `qnfo-releases/2026/08/...`, distribution_status → distributed (was "complete" + wrong-bucket path).
   - `paper:consilient-synthesis-v2`, `paper:boundary-ultrametricity`, `paper:acrp06-vpmax-extension` (H-1): phantom r2_path REMOVED, distribution_status → published (truthful: no mirror), `r2_mirror_gap: true` + note. Pre-mandate records (2026-07-31/08-01); mirroring left as ACRP-owner backlog — never claim distributed for objects that do not exist.
   - `project:configuration-space-topology` (G3): phase P0 → P8, status complete, published_doi added.
3. **D1 living-paper** (UPDATE + read-back verified): r2_key canonicalized for `exchange-phase-logical-scalar`, `from-distinction-to-dissipation`, `spin-statistics-distinction`, `configuration-space-topology` (was null).

## G2 final disposition (live Zenodo verification, no writes needed)
- `quantum-laws-of-form`: doi=21206074 (v2.0.0) / zenodo_doi=21206166 (v2.1.0) — CORRECT record/current-version convention; no change.
- `from-distinction-to-dissipation`: D1 was correct (v1.0/v1.4); KG was stale at v1.3 — fixed in KG above.

## Residual backlog (documented, no action this cycle)
- ACRP-01/02/06 R2 mirroring (pre-mandate; owner: ACRP program) — gap flagged on KG nodes.
- Legacy D1 `r2_key` values elsewhere (e.g., older papers with `papers/...` paths) — not part of this finding set.
- Semantic Scholar / OpenAlex citation tracking for Kauffman's review (L1) — RES.010 P3 item.

## Anti-pattern guardrails honored
- GIT-OWNERSHIP-1: only this file + prior evidence committed; no foreign dirt touched.
- WRONG-BUCKET-SELECTION-1: canonical bucket verified against sibling object listing before uploads.
- ZENODO-KG-OWNERSHIP-1: no DOI written without live zenodo.org/api/records verification this cycle.
- Tool-Call Execution Mandate: every write followed by same-turn read-back (KG SQL + D1 SELECT shown above).

---

## ⚠️ CORRECTION — appended 2026-08-16 (same session, post-hoc full enumeration)

**The H-1 verdict above is RETRACTED. It was based on an incomplete probe.**

### What the full enumeration revealed
A paginated, cursor-complete enumeration of both paper buckets (R2 objects API, `result_info.is_truncated` pagination) showed the `qnfo-releases` bucket uses **TWO layouts**:
- **Flat (current canonical, knowledge v2.12):** `2026/MM/<slug>/…` — used for configuration-space-topology, spin-statistics-distinction (flat copy), exchange-phase (flat copy), from-distinction (flat copy), tyranny-of-the-plus-minus-one.
- **Legacy nested:** `releases/2026/MM/<slug>/…` (a `releases/` key prefix INSIDE `qnfo-releases`) — used for the large July/August publication fleet (70+ record folders).

All three "H-1" records **DO have real mirrors** under the nested layout:
- `qnfo-releases/releases/2026/07/consilient-synthesis-v2/` — 3 objects (PROVENANCE-BUNDLE.zip, .md, .pdf) ✓
- `qnfo-releases/releases/2026/07/boundary-ultrametricity/` — 3 objects ✓
- `qnfo-releases/releases/2026/08/acrp06-vpmax-extension/` — 6 objects (incl. ERRATA-v1.1.md, v1.1 md/pdf, PROVENANCE-BUNDLE) ✓

And the G1 pair ALSO had nested mirrors before this cycle's flat copies were created:
- `qnfo-releases/releases/2026/08/exchange-phase-logical-scalar/` — 15 objects ✓ (pre-existing)
- `qnfo-releases/releases/2026/08/from-distinction-to-dissipation/` — 19 objects ✓ (pre-existing)

**Root cause of the false negative:** the first-pass probes (r2check/r2sweep/r2h1sweep) queried prefixes `2026/MM/<slug>`, bare `<slug>`, and `papers/<slug>` — none of which match keys that START with `releases/2026/MM/<slug>`. The API result shape (bare array + `result_info`) also masked pagination, capping listings at 20 objects and hiding the nested fleet. **The mirrors existed all along; the registry paths were truthful.**

### Correction executed (read-back verified)
1. `paper:consilient-synthesis-v2` → `distribution_status: distributed`, `r2_path: qnfo-releases/releases/2026/07/consilient-synthesis-v2/consilient-synthesis-v2.md`, `r2_readme: …/PROVENANCE-BUNDLE.zip`, `r2_mirror_verified: 2026-08-16`.
2. `paper:boundary-ultrametricity` → `distribution_status: distributed`, r2_path/r2_readme nested (3 objects verified).
3. `paper:acrp06-vpmax-extension` → `distribution_status: distributed`, r2_path → v1.1 md at nested key, r2_readme → PROVENANCE-BUNDLE (6 objects verified).
4. D1 `papers.r2_key` for the 3 slugs → nested keys (read-back SELECT shown).
5. All `r2_mirror_gap` flags REMOVED.

### Net state after correction (dual copies, no data loss)
- exchange-phase + from-distinction now exist in BOTH layouts: legacy nested (pre-existing) + flat canonical (this cycle). KG/D1 point at the flat canonical paths (verified objects at both). No deletion performed anywhere (R6: DELETEs irreversible).
- ACRP-01/02/06: restored to their original truthful distributed state; their legacy nested mirrors are the canonical artifacts (July convention).

### Lesson (kaizen candidate — R2-PREFIX-PROBE-SCOPE-1)
When verifying R2 mirror existence, probe ALL known key-layout prefixes per bucket: `YYYY/MM/<slug>`, `releases/YYYY/MM/<slug>`, `papers/<slug>`, AND bare `<slug>`; paginate with `result_info.cursor` until `is_truncated=false`; and verify the API result shape (bare list vs dict) before trusting object counts. A "0 objects" verdict from an under-scoped prefix probe is a probe defect, not a data absence (BLAME-EXTERNAL-1 discipline — the fault was local).
