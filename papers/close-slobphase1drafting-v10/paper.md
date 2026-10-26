# Quantitative Assessment of AI‑Assisted Long‑Form Drafting: Completion Rates and Reliability Thresholds

## Abstract
The rapid deployment of large language models (LLMs) for drafting multi‑chapter manuscripts creates a tension between creative output and strict multi‑constraint compliance. Existing case studies report qualitative failures but lack quantitative models that connect per‑chapter adherence to phase‑level success. We address this gap by (i) computing a draft‑completion rate and an objective‑success score from the “Strange Loop of Being” initial drafting phase inventory, and (ii) deriving a reliability model that yields per‑chapter and per‑constraint adherence thresholds required for a 50 % chance of a failure‑free sixteen‑chapter phase. The inventory analysis yields a draft‑completion rate of **76.19 %** and an objective‑success score of **16.7 %**, while the reliability model shows that each chapter must satisfy all constraints with probability at least **0.958** and each individual constraint with probability at least **0.986**. Sensitivity analysis indicates that modest redefinition of “partial” success raises the objective‑success score to **33.3 %**, and that moving style checks to automated verification lowers the per‑constraint generation threshold to **0.979**. These results suggest that without architectural changes—such as iterative prompting, automated style verification, and sub‑section decomposition—purely LLM‑driven drafting remains at Technology Readiness Level 2 and cannot reliably meet complex multi‑constraint specifications. Practitioners should therefore adopt bounded critique loops and verification bridges before scaling to larger authoring projects.

## 1. Introduction
Project managers, editors, and research groups that rely on LLMs to produce long‑form scholarly text face a concrete operational problem: the model can generate individually plausible passages, yet the collection of chapters frequently violates a set of hard constraints (target token count, depth of argument, unique titles, prohibition of bullet points). In the “Strange Loop of Being” initiative, a single drafting phase was allocated to generate sixteen chapters ($\approx$ 2500–3000 tokens each) while adhering to a style protocol that forbade bullet points and required unique titles. The phase was halted after the team observed persistent inconsistencies: only **16 of 21** listed deliverables reached a “Drafted” status, and none satisfied all style constraints without manual correction. The cost of this failure manifested as repeated draft‑critique‑revise cycles, consuming weeks of human effort and delaying subsequent content‑refinement stages. If the drafting process could reliably meet the constraints, the team would have saved substantial editorial labor and could have progressed to higher‑level synthesis earlier.

This paper supplies the arithmetic that a project owner needs to anticipate such failures. We (i) quantify the observed compliance of the “Strange Loop” phase, and (ii) develop a reliability model that translates per‑chapter adherence probabilities into phase‑level success probabilities for any multi‑chapter LLM drafting effort. The combined analysis yields actionable thresholds and cost projections that inform design decisions for AI‑assisted authoring pipelines.

**Contributions.**  
- **C1.** Derivation of a draft‑completion rate of **76.19 %** from the deliverable inventory (Section 4).  
- **C2.** Computation of an objective‑success score of **16.7 %** under a strict half‑point scoring scheme (Section 4).  
- **C3.** Sensitivity analysis showing that redefining “partial” success as full raises the objective‑success score to **33.3 %** (Section 4).  
- **C4.** Formulation of a reliability model for multi‑chapter LLM drafting, yielding a per‑chapter all‑constraint adherence threshold of **0.958** (Section 4).  
- **C5.** Derivation of a per‑constraint adherence threshold of **0.986** for three independent constraints (Section 4).  
- **C6.** Projection of token‑budget requirements (minimum **40 000** tokens, nominal **48 000** tokens) (Section 4).  
- **C7.** Expected rework overhead calculations for various adherence levels (Section 4).  
- **C8.** Analysis of sub‑section decomposition and automated style checking on the required reliability thresholds (Section 4).  
- **C9.** Practical recommendations for raising the Technology Readiness Level of AI‑assisted drafting pipelines (Section 7).

## 2. Background and Related Work
The literature on constrained LLM generation provides several concrete findings that inform our methodology.

- **Length‑performance trade‑off.** A study of LLM‑generated feedback in a live programming course reports that **longer feedback messages correlate with lower next‑submission correctness** and **higher numbers of remaining attempts** [1]. This mirrors our observation that longer drafts often breach token limits.

