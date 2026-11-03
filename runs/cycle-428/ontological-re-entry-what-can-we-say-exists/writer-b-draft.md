# Ontological Re-Entry: What Can We Say Exists? (Corrected Version, v2.3.1)

## Abstract

The re-entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite-resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits, and the previously published version of this framework carried an internal inconsistency: its summary table and claim register listed $1.53\times10^{12}$ reachable short predicates for $N=64$, while its own summation over conjunctions of up to $9$ literals evaluates to $1.53\times10^{13}$. This corrected version resolves that inconsistency in favor of the summation. We define a finite-distinction space $D_{N}$, count its admissible existence predicates, derive a thermodynamic admissibility criterion from Landauer's erasure cost, and formalize re-entry as a map from high-level predicates to admissible predicates. For $N=64$ binary distinctions the admissible predicates number $2^{2^{64}}\approx10^{5.553\times10^{18}}$, of which the corrected count $1.5318446128384\times10^{13}$ are reachable by short Boolean formulas, an effectively zero fraction. Erasing one distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; cycling $10^{9}$ distinctions at $1\,$Hz requires $2.87\times10^{-12}\,$W; a nanowatt observer sustains at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$-state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls (factor $1.05\times10^{6}$), and the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, so the expected resolvable object count is essentially zero. The correction changes no qualitative conclusion but restores numerical consistency for any downstream use of the reachable-predicate count.

## 1. Introduction

Resource-constrained agents—embedded AI controllers, low-power sensors, or theoretical observers limited by a finite distinction budget—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad-hoc heuristics, which hides costs and produces ambiguous semantics. A robotic system that classifies hardware components through a shared ontology implicitly asserts the existence of every component it can name, even when its memory cannot store the corresponding distinctions. A quantum-foundational theorist may posit particle-like entities without accounting for the energy needed to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This correction is itself motivated by a concrete failure of that kind of quantitative claim. The previously published version of this paper stated in its summary table and claim register that the number of short-formula-reachable existence predicates for $N=64$ is $1.53\times10^{12}$, and used $1.53\times10^{12}$ as the numerator of the reachable fraction $f_{\text{reach}}$; yet the same paper's own summation over conjunctions of up to $9$ literals evaluates to $1.53\times10^{13}$, a factor-of-ten discrepancy. Any reader who propagated the tabulated value into a feasibility calculation—for example, an ontology engineer sizing a distinction budget against a power envelope—would inherit a tenfold error in the reachable set. The correction adopted here is the value the summation actually produces, $1.53\times10^{13}$; the discrepancy is a transcription error in the table and in the numerator of $f_{\text{reach}}$, not in the summation itself. This narrow, explicitly flagged style of correction follows the erratum discipline argued for in [4], which holds that an erratum should change exactly the flagged claims and leave the surrounding machinery intact.

The paper therefore asks: **what can a finite-entropy observer legitimately claim exists, what is the minimal physical cost of those claims, and which of those claims survive compression?** The analysis yields three concrete consequences: (1) the space of admissible existence predicates grows doubly exponentially, while the set reachable by short formulas is a vanishing fraction of it; (2) each maintained distinction incurs a non-zero energy cost fixed by Landauer's principle; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:
1. A formal definition of a finite distinction space and of admissible existence predicates, with the exact counting bound $2^{2^{N}}$ (Section 3, evaluated in Section 4.1).
2. A corrected count of short-formula-reachable predicates, $N_{\text{short}}=1.5318446128384\times10^{13}$ for $N=64$ and a literal bound of $9$, replacing the previously published $1.53\times10^{12}$, with the reachable fraction recomputed accordingly (Section 4.2).
3. A thermodynamic admissibility criterion derived from the erasure cost of distinctions, quantified as $E_{\text{bit}}=2.87\times10^{-21}\,$J at $300\,$K, $P_{\text{erase}}=2.87\times10^{-12}\,$W for $10^{9}$ distinctions at $1\,$Hz, and $N_{\max}=3.48\times10^{8}$ for a $10^{-12}\,$W observer (Sections 4.3–4.5).
4. A compression-collapse analysis showing a factor $1.05\times10^{6}$ compression drives the expected resolvable object count to $\approx3.9\times10^{-38}$ for $10^{5}$ objects, with a critical survival depth $r_{\text{crit}}\approx23$ (Sections 4.6–4.7).
5. An explicit erratum record stating which published numbers change, which do not, and why (Sections 4.2 and 6.2).

The counting and thermodynamic bounds developed here also bear on adjacent problems: the operational-reality question of when a theoretical quantity is computationally real [3], and the finite-precision question of whether physical quantities can carry infinite information [6], both of which use resource bounds to police ontological commitments.

## 2. Background and Related Work

