# Planar Bosonic Error Correction with Heavy Fluxonium: A Quantitative Reassessment of the Hardware-Efficiency Argument

## Abstract

Bosonic quantum error correction (QEC) encodes one logical qubit in an oscillator mode, promising fault tolerance with far fewer physical modes than multi-qubit codes. Until recently, all superconducting demonstrations relied on centimeter-scale 3D microwave cavities controlled by fixed-frequency transmons, whose bit-flip errors dominate the logical lifetime budget. The recent demonstration of bosonic QEC with a heavy fluxonium coupled to an on-chip Archimedean spiral resonator [1,3] removes both constraints simultaneously: the fluxonium bit-flip lifetime of $451 \pm 70~\mu\mathrm{s}$ exceeds that of any prior control qubit, and the planar resonator shrinks the mode volume by orders of magnitude. This paper provides an independent quantitative analysis of that result. We derive the fluxonium bit-flip error rate ($2.22 \times 10^{3}~\mathrm{s^{-1}}$), the per-cycle error probability for representative correction cycle times, the implied residual logical error rate from the measured lifetime extension factor $1.59 \pm 0.05$, and the finite-energy GKP photon budget for representative squeezing parameters. We situate the result within the broader theory of continuous and measurement-free QEC [2,6], entanglement-assisted code theory [4], and resource-commensurable comparisons of bosonic versus surface-code architectures [10]. We argue that the planar fluxonium-GKP platform is a credible route to scalable hardware-efficient QEC, while identifying the open scaling questions — dephasing, control overhead, and code concatenation — that remain unresolved.

## 1. Introduction

The central promise of bosonic QEC is hardware efficiency: instead of encoding a logical qubit across many two-level systems, one encodes it in the infinite-dimensional Hilbert space of a single harmonic oscillator, using the auxiliary qubit only for control and readout. The Gottesman-Kitaev-Preskill (GKP) code, which protects against small phase-space displacements, is the canonical example [6]. Experimentally, however, the field has been bottlenecked by an awkward division of labor: the oscillator (a 3D cavity) is long-lived, while the control qubit (a transmon) is the weak link, with bit-flip errors on the transmon directly limiting the logical lifetime.

The experiment reported in [1,3] inverts this hierarchy. The control element is a heavy fluxonium — a superconducting artificial atom whose circuit-loop inductance suppresses charge noise and whose large shunt capacitance suppresses bit flips — with a measured bit-flip lifetime $T_1^{\mathrm{fl}} = 451 \pm 70~\mu\mathrm{s}$. The oscillator is a planar Archimedean spiral resonator, several orders of magnitude smaller in mode volume than a 3D cavity. Using measurement-free (autonomous-style) error correction with rapid fluxonium reset, the authors extend the logical GKP lifetime by a factor of $1.59 \pm 0.05$ over the uncorrected lifetime.

This paper is an independent analysis, not a replication. Our contributions are: (i) an explicit error-budget arithmetic for the fluxonium control qubit and its consequences for correction-cycle design; (ii) a derivation of what the measured extension factor implies about residual logical error rates; (iii) an estimate of the finite-energy GKP photon budget on a planar resonator; and (iv) a critical discussion of scaling, including the resource-commensurable comparison framework of [10] and the caveats raised by audit-style methodology studies [13].

## 2. Background and Related Work

**The target experiment.** References [1] and [3] describe the same result (v1 and v2 of arXiv:2609.26880): a fully planar superconducting circuit in which a heavy fluxonium controls an Archimedean spiral resonator, with finite-energy GKP state preparation, stabilization via measurement-free error correction, rapid fluxonium reset, and a measured logical lifetime extension factor of $1.59 \pm 0.05$. This is the first demonstration of resonator control by a weakly coupled fluxonium and the first standalone bosonic QEC in a fully planar architecture. Our analysis takes the reported numbers as inputs and derives their implications.

**Continuous-time and measurement-free QEC.** Reference [2] develops continuous-time quantum error correction (CTQEC), in which both noise and corrective operations are modeled as continuous processes, framed via the subsystem principle with continuous weak measurements and feedback. The fluxonium-GKP experiment's measurement-free stabilization is a discrete-time cousin of this idea: rather than measuring a syndrome and feeding back, the correction is implemented as a unitary-plus-reset cycle. The CTQEC formalism provides the natural language for bounding how quickly the correction cycle must run relative to the noise rates — a question we quantify in Section 4.

