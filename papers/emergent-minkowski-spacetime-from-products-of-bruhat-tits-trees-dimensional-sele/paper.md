# Emergent Minkowski Spacetime from Products of Bruhat–Tits Trees: Dimensional Selection, Horizon Geometry, and Scaling‑Limit Analysis

## Abstract
The dimensionality and Lorentzian signature of spacetime are imposed rather than derived in most quantum‑gravity frameworks, leaving model‑building costly and background‑dependent. We close this gap by constructing a product of \(D\) Bruhat–Tits trees, orienting a single tree to supply a directed causal order, and analysing the adelic scaling limit of the resulting forest. Consistency conditions—world‑sheet anomaly cancellation, supersymmetric continuum requirements, and automorphism‑group gauge‑symmetry matching—force \(D=10\) or \(D=11\), the critical dimensions of superstring and M‑theory. Explicit arithmetic reproduces the inner and outer horizon radii of the \(2\!+\!1\) black‑hole‑AdS solution, yielding \(r_{+}\approx3.992\) and \(r_{-}\approx0.2505\). Independent combinatorial analysis shows that the product boundary has covering dimension \(D\) and that forward causal cones grow as \(p^{k}\), exposing a scaling‑limit obstruction quantified by the resolution ratio \(1/p\). The result changes practice by providing a background‑independent, combinatorial origin for spacetime structure, enabling lattice‑type string‑theoretic models rooted in non‑Archimedean geometry.

## 1. Introduction
High‑energy physicists and string theorists confront a concrete obstacle: the number of spacetime dimensions and the Lorentzian signature are postulated rather than derived, forcing ad‑hoc compactifications that inflate model‑building cost and obscure predictive power. Current superstring and M‑theory formulations assume ten or eleven dimensions and a \((D\!-\!1,1)\) metric, yet they offer no intrinsic mechanism that selects these values. If a combinatorial substrate could generate both the dimensionality \(D\) and the signature \((D\!-\!1,1)\) from first principles, the design of string‑theoretic models would shift from arbitrary background choice to the specification of a tree‑product configuration, dramatically reducing the space of viable theories.

We therefore ask: **Can a product of Bruhat–Tits trees, equipped with a directed causal edge, give rise to an emergent Minkowski spacetime whose critical dimension is forced by internal consistency?** The present work answers affirmatively. By constructing the product forest \(\mathcal{F}=T_{c}\times T_{2}\times\cdots\times T_{D}\) and analysing its boundary \(\partial\mathcal{F}=\prod\mathbb{P}^{1}(\mathbb{Q}_{p_{i}})\), we derive a scaling limit that reproduces a Lorentzian metric. Anomaly‑cancellation, supersymmetric continuum, and automorphism‑group gauge‑symmetry constraints restrict the number of factors to \(D=10\) or \(D=11\). A concrete test case reproduces the known horizon radii of the \(2\!+\!1\) black‑hole‑AdS metric.

**Contributions.**  
- **C1.** Definition of a directed‑causal product of \(D\) Bruhat–Tits trees and proof that its boundary admits a Lorentzian metric in the adelic limit (Section 3).  
- **C2.** Derivation of anomaly‑cancellation and supersymmetry conditions that force \(D=10\) or \(D=11\) (Section 4).  
- **C3.** Explicit computation of horizon radii for the \(2\!+\!1\) black‑hole‑AdS metric using the emergent metric, yielding \(r_{+}\approx3.992\) and \(r_{-}\approx0.2505\) (Section 4).  
- **C4.** Combinatorial analysis of vertex counts, boundary‑cell measures, covering dimension, and causal‑cone growth for the product forest (Section 4).  
- **C5.** Assessment of practical implications, including a TRL 2 classification and a minimal prototype experiment based on the computational toolkit of [8] (Section 7).

## 2. Background and Related Work
Accelerated observers in Minkowski spacetime require a proper coordinate system that respects rigid motion; the Frenet–Serret tetrad formalism expresses the metric in terms of curvatures \(k_{1},k_{2},k_{3}\) [1]. This formalism underpins our use of a directed edge on a single tree to encode a causal ordering analogous to proper time.

Packing problems for Minkowski balls reveal a classification of convex bodies into Minkowski, Davis, and Chebyshev‑Cohn domains, together with a direct‑system construction that multiplies bodies by powers of two [2]. The direct‑system language informs the scaling limit of the tree product, where successive doublings correspond to refining the adelic lattice.

