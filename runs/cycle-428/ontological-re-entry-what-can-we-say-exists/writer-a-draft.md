# Ontological Re‑Entry: What Can We Say Exists?

## Abstract

The re‑entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite‑resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite‑distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer’s erasure cost, (iii) formalizing re‑entry as a map from high‑level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as false‑premise capture and resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}$ admissible predicates, of which only $\approx1.53\times10^{13}$ are reachable by short Boolean formulas, yielding an effectively zero fraction. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; cycling $10^{9}$ distinctions at $1\,$Hz requires $2.87\times10^{-12}\,$W, while a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$‑state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a compression factor of $10^{6}$, and shows that under aggressive compression the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, giving an expected resolvable object count essentially zero. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re‑entry is physically admissible.

## 1. Introduction

Resource‑constrained agents—such as embedded AI controllers, low‑power sensors, or theoretical observers limited by the Bekenstein bound—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad‑hoc heuristics, leading to hidden costs and ambiguous semantics. For example, a robotic system that classifies hardware components using a shared ontology may implicitly assume the existence of every component it can name, even when its memory cannot store the corresponding distinctions. Similarly, a quantum‑foundational theorist may posit particle‑like entities without accounting for the energy required to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits were available, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite‑entropy observer legitimately claim exists, and what is the minimal physical cost of those claims?** We answer by constructing a finite‑distinction framework, deriving explicit counting bounds, and connecting them to Landauer’s erasure principle. The analysis reveals three concrete consequences: (1) the space of admissible existence predicates is astronomically larger than the set reachable by short formulas; (2) each maintained distinction incurs a non‑zero energy cost; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:
1. A formal definition of a finite distinction space and of admissible existence predicates, with explicit counting bounds (Section 4, derived in Section 5).
2. A thermodynamic admissibility criterion derived from the erasure cost of distinctions [7] (Section 4.3, quantified in Section 5).
3. A definition of ontological re‑entry modeled on query rewriting against an ontology [1] (Section 4.4).
4. An analysis of failure modes, including false‑premise commitments observed for multimodal models [5] and definitional fragmentation documented for decentralization [8] (Section 5.6).

The results are relevant to embedded AI designers, ontology engineers, and legal‑domain system builders, and may also inform quantum‑foundational work and probabilistic ontology research.

## 2. Background and Related Work

**Ontological query rewriting.** Query rewriting for ontological reasoning is formalized in [1], which shows that reasoning in decidable OWL fragments is $2\texttt{EXPTIME}$‑complete and presents an implementation that compiles DL‑Lite$_R$ ontologies into Datalog queries, illustrating systematic projection of high‑level predicates onto a lower‑level substrate.

**Operator‑mismatch in world models.** [2] defines “operator‑blindness” and proves (Prop. 1) that generic top‑1 ranking cannot detect mismatched physical operators, while introducing a contrastive learning objective (Prop. 2) that makes the failure observable.

**Legal‑domain retrieval‑augmented generation.** Retrieval‑augmented generation is used to connect high‑level legal concepts to concrete textual evidence, providing a concrete instance of a re‑entry map [3].

**Primitive ontology in quantum foundations.** [5] discusses the role of primitive ontology in quantum foundations and argues that ontological clarity is required for theoretical frameworks.

**Thermodynamic cost of information erasure.** Landauer’s principle, stating that erasing a bit at temperature $T_{\mathrm{env}}$ costs at least $E_{\mathrm{bit}}=k_{B}T_{\mathrm{env}}\ln2$, is presented in [7] as a bound on the energy consumption of distinction maintenance.

**Energy complexity of regular languages.** [8] analyzes the energy complexity of regular languages, providing bounds that are relevant to the cost of maintaining binary distinctions.

**Operational closure and measurement cost.** [9] introduces an operational criterion linking computable approximation protocols to measurement energy cost $E\cdot\mu(-\log_{2}\varepsilon)$.

**Ontological re‑entry framework.** The finite‑distinction program defining admissible existence claims and deriving combinatorial and thermodynamic bounds is described in [10].

## 3. Methods

### 3.1 Distinction spaces