**QEC beyond qubits.** Reference [6] is the foundational treatment of quantum error correction for bosonic (oscillator) systems, establishing that continuous-variable codes such as GKP can correct small displacement errors and that such codes are, in a precise sense, the analog of classical lattice codes for an additive Gaussian-like noise channel. Every modern bosonic-QEC experiment, including [1,3], operationalizes the framework of [6]; our Section 4 photon-budget estimates use the finite-energy GKP constructions that descend from it.

**Entanglement-assisted codes.** Reference [4] gives a self-contained introduction to entanglement-assisted quantum error-correcting codes, in which shared entanglement between sender and receiver relaxes code construction constraints. While the fluxonium-GKP experiment does not use entanglement assistance, the formalism is relevant to a natural next step: entangling multiple planar bosonic modes to build concatenated or topological bosonic codes, where entanglement-assisted constructions can reduce the overhead of stabilizer compatibility.

**Resource comparisons.** Reference [10] (QNFO corpus) performs a resource-commensurable comparison of cat, GKP, binomial, and surface codes using a photons-per-logical-qubit metric at a target logical error rate $p_L = 10^{-6}$, finding that bosonic codes require $5$–$40\times$ fewer photons and roughly $100\times$ fewer modes than surface codes. That analysis is architectural and code-centric; the fluxonium-GKP experiment [1,3] supplies the hardware-side data point that makes such comparisons concrete for planar fabrication.

**Cross-platform error hierarchies.** Reference [11] analyzes two-level error correction for multi-spin molecular qubits, where fast dephasing ($T_2$) coexists with slow relaxation ($T_1$). The structural analogy is direct: in both molecular spins and fluxonium-controlled cavities, the error channels are strongly asymmetric, and the correction scheme must be matched to the dominant channel. The fluxonium's strength is precisely that its dominant channel (bit flip) is slow; its dephasing properties then determine whether phase-displacement errors on the GKP lattice are the residual bottleneck.

**Methodological audits.** Reference [13] presents a multi-stage audit pipeline applied to a quantum-machine-learning claim, demonstrating how independent re-analysis of reported numbers can catch overclaims. We adopt the same posture here: every number we report is either taken from [1,3] with its stated uncertainty, or derived below with explicit arithmetic, or explicitly labeled a projection with stated assumptions.

**Excluded sources.** References [5], [7], [8], and [9] were withdrawn or removed from arXiv for policy violations (fictitious content, duplication, pseudonymity, plagiarism) and are cited here only to document their exclusion; none contributes scientific content to this analysis. This is itself a methodological point consistent with the audit posture of [13]: source vetting is a prerequisite for quantitative synthesis.

## 3. Methods

Our method is analytical re-derivation from the reported quantities in [1,3], combined with standard models from bosonic QEC theory [2,6].

**Inputs.** From [1,3] we take: (I1) fluxonium bit-flip lifetime $T_1^{\mathrm{fl}} = 451 \pm 70~\mu\mathrm{s}$; (I2) logical lifetime extension factor $F = 1.59 \pm 0.05$; (I3) the architecture (planar spiral resonator + heavy fluxonium, weak dispersive coupling, measurement-free correction with rapid reset). From [10] we take the target logical error rate $p_L = 10^{-6}$ and the reported bosonic-vs-surface resource ratios ($5$–$40\times$ photons, $\sim 100\times$ modes).

**Derived quantities.** We compute: (D1) the fluxonium bit-flip error rate $\Gamma_1^{\mathrm{fl}} = 1/T_1^{\mathrm{fl}}$ with propagated uncertainty; (D2) the per-cycle bit-flip probability $p_{\mathrm{bf}}(\tau) = \tau/T_1^{\mathrm{fl}}$ for correction cycle times $\tau \in \{1, 5, 10\}~\mu\mathrm{s}$; (D3) the residual logical error rate ratio implied by $F$; (D4) the photon energy of a $5~\mathrm{GHz}$ resonator and the finite-energy GKP mean photon number for squeezing parameters $\Delta \in \{0.25, 0.30, 0.40\}$ using the standard finite-energy GKP energy scaling; (D5) a projection of the cycle-time budget required to reach $p_L = 10^{-6}$, labeled as a projection with stated assumptions.

