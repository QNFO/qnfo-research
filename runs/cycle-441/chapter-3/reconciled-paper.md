# The Consequences of Information States: From Irreducible Ignorance to Measurable Social Outcomes

## Abstract

Individuals, institutions, and communities constantly act on incomplete information, and the qualitative study of ignorance has documented how information inequality, misinformation, and information avoidance reshape societies. What the existing literature lacks is a quantitative bridge from an agent's information state to the concrete cost of acting inside it. This paper builds that bridge. We adopt a two-level framework in which a complete informational census $\Omega$ is accessible to internal observers only through a limited physical poll $E$, and we attach numbers to the resulting deficit. From two calibration points reported in prior work we derive a linear ignorance-cost model $C(A)=1.27\%\,(1-A)$, under which raising awareness from $A=0.5$ to $A=0.8$ cuts expected loss by a factor of $2.5$, worth $3.81$ avoided lost bookings per $10{,}000$ searches at a $10\%$ baseline (the loss at $A=0.5$ itself being $6.35$ per $10{,}000$). A layered awareness model shows that raising structural exclusion from $0.40$ to $0.60$ drops awareness from $0.45$ to $0.30$ and raises modeled loss from $0.699\%$ to $0.889\%$. Channel-fidelity arithmetic reproduces a $2.59$-fold print-over-oral retention advantage, and a relevance-ceiling result shows structural exclusion halves an agent's accessible relevance from $25\%$ to $12.5\%$. The results convert information-state narrative into checkable arithmetic and give policymakers and platform designers a falsifiable cost model.

## 1. Introduction

Decision makers in education, public policy, and AI-driven recommendation systems repeatedly act on information they do not know they lack. Prior work on awareness quantifies the stakes: losses attributable to unrecognized ignorance have been described as measured in millions of dollars per year, with a modeled ignorance cost of $0.635\%$ of a baseline uncancelled-booker rate at an awareness level of $A=0.5$ [9]. Communities facing rapid technological change face the same problem at larger scale: the paper quantifying the Luddite rising of 1811–1813 documents that policy built on the caricature of "anti-technology" protest misdiagnosed the grievance, over-invested in repression — troops, the capital-offense Frame-Breaking Act of 1812, and the execution of seventeen Luddites at York in 1813 — and under-invested in the information channels that determined whether such conflicts escalated or subsided [8]. Today the same structure recurs wherever institutions misread the information states of the populations they govern, teach, or serve.

The cost of this gap is concrete. Without a way to attach a number to an information state, a policymaker cannot compare the expected return of a literacy program against a surveillance program; a platform designer cannot price the harm of a filter bubble against the cost of breaking it; an educator cannot rank curricula by how much recognized ignorance they remove. If a defensible quantitative link existed between an agent's position on the information spectrum — from profound ignorance to expert knowledge — and the expected loss from acting there, each of these decisions could be made with stated trade-offs instead of intuition. This paper derives that link from calibration points and structural models already present in the literature, and extends it with new arithmetic on channel fidelity, exclusion, and decision attitudes.

The approach is deliberately conservative. Every quantitative claim below is either recomputed here with shown arithmetic from inputs stated in the cited works, or explicitly labeled an assumption. No experiment, survey, or measurement was performed for this paper; where an empirical test is needed, Section 7 writes it as a proposal in the conditional.

The contributions are:

- A linear ignorance-cost model $C(A)=I(1-A)$ with $I=1.27\%$, derived from the two calibration points $C(0.5)=0.635\%$ and $C(0.8)=0.254\%$ of [9], with the loss at $A=0.5$ of $6.35$ lost bookings per $10{,}000$ searches and the avoided loss of $3.81$ per $10{,}000$ from raising $A$ to $0.8$, at a $10\%$ baseline (Section 4.4).
- A sensitivity analysis of the layered awareness model $A=a_{\mathrm{access}}\cdot a_{\mathrm{comp}}\cdot(1-x_{\mathrm{excl}})$ of [10], showing that raising exclusion $x_{\mathrm{excl}}$ from $0.40$ to $0.60$ lowers awareness from $0.45$ to $0.30$ and raises modeled loss from $0.699\%$ to $0.889\%$ (Section 4.5).
- A channel-fidelity derivation reproducing the oral retention $0.3487$ after ten relays, the half-content threshold of $6.58$ retellings, the print retention $0.9044$ after ten generations, and the $2.59$-fold print advantage of [8], together with a rumor-diffusion width of $5.48$ contact-hops in thirty days (Section 4.2).
- An adaptive group-testing computation showing that approximately $133$ interrogations, rather than $2000$, suffice to locate $k=20$ organizers among $n=2000$ suspects, a $15.05$-fold reduction over exhaustive search (Section 4.3).
- A relevance-ceiling analysis of structural exclusion, in which a single agent holds at most $1$ bit of an $8$-bit relevance budget ($12.5\%$), two agents at most $2$ bits ($25\%$), and exclusion of the second agent's channel ($R_2=0$) collapses the two-agent ceiling back to $12.5\%$ (Section 4.6).
- A formal mapping of decision-making under ignorance, using the maxmin and maxmax criteria that [2] identifies with pessimistic and optimistic attitudes, to the phenomena of information avoidance and denial described qualitatively in [7] (Section 4.7).
- An engineering reading of information states, in which the frozen-variable and folding operations of cluster-algebra theory [4], the estimation-aware control trade-off of mobile-sensor planning [3], and the instrument parameters of the Origins Space Telescope [1] and the Square Kilometre Array continuum program [6] supply formal templates for how observable sets are designed, priced, and frozen (Sections 3 and 4.8).

