# Audit of the two research repositories, 2026-10-26

Scope: `QNFO/qnfo-research` and `QNFO/qnfo-ensemble-research` (now folded into the first), their writers in
`QNFO/qnfo-workers` (`qnfo-research-exec`), and the Cloudflare records that describe the same papers (D1 `qnfo-audit`,
`living-paper`). Every number below was measured on that date; the command or query is given so it can be repeated.

## 1. Why were there two research repositories?

They were created for different jobs, a month apart, and never designed to reference each other.

| | `qnfo-research` | `qnfo-ensemble-research` |
|---|---|---|
| Created | 2026-08-04 (consolidation of eight project repos by `git subtree`) | 2026-09-08 (ensemble pilot, "user directive 2026-09-08") |
| Holds | the **published** papers (`papers/<slug>/paper.md`+`README.md`), program directories, project files | the **process** artifacts of each run: grounding, independent drafts, review, verification script and report |
| Written by | hand, the member repos, and `publishV2` (`depositToGithub`, "auto-deposit") | `pushArtifactsToGitHub`, one `cycle-N/<slug>/` per run |
| Link between them | none in the data; only an equal slug, when the paper was deposited at all | none |

The pilot's own README said what it was: a protocol for writing several independent papers on one theme and keeping
"all artifacts, collateral files, and interim/intermediate drafts". The pipeline then adopted its directory layout as the
deposit target for **every** run (396 cycles), while `qnfo-research` stayed the home of the finished paper. The result was
two repositories that together hold the answer to "how was this paper made?" with no key between them.

## 2. Are all research artifacts preserved for provenance and reproducibility?

**No. What is there is intact; what is missing is recorded below, and none of it was on a ledger before today.**

Intact: all **2,338** files that a manifest lists and that exist hash to the value frozen in their manifest, and every
`reproduced` verdict below was obtained by re-executing the deposited scripts. Nothing present has been altered since
collection. (`python3 tools/provenance.py verify`)

Missing or weak:

| Finding | Count | Evidence and cause |
|---|---|---|
| Files a `MANIFEST.json` lists that the repository lacks | **154 files in 47 run directories** (43 cycles) | `grounding.md` 36, `writer-b-draft.md` 31, `writer-a-draft.md` 28, `review-report.md` 24, `verification.py` 15, `verification.md` 14, `writer-c-draft.md` 6 |
| Run directories with no `MANIFEST.json` at all | **48** (in 38 cycles; 8 cycles have none) | the manifest is the *last* file pushed, so a run that stopped part-way has none |
| Deposit events that hit HTTP 409 but were logged `ok` | **97 of 400** (`cloud_ops_events`, job `qnfo-research-exec`, kind `github`, 2026-10-10..26) | one contents-API `PUT` per file on the same branch, parallel slots racing, per-file status ignored: `return { ok: true, cycle, results }` |
| Pipeline papers whose final text is not in git | **201 of 292** slugs that have a run | the active publish path (`publishStageV2`) deposits to the ensemble repo only; `papers/<slug>/` was written only by the legacy `publishV2` |
| Published slugs with no run in git at all | about **29** (321 distinct `paper_slug` in `research_queue` with `status='published'` vs 292 slugs with a run) | pre-dates the deposit, or never landed |
| The reconciled paper of a run | **absent from every run after cycle 1** | `collectArtifacts` never reads `reconciled.md` |
| Review reports | only the last of `review-report-0/1` is kept; `fixes.json` is not deposited | `collectArtifacts` |
| Which model wrote which draft, prompts, timestamps, interpreter | **not recorded** in any manifest | v1 manifest has only `pipeline` and per-file hashes |
| Deposit ledger | `publication_artifacts`: **0** rows for any GitHub deposit (4 unrelated `poster` rows) | unquoted SQL (`datetime(now)`) in an empty `catch`, plus `publication_id INTEGER` receiving a slug |
| `bytes` in v1 manifests | wrong for **1,843 of 2,338** files | JS `String.length` (UTF-16 units), not bytes. Hashes are unaffected |
| License statements | 102 papers say *QNFO-ULA v2.0*, 38 say *CC BY 4.0*; the repository LICENSE is *ULA v2.1* | recorded per paper in `provenance.json`; not rewritten |
| DOIs | 12 papers declare more than one distinct DOI (README vs header); all are from the earlier external deposits | recorded as declared in `provenance.json`; nothing relies on them |
| Third-party archive | Software Heritage holds `qnfo-research` (full visits 2026-08-17 and 2026-10-21) and has **never seen** `qnfo-ensemble-research` (404) | the 396 cycles of process artifacts had no copy outside GitHub and Cloudflare; the next visit after the history is linked into `main` captures them |
| Verification scripts whose record cannot be reproduced | **2** of 388 | cycle-217 prints different output on every run (it orders objects by identity); cycle-26's recorded output ends in `Network connection lost.` |

