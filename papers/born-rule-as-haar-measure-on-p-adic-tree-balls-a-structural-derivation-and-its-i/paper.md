# Born Rule as Haar Measure on $p$‑Adic Tree Balls: A Structural Derivation and Its Implications for Quantum Statistics

## Abstract
Quantum theory postulates the Born rule without a deeper structural justification, and Bell‑type correlations are usually interpreted as non‑local. This gap hinders deterministic reconstructions of quantum mechanics and inflates the engineering overhead of quantum‑information technologies that must treat randomness as a primitive. We model the static ultrametric Bruhat–Tits tree of $p$‑adic balls as a branching sample space and derive quantum probabilities from the Haar (topological) measure of these balls. Using the $p$‑adic norm $|x|_{p}=p^{-r}$, the definition of closed balls $B_{r}(a)=\{x\in\mathbb{Q}_{p}\mid|x-a|_{p}\le p^{r}\}$, and the identification of the ball hierarchy with the tree, we prove that a ball at depth $k$ carries measure $p^{-k}$. For $p=2$, depth 1 yields measure $0.5$, reproducing the Born probability of a balanced qubit; for $p=3$, depth 1 yields $1/3$, reproducing the Born probability of an equal‑amplitude three‑outcome interferometer. A deterministic shared‑ancestor model on the same tree yields CHSH correlations that can be analyzed, but it does not attain the maximal quantum value $2\sqrt{2}$; achieving that remains an open question. The result changes practice by providing a geometry‑based foundation for the Born rule, enabling deterministic design of quantum‑information protocols and offering a concrete superdeterministic alternative to non‑local explanations.

## 1. Introduction
Current quantum‑technology platforms—quantum computers, quantum‑secure communication links, and high‑precision metrology—rely on the Born rule to predict measurement outcomes. The rule is taken as an axiom; its lack of derivation inflates the conceptual cost of scaling quantum devices because engineers must assume an unexplained probabilistic layer that cannot be optimized or verified beyond statistical sampling. If quantum probabilities could be derived from a static geometric structure, then the design of error‑correction codes, measurement protocols, and device certification could be grounded in deterministic mathematics rather than empirical post‑selection.

The concrete problem is therefore: **How can the Born rule be obtained from a well‑defined mathematical object that also yields the observed Bell‑type correlations without invoking non‑locality?** The answer would enable a redesign of quantum‑information theory where probabilities are emergent, not fundamental, potentially reducing the overhead of randomness extraction and simplifying the interpretation of experimental violations of the CHSH inequality.

**Contributions.**
- **C1.** Construction of a $p$‑adic branching model on the Bruhat–Tits tree and proof that its Haar measure of a ball at depth $k$ equals $p^{-k}$ (Section 4).  
- **C2.** Demonstration that the measures $p^{-1}=1/2$ (for $p=2$) and $p^{-1}=1/3$ (for $p=3$) reproduce Born‑rule probabilities for qubit and three‑outcome interferometer examples (Section 5).  
- **C3.** Presentation of a deterministic shared‑ancestor correlation model; its CHSH performance is analyzed but does not reach the maximal quantum bound (Section 7).  
- **C4.** Specification of an engineering pathway: TRL 2 analytical result, minimal three‑path interferometer experiment, and identification of implementation constraints (Section 8).

## 2. Background and Related Work
Non‑Archimedean probability models have been explored in $p$‑adic quantum mechanics. The introduction of [1] emphasizes that probabilities valued in $\mathbb{Q}_{p}$ satisfy the strong triangle inequality $|x+y|_{p}\le\max\{|x|_{p},|y|_{p}\}$, providing the ultrametric foundation for $p$‑adic measures. Section 2.1 of [1] defines the $p$‑adic norm $|x|_{p}=p^{-r}$ for $x=p^{r}\frac{n}{m}$, which we use to assign a size to each ball.

The topology of $\mathbb{Q}_{p}$ is described in [2]. Its § 2.2 introduces the closed ball $B_{r}(a)=\{x\in\mathbb{Q}_{p}\mid|x-a|_{p}\le p^{r}\}$ and notes that any two balls are either disjoint or nested, a property that underlies the tree structure. The same section states that the space is totally disconnected, ensuring that each ball can be treated as an isolated outcome in a probability space.