The framework developed here also bears on problems adjacent to its home domain: the design of formal knowledge-representation systems, where the expressible concept vocabulary of an ontology determines which questions an institution can ask [5], and the planning of large scientific surveys, where a community's collective information state is set by instrument and survey design [1], [6].

## 2. Background and Related Work

The qualitative account of information states that this paper quantifies is given in [7], which documents how information inequalities reinforce power dynamics, how the historical control of literacy by religious and political elites maintained authority over largely illiterate populations, how the digital divide excludes students and workers from online learning and remote work, and how disinformation, misinformation, and propaganda degrade trust, polarization, and decision-making. That chapter's claims are structural and narrative; the present paper's task is to attach arithmetic to them without altering their substance.

Two papers in the surrounding corpus already demonstrate that this conversion is possible. The Luddite paper takes the qualitative information-state account of the 1811–1813 rising — oral tradition, limited literacy, pub meetings, handbills, songs as information sources — and derives quantitative propositions with explicit arithmetic: an oral message at per-retelling fidelity $p=0.90$ retains $0.3487$ of its content after ten relays, a print chain at $q=0.99$ retains $0.9044$ across ten generations, a $2.59$-fold print advantage, a rumor diffusion width of $5.48$ contact-hops in thirty days, and an adaptive group-testing result in which approximately $133$ interrogations rather than $2000$ located $k=20$ organizers among $n=2000$ suspects, which the paper offers as the quantitative explanation for the movement's collapse after the York executions of 1813 [8]. That paper's method — state the assumption, show the arithmetic, interpret the result — is the method adopted here.

The awareness paper supplies the calibration this paper builds on. It formalizes a scalar awareness level and reports an impact factor $I\approx 1.27\%$ booking gain per $\%$ NDCG improvement anchored in real-world Airbnb ranking results, an ignorance cost of $C(0.5)=0.635\%$ and $C(0.8)=0.254\%$ of the baseline uncancelled-booker rate, a decision-theoretic loss function $L(p)=\max(0,12p-6)$ for a maximin agent with maximal loss $4.8$ utility units at $p=0.9$, and the projection that at a $10\%$ baseline the $0.635\%$ loss corresponds to roughly $6.35$ additional lost bookings per $10{,}000$ searches [9]. Critically for what follows, that paper also specifies a falsifiable experimental protocol: a pilot on an e-commerce platform would measure a baseline awareness level by questionnaire, randomly assign half the participants to an informational brief explaining algorithmic limitations, and compare conversion rates between groups, with a statistically significant mismatch between observed and predicted loss reduction serving as falsification [9]. Section 7 of the present paper adopts that protocol as its proposed next test.

The shaping-of-unawareness paper contributes the structural model of how awareness is produced and destroyed. It formalizes an information-ecosystem model unifying ordinal-game ignorance, sparse-signal reconstruction, and reinforcement-learning sample efficiency, and computes a representative-agent awareness of $1\times 0.75\times(1-0.40)=0.45$ in a layered model, single- and two-agent relevance ceilings of $\mu_1\le 1$ bit ($12.5\%$ of an $8$-bit unconstrained relevance) and $\mu_2\le 2$ bits ($25\%$), a collaborative advantage $\Delta\mu=R_2=1$ bit, and a zero-rate corollary showing that when $R_2=0$ the excluded agent's relevance components contribute nothing, so that structural exclusion can eliminate entire components of what an agent can relevantly know [10]. The zero-rate corollary is the formal core of this paper's treatment of information inequality: exclusion is not a reduction in quality but a removal of channels. The same paper supplies auxiliary numerical illustrations — a Fourier-coefficient usage figure, a robotic-training throughput figure, and an AlphaGo processing-rate figure — which Section 4.8 recomputes here as consistency checks on that model's arithmetic.

The decision-theoretic foundation for agents who cannot form probabilistic beliefs is given by the games-under-ignorance paper. It studies players interacting under the veil of ignorance whose beliefs are represented as subsets of opponents' actions rather than probability measures, places such interactions outside the Bayesian paradigm, and analyzes when players follow $\max\min$ or $\max\max$ decision criteria, identifying these with pessimistic and optimistic attitudes respectively; its primitive objects are finite ordinal games $\Gamma=\langle I,(A_i,\succsim_i)_{i\in I}\rangle$ with finite action sets and complete, transitive preference relations [2]. This supplies the formal vocabulary for Section 4.7, where information avoidance is read as an agent's choice of decision criterion under coarse beliefs.

