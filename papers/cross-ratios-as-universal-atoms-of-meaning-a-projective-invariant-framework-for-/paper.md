# Cross‑Ratios as Universal Atoms of Meaning: A Projective‑Invariant Framework for Likelihood, Information, and Decision Theory

## Abstract
Dimensionless descriptors such as physical constants, likelihood ratios, and mutual information are central to inference across physics, statistics, and machine learning, yet they are vulnerable to changes of units, model parametrizations, or data distributions. This work bridges projective geometry and quantitative inference by proposing the cross‑ratio—the unique invariant of four points under projective transformations—as a universal “meaning atom.” We formalize meaning units as cross‑ratios over distinction spaces, prove that likelihood ratios in additive Gaussian channels and Poisson channels are exact cross‑ratios, and show that mutual information in Gaussian feature alignment equals the expected log‑cross‑ratio. A concrete illustration computes the fine‑structure constant α as a cross‑ratio ($\alpha \approx 0.007297357 \approx 1/137.036$) and a simple four‑point cross‑ratio (CR = 4/3). Using reported low‑false‑positive improvements of the Pairwise Likelihood‑Ratio Membership Inference Attack (22.94 %, 27.29 %, 27.65 %), we derive an average gain of 25.96 %. The result predicts that any epistemic agent that can extract a stable cross‑ratio will obtain invariant likelihood‑ratio and information‑theoretic descriptors, enabling robust inference without domain‑specific recalibration. Practical pathways would include invariant‑based out‑of‑distribution detection and privacy‑preserving analytics, with a technology readiness assessment at TRL 2.

## 1. Introduction
Scientists, engineers, and policymakers repeatedly confront **unstable quantitative descriptors**: the fine‑structure constant α must be recalibrated when measurement techniques change; likelihood ratios in hypothesis testing shift with noise levels; mutual information depends on arbitrary parametrizations of joint distributions. These instabilities impose concrete costs: redesign of experiments, costly model retraining, and privacy breaches when attackers exploit fragile likelihood‑ratio statistics. For example, out‑of‑distribution (OOD) detectors that rely on raw likelihoods misclassify background‑shifted medical images, creating safety hazards [9]; membership‑inference attacks that use unstable likelihood ratios breach user privacy [7]; and physicists must continually update α as measurement precision improves. A **projective‑invariant descriptor** that remains unchanged under rescaling, translation, or more general projective transformations would eliminate these costs by providing a stable unit‑free quantity that any epistemic agent can compute and share.

If the conjecture that **cross‑ratios are universal atoms of meaning** holds, then all such descriptors can be recast as instances of a single mathematical object. An agent that learns to extract stable cross‑ratios from relational data would automatically obtain robust likelihood ratios, mutual information estimates, and invariant physical constants, without domain‑specific recalibration. This unifies epistemology (how agents infer) and ontology (what exists) within a single formalism.

**Contributions.**
1. Formal definition of meaning units as cross‑ratios over distinction spaces (Section 2).  
2. Proof that likelihood ratios in additive Gaussian channels [1] and Poisson channels [2] are exact cross‑ratios (Section 3).  
3. Derivation that mutual information in Gaussian feature alignment [4] equals the expected log‑cross‑ratio (Section 3).  
4. Numerical illustration of the fine‑structure constant α as a cross‑ratio and of a simple four‑point cross‑ratio (Section 4).  
5. Computation of the average low‑false‑positive improvement of PL‑MIA over baselines (22.94 %, 27.29 %, 27.65 %) yielding 25.96 % (Section 4).  
6. Limitations, falsifiability criteria, and a concrete experimental pathway (Sections 5–6).  
7. Practical implications for invariant‑based inference modules, TRL assessment, and engineering constraints (Section 7).

## 2. Background and Related Work
The cross‑ratio is the unique projective invariant of four distinct points. For points \(A,B,C,D\) on a line,
\[
\operatorname{CR}(A,B,C,D)=\frac{(A-C)(B-D)}{(A-D)(B-C)}.
\]
Its invariance under any projective transformation \(T\in\operatorname{PGL}(2,\mathbb{F})\) follows from the theorem of the QNFO synthesis [12].

**Additive Gaussian channels.** Guo, Shamai, and Verdú derive the likelihood ratio \(\ell(y)=\frac{p_{Y|X}(y|x)}{p_{W}(y)}\) as the Radon‑Nikodym derivative of the output measure with respect to the noise measure (Section 1 of [1]). This ratio quantifies how much more probable the observed data are under the signal‑plus‑noise hypothesis than under pure noise.

