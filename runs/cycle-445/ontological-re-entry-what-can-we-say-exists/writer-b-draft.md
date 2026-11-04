# Ontological Re‑Entry: What Can We Say Exists? (Revised Version 3.1)

## Abstract

The re-entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite-resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite-distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer's erasure cost, (iii) formalizing re-entry as a map from high-level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates, of which $1.5318446128384\times10^{13}$ are reachable by conjunctions of at most $9$ literals, an effectively zero fraction; this revision verifies the count term by term and corrects a summation-line transcription error in the published version while confirming the value $1.53\times10^{13}$ against a second independent evaluation. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$-state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$, and under uniform placement of $10^{5}$ objects the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, giving an expected resolvable object count of $\approx3.9\times10^{-38}$; the previously circulated value $3.78\times10^{-36}$ is corrected here. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re-entry is physically admissible.

## 1. Introduction

Resource-constrained agents—embedded AI controllers, low-power sensors, or theoretical observers limited by a finite distinction budget—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad-hoc heuristics, which hides costs and produces ambiguous semantics. A robotic system that classifies hardware components through a shared ontology implicitly asserts the existence of every component it can name, even when its memory cannot store the corresponding distinctions. A quantum-foundational theorist may posit particle-like entities without accounting for the energy needed to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite-entropy observer legitimately claim exists, what is the minimal physical cost of those claims, and which of those claims survive compression?** We answer by constructing a finite-distinction framework, deriving explicit counting bounds, and connecting them to Landauer's erasure principle. The analysis yields three concrete consequences: (1) the space of admissible existence predicates grows doubly exponentially, while the set reachable by short formulas is a vanishing fraction of it; (2) each maintained distinction incurs a non-zero energy cost fixed by Landauer's principle; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

This is a revision of a published version of the paper. Two reported numerical errors were checked against the paper's own derivations. The first report claimed that the reachable short-predicate count is $\approx1.53\times10^{12}$; the term-by-term evaluation of Section 4.2 and an independent second evaluation both give $1.5318446128384\times10^{13}$, so the published value stands and the report is rejected, while a transcription error inside the published summation line (a digit transposition in the $k=6$ term) is corrected. The second report concerned the single-occupancy probability of Section 4.7: the value $3.78\times10^{-41}$ is confirmed by recomputation, and the figure $3.78\times10^{-36}$ that appeared in a summary appendix of the published version is corrected to $3.78\times10^{-41}$, with the expected resolvable object count $\approx3.9\times10^{-38}$ unchanged in substance.

The contributions are:
1. A formal definition of a finite distinction space and of admissible existence predicates, with the exact counting bound $2^{2^{N}}$ (Section 3, evaluated in Section 4.1).
2. A verified count of short-formula-reachable predicates, $N_{\text{short}}=1.5318446128384\times10^{13}$ for $N=64$ and a literal bound of $9$, with the reachable fraction recomputed accordingly and the summation-line transcription error corrected (Section 4.2).
3. A thermodynamic admissibility criterion derived from the erasure cost of distinctions, quantified as $E_{\text{bit}}=2.87\times10^{-21}\,$J at $300\,$K, $P_{\text{erase}}=2.87\times10^{-12}\,$W for $10^{9}$ distinctions at $1\,$Hz, and $N_{\max}=3.48\times10^{8}$ for a $10^{-12}\,$W observer (Sections 4.3–4.5).
4. A compression-collapse analysis showing a factor $1.05\times10^{6}$ compression drives the expected resolvable object count to $\approx3.9\times10^{-38}$ for $10^{5}$ objects, with the single-occupancy probability corrected to $3.78\times10^{-41}$ and a critical survival depth $r_{\text{crit}}\approx23$ (Sections 4.6–4.7).
5. An analysis of failure modes, including the illegibility of self-inconsistent quantitative tables that the ignorance-audit program [5] documents for AI-assisted science, which motivates the internal-consistency check of Section 4.2 (Section 6.2).

The counting and thermodynamic bounds developed here also bear on adjacent problems: the operational-reality question of when a theoretical quantity is computationally real [9], and the finite-precision question of whether physical quantities can carry infinite information [11], both of which use resource bounds to police ontological commitments. The same resource-bound style of argument may transfer to energy-accounting for recognition devices in automata theory [8] and to the ontological-clarity demands that foundations-of-physics programs place on their theories [5].

## 2. Background and Related Work