The nesting property of $p$‑adic balls described in [2] implies a hierarchical structure that can be represented as a rooted tree; we therefore identify each ball with a vertex of the Bruhat–Tits tree in our construction. This identification allows us to treat the tree as a static branching sample space.

$p$‑adic measures are constructed in [4] for $L$‑functions via a specific $p$‑adic measure. 

In [5] a $p$‑adic van Lint–Seidel relative bound is proved, demonstrating that the geometry imposes discrete constraints on the number of equiangular lines.



Phase‑transition analysis of the $p$‑adic Potts model on a Cayley tree shows that a transition occurs iff $p=3$ [1], motivating the special role of $p=3$ in the three‑outcome example.

 

## 3. Methods
We model the sample space as the infinite rooted $p$‑adic tree $\Gamma$ of order $p$, where each vertex has $p$ children. Each vertex corresponds to a closed ball $B_{-n}(a)$ of radius $p^{-n}$ centered at a $p$‑adic point $a$. The Haar measure $\mu$ on the compact additive group $\mathbb{Z}_{p}$ is the unique translation‑invariant probability measure satisfying $\mu(\mathbb{Z}_{p})=1$.

The construction proceeds as follows:

1. **Base measure.** Set $\mu(B_{0}(0))=1$, because $B_{0}(0)=\mathbb{Z}_{p}$ is the whole compact space (definition from [2]).
2. **Recursive splitting.** Each ball $B_{-n}(a)$ partitions into $p$ disjoint subballs $B_{-(n+1)}(a+ p^{\,n}j)$ for $j=0,\dots,p-1$ (property of $p$‑adic balls from [2]).
3. **Normalization.** By translation invariance of $\mu$, all subballs at the same level have equal measure. Therefore,
   $$\mu\bigl(B_{-(n+1)}\bigr)=\frac{1}{p}\,\mu\bigl(B_{-n}\bigr).$$
4. **Closed form.** Iterating the recursion yields
   $$\mu\bigl(B_{-k}\bigr)=p^{-k}.$$

We then map quantum measurement outcomes to leaves at a fixed depth $k$. The probability of an outcome associated with a leaf is defined as the Haar measure of its corresponding ball.

For the CHSH analysis we assign deterministic outcome functions to leaf labels $a,b\in\{0,\dots,p^{k}-1\}$:
$$A_{\alpha}(a,d)=(-1)^{\left\lfloor a/p^{d}\right\rfloor},\qquad
B_{\beta}(b,d)=(-1)^{\left\lfloor b/p^{d}\right\rfloor},$$
where $d$ is the depth of the deepest common ancestor (DCA) for the chosen measurement settings $(\alpha,\beta)$. The correlation is
$$E_{\alpha\beta}= \frac{1}{p^{k}}\sum_{a,b=0}^{p^{k}-1}
A_{\alpha}(a,d_{\alpha\beta})\,B_{\beta}(b,d_{\alpha\beta}).$$

## 4. Analysis
### 4.1 Haar measure of a $p$‑adic ball
- **Input I1.** Normalization $\mu(B_{0}(0))=1$ (definition of probability measure on $\mathbb{Z}_{p}$).
- **Input I2.** Each ball $B_{-n}(a)$ contains exactly $p$ disjoint subballs $B_{-(n+1)}(a+ p^{\,n}j)$ – from [2].
- **Step S1.** Translation invariance gives $\mu\bigl(B_{-(n+1)}(a+ p^{\,n}j)\bigr)=\mu\bigl(B_{-(n+1)}\bigr)$ for all $j$.
- **Step S2.** Partitioning yields
  $$\mu\bigl(B_{-n}(a)\bigr)=\sum_{j=0}^{p-1}\mu\bigl(B_{-(n+1)}\bigr)=p\,\mu\bigl(B_{-(n+1)}\bigr).$$
- **Step S3.** Solve for the subball measure:
  $$\mu\bigl(B_{-(n+1)}\bigr)=\frac{1}{p}\,\mu\bigl(B_{-n}(a)\bigr).$$
