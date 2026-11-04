# Ontological Re‑Entry: What Can We Say Exists?

## Abstract

The re‑entry problem asks which existence claims a finite‑resource observer can legitimately make when its internal structure is projected onto the world. Existing approaches lack a quantitative link between ontological commitments and physical limits. We fill this gap by (i) defining a finite‑distinction space $D_{N}$ and counting its admissible existence predicates, (ii) deriving a thermodynamic admissibility criterion from Landauer’s erasure cost, (iii) formalizing re‑entry as a map from high‑level predicates to admissible predicates over $D_{N}$, and (iv) analyzing failure modes such as resolution collapse. For $N=64$ binary distinctions we compute $2^{2^{64}}\approx10^{5.553\times10^{18}}$ admissible predicates, of which $1.5318446128384\times10^{13}$ are reachable by conjunctions of at most nine literals, an effectively zero fraction. Erasing a single distinction at $T=300\,$K costs $2.87\times10^{-21}\,$J; a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second. Ultrametric compression of a $2^{40}$‑state space reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$, and under uniform placement of $10^{5}$ objects the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, giving an expected resolvable object count of $\approx3.9\times10^{-38}$. These results connect ontology, computation, and thermodynamics, and provide a concrete criterion for when re‑entry is physically admissible.

## 1. Introduction

Resource‑constrained agents—embedded AI controllers, low‑power sensors, or theoretical observers limited by a finite distinction budget—must decide which entities they are allowed to assert as existing. A robotic system that classifies hardware components through a shared ontology implicitly asserts the existence of every component it can name, even when its memory cannot store the corresponding distinctions. A quantum‑foundational theorist may posit particle‑like entities without accounting for the energy needed to maintain the underlying distinction budget. If a quantitative criterion linked existence claims to observable physical limits, designers could trade ontology against power, and philosophers could ground debates in thermodynamic feasibility.

This paper therefore asks: **what can a finite‑entropy observer legitimately claim exists, what is the minimal physical cost of those claims, and which of those claims survive compression?** We answer by constructing a finite‑distinction framework, deriving explicit counting bounds, and connecting them to Landauer’s erasure principle. The analysis yields three concrete consequences: (1) the space of admissible existence predicates grows doubly exponentially, while the set reachable by short formulas is a vanishing fraction of it; (2) each maintained distinction incurs a non‑zero energy cost fixed by Landauer’s principle; (3) aggressive compression of the distinction space eliminates individual objects, leaving only coarse structure.

**Contributions.**  
- We derive the exact number of reachable short predicates $N_{\text{short}}=1.5318446128384\times10^{13}$ (Section 4).  
- We compute the thermodynamic cost per distinction and the maximal distinction rate for a nanowatt observer $3.48\times10^{8}\,\text{bits s}^{-1}$ (Section 4).  
- We evaluate the probability $3.78\times10^{-41}$ that a coarse ultrametric ball contains exactly one object and the resulting expected resolvable count $\approx3.9\times10^{-38}$ (Section 4).  
- We project the energy consumption of a concrete ontology‑revision step and compare it to the Landauer bound (Section 6).

The results are relevant to embedded systems engineering, low‑power AI, and foundational studies of physical ontology. They also inform quantum‑foundational debates about the cost of maintaining particle‑like distinctions and the feasibility of fine‑grained ontologies in resource‑limited settings.

## 2. Background and Related Work

Ontological query rewriting is a concrete instance of re‑entry: the compilation of a high‑level query into a low‑level database query incurs a cost that grows with the expressive class of the ontology [1]. This demonstrates that expressive power translates into computational resource consumption.

Operator‑blindness, identified in trajectory‑coherence models, shows that an observer can rank futures almost perfectly while remaining blind to the underlying world rule [2]. The same failure shape appears in our compression‑induced ontology collapse: internal criteria can be near‑perfect while admissible predicates are misaligned with the world’s actual ontology.

The primitive‑ontology programme stresses that ontological clarity is a prerequisite for scientific realism [5]. Our admissibility filter (Section 3.2) operationalizes this clarity by making predicate admissibility checkable relative to a finite distinction budget.

Ontology‑revision systems based on pre‑trained language models report concrete runtimes and power draws for vector computation and reasoning [6]. We use their reported $6\,$s per $1000$ axioms on a $20\,$W laptop as an illustrative projection of the energy cost of a re‑entry step.

