# Static p‑Adic Holographic Tree as a Fixed Universal Structure: Chordality, Explicit Predictions, and Detection Thresholds

## Abstract

Cosmological data analysis faces a concrete decision problem: when a log‑periodic modulation of the cosmic microwave background (CMB) power spectrum is proposed as a signature of discrete hierarchical geometry, the analysis pipeline needs a stated amplitude, phase, period, and detection threshold, or the prediction cannot be tested or falsified. Earlier statements of the static p‑adic holographic tree model gave the modulation without an amplitude or uncertainty, invoked an undefined chordality condition, and mixed detection with null‑result thresholds without derivation. This paper repairs those defects. We restate the model — a rooted $p$‑ary tree with ultrametric distance $d_p(x,y)=p^{-k}$, observer worldlines as infinite paths, and one bit per node — and derive its quantities with shown arithmetic: an emergent Hubble‑like parameter $H=\ln 2\approx 0.6931$ in Planck‑time units, a depth‑10 holographic entropy bound $S_{10}^{\max}\approx 25.4$ bits against a node information content of $1024$ bits (ratio $\approx 40.3$), and a log‑periodic modulation $P(k)=P_0(k)\,[1+\epsilon\cos(2\pi\ln k/\ln p+\phi)]$ with period $\ln 2\approx 0.693$ in $\ln k$. From the detectability analysis of the Page–Wootters synthesis literature we adopt $\sigma_\epsilon\approx 0.01$, a detection threshold $\epsilon>0.05$, and a null‑result threshold $\epsilon<0.01$; no quantitative comparison to existing CMB data is performed here. The chordality realization claim is downgraded to an open requirement. The result converts an unfalsifiable slogan into a parameterized fit with explicit accept, reject, and inconclusive regions.

## 1. Introduction

Cosmologists who search Planck‑class CMB data for primordial signatures face a recurring methodological failure: theoretical models are published with predictions of the form "the power spectrum shows a log‑periodic modulation," with no amplitude, no phase, no period in observational units, and no stated detection threshold. Such predictions cannot be fit, cannot be rejected, and consume analysis effort that a well‑posed prediction would either focus or release. The cost is twofold. Analysts cannot add the model to a nested‑hypothesis comparison because the model has no fixed parameter vector; and model builders receive no feedback, because a prediction without a rejection region can never fail. A prediction that states its amplitude $\epsilon$, its phase $\phi$, its period $\ln p$ in $\ln k$, and its detection and null‑result thresholds changes this: it can be added to an existing spectral pipeline as one extra fit parameter, and a single reanalysis either detects, excludes, or leaves inconclusive the entire class of binary‑tree geometries.

This paper addresses that failure for a specific model family: the static p‑adic holographic tree, in which the universe is a fixed rooted $p$‑ary tree, spacetime and its apparent dynamics are properties of observer worldlines (infinite paths in the tree), and the holographic entropy assignment is carried by the node count. The model is a candidate answer to a standing puzzle — why the universe appears to evolve when its underlying structure could be static — and it competes, at the level of observational signature, with inflationary spectra that are smooth in $\ln k$. If the model's prediction holds, a modulation with period $\ln 2\approx 0.693$ in $\ln k$ and amplitude above $0.05$ would appear in existing public CMB data, and the search for an inflaton potential would acquire a discrete‑geometry alternative to constrain. If the prediction fails at the stated thresholds, the binary‑tree hypothesis is excluded at current sensitivity, which is itself a usable result.

Three defects in prior statements of this model are corrected here, and each correction is carried through the derivations:

1. **Detection threshold.** The detectability figures of the Page–Wootters synthesis work [6], together with an explicitly stated assumption on the amplitude uncertainty, are used to fix the thresholds; the derivation, including the assumption under which it holds, is given in Section 4.5 and applied in Section 7.
2. **Predictive content.** The prediction is stated with an amplitude parameter $\epsilon$, a phase $\phi$ that the model leaves free, a period $\ln p$, and an explicit statement that no quantitative comparison to existing CMB data is performed in this paper (Sections 3.5, 4.5, 6).
3. **Chordality claim.** The graph‑theoretic chordality condition is stated precisely, and its status for the present construction is resolved under an explicit convention: trees are vacuously chordal, but realizing the holographic entropy vectors of [3] on the p‑adic tree remains an open requirement, not a construction (Section 3.2, Section 6).

**Contributions.**

