# Kaizen Draft — R2/R2-Registry/Phase-Discipline Gates (2026-08-16)

**Status:** DRAFT — proposed for installation in the next dedicated kaizen session (skills dir `C:\Users\LENOVO\.deepchat\skills` is outside session allowed paths; install requires the kaizen update protocol + user approval).
**Origin:** CMD RED TEAM 5-adversary audit findings A-1/A-2/C-3/D-1/D-2 (session pVxPB_ViPCLUkdaDtykwu, 2026-08-16).
**Owner (proposed):** knowledge skill (R2/registry sections) + research skill (Phase 1 verification) + kaizen skill (cross-ref table).

---

## Gate 1 — R2-PREFIX-PROBE-SCOPE-1 (HARD)

**Anti-pattern:** declaring an R2 mirror "missing" / "0 objects" based on probes of only ONE key-layout prefix.

**Canonical case (2026-08-16):** probes for `exchange-phase-logical-scalar` tested `2026/08/<slug>`, bare `<slug>`, `papers/<slug>` — but NOT `releases/2026/08/<slug>` (the legacy nested layout INSIDE `qnfo-releases`, used for the July/August fleet). Result: false "missing mirror" verdict → 40 duplicate object uploads + a 3-node registry regression (reverted in dcab428).

**Mandate:** before declaring any mirror absent, probe ALL known key-layout prefixes per bucket:
1. `YYYY/MM/<slug>` (flat — current canonical per knowledge v2.12)
2. `releases/YYYY/MM/<slug>` (legacy nested layout — real, in-use for the July/August fleet)
3. `papers/<slug>` (architecture-doc v1.0 convention) and `papers/<slug>/YYYY-MM-DD` (invariant-structural-value style)
4. bare `<slug>` (root-level placements: pbo, zbw-fw-null-test style)
5. **PAGINATE fully** (`result_info.is_truncated` + `result_info.cursor`; API caps at `per_page=20`) — a truncated listing is not a count.
6. Verify the API result shape (bare list vs `{objects: []}`) before trusting object counts.

A "0 objects" verdict from an under-scoped probe is a probe defect, not a data absence (BLAME-EXTERNAL-1: the fault is local).

## Gate 2 — R2-ABSENCE-DOC-GATE (HARD, extends AUDIT-COMPLETENESS-1)

**Anti-pattern:** declaring R2 objects absent/lost/unrecoverable without first reading `qnfo-audit/architecture/R2-MULTI-BUCKET-ARCHITECTURE.md` (or its latest version) and enumerating the full bucket fleet.

**Canonical case (2026-08-16):** "ZERO objects in any bucket" declared before the architecture doc was read; the doc (read later) documented the bucket fleet + path conventions that would have scoped the probes correctly.

**Mandate:** AUDIT-COMPLETENESS-1's read-the-doc-first rule applies to **absence declarations** as well as destruction declarations. Sequence: (1) read architecture doc, (2) enumerate fleet (`GET /r2/buckets`), (3) probe per Gate 1 with full pagination, (4) only then assert absence.

## Gate 3 — DATA-OWNERSHIP-1 (HARD, extends GIT-OWNERSHIP-1 to registries/object stores)

**Anti-pattern:** writing KG nodes / D1 rows / R2 objects for a record owned by ANOTHER program or project without that owner's session or an explicit mandate.

**Canonical case (2026-08-16):** H-1 "remediation" demoted 3 ACRP-owned KG nodes (`distribution_status: distributed` → `published`, phantom r2_path removed) based on a false absence verdict — a regression on truthful records, reverted after ownership-blind remediation.

**Mandate:** before any KG/D1/R2 write to a record: (1) identify the owning program/project (KG `program`/`project` properties, program_registry rows, branch ownership); (2) if the owner is another program: do NOT write — document the finding + register a remediation item for the owner; (3) if the owner is this session's project or the finding is mandate-covered, proceed with read-back verification. Mirrors/registry fixes discovered in one project's cycle become findings + owner-registered items, not writes.

## Gate 4 — PHASE-BOUNDARY-DISCIPLINE-1 (HARD, process)

**Anti-pattern:** a Phase-1 due-diligence cycle executing P6/P7-class distribution writes (R2 mirrors, registry distribution-status updates, D1 r2_key changes) without a phase-transition directive.

**Canonical case (2026-08-16):** CMD RESEARCH (Phase 1) → immediate remediation writes; the CMD EXECUTE authorization arrived only after the first writes.

**Mandate:** each cycle declares its phase scope in the WBS-coded plan (P0 pre-flight / P1 due diligence / P2-P5 project phases / P6-P8 distribution). Writes beyond the declared phase require either (a) an explicit CMD directive naming the phase, or (b) a plan revision marking the phase transition, with the transition recorded in the plan explanation. Remediation of findings discovered in an audit MAY be executed in the same cycle ONLY when the finding is owned by the cycle's project AND the write is registry-truth-restoration; cross-project remediation = findings + owner-registered items (Gate 3).

---

## Installation checklist (for the kaizen session)
- [ ] Add Gates 1-3 to `knowledge` skill (R2/registry sections) + `research` skill (Phase-1 verification) — HARD gates.
- [ ] Add Gate 4 to `research` skill phase-architecture section + execution-mandate skill.
- [ ] Add all four to the kaizen anti-pattern table with canonical cases (this file is the source).
- [ ] Cross-reference R2-MULTI-BUCKET-ARCHITECTURE.md v1.1 (layout conventions reconciliation, published 2026-08-16).
- [ ] Verify 5-store prompt parity + N-2 frontmatter after install.
