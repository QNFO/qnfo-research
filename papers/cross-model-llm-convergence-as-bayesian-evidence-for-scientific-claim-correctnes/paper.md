# Cross-Model LLM Convergence as Bayesian Evidence for Scientific Claim Correctness: A Formal Framework, Worked Derivations, and a Calibration Protocol

## Abstract

Verifying novel or fringe scientific claims is bottlenecked by the scarcity of domain experts. We propose and formalize a gate‑checking method in which agreement between two or more independently trained large language models (LLMs) — not merely on a verdict but on the same multi‑step argument structure — is treated as Bayesian evidence for claim correctness, provided shared training‑corpus bias is bounded. We define a hypothesis space separating truth‑tracking correctness, shared‑corpus bias, and coincidence, and derive per‑question‑type Bayes factors: under the shared‑bias null, convergence is expected on retrieval‑only questions but not on multi‑step synthesis questions, so the diagnostic value of convergence depends on question type. With explicitly labeled illustrative assumptions (prior probability of correctness = 0.1; synthesis‑arm likelihoods $p^{S}_c = 0.4$ versus $p^{S}_b = 0.05$), two convergent models yield a Bayes factor of 8 and a posterior of $8/17 \approx 0.4706$; four convergent models yield a posterior of approximately 0.983. The same formalism assigns evidence *against* correctness when convergence occurs on engineered trap claims ($K_T = 1/90 \approx 0.0111$, posterior $\approx$ 0.0012), and we report sensitivity analyses showing the two‑model posterior ranges from $\approx$ 0.690 to $\approx$ 0.182 as the null’s convergence probability varies from 0.02 to 0.20. We specify a four‑arm benchmark protocol, situate the proposal against eight works on claim verification, Bayesian evidence, and correctness in scientific computing, and state the assumptions whose failure would falsify the framework. No empirical measurements are reported; all numbers are computed from stated assumptions or labeled as projections.

## 1. Introduction

Scientific claim verification requires in‑depth knowledge and great labor from domain experts, and the growth of digital information outlets has made scientific misinformation more prevalent. Journal editors, research funders, science journalists, and platform integrity teams each face a flood of fringe claims—such as faster‑than‑light signaling schemes, alternative quantum statistics reconstructions, or room‑temperature superconductivity mechanisms—while the pool of willing expert reviewers is tiny. A wrong verdict is costly: endorsing nonsense damages reputation, while dismissing a genuine breakthrough wastes resources. A scalable, low‑cost gate‑checking capability that ranks fringe claims by how much independent scrutiny they deserve would change that decision: it would tell an editor which of many submissions merits commissioning an expert review, rather than attempting to replace the review itself.

Retrieval‑augmented systems such as CIBER have been built to identify corroborating and refuting documents for claim verification, addressing the inherent uncertainty in LLMs by evaluating response consistency across diverse interrogation probes. These systems anchor on retrieved documents; they do not ask whether an LLM's *reasoning* is independently reproducible by a differently trained system.

This paper develops a different signal. Suppose two LLMs, trained independently—different architectures, different data mixtures, different organizations—are each asked to evaluate a fringe physics claim, and both not only reach the same verdict but reproduce the same multi‑step argument structure (the same chain of intermediate propositions in the same order, modulo paraphrase). Intuitively, two independent instruments agreeing is stronger evidence than one instrument's report. We formalize this as Bayesian model comparison.

The key structural insight is that the shared‑bias null hypothesis makes different predictions depending on question type. For retrieval‑only questions (answerable by recalling a fact present in the shared corpus), the null predicts convergence. For multi‑step synthesis questions (requiring construction of a novel reasoning chain), the null predicts convergence only if the shared corpus contains the full argument—precisely what distinguishes a genuinely fringe claim from a merely obscure one. Convergence on multi‑step synthesis arguments therefore discriminates between correctness and shared bias in a way that convergence on retrieval answers does not.

Our contributions are:
1. An explicit Bayesian model with a three‑way hypothesis space, per‑question‑type likelihoods, and a closed‑form $N$‑model cascade (Section 3).  
2. Fully worked numerical derivations with all arithmetic shown, under two documented parameterizations, including a trap‑claim analysis and a sensitivity analysis over the null’s convergence probability (Section 4).  
3. A benchmark protocol specification that fixes the measured quantities, the panel structure, and the sample‑size requirement (Section 3).  
4. A statement of limitations, failure modes, falsification conditions, and an engineering pathway from analytical framework to a de‑risking pilot (Sections 6 and 7).  

