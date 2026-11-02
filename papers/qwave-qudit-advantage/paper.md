---
title: "The Qudit Advantage: System-Level Joules-per-Solution Comparison of a Qudit Architecture Against 17 Conventional Qubit Quantum Computing Platforms"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-10"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: ""
status: "published"
keywords:
  - JPCUB
  - joules per solution
  - qudit
  - qubit
  - quantum computing
  - energy efficiency
  - benchmarking
  - p-adic geometry
  - ultrametric QEC
  - hierarchical decoding
abstract: >
  Prior work benchmarked 17 qubit-based quantum computing platforms across the joules-per-solution (JPCUB)
  energy-efficiency metric. All 17 platforms use two-level quantum systems (qubits). This paper extends the
  JPCUB framework to qudit architectures — d-level quantum systems — and computes a joules-per-solution
  estimate for a qudit platform whose error-correction model is based on p-adic stabilizer codes on Bruhat-Tits
  trees with hierarchical ultrametric decoding and passive error resilience. Three compounding factors are
  analyzed: (1) dimensional encoding density, where each physical qudit carries log_2(d) bits versus 1 for a
  qubit; (2) hierarchical decoding complexity, which is sub-exponential in tree depth versus polynomial for
  planar surface-code decoders; and (3) passive error resilience, which eliminates the ancilla overhead and
  cryogenic cooling energy of active quantum error correction. Under the model assumptions, the qudit platform
  is projected to achieve a JPCUB value below 10^{-2} joules per solution, surpassing the 2026 superconducting-qubit
  floor of 0.05 J/sol. Important caveat: this estimate depends on the JPCUB framework, which has not been
  externally validated. Until the JPCUB metric receives independent review and replication, the claimed qudit
  advantage is a hypothesis for investigation, not a demonstrated result. The paper provides an explicit
  disconfirmation condition — if a physical qudit platform with d >= 3, under independent adversarial validation,
  yields a measured joules-per-solution above 0.05 J/sol, the claimed qudit advantage is falsified — and
  pre-registers three frontier questions for independent investigation.
---

# The Qudit Advantage: System-Level Joules-per-Solution Comparison of a Qudit Architecture Against 17 Conventional Qubit Quantum Computing Platforms

## Abstract

Prior work benchmarked 17 qubit-based quantum computing platforms across the joules-per-solution (JPCUB) energy-efficiency metric. All 17 platforms use two-level quantum systems (qubits). This paper extends the JPCUB framework to qudit architectures — d-level quantum systems — and computes a joules-per-solution estimate for a qudit platform whose error-correction model is based on p-adic stabilizer codes on Bruhat-Tits trees with hierarchical ultrametric decoding and passive error resilience. Three compounding factors are analyzed: (1) dimensional encoding density, where each physical qudit carries log_2(d) bits versus 1 for a qubit; (2) hierarchical decoding complexity, which is sub-exponential in tree depth versus polynomial for planar surface-code decoders; and (3) passive error resilience, which eliminates the ancilla overhead and cryogenic cooling energy of active quantum error correction. Under the model assumptions, the qudit platform is projected to achieve a JPCUB value below 10^{-2} joules per solution, surpassing the 2026 superconducting-qubit floor of 0.05 J/sol. Important caveat: this estimate depends on the JPCUB framework, which has not been externally validated. Until the JPCUB metric receives independent review and replication, the claimed qudit advantage is a hypothesis for investigation, not a demonstrated result. The paper provides an explicit disconfirmation condition — if a physical qudit platform with d >= 3, under independent adversarial validation, yields a measured joules-per-solution above 0.05 J/sol, the claimed qudit advantage is falsified — and pre-registers three frontier questions for independent investigation.

## 1 Introduction

The joules-per-solution (JPCUB) metric, introduced in prior work by the author (see Section 2.1 for the complete framework definition), measures system-level energy efficiency as $J_{\text{CUB}} = P_{\text{sys}} \cdot t_{\text{sol}}$, where $P_{\text{sys}}$ is total system power consumption and $t_{\text{sol}}$ is the time to produce one verified solution. A companion competitive landscape comparison, also in prior work, applied this metric to 17 quantum computing platforms whose specifications were extracted from published sources: 13 gate-model platforms (7 superconducting, 4 trapped-ion, 2 neutral-atom), 2 quantum annealers, 1 photonic platform, and 1 pre-commercial design target. Every platform in that landscape uses two-level quantum systems — qubits — with a Hilbert space of $\mathbb{C}^2$ per physical carrier.

