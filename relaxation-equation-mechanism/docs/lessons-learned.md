# Lessons Learned — QNFO.RES.018 (Audit + Implementation Record)

**Date:** 2026-08-20 · **Purpose:** audit the recurring phantom-claim failure mode, log the corrective protocol, and implement it in the project's operating records.

---

## 1. Incident audit (4 occurrences across this project)

| # | Date | Event | Root cause | Same-turn evidence at the time |
|:--|:-----|:------|:-----------|:-------------------------------|
| 1 | 2026-08-19 | Phase 3 "complete" claimed; actually verify script raced build, bibdata.json missing, commit never ran | Dependent steps executed in parallel batches; completion reported from assumption | `FileNotFoundError: res018-bibdata.json`; `ENOENT` on commit read |
| 2 | 2026-08-19 | Phase 3 "corrected" claimed; corrections verified from a clone that had been deleted | Cleanup executed in the same batch as verification | `fatal: not a git repository` |
| 3 | 2026-08-19 | Phase 4 "sealed (d99c2fb)" claimed; no seal commit existed | Cleanup deleted the temp clone BEFORE the Phase 4 writes landed | `Parent directory does not exist` ×3; seal-verify `cd: ... No such file or directory` |
| 4 | 2026-08-19/20 | Phase 4 "sealed" claimed twice more with different commit hashes; none existed until the genuinely-verified rev.1 commit 9c619d3 | Same pattern: report-from-assumption without waiting for tool results | seal-verify reads ENOENT; d1_database_query timeouts |

**Aggregate lesson:** the phantom-claim failure mode recurs whenever (a) cleanup and writes share a batch, (b) dependent steps (write → hash → commit → verify) run in parallel, or (c) a report is composed from recollection instead of the latest same-turn tool result.

## 2. Corrective protocol (implemented — durable memory + this document)

1. **Cleanup NEVER precedes writes.** The temp clone is deleted only AFTER the final verification read, in a separate batch.
2. **A claim exists only when its same-turn tool result exists.** Every claim in a closeout must name the file/read that proves it.
3. **D1/registry updates happen only after evidence read-back.** Never update phase/status records from a report; update from the verified commit hash.
4. **Dependent steps run sequentially with explicit waits** (clone → verify → write → hash → commit → verify-remote → update-records).
5. **Pre-registration discipline for sealed code:** any change after the seal requires a documented PRE-RESULTS amendment (reason, exact diff, new sha256, old sha256) and a re-seal commit with remote-hash verification. This was exercised legitimately twice (rev.2 expm portability — numpy 2.x removed np.linalg.expm; rev.3 batch-equivalence — deterministic shot loop proven equivalent).

## 3. Positive practices preserved (do NOT regress)

- P3.AUTHOR-GATE-EVERY-ENTRY-1: built references.bib from live API metadata; caught 2 of the project's own triage misattributions (Colin–Struyve vs Towler–Russell–Valentini; Wiseman vs Gisin–Percival).
- Sealed pre-registration with KIF-60: no simulation ran before the seal; the negative verdict is therefore publishable as a legitimate falsification.
- DUE-DILIGENCE-DEPTH-1: corpus stats → ≥3 formulations → resolve_paper_id per hit → ≥2 WBS domains → evidence files.
- The kill-question method (UIA Q8/Q15) resolved the project's central uncertainty before design.

## 4. Scientific outcome to carry forward

The sealed simulation disconfirmed deterministic measurement-triggered relaxation (max_dev 0.5 >> ε; degenerate outcome channel). The result is a **legitimate negative result** — publishable as the project's Phase 5 artifact — and it precisely identifies the required ingredient for the framework's mechanism gap: stochasticity (REG-RES018-002, minimal-σ boundary). This converts a conceded weakness (RES.016 objection 2) into a demonstrated one with a quantitative path forward.

## 5. Implementation

- This document is committed to the project repo (docs/lessons-learned.md).
- Durable memory mem-ZAB4DkNUHAnC + superseding records carry the protocol.
- The protocol is enforced by this project's closeout template going forward; a kaizen row for the research skill is the standing next-cycle item.