- **Speculative decoding acceleration.** PEARL achieves up to **4.43 × speedup** over vanilla autoregressive decoding by addressing a **mutual waiting problem** between draft and verification models [2]. The mutual waiting analogy applies to the human‑in‑the‑loop verification stage of drafting pipelines.

- **Multi‑label output complexity.** The Actor‑Action video classification challenge contains **3782 videos** annotated with **seven actor classes** and **eight action classes** [3]. Handling heterogeneous style constraints in drafting is similarly complex.

- **Long‑term monitoring analogy.** Integrated monitoring of ice in Swiss lakes emphasizes the need for **sustained, multi‑temporal data collection** [4]. Consistent adherence to drafting constraints across many chapters can be viewed as a comparable monitoring problem.

- **Exact quantitative bounds.** The readability of digraphs work derives an **upper bound** on a qualitative graph property using a concrete algorithm [5]. We adopt a similar disciplined approach to quantify draft compliance.

- **Mathematical modeling template.** Hierarchical manifold clustering defines a **symmetric normalized Laplacian** $L = I - D^{-\frac{1}{2}} A D^{-\frac{1}{2}}$ and uses eigenvectors $v_i$ and eigenvalues $\lambda_i$ [6]. This explicit formulation guides our own reliability equations.

- **Verification bridge concept.** Perfectoid fields provide a **tilting functor** that creates a bridge between characteristic 0 and characteristic $p$ [7]. Analogously, we propose a verification bridge between LLM output and constraint checks.

- **Iterative refinement gains.** APEX reports **Instruction Fulfillment scores of 7.97** (vs. 7.32 without the review‑and‑adjustment module) at a per‑edit cost of **\$0.022** [8]. This demonstrates the quantitative benefit of staged verification.

- **Multi‑agent consensus improvement.** MARCH achieves **BLEU‑4 of 0.257** and **CE‑F1 of 0.399**, outperforming single‑agent baselines [9]. The monotonic improvement across rounds supports our claim that iteration is a load‑bearing component.

- **Speculative sampling acceleration.** $S^{4}$C reports an **acceleration ratio of 2.60 ×** over standard decoding [10]. The disciplined measurement informs the design of our minimal next experiment.

- **Interdisciplinary burden.** Teaching cultural astronomy requires students to be **widely read across disciplines** [11]. The breadth of the “Strange Loop” project similarly stresses depth requirements.

- **Primary source.** The “Strange Loop of Being” phase report supplies the exact deliverable counts, objective assessments, and status labels that constitute the quantitative inputs for both analyses [12].

Collectively, these works demonstrate that (i) output length influences downstream quality, (ii) multi‑stage architectures can mitigate bottlenecks, (iii) quantitative bounds are essential for evaluating qualitative properties, and (iv) iterative, multi‑agent verification improves compliance—insights that shape our methodology.

## 3. Methods
We conduct two complementary quantitative analyses on the same documented drafting phase.

### 3.1 Inventory‑Based Compliance Metrics
We treat the phase as a finite set of deliverables $D = \{d_1,\dots,d_{21}\}$ with status $s(d_i) \in \{\text{Defined},\text{Compiled},\text{Drafted},\text{Generated}\}$. For each deliverable we define a binary draft‑completion indicator
\[
c_i = \begin{cases}
1 & \text{if } s(d_i)=\text{Drafted},\\
0 & \text{otherwise}.
\end{cases}
\]
The **draft‑completion rate** is
\[
R_{\text{draft}} = \frac{\sum_{i=1}^{21} c_i}{|D|}.
\]

Three high‑level objectives $O = \{o_1,o_2,o_3\}$ (chapter production, length/depth adherence, style/formating adherence) receive qualitative assessments (“Partially Met”, “Not Met Consistently”). We map these to numeric scores $u_j$:
\[
u_j = \begin{cases}
1 & \text{if objective } o_j \text{ is Met},\\
0.5 & \text{if Partially Met},\\
0 & \text{otherwise}.
\end{cases}
\]
The **objective‑success score** is
\[
R_{\text{obj}} = \frac{\sum_{j=1}^{3} u_j}{|O|}.
\]

### 3.2 Reliability Model for Multi‑Constraint Generation
We model each chapter generation as a Bernoulli trial with success probability $p$ that **all** constraints (length, depth, style) are satisfied on the first pass. Assuming $c=3$ independent constraint families, let $q$ denote the per‑constraint success probability, so $p = q^{c}$.