Three works from outside the social domain supply the engineering templates. The estimation-aware control paper formulates mobile-sensor trajectory optimization in which the planner must account for how measurements collected along the trajectory affect estimation of the target state, solves the joint problem with an augmented Lagrangian method in continuous time, and demonstrates Pareto fronts trading estimation covariance against energy under weighting schemes $\omega_p$ and $\omega_u$ [3]. This is the cleanest formal statement in the corpus of the fact that information acquisition has a price, which is the rational kernel of information avoidance. The cluster-algebras textbook chapters define freezing at an index as the transformation that reclassifies a cluster variable as frozen and removes the corresponding column from the exchange matrix, prove that freezing commutes with seed mutation, and describe folding as the use of quiver symmetries to construct a quotient object with equivariant mutation dynamics [4]. These operations give a precise language for which parts of a structured information state are fixed — institutional facts, recorded records — and which remain mutable. Finally, the Origins Space Telescope interim report specifies a mission concept with a cold ($4\ \mathrm{K}$) large-aperture telescope of $9.1\ \mathrm{m}$ and five instruments providing imaging and spectroscopy from $5$ to $660$ microns, aimed at questions from the formation of the earliest galaxies to the creation of habitable worlds [1], and the Square Kilometre Array continuum-science proceedings collect chapters on revealing the physics and evolution of galaxies and galaxy clusters with SKA continuum surveys and on the star-formation history of the Universe with the SKA, revised in March 2015 for compliance with the SKA1 rebaselining [6]. Both are instances of a community deliberately choosing its physical poll $E$: the instrument parameters determine which of the world's possible observations are actually available.

The knowledge-representation survey completes the picture on the institutional side. It contrasts Formal Concept Analysis, which formalizes concepts and conceptual hierarchies mathematically, with Description Logics, which build concept descriptions from atomic concepts and atomic roles using constructors such as conjunction, disjunction, negation, value restriction, and existential restriction (the language $\mathcal{ALC}$), notes the adoption of the DL-based OWL as the standard ontology language for the semantic web and DL applications in medical informatics, software engineering, and configuration, and concludes that social networks and Web 2.0 applications are bringing new challenges for representing vast amounts of knowledge [5]. For the purposes of this paper, an ontology is an engineered information state: its vocabulary decides which distinctions an institution can even express, and therefore which ignorances it can recognize.

## 3. Methods

### 3.1 Framework

We work in the two-level framework of the preceding chapters. Let $\Omega$ denote the informational census: the complete set of facts that would fully determine the system of interest. Let $E$ denote the physical poll: the limited set of measurements and channels actually available to an internal observer. An agent's information state is the pair $(\Omega, E)$ together with the agent's position in the channels that make $E$ reachable. Three properties of this framework drive everything that follows. First, $E$ is a strict subset of what $\Omega$ would require, so every internal observer operates under an irreducible deficit. Second, $E$ is not given but engineered: instruments [1], [6], ontologies [5], and institutional record-keeping [4] all choose which measurements exist. Third, reaching $E$ has a cost, so acquiring information is a trade-off and declining to acquire it can be rational [3].

### 3.2 Quantities and models

We track four quantitative objects.

**Awareness level $A\in[0,1]$.** The fraction of an agent's relevant ignorance that the agent recognizes. The calibration of [9] attaches a cost to $A$.

**Layered awareness.** Following the layered model of [10], awareness is the product of three stage factors,

$$A = a_{\mathrm{access}} \cdot a_{\mathrm{comp}} \cdot (1 - x_{\mathrm{excl}}),$$

where $a_{\mathrm{access}}$ is the fraction of relevant channels the agent can reach, $a_{\mathrm{comp}}$ the fraction of reached content the agent can correctly interpret, and $x_{\mathrm{excl}}$ the fraction of relevance components structurally excluded from the agent's channels.

**Channel fidelity.** A transmission chain of $n$ relays, each preserving a fraction $p$ of the content, retains $p^n$; a print chain with per-generation fidelity $q$ retains $q^n$.

**Diffusion width.** A rumor spreading on a homogeneous contact network follows the heat-kernel law $\sigma(t)=\sqrt{t}$, with $t$ in days and $\sigma$ in contact-hops.

**Adaptive group testing.** Identifying $k$ defectives among $n$ items by binary splitting requires, to first order, $I \approx k\log_2(n/k)$ interrogations.

**Ignorance cost.** We adopt the linear cost form $C(A)=I(1-A)$, where $I$ is the impact factor and $C$ the loss as a fraction of a baseline rate. We take the linear form under the convention that the two calibration points of [9], $C(0.5)=0.635\%$ and $C(0.8)=0.254\%$, jointly fix the single parameter $I$; the consistency of this convention is verified in Section 4.4. The absolute loss in bookings is $B_0 \cdot C(A)$ per search, with baseline uncancelled-booker rate $B_0=10\%$.

**Relevance ceilings.** An agent's relevant knowledge is bounded by the number of channels it holds: with an $8$-bit unconstrained relevance budget, one channel gives $\mu_1\le 1$ bit and two channels $\mu_2\le 2$ bits, with a collaborative advantage $\Delta\mu = R_2$ equal to the rate of the second channel [10].

**Decision attitudes.** For an agent whose beliefs are subsets rather than probability measures, we use the $\max\min$ (pessimistic) and $\max\max$ (optimistic) criteria of [2], and the maximin loss function $L(p)=\max(0,12p-6)$ of [9].

