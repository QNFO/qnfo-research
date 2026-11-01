# Ultrametric Foundations for Quantum Dynamics: A $p$-Adic Calculus Approach

## Abstract

Fault-tolerant quantum processors demand error-correction overheads estimated at $10^{3}$–$10^{6}$ physical qubits per logical qubit, and each correction round dissipates energy through irreversible syndrome erasure. A proposed alternative models quantum dynamics over the $p$-adic fields $\mathbb{Q}_{p}$, which carry a totally disconnected ultrametric topology and a non-local kinetic term given by the Vladimirov fractional derivative. The specific gap addressed here is quantitative and falsifiability-oriented: no prior treatment extracts diffusion statistics from a $p$-adic dynamics model, compares them against the Euclidean benchmark, and states which observation refutes which claim. We derive a $p$-adic Schrödinger equation and its imaginary-time heat form, state the reduction of tree Markov dynamics to a pseudo-differential equation on $\mathbb{Q}_{p}$ as an explicit modeling assumption, and evaluate a 1000-step random walk on a hierarchical tree with $p=5$ under the assumed inputs $\mu=0.693$ (mean displacement) and $\sigma^{2}=0.122$ (variance). Explicit arithmetic gives $\sigma=0.349$, $CV=0.503$, and a variance-to-mean ratio $R=0.176$ with acceptance window $R\in[0.158,0.194]$, against a Euclidean root-mean-square benchmark $\sqrt{1000}\approx31.62$, a factor of $45.6$ larger. Two corrections organize the falsifiable content: the window tests the assumed parameter values, while the bounded-diffusion claim is a hypothesis tested by displacement growth versus plateau across step counts, with a projected unbounded-diffusion displacement of $21.9$ at $N=10^{6}$ steps against a plateau near $0.693$. If confirmed, the branching factor $p$ becomes a concrete design parameter for low-overhead quantum architectures.

## 1. Introduction

The dominant architecture for fault-tolerant quantum computation encodes logical qubits in a subspace of a larger physical Hilbert space and then measures error syndromes, decodes, and applies feedback continuously, with overhead factors of $10^{3}$–$10^{6}$ physical qubits per logical qubit [3]. Each round of this active error-correction cycle performs irreversible operations: syndrome measurement erases the pre-measurement ancilla state, decoding within the coherence time forces irreversible classical logic, and feedback applies the recovery, and by Landauer's principle the erasure of one bit at temperature $T$ dissipates at least $kT\ln 2$ as heat [3]. This situation blocks the scaling of fault-tolerant quantum computers and limits the deployment of quantum sensors in noisy environments. The people who face this problem daily are quantum-hardware architects and error-correction designers: their decisions about coupler layout and redundancy budget would change if state evolution were intrinsically confined to a discrete hierarchical structure instead of drifting on a continuum, because confinement bounds the region of the hierarchy that a logical error can reach.

If the arena of quantum dynamics were a totally disconnected ultrametric space, state evolution would be constrained to discrete branches of a tree, potentially suppressing continuous drift and reducing the active-correction burden. A foundational argument points in the same direction: every physical measurement produces a finite output, and the act of measurement can be axiomatized as a graded distinguishability map satisfying the ultrametric inequality, with the real numbers appearing only as a limit idealization [5]. The central question of this paper is whether replacing the real line by $p$-adic fields $\mathbb{Q}_{p}$, together with Vladimirov fractional derivatives and Haar-measure integrals, yields dynamics with numerical signatures that an experiment could confirm or refute, and precisely which observation refutes which claim.

Two distinctions organize the falsifiable content and are stated up front. First, a computation at a single step count $N=1000$ cannot establish that the spread of the walk fails to grow as $\sqrt{N}$; that is a scaling claim requiring displacement measured at multiple $N$, and it is therefore restated as a hypothesis with its own test. Second, a measured variance-to-mean ratio outside the acceptance window refutes the assumed parameter values, not the claim that the Vladimirov kinetic term governs the dynamics; the two falsifiers are separated in Sections 4.6 and 6.2.

The contributions are:
- Derivation of a $p$-adic Schrödinger equation, and its imaginary-time heat form, based on the Vladimirov operator and Haar measure (Section 3).
- Statement of the reduction of stationary Markov dynamics on an ultrametric tree to a pseudo-differential equation on $\mathbb{Q}_{p}$ as an explicit modeling assumption, identifying the tree random walk with the $p$-adic kinetic term (Section 4.1).
- Explicit arithmetic extraction of the diffusion statistics of a 1000-step $p$-adic random walk: standard deviation $\sigma=0.349$, coefficient of variation $CV=0.503$, and variance-to-mean ratio $R=0.176$ (Section 4).
- A corrected falsification structure: a $\pm10\%$ acceptance window $R\in[0.158,0.194]$ that tests the assumed parameters, and a separate scaling test for the bounded-diffusion hypothesis, with the projection that unbounded diffusion would drive the mean displacement to $21.9$ at $N=10^{6}$ steps while a plateau holds it near $0.693$ (Sections 4.5, 4.6 and 6.2).
- A combinatorial cross-check of the hierarchical tree against sharp degree-index bounds for trees (Section 4.7).
- Translation of the result into an engineering pathway for quantum hardware, including readiness assessment, the minimal next experiment, and binding constraints (Section 7).

