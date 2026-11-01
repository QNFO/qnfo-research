# Beyond the Qubit: Constructive Paradigms for Post-Particle Computation (Corrected Edition, v2.2)

## Abstract

Survey papers shape how funders, journalists, and research groups allocate attention across quantum-computing platforms, so a factual error in a survey propagates into real decisions. This corrected edition of "Beyond the Qubit" repairs two unsupported claims found in the previous version. First, the prior text stated that non-Abelian anyons --- the exchange type needed for universal topological quantum computation --- were experimentally confirmed in 2020 in fractional quantum Hall systems. Verification against the primary literature shows this is wrong: the 2020 fractional quantum Hall measurements concerned Abelian anyons in the $\nu = 1/3$ state, whose exchange acts by a scalar phase of unit modulus, while for the leading non-Abelian candidate state at $\nu = 5/2$ the literature states that no direct experimental evidence for non-Abelian quasiparticles exists. Second, the prior text claimed that coherent Ising machines solve combinatorial optimization problems orders of magnitude faster than classical heuristics; no supporting quantitative evidence is available, and the claim is retracted and replaced with a hedged statement. The corrected edition retains the paper's constructive program --- correlation-first architectures, manufacturability as a first-class constraint, and a physical computation ecosystem --- and adds derived supporting numbers: an Abelian-exchange modulus $|R| = 1$, an estimated braid length of order $7$ elementary braids per gate at target precision $10^{-3}$, a measurement-iteration count of $100$ for $0.1$ precision in Jones-polynomial estimation, and an anyonic error-correction threshold of at least $3.7\%$. The corrections lower the assessed readiness of topological quantum computing and sharpen the paper's argument that the field's bottleneck is epistemic before it is engineering.

## 1. Introduction

The real-world problem this corrected edition bears on is the reliability of technical claims in fast-moving research surveys. Quantum-computing survey papers are read by program managers who decide which platforms receive funding, by journalists who translate them into public expectations, and by research groups who choose which experimental platform to join. When a survey states that a foundational experimental milestone has been reached --- here, that non-Abelian anyons were experimentally confirmed in 2020 --- readers downstream treat the milestone as closed and allocate effort accordingly. If the milestone has in fact not been reached, that misallocation is not cosmetic: it shifts years of effort and significant capital toward a platform whose enabling physics is unconfirmed, and it hides from newcomers the actual open problem, which is the experimental demonstration of non-Abelian exchange statistics itself. A second class of error, the unsupported performance claim --- here, that coherent Ising machines beat classical heuristics by orders of magnitude --- inflates expectations for analog optimization hardware in the same way. What changes if this paper's corrections hold: survey readers get an accurate readiness picture of topological quantum computing, in which the demonstration of non-Abelian anyons is an open experimental goal rather than a 2020 fact, and analog-optimization claims are held to the evidentiary standard of the cited literature.

This paper is a remediation of the previous edition of "Beyond the Qubit." The constructive program of that edition is unchanged: quantum mechanics, stripped of particle ontology, is a theory of correlations; the computational primitive is the correlation, not the qubit; and the manufacturable paths forward run through measurement-based, continuous-variable, topological, thermodynamic, neuromorphic, and optical paradigms judged against real engineering constraints. What changes here is the evidentiary hygiene of two passages, and the addition of explicit derivations for the quantitative statements the corrected text now makes.

The contributions are:

1. A verified correction of the 2020 non-Abelian-anyon claim, derived from the primary literature's own statements about what was and was not measured, with the corrected sentence given in Section 5 and the derivation in Section 4.
2. A retraction of the "orders of magnitude faster than classical heuristics" claim for coherent Ising machines, with the corrected sentence given in Section 5.
3. Explicit derivations, with shown arithmetic, of the quantitative statements the corrected text relies on: the unit-modulus scalar exchange phase that distinguishes Abelian from non-Abelian statistics (Section 4), the braid-length scaling estimate at finite target precision (Section 4), the measurement-iteration count for Jones-polynomial estimation (Section 4), and the anyonic error-correction threshold (Section 4).
4. A revised readiness assessment of topological quantum computing that follows from the correction, with the falsification condition stated (Sections 5 and 6).

## 2. Background and Related Work

The corrected claims sit at the intersection of two literatures: the experimental status of non-Abelian anyons, and the evidentiary status of analog Ising solvers. The anyon literature is well represented in the sources available to this revision, and each of the following works contributes a specific point that the corrected text uses.

