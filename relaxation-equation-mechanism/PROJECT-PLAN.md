# WBS: QNFO.RES.018

# Measurement-Triggered Relaxation Dynamics: A Falsifiable Mechanism Test for the Hydrodynamic Re-Grounding of Quantum Mechanics

**Slug:** `relaxation-equation-mechanism` — **Branch:** `res/paper/relaxation-equation-mechanism` — **Repo:** QNFO/qnfo-research
**Status:** Phase 0 (Init) — **Date:** 2026-08-19 — **Escalation:** FQ1 / REG-RES016-001 from QNFO.RES.016

---

## 1. Charter

QNFO.RES.016 ("Five Objections, One Standard", DOI 10.5281/zenodo.22010489) adjudicated a
five-point critique of the Post-Quantum Synthesis (PQS) / Hydrodynamic Stability Hypothesis (HSH)
program. Its pass-1 and pass-2 adversarial audits both confirmed objection 2 — **the missing
measurement mechanism** — as the framework's one substantive weakness: the HSH paper itself
concedes (§1.6) that there is "no detailed description of how the continuous probability fluid
'clumps' or relaxes into the discrete eigenstate configurations during the strong interaction with
a measuring apparatus." The adjudication registered this as frontier question FQ1 with
pre-registration scaffold REG-RES016-001 (deadline 2027-08-19, ε=1e-2 on 2-level systems).

**This project escalates FQ1 into a standalone, falsifiable computational test.** It specifies a
candidate measurement-triggered relaxation dynamics (basins of attraction) at the level of
Reddiger's Radon–Nikodym formalism, pre-registers the parameterization, and runs a simulation
whose verdict — Born statistics reproduced within tolerance, or not — is published either way.

## 2. Core Claim (P6 — LOCKED)

> **CC-1:** A measurement-triggered relaxation dynamics (basins of attraction) can be specified at
> the level of Reddiger's Radon–Nikodym formalism such that, in a pre-registered simulation of
> 2-level systems (1e5 shots, tolerance ε = 1e-2 against the Born rule), the measured outcome
> statistics reproduce the Born probabilities within ε, while the same dynamics family remains
> consistent with the strong-field hydrodynamic reproductions of Wu, Augstein, and Figueira de
> Morisson Faria (2013).

**Disconfirmation condition:** CC-1 is disconfirmed if (a) no candidate relaxation equation can be
specified at the Radon–Nikodym level consistent with the Kolmogorovian ontology, OR (b) the
pre-registered simulation deviates beyond ε = 1e-2 without a documented auxiliary mechanism, OR
(c) the required attraction-term parameterization has more free parameters than independent
constraints (KIF-60 overfitting trap).

**SO-WHAT:** The reader should care because RES.016 established that the mechanism gap is the
single confirmed objection to the hydrodynamic re-grounding of quantum mechanics. This project
converts that weakness into a binary, pre-registered computational verdict: either the
basins-of-attraction relaxation is specifiable and reproduces the Born rule within tolerance, or
the strongest objection stands. Either outcome is publishable knowledge about the framework's
viability — no third option, no goalpost moving.

**Premise-depth disclosure:** This project's derived claims rest on three named imported inputs:
(i) Reddiger's geometric quantum theory (2017; 2026) — the Radon–Nikodym local-random-variable
formalism that anchors the Kolmogorovian ontology; (ii) the strong-field hydrodynamic reproductions
of Wu et al. (2013) — the empirical constraint the dynamics family must remain consistent with;
(iii) the PQS/HSH primary texts as adjudicated in RES.016 (DOI 10.5281/zenodo.22010489), which
define the claim being tested. Where the premises END: at the pre-registered simulation's
statistical tolerance. This project does not claim PQS is correct; it tests whether the mechanism
gap can be closed with a specified equation. A deviation beyond ε falsifies CC-1 regardless of the
framework's other merits.

## 3. Phases with WBS

| WBS | Phase | Deliverable | Gate |
|:----|:------|:------------|:-----|
| QNFO.RES.018.P0 | Init (this file) | Branch, PROJECT-PLAN.md, locked CC-1, registry row, tag | P1–P8 HARD pre-flight |
| QNFO.RES.018.P0.5 | ZENODO-INQUIRY-1 | Universal Ignorance Audit (15 Q) on CC-1 | UIA administered, answers written |
| QNFO.RES.018.P1 | Due diligence | Reddiger formalism deep-dive + GRW/CSL constraint set (Bassi–Ghirardi 2003) + Wu et al. 2013 data anchors | DUE-DILIGENCE-DEPTH-1; evidence files |
| QNFO.RES.018.P1b | Consilience gate | Cross-domain lexicon (measure theory × hydrodynamic QM × collapse models) + KIF-60 | KIF-29/KIF-60 PASS |
| QNFO.RES.018.P2 | Literature | 8-source triage + KIF-18 symmetry | Both symmetry sections |
| QNFO.RES.018.P3 | Citations | references.bib verified live | P3.AUTHOR-GATE-EVERY-ENTRY-1 |
| QNFO.RES.018.P4 | Deep research | Candidate relaxation equation + simulation harness + **pre-registration record (parameters + code committed BEFORE run)** | KIF-60 pre-registration HARD |
| QNFO.RES.018.P4b | Verdict | Simulation run → pass/fail vs ε; verdict written with evidence either way | BP-1..BP-10 numeric gates |
| QNFO.RES.018.P5 | Publication | `<slug>.md/.html/.pdf` + Zenodo + full source set | PUBLICATION-SOURCE-COMPLETENESS-1; P5.FRESH |
| QNFO.RES.018.P6 | Deploy | D1 insert + KG node + Vectorize | PUBLICATION-KG-INDEX-GAP-1 |
| QNFO.RES.018.P7 | Disseminate | Buffer/communities/IA + outreach-log (no email per mandate) | Phase 7 protocol |
| QNFO.RES.018.P8 | Distribute | R2 mirror qnfo-releases + closeout | R2-MIRROR-AFTER-PUBLISH-1 |

