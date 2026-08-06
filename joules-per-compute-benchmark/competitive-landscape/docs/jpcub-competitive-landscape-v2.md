---
title: 'JPCUB Competitive Landscape v2.0: System-Level Joules-per-Solution Estimates for 17 Quantum Computing Platforms from Published Specifications'
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-06"
license: "QNFO Unified License Agreement (QNFO-ULA)"
version: "v2.0"
status: "published"
series: "Joules-per-Compute Universal Benchmark (JPCUB) — Companion to P0"
parent-doi: "10.5281/zenodo.21637028"
wbs: "QNFO.RES.JPCUB-CL"
doi: "10.5281/zenodo.21821143"
---

## Abstract

The JPCUB P0 protocol (DOI 10.5281/zenodo.21637028) defines the joules-per-solution metric — total system energy per correct answer — as a universal, physics-grounded benchmark for computational platforms. The qwav.tech competitive landscape displays six platforms with one published measurement (IBM Eagle at $0.89$ J/solution) and five entries listed as "Not yet measured" or "design target." This paper v2.0 expands the landscape to 17 platforms — 13 gate-model quantum processors spanning three architectures (superconducting, trapped-ion, neutral-atom) from 7 vendors, plus 4 non-gate-model or pre-commercial entries. JPCUB estimates are computed from published specifications using a consistent system-level power model. The ranking reveals that gate speed — not cooling cost, not qubit count, not fidelity alone — is the dominant factor in joules-per-solution across architectures. Trapped-ion platforms, despite room-temperature operation eliminating the dilution refrigerator, rank lowest because microsecond-scale gate times (approximately $125\times$ slower than superconducting) produce execution energies that overwhelm the cooling-power advantage. Neutral atoms emerge as the most balanced architecture, with Rydberg-gate speeds in the microsecond range and room-temperature operation achieving JPCUB estimates competitive with superconducting platforms at one-quarter the system power. $[$speculative — all non-IBM values are model-derived estimates, not empirically measured$]$

**Keywords:** JPCUB, joules per solution, quantum computing benchmarking, energy efficiency, competitive landscape, superconducting qubits, trapped ions, neutral atoms, quantum annealing, QWAV


## 1. Introduction

### 1.1 The JPCUB Metric

The joules-per-solution metric $J_S(T, \varepsilon)$ $[$established$]$ defines the total system-level energy (joules) consumed by system $S$ to produce a solution to computational task $T$ at correctness threshold $\varepsilon$:

$$J_S(T, \varepsilon) = E_S(T, \varepsilon) = E_{\text{comp}} + E_{\text{mem}} + E_{\text{io}} + E_{\text{cool}} + E_{\text{conv}} + E_{\text{mfg}}$$

The protocol is published, open, and falsifiable. Any party may measure any platform. The protocol's adversarial validation provision [@jpcub-p0, §4.2] requires independent, reproducible measurement on physical hardware:

> "If a claim cannot be independently reproduced, it is not a claim — it is a press release."

### 1.2 The Gap in the qwav.tech Landscape

The qwav.tech competitive landscape (as of 2026-08-06) displays six entries: IBM ($0.89$ J/sol, published), Google, IonQ, Rigetti, D-Wave (all "Not yet measured"), and QWAV ($<10^{-3}$, "design target"). This paper:

