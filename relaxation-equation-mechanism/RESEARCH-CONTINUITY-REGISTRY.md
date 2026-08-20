# RESEARCH-CONTINUITY-REGISTRY — QNFO.RES.018

**Project:** Measurement-Triggered Relaxation Dynamics · **Slug:** relaxation-equation-mechanism
**Maintained:** living document (update with every version bump)

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | Can a measurement-triggered relaxation dynamics (basins of attraction) be specified at the level of Reddiger's Radon–Nikodym formalism that reproduces Born statistics within ε=1e-2 on 2-level systems? | **DISCONFIRMED (2026-08-20, commit d53ba49)** — sealed simulation: all 7 configurations FAIL (max_dev=0.5 >> ε); deterministic outcome channel degenerate (p_measured ∈ {0,1}) | Closed as falsified; negative result ready for Phase 5 publication | WAS YES — now CLOSED |
| FQ2 | Does the boundary-condition reading of quantization (guitar-string axiom) make any prediction that differs from standard QM for a concrete system (e.g., quantum dot spectra)? | OPEN | Select system; compute both predictions; register (carried from RES.016) | YES |
| FQ3 | What is the exact relationship between the PQS "local realism" claim and loophole-free Bell violations? | OPEN | Literature synthesis (carried from RES.016) | PARTIAL |
| FQ4 | Can a MINIMAL STOCHASTIC EXTENSION of the sealed deterministic family (e.g., noise term on z during measurement) reproduce Born statistics within ε, and what is the minimal noise magnitude required? | OPEN — scaffolded (REG-RES018-002 draft) | Seal REG-RES018-002 (parameters+code sha256) BEFORE any run | YES |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| P1 | ~~A specified relaxation equation for the Madelung fluid reproduces single-shot measurement statistics within ε of the Born rule~~ | **CLOSED — DISCONFIRMED 2026-08-20** | Sealed harness rev.3 (5239468), verdict-input.json | Triggered: max_dev 0.5 > ε for all configs |
| P2 | Minimal stochastic extension (FQ4) reproduces Born statistics within ε with noise magnitude σ ≥ σ_min | 12 months | Sealed extension harness (REG-RES018-002) | Deviation > ε without documented mechanism, or σ_min = 0 (deterministic degenerate again) |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- FQ1: **TRIGGERED** — (a) no variant achieved max-deviation < ε over the sealed 59-state test set; the deterministic family is falsified as formulated.
- FQ2: disconfirmed if the boundary-condition prediction is identical to standard QM in every observable (no discriminating content).
- FQ3: disconfirmed if a published result shows the contextual-Kolmogorov response cannot accommodate loophole-free Bell statistics.
- FQ4: disconfirmed if the minimal stochastic extension reproduces statistics only with σ below physically meaningful thresholds, or if σ_min required for ε-tolerance violates the Wu-2013 consistency constraint.

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|:---|:-----------|:--------------|:-----|:---------|
| REG-RES018-001 | **CLOSED (DISCONFIRMED)** — deterministic measurement-triggered relaxation reproduces Born within ε=1e-2 | Triggered 2026-08-20: max_dev 0.5 across all variants | artifacts/verdict-input.json + verdict.md (committed d53ba49) | — |
| REG-RES018-002 | Minimal stochastic extension: dz/dt += σ·ξ(t) during measurement window reproduces Born within ε; report minimal σ | Deviation > ε without auxiliary mechanism; σ_min = 0 (degenerate); σ_min breaks Wu-2013 consistency | Sealed extension harness (draft scaffold in artifacts/REG-RES018-002-scaffold.md) | 2028-08-20 |

## 5. CALIBRATION REGISTER

| ID | Prediction | Strength | Status |
|:---|:-----------|:---------|:-------|
| [CHECK: 2027-08] | ≥1 external researcher cites the critique-validity rubric (RES.016 §10) | WEAK | PENDING |
| [CHECK: 2028-08] | The deterministic relaxation mechanism is either closed (done — DISCONFIRMED) or revived via stochastic extension with a published verdict | STRONG | **PARTIALLY RESOLVED (deterministic branch closed)** |
| [CHECK: 2028-08] | REG-RES018-002 run completed with a published PASS/FAIL verdict | STRONG | PENDING |

## 6. NEXT ACTIONS (Prioritized)

| Prio | Action | Dependency | Target |
|:-----|:-------|:-----------|:-------|
| P0 | Publish the negative result (Phase 5): paper "A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation" — Zenodo + R2 + D1/KG/Vectorize | Verdict committed (done) | CMD PUBLISH |
| P0 | Seal REG-RES018-002 (stochastic extension): finalize harness + sha256 BEFORE any run | Scaffold committed | CMD RESEARCH/CONTINUE |
| P1 | Run REG-RES018-002 → verdict (PASS/FAIL + σ_min report) | Seal | Next cycle |
| P2 | Post-publication adversarial analysis of the negative-result paper | Publication | Publish-then-audit |

## 7. SESSION LOG

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-19 | TLJWSUQav9HeprbIXtVqT | Phase 0–3 (init, UIA, due diligence, kill-question, literature, citations) |
| 2026-08-19/20 | TLJWSUQav9HeprbIXtVqT | Phase 4 sealed (rev.1→rev.2→rev.3 with 2 documented pre-results amendments) + Phase 4b verdict: **CC-1 DISCONFIRMED** (d53ba49) |

**MAINTENANCE PROTOCOL:** update FQ/prediction/register status at every version bump; cross-ref companion DOIs when published; keep living (repo unarchived).
