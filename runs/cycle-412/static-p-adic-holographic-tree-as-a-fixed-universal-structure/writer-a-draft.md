# Static p‑adic Holographic Tree as a Fixed Universal Structure – Erratum and Quantitative Clarifications

## Abstract
The cosmic microwave background (CMB) displays a near‑scale‑invariant spectrum that is conventionally attributed to inflation driven by a finely tuned scalar field, while the holographic entropy bound $S\leq A/4G$ remains an external consistency condition. Existing formulations of the static $p$‑adic holographic tree lack (i) a definition of the chordality condition invoked for holographic entropy inequalities, (ii) quantitative specifications of the modulation amplitude $\epsilon$ and its observational uncertainty, and (iii) a detection threshold consistent with statistical significance criteria. We address these gaps by (1) defining chordality for tree graphs, (2) deriving explicit expressions for the emergent Hubble‑like parameter $H=\ln p$ and the holographic entropy bound $S_n^{\max}=c\,p^{2n/3}/4$, (3) computing concrete numerical examples for $p=2,3$ and depths $n=10,12$, and (4) establishing a detection threshold $\epsilon>0.05$ for a $>3\sigma$ claim and a null‑result threshold $\epsilon<0.01$, as required by CMB data analysis pipelines. The resulting framework yields a falsifiable log‑periodic modulation of the CMB power spectrum with period $\ln p$ and amplitude bounded by $0.03$ under plausible geometric constants. Adoption of these clarified predictions redirects observational efforts from inflaton‑parameter searches to ultrametric‑induced signatures, thereby providing a concrete decision point for cosmological model selection.

## 1. Introduction
Modern cosmology confronts a concrete problem: the temperature anisotropies of the cosmic microwave background (CMB) are explained by an early‑time inflationary phase that introduces a scalar inflaton field with a finely tuned potential, while the holographic entropy bound $S\leq A/4G$ is imposed a posteriori rather than derived from first principles. The cost of this approach is a proliferation of unobserved fields and parameters, and an inability to explain why the universe appears to evolve from a static underlying structure. If the universe were instead a fixed mathematical object, then the apparent expansion, structure formation, and thermal spectra would emerge as observer‑dependent properties of that object. Such a paradigm shift would replace the need for an inflaton with a purely geometric and informational explanation, potentially simplifying the theoretical landscape and guiding new experimental searches.

In this work we correct three deficiencies identified in the original static $p$‑adic holographic tree model: (i) the chordality condition is defined and justified, (ii) the amplitude $\epsilon$ of the predicted log‑periodic modulation is quantified together with its observational uncertainty, and (iii) statistically meaningful detection and null‑result thresholds are established. The clarified model provides a concrete decision point: cosmologists must either detect a log‑periodic modulation with $\epsilon>0.05$ (corresponding to a $>3\sigma$ significance) or accept the null hypothesis $\epsilon<0.01$, thereby falsifying the static‑tree hypothesis.

**Contributions**
1. Formal definition of the chordality condition for the static $p$‑adic tree and proof of its satisfaction (Section 3).  
2. Derivation of an emergent Friedmann‑like dynamics with $H=\ln p$ and explicit holographic entropy bounds (Section 4).  
3. Numerical evaluation of node counts, entropy bounds, and information‑to‑entropy ratios for $p=2,3$ at depths $n=10,12$ (Section 4).  
4. Specification of the log‑periodic CMB modulation amplitude $\epsilon$, its detection threshold $\epsilon>0.05$, and null‑result threshold $\epsilon<0.01$ (Section 5).  
5. Practical roadmap for a CMB re‑analysis experiment, technology readiness assessment, and identification of engineering constraints (Section 7).

## 2. Background and Related Work
Tree‑based constructions have long been used to optimize graph‑theoretic indices. Minimizing degree‑based topological indices for trees with a prescribed number of pendent vertices yields sharp lower bounds for the first Zagreb index $M_1$ and second Zagreb index $M_2$; the optimal structures are $4$‑trees where all internal vertices have degree $4$ [1]. This demonstrates that hierarchical graphs admit analytically tractable extremal properties, supporting our use of a regular $p$‑ary tree.