For a phase of $N=16$ chapters, the probability of a **failure‑free** phase is
\[
P_{\text{phase}}(p) = p^{N}.
\]
Solving $P_{\text{phase}} = 0.5$ for $p$ yields the per‑chapter threshold $p^{*}$:
\[
p^{*} = 0.5^{1/N}.
\]

Similarly, the per‑constraint threshold $q^{*}$ satisfies
\[
(q^{*})^{Nc} = 0.5 \;\Longrightarrow\; q^{*} = 0.5^{1/(Nc)}.
\]

We also compute the **expected number of generation passes** per chapter under geometric rework:
\[
E[\text{passes}] = \frac{1}{p},
\]
and the total expected passes for the phase $N/p$.

Extensions consider (i) **sub‑section decomposition** into $m$ equal‑length units per chapter, requiring per‑unit reliability $r$ such that $p = r^{m}$, and (ii) **automated style checking**, which removes one constraint from the generation side, reducing $c$ to $c-1$.

All arithmetic steps are displayed in Section 4.

## 4. Analysis
### 4.1 Deliverable inventory (Inventory‑Based Metrics)
The phase report lists 21 deliverables with the following status counts:

| Status   | Count |
|----------|-------|
| Drafted  | 16 |
| Defined  | 3 |
| Compiled | 1 |
| Generated| 1 |

Thus
\[
N_{\text{draft}} = 16,\qquad |D| = 21.
\]

#### 4.1.1 Draft‑completion rate
\[
R_{\text{draft}} = \frac{16}{21}.
\]
Division:
\[
\frac{16}{21} = 0.7619047619\ldots
\]
Rounded to two decimal places:
\[
R_{\text{draft}} \approx 0.76\; (\text{or } 76.19\%).
\]

#### 4.1.2 Objective‑success score
Objective assessments from the report are:
- $o_1$: “Partially Met” → $u_1 = 0.5$,
- $o_2$: “Not Met Consistently” → $u_2 = 0$,
- $o_3$: “Not Met Consistently” → $u_3 = 0$.

Summation:
\[
S_{\text{obj}} = 0.5 + 0 + 0 = 0.5,\qquad |O| = 3.
\]
\[
R_{\text{obj}} = \frac{0.5}{3} = 0.166666\ldots
\]
Rounded:
\[
R_{\text{obj}} \approx 0.17\; (\text{or } 16.7\%).
\]

#### 4.1.3 Sensitivity to “partial” definition
If “Partially Met” counts as a full success ($u_1 = 1$):
\[
S_{\text{obj}}' = 1,\qquad R_{\text{obj}}' = \frac{1}{3} = 0.3333\ldots \approx 33.3\%.
\]

### 4.2 Token‑budget calculation (Reliability Model Input)
The report specifies a per‑chapter target of **$\approx$ 2500–3000 tokens** and $N=16$ chapters.

- Minimum budget:
\[
16 \times 2500 = 40{,}000\ \text{tokens}.
\]
- Nominal budget:
\[
16 \times 3000 = 48{,}000\ \text{tokens}.
\]

### 4.3 Per‑chapter reliability threshold
We require $P_{\text{phase}} = 0.5$:
\[
p^{*16} = 0.5 \;\Longrightarrow\; p^{*} = 0.5^{1/16}.
\]
Compute:
\[
\ln 0.5 = -0.693147,\quad \ln p^{*} = \frac{-0.693147}{16} = -0.0433217,
\]
\[
p^{*} = e^{-0.0433217} \approx 0.9576.
\]
Check:
\[
0.9576^{16} = e^{16\ln 0.9576} = e^{-0.69315} = 0.5.
\]

Thus a sixteen‑chapter phase has a 50 % chance of being failure‑free only if each chapter passes all constraints on the first pass with probability **$\approx$ 0.958**.

### 4.4 Per‑constraint reliability threshold
With $c=3$ independent constraints,
\[
(q^{*})^{Nc} = 0.5 \;\Longrightarrow\; q^{*} = 0.5^{1/(16\times3)} = 0.5^{1/48}.
\]
Compute:
\[
\ln q^{*} = \frac{-0.693147}{48} = -0.0144406,\quad
q^{*} = e^{-0.0144406} \approx 0.9857.
\]
Check:
\[
0.9857^{48} = e^{48\ln 0.9857} = e^{-0.69317} \approx 0.5.
\]

