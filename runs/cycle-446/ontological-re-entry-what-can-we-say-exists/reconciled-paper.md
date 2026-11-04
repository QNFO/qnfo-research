# Ontological Re-Entry: What Can We Say Exists?

## Abstract

The re-entry problem asks which existence claims a finite-resource observer can legitimately make when its internal structure is projected back onto the world. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite-distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer's erasure cost, (iii) formalizing re-entry as a map from high-level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates, of which $1.5318446128384\times10^{13}$ are reachable by conjunctions of at most nine literals — an effectively zero fraction. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; a picowatt observer sustains at most $3.48\times10^{8}$ distinctions per second and a nanowatt observer $3.48\times10^{11}$. Ultrametric compression of a $2^{40}$-ball space into $2^{10}$ coarse balls, a factor of $2^{30}\approx1.07\times10^{9}$, and under uniform placement of $10^{5}$ objects the probability that any coarse ball contains exactly one object is $3.80\times10^{-41}$, giving an expected resolvable object count of $\approx3.9\times10^{-38}$. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re-entry is physically admissible.

## 1. Introduction

Resource-constrained agents — embedded AI controllers, low-power sensors, or theoretical observers limited by a finite distinction budget — must decide which entities they are allowed to assert as existing. Ontology-based systems such as those described in [1] and [6] commit to vocabularies whose computational cost is documented, but no criterion in that literature links the vocabulary to a physical distinction budget. A robotic system that classifies hardware components through a shared ontology implicitly asserts the existence of every component it can name, even when its memory cannot store the corresponding distinctions. A quantum-foundational theorist may posit particle-like entities without accounting for the energy needed to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

The cost of getting this wrong is not hypothetical. Ontologies have been adopted as high-level conceptual descriptions of data in distributed, heterogeneous repositories, and ontological query answering compiles high-level queries into database queries at a computational price that grows with expressive class [1]. Revision machinery for such ontologies already runs into wall-clock limits: the ontology-revision system of [6] sets a $1000$-second time limit on a single reasoner call, and vector preparation for a $1000$-axiom ontology takes about $6$ seconds on a laptop — compute that competes directly with the storage and erasure budget of the distinctions the ontology names. What is missing is a criterion that tells a designer when a proposed existence claim is physically admissible at all, and what it costs.

This paper therefore asks: **what can a finite-entropy observer legitimately claim exists, what is the minimal physical cost of those claims, and which of those claims survive compression?** We answer by constructing a finite-distinction framework, deriving explicit counting bounds, and connecting them to Landauer's erasure principle. The analysis yields three concrete consequences: (1) the space of admissible existence predicates grows doubly exponentially, while the set reachable by short formulas is a vanishing fraction of it; (2) each maintained distinction incurs a non-zero energy cost fixed by Landauer's principle; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

The contributions are:

- A term-by-term verified count of short reachable predicates over a $64$-bit distinction space, $N_{\text{short}}=1.5318446128384\times10^{13}$ against $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates (Sections 4.1–4.2).
- A thermodynamic budget: $E_{\text{bit}}=2.87\times10^{-21}\,$J per distinction at $300\,$K, giving $3.48\times10^{8}$ distinctions per second at $P_{\text{obs}}=10^{-12}\,$W and $3.48\times10^{11}$ at $10^{-9}\,$W (Section 4.3).
- A compression-collapse probability $p_{1}=\lambda e^{-\lambda}\approx3.80\times10^{-41}$ with expected resolvable count $\approx3.9\times10^{-38}$ (Section 4.4).
- A falsification pathway: the specific observation that would refute the collapse result, and the smallest concrete measurement that would test the thermodynamic ceiling on real hardware (Sections 6 and 7).

The same accounting could matter wherever a finite budget carries an ontology: quantum-foundational debates about which entities a theory needs, and the design of low-power embedded classifiers whose label sets are existence claims. The analysis here supports those connections only insofar as the distinction-budget model applies to them; it does not establish them independently.

