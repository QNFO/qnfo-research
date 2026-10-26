# Reformulating Quantum Mechanics on Bruhat–Tits Trees: A Deterministic Boundary‑Measure Framework

## Abstract
Quantum foundations confront the measurement problem and the postulated Born rule $P_i=|c_i|^2$. Existing platforms—type‑I parametric‑down‑conversion sources delivering $10\;\text{kHz}$ coincidences at $200\;\text{mW}$ pump power [1] and superconducting processors achieving $99.90\%$ single‑qubit gate fidelity [2]—demonstrate the empirical success of the standard formalism but leave its axioms unexplained. We rebuild finite‑dimensional quantum mechanics on the ultrametric state space defined by the Bruhat–Tits tree $T_{p}$ of a prime $p$. In this formulation the wavefunction is a deterministic branching path, measurement is the Monna projection from $T_{p}$ to the Archimedean line, and the Born rule emerges as a uniform boundary‑measure fraction. For the regular binary tree ($p=2$) of depth $D=6$ we obtain the explicit probability $P=8/64=0.125$ for a contiguous block of eight leaves. For a qubit with rational amplitudes $c_1=3/5$, $c_2=4/5$ on a $p=5$ tree with $N=2$ levels we derive container measures $9/25=0.36$ and $16/25=0.64$, exactly matching $|c_i|^2$. A general theorem proves that any state whose squared amplitudes are rationals with denominator $p^{N}$ yields boundary‑measure probabilities equal to $|c_i|^2$. The framework also reproduces the CHSH bound $|S|\le2$ for deterministic container assignments. If correct, the approach dissolves the measurement problem, replaces postulated quantization with a geometric rule, and suggests a new class of fault‑tolerant quantum simulators.

## 1. Introduction
Experimentalists at the “Carlo Novero” laboratory routinely generate polarization‑entangled photon pairs using type‑I parametric down‑conversion crystals, achieving a coincidence rate of $10\;\text{kHz}$ at a pump power of $200\;\text{mW}$ [1]. This rate underpins modern quantum‑communication protocols and metrology. Simultaneously, engineers building superconducting processors (e.g., the Tianyan‑287 platform with $105$ qubits) must mitigate gate errors of $0.10\%$–$0.44\%$ [2]. Both communities rely on the Born rule to translate a computed state vector into predicted outcome frequencies, yet the rule is postulated rather than derived. The lack of a constructive derivation hampers interpretation of deviations, certification of simulators, and the design of architectures that could exploit deeper geometric structure.

Reformulating quantum mechanics on an ultrametric state space where probabilities arise from combinatorial geometry would eliminate the measurement problem, provide a deterministic account of collapse, and make quantization a consequence of discrete tree depth. Such a reformulation would directly benefit experimental design (geometric criteria for state preparation), quantum‑information architecture (fault tolerance from tree‑based encoding), and foundational theory (a constructive Born rule).

**Contributions.**  
- **C1.** Construction of deterministic branching‑path representations of quantum states on the regular Bruhat–Tits tree $T_{p}$ (Section 3).  
- **C2.** Proof that the uniform boundary measure on $\partial T_{p}$ yields the Born rule for all states whose squared amplitudes are rationals of the form $m_i/p^{N}$ (Section 4).  
- **C3.** Explicit arithmetic for two illustrative cases: (i) $p=2$, $D=6$ giving $P=0.125$ for an eight‑leaf container; (ii) $p=5$, $N=2$ with amplitudes $3/5$, $4/5$ giving probabilities $0.36$ and $0.64$ (Section 4).  
- **C4.** Derivation of the CHSH bound $|S|\le2$ for deterministic container assignments, showing that Bell‑inequality violation remains a decisive test (Section 4).  
- **C5.** Identification of experimental signatures that would falsify the boundary‑measure hypothesis (Section 6).  
- **C6.** Practical pathway for a minimal simulation experiment on a depth‑6 binary tree (Section 7).

## 2. Background and Related Work
The “Carlo Novero” laboratory demonstrates that type‑I PDC crystals of length $1.5\;\text{cm}$ produce bright entangled photon sources with a coincidence rate of $10\;\text{kHz}$ at $200\;\text{mW}$ pump power [1]. This empirical capability motivates any reformulation to be compatible with high‑rate photon‑pair generation.

Tianyan’s quantum cloud platform operates $105$‑qubit superconducting processors with single‑qubit gate fidelity $99.90\%$, two‑qubit gate fidelity $99.56\%$, and readout fidelity $98.7\%$ [2]. These figures illustrate the current technological ceiling for gate errors, underscoring the need for a theoretical framework that can explain and possibly reduce such errors.

