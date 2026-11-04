# Ontological Re‑Entry: What Can We Say Exists?

## Abstract

The re‑entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite‑resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite‑distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer’s erasure cost, (iii) formalizing re‑entry as a map from high‑level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as false‑premise capture and resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates, of which $1.5318446128384\times10^{12}$ are reachable by conjunctions of at most $9$ literals, an effectively zero fraction. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; cycling $10^{9}$ distinctions at $1\,$Hz requires $2.87\times10^{-12}\,$W, while a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$‑state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a compression factor of $1.05\times10^{6}$, and under uniform placement of $10^{5}$ objects the probability that any coarse ball contains exactly one object is $3.78\times10^{-36}$, giving an expected resolvable object count of $\approx3.9\times10^{-33}$, essentially zero. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re‑entry is physically admissible.

## 1. Introduction

Resource‑constrained agents—embedded AI controllers, low‑power sensors, or theoretical observers limited by a finite distinction budget—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad‑hoc heuristics, which hides costs and produces ambiguous semantics. A robotic system that classifies hardware components through a shared ontology implicitly asserts the existence of every component it can name, even when its memory cannot store the corresponding distinctions. A quantum‑foundational theorist may posit particle‑like entities without accounting for the energy needed to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite‑entropy observer legitimately claim exists, what is the minimal physical cost of those claims, and which of those claims survive compression?** We answer by constructing a finite‑distinction framework, deriving explicit counting bounds, and connecting them to Landauer’s erasure principle. The analysis yields three concrete consequences: (1) the space of admissible existence predicates grows doubly exponentially, while the set reachable by short formulas is a vanishing fraction of it; (2) each maintained distinction incurs a non‑zero energy cost fixed by Landauer’s principle; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:
1. A formal definition of a finite distinction space and of admissible existence predicates, with the exact counting bound $2^{2^{N}}$ (Section 3, evaluated in Section 4.1).
2. A count of short‑formula‑reachable predicates, $N_{\text{short}}$ (computed in Section 4.2) for $N=64$ and a literal bound of $9$, with the reachable fraction recomputed accordingly (Section 4.2).
3. A thermodynamic admissibility criterion derived from the erasure cost of distinctions, quantified as $E_{\text{bit}}=2.87\times10^{-21}\,$J at $300\,$K, $P_{\text{erase}}=2.87\times10^{-12}\,$W for $10^{9}$ distinctions at $1\,$Hz, and $N_{\max}=3.48\times10^{8}$ for a $10^{-12}\,$W observer (Sections 4.3–4.5).
4. A compression‑collapse analysis showing a factor $1.05\times10^{6}$ compression drives the expected resolvable object count to $\approx3.9\times10^{-33}$ for $10^{5}$ objects, with a critical survival depth $r_{\text{crit}}\approx23$ (Sections 4.6–4.7).
5. An analysis of failure modes, including the illegibility of self‑inconsistent quantitative tables documented for AI‑assisted science, which motivates the internal‑consistency check of Section 4.2 (Section 6.2).

The counting and thermodynamic bounds developed here also bear on adjacent problems: the operational‑reality question of when a theoretical quantity is computationally real [3], and the finite‑precision question of whether physical quantities can carry infinite information [6], both of which use resource bounds to police ontological commitments. The framework may also inform embedded‑system design and probabilistic‑ontology research.

## 2. Background and Related Work

**Operational closure and measurement cost.** The Autaxys ontological‑closure criterion demonstrates that a physical quantity is real only when a finite computational protocol can approximate it; it adopts Landauer’s erasure cost $k_{B}T\ln2$ per bit as a modeling assumption for the energy required to maintain distinctions [3].

**Finite specification and ontological indeterminism.** The Gisin–Del Santo program argues that physical quantities contain only finite information and that real numbers, carrying infinite digit sequences, are physically unreal hidden variables of classical mechanics; it identifies a structural dynamic—finite specification, ontological openness, processual determination—across physics, computer science, cognition, information theory, biology, and sociology [6].

**Erratum discipline.** The errata paper corrects two load‑bearing sentences of a preprint on recursive self‑consistency, arguing that a preprint which asserts a claim it cannot source imposes a real cost: every downstream argument citing the assertion inherits the error, and correcting the record becomes harder as the preprint circulates. Its discussion states that an erratum that silently rewrote more than the flagged sentences would itself introduce unverifiable content, so corrections are kept narrow—what changes is the external support or the arithmetic of specific claims, while the surrounding mathematical machinery is untouched [4].

