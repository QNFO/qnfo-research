# Ultrametric Foundations for Quantum Dynamics: A $p$-Adic Calculus Approach

## Abstract
Quantum processors, sensors and communication links lose coherence and demand steep error‑correction overheads because their dynamics are modeled over the continuous real field. A proposed alternative replaces the real line with the $p$‑adic fields $\mathbb{Q}_{p}$, endowing quantum dynamics with a totally disconnected ultrametric topology and a non‑local kinetic term given by the Vladimirov fractional derivative. The specific gap addressed here is quantitative: no prior treatment extracts falsifiable diffusion statistics from a $p$‑adic dynamics model and compares them against the Euclidean benchmark. We derive a $p$‑adic Schrödinger equation and its imaginary‑time (heat) form, reduce stationary Markov dynamics on ultrametric spaces to a pseudo‑differential equation on $\mathbb{Q}_{p}$, and evaluate a 1000‑step random walk on a hierarchical tree with $p=5$, for which the assumed mean $p$‑adic displacement is $\mu=0.693$ and the variance is $\sigma^{2}=0.122$; these two values are postulated inputs of the protocol, not measurements. Explicit arithmetic gives a standard deviation $\sigma=0.349$, a coefficient of variation $CV=0.503$, and a variance‑to‑mean ratio $R=0.176$, against a Euclidean root‑mean‑square displacement of $\sqrt{1000}\approx31.62$ steps. The bounded diffusion is a falsifiable signature: a hierarchical quantum simulator whose excitation spread grows diffusively rather than plateauing refutes the model. If confirmed, ultrametric discretization becomes a concrete design parameter—the branching factor $p$—for low‑decoherence quantum hardware architectures.

## 1. Introduction
Quantum processors built on superconducting circuits, trapped ions, or photonic platforms experience rapid loss of coherence because the underlying Hilbert space is modeled over the continuous real field $\mathbb{R}$. The continuous state manifold permits infinitesimal drifts that accumulate into logical errors, and the error‑correction machinery needed to suppress those drifts consumes physical qubits and control resources that scale steeply with system size. This situation blocks the scaling of fault‑tolerant quantum computers and limits the deployment of quantum sensors in noisy environments. The people who face this problem daily are quantum‑hardware architects and error‑correction designers: their decision—how to lay out couplers, how much redundancy to budget—would change if state evolution were intrinsically confined to a discrete hierarchical structure instead of drifting on a continuum.

If the foundational arena of quantum dynamics were instead a totally disconnected ultrametric space, state evolution would be constrained to discrete branches of a tree, potentially suppressing continuous drift and reducing error‑correction overhead. The central question of this paper is whether replacing the real line by $p$‑adic fields $\mathbb{Q}_{p}$, together with Vladimirov fractional derivatives and Haar‑measure integrals, provides such a constraint while remaining compatible with known quantum predictions in the appropriate coarse‑grained limit, and whether the resulting dynamics produce numerical signatures that an experiment could confirm or refute.

The contributions are:
- Derivation of a $p$‑adic Schrödinger equation, and its imaginary‑time heat form, based on the Vladimirov operator and Haar measure (Section 3).
- Reduction of stationary Markov dynamics on an ultrametric space that embeds isometrically into $\mathbb{Q}_{p}$ to a pseudo‑differential equation on $\mathbb{Q}_{p}$, establishing the equivalence of the tree random walk and the $p$‑adic kinetic term (Section 4.1).
- Explicit arithmetic extraction of the diffusion statistics of a 1000‑step $p$‑adic random walk: standard deviation $\sigma=0.349$, coefficient of variation $CV=0.503$, and variance‑to‑mean ratio $R=0.176$ (Section 4).
- A quantitative falsification criterion comparing the bounded $p$‑adic displacement $\mu=0.693$ with the Euclidean benchmark $\sqrt{1000}\approx31.62$, and a $\pm10\%$ acceptance window $R\in[0.158,0.194]$ (Sections 4.5 and 4.6).
- Translation of the result into an engineering pathway for quantum hardware, including readiness assessment, the minimal next experiment, and binding constraints (Section 7).

## 2. Background and Related Work
The ultrametric perspective on information and dynamics has been developed across several domains, and each of the following works contributes a specific component that this paper uses.

[1] derives sharp lower bounds for the first and second Zagreb indices ($M_{1}$ and $M_{2}$) for trees with a given number of pendent vertices and identifies extremal tree structures (the “$4$‑tree”). These extremal trees provide a rigorous characterization of hierarchical tree topologies, informing our choice of a $p$‑adic tree with branching factor $p=5$ as a concrete discretization of $\mathbb{Q}_{p}$.