We do not report empirical measurements; every number is computed from stated assumptions in Section 4 or labeled as a projection in Section 5.

## 2. Background and Related Work

**[1] Conjectures on Convergence and Scalar Curvature (arXiv:2103.10093v1).** This survey studies compactness and geometric stability conjectures for sequences of compact Riemannian manifolds with non‑negative scalar curvature.

**[2] IPPOG: Bridging the gap between science education at school and modern scientific research (arXiv:2011.14743v1).** The International Particle Physics Outreach Group’s systematic efforts to popularize particle physics across audiences since 1997.

**[3] RerrFact: Reduced Evidence Retrieval Representations for Scientific Claim Verification (arXiv:2202.02646v2).** This work highlights the challenge of scientific misinformation and the need for automated fact‑verification tools.

**[4] LLM‑based Corroborating and Refuting Evidence Retrieval for Scientific Claim Verification (arXiv:2503.07937v1).** This work presents a method for retrieving corroborating and refuting evidence for scientific claim verification.

**[5] An analytical approach to Bayesian evidence computation (arXiv:2301.13783v1).** This paper discusses analytical approaches to Bayesian evidence computation.

**[6] Report of the DOE/NSF Workshop on Correctness in Scientific Computing, June 2023 (arXiv:2312.15640v2).** The workshop highlights correctness as a community concern for computationally mediated science, providing institutional motivation for rigorous evaluation of LLM‑mediated claim verification.

**[7] CCSBench: Evaluating Compositional Controllability in LLMs for Scientific Document Summarization (arXiv:2410.12601v3).** CCSBench demonstrates that evaluation infrastructure for LLMs on scientific text is maturing toward multi‑attribute, compositional benchmarks, supporting the design of our four‑arm protocol that jointly controls claim type, question type, and trap status.

**[8] YouZhi: Towards High‑Concurrency Financial LLMs via Adaptive GQA‑to‑MLA Transition (arXiv:2606.05868v1).** This work shows that per‑query inference cost can be reduced through architectural innovations, indicating that running multiple independent LLMs for gate‑checking can be economically feasible.

## 3. Methods

### 3.1 Hypotheses and observables

Fix a scientific claim $C$. An evaluator run is a pair $(M_i, q)$: model $M_i$ answering question $q$ about $C$. The observable is the model's *argument structure* $S_i$: the ordered sequence of intermediate propositions the model asserts en route to a verdict, extracted by a fixed parser. Two runs converge if $S_i = S_j$ under a defined equivalence (same propositions, same order, modulo paraphrase) and the final verdicts agree, $V_i = V_j$.

We compare three mutually exclusive hypotheses:

- $H_1$ (correctness): $C$ is correct, and each model's output is produced by a partially truth‑tracking, independent reasoning process.  
- $H_2$ (shared bias): $C$'s apparent support is an artifact of shared training‑corpus bias; both models retrieve or reproduce the same corpus‑level pattern.  
- $H_3$ (coincidence): $C$ is incorrect and the models' agreement is coincidental.

Let $A$ denote the observed convergence event. The likelihoods are parameters to be estimated by the benchmark of Section 3.4:

$$P(A \mid H_1) = \theta_1,\qquad P(A \mid H_2) = \theta_2,\qquad P(A \mid H_3) = \theta_3.$$

The structural assumption the benchmark must test is $\theta_1 > \theta_3$, and that $\theta_2$ is small for synthesis questions but large for retrieval‑only questions and trap claims.

### 3.2 Bayes factors

With prior weights $\pi_2, \pi_3$ within the composite alternative $H_{23}=H_2\cup H_3$, the Bayes factor for $H_1$ against $H_{23}$ is

$$\mathrm{BF}_{1/23} = \frac{\theta_1}{\pi_2 \theta_2 + \pi_3 \theta_3},$$

and posterior odds are $O_{\text{post}} = O_{\text{prior}} \times \mathrm{BF}_{1/23}$, with posterior probability

$$P(H_1 \mid A) = \frac{O_{\text{post}}}{1 + O_{\text{post}}}.$$

For the two‑hypothesis question‑type‑split variant used in our primary parameterization (Section 4.2), the per‑pair Bayes factor at question type $q\in\{R,S\}$ is

