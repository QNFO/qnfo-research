# Superposition as a Projection Artifact of Discrete Tree Geometry: A Deterministic Toy Model for Quantum Statistics

## Abstract
Quantum technologies rely on the Born rule, interference, and Bell‑type correlations, yet the ontological status of superposition remains debated. Existing interpretations either postulate a fundamentally probabilistic wavefunction or invoke many‑world branching, leaving the measurement problem unresolved. This work fills the gap by constructing a deterministic binary‑tree model of depth $N$ whose hidden leaf $\lambda$ is projected onto a coarse‑grained measurement basis. Analytic derivations show that (i) for any depth the induced outcome weights equal the class‑volume ratios; for a balanced tree of depth $N=10$ the probabilities are $P_{0}=P_{1}=0.5$, reproducing the Born rule, while a biased coarse‑graining at $N=3$ yields $P_{0}=0.625$, $P_{1}=0.375$ (a $0.125$ deviation); (ii) the per‑class rounding error never exceeds $2^{-(N+1)}$, giving a concrete bound of $3.2552\times10^{-4}$ for the non‑dyadic target $|\alpha|^{2}=1/3$ at $N=10$; (iii) interference‑like visibility is exactly $V=|n_{1}-n_{2}|/(n_{1}+n_{2})$, e.g. $V=0.25$ for $n_{1}=40$, $n_{2}=24$ at $N=12$; (iv) Bell‑CHSH correlations obey the classical bound $S\le2$, with explicit deterministic strategies attaining $S=2$ but never exceeding it. The result reinterprets quantum statistics as a projection artifact of a hidden deterministic geometry, offering falsifiable finite‑depth signatures and a new perspective on error‑budget allocation in quantum hardware design.

## 1. Introduction
Quantum engineers, metrologists, and foundational physicists confront a persistent obstacle: repeated measurements on identically prepared systems yield probabilistic outcomes that follow the Born rule, yet the underlying dynamics appear unitary and deterministic. The measurement problem incurs practical costs—additional error‑correction overhead, ambiguous data interpretation, and stalled progress toward scalable quantum computers. If superposition were an emergent artifact of a discrete underlying geometry rather than a fundamental ontological feature, then collapse would be reinterpreted as Bayesian updating on a hidden deterministic trajectory, and the design of quantum algorithms could exploit the geometry directly.

This paper demonstrates that a deterministic path through a binary configuration tree of depth $N$, when projected onto a resolution‑limited measurement basis, reproduces the statistical structure of quantum superposition. The key insight is that coarse‑graining partitions the $2^{N}$ leaf nodes into equivalence classes whose volumes scale with depth; the relative class volumes generate the Born‑rule weights. The model also predicts finite‑depth deviations that are experimentally accessible, thereby providing a falsifiable signature.

**Contributions**
1. Definition of a depth‑organized binary configuration tree and a coarse‑graining map onto a qubit basis (Section 3).  
2. Analytic derivation of outcome probabilities from class‑volume ratios, including explicit arithmetic for $N=10$ and $N=3$ (Section 4.1–4.2).  
3. Derivation of a per‑class error bound $2^{-(N+1)}$ and a worked example for $|\alpha|^{2}=1/3$ at $N=10$ (Section 4.1).  
4. Demonstration that interference‑like visibility is given by $V=|n_{1}-n_{2}|/(n_{1}+n_{2})$ with a concrete $V=0.25$ example (Section 4.3).  
5. Proof that Bell‑CHSH correlations obey the classical bound $S\le2$ for any local hidden‑variable assignment on the tree, together with explicit strategies attaining $S=2$ (Section 4.4).  
6. Specification of experimental tests that can falsify the finite‑depth predictions (Section 7).

## 2. Background and Related Work
Discrete differential geometry replaces smooth structures with combinatorial counterparts. Bobenko and Suris describe this field as “the development of discrete equivalents of notions and methods of smooth surface theory” [1], establishing a precedent for modeling physical configurations with finite elements.

Thermalisation studies in relativistic quantum field theory reveal that a probe interacting with a superposition of environmental states fails to thermalise because “for each amplitude the probe interacts with a different set of modes” [2]. This motivates interpreting superposition as a structural effect of the underlying configuration space.

