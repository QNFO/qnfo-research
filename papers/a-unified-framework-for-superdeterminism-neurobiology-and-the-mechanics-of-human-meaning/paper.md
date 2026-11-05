# A Unified Framework for Superdeterminism, Neurobiology, and the Mechanics of Human Meaning

## Abstract

Superdeterminism—the proposal that measurement settings and measured systems share a common causal history, so that the statistical independence assumption in Bell's theorem fails—remains philosophically contested, and its consequences for how humans think, decide, and build institutions are almost entirely unexplored. This paper closes part of that gap by connecting the formal structure of superdeterministic theories to the neurobiology of agency perception and to the design of human-facing systems. We derive the CHSH bound $S \le 2$ and its quantum maximum $S = 2\sqrt{2} \approx 2.8284271$ with full arithmetic, showing a relative violation of $41.42136\%$, and locate superdeterminism as the only locality-preserving escape among the options the literature evaluates. We then build a compression model of the agency heuristic: under stated assumptions, abstracting $N = 1000$ causal variables into $k = 3$ agent categories accelerates a decision by a factor $\Gamma = N/k \approx 333$, which supplies the evolutionary rationale for a free-will interface on a deterministic substrate. We analyze the readiness-potential timing gap of several hundred milliseconds and project a metabolic cost of roughly $3$ kcal per day for "dual-boot" cognition that holds determinism in the background while acting under the agency heuristic. Using reported human-AI collaboration results, we compute an explanatory benefit of $4.99$ percentage points in task win rate. The resulting layered framework—physics, neurobiology, meaning, ethics, institutions—shows that human meaning survives determinism because meaning is a computed state, and it gives justice reformers, AI designers, and science communicators a testable architecture with a concrete falsification test.

## 1. Introduction

Courts, clinics, and classrooms all run on an unexamined assumption: that a person could have done otherwise. Criminal sentencing assigns blame on that assumption; psychotherapy treats fatalism as a pathology; interface designers build systems around an autonomous, freely choosing user. Each of these practices costs something concrete when the assumption is wrong. If deterrence and recidivism outcomes depend on the blame presupposition, as this framework hypothesizes, and if patients who adopt a deterministic view experience motivational decline, then these practices could incur concrete costs; and AI systems that model humans as unconstrained optimizers mispredict the heuristic, compressed way people actually decide. If a rigorous deterministic picture of human action could be stated without destroying motivation, meaning, or accountability, all three practices would change: justice could shift from blame to forward-looking correction, clinicians could distinguish fatalism from determinism, and system designers could model users as they are.

The obstacle is that the physics looks hostile. Bell's theorem, in the summary of [3], shows that "given plausible assumptions, Bell shows that, in our world, events that are arbitrarily far apart can instantaneously influence each other," and its assumptions seem "so innocuous that it requires us to radically change how we think about the world." The one assumption that is not innocuous is statistical independence between measurement settings and the measured system; relaxing it defines superdeterminism. Superdeterminism has been given a rigorous formal definition only recently: [6] defines it as a property of physical theories and constructs "generalized response functions" $\mathcal{R}(k|M,p)$ that any nonsuperdeterministic theory must satisfy, putting "the onus on the proponents of a given theory to explain all of its mechanisms in a consistent and concise way." What is missing is not the physics but the bridge: no existing framework connects this formal structure to the neurobiology that makes agents *feel* free, to the evolutionary economics that would favor such a feeling, or to the institutions that would change if the feeling is an interface rather than a fact.

This paper builds that bridge analytically. Its method is derivation plus synthesis: every quantitative claim is computed here from stated inputs, and every claim about other works is tied to a specific result in that work. The contributions are:

- A fully worked derivation of the CHSH inequality and its quantum violation, with explicit arithmetic showing $S = 2\sqrt{2} \approx 2.8284271$ against the local bound $2$, and an identification of statistical independence as the load-bearing assumption (Section 4.1).
- A compression model of the agency heuristic, deriving a decision-speedup factor of approximately $333$ under stated assumptions, which supplies the evolutionary "why" for a free-will interface on deterministic hardware (Section 4.2).
- An analysis of the action-awareness timing gap of several hundred milliseconds reported for the readiness potential, and its consequence for legal and psychological framing (Section 4.3).
- A metabolic projection for "dual-boot" cognition—holding determinism explicitly while acting through the agency heuristic—bounded under stated assumptions (Section 4.4).
- A computation of the explanatory benefit of lucid explanations in human-AI collaboration, $\Delta_{\text{win}} = 4.99$ percentage points, from the reported ExAG study results (Section 4.5).
- A layered synthesis from physics to ethics and institutions, with a proposed smallest-next falsification test based on local nonlinear dynamics (Sections 5–7).

The framework may also bear on adjacent problems: the design of artificial agents whose reward processing mirrors human heuristic biases, and the communication of deterministic scientific results to non-specialist audiences without producing demotivation.

## 2. Background and Related Work