## 4. Milestones with gate criteria

| # | Milestone | Gate criteria |
|:--|:----------|:--------------|
| M0 | Phase 0 complete | P1–P8 pass; branch pushed; tag verified; registry row RES.018 live |
| M1 | Mechanism specified | Candidate relaxation equation written at Radon–Nikodym level; consistency argument vs Reddiger formalism; Bassi–Ghirardi constraint table |
| M2 | Pre-registration sealed | Parameterization + simulation code committed with sha256 BEFORE first run; 0 free parameters beyond constraints (KIF-60) |
| M3 | Verdict produced | Simulation complete; result vs ε reported; disconfirmation handled as success-of-test |
| M4 | Publication + distribution | Zenodo DOI live, R2 mirror, D1/KG/Vectorize, post-publication adversarial analysis |

## 5. Deliverable Registry

| ID | Deliverable | Path | Status |
|:---|:------------|:-----|:-------|
| D1 | PROJECT-PLAN.md (this file) | relaxation-equation-mechanism/PROJECT-PLAN.md | ✅ P0 |
| D2 | UIA administration record | artifacts/universal-ignorance-audit.md | P0.5 |
| D3 | Due-diligence evidence files | artifacts/external-search/ | P1 |
| D4 | Simulation harness | notebooks/relaxation_sim.py | P4 |
| D5 | Pre-registration record (sha256, timestamped) | artifacts/pre-registration.md | P4 (HARD gate) |
| D6 | Verdict record (pass/fail + evidence) | artifacts/verdict.md | P4b |
| D7 | Paper `<slug>.md/.html/.pdf` | releases/ | P5 |
| D8 | references.bib + citation-audit.md | references/ + artifacts/ | P3 |
| D9 | RESEARCH-CONTINUITY-REGISTRY.md | project root | P4 |
| D10 | Outreach log | artifacts/outreach-log.md | P7 |

## 6. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Reddiger formalism insufficiently specified for a concrete equation | Medium | High | P1 deep-dive into 2017/2026 papers; fallback parameterization anchored to Bassi–Ghirardi GRW/CSL family |
| Attraction term overfits Born statistics | High | High | KIF-60: parameterization pre-registered BEFORE run; degrees-of-freedom ≤ independent-constraints check; holdout data |
| Simulation shows deviation > ε | Medium | None (by design) | That IS the verdict — CC-1 disconfirmed, published as a legitimate result (not a failure) |
| WBS collision with concurrent session | Low | High | Atomic check-then-insert (done — RES.018 verified unique) |
| Reuse of RES.016 evidence files without re-verification | Medium | Medium | Fresh live verification in P1; RES.016 files cited as provenance, not as this project's evidence |

## 7. Success Criteria

1. CC-1 adjudicated: candidate equation specified at Radon–Nikodym level, pre-registration sealed before run, simulation verdict published with evidence — pass or fail.
2. Every numeric claim traceable to the simulation output + evidence files (BP-1..BP-10).
3. Zero fabricated references (P3.AUTHOR-GATE-EVERY-ENTRY-1 — every entry live-verified).
4. Publication reaches Zenodo + R2 + D1/KG/Vectorize with full source set.
5. Post-publication adversarial analysis dispatched and findings logged (publish-then-audit).

## 8. Practitioner Relevance (PRACTITIONER-RELEVANCE-1)

**What can a practitioner DO with this result?** A runnable, pre-registered falsification harness
for any "relaxation-into-eigenstates" mechanism proposal: (1) the candidate equation family is
exposed as a parameterized Python simulation (`notebooks/relaxation_sim.py`) with a fixed
2-level-system test protocol (1e5 shots, ε=1e-2 vs Born rule); (2) the pre-registration record
(package-versioned, sha256-sealed) lets any practitioner audit that the parameters were fixed
before the data was seen — no post-hoc fitting possible; (3) the verdict record returns a binary
PASS/FAIL with full statistics, directly usable as a due-diligence input for evaluating
hydrodynamic/relaxation-based quantum foundations claims (e.g., by grant reviewers, patent
examiners screening PQS-adjacent disclosures, or QNFO's own pipeline); (4) the harness pattern
transfers to any mechanism proposal — swap the dynamics family, keep the test protocol.

---

## Appendix: provenance

- Escalated from QNFO.RES.016 FQ1 / REG-RES016-001 (RESEARCH-CONTINUITY-REGISTRY.md, DOI 10.5281/zenodo.22010489).
- Seed inputs: HSH §1.6–1.7 primary text; Reddiger 2017/2026; Wu et al. 2013; Bassi–Ghirardi 2003; RES.016 pass-1/pass-2 audit reports.