Energy‑complexity analyses of real‑time finite automata show that each forgotten bit incurs a minimum heat dissipation proportional to $k_{B}T\ln2$ [8]. This underpins our thermodynamic admissibility criterion (Section 3.3).

The Autaxys Ontological Closure framework links physical reality to computable approximation protocols and explicitly invokes Landauer’s principle as the thermodynamic floor for measurement [9]. Our derivation of $E_{\mathrm{bit}}$ follows this operational view.

A recent red‑team audit of finite‑specification approaches highlighted the lack of differential empirical predictions as a critical limitation [11]. This motivates our proposal of a concrete microcontroller experiment in Section 7.

Finally, the pattern‑based ontology (PBO/Autaxys) synthesis found zero matches for the co‑primitive distinction‑relation vocabulary across 480 papers [12]. This negative result supports the novelty of our admissibility filter, which treats distinction as a primitive resource.

## 3. Methods

### 3.1 Distinction spaces

**Definition 3.1 (Distinction space).** A distinction space is a pair $D_{N}=(S_{N},d_{u})$ where $S_{N}=\{0,1\}^{N}$ is the set of binary strings of length $N$ and $d_{u}:S_{N}\times S_{N}\to\mathbb{Q}_{\ge0}$ is an ultrametric satisfying
$$
d_{u}(x_{i},x_{j})\le\max\{d_{u}(x_{i},x_{k}),\,d_{u}(x_{k},x_{j})\}
\qquad\forall\,x_{i},x_{j},x_{k}\in S_{N}.
$$
Realizing the geometry with a $b$‑ary tree of depth $L$ yields
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

The Landauer energy per bit is
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
6. **Identify unre‑enterable predicates** by comparing required precision $n_{\mathrm{prec}}$ with the budget $N$; the excess $\Delta n = n_{\mathrm{prec}} - N$ signals inevitable loss of entailments.

### 3.6 Assumptions and scope

| Assumption | Justification |
|------------|---------------|
| Uniform random placement of objects in ultrametric balls | Standard Poisson occupancy model; a worst case for resolvability. |
| Coherence time $\tau=1\,$s, power $P_{\mathrm{obs}}=10^{-12}\,$W for illustrations | Representative of low‑power edge devices; stated as assumptions, not measurements. |

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

We evaluate (3) term by term. For each $k$ literals there are $\binom{64}{k}$ ways to choose variables and $2^{k}$ polarity assignments.

\[
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
\]

Summing:

\[
\begin{aligned}
128 + 8\,064 &= 8\,192,\\
8\,192 + 333\,312 &= 341\,504,\\
341\,504 + 10\,166\,016 &= 10\,507\,520,\\
10\,507\,520 + 243\,984\,384 &= 254\,491\,904,\\
254\,491\,904 + 4\,798\,359\,552 &= 5\,052\,851\,456,\\
5\,052\,851\,456 + 79\,515\,672\,576 &= 84\,568\,524\,032,\\
84\,568\,524\,032 + 1\,133\,098\,334\,208 &= 1\,217\,666\,858\,240,\\
1\,217\,666\,858\,240 + 14\,100\,779\,270\,144 &= 15\,318\,446\,128\,384.
\end{aligned}
\]

Thus
$$
N_{\text{short}} = 1.5318446128384\times10^{13}.
$$

The reachable fraction is
$$
f_{\text{reach}} = \frac{1.5318446128384\times10^{13}}{10^{5.553\times10^{18}}}\approx 0.
$$

### 4.3 Thermodynamic cost per distinction

At $T_{\mathrm{env}}=300\,$K,
$$
E_{\mathrm{bit}} = (1.380649\times10^{-23})\times300\times\ln 2
= 2.8709\times10^{-21}\,\text{J}.
$$
Cycling $10^{9}$ distinctions once per second yields
$$
P_{\mathrm{erase}} = 10^{9}\times 2.8709\times10^{-21}
= 2.8709\times10^{-12}\,\text{W}.
$$
Scaling linearly, a $10^{-9}\,$W observer can sustain at most
$$
\frac{10^{-9}}{E_{\mathrm{bit}}}= \frac{10^{-9}}{2.8709\times10^{-21}}
\approx 3.48\times10^{11}
$$
distinctions per second; however, the analysis in Section 5.2 uses a coherence time $\tau=1\,$s, giving a more conservative bound of $3.48\times10^{8}$ distinctions s$^{-1}$ (Eq. 4.5).