### 3.3 Assumptions

- Fidelity $p=0.90$ per relay and $q=0.99$ per generation are constant across all relays and generations (assumed in [8]).
- The contact network is homogeneous enough for the diffusion approximation $\sigma(t)=\sqrt{t}$; no counter-information or suppression mechanism acts [8].
- Interrogations split a suspect set perfectly into halves, with no false positives or negatives [8].
- The mapping from NDCG improvement to booking gain is linear with impact factor $I=1.27\%$, and the baseline rate $B_0=10\%$ is constant across the population [9].
- Awareness $A$ is exogenous and static within each computation; dynamics are out of scope.
- Group-testing and relevance-ceiling arithmetic assumes error-free channels and exact rates.

All parameter values are taken from the cited works or are explicitly labeled assumptions where they appear.

## 4. Analysis

### 4.1 Oral and printed retention

Inputs: oral per-relay fidelity $p=0.90$ and print per-generation fidelity $q=0.99$, both stated in [8]; chain length $n=10$ relays or generations.

Oral retention after ten relays:

$$p^{10}=0.9^{10}=(0.9^5)^2=(0.59049)^2=0.3486784401\approx 0.3487.$$

Print retention after ten generations:

$$q^{10}=0.99^{10}=(0.99^5)^2=(0.9509900499)^2=0.9043820750\approx 0.9044.$$

Half-content threshold for the oral chain, solving $p^{n_{1/2}}=0.5$:

$$n_{1/2}=\frac{\ln 0.5}{\ln 0.9}=\frac{-0.6931471806}{-0.1053605157}=6.5788\approx 6.58.$$

Print-versus-oral advantage:

$$\frac{q^{10}}{p^{10}}=\frac{0.9043820750}{0.3486784401}=2.594\approx 2.59.$$

All four numbers reproduce the values reported in [8].

Sensitivity of the oral figure to the fidelity assumption: at $p=0.92$,

$$0.92^{10}=(0.92^5)^2=(0.6590815232)^2=0.4344,$$

a gain of $+0.0857$ over $0.3487$; at $p=0.88$,

$$0.88^{10}=(0.88^5)^2=(0.5277319168)^2=0.2785009\approx 0.2785,$$

a loss of $0.3487-0.2785=0.0702$ relative to the $p=0.90$ figure. A two-percentage-point change in per-relay fidelity therefore moves ten-relay retention by roughly $0.07$ to $0.09$ in absolute fraction, so the $2.59$-fold print advantage is robust to small fidelity errors but the absolute oral retention figure is not: it should be read as conditional on the assumed $p=0.90$ of [8].

### 4.2 Rumor diffusion width

Input: diffusion time $t=30$ days, stated in [8]; heat-kernel law $\sigma(t)=\sqrt{t}$ with $t$ in days and $\sigma$ in contact-hops.

$$\sigma(30)=\sqrt{30}=5.4772\approx 5.48\ \text{contact-hops}.$$

This reproduces the value reported in [8]: a rumor in this model reaches roughly five to six network steps from its origin within a month. The model assumes a homogeneous contact network with no counter-information or suppression; a real network with clustering or suppression would spread more slowly, so $5.48$ is an upper-bound width under the stated assumptions.

### 4.3 Adaptive group testing

Inputs: $n=2000$ suspects, $k=20$ organizers, both stated in [8]; binary-splitting model of Section 3.2 with perfect splits.

To first order, the number of interrogations required is

$$I \approx k\log_2\!\left(\frac{n}{k}\right)=20\cdot\log_2\!\left(\frac{2000}{20}\right)=20\cdot\log_2(100).$$

Since $\log_2(100)=\dfrac{\ln 100}{\ln 2}=\dfrac{4.6051701860}{0.6931471806}=6.6438561898$,

$$I\approx 20\times 6.6438561898=132.877\approx 133\ \text{interrogations}.$$

Exhaustive search over all suspects would require up to $n=2000$ interrogations. The reduction factor is

$$\frac{2000}{132.877}=15.054\approx 15.05.$$

Both numbers reproduce the values reported in [8], which offers this result as the quantitative explanation for the movement's collapse after the York executions of 1813: an informant-led splitting strategy could locate the organizer network with roughly one-fifteenth of the investigative effort of exhaustive search.

### 4.4 The linear ignorance-cost model

Inputs: calibration points $C(0.5)=0.635\%$ and $C(0.8)=0.254\%$ of the baseline uncancelled-booker rate, from [9]; assumed baseline rate $B_0=10\%$, from [9].

Under the linear convention $C(A)=I(1-A)$, the first calibration point fixes

$$I=\frac{C(0.5)}{1-0.5}=\frac{0.635\%}{0.5}=1.27\%.$$

Consistency check against the second point:

$$C(0.8)=1.27\%\times(1-0.8)=1.27\%\times 0.2=0.254\%,$$

which matches the second calibration point exactly. The two points of [9] are therefore consistent with a single-parameter linear model, and the model has no free parameters left after calibration.

Loss-reduction factor from raising awareness $A=0.5\to 0.8$:

$$\frac{C(0.5)}{C(0.8)}=\frac{0.635\%}{0.254\%}=2.5.$$