The review by Lahtinen and Pachos-style pedagogy in [1] establishes the computational side of the ledger: the Fibonacci anyon model is the simplest anyon model that allows universal quantum computation by braiding alone, and the review works through the full pipeline --- braiding matrices, qubit encodings, single-qubit braids approximating target operations to accuracy $\epsilon$ with minimum braid length scaling as $\mathcal{O}(\log(1/\epsilon))$, and the AJL algorithm for evaluating the Jones polynomial --- including explicit numerical simulations of the braiding operations in MatLab. This matters for the correction because it shows precisely what a working topological quantum computer would require, and therefore what the unconfirmed experimental status of non-Abelian anyons is blocking: the entire braiding-only universality route runs through quasiparticles whose existence has not been demonstrated.

Nayak-style foundational context is supplied by [3], the comprehensive review of non-Abelian anyons and topological quantum computation. Its experimental-status statement is the single most important source for the first erratum: for the $\nu = 5/2$ fractional quantum Hall state, the leading non-Abelian candidate, the review states that "there is no direct experimental evidence for the non-Abelian nature of the quasiparticles," that direct measurement of the topological nature of the state has been minimal, and that the fundamental quasiparticles of the Moore-Read Pfaffian state carry charge $e/4$, which is one of the few directly accessible handles. The review also develops the link between anyon models and link invariants, giving the relation $V_{L}(q) = \frac{1}{d}(-q^{3/2})^{w(L)} K_{L}(q)$ between the Jones polynomial and the Kauffman bracket. The corrected edition uses [3] to establish that, as of the review's own accounting, the non-Abelian nature of fractional quantum Hall quasiparticles is a theoretical expectation, not a measurement.

The Abelian side of the 2020 measurements is documented in [9], the review of non-Abelian anyons and non-Abelian vortices in topological superconductors. Its introduction records that anyons "have been experimentally observed for $\nu = 1/3$ fractional quantum Hall states" citing the 2020 works of Bartolomei et al. and Nakamura et al. The $\nu = 1/3$ Laughlin state supports Abelian anyons: exchange multiplies the wavefunction by a scalar phase factor, exactly as [9] describes for anyons generally ("a wave function of two anyons receives a nontrivial phase factor under their exchanges"). The 2020 experiments therefore confirmed the anyon concept and fractional statistics, but in an Abelian channel. The same review supplies the universality constraint that the corrected edition's Section 3.3 retains: Ising anyons "are insufficient for universal quantum computations," while Fibonacci anyons, which would be universal, are expected in the $\nu = 12/5$ state --- a system even less experimentally characterized than $\nu = 5/2$.

The structural distinction between Abelian and non-Abelian exchange is made precise in [2], which constructs an explicit lattice realization of a non-Abelian topological memory in the $D(S_{3})$ quantum double model on a square lattice of six-level spins. Its central conceptual result, stated in its conclusions, is that two encodings in the fusion channels of the model's anyons are both fault-tolerant and locally indistinguishable, but one is distinguishable by LOCC protocols and equivalent to Abelian encodings while the other is distinguishable only by non-local operations --- "the true difference between Abelian and non-Abelian anyons from a quantum information perspective." This gives the corrected edition its operational criterion: non-Abelian statistics requires a degenerate manifold of locally indistinguishable ground states on which exchange acts as a non-commuting unitary transformation, not a scalar phase. The 2020 measurements, being phase measurements on $\nu = 1/3$ anyons, do not meet this criterion.

The universality gap for the most accessible non-Abelian anyons is quantified in [6], which studies continuous error correction for Ising anyons on an $L \times L$ lattice. Two of its results are used here. First, the gate set achievable by braiding Ising anyons "will not allow for universal quantum computation for any encoding," confirming that even a confirmed Ising-anyon platform would need non-topological supplement for universality. Second, its error-correction analysis --- which reduces the anyon error model to the well-studied toric-code bit-flip model with bit-flip rate $p$ and perfect syndrome measurements, and carries an analytical proof that $p_{c} \geq 3.7\%$ for that problem --- supplies the threshold number the corrected edition reports. The paper also notes the resource concern that using non-Abelian anyons as physical qubits for a further round of error correction "may carry a large resource overhead."

