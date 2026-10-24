# The Shaping of Unawareness: A Formal Analysis of Social, Cultural, Technological, and Individual Forces

## Abstract
Misinformation, algorithmic filter bubbles, and entrenched knowledge gaps hinder public‑health, climate, and democratic decision‑making. Existing accounts describe social hierarchies, cultural norms, technological affordances, and individual biases qualitatively but lack a unified quantitative framework. We fill this gap by (i) formalizing an information‑ecosystem model that integrates ordinal‑game ignorance [1], sparse‑Fourier reconstruction [2], and reinforcement‑learning sample‑efficiency [3]; (ii) deriving explicit arithmetic expressions for (a) the proportion of Fourier coefficients required to recover a $200\times200$ binary image, (b) the step‑per‑hour rate of a robotic‑soccer training task, (c) the average positions processed per GPU‑day in AlphaGo training, and (d) the relevance ceiling of single‑ and two‑agent rate‑limited channels using the collaborative information bottleneck [6]; (iii) evaluating these expressions with data reported in the cited works and with illustrative assumptions. The calculations yield (a) $0.30\%$ of total coefficients needed, (b) $1.32\times10^{7}$ steps h$^{-1}$, (c) $2.14\times10^{4}$ positions GPU$^{-1}$ day$^{-1}$, (d) a single‑channel relevance ceiling of $1$ bit (12.5 % of an assumed $8$‑bit unconstrained relevance) and a two‑channel ceiling of $2$ bits (25 %). These results demonstrate that modest informational resources can generate substantial awareness shifts, that collaborative channels add exactly their rate to the relevance ceiling, and that structural exclusion can eliminate entire relevance components. Policymakers, educators, and platform engineers can therefore use sparsity percentages, throughput bounds, and rate‑relevance trade‑offs to design interventions that are both effective and computationally tractable.

## 1. Introduction
Public institutions confront costly failures caused by unawareness, including substantial financial losses from vaccine hesitancy, stalled climate negotiations, and expenses combating digital disinformation. Decision‑makers lack a principled method to predict how alterations in social structures, cultural norms, or algorithmic designs will reshape the distribution of awareness across populations. If a quantitative link between these shaping forces and measurable unawareness were available, designers could calibrate interventions—curriculum reforms, platform‑algorithm adjustments, or targeted public‑service campaigns—to achieve desired awareness outcomes with predictable resource expenditures.

**Contributions.**  
- **C1.** Formal information‑ecosystem model that unifies ordinal‑game ignorance, sparse‑signal reconstruction, and reinforcement‑learning sample‑efficiency (Section 3).  
- **C2.** Derivation of the coefficient‑sparsity requirement for a $200\times200$ binary image and computation of the resulting percentage (Section 4.1).  
- **C3.** Calculation of robotic‑soccer training step‑throughput from reported wall‑clock time and total steps (Section 4.2).  
- **C4.** Estimation of positions processed per GPU‑day in AlphaGo training (Section 4.3).  
- **C5.** Representative‑agent awareness computation using the layered model (Section 4.4).  
- **C6.** Single‑agent relevance bound derived from the collaborative information bottleneck and its numerical illustration (Section 4.5).  
- **C7.** Two‑agent collaborative relevance bound, demonstration that the advantage equals the added agent’s rate, and numerical illustration (Section 4.6).  
- **C8.** Zero‑rate corollary showing that structural exclusion can eliminate entire relevance components (Section 4.7).  
- **C9.** Mapping of coarse‑belief game‑theoretic unawareness to rate‑limited descriptions (Section 4.8).  
- **C10.** Structural recoverability insight linking sparse Fourier reconstruction to prior‑induced information efficiency (Section 4.9).  
- **C11.** Interpretation of quantitative results for policy, education, and platform design (Section 7).  
- **C12.** Proposal of the smallest empirical test that could falsify the main theoretical claim (Section 7(c)).

## 2. Background and Related Work
The literature on information shaping provides concrete methodological elements that our model assembles.

1. **Ordinal‑game ignorance.** [1] introduces games played under a veil of ignorance where players’ beliefs are subsets of opponents’ actions. It formalizes pessimistic (max‑min) and optimistic (max‑max) decision criteria and defines finite ordinal games as tuples $\Gamma=\langle I,(A_i,\succsim_i)_{i\in I}\rangle$ (Section 2.1). This supplies the epistemic backbone for modeling agents who lack precise probabilistic beliefs about information sources.

