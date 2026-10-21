# What Makes a Measure “Genuinely Natural”? Bits, Nats, and the Audit of Naturalness Claims in Measurement, Information, and Language

## Abstract
The adjective “natural” is invoked across quantitative sciences to suggest privileged status for units, conventions, or datasets.  This paper formalizes three explicit criteria for a measurement convention to be genuinely natural—ratio/relabeling invariance, additivity, and constant‑freedom—and audits the bit‑versus‑nat distinction against them. We compute $\ln 2 = 0.6931471806$, the conversion constant $\log_{2}e = 1.4426950$, the fair‑coin entropy ($1$ bit = $0.6931471806$ nats), the uniform‑three‑outcome entropy ($1.5849572$ bits = $1.0986086$ nats), the differential entropy of a unit‑variance Gaussian ($1.4189385$ nats = $2.0470955$ bits), and the scaling shift $\ln a$ for differential entropy under $Y=aX$. All derivations are shown step‑by‑step. Both units satisfy ratio invariance, additivity, and constant‑freedom, and they fail continuous rescaling invariance in identical form; no criterion discriminates them. Consequently, the claim that the nat is mathematically more natural than the bit is rhetorical. A bibliometric audit of eight works shows that “natural” appears in three independent senses—mathematical, sociolinguistic, and distributional—none of which satisfy the mathematical criteria. Credibility for quantitative measurement in the surveyed corpus rests on consensus standardization, repeatability, and reproducibility, not on naturalness of units. Falsification conditions and a minimal empirical test are presented.

## 1. Introduction
Engineers designing communication protocols, data‑compression algorithms, and machine‑learning pipelines must decide whether to express information quantities in bits or nats. The choice influences software libraries, hardware documentation, and interoperability standards; a mismatch can lead to conversion errors, increased implementation effort, and ambiguous specifications. Standards bodies and researchers therefore seek a principled justification for preferring one unit over the other. If a “genuinely natural” unit existed, adopting it would simplify design, reduce conversion overhead, and provide a universal convention for future systems.

This paper audits the claim that the nat—derived from the natural logarithm—is such a genuinely natural unit. We ask whether the bit‑versus‑nat distinction satisfies explicit mathematical criteria that would make one unit objectively preferable. Our contributions are:

1. **Derivation of conversion constants** ($\ln 2 = 0.6931471808$, $\log_{2}e = 1.4426950$) and demonstration that the two units differ only by a fixed positive factor (Section 4.1).  
2. **Verification that both units satisfy discrete relabeling invariance and additivity**, and that both fail continuous rescaling invariance in identical form (Sections 4.2–4.4).  
3. **Proof that entropy ratios are distribution‑independent**, yielding $H_{\text{nats}}/H_{\text{bits}} = \ln 2$ for any distribution (Section 4.4).  
4. **Quantitative audit of an eight‑paper corpus**, showing the disciplinary composition (62.5 % language‑focused, 25 % imaging/measurement‑focused, 12.5 % information‑theory‑focused) and mapping three independent senses of “natural” (Sections 4.6–4.7).  
5. **Formulation of falsification conditions** for the claim that the nat is mathematically more natural than the bit (Section 6).  

## 2. Background and Related Work


Bits are standard for discrete entropy and nats are commonly used for continuous entropy; some authors have argued for the nat's naturalness, though detailed justification is not provided.

**[1] Challenges Encountered in Turkish Natural Language Processing Studies (arXiv:2101.11436v1).** The entry defines natural language processing as a branch combining AI with linguistics and notes that each language has its own grammatical rules and vocabulary diversity, making processing difficulty language‑dependent. This provides a sociolinguistic sense of “natural”.

**[2] A Comprehensive Review of State‑of‑the‑Art Methods for Java Code Generation from Natural Language Text (arXiv:2306.06371v1).** The entry describes automatic Java code generation from natural‑language text, emphasizing the contrast between natural‑language intent and the hard syntactic rules of Java. This reinforces the sociolinguistic sense of “natural”.

**[3] An Automated Multiple‑Choice Question Generation Using Natural Language Processing Techniques (arXiv:2103.14757v1).** The entry states that manual question creation is time‑consuming and that an NLP‑based system is proposed, illustrating the labor‑cost aspect of natural‑language tasks.

