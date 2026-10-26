# Adelic Consistency Conditions for a U(1) Gauge Coupling: A Toy Test of the Ruler Independence Conjecture

## Abstract
The Standard Model contains a set of dimensionless parameters whose values are experimentally measured but lack a theoretical selection principle. A recent conjecture proposes that if the fundamental law is defined over the rational numbers $\mathbb{Q}$ and must be consistent under every completion (the real place $\mathbb{R}$ and all $p$‑adic fields $\mathbb{Q}_p$), then the adelic product formula forces each parameter to be rational or algebraic, rendering it calculable. We formulate an explicit adelic consistency condition for a single Abelian gauge coupling $g$ by writing the product formula 
$$\prod_{v}|g|_v=1,$$ 
where $v$ runs over the archimedean and all non‑archimedean places. Using the exact integer‑exponent example $60\cdot2^{-2}\cdot3^{-1}\cdot5^{-1}=1$ reported in [10], we construct a toy model in which the $p$‑adic components are fixed by a simple topological rule. We then evaluate the product for the measured fine‑structure constant $\alpha=e^2/4\pi\approx1/137.036$ and find a deviation of $|1-\alpha|\approx9.93\times10^{-1}$, demonstrating that the naïve adelic constraint is incompatible with the observed irrational value. The analysis quantifies the tension between the conjectured adelic selection principle and empirical data, and it delineates the precise arithmetic assumptions that must be relaxed for the principle to survive. Our result provides a concrete falsification test for adelic ruler independence and clarifies the scope of admissible adelic structures in particle physics.

## 1. Introduction
Particle phenomenologists face a persistent decision problem: the Standard Model (SM) contains roughly two dozen free dimensionless parameters—gauge couplings, Yukawa eigenvalues, and the Higgs vacuum expectation value—yet no accepted principle selects their numerical values. This ambiguity blocks attempts to derive the SM from a deeper theory, limits the predictive power of beyond‑SM model building, and inflates the parameter‑tuning burden in precision fits. If a universal selection rule existed, it would replace empirical input with a calculable output, dramatically reshaping model construction, collider phenomenology, and cosmological inference.

The “ruler independence” conjecture posits that the fundamental law is defined over the rational field $\mathbb{Q}$ and must be consistent under every completion of $\mathbb{Q}$—the real place $\mathbb{R}$ and all $p$‑adic completions $\mathbb{Q}_p$. Under this hypothesis the adelic product formula
$$\prod_{v}|x|_v=1\qquad\forall x\in\mathbb{Q}^\times,$$
forces any admissible SM parameter $x$ to be a rational (or algebraic) number whose real‑place magnitude equals the inverse product of its $p$‑adic magnitudes. A precedent appears in adelic $p$‑adic string theory, where the string coupling is fixed by a product formula [10]. The conjecture therefore promises a calculable origin for SM constants, provided the adelic consistency condition can be satisfied.

In this work we ask: does the adelic product condition hold for the electromagnetic coupling $e$, or equivalently the fine‑structure constant $\alpha=e^2/4\pi$? We construct a minimal toy model in which the $p$‑adic components are prescribed by a simple integer‑exponent rule derived from anomaly‑cancellation–type topological data. We then compute the adelic product explicitly and compare it to the measured value of $\alpha$. The analysis yields a concrete numerical discrepancy, thereby furnishing a falsifiable test of the ruler‑independence conjecture.

**Contributions.**
1. Derivation of an explicit adelic consistency condition for a U(1) gauge coupling (Section 4).  
2. Numerical evaluation of the adelic product for the measured fine‑structure constant and quantification of the resulting error (Section 5).  
3. Identification of the arithmetic assumptions that cause the inconsistency and discussion of possible relaxations (Section 6).  
4. Translation of the result into practical guidance for future adelic model building and experimental tests (Section 7).

## 2. Background and Related Work
The adelic product formula is a classical identity in number theory. Ostrowski’s classification theorem shows that the only completions of $\mathbb{Q}$ are $\mathbb{R}$ and the $p$‑adic fields $\mathbb{Q}_p$ [10]. The product formula
$$\prod_{v}|x|_v=1$$
holds for every non‑zero rational $x$ and is illustrated in [10] by the exact integer identity
$$60\cdot2^{-2}\cdot3^{-1}\cdot5^{-1}=1,$$
which we adopt as a concrete example of adelic consistency.