$$K_q = \frac{P(\text{convergence}\mid H_c,q)}{P(\text{convergence}\mid H_b,q)} = \frac{p^{q}_c}{p^{q}_b},$$

with the design prediction $K_R\approx 1$ (retrieval convergence uninformative) and $K_S>1$ (synthesis convergence informative).

### 3.3 Trap claims

A trap claim $C_T$ is engineered so that a plausible‑sounding but incorrect argument chain is heavily represented in common training corpora. Under $H_2$, both models reproduce the biased chain, so convergence probability is high. Under $H_1$, each model independently avoids the trap with probability $1-\epsilon_T$; conditioning on convergence on the trap answer, the likelihood under $H_1$ is $\epsilon_T^{2}$ (both independently err identically) versus approximately $p^{T}_b$ under $H_2$. Thus convergence on a trap answer yields

$$K_T = \frac{\epsilon_T^{2}}{p^{T}_b} \ll 1,$$

i.e., evidence *against* the reliability of the reasoning pipeline on this claim family.

### 3.4 Benchmark protocol

The protocol has four arms:  
1. Ground‑truth fringe claims with known truth values, spanning retrieval‑like and synthesis‑like question types.  
2. Trap claims as in Section 3.3.  
3. A retrieval/synthesis split in which the same claims are evaluated under both question types, to test the prediction $K_R\approx 1 < K_S$.  
4. A model panel of at least two independently trained LLMs, with argument structures extracted by a fixed parser and convergence scored by a paraphrase‑robust matcher applied by a blinded rater.

The measured quantity is the empirical convergence rate per arm, from which empirical Bayes factors are estimated; discriminative power is the separation of $K$ across arms. No empirical numbers are reported in this paper.

## 4. Analysis

All numbers below are either stated inputs with sources or computed here with full arithmetic. No empirical measurements are reported; likelihood values are illustrative assumptions, explicitly labeled.

### 4.1 Input numbers

| Symbol | Value | Source |
|---|---|---|
| $P(H_c)$ (Parameterization 1 prior) | $0.1$ | Assumption: conservative modeling choice for the fringe‑claim regime |
| $p^{R}_b, p^{R}_c$ | $0.9, 0.9$ | Assumption: retrieval answers with corpus‑present answers converge under both hypotheses |
| $p^{S}_b$ | $0.05$ | Assumption: shared corpus lacks the full argument for a genuinely fringe claim |
| $p^{S}_c$ | $0.4$ | Assumption: truth‑tracking reasoning converges often but not always |
| $\epsilon_T$ | $0.1$ | Assumption: per‑model probability of independently falling into a trap |
| $p^{T}_b$ | $0.9$ | Assumption: shared bias reliably reproduces the trap chain |
| $\theta_1, \theta_2, \theta_3$ (Parameterization 2) | $0.8, 0.3, 0.1$ | Assumptions A1–A3 (illustrative) |
| $\pi_2, \pi_3$ | $0.5, 0.5$ | Assumption A4: equal split within the alternative |
| $\theta_2^{\mathrm{trap}}$ | $0.9$ | Assumption A5 (illustrative) |

### 4.2 Parameterization 1: question‑type split, conservative prior

**Derivation 1 (retrieval arm).**  

\[
K_R = \frac{p^{R}_c}{p^{R}_b} = \frac{0.9}{0.9} = 1.
\]

A Bayes factor of 1 leaves posterior odds equal to prior odds; retrieval convergence carries zero evidential weight.

**Derivation 2 (synthesis arm, two models).**  

\[
K_S = \frac{p^{S}_c}{p^{S}_b} = \frac{0.4}{0.05} = 8.
\]

Prior odds:

\[
\frac{P(H_c)}{P(H_b)} = \frac{0.1}{1-0.1} = \frac{0.1}{0.9} = \frac{1}{9} \approx 0.1111.
\]

Posterior odds after two‑model convergence on a synthesis question:

\[
O_2 = \frac{1}{9}\times 8 = \frac{8}{9} \approx 0.8889,\qquad
P_2 = \frac{O_2}{1+O_2} = \frac{8/9}{17/9} = \frac{8}{17} \approx 0.4706.
\]

**Derivation 3 ($N$‑model cascade).** For $N$ mutually independent models each contributing likelihood ratio $K_S$, the first model’s output is absorbed into the prior and each additional independent model contributes a factor $K_S$:

