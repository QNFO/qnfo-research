# WBS: QNFO.RES.012

# PROJECT-PLAN: The Purpose Principle — Grounding Research in Reality, Utility, and Premise-Depth

**Status:** Phase 0 (Initialization) · **Branch:** `res/paper/research-purpose-utility` · **Date:** 2026-08-16
**Program:** QNFO.RES (QNFO Research Archive) → `QNFO/qnfo-research` (REPO-TARGET GATE verified: origin = qnfo-research.git)
**Author:** DeepChat agent (user editorial directive 2026-08-16)

---

## 0. Standing Governance Gates — PASSED IN WRITING (BEFORE Phase 0)

Per the 2026-08-16 global mandate, every new research thread must pass these gates in writing before Phase 0. This paper is ABOUT the gate, so it applies the gate to itself (epistemic legibility — the last unexamined scaffold is the one doing the examining).

### G1. So-What Gate — why a reader/funder/investor/fellow researcher should care (one sentence a non-specialist can parse)

> **"Billions of dollars, careers, and compute-hours are spent on research whose connection to any human problem is untraceable — this paper proposes and defends a testable *grounding criterion* (a research program must exhibit a live path from its questions to real-world utility and must declare where its premises end) that researchers, funders, and self-auditing AI pipelines can use to decide what deserves to be advanced, without requiring every result to be immediately useful."**

### G2. Depth-of-Premises Test — where do the premises END?

The paper's claims are normative-epistemic, not mathematical. The premise chain:

- **L0 (unanalyzable value primitive):** real-world utility is a legitimate first-order criterion for allocating research effort. This is a normative axiom — NOT derived, NOT claimed as a theorem.
- **L1 (empirical premise, named input):** academic discipline-membership, abstraction level, and knowledge silos causally produce low-traceable-utility research at scale (the "mathematician who only researches abstract mathematics" pattern). FALSIFIABLE via traceable-impact audits (G3).
- **L2 (epistemic premise, named input):** declaring where premises end (derived vs. unanalyzable primitives / named imported inputs) increases testability, accountability, and the credibility of novelty claims. FALSIFIABLE via the meta-test in G3.
- **L3 (derived):** the grounding criterion (G1-G3 of the paper), its application procedure, and the anti-pattern taxonomy (silo-lock, abstraction-for-its-own-sake, utility-deferral-without-path, premise-concealment).
- **L4 (derived, bounded):** the criterion's program-level (not per-result) scope; exploratory research remains valuable iff it keeps an OPEN grounding path.

**Claimed depth:** the paper is as deep as L0-L2 — two named inputs and one value primitive. It does NOT claim to derive utility-maximization from first principles, and it explicitly does NOT claim that all abstraction is bad (only abstraction whose grounding path is closed or untraceable).

### G3. Falsification Condition

- **F1 (causal premise):** if a traceable-impact audit of siloed, abstraction-only research programs finds real-world utility produced at rates statistically indistinguishable from grounded programs, L1 fails.
- **F2 (epistemic premise):** if requiring premise-depth disclosure systematically reduces research output quality or downstream utility (measurable disutility), L2 fails.
- **F3 (meta-test / self-siloing):** if applying the grounding criterion to the criterion itself reduces total utility (e.g., it becomes a checklist ritual that crowds out exploratory research), the criterion is self-refuting and must be revised or withdrawn.

**Anti-pattern blocked (explicitly):** long chains of deflationary analysis notes concluding only "boundary remains external" with no reader-facing payoff. This paper's payoff = a usable criterion + a falsifiable causal claim + an implementation procedure for research pipelines (human and AI).

### ZENODO-INQUIRY-1: Universal Ignorance Audit (Phase-0 application, abbreviated)

Records applied: UIA 10.5281/zenodo.21901984 + IAPS 10.5281/zenodo.21901983 (v0.3, canonical — never the superseded 21878943/21878977).