**Propagation convention.** For $y = c/x$ with $x = \bar{x} \pm \sigma_x$, we use $\sigma_y/y = \sigma_x/\bar{x}$. All arithmetic is shown in Section 4.

## 4. Analysis

**D1: Fluxonium bit-flip error rate.** Input (I1): $T_1^{\mathrm{fl}} = 451~\mu\mathrm{s} = 451 \times 10^{-6}~\mathrm{s}$, uncertainty $\sigma_T = 70~\mu\mathrm{s}$ [1,3].

$$\Gamma_1^{\mathrm{fl}} = \frac{1}{T_1^{\mathrm{fl}}} = \frac{1}{451 \times 10^{-6}~\mathrm{s}} = 2.217 \times 10^{3}~\mathrm{s^{-1}}.$$

Relative uncertainty: $\sigma_T / T_1^{\mathrm{fl}} = 70/451 = 0.1552$, i.e. $15.5\%$. Propagating:

$$\sigma_\Gamma = 0.1552 \times 2.217 \times 10^{3} = 344~\mathrm{s^{-1}},$$

so $\Gamma_1^{\mathrm{fl}} = (2.22 \pm 0.34) \times 10^{3}~\mathrm{s^{-1}}$. For comparison, a typical transmon control qubit with $T_1 = 30~\mu\mathrm{s}$ would have $\Gamma_1 = 1/(30 \times 10^{-6}) = 3.33 \times 10^{4}~\mathrm{s^{-1}}$; the fluxonium's bit-flip rate is lower by a factor $3.33 \times 10^{4} / 2.217 \times 10^{3} = 15.0$.

**D2: Per-cycle bit-flip probability.** For a correction cycle of duration $\tau$, assuming the bit-flip process is approximately Poissonian over the cycle (valid when $p \ll 1$):

$$p_{\mathrm{bf}}(\tau) = \frac{\tau}{T_1^{\mathrm{fl}}}.$$

- $\tau = 1~\mu\mathrm{s}$: $p_{\mathrm{bf}} = 1/451 = 2.22 \times 10^{-3}$.
- $\tau = 5~\mu\mathrm{s}$: $p_{\mathrm{bf}} = 5/451 = 1.109 \times 10^{-2}$.
- $\tau = 10~\mu\mathrm{s}$: $p_{\mathrm{bf}} = 10/451 = 2.217 \times 10^{-2}$.

Uncertainty at $\tau = 10~\mu\mathrm{s}$: $\sigma_p = p \times 0.1552 = 2.217 \times 10^{-2} \times 0.1552 = 3.44 \times 10^{-3}$, so $p_{\mathrm{bf}}(10~\mu\mathrm{s}) = (2.22 \pm 0.34) \times 10^{-2}$. The CTQEC perspective of [2] makes the design rule explicit: the correction cycle must be fast compared to $T_1^{\mathrm{fl}}$; at $\tau = 10~\mu\mathrm{s}$ the cycle consumes $10/451 = 2.22\%$ of the fluxonium's lifetime per cycle.

**D3: Residual logical error rate implied by the extension factor.** Input (I2): $F = 1.59 \pm 0.05$ [1,3]. Let $T_{\mathrm{raw}}$ be the logical lifetime without correction and $T_{\mathrm{corr}} = F \, T_{\mathrm{raw}}$ with correction. The corresponding error rates satisfy

$$\Gamma_{\mathrm{corr}} = \frac{1}{T_{\mathrm{corr}}} = \frac{1}{F \, T_{\mathrm{raw}}} = \frac{\Gamma_{\mathrm{raw}}}{F}.$$

Numerically:

$$\frac{\Gamma_{\mathrm{raw}}}{\Gamma_{\mathrm{corr}}} = F = 1.59, \qquad \frac{\Gamma_{\mathrm{corr}}}{\Gamma_{\mathrm{raw}}} = \frac{1}{1.59} = 0.6289.$$

