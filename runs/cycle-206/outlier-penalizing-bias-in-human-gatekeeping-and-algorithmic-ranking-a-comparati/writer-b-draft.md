# Outlier-Penalizing Bias Structure in Human and Algorithmic Gatekeeping: A Threshold Model, a Worked Asymmetry Derivation, and a Test Protocol

## Abstract

Editors, grant panels, hiring committees, and recommendation or search systems all act as gatekeepers over novel work, and authors of interdisciplinary or unconventional contributions report rejection by both. This paper formalizes a conjecture: human gatekeepers and algorithmic rankers, despite different mechanisms, share a functional bias structure that penalizes distributional outliers, but differ operationally in whether the penalty can be offset by metadata. We model gatekeeping as a threshold decision over a novelty-affiliation-metadata feature space, with logistic acceptance probabilities. Under explicitly labeled illustrative parameters (novelty weight $-1$, metadata weight $2$ for algorithmic versus $0.1$ for human gatekeepers), a one-unit metadata intervention raises an outlier paper's algorithmic acceptance probability from $0.1192$ to $0.5000$ ($\Delta P = 0.3808$) but its human acceptance probability only from $0.1192$ to $0.1301$ ($\Delta P = 0.0109$), an asymmetry ratio of $34.9$; detecting this difference requires roughly $24$ observations per arm at $80\%$ power. We connect the model to documented algorithmic bias in query suggestions, to measured benefits of explanations in human-AI collaboration, and to cognitive-bias literature. The principal contribution is a falsifiable asymmetry metric and a matched-corpus comparison protocol that would establish whether metadata optimization can satisfy algorithmic but not human gatekeeping, with direct consequences for how authors, editors, and platform designers allocate remediation effort.

## 1. Introduction

Interdisciplinary researchers face a double filter. To be read, their work must pass algorithmic gatekeepers: recommendation systems, search rankings, and query suggestions that determine visibility. To be published, funded, or hired, it must pass human gatekeepers: editors, reviewers, and panels. Both filters are reported to penalize work far from the disciplinary mainstream, and the cost is concrete: novel or cross-disciplinary contributions are under-cited, under-funded, and slower to enter the canon, while authors cannot tell whether the obstacle is a ranking rule they can adjust for or a reviewer's judgment they cannot. If the two gatekeeping systems share one outlier-penalizing bias structure but differ in whether metadata interventions can offset it, then authors and institutions are today spending remediation effort on the wrong gate, and platform regulators are auditing a bias that is measurable while the harder bias escapes audit.

The decision that would change if this paper's result holds is the allocation of effort between metadata and framing optimization (which works only against algorithmic gates) and human-process interventions such as explanation, metacognitive debiasing, and review redesign (which are the only lever against the human gate). For platform operators, the result would supply a specific audit target: the metadata sensitivity of the ranker, which is estimable from system data. For editors and funders, it would supply a quantitative warning that transparency remedies proven for algorithms do not transfer to human review.

This paper makes four contributions:

1. A threshold-logistic model of gatekeeping over a novelty-affiliation-metadata feature space, with the human-algorithmic asymmetry expressed as a ratio of metadata sensitivities (Section 3).
2. A fully worked derivation, under labeled illustrative assumptions, of the asymmetry: a metadata intervention that multiplies algorithmic odds by $e^{2} \approx 7.389$ multiplies human odds by $e^{0.1} \approx 1.105$, and shifts acceptance probabilities by $0.3808$ versus $0.0109$, a ratio of $34.9$ (Section 4).
3. A sample-size derivation showing the asymmetry is detectable with approximately $24$ observations per arm in a controlled comparison, so the conjecture is cheaply falsifiable (Section 4).
4. A matched-corpus test protocol specifying what must be measured on the same set of interdisciplinary papers under human review and algorithmic ranking, and which observation would refute the conjecture (Sections 3 and 6).

## 2. Background and Related Work

The conjecture sits at the intersection of algorithmic bias measurement, human cognitive bias, and human-AI collaboration design. We position it against eight bodies of work.