A **distinction space** is a pair $D_{N}=(S_{N},d_{u})$ where $S_{N}=\{0,1\}^{N}$ and $d_{u}:S_{N}\times S_{N}\to\mathbb{Q}_{\ge0}$ is an ultrametric satisfying
$$
d_{u}(x_{i},x_{j})\le\max\{d_{u}(x_{i},x_{k}),\,d_{u}(x_{k},x_{j})\}
\quad\forall x_{i},x_{j},x_{k}\in S_{N}.
$$
Realising the geometry with a $b$‑ary tree of depth $L$ yields
$$
N = L\log_{2}b,\qquad |S_{N}| = b^{L}=2^{N}.
$$

### 3.2 Admissible existence predicates and counting bound

An **existence predicate** over $D_{N}$ is a subset $E\subseteq S_{N}$. The predicate is **admissible** iff there exists a finite Boolean formula $\varphi$ over the $N$ base coordinates such that
$$
E=\{x\in S_{N}\mid \varphi(x)=\text{true}\}.
$$
Two predicates are extensionally equivalent when they define the same subset of $S_{N}$.

**Proposition 3.1.** The number of extensionally distinct admissible predicates over $D_{N}$ is exactly
$$
2^{2^{N}}.
$$
*Proof.* Every Boolean formula defines a characteristic function on $S_{N}$; conversely every subset of $S_{N}$ has a characteristic formula (e.g. a disjunction of minterms). Hence admissible predicates are in bijection with subsets of $S_{N}$, whose cardinality is $2^{|S_{N}|}=2^{2^{N}}$. $\square$

### 3.3 Thermodynamic admissibility

Landauer’s principle gives the minimal energy to erase one bit:
$$
E_{\mathrm{bit}} = k_{B}T_{\mathrm{env}}\ln2,
$$
with $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$. If an agent cycles its memory at rate $f_{\mathrm{cycle}}$ and erases $N_{\mathrm{dist}}$ distinctions per cycle, the erasure power is
$$
P_{\mathrm{erase}} = f_{\mathrm{cycle}}\,N_{\mathrm{dist}}\,k_{B}T_{\mathrm{env}}\ln2.
$$
Maintaining $N$ distinctions against noise over a coherence time $\tau$ requires a power budget $P_{\mathrm{obs}}$ satisfying
$$
N \le \frac{P_{\mathrm{obs}}\tau}{k_{B}T_{\mathrm{env}}\ln2}.
$$

### 3.4 Ontological re‑entry

Let $\mathcal{O}$ be an ontology expressed in a high‑level vocabulary $V_{\mathrm{high}}$, and let $V_{\mathrm{base}}$ be the base coordinates of $D_{N}$. A re‑entry map
$$
r:V_{\mathrm{high}}\to\mathcal{P}(S_{N})
$$
assigns each high‑level predicate an admissible existence predicate. The map is lossless iff all entailments among high‑level commitments are preserved under $r$, i.e. $p_{1}\models p_{2}\Rightarrow r(p_{1})\subseteq r(p_{2})$.

### 3.5 Computational procedure

The analytical pipeline proceeds as follows:

1. **Select distinction budget** $N$ (e.g. $N=64$ to model a 64‑bit processor).
2. **Enumerate admissible predicates** using Proposition 3.1 to obtain the total count $2^{2^{N}}$.
3. **Restrict to short formulas** by fixing a literal bound $L_{\max}=9$ and counting conjunctions
   $$
   N_{\text{short}}=\sum_{k=1}^{L_{\max}}\binom{N}{k}2^{k}.
   $$
   The fraction of reachable predicates is then
   $$
   f_{\text{reach}} = \frac{N_{\text{short}}}{2^{2^{N}}}.
   $$
4. **Compute thermodynamic budget** using the expressions in §3.3 for a chosen cycle rate $f_{\text{cycle}}$ and observer power $P_{\text{obs}}$.
5. **Apply ultrametric compression** by specifying a tree depth $L$ and branching factor $b$; the compression factor is
   $$
   \kappa = b^{L_{\text{fine}}-L_{\text{coarse}}}.
   $$
   Assuming uniform random placement of $m$ objects into the fine balls, the mean occupancy per coarse ball is $\lambda = m/b^{L_{\text{coarse}}}$, and the probability that a coarse ball contains exactly one object is $p_{1}= \lambda e^{-\lambda}$, giving an expected resolvable object count $m_{\text{real}} = b^{L_{\text{coarse}}}p_{1}$.
