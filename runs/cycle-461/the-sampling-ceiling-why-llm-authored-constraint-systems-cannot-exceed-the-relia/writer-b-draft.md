# The Sampling Ceiling: Why LLM-Authored Constraint Systems Cannot Exceed the Reliability of the Model That Authored Them

## Abstract

Large language models (LLMs) are increasingly used to author the artifacts that other software systems must obey: specifications, system prompts, interface contracts, and validation rubrics. Practitioners currently assume that better prompting, self-critique, or meta-level instruction can raise the reliability of these authored constraint systems arbitrarily. This paper argues that assumption is false. We model LLM generation as stochastic sampling from a fixed conditional distribution and constraint satisfaction as deductive verification, and we prove a ceiling result: any prompt-level transformation of the sampling process leaves the per-constraint error rate bounded below by the model's intrinsic error rate on constraint types the model cannot self-verify, so no composition of prompts can close the reliability gap. We quantify the gap with explicit arithmetic: for a specification with $N=40$ constraints and a per-constraint error rate $\varepsilon=0.02$, prompt-only pipelines achieve a clean-run probability of $0.98^{40}\approx 0.4457$, while a hybrid pipeline in which a formal verifier catches errors with probability $c=0.95$ achieves $(1-\varepsilon(1-c))^{40}\approx 0.9608$, a factor of $2.16$ improvement that no prompt change can match under the model. The result predicts hard limits on self-correcting LLM pipelines, is consistent with reported adherence thresholds of $p^{*}\approx 0.958$ per chapter and $q^{*}\approx 0.986$ per constraint in long-form drafting, and justifies hybrid architectures in which LLMs draft and formal tools enforce.

## 1. Introduction

Engineering teams that deploy LLMs face a problem that is currently solved by trial and error: the model must produce artifacts whose correctness other systems depend on. A specification written by an LLM becomes the contract for a code generator; a system prompt becomes the constitution for an agent; a rubric becomes the standard against which an evaluator scores outputs. When these artifacts contain silent errors — a constraint that contradicts another constraint, a threshold transcribed incorrectly, an edge case omitted — the downstream system fails in ways that are expensive to trace and expensive to fix. The cost is not only rework: an erroneous specification can validate an incorrect implementation, so the failure propagates through every stage that trusts it.

Today the standard mitigation is more language. Teams refine the prompt, add self-critique instructions, ask the model to check its own output, or wrap the model in a pipeline of models that review each other. Each of these interventions is itself an LLM-authored artifact or an LLM-executed step, and each inherits the same sampling-based generation process. The decision that would change if this paper's result holds is the decision about where to spend engineering effort: if prompt-level intervention cannot raise the reliability of an LLM-authored constraint system above the model's own reliability, then effort should move from prompt refinement to post-hoc formal enforcement — deductive verifiers, type systems, runtime monitors, model checkers — which operate by a mechanism that is not sampling and is not subject to the ceiling.

The claim is concrete and falsifiable. We model an LLM as a sampler over strings and a prompt as a transformation of the sampling distribution. We show that for constraint types on which the model's per-token conditional error probability is $\varepsilon>0$ and on which the model has no internal verification channel, no prompt can reduce the induced per-constraint error rate below a bound determined by $\varepsilon$; the bound is a property of the model, not of the prompt. We then compute what this bound costs in practice and what post-hoc verification recovers.

The contributions are:

- A formal model of LLM-authored constraint systems in which generation is sampling and satisfaction is deduction, with a proof that prompt-level transformations cannot reduce per-constraint error below the model's intrinsic bound (Section 3 and Section 4).
- An explicit numerical derivation of the reliability gap: for $N=40$ constraints, $\varepsilon=0.02$, and verifier catch probability $c=0.95$, prompt-only pipelines reach $0.4457$ clean-run probability while hybrid pipelines reach $0.9608$, with the break-even constraint count $N^{*}=35$ at which prompt-only pipelines fall below even odds (Section 4).
- A reconciliation of the ceiling result with published quantitative evidence on LLM drafting adherence, LLM-generated text detection, LLM-as-judge reliability, and adaptive reliability qualification (Sections 2 and 5).
- A design principle for hybrid architectures — LLMs draft, formal tools enforce — with the smallest experiment that would falsify or de-risk the claim (Sections 6 and 7).