- A restatement of the static p‑adic holographic tree, its ultrametric distance, and its observer worldlines, with the emergent scale factor and Hubble‑like parameter $H=\ln p/\lambda$ derived with shown arithmetic (Sections 3, 4).
- A corrected entropy calculation at depth $n=10$: $S_{10}^{\max}\approx 25.4$ bits against $I_{10}=1024$ bits, with the mismatch factor $40.3$ computed explicitly and the embedding constant $c\approx 40.3$ treated as an assumption, not a result (Section 4).
- A fully parameterized log‑periodic prediction $P(k)=P_0(k)\,[1+\epsilon\cos(2\pi\ln k/\ln p+\phi)]$ with adopted uncertainty $\sigma_\epsilon\approx 0.01$, detection threshold $\epsilon>0.05$, and null‑result threshold $\epsilon<0.01$ (Section 4.5).
- An explicit falsification criterion and a limitations list that includes the no‑go constraint proved in [6], that conditional clock‑state distances are not ultrametric except in trivial cases — a direct structural threat to the observer model used here (Section 6).
- A practical pathway: a proposed reanalysis of public Planck temperature and polarization data fitting $\epsilon$ and $\phi$ with the stated thresholds (Section 7).

## 2. Background and Related Work

Degree‑regular trees have sharp extremal index bounds, and these bounds constrain what a "generic" node‑degree profile of a hierarchical tree looks like. For trees with a given number $n$ of pendent (leaf) vertices, the first Zagreb index satisfies $M_1(T)\geq 9n-16$ for even $n$, with equality exactly for $4$‑trees in which every internal vertex has degree $4$, and $M_1(T)\geq 9n-15$ for odd $n$; the second Zagreb index satisfies $M_2(T)\geq 11n-27$ for $n\geq 8$, with equality when each stem vertex has degree $4$ or $5$ and the remaining internal vertices have degree $3$ [1]. The relevance to the present model is a consistency check on branching: the $p$‑ary tree used here is degree‑regular by construction, and results of this type show that degree regularity is the extremal, boundary case of the space of trees, not a generic member of it. Any claim that the p‑adic tree is "typical" among hierarchical geometries should therefore be treated with caution; regularity is a special structure, which is precisely what makes its predictions sharp.

Continuum thresholds can be extracted from discrete randomized structures with controlled algorithms, and the percolation literature demonstrates the workflow this paper's proposed CMB test imitates. For two‑dimensional continuum systems of randomly oriented rectangles, an efficient Monte Carlo algorithm — combining a fast union‑find update in which each cluster is stored in a tree structure, with a subcell registration scheme that limits connectivity checks to neighboring subcells — yields high‑precision percolation thresholds across aspect ratios, and the results verify and extend excluded‑area theory through a high‑order polynomial in excluded‑area reciprocals that predicts thresholds for homogeneous systems [2]. The methodological parallel is direct: a discrete combinatorial substrate (here, the tree; there, the rectangle system) supports a continuum observable (a percolation threshold; here, a spectral modulation) whose value can be estimated to stated precision by a fixed analysis pipeline on existing hardware. The percolation case also supplies the discipline this model previously lacked: thresholds are reported with uncertainties and against a quantitative theory, not as qualitative statements.

Ultrametric geometry changes information‑theoretic tradeoffs in ways that Archimedean analysis does not anticipate, and one published no‑go result bears directly on the information assignment used here. In the quantum‑error‑correction versus Quantum Darwinism setting, the Archimedean theorem reported there establishes that if the bare fidelity satisfies $F_{\text{bare}}>H_2^{-1}[(1-\delta)\ln 2]$ then no environment fragment can satisfy the Darwinism criterion, via the chain $(1-\delta)\ln 2\leq\chi(F)\leq\chi(E)\leq S(\rho_E)=S(\rho_B)\leq H_2(F_{\text{bare}})$, with the practical threshold that the two functions cannot coexist above logical fidelity $F_L>0.874$ [3]. When the same problem is embedded in an ultrametric space, the continuous redundancy function is replaced by a discrete staircase in which redundancy changes only when the information‑spreading radius advances by one tree level [3]. This quantization is the same mechanism that produces the discrete depth‑indexed entropy of Section 3.4, and it warns that any continuous‑looking quantity derived on the tree is a coarse‑grained projection of a stepwise underlying quantity.

The identification of the Bruhat–Tits tree with p‑adic anti‑de Sitter space provides the strongest existing precedent for the entropy scaling used in this model. The Bruhat–Tits tree $\mathcal{T}_p$ is an infinite $(p+1)$‑regular tree, a discrete analog of the hyperbolic plane with curvature $\sim-\log p$, homogeneous under $\mathrm{PGL}(2,\mathbb{Q}_p)$, with boundary $\partial\mathcal{T}_p=\mathbb{P}^1(\mathbb{Q}_p)$ [4]. On this geometry the Ryu–Takayanagi minimal surface is a vertex cut at depth $\operatorname{ord}_p(L)$ and the holographic entanglement entropy scales as $S_{\text{EE}}(L)\propto\operatorname{ord}_p(L)\cdot\log p$ [4]. That result — entropy proportional to depth times $\log p$ — is the structural cousin of the node‑count and area estimates of Section 3.4, and it supplies the interpretation of $\ln p$ as an entropy increment per level rather than an arbitrary parameter. The same work frames tensor networks on $\mathcal{T}_p$ as holographic quantum error‑correcting codes with the tree interior as bulk and the tree boundary as the conformal boundary [4], which is the setting in which any eventual derivation of the embedding constant $c$ of Section 3.4 would have to live.

