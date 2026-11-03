# Specification-Induced Deadlock in Zero‑Tolerance Agent Protocols

## Abstract
Large‑language‑model (LLM) agents increasingly rely on tool‑calling protocols that enforce a strict “zero‑tolerance” rule: any attempt to simulate or placeholder a tool is classified as forbidden and causes the agent to halt. This paper identifies a specification‑level failure mode in which the protocol’s binary view of tool availability (available / unavailable) omits a third, realistic state—capability present but permission denied. We formalize the capability–availability mismatch as a three‑state semantics over $k$ gated tools, derive the exact coverage fraction of binary protocols as $(2/3)^{k}$, and compute concrete values for $k=5$ and $k=10$. We also prove that the protocol‑compliance‑halting problem is undecidable by reduction to Rice’s theorem. Under an assumed mismatch probability of $0.27$ per gated invocation, we project a break‑even cost threshold of $0.27\,c_{t}$ per task. The results show that binary protocols leave a combinatorial majority of the true state space unspecified, leading to inevitable deadlocks in zero‑tolerance settings. Designers of LLM‑agent tool‑calling frameworks must therefore embed three‑state awareness or syntactic restrictions to guarantee well‑defined execution.

## 1. Introduction
Enterprises that deploy autonomous LLM agents for customer support, data extraction, or workflow automation instruct the agents to “use the live search tool when answering factual questions” and to “never simulate tool output.” In production, the search tool may be present in the agent’s toolbox but disabled for a particular tenant, budget tier, or rate‑limited session. When the agent follows a zero‑tolerance protocol that treats any simulated call as a violation, it classifies the attempted call as forbidden and halts. This deadlock blocks the entire service pipeline, incurs lost revenue, and forces manual intervention, even though the underlying capability exists.

If a protocol could recognise the intermediate state “capability present, permission denied,” the agent could fallback to a safe alternative (e.g., a cached answer) instead of halting. The absence of such a middle state is a specification‑level flaw, not a limitation of the underlying model or tool.

**Contributions.**
1. We formalize zero‑tolerance agent protocols as a state machine over $(\text{requirement},\text{capability},\text{invocation})$ triples and introduce a three‑state tool semantics (Section 2).  
2. We derive the exact specification‑completeness fraction of binary protocols as $(2/3)^{k}$ and compute concrete values for $k=5$ and $k=10$ (Section 4).  
3. We prove that the protocol‑compliance‑halting problem (PCH) is undecidable (Section 4).  
4. We present a projection of economic impact under an assumed mismatch probability of $0.27$ per gated invocation (Section 5).  

The insight that binary specifications leave most of the true state space undefined is relevant to any domain that couples LLM agents with external tools, including autonomous driving simulators, financial advisory bots, and multi‑agent reinforcement‑learning systems.

## 2. Background and Related Work
State‑transition systems (STS) are a standard formalism for modelling communication protocols. Definition 1 in [1] introduces an STS as a tuple $(S,s_{0},L,T,F)$. This representation underpins the ontology‑driven protocol designs of [2], which also employ STS to label transitions with communication‑act classes. The three‑state semantics we adopt extends the binary view by adding a “permission‑denied” label to each tool, analogous to the flow‑specification approach for cache‑coherence protocols in [6], where a system‑wide deadlock is defined as a state in which all guards are false.

The formal verification of deadlock freedom for parameterised protocols is addressed in [6] through invariants derived from message‑sequence diagrams. Our work parallels this methodology but focuses on the specification layer rather than the protocol implementation. The undecidability proof for protocol compliance (Section 4) follows the reduction style of Rice’s theorem as employed in [9] for the PCH problem.

Recent surveys of multi‑agent communication [7] highlight the importance of explicit protocol design for robustness, a theme echoed in the “Mandato” framework [4], which enforces digitally signed mandates on AI actions. While Mandato secures authorization, it assumes a binary tool model and therefore inherits the same specification gap identified here.