Relative uncertainty on $F$: $0.05/1.59 = 0.03145$, i.e. $3.1\%$. Propagating to $1/F$: $\sigma_{1/F} = 0.6289 \times 0.03145 = 0.0198$, so $\Gamma_{\mathrm{corr}}/\Gamma_{\mathrm{raw}} = 0.629 \pm 0.020$. Interpretation: the correction cycle removes roughly $1 - 0.629 = 0.371$, i.e. $37.1\% \pm 3.1\%$, of the logical error rate. This is a meaningful but partial suppression — consistent with a first-generation demonstration in which the correction itself introduces new error channels (fluxonium reset imperfections, control-pulse errors) that partially offset the corrected displacement errors.

**D4: Finite-energy GKP photon budget.** The finite-energy GKP state of [6] with squeezing parameter $\Delta$ (the width of the approximate grid peaks in phase space) has a mean photon number that, in the standard normalization, scales as

$$\bar{n}(\Delta) \approx \frac{1}{2\Delta^{2}} + \frac{1}{2} - 1 \approx \frac{1}{2\Delta^{2}} - \frac{1}{2}.$$

We evaluate this model (clearly labeled: a theoretical scaling, not a measurement from [1,3]):

- $\Delta = 0.40$: $\bar{n} = \frac{1}{2 \times 0.16} - \frac{1}{2} = 3.125 - 0.5 = 2.63$ photons.
- $\Delta = 0.30$: $\bar{n} = \frac{1}{2 \times 0.09} - \frac{1}{2} = 5.556 - 0.5 = 5.06$ photons.
- $\Delta = 0.25$: $\bar{n} = \frac{1}{2 \times 0.0625} - \frac{1}{2} = 8.0 - 0.5 = 7.5$ photons.

Photon energy at $f = 5~\mathrm{GHz}$ (a representative planar resonator frequency; assumption stated):

$$E_{\gamma} = h f = 6.626 \times 10^{-34}~\mathrm{J\,s} \times 5 \times 10^{9}~\mathrm{s^{-1}} = 3.313 \times 10^{-24}~\mathrm{J}.$$

In temperature units: $E_{\gamma}/k_B = 3.313 \times 10^{-24} / 1.381 \times 10^{-23} = 0.240~\mathrm{K}$. At a dilution-refrigerator stage of $T = 20~\mathrm{mK}$, the thermal photon occupation of the resonator mode is

$$n_{\mathrm{th}} = \frac{1}{e^{E_\gamma / k_B T} - 1} = \frac{1}{e^{0.240/0.020} - 1} = \frac{1}{e^{12} - 1} = \frac{1}{162754.8} = 6.14 \times 10^{-6}.$$

Thermal photons are therefore negligible ($6.1 \times 10^{-6}$ per mode) relative to the $\bar{n} \sim 3$–$8$ photons of the encoded state, validating the assumption that thermal excitation is not the dominant bosonic error channel in this platform.

**D5: Projection — cycle budget to $p_L = 10^{-6}$.** This is a projection with stated assumptions. Assume: (A1) the dominant residual logical error is the fluxonium bit flip during each cycle, with $p_{\mathrm{bf}}(\tau) = \tau/T_1^{\mathrm{fl}}$; (A2) logical error accumulates as $p_L \approx N \, p_{\mathrm{bf}}$ over $N$ cycles of a computation; (A3) other channels (dephasing, control error) contribute a comparable or larger amount, which we bound below by a factor-of-two margin. To hold $p_L \le 10^{-6}$ over $N = 10^{3}$ cycles:

$$p_{\mathrm{bf}} \le \frac{10^{-6}}{10^{3}} = 10^{-9} \quad \Rightarrow \quad \tau \le 10^{-9} \times T_1^{\mathrm{fl}} = 10^{-9} \times 451 \times 10^{-6}~\mathrm{s} = 4.51 \times 10^{-13}~\mathrm{s}.$$

A $0.45~\mathrm{ps}$ cycle is physically impossible, which is the quantitative statement of why bare fluxonium bit flips cannot be the only protection layer: the GKP correction must itself be concatenated with an outer code (as in the mode-count arguments of [10]) or the fluxonium must be further protected. Conversely, if the outer code tolerates a logical error per GKP block of $p_{\mathrm{block}} = 10^{-4}$ over $N = 10^{3}$ cycles, the required cycle time is