## 2. Background and Related Work

The re-entry problem sits at the junction of ontology engineering, the foundations of physics, and the thermodynamics of computation. Each field supplies one piece of the criterion assembled in Section 3.

**Ontologies as costly expressive structures.** Ontological queries are evaluated against an ontology rather than directly on a database, and their evaluation requires compiling the query into an equivalent database query and then optimizing the compiled result for size and efficiency [1]. The same work records that for the most well-known decidable fragments of OWL, ontological reasoning and query answering remain typically $2\text{exptime}$-complete, while OWL Full is undecidable. This matters here because it gives an independent, engineering-side demonstration that the expressive power of an ontology is paid for in computational resources: the re-entry map of Section 3.4 is, in that setting, exactly a rewriting step whose cost grows with the ontology's expressive class.

**Revision machinery under a compute budget.** Ontology revision incorporates a new ontology into an existing one and must resolve logical incoherence; the system of [6] implements revision algorithms with the OWL API, computes axiom vectors offline with a BERT-pretrained model, and uses the Pellet reasoner with R-MUPS computation capped at a $1000$-second time limit. Its measurements show that vector computation for a single ontology takes about $6$ seconds when the ontology contains $1000$ axioms, with time scaling mainly with axiom count, and that ontologies obtained from alignment translations, at no more than $50$ axioms, take no more than $0.5$ seconds. This is a concrete instance of the general situation modeled in Section 3: a finite machine maintaining a finite axiom set under a wall-clock and compute budget, where every revision step consumes resources that could otherwise store distinctions.

**Internal criteria versus the world in force.** In trajectory scoring, a world model can rank generic futures almost perfectly while remaining blind to which latent rule governs the present context; this failure is formalized as operator-blindness, and [2] proves that generic top-1 ranking cannot detect it whenever the candidate set excludes wrong-operator futures, with baselines retaining $\approx0.99$ generic top-1 while failing operator-sensitive metrics. The structural lesson for re-entry is direct: an observer can rank states of the world almost perfectly by its own internal criteria while being blind to which of its predicates are admissible in the world actually in force, which is precisely the failure that the admissibility filter of Section 3.2 is designed to police.

**Ontological clarity as a demand on theories.** The beables tradition holds that ontological clarity is a necessary condition on every physical theory: Bohm located the problems of the standard quantum interpretation in its obscure metaphysical content, and Bell was disappointed by the lack of ontological clarity in quantum mechanics, which he saw as the source of inconsistency between the Schrödinger equation and the collapse postulate and of redundancy in its axioms [5]. This paper shares that demand but operationalizes it: Section 3.2 defines admissibility syntactically and Section 3.3 thermodynamically, so that "ontologically clear" becomes a checkable property of a predicate relative to a distinction budget.

**Energy as a language-level property.** Landauer's principle states that each bit of information "forgotten" by a computing device dissipates heat proportional to ambient temperature; [8] formalizes the corresponding resource for automata: a device "forgets" $\log_{2}P$ bits when it arrives at a configuration with $P$ predecessors, and although any Turing machine — and even a two-way finite automaton — can be rewritten to be thermodynamically reversible, finite automata restricted to scan their input once in real-time fashion recognize only a proper subset of the regular languages at zero energy cost. Section 6 uses this to argue that the admissible-predicate class of Section 3.2 is not energy-neutral for one-pass observers.

**Computational reality criteria.** The ontological-closure criterion of [9] holds that a quantity is physically real only if a finite Turing-machine protocol approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions; its experimental-design section translates the requirement into resource estimates, with total energy cost $E\cdot\mu(n)$ when measuring to precision $\varepsilon$ requires $\mu(-\log_{2}\varepsilon)$ steps at $E$ joules each. The erasure-power form (1) of Section 3.3 is the fixed-step special case of that cost law. The finite-specification program examined in [11] supplies the complementary premise — physical quantities carry only finite information — and its cross-domain table records the same finite-specification dynamic across physics, computer science, cognition, information theory, biology, and sociology; its red-team finding R5, that neither the finite-precision program nor the closure framework has produced a differential empirical prediction, applies with equal force to the bounds derived here and motivates the microcontroller test of Section 7(c).

