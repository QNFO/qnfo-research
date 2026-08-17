# Publish Readiness — QNFO.INM.001 v0.3 (2026-08-17)

**WBS:** QNFO.INM.001 — Signal-Worker Boundary Confinement
**Status:** READY FOR CMD PUBLISH — all gates green, verified live this session.

---

## 1. Readiness Verification (all read-only, live-checked 2026-08-17)

| Check | Result | Evidence |
|:------|:-------|:---------|
| Concept chain | concept `10.5281/zenodo.21931224` → latest record `21969297` (v0.2), 9 files | Zenodo records API GET /records/21931224 |
| Stale-draft check | **None** — the only deposition matching the title is the published record (state: `done`); no draft blocks newversion creation | deposit API `?q=title:...&status=draft` |
| Deposit-vs-branch integrity (v0.2) | **3/3 sha256 MATCH** at publish-era commit `9d846ea`: md `9cfea7692b7e…`, references.bib `47505ddd489b…`, citation-audit.md `f6710c0e5c20…` | Zenodo file links.self bytes vs GitHub raw at 9d846ea |
| Branch artifacts (v0.3) | md v0.3/draft (frontmatter + header consistent, 2026-08-17); html 2,312,941 B 0 mojibake; pdf 276,645 B 0 U+FFFD (single U+FFFF = documented TrueType cmap endCode sentinel in FontFile stream, deterministic — NOT text mojibake) | build + byte scans this session |
| Citations | 19/19 in-text; 19 numbered refs; bib 19 entries, no dup keys; refs 18/19 Crossref-verified | verify suite + Crossref |
| Audit closure | 5-adversary: 4 HARD + 3 SOFT **all closed** (commits 66764cd, b329bfe, d6b919c) | git log |
| Cross-store state | Registry QNFO.INM.001 active/v0.2; D1 papers row v0.2 published, Vectorize indexed (31 chunks v0.2 body); KG node distributed; R2 mirror 9 objects; papers.qnfo.org 200 | live queries 2026-08-17 |

## 2. Publish Sequence for CMD PUBLISH (v0.3 newversion)

1. **Create newversion** of 21969297 (`POST /api/deposit/depositions/21969297/actions/newversion`; if 400 `files.enabled` → stale draft exists, use `links.latest_draft`). Reserve new DOI: `POST /api/deposit/depositions/{draft}/actions/prereserve` (records API: `POST .../draft/pids/doi`).
2. **Patch md frontmatter** (NEWVERSION-FRONTMATTER-CARRYOVER-1): `doi: <reserved v0.3 DOI>`, `status: published`, `date: 2026-08-17` — then rebuild html/pdf via CDP pipeline (body changed? yes — frontmatter/status; rebuild to keep artifacts consistent).
3. **ZENODO-PLACEHOLDER-DOI-1**: after upload, FETCH THE UPLOADED FILE back and assert no `<RESERVED>` string remains before publish (never trust `prereserved_doi` API response alone).
4. **Replace carried-over files** (ZENODO-DEPOSIT-DELETE-500-1): `GET /files` → `DELETE {file.links.self}` (per-file UUID URL, 204) → re-POST multipart. Do NOT use filename DELETE (500) or bucket PUT (404).
5. **Metadata PUT = FULL REPLACEMENT**: preserve `title/creators/license (CC-BY-4.0)/resource_type (publication-preprint)/publisher (Zenodo)/keywords/related_identifiers` (isSupplementTo → GitHub branch URL); set `version: "v0.3"` explicitly (LEGACY-PUT-VERSION-OMISSION-1 — records-API newversion does NOT inherit version label).
6. **Publish** → expect 202/200 with `state: done`.
7. **3-layer verify**: doi.org HEAD 200 → new record; DataCite findable (`api.datacite.org/dois/{new-doi}`); records API state=done + 9 files + `metadata.version = v0.3`.
8. **D1**: update `papers` row (doi → new record DOI, version v0.3, body_md → v0.3 text, zenodo_doi/zenodo_url, status published) → SELECT verify → **Vectorize re-index** via qnfo-paper-indexer `/webhook?slug=signal-worker-boundary-confinement` (X-Index-Token `chnx-idx-v1-k9m2n4p7r5t8` + browser UA per VECTORIZE-403-MISDIAGNOSIS; closes D-1) → verify `indexed:true` + `resolve_paper_id` returns v0.3 DOI.
9. **R2 mirror** (R2-MIRROR-AFTER-PUBLISH-1): bucket **`qnfo-releases`** (NOT `releases` — WRONG-BUCKET-SELECTION-1; verify against sibling object first) at `2026/08/signal-worker-boundary-confinement/` — replace md/html/pdf/bib/audit with v0.3 versions + README/PROJECT-PLAN/artifacts; verify via bucket listing (expect 9+ objects).
10. **KG**: update `paper:signal-worker-boundary-confinement` — `doi` → new record DOI, `zenodo_url`, `version: v0.3`, `distribution_status: distributed`, `r2_path`/`r2_readme` (graph-api /sync; readback via /query).
11. **Registry**: `program_registry.current_version` → `v0.3` (portfolio-state D1; readback SELECT).
12. **Closeout**: memory log (task_outcome, new DOI + concept), verify recall.

## 3. Anti-pattern checklist (mandatory at publish)

- [ ] NEWVERSION-FRONTMATTER-CARRYOVER-1 — patched frontmatter BEFORE upload; verify deposited .md contains the NEW DOI
- [ ] ZENODO-PLACEHOLDER-DOI-1 — fetched uploaded file back, no `<RESERVED>`
- [ ] ZENODO-DEPOSIT-DELETE-500-1 — per-file links.self DELETE (204), never filename DELETE
- [ ] LEGACY-PUT-VERSION-OMISSION-1 — `version: v0.3` set explicitly in metadata
- [ ] ZENODO-CONCEPT-DOI-CITE-1 — How-to-Cite/concept DOI `10.5281/zenodo.21931224` unchanged (version-agnostic)
- [ ] R2-MIRROR-AFTER-PUBLISH-1 + WRONG-BUCKET-SELECTION-1 — mirror to `qnfo-releases`, verify sibling first
- [ ] VECTORIZE-403-MISDIAGNOSIS — browser UA on ALL worker calls; token `chnx-idx-v1-k9m2n4p7r5t8`
- [ ] Tool-Call Execution Mandate — every publish claim re-queried live same-turn (doi.org, DataCite, records API, D1 SELECT, bucket listing, git ls-remote)
