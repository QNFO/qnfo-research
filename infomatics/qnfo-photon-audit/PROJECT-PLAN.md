# Project Plan & Work Breakdown Structure (WBS)

**Project:** Photonic Substrate Hypotheses for Emergent Spacetime — Technical Audit  
**Repository:** `qnfo-photon-audit`  
**Date:** 2026-07-18  
**Status:** Phase 1 — Literature Synthesis (Active) — H1-H4 lit reviews ✅, spin-statistics ✅  
**Methodology:** Falsifiability-first, pre-registration-governed, bin-classified

---

## 1. Project Charter

### 1.1 Mission

Produce a definitive, defensible technical audit of the claim cluster that photons constitute a pre-geometric information substrate — mapping exactly where rigorous peer-reviewed physics ends and rhetorical extrapolation begins. The audit uses a pre-registration rule (parameter-sparse predictions locked before comparison) and a bin classification system (A: testable now, B: needs theory first, C: not falsifiable as posed) to evaluate five sub-hypotheses.

### 1.2 Reformulated Core Claim

> The informational properties of quantum fields suggest that geometric spacetime may be emergent in some quantum gravity frameworks — and photons, as the only freely-propagating massless boson with a natural two-state (qubit) polarization structure, are the natural elementary information carriers in such a substrate.

This replaces Doc A's original non-sequitur ("photons don't obey Pauli exclusion → 3D space primacy is falsified") with a logically valid, hypothesis-framed statement connected to legitimate research programs.

### 1.3 Governing Rules

1. **Pre-registration rule:** No comparison counts as a test unless the prediction's functional form is fixed with fewer free parameters than facts to explain, and is timestamp-locked before comparison.
2. **Bin discipline:** Claims in bin C are excluded from the "tests" section and reported as open problems.
3. **Citation integrity:** Every citation traces to a real, checkable source (DOI/arXiv ID).
4. **Branch discipline:** NEVIER commit to main/master. All work on feature branches.
5. **Artifact persistence:** All documents, notebooks, and deliverables are versioned in this repository and archived to Zenodo at major milestones.

### 1.4 Success Criteria

- [ ] All 5 sub-hypotheses audited with bin assignments and evidence tags
- [ ] Curve-fitting audit appendix documents every excluded "test"
- [ ] Final verdict table with traceable citations for every [Est] tag
- [ ] "What would need to be true" section for each blocked claim
- [ ] Repository published on GitHub with full revision history
- [ ] v1.0 audit report uploaded to Zenodo with DOI

---

## 2. Project Phases

### Phase 0 — Scoping and Claim Decomposition (Week 1)

**Goal:** Establish the canonical claim set, bin assignments, and audit rubric.

| Task | ID | Description | Deliverable | Status |
|---|---|---|---|---|
| Formalize core claim | 0.1 | Lock the reformulated core claim as project charter preamble | Section 1.2 above | ✅ Complete |
| Derive bin table | 0.2 | Independently re-argue bin assignment for H1–H5 from source literature | `notebooks/phase0-bin-table.md` (confirmed vs Doc E) | ✅ Complete |
| Write audit rubric | 0.3 | Define evidence tags: [Est], [Open], [Unsup], [Blocked], [CE] | `notebooks/rubric.md` | ✅ Complete |
| Build seed bibliography | 0.4 | Annotated bibliography of ≥40 primary sources across 4 sub-literatures | `artifacts/seed-bibliography.md` (42 sources) | ✅ Complete |
| Project charter finalization | 0.5 | Freeze Phase 0 deliverables; tag as v0.1 | Git tag `v0.1-phase0` | ✅ Complete |

### Phase 1 — Literature Synthesis (Weeks 2–5)

**Goal:** Systematic review per sub-literature, bin-tagging every source.

| Task | ID | Description | Deliverable | Status |
|---|---|---|---|---|
| H1 track: EM-knot solitons + spinning solitons | 1.1 | Review Rañada, Trueba, Bouwmeester, Burinskii, Chernitskii; tag each source with bin | `artifacts/lit-review-h1.md` (17 sources, B/A/C bins, 3 gaps) | ✅ Complete |
| H2 track: Holographic entanglement + geometry | 1.2 | Review RT formula, tensor-network/MERA, causal set theory; tag domain of applicability | `artifacts/lit-review-h2.md` (24 ext + 5 int sources) | ✅ Complete |
| H3 track: Reversible computing + COTT | 1.3 | Review Bennett, Landauer, Bérut; assess COTT's claimed advantage analytically | `artifacts/lit-review-h3.md` (18 ext + 2 int sources) | ✅ Complete |
| H4 track: Adelic/p-adic QM + quantum chaos | 1.4 | Review Volovich, Vladimirov, Rydberg chaos literature; tag scale assumptions | `artifacts/lit-review-h4.md` (22 ext + 8 int sources) | ✅ Complete |
| Cross-cutting: Spin-statistics theorem | 1.5 | Compile theorem statement, assumptions, and which models (if any) circumvent it | `artifacts/spin-statistics-barrier.md` (11 sources, 4 circumvention routes) | ✅ Complete |
| Cross-cutting: H4a scale estimate | 1.6 | Quantitative estimate: Planck-scale ultrametricity → Rydberg signal magnitude | `artifacts/h4a-scale-estimate.md` (25-order bridge implausible, Bin C-) | ✅ Complete |

