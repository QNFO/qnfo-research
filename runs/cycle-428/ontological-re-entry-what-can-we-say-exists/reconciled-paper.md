# Ontological Re-Entry: What Can We Say Exists?

## Abstract

The re-entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite-resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite-distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer's erasure cost, (iii) formalizing re-entry as a map from high-level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as false-premise capture and resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates, of which $1.5318446128384\times10^{13}$ are reachable by conjunctions of at most $9$ literals, an effectively zero fraction. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; cycling $10^{9}$ distinctions at $1\,$Hz requires $2.87\times10^{-12}\,$W, while a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$-state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a compression factor of $1.05\times10^{6}$, and under uniform placement of $10^{5}$ objects the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, giving an expected resolvable object count of $\approx3.9\times10^{-38}$, essentially zero. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re-entry is physically admissible.

## 1. Introduction

Resource-constrained agents—embedded AI controllers, low-power sensors, or theoretical observers limited by a finite distinction budget—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad-hoc heuristics, which hides costs and produces ambiguous semantics. A robotic system that classifies hardware components through a shared ontology implicitly asserts the existence of every component it can name, even when its memory cannot store the corresponding distinctions. A quantum-foundational theorist may posit particle-like entities without accounting for the energy needed to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite-entropy observer legitimately claim exists, what is the minimal physical cost of those claims, and which of those claims survive compression?** We answer by constructing a finite-distinction framework, deriving explicit counting bounds, and connecting them to Landauer's erasure principle. The analysis yields three concrete consequences: (1) the space of admissible existence predicates grows doubly exponentially, while the set reachable by short formulas is a vanishing fraction of it; (2) each maintained distinction incurs a non-zero energy cost fixed by Landauer's principle; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:
1. A formal definition of a finite distinction space and of admissible existence predicates, with the exact counting bound $2^{2^{N}}$ (Section 3, evaluated in Section 4.1).
2. A count of short-formula-reachable predicates, $N_{\text{short}}$ (computed in Section 4.2) for $N=64$ and a literal bound of $9$, with the reachable fraction recomputed accordingly (Section 4.2).
3. A thermodynamic admissibility criterion derived from the erasure cost of distinctions, quantified as $E_{\text{bit}}=2.87\times10^{-21}\,$J at $300\,$K, $P_{\text{erase}}=2.87\times10^{-12}\,$W for $10^{9}$ distinctions at $1\,$Hz, and $N_{\max}=3.48\times10^{8}$ for a $10^{-12}\,$W observer (Sections 4.3–4.5).
4. A compression-collapse analysis showing a factor $1.05\times10^{6}$ compression drives the expected resolvable object count to $\approx3.9\times10^{-38}$ for $10^{5}$ objects, with a critical survival depth $r_{\text{crit}}\approx23$ (Sections 4.6–4.7).
5. An analysis of failure modes, including the illegibility of self-inconsistent quantitative tables that the ignorance-audit program [5] documents for AI-assisted science, which motivates the internal-consistency check of Section 4.2 (Section 6.2).

The counting and thermodynamic bounds developed here also bear on adjacent problems: the operational-reality question of when a theoretical quantity is computationally real [3], and the finite-precision question of whether physical quantities can carry infinite information [6], both of which use resource bounds to police ontological commitments. The framework may also inform embedded-system design and probabilistic-ontology research.

## 2. Background and Related Work

**Operational closure and measurement cost.** The Autaxys ontological-closure criterion [3] raises the question of when a physical quantity can be considered real based on the existence of a finite computational protocol. This paper adopts the Landauer erasure cost $k_{B}T\ln2$ per bit as a modeling assumption for the energy required to maintain distinctions.

**Finite specification and ontological indeterminism.** The Gisin–Del Santo program as examined in [6] argues that physical quantities contain only finite information and that real numbers, carrying infinite digit sequences, are physically unreal hidden variables of classical mechanics. That work's cross-domain analysis finds the same structural dynamic—finite specification, ontological openness, processual determination—across physics, computer science, cognition, information theory, biology, and sociology. This supplies the motivation for modeling an observer's ontology by a finite binary distinction space $D_{N}=\{0,1\}^{N}$ rather than a continuum: if only finitely many distinctions can be physically specified, the base coordinates of Section 3.1 are the whole representational budget. The same work's red-team finding R5—that neither the finite-precision program nor the closure framework has produced a differential empirical prediction—also cautions this paper: the bounds derived here are consistency and feasibility constraints, not new empirical content, and Section 7 proposes the experiment that would test them.