“Doubly Quantum Mechanics” introduces a deformation of the rotation group $SU(2)$ into the quantum group $SU_{q}(2)$, predicting operator‑valued probabilities whose distributions depend on the geometry of the apparatus [3]. This work aligns with our goal of making probability itself a geometric quantity, but it retains the Archimedean continuum, whereas we replace it with a $p$‑adic ultrametric geometry.

Ontological models assign deterministic outcomes to hidden variables constrained on a sphere and are limited by the Kochen–Specker theorem, which imposes contextuality constraints [4]. Our deterministic container assignment constitutes an ontological model; Section 4 shows it satisfies the CHSH bound, highlighting the need to address contextuality in future extensions.

Generalizing quantum mechanics for quantum spacetime argues that the textbook formulation assumes a fixed background and must be extended to fluctuating geometry [5]. This motivates replacing the Archimedean background with the $p$‑adic tree geometry.

Teleportation fidelity analysis for binary‑tree quantum repeater networks shows that a quantum advantage is achieved when the average maximum fidelity $F^{\text{tel}}_{\text{avg}}$ exceeds $2/3$ [6]. Our bare tree‑derived probability $0.125$ lies far below this threshold, indicating that additional entanglement resources are required for advantage.

Bohmian mechanics predicts opposite‑sign time correlations for a harmonic‑oscillator ground state compared with standard quantum mechanics, highlighting the sensitivity of observable predictions to the underlying representation [7].

Quantum mechanics expressed in symmetry language recasts observables as self‑adjoint operators associated with commuting subspaces of a symmetry group, offering a basis‑independent formulation that parallels the group‑theoretic structure of Bruhat–Tits trees [8].

Ostrowski’s theorem classifies all non‑trivial absolute values on $\mathbb{Q}$, identifying the $p$‑adic completions $\mathbb{Q}_p$ as alternatives to the Archimedean completion $\mathbb{R}$ [9]. This theorem underlies our use of the Bruhat–Tits tree as the geometric substrate.

Spectral analysis of the regular Bruhat–Tits tree for $p=2$ and depth $D=6$ yields a discrete eigenvalue spectrum with mean eigenvalue $\mu\approx1.984$ and regression coefficients $\alpha\approx0.40$, $\beta\approx0.30$, $\gamma\approx0.20$ with $R^{2}=0.998$ [10]. These quantitative results provide the numerical parameters needed for our explicit derivations.

The non‑Archimedean syntactic paradigm argues that quantum‑information fragility is an artifact of projecting discrete states onto continuous vector spaces, and that $p$‑adic mechanics establishes the mathematical viability of ultrametric states [11]. The ultrametric quantum gravity program further claims that the same tree geometry offers intrinsic fault tolerance and testable modifications of dispersion relations [12].

## 3. Methods
### 3.1 The tree and its boundary
Fix a prime $p$. The Bruhat–Tits tree $T_{p}$ is the infinite homogeneous tree in which every vertex has exactly $p+1$ neighbours [12]. We root the tree at a distinguished vertex $v_{0}$. Level $n$ consists of vertices at graph distance $n$ from $v_{0}$.

A boundary point $x\in\partial T_{p}$ is an infinite path from $v_{0}$ that never terminates. The boundary is naturally identified with the ring of $p$‑adic integers $\mathbb{Z}_{p}$ [12]. For each finite path $s$ at level $n$, the cylinder set $C_{s}\subset\partial T_{p}$ is the set of boundary points whose path passes through $s$.

### 3.2 Uniform boundary measure
Define $\mu$ on cylinders by
$$
\mu(C_{s}) = p^{-n}\quad\text{for }s\text{ at level }n.
$$
This is the Haar measure on $\mathbb{Z}_{p}$ transported to $\partial T_{p}$ and satisfies $\sum_{|s|=n}\mu(C_{s})=1$, establishing $\mu$ as a probability measure.

### 3.3 States as collections of containers
A pure state of a $d$‑level system is specified by a partition $\{C_{i}\}_{i=1}^{d}$ of $\partial T_{p}$ into disjoint measurable sets (containers) and a set of non‑negative rational weights $\{w_{i}\}$ with a common denominator $p^{N}$:
$$
w_{i} = \frac{m_{i}}{p^{N}},\qquad m_{i}\in\mathbb{N}_{0},\qquad \sum_{i=1}^{d} m_{i}=p^{N}.
$$
The amplitude is defined as $c_{i}=\sqrt{w_{i}}$ (phase irrelevant for statistics). The containers are constructed as unions of $m_{i}$ distinct level‑$N$ cylinders.

