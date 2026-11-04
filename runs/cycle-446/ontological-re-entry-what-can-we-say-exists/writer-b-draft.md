# Ontological Re-Entry: What Can We Say Exists?

## Abstract

The re-entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite-resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite-distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer's erasure cost, (iii) formalizing re-entry as a map from high-level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates, of which $1.5318446128384\times10^{13}$ are reachable by conjunctions of at most $9$ literals — an effectively zero fraction; a circulated claim that the reachable count is $\approx1.53\times10^{12}$ is rejected by the term-by-term summation, which confirms $1.53\times10^{13}$. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; a picowatt observer sustains at most $3.48\times10^{8}$ distinctions per second and a nanowatt observer $3.48\times10^{11}$, correcting a published figure of $3.5\times10^{5}\,\text{bits\,s}^{-1}$ for the nanowatt case. Ultrametric compression of a $2^{40}$-state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$, and under uniform placement of $10^{5}$ objects the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, giving an expected resolvable object count of $\approx3.9\times10^{-38}$; the previously circulated value $3.78\times10^{-36}$ is corrected here. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re-entry is physically admissible.

## 1. Introduction

Resource-constrained agents — embedded AI controllers, low-power sensors, or theoretical observers limited by a finite distinction budget — must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad-hoc heuristics, which hides costs and produces ambiguous semantics. A robotic system that classifies hardware components through a shared ontology implicitly asserts the existence of every component it can name, even when its memory cannot store the corresponding distinctions. A quantum-foundational theorist may posit particle-like entities without accounting for the energy needed to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

The cost of getting this wrong is not hypothetical. Ontology-based data access is now widespread in companies and government organizations, and ontologies have been adopted as high-level conceptual descriptions of data in distributed, heterogeneous repositories [1]. Legal-regulation assistants fine-tune large language models on curated supervised datasets with retrieval augmentation to support policymakers in crafting regulations [4]; every such system asserts a high-level vocabulary whose ontological commitments are rarely checked against the resources of the platform that carries it. Revision machinery for such ontologies already runs into wall-clock limits: the ontology-revision system of [6] sets a $1000$-second time limit on a single reasoner call, and vector preparation for a $1000$-axiom ontology takes about $6$ seconds on a laptop — compute that competes directly with the storage and erasure budget of the distinctions the ontology names. What is missing is a criterion that tells a designer when a proposed existence claim is physically admissible at all, and what it costs.

This paper therefore asks: **what can a finite-entropy observer legitimately claim exists, what is the minimal physical cost of those claims, and which of those claims survive compression?** We answer by constructing a finite-distinction framework, deriving explicit counting bounds, and connecting them to Landauer's erasure principle. The analysis yields three concrete consequences: (1) the space of admissible existence predicates grows doubly exponentially, while the set reachable by short formulas is a vanishing fraction of it; (2) each maintained distinction incurs a non-zero energy cost fixed by Landauer's principle; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:

- A term-by-term verified count of short reachable predicates over a $64$-bit distinction space, $N_{\text{short}}=1.5318446128384\times10^{13}$ against $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates, with the circulated $1.53\times10^{12}$ figure rejected by explicit summation (Sections 4.1–4.2).
- A corrected thermodynamic budget: $E_{\text{bit}}=2.87\times10^{-21}\,$J per distinction at $300\,$K, giving $3.48\times10^{8}$ distinctions per second at $P_{\text{obs}}=10^{-12}\,$W and $3.48\times10^{11}$ at $10^{-9}\,$W, replacing the published $3.5\times10^{5}\,\text{bits\,s}^{-1}$ microcontroller figure (Section 4.3).
- A recomputed compression-collapse probability $p_{1}=\lambda e^{-\lambda}\approx3.78\times10^{-41}$ with expected resolvable count $\approx3.9\times10^{-38}$, confirming the $10^{-41}$ exponent and correcting the circulated $3.78\times10^{-36}$ (Section 4.4).
- A falsification pathway: the specific observation that would refute the collapse result, and the smallest concrete measurement that would test the thermodynamic ceiling on real hardware (Sections 6 and 7).

The same accounting could matter wherever a finite budget carries an ontology: quantum-foundational debates about which entities a theory needs, and the design of low-power embedded classifiers whose label sets are existence claims. The analysis here supports those connections only insofar as the distinction-budget model applies to them; it does not establish them independently.