Reproducibility of the verification step, re-executed exactly as the pipeline runs it (`python -I -c <script>`, empty directory,
`PYTHONHASHSEED=0`; `python3 tools/provenance.py reproduce --all`). The reference interpreter is **CPython 3.12**: it reproduces the
recorded outputs byte for byte (3.13 reproduces 324 exactly and 49 more with the same stdout and exit code but different error wording or
traceback layout; on 3.11 two scripts do not parse, they use 3.12 f-string syntax).

| Verdict (CPython 3.12) | Runs |
|---|---|
| reproduced, exact (stdout, stderr and exit code identical) | 373 |
| not reproduced | 2 (above) |
| no recorded output to compare | 13 |
| run has no verification script | 53 (the pilot, and runs whose files never landed) |

That is **373 of 375** scripts with a record (99.5%). All 388 scripts import only the standard library. Re-running them
the way the pipeline did also explained nine "failures": the pipeline executes scripts as strings, where `__file__` does
not exist, and nine records are that `NameError`, which a file-based re-run hides.

## 3. Can they be consolidated into one?

**Yes, and it is done in this change.** `qnfo-research` is the home because it already receives the published papers,
is listed in the portfolio as the research artifact repository, and is the target of the pipeline's second writer.
`qnfo-ensemble-research` is imported with `git subtree add` (no squash) under `runs/`:

* all **2,837** source commits are reachable from the pull request branch (the merge's second parent is the ensemble head `5e41f98`;
  3,324 commits in total). The repository merges squash-only, which would drop them from `main`, so `ensemble-catchup.yml` links them to `main`
  afterwards with a content-neutral merge (rehearsed on temporary clones: 3,325 commits reachable, empty diff) and imports newer cycles;
* paths under `runs/` are the old paths, so no historical hash or manifest changes;
* `LICENSE` was byte-identical and is not duplicated; the ensemble `README`, `PROVENANCE.md` and
  `RESEARCH-PROCEDURE.md` moved to `docs/` with `git mv`;
* the live pipeline writes to one repository from `qnfo-research-exec` 0.35.0; the old repository receives a notice and
  is archived once the catch-up (`provenance/IMPORT.json`) shows nothing newer.

Considered and rejected: keeping two repositories and adding a link table (it preserves exactly the split that lost the
link); a flat `papers/<slug>/runs/` layout (it rewrites every path in 392 manifests and breaks hash continuity for no
gain the `provenance.json` join does not already give).

## 4. How do the directories relate to the published papers?

