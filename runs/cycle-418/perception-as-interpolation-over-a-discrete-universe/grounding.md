# Grounding block - source: rem-2a663687-b5b8-4dd9-8d65-feac2b7bcce7

## Research idea

Correct the published paper 'perception-as-interpolation-over-a-discrete-universe' for erratum pl-perception-as-interpolation-over-a-discrete-universe-1.0.0-1: Falsification criterion compares a reported mean absolute error to a worst-case bound: measured mean > 0.05 mm falsifies the model.
Also: pl-perception-as-interpolation-over-a-discrete-universe-1.0.0-0: Section 3's derivation: |e(x)| = |ψ(x) − [q_i(h_i^{-1}(x)) + s_i(h_i^{-1}(x))ψ(h_i^{-1}(x))]| ≤ ½|ψ(x) − ψ(h_i^{-1}(x))| ≤ ½Δx.

## Existing paper under revision (remediation only)

# Perception as Interpolation over a Discrete Universe

## Abstract
Human perception delivers a seamless experience despite receiving sparse, quantized sensory samples. The gap between discrete neural inputs and continuous phenomenology suggests that the brain implements an interpolation operator that reconstructs continuous percepts from discrete data packets. This paper formalizes perception as a reconstruction map $\mathcal{I}$ that acts on a bounded subset $\mathsf{X}$ of a Banach space $\mathsf{E}$ and produces a continuous function $\psi:\mathsf{X}\to\mathsf{F}$ in a prescribed function space $\mathscr{F}$. By importing the Lipschitz contraction property of the shift maps $s_i$ in fractal iterated‑function systems [1] and the explicit Lagrange interpolation formula over division rings [5], we derive an error bound  
\[
\|\psi(x)-\mathcal{I}[\psi](x)\|\le L_{\max}\,\Delta x,
\]  
where $L_{\max}=1/2$ and $\Delta x$ is the maximal sampling interval. Assuming, as a paper‑specific assumption, that $\Delta x=0.1\;\text{mm}$, the bound evaluates to $5\times10^{-2}\;\text{mm}$. The result predicts that perceptual filling‑in (e.g., blind‑spot completion, phi phenomenon) cannot exceed this geometric error, providing a quantitative target for psychophysical testing. If empirical measurements of perceptual interpolation error surpass $0.05\;\text{mm}$, the interpolation hypothesis would be falsified. The paper concludes with a roadmap for experimental validation and discusses engineering pathways for neuromorphic systems that emulate human‑like interpolation.

## 1. Introduction
Visual and auditory systems constantly confront incomplete sensory data: the optic nerve leaves a blind spot, motion perception stitches together discrete frames, and phonemic restoration fills missing sounds. These gaps cost the brain additional processing time and can lead to perceptual errors, yet everyday agents—human drivers, pilots, and surgeons—rely on the illusion of continuity to make rapid decisions. If perception truly operates as an interpolation over a fundamentally discrete substrate, then a precise mathematical description of the interpolation kernel would enable designers of autonomous vehicles, prosthetic sensors, and virtual‑reality interfaces to predict and control perceptual gaps. Moreover, a validated interpolation model would clarify the neural basis of agency.

**Contributions.**  
- **C1.** Formal definition of a perception‑as‑interpolation operator $\mathcal{I}$ based on fractal iterated‑function system (IFS) theory [1] (Section 2).  
- **C2.** Derivation of a universal error bound $\|\psi-\mathcal{I}[\psi]\|\le L_{\max}\Delta x$ using the Lipschitz constant $L(s_i)=\tfrac12$ from the IFS contraction property [1] (Section 4).  
- **C3.** Numerical evaluation of the bound for a biologically plausible sampling interval, yielding a concrete prediction of $5\times10^{-2}\;\text{mm}$ (Section 5).  
- **C4.** Identification of falsification criteria and a minimal psychophysical experiment to test the bound (Section 6).  

## 2. Background and Related Work
Fractal interpolation theory provides a natural language for reconstructing functions from sparse data. In the classic Fractal Interpolation Problem, a bounded set $\mathsf{X}\subset\mathsf{E}$ and a Banach space $\mathsf{F}$ admit a global function $\psi$ satisfying functional equations $\psi(h_i(x))=q_i(x)+s_i(x)\psi(x)$ [1, §1]. The shift maps $s_i$ are contractions with Lipschitz constant $L(s_i)=\tfrac12$ [1, §3], guaranteeing the existence of a unique fixed point that can be interpreted as an interpolant.

Quaternionic polynomial interpolation extends the Lagrange construction to non‑commutative settings. The Lagrange interpolation polynomial $\widetilde{f}(z)=\sum_{j=1}^{n}\frac{c_j p_j(z)}{p_j(z_j)}$ reproduces prescribed values $c_j$ at nodes $z_j$ [2, §1]. Although the underlying field is non‑commutative, the uniqueness and low degree of the solution mirror the classical case, suggesting that interpolation mechanisms are robust across algebraic structures.

 This discrete ontology aligns with the hypothesis that neural data are sampled from a fundamentally quantized substrate.

Lagrange interpolation over division rings shows that, despite left‑right evaluation asymmetries, a unique polynomial $f_L$ satisfying $f_L(\alpha_i)=c_i$ exists for any distinct nodes $\alpha_i$ [5, §1]. The explicit formula $f_L(z)=\sum_{i=1}^{n}\frac{p_i(z)c_i}{p_i(\alpha_i)}$ provides a constructive method for interpolation in non‑commutative settings.

Multivariate skew polynomial interpolation extends evaluation and interpolation to several variables over division rings [7, §3]. The evaluation map $E_{\mathbf{a}}$ is left‑linear, and a Lagrange‑type theorem guarantees the existence of interpolants on finitely generated $P$‑closed sets [7, §11].

Cyclic matrices over division rings admit polynomial interpolation via companion matrices, with left and right evaluations defined by $f^{\bm{\mathfrak{e}}_{\ell}}(A)=\sum A^j f_j$ and $f^{\bm{\mathfrak{e}}_{r}}(A)=\sum f_j A^j$ [8, §2.1]. This algebraic machinery underlies many coding‑theoretic interpolation algorithms.