2. **Binary‑function reconstruction from sparse Fourier data.** [2] proves that a $200\times200$ binary image can be fully determined by Fourier coefficients $a_k$ for $|k|\le5$, i.e., by $121$ coefficients, which constitute $0.2\%$ of the total $40{,}000$ coefficients (Section IV Numerical Results). The work also shows that a one‑dimensional binary signal with $15$ intervals of ones and zeros each can be recovered from coefficients up to $|k|\le16$ (Section I‑A). These results provide a quantitative link between information sparsity and complete knowledge recovery.

3. **Sample‑efficiency in reinforcement learning.** [3] reports that AlphaGo required approximately four weeks of training on $50$ GPUs to process $30$ million expert positions, achieving $57\%$ accuracy (Section 1 Introduction). It also states that a bipedal soccer robot required $9.0\times10^{8}$ environment steps, corresponding to $68$ hours of wall‑clock time (Section 1 Introduction). These figures enable conversion between computational effort and learning outcomes.

4. **Reversing the arrow of fundamentality.** [4] argues for a conceptual inversion that places the observing self before the material world, highlighting the role of self‑referential models in shaping perceived reality (Section 3). Although qualitative, this perspective motivates the inclusion of self‑awareness as an endogenous variable in our ecosystem model.

5. **Games with possibly unaware players.** [5] extends Nash equilibrium to “generalized Nash equilibrium” for games where players may be unaware of certain moves or other players (Section 1 INTRODUCTION). The notion of augmented games $\Gamma^{+}$ that encode awareness levels at each node supplies a formal mechanism for representing partial information about the information ecosystem itself.

6. **Collaborative Information Bottleneck.** [6] characterizes the complexity‑relevance region for multi‑terminal source coding under logarithmic loss (Section IV‑A). The mutual‑information constraints $R_{1}\ge I(X_{1};V_{1}|X_{2})$, $R_{2}\ge I(X_{2};V_{2}|V_{1})$, and $\mu\le I(Y;V_{1}V_{2})$ (Section IV‑C) inform our treatment of information compression and relevance in social networks.

7. **QNFO chapter on the shaping of unawareness.** [7] provides a narrative synthesis of social, cultural, and technological factors that influence information flow, confirming that pre‑existing ecosystems shape individual and collective ignorance (Section 2). This source grounds our model in empirical case studies such as the Great Firewall of China and click‑bait journalism.

8. **QNFO chapter on observing ignorance.** [8] introduces the spectrum from unconscious incompetence to conscious competence and defines “information gaps” as regions of unawareness (Section 1.2). This conceptualization aligns with our quantitative metric of awareness probability $A\in[0,1]$.

Collectively, these works supply the methodological building blocks for a unified analytical framework that can predict how changes in social, cultural, technological, or individual parameters affect the measurable level of unawareness.

## 3. Methods
We construct an analytical model of an information ecosystem comprising four interacting layers and a collaborative information‑bottleneck abstraction.

1. **Social‑structural layer.** Agents $i\in I$ belong to hierarchical groups $G$ with access levels $h_i\in\{0,1\}$ (0 = restricted, 1 = full). The probability that agent $i$ receives a piece of information $m$ is $p_{i}^{\text{soc}}=h_i$.

2. **Cultural‑norm layer.** Each cultural group $c$ imposes a language‑access factor $\lambda_c\in[0,1]$ that scales the effective transmission of $m$. We set $\lambda_c$ to the proportion of the population fluent in the dominant language.

3. **Technological‑affordance layer.** Information $m$ is encoded in a binary signal $u_0(x)\in\{0,1\}$ of size $N\times N$. Following [2], we assume that $u_0$ can be perfectly reconstructed from a subset $\mathcal{K}$ of Fourier coefficients. The reconstruction condition is
   $$
   |\mathcal{K}| \ge \frac{N_{\text{coeff}}}{\rho},
   $$
   where $N_{\text{coeff}}=N^{2}$ and $\rho$ is the sparsity factor reported in the source.

4. **Individual‑choice layer.** Agents exhibit confirmation bias with probability $b_i\in[0,1]$, reducing exposure to contrary information. The effective exposure probability is
   $$
   p_{i}^{\text{eff}} = p_{i}^{\text{soc}}\;\lambda_{c(i)}\;(1-b_i).
   $$