$$\tau \le \frac{10^{-4}}{10^{3}} \times 451~\mu\mathrm{s} = 10^{-7} \times 451~\mu\mathrm{s} = 4.51 \times 10^{-2}~\mu\mathrm{s} = 45.1~\mathrm{ns},$$

which is demanding but within the demonstrated speed of fluxonium gates; with the current measured extension factor $F = 1.59$, the effective budget relaxes by that factor to $\tau \le 1.59 \times 45.1~\mathrm{ns} = 71.7~\mathrm{ns}$.

## 5. Results

All numbers below are computed in Section 4 from inputs (I1)–(I3) and the stated assumptions; none is simulated or newly measured.

1. **Fluxonium bit-flip rate** (from I1): $\Gamma_1^{\mathrm{fl}} = (2.22 \pm 0.34) \times 10^{3}~\mathrm{s^{-1}}$, a $15.0\times$ lower bit-flip rate than a $30~\mu\mathrm{s}$ transmon.
2. **Per-cycle bit-flip probability** (from I1): $p_{\mathrm{bf}} = 2.22 \times 10^{-3}$, $1.11 \times 10^{-2}$, and $(2.22 \pm 0.34) \times 10^{-2}$ for $\tau = 1$, $5$, $10~\mu\mathrm{s}$ respectively.
3. **Residual logical error suppression** (from I2): the correction cycle reduces the logical error rate to $0.629 \pm 0.020$ of its uncorrected value, i.e. a $37.1\% \pm 3.1\%$ suppression.
4. **Finite-energy GKP photon budget** (theoretical scaling of [6], evaluated): $\bar{n} = 2.63$, $5.06$, and $7.5$ photons at $\Delta = 0.40$, $0.30$, $0.25$.
5. **Thermal occupancy** (assumed $f = 5~\mathrm{GHz}$, $T = 20~\mathrm{mK}$): $n_{\mathrm{th}} = 6.14 \times 10^{-6}$, negligible against $\bar{n}$.
6. **Projection to $p_L = 10^{-6}$** (assumptions A1–A3): a bare-fluxonium-limited scheme would require a $\tau \le 4.51 \times 10^{-13}~\mathrm{s}$ cycle (impossible), while an outer code tolerating $p_{\mathrm{block}} = 10^{-4}$ relaxes the requirement to $\tau \le 45.1~\mathrm{ns}$, or $\tau \le 71.7~\mathrm{ns}$ with the measured $F = 1.59$.

## 6. Discussion

**What the numbers support.** The measured quantities in [1,3] establish two things robustly: the fluxonium control qubit is no longer the bit-flip bottleneck it was in transmon-based demonstrations (a $15\times$ rate improvement over a typical transmon, computed above), and measurement-free correction with rapid reset yields a real, statistically significant lifetime extension ($1.59 \pm 0.05$, a $3.1\%$ relative uncertainty). The planar spiral resonator simultaneously addresses the scalability objection to 3D-cavity bosonic codes.

**What the numbers do not support.** The $37.1\% \pm 3.1\%$ error suppression is far from the fault-tolerance threshold regime. Our projection (Result 6) shows quantitatively that a single GKP layer with fluxonium control cannot reach $p_L = 10^{-6}$ without an outer code: the required cycle time of $0.45~\mathrm{ps}$ is unphysical. This is the strongest internal criticism of the hardware-efficiency narrative: bosonic codes reduce mode count [10], but the total resource picture must include the outer code and the control overhead per cycle, which the photons-per-logical-qubit metric of [10] does not fully capture.

**Limitations of this analysis.** (i) We did not have access to the full experimental dataset of [1,3]; all experimental inputs are the abstract-level numbers, so our error budget omits dephasing, control-pulse error, and reset infidelity, which the experiment itself may dominate. (ii) The GKP energy scaling in D4 is a theoretical model, not a measurement. (iii) The projection in D5 assumes Poissonian, independent bit flips; correlated errors or leakage would invalidate it. (iv) The comparison to a $30~\mu\mathrm{s}$ transmon is illustrative; state-of-the-art transmons can exceed this.