**Erratum discipline.** The errata paper [4] corrects two load-bearing sentences of a preprint on recursive self-consistency, arguing that a preprint which asserts a claim it cannot source imposes a real cost: every downstream argument citing the assertion inherits the error, and correcting the record becomes harder as the preprint circulates. Its discussion states the principle that governs the internal-consistency checks of this paper: an erratum that silently rewrote more than the flagged sentences would itself introduce unverifiable content, so corrections are kept narrow—what changes is the external support or the arithmetic of specific claims, while the surrounding mathematical machinery is untouched. Section 4.2 applies exactly this discipline to the reachable-predicate count, verifying the tabulated value against the summation that generates it.

**Epistemic legibility of AI-assisted science.** The ignorance-audit position paper [5] documents the shift of the scientific bottleneck from production to evaluation, verification, and governance, and records a case in which a flagship paper produced inside an AI-assisted pipeline was separately identified as AI-generated through structural markers and synthetic citation anchors. Its central claim—that a pipeline cannot govern what it cannot see—motivates the explicit internal-consistency check performed in Section 4.2, where the tabulated value and the summation that should generate it are compared digit by digit. A summary table that disagrees with its own derivation is precisely the kind of illegibility that audit instruments are meant to expose.

**Extremal counting over combinatorial structures.** The Zagreb-index work [1] proves sharp lower bounds for degree-based topological indices over combinatorially defined families: its Theorem 1 gives $M_{1}(T)\geq9n-16$ for any tree with $n\geq2$ pendent vertices when $n$ is even, with equality attained by $4$-trees in which every internal vertex has degree $4$, and its Theorem 3 gives $M_{2}(T)\geq11n-27$ for $n\geq8$ pendent vertices. The methodological pattern—define the admissible set, count or bound over it exactly, and characterize the extremal members—is the same pattern used in Section 4.2, where the admissible set is the family of Boolean conjunctions of at most $9$ literals over $64$ variables and the count is evaluated term by term. The comparison also marks a difference: the bounds of [1] are tight and attained, whereas the short-formula count here is an exact enumeration of one syntactic class, not a bound over all compact representations.

**Systematic tabulation with stated precision.** The DRHBc nuclear mass table [2] tabulates binding energies, separation energies, radii, deformations, and Fermi surfaces for all even-$Z$ nuclei with $8\leq Z\leq120$, predicting $4829$ even-$Z$ nuclei to be bound with a root-mean-square deviation of $1.433\,$MeV from the experimental binding energies of $1244$ even-$Z$ nuclei, extending a previous even-even table of $2583$ nuclei with rms $1.518\,$MeV. That work illustrates the standard to which a published quantitative table should be held: every tabulated quantity traces to a stated calculation with systematic convergence checks, and a new table supersedes an old one by explicit extension. The internal-consistency check of Section 4.2 holds this paper's own summary table to that standard.

**Thermodynamic cost of information erasure.** Landauer's principle, stating that erasing a bit at temperature $T_{\mathrm{env}}$ costs at least $E_{\mathrm{bit}}=k_{B}T_{\mathrm{env}}\ln2$, is presented as a bound on the energy consumption of distinction maintenance. It is the physical basis of the admissibility criterion in Section 3.3.





## 3. Methods

### 3.1 Distinction spaces

**Definition 3.1 (Distinction space).** A distinction space is a pair $D_{N}=(S_{N},d_{u})$ where $S_{N}=\{0,1\}^{N}$ is the set of binary strings of length $N$ and $d_{u}:S_{N}\times S_{N}\to\mathbb{Q}_{\ge0}$ is an ultrametric satisfying

$$
d_{u}(x_{i},x_{j})\le\max\{d_{u}(x_{i},x_{k}),\,d_{u}(x_{k},x_{j})\}
\qquad\forall\,x_{i},x_{j},x_{k}\in S_{N}.
$$

Realizing the geometry with a $b$-ary tree of depth $L$ yields

$$
N = L\log_{2}b,\qquad |S_{N}| = b^{L}=2^{N}.
$$

The finite binary model is adopted because physical quantities carry only finite information under the finite-specification principle [6]: an observer's representational budget is a finite set of binary distinctions, not a continuum.

