# JPCUB Standard v1.0: Universal Joules-per-Solution Benchmarking Protocol

**WBS:** QNFO.RES.JPCUB.P5
**Author:** QNFO Research Collective
**Date:** 2026-08-06
**Status:** Draft — Genre C (Internal/Operations) → Target: Genre A (Epistemic, published standard)
**Parent:** JPCUB P0 (DOI 10.5281/zenodo.21637028), CL v2.0 (DOI 10.5281/zenodo.21821767)

---

## 1. Purpose

The JPCUB framework (P0 paper, DOI 10.5281/zenodo.21637028) defines the joules-per-solution metric and measurement protocol. This standard document formalizes the framework for adoption as a community benchmark, with three key extensions beyond the P0 paper:

1. **Tiered validation framework** — a graduated path from self-reported values to independently verified measurements
2. **Task taxonomy** — a representative task sample covering multiple computational paradigms
3. **Governance model** — separation of benchmark ownership from any single vendor or research group

## 2. The Metric

### 2.1 Formal Definition

For computational system $S$, task $T$, and correctness threshold $\varepsilon$:

$$J_S(T, \varepsilon) = E_{\text{comp}} + E_{\text{mem}} + E_{\text{io}} + E_{\text{cool}} + E_{\text{conv}} + E_{\text{mfg}}$$

### 2.2 Energy Components

| Component | Symbol | Measurement Method |
|:----------|:-------|:-------------------|
| Computation | $E_{\text{comp}}$ | Wall-plug power × execution time (incremental above idle baseline) |
| Memory | $E_{\text{mem}}$ | DRAM/storage energy during task window |
| I/O and Networking | $E_{\text{io}}$ | Data movement energy (inter-chip, inter-node) |
| Cooling | $E_{\text{cool}}$ | Facility cooling energy attributable to system during task |
| Power Conversion | $E_{\text{conv}}$ | AC-DC/DC-DC conversion losses |
| Amortized Manufacturing | $E_{\text{mfg}}$ | Embodied energy ÷ expected lifetime operations |

### 2.3 Measurement Methodology

**Incremental energy (canonical):** Measure total system power at steady-state idle, then measure total system power during task execution. The JPCUB value is:

$$J_S(T, \varepsilon) = \frac{(P_{\text{task}} - P_{\text{idle}}) \times t_{\text{exec}}}{p_{\text{succ}}}$$

Where $p_{\text{succ}}$ is the empirically measured success probability over at least 100 independent shots/trials, and $P_{\text{task}}$, $P_{\text{idle}}$ are measured at the wall plug with calibrated power meters.

**Shared infrastructure:** For systems sharing infrastructure (e.g., a dilution refrigerator serving multiple quantum processors), allocate infrastructure energy proportionally to the task's share of total utilization.

## 3. Tiered Validation Framework

The most significant gap in JPCUB adoption is the cost of independent measurement. A full adversarial validation requires physical access to hardware that may cost $10^7$–$10^8$ USD. The tiered framework creates a graduated path.

### 3.1 Validation Tiers

| Tier | Name | Requirements | Evidential Weight |
|:-----|:-----|:-------------|:------------------|
| **Tier 1** | **Self-Reported** | Vendor publishes JPCUB value with: methodology document, power measurement data, success probability data, circuit specification | Low — trust-based |
| **Tier 2** | **Cloud-Verified** | Independent party measures JPCUB on cloud-accessible hardware (e.g., IBM Quantum, Amazon Braket, IonQ Cloud) | Medium — independent but platform-limited |
| **Tier 3** | **Adversarial** | Independent party measures JPCUB on physical hardware with on-site access, calibration verification, and adversarial task selection | High — gold standard |

### 3.2 Tier Promotion

A Tier 1 value can be promoted to Tier 2 when:
- An independent party reproduces the measurement on the same cloud-accessible hardware
- The reproduced value is within 20% of the self-reported value
- The independent party publishes their methodology, raw data, and code

A Tier 2 value can be promoted to Tier 3 when:
- An independent party conducts an on-site measurement following the adversarial validation protocol (P0 §4.2)
- The adversarial measurement includes at least one task NOT pre-selected by the vendor
- The reproduced value is within 10% of the self-reported value

