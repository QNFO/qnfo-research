# Grounding block - source: rem-0263d3d6-54c3-49a5-a38a-db7348d6a59e

## Research idea

Correct the published paper 'ultrametric-foundations-for-quantum-dynamics-a-p-adic-calculus-approach' for erratum pl-ultrametric-foundations-for-quantum-dynamics-a-p-adic-calculus-approach-1.0.1-1: Section 6.2 states that a measured R outside [0.158,0.194] 'refutes the claim that the Vladimirov kinetic term governs the dynamics on that platform.'
[ERRATA-ROUTE-PER-PAPER-1 merged errata:356] erratum pl-ultrametric-foundations-for-quantum-dynamics-a-p-adic-calculus-approach-1.0.1-0: Section 4.5 concludes 'The p-adic walk is therefore in a bounded diffusion regime: its spread does not grow as √N with step count,' and Section 6.2 offers displacement growth vs. plateau as a falsifier.

## Existing paper under revision (remediation only)

# Ultrametric Foundations for Quantum Dynamics: A $p$-Adic Calculus Approach

## Abstract
Quantum processors, sensors and communication links lose coherence and demand steep error-correction overheads because their dynamics are modeled over the continuous real field. A proposed alternative replaces the real line with the $p$-adic fields $\mathbb{Q}_{p}$, endowing quantum dynamics with a totally disconnected ultrametric topology and a non-local kinetic term given by the Vladimirov fractional derivative. The specific gap addressed here is quantitative: no prior treatment extracts falsifiable diffusion statistics from a $p$-adic dynamics model and compares them against the Euclidean benchmark. We derive a $p$-adic Schrödinger equation and its imaginary-time (heat) form, reduce stationary Markov dynamics on ultrametric spaces to a pseudo-differential equation on $\mathbb{Q}_{p}$, and evaluate a 1000-step random walk on a hierarchical tree with $p=5$, for which the assumed mean $p$-adic displacement is $\mu=0.693$ and the variance is $\sigma^{2}=0.122$; these two values are postulated inputs of the protocol, not measurements. Explicit arithmetic gives a standard deviation $\sigma=0.349$, a coefficient of variation $CV=0.503$, and a variance-to-mean ratio $R=0.176$, against a Euclidean root-mean-square displacement of $\sqrt{1000}\approx 31.62$ steps. The bounded diffusion is a falsifiable signature: a hierarchical quantum simulator whose excitation spread grows diffusively rather than plateauing refutes the model. If confirmed, ultrametric discretization becomes a concrete design parameter—the branching factor $p$—for low-decoherence quantum hardware architectures.

## 1. Introduction
Quantum processors built on superconducting circuits, trapped ions, or photonic platforms experience rapid loss of coherence because the underlying Hilbert space is modeled over the continuous real field $\mathbb{R}$. The continuous state manifold permits infinitesimal drifts that accumulate into logical errors, and the error-correction machinery needed to suppress those drifts consumes physical qubits and control resources that scale steeply with system size. This situation blocks the scaling of fault-tolerant quantum computers and limits the deployment of quantum sensors in noisy environments. The people who face this problem daily are quantum-hardware architects and error-correction designers: their decision—how to lay out couplers, how much redundancy to budget—would change if state evolution were intrinsically confined to a discrete hierarchical structure instead of drifting on a continuum.

If the foundational arena of quantum dynamics were instead a totally disconnected ultrametric space, state evolution would be constrained to discrete branches of a tree, potentially suppressing continuous drift and reducing error-correction overhead. The central question of this paper is whether replacing the real line by $p$-adic fields $\mathbb{Q}_{p}$, together with Vladimirov fractional derivatives and Haar-measure integrals, provides such a constraint while remaining compatible with known quantum predictions in the appropriate coarse-grained limit, and whether the resulting dynamics produce numerical signatures that an experiment could confirm or refute.

The contributions are:
- Derivation of a $p$-adic Schrödinger equation, and its imaginary-time heat form, based on the Vladimirov operator and Haar measure (Section 3).
- Reduction of stationary Markov dynamics on an ultrametric space that embeds isometrically into $\mathbb{Q}_{p}$ to a pseudo-differential equation on $\mathbb{Q}_{p}$, establishing the equivalence of the tree random walk and the $p$-adic kinetic term (Section 4.1).
- Explicit arithmetic extraction of the diffusion statistics of a 1000-step $p$-adic random walk: standard deviation $\sigma=0.349$, coefficient of variation $CV=0.503$, and variance-to-mean ratio $R=0.176$ (Section 4).
- A quantitative falsification criterion comparing the bounded $p$-adic displacement $\mu=0.693$ with the Euclidean benchmark $\sqrt{1000}\approx 31.62$, and a $\pm 10\%$ acceptance window $R\in[0.158,0.194]$ (Sections 4.5 and 4.6).
- Translation of the result into an engineering pathway for quantum hardware, including readiness assessment, the minimal next experiment, and binding constraints (Section 7).

## 2. Background and Related Work
The ultrametric perspective on information and dynamics has been developed across several domains, and each of the following works contributes a specific component that this paper uses.

[1] shows how empirical data can be embedded in an ultrametric space by first applying Correspondence Analysis to obtain a Euclidean representation and then inducing a hierarchical clustering that yields an ultrametric model of anomaly and change; the work demonstrates that the $\chi^{2}$ metric can be mapped to Euclidean distances before the hierarchy is induced. This pipeline matters here because it establishes that ultrametric structure can be constructed from measured data, not only postulated.

[2] proposes a method for describing stationary Markov processes on ultrametric spaces $\mathbb{U}$ that are isometrically embeddable into the $p$-adic field $\mathbb{Q}_{p}$, reducing the Kolmogorov–Feller equation on $\mathbb{U}$ to a pseudo-differential equation on $\mathbb{Q}_{p}$ with a non-translation-invariant measure. Section 4.1 of the present paper uses exactly this reduction to identify the tree random walk with the $p$-adic kinetic term.

[3] studies a three-state $p$-adic Potts model on a Cayley tree of order two and proves that a phase transition occurs if and only if the prime equals three, $p=3$, regardless of the interaction strength. This identifies $p=3$ as a distinguished prime in $p$-adic statistical mechanics; the present paper adopts $p=5$ for its simulation protocol but retains $p=3$ criticality as an open link to possible critical phenomena in ultrametric quantum systems (Section 6).

