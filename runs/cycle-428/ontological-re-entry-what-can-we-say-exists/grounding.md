# Grounding block - source: rem-e1985657-d3c9-4f0f-80bf-c88e6b91a1a0

## Research idea

Correct the published paper 'ontological-re-entry-what-can-we-say-exists' for erratum pl-ontological-re-entry-what-can-we-say-exists-2.3.0-0: Summary table (§5.9) and Appendix B (C3) list reachable short predicates as 1.53×10^12, and §5.2's f_reach uses 1.53×10^12 as numerator, while §5.2's own summation computes 1.53×10^13.

## Existing paper under revision (remediation only)

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

## 2. Background and Related Work

**Ontological query rewriting.** Query rewriting for ontological reasoning is formalized in [1], which shows that reasoning in decidable OWL fragments is $2\texttt{EXPTIME}$‑complete and presents an implementation that compiles DL‑Lite$_R$ ontologies into Datalog queries, illustrating systematic projection of high‑level predicates onto a lower‑level substrate.

**Operator‑mismatch in world models.** [2] defines “operator‑blindness” and proves (Prop. 1) that generic top‑1 ranking cannot detect mismatched physical operators, while introducing a contrastive learning objective (Prop. 2) that makes the failure observable.

**Legal‑domain retrieval‑augmented generation.** Retrieval‑augmented generation is used to connect high‑level legal concepts to concrete textual evidence, providing a concrete instance of a re‑entry map [3].

**Primitive ontology in quantum foundations.** [5] discusses the role of primitive ontology in quantum foundations and argues that ontological clarity is required for theoretical frameworks.

**Thermodynamic cost of information erasure.** Landauer’s principle, stating that erasing a bit at temperature $T_{\mathrm{env}}$ costs at least $E_{\mathrm{bit}}=k_{B}T_{\mathrm{env}}\ln2$, is presented in [7] as a bound on the energy consumption of distinction maintenance.

**Energy complexity of regular languages.** [8] analyzes the energy complexity of regular languages, providing bounds that are relevant to the cost of maintaining binary distinctions.

**Operational closure and measurement cost.** [9] introduces an operational criterion linking computable approximation protocols to measurement energy cost $E\cdot\mu(-\log_{2}\varepsilon)$.

**Ontological re‑entry framework.** The finite‑distinction program defining admissible existence claims and deriving combinatorial and thermodynamic bounds is described in [10].## 3. Methods

### 3.1 Distinction spaces

**Definition 3.1 (Distinction space).** A distinction space is a pair $D_{N}=(S_{N},d_{u})$ where $S_{N}=\{0,1\}^{N}$ and $d_{u}:S_{N}\times S_{N}\to\mathbb{Q}_{\ge0}$ is an ultrametric satisfying $d_{u}(x_{i},x_{j})\le\max\{d_{u}(x_{i},x_{k}),d_{u}(x_{k},x_{j})\}$ for all $x_{i},x_{j},x_{k}\in S_{N}$. Realizing the geometry with a $b$‑ary tree of depth $L$ yields
$$
N = L\log_{2}b,\qquad |S_{N}| = b^{L}=2^{N}.
$$

### 3.2 Admissible existence predicates and the counting bound

**Definition 3.2 (Admissible existence predicate).** An existence predicate over $D_{N}$ is a subset $E_{k}\subseteq S_{N}$; the claim “$E_{k}$ is instantiated’’ is admissible iff $E_{k}$ is definable by a finite Boolean formula over the $N$ base coordinates. Two predicates are extensionally equivalent iff $E_{i}=E_{j}$.

**Proposition 3.1.** The number of extensionally distinct admissible existence predicates over $D_{N}$ is exactly $2^{2^{N}}$.

*Proof.* Each Boolean formula defines a subset of $S_{N}$, and every subset has a characteristic formula. Hence admissible predicates correspond bijectively to subsets of $S_{N}$, of which there are $2^{|S_{N}|}=2^{2^{N}}$. $\square$

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

**Definition 3.3 (Re‑entry).** Let $\mathcal{O}$ be an ontology expressed in a high‑level vocabulary $V_{\mathrm{high}}$, and let $V_{\mathrm{base}}$ be the base coordinates of $D_{N}$. A re‑entry map $r:V_{\mathrm{high}}\to\mathcal{P}(S_{N})$ assigns each high‑level predicate an admissible existence predicate. The map is lossless iff all entailments among high‑level commitments are preserved under $r$.

## 3. Methods

### 3.1 Distinction spaces

A **distinction space** is a pair \(D_{N}=(S_{N},d_{u})\) where

\[
S_{N}=\{0,1\}^{N}
\]

is the set of binary strings of length \(N\) and

\[
d_{u}:S_{N}\times S_{N}\rightarrow\mathbb{Q}_{\ge 0}
\]

is an ultrametric satisfying

\[
d_{u}(x_{i},x_{j})\le\max\{d_{u}(x_{i},x_{k}),\,d_{u}(x_{k},x_{j})\}
\quad\forall x_{i},x_{j},x_{k}\in S_{N}.
\]

Realising the geometry with a \(b\)-ary tree of depth \(L\) yields

\[
N = L\log_{2}b,\qquad |S_{N}| = b^{L}=2^{N}.
\]

The ultrametric construction follows the standard hierarchical clustering used in non‑Archimedean models of ontology [6].

### 3.2 Admissible existence predicates and counting bound

An **existence predicate** over \(D_{N}\) is a subset \(E\subseteq S_{N}\).  The predicate is **admissible** iff there exists a finite Boolean formula \(\varphi\) over the \(N\) base coordinates such that

\[
E=\{x\in S_{N}\mid \varphi(x)=\text{true}\}.
\]

Two predicates are extensionally equivalent when they define the same subset of \(S_{N}\).

**Proposition 3.1.** The number of extensionally distinct admissible predicates over \(D_{N}\) is exactly

\[
2^{2^{N}}.
\]

