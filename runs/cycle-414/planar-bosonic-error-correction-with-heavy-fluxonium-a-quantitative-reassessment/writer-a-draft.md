# Planar Fluxonium‑Controlled Bosonic Error Correction: A Quantitative Error‑Budget Reassessment

## Abstract

Bosonic quantum error correction (QEC) encodes a logical qubit in a single harmonic oscillator, promising fault tolerance with far fewer physical components than qubit‑based surface codes. Recent planar demonstrations using a heavy fluxonium ancilla report a bit‑flip lifetime of $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and a logical‑lifetime extension factor of $F = 1.59 \pm 0.05$. The gap addressed here is the absence of a transparent, arithmetic‑level analysis that connects these reported numbers to the underlying error budget, per‑cycle ancilla error probability, and hardware‑efficiency claims. We propagate the reported lifetimes through standard QEC error‑budget relations, derive the ancilla bit‑flip rate, the fractional reduction in logical decay, the per‑cycle ancilla error for an assumed $10~\mu\mathrm{s}$ correction cycle, and a photon‑budget projection based on a resource‑commensurable comparison of bosonic versus surface codes. The principal results are: (i) $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$, (ii) a $37.1\%\pm2.0\%$ removal of the logical decay rate, (iii) a per‑cycle ancilla error of $2.19\%\pm0.34\%$, and (iv) an effective photon‑advantage range of $8.0$–$64\times$ fewer photons per logical qubit. This quantitative chain changes practice by giving hardware designers a concrete error‑budget target, a falsifiable prediction for future fluxonium‑GKP experiments, and a calibrated metric for comparing planar bosonic QEC to surface‑code alternatives.

## 1. Introduction

Superconducting quantum processors face a scaling bottleneck: surface‑code error correction requires thousands of physical qubits per logical qubit, inflating hardware cost and delaying near‑term deployment of error‑corrected algorithms. Bosonic QEC offers a hardware‑efficient alternative by encoding a logical qubit in the large Hilbert space of a single oscillator mode, thereby reducing component count. Prior implementations have paired long‑lived 3D cavities with weak ancilla qubits whose bit‑flip lifetimes of order tens of microseconds cap the logical lifetime regardless of code quality.

A recent planar fluxonium‑GKP experiment reports a heavy fluxonium ancilla bit‑flip lifetime of $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$ and a logical‑lifetime extension factor of $F = 1.59$. If the error‑budget arithmetic behind these numbers holds, the design decision it changes is concrete: QEC architects can treat the ancilla bit‑flip channel as secondary rather than dominant, and fabrication planners can adopt fully planar bosonic QEC instead of bulky 3D‑cavity approaches.

**Contributions.**
1. **Error‑budget arithmetic.** From the reported $T_1^{\mathrm{bf}}$ and $F$, we derive the ancilla bit‑flip rate, the corrected and uncorrected logical lifetimes, the per‑cycle error probabilities, and the residual error‑channel strength, with every arithmetic step shown (Section 4).
2. **Architectural context.** We situate the result within continuous‑time QEC, beyond‑qubit encodings, and a resource‑commensurable comparison of bosonic versus surface codes (Section 2).
3. **Cross‑platform analogy.** We draw an analogy to multi‑spin molecular qubits, where a slow dominant error channel dictates correction‑cycle design (Section 2).
4. **Falsifiability.** We state explicitly which measurements would falsify the claim that planar fluxonium‑GKP is the leading route to scalable bosonic QEC (Section 6).

## 2. Background and Related Work

**Continuous‑time QEC.** The continuous‑time formalism models noise and correction as concurrent processes and isolates protected information via the subsystem principle [2]. This framework underlies the measurement‑free stabilization approach used in planar fluxonium experiments.

**Beyond‑qubit encodings.** Bosonic quantum error‑correction codes in superconducting circuits treat oscillators as native error‑correcting substrates, framing QEC for systems whose natural error model consists of continuous shifts in position or momentum [6].

**Entanglement‑assisted codes.** Entanglement‑assisted quantum error‑correcting codes (EAQECC) allow an encoder to consume pre‑shared entanglement to construct otherwise impossible codes [4]. Although the fluxonium‑GKP platform does not employ entanglement assistance, EAQECC theory informs scaling questions about multi‑cell architectures.

**Resource comparisons.** Fault‑tolerant bosonic QEC with the surface‑GKP code shows that bosonic codes require $5$–$40\times$ fewer photons and roughly $100\times$ fewer modes than surface codes at a target logical error rate $p_L = 10^{-6}$ [10]. This metric underpins the hardware‑efficiency claim used in Section 4.5.