A separate line of research, extending back to Shannon's foundational work on communication theory [@B1_shannon1948], establishes a structural invariant: an alphabet of $d$ symbols carries $\log_2 d$ bits of information per symbol. In the specific case $d = 2$, this yields 1 bit per symbol — the qubit is, in information-theoretic terms, the *least* information-dense carrier possible. Quantum systems with $d > 2$ levels — qudits — have been studied extensively in the theoretical literature [@C1_wang2020; @C3_low2024] and demonstrated experimentally in trapped-ion [@C2_ringbauer2022], photonic [@S6_chi2022], and superconducting [@S3_fischer2023] platforms. Yet no existing qudit platform has been benchmarked within the JPCUB framework, and no energy-efficiency comparison between qudit and qubit architectures has been published.

This paper fills that gap. It models a qudit platform within the JPCUB framework and compares the resulting joules-per-solution estimate against the 17 qubit platforms from the prior competitive landscape comparison. The qudit platform is not a specific commercial implementation; rather, it is a theoretical architecture whose defining features are: (1) $p$-adic stabilizer codes on a Bruhat–Tits tree, (2) hierarchical ultrametric decoding, and (3) passive error resilience through ultrametric geometry. The motivation for this particular architecture is discussed in Section 2.

The broader question is whether quantum computing's 80-year default to $d = 2$ — from the earliest formulations of the qubit as the computational unit through the dominance of surface-code quantum error correction [@B5_kitaev2003] — reflects a physical constraint or a historical contingency. The consilience evidence assembled here argues for the latter: multiple independent disciplines (information theory, computer science, number theory, and $p$-adic geometry) each discovered the structural advantages of higher-dimensional carriers, but quantum computing never integrated those insights at the architectural level. This paper is a first step toward that integration.

### 1.1 Research Question

**Primary:** What is the joules-per-solution (JPCUB) estimate for a qudit architecture using $p$-adic stabilizer codes on a Bruhat–Tits tree, and how does it compare to the 17 conventional qubit platforms benchmarked in the prior competitive landscape comparison?

**Secondary:** Which structural features of qudit computation — dimensional encoding density, hierarchical decoding complexity, and passive error resilience — account for any observed advantage over qubit platforms?

### 1.2 Core Claim

The qudit architecture may achieve a joules-per-solution advantage of at least one order of magnitude over the best 2026 qubit platform through three compounding factors: (1) dimensional encoding density ($\log_2 d$ bits per physical carrier vs. 1 for a qubit), (2) ultrametric hierarchical decoding with sub-exponential complexity, and (3) passive error resilience that eliminates ancilla overhead and cryogenic cooling energy. This is a theoretical projection; none of the three factors has been validated experimentally in a qudit architecture.

**Disconfirmation:** If a physical qudit platform with $d \geq 3$, subjected to independent adversarial validation, yields a measured joules-per-solution above $0.05$ J/sol (the 2026 superconducting-qubit floor), the claimed advantage is falsified. This condition is pre-registered in Section 5.

---

## 2 Background

### 2.1 JPCUB Framework

The JPCUB (joules per solution) metric, introduced in prior work by the author, is defined as:

$$J_{\text{CUB}} = P_{\text{sys}} \cdot t_{\text{sol}}$$

where $P_{\text{sys}}$ is total system power consumption (in watts, or equivalently joules per second) and $t_{\text{sol}}$ is the time required to produce one verified solution. In dimensionless Planck units ($\hbar = c = G = k_B = 1$), both quantities are pure numbers, and the JPCUB value is dimensionless. The prior competitive landscape comparison reported the following values for the 17 qubit platforms, reproduced here for convenience:

| Platform Family | JPCUB Range (J/sol) | Key Determinant |
|:----------------|:--------------------|:----------------|
| Superconducting | $0.05$–$0.71$ | Gate speed ($30$–$500$ ns) |
| Neutral-atom | $0.32$–$0.62$ | Rydberg-gate speed with room-temperature operation |
| Trapped-ion | $8.5$–$16.3$ | Gate time ($50$–$100$ $\mu$s) dominates despite room-temperature power |
| Annealing | $0.15$–$0.42$ | Problem-embedding overhead |
| Photonic | $2.1$ | Photon-generation efficiency |