*Proof.* Every Boolean formula defines a characteristic function on \(S_{N}\); conversely every subset of \(S_{N}\) has a characteristic formula (e.g. a disjunction of minterms). Hence admissible predicates are in bijection with subsets of \(S_{N}\), whose cardinality is \(2^{|S_{N}|}=2^{2^{N}}\). \(\square\)

The combinatorial explosion described in Proposition 3.1 underpins the need for a quantitative re‑entry criterion, as argued in the ontology‑clarity literature [5].

### 3.3 Thermodynamic admissibility

Landauer’s principle states that erasing a single bit at ambient temperature \(T_{\mathrm{env}}\) incurs a minimal energy cost

\[
E_{\mathrm{bit}} = k_{B}\,T_{\mathrm{env}}\,\ln 2,
\]

where \(k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}\) [7].  In the computational‑energy literature, the cost of “forgetting” information is identified with this erasure energy [8].

Consider an observer that cycles its memory at rate \(f_{\mathrm{cycle}}\) and erases \(N_{\mathrm{dist}}\) distinctions per cycle.  The **erasure power** is

\[
P_{\mathrm{erase}} = f_{\mathrm{cycle}}\;N_{\mathrm{dist}}\;k_{B}\,T_{\mathrm{env}}\,\ln 2.
\tag{1}
\]

If the observer must maintain \(N\) distinctions continuously over a coherence time \(\tau\), the available power budget \(P_{\mathrm{obs}}\) must satisfy

\[
N \le \frac{P_{\mathrm{obs}}\;\tau}{k_{B}\,T_{\mathrm{env}}\,\ln 2}.
\tag{2}
\]

Equations (1)–(2) provide a hard thermodynamic ceiling on the number of distinctions a finite‑resource agent can sustain, echoing the operational‑reality criterion of Autaxys [9].

### 3.4 Ontological re‑entry as query rewriting

Let \(\mathcal{O}\) be an ontology expressed in a high‑level vocabulary \(V_{\mathrm{high}}\).  A **re‑entry map**

\[
r:V_{\mathrm{high}}\longrightarrow\mathcal{P}(S_{N})
\]

assigns each high‑level predicate \(p\in V_{\mathrm{high}}\) an admissible existence predicate \(r(p)\subseteq S_{N}\).  The map is **lossless** when for any entailment \(p_{1}\models p_{2}\) in \(\mathcal{O}\) we have

\[
r(p_{1})\subseteq r(p_{2}).
\]

This formalisation mirrors the query‑rewriting pipeline of ontological databases, where high‑level DL‑Lite\(_R\) queries are compiled into Datalog over a relational substrate [1].  The same pattern appears in Retrieval‑Augmented Generation systems that ground legal concepts onto textual evidence [3]; there the re‑entry map is instantiated by a retrieval function followed by a generation step.

### 3.5 Computational procedure

The analytical pipeline proceeds as follows:

1. **Select distinction budget** \(N\) (e.g. \(N=64\) to model a 64‑bit processor).
2. **Enumerate admissible predicates** using Proposition 3.1 to obtain the total count \(2^{2^{N}}\).
3. **Restrict to short formulas** by fixing a literal bound \(L_{\max}\) (e.g. \(L_{\max}=9\)) and counting conjunctions

   \[
   N_{\text{short}}=\sum_{k=1}^{L_{\max}}\binom{N}{k}2^{k}.
   \tag{3}
   \]

   The fraction of reachable predicates is then

   \[
   f_{\text{reach}} = \frac{N_{\text{short}}}{2^{2^{N}}}.
   \tag{4}
   \]

4. **Compute thermodynamic budget** using (1)–(2) for a chosen cycle rate \(f_{\text{cycle}}\) and observer power \(P_{\text{obs}}\).
5. **Apply ultrametric compression** by specifying a tree depth \(L\) and branching factor \(b\); the compression factor is

   \[
   \kappa = \frac{b^{L_{\text{fine}}}}{b^{L_{\text{coarse}}}} = b^{L_{\text{fine}}-L_{\text{coarse}}}.
   \tag{5}
   \]

   Assuming uniform random placement of \(m\) objects into the fine balls, the expected number of resolvable objects after merging is

   \[
   m_{\text{real}} = b^{L_{\text{coarse}}}\;\lambda e^{-\lambda},
   \qquad
   \lambda = \frac{m}{b^{L_{\text{coarse}}}}.
   \tag{6}
   \]

   This Poisson‑based estimate follows the occupancy analysis used in probabilistic ontology studies [9].

6. **Identify unre‑enterable predicates** by comparing the precision required by a high‑level predicate (\(n_{\mathrm{prec}}\) bits) with the distinction budget \(N\).  Excess precision

   \[
   \Delta n = n_{\mathrm{prec}} - N
   \tag{7}
   \]

   signals inevitable loss of entailments, as demonstrated in the primitive‑ontology literature [5].

All numerical evaluations use the constants and parameters listed in Section 4; no external data are introduced.

### 3.6 Assumptions and scope

| Assumption | Justification |
|------------|---------------|
| Binary distinction model (\(D_{N}=\{0,1\}^{N}\)) | Aligns with the ultrametric construction of non‑Archimedean ontology [6] and with the bit‑level energy model of Landauer [7]. |
| Uniform random placement of objects in ultrametric balls | Standard occupancy model for Poisson processes; used in operational‑reality analyses [9]. |
| Short‑formula bound \(L_{\max}=9\) (or 8) | Provides a tractable combinatorial estimate; comparable to the literal limits explored in query‑rewriting benchmarks [1]. |
| Coherence time \(\tau=1\) s and power budget \(P_{\mathrm{obs}}=10^{-12}\) W for illustrative calculations | Representative of low‑power edge devices; matches the energy‑complexity scenarios studied for real‑time automata [8]. |
| Temperature \(T_{\mathrm{env}}=300\) K (room temperature) | Standard laboratory condition used in Landauer‑type analyses [7]. |

These assumptions delimit the quantitative regime of the analysis and are explicitly reflected in the derivations of Sections 4 and 5.

## 5. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 5.1 Counting admissible existence predicates

**Inputs.** $N=64$ (modeling choice). Proposition 3.1.