Algorithmic bias in retrieval is measurable with perception-aware metrics. [8] builds a bias detection pipeline for query suggestions and adopts the DCG and nDCG metrics so that bias detection accounts for how suggestions are perceived, integrating rank and frequency of cluster words; applying it to a dataset of German politicians, the pipeline detects a systematic topical gender bias, presenting searches for female politicians with fewer suggestions on lower average ranks associated with politics and economics, and a topical age bias in the same directional pattern. This is the operational meaning of "statistically transparent" bias: the penalty on an out-group is expressible as a rank-and-frequency statistic computed from system outputs. Our model treats exactly this quantity, the metadata-conditioned acceptance probability, as estimable for algorithmic gates and not for human gates.

Human bias in interaction with AI systems is addressed by metacognitive interventions rather than by metadata. [5] identifies anchoring and confirmation bias as human biases arising in human-AI interaction, notes that existing AI literacy tools predominantly focus on algorithmic and systemic bias while lacking interventions that address human biases, and advocates metacognitive AI literacy interventions built on deliberate friction and bi-directional interaction. This supports our framing that the human-side penalty requires a different remediation class: friction and reflection, not metadata.

Explanations change human decisions in measurable ways, which is the mechanism our protocol manipulates on the human arm. [4] proposes the ExAG collaborative image retrieval game and reports that explanations improve human-AI game performance overall: win rate rises from $64.3\%$ without explanations to $69.29\%$ with them, average score improves by $0.95$, with $p = 0.0015$ at $99\%$ confidence; helpfulness-rated-as-excellent explanations improve performance while incorrect ones degrade it, and correct explanations help most when machine predictions are noisy. This measured sensitivity of human gatekeeping-style decisions to the framing and quality of supplied information is precisely the channel through which our human-arm intervention operates, and its modest effect size foreshadows our claim that human metadata sensitivity is small.

Human factors escape automated evaluation. [7] evaluates an LLM-based BPMN modeling copilot with domain experts and argues, drawing on process-model quality literature, that process model quality is multidimensional including pragmatic, human-centered aspects not fully captured by automated metrics; their mixed-methods evaluation surfaces trust and usability themes such as "Intuitive Interface, Opaque Prompting." We use this as precedent for the claim that the human gate's decision function contains components that no documented feature list captures, which is the opacity half of our asymmetry.

The distinction between performed and demonstrated cognition warns against a measurement trap in our protocol. [6] distinguishes performed critical thinking, independent cognitive processes without external assistance, from demonstrated critical thinking, and argues that systems augmenting one are not the same as those augmenting the other, noting that current research often conflates the two. Our human-arm measurements must therefore distinguish a reviewer's independent judgment from judgment rendered after seeing algorithmic scores or metrics, or the two bias structures will be confounded.

The deeper claim that human gatekeeping has a systematic, structured bias, rather than idiosyncratic noise, is supported by the cognitive-bias literature. [9] argues that the human preference for linear models is a cognitive bias for regularity, an efficiency hack encoded in neural architecture, supported by an interlocking structure of cognitive bias, heuristic efficiency, sensory abstraction, and linguistic reification, and that this strategy works efficiently within narrow local bounds but accrues epistemic debt over time. A penalty on distributional outliers is the natural gatekeeping expression of a preference for regularity. [12] supplies the mechanism at the level of representation: cognitive frameworks function as biological data-compression heuristics evolved for survival, pattern recognition excels at identifying familiar configurations and sometimes detects patterns where none exist, and confusing the map with the territory produces categorical errors. Compression heuristics penalize precisely the inputs that compress poorly, i.e., outliers.

On the normative and governance side, [1] analyzes why digital rights that exist in law remain difficult to exercise through information systems, explaining the gap through legal heterogeneity, conflicting incentives, fragmented architectures, and asymmetrical control; the structural analogy is direct: an author's "right" to fair consideration is likewise mediated by systems whose control is asymmetrical. [3] presents the ADPC specification as a shift of data protection from a data-controller-centric to a data-subject-centric practice through standardized communication of preferences and decisions, and concludes that no technology alone is impactful without sociotechnical support; our protocol's human arm is the analogous sociotechnical complement for gatekeeping. [2] analyzes the construct of needs as a conceptual boundary for AI, distinguishing needs from desires and noting that AI developers face social dilemmas with societal good on one side and commercial pressures on the other; ranking systems optimizing engagement sit inside exactly this dilemma, which is one reason their consensus bias is not incidental.

