# P6 Zenodo Remediation — RESOLVED ✅

**Record v2:** 10.5281/zenodo.21964824 (published 2026-08-16, status=published, files=15) · Concept: 10.5281/zenodo.21964565
**Branch:** res/paper/research-purpose-utility @ ae1039f

## Status
**RESOLVED 2026-08-16.** Newversion published with ALL 15 source files (citation-audit.md added), every file checksum-verified (ALL VERIFIED: True), DataCite FINDABLE, R2 mirror updated. The v1 record (10.5281/zenodo.21964566) remains as the historical 14/15 version; the concept DOI resolves to the latest (v2).

## Original finding (2026-08-16)

## Remediation procedure (next CMD CONTINUE / next session)

1. `POST https://zenodo.org/api/deposit/depositions/21964566/actions/newversion` (deposit API, Bearer ZENODO_TOKEN from C:\Users\LENOVO\keys.json, browser-like UA) → new draft id, carried-over files.
2. Reserve the NEW version DOI: `POST /api/deposit/depositions/{newid}/actions/pids/doi` (or prereserve_doi on deposit creation) → new DOI.
3. **NEWVERSION-FRONTMATTER-CARRYOVER-1:** patch `research-purpose-utility.md` frontmatter `doi:` → NEW version DOI (keep status: published); rebuild `research-purpose-utility.html` + `.pdf` (pandoc → citeproc → MathJax inline → render-pdf.cjs CDP).
4. **ZENODO-DEPOSIT-DELETE-500-1:** replace carried-over files in the draft — `GET /api/deposit/depositions/{newid}/files` → `DELETE {file.links.self}` (per-file UUID URL, NOT `/files/{FILENAME}` which 500s; bucket PUT 404) → re-POST multipart with the patched `.md/.html/.pdf`.
5. Add `citation-audit.md`: declare → PUT content → **WAIT ≥30s** → commit (the InvenioRDM commit endpoint 500s if called immediately after content PUT — the proven pattern: batch declare `[{"key": name}]`, PUT `links.content`, sleep 30, POST `/draft/files/{name}/commit`, retry ×6 with 15s backoff).
6. `POST /api/deposit/depositions/{newid}/actions/publish` → verify state=done.
7. Verify: DataCite new DOI findable + doi.org 200 + concept DOI chain resolves to latest.
8. Update `references/README.md` + PROJECT-PLAN P6 status; commit/push; close.

## Root cause (for kaizen)
InvenioRDM `POST /draft/files` with a LIST of keys **replaces/initializes the file set** — a batch declare containing only some keys drops the others (observed: p6i batch [.md,.html] dropped README/PROJECT-PLAN; final set lost citation-audit.md). Rule: after ANY batch declare, re-verify the full expected file set before publish; prefer declare-in-one-batch-ALL-files or verify-after-every-declare (ZENODO-FILE-SET-REPLACE-1 candidate).