Absolute loss at the assumed $B_0=10\%$ baseline: the fractional loss $C(A)$ applies to the baseline rate, so the loss in percentage-points of searches is $B_0\cdot C(A)$. At $A=0.5$,

$$10\%\times 0.635\%=0.0635\ \text{percentage-points},$$

i.e. $0.000635\times 10{,}000=6.35$ lost bookings per $10{,}000$ searches, reproducing the projection of [9]. At $A=0.8$,

$$10\%\times 0.254\%=0.0254\ \text{percentage-points},$$

i.e. $2.54$ lost bookings per $10{,}000$ searches. The avoided loss from the awareness gain $0.5\to 0.8$ is therefore $6.35-2.54=3.81$ bookings per $10{,}000$ searches. We note that the $6.35$ figure is the loss at $A=0.5$, not the avoided amount; the avoided amount under this model is $3.81$ per $10{,}000$.

### 4.5 Sensitivity of the layered awareness model

Inputs: layered model $A=a_{\mathrm{access}}\cdot a_{\mathrm{comp}}\cdot(1-x_{\mathrm{excl}})$ of [10], with the representative-agent values $a_{\mathrm{access}}=1$, $a_{\mathrm{comp}}=0.75$, $x_{\mathrm{excl}}=0.40$; impact factor $I=1.27\%$ from Section 4.4; baseline $B_0=10\%$.

Baseline awareness:

$$A_1=1\times 0.75\times(1-0.40)=0.75\times 0.60=0.45,$$

reproducing the representative-agent value of [10]. Modeled loss at $A_1$:

$$C(0.45)=1.27\%\times(1-0.45)=1.27\%\times 0.55=0.6985\%\approx 0.699\%.$$

Raising structural exclusion to $x_{\mathrm{excl}}=0.60$:

$$A_2=1\times 0.75\times(1-0.60)=0.75\times 0.40=0.30,$$

$$C(0.30)=1.27\%\times(1-0.30)=1.27\%\times 0.70=0.889\%.$$

The exclusion increase of $0.20$ lowers awareness by $0.15$ and raises modeled loss by $0.889\%-0.699\%=0.190\%$ of the baseline rate, i.e. at $B_0=10\%$ an increase from $6.985$ to $8.89$ lost bookings per $10{,}000$ searches, or $+1.905$ per $10{,}000$. The sensitivity is linear by construction: $\partial C/\partial x_{\mathrm{excl}}=I\cdot a_{\mathrm{access}}\cdot a_{\mathrm{comp}}=1.27\%\times 0.75=0.9525\%$ per unit of exclusion, so each ten-percentage-point rise in exclusion adds $0.09525\%$ of baseline loss, about $0.95$ lost bookings per $10{,}000$ searches.

### 4.6 Relevance ceilings under structural exclusion

Inputs: $8$-bit unconstrained relevance budget, single- and two-agent ceilings $\mu_1\le 1$ bit and $\mu_2\le 2$ bits, collaborative advantage $\Delta\mu=R_2$, and the zero-rate corollary, all from [10].

Single agent: $\mu_1/8\le 1/8=0.125=12.5\%$ of the unconstrained budget. Two agents: $\mu_2/8\le 2/8=0.25=25\%$. The collaborative advantage is $\Delta\mu=R_2=1$ bit, so the second channel doubles the ceiling from $12.5\%$ to $25\%$.

Under the zero-rate corollary of [10], setting $R_2=0$ — the second agent's channel is structurally excluded — collapses the two-agent ceiling back to $\mu_2\le 1$ bit, i.e. $12.5\%$, and the excluded agent's relevance components contribute nothing. Exclusion therefore does not degrade the quality of what the remaining agent knows; it removes entire components of what the pair can relevantly know, halving the accessible ceiling from $25\%$ to $12.5\%$ in this illustration.

### 4.7 Decision attitudes under ignorance

Inputs: the $\max\min$/$\max\max$ criteria for agents with subset-valued beliefs, identified with pessimistic and optimistic attitudes, from [2]; the maximin loss function $L(p)=\max(0,12p-6)$ with maximal loss $4.8$ utility units at $p=0.9$, from [9].

The loss function is zero below the threshold $p=0.5$ (since $12p-6\le 0$ there) and rises linearly above it. At $p=0.9$: $L(0.9)=12\times 0.9-6=10.8-6=4.8$, reproducing the maximal loss of [9]. A pessimistic ($\max\min$) agent who cannot form a probability measure over outcomes — the situation [2] places outside the Bayesian paradigm — prices the unrecognized state at the worst-case loss $4.8$; an optimistic ($\max\max$) agent prices it at the best case and treats the loss as zero for $p\le 0.5$. Information avoidance, described qualitatively in [7] as the rejection of available information to preserve a worldview, maps in this vocabulary to an agent's choice of the $\max\max$ criterion over the $\max\min$ criterion: the avoidance decision is the selection of a decision rule, not a change in the information set. The cost of that selection is the difference between the two criteria's valuations, which at $p=0.9$ is $4.8$ utility units in the illustrative game of [9].

### 4.8 Consistency checks on the shaping-of-unawareness arithmetic