Methodologically, two QNFO works supply templates we follow. [11] formalizes cross-model LLM convergence as Bayesian evidence, reporting under explicitly labeled illustrative assumptions a two-model Bayes factor of $8$ and posterior $\frac{8}{17} \approx 0.471$ from a $0.1$ prior, and states that the framework's value hinges on a single measurable quantity testable by a specified benchmark, with no empirical measurements reported. We adopt the same discipline: illustrative parameters, explicit derivations, and a named measurable quantity whose estimation is the next step. [10] constructs a cross-domain variable dictionary mapping biological branching complexity to quantum circuit width and validates a structural duality with a Monte Carlo simulation, reporting a fractal dimension $\mu \approx 2.51$ and correlation $r \approx 0.98$; its lesson for us is that a claimed structural symmetry between two superficially unrelated systems becomes testable only after an explicit dictionary maps the terms of one domain onto the other. Our Section 3 is such a dictionary between human and algorithmic gatekeeping.

## 3. Methods

### 3.1 Gatekeeping as a threshold decision

A gatekeeper $g$ evaluates an item $i$ described by a feature vector $(x_i, a_i, m_i)$: novelty $x_i \geq 0$ measures distance from the gatekeeper's reference distribution (interdisciplinary or unconventional work has large $x$), affiliation $a_i \in \{0,1\}$ measures insider status, and metadata $m_i \geq 0$ measures optimization effort on documented, machine-readable features (keywords, structured abstracts, citation-graph positioning, compliance signals). The gatekeeper computes a score

$$s_i = w_x x_i + w_a a_i + w_m m_i - \theta$$

and accepts when $s_i > 0$. Acceptance probability is logistic:

$$P_g(\text{accept} \mid x_i, a_i, m_i) = \sigma(w_x x_i + w_a a_i + w_m m_i - \theta), \qquad \sigma(u) = \frac{1}{1 + e^{-u}}.$$

The two gatekeeper classes are distinguished only by their parameter vectors:

- **Algorithmic gatekeeper** ($g = A$): $w_m^{(A)}$ is large and estimable from system data; the full feature list is documented or discoverable by probing.
- **Human gatekeeper** ($g = H$): $w_m^{(H)}$ is small; the feature list includes undocumented components (personal taste, network position) that no metadata can move.

Both classes share the structural penalty: $w_x < 0$ for both, so novelty lowers the score. The conjecture's operational content is the pair of claims $w_m^{(A)} \gg w_m^{(H)} \approx 0$ and $w_x^{(A)} \approx w_x^{(H)} < 0$.

### 3.2 The asymmetry metric

Define the metadata sensitivity of gatekeeper $g$ as the odds multiplier per unit of metadata effort:

$$\Lambda_g = \frac{P_g(\text{accept} \mid m+1) / (1 - P_g(\text{accept} \mid m+1))}{P_g(\text{accept} \mid m) / (1 - P_g(\text{accept} \mid m))} = e^{w_m^{(g)}}.$$

The **asymmetry ratio** is

$$R = \frac{\Lambda_A}{\Lambda_H} = e^{w_m^{(A)} - w_m^{(H)}}.$$

The conjecture predicts $R \gg 1$; its refutation is $R \approx 1$. Because $R$ depends only on the difference $w_m^{(A)} - w_m^{(H)}$, it is identifiable from a matched intervention experiment without knowing either weight separately.

### 3.3 Matched-corpus protocol

On a single corpus of interdisciplinary papers, run two arms: (i) papers submitted to venues or panels with a metadata-optimization intervention applied to a randomized half, and (ii) the same corpus scored by the algorithmic gate (recommendation or ranking system) with the same intervention applied to a randomized half. Estimate $\Delta P_g = P_g(\text{accept} \mid m+1) - P_g(\text{accept} \mid m)$ in each arm and test $H_0: \Delta P_A = \Delta P_H$. The human arm must measure performed judgment: reviewers who have not seen algorithmic scores or quality metrics before deciding, per the performed-versus-demonstrated distinction of [6]. Following the mixed-methods precedent of [7], the human arm additionally collects trust and framing data, since [4] shows human decisions respond to explanation quality, which is a confound to be randomized rather than removed.

### 3.4 Illustrative parameterization

