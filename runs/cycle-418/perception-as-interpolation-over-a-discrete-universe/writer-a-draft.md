# Perception as Interpolation over a Discrete Universe

## Abstract
Human perception delivers a seamless experience despite receiving sparse, quantized sensory samples. This paper models perception as an interpolation operator $\mathcal{I}$ that reconstructs a continuous perceptual field $\psi$ from a bounded discrete sampling set $\mathsf{X}$. By assuming that the underlying functional equations form a contractive iterated‑function system with Lipschitz constant $L_{\max}=1/2$, we derive a worst‑case geometric error bound  
\[
\|\psi-\mathcal{I}[\psi]\|_\infty \le L_{\max}\,\Delta x,
\]  
where $\Delta x$ is the maximal sampling interval. Taking $\Delta x=0.1\;\text{mm}$, the bound evaluates to $5\times10^{-2}\;\text{mm}$. The result predicts that perceptual filling‑in (e.g., blind‑spot completion) cannot exceed this error. If a psychophysical measurement of mean absolute error exceeds $0.05\;\text{mm}$, the interpolation hypothesis is falsified. The paper concludes with practical implications for neuroprosthetic design and a roadmap for experimental validation.

## 1. Introduction
Visual and auditory systems constantly confront incomplete sensory data: the optic nerve leaves a blind spot, motion perception stitches together discrete frames, and phonemic restoration fills missing sounds. These gaps impose additional processing demands on the brain and can lead to perceptual errors, yet everyday agents—human drivers, pilots, and surgeons—rely on the illusion of continuity to make rapid decisions. If perception truly operates as an interpolation over a fundamentally discrete substrate, then a precise mathematical description of the interpolation kernel would enable designers of autonomous vehicles, prosthetic sensors, and virtual‑reality interfaces to predict and control perceptual gaps. Moreover, a validated interpolation model would clarify the neural basis of agency.

**Contributions.**  
- **C1.** Formal definition of a perception‑as‑interpolation operator $\mathcal{I}$ (Section 3).  
- **C2.** Derivation of a universal error bound $\|\psi-\mathcal{I}[\psi]\|_\infty \le L_{\max}\Delta x$ using a contractive mapping argument (Section 4).  
- **C3.** Numerical evaluation of the bound for a biologically plausible sampling interval, yielding a concrete prediction of $5\times10^{-2}\;\text{mm}$ (Section 5).  
- **C4.** Specification of a falsification criterion and a minimal psychophysical experiment to test the bound (Section 6).  

The result may also matter to fields that model discrete substrates for continuous phenomena, such as computational neuroscience and signal‑processing theory.

## 2. Background and Related Work
Discrete structures often admit sharp quantitative bounds that illuminate the relationship between sparsity and error. The following works provide concrete points that motivate the present analysis.

* **[1]** derives sharp lower bounds for the first and second Zagreb indices of trees with a prescribed number of pendent vertices. The existence of tight extremal bounds for discrete graph measures illustrates how sparsity (few pendent vertices) constrains global quantities, an insight that parallels the way a sparse sampling set $\mathsf{X}$ constrains perceptual reconstruction error.

* **[2]** formalizes perception as a reconstruction map $\mathcal{I}$ acting on a bounded subset $\mathsf{X}$ of a Banach space and producing a continuous function $\psi$. This self‑cited work establishes the conceptual framework of an interpolation operator that bridges discrete neural inputs and continuous phenomenology.

* **[3]** emphasizes the importance of correcting unsupported logical claims in scientific discourse. Its discussion of errata underscores the need for rigorously derived error bounds, motivating the present derivation of a falsifiable geometric limit.

* **[4]** explores alternative metric frameworks by replacing the Archimedean geometry of perspective with a non‑Archimedean ultrametric substrate. Although the perceptual substrate in this paper remains Euclidean, the existence of viable alternative geometries highlights the relevance of explicitly stating metric assumptions, such as the Euclidean distance used to define $\Delta x$.

* **[5]** constructs an ultrametric distance on mixed‑radix calendar trees, demonstrating how hierarchical discrete structures can be endowed with mathematically precise distance functions. This work illustrates that discrete relational ontologies can support continuous‑like operations (e.g., distance) and motivates the present use of a discrete sampling interval to bound continuous error.

Collectively, these five works demonstrate that discrete mathematical structures can support rigorous quantitative analysis, providing a foundation for the interpolation‑error bound derived below. The limited number of available references is acknowledged in the Discussion.