## 2. Background and Related Work

The re-entry problem sits at the junction of ontology engineering, the foundations of physics, and the thermodynamics of computation. Each field supplies one piece of the criterion assembled in Section 3.

**Ontologies as costly expressive structures.** Ontological queries are evaluated against an ontology rather than directly on a database, and their evaluation requires compiling the query into an equivalent database query and then optimizing the compiled result for size and efficiency [1]. The same source records that for the most well-known decidable fragments of OWL, ontological reasoning and query answering remain typically $2\text{exptime}$-complete, while OWL Full is undecidable. This matters here because it gives an independent, engineering-side demonstration that the expressive power of an ontology is paid for in computational resources: the re-entry map of Section 3.4 is, in that setting, exactly a rewriting step whose cost grows with the ontology's expressive class.

**Revision machinery under a compute budget.** Ontology revision incorporates a new ontology into an existing one and must resolve logical incoherence; the system of [6] implements revision algorithms with the OWL API, computes axiom vectors offline with a BERT-pretrained model, and uses the Pellet reasoner with R-MUPS computation capped at a $1000$-second time limit. Its measurements show that vector computation for a single ontology takes about $6$ seconds when the ontology contains $1000$ axioms, with time scaling mainly with axiom count, and that ontologies obtained from alignment translations, at no more than $50$ axioms, take no more than $0.5$ seconds. This is a concrete instance of the general situation modeled in Section 3: a finite machine maintaining a finite axiom set under a wall-clock and compute budget, where every revision step consumes resources that could otherwise store distinctions.

**Internal criteria versus the world in force.** In trajectory scoring, a world model can rank generic futures almost perfectly while remaining blind to which latent rule governs the present context; this failure is formalized as operator-blindness, and [2] proves that generic top-1 ranking cannot detect it whenever the candidate set excludes wrong-operator futures, with baselines retaining $\approx0.99$ generic top-1 while failing operator-sensitive metrics. The structural lesson for re-entry is direct: an observer can rank states of the world almost perfectly by its own internal criteria while being blind to which of its predicates are admissible in the world actually in force, which is precisely the failure that the admissibility filter of Section 3.2 is designed to police.

**Statistical admissibility with missing support.** Class-conditional conformal prediction requires labelled calibration examples of every class, and for classes with none, existing methods are either undefined or fall back to a shared marginal threshold; [3] shows that a descriptor-based correction improves worst-class coverage on ImageNet classes with zero calibration examples by $0.058$ $[0.006,0.110]$ at matched average set size, and that below roughly $35$ evaluation examples per class even an oracle observing the test labels cannot improve worst-class coverage. The parallel is exact in structure: below a resource threshold, no observer — however privileged — can resolve a distinction, which is the same shape as the compression-collapse result of Section 4.4, where below a critical depth no placement of objects yields resolvable individuals.

**Ontological clarity as a demand on theories.** The beables tradition holds that ontological clarity is a necessary condition on every physical theory: Bohm located the problems of the standard quantum interpretation in its obscure metaphysical content, and Bell was disappointed by the lack of ontological clarity in quantum mechanics, which he saw as the source of inconsistency between the Schrödinger equation and the collapse postulate and of redundancy in its axioms [5]. This paper shares that demand but operationalizes it: Section 3.2 defines admissibility syntactically and Section 3.3 thermodynamically, so that "ontologically clear" becomes a checkable property of a predicate relative to a distinction budget.

**Energy as a language-level property.** Landauer's principle states that each bit of information "forgotten" by a computing device dissipates heat proportional to ambient temperature; [8] formalizes the corresponding resource for automata: a device "forgets" $\log_{2}P$ bits when it arrives at a configuration with $P$ predecessors, and although any Turing machine — and even a two-way finite automaton — can be rewritten to be thermodynamically reversible, finite automata restricted to scan their input once in real-time fashion recognize only a proper subset of the regular languages at zero energy cost. Section 6.4 uses this to argue that the admissible-predicate class of Section 3.2 is not energy-neutral for one-pass observers.

