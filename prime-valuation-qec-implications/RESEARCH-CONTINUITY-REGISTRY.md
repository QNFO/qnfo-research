# RESEARCH-CONTINUITY-REGISTRY — QNFO.RES.006

**Project:** Implications for Computing and Quantum Error Correction
**Slug:** prime-valuation-qec-implications
**DOI:** 10.5281/zenodo.21922813 (v0.2)
**Maintained:** 2026-08-13 — living document (v2.64 protocol)

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | Does there exist a non-trivial valuation invariant of stabilizer codes (≠ v₂(dim H), v₂(dim H_L)) with classification or predictive power? | OPEN | Resolve NTOF under-specification; re-implement Algorithm 4.4; fresh 50/family generation | YES (REG-RES006-001) |
| FQ2 | Is the QEC overhead (physical:logical qubits) bounded below by a valuation-structure function, and how does it compare to the quantum Singleton bound? | UNTESTED | Derive candidate bound; compare to Singleton; red-team | YES |
| FQ3 | Is there a valuation-based complexity characterization of reversible/Clifford computation that differs from (or tightens) the standard one? | PROMISSORY | Define the characterization; test on concrete tasks | YES |
| FQ4 | Does the no-cloning re-expression (non-cloneable redundancy) yield a checkable consequence for QEC limits beyond the standard no-cloning statement? | RISK-HIGH | Identify one consequence; test | YES |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition | Status |
|:---|:-----------|:------------|:-----------|:--------------------------|:-------|
| P1 | The naive [[n,k,d]]→branch-depth mapping (n,k) carries no new content | 2026-08 (done) | Definitional analysis (§3) | Claimed extra content beyond relabeling | CONFIRMED (self-corrected) |
| P2 | C7.3' Mahler spectral separation (v_p^max optimal≈28 vs random≈4, gap≥10) reproduces | 2026-08-13 (attempted) | rq3-mahler-reproduction.py, 55 codes | gap ≥ 10 at n ≤ 18 | **NOT REPRODUCED** (optimal 4, random 3/6) |
| P3 | 83% Kodaira–Néron classifier accuracy reproduces above a stated baseline | P4 (next cycle) | REG-RES006-001 re-implementation | fails to exceed baseline by pre-registered margin | UNVERIFIED-INTERNAL |
| P4 | A valuation-based overhead bound is tighter than the Singleton bound | P4-P5 | derivation + code-family scan | bound weaker than/equal to Singleton | UNTESTED |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- **RQ1 (FQ1):** disconfirmed if no non-trivial valuation invariant is found after the re-implementation and fresh generation.
- **RQ2 (FQ2):** disconfirmed if the overhead bound is not tighter than or equivalent to the quantum Singleton bound.
- **RQ3 (FQ3):** disconfirmed if no valuation-based complexity characterization is produced.
- **RQ4 (FQ4):** disconfirmed if the no-cloning re-expression yields no new checkable consequence.
- **RQ5 (C8):** disconfirmed if independent reproduction fails to exceed baseline by pre-registered margin.

## 4. PRE-REGISTRATION SCAFFOLDS

### REG-RES006-001 — 83% classifier reproduction (BLOCKED — under-specification)
- **Hypothesis:** Algorithm 4.4 (Kodaira–Néron fiber classifier) assigns code families at 83% accuracy on fresh generation.
- **Falsification:** observed accuracy ≤ majority-class baseline + margin.
- **Data:** 50 codes/family × 4 families (surface, CSS, optimal, random), seeded generation protocol, fresh splits.
- **Deadline:** next P4 cycle.
- **BLOCKERS:** Mahler target function undefined in NTOF; Cox-ring ideal I_C unspecified. Resolution required from source author.

## 5. CALIBRATION REGISTER

| Date | Prediction | Strength | Outcome |
|:-----|:-----------|:---------|:--------|
| 2026-08-13 | C2/C3 relabeling finding | strong (definitional) | CONFIRMED |
| 2026-08-13 | P2 Mahler separation | medium | NOT REPRODUCED at n ≤ 18 |

## 6. NEXT ACTIONS (Prioritized)

| Priority | Action | Dependency | Target |
|:---------|:-------|:-----------|:-------|
| P0 | Obtain NTOF source clarification (Mahler target function; I_C ideal) | none | source author / NTOF record |
| P1 | Complete K–N leg re-implementation (I_C resolution) | P0 | next P4 cycle |
| P2 | Fresh 50/family code generation with seeds | P1 | REG-RES006-001 |
| P3 | Derive valuation-based overhead bound; compare to Singleton | none | FQ2 |
| P4 | Update this registry after each attempt | every cycle | living doc |

## 7. SESSION LOG + MAINTENANCE PROTOCOL

- 2026-08-13: Registry created (v0.2 publication cycle). P1/P2 executed by concurrent pipeline; P3 pending.
- **Maintenance:** update this file on every reproduction attempt, prediction outcome, or new FQ; bump a version counter; commit to the project branch. Do NOT let it become a static artifact.