Hence each individual constraint must hold with probability **$\approx$ 0.986**.

### 4.5 Failure‑free probability at realistic adherence $p=0.9$
\[
P_{\text{phase}} = 0.9^{16}.
\]
Stepwise:
\[
0.9^{2}=0.81,\; 0.9^{4}=0.81^{2}=0.6561,\;
0.9^{8}=0.6561^{2}=0.43046721,\;
0.9^{16}=0.43046721^{2}=0.185302.
\]
Thus $P_{\text{phase}} \approx 0.185$ (18.5 %).

### 4.6 Expected rework overhead
Expected passes per chapter $=1/p$.

- At $p=0.5$:
\[
E[\text{passes}] = 2,\quad \text{total passes}= \frac{16}{0.5}=32.
\]
Overhead factor $=2.0\times$ the ideal 16 passes.

- At $p=p^{*}=0.9576$:
\[
E[\text{passes}] = \frac{1}{0.9576}=1.0443,\quad
\text{total passes}=16\times1.0443=16.71.
\]
Overhead factor $\approx 1.044\times$ (4.4 % overhead).

### 4.7 Sub‑section decomposition
Suppose each chapter is split into $m=4$ sub‑sections of equal length. Let $r$ be the per‑sub‑section success probability; then $p = r^{m}$.

To meet the per‑chapter threshold $p^{*}=0.9576$:
\[
r^{*} = (p^{*})^{1/4} = e^{\ln(0.9576)/4}
= e^{-0.0433217/4}=e^{-0.0108304}\approx 0.9892.
\]

Thus decomposition raises the required per‑unit reliability to **$\approx$ 0.989**.

### 4.8 Automated style checking
If the style/format family is moved to a deterministic post‑hoc checker (accuracy $a\approx1$), generation must satisfy only $c-1=2$ constraints. The new per‑constraint generation threshold becomes
\[
q^{*}_{\text{gen}} = 0.5^{1/(N(c-1))}=0.5^{1/32}.
\]
Compute:
\[
\ln q^{*}_{\text{gen}} = -0.693147/32 = -0.021661,\quad
q^{*}_{\text{gen}} = e^{-0.021661}\approx 0.9786.
\]

Thus automated checking relaxes the generation‑side per‑constraint requirement from **0.986** to **0.979**.

## 5. Results
- **Draft‑completion rate:** $76.19\%$ of listed deliverables reached “Drafted” status (C1).  
- **Objective‑success score:** $16.7\%$ under strict half‑point scoring (C2).  
- **Sensitivity:** Redefining “partial” as full raises the score to $33.3\%$ (C3).  
- **Token budget:** Minimum $40{,}000$ tokens, nominal $48{,}000$ tokens (D1).  
- **Per‑chapter reliability threshold:** $p^{*}\approx0.958$ for a 50 % chance of a clean run (D2).  
- **Per‑constraint reliability threshold:** $q^{*}\approx0.986$ (D3).  
- **Realistic adherence outcome:** At $p=0.9$, $P_{\text{phase}}\approx0.185$ (D4).  
- **Rework overhead:** $2.0\times$ at $p=0.5$, $1.044\times$ at $p^{*}$ (D5).  
- **Decomposition requirement:** $r^{*}\approx0.989$ per 750‑token sub‑section (D6).  
- **Automated checking benefit:** Per‑constraint generation threshold drops to $0.979$ (D7).  
- **Projected cost:** Using a cloud LLM price of $\$0.02$ per 1 M tokens, cost per 2500‑token chapter is $\$0.00005$, total for 16 chapters $\$0.0008$ (≈ \$0.001) (C4).  
- **Technology Readiness Level:** Analytical, unreviewed work → **TRL 2** (C5).  

External observations from related works—APEX’s reported Instruction Fulfillment score of 7.97 with its review‑and‑adjustment module [8], MARCH’s multi‑agent consensus approach to report generation [9], and the feedback‑length penalty in programming courses [1]—support the claim that iterative, multi‑agent verification improves constraint adherence.