Emergent time and emergent light speed from a static tree have been derived formally, establishing that the "static substrate, dynamic observers" move used here has an existing derivation template. In the Bruhat–Tits derivation of emergent spacetime, the tree's adjacency operator $A$ serves as the effective Hamiltonian within a rigged Hilbert space, time emerges as an epistemic coarse‑grained parameter via the Page–Wootters mechanism, a causal light‑cone structure arises from Lieb–Robinson bounds, and the dimensionless upper bound on the speed of light is the Lieb–Robinson velocity derived from the spectral radius of the tree [5]. This matters for the present model in two ways. First, it shows the mapping $\tau\mapsto t$ of Section 3.2 need not be an unexplained postulate: the Page–Wootters conditioning provides the mechanism by which a static structure yields sequential observation. Second, the spectral‑radius derivation of a physical constant shows how a dimensionless number like $H=\ln p$ could in principle be tied to a measured quantity rather than left as a tree‑time artifact.

The convergent synthesis literature supplies both the detectability numbers used in this paper and a no‑go theorem that constrains the observer model. The synthesis chain runs from a radix $p$ through the p‑adic numbers $\mathbb{Q}_p$, the ultrametric $d_p(x,y)=|x-y|_p$, tree hierarchy, and Bruhat–Tits buildings, with the Wheeler–DeWitt equation $H|\Psi\rangle=0$ eliminating external time and Page–Wootters conditioning producing clock states whose correlation structure is conjectured to be ultrametric [6]. Two results from that work are used quantitatively here. First, its CMB detectability analysis reports that a 3% p‑adic amplitude in simulated Planck data lies at the edge of detectability and that the signal must exceed 5% for Planck detection, with public Planck data enabling an analysis of under one hour [6]; Section 4.5 adopts the 5% threshold and derives $\sigma_\epsilon\approx 0.01$ under an explicitly stated reading of the significance figure. Second, its formal no‑go theorem proves that for any finite‑dimensional real energy spectrum with non‑negative weights, the Page–Wootters conditional state distance $d(\tau_1,\tau_2)=1-\bigl|\sum_n w_n e^{-iE_n(\tau_1-\tau_2)}\bigr|$ is not strictly ultrametric for all $\tau_1,\tau_2$ unless the clock is trivial (one state, or all energies equal), because a non‑constant ultrametric on the connected space $\mathbb{R}$ would require clopen balls, of which $\mathbb{R}$ has none [6]. The same work reports that a $D=4$ Fourier‑clock construction was falsified by its own distance spectrum, which had 29 distinct values for $N=30$ states [6]. This no‑go theorem is carried as a structural limitation in Section 6: the observer worldlines of the present model live on the tree and inherit its ultrametric, but the conditional states that would define an observer's clock are provably non‑ultrametric in any non‑trivial Archimedean parametrization, so the reconciliation of the two is an open problem, not a solved step.



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

### 3.2 Chordality condition

A graph is chordal if every cycle of length greater than three possesses a chord, an edge joining two non‑consecutive vertices of the cycle. We take this graph‑theoretic definition, under the convention that vacuous satisfaction by acyclic graphs counts as satisfaction: a tree contains no cycles, so the condition holds for the p‑adic tree trivially. Whether this definition coincides with the condition under which the graph models of [3] realize prescribed holographic entropy vectors is not established by the present analysis; accordingly, realizing holographic entropy vectors on the p‑adic tree is treated throughout this paper as an open requirement, not as a construction. This convention is stated here because it governs the entropy assignment of Section 3.4.

### 3.3 Observer worldlines and proper time

An observer is an infinite directed path $\gamma=\{x_0,x_1,x_2,\dots\}$ with $x_0=\epsilon$ and $x_{n+1}=x_n\alpha_n$. The discrete proper time after $n$ steps is

$$
\tau=n,
$$

mapped to continuous cosmic time by $t=\lambda\,\tau$, where $\lambda$ is a conversion factor with dimensions of time. We assume $\lambda$ is constant; its physical value is unknown and is carried as a limitation in Section 6. The mechanism by which a static structure yields sequential observation is not postulated here but inherited: in the Bruhat–Tits derivation of emergent spacetime, the adjacency operator acts as an effective Hamiltonian and time is an epistemic, coarse‑grained parameter produced by Page–Wootters conditioning [5]. Section 6 records the no‑go theorem that constrains that conditioning [6].

### 3.4 Emergent scale factor and Hubble‑like parameter

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

### 3.5 Holographic information content and entropy bound

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

### 3.6 The log‑periodic prediction, stated with its parameters

