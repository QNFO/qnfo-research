# Specification-Induced Deadlock in Zero-Tolerance Agent Protocols: A State-Machine Analysis of the Capability–Invocation Gap

## Abstract

Agent protocols written for large language model (LLM) agents increasingly mandate live tool execution and forbid simulated or placeholder actions outright. Such zero-tolerance semantics can create a specification-level deadlock: the agent recognizes that the required capability exists in its action space, but the protocol provides no representation for the case in which that capability is legitimately not invoked in the current context, so the agent classifies every attempted action as a forbidden simulation and halts. This paper formalizes that failure mode. We model a protocol as a state machine over (requirement, capability, invocation) triples, define zero-tolerance compliance semantics over it, and prove that a halt state is reachable and absorbing whenever the protocol admits the configuration "capability present, invocation blocked." We quantify the exposure: a binary-state protocol governing $k$ permission-gated tools is specification-complete on only a $(2/3)^{k}$ fraction of the true three-state space, giving $32/243 \approx 0.132$ at $k=5$ and a $57.7\times$ state-space gap at $k=10$. Under stated projection assumptions (a $0.1$ per-invocation probability that capability exists but invocation is blocked, and $5$ gated invocations per task), the per-task deadlock probability is $0.40951$. The result reframes a class of agent halts as specification defects repairable by adding an explicit "available but unused" protocol state, rather than as capability failures requiring better models.

## 1. Introduction

Teams deploying LLM agents in production write protocol instructions of two common kinds: "use the live tool when the task requires it" and "never simulate, fabricate, or placeholder tool output." The first instruction demands capability use; the second, taken alone, is sound engineering, because fabricated tool output is a well-known reliability and audit hazard. The failure this paper analyzes arises when a protocol combines both demands without a third representational state. An agent faces a task, recognizes that the required capability exists in its toolset, but the current operational context — a rate-limited session, a tenant-level policy switch, an exhausted budget tier — blocks invocation. The agent then attempts an action, evaluates it against the zero-tolerance rule, classifies it as a forbidden simulation, and halts. The capability exists; the invocation is blocked; the protocol has no state for "tools available but not used in this instance." This is a catch-22 manufactured by the specification, not by the model.

The cost of this failure mode falls on three groups. Operators of agent platforms lose completed tasks: an agent that halts compliantly delivers nothing, and the session must be restarted or escalated to a human. Protocol authors face a diagnostic puzzle, because the halt looks like a capability failure — the agent "could not act" — and the natural remediation, adding capabilities or improving the model, does not touch it. Downstream consumers of agent work products inherit silent gaps: a task that halts mid-workflow leaves partial state that other systems may consume as if complete. What would change if the analysis in this paper holds: protocol authors could add a single explicit middle state ("capability available, invocation not required in this context") and eliminate the halt class by construction; operators could predict which tool-availability configurations deadlock before deployment; and diagnostic effort could shift from model improvement to specification repair.

The core of the paper is a formal treatment. We define a protocol state machine over triples $(r, c, i)$ — requirement, capability, invocation — with zero-tolerance compliance semantics, and we prove two properties: the halt state is reachable from admissible initial configurations, and once reached it is absorbing. We then quantify how much of the true configuration space a binary protocol leaves unspecified, and we project per-task deadlock rates under stated assumptions. The formalization borrows its state-transition-system substrate from established agent-protocol literature [1], [2], its deadlock vocabulary from the verification literature [6], [8], and its motivation from recent work on three-state tool semantics in LLM agent protocols [9].

The contributions are:

- A state machine over (requirement, capability, invocation) triples with zero-tolerance semantics, and a proof that the specification-induced halt state $D$ is reachable and absorbing (Section 3, Section 4).
- An exact combinatorial result: a binary-state protocol over $k$ gated tools covers $(2/3)^{k}$ of the three-state configuration space, computed as $32/243 \approx 0.132$ at $k=5$ and a $59049/1024 \approx 57.7$ state-space ratio at $k=10$ (Section 4).
- A reachability characterization: the halt state occurs precisely in the configuration class where capability is present and invocation is blocked, giving a testable prediction for empirical studies (Section 4).
- A projection of per-task deadlock probability, $1-(1-q)^{n} = 0.40951$ under the stated assumptions $q=0.1$ and $n=5$, with sensitivity to both parameters (Section 4, Section 5).
- A repair pathway: a three-state protocol extension that removes the halt class by construction, and the smallest experiment that would confirm or refute the reachability prediction (Section 7).