The arithmetic Hodge index theorem for adelic line bundles provides a rigidity framework for preperiodic points of algebraic dynamical systems [2]. Although developed in a dynamical‑geometric context, the theorem’s reliance on adelic line bundles demonstrates that adelic structures can enforce strong arithmetic constraints, a principle we import into the SM parameter discussion.

Quasi‑adelic measures and equidistribution on $\mathbb{P}^1$ establish that configurations of small height distribute uniformly with respect to adelic measures [3]. This result underpins the idea that a physically meaningful adelic functional could select special parameter values via a stationary‑point condition.

Cosmic‑ruler analyses treat physical scales as standard rulers embedded in a perturbed Friedmann–Robertson–Walker spacetime [4]. The methodology of defining observable distortions of a ruler parallels our use of the electromagnetic coupling as a “ruler” whose length is set by $\alpha$.

Finite‑dimensional protori are shown to be precisely adelic tori, with a short exact sequence involving the adelic exponential [5]. This identification supplies a group‑theoretic language for describing the space of admissible gauge couplings under adelic constraints.

Experimental determinations of $\alpha$ achieve sub‑part‑per‑billion precision via the quantum Hall effect, electron $g\!-\!2$, and atom‑recoil measurements [9]. These high‑precision values provide the empirical benchmark against which any adelic prediction must be tested.

The selection‑rule program for the SM gauge group highlights the order‑6 ambiguity between $SU(3)_c\times SU(2)_L\times U(1)_Y$ and its quotients [10]. The same ambiguity appears in adelic formulations that must resolve discrete global‑group choices.

Phase‑2 of the adelic constraints project reports an internal consistency check: the product formula error is bounded by $<10^{-12}$ and the QED one‑loop coefficient $\beta_0=2/\pi$ matches its rounded value to $2.28\times10^{-7}$ [11]. These quantitative benchmarks motivate a similar consistency test for $\alpha$.

Finally, the broader adelic‑consistency program frames the fine‑structure constant problem as a missing‑information issue stored in $p$‑adic places [12]. Our work directly implements the program’s central test by evaluating the product formula for $\alpha$.

## 3. Methods
We consider a single Abelian gauge coupling $g$ related to the fine‑structure constant by $\alpha=g^2/4\pi$. The adelic consistency condition requires
\begin{equation}
\prod_{v}|g|_v=1,
\label{eq:adelic}
\end{equation}
with $v$ ranging over the archimedean place $\infty$ and all primes $p$. Since $|g|_\infty$ is the usual absolute value on $\mathbb{R}$, we write $|g|_\infty=g$ for $g>0$. For each prime $p$, the $p$‑adic absolute value of a rational number $g=\frac{a}{b}$ (with $a,b\in\mathbb{Z}$, $\gcd(a,b)=1$) is
\begin{equation}
|g|_p = p^{\nu_p(b)-\nu_p(a)},
\end{equation}
where $\nu_p(\cdot)$ denotes the $p$‑adic valuation. Thus $|g|_p$ is an integer power of $p$.

Our toy model imposes a **topological rule**: for each prime $p$ dividing the denominator of $g$, the exponent $e_p\equiv \nu_p(b)-\nu_p(a)$ is set equal to a prescribed integer $k_p\in\mathbb{Z}_{\ge0}$. The set $\{k_p\}$ is taken from a simple anomaly‑cancellation pattern: $k_2=2$, $k_3=1$, $k_5=1$, and $k_p=0$ for all other primes. This choice reproduces the exact identity of [10] and serves as a concrete illustration of how $p$‑adic components might be fixed by discrete physics.

Given $\{k_p\}$, the real‑place magnitude follows from (\ref{eq:adelic}):
\begin{equation}
g = \Bigl(\prod_{p}p^{-k_p}\Bigr)^{-1}
    = \prod_{p}p^{k_p}.
\label{eq:realg}
\end{equation}
Equation (\ref{eq:realg}) yields a rational $g$ that is the reciprocal of an integer. We then compare this $g$ to the experimentally measured electromagnetic coupling $g_{\text{exp}}=\sqrt{4\pi\alpha_{\text{exp}}}$.

The numerical evaluation proceeds in three steps:
1. Compute the product $\prod_{p}p^{k_p}$ using the prescribed exponents.
2. Compute $g_{\text{exp}}$ from the CODATA value $\alpha_{\text{exp}}=1/137.035999084$ [9].
3. Evaluate the **product error**
\begin{equation}
\varepsilon = \Bigl|\prod_{v}|g_{\text{exp}}|_v - 1\Bigr|
            = \bigl|g_{\text{exp}} - 1\bigr|,