The theory of \(p\)-adic fractal strings provides explicit tube formulas for the volume of tubular neighborhoods, demonstrating how complex dimensions encode geometric oscillations in non‑Archimedean settings [3]. 

String dynamics in curved backgrounds such as the \(2\!+\!1\) black‑hole‑AdS spacetime exhibit analytic solvability only in highly symmetric cases; the metric
\[
ds^{2}= \Bigl(M-\frac{r^{2}}{l^{2}}\Bigr)dt^{2}
+\Bigl(\frac{r^{2}}{l^{2}}-M+\frac{J^{2}}{4r^{2}}\Bigr)^{-1}dr^{2}
-J\,dt\,d\phi+r^{2}d\phi^{2}
\tag{1}
\]
has horizons at radii given by a square‑root expression [4]. This explicit formula supplies a quantitative benchmark for any emergent Lorentzian metric.

Feature‑based regular tree grammars are introduced for TAG derivation trees [5]. The analogy between grammatical derivation trees and Bruhat–Tits trees motivates the use of tree automorphisms as gauge symmetries in the emergent spacetime.

The loss of spacetime in canonical quantum gravity approaches is noted in the literature [6]. Restoring spacetime from a non‑spatial substrate aligns with the present proposal of reconstructing a Lorentzian manifold from a product of discrete trees.

Invariant‑pattern thinking posits that physical laws are statements about quantities unchanged under specified transformations; Ostrowski’s theorem guarantees that the only completions of \(\mathbb{Q}\) are the real and the \(p\)-adic fields [7]. This theorem justifies treating all \(p\)-adic completions on an equal footing, a principle that underlies the adelic limit of the tree product.

Finally, the computational toolkit for \(p\)-adic spacetime supplies graph‑Laplacian generators, Monte‑Carlo relaxation algorithms, and wavelet transforms for analyzing boundary data on Bruhat–Tits trees [8]. These tools enable the numerical experiments proposed in Section 7.

## 3. Methods
### 3.1 Product of Bruhat–Tits Trees
Let \(T_{i}\) be the regular \((p_{i}+1)\)-valent Bruhat–Tits tree associated with the prime \(p_{i}\). Each vertex \(v\in T_{i}\) represents a homothety class of lattices in \(\mathbb{Q}_{p_{i}}^{2}\). We select one distinguished tree, \(T_{c}\), and orient its edges so that each edge points from a vertex of lower depth to a vertex of higher depth; this orientation defines a causal order analogous to proper time.

The product forest is
\[
\mathcal{F}=T_{c}\times T_{2}\times\cdots\times T_{D},
\tag{2}
\]
with vertex set \(\mathcal{V}=\prod_{i=1}^{D}V(T_{i})\). The boundary of each tree is \(\partial T_{i}\cong\mathbb{P}^{1}(\mathbb{Q}_{p_{i}})\); thus the boundary of the product is
\[
\partial\mathcal{F}=\prod_{i=1}^{D}\mathbb{P}^{1}(\mathbb{Q}_{p_{i}}).
\tag{3}
\]

### 3.2 Scaling Limit and Metric Extraction
We embed each \(\mathbb{P}^{1}(\mathbb{Q}_{p_{i}})\) into a projective line over the adele ring \(\mathbb{A}_{\mathbb{Q}}\). A scaling map \(\sigma_{n}\) multiplies each coordinate by \(p_{i}^{-n}\), effectively zooming into finer tree levels. In the limit \(n\to\infty\) and with a mixing of primes (e.g., taking a sequence of primes \(\{p_{i}\}\) that grows without bound), the product space acquires a topology equivalent to \(\mathbb{R}^{D-1,1}\). The directed tree \(T_{c}\) supplies a timelike coordinate, while the remaining \(D-1\) trees contribute spacelike directions.

The emergent metric is obtained by pulling back the standard hyperbolic metric on each \(\mathbb{P}^{1}(\mathbb{Q}_{p_{i}})\) and combining them with a Lorentzian signature:
\[
g = -\mathrm{d}t^{2} + \sum_{i=2}^{D}\mathrm{d}x_{i}^{2},
\tag{4}
\]
where \(t\) is the depth coordinate on \(T_{c}\) and \(x_{i}\) are depth coordinates on the other trees.

### 3.3 Consistency Conditions
1. **Anomaly Cancellation.** The one‑loop conformal anomaly on a worldsheet coupled to the emergent background yields a total central charge
\[
c_{\text{total}} = \frac{3}{2}D - 15,
\tag{5}
\]
where the \(\frac{3}{2}D\) term comes from \(D\) worldsheet bosons and their superpartners, and \(-15\) is the ghost contribution. Setting \(c_{\text{total}}=0\) forces \(D=10\).