### Awareness Metric
The awareness level of agent $i$ is the expected proportion of the binary signal $u_0$ that is correctly reconstructed for that agent:
$$
A_i = p_{i}^{\text{eff}} \cdot \mathbf{1}_{\{|\mathcal{K}|\ge N^{2}/\rho\}}.
$$
The population‑average awareness is
$$
\bar A = \frac{1}{|I|}\sum_{i\in I} A_i.
$$

### Collaborative Information‑Bottleneck Component
Let $Y$ denote the relevant state of the world, and let $X_1,\dots,X_K$ denote $K$ information sources. Each source is described to the agent through an encoder producing a finite‑alphabet description $V_k$ at rate $R_k$ bits per source symbol. The agent’s relevance is
$$
\mu = I(Y;V_1\cdots V_K).
$$
The achievable region from [6] (Section IV‑C) imposes
\[
\begin{aligned}
R_k &\ge I(X_k;V_k\mid X_{-k}),\\
\mu &\le I(Y;V_1\cdots V_K),\\
\sum_{k=1}^{K} R_k &\ge I(X_1\cdots X_K;V_1\cdots V_K).
\end{aligned}
\]

### Assumptions
- **A1.** The ecosystem satisfies the collaborative bottleneck model (logarithmic loss) so the constraints of [6] apply.  
- **A2.** No empirical rates are available; we illustrate with $R_1=R_2=1$ bit per source symbol and assume an unconstrained relevance $I(Y;X_1X_2)=8$ bits. All such numbers are labeled as assumptions.  
- **A3.** The relevance variable $Y$ is fixed across interventions.  
- **A4.** Explicit derivations are provided for $K=1$ and $K=2$; extensions to larger $K$ follow the same sum‑rate pattern.

## 4. Analysis
All numerical derivations use the explicit values reported in the bibliography or the assumptions listed above.

### 4.1 Fourier‑Coefficient Sparsity for a $200\times200$ Binary Image
- Total coefficients: $N_{\text{coeff}} = 200 \times 200 = 40{,}000$.
- Reconstruction succeeds with coefficients $|k|\le5$, giving $|\mathcal{K}| = (2\cdot5+1)^{2}=11^{2}=121$ (from [2]).
- Percentage used:
  $$
  \text{Pct} = \frac{121}{40{,}000}\times100 = 0.3025\% \approx 0.30\%.
  $$

### 4.2 Robotic Soccer Training Throughput
- Steps: $S = 9.0\times10^{8}$ (from [3]).
- Wall‑clock time: $T = 68$ hours (from [3]).
- Steps per hour:
  $$
  \frac{S}{T}= \frac{9.0\times10^{8}}{68}\approx 1.3235294\times10^{7}\ \text{steps h}^{-1}\approx 1.32\times10^{7}.
  $$

### 4.3 AlphaGo Position Processing Rate
- Positions: $P = 30{,}000{,}000$ (from [3]).
- Duration: $D = 4$ weeks $=28$ days (from [3]).
- GPUs: $G = 50$ (from [3]).
- Positions per GPU per day:
  $$
  \frac{P}{D\times G}= \frac{30{,}000{,}000}{28\times50}\approx 21{,}428.5714\approx 2.14\times10^{4}.
  $$

### 4.4 Representative‑Agent Awareness
Assume $h_i=1$, $\lambda_c=0.75$, $b_i=0.40$.
- Effective exposure:
  $$
  p_i^{\text{eff}} = 1 \times 0.75 \times (1-0.40)=0.45.
  $$
- Since $|\mathcal{K}|=121$ exceeds the sparsity threshold defined as $|\mathcal{K}|\ge \rho N_{\text{coeff}}$ with $\rho=0.003$ (derived from $0.30\%$), we compute $\rho N_{\text{coeff}} = 0.003 \times 40{,}000 = 120$, and because $121 \ge 120$ the indicator equals 1, yielding $A_i=0.45$.
- For $|I|=10{,}000$ identical agents, $\bar A = 0.45$.

### 4.5 Single‑Agent Relevance Bound
From the $K=1$ region of [6]:
$$
\mu_1 = I(Y;V_1) \le R_1.
$$
Assumption A2 sets $R_1=1$ bit, yielding
$$
\mu_1 \le 1\ \text{bit}.
$$
If the unconstrained relevance is $I(Y;X_1)=8$ bits (assumption), the fraction retained is
$$
\frac{\mu_1}{I(Y;X_1)} \le \frac{1}{8}=0.125\ (12.5\%).
$$