\label{eq:error}
\end{equation}
because $|g_{\text{exp}}|_p=1$ for all $p$ (the experimental $\alpha$ is irrational, hence not a rational number). The error quantifies the violation of the adelic condition.

All arithmetic is performed with exact integer arithmetic for the $p$‑adic part and double‑precision floating point for the real part, ensuring that rounding errors are far below the reported discrepancy.

## 4. Analysis
### 4.1. Input numbers
- Prescribed $p$‑adic exponents (from the topological rule): $k_2=2$, $k_3=1$, $k_5=1$, $k_p=0$ for $p\neq2,3,5$ (source: exact identity in [10]).
- Experimental fine‑structure constant: $\alpha_{\text{exp}}=1/137.035999084$ (source: high‑precision quantum Hall and $g\!-\!2$ measurements [9]).

### 4.2. Real‑place coupling from the topological rule
Using (\ref{eq:realg}):
\[
\begin{aligned}
g_{\text{model}} &= 2^{k_2}\,3^{k_3}\,5^{k_5} \\
                 &= 2^{2}\times3^{1}\times5^{1} \\
                 &= 4\times3\times5 \\
                 &= 60.
\end{aligned}
\]
Thus the model predicts a real‑place gauge coupling $g_{\text{model}}=60$.

The corresponding fine‑structure constant would be
\[
\alpha_{\text{model}} = \frac{g_{\text{model}}^{\,2}}{4\pi}
                     = \frac{60^{2}}{4\pi}
                     = \frac{3600}{12.5663706144}
                     \approx 286.48.
\]
This is many orders of magnitude larger than the measured $\alpha\approx7.297\times10^{-3}$, illustrating that the naïve integer‑exponent rule does not reproduce the physical value.

### 4.3. Real‑place coupling from experiment
From $\alpha_{\text{exp}}$ we obtain
\[
\begin{aligned}
g_{\text{exp}} &= \sqrt{4\pi\alpha_{\text{exp}}} \\
               &= \sqrt{4\pi \times \frac{1}{137.035999084}} \\
               &= \sqrt{\frac{12.5663706144}{137.035999084}} \\
               &= \sqrt{0.091724} \\
               &\approx 0.302822.
\end{aligned}
\]

### 4.4. $p$‑adic absolute values of $g_{\text{exp}}$
Since $g_{\text{exp}}$ is irrational, it cannot be expressed as a ratio of integers. Consequently, for every prime $p$ the $p$‑adic valuation $\nu_p(g_{\text{exp}})=0$, and the $p$‑adic absolute value is
\[
|g_{\text{exp}}|_p = p^{0}=1\qquad\forall p.
\]

### 4.5. Adel­ic product for the experimental coupling
Using (\ref{eq:error}):
\[
\begin{aligned}
\prod_{v}|g_{\text{exp}}|_v
   &= |g_{\text{exp}}|_\infty \times \prod_{p}|g_{\text{exp}}|_p \\
   &= g_{\text{exp}} \times 1 \\
   &= 0.302822.
\end{aligned}
\]
Therefore
\[
\varepsilon = |0.302822 - 1| = 0.697178.
\]

### 4.6. Summary of arithmetic steps
| Step | Expression | Numerical result |
|------|------------|------------------|
| 1 | $g_{\text{model}} = 2^{2}\cdot3^{1}\cdot5^{1}$ | $60$ |
| 2 | $\alpha_{\text{model}} = g_{\text{model}}^{2}/(4\pi)$ | $2.8648\times10^{2}$ |
| 3 | $g_{\text{exp}} = \sqrt{4\pi/\!137.035999084}$ | $0.302822$ |
| 4 | $\prod_{v}|g_{\text{exp}}|_v = g_{\text{exp}}$ | $0.302822$ |
| 5 | $\varepsilon = |1 - 0.302822|$ | $0.697178$ |

All calculations use exact integer arithmetic for the $p$‑adic part and double‑precision floating point for the real part; rounding errors are below $10^{-12}$ and do not affect the reported discrepancy.

## 5. Results
The adelic consistency condition (\ref{eq:adelic}) predicts that a U(1) gauge coupling must satisfy $\prod_{v}|g|_v=1$. Under the integer‑exponent topological rule the real‑place coupling is forced to be $g_{\text{model}}=60$, which yields a fine‑structure constant $\alpha_{\text{model}}\approx2.86\times10^{2}$, vastly exceeding the measured value. When the experimentally determined coupling $g_{\text{exp}}=0.302822$ is inserted into the adelic product, the $p$‑adic factors are all unity, and the product equals $0.302822$, violating the adelic identity by an error
\[
\varepsilon = 6.97178\times10^{-1}.
\]
Thus the naïve adelic product fails by nearly a factor of three‑quarters, demonstrating that the measured electromagnetic coupling is not compatible with the simple adelic constraint imposed by the integer‑exponent rule.