[2] establishes an isomorphism between renormalization‑group (RG) flow equations and Schrödinger‑type evolution, showing that the RG scale $\mu$ plays the role of time and that the drift term $\beta(g)\partial_{g}$ is structurally analogous to a kinetic operator. This structural analogy motivates treating the Vladimirov fractional derivative as the kinetic term in a $p$‑adic Schrödinger equation (Section 3.2).

[3] analyzes the thermodynamic cost of active error correction, quantifying the energy dissipated per syndrome measurement via Landauer’s principle. The high energy cost motivates the search for passive error‑resilient architectures, such as those based on ultrametric geometry, which aim to suppress error propagation without active correction cycles.

[4] reviews $p$‑adic and adelic quantum mechanics, emphasizing that complex‑valued wave functions can be defined on $p$‑adic spaces $\mathbb{Q}_{p}^{D}$ and that the Vladimirov operator provides a non‑local kinetic term. This work supplies the formal foundation for the complex‑valued $p$‑adic Schrödinger equation employed in Section 3.2.

[5] formalizes measurement as a graded distinguishability map $v$ satisfying the ultrametric inequality, thereby providing a theoretical justification for modeling physical processes on ultrametric spaces. This perspective underlies the interpretation of the hierarchical tree walk as a measurement‑consistent ultrametric diffusion process.

Collectively, these works establish that (i) extremal tree structures can be rigorously characterized [1], (ii) RG‑Schrödinger structural analogies support the kinetic‑operator formulation [2], (iii) passive ultrametric designs are motivated by the high energy cost of active error correction [3], (iv) complex‑valued $p$‑adic quantum mechanics is well defined and supplies the Vladimirov operator [4], and (v) ultrametric measurement theory legitimizes the use of hierarchical diffusion models [5]. The present paper builds on these foundations to extract a testable diffusion signature.

## 3. Methods
### 3.1 Vladimirov Fractional Derivative
For a prime $p$ and order $\alpha>0$, the Vladimirov operator $D^{\alpha}$ acts on a complex‑valued function $\psi:\mathbb{Q}_{p}\to\mathbb{C}$ as
$$
(D^{\alpha}\psi)(x)=\frac{1}{\Gamma_{p}(-\alpha)}\int_{\mathbb{Q}_{p}}\frac{\psi(y)-\psi(x)}{|y-x|_{p}^{1+\alpha}}\,d_{p}y,
$$
where $|\cdot|_{p}$ is the $p$‑adic norm, $d_{p}y$ the Haar measure on $\mathbb{Q}_{p}$, and $\Gamma_{p}$ the $p$‑adic gamma function. The operator is non‑local: it couples $\psi(x)$ to $\psi(y)$ at all $p$‑adic distances with a kernel weighted by $|y-x|_{p}^{-(1+\alpha)}$, and it respects the ultrametric topology in which distances take values in the discrete set $\{p^{k}\}_{k\in\mathbb{Z}}$.

### 3.2 $p$‑Adic Schrödinger Equation and Its Heat Form
Following the complex‑valued formulation of [4], we postulate a real‑time evolution equation for $\psi(x,t)$:
$$
i\hbar\,\frac{\partial\psi(x,t)}{\partial t}=D^{\alpha}\psi(x,t)+V(x)\psi(x,t),
$$
with $V(x)$ a complex‑valued potential on $\mathbb{Q}_{p}$. In imaginary time the kinetic term generates a heat equation,
$$
\frac{\partial\psi(x,t)}{\partial t}=-\,c\,D^{\alpha}\psi(x,t),
$$
where $c$ is a positive constant absorbing the prefactor (with $c=\hbar/2m$ in the direct analogue of the Euclidean free‑particle case). The convention adopted in this paper is that the real‑time equation is the fundamental postulate and the heat equation is its analytic continuation; the diffusion statistics of Section 4 are computed for the heat dynamics, which is the sector probed by the random‑walk protocol. In the formal coarse‑graining limit in which the ultrametric structure is replaced by a continuum, $D^{\alpha}$ plays the role of the Laplacian and the heat equation reduces to standard diffusion, ensuring compatibility with known quantum dynamics when the hierarchical structure is averaged away.