## 2. Background and Related Work

The ultrametric perspective on measurement, dynamics, and quantum theory has been developed along several independent lines, and each of the following works contributes a specific component that this paper uses.

[1] derives sharp lower bounds for the first and second Zagreb indices of trees with a given number of pendent vertices: Theorem 1 gives $M_{1}(T)\ge 9n-16$ for a tree with $n$ even pendent vertices, with equality exactly for $4$-trees in which every internal vertex has degree $4$ (and $M_{1}(T)\ge 9n-15$ for odd $n$), and Theorem 3 gives $M_{2}(T)\ge 11n-27$ for $n\ge 8$, with equality when each stem vertex has degree $4$ or $5$. This matters here because the hierarchical coupling graph that a hardware implementation would fabricate is a tree with a definite degree profile, and degree-based indices are the standard combinatorial descriptors of such graphs; Section 4.7 uses these theorems as an independent consistency check on the $p=5$ ball tree.

[2] identifies a structural isomorphism between the renormalization group and harmonic quantum mechanics, rooted in the spectral decomposition of self-adjoint operators under scale transformations. Its first pillar sets the equally spaced oscillator spectrum $E_{n}=\hbar\omega\left(n+\tfrac{1}{2}\right)$ against Wilson's integration of a momentum shell $[\Lambda/b,\Lambda]$, treating shell elimination as projection onto progressively fewer energy levels; its second pillar reads RG fixed points as stationary states, with relevant operators analogous to creation operators that move the system away from the fixed point; and its third pillar reads the Callan–Symanzik equation as a Schrödinger-type evolution equation in which the scale $\mu$ plays the role of time. This is the precedent for treating hierarchically arranged scales as physically meaningful labels: the $p$-adic tree of Section 3.3 organizes space into discrete scales $p^{k}$ in the same log-structured way that RG shells organize momentum, and [2] establishes that quantum formalism natively supports such scale decompositions. The isomorphism is used here as motivation only, not as a derivation.

[3] examines the thermodynamic cost of active quantum error correction and proposes passive error resilience through ultrametric geometry as an alternative, with quantum metrology as the nearer-term application because a sensor needs to maintain entanglement across only a small number of probes ($N\sim 10$) for a single measurement cycle rather than coherence across millions of qubits. Its accounting of the three irreversible operations per correction round and the $10^{3}$–$10^{6}$ overhead factor supplies the quantitative motivation for the problem stated in Section 1, and its proposal that ultrametric geometry could provide passive resilience is the architectural hypothesis that the diffusion signature of this paper would test.

[4] audits a harmonic-oscillator-centered framework against Ostrowski's theorem, which classifies the non-trivial absolute values of $\mathbb{Q}$ into the Archimedean one and the $p$-adic ones, and finds that the audited framework's core mechanism was tested exclusively over $\mathbb{R}$: the $\beta$-function mechanism is infinity-place-specific, with a different universality class confirmed at the $p$-adic place, and $\mathbb{Q}_{p}$ carries no order, which eliminates the standard structures of $S$-matrix theory, Noether analysis, and measurement as usually formulated. The audit also records that $\pi$ is adelic, with $\pi_{p}=(p-1)/p$ at each prime. This is the cautionary component for the present paper: intuitions formed on the continuum, including the interpretation of displacement statistics, do not transfer automatically to $\mathbb{Q}_{p}$, and Section 6 treats the ordering loss as a structural limitation of any $p$-adic dynamics.

[5] axiomatizes measurement itself without the real numbers: a valuation space $(\mathcal{S},v)$ equips a poset of states with a graded distinguishability map $v:\mathcal{S}^{2}\to\mathbb{N}\cup\{\infty\}$ satisfying identity of indiscernibles, symmetry, and the ultrametric inequality, and the effective spatial dimension $d$ emerges as the asymptotic growth exponent of the distinguishability graph. Because no finite measurement protocol can discriminate non-computable reals, the Archimedean continuum's uncountable breadth has no physical signature, and $\mathbb{R}$ enters only as a limit idealization. This supplies the foundational license for the whole program: if the operational content of measurement is ultrametric at the axioms, then formulating dynamics over $\mathbb{Q}_{p}$ is not an arbitrary formal substitution but a return to the structure that finite distinguishability already carries.

Collectively, these works establish that degree-constrained trees admit sharp extremal characterization [1], that scale-hierarchical decompositions are native to quantum formalism [2], that the overhead of active error correction motivates passive ultrametric alternatives [3], that Archimedean mechanisms can fail to survive at non-Archimedean places [4], and that finite measurement is axiomatizable over ultrametric valuations without $\mathbb{R}$ [5]. The present paper builds on these foundations to extract a testable diffusion signature.

## 3. Methods

### 3.1 Vladimirov Fractional Derivative