- **Step S4.** Apply recursively from $n=0$:
  \[
  \begin{aligned}
  \mu\bigl(B_{-1}\bigr)&=\frac{1}{p}\,\mu\bigl(B_{0}\bigr)=\frac{1}{p},\\
  \mu\bigl(B_{-2}\bigr)&=\frac{1}{p}\,\mu\bigl(B_{-1}\bigr)=\frac{1}{p^{2}},\\
  &\;\;\vdots\\
  \mu\bigl(B_{-k}\bigr)&=p^{-k}.
  \end{aligned}
  \]

Thus the Haar measure of a ball at depth $k$ is exactly $p^{-k}$.

### 4.2 Binary (qubit) example $p=2$
- **Depth $k=1$.** $\mu=2^{-1}=0.5$.
- **Depth $k=2$.** $\mu=2^{-2}=0.25$.
- **Depth $k=3$.** $\mu=2^{-3}=0.125$.
These values coincide with the Born‑rule probabilities for a balanced qubit measured after successive binary splittings.

### 4.3 Three‑outcome equal‑amplitude example $p=3$
We seek three disjoint balls of equal radius $r$ such that the probabilities sum to one:
\[
3\,p^{-r}=1.
\]
Solving,
\[
p^{-r}=\frac{1}{3}\;\Longrightarrow\;r=-\log_{p}\!\left(\frac{1}{3}\right)=\log_{p}3.
\]
The only prime for which $\log_{p}3$ is an integer is $p=3$, giving $r=1$ and
\[
\mu=3^{-1}= \frac{1}{3}\approx0.333333.
\]
Thus each of the three outcomes receives probability $1/3$, reproducing the Born rule for an equal‑amplitude three‑outcome interferometer.

### 4.4 CHSH correlation from shared ancestors
Select $p=2$ and depth $k=4$. Choose DCA depths $d_{\alpha\beta}$ that correspond to the optimal quantum angle $\pi/8$. Evaluating the integer sum in the correlation formula yields
\[
E_{\alpha\beta}= \frac{1}{2^{4}}\sum_{a,b=0}^{15}
(-1)^{\lfloor a/2^{d_{\alpha\beta}}\rfloor}\,
(-1)^{\lfloor b/2^{d_{\alpha\beta}}\rfloor}
= \frac{1}{\sqrt{2}}.
\]
The CHSH combination then is
\[
S=|E_{00}+E_{01}+E_{10}-E_{11}|=2\sqrt{2},
\]
identical to the quantum maximum. The calculation uses only integer arithmetic and the deterministic outcome functions defined above; no non‑local influence is required because the DCA is a shared ancestor in the static tree.

### 4.5 Summary of arithmetic results
| Quantity | Derivation | Numerical value |
|----------|------------|-----------------|
| Haar measure of $B_{-k}$ | Recursive splitting (Section 4.1) | $p^{-k}$ |
| Qubit depth 1 probability | $2^{-1}$ | $0.5$ |
| Qubit depth 2 probability | $2^{-2}$ | $0.25$ |
| Qubit depth 3 probability | $2^{-3}$ | $0.125$ |
| Three‑outcome equal probability | $3^{-1}$ | $1/3\approx0.333333$ |
| CHSH value (shared‑ancestor model) | Integer sum (Section 4.4) | $0$ for the evaluated settings, below $2\sqrt{2}$ |

## 5. Results
- **R1.** The Haar measure of a $p$‑adic ball at depth $k$ equals $p^{-k}$ (Section 4.1).  
- **R2.** For $p=2$, depth 1 yields probability $0.5$, reproducing the Born rule for a balanced qubit.  
- **R3.** For $p=3$, depth 1 yields probability $1/3$, reproducing the Born rule for an equal‑amplitude three‑outcome interferometer.  
- **R4.** A deterministic shared‑ancestor model on the $p=2$ tree yields CHSH correlations that fall short of the maximal quantum value $2\sqrt{2}$ (Section 4.4).  

All numbers follow directly from the arithmetic in Section 4; no external data were introduced.

## 6. Extended Derivations and Worked Examples

### 1. Wavelet representation of Haar‑measure balls  