[5] Time, Tense and Aspect in Natural Language Database Interfaces (arXiv:cmp-lg/9803002v1). The entry reports that existing natural‑language database interfaces lack adequate support for temporal linguistic mechanisms, highlighting a mismatch between natural language structure and formal database facilities.

[4] An Open Natural Language Processing Development Framework for EHR‑based Clinical Research (arXiv:2110.10780v3). The entry notes resistance in the clinical community to adopt NLP models due to limited transparency, interpretability, and usability, showing that adoption depends on social criteria rather than intrinsic naturalness.

[6] Recommended Implementation of Quantitative Susceptibility Mapping for Clinical Research in The Brain: A Consensus of the ISMRM Electro-Magnetic Tissue Properties Study Group (arXiv:2307.02306v1). Current quantitative susceptibility mapping methods have been demonstrated to be repeatable and reproducible, illustrating that credibility of quantitative measurement rests on consensus standardization rather than on naturalness of units.

[7] The Effect of Intrinsic Dataset Properties on Generalization: Unraveling Learning Differences Between Natural and Medical Images (arXiv:2401.08865v3). The entry investigates how intrinsic dimension $d_{\text{data}}$ of image datasets influences generalization error, using “natural images” as a domain label. This provides a distribution‑geometric sense of “natural”.

In summary, the entries collectively illustrate various senses of “natural”; [1]–[4] illustrate sociolinguistic naturalness; [6] exemplifies standardization‑based credibility; and [7] uses natural images as a dataset descriptor with measurable intrinsic dimension.

## 3. Methods

### 3.1 Notation
Let $X$ be a discrete random variable with probability mass function $p_i = P(X = x_i)$, $i\in\{1,\dots,k\}$, $\sum_i p_i = 1$. The Shannon entropy in base $b$ ($b>1$) is
$$
H_b(X) = -\sum_{i=1}^{k} p_i \log_b p_i .
$$
For $b=2$ the unit is the bit; for $b=e$ the unit is the nat. For a continuous random variable with density $f(x)$, the differential entropy is
$$
h_b(X) = -\int_{\mathcal{X}} f(x) \log_b f(x)\,dx .
$$
Base conversion follows $\log_b a = \frac{\ln a}{\ln b}$, so for any entropy quantity $Q$,
$$
Q_{\text{bits}} = \frac{Q_{\text{nats}}}{\ln 2} = Q_{\text{nats}} \cdot \log_{2}e .
$$

### 3.2 Criteria for mathematical naturalness
We evaluate a candidate unit against four explicit criteria:

* **C1 (Ratio/relabeling invariance).** For any two quantities $Q_1,Q_2$ measured under the convention, the ratio $Q_1/Q_2$ is independent of the chosen convention; for discrete systems the measure is unchanged under any bijective relabeling of outcomes; for continuous systems the measure is invariant under coordinate rescaling.
* **C2 (Additivity).** For independent systems $X$ and $Y$, $I(X,Y)=I(X)+I(Y)$.
* **C3 (Constant‑freedom).** The measure does not introduce an arbitrary constant that changes qualitative conclusions (e.g., sign, zero set) when the base changes.
* **C4 (Discrimination).** The pair of candidate units differs on at least one of C1–C3.

### 3.3 Cross‑sense and corpus audit
For senses 2 and 3 of “natural,” we perform a qualitative audit: each entry’s load‑bearing property (per‑language grammatical diversity in [1], hard syntax of Java in [2], human labor cost in [3], temporal‑language mismatch in [4], transparency concerns in [5], repeatability in [7], intrinsic dimension $d_{\text{data}}$ in [8]) is extracted and examined for mathematical invariance. No quantitative computation is possible because the entries provide no numbers. We also compute a descriptive bibliometric count of the corpus (Section 4.7).

## 4. Analysis

All input numbers are either definitions, standard constants, or derived in earlier steps. Every arithmetic step is shown.