By slug, and only when the paper was deposited. Measured: 292 distinct run slugs in `runs/` across 440 run directories
(86 slugs appear in more than one cycle, because a revision goes back through the pipeline; the cycle-1 pilot is counted
separately). 79 have an exact `papers/<slug>/`, 9 an exact program-directory copy, 3 link to 2 papers through the
collision suffix (the pipeline replaces the tail of two colliding 80-character slugs with `-` + 8 hex characters of the
`research_queue` id), and **201 have no deposited paper**. 51 of the 140 papers in the repository have no run
(hand-written or pre-pipeline: chapters, the eight member repositories' papers).
The published page is `papers.qnfo.org/papers/<slug>`; its text lives in living-paper D1 (`papers.body_md`), which is
also where the 201 missing texts come from.

After this change the relation is explicit in three places that agree: `papers/<slug>/provenance.json` (paper to runs),
each run's `ro-crate-metadata.json` (run to paper URL and to its sources), and D1 `research_run_ledger` (run id, slug,
version, hashes, commit).

## 5. Are code and other non-text artifacts stored?

* **Code:** yes for what the pipeline produces: 388 `verification.py` scripts, kept beside the report that records their
  output, plus the helper scripts at the root of this repository. The pipeline's own code is `qnfo-workers/qnfo-research-exec`;
  the manifest now names the worker version that produced a run.
* **Non-text artifacts:** only in the merged project repositories and `releases/` (41 PDF, 15 Lean, 13 HTML, 10 TeX, 5 zip,
  1 PNG, a `.cls` and a `.bst`). **None for the 292 pipeline papers**: no rendered PDF/HTML, no figures, no data files;
  their only outputs are Markdown, Python and JSON. Rendered forms are derived from `paper.md` and live on
  papers.qnfo.org and in R2.
* **Large files:** the Cloudflare Artifacts mirror refuses a blob over 32 MB (the fleet already holds one 76 MB blob that
  it cannot mirror). The standard sets a 25 MB limit and a pointer-file convention (`*.pointer.json`: sha256, bytes, R2
  key); `verify` enforces both. The largest tracked file today is 5.2 MB.
* **Secrets:** none found in either repository (key, token and private-key patterns).

## 6. What was done about it

Repository (this pull request): import with history; `docs/PROVENANCE-STANDARD.md`; `tools/provenance.py` (28 tests,
two mutation-checked); 441 run crates; 140 paper records; the 298-row ratchet ledger; schemas; `.gitattributes`;
`CITATION.cff`; the CI workflow.

Pipeline (`qnfo-workers`, `qnfo-research-exec` 0.35.0, separate pull request): the atomic single-commit deposit with
retry and read-back, the v2 manifest and crate, the paper in the same commit, the D1 ledger and its failure-mode
detector, restoration of the missing run files from R2 (accepted only if the hash equals the manifest's) and of the
missing paper texts from living-paper, and the repaired SQL.

Fleet follow-ups (no session action; each has a doer and a closing probe): the worker's sync tick dispatches the history link and, once it
holds, files the archive request for the legacy repository (`PORTFOLIO-ARCHIVE-1`, reversible). Software Heritage needs no request: it visits
`qnfo-research` on its own. One decision stays with the owner because it is a legal act in the owner's name: the license line of the 38 papers
whose README still says CC BY 4.0 (a card with its default in effect: they keep the line they declare, recorded in `provenance.json`).

## Reproducing this audit

```
python3 tools/provenance.py verify
python3 tools/provenance.py reproduce --all
python3 tools/provenance.py index | head
python3 -m unittest discover -s tools -p 'test_*.py'
git log --oneline | wc -l                     # 3324 (486 own + 2837 imported + the merge)
git cat-file -t 5e41f98532428c2c19d6bbedb1315742e85021c4     # commit: the ensemble head is in this history
```

D1 numbers (read-only, `qnfo-audit`): `SELECT count(*), sum(text LIKE '%"status":409%') FROM cloud_ops_events WHERE
job='qnfo-research-exec' AND kind='github'` (400, 97); `SELECT count(*) FROM publication_artifacts WHERE artifact_type
<> 'poster'` (0); `SELECT count(DISTINCT paper_slug) FROM research_queue WHERE status='published'` (321).