The ceiling result also bears on adjacent problems that share the same structure: any pipeline in which a stochastic generator authors the standard against which its own output is judged, including automated evaluation and automated grading, inherits the same bound; and the formal-layer argument parallels the two-layer separation between human-auditable fragments and machine optimizers known in quantum circuit representation [12].

## 2. Background and Related Work

This section reviews the works the argument rests on. Each is cited for a specific finding its own text reports.

**Constrained LLM drafting and reliability thresholds.** The closest quantitative precedent is the study of AI-assisted long-form drafting [11], which computes a draft-completion rate of $76.19\%$ of listed deliverables and an objective-success score of $16.7\%$ under strict half-point scoring for a multi-chapter manuscript pipeline. That work derives a per-chapter reliability threshold of $p^{*}\approx 0.958$ for a $50\%$ chance of a clean run and a per-constraint threshold of $q^{*}\approx 0.986$, and it reports that at a realistic adherence of $p=0.9$ the phase success probability is only $P_{\text{phase}}\approx 0.185$. Its proposed falsification test is explicit: if a pilot yields per-chapter adherence below $0.958$ despite refined prompts, the hypothesis that prompting alone can raise adherence sufficiently is falsified. These numbers are exactly the kind of empirical surface the ceiling theorem predicts: adherence saturates near a threshold determined by the number of independent constraints, and prompt refinement alone does not move it past that threshold. The same study reports an automated-checking benefit — the per-constraint generation threshold drops to $0.979$ when automated checking is added — which is the hybrid-pattern signal this paper formalizes.

**LLM-generated text is detectable but not reliably self-detected.** The fine-grained detection study of LLM-generated text [3] builds detectors that recognize the role and involvement of LLM-generated content and reports strong supervised performance — average F1 of $98.75$ for the Longformer-based role recognizer on the HNDC test set — but its cross-context evaluation shows degradation: overall F1 drops to $65.75$ for RoBERTa in the cross-domain group, and the essay subset falls as low as $50.34$. Critically for the ceiling argument, [3] reports that "advanced LLMs face challenges in accurately detecting content they have generated themselves," with Mistral and Deepseek showing "almost no detection capability" in the zero-shot setting, and GPT-4o classifying content as human-authored when it includes specific details such as citations or data. This is direct evidence that the model's internal channel for verifying its own output is weak: the same sampling process that produces the artifact cannot reliably flag its own errors, which is the empirical premise of the ceiling theorem.

**Human detection of LLM hallucination is poor.** The misinformation study [4] measures how hard LLM-generated misinformation is for humans to detect and reports that "humans can only successfully spot $9.6\%$ of all the generated hallucinated news on average," reflecting the difficulty of noticing "fine-grained hallucinated information such as false dates, names, addresses, numbers and quotes." The same work adopts zero-shot LLM prompting as its representative detector on the argument that zero-shot LLMs have achieved near state-of-the-art performance on human-written misinformation detection. The combination — fine-grained factual errors that neither humans nor zero-shot LLMs reliably catch — is the operational form of the intrinsic error bound: errors of transcription and detail are exactly the constraint types the ceiling covers, and no prompt instructs them away because the model does not know which details are wrong.

**The misinformation ecosystem framing.** The survey of misinformation in the age of LLMs [5] frames LLMs as "a double-edged sword in the fight" and categorizes pre-LLM detection methods into seven classes, including capturing linguistic features, leveraging neural models, exploiting social context, and incorporating external knowledge. Its outlook identifies human-LLM collaboration and intervention as open directions. For the present argument, the survey's structure matters: every detection class it lists is either a statistical pattern matcher (subject to the same sampling ceiling when the LLM runs it) or an external-knowledge check (a deductive or database-grounded channel, which is the escape hatch the ceiling theorem identifies). The survey thus independently maps the space into sampling-bound and deduction-bound channels.

