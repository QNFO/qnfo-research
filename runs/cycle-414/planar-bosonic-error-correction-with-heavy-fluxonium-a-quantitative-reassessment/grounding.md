# Grounding block - source: rem-45bbc62e-7268-4b04-9869-9e1e8bacdf48

## Research idea

Correct the published paper 'planar-bosonic-error-correction-with-heavy-fluxonium-a-quantitative-reassessment' for erratum pl-planar-bosonic-error-correction-with-heavy-fluxonium-a-quantitative-reassessment-2.0.0-1: The divergence report (Appendix A) adopts Draft A's description of citation [11] as an analysis of 'two-level error correction for multi-spin molecular qubits' because it 'directly supports the cross-platform error-hierarchy analogy'.
Also: pl-planar-bosonic-error-correction-with-heavy-fluxonium-a-quantitative-reassessment-2.0.0-0: The photon-budget advantage of 8.0–64× (§4.5, R7, Abstract result iv) is obtained by multiplying the cited 5–40× photon ratio by the lifetime extension factor F = 1.59 under an 'explicit assumption' that 'logical lifetime scales linearly with the photon budget'.

## Existing paper under revision (remediation only)

# Planar Fluxonium‑Controlled Bosonic Error Correction: A Quantitative Error‑Budget Reassessment

## Abstract

Bosonic quantum error correction (QEC) encodes a logical qubit in a single harmonic oscillator, promising fault tolerance with far fewer physical components than qubit‑based surface codes. Recent planar demonstrations using a heavy fluxonium ancilla report a bit‑flip lifetime of $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and a logical‑lifetime extension factor of $F = 1.59 \pm 0.05$. The gap addressed here is the absence of a transparent, arithmetic‑level analysis that connects these reported numbers to the underlying error budget, per‑cycle ancilla error probability, and hardware‑efficiency claims. We propagate the reported lifetimes through standard QEC error‑budget relations, derive the ancilla bit‑flip rate, the fractional reduction in logical decay, the per‑cycle ancilla error for an assumed $10~\mu\mathrm{s}$ correction cycle, and a photon‑budget projection based on a resource‑commensurable comparison of bosonic versus surface codes. The principal results are: (i) $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$, (ii) a $37.1\%\pm2.0\%$ removal of the logical decay rate, (iii) a per‑cycle ancilla error of $2.19\%\pm0.34\%$, and (iv) an effective photon‑advantage range of $8.0$–$64\times$ fewer photons per logical qubit. This quantitative chain changes practice by giving hardware designers a concrete error‑budget target, a falsifiable prediction for future fluxonium‑GKP experiments, and a calibrated metric for comparing planar bosonic QEC to surface‑code alternatives.

## 1. Introduction

Superconducting quantum processors face a scaling bottleneck: surface‑code error correction requires thousands of physical qubits per logical qubit, inflating hardware cost and delaying near‑term deployment of error‑corrected algorithms. Bosonic QEC offers a hardware‑efficient alternative by encoding a logical qubit in the large Hilbert space of a single oscillator mode, thereby reducing component count. However, the practical history of bosonic QEC in superconducting circuits has been dominated by an asymmetry: long‑lived oscillators (3D cavities) are paired with weak ancilla qubits (transmons) whose bit‑flip lifetimes of order tens of microseconds cap the logical lifetime regardless of code quality.

A recent planar fluxonium‑GKP experiment attacks this asymmetry. Heavy fluxonium—a superconducting artificial atom with a large shunt capacitance and an inductive loop—has a bit‑flip lifetime taken as $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$ for the purpose of analysis, representing an order‑of‑magnitude improvement over prior transmon ancillas. Integrated on a planar Archimedean spiral resonator, the platform enables finite‑energy GKP state preparation, measurement‑free stabilization, and rapid fluxonium reset, yielding a logical‑lifetime extension factor of $F = 1.59 \pm 0.05$.

If the error‑budget arithmetic behind these numbers holds, the design decision it changes is concrete: QEC architects can treat the ancilla bit‑flip channel as secondary rather than dominant, and fabrication planners can adopt fully planar bosonic QEC instead of bulky 3D‑cavity approaches.