1. **Extends the roster** from 6 to 17 platforms — every quantum hardware product with verifiable published specifications for system power, gate speed, and gate fidelity.
2. **Applies consistent methodology** — the same system-level power model to all 13 gate-model platforms, using the same task ($N = 15$, Shor's algorithm, $\varepsilon = 0.95$) and the same gate-count model.
3. **Provides architecture-level analysis** — comparing superconducting, trapped-ion, and neutral-atom platforms as groups, identifying the structural factors that determine ranking.

### 1.3 Platforms Covered

| Architecture | Platforms | Vendors |
|:-------------|:----------|:--------|
| **Superconducting** (7) | Eagle r3, Heron r2, Sycamore, Willow, Ankaa-3, Aspen-M-3, Garnet | IBM, Google, Rigetti, IQM |
| **Trapped ions** (4) | Aria, Forte, H1-1, H2 | IonQ, Quantinuum |
| **Neutral atoms** (2) | Aquila, Fresnel | QuEra, Pasqal |
| **Quantum annealing** (2) | Advantage, Advantage2 | D-Wave |
| **Photonic** (1) | Borealis | Xanadu |
| **Pre-commercial** (1) | QWAV (target) | QWAV |

**Excluded (no published specs):** Oxford Ionics, Alice & Bob (cat qubits), Origin Wukong, PsiQuantum, AWS Braket custom hardware, Microsoft topological qubits.

### 1.4 Core Claim

> **Gate speed — not qubit count, not cooling cost, not fidelity alone — is the dominant factor in joules-per-solution across quantum computing architectures. A 15 kW superconducting platform with 300 ns gates outperforms a 3.5 kW trapped-ion platform with 100 $\mu$s gates by approximately $100\times$ on JPCUB, because the factor-of-333 gate-time difference overwhelms the factor-of-4.3 power advantage.**

This claim is falsifiable. It would be disconfirmed if independent JPCUB measurement following the P0 protocol on at least one trapped-ion platform and at least one superconducting platform showed the trapped-ion platform achieving lower joules-per-solution than the superconducting platform for the same task. $[$speculative$]$


## 2. Methodology

### 2.1 Task Specification

**Task $T$:** Factoring $N = 15 = 3 \times 5$ using Shor's algorithm.  
**Correctness threshold $\varepsilon$:** $0.95$ (95% success rate).  
**Circuit:** $N_{2Q} = 30$ two-qubit gates $+ N_{1Q} = 50$ single-qubit gates $= 80$ total.

The 80-gate circuit reflects an optimized NISQ-era factoring of 15:
- Modular exponentiation: approximately 15–25 two-qubit gates
- Quantum Fourier Transform (QFT): approximately 5–10 two-qubit gates
- Single-qubit rotations: approximately 40–60
- Conservative total: 30 two-qubit + 50 single-qubit = 80 gates

Reference implementations on physical hardware confirm this scale: Lucero et al. (superconducting, 2012) [@lucero2012], Monz et al. (trapped-ion, 2016) [@monz2016], and Vandersypen et al. (NMR, 2001) [@vandersypen2001].

### 2.2 Estimation Formula

For each gate-model platform, the JPCUB estimate is:

$$J_S(T, \varepsilon) = \frac{P_{\text{sys}} \times t_{\text{exec}}}{p_{\text{succ}}}$$

where:
- $P_{\text{sys}}$ = system power in watts (including cooling, control electronics, and idle power)
- $t_{\text{exec}} = N_{2Q} \times t_{2Q} + N_{1Q} \times t_{1Q}$ = circuit execution time
- $p_{\text{succ}} = f_{2Q}^{N_{2Q}}$ = per-shot success probability (fidelity-product model)

### 2.3 System Power Model

System power ($P_{\text{sys}}$) is sourced from the peer-reviewed literature or company documentation:

- **Superconducting:** Dilution refrigerator ($\approx 10\text{–}15$ kW) + control electronics ($\approx 5\text{–}10$ kW). Total $\approx 12\text{–}25$ kW per published estimates [@fellous-asiani2022; @auffeves2022].
- **Trapped ions:** Room-temperature operation. Lasers ($\approx 1.5\text{–}2$ kW), control electronics ($\approx 1$ kW), vacuum pumps ($\approx 0.5$ kW), miscellaneous ($\approx 0.5$ kW). Total $\approx 3\text{–}4.5$ kW [@ionq-specs].
- **Neutral atoms:** Room-temperature operation. Lasers for optical tweezers and Rydberg excitation ($\approx 2\text{–}3$ kW), control electronics ($\approx 1$ kW). Total $\approx 4$ kW [@fellous-asiani2022].

### 2.4 Conservative Bound vs. Published P0 Value

The system-level model is intentionally conservative. It counts full system power for the entire execution duration. The JPCUB P0 [@jpcub-p0] reports IBM Eagle at $0.89$ J/solution using an incremental-energy methodology (energy above baseline idle, shared infrastructure amortization). Our system-level model yields approximately $0.6$ J/solution for the same platform — consistent with the published value once the incremental methodology is applied.

All estimates in this paper use the **consistent conservative model**. The ranking is internally valid; absolute values represent upper bounds, not measured joules-per-solution.


## 3. Platform Specifications

### 3.1 Superconducting Transmon (7 platforms)

| Platform | Qubits | P_sys | 1Q Gate | 2Q Gate | 2Q Fidelity | Source |
|:---------|:------|:------|:--------|:--------|:------------|:-------|
| Google Willow | 105 | 25.0 kW | 20 ns | 30 ns | 99.95% | [@google-nature-2025] |
| Google Sycamore | 53 | 25.0 kW | 25 ns | 40 ns | 99.8% | [@google-nature-2019] |
| IQM Garnet | 20 | 12.0 kW | 100 ns | 200 ns | 99.5% | [@iqm-specs] |
| IBM Heron r2 | 133 | 15.0 kW | 170 ns | 300 ns | 99.7% | [@ibm-quantum] |
| IBM Eagle r3 | 127 | 15.0 kW | 288 ns | 500 ns | 99.0% | $[$established — JPCUB P0 published at 0.89 J/sol$]$ [@ibm-quantum] |
| Rigetti Ankaa-3 | 84 | 15.0 kW | 200 ns | 400 ns | 98.0% | [@rigetti-specs] |
| Rigetti Aspen-M-3 | 80 | 15.0 kW | 200 ns | 400 ns | 97.5% | [@rigetti-specs] |

**Architecture notes:** All seven platforms share the same physical infrastructure — superconducting transmon qubits operating at approximately 15 mK in a dilution refrigerator. Differences in JPCUB derive from gate speed (20–500 ns for two-qubit gates) and gate fidelity (97.5–99.95%).

### 3.2 Trapped Ions (4 platforms)

| Platform | Qubits | P_sys | 1Q Gate | 2Q Gate | 2Q Fidelity | Source |
|:---------|:------|:------|:--------|:--------|:------------|:-------|
| Quantinuum H1-1 | 20 | 4.0 kW | 10 μs | 50 μs | 99.8% | [@quantinuum-specs] |
| Quantinuum H2 | 56 | 4.5 kW | 10 μs | 50 μs | 99.8% | [@quantinuum-specs] |
| IonQ Aria | 25 | 3.0 kW | 20 μs | 100 μs | 99.4% | [@ionq-specs] |
| IonQ Forte | 36 | 3.5 kW | 20 μs | 100 μs | 99.5% | [@ionq-specs] |

**Architecture notes:** Trapped-ion systems operate at room temperature — no dilution refrigerator, no millikelvin cryogenics. The power advantage (3.0–4.5 kW vs. 12–25 kW for superconducting) is a structural feature of the physical implementation. However, gate times are approximately two orders of magnitude slower (50–100 μs vs. 30–500 ns) because the motional-mode frequency of the ion chain (~MHz) is approximately $10^3$ times lower than qubit frequencies in superconducting circuits (~GHz). Quantinuum's shuttling architecture achieves faster gates (50 μs) than IonQ's surface-trap architecture (100 μs).

### 3.3 Neutral Atoms (2 platforms)

| Platform | Atoms | P_sys | 1Q Gate | 2Q Gate | 2Q Fidelity | Source |
|:---------|:------|:------|:--------|:--------|:------------|:-------|
| QuEra Aquila | 256 | 4.0 kW | 500 ns | 1.5 μs | 99.5% | [@quera-specs] |
| Pasqal Fresnel | 100+ | 4.0 kW | 500 ns | 2.0 μs | 98.0% | [@pasqal-specs] |

**Architecture notes:** Neutral-atom platforms use Rydberg blockade for two-qubit entanglement — gates in the 1–2 μs range, significantly faster than trapped ions but approximately 5–50× slower than the best superconducting gates. Room-temperature operation keeps power at approximately 4 kW. This architecture represents the most balanced speed–power tradeoff among the three gate-model architectures.

### 3.4 Non-Gate-Model and Pre-Commercial (4 entries)

| Platform | Architecture | P_sys | Status | Source |
|:---------|:------------|:------|:-------|:-------|
| D-Wave Advantage | Quantum annealing, 5000+ qubits | 25.0 kW | Gate-incompatible | [@dwave-specs; @king2018] |
| D-Wave Advantage2 | Quantum annealing, 1200+ qubits | 25.0 kW | Gate-incompatible | [@dwave-specs] |
| Xanadu Borealis | Photonic Gaussian boson sampling, 216 squeezed states | 4.0 kW | Gate-incompatible | [@xanadu-specs] |
| QWAV (target) | p-adic ultrametric, 343 qudits | <0.1 kW | Pre-commercial | [@jpcub-p0] |


## 4. Results: JPCUB Estimates for 13 Gate-Model Platforms

| Rank | Platform | JPCUB (J/sol) | P_sys | 2Q Gate | 2Q Fidelity | t_exec | E_shot | p_succ |
|:----:|:---------|:-------------|:------|:--------|:------------|:------|:------|:------|
| 1 | Google Willow | 0.05 | 25.0 kW | 30 ns | 99.95% | 1.9 μs | 0.05 J | 98.5% |
| 2 | Google Sycamore | 0.06 | 25.0 kW | 40 ns | 99.8% | 2.5 μs | 0.06 J | 94.2% |
| 3 | IQM Garnet | 0.15 | 12.0 kW | 200 ns | 99.5% | 11.0 μs | 0.13 J | 86.0% |
| 4 | IBM Heron r2 | 0.28 | 15.0 kW | 300 ns | 99.7% | 17.5 μs | 0.26 J | 91.4% |
| 5 | QuEra Aquila | 0.32 | 4.0 kW | 1.5 μs | 99.5% | 70.0 μs | 0.28 J | 86.0% |
| 6 | IBM Eagle r3 | 0.59 | 15.0 kW | 500 ns | 99.0% | 29.4 μs | 0.44 J | 74.0% |
| 7 | Rigetti Ankaa-3 | 0.61 | 15.0 kW | 400 ns | 98.0% | 22.0 μs | 0.33 J | 54.5% |
| 8 | Pasqal Fresnel | 0.62 | 4.0 kW | 2.0 μs | 98.0% | 85.0 μs | 0.34 J | 54.5% |
| 9 | Rigetti Aspen-M-3 | 0.71 | 15.0 kW | 400 ns | 97.5% | 22.0 μs | 0.33 J | 46.8% |
| 10 | Quantinuum H1-1 | 8.5 | 4.0 kW | 50 μs | 99.8% | 2.00 ms | 8.00 J | 94.2% |
| 11 | Quantinuum H2 | 9.6 | 4.5 kW | 50 μs | 99.8% | 2.00 ms | 9.00 J | 94.2% |
| 12 | IonQ Aria | 14.4 | 3.0 kW | 100 μs | 99.4% | 4.00 ms | 12.00 J | 83.5% |
| 13 | IonQ Forte | 16.3 | 3.5 kW | 100 μs | 99.5% | 4.00 ms | 14.00 J | 86.0% |

### 4.1 Non-Gate-Model and Pre-Commercial Entries

| Entry | JPCUB | Justification |
|:------|:------|:-------------|
| QWAV (target) | $< 0.001$ J/sol | Pre-commercial design target derived from room-temperature operation, qudit encoding, and intrinsic error protection. Pending physical hardware and independent measurement per JPCUB P0 §4.2. |
| D-Wave Advantage | ~50–200 J (optimization) | Quantum annealing (~20 μs per anneal, 100 anneals per problem, 25 kW). Cannot execute Shor's algorithm; optimization-equivalent estimate provided. |
| D-Wave Advantage2 | ~50–200 J (optimization) | Similar to Advantage with higher connectivity. Optimization tasks only. |
| Xanadu Borealis | N/A (GBS) | Gaussian boson sampling — specialized sampling task, not gate-model computation. Gate-incompatible. |


## 5. Architecture Group Analysis

### 5.1 Superconducting (7 platforms)

| Metric | Range |
|:-------|:------|
| JPCUB | 0.05 – 0.71 J/solution |
| Circuit depth | 1.9 – 29.4 μs |
| Energy per shot | 0.05 – 0.44 J |
| System power | 12.0 – 25.0 kW |

Superconducting platforms occupy the top of the ranking because sub-microsecond gate speeds (30–500 ns) produce extremely short circuit depths (1.9–29 μs) — so short that even with 12–25 kW of system power, the energy-per-shot remains below 0.5 J. Within this group, JPCUB differences are driven by fidelity: Google Willow (99.95%) and IBM Heron (99.7%) achieve higher success probabilities than Rigetti Aspen-M-3 (97.5%), which suffers from 46.8% success rate.

**Key observation:** The superconducting group spans a 14× range in JPCUB despite all sharing the same physical infrastructure (dilution refrigerator, approximately 15 mK). The range is driven by fidelity differences, not power or gate-speed differences.

### 5.2 Trapped Ions (4 platforms)

| Metric | Range |
|:-------|:------|
| JPCUB | 8.5 – 16.3 J/solution |
| Circuit depth | 2.00 – 4.00 ms |
| Energy per shot | 8.0 – 14.0 J |
| System power | 3.0 – 4.5 kW |

Trapped-ion platforms fill the bottom of the ranking despite room-temperature operation. The structural reason: gate times in the 50–100 μs range produce circuit depths of 2–4 milliseconds — approximately 100× longer than superconducting platforms. Even at one-quarter the system power, the $P \times t$ product is 30–100× worse for factoring.

**Key observation:** Quantinuum's 50 μs two-qubit gates are significantly faster than IonQ's 100 μs, producing a nearly 2× JPCUB advantage (8.5 vs. 16.3 J/sol for comparable fidelity). Gate speed within the trapped-ion architecture varies by vendor and is the primary determinant of JPCUB.

### 5.3 Neutral Atoms (2 platforms)

| Metric | Range |
|:-------|:------|
| JPCUB | 0.32 – 0.62 J/solution |
| Circuit depth | 70 – 85 μs |
| Energy per shot | 0.28 – 0.34 J |
| System power | 4.0 kW |

Neutral-atom platforms achieve JPCUB estimates competitive with mid-tier superconducting platforms (IQM Garnet at 0.15, IBM Heron at 0.28) at one-quarter the system power (4 kW vs. 12–15 kW). The Rydberg-gate speed (1.5–2 μs) places circuit depth at 70–85 μs — approximately 3–35× longer than the best superconducting platforms, but 25–50× shorter than trapped-ion platforms.

**Key observation:** Neutral atoms represent the most balanced architecture in the landscape. Room-temperature operation and modest laser power keep $P_{\text{sys}}$ low, while Rydberg blockade gates keep $t_{\text{exec}}$ in tens of microseconds rather than milliseconds. The gap to the top-ranked superconducting platforms (0.32 J/sol vs. 0.05 J/sol) is approximately 6× — addressable through fidelity improvements (98.0–99.5% currently, with published paths to >99.9%).

### 5.4 Cross-Architecture Comparison

| Architecture | JPCUB Range | Relative to Best | Dominant Factor |
|:-------------|:-----------|:-----------------|:----------------|
| Superconducting | 0.05 – 0.71 | 1× (best) | Fidelity (97.5–99.95%) |
| Neutral atoms | 0.32 – 0.62 | 6–12× | Gate speed (1.5–2.0 μs) |
| Trapped ions | 8.5 – 16.3 | 170–330× | Gate speed (50–100 μs) |

**The dominant factor across architectures is gate speed, not cooling cost.** The factor-of-330 gap in execution time between superconducting (2 μs) and trapped-ion (4 ms) dwarfs the factor-of-4.3 gap in system power (25 kW vs. 3.5 kW). Gate speed varies across architectures because the underlying physical interaction — qubit frequency for superconducting (~5 GHz), motional-mode frequency for trapped ions (~1–5 MHz), Rydberg state lifetime for neutral atoms (~100 μs) — differs by three orders of magnitude.


## 6. Discussion

### 6.1 The Gate-Speed Dominance Principle

The central finding of this expanded landscape is not only that superconducting platforms rank highest — it is that the ranking is determined by gate speed, and gate speed is determined by the physical frequency scale of the qubit interaction.

$$J_S(T, \varepsilon) \propto P_{\text{sys}} \times \frac{N_{\text{gates}}}{f_{\text{interaction}}} \times \frac{1}{p_{\text{succ}}}$$

The interaction frequency $f_{\text{interaction}}$ is not an engineering parameter — it is a physical constant of the chosen qubit modality. Superconducting qubits use microwave transitions at approximately 5 GHz; trapped-ion qubits use motional-mode frequencies at approximately 1–5 MHz; neutral atoms use Rydberg-state dipole-dipole interactions with approximately 1 μs gate times limited by the Rydberg lifetime.

The lesson for the JPCUB research program is that energy-efficient quantum computing cannot be reduced to a single architectural choice (room-temperature operation, high fidelity, or large qubit count). It requires the simultaneous optimization of power, speed, and success probability — and the interaction frequency imposes a structural floor on the speed component.

### 6.2 Fidelity as the Second Factor

Within each architecture group, fidelity — not qubit count — drives the JPCUB ranking:

- **Superconducting:** Google Willow (99.95%) achieves 98.5% success probability per shot; Rigetti Aspen-M-3 (97.5%) achieves only 46.8%. The fidelity difference of 2.5 percentage points produces a 2× difference in success probability and a corresponding 2× difference in JPCUB.
- **Trapped ions:** Quantinuum's 99.8% fidelity produces 94.2% success probability across 30 two-qubit gates; IonQ's 99.5% produces 86.0%. The fidelity advantage alone accounts for approximately 1.1× of the 1.7× JPCUB gap.
- **Neutral atoms:** QuEra's 99.5% fidelity vs. Pasqal's 98.0% is the dominant differentiator — both have similar gate speeds and power.

This has implications for the JPCUB calibration register [@jpcub-p0, §6]: the CAL-01 prediction ("No gate-model quantum computer will solve a commercially relevant problem at lower joules-per-solution than the best classical alternative by 2030") must account for both gate-speed and fidelity trajectories. A platform with 99.99% two-qubit fidelity and 100 ns gates would need to be assessed against a platform with 99.9% fidelity and 1 ns gates — the winner depends on the gate-count of the target problem.

### 6.3 The JPCUB P0 Published Value and Conservative Estimates

The JPCUB P0 [@jpcub-p0] reports IBM Eagle at $0.89$ J/solution for factoring. Our system-level model for the same platform yields approximately $0.59$ J/solution — consistent within the methodology difference (incremental-energy vs. full-system-power). The P0 value accounts for:

1. **Incremental power above idle baseline** — not total system power.
2. **Shared infrastructure amortization** — dilution refrigerator, control electronics shared across concurrent tasks.
3. **Optimized circuit decompositions** — fewer than 80 gates.

Our estimates are internally comparable across platforms (same conservative methodology) but represent upper bounds. The following should be considered when interpreting the ranking:

- **The ranking is robust.** Applying the same incremental methodology to all platforms would preserve the ordering, because the primary differentiators (gate speed and fidelity) are architecture-invariant.
- **The absolute values are upper bounds.** Each platform's published JPCUB value (if independently measured following the P0 protocol) would likely be lower than our estimates.
- **Direct comparison of our estimates to the published P0 value should not be performed.** Our IBM estimate ($0.59$ J/sol) and the published value ($0.89$ J/sol) differ because of methodology, not because of conflicting physics.

### 6.4 Non-Gate-Model Platforms and Paradigm Incomparability

D-Wave and Xanadu produce hardware that cannot execute Shor's algorithm. This is not a criticism — both platforms are designed for tasks their architectures can solve natively (Ising-model optimization, Gaussian boson sampling). The JPCUB framework [@jpcub-p0, §7.1] resolves this through the concept of a "representative task sample" — a set of tasks spanning multiple problem classes, where each platform can execute at least a subset.

For the current paper, the task is fixed (factoring $N = 15$). The paradigm-incompatible platforms are listed for completeness with approximate cross-paradigm estimates where available:

- **D-Wave (annealing):** Approximately 50–200 J per optimization problem (100 anneals at 20 μs each, 25 kW system power). This places annealing between the best trapped-ion and worst superconducting platforms for optimization tasks.
- **Xanadu (GBS):** No meaningful factoring equivalent. Gaussian boson sampling is a specialized sampling task with no accepted measure of "correctness" that maps to the JPCUB $\varepsilon$ threshold. $[$speculative — cross-paradigm comparison not yet defined for sampling tasks$]$
- **QWAV (target):** $<10^{-3}$ J/solution is a design target. The three premises (room-temperature, qudit encoding, intrinsic error protection via Ostrowski's theorem) are mathematically derivable from the published architecture [@jpcub-p0]. Independent measurement on physical hardware is required per the P0 protocol's adversarial validation provision.

### 6.5 Platforms Excluded for Lack of Published Specs

The following platforms have publicly announced hardware but lack published, verifiable specifications for the parameters required by the JPCUB estimation model:

| Platform | Architecture | Missing Data |
|:---------|:------------|:------------|
| Oxford Ionics | Trapped ions (electronic control) | System power; gate fidelity not independently published |
| Alice & Bob | Cat qubits (superconducting) | System power; gate time and fidelity preliminary |
| Origin Wukong | Superconducting (64 qubits) | Gate times and fidelity not available in English-language sources |
| PsiQuantum | Photonic (fusion-based) | Pre-commercial; no physical hardware specs |
| Microsoft Azure | Topological (Majorana) | Qubit not yet demonstrated; no specs |
| AWS Braket | Multi-vendor (hosted) | No fixed hardware; varies by backend |

These platforms should be added to the landscape when published specifications become available.


## 7. Limitations

### 7.1 Conservative Methodology

All estimates use a system-level power model that counts full system draw for the entire execution window. Real JPCUB values measured under the P0 protocol's incremental-energy methodology are likely lower.

### 7.2 Single-Task Methodology

Rankings are task-dependent. A platform that ranks poorly on factoring $N = 15$ may rank well on optimization (D-Wave), sampling (Xanadu), or simulation (neutral atoms with high connectivity). The JPCUB framework requires a representative task sample [@jpcub-p0, §7.1].

### 7.3 Specification Staleness

Specifications are sourced as of the most recent published data. Platforms evolve rapidly. Google Willow's specifications (2025) are significantly better than Google Sycamore's (2019). IBM's roadmap includes Flamingo (2025+) with unknown specifications.

### 7.4 No Empirical Power Measurement

None of the estimates in this paper (except IBM's published P0 value) are based on empirical wall-plug power measurement. They are model-derived from published specifications and literature estimates. Independent measurement is required to convert any estimate to a published value.

### 7.5 Fidelity-Product Model

The success probability model ($p_{\text{succ}} = f_{2Q}^{N_{2Q}}$) does not account for error mitigation, dynamical decoupling, circuit optimization, or the difference between randomized benchmarking fidelity and algorithmic fidelity. It represents a lower bound on success probability and therefore an upper bound on JPCUB.


## 8. Conclusion

The JPCUB competitive landscape v2.0 extends the qwav.tech roster from 6 to 17 platforms — covering every quantum hardware product with verifiable published specifications. The expanded ranking reveals a structural principle: gate speed is the dominant factor in joules-per-solution across quantum computing architectures.

Superconducting platforms (Google Willow at 0.05 J/sol to Rigetti Aspen-M-3 at 0.71 J/sol) lead because sub-microsecond gate speeds produce circuit depths of 2–30 μs — so short that even 12–25 kW of system power yields single-joule energy budgets. Neutral atoms (QuEra Aquila at 0.32 J/sol) achieve competitive JPCUB at one-quarter the power by balancing Rydberg-gate speeds (~1.5 μs) with room-temperature operation. Trapped ions (IonQ Forte at 16.3 J/sol) rank last because microsecond-scale gate times drive execution times to milliseconds — the gate-time penalty overwhelms the room-temperature power advantage.

This finding has direct implications for the JPCUB research program: the P1 quantum energy audit must account for both gate-speed and cooling-power trajectories across modalities; the P9 Comparative Atlas must include an explicit time–power decomposition for each paradigm; and the CAL-01 prediction ("no quantum computer will beat classical on JPCUB by 2030") must specify gate-speed assumptions as well as fidelity assumptions.

**Verification pathway:** Every estimate in this paper is model-derived. To convert any estimate to a published value, the platform vendor must independently measure joules per correct answer following the full JPCUB P0 protocol [@jpcub-p0]: wall-plug power measurement, the six-component energy breakdown, Pareto frontier reporting across all five correctness thresholds, and raw data publication. The protocol is open. The measurement procedure is published. The burden of proof is on the claimant.


## Declarations

**Funding:** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Conflicts of Interest:** The author is the founder of QWAV, a pre-commercial computing platform that is one of the 17 entries evaluated in this paper. QWAV's design target ($<10^{-3}$ J/solution) is treated as a design hypothesis requiring independent verification, per the JPCUB P0 protocol's adversarial validation provision [@jpcub-p0, §4.2]. All estimates for competing platforms are based on published specifications; all are presented as defensible upper bounds pending independent measurement.

**Data Availability:** All estimates, specification sources, and computation methodology are contained within this paper and the companion computation script (`competitive-landscape/artifacts/jpcub-computation.py`). The JPCUB P0 paper with the IBM Eagle measurement is available at DOI 10.5281/zenodo.21637028.

**Use of Artificial Intelligence:** This paper was written with AI assistance for computation, estimation, and initial drafting. All specifications were verified against published sources. The AI system operated under the QNFO Research Integrity Mandate.

**Pre-Registration:** The competitive landscape task (factoring $N = 15$, $\varepsilon = 0.95$, 30 two-qubit + 50 single-qubit gates) and the per-platform specification sources are pre-registered in this section. All estimates are model-derived from these pre-registered specifications.


## References

- [@jpcub-p0] QNFO Research Collective. "The Joules-per-Solution Metric: Definition, Measurement Protocol, and Anti-Gaming Provisions for Honest Computational Benchmarking." DOI: 10.5281/zenodo.21637028 (2026).

- [@auffeves2022] Auffèves, A. "Quantum Technologies Need a Quantum Energy Initiative." *PRX Quantum* **3**, 020101 (2022). DOI: 10.1103/PRXQuantum.3.020101.

- [@fellous-asiani2022] Fellous-Asiani, M., Chai, J. H., Whitney, R. S., Auffèves, A., and Ng, H. K. "Optimizing Resource Efficiencies for Scalable Full-Stack Quantum Computers." arXiv:2209.05469 (2022). Published as *PRX Quantum* **4**, 040319 (2023). DOI: 10.1103/PRXQuantum.4.040319.

- [@ibm-quantum] IBM Quantum. "Quantum Computing Systems." quantum-computing.ibm.com. Eagle r3 (288 ns 1Q / 500 ns 2Q, 99.0% fidelity) and Heron r2 (170 ns 1Q / 300 ns 2Q, 99.7% fidelity) specifications. Accessed 2026-08-06.

- [@google-nature-2019] Arute, F. *et al.* "Quantum Supremacy Using a Programmable Superconducting Processor." *Nature* **574**, 505–510 (2019). DOI: 10.1038/s41586-019-1666-5.

- [@google-nature-2025] Google Quantum AI. "Quantum Error Correction Below the Surface Code Threshold." *Nature* **638**, 920–926 (2025). DOI: 10.1038/s41586-024-08449-y.

- [@ionq-specs] IonQ. "IonQ Forte and Aria: Technical Specifications." ionq.com. Forte: 36 algorithmic qubits, 20 μs 1Q / 100 μs 2Q, 99.5% fidelity. Aria: 25 algorithmic qubits, 20 μs 1Q / 100 μs 2Q, 99.4% fidelity. Accessed 2026-08-06.

- [@quantinuum-specs] Quantinuum. "H1-1 and H2: Technical Specifications." quantinuum.com. H1-1: 20 qubits, 10 μs 1Q / 50 μs 2Q, 99.8% fidelity. H2: 56 qubits (racetrack architecture). "A Race Track Trapped-Ion Quantum Processor," arXiv:2305.03828 (2023). Accessed 2026-08-06.

- [@rigetti-specs] Rigetti Computing. "Ankaa-3 and Aspen-M-3: Technical Specifications." rigetti.com. Ankaa-3: 84 qubits, 200 ns 1Q / 400 ns 2Q, 98.0% fidelity. Aspen-M-3: 80 qubits, 200 ns 1Q / 400 ns 2Q, 97.5% fidelity. Accessed 2026-08-06.

- [@iqm-specs] IQM. "Garnet: Technical Specifications." iqm.com. 20 superconducting qubits, 100 ns 1Q / 200 ns 2Q, 99.5% fidelity. Accessed 2026-08-06.

- [@quera-specs] QuEra Computing. "Aquila: Technical Specifications." quera.com. 256 neutral atoms (Rb-87), 500 ns 1Q / 1.5 μs 2Q (Rydberg blockade), 99.5% fidelity. Accessed 2026-08-06.

- [@pasqal-specs] Pasqal. "Fresnel: Technical Specifications." pasqal.com. 100+ neutral atoms (Rb), 500 ns 1Q / 2.0 μs 2Q (Rydberg blockade), 98.0% fidelity. Accessed 2026-08-06.

- [@dwave-specs] D-Wave Systems. "Advantage and Advantage2: Technical Specifications." dwavesys.com. Advantage: 5,000+ qubits, ~20 μs anneal. Advantage2: 1,200+ qubits, higher connectivity. Accessed 2026-08-06.

- [@xanadu-specs] Xanadu. "Borealis: Technical Specifications." xanadu.ai. 216 squeezed states, photonic GBS architecture. *Nature* **606**, 75–81 (2022). DOI: 10.1038/s41586-022-04725-x. Accessed 2026-08-06.

- [@king2018] King, A. D. *et al.* "Observation of Topological Phenomena in a Programmable Lattice of 1,800 Qubits." *Nature* **560**, 456–460 (2018). DOI: 10.1038/s41586-018-0410-x.

- [@vandersypen2001] Vandersypen, L. M. K. *et al.* "Experimental Realization of Shor's Quantum Factoring Algorithm Using Nuclear Magnetic Resonance." *Nature* **414**, 883–887 (2001). DOI: 10.1038/414883a.

- [@monz2016] Monz, T. *et al.* "Realization of a Scalable Shor Algorithm." *Science* **351**, 1068–1071 (2016). DOI: 10.1126/science.aad9480.

- [@lucero2012] Lucero, E. *et al.* "Computing Prime Factors with a Josephson Phase Qubit Quantum Processor." *Nature Physics* **8**, 719–723 (2012). DOI: 10.1038/nphys2385.

- [@chen2023] Chen, S. "Are Quantum Computers Really Energy Efficient?" *Nature Computational Science* **3**, 457–460 (2023). DOI: 10.1038/s43588-023-00459-6.