For a prime $p$ and order $\alpha>0$, the Vladimirov operator $D^{\alpha}$ acts on a complex-valued function $\psi:\mathbb{Q}_{p}\to\mathbb{C}$ as

$$
(D^{\alpha}\psi)(x)=\frac{1}{\Gamma_{p}(-\alpha)}\int_{\mathbb{Q}_{p}}\frac{\psi(y)-\psi(x)}{|y-x|_{p}^{1+\alpha}}\,d_{p}y,
$$

where $|\cdot|_{p}$ is the $p$-adic norm, $d_{p}y$ the Haar measure on $\mathbb{Q}_{p}$, and $\Gamma_{p}$ the $p$-adic gamma function. The operator is non-local: it couples $\psi(x)$ to $\psi(y)$ at all $p$-adic distances with a kernel weighted by $|y-x|_{p}^{-(1+\alpha)}$, and it respects the ultrametric topology in which distances take values in the discrete set $\{p^{k}\}_{k\in\mathbb{Z}}$. The caution of [4] applies here: structures defined over $\mathbb{R}$, including ordered spectra and standard measurement formalisms, do not transfer automatically to $\mathbb{Q}_{p}$, so every interpretive claim below is confined to what the ultrametric structure itself supports.

### 3.2 $p$-Adic Schrödinger Equation and Its Heat Form

Following the complex-valued $p$-adic formulation reviewed in [4], we postulate a real-time evolution equation for $\psi(x,t)$:

$$
i\hbar\,\frac{\partial\psi(x,t)}{\partial t}=D^{\alpha}\psi(x,t)+V(x)\psi(x,t),
$$

with $V(x)$ a complex-valued potential on $\mathbb{Q}_{p}$. In imaginary time the kinetic term generates a heat equation,

$$
\frac{\partial\psi(x,t)}{\partial t}=-\,c\,D^{\alpha}\psi(x,t),
$$

where $c$ is a positive constant absorbing the prefactor. The convention adopted in this paper is that the real-time equation is the fundamental postulate and the heat equation is its analytic continuation; the diffusion statistics of Section 4 are computed for the heat dynamics, which is the sector probed by the random-walk protocol. In the formal coarse-graining limit in which the ultrametric structure is replaced by a continuum, $D^{\alpha}$ plays the role of the Laplacian and the heat equation reduces to standard diffusion, ensuring compatibility with known quantum dynamics when the hierarchical structure is averaged away. The RG–Schrödinger isomorphism of [2] motivates, but does not derive, this kinetic-operator reading: [2] shows that scale-hierarchical decompositions are native to quantum formalism through its three pillars, and the $p$-adic tree organizes space into discrete scales $p^{k}$ in the same log-structured way.

### 3.3 Hierarchical Tree Representation

The field $\mathbb{Q}_{p}$ is represented as an infinite rooted tree (the Bruhat–Tits tree) in which each vertex corresponds to a $p$-adic ball of radius $p^{-k}$ for integer $k\ge0$. A random walk on this tree moves to a neighboring vertex at each discrete time step. The ultrametric distance between two vertices $v$ and $w$ is $|v-w|_{p}=p^{-k}$, where $k$ is the depth of their lowest common ancestor. A finite tree of branching factor $p$ and depth $L$ discretizes the field; the walk records the $p$-adic displacement after $N$ steps,

$$
\Delta_{p}=|x_{N}-x_{0}|_{p}.
$$

### 3.4 Simulation Protocol

We define the simulation protocol as follows: a 1000-step random walk on a $p$-adic tree with $p=5$, chosen to match the $5$-adic construction discussed in [5]. The walk proceeds by moves to neighboring balls with transition probability proportional to $|y-x|_{p}^{-(1+\alpha)}$, implementing the kinetic term $D^{\alpha}$ with $\alpha=1$. We assume as inputs a mean $p$-adic displacement $\mu=0.693$ and variance $\sigma^{2}=0.122$ for this walk.

These two numbers are the only quantitative inputs to the analysis of Section 4; all other quantities are derived from them by explicit arithmetic. They are postulated protocol parameters, not measurements, and every result below inherits that status.

## 4. Analysis

### 4.1 Reduction of Tree Markov Dynamics to the $p$-Adic Kinetic Term

We state the following as an explicit modeling assumption, not a derived theorem. A stationary Markov process on an ultrametric space $\mathbb{U}$ embedding isometrically into $\mathbb{Q}_{p}$ satisfies a Kolmogorov–Feller equation

$$
\frac{\partial f(x,t)}{\partial t}=W_{m(x)}f(x,t),
\qquad
W_{m(x)}f(x)=\int_{\mathbb{Q}_{p}}m(y)\,W(|x-y|_{p})\bigl[f(y)-f(x)\bigr]\,d_{p}y,
$$