The ultrametric distance is invariant under rescaling of separations by powers of $p$: if two nodes share a longest common prefix of length $k$, their distance is $p^{-k}$ regardless of the absolute depth scale, so any two‑point correlation $C(\Delta)$ defined on the tree obeys $C(p\,\Delta)=C(\Delta)$. In Fourier space this implies the ansatz

$$
P(k)=P_{0}(k)\left[1+\epsilon\cos\!\left(2\pi\frac{\ln k}{\ln p}+\phi\right)\right],
$$

with four stated ingredients:

with four stated ingredients:

1. **Baseline spectrum** $P_{0}(k)$, the smooth power spectrum that would be fit in the absence of the tree; the model does not predict $P_{0}(k)$ and treats it as a nuisance function.
2. **Amplitude** $\epsilon$, the fractional modulation depth; this is the single parameter the proposed reanalysis of Section 7 fits, and the quantity to which the detection and null‑result thresholds of Section 4.5 attach.
3. **Phase** $\phi$, the offset of the cosine in $\ln k$; the model as stated leaves $\phi$ free, so a detection requires fitting two parameters $(\epsilon,\phi)$, and the effective significance penalty of one extra fitted parameter is carried in the thresholds of Section 4.5.
4. **Period** $\ln p$ in $\ln k$: for $p=2$ the modulation completes one full cycle per factor‑of‑two change in $k$, so the pattern is self‑similar under $k\mapsto 2k$.

The prediction is stated here as a fit template only. No quantitative comparison to existing CMB data is performed in this paper; the numbers in Section 4.5 are thresholds derived from the detectability analysis of [6], not fit results.

## 4. Analysis

### 4.1 Node counts at finite depth

For a $p$‑ary tree, the number of nodes at depth $n$ is $p^{n}$ and the total number of nodes up to and including depth $n$ is

$$
N_{\text{tot}}(n)=\sum_{j=0}^{n}p^{j}=\frac{p^{n+1}-1}{p-1}.
$$

For $p=2$, $n=5$: $N_{5}=2^{5}=32$, with the intermediate powers $2^{1}=2$, $2^{2}=4$, $2^{3}=8$, $2^{4}=16$, $2^{5}=32$. For $p=2$, $n=10$: $N_{10}=2^{10}=1024$, and the total node count is

$$
N_{\text{tot}}(10)=\frac{2^{11}-1}{2-1}=2047.
$$

The one‑bit‑per‑node assignment of Section 3.5 therefore gives a depth‑10 shell information of $I_{10}=1024$ bits and a cumulative information of $2047$ bits; the shell figure is the one compared against the holographic bound below, because the bound is set by a boundary area, not a volume.

### 4.2 Effective Hubble parameter for $p=2$

With the assumption $\lambda=1$ (one tree step per Planck time), Section 3.4 gives

$$
H=\frac{\ln p}{\lambda}=\ln 2.
$$

Evaluating the natural logarithm, $\ln 2=0.693147\ldots$, so

$$
H\approx 0.6931
$$

in Planck‑time units. This is a derived consequence of the definitions, not an independent prediction: any change in $p$ rescales $H$ as $\ln p$, and any change in the assumed conversion $\lambda$ rescales it as $1/\lambda$. The number is quoted because it is the model's expansion rate in the only unit system in which the derivation fixes it.

### 4.3 Holographic entropy bound at depth $n=10$

Section 3.5 gives $S_{n}^{\max}=\frac{c}{4}\,p^{2n/3}$ with $G=1$. For $p=2$, $n=10$:

$$
S_{10}^{\max}=\frac{c}{4}\,2^{20/3}.
$$

Step 1: split the exponent, $2^{20/3}=2^{6}\cdot 2^{2/3}$. Step 2: $2^{6}=64$. Step 3: $2^{2/3}=\sqrt[3]{4}$. Evaluating the cube root, $\sqrt[3]{4}=1.5874011\ldots$, since $1.5874^{3}=4.0000$ to the shown precision ($1.5874^{2}=2.51984$; $2.51984\times1.5874=4.0001$). Step 4:

$$
2^{20/3}=64\times 1.5874011=101.5937.
$$

Step 5, with the assumption $c=1$:

$$
S_{10}^{\max}=\frac{101.5937}{4}=25.3984\approx 25.4\ \text{bits}.
$$

The value $25.4$ bits is therefore conditional on $c=1$; the general result is $S_{10}^{\max}=25.3984\,c$ bits.

### 4.4 Comparison ratio and the embedding constant

The ratio of shell information to the $c=1$ holographic bound is

$$
\frac{I_{10}}{S_{10}^{\max}}=\frac{1024}{25.3984}=40.317\approx 40.3.
$$

Arithmetic check: $25.3984\times 40=1015.94$; $25.3984\times40.3=1023.56$; $25.3984\times40.32=1024.06$, so the ratio is $40.32$ to the shown precision, quoted as $40.3$. The raw node count at depth 10 exceeds the $c=1$ holographic bound by a factor of about $40$. Equality would require