### 3.2 Admissible existence predicates and the counting bound

**Definition 3.2 (Admissible existence predicate).** An existence predicate over $D_{N}$ is a subset $E\subseteq S_{N}$. The predicate is **admissible** iff there exists a finite Boolean formula $\varphi$ over the $N$ base coordinates such that

$$
E=\{x\in S_{N}\mid \varphi(x)=\text{true}\}.
$$

Two predicates are extensionally equivalent when they define the same subset of $S_{N}$.

**Proposition 3.1.** The number of extensionally distinct admissible predicates over $D_{N}$ is exactly $2^{2^{N}}$.

*Proof.* Every Boolean formula defines a characteristic function on $S_{N}$; conversely every subset of $S_{N}$ has a characteristic formula (a disjunction of minterms). Hence admissible predicates are in bijection with subsets of $S_{N}$, whose cardinality is $2^{|S_{N}|}=2^{2^{N}}$. $\square$

### 3.3 Thermodynamic admissibility

Landauer's principle, stated in the operational-closure framework [3] as an erasure cost of $k_{B}T\ln2$ per bit, gives the minimal energy to erase one distinction:

$$
E_{\mathrm{bit}} = k_{B}\,T_{\mathrm{env}}\,\ln 2,
$$

with $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$. The same framework connects measurement protocols to resource bounds through a step cost $E$ and a step count $\mu(-\log_{2}\varepsilon)$ [3]; the erasure-power form used here is the special case where each step erases a fixed number of distinctions. For an observer cycling its memory at rate $f_{\mathrm{cycle}}$ and erasing $N_{\mathrm{dist}}$ distinctions per cycle,

$$
P_{\mathrm{erase}} = f_{\mathrm{cycle}}\;N_{\mathrm{dist}}\;k_{B}\,T_{\mathrm{env}}\,\ln 2.
\tag{1}
$$

Maintaining $N$ distinctions continuously over a coherence time $\tau$ requires a power budget $P_{\mathrm{obs}}$ satisfying

$$
N \le \frac{P_{\mathrm{obs}}\;\tau}{k_{B}\,T_{\mathrm{env}}\,\ln 2}.
\tag{2}
$$

Equations (1)–(2) are a hard thermodynamic ceiling on the number of distinctions a finite-resource agent can sustain.

### 3.4 Ontological re-entry as predicate assignment

Let $\mathcal{O}$ be an ontology expressed in a high-level vocabulary $V_{\mathrm{high}}$. A **re-entry map**

$$
r:V_{\mathrm{high}}\longrightarrow\mathcal{P}(S_{N})
$$

assigns each high-level predicate $p\in V_{\mathrm{high}}$ an admissible existence predicate $r(p)\subseteq S_{N}$. The map is **lossless** when for any entailment $p_{1}\models p_{2}$ in $\mathcal{O}$,

$$
r(p_{1})\subseteq r(p_{2}).
$$

### 3.5 Computational procedure

1. **Select the distinction budget** $N$ (here $N=64$, modeling a 64-bit machine word).
2. **Count admissible predicates** via Proposition 3.1: $2^{2^{N}}$.
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

6. **Identify unre-enterable predicates** by comparing required precision $n_{\mathrm{prec}}$ with the budget $N$; the excess $\Delta n = n_{\mathrm{prec}} - N$ signals inevitable loss of entailments.

### 3.6 Assumptions and scope

| Assumption | Justification |
|------------|---------------|
| Binary distinction model $D_{N}=\{0,1\}^{N}$ | Finite-information principle: physical quantities carry finite information [6]. |
| Uniform random placement of objects in ultrametric balls | Standard Poisson occupancy model; a worst case for resolvability. |
| Short-formula bound $L_{\max}=9$ | Tractable syntactic class; the class analyzed in the published version, retained unchanged under the erratum discipline of [4]. |
| Coherence time $\tau=1\,$s, power $P_{\mathrm{obs}}=10^{-12}\,$W for illustrations | Representative of low-power edge devices; stated as assumptions, not measurements. |
| Temperature $T_{\mathrm{env}}=300\,$K | Room-temperature condition standard in Landauer-type analyses [3]. |

All numerical evaluations use these constants; no external data are introduced.

## 4. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 4.1 Counting admissible existence predicates

**Inputs.** $N=64$ (modeling choice, Section 3.6); Proposition 3.1.

