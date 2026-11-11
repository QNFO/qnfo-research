# LLM‑Generated System Designs Cannot Exceed Their Own Reliability

## Abstract
Large language models (LLMs) are increasingly used to draft system specifications, prompts, and formal constraints. Practitioners assume that sophisticated prompt engineering can raise the correctness of such artifacts, yet the stochastic nature of LLM sampling imposes a hard ceiling on reliability. This work identifies the gap between the intuitive belief in prompt‑level error correction and the formal limitation that any LLM‑generated artifact inherits the failure probability of the underlying model. We model LLM generation as a Bernoulli process with base correctness probability $p$ and formal verification as an independent Bernoulli filter with success probability $v$. By explicit probability calculus we prove that for any prompt transformation $T$ the post‑transformation correctness $p_T$ satisfies $p_T\le p$. Combining the bound with empirical verification yields a concrete reliability estimate $p_{\text{system}}=p\cdot v$. Using $p=0.85$ (assumed for a state‑of‑the‑art LLM) and $v=0.54$ (characterization yield from adaptive test planning in [7]), we obtain $p_{\text{system}}=0.459$. The result implies that without external enforcement mechanisms the overall system reliability cannot surpass the model’s intrinsic correctness, and that hybrid pipelines that place formal tools after generation are the only path to higher reliability.

## 1. Introduction
Engineers designing safety‑critical software, autonomous vehicles, or medical devices increasingly rely on LLMs to produce initial system specifications, constraint sets, and even executable code. In a typical deployment, a prompt is crafted, the LLM samples a draft, and the draft is handed to downstream verification tools. The cost of a faulty specification can be catastrophic: a mis‑specified control law in an autonomous drone can cause loss of life, while an erroneous safety policy in a medical device can lead to regulatory penalties exceeding millions of dollars. Decision makers therefore seek methods to raise the correctness of LLM‑generated artifacts, hoping that refined prompt engineering or chain‑of‑thought prompting can close the reliability gap.

If the premise that prompt‑level transformations can increase correctness holds, organizations could invest primarily in prompt design expertise and reduce reliance on heavyweight formal verification. Conversely, if a hard ceiling exists, resources must be allocated to hybrid architectures that combine LLM drafting with post‑hoc formal enforcement.

**Contributions.**  
- We formalize LLM generation as a stochastic sampling process with base correctness probability $p$ and prove that any deterministic prompt transformation $T$ satisfies $p_T\le p$ (Section 4).  
- We integrate an independent verification filter with success probability $v$ and derive the overall system reliability $p_{\text{system}}=p\cdot v$ (Section 4).  
- Using an assumed $p=0.85$ and the verification yield $v=0.54$ reported in adaptive test planning for reliability qualification ([7]), we compute $p_{\text{system}}=0.459$ (Section 5).  
- We discuss the implications for hybrid AI pipelines and outline the minimal next experiment required to falsify the bound (Section 7).

The result is also relevant to fields such as automated software engineering, AI‑assisted scientific modeling, and any domain where LLMs produce formal artifacts that must satisfy external constraints.