**Negative results as existence claims.** The PBO/Autaxys framework reports a systematic synthesis over $480$ papers that found zero matches for its core D/R+OC vocabulary, a result its authors read as shifting the burden of proof rather than proving uniqueness [12]. The present paper makes the analogous negative claim at smaller scale — that short formulas reach a vanishing fraction of predicate space — and supports it with the exact enumeration of Section 4.2 rather than a literature survey.

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

All numerical evaluations use these constants; no external data are introduced.

## 4. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 4.1 Counting admissible existence predicates

**Inputs.** $N=64$ (modeling choice, Section 3.6); Proposition 3.1.

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

We count conjunctions of up to $9$ literals. For each $k$ literals there are $\binom{64}{k}$ ways to choose the variables and $2^{k}$ ways to assign polarity, giving $\binom{64}{k}2^{k}$ distinct conjunctions. The binomial coefficients are computed from the recursion $\binom{64}{k}=\binom{64}{k-1}\,(64-k+1)/k$; for example $\binom{64}{2}=64\times63/2=2016$, $\binom{64}{3}=2016\times62/3=41664$, and so on to $\binom{64}{9}=27\,540\,584\,512$. The term-by-term evaluation of (3) is:

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

The reachable fraction is

$$
f_{\text{reach}} = \frac{1.5318446128384\times10^{13}}{10^{5.553\times10^{18}}}\approx 0.
$$

### 4.3 Thermodynamic budget for distinction maintenance

**Inputs.** $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$ (fixed physical constant, Section 3.3); $T_{\mathrm{env}}=300\,\mathrm{K}$ (assumption, Section 3.6); $\ln 2 = 0.6931472$; illustration powers $P_{\mathrm{obs}}=10^{-12}\,\mathrm{W}$ and $10^{-9}\,\mathrm{W}$ (assumptions, Section 3.6).

Erasure cost per distinction:

$$
E_{\mathrm{bit}} = k_{B}\,T_{\mathrm{env}}\,\ln 2
= 1.380649\times10^{-23}\times300\times0.6931472.
$$

Step 1: $1.380649\times10^{-23}\times300 = 4.141947\times10^{-21}\,\mathrm{J}$.

Step 2: $4.141947\times10^{-21}\times0.6931472 = 2.8709\times10^{-21}\,\mathrm{J}$.

So

$$
E_{\mathrm{bit}} = 2.87\times10^{-21}\,\mathrm{J}
$$

per distinction at $300\,\mathrm{K}$.

Distinctions per second at a given power, from (2) with $\tau=1\,\mathrm{s}$:

$$
\dot{N}_{\max} = \frac{P_{\mathrm{obs}}}{E_{\mathrm{bit}}}.
$$

Picowatt observer:

$$
\dot{N}_{\max} = \frac{10^{-12}}{2.8709\times10^{-21}}
= \frac{1}{2.8709}\times10^{9}
= 3.483\times10^{8}\ \text{distinctions per second}.
$$

Nanowatt observer:

$$
\dot{N}_{\max} = \frac{10^{-9}}{2.8709\times10^{-21}} = 3.483\times10^{11}\ \text{distinctions per second}.
$$

Conversely, an observer cycling $10^{9}$ distinctions once per second requires at minimum

$$
P_{\mathrm{erase}} = 10^{9}\times2.8709\times10^{-21} = 2.87\times10^{-12}\,\mathrm{W}.
$$

These are lower bounds: they count only the Landauer erasure cost and ignore switching losses, leakage, and control overhead, all of which push real hardware further above the floor. The floor is nevertheless absolute, because Landauer's principle fixes the entropy cost of forgetting a bit at any fixed ambient temperature [8], and the same cost law appears as the fixed-step special case of the measurement-resource estimate $E\cdot\mu(n)$ of the ontological-closure framework [9].