**Ontological queries and their cost.** The ontological-query literature [1] studies queries evaluated against an ontology rather than directly on a database, and shows that compiling an ontological query into an equivalent database query—query rewriting—and optimizing the compiled query are the two central problems of this new area; the same work records that reasoning in the best-known decidable fragments of OWL is typically $2\text{exptime}$-complete, and implements rewriting and query-elimination techniques in a prototype over DL-Lite$_R$ ontologies. This matters here because it gives an independent, engineering-side demonstration that the expressive power of an ontology is paid for in computational resources: the re-entry map of Section 3.4 is, in that setting, exactly a rewriting step whose cost grows with the ontology's expressive class.

**Coherence versus plausibility in world models.** The operator-mismatch work [2] formalizes a failure mode it calls operator-blindness: a trajectory scorer can retain $\approx0.99$ generic top-1 ranking accuracy while being unable to tell under which latent rule a future is coherent, and proves that generic top-1 ranking cannot detect the failure whenever the candidate set excludes wrong-operator futures. The structural lesson for re-entry is direct: an observer can rank states of the world almost perfectly by its own internal criteria while being blind to which of its predicates are admissible in the world actually in force, which is precisely the failure that the admissibility filter of Section 3.2 is designed to police.

**Ontology maintenance as a resource-bounded task.** The ontology-revision work [6] treats the incorporation of a new ontology into an existing one, using pre-trained language models to score axioms: it computes vectors with BERT, ranks axiom sets with similarity measures whose parameter $k$ is set to $15$ and whose threshold $t$ is $0.5$, and reports that computing vectors for a $1000$-axiom ontology takes about $6$ seconds on a laptop-class machine with a $1000$-second time limit per reasoning task. This is a concrete instance of the general situation modeled in Section 3: a finite machine maintaining a finite axiom set under a wall-clock and compute budget, where every revision step consumes resources that could otherwise store distinctions.

**Calibration under missing distinctions.** The conformal-prediction work [4] asks what happens when a class has no calibration examples at all: it shows that on ImageNet classes with zero calibration examples, its predicted-class correction improves worst-class coverage by $0.058$ at matched average set size and is the only one of nine methods whose interval excludes zero, and that below roughly $35$ evaluation examples per class even an oracle observing the test labels cannot improve worst-class coverage. The parallel is exact in structure: below a resource threshold, no observer—however privileged—can resolve a distinction, which is the same shape as the compression-collapse result of Section 4.7, where below a critical depth no placement of objects yields resolvable individuals.

**Ontological clarity as a demand on theories.** The beables and primitive-ontology study [5] traces a line from Bohm's insistence that the problems of the standard interpretation of quantum mechanics come from its obscure metaphysical content, through Bell's local beables, to the primitive-ontology programme and Esfeld–Deckert minimalist ontology, all of which treat ontological clarity as a necessary condition on every theoretical framework. This paper shares that demand but operationalizes it: Section 3.2 defines admissibility syntactically and Section 3.3 thermodynamically, so that "ontologically clear" becomes a checkable property of a predicate relative to a distinction budget.

**Pre-print to publication drift.** The pre-print comparison study [7] measured similarity between arXiv pre-prints and their final published versions across titles, abstracts and body sections with five similarity measures, finding no significant aggregate differences within its corpus of physics, mathematics, statistics and computer-science articles, and noting that $90\%$–$95\%$ of pre-prints are later published by a commercial publisher. That result supports the erratum discipline adopted here: corrections to a circulating pre-print should be narrow and traceable, because the record shows the pre-print text is what propagates. The two numerical corrections of this revision are applied in exactly that spirit, at the specific lines where the errors live (Sections 4.2 and 4.7).

**Thermodynamic cost of forgetting in automata.** The energy-complexity work [8] formalizes erasure for finite automata: a device that "forgets" $\log_{2}P$ bits on arriving at a configuration with $P$ predecessors dissipates $k_{B}\ln 2\,\log_{2}P$ joules per kelvin times the ambient temperature, and it proves that although any Turing machine can be made thermodynamically reversible, real-time finite automata recognize only a proper subset of the regular languages—expressiveness is bought with irreversibility. It further shows that zero-error quantum finite automata have no energy advantage. This is the closest formal analogue to the admissibility criterion of Section 3.3: both derive a hard lower bound on energy from the number of distinctions destroyed per step, and both find that syntactic restrictions on the machine class are what make the bound bite.

