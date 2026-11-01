# Static p‑Adic Holographic Tree as a Fixed Universal Structure: Corrected Detection Thresholds and Explicit Predictive Content

## Abstract

Cosmological data analysis faces a concrete decision problem: when a log‑periodic modulation of the cosmic microwave background (CMB) power spectrum is proposed as a signature of discrete hierarchical geometry, the analysis pipeline needs a stated amplitude, phase, period, and detection threshold, or the prediction cannot be tested or falsified. Earlier versions of the static p‑adic holographic tree model stated the modulation without an amplitude, phase, or uncertainty, claimed an undefined "chordality condition" was satisfied by construction, and mixed a 5% detection threshold with a 1% null‑result threshold without derivation. This paper repairs those defects. We restate the model — a rooted $p$‑ary tree with ultrametric distance $d_p(x,y)=p^{-k}$, observer worldlines as infinite paths, and one bit per node — and derive its quantities with shown arithmetic: an emergent Hubble‑like parameter $H=\ln 2\approx 0.6931$ in Planck‑time units, a depth‑10 holographic entropy bound $S_{10}^{\max}\approx 25.4$ bits against a node information content of $1024$ bits (ratio $\approx 40.3$), and a log‑periodic modulation $P(k)=P_0(k)\,[1+\epsilon\cos(2\pi\ln k/\ln p+\phi)]$ with period $\ln 2\approx 0.693$ in $\ln k$. Using the detectability result that a 3% modulation amplitude corresponds to $0.03\sigma$ on Planck data, we derive $\sigma_\epsilon\approx 0.01$, adopt $\epsilon>0.05$ as the detection threshold and $\epsilon<0.01$ as the null‑result threshold, and state that no quantitative comparison to existing CMB data is performed here. The chordality claim is withdrawn as unverified. The result changes practice by converting an unfalsifiable slogan into a parameterized fit with explicit accept, reject, and inconclusive regions.

## 1. Introduction

Cosmologists who search Planck‑class CMB data for primordial signatures face a recurring methodological failure: theoretical models are published with predictions of the form "the power spectrum shows a log‑periodic modulation," with no amplitude, no phase, no period in observational units, and no stated detection threshold. Such predictions cannot be fit, cannot be rejected, and consume analysis effort that a well‑posed prediction would either focus or release. The cost is twofold. Analysts cannot add the model to a nested‑hypothesis comparison because the model has no fixed parameter vector; and model builders receive no feedback, because a prediction without a rejection region can never fail. A prediction that states its amplitude $\epsilon$, its phase $\phi$, its period $\ln p$ in $\ln k$, and its detection and null‑result thresholds changes this: it can be added to an existing spectral pipeline as one extra fit parameter, and a single reanalysis either detects, excludes, or leaves inconclusive the entire class of binary‑tree geometries.

This paper addresses that failure for a specific model family: the static p‑adic holographic tree, in which the universe is a fixed rooted $p$‑ary tree, spacetime and its apparent dynamics are properties of observer worldlines (infinite paths in the tree), and the holographic entropy assignment is carried by the node count. The model is a candidate answer to a standing puzzle — why the universe appears to evolve when its underlying structure could be static — and it competes, at the level of observational signature, with inflationary spectra that are smooth in $\ln k$. If the model's prediction holds, a modulation with period $\ln 2\approx 0.693$ in $\ln k$ and amplitude above $0.05$ would appear in existing public CMB data, and the search for an inflaton potential would acquire a discrete‑geometry alternative to constrain. If the prediction fails at the stated thresholds, the binary‑tree hypothesis is excluded at current sensitivity, which is itself a usable result.

Three defects in the prior version of this model are corrected here, and each correction is carried through the derivations:

1. **Detection threshold.** The prior text used a detection threshold of $\epsilon>0.01$ in one place and a 5% threshold in another. We derive the observational uncertainty $\sigma_\epsilon\approx 0.01$ from the detectability analysis of the Page‑Wootters synthesis literature [6], adopt $\epsilon>0.05$ as the detection threshold for a $>3\sigma$ claim, and adopt $\epsilon<0.01$ as the null‑result threshold (Section 4.5, Section 7).
2. **Predictive content.** The prediction is now stated with an amplitude parameter $\epsilon$, a phase $\phi$ that the model leaves free, a period $\ln p$, and an explicit statement that no quantitative comparison to existing CMB data is performed in this paper (Sections 3.5, 4.5, 6).
3. **Chordality claim.** The prior text asserted that the tree "satisfies this condition by construction" for a chordality condition governing when tree graphs can realize prescribed holographic entropy vectors. That condition is not defined, proved, or cited anywhere in the present grounding, so the claim is withdrawn: realizing holographic entropy vectors on the p‑adic tree remains an open requirement, not a construction (Section 6).