### 4.4 Compression collapse of resolvable objects

**Inputs.** Tree levels $L_{\text{fine}}=40$, $L_{\text{coarse}}=10$, branching $b=2$ (modeling choice, Section 3.5); $m=10^{5}$ objects placed uniformly at random (assumption, Section 3.6).

Compression factor, from (4):

$$
\kappa = b^{L_{\text{fine}}-L_{\text{coarse}}} = 2^{30} = 1\,073\,741\,824 \approx 1.07\times10^{9}.
$$

The $2^{40}$ fine balls merge into $2^{10}=1024$ coarse balls.

Mean occupancy per coarse ball:

$$
\lambda = \frac{m}{b^{L_{\text{coarse}}}} = \frac{10^{5}}{1024} = 97.65625.
$$

Under the Poisson occupancy model, the probability that a given coarse ball contains exactly one object is $\lambda e^{-\lambda}$. The expected number of coarse balls containing exactly one object, i.e. the resolvable individuals after compression, is

$$
m_{\text{real}} = b^{L_{\text{coarse}}}\,\lambda e^{-\lambda}.
$$

Computing $e^{-\lambda}$: with $\log_{10}e = 1/\ln 10 = 0.434294$,

$$
\log_{10}\!\left(e^{-97.65625}\right) = -97.65625\times0.434294 = -42.4104,
$$

so

$$
e^{-97.65625} = 10^{-42.4104} = 10^{-43}\times10^{0.5896} = 3.886\times10^{-43}.
$$

Then

$$
p_{1} = \lambda e^{-\lambda} = 97.65625\times3.886\times10^{-43} = 3.796\times10^{-41},
$$

The expected resolvable count is

$$
m_{\text{real}} = 1024\times3.796\times10^{-41} = 3.887\times10^{-38}\approx3.9\times10^{-38}.
$$

The sensitivity is extreme: since $p_{1}=\lambda e^{-\lambda}$ with $\lambda\approx97.66$, a $1\%$ change in $m$ shifts $\log_{10}p_{1}$ by approximately $0.01\times97.66\times0.4343\approx0.42$, i.e. a factor of about $2.6$ in the survival probability. The conclusion that individual objects do not survive this compression is therefore robust only in order of magnitude, and Section 6 qualifies it accordingly. The structural reading is that below a critical depth, no placement of objects yields resolvable individuals: the observer's coarse vocabulary cannot re-enter the fine-grained existence claims it was meant to ground.

## 5. Results

The analytical pipeline yields the following concrete outcomes, each derived with shown arithmetic in Section 4.

1. **Combinatorial explosion of admissible predicates.** For $N=64$ binary distinctions the space of admissible existence predicates is $2^{2^{64}}\approx10^{5.553\times10^{18}}$ (Section 4.1), yet only $N_{\text{short}}=1.5318446128384\times10^{13}$ of them are reachable by conjunctions of at most $9$ literals (Section 4.2, term-by-term verified). The reachable fraction $f_{\text{reach}}$ is effectively zero: short formulas sample a vanishing slice of predicate space.

2. **Thermodynamic floor for distinction maintenance.** Erasing a single distinction at $300\,\mathrm{K}$ costs $E_{\mathrm{bit}}=2.87\times10^{-21}\,\mathrm{J}$ (Section 4.3). Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,\mathrm{W}$. Scaling linearly, a picowatt observer sustains at most $3.48\times10^{8}$ distinctions per second and a nanowatt observer at most $3.48\times10^{11}$ (Section 4.3). These are lower bounds on power and upper bounds on distinction throughput.

