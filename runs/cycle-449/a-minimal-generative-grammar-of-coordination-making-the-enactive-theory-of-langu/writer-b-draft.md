# A Minimal Generative Grammar of Coordination: Making the Enactive Theory of Language Falsifiable in Multi-Agent Simulation

## Abstract

The enactive thesis that language is an interaction protocol which generates, rather than describes, social reality is widely cited but rarely tested, because no operational specification of the thesis exists. This gap blocks both a research programme — nobody can say which simulation outcome would confirm or refute the thesis — and an engineering goal, namely autonomous agents that bootstrap shared meaning without a pre-installed world model. We convert the thesis into a design specification by defining a minimal grammar of coordination: a finite inventory of form-meaning constructions, an alignment update rule, and a norm-codification threshold, implemented as the only communicational endowment of agents that share no prior ontology. We derive analytical predictions for three measurable outputs: a lexicon-sufficiency bound $L \geq S^{1/m}$ (22 constructions for $10^4$ situation types at message length 3), a normative-complexity ceiling of 66 coordination patterns for a 50-agent community, and a perturbation law under which a 30% bot-message fraction reduces the stable shared lexicon from 52.8 to 39.0 constructions, a 26.1% drop. These quantities are computed from stated assumptions, not simulated. The derivation yields falsifiable predictions that distinguish grammar variants, specifies the simulation study that would test them, and gives trust-and-safety analysts a spectrum-based, rather than threshold-based, target for measuring coordination in live platforms.

## 1. Introduction

Two communities face the same unsolved problem from opposite sides. The first is the trust-and-safety and platform-integrity community: coordinated inauthentic behaviour on social media — astroturf networks, troll farms, bot-driven spam — manipulates public discussion, and the analytical tools available to detect it impose arbitrary binary thresholds that discard most of the coordination signal present in the data [1]. The second is the multi-agent AI community: as autonomous agents and generative systems enter social contexts whose societal impacts are still being assessed [7], systems are deployed that communicate through human language acquired from data, with no specification of how a community of artificial agents could generate its own shared meanings from interaction alone. Both communities lack a theory of coordination precise enough to engineer: the first cannot predict how a platform's coordination structure responds to interventions, and the second cannot specify the communicational protocol an agent population needs to sustain a stable social reality. What would change if the result of this paper holds: the claim that language generates social reality would become a testable design specification, and a designer could tune a named parameter of an agent protocol and predict the resulting lexicon size, normative complexity, and resilience to perturbation before running anything.

The philosophical source of the blockage is the enactive model of language, in which language is not a code that transmits descriptions of a pre-existing world but an interaction protocol that brings a shared social world into being between agents. The thesis is widely repeated and almost never tested, because it has been stated without an operational form: no definition says what the minimal protocol is, what outputs count as an "enacted world," or which observation would refute the claim. Critics can therefore dismiss the thesis as unfalsifiable, and engineers cannot use it, because a thesis with no parameters is not a design. The present paper removes that blockage by treating the enactive thesis the way a physicist treats a symmetry principle: as a constraint from which measurable consequences are derived.

Our approach is to write down the smallest protocol that could plausibly generate a social reality between agents with no pre-shared world model, and to call it a grammar of coordination. The protocol has three components, each chosen to be minimal: (i) a finite inventory of constructions — form-meaning mappings that agents imitate, align, and reuse, in the sense in which construction grammar treats all linguistic knowledge as freely combinable constructions on a lexicon-grammar continuum [3]; (ii) an alignment update rule that shifts each agent's constructions toward those of successful interaction partners; and (iii) a norm-codification threshold at which a repeatedly successful coordination pattern becomes a norm that constrains future interactions. We then derive, analytically and with all arithmetic shown, three quantities that a simulation of this protocol must reproduce if the enactive thesis is operational: a lexicon-sufficiency bound, a normative-complexity ceiling, and a perturbation-response law for injected inauthentic messages of the kind that bot networks produce in real platforms [6].

