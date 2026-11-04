# Phase 1.5 Gate Summary — Bin Table Update

**Project:** qnfo-photon-audit — Task 1.5.5  
**Date:** 2026-07-21  
**Status:** Complete  
**Pre-registration rule:** All gate memos locked BEFORE Phase 2 testing. Any post-hoc promotion of a claim from Bin C to Bin B requires documenting (a) what new evidence emerged, and (b) why it could not have been predicted from Phase 1 data.

---

## 1. Gate Results

| Gate | Task | Verdict | Bin | Key Finding |
|------|------|---------|-----|-------------|
| H1-G1 | g-2 at Dirac level | PASS | A | KN soliton repoduces g=2; non-evidential (g=2 is required by relativity for any spin-½ particle) |
| H1-G2 | g-2 QED corrections | BLOCKED | C | No derivation exists; KN quantization not available (requires full QG theory) |
| H2b | Knot→mass mapping | CONFIRMED BIN C | C | No parameter-free mapping exists; knot invariants (integer) cannot span mass spectrum (6 orders of magnitude) without free parameters |
| H3 | COTT vs reversible logic | CONFIRMED BIN C | C | Zero external COTT papers; standard reversible logic (Bennett 1973) already achieves zero dissipation; COTT provides NO operation beyond Toffoli-Fredkin reversible gates |
| H4b | p-fixing principle | CONFIRMED BIN C | C | No independent p-fixing principle exists in p-adic QM literature; p is always a free parameter; adelic product diverges without truncation criterion |

---

## 2. Updated Bin Table

### Bin A — Established / Non-evidential

| Claim | Bin | Justification |
|-------|-----|--------------|
| H1a (Dirac g-2) | A | CODATA 2022 agreement; g=2 is a necessary consequence of relativistic QM for spin-½ particles, not unique to photonic-substrate |
| EM knots exist (Rañada 1989) | A | Rigorous mathematical result; experimentally realized (Bouwmeester 2008) |

### Bin B — Open / Pre-registerable

| Claim | Bin | Pre-registration status |
|-------|-----|------------------------|
| H1b (knotted photon → electron observables) | B | BLOCKED by H1-G2 (no g-2 derivation). Promotion to A requires: (a) explicit Lagrangian, (b) g-2 to 3+ significant figures, (c) charge derivation. **No Phase 2 test designed — gating condition not met.** |
| Spin-statistics circumvention (composite-boson route) | B | Suzuki (2017) provides formal path; no photonic-model instantiation exists. **Phase 2 test designable only if a specific composite-photon Lagrangian is provided first.** |

### Bin C — Untestable / Blocked

| Claim | Bin | Reason |
|-------|-----|--------|
| H1c (EM knots → spin-½ from bosonic fields) | C | Spin-statistics theorem. Composite-boson route (Suzuki 2017) is the only viable path; fundamental-boson route is blocked |
| H1-G2 (g-2 from KN) | C | No derivation exists; KN quantization requires full quantum gravity |
| H2b (knot→mass) | C | No mapping exists; knot invariants (integer) vs mass spectrum (6 orders of magnitude) — fundamental mismatch |
| H3 (COTT) | C | Zero external validation; standard reversible logic already superior |
| H4b (p-fixing) | C | No principle exists; p is free parameter in all models |
| H4a (Planck→Rydberg bridge) | C- | 25-order bridge implausible under standard QFT; ultrametric non-locality provides only conceptual possibility with free metric f(k) |

---

## 3. Promotion Log

**No claims promoted from Bin B to Bin A or from Bin C to Bin B during this gate review.**

Every Bin C claim remained Bin C after analytical scrutiny. Every Bin B claim remained Bin B because its gate condition (g-2 derivation, explicit Lagrangian, charge derivation) was not met. This is the expected outcome — the Phase 0 bin table's Bin C expectations (H3, H4b) were confirmed, and the H2b Bin C expectation was confirmed.

---

## 4. Recommendations for Phase 2

### Phase 2 executable tasks (gating conditions met)

| Task | ID | Bin | Justification |
|------|----|-----|---------------|
| H2a: Quantized Berry phase prediction | 2.1 | B | Photonic vortex soliton has well-defined topological charge; Berry phase is computable from known formalism. **GATE: literature comparison only (no new experiment).** |
| H5: Reversible logic calorimetry | 2.3 | B | Literature verification of existing Landauer-limit calorimetry experiments. No COTT-specific prediction — standard reversible logic benchmark. |

### Phase 2 blocked tasks (gating conditions NOT met)

| Task | ID | Reason |
|------|----|--------|
| H4a Rydberg spectroscopy | 2.2 | Bin C-: p not fixed; ultrametric metric f(k) free; Planck-Rydberg bridge implausible |
| Promoted claims | 2.4 | No claims were promoted during gate review |

---

## 5. Cross-Referencing

### 5a. Spin-statistics interaction with H1-G1

The spin-statistics barrier (`artifacts/spin-statistics-barrier.md`) found that the composite-boson route (Suzuki 2017) is the least problematic path for the photonic-substrate hypothesis. However, the composite-boson route does NOT address g-2 — the g-2 gap is a SEPARATE blocking condition from spin-statistics. Even if photons emerge as composite bosons from a fermionic substrate, the g-2 correction still requires a quantum-field-theoretic derivation that no knotted-soliton model provides.

### 5b. H4a interaction with H4b

Both H4a (scale estimate) and H4b (p-fixing) are Bin C. The p-fixing problem is the MORE FUNDAMENTAL gate — even if the Planck-Rydberg bridge were plausible (which H4a shows it is not under standard assumptions), no p-adic model could make a specific prediction without a p-fixing principle. The two Bin C classifications are independent and multiplicative in severity.

---

## 6. Gate Summary Closeout

| Metric | Value |
|--------|-------|
| Gates attempted | 5 |
| Gates passed | 1 (H1-G1: non-evidential) |
| Gates blocked | 4 (H1-G2, H2b, H3, H4b) |
| Bin A claims confirmed | 2 |
| Bin B claims confirmed | 2 |
| Bin C claims confirmed | 5 |
| Bin C- claims confirmed | 1 |
| Claims promoted | 0 |
| Claims demoted | 0 |
| Phase 2 executable tasks | 2 (H2a, H5) |
| Phase 2 blocked tasks | 2 (H4a, promoted claims) |

**Phase 1.5 closeout statement:** All gate conditions evaluated. The pre-registration rule is enforced. No claim was tested in Phase 2 without first being gated in Phase 1.5. The H3, H4b, and H2b Bin C assignments are confirmed by analytic analysis and exhaustive literature survey. The H1 g-2 gap remains the single most blocking condition for the photonic-substrate hypothesis.