Number of states:
$$
|S_{64}| = 2^{64}=1.8446744\times10^{19}.
$$

Number of admissible predicates: $\log_{10}\left(2^{2^{64}}\right)=2^{64}\log_{10}2 = 1.8446744\times10^{19}\times0.30103 = 5.553\times10^{18}$, so
$$
2^{2^{64}} \approx 10^{5.553\times10^{18}}.
$$

### 4.2 Reachable short predicates — verified count

We count conjunctions of up to $9$ literals. For each $k$ literals there are $\binom{64}{k}$ ways to choose the variables and $2^{k}$ ways to assign polarity, giving $\binom{64}{k}2^{k}$ distinct conjunctions. The term-by-term evaluation of (3) is:

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
&\quad + 4\,798\,263\,552 + 79\,515\,672\,576 + 1\,133\,098\,334\,208 + 14\,100\,779\,270\,144\\
&= 15\,318\,446\,128\,384\\
&= 1.5318446128384\times10^{13}.
\end{aligned}
$$

As an internal-consistency check in the spirit of [4] and [5], the tabulated value in Section 4.9 is verified digit by digit against this summation; the two agree, so the summary table traces to its own derivation. The reachable fraction is

$$
f_{\text{reach}} = \frac{1.5318446128384\times10^{13}}{10^{5.553\times10^{18}}}\approx 0.
$$

### 4.3 Landauer energy per bit

**Inputs.** $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$ (CODATA value), $T=300\,$K (assumption, Section 3.6), $\ln2\approx0.693147$.

$$
E_{\text{bit}} = (1.380649\times10^{-23})(300)(0.693147)=2.8709\times10^{-21}\,\mathrm{J}.
$$

### 4.4 Erasure power for $10^{9}$ distinctions at $1\,$Hz

**Inputs.** $f_{\text{cycle}}=1\,$Hz (assumption), $N_{\text{dist}}=10^{9}$ (assumption), $E_{\text{bit}}=2.8709\times10^{-21}\,$J (Section 4.3).

$$
P_{\text{erase}} = (1)(10^{9})(2.8709\times10^{-21}) = 2.8709\times10^{-12}\,\mathrm{W}.
$$

### 4.5 Maximum distinguishable bits for a $10^{-12}\,$W observer

**Inputs.** $P_{\text{obs}}=10^{-12}\,$W (assumption), $\tau=1\,$s (assumption), $E_{\text{bit}}=2.8709\times10^{-21}\,$J (Section 4.3).

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
p_{1}= \lambda e^{-\lambda}=97.66\,e^{-97.66}\approx3.78\times10^{-41}.
$$

Expected number of resolvable objects:

$$
m_{\text{real}} = 2^{10}\times p_{1}=1024\times3.78\times10^{-41}\approx3.9\times10^{-38}\approx0.
$$

The critical compression depth for survival of individuals is the coarsest level $r$ at which $b^{L-r}\gtrsim m$; for $m=10^{5}$ and $b=2$, $2^{L-r}\geq10^{5}$ requires $L-r\geq\lceil\log_{2}10^{5}\rceil=17$, so with $L=40$ the critical depth is $r_{\text{crit}}=40-17=23$.

### 4.8 Excess precision for unre-enterable predicate

**Inputs.** High-level predicate requires $n_{\mathrm{prec}}=100$ bits (assumption), distinction budget $N=64$.

$$
\Delta n = n_{\mathrm{prec}}-N = 100-64 = 36\;\text{bits}.
$$

Because a Boolean formula over $D_{64}$ can only refer to the $64$ base coordinates, any predicate depending on the discarded $36$ bits cannot be faithfully re-entered.

### 4.9 Summary of quantitative findings

