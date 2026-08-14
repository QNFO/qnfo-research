# Toy-Model Suite Deposit — Publication Decision (P7)

**WBS:** QNFO.RES.009.P7 · **Date:** 2026-08-14 · **Status:** DECISION MADE — separate Zenodo deposit
**Scope:** publication vehicle for the T4–T7 toy-model suite + disciplined companion essay.

## Decision record

**Question:** should the T4–T7 toy-model suite (companion essay + four executable
notebooks) be published as (a) a separate Zenodo deposit, or (b) attached to the paper
v1.1 newversion?

**Decision: SEPARATE Zenodo deposit.** Rationale:
1. **v1.1 is a correction vehicle.** Its scope is the §5/F2 abelian-pair amendment and
   references.bib remediation (concurrent session's cycle). The toy-model suite is a
   research expansion, not a correction — mixing them muddies both artifacts.
2. **No Zenodo collision.** The concurrent session owns the v1.1 newversion; a second
   writer on the same deposit risks NEWVERSION-FRONTMATTER-CARRYOVER-1-class races.
3. **The suite is a coherent standalone contribution:** one arc (statistics from
   syntactic exchange → boundary cost → capacity ceiling → second-law-gated braids),
   four executable models, honest [TOY MODEL — SYNTACTIC] / [NOT YET EVIDENCE] labels,
   and a disciplinary story (three idealizations caught by pre-registered tests in T7
   alone — the suite is itself a case study in pre-registration discipline).

## Deposit bundle manifest

| File | Role |
|---|---|
| `docs/companion-essay-draft.md` | Flagship essay (disciplined register; [RETRODICTION]/[NOT YET EVIDENCE]/[EXTRAPOLATION] labels) |
| `artifacts/notebooks/t4-toy-model.md` + `.py` | Statistics from syntactic exchange (P1, REG-009-001) |
| `artifacts/notebooks/t5-boundary-cost-model.md` + `.py` | Boundary cost (FQ1, REG-009-002) |
| `artifacts/notebooks/t6-capacity-bound.md` + `.py` | Capacity ceiling (FQ1 formal, REG-009-003) |
| `artifacts/notebooks/t7-second-law-gated-braid.md` + `.py` | Second-law-gated braids (FQ3, REG-009-004; exact-chain version) |
| `docs/fq3-irreversibility-mapping.md` | FQ3 mapping (arrow at the erasure gate) |
| `RESEARCH-CONTINUITY-REGISTRY.md` | Pre-registration scaffold + falsifiability ledger |
| README (generated at deposit time) | Bundle map + relationship to the published paper (DOI 10.5281/zenodo.21938971) + the three-deep-inquiry-note provenance |

## Proposed metadata (for the CMD PUBLISH cycle)

- **Title:** "From Distinction to Dissipation: Companion Essay and Executable Toy-Model
  Suite for the Boson/Fermion Distinction Program" (final title decision at publish).
- **Description:** the suite answers the deep-inquiry question "what is the cost of
  drawing a boundary?" at toy-model level: the draw is free (reversible), the upkeep is
  not; capacity ceiling floor(ΔS/k_B ln 2); implementable braid set = f(p, P, T) with
  inversion toll 2 kT ln 2. All claims labeled [TOY MODEL — SYNTACTIC] / [NOT YET
  EVIDENCE]; no physical derivation is claimed.
- **License:** cc-by-4.0. **Community:** qnfo. **Language:** eng.
- **Related identifiers (isSupplementTo):** https://github.com/QNFO/qnfo-research/tree/res/paper/spin-statistics-distinction
  (PUBLICATION-SOURCE-COMPLETENESS-1 shape) + the paper DOI 10.5281/zenodo.21938971.

## Publish checklist (for the CMD PUBLISH cycle)

- [ ] Verify the essay's four references (Marletto–Vedral arXiv:2112.03392; Pauli 1940
      PR 58, 716; Spencer-Brown 1969; Quni-Gudzinas 2026) via Crossref/arXiv (citation
      audit).
- [ ] Re-run all four notebooks one final time (pinned outputs) before upload.
- [ ] BP-1..BP-10 gates (research skill §P5): language gate, no internal WBS codes in
      the essay body (INTERNAL-REF-1), AI-quality gate, source-completeness gate.
- [ ] README generation + GitHub related_identifiers (branch URL).
- [ ] Zenodo new deposit (not a newversion of the paper — separate concept) → publish →
      verify records API + DataCite + OpenAIRE.
- [ ] Registry §7 log entry; memory closeout.
