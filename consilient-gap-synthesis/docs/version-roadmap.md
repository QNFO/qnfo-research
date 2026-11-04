# Version Roadmap — Consilient Gap Synthesis

**Date:** 2026-07-29
**Based on:** Phase 2 Gap Registry (42 gaps, 5 categories)
**Principle:** Topological sort of dependency DAG → phased releases

---

## Overview

The 42 identified gaps form a predominantly acyclic dependency graph with depth ≤3. Infrastructure gaps block Content gaps, which block Dissemination gaps. This natural layering maps directly to versioned releases:

| Version | Theme | Gaps | Effort | Cumulative Impact |
|:--------|:------|:-----|:-------|:------------------|
| **v2.0** | Infrastructure Foundation | 5 HIGH + 5 MEDIUM | ~4 sessions (L) | Unblocks 40% of remaining gaps |
| **v2.1** | Content Registry Remediation | 2 HIGH + 5 MEDIUM | ~3 sessions (M) | 917 papers verified, all cross-reference gaps closed |
| **v2.2** | Governance Completion | 1 HIGH + 1 MEDIUM | ~5 sessions (XL) | QNFO.GOV complete, 17 tasks executed |
| **v2.3** | Physics Validation Pipeline | 1 MEDIUM + 4 LOW | ~8 sessions (XL) | All unvalidated claims triaged |
| **v2.4** | Dissemination Closeout | 2 MEDIUM + 1 LOW | ~1 session (S) | All published papers disseminated |

---

## v2.0 — Infrastructure Foundation ⭐

**Theme:** Resolve the root blockers that cascade into all downstream gap categories.

**Target effort:** 4 sessions
**Target completion:** 2026-08-05

### Tasks

| ID | Task | Gap | Effort | Priority |
|:---|:-----|:----|:-------|:---------|
| V2.0-01 | Build Consistency Engine Worker (OI-003) | I-01 | **L** | 1 — Root blocker |
| V2.0-02 | Recover Infomatics from R2, rebuild GitHub history | I-02 | **M** | 2 |
| V2.0-03 | Create biophoton GitHub remote + push all tags | I-03 | **S** | 3 |
| V2.0-04 | Redeploy qnfo-hub Pages (papers-server 404 fix) | I-05 | **S** | 4 |
| V2.0-05 | Sync qnfo-unified-plan to R2 | I-04 | **S** | 5 |
| V2.0-06 | Create the-informational-universe GitHub repo + Phase 0 scaffold | I-07 | **S** | 6 |

### Verification Gates
- Consistency Engine Worker running, queryable via API
- Infomatics repo on GitHub with linear master history
- biophoton repo pushed to QNFO GitHub org
- `curl -sI https://papers.qnfo.org/papers/paper-computable-real-boundary` → HTTP 200
- `npx wrangler r2 object get qnfo-projects/qnfo-unified-plan/releases/qnr-justification-memo-v5.0.pdf --remote` → file round-trips

---

## v2.1 — Content Registry Remediation

**Theme:** Fix cross-reference gaps — D1 missing DOIs, paper_ids registry, vectorization, KG sync.

**Target effort:** 3 sessions
**Target completion:** 2026-08-10

### Tasks

| ID | Task | Gap | Effort | Priority |
|:---|:-----|:----|:-------|:---------|
| V2.1-01 | Verify 463 D1 papers with missing DOIs — cross-reference KG properties | C-01 | **L** | 1 |
| V2.1-02 | Seed 7 missing paper_ids registry entries | C-02 | **S** | 2 |
| V2.1-03 | Vectorize biophoton paper body | C-03 | **S** | 3 |
| V2.1-04 | Create biophoton KG Paper node + edges | C-04 | **S** | 4 |
| V2.1-05 | Update qnfo-unified-plan D1 living-paper row (v5.0 metadata) | C-06 | **S** | 5 |
| V2.1-06 | Run KIF-23 reconciliation: D1↔KG paper count re-check | — | **M** | 6 |
| V2.1-07 | Resolve fine-structure-constant-cross-ratio active status | C-13 | **M** | 7 |