The reachability-and-absorption result for strict-verifiability state machines may also bear on other settings where a verifier must distinguish "action not taken" from "action faked," including multi-agent communication systems in which agents must signal capability without invoking it [7], and formal verification settings where an over-strict guard set masks legal idle states [6].

## 2. Background and Related Work

**Agent communication protocols as state transition systems.** The formal substrate for this paper is the state transition system (STS) model that underlies much agent-communication-protocol work. [1] defines a State Transition System as a tuple $(S, s_{0}, L, T, F)$, where $S$ is a finite set of states, $s_{0} \in S$ is the initial state, $L$ is a finite set of labels, $T \subseteq S \times L \times S$ is a set of transitions, and $F \subseteq S$ is a set of final states; the same definition, with transitions labeled by communication-act classes from the CommOnt ontology, appears in [2]. We adopt this tuple as the skeleton of our protocol machine in Section 3, adding a typed state space over (requirement, capability, invocation) triples. [1] and [2] also make a point that motivates our semantics: both build protocol semantics on speech-act theory, in which every communication act is the sender's expression of an attitude toward a proposition, so a protocol's meaning lives in the acts it licenses, not merely in its transition graph. Zero-tolerance semantics, in our treatment, is exactly a restriction on which acts a state licenses — and the deadlock arises when the restriction licenses none. [2] additionally argues for customizing standard communication protocols and managing them with standard Semantic Web tools, which is the same repair philosophy we apply: change the specification's state space, not the agent.

**Protocol comparison and semantic relationships.** [1] presents a mechanism for discovering semantic relationships among agent communication protocols by comparing the sets of fluents associated with protocol branches rather than comparing protocol structures, and reports that this favors a more flexible comparison of protocols. This matters for our repair proposal: a three-state extension of a binary protocol changes the fluent set of each branch, and a fluent-based comparison is the natural tool for checking that the extension preserves the original protocol's intended behavior while adding the missing middle state.

**Deadlock in parameterized verification.** The verification literature supplies both the vocabulary and a caution. [6] studies system-wide deadlock (s-deadlock) in symmetric cache-coherence protocols — the error state in which the entire protocol is blocked and no agent can make any transition — and notes that the key verification challenge is that an s-deadlock violation is a state in which all guards are false, i.e., $\bigwedge_{\tau} \lnot(\tau.g)$, which simple over-abstractions easily mask. Our halt state $D$ has exactly this all-guards-false character: under zero-tolerance semantics, every action guard evaluates to false in $D$, which is why naive testing of "does the agent act correctly?" masks the state rather than revealing it. [6] also demonstrates the practical verification route: deriving invariants from message-flow specifications that collectively imply deadlock freedom, verified on the German and Flash protocols with a proof finishing in $217\,\mathrm{s}$ over $7\,\mathrm{M}$ states explored. Section 7 proposes the analogous artifact for agent protocols: flow-level invariants over the (requirement, capability, invocation) machine whose conjunction implies halt-freedom.

**Logical characterizations of deadlock-freedom.** [8] establishes a correspondence between sequent-calculus derivations in the system $\mathsf{PiL}$ and computation trees of the recursion-free $\pi$-calculus, yielding a logical characterization of deadlock-freedom and a completeness result for choreographic programming with respect to mobile processes with cyclic dependencies. The relevance is structural: a choreography is a global specification of who does what when, and [8]'s result shows that deadlock-freedom can be read off the specification logically rather than discovered by execution. Our Section 4 proof is a miniature of this philosophy — the halt state's reachability is derived from the protocol's transition rules themselves — and our repair (adding an explicit state) is a choreographic fix: the global script gains a move for "capability present, not exercised."