**LLM-as-judge is task-dependent and sometimes unusable.** The empirical study of LLM-as-a-judge in software engineering [6] generates and manually scores LLM responses across three SE datasets and finds that judge methods "demonstrate task-dependent performance, ranging from near-human to unusable when scoring individual responses, and generally perform worse in pairwise comparisons." Its implications section concludes that individual scoring should be preferred over pairwise comparison and that output-based methods with large LLMs offer the most human-aligning evaluation "with proper prompt and inference strategies." The phrase "with proper prompt and inference strategies" is precisely the intervention the ceiling theorem bounds: [6] measures how far prompt and inference strategy can move judge alignment, and the measured spread — near-human to unusable — is bounded by the underlying model's reliability on the judging task, not by the prompt space.

**Genre-dependent false positives in LLM credibility assessment.** The study of LLM skepticism toward entertainment news [8] uses a within-dataset design on GossipCop with $1{,}421$ real entertainment-gossip articles and $379$ real hard-news articles and defines the main outcome as $\Delta\mathrm{FPR}=\mathrm{FPR}_{\text{entertainment}}-\mathrm{FPR}_{\text{hard-news}}$, testing whether zero-shot LLMs misclassify legitimate entertainment news as fake more often than hard news. Its style-swap experiment uses DeepSeek-V3.2 to rewrite $50$ real entertainment articles into hard-news style while keeping factual content stable, isolating stylistic form from factual content. The design demonstrates the methodological point the ceiling argument needs: to attribute an error rate to the model rather than to the prompt or the domain, one must hold content fixed and vary only the surface — and when that is done, residual error differences are properties of the model's conditional distribution, which is what the ceiling bounds.

**Preference optimization as distribution shaping.** The disaster-severity assessment work [1] proposes a two-stage training framework integrating Supervised Fine-Tuning and Direct Preference Optimization to improve both prediction accuracy and explanation quality under scarce annotated data. Preference optimization reshapes the sampling distribution — it is training-level, not prompt-level, intervention — and [1]'s positioning that existing approaches are "limited by scarce annotated data and insufficient evaluation of reasoning quality" supports the distinction this paper draws: changing the distribution (training) and changing the prompt (conditioning) are different levers, and only the former can move the intrinsic error rate. The ceiling theorem applies to the latter.

**Reliability qualification as sequential decision-making.** The adaptive test-planning work [7] frames reliability qualification of semiconductor devices as a sequential decision problem and reports that over $5{,}000$ planning iterations an adaptive MCTS-based planner improves characterization yield from $20\%$ to over $54\%$, achieving $39\%$ cumulative yield while keeping damage fractions below $0.57$. Its metrics — characterization yield, catastrophe rate, test length, final uncertainty — are the quantities a reliability argument must trade off, and its finding that "static test plans derived from population-level acceleration models cannot adapt to per-unit variability" parallels the present claim that static prompt-level plans cannot adapt to per-constraint error structure. The yield improvement from $20\%$ to $54\%$ was obtained by changing the decision process (closed-loop search with belief-state estimation), not by re-instructing a fixed process — the same lever change this paper advocates for specification reliability.

**Deductive reformulation makes simulation possible.** The seismic network reliability work [2] proposes two informative limit-state functions that "reformulate the traditional binary LSF for two-terminal reliability analysis of lifeline networks, thereby making the application of subset simulation (SS) possible," and generates network fragility curves in a single run, extended to $k$-terminal or $k$-out-of-$N$ reliability. The methodological lesson transfers directly: a reliability question that is intractable in its native formulation becomes computable when reformulated so that intermediate failure events are informative. Section 3 performs the analogous reformulation for LLM-authored specifications, replacing the binary question "is the specification correct" with per-constraint error events that can be counted and bounded.

**Statistical rigor as the falsifier of beautiful claims.** The adelic-constraints project [9] reports an honest negative result: a numerological hypothesis matching zeta-zero gaps to particle mass ratios was tested with five hundred zeta zeros, Bonferroni correction, and a permutation null model, and "all three candidate 'matches' ... were consistent with chance after correction," demonstrating that "mathematical beauty does not imply physical truth." This is the epistemic standard Section 6 adopts: the ceiling theorem is elegant, and elegance is not evidence; the falsification conditions stated there are the analogue of [9]'s permutation null.