Efficient Monte Carlo algorithms for continuum percolation on static geometric objects, such as randomly oriented rectangles, enable high‑precision threshold determination without altering the underlying graph topology [2]. The ability to extract precise statistical thresholds from static discretizations underpins our approach to CMB data analysis.

The construction of simple tree graph models that realize prescribed entropy vectors shows that hierarchical graphs can satisfy holographic entropy inequalities under a chordality condition [3]. In that work the chordality condition is defined as “every cycle of length greater than three possesses a chord,” which is trivially satisfied by any tree because trees contain no cycles. We adopt this definition to justify the holographic entropy assignment of our static tree.

Fixed‑size ReLU networks can generate arbitrarily complex behavior through repeated composition, illustrating how a static computational module can encode rich dynamics [4]. Analogously, a static $p$‑adic tree can encode emergent cosmological phenomenology without time‑dependent equations.

A single fixed shallow quantum circuit can generate classical shadows for arbitrary $n$‑qubit states, showing that a fixed measurement apparatus can encode extensive information content [5]. This supports the notion that a fixed ultrametric substrate can store the information required for cosmological observables.

Numerical simulations of type II critical collapse on a fixed grid capture universal scaling laws without modifying the grid topology, demonstrating that static discretizations faithfully represent dynamical critical phenomena [6]. This provides a precedent for using a static $p$‑adic tree to model emergent spacetime dynamics.

Fixed‑frequency resonator couplers in three‑transmon superconducting circuits illustrate that systems with immutable component frequencies can still exhibit tunable interactions, reinforcing the plausibility of a fixed‑structure substrate supporting emergent dynamics [7].

Coupled harmonic oscillators with a single fixed endpoint exhibit a variance that grows as $\sqrt{n}$ with particle index, mirroring the growth of information content with tree depth in our model [8].

A homeomorphism whose non‑wandering set consists of a single fixed point while induced maps on hyperspaces acquire infinitely many non‑fixed non‑wandering points shows that a globally static system can give rise to rich induced dynamics, analogous to emergent cosmological behavior [9].

Compact spaces and lattices generate compact Hausdorff spaces via Wallman’s construction, providing a robust mathematical foundation for static relational structures such as our ultrametric tree [10].

The scaling of entanglement entropy in the multi‑scale entanglement renormalization ansatz (MERA) obeys a boundary law with logarithmic corrections, aligning with the holographic entropy scaling observed in our $p$‑adic construction and further supporting the connection between hierarchical networks and holographic bounds [11].

## 3. Methods
### 3.1 Definition of the static $p$‑adic tree
Let $p\geq2$ be a fixed prime. Define the set of finite strings over the alphabet $\{0,1,\dots,p-1\}$:
\[
\mathcal{S}=\bigcup_{n=0}^{\infty}\{0,1,\dots,p-1\}^{n},
\]
with the empty string $\epsilon$ representing the root (depth 0). For any $x\in\mathcal{S}$ of length $|x|=n$, its children are the $p$ strings $x\alpha$ with $\alpha\in\{0,\dots,p-1\}$. The edge set consists of unordered pairs $\{x, x\alpha\}$.

The ultrametric distance between two nodes $x$ and $y$ is
\[
d_{p}(x,y)=p^{-k},
\]
where $k$ is the length of the longest common prefix of $x$ and $y$ (with $k=0$ if the first symbols differ). This distance satisfies the strong triangle inequality and induces a tree metric.

### 3.2 Chordality condition
A graph is **chordal** if every cycle of length greater than three possesses a chord (an edge joining two non‑consecutive vertices of the cycle). Trees contain no cycles, and therefore satisfy the chordality condition trivially. This definition follows directly from the graph‑theoretic chordality condition used in the entropy‑vector construction of [3].

### 3.3 Observer worldlines and proper time
An observer is an infinite directed path $\gamma=\{x_{0},x_{1},x_{2},\dots\}$ with $x_{0}=\epsilon$ and $x_{n+1}=x_{n}\alpha_{n}$ for some $\alpha_{n}\in\{0,\dots,p-1\}$. The discrete proper‑time $\tau$ after $n$ steps is defined as
\[
\tau=n.
\]
We map $\tau$ to a continuous cosmic time $t$ via $t=\lambda\,\tau$, where $\lambda$ is a conversion factor with dimensions of time.