- **Phases 1-2 (declare what is known/assumed):** the gates above are written; assumptions enumerated (L0-L2).
- **Phases 3-4 (declare what is NOT known):** (i) no established metric for "real-world utility traceability" exists — the paper must propose one, not assume one; (ii) the empirical base for L1 is anecdotal + case-based, not a controlled corpus study — the paper must say so; (iii) the interaction of the criterion with AI-assisted pipelines (which can generate silo-fodder at scale) is under-theorized — a contribution opportunity.
- **Phase 5 (recursive meta-question):** "What if the grounding criterion is wrong about everything?" → F3 (self-siloing) is the standing disconfirmation route; the paper invites adversarial validation.

---

## 1. Charter

### 1.1 Problem

The research ecosystem allocates enormous resources to work whose connection to real-world utility is untraceable. Disciplinary silos reward abstraction-for-its-own-sake; novelty claims are routinely unbounded by the depth of their premises; and AI-assisted pipelines can now generate silo-fodder at arbitrary scale, amplifying the failure mode. The user's editorial mandate (2026-08-16) states the need: research must have purpose and real-world utility (conceptual, not-yet-realized utility counts); pure theory without a practical application is effectively useless; and a theory/theorem is only as deep as its premises.

### 1.2 Core Claim (LOCKED — P6)

> **A research program's claim to advancement should be evaluated by a grounding criterion: (G1) it must exhibit a live, non-vacuous path from its questions to real-world utility (practical application, decision-relevant knowledge, or a concrete artifact), with the path traceable and the utility asserted in falsifiable form; (G2) it must declare where its premises end (derived claims vs. unanalyzable primitives or named imported inputs); and (G3) it must not derive legitimacy solely from membership in an academic discipline, abstraction level, or knowledge silo. Exploratory research remains valuable iff it maintains an open grounding path (a stated candidate route to utility). The criterion is program-level and directional, not per-result.**

Locked 2026-08-16 (Phase 0). Any reformulation requires a new P6 gate.

### 1.3 Contribution

1. **A usable, non-tautological criterion** (the grounding test) with a concrete application procedure — not a slogan.
2. **A falsifiable causal claim** (L1) with a specified audit design (traceable-impact audit) — not a rhetorical preference.
3. **An anti-pattern taxonomy** for research programs and AI pipelines (silo-lock, abstraction-for-its-own-sake, utility-deferral-without-path, premise-concealment).
4. **A premise-depth disclosure standard** usable at publication time (extends SO-WHAT-GATE-1 / research v2.114 with the "how deep does the theory go" question operationalized as L0-Ln chains).
5. **An implementation procedure** for research pipelines (Phase 0 gate: grounding declaration + premise-depth chain + falsification condition) — immediately usable by QNFO and by external self-auditing pipelines.

---

## 2. Phases with WBS

| Phase | WBS | Deliverable | Gate |
|:------|:----|:------------|:-----|
| P0 Init | QNFO.RES.012.P0 | Branch, PROJECT-PLAN.md, core-claim.md, commit/tag/push | HARD: gates G1-G3 written + core claim locked |
| P1 Due Diligence | QNFO.RES.012.P1 | DUE-DILIGENCE-DEPTH-1 full-corpus sweep + external verification + gap analysis | HARD: gap analysis with premise-chain depth |
| P2 Literature | QNFO.RES.012.P2 | 8 parallel sources, dedup, classify (KIF-18) | HARD: P2 gate |
| P3 Citations | QNFO.RES.012.P3 | references.bib, AUTHOR-GATE live verification | HARD: P3.AUTHOR-GATE |
| P4 Research | QNFO.RES.012.P4 | Full draft: criterion, audit design, taxonomy, implementation | HARD: BP gates + red-team |
| P5 Publication | QNFO.RES.012.P5 | paper.md/html/pdf (pandoc→MathJax→CDP), BP-1..BP-10, SO-WHAT-GATE-1 | HARD: PANDOC-SAFE + BP-1/2 |
| P6 Deploy | QNFO.RES.012.P6 | Zenodo deposit (ALL source files), D1 living-paper, papers server | HARD: live DOI + R2 mirror |
| P7 Disseminate | QNFO.RES.012.P7 | Social posts (SO-WHAT-GATE-1), SEO, IA snapshot | SOFT |
| P8 Distribute | QNFO.RES.012.P8 | GitHub tag, Zenodo newversion, R2 archive, KG records | HARD: R2-MIRROR-AFTER-PUBLISH-1 |