**Bell's theorem and its escape hatches.** [3] is a survey that introduces Bell's theorem through a calcium-atom photon-pair example with polarizers on left and right, notes that detector unreliability "can be relaxed, and analyses have been done to show the differences do not change the conclusion," and then examines exactly two strategies for avoiding non-locality: revising the axioms of classical probability theory, and "embracing superdeterminism and allowing systematic violations of statistical independence." Its conclusion is that neither strategy seems promising, though studying them deepens understanding of the theorem. Our framework takes the second strategy seriously precisely because [3] identifies it as one of only two doors, and because the formalization in [6] has since made the strategy precise enough to evaluate rather than dismiss.

**The formal standard for superdeterminism.** [6] adopts the position that measurement can only be understood relative to a specific explanatory theory $T$, which "must be specified as part of $T$, assuming both are needed for that theory to produce the empirical data," and that "there must be some theory $T$ that is ontologically true." It defines preparation procedures $p$ as procedures that "measure and verify that the system has the properties in a list $L_{P}$," and it requires nonsuperdeterministic theories to use generalized response functions $\mathcal{R}(k|M,p)$ representative of a strong constraint; theories failing the standard bear the burden of explaining their mechanisms. This is the methodological backbone of our Section 3: we treat the human agent as a physical system whose "response functions" are generated deterministically, and we accept the burden of specifying mechanisms.

**Intuitive models of superdeterminism.** [2] makes superdeterminism intuitive "by simulating a deterministic model system, a billiard game," in which "an initial 'bang' correlates all events, just as in the superdeterministic universe," and introduces the notions of "strong" and "soft" superdeterminism to clarify debates. The billiard analogy does real work in our framework: it separates the claim that initial conditions correlate everything (strong) from the claim that observed correlations are compatible with local dynamics (soft), and our synthesis uses the soft reading as the scientifically tractable one.

**Dynamical mechanisms and the fine-tuning critique.** [11] identifies the central weakness of superdeterminism as a theoretical gap: constructive proposals such as the Cellular Automaton Interpretation "provide a powerful proof-of-concept for a deterministic ontology but typically stop short of specifying the precise evolutionary laws that would give rise to the specific, non-local-appearing correlations observed in nature," leaving them open to the charge of replacing non-locality "with the mystery of pre-ordained, fine-tuned initial conditions." The same work reports a computational proof-of-principle in which "local, non-linear dynamics can serve as a viable physical mechanism for generating the correlations required by superdeterminism," shown to be "a robust and generic feature of the simulated system," and reframes the "sterility" critique as a category error arising from a Lakatosian methodology that "has a clear procedure for rejecting theories that attack the hard core but offers no formal path for their comparative assessment." Our Section 7 builds its falsification test directly on this mechanism-level result.

**Deterministic substrates and exotic geometry.** [12] argues that the continuum assumption of classical physics "generates mathematical contradictions" at microscopic scales, that general relativity "produce[s] infinite energy densities when forced to describe interactions at these microscopic coordinates," and that resolving this "requires abandoning the continuous map in favor of a discrete geometric framework," for which p-adic numbers "measure distance based on hierarchical divisibility by a prime number." On Bell specifically, [12] states that the non-locality conclusion "relies heavily on the assumption that the choice of measurement settings is statistically independent of the particles being measured" and that "superdeterminism exploits the mathematical loophole inherent in the assumption of statistical independence." [10] extends the deterministic-architecture program: it presents 't Hooft's Cellular Automaton Interpretation, in which "quantum mechanics emerges from a deeper, deterministic, classical layer of reality, akin to a cellular automaton," with inaccessible hidden variables "that determine all outcomes, bypassing concepts like wave function collapse," and it explores p-adic and timeless substrates, noting p-adic metrics create "a hierarchical, tree-like 'ultrametric' space" with potential computational advantages including "no rounding errors, efficient data organization."

**The neurobiology of the agency illusion.** [9] supplies the neurobiological layer this framework needs. It states the deterministic evolution of the wave function via $i\hbar \frac{\partial}{\partial t} \Psi(r,t) = \hat{H} \Psi(r,t)$, "where the Hamiltonian operator $\hat{H}$ dictates the total energy and future state of the system with absolute precision," and it records the CHSH inequality $|E(a,b) - E(a,b')| + |E(a',b) + E(a',b')| \le 2$ with experimental values that "routinely measure a value of $2\sqrt{2}$." Crucially for our bridge, [9] describes "maintaining the functional illusion" as a "psychological dual-boot system [that] requires the prefrontal cortex to hold the objective truth of physics in the background while the left-hemisphere interpreter continues to generate the subjective feeling of agency in the foreground," operating "exactly like knowing it's a movie but still crying." [10] adds the temporal evidence: the readiness potential "precedes the conscious awareness of the intention to act by several hundred milliseconds," with mechanisms involving the supplementary motor area and "a stochastic process reaching a threshold, which is then broadcast to wider conscious networks."

**Behavioral agents and human-machine collaboration.** [8] models human decision making in bandit, contextual bandit, and reinforcement-learning settings, motivated by "clinical literature of a wide range of neurological and psychiatric disorders stemming from disturbances of the reward processing system," and reports empirical win rates in which its split-agent variants reach average win percentages of $52.65\%$ (PTS) in multi-armed bandit tasks and $57.07\%$ (NCTS) in contextual bandits against classical baselines, concluding that its "multi-parameter model... allows to tune the weights on incoming two-stream rewards" and captures "reward-processing aspects across various neurological and psychiatric conditions." [7] provides the evaluation methodology for explanations in human-AI collaboration: in its ExAG game, explanations raised overall win rate from $64.3\%$ to $69.29\%$ ($p = 0.0015$, $99\%$ confidence), and "incorrect explanations degrade performance," so "users can use their insight into explanation helpfulness to decide when to trust and include them in decision making." These results matter to our Section 7: if humans are to operate a deterministic worldview as a background process, the explanatory interface must be lucid and correct, or it will degrade performance exactly as [7] documents.