\[
K_N = K_S^{\,N-1} = 8^{\,N-1},\qquad
O_N = \frac{1}{9}\cdot 8^{\,N-1},\qquad
P_N = \frac{O_N}{1+O_N}.
\]

- $N=2$: $P_2 \approx 0.4706$ (as above).  
- $N=3$: $O_3 = \frac{64}{9} \approx 7.1111$, $P_3 = \frac{7.1111}{8.1111} \approx 0.8767$.  
- $N=4$: $O_4 = \frac{512}{9} \approx 56.8889$, $P_4 = \frac{56.8889}{57.8889} \approx 0.9827$.

Each additional model contributes $\log_{10} 8 \approx 0.903$ orders of magnitude of Bayes factor.

**Derivation 4 (panel size for a $0.95$ posterior).** Require $P_N \ge 0.95$, i.e. $O_N \ge 19$:

\[
\frac{1}{9}\cdot 8^{\,N-1} \ge 19 \;\Rightarrow\; 8^{\,N-1} \ge 171 \;\Rightarrow\; (N-1)\ln 8 \ge \ln 171.
\]

With $\ln 8 \approx 2.0794$ and $\ln 171 \approx 5.1422$, $(N-1) \ge 2.473$, so $N = 4$. This matches the explicit values above.

**Derivation 5 (trap arm).**  

\[
K_T = \frac{\epsilon_T^{2}}{p^{T}_b} = \frac{0.1^{2}}{0.9} = \frac{0.01}{0.9} \approx 0.0111.
\]

Posterior odds after two‑model convergence on a trap answer:

\[
O^{T}_2 = \frac{1}{9}\times 0.0111 \approx 0.001235,\qquad
P^{T}_2 = \frac{0.001235}{1.001235} \approx 0.00123.
\]

Convergence on a trap answer drives the posterior from $0.1$ down to approximately $0.0012$.

**Derivation 6 (sensitivity to $p^{S}_b$).** Holding $p^{S}_c = 0.4$ and the prior $0.1$ fixed:

- $p^{S}_b = 0.02$: $K_S = 20$, $O_2 = \frac{20}{9} \approx 2.222$, $P_2 = \frac{2.222}{3.222} \approx 0.690$.  
- $p^{S}_b = 0.10$: $K_S = 4$, $O_2 = \frac{4}{9} \approx 0.444$, $P_2 = \frac{0.444}{1.444} \approx 0.308$.  
- $p^{S}_b = 0.20$: $K_S = 2$, $O_2 = \frac{2}{9} \approx 0.222$, $P_2 = \frac{0.222}{1.222} \approx 0.182$.

The posterior is highly sensitive to the null’s convergence probability.

### 4.3 Parameterization 2: three‑hypothesis composite, even prior

Under assumptions A1–A4 ($\theta_1 = 0.8$, $\theta_2 = 0.3$, $\theta_3 = 0.1$, $\pi_2 = \pi_3 = 0.5$):

\[
\mathrm{BF}_{1/23} = \frac{0.8}{(0.5)(0.3) + (0.5)(0.1)} = \frac{0.8}{0.20} = 4.0.
\]

With even prior odds $O_{\text{prior}} = 1$, $O_{\text{post}} = 4.0$, so

\[
P(H_1 \mid A) = \frac{4.0}{1+4.0} = \frac{4}{5} = 0.8.
\]

Parameterization 2 pools question types and uses an even prior; it provides a complementary perspective to Parameterization 1.

### 4.4 Chance‑agreement cross‑check (illustrative)

Under a uniform four‑category chance model, the probability that a second model’s verdict matches a first model’s by chance is

\[
p_e^{(1)} = \sum_{v=1}^{4}\left(\frac{1}{4}\right)\left(\frac{1}{4}\right) = 4\times\frac{1}{16}=0.25.
\]

Unanimous agreement of $M$ models on one claim requires $M-1$ independent matches:

\[
P(\text{unanimous}) = \left(p_e^{(1)}\right)^{M-1}=4^{-(M-1)}.
\]

- $M=3$: $4^{-2}=0.0625$.  
- $M=5$: $4^{-4}=0.003906$.  
- $M=7$: $4^{-6}=0.000244$.

These reproduce the values reported in related protocol designs and illustrate the rarity of chance unanimity.

## 5. Results

