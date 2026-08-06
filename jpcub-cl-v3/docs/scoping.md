# JPCUB Competitive Landscape v3.0: Multi-Task Scoping Document

**WBS:** QNFO.RES.JPCUB.P4
**Author:** QNFO Research Collective
**Date:** 2026-08-06
**Status:** Draft — Genre C (Internal/Operations)
**Parent:** JPCUB CL v2.0 (DOI 10.5281/zenodo.21821767)

---

## 1. Purpose

JPCUB CL v2.0 established the joules-per-solution ranking for 17 quantum computing platforms on a single task (factoring $N = 15$). The core finding — gate speed dominates joules-per-solution — is `[speculative — single-task]`. CL v3.0 must extend the methodology to multiple tasks to establish ranking robustness and cross-paradigm comparability.

## 2. Task Selection

### 2.1 Task Taxonomy

CL v3.0 adds three task classes, each designed to stress a different JPCUB cost driver:

| Task Class | Description | Primary Cost Driver Stressed | Platforms |
|:-----------|:------------|:-----------------------------|:----------|
| **Factoring** (existing) | Shor's algorithm, $N = 15$ | Gate speed | All 13 gate-model |
| **Deep Circuit** | Quantum chemistry simulation (e.g., $H_2O$ ground state, 6-31G basis) | Fidelity, error mitigation | Gate-model with $>50$ qubits |
| **Optimization** | Ising-model ground state (MAX-CUT on random 20-node graph) | Paradigm-native speed (annealing vs. QAOA) | Gate-model + annealing |
| **Classical Baseline** | Same tasks on classical hardware (CPU, GPU, TPU) | Cross-paradigm comparability | All classical |

### 2.2 Deep Circuit Task Specification

**Task $T_2$:** Compute the ground-state energy of $H_2O$ in the 6-31G basis set to within chemical accuracy ($\varepsilon = 1.6$ mHa).

- **Circuit depth:** $\approx 500$–$2000$ two-qubit gates (hardware-efficient ansatz or UCCSD)
- **Correctness threshold:** $\varepsilon = 0.95$ probability of energy within 1.6 mHa of FCI reference
- **Reference:** Classical FCI/CASCI benchmark from PySCF or Psi4
- **Platforms:** Gate-model platforms with $\geq 50$ qubits (Willow, Heron, H2, Forte, Aquila)

**Why this task:** Deep circuits shift the JPCUB ranking from gate-speed-dominated to fidelity-dominated. The fidelity-product model ($p_{\text{succ}} = f_{2Q}^{N_{2Q}}$) becomes the dominant term when $N_{2Q} \gg 30$. A platform with 99.95% fidelity but slower gates may outperform a platform with 99.8% fidelity and faster gates on deep circuits.

**Falsifiable prediction:** The ranking of superconducting platforms (Willow vs. Heron) will invert between the factoring task (gate-speed dominated) and the deep-circuit task (fidelity-dominated). Google Willow's 99.95% fidelity should give it a larger advantage on deep circuits than on shallow circuits.

### 2.3 Optimization Task Specification

**Task $T_3$:** Find the maximum cut of a random 20-node Erdős–Rényi graph ($p = 0.5$).

- **Correctness threshold:** $\varepsilon = 0.95$ probability of finding a cut within 5% of the best-known cut
- **Gate-model approach:** QAOA with $p = 2$–$4$ layers on superconducting/neutral-atom/trapped-ion hardware
- **Annealing approach:** D-Wave Advantage/Advantage2, 100–1000 anneals per problem instance
- **Classical baseline:** Goemans–Williamson SDP relaxation + local search

**Why this task:** This is the first task where D-Wave's annealing architecture can compete directly with gate-model platforms on the SAME JPCUB metric. The cross-paradigm comparison is what JPCUB was designed for.

**Falsifiable prediction:** D-Wave Advantage2 will achieve lower joules-per-solution than at least one trapped-ion platform for this optimization task, despite being gate-incompatible for factoring. If D-Wave's JPCUB is higher than all gate-model platforms on their native task, the annealing paradigm's energy advantage is not real.

### 2.4 Classical Baseline Task Specification

For each quantum task, measure JPCUB on classical hardware:

| Architecture | Device | J/op (chip-level) | P_sys (wall-plug) |
|:-------------|:-------|:------------------|:------------------|
| x86 Server CPU | AMD EPYC / Intel Xeon | $\approx 2 \times 10^{-9}$ | $\approx 200$–$400$ W |
| Smartphone ARM | Apple A17 / Snapdragon 8 Gen 3 | $\approx 5 \times 10^{-10}$ | $\approx 3$–$5$ W |
| GPU | NVIDIA H100 | $\approx 5 \times 10^{-10}$ (integer) | $\approx 350$–$700$ W |
| TPU/accelerator | Google TPU v5 | $\approx 10^{-10}$ | $\approx 200$–$450$ W |

**Note:** For tasks trivially solved by classical hardware ($N = 15$ factoring), the classical JPCUB is $\approx 10^{-7}$ J/sol — $10^6$–$10^7\times$ better than any quantum platform. This is established in CL v2.0 §8.1.

## 3. Methodology Extensions

### 3.1 Fidelity Model Upgrade

The current fidelity-product model ($p_{\text{succ}} = f_{2Q}^{N_{2Q}}$) is a lower bound. CL v3.0 should add:

1. **Error mitigation accounting** — surface-code threshold effects, zero-noise extrapolation
2. **Algorithmic fidelity** — randomized benchmarking vs. algorithmic fidelity gap
3. **Circuit optimization** — platform-specific transpiler effects on gate count

### 3.2 Power Model Refinement

1. **Incremental energy methodology** — follow JPCUB P0 §3.3 for comparability with published IBM Eagle value (0.89 J/sol)
2. **Idle power amortization** — distinguish steady-state infrastructure draw from task-specific energy
3. **Shared infrastructure** — model multi-tenancy effects (multiple concurrent tasks sharing a dilution refrigerator)

### 3.3 Cross-Paradigm Normalization

For annealing and sampling platforms that cannot execute gate-model tasks:
- Define **paradigm-native tasks** with cross-paradigm equivalents
- Report JPCUB on paradigm-native tasks with explicit cross-paradigm caveats
- Do not force gate-model metrics onto non-gate-model platforms

## 4. Deliverables

| Deliverable | Description | Format |
|:------------|:------------|:-------|
| CL v3.0 paper | Multi-task competitive landscape | Zenodo preprint (md, pdf, html) |
| Reproducible computation | Python script with all JPCUB computations | GitHub repo |
| Specification traceability | Source citations for every platform parameter | Appendix or companion file |
| Cross-paradigm atlas | Updated per-operation atlas with new tasks | Table in paper |

## 5. Timeline

| Phase | Description | Target |
|:------|:------------|:-------|
| P1 | Due diligence — external benchmarks, new platform specs | Q3 2026 |
| P2 | Literature — quantum chemistry benchmarks, optimization baselines | Q3 2026 |
| P4 | Computation — JPCUB estimates for all 3 tasks | Q4 2026 |
| P5 | Publication — Zenodo deposit | Q4 2026 |

## 6. Risks

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Deep-circuit specifications unavailable | Medium | Delays ranking | Use approximate circuits from literature |
| D-Wave JPCUB estimate too approximate | Medium | Weakens cross-paradigm claim | Conservative upper bound; flag as approximate |
| New platform releases during scoping | High | Scope creep | Freeze specs at publication date; defer new platforms to v4.0 |

## 7. Calibration Register

```
[CHECK: 2027-Q1] CL v3.0 will confirm gate-speed dominance on factoring but show fidelity dominance on deep circuits.
Strength: [MODERATE] | Status: [PENDING]

[CHECK: 2027-Q2] At least one annealing platform will achieve lower JPCUB than at least one gate-model platform on the optimization task.
Strength: [WEAK] | Status: [PENDING]

[CHECK: 2027-Q2] The cross-paradigm ranking will change between the factoring and optimization tasks.
Strength: [MODERATE] | Status: [PENDING]
```

## References

1. JPCUB P0: DOI 10.5281/zenodo.21637028
2. JPCUB CL v2.0: DOI 10.5281/zenodo.21821767
3. Gidney & Ekerå (2021): DOI 10.22331/q-2021-04-15-433