with a possibly non-translation-invariant measure $m(y)\,d_{p}y$. We assume that when the jump kernel scales as $W(r)\propto r^{-(1+\alpha)}$, this operator coincides in form with the Vladimirov operator of Section 3.1. Under this assumption, the tree random walk of Section 3.4, whose transition probabilities are proportional to $|y-x|_{p}^{-(1+\alpha)}$, is the discrete implementation of exactly this pseudo-differential dynamics, and its displacement statistics probe the heat equation of Section 3.2. The precedent for treating such scale-hierarchical structures as quantum-mechanically meaningful is the isomorphism of [2]; the assumption itself is not derived from [2] or from any other cited work.

### 4.2 Standard Deviation from the Assumed Variance

Input: $\sigma^{2}=0.122$ (assumed, Section 3.4). We compute $\sigma=\sqrt{0.122}$ by Newton–Raphson iteration:

1. Initial guess $x_{0}=0.35$, since $0.35^{2}=0.1225$.
2. Update $x_{1}=\frac{1}{2}\left(x_{0}+\dfrac{\sigma^{2}}{x_{0}}\right)=\frac{1}{2}\left(0.35+\dfrac{0.122}{0.35}\right)$. Now $0.122/0.35=0.348571\ldots$, so $x_{1}=0.349286$ (rounded to six decimals).
3. Check: $0.349286^{2}=0.122001\ldots$, which agrees with $0.122$ to within $10^{-5}$.

Thus $\sigma=0.349$ to three decimal places.

### 4.3 Coefficient of Variation

Input: $\mu=0.693$ (assumed, Section 3.4) and $\sigma=0.349$ from Section 4.2.

$$
CV=\frac{\sigma}{\mu}=\frac{0.349}{0.693}.
$$

Multiplying numerator and denominator by $1000$: $349/693$. Long division gives $349/693=0.5036\ldots$ (since $693\times0.5=346.5$ and $693\times0.504=349.272$, the ratio lies between $0.503$ and $0.504$). Hence

$$
CV\approx0.503.
$$

### 4.4 Variance-to-Mean Ratio

Input: $\sigma^{2}=0.122$ and $\mu=0.693$.

$$
R=\frac{\sigma^{2}}{\mu}=\frac{0.122}{0.693}=\frac{122}{693}.
$$

Long division: $693$ into $1220$ goes $1$ time ($693$), remainder $527$; bring down a zero, $5270/693$ gives $7$ ($7\times693=4851$), remainder $419$; bring down a zero, $4190/693$ gives $6$ ($6\times693=4158$), remainder $32$; continuing, $320/693$ gives $0$, and $3200/693$ gives $4$ ($4\times693=2772$), remainder $428$. Thus

$$
R\approx0.1761\approx0.176.
$$

The two statistics $CV=0.503$ and $R=0.176$ are complementary descriptions of the same distribution; the check $CV^{2}\cdot\mu=0.5036^{2}\times0.693=0.1758\approx0.176$ is consistent with $R=\sigma^{2}/\mu$.

### 4.5 Euclidean Benchmark and the Factor $45.6$

For a simple symmetric random walk on a one-dimensional Euclidean lattice, the root-mean-square displacement after $N$ steps is $\sqrt{N}$. With $N=1000$:

1. Initial guess $x_{0}=31.62$, since $31.62^{2}=999.0244$.
2. Update $x_{1}=\frac{1}{2}\left(31.62+\dfrac{1000}{31.62}\right)$. Now $1000/31.62=31.6256\ldots$, so $x_{1}=31.6228$.
3. Check: $31.6228^{2}=999.999\ldots$, agreeing with $1000$ to within $10^{-3}$.

Thus $\sqrt{1000}\approx31.62$. The $p$-adic mean displacement $\mu=0.693$ is smaller than this benchmark by a factor $31.62/0.693=45.6$ (since $0.693\times45.6=31.60$). At the single step count $N=1000$ this comparison shows only that the assumed displacement is far below the Euclidean value; whether the gap persists as $N$ grows is the scaling hypothesis of Section 4.6, not a result established here.

### 4.6 Falsification Structure

Two distinct claims require two distinct falsifiers, and we state the convention adopted in this paper explicitly: the acceptance window tests the assumed parameter values, while the bounded-diffusion claim is tested by scaling, following the corrected formulation.

**(a) Acceptance window for $R$ (parameter test).** We define a $\pm10\%$ acceptance window around the predicted ratio:

- Lower bound: $0.9\times0.176=0.1584$.
- Upper bound: $1.1\times0.176=0.1936$.

Rounded to three decimals, the window is $R\in[0.158,0.194]$. A measured variance-to-mean ratio outside this window, for a system verified to implement the $p=5$ ultrametric topology of Section 3.4, refutes the assumed parameter values $\mu=0.693$ and $\sigma^{2}=0.122$ as quantified here. It does not by itself refute the claim that the Vladimirov kinetic term governs the dynamics, because the window is calibrated on the assumed inputs.

**(b) Scaling test for the bounded-diffusion hypothesis.** The hypothesis is that the mean displacement plateaus near $\mu\approx0.693$ as $N$ grows, rather than growing as $\sqrt{N}$. Its test requires displacement measured at multiple step counts. As a labeled projection with stated assumptions: if the displacement instead grew diffusively, anchored to the assumed value $0.693$ at $N_{0}=1000$ and scaling as $\sqrt{N/N_{0}}$, then at $N=10^{6}$ steps the displacement would be