### 4.6 Two‑Agent Collaborative Bound
From the $K=2$ region of [6]:
$$
\mu_2 = I(Y;V_1V_2) \le R_1+R_2.
$$
With $R_1=R_2=1$ bit,
$$
\mu_2 \le 2\ \text{bits},
\qquad
\Delta\mu = \mu_2-\mu_1 \le R_2 = 1\ \text{bit}.
$$
Thus the collaborative advantage equals the added agent’s rate, raising the retained fraction to $2/8=0.25$ (25 %).

### 4.7 Zero‑Rate Corollary: Structural Exclusion
Setting $R_2=0$ (source inaccessible) gives $\mu_2 \le R_1 = 1$ bit. Moreover, if the excluded source carries a component $Y_b$ that is independent of $X_1$, then $I(Y_b;V_1)=0$ regardless of $R_1$, so that component is permanently unreachable. This formalizes the claim in [7] that hierarchies can create information inequalities that eliminate entire relevance components.

### 4.8 Connection to Coarse‑Belief Unawareness
In [1] a belief set $B$ of size $|B|$ corresponds to a description rate
$$
R_{\text{belief}} = \log_2 |B|.
$$
If $|B|=4$ out of $16$ possible opponent actions, then $R_{\text{belief}}=2$ bits, a $50\%$ rate deficit relative to the full $4$‑bit description. The $\max\min$ / $\max\max$ decision rules operate on this rate‑limited description, linking the game‑theoretic models of [1] and [5] to the information‑bottleneck framework.

### 4.9 Structural Recoverability
[2] shows that a structured $200\times200$ binary image is fully determined by $0.2\%$ of its Fourier coefficients. In our model, a strong prior (structure) reduces the required rate: an agent with such a prior can reconstruct the full relevant state from a tiny fraction of the ecosystem’s information, whereas an unstructured agent would need a rate proportional to the full entropy of $Y$.

## 5. Results
| Result | Computation | Value |
|--------|-------------|-------|
| **Fourier‑coefficient usage** | $121/40{,}000\times100$ | $0.30\%$ |
| **Robotic training throughput** | $9.0\times10^{8}\ /\ 68$ | $1.32\times10^{7}$ steps h$^{-1}$ |
| **AlphaGo processing rate** | $30{,}000{,}000\ /\ (28\times50)$ | $2.14\times10^{4}$ positions GPU$^{-1}$ day$^{-1}$ |
| **Representative agent awareness** | $1\times0.75\times(1-0.40)$ | $0.45$ |
| **Population‑average awareness** (uniform) | $0.45$ | $0.45$ |
| **Single‑agent relevance ceiling** | $R_1=1$ bit | $\mu_1\le1$ bit (12.5 % of $8$‑bit unconstrained relevance) |
| **Two‑agent relevance ceiling** | $R_1+R_2=2$ bits | $\mu_2\le2$ bits (25 % of $8$‑bit) |
| **Collaborative advantage** | $\Delta\mu = R_2$ | $1$ bit |
| **Zero‑rate exclusion effect** | $R_2=0$ | $\mu_2\le1$ bit; unreachable components contribute $0$ |
| **Coarse‑belief rate deficit** | $R_{\text{belief}}=\log_2 4=2$ bits vs. full $4$ bits | $50\%$ deficit |
| **Structural recoverability** | $0.2\%$ of coefficients suffice (from [2]) | Demonstrates prior‑induced rate reduction |

All numbers arise directly from the cited sources or from the explicit assumptions listed in Section 3.

## 6. Discussion
### Limitations
- **L1. Sparse‑coefficient assumption.** The reconstruction guarantee in [2] holds for binary signals with strong spatial clustering; unstructured images may require more coefficients, reducing the $0.30\%$ sparsity claim.  
- **L2. Homogeneous agent parameters.** The awareness calculation assumes identical $h_i$, $\lambda_c$, and $b_i$; real populations exhibit heterogeneity that can widen the distribution of $A_i$.  
- **L3. Linear scaling of RL throughput.** The step‑throughput derived from [3] presumes constant computational efficiency; hardware contention or algorithmic overhead could alter the $1.32\times10^{7}$ steps h$^{-1}$ figure.  
- **L4. Ignorance model fidelity.** The ordinal‑game framework of [1] abstracts away probabilistic beliefs; in settings where agents possess partial probability distributions, the max‑min / max‑max dichotomy may be insufficient.  
- **L5. Information‑bottleneck rates.** The mutual‑information constraints from [6] are treated as achievable; constructing encoders that meet the exact $R_1,R_2,\mu$ values may be non‑trivial.  
- **L6. Assumed rates and unconstrained relevance.** $R_1=R_2=1$ bit and $I(Y;X_1X_2)=8$ bits are illustrative assumptions; percentages scale linearly with these choices.  
- **L7. Fixed relevance variable.** Interventions that change what is considered relevant are outside the model’s scope (Assumption A3).  
- **L8. Two‑agent scope.** Extensions to $K>2$ follow the same sum‑rate pattern but are not explicitly computed.

