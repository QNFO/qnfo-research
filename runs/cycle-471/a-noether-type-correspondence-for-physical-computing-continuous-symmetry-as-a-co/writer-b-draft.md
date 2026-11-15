# A Noether-Like Correspondence for Symmetry-Exploiting Physical Computing and Hybrid Intelligence

## Abstract

Physical computing systems—resonators, crystals, and cyclic structures—can perform computational work, but no general principle tells a designer when the geometry of such a substrate yields a provable reduction in computational cost. This paper addresses that gap by formalizing circular and rotational symmetry (SO(2)/U(1)) as a first-class design constraint linking physical device design and learning architectures. We derive a Noether-like correspondence: continuous symmetry of a physical computing substrate implies a conserved computational quantity, and symmetry-adapted (harmonic) decomposition of both the substrate model and the learning architecture reduces cost by factors that we compute explicitly. For a cyclic structure with 360 sectors and 1000 degrees of freedom per sector, block-diagonalization into 8 retained harmonics reduces a dense solve cost by a factor of $5.83 \times 10^{6}$ and the degrees of freedom by a factor of 45; a rotation-equivariant encoder layer with 1024 units shrinks from $1.05 \times 10^{6}$ parameters to 2048, a factor of 512. At the Landauer scale, a bit reset at 300 K costs $2.87 \times 10^{-21}$ J, so conservation of a computational quantity that avoids resets is an energy argument as well as a cost argument. The result changes practice by giving hybrid physical–digital system designers a concrete criterion—symmetry class determines the harmonic truncation and the parameter budget—rather than ad hoc tuning.

## 1. Introduction

Engineers who build edge AI systems face a widening gap between what their workloads demand and what their power and latency budgets allow. The edge-intelligence survey of [1] documents the scale of the problem: billions of mobile and IoT devices generate data that must be processed by computation-intensive deep learning models in resource-constrained environments, and its concluding remarks state that there is "a stringent need to pushing the AI frontier from the cloud to the network edge" precisely because edge computing is the recognized answer for such workloads. The same survey identifies a high-dimensional configuration problem for edge inference systems—in video analytics, frame rate, resolution, model selection and early-exit must be chosen in real time—so every principled reduction in model or substrate complexity translates directly into configuration space that a deployment no longer has to search. Today, when a designer couples a physical substrate (a resonator array, a phononic crystal, a cyclic structure) to a digital controller, the physical part is modeled at full size and the learned part is parameterized without reference to the substrate's geometry; both choices waste resources, and neither carries a guarantee.

A concrete capability would change this. If a continuous symmetry of the physical substrate could be shown to imply a conserved computational quantity—analogous to how Noether's theorem links continuous symmetries to conservation laws—then the designer would know, before building anything, which degrees of freedom are redundant and may be eliminated: the cyclic structure reduces to a single sector per harmonic, and the learning architecture coupled to it inherits the same harmonic basis. The structural-engineering precedent is well established: cyclic-symmetry modeling reduces the analysis of a full structure to a single sector, and [3] shows the mechanism in a rigorous setting, proving that for hybrid Lagrangian systems with a cyclic variable, "the degrees of freedom for the corresponding hybrid Lagrangian system can be reduced by means of" Routh reduction, with the reduction requiring two invariance properties—a cyclic regular Lagrangian and a cyclic constraint function [3, §3.2]. What is missing is the corresponding statement for computation: a derivation that ties the symmetry class of a physical computing substrate to a quantified reduction in computational cost and model parameters, stated in terms that both device designers and machine-learning architects can use.

This paper supplies that derivation. We work with the simplest nontrivial continuous symmetry, SO(2)/U(1) (rotations, equivalently phase rotations), because it is the symmetry of the most common physical computing primitives—disk resonators, ring resonators, cyclic arrays—and because [11] argues that the circle manifold $S^1$, defined as $\{z \in \mathbb{C} \mid |z| = 1\}$ or equivalently $\mathbb{R}/\mathbb{Z}$, "possesses precisely the minimal topological complexity needed to generate physical reality," making it the natural first case for any symmetry-based design principle. We state and prove a Noether-like correspondence for a class of physical computing substrates whose dynamics are invariant under a U(1) action, identify the conserved quantity, and show that it licenses harmonic (Fourier) decomposition on both sides of a hybrid physical–digital system. We then compute the cost reductions that follow, for structural-style physical modeling and for symmetry-constrained learning architectures, with all arithmetic shown.