Collectively, these works demonstrate that interpolation is a mathematically well‑posed operation across a wide spectrum of algebraic and geometric contexts, supporting the plausibility of a universal perceptual interpolation mechanism.

The discrete relational ontology presented in [3] argues that a finite number of degrees of freedom, motivated by black‑hole entropy considerations, can give rise to a continuum approximation, reinforcing the premise of a fundamentally discrete perceptual substrate.  

Fractal interpolation over nonlinear partitions [4] establishes that, even with $C^{1}$‑diffeomorphic partition maps $h_i$, the functional equations admit a unique solution $\psi$, provided the maps generate a disjoint partition of $\mathsf{X}$.  

Mean‑value interpolation on polygons [6] proves continuity of the interpolant at edges and vertices (Theorems 1 and 2), showing that the method yields a continuous reconstruction on arbitrary polygonal domains.  

Integer‑lattice interpolation [9] constructs Kronecker‑delta‑like basis functions on a regular grid, enabling exact reconstruction on integer‑valued sampling lattices.  

Human perception of performance [10] reports that observers rely on a small set of salient features, providing empirical support for the assumption of sparse sampling with an effective interval $\Delta x$.  

Fast Kötter‑Nielsen‑Høholdt interpolation [11] demonstrates a quasi‑linear runtime for degree‑restricted polynomial interpolation, confirming that low‑complexity interpolants are computationally feasible for real‑time neuromorphic implementation.

## 3. Methods
We model the brain’s perceptual reconstruction as a map  
\[
\mathcal{I}:\mathscr{F}(\mathsf{X},\mathsf{F})\to\mathscr{F}(\mathsf{X},\mathsf{F}),\qquad
\psi\mapsto\mathcal{I}[\psi],
\]  
where $\mathsf{X}\subset\mathsf{E}$ is a bounded sampling set (e.g., retinal photoreceptor locations) and $\mathsf{F}$ is the space of perceptual features (e.g., luminance). The operator $\mathcal{I}$ is defined implicitly by the fractal IFS functional equations  
\[
\mathcal{I}[\psi]\bigl(h_i(x)\bigr)=q_i(x)+s_i(x)\,\psi(x),\qquad i=1,\dots,n,
\]  
with $h_i$ partitioning $\mathsf{X}$, $q_i\in\mathscr{F}$ encoding local sensory measurements, and $s_i$ the contraction maps from [1, §3] satisfying $L(s_i)=\tfrac12$.  

**Assumptions.**  
1. **Discrete sampling interval** $\Delta x=\max_{i}\|x_{i+1}-x_i\|$ is constant across $\mathsf{X}$.  
2. **Lipschitz continuity** of the true perceptual function $\psi$ with constant $L_\psi\le 1$ (a mild smoothness assumption).  
3. **Stationarity** of the IFS parameters across the perceptual field.  

Under these assumptions, the error $e(x)=\psi(x)-\mathcal{I}[\psi](x)$ can be bounded as follows. For any $x\in\mathsf{X}$,
\[
|e(x)| = |\psi(x)-\mathcal{I}[\psi](x)|
      = |\psi(x)-[q_i(h_i^{-1}(x))+s_i(h_i^{-1}(x))\psi(h_i^{-1}(x))]|
\]\nusing the IFS definition. Applying the triangle inequality and the Lipschitz property $|s_i(u)-s_i(v)|\le L(s_i)\,|u-v|$ with $L(s_i)=\tfrac12$ gives
\[
|e(x)|\le \tfrac12\,|\psi(x)-\psi(h_i^{-1}(x))|\le \tfrac12\,\Delta x,
\]\nsince the distance between $x$ and its pre‑image under $h_i$ is at most the maximal sampling interval $\Delta x$. Taking the supremum over $x$ yields
\[
\|e\|_\infty \le \frac12\,\Delta x = L_{\max}\,\Delta x.
\]  
where $L_{\max}=\max_i L(s_i)=\tfrac12$.

## 4. Analysis
We compute the error bound step by step.

1. From [1, §3] each shift map $s_i$ satisfies  
   \[
   L(s_i)=\frac12.
   \]  
   Therefore $L_{\max}= \frac12$.

2. Define the maximal sampling interval  
   \[
   \Delta x = \max_{i}\|x_{i+1}-x_i\|.
   \]  
   We adopt the assumption (A1) that $\Delta x = 0.1\;\text{mm}$ (this value is taken as a representative interval for illustration).

3. Assuming the IFS contraction with constant $L_{\max}=1/2$ and that the inverse partition map $h_i^{-1}$ does not move a point farther than the maximal sampling interval $\Delta x$, we obtain
   \[
   \|e(x)\| = \|\psi(x)-\mathcal{I}[\psi](x)\|\le L_{\max}\,\Delta x.
   \]

4. Substituting the numerical values:  
   \[
   \|e\|_\infty \le \frac12 \times 0.1\;\text{mm}
   = 0.05\;\text{mm}.
   \]  

Thus the worst‑case interpolation error is bounded by $5\times10^{-2}\;\text{mm}$.

## 5. Results
The derived bound predicts that any perceptual filling‑in phenomenon (e.g., blind‑spot completion) will deviate from the true underlying stimulus by no more than $0.05\;\text{mm}$ in geometric terms.  This quantitative prediction is directly testable with high‑resolution psychophysical methods (e.g., adaptive optics retinal imaging combined with forced‑choice localization tasks).

## 6. Discussion

### 1. Sensitivity of the geometric error bound to the sampling interval  

The worst‑case error derived in Section 4 is  
\[
\|e\|_\infty \le L_{\max}\,\Delta x,
\]  
with $L_{\max}=1/2$ from the contraction property of the shift maps $s_i$ (see [1, §3]).  
If the sampling interval is treated as a variable, the bound scales linearly:

\[
\boxed{\|e\|_\infty(\Delta x)=\frac12\,\Delta x}.
\]

**Worked example 1.**  
Assume a hypothetical increase in photoreceptor density that halves the average spacing to $\Delta x=0.05\;\text{mm}$. Substituting into the boxed formula gives  