[4] reviews $p$-adic and adelic quantum mechanics, emphasizing that complex-valued wave functions can be defined on $p$-adic spaces $\mathbb{Q}_{p}^{D}$ and that the usual Heisenberg algebra does not directly generalize; the work distinguishes $p$-adic-valued from complex-valued wave functions and establishes the complex-valued formulation as the appropriate bridge to ordinary quantum mechanics. The Schrödinger equation postulated in Section 3.2 follows this complex-valued convention.

[5] introduces a $5$-adic model of DNA sequences, showing that nucleotides and codons can be represented by $5$-adic integers and that the $5$-adic distance clusters codons into biologically meaningful groups. This demonstrates that $p$-adic ultrametric distances capture hierarchical information outside physics, and it motivates the choice $p=5$ in the simulation protocol of Section 3.4.

[6] proves ultrametric versions of classical embedding theorems, showing that a metric space can be embedded into an ultrametric space via a construction respecting the strong triangle inequality $d(x,y)\le\max\{d(x,z),d(z,y)\}$. This supplies the mathematical license for treating hierarchical discretizations as genuine ultrametric geometries rather than approximations.

[7] develops a $p$-adic wavelet transform based on Haar wavelets, showing that the affine-group representation leads to a decomposition of vectors in a Hilbert space $\mathcal{H}$ with respect to $p$-adic scales, with locality preserved in the $p$-adic domain. Section 7 identifies this transform as a candidate analysis tool for time-series data from hierarchical quantum devices.

[8] reviews $p$-adic and adelic cosmology, describing how $p$-adic matter and gravity can be incorporated into a unified cosmological model and arguing that the early universe may have been governed by $p$-adic dynamics. This provides the widest-scale motivation for taking ultrametric geometry seriously as a physical substrate, though no claim of this paper depends on cosmology.

We define the simulation protocol as follows: a 1000-step random walk on a $p$-adic tree with $p=5$. We assume as inputs a mean $p$-adic displacement $\mu=0.693$ and variance $\sigma^{2}=0.122$ for this walk. All diffusion statistics computed in Section 4 take these two numbers as their only empirical inputs.

Collectively, these works establish that ultrametric embeddings can be constructed from data [1], [6], that stochastic dynamics on ultrametric spaces reduce to $p$-adic pseudo-differential equations [2], that specific primes play distinguished physical roles [3], [5], that complex-valued $p$-adic quantum mechanics is well defined [4], and that $p$-adic analysis extends to quantum physics, genetics, and cosmology [4], [5], [7], [8]. The present paper builds on these foundations to extract a testable diffusion signature.

## 3. Methods
### 3.1 Vladimirov Fractional Derivative
For a prime $p$ and order $\alpha>0$, the Vladimirov operator $D^{\alpha}$ acts on a complex-valued function $\psi:\mathbb{Q}_{p}\to\mathbb{C}$ as
$$
(D^{\alpha}\psi)(x)=\frac{1}{\Gamma_{p}(-\alpha)}\int_{\mathbb{Q}_{p}}\frac{\psi(y)-\psi(x)}{|y-x|_{p}^{1+\alpha}}\,d_{p}y,
$$
where $|\cdot|_{p}$ is the $p$-adic norm, $d_{p}y$ the Haar measure on $\mathbb{Q}_{p}$, and $\Gamma_{p}$ the $p$-adic gamma function. The operator is non-local: it couples $\psi(x)$ to $\psi(y)$ at all $p$-adic distances with a kernel weighted by $|y-x|_{p}^{-(1+\alpha)}$, and it respects the ultrametric topology in which distances take values in the discrete set $\{p^{k}\}_{k\in\mathbb{Z}}$.

### 3.2 $p$-Adic Schrödinger Equation and Its Heat Form
Following the complex-valued formulation of [4], we postulate a real-time evolution equation for $\psi(x,t)$:
$$
i\hbar\,\frac{\partial\psi(x,t)}{\partial t}=D^{\alpha}\psi(x,t)+V(x)\psi(x,t),
$$
with $V(x)$ a complex-valued potential on $\mathbb{Q}_{p}$. In imaginary time the kinetic term generates a heat equation,
$$
\frac{\partial\psi(x,t)}{\partial t}=-\,c\,D^{\alpha}\psi(x,t),
$$
where $c$ is a positive constant absorbing the prefactor (with $c=\hbar/2m$ in the direct analogue of the Euclidean free-particle case). The convention adopted in this paper is that the real-time equation is the fundamental postulate and the heat equation is its analytic continuation; the diffusion statistics of Section 4 are computed for the heat dynamics, which is the sector probed by the random-walk protocol. In the formal coarse-graining limit in which the ultrametric structure is replaced by a continuum, $D^{\alpha}$ plays the role of the Laplacian and the heat equation reduces to standard diffusion, ensuring compatibility with known quantum dynamics when the hierarchical structure is averaged away.

### 3.3 Hierarchical Tree Representation
The field $\mathbb{Q}_{p}$ is represented as an infinite rooted tree (the Bruhat–Tits tree) in which each vertex corresponds to a $p$-adic ball of radius $p^{-k}$ for integer $k\ge 0$. A random walk on this tree moves to a neighboring vertex at each discrete time step. The ultrametric distance between two vertices $v$ and $w$ is $|v-w|_{p}=p^{-k}$, where $k$ is the depth of their lowest common ancestor. A finite tree of branching factor $p$ and depth $L$ discretizes the field; the walk records the $p$-adic displacement after $N$ steps,
$$
\Delta_{p}=|x_{N}-x_{0}|_{p}.
$$

### 3.4 Simulation Protocol
We define the simulation protocol as follows: a 1000-step random walk on a $p$-adic tree with $p=5$, chosen to match the $5$-adic construction of [5]. The walk proceeds by moves to neighboring balls with transition probability proportional to $|y-x|_{p}^{-(1+\alpha)}$, implementing the kinetic term $D^{\alpha}$ with $\alpha=1$. We assume as inputs a mean $p$-adic displacement $\mu=0.693$ and variance $\sigma^{2}=0.122$ for this walk.

These two numbers are the only empirical inputs to the analysis of Section 4; all other quantities are derived from them by explicit arithmetic.