3. **Compression-induced ontology collapse.** An ultrametric tree with $L_{\text{fine}}=40$ and $L_{\text{coarse}}=10$ at $b=2$ compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $\kappa=2^{30}\approx1.07\times10^{9}$ (Section 4.4). Under uniform placement of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $p_{1}=\lambda e^{-\lambda}\approx3.80\times10^{-41}$ with $\lambda=97.65625$, giving an expected resolvable object count of $m_{\text{real}}\approx3.9\times10^{-38}$ (Section 4.4). Individual existence claims do not survive this compression; only coarse structure does.

Together these three results give the criterion asked for in Section 1: an existence claim is physically admissible for a finite-resource observer only if (i) its predicate is reachable within the observer's formula budget, (ii) the distinctions it requires fit within the observer's Landauer-limited power budget, and (iii) the predicate survives the observer's compression of its distinction space. A claim failing any condition is unre-enterable: the observer cannot legitimately assert it.

## 6. Discussion

The analysis rests on four assumptions: (1) the binary distinction model is sufficient to capture the structure of physical quantities; (2) the ultrametric compression factor $\kappa$ of (4) approximates the actual compression ratio; (3) uniform random placement of objects in the fine balls is a reasonable occupancy model; and (4) the critical survival depth is a good indicator of the minimum number of distinctions required to maintain a resolvable object count. Assumptions (1) and (3) are stated as modeling choices in Section 3.6, and $T_{\mathrm{env}}=300\,\mathrm{K}$ is stated there as an assumption; assumptions (2) and (4) are modeling choices introduced in Sections 3.5 and 4.4, not measurements.

**Limitations, itemized.**

- *Binary distinction model.* The results are derived for $S_{N}=\{0,1\}^{N}$. A continuous model of physical quantities, in which the distinction budget is not discrete, would change the counting bounds of Sections 4.1–4.2 entirely; whether such a model preserves the collapse result of Section 4.4 is an open question.
- *Uniform placement.* The Poisson occupancy model is a worst case for resolvability. Clustered placements could leave some coarse balls with exactly one object at far higher rates, raising $m_{\text{real}}$ by orders of magnitude; the collapse conclusion is robust only in order of magnitude, as the sensitivity computation in Section 4.4 shows (a $1\%$ change in $m$ moves $p_{1}$ by a factor of about $2.6$).
- *Erasure-only accounting.* Equations (1)–(2) count only Landauer erasure cost. Real observers pay switching, leakage, and control overhead, so the computed throughputs $3.48\times10^{8}$ and $3.48\times10^{11}$ distinctions per second are upper bounds on what the stated powers can sustain.
- *Fixed illustration parameters.* $\tau=1\,\mathrm{s}$, $T_{\mathrm{env}}=300\,\mathrm{K}$, and the two illustration powers are assumptions, not measurements of any device.
- *No differential empirical prediction.* As the red-team finding R5 recorded for the finite-specification and closure frameworks states, neither program has produced a differential empirical prediction [11]; the bounds derived here inherit that status. They are feasibility constraints, and the microcontroller test of Section 7(c) is the proposed differential measurement.
- *Short-formula restriction.* The bound $L_{\max}=9$ is a modeling choice. A different literal bound changes $N_{\text{short}}$ polynomially in $\binom{N}{L_{\max}}$ while the denominator $2^{2^{N}}$ is unchanged, so the vanishing-fraction conclusion is insensitive to $L_{\max}$ for any fixed bound, but the specific value $1.53\times10^{13}$ is not.

**Failure modes.** Two failure modes follow from the model. *Resolution collapse*: the observer's coarse vocabulary cannot resolve individuals, so its existence claims silently fail condition (iii) above. *False-premise capture*: the observer's ontology is inconsistent with the world actually in force, so its internal criteria rank states almost perfectly while the admissibility of its predicates goes unchecked — the same structural failure that the operator-blindness result of [2] formalizes for trajectory scoring, where a scorer retains $\approx0.99$ generic top-1 while failing operator-sensitive metrics. The admissibility filter of Section 3.2 is designed to police exactly this gap.

