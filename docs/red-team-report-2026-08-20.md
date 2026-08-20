# Red-Team Audit Report — QNFO.RES.021 (2026-08-20, CMD RED TEAM)

**Audited artifact:** branch `res/paper/finite-distinction-quantum-mechanics` at
fac9b82 (QNFO/qnfo-research). READ-ONLY audit; no audited file was modified. This
report is the aggregation required by the POST-PUBLICATION ADVERSARIAL ANALYSIS GATE.

**Dispatch:** 3 reviewer slots (Accuracy / Completeness / Dependency) + carry-over of
the completed Phase 0/1 review (4 SOFT, 0 HARD). Result per slot:

| Slot | Result |
|---|---|
| Accuracy | COMPLETED — 1 HARD, 5 SOFT |
| Completeness | FAILED (child session completed without a final answer — SUBAGENT-SLOT-FAILURE-1) → direct parent fallback: core targets PASS, 3 SOFT |
| Dependency | COMPLETED — 1 HARD, 7 SOFT |
| Phase 0/1 (prior) | COMPLETED — 0 HARD, 4 SOFT |

**Novelty (parent, direct):** G1 (entropy-Hessian → unitarity emergence with finite-N
predictions) remains uncovered in the corpus after 5 sweep formulations; external
anchors (Gisin, PBR, Hardy, Aaronson, Vedral) constrain but do not pre-empt. Novelty
HOLD (graded conjecture).

**Status (parent, direct):** branch head fac9b82 pushed + ls-remote verified; tag
v0.1-phase0-res021 present at P0 commit 3027054 (correct phase-tag placement);
program_registry phase P2; handoffs 28653/28654; KG-stats claims in the evidence file
match live `query_graph(stats)` exactly (reviewer-verified).

---

## HARD FINDINGS (2 — internal consistency, no fabricated citations, no claim inflation)

- **H-1 (Accuracy).** PROJECT-PLAN.md §9 and docs/deep-research.md §6 state "6
  cross-system validations (2 partial flagged)"; the authoritative evidence table
  (artifacts/external-search/evidence-2026-08-20.md §3) shows **3 of 6 rows PARTIAL**
  (continuum-trilogy-01, valuation-independent-foundations, time-from-a-timeless-
  universe). Canonical count = 3. Remediation: reword both summaries to "3 partial
  (1–2 flagged)" and add the missing flag annotation in the evidence table.
- **H-2 (Dependency).** docs/paper-outline-2026-08-20.md footer claims "the UIA Q15
  seed … is answered explicitly in §5"; §5 contains NO answer to the Q15
  meta-question (does N→∞ reimport the continuum via the parameter space?). Load-
  bearing (it is the registered seed of the next audit pass). Remediation: add an
  explicit §5 treatment of the Q15 question, or re-point the footer claim.

## SOFT FINDINGS (13, deduplicated across slots)

| # | File | Finding |
|---|---|---|
| S-1 | evidence §3 | Slug label `continuum-trilogy-01-…` for DOI 10.5281/zenodo.21672990; the DOI is the trilogy concept DOI and the cited Depth/Breadth/Valuation content is trilogy-03 — align the label to trilogy-03. |
| S-2 | outline footer | Section-to-gap map assigns G4 to §3 (no relational-time content there; §7 is the G4 section) and omits G2 for §3's underdetermination paragraph. |
| S-3 | plan §9 | "12 external imports live-verified" not enumerable from the evidence file (no 12-item enumeration exists). Add the enumeration or reword. |
| S-4 | plan header | Header still says "Status: Phase 0 — Initialized" while §9 documents P1 and P2 artifacts exist. |
| S-5 | plan §3 | Summary table compresses falsifiers (H-CONT omits falsifier (b); H-UNIT omits the symplecticity-defect falsifier) — summary-level, no contradiction with the cards doc. |
| S-6 | outline §7 | PW imported-vs-derived boundary stated but should be sharpened at P6 (which PW machinery is imported vs derived by the finite-distinction clock). |
| S-7 | plan §2/§9 | P6 WATCH ITEM (prior SOFT-3): the frozen §2 core claim retains "continuum is unphysical"; the P1 re-mapping demotes to "uncountable precision is unphysical". The paper draft MUST ship the restated claim; verify at P6. |
| S-8 | plan P0 row | Tag name written truncated ("v0.1-phase0"); canonical tag `v0.1-phase0-res021` exists on origin at 3027054 (parent-verified via ls-remote). |
| S-9 | D1 living-paper | `entropic-operational-paradigm` row has `doi:null` while docs cite 10.5281/zenodo.17687207 — D1 backfill needed (data-quality; does not affect RES.021 claims). |
| S-10 | evidence §1 | UMP.010 underdetermination theorem cited but no UMP.010 DOI row (10.5281/zenodo.21979032) in the evidence file — add at P3. |
| S-11 | outline | No explicit registration of the P6 frozen-claim reconciliation obligation (present in plan §9 only). |
| S-12 | outline | No references/citation-audit marker (P3 obligation lives only in the plan phase table). |
| S-13 | outline | No P8 distribution note (R2 mirror, D1/KG, program_registry re-point). |

## Reviewer-verified positives

- All 11 load-bearing external anchors appear in the evidence file; 8 arXiv IDs
  re-verified live (titles/authors match); corpus DOIs (21120286, 21647362, 21672990)
  resolve live; RES.020 parent chain (22035210 / concept 22031551) verified.
- KG stats (8,322 nodes / 8,497 edges + label counts) match live query exactly.
- WBS codes P0–P8 unique, sequential, no gaps. Hypothesis-card falsifiers ↔ outline
  F1–F5 one-to-one consistent. UIA 15/15 with Q14 silence + Q15 seed.
- P2 falsifier-register re-check correctly logged as dated amendments (claims
  unchanged).

## Verdict

**2 HARD + 13 SOFT, zero integrity findings (no fabricated citations, no claim
inflation, no dangling external references).** Both HARDs are internal-consistency
defects in project documentation; the frozen core claim and the hypothesis cards'
claim texts are unaffected. Remediation is one edit pass at P3 start (H-1, H-2,
S-1–S-13 where cheap), with S-7 as the mandatory P6 verification item.