### 3.3 Current Landscape (2026-08-06)

| Platform | Tier | JPCUB | Validator |
|:---------|:-----|:------|:----------|
| IBM Eagle r3 | **Tier 1** | 0.89 J/sol | IBM (self-reported, P0 protocol) |
| Google Willow | **Tier 0** (model) | 0.05 J/sol | Model-derived upper bound |
| All other CL v2.0 entries | **Tier 0** (model) | Various | Model-derived upper bounds |
| QWAV | **Tier 0** (target) | $<10^{-3}$ J/sol | Design target |

## 4. Task Taxonomy

### 4.1 Representative Task Sample

The JPCUB standard requires measurement on at least two tasks from the representative task sample:

| Task ID | Description | Paradigm(s) | Gate Count (quantum) | Classical Equivalent |
|:--------|:------------|:------------|:---------------------|:---------------------|
| **T-FACT** | Factoring $N = 15$ via Shor's algorithm | Gate-model quantum | 80 gates (30 2Q + 50 1Q) | Trial division, $10^2$ operations |
| **T-CHEM** | Ground-state energy of $H_2O$, 6-31G, $\varepsilon = 1.6$ mHa | Gate-model quantum (deep circuit) | $\approx 500$–$2000$ 2Q gates | FCI/CASCI, minutes on CPU |
| **T-OPT** | MAX-CUT on random 20-node graph, within 5% of best-known | Gate-model + annealing | QAOA $p=2$–$4$ (variable gates) | GW-SDP + local search, seconds on CPU |
| **T-ML** | MNIST image classification, $\varepsilon = 0.95$ accuracy | Quantum ML + classical ML | Quantum kernel/QNN (variable) | CNN inference, $<10^6$ FLOPs |

### 4.2 Task Selection Rules

1. A platform must report JPCUB on at least **one paradigm-native task** and **one cross-paradigm task** where a classical equivalent exists
2. If a platform cannot execute any task in the taxonomy, it must propose a new task with justification for inclusion
3. The task set must be pre-registered before measurement begins

## 5. Anti-Gaming Provisions

### 5.1 Adversarial Validation (P0 §4.2)

Any party may measure any platform. The measurement protocol, raw data, and analysis code must be published. A claim that cannot be independently reproduced is not a claim.

### 5.2 Pre-Registration (P0 §4.3)

Before measurement:
1. Declare the task, methodology, and correctness threshold
2. Register the declaration with a timestamped, immutable record (Zenodo deposit, git commit, or blockchain anchor)
3. The measurement must follow the pre-registered methodology — post-hoc methodology changes invalidate the claim

### 5.3 Pareto Frontier Reporting (P0 §4.4)

For platforms where joules-per-solution trades off against other metrics (speed, accuracy, cost):
1. Report the full Pareto frontier, not a single operating point
2. The frontier must include at least 5 operating points spanning the tradeoff space
3. Cherry-picked frontier points (e.g., the best 2 out of 10 measured points) invalidate the claim

### 5.4 Conservative Bounds

When empirical measurement is not available:
1. Model-derived estimates must use conservative upper bounds (worst-case parameters)
2. The methodology section must explicitly state which parameters are model-derived vs. empirically measured
3. Model-derived values carry the label `[MODEL-DERIVED UPPER BOUND — not empirically measured]`

## 6. Reporting Standard

### 6.1 Required Fields

Every JPCUB report must include:

| Field | Description |
|:------|:------------|
| Platform identifier | Vendor, model, architecture, qubit/qudit count |
| Task specification | Task ID, input, correctness threshold, circuit/gate count |
| System power | Wall-plug measurement with instrument calibration |
| Execution time | Gate-level timing or wall-clock measurement |
| Success probability | Empirical measurement with confidence interval (min 100 shots) |
| JPCUB value | Computed joules-per-solution with uncertainty |
| Validation tier | Tier 1/2/3 with validator identity |
| Methodology | Incremental vs. full-system, infrastructure amortization |
| Raw data | Power traces, success/failure log, code repository |

### 6.2 Uncertainty Reporting

Every JPCUB value must include an uncertainty estimate:

$$J_S(T, \varepsilon) \pm \sigma_J$$

Where $\sigma_J$ is derived from:
- Power measurement uncertainty ($\sigma_P$)
- Timing uncertainty ($\sigma_t$)
- Success probability uncertainty (binomial, $\sigma_p = \sqrt{p(1-p)/n}$)
- Energy component uncertainties (cooling, conversion, manufacturing)

## 7. Governance

### 7.1 Separation Principle

JPCUB is NOT owned by QWAV, QNFO, or any single vendor or research group. It is a community benchmark. The governance model ensures:

1. **No vendor has editorial control** over the benchmark definition
2. **No vendor can exclude a competitor** from the competitive landscape
3. **No vendor can modify the measurement protocol** to favor their architecture

### 7.2 Proposed Governance Structure

| Body | Role | Composition |
|:-----|:-----|:------------|
| **JPCUB Steering Committee** | Approves task taxonomy changes, standard revisions | 5–7 members from academia, industry, and national labs; no single organization >2 seats |
| **JPCUB Technical Working Group** | Maintains measurement protocol, computation tools, reference implementations | Open to all; chaired by Steering Committee member |
| **JPCUB Validation Board** | Reviews Tier 2 and Tier 3 validations | 3 independent experts per validation; rotating membership |
| **JPCUB Secretariat** | Maintains website, database, and competitive landscape | Hosted by a neutral academic institution or standards body |

### 7.3 QWAV/QNFO Role

QWAV/QNFO is the **first adopter and initial contributor**, not the owner. Specifically:

1. QWAV contributes the initial standard document, measurement tools, and competitive landscape database
2. QWAV submits its own hardware to adversarial (Tier 3) validation before asking competitors to do so
3. QNFO funds the initial Secretariat infrastructure (website, database, computation tools) as a public good
4. After 12 months, governance transitions to the Steering Committee

### 7.4 Standards Body Path

Target: JPCUB is proposed as an IEEE standard (or equivalent) within 3 years of initial publication. The path:

1. **Year 1:** Publish as a community standard on Zenodo with open peer review
2. **Year 2:** Partner with an academic institution or national lab for Secretariat hosting
3. **Year 3:** Submit to IEEE Standards Association (or equivalent) for formal standardization

## 8. Competitive Landscape Database

### 8.1 Public Dashboard

A live dashboard at `jpcub.qwav.tech` (or equivalent neutral domain) displaying:
- All platforms with their JPCUB values, tiers, and task specifications
- Tier-appropriate visual separation (measured vs. model-derived vs. design targets)
- Full methodology traceability (click to see raw data, power traces, code)
- Historical tracking (versioned entries, methodology changes over time)

### 8.2 Submission Process

1. Vendor or independent party submits a JPCUB report (Section 6)
2. Technical Working Group reviews for methodology compliance (not result validation — that is Tier 2/3)
3. Approved submissions appear on the dashboard within 7 days
4. Disputed submissions are marked as `[UNDER REVIEW]` with the dispute rationale public

## 9. Calibration Register

```
[CHECK: 2027] JPCUB standard document will have been cited by at least one non-QNFO entity.
Strength: [WEAK] | Status: [PENDING]

[CHECK: 2027] At least one platform will have advanced from Tier 0 (model) to Tier 1 (self-reported).
Strength: [MODERATE] | Status: [PENDING]

[CHECK: 2028] JPCUB governance will include at least one non-QNFO Steering Committee member.
Strength: [WEAK] | Status: [PENDING]

[CHECK: 2029] JPCUB will be proposed as an IEEE (or equivalent) standard.
Strength: [WEAK] | Status: [PENDING]
```

## 10. References

1. JPCUB P0: DOI 10.5281/zenodo.21637028
2. JPCUB CL v2.0: DOI 10.5281/zenodo.21821767
3. JPCUB Strategic Assessment: Session Lix-MUWJTX69KVWScl01C (2026-08-06)
4. SPECpower_ssj2008: https://www.spec.org/power_ssj2008/
5. Green500: https://www.top500.org/lists/green500/
6. MLPerf Power: https://mlcommons.org/benchmarks/power/