Three auxiliary figures reported in [10] are recomputed here as checks.

Fourier-coefficient usage: $121/40{,}000\times 100 = 0.3025\%\approx 0.30\%$, matching the reported $0.30\%$.

Robotic-training throughput: $9.0\times 10^{8}$ steps over $68$ hours gives

$$\frac{9.0\times 10^{8}}{68}=1.3235\times 10^{7}\approx 1.32\times 10^{7}\ \text{steps h}^{-1},$$

matching the reported $1.32\times 10^{7}$ steps h$^{-1}$.

AlphaGo processing rate: $30{,}000{,}000$ positions over $28\times 50=1400$ GPU-days gives

$$\frac{30{,}000{,}000}{1400}=2.1429\times 10^{4}\approx 2.14\times 10^{4}\ \text{positions GPU}^{-1}\ \text{day}^{-1},$$

matching the reported $2.14\times 10^{4}$. All three checks pass, supporting the internal arithmetic of the layered and relevance models of [10] that Sections 4.5 and 4.6 build on.

## 5. Results

The derivations of Section 4 yield the following quantitative statements. Every value is either recomputed above with shown arithmetic from inputs stated in the cited works, or labeled an assumption.

| Quantity | Value | Source of inputs | Derivation |
|---|---|---|---|
| Oral retention after 10 relays | $0.3487$ | $p=0.90$ from [8] | Section 4.1 |
| Oral half-content threshold | $6.58$ relays | $p=0.90$ from [8] | Section 4.1 |
| Print retention after 10 generations | $0.9044$ | $q=0.99$ from [8] | Section 4.1 |
| Print-vs-oral advantage | $2.59$-fold | $p,q$ from [8] | Section 4.1 |
| Oral retention sensitivity ($p=0.92$ / $p=0.88$) | $0.4344$ / $0.2785$ | assumption sweep | Section 4.1 |
| Rumor diffusion width at 30 days | $5.48$ contact-hops | $t=30$ from [8] | Section 4.2 |
| Adaptive group-testing interrogations | $\approx 133$ | $n=2000$, $k=20$ from [8] | Section 4.3 |
| Reduction vs exhaustive search | $15.05$-fold | $n=2000$, $k=20$ from [8] | Section 4.3 |
| Impact factor | $I=1.27\%$ | calibration of [9] | Section 4.4 |
| Loss at $A=0.5$ / $A=0.8$ | $0.635\%$ / $0.254\%$ | calibration of [9] | Section 4.4 |
| Awareness-gain loss reduction | $2.5$-fold | calibration of [9] | Section 4.4 |
| Absolute loss at $A=0.5$, $B_0=10\%$ | $6.35$ per $10{,}000$ | $B_0=10\%$ from [9] | Section 4.4 |
| Avoided loss, $A:0.5\to 0.8$, $B_0=10\%$ | $3.81$ per $10{,}000$ | $B_0=10\%$ from [9] | Section 4.4 |
| Layered awareness, $x_{\mathrm{excl}}=0.40$ / $0.60$ | $0.45$ / $0.30$ | model of [10] | Section 4.5 |
| Modeled loss, $x_{\mathrm{excl}}=0.40$ / $0.60$ | $0.699\%$ / $0.889\%$ | $I$ from [9], model of [10] | Section 4.5 |
| Loss sensitivity to exclusion | $0.9525\%$ per unit $x_{\mathrm{excl}}$ | $I$ from [9], model of [10] | Section 4.5 |
| Single-agent relevance ceiling | $1$ bit ($12.5\%$) | [10] | Section 4.6 |
| Two-agent relevance ceiling | $2$ bits ($25\%$) | [10] | Section 4.6 |
| Ceiling under exclusion ($R_2=0$) | $1$ bit ($12.5\%$) | zero-rate corollary of [10] | Section 4.6 |
| Maximin loss at $p=0.9$ | $4.8$ utility units | [9], criteria of [2] | Section 4.7 |
| Fourier-coefficient usage | $0.30\%$ | [10] | Section 4.8 |
| Robotic-training throughput | $1.32\times 10^{7}$ steps h$^{-1}$ | [10] | Section 4.8 |
| AlphaGo processing rate | $2.14\times 10^{4}$ positions GPU$^{-1}$ day$^{-1}$ | [10] | Section 4.8 |

Three results are new to this paper rather than reproductions: the sensitivity sweep of the oral-retention figure (Section 4.1), the exact consistency verification of the two calibration points of [9] under the linear model, including the corrected avoided-loss figure of $3.81$ per $10{,}000$ (Section 4.4), and the closed-form loss sensitivity to structural exclusion, $0.9525\%$ of baseline per unit exclusion (Section 4.5).

## 6. Discussion

The central claim of this paper is that the qualitative account of information states in [7] can be converted into checkable arithmetic without altering its substance, using calibration points from [9], structural models from [10], and templates from [8]. The conversion succeeds in the narrow sense that every quantity in the results table follows from stated inputs by shown arithmetic, and the auxiliary checks of Section 4.8 confirm the internal consistency of the models it builds on. The conversion is weaker in three respects that bound what the results can be used for.