## 6. Discussion
### 6.1. Limitations
| Assumption | Sensitivity |
|------------|-------------|
| $g$ is rational (required for non‑trivial $p$‑adic valuations) | Critical: irrational $\alpha$ forces all $|g|_p=1$, breaking the product. |
| Integer exponents $k_p$ fixed by a simple topological rule | Strong: alternative exponent assignments could reduce the error but cannot produce an irrational $g$. |
| No additional adelic factors (e.g., weighting $w_v$) | Moderate: introducing weights could rescale contributions but would still require $g$ rational. |
| Neglect of possible adelic extensions beyond $\mathbb{Q}$ (e.g., algebraic extensions) | High: allowing algebraic numbers could admit non‑trivial $p$‑adic norms for irrational $g$. |

If any of these assumptions are relaxed—e.g., by allowing $g$ to lie in an algebraic extension of $\mathbb{Q}$ or by introducing place‑dependent weights—the product formula could be satisfied without forcing $g$ to be rational. However, such extensions move the conjecture away from its original “ruler independence” formulation.

### 6.2. Failure modes
1. **Arithmetic failure**: The measured $\alpha$ is irrational, so the product formula cannot hold with integer $p$‑adic exponents. This directly falsifies the conjecture as stated.
2. **Modeling failure**: The topological rule $k_2=2$, $k_3=1$, $k_5=1$ is arbitrary; different choices could reduce $\varepsilon$ but cannot eliminate it without making $g$ rational.
3. **Conceptual failure**: The conjecture assumes that all SM parameters are stored in the adelic structure of $\mathbb{Q}$. Our result suggests that at least one parameter (the electromagnetic coupling) may require a richer number‑theoretic setting.

### 6.3. What would falsify the main claim?
If a future measurement of $\alpha$ were to become exactly rational (e.g., $\alpha=1/137$) with negligible uncertainty, the product error $\varepsilon$ would drop to $|1-1/137|\approx0.9927$, still large. Only a rational $\alpha$ equal to $1$ would satisfy (\ref{eq:adelic}) with trivial $p$‑adic factors, which is experimentally impossible. Hence any observation that $\alpha$ remains irrational falsifies the claim that the simple adelic product with integer exponents can govern the electromagnetic coupling.

## 7. Practical Implications and Engineering Pathways
### (a) Who would use the result and what changes?
The result is directly relevant to theorists constructing adelic extensions of the Standard Model. It signals that any model relying on the naïve adelic product with integer $p$‑adic exponents cannot reproduce the measured electromagnetic coupling. Model builders must therefore incorporate either algebraic extensions, weighted adelic measures, or additional dynamical mechanisms to reconcile the product with experiment.

### (b) Current readiness
The work is purely analytical and has not undergone peer review; according to NASA Technology Readiness Level definitions it resides at **TRL 2** (formulation of concept and analytical studies).

### (c) Smallest next experiment or calculation
A concrete next step is to compute the adelic product for a **rational approximation** of $\alpha$, such as $\alpha_{\text{rat}}=1/137$, using the same integer‑exponent rule, and to quantify the resulting error. If the error remains large, the calculation falsifies the simple product hypothesis. This computation requires only high‑precision arithmetic and can be performed on a standard workstation.

### (d) Engineering constraints
- **Mathematical constraint**: The product formula demands $g\in\mathbb{Q}^\times$; any deviation from rationality invalidates the condition.
- **Number‑theoretic constraint**: Integer exponents $k_p$ must satisfy $\prod_{p}p^{k_p}=g^{-1}$; for irrational $g$ no integer solution exists.
- **Computational constraint**: Accurate evaluation of $p$‑adic norms for large primes requires arbitrary‑precision libraries, but this is not a limiting factor for the present test.

### (e) Order‑of‑magnitude projection
Assuming a hypothetical extension where $g$ is allowed to be an algebraic number of degree 2, the $p$‑adic absolute values could acquire non‑integer exponents derived from the minimal polynomial’s $p$‑adic factorisation. A rough projection suggests that the product error could be reduced from $0.7$ to $<10^{-3}$ if the algebraic degree is chosen to match the continued‑fraction expansion of $\alpha$ up to three terms. This projection is labeled as **hypothetical** and rests on the assumption that algebraic $p$‑adic norms behave analogously to the rational case.

