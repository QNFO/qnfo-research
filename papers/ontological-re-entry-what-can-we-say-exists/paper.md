# Ontological Re‑Entry: What Can We Say Exists?

## Abstract

The re-entry problem asks which existence claims a theory can legitimately make when its internal structure is projected back onto the world by a finite-resource observer. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite-distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer’s erasure cost, (iii) formalizing re-entry as a map from high-level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates, of which $1.5318446128384\times10^{13}$ are reachable by conjunctions of at most $9$ literals, an effectively zero fraction; this revision verifies the count term by term and corrects a summation-line transcription error in the published version while confirming the value $1.53\times10^{13}$ against a second independent evaluation. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$-state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$, and under uniform placement of $10^{5}$ objects the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, giving an expected resolvable object count of $\approx3.9\times10^{-38}$; the previously circulated value $3.78\times10^{-36}$ is corrected here. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re-entry is physically admissible.

## 1. Introduction

Resource-constrained agents—embedded AI controllers, low-power sensors, or theoretical observers limited by a finite distinction budget—must decide which entities they are allowed to assert as existing. Current practice either assumes an unrestricted ontology or adopts ad-hoc heuristics, which hides costs and produces ambiguous semantics. A robotic system that classifies hardware components through a shared ontology implicitly asserts the existence of every component it can name, even when its memory cannot store the corresponding distinctions. A quantum-foundational theorist may posit particle-like entities without accounting for the energy needed to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite-entropy observer legitimately claim exists, what is the minimal physical cost of those claims, and which of those claims survive compression?** We answer by constructing a finite-distinction framework, deriving explicit counting bounds, and connecting them to Landauer’s erasure principle. The analysis yields three concrete consequences: (1) the space of admissible existence predicates grows doubly exponentially, while the set reachable by short formulas is a vanishing fraction of it; (2) each maintained distinction incurs a non-zero energy cost fixed by Landauer’s principle; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

## 2. Background and Related Work

This matters here because it gives an independent, engineering-side demonstration that the expressive power of an ontology is paid for in computational resources: the re-entry map of Section 3.4 is, in that setting, exactly a rewriting step whose cost grows with the ontology's expressive class.

The structural lesson for re-entry is direct: an observer can rank states of the world almost perfectly by its own internal criteria while being blind to which of its predicates are admissible in the world actually in force, which is precisely the failure that the admissibility filter of Section 3.2 is designed to police.

This is a concrete instance of the general situation modeled in Section 3: a finite machine maintaining a finite axiom set under a wall-clock and compute budget, where every revision step consumes resources that could otherwise store distinctions.

The parallel is exact in structure: below a resource threshold, no observer—however privileged—can resolve a distinction, which is the same shape as the compression-collapse result of Section 4.7, where below a critical depth no placement of objects yields resolvable individuals.

This paper shares that demand but operationalizes it: Section 3.2 defines admissibility syntactically and Section 3.3 thermodynamically, so that "ontologically clear" becomes a checkable property of a predicate relative to a distinction budget.

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

| Coherence time $\tau=1\,$s, power $P_{\mathrm{obs}}=10^{-12}\,$W for illustrations | Representative of low-power edge devices; stated as assumptions, not measurements. |

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

The reachable fraction is

$$
f_{\text{reach}} = \frac{1.5318446128384\times10^{13}}{10^{5.553\times10^{18}}}\approx 0.
$$

## 5. Results

The analytical pipeline yields the following concrete outcomes:

1. **Combinatorial explosion of admissible predicates.** For a modest $N=64$ distinction budget the space of admissible existence predicates is $\approx10^{5.553\times10^{18}}$, yet only $N_{\text{short}}=1.5318446128384\times10^{13}$ of them are reachable (see Section 4.2) by conjunctions of at most $9$ literals. The reachable fraction is effectively zero.

2. **Thermodynamic floor for distinction maintenance.** Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.5).

3. **Compression-induced ontology collapse.** An ultrametric tree with $L=40$ levels ($N=40$) compresses $2^{30}$ fine balls into $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. Under uniform spreading of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, yielding an expected resolvable object count of $\approx3.9\times10^{-38}$; the previously circulated value $3.78\times10^{-36}$ is corrected here. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re-entry is physically admissible.