**Contributions.**

- A restatement of the static p‑adic holographic tree, its ultrametric distance, and its observer worldlines, with the emergent scale factor and Hubble‑like parameter $H=\ln p/\lambda$ derived with shown arithmetic (Sections 3, 4).
- A corrected entropy calculation at depth $n=10$: $S_{10}^{\max}\approx 25.4$ bits against $I_{10}=1024$ bits, with the mismatch factor $40.3$ computed explicitly and the embedding constant $c\approx 40.3$ treated as an assumption, not a result (Section 4).
- A fully parameterized log‑periodic prediction $P(k)=P_0(k)\,[1+\epsilon\cos(2\pi\ln k/\ln p+\phi)]$ with derived uncertainty $\sigma_\epsilon\approx 0.01$, detection threshold $\epsilon>0.05$, and null‑result threshold $\epsilon<0.01$ (Section 4.5).
- An explicit falsification criterion and a limitations list that includes the no‑go constraint, proved in the Page‑Wootters synthesis literature, that conditional clock‑state distances are not ultrametric except in trivial cases — a direct structural threat to the observer model used here (Section 6).
- A practical pathway: a proposed reanalysis of public Planck temperature and polarization data fitting $\epsilon$ and $\phi$ with the stated thresholds, writable as a sub‑hour analysis on existing software (Section 7).

## 2. Background and Related Work

This section positions the model against six works. Because the available literature for this revision contains six entries rather than the eight or more a full survey would use, the coverage below is complete with respect to what is available but narrower than a general review of holographic cosmology; this limitation is restated in Section 6.

Degree‑regular trees have sharp extremal index bounds, and these bounds constrain what a "generic" node‑degree profile of a hierarchical tree looks like. For trees with a given number $n$ of pendent (leaf) vertices, the first Zagreb index satisfies $M_1(T)\geq 9n-16$ for even $n$, with equality exactly for $4$‑trees in which every internal vertex has degree $4$, and $M_1(T)\geq 9n-15$ for odd $n$ [1]. The second Zagreb index satisfies $M_2(T)\geq 11n-27$ for $n\geq 8$, with equality when each stem vertex has degree $4$ or $5$ and the remaining internal vertices have degree $3$ [1]. The relevance to the present model is a consistency check on branching: the $p$‑ary tree used here is degree‑regular by construction, and results of this type show that degree regularity is the extremal, boundary case of the space of trees, not a generic member of it. Any claim that the p‑adic tree is "typical" among hierarchical geometries should therefore be treated with caution; regularity is a special structure, which is precisely what makes its predictions sharp.

Continuum thresholds can be extracted from discrete randomized structures with controlled algorithms, and the percolation literature demonstrates the workflow this paper's proposed CMB test imitates. For two‑dimensional continuum systems of randomly oriented rectangles, an efficient Monte Carlo algorithm — combining a fast union‑find update in which each cluster is stored in a tree structure, with a subcell registration scheme that limits connectivity checks to neighboring subcells — yields high‑precision percolation thresholds across aspect ratios, and the results verify and extend excluded‑area theory through a high‑order polynomial in excluded‑area reciprocals that predicts thresholds for homogeneous systems [2]. The methodological parallel is direct: a discrete combinatorial substrate (here, the tree; there, the rectangle system) supports a continuum observable (a percolation threshold; here, a spectral modulation) whose value can be estimated to stated precision by a fixed analysis pipeline on existing hardware. The percolation case also illustrates the discipline this paper previously lacked: thresholds are reported with uncertainties and against a quantitative theory, not as qualitative statements.

