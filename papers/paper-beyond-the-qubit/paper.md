# Beyond the Qubit: Constructive Paradigms for Post-Particle Computation

## Abstract

Survey literature shapes how funders, program managers, and research groups allocate attention across quantum-computing platforms, so a factual error in a survey propagates into real decisions. This paper repairs two such errors and adds a quantitative scaling analysis. First, it corrects the claim that non-Abelian anyons were experimentally confirmed in 2020 in fractional quantum Hall systems: the 2020 measurements concerned Abelian anyons in the $\nu = 1/3$ state, whose exchange acts by a scalar phase of unit modulus, while for the leading non-Abelian candidate at $\nu = 5/2$ the review literature states that no direct experimental evidence for non-Abelian quasiparticles exists. Second, it retracts the claim that coherent Ising machines solve combinatorial optimization problems orders of magnitude faster than classical heuristics, for which no supporting quantitative evidence is available. The paper retains the constructive program of correlation-first architectures and adds derived numbers: an Abelian exchange modulus $|R| = 1$, a braid length of order $7$ elementary braids per gate at target precision $10^{-3}$, a measurement-iteration count of $100$ for $0.1$ precision in Jones-polynomial estimation, an anyonic error-correction threshold of at least $3.7\%$, and — under explicitly stated assumptions — a fault-tolerance overhead of roughly $10^{3}$ physical qubits per logical qubit, i.e. $10^{5}$–$10^{6}$ physical qubits for $10^{2}$–$10^{3}$ logical qubits. The corrections lower the assessed readiness of topological quantum computing and locate the field's bottleneck in experimental confirmation before engineering scale-up.

## 1. Introduction

Two classes of error degrade decision-making in quantum-computing research today. The first is the premature announcement of a foundational experimental milestone. Quantum-computing survey papers are read by program managers who decide which platforms receive funding, by journalists who translate them into public expectations, and by research groups who choose which experimental platform to join. When a survey states that non-Abelian anyons — the exchange type needed for universal topological quantum computation — were experimentally confirmed in 2020, readers downstream treat the milestone as closed and allocate effort accordingly. If the milestone has in fact not been reached, that misallocation is not cosmetic: it shifts years of effort and significant capital toward a platform whose enabling physics is unconfirmed, and it hides from newcomers the actual open problem, which is the experimental demonstration of non-Abelian exchange statistics itself. The second class is the unsupported performance claim: the assertion that coherent Ising machines beat classical heuristics by orders of magnitude inflates expectations for analog optimization hardware in exactly the same way. What changes if this paper's corrections hold is that survey readers get an accurate readiness picture, in which the demonstration of non-Abelian anyons is an open experimental goal rather than a settled fact, and analog-optimization claims are held to the evidentiary standard of the cited literature.

A second pressure on the field is quantitative. Under the incumbent qubit-gate-circuit paradigm, fault-tolerant operation requires error correction, and error correction multiplies the physical hardware count. This paper quantifies that burden under explicitly stated assumptions: with a physical error rate $p = 10^{-3}$ against a code threshold $p_{\mathrm{th}} = 10^{-2}$, each logical qubit costs roughly $10^{3}$ physical qubits, so a commercially useful logical capacity of $10^{2}$–$10^{3}$ logical qubits demands $10^{5}$–$10^{6}$ physical qubits — a million-scale cryogenic control problem. If the assumptions hold, substrate choices that avoid or reduce the correction overhead deserve systematic attention alongside the universal digital scaffold.

Beneath both problems sits the paper's constructive thesis. Quantum mechanics, stripped of particle ontology, is a theory of correlations: the computational primitive is the correlation structure, not the qubit as a particle-like two-level object. Manufacturable paths forward run through measurement-based, continuous-variable, topological, thermodynamic, and analog paradigms judged against real engineering constraints — a "physical computation ecosystem" in which each substrate is matched to the algorithmic need it serves natively.

The contributions are:

1. A verified correction of the 2020 non-Abelian-anyon claim, derived from the primary literature's own statements about what was and was not measured, with the operational criterion that separates Abelian from non-Abelian exchange (Sections 2 and 4).
2. Explicit derivations, with shown arithmetic, of the quantitative statements the corrected analysis relies on: the unit-modulus scalar exchange phase (Section 4.1), the braid-length scaling estimate at finite target precision (Section 4.2), the measurement-iteration count for Jones-polynomial estimation (Section 4.3), and the anyonic error-correction threshold (Section 4.4).
3. A physical-qubit overhead derivation under stated assumptions, giving $\sim 10^{3}$ physical qubits per logical qubit and $10^{5}$–$10^{6}$ total for $10^{2}$–$10^{3}$ logical qubits, with uncertainty propagation (Section 4.5).
4. A revised readiness assessment of topological quantum computing that follows from the correction, with falsification conditions, limitations, and a smallest de-risking experiment (Sections 5, 6, and 7).