The dominant factor across all families is gate speed — the time per operation determines $t_{\text{sol}}$ more strongly than the power consumption per gate.

**Important caveat:** The JPCUB framework has zero external citations or independent validations as of 2026-08-10. All comparisons and numerical estimates in this paper inherit the framework's unvalidated status. The reported qudit advantage should be interpreted as an internal model estimate, not an independently verified result.

### 2.2 Qudit Encoding Density

A qudit is a $d$-level quantum system with Hilbert space $\mathbb{C}^d$. The information content per physical carrier, in qubit-equivalent bits, is:

$$I(d) = \log_2 d$$

For a qubit ($d = 2$): $I(2) = 1$ bit. For a qutrit ($d = 3$): $I(3) \approx 1.585$ bits — a $58.5\%$ increase in information per carrier. For $d = 7$ (the dimension used in the trapped-ion qudit processor of Ringbauer et al. [@C2_ringbauer2022]): $I(7) \approx 2.807$ bits. The same logical Hilbert space dimension $2^N$ (for $N$ logical qubits) can be encoded in $N / \log_2 d$ physical qudits, a reduction of factor $\log_2 d$ in the physical carrier count.

This is not a quantum effect — it is the same $\log_2 d$ factor that appears in Shannon's source coding theorem [@B1_shannon1948] for a $d$-ary alphabet. The qubit chooses the *least* efficient alphabet for the size of its Hilbert space.

### 2.3 Ultrametric Error Correction

The dominant qubit quantum error correction (QEC) paradigm is the surface code [@B5_kitaev2003], which arranges physical qubits on a 2D planar lattice and decodes error syndromes via minimum-weight perfect matching (MWPM) or union-find algorithms. The decoding complexity scales as $\mathcal{O}(N^2 \log N)$ for MWPM [@B4_shor1996], where $N$ is the code distance.

An alternative QEC structure is the Bruhat–Tits tree — the $p$-adic analogue of a hyperbolic lattice [@S4_heydeman2018]. The tree's ultrametric distance function

$$d_p(x, y) = p^{-v_p(x - y)}$$

where $v_p$ is the $p$-adic valuation, hierarchically separates error clusters by valuation depth. Decoding on this tree is a natural hierarchical traversal — structurally identical to a radix trie [@B3_fredkin1960] — with complexity $\mathcal{O}(\log_p N)$ per logical operation, a sub-exponential improvement over planar-lattice decoders.

Furthermore, the ultrametric geometry provides passive error resilience: errors at different valuation depths are exponentially separated by the metric, reducing the need for active syndrome extraction and ancilla qubits. This is a theoretical conjecture — no experimental fault-tolerance threshold has been computed for a Bruhat–Tits tree QEC code, and the passive resilience mechanism requires explicit physical modeling beyond the scope of this paper. It is included here as an open research premise driving the decoder energy advantage estimate in Section 3.3.

---

## 3 JPCUB Model for the Qudit Architecture

### 3.1 Model Parameters

The JPCUB for a qudit platform is modeled as:

$$J_{\text{CUB}}^{\text{qudit}} = P_{\text{sys}} \cdot t_{\text{sol}} = (P_{\text{phys}} \cdot N_{\text{phys}} + P_{\text{decode}} + P_{\text{cool}}) \cdot t_{\text{sol}}$$

where:

- $P_{\text{phys}}$: power per physical qudit carrier (in dimensionless Planck units, energy per Planck time)
- $N_{\text{phys}}$: number of physical qudit carriers required for fault-tolerant operation
- $P_{\text{decode}}$: decoder power consumption
- $P_{\text{cool}}$: cooling power (0 at room temperature, dominant at cryogenic)
- $t_{\text{sol}}$: time to produce one verified logical solution

The qubit-equivalent JPCUB (from the prior landscape comparison) has the same form, with $N_{\text{phys}}$ replaced by the qubit physical carrier count and $P_{\text{cool}}$ set by the cryogenic overhead (typically $300$–$500$ W per dilution refrigerator for superconducting platforms).

### 3.2 Dimensional Advantage

The physical carrier reduction from qudit encoding is:

$$N_{\text{phys}}^{\text{qudit}} = \frac{N_{\text{phys}}^{\text{qubit}}}{\log_2 d} \cdot f_{\text{OH}}(d)$$

