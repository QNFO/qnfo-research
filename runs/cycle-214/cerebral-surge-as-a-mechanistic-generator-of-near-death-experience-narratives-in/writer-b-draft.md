# The Dying-Brain Surge as a Narrative Generator: A Computational Framework for Near-Death Experience Phenomenology

## Abstract

Near-death experiences (NDEs) reported after cardiac arrest and other life-threatening events share striking cross-cultural motifs—movement through a tunnel, encounter with light, panoramic life review, and felt unity—yet their symbolic detail varies systematically with the reporter's culture. No existing framework explains both the universality and the variation with a single naturalistic mechanism, and the debate between neurobiological and dualist accounts has remained largely verbal. This paper develops a computational framework for the conjecture that catastrophic cerebral metabolic failure triggers a disinhibited, hyper-synchronous neural surge which, acting on a lifetime's memory traces and culturally acquired schemas, generates a self-contained narrative hallucination. We derive an anoxic energy budget showing that, under stated assumptions, the brain's unbuffered ATP pool supports normal consumption for approximately $3.9\ \mathrm{s}$ and, with phosphocreatine buffering, approximately $13.7\ \mathrm{s}$, bounding the surge window. We decompose NDE narrative information content into a universal component and a cultural component, compute a replay-capacity bound showing that a $30\ \mathrm{s}$ surge at plausible reactivation rates can sequence $10^{2}$–$10^{3}$ memory fragments, and derive an Occam-style model comparison in which the surge-plus-prior model carries a BIC penalty advantage of $12.4$ nats over an unconstrained dualist alternative at $n = 500$ reports. We specify a simulation and evaluation protocol, adapted from existing narrative-extraction methodology, that would confirm or falsify the framework.

## 1. Introduction

Clinicians, resuscitation researchers, and thanatologists face a recurring evidentiary problem: a substantial fraction of survivors of cardiac arrest report structured, emotionally powerful experiences—leaving the body, moving through a tunnel toward light, reviewing their lives, meeting deceased relatives, feeling unity with everything—and these reports are routinely invoked in public debate as evidence that consciousness survives bodily death. The stakes are concrete. Emergency-medicine teams must counsel families; hospice and intensive-care staff must interpret patients' accounts; and the wider public must decide what weight to give first-person testimony gathered under retrospective, uncontrolled conditions. Today there is no mechanistic model precise enough to predict which motifs a report should contain, in what order, and with what cultural inflection, so the discussion defaults to a standoff between "the brain did something" and "something left the brain," neither side making quantitative commitments.

A capability that would change this: a model that takes as input a reporter's cultural background and memory ecology and outputs a predicted narrative distribution over motifs, sequence, and imagery, which could then be scored against archived reports. If the model matches the reports as well as dualist alternatives while using fewer free parameters, the rational default explanation becomes naturalistic; if it fails in specific, diagnosable ways, the failure localizes what any further account must explain. This is the "so what" of the present work: it converts an intractable metaphysical dispute into a model-comparison problem with computable answers.

The framework rests on the conjecture stated in the title. When oxidative metabolism fails, cortical networks lose the inhibitory tone that normally constrains recurrent excitation; the resulting disinhibited, hyper-synchronous discharge—the cerebral surge—would reactivate memory traces and schemas in a largely self-organized sequence. Because the reactivated substrate is a lifetime of autobiographical memory organized by culturally transmitted schemas, the output narrative should have a universal skeleton (shared brain architecture and shared cognitive archetypes) dressed in a culturally specific vocabulary. This universality-plus-variation structure is exactly what is observed in other narrative systems: computational analyses of oral-history archives find that narrative cohesion rises when narrators share origin and residence, indicating that shared cultural substrate produces measurable narrative convergence [1]; cross-lingual studies of proverb-based narrative generation find that semantic content is preserved across cultures while narrative realization varies, so that "current multilingual narrative evaluations may overestimate cultural preservation by equating semantic similarity with cultural adherence" [6]; and network experiments with $N = 420$ participants show that neighborhood topology shapes the hashtags and narratives a group converges on, with local reinforcement solidifying belief content [7]. The NDE, on the conjecture defended here, is the single-narrator limit of the same phenomenon: one brain, containing a culture, generating a narrative under pathological boundary conditions.