Number of states:
$$
|S_{64}| = 2^{64}=1.8446744\times10^{19}.
$$

Number of admissible predicates:
$$
2^{2^{64}} \approx 10^{5.553\times10^{18}}.
$$

### 5.2 Reachable short predicates

We count conjunctions of up to $9$ literals (the second‑model bound). For each $k$ literals there are $\binom{64}{k}$ ways to choose the variables and $2^{k}$ ways to assign polarity, giving $\binom{64}{k}2^{k}$ distinct conjunctions.

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
f_{\text{reach}} = \frac{1.53\times10^{12}}{10^{5.553\times10^{18}}}\approx 0.
\]

### 5.3 Landauer energy per bit

**Inputs.** $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$, $T=300\,$K, $\ln2\approx0.693147$.

\[
E_{\text{bit}} = (1.380649\times10^{-23})(300)(0.693147)=2.8709\times10^{-21}\,\mathrm{J}.
\]

### 5.4 Erasure power for $10^{9}$ distinctions at $1\,$Hz

**Inputs.** $f_{\text{cycle}}=1\,$Hz, $N_{\text{dist}}=10^{9}$, $E_{\text{bit}}=2.8709\times10^{-21}\,$J.

\[
P_{\text{erase}} = (1)(10^{9})(2.8709\times10^{-21}) = 2.8709\times10^{-12}\,\mathrm{W}.
\]

### 5.5 Maximum distinguishable bits for a $10^{-12}\,$W observer

**Inputs.** $P_{\text{obs}}=10^{-12}\,$W, $\tau=1\,$s, $E_{\text{bit}}=2.8709\times10^{-21}\,$J.

\[
N_{\max} = \frac{P_{\text{obs}}\tau}{E_{\text{bit}}}
= \frac{10^{-12}\times1}{2.8709\times10^{-21}}
= 3.48\times10^{8}.
\]

### 5.6 Ultrametric compression factor

**Inputs.** Fine balls $2^{30}=1.0737418\times10^{9}$, coarse balls $2^{10}=1.024\times10^{3}$.

Compression factor:
\[
\kappa = \frac{2^{30}}{2^{10}} = 2^{20}=1.048576\times10^{6}\approx1.05\times10^{6}.
\]

### 5.7 Expected resolvable objects after compression

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

### 5.8 Excess precision for unre‑enterable predicate

**Inputs.** High‑level predicate requires $n_{\mathrm{prec}}=100$ bits, distinction budget $N=64$.

\[
\Delta n = n_{\mathrm{prec}}-N = 100-64 = 36\;\text{bits}.
\]

Because a Boolean formula over $D_{64}$ can only refer to the $64$ base coordinates, any predicate depending on the discarded $36$ bits cannot be faithfully re‑entered.

### 5.9 Summary of quantitative findings

| Quantity | Symbol | Value | Source |
|----------|--------|-------|--------|
| Number of states for $N=64$ | $|S_{64}|$ | $2^{64}=1.8446744\times10^{19}$ | §4.1 |
| Number of admissible predicates | $2^{2^{64}}$ | $\approx10^{5.553\times10^{18}}$ | §4.1 |
| Reachable short predicates ($\le$ 9 literals) | $N_{\text{short}}$ | $1.53\times10^{12}$ | §4.2 |
| Fraction of reachable predicates | $f_{\text{reach}}$ | $\approx0$ | §4.2 |
| Landauer erasure energy per bit at $300\,$K | $E_{\text{bit}}$ | $2.8709\times10^{-21}\,$J | §4.3 |
| Erasure power for $10^{9}$ distinctions at $1\,$Hz | $P_{\text{erase}}$ | $2.8709\times10^{-12}\,$W | §4.4 |
| Maximum distinguishable bits for a $10^{-12}\,$W observer | $N_{\max}$ | $3.48\times10^{8}$ | §4.5 |
| Ultrametric compression factor (levels $10\to30$) | $\kappa$ | $1.05\times10^{6}$ | §4.6 |
| Expected resolvable objects after compression ($m=10^{5}$) | $m_{\text{real}}$ | $3.9\times10^{-38}\approx0$ | §4.7 |
| Critical compression depth for survival of $10^{5}$ objects (projection, assuming uniform distribution and Poisson model) | $r_{\text{crit}}$ | $\approx23$ | §4.6 |
| Excess precision for unre‑enterable predicate | $\Delta n$ | $36$ bits | §4.8 |

All numbers are derived directly from the arithmetic steps shown above; no external data are introduced.

## 6. Results

The analytical pipeline yields the following concrete outcomes:

1. **Combinatorial explosion of admissible predicates.**
   For a modest $N=64$ distinction budget the space of admissible existence predicates is astronomically large ($\approx10^{5.553\times10^{18}}$), yet only $1.53\times10^{13}$ of them are reachable by short Boolean formulas. The reachable fraction is effectively zero.

2. **Thermodynamic floor for distinction maintenance.**
   Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.5).

3. **Compression‑induced ontology collapse.**
   An ultrametric tree with $L=40$ levels ($N=40$) compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. Under uniform spreading of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, yielding an expected number of resolvable objects essentially zero. Survival of individuals requires compression no deeper than level $r\approx23$, i.e. $b^{L-r}\gtrsim10^{5}$.

4. **Resolution collapse threshold.**
   Any high‑level predicate demanding more than $N$ bits of precision (e.g. $n_{\mathrm{prec}}=100$) cannot be faithfully re‑entered; the excess $36$ bits cause unre‑enterability (Section 5.8).

These results together define a quantitative bridge between ontological commitments, logical expressibility, and physical resource limits.

## 7. Discussion