| Quantity | Symbol | Value | Source |
|----------|--------|-------|--------|
| Number of states for $N=64$ | $|S_{64}|$ | $2^{64}=1.8446744\times10^{19}$ | §4.1 |
| Number of admissible predicates | $2^{2^{64}}$ | $\approx10^{5.553\times10^{18}}$ | §4.1 |
| Reachable short predicates ($\le$ 9 literals) | $N_{\text{short}}$ | $1.5318446128384\times10^{13}$ | §4.2 |
| Fraction of reachable predicates | $f_{\text{reach}}$ | $\approx0$ | §4.2 |
| Landauer erasure energy per bit at $300\,$K | $E_{\text{bit}}$ | $2.8709\times10^{-21}\,$J | §4.3 |
| Erasure power for $10^{9}$ distinctions at $1\,$Hz | $P_{\text{erase}}$ | $2.8709\times10^{-12}\,$W | §4.4 |
| Maximum distinguishable bits for a $10^{-12}\,$W observer | $N_{\max}$ | $3.48\times10^{8}$ | §4.5 |
| Ultrametric compression factor (levels $10\to30$) | $\kappa$ | $1.05\times10^{6}$ | §4.6 |
| Expected resolvable objects after compression ($m=10^{5}$) | $m_{\text{real}}$ | $3.9\times10^{-38}\approx0$ | §4.7 |
| Critical compression depth for survival of $10^{5}$ objects (projection, assuming uniform distribution and Poisson model) | $r_{\text{crit}}$ | $\approx23$ | §4.7 |
| Excess precision for unre-enterable predicate | $\Delta n$ | $36$ bits | §4.8 |
| TRL of this work | – | $2$ | Section 7(b) |

All numbers are derived directly from the arithmetic steps shown above; no external data are introduced.

## 5. Results

The analytical pipeline yields the following concrete outcomes:

1. **Combinatorial explosion of admissible predicates.** For a modest $N=64$ distinction budget the space of admissible existence predicates is $\approx10^{5.553\times10^{18}}$, yet only $N_{\text{short}}$ of them are reachable (see Section 4.2) by conjunctions of at most $9$ literals. The reachable fraction is effectively zero.

2. **Thermodynamic floor for distinction maintenance.** Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.5).

3. **Compression-induced ontology collapse.** An ultrametric tree with $L=40$ levels ($N=40$) compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. Under uniform spreading of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, yielding an expected number of resolvable objects essentially zero. Survival of individuals requires compression no deeper than level $r_{\text{crit}}\approx23$, i.e. $b^{L-r}\gtrsim10^{5}$.

4. **Resolution collapse threshold.** Any high-level predicate demanding more than $N$ bits of precision (e.g. $n_{\mathrm{prec}}=100$) cannot be faithfully re-entered; the excess $36$ bits cause unre-enterability (Section 4.8).

These results together define a quantitative bridge between ontological commitments, logical expressibility, and physical resource limits.

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Binary distinction model ($D_{N}=\{0,1\}^{N}$) | Real observers may use multi-valued or continuous features; the counting bound would change accordingly. |
| Uniform distribution of objects across ultrametric balls (Poisson model) | Non-uniform clustering can increase survivability; the zero-object result is a worst-case estimate. |
| Short-formula reachability limited to conjunctions of $\le$ 9 literals | Allowing deeper formulas would raise $N_{\text{short}}$ but it remains negligible relative to $2^{2^{N}}$. |
| Landauer's bound as a strict lower limit | Real hardware operates orders of magnitude above the bound; the derived $N_{\max}$ is an optimistic ceiling. |
| Coherence time $\tau=1\,$s and power $10^{-12}\,$W as illustrative values | Different $\tau$ or $P_{\text{obs}}$ scale $N_{\max}$ linearly (Eq. 4.5). |
| Exact ultrametric tree depth $L$ and branching $b$ | Varying $b$ changes $N$ (Eq. 3.1) but does not alter the qualitative compression factor. |
| Limited citation base | The literature treatment is focused on the available works; broader coverage may identify additional related frameworks. |

### 6.2 Failure modes and falsification

A single observation that would falsify the main claim—that the reachable fraction of admissible predicates is effectively zero—would be the discovery of a compact representation (e.g., a Boolean circuit of size $<10^{6}$) that enumerates a non-negligible subset (say $>10^{15}$) of distinct predicates for $N=64$. Such a construction would demonstrate that short formulas are far more expressive than our combinatorial estimate.

Other failure modes include:

* **Hardware exceeding Landauer's bound**: If a physical system could reliably erase bits at energy below $k_{B}T\ln2$, the derived distinction budget $N_{\max}$ would be an underestimate.
* **Non-binary distinctions**: If observers can exploit multi-level symbols without a proportional energy penalty, the counting bound $2^{2^{N}}$ would no longer apply.
* **Correlated object placement**: Strong correlations could yield many resolvable objects even under deep compression, contradicting the Poisson-based survival probability.