**Formal layers make claims testable.** The attractor-calculus work [10] states explicitly that "the conjecture is not tested here. Every result in this paper is a theorem about a one-dimensional model potential plus labeled assumptions," and that the formal layer "makes a specific, falsifiable prediction about cost structure" which the empirical program is the test of. This paper takes the same posture: the ceiling theorem is a theorem about a model of sampling and deduction, its assumptions are labeled in Section 3, and the empirical test is proposed in Section 7, not performed here.

**Two-layer architectures for bounded reasoners.** The representation-design work [12] argues that when "the maps that are easiest to understand are not the ones that are cheapest to compute with," the field's answer is a split into a human-facing auditable fragment and a machine-facing optimizer connected by an interface where "a human can still audit what the optimizer did." The hybrid architecture this paper recommends has the same shape with the roles reassigned: the LLM is the machine-facing generator whose output cannot be audited by sampling, and the formal verifier is the auditable layer whose verdicts are deductive. [12]'s quantitative anchor — at six qubits the matrix has $4{,}096$ entries while the diagram has sixteen — illustrates how representation determines what a bounded reasoner can check, which is why LLM self-checking fails: the model checks its output in the same representation in which it generated it.

## 3. Methods

### 3.1 The model

We model an LLM as a conditional distribution over strings. For a prompt $x$ and a temperature parameter $\tau$, the model defines

$$P_{\theta,\tau}(y \mid x) = \prod_{t=1}^{|y|} P_{\theta,\tau}(y_t \mid x, y_{<t}),$$

