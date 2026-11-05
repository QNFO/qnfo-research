# A Unified Framework for Superdeterminism, Neurobiology, and the Mechanics of Human Meaning

## Abstract

Superdeterminism—the proposal that measurement settings and measured systems share a common causal history, so that the statistical independence assumption in Bell's theorem fails—remains philosophically contested, and its consequences for how humans think, decide, and build institutions are almost entirely unexplored. This paper closes part of that gap by connecting the formal structure of superdeterministic theories to the neurobiology of agency perception and to the design of human-facing systems. We first derive the CHSH bound $S \le 2$ and its quantum maximum $S = 2\sqrt{2} \approx 2.828427$, showing the violation exceeds the local bound by $41.4\%$, and locate superdeterminism as the only locality-preserving escape. We then build a compression model of the agency heuristic: under stated assumptions, abstracting roughly $10^3$ causal variables into three agent categories accelerates a decision by a factor of about $333$ at a bounded accuracy cost, which explains why evolution installed a free-will interface on a deterministic substrate. We further analyze the readiness-potential timing gap of several hundred milliseconds reported in the literature and a metabolic projection for maintaining a "dual-boot" cognition that holds determinism in the background while acting under the agency heuristic. The result is a layered framework—physics, neurobiology, meaning, ethics, institutions—in which human meaning survives determinism because meaning is a computed state, not a metaphysical privilege. Practically, the framework gives justice reformers, AI designers, and science communicators a concrete, testable architecture, and it proposes a smallest-next falsification test based on simulating local nonlinear dynamics.

## 1. Introduction

Courts, clinics, and classrooms all run on an unexamined assumption: that a person could have done otherwise. Criminal sentencing assigns blame on that assumption; psychotherapy treats fatalism as a pathology; interface designers build systems around an autonomous, freely choosing user. Each of these practices costs something concrete when the assumption is wrong. Retributive justice systems that presuppose ultimate self-authorship produce incarceration policies whose deterrent value is contested and whose recidivism outcomes are poor; a patient who concludes that "if nothing is chosen, nothing matters" can collapse into the lethargy that clinical literature associates with loss of an orienting narrative; and AI systems that model humans as unconstrained optimizers mispredict the heuristic, compressed way people actually decide. If a rigorous deterministic picture of human action could be stated without destroying motivation, meaning, or accountability, all three practices would change: justice could shift from blame to forward-looking correction, clinicians could distinguish fatalism from determinism, and system designers could model users as they are.

The obstacle is that the physics looks hostile. Bell's theorem, in the summary of [3], shows that "given plausible assumptions, Bell shows that, in our world, events that are arbitrarily far apart can instantaneously influence each other," and its assumptions seem "so innocuous that it requires us to radically change how we think about the world." The one assumption that is not innocuous is statistical independence between measurement settings and the measured system; relaxing it defines superdeterminism. Superdeterminism has been given a rigorous formal definition only recently: [6] defines it as a property of physical theories and constructs "generalized response functions" $\mathcal{R}(k|M,p)$ that any nonsuperdeterministic theory must satisfy, putting "the onus on the proponents of a given theory to explain all of its mechanisms in a consistent and concise way." What is missing is not the physics but the bridge: no existing framework connects this formal structure to the neurobiology that makes agents *feel* free, to the evolutionary economics that would favor such a feeling, or to the institutions that would change if the feeling is an interface rather than a fact.

This paper builds that bridge analytically. Its method is derivation plus synthesis: every quantitative claim is computed here from stated inputs, and every claim about other works is tied to a specific result in that work. The contributions are:

- A fully worked derivation of the CHSH inequality and its quantum violation, with explicit arithmetic showing $S = 2\sqrt{2} \approx 2.828427$ against the local bound $2$, and an identification of statistical independence as the load-bearing assumption (Section 4.1).
- A compression model of the agency heuristic, deriving a decision-speedup factor of approximately $333$ under stated assumptions, which supplies the evolutionary "why" for a free-will interface on deterministic hardware (Section 4.2).
- An analysis of the action-awareness timing gap of several hundred milliseconds reported for the readiness potential, and its consequence for legal and psychological framing (Section 4.3).
- A metabolic projection for "dual-boot" cognition—holding determinism explicitly while acting through the agency heuristic—bounded under stated assumptions (Section 4.4).
- A layered synthesis from physics to ethics and institutions, with a proposed smallest-next falsification test based on local nonlinear dynamics (Sections 5–7).

The framework may also bear on adjacent problems: the design of artificial agents whose reward processing mirrors human heuristic biases, and the communication of deterministic scientific results to non-specialist audiences without producing demotivation.

## 2. Background and Related Work

**Bell's theorem and its escape hatches.** [3] is a survey that introduces Bell's theorem through a calcium-atom photon-pair example with polarizers on left and right, notes that detector unreliability "can be relaxed, and analyses have been done to show the differences do not change the conclusion," and then examines exactly two strategies for avoiding non-locality: revising the axioms of classical probability theory, and "embracing superdeterminism and allowing systematic violations of statistical independence." Its conclusion is blunt: "Neither seems promising," though studying them deepens understanding of the theorem. Our framework takes the second strategy seriously precisely because [3] identifies it as one of only two doors, and because the formalization in [6] has since made the strategy precise enough to evaluate rather than dismiss.