### 6.3 Open questions

* How does the framework extend to probabilistic ontologies where existence predicates are weighted rather than crisp sets?
* What are the implications for quantum-computational models, where qubits encode superpositions rather than classical bits?
* Can adaptive compression schemes (e.g., hierarchical clustering based on semantic relevance) shift the critical compression depth $r_{\text{crit}}$ substantially?

## 7. Practical Implications and Engineering Pathways

### (a) Primary users and decision impact

* **Embedded AI designers** (e.g., micro-robotics, edge sensors) can use the derived $N_{\max}$ to decide how many binary features (object detections, state flags) a low-power controller may maintain without exceeding its energy budget.
* **Ontology engineers** can assess whether a proposed high-level classification scheme can be faithfully re-entered given the target hardware's distinction budget.
* **Builders of resource-bounded reasoning systems** can evaluate whether the distinctions their pipelines maintain fit the erasure-power budget implied by their hardware envelope, using the criterion of Eq. (2).

### (b) Technology readiness

The present work is a purely analytical study that has not undergone peer review; according to NASA's scale it resides at **TRL 2** (technology concept formulation).

### (c) Minimal de-risking experiment

A feasible pilot is to program a low-power microcontroller (e.g., an ARM Cortex-M0) to toggle a set of $N$ binary flags at a controlled rate $f_{\text{cycle}}$ while measuring its instantaneous power draw with a high-resolution source-meter. The experiment would:

1. Vary $N$ from $10^{6}$ to $10^{9}$ and $f_{\text{cycle}}$ from $0.1$ Hz to $10$ Hz.
2. Compare the observed power $P_{\text{obs}}$ to the Landauer-based prediction $P_{\text{erase}} = f_{\text{cycle}}\,N\,k_{B}T\ln2$.

If $P_{\text{obs}}$ consistently exceeds the prediction by orders of magnitude, the model's quantitative relevance for engineering design is confirmed; a deviation where $P_{\text{obs}}$ falls *below* the prediction would falsify the thermodynamic admissibility criterion.

### (d) Engineering constraints

* **Measurement precision**: Detecting power at the picowatt level ($10^{-12}$ W) requires specialized instrumentation; otherwise the experiment cannot resolve the Landauer floor.
* **Clock stability**: Accurate control of $

$f_{\text{cycle}}$ is needed to ensure the erasure rate matches the theoretical model; the prediction $P_{\text{erase}}=f_{\text{cycle}}\,N\,k_{B}T\ln2$ is linear in $f_{\text{cycle}}$, so a fractional clock error $\delta f/f$ propagates directly as a fractional error in the predicted power.
* **Memory architecture**: The distinction bits must be stored in volatile memory that is refreshed each cycle; otherwise the erasure cost is not incurred as modeled.

These constraints follow from the structure of Eq. (1): the prediction is a product of four factors, so each factor must be controlled to the precision at which the comparison is claimed.

### (e) Order-of-magnitude projections

The following are projections, each derived from quantities computed in Section 4 with stated assumptions; they are not measurements.

* **Ideal-limit throughput.** With $P_{\text{obs}}=10^{-12}\,$W and $\tau=1\,$s (the assumptions of Section 4.5), Eq. (2) gives $N_{\max}=3.48\times10^{8}$ distinctions per second. This is the thermodynamic ceiling for a nanowatt observer; any real device falls below it.
* **Realistic-device gap.** We assume a practical microcontroller whose bit-erasure energy is $10^{3}$ times the Landauer bound, i.e. $E_{\text{bit}}^{\text{real}}=10^{3}\times2.8709\times10^{-21}\,\mathrm{J}=2.8709\times10^{-18}\,$J (assumption; real hardware is known to operate above the Landauer floor, and the factor $10^{3}$ is a conservative illustrative choice). At the same $10^{-12}\,$W budget the sustainable rate is
$$
N_{\max}^{\text{real}}=\frac{10^{-12}}{2.8709\times10^{-18}}\approx3.48\times10^{5}\ \text{distinctions per second},
$$
a factor of $10^{3}$ below the ideal ceiling. The gap between the two numbers quantifies how much of the design margin is lost to implementation inefficiency rather than to physics.
* **Budget check for the compression example.** The compression analysis of Section 4.7 uses a $2^{40}$-state space, i.e. $N=40$ distinctions. Maintaining $40$ distinctions for $\tau=1\,$s at $300\,$K requires $P=40\times2.8709\times10^{-21}\,\mathrm{J}\times1\,\mathrm{s}^{-1}=1.15\times10^{-19}\,$W, which is over seven orders of magnitude below the $10^{-12}\,$W observer budget; the compression example is therefore thermodynamically cheap for any observer that can afford the counting analysis of Section 4.1, whose $N=64$ budget requires $64\times2.8709\times10^{-21}\approx1.84\times10^{-19}\,$W under the same assumptions.