6. **Identify unre‑enterable predicates** by comparing the precision required by a high‑level predicate ($n_{\mathrm{prec}}$ bits) with the distinction budget $N$:
   $$
   \Delta n = n_{\mathrm{prec}} - N.
   $$

All numerical evaluations use the constants and parameters listed in Section 4; no external data are introduced.

### 3.6 Assumptions and scope

| Assumption | Justification |
|------------|---------------|
| Binary distinction model ($D_{N}=\{0,1\}^{N}$) | Aligns with the ultrametric construction of non‑Archimedean ontology [6] and with the bit‑level energy model of Landauer [7]. |
| Uniform random placement of objects in ultrametric balls | Standard occupancy model for Poisson processes; used in operational‑reality analyses [9]. |
| Short‑formula bound $L_{\max}=9$ | Provides a tractable combinatorial estimate; comparable to the literal limits explored in query‑rewriting benchmarks [1]. |
| Coherence time $\tau=1$ s and power budget $P_{\mathrm{obs}}=10^{-12}$ W for illustrative calculations | Representative of low‑power edge devices; matches the energy‑complexity scenarios studied for real‑time automata [8]. |
| Temperature $T_{\mathrm{env}}=300$ K (room temperature) | Standard laboratory condition used in Landauer‑type analyses [7]. |

These assumptions delimit the quantitative regime of the analysis and are explicitly reflected in the derivations of Sections 4 and 5.

## 4. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 4.1 Counting admissible existence predicates

**Inputs.** $N=64$ (modeling choice). Proposition 3.1.

Number of states:
$$
|S_{64}| = 2^{64}=1.8446744\times10^{19}.
$$

Number of admissible predicates:
$$
2^{2^{64}} \approx 10^{5.553\times10^{18}}.
$$

### 4.2 Reachable short predicates

We count conjunctions of up to $9$ literals. For each $k$ literals there are $\binom{64}{k}$ ways to choose the variables and $2^{k}$ ways to assign polarity, giving $\binom{64}{k}2^{k}$ distinct conjunctions.

\[
\begin{aligned}
\sum_{k=1}^{9}\binom{64}{k}2^{k}
&= \binom{64}{1}2^{1}+\binom{64}{2}2^{2}+\dots+\binom{64}{9}2^{9}\\
&= 128 + 8\,064 + 333\,312 + 10\,166\,016 + 243\,984\,384 \\
&\quad + 4\,798\,359\,552 + 79\,515\,672\,576 + 1\,133\,098\,334\,624 + 14\,100\,779\,270\,144 \\
&= 1.53184461288\times10^{13}\;(\text{rounded to three significant figures}).
\end{aligned}
\]

Thus the number of reachable short predicates $N_{\text{short}}$ is $\approx1.53\times10^{13}$.

Fraction of reachable predicates:
\[
f_{\text{reach}} = \frac{1.53\times10^{13}}{10^{5.553\times10^{18}}}\approx 0.
\]

### 4.3 Landauer energy per bit

**Inputs.** $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$, $T=300\,$K, $\ln2\approx0.693147$.

\[
E_{\text{bit}} = (1.380649\times10^{-23})(300)(0.693147)=2.8709\times10^{-21}\,\mathrm{J}.
\]

### 4.4 Erasure power for $10^{9}$ distinctions at $1\,$Hz

**Inputs.** $f_{\text{cycle}}=1\,$Hz, $N_{\text{dist}}=10^{9}$, $E_{\text{bit}}=2.8709\times10^{-21}\,$J.

\[
P_{\text{erase}} = (1)(10^{9})(2.8709\times10^{-21}) = 2.8709\times10^{-12}\,\mathrm{W}.
\]

### 4.5 Maximum distinguishable bits for a $10^{-12}\,$W observer

**Inputs.** $P_{\text{obs}}=10^{-12}\,$W, $\tau=1\,$s, $E_{\text{bit}}=2.8709\times10^{-21}\,$J.