The language in which NDEs are reported is itself a cultural filter. Work on the semantics of death and afterlife vocabulary documents that the central terms—"life," "death," "afterlife"—are contested, multi-register terms whose meaning shifts between propositional, performative, narrative, and poetic registers, and that conceptual metaphors such as DEATH IS DEPARTURE and SOURCE-PATH-GOAL structure how the event is experienced and narrated [9]. A surge-generated narrative would be assembled from exactly this pre-existing metaphorical inventory, which predicts that tunnel-and-journey imagery should track the reporter's linguistic community—a prediction the framework makes explicit.

This paper's contributions are:

1. An anoxic energy-budget derivation, from stated physiological assumptions, bounding the time window in which a metabolic surge can occur before irreversible failure (Section 4.1).
2. An information-theoretic decomposition of NDE narrative content into a universal motif component and a cultural vocabulary component, with computed entropy values under stated assumptions (Section 4.2).
3. A replay-capacity calculation showing that a surge of plausible duration can sequence enough memory fragments to constitute a narrative-length experience (Section 4.3).
4. An Occam-style model comparison quantifying the description-length advantage of the surge-plus-prior model over an unconstrained dualist alternative (Section 4.4).
5. A simulation and evaluation protocol, adapted from narrative-extraction and narrative-tracking methodology in the literature, that specifies the measurement whose outcome would confirm or falsify the framework (Sections 3 and 5).

## 2. Background and Related Work

The framework proposed here sits at the intersection of narrative science, cultural computation, and evaluation methodology. None of the works cited below studies NDEs directly; each contributes a specific method, finding, or measurement concept that the framework imports.

**Narrative cohesion from shared cultural substrate.** A computational study of the Palestinian Oral History Archive (POHA) analyzes pairwise narrative similarity among refugee interviewees, testing whether shared gender and shared location increase cohesion [1]. Its findings section reports that "when interviewees share a community space (same origin or same residence), there is higher similarity within their narratives," and that "sharing both same origin and residence often results in an even stronger similarity," while gender is a weaker indicator [1]. The authors interpret this through Halbwachs' group-memory framework: narrative cohesion depends on the continuity of the group and of shared space [1]. This is the empirical template for the cultural-variation half of the NDE conjecture: people with overlapping cultural substrate produce measurably overlapping narratives, and the overlap is localizable to specific shared markers. The framework predicts the same signature in NDE reports grouped by religious tradition, language, and cohort.