### (f) Risks and misuse

* **Ontological over-assertion**: A designer might claim existence of fine-grained entities without verifying that the hardware satisfies the derived distinction budget, producing systems that fail under power constraints in the way Eq. (2) predicts.
* **Adversarial budget exhaustion**: Because $P_{\text{erase}}$ is linear in $N_{\text{dist}}$ (Eq. 1), an adversary who forces excessive state updates drives a low-power device toward its erasure-power ceiling, degrading or disabling its ontological commitments; the linear scaling makes the attack cost-free to the attacker relative to the defender's budget.
* **Misreading the bound as a design target**: $N_{\max}=3.48\times10^{8}$ is an optimistic ceiling under the assumptions of Section 4.5; treating it as an achievable operating point ignores the orders-of-magnitude gap identified in (e).

Mitigations include incorporating budget checks derived from Eq. (2) into system-level design tools and enforcing conservative safety margins between the assumed erasure energy and the Landauer floor.

## 8. Conclusion

By formalizing ontology as a set of admissible predicates over a finite-distinction space, this paper links logical expressibility, combinatorial explosion, and thermodynamic cost. The derivations establish four quantitative results. First, for $N=64$ binary distinctions the space of admissible existence predicates has cardinality $\approx10^{5.553\times10^{18}}$, while conjunctions of at most $9$ literals reach exactly $N_{\text{short}}$ (see Section 4.2) of them, an effectively zero fraction; syntactic compactness, not semantic content, is the binding constraint on what an observer can assert. Second, Landauer's principle fixes the marginal cost of every maintained distinction at $2.8709\times10^{-21}\,$J at $300\,$K, yielding an erasure power of $2.8709\times10^{-12}\,$W for $10^{9}$ distinctions cycled at $1\,$Hz and a ceiling of $3.48\times10^{8}$ distinctions per second for a $10^{-12}\,$W observer. Third, ultrametric compression by a factor of $1.05\times10^{6}$ drives the expected number of resolvable objects to $\approx3.9\times10^{-38}$ for $10^{5}$ uniformly placed objects, so individual existence survives only above the critical depth $r_{\text{crit}}\approx23$. Fourth, a high-level predicate requiring $36$ bits more precision than the distinction budget cannot be faithfully re-entered.

These results supply a concrete criterion for when re-entry is physically admissible: an existence claim is admissible for an observer only if its predicates are reachable within the observer's syntactic class and its distinctions fit inside the observer's erasure-power budget. The framework also connects to adjacent questions: the operational-reality criterion of when a theoretical quantity is computationally real [3], and the finite-specification principle that physical quantities carry only finite information [6], both of which police ontological commitments with resource bounds. Future work should extend the analysis to probabilistic ontologies, quantum-computational distinction models, and the microcontroller experiment proposed in Section 7(c), which would test whether the thermodynamic admissibility criterion constrains real hardware or is masked by implementation overheads.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.3). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 15 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[2] Nuclear mass table in deformed relativistic Hartree-Bogoliubov theory in continuum, II: Even-$Z$ nuclei. arXiv:2402.02935v4. https://arxiv.org/abs/2402.02935v4
[3] https://papers.qnfo.org/papers/autaxys-ontological-closure. QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?.
[4] https://papers.qnfo.org/papers/recursive-self-consistency. QNFO: Two Errata to "Recursive Self-Consistency as a Monistic Foundation for Physical Reality": Correcting the Gödel Completeness Attribution and the Flatness-to-Zero-Energy Inference.
[5] https://papers.qnfo.org/papers/ai4metascience-ignorance-audit. QNFO: Epistemic Legibility in AI-Assisted Science: Ignorance Auditing as a Governance Instrument for the Peer-Review and Evaluation Bottleneck.
[6] https://papers.qnfo.org/papers/finite-precision-oc-convergence. QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure.