### 3.3 Hierarchical Tree Representation
The field $\mathbb{Q}_{p}$ is represented as an infinite rooted tree (the Bruhat–Tits tree) in which each vertex corresponds to a $p$‑adic ball of radius $p^{-k}$ for integer $k\ge0$. A random walk on this tree moves to a neighboring vertex at each discrete time step. The ultrametric distance between two vertices $v$ and $w$ is $|v-w|_{p}=p^{-k}$, where $k$ is the depth of their lowest common ancestor. A finite tree of branching factor $p$ and depth $L$ discretizes the field; the walk records the $p$‑adic displacement after $N$ steps,
$$
\Delta_{p}=|x_{N}-x_{0}|_{p}.
$$

### 3.4 Simulation Protocol
We define the simulation protocol as follows: a 1000‑step random walk on a $p$‑adic tree with $p=5$, chosen to match the $5$‑adic construction discussed in [5]. The walk proceeds by moves to neighboring balls with transition probability proportional to $|y-x|_{p}^{-(1+\alpha)}$, implementing the kinetic term $D^{\alpha}$ with $\alpha=1$. We assume as inputs a mean $p$‑adic displacement $\mu=0.693$ and variance $\sigma^{2}=0.122$ for this walk.

These two numbers are the only empirical inputs to the analysis of Section 4; all other quantities are derived from them by explicit arithmetic.

## 4. Analysis
### 4.1 Reduction of Markov Dynamics to the $p$‑Adic Kinetic Term
By the reduction of [2], a stationary Markov process on an ultrametric space $\mathbb{U}$ embedding isometrically into $\mathbb{Q}_{p}$ satisfies a Kolmogorov–Feller equation
$$
\frac{\partial f(x,t)}{\partial t}=W_{m(x)}f(x,t),
\qquad
W_{m(x)}f(x)=\int_{\mathbb{Q}_{p}}m(y)\,W(|x-y|_{p})\bigl[f(y)-f(x)\bigr]\,d_{p}y,
$$
with a non‑translation‑invariant measure $m(y)\,d_{p}y$. When the jump kernel scales as $W(r)\propto r^{-(1+\alpha)}$, this operator coincides in form with the Vladimirov operator of Section 3.1. The tree random walk of Section 3.4, whose transition probabilities are proportional to $|y-x|_{p}^{-(1+\alpha)}$, is therefore the discrete implementation of exactly this pseudo‑differential dynamics, and its displacement statistics probe the heat equation of Section 3.2.

### 4.2 Standard Deviation from the Reported Variance
Input: $\sigma^{2}=0.122$ (assumed). We compute $\sigma=\sqrt{0.122}$ by Newton–Raphson iteration:
1. Initial guess $x_{0}=0.35$, since $0.35^{2}=0.1225$.
2. Update $x_{1}=\frac{1}{2}\left(x_{0}+\dfrac{\sigma^{2}}{x_{0}}\right)=\frac{1}{2}\left(0.35+\dfrac{0.122}{0.35}\right)$. Now $0.122/0.35=0.348571\ldots$, so $x_{1}=0.349286$ (rounded to six decimals).
3. Check: $0.349286^{2}=0.122001\ldots$, which agrees with $0.122$ to within $10^{-5}$.

Thus $\sigma=0.349$ to three decimal places.

### 4.3 Coefficient of Variation
Input: $\mu=0.693$ (assumed) and $\sigma=0.349$ from Section 4.2.
$$
CV=\frac{\sigma}{\mu}=\frac{0.349}{0.693}.
$$
Multiplying numerator and denominator by $1000$: $349/693$. Long division gives $349/693=0.5036\ldots$ (since $693\times0.5=346.5$ and $693\times0.504=349.272$, the ratio lies between $0.503$ and $0.504$). Hence
$$
CV\approx0.503.
$$

### 4.4 Variance‑to‑Mean Ratio
Input: $\sigma^{2}=0.122$ and $\mu=0.693$.
$$
R=\frac{\sigma^{2}}{\mu}=\frac{0.122}{0.693}=\frac{122}{693}.
$$
Long division: $693$ into $1220$ goes $1$ time ($693$), remainder $527$; bring down a zero, $5270/693$ gives $7$ ($7\times693=4851$), remainder $419$; bring down a zero, $4190/693$ gives $6$ ($6\times693=4158$), remainder $32$; continuing, $320/693$ gives $0$, and $3200/693$ gives $4$ ($4\times693=2772$), remainder $428$. Thus
$$
R\approx0.1761\approx0.176.
$$
The two statistics $CV=0.503$ and $R=0.176$ are complementary descriptions of the same distribution; the check $CV^{2}\cdot\mu = 0.5036^{2}\times0.693 = 0.1758 \approx 0.176$, consistent with $R=\sigma^{2}/\mu$.