Ultrametric geometry changes information‑theoretic tradeoffs in ways that Archimedean analysis does not anticipate, and one published no‑go result bears directly on the information assignment used here. In the quantum‑error‑correction versus Quantum Darwinism setting, the Archimedean theorem of Maity et al. establishes that if the bare fidelity satisfies $F_{\text{bare}}>H_2^{-1}[(1-\delta)\ln 2]$ then no environment fragment can satisfy the Darwinism criterion, via the chain $(1-\delta)\ln 2\leq\chi(F)\leq\chi(E)\leq S(\rho_E)=S(\rho_B)\leq H_2(F_{\text{bare}})$, with the practical threshold that the two functions cannot coexist above logical fidelity $F_L>0.874$ [3]. When the same problem is embedded in an ultrametric space, the continuous redundancy function is replaced by a discrete staircase in which redundancy changes only when the information‑spreading radius advances by one tree level [3]. This quantization is the same mechanism that produces the discrete depth‑indexed entropy of Section 3.4, and it warns that any continuous‑looking quantity derived on the tree is a coarse‑grained projection of a stepwise underlying quantity.

The identification of the Bruhat–Tits tree with p‑adic anti‑de Sitter space provides the strongest existing precedent for the entropy scaling used in this model. The Bruhat–Tits tree $\mathcal{T}_p$ is an infinite $(p+1)$‑regular tree, a discrete analog of the hyperbolic plane with curvature $\sim-\log p$, homogeneous under $\mathrm{PGL}(2,\mathbb{Q}_p)$, with boundary $\partial\mathcal{T}_p=\mathbb{P}^1(\mathbb{Q}_p)$ [4]. On this geometry the Ryu–Takayanagi minimal surface is a vertex cut at depth $\operatorname{ord}_p(L)$ and the holographic entanglement entropy scales as $S_{\text{EE}}(L)\propto\operatorname{ord}_p(L)\cdot\log p$ [4]. That result — entropy proportional to depth times $\log p$ — is the structural cousin of the node‑count and area estimates of Section 3.4, and it supplies the interpretation of $\ln p$ as an entropy increment per level rather than an arbitrary parameter. The same work frames tensor networks on $\mathcal{T}_p$ as holographic quantum error‑correcting codes with the tree interior as bulk and the tree boundary as the conformal boundary [4], which is the setting in which any eventual derivation of the embedding constant $c$ of Section 3.4 would have to live.

Emergent time and emergent light speed from a static tree have been derived formally, establishing that the "static substrate, dynamic observers" move used here has an existing derivation template. In the Bruhat–Tits derivation of emergent spacetime, the tree's adjacency operator $A$ serves as the effective Hamiltonian within a rigged Hilbert space, time emerges as an epistemic coarse‑grained parameter via the Page‑Wootters mechanism, a causal light‑cone structure arises from Lieb–Robinson bounds, and the dimensionless upper bound on the speed of light is the Lieb–Robinson velocity derived from the spectral radius of the tree [5]. This matters for the present model in two ways. First, it shows the mapping $\tau\mapsto t$ of Section 3.2 need not be an unexplained postulate: the Page‑Wootters conditioning provides the mechanism by which a static structure yields sequential observation. Second, the spectral‑radius derivation of a physical constant shows how a dimensionless number like $H=\ln p$ could in principle be tied to a measured quantity rather than left as a tree‑time artifact.

The convergent synthesis literature supplies both the detectability numbers used in this revision and a no‑go theorem that constrains the observer model. The synthesis chain runs from a radix $p$ through the p‑adic numbers $\mathbb{Q}_p$, the ultrametric $d_p(x,y)=|x-y|_p$, tree hierarchy, and Bruhat–Tits buildings, with the Wheeler–DeWitt equation $H|\Psi\rangle=0$ eliminating external time and Page‑Wootters conditioning producing clock states whose correlation structure is conjectured to be ultrametric [6]. Two results from that work are used quantitatively here. First, its CMB detectability analysis reports that a 3% p‑adic amplitude in simulated Planck data corresponds to $0.03\sigma$ and is undetectable, and that the signal must exceed 5% for Planck detection, with public Planck data enabling an analysis of under one hour [6]; Section 4.5 derives $\sigma_\epsilon\approx 0.01$ from the first pair of numbers and adopts the 5% threshold. Second, its formal no‑go theorem proves that for any finite‑dimensional real energy spectrum with non‑negative weights, the Page‑Wootters conditional state distance $d(\tau_1,\tau_2)=1-\bigl|\sum_n w_n e^{-iE_n(\tau_1-\tau_2)}\bigr|$ is not strictly ultrametric for all $\tau_1,\tau_2$ unless the clock is trivial (one state, or all energies equal), because a non‑constant ultrametric on the connected space $\mathbb{R}$ would require clopen balls, of which $\mathbb{R}$ has none [6]. The same work reports that a $D=4$ Fourier‑clock construction was falsified by its own distance spectrum, which had 29 distinct values for $N=30$ states [6]. This no‑go theorem is carried as a structural limitation in Section 6: the observer worldlines of the present model live on the tree and inherit its ultrametric, but the conditional states that would define an observer's clock are provably non‑ultrametric in any non‑trivial Archimedean parametrization, so the reconciliation of the two is an open problem, not a solved step.