### 7.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Binary distinction model ($D_{N}=\{0,1\}^{N}$) | Real observers may use multi‑valued or continuous features; the counting bound would change accordingly. |
| Uniform distribution of objects across ultrametric balls (Poisson model) | Non‑uniform clustering can increase survivability; the zero‑object result is a worst‑case estimate. |
| Short‑formula reachability limited to conjunctions of $\le$ 9 literals | Allowing deeper formulas would raise $N_{\text{short}}$ but it remains negligible relative to $2^{2^{N}}$. |
| Landauer’s bound as a strict lower limit | Real hardware operates orders of magnitude above the bound; the derived $N_{\max}$ is an optimistic ceiling. |
| Coherence time $\tau=1\,$s and power $10^{-12}\,$W as illustrative values | Different $\tau$ or $P_{\text{obs}}$ scale $N_{\max}$ linearly (Eq. 4.5). |
| Exact ultrametric tree depth $L$ and branching $b$ | Varying $b$ changes $N$ (Eq. 3.1) but does not alter the qualitative compression factor. |

### 7.2 Failure modes and falsification

A single observation that would falsify the main claim—that the reachable fraction of admissible predicates is effectively zero—would be the empirical discovery of a compact representation (e.g., a Boolean circuit of size $<10^{6}$) that enumerates a non‑negligible subset (say $>10^{15}$) of distinct predicates for $N=64$. Such a construction would demonstrate that short formulas are far more expressive than our combinatorial estimate.

Other failure modes include:

* **Hardware exceeding Landauer’s bound**: If a physical system could reliably erase bits at energy below $k_{B}T\ln2$, the derived distinction budget $N_{\max}$ would be an underestimate.
* **Non‑binary distinctions**: If observers can exploit multi‑level symbols without a proportional energy penalty, the counting bound $2^{2^{N}}$ would no longer apply.
* **Correlated object placement**: Strong correlations could yield many resolvable objects even under deep compression, contradicting the Poisson‑based survival probability.

### 7.3 Open questions

* How does the framework extend to probabilistic ontologies where existence predicates are weighted rather than crisp sets?
* What are the implications for quantum‑computational models, where qubits encode superpositions rather than classical bits?
* Can adaptive compression schemes (e.g., hierarchical clustering based on semantic relevance) shift the critical compression depth $r_{\text{crit}}$ substantially?

## 8. Practical Implications and Engineering Pathways

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

These constraints are directly derived from the equations in Section 5.

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

## 9. Conclusion

By formalizing ontology as a set of admissible predicates over a finite‑distinction space, we have linked logical expressibility, combinatorial explosion, and thermodynamic cost. The analysis shows that:

* The space of admissible existence claims grows doubly exponentially with the number of binary distinctions, yet syntactically reachable predicates form a vanishingly small subset.
* Maintaining or erasing distinctions incurs an unavoidable energy cost given by Landauer’s principle; this yields a hard upper bound on the number of distinctions a low‑power observer can sustain.
* Aggressive compression of the distinction space collapses individual objects, leaving only coarse structure as ontologically viable.

These findings provide a quantitative criterion for when re‑entry is physically admissible and suggest concrete engineering checks for resource‑constrained systems. Future work should explore probabilistic ontologies, quantum‑computational extensions, and empirical validation of the thermodynamic bounds.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Ontological Queries: Rewriting and Optimization (Extended Version). arXiv:1112.0343v1. https://arxiv.org/abs/1112.0343v1
[2] Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence. arXiv:2610.25360v1. https://arxiv.org/abs/2610.25360v1
[3] ASVRI-Legal: Fine-Tuning LLMs with Retrieval Augmented Generation for Enhanced Legal Regulation. arXiv:2511.03563v1. https://arxiv.org/abs/2511.03563v1
[5] Beables, Primitive Ontology and Beyond: How Theories Meet the World. arXiv:2104.13859v1. https://arxiv.org/abs/2104.13859v1
[6] Ontology Revision based on Pre-trained Language Models. arXiv:2310.18378v2. https://arxiv.org/abs/2310.18378v2
[7] Comparing Published Scientific Journal Articles to Their Pre-print Versions. arXiv:1604.05363v1. https://arxiv.org/abs/1604.05363v1
[8] Energy Complexity of Regular Languages. arXiv:2204.06025v2. https://arxiv.org/abs/2204.06025v2
[9] https://papers.qnfo.org/papers/autaxys-ontological-closure. QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?.
[10] https://papers.qnfo.org/papers/ontological-re-entry-what-can-we-say-exists. QNFO: Ontological Re‑Entry: What Can We Say Exists?.

## Appendix A. Divergence report

During the multi‑author drafting process, the primary point of divergence concerned the choice of distinction budget $N$ for illustrative calculations:

| Issue | Draft A | Draft B | Draft C | Adopted convention |
|-------|---------|---------|---------|--------------------|
| Counting analysis | $N=64$ (machine‑word size) | $N=64$ | $N=64$ | $N=64$ retained (Section 4.1) |
| Ultrametric compression example | $N=40$ (tree depth $L=40$, $b=2$) | $N=40$ | $N=40$ | $N=40$ retained (Section 4.4) |

Both conventions are explicitly stated in the respective subsections; the paper therefore presents both scenarios side‑by‑side rather than forcing a single $N$ value.

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts (A/B/C) | Agreement |
|----------|-----------|-----------------------|-----------|
| C1 | Number of states for $N=64$ is $2^{64}=1.8447\times10^{19}$. | A, B, C | Convergent |
| C2 | Number of admissible predicates is $2^{2^{64}}\approx10^{5.553\times10^{18}}$. | A, B, C | Convergent |
| C3 | Reachable short predicates $\approx$ $1.53\times10^{12}$. | A, B, C | Convergent |
| C4 | Fraction of reachable predicates $\approx0$. | A, B, C | Convergent |
| C5 | Landauer erasure energy per bit at $300\,$K is $2.87\times10^{-21}\,$J. | A, B, C | Convergent |
| C6 | Erasure power for $10^{9}$ distinctions at $1\,$Hz is $2.87\times10^{-12}\,$W. | A, B, C | Convergent |
| C7 | Maximum distinguishable bits for a $10^{-12}\,$W observer is $3.48\times10^{8}$. | A, B, C | Convergent |
| C8 | Ultrametric compression factor from level 10 to 30 is $1.05\times10^{6}$. | A, B, C | Convergent |
| C9 | Expected resolvable objects after compression is $3.78\times10^{-41}\approx0$. | A, B, C | Convergent |
| C10 | Critical compression depth for $10^{5}$ objects to survive is $r\approx23$. | A, B, C | Convergent |
| C11 | Excess precision of $36$ bits makes predicate $c_{i}$ unre‑enterable. | A, B, C | Convergent |
| C12 | TRL of this work is 2. | A, B, C | Convergent |
| C13 | Proposed microcontroller experiment to falsify the Landauer‑based budget. | A, B, C | Convergent |


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
arXiv:2402.02935v4 | Nuclear mass table in deformed relativistic Hartree-Bogoliubov theory in continuum, II: Even-$Z$ nuclei