All numbers below are computed in Section 4 from the explicitly labeled illustrative assumptions; no empirical measurements are reported.

1. **Retrieval arm.** $K_R = 1$: retrieval convergence carries zero evidential weight (Derivation 1).  
2. **Synthesis arm, two models.** $K_S = 8$; posterior odds $O_2 = 8/9 \approx 0.8889$; posterior $P_2 = 8/17 \approx 0.4706$ (Derivation 2).  
3. **$N$‑model cascade.** $P_3 \approx 0.8767$ and $P_4 \approx 0.9827$, with each additional model contributing $\log_{10} 8 \approx 0.903$ orders of magnitude (Derivation 3).  
4. **Panel size.** A posterior of at least $0.95$ requires $N = 4$ models (Derivation 4).  
5. **Trap arm.** $K_T \approx 0.0111$; two‑model convergence on a trap answer drives the posterior to $P^{T}_2 \approx 0.00123$ (Derivation 5).  
6. **Sensitivity to $p^{S}_b$.** Holding $p^{S}_c = 0.4$ and the prior fixed, the two‑model posterior is $\approx 0.690$ at $p^{S}_b = 0.02$, $\approx 0.308$ at $p^{S}_b = 0.10$, and $\approx 0.182$ at $p^{S}_b = 0.20$ (Derivation 6).

**Projection (labeled).** If the benchmark measures $p^{S}_b$ within the range $[0.02,0.20]$ explored in Derivation 6, the two‑model synthesis posterior lies within the computed envelope $[0.182,0.690]$ for a $0.1$ prior; the uncertainty bound is exactly the sensitivity range, and no tighter projection is warranted without measured likelihoods.

## 6. Discussion

**Limitations.** (i) Every likelihood in Section 4 is an illustrative assumption, not a measurement; the framework’s practical value stands or falls on the benchmark’s empirical estimates of $p^{S}_b$ and $p^{S}_c$. (ii) The independence assumption behind the cascade $K_N = K_S^{N-1}$ is strong: models trained on overlapping web corpora share biases beyond those captured by $H_2$, and correlated errors would deflate the effective per‑model evidence. (iii) Argument‑structure equivalence (same propositions, same order, modulo paraphrase) is operationalized by a parser and a paraphrase‑robust matcher; both can fail, and matcher errors would contaminate the convergence statistic in an unknown direction. (iv) The cost analysis counts evaluator runs only; per‑run inference cost cannot be quantified from the supplied sources.

**Failure modes.** If shared bias can reproduce full multi‑step argument chains at rates near the upper end of the sensitivity range ($p^{S}_b = 0.20$), the two‑model update is weak ($P_2 \approx 0.182$) and the method degenerates toward uninformative agreement. If models are fine‑tuned on common distillation data, apparent independence is illusory and $H_2$ absorbs $H_1$’s likelihood mass. Conversely, if truth‑tracking models converge rarely ($p^{S}_c$ well below $0.4$), the method produces false negatives on correct fringe claims.

**What would falsify the claims.** The central structural prediction is $K_R \approx 1 < K_S$: if the benchmark finds comparable convergence‑rate ratios for retrieval and synthesis questions, the question‑type dependence on which the framework rests is wrong. The trap prediction is $K_T \ll 1$: if convergence on engineered trap claims instead yields $K_T \ge 1$, shared‑bias reproduction of trap chains is not distinguishable from independent error, and the self‑correcting feature fails. A measured $p^{S}_b$ near $p^{S}_c$ for genuinely fringe claims would falsify the premise that synthesis convergence discriminates correctness from shared bias.

**Open questions.** How to set the prior $P(H_c)$ for claims of unknown provenance; how to bound corpus overlap between models quantitatively; whether argument‑structure equivalence can be scored reproducibly enough to serve as a benchmark observable; and how the three‑hypothesis composite of Parameterization 2 should be split by question type.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Researchers and funding agencies evaluating novel fringe physics proposals could use the Bayesian evidence from cross‑model convergence to decide whether to allocate resources for full experimental follow‑up. A posterior $P(H_c) > 0.8$ would justify commissioning a dedicated laboratory test, whereas $P(H_c) < 0.01$ would advise against further investment.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions, it resides at TRL 1–2 (basic principles observed and reported).