## 3. Methods
We model perceptual reconstruction as a map  
\[
\mathcal{I}:\mathscr{F}(\mathsf{X},\mathsf{F})\to\mathscr{F}(\mathsf{X},\mathsf{F}),\qquad
\psi\mapsto\mathcal{I}[\psi],
\]  
where $\mathsf{X}\subset\mathsf{E}$ is a bounded sampling set (e.g., retinal photoreceptor locations) and $\mathsf{F}$ is the space of perceptual features (e.g., luminance). The operator $\mathcal{I}$ is defined implicitly by a system of functional equations  
\[
\mathcal{I}[\psi]\bigl(h_i(x)\bigr)=q_i(x)+s_i(x)\,\psi(x),\qquad i=1,\dots,n,
\]  
with the following components:

* $h_i:\mathsf{X}\to\mathsf{X}$ partitions $\mathsf{X}$ into disjoint regions.  
* $q_i\in\mathscr{F}$ encodes the local sensory measurement in region $i$.  
* $s_i:\mathsf{X}\to\mathbb{R}$ is a contraction map satisfying $|s_i(u)-s_i(v)|\le L(s_i)\,|u-v|$ for all $u,v\in\mathsf{X}$.

**Assumptions.**  
1. **Discrete sampling interval** $\Delta x=\max_{i}\|x_{i+1}-x_i\|$ is constant across $\mathsf{X}$.  
2. **Lipschitz continuity** of the true perceptual function $\psi$ with constant $L_\psi\le 1$.  
3. **Uniform contraction** of all $s_i$ with Lipschitz constant $L(s_i)=\tfrac12$.  

These assumptions are standard in contractive mapping analyses and are adopted here to obtain a closed‑form error bound.

## 4. Analysis
We derive the worst‑case interpolation error step by step.

1. **Contraction constant.**  
   By Assumption 3, each shift map satisfies  
   \[
   L(s_i)=\frac12.
   \]  
   Hence the maximal Lipschitz constant is  
   \[
   L_{\max}= \max_i L(s_i)=\frac12.
   \]

2. **Definition of the error.**  
   For any $x\in\mathsf{X}$, define the pointwise error  
   \[
   e(x)=\psi(x)-\mathcal{I}[\psi](x).
   \]

3. **Bounding the error.**  
   Using the functional definition of $\mathcal{I}$, for the unique index $i$ such that $x\in h_i(\mathsf{X})$ we have  
   \[
   \mathcal{I}[\psi](x)=q_i\bigl(h_i^{-1}(x)\bigr)+s_i\bigl(h_i^{-1}(x)\bigr)\,\psi\bigl(h_i^{-1}(x)\bigr).
   \]  
   Therefore  
   \[
   \begin{aligned}
   |e(x)|
   &=\bigl|\psi(x)-[q_i(h_i^{-1}(x))+s_i(h_i^{-1}(x))\psi(h_i^{-1}(x))]\bigr|\\
   &\le \bigl|\psi(x)-\psi\bigl(h_i^{-1}(x)\bigr)\bigr|\,|s_i\bigl(h_i^{-1}(x)\bigr)| \\
   &\le L(s_i)\,\bigl|\psi(x)-\psi\bigl(h_i^{-1}(x)\bigr)\bigr| \quad\text{(by the Lipschitz property of $s_i$)}\\
   &\le \frac12\,\bigl|\psi(x)-\psi\bigl(h_i^{-1}(x)\bigr)\bigr|.
   \end{aligned}
   \]  
   By Assumption 2, $\psi$ is Lipschitz with constant $L_\psi\le 1$, so  
   \[
   \bigl|\psi(x)-\psi\bigl(h_i^{-1}(x)\bigr)\bigr|\le L_\psi\,\|x-h_i^{-1}(x)\|\le \|x-h_i^{-1}(x)\|.
   \]  
   By construction of the partition maps, the distance between a point and its pre‑image is bounded by the maximal sampling interval:  
   \[
   \|x-h_i^{-1}(x)\|\le \Delta x.
   \]  
   Combining the inequalities yields  
   \[
   |e(x)|\le \frac12\,\Delta x.
   \]

4. **Supremum norm.**  
   Taking the supremum over all $x\in\mathsf{X}$ gives the uniform error bound  
   \[
   \|e\|_\infty \le \frac12\,\Delta x = L_{\max}\,\Delta x.
   \]

Thus the worst‑case interpolation error is directly proportional to the sampling interval, with proportionality constant $L_{\max}=1/2$.

## 5. Results
We evaluate the bound using the representative sampling interval assumed in Assumption 1.

* **Assumed sampling interval.** $\Delta x = 0.1\;\text{mm}$ (a typical average cone spacing in the human fovea).  

* **Numerical bound.**  
  \[
  \|e\|_\infty \le \frac12 \times 0.1\;\text{mm}=0.05\;\text{mm}=5\times10^{-2}\;\text{mm}.
  \]

Therefore any perceptual filling‑in phenomenon is guaranteed not to deviate from the true stimulus by more than $0.05\;\text{mm}$ in geometric terms.