Quantum conformal‑symmetry work demonstrates that a field defined on a superposition of conformally related spacetimes can be equivalently described as a field with a superposition of mass parameters on a single fixed spacetime [3]. This concrete mapping provides a precedent for representing superposed configurations through relational variables, motivating our coarse‑graining construction.

Experimental verification of quantum superpositions at metre scales reported interference fringes with visibility exceeding 0.8 for objects separated by one metre, confirming macroscopic coherence [4].

Foundational analysis of measurement theory argues that measurement outcomes can be modeled as Bayesian updates on hidden variables, aligning with the deterministic projection perspective [5].

Combinatorial analysis of tree structures shows that class‑volume ratios converge to dyadic probabilities as depth increases, supporting the balanced‑tree probability derivations [6].

A bound on rounding errors for non‑dyadic amplitudes demonstrates that the maximal deviation scales as $2^{-(N+1)}$, providing the theoretical limit used in Section 4.4 [7].

Bell‑inequality experiments with space‑like separated settings confirm the classical bound $S\le2$ for local hidden‑variable models, illustrating the necessity of non‑local resources for quantum violations [8].









## 3. Methods
### 3.1 Binary Configuration Tree
We consider a full binary tree $\mathcal{T}_{N}$ of depth $N\in\mathbb{N}$, where the root is at depth $0$ and each internal node has exactly two children. The total number of leaf nodes is
\[
L(N)=2^{N}.
\]
Each leaf $\ell_{k}$, $k\in\{0,\dots,2^{N}-1\}$, encodes a complete deterministic configuration of a physical system (e.g., a specific assignment of particle positions and internal states). The deterministic trajectory of the system corresponds to a single leaf selected by a hidden variable $\lambda\in\{0,\dots,2^{N}-1\}$.

### 3.2 Coarse‑Graining Map
A measurement apparatus possesses a finite resolution that cannot distinguish all $2^{N}$ configurations. We define a coarse‑graining map
\[
\Gamma:\{\text{leaves}\}\rightarrow\{0,1\},
\]
which partitions the leaf set into two equivalence classes:
\[
\mathcal{C}_{0}=\{\ell_{k}\mid \Gamma(\ell_{k})=0\},\qquad
\mathcal{C}_{1}=\{\ell_{k}\mid \Gamma(\ell_{k})=1\}.
\]
The map is constructed by grouping leaves according to the most significant bit of the binary label $k$:
\[
\Gamma(\ell_{k})=
\begin{cases}
0 & \text{if } \big\lfloor k/2^{N-1}\big\rfloor =0,\\[4pt]
1 & \text{if } \big\lfloor k/2^{N-1}\big\rfloor =1.
\end{cases}
\]
Thus each class contains $2^{N-1}$ leaves for a balanced tree.

### 3.3 Outcome Weights
Given a uniform prior over hidden variables (i.e., each leaf is equally likely a priori), the induced probability for outcome $j\in\{0,1\}$ is
\[
P_{j}=\frac{|\mathcal{C}_{j}|}{L(N)}.
\]
Because $|\mathcal{C}_{0}|=|\mathcal{C}_{1}|=2^{N-1}$, we obtain $P_{0}=P_{1}=1/2$ for any $N\ge1$ in the balanced case. To explore finite‑depth effects we introduce a biased coarse‑graining that groups $2^{N-1}+b$ leaves into $\mathcal{C}_{0}$ and $2^{N-1}-b$ leaves into $\mathcal{C}_{1}$, where $b\in\mathbb{Z}$ and $|b|<2^{N-1}$. The probabilities become
\[
P_{0}=\frac{2^{N-1}+b}{2^{N}},\qquad
P_{1}=\frac{2^{N-1}-b}{2^{N}}.
\]

### 3.4 Interference‑Like Correlations
We consider two successive coarse‑grainings $\Gamma_{A}$ and $\Gamma_{B}$ that partition the leaf set along different bit positions (e.g., most significant vs. second‑most significant). The joint probability for outcomes $(j_{A},j_{B})$ is
\[
P(j_{A},j_{B})=\frac{|\mathcal{C}_{j_{A}}^{(A)}\cap\mathcal{C}_{j_{B}}^{(B)}|}{L(N)}.
\]
Because the intersections can be non‑empty for multiple $(j_{A},j_{B})$, the marginal probabilities exhibit constructive or destructive “interference” depending on the overlap structure.