The contributions are:

- A Noether-like theorem for a class of U(1)-symmetric physical computing substrates: invariance of the substrate dynamics under a continuous phase rotation implies conservation of a mode-occupation quantity, which we interpret as a conserved computational register (Section 4.1).
- An explicit cost derivation for harmonic truncation of cyclic physical models: for $N = 360$ sectors with $n = 1000$ degrees of freedom each and $K = 8$ retained harmonics, the degrees of freedom fall by a factor of 45 and the dense-solve cost by a factor of $5.83 \times 10^{6}$ (Section 4.2).
- An explicit parameter derivation for symmetry-constrained encoders: a rotation-equivariant layer on 1024 units with 8 harmonics at multiplicity 16 carries 2048 parameters against $1.05 \times 10^{6}$ for an unconstrained layer, a factor of 512 (Section 4.3).
- An energy argument connecting conservation to Landauer-scale cost: a bit reset at $T = 300$ K dissipates $2.87 \times 10^{-21}$ J, so a conserved quantity that eliminates resets per cycle is an efficiency mechanism, not only a compression mechanism (Section 4.4).
- A falsification criterion and a proposed minimal test: if harmonic truncation at the computed budget does not preserve task fidelity in a symmetry-constrained autoencoder benchmark, the correspondence's practical claim fails (Sections 6 and 7).

The correspondence, being stated in the language of group actions on dynamical systems and of parameterized function approximators, transfers in principle to any setting where a continuous symmetry acts on a computational substrate; two adjacent fields where the same reduction logic appears are structural dynamics of cyclic machines and equivariant learning on periodic data, and we flag both where the derivation supports them.

## 2. Background and Related Work

The physical-computation tradition. [9] articulates the Inverted Church-Turing-Deutsch thesis, positing "that physical Hamiltonian systems can serve as efficient computational substrates" and defining computation "not as the manipulation of symbols, but as the time evolution of physical systems governed by engineered Hamiltonians" [9, §2.7]. Its methodology distinguishes two modes—Class A (Ising-based optimization) and Class B (spectral synthesis)—and its Class B pipeline couples finite-difference discretization with gradient-based optimization to translate "a target list of numbers (eigenvalues) into a blueprint for a physical device (the potential $V(x)$)" [9, §4.7]. Our framework is complementary: where [9] engineers Hamiltonians to encode answers, we ask which symmetries of such engineered Hamiltonians make the encoding cheaper, and we answer with harmonic decomposition of $H_{\mathrm{Spectral}}$-type systems under U(1). [10] argues that biological and engineered computational systems implement "categorically equivalent computational architectures," with equivalence manifesting "through precise mathematical isomorphisms in energy management, information processing, and topological p[roperties]" [10, §1.0]; its validation framework proposes benchmarking neuromorphic implementations "against conventional architectures to validate the predicted gains in energy efficiency and robustness" [10, §7.0]. Our conserved-quantity result gives such benchmarks a structural target: the quantity to compare across the biological–engineered isomorphism is the symmetry-conserved mode occupation.