## 2. Background and Related Work

The corrected claims sit at the intersection of two literatures: the experimental status of non-Abelian anyons, and the evidentiary status of analog Ising solvers. Each of the following works contributes a specific point that the analysis uses.

The pedagogical review [1] establishes the computational side of the ledger: the Fibonacci anyon model is the simplest anyon model that allows universal quantum computation by braiding alone, and the review works through the full pipeline — braiding matrices, qubit encodings, single-qubit braids approximating target operations to accuracy $\epsilon$ with minimum braid length scaling as $\mathcal{O}(\log(1/\epsilon))$, and the AJL algorithm for evaluating the Jones polynomial — including numerical simulations of the braiding operations. This matters for the correction because it shows precisely what a working topological quantum computer would require, and therefore what the unconfirmed experimental status of non-Abelian anyons is blocking: the entire braiding-only universality route runs through quasiparticles whose existence has not been demonstrated.

Foundational context is supplied by [3], the comprehensive review of non-Abelian anyons and topological quantum computation. Its experimental-status statement is the single most important source for the first correction: for the $\nu = 5/2$ fractional quantum Hall state, the leading non-Abelian candidate, the review states that "there is no direct experimental evidence for the non-Abelian nature of the quasiparticles," that direct measurement of the topological nature of the state has been minimal, and that the fundamental quasiparticles of the Moore-Read Pfaffian state carry charge $e/4$, one of the few directly accessible handles. The review also develops the link between anyon models and link invariants, giving the relation $V_{L}(q) = \frac{1}{d}(-q^{3/2})^{w(L)} K_{L}(q)$ between the Jones polynomial and the Kauffman bracket. This paper uses [3] to establish that, as of the review's own accounting, the non-Abelian nature of fractional quantum Hall quasiparticles is a theoretical expectation, not a measurement.

The Abelian side of the 2020 measurements is documented in [9], the review of non-Abelian anyons and non-Abelian vortices in topological superconductors. Its introduction records that anyons "have been experimentally observed for $\nu = 1/3$ fractional quantum Hall states," citing the 2020 works of Bartolamei et al. and Nakamura et al. The $\nu = 1/3$ Laughlin state supports Abelian anyons: exchange multiplies the wavefunction by a scalar phase factor, exactly as [9] describes for anyons generally ("a wave function of two anyons receives a nontrivial phase factor under their exchanges"). The 2020 experiments therefore confirmed the anyon concept and fractional statistics, but in an Abelian channel. The same review supplies the universality constraint that Section 5 retains: Ising anyons "are insufficient for universal quantum computations," while Fibonacci anyons, which would be universal, are expected in the $\nu = 12/5$ state — a system even less experimentally characterized than $\nu = 5/2$.

The structural distinction between Abelian and non-Abelian exchange is made precise in [2], which constructs an explicit lattice realization of a non-Abelian topological memory in the $D(S_{3})$ quantum double model on a square lattice of six-level spins. Its central conceptual result, stated in its conclusions, is that two encodings in the fusion channels of the model's anyons are both fault-tolerant and locally indistinguishable, but one is distinguishable by LOCC protocols and equivalent to Abelian encodings, while the other is distinguishable only by non-local operations; [2] presents this as the operational distinction between Abelian and non-Abelian anyons from a quantum-information perspective. This gives the operational criterion used in Section 4: non-Abelian statistics requires a degenerate manifold of locally indistinguishable ground states on which exchange acts as a non-commuting unitary transformation, not a scalar phase. The 2020 measurements, being phase measurements on $\nu = 1/3$ anyons, do not meet this criterion.

The universality gap for the most accessible non-Abelian anyons is quantified in [6], which studies continuous error correction for Ising anyons on an $L \times L$ lattice. Two of its results are used here. First, the gate set achievable by braiding Ising anyons "will not allow for universal quantum computation for any encoding," confirming that even a confirmed Ising-anyon platform would need non-topological supplement for universality. Second, its error-correction analysis — which reduces the anyon error model to the well-studied toric-code bit-flip model with bit-flip rate $p$ and perfect syndrome measurements, and carries an analytical proof that $p_{c} \geq 3.7\%$ for that problem — supplies the threshold number reported in Section 4.4. The paper also notes the resource concern that using non-Abelian anyons as physical qubits for a further round of error correction "may carry a large resource overhead."