\[
\|e\|_\infty = \frac12 \times 0.05\;\text{mm}=0.025\;\text{mm}.
\]  

All arithmetic steps are shown explicitly: $0.5\times0.05=0.025$. The relative error with respect to a typical receptive‑field diameter $d\approx1\;\text{mm}$ is  

\[
\frac{\|e\|_\infty}{d}= \frac{0.025}{1}=2.5\%.
\]  

Thus a doubling of sampling density reduces the worst‑case geometric error by a factor of two, confirming the linear dependence.

**Worked example 2.**  
If a retinal prosthesis can achieve $\Delta x=0.02\;\text{mm}$, the bound becomes  

\[
\|e\|_\infty = \frac12 \times 0.02\;\text{mm}=0.01\;\text{mm},
\]  

which corresponds to a $1\%$ relative error for $d=1\;\text{mm}$. This calculation follows the same substitution steps as above.

These examples illustrate that any design decision that changes $\Delta x$ directly translates into a proportional change in the guaranteed worst‑case interpolation error.

### 2. Influence of the Lipschitz constant  

The constant $L_{\max}$ originates from the IFS contraction maps $s_i$ defined in [1, §3] as $L(s_i)=\tfrac12$. Alternative IFS constructions can yield different Lipschitz constants. Suppose an IFS variant has $L(s_i)=\lambda$ with $0<\lambda<1$. Re‑deriving the bound yields  

\[
\|e\|_\infty \le \lambda\,\Delta x.
\]  

If $\lambda=0.3$, the bound for the baseline $\Delta x=0.1\;\text{mm}$ becomes  

\[
\|e\|_\infty =0.3\times0.1\;\text{mm}=0.03\;\text{mm},
\]  

a $3\%$ relative error. The arithmetic is $0.3\times0.1=0.03$. This demonstrates that the choice of IFS influences the tightness of the error guarantee.

### 3. Compatibility with non‑commutative Lagrange interpolation  

Quaternionic polynomial interpolation provides a concrete non‑commutative instance of exact reconstruction at prescribed nodes. Equation (1.2) in [2] gives the Lagrange polynomial  

\[
\widetilde{f}(z)=\sum_{j=1}^{n}\frac{c_{j}\,p_{j}(z)}{p_{j}(z_{j})},
\qquad
p_{j}(z)=\prod_{\substack{i=1\\ i\neq j}}^{n}(z-z_{i}).
\]  

Because each term satisfies $\widetilde{f}(z_{j})=c_{j}$, the interpolant reproduces the data exactly at the nodes. Embedding this construction into the IFS framework, we identify the nodes $\{z_{i}\}$ with the discrete sampling set $\mathsf{X}$ and the values $\{c_{i}\}$ with the sensory measurements $q_i(x)$. The contraction maps $s_i$ act on the residual error between the true perceptual function $\psi$ and the interpolant $\widetilde{f}$; we assume that the error after each IFS iteration is reduced by the factor $L_{\max}=1/2$. Thus the quaternionic Lagrange formula supplies an explicit algebraic kernel that exactly reproduces prescribed values at the nodes, as shown in [2]; we assume, for the purpose of this analysis, that this kernel satisfies the Lipschitz contraction $L_{\max}=1/2$.

### 4. Nonlinear partitions and the uniqueness of the interpolant  

The fractal interpolation problem over nonlinear partitions, introduced in [4], replaces affine partition maps $h_i$ with $C^{1}$‑diffeomorphisms that are not affine. Section 3.1 of [4] proves that, under the condition that the collection $\{h_i\}$ generates a disjoint partition $\mathsf{X}=\coprod_{i=1}^{n}h_i(\mathsf{X})$, the functional equations  

\[
\psi\bigl(h_i(x)\bigr)=q_i(x)+s_i(x)\,\psi(x)
\]  

have a **unique** solution $\psi\in\mathscr{F}(\mathsf{X},\mathsf{F})$. The proof relies on the contractivity of the maps $s_i$, which are assumed to satisfy $L(s_i)=\tfrac12$ exactly as in [1, §3]. Consequently, the error bound derived in Section 4 remains valid even when the underlying partition is nonlinear, because the same contraction argument applies verbatim. No additional numerical assumptions are required beyond those already stated.

### 5. Transfinite mean‑value interpolation on polygons  

Mean‑value (MV) coordinates provide a geometric interpolation scheme on arbitrary polygons. Theorem 1 of [6] shows that for any interior point $\mathbf{y}_{*}$ on an edge, the MV interpolant $g(\mathbf{x})$ satisfies  

\[
\lim_{\mathbf{x}\to\mathbf{y}_{*}} g(\mathbf{x}) = f(\mathbf{y}_{*}),
\]  

and Theorem 2 proves the analogous result for vertices. These convergence statements guarantee **continuity** of the interpolant at the boundary of the domain. When the polygonal domain is identified with a discretized retinal patch, the MV interpolant plays the role of the operator $\mathcal{I}$ applied to boundary measurements $f$. The continuity at edges and vertices ensures that the Lipschitz constant of the interpolant does not exceed the maximum of the Lipschitz constants of the boundary data. Since the boundary data are sampled at spacing $\Delta x$, the same bound $\|e\|_\infty\le L_{\max}\Delta x$ follows, with $L_{\max}=1/2$ inherited from the underlying IFS contraction.

### 6. Multivariate skew‑polynomial interpolation  

The multivariate skew‑polynomial framework of [7] extends the univariate Lagrange theorem to several variables over division rings. Section 4 of [7] states a **Lagrange‑type theorem**: for any finitely generated $P$‑closed set $\Omega\subset\mathbb{F}^{n}$ there exists a unique multivariate skew polynomial $F$ such that  

\[
F(\mathbf{a}) = c_{\mathbf{a}} \quad\text{for all}\quad \mathbf{a}\in\Omega,
\]  

where $c_{\mathbf{a}}$ are prescribed target values. The proof constructs $F$ by a linear combination of basis polynomials analogous to (1.2) in [5]. Because the evaluation map $E_{\mathbf{a}}$ is left‑linear, the interpolation error is again governed by the Lipschitz constants of the underlying shift operators, which are taken to be $1/2$ in our IFS model. Therefore the multivariate setting inherits the same worst‑case bound, confirming that the result is dimension‑independent.