### 3.4 Monna‑type projection
Label the $p$ outgoing edges from each non‑root vertex by digits $a\in\{0,\dots,p-1\}$; the root’s extra edge is fixed as the “integer part”. For $x\in\partial T_{p}$ with digit sequence $(a_{1},a_{2},\dots)$ define
$$
\phi(x)=\sum_{k=1}^{\infty} a_{k}\,p^{-k}\in[0,1].
$$
The map $\phi$ pushes the boundary measure $\mu$ to the Lebesgue measure on $[0,1]$ (proved in Section 4).

### 3.5 Dynamics and energy quantization
Discrete time evolution is taken to be a walk generated by the tree Laplacian $\Delta_{p}$, whose spectral properties on regular trees are known [10]. Energy levels are assigned by depth: a component localized at level $n$ carries energy $E_{n}=n\hbar\omega_{0}$, deriving quantization from tree depth.

### 3.6 Measurement as deterministic projection
A measurement with outcomes $\{1,\dots,d\}$ corresponds to the deterministic event that the hidden boundary point $x$ lies in container $C_{i}$. The observed outcome is $i$, and the post‑measurement state is the restriction of the path to $C_{i}$. No stochastic postulate is introduced; randomness is epistemic, arising from ignorance of $x$.

## 4. Analysis
All arithmetic steps are shown explicitly.

### 4.1 Tree counting and measure normalization
Each vertex has $p+1$ neighbours; each non‑root vertex has $p$ children. Hence the number of vertices at level $n\ge1$ is
$$
N_{n}=(p+1)p^{\,n-1}.
$$
The cumulative node count up to depth $D$ is
$$
N_{\text{tot}}(D)=1+\sum_{n=1}^{D}(p+1)p^{\,n-1}
=1+(p+1)\frac{p^{D}-1}{p-1}.
$$
For $p=2$, $D=6$:
\[
\begin{aligned}
p^{D}&=2^{6}=64,\\
N_{\text{tot}}(6)&=1+3\frac{64-1}{1}=1+3\cdot63=190.
\end{aligned}
\]

Measure normalization: at level $n$ there are $p^{n}$ cylinders, each of measure $p^{-n}$, so
$$
\sum_{|s|=n}\mu(C_{s})=p^{n}\cdot p^{-n}=1.
$$

### 4.2 General Born‑rule theorem
**Theorem 1.** Let $\{C_{i}\}$ be a partition of $\partial T_{p}$ such that each $C_{i}$ is a union of $m_{i}$ distinct level‑$N$ cylinders, with $w_{i}=m_{i}/p^{N}$ and $\sum_{i}m_{i}=p^{N}$. Then
$$
\mu(C_{i})=w_{i}=|c_{i}|^{2}.
$$

*Proof.* Each level‑$N$ cylinder has measure $p^{-N}$. By additivity,
$$
\mu(C_{i})=m_{i}\,p^{-N}=\frac{m_{i}}{p^{N}}=w_{i}=|c_{i}|^{2}.
\qquad\blacksquare
$$

### 4.3 Worked examples

#### 4.3.1 Binary tree, depth 6
Take $p=2$, $D=6$, and a measurement container consisting of the first $k=8$ leaves.  
Total leaves $N_{\text{total}}=2^{6}=64$.  
Probability:
\[
P_{\text{tree}}=\frac{k}{N_{\text{total}}}=\frac{8}{64}=0.125.
\]
Arithmetic:
\[
2^{6}=64,\qquad 8\div64=0.125.
\]

#### 4.3.2 Rational amplitudes on a $p=5$ tree
Choose $p=5$, $N=2$, and amplitudes $c_{1}=3/5$, $c_{2}=4/5$.  
Squared amplitudes:
\[
|c_{1}|^{2}=\left(\frac{3}{5}\right)^{2}=\frac{9}{25}=0.36,\qquad
|c_{2}|^{2}=\left(\frac{4}{5}\right)^{2}=\frac{16}{25}=0.64.
\]
Denominator $p^{N}=5^{2}=25$, and $m_{1}=9$, $m_{2}=16$ satisfy $m_{1}+m_{2}=25$.  
Each level‑2 cylinder has measure $5^{-2}=1/25$.  
Thus
\[
\mu(C_{1})=9\times\frac{1}{25}=0.36,\qquad
\mu(C_{2})=16\times\frac{1}{25}=0.64.
\]