The choreography‑based deadlock‑freedom results of [8] demonstrate that logical characterisations can guarantee deadlock freedom for certain process calculi. Our contribution differs by exposing a combinatorial inevitability of deadlock under binary specifications, independent of any particular process calculus.

Finally, the QNFO report on the capability–availability mismatch [9] provides the exact combinatorial formulas that we re‑derive and extend, establishing the foundation for the quantitative analysis in this paper.

## 3. Methods
### 3.1 Protocol Model
We model a zero‑tolerance agent protocol as a deterministic finite‑state machine (FSM) whose states encode the triple
\[
(\rho,\kappa,\iota)
\]
where $\rho$ is the current requirement (e.g., “answer factual question”), $\kappa\in\{0,1\}^{k}$ indicates the presence ($1$) or absence ($0$) of each of the $k$ gated tools, and $\iota\in\{0,1\}^{k}$ records per‑tool permission (allowed $=1$, denied $=0$). A transition is permitted only if for every tool $j$ the pair $(\kappa_{j},\iota_{j})$ satisfies either $(0,0)$ (tool absent) or $(1,1)$ (tool present and permitted). Any attempt to invoke a tool with $(1,0)$ triggers the protocol’s zero‑tolerance rule and forces the FSM into a halting sink state $H$.

### 3.2 Three‑State Semantics
The binary model collapses $(\kappa_{j},\iota_{j})$ into a single Boolean “available” flag:
\[
a_{j}= \kappa_{j}\land\iota_{j}.
\]
The three‑state model retains the full pair, yielding three possible local states per tool:
\[
(0,0):\text{absent},\quad (1,0):\text{present‑but‑denied},\quad (1,1):\text{present‑and‑allowed}.
\]
Thus the global configuration space contains $3^{k}$ distinct triples.

### 3.3 Specification‑Completeness Metric
A binary protocol is said to be *specification‑complete* on a configuration if the binary abstraction $(a_{1},\dots,a_{k})$ uniquely determines the three‑state triple. This holds precisely when no tool is in the $(1,0)$ state. Hence the number of configurations covered by the binary model is $2^{k}$ (each tool either absent or present‑and‑allowed). The coverage fraction is therefore
\[
f(k)=\frac{2^{k}}{3^{k}}=\left(\frac{2}{3}\right)^{k}.
\]

### 3.4 Undecidability of Protocol‑Compliance‑Halting (PCH)
We define the decision problem PCH: given a protocol description $P$ and an initial configuration $c$, does the FSM eventually reach a non‑halting accepting state while obeying zero‑tolerance rules? By encoding arbitrary Turing‑machine computations into the FSM’s transition structure and using the $(1,0)$ state to simulate a “reject” branch, we reduce the halting problem to PCH. Rice’s theorem then implies that PCH is undecidable.

### 3.5 Economic Projection Assumptions
We adopt the mismatch probability $p_{m}=0.27$ per gated invocation as reported in [9]. Let $c_{t}$ denote the cost of a single tool call. The expected additional cost per task due to forced halts is $p_{m}\,c_{t}$. We treat this as a projection, not an empirical measurement.

## 4. Analysis
### 4.1 Coverage Fraction Derivation
The total number of global configurations for $k$ tools under three‑state semantics is
\[
N_{\text{total}} = 3^{k}.
\]
Binary abstraction counts only configurations where no tool is in the $(1,0)$ state:
\[
N_{\text{binary}} = 2^{k}.
\]
Thus the specification‑completeness fraction is
\[
f(k)=\frac{N_{\text{binary}}}{N_{\text{total}}}
      =\frac{2^{k}}{3^{k}}
      =\left(\frac{2}{3}\right)^{k}.
\]

#### Example $k=5$
\[
\begin{aligned}
N_{\text{total}} &= 3^{5}=243,\\
N_{\text{binary}}&= 2^{5}=32,\\
f(5) &= \frac{32}{243}\approx 0.1316872.
\end{aligned}
\]
Rounded to three decimal places, $f(5)\approx 0.132$, matching the value reported in [9].