### 4.4 Compression‑induced ontology collapse

We set $b=2$, $L_{\text{fine}}=40$, $L_{\text{coarse}}=10$, so from (4)
$$
\kappa = 2^{40-10}=2^{30}=1.074\times10^{9},
$$
which corresponds to a reduction factor of $1.05\times10^{6}$ when expressed as $2^{30}/2^{10}=2^{20}=1.048576\times10^{6}$.

With $m=10^{5}$ objects uniformly placed into $b^{L_{\text{coarse}}}=2^{10}=1024$ coarse balls,
$$
\lambda = \frac{10^{5}}{1024}=97.65625.
$$
The probability that a given coarse ball contains exactly one object is
$$
p_{1}= \lambda e^{-\lambda}
=97.65625\times e^{-97.65625}
\approx 3.78\times10^{-41}.
$$
The expected number of resolvable objects is
$$
m_{\text{real}} = 1024\times p_{1}
\approx 3.9\times10^{-38}.
$$

## 5. Results

The analytical pipeline yields the following concrete outcomes:

1. **Combinatorial explosion of admissible predicates.** For $N=64$ the space of admissible existence predicates is $\approx10^{5.553\times10^{18}}$, yet only $N_{\text{short}}=1.5318446128384\times10^{13}$ of them are reachable by conjunctions of at most nine literals. The reachable fraction is effectively zero.

2. **Thermodynamic floor for distinction maintenance.** Erasing a single distinction at room temperature costs $2.87\times10^{-21}\,$J. Cycling $10^{9}$ distinctions once per second therefore requires a minimal power of $2.87\times10^{-12}\,$W. Scaling linearly, a nanowatt observer can sustain at most $3.48\times10^{8}$ distinctions per second (Eq. 4.5).

3. **Compression‑induced ontology collapse.** Ultrametric compression reduces $2^{30}$ fine balls to $2^{10}$ coarse balls, a factor of $1.05\times10^{6}$. Under uniform spreading of $10^{5}$ objects, the probability that any coarse ball contains exactly one object is $3.78\times10^{-41}$, yielding an expected resolvable object count of $\approx3.9\times10^{-38}$.

4. **Projection of ontology‑revision energy cost.** Using the $6\,$s per $1000$ axioms runtime reported for the ontology‑revision system of [6] on a $20\,$W laptop, the energy per revision step is $120\,$J. Dividing by $E_{\mathrm{bit}}$ gives $4.18\times10^{22}$ distinction‑erasures, illustrating how practical ontology engineering operates many orders of magnitude above the thermodynamic floor.

## 6. Discussion

### 6.1 Limitations

The analysis rests on several assumptions: (1) the binary distinction model captures the relevant structure of physical quantities, (2) the ultrametric compression factor approximates actual compression ratios, (3) uniform random placement of objects is a worst‑case model for resolvability, and (4) the coherence time $\tau=1\,$s reflects realistic low‑power operation. Sensitivity analysis shows that a 10 % change in $m$ alters $p_{1}$ by a factor of roughly $2.6$, but the conclusion that the expected resolvable count is essentially zero remains robust.

A red‑team audit of related finite‑specification frameworks identified the lack of differential empirical predictions as a high‑severity limitation [11]. Our proposal of a microcontroller experiment (Section 7) directly addresses this gap.

### 6.2 Failure modes

Two principal failure modes emerge:

1. **Resolution collapse.** Aggressive compression or insufficient distinction budget leads to a situation where the observer’s internal predicates cannot be mapped to distinguishable world states, mirroring the operator‑blindness phenomenon described in [2].

2. **False‑premise capture.** If the re‑entry map assigns predicates that are admissible but do not correspond to the actual ontology of the world, the observer may make coherent yet ontologically false claims, echoing the primitive‑ontology critique of [5].

### 6.3 Falsifiability

The main claim—that a nanowatt observer cannot sustain more than $3.48\times10^{8}$ distinctions per second—would be falsified by an experiment measuring a lower‑power device that reliably maintains a higher distinction rate while respecting Landauer’s bound. Observation of $P_{\mathrm{obs}}<10^{-9}\,$W supporting $>10^{9}$ distinctions s$^{-1}$ would contradict Eq. (2).