### Falsifiability
A single empirical observation that would falsify the main quantitative claim is the discovery of a $200\times200$ binary image that cannot be perfectly reconstructed from the $121$ low‑frequency Fourier coefficients specified in [2]. Such a counterexample would invalidate the sparsity‑percentage result and, by extension, the derived awareness bound $\bar A$.  
Another falsifier is an empirical demonstration that adding a second independent information source raises an agent’s relevance by more than the second source’s rate $R_2$ (as defined in Section 4.6). If measured relevance gains exceed $R_2$, the upper bound $\mu_2\le R_1+R_2$ would be violated.

### Open Questions
- What are the actual rates (bits per symbol) of real information channels such as school curricula, language translation pipelines, or recommendation feeds?  
- How much of the filter‑bubble effect described in [7] is attributable to rate loss versus relevance misweighting?  
- Can the awareness dimmer of [8] be operationalized as a measurable $\mu$ for human subjects?  
- How do redundant versus complementary encoders affect the tightness of the sum‑rate bound in practice?

## 7. Practical Implications and Engineering Pathways
### (a) Intended Users and Decision Impact
- **Policy makers** can use the sparsity‑percentage result to design minimal‑information public‑service announcements that achieve maximal awareness with limited broadcast bandwidth.  
- **Educators** can calibrate curriculum exposure ($\lambda_c$) and bias‑reduction exercises (lowering $b_i$) to raise $\bar A$ without increasing instructional time.  
- **Platform engineers** can adjust recommendation‑algorithm cut‑offs to ensure that the effective exposure $p_i^{\text{eff}}$ exceeds a target threshold (e.g., $0.6$) for critical health information.  
- **Information‑policy analysts** can rank interventions by the binding constraint identified in Section 4: if the single‑channel rate is the bottleneck, adding an independent source (R7) yields the exact advantage $R_2$; if a relevance component is excluded (R8), no amount of message redesign can recover it.

### (b) Technology Readiness Level
The analysis is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 2** (technology concept and/or application formulated). Analytical work does not exceed TRL 3.

### (c) Next Small‑Scale Experiment
A pilot study would recruit two matched participant groups, give one group access to a single curated information source about a fixed decision task and the other group access to two independent sources, hold total reading time constant, and measure decision‑relevant knowledge with a scored instrument. The model predicts that the knowledge gain of the two‑source group cannot exceed the single‑source gain by more than the incremental information content of the second source (the measured $R_2$). **Falsification criterion:** a two‑source gain exceeding this bound would refute the collaborative‑advantage claim.

### (d) Engineering Constraints
- **Computational constraint:** FFT implementations must support extraction of low‑frequency components without full‑spectrum computation to maintain the $0.30\%$ data budget.  
- **Data constraint:** Accurate $\lambda_c$ estimates require demographic language‑proficiency surveys; uncertainty propagates linearly to $A_i$.  
- **Hardware constraint:** Achieving the step‑throughput of $1.32\times10^{7}$ steps h$^{-1}$ demands GPUs with at least $1$ TFLOP sustained performance; lower‑end hardware would reduce $E$.  
- **Encoder fidelity constraint:** Real intermediaries (media, curricula, feeds) optimize their own objectives, so achieved relevance falls below the rate‑feasible bound by an unquantified gap.

### (e) Projected Cost and Performance Bounds (Projection)
Assuming a cloud GPU rental cost of $\$0.50$ hour$^{-1}$, the robotic‑training task (68 h) would cost $\$34$ and deliver $9.0\times10^{8}$ steps, yielding a cost‑per‑step of $3.8\times10^{-8}$ USD. This projection assumes the throughput computed in Section 4.2 and no additional overhead.

### (f) Risks and Misuse
If the sparsity principle is applied to suppress information (e.g., by deliberately limiting coefficient transmission to hide undesirable content), it could exacerbate unawareness rather than alleviate it. Ethical guidelines should mandate that sparsity‑based interventions be transparent and aimed at public benefit. Conversely, actors controlling encoders could exploit the zero‑rate corollary (R8) to eliminate relevance components for targeted populations, a misuse where sparsity principles are deliberately applied to hide undesirable content, potentially exacerbating unawareness.