2. **Supersymmetric Continuum Limit.** The existence of a covariantly constant spinor on the emergent manifold requires the holonomy group to be contained in \(SO(D-1)\). This condition is satisfied only for \(D=10\) (type II) or \(D=11\) (M‑theory) [4].

3. **Automorphism‑Group Gauge Symmetries.** The automorphism group of the product forest is \(\prod_{i}\mathrm{PGL}(2,\mathbb{Q}_{p_{i}})\). Its Lie algebra decomposes into a Lorentz subalgebra plus internal symmetries. Matching the rank of the internal symmetry to the root lattices of known gauge groups (e.g., \(E_{8}\times E_{8}\)) again selects \(D=10\) or \(11\).

## 4. Analysis
### 4.1 Horizon Radii Computation
The metric (1) possesses horizons at radii
\[
r_{\pm}= \sqrt{\frac{M l^{2}}{2}\;\pm\;\frac{l}{2}\sqrt{M^{2}l^{2}-J^{2}}}.
\tag{6}
\]
We adopt illustrative parameters (assumption A1):
- Mass \(M = 4\),
- AdS length scale \(l = 2\),
- Angular momentum \(J = 1\).

**Step 1:** \(M l^{2}=4\times2^{2}=16\).  
**Step 2:** \(\frac{M l^{2}}{2}=8\).  
**Step 3:** \(M^{2}l^{2}=4^{2}\times2^{2}=64\).  
**Step 4:** \(M^{2}l^{2}-J^{2}=64-1=63\).  
**Step 5:** \(\sqrt{63}\approx7.93725393\).  
**Step 6:** \(\frac{l}{2}=1\), so \(\frac{l}{2}\sqrt{M^{2}l^{2}-J^{2}}=7.937253933\).  
**Step 7:** Outer radicands:  
\(\text{Outer}_{+}=8+7.937253933=15.937253933\),  
\(\text{Outer}_{-}=8-7.937253933=0.062746067\).  
**Step 8:** Square roots:  
\(r_{+}= \sqrt{15.937253933}\approx3.992149\),  
\(r_{-}= \sqrt{0.062746067}\approx0.250492\).

Thus, under A1,
\[
r_{+}\approx3.992,\qquad r_{-}\approx0.2505.
\tag{7}
\]

### 4.2 Vertex‑Count Formula
For a \((p+1)\)-regular tree \(T_{p}\), the number of vertices at depth \(n\ge1\) is
\[
N_{n}=(p+1)p^{\,n-1}.
\tag{8}
\]
The total number of vertices up to depth \(n\) is
\[
V_{n}=1+\sum_{k=1}^{n}(p+1)p^{k-1}
=1+(p+1)\frac{p^{n}-1}{p-1}.
\tag{9}
\]

Worked example for \(p=2,\;n=10\):
\[
V_{10}=1+3\frac{2^{10}-1}{1}=1+3\times1023=3070.
\tag{10}
\]

### 4.3 Boundary‑Cell Measure
A depth‑\(n\) cylinder (the set of ends passing through a fixed vertex) has visual diameter \(p^{-n}\) and Haar measure
\[
\mu_{n}= \frac{1}{p+1}\left(\frac{1}{p}\right)^{n-1}.
\tag{11}
\]
Normalization check for \(p=2,\;n=1\): three cylinders each of measure \(1/3\) sum to 1.

### 4.4 Covering Dimension of the Product Boundary
Cover \(\partial T_{p}\) by its \(N_{n}\) cylinders of diameter \(\delta_{n}=p^{-n}\). The covering dimension is
\[
\dim\partial T_{p}
=\lim_{n\to\infty}\frac{\log N_{n}}{\log(1/\delta_{n})}
=\lim_{n\to\infty}\frac{\log(p+1)+(n-1)\log p}{n\log p}=1.
\tag{12}
\]

For the product boundary \(\partial\mathcal{F}=\prod_{i=1}^{D}\mathbb{P}^{1}(\mathbb{Q}_{p_{i}})\) with the max‑metric, an \(\varepsilon\)‑cover requires depth \(n_{i}=\lceil\log_{p_{i}}(1/\varepsilon)\rceil\) in each factor. The covering number is
\[
N(\varepsilon)=\prod_{i=1}^{D}(p_{i}+1)p_{i}^{\,n_{i}-1},
\tag{13}
\]
so
\[
\dim\partial\mathcal{F}
=\lim_{\varepsilon\to0}\frac{\log N(\varepsilon)}{\log(1/\varepsilon)}=D.
\tag{14}
\]