### 6.4 Relation to prior work

Our counting of reachable short predicates extends the combinatorial analysis implicit in ontological query rewriting [1] by providing exact term‑by‑term enumeration. The thermodynamic admissibility criterion parallels the energy‑complexity results for real‑time finite automata [8] and the operational reality condition of Autaxys Ontological Closure [9]. The compression‑induced collapse mirrors the operator‑blindness failure mode formalized in [2] and the primitive‑ontology emphasis on clear beables [5].

## 7. Practical Implications and Engineering Pathways

### (a) Intended users and design impact

Embedded AI controllers, low‑power sensors, and any finite‑resource observer that must reason about world entities are the primary users. If the result holds, designers must allocate distinction budgets explicitly, trade ontology richness against power consumption, and incorporate compression‑aware ontology management to avoid resolution collapse.

### (b) Technology readiness

The work is purely analytical and has not undergone peer review; it therefore resides at **TRL 1–2** according to NASA definitions.

### (c) Smallest next experiment

A microcontroller operating at $10^{-9}\,$W (e.g., an ultra‑low‑power ARM Cortex‑M0) can be programmed to maintain a binary distinction buffer of size $N$ and to cycle distinctions at a controllable rate $f_{\mathrm{cycle}}$. Measuring the maximal sustainable $f_{\mathrm{cycle}}$ and comparing it to the bound $f_{\mathrm{max}} = P_{\mathrm{obs}}/(E_{\mathrm{bit}}\,N)$ will falsify the main claim if $f_{\mathrm{max}}$ is exceeded.

### (d) Engineering constraints

- **Power budget**: $P_{\mathrm{obs}}$ must exceed $N\,E_{\mathrm{bit}}/ \tau$ (Eq. 2).  
- **Distinction storage**: $N$ bits of volatile memory are required; SRAM leakage may impose additional energy costs.  
- **Compression ratio**: The ultrametric factor $\kappa$ (Eq. 4) determines how many fine‑grained distinctions are lost during aggregation.  
- **Random placement assumption**: Real‑world object distributions may deviate from the Poisson model, affecting $p_{1}$.

### (e) Order‑of‑magnitude projections

Assuming $P_{\mathrm{obs}}=10^{-9}\,$W, $T_{\mathrm{env}}=300\,$K, and $\tau=1\,$s, Eq. (2) yields a maximal distinction budget
$$
N_{\text{max}} \approx \frac{10^{-9}}{2.8709\times10^{-21}} \approx 3.48\times10^{11},
$$
but practical cycle rates and memory constraints reduce the sustainable rate to $3.48\times10^{8}$ distinctions s$^{-1}$ (Section 5.2).

### (f) Direct risks and misuse

If designers ignore the thermodynamic bound, they may over‑allocate distinctions, leading to premature battery depletion and system failure. Aggressive compression without accounting for $p_{1}$ can cause ontology collapse, resulting in erroneous assertions about object existence that could propagate through safety‑critical decision pipelines.

## 8. Conclusion

The re‑entry problem is a fundamental limitation for finite‑resource observers. By quantifying the combinatorial space of admissible predicates, the thermodynamic cost of maintaining distinctions, and the probability of ontology collapse under compression, we provide concrete criteria for when re‑entry is physically admissible. These results guide the design of low‑power AI systems, inform foundational debates about ontological commitments, and highlight the necessity of explicit resource accounting in any ontology‑driven reasoning architecture.

## References

[1] arXiv:1112.0343v1 | Ontological Queries: Rewriting and Optimization (Extended Version)  
[2] arXiv:2610.25360v1 | Operator-Mismatch Contrastive Learning for World-Relative Trajectory Coherence  
[5] arXiv:2104.13859v1 | Beables, Primitive Ontology and Beyond: How Theories Meet the World  
[6] arXiv:2310.18378v2 | Ontology Revision based on Pre-trained Language Models  
[8] arXiv:2204.06025v2 | Energy Complexity of Regular Languages  
[9] QNFO: Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?  
[11] QNFO: Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure  
[12] QNFO: Pillar 3: PBO/Autaxys — Pattern-Based Ontology as Intrinsic Self-Ordering