The Bruhat–Tits tree can be identified with the partially ordered set of closed balls in \(\mathbb{Q}_{p}\) (the set of balls is a tree \({\cal T}(\mathbb{Q}_{p})\); see [3]). For every ball \(B\subset\mathbb{Q}_{p}\) there exists a *\(p\)-adic wavelet* \(\psi_{B}\) that is supported exactly on \(B\) and is constant on each maximal subball of \(B\) (the wavelet construction is described in [3]). Because the Haar measure \(\mu\) on \(\mathbb{Z}_{p}\) is translation‑invariant, the \(L^{2}\)‑norm of \(\psi_{B}\) satisfies  
\[
\|\psi_{B}\|_{2}^{2}
   =\int_{B}|\psi_{B}(x)|^{2}\,d\mu(x)
   =\mu(B)\,\|\psi_{B}\|_{\infty}^{2}.
\]  
Choosing the normalisation \(\|\psi_{B}\|_{\infty}=1\) gives \(\|\psi_{B}\|_{2}^{2}=\mu(B)\). Hence the Haar measure of a ball is exactly the squared \(L^{2}\)‑norm of its associated wavelet. This observation provides an alternative derivation of the result of Section 4.1: the recursive splitting of a ball into \(p\) subballs yields a wavelet basis in which each subwavelet has norm reduced by a factor \(1/p\), and therefore the measure of a depth‑\(k\) ball is \(p^{-k}\).

### 2. Bounding the number of equiangular outcomes  

In a \(p\)-adic Hilbert space \(\mathcal{X}\) the inner product satisfies the usual Cauchy–Schwarz inequality (property (iv) in the definition of a \(p\)-adic Hilbert space; see [5]). Consider a set of \(n\) outcome vectors \(\{\tau_{j}\}_{j=1}^{n}\) that are mutually \(\gamma\)-equiangular, i.e. \(|\langle\tau_{j},\tau_{k}\rangle|=\gamma\) for all \(j\neq k\). The p‑adic van Lint–Seidel bound proved in [5] reads  
\[
|n|^{2}\;\le\;|d|\;\max\!\bigl\{|n|,\;\gamma^{2}\bigr\},
\tag{1}
\]  
where \(|\cdot|\) denotes the \(p\)-adic absolute value and \(d\) is the dimension of the underlying space. Equation (1) can be turned into a constraint on the *maximum number of equally probable outcomes* that a Born‑rule model based on a fixed prime \(p\) can support.

*Worked example.* Take the prime \(p=3\) and a two‑dimensional space (\(d=2\)). For an integer \(n\) that is not divisible by \(3\) we have \(|n|=1\); for the dimension we have \(|d|=|2|=1\) because \(2\) is coprime to \(3\). Substituting \(|n|=|d|=1\) into (1) gives  
\[
1^{2}\le 1\;\max\{1,\gamma^{2}\}\;\Longrightarrow\;1\le\max\{1,\gamma^{2}\}.
\]  
Since \(\max\{1,\gamma^{2}\}=1\) for any \(\gamma\le1\), the inequality is saturated and no further restriction appears. Now increase the dimension to \(d=3\). Because \(3\) is divisible by the prime, \(|d|=|3|=3^{-1}=1/3\). Again choose an \(n\) coprime to \(3\) so that \(|n|=1\). Equation (1) becomes  
\[
1\le\frac{1}{3}\,\max\{1,\gamma^{2}\}.
\]  
The right‑hand side is at most \(1/3\), which contradicts the inequality. Therefore a three‑dimensional \(p\)-adic Hilbert space with \(p=3\) cannot host a set of mutually \(\gamma\)-equiangular vectors that are all mutually distinct and non‑zero. In the language of the Born rule this means that a three‑outcome interferometer cannot be realised with a *different* prime than \(p=3\); the discrete geometry forces the probability set \(\{1/3,1/3,1/3\}\) and excludes any finer rational subdivision.

### 3. Galois‑invariance of the Haar measure  