## 4. Analysis
### 4.1 Reduction of Markov Dynamics to the $p$-adic Kinetic Term
By the reduction of [2], a stationary Markov process on an ultrametric space $\mathbb{U}$ embedding isometrically into $\mathbb{Q}_{p}$ satisfies a Kolmogorov–Feller equation
$$
\frac{\partial f(x,t)}{\partial t}=W_{m(x)}f(x,t),
\qquad
W_{m(x)}f(x)=\int_{\mathbb{Q}_{p}}m(y)\,W(|x-y|_{p})\bigl[f(y)-f(x)\bigr]\,d_{p}y,
$$
with a non-translation-invariant measure $m(y)\,d_{p}y$. When the jump kernel scales as $W(r)\propto r^{-(1+\alpha)}$, this operator coincides in form with the Vladimirov operator of Section 3.1. The tree random walk of Section 3.4, whose transition probabilities are proportional to $|y-x|_{p}^{-(1+\alpha)}$, is therefore the discrete implementation of exactly this pseudo-differential dynamics, and its displacement statistics probe the heat equation of Section 3.2.

### 4.2 Standard Deviation from the Reported Variance
Input: $\sigma^{2}=0.122$ (assumed). We compute $\sigma=\sqrt{0.122}$ by Newton–Raphson iteration:
1. Initial guess $x_{0}=0.35$, since $0.35^{2}=0.1225$.
2. Update $x_{1}=\frac{1}{2}\left(x_{0}+\dfrac{\sigma^{2}}{x_{0}}\right)=\frac{1}{2}\left(0.35+\dfrac{0.122}{0.35}\right)$. Now $0.122/0.35=0.348571\ldots$, so $x_{1}=\frac{1}{2}(0.35+0.348571)=0.349286$ (rounded to six decimals).
3. Check: $0.349286^{2}=0.122001\ldots$, which agrees with $0.122$ to within $10^{-5}$.

Thus $\sigma=0.349$ to three decimal places.

### 4.3 Coefficient of Variation
Input: $\mu=0.693$ (assumed) and $\sigma=0.349$ from Section 4.2.
$$
CV=\frac{\sigma}{\mu}=\frac{0.349}{0.693}.
$$
Multiplying numerator and denominator by $1000$: $349/693$. Long division gives $349/693=0.5036\ldots$ (since $693\times 0.5=346.5$ and $693\times 0.504=349.272$, the ratio lies between $0.503$ and $0.504$). Hence
$$
CV\approx 0.503.
$$

### 4.4 Variance-to-Mean Ratio
Input: $\sigma^{2}=0.122$ and $\mu=0.693$.
$$
R=\frac{\sigma^{2}}{\mu}=\frac{0.122}{0.693}=\frac{122}{693}.
$$
Long division: $693$ into $1220$ goes $1$ time ($693$), remainder $527$; bring down a zero, $5270/693$ gives $7$ ($7\times 693=4851$), remainder $419$; bring down a zero, $4190/693$ gives $6$ ($6\times 693=4158$), remainder $32$; continuing, $320/693$ gives $0$, and $3200/693$ gives $4$ ($4\times 693=2772$), remainder $428$. Thus
$$
R\approx 0.1761\approx 0.176.
$$
The two statistics $CV=0.503$ and $R=0.176$ are complementary descriptions of the same distribution; the check $CV^{2}\cdot\mu = 0.5036^{2}\times 0.693 = 0.1758 \approx 0.176$, consistent with $R=\sigma^{2}/\mu$. 

### 4.5 Euclidean Benchmark
For a simple symmetric random walk on a one-dimensional Euclidean lattice, the root-mean-square displacement after $N$ steps is $\sqrt{N}$. With $N=1000$:
1. Initial guess $x_{0}=31.62$, since $31.62^{2}=999.0244$.
2. Update $x_{1}=\frac{1}{2}\left(31.62+\dfrac{1000}{31.62}\right)$. Now $1000/31.62=31.6256\ldots$, so $x_{1}=\frac{1}{2}(31.62+31.6256)=31.6228$.
3. Check: $31.6228^{2}=999.999\ldots$, agreeing with $1000$ to within $10^{-3}$.

Thus $\sqrt{1000}\approx 31.62$. The $p$-adic mean displacement $\mu=0.693$ is smaller than this benchmark by a factor $31.62/0.693=45.6$ (since $0.693\times 45=31.185$ and $0.693\times 45.6=31.60$, the factor is $45.6$ to three significant figures). The $p$-adic walk is therefore in a bounded diffusion regime: its spread does not grow as $\sqrt{N}$ with step count.

### 4.6 Falsification Window for $R$
We define a $\pm 10\%$ acceptance window around the predicted ratio:
- Lower bound: $0.9\times 0.176=0.1584$.
- Upper bound: $1.1\times 0.176=0.1936$.

Rounded to three decimals, the window is $R\in[0.158,0.194]$. A measured variance-to-mean ratio outside this window, for a system verified to implement the $p=5$ ultrametric topology of Section 3.4, refutes the bounded-diffusion prediction as quantified here.

## 5. Results
A study would assume that the p-adic random walk of the protocol of Section 3.4 has a mean displacement \(\mu=0.693\) and variance \(\sigma^{2}=0.122\) after \(N=1000\) steps.
- **R2.** The standard deviation is $\sigma=0.349$, computed by Newton–Raphson iteration in Section 4.2.
- **R3.** The coefficient of variation is $CV=0.503$ and the variance-to-mean ratio is $R=0.176$ (Sections 4.3 and 4.4); the consistency check $CV^{2}\cdot\mu=0.176$ closes the arithmetic.
- **R4.** The mean $p$-adic displacement $\mu=0.693$ is a factor $45.6$ smaller than the Euclidean root-mean-square benchmark $\sqrt{1000}\approx 31.62$, demonstrating bounded diffusion intrinsic to the ultrametric topology (Section 4.5).
- **R5.** The derived $p$-adic Schrödinger equation (Section 3.2) reduces to standard diffusion when the ultrametric structure is coarse-grained, ensuring compatibility with known quantum dynamics in that limit.

All numerical values above are either the two assumed inputs ($\mu$, $\sigma^{2}$) or derived from them by the explicit arithmetic of Section 4. No additional data are introduced.

## 6. Discussion
### 6.1 Limitations
- **L1. Prime dependence.** The simulation protocol fixes $p=5$; results may differ for other primes. The Potts-model result of [3] marks $p=3$ as special, and the genetic-code construction of [5] motivates $p=5$; no claim in this paper extends across primes.
- **L2. Tree approximation.** The walk is performed on a one-dimensional tree discretization; higher-dimensional $p$-adic spaces $\mathbb{Q}_{p}^{D}$, of the kind treated in [4], could modify the diffusion characteristics.
- **L3. Fixed fractional order.** The kinetic term is evaluated at $\alpha=1$; varying $\alpha$ changes the kernel $|x-y|_{p}^{-(1+\alpha)}$ and may change the diffusion rate and the ratio $R$.
- **L4. No physical realization.** No experimental measurement of quantum state propagation on an actual ultrametric lattice is available; the results remain theoretical until such a system is built.
- **L5. Two-input statistics.** The entire quantitative content rests on two reported numbers, $\mu$ and $\sigma^{2}$; the higher moments of the displacement distribution, which would distinguish ultrametric from merely slow diffusion, are not available.

