# Grounding block - source: rem-15b819c9-8f0f-4b57-ae3a-8dba2da7395c

## Research idea

Correct the published paper 'static-p-adic-holographic-tree-as-a-fixed-universal-structure' for erratum pl-static-p-adic-holographic-tree-as-a-fixed-universal-structure-1.0.1-0: Detection threshold of 5% (ε exceeding 0.05 for a >3σ detection) versus null-result threshold ε<0.01.
Also: rev-static-p-adic-holographic-tree-as-a-fixe-1ltnjol: [missing-limitations] The prediction is stated without specifying amplitude, phase, or observational uncertainty, and no quantitative comparison to existing CMB data is given. At: "The model predicts a log‑periodic modulation of the CMB power spectrum with period log p, providing a falsifiable signature."
Also: rev-static-p-adic-holographic-tree-as-a-fixe-15o0kj8: [overclaim/unsupported] The chordality condition is not defined in the paper, and no proof or citation establishes that the p-adic tree satisfies it. At: "Our tree satisfies this condition by construction, providing a concrete realization of holographic entropy bounds."
Also: rev-static-p-adic-holographic-tree-as-a-fixe-1m6lq5u: [terminology-isolation] The term 'chordality condition' is used but never defined anywhere in the paper. At: "chordality condition"

## Existing paper under revision (remediation only)

# Static p‑adic Holographic Tree as a Fixed Universal Structure

## Abstract
The observed cosmic microwave background (CMB) exhibits a near‑scale‑invariant spectrum that is conventionally explained by inflationary dynamics. Yet the underlying mechanism that generates the holographic entropy bound and the apparent flow of time remains unsettled. We propose that the universe is a static hierarchical tree endowed with a p‑adic ultrametric geometry and a holographic information assignment to its nodes. In this framework spacetime and dynamics emerge from observer worldlines that are paths in the tree, while the tree’s fixed combinatorial structure encodes all physical degrees of freedom. We formalize the tree, derive an effective Friedmann‑like expansion law from the discrete proper‑time defined by edge traversal, and compute the holographic entropy associated with a finite depth. For a binary tree (p = 2) at depth n = 10 we obtain an effective Hubble‑like parameter H = ln 2 $\approx$ 0.693 (tree‑time units) and a holographic entropy bound of S $\approx$ 25.4 bits, consistent with the observed CMB entropy density up to an order‑of‑magnitude factor. The model predicts a log‑periodic modulation of the CMB power spectrum with period log p, providing a falsifiable signature. Contributions are: (1) a precise definition of the static p‑adic holographic tree and observer worldlines; (2) an analytic derivation of emergent Friedmann dynamics; (3) a quantitative entropy estimate matching holographic bounds; (4) a concrete observational test; and (5) a roadmap for experimental validation.

## 1. Introduction
Modern cosmology faces a concrete problem: the CMB temperature anisotropies are explained by an early‑time inflationary phase that requires a scalar field with finely tuned potential, while the holographic entropy bound $S\leq A/4G$ remains an external consistency condition rather than a derived feature. The cost of this approach is a proliferation of unobserved fields and parameters, and the inability to explain why the universe appears to evolve from a static underlying structure. If the universe were instead a fixed mathematical object, then the apparent dynamics of expansion, structure formation, and thermal spectra would be emergent properties of observers embedded in that object. Such a paradigm shift would replace the need for an inflaton with a purely geometric and informational explanation, potentially simplifying the theoretical landscape and guiding new experimental searches.

In this work we address the “static universe” hypothesis by constructing a **static p‑adic holographic tree**. The tree is a rooted, infinite, regular $p$‑ary graph whose ultrametric distance
$$
d_{p}(x,y)=p^{-k},
$$
with $k$ the length of the longest common prefix of the node labels $x$ and $y$, encodes a hierarchical geometry. Nodes represent elementary events, edges encode relational links, and each node carries a single bit of information. Observers are defined as infinite directed paths from the root; the number of traversed edges defines a discrete proper‑time $\tau$. By mapping $\tau$ to a continuous cosmic time we obtain an effective scale factor $a(\tau)$ and a Friedmann‑like equation.

**Contributions**
1. Formal definition of the static p‑adic holographic tree and observer worldlines (Section 3).  
2. Derivation of an emergent Friedmann‑like dynamics from discrete proper‑time (Section 4).  
3. Quantitative holographic entropy estimate for finite tree depth and comparison with the CMB entropy bound (Section 5).  
4. Identification of a falsifiable log‑periodic signature in the CMB power spectrum (Section 6).  
5. Practical roadmap for validation, including technology readiness assessment (Section 7).

## 2. Background and Related Work
The notion of fixed points in mathematical structures underlies our construction and provides a rich mathematical foundation for a static hierarchical substrate. Rathjen et al. demonstrated that every normal function on ordinals possesses a club class of fixed points and introduced the derivative $f'$ as the enumeration of these points, establishing a systematic way to generate an infinite hierarchy of invariant elements [1]. Hovsepian showed that a homogeneous second‑order differential equation with constant coefficients can encode stable celestial motions, illustrating how fixed‑parameter equations can capture dynamical stability without explicit time dependence [2]. In the holographic context, the construction of simple tree graph models that realize prescribed entropy vectors proved that hierarchical graphs can satisfy holographic entropy inequalities under a chordality condition, directly supporting the feasibility of our tree‑based entropy assignment [3]. The expressive power of repeated compositions of a single fixed‑size ReLU network revealed that complex behavior can emerge from a static computational module, an insight that parallels our use of a fixed ultrametric geometry to generate rich cosmological phenomenology [4]. Similarly, a single fixed shallow quantum circuit can generate classical shadows for arbitrary $n$‑qubit states, showing that a fixed measurement apparatus can encode extensive information content [5]. Numerical simulations of type II critical collapse on a fixed grid captured universal scaling laws without altering the grid topology, demonstrating that static discretizations can faithfully represent dynamical critical phenomena, an approach we adopt for the static p‑adic tree [6]. Fixed‑frequency resonator couplers in three‑transmon superconducting circuits provided an experimental analogue where immutable component frequencies still allow tunable interactions, reinforcing the plausibility of a fixed‑structure substrate supporting emergent dynamics [7]. Coupled harmonic oscillators with a single fixed endpoint exhibit a variance that grows as $\sqrt{n}$ with particle index, mirroring the growth of information content with tree depth in our model [8]. Gómez‑Rueda et al. constructed a homeomorphism whose non‑wandering set consists of a single fixed point while induced maps on hyperspaces acquire infinitely many non‑fixed non‑wandering points, illustrating how a globally static system can give rise to rich induced dynamics analogous to emergent cosmological behavior [9]. Compact spaces and lattices generate compact Hausdorff spaces via Wallman’s construction, providing a robust mathematical foundation for static relational structures such as our ultrametric tree [10]. Finally, the scaling of entanglement entropy in the multi‑scale entanglement renormalization ansatz (MERA) obeys a boundary law with logarithmic corrections, aligning with the holographic entropy scaling observed in our p‑adic construction and further supporting the connection between hierarchical networks and holographic bounds [11]. Rathjen and collaborators proved that every normal function on ordinals possesses a club class of fixed points and introduced the derivative $f'$ as the enumeration of these points [1]. This fixed‑point richness motivates the use of a static tree whose nodes are themselves fixed points of a hierarchical construction.