**Falsification.** The main quantitative result of Section 4.4 would be falsified by a concrete observation: a placement of $10^{5}$ objects into the $2^{40}$-ball space for which the number of coarse balls containing exactly one object is large — say within a few orders of magnitude of $1024$ rather than $\approx3.9\times10^{-38}$ — under the stated tree geometry. Since the derivation assumes uniform placement, the falsifying observation would show that real placements are so strongly clustered that the Poisson model fails by tens of orders of magnitude, which would collapse the compression result rather than merely perturb it. The thermodynamic ceiling of Section 4.3 would be falsified by a device that sustains more than $P_{\mathrm{obs}}\tau/(k_{B}T_{\mathrm{env}}\ln2)$ irreversible bit-erasures per second at the stated power and temperature, which would contradict Landauer's principle as formalized for finite automata in [8]; testing the ceiling at picowatt scale remains an open empirical question (Section 7(c)).

**Open questions.** (1) How does compression-induced collapse affect re-entry in quantum mechanics, where the relevant distinction budget may be far smaller? (2) Can the re-entry problem be formulated over a continuous model of physical quantities, and does collapse survive? (3) How does the re-entry criterion relate to computational realism, the question of whether a theoretical quantity is computationally real in the sense of [9]? (4) What occupancy model replaces uniform placement for naturally arising ultrametric data?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result, and what changes.** The users are designers of ontology-based systems and of low-power embedded classifiers. For ontology engineers, the criterion changes a design decision: before adopting an ontology whose vocabulary implies $n_{\mathrm{prec}}$ distinctions, check $n_{\mathrm{prec}}$ against the deployment platform's Landauer-limited budget $\dot{N}_{\max}$ from Section 4.3; the excess $\Delta n=n_{\mathrm{prec}}-N$ from Section 3.5 quantifies the entailments that will be lost. For embedded-systems designers, the result converts a label set into a power line item: a classifier asserting $10^{9}$ distinction-erasures per second needs at least $2.87\times10^{-12}\,\mathrm{W}$ on erasure alone. For foundational debates, the result supplies a checkable admissibility property in place of the unoperationalized demand for ontological clarity shared by the beables tradition [5]. Where no specific deployment can yet be named, the work is foundational: it establishes the counting and thermodynamic constraints that any future re-entry implementation must satisfy.

**(b) Readiness.** Against the NASA Technology Readiness Level definitions, this work is analytical and has not been peer reviewed: it is TRL 1–2. The derivations are paper-level; no hardware, no prototype, and no measurement exist. Analytical work of this kind does not exceed TRL 3, and nothing here supports a manufacturing-readiness claim.

**(c) Smallest next test.** The smallest concrete test of the thermodynamic ceiling is a microcontroller experiment: run a fixed erasure workload (a known number of bit-clears per second through a memory buffer) on a microcontroller whose supply power is metered at the $10^{-9}\,\mathrm{W}$ scale, and measure whether the achieved erasure rate exceeds the ceiling $\dot{N}_{\max}=3.48\times10^{11}$ distinctions per second derived in Section 4.3. An observed sustained rate above the ceiling at the metered power would refute the ceiling's applicability; a rate far below it would confirm only that real overheads dominate, which the model already predicts. The smallest test of the collapse result is computational, not physical: generate object placements in a $2^{40}$-ball ultrametric space under clustered and adversarial (non-uniform) distributions and count coarse balls with exactly one object; a distribution yielding a resolvable count many orders of magnitude above $3.9\times10^{-38}$ would refute the uniform-placement collapse claim as stated.

**(d) Binding constraints.** The constraints that would bind first in any implementation, in the order the derivations fix them: the erasure-energy floor $E_{\mathrm{bit}}=2.87\times10^{-21}\,\mathrm{J}$ (Section 4.3), which no material choice removes; the formula budget $L_{\max}$, which bounds which predicates are expressible at all (Section 4.2); and the compression geometry, which fixes $\kappa$ and therefore the resolvable-object count (Section 4.4). Data constraints — what occupancy model describes real placements — remain an open question rather than a derived bound. Regulatory or cost constraints are not derived here and are listed as open questions.