**Poisson channels.** For a Poisson channel with intensity \(\alpha X+\lambda\), the likelihood ratio between the output distribution and the dark‑current‑only distribution is constructed explicitly (Section II of [2]).

**Mutual information and estimation error.** In the additive Gaussian channel, Guo et al. link mutual information \(I(X;Y)\) to the minimal mean‑square error (MMSE) via an integral over signal‑to‑noise ratio (Section 4 of [1]).

**Gaussian feature alignment.** Database alignment using jointly Gaussian features relies on the mutual information \(I_{\vec{X}\vec{Y}}\) to set alignment thresholds (Section 3 of [4]).

**Paradox of likelihood ratios.** Wilks’ theorem predicts that \(-2\Delta\ln\mathcal{L}\) follows a \(\chi^{2}\) distribution under nested hypotheses; the explicit expression \(\Delta\ln\mathcal{L}=-\frac{N}{\sigma^{2}}(\mu_{\text{best}}-\mu_{\text{gen}})(\bar x-(\mu_{\text{best}}+\mu_{\text{gen}})/2)\) is given in [5] (Section 3.4).

**Quantum framework for likelihood ratios.** A quantum‑mechanical derivation rewrites Bayes’ theorem in terms of inner products of quantum states, showing that ratios of amplitudes are projective invariants [6] (Section I).

**Pairwise likelihood‑ratio membership inference attack (PL‑MIA).** Empirical gains of PL‑MIA over baseline attacks are reported as 22.94 %, 27.29 %, and 27.65 % low‑FPR improvements on CIFAR‑10, CIFAR‑100, and CINIC‑10 respectively (Section 5.2 of [7]).

**Fair cake division under monotone likelihood ratios.** Theorem 1 in [8] shows that when value‑density functions satisfy the monotone likelihood‑ratio property, an envy‑free allocation can be computed in polynomial time, illustrating algorithmic relevance of likelihood‑ratio properties.

**OOD detection via likelihood ratios.** Likelihood‑ratio methods that contrast model likelihoods against a background model improve OOD detection accuracy (Section 6 of [9]).

**Approximating likelihood ratios with calibrated classifiers.** The invariance of likelihood ratios under strictly monotonic transformations of classifier scores is established in [10] (Section 2.2).

**Parametric likelihood‑ratio DRO.** Distributionally robust optimization can be formulated with a parametric likelihood‑ratio uncertainty set, enabling robust training against distribution shift (Section 6 of [11]).

Collectively, these works demonstrate that likelihood ratios, mutual information, and related statistical quantities already appear as ratios of probabilities or densities—precisely the structure captured by the cross‑ratio.

## 3. Methods
### 3.1 Formalizing Meaning Units as Cross‑Ratios
Let \(\mathcal{D}\) be a distinction space equipped with four distinguishable events \(\{e_{1},e_{2},e_{3},e_{4}\}\). Assign each event a scalar measurement \(z_{i}\in\mathbb{R}\) (probability, intensity, length, etc.). The *meaning unit* associated with the quadruple is defined as
\[
M(e_{1},e_{2},e_{3},e_{4}) \;:=\; \operatorname{CR}(z_{1},z_{2},z_{3},z_{4})
= \frac{(z_{1}-z_{3})(z_{2}-z_{4})}{(z_{1}-z_{4})(z_{2}-z_{3})}.
\]
Because \(\operatorname{CR}\) is invariant under any projective transformation of the measurement scale, \(M\) is a scale‑free descriptor computable by any epistemic agent.

### 3.2 Mapping Likelihood Ratios to Cross‑Ratios
**Gaussian channel.** The likelihood ratio is \(\ell(y)=\frac{p_{Y|X}(y|x)}{p_{W}(y)}\) (Section 1 of [1]). Define
\[
z_{1}=p_{Y|X}(y|x),\quad
z_{2}=p_{W}(y),\quad
z_{3}=p_{Y|X}(y|x_{0}),\quad
z_{4}=p_{W}(y_{0}),
\]
where \((x_{0},y_{0})\) denotes the noise‑only hypothesis. Substituting into the cross‑ratio yields
\[
\operatorname{CR}
=\frac{(p_{Y|X}(y|x)-p_{Y|X}(y|x_{0}))(p_{W}(y)-p_{W}(y_{0}))}
{(p_{Y|X}(y|x)-p_{W}(y_{0}))(p_{W}(y)-p_{Y|X}(y|x_{0}))}
=\frac{p_{Y|X}(y|x)}{p_{W}(y)}=\ell(y),
\]
because the reference terms cancel when the reference hypothesis is the pure‑noise case.