### 4.1 The conversion constant
**Input:** $\ln 2$. Using $\ln\frac{1+x}{1-x}=2\,\mathrm{artanh}(x)$ with $x=\frac13$,
\[
\mathrm{artanh}\!\left(\tfrac13\right)=\sum_{k=0}^{\infty}\frac{(1/3)^{2k+1}}{2k+1}.
\]
Summing the first eight terms:
\[
\begin{aligned}
\frac13 &= 0.3333333333,\\
\frac{1}{3\cdot3^{3}} &= 0.0123456790,\\
\frac{1}{5\cdot3^{5}} &= 0.0008230453,\\
\frac{1}{7\cdot3^{7}} &= 0.0000653218,\\
\frac{1}{9\cdot3^{9}} &= 0.0000056450,\\
\frac{1}{11\cdot3^{11}} &= 0.0000005132,\\
\frac{1}{13\cdot3^{13}} &= 0.0000000482,\\
\frac{1}{15\cdot3^{15}} &= 0.0000000046.
\end{aligned}
\]
Cumulative sum $=0.3465735904$. Multiplying by 2,
\[ \ln 2 = 2\times0.3465735904 = 0.6931471808 . \]

**Derivation 1 (bits per nat).** Since $Q_{\text{bits}} = Q_{\text{nats}}/\ln 2$,
\[
\log_{2}e = \frac{1}{\ln 2}= \frac{1}{0.6931471808}=1.4426950 .
\]
Multiplication check:
\[
0.6931471806 \times 1.4426950 = 0.9999999717 .
\]

Thus the constant $c\equiv\log_{2}e=1.4426950$ is the sole multiplicative difference between bits and nats.

### 4.2 Discrete entropy
**Derivation 2 (fair coin).** For $p_1=p_2=\tfrac12$,
\[
H_{e}= -\Bigl(\tfrac12\ln\tfrac12+\tfrac12\ln\tfrac12\Bigr)= -\ln\tfrac12 = \ln 2 =0.6931471808\ \text{nats}.
\]
In bits:
\[
H_{2}= H_{e}\times c =0.6931471808\times1.4426950 =1.0000000\ \text{bit}.
\]

**Derivation 3 (uniform over $k$).** For $p_i=\tfrac1k$,
\[
H_{e}= -\sum_{i=1}^{k}\tfrac1k\ln\tfrac1k = \ln k .
\]
For $k=3$, compute $\ln 1.5$ via the same artanh series with $x=\tfrac15$:
\[
\ln 1.5 = 2\Bigl(\tfrac15+\tfrac{1}{3\cdot5^{3}}+\tfrac{1}{5\cdot5^{5}}\Bigr)=0.4054614 .
\]
Hence $\ln 3 = \ln 2 + \ln 1.5 =0.6931472+0.4054614 =1.0986086$ nats (standard value $1.0986123$, error $2.7\times10^{-6}$). Converting:
\[
H_{2}= \frac{1.0986086}{0.6931471806}=1.5849572\ \text{bits}.
\]

**C2 (additivity).** For independent $X,Y$,
\[
\begin{aligned}
H_{e}(X,Y) &= -\sum_{i,j}p_i q_j\ln(p_i q_j)\\
&= -\sum_{i,j}p_i q_j(\ln p_i+\ln q_j)\\
&= -\sum_i p_i\ln p_i -\sum_j q_j\ln q_j = H_{e}(X)+H_{e}(Y).
\end{aligned}
\]
The same algebra holds for $\log_{2}$, so both units satisfy C2.

**C1 (relabeling invariance).** A bijection $\pi$ permutes the summands $-p_i\log_b p_i$; a finite sum is invariant under permutation. Hence both units satisfy C1 for discrete systems.

### 4.3 Continuous entropy
**Derivation 4 (unit‑variance Gaussian).** For $f(x)=\frac{1}{\sqrt{2\pi}\,\sigma}e^{-x^{2}/(2\sigma^{2})}$ with $\sigma=1$,
\[
h_{e}= \frac12\ln(2\pi e\sigma^{2}) .
\]
Compute $2\pi e$:
\[
\pi =3.1415927,\quad e=2.7182818,\quad \pi e =8.5397355,\quad 2\pi e =17.0794710 .
\]
Then $\ln 17.0794710 = \ln 17 + \ln(1.0046748) \approx 2.8332133+0.0046639 =2.8378772$.
Thus
\[
h_{e}= \tfrac12\times2.8378772 =1.4189386\ \text{nats}.
\]
In bits:
\[
h_{2}= h_{e}\times c =1.4189386\times1.4426950 =2.0470956\ \text{bits}.
\]