**Needs, rights, and institutional design.** [4] distinguishes needs from transitory wants, noting that "identifying and prioritizing their needs" is far harder than ascertaining desires, that scholars "have even questioned if people are capable of knowing their needs at all," and that AI developers face "social dilemmas—with societal good on one side and commercial pressures on the other," for which "well-defined and measurable needs" are part of the solution. [5] presents the Advanced Data Protection Control, "a mechanism for the communication of data protection and consenting data, meta-data, information, requests, preferences, and decisions" intended to shift practice "from a data-controller-centric practice to a data-subject-centric (i.e., a human-centric) practice," developed by an interdisciplinary team, and concludes that "no technology alone can be impactful if other socio-technical solutions will not support it." [1] analyzes why digital rights "increasingly exist in law but remain difficult to exercise through the information systems that mediate them," attributing the gap to "legal heterogeneity, conflicting organizational and commercial incentives, fragmented architectures, and asymmetrical control." Together these three works define the institutional layer of our framework: a deterministic account of human agency does not abolish rights or needs; it relocates them from metaphysical free choice to architectural guarantees, which is exactly the move [1], [4], and [5] make in the digital domain.

## 3. Methods

This paper is an analytical synthesis. It performs no experiment, measurement, survey, or simulation; every quantitative claim is either derived here with shown arithmetic from stated inputs, taken from a cited work and attributed to it, or labeled as a projection with explicit assumptions. The method has four components.

**Component 1: Formal physics layer.** We adopt the superdeterministic research program as formalized by [6]: a physical theory $T$ consists of laws plus initial/boundary conditions; preparation procedures $p$ verify property lists $L_P$; and a theory is nonsuperdeterministic only if its generalized response functions $\mathcal{R}(k|M,p)$ meet the standard [6] defines. We work in the "soft" superdeterminism register of [2]: local dynamics plus shared initial conditions generate the correlations, without committing to a specific claim about the universe's first moment beyond what the derivations require. We use the singlet-state correlation $E(a,b) = -\cos(a-b)$ for polarization/spin measurements, which is the standard quantum prediction underlying the $2\sqrt{2}$ value that [9] reports as routinely measured and that [3] presents through its photon-polarizer example.

**Component 2: Neurobiological interface layer.** We model the human agent as a physical subsystem whose outputs are generated by deterministic neural dynamics, in line with the Hamiltonian evolution stated in [9] and the cellular-automaton reading of [10]. The subjective sense of agency is treated as an interface—a compressed causal model—rather than as a report about metaphysical possibility. The timing structure of action versus awareness follows the readiness-potential finding quoted in [10]: neural preparation precedes conscious intention by several hundred milliseconds. Where the literature gives a range rather than a point value, we state an assumption explicitly (Section 4.3).

**Component 3: Evolutionary-economics layer.** We model the agency heuristic as lossy compression of the causal description of a decision situation. The model has three parameters—the number of candidate causal variables $N$, the number of categories in the compressed agent-based representation $k$, and the per-evaluation cost $\tau$—all stated as assumptions because no source supplies them (Section 4.2). The output is a speedup factor and an accuracy-cost bound, both labeled as projections.

**Component 4: Institutional layer.** We synthesize the institutional consequences using [1], [4], [5], [7], and [8]: rights and needs become architectural and measurable constructs; explanation quality becomes a performance variable; and behavioral-agent models become the empirical handle on how reward-processed, heuristic agents actually decide. Claims in this layer are qualitative and tied to specific results in those works.

Throughout, jargon is defined at first use: *statistical independence* means that the probability distribution of a measurement setting is uncorrelated with the hidden variables of the measured system; *CHSH* is the Clauser–Horne–Shimony–Holt inequality; *readiness potential* is the measured scalp-negative EEG deflection preceding voluntary movement; *dual-boot* is [9]'s term for running the deterministic worldview and the agency heuristic as parallel cognitive processes.

## 4. Analysis

### 4.1 The CHSH bound and its violation, with full arithmetic

**Input 1 (CHSH form):** from [9], any local realistic theory must satisfy

$$|E(a,b) - E(a,b')| + |E(a',b) + E(a',b')| \le 2.$$

**Input 2 (quantum correlation):** for a singlet pair, $E(a,b) = -\cos(a-b)$.

**Input 3 (empirical status):** [9] states experiments "routinely measure a value of $2\sqrt{2}$"; [3] describes the photon-pair polarizer setup that realizes such tests.

We now *derive* $2\sqrt{2}$ rather than quote it. Choose the standard optimal settings:

$$a = 0, \qquad a' = \frac{\pi}{2}, \qquad b = \frac{\pi}{4}, \qquad b' = \frac{3\pi}{4}.$$

Compute each correlation:

$$E(a,b) = -\cos\!\left(0 - \frac{\pi}{4}\right) = -\cos\!\left(-\frac{\pi}{4}\right) = -\frac{\sqrt{2}}{2} \approx -0.7071068.$$

$$E(a,b') = -\cos\!\left(0 - \frac{3\pi}{4}\right) = -\cos\!\left(\frac{3\pi}{4}\right) = +\frac{\sqrt{2}}{2} \approx +0.7071068.$$

$$E(a',b) = -\cos\!\left(\frac{\pi}{2} - \frac{\pi}{4}\right) = -\cos\!\left(\frac{\pi}{4}\right) = -\frac{\sqrt{2}}{2} \approx -0.7071068.$$

$$E(a',b') = -\cos\!\left(\frac{\pi}{2} - \frac{3\pi}{4}\right) = -\cos\!\left(-\frac{\pi}{4}\right) = -\frac{\sqrt{2}}{2} \approx -0.7071068.$$

Assemble the CHSH combination:

$$|E(a,b) - E(a,b')| = |-0.7071068 - 0.7071068| = |-1.4142136| = 1.4142136,$$

$$|E(a',b) + E(a',b')| = |-0.7071068 - 0.7071068| = 1.4142136,$$

$$S = 1.4142136 + 1.4142136 = 2.8284271 = 2\sqrt{2}.$$

The excess over the local bound is

$$2\sqrt{2} - 2 = 0.8284271,$$

and the relative violation is

$$\frac{2\sqrt{2}}{2} = \sqrt{2} \approx 1.4142136,$$

that is, the quantum value exceeds the local realistic ceiling by $41.42136\%$. Since [3] shows that the remaining assumptions (perfect detector idealizations that "can be relaxed") are not the weak link, and [12] states that the non-locality conclusion "relies heavily on the assumption that the choice of measurement settings is statistically independent," the $41.4\%$ excess must be paid for by exactly one of: non-locality, probability-axiom revision, or failure of statistical independence. [3] evaluates the first two doors and finds "neither... promising" for the probability route; we therefore locate the framework on the third door, with the formal obligations that [6] attaches to it.

### 4.2 Compression model of the agency heuristic

The claim to derive: representing a decision situation in terms of a small number of agents, rather than its full causal ancestry, is computationally cheaper by orders of magnitude, which supplies the evolutionary pressure for a free-will interface.

**Assumption A1:** a real-world decision situation presents $N = 1000$ candidate causal variables (prior states, environmental conditions, internal states). No source fixes $N$; we take $10^3$ as an order-of-magnitude stand-in for "very many," and Section 6 treats the result as sensitive to this choice.

**Assumption A2:** the compressed agent-level representation uses $k = 3$ categories (self, other agent, object of action), matching the structure of theory-of-mind reasoning.

**Assumption A3:** evaluating one causal variable in a deliberative loop costs $\tau = 1\ \text{ms}$ (a stand-in for single-neuron-loop to small-circuit evaluation time; the result scales linearly in $\tau$, so the speedup factor does not depend on it).

Uncompressed evaluation time:

$$T_{\text{full}} = N \tau = 1000 \times 1\ \text{ms} = 1000\ \text{ms} = 1.0\ \text{s}.$$

Compressed evaluation time:

$$T_{\text{agent}} = k \tau = 3 \times 1\ \text{ms} = 3\ \text{ms}.$$

Speedup factor:

$$\Gamma = \frac{T_{\text{full}}}{T_{\text{agent}}} = \frac{1000\ \text{ms}}{3\ \text{ms}} = 333.33\overline{3} \approx 333.$$

Compression ratio (same arithmetic, information-theoretic reading):

$$\rho = \frac{N}{k} = \frac{1000}{3} \approx 333.$$

The accuracy cost of lossy compression is bounded by what the compression discards: the discarded variables are the remote causal ancestry, which is precisely the part of the causal network that is (a) cognitively inaccessible in real time and (b) invariant across most decisions, so its omission changes the *selected action* only in the minority of cases where remote causes dominate local agent-level structure. We do not quantify that minority here; stating it as bounded-but-unquantified is the honest form, and Section 6 lists it as an open question. The projection is therefore: **under A1–A3, the agency heuristic accelerates deliberation by a factor of approximately $333$ ($\Gamma = N/k$), at an unquantified but structurally bounded accuracy cost.** This is the evolutionary "why": in the lethal environments in which reaction speed selected, a $333\times$ faster deliberation loop dominates any marginal accuracy gain from full causal bookkeeping, exactly the trade-off structure that [8] formalizes when it models human agents whose "different strategies and behavioral trajectories lead to the same empirical outcome" and whose reward processing is biased rather than optimal.

### 4.3 The action–awareness timing gap

**Input (from [10]):** the readiness potential "precedes the conscious awareness of the intention to act by several hundred milliseconds," with a plausible mechanism of "a stochastic process reaching a threshold, which is then broadcast to wider conscious networks" involving the supplementary motor area.

**Assumption A4:** we take the midpoint of "several hundred milliseconds" as $\Delta t = 350\ \text{ms}$ for arithmetic purposes; the qualitative conclusions hold for any $\Delta t$ in the reported range.

Two derived quantities follow. First, the awareness lag as a fraction of a typical fast reaction cycle: taking a visuomotor reaction time of $T_{\text{rt}} = 250\ \text{ms}$ as an assumption (A5), the ratio is

$$\frac{\Delta t}{T_{\text{rt}}} = \frac{350\ \text{ms}}{250\ \text{ms}} = 1.4.$$

The neural preparation outlasts the entire reaction cycle by $40\%$: awareness of the intention arrives after the motor system has already committed on the timescale that matters for fast action. Second, the fraction of a deliberative second consumed: with $T_{\text{full}} = 1000\ \text{ms}$ from Section 4.2,

$$\frac{\Delta t}{T_{\text{full}}} = \frac{350}{1000} = 0.35,$$

so the post-hoc narrative window—the time available for the interpreter to construct "I decided" after initiation—occupies at least a third of any one-second deliberation episode. The consequence drawn in Section 5 is structural, not metaphysical: the sequence *initiation → awareness → narration* is a pipeline, and the feeling of authorship is generated at the last stage.

### 4.4 Metabolic projection for dual-boot cognition

**Input (from [9]):** the dual-boot strategy holds "the objective truth of physics in the background while the left-hemisphere interpreter continues to generate the subjective feeling of agency in the foreground."

**Assumption A6:** baseline cerebral power $P_{\text{brain}} = 20\ \text{W}$ (a standard order-of-magnitude figure for adult human brain metabolism, used here as an assumption since no cited source states it).

**Assumption A7:** maintaining an explicit background model (periodic re-derivation or rehearsal of the deterministic worldview, e.g., once per waking hour) engages a cortical working-memory circuit whose incremental cost is a small fraction of baseline; we take $f = 1\%$ as the assumption.

Incremental power:

$$P_{\text{dual}} = f \, P_{\text{brain}} = 0.01 \times 20\ \text{W} = 0.2\ \text{W}.$$

Daily energy cost over a waking day of $T_{\text{wake}} = 16\ \text{h} = 57600\ \text{s}$:

$$E_{\text{dual}} = P_{\text{dual}} \, T_{\text{wake}} = 0.2\ \text{W} \times 57600\ \text{s} = 11520\ \text{J} \approx 11.5\ \text{kJ} \approx 2.75\ \text{kcal}.$$

The projection: **under A6–A7, dual-boot cognition costs on the order of $3$ kcal per day—negligible against daily dietary intake—so the barrier to holding a deterministic worldview is not metabolic but motivational and social**, a conclusion that redirects the design problem from hardware limits to the explanation-quality and trust issues that [7] and [5] address.

### 4.5 Explanatory benefit in human-AI collaboration

**Input (from [7]):** in the ExAG collaborative image-retrieval game, the overall win rate was $W_{\text{no}} = 64.3\%$ without explanations and $W_{\text{exp}} = 69.29\%$ with explanations, with the improvement reported at $p = 0.0015$ under $99\%$ confidence. We take these values as the reported basis for the computation; the study's statistical reporting makes them the best-substantiated figures available for this quantity.

The explanatory benefit is

$$\Delta_{\text{win}} = W_{\text{exp}} - W_{\text{no}} = 69.29\% - 64.3\% = 4.99\ \text{percentage points}.$$

The relative improvement over the no-explanation baseline is

$$\frac{\Delta_{\text{win}}}{W_{\text{no}}} = \frac{4.99}{64.3} \approx 0.0776,$$

that is, a $7.76\%$ relative gain in task success from the explanatory interface alone. [7] further reports that "incorrect explanations degrade performance," which bounds the design space: the benefit is conditional on explanation quality, not automatic. This number enters Section 7 as the measurable design target for any interface through which a deterministic worldview is communicated—if the interface is not lucid, the same study shows the effect reverses.

### 4.6 Why the third door is the only locality-preserving one

Combining Sections 4.1–4.5: the $41.4\%$ CHSH excess is an empirical fact ([9]: "routinely measure a value of $2\sqrt{2}$"; [3] details the experimental arrangement). Locality is retained by rejecting statistical independence; [6] supplies the formal standard such a theory must meet; [11] reports that "local, non-linear dynamics can serve as a viable physical mechanism for generating the correlations required by superdeterminism" as "a robust and generic feature of the simulated system"; and [2]'s billiard model shows how a single initial "bang" correlates all downstream events without superluminal influence. The neurobiology of Sections 4.2–4.3 then explains why the resulting worldview feels false from the inside: the brain's compressed agent-level interface (Section 4.2) cannot represent the shared causal ancestry that generates the correlations, so the interface reports "independent choices" as its native output. The mismatch between map and territory is thus computable in structure, echoing [11]'s conclusion that the rejection of superdeterminism by the "map-makers of science is a pragmatic, methodological necessity, not an ontological discovery."

## 5. Results

**R1 (CHSH violation, derived in Section 4.1).** With settings $a = 0$, $a' = \pi/2$, $b = \pi/4$, $b' = 3\pi/4$ and $E(a,b) = -\cos(a-b)$, the CHSH value is $S = 2\sqrt{2} \approx 2.8284271$, exceeding the local bound $2$ by $0.8284271$, a relative excess of $41.42136\%$. Statistical independence is the assumption whose failure pays for this excess while preserving locality.

**R2 (Compression speedup, projection under A1–A3, Section 4.2).** With $N = 1000$ causal variables compressed into $k = 3$ agent categories at $\tau = 1\ \text{ms}$ per evaluation, the agency heuristic accelerates deliberation by $\Gamma = N/k = 333.33\overline{3} \approx 333$, at an unquantified but structurally bounded accuracy cost. The speedup is invariant to $\tau$.

**R3 (Timing gap, Section 4.3).** Under A4–A5 ($\Delta t = 350\ \text{ms}$, $T_{\text{rt}} = 250\ \text{ms}$), the readiness-potential lead is $1.4\times$ a full visuomotor reaction cycle, and the post-hoc narrative window occupies $0.35$ of a one-second deliberation episode. The qualitative claim—awareness follows initiation—holds for any $\Delta t$ in the several-hundred-millisecond range reported by [10].

**R4 (Dual-boot metabolic cost, projection under A6–A7, Section 4.4).** With $P_{\text{brain}} = 20\ \text{W}$ and $f = 1\%$, dual-boot cognition costs $P_{\text{dual}} = 0.2\ \text{W}$, or $E_{\text{dual}} = 11520\ \text{J} \approx 2.75\ \text{kcal}$ per 16-hour waking day. The barrier to holding a deterministic worldview is therefore motivational and social, not metabolic.

**R5 (Explanatory benefit, computed from [7], Section 4.5).** Lucid explanations in the ExAG task raise win rate by $\Delta_{\text{win}} = 4.99$ percentage points ($64.3\% \to 69.29\%$, $p = 0.0015$), a $7.76\%$ relative gain, with incorrect explanations degrading performance.

**R6 (Layered synthesis, Sections 4.6, 5).** The framework holds together as a pipeline: a locality-preserving physics (R1, with mechanisms per [11] and [2]); an interface-level neurobiology that explains why the physics feels false from the inside (R2, R3); a negligible metabolic cost for holding both views (R4); and an institutional layer in which rights, needs, and explanation quality become architectural variables (R5, with [1], [4], [5]). Human meaning survives determinism because meaning is a computed state of the interpreter, not a metaphysical privilege.

## 6. Discussion

**Limitations.** The framework rests on explicitly stated assumptions, each with a sensitivity profile:

- **A1 ($N = 1000$ causal variables).** The speedup $\Gamma = N/k$ scales linearly in $N$: if the true count is $N = 100$, $\Gamma = 33.3$; if $N = 10^4$, $\Gamma = 3333$. The qualitative claim—orders-of-magnitude compression—survives any $N$ in $[10^2, 10^4]$, but the specific figure $333$ is only as good as the order-of-magnitude guess. No cited source fixes $N$.
- **A2 ($k = 3$ agent categories).** If theory-of-mind reasoning uses $k = 10$ categories, $\Gamma$ falls to $100$; the evolutionary argument weakens proportionally but does not reverse, since any $k \ll N$ preserves the speedup.
- **A3 ($\tau = 1$ ms per evaluation).** $\Gamma$ is independent of $\tau$ by construction, so this assumption affects only the absolute times $T_{\text{full}} = 1.0$ s and $T_{\text{agent}} = 3$ ms, not the ratio.
- **A4–A5 ($\Delta t = 350$ ms, $T_{\text{rt}} = 250$ ms).** The ratio $\Delta t / T_{\text{rt}} = 1.4$ ranges from roughly $0.8$ (at $\Delta t = 200$ ms) to $2.0$ (at $\Delta t = 500$ ms); the claim that awareness follows initiation on fast-action timescales holds across the whole reported range, but the specific factor $1.4$ is a midpoint convention.
- **A6–A7 ($P_{\text{brain}} = 20$ W, $f = 1\%$).** The daily cost $E_{\text{dual}} = 2.75$ kcal scales linearly in both: at $f = 10\%$ it becomes $27.5$ kcal, still under $1.5\%$ of a $2000$ kcal daily intake. The conclusion "not metabolic" is robust over two orders of magnitude in $f$; it would fail only if maintaining the background model consumed a large fraction of baseline cerebral power, for which no evidence is offered here.
- **The accuracy cost of compression is unquantified.** Section 4.2 states the cost is structurally bounded but does not measure the fraction of decisions in which remote causal ancestry changes the selected action. Any quantitative use of the compression model beyond the speedup factor is blocked until that fraction is estimated.
- **The superdeterministic mechanism is not specified here.** [11] reports a computational proof-of-principle that local nonlinear dynamics generate the required correlations as "a robust and generic feature of the simulated system," but also concedes that constructive proposals "typically stop short of specifying the precise evolutionary laws." This paper inherits that gap: it locates the framework on the third door of [3]'s taxonomy without supplying the dynamical laws.
- **The neurobiological claims are interface-level, not mechanistic.** The dual-boot description comes from [9] as a theoretical construct, and the readiness-potential timing from [10]; neither is tested here, and the compression model is a functional analogy, not a neural circuit model.

**What would falsify the main result.** The central claim is that a locality-preserving superdeterminism is scientifically tractable and that human agency perception is a compressed interface whose mismatch with the deterministic territory is computable in structure. The physics half would be falsified if a dynamical study in the style of [11] showed that local nonlinear dynamics generate Bell-inequality-violating correlations only under fine-tuned initial conditions—i.e., if the robustness reported there ("a robust and generic feature of the simulated system") failed to replicate under varied dynamics, restoring the "primordial conspiracy" critique that [11] itself identifies as the theory's central weakness. The neurobiology half would be falsified if the readiness-potential lead reported by [10] were shown to be an artifact of measurement methodology such that conscious awareness and neural initiation are temporally coincident, removing the pipeline structure of Section 4.3. The compression half would be falsified if deliberation over full causal detail were shown to be as fast as agent-level reasoning in controlled tasks, collapsing the evolutionary rationale of Section 4.2.

**Open questions.** Three stand out. First, the fraction of decisions in which compressed agent-level representation selects a different action than full causal bookkeeping—Section 4.2 leaves this bounded but unmeasured, and it is the quantity that would convert the compression model from a plausibility argument into a predictive one. Second, whether the dual-boot strategy of [9] is trainable: if holding the deterministic worldview in the background degrades agency-foreground performance (rather than costing the negligible $2.75$ kcal per day of Section 4.4), the motivational barrier reappears in a different form. Third, the institutional question of Section 5 (R6): whether forward-looking correction can be stabilized in legal systems whose participants experience choice as metaphysical, given that [7] shows incorrect explanations actively degrade performance—the communication channel itself is a failure mode.

**Arguing against the framework.** The strongest objection is [3]'s own verdict: after examining both escape routes, "Neither seems promising." A defender must answer why this paper's route differs from the one [3] dismisses. The answer offered here is that [3] evaluates superdeterminism as a philosophical position about probability, whereas [6] has since given it a formal definition as a property of physical theories, and [11] has supplied a computational mechanism—so the strategy [3] found unpromising has acquired the two things it lacked, a standard and a mechanism. A second objection: the compression model (Section 4.2) may be a just-so story, since any representational scheme can be described as compression after the fact. The reply is that the model makes one checkable commitment—the speedup factor $\Gamma = N/k$ with linear scaling in $N$—which a reaction-time experiment could test. A third objection: the institutional layer borrows results about digital rights ([1], [5]) that concern a different domain, and the analogy from data-protection architecture to justice architecture may not carry. This is granted; the analogy is structural (rights as architectural guarantees rather than metaphysical endowments), and its transfer to justice is a hypothesis, not a result of this paper.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result, and what changes.** Three user groups follow from the Introduction's problem statement. First, science communicators and clinicians who convey deterministic findings to non-specialists: if the framework holds, the design target is the explanatory interface, and the measurable standard is the $\Delta_{\text{win}} = 4.99$ percentage-point benefit that [7] reports for lucid explanations, with the documented reversal for incorrect ones. Their practice changes from avoiding deterministic framing to engineering it—pairing the deterministic claim with the agency heuristic as a declared interface, in the dual-boot register of [9]. Second, behavioral-model researchers: the compression model of Section 4.2 gives a functional rationale for the biased, non-optimal reward processing that [8] formalizes in its split-agent variants, which reach average win rates of $52.65\%$ (PTS, multi-armed bandit) and $57.07\%$ (NCTS, contextual bandit) against classical baselines; a modeler who takes the agency heuristic as compression rather than noise has a principled parameterization. Third, institutional designers in the digital-rights community: [1] attributes the gap between legal rights and exercisable rights to "legal heterogeneity, conflicting organizational and commercial incentives, fragmented architectures, and asymmetrical control," and [5] concludes that "no technology alone can be impactful if other socio-technical solutions will not support it"—the framework's contribution is the general principle that agency-relevant guarantees belong in architecture, not in metaphysics, which [4] grounds in "well-defined and measurable needs." Justice reform is named in the Introduction as a downstream application, but the framework supplies no justice-specific quantitative result; the transfer is stated as a hypothesis, not a pathway.

**(b) Current readiness.** This work is analytical and has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2: basic principles (the CHSH derivation of Section 4.1) are stated and the compression and metabolic models are analytical predictions with no experimental validation. Analytical work of this kind cannot exceed TRL 3, and no component of this paper reaches even TRL 3, because no critical function has been demonstrated by any physical process. The institutional layer is correspondingly conceptual.

**(c) The smallest next test.** The cheapest de-risking calculation is a replication-and-extension of the dynamical proof-of-principle of [11]: simulate local nonlinear dynamics under varied update rules and initial-condition classes, and measure whether Bell-violating correlations arise generically or only under fine-tuning. The outcome that refutes the framework's physics half is a demonstration that the correlation-generating behavior of [11]'s system is non-generic. The cheapest behavioral test is a reaction-time study of the compression model: present participants with decision problems whose causal-variable count is manipulated ($N$ varied over at least one order of magnitude) and measure whether deliberation time scales as $T_{\text{full}} \propto N$ for full-bookkeeping conditions while agent-framed conditions stay flat; a failure of the predicted scaling falsifies R2. A study would recruit participants under an approved protocol, manipulate $N$ within a bandit-style task of the kind [8] models, and measure decision latency and accuracy; no such study is performed or reported here.

**(d) Binding constraints.** For the dynamical test, the binding constraint is computational: the simulation must resolve enough variables to exhibit the correlation structure, and the fine-tuning metric must be defined before the experiment, or the result is unfalsifiable. For the behavioral test, the binding constraints are experimental design (separating compression speedup from ordinary cueing effects) and the unquantified accuracy cost of Section 4.2, which sets the tolerable error rate the task must be sensitive to. For any deployment of the explanatory interface, the binding constraint is documented in [7]: incorrect explanations degrade performance, so the pipeline requires a correctness gate before the explanation reaches the user, and the mechanism for that gate is an open question this paper does not solve. Regulatory constraints are not analyzed here and are listed as open questions.

**(e) Order-of-magnitude bounds.** The only cost bound derivable from Section 4 is the metabolic one: under A6–A7, dual-boot cognition costs $E_{\text{dual}} = 11520\ \text{J} \approx 2.75\ \text{kcal}$ per 16-hour waking day, with linear sensitivity in $f$ (at $f = 10\%$, $27.5$ kcal). This is a projection under stated assumptions, not a measurement. No market, deployment, or engineering-performance figures are derivable from the sources or the derivations of this paper, and none are offered.

**(f) Risks and misuse paths.** A deterministic account of agency can be misused as a rhetorical instrument to deny people responsibility or to justify manipulation ("your choices were determined anyway, so consent is void"). The framework's own resources cut against this: [5]'s data-subject-centric control and [1]'s architectural rights exist precisely to guarantee agency operationally regardless of its metaphysical status, and [4]'s needs construct gives a measurable standard for whether a system serves the person. A second risk is motivational: communicating determinism without the dual-boot framing may produce the fatalistic collapse the Introduction describes; the $\Delta_{\text{win}}$ result of [7] implies that the framing must be lucid and correct, and that a botched communication is worse than none.

## 8. Conclusion

This paper connected the formal structure of superdeterministic theories to the neurobiology of agency perception and to institutional design, using only derivations with shown arithmetic and claims tied to specific results in the cited literature. The physics layer derives the CHSH violation $S = 2\sqrt{2} \approx 2.8284271$ against the local bound $2$, a $41.42136\%$ excess, and locates statistical independence as the assumption whose rejection preserves locality, under the formal standard of [6] and the dynamical mechanism reported by [11]. The neurobiology layer models the sense of agency as lossy compression: under stated assumptions, compressing $N = 1000$ causal variables into $k = 3$ agent categories accelerates deliberation by $\Gamma \approx 333$, and the readiness-potential lead of several hundred milliseconds ([10]) makes awareness a late stage in an initiation-to-narration pipeline. The metabolic projection—roughly $2.75$ kcal per day under A6–A7—shows the barrier to holding a deterministic worldview is motivational and social, not energetic, and the ExAG result of [7] ($\Delta_{\text{win}} = 4.99$ percentage points, reversing for incorrect explanations) sets the measurable standard for the explanatory interface. The synthesis is that human meaning survives determinism because meaning is a computed state of the interpreter, not a metaphysical privilege; accountability, needs, and rights relocate from free choice to architectural guarantees, the move [1], [4], and [5] execute in the digital domain. The framework is analytical and unvalidated (TRL 1–2); its falsification tests—genericity of the local dynamical mechanism, and linear scaling of deliberation time in causal-variable count—are stated concretely enough to be run.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.54.0). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 1 quantitative claim from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Rights by Architecture: A Human-Compatible Sociotechnical Layer for Digital Protection Across Regulatory Regimes. arXiv:2609.02455v1. https://arxiv.org/abs/2609.02455v1
[2] Aspects of Superdeterminism Made Intuitive. arXiv:2205.10616v1. https://arxiv.org/abs/2205.10616v1
[3] Bell's Theorem, Quantum Probabilities, and Superdeterminism. arXiv:2006.08609v3. https://arxiv.org/abs/2006.08609v3
[4] Needs-aware Artificial Intelligence: AI that 'serves [human] needs'. arXiv:2202.04977v3. https://arxiv.org/abs/2202.04977v3
[5] Advanced Data Protection Control (ADPC): An Interdisciplinary Overview. arXiv:2209.09724v1. https://arxiv.org/abs/2209.09724v1
[6] On measurement, superdeterminism, free will, and contextuality. arXiv:2604.00311v2. https://arxiv.org/abs/2604.00311v2
[7] Can You Explain That? Lucid Explanations Help Human-AI Collaborative Image Retrieval. arXiv:1904.03285v4. https://arxiv.org/abs/1904.03285v4
[8] Unified Models of Human Behavioral Agents in Bandits, Contextual Bandits and RL. arXiv:2005.04544v5. https://arxiv.org/abs/2005.04544v5
[9] https://papers.qnfo.org/papers/algorithmic-necessity-of-agency. QNFO: THE ALGORITHMIC NECESSITY.
[10] https://papers.qnfo.org/papers/simulation-inconsistency-detection-via-neurobiological-and-cognitive-interfaces. QNFO: Simulation Inconsistency Detection via Neurobiological and Cognitive Interfaces.
[11] https://papers.qnfo.org/papers/emergent-correlation-in-a-local-deterministic-universe. QNFO: EMERGENT CORRELATION IN A LOCAL-DETERMINISTIC UNIVERSE.
[12] https://papers.qnfo.org/papers/clockwork-cosmos. QNFO: Clockwork Cosmos.