$$
c=\frac{4\,I_{10}}{2^{20/3}}=\frac{4096}{101.5937}=40.317,
$$

so the consistency value is $c\approx 40.3$. Throughout this paper $c\approx 40.3$ is treated as an **assumption** required for internal consistency, not a result: no derivation of $c$ from the Bruhat–Tits geometry is given here, and Section 3.5 records that the natural entropy variable on that geometry is depth times $\log p$ [4], a scaling whose reconciliation with the $p^{2n/3}$ ansatz is open.

### 4.5 Detection and null‑result thresholds

The detectability analysis of [6] reports three figures for simulated Planck data: a 3% p‑adic amplitude lies at the edge of detectability, the signal must exceed 5% for Planck detection, and the analysis of public Planck data takes under one hour. These figures do not by themselves fix an amplitude uncertainty; we therefore adopt an explicit assumption and state the thresholds as conditional on it.

**Assumption.** We assume, for definiteness, that a 3% modulation sits at the $3\sigma$ edge of detectability, i.e. an amplitude of $0.03$ corresponds to the detection‑significance boundary. Under this assumption the $1\sigma$ uncertainty on the fitted amplitude is

$$
\sigma_{\epsilon}\approx 0.01.
$$

This is an assumption of this paper, not a figure derived from [6]; the alternative literal reading, in which the 3% amplitude has significance $0.03\sigma$ and $\sigma_{\epsilon}=1$, is carried alongside in Section 6.1.

Consistency checks of the assumption against the other two figures of [6]: with $\sigma_{\epsilon}=0.01$, a 5% amplitude corresponds to $0.05/0.01=5\sigma$, which exceeds the standard $3\sigma$ detection criterion and matches the statement that the signal must exceed 5% for Planck detection; and a 3% amplitude at $3\sigma$ is indeed "at the edge" of detectability rather than clearly detected, matching the reported status. The three figures of [6] are mutually consistent under this single reading, which is the reason the assumption is adopted.

**Thresholds.** With $\sigma_{\epsilon}\approx 0.01$:

- **Detection threshold:** $\epsilon>0.05$. A fitted amplitude above $0.05$ corresponds to a significance above $5\sigma$, clearing the $3\sigma$ criterion with margin for the extra fitted phase parameter $\phi$.
- **Null‑result threshold:** $\epsilon<0.01$. A fitted amplitude below $0.01$ lies below $1\sigma$; the binary‑tree modulation is then excluded at current sensitivity, because a true amplitude at the detection threshold ($0.05$, i.e. $5\sigma$) would with overwhelming probability not produce a best fit below $1\sigma$.
- **Inconclusive region:** $0.01\leq\epsilon\leq 0.05$. A best fit in this band neither detects nor excludes the model; the analysis returns an upper limit rather than a decision.

These three regions are the decision structure used in Section 7. They are thresholds derived from an adopted reading of published detectability figures, not results of a data analysis performed here.

### 4.6 Period in observational variables and number of oscillations

The modulation period in $\ln k$ is $\ln p$; for $p=2$,

$$
\Delta(\ln k)_{\text{period}}=\ln 2\approx 0.693,
$$

so one full oscillation corresponds to a factor‑of‑two change in wavenumber or multipole ($k\mapsto 2k$). Over a multipole range $30\leq\ell\leq 2500$, the number of visible oscillation periods is

$$
N_{\text{osc}}=\frac{\ln(\ell_{\max}/\ell_{\min})}{\ln 2}=\frac{\ln(2500/30)}{\ln 2}=\frac{\ln 83.333}{0.693147}=\frac{4.4229}{0.693147}=6.38.
$$

Arithmetic: $2500/30=83.333$; $\ln 83.333=\ln 250-\ln 3=5.5215-1.0986=4.4229$; $4.4229/0.693147=6.381$. A binary‑tree modulation therefore produces about $6.4$ full oscillations across the range probed by Planck‑class temperature data — enough cycles for the periodicity itself to be identified in a spectral fit, which is what makes the two‑parameter fit $(\epsilon,\phi)$ of Section 7 well posed.

## 5. Results

The following numbers are computed in Section 4 with shown arithmetic; no data analysis, simulation, or fit was performed for this paper.