Symmetry and reduction in dynamics. [3] is the closest formal precedent. It studies simple hybrid systems, characterized by the tuple $\mathbf{H}=(D,X,\mathcal{S},\Delta)$ with domain $D$, vector field $X$, co-dimension-1 switching surface $\mathcal{S}$, and impact map $\Delta$ [3, §3.1], and proves that when the configuration space is $Q=P\times G$ with $G$ an abelian Lie group, a cyclic regular Lagrangian and a cyclic constraint function jointly allow definition of a Routhian $R_{c}^{\mu}:TP\to\mathbb{R}$ and a reduced constraint $\bar{h}:P\to\mathbb{R}$ [3, §3.2]. Our Theorem 1 is the computational reading of exactly this mechanism: the abelian group is U(1), the cyclic coordinate is the phase of each harmonic mode, and the "reduced" system is the harmonic-sector model. [11] supplies the topological motivation for choosing the circle as the primitive symmetry: it defines $S^1$ as $\{z \in \mathbb{C} \mid |z| = 1\}$, topologically equivalent to $\mathbb{R}/\mathbb{Z}$, "the simplest non-trivial topological space that incorporates both continuity and discreteness" [11, §1.1.1], and its verification section explicitly seeks to transform the framework "from conceptual insight to empirically testable science" through "empirical validation through direct and indirect topological measurements, and computational verification" [11, §6.0]. Our harmonic-truncation cost results are precisely such a computational verification, for the special case where the circle acts as a physical symmetry rather than a foundational ontology; we adopt [11]'s circle as a design object without endorsing its stronger ontological thesis.

Hybrid execution architectures. [2] presents Tierkreis, "a higher-order dataflow graph program representation and runtime designed for compositional, quantum-classical hybrid algorithms," motivated by the remote nature of quantum computers and the back-and-forth between classical and quantum phases that "makes understanding, debugging, and verifying quantum software unnecessarily difficult" [2, §I]. Its dataflow model—nodes as pure functional primitives, edges as port-to-port connections [2, §II-A]—is the execution substrate into which our symmetry-constrained hybrid loops would compile: a harmonic-sector physical solver and its equivariant digital controller are both pure functional nodes whose symmetry-respecting interfaces are the edges. [5] makes the locality argument quantitative in structure: it introduces the Quantum Execution Locality Framework (QELF), representing hybrid applications as directed dataflows whose key characteristic is "quantum execution locality, the extent to which computation remains resident on the QPU before measurement or synchronization," by analogy with GPU kernels that "minimize host-device communication" [5, §II], and concludes that "the effectiveness of quantum acceleration depends not only on algorithmic capability, but also on the extent to which computation remains resident on the QPU" [5, §IX]. Our conservation result is a locality statement in [5]'s sense: a conserved mode occupation means the symmetric subspace need never be synchronized out of the physical substrate, so symmetry increases effective execution locality.

Energy accounting. [4] provides the accounting conventions our energy argument adopts. It proposes two bits-per-joule metrics—Thermodynamic Epiplexity per Joule and empowerment per joule—under "explicit boundary, coarse-graining/noise, horizon/reset, and cost conventions" [4, §1], distinguishing measured energy $E_{\mathrm{cons}}$ inside an accounting boundary from thermodynamic dissipation $Q_{\mathrm{diss}}$ [4, §1.1]. Its operational proxy defines a compression gain $G^{\mathrm{MDL}}(C) = N(\ell_0 - \ell(C))$ in bits for $N$ tokens and an efficiency $\eta_{\mathcal{E}}^{\mathrm{MDL}}(C) = G^{\mathrm{MDL}}(C)/E_{\mathrm{train}}(C)$ [4, §6]. We use its reset-horizon convention in Section 4.4: a conserved quantity removes reset events from the accounting boundary, which is exactly the lever its conventions are designed to expose. Its conclusion that "meaningful comparisons require the stated conventions; without them, information gain and dissipation can be decoupled" [4, §7] is the reason we state every energy number with its boundary.

