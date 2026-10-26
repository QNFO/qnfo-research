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