1. **Node counts.** At depth 5 the binary tree has $N_{5}=32$ nodes; at depth 10, $N_{10}=1024$ nodes and $N_{\text{tot}}(10)=2047$ cumulative nodes (Section 4.1).
2. **Emergent Hubble‑like parameter.** For $p=2$ and the assumption $\lambda=1$, $H=\ln 2\approx 0.6931$ in Planck‑time units (Section 4.2).
3. **Holographic entropy bound.** At depth 10 with $c=1$, $S_{10}^{\max}=25.3984\approx 25.4$ bits; in general $S_{10}^{\max}=25.3984\,c$ bits (Section 4.3).
4. **Consistency ratio and embedding constant.** $I_{10}/S_{10}^{\max}=40.3$ at $c=1$; equality requires the assumption $c\approx 40.3$, carried as an assumption throughout (Section 4.4).
5. **Detectability thresholds.** Under the assumption $\sigma_{\epsilon}\approx 0.01$ adopted in Section 4.5, detection requires $\epsilon>0.05$, a null result is $\epsilon<0.01$, and $0.01\leq\epsilon\leq 0.05$ is inconclusive (Section 4.5).
6. **Log‑periodic signature.** The modulation $P(k)=P_{0}(k)[1+\epsilon\cos(2\pi\ln k/\ln 2+\phi)]$ has period $\ln 2\approx 0.693$ in $\ln k$ and produces $N_{\text{osc}}\approx 6.4$ oscillations over $30\leq\ell\leq 2500$ (Section 4.6).

All numerical values follow from the formulas of Section 3 and the parameters $p=2$, $\lambda=1$, $c=1$ (or $c\approx 40.3$ for entropy matching), together with the adopted reading of the detectability figures of [6].

## 6. Discussion

### 6.1 Limitations

The result of this paper — a parameterized, thresholded prediction — rests on the following assumptions, each with its sensitivity stated.

- **Conversion factor $\lambda$.** The identification of one tree step with one Planck time ($\lambda=1$) is an assumption; $H=\ln p/\lambda$ scales inversely with it, and no derivation of $\lambda$ from the tree geometry is given here. The emergent‑spacetime derivation of [5] shows how a dimensionless constant can be tied to the spectral radius of the tree, but that step is not carried out for $H$ in this paper.
- **Embedding constant $c$.** The value $c\approx 40.3$ is an assumption required to reconcile $I_{10}=1024$ bits with the holographic bound; the entropy comparison is vacuous without it, and no first‑principles derivation exists in this paper.
- **Area ansatz $A_{n}=c\,p^{2n/3}$.** The $2/3$ power reflecting a three‑dimensional embedding is an ansatz, not a derivation. The natural entropy variable on the Bruhat–Tits tree is depth times $\log p$ [4]; if that scaling replaces the ansatz, the entropy comparison of Section 4.3 changes form entirely, and the ratio $40.3$ loses its meaning.
- **One bit per node.** The ultrametric QEC analysis of [3] shows that information on such trees is organized in discrete redundancy steps (a staircase in which redundancy changes only when the information‑spreading radius advances one level), not as a uniform per‑node budget; the true information content could differ from $p^{n}$ by a level‑dependent factor.
- **Chordality.** Under the stated convention, trees are vacuously chordal; whether that coincides with the condition under which the graph models of [3] realize prescribed holographic entropy vectors is unresolved, so the claim that the p‑adic tree realizes holographic entropy bounds remains an open requirement, not a construction.
- **No‑go constraint on the observer model.** [6] proves that the Page–Wootters conditional state distance $d(\tau_1,\tau_2)=1-\bigl|\sum_n w_n e^{-iE_n(\tau_1-\tau_2)}\bigr|$ is not strictly ultrametric for all $\tau_1,\tau_2$ unless the clock is trivial, because a non‑constant ultrametric on the connected space $\mathbb{R}$ would require clopen balls, of which $\mathbb{R}$ has none; the same work reports that a $D=4$ Fourier‑clock construction was falsified by its own distance spectrum, with 29 distinct values for $N=30$ states. Observer worldlines in the present model inherit the tree's ultrametric, but the conditional states that would realize an observer's clock are provably non‑ultrametric in any non‑trivial Archimedean parametrization. The reconciliation is an open problem and a direct structural threat to the "static substrate, dynamic observers" move.
- **Detectability assumption.** The thresholds $\epsilon>0.05$ and $\epsilon<0.01$ follow from the assumption $\sigma_{\epsilon}\approx 0.01$ adopted in Section 4.5, not from a figure derived in [6]. Under the alternative literal reading — the 3% amplitude has significance $0.03\sigma$, giving $\sigma_{\epsilon}=1$ — the thresholds change: the detection threshold would move far above $0.05$ and the null‑result threshold far above $0.01$. The decision structure of Section 7 is therefore assumption‑dependent, and the assumption is stated so that it can be checked against the source.
- **Scope of the reference base.** The works cited and listed in the References number six; the paper's quantitative anchors come from [6] (thresholds and no‑go theorem) and [4] (entropy scaling), with [1], [2], [3], [5] supplying structural constraints. No claim in this paper rests on literature beyond these six works, and the detectability figures in particular trace to a single source, [6], which has not been independently reproduced here.

### 6.2 Falsification