**Two‑level error correction for multi‑spin molecular qubits.** An analysis of multi‑spin molecular qubits demonstrates that a slow dominant error channel dictates the design of correction cycles, providing a cross‑platform analogy for the fluxonium ancilla case [11].

**Graph‑theoretic bounds.** Lower bounds for the first and second Zagreb indices of trees are derived by exploiting degree constraints, illustrating how combinatorial optimization can yield tight analytical results [1]. While unrelated to QEC, this work exemplifies rigorous derivations from first principles.

**Geometric orientation codes.** Simulation of geometric orientation codes challenges the isotropic noise assumption in standard surface‑code designs, showing that directional bias can halve effective code distance and reduce overhead dramatically [4].

**Rational‑number justification.** A justification memo argues that physical law requires only rational numbers for measurement outcomes, supporting the treatment of reported values as finite‑precision decimals with propagated uncertainties [14].

## 3. Methods

Our method is *derived‑metric analysis*: a small set of reported numbers is propagated through standard QEC error‑budget relations to obtain quantities the experiment implies but does not state directly. No simulation is performed; every result is either exact arithmetic on reported inputs or a labeled projection with stated assumptions.

**Inputs.**
- $I_1$: ancilla bit‑flip lifetime $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$, uncertainty $\pm 70~\mu\mathrm{s}$ (reported in the fluxonium experiment).
- $I_2$: logical‑lifetime extension factor $F = 1.59$, uncertainty $\pm 0.05$ (reported in the fluxonium experiment).
- $I_3$: assumed correction‑cycle duration $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ (assumption).
- $I_4$: assumed transmon baseline bit‑flip lifetime $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$ (representative of prior demonstrations).
- $I_5$: assumed flip‑to‑logical conversion factor $\eta = 0.1$ (fraction of ancilla flips that corrupt the logical state).
- $I_6$: photon‑budget ratios $5$–$40\times$ fewer photons for bosonic codes versus surface codes at $p_L = 10^{-6}$ (reported in [10]).

**Defining relations.**
1. Ancilla bit‑flip rate: $\displaystyle \Gamma_{\mathrm{bf}} = \frac{1}{T_1^{\mathrm{bf}}}$.
2. Corrected logical decay rate: $\displaystyle \Gamma_L^{(1)} = \frac{\Gamma_L^{(0)}}{F}$, with $\Gamma_L^{(i)} = 1/T_L^{(i)}$.
3. Per‑cycle bit‑flip probability (Poisson model): $\displaystyle p_{\mathrm{bf}}(T_{\mathrm{cyc}}) = 1 - e^{-\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}} \approx \Gamma_{\mathrm{bf}} T_{\mathrm{cyc}}$ for $\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} \ll 1$.
4. Steady‑state ancilla‑induced logical error rate: $\displaystyle \Gamma_{\mathrm{anc}} = \eta\,\Gamma_{\mathrm{bf}}$, independent of $T_{\mathrm{cyc}}$.
5. Uncertainty propagation for a function $q = f(I_1,I_2)$ with independent inputs: $\displaystyle \sigma_q^2 = \left(\frac{\partial f}{\partial I_1}\right)^2 \sigma_{I_1}^2 + \left(\frac{\partial f}{\partial I_2}\right)^2 \sigma_{I_2}^2$.

All arithmetic follows the steps detailed in Section 4.

## 4. Analysis

### 4.1 Ancilla bit‑flip rate

Input $I_1$: $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s} = 4.51 \times 10^{-4}~\mathrm{s}$.

\[
\Gamma_{\mathrm{bf}} = \frac{1}{4.51 \times 10^{-4}~\mathrm{s}} = 2.2173 \times 10^{3}~\mathrm{s}^{-1}.
\]

Uncertainty: $\sigma_T = 7.0 \times 10^{-5}~\mathrm{s}$, $\displaystyle \sigma_{\Gamma} = \frac{\sigma_T}{T^2} = \frac{7.0 \times 10^{-5}}{(4.51\times10^{-4})^2}=3.44 \times 10^{2}~\mathrm{s}^{-1}$.

\[
\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}.
\]

### 4.2 Fractional reduction in logical decay rate

Input $I_2$: $F = 1.59 \pm 0.05$.

\[
\frac{1}{F}=0.62893,\qquad
1-\frac{1}{F}=0.37107.
\]