### Phase 1.5 — Pre-Registration Gate (Week 5–6)

**Goal:** For every B/C claim, attempt to construct a parameter-sparse, lockable prediction. Promote or formally log as untestable.

| Task | ID | Description | Deliverable | Status |
|---|---|---|---|---|
| H1 gate | 1.5.1 | Attempt g-2 correction derivation from Kerr–Newman soliton machinery; lock or log | `artifacts/h1-gate-memo.md` (H1-G1: PASS, H1-G2: BLOCKED — no KN g-2 derivation exists) | ✅ Complete |
| H2b gate | 1.5.2 | Attempt parameter-free knot→mass mapping; expected: no such mapping exists → bin C confirmed | `artifacts/h2b-gate-memo.md` (CONFIRMED BIN C — no parameter-free mapping exists) | ✅ Complete |
| H3 gate | 1.5.3 | Resolve analytically: does COTT permit any operation standard reversible logic cannot? | `artifacts/h3-gate-memo.md` (CONFIRMED BIN C — zero external COTT validation; redundant with standard reversible logic) | ✅ Complete |
| H4b gate | 1.5.4 | Survey adelic literature for independent v_p fixing principle; expected: none exists → bin C confirmed | `artifacts/h4b-gate-memo.md` (CONFIRMED BIN C — no p-fixing principle exists) | ✅ Complete |
| Gate summary | 1.5.5 | Compile all gate memos; update bin table with promotions/demotions | `artifacts/gate-summary.md` (5 gates: 1 pass, 4 blocked. 0 promotions. Bin table final.) | ✅ Complete |

### Phase 2 — Runnable Tests (Weeks 6–10)

**Goal:** Execute only bin-A claims with locked predictions. No bin B/C claims run as "tests."

| Task | ID | Description | Deliverable | Status |
|---|---|---|---|---|
| H2a test | 2.1 | Design quantized Berry phase prediction for photonic vortex soliton; compare to literature data | `artifacts/h2a-test-results.md` (INCONCLUSIVE — knot-specific Berry phase never measured; data gap) | ✅ Complete |
| H4a spectroscopy | 2.2 | Spacing-statistic analysis on existing Rydberg datasets (literature data, not new experiment) | `artifacts/h4a-test-results.md` | 🚫 Blocked (Bin C-: no p-fixing principle, metric f(k) free — no testable prediction) |
| H5 verification | 2.3 | Literature-verification of reversible logic calorimetry results near Landauer limit | `artifacts/h5-verification.md` (CONFIRMED — Landauer bound holds across 6 systems; reinforces H3 Bin C) | ✅ Complete |
| Promoted claims | 2.4 | Any claim promoted from bin B by Phase 1.5 gets its locked prediction compared to data here | Per-claim result doc | 🚫 Blocked (0 claims promoted per gate-summary.md — no work applicable) |

### Phase 3 — Synthesis and Audit Report (Weeks 10–12)

**Goal:** Compile final report with verdict table, curve-fitting audit appendix, and adversarial review.

| Task | ID | Description | Deliverable | Status |
|---|---|---|---|---|
| Verdict table | 3.1 | Final verdict table: all H1–H5 with bin, outcome, citations | `artifacts/verdict-table.md` (13 sub-hypotheses evaluated) | ✅ Complete |
| Curve-fitting audit | 3.2 | Appendix listing every excluded "test" with reason | `artifacts/curve-fitting-audit.md` (8 excluded matches, 4-point checklist) | ✅ Complete |
| Draft report v1 | 3.3 | Full technical report: abstract, methodology, per-hypothesis audit, cross-cutting issues, verdicts | `releases/audit-report-v1.0.md` (drafted, NOT yet publication-cleared — see 3.4) | ✅ Drafted |
| Adversarial review | 3.4 | Check no Phase 2 result violates pre-registration rule; re-verify all derivations | `artifacts/adversarial-review.md` — Initial verdict FAIL; v1.1 revision executed addressing all 4 MAJOR findings. Re-audit by REVIEWER subagent returned PASS. | ✅ Complete — v1.1 cleared |

### Phase 4 — External Sanity Check, Revision, and Finalization

**Goal:** Sanity-check, revise, finalize, and close out.