$$
0.693\times\sqrt{\frac{10^{6}}{1000}}=0.693\times\sqrt{1000}=0.693\times31.62=21.9.
$$

The arithmetic: $10^{6}/1000=1000$, $\sqrt{1000}=31.62$ (Section 4.5), and $0.693\times31.62=21.9$ (three significant figures). A plateau holds the displacement near $0.693$; a measured displacement near $21.9$ at $N=10^{6}$, under a verified $p=5$ topology, refutes the bounded-diffusion hypothesis. The uncertainty of this projection is inherited directly from the assumed inputs: a $\pm10\%$ uncertainty in $\mu$ propagates linearly to a $\pm10\%$ uncertainty in the projected displacement, i.e. $21.9\pm2.2$.

### 4.7 Combinatorial Cross-Check Against Sharp Tree Bounds

The hierarchical coupling graph of Section 3.3 is a tree, so the sharp bounds of [1] apply as an independent consistency check. Consider the depth-$L=2$ finite truncation of the $p=5$ ball tree: a root of degree $5$, five internal vertices each of degree $6$ (one parent edge plus five child edges), and $n=25$ pendent vertices. The first Zagreb index is $M_{1}=\sum_{v}(\deg v)^{2}$:

$$
M_{1}=5^{2}+5\times6^{2}+25\times1^{2}=25+180+25=230.
$$

The second Zagreb index is $M_{2}=\sum_{uv\in E}\deg(u)\deg(v)$:

$$
M_{2}=5\times(5\times6)+25\times(6\times1)=150+150=300.
$$

Since $n=25$ is odd, Theorem 1 of [1] gives $M_{1}\ge 9n-15=9\times25-15=210$, and Theorem 3 of [1] gives $M_{2}\ge 11n-27=11\times25-27=248$ (with $n\ge8$ satisfied). Both bounds hold: $230\ge210$ and $300\ge248$. The excess over the bounds reflects the degree-$6$ internal vertices of the $p=5$ ball tree, which lie outside the extremal $4$-tree family of [1]; the check confirms that the fabricated graph is a well-defined member of the tree class that [1] characterizes, and it would flag any coupling-network design whose degree profile fell below these bounds.

## 5. Results

All numerical values below are either the two assumed inputs ($\mu=0.693$, $\sigma^{2}=0.122$) or derived from them by the explicit arithmetic of Section 4. No additional data are introduced. The derived results are:

- **Diffusion statistics (Section 4.2–4.4).** From the assumed variance $\sigma^{2}=0.122$, Newton–Raphson iteration gives $\sigma=0.349$; from the assumed mean $\mu=0.693$, the coefficient of variation is $CV=\sigma/\mu=0.349/0.693\approx0.503$, and the variance-to-mean ratio is $R=\sigma^{2}/\mu=0.122/0.693\approx0.176$. The internal check $CV^{2}\cdot\mu=0.5036^{2}\times0.693=0.1758\approx0.176$ closes the calculation.
- **Euclidean benchmark (Section 4.5).** At $N=1000$ steps, the Euclidean root-mean-square displacement is $\sqrt{1000}\approx31.62$, so the assumed $p$-adic mean displacement $\mu=0.693$ is smaller by a factor $31.62/0.693\approx45.6$.
- **Falsification structure (Section 4.6).** The $\pm10\%$ acceptance window around $R=0.176$ is $R\in[0.158,0.194]$, which tests the assumed parameter values; the bounded-diffusion hypothesis is tested separately by displacement growth versus plateau across step counts, with the labeled projection that unbounded diffusive growth anchored at $0.693$ at $N_{0}=1000$ would reach $0.693\times\sqrt{1000}=21.9\pm2.2$ at $N=10^{6}$ steps, against a plateau near $0.693$.
- **Combinatorial cross-check (Section 4.7).** For the depth-$L=2$, $p=5$ ball tree with $n=25$ pendent vertices, the first Zagreb index is $M_{1}=230$ and the second is $M_{2}=300$; both satisfy the sharp bounds of [1], $M_{1}\ge210$ and $M_{2}\ge248$.

Each value above is a consequence of the two assumed inputs and the arithmetic of Section 4; none is a measurement.

## 6. Discussion

### 6.1 Limitations

