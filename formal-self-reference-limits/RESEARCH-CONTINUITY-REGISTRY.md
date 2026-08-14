# Research Continuity Registry — QNFO.RES.008 Formal Self-Reference Limits

**Created:** 2026-08-14 (Phase 5 publication, v2.64 HARD protocol)
**Repository:** QNFO/qnfo-research, branch res/paper/formal-self-reference-limits
**Status:** LIVE — maintained with version bumps

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | Can the self-knowledge bound of a formal system be characterized uniformly (Gödel-numbering style) across logic, computation, and measurement as a single invariant — a "blind-spot invariant" analogous to depth in prime valuation? | OPEN (paper §7) | Formalize candidate invariant; test on logic/computation/measurement triples | YES |
| FQ2 | Does the objectification thesis predict a measurable signature in AI self-modeling systems (e.g., LLM self-report limits) beyond Gödelian bounds? | OPEN | Literature + experiment design | YES |
| FQ3 | Is the convention-layer/non-invariance claim (C1) generalizable from bases/units to coordinates, gauges, and reference frames? | OPEN | Extend radix-agnostic protocol to gauge redundancy | PARTIAL |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| P1 | No consistent recursively axiomatizable formal system can define its own truth predicate and prove all its own true statements (equivalently: no such system exists). | Standing (classical) | Literature/formal proof search | Exhibit such a system — contradicts Tarski/Gödel (paper §9.1) |
| P2 | No anthropocentric convention change alters a formal theorem rather than its representation; in particular, no physical radix is privileged. | Standing | Radix-agnostic DSI protocol on new datasets (Planck null is evidence) | Exhibit base-dependent arithmetic theorem (paper §9.2) |
| P3 | Any observer-as-node framework in ultrametric/relational quantum foundations retains a residual external perspective (global topology not locally computable). | 2026-2027 | S10-observer extensions | Framework with fully local, external-free self-location |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- FQ1: disconfirmed if a formal system's self-knowledge bound is shown to be *not* uniform across logic/computation/measurement (e.g., measurement case differs from logical case).
- FQ2: disconfirmed if an AI system exhibits complete, consistent self-reporting with no Gödelian-style blind spot in a sufficiently expressive formal language.
- FQ3: disconfirmed if a convention change (coordinates/gauges) alters a theorem rather than representation.

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|:---|:-----------|:--------------|:-----|:---------|
| REG-RES008-001 | Blind-spot invariant exists and is computable for PA-like systems | Construct PA fragment with computable full self-knowledge | Formalization + proof script | 2027-06 |
| REG-RES008-002 | Radix-agnostic DSI null replicates on CMB-S4 | Certified DSI detection with pre-registered tolerance | CMB-S4 public maps | On data release |

## 5. CALIBRATION REGISTER

| Date | Prediction | Strength | Result | Notes |
|:-----|:-----------|:---------|:-------|:------|
| [CHECK: 2026-08-14] | P1 (Tarski/Gödel stability) | HIGH (theorem-grade) | SUPPORTED (standing) | Classical; extended by Savelyev/Visser |
| [CHECK: 2026-08-14] | P2 (radix silence) | MEDIUM-HIGH | SUPPORTED (Planck 2018 null, silent-radix theorem) | Evidence at 10.5281/zenodo.21902891, 10.5281/zenodo.21046734 |
| [CHECK: 2026-08-14] | P3 (residual external perspective) | MEDIUM | SUPPORTED (S10 verdict) | Evidence at 10.5281/zenodo.21473899 |

## 6. NEXT ACTIONS (PRIORITIZED)

| Priority | Action | Dependency | Target |
|:---------|:-------|:-----------|:-------|
| P0 | Complete Phase 5 publication (Zenodo deposit + D1 + Vectorize + KG + R2) | This branch | 2026-08-14 |
| P1 | Formalize blind-spot invariant candidate (FQ1) | Post-publication | 2026-Q4 |
| P2 | Monitor S10-observer extension literature (P3) | None | Monthly |

## 7. SESSION LOG + MAINTENANCE

- **2026-08-14:** Registry created at Phase 5 (publication pipeline). FQ1-3, P1-3, REG-001/002, calibration register seeded. Maintain with every version bump of the paper; re-check calibration entries on [CHECK] dates.
- Maintenance protocol: on any paper revision, update FQs/predictions affected; on any external corroboration/refutation, update calibration register with evidence link.