**(e) Order-of-magnitude bounds (projections).** Under the stated assumptions ($T_{\mathrm{env}}=300\,\mathrm{K}$, $\tau=1\,\mathrm{s}$, illustration powers from Section 3.6), the derived bounds are: $2.87\times10^{-21}\,\mathrm{J}$ per distinction-erasure; $3.48\times10^{8}$ distinctions per second at $10^{-12}\,\mathrm{W}$; $3.48\times10^{11}$ at $10^{-9}\,\mathrm{W}$. As a further projection, we assume a laptop-class platform drawing $P_{\text{plat}}=20\,\mathrm{W}$ during an ontology-revision preparation step; the revision system of [6] measures about $6\,\mathrm{s}$ of vector computation for a $1000$-axiom ontology on a laptop, so the energy per preparation step is $E_{\text{rev}}=20\times6=120\,\mathrm{J}$, equivalent to

$$
\frac{120}{2.8709\times10^{-21}} = 4.18\times10^{22}
$$

distinction-erasures at the Landauer floor. This quantifies how far practical ontology machinery operates above the thermodynamic floor; it is a projection under the stated assumptions, with the $6\,\mathrm{s}$ figure attributed to [6] and the $20\,\mathrm{W}$ platform power assumed.

**(f) Risks and misuse.** A direct misuse path exists: the admissibility criterion could be invoked to declare entities "non-existent" because a particular observer's budget cannot sustain them, when the model licenses only the weaker claim that the observer cannot legitimately assert them. The criterion is observer-relative; presenting it as world-relative would be an error of exactly the kind the re-entry framing is meant to prevent.

## 8. Conclusion

This paper derived a quantitative criterion for which existence claims a finite-resource observer can legitimately make. The criterion has three parts, each with a computed bound: reachability, under which short formulas over a $64$-bit distinction space reach only $1.5318446128384\times10^{13}$ of $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates (Sections 4.1–4.2); thermodynamic admissibility, under which erasing one distinction at $300\,\mathrm{K}$ costs $2.87\times10^{-21}\,\mathrm{J}$ and a nanowatt observer sustains at most $3.48\times10^{11}$ distinctions per second (Section 4.3); and compressibility, under which a $2^{30}$-fold ultrametric compression of a $10^{5}$-object placement leaves an expected resolvable count of $\approx3.9\times10^{-38}$ (Section 4.4). An existence claim failing any part is unre-enterable for that observer. The bounds are feasibility constraints, not measurements; binary distinctions and uniform placement are stated as assumptions in Section 3.6, erasure-only accounting is a stated limitation of the thermodynamic model, and the sensitivity of the collapse result is computed in Section 4.4 and qualified in Section 6; the microcontroller test and the clustered-placement computation of Section 7(c) are the proposed next steps that would de-risk or refute them.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.4). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 12 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Ontological Queries: Rewriting and Optimization (Extended Version). arXiv:1112.0343v1. https://arxiv.org/abs/1112.0343v1
[2] Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence. arXiv:2610.25360v1. https://arxiv.org/abs/2610.25360v1
[5] Beables, Primitive Ontology and Beyond: How Theories Meet the World. arXiv:2104.13859v1. https://arxiv.org/abs/2104.13859v1
[6] Ontology Revision based on Pre-trained Language Models. arXiv:2310.18378v2. https://arxiv.org/abs/2310.18378v2
[8] Energy Complexity of Regular Languages. arXiv:2204.06025v2. https://arxiv.org/abs/2204.06025v2
[9] https://papers.qnfo.org/papers/autaxys-ontological-closure. QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?.
[11] https://papers.qnfo.org/papers/finite-precision-oc-convergence. QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure.
[12] https://papers.qnfo.org/papers/pbo-autaxys. QNFO: Pillar 3: PBO/Autaxys — Pattern-Based Ontology as Intrinsic Self-Ordering.