The derivations use a coordination-weight model chosen to mirror the spectrum view of coordination argued for in the platform-integrity literature: coordination is a matter of degree present to some extent in every community, not a binary property cut at a fixed threshold [1]. The perturbation model uses a bot-fraction parameter motivated by documented bot behaviour in content-spreading dynamics and election-period manipulation [6], [5]. The falsifiability criterion for the whole programme follows the requirement that a hypothesis posit cause and effect and be testable at bounded resource cost [8]. The generative character of the protocol — order arising from internal dynamics rather than pre-imposed rules — is articulated in the autaxys literature as a generative engine of relational processing, symmetry breaking, feedback, resonance, and critical transitions [11], and its tension among novelty, efficiency, and persistence [12] maps directly onto the three viability outputs we measure.

The contributions of this paper are:

- A formal definition of the minimal grammar of coordination as a three-component protocol (construction inventory, alignment rule, codification threshold) for agents with no pre-shared world model, given in Section 3.
- A derivation of the lexicon-sufficiency bound $L \geq S^{1/m}$, giving $L = 22$ constructions for $S = 10^4$ situation types at message length $m = 3$, in Section 4.1.
- A derivation of the normative-complexity ceiling $n = \min\{\binom{c}{2}, Lm\} = 66$ norms for a 50-agent community, with a compression ratio of 18.6 relative to unstructured pairwise norms, in Section 4.2.
- A derivation of the perturbation-response law: at bot fraction $b = 0.3$ the stable shared lexicon falls from $L^* = 52.8$ to $L^* = 39.0$ constructions, a 26.1% reduction, in Section 4.3.
- A falsifiability analysis stating which simulation outcomes would confirm and which would refute the operationalised enactive thesis, in Section 5 and Section 6.
- A translation of the results into an engineering pathway — who would use the grammar, at what readiness level, and what the smallest decisive experiment is — in Section 7.

Beyond multi-agent AI and platform integrity, the same protocol-level view of coordination bears on any field that models how shared structure grows out of repeated interaction, including the layered relational data extracted from online sharing systems [2] and the linguistic modelling of communication as a bidirectional process between users [3].

## 2. Background and Related Work

**Coordination as a measurable spectrum.** The detection of coordinated behaviour on social media has been dominated by manual investigation and by computational approaches that make simplifying assumptions to become tractable; the network-based framework of [1] instead embeds the intrinsic properties of coordination in its methodology, using a six-step pipeline that begins by selecting a starting set of users and proceeds through network construction and filtering to coordination-aware community detection. Its comparative evaluation shows the decisive methodological point for our purposes: by refusing to enforce a binary separation between coordinated and uncoordinated behaviour, the framework studies coordination across its entire spectrum, measuring the intrinsic coordination of each emerging community, whereas threshold-based approaches cut all edges below an arbitrary strict threshold and thereby discard the graded structure. The conclusions of [1] state the finding explicitly: there is a certain extent of coordination in every online community, but not all coordinated groups are equally interesting, and per-community coordination degree enables finer-grained downstream analysis than fixed thresholds. We adopt exactly this spectrum view as the measurement layer of our simulation programme: the coordination structure that our agent grammar generates is a weighted network whose edge weights are degrees of alignment, not a binary graph.

**Layered relational structure.** The data that online sharing systems accumulate reflects users' collective behaviour and shared activities, and from it multiple kinds of relationships can be extracted and grouped into layers — direct and oblique relations — forming a multidimensional social network [2]. This matters for our protocol design because a community of agents generates exactly such layers endogenously: a layer of direct interaction history, a layer of imitated or second-hand alignment, and a layer of codified norms. Our grammar treats these layers as outputs to be measured, and the multidimensional-network result of [2] supplies the representational format in which the outputs are compared across simulation runs and against real platform data.