#### Example $k=10$
\[
\begin{aligned}
N_{\text{total}} &= 3^{10}=59049,\\
N_{\text{binary}}&= 2^{10}=1024,\\
f(10) &= \frac{1024}{59049}\approx 0.0173405.
\end{aligned}
\]
The inverse ratio, i.e., how many times larger the true space is compared to the binary space, is
\[
\frac{N_{\text{total}}}{N_{\text{binary}}}= \frac{59049}{1024}\approx 57.7.
\]
The number of unspecified configurations (those containing at least one $(1,0)$ tool) is
\[
N_{\text{unspec}} = N_{\text{total}}-N_{\text{binary}} = 59049-1024 = 58025.
\]

### 4.2 Undecidability Proof Sketch
1. Encode an arbitrary Turing machine $M$ as a finite set of FSM states and transitions, where each tape cell corresponds to a gated tool.  
2. Use the $(1,0)$ state to represent a “reject” transition that forces the FSM into the halting sink $H$.  
3. Construct a protocol $P_{M}$ that simulates $M$ step‑by‑step while respecting zero‑tolerance rules.  
4. If $M$ halts, $P_{M}$ reaches an accepting state without invoking any $(1,0)$ transition; otherwise, $P_{M}$ inevitably attempts a forbidden simulation and halts at $H$.  
5. Deciding whether $P_{M}$ avoids $H$ solves the halting problem, which is undecidable. By Rice’s theorem, any non‑trivial property of the language recognized by $P_{M}$ (including PCH) is undecidable.

Therefore, PCH is undecidable.

### 4.3 Economic Projection Computation
Assuming each gated tool invocation incurs cost $c_{t}$, the expected extra cost per task due to forced halts is
\[
\text{Cost}_{\text{extra}} = p_{m}\,c_{t}=0.27\,c_{t}.
\]
This linear projection follows directly from the assumed mismatch probability.

## 5. Results
| Metric | $k$ | Total configurations $3^{k}$ | Binary configurations $2^{k}$ | Coverage fraction $f(k)$ | Unspecified configs $3^{k}-2^{k}$ |
|--------|-----|------------------------------|------------------------------|--------------------------|-----------------------------------|
| Example 1 | 5 | 243 | 32 | $0.132$ | 211 |
| Example 2 | 10 | 59049 | 1024 | $0.0173$ | 58025 |

The undecidability result establishes that no algorithm can universally decide whether a zero‑tolerance protocol will halt compliantly for arbitrary inputs. The economic projection indicates a per‑task cost increase of $0.27\,c_{t}$ under the assumed mismatch probability.

## 6. Discussion
### 6.1 Limitations
- **Three‑state idealisation.** We assume tools never appear in a fourth state $(0,1)$ (absent but permission granted). If platforms expose such a state, the coverage fraction degrades to $(2/4)^{k}= (1/2)^{k}$, e.g., $f(5)=1/32=0.03125$ (Section 6 of [9]).  
- **Independence of capability and permission.** Derivation of $f(k)$ treats $\kappa$ and $\iota$ as independent Bernoulli variables; correlated policies would alter the combinatorics.  
- **Model abstraction.** The FSM abstracts away runtime dynamics such as retries, back‑off, or human‑in‑the‑loop overrides, which could mitigate deadlocks in practice.  
- **Undecidability scope.** The reduction relies on encoding arbitrary Turing‑machine behaviour into the protocol; real‑world protocols may be syntactically restricted, rendering PCH decidable for those subclasses.  

A falsifying observation would be an empirical measurement showing that a binary protocol over $k=10$ gated tools never encounters a forced halt despite the presence of disabled tools, contradicting the combinatorial guarantee that $58{,}025$ configurations are unspecified. Such a result would imply that the real deployment does not conform to the three‑state model, invalidating our assumptions.