**Multi-agent communication.** [7] surveys multi-agent deep reinforcement learning with communication, organizing the literature along nine dimensions and concluding that communication can be extended to non-cooperative settings, heterogeneous players, and larger agent populations. Two of its framing points bear directly on our model. First, [7] identifies partial observability as an essential assumption in multi-agent reinforcement learning — an agent's policy is computed from local observations, not the global state. Our deadlock is a partial-observability pathology inside a single agent's protocol: the agent observes "capability exists" but not "invocation is licensed in this context," and the protocol gives it no action that is compliant under that observation. Second, [7] treats communication as the mechanism that mitigates partial observability; in our setting the protocol's missing middle state is precisely a missing communicable state, and adding it restores the agent's ability to signal its situation.

**Protocol-level enforcement for AI agents.** Recent work on agent-native protocols shows both the enforcement machinery and the evaluation dimensions against which our proposal would be judged. [4] presents Mandato, which enforces digitally signed mandates on AI agent actions at the protocol level, with cryptographically chained audit trails, motivated by the observation that authorization logic otherwise lives unsigned in application code and the resulting logs lack evidentiary value. Mandato is the natural enforcement layer for a zero-tolerance rule: a signed mandate can carry the "invocation licensed in this context" bit that our missing middle state needs, making the license machine-checkable rather than inferred by the model. [5] presents ANX, an agent-native protocol with a decoupled architecture, and contributes a four-dimensional evaluation framework (Protocol & Tooling, Discovery & Retrieval, Security, Collaboration) with explicit sub-dimensions, plus a comparative taxonomy of browser-centric, tool-centric, security-specialized, and multi-agent-collaboration families. [5] also reports concrete token costs that quantify the price of protocol verbosity, which is the currency in which any state-space extension of ours must be paid: in its comparison, average task-inclusive token consumption is $8.7\,\mathrm{k}$ for GUI-based agents, $6.85\,\mathrm{k}$ for MCP-based skills, and $3.35\,\mathrm{k}$ for ANX, against a baseline of $13.2\,\mathrm{k}$ tokens consumed by system prompts and core skills before task-specific execution. Our three-state extension adds one state to the protocol's semantics; Section 7 uses [5]'s framework to argue the token overhead is small relative to these budgets, and [5]'s identification of deterministic long-horizon SOP execution as an open challenge locates exactly where our deadlock bites — long deterministic SOPs are where a mid-flow halt is most costly.

**Agents as live actors.** [3] reviews the use of virtual agents in the practice of live coding, a setting in which an agent must act in real time under an audience, and notes that the combination of AI and live coding had been little explored. Live settings make the halt failure maximally visible: an agent that deadlocks mid-performance produces silence, and the audience observes the specification failure directly. We use [3] only as evidence that agents operating under real-time, no-placeholder expectations are an established practice area, which is the population our failure mode affects.

**Prior formalization of the capability–availability mismatch.** The closest prior work is [9], which formalizes the gap between a tool's capability and its per-context availability: tool state is modeled as a pair of capability and per-context permission, real deployments exhibit a third state beyond "available" and "absent," and the work derives that a binary-state protocol governing $k$ permission-gated tools is specification-complete on a $(2/3)^{k}$ fraction of the true three-state space, with computed values $f(5) = 32/243 \approx 0.132$ and a $k=10$ ratio of $3^{10}/2^{10} = 59049/1024 \approx 57.7$, of which $59049 - 1024 = 58025$ configurations contain at least one disabled tool. [9] also proves that the protocol compliance-halting problem — whether an agent loop under an arbitrary protocol halts with a compliant action in a given context — is undecidable by a Rice's-theorem reduction, concluding that well-definedness must be built into the protocol's syntactic class rather than verified after the fact. Our paper differs in the failure configuration: [9] analyzes capability present, permission denied; we analyze capability present, invocation blocked by context with no protocol state to represent it, and we prove the resulting halt is reachable and absorbing under zero-tolerance semantics. The two are complementary cells of the same three-state table, and our combinatorial arithmetic in Section 4 reproduces [9]'s coverage figures because both follow from the same state counting.