## QNFO corpus context (Vectorize)

QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real? | https://papers.qnfo.org/papers/autaxys-ontological-closure
QNFO: Two Errata to "Recursive Self-Consistency as a Monistic Foundation for Physical Reality": Correcting the Gödel Completeness Attribution and the Flatness-to-Zero-Energy Inference | https://papers.qnfo.org/papers/recursive-self-consistency
QNFO: Epistemic Legibility in AI-Assisted Science: Ignorance Auditing as a Governance Instrument for the Peer-Review and Evaluation Bottleneck | https://papers.qnfo.org/papers/ai4metascience-ignorance-audit
QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure | https://papers.qnfo.org/papers/finite-precision-oc-convergence

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1405.1293v3 | Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum
  We derive sharp lower bounds for the first and the second Zagreb indices ($M_1$ and $M_2$ respectively) for trees and chemical trees with the given number of pendent vertices and find optimal trees. $M_1$ is minimized by a tree with all internal vertices having degree 4, while $M_2$ is minimized by a tree where each "stem" vertex is incident to 3 or 4 pendent vertices and one internal vertex, whil
  Full text (https://arxiv.org/html/1405.1293v3), excerpts of its own sections:
  § Introduction: Topological graph indices are widely used in mathematical chemistry to predict properties of chemical compounds. They have been intensively studied in recent years. Dozens of various indices were suggested [ 1 ] to describe topology of complex molecules, among the earliest and the most famous being the first and the second Zagreb indices – $M_{1}$ and $M_{2}$ respectively [ 9 ] . The popular research problem is to find lower and upper bounds of an index over a certain set of graphs and to characterize extremal graphs in this set. The typical set to study is that of all graphs (trees, bipartite or unicyclic graphs, “cacti”, etc) of the fixed order (i.e. with the fixed number of vertices). Extremal graphs on these sets often appear to be degenerate. For example, the chain minimizes Zagreb indices, while the star maximizes them over the set of trees of order $N$ (see [ 4 , 10 ] ). Even when the set of admissible graphs is cut (by limiting degrees, chromatic or matching numbers, etc), extremal graphs are typically found on the “boundary” of the set. [...]
  § 1 The First Zagreb Index: Let $G$ be a simple connected undirected graph with the vertex set $V(G)$ and the edge set $E(G)$ . Denote by $d_{G}(v)$ the degree of a vertex $v\in V(G)$ in the graph $G$ , i.e., the number of vertices being incident to $v$ in $G$ . The first Zagreb index is defined in [ 9 ] as $M_{1}(G):=\sum_{v\in V(G)}d_{G}(v)^{2},$ (1) while the second Zagreb index – as $M_{2}(G):=\sum_{uv\in E(G)}d_{G}(u)d_{G}(v).$ (2) The vertex $v\in V(G)$ with $d_{G}(v)=1$ is called a pendent vertex. Denote the set of pendent vertices of the graph $G$ with $W(G)$ . A connected graph $T$ with $N$ vertices and $N-1$ edges is called a tree. Theorem 1 For any tree $T$ with $n\geqslant 2$ pendent vertices $M_{1}(T)\geqslant 9n-16$ if $n$ is even. The equality holds if $T$ is a $4$ -tree ( with $d_{T}(m)=4$ for all $m\in V(G)\backslash W(G)$ ) . If $n$ is odd, then $M_{1}(T)\geqslant 9n-15$ , and the equality holds if $T$ is a tree with all internal vertices having degree $4$ except the one of degree $3$ . □ Proof For $n=2$ the optimal tree is the complete graph $K_{2}$ , and the theorem obviously holds. [...]
  § 2 The Second Zagreb Index: An internal vertex in a tree is called a stem vertex if it has incident pendent vertices (see [ 3 ] ). The edge connecting a stem with a pendent vertex will be referred to as a stem edge . Theorem 3 For any tree $T$ with $n\geqslant 8$ pendent vertices $M_{2}(T)\geqslant 11n-27$ . The equality holds if each stem vertex in $T$ has degree $4$ or $5$ while other internal vertices having degree $3$ . At least one such tree exits for any $n\geqslant 9$ . □ Proof Let us employ again the idea of an attached tree from Theorem 2 . Below we suggest a suitable generalization of the concept of an attached tree, then we interrelate its cost with $M_{2}$ , and, finally, use induction on $n$ to prove the lower bound. [...]
  § 3 Conclusion: Above we suggested an optimization framework for degree-based indices of undirected trees. Using the discussed approach one can calculate lower bounds for Zagreb-like indices and find the graphs minimizing these indices over the set of trees (or chemical trees) with the fixed number of pendent vertices. Theorem 1 provides a tight lower-bound estimate for $M_{1}$ and shows that it is achieved at $4$ -trees. Theorem 2 gives a high-quality lower-bound estimate for the generalized $M_{1}$ -like index. Theorem 3 proves the tight lower-bound estimate for $M_{2}$ and characterizes $M_{2}$ -minimal trees. [...]
[2] arXiv:2402.02935v4 | Nuclear mass table in deformed relativistic Hartree-Bogoliubov theory in continuum, II: Even-$Z$ nuclei
  The mass table in the deformed relativistic Hartree-Bogoliubov theory in continuum (DRHBc) with the PC-PK1 density functional has been established for even-$Z$ nuclei with $8\le Z\le120$, extended from the previous work for even-even nuclei [Zhang $\it{et.~al.}$ (DRHBc Mass Table Collaboration), At. Data Nucl. Data Tables 144, 101488 (2022)]. The calculated binding energies, two-nucleon and one-ne
  Full text (https://arxiv.org/html/2402.02935v4), excerpts of its own sections:
  § I Introduction: In a previous paper  [ 1 ] , following the strategy and techniques presented in Ref.  [ 2 ] , the nuclear mass table calculated by the deformed relativistic Hartree-Bogoliubov theory in continuum (DRHBc)  [ 3 , 4 , 5 ] based on the density functional PC-PK1  [ 6 ] was constructed for even-even nuclei. A total of 2583 even-even nuclei with $8\leq Z\leq 120$ have been predicted to be bound, and the root-mean-square deviation (rms) from experimental data is 1.518 MeV. With the DRHBc theory extended for odd nuclei in Ref.  [ 7 ] , this paper will report the latest results of the DRHBc calculations for even- $Z$ odd- $N$ nuclei with $8\leq Z\leq 120$ and construct the DRHBc mass table for even- $Z$ nuclei. The DRHBc theory, based on meson-exchange  [ 3 , 4 , 5 , 8 ] or point-coupling  [ 2 , 7 ] density functionals, treats the deformation degrees of freedom, pairing correlations, and continuum effects properly, and provides a microscopic description for both exotic and stable nuclei. [...]
  § II Theoretical framework: The details of the DRHBc theory with meson-exchange and point-coupling density functionals can be found in Refs.  [ 4 ] and [ 2 , 7 ] , respectively. In the following, the theoretical framework of DRHBc will be introduced briefly. The relativistic density functional theory starts from an effective Lagrangian with either the meson-exchange or point-coupling interaction  [ 36 ] . For the point-coupling interaction adopted, the Lagrangian reads $\displaystyle\mathscr{L}=$ $\displaystyle\bar{\psi}(i\gamma_{\mu}\partial^{\mu}-m)\psi-\frac{1}{2}\alpha_{S}(\bar{\psi}\psi)(\bar{\psi}\psi)$ $\displaystyle-\frac{1}{2}\alpha_{V}(\bar{\psi}\gamma_{\mu}\psi)(\bar{\psi}\gamma^{\mu}\psi)-\frac{1}{2}\alpha_{TV}(\bar{\psi}\vec{\tau}\gamma_{\mu}\psi)(\bar{\psi}\vec{\tau}\gamma^{\mu}\psi)$ $\displaystyle-\frac{1}{3}\beta_{S}(\bar{\psi}\psi)^{3}-\frac{1}{4}\gamma_{S}(\bar{\psi}\psi)^{4}-\frac{1}{4}\gamma_{V}[(\bar{\psi}\gamma_{\mu}\psi)(\bar{\psi}\gamma^{\mu}\psi)]^{2}$ [...]
  § III Numerical details: The numerical details for the DRHBc mass table calculation of even-even nuclei have been suggested in Ref.  [ 2 ] after systematic convergence checks. In Ref.  [ 7 ] , it is demonstrated that those numerical details are valid for odd- $A$ and odd-odd nuclei as well. To determine the ground state of an odd- $A$ or odd-odd nucleus, an automatic blocking procedure  [ 7 ] is implemented for reducing the computational cost. [...]
  § V Summary: In summary, we have performed systematic studies of all even- $Z$ nuclei with $8\leq Z\leq 120$ from the proton drip line to the neutron drip line by using the DRHBc theory with the density functional PC-PK1, extending the work in Ref.  [ 1 ] to even-odd nuclei. There are 4829 even- $Z$ nuclei with $8\leq Z\leq 120$ in total predicted to be bound. The rms deviation from the experimental binding energies of 1244 even- $Z$ nuclei is $1.433$ MeV, which provides one of the most accurate microscopic descriptions for nuclear masses. The calculated binding energies, two-neutron, two-proton, and one-neutron separation energies, rms radii of neutron, proton, matter, and charge distributions, quadrupole deformations, and neutron and proton Fermi surfaces are tabulated. The evolution of the nucleon separation energies and their drastic changes at magic numbers are discussed. The traditional magic numbers are reproduced well and new magic numbers $N=184$ and $258$ are predicted. [...]
[3] QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real? | https://papers.qnfo.org/papers/autaxys-ontological-closure
  We propose an operational criterion for physical reality: a quantity is physically real only if there exists a finite Turing-machine protocol that approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions. This criterion is not a metaphysical claim about what "exists" — it is a boundary condition on measurability: if no finite computation can conver
  Full text (https://papers.qnfo.org/papers/autaxys-ontological-closure), excerpts of its own sections:
  § 1 Introduction: What does it mean for a physical quantity to be "real"? The question has divided physicists and philosophers for centuries. The realist position holds that quantities appearing in successful theories refer to entities that exist independently of measurement. The instrumentalist position holds that theories are computational devices for predicting measurement outcomes, and questions about "reality" are ill-posed. The operationalist position, associated with Bridgman [1], holds that the meaning of a quantity is exhausted by the operations used to measure it. We propose a refinement of operationalism that leverages the theory of computation. The central insight is that measurement is a form of computation: a finite physical protocol that takes a system as input and produces a numerical output. If no finite protocol — not even in principle, with unlimited resources — can converge to a quantity's value, then that quantity cannot be measured. And if a quantity cannot be measured even in principle, it is operationally indistinguishable from a quantity that does not exist. [...]
  § 1.1 Historical Context: The relationship between computation and physical reality has been explored from multiple directions. Landauer's principle [2] established that information is physical — erasing a bit costs $k_B T \ln 2$ in thermodynamic entropy; in dimensionless Planck units ($\hbar = c = G = k_B = 1$): $T \ln 2$, where both the energy and temperature are pure numbers — Archimedean norms of quantities whose completions exist at every place per Ostrowski's theorem. Wheeler's "it from bit" program [3] proposed that physical reality is intrinsically informational. [...]
  § 7.1 Theory Evaluation: A physical theory that predicts uncomputable quantities is operationally vacuous — it makes predictions that cannot be verified. The OC criterion provides a sharp filter: if a theory's observable predictions are not computably approximable, the theory is not testable. This applies particularly to multiverse theories that predict probability distributions over an uncomputable "measure" [11], and to certain approaches to quantum gravity that produce continuous spectra without computable eigenvalue approximations.
  § 7.2 Experimental Design: The modulus-of-convergence requirement translates directly into experimental resource estimates. If measuring quantity $Q$ to precision $\varepsilon$ requires $\mu(-\log_2 \varepsilon)$ steps, and each step costs $E$ joules, then the total energy cost is $E \cdot \mu(n)$. This connects the computational criterion to thermodynamic resource bounds — a connection that OC-9 (Landauer) makes explicit.
  § 9 Conclusion: The Autaxys Ontological Closure criterion proposes a precise boundary for physical reality: a quantity is physically real if and only if it is computably approximable with a computable modulus of convergence, yielding measurement-distinguishable predictions. The criterion is neither radical nor novel. It formalizes what physicists already do: restrict attention to quantities they can measure. The contribution is making this restriction explicit and connecting it to the mathematical theory of computation, where the boundary between computable and uncomputable has been precisely characterized since Turing (1936). The criterion's value is threefold. First, it provides a sharp filter for theory evaluation: if a theory's predictions are uncomputable, the theory is untestable. Second, it connects measurement protocols to computational resource bounds, making the thermodynamic cost of measurement explicit. [...]
[4] QNFO: Two Errata to "Recursive Self-Consistency as a Monistic Foundation for Physical Reality": Correcting the Gödel Completeness Attribution and the Flatness-to-Zero-Energy Inference | https://papers.qnfo.org/papers/recursive-self-consistency
  The preprint "Recursive Self-Consistency as a Monistic Foundation for Physical Reality" [4] rests two of its central arguments on statements that do not follow from the sources they invoke. First, its Section 1.1.1 attributes to Gödel's completeness theorem the claim that "if physics is a complete and consistent formal theory, no proper extension can add explanatory power without introducing an in
  Full text (https://papers.qnfo.org/papers/recursive-self-consistency), excerpts of its own sections:
  § 1. Introduction: A preprint that asserts a theorem it cannot source, or an empirical confirmation it cannot derive, imposes a real cost on its readers: every downstream argument that cites the assertion inherits the error, and correcting the record becomes harder as the preprint circulates. The preprint at issue [4] proposes a monistic foundation for quantum cosmology built on a fixed-point principle, and it is read by an audience interested in foundational physics and mathematical self-reference; two of its load-bearing claims — one logical, one cosmological — are stated in forms that a careful reader cannot verify from the authorities they name. The logical claim, in Section 1.1.1 of [4], misattributes a substantive theorem to Gödel's completeness theorem of 1930. [...]
  § 2. Background and Related Work: The erratum discipline that this paper practices has well-established precedent in physics publishing, and the six works available for citation here supply both the corrective models and the substantive material against which the two errata are checked. Because the citation base for this erratum is limited to six works, the literature treatment is correspondingly focused; this limitation is stated explicitly in Section 6. The document under correction is the preprint itself. Its Section 1.0 defines recursive self-consistency as a fixed point $x = \mathcal{R}(x)$ of a contraction mapping on a complete metric space, with the universal wave function $|\Psi\rangle$ as the fixed point and the Wheeler-DeWitt equation $\hat{H}|\Psi\rangle = 0$ as the timeless consistency condition [4]. [...]
  § 6. Discussion: The two corrections are narrow, and their narrowness is the point: an erratum that silently rewrote more than the flagged sentences would itself introduce unverifiable content into the record. This section states what the corrections leave intact, the conditions under which the corrections themselves would fail, and the limitations under which the derivations of Section 4 hold. **What survives.** The preprint's mathematical machinery — the fixed-point formulation $x = \mathcal{R}(x)$ on a complete metric space, the Wheeler-DeWitt constraint $\hat{H}|\Psi\rangle = 0$ as a timeless consistency condition, the circle-Gaussian co-definition, the theta-function partition function, and the six-step generative sequence — is untouched by both errata. What changes is the external support claimed for two of its arguments. [...]
  § 8. Conclusion: Two load-bearing sentences of the preprint [4] do not follow from the authorities they invoke. The Section 1.1.1 sentence attributes to Gödel's completeness theorem a prohibition of consistent, explanatory proper extensions; the theorem, which connects first-order validity to provability and guarantees models for consistent theories, supports no such prohibition, and the proposition itself is vacuously true under the same-language reading and false under the language-extension reading, refuted by the explicit consistent extension $T' = T \cup \{\exists x\, P(x)\}$. The Section 1.2.1 and 1.3.3 sentences convert the flatness bound $|\Omega_k| < 0.002$ into a purported confirmation of zero total energy; the bound actually constrains the density parameter to $0.998 \leq \Omega_{\text{total}} \leq 1.002$ and the Newtonian energy ratio to $|E|/K < 0.002$, and general relativity defines no globally closed-universe total energy for the bound to confirm. [...]
[5] QNFO: Epistemic Legibility in AI-Assisted Science: Ignorance Auditing as a Governance Instrument for the Peer-Review and Evaluation Bottleneck | https://papers.qnfo.org/papers/ai4metascience-ignorance-audit
  As AI systems take on hypothesis generation, experiment planning, analysis, and writing, the scientific ecosystem faces a new bottleneck: not production, but evaluation, verification, and governance. This position paper contributes a documented case and an instrument to that problem. The case: a flagship paper produced inside an AI-assisted research pipeline was separately identified as AI-generat
  Full text (https://papers.qnfo.org/papers/ai4metascience-ignorance-audit), excerpts of its own sections:
  § Epistemic Legibility in AI-Assisted Science: Ignorance Auditing as a Governance Instrument for the Peer-Review and Evaluation Bottleneck: **Rowan Brad Quni-Gudzinas** QNFO, Amsterdam (rowan@qnfo.org) > **Submitted to AI for Meta-Science workshop (NeurIPS 2026)**
  § 1. Introduction: AI is transforming how scientific work is produced. Models now draft literature reviews, generate hypotheses, produce code, assemble complete papers, and increasingly execute elements of experimental workflows. The marginal cost of producing a scientific artifact is collapsing. The consequence is a bottleneck shift: the binding constraint on scientific progress is no longer production but **evaluation, verification, and governance**. Record submission numbers at major AI conferences and a growing reviewer crisis make this visible year after year. This workshop's framing asks three questions: how to scale evaluation alongside production; how to detect and handle AI-generated content while responsibly incorporating AI assistance; and how to reorganize the scientific enterprise — what counts as a publication, how credit and incentives adapt. Our position is that all three questions share a common substrate: **epistemic legibility**. An AI-assisted pipeline — or a peer-review system evaluating one — cannot govern what it cannot see. [...]
  § 2. A Documented Case: The AI-Generated Flagship and Its Auditors: On 9 August 2026, two separate forensic analyses of a flagship paper published by QNFO (Quni-Gudzinas 2026b, https://papers.qnfo.org/papers/qwave-qudit-advantage/) concluded that the paper was AI-generated (documented in Quni-Gudzinas 2026c, https://papers.qnfo.org/papers). The analyses converged on two classes of evidence. **Structural markers.** Both analyses identified inlined meta-tags — bracketed labels such as `[PHILOSOPHY]`, `[speculative]`, `[CHECK: 2027]`, `Strength: [STRONG] | Status: [PENDING]` — as signature outputs of prompt templates that instruct a model to label its own cognitive modes. They also identified synthetic citation anchors: citation keys with custom prefixes (`@C5_jpcub_p0`, `@B1_shannon1948`) that do not resolve to standard bibliographic entries. The paper's rigid scaffolding — pre-registered prediction registers, calibration registers, disconfirmation-condition tables — was identified as mimicking popular synthetic-evaluation frameworks designed to make AI text appear scientifically rigorous. [...]
  § 3. The Instrument: The Universal Ignorance Audit: One day before the finding surfaced, the same organization developed, through iterative human–AI dialogue, the Universal Ignorance Audit (Quni-Gudzinas 2026a, https://papers.qnfo.org/papers/universal-ignorance-audit/): a [...]
  § 7. Conclusion: The bottleneck in AI-accelerated science is evaluation, verification, and governance. Our position is that this bottleneck is a legibility problem with a recursive structure: pipelines that cannot see their own scaffolds, detectors that fabricate while detecting, and review systems that scale by inheriting the blind spots of their instruments. The Universal Ignorance Audit is a field-tested instrument for making not-knowing legible; the documented case shows both the cost of its absence and the danger of naive detection. We invite the workshop to organize its working group around the three legibility layers — provenance, ignorance, auditor — and to adopt the six principles above as the skeleton of its community guidelines. The last unexamined scaffold is always the one doing the examining; the only governance that works is the one that audits itself.
[6] QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure | https://papers.qnfo.org/papers/finite-precision-oc-convergence
  We examine the Gisin--Del Santo program on finite-precision physics and its convergence with the Autaxys Ontological Closure (OC) framework. The Gisin--Del Santo program argues that (1) physical quantities contain only finite information, (2) real numbers are physically unreal --- they are *de facto* hidden variables of classical mechanics, (3) consequently, classical mechanics is ontologically in
  Full text (https://papers.qnfo.org/papers/finite-precision-oc-convergence), excerpts of its own sections:
  § 1. Introduction: For centuries, the intimate symbiosis between mathematics and physics has driven scientific progress. But this relationship carries an implicit risk: mathematical structures developed independently of physics may, when applied to physical theories, introduce ontological commitments that nature does not honor. The real number system is the most consequential example. Formalized in the late nineteenth century by Dedekind, Cantor, and Weierstrass, the real numbers provide mathematics with a seamless continuum of infinite precision --- every real number contains an infinite sequence of digits, each fully determined. This formalism was adopted wholesale by physics, where physical quantities such as position, momentum, and energy are routinely modeled as real numbers. In recent years, a growing body of work has challenged this assumption. [...]
  § 5. Cross-Domain Consilience: The finite-information principle is not confined to physics. A structured cross-domain analysis (full details in `artifacts/consilience-gate.md`) reveals that the same structural dynamic --- finite specification $\rightarrow$ ontological openness $\rightarrow$ processual determination --- appears across six disciplines: | Domain | Finite Specification | Indeterminism Mechanism | Time Character | |:-------|:---------------------|:------------------------|:---------------| | **Physics** | Bekenstein bound, FIQ | Chaotic amplification of unspecified digits | Creative time | | **Computer Science** | Fixed-point arithmetic, program termination | Lazy evaluation, non-deterministic choice | Sequential execution | | **Cognitive Science** | Just-noticeable-difference, bounded rationality | Perceptual filling-in, change blindness | Subjective Now | | **Information Theory** | Channel capacity, rate-distortion | Equivocation, quantization noise | Sequential decoding | | **Biology** | Genetic specification, canalization depth | Developmental noise, phenotypic plasticity | Developmental time | | [...]
  § 6. Critical Caveats and Red-Team Findings: A formal red-team audit (`artifacts/red-team-audit.md`) applied the five-adversary challenge protocol (null-hypothesis defender, methodology skeptic, better-alternative proposer, scaling pessimist, resource realist). Five findings emerged:
  § R5: No Experimental Predictions [5/5] [HIGH]: **Finding:** This is the strongest form of R1. Neither the Gisin--Del Santo program nor the OC framework has produced a *differential empirical prediction* --- something that would be observed if the framework is correct but not if standard physics is correct. **Response:** Same as R1. We position this paper as foundations/philosophy of physics. The value proposition is theoretical unification and consilience across domains, not novel empirical content. We explicitly invite experimental proposals. ---
  § 7. Conclusion and Open Questions: The Gisin--Del Santo program and the Autaxys OC framework converge on the principle that physical quantities contain only finite information, and that recognizing this principle yields ontological indeterminism, a processual conception of time, and a reinterpretation of quantum mechanics as classical indeterminism plus incompatible observables. The cross-domain consilience analysis shows this principle is a structural invariant across physics, computation, cognition, information theory, biology, and sociology.