The route around the Ising-anyon universality gap inside the surface code is the subject of [4], which proposes hybrid islands of a qudit surface code based on the non-Abelian group $S_{3}$ embedded in the qubit surface code, connected by gapped domain walls between the $D(\mathbb{Z}_{2})$ and $D(S_{3})$ quantum double models. Transferring logical information across such a domain wall creates a non-stabilizer state, which combined with the surface code's Clifford gates yields universal quantum computation. Importantly for the readiness assessment, [4] states that full fault-tolerance of the scheme is not yet proven: it "must be shown that the logical error rate can be reduced arbitrarily by increasing the size of the islands," and the only current proof of full fault-tolerance concerns non-cyclic anyon models. This is exactly the kind of conditional, unproven status that the erroneous 2020 claim obscured.

The experimental-host question is broadened by [5], which shows that Ising anyons can be engineered in a superconductor/Abelian quantum Hall heterostructure: a spin-unpolarized $\nu = 2/3$ fractional quantum Hall backbone coupled to an $s$-wave superconductor, with a trench realizing a $\mathbb{Z}_{3}$ parafermion critical point at the boundary. This proposal family matters to the correction because it demonstrates that candidate non-Abelian platforms are engineered heterostructures whose operation is itself unverified, not existing devices. The host landscape is broadened further by [7], which proposes spin-liquid-based topological qubits in Kitaev materials, with two scalable design classes (magnetic tunnel junction arrays and semiconductor-coupled charge-anyon composites), while stating plainly that detecting individual anyons in non-Abelian Kitaev spin liquids "poses a daunting task" because the fractionalized degrees of freedom couple only weakly to local probes — electrons from a lead cannot directly hybridize with emergent Majorana fermions born in the spin liquid.

The operational side of braiding is addressed by [10], which replaces adiabatic anyon transport with adiabatic variation of pairwise interactions in a T-junction geometry of four anyons, showing that the resulting Berry matrix matches the braiding operation and that residual ground-state splitting errors are suppressed exponentially in the number of anyons added to the system. This is relevant to the engineering assessment in Section 7: even the gate-implementation mechanics of topological quantum computation remain at the level of proposals with error analyses, not demonstrated hardware. On the theory side, [11] investigates whether multiple-braiding in $SU(2)_{k}$ anyon models can realize universal quantum gate compilation, finding through analysis of the multiple elementary braiding matrices that multiple-braiding loses universality only when the braiding multiplicity collapses the matrices — a compilation-theoretic result that presupposes, rather than provides, the physical anyons.

On the analog-optimization side, this paper takes the conservative reading of the coherent-Ising-machine literature. Coherent Ising machines are engineered analog systems whose dynamics minimize Ising-type cost functions; no source available to this analysis states, measures, or derives a speedup factor for them relative to classical heuristics. We therefore assert no performance advantage for them, under the convention that a quantitative claim with no derivable value and no supporting source is retracted rather than re-estimated (Section 4.5). This choice is made explicitly because a stronger claim circulates in survey literature and could not be verified here.

## 3. Methods

The paper's method is claim-level verification against primary sources, combined with explicit derivation of every quantitative statement the corrected text retains and an explicitly assumed scaling model for error-correction overhead.

**Claim verification standard.** A factual claim about experimental status is retained only if a primary source states it. For the anyon-status question, the relevant primary statements are: [9]'s record that anyons were experimentally observed in $\nu = 1/3$ fractional quantum Hall states in 2020, which are Abelian anyons; [3]'s statement that there is no direct experimental evidence for the non-Abelian nature of the $\nu = 5/2$ quasiparticles; and [2]'s operational criterion that non-Abelian statistics requires exchange acting as a non-commuting transformation on a degenerate manifold of locally indistinguishable states. For the coherent-Ising-machine question, no source available states a speedup factor over classical heuristics, so the quantitative claim fails the standard and is retracted.

**Derivation standard.** Every number in the corrected text is either derived with shown arithmetic from inputs stated in the cited sources, or labeled as an assumption or order-of-magnitude estimate with its unknown constant declared. No new experimental claim is introduced; this paper performs no measurement, simulation on hardware, or survey.