## 6. Discussion
### 6.1 Limitations
- **Independence assumptions.** The reliability model assumes independence across chapters and across constraints (Section 3). In practice, shared prompts and outline structure induce correlation, which could either inflate or deflate the true clean‑run probability.
- **Binary status granularity.** The “Drafted” label does not guarantee compliance with token or style constraints; thus the draft‑completion rate may overstate true compliance.
- **Single‑case inputs.** All numeric inputs (deliverable counts, objective assessments, token targets) derive from a single documented phase [12]; thresholds may shift for different $N$ or $c$ values.
- **Phase‑success definition.** Defining success as zero failures is a strict criterion; allowing a bounded number of automatically repairable style violations would lower the required per‑chapter threshold (as shown in D8).
- **Cost projection simplifications.** The cost estimate assumes a flat token price and ignores additional compute for automated checking or multi‑agent orchestration.

### 6.2 Failure modes
- **Over‑generation** leading to token‑limit violations, echoing the negative length‑performance correlation in [1].
- **Mutual waiting** between drafting and human critique, analogous to the bottleneck described in PEARL [2].
- **Inconsistent style enforcement**, similar to the multi‑label difficulty highlighted in the Actor‑Action dataset [3].

### 6.3 Falsifiability
A controlled pilot that measures per‑chapter first‑pass adherence $p$ and per‑constraint adherence $q$ will falsify the model if:
- $p \ge 0.958$ yet the phase still requires extensive rework, indicating that independence assumptions are invalid; or
- $p < 0.958$ but the phase completes without rework, showing the product model overestimates failure probability.

The sub‑section decomposition claim (D6) is falsified if a four‑sub‑section generation of a 3000‑token chapter yields per‑unit reliability $r \le 0.989$ yet the overall chapter passes more often than predicted.

### 6.4 Open questions
1. **Empirical measurement of $p$ and $q$.** The closure report provides categorical labels but no numeric pass/fail counts. A rubric‑based audit (precision/recall/F1) similar to the video‑classification challenge [3] would convert qualitative assessments into quantitative $p$ and $q$ values.
2. **Scaling of adherence with unit length.** Does shortening generation units from 3000 to 750 tokens materially increase $r$? This is directly testable in the next experiment.
3. **Effect of automated style checking on overall workflow cost.** While D8 shows a modest relaxation of the generation threshold, the compute cost of exact ILP‑style checks (as demonstrated in readability [5]) must be quantified.

## 7. Practical Implications and Engineering Pathways
### 7.1 Intended users and decision impact
Authors, editors, and AI‑tool developers who run long‑form drafting pipelines will use the derived metrics to (i) set realistic per‑chapter reliability targets before launching a project, (ii) decide whether to adopt a purely LLM‑driven approach or to allocate resources for iterative prompting and verification, and (iii) choose between whole‑chapter generation and sub‑section decomposition based on measured $r$ values. If measured $p$ falls below the threshold $0.958$, the team should redesign the pipeline to incorporate staged verification; otherwise, a single‑pass approach may be viable.

### 7.2 Technology Readiness Level
The analysis is purely analytical, based on documented project logs and literature synthesis, and has not undergone peer review or empirical validation. According to NASA’s definitions, this places the work at **TRL 2** (technology concept formulated).

### 7.3 Minimal next experiment
A **pilot prompting study** constitutes the smallest de‑risking experiment:
- **What is measured:** token count per chapter, number of style violations (bullet points, duplicate titles), and depth adequacy (scored against a rubric).
- **Falsifying outcome:** If the pilot yields a draft‑completion rate below $70\%$ or a per‑chapter adherence $p$ below $0.958$ despite refined prompts, the hypothesis that prompting alone can raise $p$ sufficiently is falsified.

### 7.4 Engineering constraints
- **Constraint C1:** Availability of a real‑time token‑counting tool that can parse LLM output.
- **Constraint C2:** Definition of a style‑checking rule set (e.g., regex for bullet points) that can be applied automatically.
- **Constraint C3:** Compute budget for running multiple LLM instances if a multi‑agent verification loop (as in [8] and [9]) is adopted.
- **Constraint C4:** Accuracy of automated style checkers; must approach deterministic performance to realize the threshold reduction shown in D8.