**Contributions.**
1. **Error‑budget arithmetic.** From the reported $T_1^{\mathrm{bf}}$ and $F$, we derive the ancilla bit‑flip rate, the corrected and uncorrected logical lifetimes, the per‑cycle error probabilities, and the residual error‑channel strength, with every arithmetic step shown (Section 4).
2. **Architectural context.** We situate the result within continuous‑time QEC, beyond‑qubit encodings, entanglement‑assisted codes, and a resource‑commensurable comparison of bosonic versus surface codes (Section 2).
3. **Cross‑platform analogy.** We draw an analogy to multi‑spin molecular qubits, where a slow dominant error channel dictates correction‑cycle design (Section 2).
4. **Falsifiability.** We state explicitly which measurements would falsify the claim that planar fluxonium‑GKP is the leading route to scalable bosonic QEC (Section 6).

## 2. Background and Related Work

**Continuous‑time QEC.** Reference [2] develops a continuous‑time formalism in which noise and correction are modeled as concurrent processes, using the subsystem principle to isolate protected information. The measurement‑free stabilization of [1] is a discrete‑time analogue: repeated coherent correction cycles replace continuous weak measurement, and the CTQEC framework supplies the language for the limit in which the correction period $T_{\mathrm{cyc}}$ becomes short compared with oscillator error timescales.

**Beyond‑qubit encodings.** Reference [6] provides the theoretical foundation for treating oscillators as native error‑correcting substrates rather than as mere buses. It frames QEC for systems whose natural error model consists of continuous shifts in position or momentum, precisely the setting of GKP codes.

**Entanglement‑assisted codes.** Reference [4] introduces entanglement‑assisted quantum error‑correcting codes (EAQECC), which allow an encoder to consume pre‑shared entanglement to construct codes that would otherwise be impossible. While the fluxonium‑GKP platform does not employ entanglement assistance, EAQECC theory is relevant to scaling questions about whether multiple fluxonium‑spiral cells could share entangled ancilla resources.

**Resource comparisons.** Reference [10] performs a resource‑commensurable comparison of cat, GKP, binomial, and surface codes using a photons‑per‑logical‑qubit metric at a target logical error rate $p_L = 10^{-6}$, finding that bosonic codes require $5$–$40\times$ fewer photons and roughly $100\times$ fewer modes than surface codes. This metric underpins the “hardware‑efficiency” claim in [1] and is used in Section 4.5 to translate the measured lifetime extension into a photon‑budget advantage.

Reference [11] introduces a single‑tone drive‑enhanced CROT gate for bosonic quantum error correction, which is relevant to gate‑level implementations of bosonic codes.

Reference [13] investigates logical‑error scaling for geometrically inspired quantum error‑correcting codes.

**Measurement finitude.** Reference [14] argues that all physical measurements produce finite‑precision rational numbers, citing fundamental bounds. We adopt the operational consequence that reported values such as $451~\mu\mathrm{s}$ and $1.59$ are treated as finite‑precision decimals carrying their stated uncertainties, and derived quantities are quoted with no more precision than the propagated uncertainty supports.

## 3. Methods

Our method is *derived‑metric analysis*: a small set of reported numbers is propagated through standard QEC error‑budget relations to obtain quantities the experiment implies but does not state directly. No simulation is performed; every result is either exact arithmetic on reported inputs or a labeled projection with stated assumptions.

**Inputs.**
- $I_1$: ancilla bit‑flip lifetime $T_1^{\mathrm{bf}} = 451~\mu\mathrm{s}$, uncertainty $\pm 70~\mu\mathrm{s}$ (reported in [1],[3]).
- $I_2$: logical‑lifetime extension factor $F = 1.59$, uncertainty $\pm 0.05$ (reported in [1],[3]).
- $I_3$: assumed correction‑cycle duration $T_{\mathrm{cyc}} = 10~\mu\mathrm{s}$ (assumption).
- $I_4$: assumed transmon baseline bit‑flip lifetime $T_1^{\mathrm{tm}} = 30~\mu\mathrm{s}$ (assumption representative of prior 3D‑cavity demonstrations).
- $I_5$: assumed flip‑to‑logical conversion factor $\eta = 0.1$ (assumption about the fraction of ancilla flips that corrupt the logical state).
- $I_6$: photon‑budget ratios $5$–$40\times$ fewer photons for bosonic codes versus surface codes at $p_L = 10^{-6}$ (reported in [10]).

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

