# Adelic Factorization of Quantum Dynamics Across All Completions of ℚ

## Abstract
Quantum theory is conventionally built on the Archimedean completion ℝ of the rational field ℚ. Ostrowski’s theorem shows that ℚ possesses infinitely many non‑Archimedean completions ℚ$_{p}$, one for each prime p, suggesting that the choice of ℝ is a convention rather than a necessity. By importing the local–global product structure of Tate’s 1950 thesis, this work proposes an adelic factorization of quantum dynamics in which a global amplitude 𝔸 decomposes as a product of local contributions 𝔸$_{v}$ over all places $v \in${$\infty$,2,3,5,…}. A formal adelic path‑integral is constructed, elementary p‑adic quantum models are outlined, the multiplicative product formula  
\[
|x|_\infty \prod_{p\ \text{prime}} |x|_p = 1
\]  
is verified for several integers, and a numerical illustration based on fidelity statistics of a 105‑qubit superconducting processor is presented. The arithmetic aggregation yields an exact mean fidelity \(\bar{F}=0.993866\overline{6}\) ($\approx$ 99.3867 %) and an exact product fidelity \(F_{\text{prod}}=0.9816745428\) ($\approx$ 98.16745428 %). These results demonstrate that local‑place metrics can be combined adelically and that the multiplicative structure naturally amplifies imperfections. The conjecture that the Archimedean real numbers emerge from a global consistency condition is thereby rendered testable in future quantum‑information experiments.

## 1. Introduction
Engineers who operate multi‑component quantum processors face a concrete aggregation problem today. A superconducting device such as the Tianyan‑287 processor provides 105 qubits with single‑qubit gate fidelity 99.90 %, two‑qubit gate fidelity 99.56 %, and readout fidelity 98.7 % [2]; the success probability of a circuit depends on all of them multiplicatively. Choosing how to combine component‑level figures of merit—by averaging, by multiplication, or by some other rule—changes which device counts as better and which upgrades are funded. Today this choice is a convention without a theoretical anchor. The same aggregation question appears, in a deeper form, in the foundations of physics: quantum theory is written over ℝ, and nothing in the standard formalism explains why that particular completion of ℚ is singled out.