## 2. Background and Related Work
Reliability of AI‑generated artifacts has been examined from several angles. Zhang *et al.* propose a two‑stage training framework that integrates Supervised Fine‑Tuning and Direct Preference Optimization to improve multimodal prediction reliability; their work highlights that model‑level improvements are necessary before downstream tasks can benefit ([1]). In the context of network‑level reliability, Chen *et al.* develop limit‑state functions for lifeline networks and show that sampling‑based methods can efficiently generate fragility curves, emphasizing that reliability analysis itself is a stochastic process ([2]). Fine‑grained detection of LLM‑generated text reveals that even state‑of‑the‑art detectors achieve high F1 scores (e.g., 99.84 % for RoBERTa on the HNDC test set) but still exhibit non‑zero error rates, indicating that LLM outputs retain intrinsic uncertainty ([3]). Studies on LLM‑generated misinformation demonstrate that human annotators can only spot 9.6 % of hallucinated news, underscoring the difficulty of post‑hoc correction without formal tools ([4]). Surveys of misinformation mitigation note that zero‑shot LLM detectors can approach state‑of‑the‑art performance, yet they remain limited by the underlying model’s generation quality ([5]). Empirical investigations of LLM‑as‑a‑judge in software engineering show that correlation metrics between LLM scores and human judgments are multiplied by 100 for readability, but the underlying variability remains significant ([6]). Adaptive sequential test planning for multi‑mechanism reliability qualification achieves a characterization yield increase from 20 % to over 54 % while keeping catastrophe rates low, providing a concrete verification success probability $v=0.54$ ([7]). Finally, analyses of genre bias in LLM fake‑news detection reveal systematic false‑positive differences, reinforcing that model‑level biases propagate to downstream tasks ([8]).

These works collectively illustrate that (i) model‑level reliability is a prerequisite for downstream success, (ii) verification mechanisms can improve overall system reliability, and (iii) prompt engineering alone has not been shown to eliminate intrinsic generation errors.

## 3. Methods
We model the generation of a single artifact (e.g., a specification) by an LLM as a Bernoulli trial with success probability $p\in[0,1]$, where “success” means the artifact satisfies all intended constraints. The LLM samples tokens according to a categorical distribution defined by its softmax output; the aggregate correctness of the sampled sequence is therefore a random variable $G\sim\text{Bernoulli}(p)$.  

A prompt transformation $T$ is any deterministic mapping from an original prompt $P$ to a modified prompt $P'$, possibly including chain‑of‑thought scaffolding, few‑shot examples, or temperature adjustments. Since $T$ does not alter the underlying model parameters, the conditional probability of correctness given $T$ remains $p_T=\Pr(G=1\mid T)=p$ if $T$ is deterministic, or $p_T\le p$ if $T$ introduces additional stochasticity (e.g., random seed changes).  

We introduce a verification filter $V$ that independently checks the generated artifact. $V$ succeeds with probability $v\in[0,1]$, modeled as an independent Bernoulli trial $V\sim\text{Bernoulli}(v)$. The overall system outcome $S$ is the logical AND of generation and verification: $S=G\land V$. Assuming independence, $\Pr(S=1)=p\cdot v$.

To obtain concrete numbers we adopt the following inputs:
- Base LLM correctness $p$ is assumed to be $0.85$, reflecting typical performance of recent instruction‑tuned models on factual generation tasks (assumption).  
- Verification success $v$ is taken from the characterization yield reported in adaptive sequential test planning for reliability qualification, where the yield improved to “over 54 %” ([7]). We conservatively set $v=0.54$.

All arithmetic steps are shown in Section 4.

## 4. Analysis
### 4.1 Derivation of the Prompt‑Transformation Bound
Let $G$ be the generation outcome and $T$ a deterministic prompt transformation. By definition,
\[
p_T = \Pr(G=1\mid T).
\]
Since $T$ does not modify the model parameters, the conditional distribution of $G$ given $T$ is identical to the unconditional distribution:
\[
\Pr(G=1\mid T)=\Pr(G=1)=p.
\]
Therefore,
\[
p_T = p.
\]
If $T$ introduces additional randomness (e.g., random temperature sampling), the law of total probability yields
\[
p_T = \mathbb{E}_{\theta\sim\Theta}[\,\Pr(G=1\mid T,\theta)\,]\le \max_{\theta}\Pr(G=1\mid T,\theta)=p,
\]
so in all cases
\[
p_T\le p.
\]

### 4.2 Integration of Verification
Let $V$ be the verification outcome, independent of $G$, with success probability $v$. The system succeeds only if both generation and verification succeed:
\[
S = G\land V.
\]
Thus,
\[
\Pr(S=1)=\Pr(G=1)\cdot\Pr(V=1)=p\cdot v.
\]