**Scaling model.** For the error-correction overhead of Section 4.5, we assume a surface-code-style scheme with a physical error rate $p = 10^{-3}$ and a threshold $p_{\mathrm{th}} = 10^{-2}$, and we assume the overhead relation $N_{\mathrm{phys}} \approx \alpha (p_{\mathrm{th}}/p)^{\beta}$ with base factor $\alpha = 10^{2}$ and exponent $\beta = 1$. These three parameter choices are modeling assumptions of this paper, adopted for their representativeness of present superconducting-qubit error rates and the standard threshold scale; they are not attributed to any cited source. All calculations are analytical; uncertainty in $p$ is propagated as $\pm 10\%$, also an assumption.

**Scope.** The remediation is confined to the two corrected claims and to quantitative statements made in their support. The constructive program — the ontological stripping of particle language, the paradigm survey, and the research agenda — is carried forward, and its claims are re-examined only where the corrections touch them, notably the readiness assessment of topological quantum computing, which the correction revises downward.

## 4. Analysis

This section derives every quantitative statement used by the corrected text. Each input is stated with its source or labeled as an assumption; each arithmetic step is shown.

### 4.1 The exchange phase of an Abelian anyon has unit modulus

**Input 1.** [9] states that a wave function of two anyons receives a nontrivial phase factor under their exchanges, and that anyons were experimentally observed in $\nu = 1/3$ fractional quantum Hall states in 2020.

**Input 2.** [2] states the operational content of non-Abelian statistics: local measurements on two non-Abelian quasiparticles cannot determine how they behave as a composite, so exchange acts on a degenerate manifold of locally indistinguishable states; [9] states that exchanges of non-Abelian anyons are described by unitary transformations operating on topologically protected degenerate ground states.

**Derivation.** For an Abelian anyon, the exchange operator is one-dimensional: it multiplies the wavefunction by the scalar $R = e^{2\pi i s}$ with $s \in \mathbb{R}$. Its modulus is

$$|R| = |e^{2\pi i s}| = \sqrt{\cos^{2}(2\pi s) + \sin^{2}(2\pi s)} = \sqrt{1} = 1,$$

since $\cos^{2}\theta + \sin^{2}\theta = 1$ for every real $\theta$. The exchange therefore acts by a phase of unit modulus — a one-dimensional, hence necessarily commuting, representation. By contrast, a non-Abelian exchange requires a representation of dimension $d \geq 2$ acting on the degenerate ground-state manifold, per Input 2, because a one-dimensional representation of any group is commutative: for scalars $a, b \in \mathbb{C}$, $ab = ba$ identically.

### 4.2 Braid length at finite target precision

**Input 3.** [1] states that single-qubit braids approximating required operations to a desired accuracy $\epsilon$ have minimum braid length scaling as $\mathcal{O}(\log(1/\epsilon))$.

**Assumption 1.** The proportionality constant in the scaling law is of order unity; we take it to be exactly $1$ and the logarithm natural. This is a modeling assumption of this paper, adopted because [1] gives the scaling form but not a numerical constant, and because a constant of $1$ yields a conservative lower-end estimate.

**Derivation.** With the assumed form $L = \ln(1/\epsilon)$ and target precision $\epsilon = 10^{-3}$:

$$L = \ln\left(\frac{1}{10^{-3}}\right) = \ln(10^{3}) = 3\ln 10 = 3 \times 2.302585\ldots = 6.9078\ldots \approx 7.$$

So a single-qubit gate at $10^{-3}$ target precision requires a braid of order $7$ elementary braids under this assumption. The estimate is a lower-end figure: if the true proportionality constant exceeds $1$, or if the scaling carries the Solovay-Kitaev-type exponent power, the length grows accordingly. The number's role is to show that even the *theory-side* compilation cost is finite and modest; the binding uncertainty is physical, not combinatorial.

### 4.3 Measurement iterations for Jones-polynomial estimation

**Input 4.** [1] states that the precision of the AJL algorithm's convergence is determined primarily by the number of iterations of the Hadamard test, with convergence at a rate proportional to $1/\sqrt{N}$, where $N$ is the number of iterations and repeated measurements.

**Assumption 2.** The proportionality constant in the $1/\sqrt{N}$ convergence law is taken as $1$, so that the statistical precision equals $1/\sqrt{N}$. This is again a modeling assumption; [1] gives the rate but not the constant.

**Derivation.** Setting the target statistical precision $\delta = 0.1$:

$$\delta = \frac{1}{\sqrt{N}} \quad \Longrightarrow \quad N = \frac{1}{\delta^{2}} = \frac{1}{(0.1)^{2}} = \frac{1}{0.01} = 100.$$

So estimating a Jones-polynomial value to $0.1$ precision requires on the order of $100$ measurement iterations. [1] additionally notes that the uncertainty scales with the factor $d^{n-1}$ (trace closure) or $d^{n/2-1}$ (plat closure), where $1 < d < 2$ for $k > 3$ and $n$ is the strand number, so knots with more strands carry larger error bars at fixed $N$; the count of $100$ is therefore a per-knot, fixed-strand figure, not a universal constant.