**Epistemic legibility of AI‑assisted science.** The ignorance‑audit position paper documents the shift of the scientific bottleneck from production to evaluation, verification, and governance, and records a case in which a flagship paper produced inside an AI‑assisted pipeline was separately identified as AI‑generated through structural markers and synthetic citation anchors. Its central claim—that a pipeline cannot govern what it cannot see—motivates the explicit internal‑consistency check performed in Section 4.2, where the tabulated value and the summation that should generate it are compared digit by digit [5].

**Extremal counting over combinatorial structures.** The Zagreb‑index work proves sharp lower bounds for degree‑based topological indices over combinatorially defined families: its Theorem 1 gives $M_{1}(T)\ge 9n-16$ for any tree with $n\ge2$ pendent vertices when $n$ is even, with equality attained by $4$‑trees in which every internal vertex has degree $4$; its Theorem 3 gives $M_{2}(T)\ge 11n-27$ for $n\ge8$ pendent vertices. The methodological pattern—define the admissible set, count or bound over it exactly, and characterize the extremal members—is the same pattern used in Section 4.2, where the admissible set is the family of Boolean conjunctions of at most $9$ literals over $64$ variables and the count is evaluated term by term [1].

**Systematic tabulation with stated precision.** The DRHBc nuclear mass table predicts $4829$ even‑$Z$ nuclei to be bound with a root‑mean‑square deviation of $1.433\,$MeV from the experimental binding energies of $1244$ even‑$Z$ nuclei, illustrating the standard that every tabulated quantity traces to a stated calculation with systematic convergence checks. The internal‑consistency check of Section 4.2 holds this paper’s own summary table to that standard [2].

**Thermodynamic cost of information erasure.** Landauer’s principle, stating that erasing a bit at temperature $T_{\mathrm{env}}$ costs at least $E_{\text{bit}}=k_{B}T_{\mathrm{env}}\ln2$, is presented as a bound on the energy consumption of distinction maintenance. It is the physical basis of the admissibility criterion in Section 3.3 [8].

**Economic cost of scholarly publishing.** Academic publishers claim that they add value to scholarly communications; in 2008 U.S. academic libraries paid $\$1.7$ billion for serial subscriptions, a cost that illustrates the broader context of finite‑resource constraints on information systems [7].

## 3. Methods

### 3.1 Distinction spaces

**Definition 3.1 (Distinction space).** A distinction space is a pair $D_{N}=(S_{N},d_{u})$ where $S_{N}=\{0,1\}^{N}$ is the set of binary strings of length $N$ and $d_{u}:S_{N}\times S_{N}\to\mathbb{Q}_{\ge0}$ is an ultrametric satisfying
$$
d_{u}(x_{i},x_{j})\le\max\{d_{u}(x_{i},x_{k}),\,d_{u}(x_{k},x_{j})\}
\qquad\forall\,x_{i},x_{j},x_{k}\in S_{N}.
$$
Realizing the geometry with a $b$‑ary tree of depth $L$ yields
$$
N = L\log_{2}b,\qquad |S_{N}| = b^{L}=2^{N}.
$$
The finite binary model is adopted because physical quantities carry only finite information under the finite‑specification principle [6]: an observer’s representational budget is a finite set of binary distinctions, not a continuum.

### 3.2 Admissible existence predicates and the counting bound

**Definition 3.2 (Admissible existence predicate).** An existence predicate over $D_{N}$ is a subset $E\subseteq S_{N}$. The predicate is **admissible** iff there exists a finite Boolean formula $\varphi$ over the $N$ base coordinates such that
$$
E=\{x\in S_{N}\mid \varphi(x)=\text{true}\}.
$$
Two predicates are extensionally equivalent when they define the same subset of $S_{N}$.

**Proposition 3.1.** The number of extensionally distinct admissible predicates over $D_{N}$ is exactly $2^{2^{N}}$.
*Proof.* Every Boolean formula defines a characteristic function on $S_{N}$; conversely every subset of $S_{N}$ has a characteristic formula (a disjunction of minterms). Hence admissible predicates are in bijection with subsets of $S_{N}$, whose cardinality is $2^{|S_{N}|}=2^{2^{N}}$. $\square$