- **L1. Assumed inputs.** The entire quantitative content rests on two postulated numbers, $\mu=0.693$ and $\sigma^{2}=0.122$, from a single protocol at a single step count. Every derived statistic ($\sigma$, $CV$, $R$, the window, the factor $45.6$, the projection $21.9$) inherits their status as assumptions; a change in either input rescales the results directly, since $R=\sigma^{2}/\mu$ is linear in the numerator and inversely linear in the denominator.
- **L2. Single step count.** The statistics are computed at $N=1000$ only. The bounded-diffusion claim is therefore a hypothesis (Section 4.6(b)), not a result; only a multi-$N$ displacement measurement can establish or destroy it.
- **L3. Prime dependence.** The protocol fixes $p=5$; results may differ for other primes. No claim in this paper extends across primes, and the choice of $p=5$ is a protocol decision, not a derived optimum.
- **L4. Tree approximation.** The walk is performed on a one-dimensional tree discretization; higher-dimensional $p$-adic spaces $\mathbb{Q}_{p}^{D}$, of the kind treated in [4], could modify the diffusion characteristics.
- **L5. Fixed fractional order.** The kinetic term is evaluated at $\alpha=1$; varying $\alpha$ changes the kernel $|x-y|_{p}^{-(1+\alpha)}$ and may change the diffusion rate and the ratio $R$.
- **L6. No physical realization.** No experimental measurement of quantum state propagation on an actual ultrametric lattice is available; the results remain theoretical until such a system is built.
- **L7. Two-input statistics.** The higher moments of the displacement distribution, which would distinguish ultrametric bounded diffusion from any other confinement mechanism, are not fixed by the two assumed inputs and are not derived here.
- **L8. Ordering loss.** As the audit of [4] records, $\mathbb{Q}_{p}$ carries no order, which eliminates the standard structures of $S$-matrix theory, Noether analysis, and measurement as usually formulated; any interpretive claim built on ordered spectra or continuum measurement formalism does not transfer to the $p$-adic setting, and this paper confines itself to what the ultrametric structure supports.

### 6.2 Falsification Structure

The falsifiable content separates into two claims with two distinct falsifiers, and the convention of Section 4.6 is restated here: the acceptance window tests the assumed parameter values, while the bounded-diffusion claim is tested by scaling.

**(a) Parameter test.** A measured variance-to-mean ratio outside $R\in[0.158,0.194]$, for a system verified to implement the $p=5$ ultrametric topology of Section 3.4, refutes the assumed parameter values $\mu=0.693$ and $\sigma^{2}=0.122$ as quantified here. It does not by itself refute the claim that the Vladimirov kinetic term governs the dynamics, because the window is calibrated on the assumed inputs; a measured $R$ outside the window is consistent with correct Vladimirov dynamics and different protocol parameters.

**(b) Scaling test for the bounded-diffusion hypothesis.** The hypothesis is that the mean displacement plateaus near $\mu\approx0.693$ as $N$ grows. The observation that would falsify it is direct: a displacement measured at multiple step counts that grows in the Euclidean manner, approaching the projected value of $21.9\pm2.2$ at $N=10^{6}$ steps (Section 4.6(b)) rather than plateauing near $0.693$, refutes the bounded-diffusion hypothesis under a verified $p=5$ topology. Conversely, a plateau in displacement with increasing $N$, with $R$ inside the window, supports the model's quantitative content. An observation that would falsify the paper's central modeling assumption itself—a displacement statistics pattern incompatible with any stationary jump process on the tree, such as systematic drift of the mean across repeated runs at fixed $N$—would undermine the reduction of Section 4.1 rather than either falsifier above.

### 6.3 Failure Modes

- **F1. Numerical artifact.** An error in discretizing the Vladimirov operator could produce artificial confinement, mimicking a plateau without any ultrametric physics. The falsification test must therefore include a control with a deliberately Euclidean-like kernel.
- **F2. Environmental dominance.** Decoherence not captured by the ultrametric model could dominate the dynamics and mask the predicted plateau, producing a false negative for the scaling test.
- **F3. Topology mismatch.** If the fabricated coupling network does not realize the claimed $p$-adic ball structure, the measured $R$ is not a test of the model, and both falsifiers lose their force.
- **F4. Parameter drift.** Because the window is calibrated on assumed inputs, a protocol whose true parameters differ from $\mu=0.693$, $\sigma^{2}=0.122$ would fail the window test while the underlying dynamics remain correct; the two falsifiers must always be reported together.

### 6.4 A Labeled Hypothesis on Spectral Discreteness

As an explicitly labeled hypothesis, not a derived result of this paper: if eigenfunctions of $D^{\alpha}$ on $\mathbb{Q}_{p}$ carry eigenvalues scaling as a power of $p$ in the scale index, then setting $\alpha=1$ would suggest a fundamental spacing of order $p^{-1}$ for the kinetic energy. For $p=5$ this would give a spacing $\Delta E=5^{-1}=0.2$ in units where the proportionality constant is unity. We emphasize that the proportionality constant is not fixed by any result in this paper, that the spectral claim is not derived here, and that this hypothesis is listed so that it can be tested or refuted by the same simulator platform proposed in Section 7; it is not part of the paper's supported results.

### 6.5 Open Questions

- The paper's literature base is restricted to five works, so the related-work coverage is correspondingly narrow: no independent survey of $p$-adic quantum dynamics, ultrametric diffusion, or tree-index combinatorics beyond [1]–[5] informs the modeling assumptions or the falsification structure, and any conclusion drawn here may require revision against a broader literature.
- How does the choice of prime $p$ affect the spectrum of the Vladimirov operator and hence observable energy levels?
- What are the higher moments of the displacement distribution under the protocol of Section 3.4, and do they distinguish ultrametric bounded diffusion from other confinement mechanisms?
- Can the framework be extended to multi-particle entanglement while preserving ultrametric locality, given that the Heisenberg algebra does not directly generalize on $p$-adic spaces [4]?
- Does the coarse-graining limit of Section 3.2 admit a quantitative matching condition that fixes the constant $c$ in physical units?