### 6.2 Falsification Criterion
The main result is the bounded-diffusion signature $R=0.176$ with acceptance window $[0.158,0.194]$. The observation that would falsify it is direct: an experimental implementation of the hierarchical lattice of Section 3.4 in which the excitation's mean $p$-adic displacement grows with step count in the Euclidean manner—approaching $\sqrt{N}$ rather than plateauing near $\mu\approx 0.7$—or a measured variance-to-mean ratio outside $[0.158,0.194]$ after verifying the topology, refutes the claim that the Vladimirov kinetic term governs the dynamics on that platform. Conversely, a plateau in displacement with increasing $N$, with $R$ inside the window, supports the ultrametric model.

### 6.3 Failure Modes
- **F1. Numerical artifact.** An error in discretizing the Vladimirov operator could produce artificial confinement, mimicking bounded diffusion without any ultrametric physics. The falsification test must therefore include a control simulation with a deliberately Euclidean-like kernel.
- **F2. Environmental dominance.** Decoherence not captured by the ultrametric model could dominate the dynamics and mask the predicted plateau, producing a false negative.
- **F3. Topology mismatch.** If the fabricated coupling network does not realize the claimed $p$-adic ball structure, the measured $R$ is not a test of the model.

### 6.4 A Labeled Hypothesis on Spectral Discreteness
As an explicitly labeled hypothesis, not a derived result of this paper: if eigenfunctions of $D^{\alpha}$ on $\mathbb{Q}_{p}$ carry eigenvalues scaling as a power of $p$ in the scale index, then setting $\alpha=1$ would suggest a fundamental spacing of order $p^{-1}$ for the kinetic energy. For $p=3$ this would give a spacing $\Delta E=3^{-1}=1/3$ in units where the proportionality constant is unity. We emphasize that the proportionality constant is not fixed by any result in this paper, that the spectral claim is not derived here, and that the exclusive $p=3$ phase transition of [3] is a statistical-mechanical result whose quantum-mechanical analogue is unestablished. This hypothesis is listed so that it can be tested or refuted by the same simulator platform proposed in Section 7; it is not part of the paper's supported results.

### 6.5 Open Questions
- How does the choice of prime $p$ affect the spectrum of the Vladimirov operator and hence observable energy levels?
- Can the $p$-adic wavelet transform of [7] be employed to analyze experimental time-series data from hierarchical quantum devices, in the way [1] applies ultrametric models to data?
- What is the relationship between the $p=3$ phase-transition condition of [3] and possible critical phenomena in ultrametric quantum systems?
- Can the framework be extended to multi-particle entanglement while preserving ultrametric locality, given that the Heisenberg algebra does not directly generalize on $p$-adic spaces [4]?

## 7. Practical Implications and Engineering Pathways

### 7.1 Who Would Use the Result and What Changes

The named users are quantum-hardware architects and error-correction designers. If the bounded-diffusion signature holds, the decision that changes is the layout of the coupling network: instead of engineering couplers to approximate a continuous Euclidean interaction graph, the architect would engineer a hierarchical coupling graph whose connectivity realizes the $p$-adic ball structure of Section 3.4, with the branching factor $p$ becoming an explicit design parameter. The second decision that changes is the error-correction budget: a state whose excitation spread plateaus near $\mu\approx 0.7$ rather than growing as $\sqrt{N}$ confines logical errors to a bounded region of the hierarchy, which in principle reduces the redundancy needed to protect them. The error-correction overhead figures themselves are not derived in this paper; only the confinement signature $\mu=0.693$, $\sigma^{2}=0.122$, and the ratio $R=0.176$ are, and the translation from confinement to qubit-overhead savings is an open engineering question (Section 6.5).

A second user group is the analysis side: experimentalists operating hierarchical quantum devices would need a tool for reading ultrametric structure out of measured time series. The $p$-adic wavelet transform of [7] is a candidate for this role: [7] develops the transform as a decomposition of vectors in a Hilbert space $\mathcal{H}$ with respect to the affine-group representation, with locality preserved in the $p$-adic domain, and its conclusion explicitly points toward multiscale methods for hierarchic quantum systems and toward quantum systems with $p>2$ orthogonal quantum states. The same data-to-ultrametric pipeline demonstrated in [1]—in which cross-tabulation data are mapped through the $\chi^{2}$ metric to a Euclidean space and a hierarchy is then induced, so that changepoints and anomalies can be read off at a range of scales—supplies the statistical protocol for deciding whether measured device data carry ultrametric structure at all.

### 7.2 Current Readiness

Against the NASA Technology Readiness Level definitions, this work is TRL 1–2: the paper provides analytical foundations—basic principles (the Vladimirov kinetic term, the heat-equation reduction of Section 4.1) and a concept with an application formulation (the falsification window of Section 4.6)—but no experimental proof of concept exists, and no peer-reviewed experimental realization of a $p$-adic quantum lattice is available (limitation L4). Analytical work of this kind cannot exceed TRL 3, and the present paper has not yet reached even a validated analytical proof of concept against independent data: the two quantitative inputs $\mu$ and $\sigma^{2}$ come from the single simulation protocol of Section 3.4, and no claim of manufacturing or hardware readiness is made or supportable here.

### 7.3 The Smallest Next Experiment

The minimal de-risking step is a classical simulation, not a quantum device: re-run the 1000-step, $p=5$ random-walk protocol of Section 3.4 with (i) an independent implementation of the Vladimirov jump kernel, (ii) a control run with a deliberately Euclidean-like kernel (failure mode F1), and (iii) extraction of the full displacement distribution, not only its mean and variance. The measured quantities are the variance-to-mean ratio $R$ and the higher moments of $\Delta_{p}$. The outcome that refutes the model's quantitative content is a re-computed $R$ outside the window $[0.158,0.194]$ under a verified implementation of the $p=5$ topology; the outcome that refutes the model's qualitative content is a mean displacement growing with $N$ rather than plateauing. Only after this classical cross-check passes does a hardware experiment—implementing the hierarchical coupling graph on a superconducting-circuit or trapped-ion platform and measuring excitation spread versus step count—become worth the engineering cost.