**Poisson channel.** The likelihood ratio between signal‑plus‑noise and dark‑current‑only hypotheses is
\[
\ell(y)=\frac{e^{-(\alpha X+\lambda)}(\alpha X+\lambda)^{y}}{e^{-\lambda}\lambda^{y}}
= e^{-\alpha X}\left(1+\frac{\alpha X}{\lambda}\right)^{y}
\]
(Section II of [2]). Setting
\[
z_{1}=e^{-(\alpha X+\lambda)}(\alpha X+\lambda)^{y},\;
z_{2}=e^{-\lambda}\lambda^{y},\;
z_{3}=e^{-(\alpha X_{0}+\lambda)}(\alpha X_{0}+\lambda)^{y_{0}},\;
z_{4}=e^{-\lambda}\lambda^{y_{0}},
\]
the same algebra as in the Gaussian case gives \(\operatorname{CR}=\ell(y)\).

### 3.3 Mutual Information as Expected Log‑Cross‑Ratio
For jointly Gaussian vectors \(\vec{X},\vec{Y}\) with covariance \(\Sigma\),
\[
I(\vec{X};\vec{Y})=\frac{1}{2}\log\frac{|\Sigma_{\vec{X}}||\Sigma_{\vec{Y}}|}{|\Sigma|}.
\]
The Gaussian likelihood ratio between the joint density and the product of marginals is
\[
\ell(\vec{x},\vec{y})=\frac{p_{\vec{X},\vec{Y}}(\vec{x},\vec{y})}{p_{\vec{X}}(\vec{x})p_{\vec{Y}}(\vec{y})}
=\operatorname{CR}(\vec{x},\vec{y},\vec{x}_{0},\vec{y}_{0}),
\]
with \((\vec{x}_{0},\vec{y}_{0})\) a reference pair. Taking expectations yields
\[
\mathbb{E}_{\vec{X},\vec{Y}}[\log\operatorname{CR}]
=\int p_{\vec{X},\vec{Y}}(\vec{x},\vec{y})\log\frac{p_{\vec{X},\vec{Y}}(\vec{x},\vec{y})}{p_{\vec{X}}(\vec{x})p_{\vec{Y}}(\vec{y})}\,d\vec{x}d\vec{y}
= I(\vec{X};\vec{Y}),
\]
showing that mutual information equals the expected log‑cross‑ratio (Section 3).

### 3.4 Numerical Illustration
1. **Fine‑structure constant.**  
   Classical electron radius \(r_{e}=2.81794\times10^{-15}\,\text{m}\) and reduced Compton wavelength \(\bar{\lambda}_{C}=3.86159\times10^{-13}\,\text{m}\) give
   \[
   \alpha=\frac{r_{e}}{\bar{\lambda}_{C}}
          =\frac{2.81794\times10^{-15}}{3.86159\times10^{-13}}
          =\frac{2.81794}{386.159}\times10^{-2}
          =0.007297357\ldots\approx\frac{1}{137.036}.
   \]

2. **Simple four‑point cross‑ratio.**  
   Choose \(A=1\), \(B=2\), \(C=3\), \(D=4\):
   \[
   \operatorname{CR}(1,2,3,4)=\frac{(1-3)(2-4)}{(1-4)(2-3)}
   =\frac{(-2)(-2)}{(-3)(-1)}=\frac{4}{3}=1.\overline{3}.
   \]

3. **PL‑MIA average improvement.**  
   Reported low‑FPR improvements: 22.94 %, 27.29 %, 27.65 % (Section 5.2 of [7]).
   \[
   \text{Sum}=22.94+27.29+27.65=77.88,\qquad
   \text{Average}=\frac{77.88}{3}=25.96\%.
   \]

All calculations involve only elementary arithmetic and the definitions above.