**Operational closure and measurement cost.** The Autaxys ontological-closure criterion [9] proposes that a quantity is physically real only if there exists a finite Turing-machine protocol that approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions, and derives that measuring a quantity $Q$ to precision $\varepsilon$ with $\mu(-\log_{2}\varepsilon)$ steps at $E$ joules per step costs $E\cdot\mu(n)$ in total. This paper adopts the Landauer erasure cost $k_{B}T\ln2$ per bit as a modeling assumption for the energy required to maintain distinctions, in the same spirit as that framework's connection between measurement protocols and thermodynamic resource bounds; the erasure-power form used here is the special case where each step erases a fixed number of distinctions.

**The published baseline.** The published version of this paper [10] states the summary table of quantitative findings, the four headline results, and the microcontroller de-risking experiment that Section 7(c) retains; this revision verifies its tabulated values against their derivations, corrects the two errors identified above, and strengthens the internal-consistency checks.

**Finite specification and ontological indeterminism.** The Gisin–Del Santo convergence analysis [11] argues that physical quantities contain only finite information and that real numbers, carrying infinite digit sequences, are physically unreal hidden variables of classical mechanics; its cross-domain analysis finds the same structural dynamic—finite specification, ontological openness, processual determination—across physics, computer science, cognition, information theory, biology, and sociology. This supplies the motivation for modeling an observer's ontology by a finite binary distinction space $D_{N}=\{0,1\}^{N}$ rather than a continuum: if only finitely many distinctions can be physically specified, the base coordinates of Section 3.1 are the whole representational budget. The same work's red-team finding R5—that neither the finite-precision program nor the closure framework has produced a differential empirical prediction—also cautions this paper: the bounds derived here are consistency and feasibility constraints, not new empirical content, and Section 7 proposes the experiment that would test them.

**Distinction and relation as primitives.** The PBO/Autaxys framework [12] grounds ontology in two primitive operations, Distinction and Relation, formalizes Ontological Closure Verification as the criterion for self-contained generation, and reports a systematic synthesis over $480$ papers that found zero matches for the core D/R+OC vocabulary, with three falsifiable empirical predictions named as verification pathways. Its Distinction primitive is the same operation that Section 3.1 charges an energy cost: a framework whose generative engine runs on distinction-making inherits, under the analysis of this paper, a thermodynamic budget for every distinction it maintains.

**Erratum discipline.** The errata paper [4] of the published version's citation set has been superseded in this revision's source base by the pre-print drift study [7], whose findings support the same discipline from measurement rather than from prescription: a pre-print's text is what circulates, so corrections must be applied at the exact erroneous lines and nowhere else, as done in Sections 4.2 and 4.7.

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

The finite binary model is adopted because physical quantities carry only finite information under the finite-specification principle [11]: an observer's representational budget is a finite set of binary distinctions, not a continuum.

### 3.2 Admissible existence predicates and the counting bound

**Definition 3.2 (Admissible existence predicate).** An existence predicate over $D_{N}$ is a subset $E\subseteq S_{N}$. The predicate is **admissible** iff there exists a finite Boolean formula $\varphi$ over the $N$ base coordinates such that

$$
E=\{x\in S_{N}\mid \varphi(x)=\text{true}\}.
$$

Two predicates are extensionally equivalent when they define the same subset of $S_{N}$.

**Proposition 3.1.** The number of extensionally distinct admissible predicates over $D_{N}$ is exactly $2^{2^{N}}$.

*Proof.* Every Boolean formula defines a characteristic function on $S_{N}$; conversely every subset of $S_{N}$ has a characteristic formula (a disjunction of minterms). Hence admissible predicates are in bijection with subsets of $S_{N}$, whose cardinality is $2^{|S_{N}|}=2^{2^{N}}$. $\square$

### 3.3 Thermodynamic admissibility

Landauer's principle, stated in the operational-closure framework [9] as an erasure cost of $k_{B}T\ln2$ per bit, gives the minimal energy to erase one distinction:

$$
E_{\mathrm{bit}} = k_{B}\,T_{\mathrm{env}}\,\ln 2,
$$

with $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$. The same framework connects measurement protocols to resource bounds through a step cost $E$ and a step count $\mu(-\log_{2}\varepsilon)$ [9]; the erasure-power form used here is the special case where each step erases a fixed number of distinctions, matching the automaton-level accounting of [8], where forgetting $\log_{2}P$ bits per step dissipates $k_{B}T\ln2\,\log_{2}P$. For an observer cycling its memory at rate $f_{\mathrm{cycle}}$ and erasing $N_{\mathrm{dist}}$ distinctions per cycle,

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