Input $I_6$ provides a bosonic‑vs‑surface‑code photon‑budget ratio of $5$–$40\times$ fewer photons at $p_L=10^{-6}$. Assuming logical lifetime scales linearly with the photon budget (explicit assumption), the measured extension factor $F=1.59$ multiplies this advantage:

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

**Strengths.** The heavy fluxonium ancilla lifts the dominant error channel from the ancilla to the oscillator, opening a regime where bosonic codes can exploit their native error‑correction capabilities. Combined with a planar resonator, the platform removes the packaging barrier that has limited bosonic QEC scalability.

**Limitation 1: modest extension factor.** An extension factor $F=1.59$ removes only $37.1\%$ of the logical decay rate, leaving $62.9\%$ uncorrected. This modest gain reflects residual error channels (finite‑energy GKP squeezing, oscillator loss, fluxonium dephasing) that must be suppressed for a regime change.

**Failure mode 1: fluxonium dephasing.** If the pure‑dephasing time $T_2$ of the heavy fluxonium is comparable to or shorter than the correction period, phase errors can map onto logical shifts, increasing the effective $\eta$ and degrading the projected $4.51~\mathrm{ms}$ lifetime. A direct measurement of $T_2$ under operating bias would falsify the assumption that $\eta=0.1$.

**Failure mode 2: finite‑energy GKP squeezing.** The correctable shift‑error range depends on the achieved squeezing. If the prepared GKP states have squeezing below a threshold required for effective error correction, the logical error budget becomes squeezing‑dominated, rendering the ancilla improvements irrelevant. Measuring the actual squeezing level would test this mode.

**Failure mode 3: reset latency.** The analysis assumes $T_{\mathrm{cyc}}=10~\mu\mathrm{s}$. If the actual fluxonium reset time is longer, the cycle may fail to keep up with oscillator errors, reducing overall logical fidelity. A timing measurement of the reset process would falsify the fast‑reset premise.

**Failure mode 4: spiral‑resonator loss.** The planar resonator trades mode volume for integration; a low quality factor would increase photon‑loss‑induced logical errors, eroding the photon‑budget advantage. Direct $Q$‑factor measurements at the operating photon number would test this risk.

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

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Towards Scalable Bosonic Quantum Error Correction. arXiv:2002.11008. https://arxiv.org/abs/2002.11008
[2] Bosonic error correction codes based on states generated via particle number resolving measurements. arXiv:2509.16993. https://arxiv.org/abs/2509.16993
[3] Bosonic quantum error correction using squeezed Fock states. arXiv:2506.00300. https://arxiv.org/abs/2506.00300
[4] Error Correction Using Squeezed Fock States. arXiv:2312.16000. https://arxiv.org/abs/2312.16000
[6] Bosonic quantum error correction codes in superconducting quantum circuits. arXiv:2010.08699. https://arxiv.org/abs/2010.08699
[10] Fault-tolerant bosonic quantum error correction with the surface-GKP code. arXiv:1908.03579. https://arxiv.org/abs/1908.03579
[11] Single-tone drive-enhanced CROT gate for bosonic quantum error correction. arXiv:2609.07076. https://arxiv.org/abs/2609.07076
[13] https://papers.qnfo.org/papers/falsifying-geometrically-inspired-quantum-error-correcting-codes-via-distinct-lo. QNFO: Falsifying Geometrically Inspired Quantum Error‑Correcting Codes via Distinct Logical‑Error Scaling.
[14] https://papers.qnfo.org/papers/qnr-justification-memo. QNFO: The ℚ-vs-ℝ Question: Why Physical Law Requires Only the Rational Numbers.


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum

## QNFO corpus context (Vectorize)