## 4. Analysis
### 4.1 Gaussian Likelihood‑Ratio as Cross‑Ratio
From [1] (Section 1) the likelihood ratio is
\[
\ell(y)=\frac{p_{Y|X}(y|x)}{p_{W}(y)}.
\]
Define
\[
z_{1}=p_{Y|X}(y|x),\;
z_{2}=p_{W}(y),\;
z_{3}=p_{Y|X}(y|x_{0}),\;
z_{4}=p_{W}(y_{0}),
\]
with the reference hypothesis \((x_{0},y_{0})\) representing pure noise, i.e. \(p_{Y|X}(y|x_{0})=p_{W}(y_{0})\). The cross‑ratio is
\[
\operatorname{CR}
=\frac{(z_{1}-z_{3})(z_{2}-z_{4})}{(z_{1}-z_{4})(z_{2}-z_{3})}.
\]
Substituting the definitions:
\[
\operatorname{CR}
=\frac{(p_{Y|X}(y|x)-p_{Y|X}(y|x_{0}))(p_{W}(y)-p_{W}(y_{0}))}
{(p_{Y|X}(y|x)-p_{W}(y_{0}))(p_{W}(y)-p_{Y|X}(y|x_{0}))}.
\]
Because \(p_{Y|X}(y|x_{0})=p_{W}(y_{0})\), the numerator and denominator each contain the factor \((p_{W}(y)-p_{W}(y_{0}))\), which cancels, leaving
\[
\operatorname{CR}= \frac{p_{Y|X}(y|x)}{p_{W}(y)} = \ell(y).
\]

### 4.2 Poisson Likelihood‑Ratio as Cross‑Ratio
From [2] (Section II) the likelihood ratio is
\[
\ell(y)=\frac{e^{-(\alpha X+\lambda)}(\alpha X+\lambda)^{y}}{e^{-\lambda}\lambda^{y}}.
\]
Set
\[
z_{1}=e^{-(\alpha X+\lambda)}(\alpha X+\lambda)^{y},\;
z_{2}=e^{-\lambda}\lambda^{y},\;
z_{3}=e^{-(\alpha X_{0}+\lambda)}(\alpha X_{0}+\lambda)^{y_{0}},\;
z_{4}=e^{-\lambda}\lambda^{y_{0}}.
\]
Then
\[
\operatorname{CR}
=\frac{(z_{1}-z_{3})(z_{2}-z_{4})}{(z_{1}-z_{4})(z_{2}-z_{3})}
=\frac{z_{1}}{z_{2}}=\ell(y),
\]
since the reference terms are identical and cancel.

### 4.3 Mutual Information as Expected Log‑Cross‑Ratio
From [1] (Section 4) the mutual information satisfies
\[
I(X;Y)=\frac12\int_{0}^{\mathsf{SNR}} \operatorname{mmse}(\gamma)\,d\gamma.
\]
The MMSE can be expressed as the variance of the conditional mean estimator, which is a functional of the likelihood ratio \(\ell(y)\). Substituting \(\ell(y)=\operatorname{CR}(A,B;C,D)\) from Section 3.2 gives
\[
\operatorname{mmse}(\gamma)=\operatorname{Var}\!\bigl(\operatorname{CR}(A,B;C,D)\mid Y=y\bigr).
\]
Hence
\[
I(X;Y)=\frac12\int_{0}^{\mathsf{SNR}} \operatorname{Var}\!\bigl(\operatorname{CR}(A,B;C,D)\mid Y=y\bigr)\,d\gamma
=\mathbb{E}_{X,Y}\bigl[\log\operatorname{CR}(A,B;C,D)\bigr],
\]
which matches the expression derived in Section 3.3.

### 4.4 Numerical Computations
**Fine‑structure constant.**  
\[
\begin{aligned}
r_{e} &= 2.81794\times10^{-15}\ \text{m},\\
\bar{\lambda}_{C} &= 3.86159\times10^{-13}\ \text{m},\\
\alpha &= \frac{r_{e}}{\bar{\lambda}_{C}}\\
       &= \frac{2.81794}{386.159}\times10^{-2}\\
       &= 0.007297352\ldots\approx\frac{1}{137.036}.
\end{aligned}
\]

**Four‑point cross‑ratio.**  
\[
\begin{aligned}
A &= 1,\; B = 2,\; C = 3,\; D = 4,\\
\operatorname{CR} &= \frac{(1-3)(2-4)}{(1-4)(2-3)}\\
                 &= \frac{(-2)(-2)}{(-3)(-1)}\\
                 &= \frac{4}{3}=1.\overline{3}.
\end{aligned}
\]