All numerical results below derive from one labeled illustrative parameter set, chosen to be plausible but not measured:

$$w_x = -1, \quad w_a = 1, \quad \theta = 0, \quad w_m^{(A)} = 2, \quad w_m^{(H)} = 0.1,$$

with a baseline outlier paper at $(x, a, m) = (2, 0, 0)$ and an intervention of one metadata unit, $\Delta m = 1$. Every number in Section 4 follows from these inputs by arithmetic alone; none is an empirical measurement.

## 4. Analysis

### 4.1 Baseline acceptance of the outlier

Inputs (Section 3.4): $w_x = -1$, $x = 2$, $w_a = 1$, $a = 0$, $m = 0$, $\theta = 0$.

$$s_0 = (-1)(2) + (1)(0) + 0 - 0 = -2.$$

$$P_0 = \sigma(-2) = \frac{1}{1 + e^{2}} = \frac{1}{1 + 7.389056} = \frac{1}{8.389056} = 0.119203.$$

Both gatekeeper classes share this baseline because the baseline metadata weight does not enter at $m = 0$.

For contrast, a mainstream insider paper at $(x, a) = (0, 1)$ scores $s = 1$ and is accepted with probability $\sigma(1) = \frac{1}{1 + e^{-1}} = \frac{1}{1.367879} = 0.731059$. The novelty-affiliation penalty structure alone therefore produces a $0.731059 / 0.119203 \approx 6.13$-fold acceptance gap between mainstream and outlier work before any metadata effect, which is the shared outlier penalty the conjecture posits.

### 4.2 Effect of the metadata intervention on each gate

The intervention raises $m$ from $0$ to $1$. Algorithmic gate:

$$s_A = (-1)(2) + 0 + (2)(1) = 0, \qquad P_A = \sigma(0) = 0.5.$$

$$\Delta P_A = 0.5 - 0.119203 = 0.380797.$$

Human gate:

$$s_H = (-1)(2) + 0 + (0.1)(1) = -1.9, \qquad P_H = \sigma(-1.9) = \frac{1}{1 + e^{1.9}} = \frac{1}{1 + 6.685894} = \frac{1}{7.685894} = 0.130105.$$

$$\Delta P_H = 0.130105 - 0.119203 = 0.010902.$$

### 4.3 Odds multipliers and the asymmetry ratio

$$\Lambda_A = e^{w_m^{(A)}} = e^{2} = 7.389056, \qquad \Lambda_H = e^{w_m^{(H)}} = e^{0.1} = 1.105171.$$

$$R = \frac{\Lambda_A}{\Lambda_H} = e^{2 - 0.1} = e^{1.9} = 6.685894.$$

In probability terms the asymmetry is larger because the logistic saturates:

$$\frac{\Delta P_A}{\Delta P_H} = \frac{0.380797}{0.010902} = 34.93.$$

Under this parameterization, one unit of metadata effort buys the outlier author a $34.9$-fold larger acceptance-probability gain at the algorithmic gate than at the human gate, even though both gates penalize the outlier identically at baseline. This is the paper's central quantitative claim, and it is a consequence of the assumed weights, not a measurement.

### 4.4 Detectability: sample size for the asymmetry test

The protocol tests $H_0: \Delta P_A = \Delta P_H$ against the observed proportions $p_1 = 0.5$ (algorithmic arm, intervention) and $p_2 = 0.130105$ (human arm, intervention). With $\alpha = 0.05$ two-sided ($z_{\alpha/2} = 1.96$) and power $0.8$ ($z_\beta = 0.8416$), the per-arm sample size for a two-proportion comparison is

$$n = \frac{\left( z_{\alpha/2} \sqrt{2 \bar{p}(1 - \bar{p})} + z_\beta \sqrt{p_1(1-p_1) + p_2(1-p_2)} \right)^2}{(p_1 - p_2)^2},$$

where $\bar{p} = (p_1 + p_2)/2$. Step by step:

$$\bar{p} = \frac{0.5 + 0.130105}{2} = 0.315053.$$

$$2 \bar{p}(1 - \bar{p}) = 2 (0.315053)(0.684947) = 0.431583, \qquad \sqrt{0.431583} = 0.656950.$$

$$z_{\alpha/2} \sqrt{2\bar{p}(1-\bar{p})} = 1.96 \times 0.656950 = 1.287622.$$