The route around the Ising-anyon universality gap inside the surface code is the subject of [4], which proposes hybrid islands of a qudit surface code based on the non-Abelian group $S_{3}$ embedded in the qubit surface code, connected by gapped domain walls between the $D(\mathbb{Z}_{2})$ and $D(S_{3})$ quantum double models. Transferring logical information across such a domain wall creates a non-stabilizer state, which combined with the surface code's Clifford gates yields universal quantum computation. Importantly for the readiness assessment, [4] states that full fault-tolerance of the scheme is not yet proven: it "must be shown that the logical error rate can be reduced arbitrarily by increasing the size of the islands," and the only current proof of full fault-tolerance concerns non-cyclic anyon models. This is exactly the kind of conditional, unproven status that the erroneous 2020 claim obscured.

The experimental-host question is broadened by [5], which shows that Ising anyons can be engineered in a superconductor/Abelian quantum Hall heterostructure: a spin-unpolarized $\nu = 2/3$ fractional quantum Hall backbone coupled to an $s$-wave superconductor, with a trench realizing a $\mathbb{Z}_{3}$ parafermion critical point at the boundary. This proposal family matters to the correction because it demonstrates that candidate non-Abelian platforms are engineered heterostructures whose operation is itself unverified, not existing devices. The host landscape is broadened further by [7], which proposes spin-liquid-based topological qubits in Kitaev materials, with two scalable design classes (magnetic tunnel junction arrays and semiconductor-coupled charge-anyon composites), while stating plainly that detecting individual anyons in non-Abelian Kitaev spin liquids "poses a daunting task" because the fractionalized degrees of freedom couple only weakly to local probes --- electrons from a lead cannot directly hybridize with emergent Majorana fermions born in the spin liquid.

The operational side of braiding is addressed by [10], which replaces adiabatic anyon transport with adiabatic variation of pairwise interactions in a T-junction geometry of four anyons, showing that the resulting Berry matrix matches the braiding operation and that residual ground-state splitting errors are suppressed exponentially in the number of anyons added to the system. This is relevant to the corrected edition's engineering assessment: even the gate-implementation mechanics of topological quantum computation remain at the level of proposals with error analyses, not demonstrated hardware. On the theory side, [11] investigates whether multiple-braiding in $SU(2)_{k}$ anyon models can realize universal quantum gate compilation, finding through analysis of the multiple elementary braiding matrices that multiple-braiding loses universality only when the braiding multiplicity collapses the matrices --- a compilation-theoretic result that presupposes, rather than provides, the physical anyons.

Finally, two works from the QNFO program bear on the conceptual framing. [12] analyzes the bounded-occupation family $\sum_{v_p(n) \le m} n^{-s} = \zeta(s)/\zeta((m+1)s)$ that interpolates between fermionic ($m = 1$) and bosonic ($m \to \infty$) statistics, and proves by direct computation that this counting family carries no exchange phase: the occupation-label exchange on the two-particle sector has eigenvalues $\{1, 1, -1\}$ for every cap $m \geq 2$, a permutation spectrum rather than a braid representation, so counting structure and exchange statistics are distinct layers. [14] establishes the invariant $R = e^{2\pi i s}$ relating the exchange phase of identical particles to their topological spin, with the boson/fermion dichotomy as the parity of $2s$ in three dimensions and arbitrary $e^{2\pi i s}$ phases describing anyons in two. Both are used in Section 4 to make the Abelian/non-Abelian distinction sharp: an Abelian exchange is a one-dimensional representation carrying a scalar of unit modulus, and the 2020 measurements confirmed exactly that.

## 3. Methods

This paper's method is claim-level remediation by source verification and minimal edit, combined with explicit derivation of every quantitative statement the corrected text retains.

**Claim extraction.** Two sentences in the previous edition were flagged for correction: (E1) the statement in Section 3.3 that the existence of non-Abelian anyons "was only experimentally confirmed in 2020 in fractional quantum Hall systems," and (E2) the statement in Section 5.2 that coherent Ising machines "have demonstrated solving combinatorial optimization problems orders of magnitude faster than classical heuristics for certain problem classes."