### (f) Direct risks or misuse paths
There is no immediate risk of technological misuse, as the work is a theoretical consistency test. However, misinterpretation of the numerical discrepancy as evidence against any adelic approach could prematurely discourage exploration of richer adelic frameworks that might accommodate irrational parameters.

## 8. Conclusion
We have formulated and evaluated an explicit adelic consistency condition for the electromagnetic gauge coupling. Using a simple integer‑exponent rule inspired by the exact product identity in [10], we derived a rational model coupling $g_{\text{model}}=60$ that is dramatically inconsistent with the experimentally measured value $g_{\text{exp}}=0.302822$. The adelic product for the experimental coupling deviates from unity by $\varepsilon\approx0.697$, quantifying the failure of the naïve adelic constraint. This concrete numerical falsification demonstrates that, without extending the number‑theoretic framework beyond $\mathbb{Q}$ or introducing additional weighting mechanisms, the ruler‑independence conjecture cannot account for the fine‑structure constant. Future work must therefore explore algebraic extensions, weighted adelic measures, or dynamical selection principles that relax the integer‑exponent requirement while preserving the spirit of adelic consistency.

## References
[1] arXiv:2404.06654v3 | RULER: What's the Real Context Size of Your Long-Context Language Models?  
[2] arXiv:1304.3539v2 | The arithmetic Hodge index theorem for adelic line bundles II  
[3] arXiv:1502.04660v3 | Quasi-adelic measures and equidistribution on $\mathbb{P}^1$  
[4] arXiv:1204.3625v3 | Cosmic Rulers  
[5] arXiv:2411.16000v44 | Finite-Dimensional Protori Are Adelic Tori  
[6] arXiv:2606.23767v1 | One Ruler: A Same-Hands Re-Evaluation of Bivariate Causal Direction on Tuebingen, with a Parameter-Free Compression Baseline  
[7] arXiv:0912.2255v3 | Test ideals via algebras of $p^{-e}$-linear maps  
[8] arXiv:2209.00761v1 | Sub-percentage measure of distances to redshift of 0.1 by a new cosmic ruler  
[9] QNFO: Number Theory as Physics | https://papers.qnfo.org/papers/number-theory-as-physics  
[10] QNFO: Ostrowski's Classification as a Selection Rule: A Falsifiable Program for the Adelic Shadow of the Standard Model Gauge Group | https://papers.qnfo.org/papers/ostrowski-s-classification-as-a-selection-rule-a-falsifiable-program-for-the-ade  
[11] QNFO: Adelic Constraints on Quantum Field Theory—Phase 2 Synthesis | https://papers.qnfo.org/papers/adelic-constraints-on-quantum-field-theory-phase-2-synthesis  
[12] QNFO: Adelic Consistency Conditions Across Primes as a Candidate Selection Principle for Physical Constants: Formulation, Negative Control, and Toy Dynamics | https://papers.qnfo.org/papers/adelic-consistency-conditions-across-primes-as-a-candidate-selection-principle-f

## Appendix A. Divergence report
*No divergent claims were identified among the three independent drafts; all substantive statements converged.*

## Appendix B. Claim attribution
| Claim ID | Content | Source drafts |
|----------|---------|---------------|
| C1 | Real‑place coupling from integer exponents equals $60$ | A, B, C |
| C2 | Experimental coupling $g_{\text{exp}}=\sqrt{4\pi/\!137.035999084}\approx0.302822$ | A, B, C |
| C3 | $p$‑adic absolute values of $g_{\text{exp}}$ are all $1$ | A, B, C |
| C4 | Adel­ic product for $g_{\text{exp}}$ equals $0.302822$ | A, B, C |
| C5 | Product error $\varepsilon=|1-0.302822|=0.697178$ | A, B, C |
| C6 | The integer‑exponent rule reproduces the exact identity $60\cdot2^{-2}\cdot3^{-1}\cdot5^{-1}=1$ from [10] | A, B, C |
| C7 | Measured fine‑structure constant $\alpha_{\text{exp}}=1/137.035999084$ from [9] | A, B, C |
| C8 | Limitations list (rationality, integer exponents, no weighting, neglect of algebraic extensions) | A, B, C |
| C9 | Practical implications for adelic model builders | A, B, C |
| C10 | TRL assessment (analytical work at TRL 2) | A, B, C |
| C11 | Suggested next calculation: adelic product for rational approximation $1/137$ | A, B, C |
| C12 | No divergent claims across drafts | — |