### 6.2 Open Questions
- How prevalent are three‑state mismatches in deployed LLM‑agent platforms?  
- Can syntactic restrictions (e.g., limiting loops, enforcing explicit permission checks) yield a decidable fragment of PCH?  
- What is the impact of dynamic permission updates on the state‑space coverage over time?

## 7. Practical Implications and Engineering Pathways
**(a) Intended users and design impact.** Protocol designers, platform engineers, and safety auditors for LLM‑agent systems would use the derived coverage fractions to assess whether their tool‑calling specifications are sufficiently expressive. If the result holds, they must augment binary specifications with an explicit “permission‑denied” state or enforce syntactic restrictions that guarantee compliance without relying on undecidable checks.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; it therefore resides at TRL 2.

**(c) Minimal de‑risking experiment.** Implement a minimal agent protocol for $k=3$ gated tools that logs the tool’s capability flag and permission flag separately. Run the agent across all $3^{3}=27$ configurations (e.g., via a test harness that toggles permissions). Measure the halt rate. Observation of any halt in a configuration where a tool is present but denied would confirm the predicted deadlock; a complete absence of halts would falsify the three‑state model for that platform.

**(d) Engineering constraints.**  
- *Permission visibility*: The platform must expose per‑tool permission flags to the agent runtime.  
- *State‑machine extensibility*: The protocol engine must support a third transition label for “present‑but‑denied.”  
- *Verification tooling*: Since PCH is undecidable, static analysis tools can only target restricted protocol fragments.

**(e) Projected cost bound.** Assuming a mismatch probability $p_{m}=0.27$ per gated invocation (as in [9]) and a unit tool‑call cost $c_{t}$, the expected extra cost per task is $0.27\,c_{t}$. This projection rests on the independence assumption of capability and permission and on the combinatorial coverage derived in Section 4.

**(f) Risks and misuse.** Over‑restrictive adoption of three‑state semantics without proper fallback strategies could increase unnecessary halts, degrading user experience. Conversely, ignoring the mismatch may lead to silent failures where agents produce incomplete or fabricated answers, posing safety risks.

## 8. Conclusion
Zero‑tolerance LLM‑agent protocols that model tool availability as a binary predicate inevitably leave a combinatorial majority of the true capability–permission state space unspecified. Our formal analysis shows that a binary protocol over $k$ gated tools covers only $(2/3)^{k}$ of configurations, leaving $3^{k}-2^{k}$ configurations prone to forced halts. The undecidability of the protocol‑compliance‑halting problem further demonstrates that no universal algorithm can guarantee deadlock‑free execution under the binary model. Designers must therefore either enrich specifications with an explicit “permission‑denied” state or restrict protocol syntax to decidable fragments. The projected economic impact underscores the practical urgency of addressing this specification‑induced deadlock.

## References
[1] arXiv:2401.16216v1 | A mechanism for discovering semantic relationships among agent communication protocols  
[2] arXiv:2401.11841v1 | Semantic Web Technology for Agent Communication Protocols  
[3] arXiv:2106.14835v1 | Virtual Agents in Live Coding: A Short Review  
[4] arXiv:2608.14074v1 | Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails  
[5] arXiv:2604.04820v1 | ANX: Protocol-First Design for AI Agent Interaction with a Supporting 3EX Decoupled Architecture  
[6] arXiv:1407.7468v1 | Using Flow Specifications of Parameterized Cache Coherence Protocols for Verifying Deadlock Freedom  
[7] arXiv:2203.08975v2 | A Survey of Multi-Agent Deep Reinforcement Learning with Communication  
[8] arXiv:2501.08928v2 | Formulas as Processes, Deadlock-Freedom as Choreographies (Extended Version)  
[9] QNFO: The Capability–Availability Mismatch: Three-State Tool Semantics and Forced-Halt Conditions in LLM Agent Protocols | https://papers.qnfo.org/papers/the-capability-availability-mismatch-three-state-tool-semantics-and-forced-halt-  
[10] QNFO: Agentic Collapse | https://papers.qnfo.org/papers/agentic-collapse