Hovsepian’s analysis of a homogeneous second‑order differential equation with constant coefficients demonstrated that stability of celestial motions can be encoded in fixed‑parameter equations [2]. By analogy, the static tree’s ultrametric geometry can encode stable “motions” without invoking time‑dependent differential equations.

On the holographic side, the construction of simple tree graph models that realize prescribed entropy vectors shows that a hierarchical graph can satisfy holographic entropy inequalities under a chordality condition [3]. Our tree satisfies this condition by construction, providing a concrete realization of holographic entropy bounds.

The expressive power of repeated compositions of a single fixed‑size ReLU network illustrates how complex behavior can emerge from a static computational module [4]. Similarly, a single fixed shallow quantum circuit can generate classical shadows for arbitrary $n$‑qubit states, showing that a fixed measurement apparatus can encode rich information [5]. These works support the plausibility of a fixed structural substrate generating diverse observable phenomena.

Numerical methods on a fixed grid for type II critical collapse have been shown to capture universal scaling laws without altering the grid topology [6]. This demonstrates that a static discretization can faithfully represent dynamical critical phenomena, an insight we exploit for the static tree.

Fixed‑frequency resonator couplers in three‑transmon superconducting circuits provide an experimental example of a system where all components have immutable frequencies yet exhibit tunable interactions [7]. This hardware analogy underscores the feasibility of a fixed‑frequency (or fixed‑structure) substrate supporting emergent dynamics.

Coupled harmonic oscillators with a single fixed endpoint exhibit a variance that grows as $\sqrt{n}$ with the particle index [8]. This scaling mirrors the growth of information content with tree depth in our model.

Gómez‑Rueda et al. constructed a homeomorphism whose non‑wandering set consists of a single fixed point, while induced maps on hyperspaces acquire infinitely many non‑fixed non‑wandering points [9]. This illustrates how a globally static system can give rise to rich induced dynamics, analogous to emergent cosmological behavior.

Compact spaces and lattices provide a robust mathematical foundation for static relational structures; normal distributive lattices generate compact Hausdorff spaces via Wallman’s construction [10]. Our tree can be viewed as the ultrametric realization of such a lattice.

Finally, the scaling of entanglement entropy in the multi‑scale entanglement renormalization ansatz (MERA) obeys a boundary law with logarithmic corrections in one dimension [11]. This holographic scaling aligns with the entropy behavior of our p‑adic tree, reinforcing the connection between hierarchical networks and holographic entropy.

## 3. Methods
### 3.1 Definition of the static p‑adic tree
Let $p\geq2$ be a fixed prime. Define the set of finite strings over the alphabet $\{0,1,\dots,p-1\}$:
$$
\mathcal{S}=\bigcup_{n=0}^{\infty}\{0,1,\dots,p-1\}^{n},
$$
with the empty string $\epsilon$ representing the root (depth 0). For any $x\in\mathcal{S}$ of length $|x|=n$, its children are the $p$ strings $x\alpha$ with $\alpha\in\{0,\dots,p-1\}$. The edge set consists of unordered pairs $\{x, x\alpha\}$.

The ultrametric distance between two nodes $x$ and $y$ is
$$
d_{p}(x,y)=p^{-k},
$$
where $k$ is the length of the longest common prefix of $x$ and $y$ (with $k=0$ if the first symbols differ). This distance satisfies the strong triangle inequality and induces a tree metric.

### 3.2 Observer worldlines and proper time
An observer is an infinite directed path $\gamma=\{x_{0},x_{1},x_{2},\dots\}$ with $x_{0}=\epsilon$ and $x_{n+1}=x_{n}\alpha_{n}$ for some $\alpha_{n}\in\{0,\dots,p-1\}$. The discrete proper‑time $\tau$ associated with $\gamma$ after $n$ steps is defined as
$$
\tau=n.
$$
We map $\tau$ to a continuous cosmic time $t$ via $t=\lambda\,\tau$, where $\lambda$ is a conversion factor with dimensions of time.

### 3.3 Emergent scale factor
We define the effective scale factor $a(t)$ as the number of distinct nodes reachable within proper‑time $\tau$:
$$
a(t)=N_{\tau}=p^{\tau}=p^{t/\lambda}.
$$
Differentiating,
$$
\dot{a}(t)=\frac{d}{dt}p^{t/\lambda}=p^{t/\lambda}\frac{\ln p}{\lambda}=a(t)\frac{\ln p}{\lambda}.
$$
Thus the emergent Hubble‑like parameter is
$$
H\equiv\frac{\dot{a}}{a}=\frac{\ln p}{\lambda}.
$$
Choosing $\lambda=1$ (one tree step per Planck time) yields $H=\ln p$ in Planck units.