## 3. Milestones with Gate Criteria

1. **M0 (P0):** scaffold committed on `res/paper/research-purpose-utility`; gates G1-G3 in writing; core claim locked. — DONE THIS SESSION.
2. **M1 (P1):** due-diligence evidence file (`artifacts/external-search/`) with >=3 query formulations per topic, cross-system ID validation, >=2 adjacent WBS domains (RES + CFE + SLB), external verification (arXiv/OpenAlex/Crossref); gap analysis states premise-chain depth.
3. **M2 (P2-P3):** literature classified; every citation AUTHOR-GATE verified.
4. **M3 (P4):** full draft passes BP-1..BP-10 + red-team (Accuracy/Completeness/Dependency).
5. **M4 (P5-P6):** published to Zenodo with ALL source files (PUBLICATION-SOURCE-COMPLETENESS-1); DOI live (DataCite 200); R2 mirror qnfo-releases; KG distribution_status=distributed.
6. **M5 (P7-P8):** dissemination complete; newversion + tag; post-publication adversarial analysis (mandatory).

## 4. Deliverable Registry

| Deliverable | Path | Status |
|:------------|:-----|:-------|
| PROJECT-PLAN.md | `research-purpose-utility/PROJECT-PLAN.md` | DONE |
| Core claim (locked) | `research-purpose-utility/docs/core-claim.md` | DONE |
| Due-diligence evidence | `research-purpose-utility/artifacts/external-search/` | PENDING (P1) |
| Gap analysis | `research-purpose-utility/artifacts/gap-analysis.md` | PENDING (P1) |
| Consilience gate | `research-purpose-utility/artifacts/consilience-gate.md` | PENDING (P2) |
| references.bib + citation-audit.md | `research-purpose-utility/` | PENDING (P3) |
| paper.md/html/pdf + README | `research-purpose-utility/releases/` | PENDING (P5) |
| Zenodo deposit + R2 mirror | external | PENDING (P6) |

## 5. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Criterion judged tautological ("all research is useful eventually") | MED | HIGH | Falsifiable L1 + audit design + "non-vacuous path" operationalization |
| Silo-defense backlash (disciplinary gatekeepers) | HIGH | LOW | No-journal stance (NO-JOURNALS-1); Zenodo-first; tone = proposal not attack |
| Paper becomes the anti-pattern it describes (pure abstraction) | MED | HIGH | Meta-test F3; every section carries a reader-facing payoff |
| Corpus self-reference (QNFO papers as the only examples) | MED | MED | External verification (arXiv/OpenAlex) + at least 2 non-QNFO case families |
| Concurrent WBS collision | LOW | HIGH | RES.012 claimed atomically via branch creation this session |

## 6. Success Criteria

1. A reader who is not a philosopher can state the criterion in one sentence and apply it to a research program in <10 minutes.
2. A hostile reviewer cannot dismiss the causal claim as unfalsifiable (F1-F3 are concrete).
3. The premise-depth disclosure standard is directly usable at publication time (extends SO-WHAT-GATE-1).
4. The paper itself passes its own criterion (a live grounding path exists: decision-relevant guidance for funders/researchers/pipelines).
5. Post-publication adversarial analysis surfaces 0 HARD findings (or all remediated before P8).

---

## 7. Phase 0 Checklist (this session)

- [x] WBS resolve: **QNFO.RES.012** (git log confirms RES.011 last claimed; RES.012 unclaimed; D1 program_registry INSERT deferred to next D1-capable session per WBS-REGISTRY-STALE-1 CHECK-THEN-WRITE)
- [x] Branch `res/paper/research-purpose-utility` created (atomic claim)
- [x] Scaffold docs/ artifacts/ notebooks/ releases/
- [x] PROJECT-PLAN.md (this file, first line WBS code)
- [x] Gates G1-G3 IN WRITING (section 0)
- [x] Core claim locked (docs/core-claim.md)
- [ ] Commit + tag + push (pending — same session)