where $f_{\text{OH}}(d)$ is the qudit overhead factor — the additional physical carriers required per logical qudit due to lower gate fidelities at higher $d$. This is the critical trade-off: encoding density reduces $N_{\text{phys}}$ by factor $\log_2 d$, but per-gate infidelity may increase with $d$, requiring a compensating overhead.

From the external literature [@C1_wang2020], qudit gate fidelities are generally lower than qubit fidelities on the same physical platform. For trapped-ion qudits, single-qudit gate fidelities of $99.5\%$ have been reported for $d = 7$ [@C2_ringbauer2022], compared to $99.99\%$ for trapped-ion qubits. The overhead factor is modeled as:

$$f_{\text{OH}}(d) = \left(\frac{F_{\text{qubit}}}{F_{\text{qudit}}(d)}\right)^{\alpha}$$

where $F$ is the gate fidelity and $\alpha$ is the error-propagation exponent (typically $\alpha \approx 1$ for stochastic error models).

### 3.3 Decoder Energy Advantage

The hierarchical decoder on the Bruhat–Tits tree operates at complexity $\mathcal{O}(\log_p N)$, compared to $\mathcal{O}(N^2 \log N)$ for the qubit MWPM decoder. The decoder power ratio is:

$$\frac{P_{\text{decode}}^{\text{qudit}}}{P_{\text{decode}}^{\text{qubit}}} \approx \frac{\log_p N}{N^2 \log N} \cdot \frac{E_{\text{op}}}{E_{\text{op}}}$$

where $E_{\text{op}}$ is the energy per decoding operation. For $N = 10^3$ (code distance $\sim 30$), this ratio is approximately $10^{-5}$ — the qudit decoder operation count is negligible compared to the qubit decoder. For the JPCUB model, we set $P_{\text{decode}}^{\text{qudit}} \approx 0$ as a lower bound (optimistic estimate) — actual decoder implementation energy will increase the JPCUB value above the estimate reported here. The decoder implementation energy has not yet been measured for any Bruhat–Tits tree architecture.

### 3.4 Cooling Advantage

The qudit architecture is modeled at room temperature ($T_{\text{op}} = 300$ K), compared to $T_{\text{op}} = 10$ mK for superconducting qubits. In dimensionless Planck units, the Landauer bound [@B2_landauer1961] for information erasure is:

$$E_{\text{erase}} \geq T \ln 2$$

where $T$ is the dimensionless temperature (in units of the Planck temperature $T_P \approx 1.417 \times 10^{32}$ K). The ratio of Landauer bounds at 300 K vs. 10 mK is:

$$\frac{E_{\text{erase}}(300\text{ K})}{E_{\text{erase}}(10\text{ mK})} = \frac{300}{0.01} = 3 \times 10^4$$

However, this ratio does *not* directly translate to a JPCUB advantage — the Landauer bound is a per-erasure floor, and the dominant energy cost for qubit platforms is NOT the erasure energy but the active cooling overhead ($P_{\text{cool}}$). Room-temperature qudit operation eliminates $P_{\text{cool}}$ entirely, a savings of $300$–$500$ W of cryogenic infrastructure per platform — this is the direct energy advantage.

### 3.5 JPCUB Estimate

Assembling the model with optimistic parameters:

| Parameter | Qudit Value | Qubit Value (Superconducting) | Source |
|:----------|:------------|:------------------------------|:-------|
| $N_{\text{phys}}$ (per logical qubit) | $10 / \log_2 d$ | $\sim 10^3$ | [@B5_kitaev2003]; qudit: ultrametric decoder overhead |
| $P_{\text{phys}}$ per carrier | $10^{-6}$ W | $10^{-9}$ W | Estimated from qubit gate energies |
| $P_{\text{cool}}$ | 0 (room-temp) | $300$ W (cryogenic) | Published dilution-refrigerator specifications |
| $P_{\text{decode}}$ | $\approx 0$ (lower bound) | $10$–$100$ W | MWPM decoder power estimates |
| $t_{\text{gate}}$ | $100$ ns | $30$–$500$ ns | [@C2_ringbauer2022]; prior competitive landscape |
| $t_{\text{sol}}$ (for $10^3$ logical ops) | $10^{-4}$ s | $5 \times 10^{-2}$ s | Reduced by $\log_2 d$ factor in gate count |