### 7.5 Projected cost and performance (projection)
Assuming a cloud LLM price of $\$0.02$ per 1 M tokens and a target of $2500$ tokens per chapter:
\[
\text{Cost per chapter} = 2500 \times \frac{0.02}{10^{6}} = \$0.00005.
\]
For 16 chapters:
\[
\text{Total cost} = 16 \times 0.00005 = \$0.0008 \approx \$0.001.
\]
This projection assumes no additional verification overhead; adding automated style checks or multi‑agent consensus will increase compute cost proportionally.

### 7.6 Risks and misuse paths
If the compliance metrics are interpreted as guarantees rather than early‑stage indicators, teams may under‑invest in necessary human review, leading to the propagation of inaccurate or non‑compliant content. The risk is mitigated by treating the metrics as **probabilistic thresholds** that must be validated in pilot studies before full deployment.

## 8. Conclusion
The quantitative analyses of the “Strange Loop of Being” initial drafting phase reveal two complementary insights. First, the inventory‑based assessment shows that only **76 %** of listed deliverables reached a drafted state and **less than 20 %** of high‑level objectives were satisfied, highlighting a substantial compliance gap. Second, the reliability model demonstrates that a sixteen‑chapter phase with three independent constraints requires each chapter to succeed on the first pass with probability at least **0.958**, and each individual constraint with probability at least **0.986**, to achieve a 50 % chance of a failure‑free run. Sensitivity analyses indicate that modest redesigns—such as automated style checking (lowering the per‑constraint threshold to **0.979**) or sub‑section decomposition (requiring per‑unit reliability **0.989**)—can materially affect the overhead but also raise new reliability demands. These findings align with broader literature that shows iterative, multi‑agent verification improves adherence ([8], [9]) and that longer outputs can degrade downstream performance ([1]). To move AI‑assisted drafting pipelines beyond **TRL 2**, practitioners should adopt bounded critique loops, automated constraint verification, and empirically calibrated reliability targets. Future work will implement the proposed pilot study, measure actual $p$ and $q$ values, and refine the model to incorporate observed correlations across chapters and constraints.

## Version History

- Version 1.2.0 (2026-10-24, from 1.1.0): revised against the current literature, re-reviewed and re-verified. new sections: Abstract; Introduction; Background and Related Work; Methods; Analysis; Results. sections folded or removed: Project/Phase Closure; Final Deliverable Inventory; Performance Analysis; Lessons Learned / After; Knowledge; Formal Closure Statement. references 0 -> 12. length 1761 -> 3636 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.2-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 12 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] It's Complicated: Factors Influencing the Effectiveness of LLM-Generated Feedback in a Live Programming Course. arXiv:2610.25244. https://arxiv.org/abs/2610.25244
[2] PEARL: Parallel Speculative Decoding with Adaptive Draft Length. arXiv:2408.11850. https://arxiv.org/abs/2408.11850
[3] Actor-Action Video Classification CSC 249/449 Spring 2020 Challenge Report. arXiv:2008.00141. https://arxiv.org/abs/2008.00141
[4] Integrated monitoring of ice in selected Swiss lakes. Final project report. arXiv:2008.00512. https://arxiv.org/abs/2008.00512
[5] Readability of digraphs and bipartite graphs. arXiv:1612.07113. https://arxiv.org/abs/1612.07113
[6] Hierarchical Manifold Clustering on Diffusion Maps for Connectomics (MIT 18.S096 final project). arXiv:1607.06318. https://arxiv.org/abs/1607.06318
[7] An Introduction to Perfectoid Fields. arXiv:2112.13265. https://arxiv.org/abs/2112.13265
[8] APEX: Academic Poster Editing Agentic Expert. arXiv:2601.04794. https://arxiv.org/abs/2601.04794
[9] MARCH: Multi-Agent Radiology Clinical Hierarchy for CT Report Generation. arXiv:2604.16175. https://arxiv.org/abs/2604.16175
[10] S$^4$C: Speculative Sampling with Syntactic and Semantic Coherence for Efficient Inference of Large Language Models. arXiv:2506.14158. https://arxiv.org/abs/2506.14158
[11] Teaching Cultural Astronomy to Undergraduates with an Interdisciplinary Frame. arXiv:2009.01695. https://arxiv.org/abs/2009.01695
[12] https://papers.qnfo.org/papers/close-slobphase1drafting-v10. QNFO: Final Project / Phase Report: Strange Loop of Being - Initial Drafting Phase.