First, the models are linear or power-law by assumption, not by measurement. The cost model $C(A)=I(1-A)$ is fixed by two points and verified against exactly those two points; a third calibration point at, say, $A=0.65$ would test linearity, and no source states one. If the true cost function is convex in $A$ — plausible if the last units of ignorance are the cheapest to remove — the linear model understates the value of awareness gains at high $A$ and overstates them at low $A$. Second, the awareness level $A$ is exogenous and static in every computation here. The dynamics — how exclusion feeds back into access, how awareness decays without reinforcement — are out of scope, so the results price a static information state but cannot predict the trajectory of one. Third, the absolute figures all inherit the assumed baseline $B_0=10\%$ from [9]; the fractional results ($0.699\%$, $0.889\%$, the $2.5$-fold factor) are baseline-independent, but every per-$10{,}000$ figure scales linearly with $B_0$ and should be rescaled for any other setting.

The mapping of information avoidance to criterion choice in Section 4.7 is the loosest link in the chain. It identifies avoidance with the adoption of a $\max\max$ rule under subset-valued beliefs, using the vocabulary of [2] and the loss function of [9]. This is a formal analogy, not a derivation: nothing in [2] or [9] states that human information avoiders behave as $\max\max$ agents, and [7] describes avoidance driven by cognitive dissonance and ideological commitment, which are not decision-theoretic attitudes in this sense. The mapping should be read as a hypothesis that makes avoidance amenable to cost accounting, not as a validated mechanism.

Falsification. The main result — that the linear ignorance-cost model with $I=1.27\%$ usefully prices information states — would be falsified if the experimental protocol of [9], adopted in Section 7 below, produced a statistically significant mismatch between the observed and predicted reduction in loss when awareness is raised from $A=0.5$ toward $A=0.8$. A secondary falsifier is a third calibration point inconsistent with the line: any measured $C(A)$ at intermediate $A$ that departs from $1.27\%(1-A)$ by more than the measurement noise would break the single-parameter model. For the layered model, a measured awareness response to a known exclusion change that does not track the product form $a_{\mathrm{access}}\cdot a_{\mathrm{comp}}\cdot(1-x_{\mathrm{excl}})$ would falsify the multiplicative structure of [10] as applied here.

Limitations, with sensitivity:

- Linearity of $C(A)$: rests entirely on two calibration points from [9]; no intermediate point exists in the sources. A convex true curve changes the avoided-loss figure of $3.81$ per $10{,}000$ in either direction.
- Baseline $B_0=10\%$: an assumption of [9], not a measurement; all absolute figures scale linearly with it.
- Constant fidelity $p=0.90$, $q=0.99$: assumed in [8]; Section 4.1 shows a $\pm 0.02$ fidelity change moves ten-relay oral retention by $+0.086$ or $-0.070$, so the $2.59$-fold advantage is robust but the absolute retention is not.
- Perfect binary splitting in group testing: assumed in [8]; false positives would raise the $133$ figure.
- Homogeneous contact network for $\sigma(t)=\sqrt{t}$: assumed in [8]; clustering lowers the $5.48$-hop width.
- Static, exogenous $A$: dynamics excluded by assumption here; no source supplies them.
- Criterion-choice reading of avoidance: a formal analogy between [2] and [7], not derived from either.
- No new empirical work: this paper performs no experiment, survey, or measurement; every empirical anchor is borrowed from [8], [9], or [10], and the framework's empirical status is exactly the status of those anchors.

An open question is whether the impact factor $I=1.27\%$, anchored in e-commerce ranking results in [9], transfers to the education and policy settings of [7]. No cited work measures awareness costs outside a recommendation-platform context, and the transfer to education and policy settings is an assumption, not a result.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result, and what changes.** Three user groups follow from the problem statement of Section 1. A platform designer pricing the harm of a filter bubble can use the exclusion sensitivity of Section 4.5: under the layered model, each ten-percentage-point rise in structural exclusion adds $0.95$ lost bookings per $10{,}000$ searches at a $10\%$ baseline, which converts an interface-design decision (how much diversity to force into a feed) into a stated trade-off. A policymaker comparing an information intervention against a control intervention can use the calibration of Section 4.4: raising recognized awareness from $0.5$ to $0.8$ is worth $3.81$ avoided lost bookings per $10{,}000$ searches under the stated assumptions, a number that can be set against the intervention's cost. An educator or curriculum designer can use the channel-fidelity result of Section 4.1: a print-quality channel ($q=0.99$) retains $2.59$ times more content over ten generations than an oral-quality channel ($p=0.90$), which prices literacy investment in retention terms. The historical analysis of [8] shows the cost of getting this wrong: repression-first policy in 1811–1813 misread the information state of the affected communities and under-invested in the channels that would have changed the outcome.

**(b) Readiness.** This work is purely analytical and has not been peer reviewed; under the NASA Technology Readiness Level definitions it sits at TRL 1–2: basic principles observed and reported, with the quantitative bridge formulated but unsupported by empirical application. No claim above TRL 3 is made or supportable, since no model here has been applied in a controlled setting.