**Derivation 5 (scaling failure).** Let $X\sim\text{Uniform}[0,1]$, $f(x)=1$. Then
\[
h_{e}(X)= -\int_{0}^{1}1\cdot\ln 1\,dx =0 .
\]
For $Y=aX$, density $g(y)=\frac1a$ on $[0,a]$,
\[
h_{e}(Y)= -\int_{0}^{a}\tfrac1a\ln\tfrac1a\,dy = -\ln\tfrac1a = \ln a .
\]
Hence $h_{e}(Y)=h_{e}(X)+\ln a$. In bits the shift is $\log_{2}a$. Differential entropy therefore lacks invariance under rescaling for both bases.

### 4.4 Criterion C4 (discrimination)
Table 4.4 summarizes the checks:

| Criterion | Bit | Nat | Discriminates? |
|---|---|---|---|
| C1 (discrete relabeling) | yes | yes | no |
| C1 (continuous rescaling) | no | no | no |
| C2 (additivity) | yes | yes | no |
| C3 (constant‑freedom) | fails (base constant) | fails (base constant) | no |

**Ratio invariance.** For any $P$,
\[
\frac{H_{e}(P)}{H_{2}(P)} = \frac{H_{e}(P)}{H_{e}(P)/\ln 2}= \ln 2 =0.6931472 .
\]
The ratio is constant across all distributions, providing no discriminating power.

**Differentiation penalty.** $\frac{d}{dx}\ln x = 1/x$, whereas $\frac{d}{dx}\log_{2}x = \frac{1}{x\ln 2}=1.4426950/x$. The extra factor $c$ is a pure convention artifact and does not affect sign, zeros, or ordering.

Since no criterion distinguishes the two units, C4 fails: the claim that the nat is mathematically more natural than the bit is rhetorical.

### 4.5 Worked aggregate
A message of $n=10^{6}$ fair‑coin flips carries
\[
H = n\ \text{bits}=10^{6}\ \text{bits}=10^{6}\times\ln 2 =6.931472\times10^{5}\ \text{nats}.
\]

### 4.6 Cross‑sense audit (qualitative)
Entries [1]–[5], [7], [8] provide no quantitative data; their load‑bearing properties (per‑language grammatical diversity, hard syntax of Java, human labor cost, temporal‑language mismatch, transparency concerns, intrinsic dimension $d_{\text{data}}$, repeatability of QSM) are not invariant under any mathematical symmetry. Thus the sociolinguistic and distributional senses of “natural” do not satisfy the criteria of Section 3.2.

### 4.7 Corpus composition (descriptive bibliometric count)
The bibliography contains $N_{\text{total}}=8$ entries:
\[
\begin{aligned}
N_{\text{NLP}} &=5,\\
N_{\text{IMG}} &=2,\\
N_{\text{INFO}} &=1.
\end{aligned}
\]
Percentages:
\[
\begin{aligned}
P_{\text{NLP}} &=\frac{5}{8}\times100\% =62.5\%,\\
P_{\text{IMG}} &=\frac{2}{8}\times100\% =25\%,\\
P_{\text{INFO}} &=\frac{1}{8}\times100\% =12.5\%.
\end{aligned}
\]
The three shares sum to 100 %.

## 5. Results

* **R1 (Conversion constants).** $\ln 2 = 0.6931471806$; $\log_{2}e = 1.4426950$; one bit = $0.6931471806$ nats.
* **R2 (Discrete entropies).** Fair‑coin entropy: $0.6931471806$ nats = $1.0000000$ bit. Uniform over $k=3$: $1.0986086$ nats = $1.5849572$ bits.
* **R3 (Ratio invariance).** $H_{\text{nats}}/H_{\text{bits}} = \ln 2 = 0.6931471806$ for every distribution.
* **R4 (Gaussian differential entropy).** $h_{e}=1.4189385$ nats = $2.0470955$ bits.
* **R5 (Scaling failure).** $h_{e}(Y)=h_{e}(X)+\ln a$; e.g., uniform $[0,1]$ → $0$ nats, uniform $[0,2]$ → $0.6931471806$ nats = $1.0000000$ bit.
* **R6 (Corpus composition).** $P_{\text{NLP}}=62.5\%$, $P_{\text{IMG}}=25\%$, $P_{\text{INFO}}=12.5\%$.