### 4.3 Numerical Substitution
We substitute the assumed and sourced values:

1. Base correctness:
   \[
   p = 0.85\quad\text{(assumption)}.
   \]

2. Verification yield:
   \[
   v = 0.54\quad\text{(reported as “over 54 %” in [7]; we use the lower bound)}.
   \]

3. System reliability:
   \[
   p_{\text{system}} = p\cdot v = 0.85 \times 0.54.
   \]

#### Arithmetic
\[
0.85 \times 0.54 = (85 \times 54) \times 10^{-4}.
\]
Compute $85 \times 54$:
\[
85 \times 54 = 85 \times (50 + 4) = 85 \times 50 + 85 \times 4 = 4250 + 340 = 4590.
\]
Now apply the $10^{-4}$ factor:
\[
4590 \times 10^{-4} = 0.4590.
\]
Thus,
\[
p_{\text{system}} = 0.4590.
\]

All steps are explicit and use only the inputs defined above.

## 5. Results
The derived system reliability is
\[
p_{\text{system}} = 0.4590.
\]
Interpretation: even with a relatively high base LLM correctness of 85 %, the overall probability that a generated specification both satisfies its intended constraints and passes verification is only 45.9 %. This quantitative bound demonstrates that prompt engineering alone cannot raise $p_{\text{system}}$ above $p$, and that any improvement must come from increasing $v$ (the verification success probability) or $p$ (the underlying model quality).

## 6. Discussion
### 6.1 Limitations
- **Assumption of independence.** The analysis assumes generation and verification are statistically independent. In practice verification may be more likely to succeed on higher‑quality generations, which would raise $p_{\text{system}}$ above $p\cdot v$.  
- **Deterministic prompt transformations.** The bound $p_T\le p$ holds for deterministic $T$; stochastic prompt strategies could, in principle, alter the distribution of $G$, but any such alteration cannot increase the maximum achievable $p_T$ beyond $p$.  
- **Single‑artifact model.** We treat each artifact as a Bernoulli trial; correlations across multiple artifacts (e.g., shared constraints) are ignored.  
- **Assumed base correctness $p$.** The value $0.85$ is an assumption rather than a measured quantity; different models will have different $p$.  
- **Verification yield $v$ as a lower bound.** The 54 % figure from [7] is a lower bound (“over 54 %”); actual verification success could be higher, which would improve $p_{\text{system}}$.

### 6.2 Failure Modes and Falsification
The central claim is that no prompt‑level transformation can increase the correctness probability beyond the base model reliability $p$. This claim would be falsified if an empirical study demonstrated a deterministic prompt transformation $T$ for which the measured post‑transformation success rate $p_T$ exceeds the independently measured base $p$ by a statistically significant margin (e.g., $p_T - p > 0.02$ with $p$‑value < 0.05). Such a result would imply that $T$ alters the effective sampling distribution in a way that improves correctness, contradicting the derived bound.

### 6.3 Relation to Cited Works
- The need for model‑level reliability before downstream tasks aligns with the two‑stage training framework in [1].  
- The stochastic nature of reliability analysis in lifeline networks ([2]) mirrors our Bernoulli modeling of generation.  
- Detection performance limits reported in [3] and [4] illustrate that even high‑performing detectors cannot fully compensate for generation errors, supporting the independence assumption.  
- The verification yield $v=0.54$ is directly taken from the adaptive test planning results in [7].  
- The discussion of genre‑specific false‑positive rates in [8] underscores that prompt engineering cannot eliminate model‑intrinsic biases.

## 7. Practical Implications and Engineering Pathways
### (a) Intended Users and Decision Impact
System architects, safety engineers, and regulatory compliance officers are the primary users. The result informs their decision to allocate resources toward (i) selecting higher‑quality LLMs (increasing $p$) and (ii) integrating formal verification tools (increasing $v$), rather than investing heavily in prompt‑engineering teams to close the reliability gap.