**Constructions as the unit of coordination.** Construction grammar and artificial intelligence share a long-standing attitude toward communication: language serves the communicative needs of its users, production expresses an idea as an utterance, comprehension reconstructs the intention behind an observed utterance, and communication is bidirectional [3]. The basic tenets that [3] maps onto AI data structures are the ones our grammar adopts verbatim: all linguistic knowledge is captured in constructions, form-meaning mappings that can freely combine as long as no conflicts occur, and there is no lexicon-grammar divide — words and grammar rules are points on one continuum. This gives our protocol its minimal unit: an agent's entire communicational endowment is a set of constructions, and "learning to coordinate" is the growth and alignment of that set. [3] further documents that AI methods have historically been the route by which constructionist linguistics was made computationally operational, which is precisely the move we make for the enactive thesis.

**Perturbation by inauthentic agents.** Social bots are efficient automatic tools for generating content and diffusing information to human populations, and their interplay with information diffusion has been documented in two domains: political manipulation, as in the use of social bots during the 2016 US Presidential Election to sway discussion around candidates and frame agendas, and social spam campaigns [6]. The same chapter reviews the detection toolbox — graph-centric detection, crowdsourcing, and feature-based supervised learning — and the tools used in its case studies, including Bot Or Not for bot detection and SentiStrength for sentiment analysis. The concrete mechanism of manipulation is documented for the 2016 case in which a network of accounts animated by Russian operatives attempted to divert American political discourse, creating an online astroturf in direct contact with the public [5]. For our programme these works fix the perturbation model: an exogenous population of agents that emits well-formed-looking messages without participating in the alignment dynamics. Section 4.3 derives the predicted effect of such a population on the shared lexicon, and Section 7 proposes the simulation experiment that would test the prediction.

**Generative AI entering social reality.** The social impact of generative models has become a live assessment problem, with documented benefits such as enhanced customer service and automation of repetitive tasks, and documented areas of concern concentrated on privacy and bias [7]. That review's conclusion — that generative AI reflects the social context in which it was created, so that repairing the model alone is insufficient without examining the social factors around it — is an argument for systems whose social context is generated endogenously and therefore inspectable at the protocol level. Our grammar supplies exactly that: a generative model whose "social context" is the construction population its own interactions produce, making the analogue of bias and norm formation a measurable quantity rather than an emergent mystery.

**Falsifiability and experiment design as constraints on the programme.** The Artificial Scientist framework requires that a hypothesis be falsifiable, positing cause and effect, and that under finite computational resources the search over hypotheses be guided by an explicit heuristic weighing plausibility and expected profit [8]. Its treatment of experimental design — isolating the hypothesised cause, controlling other variables, and evaluating the information gain of an experiment against its resource cost and risk, with geometric-mean utility recommended when future capability depends on preceding outcomes — is the standard we use in Section 7 when specifying the smallest decisive experiment. [8] also supplies a cautionary negative result that shapes our protocol design: in its binary-task example, observational situation-response data alone cannot induce two concurrent rules, so an agent restricted to passive observation fails where interactive experimentation would succeed; this is a direct argument that our agents must act and align, not merely observe.

**Endogenous order as a generative engine.** The autaxys framework posits intrinsic self-ordering — self-arranging, self-generating patterned existence without recourse to external agents or pre-imposed rules — operated by a generative engine of core dynamics named as Relational Processing, Spontaneous Symmetry Breaking, Feedback Dynamics, Resonance, and Critical State Transitions, together with meta-logical principles including Intrinsic Coherence, Conservation of Distinguishability, and Parsimony [11]. Our grammar is a deliberate social-scale instantiation of that template: relational processing is the interaction history, symmetry breaking is the convergence of a population of variant constructions onto one shared form, feedback is the alignment update rule, and critical state transitions are the codification events at the norm threshold. The same framework's trilemma of Novelty, Efficiency, and Persistence, resolved continuously within a relational substrate [12], maps one-to-one onto the three viability outputs we measure: adaptability (novelty), lexicon parsimony (efficiency), and persistence under perturbation. [12] also proposes that the adequacy of such a foundational model be judged by comprehensive coherence — internal consistency plus explanatory power — rather than by isolated empirical verification alone; we take the stricter standard, demanding both coherence and the falsifiable simulation predictions of Section 5.