The observation that would falsify the central claim is the following: a reanalysis of public Planck temperature and polarization data, fitting $(\epsilon,\phi)$ in the template of Section 3.6 over $30\leq\ell\leq 2500$, that returns a best‑fit amplitude $\epsilon<0.01$ with an uncertainty consistent with $\sigma_{\epsilon}\approx 0.01$. Under the convention of Section 4.5, such a result excludes the binary‑tree modulation at current sensitivity, because a true amplitude at the detection threshold of $0.05$ would be a $5\sigma$ effect and would not plausibly produce a sub‑$1\sigma$ best fit. Conversely, the claim is corroborated — not proved — by a detection at $\epsilon>0.05$ with period $\ln 2$ in $\ln\ell$; a modulation with a different period would falsify the specific $p=2$ hypothesis while leaving other primes open, since the period $\ln p$ is the only model‑dependent signature that distinguishes primes. A detection of a modulation at period $\ln 2$ but with a phase structure inconsistent with a single cosine (for example, higher harmonics at fixed amplitude) would falsify the specific ansatz of Section 3.6 while leaving the tree geometry untested.

### 6.3 Open questions

- Can the embedding constant $c$ be derived from the Bruhat–Tits geometry, replacing the $p^{2n/3}$ ansatz with the depth‑times‑$\log p$ scaling of [4]?
- Can the conditional clock states of an observer be constructed so as to evade the no‑go theorem of [6] — for example, with a number‑theoretic energy spectrum, an open problem that [6] itself poses?
- Is there a mechanism that selects a particular prime $p$, or does the adelic sum over primes of [5] enter the observable spectrum?
- What dynamical equations govern matter fields on the tree, and do they reproduce standard model interactions?
- Can tree depth be linked to the observed horizon scale through a renormalization‑group flow, as the AdS/CFT‑as‑RG‑flow correspondence of [4] suggests?

## 7. Practical Implications and Engineering Pathways

### (a) Users and decision impact

The users are theoretical cosmologists and quantum‑gravity model builders, and the analysis teams who maintain CMB spectral pipelines. If the result holds — that the binary‑tree prediction is a two‑parameter log‑periodic modulation with the thresholds of Section 4.5 — the decision that changes is concrete: a nested‑hypothesis comparison in an existing spectral pipeline gains one model with a fixed parameter vector $(\epsilon,\phi)$, and a single reanalysis of public data returns one of three decisions (detect, exclude, inconclusive) for the entire class of binary‑tree geometries. Model builders likewise gain a feedback channel that prior unfalsifiable statements lacked.

### (b) Technology readiness level

The work is purely analytical and has not been peer reviewed; against the NASA Technology Readiness Level definitions it resides at **TRL 2** (technology concept and/or application formulated). No hardware is involved, no data analysis was performed, and no claim of experimental or manufacturing readiness is made. Analytical work of this kind cannot exceed TRL 3 by construction.

### (c) Minimal next test

The smallest de‑risking step is a proposed reanalysis, written here as a proposal in the conditional: a study would fit the template $P(\ell)=P_{0}(\ell)\,[1+\epsilon\cos(2\pi\ln\ell/\ln 2+\phi)]$ to the public Planck temperature and polarization angular power spectrum over $30\leq\ell\leq 2500$, would measure the best‑fit amplitude $\epsilon$ and its uncertainty, and would apply the thresholds of Section 4.5. The outcome that refutes the model is a best fit $\epsilon<0.01$; the outcome that establishes it is $\epsilon>0.05$ at period $\ln 2$; anything between returns an upper limit. The analysis uses existing public data and standard spectral‑estimation software; [6] reports that the corresponding analysis of public Planck data takes under one hour, which sets the expected computational scale.

### (d) Binding constraints

- **Depth‑to‑multipole mapping.** The prediction is stated in $\ln k$; converting it to $\ln\ell$ requires a calibrated relation between tree depth and angular scale, which is currently an open modeling question rather than a derived input.
- **Cosmic variance.** The fractional sampling uncertainty of the angular power spectrum scales as $\sqrt{2/(2\ell+1)}$. At $\ell=30$ this is $\sqrt{2/61}=0.181$, i.e. $18.1\%$, which dwarfs any $\epsilon\leq 0.05$; at $\ell=2000$ it is $\sqrt{2/4001}=0.0223$, i.e. $2.2\%$, still comparable to the detection threshold. Sensitivity to the modulation is therefore concentrated at high $\ell$, and the low‑$\ell$ modes contribute mainly to constraining $\phi$.
- **Data and compute.** The analysis requires high‑precision spectral estimation on public Planck products; no novel hardware, instrument, or dataset is required, and the compute scale is bounded by the under‑one‑hour figure reported in [6].
- **Foreground and systematics contamination.** Not quantified in this paper; whether foreground removal degrades the effective $\sigma_{\epsilon}$ below the assumed $0.01$ is an open question that the proposed reanalysis would answer.

### (e) Projected performance bounds

