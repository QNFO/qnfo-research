# H1 Gate Memo: g-2 Correction from Kerr-Newman Soliton Machinery

**Project:** qnfo-photon-audit — Task 1.5.1  
**Date:** 2026-07-21  
**Status:** Phase 1.5 Pre-Registration Gate  
**Gate:** Attempt g-2 correction derivation from Kerr-Newman soliton machinery; lock or log

---

## 1. Gate Question

Can the Kerr-Newman (KN) electron model (Burinskii 2000, 2015, 2023) or extended EM-knot soliton models reproduce the electron's anomalous magnetic moment a_e = (g-2)/2 to the experimentally measured precision of 1 part in 10¹²?

---

## 2. Background: The g-2 Gap

### 2a. Experimental value

CODATA 2022: a_e(exp) = 0.001 159 652 180 59 (13) → precision: 1.1 × 10⁻¹³

### 2b. QED prediction

The Dirac equation predicts g = 2 exactly → a_e(Dirac) = 0. The first QED correction (Schwinger 1948) gives:

a_e(QED, 1-loop) = α / (2π) = 0.001 161 409 7...

The full QED calculation (10th-order + hadronic + electroweak) agrees with experiment to ~1 part in 10¹² — the most precisely tested prediction in all of physics.

### 2c. What the KN model provides

Burinskii's Kerr-Newman electron model produces the Dirac value g = 2 from the Kerr geometry's intrinsic spinorial structure. This is the CLASSICAL gyromagnetic ratio from the KN solution, NOT a quantum-corrected value. The KN solution has:

- Mass: M (free parameter of the solution)
- Angular momentum: J = Ma (a = rotation parameter)
- Charge: e (free parameter)
- Magnetic moment: μ = e a (exactly, from KN geometry)

The relationship μ = (e/m) × J/2 gives g = 2 exactly, matching the Dirac equation's prediction for a spin-½ particle.

---

## 3. Attempted Derivation

### 3a. Can the KN model produce g-2 corrections?

**Short answer: No published derivation exists.**

Longer analysis: The QED g-2 correction arises from virtual photon exchange (vertex correction), vacuum polarization (photon self-energy), and electron self-energy diagrams — fundamentally quantum field-theoretic processes. The KN solution is a purely CLASSICAL solution of Einstein-Maxwell theory:

1. **No virtual particles:** The KN geometry has no mechanism for virtual photon loops (vertex correction), the dominant contribution to a_e.
2. **No QED vertices:** The KN solution's coupling between the electron and electromagnetic field is classical (through the Einstein-Maxwell field equations), not quantum (through the QED interaction vertex ieγ^μ).
3. **No renormalization scale:** QED corrections depend on the renormalization scale μ and the running of α(Q²). The KN geometry has no renormalization group flow.

### 3b. Potential routes (none realized)

| Route | Mechanism | Status |
|-------|-----------|--------|
| KN quantum fluctuations | Quantize the KN solution; compute one-loop corrections | No published work. KN quantization encounters major obstacles: time-like naked singularity, no consistent quantum gravity theory |
| KN + QED perturbation | Treat KN as a classical background; compute QED corrections on this background | Speculative. Background field method in QED is well-established, but KN as background has never been used for g-2 calculations |
| String theory embedding | Embed KN in string theory; derive g-2 from stringy corrections | No published work. KN solution is not a known string-theoretic object in standard compacifications |
| Semiclassical gravity | Compute g-2 from KN in semiclassical gravity (QFT on curved KN background) | No published work. Semiclassical gravity on KN background is mathematically challenging (singularity, closed timelike curves) |

### 3c. Burinskii's position

Burinskii (2023, "Kerr-Newman electron and the problem of spin," *Phys. Part. Nucl.* 54(5), 865) acknowledges the g-2 gap implicitly — his program focuses on the classical KN geometry reproducing g=2 exactly, and he treats the QED corrections as a separate quantum regime not addressed by the KN description. Burinskii does NOT claim that the KN model reproduces g-2.

---

## 4. Reformulation as a Locked Gap

The H1 gate is reformulated as two sub-gates:

### 4a. H1-G1: KN → g=2 (confirmed)

The KN solution produces g=2 exactly. This is [Est] and matches the Dirac prediction. **Gate: PASS — KN reproduces Dirac-level g=2.**

### 4b. H1-G2: KN → g-2 correction (not achieved)

The KN solution does NOT produce g-2 corrections to any precision. No published work even attempts this derivation, and fundamental obstacles exist:

1. QED loops require quantum field theory; KN is classical
2. KN quantization encounters the singularity and closed-timelike-curve problems of the KN geometry
3. The KN solution's mass parameter M is free — not derived from topology or any other principle

**Gate: BLOCKED — no KN-based g-2 derivation exists, nor is one likely without a quantization of the KN solution (i.e., a full theory of quantum gravity).**

---

## 5. Verdict

**H1 gate: PARTIALLY SATISFIED.**

| Sub-gate | Status | Bin |
|----------|--------|-----|
| H1-G1 (KN → g=2) | PASS — classical KN geometry reproduces g=2 | Bin A — [Est] |
| H1-G2 (KN → g-2 correction) | BLOCKED — no derivation exists; KN quantization not available | Bin C — [Blocked] |

### Locked Prediction

**LOCKED-001:** The KN solution predicts g=2 exactly (classical Dirac value). This prediction is already confirmed by the Dirac equation independently of any soliton model — it does not distinguish KN from standard QFT. Any claim that KN uniquely predicts g=2 beyond what Dirac/QED already does is void because g=2 is a necessary consequence of relativistic quantum mechanics for spin-½ particles, not a unique prediction of the KN model.

### Falsifiability

The H1 claim would be SUPPORTED (beyond Dirac) if: an extended KN-soliton model produces a specific numerical value for a_e = (g-2)/2 that matches experiment to better than 1% with zero free parameters beyond the Standard Model.

It would be DISCONFIRMED if: a rigorous no-go theorem proves that ANY classical soliton model (not just KN) must produce g=2 exactly and can never generate the loop-level corrections that are the origin of g-2 in QFT.

---

## 6. Recommendation for Gate Summary (Task 1.5.5)

- **H1-G1 → Bin A (confirmed):** KN reproduces g=2. This is non-evidential for the photonic-substrate hypothesis because g=2 is already required by relativistic quantum mechanics for any spin-½ particle.
- **H1-G2 → Bin C (locked):** g-2 corrections cannot be derived from KN soliton machinery without a full quantum gravity theory. This is a blocking gap.
- **Overall H1 → Bin B (unchanged):** g-2 gap prevents promotion to Bin A. The classical g=2 reproduction is necessary but not sufficient.