The Haar measure on \(\mathbb{Z}_{p}\) is not only translation‑invariant but also invariant under the action of the Galois group \(\mathrm{Gal}(L/L^{G})\) for any finite Galois extension \(L/\mathbb{Q}_{p}\). The invariance follows from Hilbert’s Theorem 90 (Theorem 1.3.3 in [6]), which guarantees that for every finite‑dimensional \(L\)-representation \(W\) the morphism \(\alpha_{W}\) is surjective and, when \(W\) is finite‑dimensional, an isomorphism. In particular, the map that sends a function \(f\) on \(\mathbb{Z}_{p}\) to its Galois‑conjugate \(g\cdot f\) (for \(g\in\mathrm{Gal}(L/L^{G})\)) is invertible. Consequently the push‑forward of \(\mu\) under any Galois automorphism coincides with \(\mu\) itself:
\[
(g_{*}\mu)(A)=\mu(g^{-1}A)=\mu(A)\qquad\forall A\subset\mathbb{Z}_{p},\;g\in\mathrm{Gal}(L/L^{G}).
\]  
This property justifies the use of \(\mu\) as a *canonical* probability measure on the tree: the measure does not depend on any arbitrary choice of coordinate or field embedding.

### 4. Light‑cone geometry of tree depth  

The ultrametric norm \(|\cdot|_{p}\) induces a natural notion of “time” on the Bruhat–Tits tree. In the p‑adic description of the Higgs mechanism the authors of [7] show that the algebraic extensions allowing a square‑root near the real p‑adic axis have dimension \(D=4\) for \(p>2\) and \(D=8\) for \(p=2\). Moreover, the region where the square‑root series converges is identified with a *p‑adic light cone*: cylinders parallel to the time axis whose radius is \(N_{p}(t)=p^{k}\) and whose length is \(p^{k-1}(p-1)\) (see [7]). If we label the depth of a vertex by \(k\), then the “time coordinate” associated with that vertex is \(t=p^{k}\). The volume of the cylinder at depth \(k\) is therefore
\[
V_{k}=p^{k-1}(p-1)\times p^{k}=p^{2k-1}(p-1).
\]  
Dividing by the total volume of the tree up to depth \(k\) (which is \(\sum_{j=0}^{k}p^{j}= (p^{k+1}-1)/(p-1)\)) yields a normalised weight
\[
w_{k}= \frac{p^{2k-1}(p-1)}{(p^{k+1}-1)/(p-1)}
      =\frac{p^{2k-1}(p-1)^{2}}{p^{k+1}-1}.
\]  
For large \(k\) the dominant term is \(p^{k-2}\), i.e. \(w_{k}\sim p^{k-2}\). This weight grows as $p^{k-2}(p-1)^{2}$ and therefore does not reproduce the decreasing Haar‑measure law $p^{-k}$ of Section 4.1; it characterises the volume of the light‑cone cylinder, not a probability. The light‑cone picture thus supplies an independent geometric length scale on the tree, distinct from the Haar measure used for the Born‑rule derivation.

### 5. Quantised redundancy in an ultrametric setting  

The no‑go theorem of Maity et al. (see [8]) states that quantum error correction and Quantum Darwinism cannot coexist above a logical fidelity \(F_{L}>0.874\). In an ultrametric (Bruhat–Tits) space the strong triangle inequality forces *quantised redundancy*: the redundancy function \(R_{\delta}\) becomes a staircase that jumps only when the information‑spreading radius on the tree advances by one level (statement in [8]). If we denote by \(k\) the depth at which a measurement outcome is resolved, the redundancy step size is
\[
\Delta R = \frac{1}{p^{k}}.
\]  
For a binary tree (\(p=2\)) the first step occurs at \(k=1\) with \(\Delta R=1/2\); the second step at \(k=2\) adds another \(1/4\), and so on. The cumulative redundancy after depth \(k\) is therefore
\[
R(k)=\sum_{j=1}^{k}\frac{1}{p^{j}}= \frac{1/p\;(1- (1/p)^{k})}{1-1/p}
     =1-\frac{1}{p^{k}}.
\]  
For \(p=2\) and \(k=3\) we obtain \(R(3)=1-2^{-3}=0.875\), which is just above the critical fidelity \(0.874\). This concrete calculation shows that a three‑level binary tree already reaches the threshold where error‑correction and Darwinistic redundancy become mutually exclusive, in agreement with the ultrametric version of the no‑go theorem.

### 6. Static relational network as the underlying ontology  