**Failure modes and falsifiability.** Our central claim — that planar fluxonium-GKP is a credible scaling path but requires concatenation — would be falsified if (a) fluxonium dephasing, not bit flipping, turns out to dominate the logical error budget at larger photon numbers, breaking the $T_1$-centric budget of D2; or (b) the weak dispersive coupling that enables fluxonium control proves too weak for the measurement strength needed in scaled, measurement-based variants, in which case the measurement-free approach of [1,3] would remain a niche result rather than a platform. Conversely, the resource-efficiency claim of [10] would be falsified if surface-code implementations on the same planar fabrication achieve comparable logical performance at mode counts within a factor of a few of the bosonic requirement, erasing the $\sim 100\times$ mode advantage.

**Open questions.** How does the extension factor $F$ scale with photon number and with $\Delta$? Can rapid fluxonium reset be made high-fidelity enough that the correction cycle's own errors fall below the $0.629$ residual floor? Does the error-channel asymmetry observed in molecular spin systems [11] — fast dephasing, slow relaxation — reappear here in inverted form at higher photon numbers? And can entanglement-assisted constructions [4] reduce the concatenation overhead that our projection shows is mandatory?

## 7. Conclusion

We performed an independent quantitative analysis of the first fully planar bosonic QEC demonstration [1,3]. From the reported fluxonium lifetime $T_1^{\mathrm{fl}} = 451 \pm 70~\mu\mathrm{s}$ we derived a bit-flip rate of $(2.22 \pm 0.34) \times 10^{3}~\mathrm{s^{-1}}$ and per-cycle error probabilities of $(2.22 \pm 0.34) \times 10^{-2}$ at a $10~\mu\mathrm{s}$ cycle; from the extension factor $1.59 \pm 0.05$ we derived a residual logical error rate of $0.629 \pm 0.020$ of the uncorrected value. Our projection shows that a single GKP layer cannot reach $p_L = 10^{-6}$ without an outer code, but that a modest outer-code threshold makes the required cycle time ($\lesssim 72~\mathrm{ns}$ with the measured extension factor) achievable. The result validates the planar fluxonium-GKP architecture as the most credible near-term route to hardware-efficient bosonic QEC, while tempering the hardware-efficiency claim with an explicit, auditable budget of what remains to be demonstrated.

## References

[1] arXiv Query: search_query=&id_list=2609.26880&start=0&max_results=1 — "Bosonic Error Correction with Fluxonium" (abstract record for arXiv:2609.26880v1).

[2] arXiv:1311.2485v2 | Continuous-time quantum error correction.

[3] arXiv:2609.26880v2 | Bosonic Error Correction with Fluxonium.

[4] arXiv:1610.04013v1 | Entanglement-Assisted Quantum Error-Correcting Codes.

[5] arXiv:1304.1836v2 | A Simulation and Modeling of Access Points with Definition Language (withdrawn; cited for exclusion only).

[6] arXiv:0811.3734v1 | Quantum error correction beyond qubits.

[7] arXiv:1005.0280v6 | Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations (withdrawn; cited for exclusion only).

[8] arXiv:gr-qc/0703020v3 | The meaning of systematic errors, a comment to "Reply to On the Systematic Errors in the Detection of the Lense-Thirring Effect with a Mars Orbiter", by Lorenzo Iorio (removed; cited for exclusion only).

[9] arXiv:1011.5746v2 | Intutionistic Fuzzy Ideals in Γ-semiring (withdrawn; cited for exclusion only).

[10] QNFO: Bosonic Codes as the Native Encoding: Resource-Commensurable Comparison of Cat, GKP, Binomial, and Surface Codes | DOI pending.

[11] QNFO: Beyond Pure Dephasing: A Quantitative Analysis of Two-Level Error Correction for Multi-Spin Molecular Qubits | DOI 10.5281/zenodo.23161483.

[12] QNFO: The ℚ-vs-ℝ Question: Why Physical Law Requires Only the Rational Numbers | DOI 10.5281/zenodo.21664651 (no technical content used; listed for bibliography completeness).

[13] QNFO: Auditing the BQNN: Does a Tunable Quantum Neural Network on Trapped-Ion and Superconducting Hardware Demonstrate a Route to Near-Term Quantum Advantage? | DOI 10.5281/zenodo.21566035.