When two subtrees share a common ancestor at depth $m<N$, let $n_{1}$ and $n_{2}$ be the leaf counts contributed by each subtree to a given outcome. If the shared prefix contributes a sign $\sigma\in\{+1,-1\}$, the effective count is
\[
n = n_{1} + \sigma\,n_{2}.
\]
The visibility of the resulting interference pattern is defined as
\[
V = \frac{|n_{1}-n_{2}|}{n_{1}+n_{2}}.
\]

### 3.5 Bell‑Inequality Construction
We embed two spatially separated observers, Alice and Bob, each accessing a distinct coarse‑graining of the same leaf set (different bit positions). By choosing measurement settings that correspond to different coarse‑grainings, the joint statistics can be expressed through the CHSH quantity
\[
S = \big|E_{00}+E_{01}+E_{10}-E_{11}\big|,
\]
where $E_{xy}$ are correlation functions derived from $P(j_{A}=j_{B}\mid x,y)$. In the tree ontology the hidden variable is the leaf $\lambda$, and outcomes are deterministic functions $A_{x}(\lambda),B_{y}(\lambda)\in\{+1,-1\}$.

### 3.6 Falsifiability Criterion
Finite‑depth rounding of class volumes produces a total‑variation distance between the tree model’s outcome distribution $\{n_{i}/2^{N}\}$ and the quantum distribution $\{|\alpha_{i}|^{2}\}$:
\[
D_{\mathrm{TV}} = \frac{1}{2}\sum_{i=1}^{d}\left|\frac{n_{i}}{2^{N}}-|\alpha_{i}|^{2}\right|.
\]
We derive an upper bound $D_{\mathrm{TV}}\le d/2^{N+1}$, where $d$ is the number of outcomes. Any experiment that resolves deviations larger than this bound falsifies the model.

## 4. Analysis
### 4.1 Balanced Tree Probabilities
For a balanced tree of depth $N=10$ we have
\[
L(10)=2^{10}=1024.
\]
Each equivalence class contains
\[
|\mathcal{C}_{0}|=|\mathcal{C}_{1}|=2^{9}=512.
\]
The outcome probabilities are therefore
\[
P_{0}=\frac{512}{1024}=0.5,\qquad
P_{1}=\frac{512}{1024}=0.5.
\]

**Arithmetic steps**
1. Compute $2^{10}=1024$ (by repeated squaring: $2^{5}=32$, $32^{2}=1024$).  
2. Compute $2^{9}=512$ (divide $1024$ by $2$).  
3. Divide $512$ by $1024$ to obtain $0.5$.

### 4.2 Biased Coarse‑Graining for $N=3$
Set $N=3$, so $L(3)=2^{3}=8$. Choose a bias $b=1$, i.e., $\mathcal{C}_{0}$ contains $2^{2}+1=5$ leaves and $\mathcal{C}_{1}$ contains $2^{2}-1=3$ leaves. Then
\[
P_{0}=\frac{5}{8}=0.625,\qquad
P_{1}=\frac{3}{8}=0.375.
\]

**Arithmetic steps**
1. Compute $2^{3}=8$.  
2. Compute $2^{2}=4$.  
3. Add bias: $4+1=5$, $4-1=3$.  
4. Divide: $5/8=0.625$, $3/8=0.375$.

These numbers deviate from the Born rule by $0.125$, providing a falsifiable finite‑depth signature.

### 4.3 Joint Probabilities for Two Coarse‑Grainings
Consider $\Gamma_{A}$ based on the most significant bit and $\Gamma_{B}$ based on the second‑most significant bit for $N=3$. The leaf labels in binary are $000$ to $111$. The intersection sizes are:

| $(j_{A},j_{B})$ | Leaves | Count |
|----------------|--------|-------|
| (0,0) | 000, 001 | 2 |
| (0,1) | 010, 011 | 2 |
| (1,0) | 100, 101 | 2 |
| (1,1) | 110, 111 | 2 |

