# Publish State — QNFO.RES.019 (2026-08-20)

## Status: STAGED — publish blocked on the Zenodo file-commit 500 window

Deposit: **22031556** (fresh record), reserved DOI **10.5281/zenodo.22031556**.
Frontmatter + repo: commit `e1bbb9f` (corrected DOI; the earlier 22031417 write was a
guessed-ID error caught by readback — EXEC-PHANTOM-DOUBLE-EDGED-1).

## What is complete on the deposit

- Metadata PUT (deposit API): 200 — version 1.0, publication_date 2026-08-20, creators,
  license cc-by-nc-sa-4.0, keywords, GitHub isSupplementTo related_identifier.
- 7 flat files in the bucket (201): md/html/pdf, references.bib, citation-audit.md,
  PROJECT-PLAN.md, README.md.
- 7 subdir entries init'd + content uploaded via records-API (docs/deep-research.md,
  artifacts/universal-ignorance-audit.md, artifacts/external-search/corpus-sweep-2026-08-20.md,
  artifacts/verification/verify-claims.{py,log,json}, figures/fig1-two-layer-structure.svg).
- 4 commits landed (html, references.bib, PROJECT-PLAN, README); the rest are in the
  Zenodo file-commit **500 window** (error_id-prefixed server errors; same state as the
  RES.015 saga 2026-08-19 — transient, passes in minutes-to-hours).

## Retry recipe (exact)

1. Probe: commit one pending entry (e.g. `figures/fig1-two-layer-structure.svg` via
   `POST /api/records/22031556/draft/files/<key>/commit`). When it returns non-500:
2. Re-run the commit-retry pass over all pending entries (20s gaps, 6 attempts each).
3. `POST /api/deposit/depositions/22031556/actions/publish` → expect 202.
4. Verify: record state done, doi.org HEAD 200, DataCite findable, no `<RESERVED>` in the
   deposited .md, frontmatter DOI == record DOI.
5. Then: R2 mirror (qnfo-releases/2026/08/visual-graphs-vs-matrices-epistemic-design/,
   wrangler --remote), D1 INSERT papers row, KG node, registry P6, tag
   v1.0-published-res019 at the corrected commit.

Do NOT discard 22031556 — metadata + bucket files are complete and survive retries.

## Root-cause note

Same backend failure mode as RES.015 (ZENODO-FILE-SERVICE-FLAKE-1 class): the records-API
commit endpoint 500s in windows under load; bucket PUTs and content PUTs succeed. The
window clears with time; retries after the window land (4 commits landed this cycle before
the window opened).