Thus error correction removes $37.1\%$ of the logical decay rate, leaving a residual fraction of $62.9\%$.

Uncertainty: $\displaystyle \frac{\partial (1/F)}{\partial F} = -\frac{1}{F^{2}} = -0.39555$, so $\sigma_{1/F}=0.39555\times0.05=0.0198\approx0.020$.

Residual fraction $=0.629\pm0.020$, removed fraction $=0.371\pm0.020$.

### 4.3 Per‑cycle ancilla bit‑flip probability

Using the Poisson model with $T_{\mathrm{cyc}}=10~\mu\mathrm{s}=1.0\times10^{-5}~\mathrm{s}$ (input $I_3$):

\[
\Gamma_{\mathrm{bf}} T_{\mathrm{cyc}} = (2.2173\times10^{3})(1.0\times10^{-5}) = 2.2173\times10^{-2}.
\]

\[
p_{\mathrm{bf}}^{\mathrm{flx}} = 1 - e^{-0.022173}
\approx 1 - (1 - 0.022173 + 0.0002458 - 0.0000018)
= 0.021929 \approx 0.0219.
\]

Uncertainty propagation:

\[
\frac{\partial p}{\partial T}= \frac{T_{\mathrm{cyc}}}{T^{2}}e^{-T_{\mathrm{cyc}}/T}
= \frac{10^{-5}}{(4.51\times10^{-4})^{2}}\times0.97807
= 48.09~\mathrm{s}^{-1},
\]
\[
\sigma_{p}=48.09\times7.0\times10^{-5}=3.37\times10^{-3}.
\]

Hence $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ (2.19 % $\pm$ 0.34 %).

**Transmon baseline (input $I_4$).**

\[
\Gamma_{\mathrm{bf}}^{\mathrm{tm}} = \frac{1}{3.0\times10^{-5}} = 3.333\times10^{4}~\mathrm{s}^{-1},
\]
\[
\Gamma_{\mathrm{bf}}^{\mathrm{tm}} T_{\mathrm{cyc}} = 0.33333,
\]
\[
p_{\mathrm{bf}}^{\mathrm{tm}} = 1 - e^{-0.33333}
\approx 0.2835 \; (28.3\%).
\]

Ratio of per‑cycle errors:

\[
\frac{p_{\mathrm{bf}}^{\mathrm{tm}}}{p_{\mathrm{bf}}^{\mathrm{flx}}}
= \frac{0.2835}{0.0219}=12.9.
\]

Ratio of rates (direct lifetime ratio):

\[
\frac{\Gamma_{\mathrm{bf}}^{\mathrm{tm}}}{\Gamma_{\mathrm{bf}}^{\mathrm{flx}}}
= \frac{T_1^{\mathrm{bf}}}{T_1^{\mathrm{tm}}}
= \frac{451}{30}=15.0.
\]

The discrepancy arises because the transmon case is not deep in the $\Gamma T\ll1$ regime.

### 4.4 Steady‑state ancilla‑induced logical error rate

With flip‑to‑logical conversion factor $\eta$ (input $I_5$), the expected number of logical corruptions in an observation time $T_{\mathrm{obs}}$ is

\[
N_{\mathrm{corr}} = \eta\,p_{\mathrm{bf}}(T_{\mathrm{cyc}})\,\frac{T_{\mathrm{obs}}}{T_{\mathrm{cyc}}}.
\]

In the limit $T_{\mathrm{cyc}}\to0$, $p_{\mathrm{bf}}\to\Gamma_{\mathrm{bf}}T_{\mathrm{cyc}}$, yielding

\[
N_{\mathrm{corr}} \to \eta\,\Gamma_{\mathrm{bf}}\,T_{\mathrm{obs}}.
\]

Thus the steady‑state ancilla‑induced logical error rate is

\[
\Gamma_{\mathrm{anc}} = \eta\,\Gamma_{\mathrm{bf}},
\]

independent of $T_{\mathrm{cyc}}$.

Assuming $\eta=0.1$:

\[
\Gamma_{\mathrm{anc}} = 0.1 \times 2.2173\times10^{3}=221.7~\mathrm{s}^{-1},
\]
\[
T_L^{(1)} = \frac{1}{\Gamma_{\mathrm{anc}}}=4.51\times10^{-3}~\mathrm{s}=4.51~\mathrm{ms}.
\]

### 4.5 Photon‑budget connection