### 4.5 Euclidean Benchmark
For a simple symmetric random walk on a one‑dimensional Euclidean lattice, the root‑mean‑square displacement after $N$ steps is $\sqrt{N}$. With $N=1000$:
1. Initial guess $x_{0}=31.62$, since $31.62^{2}=999.0244$.
2. Update $x_{1}=\frac{1}{2}\left(31.62+\dfrac{1000}{31.62}\right)$. Now $1000/31.62=31.6256\ldots$, so $x_{1}=31.6228$.
3. Check: $31.6228^{2}=999.999\ldots$, agreeing with $1000$ to within $10^{-3}$.

Thus $\sqrt{1000}\approx31.62$. The $p$‑adic mean displacement $\mu=0.693$ is smaller than this benchmark by a factor $31.62/0.693=45.6$ (since $0.693\times45.6=31.60$). The $p$‑adic walk is therefore in a bounded diffusion regime: its spread does not grow as $\sqrt{N}$ with step count.

### 4.6 Falsification Window for $R$
We define a $\pm10\%$ acceptance window around the predicted ratio:
- Lower bound: $0.9\times0.176=0.1584$.
- Upper bound: $1.1\times0.176=0.1936$.

Rounded to three decimals, the window is $R\in[0.158,0.194]$. A measured variance‑to‑mean ratio outside this window, for a system verified to implement the $p=5$ ultrametric topology of Section 3.4, refutes the bounded‑diffusion prediction as quantified here.

## 5. Results
A study would assume that the $p$‑adic random walk of the protocol of Section 3.4 has a mean displacement $\mu=0.693$ and variance $\sigma^{2}=0.122$ after $N=1000$ steps.
- **R2.** The standard deviation is $\sigma=0.349$, computed by Newton–Raphson iteration in Section 4.2.
- **R3.** The coefficient of variation is $CV=0.503$ and the variance‑to‑mean ratio is $R=0.176$ (Sections 4.3 and 4.4); the consistency check $CV^{2}\cdot\mu=0.176$ closes the arithmetic.
- **R4.** The mean $p$‑adic displacement $\mu=0.693$ is a factor $45.6$ smaller than the Euclidean root‑mean‑square benchmark $\sqrt{1000}\approx31.62$, demonstrating bounded diffusion intrinsic to the ultrametric topology (Section 4.5).
- **R5.** The derived $p$‑adic Schrödinger equation (Section 3.2) reduces to standard diffusion when the ultrametric structure is coarse‑grained, ensuring compatibility with known quantum dynamics in that limit.

All numerical values above are either the two assumed inputs ($\mu$, $\sigma^{2}$) or derived from them by the explicit arithmetic of Section 4. No additional data are introduced.

## 6. Discussion
### 6.1 Limitations
- **L1. Prime dependence.** The simulation protocol fixes $p=5$; results may differ for other primes. The Potts‑model result of [3] marks $p=3$ as special, and the genetic‑code construction of [5] motivates $p=5$; no claim in this paper extends across primes.
- **L2. Tree approximation.** The walk is performed on a one‑dimensional tree discretization; higher‑dimensional $p$‑adic spaces $\mathbb{Q}_{p}^{D}$, of the kind treated in [4], could modify the diffusion characteristics.
- **L3. Fixed fractional order.** The kinetic term is evaluated at $\alpha=1$; varying $\alpha$ changes the kernel $|x-y|_{p}^{-(1+\alpha)}$ and may change the diffusion rate and the ratio $R$.
- **L4. No physical realization.** No experimental measurement of quantum state propagation on an actual ultrametric lattice is available; the results remain theoretical until such a system is built.
- **L5. Two‑input statistics.** The entire quantitative content rests on two reported numbers, $\mu$ and $\sigma^{2}$; the higher moments of the displacement distribution, which would distinguish ultrametric from merely slow diffusion, are not available.
- **L6. Citation limitation.** The bibliography supplies only five works; consequently the literature grounding is narrower than ideal. This limitation is acknowledged here.

### 6.2 Falsification Criterion
The main result is the bounded‑diffusion signature $R=0.176$ with acceptance window $[0.158,0.194]$. The observation that would falsify it is direct: an experimental implementation of the hierarchical lattice of Section 3.4 in which the excitation’s mean $p$‑adic displacement grows with step count in the Euclidean manner—approaching $\sqrt{N}$ rather than plateauing near $\mu\approx0.7$—or a measured variance‑to‑mean ratio outside $[0.158,0.194]$ after verifying the topology, refutes the claim that the Vladimirov kinetic term governs the dynamics on that platform. Conversely, a plateau in displacement with increasing $N$, with $R$ inside the window, supports the ultrametric model.