### 4.4 Anyonic error-correction threshold

**Input 5.** [6] reduces the anyon error model for Ising anyons on an $L \times L$ lattice to the toric-code bit-flip model with bit-flip rate $p$ and perfect syndrome measurements, and states that an analytical proof gives $p_{c} \geq 3.7\%$ for that problem.

**Derivation.** The threshold is a cited bound, not a quantity this paper derives from first principles; the arithmetic here is unit conversion and margin comparison. Converting:

$$p_{c} \geq 3.7\% = \frac{3.7}{100} = 0.037.$$

Against the assumed physical error rate $p = 10^{-3}$ of Section 4.5, the margin is

$$\frac{p_{c}}{p} = \frac{0.037}{10^{-3}} = 37.$$

The operating point sits a factor of $37$ below the proven lower bound on the threshold. Two qualifications follow from [6]'s own analysis: the bound applies to the anyon sector under perfect syndrome measurements, while the fermion errors produced or swallowed during continuous correction generate a more involved correlated error model; and [6] notes that using non-Abelian anyons as physical qubits for a further round of error correction may carry a large resource overhead. The threshold therefore certifies the *anyon sector* of a hypothetical Ising-anyon architecture, not the architecture as a whole.

### 4.5 Fault-tolerance overhead under stated assumptions

**Assumption 3.** We assume a surface-code-style scheme with physical error rate $p = 10^{-3}$ and threshold $p_{\mathrm{th}} = 10^{-2}$, and the overhead relation

$$N_{\mathrm{phys}} \approx \alpha \left(\frac{p_{\mathrm{th}}}{p}\right)^{\beta}$$

with base factor $\alpha = 10^{2}$ and exponent $\beta = 1$. These parameter choices are modeling assumptions of this paper, adopted for their representativeness of present superconducting-qubit error rates and the standard threshold scale; they are not attributed to any cited source. Uncertainty in $p$ is propagated as $\pm 10\%$, also an assumption.

**Derivation.** Central value:

$$N_{\mathrm{phys}} = 10^{2} \times \left(\frac{10^{-2}}{10^{-3}}\right)^{1} = 10^{2} \times 10^{1} = 10^{3}.$$

Uncertainty propagation. With $p \in [0.9 \times 10^{-3},\ 1.1 \times 10^{-3}]$:

$$\frac{p_{\mathrm{th}}}{p}\bigg|_{p = 1.1 \times 10^{-3}} = \frac{10^{-2}}{1.1 \times 10^{-3}} = 9.0909\ldots, \qquad \frac{p_{\mathrm{th}}}{p}\bigg|_{p = 0.9 \times 10^{-3}} = \frac{10^{-2}}{0.9 \times 10^{-3}} = 11.1111\ldots$$

$$N_{\mathrm{phys}} \in \left[10^{2} \times 9.0909\ldots,\ 10^{2} \times 11.1111\ldots\right] = [909.09\ldots,\ 1111.11\ldots] \approx [9.1 \times 10^{2},\ 1.1 \times 10^{3}].$$

Total physical-qubit count for $N_{\mathrm{log}}$ logical qubits is $N_{\mathrm{tot}} = N_{\mathrm{log}} \times N_{\mathrm{phys}}$. At the interval endpoints:

$$N_{\mathrm{tot}}\big|_{N_{\mathrm{log}} = 10^{2},\ N_{\mathrm{phys}} = 909.09\ldots} = 9.09 \times 10^{4} \approx 10^{5},$$

$$N_{\mathrm{tot}}\big|_{N_{\mathrm{log}} = 10^{3},\ N_{\mathrm{phys}} = 1111.11\ldots} = 1.11 \times 10^{6} \approx 10^{6}.$$

So under the stated assumptions, a machine with $10^{2}$–$10^{3}$ logical qubits requires $10^{5}$–$10^{6}$ physical qubits. The dominant sensitivity is to the ratio $p_{\mathrm{th}}/p$. Under the assumed relation with $\beta = 1$, lowering $p$ to $10^{-4}$ gives $N_{\mathrm{phys}} = 10^{2} \times (10^{-2}/10^{-4})^{1} = 10^{2} \times 10^{2} = 10^{4}$, a tenfold increase relative to the central value $10^{3}$; this contradicts the known physical behavior of surface codes, whose overhead falls as $p$ decreases. The linear model with fixed $\alpha$ therefore does not reproduce the physical decrease of surface-code overhead away from threshold, and we restrict its validity to the stated operating point $p = 10^{-3}$ and its $\pm 10\%$ band, treating extrapolation outside that band as unsupported by the model. This restriction is itself a limitation of the derivation, recorded in Section 6. This restriction is itself a limitation of the derivation, recorded in Section 6.