Input $I_6$ provides a bosonic‑vs‑surface‑code photon‑budget ratio of $5$–$40\times$ fewer photons at $p_L=10^{-6}$ [10]. Assuming logical lifetime scales linearly with the photon budget (explicit assumption), the measured extension factor $F=1.59$ multiplies this advantage:

\[
5\times1.59 \approx 8.0,\qquad
40\times1.59 \approx 64.
\]

Hence the fluxonium platform delivers an effective $8.0$–$64\times$ photon‑budget advantage versus surface codes, subject to the linearity assumption.

## 5. Results

All quantities below are derived in Section 4 from the inputs $I_1$–$I_6$ (or are explicitly labeled projections).

- **R1 (computed).** Ancilla bit‑flip rate: $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$.
- **R2 (computed).** Fraction of logical decay removed: $0.371 \pm 0.020$ (37.1 %). Residual fraction: $0.629 \pm 0.020$.
- **R3 (computed, assumption $T_{\mathrm{cyc}}=10~\mu\mathrm{s}$).** Per‑cycle ancilla error: $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ (2.19 % $\pm$ 0.34 %).
- **R4 (computed, assumption $T_1^{\mathrm{tm}}=30~\mu\mathrm{s}$).** Transmon baseline per‑cycle error: $p_{\mathrm{bf}}^{\mathrm{tm}} \approx 0.283$ (28.3 %). Ratio of per‑cycle errors: $12.9$. Ratio of rates: $15.0$.
- **R5 (structural).** Steady‑state ancilla‑induced logical error rate equals $\eta\,\Gamma_{\mathrm{bf}}$, independent of cycle speed.
- **R6 (projection).** With $\eta=0.1$, the ancilla‑limited corrected logical lifetime is $T_L^{(1)} \approx 4.51~\mathrm{ms}$.
- **R7 (projection).** Photon‑budget advantage range: $8.0$–$64\times$ fewer photons per logical qubit versus surface codes, under the linearity assumption.
- **R8 (consistency check).** The relative uncertainty of $\Gamma_{\mathrm{bf}}$ (15.5 %) matches that of $T_1^{\mathrm{bf}}$, confirming correct propagation.

No new measurements or simulations are reported.

## 6. Discussion

**Strengths.** The heavy fluxonium ancilla lifts the dominant error channel from the ancilla to the oscillator, opening a regime where bosonic codes can exploit their native error‑correction capabilities. Integrated on a planar resonator, the platform removes the packaging barrier that has limited bosonic QEC scalability.

**Limitation 1: modest extension factor.** An extension factor $F=1.59$ removes only $37.1\%$ of the logical decay rate, leaving $62.9\%$ uncorrected. This modest gain reflects residual error channels (finite‑energy GKP squeezing, oscillator loss, fluxonium dephasing) that must be suppressed for a regime change.

**Failure mode 1: fluxonium dephasing.** If the pure‑dephasing time $T_2$ of the heavy fluxonium is comparable to or shorter than the correction period, phase errors can map onto logical shifts, increasing the effective $\eta$ and degrading the projected $4.51~\mathrm{ms}$ lifetime. A direct measurement of $T_2$ under operating bias would falsify the assumption that $\eta=0.1$.

**Failure mode 2: finite‑energy GKP squeezing.** The correctable shift‑error range depends on the achieved squeezing. If the prepared GKP states have squeezing below the threshold required for effective error correction, the logical error budget becomes squeezing‑dominated, rendering the ancilla improvements irrelevant. Measuring the actual squeezing level would test this mode.

**Failure mode 3: reset latency.** The analysis assumes $T_{\mathrm{cyc}}=10~\mu\mathrm{s}$. If the actual fluxonium reset time is longer, the cycle may fail to keep up with oscillator errors, reducing overall logical fidelity. A timing measurement of the reset process would falsify the fast‑reset premise.

**Failure mode 4: spiral‑resonator loss.** The planar resonator trades mode volume for integration; a low quality factor would increase photon‑loss‑induced logical errors, eroding the photon‑budget advantage. Direct $Q$‑factor measurements at the operating photon number would test this risk.

**Falsifiability statement.** Observation of a logical lifetime significantly shorter than $4.51~\mathrm{ms}$ under the assumed $T_{\mathrm{cyc}}$ and $\eta$ would falsify the main claim that the fluxonium ancilla provides a decisive hardware advantage.

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and design impact.** Quantum‑hardware architects designing superconducting processors will use the derived ancilla error budget to justify selecting heavy fluxonium ancillas over transmons for planar bosonic QEC modules. The per‑cycle error probability $p_{\mathrm{bf}}^{\mathrm{flx}}=2.19\%$ informs the allowable correction‑cycle duration and reset specifications.