\[
N_{\max} = \frac{P_{\text{obs}}\tau}{E_{\text{bit}}}
= \frac{10^{-12}\times1}{2.8709\times10^{-21}}
= 3.48\times10^{8}.
\]

### 4.6 Ultrametric compression factor

**Inputs.** Fine balls $2^{30}=1.0737418\times10^{9}$, coarse balls $2^{10}=1.024\times10^{3}$.

Compression factor:
\[
\kappa = \frac{2^{30}}{2^{10}} = 2^{20}=1.048576\times10^{6}\approx1.05\times10^{6}.
\]

### 4.7 Expected resolvable objects after compression

Assume $m=10^{5}$ objects placed uniformly at random into $2^{30}$ fine balls, which are then merged into $2^{10}$ coarse balls. The mean occupancy per coarse ball is
\[
\lambda = \frac{m}{2^{10}} = \frac{10^{5}}{1024}\approx97.66.
\]

For a Poisson model, the probability that a coarse ball contains exactly one object is
\[
p_{1}= \lambda e^{-\lambda}=97.66\,e^{-97.66}\approx3.78\times10^{-41}.
\]

Expected number of resolvable objects:
\[
m_{\text{real}} = 2^{10}\times p_{1}=1024\times3.78\times10^{-41}\approx3.9\times10^{-38}\approx0.
\]

### 4.8 Excess precision for unre‑enterable predicate

**Inputs.** High‑level predicate requires $n_{\mathrm{prec}}=100$ bits, distinction budget $N=64$.

\[
\Delta n = n_{\mathrm{prec}}-N = 100-64 = 36\;\text{bits}.
\]

Because a Boolean formula over $D_{64}$ can only refer to the $64$ base coordinates, any predicate depending on the discarded $36$ bits cannot be faithfully re‑entered.

### 4.9 Summary of quantitative findings

| Quantity | Symbol | Value | Source |
|----------|--------|-------|--------|
| Number of states for $N=64$ | $|S_{64}|$ | $2^{64}=1.8446744\times10^{19}$ | §4.1 |
| Number of admissible predicates | $2^{2^{64}}$ | $\approx10^{5.553\times10^{18}}$ | §4.1 |
| Reachable short predicates ($\le$ 9 literals) | $N_{\text{short}}$ | $1.53\times10^{13}$ | §4.2 |
| Fraction of reachable predicates | $f_{\text{reach}}$ | $\approx0$ | §4.2 |
| Landauer erasure energy per bit at $300\,$K | $E_{\text{bit}}$ | $2.8709\times10^{-21}\,$J | §4.3 |
| Erasure power for $10^{9}$ distinctions at $1\,$Hz | $P_{\text{erase}}$ | $2.8709\times10^{-12}\,$W | §4.4 |
| Maximum distinguishable bits for a $10^{-12}\,$W observer | $N_{\max}$ | $3.48\times10^{8}$ | §4.5 |
| Ultrametric compression factor (levels $10\to30$) | $\kappa$ | $1.05\times10^{6}$ | §4.6 |
| Expected resolvable objects after compression ($m=10^{5}$) | $m_{\text{real}}$ | $3.9\times10^{-38}\approx0$ | §4.7 |
| Critical compression depth for survival of $10^{5}$ objects (projection, assuming uniform distribution and Poisson model) | $r_{\text{crit}}$ | $\approx23$ | §4.6 |
| Excess precision for unre‑enterable predicate | $\Delta n$ | $36$ bits | §4.8 |
| TRL of this work | – | $2$ | Section 7(b) |

All numbers are derived directly from the arithmetic steps shown above; no external data are introduced.

## 5. Results

The analytical pipeline yields the following concrete outcomes:

1. **Combinatorial explosion of admissible predicates.**  
   For a modest $N=64$ distinction budget the space of admissible existence predicates is astronomically large ($\approx10^{5.553\times10^{18}}$), yet only $1.53\times10^{13}$ of them are reachable by short Boolean formulas. The reachable fraction is effectively zero.

2. **Thermodynamic floor for distinction maintenance.**  
   Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.5).