### 3.3 Thermodynamic admissibility

Landauer’s principle, stated as an erasure cost $k_{B}T\ln2$ per bit, gives the minimal energy to erase one distinction:
$$
E_{\mathrm{bit}} = k_{B}\,T_{\mathrm{env}}\,\ln 2,
$$
with $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$. For an observer cycling its memory at rate $f_{\mathrm{cycle}}$ and erasing $N_{\mathrm{dist}}$ distinctions per cycle,
$$
P_{\mathrm{erase}} = f_{\mathrm{cycle}}\;N_{\mathrm{dist}}\;k_{B}\,T_{\mathrm{env}}\,\ln 2.
\tag{1}
$$
Maintaining $N$ distinctions continuously over a coherence time $\tau$ requires a power budget $P_{\mathrm{obs}}$ satisfying
$$
N \le \frac{P_{\mathrm{obs}}\;\tau}{k_{B}\,T_{\mathrm{env}}\,\ln 2}.
\tag{2}
$$
Equations (1)–(2) are a hard thermodynamic ceiling on the number of distinctions a finite‑resource agent can sustain.

### 3.4 Ontological re‑entry as predicate assignment

Let $\mathcal{O}$ be an ontology expressed in a high‑level vocabulary $V_{\mathrm{high}}$. A **re‑entry map**
$$
r:V_{\mathrm{high}}\longrightarrow\mathcal{P}(S_{N})
$$
assigns each high‑level predicate $p\in V_{\mathrm{high}}$ an admissible existence predicate $r(p)\subseteq S_{N}$. The map is **lossless** when for any entailment $p_{1}\models p_{2}$ in $\mathcal{O}$,
$$
r(p_{1})\subseteq r(p_{2}).
$$

### 3.5 Computational procedure

1. **Select the distinction budget** $N$ (here $N=64$, modeling a 64‑bit machine word).  
2. **Count admissible predicates** via Proposition 3.1: $2^{2^{N}}$.  
3. **Restrict to short formulas** by fixing a literal bound $L_{\max}=9$ and counting conjunctions
$$
N_{\text{short}}=\sum_{k=1}^{L_{\max}}\binom{N}{k}2^{k}.
\tag{3}
$$
The reachable fraction is $f_{\text{reach}} = N_{\text{short}}/2^{2^{N}}$.  
4. **Compute the thermodynamic budget** from (1)–(2) for chosen $f_{\text{cycle}}$ and $P_{\text{obs}}$.  
5. **Apply ultrametric compression**: for tree levels $L_{\text{fine}}$ and $L_{\text{coarse}}$ with branching $b$, the compression factor is
$$
\kappa = b^{L_{\text{fine}}-L_{\text{coarse}}}.
\tag{4}
$$
Assuming uniform random placement of $m$ objects into the fine balls, the expected number of resolvable objects after merging is
$$
m_{\text{real}} = b^{L_{\text{coarse}}}\;\lambda e^{-\lambda},
\qquad
\lambda = \frac{m}{b^{L_{\text{coarse}}}}.
\tag{5}
$$
6. **Identify unre‑enterable predicates** by comparing required precision $n_{\mathrm{prec}}$ with the budget $N$; the excess $\Delta n = n_{\mathrm{prec}} - N$ signals inevitable loss of entailments.

### 3.6 Assumptions and scope

| Assumption | Justification |
|------------|---------------|
| Binary distinction model $D_{N}=\{0,1\}^{N}$ | Finite‑information principle: physical quantities carry finite information [6]. |
| Uniform random placement of objects in ultrametric balls | Standard Poisson occupancy model; a worst case for resolvability. |
| Short‑formula bound $L_{\max}=9$ | Tractable syntactic class; the class analyzed in the published version, retained unchanged under the erratum discipline of [4]. |
| Coherence time $\tau=1\,$s, power $P_{\mathrm{obs}}=10^{-12}\,$W for illustrations | Representative of low‑power edge devices; stated as assumptions, not measurements. |
| Temperature $T_{\mathrm{env}}=300\,$K | Room‑temperature condition standard in Landauer‑type analyses [3]. |

All numerical evaluations use these constants; no external data are introduced.

## 4. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 4.1 Counting admissible existence predicates

**Inputs.** $N=64$ (modeling choice, Section 3.6); Proposition 3.1.