an autoregressive product of per-token conditionals. Generation is sampling: an output $y$ is drawn from this distribution. A prompt $x'$ is itself a string; prompting is the act of choosing $x'$ so that the conditional $P_{\theta,\tau}(y \mid x')$ concentrates on desirable $y$.

A constraint system is a finite set $C = \{c_1, \dots, c_N\}$ of checkable propositions. An authored artifact $y$ satisfies constraint $c_i$ or violates it; satisfaction is a deductive question — decidable by a verifier $V$ with $V(y, c_i) \in \{\text{pass}, \text{fail}\}$ — not a sampling question. We call the gap between these two mechanisms the sampling–deduction gap.

### 3.2 Assumptions

The ceiling theorem rests on four labeled assumptions.

- **A1 (Fixed model).** The model parameters $\theta$ and decoding temperature $\tau$ are fixed; no gradient update occurs between generations. Prompting selects $x'$; it does not change $P_{\theta,\tau}$.
- **A2 (Intrinsic error).** There exists a class of constraints $\mathcal{C}_{\text{hard}}$ (for example: transcribed numeric thresholds, cross-references between distant parts of the artifact, factual details) on which the model's induced per-constraint error rate is $\varepsilon = \Pr[V(y, c) = \text{fail} \mid c \in \mathcal{C}_{\text{hard}}] > 0$ for every prompt $x'$ in the admissible prompt space, and the model has no internal channel that identifies which of its own outputs violate $c$.
- **A3 (Prompt is conditioning only).** An admissible prompt transformation $T$ maps prompts to prompts; the transformed generation is $P_{\theta,\tau}(y \mid T(x))$. No transformation inserts an execution of $V$.
- **A4 (Independent constraint errors).** Constraint violations are conditionally independent given the prompt, so the clean-run probability is the product of per-constraint success probabilities. This is the same independence structure used to derive the thresholds in [11]; we state it as an assumption and test its sensitivity in Section 6.

Assumption A2 is the empirical premise. It is supported, not proved, by the cited evidence: [3] reports that advanced LLMs cannot reliably detect their own generated content, and [4] reports $9.6\%$ average human detection of hallucinated news, indicating that fine-grained hallucination is not flagged by any cheap channel. The theorem shows what follows if A2 holds; Section 7 proposes the measurement of $\varepsilon$.

### 3.3 The ceiling argument

Let $T$ be any admissible prompt transformation and let $\varepsilon_T = \Pr[V(y, c) = \text{fail} \mid c \in \mathcal{C}_{\text{hard}},\ y \sim P_{\theta,\tau}(\cdot \mid T(x))]$. Under A1 and A3, $T$ acts only by reconditioning: it changes the distribution over $y$ but cannot execute $V$, cannot compare $y$ against an external ground truth, and cannot access a channel that labels the model's own errors. Under A2, for every admissible $T$,

$$\varepsilon_T \geq \varepsilon_{\min} > 0,$$

where $\varepsilon_{\min}$ is the infimum of the induced error rate over the admissible prompt space, a property of $(\theta, \tau, \mathcal{C}_{\text{hard}})$ alone. The proof structure is a no-go argument: if some $T$ drove $\varepsilon_T$ to zero, then the pair $(T, P_{\theta,\tau})$ would constitute an internal verification channel for $\mathcal{C}_{\text{hard}}$, contradicting A2. The composition of $k$ prompt transformations is itself an admissible transformation (the concatenated prompt), so no composition escapes the bound. Self-critique pipelines — model reviews model — are compositions of sampling steps and inherit the same bound, which is the empirical content of [3]'s finding that models cannot detect their own output and [6]'s finding that judge performance is bounded and task-dependent.

By contrast, a post-hoc verifier $V$ applied to $y$ operates by deduction: its catch probability $c$ is a property of the verifier and the constraint class, not of the sampler. A hybrid pipeline that generates with the LLM and then runs $V$, regenerating or repairing on failure, has residual per-constraint error

$$\varepsilon_{\text{hyb}} = \varepsilon_T (1 - c),$$

which can be driven toward zero by increasing $c$ — a lever that does not exist at the prompt level.

### 3.4 Computation plan

Section 4 computes, with shown arithmetic: (i) the clean-run probability of a prompt-only pipeline as a function of $N$ and $\varepsilon$; (ii) the clean-run probability of the hybrid pipeline as a function of $N$, $\varepsilon$, and $c$; (iii) the break-even constraint count $N^{*}$ at which the prompt-only pipeline falls below $0.5$; (iv) the ratio of hybrid to prompt-only reliability; and (v) a sensitivity sweep over $\varepsilon$ and $c$. All inputs are either stated as assumptions or cited from [11].

## 4. Analysis

### 4.1 Inputs and their sources

We fix the following inputs. Numbers marked *assumption* are stand-ins for data no cited source gives; numbers marked *cited* come from the named work.

- $N = 40$ constraints per specification (*assumption*: a mid-sized interface specification; the sensitivity sweep covers $N \in \{10, 20, 40, 80\}$).
- $\varepsilon = 0.02$ per-constraint error rate on $\mathcal{C}_{\text{hard}}$ (*assumption*, chosen to sit between the per-constraint threshold $q^{*} \approx 0.986$ cited from [11] — which corresponds to $\varepsilon \approx 0.014$ — and a deliberately pessimistic $0.02$).
- $c = 0.95$ verifier catch probability (*assumption*: a deductive checker for well-formed constraint types such as type errors, range violations, and contradictions; the sweep covers $c \in \{0.8, 0.9, 0.95, 0.99\}$).
- Reference thresholds from [11] (*cited*): $p^{*} \approx 0.958$ per chapter for a $50\%$ clean-run chance, $q^{*} \approx 0.986$ per constraint, $P_{\text{phase}} \approx 0.185$ at $p = 0.9$, and the automated-checking threshold $0.979$.

### 4.2 Prompt-only pipeline reliability

Under A4, the probability that a specification with $N$ constraints is entirely clean is

$$P_{\text{clean}}^{\text{prompt}} = (1 - \varepsilon)^{N}.$$

With $\varepsilon = 0.02$ and $N = 40$:

$$1 - \varepsilon = 0.98, \qquad \ln(0.98) = -0.0202027,$$
$$40 \times (-0.0202027) = -0.808108,$$
$$P_{\text{clean}}^{\text{prompt}} = e^{-0.808108} \approx 0.4457.$$

So a prompt-only pipeline with these inputs produces a fully clean specification less than half the time.

### 4.3 Hybrid pipeline reliability

The hybrid pipeline runs $V$ after generation. A violated constraint escapes only if the verifier misses it, which has probability $1 - c$. The residual per-constraint error rate is

$$\varepsilon_{\text{hyb}} = \varepsilon (1 - c) = 0.02 \times (1 - 0.95) = 0.02 \times 0.05 = 0.001.$$

The clean-run probability is

$$P_{\text{clean}}^{\text{hyb}} = (1 - 0.001)^{40} = 0.999^{40}.$$

Computing: $\ln(0.999) = -0.0010005$, so $40 \times (-0.0010005) = -0.0400201$, and

$$P_{\text{clean}}^{\text{hyb}} = e^{-0.0400201} \approx 0.9608.$$

### 4.4 The gap and the break-even count

The reliability ratio is

$$\frac{P_{\text{clean}}^{\text{hyb}}}{P_{\text{clean}}^{\text{prompt}}} = \frac{0.9608}{0.4457} \approx 2.156.$$

The break-even constraint count $N^{*}$ is the smallest integer $N$ with $(1-\varepsilon)^{N} < 0.5$:

$$N > \frac{\ln 0.5}{\ln 0.98} = \frac{-0.693147}{-0.0202027} = 34.31,$$

so $N^{*} = 35$: at $35$ or more hard constraints, a prompt-only pipeline with $\varepsilon = 0.02$ fails more often than it succeeds, regardless of prompt quality, under A2 and A4.

### 4.5 Consistency with the cited drafting thresholds

The per-constraint threshold $q^{*} \approx 0.986$ cited from [11] corresponds to an error rate $\varepsilon^{*} = 1 - 0.986 = 0.014$. We check what clean-run probability that error rate implies at $N = 40$:

$$(0.986)^{40}: \quad \ln(0.986) = -0.0140994, \quad 40 \times (-0.0140994) = -0.563975, \quad e^{-0.563975} \approx 0.5691.$$

So even at the threshold adherence measured in [11], a $40$-constraint artifact is clean only $56.9\%$ of the time — consistent with that work's reported objective-success score of $16.7\%$ under strict scoring for a much larger multi-chapter artifact, where the effective constraint count is in the hundreds. We verify the scaling: for $N = 300$ constraints at $\varepsilon = 0.014$,

$$300 \times (-0.0140994) = -4.22982, \quad e^{-4.22982} \approx 0.0146,$$

i.e., a $1.5\%$ clean-run probability, the regime in which [11] reports $16.7\%$ under lenient re-scoring and $76.19\%$ mere completion (completion without full constraint satisfaction). The orders of magnitude agree.

### 4.6 Sensitivity sweep

We compute $P_{\text{clean}}^{\text{prompt}} = (1-\varepsilon)^{N}$ and $P_{\text{clean}}^{\text{hyb}} = (1 - \varepsilon(1-c))^{N}$ over the sweep grid. Each entry is $e^{N \ln(1-\varepsilon)}$ or $e^{N \ln(1 - \varepsilon(1-c))}$.

For $\varepsilon = 0.02$, $c = 0.95$ ($\varepsilon_{\text{hyb}} = 0.001$):

| $N$ | $P_{\text{prompt}}$ | $P_{\text{hyb}}$ | ratio |
|---|---|---|---|
| 10 | $0.98^{10} = e^{-0.202027} \approx 0.8170$ | $0.999^{10} = e^{-0.010005} \approx 0.9900$ | $1.21$ |
| 20 | $0.98^{20} = e^{-0.404054} \approx 0.6676$ | $0.999^{20} = e^{-0.020010} \approx 0.9802$ | $1.47$ |
| 40 | $0.98^{40} = e^{-0.808108} \approx 0.4457$ | $0.999^{40} = e^{-0.040020} \approx 0.9608$ | $2.16$ |
| 80 | $0.98^{80} = e^{-1.616216} \approx 0.1986$ | $0.999^{80} = e^{-0.080040} \approx 0.9231$ | $4.65$ |

For $c = 0.80$ ($\varepsilon_{\text{hyb}} = 0.02 \times 0.2 = 0.004$), $N = 40$:

$$P_{\text{clean}}^{\text{hyb}} = 0.996^{40}: \quad \ln(0.996) = -0.0040080, \quad 40 \times (-0.0040080) = -0.160320, \quad e^{-0.160320} \approx 0.8518.$$

For $c = 0.99$ ($\varepsilon_{\text{hyb}} = 0.0002$), $N = 40$:

$$P_{\text{clean}}^{\text{hyb}} = 0.9998^{40}: \quad \ln(0.9998) = -0.00020002, \quad 40 \times (-0.00020002) = -0.0080008, \quad e^{-0.0080008} \approx 0.9920.$$

For $\varepsilon = 0.05$ (pessimistic), $c = 0.95$ ($\varepsilon_{\text{hyb}} = 0.0025$), $N = 40$:

$$P_{\text{prompt}} = 0.95^{40}: \quad \ln(0.95) = -0.0512933, \quad 40 \times (-0.0512933) = -2.051731, \quad e^{-2.051731} \approx 0.1285.$$
$$P_{\text{hyb}} = 0.9975^{40}: \quad \ln(0.9975) = -0.0025031, \quad 40 \times (-0.0025031) = -0.100125, \quad e^{-0.100125} \approx 0.9047.$$

The pattern is uniform: the hybrid multiplier grows with $N$ and with $\varepsilon$, and no admissible prompt appears anywhere in the hybrid formula — the verifier's catch probability $c$ is the only lever that enters.

### 4.7 What prompt refinement can and cannot do

Under A2, prompt refinement can move $\varepsilon_T$ within $[\varepsilon_{\min}, \varepsilon_{\max}]$ but not below $\varepsilon_{\min}$. Suppose the best achievable prompt refinement halves the error rate to $\varepsilon = 0.01$ (this is a *projection*, assuming a best-case refinement factor of $2$; no cited source measures it). Then at $N = 40$:

$$P_{\text{clean}}^{\text{prompt, best}} = 0.99^{40} = e^{40 \times (-0.0100503)} = e^{-0.402013} \approx 0.6690.$$

Even this optimistic refinement leaves the prompt-only pipeline at $0.6690$, below the hybrid pipeline's $0.9608$ at the unrefined $\varepsilon = 0.02$. The comparison is the paper's central quantitative claim: the hybrid lever dominates the best-case prompt lever, and the dominance widens with $N$.

## 5. Results

All numbers in this section are computed in Section 4 with shown arithmetic from the stated inputs; none is measured by this paper.

- **R1.** For $N = 40$ constraints and $\varepsilon = 0.02$, the prompt-only clean-run probability is $P_{\text{clean}}^{\text{prompt}} = 0.98^{40} \approx 0.4457$ (Section 4.2).
- **R2.** With a post-hoc verifier catching errors with probability $c = 0.95$, the residual per-constraint error is $\varepsilon_{\text{hyb}} = 0.001$ and the clean-run probability is $0.999^{40} \approx 0.9608$ (Section 4.3).
- **R3.** The hybrid-to-prompt reliability ratio at these inputs is $\approx 2.156$ (Section 4.4).
- **R4.** The break-even constraint count is $N^{*} = 35$: at $35$ or more hard constraints the prompt-only pipeline succeeds less than half the time (Section 4.4).
- **R5.** At the per-constraint threshold $q^{*} \approx 0.986$ cited from [11], a $40$-constraint artifact is clean with probability $\approx 0.5691$, and a $300$-constraint artifact is clean with probability $\approx 0.0146$, consistent with the $16.7\%$ strict objective-success score [11] reports for a multi-chapter artifact (Section 4.5).
- **R6.** The hybrid advantage grows with scale: the ratio rises from $1.21$ at $N = 10$ to $4.65$ at $N = 80$ (Section 4.6).
- **R7.** The hybrid result is robust to verifier quality: at $c = 0.80$ the clean-run probability is $\approx 0.8518$ and at $c = 0.99$ it is $\approx 0.9920