### 7. Cyclic‑matrix interpolation and constructive kernels  

Cyclic matrices over division rings admit a polynomial representation via companion matrices, as described in [8]. Section 2.1 shows that for a cyclic matrix $A$ and a vector $\mathbf{v}$, the minimal polynomial $\mathfrak{P}_{A,\mathbf{v}}$ satisfies  

\[
\mathfrak{P}_{A,\mathbf{v}}(A)\,\mathbf{v}=0.
\]  

The interpolation formula in [8] constructs a polynomial $p$ such that $p(A)\mathbf{v}$ reproduces a prescribed data vector. Translating $A$ to a discretized sampling operator and $\mathbf{v}$ to the sensory measurement vector $q_i$, the polynomial $p$ becomes an explicit kernel implementing $\mathcal{I}$. Because the minimal polynomial is of degree $n$ (the dimension of the sampling set), the kernel exactly interpolates $n$ data points. We assume that the residual error after applying $p$ is bounded by $L_{\max}\Delta x, consistent with the scalar case.

### 8. Integer‑lattice interpolation and homogeneous polynomials  

 This result can be used to construct interpolation kernels on integer‑valued sampling grids, which model the discrete arrangement of photoreceptors when their positions are approximated by lattice points. By selecting $P$ to vanish on all points except a single target node, one obtains a Kronecker‑delta‑like basis function. Superposing these basis functions yields an exact interpolant on the integer lattice. The Lipschitz constant of the resulting piecewise‑polynomial interpolant is bounded by the maximum distance between adjacent lattice points, i.e. $\Delta x$, and the contraction factor $1/2$ from the IFS, leading again to the bound $\|e\|_\infty\le\frac12\Delta x$.

### 9. Empirical motivation from limited perceptual features  

Human evaluators of complex stimuli, such as soccer performance in [10], rely on a **small set of noticeable features**. The work [10] reports that observers rely on a small set of salient features. This behavioral observation supports the modeling assumption that the perceptual system samples a high‑dimensional stimulus field at a sparse set of salient locations. The sparsity is quantified by an effective sampling interval $\Delta x$ that reflects the average spacing between attended features. Consequently, the analytical error bound derived from the IFS model is directly applicable to such limited‑feature perception.

### 10. Computational load of the interpolation operator  

 Section 5 of [11] emphasizes that the algorithm operates on **degree‑restricted polynomials**, which aligns with our requirement that the interpolant $\mathcal{I}[\psi]$ be of low degree to ensure real‑time applicability in neuromorphic hardware. Because the algorithm’s runtime scales quasi‑linearly with the number of samples $n$, the computational load of implementing $\mathcal{I}$ in a prosthetic device or a neuromorphic sensor remains modest, even for dense sampling ($n$ large). No additional arithmetic is introduced beyond the polynomial evaluations already required by the IFS recursion.

### 11. Alignment with a discrete relational ontology  

 The causal‑set approach of [3] further supports this view by showing that a finite number of degrees of freedom (motivated by black‑hole entropy) can give rise to a continuum approximation. Hence the mathematical framework of Sections 2–4 is consistent with a broader theoretical picture in which discreteness is a foundational premise.

### 12. Summary of the extended derivations  

| Derivation | Source of supporting statement | Result |
|------------|------------------------------|--------|
| Linear scaling of $\|e\|_\infty$ with $\Delta x$ | Contraction $L(s_i)=1/2$ from [1, §3] | $\|e\|_\infty = \frac12\Delta x$ |
| Effect of alternative Lipschitz constant $\lambda$ | Definition of Lipschitz constant in [1, §2] | $\|e\|_\infty \le \lambda\Delta x$ |
| Exact reconstruction at nodes via quaternionic Lagrange formula | Equation (1.2) in [2] | $\widetilde{f}(z_j)=c_j$ |
| Uniqueness under nonlinear partitions | Existence theorem in [4, §3.1] | Same error bound holds |
| Continuity of MV interpolant at edges/vertices | Theorem 1 and 2 in [6] | Guarantees $L_{\max}$ does not increase |
| Multivariate skew‑polynomial Lagrange‑type theorem | Section 4 of [7] | Unique interpolant on $P$‑closed sets |
| Cyclic‑matrix polynomial kernel construction | Minimal polynomial property in [8, §2.1] | Exact interpolation on $n$ points |
| Homogeneous polynomial existence on integer lattices | Lemma 1.1 in [9] | Basis functions for lattice interpolation |
| Sparse feature selection in human judgment | Feature‑selection discussion in [10, §0.3] | Empirical support for sparse $\Delta x$ |
| Fast polynomial construction algorithm | Complexity result in [11, §5] | Low computational overhead |

| Causal‑set finite‑degree‑of‑freedom argument | Black‑hole entropy motivation in [3, §2] | Upper bound on $n$ and thus on $\Delta x$ |

These extended derivations demonstrate that the error bound $\|e\|_\infty\le\frac12\Delta x$ is robust across a wide variety of interpolation frameworks—commutative, non‑commutative, linear, nonlinear, scalar, and multivariate—and that it aligns with both computational considerations and philosophical motivations for a discrete perceptual substrate.

## 7. Practical Implications and Engineering Pathways

**Limitations.**  
- **L1.** The Lipschitz constant $L_{\max}=1/2$ is inherited from the specific IFS construction in [1]; alternative IFS designs could yield different constants.  
- **L2.** The sampling interval $\Delta x=0.1\;\text{mm}$ is an assumption (A1) based on average cone spacing; actual spacing varies across the retina.  
- **L3.** The model treats perception as a static operator, ignoring temporal dynamics and feedback loops present in cortical processing.  
- **L4.** The error bound is worst‑case; typical perceptual errors may be substantially smaller.

**Falsification criterion.**  
A proposed experiment would measure the geometric discrepancy between a physically presented stimulus and its perceived location (e.g., using a calibrated retinal projector). If the reported mean absolute error exceeded the derived worst-case bound of $0.05\;\text{mm}$ under controlled conditions, the interpolation hypothesis as formalized here would be falsified; a measured error at or below this threshold would be consistent with it.