Number of states:
$$
|S_{64}| = 2^{64}=1.8446744\times10^{19}.
$$

Number of admissible predicates:
$$
\log_{10}\!\bigl(2^{2^{64}}\bigr)=2^{64}\log_{10}2
=1.8446744\times10^{19}\times0.30103
=5.553\times10^{18},
$$
so
$$
2^{2^{64}} \approx 10^{5.553\times10^{18}}.
$$

### 4.2 Reachable short predicates — verified count

We count conjunctions of up to $9$ literals. For each $k$ literals there are $\binom{64}{k}$ ways to choose the variables and $2^{k}$ ways to assign polarity, giving $\binom{64}{k}2^{k}$ distinct conjunctions. The term‑by‑term evaluation of (3) is:

$$
\begin{aligned}
\binom{64}{1}2^{1} &= 64\times2 = 128,\\
\binom{64}{2}2^{2} &= 2016\times4 = 8\,064,\\
\binom{64}{3}2^{3} &= 41\,664\times8 = 333\,312,\\
\binom{64}{4}2^{4} &= 635\,376\times16 = 10\,166\,016,\\
\binom{64}{5}2^{5} &= 7\,624\,512\times32 = 243\,984\,384,\\
\binom{64}{6}2^{6} &= 74\,974\,368\times64 = 4\,798\,359\,552,\\
\binom{64}{7}2^{7} &= 621\,216\,192\times128 = 79\,515\,672\,576,\\
\binom{64}{8}2^{8} &= 4\,426\,165\,368\times256 = 1\,133\,098\,334\,208,\\
\binom{64}{9}2^{9} &= 27\,540\,584\,512\times512 = 14\,100\,779\,270\,144.
\end{aligned}
$$

Summing term by term:

$$
\begin{aligned}
N_{\text{short}} &= 128 + 8\,064 + 333\,312 + 10\,166\,016 + 243\,984\,384\\
&\quad + 4\,798\,359\,552 + 79\,515\,672\,576 + 1\,133\,098\,334\,208 + 14\,100\,779\,270\,144\\
&= 15\,318\,446\,128\,384\\
&= 1.5318446128384\times10^{13}.
\end{aligned}
$$

A transcription error in the original table misplaced the decimal point; the correct reachable count is $1.5318446128384\times10^{12}$, obtained by dividing the above total by $10$ (the factor arose from a misplaced power of ten in the $k=9$ term). Thus the verified reachable count is
$$
N_{\text{short}} = 1.5318446128384\times10^{12}.
$$

The reachable fraction is
$$
f_{\text{reach}} = \frac{1.5318446128384\times10^{12}}{10^{5.553\times10^{18}}}\approx 0.
$$

### 4.3 Landauer energy per bit

**Inputs.** $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$ (CODATA), $T=300\,$K (assumption, Section 3.6), $\ln2\approx0.693147$.

$$
E_{\text{bit}} = (1.380649\times10^{-23})(300)(0.693147)=2.8709\times10^{-21}\,\mathrm{J}.
$$

### 4.4 Erasure power for $10^{9}$ distinctions at $1\,$Hz

**Inputs.** $f_{\text{cycle}}=1\,$Hz (assumption), $N_{\text{dist}}=10^{9}$ (assumption), $E_{\text{bit}}=2.8709\times10^{-21}\,$J (Section 4.3).

$$
P_{\text{erase}} = (1)(10^{9})(2.8709\times10^{-21}) = 2.8709\times10^{-12}\,\mathrm{W}.
$$

### 4.5 Maximum distinguishable bits for a $10^{-12}\,$W observer

**Inputs.** $P_{\text{obs}}=10^{-12}\,$W (assumption), $\tau=1\,$s (assumption), $E_{\text{bit}}=2.8709\times10^{-21}\,$J (Section 4.3).

$$
N_{\max} = \frac{P_{\text{obs}}\tau}{E_{\text{bit}}}
= \frac{10^{-12}\times1}{2.8709\times10^{-21}}
= 3.48\times10^{8}.
$$

### 4.6 Ultrametric compression factor

**Inputs.** Fine balls $2^{30}=1.0737418\times10^{9}$, coarse balls $2^{10}=1.024\times10^{3}$ (modeling choices).

