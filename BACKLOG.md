# BACKLOG — LLM Force Multiplier

> Prioritized future work queue. Items move to SPRINT.md when activated.

## Priority Legend
- **P0:** Next immediate action
- **P1:** This sprint or next
- **P2:** Within 1-2 sprints
- **P3:** Future / nice-to-have

---

## P0 — Immediate Next Steps

| ID | Task | Status | Notes |
|:---|:-----|:-------|:------|
| B-001 | Decide next sprint focus | ✅ Done | Sprint 2: arXiv preparation + backlog cleanup |
| B-002 | Human review of 0.2.md | 🔄 In Progress | Architecture reviewed; full read-through pending |
| B-018 | Submit to arXiv | ⬜ Pending | Manuscript ready; metadata added to 0.2.md |

## P1 — Core Development

| ID | Task | Status | Notes |
|:---|:-----|:-------|:------|
| B-003 | Extract prompt library as standalone file | ✅ Done | Embedded in 0.2.md Appendix A; reusable format |
| B-004 | Expand mini-paper into full manuscript | ✅ Done | 0.2.md — 8 sections, 3 appendices, 26 refs |
| B-005 | Containerize Solo-Research Stack | ⬜ Pending | Dockerfile in Appendix C (aspirational); useful for distribution |
| B-006 | Add literature review | ✅ Done | 0.2.md §1.4 — 14 references, AI-augmented research survey |
| B-007 | Develop verification checklist for LLM outputs | ⬜ Pending | Critical for scientific integrity; not yet drafted |
| B-019 | Add third validation case study | ⬜ Pending | Comp bio or pure math needed to strengthen §6 |

## P2 — Validation & Generalization

| ID | Task | Status | Notes |
|:---|:-----|:-------|:------|
| B-008 | Design controlled experiment protocol | ✅ Done | 0.2.md §5 — 3-condition between-subjects, power analysis |
| B-009 | Recruit participants for controlled experiment | ⬜ Pending | Requires institutional access; postdocs or graduate students |
| B-010 | Computational biology case study | ⬜ Pending | Phylogenetic tree reconstruction with Snakemake/IQ-TREE walkthrough |
| B-011 | Pure mathematics case study | ⬜ Pending | Proof-assistant integration with Lean/Coq walkthrough |
| B-012 | Philosophy of science case study | ⬜ Pending | Systematic review of realism vs. anti-realism arguments |
| B-020 | Sensitivity analysis for experiment power | ✅ Done | Added in reader test fix — σ = 40/80/120h scenarios |

## P3 — Dissemination

| ID | Task | Status | Notes |
|:---|:-----|:-------|:------|
| B-013 | Submit to arXiv | ⬜ Pending | arXiv metadata added to 0.2.md; ready for upload |
| B-014 | Target journal submission | ⬜ Pending | Nature Human Behaviour / Synthese / Royal Society Open Science |
| B-015 | Develop workshop/tutorial materials | ⬜ Pending | For early-career scientists |
| B-016 | Create project website / landing page | ⬜ Pending | Public face of the methodology |
| B-017 | Video walkthrough of force-multiplier protocol | ⬜ Pending | Demonstration for wider audience |
| B-021 | Format 0.2.md as LaTeX for journal submission | ⬜ Pending | pandoc conversion + journal-specific formatting |
| B-022 | Add acknowledgments section with grant info | ⬜ Pending | Placeholder exists; needs actual grant numbers |

## Backlog Cleanup Notes (2026-05-13)
- B-003, B-004, B-006, B-008, B-020: Marked DONE — completed during Sprint 1
- B-018, B-019, B-020, B-021, B-022: New items added from session discoveries
- B-005: Retained despite architecture correction — Docker stack still useful for distribution
- B-010-B-012: Retained — cross-domain case studies are the strongest remaining evidence gap