**Open questions.**  
- How do adaptive learning mechanisms modify the IFS parameters $h_i$, $q_i$, and $s_i$ over development?  
- Can the framework be extended to multimodal integration, where $\mathsf{F}$ includes auditory and somatosensory features?  
- What is the relationship between the interpolation error bound and the subjective sense of agency in decision‑making tasks?

## 7. Practical Implications and Engineering Pathways
**(a) Intended users and design impact.**  
Neuroscientists designing visual prostheses, engineers building neuromorphic sensors, and AI researchers developing generative perception models would use the bound to set hardware sampling densities and interpolation kernel parameters. If a retinal implant samples at intervals larger than $0.1\;\text{mm}$, then under the paper’s assumptions the bound would predict errors exceeding $0.05\;\text{mm}$; this projection depends on the untested interpolation hypothesis.

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; it resides at NASA Technology Readiness Level 2 (concept formulation).

**(c) Minimal de‑risking experiment.**  
A psychophysical pilot would present a high‑contrast edge with a controlled blind spot (masked region) and ask participants to localize the edge across the gap. The experiment would record the geometric deviation between the true edge position and the reported position. An average deviation $>0.05\;\text{mm}$ would falsify the model; a deviation $\le0.05\;\text{mm}$ would support it.

**(d) Engineering constraints.**  
- **Sampling density:** The bound directly ties error to $\Delta x$; thus electrode or photoreceptor spacing is the primary constraint.  
- **Kernel implementation:** Realizing the contraction maps $s_i$ requires hardware that can apply a $1/2$ scaling factor to the interpolated signal, which is straightforward in digital signal processors.  
- **Computational load:** The IFS recursion converges geometrically, implying low computational overhead for real‑time implementation.

**(e) Projected performance.**  
Assuming a prosthetic device with $\Delta x=0.08\;\text{mm}$ (a 20 % reduction in the sampling interval, corresponding to a 25 % increase in sampling density relative to the assumption), the bound becomes  
\[
\|e\|_\infty \le \frac12 \times 0.08\;\text{mm}=0.04\;\text{mm},
\]  
a $20\%$ reduction in worst‑case error.

**(f) Risks and misuse.**  
Over‑reliance on the bound could lead designers to ignore other sources of perceptual distortion (e.g., neural adaptation). Deploying a device that meets the geometric error criterion but fails to account for temporal latency could degrade user safety in high‑speed tasks.

## 9. Conclusion
By casting perception as a fractal‑IFS‑based interpolation operator, we derived a universal geometric error bound that links discrete sampling density to perceptual fidelity. The bound yields a concrete, testable prediction ($0.05\;\text{mm}$ worst‑case error for a $0.1\;\text{mm}$ sampling interval) and provides a quantitative design target for neuroprosthetic and neuromorphic systems. Future work will extend the model to incorporate temporal dynamics, adaptive learning of IFS parameters, and multimodal integration, thereby sharpening the bridge between discrete neural data and the continuous flow of conscious experience.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Fractal Interpolation over Curves. arXiv:2209.01033. https://arxiv.org/abs/2209.01033
[2] Polynomial interpolation over quaternions. arXiv:1405.3707. https://arxiv.org/abs/1405.3707
[3] Discovering the Discrete Universe. arXiv:1003.5890. https://arxiv.org/abs/1003.5890
[4] Fractal Interpolation over Nonlinear Partitions. arXiv:2203.07935. https://arxiv.org/abs/2203.07935
[5] Lagrange interpolation over division rings. arXiv:1909.06882. https://arxiv.org/abs/1909.06882
[6] Transfinite mean value interpolation over polygons. arXiv:1906.08358. https://arxiv.org/abs/1906.08358
[7] Evaluation and interpolation over multivariate skew polynomial rings. arXiv:1710.09606. https://arxiv.org/abs/1710.09606
[8] Cyclic matrices and polynomial interpolation over division rings. arXiv:2112.02716. https://arxiv.org/abs/2112.02716
[9] Interpolation over ZZ and torsion in class groups. arXiv:1905.12097. https://arxiv.org/abs/1905.12097
[10] Human Perception of Performance. arXiv:1712.02224. https://arxiv.org/abs/1712.02224
[11] Fast Kötter-Nielsen-Høholdt Interpolation over Skew Polynomial Rings. arXiv:2202.09057. https://arxiv.org/abs/2202.09057


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum

## QNFO corpus context (Vectorize)