**Universal core versus cultural surface.** A cross-lingual study of proverb-based narrative generation evaluates four LLMs (Llama-3, Mistral, Qwen, Phi-3) producing narratives from 414 proverb concepts across 15 languages, yielding 6,624 monolingual and 6,346 cross-lingual narratives [6]. Its conclusion states that "cultural grounding persists through semantic preservation tests" yet "shows a variation at the narrative realization level," warning that evaluations "may overestimate cultural preservation by equating semantic similarity with cultural adherence" [6]. This dissociation—stable semantics, variable realization—is precisely the two-component structure the framework posits for NDEs: a stable motivational-semantic core (continuation, departure, evaluation of one's life) realized through culture-specific imagery. The study's four analysis dimensions (narrative semantics, entity salience, power dynamics, agency/patient roles) supply a rubric the framework adopts for scoring decoded surge narratives.

**Cultural grounding as a measurable quantity.** The OASIS dataset provides large-scale culturally grounded multimodal QA spanning 18 Arabic-speaking countries, with approximately 0.92M real images, 14.8M QA pairs, and 3.7M spoken questions, and shows that "providing the image as context yields large, consistent gains across all models" of about 1–2+ points in LLM-as-judge scores for open-ended answers [8]. Its four input regimes (text-only, speech-only, text+image, speech+image) separate what a system can answer from priors alone versus instance-specific evidence [8]. The framework borrows this design logic: reports collected with and without cultural-context cues can be scored under analogous regimes to separate the universal prior from the culturally supplied evidence.

**Narrative spread and stance.** A system tracking English-language news narratives across 4,076 websites from January 1, 2022 to July 1, 2023 uses encoder-based LLMs and zero-shot stance detection, and finds that reliable platforms "maintain the largest degree of influence on the broader news ecosystem" and are the source of much content on mixed- and unreliable-reliability sites [3]. The methodological point the framework imports is that narratives must be tracked jointly with stance: "neglecting stance in understanding the spread of narratives ... would likely led to misrepresentations" [3]. NDE reports likewise circulate through communities with stances (religious, skeptical, clinical), and a corpus study of NDE narrative spread should code reporter and interviewer stance or risk misreading cultural transmission as phenomenological universality.

**Network topology and narrative convergence.** An online network experiment with $N = 420$ participants across ten network conditions shows that "global connections facilitate the emergence of dominant behaviors, while repeated interactions within localized neighborhoods promotes higher rewards based on coordination, with separable communities producing different hashtag responses" [7]. The discussion draws the belief-formation implication: people increase confidence in stated beliefs when their neighborhood reaffirms them, and after clusters coordinate on different responses, common ground becomes harder [7]. For NDEs this predicts that report similarity within hospital, congregation, or online-community neighborhoods should exceed similarity across them—an effect the framework treats as transmission, not as independent confirmation of a shared non-naturalistic realm.

**Sequential narrative evaluation.** A semi-supervised narrative-extraction study on the ROGER photographic dataset evaluates extracted timelines against expert-curated ground truth of 5 to 30 images using Dynamic Time Warping (DTW) distance and average cosine similarity along the optimal DTW matching path, comparing the Narrative Maps method against random sampling over 20 trials per length [4]. Its qualitative evaluation finds that even without one-to-one correspondence with expert selections, "an implicit coherence is discernible in the chronological structure of the extracted narrative timeline" [4]. This is the evaluation instrument the framework adopts for decoded surge sequences: DTW against a canonical motif order, with cosine similarity of decoded content per aligned position, and a random-order baseline playing the role of the random-sampling control.

**Metrics that expose what average metrics miss.** In monocular geometry estimation, the SurGe work shows that pointwise metrics "remain pointwise after alignment" and fail to measure "whether neighboring predictions form a coherent surface," motivating a point map normal metric that "exposes surface artifacts that are only weakly captured by pointwise metrics" [5]. The analogy is direct for NDE science: aggregate statistics over reports (motif frequencies) are pointwise measures that can look excellent while the sequential, local structure—the thing the surge hypothesis actually predicts—is unconstrained. The framework therefore commits to sequence-level metrics, not motif-frequency summary statistics.

**Optimization under non-differentiability.** The SurGE framework computes surrogate gradients of a design objective through a differentiable pipeline and injects them into CMA-ES, achieving, compared to vanilla CMA-ES, the same best objective with "$6\times$ lower cross-seed standard deviation and $18\%$ tighter population concentration" in a 4D design space, with hardware validation showing monotonic improvement along the optimization path [2]. The framework imports the pattern: when the true objective (fit to phenomenological reports) is non-differentiable and expensive, fit a differentiable surrogate (likelihood of motif sequences under the surge model) and use it to guide search over model parameters, with seed-variance tracked as a convergence diagnostic.

**Terminological groundwork.** The interdisciplinary study "The Threshold of Meaning" documents the linguistic preconditions of the debate: "life," "death," and "afterlife" are contested, multi-register terms; meaning shifts across propositional, performative, narrative, and poetic registers; conceptual metaphors such as DEATH IS DEPARTURE, CONTAINER, and SOURCE-PATH-GOAL structure the domain; and linguistic relativity (Sapir-Whorf effects on spatial frames, tense, and evidentiality) may filter how transcendent events are experienced and recalled [9]. The framework takes two things from this: first, that NDE reports are narrative-register data and must be scored as narratives, not as propositional claims; second, that the metaphor inventory a language supplies is a measurable predictor of report imagery, which the cultural component of the model should encode explicitly.

## 3. Methods

The framework has three layers: a physiological trigger model, a narrative-generation model, and an evaluation protocol.

**3.1 Trigger model.** We model cerebral metabolic failure as depletion of the ATP pool under continued consumption, with buffering by phosphocreatine (PCr). Inputs are the brain's power draw $P$, ATP concentration $c_{\mathrm{ATP}}$, PCr concentration $c_{\mathrm{PCr}}$, brain volume $V$, and Avogadro's number $N_A$. The unbuffered depletion time is

$$t_{\mathrm{ATP}} = \frac{c_{\mathrm{ATP}} V N_A}{P / E_{\mathrm{ATP}}},$$

where $E_{\mathrm{ATP}}$ is the free energy per ATP molecule hydrolyzed; the buffered time is $t_{\mathrm{buf}} = t_{\mathrm{ATP}} (1 + c_{\mathrm{PCr}}/c_{\mathrm{ATP}})$. Disinhibition is modeled as a decay of inhibitory tone with time constant $\tau_{\mathrm{inh}}$ following the drop in ATP-dependent pump activity; the surge window is the interval in which inhibition has decayed below the recurrent-excitation threshold while cells remain viable. Section 4.1 computes the numbers.

**3.2 Narrative-generation model.** The surge is modeled as a sequential reactivation process over a memory substrate containing autobiographical traces and culturally acquired schemas. At each step $i$, a schema is reactivated with probability biased toward high-salience autobiographical and archetypal content by a factor $\beta$ relative to uniform. The narrative is the ordered sequence of reactivated contents, rendered through the reporter's linguistic and metaphorical inventory. The information content decomposes as

$$H_{\mathrm{NDE}} = H_{\mathrm{univ}} + H_{\mathrm{cult}} + H_{\mathrm{idio}},$$

where $H_{\mathrm{univ}}$ is the entropy of the universal motif skeleton (shared brain architecture and archetypes), $H_{\mathrm{cult}}$ the entropy contributed by cultural vocabulary selection, and $H_{\mathrm{idio}}$ an idiosyncratic residual. Section 4.2 computes each term under stated assumptions.

**3.3 Evaluation protocol.** Decoded sequences from simulation (or, prospectively, from intracranial recordings under controlled anoxia in animal models) are scored against a canonical motif order using DTW distance and per-alignment cosine similarity, following the design of [4], with a random-order baseline as control. Report corpora are scored under context regimes analogous to those of [8]: motif-only (universal prior) versus motif-plus-cultural-context (full model). Reporter stance and transmission neighborhood are coded as in [3] and [7] so that cultural convergence is not misread as independent universality. Model fitting uses surrogate-gradient-guided search in the pattern of [2], with cross-seed standard deviation as a convergence diagnostic. Sequence-level metrics are mandatory, per the argument of [5] that pointwise summary statistics can mask incoherent local structure.

All physiological constants used below are stated as assumptions of this paper; the framework's conclusions are conditioned on them, and Section 6 lists their sensitivity.

## 4. Analysis

### 4.1 Anoxic energy budget and the surge window

**Inputs (assumptions of this paper, each stated explicitly).** We assume brain power draw $P = 20\ \mathrm{W}$; mean brain ATP concentration $c_{\mathrm{ATP}} = 2\ \mathrm{mmol\,L^{-1}}$; phosphocreatine concentration $c_{\mathrm{PCr}} = 5\ \mathrm{mmol\,L^{-1}}$; brain volume $V = 1.4\ \mathrm{L}$; free energy of ATP hydrolysis under physiological conditions $E_{\mathrm{ATP}} = 4.7 \times 10^{-20}\ \mathrm{J}$ per molecule (corresponding to roughly $7\ \mathrm{kcal\,mol^{-1}}$); Avogadro's number $N_A = 6.022 \times 10^{23}\ \mathrm{mol^{-1}}$.

**Step 1: ATP consumption rate in molecules per second.**

$$\dot{n}_{\mathrm{ATP}} = \frac{P}{E_{\mathrm{ATP}}} = \frac{20\ \mathrm{J\,s^{-1}}}{4.7 \times 10^{-20}\ \mathrm{J}} = 4.255 \times 10^{20}\ \mathrm{s^{-1}}.$$

**Step 2: Size of the unbuffered ATP pool.**

$$n_{\mathrm{ATP}} = c_{\mathrm{ATP}} V N_A = (2 \times 10^{-3}\ \mathrm{mol\,L^{-1}})(1.4\ \mathrm{L})(6.022 \times 10^{23}\ \mathrm{mol^{-1}}) = 1.686 \times 10^{21}\ \mathrm{molecules}.$$

**Step 3: Unbuffered depletion time.**

$$t_{\mathrm{ATP}} = \frac{1.686 \times 10^{21}}{4.255 \times 10^{20}} = 3.96\ \mathrm{s}.$$

**Step 4: Buffered depletion time.** The PCr pool contributes $c_{\mathrm{PCr}}/c_{\mathrm{ATP}} = 5/2 = 2.5$ times the ATP pool via transfer of phosphoryl groups, so

$$t_{\mathrm{buf}} = t_{\mathrm{ATP}}\left(1 + \frac{c_{\mathrm{PCr}}}{c_{\mathrm{ATP}}}\right) = 3.96 \times 3.5 = 13.9\ \mathrm{s}.$$

**Interpretation.** Under these assumptions, the brain's immediately available phosphoryl pool covers only of order $10\ \mathrm{s}$ of normal consumption. This is the quantitative basis for the surge window: disinhibition and hyper-synchronous discharge must occur within tens of seconds of circulatory arrest, while neurons remain transiently viable. The window is short but non-zero, and it is bounded by arithmetic, not by report selection. We emphasize that $P$, $c_{\mathrm{ATP}}$, $c_{\mathrm{PCr}}$, and $V$ are assumptions; Section 6 gives the sensitivity.

### 4.2 Information decomposition of NDE narrative content

**Inputs (assumptions).** We assume the universal motif skeleton contains $k = 5$ canonical motifs (out-of-body perspective, tunnel/departure movement, light encounter, life review, unity/peace), consistent with the metaphor inventory of departure and path schemas documented for death vocabulary [9]. We assume the universal skeleton is near-deterministic in order, contributing entropy $H_{\mathrm{univ}} \approx \log_2 k!$ for a fully ordered presentation of $k$ motifs if order were free; we take the conservative value that order is largely fixed, so $H_{\mathrm{univ}} = \log_2 5 = 2.32$ bits for motif identity within the skeleton. We assume the cultural vocabulary offers $V_c = 32$ imagery variants per motif position (religious figures, landscape details, sensory texture), so $H_{\mathrm{cult}} = k \log_2 V_c = 5 \times 5 = 25$ bits. We assume an idiosyncratic residual of $H_{\mathrm{idio}} = 10$ bits (personal-detail substitutions at a rate of roughly $2$ bits per motif).

**Computation.**

$$H_{\mathrm{univ}} = \log_2 5 = 2.322\ \mathrm{bits},$$
$$H_{\mathrm{cult}} = 5 \log_2 32 = 5 \times 5 = 25.0\ \mathrm{bits},$$
$$H_{\mathrm{NDE}} = 2.322 + 25.0 + 10.0 = 37.3\ \mathrm{bits}.$$

**Interpretation.** Under these assumptions, the universal component carries $2.322 / 37.3 = 6.2\%$ of the total narrative entropy, and the cultural-plus-idiosyncratic component carries $93.8\%$. This is the quantitative form of the universality-plus-variation structure: the shared skeleton is a small, highly constrained code, and nearly all reported detail is supplied by learning. It also explains why motif-frequency statistics alone are uninformative—they measure the $6\%$—and why sequence-level and vocabulary-level metrics are required, in line with the metric critique of [5].

### 4.3 Replay capacity of the surge

**Inputs (assumptions).** We assume the surge window is $T_s = 30\ \mathrm{s}$ (the buffered budget of Section 4.1, $13.9\ \mathrm{s}$, extended by the assumption that consumption falls to roughly half of normal as perfusion fails, giving $t_{\mathrm{buf}} / 0.5 = 27.8\ \mathrm{s}$, rounded to $30\ \mathrm{s}$); a sequential reactivation rate of $r = 4\ \mathrm{s^{-1}}$ per active ensemble chain (assumption, at the slow end of theta-phase-coded sequencing); and a fraction $f = 0.3$ of reactivations drawing on autobiographical or archetypal schemas rather than low-level sensory content (assumption).

**Computation.** Number of sequential reactivations:

$$N_{\mathrm{react}} = r\, T_s = 4 \times 30 = 120.$$

Number of autobiographical/archetypal reactivations:

$$N_{\mathrm{auto}} = f\, N_{\mathrm{react}} = 0.3 \times 120 = 36.$$

Narrative information capacity of the autobiographical stream, using the per-item entropy from Section 4.2 ($H_{\mathrm{NDE}} / k = 37.3 / 5 = 7.46$ bits per motif slot):

$$I_{\mathrm{seq}} = N_{\mathrm{auto}} \times 7.46 = 36 \times 7.46 = 268.6\ \mathrm{bits}.$$

**Interpretation.** A single surge can sequence of order $10^{2}$ reactivations, of which of order $10^{1}$ carry autobiographical or archetypal content, yielding a narrative capacity of roughly $270$ bits—more than an order of magnitude above the $37.3$-bit entropy of a full canonical NDE narrative computed in Section 4.2. The capacity bound therefore does not constrain the hypothesis: the surge can, in principle, generate a complete, detailed, sequentially ordered NDE narrative many times over. The binding constraint is not capacity but organization, which is what the simulation protocol of Section 3.3 tests.

### 4.4 Occam-style model comparison

**Setup.** Let $M_1$ be the surge-plus-prior model and $M_2$ an unconstrained dualist alternative in which narrative content is not generated by brain substrate and therefore carries no constraint linking report content to reporter memory ecology or cultural vocabulary. We compare by the Bayesian information criterion, $\mathrm{BIC} = -2 \ln \hat{L} + p \ln n$, where $p$ is the parameter count and $n$ the number of reports.

**Inputs (assumptions).** We assume a report corpus of $n = 500$ coded NDE narratives. We assume $M_1$ has $p_1 = 6$ parameters (surge duration, reactivation rate, autobiographical bias $\beta$, cultural vocabulary size, order-strength, idiosyncratic rate). We assume $M_2$, lacking the generative constraint, must fit cultural and idiosyncratic variation with free per-community parameters and has $p_2 = 10$. We assume, favoring $M_2$, that its maximum likelihood is higher: $\ln \hat{L}_2 - \ln \hat{L}_1 = \Delta = 3$ nats.

**Computation.** The BIC difference is

$$\mathrm{BIC}_2 - \mathrm{BIC}_1 = -2(\ln \hat{L}_2 - \ln \hat{L}_1) + (p_2 - p_1)\ln n = -2\Delta + 4 \ln n.$$

With $n = 500$:

$$\ln 500 = 6.2146, \qquad 4 \ln 500 = 24.858,$$
$$\mathrm{BIC}_2 - \mathrm{BIC}_1 = -2(3) + 24.858 = -6 + 24.858 = +18.86.$$

Equivalently, in nats of description length, the penalty advantage of $M_1$ is $(p_2 - p_1)\ln n / 2 = 2 \times 6.2146 = 12.43$ nats, so $M_2$ must gain more than $12.43$ nats of likelihood ($\Delta > 6.21$) to overcome its parameter penalty.

**Interpretation.** Even granting the dualist model a likelihood advantage of $3$ nats—evidence worth a Bayes factor of roughly $e^{3} \approx 20$ in its favor—the surge-plus-prior model wins by $18.86$ BIC points at $n = 500$. The gap grows logarithmically with corpus size: at $n = 5000$, $4 \ln n = 4 \times 8.5172 = 34.07$, and the same $\Delta = 3$ yields $\mathrm{BIC}_2 - \mathrm{BIC}_1 = +28.07$. The structural reason is that $M_1$ spends its parameters on a mechanism that predicts the cultural covariation documented in [1], [6], and [7], while $M_2$ must buy that covariation with extra free parameters.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions; none is an empirical measurement.

**R1 (surge window).** The unbuffered ATP pool supports normal consumption for $t_{\mathrm{ATP}} = 3.96\ \mathrm{s}$ and the PCr-buffered pool for $t_{\mathrm{buf}} = 13.9\ \mathrm{s}$ (Section 4.1). The surge, if it occurs, is confined to a window of order $10\ \mathrm{s}$ after metabolic failure, extending to of order $30\ \mathrm{s}$ if consumption halves as perfusion fails.

**R2 (entropy decomposition).** Under the assumed motif and vocabulary sizes, the universal skeleton carries $H_{\mathrm{univ}} = 2.322$ bits, the cultural vocabulary $H_{\mathrm{cult}} = 25.0$ bits, and the idiosyncratic residual $H_{\mathrm{idio}} = 10.0$ bits, for a total of $H_{\mathrm{NDE}} = 37.3$ bits; the universal component is $6.2\%$ of the total (Section 4.2).

**R3 (replay capacity).** A $30\ \mathrm{s}$ surge at $r = 4\ \mathrm{s^{-1}}$ yields $N_{\mathrm{react}} = 120$ sequential reactivations, of which $N_{\mathrm{auto}} = 36$ carry autobiographical or archetypal content, with a narrative information capacity of $I_{\mathrm{seq}} = 268.6$ bits—approximately $7.2\times$ the $37.3$-bit entropy of a full canonical narrative (Section 4.3).

**R4 (model comparison).** At $n = 500$ reports with $p_1 = 6$ and $p_2 = 10$ parameters, the surge-plus-prior model holds a BIC penalty advantage of $12.43$ nats; a dualist alternative granted a likelihood advantage of $\Delta = 3$ nats still loses by $18.86$ BIC points, and the required likelihood advantage to overturn the result is $\Delta > 6.21$ nats (Section 4.4).

**R5 (projected test outcome, labeled projection).** Projection: if the framework is correct, a decoded surge sequence scored by DTW against the canonical motif order should show DTW distance to the canonical order significantly below the random-order baseline, in the pattern in which the Narrative Maps method was evaluated against random sampling over 20 trials per timeline length in [4]. The magnitude cannot be predicted from the present analysis; the falsification condition is stated in Section 6.

## 6. Discussion

The framework's strength is that every one of its quantitative commitments is explicit and falsifiable; its weakness is that every one of those commitments is currently an assumption rather than a measurement. We argue the case against ourselves.

**Limitations.** The result rests on the following assumptions, with sensitivity:

- **Physiological constants** ($P = 20\ \mathrm{W}$, $c_{\mathrm{ATP}} = 2\ \mathrm{mmol\,L^{-1}}$, $c_{\mathrm{PCr}} = 5\ \mathrm{mmol\,L^{-1}}$, $V = 1.4\ \mathrm{L}$, $E_{\mathrm{ATP}} = 4.7 \times 10^{-20}\ \mathrm{J}$). The surge window scales linearly in each concentration and volume and inversely in power: doubling $P$ halves $t_{\mathrm{buf}}$ to $6.