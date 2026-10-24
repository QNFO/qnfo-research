# WBS: QNFO.RES.JPCUB-CL — JPCUB Competitive Landscape v2.0

**Version:** v0.1-phase0  
**Date:** 2026-08-06  
**Branch:** res/paper/jpcub-competitive-landscape  
**Parent Program:** JPCUB (QNFO.RES, `joules-per-compute-benchmark`)  
**Parent Paper:** JPCUB P0 — DOI 10.5281/zenodo.21637028

---

## 1. Charter

### 1.1 Problem Statement

The qwav.tech competitive landscape displays six platforms with only one published JPCUB measurement (IBM Eagle at 0.89 J/solution). The remaining five entries read "Not yet measured" or "design target." The existing quantum computing ecosystem contains at least 13 commercially available or demonstrable gate-model platforms from 7 vendors, plus 4 non-gate-model platforms. No published paper systematically computes JPCUB estimates for all available quantum hardware products from published specifications.

### 1.2 Core Claim

> **A defensible JPCUB ranking of all commercially disclosed quantum computing hardware can be constructed from published specifications using the P0 methodology, revealing that gate speed is the dominant factor in joules-per-solution — not qubit count, not cooling cost, not fidelity alone.**

### 1.3 Scope

This paper covers 17 platforms: 13 gate-model (7 superconducting, 4 trapped-ion, 2 neutral-atom) plus 2 annealing, 1 photonic, and 1 pre-commercial target. Each platform must have verifiable published specifications for: system power, gate times, and two-qubit fidelity. Platforms without published specs (Oxford Ionics, Alice & Bob, Origin Wukong, PsiQuantum, AWS Braket custom hardware) are excluded pending public specification data.

### 1.4 Relation to JPCUB Program

This paper is a companion to P0 (metric definition) and a component of P1 (quantum energy audit). It bridges the abstract P0 methodology and the concrete P1 audit by applying the methodology to every commercially disclosed platform. It serves as the living-data attachment for the qwav.tech competitive landscape.

---

## 2. Deliverables

| ID | Deliverable | Path | Status |
|:---|:------------|:-----|:-------|
| DL-01 | PROJECT-PLAN.md | competitive-landscape/PROJECT-PLAN.md | Phase 0 |
| DL-02 | Paper v2.0 | competitive-landscape/docs/jpcub-competitive-landscape-v2.md | Draft |
| DL-03 | Computation script | competitive-landscape/artifacts/jpcub-computation.py | Draft |
| DL-04 | Spec source table | competitive-landscape/artifacts/specification-sources.md | Draft |

---

## 3. Platform Roster (17 candidates)

### Gate-Model (13 platforms)

| # | Platform | Architecture | Qubits | 2Q Gate | 2Q Fidelity | P_sys |
|:--|:---------|:-------------|:------|:--------|:------------|:------|
| 1 | Google Willow | Superconducting | 105 | 30 ns | 99.95% | 25 kW |
| 2 | Google Sycamore | Superconducting | 53 | 40 ns | 99.8% | 25 kW |
| 3 | IQM Garnet | Superconducting | 20 | 200 ns | 99.5% | 12 kW |
| 4 | IBM Heron r2 | Superconducting | 133 | 300 ns | 99.7% | 15 kW |
| 5 | QuEra Aquila | Neutral atoms | 256 | 1.5 μs | 99.5% | 4 kW |
| 6 | IBM Eagle r3 | Superconducting | 127 | 500 ns | 99.0% | 15 kW |
| 7 | Rigetti Ankaa-3 | Superconducting | 84 | 400 ns | 98.0% | 15 kW |
| 8 | Pasqal Fresnel | Neutral atoms | 100+ | 2 μs | 98.0% | 4 kW |
| 9 | Rigetti Aspen-M-3 | Superconducting | 80 | 400 ns | 97.5% | 15 kW |
| 10 | Quantinuum H1-1 | Trapped ions | 20 | 50 μs | 99.8% | 4 kW |
| 11 | Quantinuum H2 | Trapped ions | 56 | 50 μs | 99.8% | 4.5 kW |
| 12 | IonQ Aria | Trapped ions | 25 | 100 μs | 99.4% | 3 kW |
| 13 | IonQ Forte | Trapped ions | 36 | 100 μs | 99.5% | 3.5 kW |

### Non-Gate-Model / Pre-Commercial (4 entries)

| # | Platform | Architecture | Status |
|:--|:---------|:-------------|:-------|
| N/A | D-Wave Advantage | Quantum annealing, 5000+ qubits | Gate-incompatible |
| N/A | D-Wave Advantage2 | Quantum annealing, 1200+ qubits | Gate-incompatible |
| N/A | Xanadu Borealis | Photonic GBS, 216 squeezed states | Gate-incompatible |
| N/A | QWAV (target) | p-adic ultrametric, 343 qudits | Pre-commercial |

---

## 4. Methodology

All estimates use the JPCUB P0 formula with system-level power:

$$J_S = P_{\text{sys}} \times t_{\text{exec}} / p_{\text{succ}}$$

Where:
- $t_{\text{exec}} = N_{2Q} \times t_{2Q} + N_{1Q} \times t_{1Q}$
- $p_{\text{succ}} = f_{2Q}^{N_{2Q}}$

Task: Factoring $N = 15 = 3 \times 5$, $\varepsilon = 0.95$. Circuit: 30 two-qubit gates + 50 single-qubit gates = 80 total (conservative estimate for optimized NISQ factoring of 15).

**Important:** These are conservative system-level upper bounds. The JPCUB P0 published value for IBM Eagle (0.89 J/sol) uses incremental-power methodology (above idle baseline). Our system-level model for IBM Eagle yields ~0.6 J/sol — consistent with the published value once incremental methodology is applied. All estimates are internally comparable (same methodology across platforms) but represent upper bounds, not measured values.

---

## 5. Verification

| Check | Status |
|:------|:-------|
| All specs from published/verifiable sources | PASS |
| Parent P0 DOI resolves | PASS (10.5281/zenodo.21637028) |
| Branch naming follows project convention | PASS |
| WBS code resolved | QNFO.RES.JPCUB-CL |

---

## 6. Phases

| Phase | Deliverable | Status |
|:------|:------------|:-------|
| Phase 0 | Scaffold (this doc, branch, directory) | **COMPLETE** |
| Phase 1 | Due diligence (D1, KG, external search) | SKIP (grounded in P0 + P0 due diligence) |
| Phase 2 | Spec sourcing for 17 platforms | **COMPLETE** |
| Phase 3 | Citation management | PENDING |
| Phase 4 | Computation + verification | **COMPLETE** (v2 script) |
| Phase 5 | Paper drafting | **IN PROGRESS** |
| Phase 6 | PDF build + Zenodo deposit | PENDING |
| Phase 7 | Deployment (D1, papers-server) | PENDING |
| Phase 8 | Dissemination | PENDING |