### Verification Gates
- 463-DOI audit report with breakdown (kg-backfill vs genuine missing)
- `SELECT COUNT(*) FROM paper_ids` = `SELECT COUNT(*) FROM papers` (910→917)
- `search_papers("biophoton ultrametric")` returns biophoton paper
- `query_graph(neighbors, paper:biophoton-ultrametric-consilience)` returns edges
- D1↔KG paper delta ≤ 5 (acceptable drift, any remainder flagged for next audit cycle)

---

## v2.2 — Governance Completion

**Theme:** Complete QNFO.GOV governance framework and kepler sub-project audits.

**Target effort:** 5 sessions
**Target completion:** 2026-08-25

### Tasks

| ID | Task | Gap | Effort | Priority |
|:---|:-----|:----|:-------|:---------|
| V2.2-01 | Execute 17 remaining QNFO.GOV tasks across 3 phases | G-01 | **L** | 1 |
| V2.2-02 | Audit kepler sub-projects (Phase 0 protocol compliance) | G-02 | **M** | 2 |
| V2.2-03 | Update CFPE quarterly calibration register | G-03 | **S** | 3 |
| V2.2-04 | (If I-01 complete) Wire automated compliance checks | G-04 | **XL** | 4 |
| V2.2-05 | Publish Infomatics (recovered from I-02) through full pipeline | C-05 | **M** | 5 |
| V2.2-06 | Publish the-informational-universe (repo from I-07) | C-07 | **L** | 6 |

### Verification Gates
- QNFO.GOV all 36/36 tasks marked complete
- All kepler sub-projects have Phase 0 tags and PROJECT-PLAN.md
- Infomatics DOI live on Zenodo, papers-server HTTP 200

---

## v2.3 — Physics Validation Pipeline

**Theme:** Triage all unvalidated physics claims — calibration training, experiment execution, external literature.

**Target effort:** 8 sessions
**Target completion:** 2026-09-20

### Tasks

| ID | Task | Gap | Effort | Priority |
|:---|:-----|:----|:-------|:---------|
| V2.3-01 | If hardware available: run ultrametric-well neural operator training | P-01, I-06 | **XL** | 1 |
| V2.3-02 | Complete biophoton Bayesian cascade calibration training (Stage -1) | P-04 | **M** | 2 |
| V2.3-03 | Validate biophoton PW clock extrapolation | P-05 | **L** | 3 |
| V2.3-04 | Draft formal LoF proof for measurable G2 (Re-entry fixed point) | P-02 | **M** | 4 |
| V2.3-05 | Execute measurable G3 experiment (ultrametric vs Archimedean error) | P-03 | **L** | 5 |
| V2.3-06 | Resolve biophoton external literature gap | — | **M** | 6 |

### Verification Gates
- Calibration training Brier score recorded for biophoton cascade
- G2 formal proof committed (or marked [DEFERRED: beyond current scope])
- G3 experiment results documented (or marked [NOT-YET-FALSIFIABLE])
- ultrametric-well marked [COMPLETED] or [HARDWARE-BLOCKED: escalated]

---

## v2.4 — Dissemination Closeout

**Theme:** Final distribution — Buffer posts, remaining social media, closeout verification.

**Target effort:** 1 session
**Target completion:** 2026-09-25

### Tasks

| ID | Task | Gap | Effort | Priority |
|:---|:-----|:----|:-------|:---------|
| V2.4-01 | Resolve Buffer token staleness (KIF-45) | D-02 | **S** | 1 |
| V2.4-02 | Buffer post: biophoton-ultrametric-consilience | D-01 | **S** | 2 |
| V2.4-03 | Buffer post: qnfo-unified-plan v5.0 | D-03 | **S** | 3 |
| V2.4-04 | Full-stack verification: GitHub+Zenodo+R2+D1/KG for all v2.x deliverables | — | **M** | 4 |