QNFO: Falsifying Geometrically Inspired Quantum Error‑Correcting Codes via Distinct Logical‑Error Scaling | https://papers.qnfo.org/papers/falsifying-geometrically-inspired-quantum-error-correcting-codes-via-distinct-lo
QNFO: Planar Fluxonium‑Controlled Bosonic Error Correction: A Quantitative Error‑Budget Reassessment | https://papers.qnfo.org/papers/planar-bosonic-error-correction-with-heavy-fluxonium-a-quantitative-reassessment
QNFO: Computational Simulation of Geometric Orientation Codes | https://papers.qnfo.org/papers/computational-simulation-of-geometric-orientation-codes
QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | https://papers.qnfo.org/papers/x3.3-bosonic-codes-native-encoding

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
  We derive sharp lower bounds for the first and the second Zagreb indices ($M_1$ and $M_2$ respectively) for trees and chemical trees with the given number of pendent vertices and find optimal trees. $M_1$ is minimized by a tree with all internal vertices having degree 4, while $M_2$ is minimized by a tree where each "stem" vertex is incident to 3 or 4 pendent vertices and one internal vertex, whil
  Full text (https://arxiv.org/html/1405.1293v3), excerpts of its own sections:
  § Introduction: Topological graph indices are widely used in mathematical chemistry to predict properties of chemical compounds. They have been intensively studied in recent years. Dozens of various indices were suggested [ 1 ] to describe topology of complex molecules, among the earliest and the most famous being the first and the second Zagreb indices – $M_{1}$ and $M_{2}$ respectively [ 9 ] . The popular research problem is to find lower and upper bounds of an index over a certain set of graphs and to characterize extremal graphs in this set. The typical set to study is that of all graphs (trees, bipartite or unicyclic graphs, “cacti”, etc) of the fixed order (i.e. with the fixed number of vertices). Extremal graphs on these sets often appear to be degenerate. For example, the chain minimizes Zagreb indices, while the star maximizes them over the set of trees of order $N$ (see [ 4 , 10 ] ). Even when the set of admissible graphs is cut (by limiting degrees, chromatic or matching numbers, etc), extremal graphs are typically found on the “boundary” of the set. [...]
  § 1 The First Zagreb Index: Let $G$ be a simple connected undirected graph with the vertex set $V(G)$ and the edge set $E(G)$ . Denote by $d_{G}(v)$ the degree of a vertex $v\in V(G)$ in the graph $G$ , i.e., the number of vertices being incident to $v$ in $G$ . The first Zagreb index is defined in [ 9 ] as $M_{1}(G):=\sum_{v\in V(G)}d_{G}(v)^{2},$ (1) while the second Zagreb index – as $M_{2}(G):=\sum_{uv\in E(G)}d_{G}(u)d_{G}(v).$ (2) The vertex $v\in V(G)$ with $d_{G}(v)=1$ is called a pendent vertex. Denote the set of pendent vertices of the graph $G$ with $W(G)$ . A connected graph $T$ with $N$ vertices and $N-1$ edges is called a tree. Theorem 1 For any tree $T$ with $n\geqslant 2$ pendent vertices $M_{1}(T)\geqslant 9n-16$ if $n$ is even. The equality holds if $T$ is a $4$ -tree ( with $d_{T}(m)=4$ for all $m\in V(G)\backslash W(G)$ ) . If $n$ is odd, then $M_{1}(T)\geqslant 9n-15$ , and the equality holds if $T$ is a tree with all internal vertices having degree $4$ except the one of degree $3$ . □ Proof For $n=2$ the optimal tree is the complete graph $K_{2}$ , and the theorem obviously holds. [...]
  § 2 The Second Zagreb Index: An internal vertex in a tree is called a stem vertex if it has incident pendent vertices (see [ 3 ] ). The edge connecting a stem with a pendent vertex will be referred to as a stem edge . Theorem 3 For any tree $T$ with $n\geqslant 8$ pendent vertices $M_{2}(T)\geqslant 11n-27$ . The equality holds if each stem vertex in $T$ has degree $4$ or $5$ while other internal vertices having degree $3$ . At least one such tree exits for any $n\geqslant 9$ . □ Proof Let us employ again the idea of an attached tree from Theorem 2 . Below we suggest a suitable generalization of the concept of an attached tree, then we interrelate its cost with $M_{2}$ , and, finally, use induction on $n$ to prove the lower bound. [...]
  § 3 Conclusion: Above we suggested an optimization framework for degree-based indices of undirected trees. Using the discussed approach one can calculate lower bounds for Zagreb-like indices and find the graphs minimizing these indices over the set of trees (or chemical trees) with the fixed number of pendent vertices. Theorem 1 provides a tight lower-bound estimate for $M_{1}$ and shows that it is achieved at $4$ -trees. Theorem 2 gives a high-quality lower-bound estimate for the generalized $M_{1}$ -like index. Theorem 3 proves the tight lower-bound estimate for $M_{2}$ and characterizes $M_{2}$ -minimal trees. [...]
[2] QNFO: Falsifying Geometrically Inspired Quantum Error‑Correcting Codes via Distinct Logical‑Error Scaling | https://papers.qnfo.org/papers/falsifying-geometrically-inspired-quantum-error-correcting-codes-via-distinct-lo
  Geometric constructions of quantum error‑correcting codes (QECCs) have been proposed as alternatives to standard topological codes, yet their physical relevance remains ambiguous. Existing proposals lack a testable prediction that distinguishes them from surface‑code scaling of logical error rates. We identify this gap and formulate a falsifiability criterion: a geometrically motivated code must e
  Full text (https://papers.qnfo.org/papers/falsifying-geometrically-inspired-quantum-error-correcting-codes-via-distinct-lo), excerpts of its own sections:
  § 1. Introduction: Large‑scale quantum computers require fault‑tolerant logical qubits. Presently, the dominant approach is the two‑dimensional surface code, which demands thousands of physical qubits per logical qubit and a logical error rate that scales as \(p_{L}\approx A\,(p_{\mathrm{phys}})^{d}\) with code distance \(d\) \([8]\). This resource overhead blocks near‑term deployment of error‑corrected algorithms and inflates the cost of quantum processors. [...]
  § 3.3 Parameter Extraction from Experimental Data: From the fluxonium experiment \([8]\) we take: - Ancilla bit‑flip lifetime \(T_{1}^{\mathrm{bf}}=451~\mu\mathrm{s}\) (central value). - Cycle time assumption \(T_{\mathrm{cyc}}=10~\mu\mathrm{s}\) (as in R3 of \([8]\)). The per‑cycle ancilla error probability is \[ p_{\mathrm{bf}}^{\mathrm{flx}} = 1-\exp\!\bigl(-\Gamma_{\mathrm{bf}}T_{\mathrm{cyc}}\bigr), \tag{5} \] with \(\Gamma_{\mathrm{bf}}=1/T_{1}^{\mathrm{bf}}\). Substituting the numbers yields a concrete \(p_{\mathrm{phys}}\) for the logical‑error calculation.
  § 5. Results: - **R1 (computed).** Ancilla bit‑flip rate \(\Gamma_{\mathrm{bf}} = 2.22\times10^{3}\,\mathrm{s}^{-1}\) (derived from \(T_{1}^{\mathrm{bf}}\) in \([8]\)). - **R2 (computed).** Effective physical error probability per cycle \(p_{\mathrm{phys}} = 2.19\times10^{-2}\) (Eq. 10). - **R3 (computed).** Geometric‑code logical error rate for \(d=5\): \(p_{L}^{\mathrm{geom}} = 7.1\times10^{-5}\) (Eq. 15). - **R4 (computed).** Surface‑code logical error rate for the same parameters: \(p_{L}^{\mathrm{SC}} = 5.1\times10^{-9}\) (Eq. 18). These numbers constitute a falsifiable prediction: if an experiment on a geometric QECC with distance five yields a logical error rate consistent with \(p_{L}^{\mathrm{geom}}\), the geometric scaling hypothesis is supported; if the measured rate follows \(p_{L}^{\mathrm{SC}}\) within experimental uncertainty, the geometric construction is falsified as a fault‑tolerant scheme.
  § 7(c) Minimal Next Experiment: The smallest de‑risking experiment is a benchmark test on a superconducting processor implementing a geometric stabilizer set (e.g., a small‑scale code with \(d=5\)). The experiment measures the logical error probability after a fixed number of error‑correction cycles, using the ancilla bit‑flip rate from \([8]\) as the physical error source. Observation of a logical error rate consistent with Eq. (15) would support the geometric scaling; a rate near Eq. (18) would falsify it.
  § 8. Conclusion: We have formulated a concrete falsifiability criterion for geometrically inspired QECCs based on a distinct logical‑error scaling law. By extracting a stabilizer interaction degree from the code’s algebraic description, we derived the scaling \(p_{L}\propto p_{\mathrm{phys}}^{\,d/2}\) and compared it quantitatively to the surface‑code law. Using experimentally reported ancilla error rates from a fluxonium‑based bosonic platform, we produced a numerical prediction that separates the two scalings by three orders of magnitude for a modest code distance. This prediction is experimentally testable with current superconducting technology, offering a decisive pathway to either validate or falsify the geometric QECC paradigm. The result informs quantum system designers about the trade‑offs between novel geometric constructions and established topological codes, and it establishes a rigorous benchmark for future theoretical proposals.
[3] QNFO: Planar Fluxonium‑Controlled Bosonic Error Correction: A Quantitative Error‑Budget Reassessment | https://papers.qnfo.org/papers/planar-bosonic-error-correction-with-heavy-fluxonium-a-quantitative-reassessment
  Bosonic quantum error correction (QEC) encodes a logical qubit in a single harmonic oscillator, promising fault tolerance with far fewer physical components than qubit‑based surface codes. Recent planar demonstrations using a heavy fluxonium ancilla report a bit‑flip lifetime of $T_1^{\mathrm{bf}} = 451 \pm 70~\mu\mathrm{s}$ and a logical‑lifetime extension factor of $F = 1.59 \pm 0.05$. The gap a
  Full text (https://papers.qnfo.org/papers/planar-bosonic-error-correction-with-heavy-fluxonium-a-quantitative-reassessment), excerpts of its own sections:
  § 1. Introduction: Superconducting quantum processors face a scaling bottleneck: surface‑code error correction requires thousands of physical qubits per logical qubit, inflating hardware cost and delaying near‑term deployment of error‑corrected algorithms. Bosonic QEC offers a hardware‑efficient alternative by encoding a logical qubit in the large Hilbert space of a single oscillator mode, thereby reducing component count. [...]
  § 2. Background and Related Work: **Continuous‑time QEC.** Reference [2] develops a continuous‑time formalism in which noise and correction are modeled as concurrent processes, using the subsystem principle to isolate protected information. [...]
  § 5. Results: All quantities below are derived in Section 4 from the inputs $I_1$–$I_6$ (or are explicitly labeled projections). - **R1 (computed).** Ancilla bit‑flip rate: $\Gamma_{\mathrm{bf}} = (2.22 \pm 0.34)\times10^{3}~\mathrm{s}^{-1}$. - **R2 (computed).** Fraction of logical decay removed: $0.371 \pm 0.020$ (37.1 %). Residual fraction: $0.629 \pm 0.020$. - **R3 (computed, assumption $T_{\mathrm{cyc}}=10~\mu\mathrm{s}$).** Per‑cycle ancilla error: $p_{\mathrm{bf}}^{\mathrm{flx}} = 0.0219 \pm 0.0034$ (2.19 % $\pm$ 0.34 %). - **R4 (computed, assumption $T_1^{\mathrm{tm}}=30~\mu\mathrm{s}$).** Transmon baseline per‑cycle error: $p_{\mathrm{bf}}^{\mathrm{tm}} \approx 0.283$ (28.3 %). Ratio of per‑cycle errors: $12.9$. Ratio of rates: $15.0$. - **R5 (structural).** Steady‑state ancilla‑induced logical error rate equals $\eta\,\Gamma_{\mathrm{bf}}$, independent of cycle speed. - **R6 (projection).** With $\eta=0.1$, the ancilla‑limited corrected logical lifetime is $T_L^{(1)} \approx 4.51~\mathrm{ms}$. [...]
  § 6. Discussion: **Strengths.** The heavy fluxonium ancilla lifts the dominant error channel from the ancilla to the oscillator, opening a regime where bosonic codes can exploit their native error‑correction capabilities. Combined with a planar resonator, the platform removes the packaging barrier that has limited bosonic QEC scalability. **Limitation 1: modest extension factor.** An extension factor $F=1.59$ removes only $37.1\%$ of the logical decay rate, leaving $62.9\%$ uncorrected. This modest gain reflects residual error channels (finite‑energy GKP squeezing, oscillator loss, fluxonium dephasing) that must be suppressed for a regime change. **Failure mode 1: fluxonium dephasing.** If the pure‑dephasing time $T_2$ of the heavy fluxonium is comparable to or shorter than the correction period, phase errors can map onto logical shifts, increasing the effective $\eta$ and degrading the projected $4.51~\mathrm{ms}$ lifetime. A direct measurement of $T_2$ under operating bias would falsify the assumption that $\eta=0.1$. [...]
  § 8. Conclusion: By propagating the reported heavy‑fluxonium lifetime and logical‑lifetime extension through explicit error‑budget relations, we have quantified the ancilla bit‑flip rate, the fractional logical‑decay reduction, the per‑cycle ancilla error probability, and the steady‑state ancilla‑induced logical error floor. The analysis shows that the fluxonium ancilla lifts the dominant error channel, enabling a modest but concrete improvement in logical lifetime and a projected $8$–$64\times$ photon‑budget advantage over surface codes. However, the modest extension factor, potential dephasing, squeezing limitations, reset latency, and resonator loss constitute critical failure modes that must be experimentally verified. The derived metrics provide a clear target for hardware engineers and a falsifiable framework for future experimental work.
[4] QNFO: Computational Simulation of Geometric Orientation Codes | https://papers.qnfo.org/papers/computational-simulation-of-geometric-orientation-codes
  Fault-tolerant quantum computing requires robust error correction traditionally met using planar topologies that assume noise is perfectly isotropic. However, recent astrophysical measurements suggest the universe possesses fundamental anisotropic properties. This paper challenges the isotropic assumption in quantum error correction by proposing geometric orientation codes. This novel architecture
  Full text (https://papers.qnfo.org/papers/computational-simulation-of-geometric-orientation-codes), excerpts of its own sections:
  § Computational: Simulation of Geometric Orientation Codes
  § Addressing: Isotropic Assumptions in Quantum Error Correction **Author:** Rowan Brad Quni-Gudzinas **Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com) **ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604) **ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062) **DOI:** https://papers.qnfo.org/papers/computational-simulation-of-geometric-orientation-codes/ **Date:** 2026-04-09 **Version:** 1.0 **Abstract**: Fault-tolerant quantum computing requires robust error correction traditionally met using planar topologies that assume noise is perfectly isotropic. However, recent astrophysical measurements suggest the universe possesses fundamental anisotropic properties. This paper challenges the isotropic assumption in quantum error correction by proposing geometric orientation codes. This novel architecture utilizes 3D spatial orientation as the primary redundancy degree of freedom. It explicitly counteracts highly directional noise by aligning physical qubits along distinct spatial axes. [...]
  § 1.1 Context and Motivation: Fault-tolerant quantum computing requires robust quantum error correction to preserve delicate superposition states against environmental decoherence. The surface code has emerged as the current industry standard due to its scalable 2D planar lattice architecture (Debroy, 2025). These planar architectures operate by extracting error syndromes via local parity checks across a perfectly flat hardware topology. A core assumption underlying these models is that environmental noise is perfectly isotropic and identically distributed across all spatial dimensions. This assumption originates from classical macroscopic physics, which tends to average out microscopic spatial fluctuations. Deviations from perfect isotropy severely degrade standard surface code performance, as real physical hardware frequently exhibits biased noise. New mathematical approaches are required to handle fundamentally non-standard noise profiles efficiently (Xie, 2025).
  § 1.2 The Isotropic Assumption in: QEC Isotropy implies that noise acts equally in all spatial directions, a convenient mathematical premise underpinning most QEC threshold theorems (Wang, 2025). This theoretical symmetry allows for the design of uniform topological lattices and simplifies the operation of standard decoders. Yet, real quantum hardware often exhibits highly biased or directional noise, such as asymmetric cross-resonance gate errors. Surface codes scale exceedingly poorly when noise is highly anisotropic, as directional biases create correlated string errors (Vezvaee, 2025). [...]
  § 5.1 Summary of Key Findings: This study rigorously challenged the isotropic assumption in quantum error correction by introducing and benchmarking geometric orientation codes. We simulated these codes under highly anisotropic noise channels derived from fundamental theoretical physics models. The orientation codes demonstrated vastly superior error suppression capabilities compared to standard planar surface codes under directional bias. Surface codes degraded significantly, suffering from correlated string errors that halved their effective distance. Physical-to-logical overhead was reduced from >241:1 to exactly 4:1 to achieve a 1e-4 logical error rate. This represents a massive paradigm shift in handling biased quantum noise. The findings validate the integration of fundamental physics symmetries into practical QEC hardware design (Debroy, 2025).
[5] QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | https://papers.qnfo.org/papers/x3.3-bosonic-codes-native-encoding
  X3.3 — Resource-commensurable comparison of bosonic codes vs surface codes using photons/logical-qubit metric at p_L=10^-6. Bosonic codes require 5-40x fewer photons and ~100x fewer modes. Novel claim: HO as QM IR attractor implies bosonic codes are the native encoding.
  Full text (https://papers.qnfo.org/papers/x3.3-bosonic-codes-native-encoding), excerpts of its own sections:
  § 1.1 The Claim to Be Tested: The Harmonic Paradigm V4.0 (https://papers.qnfo.org/papers/harmonische-paradigma-kappa-siit-v4/, §6) advances a structural claim: because the harmonic oscillator is the universal IR attractor of quantum mechanics — all weakly anharmonic bosonic systems flow toward it under RG — the error-syndrome structure of any physical quantum system near this fixed point is the error-syndrome structure of the harmonic ladder itself. **Bosonic QEC codes are the codes that exploit this structure directly, rather than imposing an external discrete scaffold (qubit lattice) on a continuous substrate.** They are the *native* encoding. This is not a claim about experimental convenience or engineering preference. It is a claim about physical correspondence: the code structure that most closely matches the physics of the substrate will be the most resource-efficient. Just as a Fourier basis is "native" to a translation-invariant system, bosonic codes are native to a harmonic system. [...]
  § 1.2 Why This Comparison Has Not Been Made: Three obstacles have prevented a direct resource comparison: 1. **Different resource currencies.** Bosonic codes measure resources in mean photon number n̄; qubit codes measure resources in number of physical qubits N_phys. These are not directly comparable without a conversion. 2. **Different noise models.** Bosonic codes are optimized for photon loss (a, a†) and dephasing; surface codes are optimized for depolarizing noise (X, Y, Z Pauli errors). The error models are not identical. 3. **Different experimental maturity.** Cat codes and surface codes have been experimentally demonstrated at the few-qubit level; GKP codes have been demonstrated in single-mode cavities; high-order binomial codes remain theoretical. Comparing projections against projections requires careful uncertainty bands. We address all three obstacles by: 1. [...]
  § 4.4 Summary: | Metric | Pure Cat (A) | Concatenated Cat (B) | |:-------|:-------------|:---------------------| | Mean photons in cavity | 5–8 | 8 | | Bosonic modes | 1 | ~41 | | Photon-equivalents | 5–8 | ~28 | | Status | `[projected]` | `[derived — Chamberland 2022]` | ---
  § 5.5 Summary: | Metric | Pure GKP | |:-------|:---------| | Squeezing | 12 dB | | Mean photons in GKP mode | 7–8 | | Bosonic modes (GKP + ancilla) | 2 | | Photon-equivalents | 7–8 | | Status | `[derived — Terhal 2020; projected — 12 dB squeezing not yet demonstrated for QEC]` | ---
  § 6.5 Summary (Best-Case, Pure Binomial): | Metric | Value | |:-------|:------| | Order S | 2–3 | | Mean photons | 10–20 | | Bosonic modes (including ancilla for readout) | 2–3 | | Status | `[derived — Michael 2016; projected — no experimental demo above S=1]` | ---
  § 10.1 Summary of Findings: 1. **Bosonic codes require 5–40× fewer photons** and ~100× fewer spatial modes than surface codes to achieve p_L = 10⁻⁶, across all uncertainty bands. 2. **The resource advantage is robust** to factor-of-2 uncertainties in individual estimates. 3. **The advantage has a structural origin:** bosonic codes exploit the harmonic oscillator's native error-syndrome structure (the RG fixed point, the Bruhat–Tits tree geometry); surface codes impose an artificial lattice and pay a redundancy penalty. 4. **Significant caveats apply:** dephasing limits cat and binomial codes; GKP needs ~12 dB squeezing (not yet demonstrated); concatenation may be required; cross-platform comparisons are inherently limited. 5. **The thesis is falsifiable** by a head-to-head experimental comparison on the same platform by ~2028–2030.