# ERRATA — QNFO.RES.004 / QNFO.RES.005 WBS Collision Resolution

**Date:** 2026-08-13 · **Applies to:** program_registry (D1), KG nodes/edges, qnfo-research repo tags
**Trigger:** Mandate 3 reviewer subagent audit (delegation UvVgwFVWi64PmgGa6kmNH) — HARD-1 cross-system WBS collision.

## Incident

- **2026-08-12** — commit `462c36b` tagged `v0.1-phase0-res004`, message *"feat(res.004): Phase 0 scaffold for QWAV GTM/R&D strategy"* (directory `qwav-gtm-strategy/`). QNFO.RES.004 = **QWAV GTM/R&D Strategy** (parent records: completed through Phase 4; only surviving traces: the tag + KG node `paper:qwav-gtm-strategy`).
- **2026-08-13** — Phase 0 WBS resolution for Prime Valuation Depth queried D1 `program_registry` + `WBS.TAXONOMY.md`, found no RES.004 row, and assigned **QNFO.RES.004 = Prime Valuation Depth** without checking the git-tag namespace. Collision created.

## Resolution (renumbering decision)

1. **QWAV GTM/R&D Strategy keeps `QNFO.RES.004`** — prior claim, tag evidence, P4-complete. Re-anchored in D1 `program_registry` (wbs_order 3, kg_node_id `proj-qwav-gtm-strategy`) and KG node `proj-qwav-gtm-strategy` + `BELONGS_TO → prog-res`.
2. **Prime Valuation Depth renumbered to `QNFO.RES.005`** — D1 row UPDATE (wbs_order 4, phase P8, status published, kg_node_id `proj-prime-valuation-depth`, d1_slug `prime-valuation-depth`, current_version `v0.1-published`); KG properties updated on `proj-prime-valuation-depth` + `paper:prime-valuation-depth`.
3. **Published artifact unaffected** — the Zenodo deposit (DOI 10.5281/zenodo.21918032) carries zero WBS codes in the paper body (INTERNAL-REF-1 compliance verified at P5); no newversion required.
4. **Git tags unchanged** (immutable public refs): `v0.1-phase0-res004` → GTM; `v0.1-phase0-prime-valuation-depth` + `v0.1-published-prime-valuation-depth` → Prime (RES.005).

## Prevention

Phase-0 WBS resolution MUST check ALL namespaces before assigning: D1 `program_registry` + `WBS.TAXONOMY.md` + **git tags in the target repo** + KG paper/project nodes. The `v0.1-phase0-res004` WBS-numeric tag convention is deprecated (see D1 finding); slug-suffixed tags are canonical.