## 5. Results

The paper's computed and cited numbers, each traced to its derivation in Section 4, are:

1. **Abelian exchange modulus** (Section 4.1): the exchange operator of an Abelian anyon acts by the scalar $R = e^{2\pi i s}$ with $|R| = 1$, a one-dimensional and therefore necessarily commuting representation. The $\nu = 1/3$ anyons observed in 2020, per [9], are of this type.

2. **Braid length** (Section 4.2): under the stated assumption of a unit proportionality constant, a single-qubit gate at target precision $\epsilon = 10^{-3}$ requires $L = \ln(10^{3}) = 6.908 \approx 7$ elementary braids.

3. **Measurement iterations** (Section 4.3): under the stated assumption of a unit proportionality constant in the $1/\sqrt{N}$ law, Jones-polynomial estimation to precision $0.1$ requires $N = 100$ measurement iterations.

4. **Anyonic error-correction threshold** (Section 4.4): $p_{c} \geq 0.037$ for the Ising-anyon anyon sector under the reduction of [6], a factor of $37$ above the assumed operating error rate $p = 10^{-3}$.

5. **Fault-tolerance overhead** (Section 4.5): under Assumption 3, $N_{\mathrm{phys}} \approx 10^{3}$ physical qubits per logical qubit, with the $\pm 10\%$ propagated band $[9.1 \times 10^{2},\ 1.1 \times 10^{3}]$, and $N_{\mathrm{tot}} \approx 10^{5}$–$10^{6}$ physical qubits for $10^{2}$–$10^{3}$ logical qubits.

6. **Corrected experimental status** (Sections 2 and 4.1): the 2020 fractional quantum Hall measurements recorded in [9] concerned Abelian anyons at $\nu = 1/3$; for the leading non-Abelian candidate at $\nu = 5/2$, [3] states there is no direct experimental evidence for the non-Abelian nature of the quasiparticles. The claim that non-Abelian anyons were experimentally confirmed in 2020 is therefore corrected to: the anyon concept and fractional statistics were confirmed in an Abelian channel; non-Abelian exchange statistics remain undemonstrated.

7. **Retracted performance claim** (Sections 2 and 3): the claim that coherent Ising machines solve combinatorial optimization problems orders of magnitude faster than classical heuristics is retracted, because no source available to this analysis states, measures, or derives such a speedup factor.

Items 1–5 are derived or converted with shown arithmetic under labeled assumptions; items 6–7 are claim-level corrections grounded in the cited sources' own statements.

## 6. Discussion

The corrections change the readiness picture, not the theoretical appeal, of topological quantum computation. The braiding-only universality route through Fibonacci anyons [1], the domain-wall route to universality inside the surface code [4], and the heterostructure and spin-liquid host proposals [5], [7] all remain internally coherent research programs. What the correction removes is the premise that their enabling physics has been demonstrated. Every one of these programs presupposes non-Abelian quasiparticles whose exchange statistics have not been measured; [3] states this directly for $\nu = 5/2$, and [9] records that the confirmed 2020 observations are Abelian.

**Limitations.** The quantitative results rest on the following assumptions, with their sensitivity:

- The braid-length estimate (Section 4.2) assumes a unit proportionality constant in $L = \ln(1/\epsilon)$. If the true constant is $c$, the estimate scales linearly in $c$; a constant of $3$ gives $L \approx 21$ rather than $7$. The qualitative conclusion (finite, modest compilation cost) is insensitive; the specific number is not.
- The measurement count (Section 4.3) assumes a unit constant in the $1/\sqrt{N}$ law and a fixed strand number. [1] states that uncertainty grows with the factor $d^{n-1}$ or $d^{n/2-1}$, so the count of $100$ underestimates the iterations needed for larger knots.
- The threshold figure (Section 4.4) is a cited lower bound for the anyon sector under perfect syndrome measurements; the correlated fermion error model of [6] is outside the bound, and the resource overhead of a second error-correction round is flagged by [6] as potentially large.
- The overhead model (Section 4.5) assumes $\alpha = 10^{2}$, $\beta = 1$, $p = 10^{-3}$, $p_{\mathrm{th}} = 10^{-2}$, and is valid only near the stated operating point: as shown in Section 4.5, the linear model does not extrapolate to substantially smaller $p$, where real surface-code behavior departs from it. The headline range $10^{5}$–$10^{6}$ inherits all four parameter choices; a different $\alpha$ shifts it proportionally.
- The claim-level corrections depend on the cited sources' own accounting: [3]'s statement is a review-level assessment, and a direct non-Abelian exchange measurement published after the review's accounting would supersede it.