## 3. Methods

### 3.1 Definition of the static p‑adic tree

Let $p\geq 2$ be a fixed prime. Define the set of finite strings over the alphabet $\{0,1,\dots,p-1\}$:

$$
\mathcal{S}=\bigcup_{n=0}^{\infty}\{0,1,\dots,p-1\}^{n},
$$

with the empty string $\epsilon$ as the root at depth $0$. For $x\in\mathcal{S}$ with $|x|=n$, the children of $x$ are the $p$ strings $x\alpha$, $\alpha\in\{0,\dots,p-1\}$; the edge set is $\{\{x,x\alpha\}\}$. The ultrametric distance between nodes $x,y$ is

$$
d_{p}(x,y)=p^{-k},
$$

where $k$ is the length of the longest common prefix of $x$ and $y$ ($k=0$ if the first symbols differ). This satisfies the strong triangle inequality $d_p(x,z)\leq\max\{d_p(x,y),d_p(y,z)\}$ and is a tree metric. The structure is the rooted, regular $p$‑ary subtree of the Bruhat–Tits tree $\mathcal{T}_p$, which is $(p+1)$‑regular and carries curvature $\sim-\log p$ [4]; the rooted $p$‑ary version is the causal cone below a chosen boundary ray, which is the object an observer worldline naturally spans.

### 3.2 Observer worldlines and proper time

An observer is an infinite directed path $\gamma=\{x_0,x_1,x_2,\dots\}$ with $x_0=\epsilon$ and $x_{n+1}=x_n\alpha_n$. The discrete proper time after $n$ steps is

$$
\tau=n,
$$

mapped to continuous cosmic time by $t=\lambda\,\tau$, where $\lambda$ is a conversion factor with dimensions of time. We assume $\lambda$ is constant; its physical value is unknown and is carried as a limitation in Section 6. The mechanism by which a static structure yields sequential observation is not postulated here but inherited: in the Bruhat–Tits derivation of emergent spacetime, the adjacency operator acts as an effective Hamiltonian and time is an epistemic, coarse‑grained parameter produced by Page–Wootters conditioning [5]. Section 6 records the no‑go theorem that constrains that conditioning [6].

### 3.3 Emergent scale factor and Hubble‑like parameter

Define the effective scale factor as the number of distinct nodes reachable within proper time $\tau$:

$$
a(t)=N_{\tau}=p^{\tau}=p^{t/\lambda}.
$$

Differentiating,

$$
\dot{a}(t)=\frac{d}{dt}\,p^{t/\lambda}=p^{t/\lambda}\,\frac{\ln p}{\lambda}=a(t)\,\frac{\ln p}{\lambda},
$$

so the emergent Hubble‑like parameter is

$$
H\equiv\frac{\dot{a}}{a}=\frac{\ln p}{\lambda}.
$$

With the assumption $\lambda=1$ (one tree step per Planck time), $H=\ln p$ in Planck units. The interpretation of $\ln p$ as a physical increment is supported by the p‑adic AdS correspondence, in which the entanglement entropy per tree level scales as $\log p$ [4].

### 3.4 Holographic information content and entropy bound

Assign one bit to each node. The total information up to depth $n$ is

$$
I_{n}=p^{n}\ \text{bits}.
$$

The maximal entropy of a spherical region of radius $R_n$ obeys $S_n\leq A_n/4G$. We model the boundary area as proportional to the leaf count raised to the $2/3$ power, reflecting a three‑dimensional embedding:

$$
A_{n}=c\,p^{\frac{2n}{3}},
$$

with $c$ a dimensionless constant of order unity, and $G=1$ in Planck units, giving

$$
S_{n}^{\max}=\frac{c}{4}\,p^{\frac{2n}{3}}.
$$