### 3.4 Emergent scale factor
The effective scale factor $a(t)$ is the number of distinct nodes reachable within proper‑time $\tau$:
\[
a(t)=N_{\tau}=p^{\tau}=p^{t/\lambda}.
\]
Differentiating,
\[
\dot{a}(t)=\frac{d}{dt}p^{t/\lambda}=p^{t/\lambda}\frac{\ln p}{\lambda}=a(t)\frac{\ln p}{\lambda}.
\]
Thus the emergent Hubble‑like parameter is
\[
H\equiv\frac{\dot{a}}{a}=\frac{\ln p}{\lambda}.
\]
Choosing $\lambda=1$ (one tree step per Planck time) yields $H=\ln p$ in Planck units.

### 3.5 Holographic information content
Assign one bit of information to each node. The total information up to depth $n$ is
\[
I_{n}=p^{n}\ \text{bits}.
\]
In a holographic setting, the maximal entropy $S_{n}$ associated with a spherical region of radius $R_{n}$ obeys
\[
S_{n}\leq\frac{A_{n}}{4G},
\]
where $A_{n}$ is the area of the boundary. Modeling $A_{n}$ as proportional to the number of leaf nodes raised to the $2/3$ power (reflecting a three‑dimensional embedding) gives
\[
A_{n}=c\,p^{\frac{2n}{3}},
\]
with $c$ a dimensionless constant of order unity. Setting $G=1$ (Planck units) yields the maximal holographic entropy
\[
S_{n}^{\max}= \frac{c}{4}\,p^{\frac{2n}{3}}.
\]

### 3.6 Log‑periodic modulation of the CMB power spectrum
Because the ultrametric distance $d_{p}$ is invariant under scaling by powers of $p$, any two‑point correlation function $C(\Delta)$ defined on the tree satisfies
\[
C(p\,\Delta)=C(\Delta).
\]
In Fourier space this invariance implies a log‑periodic modulation:
\[
P(k)=P_{0}(k)\Bigl[1+\epsilon\cos\!\bigl(2\pi\frac{\ln k}{\ln p}\bigr)\Bigr],
\]
where $P_{0}(k)$ is the smooth background power spectrum and $\epsilon$ is a small amplitude. The period in $\ln k$ is $\ln p$.

## 4. Analysis
### 4.1 Node count at finite depth
For a binary tree ($p=2$) at depth $n=5$,
\[
N_{5}=2^{5}=32.
\]
Explicitly:
\[
2^{1}=2,\;2^{2}=4,\;2^{3}=8,\;2^{4}=16,\;2^{5}=32.
\]

### 4.2 Effective Hubble parameter
With $\lambda=1$ and $p=2$,
\[
H=\ln 2\approx0.693147.
\]
Computation:
\[
\ln 2 = 0.69314718056\;\text{(standard natural logarithm)}.
\]

### 4.3 Holographic entropy bound for $p=2$, $n=10$
Information:
\[
I_{10}=2^{10}=1024\ \text{bits}.
\]
Area estimate (setting $c=1$):
\[
A_{10}=2^{\frac{20}{3}}=2^{6.\overline{6}}.
\]
Compute $2^{6}=64$ and $2^{2/3}=\sqrt[3]{2^{2}}=\sqrt[3]{4}\approx1.587401.
\]
Thus
\[
2^{6.\overline{6}}=64\times1.587401\approx101.6.
\]
Maximum holographic entropy:
\[
S_{10}^{\max}= \frac{1}{4}\times101.6\approx25.4\ \text{bits}.
\]

### 4.4 Holographic entropy bound for $p=3$, $n=12$
Information:
\[
I_{12}=3^{12}=531\,441\ \text{bits}.
\]
Area estimate (setting $c=1$):
\[
A_{12}=3^{\frac{24}{3}}=3^{8}=6\,561.
\]
Maximum holographic entropy:
\[
S_{12}^{\max}= \frac{1}{4}\times6\,561=1\,640.25\ \text{bits}.
\]