**Verification standard.** A factual claim about experimental status is retained only if a primary source states it. For E1, the relevant primary statements are: [9]'s record that anyons were experimentally observed in $\nu = 1/3$ fractional quantum Hall states in 2020 (Bartolomei et al.; Nakamura et al.), which are Abelian anyons; [3]'s statement that there is no direct experimental evidence for the non-Abelian nature of the $\nu = 5/2$ quasiparticles; and [2]'s operational criterion that non-Abelian statistics requires exchange acting as a non-commuting transformation on a degenerate manifold of locally indistinguishable states. For E2, no source available to this revision quantifies a speedup of coherent Ising machines over classical heuristics; the citation attached to the original sentence does not appear in the verified literature of this revision, so the quantitative claim fails the standard and is retracted.

**Minimal-edit principle.** Each correction changes the smallest text span that restores accuracy, preserving the surrounding argument. The corrected sentences are reported verbatim in Section 5.

**Derivation standard.** Every number in the corrected text is either derived in Section 4 with shown arithmetic from inputs stated in the cited sources, or labeled as an assumption or order-of-magnitude estimate with its unknown constant declared. No new experimental claim is introduced; this paper performs no measurement, simulation on hardware, or survey.

**Scope.** The remediation is confined to the two flagged sentences and to quantitative statements that the corrected text newly makes in their support. The remainder of the constructive program --- the ontological stripping, the five-paradigm survey, the manufacturability assessment, and the research agenda --- is carried forward unchanged from the previous edition, and its claims were not re-verified here except where the corrections touch them (notably the readiness assessment of topological quantum computing in Section 3.3, which the correction revises downward).

## 4. Analysis

This section derives every quantitative statement used by the corrected text. Each input is stated with its source; each arithmetic step is shown.

### 4.1 The exchange phase of an Abelian anyon has unit modulus

**Input 1.** [14] establishes the invariant relating exchange phase to topological spin: $R = e^{2\pi i s}$, where $s$ is the spin parameter, with arbitrary real $s$ describing anyons in two spatial dimensions.

**Input 2.** [9] states that a wave function of two anyons receives a nontrivial phase factor under their exchanges, and that anyons were experimentally observed in $\nu = 1/3$ fractional quantum Hall states in 2020.

**Input 3.** [2] states the operational content of non-Abelian statistics: local measurements on two non-Abelian quasiparticles cannot determine how they behave as a composite, so exchange acts on a degenerate manifold of locally indistinguishable states; [9] states that exchanges of non-Abelian anyons are described by unitary transformations operating on topologically protected degenerate ground states.

**Derivation.** For an Abelian anyon, the exchange operator is one-dimensional: it multiplies the wavefunction by the scalar $R = e^{2\pi i s}$ with $s \in \mathbb{R}$. Its modulus is

$$|R| = |e^{2\pi i s}| = \sqrt{\cos^{2}(2\pi s) + \sin^{2}(2\pi s)} = \sqrt{1} = 1,$$

since $\cos^{2}\theta + \sin^{2}\theta = 1$ for every real $\theta$. The exchange therefore acts by a phase of unit modulus --- a one-dimensional, hence necessarily commuting, representation. By contrast, a non-Abelian exchange requires a representation of dimension $d \geq 2$ acting on the degenerate ground-state manifold, per Inputs 2 and 3, because a one-dimensional representation of any group is commutative: for scalars $a, b \in \mathbb{C}$, $ab = ba$ identically.

**Conclusion.** The 2020 measurements recorded in [9] --- phase observations on $\nu = 1/3$ anyons --- confirmed exchange phases of the form $R = e^{2\pi i s}$ with $|R| = 1$: Abelian anyons. They did not, and could not, confirm the matrix-valued exchange on a locally indistinguishable degenerate manifold that defines non-Abelian statistics. This is the arithmetic core of Erratum E1.

### 4.2 Braid length at finite target precision

**Input.** [1] states that the minimum length of single-qubit braids approximating a required operation to accuracy $\epsilon$ scales as $\mathcal{O}(\log(1/\epsilon))$.

**Derivation.** Take a target precision $\epsilon = 10^{-3}$, a representative gate-synthesis target. Then

$$\log\frac{1}{\epsilon} = \log(10^{3}) = 3\log 10 = 3 \times 2.302585\ldots = 6.907755\ldots$$

using $\log 10 = 2.302585\ldots$ (natural logarithm). The scaling statement carries an unspecified model-dependent constant $c$, so the estimate is

$$L_{\text{braid}} \sim c \times 6.91,$$