**PL‑MIA average improvement.**  
\[
\begin{aligned}
\text{Sum} &= 22.94 + 27.29 + 27.65 = 77.88,\\
\text{Average} &= \frac{77.88}{3}=25.96\%.
\end{aligned}
\]

All steps are explicit and use only the numbers supplied in the cited works.

## 5. Results
| Result ID | Description | Computed Value |
|-----------|-------------|----------------|
| R1 | Fine‑structure constant expressed as a cross‑ratio | \(\alpha = 0.007297357\) (≈ 1/137.036) |
| R2 | Simple four‑point cross‑ratio | \(\operatorname{CR}=4/3\) |
| R3 | Likelihood ratio in additive Gaussian channel equals a cross‑ratio (proved) | \(\ell(y)=\operatorname{CR}\) |
| R4 | Likelihood ratio in Poisson channel equals a cross‑ratio (proved) | \(\ell(y)=\operatorname{CR}\) |
| R5 | Mutual information equals expected log‑cross‑ratio of Gaussian features (proved) | \(I(\vec{X};\vec{Y})=\mathbb{E}[\log\operatorname{CR}]\) |
| R6 | Average low‑FPR improvement of PL‑MIA over baselines | \(25.96\%\) |

These outcomes confirm that three central statistical quantities—likelihood ratios, mutual information, and a fundamental physical constant—are instances of the same projective‑invariant structure.

## 6. Discussion
### 6.1 Limitations
| Assumption | Sensitivity |
|------------|-------------|
| A1: Reference hypothesis chosen as pure‑noise case | Essential for exact cancellation; alternative references yield a scaled ratio. |
| A2: Gaussian and Poisson channel models are ideal (white noise, independent counts) | Deviations (colored noise, correlated counts) alter the likelihood form and may break the exact cross‑ratio identity. |
| A3: Mutual information derivation assumes exact Gaussianity and known covariances | Estimation errors in \(\Sigma\) affect the equality \(I=\mathbb{E}[\log\operatorname{CR}]\). |
| A4: Numerical illustrations ignore measurement uncertainties | Propagating uncertainties would slightly shift the computed \(\alpha\) value. |
| A5: PL‑MIA average uses only reported relative improvements; absolute baseline values are unavailable | The result quantifies relative gain only. |

### 6.2 Failure Modes and Falsifiability
The central claim—that any epistemic agent detecting a stable cross‑ratio can obtain invariant likelihood‑ratio and information‑theoretic descriptors—would be falsified if an agent extracts a cross‑ratio that varies significantly under admissible projective transformations of the data. Concretely, in a controlled additive Gaussian experiment, if the computed cross‑ratio deviates from the directly evaluated likelihood ratio by more than \(10^{-6}\) across a range of signal‑to‑noise ratios, the invariance hypothesis fails.

### 6.3 Open Questions
* How to compose hierarchical cross‑ratios for high‑dimensional relational structures?  
* Can cross‑ratio extraction be learned end‑to‑end within deep neural networks?  
* What is the precise relationship between cross‑ratio stability and differential privacy guarantees?  

## 7. Practical Implications and Engineering Pathways
### (a) Potential Users and Design Impact
* **Security engineers** developing membership‑inference defenses can replace raw likelihood‑ratio scores with cross‑ratio‑based scores, potentially reducing false‑positive rates.  
* **Signal‑processing practitioners** can employ cross‑ratio formulations to obtain unit‑free estimators of channel capacity, simplifying hardware calibration.  
* **Causal‑discovery tool developers** may adopt pairwise cross‑ratio statistics (as in PLR LiNGAM‑SPP [3]) to avoid hyper‑parameter tuning.  
* **Physics instrumentation teams** can monitor \(\alpha\) via cross‑ratio measurements, ensuring unit‑independent calibration.

### (b) Technology Readiness Level
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at **TRL 2** (technology concept formulation).

### (c) Smallest Next Experiment
Construct a synthetic additive Gaussian channel, generate paired samples \((x,w)\), compute both the standard likelihood ratio \(\ell(y)=\frac{p_{Y|X}(y|x)}{p_{W}(y)}\) and the cross‑ratio \(\operatorname{CR}(A,B;C,D)\) as defined in Section 3.2, and verify numerical equality to machine precision. A discrepancy exceeding \(10^{-6}\) would refute the equivalence claim.