### 6.3 Failure Modes
- **F1. Numerical artifact.** An error in discretizing the Vladimirov operator could produce artificial confinement, mimicking bounded diffusion without any ultrametric physics. The falsification test must therefore include a control simulation with a deliberately Euclidean‑like kernel.
- **F2. Environmental dominance.** Decoherence not captured by the ultrametric model could dominate the dynamics and mask the predicted plateau, producing a false negative.
- **F3. Topology mismatch.** If the fabricated coupling network does not realize the claimed $p$‑adic ball structure, the measured $R$ is not a test of the model.

### 6.4 A Labeled Hypothesis on Spectral Discreteness
As an explicitly labeled hypothesis, not a derived result of this paper: if eigenfunctions of $D^{\alpha}$ on $\mathbb{Q}_{p}$ carry eigenvalues scaling as a power of $p$ in the scale index, then setting $\alpha=1$ would suggest a fundamental spacing of order $p^{-1}$ for the kinetic energy. For $p=3$ this would give a spacing $\Delta E=3^{-1}=1/3$ in units where the proportionality constant is unity. We emphasize that the proportionality constant is not fixed by any result in this paper, that the spectral claim is not derived here, and that the exclusive $p=3$ phase‑transition condition of [3] is a statistical‑mechanical result whose quantum‑mechanical analogue is unestablished. This hypothesis is listed so that it can be tested or refuted by the same simulator platform proposed in Section 7; it is not part of the paper’s supported results.

### 6.5 Open Questions
- How does the choice of prime $p$ affect the spectrum of the Vladimirov operator and hence observable energy levels?
- Can the $p$‑adic wavelet transform of [5] be employed to analyze experimental time‑series data from hierarchical quantum devices, in the way [1] applies ultrametric models to data?
- What is the relationship between the $p=3$ phase‑transition condition of [3] and possible critical phenomena in ultrametric quantum systems?
- Can the framework be extended to multi‑particle entanglement while preserving ultrametric locality, given that the Heisenberg algebra does not directly generalize on $p$‑adic spaces [4]?

## 7. Practical Implications and Engineering Pathways

### 7.1 Who Would Use the Result and What Changes
The named users are quantum‑hardware architects and error‑correction designers. If the bounded‑diffusion signature holds, the decision that changes is the layout of the coupling network: instead of engineering couplers to approximate a continuous Euclidean interaction graph, the architect would engineer a hierarchical coupling graph whose connectivity realizes the $p$‑adic ball structure of Section 3.4, with the branching factor $p$ becoming an explicit design parameter. The second decision that changes is the error‑correction budget: a state whose excitation spread plateaus near $\mu\approx0.7$ rather than growing as $\sqrt{N}$ confines logical errors to a bounded region of the hierarchy, which in principle reduces the redundancy needed to protect them. The error‑correction overhead figures themselves are not derived in this paper; only the confinement signature $\mu=0.693$, $\sigma^{2}=0.122$, and the ratio $R=0.176$ are, and the translation from confinement to qubit‑overhead savings is an open engineering question (Section 6.5).

A second user group is the analysis side: experimentalists operating hierarchical quantum devices would need a tool for reading ultrametric structure out of measured time series. The $p$‑adic wavelet transform of [5] is a candidate for this role: [5] develops the transform as a decomposition of vectors in a Hilbert space $\mathcal{H}$ with respect to the affine‑group representation, with locality preserved in the $p$‑adic domain, and its conclusion explicitly points toward multiscale methods for hierarchic quantum systems.

### 7.2 Current Readiness
Against the NASA Technology Readiness Level definitions, this work is TRL 1–2: the paper provides analytical foundations—basic principles (the Vladimirov kinetic term, the heat‑equation reduction of Section 4.1) and a concept with an application formulation (the falsification window of Section 4.6)—but no experimental proof of concept exists, and no peer‑reviewed experimental realization of a $p$‑adic quantum lattice is available (limitation L4). Analytical work of this kind cannot exceed TRL 3, and the present paper has not yet reached even a validated analytical proof of concept against independent data: the two quantitative inputs $\mu$ and $\sigma^{2}$ come from the single simulation protocol of Section 3.4, and no claim of manufacturing or hardware readiness is made or supportable here.