i.e., of order $7$ elementary braids per approximated single-qubit gate for $c = 1$, and proportionally more for larger $c$. This is an order-of-magnitude estimate: the constant $c$ is not given by [1] and is declared unknown.

### 4.3 Measurement iterations for Jones-polynomial estimation

**Input.** [1] states that the precision of the AJL algorithm's convergence is determined primarily by the number of iterations $N$ of the Hadamard test, with convergence at a rate proportional to $1/\sqrt{N}$.

**Derivation.** Setting the statistical precision $\delta \propto N^{-1/2}$ and targeting $\delta = 0.1$ --- the error-bar width [1] reports for the trace closure of the figure-eight knot with $n = 3$ --- gives

$$N = \frac{1}{\delta^{2}} = \frac{1}{(0.1)^{2}} = \frac{1}{0.01} = 100.$$

So roughly $100$ Hadamard-test iterations are needed to reach $0.1$-level precision, up to the proportionality constant of the convergence rate. This is an estimate under the assumed proportionality $\delta = N^{-1/2}$; the constant is not given by [1].

### 4.4 Anyonic error-correction threshold

**Input.** [6] states that the anyon error model reduces to the toric-code bit-flip model with bit-flip rate $p$ and perfect syndrome measurements, and that an analytical proof gives $p_{c} \geq 3.7\%$ for that problem.

**Derivation.** No arithmetic is needed beyond unit conversion:

$$p_{c} \geq 3.7\% = \frac{3.7}{100} = 0.037.$$

The threshold is a lower bound on the correctable bit-flip rate for the anyon sector under the stated assumptions (perfect syndrome measurements; the fermion sector, which [6] treats separately with a more involved correlated error model, is not included in this bound).

### 4.5 Status of the coherent-Ising-machine claim

**Input.** The previous edition's sentence (E2) asserted a demonstrated speedup of "orders of magnitude" over classical heuristics for certain problem classes, attributed to coherent Ising machines. No source available to this revision states, measures, or derives any speedup factor for coherent Ising machines relative to classical heuristics.

**Derivation.** A claim of "orders of magnitude" is quantitative: it asserts a ratio $r$ between solution times or solution qualities satisfying $r \geq 10$ at minimum, and typically $r \geq 100$. With no source giving $r$, the claim has no derivable value. Under the verification standard of Section 3, a quantitative claim with no derivable value and no supporting source is retracted rather than re-estimated. The corrected sentence therefore makes no performance assertion; it characterizes coherent Ising machines by what they are (engineered analog systems whose dynamics minimize Ising-type cost functions) and marks their advantage over classical heuristics as unestablished at the level the original sentence claimed.

### 4.6 Summary of derived quantities

| Quantity | Value | Source of inputs | Status |
|---|---|---|---|
| Abelian exchange modulus $\lvert R \rvert$ | $1$ | [14], [9] | Derived (Section 4.1) |
| Braid length at $\epsilon = 10^{-3}$ | $\sim 6.91 \times c$ elementary braids | [1] | Order-of-magnitude, $c$ unknown |
| Hadamard-test iterations for $\delta = 0.1$ | $\sim 100$ | [1] | Estimate, proportionality constant unknown |
| Anyon error-correction threshold $p_{c}$ | $\geq 0.037$ | [6] | Cited bound, unit-converted |

## 5. Results

The results of this remediation are the two corrected sentences, the revised readiness statement they force, and the derived numbers of Section 4.

**Corrected sentence for Erratum E1 (replacing the Section 3.3 sentence of the previous edition).** The previous edition stated: "The existence of non-abelian anyons --- the type needed for universal quantum computation --- was only experimentally confirmed in 2020 in fractional quantum Hall systems." The corrected sentence is:

> "The existence of non-Abelian anyons --- the exchange type needed for universal topological quantum computation --- has not been experimentally confirmed. What was measured in 2020, in fractional quantum Hall experiments, were Abelian anyons in the $\nu = 1/3$ state, whose exchange acts by a scalar phase of unit modulus; for the leading non-Abelian candidate, the $\nu = 5/2$ state, the review literature states that there is no direct experimental evidence for the non-Abelian nature of the quasiparticles. Demonstrating non-Abelian exchange --- a unitary, non-commuting transformation on a degenerate manifold of locally indistinguishable states --- remains an open experimental goal."

**Corrected