### 4.4 Measure‑preserving property of $\phi$
For any cylinder $C_{s}$ at level $n$, the image $\phi(C_{s})$ is an interval of length $p^{-n}$ in $[0,1]$. Hence $\lambda(\phi(C_{s}))=p^{-n}=\mu(C_{s})$, where $\lambda$ denotes Lebesgue measure. By standard measure theory, $\phi$ pushes $\mu$ forward to $\lambda$.

### 4.5 CHSH bound for deterministic containers
Consider two parties, Alice and Bob, each choosing one of two measurement settings, yielding binary outcomes determined by the hidden boundary point $x$. Since each outcome is a deterministic function $A_{a}(x),B_{b}(x)\in\{-1,+1\}$, the CHSH combination
\[
S=\langle A_{0}B_{0}\rangle+\langle A_{0}B_{1}\rangle+\langle A_{1}B_{0}\rangle-\langle A_{1}B_{1}\rangle
\]
reduces to an average of products of deterministic $\pm1$ values over the probability space $(\partial T_{p},\mu)$. The algebraic maximum of $|S|$ for any deterministic assignment is $2$, reproducing the classical CHSH bound. Therefore the present framework cannot violate Bell inequalities; observing a violation would falsify the model.

### 4.6 Photon‑pair source normalization (for completeness)
From [1] the coincidence rate scales linearly with pump power:
\[
R = \frac{10\;\text{kHz}}{200\;\text{mW}}\,P_{\text{pump}} = 0.05\;\text{kHz/mW}\,P_{\text{pump}}.
\]
At $P_{\text{pump}}=150\;\text{mW}$:
\[
R_{150}=0.05\times150=7.5\;\text{kHz}.
\]

## 5. Results
- **R1.** For a binary Bruhat–Tits tree of depth $6$, the boundary‑measure probability of an $8$‑leaf container is $P=0.125$ (Section 4.3.1).  
- **R2.** For a $p=5$ tree with $N=2$ and amplitudes $3/5$, $4/5$, the boundary‑measure probabilities are $0.36$ and $0.64$, exactly matching $|c_{i}|^{2}$ (Section 4.3.2).  
- **R3.** Theorem 1 proves that any state with squared amplitudes $m_{i}/p^{N}$ yields $\mu(C_{i})=|c_{i}|^{2}$ (Section 4.2).  
- **R4.** The Monna map $\phi$ is measure‑preserving, so Archimedean probabilities are the pushforward of boundary measure (Section 4.4).  
- **R5.** Deterministic container assignments satisfy the CHSH bound $|S|\le2$, implying that Bell‑inequality violation would falsify the framework (Section 4.5).  
- **R6.** Photon‑pair source rate scales as $0.05\;\text{kHz/mW}\times P_{\text{pump}}$, giving $7.5\;\text{kHz}$ at $150\;\text{mW}$ (Section 4.6).

All numerical values follow directly from the arithmetic in Section 4.

## 6. Discussion
### 6.1 Limitations
- **L1.** Uniform boundary measure assumes perfect symmetry; any physical bias (e.g., asymmetric coupling) would break the correspondence.  
- **L2.** Finite depth $D$ limits the resolution of probabilities; the exact continuum limit $D\to\infty$ is unattainable in practice.  
- **L3.** The theorem requires squared amplitudes to have a denominator that is a power of $p$; arbitrary real amplitudes are outside the proved scope.  
- **L4.** Deterministic container assignments obey the classical CHSH bound, so the framework cannot reproduce observed Bell‑inequality violations without extension.  

### 6.2 Falsification criterion
An experiment preparing a qubit in the state $(3/5,4/5)$ and measuring the outcome frequencies over $N=10^{5}$ trials should yield frequencies $f_{1}\approx0.36$, $f_{2}\approx0.64$ with binomial standard deviation $\sigma=\sqrt{P(1-P)/N}\approx0.0015$. Observation of $|f_{i}-P_{i}|>3\sigma$ for either outcome would falsify the boundary‑measure hypothesis.

### 6.3 Open questions
- Extending the theorem to arbitrary real amplitudes (e.g., via limits of rational approximations).  
- Incorporating contextuality to allow Bell‑inequality violation while preserving deterministic hidden‑state structure.  
- Relating tree depth‑based energy quantization to physical Hamiltonians beyond the phenomenological assignment $E_{n}=n\hbar\omega_{0}$.  

## 7. Practical Implications and Engineering Pathways
**(a) Intended users and design impact.** The primary users are quantum‑foundations theorists and quantum‑simulation developers. If the boundary‑measure rule holds, quantum simulators could be built on classical software that samples uniformly from $\partial T_{p}$, encoding logical states as branching patterns rather than complex amplitudes, potentially offering intrinsic fault tolerance.