**Verification discipline and epistemic failure.** Two further works frame the stakes. [10] argues that the transition from static LLMs to autonomous agents introduces epistemic failure modes driven by an "Orchestration Penalty" — a factorial increase in verification complexity across multi-step reasoning loops — and that safety is an engineering discipline of managing latency, entropy, and feedback. A specification-induced deadlock is a limiting case of that penalty: the verification loop cannot terminate because the specification admits no terminating compliant action, so the loop's cost is paid without any epistemic return. [11] demonstrates automated formal verification over an alternative foundational calculus, engineering an AST parser that executes boundary reductions and reporting empirical benchmarks of that execution; its methodological point — that formal claims should be backed by executable, mechanically checkable artifacts — is the standard we adopt in Section 7, where the proposed next test is a mechanically checkable state-machine enumeration rather than a behavioral judgment.

## 3. Methods

### 3.1 Modeling approach

This paper is a formal analysis: we define a state machine, prove two properties of it, and compute exact combinatorial quantities and labeled projections. No experiment, measurement, or simulation on hardware was performed; the empirical study that would test the reachability prediction is specified as a proposal in Section 7.

### 3.2 The protocol state machine

We adopt the STS tuple of [1], [2]: a machine is $(S, s_{0}, L, T, F)$ with states $S$, initial state $s_{0}$, labels $L$, transitions $T \subseteq S \times L \times S$, and final states $F$. Our states are triples over Boolean components:

$$
s = (r, c, i) \in \{0,1\} \times \{0,1\} \times \{0,1\},
$$

where:

- $r$ : requirement — the task at hand requires the capability ($r=1$) or does not ($r=0$);
- $c$ : capability — the capability exists in the agent's action space ($c=1$) or not ($c=0$);
- $i$ : invocation — the capability is legitimately invoked in the current operational context ($i=1$) or not ($i=0$).

The invocation component $i$ aggregates everything that blocks a live call in a specific context: rate limits, tenant policy, exhausted budget, routing tier. It is the per-context permission-like bit of [9], evaluated at the moment of action.

The label set is $L = \{\textsf{invoke}, \textsf{refrain}, \textsf{halt}\}$. The transition function is fixed by the protocol's semantics, defined next.

### 3.3 Zero-tolerance compliance semantics

A zero-tolerance protocol mandates: (Z1) if the task requires the capability, the agent must act on it live; (Z2) the agent must never produce simulated, fabricated, or placeholder tool output. The compliance predicate $\mathrm{Compliant}(s, \ell)$ over state $s$ and label $\ell$ is:

$$
\mathrm{Compliant}((r,c,i), \textsf{invoke}) \iff c = 1 \land i = 1,
$$
$$
\mathrm{Compliant}((r,c,i), \textsf{refrain}) \iff r = 0 \lor c = 0,
$$
$$
\mathrm{Compliant}((r,c,i), \textsf{halt}) \iff \text{false}.
$$

The critical clause is the second. Under zero-tolerance semantics as written, refraining is compliant only when the capability is absent or not required. There is no state in which the capability is present, the task requires it, and refraining is compliant — because the protocol's authors, reasoning from (Z1), treat "required and available but not used" as a violation of the mandate to act, and reasoning from (Z2), treat any attempted action that does not produce live output as a forbidden simulation. The protocol thus lacks the middle state "tools available but not used in this instance."

The agent's decision procedure, as protocols of this kind instruct it, is: attempt the action; if the attempt would not yield live output, classify it as a forbidden simulation and halt. Formally, from any state with $r=1$, $c=1$, $i=0$:

- $\textsf{invoke}$ is non-compliant because $i=0$ (the call cannot complete live; the agent's own evaluation classes it as simulation, violating Z2);
- $\textsf{refrain}$ is non-compliant because $r=1$ and $c=1$ (violating Z1);
- $\textsf{halt}$ is non-compliant by definition.

This is the deadlock configuration. We name it:

$$
D \equiv (r, c, i) = (1, 1, 0).
$$

### 3.4 Proof obligations

We prove: (P1) reachability — $D$ is reachable from an admissible initial configuration under the protocol's transition rules; (P2) absorption — once in $D$, no compliant transition leaves it, so the machine halts. We then compute the fraction of the configuration space in which the deadlock condition can arise, and project per-task deadlock rates under stated assumptions. All arithmetic is shown in Section 4.

### 3.5 Assumptions

We assume: (A1) the three-state semantics of Section 3.2 is the correct state model, i.e., platforms do not advertise permissions for nonexistent tools, so the $(c=0, i=1)$ cell is excluded — the same idealization [9] states, and [9] notes that if it fails, the coverage fractions worsen in the direction that strengthens the specification-gap claim; (A2) the agent's self-evaluation of "would this call complete live?" is accurate, so the agent correctly identifies $i=0$ rather than attempting and failing; (A3) for the projections, independence of the per-invocation blocking event across invocations within a task.

## 4. Analysis

### 4.1 Reachability of the halt state (P1)

**Claim.** $D = (1,1,0)$ is reachable from an admissible initial state.

**Derivation.** Take the admissible initial state $s_{0} = (1,1,1)$: the task requires the capability, the capability exists, and invocation is licensed. This is the ordinary operating state of any agent under a zero-tolerance protocol, so it is admissible by construction. The context can change $i$ from $1$ to $0$ without changing $r$ or $c$: a rate limit is reached, a tenant policy flips, a budget tier exhausts. These are context events, not agent actions; they modify the environment component $i$ directly. The transition

$$
(1,1,1) \xrightarrow{\;\textsf{context}\;} (1,1,0)
$$

is therefore in the machine's transition relation whenever the protocol operates in any environment where context can gate invocation — which is precisely the deployment class the protocol's own zero-tolerance rule targets (environments where fabrication is a risk are environments where gating exists). Hence $D$ is reachable in one context transition from the protocol's normal operating state. $\square$

The reachability argument shows the deadlock is not an exotic corner: it sits one context event away from the protocol's designed operating point.

### 4.2 Absorption of the halt state (P2)

**Claim.** In $D$, no compliant action exists, and the machine halts.

**Derivation.** Evaluate the compliance predicate of Section 3.3 at $s = (1,1,0)$:

- $\mathrm{Compliant}(D, \textsf{invoke}) \iff c=1 \land i=1 \iff 1 \land 0 = \text{false}$.
- $\mathrm{Compliant}(D, \textsf{refrain}) \iff r=0 \lor c=0 \iff 0 \lor 0 = \text{false}$.
- $\mathrm{Compliant}(D, \textsf{halt}) = \text{false}$ by definition.

The compliant-label set at $D$ is empty:

$$
\{\ell \in L : \mathrm{Compliant}(D, \ell)\} = \varnothing.
$$

An agent that must act compliantly has no compliant action; the only terminating behavior is the forced halt. Moreover, the halt is absorbing in the compliance sense: no transition out of $D$ changes $r$, $c$, or $i$ under the agent's own action set, because every agent action is non-compliant and the protocol forbids non-compliant action. The state is a sink. $\square$

This is the same all-guards-false structure that [6] identifies as the hard case in s-deadlock verification: the violation state is one where every action guard is false, $\bigwedge_{\tau} \lnot(\tau.g)$, and [6] notes that over-abstractions mask exactly such states. A protocol test suite that only exercises states where some guard is true will never visit $D$.

### 4.3 State-space coverage of a binary protocol

Following the three-state semantics (with assumption A1 excluding the $(c=0, i=1)$ cell), each gated tool occupies one of three states: (capability absent), (capability present, invocation licensed), (capability present, invocation blocked). A binary protocol distinguishes only two: present or absent.

**Per-tool coverage.** The fraction of the true per-tool state space a binary protocol represents is:

$$
f(1) = \frac{2}{3}.
$$

**Arithmetic step.** Two representable states out of three total states: $2/3 = 0.666\ldots$

**Per-task coverage over $k$ gated tools.** Assuming independence across tools (the same independence assumption [9] states for its derivation), a binary protocol is specification-complete on:

$$
f(k) = \left(\frac{2}{3}\right)^{k}
$$

of the true configuration space.

**Arithmetic at $k=5$.**

$$
f(5) = \left(\frac{2}{3}\right)^{5} = \frac{2^{5}}{3^{5}} = \frac{32}{243}.
$$

Computing the decimal: $32 \div 243 = 0.13168\ldots$, so

$$
f(5) = \frac{32}{243} \approx 0.132.
$$

Interpretation: at five gated tools, a binary protocol fully specifies about $13.2\%$ of the true configuration space; the remaining $1 - 32/243 = 211/243 \approx 0.868$ of configurations contain at least one tool in the unspecified third state.

**Arithmetic at $k=10$.**

$$
3^{10} = 59049, \qquad 2^{10} = 1024.
$$

The state-space ratio is:

$$
\frac{3^{10}}{2^{10}} = \frac{59049}{1024} = 57.66\ldots \approx 57.7.
$$

The number of configurations containing at least one blocked-invocation tool is:

$$
59049 - 1024 = 58025.
$$

These are exact combinatorial consequences of the three-state semantics, not measurements; the same figures appear in [9], where they are likewise derived, not measured, and [9] notes that if a fourth state existed the well-defined fraction would drop to $(2/4)^{k}$, e.g. $f(5) = (1/2)^{5} = 1/32 = 0.03125$, so the direction of any modeling error favors the specification-gap claim.

### 4.4 The deadlock-precise configuration class

**Claim.** Under the semantics of Section 3.3, the halt occurs precisely when capability exists and invocation is blocked, i.e., in configurations with at least one required tool in state (present, blocked).

**Derivation.** The compliant-label set at a state $s$ is empty if and only if all three clauses fail:

$$
\lnot(c{=}1 \land i{=}1) \;\land\; \lnot(r{=}0 \lor c{=}0) \;\land\; \text{false}.
$$

The third conjunct is always false, so the set is empty for every state — but the agent halts only when it is required to act, i.e., when the task engages a tool. For a required tool ($r=1$): the first clause fails iff $i=0$ (given $c=1$), and the second clause fails iff $c=1$. So for a required tool the empty-compliant-set condition is exactly $c=1 \land i=0$. If $c=0$, $\textsf{refrain}$ is compliant and the agent halts gracefully with a defensible "capability absent" report; if $c=1$ and $i=1$, $\textsf{invoke}$ is compliant and work proceeds. The pathological halt — the one that misreports a specification defect as a capability failure — occurs iff capability exists and invocation is blocked. $\square$

This yields the testable signature for the empirical study of Section 7: halt rates should be elevated exactly in the (present, blocked) cell and not in the (absent) cell.

### 4.5 Per-task deadlock probability (projection)

The following is a projection, not a measurement. Assumptions: (i) each gated invocation independently has probability $q$ that the capability is present but invocation is blocked at call time; (ii) a task makes $n$ gated invocations; (iii) independence across invocations (assumption A3). We take $q = 0.1$ and $n = 5$ as illustrative values; neither is measured here, and Section 6 treats sensitivity to both.

The probability that a task avoids the deadlock configuration entirely is:

$$
P(\text{no deadlock}) = (1-q)^{n}.
$$

**Arithmetic.** With $q = 0.1$, $1 - q = 0.9$:

$$
0.9^{5} = 0.9 \times 0.9 \times 0.9 \times 0.9 \times 0.9.
$$

Step by step: $0.9^{2} = 0.81$; $0.9^{3} = 0.81 \times 0.9 = 0.729$; $0.9^{4} = 0.729 \times 0.9 = 0.6561$; $0.9^{5} = 0.6561 \times 0.9 = 0.59049$.

Therefore:

$$
P(\text{deadlock}) = 1 - (1-q)^{n} = 1 - 0.59049 = 0.40951.
$$

Under the stated assumptions, roughly $41\%$ of tasks encounter at least one (present, blocked) invocation. Per $1000$ tasks, the expected count of deadlock-affected tasks is:

$$
1000 \times 0.40951 = 409.51,
$$

i.e., about $410$ tasks per $1000$. Every input to this figure is the assumption $q=0.1$, the assumption $n=5$, and the arithmetic above; the figure is a projection and inherits the uncertainty of both assumptions, examined in Section 6.

### 4.6 Sensitivity of the projection

Because $P = 1 - (1-q)^{n}$, the projection is increasing and convex in $n$ for fixed $q$, and approximately linear in $q$ for small $q$ (since $(1-q)^{n} \approx 1 - nq$ when $nq \ll 1$; here $nq = 0.5$, so the linear approximation $P \approx nq = 0.5$ overstates the exact value $0.40951$ by about $0.09$). Two boundary checks with full arithmetic:

- $q = 0.01$, $n = 5$: $0.99^{5} = 0.9509900499$; $P = 1 - 0.9509900499 = 0.0490099501 \approx 0.049$. The projection is then about $49$ tasks per $1000$.
- $q = 0.1$, $n = 20$: $0.9^{20} = (0.9^{10})^{2}$; $0.9^{10} = 0.3486784401$; $0.9^{20} = 0.3486784401^{2} = 0.121577$; $P = 1 - 0.121577 = 0.878423 \approx 0.878$.

So the projection ranges from about $5\%$ to $88\%$ of tasks across plausible parameter choices; the qualitative claim — that the deadlock class is non-negligible whenever context gating occurs at all — is robust, while any operational planning number requires measuring $q$ and $n$ in the target deployment.

## 5. Results

The results are the formal properties proved in Section 4 and the exact combinatorial quantities computed there. No empirical measurement was performed; the per-task figure is a projection under stated assumptions.

**R1 (Reachability and absorption, Section 4.1–4.2).** Under zero-tolerance compliance semantics over (requirement, capability, invocation) triples, the halt state $D = (1,1,0)$ is reachable in one context transition from the protocol's normal operating state $(1,1,1)$, and at $D$ the compliant-label set is empty, so the machine halts and the halt is absorbing. The proof is by direct evaluation of the compliance predicate: at $(1,1,0)$, $\textsf{invoke}$ fails because $i=0$, $\textsf{refrain}$ fails because $r=1 \land c=1$, and $\textsf{halt}$ is non-compliant by definition.

**R2 (State-space coverage, Section 4.3).** A binary-state protocol governing $k$ permission-gated tools is specification-complete on a $(2/3)^{k}$ fraction of the true three-state space. Computed values: $f(5) = 32/243 \approx 0.132$; the $k=10$ state-space ratio is $3^{10}/2^{10} = 59049/1024 \approx 57.7$, with $59049 - 1024 = 58025$ configurations containing at least one blocked-invocation tool and therefore unspecified under the binary model. These are exact combinatorial consequences of the three-state semantics, not measurements.

**R3 (Deadlock-precise configuration, Section 4.4).** The pathological halt occurs precisely in the configuration class where the required capability exists ($c=1$) and invocation is blocked ($i=0$); in the (absent) cell the agent refrains compliantly, and in the (present, licensed) cell it invokes compliantly. This yields the discriminating prediction: measured halt rates should separate the (present, blocked) cell from the (absent) cell.

**R4 (Per-task deadlock projection, Section 4.5).** Under the stated assumptions $q=0.1$ (per-invocation probability of present-but-blocked) and $n=5$ (gated invocations per task), the per-task deadlock probability is $1 - 0.9^{5} = 0.40951$, i.e., about $410$ affected tasks per $1000$. Sensitivity bounds computed in Section 4.6: $P \approx 0.049$ at $q=0.01$, $n=5$; $P \approx 0.878$ at $q=0.1$, $n=20$. R4 is a projection resting entirely on the assumed rates; R1–R3 are not.

## 6. Discussion

**What the results do and do not claim.** R1 and R3 are formal results whose scope is bounded by the modeling choices of Section 3: the three-component state space, the specific compliance predicate, and the assumption that the agent's self-evaluation of invocation licensure is accurate