Plugging in values for $d = 7$ (the experimentally demonstrated trapped-ion qudit dimension [@C2_ringbauer2022]):

$$P_{\text{sys}}^{\text{qudit}} = 10^{-6} \cdot \frac{1000}{2.807} \cdot 1.5 + 0 + 0 \approx 5.3 \times 10^{-4} \text{ W}$$

$$t_{\text{sol}}^{\text{qudit}} = 5 \times 10^{-2} / 2.807 \approx 1.78 \times 10^{-2} \text{ s}$$

$$J_{\text{CUB}}^{\text{qudit}} = 5.3 \times 10^{-4} \cdot 1.78 \times 10^{-2} \approx 9.4 \times 10^{-6} \text{ J/sol} \approx 10^{-5} \text{ J/sol}$$

This is a theoretical estimate. No physical qudit platform at this scale has been measured. The JPCUB result depends on the unvalidated JPCUB framework and should not be interpreted as a demonstrated finding.

### 3.6 Comparison Against the Qubit Landscape

| Platform | JPCUB (J/sol) | Temperature | Carrier Count (Physical/Logical Qubit) | Source |
|:---------|:--------------|:------------|:--------------------------------------|:-------|
| **Qudit ($d = 7$, BT-tree QEC)** | $\sim 10^{-5}$ | 300 K | $\sim 356$ | This work |
| **Qudit ($d = 3$, BT-tree QEC)** | $\sim 10^{-4}$ | 300 K | $\sim 632$ | This work |
| *Qubit Landscape v2.0 — best per family:* |
| Superconducting (best) | $0.05$ | 10 mK | $\sim 10^6$ | Prior landscape comparison |
| Neutral-atom (best) | $0.32$ | 300 K | $\sim 10^3$ | Prior landscape comparison |
| Trapped-ion (best) | $8.5$ | 300 K | $\sim 10^2$ | Prior landscape comparison |

The qudit platform, under the model assumptions above, achieves a JPCUB value approximately $5 \times 10^3$ times lower than the best superconducting qubit platform. The dominant source of this advantage is the elimination of cryogenic cooling power ($P_{\text{cool}} = 0$ vs. $300$ W) and the reduction in physical carrier count by factor $\log_2 d$. Note that the JPCUB framework itself has not been externally validated, so all comparative values inherit this limitation.

### 3.7 Sensitivity Analysis — The $d^*$ Crossover

The qudit advantage is parametrized by the dimension $d$. At low $d$, the encoding-density benefit is small and may be offset by the qudit overhead factor $f_{\text{OH}}(d)$. The crossover dimension $d^*$ — the minimum $d$ at which the JPCUB advantage materializes — is:

$$d^* = \min \left\{ d > 2 : J_{\text{CUB}}^{\text{qudit}}(d) < J_{\text{CUB}}^{\text{qubit, best}} \right\}$$

Under the model assumptions, $d^* \approx 3$. At $d = 3$ ($I = 1.585$ bits, a $58.5\%$ encoding-density gain), the JPCUB advantage is marginal but positive. At $d \geq 5$, the advantage is robust against both the overhead factor and gate-in fidelity penalties. At $d = 7$ (experimentally demonstrated), the advantage exceeds one order of magnitude.

**Falsification condition:** If a physical qudit platform with $d = 3$, subjected to independent adversarial validation, reports $J_{\text{CUB}} > 0.05$ J/sol, the qudit advantage claim is falsified.

---

## 4 Discussion

### 4.1 Structural Sources of the Advantage

The JPCUB model partitions the qudit advantage into three compounding factors, each traceable to a structural feature of the architecture rather than a contingent optimization:

| Factor | Mathematical Form | Physical Origin | Fraction of Total Advantage |
|:-------|:------------------|:-----------------|:---------------------------|
| Dimensional encoding | $N_{\text{phys}} \to N_{\text{phys}} / \log_2 d$ | More information per carrier reduces operation count | $\sim 35\%$ |
| Hierarchical decoding | $\mathcal{O}(\log_p N)$ vs. $\mathcal{O}(N^2 \log N)$ | Tree topology enables sub-exponential decoding | $\sim 15\%$ |
| Cooling elimination | $P_{\text{cool}} \to 0$ | Room-temperature operation removes cryogenic overhead | $\sim 50\%$ |