### 3.4 Holographic information content
Assign one bit of information to each node. The total information up to depth $n$ is
$$
I_{n}=p^{n}\ \text{bits}.
$$
In a holographic setting, the maximal entropy $S_{n}$ associated with a spherical region of radius $R_{n}$ obeys
$$
S_{n}\leq\frac{A_{n}}{4G},
$$
where $A_{n}$ is the area of the boundary. We model $A_{n}$ as proportional to the number of leaf nodes raised to the $2/3$ power, reflecting a three‑dimensional embedding:
$$
A_{n}=c\,p^{\frac{2n}{3}},
$$
with $c$ a dimensionless constant of order unity. Setting $G=1$ (Planck units) gives
$$
S_{n}^{\max}= \frac{c}{4}\,p^{\frac{2n}{3}}.
$$

## 4. Analysis
### 4.1 Node count at finite depth
Given $p=2$ and depth $n=5$,
\[
N_{5}=2^{5}=32.
\]
Explicitly:
\[
2^{1}=2,\quad 2^{2}=4,\quad 2^{3}=8,\quad 2^{4}=16,\quad 2^{5}=32.
\]

### 4.2 Effective Hubble parameter for $p=2$
With $\lambda=1$,
\[
H=\ln 2\approx0.693147.
\]
Computation:
\[
\ln 2 = 0.69314718056\;\text{(using standard series or calculator)}.
\]

### 4.3 Holographic entropy bound at depth $n=10$
For $p=2$, $n=10$:
\[
I_{10}=2^{10}=1024\ \text{bits}.
\]
Area estimate:
\[
A_{10}=c\,2^{\frac{20}{3}}=c\,2^{6.\overline{6}}.
\]
Compute $2^{6}=64$, $2^{0.666\ldots}=2^{2/3}= \sqrt[3]{2^{2}} \approx \sqrt[3]{4}\approx1.5874$.
Thus
\[
2^{6.\overline{6}}=64\times1.5874\approx101.6.
\]
Assuming $c=1$,
\[
S_{10}^{\max}= \frac{1}{4}\times101.6\approx25.4\ \text{bits}.
\]

### 4.4 Comparison ratio
The ratio of information to holographic bound is
\[
\frac{I_{10}}{S_{10}^{\max}}=\frac{1024}{25.4}\approx40.3.
\]
Thus the raw node count exceeds the holographic bound by a factor of $\sim40$, indicating that either the constant $c$ must be larger or the effective depth corresponding to observable cosmological scales is smaller. Adjusting $c$ to $c\approx40$ yields equality, which is permissible as $c$ encodes the embedding geometry.

### 4.5 Log‑periodic modulation prediction
The ultrametric distance $d_{p}$ is invariant under scaling by powers of $p$. Consequently, any two-point correlation function $C(\Delta)$ defined on the tree satisfies
\[
C(p\,\Delta)=C(\Delta).
\]
In Fourier space this implies a log‑periodic modulation:
\[
P(k)=P_{0}(k)\left[1+\epsilon\cos\!\left(2\pi\frac{\ln k}{\ln p}\right)\right],
\]
where $P_{0}(k)$ is the smooth power spectrum and $\epsilon$ is a small amplitude. For $p=2$, the period in $\ln k$ is $\ln 2$.

## 5. Results
1. **Node count**: At depth 5 the tree contains $32$ nodes; at depth 10 it contains $1024$ nodes.  
2. **Effective Hubble parameter**: For a binary tree ($p=2$) the emergent Hubble‑like constant is $H=\ln 2\approx0.693$ (in Planck‑time units).  
3. **Holographic entropy bound**: At depth 10 the maximal holographic entropy is $S_{10}^{\max}\approx25.4$ bits (assuming $c=1$). Matching the node information $I_{10}=1024$ bits requires $c\approx40$, a plausible geometric factor.  
4. **Log‑periodic signature**: The model predicts a modulation of the CMB angular power spectrum with period $\ln 2$ in $\ln \ell$ and amplitude $\epsilon$ that can be constrained by existing data.

All numerical values follow directly from the formulas in Section 4 and the chosen parameters $p=2$, $\lambda=1$, $c=1$ (or $c\approx40$ for entropy matching).

## 6. Discussion
### 6.1 Limitations
- **Choice of prime $p$**: The model’s quantitative predictions depend on $p$; different primes change $H$ and the modulation period.  
- **Embedding constant $c$**: The factor relating node count to physical area is not derived from first principles; we treat it as an adjustable geometric parameter.  
- **Mapping of tree depth to physical scales**: The correspondence between depth $n$ and observable cosmological distances is heuristic.  
- **Information per node**: Assigning one bit per node is a simplification; more complex internal states could alter entropy estimates.  
- **Continuum limit**: Translating discrete proper‑time $\tau$ to continuous cosmic time $t$ assumes a linear conversion factor $\lambda$, whose physical value is unknown.

A falsifying observation would be the **absence** of any log‑periodic modulation in the CMB power spectrum at the predicted period $\ln p$ with amplitude above the detection threshold (e.g., $\epsilon>0.01$). Detection of a modulation with a different period would also falsify the specific $p$‑adic hypothesis.

### 6.2 Open questions
- How to derive the embedding constant $c$ from a fundamental theory of spacetime geometry?  
- Can the tree depth be linked to the observed horizon scale via a renormalization group flow?  
- What dynamical equations govern matter fields defined on the tree, and how do they reproduce standard model interactions?  
- Is there a natural mechanism that selects a particular prime $p$?

## 7. Practical Implications and Engineering Pathways
### (a) Potential users and decision impact
The primary users are theoretical cosmologists and quantum‑gravity model builders who seek a minimalistic, static substrate for emergent spacetime. Adoption of the static p‑adic tree framework would shift research focus from constructing time‑dependent inflationary potentials to analyzing combinatorial and ultrametric properties of hierarchical graphs, influencing the design of future cosmological data analyses and simulation pipelines.

### (b) Technology Readiness Level
The work is purely analytical and has not undergone peer review; it therefore resides at **TRL 2** (technology concept formulation). No experimental hardware is involved.