**Computational reality criteria.** The ontological-closure criterion of [9] holds that a quantity is physically real only if a finite Turing-machine protocol approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions; its experimental-design section translates the requirement into resource estimates, with total energy cost $E\cdot\mu(n)$ when measuring to precision $\varepsilon$ requires $\mu(-\log_{2}\varepsilon)$ steps at $E$ joules each. The erasure-power form (1) of Section 3.3 is the fixed-step special case of that cost law. The finite-specification program examined in [11] supplies the complementary premise — physical quantities carry only finite information — and its cross-domain table records the same finite-specification dynamic across physics, computer science, cognition, information theory, biology, and sociology; its red-team finding R5, that neither the finite-precision program nor the closure framework has produced a differential empirical prediction, applies with equal force to the bounds derived here and motivates the microcontroller test of Section 7(c).

**Negative results as existence claims.** The PBO/Autaxys framework reports a systematic synthesis over $480$ papers that found zero matches for its core D/R+OC vocabulary, a result its authors read as shifting the burden of proof rather than proving uniqueness [12]. The present paper makes the analogous negative claim at smaller scale — that short formulas reach a vanishing fraction of predicate space — and supports it with the exact enumeration of Section 4.2 rather than a literature survey. Finally, the publication-side study of [7], which compared pre-prints to their final published versions across five similarity measures and found no significant aggregate differences within its arXiv corpus, is a reminder that numerical corrections of the kind made in Sections 4.2–4.4 are exactly the kind of change that propagates quietly between versions of a paper; the corrections here are stated explicitly so that they can be audited against the derivations rather than trusted to a version history.

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

### 3.2 Admissible existence predicates and the counting bound

**Definition 3.2 (Admissible existence predicate).** An existence predicate over $D_{N}$ is a subset $E\subseteq S_{N}$. The predicate is **admissible** iff there exists a finite Boolean formula $\varphi$ over the $N$ base coordinates such that

$$
E=\{x\in S_{N}\mid \varphi(x)=\text{true}\}.
$$

Two predicates are extensionally equivalent when they define the same subset of $S_{N}$.

**Proposition 3.1.** The number of extensionally distinct admissible predicates over $D_{N}$ is exactly $2^{2^{N}}$.

*Proof.* Every Boolean formula defines a characteristic function on $S_{N}$; conversely every subset of $S_{N}$ has a characteristic formula (a disjunction of minterms). Hence admissible predicates are in bijection with subsets of $S_{N}$, whose cardinality is $2^{|S_{N}|}=2^{2^{N}}$. $\square$

### 3.3 Thermodynamic admissibility

Erasing one bit at environment temperature $T_{\text{env}}$ costs

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
| Uniform random placement of objects in ultrametric balls | Standard Poisson occupancy model; a worst case for resolvability. |
| Coherence time $\tau=1\,$s; illustration powers $P_{\text{obs}}=10^{-12}\,$W (picowatt observer) and $10^{-9}\,$W (nanowatt microcontroller) | Representative of low-power edge devices; stated as assumptions, not measurements. |
| Binary distinction model captures the structure of physical quantities | Modeling choice; a continuous alternative is an open question (Section 6). |

All numerical evaluations use these constants; no external data are introduced. Where this revision reports a correction to a previously circulated number, the correction is decided by the paper's own derivations, shown step by step in Section 4.

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

### 4.2 Reachable short predicates — verified count, with the $10^{12}$ claim rejected

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

**Correction 1 (reachable-count exponent).** A claim circulated during revision holds that the number of reachable short predicates is $\approx1.53\times10^{12}$. We take the term-by-term evaluation above as decisive and reject the $10^{12}$ figure: the nine terms are each fixed by the recursion $\binom{64}{k}=\binom{64}{k-1}(64-k+1)/k$, the largest term alone is $1.41\times10^{13}$, and the running partial sums reproduce $15\,318\,446\,128\,384$ digit by digit. A count of $1.53\times10^{12}$ would require every term to be smaller by a factor of $10$, which the displayed products contradict; in particular the $k=9$ term $27\,540\,584\,512\times512=14\,100\,779\,270\,144$ exceeds $1.53\times10^{12}$ on its own. The reachable count is therefore $1.5318446128384\times10^{13}$, and $f_{\text{reach}}$ uses this value as numerator:

$$
f_{\text{reach}} = \frac{1.5318446128384\times