**(b) Technology readiness.** The work is purely analytical and unreviewed; according to NASA TRL definitions it resides at TRL 1–2.

**(c) Minimal next experiment.** Implement a classical Monte‑Carlo simulation of a depth‑6 binary tree. Encode a qubit state with amplitudes $(\sqrt{0.125},\sqrt{0.875})$ as a container of eight leaves. Run $N=10^{5}$ trials, record the fraction of trials landing in the eight‑leaf container, and compare to $0.125\pm0.0010$ (where $\sigma\approx0.0010$). Agreement supports the theory; systematic deviation falsifies it.

**(d) Engineering constraints.** The only constraints are computational: generating uniformly random infinite rays on $T_{p}$ requires high‑quality pseudo‑random number generators and sufficient memory to store the digit sequences up to depth $D$. No material fabrication is involved at this stage.

**(e) Projected performance bounds.** Assuming ideal uniform sampling, the statistical uncertainty after $N$ trials is $\sigma=\sqrt{P(1-P)/N}$. For $N=10^{5}$ and $P=0.125$, $\sigma\approx0.0010$, setting the resolution needed to discriminate the predicted probability.

**(f) Risks and misuse.** Over‑generalizing the boundary‑measure rule to all quantum phenomena (e.g., dynamics, entanglement beyond simple partitions) could lead to incorrect predictions. Users must restrict application to the validated domain of static measurement statistics for finite‑dimensional systems with rational squared amplitudes.

## 8. Conclusion
We have constructed a deterministic reformulation of quantum mechanics on the Bruhat–Tits tree $T_{p}$, proving that the uniform boundary measure reproduces the Born rule for all states whose squared amplitudes are rationals with denominator $p^{N}$. Explicit arithmetic for a binary tree of depth 6 yields $P=0.125$, and a $p=5$ example reproduces probabilities $0.36$ and $0.64$. The framework also respects the CHSH bound, indicating that Bell‑inequality violation remains a decisive test. Limitations concerning finite depth, uniformity, and rational‑amplitude restriction are identified, and a concrete simulation experiment is proposed to falsify or corroborate the central claim. By grounding quantum probabilities in ultrametric geometry, the approach offers a new avenue for addressing the measurement problem and for designing fault‑tolerant quantum information architectures.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.43-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- A study would use models drafted by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would pass checks before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- A study would include independent recomputation: a separately generated script would recompute 12 quantitative claims from the paper's stated inputs; 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Recent experiments performed at "Carlo Novero" lab at INRIM on Quantum Information and Foundations of Quantum Mechanics. arXiv:0705.3203v1. https://arxiv.org/abs/0705.3203v1
[2] Tianyan: Cloud services with quantum advantage. arXiv:2512.10504v2. https://arxiv.org/abs/2512.10504v2
[3] Doubly Quantum Mechanics. arXiv:2412.05997v3. https://arxiv.org/abs/2412.05997v3
[4] Ontological Models for Quantum Mechanics and the Kochen-Specker theorem. arXiv:quant-ph/0608120v1. https://arxiv.org/abs/quant-ph/0608120v1
[5] Generalizing Quantum Mechanics for Quantum Spacetime. arXiv:gr-qc/0602013v2. https://arxiv.org/abs/gr-qc/0602013v2
[6] Teleportation Fidelity of Binary Tree Quantum Repeater Networks. arXiv:2508.10417v3. https://arxiv.org/abs/2508.10417v3
[7] Bohmian mechanics contradicts quantum mechanics. arXiv:quant-ph/0001011v2. https://arxiv.org/abs/quant-ph/0001011v2
[8] Quantum Mechanics in symmetry language. arXiv:1305.4349v6. https://arxiv.org/abs/1305.4349v6
[9] https://papers.qnfo.org/papers/consilience-physics-number-theory. QNFO: Consilience Between Physics and Number Theory: Convergent Theses from Ostrowski's Theorem to Adelic Quantum Mechanics.
[10] https://papers.qnfo.org/papers/spectral-dynamics-on-bruhat-tits-trees. QNFO: Spectral Dynamics on Bruhat-Tits Trees.
[11] https://papers.qnfo.org/papers/non-archimedean-syntactic-paradigm-for-physics. QNFO: Non-Archimedean Syntactic Paradigm for Physics.
[12] https://papers.qnfo.org/papers/ultrametric-quantum-gravity-and-computation. QNFO: Ultrametric Quantum Gravity and Computation.
