# QNFO research provenance standard

Version 1.0, 2026-10-26. Applies to this repository (`QNFO/qnfo-research`), which since 2026-10-26 is the single home of
every research artifact: the published papers, the pipeline runs that produced them, and the project repositories merged
earlier. It replaces the two thin standards it inherited (the root `PROVENANCE.md` mapping table and the ensemble
pilot's five-line standard, kept verbatim in [`docs/provenance/`](provenance/)).

The audit that motivated it, with the numbers, is [`REPOSITORY-AUDIT-2026-10-26.md`](REPOSITORY-AUDIT-2026-10-26.md).

## 1. What must be true of every published paper

| Property | Meaning here | How it is enforced |
|---|---|---|
| **Traceable** | From a paper on papers.qnfo.org to the exact run that produced it, and from the run to the sources it was grounded on. | `papers/<slug>/provenance.json` links the paper to its runs; each run's `ro-crate-metadata.json` links to the sources and the paper URL; D1 `research_run_ledger` records the same join with the commit. |
| **Verifiable** | Any artifact can be checked byte-for-byte against a hash written when it was produced. | SHA-256 in `MANIFEST.json` (frozen) and in the crate; `tools/provenance.py verify` in CI. |
| **Reproducible** | Every quantitative claim has a deposited script that can be re-run and compared with the recorded output. | `tools/provenance.py reproduce`; stdlib-only scripts; fixed hash seed; a nondeterministic script counts as a failure. |
| **Complete** | Nothing the pipeline produced is dropped, and anything that was dropped is on a ledger with its cause. | The deposit is one atomic commit; `provenance/known-gaps.json` is a ratchet. |
| **Immutable** | A recorded artifact is never edited; a change is a new version with its own record. | `MANIFEST.json` is frozen at collection; paper hashes are append-only snapshots; no history rewrites. |
| **Citable and archivable** | A stable identifier and a metadata file a citation tool understands. | `CITATION.cff` (repository), the paper URL, SWHID (section 7). |

## 2. Layout

```
runs/cycle-<N>/<slug>/            one pipeline run: grounding, writer drafts, review, verification, [reconciled paper]
    MANIFEST.json                   the pipeline's own record (hash per file). Frozen; never rewritten.
    ro-crate-metadata.json          RO-Crate 1.2, Process Run Crate profile: packaging, fixity, stages, re-execution
runs/cycle-1/                     the 2026-09-08 pilot (three writers, one manifest for the cycle)
papers/<slug>/                    the published paper (paper.md, README.md) + provenance.json
<program>/<slug>/                 the same, for a slug programFor() assigns to a program directory
                                  (silent-radix, adelic-freedom, joules-per-compute-benchmark, ...)
<member-repo>/                    the eight project repositories merged on 2026-08-04 (git subtree), unchanged
provenance/known-gaps.json        every known defect, each with a cause and a recovery path (ratchet)
provenance/IMPORT.json            where runs/ came from and how to catch up
schemas/                          JSON Schemas for provenance.json and known-gaps.json
tools/provenance.py               verify | backfill | reproduce | index  (standard library only)
docs/                             this standard, the audit, the research procedure
```

`runs/` keeps the ensemble repository's own paths (`cycle-N/<slug>/...`), so every hash in every historical manifest still
resolves. The import is a `git subtree add` (no squash) that keeps all 2,837 source commits reachable from the pull request branch.
This repository merges squash-only, which would drop them from `main`; `.github/workflows/ensemble-catchup.yml` therefore records the
source history as a parent of `main` afterwards (`git merge -s ours`: no file changes) and imports whatever the legacy repository gained
since. `provenance/IMPORT.json` names the source head and the commands. `git log` then shows each file's original deposit commit, and
`backfill` reads deposit dates from it; until the link exists a crate keeps the date it already records.

### The join

A paper and its runs share a **slug** (the title cut at 80 characters). Two things can disturb that and both are handled:

* **Re-runs.** A slug can have several runs (revisions go back through the pipeline). `provenance.json` lists all of
  them; the newest is the one that produced the current text.
* **Collisions.** When two cut slugs collide the pipeline replaces the tail with `-` plus the first 8 hex characters of
  the `research_queue` row id. A run and its paper can then carry different tails of the same 71-character head;
  `tools/provenance.py` links them as `match: slug-collision-suffix`.

The durable key is the `research_queue` row id (D1). New deposits write it into the manifest and the ledger
(`research_run_ledger.run_id`), so the join no longer depends on slug text.

## 3. The records

### 3.1 `MANIFEST.json` (the pipeline's record)

* **v1** (`pipeline`, `files{name: {sha256, bytes}}`; the 2026-09-08 pilot has its own shape with `writers{}`): frozen.
  Two known defects, kept as they are because the file is frozen and the hashes are what matters: `bytes` is a JavaScript
  string length (UTF-16 code units), not a byte count, for 1,843 of 2,338 files; and a manifest was written *before* its
  files were pushed, so it can list files that never arrived (section 8).
* **v2** (`schema: "qnfo-run-manifest/2"`, written by qnfo-research-exec from 0.35.0): adds `run` (research_queue id, slug,
  cycle, worker version, finish time), `models` (the configured model names at deposit time; they are *configured*, not
  observed per call), `paper` (version, sha256, bytes, path), a `role` per file, and true UTF-8 `bytes`. The manifest
  lists every file in the run directory except itself and `ro-crate-metadata.json`; `verify` treats an unlisted file in a
  v2 run as an error.

### 3.2 `ro-crate-metadata.json` (the standard, interoperable record)

[RO-Crate 1.2](https://www.researchobject.org/ro-crate/specification/1.2) (Recommendation, 2025-06-04) with the
[Process Run Crate](https://w3id.org/ro/wfrun/process/0.4) profile (v0.4), which is the profile for "tools were run by
hand or by an unincluded script, and the result files are data entities". Each run crate has:

* a root `Dataset` with author (ORCID), license, `about` the paper URL, `conformsTo` the profile, `qnfo:cycle`,
  `qnfo:slug`, `qnfo:pipelineVersion` and the deposit commit/time taken from git history;
* a `File` per artifact with `sha256`, `contentSize`, `encodingFormat` and `qnfo:role`;
* `CreateAction`s for the stages: grounding (objects: the arXiv/DOI sources extracted from `grounding.md`), drafting,
  reconciliation, review, **verification as the pipeline ran it** (status and exit code from the recorded output) and
  **verification re-executed by `tools/provenance.py`** (interpreter version, comparison verdict, stdout hash);
* a contextual entity (not a `hasPart`) for every file the manifest promised and the repository does not hold.

The stage actions other than verification carry `qnfo:basis: inferred-from-procedure`: they follow
[`RESEARCH-PROCEDURE.md`](RESEARCH-PROCEDURE.md), they were not individually instrumented. The model that wrote each
draft is **not recorded** for historical runs and the crate does not pretend otherwise.

PROV-O reading of the same graph: `CreateAction` is a `prov:Activity`; `instrument` is `prov:wasAssociatedWith`;
`object` is `prov:used`; `result` is `prov:wasGeneratedBy` (inverse); the paper is `prov:wasDerivedFrom` the reconciled
draft through the review and verification activities.

### 3.3 `papers/<slug>/provenance.json` ([schema](../schemas/paper-provenance.schema.json))

The paper side of the join: the runs that produced it (`path`, `match`, the manifest hash), what its own README and
header **declare** (version, license, DOIs; recorded, not asserted, because they disagree across papers), identifiers
(`research_queue_ids`, `living_paper_slug`), append-only **snapshots** of `paper.md` (sha256, bytes, version, commit,
basis) and **events** (`corrected`, `retracted`, `restored`, `superseded`). Git history holds every earlier text; the
snapshot list is what lets an auditor tie a hash seen on papers.qnfo.org to a commit without walking history.

### 3.4 `provenance/known-gaps.json` ([schema](../schemas/known-gaps.schema.json)): the ratchet

Every defect the audit found is a row with `kind`, `path`, `cause`, `recovery` and `status`; `expected_sha256` for a
missing file means a restored copy is accepted only if it hashes to that value. `verify` tolerates exactly these rows
and fails on anything else, so the set can only shrink: the commit that closes a gap deletes its row (a gap whose file
is back but whose row remains is a warning). A new defect must either be fixed or appear here with a cause, in the same
commit that introduces it.

## 4. Standards adopted and what was left out

| Standard | Used for | Why |
|---|---|---|
| [RO-Crate 1.2](https://www.researchobject.org/ro-crate/specification/1.2) + Process Run Crate 0.4 | per-run packaging and provenance | A Recommendation with tooling, a profile for exactly this shape (an unincluded script produced the results), JSON-LD so no library is needed to write it. |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | the conceptual model (mapping in 3.2) | RO-Crate's actions map onto it; no separate PROV file is kept, so nothing can drift. |
| [CITATION.cff 1.2.0](https://github.com/citation-file-format/citation-file-format/blob/1.2.0/schema-guide.md) | `CITATION.cff` at the root | GitHub renders "Cite this repository" from it; Zenodo and other tools read the same file. |
| [FAIR4RS](https://zenodo.org/records/6623556) (DOI 10.15497/RDA00068) | checklist for the tooling and records | Findable (identifiers, rich metadata), Accessible (public, open protocol), Interoperable (open formats), Reusable (license, provenance). |
| [SWHID, ISO/IEC 18670:2025](https://www.ouvrirlascience.fr/the-software-hash-identifier-swhid-has-become-an-international-iso-iec-standard/) | intrinsic identifier of the repository state | A git commit hash *is* the SWHID revision id (`swh:1:rev:<commit>`), so identification costs nothing; archiving it is a separate step (section 7). |
| JSON Schema 2020-12 | `schemas/` | The two record types are validated against these files by the tool itself. |
| GitHub Git Data API | the atomic deposit (section 6) | blobs, tree, commit, then one ref update: all or nothing. |
| in-toto / SLSA provenance | **not adopted yet** | They attest a builder identity with a signing key. The pipeline has no signing identity; an unsigned attestation adds a format, not trust. Revisit when the deposit commit is signed. |
| DOI registration | **not used for new papers** | The fleet publishes in-house and writes `doi` NULL (`NOZ-DOI-1`, `NO-REGISTRAR-1`; no external DOI deposit since 2026-10-10). A DOI found in an older README or header is recorded as declared in `provenance.json`; nothing relies on it. |

## 5. Fixity and immutability rules

1. SHA-256 is the fixity function. A file's hash is written when the file is produced and never recomputed to "repair" a
   record.
2. After its `MANIFEST.json` lands, a run directory is append-only: files may be added (the crate, a restored file whose
   hash matches the manifest), never changed. `HASH_MISMATCH` is an error that no ledger row can excuse.
3. `.gitattributes` marks `runs/**` and `papers/**` as `-text`: a checkout with `core.autocrlf` would otherwise rewrite
   line endings and fail every hash.
4. No history rewrites on `main` of this repository. The import of the ensemble history is a merge, not a rebase.
5. **Large files.** The Cloudflare Artifacts mirror refuses a blob over 32 MB; `verify` fails any file over 25 MB. Such a
   file is stored in R2 under `sha256/<aa>/<hash>` and committed as `<name>.pointer.json`
   (`{"sha256", "bytes", "store": "r2", "key", "media_type"}`). Pointer files are validated; the object itself is checked
   by hash when it is fetched.
6. **Secrets** are never committed. Both repositories were scanned for key, token and private-key patterns on 2026-10-26
   (none found; the helper scripts at the root read credentials from environment variables or a file outside the repository).

## 6. Reproducibility rules

* A verification script uses the standard library only (all imports in the 388 deposited scripts are standard library:
  `math` 386, `fractions` 55, `decimal` 11, `cmath` 4, and one each of `itertools`, `json`, `re`, `sys`) and prints one
  `CLAIM ...` line per quantitative claim.
* It is executed as the pipeline executes it: `python -I -c "<script text>"`, in an empty directory, with
  `PYTHONHASHSEED=0` and no network. A string execution has no `__file__`: nine historical runs recorded
  `NameError: name '__file__' is not defined` for that reason, and a file-based re-run would not reproduce the crash.
* The recorded output (`## Execution output` in `verification.md`: stdout, `[stderr]`, `[exit N]`) is compared with a fresh
  run. Verdicts: `reproduced-exact`; `reproduced-equivalent` (same stdout and exit code and exception type; only the
  interpreter-version traceback layout or error suggestion differs, which is what changed between Python versions);
  `not-reproduced`; `no-recorded-output`.
* A script that prints different output on repeated runs, under the same or different hash seeds, is
  `nondeterministic` and is never reported as reproduced. It is a ledger entry until it is regenerated.
* `python3 tools/provenance.py reproduce <run>` does one run; `reproduce --all` runs every script and fails when a run
  that reproduced before no longer does (a regression in the environment or in a file).

## 7. Deposit protocol (what qnfo-research-exec must do, from 0.35.0)

1. Build everything for one paper in memory: the run artifacts (`grounding`, drafts, review, verification, **the
   reconciled paper**), the v2 manifest, the crate, `paper.md`, `README.md`, and the updated `provenance.json` (a new
   snapshot).
2. Write it as **one commit**: create blobs, create a tree on the current head tree, create the commit with the head as
   its parent, move `refs/heads/main` without `force`. If the ref update is refused (another writer committed first),
   re-read the head, rebuild the tree and retry, up to five times with jittered backoff. The cycle number is chosen
   inside that loop, so two writers cannot take the same one.
3. **Verify the write**: read `MANIFEST.json` back at the new commit and compare its hash. Only then is the deposit `ok`.
4. Record it: one `research_run_ledger` row (run id, slug, cycle, paper version, paper sha256, manifest sha256, commit,
   status). A failed deposit is `error` with the reason, is retried by the next tick, and files an issue after three
   failures. It is never reported as `ok`.
5. The retraction/correction path (`ciGithubSync`) goes through the same function: it appends a snapshot and an event, so
   a withdrawal is on the paper's record.

**Archiving (SWHID).** `swh:1:rev:<head commit>` identifies the repository state. Asking Software Heritage to archive
the repository ("save code now") is a one-way publication to a third party, so it is filed as a fleet issue with a
closing probe rather than done from a session; the identifier itself needs no archive.

## 8. What the audit found wrong with the old deposit (and what now prevents it)

| Defect | Cause in the code | Prevention |
|---|---|---|
| 154 manifest-listed files absent from 47 runs; 48 runs with no manifest | `pushArtifactsToGitHub` made one contents-API `PUT` per file on the same branch; concurrent slots got HTTP 409 and the loop ignored the status; the manifest is the *last* file, so a failed run often has none | Atomic single commit with retry (section 7.2); manifest read-back (7.3) |
| 97 of 400 deposit events contained a 409 but were logged `ok` | `return { ok: true, ... }` regardless of per-file status | `ok` only after read-back; `error` otherwise |
| 201 pipeline papers (published when their run was deposited) have no `paper.md` here | the active publish path deposits only to the ensemble repo; only the legacy `publishV2` wrote `papers/<slug>/` | the paper is part of the same commit; a backfill job restores the missing ones from living-paper |
| No `publication_artifacts` rows for any deposit | unquoted SQL (`datetime(now)`) inside an empty `catch` | rows go to `research_run_ledger`; errors are logged and counted |
| the reconciled paper is not in the run | `collectArtifacts` omits `reconciled.md` | included (role `reconciliation`) |
| the cycle number can collide | `max(cycle-N)+1` read before the writes | chosen inside the retry loop |
| `bytes` is not a byte count | JS `String.length` | v2 uses UTF-8 bytes |

## 9. Verifying

```
python3 tools/provenance.py verify              # integrity, completeness, linkage, schemas, blobs  (exit 1 on any error)
python3 tools/provenance.py verify --strict     # warnings fail too
python3 tools/provenance.py reproduce runs/cycle-396/<slug>
python3 tools/provenance.py reproduce --all
python3 tools/provenance.py index               # paper <-> run catalog, JSON lines
python3 -m unittest discover -s tools -p 'test_*.py'
```

CI runs the tests and `verify` on every push and pull request that touches the research trees
(`.github/workflows/provenance.yml`), and `reproduce --all` on pull requests that touch `runs/`.

## 10. Limits, stated plainly

* The record proves what was deposited and that it has not changed since. It does not prove that a model's claim is
  true, that a cited source supports the sentence around it, or that the verification script tests the right thing.
* Historical runs do not record which model wrote which draft, or when the verification ran (the deposit time is used
  and labelled as such). New runs record the configured models, not the model that answered each call.
* Nothing here is signed. Integrity rests on git's content addressing, the Cloudflare Artifacts mirror (a second copy
  that `artifact_sync_state` compares with GitHub) and the D1 ledger that holds the same hashes outside git.
* The 201 papers without text in this repository are a recorded gap until the backfill job has restored them; the
  published text on papers.qnfo.org (living-paper D1) is the source of that restore.