**Language as process, not inventory.** A deterministic process ontology observes that human grammar compels us to reify dynamic processes into static things — saying "an electron travels" suggests an entity separate from the travelling — and must consciously work against the grain of its own linguistic medium, treating nouns as temporary shorthands for repeating patterns [10]. This is the linguistic analogue of our central move: a "lexicon" in our model is not a static codebook but a population of repeating interaction patterns whose stability is itself the measured output. [10]'s further point that apparent noise is often the system expressing correlated history rather than error — that we should read the noise rather than filter it out — motivates our spectrum-based measurement layer, which retains graded alignment weights instead of thresholding them away, in agreement with [1].

## 3. Methods

This paper's method is analytical model-building followed by explicit derivation; no simulation, experiment, or data collection was performed, and every number in Section 4 is computed from stated assumptions by shown arithmetic. A study that would test the derivations is specified as a proposal in Section 7.

**The protocol.** A population of $N$ agents interacts in discrete rounds. Agent $i$ carries a construction inventory $C_i = \{(f_k, \mu_k)\}$ of form-meaning pairs, following the construction-grammar tenet that all linguistic knowledge is captured in freely combinable constructions [3]. No agent is given a world model, an ontology, or a shared codebook: the inventory is the agent's entire communicational endowment, and the meanings $\mu_k$ are grounded only in the agent's own interaction history. In round $t$, a pair of agents $(i, j)$ engages in a joint task whose success is defined operationally (a coordinated action succeeds if both agents' subsequent actions match). Agent $i$ selects constructions from $C_i$, combines them without conflict as construction grammar permits [3], and transmits; agent $j$ attempts to reconstruct the intention, in the bidirectional production-comprehension loop of [3]. On success, both agents shift the used constructions toward each other's variants by an alignment rate $\alpha \in (0, 1]$; on failure, each agent invents or mutates a candidate construction with novelty rate $\nu$. When a construction has participated in successful coordination in a fraction $\theta$ of a sliding window of interactions across distinct partners, it is codified: it becomes a norm that constrains future interactions and is resistant to mutation. The triple $(C, \alpha, \theta)$, together with $(\nu)$, is the grammar of coordination.

**Measurement layer.** Following the spectrum view of coordination [1], we do not threshold interactions into coordinated/not-coordinated. Instead we maintain a weighted interaction network in which the weight $w_{ij} \in [0,1]$ is the empirical success rate of the pair $(i,j)$, and we record per-community distributions of $w$. Following the multidimensional-network format of [2], we record three layers: the direct interaction layer ($w_{ij}$), the imitation layer (constructions adopted from third parties), and the norm layer (codified constructions).

**Viability outputs.** The enactive thesis, operationalised, claims that a stable social reality emerges endogenously. We define three measurable viability outputs, chosen to instantiate the novelty-efficiency-persistence trilemma of [12]:

- $L^*$: the equilibrium size of the shared construction inventory (efficiency/parsimony);
- $n$: the number of codified norms (normative complexity);
- $\rho(b)$: the resilience of $L^*$ under an exogenous bot fraction $b$ (persistence).

Adaptability is measured as the rate at which new constructions enter the inventory and is left as a simulation-measured quantity; the derivations here concern $L^*$, $n$, and $\rho$.

**Assumptions.** The derivations require input values that no cited source provides; each is stated as an assumption and its sensitivity is examined in Section 6. We assume: $S = 10^4$ distinct situation types the community must coordinate over; message length $m = 3$ constructions; community size $c = 50$ for the norm derivation; pairwise coordination weights approximately exponential with mean $\mu_w = 0.05$; bot fraction $b = 0.3$; construction reinforcement rate $r = 1.0$ per round; construction decay rate $\lambda = 0.2$ per round without reinforcement; and inventory carrying capacity $K = 66$ from the norm derivation of Section 4.2.

## 4. Analysis

### 4.1 Lexicon-sufficiency bound

**Input numbers.** $S = 10^4$ situation types (assumption, Section 3); message length $m = 3$ constructions (assumption, Section 3).

**Derivation.** A message of $m$ constructions drawn from a lexicon of size $L$ can distinguish at most $L^m$ situation types, since each of the $m$ slots admits $L$ choices and constructions combine freely [3]. Sufficiency of the lexicon requires

$$L^m \geq S \quad \Longrightarrow \quad L \geq S^{1/m}.$$

With $S = 10^4$ and $m = 3$:

$$L \geq 10^{4/3} = 10^{1.3333\ldots} = 21.5443\ldots$$

Since $L$ is an integer count of constructions, we round up:

$$L_{\min} = 22.$$

**Check.** $22^3 = 10648 \geq 10^4$; $21^3 = 9261 < 10^4$. The bound is tight at 22.

**Interpretation.** A community of agents with no pre-shared world model needs only 22 aligned constructions to coordinate over ten thousand situation types at message length three. This is the efficiency claim of the operationalised enactive thesis: shared meaning is cheap because constructions compose. It also yields a falsifiable prediction: a simulation in which the grammar is complete should converge to a shared inventory of order $10^{4/m}$ constructions, and a grammar variant that forbids free combination (a fixed-phrase protocol) would need $L \geq S = 10^4$ instead — a difference of three orders of magnitude that Section 5 turns into a decisive test.

### 4.2 Normative-complexity ceiling

**Input numbers.** Community size $c = 50$ (assumption, Section 3); $L = 22$ (derived, Section 4.1); $m = 3$ (assumption, Section 3).

**Derivation.** Without constructional reuse, every distinct pair of agents that must adjudicate a recurring interaction type would require its own norm, giving an unstructured norm count of

$$\binom{c}{2} = \frac{50 \times 49}{2} = \frac{2450}{2} = 1225.$$

With constructional reuse, each norm is a codified coordination pattern expressible as a construction-sequence of length up to $m$ over the lexicon, so the number of distinct expressible patterns is bounded by

$$L \cdot m = 22 \times 3 = 66.$$

The codified norm count is therefore

$$n = \min\{\binom{c}{2},\; L \cdot m\} = \min\{1225,\; 66\} = 66.$$

The compression ratio of constructional reuse over pairwise norms is

$$\frac{1225}{66} = 18.5606\ldots \approx 18.6.$$

**Interpretation.** The grammar caps normative complexity at 66 for a 50-agent community, an 18.6-fold reduction relative to unstructured pairwise norm formation. This is the parsimony principle of [11] (Conservation of Distinguishability with Parsimony) made quantitative at social scale, and it supplies the second falsifiable prediction: norm counts in simulation should saturate near $Lm$, not near $\binom{c}{2}$, and should scale as $O(Lm)$ rather than $O(c^2)$ as the community grows.

### 4.3 Perturbation-response law

**Input numbers.** Bot fraction $b = 0.3$ (assumption, Section 3, motivated by documented bot-driven diffusion and manipulation in platforms [6], [5]); reinforcement rate $r = 1.0$ per round; decay rate $\lambda = 0.2$ per round; carrying capacity $K = 66$ (derived, Section 4.2).

**Derivation, step 1: effective alignment.** A bot emits well-formed messages but does not participate in the alignment dynamics: its constructions are not updated by success, and its messages fail coordination with aligned partners at an elevated rate. We model the bot's effect as noise on both sides of each human-agent interaction: a message is useful for alignment only if it originates from a participating agent (probability $1 - b$) and is received in a context where the partner's participating message dominates (probability $1 - b$). The effective alignment rate is therefore

$$\alpha_{\text{eff}} = \alpha (1 - b)^2.$$

With $b = 0.3$:

$$(1 - b)^2 = 0.7^2 = 0.49, \qquad \alpha_{\text{eff}} = 0.49\,\alpha.$$

Equivalently, the effective decay rate of unreinforced constructions rises by the inverse factor:

$$\lambda_{\text{eff}} = \frac{\lambda}{(1-b)^2} = \frac{0.2}{0.49} = 0.40816\ldots$$

**Derivation, step 2: equilibrium lexicon.** We model the shared inventory size $L(t)$ as growing logistically toward the capacity $K$ through reinforcement and decaying at rate $\lambda_{\text{eff}}$:

$$\frac{dL}{dt} = r\left(1 - \frac{L}{K}\right) - \lambda_{\text{eff}} L.$$

Setting $dL/dt = 0$:

$$r\left(1 - \frac{L^*}{K}\right) = \lambda_{\text{eff}} L^* \quad \Longrightarrow \quad L^* = K\left(1 - \frac{\lambda_{\text{eff}}}{r}\right).$$

Clean (unperturbed) case, $\lambda_{\text{eff}} = \lambda = 0.2$, $r = 1.0$, $K = 66$:

$$L^*_{\text{clean}} = 66 \times (1 - 0.2) = 66 \times 0.8 = 52.8.$$

Perturbed case, $\lambda_{\text{eff}} = 0.40816$:

$$L^*_{\text{bot}} = 66 \times \left(1 - \frac{0.40816}{1.0}\right) = 66 \times 0.59184 = 39.0614\ldots \approx 39.0.$$

**Derivation, step 3: resilience.** The fractional loss of the stable shared lexicon is

$$\rho = \frac{L^*_{\text{clean}} - L^*_{\text{bot}}}{L^*_{\text{clean}}} = \frac{52.8 - 39.0614}{52.8} = \frac{13.7386}{52.8} = 0.26020\ldots \approx 26.1\%.$$

**Interpretation.** A 30% bot-message fraction, because it degrades alignment on both the sending and receiving side, cuts the sustainable shared lexicon by 26.1% — more than the naive $b = 30\%$ because of the quadratic factor $(1-b)^2 = 0.49$. This quadratic amplification is the third falsifiable prediction: a simulation should show lexicon loss scaling as $(1-b)^2$ in the moderate-$b$ regime, not linearly in $b$. It also gives platform analysts a quantitative stake in the spectrum view of [1]: the damage of an inauthentic population is a measurable, nonlinear function of its share of message volume, estimable per community from the weighted coordination network rather than from a binary bot/not-bot classification of the kind whose limitations [6] documents in its review of graph-centric, crowdsourcing, and feature-based detection.

### 4.4 Coordination-spectrum retention

**Input numbers.** Exponential coordination-weight distribution with mean $\mu_w = 0.05$ (assumption, Section 3); threshold $t = 0.15$, chosen as a strict cut in the style criticised in [1]; population $N = 1000$ agents (assumption, Section 3).

**Derivation.** For an exponential distribution with mean $\mu_w$, the fraction of pairwise coordination weights above threshold $t$ is

$$P(w > t) = e^{-t/\mu_w} = e^{-0.15/0.05} = e^{-3} = 0.049787\ldots \approx 4.98\%.$$

The complete interaction graph on $N = 1000$ agents has

$$\binom{1000}{2} = \frac{1000 \times 999}{2} = 499500$$

edges. A threshold-based analysis retains

$$499500 \times 0.049787 = 24868.4\ldots \approx 24868$$

edges and discards the remaining $499500 - 24868 = 474632$ edges, i.e. $95.02\%$ of the pairwise coordination information. The spectrum-based layer of Section 3 retains all $499500$ weighted edges. The retention ratio is

$$\frac{499500}{24868} = 20.087\ldots \approx 20.1\text{-fold}.$$

**Interpretation.** At a strict threshold, twenty-fold more graded coordination structure is available to a spectrum-based measurement than to a binary cut. This quantifies, for the simulation setting, the methodological argument that [1] makes empirically — that threshold approaches enforce a binary separation and lose the graded structure that per-community coordination degrees reveal — and it defines what the simulation's measurement layer must record so