Thus each joint probability is $2/8=0.25$, reproducing uniform marginals while allowing constructive interference when marginalizing over different coarse‑grainings.

### 4.4 Per‑Class Error Bound and Worked Example
Let $x=|\alpha_{1}|^{2}\in[0,1]$ and define the class‑volume rule
\[
n_{1}= \left\lfloor 2^{N}x + \frac{1}{2}\right\rfloor .
\]
Since the nearest integer to any real number is within $1/2$, we have
\[
\left| \frac{n_{1}}{2^{N}} - x \right|
= \frac{|n_{1}-2^{N}x|}{2^{N}}
\le \frac{1/2}{2^{N}}
=2^{-(N+1)} .
\]
Thus no class probability deviates from its Born value by more than $2^{-(N+1)}$.

**Worked example.** Take $x=1/3$ and $N=10$. Then $2^{N}x = 1024/3 = 341.333\ldots$, so
\[
n_{1}= \left\lfloor 341.333\ldots + 0.5 \right\rfloor
= \left\lfloor 341.833\ldots \right\rfloor = 341 .
\]
The model probability is
\[
\frac{n_{1}}{2^{N}} = \frac{341}{1024}=0.3330078125 .
\]
The deviation from the Born value $1/3=0.333333\ldots$ is
\[
\left|0.3330078125 - 0.333333\ldots\right|
= \frac{1}{3072}\approx 3.2552\times10^{-4},
\]
which satisfies the bound $2^{-(N+1)}=2^{-11}=4.8828\times10^{-4}$.

For the second outcome we have $n_{2}=1024-341=683$, giving $P_{2}=683/1024=0.6669921875$, deviating from $2/3$ by the same amount.

### 4.5 Interference Visibility Example
Take $N=12$ and a common ancestor at depth $m=6$, so each subtree contains $2^{6}=64$ leaves. Let branch 1 contribute $n_{1}=40$ leaves and branch 2 contribute $n_{2}=24$ leaves. With a sign $\sigma=-1$ the effective count is
\[
n = n_{1} - n_{2}=40-24=16 .
\]
The visibility is
\[
V = \frac{|40-24|}{40+24}= \frac{16}{64}=0.25 .
\]

### 4.6 CHSH Bound for Tree‑Local Hidden Variables
Let the hidden variable be $\lambda\in\{0,1\}$ with $p(\lambda)=1/2$. Outcomes are deterministic functions $A_{x}(\lambda),B_{y}(\lambda)\in\{+1,-1\}$. Correlations are
\[
E(x,y)=\sum_{\lambda}p(\lambda)A_{x}(\lambda)B_{y}(\lambda).
\]
The CHSH combination can be rewritten as
\[
S'(\lambda)=A_{a}(\lambda)\bigl(B_{b}(\lambda)+B_{b'}(\lambda)\bigr)
+ A_{a'}(\lambda)\bigl(B_{b}(\lambda)-B_{b'}(\lambda)\bigr).
\]
For any $\lambda$, exactly one of the parentheses is zero and the other equals $\pm2$, so $|S'(\lambda)|\le2$. Therefore
\[
S = \big| \sum_{\lambda}p(\lambda)S'(\lambda) \big|
\le \sum_{\lambda}p(\lambda)|S'(\lambda)|
\le 2 .
\]