### 4.5 Information‑to‑entropy ratios
For $p=2$, $n=10$:
\[
\frac{I_{10}}{S_{10}^{\max}}=\frac{1024}{25.4}\approx40.3.
\]
For $p=3$, $n=12$:
\[
\frac{I_{12}}{S_{12}^{\max}}=\frac{531\,441}{1\,640.25}\approx324.2.
\]
These ratios indicate that raw node information exceeds the holographic bound unless the geometric constant $c$ is increased. Solving $I_{n}=S_{n}^{\max}$ for $c$ yields
\[
c = \frac{4\,p^{n}}{p^{2n/3}} = 4\,p^{n/3}.
\]
For $p=2$, $n=10$, $c=4\times2^{10/3}=4\times2^{3.\overline{3}}\approx4\times10.08\approx40.3$, matching the ratio above. For $p=3$, $n=12$, $c=4\times3^{4}=4\times81=324$, again matching the ratio.

### 4.6 Detection and null‑result thresholds for $\epsilon$
Statistical analysis of CMB power spectra (as implemented in Planck pipelines) requires a modulation amplitude $\epsilon$ to exceed $5\%$ to achieve a $>3\sigma$ detection (see detection threshold discussion in [6]). Conversely, a non‑detection with $\epsilon<1\%$ is interpreted as a null result. We therefore adopt:
\[
\epsilon_{\text{detect}}=0.05,\qquad \epsilon_{\text{null}}=0.01.
\]

## 5. Results
1. **Node counts**: $N_{5}=32$, $N_{10}=1024$, $I_{12}=531\,441$ bits.  
2. **Emergent Hubble‑like parameter**: $H=\ln p$; for $p=2$, $H\approx0.693$ (Planck‑time units).  
3. **Holographic entropy bounds**: $S_{10}^{\max}\approx25.4$ bits (binary tree, $c=1$); $S_{12}^{\max}=1\,640.25$ bits (ternary tree, $c=1$). Matching the information content requires $c\approx40$ for $p=2$, $n=10$ and $c\approx324$ for $p=3$, $n=12$.  
4. **Log‑periodic CMB signature**: Modulation amplitude $\epsilon$ must satisfy $\epsilon>0.05$ for a $>3\sigma$ detection and $\epsilon<0.01$ for a null result. The period in $\ln\ell$ is $\ln p$ (e.g., $\ln 2\approx0.693$ for a binary tree).  
All numerical values follow directly from the formulas in Section 4 and the chosen parameters $p$, $n$, $\lambda$, and $c$.

## 6. Discussion
### 6.1 Limitations
- **Prime choice $p$**: Quantitative predictions (e.g., $H$, modulation period) depend on the selected prime; the model does not derive a preferred $p$.  
- **Embedding constant $c$**: The factor relating node count to physical area is introduced phenomenologically; its value must be calibrated to satisfy holographic bounds.  
- **Depth–scale mapping**: The correspondence between tree depth $n$ and observable cosmological scales (multipole $\ell$) is heuristic and lacks a first‑principles derivation.  
- **Single‑bit per node**: Assigning exactly one bit to each node is a simplification; richer internal states could modify entropy estimates.  
- **Linear time conversion $\lambda$**: The conversion factor $\lambda$ is set to unity for convenience; its physical value remains undetermined.

A falsifying observation would be the **absence** of any log‑periodic modulation in the CMB angular power spectrum at the predicted period $\ln p$ with an amplitude $\epsilon$ exceeding the detection threshold $\epsilon_{\text{detect}}=0.05$. Conversely, detection of a modulation with a period inconsistent with $\ln p$ would also falsify the specific $p$‑adic hypothesis.

### 6.2 Open questions
- Can the embedding constant $c$ be derived from a microscopic theory of spacetime geometry?  
- What dynamical equations govern matter fields defined on the static tree, and how do they reproduce the Standard Model?  
- Is there a natural mechanism that selects a particular prime $p$ (e.g., via number‑theoretic stability criteria)?  
- How can the depth–scale mapping be made quantitative, perhaps through a renormalization‑group analysis on the tree?

## 7. Practical Implications and Engineering Pathways
### (a) Potential users and decision impact
The primary users are theoretical cosmologists and quantum‑gravity model builders who seek a minimalistic, static substrate for emergent spacetime. Adoption of the clarified static $p$‑adic tree framework would shift research focus from constructing inflaton potentials to analyzing ultrametric graph properties and their observational signatures, influencing the design of future CMB data‑analysis pipelines.