## 7. Practical Implications and Engineering Pathways

### 7.1 Who Would Use the Result and What Changes

The named users are quantum-hardware architects and error-correction designers. The problem they face is stated in Section 1: active error correction carries overhead factors of $10^{3}$–$10^{6}$ physical qubits per logical qubit and three irreversible operations per round whose erasure cost is bounded below by Landauer's principle [3]. If the bounded-diffusion signature holds, the decision that changes is the layout of the coupling network: instead of engineering couplers to approximate a continuous Euclidean interaction graph, the architect would engineer a hierarchical coupling graph whose connectivity realizes the $p$-adic ball structure of Section 3.4, with the branching factor $p$ becoming an explicit design parameter. The second decision that changes is the error-correction budget: a state whose excitation spread plateaus near $\mu\approx0.7$ rather than growing as $\sqrt{N}$ confines logical errors to a bounded region of the hierarchy, which in principle reduces the redundancy needed to protect them. The error-correction overhead figures themselves are not derived in this paper; only the confinement signature $\mu=0.693$, $\sigma^{2}=0.122$, and the ratio $R=0.176$ are, and the translation from confinement to qubit-overhead savings is an open engineering question (Section 6.5).

A second user group is the analysis side: experimentalists operating hierarchical quantum devices would need a tool for reading ultrametric structure out of measured time series. The degree-based extremal characterization of trees in [1] supplies a design-side check for this group as well: any proposed coupling graph can be audited against the sharp bounds $M_{1}\ge9n-16$ (even $n$) and $M_{2}\ge11n-27$ ($n\ge8$) before fabrication, exactly as the depth-$L=2$ check of Section 4.7 audits the $p=5$ ball tree. A coupling-network design whose degree profile fell below these bounds would signal a fabrication or specification error before any quantum measurement is attempted.

### 7.2 Current Readiness

Against the NASA Technology Readiness Level definitions, this work is TRL 1–2: the paper provides analytical foundations—basic principles (the Vladimirov kinetic term, the heat-equation reduction of Section 4.1) and a concept with an application formulation (the falsification structure of Section 4.6)—but no experimental proof of concept exists, and no peer-reviewed experimental realization of a $p$-adic quantum lattice is available (limitation L6). Analytical work of this kind cannot exceed TRL 3, and the present paper has not yet reached a validated analytical proof of concept against independent data: the two quantitative inputs $\mu$ and $\sigma^{2}$ come from the single assumed protocol of Section 3.4, and no claim of manufacturing or hardware readiness is made or supportable here.

### 7.3 The Smallest Next Experiment

The minimal de-risking step is a classical computation, not a quantum device: re-run the 1000-step, $p=5$ random-walk protocol of Section 3.4 with (i) an independent implementation of the Vladimirov jump kernel, (ii) a control run with a deliberately Euclidean-like kernel (failure mode F1), and (iii) extraction of the full displacement distribution, not only its mean and variance, at multiple step counts $N$. The measured quantities are the variance-to-mean ratio $R$, the higher moments of $\Delta_{p}$, and the displacement-versus-$N$ curve. The outcome that refutes the model's quantitative parameter content is a re-computed $R$ outside the window $[0.158,0.194]$ under a verified implementation of the $p=5$ topology; the outcome that refutes the bounded-diffusion hypothesis is a mean displacement growing with $N$ in the Euclidean manner, approaching the projected $21.9$ at $N=10^{6}$ rather than plateauing near $0.693$. Only after this classical cross-check passes does a hardware experiment—implementing the hierarchical coupling graph on a superconducting-circuit or trapped-ion platform and measuring excitation spread versus step count—become worth the engineering cost.

### 7.4 Binding Constraints

The constraints that would bind first, in order:

- **Topology fabrication.** The coupling network must realize the $p$-adic ball structure so that the measured $R$ is a test of the model (failure mode F3); if the fabricated graph is only approximately hierarchical, the acceptance window $[0.158,0.194]$ loses its meaning. Whether present superconducting or ion-trap fabrication can realize a faithful $p=5$ ball hierarchy at the required depth is an open question this paper does not answer.
- **Distributional statistics.** The falsification structure is calibrated on a mean and a variance only (limitation L7); a hardware test would need the full displacement distribution to distinguish ultrametric bounded diffusion from any other confinement mechanism. No higher-moment predictions are derived in this paper, so the required distributional targets are an open question.
- **Prime and order dependence.** The prediction is fixed at $p=5$, $\alpha=1$ (limitations L3, L5); a platform that can only realize other primes or other kernel exponents cannot test the specific window derived here.
- **Environmental dominance.** Decoherence not captured by the ultrametric model could mask the plateau (failure mode F2), so the experiment requires coherence times long relative to the walk duration; what coherence budget that requires is an open question, since no decoherence rate is derived in this paper.