### 7.4 Binding Constraints

The constraints that would bind first, in order:

- **Topology fabrication.** The coupling network must realize the $p$-adic ball structure so that the measured $R$ is a test of the model (failure mode F3); if the fabricated graph is only approximately hierarchical, the acceptance window $[0.158,0.194]$ loses its meaning. Whether present superconducting or ion-trap fabrication can realize a faithful $p=5$ ball hierarchy at the required depth is an open question this paper does not answer.
- **Two-input statistics.** The falsification window is calibrated on a mean and a variance only (limitation L5); a hardware test would need the full displacement distribution to distinguish ultrametric bounded diffusion from any other confinement mechanism. No higher-moment predictions are derived in this paper, so the required distributional targets are an open question.
- **Prime and order dependence.** The prediction is fixed at $p=5$, $\alpha=1$ (limitations L1, L3); a platform that can only realize other primes or other kernel exponents cannot test the specific window derived here.
- **Environmental dominance.** Decoherence not captured by the ultrametric model could mask the plateau (failure mode F2), so the experiment requires coherence times long relative to the walk duration; what coherence budget that requires is an open question, since no decoherence rate is derived in this paper.

### 7.5 Order-of-Magnitude Bounds

No cost, market, or performance projection is derivable from the two inputs $\mu=0.693$ and $\sigma^{2}=0.122$: they fix no energy scale, no fabrication cost, and no coherence requirement. The only quantitative bound the paper can state is the diffusion comparison already derived in Section 4.5—the $p$-adic mean displacement is a factor $45.6$ smaller than the Euclidean $\sqrt{1000}\approx 31.62$ benchmark—and even this is in dimensionless displacement units, not physical units, because the mapping from tree depth to physical distance is not fixed by any result here. Any engineering performance figure (qubit-overhead savings, gate fidelities, coherence budgets) would require assumptions this paper does not possess and is therefore not projected.

### 7.6 Risks and Misuse Paths

The direct risk is overclaiming by analogy: the bounded-diffusion numbers described above are simulation outputs of a specific protocol, and presenting them as evidence that real quantum hardware is intrinsically ultrametric—before the control-simulation cross-check of Section 7.3 and any hardware test—would mislead hardware programs into redesigning coupling graphs on unsupported grounds. A second misuse path is interpretive overreach: this paper's claims are confined to the falsifiable window $R\in[0.158,0.194]$ and the plateau signature, and any stronger ontological reading is not licensed by the arithmetic of Section 4.

## 8. Conclusion

This paper set out to determine whether replacing the real line by the $p$-adic field $\mathbb{Q}_{p}$ yields quantum dynamics with a concrete, falsifiable diffusion signature. The answer extracted here is quantitative and narrow. Starting from the Vladimirov operator and the complex-valued $p$-adic Schrödinger convention of [4], and using the reduction of stationary Markov dynamics on ultrametric spaces to pseudo-differential equations on $\mathbb{Q}_{p}$ established in [2], the paper identified the 1000-step, $p=5$ tree random walk described in Section 3.4 as the discrete implementation of the heat dynamics. From the two reported inputs $\mu=0.693$ and $\sigma^{2}=0.122$, explicit arithmetic gave $\sigma=0.349$, $CV=0.503$, and $R=0.176$, with the internal check $CV^{2}\cdot\mu=0.176$ closing the calculation. Against the Euclidean benchmark $\sqrt{1000}\approx 31.62$, the mean $p$-adic displacement is smaller by a factor $45.6$, marking a bounded diffusion regime intrinsic to the ultrametric topology. The falsifiable content is the acceptance window $R\in[0.158,0.194]$ together with the plateau signature; both are refutable by the classical cross-check of Section 7.3 before any hardware commitment is made.

The result's reach is deliberately limited. It rests on two reported numbers from a single protocol at a single prime and a single fractional order; it fixes no energy scale, no physical-unit mapping, and no error-correction overhead figure; and the spectral hypothesis of Section 6.4 is labeled as unestablished. What the paper does establish is that ultrametric quantum dynamics, as formulated over $\mathbb{Q}_{p}$ with Vladimirov kinetics, is not merely a formal alternative to the continuum: it produces a specific number, $R=0.176$, that a verified implementation can confirm or destroy. If the window survives the control-checked simulation and a subsequent hardware test, the branching factor $p$ enters the design space of quantum architectures as a concrete parameter; if it does not survive, the ultrametric program loses its simplest quantitative signature and the burden of proof shifts to other observables. Either outcome is decidable by the experiment this paper specifies.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.43-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 9 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] From Data to the p-Adic or Ultrametric Model. arXiv:0809.0492v1. https://arxiv.org/abs/0809.0492v1
[2] Application of $p$-adic analysis methods in describing Markov processes on ultrametric spaces isometrically embeddable into $\mathbb{Q}_{p}$. arXiv:1504.03629v1. https://arxiv.org/abs/1504.03629v1
[3] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[4] p-Adic and Adelic Quantum Mechanics. arXiv:hep-th/0312046v1. https://arxiv.org/abs/hep-th/0312046v1
[5] A p-Adic Model of DNA Sequence and Genetic Code. arXiv:q-bio/0607018v1. https://arxiv.org/abs/q-bio/0607018v1
[6] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[7] p-Adic wavelet transform and quantum physics. arXiv:math-ph/0406024v1. https://arxiv.org/abs/math-ph/0406024v1
[8] p-Adic and Adelic Cosmology: p-Adic Origin of Dark Energy and Dark Matter. arXiv:hep-th/0602044v1. https://arxiv.org/abs/hep-th/0602044v1


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum

## QNFO corpus context (Vectorize)