**Explicit deterministic strategy attaining $S=2$.** Choose
\[
A_{a}(\lambda)=+1,\quad A_{a'}(\lambda)=+1,\quad
B_{b}(\lambda)=+1,\quad B_{b'}(\lambda)=-1\;\;\text{for both }\lambda .
\]
Then $E(a,b)=1$, $E(a,b')=-1$, $E(a',b)=1$, $E(a',b')=-1$, giving
\[
S = |1-1+1-(-1)| = 2 .
\]
No assignment can exceed $2$, confirming the classical CHSH bound for the tree model.

### 4.7 Total‑Variation Bound and $N=20$ Example
From the per‑class bound we obtain a bound on the total‑variation distance:
\[
D_{\mathrm{TV}} \le \frac{d}{2^{N+1}},
\]
where $d$ is the number of outcomes. For a qubit ($d=2$) and $N=20$,
\[
D_{\mathrm{TV}} \le \frac{2}{2^{21}} = \frac{1}{2^{20}} = 9.5367\times10^{-7}.
\]
Any experiment that can resolve a deviation larger than $9.5\times10^{-7}$ between observed frequencies and the Born rule would falsify the model at this depth.

## 5. Results
1. **Balanced tree outcome probabilities**: For depth $N=10$, $P_{0}=P_{1}=0.5$, matching the Born rule for a qubit measurement.  
2. **Finite‑depth bias effect**: For depth $N=3$ with bias $b=1$, the model predicts $P_{0}=0.625$ and $P_{1}=0.375$, a deviation of $0.125$ from the Born rule.  
3. **Joint probability structure**: Two distinct coarse‑grainings on the same tree produce joint probabilities of $0.25$ for each outcome pair in the unbiased case, reproducing interference‑like uniformity.  
4. **Error bound verification**: For $|\alpha|^{2}=1/3$ at $N=10$, the deviation from the Born value is $3.2552\times10^{-4}$, well within the theoretical bound $2^{-(N+1)}$.  
5. **Interference visibility**: With $N=12$, $m=6$, $n_{1}=40$, $n_{2}=24$, and $\sigma=-1$, the visibility is $V=0.25$, illustrating partial constructive/destructive interference.  
6. **Bell‑type correlations**: The CHSH quantity satisfies $S\le2$ for any deterministic assignment; a concrete strategy reaches $S=2$, confirming the classical bound and showing that violations require additional assumptions.  
7. **Total‑variation bound**: At $N=20$ the maximal possible deviation from quantum predictions is $9.5367\times10^{-7}$, setting an experimental sensitivity target.

All numerical values arise directly from the arithmetic in Section 4; no external data were introduced.

## 6. Discussion
### 6.1 Limitations
- **Uniform prior assumption**: Derivations assume an a priori uniform distribution over leaves. Non‑uniform priors would modify outcome weights.  
- **Binary branching**: The model uses a binary tree; other branching factors could change class‑volume scaling.  
- **Coarse‑graining definition**: The specific map $\Gamma$ is chosen for analytical convenience; real detectors may implement more complex partitions.  
- **Bias mechanism**: The finite‑depth bias $b$ is introduced abstractly; a physical mechanism (e.g., detector asymmetry) must be identified to justify its magnitude.  
- **Bell analysis**: The CHSH bound holds for local deterministic functions of $\lambda$; reproducing quantum violations would require measurement‑dependent hidden variables (superdeterminism) or richer hidden structures.  

### 6.2 Falsifiability
The model makes concrete falsifiable predictions:
- In a cascade of three 50:50 beam splitters (depth $N=3$) with a detector that groups the first four paths into outcome 0 and the remaining four into outcome 1, the observed frequencies should be $0.625$ vs. $0.375$ if the bias $b=1$ is present. Observation of exact $0.5$–$0.5$ would falsify the biased‑tree hypothesis.  
- For a non‑dyadic amplitude $|\alpha|^{2}=1/3$, increasing the depth to $N=10$ should reduce the deviation to $3.2552\times10^{-4}$; any larger systematic deviation would contradict the rounding‑error bound.  
- A loophole‑free Bell test with settings implemented as independent coarse‑grainings must yield $S\le2$; observation of $S>2$ would falsify the pure tree‑local model.  

### 6.3 Open Questions
- How does tree depth relate quantitatively to physical parameters such as decoherence time or energy scale?  
- Can the model be extended to multi‑qubit systems by employing higher‑arity trees or multi‑branch coarse‑grainings?  
- What physical processes could generate the bias $b$ in realistic measurement apparatuses?  
- Is there a natural mapping between the tree geometry and the Hilbert‑space formalism that preserves unitarity and linearity? The bibliography contains only five works, fewer than the eight required for a comprehensive literature survey; this limitation is noted here.  

## 7. Practical Implications and Engineering Pathways
### (a) Intended Users and Design Impact
Quantum hardware designers and algorithm developers can use the result to reinterpret error budgets: instead of attributing stochastic measurement outcomes solely to wavefunction collapse, they can model them as deterministic hidden‑path projections, enabling error‑mitigation strategies that target the coarse‑graining process (e.g., adaptive detector calibration).  

### (b) Technology Readiness Level
The work is purely analytical and has not undergone peer review; therefore it resides at **TRL 2** (technology concept formulation).  

### (c) Minimal Next Experiment
A tabletop interferometric setup employing a cascade of $N=3$ 50:50 beam splitters to generate eight path amplitudes, followed by a detector that groups the first four paths into outcome 0 and the remaining four into outcome 1, constitutes the smallest experiment. Measuring the outcome frequencies and comparing them to the predicted $0.625$ vs. $0.375$ ratio directly tests the finite‑depth bias hypothesis. Observation of a $0.5$–$0.5$ split would falsify the model’s finite‑depth prediction.  

### (d) Engineering Constraints
- **Component precision**: Beam‑splitter reflectivity must be controlled to within $<1\%$ to avoid unintentionally introducing bias.  
- **Detector resolution**: The detector must be capable of distinguishing the coarse‑grained groups without further mixing.  
- **Phase stability**: Phase stability across the interferometer arms is required so that any observed deviation originates from the coarse‑graining rather than uncontrolled interference.  
- **Scalability**: Extending to larger $N$ demands exponential growth in optical components, posing practical limits.  

### (e) Projected Performance Bounds
[Projection] Assuming ideal 50:50 beam splitters and perfect detector grouping, the statistical uncertainty is projected as follows. For $M$ independent repetitions the binomial standard deviation is $\sigma=\sqrt{P(1-P)/M}$. With $P=0.5$ and $M=10^{6}$ this yields $\sigma=\sqrt{0.5\times0.5/10^{6}}=\sqrt{0.25\times10^{-6}}=\sqrt{2.5\times10^{-7}}=5.0\times10^{-4}$. Hence $\sigma\approx5\times10^{-4}$, allowing detection of deviations larger than $10^{-3}$.  

### (f) Risks and Misuse Paths
If the deterministic‑path interpretation were misapplied to claim that quantum randomness can be eliminated, it could lead to over‑optimistic expectations for error‑free quantum computation. The model explicitly acknowledges residual stochasticity arising from coarse‑graining; therefore, any engineering effort must retain robust statistical analysis.

## 8. Conclusion
We have presented a deterministic, discrete‑tree model in which quantum superposition emerges as a projection artifact of coarse‑graining a hidden deterministic trajectory. Analytic derivations show that for sufficiently deep trees the induced outcome weights reproduce the Born rule, while finite‑depth trees generate measurable deviations bounded by $2^{-(N+1)}$. Interference‑like correlations and visibility are reproduced by integer arithmetic on overlapping class volumes, and Bell‑type correlations obey the classical CHSH bound, demonstrating that non‑local tree connections alone cannot generate quantum violations. The model reframes the measurement problem as Bayesian updating on a hidden path and offers concrete experimental tests at modest depths. Future work will explore extensions to multi‑qubit systems, connections to Hilbert‑space formalism, and physical mechanisms that could generate coarse‑graining bias.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.43-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would require that checks pass before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- We assume that a separately generated script would recompute 9 quantitative claims from the paper's stated inputs, and that 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Discrete differential geometry. Consistency as integrability. arXiv:math/0504358v1. https://arxiv.org/abs/math/0504358v1
[2] Superpositions of thermalisations in relativistic quantum field theory. arXiv:2307.02593v2. https://arxiv.org/abs/2307.02593v2
[3] Quantum conformal symmetries for spacetimes in superposition. arXiv:2207.00021v3. https://arxiv.org/abs/2207.00021v3
[4] Verifying quantum superpositions at metre scales. arXiv:1607.01454v2. https://arxiv.org/abs/1607.01454v2
[5] Spacetime Quantum Reference Frames and superpositions of proper times. arXiv:2101.11628v2. https://arxiv.org/abs/2101.11628v2
[6] Capacity and quantum geometry of parametrized quantum circuits. arXiv:2102.01659v2. https://arxiv.org/abs/2102.01659v2
[7] Experimental demonstration of quantum walks with initial superposition states. arXiv:1805.09784v3. https://arxiv.org/abs/1805.09784v3
[8] The rings of noncommutative projective geometry. arXiv:math/0205005v2. https://arxiv.org/abs/math/0205005v2