Evaluation and search framing. [7] surveys tests of machine intelligence and proposes evaluation criteria—Valid, Informative, Wide range, General, Dynamic, Unbiased, Fundamental—for any proposed measure [7, §11]. We borrow its discipline for our fidelity-versus-cost claim: the claim is checkable only relative to a stated task and truncation level, which is why Section 6 lists the exact observation that would falsify it. [6] frames hypothesis selection under finite computation: "If we assume computational resources are finite, then there is a cost to consider in the search for hypotheses," and an agent needs "a heuristic to inform its search of the space of possible hypotheses" [6, §Evaluation of Hypotheses]. Our cost-reduction factors are such a heuristic made concrete for architecture search: symmetry class prunes the hypothesis space of admissible architectures before any training run. [6]'s caution that observational data alone may be insufficient—its addition-versus-multiplication example in which "knowing a situation is observed with addition, or with multiplication, would not convey any useful information" for forming mutually exclusive rules [6, §Comparison with Respect to Experimentation]—also motivates our insistence that symmetry be encoded as a constraint rather than learned from data alone. [1], finally, supplies the deployment context and the configuration-space argument stated in Section 1: its survey of distributed training systems notes that privacy-preserving systems such as FedAvg and BlockFL dominate Table II of existing frameworks [1, §IV-D], and its inference-systems summary stresses that enabling techniques "should work in a cooperative manner" [1, §V-D]—a cooperation our hybrid substrate-plus-controller design assumes. [8] offers a boundary-based ontology in which "the single foundational element of this framework is a basic syntactic token" representing "the drawing of a boundary within an otherwise undifferentiated space" [8, §1.1], with an idempotence law under which "two adjacent and identical boundaries are structurally equivalent to a single boundary" [8, §1.4]; we cite it for the observation that redundancy-elimination laws of exactly this shape (identical elements collapse to one) are the algebraic mirror of the sector-reduction our symmetry argument performs, though we do not rely on its ontological claims.

## 3. Methods

This paper is analytical. It performs no experiment, measurement, or simulation; every number in Section 5 is computed in Section 4 from stated inputs, and every proposed test is written as a proposal in Section 7.

Model. A physical computing substrate is a dynamical system whose state $x(t)$ evolves on a configuration manifold $Q$ and whose computational role is to encode, in its asymptotic or relaxed state, the answer to a task (an optimization instance, a spectral transform, a filter response), following the Hamiltonian-engineering reading of computation of [9]. We restrict to substrates with a cyclic structure: $Q = P \times S^1$, or more generally $Q = P \times G$ with $G$ abelian, matching the setting of [3, §3.2]. The substrate dynamics are given by a regular Lagrangian $L: TQ \to \mathbb{R}$, regular in the sense of [3, §2] that $\det\left(\frac{\partial^{2}L}{\partial\dot{q}^{i}\partial\dot{q}^{j}}\right) \neq 0$.

Assumptions. (A1) The Lagrangian $L$ and any switching constraint $h$ are invariant under the U(1) action on the cyclic coordinate (the cyclic hypothesis of [3]). (A2) The computational task is invariant under the same action: rotating the substrate's phase does not change the answer, only its gauge. (A3) The retained-harmonic count $K$ and per-sector degrees of freedom $n$ are design inputs; we take $N = 360$, $n = 1000$, $K = 8$ as a representative cyclic structure (a 360-sector ring, e.g., a segmented resonator or a 360-element cyclic array) and state the sensitivity to $K$ explicitly. (A4) For the learning architecture, the encoder operates on data with an exact SO(2) symmetry and the equivariant basis is the harmonic basis on $S^1$; multiplicities are design inputs taken as $r = 16$. (A5) For the energy argument, the accounting boundary is the substrate plus its per-cycle reset logic, in the convention of [4, §1.1], and the bath temperature is $T = 300$ K.

Derivations. Section 4.1 proves the Noether-like correspondence by the standard momentum-map argument restricted to $G = U(1)$, following the reduction machinery of [3]. Sections 4.2–4.4 are arithmetic: each states its inputs, applies its formula, and shows every step.

## 4. Analysis

### 4.1 The Noether-like correspondence

Let the substrate have configuration $Q = P \times S^1$ with coordinates $(p, \theta)$, $\theta \in S^1$, and regular Lagrangian $L$ invariant under the U(1) action $\theta \mapsto \theta + \alpha$. Define the momentum conjugate to $\theta$:

$$J = \frac{\partial L}{\partial \dot{\theta}}.$$

**Claim 1 (conservation).** Along any solution of the Euler–Lagrange equations, $\frac{dJ}{dt} = 0$.

*Derivation.* The Euler–Lagrange equation for the cyclic coordinate is

$$\frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}} - \frac{\partial L}{\partial \theta} = 0.$$

By invariance under $\theta \mapsto \theta + \alpha$, $L$ does not depend on $\theta$, so $\frac{\partial L}{\partial \theta} = 0$, hence $\frac{dJ}{dt} = 0$. $\square$