| Task | ID | Description | Deliverable | Status |
|---|---|---|---|---|
| Sanity check | 4.1 | Self-critique against textbook results (spin-statistics, Bennett's theorem, RT scope, Landauer bound) | `artifacts/sanity-check-v1.1.md` (PASS — no canonical physics errors found) | ✅ Complete |
| Revision v1.1 | 4.2 | Address adversarial review Findings 1–4 (H1c reconciliation, B/C boundary, H4a→Bin U, spin-statistics softening); re-run REVIEWER subagent | `releases/audit-report-v1.1.md` (222 lines, all 4 MAJOR findings resolved, re-audit PASS) | ✅ Complete |
| Publication | 4.3 | Git tag, commit all deliverables, closeout handoff | Git tag `v1.1-photon-audit`; closeout handoff; onward to Zenodo publication (deferred to post-closeout session) | ⚠️ Git tagged; Zenodo publication deferred |

---

## 3. Milestones and Gate Criteria

| Milestone | Gate Criteria | Target | Status |
|---|---|---|---|
| **M0: Project Charter** | Reformulated claim locked, bin table independently argued, bibliography seeded | Week 1 | ✅ Complete |
| **M1: Literature Complete** | All 4 sub-literatures reviewed, ≥40 sources tagged with bin and justification | Week 5 | ✅ Complete |
| **M1.5: Gate Complete** | All B/C claims gated; bin table finalized with promotions/demotions | Week 6 | ✅ Complete |
| **M2: Tests Complete** | All bin-A claims tested with locked predictions; results documented | Week 10 | ✅ Complete |
| **M3: Audit Report** | Full report with verdict table, curve-fitting appendix, adversarial review, v1.1 revision, reviewer re-audit PASS | Week 12 | ✅ Complete — v1.1 |
| **M4: Closeout** | Git tagged, sanity-checked, closeout handoff written; Zenodo publication deferred | Week 14 | ✅ Complete — v1.1 |

---

## 4. Deliverable Registry

| Deliverable | Path | Format | Zenodo | Phase |
|---|---|---|---|---|
| Project charter | `PROJECT-PLAN.md` | Markdown | v0.1 bundle | 0 |
| Audit rubric | `notebooks/rubric.md` | Markdown | v0.1 bundle | 0 |
| Seed bibliography | `artifacts/seed-bibliography.md` | Markdown | v0.1 bundle | 0 |
| Lit review — H1 | `artifacts/lit-review-h1.md` | Markdown | Phase 1 bundle | 1 |
| Lit review — H2 | `artifacts/lit-review-h2.md` | Markdown | Phase 1 bundle | 1 |
| Lit review — H3 | `artifacts/lit-review-h3.md` | Markdown | Phase 1 bundle | 1 |
| Lit review — H4 | `artifacts/lit-review-h4.md` | Markdown | Phase 1 bundle | 1 |
| Gate memos (×4) | `artifacts/h*-gate-memo.md` | Markdown | Phase 1.5 bundle | 1.5 |
| Test results (×3+) | `artifacts/h*-test-results.md` | Markdown | Phase 2 bundle | 2 |
| Final audit report | `releases/audit-report-v1.0.md` | Markdown + PDF | v1.0 with DOI | 4 |

---

## 5. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| H1 never escapes bin B (no lockable prediction exists) | High | Medium | Report honestly; this IS a valid result |
| H2b/H4b confirmed bin C (curve-fitting) | Near-certain | Low | Expected; already flagged in Doc E |
| LLM citation hallucination | Medium | High | Every citation verified against source text before inclusion |
| Timeline overrun (14 weeks → 20 weeks) | Medium | Medium | Prioritize bin-A tests first; bin B/C gate memos can parallelize |
| Spin-statistics barrier blocks H1 entirely | Medium | High | Document as [Blocked]; shifts focus to H2a (the only bin-A frontier claim) |

---

## 6. Version History

| Version | Date | Description | Git Tag |
|---|---|---|---|
| v0.1 | 2026-07-18 | Project charter + seed documents + Doc E audit | `v0.1-phase0` |
| v1.0 | 2026-07-21 | Initial audit report (FAIL at adversarial review) | — |
| v1.1 | 2026-07-21 | Revised audit report addressing all 4 MAJOR adversarial review findings; reviewer re-audit PASS; sanity-check PASS | `v1.1-photon-audit` |

---

## 7. Current Execution (Phase 4 — Closeout)

**Status:** Phase 4 closeout complete. All 4 phases and all milestones achieved.
**Next action:** Zenodo publication (deferred to post-closeout session); rubric update to add Bin U.

### Phase 4 Summary:

1. ✅ Sanity check (4.1): Verified v1.1 report against canonical textbook results — PASS, no errors found.
2. ✅ Revision v1.1 (4.2): All 4 MAJOR adversarial review findings resolved; REVIEWER re-audit PASS.
3. ✅ Git tagged (4.3): `v1.1-photon-audit` tag applied.
4. ⚠️ Zenodo publication: Deferred — requires Zenodo API authentication and artifact bundling.
5. ⚠️ Rubric update: `notebooks/rubric.md` should add Bin U category in post-v1.1 maintenance.