**Falsification.** The main corrected claim — that non-Abelian exchange statistics in fractional quantum Hall systems are undemonstrated — would be falsified by a single published interference or fusion-channel measurement that satisfies the operational criterion of Section 4.1: exchange acting as a non-commuting transformation on a degenerate manifold of locally indistinguishable states, per the distinction established in [2]. Specifically, a measurement showing that quasiparticle exchange at $\nu = 5/2$ (or any other host) rotates the state within a locally indistinguishable degenerate subspace, rather than multiplying the wavefunction by a scalar phase, would overturn the correction and restore the stronger readiness assessment. The overhead result would be falsified if a demonstrated error-correction architecture achieved $10^{2}$–$10^{3}$ logical qubits with materially fewer than $10^{5}$ physical qubits at $p \approx 10^{-3}$, or if the threshold relevant to the full architecture (including the fermion sector) fell below the operating error rate.

**Open questions.** Whether the $\nu = 12/5$ state, which [9] identifies as the expected host of universal Fibonacci anyons, can be experimentally characterized at all remains open; [3] states that even less is known about it than about $\nu = 5/2$. Whether the domain-wall scheme of [4] admits a full fault-tolerance proof for cyclic anyon models is open by [4]'s own statement. Whether spin-liquid hosts can be probed at the single-anyon level is open, with [7] describing the detection problem as daunting because the fractionalized degrees of freedom couple only weakly to local probes.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The primary users are survey authors, program managers at funding agencies, and research-group leaders choosing experimental platforms. If the corrections hold, the decision that changes is the allocation of effort and capital: the demonstration of non-Abelian exchange statistics becomes the recognized gating milestone for topological quantum computing, rather than a presumed-completed step, and analog-optimization hardware claims are held to the standard of quantitative, sourced evidence. A secondary user is the experimental community working on $\nu = 5/2$ and $\nu = 12/5$ interferometry, for whom the operational criterion of Section 4.1 supplies the explicit target: demonstrate exchange as a non-commuting transformation on a locally indistinguishable degenerate manifold, not merely a phase.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this paper's own work is analytical and unreviewed: TRL 1–2. The corrected claims and derived numbers are at the level of basic principles and applied analysis. The hardware programs the assessment covers are likewise early: [5] and [7] are proposals with error analyses, not demonstrated devices; [10] shows that even the gate-implementation mechanics — braiding via pairwise interactions in a T-junction — remain at the level of proposals, with exponential protection in the number of added anyons proven analytically but not realized. No claim in this paper supports a readiness level above TRL 3 for any topological quantum computing architecture.

**(c) Smallest next experiment.** The smallest de-risking experiment is a Fabry-Pérot interferometry measurement on a $\nu = 5/2$ device that attempts to distinguish the even-odd quasiparticle-count oscillation pattern expected for non-Abelian exchange from the Abelian alternative, with the oscillation visibility and phase compared against the two statistics' predictions. The outcome that refutes the paper's corrected claim is a measured interference signal that matches the non-Abelian prediction and cannot be reproduced by an Abelian model with any choice of parameters. A complementary, cheaper first step is a calculation: a full numerical decoding study of the $D(S_{3})$ domain-wall syndrome of [4], which would establish or refute the arbitrary suppression of logical error rates with island size that [4] identifies as the open fault-tolerance question.

**(d) Binding constraints.** In order of first binding: (i) the experimental confirmation itself — no engineering pathway exists until exchange statistics are measured, per the criterion of Section 4.1; (ii) host-material quality — [5]'s heterostructure requires a spin-unpolarized $\nu = 2/3$ fractional quantum Hall backbone coupled to an $s$-wave superconductor with a trench realizing a $\mathbb{Z}_{3}$ parafermion critical point, a fabrication stack with no demonstrated working instance; (iii) detection — [7] states that individual anyons in non-Abelian Kitaev spin liquids couple only weakly to local probes, so readout is an open question for that host class; (iv) for the overhead estimate, the cryogenic control of $10^{5}$–$10^{6}$ physical qubits is the scale constraint, under Assumption 3. Whether the thermodynamic cost of such a system is dissipation-limited is an open question this paper does not quantify.