This is the $G = U(1)$ case of the reduction in [3, §3.2], where the cyclic regular Lagrangian and the cyclic constraint jointly define the Routhian $R_{c}^{\mu}:TP\to\mathbb{R}$ on the reduced space; [3] states that these "two invariance properties allow to define the Routhian" and the reduced constraint function, which is the formal operation our Claim 1 instantiates.

**Claim 2 (computational reading).** If the substrate's computational output is a function of its relaxed state, and the task satisfies (A2), then the value of $J$ is a computational invariant: it is fixed at initialization, is unchanged by the computation, and every admissible computation acts only on the $P$ sector at fixed $J$. We call $J$ the conserved computational register. Its operational content: the phase degree of freedom carries no information the task can read, so no resource need be spent writing, transmitting, or resetting it.

### 4.2 Cost of harmonic truncation for cyclic physical models

Inputs (assumptions per A3): $N = 360$ sectors; $n = 1000$ degrees of freedom per sector; $K = 8$ harmonics retained. The full model has

$$D_{\mathrm{full}} = N \cdot n = 360 \times 1000 = 360{,}000 \text{ degrees of freedom}.$$

Block-diagonalization by the cyclic symmetry decomposes the full model into $K$ independent harmonic sectors, each of dimension $n$ (each harmonic couples only identical-index degrees of freedom across sectors, giving one $n \times n$ block per harmonic). The truncated model has

$$D_{\mathrm{trunc}} = K \cdot n = 8 \times 1000 = 8{,}000 \text{ degrees of freedom},$$

so the degrees-of-freedom reduction factor is

$$\frac{D_{\mathrm{full}}}{D_{\mathrm{trunc}}} = \frac{360{,}000}{8{,}000} = 45.$$

For a dense direct solve, cost scales as dimension cubed. The full-model cost in units of $n^3$ is

$$C_{\mathrm{full}} = (N n)^3 = (360 \times 1000)^3 = 360^3 \times 10^9.$$

Computing $360^3$: $360^2 = 129{,}600$; $129{,}600 \times 360 = 46{,}656{,}000$. So $C_{\mathrm{full}} = 4.6656 \times 10^{16}$ (in units of $10^{-9}$ of the natural scale; we keep the ratio form). The truncated cost is

$$C_{\mathrm{trunc}} = K \cdot n^3 = 8 \times 10^9.$$

The speedup factor is

$$\frac{C_{\mathrm{full}}}{C_{\mathrm{trunc}}} = \frac{46{,}656{,}000 \times 10^9}{8 \times 10^9} = \frac{46{,}656{,}000}{8} = 5{,}832{,}000 = 5.83 \times 10^{6}.$$

Equivalently, $\frac{N^3}{K} = \frac{360^3}{8} = \frac{46{,}656{,}000}{8} = 5{,}832{,}000$, confirming the ratio. Sensitivity to $K$: the speedup is $N^3/K$, so it degrades linearly in $K$; at $K = 36$ harmonics it is still $46{,}656{,}000/36 = 1{,}296{,}000 = 1.30 \times 10^{6}$, and the degrees-of-freedom factor is $N/K = 360/36 = 10$.

### 4.3 Parameter count for symmetry-constrained encoders

Inputs (assumptions per A4): layer width $m = 1024$; harmonic basis with $K = 8$ harmonics; multiplicity $r = 16$ per harmonic, with $K \cdot r \leq m$ required for the basis to fit the layer ($8 \times 16 = 128 \leq 1024$, satisfied).

An unconstrained linear layer carries a full matrix $W \in \mathbb{R}^{m \times m}$:

$$P_{\mathrm{full}} = m^2 = 1024^2 = 1{,}048{,}576 \text{ parameters}.$$

A rotation-equivariant layer in the harmonic basis is block-diagonal: one $r \times r$ block per harmonic, acting within each harmonic's multiplicity space, giving

$$P_{\mathrm{eq}} = K \cdot r^2 = 8 \times 16^2 = 8 \times 256 = 2{,}048 \text{ parameters}.$$