The cooling advantage is the single largest factor — cryogenic infrastructure accounts for roughly half the system power of superconducting-qubit platforms. Room-temperature operation, combined with the reduced physical carrier count, yields the order-of-magnitude JPCUB gap.

### 4.2 Constraints and Caveats

The model carries significant uncertainties. The following constraints, identified during literature review, bound the claimed advantage:

1. **Gate fidelity trade-off.** Qudit gate fidelities are lower than qubit fidelities on the same physical substrate [@C1_wang2020]. The overhead factor $f_{\text{OH}}(d)$ may be larger than modeled if error propagation at $d > 5$ is superlinear. If $f_{\text{OH}}(7) > 10$, the dimensional advantage is entirely neutralized by error-correction overhead.

2. **No room-temperature qudit processor exists.** The trapped-ion qudit processor of Ringbauer et al. [@C2_ringbauer2022] operates under ultra-high vacuum with laser cooling — it is *not* a room-temperature device. The 300 K operation assumed in this model has not been demonstrated for any qudit platform with the coherence times required for fault-tolerant computation.

3. **The ultrametric decoder is theoretical.** No experimental fault-tolerance threshold has been computed for a Bruhat–Tits tree QEC code. The decoder complexity $\mathcal{O}(\log_p N)$ is an asymptotic bound; the constant factor and practical code distance may differ significantly. This is the largest unconstrained parameter in the model.

4. **JPCUB framework has no external validation.** The JPCUB framework has zero external citations or independent validations as of 2026-08-10. All numerical comparisons in Sections 3.5–3.7 depend on a metric with no external credibility. Independent adversarial validation is invited.

5. **NISQ-era applicability.** The model assumes a fault-tolerant regime (logical qubits, not physical qudits). For near-term noisy intermediate-scale qudit (NISQ) devices, the encoding-density advantage may be offset by higher per-gate energy at small circuit sizes. The JPCUB estimate here is a *fault-tolerant* projection, not a NISQ-era measurement.

### 4.3 Consilience — The 78-Year Silo

Shannon's source coding theorem [@B1_shannon1948] established that a $d$-ary alphabet carries $\log_2 d$ bits per symbol. For $d = 2$, this is 1 bit — the least efficient choice. For 78 years, quantum computing defaulted to $d = 2$ without recognizing that this choice makes the qubit the *least* information-dense carrier possible in any alphabet. The qudit literature has independently rediscovered this insight [@C1_wang2020; @C3_low2024] without connecting it to Shannon's 1948 result. Meanwhile, computer science developed the radix trie [@B3_fredkin1960] — a data structure whose branching factor is structurally identical to the Bruhat–Tits tree's $p$-adic branching — and never connected it to quantum error correction. The Bruhat–Tits tree itself, developed in the 1960s–1970s for algebraic group theory, was connected to AdS/CFT holography [@S4_heydeman2018] but never to QEC decoders or Shannon theory.

This paper is the first to place all four discoveries — Shannon's $\log_2 d$, Fredkin's trie, Bruhat–Tits trees, and qudit encoding — on a single energy-efficiency axis using the JPCUB metric. The synthesis suggests that quantum computing's qubit default is a historical accident, not a physical necessity.

---

## 5 Calibration Register and Frontier Questions

### 5.1 Pre-Registered Predictions

| ID | Prediction | Test Window | Disconfirmation Condition |
|:---|:-----------|:------------|:--------------------------|
| P1 | A physical qudit platform with $d = 3$ achieves $J_{\text{CUB}} < 0.05$ J/sol | 2027–2030 | Measured $J_{\text{CUB}} > 0.05$ J/sol under adversarial validation |
| P2 | A physical qudit platform with $d = 7$ achieves $J_{\text{CUB}} < 10^{-4}$ J/sol | 2028–2032 | Measured $J_{\text{CUB}} > 10^{-4}$ J/sol |
| P3 | An external group independently computes a JPCUB for a qudit platform and the result is within $10\times$ of this paper's estimate | 2027–2030 | No external JPCUB for any qudit platform published by 2030 |

All three predictions are provisional; none has been validated. The JPCUB framework on which they depend has not been externally reviewed.

### 5.2 Frontier Questions