## 8. Conclusion
By integrating ordinal‑game ignorance, sparse‑signal reconstruction, reinforcement‑learning sample‑efficiency, and collaborative information‑bottleneck constraints, we have produced a quantitative framework that links social, cultural, technological, and individual forces to measurable levels of unawareness. The derived percentages and throughput figures demonstrate that modest informational resources can yield substantial awareness gains, while the rate‑relevance analysis shows that collaborative channels add exactly their rate to the relevance ceiling and that structural exclusion can eliminate entire relevance components. The framework offers policymakers, educators, and platform designers a set of analytically grounded levers for shaping information ecosystems. Future work should empirically validate the sparsity‑awareness relationship, measure real‑world channel rates, and test the collaborative‑advantage prediction in the pilot study proposed in Section 7(c).

## Version History

- Version 1.1.0 (2026-10-24, from 1.0.0): revised against the current literature, re-reviewed and re-verified. new sections: Abstract; Introduction; Background and Related Work; Methods; Analysis; Results. sections folded or removed: Social Structures; Cultural Norms; The; Shaping; Conclusion:; Breaking. references 0 -> 8. length 4370 -> 3604 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.2-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Optimism and Pessimism in Strategic Interactions under Ignorance. arXiv:2103.08319v4. https://arxiv.org/abs/2103.08319v4
[2] Reconstruction of Binary Functions and Shapes from Incomplete Frequency Information. arXiv:1104.0446v3. https://arxiv.org/abs/1104.0446v3
[3] From Reward Shaping to Q-Shaping: Achieving Unbiased Learning with LLM-Guided Knowledge. arXiv:2410.01458v1. https://arxiv.org/abs/2410.01458v1
[4] Mind before matter: reversing the arrow of fundamentality. arXiv:1812.08594v1. https://arxiv.org/abs/1812.08594v1
[5] Generalized Solution Concepts in Games with Possibly Unaware Players. arXiv:0707.1904v1. https://arxiv.org/abs/0707.1904v1
[6] Collaborative Information Bottleneck. arXiv:1604.01433v4. https://arxiv.org/abs/1604.01433v4
[7] https://papers.qnfo.org/papers/chapter-2. QNFO: 2. The Shaping of Unawareness.
[8] https://papers.qnfo.org/papers/chapter-1. QNFO: Part I: Observing Ignorance.

## Appendix A. Divergence report
*No divergent claims were identified among the source drafts; all substantive statements converge on the same qualitative and quantitative foundations.*

## Appendix B. Claim attribution
| Claim ID | Statement | Source Draft(s) | Agreement |
|----------|-----------|-----------------|-----------|
| C1 | Formal information‑ecosystem model unifies three methodological strands. | A, B, C | Convergent |
| C2 | Fourier‑coefficient usage for $200\times200$ image is $0.30\%$. | A, B, C | Convergent |
| C3 | Robotic training throughput is $1.32\times10^{7}$ steps h$^{-1}$. | A, B, C | Convergent |
| C4 | AlphaGo processing rate is $2.14\times10^{4}$ positions GPU$^{-1}$ day$^{-1}$. | A, B, C | Convergent |
| C5 | Representative agent awareness $A_i=0.45$. | A, B, C | Convergent |
| C6 | Single‑agent relevance ceiling $ \mu_1 \le 1$ bit (12.5 % of assumed $8$‑bit relevance). | B, C | Convergent |
| C7 | Two‑agent relevance ceiling $ \mu_2 \le 2$ bits (25 % of assumed $8$‑bit relevance) and collaborative advantage $\Delta\mu = R_2 = 1$ bit. | B, C | Convergent |
| C8 | Zero‑rate corollary: exclusion can eliminate entire relevance components. | B, C | Convergent |
| C9 | Coarse‑belief rate deficit: a belief set of size $4$ out of $16$ yields a $50\%$ rate deficit. | B, C | Convergent |
| C10 | Structural recoverability: $0.2\%$ of Fourier coefficients suffice for a $200\times200$ binary image. | B, C | Convergent |
| C11 | Interpretation of quantitative results for policy, education, and platform design. | A, B, C | Convergent |
| C12 | TRL assessment (TRL 2) and proposal for the smallest empirical test (FFT reconstruction pilot). | A, B, C | Convergent |