The reduction factor is

$$\frac{P_{\mathrm{full}}}{P_{\mathrm{eq}}} = \frac{1{,}048{,}576}{2{,}048} = 512.$$

Sensitivity: the factor is $m^2/(K r^2)$; at $r = 32$, $K = 8$, it is $1{,}048{,}576/(8 \times 1024) = 1{,}048{,}576/8192 = 128$. The equivariant parameter count is independent of $m$ once $K r \leq m$, so the savings grow quadratically in $m$: at $m = 4096$ with the same $K, r$, $P_{\mathrm{full}} = 4096^2 = 16{,}777{,}216$ and the factor is $16{,}777{,}216/2048 = 8192$.

### 4.4 Landauer-scale energy of the conserved register

Inputs: bath temperature $T = 300$ K (A5); Boltzmann constant $k_{\mathrm{B}} = 1.380649 \times 10^{-23}$ J/K; $\ln 2 = 0.693147$. The Landauer cost of one logically irreversible bit reset is

$$E_{\mathrm{bit}} = k_{\mathrm{B}} T \ln 2 = (1.380649 \times 10^{-23}) \times 300 \times 0.693147.$$

Step 1: $1.380649 \times 300 = 414.1947$, so $k_{\mathrm{B}} T = 4.141947 \times 10^{-21}$ J. Step 2: $4.141947 \times 0.693147 = 2.87088 \times 10^{-21}$. So

$$E_{\mathrm{bit}} = 2.87 \times 10^{-21} \text{ J per reset at } 300 \text{ K}.$$

By Claim 2, the conserved register $J$ is written once at initialization and never reset. If a hybrid cycle would otherwise reset a phase register of $b$ bits per cycle, the avoided dissipation per cycle is

$$E_{\mathrm{avoided}} = b \cdot E_{\mathrm{bit}} = b \times 2.87 \times 10^{-21} \text{ J}.$$

For illustration with $b = 8$: $E_{\mathrm{avoided}} = 8 \times 2.87088 \times 10^{-21} = 2.297 \times 10^{-20}$ J per cycle. This is a projection under assumptions A1–A5 and the stated boundary convention of [4, §1.1]; it is a floor-scale argument (real resets cost many $k_{\mathrm{B}}T$), and its role is to establish that conservation converts to energy, not to predict end-to-end system savings. The accounting matters: [4] distinguishes $E_{\mathrm{cons}}$ from $Q_{\mathrm{diss}}$ and warns that without explicit conventions "information gain and dissipation can be decoupled" [4, §7]; our number is a $Q_{\mathrm{diss}}$-side floor inside the stated boundary.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions; none is measured or simulated.

1. **Conserved computational register (Claim 1–2, Section 4.1).** For any U(1)-symmetric substrate with regular cyclic Lagrangian, the conjugate momentum $J = \partial L/\partial \dot{\theta}$ is conserved and acts as a computational invariant at fixed task gauge. This is a structural result, not a number.

2. **Degrees-of-freedom reduction (Section 4.2).** For $N = 360$, $n = 1000$, $K = 8$: $D_{\mathrm{full}} = 360{,}000$, $D_{\mathrm{trunc}} = 8{,}000$, reduction factor **45**.

3. **Dense-solve speedup (Section 4.2).** Same inputs: $C_{\mathrm{full}}/C_{\mathrm{trunc}} = N^3/K = 5{,}832{,}000 \approx \mathbf{5.83 \times 10^{6}}$. At $K = 36$: $1.30 \times 10^{6}$; degrees-of-freedom factor 10.

4. **Encoder parameter reduction (Section 4.3).** For $m = 1024$, $K = 8$, $r = 16$: $P_{\mathrm{full}} = 1{,}048{,}576$, $P_{\mathrm{eq}} = 2{,}048$, reduction factor **512**. At $m = 4096$ with the same harmonic budget: factor 8192.

5. **Landauer floor and avoided resets (Section 4.4, projection).** $E_{\mathrm{bit}} = 2.87 \times 10^{-21}$ J at 300 K; avoided dissipation $b \cdot E_{\mathrm{bit}}$, e.g., $2.30 \times 10^{-20}$ J per cycle for $b = 8$. Labeled a projection under A1–A5 and the boundary convention of [4].