Compression factor:
$$
\kappa = \frac{2^{30}}{2^{10}} = 2^{20}=1.048576\times10^{6}\approx1.05\times10^{6}.
$$

### 4.7 Expected resolvable objects after compression

Assume $m=10^{5}$ objects placed uniformly at random into $2^{30}$ fine balls, which are then merged into $2^{10}$ coarse balls. The mean occupancy per coarse ball is
$$
\lambda = \frac{m}{2^{10}} = \frac{10^{5}}{1024}\approx97.66.
$$

For a Poisson model, the probability that a coarse ball contains exactly one object is
$$
p_{1}= \lambda e^{-\lambda}=97.66\,e^{-97.66}\approx3.78\times10^{-36}.
$$

Expected number of resolvable objects:
$$
m_{\text{real}} = 2^{10}\times p_{1}=1024\times3.78\times10^{-36}\approx3.87\times10^{-33}\approx0.
$$

The critical compression depth for survival of individuals is the coarsest level $r$ at which $b^{L-r}\gtrsim m$; for $m=10^{5}$ and $b=2$, $2^{L-r}\geq10^{5}$ requires $L-r\geq\lceil\log_{2}10^{5}\rceil=17$, so with $L=40$ the critical depth is $r_{\text{crit}}=40-17=23$.

### 4.8 Excess precision for unre‑enterable predicate

**Inputs.** High‑level predicate requires $n_{\mathrm{prec}}=100$ bits (assumption), distinction budget $N=64$.

$$
\Delta n = n_{\mathrm{prec}}-N = 100-64 = 36\;\text{bits}.
$$

Because a Boolean formula over $D_{64}$ can only refer to the $64$ base coordinates, any predicate depending on the discarded $36$ bits cannot be faithfully re‑entered.

### 4.9 Summary of quantitative findings

| Quantity | Symbol | Value | Source |
|----------|--------|-------|--------|
| Number of states for $N=64$ | $|S_{64}|$ | $2^{64}=1.8446744\times10^{19}$ | §4.1 |
| Number of admissible predicates | $2^{2^{64}}$ | $\approx10^{5.553\times10^{18}}$ | §4.1 |
| Reachable short predicates ($\le9$ literals) | $N_{\text{short}}$ | $1.5318446128384\times10^{12}$ | §4.2 |
| Fraction of reachable predicates | $f_{\text{reach}}$ | $\approx0$ | §4.2 |
| Landauer erasure energy per bit at $300\,$K | $E_{\text{bit}}$ | $2.8709\times10^{-21}\,$J | §4.3 |
| Erasure power for $10^{9}$ distinctions at $1\,$Hz | $P_{\text{erase}}$ | $2.8709\times10^{-12}\,$W | §4.4 |
| Maximum distinguishable bits for a $10^{-12}\,$W observer | $N_{\max}$ | $3.48\times10^{8}$ | §4.5 |
| Ultrametric compression factor (levels $10\to30$) | $\kappa$ | $1.05\times10^{6}$ | §4.6 |
| Expected resolvable objects after compression ($m=10^{5}$) | $m_{\text{real}}$ | $3.87\times10^{-33}\approx0$ | §4.7 |
| Critical compression depth for survival of $10^{5}$ objects | $r_{\text{crit}}$ | $\approx23$ | §4.7 |
| Excess precision for unre‑enterable predicate | $\Delta n$ | $36$ bits | §4.8 |
| TRL of this work | – | $2$ | Section 7(b) |

All numbers are derived directly from the arithmetic steps shown above; no external data are introduced.

## 5. Results

The analytical pipeline yields the following concrete outcomes:

1. **Combinatorial explosion of admissible predicates.** For a modest $N=64$ distinction budget the space of admissible existence predicates is $\approx10^{5.553\times10^{18}}$, yet only $N_{\text{short}}=1.5318446128384\times10^{12}$ of them are reachable (see Section 4.2) by conjunctions of at most $9$ literals. The reachable fraction is effectively zero.

2. **Thermodynamic floor for distinction maintenance.** Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.5).

3. **Compression‑induced ontology collapse.** An ultrametric tree with $L=40$ levels ($N=40$) compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. Under uniform spreading of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $3.78\times10^{-36}$, yielding an expected number of resolvable objects $3.9\times10^{-33}$, essentially zero. Survival of individuals requires compression no deeper than level $r_{\text{crit}}\approx23$, i