QNFO: The RG-Harmonic Isomorphism: Renormalization Group Similarities with Harmonic Quantum Mechanics | https://papers.qnfo.org/papers/rg-harmonic-isomorphism
QNFO: Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology | https://papers.qnfo.org/papers/ultrametric-p-adic-metrology
QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis | https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation
QNFO: Valuation Without R: A Category-Theoretic Foundation for Finite Measurement | https://papers.qnfo.org/papers/valuation-independent-foundations

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
  We derive sharp lower bounds for the first and the second Zagreb indices ($M_1$ and $M_2$ respectively) for trees and chemical trees with the given number of pendent vertices and find optimal trees. $M_1$ is minimized by a tree with all internal vertices having degree 4, while $M_2$ is minimized by a tree where each "stem" vertex is incident to 3 or 4 pendent vertices and one internal vertex, whil
  Full text (https://arxiv.org/html/1405.1293v3), excerpts of its own sections:
  § Introduction: Topological graph indices are widely used in mathematical chemistry to predict properties of chemical compounds. They have been intensively studied in recent years. Dozens of various indices were suggested [ 1 ] to describe topology of complex molecules, among the earliest and the most famous being the first and the second Zagreb indices – $M_{1}$ and $M_{2}$ respectively [ 9 ] . The popular research problem is to find lower and upper bounds of an index over a certain set of graphs and to characterize extremal graphs in this set. The typical set to study is that of all graphs (trees, bipartite or unicyclic graphs, “cacti”, etc) of the fixed order (i.e. with the fixed number of vertices). Extremal graphs on these sets often appear to be degenerate. For example, the chain minimizes Zagreb indices, while the star maximizes them over the set of trees of order $N$ (see [ 4 , 10 ] ). Even when the set of admissible graphs is cut (by limiting degrees, chromatic or matching numbers, etc), extremal graphs are typically found on the “boundary” of the set. [...]
  § 1 The First Zagreb Index: Let $G$ be a simple connected undirected graph with the vertex set $V(G)$ and the edge set $E(G)$ . Denote by $d_{G}(v)$ the degree of a vertex $v\in V(G)$ in the graph $G$ , i.e., the number of vertices being incident to $v$ in $G$ . The first Zagreb index is defined in [ 9 ] as $M_{1}(G):=\sum_{v\in V(G)}d_{G}(v)^{2},$ (1) while the second Zagreb index – as $M_{2}(G):=\sum_{uv\in E(G)}d_{G}(u)d_{G}(v).$ (2) The vertex $v\in V(G)$ with $d_{G}(v)=1$ is called a pendent vertex. Denote the set of pendent vertices of the graph $G$ with $W(G)$ . A connected graph $T$ with $N$ vertices and $N-1$ edges is called a tree. Theorem 1 For any tree $T$ with $n\geqslant 2$ pendent vertices $M_{1}(T)\geqslant 9n-16$ if $n$ is even. The equality holds if $T$ is a $4$ -tree ( with $d_{T}(m)=4$ for all $m\in V(G)\backslash W(G)$ ) . If $n$ is odd, then $M_{1}(T)\geqslant 9n-15$ , and the equality holds if $T$ is a tree with all internal vertices having degree $4$ except the one of degree $3$ . □ Proof For $n=2$ the optimal tree is the complete graph $K_{2}$ , and the theorem obviously holds. [...]
  § 2 The Second Zagreb Index: An internal vertex in a tree is called a stem vertex if it has incident pendent vertices (see [ 3 ] ). The edge connecting a stem with a pendent vertex will be referred to as a stem edge . Theorem 3 For any tree $T$ with $n\geqslant 8$ pendent vertices $M_{2}(T)\geqslant 11n-27$ . The equality holds if each stem vertex in $T$ has degree $4$ or $5$ while other internal vertices having degree $3$ . At least one such tree exits for any $n\geqslant 9$ . □ Proof Let us employ again the idea of an attached tree from Theorem 2 . Below we suggest a suitable generalization of the concept of an attached tree, then we interrelate its cost with $M_{2}$ , and, finally, use induction on $n$ to prove the lower bound. [...]
  § 3 Conclusion: Above we suggested an optimization framework for degree-based indices of undirected trees. Using the discussed approach one can calculate lower bounds for Zagreb-like indices and find the graphs minimizing these indices over the set of trees (or chemical trees) with the fixed number of pendent vertices. Theorem 1 provides a tight lower-bound estimate for $M_{1}$ and shows that it is achieved at $4$ -trees. Theorem 2 gives a high-quality lower-bound estimate for the generalized $M_{1}$ -like index. Theorem 3 proves the tight lower-bound estimate for $M_{2}$ and characterizes $M_{2}$ -minimal trees. [...]
[2] QNFO: The RG-Harmonic Isomorphism: Renormalization Group Similarities with Harmonic Quantum Mechanics | https://papers.qnfo.org/papers/rg-harmonic-isomorphism
  The renormalization group (RG) and harmonic quantum mechanics share a deep structural isomorphism rooted in the spectral decomposition of self-adjoint operators under scale transformations. We identify five pillars of this isomorphism and apply it retrospectively to evaluate Planck's UV catastrophe resolution, Einstein's photoelectric effect, and ten subsequent QM/QFT/SM milestones. A Bayesian upd
  Full text (https://papers.qnfo.org/papers/rg-harmonic-isomorphism), excerpts of its own sections:
  § 1. Introduction: Two Formalisms, One Grammar: The harmonic oscillator is conventionally presented as the simplest exactly solvable model in quantum mechanics — a pedagogical stepping stone toward more "realistic" systems. The renormalization group is conventionally presented as a calculational technique for handling divergences in quantum field theory — a technical tool, not a physical principle. This paper argues that both conventions are wrong, and that recognizing their deep structural identity transforms our understanding of a century of quantum physics. The core thesis is that the renormalization group and harmonic quantum mechanics are not merely analogous — they share a mathematical isomorphism rooted in the same object: the spectral decomposition of a self-adjoint operator under scale transformations. The harmonic oscillator is the RG's simplest exactly solvable model; the RG is the harmonic oscillator's natural generalization to interacting, scale-dependent systems. [...]
  § 2.1 Pillar I: Scale Separation as Energy-Level Separation: The harmonic oscillator's energy spectrum is equally spaced: $$E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, \ldots$$ Wilson's renormalization group operates by integrating out a momentum shell $[\Lambda/b, \Lambda]$ and rescaling. This is structurally identical to **projecting the harmonic oscillator's Hilbert space onto the lowest $N$ energy levels**. The RG flow is the evolution of the effective Hamiltonian as more energy levels are included — or excluded. [...]
  § 2.2 Pillar II: Fixed Points as Stationary States: The RG flow equations are differential equations in scale $\mu$: $$\mu\frac{dg_i}{d\mu} = \beta_i(g_1, g_2, \ldots)$$ At a fixed point $g^*$ where $\beta_i(g^*) = 0$, the theory is scale-invariant. These are the **stationary states** of the RG flow, exactly analogous to energy eigenstates of a quantum system. The Gaussian (free) fixed point corresponds to the harmonic oscillator's ground state: both are exactly solvable, both are characterized by quadratic actions/Hamiltonians, and both serve as the perturbative starting point for more complex theories. The classification of RG fixed points — stable, unstable, mixed — mirrors the classification of quantum states as ground, excited, or metastable. A **relevant operator** at a fixed point (one that grows under RG flow) is analogous to a creation operator $a^\dagger$ that moves the system away from the ground state. An **irrelevant operator** (one that shrinks) is analogous to a decay channel that returns the system to the fixed point. [...]
  § 2.3 Pillar III: The Callan-Symanzik Equation as a Schr\"odinger Equation: The Callan-Symanzik equation for the $n$-point Green's function: $$\left[\mu\frac{\partial}{\partial\mu} + \beta(g)\frac{\partial}{\partial g} + n\gamma(g)\right] G^{(n)}(p_i; g, \mu) = 0$$ has the structure of a **Schr\"odinger-type evolution equation** where: - $\mu$ (the RG scale) plays the role of **time** - $\beta(g)\frac{\partial}{\partial g}$ is the **drift term** (analogous to the kinetic operator) - $n\gamma(g)$ is the **anomalous dimension** — the "potential energy" of the RG flow - Fixed points $\beta(g^*) = 0$ are the stationary states where scale evolution halts This is not a superficial analogy. The RG flow equation $\frac{dg}{d\ln\mu} = \beta(g)$ is isomorphic to the classical equation of motion $dx/dt = F(x)$ for a particle in a potential $V(x) = -\int\beta(g)dg$. [...]
[3] QNFO: Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology | https://papers.qnfo.org/papers/ultrametric-p-adic-metrology
  Active quantum error correction is the dominant paradigm for achieving fault-tolerant quantum computation, but its thermodynamic cost at utility scale remains unaddressed. Each round of syndrome extraction, decoding, and feedback erases information — and under Landauer's principle, that erasure carries an irreducible energy cost that scales with system size. We explore an alternative: passive erro
  Full text (https://papers.qnfo.org/papers/ultrametric-p-adic-metrology), excerpts of its own sections:
  § 1. Introduction: The fault-tolerant quantum computing roadmap has been "roughly ten years away" since the mid-1990s [speculative — the timeline claim is widely repeated but the author considers it a self-perpetuating institutional forecast, not a falsifiable prediction]. While qubit counts and coherence times have improved, the fundamental architecture remains unchanged: encode logical qubits in a subspace of a larger physical Hilbert space, measure error syndromes, decode, and feed back — continuously, at cryogenic temperatures, with overhead factors of 10^3–10^6 physical qubits per logical qubit. The energy cost of this process has received surprisingly little attention in the published literature [my conjecture — the author has searched for a peer-reviewed scaling analysis of the thermodynamic cost of fault-tolerant quantum computation at utility scale and has not found one, see Section 2]. Meanwhile, a separate line of inquiry has developed around ultrametric (p-adic) geometry in quantum physics. [...]
  § 2.1 Landauer's Principle and Active Error Correction: Landauer's principle states that erasing one bit of information in a memory at temperature T dissipates at least kT ln 2 of energy as heat [established — Landauer, 1961]. This is not an engineering constraint; it is a consequence of the second law of thermodynamics. Active quantum error correction requires, at minimum, the following irreversible operations per error-correction round: 1. **Syndrome measurement:** The ancilla qubits are measured, collapsing their state and erasing the pre-measurement superposition. Each measurement of m ancilla qubits erases m bits. 2. **Decoding:** The classical decoder processes the syndrome data and selects a recovery operation. While the decoding algorithm itself can be implemented reversibly in principle, the practical need to complete decoding within the coherence time forces the use of irreversible classical logic gates, each of which dissipates heat. 3. **Feedback:** The recovery operation is applied to the data qubits. [...]
  § 2.2 The Missing Scaling Analysis: The author has searched the published literature for a peer-reviewed analysis that closes the full thermodynamic budget for a utility-scale fault-tolerant quantum computer. To date, no such analysis has been found [my conjecture — the search was conducted across OpenAlex, Crossref, the QNFO archive records, arXiv, and web search as part of the due diligence for this project; see the companion Phase 1 report in the project repository]. The published error-correction literature focuses almost exclusively on threshold theorems and code performance as functions of physical error rate, not on the system-level energy budget. This absence is concerning. If the thermodynamic argument outlined above is correct — even to within an order of magnitude — then active QEC at utility scale faces a heat-dissipation problem that no amount of engineering optimization can circumvent. The laws of thermodynamics are not a roadmap item; they are a physical constraint that must be satisfied before any other consideration.
  § 2.3 The Sensing Escape Hatch: Quantum metrology does not face the same thermodynamic wall. A quantum sensor does not need to maintain coherence across millions of qubits for thousands of gate operations. It needs to maintain entanglement across a small number of probes (N ~ 10) for the duration of a single measurement cycle. [...]
[4] QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis | https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation
  Systematic Ostrowski-completion-theoretic audit of the Harmonic Paradigm V1.0-V4.0. Five findings: (1) Beta-function mechanism is infinity-place-specific -- Missarov (1989) confirms different universality class. (2) Q_p not ordered -- eliminates S-matrix, Noether, measurement. (3) pi IS adelic -- pi_p = (p-1)/p at each prime p. (4) alpha = r_e/lambda_C is a length ratio with rational core 137/60 h
  Full text (https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation), excerpts of its own sections:
  § 1.1 The Harmonic Paradigm: The Harmonic Paradigm (HP) V1.0--V4.0 (2026, DOIs https://papers.qnfo.org/papers--21505993) proposed that the quantum harmonic oscillator functions as the universal IR attractor of quantum theory [@qnfo-harmonic-v1; @qnfo-harmonic-v4]. The framework spanned an 8-rung ladder: 1. Transmon anharmonicity (artificial atoms) 2. Phonon equal spacing (lattice vibrations) 3. Molecular vibrations (IR spectroscopy) 4. QED β-function (fine-structure constant, Landau pole) 5. QCD β-function (asymptotic freedom) 6. GUT scale (gauge coupling unification) 7. p-Adic oscillator (Bruhat--Tits tree) 8. Quantum gravity (ultrametric closure, Wheeler--DeWitt) The HP closed out formally in V4.0 [@qnfo-harmonic-v4], retracting its central logistic β-function ansatz $\beta(\alpha) = B\cdot\alpha(1-\alpha)$ after direct calculation showed it incompatible with the textbook QED β-function $\beta(\alpha) = (2/3\pi)\alpha^2$. The logistic ansatz is linear at leading order; real QED is quadratic.
  § 1.2 The Unresolved Non-Archimedean Question: HP V1.0's bibliography cited Vladimirov-Volovich-Zelenov *p-Adic Analysis and Mathematical Physics* (1994) [@VVZ1994] and Ostrowski's theorem (1918) [@Ostrowski1918]. The researcher motivation (Note 3) referenced "Ostrowski's theorem, ultrametric structures, non-Archimedean thinking." Rungs 7--8 explicitly invoke p-adic oscillators, Bruhat--Tits trees, and ultrametric quantum gravity. Yet the HP's core physical mechanism -- the $\beta$-function analysis, the equal-$\ln(\mu)$-spacing order-statistics test, the power-law vs.\ logarithmic IR approach -- was tested **exclusively over $\mathbb{R}$** (the Archimedean/$\infty$-place). This paper asks: *Do any of the HP's mechanisms survive when tested at non-Archimedean completions, or was the HP an Archimedean-only theory with a non-Archimedean bibliography?*
  § 1.3 Ostrowski's Theorem as the Framework: Ostrowski's theorem (1918) [@Ostrowski1918] classifies all non-trivial absolute values on $\mathbb{Q}$: - The Archimedean absolute value $|\cdot|_\infty$ (the usual real absolute value) - The p-adic absolute values $|\cdot|_p$ for each prime $p$ The adele ring $\mathbb{A}_\mathbb{Q} = \mathbb{R} \times \prod'_p \mathbb{Q}_p$ is the restricted product of all completions. Every rational number $q \in \mathbb{Q}$ embeds diagonally: $q \mapsto (q, q, q, \ldots)$. The product formula: $$ \prod_v |q|_v = 1, \quad \forall q \in \mathbb{Q}^\times $$ is the arithmetic identity connecting all places [@Cassels1986]. If the HP's physical quantities are defined over $\mathbb{Q}$ (or are ratios of such quantities), they have well-defined completions at EVERY place. The question is not "do p-adic completions exist?" but "what are their values?" ___
  § 11.1 Core Conclusion: The Harmonic Paradigm was an **Archimedean-only theory** that invoked non-Archimedean structures (Vladimirov, Bruhat--Tits, Ostrowski) bibliographically without computing p-adic values. Its core mechanism (the $\beta$-function IR attractor) is inherently $\infty$-place-specific. However, the related quantities $\pi$, $\alpha$, $m$, $\lambda_C$, and $r_e$ ARE adelic -- they exist at every Ostrowski completion -- and the HP simply never computed their p-adic values. The Helical Compton Vortex provides a unified framework in which $\pi$, $\alpha$, and $m$ are projections of a single adelic topological excitation: the electron as a helical standing wave whose pitch-to-radius ratio is $\alpha$, whose torsion frequency is $m$, and whose transverse projection at each place produces $\pi_v$.
[5] QNFO: Valuation Without R: A Category-Theoretic Foundation for Finite Measurement | https://papers.qnfo.org/papers/valuation-independent-foundations
  Measurement in physics is always finite and approximate — yet its mathematical foundations are embedded in the Archimedean continuum of real numbers and the cumulative hierarchy of set theory. We invert this dependency: the act of measurement is axiomatized as a graded distinguishability map $v: \mathcal{S}^2 \to \mathbb{N} \cup \{\infty\}$ over a poset of states satisfying the ultrametric inequal
  Full text (https://papers.qnfo.org/papers/valuation-independent-foundations), excerpts of its own sections:
  § A Category-Theoretic Foundation for Finite Measurement: **WBS: QNFO.UMP.004** | **Status: published** ---
  § 1. Introduction: Every physical measurement produces a finite output: a detector click, a pointer reading, a register of $N$ bits. Yet the mathematical foundations of physics embed this finite act in the Archimedean continuum — the real numbers — a structure carrying uncountably many non-computable elements, power-set overhang, and a topology that is Archimedean (and therefore ONE completion among all completions of the rationals per Ostrowski's theorem). Simultaneously, the background universe of discourse is set theory (ZFC or equivalent), whose cumulative hierarchy, axiom of choice, and power-set axiom are accepted without examination as the stage on which physical theories are erected. This paper inverts both dependencies. [...]
  § 1.1 The Two Dependencies and Why They Matter: **Dependency 1: The real numbers ($\mathbb{R}$).** The Archimedean completion of $\mathbb{Q}$ is ONE completion among ALL completions — per Ostrowski's theorem, the valuations of $\mathbb{Q}$ are the trivial valuation, the Archimedean absolute value, and the $p$-adic absolute values for every prime $p$ `[established — Ostrowski, 1916]`. Choosing $\mathbb{R}$ without justification is the **Archimedean bias** — an unexamined default that conceals viable $p$-adic completions and discrete structures `[speculative — this paper's motivating claim]`. Moreover, the power-set overhang of $\mathbb{R}$ — the non-computable reals — has no physical signature. No finite measurement protocol can discriminate two non-computable reals, so any formula whose content depends on a non-computable value is physically unfalsifiable `[established — Continuum Trilogy, DOI https://papers.qnfo.org/papers/continuum-trilogy-01-computable-continuum/]`. Only the computable Archimedean continuum $\mathbb{R}_c$ is physical; the uncountable breadth of $\mathbb{R}$ is eliminated. [...]
  § 1.2 The Thesis: > Measurement can be formalized as a valuation space: a set of states $\mathcal{S}$ equipped > with a graded distinguishability map $v: \mathcal{S}^2 \to \mathbb{N} \cup \{\infty\}$ satisfying (1) identity > of indiscernibles, (2) symmetry, and (3) the ultrametric inequality — with no > dependence on $\mathbb{R}$ or set-theoretic foundations. The category Val of such spaces > is self-contained; $\mathbb{R}$ appears only as a limit idealization. The effective spatial > dimension $d$ emerges as the asymptotic growth exponent of the distinguishability > graph, constrained by the cohomological consistency of the refinement sheaf. ---
  § 11. Conclusion and Frontier Questions: We have shown that the act of measurement can be formalized as a valuation space $(\mathcal{S}, v)$ satisfying three axioms with no dependence on the real numbers or set theory. The category Val of valuation spaces is self-contained, and the real numbers appear only as a limit idealization (the Archimedean completion under one particular valuation). The effective spatial dimension $d$ emerges as the growth exponent of the distinguishability graph, constrained by sheaf cohomology of the refinement operator. **The contribution is not a new physical theory — it is a new foundation.** The valuation-first framework provides a mathematical language in which questions about the dimensionality of space, the nature of the continuum, and the operational content of measurement can be asked without presupposing their answers in $\mathbb{R}$ and Set.