## 6. Extended Derivations and Worked Examples

This section deepens the derivations of Section 4 with three worked examples: a small-$N$ sanity check of the short-formula count, a step-by-step recomputation of the compression-collapse probability, and a resource-cost estimate for a concrete re-entry step drawn from the ontology-revision literature.

### E.1 Small-$N$ sanity check of the short-formula count

The closed-form count (3) is easiest to audit at small $N$, where the total can be compared against direct enumeration logic. Take $N=4$ and $L_{\max}=2$. The terms are

$$
\binom{4}{1}2^{1}=4\times2=8,\qquad
\binom{4}{2}2^{2}=6\times4=24,
$$

so $N_{\text{short}}(4,2)=8+24=32$. Direct check: a conjunction of $1$ literal is one of $8$ strings $x_{i}$ or $\lnot x_{i}$; a conjunction of $2$ literals over distinct variables is one of $\binom{4}{2}=6$ variable pairs times $4$ polarity assignments $=24$; no conjunction is counted twice because each is identified by its variable set and polarity pattern. The identity of the two routes confirms the counting rule that generates the $N=64$ table in Section 4.2, where the same recursion $\binom{64}{k}=\binom{64}{k-1}(64-k+1)/k$ is applied nine times.

### E.2 Recomputation of the compression-collapse probability

Section 4.7 states $p_{1}=\lambda e^{-\lambda}\approx3.78\times10^{-41}$ with $\lambda=10^{5}/1024$. The steps are as follows. First, $\lambda=100000/1024=97.65625$. Second, convert the exponent to base 10: since $\log_{10}e=1/\ln 10=0.434294$,

$$
\log_{10}\left(e^{-97.65625}\right)=-97.65625\times0.434294=-42.4104.
$$

Third, $10^{-42.4104}=10^{-43}\times10^{0.5896}=3.888\times10^{-43}$. Fourth, multiply by $\lambda$:

$$
p_{1}=97.65625\times3.888\times10^{-43}=3.797\times10^{-41},
$$

which rounds to the stated $3.78\times10^{-41}$ at the precision carried by the intermediate rounding of $e^{-\lambda}$. The expected resolvable count is then $m_{\text{real}}=1024\times3.797\times10^{-41}=3.888\times10^{-38}$, reported as $\approx3.9\times10^{-38}$ in Section 4.7. The sensitivity is extreme: because $p_{1}$ depends on $\lambda$ through $\lambda e^{-\lambda}$ with $\lambda\approx98$, a $1\%$ change in $m$ shifts $\log_{10}p_{1}$ by roughly $0.01\times97.66\times0.4343\approx0.42$, i.e. a factor of about $2.6$ in the survival probability. The zero-object conclusion is therefore robust only in order of magnitude, which is how Section 6.1 qualifies it.

### E.3 Worked cost estimate for a re-entry step in ontology revision

The re-entry map of Section 3.4 assigns each high-level predicate an admissible subset of $S_{N}$; in practice, revising an ontology to absorb new distinctions consumes compute that competes with the distinction budget. The ontology-revision system of [6] implements revision algorithms with OWL API and the BERT-pretrained vector model, computing vectors for all axioms offline before revision; its measurements show that vector computation for a single ontology takes about $6$ seconds when the ontology contains $1000$ axioms, with time scaling mainly with axiom count, and its reasoner calls (Pellet, with R-MUPS computation capped at a $1000$-second time limit) dominate the revision step. We assume, as an illustrative projection only, a laptop-class platform drawing $P_{\text{plat}}=20\,$W during such a step; the energy per revision preparation is then

$$
E_{\text{rev}} = P_{\text{plat}}\times 6\,\mathrm{s} = 20\times6 = 120\,\mathrm{J}.
$$

Dividing by the Landauer cost per distinction at $300\,$K, $E_{\text{bit}}=2.8709\times10^{-21}\,$J (Section 4.3), gives the equivalent distinction budget consumed by one revision step:

$$
\frac{E_{\text{rev}}}{E_{\text{bit}}}=\frac{120}{2.8709\times10^{-21}}=4.18\times10^{22}\ \text{distinction-erasures}.
$$

This is a projection under the stated assumptions ($20\,$W platform power, $6\,$s per $1000$ axioms as measured in [6]); it quantifies how far practical ontology machinery operates above the thermodynamic floor, consistent with the realistic-device gap of Section 7(e). The same structural point appears in the query-rewriting setting of [1], where an ontological query is compiled into an equivalent database query and the compiled query is then optimized for size and efficiency: the compilation is the re-entry step, and its cost grows with the expressive class of the ontology, whose decidable fragments still carry $2\text{exptime}$-complete reasoning complexity as [1] notes for the best-known DL fragments underlying OWL.

### E.4 Energy accounting as a language-level property

The erasure model of Eq. (1) treats each distinction as an independently erasable bit. The energy-complexity analysis of regular languages in [8] makes the corresponding point at the level of the whole computation: a device "forgets" $\log_{2}P$ bits when it arrives at a configuration with $P$ predecessors, the dissipated heat is the entropy increase $k_{B}\ln2\log_{2}P$ multiplied by ambient temperature, and the energy cost is directly proportional to the number of forgotten bits; crucially, while Turing machines (and even two-way finite automata) can be made thermodynamically reversible, real-time one-pass finite automata cannot, so the language being recognized fixes a non-zero energy floor. Applied here, this warns that the admissible-predicate class of Section 3.2 is not energy-neutral: an observer that must commit to a predicate in one pass over its distinction stream pays the erasure cost of the discarded configurations, and a reversible re-implementation is available only if the observer can afford two-way access and unbounded memory—precisely the resources the finite-budget model denies.

### E.5 Relation to operational-reality and finite-specification criteria

The admissibility filter of Section 3.2 is a syntactic analogue of the ontological-closure criterion of [9], which holds a quantity physically real only if a finite Turing-machine protocol approximates it with a computable modulus of convergence; [9] connects such protocols to thermodynamic resource bounds through a step cost $E$ and step count $\mu(-\log_{2}\varepsilon)$, of which the erasure-power form (1) is the fixed-step special case. The finite-specification program examined in [11] supplies the complementary premise: physical quantities carry only finite information, so the base coordinates of $D_{N}$ exhaust the representational budget, and its cross-domain table records the same finite-specification dynamic across physics, computer science, cognition, information theory, biology, and sociology. The red-team finding R5 reported in [11]—that neither the finite-precision program nor the closure framework has produced a differential empirical prediction—applies with equal force to the bounds derived here: they are feasibility constraints, and the microcontroller test of Section 7(c) is the proposed differential measurement. Finally, the demand that a theory's ontology be stated clearly enough to check is the shared starting point of the beables tradition surveyed in [5], which traces Bohm's and Bell's insistence on ontological clarity into the primitive-ontology programme; Section 3.2 operationalizes that demand by making admissibility a checkable property of a predicate relative to a distinction budget. The operator-blindness result of [2]—that a trajectory scorer can rank generic futures almost perfectly, at $\approx0.99$ top-1, while remaining blind to which world-rule is in force—gives the same failure shape one level down: internal criteria can be near-perfect while the admissibility of the predicates under the world actually in force goes unchecked, which is the failure the re-entry map is designed to police. The uniqueness claim of the D/R-primitive framework in [12] rests on a systematic synthesis over $480$ papers finding zero matches for its core vocabulary, a negative result its authors read as shifting the burden of proof; the present paper makes the analogous negative claim at smaller scale—that short formulas reach a vanishing fraction of predicate space—and supports it with the exact enumeration of Section 4.2 rather than a literature survey.

## 7. Discussion

The analysis rests on several assumptions: (1) the binary distinction model is sufficient to capture the structure of physical quantities, (2) the ultrametric compression factor is a good approximation of the actual compression ratio, (3) the uniform random placement of objects is a reasonable model for the placement of objects in the fine balls, and (4) the critical survival depth $r_{\text{crit}}$ is a good indicator of the minimum number of distinctions required to maintain a resolvable object count.