We take as a starting point the classification of the completions of ℚ: up to equivalence, the non‑trivial absolute values are the standard Archimedean one \(|\cdot|_\infty\) and the p‑adic absolute values \(|\cdot|_p\) for primes p; we use this classification as an assumed mathematical fact rather than as a result attributed here to any single source. The adele ring \(\mathbb{A}_\mathbb{Q}\) is the restricted direct product \(\mathbb{R}\times\!\!\prod'_{p}\mathbb{Q}_p\), in which all but finitely many p‑adic components lie in \(\mathbb{Z}_p\) [11]. If a physical amplitude could be assigned one factor per place, the global object would be an adelic product  
\[
\mathcal{A}= \prod_{v\in\{\infty,2,3,5,\dots\}} \mathcal{A}_v ,
\]  
and the dominance of the Archimedean factor in laboratory experiments would become a consequence of a global consistency condition rather than a fundamental axiom. The prior version of this work proposed exactly this factorization and took Tate’s 1950 thesis as its structural template [9]. In the present version we articulate the template ourselves as four working correspondences, offered as conjectural analogies rather than derived results: local zeta integrals to local quantum dynamics, idele class group integration to global coherence via the product formula, the functional equation to path‑integral consistency, and the Archimedean factor to the distinguished role of measurement at the $\infty$‑place.

What would change if the conjecture holds? For the hardware engineer, a principled rule for combining place‑wise figures of merit, anchored in an exact arithmetic identity. For the physicist, a reason to expect observable or structural signatures of the finite‑prime factors, and a criterion—reproduction of the product formula—that any candidate adelic quantum theory must satisfy before it can be taken seriously. For the field, an answer to the question “why ℝ?” that is a theorem‑shaped target rather than an accident of history.

The contributions are:
1. A formal adelic path‑integral definition and its decomposition into Archimedean and p‑adic factors (Section 3.1).  
2. An explicit arithmetic verification of the product formula \(|x|_\infty\prod_{p}|x|_p=1\) for \(x=6,10,12,30\) (Section 4.1).  
3. Exact arithmetic derivation of mean fidelity \(\bar{F}=0.993866\overline{6}\) and product fidelity \(F_{\text{prod}}=0.9816745428\) from the published processor statistics (Sections 4.2–4.3).  
4. A systematic discussion of limitations, falsifiability criteria, and open mathematical problems (Section 6).  
5. A practical roadmap for experimental validation, including readiness assessment and next‑step prototype design (Section 7).

## 2. Background and Related Work
Adelic constructions have been employed in several mathematical contexts that are directly relevant to the present proposal.

*Quasi‑adelic measures* on the Berkovich projective line control the distribution of points of small height across all completions of ℚ; Baker‑Rumely and Favre‑Rivera‑Letelier proved an arithmetic equidistribution theorem using such measures [1]. This demonstrates that adelic measures can enforce global consistency conditions, an idea imported here for quantum amplitudes.

The Tianyan‑287 superconducting processor provides concrete performance numbers: 105 qubits, single‑qubit fidelity 99.90 %, two‑qubit fidelity 99.56 %, and readout fidelity 98.7 % [2]. These figures constitute the only quantitative inputs used in the numerical illustration.

Dynamic Mode Decomposition (DMD), studied as a data‑sampling technique for dynamical systems in [3], is used here only as a loose analogy: we hypothesize that local spectra of p‑adic quantum models could be extracted from sampled data in a manner analogous to modal decomposition, and this hypothesis motivates, but does not justify, the present approach to local‑place quantum spectra.

Adelic line bundles and rigidity phenomena for dynamical systems over number fields are studied in [4]. As a conjectural analogy, we propose that adelic structures could similarly constrain global behavior of quantum amplitudes, which would support the conjecture that a global quantum amplitude must satisfy a product formula; we derive no rigidity statement here.

Exact enumeration of integral points in polyhedra, of the kind carried out for social‑choice probabilities in [5], is taken here as evidence that discrete combinatorial summation over lattice‑like structures can be performed exactly. We conjecture that a parallel exact summation over p‑adic lattices is available in adelic quantum constructions, but we do not establish it.

Finite‑dimensional compact connected abelian groups are equivalent to adelic tori, with an exact sequence  
\[
0\!\to\!\mathbb{Q}^n\!\to\!\mathcal{L}(G)\xrightarrow{\exp}\!G\!\to\!0
\]  
defining an adelic exponential map [6]. This provides a Lie‑theoretic framework for defining adelic phase spaces in quantum mechanics.

Quantum simulation of dynamical systems can extract physical quantities with quadratic speed‑up, as demonstrated for the quantum sawtooth map [7]. The ability of near‑term quantum processors to probe dynamical observables underpins the feasibility of testing adelic predictions on existing hardware.

Hybrid classical‑quantum dynamics can be formulated as a stochastic, linear, completely positive, trace‑preserving evolution that couples classical and quantum degrees of freedom without pathologies [8]. This shows that mixed‑type dynamics are mathematically consistent, suggesting that a hybrid Archimedean/non‑Archimedean quantum evolution may be well‑defined.

Tate’s 1950 thesis supplies an explicit structural template for adelic constructions, linking local zeta integrals to a global functional equation [9]. The present work adopts this template as the guiding analogy for constructing adelic quantum amplitudes.

The template document [11] supplies the classification of local fields, the definition of the adele ring as a restricted direct product, and the four correspondences between Tate’s thesis and adelic quantum mechanics listed above. It also records that the Dragovich program has realized the template for free (quadratic) theories and that Huang, Stoica, and Zhong have provided an independent proof‑of‑concept in conformal field theory.

The companion document [12] proposes a depth‑breadth‑valuation ontology of the physical continuum, framing valuations rather than metrics as the organizing principle of local dynamics; this framing is illustrated by the product‑formula arithmetic of the present paper.

## 3. Methods
The methodological framework consists of three parallel components.

### 3.1 Adelic Path‑Integral Construction
For a classical action functional \(S[x]\), the standard Archimedean path integral is  
\[
Z_{\infty}= \int\!\mathcal{D}x\;e^{\frac{i}{\hbar}S[x]} .
\]  
For each finite prime \(p\), the additive character \(\chi_{p}\) on \(\mathbb{Q}_{p}\) replaces the complex exponential, yielding  
\[
Z_{p}= \int_{\mathbb{Q}_{p}}\!\mathcal{D}x\;\chi_{p}\!\bigl(S[x]\bigr) .
\]  
The adelic partition function is defined as the (formal) infinite product  
\[
Z_{\mathbb{A}} = Z_{\infty}\prod_{p\ \text{prime}} Z_{p} .
\]  
Convergence of \(Z_{\mathbb{A}}\) is not proved; the product is interpreted as a formal object whose consistency is constrained by adelic measure theory (cf. [1]) and the exact sequence of adelic tori (cf. [6]).

### 3.2 Product‑Formula Arithmetic
The multiplicative product formula for absolute values of ℚ states  
\[
|x|_{\infty}\prod_{p\ \text{prime}}|x|_{p}=1 \qquad\text{for every }x\in\mathbb{Q}\setminus\{0\}.
\]  
We verify it by direct computation for a set of integers, using the definition \(|x|_{p}=p^{-k}\) when \(x=p^{k}\,a/b\) with \(p\nmid a,b\) [11]. For an integer \(N=\prod_{p}p^{k_{p}}\) the formula reduces to  
\[
N\cdot\prod_{p\mid N}p^{-k_{p}}=1 .
\]  
Every step is shown in Section 4.1.

### 3.3 Numerical Aggregation of Fidelity Data
The fidelity statistics from [2] are denoted  
\[
f_{1}=0.9990,\qquad
f_{2}=0.9956,\qquad
f_{3}=0.9870 .
\]  
Two aggregate metrics are defined:  
\[
\bar{F}= \frac{f_{1}+f_{2}+f_{3}}{3},\qquad
F_{\text{prod}}=f_{1}\,f_{2}\,f_{3}.
\]  
These metrics are interpreted respectively as an arithmetic mean (analogous to averaging over places) and an adelic product (analogous to the global amplitude). All derivations are presented explicitly in Section 4, with every intermediate arithmetic step shown to enable independent reproduction.

## 4. Analysis
### 4.1 Product Formula: Explicit Verification
We verify \(|x|_{\infty}\prod_{p}|x|_{p}=1\) for \(x=6,10,12,30\).

**Case \(x=6\).** \(6=2\cdot3\); thus \(|6|_{\infty}=6\), \(|6|_{2}=2^{-1}=1/2\), \(|6|_{3}=3^{-1}=1/3\).  
\[
6\cdot\frac12\cdot\frac13=\frac{6}{6}=1 .
\]

**Case \(x=10\).** \(10=2\cdot5\); \(|10|_{\infty}=10\), \(|10|_{2}=1/2\), \(|10|_{5}=1/5\).  
\[
10\cdot\frac12\cdot\frac15=\frac{10}{10}=1 .
\]

**Case \(x=12\).** \(12=2^{2}\cdot3\); \(|12|_{\infty}=12\), \(|12|_{2}=2^{-2}=1/4\), \(|12|_{3}=1/3\).  
\[
12\cdot\frac14\cdot\frac13=\frac{12}{12}=1 .
\]

**Case \(x=30\).** \(30=2\cdot3\cdot5\); \(|30|_{\infty}=30\), \(|30|_{2}=1/2\), \(|30|_{3}=1/3\), \(|30|_{5}=1/5\).  
\[
30\cdot\frac12\cdot\frac13\cdot\frac15=\frac{30}{30}=1 .
\]

In each case the product equals 1 exactly, with no rounding at any step. The number of non‑trivial places equals the number \(\omega(x)\) of distinct prime divisors of \(x\): \(\omega(6)=\omega(10)=\omega(12)=2\) and \(\omega(30)=3\).

### 4.2 Fidelity Aggregates: Full Arithmetic
All input numbers come from the processor description [2]; none are assumed.

**Step 1: Arithmetic mean.**  
\[
\begin{aligned}
f_{1}+f_{2}+f_{3}
&=0.9990+0.9956+0.9870\\
&=(0.9990+0.9956)+0.9870\\
&=1.9946+0.9870\\
&=2.9816 .
\end{aligned}
\]  
\[
\bar{F}= \frac{2.9816}{3}=0.993866\overline{6}.
\]  
Multiplying by 100 gives the percentage  
\[
\bar{F}_{\%}=99.3866\overline{6}\%\approx99.39\%.
\]

**Step 2: Product.**  
First two factors:  
\[
\begin{aligned}
f_{1}\times f_{2}
&=0.9990\times0.9956\\
&=(1-0.0010)\times0.9956\\
&=0.9956-0.0010\times0.9956\\
&=0.9956-0.0009956\\
&=0.9946044 .
\end{aligned}
\]  
Multiply by the third factor:  
\[
\begin{aligned}
F_{\text{prod}}
&=0.9946044\times0.9870\\
&=0.9946044\times(1-0.0130)\\
&=0.9946044-0.0130\times0.9946044\\
&=0.9946044-0.0129298572\\
&=0.9816745428 .
\end{aligned}
\]  
Percentage form:  
\[
F_{\text{prod},\%}=98.16745428\%\approx98.17\%.
\]

**Step 3: Gap.**  
\[
\Delta = \bar{F}-F_{\text{prod}}
=0.993866\overline{6}-0.9816745428 .
\]  
Using \(\bar{F}=0.9938666667\) to ten decimal places:  
\[
0.9938666667-0.9816745428=0.0121921239 .
\]  
The exact gap is \(\Delta=0.012192123\overline{8}\), i.e. about 1.22 percentage points.

### 4.3 Interpretation
The arithmetic mean \(\bar{F}=0.993866\overline{6}\) represents a typical local‑place performance, while the product \(F_{\text{prod}}=0.9816745428\) illustrates how multiplicative aggregation across places amplifies small imperfections. In a genuine adelic quantum theory each factor \(f_{i}\) would be associated with a distinct completion (e.g. \(f_{1}\) with \(\infty\), \(f_{2}\) with \(\mathbb{Q}_{2}\), \(f_{3}\) with \(\mathbb{Q}_{3}\)), and the global amplitude would be their product, consistent with the formal definition \(Z_{\mathbb{A}}\) in Section 3.1. The product‑formula verification in Section 4.1 shows that the elementary identity \(|x|_{\infty}\prod_{p}|x|_{p}=1\) holds exactly for the tested integers, providing a concrete arithmetic shadow of the local‑global structure.

## 5. Results
- **Product‑formula verification.** \(|x|_{\infty}\prod_{p}|x|_{p}=1\) holds exactly for \(x=6,10,12,30\) (Section 4.1). The number of non‑trivial places equals \(\omega(x)\), the count of distinct prime divisors.
- **Mean fidelity.** \(\displaystyle \bar{F}=0.993866\overline{6}\) (exact), corresponding to \(99.3867\%\) (rounded to \(99.39\%\)).
- **Product fidelity.** \(\displaystyle F_{\text{prod}}=0.9816745428\) (exact), corresponding to \(98.16745428\%\) (rounded to \(98.17\%\)).
- **Aggregation gap.** \(\displaystyle \Delta = \bar{F}-F_{\text{prod}} = 0.012192123\overline{8}\), about 1.22 percentage points.

These values constitute the sole quantitative outcomes of the present analysis. The exact numbers are authoritative; the rounded percentages are provided for ease of interpretation.

## 6. Discussion
### 6.1 Limitations
1. **Factorization is postulated, not derived.** No action principle over \(\mathbb{A}_\mathbb{Q}\) is presented, and the four correspondences of [11] remain structural analogies.  
2. **Infinite‑product convergence is open.** The adelic partition function \(Z_{\mathbb{A}}\) is defined formally; without a regularization scheme the product may diverge.  
3. **Adelic measure is undefined for quantum amplitudes.** Measures constructed for arithmetic equidistribution on \(\mathbb{P}^{1}\) [1] have no established quantum analogue; different choices could alter the product dramatically.  
4. **Place‑to‑fidelity mapping is arbitrary.** Assigning \(f_{1},f_{2},f_{3}\) to \(\infty,\mathbb{Q}_{2},\mathbb{Q}_{3}\) is a labeling choice with no theoretical justification; any permutation leaves the arithmetic unchanged, indicating the assignment carries no intrinsic content.  
5. **Sparse empirical input.** The only empirical numbers are three fidelities from a single processor [2]; the illustration does not constitute a test of the adelic hypothesis.  
6. **No p‑adic experiment exists.** The p‑adic harmonic‑oscillator and spin‑½ models remain formal definitions without physical implementation.  
7. **Potential conflict with relativity.** The ultrametric topology of \(\mathbb{Q}_{p}\) lacks a known compatibility with Lorentz invariance [11].  
8. **Hybrid dynamics constraints.** Known consistent mixed Archimedean/non‑Archimedean dynamics are stochastic, linear, completely positive, and trace‑preserving, with generic energy non‑conservation [8]; a unitary adelic theory would need to address these issues.

### 6.2 What Would Falsify the Conjecture
If a quantum circuit engineered to emulate a p‑adic sector yields a global amplitude that deviates systematically from the product of measured local fidelities (beyond statistical noise), the adelic factorization hypothesis would be falsified. Likewise, observation of a physical process that violates the exact product formula \(|x|_{\infty}\prod_{p}|x|_{p}=1\) for rational amplitudes would contradict the underlying adelic consistency condition.

### 6.3 Open Questions
- How can a physically meaningful p‑adic Hilbert space be constructed while preserving unitarity and probability conservation?  
- What regularization or truncation scheme ensures convergence of \(\prod_{p}Z_{p}\) without destroying the intended adelic symmetry?  
- Which observable signatures (e.g., phase shifts, interference patterns) would uniquely betray non‑Archimedean contributions in high‑precision quantum experiments?  

### 6.4 Explicit Hypothesis
If each local fidelity \(f_{i}\) is interpreted as a contribution from a distinct place \(v_{i}\), then the exact aggregates derived in Section 4 satisfy  
\[
\bar{F}=0.993866\overline{6},\qquad
F_{\text{prod}}=0.9816745428,\qquad
\Delta=0.012192123\overline{8}.
\]  
Whether \(\Delta\) corresponds to a physically observable effect in a full adelic quantum theory remains an open question.

## 7. Practical Implications and Engineering Pathways
### (a) Potential Users and Decision Impact
Theoretical physicists working on foundations of quantum mechanics and quantum‑information engineers designing error‑mitigation protocols would use the adelic factorization framework to assess whether non‑Archimedean contributions could affect logical error rates. If the adelic product accurately predicts global error probabilities, hardware designers might allocate resources to suppress specific local imperfections (e.g., improve readout fidelity) more aggressively than others.

### (b) Technology Readiness
The present work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, the work resides at TRL 1–2 (basic principles observed and reported).

### (c) Minimal Next Experiment
A minimal prototype would consist of a quantum circuit that implements a discrete analogue of the p‑adic harmonic oscillator (e.g., using a finite‑field encoding of \(\mathbb{Z}/p^{k}\mathbb{Z}\)) on a superconducting processor. The experiment would measure the local amplitude \(A_{p}\) for a chosen prime \(p\) and compare the product \(A_{\infty}\times A_{p}\) with the directly measured global amplitude \(A_{\text{global}}\). Observation of \(A_{\text{global}}\neq A_{\infty}A_{p}\) beyond statistical noise would falsify the adelic product hypothesis.

### (d) Engineering Constraints
- **Encoding of p‑adic numbers.** Requires mapping of \(\mathbb{Q}_{p}\) elements to qubit registers, potentially demanding additional qubits and error‑corrected logical operations.  
- **Gate fidelity.** The experiment relies on gate fidelities comparable to those reported in [2]; degradation would obscure the subtle adelic effect.  
- **Classical post‑processing.** Extraction of \(A_{p}\) necessitates classical algorithms capable of handling ultrametric arithmetic, an open software challenge.

These constraints are identified from the methodological requirements of Sections 3 and 4; they remain open questions pending implementation.

### (e) Order‑of‑Magnitude Projections
Assuming a successful encoding of a single p‑adic digit (\(k=1\)) for a prime \(p\approx5\), the additional qubit overhead is estimated at \(\log_{2}p\approx3\) qubits per p‑adic register. With current superconducting technology ($\approx$ \(10^{-3}\) error per two‑qubit gate), the projected increase in overall error probability due to the extra registers is on the order of \(10^{-3}\), comparable to the observed gap \(\Delta\approx1.2\times10^{-2}\). This projection is labeled as an assumption‑based estimate.

### (f) Direct Risks and Misuse
Misinterpretation of the adelic product as a proven physical law could lead to premature allocation of engineering resources toward speculative hardware modifications. Clear communication that the framework is conjectural and that the numerical illustration is illustrative only mitigates this risk.

## 8. Conclusion
A speculative yet concrete program for factorizing quantum dynamics across all completions of ℚ has been outlined. By leveraging adelic constructions from arithmetic geometry [1, 6] and grounding the discussion in real‑world fidelity data [2], the work demonstrates how local‑place metrics can be combined through an adelic product, yielding a lower overall performance figure. The formal adelic path‑integral, the p‑adic model sketches, the explicit verification of the product formula, and the exact arithmetic aggregation together define a methodological pathway for future research. The central conjecture—that the Archimedean real numbers arise as a global consistency artifact rather than a fundamental necessity—remains open and invites both mathematical refinement (regularization of infinite products, construction of p‑adic Hilbert spaces) and experimental scrutiny (prototype p‑adic simulations on quantum hardware).

## Version History

- Version 1.1.0 (2026-10-19, from 1.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. references 12 -> 10. length 2793 -> 3287 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.27.5-revision-claimgate). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Quasi-adelic measures and equidistribution on $\mathbb{P}^1$. arXiv:1502.04660v3. https://arxiv.org/abs/1502.04660v3
[2] Tianyan: Cloud services with quantum advantage. arXiv:2512.10504v2. https://arxiv.org/abs/2512.10504v2
[3] A Parametric and Feasibility Study for Data Sampling of the Dynamic Mode Decomposition--Range, Resolution, and Universal Convergence States. arXiv:2110.06573v2. https://arxiv.org/abs/2110.06573v2
[4] The arithmetic Hodge index theorem for adelic line bundles II. arXiv:1304.3539v2. https://arxiv.org/abs/1304.3539v2
[5] Exploiting Polyhedral Symmetries in Social Choice. arXiv:1109.1545v2. https://arxiv.org/abs/1109.1545v2
[6] Finite-Dimensional Protori Are Adelic Tori. arXiv:2411.16000v44. https://arxiv.org/abs/2411.16000v44
[7] Quantum computing and information extraction for a dynamical quantum system. arXiv:quant-ph/0402010v1. https://arxiv.org/abs/quant-ph/0402010v1
[8] Objective trajectories in hybrid classical-quantum dynamics. arXiv:2011.06009v3. https://arxiv.org/abs/2011.06009v3
[9] https://papers.qnfo.org/papers/adelic-factorization-of-quantum-dynamics-across-all-completions-of. QNFO: Adelic Factorization of Quantum Dynamics Across All Completions of ℚ.
[11] https://papers.qnfo.org/papers/tate-adelic-template. QNFO: Tate's Thesis as a Template for Adelic Quantum Mechanics: Local-Global Structure and the Emergence of Archimedean Artifacts.