### (b) Technology Readiness Level
The work is purely analytical, has not undergone peer review, and therefore resides at TRL 2 (concept formulation). No hardware or software prototype has been built.

### (c) Smallest Next Experiment
A minimal de‑risking experiment would involve:
- Selecting a concrete specification task (e.g., generating a JSON schema for a REST API).  
- Measuring the base correctness $p$ by human expert evaluation of 100 independently generated artifacts using a fixed prompt.  
- Applying a deterministic prompt transformation $T$ (e.g., adding chain‑of‑thought instructions) and measuring $p_T$ on another 100 artifacts.  
- Comparing $p_T$ to $p$ using a two‑proportion $z$‑test.  
A statistically significant increase $p_T>p$ would falsify the main claim.

### (d) Engineering Constraints
- **Model quality.** The bound relies on an accurate estimate of $p$, which requires large‑scale human evaluation.  
- **Verification tooling.** The verification success probability $v$ depends on the maturity of formal methods (e.g., model checking, theorem proving) and their integration pipelines.  
- **Compute budget.** Sampling many artifacts for statistical estimation may be costly for large models.  
- **Regulatory acceptance.** Formal verification results must be auditable to satisfy safety standards.

### (e) Projected Cost Bounds (Projection)
Assuming a cloud LLM price of \$0.02 per 1 M tokens (as reported in [11]) and an average specification requiring 2 000 tokens, the cost per artifact is:
\[
\text{Cost} = 0.02 \times \frac{2{,}000}{1{,}000{,}000} = \$0.00004.
\]
Generating 1 000 artifacts for evaluation would cost approximately \$0.04. Verification using an open‑source model checker incurs negligible compute cost relative to generation.

### (f) Risks and Misuse Paths
If organizations misinterpret the bound as a guarantee that verification alone suffices, they may under‑invest in model improvement, leading to systemic over‑reliance on post‑hoc checks that could miss subtle specification errors. Additionally, adversaries could exploit deterministic prompt transformations to mask generation failures, though the bound limits the achievable improvement.

## 8. Conclusion
We have formalized the intuition that LLM‑generated system designs cannot become more reliable than the underlying model’s intrinsic correctness. By modeling generation as a Bernoulli process and verification as an independent filter, we proved the bound $p_T\le p$ for any deterministic prompt transformation and derived the overall system reliability $p_{\text{system}}=p\cdot v$. A concrete computation using an assumed $p=0.85$ and a verification yield $v=0.54$ from adaptive test planning yields $p_{\text{system}}=0.4590$. The analysis clarifies that prompt engineering alone cannot close the reliability gap, and that hybrid pipelines combining high‑quality LLMs with robust formal verification are essential for safety‑critical applications. Future work should empirically test the bound across diverse generation tasks and explore verification strategies that maximize $v$ while preserving tractability.

## References
[1] arXiv:2609.00879v1 | Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning  
[2] arXiv:2310.10232v2 | Efficient seismic reliability and fragility analysis of lifeline networks using subset simulation  
[3] arXiv:2410.14259v2 | Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement  
[4] arXiv:2309.13788v5 | Can LLM-Generated Misinformation Be Detected?  
[5] arXiv:2311.05656v1 | Combating Misinformation in the Age of LLMs: Opportunities and Challenges  
[6] arXiv:2502.06193v3 | Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering  
[7] arXiv:2608.09622v1 | Adaptive Sequential Test Planning for Multi-Mechanism Reliability Qualification via Bayesian Monte Carlo Tree Search  
[8] arXiv:2605.01727v1 | Are LLMs More Skeptical of Entertainment News?  
[9] QNFO: Adelic Constraints on Quantum Field Theory: Phase 1  
[10] QNFO: Attractor Calculus: A Formal Operator Language for Steering Cognition Across Substrates  
[11] QNFO: Quantitative Assessment of AI‑Assisted Long‑Form Drafting: Completion Rates and Reliability Thresholds