The following are **projections**, labeled as such, with their assumptions stated. Assuming the convention of Section 4.5 ($\sigma_{\epsilon}\approx 0.01$) and foreground systematics that do not inflate the amplitude uncertainty beyond that value, the projected sensitivity of a Planck reanalysis is a detection floor at $\epsilon\approx 0.05$ and an exclusion floor at $\epsilon\approx 0.01$. The projected number of resolvable oscillations is $N_{\text{osc}}\approx 6.4$ over $30\leq\ell\leq 2500$, derived in Section 4.6 from the stated multipole range and the period $\ln 2$; this figure depends only on the range and the period and is insensitive to the amplitude. No cost figures are derivable from the inputs of this paper and none are projected.

### (f) Risks and misuse

The framework is purely theoretical and carries no technological misuse path. The operative risk is interpretive: a log‑periodic modulation detected at period $\ln 2$ could be misread as evidence for mechanisms outside the model (for example, new particle species or early‑universe features), diverting analysis effort. The mitigation is the decision structure itself: the model is accepted only with the full parameter vector $(\epsilon,\phi)$ at the stated period, and a detection at any other period is a falsification of the $p=2$ hypothesis, not a confirmation of the framework.

## 8. Conclusion

This paper has converted the static p‑adic holographic tree from an unfalsifiable slogan into a parameterized, thresholded prediction. The model — a rooted $p$‑ary tree with ultrametric distance $d_p(x,y)=p^{-k}$, observer worldlines as infinite paths, and one bit per node — yields, for $p=2$ and the assumption $\lambda=1$, an emergent Hubble‑like parameter $H=\ln 2\approx 0.6931$ in Planck‑time units, a depth‑10 holographic entropy bound $S_{10}^{\max}=25.3984\,c$ bits ($\approx 25.4$ bits at $c=1$) against a shell information content of $I_{10}=1024$ bits, and a consistency ratio of $40.3$ that fixes the embedding constant at the assumed value $c\approx 40.3$.

The observational content is the log‑periodic modulation $P(k)=P_0(k)\,[1+\epsilon\cos(2\pi\ln k/\ln p+\phi)]$, with period $\ln 2\approx 0.693$ in $\ln k$ and about $6.4$ full oscillations over $30\leq\ell\leq 2500$. Under the assumption $\sigma_\epsilon\approx 0.01$ adopted in Section 4.5, the fitted amplitude uncertainty is $\sigma_\epsilon\approx 0.01$, detection requires $\epsilon>0.05$, a null result at $\epsilon<0.01$ excludes the binary‑tree hypothesis at current sensitivity, and the band $0.01\leq\epsilon\leq 0.05$ is inconclusive. A single reanalysis of public Planck temperature and polarization data, fitting the two parameters $(\epsilon,\phi)$, therefore returns one of three decisions for the entire class of binary‑tree geometries.

Three corrections to prior statements of the model were carried through the derivations. The detection and null‑result thresholds are now derived, under an explicitly stated convention, rather than asserted. The prediction now specifies its amplitude, phase, period, and uncertainty, and no quantitative comparison to existing CMB data is claimed. The chordality claim is downgraded: trees are vacuously chordal under the stated graph‑theoretic convention, but realizing the holographic entropy vectors of [3] on the p‑adic tree remains an open requirement, not a construction.

The result rests on assumptions that are stated rather than hidden: the conversion factor $\lambda$, the embedding constant $c$, the $p^{2n/3}$ area ansatz, the one‑bit‑per‑node assignment, and the adopted reading of the detectability figures. The no‑go theorem of [6] — that Page–Wootters conditional state distances are not ultrametric except for trivial clocks — stands as a direct structural threat to the observer model and marks the reconciliation of Archimedean clock states with the tree's ultrametric as the central open problem. If the proposed reanalysis returns $\epsilon<0.01$, the binary‑tree hypothesis is excluded at current sensitivity; if it returns $\epsilon>0.05$ at period $\ln 2$, the search for an inflaton potential acquires a discrete‑geometry alternative to constrain. Either outcome is a usable result, which is what the prior unfalsifiable statement could not provide.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 2.0.0 (2026-11-01, from 1.0.1): rewritten in full through the research pipeline. references 11 -> 6. length 3207 -> 6196 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.40.12-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 12 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[2] Percolation thresholds of two-dimensional continuum systems of rectangles [with erratum]. arXiv:1604.01315v1. https://arxiv.org/abs/1604.01315v1
[3] https://papers.qnfo.org/papers/qec-darwinism-ultrametric. QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces.
[4] https://papers.qnfo.org/papers/x3.4-holographic-qec-ads-cft-rg-flow. QNFO: Holographic QEC as AdS/CFT RG Flow on Bruhat–Tits Trees.
[5] https://papers.qnfo.org/papers/formal-derivation-of-emergent-spacetime. QNFO: Formal Derivation of Emergent Spacetime to the Bruhat-Tits Tree.
[6] https://papers.qnfo.org/papers/radix-to-ultrametrics-to-page-wootters-to-wheeler-dewitt-to. QNFO: Radix to Ultrametrics to Page-Wootters to Wheeler-DeWitt to Bruhat-Tits: A Convergent Synthesis.