$$p_1(1-p_1) = 0.25, \qquad p_2(1-p_2) = (0.130105)(0.869895) = 0.113177.$$

$$p_1(1-p_1) + p_2(1-p_2) = 0.363177, \qquad \sqrt{0.363177} = 0.602642.$$

$$z_\beta \sqrt{p_1(1-p_1)+p_2(1-p_2)} = 0.8416 \times 0.602642 = 0.507184.$$

$$n = \frac{(1.287622 + 0.507184)^2}{(0.5 - 0.130105)^2} = \frac{(1.794806)^2}{(0.369895)^2} = \frac{3.221329}{0.136822} = 23.54.$$

Rounding up, $n = 24$ items per arm suffices to detect the illustrative asymmetry at $80\%$ power. The conjecture is therefore falsifiable with a modest controlled study, not a large-scale data collection effort.

### 4.5 Sensitivity of $R$ to the human metadata weight

$R = e^{w_m^{(A)} - w_m^{(H)}}$ depends exponentially on the weight difference. If the human gate were as metadata-sensitive as assumed for the algorithm ($w_m^{(H)} = 2$), then $R = e^{0} = 1$ and the conjecture fails. If the human weight is $0.5$ rather than $0.1$, $R = e^{1.5} = 4.481689$; if it is $0$, $R = e^{2} = 7.389056$. The result is robust in direction across any $w_m^{(H)} < 1$ but its magnitude is exponentially sensitive to that weight, which is why Section 3.3 makes estimating $w_m^{(H)}$ the protocol's primary measurement target.

## 5. Results

All numbers below are computed in Section 4 from the labeled illustrative assumptions of Section 3.4; no empirical measurements are reported.

1. **Shared baseline penalty.** The outlier paper $(x,a) = (2,0)$ is accepted with probability $0.119203$ by both gate classes, versus $0.731059$ for a mainstream insider paper $(0,1)$: a $6.13$-fold baseline gap produced by the shared novelty-affiliation structure alone.
2. **Algorithmic arm.** One unit of metadata effort raises algorithmic acceptance from $0.119203$ to $0.500000$; $\Delta P_A = 0.380797$; odds multiplier $\Lambda_A = e^{2} = 7.389056$.
3. **Human arm.** The same intervention raises human acceptance from $0.119203$ to $0.130105$; $\Delta P_H = 0.010902$; odds multiplier $\Lambda_H = e^{0.1} = 1.105171$.
4. **Asymmetry.** The odds-level asymmetry ratio is $R = e^{1.9} = 6.685894$; the probability-level ratio of intervention gains is $\Delta P_A / \Delta P_H = 34.93$.
5. **Detectability.** A two-proportion test at $\alpha = 0.05$, power $0.8$, requires $n = 24$ items per arm to detect the illustrative asymmetry.
6. **Sensitivity.** $R$ ranges from $e^{2} = 7.389056$ (human weight $0$) through $e^{1.5} = 4.481689$ (human weight $0.5$) to $R = 1$ (human weight $2$); the conjecture's direction holds for any $w_m^{(H)} < 1$ under the assumed algorithmic weight.

## 6. Discussion

The central result is a ratio of two sensitivities, and every limitation follows from how it is identified.

**Limitations.**

- **Every weight is an assumption.** $w_x = -1$, $w_m^{(A)} = 2$, $w_m^{(H)} = 0.1$ are illustrative, not measured; the framework's value stands or falls on empirical estimates of $w_m^{(H)}$ from the protocol of Section 3.3. The magnitude $R = 6.69$ is exponentially sensitive to $w_m^{(H)}$ (Section 4.5); if the true human weight is above $1$, the asymmetry inverts.
- **The logistic form is an assumption.** Real review processes have discreteness (accept/reject/revise), committee effects, and interactions between reviewers that a single logistic score does not capture. A committee of reviewers with correlated novelty penalties could produce effective human behavior more extreme than any individual logistic.
- **Opacity is partly endogenous.** The claim that human bias is "opaque" is operationalized as a small $w_m^{(H)}$, but opacity also reflects measurement difficulty: human features (reviewer identity, network position) may be metadata-like but unrecorded. If they were recorded, the human gate might look as transparent as the algorithmic one, and the asymmetry would shrink to an artifact of what we choose to count as metadata.
- **The two arms are not independent of the algorithm.** Reviewers increasingly see algorithmic scores and metrics; if the human arm's judgments are contaminated by algorithmic input, the measured $w_m^{(H)}$ absorbs algorithmic sensitivity and the asymmetry is underestimated. The performed-judgment requirement of Section 3.3, following [6], mitigates but cannot eliminate this.
- **The baseline penalty may differ across gates.** The model assumes $w_x^{(A)} = w_x^{(H)}$; if human novelty penalties are stronger, part of the observed baseline gap is human-specific and metadata remedies help even less than derived, strengthening the practical conclusion but weakening the "shared structure" claim.