## 6. Discussion

The correspondence is proved only for the case where the symmetry group is abelian and acts on a cyclic coordinate, and only for tasks that respect the symmetry (A2). The Routh-reduction precedent of [3] requires exactly the two invariance properties—a cyclic Lagrangian and a cyclic constraint—and a hybrid system whose guard or reset map breaks the symmetry falls outside the theorem; a substrate whose readout distinguishes phases (a gauge-dependent task) likewise forfeits Claim 2. The cost factors of Sections 4.2–4.3 assume the harmonic truncation preserves task fidelity; we have derived the cost side only, and the fidelity side is the empirical question the framework cannot settle analytically.

**What would falsify the main result.** The practical claim—that symmetry-constrained substrates and architectures deliver the computed savings at preserved fidelity—would be falsified by a single reproducible demonstration on a U(1)-symmetric task in which the $K = 8$ harmonic truncation (or the 2048-parameter equivariant layer) suffers a fidelity loss that no admissible $K$ within the computed budget recovers, while an unconstrained model of the same task succeeds. A second falsifier is theoretical: a counterexample substrate with continuous U(1) invariance of $L$ whose computational output nevertheless depends on $\theta$, which would break Claim 2 and show the momentum-map reading fails for relaxed-state computation.

**Limitations list.** (i) Abelian-group restriction: the derivation uses $G = U(1)$; non-abelian symmetries need representation theory beyond Section 4 and are open. (ii) Task gauge invariance (A2): sensitive—if the task reads phase, the entire reduction collapses. (iii) Regularity of $L$ (A1, per [3, §2]): degenerate Lagrangians are excluded. (iv) Harmonic-count choice: the speedup $N^3/K$ degrades linearly in $K$; if fidelity requires $K$ comparable to $N$, the savings vanish (at $K = N$ the factor is $N^2$, still large for dense solves, but the degrees-of-freedom factor becomes 1). (v) Equivariant basis exactness (A4): data with only approximate symmetry erodes the 512× parameter factor in proportion to the symmetry violation, an effect we have not quantified. (vi) Energy projection: the $2.87 \times 10^{-21}$ J figure is a thermodynamic floor under the [4] conventions; real reset energies are higher, so the projection bounds savings from below but says nothing about control electronics. (vii) No empirical content yet: every number is analytical under stated assumptions; the framework's predictions have not been tested on hardware or in training runs. (viii) The stronger ontological reading of circular topology in [11] is not used or endorsed; only the design-level role of $S^1$ enters.

**Open questions.** Does the correspondence extend to discrete symmetries (cyclic groups $C_N$), where the harmonic decomposition is the discrete Fourier transform and the conservation statement weakens? What is the correct analogue of the momentum map for stochastic substrates, e.g., the Ising-class engines of [9]? Can the conserved register be measured experimentally as a winding number in the sense of topological observables, connecting to the verification strategies [11, §6.0] proposes?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are designers of cyclic physical computing substrates—ring and disk resonator arrays, cyclic phononic structures, segmented rotors used as analog solvers—and the engineers who build the hybrid controllers around them, in the sense of the dataflow hybrid systems of [2] and [5]. For them the result changes one design decision: instead of modeling the full $N$-sector structure and tuning an unconstrained controller, they fix the symmetry class, retain $K$ harmonics justified by the task's spectral content, and budget the digital side at $K r^2$ parameters per equivariant layer. For edge-AI system architects, the framework addresses the configuration problem [1, §V-D] documents: symmetry class is a discrete design choice that removes whole families of configuration parameters (model width, sector count) from real-time search. For benchmark designers in the style of [10, §7.0], the conserved register is the quantity to track across biological and engineered implementations.

**(b) Readiness.** This work is purely analytical and has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2: basic principles observed and reported (the reduction mechanism of [3], the accounting conventions of [4]) and a concept formulated. It does not exceed TRL 3, and no manufacturing or hardware readiness is claimed.

**(c) Smallest next test.** The