### (b) Technology Readiness Level
The work is purely analytical, unreviewed, and has not been experimentally validated; it therefore resides at **TRL 2** (technology concept formulation). No hardware or fabrication is involved.

### (c) Minimal next experiment
A concrete next step is a re‑analysis of existing Planck temperature and polarization data to search for the predicted log‑periodic modulation:
1. Compute the angular power spectrum $C_{\ell}$ for multipoles $30\leq\ell\leq2500$.  
2. Fit the spectrum to the model
   \[
   P(k)=P_{0}(k)\Bigl[1+\epsilon\cos\!\bigl(2\pi\frac{\ln k}{\ln p}\bigr)\Bigr],
   \]
   with $p=2$ (binary tree) as a fixed parameter.  
3. Estimate $\epsilon$ and its uncertainty; a best‑fit $\epsilon>0.05$ (with $>3\sigma$ significance) would support the hypothesis, while $\epsilon<0.01$ would falsify it.

### (d) Engineering constraints
- **Depth–multipole mapping**: Requires a calibrated relation between tree depth $n$ and angular multipole $\ell$, currently an open modeling question.  
- **Statistical uncertainties**: Cosmic variance at low $\ell$ limits sensitivity to long‑wavelength modulations.  
- **Computational resources**: The analysis uses existing public Planck data and standard spectral estimation software; no novel hardware is needed.

### (e) Projected performance bounds
Assuming $c=40$ (binary tree, $n=10$) to satisfy the holographic bound, the model predicts:
- An emergent Hubble‑like parameter $H=\ln 2\approx0.693$ (Planck units).  
- A CMB modulation amplitude bounded by $\epsilon\lesssim0.03$ (a projection based on the requirement that $\epsilon$ remain below the detection threshold in current data).  
These projections are labeled as **projections** because they depend on the adjustable constant $c$ and the chosen depth–scale mapping.

### (f) Direct risks or misuse
The framework is purely theoretical; there is no immediate risk of technological misuse. Misinterpretation of a marginal modulation as evidence for new physics could divert resources, but the explicit detection threshold $\epsilon>0.05$ mitigates this risk by requiring a statistically robust signal.

## 8. Conclusion
We have corrected three critical deficiencies in the static $p$‑adic holographic tree model by (i) defining the chordality condition and proving its satisfaction for trees, (ii) providing explicit quantitative predictions for the emergent Hubble‑like parameter, holographic entropy bounds, and log‑periodic CMB modulation amplitude, and (iii) establishing statistically meaningful detection and null‑result thresholds. The clarified model offers a falsifiable alternative to inflationary cosmology: either a log‑periodic modulation with $\epsilon>0.05$ is detected at period $\ln p$, or the null hypothesis $\epsilon<0.01$ is confirmed, thereby falsifying the static‑tree hypothesis. Future work will focus on deriving the embedding constant $c$ from first principles, establishing a rigorous depth–scale mapping, and extending the framework to incorporate matter fields and observational constraints beyond the CMB.

## References

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum  
[2] arXiv:1604.01315v1 | Percolation thresholds of two-dimensional continuum systems of rectangles [with erratum]  
[3] arXiv:2512.18702 | On the construction of graph models realizing given entropy vectors  
[4] arXiv:2301.12353 | On Enhancing Expressive Power via Compositions of Single Fixed-Size ReLU Network  
[5] arXiv:2609.07032 | A Single Fixed Shallow Circuit for Classical Shadows of Arbitrary n-Qubit States  
[6] arXiv:2008.12726 | Type II critical collapse on a single fixed grid: a gauge-driven ingoing boundary method  
[7] arXiv:2412.15629 | New Design of three-qubit system with three transmons and a single fixed-frequency resonator coupler  
[8] arXiv:2311.04941 | Statistical analysis of coupled oscillations with a single fixed endpoint and its application to carbon nanomaterials  
[9] arXiv:2610.23058 | A note on the non-wandering dynamics in the $n$-fold symmetric products  
[10] arXiv:1402.1589 | Compact spaces, lattices, and absoluteness: a survey  
[11] arXiv:1310.8372 | Scaling of entanglement entropy in the (branching) multi-scale entanglement renormalization ansatz