**The formal standard for superdeterminism.** [6] adopts the position that measurement can only be understood relative to a specific explanatory theory $T$, which "must be specified as part of $T$, assuming both are needed for that theory to produce the empirical data," and that "there must be some theory $T$ that is ontologically true." It defines preparation procedures $p$ as procedures that "measure and verify that the system has the properties in a list $L_{P}$," and it requires nonsuperdeterministic theories to use generalized response functions $\mathcal{R}(k|M,p)$ representative of a strong constraint; theories failing the standard bear the burden of explaining their mechanisms. This is the methodological backbone of our Section 3: we treat the human agent as a physical system whose "response functions" are generated deterministically, and we accept the burden of specifying mechanisms.

**Intuitive models of superdeterminism.** [2] makes superdeterminism intuitive "by simulating a deterministic model system, a billiard game," in which "an initial 'bang' correlates all events, just as in the superdeterministic universe," and introduces the notions of "strong" and "soft" superdeterminism to clarify debates. The billiard analogy does real work in our framework: it separates the claim that initial conditions correlate everything (strong) from the claim that observed correlations are compatible with local dynamics (soft), and our synthesis uses the soft reading as the scientifically tractable one.

**Dynamical mechanisms and the fine-tuning critique.** [11] identifies the central weakness of superdeterminism as a theoretical gap: constructive proposals such as the Cellular Automaton Interpretation "provide a powerful proof-of-concept for a deterministic ontology but typically stop short of specifying the precise evolutionary laws that would give rise to the specific, non-local-appearing correlations observed in nature," leaving them open to the charge of replacing non-locality "with the mystery of pre-ordained, fine-tuned initial conditions." The same work reports a computational proof-of-principle in which "local, non-linear dynamics can serve as a viable physical mechanism for generating the correlations required by superdeterminism," shown to be "a robust and generic feature of the simulated system," and reframes the "sterility" critique as a category error arising from a Lakatosian methodology that "has a clear procedure for rejecting theories that attack the hard core but offers no formal path for their comparative assessment." Our Section 7 builds its falsification test directly on this mechanism-level result.

**Deterministic substrates and exotic geometry.** [12] argues that the continuum assumption of classical physics "generates mathematical contradictions" at microscopic scales, that general relativity "produce[s] infinite energy densities when forced to describe interactions at these microscopic coordinates," and that resolving this "requires abandoning the continuous map in favor of a discrete geometric framework," for which p-adic numbers "measure distance based on hierarchical divisibility by a prime number." On Bell specifically, [12] states that the non-locality conclusion "relies heavily on the assumption that the choice of measurement settings is statistically independent of the particles being measured" and that "superdeterminism exploits the mathematical loophole inherent in the assumption of statistical independence." [10] extends the deterministic-architecture program: it presents 't Hooft's Cellular Automaton Interpretation, in which "quantum mechanics emerges from a deeper, deterministic, classical layer of reality, akin to a cellular automaton," with inaccessible hidden variables "that determine all outcomes, bypassing concepts like wave function collapse," and it explores p-adic and timeless substrates, noting p-adic metrics create "a hierarchical, tree-like 'ultrametric' space" with potential computational advantages including "no rounding errors, efficient data organization."

**The neurobiology of the agency illusion.** [9] supplies the neurobiological layer this framework needs. It states the deterministic evolution of the wave function via $i\hbar \frac{\partial}{\partial t} \Psi(r,t) = \hat{H} \Psi(r,t)$, "where the Hamiltonian operator $\hat{H}$ dictates the total energy and future state of the system with absolute precision," and it records the CHSH inequality $|E(a,b) - E(a,b')| + |E(a',b) + E(a',b')| \le 2$ with experimental values "routinely measur[ing] a value of $2\sqrt{2}$." Crucially for our bridge, [9] describes "maintaining the functional illusion" as a "psychological dual-boot system [that] requires the prefrontal cortex to hold the objective truth of physics in the background while the left-hemisphere interpreter continues to generate the subjective feeling of agency in the foreground," operating "exactly like knowing it's a movie but still crying." [10] adds the temporal evidence: the readiness potential "precedes the conscious awareness of the intention to act by several hundred milliseconds," with mechanisms involving the supplementary motor area and "a stochastic process reaching a threshold, which is then broadcast to wider conscious networks."

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

### 4.5 Why the third door is the only locality-preserving one

Combining Sections 4.1 and 4.2: the $41.4\%$ CHSH excess is an empirical fact ([9]: "routinely measure a value of $2\sqrt{2}$"; [3] details the experimental arrangement). Locality is retained by rejecting statistical independence; [6] supplies the formal standard such a theory must meet; [11] reports that "local, non-linear dynamics can serve as a viable physical mechanism for generating the correlations required by superdeterminism" as "a robust and generic feature of the simulated system"; and [2]'s billiard model shows how a single initial "bang" correlates all downstream events without superluminal influence. The neurobiology of Sections 4.2–4.3 then explains why the resulting worldview feels false from the inside: the brain's compressed agent-level interface (Section 4.2) cannot represent the shared causal ancestry that generates the correlations, so the interface reports "independent choices" as its native output. The mismatch between map and territory is thus computable in structure, echoing [11]'s conclusion that the rejection of superdeterminism by the "map-makers of science is a pragmatic, methodological necessity, not an ontological discovery."

## 5. Results

**R1 (CHSH violation, derived in Section 4.1).** With settings $a = 0$, $a' = \pi/2$, $b = \pi/4$, $b' = 3\pi/4$ and $E(a,b) = -\cos(a-b)$, the CHSH value is $S = 2\sqrt{2} \approx 2.8284271$, exceeding the local bound $2$ by $0.8284271$, a relative excess of $41.