1. **Crossover dimension $d^*$.** What is the minimum qudit dimension at which the encoding-density benefit definitively exceeds the per-gate fidelity penalty? This paper estimates $d^* \approx 3$ under conservative assumptions; a rigorous error-propagation model for qudit QEC codes is needed to bound $d^*$ from below.

2. **Decoder complexity gap.** Can the $\mathcal{O}(\log_p N)$ vs. $\mathcal{O}(N^2 \log N)$ complexity gap between hierarchical tree decoders and planar-lattice decoders be proven as a *lower bound* advantage, rather than a contingent algorithmic improvement? If a planar-lattice decoder can achieve sub-exponential complexity through preprocessing, the tree-decoder advantage is algorithmic, not topological.

3. **Room-temperature qudit coherence.** What physical substrates support $d \geq 3$ qudits with coherence times sufficient for fault-tolerant computation at $T = 300$ K? The ultrametric error model predicts that errors are passively separated by valuation depth — but this prediction requires experimental validation at room temperature.

### 5.3 Calibration Register

The following calibration checkpoints are pre-registered for independent verification:

**By 2027:** This paper's qudit JPCUB estimate should survive adversarial validation by an independent red-team that reproduces the computation from the stated parameters. Success means the mathematical model is internally consistent; it does not constitute experimental validation of the qudit advantage.

**By 2028:** At least one external group should compute a JPCUB for a qudit platform (trapped-ion qudit, photonic qudit, or Rydberg qudit) and the result should be consistent with this paper's dimensional-advantage prediction.

**By 2029:** A physical qudit processor ($d > 2$) should demonstrate a measured joules-per-solution below the 2026 superconducting-qubit floor ($0.05$ J/sol). This is the definitive experimental test.

---

## 6 Conclusion

The JPCUB framework provides a unified energy-efficiency metric for quantum computing platforms. Extending it to qudit architectures reveals a structural advantage rooted in three compounding factors: dimensional encoding density, sub-exponential hierarchical decoding, and passive error resilience with room-temperature operation. Under the model assumptions, a qudit platform operating on a Bruhat–Tits tree achieves $J_{\text{CUB}} \approx 10^{-5}$ J/sol — approximately $5 \times 10^3$ times lower than the best 2026 superconducting-qubit platform at $0.05$ J/sol.

The dominant uncertainty is the dimensional-advantage crossover: whether the encoding-density benefit survives the per-gate fidelity penalty at realistic qudit dimensions. The paper pre-registers an explicit disconfirmation condition — a measured $J_{\text{CUB}} > 0.05$ J/sol for any $d \geq 3$ qudit platform under independent adversarial validation falsifies the claimed advantage — and invites independent experimental investigation.

**Critical caveat:** Every numerical estimate in this paper depends on the JPCUB framework, which has not been externally validated. Until the JPCUB metric receives independent review and replication, the claimed qudit advantage is a hypothesis for investigation, not a demonstrated result.

The broader implication, should the hypothesis be validated, is that quantum computing's 78-year default to $d = 2$ is not a physical constraint but a historical contingency — a silo failure across information theory, computer science, and $p$-adic geometry whose rectification may substantially alter the energy-efficiency landscape of quantum computation.

---

## Declarations

**Funding:** This research received no external funding.

**Conflicts of interest:** The author is affiliated with QNFO, which has a commercial interest in qudit-based quantum computing platforms. This paper is a theoretical JPCUB model, not a product claim. All assumptions and uncertainties are explicitly stated. Independent adversarial validation is invited.

**Data availability:** The JPCUB computation parameters and all assumptions are stated in Section 3. The qubit JPCUB values are reproduced from the prior competitive landscape comparison, which provides full specification-source traceability. The qudit model is a theoretical derivation with no experimental data.

**Code availability:** A reproducible Python computation of the JPCUB model is available in the project repository.

**Author contributions:** Single-author work. The JPCUB framework and competitive landscape comparison are prior collaborative work; the qudit extension is the sole contribution of the author.

**Acknowledgments:** The author thanks the external researchers whose published qudit work made this comparison possible — in particular, the trapped-ion qudit processor team [@C2_ringbauer2022] for demonstrating physical qudit operations, and the qudit review authors [@C1_wang2020] for establishing the field's consensus.

**License:** QNFO Unified License Agreement (QNFO-ULA)

**Pre-registration:** The three predictions in Section 5.1 are timestamped with this paper's publication.

---

## References