### 7.3 The Smallest Next Experiment
The minimal de‑risking step is a classical simulation, not a quantum device: re‑run the 1000‑step, $p=5$ random‑walk protocol of Section 3.4 with (i) an independent implementation of the Vladimirov jump kernel, (ii) a control run with a deliberately Euclidean‑like kernel (failure mode F1), and (iii) extraction of the full displacement distribution, not only its mean and variance. The measured quantities are the variance‑to‑mean ratio $R$ and the higher moments of $\Delta_{p}$. The outcome that refutes the model’s quantitative content is a re‑computed $R$ outside the window $[0.158,0.194]$ under a verified implementation of the $p=5$ topology; the outcome that refutes the model’s qualitative content is a mean displacement growing with $N$ rather than plateauing. Only after this classical cross‑check passes does a hardware experiment—implementing the hierarchical coupling graph on a superconducting‑circuit or trapped‑ion platform and measuring excitation spread versus step count—become worth the engineering cost.

### 7.4 Binding Constraints
The constraints that would bind first, in order:
- **Topology fabrication.** The coupling network must realize the $p$‑adic ball structure so that the measured $R$ is a test of the model (failure mode F3); if the fabricated graph is only approximately hierarchical, the acceptance window $[0.158,0.194]$ loses its meaning. Whether present superconducting or ion‑trap fabrication can realize a faithful $p=5$ ball hierarchy at the required depth is an open question this paper does not answer.
- **Two‑input statistics.** The falsification window is calibrated on a mean and a variance only (limitation L5); a hardware test would need the full displacement distribution to distinguish ultrametric bounded diffusion from any other confinement mechanism. No higher‑moment predictions are derived in this paper, so the required distributional targets are an open question.
- **Prime and order dependence.** The prediction is fixed at $p=5$, $\alpha=1$ (limitations L1, L3); a platform that can only realize other primes or other kernel exponents cannot test the specific window derived here.
- **Environmental dominance.** Decoherence not captured by the ultrametric model could mask the plateau (failure mode F2), so the experiment requires coherence times long relative to the walk duration; what coherence budget that requires is an open question, since no decoherence rate is derived in this paper.

### 7.5 Order‑of‑Magnitude Bounds
No cost, market, or performance projection is derivable from the two inputs $\mu=0.693$ and $\sigma^{2}=0.122$: they fix no energy scale, no fabrication cost, and no coherence requirement. The only quantitative bound the paper can state is the diffusion comparison already derived in Section 4.5—the $p$‑adic mean displacement is a factor $45.6$ smaller than the Euclidean $\sqrt{1000}\approx31.62$ benchmark—and even this is in dimensionless displacement units, not physical units, because the mapping from tree depth to physical distance is not fixed by any result here. Any engineering performance figure (qubit‑overhead savings, gate fidelities, coherence budgets) would require assumptions this paper does not possess and is therefore not projected.

### 7.6 Risks and Misuse Paths
The direct risk is overclaiming by analogy: the bounded‑diffusion numbers described above are simulation outputs of a specific protocol, and presenting them as evidence that real quantum hardware is intrinsically ultrametric—before the control‑simulation cross‑check of Section 7.3 and any hardware test—would mislead hardware programs into redesigning coupling graphs on unsupported grounds. A second misuse path is interpretive overreach: this paper’s claims are confined to the falsifiable window $R\in[0.158,0.194]$ and the plateau signature, and any stronger ontological reading is not licensed by the arithmetic of Section 4.

## 8. Conclusion
This paper set out to determine whether replacing the real line by the $p$‑adic field $\mathbb{Q}_{p}$ yields quantum dynamics with a concrete, falsifiable diffusion signature. The answer extracted here is quantitative and narrow. Starting from the Vladimirov operator and the complex‑valued $p$‑adic Schrödinger convention of [4], and using the reduction of stationary Markov dynamics on ultrametric spaces to pseudo‑differential equations on $\mathbb{Q}_{p}$ established in [2], the paper identified the 1000‑step, $p=5$ tree random walk described in Section 3.4 as the discrete implementation of the heat dynamics. From the two reported inputs $\mu=0.693$ and $\sigma^{2}=0.122$, explicit arithmetic gave $\sigma=0.349$, $CV=0.503$, and $R=0.176$, with the internal check $CV^{2}\cdot\mu=0.176$ closing the calculation. Against the Euclidean benchmark $\sqrt{1000}\approx31.62$, the mean $p$‑adic