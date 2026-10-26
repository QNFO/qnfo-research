# runs/ : pipeline runs

One directory per run of the QNFO automated research pipeline, kept exactly as deposited.
This directory is the former `QNFO/qnfo-ensemble-research` repository (imported 2026-10-26 with its full history,
see `../provenance/IMPORT.json`); the paths are unchanged.

```
runs/cycle-<N>/<slug>/
    grounding.md                 literature grounding (the sources the drafts may cite)
    writer-a-draft.md, ...       independent drafts
    reconciled-paper.md          the reconciled paper of the run (deposits from 0.35.0)
    review-report.md             adversarial review
    verification.py              the script that checks each quantitative claim
    verification.md              claims, script, recorded execution output, adjudication
    MANIFEST.json                the pipeline's hash record. Frozen: never rewritten.
    ro-crate-metadata.json       RO-Crate 1.2 (Process Run Crate) record: files, hashes, stages, re-execution
runs/cycle-1/                    the 2026-09-08 pilot: three writers, one manifest for the cycle
```

* The paper a run produced is `papers/<slug>/paper.md` (or `<program>/<slug>/`); `papers/<slug>/provenance.json` lists its
  runs. 201 pipeline papers do not have their text in the repository yet; `../provenance/known-gaps.json` lists each one.
* Never edit a file here. `python3 tools/provenance.py verify` fails on any change to a hashed file.
* `python3 tools/provenance.py reproduce runs/cycle-N/<slug>` re-runs the verification script and compares it with the
  recorded output.

Standard: `../docs/PROVENANCE-STANDARD.md`. Audit and numbers: `../docs/REPOSITORY-AUDIT-2026-10-26.md`.
The pilot's original README and provenance standard are in `../docs/provenance/`.