### Verification Gates
- Buffer queue shows 3+ posts SCHEDULED across Twitter/LinkedIn/Bluesky
- All v2.x deliverables pass Core Distribution Gate

---

## Gap-to-Version Mapping (Quick Reference)

| Gap ID | Version | Task |
|:-------|:--------|:-----|
| I-01 ⭐ | v2.0 | V2.0-01 |
| I-02 | v2.0 | V2.0-02 |
| I-03 | v2.0 | V2.0-03 |
| I-04 | v2.0 | V2.0-05 |
| I-05 | v2.0 | V2.0-04 |
| I-06 | v2.3 | V2.3-01 |
| I-07 | v2.0 | V2.0-06 |
| C-01 | v2.1 | V2.1-01 |
| C-02 | v2.1 | V2.1-02 |
| C-03 | v2.1 | V2.1-03 |
| C-04 | v2.1 | V2.1-04 |
| C-05 | v2.2 | V2.2-05 |
| C-06 | v2.1 | V2.1-05 |
| C-07 | v2.2 | V2.2-06 |
| G-01 | v2.2 | V2.2-01 |
| G-02 | v2.2 | V2.2-02 |
| G-03 | v2.2 | V2.2-03 |
| D-01 | v2.4 | V2.4-02 |
| D-02 | v2.4 | V2.4-01 |
| D-03 | v2.4 | V2.4-03 |
| P-01 | v2.3 | V2.3-01 |
| P-02 | v2.3 | V2.3-04 |
| P-03 | v2.3 | V2.3-05 |
| P-04 | v2.3 | V2.3-02 |
| P-05 | v2.3 | V2.3-03 |

**LOW-severity gaps (I-08 through I-16, C-08 through C-14, G-04):** Deferred to v2.5+ backlog. These are nice-to-haves that do not block any other gap and carry low EV per session relative to v2.0-v2.4.

---

## Timeline Summary

```
v2.0 ████████░░░░░░░░░░░░░░░░ 2026-08-05  (4 sessions, Infrastructure Foundation)
v2.1 ░░░░░░░░████████░░░░░░░░ 2026-08-10  (3 sessions, Content Registry)
v2.2 ░░░░░░░░░░░░░░░░████████ 2026-08-25  (5 sessions, Governance Completion)
v2.3 ░░░░░░░░░░░░░░░░░░░░░░██ 2026-09-20  (8 sessions, Physics Validation)
v2.4 ░░░░░░░░░░░░░░░░░░░░░░░█ 2026-09-25  (1 session,  Dissemination)
                                   ↑
                          Total: ~21 sessions
                          8 calendar weeks
```

**Parallelization opportunity:** v2.3 (Physics Validation) is largely independent of v2.1-v2.2 (it depends only on I-06 from v2.0, which is hardware-blocked). v2.3 can start in parallel with v2.1 if resources permit. This would compress the total timeline from 8 weeks to ~6 weeks.

---

## Risk-Adjusted Timeline

| Risk | Probability | Impact on Schedule |
|:-----|:-----------|:-------------------|
| Consistency Engine (I-01) takes >3 sessions | Medium | +2 weeks (cascades to v2.1) |
| QNFO.GOV tasks hit unforeseen policy blockers | Medium | +3 weeks |
| ultrametric-well remains hardware-blocked | High | v2.3 unaffected (it's deferred, not blocking) |
| Buffer token not regenerated by user | Medium | v2.4 blocked until resolved |
| New gaps discovered during v2.0 execution | High | +1-2 weeks (cataloged, not blocking) |

**Best case:** 6 weeks (with parallelization)
**Expected:** 8 weeks
**Worst case:** 13 weeks (all risks materialize)