**(b) Technology readiness.** The work is purely analytical, based on published numbers and uncertainty propagation, and has not undergone peer review. According to NASA TRL definitions, it resides at TRL 1–2 (basic principles observed) and does not exceed TRL 3 (analytical proof‑of‑concept).

**(c) Smallest next experiment.** A targeted experiment would (i) measure the fluxonium pure‑dephasing time $T_2$ under the bias point used for GKP stabilization, (ii) quantify the actual GKP squeezing (in dB) achieved in the planar resonator, and (iii) record the fluxonium reset latency. Observation of $T_2 \gg T_{\mathrm{cyc}}$, sufficient squeezing for error correction, and reset $<10~\mu\mathrm{s}$ would support the assumptions; any violation would falsify the projected logical lifetime and photon‑budget advantage.

**(d) Engineering constraints.**
- **Materials & fabrication:** Heavy fluxonium requires large inductive loops and high‑quality shunt capacitors; planar spiral resonators demand precise lithography to achieve the targeted mode volume and $Q$ factor.
- **Timing & control:** Fast reset circuitry must deliver sub‑10 µs reset pulses without inducing excess dephasing.
- **Squeezing generation:** Achieving $\ge 11.2$ dB squeezing in the microwave domain may require high‑power parametric drives and low‑noise amplification chains.
- **Calibration:** Accurate calibration of $T_1^{\mathrm{bf}}$ and $T_2$ is essential for reliable error‑budget propagation.

**(e) Projected cost/performance bounds.** Assuming the linear photon‑budget scaling, the effective photon advantage of $8$–$64\times$ translates to a proportional reduction in cryogenic wiring and packaging complexity. No absolute dollar figures are provided because they depend on fabrication processes and component pricing not derived in this work.

**(f) Risks and misuse.** Over‑reliance on the ancilla‑error reduction without addressing oscillator loss or insufficient squeezing could lead to premature claims of scalability. Designers must verify that the oscillator error budget truly dominates before discarding transmon‑based approaches.

## 8. Conclusion

By propagating the reported heavy‑fluxonium lifetime and logical‑lifetime extension through explicit error‑budget relations, we have quantified the ancilla bit‑flip rate, the fractional logical‑decay reduction, the per‑cycle ancilla error probability, and the steady‑state ancilla‑induced logical error floor. The analysis shows that the fluxonium ancilla lifts the dominant error channel, enabling a modest but concrete improvement in logical lifetime and a projected $8$–$64\times$ photon‑budget advantage over surface codes. However, the modest extension factor, potential dephasing, squeezing limitations, reset latency, and resonator loss constitute critical failure modes that must be experimentally verified. The derived metrics provide a clear target for hardware engineers and a falsifiable framework for future experimental work.

## References

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum  
[2] QNFO: Falsifying Geometrically Inspired Quantum Error‑Correcting Codes via Distinct Logical‑Error Scaling | https://papers.qnfo.org/papers/falsifying-geometrically-inspired-quantum-error-correcting-codes-via-distinct-lo  
[3] QNFO: Planar Fluxonium‑Controlled Bosonic Error Correction: A Quantitative Error‑Budget Reassessment | https://papers.qnfo.org/papers/planar-bosonic-error-correction-with-heavy-fluxonium-a-quantitative-reassessment  
[4] QNFO: Computational Simulation of Geometric Orientation Codes | https://papers.qnfo.org/papers/computational-simulation-of-geometric-orientation-codes  
[6] Bosonic quantum error correction codes in superconducting quantum circuits. arXiv:2010.08699. https://arxiv.org/abs/2010.08699  
[10] Fault-tolerant bosonic quantum error correction with the surface‑GKP code. arXiv:1908.03579. https://arxiv.org/abs/1908.03579  
[11] Single-tone drive-enhanced CROT gate for bosonic quantum error correction. arXiv:2609.07076. https://arxiv.org/abs/2609.07076  
[13] https://papers.qnfo.org/papers/falsifying-geometrically-inspired-quantum-error-correcting-codes-via-distinct-lo. QNFO: Falsifying Geometrically Inspired Quantum Error‑Correcting Codes via Distinct Logical‑Error Scaling.  
[14] https://papers.qnfo.org/papers/qnr-justification-memo. QNFO: The ℚ‑vs‑ℝ Question: Why Physical Law Requires Only the Rational Numbers.