The citation base available for this correction is limited to six works; the literature treatment is correspondingly focused, and this limitation is stated explicitly in Section 6.

**Operational closure and measurement cost.** The Autaxys ontological-closure criterion [3] proposes that a physical quantity is real only if a finite Turing-machine protocol approximates it with a computable modulus of convergence, so that unmeasurable quantities are operationally indistinguishable from nonexistent ones. Its experimental-design section makes the resource link explicit: if measuring a quantity $Q$ to precision $\varepsilon$ requires $\mu(-\log_{2}\varepsilon)$ steps and each step costs $E$ joules, the total energy is $E\cdot\mu(n)$, connecting the computational criterion to thermodynamic bounds through Landauer's principle, which that work states as an erasure cost of $k_{B}T\ln2$ per bit. This is the direct ancestor of the thermodynamic admissibility criterion used in Section 3.3: an existence claim is admissible for an observer only if the distinctions it requires fit inside the observer's erasure power budget.

**Finite specification and ontological indeterminism.** The Gisin–Del Santo program as examined in [6] argues that physical quantities contain only finite information and that real numbers, carrying infinite digit sequences, are physically unreal hidden variables of classical mechanics. That work's cross-domain analysis finds the same structural dynamic—finite specification, ontological openness, processual determination—across physics, computer science, cognition, information theory, biology, and sociology. This supplies the motivation for modeling an observer's ontology by a finite binary distinction space $D_{N}=\{0,1\}^{N}$ rather than a continuum: if only finitely many distinctions can be physically specified, the base coordinates of Section 3.1 are the whole representational budget. The same work's red-team finding R5—that neither the finite-precision program nor the closure framework has produced a differential empirical prediction—also cautions this paper: the bounds derived here are consistency and feasibility constraints, not new empirical content, and Section 7 proposes the experiment that would test them.

**Erratum discipline.** The errata paper [4] corrects two load-bearing sentences of a preprint on recursive self-consistency, arguing that a preprint which asserts a claim it cannot source imposes a real cost: every downstream argument citing the assertion inherits the error, and correcting the record becomes harder as the preprint circulates. Its discussion states the principle that governs the present correction: an erratum that silently rewrote more than the flagged sentences would itself introduce unverifiable content, so the corrections are kept narrow—what changes is the external support or the arithmetic of specific claims, while the surrounding mathematical machinery is untouched. Section 4.2 applies exactly this discipline to the $1.53\times10^{12}$ versus $1.53\times10^{13}$ discrepancy.

**Epistemic legibility of AI-assisted science.** The ignorance-audit position paper [5] documents the shift of the scientific bottleneck from production to evaluation, verification, and governance, and records a case in which a flagship paper produced inside an AI-assisted pipeline was separately identified as AI-generated through structural markers and synthetic citation anchors. Its central claim—that a pipeline cannot govern what it cannot see—motivates the explicit internal-consistency check performed in Section 4.2, where the tabulated value and the summation that should generate it are compared digit by digit. A summary table that disagrees with its own derivation is precisely the kind of illegibility that audit instruments are meant to expose.

**Extremal counting over combinatorial structures.** The Zagreb-index work [1] proves sharp lower bounds for degree-based topological indices over combinatorially defined families: its Theorem 1 gives $M_{1}(T)\geq9n-16$ for any tree with $n\geq2$ pendent vertices when $n$ is even, with equality attained by $4$-trees in which every internal vertex has degree $4$, and its Theorem 3 gives $M_{2}(T)\geq11n-27$ for $n\geq8$ pendent vertices. The methodological pattern—define the admissible set, count or bound over it exactly, and characterize the extremal members—is the same pattern used in Section 4.2, where the admissible set is the family of Boolean conjunctions of at most $9$ literals over $64$ variables and the count is evaluated term by term. The comparison also marks a difference: the bounds of [1] are tight and attained, whereas the short-formula count here is an exact enumeration of one syntactic class, not a bound over all compact representations.

**Systematic tabulation with stated precision.** The DRHBc nuclear mass table [2] tabulates binding energies, separation energies, radii, deformations, and Fermi surfaces for all even-$Z$ nuclei with $8\leq Z\leq120$, predicting $4829$ even-$Z$ nuclei to be bound with a root-mean-square deviation of $1.433\,$MeV from the experimental binding energies of $1244$ even-$Z$ nuclei, extending a previous even-even table of $2583$ nuclei with rms $1.518\,$MeV. That work illustrates the standard to which a published quantitative table should be held: every tabulated quantity traces to a stated calculation with systematic convergence checks, and a new table supersedes an old one by explicit extension. The erratum corrected here failed that standard in one cell: the summary table's reachable-predicate entry did not trace to the summation printed in its own derivation section. Section 4.2 restores the traceability.

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

### 4.2 Reachable short predicates — corrected count

We count conjunctions of up