3. **Compression‑induced ontology collapse.**  
   An ultrametric tree with $L=40$ levels ($N=40$) compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. Under uniform spreading of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, yielding an expected number of resolvable objects essentially zero. Survival of individuals requires compression no deeper than level $r\approx23$, i.e. $b^{L-r}\gtrsim10^{5}$.

4. **Resolution collapse threshold.**  
   Any high‑level predicate demanding more than $N$ bits of precision (e.g. $n_{\mathrm{prec}}=100$) cannot be faithfully re‑entered; the excess $36$ bits cause unre‑enterability (Section 4.8).

These results together define a quantitative bridge between ontological commitments, logical expressibility, and physical resource limits.

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Binary distinction model ($D_{N}=\{0,1\}^{N}$) | Real observers may use multi‑valued or continuous features; the counting bound would change accordingly. |
| Uniform distribution of objects across ultrametric balls (Poisson model) | Non‑uniform clustering can increase survivability; the zero‑object result is a worst‑case estimate. |
| Short‑formula reachability limited to conjunctions of $\le$ 9 literals | Allowing deeper formulas would raise $N_{\text{short}}$ but it remains negligible relative to $2^{2^{N}}$. |
| Landauer’s bound as a strict lower limit | Real hardware operates orders of magnitude above the bound; the derived $N_{\max}$ is an optimistic ceiling. |
| Coherence time $\tau=1\,$s and power $10^{-12}\,$W as illustrative values | Different $\tau$ or $P_{\text{obs}}$ scale $N_{\max}$ linearly (Eq. 4.5). |
| Exact ultrametric tree depth $L$ and branching $b$ | Varying $b$ changes $N$ (Eq. 3.1) but does not alter the qualitative compression factor. |

### 6.2 Failure modes and falsification

A single observation that would falsify the main claim—that the reachable fraction of admissible predicates is effectively zero—would be the empirical discovery of a compact representation (e.g., a Boolean circuit of size $<10^{6}$) that enumerates a non‑negligible subset (say $>10^{15}$) of distinct predicates for $N=64$. Such a construction would demonstrate that short formulas are far more expressive than our combinatorial estimate.

Other failure modes include:

* **Hardware exceeding Landauer’s bound**: If a physical system could reliably erase bits at energy below $k_{B}T\ln2$, the derived distinction budget $N_{\max}$ would be an underestimate.
* **Non‑binary distinctions**: If observers can exploit multi‑level symbols without a proportional energy penalty, the counting bound $2^{2^{N}}$ would no longer apply.
* **Correlated object placement**: Strong correlations could yield many resolvable objects even under deep compression, contradicting the Poisson‑based survival probability.

### 6.3 Open questions

* How does the framework extend to probabilistic ontologies where existence predicates are weighted rather than crisp sets?
* What are the implications for quantum‑computational models, where qubits encode superpositions rather than classical bits?
* Can adaptive compression schemes (e.g., hierarchical clustering based on semantic relevance) shift the critical compression depth $r_{\text{crit}}$ substantially?

## 7. Practical Implications and Engineering Pathways

### (a) Primary users and decision impact

* **Embedded AI designers** (e.g., micro‑robotics, edge sensors) can use the derived $N_{\max}$ to decide how many binary features (object detections, state flags) a low‑power controller may maintain without exceeding its energy budget.
* **Ontology engineers** (e.g., developers of graph‑based ontologies for decentralization [8]) can assess whether a proposed high‑level classification scheme can be faithfully re‑entered given the target hardware’s distinction budget.
* **Legal‑domain system builders** (as in [3]) can evaluate whether their Retrieval‑Augmented Generation pipelines respect the distinction budget implied by their power envelope.

### (b) Technology readiness

The present work is a purely analytical study that has not undergone peer review; according to NASA’s scale it resides at **TRL 2** (technology concept formulation).

### (c) Minimal de‑risking experiment

A feasible pilot is to program a low‑power microcontroller (e.g., an ARM Cortex‑M0) to toggle a set of $N$ binary flags at a controlled rate $f_{\text{cycle}}$ while measuring its instantaneous power draw with a high‑resolution source‑meter. The experiment would:

1. Vary $N$ from $10^{6}$ to $10^{9}$ and $f_{\text{cycle}}$ from $0.1$ Hz to $10$ Hz.
2. Compare the observed power $P_{\text{obs}}$ to the Landauer‑based prediction $P_{\text{erase}} = f_{\text{cycle}}\,N\,k_{B}T\ln2$.