**(c) The smallest next test.** The protocol specified in [9] is adopted here as the proposed next experiment, written in the conditional. A pilot study on an e-commerce platform would measure a baseline awareness level $A$ with a brief questionnaire on users' confidence in understanding the recommendation algorithm, randomly assign half the participants to an informational brief explaining algorithmic limitations, and compare conversion rates between groups. The model predicts a loss reduction from $C(A_{\mathrm{control}})$ to $C(A_{\mathrm{treatment}})$ with $I=1.27\%$; a statistically significant mismatch between observed and predicted reduction refutes the linear cost model. A single pilot with a few thousand users per arm would be sufficient to detect effects of the predicted size ($0.0381$ percentage-points of conversion, i.e. $3.81$ lost bookings per $10{,}000$ searches, between $A=0.5$ and $A=0.8$ at the assumed baseline), though the required sample size for a given power is not derived here and remains an open calculation.

**(d) Binding constraints.** The first constraint to bind in any empirical test is measurement validity: the questionnaire proxy for $A$ is unvalidated, and error in $A$ propagates directly into the calibration of $I$. The second is baseline heterogeneity: the model assumes a constant $B_0$ across the population, and Section 4.5's sensitivity shows how exclusion-driven heterogeneity in $A$ alone moves loss by $0.19\%$ of baseline across the modeled range. Whether the NDCG-to-booking impact factor transfers across platforms and domains is an open question the sources do not answer. For the historical and policy applications, the binding constraint is data: no source supplies a measured awareness level for any population outside the illustrative Airbnb context of [9].

**(e) Order-of-magnitude bounds.** As a labeled projection with stated assumptions: if the linear model holds and $B_0=10\%$, an intervention that raises average awareness by $\Delta A=0.1$ avoids $I\cdot\Delta A\cdot B_0 = 1.27\%\times 0.1\times 10\% = 0.0127\%$ of searches, i.e. about $1.27$ lost bookings per $10{,}000$ searches. This projection assumes the linear model, the $10\%$ baseline, and constant $I$; it is not a measurement.

**(f) Risks and misuse.** The same arithmetic that prices an information intervention prices an information restriction: a planner could use the exclusion sensitivity of Section 4.5 to select a level of structural exclusion that keeps modeled loss below a visibility threshold while maximizing exclusion. Publishing the cost model makes that optimization easier. A second misuse is false precision: the fractional figures carry the authority of arithmetic while resting on two calibration points and an assumed baseline, and citing them without the assumptions would overstate what is known.

## 8. Conclusion

This paper converted the qualitative information-state account of [7] into a body of checkable arithmetic built on three quantitative anchors: the channel-fidelity and group-testing results of [8], the awareness calibration of [9], and the layered and relevance models of [10]. The resulting cost model $C(A)=1.27\%(1-A)$ is exactly consistent with both of its calibration points, prices an awareness gain from $0.5$ to $0.8$ at a $2.5$-fold loss reduction and $3.81$ avoided lost bookings per $10{,}000$ searches at the assumed $10\%$ baseline, and combines with the layered model of [10] to show that a twenty-point rise in structural exclusion raises modeled loss from $0.699\%$ to $0.889\%$ of baseline. The relevance-ceiling analysis shows exclusion halving a two-agent accessible budget from $25\%$ to $12.5\%$, and the decision-attitude mapping frames information avoidance as a choice of decision criterion with a computable price. The framework's empirical status is inherited from its anchors, its dynamics are unwritten, and its transfer beyond recommendation-platform settings is untested; the falsification path is the randomized informational-brief pilot of [9]. What the conversion changes in practice is modest but concrete: information-state claims can now be stated as numbers with stated assumptions, and the next experiment that would confirm or break the model is specified.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.4). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 16 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] The Origins Space Telescope (OST) Mission Concept Study Interim Report. arXiv:1809.09702v1. https://arxiv.org/abs/1809.09702v1
[2] Optimism and Pessimism in Strategic Interactions under Ignorance. arXiv:2103.08319v4. https://arxiv.org/abs/2103.08319v4
[3] Continuous-Time Estimation-Aware Optimal Control of Mobile Sensors for Target Tracking. arXiv:2610.06654v1. https://arxiv.org/abs/2610.06654v1
[4] Introduction to Cluster Algebras. Chapters 4-5. arXiv:1707.07190v3. https://arxiv.org/abs/1707.07190v3
[5] A Survey on how Description Logic Ontologies Benefit from Formal Concept Analysis. arXiv:1107.2822v1. https://arxiv.org/abs/1107.2822v1
[6] Proceedings of 'Advancing Astrophysics with the SKA' (AASKA14) - Continuum Science' Chapters. arXiv:1412.6942v2. https://arxiv.org/abs/1412.6942v2
[7] https://papers.qnfo.org/papers/chapter-3. QNFO: 3. The Consequences of Information States.
[8] https://papers.qnfo.org/papers/chapter-4. QNFO: Part II: Historical Perspectives on Information States.
[9] https://papers.qnfo.org/papers/chapter-1. QNFO: Observing Ignorance: A Unified Theoretical Framework for Information Awareness.
[10] https://papers.qnfo.org/papers/chapter-2. QNFO: The Shaping of Unawareness: A Formal Analysis of Social, Cultural, Technological, and Individual Forces.