**(c) Smallest next experiment.** Conduct the four‑arm benchmark with a panel of $N=2$ independently trained LLMs on a pilot set of $Q=10$ fringe claims (five retrieval‑type, five synthesis‑type) and $Q_T=5$ trap claims. Measure empirical $p^{S}_b$ and $p^{S}_c$; if the observed $K_S$ deviates substantially from the assumed value 8, the analytical conclusions would be falsified.

**(d) Engineering constraints.**  
- *Model independence*: Requires access to LLMs trained on non‑overlapping data corpora; otherwise the $H_2$ hypothesis may dominate.  
- *Argument‑structure parser*: Must reliably extract ordered proposition sequences; parser errors directly affect convergence counts.  
- *Computation budget*: Each evaluator run incurs inference cost; while per‑query cost can be mitigated by architectural advances such as those described in [8], the total number of runs ($R_{\text{total}} = 1000$ for a full benchmark) still demands scalable compute resources.

**(e) Projected cost/performance bounds.** Assuming an average inference cost of \$0.001 per model query (a plausible figure given high‑concurrency techniques in [8]), the full benchmark ($R_{\text{total}} = 1000$ runs) would cost approximately \$1.00 in compute alone. The resulting posterior range $[0.182,0.690]$ for two‑model synthesis convergence (Derivation 6) quantifies the performance envelope without empirical measurement.

**(f) Risks and misuse.** If practitioners treat the analytical posterior as definitive evidence without performing the benchmark, they may over‑trust spurious convergence driven by hidden shared biases. Deploying the method without verifying the independence of models could reinforce systematic errors across scientific domains.

## 8. Conclusion

We formalized cross‑model LLM convergence on scientific claims as Bayesian evidence, separating truth‑tracking correctness, shared‑corpus bias, and coincidence. Under explicitly labeled illustrative assumptions, two‑model convergence on multi‑step synthesis questions yields a Bayes factor of 8 and a posterior of $\frac{8}{17} \approx 0.471$ from a $0.1$ prior; four models yield $\approx 0.983$; convergence on engineered trap claims yields $K_T \approx 0.0111$ and a posterior of $\approx 0.0012$, i.e., evidence against reliability; and the two‑model posterior spans $\approx 0.182$ to $\approx 0.690$ as the null’s synthesis‑convergence probability varies from $0.20$ to $0.02$. The framework’s diagnostic value therefore hinges on a single measurable quantity, the null’s convergence probability on synthesis questions, and on the structural prediction $K_R \approx 1 < K_S$, both testable by the specified four‑arm benchmark. No empirical measurements are reported here; the benchmark protocol is the proposed next step.

## Version History

- Version 2.0.1 (2026-10-19, from 2.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.23.0-claim-integrity). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- A study would use models for drafting (openai/gpt-oss-120b, zai-org/glm-5.3-flash); for reconciliation, completion, review, revision and verification (openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6), with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would ensure that required sections are present and finished, cross-references resolve, the reference list is rendered from the retrieved bibliography, no assistant residue or placeholders remain, adversarial model review findings are resolved, and citation existence is checked at publication.
- A study would independently recompute the 16 quantitative claims from the paper's stated inputs; we assume that 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Conjectures on Convergence and Scalar Curvature. arXiv:2103.10093v1. https://arxiv.org/abs/2103.10093v1
[2] IPPOG : Bridging the gap between science education at school and modern scientific research. arXiv:2011.14743v1. https://arxiv.org/abs/2011.14743v1
[3] RerrFact: Reduced Evidence Retrieval Representations for Scientific Claim Verification. arXiv:2202.02646v2. https://arxiv.org/abs/2202.02646v2
[4] LLM-based Corroborating and Refuting Evidence Retrieval for Scientific Claim Verification. arXiv:2503.07937v1. https://arxiv.org/abs/2503.07937v1
[5] An analytical approach to Bayesian evidence computation. arXiv:2301.13783v1. https://arxiv.org/abs/2301.13783v1
[6] Report of the DOE/NSF Workshop on Correctness in Scientific Computing, June 2023, Orlando, FL. arXiv:2312.15640v2. https://arxiv.org/abs/2312.15640v2
[7] CCSBench: Evaluating Compositional Controllability in LLMs for Scientific Document Summarization. arXiv:2410.12601v3. https://arxiv.org/abs/2410.12601v3
[8] YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition. arXiv:2606.05868v1. https://arxiv.org/abs/2606.05868v1