QNFO: Perception as Interpolation over a Discrete Universe | https://papers.qnfo.org/papers/perception-as-interpolation-over-a-discrete-universe
QNFO: Two Errata to "Recursive Self-Consistency as a Monistic Foundation for Physical Reality": Correcting the Gödel Completeness Attribution and the Flatness-to-Zero-Energy Inference | https://papers.qnfo.org/papers/recursive-self-consistency
QNFO: Non-Archimedean Projective Perspective: The Monna Map as a Visual Rendering Interface | https://papers.qnfo.org/papers/non-archimedean-projective-perspective
QNFO: Numeral Trees as the Native Ultrametric Geometry of Cyclic Time | https://papers.qnfo.org/papers/numeral-trees-as-the-native-ultrametric-geometry-of-cyclic-time

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
  We derive sharp lower bounds for the first and the second Zagreb indices ($M_1$ and $M_2$ respectively) for trees and chemical trees with the given number of pendent vertices and find optimal trees. $M_1$ is minimized by a tree with all internal vertices having degree 4, while $M_2$ is minimized by a tree where each "stem" vertex is incident to 3 or 4 pendent vertices and one internal vertex, whil
  Full text (https://arxiv.org/html/1405.1293v3), excerpts of its own sections:
  § Introduction: Topological graph indices are widely used in mathematical chemistry to predict properties of chemical compounds. They have been intensively studied in recent years. Dozens of various indices were suggested [ 1 ] to describe topology of complex molecules, among the earliest and the most famous being the first and the second Zagreb indices – $M_{1}$ and $M_{2}$ respectively [ 9 ] . The popular research problem is to find lower and upper bounds of an index over a certain set of graphs and to characterize extremal graphs in this set. The typical set to study is that of all graphs (trees, bipartite or unicyclic graphs, “cacti”, etc) of the fixed order (i.e. with the fixed number of vertices). Extremal graphs on these sets often appear to be degenerate. For example, the chain minimizes Zagreb indices, while the star maximizes them over the set of trees of order $N$ (see [ 4 , 10 ] ). Even when the set of admissible graphs is cut (by limiting degrees, chromatic or matching numbers, etc), extremal graphs are typically found on the “boundary” of the set. [...]
  § 1 The First Zagreb Index: Let $G$ be a simple connected undirected graph with the vertex set $V(G)$ and the edge set $E(G)$ . Denote by $d_{G}(v)$ the degree of a vertex $v\in V(G)$ in the graph $G$ , i.e., the number of vertices being incident to $v$ in $G$ . The first Zagreb index is defined in [ 9 ] as $M_{1}(G):=\sum_{v\in V(G)}d_{G}(v)^{2},$ (1) while the second Zagreb index – as $M_{2}(G):=\sum_{uv\in E(G)}d_{G}(u)d_{G}(v).$ (2) The vertex $v\in V(G)$ with $d_{G}(v)=1$ is called a pendent vertex. Denote the set of pendent vertices of the graph $G$ with $W(G)$ . A connected graph $T$ with $N$ vertices and $N-1$ edges is called a tree. Theorem 1 For any tree $T$ with $n\geqslant 2$ pendent vertices $M_{1}(T)\geqslant 9n-16$ if $n$ is even. The equality holds if $T$ is a $4$ -tree ( with $d_{T}(m)=4$ for all $m\in V(G)\backslash W(G)$ ) . If $n$ is odd, then $M_{1}(T)\geqslant 9n-15$ , and the equality holds if $T$ is a tree with all internal vertices having degree $4$ except the one of degree $3$ . □ Proof For $n=2$ the optimal tree is the complete graph $K_{2}$ , and the theorem obviously holds. [...]
  § 2 The Second Zagreb Index: An internal vertex in a tree is called a stem vertex if it has incident pendent vertices (see [ 3 ] ). The edge connecting a stem with a pendent vertex will be referred to as a stem edge . Theorem 3 For any tree $T$ with $n\geqslant 8$ pendent vertices $M_{2}(T)\geqslant 11n-27$ . The equality holds if each stem vertex in $T$ has degree $4$ or $5$ while other internal vertices having degree $3$ . At least one such tree exits for any $n\geqslant 9$ . □ Proof Let us employ again the idea of an attached tree from Theorem 2 . Below we suggest a suitable generalization of the concept of an attached tree, then we interrelate its cost with $M_{2}$ , and, finally, use induction on $n$ to prove the lower bound. [...]
  § 3 Conclusion: Above we suggested an optimization framework for degree-based indices of undirected trees. Using the discussed approach one can calculate lower bounds for Zagreb-like indices and find the graphs minimizing these indices over the set of trees (or chemical trees) with the fixed number of pendent vertices. Theorem 1 provides a tight lower-bound estimate for $M_{1}$ and shows that it is achieved at $4$ -trees. Theorem 2 gives a high-quality lower-bound estimate for the generalized $M_{1}$ -like index. Theorem 3 proves the tight lower-bound estimate for $M_{2}$ and characterizes $M_{2}$ -minimal trees. [...]
[2] QNFO: Perception as Interpolation over a Discrete Universe | https://papers.qnfo.org/papers/perception-as-interpolation-over-a-discrete-universe
  Human perception delivers a seamless experience despite receiving sparse, quantized sensory samples. The gap between discrete neural inputs and continuous phenomenology suggests that the brain implements an interpolation operator that reconstructs continuous percepts from discrete data packets. This paper formalizes perception as a reconstruction map $\mathcal{I}$ that acts on a bounded subset $\m
  Full text (https://papers.qnfo.org/papers/perception-as-interpolation-over-a-discrete-universe), excerpts of its own sections:
  § 1. Introduction: Visual and auditory systems constantly confront incomplete sensory data: the optic nerve leaves a blind spot, motion perception stitches together discrete frames, and phonemic restoration fills missing sounds. These gaps cost the brain additional processing time and can lead to perceptual errors, yet everyday agents—human drivers, pilots, and surgeons—rely on the illusion of continuity to make rapid decisions. If perception truly operates as an interpolation over a fundamentally discrete substrate, then a precise mathematical description of the interpolation kernel would enable designers of autonomous vehicles, prosthetic sensors, and virtual‑reality interfaces to predict and control perceptual gaps. Moreover, a validated interpolation model would clarify the neural basis of agency. **Contributions.** - **C1.** Formal definition of a perception‑as‑interpolation operator $\mathcal{I}$ based on fractal iterated‑function system (IFS) theory [1] (Section 2). [...]
  § 5. Results: The derived bound predicts that any perceptual filling‑in phenomenon (e.g., blind‑spot completion) will deviate from the true underlying stimulus by no more than $0.05\;\text{mm}$ in geometric terms.  This quantitative prediction is directly testable with high‑resolution psychophysical methods (e.g., adaptive optics retinal imaging combined with forced‑choice localization tasks).
  § 9. Empirical motivation from limited perceptual features: Human evaluators of complex stimuli, such as soccer performance in [10], rely on a **small set of noticeable features**. The work [10] reports that observers rely on a small set of salient features. [...]
  § 12. Summary of the extended derivations: | Derivation | Source of supporting statement | Result | |------------|------------------------------|--------| | Linear scaling of $\|e\|_\infty$ with $\Delta x$ | Contraction $L(s_i)=1/2$ from [1, §3] | $\|e\|_\infty = \frac12\Delta x$ | | Effect of alternative Lipschitz constant $\lambda$ | Definition of Lipschitz constant in [1, §2] | $\|e\|_\infty \le \lambda\Delta x$ | | Exact reconstruction at nodes via quaternionic Lagrange formula | Equation (1.2) in [2] | $\widetilde{f}(z_j)=c_j$ | | Uniqueness under nonlinear partitions | Existence theorem in [4, §3.1] | Same error bound holds | | Continuity of MV interpolant at edges/vertices | Theorem 1 and 2 in [6] | Guarantees $L_{\max}$ does not increase | | Multivariate skew‑polynomial Lagrange‑type theorem | Section 4 of [7] | Unique interpolant on $P$‑closed sets | | Cyclic‑matrix polynomial kernel construction | Minimal polynomial property in [8, §2.1] | Exact interpolation on $n$ points | | Homogeneous polynomial existence on integer lattices | Lemma 1.1 in [9] | Basis functions for lattice interpolation | | Sparse feature [...]
  § 9. Conclusion: By casting perception as a fractal‑IFS‑based interpolation operator, we derived a universal geometric error bound that links discrete sampling density to perceptual fidelity. The bound yields a concrete, testable prediction ($0.05\;\text{mm}$ worst‑case error for a $0.1\;\text{mm}$ sampling interval) and provides a quantitative design target for neuroprosthetic and neuromorphic systems. Future work will extend the model to incorporate temporal dynamics, adaptive learning of IFS parameters, and multimodal integration, thereby sharpening the bridge between discrete neural data and the continuous flow of conscious experience.
[3] QNFO: Two Errata to "Recursive Self-Consistency as a Monistic Foundation for Physical Reality": Correcting the Gödel Completeness Attribution and the Flatness-to-Zero-Energy Inference | https://papers.qnfo.org/papers/recursive-self-consistency
  The preprint "Recursive Self-Consistency as a Monistic Foundation for Physical Reality" [4] rests two of its central arguments on statements that do not follow from the sources they invoke. First, its Section 1.1.1 attributes to Gödel's completeness theorem the claim that "if physics is a complete and consistent formal theory, no proper extension can add explanatory power without introducing an in
  Full text (https://papers.qnfo.org/papers/recursive-self-consistency), excerpts of its own sections:
  § 1. Introduction: A preprint that asserts a theorem it cannot source, or an empirical confirmation it cannot derive, imposes a real cost on its readers: every downstream argument that cites the assertion inherits the error, and correcting the record becomes harder as the preprint circulates. The preprint at issue [4] proposes a monistic foundation for quantum cosmology built on a fixed-point principle, and it is read by an audience interested in foundational physics and mathematical self-reference; two of its load-bearing claims — one logical, one cosmological — are stated in forms that a careful reader cannot verify from the authorities they name. The logical claim, in Section 1.1.1 of [4], misattributes a substantive theorem to Gödel's completeness theorem of 1930. [...]
  § 2. Background and Related Work: The erratum discipline that this paper practices has well-established precedent in physics publishing, and the six works available for citation here supply both the corrective models and the substantive material against which the two errata are checked. Because the citation base for this erratum is limited to six works, the literature treatment is correspondingly focused; this limitation is stated explicitly in Section 6. The document under correction is the preprint itself. Its Section 1.0 defines recursive self-consistency as a fixed point $x = \mathcal{R}(x)$ of a contraction mapping on a complete metric space, with the universal wave function $|\Psi\rangle$ as the fixed point and the Wheeler-DeWitt equation $\hat{H}|\Psi\rangle = 0$ as the timeless consistency condition [4]. [...]
  § 6. Discussion: The two corrections are narrow, and their narrowness is the point: an erratum that silently rewrote more than the flagged sentences would itself introduce unverifiable content into the record. This section states what the corrections leave intact, the conditions under which the corrections themselves would fail, and the limitations under which the derivations of Section 4 hold. **What survives.** The preprint's mathematical machinery — the fixed-point formulation $x = \mathcal{R}(x)$ on a complete metric space, the Wheeler-DeWitt constraint $\hat{H}|\Psi\rangle = 0$ as a timeless consistency condition, the circle-Gaussian co-definition, the theta-function partition function, and the six-step generative sequence — is untouched by both errata. What changes is the external support claimed for two of its arguments. [...]
  § 8. Conclusion: Two load-bearing sentences of the preprint [4] do not follow from the authorities they invoke. The Section 1.1.1 sentence attributes to Gödel's completeness theorem a prohibition of consistent, explanatory proper extensions; the theorem, which connects first-order validity to provability and guarantees models for consistent theories, supports no such prohibition, and the proposition itself is vacuously true under the same-language reading and false under the language-extension reading, refuted by the explicit consistent extension $T' = T \cup \{\exists x\, P(x)\}$. The Section 1.2.1 and 1.3.3 sentences convert the flatness bound $|\Omega_k| < 0.002$ into a purported confirmation of zero total energy; the bound actually constrains the density parameter to $0.998 \leq \Omega_{\text{total}} \leq 1.002$ and the Newtonian energy ratio to $|E|/K < 0.002$, and general relativity defines no globally closed-universe total energy for the bound to confirm. [...]
[4] QNFO: Non-Archimedean Projective Perspective: The Monna Map as a Visual Rendering Interface | https://papers.qnfo.org/papers/non-archimedean-projective-perspective
  Things farther away appear smaller, and two-point linear perspective is taken to approximate the eye. That phenomenology is Archimedean geometry. This paper asks what changes if the metric of physical space were instead non-Archimedean and ultrametric. Four moves: (1) the Archimedean anatomy of perspective; (2) the ultrametric demolition (naive direct-reading model falsified by smooth vision, C3-C
  Full text (https://papers.qnfo.org/papers/non-archimedean-projective-perspective), excerpts of its own sections:
  § 1. Introduction and Positioning: The originating question (Obsidian note `_26228180341.md`, 2026-08-16): *"Things that are farther away appear smaller, and 2 point linear perspective is thought to approximate our eyes — but what if instead of an Archimedean linear geometry, perspective is actually non-Archimedean and ultrametric? Would we perceive the same thing, and what would that actually mean ontologically?"* The QNFO corpus already treats ultrametric geometry as the candidate substrate for physics and computation [1,2,3], the external p-adic-physics literature pursues the same substrate hypothesis at the Planck scale [6,7,8], the corpus treats the observer as a node inside the ultrametric tree [4], and names the Monna map as the ratio-based interface between p-adic structure and continuous experience [5]. [...]
  § 2. The Archimedean Anatomy of Perspective [TERRITORY]: Linear perspective rests on three Archimedean ingredients. **(a) Similar triangles.** For an object of height $h$ at distance $d$ from an eye, the apparent size is governed by the subtended angle $\theta \approx h/d$ for $d \gg h$. The proportionality is the similar-triangles theorem of Euclidean geometry, and it requires two things: a well-defined ratio of lengths, and a well-defined angle. **(b) Additive distance along geodesics.** The distance $d$ is accumulated along a straight line — a geodesic — and satisfies the Archimedean property: finitely many steps of any positive length can cross any finite gap. Distance is the sum of its parts, which is exactly what makes "farther" a continuous degree. **(c) Projective closure.** Two-point perspective is projective geometry over $\mathbb{R}$: parallel lines are completed by ideal points — the vanishing points — on the line at infinity. The construction is algebraic over the reals and inherits the real field's order, completeness, and Archimedean valuation. [...]
  § 5. The Underdetermination Theorem [MAP]: **Theorem (perceptual underdetermination).** Given premises (i) and (ii), no finite set of first-person visual observations — apparent sizes, parallax, vanishing-point convergence — can distinguish an Archimedean substrate from an ultrametric substrate. *Proof sketch.* Both substrates render into the same image space $V$. For the Archimedean substrate, take $R$ to be the familiar similarity rendering. For the ultrametric substrate, compose a surjection $\pi \colon X \to \mathbb{Q}_p$ with the Monna map applied coordinate-wise to the three components of $V \cong \mathbb{R}^3$: $R = (M \circ \pi, M \circ \pi, M \circ \pi)$. Every measurement the observer can make lives in $V$; the two renderings differ only behind the interface, where no measurement reaches. Therefore the observation records are identical. $\square$ **Corollary.** "Would we perceive the same thing?" — yes, in principle: the same first-person world is compatible with both metrics. **The honest converse.** This does not show the world is ultrametric. [...]
  § 9. Conclusion: Naive ultrametric perception is falsified by smooth vision — recorded, not avoided (C3–C4). Rendered ultrametric perception is indistinguishable from Archimedean perception (§5). Together: the world's metric is a postulate, validated only by interaction, and the only thing perception ever measures is the interface. The originating question's answer is therefore both — we would perceive the same thing, and the meaning of that fact is that the continuum is a rendering, not a fact about the rendered. ---
[5] QNFO: Numeral Trees as the Native Ultrametric Geometry of Cyclic Time | https://papers.qnfo.org/papers/numeral-trees-as-the-native-ultrametric-geometry-of-cyclic-time
  Cyclic timestamps are stored linearly but intrinsically form mixed‑radix positional strings that nest hour, day, month, and finer cycles. Existing pipelines treat timestamps as points on the real line, ignoring this hierarchy and causing mis‑grouping across cycle boundaries. The gap is a lack of a mathematically grounded distance that respects the hierarchical nesting of calendar cycles. We formal
  Full text (https://papers.qnfo.org/papers/numeral-trees-as-the-native-ultrametric-geometry-of-cyclic-time), excerpts of its own sections:
  § 1. Introduction: Engineers of embedded systems, data‑scientists analyzing seasonal patterns, and educators teaching number sense all confront the same obstacle: **cyclic timestamps are forced into a linear metric that ignores the hierarchical nesting of second → minute → hour → day → month**. The cost is twofold. First, clustering algorithms that treat timestamps as points on the real line mis‑group events that are close in a cyclic sense (e.g., 23:59 → 00:01). Second, cognitive models that assume a linear mental number line cannot explain why children rapidly grasp magnitude relationships across orders of magnitude. If the *native* geometry of timestamps were recognized as an ultrametric tree, then a simple distance function would automatically respect cyclic nesting, and the brain’s logarithmic number sense could be re‑interpreted as ultrametric tree perception. [...]
  § 2. Background and Related Work: The present work builds on a diverse literature that links trees, ultrametrics, and cyclic structures. 1. [...]
  § 5. Results: The analysis yields the following concrete ultrametric distances for the mixed‑radix calendar tree: | Pair of timestamps | First differing level | Computed distance | |--------------------|-----------------------|-------------------| | $t_1$ vs $t_2$ (hour differs) | hour | $0.0416667$ | | $t_1$ vs $t_3$ (day differs) | day | $0.0333333$ | | $t_1$ vs $t_4$ (month differs)| month| $0.0833333$ | These numbers are derived solely from the branching factors and the valuation formula; no simulation or empirical measurement is involved. The distances respect the ultrametric property, guaranteeing that any hierarchical clustering algorithm using $d_{\text{mix}}$ will produce a dendrogram whose merges occur exactly at the first differing calendar level.
  § 7.1. Who would use the result and what changes?: - **Data scientists** analyzing seasonal or diurnal patterns can replace Euclidean timestamp distances with $d_{\text{mix}}$, automatically respecting cyclic boundaries. - **Embedded‑system designers** can implement tree‑structured counters (e.g., a 24‑branch hour counter feeding a 30‑branch day counter) that compute distances with a single table lookup, reducing arithmetic overhead. - **Cognitive psychologists** gain a quantitative hypothesis for experiments probing number sense across orders of magnitude.
  § 7.3. Smallest next experiment: Construct a depth‑2 hardware counter: an 8‑bit hour counter (branching $24$) feeding a 5‑bit day counter (branching $30$). Measure the latency of computing $d_{\text{mix}}$ between two timestamps using a comparator that identifies the first differing level. The experiment falsifies the result if the measured latency exceeds that of a conventional linear subtraction by more than a factor of $2$.
  § 8. Conclusion: We have formalized the numeral tree as a mixed‑radix ultrametric space, derived explicit distances that respect cyclic nesting, and proved that the resulting distance satisfies the strong triangle inequality. The derived distances ($0.0416667$, $0.0333333$, $0.0833333$) follow directly from branching factors and guarantee consistent hierarchical clustering. This framework offers a low‑cost, mathematically rigorous tool for cyclic time analysis, a plausible explanation for the brain’s logarithmic number sense, and a clear engineering pathway for tree‑structured counters. Future work will empirically test the cognitive hypothesis and prototype the hardware counter described in Section 7.3.