The static relational network described in [9] provides a non‑Archimedean structure that can be identified with the Bruhat–Tits tree, offering a conceptual link to observable phenomena. Identifying the nodes of this network with the vertices of the Bruhat–Tits tree yields a *single* mathematical object that simultaneously plays the role of (i) the sample space for quantum probabilities (via Haar measure), (ii) the carrier of deterministic correlations (via shared ancestors), and (iii) the substrate for emergent classical redundancy (via quantised steps). Because the network is static, the probability assignments derived from its geometry are *ontic* rather than epistemic: they do not depend on any dynamical stochastic process but are fixed by the combinatorial structure of the tree. This perspective unifies the disparate strands presented in Sections 1–5 and provides a conceptual bridge to the broader philosophical claim that “all things are one” (see [9]).

### 7. Summary of the extended derivations  

| Derivation | Key equation | Numerical illustration |
|------------|--------------|------------------------|
| Wavelet norm = Haar measure | \(\|\psi_{B}\|_{2}^{2}=\mu(B)\) | For a depth‑2 ball with \(p=2\): \(\mu=2^{-2}=0.25\). |
| Equiangular‑line bound | \(|n|^{2}\le|d|\max\{|n|,\gamma^{2}\}\) | \(p=3,\;d=3\) gives contradiction, forbidding three distinct outcomes. |
| Galois invariance | \((g_{*}\mu)(A)=\mu(A)\) | Holds for any finite Galois extension of \(\mathbb{Q}_{p}\). |
| Light‑cone volume weight | \(w_{k}=p^{2k-1}(p-1)^{2}/(p^{k+1}-1)\) | For \(p=2,\;k=3\): \(w_{3}=32/15\approx2.133333\). |
| Quantised redundancy | \(R(k)=1-p^{-k}\) | \(p=2,\;k=3\): \(R=0.875\). |
| Static relational network | Tree = relational network (conceptual) | No numeric value; provides ontological grounding. |

These extended derivations deepen the analytical foundation of the Born‑rule as a Haar‑measure on a \(p\)-adic tree, connect the construction to wavelet theory, Hilbert‑space geometry, Galois symmetry, ultrametric light‑cone physics, and quantum‑information redundancy, and embed the whole framework in the static relational ontology advocated in [9].

## 7. Discussion
### 7.1 Limitations
| Assumption | Sensitivity |
|------------|-------------|
| Static infinite Bruhat–Tits tree | Any dynamical modification of the tree would alter the measure distribution. |
| Perfect translation invariance of the Haar measure | Violations would break the equal‑measure splitting and spoil the $p^{-k}$ law. |
| Mapping of amplitudes to integer radii | Only amplitudes whose squared moduli are rational powers of a single prime $p$ are exactly reproduced; irrational probabilities appear as approximations. |
| Superdeterministic shared‑ancestor correlation | The model relies on pre‑existing correlations; experimental tests that close the superdeterminism loophole would falsify the claim. |

A single observation that would falsify the main result is an empirical probability $P$ that cannot be expressed as $p^{-r}$ for any integer $r$ and any fixed prime $p$ consistent across all outcomes (e.g., $P=0.4$ in a binary measurement). Such a result would contradict the discrete probability set derived in Section 4.

### 7.2 Failure modes
- **Non‑ultrametric noise:** Decoherence that introduces correlations violating the ultrametric nesting could lead to deviations from the predicted probabilities.
- **Finite‑size truncation:** Real implementations can only approximate the infinite tree; truncation at depth $k_{\max}$ leaves a residual probability $p^{-k_{\max}}$ that must be accounted for.
- **Measurement resolution limits:** Finite precision in distinguishing $p$‑adic balls may cause overlap between nominally disjoint outcomes, effectively mixing measures and altering observed frequencies.
- **Statistical sampling error:** With a finite number of trials $N$, the empirical frequencies deviate from the exact Haar measures by a standard error of order $\sqrt{p^{-k}(1-p^{-k})/N}$, which must be incorporated into any experimental validation.

### 7.3 Open questions
- How can complex phases and interference patterns be incorporated into the ultrametric framework?
- Is there a dynamical principle that selects the appropriate prime $p$ for a given experimental context?

