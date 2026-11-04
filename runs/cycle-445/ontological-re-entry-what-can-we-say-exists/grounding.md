# Grounding block - source: rem-rev-692850b7-8b7e-461d-8b7e-9530c1bc7f48

## Research idea

Re-entry from 10.5281/zenodo.19202950: ontological one (what can we say exists?

Post-publication revision of the published paper "Ontological Re‑Entry: What Can We Say Exists?" (version 2.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 10 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 10, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. The number of reachable short predicates is ≈1.53×10^12 (abstract, §4.7 table, Appendix B C3). (confirmed by a second model)
2. The probability that any coarse ball contains exactly one object is 3.78×10^-41, so expected resolvable objects is essentially zero (§5.3); Appendix B C8 says 3.78×10^-36. (confirmed by a second model)

## Existing paper under revision (remediation only)

# Ontological Re‑Entry: What Can We Say Exists?

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

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Results; Discussion; Practical Implications and Engineering Pathways; Conclusion; Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 10. length 3939 -> 3867 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix B. Claim attribution; Appendix B. Claim attribution. references 10 -> 9. length 3910 -> 3366 words.
- Version 2.2.0 (2026-10-20, from 2.1.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples; Appendix B. Claim attribution. references 9 -> 12. length 3445 -> 4616 words.
- Version 2.3.0 (2026-10-21, from 2.2.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Extended Derivations and Worked Examples. references 12 -> 9. length 4730 -> 4164 words.
- Version 3.0.0 (2026-11-03, from 2.3.0): rewritten in full through the research pipeline. references 9 -> 6. length 4164 -> 4638 words.

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


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1112.0343v1 | Ontological Queries: Rewriting and Optimization (Extended Version)
arXiv:2610.25360v1 | Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence
arXiv:2511.03563v1 | ASVRI-Legal: Fine-Tuning LLMs with Retrieval Augmented Generation for Enhanced Legal Regulation
arXiv:2610.25349v1 | Predicted Class Correction: Conformal Thresholds for Classes with No Calibration Data
arXiv:2104.13859v1 | Beables, Primitive Ontology and Beyond: How Theories Meet the World
arXiv:2310.18378v2 | Ontology Revision based on Pre-trained Language Models
arXiv:1604.05363v1 | Comparing Published Scientific Journal Articles to Their Pre-print Versions
arXiv:2204.06025v2 | Energy Complexity of Regular Languages

## QNFO corpus context (Vectorize)

QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real? | https://papers.qnfo.org/papers/autaxys-ontological-closure
QNFO: Ontological Re‑Entry: What Can We Say Exists? | https://papers.qnfo.org/papers/ontological-re-entry-what-can-we-say-exists
QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure | https://papers.qnfo.org/papers/finite-precision-oc-convergence
QNFO: Pillar 3: PBO/Autaxys — Pattern-Based Ontology as Intrinsic Self-Ordering | https://papers.qnfo.org/papers/pbo-autaxys

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1112.0343v1 | Ontological Queries: Rewriting and Optimization (Extended Version)
  Ontological queries are evaluated against an ontology rather than directly on a database. The evaluation and optimization of such queries is an intriguing new problem for database research. In this paper we discuss two important aspects of this problem: query rewriting and query optimization. Query rewriting consists of the compilation of an ontological query into an equivalent query against the u
  Full text (https://arxiv.org/html/1112.0343v1), excerpts of its own sections:
  § 1 Introduction: This paper is about ontological query processing, an important new challenge to database research. We will review existing methods and propose new algorithms for compiling an ontological query , that is, a query against an ontology on top of a relational database, into a direct query against this database, and we will deal with optimization issues related to this process so as to obtain possibly small and efficient compiled queries. In this section, we first discuss a number of relevant concepts, and then illustrate query rewriting and optimization processes in the context of a small but non-trivial example.
  § Ontologies.: The use of ontologies and ontological reasoning in companies, governmental organizations, and other enterprises has become widespread in recent years. An ontology is an explicit specification of a conceptualization of an area of interest  [ 2 ] , and consists of a formal representation of knowledge as a set of concepts within a domain, and the relationships between those concepts   [ 3 ] . To distinguish an enterprise ontology from a data dictionary, Dave McComb explicitly refers to the formal semantics of ontologies that enables automated processing and inferencing, while the interpretation of a data dictionary is strictly done by humans  [ 4 ] . Moreover, ontologies have been adopted as high-level conceptual descriptions of the data contained in data repositories that are sometimes distributed and heterogeneous in the data models. Due to their high expressive power, ontologies are also substituting more traditional conceptual models such as UML class-diagrams and E/R schemata.
  § Description Logics.: Description logics (DLs) are logical languages for expressing and modelling ontologies. The best known DLs are those underlying the OWL language 1 1 1 http://www.w3.org/TR/owl2-overview/ . The main ontological reasoning and query answering tasks in the complete OWL language, called OWL Full , are undecidable. For the most well-known decidable fragments of OWL, ontological reasoning and query answering is still computationally very hard, typically 2 exptime -complete. [...]
  § Ontology Based Data Access (OBDA).: We are currently witnessing the marriage of ontological reasoning and database technology. In fact, this amalgamation consists in the realization of the obvious idea that ABoxes shall be implemented in form of a relational database, or even stored in classical RDBMSs. [...]
  § 7 Implementation and Experimental Setting: TGD-rewrite (without the additional check described in Subsection  5.1 ) and the query elimination technique presented in Section  6 have been implemented in the prototype system Nyaya  [ 36 ] available at http://mais.dia.uniroma3.it/Nyaya . The reasoning and query answering engine is based on the IRIS Datalog engine 7 7 7 http://www.iris-reasoner.org/ . extended to support the FO-rewritable fragments of the Datalog ± family. In particular, we extended IRIS to natively support existential variables in the head without introducing function symbols and to support the constant $\mathit{false}$ as head of a rule (used to represent negative constraints). Both IRIS and our extension are implemented in Java. Since TGD-rewrite is designed for reasoning over ontologies with large ABoxes, we put ourselves in a similar experimental setting such that of  [ 19 ] . Thus, we use DL-Lite R ontologies with a varying number of axioms. The queries under consideration are based on canonical examples used in the research projects where these ontologies have been developed. [...]
[2] arXiv:2610.25360v1 | Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence
  World models are increasingly judged by how well they rank plausible futures, yet plausibility alone is the wrong target. The same scene can evolve under many latent rules, and a future that is smooth and physically valid under one rule can be incoherent under the rule actually in force. We formalize the resulting failure, operator-blindness, and show that it is systematically hidden by standard e
  Full text (https://arxiv.org/html/2610.25360v1), excerpts of its own sections:
  § 1 Introduction: A world model should anticipate futures, and we usually grade it by whether it ranks a true continuation above corrupted or random alternatives. This target— generic plausibility —is necessary but quietly insufficient. The same multi-object scene can evolve under many latent rules (gravity, damping, attraction, restitution), and a future that is perfectly plausible under one rule can be incoherent under the rule actually governing the present context. A world model must therefore answer not only “is this future plausible?” but “ under which world is it coherent? ” The distinction mirrors an asymmetry in human cognition. People reason about what is factually plausible, but they also imagine freely—recombining familiar elements into scenes that need not match the present world, yet remain internally consistent under different rules [ 1 , 2 , 24 , 25 ] . A capable world model arguably needs both faculties: the generativity to entertain plausible-elsewhere futures and the discernment to recognize which of them is coherent here. [...]
  § Contributions.: • A failure mode, formalized. We define operator-blindness and prove that generic top-1 ranking cannot detect it whenever the candidate set excludes wrong-operator futures (Section  3 , Prop.  1 ). • An objective and a protocol. OMC uses wrong-operator hard negatives; we pair it with operator-sensitive ranking, coherence stratification, and an operator $\times$ trajectory energy matrix, and prove that the wrong-operator negative is what drives the trained ordering (Section  4 , Prop.  2 ). • Evidence. On synthetic IID/OOD operator parameters, two backbones, and feature-level CoPhy ballsCF , OMC lifts operator-sensitive metrics well above a baseline that retains $\approx\!0.99$ generic top-1 (Sections  6 – 8 ). OMC is a coherence signal for trajectory scoring, not a generative architecture or planner; we substantiate exactly the relational claim above and delimit the rest in Section  9 . [...]
  § World models.: Latent-dynamics and Dreamer-style models learn dynamics and imagine rollouts for control [ 3 , 26 , 4 , 27 ] ; joint-embedding predictive architectures learn predictive representations and acquire intuitive physics from video [ 5 , 6 , 23 , 28 ] . These are representational/generative approaches; OMC is a complementary objective/evaluation signal that can sit atop such representations, and the latent-operator inference we use is standard rather than a contribution.
  § Explicit physical structure.: A parallel tradition encodes physics through physics-informed losses [ 7 ] or conservation-law architectures [ 8 , 9 ] . OMC neither imposes nor presupposes such structure; it asks the scorer to learn a relative coherence signal, and our results show that neither implicit nor explicit physics by itself yields operator-sensitive scoring.
  § 10 Conclusion: Plausibility is not coherence. A trajectory scorer can rank generic futures almost perfectly while remaining blind to which world is in force—a failure we formalized as operator-blindness and proved invisible to generic ranking. Operator-Mismatch Contrastive learning makes valid-but-wrong-operator trajectories the hard negatives, and we showed both theoretically and empirically—across synthetic IID/OOD, two backbones, and external CoPhy—that this single change to what counts as a negative exposes and repairs the failure.
[3] arXiv:2511.03563v1 | ASVRI-Legal: Fine-Tuning LLMs with Retrieval Augmented Generation for Enhanced Legal Regulation
  In this study, we explore the fine-tuning of Large Language Models (LLMs) to better support policymakers in their crucial work of understanding, analyzing, and crafting legal regulations. To equip the model with a deep understanding of legal texts, we curated a supervised dataset tailored to the specific needs of the legal domain. Additionally, we integrated the Retrieval-Augmented Generation (RAG
  Full text (https://ar5iv.labs.arxiv.org/html/2511.03563v1), excerpts of its own sections:
  § Submission history: From: One Octadion [ view email ] [v1] Wed, 5 Nov 2025 15:45:52 UTC (407 KB) Full-text links:
  § Access Paper:: View a PDF of the paper titled ASVRI-Legal: Fine-Tuning LLMs with Retrieval Augmented Generation for Enhanced Legal Regulation, by One Octadion and 3 other authors View PDF view license
  § Current browse context:: cs.CL < prev | next > new | recent | 2025-11 Change to browse by: cs
  § Bookmark: Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? [...]
[4] arXiv:2610.25349v1 | Predicted Class Correction: Conformal Thresholds for Classes with No Calibration Data
  Class-conditional conformal prediction calibrates a separate score threshold for every class and therefore requires labelled calibration examples of every class. In long-tailed deployments these are exactly what is missing: rare classes are left with few or no held-out examples, and existing methods are either undefined for them or fall back to the shared marginal threshold. We ask whether the per
  Full text (https://arxiv.org/html/2610.25349v1), excerpts of its own sections:
  § 1 Introduction: A prediction set replaces one fallible prediction with a short list that is likely to contain the true label. Conformal prediction turns any trained classifier into such a procedure, with a finite-sample coverage guarantee and no assumptions on the data distribution [ 45 , 39 , 2 ] . Figure 1 : A class with no calibration example still receives a threshold of its own. ImageNet class $754$ is held out, so $n_{y}=0$ : every classwise method either leaves it undefined or hands it the shared marginal threshold. Its descriptor $\varphi(y)$ is read from the classifier head, whose three nearest rows to it are other audio equipment, and the fitted regression turns that geometry into an offset. The threshold moves from $\hat{q}=0.9657$ to $0.9812$ and coverage of the class from $0.658$ to $0.750$ , against $0.803$ for an oracle given the test labels. [...]
  § Summary of findings.: We evaluate on ImageNet [ 37 ] , two long-tailed datasets [ 16 , 44 ] , three backbones, four score functions and $15$ corruption types [ 22 ] , for a total of $412$ configurations. (i) On ImageNet classes with zero calibration examples, PCC improves worst-class coverage by $0.058$ $[0.006,0.110]$ at matched average set size and is the only one of nine methods whose interval excludes zero; six of the eight baselines change the statistic by exactly zero ( Tab.   1 ). (ii) Few classes need to be labelled for this to work: holding out $90\%$ of classes, which leaves $100$ labelled classes out of $1000$ , still yields $0.052$ with a confidence interval excluding zero, and our protocol’s floor is $p+2$ labelled classes for $p$ descriptors ( Figure   2 b). (iii) Below roughly $35$ evaluation examples per class, an oracle that observes the test labels cannot improve worst-class coverage either, so what disappears there is the room to improve and not the ability to take it ( Figure   2 a). [...]
  § 4.3 The role of evaluation depth: Applied without modification, PCC fails on two long-tailed datasets and two additional backbones. All four lie on one axis, with a second cause beneath it for one, and finding the axis meant discarding two explanations we had held. Calibration depth is not the cause. Capping calibration examples inside ImageNet gives a dose-response from $0.033$ at ten per class to $0.060$ at one hundred, with every interval excluding zero ( Tab. S4 ), and ten per class is far thinner than the settings that fail. Descriptors endogenous to the scoring model are not the cause either: replacing each backbone’s own head with a fixed exogenous one leaves every interval containing zero ( Sec. J ). How much evaluation data each dataset actually has is Figure   2 a. On ImageNet every class carries about $1168$ examples; on Pl@ntNet-300K the median class has three and on iNaturalist-2018 two, so $83\%$ and $97\%$ of their classes respectively fall below the threshold at which we report a per-class estimate at all. Figure   2 b caps the number of evaluation examples per class inside ImageNet instead. [...]
  § 5 Discussion: A per-class conformal correction can be predicted from calibration-label-free descriptors and applied to classes with no calibration examples at all. On ImageNet it takes $42\%$ of an oracle ceiling there and is the only one of nine methods whose improvement is distinguishable from none, two of the eight baselines being undefined for all such classes, and it needs labels for as few as a tenth of the classes. Marginal coverage is preserved because a single scalar is calibrated ( Proposition   2 ).
[5] arXiv:2104.13859v1 | Beables, Primitive Ontology and Beyond: How Theories Meet the World
  Bohm and Bell's approaches to the foundations of quantum mechanics share notable features with the contemporary Primitive Ontology perspective and Esfeld and Deckert minimalist ontology. For instance, all these programs consider ontological clarity a necessary condition to be met by every theoretical framework, promote scientific realism also in the quantum domain and strengthen the explanatory po
  Full text (https://arxiv.org/html/2104.13859v1), excerpts of its own sections:
  § 1 Introduction: Quantum Mechanics (QM) is one of the most efficient descriptions of the inherent structure of matter and its behavior. As is known, however, this theory represents elementary objects in a way that drastically changed our conception of reality, speaking about intrinsically indeterminate systems, non-local interactions, wave-particle dualities, etc. . Indeed, it is still a pivotal philosophical challenge to understand what scientific image of the world it provides—i.e. to comprehend its ontology, and how the macroscopic realm can be explained from it. Referring to this, it is worth noting that quantum theory is affected by several conceptual and technical conundra; hence, we cannot consider it the final word about ontological matters, notwithstanding its empirical success. In particular, scholars agree that QM contains physically ill-defined notions within its axioms, and inconsistencies among its dynamical laws—resulting in the (in)famous quantum measurement problem. Against this background, the Primitive Ontology (PO) approach has been advanced to overcome these issues. [...]
  § 2 David Bohm, Pluralism and Infinitism: Ontological clarity is an essential feature of physical theories according to Bohm. On his view the problems of the standard interpretation of QM come from its obscure metaphysical content. Bohm was deeply unsatisfied by the lack of explanation of measurement results, since quantum theory excludes a precise characterization of individual systems as well as an accurate description of their dynamical evolution “without proving that such a renunciation is necessary” ( Bohm, (1952) :168). Furthermore, he argued that the empirical robustness of QM and its contingent mathematical structure are not sufficient to exclude a priori other ontologically clearer formulations. To tame these issues, Bohm joined the foundational debate proposing an alternative interpretation of QM where quantum particles have definite positions and velocities, and are dynamically guided by a real $\psi$ -field, challenging the metaphysical indeterminacy of the standard formulation. [...]
  § 3 Local and Non-local Beables: It is well-known that Bell was disappointed by the lack of ontological clarity in QM, which in his opinion was the source of its inconsistency and redundancy. Inconsistency because the dynamical laws of the theory contradict each other 4 4 4 These laws are the Schrödinger equation and the collapse postulate. ; redundancy because some central notions contained in its axioms, e.g. [...]
  § 6 Conclusion: Starting from Bohm’s infinitism and Bell’s theory of local beables, we arrived to the PO programme and its most recent development, i.e. Esfeld and Deckert’s minimalist ontology. Although the initial steps of this journey are in open contradiction w.r.t. the latest works proposed within the PO community, there is still some confusion in literature, where it is not uncommon to conflate Bell’s methodological approach with the PO programme, and the latter with Esfeld and Deckert’s views. Thus, in this essay I underlined the main differences among these projects. In particular, we saw that Bell’s methodological approach shows important similarities with Bohm’s ideas, sharing the belief about the provisional character of physical theories and a pluralist attitude towards their ontology. Then the PO programme has been presented emphasizing some important differences w.r.t. Bell’s and Bohm’s views. Elaborating on Allori’s works, I have pointed out new divergences between these two schools of thought. [...]
[6] arXiv:2310.18378v2 | Ontology Revision based on Pre-trained Language Models
  Ontology revision aims to seamlessly incorporate a new ontology into an existing ontology and plays a crucial role in tasks such as ontology evolution, ontology maintenance, and ontology alignment. Similar to repair single ontologies, resolving logical incoherence in the task of ontology revision is also important and meaningful, because incoherence is a main potential factor to cause inconsistenc
  Full text (https://arxiv.org/html/2310.18378v2), excerpts of its own sections:
  § 5 Experiments: In this section, we first introduce the data set and experimental settings, and then provide experimental results. It should be noted that all algorithms were implemented with OWL API 3 3 3 http://owlcs.github.io/owlapi/ in Java. The functionality of computing vectors for sentences was implemented in Python, and the pre-trained model BERT was applied to calculate vectors (see the introduction in Section 2 ). To perform standard reasoning tasks, the widely used DL reasoner Pellet [ 34 ] was selected. In addition, according to our experience, the parameter $k$ in the definition of sim euc (see Definition 10 ) was set to be $15$ for our experiments, and the threshold $t$ in the definition of similarity between an axiom set and an axiom (see Definition 15 ) was assigned to be $0.5$ . All implementations together with our data set and experimental results are available online 4 4 4 https://github.com/QiuJi345/ontRevision .
  § 5.2 Experimental Settings: All experiments were performed on a laptop with 1.99 GHz Intel ® Core TM CPU and 16GB RAM, using a 64-bit Windows 11 operating system. A time limit of 1,000 seconds is set to compute R-MUPS for an unsatisfiable concept or compute a diagnosis. A black-box algorithm implemented in [ 9 ] was exploited to compute R-MUPS or R-MIPS. We evaluate our two revision algorithms by using different subset extraction strategies configured in the following ways. • mipsUnion_cos / mipsUnion_euc : The two extraction strategies indicate ranking axioms by the scoring function $score_{mipsUnion}$ (see Definition 16 ) with similarity measures ${sim}_{cos}$ and ${sim}_{euc}$ (see Definition 9 and Definition 10 ) separately, and then selecting axioms with the highest score from each R-MIPS. • mips_cos / mips_euc : The two extraction strategies represent ranking axioms by the scoring function $score_{mips}$ (see Definition 17 ) with similarity measures ${sim}_{cos}$ and ${sim}_{euc}$ separately, and then selecting axioms with the highest score from each R-MIPS. [...]
  § 5.3 Experimental Results: In this section, we first present the results about the preparation about computing vectors, R-MUPS and R-MIPS. We then describe the results about revision based on all R-MIPS and local R-MIPS. Finally, a brief discussion of all experimental results is provided.
  § 5.3.1 Results about preparation: Before revising a rebuttal ontology by applying one of our semantics-based scoring function, the vectors of all axioms in an ontology needs to be calculated first. This process can be done offline. Table 3 provides the time to compute vectors for a single ontology. From the table, we can obviously observe that the efficiency of computing vectors mainly relies on the number of axioms. Each km ontology contains 1000 axioms, and thus they spent similar time (i.e., about 6 seconds). For ontologies O2 and O4, they also contain around 1000 axioms and took similar time to finish the computation of vectors. As for the ontologies obtained by translating ontology alignments, they usually include no more than 50 axioms and each of them took no more than 0.5 seconds.
  § 5.3.2 Results about computing all R-MIPS: In this section, we present the results about all R-MIPS in a rebuttal ontology with respect to its corresponding reliable ontology together with R-MUPS information, since all R-MIPS are obtained based on all R-MUPS of all unsatisfiable concepts. Table 4 gives the details about the results of R-MUPS and R-MIPS. The 2nd column displays the average number of R-MUPS per unsatisfiable concept. [...]
[7] arXiv:1604.05363v1 | Comparing Published Scientific Journal Articles to Their Pre-print Versions
  Academic publishers claim that they add value to scholarly communications by coordinating reviews and contributing and enhancing text during publication. These contributions come at a considerable cost: U.S. academic libraries paid $1.7 billion for serial subscriptions in 2008 alone. Library budgets, in contrast, are flat and not able to keep pace with serial price inflation. We have investigated 
  Full text (https://arxiv.org/html/1604.05363v1), excerpts of its own sections:
  § 1 Introduction: Academic publishers of all types claim that they add value to scholarly communications by coordinating reviews and contributing and enhancing text during publication. These contributions come at a considerable cost: U.S. academic libraries paid $\$1.7$ billion for serial subscriptions in $2008$ alone and this number continues to rise. Library budgets, in contrast, are flat and not able to keep pace with serial price inflation. Several institutions have therefore discontinued or significantly scaled back their subscription agreements with commercial publishers such as Elsevier and Wiley-Blackwell. [...]
  § 5 Experiment Results: We calculated the similarity metrics described above for each pair of corresponding pre-print and final published papers in our data set, comparing titles, abstracts, and body sections when available. From the results of these calculations, we generated visualizations of the similarity distributions for each metric. Subsequent examinations and analyses of these distributions provided novel insights into the question of how and to what degree the text contents of scientific papers may change from their pre-print instantiations to the final published version. Because each section of a publication differs in its purpose and characteristics (e.g., length, standard formatting) and each metric addresses the notion of similarity from a different perspective, we present the results of our comparisons per section (title, abstract, and body), subdivided by comparison metric. Figure 3 : Comparison results for abstracts
  § 7 Discussion and Future Work: The results outlined in this paper are from a preliminary study on the similarity of pre-print articles to their final published counterparts. There are many areas where this study could be improved and enhanced. One limitation to this work is the focus on arXiv.org as the sole corpus of pre-print articles. As a result, all of the articles are from a relatively limited slice of the STM domain — specifically, physics, mathematics, statistics, and computer science, as shown in Figure 1 . Expanding this line of experiments to other domains such as the biological sciences, humanities, social sciences, and economics might return different results, as the review and editorial practices in other disciplines can vary considerably. As part of our future work, we are planning to conduct this experiment again with articles from the RePEc.org corpus (economics) and from bioRxiv.org (biology), for example. The matching of a pre-print version of an article to its final published version was done by means of the article’s DOI. [...]
  § 8 Conclusions: This study is motivated by academic publishers’ claims of the value they add to scholarly articles by copyediting and making further enhancements to the text. We present results from our preliminary study to investigate the textual similarity of scholarly pre-prints and their final published counterparts. We apply five different similarity measures to individual extracted sections from the articles’ full text contents and analyze their results. We have shown that, within the boundaries of our corpus, there are no significant differences in aggregate between pre-prints and their corresponding final published versions. In addition, the vast majority of pre-prints ( $90\%$ - $95\%$ ) are published by the open access pre-print service first and later by a commercial publisher. [...]
[8] arXiv:2204.06025v2 | Energy Complexity of Regular Languages
  Each step that results in a bit of information being ``forgotten'' by a computing device has an intrinsic energy cost. Although any Turing machine can be rewritten to be thermodynamically reversible without changing the recognized language, finite automata that are restricted to scan their input once in ``real-time'' fashion can only recognize the members of a proper subset of the class of regular
  Full text (https://arxiv.org/html/2204.06025v2), excerpts of its own sections:
  § 1 Introduction: The discovery of the relationship between thermodynamics and computation, revealing the links between the concepts of heat, entropy, and information, is a landmark scientific achievement [ 12 ] . As shown by Landauer [ 10 ] , each bit of information “forgotten” by a computing device is associated with the dissipation of an amount of heat proportional to the absolute temperature of the device, and thus an unavoidable minimum energy cost for any fixed temperature. Turing machine programs [ 2 ] (and even finite automata with two-way access to their input strings [ 8 ] ) can be rewritten to be reversible , so that each one of their configurations has a single possible predecessor, and their computational steps can therefore in principle be executed using arbitrarily small amounts of energy, but things change when one limits attention to real-time finite automata. [...]
  § 2 Information erasure by finite automata and the general QFA model: It is important to start by clarifying the nature of the resource whose usage is studied in this paper. A computing device is said to “forget” $\log_{2}P$ bits of information when it arrives at a configuration which has $P$ predecessors, this increases the entropy by $k_{B}\ln{2}\log_{2}P$ joules per kelvin (where $k_{B}$ is Boltzmann’s constant), and the amount of dissipated heat can be calculated by multiplying this entropy difference by the ambient temperature $T$ [ 10 ] . It is evident that the energy cost under consideration is directly proportional to the number of forgotten bits. We will therefore define the energy complexity of a finite automaton as the maximum number of bits of information that it forgets while running on any input string of a given length. Although we considered the name ‘‘entropy complexity’’, we decided that ‘‘energy’’ is a much more natural concept to associate with the notion of a ‘‘‘resource’’, when compared to entropy. [...]
  § 3 Zero-error QFAs have no energy advantage: For any language $L$ defined over alphabet $\Sigma$ , the “indistinguishability” relation $\equiv_{L}$ on the set $\Sigma^{*}$ is defined as follows: $(x\equiv_{L}y)\iff(\forall z\in\Sigma^{*}[xz\in L\iff yz\in L]).$ Lemma 1 . Let $M$ be a QFA recognizing a language $L$ with zero error. Let $x$ and $y$ be strings such that $x\not\equiv_{L}y$ . If $\ket{\psi_{x}},\ket{\psi_{y}}\in\mathcal{H}_{n}$ are any two vectors that are attained by $M$ with nonzero probability after it reads $x$ or $y$ , respectively, then $\innerproduct{\psi_{x}}{\psi_{y}}=0$ . Proof. [...]
  § 7 Concluding remarks: The approach we present for the study of energy complexity can be extended to several other scenarios, like interactive proof systems, involving finite-memory machines. We end with a list of our plans for future research, and open questions. • As we noted, the general QFA model is not flexible enough to study the energy costs of computational steps which forget less information than the maximum amount allowed by the number of operation elements. The formulation of a new model that is able to explicitly represent distinctions between the “cheap” and “costly” steps of a quantum finite automaton would be helpful in answering further energy complexity questions about those machines. • Are there languages whose bounded-error recognition by QFAs have lower energy complexity than their zero-error recognition? Would the results of Theorems 5 , 6 and 7 about maximum step costs be helpful in answering this question?
[9] QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real? | https://papers.qnfo.org/papers/autaxys-ontological-closure
  We propose an operational criterion for physical reality: a quantity is physically real only if there exists a finite Turing-machine protocol that approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions. This criterion is not a metaphysical claim about what "exists" — it is a boundary condition on measurability: if no finite computation can conver
  Full text (https://papers.qnfo.org/papers/autaxys-ontological-closure), excerpts of its own sections:
  § 1 Introduction: What does it mean for a physical quantity to be "real"? The question has divided physicists and philosophers for centuries. The realist position holds that quantities appearing in successful theories refer to entities that exist independently of measurement. The instrumentalist position holds that theories are computational devices for predicting measurement outcomes, and questions about "reality" are ill-posed. The operationalist position, associated with Bridgman [1], holds that the meaning of a quantity is exhausted by the operations used to measure it. We propose a refinement of operationalism that leverages the theory of computation. The central insight is that measurement is a form of computation: a finite physical protocol that takes a system as input and produces a numerical output. If no finite protocol — not even in principle, with unlimited resources — can converge to a quantity's value, then that quantity cannot be measured. And if a quantity cannot be measured even in principle, it is operationally indistinguishable from a quantity that does not exist. [...]
  § 1.1 Historical Context: The relationship between computation and physical reality has been explored from multiple directions. Landauer's principle [2] established that information is physical — erasing a bit costs $k_B T \ln 2$ in thermodynamic entropy; in dimensionless Planck units ($\hbar = c = G = k_B = 1$): $T \ln 2$, where both the energy and temperature are pure numbers — Archimedean norms of quantities whose completions exist at every place per Ostrowski's theorem. Wheeler's "it from bit" program [3] proposed that physical reality is intrinsically informational. [...]
  § 7.1 Theory Evaluation: A physical theory that predicts uncomputable quantities is operationally vacuous — it makes predictions that cannot be verified. The OC criterion provides a sharp filter: if a theory's observable predictions are not computably approximable, the theory is not testable. This applies particularly to multiverse theories that predict probability distributions over an uncomputable "measure" [11], and to certain approaches to quantum gravity that produce continuous spectra without computable eigenvalue approximations.
  § 7.2 Experimental Design: The modulus-of-convergence requirement translates directly into experimental resource estimates. If measuring quantity $Q$ to precision $\varepsilon$ requires $\mu(-\log_2 \varepsilon)$ steps, and each step costs $E$ joules, then the total energy cost is $E \cdot \mu(n)$. This connects the computational criterion to thermodynamic resource bounds — a connection that OC-9 (Landauer) makes explicit.
  § 9 Conclusion: The Autaxys Ontological Closure criterion proposes a precise boundary for physical reality: a quantity is physically real if and only if it is computably approximable with a computable modulus of convergence, yielding measurement-distinguishable predictions. The criterion is neither radical nor novel. It formalizes what physicists already do: restrict attention to quantities they can measure. The contribution is making this restriction explicit and connecting it to the mathematical theory of computation, where the boundary between computable and uncomputable has been precisely characterized since Turing (1936). The criterion's value is threefold. First, it provides a sharp filter for theory evaluation: if a theory's predictions are uncomputable, the theory is untestable. Second, it connects measurement protocols to computational resource bounds, making the thermodynamic cost of measurement explicit. [...]
[10] QNFO: Ontological Re‑Entry: What Can We Say Exists? | https://papers.qnfo.org/papers/ontological-re-entry-what-can-we-say-exists
  The re-entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite-resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite-distinction space $D_{N}$ and counting its admissible existence predicates, (ii) derivin
  Full text (https://papers.qnfo.org/papers/ontological-re-entry-what-can-we-say-exists), excerpts of its own sections:
  § 4.9 Summary of quantitative findings: | Quantity | Symbol | Value | Source | |----------|--------|-------|--------| | Number of states for $N=64$ | $|S_{64}|$ | $2^{64}=1.8446744\times10^{19}$ | §4.1 | | Number of admissible predicates | $2^{2^{64}}$ | $\approx10^{5.553\times10^{18}}$ | §4.1 | | Reachable short predicates ($\le$ 9 literals) | $N_{\text{short}}$ | $1.5318446128384\times10^{13}$ | §4.2 | | Fraction of reachable predicates | $f_{\text{reach}}$ | $\approx0$ | §4.2 | | Landauer erasure energy per bit at $300\,$K | $E_{\text{bit}}$ | $2.8709\times10^{-21}\,$J | §4.3 | | Erasure power for $10^{9}$ distinctions at $1\,$Hz | $P_{\text{erase}}$ | $2.8709\times10^{-12}\,$W | §4.4 | | Maximum distinguishable bits for a $10^{-12}\,$W observer | $N_{\max}$ | $3.48\times10^{8}$ | §4.5 | | Ultrametric compression factor (levels $10\to30$) | $\kappa$ | $1.05\times10^{6}$ | §4.6 | | Expected resolvable objects after compression ($m=10^{5}$) | $m_{\text{real}}$ | $3.9\times10^{-38}\approx0$ | §4.7 | | Critical compression depth for survival of $10^{5}$ objects (projection, assuming uniform distribution and Poisson model) [...]
  § 5. Results: The analytical pipeline yields the following concrete outcomes: 1. **Combinatorial explosion of admissible predicates.** For a modest $N=64$ distinction budget the space of admissible existence predicates is $\approx10^{5.553\times10^{18}}$, yet only $N_{\text{short}}$ of them are reachable (see Section 4.2) by conjunctions of at most $9$ literals. The reachable fraction is effectively zero. 2. **Thermodynamic floor for distinction maintenance.** Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.5). 3. **Compression-induced ontology collapse.** An ultrametric tree with $L=40$ levels ($N=40$) compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. [...]
  § (c) Minimal de-risking experiment: A feasible pilot is to program a low-power microcontroller (e.g., an ARM Cortex-M0) to toggle a set of $N$ binary flags at a controlled rate $f_{\text{cycle}}$ while measuring its instantaneous power draw with a high-resolution source-meter. The experiment would: 1. Vary $N$ from $10^{6}$ to $10^{9}$ and $f_{\text{cycle}}$ from $0.1$ Hz to $10$ Hz. 2. Compare the observed power $P_{\text{obs}}$ to the Landauer-based prediction $P_{\text{erase}} = f_{\text{cycle}}\,N\,k_{B}T\ln2$. If $P_{\text{obs}}$ consistently exceeds the prediction by orders of magnitude, the model's quantitative relevance for engineering design is confirmed; a deviation where $P_{\text{obs}}$ falls *below* the prediction would falsify the thermodynamic admissibility criterion.
  § 8. Conclusion: By formalizing ontology as a set of admissible predicates over a finite-distinction space, this paper links logical expressibility, combinatorial explosion, and thermodynamic cost. The derivations establish four quantitative results. First, for $N=64$ binary distinctions the space of admissible existence predicates has cardinality $\approx10^{5.553\times10^{18}}$, while conjunctions of at most $9$ literals reach exactly $N_{\text{short}}$ (see Section 4.2) of them, an effectively zero fraction; syntactic compactness, not semantic content, is the binding constraint on what an observer can assert. [...]
[11] QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure | https://papers.qnfo.org/papers/finite-precision-oc-convergence
  We examine the Gisin--Del Santo program on finite-precision physics and its convergence with the Autaxys Ontological Closure (OC) framework. The Gisin--Del Santo program argues that (1) physical quantities contain only finite information, (2) real numbers are physically unreal --- they are *de facto* hidden variables of classical mechanics, (3) consequently, classical mechanics is ontologically in
  Full text (https://papers.qnfo.org/papers/finite-precision-oc-convergence), excerpts of its own sections:
  § 1. Introduction: For centuries, the intimate symbiosis between mathematics and physics has driven scientific progress. But this relationship carries an implicit risk: mathematical structures developed independently of physics may, when applied to physical theories, introduce ontological commitments that nature does not honor. The real number system is the most consequential example. Formalized in the late nineteenth century by Dedekind, Cantor, and Weierstrass, the real numbers provide mathematics with a seamless continuum of infinite precision --- every real number contains an infinite sequence of digits, each fully determined. This formalism was adopted wholesale by physics, where physical quantities such as position, momentum, and energy are routinely modeled as real numbers. In recent years, a growing body of work has challenged this assumption. [...]
  § 5. Cross-Domain Consilience: The finite-information principle is not confined to physics. A structured cross-domain analysis (full details in `artifacts/consilience-gate.md`) reveals that the same structural dynamic --- finite specification $\rightarrow$ ontological openness $\rightarrow$ processual determination --- appears across six disciplines: | Domain | Finite Specification | Indeterminism Mechanism | Time Character | |:-------|:---------------------|:------------------------|:---------------| | **Physics** | Bekenstein bound, FIQ | Chaotic amplification of unspecified digits | Creative time | | **Computer Science** | Fixed-point arithmetic, program termination | Lazy evaluation, non-deterministic choice | Sequential execution | | **Cognitive Science** | Just-noticeable-difference, bounded rationality | Perceptual filling-in, change blindness | Subjective Now | | **Information Theory** | Channel capacity, rate-distortion | Equivocation, quantization noise | Sequential decoding | | **Biology** | Genetic specification, canalization depth | Developmental noise, phenotypic plasticity | Developmental time | | [...]
  § 6. Critical Caveats and Red-Team Findings: A formal red-team audit (`artifacts/red-team-audit.md`) applied the five-adversary challenge protocol (null-hypothesis defender, methodology skeptic, better-alternative proposer, scaling pessimist, resource realist). Five findings emerged:
  § R5: No Experimental Predictions [5/5] [HIGH]: **Finding:** This is the strongest form of R1. Neither the Gisin--Del Santo program nor the OC framework has produced a *differential empirical prediction* --- something that would be observed if the framework is correct but not if standard physics is correct. **Response:** Same as R1. We position this paper as foundations/philosophy of physics. The value proposition is theoretical unification and consilience across domains, not novel empirical content. We explicitly invite experimental proposals. ---
  § 7. Conclusion and Open Questions: The Gisin--Del Santo program and the Autaxys OC framework converge on the principle that physical quantities contain only finite information, and that recognizing this principle yields ontological indeterminism, a processual conception of time, and a reinterpretation of quantum mechanics as classical indeterminism plus incompatible observables. The cross-domain consilience analysis shows this principle is a structural invariant across physics, computation, cognition, information theory, biology, and sociology.
[12] QNFO: Pillar 3: PBO/Autaxys — Pattern-Based Ontology as Intrinsic Self-Ordering | https://papers.qnfo.org/papers/pbo-autaxys
  PBO/Autaxys (Pattern-Based Ontology) is presented as an intrinsic self-ordering meta-framework grounded in two primitive operations: Distinction (D) and Relation (R). From these D/R primitives, all patterns, structures, and physical laws are shown to emerge without recourse to external agents or pre-imposed rules. We formalize Ontological Closure Verification (OCV) as the criterion for self-contai
  Full text (https://papers.qnfo.org/papers/pbo-autaxys), excerpts of its own sections:
  § Pillar 3: PBO/Autaxys — Pattern-Based Ontology as Intrinsic Self-Ordering: *QNFO Unified License Agreement (QNFO-ULA)*
  § 1. Introduction: Autaxys as Generative Meta-Framework: The central problem of fundamental ontology is the origin of order. Why is there structured reality rather than undifferentiated chaos? [...]
  § 4.2 Results: Zero Matches: The synthesis identified **zero papers** that employ D/R as dual co-primitives in the specific sense required by PBO/Autaxys. The closest approximants were: | Domain | Nearest Approach | Gap | |--------|-----------------|-----| | Spencer-Brown (1969) | Distinction as primitive | Does not develop D/R as co-primitive algebra; lacks Relation as independent generator | | Baez & Stay (2011) | Categorical physics with morphisms as processes | Morphisms derived from categories, not from D/R primitives; categories assume pre-existing objects | | Wolfram (2020) | Hypergraph rewriting | Rules are externally specified, not intrinsic to the rewriting act itself | | Vidotto (2022) | Relational quantum mechanics | Relations supervene on pre-existing quantum states; not co-primitive | | Arsiwalla & Gorard (2020) | DPO hypergraph rewriting | Nodes and edges assumed a priori; no derivation from distinction | Each of these approaches either (a) assumes more primitives than D/R, (b) derives relations from pre-existing objects rather than positing them as co-primitive, or (c) imports external rules or [...]
  § 4.3 Significance of the Negative Result: The zero-match result across 480 papers is a **strong negative finding** — it does not prove uniqueness (one cannot prove a negative across all possible literature), but it does shift the burden of proof. If PBO/Autaxys were merely a re-description of existing work, the core vocabulary should appear in at least some of the 480 surveyed papers. Its absence suggests that the D/R+OC combination genuinely constitutes a novel ontological framework. We note two caveats. First, the search was limited to English-language academic and technical literature; non-English traditions (particularly in process philosophy) may contain cognate concepts. Second, the corpus was constructed from publicly available sources and may under-represent proprietary or classified research. Nevertheless, the synthesis provides reasonable confidence that PBO/Autaxys is not a duplication of existing scholarly work. ---
  § 8. Conclusion: We have presented PBO/Autaxys — Pattern-Based Ontology as an intrinsic self-ordering framework — grounded in two primitive operations: Distinction and Relation. From these D/R primitives, the five operational dynamics of the Autaxys generative engine emerge as compound D/R patterns. The framework satisfies Ontological Closure Verification: it generates all structures it describes from its own primitives without external reliance. A systematic literature synthesis across 480 papers in foundational physics, computational ontology, information theory, and adjacent fields found zero matches for the core D/R+OC vocabulary, substantiating the uniqueness claim of the framework. Three falsifiable empirical predictions — Dissonance-Induced Bifurcation, OCV Saturation Threshold, and Token Calculus Cascade Bound — provide concrete experimental pathways for verification or falsification. The PBO Token Calculus bridges the continuous D/R algebra to the discrete tokens of observable reality, providing a formal grammar for pattern generation and a topological origin for mass parameters. [...]