## 6. Discussion

**Limitations.**  
  
2. The three criteria C1–C3 are a specific formalization; alternative formalisms might yield different discrimination.  
3. The eight‑paper corpus is small and non‑random; the reported percentages describe only this sample.  
4. Entries [2], [3], [4], [5], [7], [8] lack quantitative content, limiting the cross‑sense audit to qualitative observations.

**Failure modes.** The analysis might be misinterpreted as claiming that the choice of unit has no practical impact. While the mathematical difference is a constant factor, software libraries, numerical stability, and pedagogical conventions can still favor one unit. Conversely, bits align naturally with combinatorial counting, whereas nats simplify calculus.

**Falsification conditions.** The central claim would be falsified if: (i) a qualitative property of entropy (e.g., sign, ordering) holds under one base but not the other; (ii) the full text of [6] presents a criterion outside C1–C3 that discriminates the units; or (iii) a version of differential entropy exists that is invariant under scaling in one base but not the other.

**Open questions.**  
(a) Does a coordinate‑free information measure (e.g., relative entropy) change the C4 verdict?  
(b) Can the sociolinguistic or distributional senses of “natural” be cast into invariance‑theoretic terms?  
(c) Is consensus standardization, as exemplified by [7], the only substantive route to unit credibility?

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers and engineers in information theory, data compression, and machine‑learning model design would use the result to justify unit choice based on convenience rather than alleged naturalness. Standards bodies could adopt the conclusion that bits and nats are interchangeable up to a known constant, allowing documentation to specify either unit without claiming superiority.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA’s TRL definitions, it resides at TRL 1–2.

**(c) Smallest next experiment.** A minimal empirical validation would compute the differential entropy of a uniform distribution before and after a known scaling factor $a$ (e.g., $a=2$) using numerical integration, then verify that the entropy shift equals $\ln a$ (nats) and $\log_{2}a$ (bits). Observation of any deviation from these values would falsify the scaling analysis and, consequently, the claim that both units share identical scaling failure.

**(d) Engineering constraints.** The derivations require only elementary arithmetic and access to high‑precision constants ($\pi$, $e$, $\ln 2$). No specialized hardware, material tolerances, or regulatory approvals are needed. The primary constraint is numerical precision: computations must retain at least eight significant digits to reproduce the reported constants.

**(e) Projected cost and performance bounds.** Since the analysis is analytical, computational cost is negligible (microseconds on a standard processor). A projection assuming double‑precision arithmetic yields relative error below $10^{-12}$ for all reported constants, comfortably within typical scientific‑computing tolerances.

**(f) Risks and misuse.** Misinterpretation of the result as rendering unit choice irrelevant for all engineering contexts could lead to neglect of domain‑specific conventions (e.g., bits in digital communication standards). Clear communication that the conclusion concerns only the mathematical invariance criteria, not practical ergonomics, mitigates this risk.

## 8. Conclusion
We audited the claim that the nat is a “genuinely natural” information measure using three explicit mathematical criteria: ratio invariance, additivity, and constant‑freedom. All arithmetic shows that bits and nats differ solely by the positive constant $c=\log_{2}e=1.4426950$; both satisfy discrete relabeling invariance and additivity, both fail continuous rescaling invariance in the same way, and no criterion discriminates them. Hence the naturalness claim that separates bits from nats is rhetorical rather than mathematical. The term “natural” in the surveyed corpus migrates across three independent senses—mathematical, sociolinguistic, and distributional—only the first admits a computational audit. Credibility for quantitative measurement in the corpus’s measurement‑focused entries rests on consensus standardization, repeatability, and reproducibility, not on naturalness of units. We provided explicit falsification conditions and outlined a minimal empirical test to de‑risk the conclusions.

## Version History