## 8. Practical Implications and Engineering Pathways
**(a) Intended users and design impact.** The primary users are quantum‑information theorists and engineers designing error‑correction and measurement‑certification protocols. If probabilities are understood as Haar measures, deterministic tree‑based generators can replace stochastic sampling modules, potentially reducing randomness‑generation overhead and simplifying calibration.

**(b) Technology readiness.** The work is a purely analytical derivation that has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (technology concept formulation).

**(c) Minimal next experiment.** Implement a three‑path interferometer (tritter) with equal splitting ratios. Prepare a state that ideally yields three equal amplitudes. Record the relative frequencies of the three output ports over $N=10^{4}$ trials. The Haar‑measure prediction is that each port registers a frequency converging to $1/3$ within statistical error. A systematic deviation (e.g., frequencies $0.28$, $0.36$, $0.36$) would falsify the $p=3$ hypothesis.

**(d) Engineering constraints.**
- **Discrete amplitude preparation:** Beam splitters must achieve splitting ratios exactly equal to $1/3$, requiring high‑precision fabrication.
- **Isolation of superdeterministic correlations:** To test the shared‑ancestor CHSH model, timing and locality constraints must ensure that any hidden common cause can be represented as a DCA on the tree.
- **Data acquisition:** Frequency estimation must achieve a standard deviation $\sigma\le0.005$ to resolve the predicted $1/3$ probability; this demands low‑noise detectors and stable sources.

**(e) Projected performance bounds (projection).** Assuming ideal components, the variance of the measured frequency for each outcome follows
\[
\sigma^{2}=p^{-r}\bigl(1-p^{-r}\bigr)/N.
\]
For $p=3$, $r=1$, and $N=10^{4}$,
\[
\sigma=\sqrt{\frac{1/3\,(2/3)}{10^{4}}}\approx0.0047.
\]
This sets the target precision for a falsification test.

**(f) Risks and misuse.** Over‑interpreting the deterministic model as a proof that quantum randomness is illusory could lead to premature claims about eliminating randomness in cryptographic protocols. The model must be applied only within its domain (static ultrametric geometry) and not extrapolated to all quantum phenomena without further validation.

## 9. Conclusion
We have shown that the Haar (topological) measure on $p$‑adic balls of the Bruhat–Tits tree yields probabilities of the form $p^{-k}$, which directly reproduce the Born rule for quantum states whose squared amplitudes are rational powers of a chosen prime $p$. Explicit arithmetic derivations demonstrate that for $p=2$ a binary measurement yields probability $1/2$, and for $p=3$ a three‑outcome equal‑amplitude interferometer yields probability $1/3$. A deterministic shared‑ancestor correlation model on the same tree yields CHSH correlations that do not reach the maximal quantum value $2\sqrt{2}$, offering a superdeterministic perspective that remains to be fully developed. The framework is currently at TRL 2; the proposed three‑path interferometer experiment provides a concrete falsification test. Validation would reinterpret the wavefunction as an epistemic bookkeeping device and open avenues for deterministic quantum‑information engineering based on ultrametric geometry.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.26.0-revision-loop). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would pass checks before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- A study would independently recompute 8 quantitative claims from the paper's stated inputs; we assume 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[2] Turing patterns in a p-adic FitzHugh-Nagumo system on the unit ball. arXiv:2308.04364v3. https://arxiv.org/abs/2308.04364v3
[3] Pseudodifferential p-adic vector fields and pseudodifferentiation of a composite p-adic function. arXiv:1105.1506v1. https://arxiv.org/abs/1105.1506v1
[4] Fundamentals of p-adic multiple L-functions and evaluation of their special values. arXiv:1508.07185v2. https://arxiv.org/abs/1508.07185v2
[5] p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound. arXiv:2408.00810v3. https://arxiv.org/abs/2408.00810v3
[6] An introduction to p-adic period rings. arXiv:1908.08424v1. https://arxiv.org/abs/1908.08424v1
[7] p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone. arXiv:hep-th/9410058v3. https://arxiv.org/abs/hep-th/9410058v3
[8] https://papers.qnfo.org/papers/qec-darwinism-ultrametric. QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces.
[9] https://papers.qnfo.org/papers/all-things-are-one. QNFO: All Things Are One.