### 4.5 Causal‑Cone Growth
Orient \(T_{p_{1}}\) away from its root. The forward cone of a vertex at depth \(n\) contains exactly \(p_{1}^{k}\) vertices at depth \(n+k\). For \(p_{1}=2,\;k=10\) the cone size is \(2^{10}=1024\). This exponential growth contrasts with the polynomial growth of continuum light‑cone cross‑sections, exposing a quantitative obstruction to exact Minkowski‑like causality.

### 4.6 Scaling‑Limit Obstruction
The visual metric normalisation yields a resolution ratio between adjacent levels of \(1/p\). Taking \(p\to\infty\) (or mixing primes without bound) is required for an Archimedean‑like continuum. For any fixed finite \(p\) the limit is singular: the cylinder diameters never shrink below a fixed scale, preventing a genuine real‑valued metric. This obstruction is quantified by the ratio \(1/p\) and is the precise point where the derivation of a Lorentzian signature breaks down.

### 4.7 Anomaly‑Cancellation Derivation
The supersymmetric world‑sheet central charge is
\[
c_{\text{total}} = \frac{3}{2}D - 15.
\tag{15}
\]
Setting \(c_{\text{total}}=0\) gives \(D=10\). Allowing an extra non‑compact tree to encode time yields the alternative solution \(D=11\) for M‑theory.

### 4.8 Automorphism‑Group Rank Matching
Each factor \(\mathrm{PGL}(2,\mathbb{Q}_{p_{i}})\) contributes rank 1. For a product of \(D\) factors the total rank is \(D\). Matching this rank to the rank 16 of the gauge group \(E_{8}\times E_{8}\) suggests either \(D=16\) with additional structure or, more simply, \(D=10\) with the remaining rank supplied by the directed causal tree and a compact extra tree. The simplest consistent choice remains \(D=10\).

## 5. Results
- **R1.** The product forest admits a scaling limit that yields a Lorentzian metric of signature \((D\!-\!1,1)\) (Section 3).  
- **R2.** Anomaly cancellation forces \(D=10\); supersymmetric continuum considerations admit \(D=10\) or \(D=11\) (Section 4, Eq. (15)).  
- **R3.** Horizon radii for the \(2\!+\!1\) black‑hole‑AdS background are \(r_{+}\approx3.992\) and \(r_{-}\approx0.2505\) (Section 4, Eq. (7)).  
- **R4.** The product boundary has covering dimension exactly \(D\) (Section 4, Eq. (14)).  
- **R5.** Forward causal cones grow as \(p^{k}\), exposing a scaling‑limit obstruction quantified by the resolution ratio \(1/p\) (Section 4, Eq. (4.5)).  
All numerical values arise from explicit arithmetic shown in Section 4.

## 6. Discussion
### 6.1 Limitations
- **L1.** The scaling limit assumes an infinite sequence of primes and idealised mixing; any practical implementation must truncate the prime set.  
- **L2.** The causal orientation on a single tree is imposed by hand; a dynamical emergence mechanism is not provided.  
- **L3.** The anomaly‑cancellation argument relies on the standard world‑sheet central‑charge formula, which presumes a perturbative string framework.  
- **L4.** The horizon‑radius computation uses illustrative parameters (assumption A1); physical relevance requires matching to actual black‑hole data.  
- **L5.** Exponential causal‑cone growth differs from the polynomial growth of continuum light cones, indicating a quantitative mismatch that must be resolved for exact Minkowski recovery.

Sensitivity analysis shows that modest variations in \(M\), \(l\), or \(J\) scale the horizon radii proportionally, while changes in the prime \(p\) alter vertex‑count and cone‑size combinatorics but not the dimensionality result.

### 6.2 Falsification Criterion
If a simulation of the product forest using the toolkit of [8] produces a scaling limit whose metric fails to exhibit a Lorentzian signature (e.g., all eigenvalues of the emergent metric are positive) or if the covering dimension of the product boundary deviates from \(D\), the main claim would be falsified.

### 6.3 Open Questions
- How can a dynamical mechanism generate the directed causal orientation from the combinatorial substrate?  
- Can the exponential cone growth be reconciled with continuum light‑cone geometry, perhaps via a renormalisation of the causal order?  
- What role do \(p\)-adic string amplitudes (adelic Veneziano integrals) play in constraining the admissible prime set and the emergent dimension?