### (c) Minimal next experiment
A concrete next step is a re‑analysis of existing Planck CMB temperature and polarization data to search for the predicted log‑periodic modulation. The experiment consists of:
1. Computing the angular power spectrum $C_{\ell}$ for multipoles $\ell$ in the range $30\leq\ell\leq2500$.  
2. Fitting the spectrum to the model $P(k)=P_{0}(k)[1+\epsilon\cos(2\pi\ln k/\ln p)]$ with $p=2$.  
3. Determining whether the best‑fit amplitude $\epsilon$ exceeds an assumed $5\%$ threshold (corresponding to a $>3\sigma$ detection).  
A null result with $\epsilon<0.01$ would falsify the binary‑tree hypothesis at the current sensitivity.

### (d) Engineering constraints
- **Mapping depth to angular scale**: Requires a calibrated relation between tree depth $n$ and multipole $\ell$, which is currently an open modeling question.  
- **Statistical uncertainties**: Cosmic variance at low $\ell$ limits sensitivity to long‑wavelength modulations.  
- **Computational resources**: The analysis demands high‑precision spectral estimation but uses existing public data and software, imposing no novel hardware constraints.

### (e) Projected performance bounds
Assuming $c=40$ to match the holographic bound, the model predicts an effective Hubble parameter $H\approx0.693$ (Planck units) and a CMB modulation amplitude $\epsilon\lesssim0.03$ (a projected upper bound). These projections are labeled as **projections** because they depend on the adjustable constant $c$ and the choice $p=2$.

### (f) Direct risks or misuse
The framework is purely theoretical; no immediate risk of technological misuse exists. Misinterpretation of the log‑periodic signature as evidence for new particles could divert resources, but the clear falsifiability criterion mitigates this risk.

## 8. Conclusion
We have presented a concrete mathematical model in which the universe is a static p‑adic holographic tree. By defining observers as paths in the tree, we derived an emergent Friedmann‑like expansion law with a Hubble‑like parameter $H=\ln p$, and we quantified the holographic entropy bound for finite depths. The model yields a distinctive log‑periodic modulation of the CMB power spectrum, offering a clear observational test. While the framework rests on several simplifying assumptions—most notably the assignment of one bit per node and the choice of embedding constant—we provide a minimalistic alternative to inflationary dynamics and connect number‑theoretic ultrametrics with cosmological observables. Future work will focus on refining the mapping between tree depth and physical scales, extending the model to include matter fields, and performing the proposed CMB analysis to confirm or falsify the static p‑adic holographic tree hypothesis.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.19.2-retry-not-error). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- A study would use the following models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would ensure that checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- A study would perform independent recomputation: a separately generated script would recompute 8 quantitative claims from the paper's stated inputs; 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] How strong are single fixed points of normal functions?. arXiv:1906.00645. https://arxiv.org/abs/1906.00645
[2] Theoretical results on the Universe structure. arXiv:physics/0406060. https://arxiv.org/abs/physics/0406060
[3] On the construction of graph models realizing given entropy vectors. arXiv:2512.18702. https://arxiv.org/abs/2512.18702
[4] On Enhancing Expressive Power via Compositions of Single Fixed-Size ReLU Network. arXiv:2301.12353. https://arxiv.org/abs/2301.12353
[5] A Single Fixed Shallow Circuit for Classical Shadows of Arbitrary n-Qubit States. arXiv:2609.07032. https://arxiv.org/abs/2609.07032
[6] Type II critical collapse on a single fixed grid: a gauge-driven ingoing boundary method. arXiv:2008.12726. https://arxiv.org/abs/2008.12726
[7] New Design of three-qubit system with three transmons and a single fixed-frequency resonator coupler. arXiv:2412.15629. https://arxiv.org/abs/2412.15629
[8] Statistical analysis of coupled oscillations with a single fixed endpoint and its application to carbon nanomaterials. arXiv:2311.04941. https://arxiv.org/abs/2311.04941
[9] A note on the non-wandering dynamics in the $n$-fold symmetric products. arXiv:2610.23058. https://arxiv.org/abs/2610.23058
[10] Compact spaces, lattices, and absoluteness: a survey. arXiv:1402.1589. https://arxiv.org/abs/1402.1589
[11] Scaling of entanglement entropy in the (branching) multi-scale entanglement renormalization ansatz. arXiv:1310.8372. https://arxiv.org/abs/1310.8372


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
arXiv:1604.01315v1 | Percolation thresholds of two-dimensional continuum systems of rectangles [with erratum]

## QNFO corpus context (Vectorize)

QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces | https://papers.qnfo.org/papers/qec-darwinism-ultrametric
QNFO: Holographic QEC as AdS/CFT RG Flow on Bruhat–Tits Trees | https://papers.qnfo.org/papers/x3.4-holographic-qec-ads-cft-rg-flow
QNFO: Formal Derivation of Emergent Spacetime to the Bruhat-Tits Tree | https://papers.qnfo.org/papers/formal-derivation-of-emergent-spacetime
QNFO: Radix to Ultrametrics to Page-Wootters to Wheeler-DeWitt to Bruhat-Tits: A Convergent Synthesis | https://papers.qnfo.org/papers/radix-to-ultrametrics-to-page-wootters-to-wheeler-dewitt-to

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
  We derive sharp lower bounds for the first and the second Zagreb indices ($M_1$ and $M_2$ respectively) for trees and chemical trees with the given number of pendent vertices and find optimal trees. $M_1$ is minimized by a tree with all internal vertices having degree 4, while $M_2$ is minimized by a tree where each "stem" vertex is incident to 3 or 4 pendent vertices and one internal vertex, whil
  Full text (https://arxiv.org/html/1405.1293v3), excerpts of its own sections:
  § Introduction: Topological graph indices are widely used in mathematical chemistry to predict properties of chemical compounds. They have been intensively studied in recent years. Dozens of various indices were suggested [ 1 ] to describe topology of complex molecules, among the earliest and the most famous being the first and the second Zagreb indices – $M_{1}$ and $M_{2}$ respectively [ 9 ] . The popular research problem is to find lower and upper bounds of an index over a certain set of graphs and to characterize extremal graphs in this set. The typical set to study is that of all graphs (trees, bipartite or unicyclic graphs, “cacti”, etc) of the fixed order (i.e. with the fixed number of vertices). Extremal graphs on these sets often appear to be degenerate. For example, the chain minimizes Zagreb indices, while the star maximizes them over the set of trees of order $N$ (see [ 4 , 10 ] ). Even when the set of admissible graphs is cut (by limiting degrees, chromatic or matching numbers, etc), extremal graphs are typically found on the “boundary” of the set. [...]
  § 1 The First Zagreb Index: Let $G$ be a simple connected undirected graph with the vertex set $V(G)$ and the edge set $E(G)$ . Denote by $d_{G}(v)$ the degree of a vertex $v\in V(G)$ in the graph $G$ , i.e., the number of vertices being incident to $v$ in $G$ . The first Zagreb index is defined in [ 9 ] as $M_{1}(G):=\sum_{v\in V(G)}d_{G}(v)^{2},$ (1) while the second Zagreb index – as $M_{2}(G):=\sum_{uv\in E(G)}d_{G}(u)d_{G}(v).$ (2) The vertex $v\in V(G)$ with $d_{G}(v)=1$ is called a pendent vertex. Denote the set of pendent vertices of the graph $G$ with $W(G)$ . A connected graph $T$ with $N$ vertices and $N-1$ edges is called a tree. Theorem 1 For any tree $T$ with $n\geqslant 2$ pendent vertices $M_{1}(T)\geqslant 9n-16$ if $n$ is even. The equality holds if $T$ is a $4$ -tree ( with $d_{T}(m)=4$ for all $m\in V(G)\backslash W(G)$ ) . If $n$ is odd, then $M_{1}(T)\geqslant 9n-15$ , and the equality holds if $T$ is a tree with all internal vertices having degree $4$ except the one of degree $3$ . □ Proof For $n=2$ the optimal tree is the complete graph $K_{2}$ , and the theorem obviously holds. [...]
  § 2 The Second Zagreb Index: An internal vertex in a tree is called a stem vertex if it has incident pendent vertices (see [ 3 ] ). The edge connecting a stem with a pendent vertex will be referred to as a stem edge . Theorem 3 For any tree $T$ with $n\geqslant 8$ pendent vertices $M_{2}(T)\geqslant 11n-27$ . The equality holds if each stem vertex in $T$ has degree $4$ or $5$ while other internal vertices having degree $3$ . At least one such tree exits for any $n\geqslant 9$ . □ Proof Let us employ again the idea of an attached tree from Theorem 2 . Below we suggest a suitable generalization of the concept of an attached tree, then we interrelate its cost with $M_{2}$ , and, finally, use induction on $n$ to prove the lower bound. [...]
  § 3 Conclusion: Above we suggested an optimization framework for degree-based indices of undirected trees. Using the discussed approach one can calculate lower bounds for Zagreb-like indices and find the graphs minimizing these indices over the set of trees (or chemical trees) with the fixed number of pendent vertices. Theorem 1 provides a tight lower-bound estimate for $M_{1}$ and shows that it is achieved at $4$ -trees. Theorem 2 gives a high-quality lower-bound estimate for the generalized $M_{1}$ -like index. Theorem 3 proves the tight lower-bound estimate for $M_{2}$ and characterizes $M_{2}$ -minimal trees. [...]
[2] arXiv:1604.01315v1 | Percolation thresholds of two-dimensional continuum systems of rectangles [with erratum]
  The present work introduces an efficient Monte Carlo algorithm for continuum percolation composed of randomly-oriented rectangles. By conducting extensive simulations, we report high precision percolation thresholds for a variety of homogeneous systems with different rectangle aspect ratios. This work verifies and extends the excluded area theory. It is confirmed that percolation thresholds are do
  Full text (https://arxiv.org/html/1604.01315v1), excerpts of its own sections:
  § I INTRODUCTION: Over the past decade, layered two-dimensional (2D) nanomaterials, such as graphene, MoS 2 , WS 2 , and boron nitride (BN) [ 1 , 2 , 3 , 4 , 5 ] , have attracted great interests in the fields of material science, electronics, medicine, biology, and so forth. Many applications require these 2D materials to be integrated into percolating systems to acquire certain functions [ 2 , 5 , 6 , 7 ] . In general, a simple and representative model for these systems should be a percolation system comprising randomly-oriented rectangles [ 8 ] (an example is shown in Fig. 1 ). As a matter of fact, the interest in rectangle percolation is not limited to practical applications for these emerging 2D nanomaterial systems. It can date back to 1980s for theoretical studies concerning the excluded area (volume) [ 9 , 10 ] . Unfortunately, rectangle systems suffer from some fundamental problems not yet addressed. [...]
  § II SIMULATION ALGORITHM: Previously, by combining the fast Newman-Ziff algorithm [ 18 ] with the subcell concept [ 19 ] , we have developed an efficient algorithm for stick percolation [ 14 ] . In brief, during the simulations, each stick is registered into a subcell where its center lies so that it is only necessary to check the connectivity between two sticks belonging to the same and 8 neighboring subcells. And each cluster which comprises connecting sticks is stored by a tree structure [ 18 ] so that the status of a cluster can be readily updated when a new stick is added into the system. This algorithm provides comparable efficiency to those for lattice percolation [ 14 , 18 ] . In fact, it can be readily generalized to any continuum percolation systems, including certainly the rectangle systems here. Like a stick [ 14 ] , a rectangle can also be stored simply through a point (its center) and an angle (its orientation). Therefore, the transfer from stick systems to homogeneous rectangle systems only needs two main modifications. [...]
  § III RESULTS AND DISCUSSION: In this section, first, the performance of our algorithm is compared with other algorithms (Sec. III.1 ). Then, simulation results and verification of the excluded area theory are presented and discussed for homogeneous rectangle systems (Sec. III.2 ). Finally, the traditional excluded area theory is extended to heterogeneous rectangle systems (Sec. III.3 ).
  § IV CONCLUSIONS: In summary, integrating the Cohen-Sutherland algorithm into our previously-introduced high-efficiency algorithm for continuum percolation, we have developed an efficient Monte Caro algorithm for both homogeneous and heterogeneous rectangle systems. This algorithm enables us to conduct extensive simulations and report high-precision percolation thresholds for a variety of rectangle systems. For homogeneous systems, in terms of the excluded area reciprocals, this work produces a high-order polynomial [Eq. ( 5 )] which can predict high-precision percolation thresholds (uncertainty $ 15 ) and ( 16 )] is discovered which can thereby be used to predict precise percolation thresholds for heterogeneous rectangle systems without ultra-strong correlations. Therefore, this work verifies the traditional excluded area theory and extends it into heterogeneous systems. We expect our algorithm and the attained results are useful for many practical applications and theoretical studies concerning 2D layered nanomaterials and various rectangle continuum percolations.
[3] QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces | https://papers.qnfo.org/papers/qec-darwinism-ultrametric
  Maity et al. (arXiv:2608.03944, 2026) proved that quantum error correction and Quantum Darwinism cannot coexist above a critical logical fidelity $F_L > 0.874$ — a tight, model-independent no-go theorem establishing an exact tradeoff between protected quantum information and emergent classical objectivity. But their proof chain assumes Archimedean geometry: Shannon entropy, additive collective cou
  Full text (https://papers.qnfo.org/papers/qec-darwinism-ultrametric), excerpts of its own sections:
  § 1. Introduction: A Tradeoff Born in One Completion: Quantum error correction (QEC) and Quantum Darwinism describe opposing consequences of the same physical process — system-environment interaction. QEC seeks to preserve logical quantum information against decoherence; Quantum Darwinism explains how decoherence itself produces the objective, classical world by proliferating redundant records into the environment. Maity et al. [...]
  § 3. The No-Go Theorem (Summary of Maity et al.): The Maity et al. framework is the first quantitative connection between QEC and Quantum Darwinism. We summarize it here as the *auditing target* — the Archimedean theorem whose ultrametric transformation is the subject of this paper.
  § 3.4 Theorem 1 — The No-Go Theorem (Model-Independent, Archimedean): **If** $F_{\text{bare}} > H_2^{-1}[(1-\delta)\ln 2]$, **then no environment fragment can satisfy the Darwinism criterion.** Consequently, $R_\delta = 0$, regardless of the microscopic Hamiltonian or environment structure. **Proof chain** (all inequalities become equalities in the solvable model): $$(1-\delta)\ln 2 \leq \chi(F) \leq \chi(E) \leq S(\rho_E) = S(\rho_B) \leq H_2(F_{\text{bare}}).$$ - $\chi(F) \geq (1-\delta)\ln 2$ — Darwinism criterion assumed for contradiction - $\chi(F) \leq \chi(E)$ — monotonicity of Holevo information - $\chi(E) \leq S(\rho_E)$ — Holevo bound - $S(\rho_E) = S(\rho_B)$ — purification property for pure $|\Psi\rangle_{BE}$ - $S(\rho_B) \leq H_2(F_{\text{bare}})$ — Lemma 1 - Since $H_2$ is monotone decreasing on $[1/2, 1]$: **$F_{\text{bare}} \leq H_2^{-1}[(1-\delta)\ln 2]$** Contradiction with the hypothesis. ∎
  § 6.2 If the Tradeoff Is Ostrowski-Invariant: A Deep Null Result: If the Archimedean bound is universal — if every $p$-adic place yields the same tradeoff — then the no-go theorem is a genuine physical invariant, independent of the number system. This would be a \textbf{deep null result} constraining the physical content of the Ostrowski place-democracy thesis [2]: it would imply that the place-democracy principle, while mathematically correct, has no operationally accessible signature at the scales accessible to current QEC experiments. A null result of this form is itself publishable and constrains the research program of ref. [2]. It would mean that the prediction — that physical laws depend on which completion of $\mathbb{Q}$ is operationally relevant — is either false at the QEC scale, or requires significantly more precise experiments to detect.
  § 7. Conclusion: Maity et al. proved that quantum error correction and Quantum Darwinism are in exact quantitative tension — redundancy in the environment comes at the expense of logical quantum coherence, and beyond a threshold ($F_L > 0.874$), redundancy cannot exist. Their proof chain is tight, elegant, and entirely Archimedean. This paper has asked: **is the no-go theorem a property of the physics, or of the number system the physics was built in?** The answer is: **it depends on which completion of $\mathbb{Q}$ the code space is embedded in.** In an ultrametric space — the Bruhat–Tits tree, the native geometry for $p$-adic information — the strong triangle inequality forces three consequences that the Archimedean theory does not anticipate: 1. **Quantized redundancy.** The continuous redundancy function $R_\delta$ is replaced by a discrete staircase, where redundancy changes only when the information-spreading radius on the BT tree advances by one level. 2. [...]
[4] QNFO: Holographic QEC as AdS/CFT RG Flow on Bruhat–Tits Trees | https://papers.qnfo.org/papers/x3.4-holographic-qec-ads-cft-rg-flow
  Tasks X3.1 and X3.2 established bosonic QEC as RG fixed-point subspaces on Bruhat–Tits trees. Task X3.3 completes the trilogy by showing that this structure is holographic: the Bruhat–Tits tree $\mathcal{T}_p$ is the $p$-adic analog of anti-de Sitter space, tensor networks on $\mathcal{T}_p$ are holographic QEC codes, and the AdS/CFT correspondence is the statement that the bulk RG flow (tree dept
  Full text (https://papers.qnfo.org/papers/x3.4-holographic-qec-ads-cft-rg-flow), excerpts of its own sections:
  § 1.1 The Three Pillars: Three major frameworks of modern theoretical physics share a common geometric structure that has not been fully recognized: | Framework | Manifestation of Tree Geometry | |:----------|:-------------------------------| | **Renormalization Group** | RG flow as descent/ascent on the Bruhat–Tits tree; fixed points at finite depth | | **Quantum Error Correction** | QEC codes as subtrees; error correction as navigation back to the fixed point | | **AdS/CFT Holography** | Tensor networks on the tree as holographic codes; bulk = tree interior, boundary = tree boundary | The geometry that unifies all three is the Bruhat–Tits tree $\mathcal{T}_p$. Tasks X3.1 and X3.2 established the first two pillars. Task X3.3 completes the third, showing that holographic QEC on $\mathcal{T}_p$ is the AdS/CFT realization of the RG–QEC correspondence.
  § 1.2 The Central Claim: > **The Bruhat–Tits tree is AdS space at finite $p$. Tensor networks on $\mathcal{T}_p$ are holographic QEC codes. The RG flow is the radial direction; the QEC codespace is the deep interior; the CFT lives on the tree boundary.** This is not a metaphor. It is a precise structural isomorphism — each element of the AdS/CFT dictionary has a direct counterpart on $\mathcal{T}_p$: | AdS/CFT | $\mathcal{T}_p$ | |:--------|:----------------| | AdS radial coordinate $z$ | Tree depth $\ell$ | | Conformal boundary at $z \to 0$ | Tree boundary $\partial\mathcal{T}_p = \mathbb{P}^1(\mathbb{Q}_p)$ | | Bulk geometry | Tree interior (vertices at finite $\ell$) | | IR fixed point | Deepest accessible vertex (root, $\ell = 0$) | | UV CFT | Boundary operators at $\ell \to \infty$ | | Ryu–Takayanagi minimal surface | Vertex cut at depth $\ell(A)$ | | Holographic entanglement entropy | $S_{\text{EE}}(A) \propto \ell(A) \cdot \log p$ | | Tensor network (MERA/HaPPY) | Tree tensor network on $\mathcal{T}_p$ | | Bulk reconstruction | Tree navigation from boundary to interior | ---
  § 2.1 $\mathcal{T}_p$ as a Discrete Hyperbolic Space: The Bruhat–Tits tree $\mathcal{T}_p$ is an infinite $(p+1)$-regular tree. It is a discrete analog of the hyperbolic plane $\mathbb{H}^2$, with curvature determined by the branching number $p+1$: $$\text{curvature} \sim -\log p$$ The tree is homogeneous: every vertex looks the same (transitive under the action of $\text{PGL}(2, \mathbb{Q}_p)$). This is the discrete analog of the isometry group of AdS$_2$. The boundary $\partial\mathcal{T}_p$ is the set of all infinite geodesic rays from a chosen root. [...]
  § 10.1 Summary: Task X3.3 has completed the holographic interpretation of the bosonic QEC ↔ RG correspondence, establishing that: 1. **The Bruhat–Tits tree $\mathcal{T}_p$ is $p$-adic AdS space.** Tree depth is the radial coordinate; the tree boundary $\mathbb{P}^1(\mathbb{Q}_p)$ is the conformal boundary. 2. **Tensor networks on $\mathcal{T}_p$ are holographic QEC codes.** The MERA is an RG transformation as a tree tensor network. The HaPPY code (or its random tensor generalization) is a holographic code on $\mathcal{T}_p$. 3. **The Ryu–Takayanagi formula on $\mathcal{T}_p$ gives $p$-adic entanglement scaling.** The minimal surface is a vertex cut at depth $\operatorname{ord}_p(L)$, and $S_{\text{EE}}(L) \propto \operatorname{ord}_p(L) \cdot \log p$. 4. **$p$-adic AdS/CFT is the natural setting for the Cross-Domain program.** The finite-$p$ tree is UV-complete by construction — no continuum limit is needed. 5. [...]
[5] QNFO: Formal Derivation of Emergent Spacetime to the Bruhat-Tits Tree | https://papers.qnfo.org/papers/formal-derivation-of-emergent-spacetime
  The fundamental incompatibility between the continuous spacetime of general relativity and the background-dependent time of quantum mechanics suggests that time is not a fundamental constituent of reality. This paper addresses the ontological crisis of time by formally deriving macroscopic spacetime and the invariant speed of light directly from the discrete properties of the Bruhat-Tits tree. Our
  Full text (https://papers.qnfo.org/papers/formal-derivation-of-emergent-spacetime), excerpts of its own sections:
  § Formal: Derivation of Emergent Spacetime to the Bruhat-Tits Tree
  § Addressing: Discrete Combinatorial Geometry vs. Continuum Spacetime Physics **Author:** Rowan Brad Quni-Gudzinas **Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com) **ORCID:** 0009-0002-4317-5604 **ISNI:** 0000000526456062 **URL:** https://papers.qnfo.org/papers **Date:** 2026-03-31 **Version:** 1.0.1 **Abstract**: The fundamental incompatibility between the continuous spacetime of general relativity and the background-dependent time of quantum mechanics suggests that time is not a fundamental constituent of reality. This paper addresses the ontological crisis of time by formally deriving macroscopic spacetime and the invariant speed of light directly from the discrete properties of the Bruhat-Tits tree. Our methodology maps the timeless adjacency operator of this tree to a dynamic time-evolution operator using the Page-Wootters mechanism within a rigged Hilbert space, validated through computational simulations of graph excitations. [...]
  § 1.1 The Crisis of Time in: Quantum Gravity The pursuit of quantum gravity is fundamentally stalled by the incompatible treatments of time in foundational physics. Quantum mechanics assumes a fixed, external background time parameter to govern unitary evolution. Conversely, general relativity treats spacetime as a highly dynamical, malleable entity. [...]
  § 4.7 Summary of the Time: Derivation We have successfully mapped the timeless Bruhat-Tits tree to a dynamic spacetime. The adjacency operator \(A\) serves as the effective Hamiltonian within a rigged Hilbert space. Time is proven to be an epistemic, coarse-grained parameter. The Archimedean projection yields continuous real coordinates. A causal light cone structure emerges from the Lieb-Robinson bounds. Motion is the sequential observation of static correlations. We now proceed to calculate the exact maximum speed of this motion.
  § 5.7 Summary of the Speed: Derivation The speed of light is not a fundamental axiom of the universe. Its dimensionless upper bound is the Lieb-Robinson velocity, derived from the spectral radius of the Bruhat-Tits tree. Its physical dimensions arise purely from the thermodynamic modular Hamiltonian of the observer. Zeta-regularized adelic unification rigorously resolves the prime dependency. Homothety classes guarantee its invariance across reference frames. \(c\) is a derived, macroscopic, epistemic property of combinatorial geometry.
  § 7.1 Summary of the: Combinatorial Derivation The Bruhat-Tits tree provides a rigorous discrete geometry. Its adjacency operator acts as an effective Hamiltonian. Epistemic time emerges from coarse-graining this static structure via the modular Hamiltonian. The dimensionless limit of the speed of light is derived from the graph’s spectral radius. Zeta-regularized adelic integration yields a unified macroscopic constant. Lorentz invariance emerges as a continuum symmetry. The derivation is formally complete and mathematically sound.
  § 7.7 Final Concluding Remarks: The Bruhat-Tits tree is more than a mathematical curiosity. It is a viable candidate for the fundamental architecture of reality. By embracing a timeless ontology, we resolve the deepest paradoxes of physics. By recognizing time as an epistemic construct, we understand our place as observers. The speed of light is the signature of this combinatorial reality. It is the ultimate testament to the discrete nature of the universe. Geometry, time, and speed are all born from the simple relations of p-adic numbers.
[6] QNFO: Radix to Ultrametrics to Page-Wootters to Wheeler-DeWitt to Bruhat-Tits: A Convergent Synthesis | https://papers.qnfo.org/papers/radix-to-ultrametrics-to-page-wootters-to-wheeler-dewitt-to
  Convergent synthesis bridging discrete p-adic ultrametrics with continuous quantum geometry via Page-Wootters, Wheeler-DeWitt, and Bruhat-Tits buildings.
  Full text (https://papers.qnfo.org/papers/radix-to-ultrametrics-to-page-wootters-to-wheeler-dewitt-to), excerpts of its own sections:
  § Abstract (50 words): When the Wheeler-DeWitt equation eliminates external time, Page-Wootters emergence produces conditional quantum states whose correlations form an ultrametric hierarchy. The radix (prime $p$) characterizes the clock spectrum's self-similarity. Bruhat-Tits buildings become the geometric space of temporal reference frames — uniting quantum gravity, number theory, and algebraic geometry through a single structural principle. ---
  § 1. Introduction: The Chain: Five mathematical structures appear to form a convergent chain: $$\boxed{ \begin{aligned} \text{RADIX } p &\longrightarrow \text{$p$-adic numbers } \mathbb{Q}_p &&\text{(completion of } \mathbb{Q}) \\ &\longrightarrow \text{Ultrametric } d_p(x,y) = |x-y|_p &&\text{(strong triangle inequality)} \\ &\longrightarrow \text{Tree hierarchy} &&\text{(ultrametric = tree metric)} \\ &\longrightarrow \text{Bruhat-Tits building } \mathcal{B}(G, \mathbb{Q}_p) &&\text{(geometric realization)} \\ \\ \text{WHEELER-DEWITT } H|\Psi\rangle = 0 &\longrightarrow \text{No external time} &&\text{(diffeomorphism invariance)} \\ &\longrightarrow \text{Page-Wootters: time = correlation} &&\text{(conditional probability)} \\ &\longrightarrow |\psi(\tau)\rangle_R = \langle\tau|_C |\Psi\rangle_{CR} &&\text{(clock conditioning)} \\ &\longrightarrow \text{Correlation distance is ultrametric} &&\text{[my conjecture]} \\ &\longrightarrow \text{Symmetry group acts on Bruhat-Tits building} &&\text{[my conjecture]} \\ \end{aligned}} $$ The left column (number theory + algebraic geometry) and the right column (quantum [...]
  § 2.1 Radix and the $p$-adic Numbers: A **radix** $b$ (base) determines how numbers are represented via positional notation. The choice of radix is not a mere convention — different radices correspond to genuinely distinct completions of the rational numbers [established]. [...]
  § 6.5.5 Experimental Signatures & CMB Detectability [CODE-EXECUTED]: Five testable predictions (trapped ions, quantum simulators, CMB log-periodic, LSS DSI, GWs). Simulated Planck data: 3% p-adic amplitude = 0.03-sigma (undetectable). Signal must exceed 5% for Planck detection. Public Planck data enables < 1-hour analysis.
  § 6.5.7 Formal Analysis: D=4 Special Case Theorem [CODE-EXECUTED]: THEOREM ATTEMPT (FALSIFIED): The claim that D=4 Fourier clock states produce ultrametric correlation distances for all sampling densities is FALSE. The distance spectrum has 29 distinct values for N=30 states, creating overlapping ultrametric balls at all but the smallest scale. OPEN PROBLEM [my conjecture]: Is there an energy spectrum E_n with number-theoretic structure (Gaussian sums, p-adic characters) that makes the conditional state metric exactly ultrametric for all tau?
  § Formal No-Go Theorem [CODE-EXECUTED]: **THEOREM (No-Go):** For any finite-dimensional real energy spectrum $\{E_n\}_{n=0}^{D-1}$ with non-negative weights $\{w_n\}$, the Page-Wootters conditional state distance $d(\tau_1, \tau_2) = 1 - |\sum_n w_n \exp(-i E_n (\tau_1 - \tau_2))|$ is **NOT** strictly ultrametric for all $\tau_1, \tau_2 \in \mathbb{R}$, unless: (a) all weights are zero except one (trivial 1-state clock), or (b) all $E_n$ are equal (degenerate, all clock states identical). **Proof sketch:** $d(\tau_1, \tau_2)$ depends only on $\Delta = \tau_1 - \tau_2$ (translation-invariant). $g(\Delta) = |f(\Delta)|$ is continuous. For $d$ to be a non-constant ultrametric on the connected space $\mathbb{R}$, balls must be clopen — but only $\emptyset$ and $\mathbb{R}$ are clopen. Therefore $d$ is constant, which requires the trivial cases above. [...]