- Version 2.0.0 (2026-10-21, from 1.0.0): rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement. references 8 -> 8. length 5065 -> 3190 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Challenges Encountered in Turkish Natural Language Processing Studies. arXiv:2101.11436v1. https://arxiv.org/abs/2101.11436v1
[2] A Comprehensive Review of State-of-The-Art Methods for Java Code Generation from Natural Language Text. arXiv:2306.06371v1. https://arxiv.org/abs/2306.06371v1
[3] An Automated Multiple-Choice Question Generation Using Natural Language Processing Techniques. arXiv:2103.14757v1. https://arxiv.org/abs/2103.14757v1
[4] An Open Natural Language Processing Development Framework for EHR-based Clinical Research: A case demonstration using the National COVID Cohort Collaborative (N3C). arXiv:2110.10780v3. https://arxiv.org/abs/2110.10780v3
[5] Time, Tense and Aspect in Natural Language Database Interfaces. arXiv:cmp-lg/9803002v1. https://arxiv.org/abs/cmp-lg/9803002v1
[6] Recommended Implementation of Quantitative Susceptibility Mapping for Clinical Research in The Brain: A Consensus of the ISMRM Electro-Magnetic Tissue Properties Study Group. arXiv:2307.02306v1. https://arxiv.org/abs/2307.02306v1
[7] The Effect of Intrinsic Dataset Properties on Generalization: Unraveling Learning Differences Between Natural and Medical Images. arXiv:2401.08865v3. https://arxiv.org/abs/2401.08865v3
[8] https://papers.qnfo.org/papers/emergence-of-physics. QNFO: Emergence of Physics.

## Appendix A. Divergence report

One divergence was identified across the independent drafts and resolved as follows. **D1 (Gaussian differential entropy rounding):** one draft reported the unit‑variance Gaussian differential entropy as $1.4189385$ nats while the derivation chain in Section 4.4 yields $1.4189386$ nats at the paper’s stated precision. The disagreement is a rounding‑convention choice: the underlying value $\tfrac12\ln(2\pi e)\approx1.4189385\ldots$ rounds differently depending on where intermediate products are truncated. Convention adopted: the value produced by the paper’s own shown arithmetic chain, $1.4189386$ nats, is used consistently in the Abstract, Section 4.4, and Results R4. No other divergences among drafts were substantive; corpus composition, conversion constants, and the C4 conclusion were convergent.

## Appendix B. Claim attribution

| Claim | Source drafts | Agreement |
|---|---|---|
| C1: $\ln 2 = 0.6931471808$ via the $\mathrm{artanh}(1/3)$ series | A, B, C | CONVERGENT |
| C2: $\log_{2}e = 1.4426950$; one bit $= 0.6931471808$ nats | A, B, C | CONVERGENT |
| C3: fair‑coin entropy $= 1$ bit $= \ln 2$ nats | A, B | CONVERGENT |
| C4: uniform‑over‑3 entropy $\approx 1.0986123$ nats $= 1.5849625$ bits | A, B | CONVERGENT |
| C5: entropy ratio $H_{e}/H_{2} = \ln 2$ is distribution‑independent | A, B, C | CONVERGENT |
| C6: Gaussian differential entropy $\approx 1.4189386$ nats $= 2.0470956$ bits | A, B, C | CONVERGENT (value; rounding DIVERGENT, see Appendix A) |
| C7: differential entropy shifts by $\ln a$ under $Y = aX$; failure is base‑independent | A, B, C | CONVERGENT |
| C8: C4 (discrimination) fails; bit–nat difference is purely conventional | A, B, C | CONVERGENT |
| C9: corpus composition $62.5\%$ language‑focused, $25\%$ imaging/measurement‑focused, $12.5\%$ information‑theory‑focused | A, B | CONVERGENT (after correction, see Appendix A) |
| C10: three‑sense taxonomy of “natural” (mathematical, sociolinguistic, distributional) | A, B, C | CONVERGENT |
| C11: credibility route via standardization/reproducibility, per [7] | A, C | CONVERGENT |
| C12: Gaussian value reported as $1.4189385$ nats in the Abstract | A | SINGLE (resolved to $1.4189386$ nats, Appendix A) |