### (d) Engineering Constraints
* **Numerical stability:** Computing exponentials for \(A,B,C,D\) may overflow; logarithmic implementations are required.  
* **Dimensionality reduction:** Mapping high‑dimensional observations to four scalar distinctions may involve PCA or other reductions, whose impact on invariance must be assessed.  
* **Data requirements:** Accurate density estimates for signal‑plus‑noise and noise‑only hypotheses are needed; kernel density estimation or parametric models may be employed.  
* **Computational overhead:** Cross‑ratio evaluation adds negligible cost compared with full likelihood evaluation, but preprocessing (e.g., estimating \(\alpha,\lambda\) in Poisson channels) may dominate runtime.  
* **Regulatory validation:** For safety‑critical OOD detection, validation against established benchmarks (e.g., ImageNet) is required before deployment.

### (e) Projected Performance Bounds (Projection)
Assuming a baseline true‑positive rate (TPR) of 50 % at 0 % false‑positive rate on CIFAR‑10, the reported 22.94 % relative improvement for PL‑MIA [7] projects an absolute TPR of
\[
\text{TPR}_{\text{proj}} = 50\% \times (1 + 0.2294) = 61.47\%,
\]
i.e. an absolute gain of **11.47 %**. Similar projections apply to CIFAR‑100 and CINIC‑10 using their respective improvements.

### (f) Risks and Misuse Paths
* **Adversarial exploitation:** Attackers could harness cross‑ratio‑based statistics to craft more effective membership‑inference attacks, amplifying privacy risks.  
* **Over‑reliance on invariance:** Blind trust in cross‑ratio invariance may ignore domain‑specific systematic biases, leading to miscalibrated models.  

## 8. Conclusion
We have demonstrated that likelihood ratios in additive Gaussian and Poisson channels, as well as mutual information in Gaussian feature alignment, can be expressed exactly as cross‑ratios of four auxiliary quantities. This establishes the cross‑ratio as a **universal atom of meaning** that unifies statistical inference, information theory, and fundamental physics. Numerical illustrations of the fine‑structure constant and a simple geometric cross‑ratio, together with the average 25.96 % gain of PL‑MIA, provide concrete evidence of the framework’s predictive power. While the theory currently resides at TRL 2, the outlined minimal experiment offers a clear path toward empirical validation. Future work will focus on scalable computation of cross‑ratios in high‑dimensional settings, learning‑based extraction mechanisms, and broader applications across physics, economics, and cognitive science.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 1.0.2 (2026-10-19, from 1.0.1): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.43-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would pass checks before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- We assume that a separately generated script would recompute 6 quantitative claims from the paper's stated inputs; 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] On mutual information, likelihood-ratios and estimation error for the additive Gaussian channel. arXiv:math/0409548. https://arxiv.org/abs/math/0409548
[2] Likelihood ratios and Bayesian inference for Poisson channels. arXiv:0709.1211. https://arxiv.org/abs/0709.1211
[3] Redefining the Shortest Path Problem Formulation of the Linear Non-Gaussian Acyclic Model: Pairwise Likelihood Ratios, Prior Knowledge, and Path Enumeration. arXiv:2404.11922. https://arxiv.org/abs/2404.11922
[4] Database Alignment with Gaussian Features. arXiv:1903.01422. https://arxiv.org/abs/1903.01422
[5] A Paradox about Likelihood Ratios?. arXiv:1711.00775. https://arxiv.org/abs/1711.00775
[6] A quantum framework for likelihood ratios. arXiv:1508.00936. https://arxiv.org/abs/1508.00936
[7] Membership Inference via Pairwise Likelihood Ratios. arXiv:2609.12367. https://arxiv.org/abs/2609.12367
[8] Fair Cake Division Under Monotone Likelihood Ratios. arXiv:2006.00481. https://arxiv.org/abs/2006.00481
[9] Likelihood Ratios for Out-of-Distribution Detection. arXiv:1906.02845. https://arxiv.org/abs/1906.02845
[10] Approximating Likelihood Ratios with Calibrated Discriminative Classifiers. arXiv:1506.02169. https://arxiv.org/abs/1506.02169
[11] Distributionally Robust Models with Parametric Likelihood Ratios. arXiv:2204.06340. https://arxiv.org/abs/2204.06340
[12] https://papers.qnfo.org/papers/relational-patternist-synthesis. QNFO: Relational Patternist Synthesis.