**(e) Order-of-magnitude bounds.** The only quantitative projection this paper offers is the overhead range of Section 4.5: $10^{3}$ physical qubits per logical qubit, $10^{5}$–$10^{6}$ total for $10^{2}$–$10^{3}$ logical qubits, labeled a projection under Assumption 3 with the $\pm 10\%$ propagated band. No cost, market, or performance figure beyond this is derivable from the sources or the model, and none is asserted.

**(f) Risks and misuse paths.** The corrected claims can be misused in the opposite direction: an inaccurate reading of this paper could support the claim that topological quantum computing is refuted rather than unconfirmed. The correction is about experimental status, not theoretical viability; [1], [2], [4], and [6] collectively establish that the theoretical pipeline is coherent. The retraction of the coherent-Ising-machine speedup claim likewise does not establish that such machines lack value; it establishes that a specific quantitative performance claim lacks supporting evidence in the sources available here.

## 8. Conclusion

This paper corrected two factual errors that propagate from survey literature into funding and research decisions, and it replaced the corrected text's qualitative posture with derived numbers. The 2020 fractional quantum Hall measurements confirmed Abelian anyons at $\nu = 1/3$, whose exchange acts by a scalar phase of unit modulus — derived in Section 4.1 as $|R| = 1$ for any one-dimensional exchange representation — while the non-Abelian status of the $\nu = 5/2$ quasiparticles remains, per [3], without direct experimental evidence. The claim of an orders-of-magnitude coherent-Ising-machine speedup was retracted for lack of any supporting quantitative source. The retained constructive program now carries explicit figures: a braid length of order $7$ elementary braids per gate at $10^{-3}$ target precision under a stated assumption, $100$ measurement iterations for $0.1$-precision Jones-polynomial estimation, an anyon-sector error-correction threshold of at least $3.7\%$, and — under explicitly labeled modeling assumptions — roughly $10^{3}$ physical qubits per logical qubit, i.e. $10^{5}$–$10^{6}$ physical qubits for $10^{2}$–$10^{3}$ logical qubits. The net effect is a downward revision of the assessed readiness of topological quantum computing and a relocation of its bottleneck: the field's gating problem is the experimental demonstration of non-Abelian exchange statistics itself, against the operational criterion that exchange act as a non-commuting transformation on a degenerate manifold of locally indistinguishable states. That demonstration, not engineering scale-up, is the milestone on which the paradigm's next assessment should turn.

## Version History

- Version 2.0.0 (2026-09-14, from 1.0.0): Adversarial audit revision. Fixes: no substantive corrections required.
- Version 3.0.0 (2026-11-01, from 2.1.0): rewritten in full through the research pipeline. new sections: Introduction; Background and Related Work; Methods; Analysis; Results; Discussion. sections folded or removed: The Textbook Picture and Its Projections; The Minimal Ontological Commitments of Quantum Mechanics; What Is NOT There: The Absent Ontology; The Relational Core: Quantum Mechanics as a Theory of Correlations; The Physical Meaning of "Quantum"; Measurement-Based Quantum Computing (MBQC). references 0 -> 10. length 7705 -> 5670 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.40.12-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 10 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Introduction to topological quantum computation with non-Abelian anyons. arXiv:1802.06176. https://arxiv.org/abs/1802.06176
[2] Universal quantum computation with a non-Abelian topological memory. arXiv:0906.2748. https://arxiv.org/abs/0906.2748
[3] Non-Abelian Anyons and Topological Quantum Computation. arXiv:0707.1889. https://arxiv.org/abs/0707.1889
[4] Universal quantum computation in the surface code using non-Abelian islands. arXiv:1811.06738. https://arxiv.org/abs/1811.06738
[5] Universal topological quantum computation from a superconductor/Abelian quantum Hall heterostructure. arXiv:1307.4403. https://arxiv.org/abs/1307.4403
[6] Continuous error correction for Ising anyons. arXiv:1508.04033. https://arxiv.org/abs/1508.04033
[7] Spin-liquid-based topological qubits. arXiv:2411.08093. https://arxiv.org/abs/2411.08093
[9] Non-Abelian Anyons and Non-Abelian Vortices in Topological Superconductors. arXiv:2301.11614. https://arxiv.org/abs/2301.11614
[10] Braiding of non-Abelian anyons using pairwise interactions. arXiv:1210.5452. https://arxiv.org/abs/1210.5452
[11] Universal Quantum Gate Compilation in $SU(2)_k$ Anyon Models via Multiple-Braiding. arXiv:2602.15324. https://arxiv.org/abs/2602.15324
