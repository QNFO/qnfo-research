# Publish State — RES.015 v0.4 (2026-08-19)

## Status: READY-TO-PUBLISH, BLOCKED ON ZENODO FILE SERVICE

Draft: **22010380** (fresh; predecessor 22009416 discarded after file-index corruption).
Reserved DOI: **10.5281/zenodo.22010380** (concept DOI 10.5281/zenodo.21991895 unchanged).
Frontmatter + repo: commit `c23eb67` (frontmatter doi -> 22010380; html/pdf verified free of the old DOI).

## What is complete on the draft

- Metadata PUT (deposit API): 200 — version 0.4, publication_date 2026-08-19, creators,
  license cc-by-nc-sa-4.0, keywords, related_identifiers (GitHub isSupplementTo → https://github.com/QNFO/qnfo-research/tree/res/paper/zx-diagram-fault-lines). VALIDATOR-CLEAN
  (the only publish errors were file-transfer, never metadata).
- 7 flat files via bucket PUT (permanent bucket objects): zx-diagram-fault-lines.md/.html/.pdf,
  references.bib, citation-audit.md, PROJECT-PLAN.md, README.md.
- 8 subdir files via records-API: entries init'd + content uploaded (deep-research,
  import-provenance, advancement-map, universal-ignorance-audit, calibration-register,
  corpus-sweep, qpl2026-zx-cluster, falsifiability-sweep). Commits intermittent — see below.

## Diagnostic record (why publish fails)

Publish (deposit-API POST /actions/publish) returns 400: "One or more files have not completed
their transfer." Root cause chain observed across 2026-08-19 (12+ publish attempts, 3 API
surfaces, 2 drafts):

1. Records-API commit endpoint nondeterministic: returns 200 / 404 / 500 / 504. The 404s name
   a DIFFERENT file than the one being committed (off-by-one pattern) — the server-side file
   index lags the uploads. 500s/504s = transient server errors (error_id-prefixed).
2. Evidence the backend is load-sensitive: commits DID succeed earlier the same day
   (v22/v23/v26: 6 distinct 200-OK commits on retries 1-2); the 500 window arrived late in the
   day. A fresh draft (22010380) shows the same behavior — NOT per-draft corruption.
3. Deposit-API view counts only bucket files (7); records-API view shows 13-15 entries. The
   publish validator reads the deposit registry, which sees the uncommitted subdir entries.

## Retry recipe (exact commands)

1. `python zx_zenodo_v31.py a` then `python zx_zenodo_v31.py b` (commit-retry-focused; init only
   when the entry is missing; 25s settle + 3 commit attempts per file).
2. `python zx_zenodo_v32.py` (census + 90s settle + 4 publish attempts).
3. On success: run `zx_zenodo_v15.py` (sha256 parity of deposited .md, doi.org HEAD, DataCite,
   R2 mirror via wrangler) then `zx_zenodo_v18.py` (D1 papers update + KG node DOI -> new record
   DOI; readbacks).
4. Tag `v0.4-published-res015` after verification.

Retry cadence: the 500 window is transient; retry within hours rather than minutes
(ZENODO-STALE-DRAFT-BLOCK-1 class: do not discard 22010380 — its bucket files + metadata are
complete and the commit endpoint only needs to recover).

## Kaizen candidate

ZENODO-FILE-SERVICE-FLAKE-1: records-API file-commit under platform load is nondeterministic
(404 off-by-one index lag + 500/504 windows); deposit view ≠ records view; publish validator
keys on the deposit registry. Mitigation for the pipeline: prefer bucket PUT (flat keys),
isolate subdir commits with long settle + retries, and NEVER hammer (rapid sequential commits
amplify the lag — the day's own data shows success only after idle gaps).