### 7.5 Order-of-Magnitude Bounds

No cost, market, or performance projection is derivable from the two inputs $\mu=0.693$ and $\sigma^{2}=0.122$: they fix no energy scale, no fabrication cost, and no coherence requirement. The only quantitative bounds the paper can state are the diffusion comparison already derived in Section 4.5—the $p$-adic mean displacement is a factor $45.6$ smaller than the Euclidean $\sqrt{1000}\approx31.62$ benchmark at $N=1000$—and the scaling projection of Section 4.6(b), which is a labeled projection with stated assumptions: it assumes unbounded diffusive growth anchored to the assumed value $0.693$ at $N_{0}=1000$, gives $21.9\pm2.2$ at $N=10^{6}$, and carries a $\pm10\%$ uncertainty inherited linearly from the assumed $\mu$. Both quantities are in dimensionless displacement units, not physical units, because the mapping from tree depth to physical distance is not fixed by any result here. Any engineering performance figure (qubit-overhead savings, gate fidelities, coherence budgets) would require assumptions this paper does not possess and is therefore not projected.

### 7.6 Risks and Misuse Paths

The direct risk is overclaiming by analogy: the diffusion numbers described above derive from two assumed protocol inputs, and presenting them as evidence that real quantum hardware is intrinsically ultrametric—before the control-checked cross-check of Section 7.3 and any hardware test—would mislead hardware programs into redesigning coupling graphs on unsupported grounds. A second misuse path is conflating the two falsifiers: reporting a window failure as a refutation of Vladimirov dynamics, or a plateau observation as a confirmation of the parameter values, would both misstate what Section 4.6 licenses. A third is interpretive overreach: this paper's claims are confined to the falsifiable window $R\in[0.158,0.194]$ and the scaling test, and any stronger ontological reading is not licensed by the arithmetic of Section 4.

## 8. Conclusion

This paper set out to determine whether replacing the real line by the $p$-adic field $\mathbb{Q}_{p}$ yields quantum dynamics with a concrete, falsifiable diffusion signature. The answer extracted here is quantitative and narrow. Starting from the Vladimirov operator and the complex-valued $p$-adic Schrödinger convention of [4], and stating as an explicit modeling assumption the identification of tree Markov dynamics with the $p$-adic kinetic term (Section 4.1), the paper defined the 1000-step, $p=5$ tree random walk of Section 3.4 as the discrete probe of the heat dynamics. From the two assumed inputs $\mu=0.693$ and $\sigma^{2}=0.122$, explicit arithmetic gave $\sigma=0.349$, $CV=0.503$, and $R=0.176$, with the internal check $CV^{2}\cdot\mu=0.1758\approx0.176$ closing the calculation. Against the Euclidean benchmark $\sqrt{1000}\approx31.62$, the mean $p$-adic displacement is smaller by a factor $45.6$ at $N=1000$. The falsifiable content is organized into two corrected claims: the acceptance window $R\in[0.158,0.194]$ tests the assumed parameter values, and the bounded-diffusion hypothesis is tested by displacement growth versus plateau across step counts, with a projected unbounded-diffusion displacement of $21.9\pm2.2$ at $N=10^{6}$ against a plateau near $0.693$. The combinatorial cross-check of Section 4.7 confirms that the $p=5$ ball tree satisfies the sharp degree-index bounds of [1].

The result's reach is deliberately limited. It rests on two assumed numbers from a single protocol at a single step count, a single prime, and a single fractional order; it fixes no energy scale, no physical-unit mapping, and no error-correction overhead figure; and the spectral hypothesis of Section 6.4 is labeled as unestablished. What the paper does establish is that ultrametric quantum dynamics, as formulated over $\mathbb{Q}_{p}$ with Vladimirov kinetics, is not merely a formal alternative to the continuum: it produces a specific number, $R=0.176$, and a specific scaling signature, both decidable by the classical cross-check of Section 7.3 before any hardware commitment is made. If the window and the plateau survive that cross-check and a subsequent hardware test, the branching factor $p$ enters the design space of quantum architectures as a concrete parameter; if they do not, the ultrametric program loses its simplest quantitative signature and the burden of proof shifts to other observables. Either outcome is decidable by the experiment this paper specifies.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 2.0.0 (2026-11-01, from 1.0.1): rewritten in full through the research pipeline. references 8 -> 5. length 4482 -> 5842 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.40.12-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 15 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[2] https://papers.qnfo.org/papers/rg-harmonic-isomorphism. QNFO: The RG-Harmonic Isomorphism: Renormalization Group Similarities with Harmonic Quantum Mechanics.
[3] https://papers.qnfo.org/papers/ultrametric-p-adic-metrology. QNFO: Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology.
[4] https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation. QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis.
[5] https://papers.qnfo.org/papers/valuation-independent-foundations. QNFO: Valuation Without R: A Category-Theoretic Foundation for Finite Measurement.