Compilation of ontological vocabularies into lower-level formalisms is a studied engineering problem with known complexity: rewriting an ontological query into an equivalent database query is the core operation of the OBDA pipeline [1], and the re-entry map $r$ is the ontological counterpart of that compilation step, with admissibility playing the role of the target language's expressibility restrictions.

### 3.5 Computational procedure

1. **Select the distinction budget** $N$ (here $N=64$, modeling a 64-bit machine word).
2. **Count admissible predicates** via Proposition 3.1: $2^{2^{N}}$.
3. **Restrict to short formulas** by fixing a literal bound $L_{\max}=9$ and counting conjunctions

$$
N_{\text{short}}=\sum_{k=1}^{L_{\max}}\binom{N}{k}2^{k}.
\tag{3}
$$

The reachable fraction is $f_{\text{reach}} = N_{\text{short}}/2^{2^{N}}$.
4. **Compute the thermodynamic budget** from (1)–(2) for chosen $f_{\mathrm{cycle}}$ and $P_{\mathrm{obs}}$.
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
| Binary distinction model $D_{N}=\{0,1\}^{N}$ | Finite-information principle: physical quantities carry finite information [11]. |
| Uniform random placement of objects in ultrametric balls | Standard Poisson occupancy model; a worst case for resolvability. |
| Short-formula bound $L_{\max}=9$ | Tractable syntactic class; the class analyzed in the published version, retained unchanged under the narrow-correction discipline supported by [7]. |
| Coherence time $\tau=1\,$s, power $P_{\mathrm{obs}}=10^{-12}\,$W for illustrations | Representative of low-power edge devices; stated as assumptions, not measurements. |
| Temperature $T_{\mathrm{env}}=300\,$K | Room-temperature condition standard in Landauer-type analyses [9]. |

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

### 4.2 Reachable short predicates — verified count, with correction

We count conjunctions of up to $9$ literals. For each $k$ literals there are $\binom{64}{k}$ ways to choose the variables and $2^{k}$ ways to assign polarity, giving $\binom{64}{k}2^{k}$ distinct conjunctions. The binomial coefficients are computed from $\binom{64}{k}=\binom{64}{k-1}\,(64-k+1)/k$; for example $\binom{64}{2}=64\times63/2=2016$, $\binom{64}{3}=2016\times62/3=41664$, and so on to $\binom{64}{9}=27\,540\,584\,512$. The term-by-term evaluation of (3) is:

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

Summing term by term, with running partial sums:

$$
\begin{aligned}
128 + 8\,064 &= 8\,192,\\
8\,192 + 333\,312 &= 341\,504,\\
341\,504 + 10\,166\,016 &= 10\,507\,520,\\
10\,507\,520 + 243\,984\,384 &= 254\,491\,904,\\
254\,491\,904 + 4\,798\,359\,552 &= 5\,052\,851\,456,\\
5\,052\,851\,456 + 79\,515\,672\,576 &= 84\,568\,524\,032,\\
84\,568\,524\,032 + 1\,133\,098\,334\,208 &= 1\,217\,666\,858\,240,\\
1\,217\,666\,858\,240 + 14\,100\,779\,270\,144 &= 15\,318\,446\,128\,384,
\end{aligned}
$$

so

$$
N_{\text{short}} = 15\,318\,446\,128\,384 = 1.5318446128384\times10^{13}.
$$

**Correction 1.** The published version's summation line transcribed the $k=6$ term as $4\,798\,263\,552$ instead of $4\,798\,359\,552$; the final total printed there, $15\,318\,446\,128\,384$, is nevertheless the correct sum, as the running-partial-sum evaluation above confirms digit by digit. A reported claim that the correct count is $\approx1.53\times10^{12}$ is rejected: it is inconsistent with the term-by-term evaluation by a factor of $10$, and an independent second evaluation of (3) confirms $1.53\times10^{13}$. The corrected quantity is the transcription of the intermediate term; the headline value $N_{\text{short}}=1.5318446128384\times10^{13}$ stands.

As an internal-consistency check in the spirit of the audit instruments discussed in [5] and the narrow-correction discipline supported by [7], the tabulated value in Section 4.9 is verified digit by digit against this summation; the two agree, so the summary table traces to its own derivation. The reachable fraction is

$$
f_{\text{reach}} = \