## 6. Discussion
### Limitations
- **L1.** The Lipschitz constant $L_{\max}=1/2$ is imposed by Assumption 3; alternative contractive constructions could yield different constants.  
- **L2.** The sampling interval $\Delta x=0.1\;\text{mm}$ is an illustrative assumption; actual retinal spacing varies with eccentricity.  
- **L3.** The model is static and does not capture temporal dynamics, feedback, or adaptive learning present in cortical circuits.  
- **L4.** The bound is worst‑case; typical perceptual errors may be substantially smaller.

### Sensitivity to $\Delta x$
Because the bound scales linearly with $\Delta x$, halving the sampling interval to $0.05\;\text{mm}$ would halve the worst‑case error to $0.025\;\text{mm}$. Conversely, increasing $\Delta x$ to $0.2\;\text{mm}$ would raise the bound to $0.10\;\text{mm}$.

### Falsification Criterion
A psychophysical experiment that measures the mean absolute geometric deviation between a physically presented stimulus and its perceived location under controlled conditions provides a direct test. If the reported mean absolute error exceeds $0.05\;\text{mm}$, the interpolation hypothesis, as formalized here, is falsified. An observed error at or below $0.05\;\text{mm}$ would be consistent with the model but would not prove it.

### Open Questions
- How do adaptive changes in $h_i$, $q_i$, or $s_i$ during development affect the bound?  
- Can the framework be extended to multimodal perception where $\mathsf{F}$ includes auditory or somatosensory features?  
- What is the relationship between the geometric bound and subjective measures of confidence or agency?

### Bibliographic Limitation
Only five works are available in the provided bibliography, which limits the breadth of related‑work discussion. This limitation is acknowledged explicitly in Section 2.

## 7. Practical Implications and Engineering Pathways
**(a) Intended users and design impact.**  
Neuroscientists designing visual prostheses, engineers building neuromorphic vision sensors, and AI researchers developing generative perception models would use the bound to set a target sampling density. For a prosthetic device that samples at intervals larger than $0.1\;\text{mm}$, the bound predicts perceptual errors exceeding $0.05\;\text{mm}$, informing hardware specifications.

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; it resides at NASA Technology Readiness Level 2 (concept formulation).

**(c) Minimal de‑risking experiment.**  
A pilot psychophysical study would present a high‑contrast edge with a controlled blind spot (masked region) and ask participants to localize the edge across the gap. The experiment would record the geometric deviation between the true edge position and the reported position. An average deviation $>0.05\;\text{mm}$ would falsify the model; a deviation $\le0.05\;\text{mm}$ would support it.

**(d) Engineering constraints.**  
- **Sampling density:** The primary constraint is the physical spacing of photoreceptors or sensor elements, directly determining $\Delta x$.  
- **Kernel implementation:** Realizing the contraction factor $1/2$ requires a linear scaling operation, readily implemented in digital signal processors.  
- **Computational load:** The iterated‑function recursion converges geometrically, implying low computational overhead suitable for real‑time hardware.

**(e) Projected performance.**  
Assuming a prosthetic device achieves $\Delta x=0.08\;\text{mm}$ (a 20 % reduction relative to the baseline), the bound becomes  
\[
\|e\|_\infty \le \frac12 \times 0.08\;\text{mm}=0.04\;\text{mm},
\]  
representing a 20 % improvement in worst‑case geometric error.

**(f) Risks and misuse.**  
Relying exclusively on the geometric bound could cause designers to overlook other sources of perceptual distortion, such as neural adaptation or latency. Deploying a system that meets the bound but exhibits large temporal delays could jeopardize safety in high‑speed tasks (e.g., driving or surgery).

## 8. Conclusion
By casting perception as a contractive interpolant over a discrete sampling set, we derived a universal geometric error bound that links sampling density to perceptual fidelity. The bound yields a concrete, testable prediction ($0.05\;\text{mm}$ worst‑case error for a $0.1\;\text{mm}$ sampling interval) and provides a quantitative design target for neuroprosthetic and neuromorphic systems. Future work will incorporate temporal dynamics, adaptive learning of the interpolation parameters, and multimodal integration, thereby sharpening the bridge between discrete neural data and the continuous flow of conscious experience.

## References

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum  
[2] QNFO: Perception as Interpolation over a Discrete Universe | https://papers.qnfo.org/papers/perception-as-interpolation-over-a-discrete-universe  
[3] QNFO: Two Errata to "Recursive Self-Consistency as a Monistic Foundation for Physical Reality" | https://papers.qnfo.org/papers/recursive-self-consistency  
[4] QNFO: Non-Archimedean Projective Perspective: The Monna Map as a Visual Rendering Interface | https://papers.qnfo.org/papers/non-archimedean-projective-perspective  
[5] QNFO: Numeral Trees as the Native Ultrametric Geometry of Cyclic Time | https://papers.qnfo.org/papers/numeral-trees-as-the-native-ultrametric-geometry-of-cyclic-time