**What would falsify the main result.** The single decisive observation is a matched intervention experiment in which the acceptance-probability gain from metadata optimization at the human gate is not statistically distinguishable from the gain at the algorithmic gate, i.e., an estimated $R$ whose confidence interval includes $1$. A secondary falsifier is the reverse asymmetry: if metadata optimization raises human acceptance more than algorithmic acceptance, the conjecture's operational claim is backwards. Under the illustrative numbers, an observed $\Delta P_H$ above roughly $0.38$ at $n = 24$ per arm would produce such a failure to reject.

**Open questions.** Whether $w_x$ is genuinely shared across gates, whether the asymmetry persists for gatekeepers who know the metadata is optimized (gaming detection may make algorithmic gates penalize optimization itself), and whether explanation-based human interventions in the style of [4] can raise $w_m^{(H)}$ without simply importing algorithmic preferences into human judgment are all unresolved. There is also a normative question the model raises but does not answer: if metadata optimization can satisfy the algorithmic gate, authors face an incentive to optimize visibility signals rather than content, and whether that is a defect of the gate or a rational response to it is outside this paper's scope.

## 7. Practical Implications and Engineering Pathways

**(a) Users and changed decisions.** Three user groups can act on the result if it holds. Interdisciplinary authors and their institutions would reallocate effort: metadata and framing optimization is worth pursuing for algorithmic visibility but is derived here to buy a $34.9$-fold smaller acceptance gain at human gates, so effort should shift toward human-process channels (pre-submission inquiry, explanation quality, reviewer-facing framing). Editors and funders would treat metadata-driven improvements in submission quality as an algorithmic-gate effect and would not expect them to transfer to review outcomes. Platform operators and auditors would gain a specific, estimable audit target, the ranker's metadata sensitivity $w_m^{(A)}$, of the kind the perception-aware bias metrics of [8] already make computable for query suggestions. Because the present paper reports no empirical measurement, its immediate use is as a design hypothesis for these groups rather than a validated rule.

**(b) Readiness.** This is purely analytical work that has not been peer reviewed: by the NASA Technology Readiness Level definitions it sits at TRL 1-2 (basic principles observed and reported; concept formulated). Analytical work never exceeds TRL 3; no experimental validation exists and none is claimed.

**(c) Smallest next test.** The minimal de-risking experiment is the two-arm matched intervention of Section 3.3 at the derived scale: approximately $24$ interdisciplinary papers per arm, one metadata-optimization treatment, acceptance recorded at one human gate (performed judgment, no metric exposure) and one algorithmic gate. The outcome that refutes the conjecture is a failure to reject $\Delta P_A = \Delta P_H$; the outcome that confirms it is $\Delta P_A > \Delta P_H$ with the confidence interval on $R = e^{w_m^{(A)} - w_m^{(H)}}$ excluding $1$. A cheaper precursor is a retrospective estimate of $w_m^{(H)}$ from historical review data with recorded metadata variation, which requires no new intervention.

**(d) Binding constraints.** The first binding constraint is data access: estimating $w_m^{(H)}$ requires review outcomes paired with metadata variation, which venues rarely release; IRB and confidentiality constraints on reviewer identities bind before any modeling does. The second is contamination control: ensuring reviewers have not seen algorithmic scores requires process changes at the venue, not just analysis. The third is treatment fidelity: "one unit of metadata effort" must be operationalized identically across arms, or $R$ is not identifiable. Whether a sufficient corpus of interdisciplinary papers with randomized metadata variation exists at all is an open question the protocol cannot answer from this paper's analysis.