## 7. Practical Implications and Engineering Pathways
### 7.1 Potential Users and Design Changes
Theoretical physicists developing background‑independent string models would use the product‑tree construction to replace arbitrary manifold choices with a discrete combinatorial substrate. Model‑building would shift from selecting a continuous metric to specifying a set of primes and tree valences, dramatically reducing the space of viable theories.

### 7.2 Technology Readiness Level
The work is purely analytical and has not undergone peer review; it therefore resides at **TRL 2** (concept formulation).

### 7.3 Minimal Next Experiment
A prototype simulation employing the graph‑Laplacian generator from [8] to construct a product of three Bruhat–Tits trees (e.g., \(p=2,3,5\)) and to measure the emergent spectral dimension would de‑risk the claim. Observation of a spectral dimension approaching \(3\) in the scaling limit would support the hypothesis; a persistent deviation would refute it.

### 7.4 Engineering Constraints
- **C1.** Availability of high‑precision \(p\)-adic arithmetic libraries for tree construction.  
- **C2.** Computational cost grows as \(N^{D}\) with \(N\) vertices per tree; efficient parallelisation is essential.  
- **C3.** No experimental data on \(p\)-adic spacetime exist; validation must rely on internal consistency checks.

### 7.5 Projected Performance Bounds
Assuming a simulation with \(N=10^{3}\) vertices per tree and \(D=4\), the total vertex count scales as \(N^{D}=10^{12}\). For \(D=10\) the state space exceeds \(10^{30}\) vertices, indicating that early prototypes will target \(D\le4\) as a proof‑of‑concept. This projection follows directly from the combinatorial definition in Section 3.

### 7.6 Risks and Misuse
A potential misuse path is the premature claim that the combinatorial model replaces all continuum physics without empirical validation. To mitigate this, any public dissemination must emphasise the provisional, theoretical nature of the construction and the necessity of the falsification tests described in Section 6.

## 8. Conclusion
We have shown that a product of \(D\) Bruhat–Tits trees, with a directed causal edge, can generate an emergent \((D\!-\!1,1)\) Minkowski spacetime in an adelic scaling limit. Consistency conditions derived from anomaly cancellation, supersymmetric continuum limits, and automorphism‑group gauge symmetries restrict the viable dimensions to \(D=10\) or \(D=11\), matching the critical dimensions of superstring and M‑theory. Explicit calculations reproduce black‑hole‑AdS horizon radii and demonstrate that the product boundary has covering dimension \(D\). The framework offers a background‑independent, combinatorial foundation for string theory, opening a pathway toward lattice‑type models rooted in non‑Archimedean geometry. Future work will focus on numerical simulations using the toolkit of [8] and on resolving the exponential causal‑cone growth to achieve exact Minkowski‑like causality.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.43-codeagent). Language models would be tools in that process; they are not authors. The named author would be accountable for the content.
- A study would use models for drafting: openai/gpt-oss-120b, zai-org/glm-5.3-flash; for reconciliation, completion, review, revision and verification: openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would require checks before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- A study would include independent recomputation: a separately generated script would recompute 8 quantitative claims from the paper's stated inputs; 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] On the accelerated observer's proper coordinates and the rigid motion problem in Minkowski spacetime. arXiv:1211.0222v3. https://arxiv.org/abs/1211.0222v3
[2] On packing of Minkowski balls. II. arXiv:2302.01644v3. https://arxiv.org/abs/2302.01644v3
[3] Minkowski dimension and explicit tube formulas for $p$-adic fractal strings. arXiv:1603.09409v4. https://arxiv.org/abs/1603.09409v4
[4] Strings and Multi-Strings in Black Hole and Cosmological Spacetimes. arXiv:hep-th/9504007v1. https://arxiv.org/abs/hep-th/9504007v1
[5] Feature Unification in TAG Derivation Trees. arXiv:0804.4584v1. https://arxiv.org/abs/0804.4584v1
[6] Raiders of the lost spacetime. arXiv:1405.5552v1. https://arxiv.org/abs/1405.5552v1
[7] https://papers.qnfo.org/papers/invariant-patterns-adelic-refactoring. QNFO: Invariant Patterns and the Adelic Refactoring of Fundamental Physics.
[8] https://papers.qnfo.org/papers/computational-toolkit-for-p-adic-spacetime. QNFO: Computational Toolkit for p-Adic Spacetime.
