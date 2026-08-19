# RESEARCH-CONTINUITY-REGISTRY — QNFO.RES.016

**Project:** Post-Quantum Synthesis Critique Adjudication · **Slug:** pqs-critique-adjudication
**Maintained:** living document (update with every version bump)

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | Can a measurement-triggered relaxation dynamics (basins of attraction) be specified at the level of Reddiger's Radon–Nikodym formalism while preserving the quantitative strong-field reproductions already achieved by hydrodynamic trajectories (Wu et al. 2013: HHG spectra)? | OPEN | Derive candidate relaxation equation; compare with Bassi–Ghirardi dynamical-reduction constraints | YES (simulation pre-reg) |
| FQ2 | Does the boundary-condition reading of quantization (guitar-string axiom) make any prediction that differs from standard QM for a concrete system (e.g., quantum dot spectra)? | OPEN | Select system; compute both predictions; register | YES |
| FQ3 | What is the exact relationship between the PQS "local realism" claim and loophole-free Bell violations (Hensen et al. 2015)? | OPEN | Literature synthesis on contextual-Kolmogorov responses | PARTIAL (logic, not experiment) |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| P1 | A specified relaxation equation for the Madelung fluid reproduces single-shot measurement statistics within tolerance ε of the Born rule | 24 months | Simulation vs. weak-measurement datasets (superconducting circuits, Hacohen-Gourgy & Martin lineage) | Distribution deviates beyond ε without a documented auxiliary mechanism |
| P2 | The critique-validity rubric (Section 10 of the paper) applied by two independent evaluators to the same 10-objection set yields agreement on ≥8 of 10 grades | 12 months | Inter-rater audit | Agreement < 8/10 (rubric not operational) |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- FQ1 disconfirmed if: no relaxation equation consistent with both the Kolmogorovian ontology and measured statistics is produced within the window.
- FQ2 disconfirmed if: for the chosen system, the boundary-condition prediction is identical to standard QM in every observable (no discriminating content).
- FQ3 disconfirmed if: a published result shows the contextual-Kolmogorov response cannot accommodate loophole-free Bell statistics.

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|:---|:-----------|:--------------|:-----|:---------|
| REG-RES016-001 | Basins-of-attraction relaxation with radial-basis attraction term recovers Born statistics on 2-level systems within ε=1e-2 | Hit-rate deviation > 1e-2 on 1e5 simulated shots | Synthetic trajectory simulation (public repo) | 2027-08-19 |
| REG-RES016-002 | Critique-rubric inter-rater agreement ≥ 0.8 | Agreement < 0.8 | 10-objection audit by 2 independent raters | 2027-08-19 |

## 5. CALIBRATION REGISTER

| ID | Prediction | Strength | Status |
|:---|:-----------|:---------|:-------|
| [CHECK: 2027-08] | ≥1 external researcher cites the critique-rubric (Section 10) independently of PQS | WEAK | PENDING |
| [CHECK: 2028-08] | The mechanism gap (objection 2) is either closed by a specified equation or explicitly abandoned in a PQS revision | STRONG | PENDING |

## 6. NEXT ACTIONS (Prioritized)

| Prio | Action | Dependency | Target |
|:-----|:-------|:-----------|:-------|
| P0 | User review of draft v0.1 (plain-prose gate) | Draft committed | Next session |
| P0 | Phase 5 publication: pandoc → MathJax SVG → CDP PDF; Zenodo deposit with full source set | Draft approved | CMD PUBLISH |
| P1 | Phase 6: D1 insert + KG node + Vectorize index | P5 | Post-publish |
| P1 | R2 mirror to qnfo-releases + distribution_status | P5 | Post-publish |
| P2 | Post-publication adversarial analysis (Accuracy/Completeness/Dependency) | P5 | Publish-then-audit |

## 7. SESSION LOG

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-19 | TLJWSUQav9HeprbIXtVqT | Phase 0–1b (init, UIA, due diligence, consilience) |
| 2026-08-19 | TLJWSUQav9HeprbIXtVqT | Phase 2–4 (literature, citations, adjudication draft v0.1) |

**MAINTENANCE PROTOCOL:** update FQ/prediction/register status at every version bump; cross-ref companion DOIs when published; keep living (repo unarchived).