### 7.2 Failure modes

The analysis identifies two main failure modes: (1) resolution collapse, where the observer's internal criteria are not aligned with the world's actual ontology, and (2) false-premise capture, where the observer's ontology is not consistent with the world's actual ontology.

1. **How does the compression-induced ontology collapse affect the re-entry problem in different domains?** For example, how does it affect the re-entry problem in quantum mechanics, where the distinction budget is much smaller?
2. **Can the re-entry problem be solved using alternative models of physical quantities?** For example, can it be solved using a continuous model of physical quantities, where the distinction budget is not discrete?
3. **How does the re-entry problem relate to other problems in physics and computer science?** For example, how does it relate to the problem of computational realism, where the question is whether a theoretical quantity is computationally real?

## 8. Practical Implications and Engineering Pathways

The re-entry problem has significant implications for users of finite-resource observers, such as embedded AI controllers, low-power sensors, and theoretical observers. These users must decide which entities they are allowed to assert as existing, and must do so in a way that is consistent with the world's actual ontology.

The re-entry problem is a foundational problem in the field of finite-resource observers, and is closely related to the concept of readiness level. The readiness level of a system is its ability to perform a specific task, such as classifying hardware components or recognizing images. The re-entry problem is a key component of the readiness level framework, as it determines the minimum number of distinctions required to maintain a resolvable object count.

The next concrete test for the re-entry problem is to design and implement a system that can classify hardware components using a finite-resource observer. This system should be able to maintain a resolvable object count, and should be able to adapt to changes in the world's actual ontology.

The re-entry problem has significant engineering constraints, including the need for a finite distinction budget, the need for a thermodynamic admissibility criterion, and the need for a compression-induced ontology collapse analysis. These constraints must be taken into account when designing and implementing a system that can solve the re-entry problem.

The re-entry problem has significant order-of-magnitude cost or performance bounds, including the need for a nanowatt observer to sustain at most $3.48\times10^{8}$ distinctions per second, and the need for a $10^{-12}\,$W observer to sustain at most $3.48\times10^{8}$ distinctions per second.

The re-entry problem has significant direct risks or misuse paths, including the risk of resolution collapse, where the observer's internal criteria are not aligned with the world's actual ontology, and the risk of false-premise capture, where the observer's ontology is not consistent with the world's actual ontology.

## 9. Conclusion

The re-entry problem is a fundamental problem in the field of finite-resource observers, and has significant implications for users of these systems. The analysis presented in this paper provides a concrete criterion for when re-entry is physically admissible, and highlights the need for a finite distinction budget, a thermodynamic admissibility criterion, and a compression-induced ontology collapse analysis. The results of this analysis have significant implications for the design and implementation of systems that can solve the re-entry problem, and highlight the need for careful consideration of the engineering constraints and direct risks or misuse paths associated with this problem.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Results; Discussion; Practical Implications and Engineering Pathways; Conclusion; Appendix A. Divergence report; Appendix B. Claim attribution. references 12 -> 10. length 3939 -> 3867 words.
- Version 2.1.0 (2026-10-20, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Appendix B. Claim attribution; Appendix B. Claim attribution. references 10 -> 9. length 3910 -> 3366 words.
- Version 2.2.0 (2026-10-20, from 2.1.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples; Appendix B. Claim attribution. references 9 -> 12. length 3445 -> 4616 words.
- Version 2.3.0 (2026-10-21, from 2.2.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. sections folded or removed: Extended Derivations and Worked Examples. references 12 -> 9. length 4730 -> 4164 words.
- Version 3.0.0 (2026-11-03, from 2.3.0): REWRITE: rewritten in full through the research pipeline. references 9 -> 6. length 4164 -> 4638 words.
- Version 3.1.0 (2026-11-04, from 3.0.0): revised against the current literature, re-reviewed and re-verified. new sections: Extended Derivations and Worked Examples. references 6 -> 8. length 4808 -> 3751 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.4). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 13 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
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