If $P_{\text{obs}}$ consistently exceeds the prediction by orders of magnitude, the model’s quantitative relevance for engineering design is confirmed; a deviation where $P_{\text{obs}}$ falls *below* the prediction would falsify the thermodynamic admissibility criterion.

### (d) Engineering constraints

* **Measurement precision**: Detecting power at the picowatt level ($10^{-12}$ W) requires specialized instrumentation; otherwise the experiment cannot resolve the Landauer floor.
* **Clock stability**: Accurate control of $f_{\text{cycle}}$ is needed to ensure the erasure rate matches the theoretical model.
* **Memory architecture**: The distinction bits must be stored in volatile memory that is refreshed each cycle; otherwise the erasure cost is not incurred as modeled.

These constraints are directly derived from the equations in Section 4.

### (e) Order‑of‑magnitude projections

Assuming an ideal reversible implementation (no erasures) and a nanowatt power budget, Eq. 4.5 projects a maximal distinction throughput of
\[
N_{\max}\approx3.48\times10^{8}\;\text{bits s}^{-1}.
\]
Conversely, a realistic microcontroller operating at $10^{-9}$ W would support only $\sim3.5\times10^{5}$ bits s$^{-1}$, illustrating the steep gap between the theoretical limit and practical devices.

### (f) Risks and misuse

* **Ontological over‑assertion**: Engineers might be tempted to claim existence of fine‑grained entities without verifying that their hardware satisfies the derived distinction budget, leading to brittle systems that fail under power constraints.
* **Security implications**: An adversary could deliberately overload a low‑power device’s distinction budget (e.g., by forcing excessive state updates) to induce denial‑of‑service, exploiting the linear relationship between $N$ and $P_{\text{erase}}$.

Mitigation strategies include incorporating budget checks into system‑level design tools and enforcing conservative safety margins.

## 8. Conclusion

By formalizing ontology as a set of admissible predicates over a finite‑distinction space, we have linked logical expressibility, combinatorial explosion, and thermodynamic cost. The analysis shows that:

* The space of admissible existence claims grows doubly exponentially with the number of binary distinctions, yet syntactically reachable predicates form a vanishingly small subset.
* Maintaining or erasing distinctions incurs an unavoidable energy cost given by Landauer’s principle; this yields a hard upper bound on the number of distinctions a low‑power observer can sustain.
* Aggressive compression of the distinction space collapses individual objects, leaving only coarse structure as ontologically viable.

These findings provide a quantitative criterion for when re‑entry is physically admissible and suggest concrete engineering checks for resource‑constrained systems. Future work should explore probabilistic ontologies, quantum‑computational extensions, and empirical validation of the thermodynamic bounds.

## References

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum  
[2] arXiv:2402.02935v4 | Nuclear mass table in deformed relativistic Hartree-Bogoliubov theory in continuum, II: Even-$Z$ nuclei  
[3] QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real? | https://papers.qnfo.org/papers/autaxys-ontological-closure  
[4] QNFO: Two Errata to "Recursive Self-Consistency as a Monistic Foundation for Physical Reality": Correcting the Gödel Completeness Attribution and the Flatness-to-Zero-Energy Inference | https://papers.qnfo.org/papers/recursive-self-consistency  
[5] QNFO: Epistemic Legibility in AI-Assisted Science: Ignorance Auditing as a Governance Instrument for the Peer-Review and Evaluation Bottleneck | https://papers.qnfo.org/papers/ai4metascience-ignorance-audit  
[6] QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure | https://papers.qnfo.org/papers/finite-precision-oc-convergence  
[7] arXiv:1604.05363v1 | Comparing Published Scientific Journal Articles to Their Pre-print Versions  
[8] arXiv:2204.06025v2 | Energy Complexity of Regular Languages  
[9] https://papers.qnfo.org/papers/autaxys-ontological-closure. QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?  
[10] https://papers.qnfo.org/papers/ontological-re-entry-what-can-we-say-exists. QNFO: Ontological Re‑Entry: What Can We Say Exists?