Two honesty notes attach to this subsection. The one‑bit‑per‑node assignment is a simplification; the ultrametric QEC literature shows that information on such trees is organized in discrete redundancy steps rather than as a uniform per‑node budget [3]. And the factor $p^{2n/3}$ is an embedding ansatz, not a derivation; the natural entropy variable on the Bruhat–Tits tree is depth times $\log p$ [4], and reconciling the two is open. The constant $c$ is treated throughout as an adjustable geometric parameter, and the value $c\approx 40.3$ derived in Section 4.4 is an assumption required for consistency, not a prediction.

### 3.5 The log‑periodic prediction, stated with its parameters

The ultrametric distance satisfies $d_p(p\,\Delta)=p\cdot p^{-k'}$ structure invariance under rescaling of separations by powers of $p$; consequently any two‑point correlation $C(\Delta)$ defined on the tree obeys $C(p\,\Delta)=C(\Delta)$. In Fourier space this implies the ansatz

$$
P(k)=P_{0}(k)\left[1+\epsilon\cos\!\left(2\pi\frac{\ln k}{\ln p}+\phi\right)\right],
$$

with four stated ingredients:

- **Amplitude** $\epsilon$: dimensionless fractional modulation, the single free physical parameter of the model.
- **Phase** $\phi$: not fixed by the model; the tree construction determines the period but not the phase of the modulation, so $\phi$ is a free fit parameter and any measured nonzero $\phi$ is unexplained by the model (Section 6).
- **Period** $\ln p$: for $p=2$, the period in $\ln k$ is $\ln 2\approx 0.693$.
- **Observational uncertainty** $\sigma_\epsilon\approx 0.01$, derived in Section 4.5 from the detectability analysis of [6].

No quantitative comparison to existing CMB data is performed in this paper. The prediction is stated so that such a comparison can be performed by others; the proposed analysis is specified in Section 7.

## 4. Analysis

### 4.1 Node count at finite depth

For $p=2$, depth $n=5$:

$$
N_{5}=2^{5}=32,
$$

with the intermediate values $2^{1}=2$, $2^{2}=4$, $2^{3}=8$, $2^{4}=16$, $2^{5}=32$. At depth $n=10$:

$$
N_{10}=2^{10}=1024.
$$

### 4.2 Effective Hubble parameter for $p=2$

With $\lambda=1$,

$$
H=\ln 2.
$$

Evaluating: $\ln 2=0.69314718056$ (standard value of the natural logarithm of 2). To the precision the model supports,

$$
H\approx 0.6931\ \text{(Planck‑time units)}.
$$

### 4.3 Holographic entropy bound at depth $n=10$

For $p=2$, $n=10$, the information content is

$$
I_{10}=2^{10}=1024\ \text{bits}.
$$

The area estimate requires $2^{20/3}$. Split the exponent:

$$
2^{20/3}=2^{6}\cdot 2^{2/3}.
$$

Compute each factor. $2^{6}=64$. For $2^{2/3}$: $2^{2}=4$, and $\sqrt[3]{4}=1.587401$ (since $1.587401^{3}=4.0000$ to six digits: $1.587401^{2}=2.519842$, and $2.519842\times1.587401=4.000000$). Therefore

$$
2^{20/3}=64\times 1.587401=101.5937.
$$

With the assumption $c=1$,

$$
S_{10}^{\max}=\frac{1}{4}\times 101.5937=25.3984\ \text{bits}\approx 25.4\ \text{bits}.
$$

### 4.4 Information‑to‑bound ratio and the embedding constant

The ratio of node information to the holographic bound at $c=1$ is

$$
\frac{I_{10}}{S_{10}^{\max}}=\frac{1024}{25.3984}=40.317.
$$

Arithmetic: $25.3984\times 40=1015.936$; $1024-1015.936=8.064$; $8.064/25.3984=0.3174$; total $40.317$. The raw node count therefore exceeds the $c=1$ holographic bound by a factor of $\approx 40.3$. Equality requires

$$
c=\frac{4\,I_{10}}{2^{20/3}}=\frac{4096}{101.5937}=40.317,
$$

so the consistency value is $c\approx 40.3$. This is stated as an assumption about the embedding geometry, not a derived result; Section 6 lists what a derivation of $c$ would require.

### 4.5 Detection and null‑result thresholds for the log‑periodic signature

The detectability analysis of the Page–Wootters synthesis work states two