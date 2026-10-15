# The Switching Economics of Hamiltonian Re-Entry Computation: A Cost-Model Comparison with Stored-Program Architectures

## Abstract

Stored-program (von Neumann) architectures pay a per-operation switching cost for instruction fetch, decode, and memory traffic, while a proposed Hamiltonian-computation paradigm identifies computation with continuous dynamical trajectories that re-enter a designated operating region of phase space. The specific gap addressed here is that the re-entry proposal has no explicit, parameterized cost accounting against the switching economics of the stored-program regime, so its economic case cannot be evaluated or falsified. This paper adopts the minimal two-model cost formalism of the prior re-entry analysis — an explicit-controller model with per-operation switching cost $c_{\mathrm{sw}}$ and an autonomous re-entry model with per-operation cost $c_{\mathrm{re}}$ — and extends it with a cache-aware break-even derivation and a cross-convention figure of merit. Under the stated illustrative assumptions ($k_{\mathrm{acc}} = 4$ memory accesses per operation, $t_{\mathrm{mem}} = 16$ time units per access, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$), the switching cost per operation is $c_{\mathrm{sw}} = 65$ time units against a re-entry cost $c_{\mathrm{re}} = 5$, a ratio of $13.0$; the switching overhead fraction is $f_{\mathrm{sw}} = 64/65 = 0.984615\ldots$ versus $f_{\mathrm{re}} = 0.2$. Break-even occurs at $t_{\mathrm{mem}}^{*} = 1$ time unit, the verdict tolerates re-entry overheads up to $t_{\mathrm{re}}^{*} = 61$ time units, and the new cache-aware analysis gives a break-even hit rate $h^{*} = 15/15.5 = 0.967741\ldots$ for a cache access costing half a time unit. The comparison is placed inside the von Neumann-algebra and switching-hardware literatures. All quantitative results are model projections with stated assumptions; no empirical measurements are claimed.

## 1. Introduction

Every computing architecture pays a price for moving state from where it is stored to where it is transformed. In a stored-program (von Neumann) architecture this price appears as the fetch-decode-execute cycle: before any arithmetic happens, the machine must switch its control and data paths to bring an instruction into the processing unit. John Backus identified two levels of this cost. The "von Neumann bottleneck" is the limited throughput between CPU and memory, much smaller than the rate at which the CPU can work; the "intellectual von Neumann bottleneck" is that programming cannot go beyond planning the enormous traffic of words through that bottleneck; and the "von Neumann vicious circle" is that non-von Neumann architectures cannot be developed for lack of effective non-von Neumann languages, which cannot be created for lack of conceptual foundations for such architectures [2]. Any proposal for a fundamentally different computational substrate must therefore be evaluated not only for physical plausibility but for its switching economics, stated in terms that survive the language-architecture lock-in the vicious circle describes.

The proposal evaluated here is the Hamiltonian-computation paradigm: the identification of computation with continuous dynamical trajectories that re-enter a designated operating region of phase space, so that one act of dynamical setup is reused many times without an external controller re-issuing it. A prior analysis, which this paper takes as its starting point, constructed a minimal two-model cost comparison of this re-entry paradigm against von Neumann switching costs. That analysis derived a per-operation switching cost of $65$ time units against a re-entry cost of $5$ under explicitly memory-bound assumptions, a ratio of $13.0$, and identified the parameters on which the case turns. What remains missing is threefold. First, the prior model assumes fully serialized, uncached memory, and no cache-aware break-even condition has been derived; since real hierarchies cache aggressively, this is the assumption most likely to overturn the verdict. Second, the two cost conventions used in the prior work (time units and abstract cost units) have not been combined into a single cross-convention figure of merit. Third, the comparison has not been connected to the mathematical literature on von Neumann algebras, ergodic theory, and entropy, which supplies the natural language for the long-time statistics of re-entering dynamical systems and for the entropy bookkeeping of the loop.

Who faces this problem, and what does it cost them? Researchers proposing non-von Neumann substrates — dynamical-systems, neuromorphic, and quantum-computing groups — currently must argue their case against an architecture whose switching economics are entrenched, without a shared parameter vocabulary in which the argument can be settled by measurement. If the cost model developed here holds as a framing, the debate reduces to a small set of measurable quantities: the effective memory time $t_{\mathrm{mem}}^{\mathrm{eff}}$, the re-entry overhead $t_{\mathrm{re}}$, the per-pass loop cost $c_p$, and the reuse factor $n$. If it fails — for example, if the cache-aware break-even hit rate turns out to be unreachable in practice — the re-entry proposal loses its economic case in the regime that matters, and resources shift accordingly.

The contributions are:

1. A restatement and verification, with fully shown arithmetic, of the two-model cost formalism and its headline results ($c_{\mathrm{sw}} = 65$, $c_{\mathrm{re}} = 5$, ratio $13.0$, break-even $t_{\mathrm{mem}}^{*} = 1$, robustness threshold $t_{\mathrm{re}}^{*} = 61$), drawn from the prior analysis and re-derived in Section 4.
2. A new cache-aware break-even derivation giving the critical cache hit rate $h^{*} = 15/15.5 = 0.967741\ldots$ at which the re-entry advantage vanishes for a cache access costing $0.5$ time units (Section 4, Derivation 8).
3. A cross-convention figure of merit $\sqrt{13.0 \times 3.125} = 6.3738\ldots$ combining the time-unit and cost-unit parameterizations (Section 4, Derivation 9).
4. A literature synthesis placing the comparison inside the switching-fabric literature [1], the Backus critique [2], and the von Neumann-algebra tradition of entropy [3], spectral graph complexity [4], ergodic theory [5], regularity [6], embedding and amenability [7], spectral theory of positive maps [8], and rigidity [9] (Section 2).
5. An explicit falsification criterion and limitations list for the claimed advantage (Section 6).

No empirical measurements are reported. Every number in Sections 4 and 5 is either derived by shown arithmetic from parameters declared in Section 3, or is a projection whose assumptions are stated inline.

## 2. Background and Related Work

**Switching fabrics and the cost of redirection.** The throughput of input-queued packet switches is limited by head-of-line blocking, and at each time-slot a traffic scheduler must configure a connection pattern for the switch fabric to avoid output contentions and maximize throughput; a good scheduler improves throughput and reduces end-to-end delay at low computation complexity [1]. Input scheduling based on Birkhoff-von-Neumann (BvN) decomposition achieves high throughput and low complexity, but the performance of the BvN switch becomes less predictable when the input traffic is bursty; the deflection-compensated BvN (D-BvN) switch architecture was proposed to enhance the quasi-static scheduling based on BvN decomposition, and its simulation compares average end-to-end delay against an ideal-deflection analytical lower bound, with the required critical VOQ size for a loss rate of $P_l = 10^{-5}$ entering the comparison and the average delay increasing linearly with burstiness [1]. This literature supplies the precedent for treating a switching event as the atomic unit of cost: in [1] the switching fabric's schedule is the bottleneck resource, exactly as the fetch-decode-execute cycle is in the stored-program model of Section 3. The re-entry paradigm's claim, in this vocabulary, is that a closed dynamical loop removes the per-slot scheduling act altogether.

**The Backus critique and the vicious circle.** The "von Neumann vicious circle" is the fact that non-von Neumann computer architectures cannot be developed because of the lack of widely available and effective non-von Neumann languages, and new languages cannot be created because of lack of conceptual foundations for non-von Neumann architectures, the reason being that programming languages are high-level abstract isomorphic copies of von Neumann computers [2]. The same source develops the functional-programming counter-tradition: primitive recursion as the basic schema for computing on natural numbers, higher-order primitive recursion via the Grzegorczyk iterator $R^{A}$ with $R^{A}(1)(c)(a) = a$ and $R^{A}(n+1)(c)(a) = c(n)(R^{A}(n)(c)(a))$, and the observation that the C$\lambda$aSH approach — from Haskell through term rewriting to a standard HDL — remains "still unsatisfactory" because the rewritten term ends as imperative code [2]. This matters here in two ways. It explains why a cost comparison must be stated in architecture-neutral parameters rather than in the vocabulary of either regime; and it shows that the loop-reuse structure of the re-entry model has a functional analogue, since the iterator $R^{A}$ re-uses the step function $c$ across $n$ applications just as the re-entry loop re-uses one dynamical segment across $n$ passes.

**Von Neumann entropy as bookkeeping.** Von Neumann associated an entropy quantity to a statistical operator in 1927, by a gedanken experiment on the ground of phenomenological thermodynamics, and the discussion was extended in his 1932 book *Mathematische Grundlagen der Quantenmechanik*; the historical reconstruction stresses the role of superselection sectors [3]. The same historical account records Shannon's derivation that the only uncertainty measure $H$ satisfying three reasonable requirements is $H = -K\sum_{i=1}^{n}p_i \log p_i$, with $K$ a positive constant [3]. For the re-entry model this supplies the bookkeeping functional: when the paper of Section 4 computes a dimensionless overhead quantity $\eta = \ln(5/4)$, it is a logarithmic ratio of the same kind that the Gibbs-von Neumann and Shannon functionals make meaningful, and any future thermodynamic interpretation of re-entry cost would be written in this currency.

**Entropy as a spectral complexity measure.** The von Neumann entropy of a graph is a spectral complexity measure applied in complex-network analysis and pattern recognition, with two variants based on the graph Laplacian and the normalized graph Laplacian; because of its computational complexity, previous works approximated it, and experiments on path graphs, random graphs with small-world structure, and real-world networks showed that the Laplacian and normalized Laplacian entropies capture related yet different structural patterns, that the quadratic approximations fail to explain non-trivial structures for the Laplacian case, and that the quality of approximation depends on graph topology [4]. This is directly relevant to the re-entry loop: a re-entry structure is a graph of dynamical transitions, and [4] establishes both that entropy-style measures characterize such structure and that cheap approximations of them can mislead in a topology-dependent way — a caution for any attempt to certify a re-entry loop's cost by an approximate spectral quantity.

**Long-time statistics of dynamical cocycles.** The classical Multiplicative Ergodic Theorem of Oseledets has been generalized to cocycles taking values in a semi-finite von Neumann algebra, allowing a continuous Lyapunov distribution; in the finite-dimensional version, for a measure-preserving transformation $f$ and a measurable cocycle $c$ satisfying a first-moment condition, the limit operator $\Lambda(x) := \lim_{n \to \infty}[c(n,x)^{*}c(n,x)]^{1/2n}$ exists almost everywhere and its eigenvalues $e^{\lambda_1(x)} > \cdots > e^{\lambda_k(x)}$ are the Lyapunov exponents, invariant under $f$ [5]. The proof technique builds the pointwise ergodic theorem into the von Neumann-algebra setting, with the cocycle uniformly bounded and averages $A_n(x,y) = \frac{1}{n}\sum_{k=0}^{n-1}\phi(F^k(x,y))$ converging [5]. For re-entry computation this is the rigorous language for the question the model assumes away: whether the mean re-entry time $t_{\mathrm{re}}$ exists and is stable is a statement about the asymptotic statistics of a dynamical cocycle, and [5] shows both that such statistics can be controlled by ergodic-theoretic hypotheses and that the control requires moment and boundedness conditions that a physical re-entry loop would have to be verified against.

**Regularity as an algebraic lens on loops.** A ring is von Neumann regular if for every $a$ there is a $b$ with $aba = a$; the notion was invented by von Neumann in the 1930s in his study of von Neumann algebras, regular rings are precisely the rings for which every module is flat, and regularity is rare — a group ring $RG$ is regular if and only if $R$ is regular, $G$ is locally finite and the order of every finite subgroup of $G$ is invertible in $R$, while Leavitt path algebras are regular if and only if the defining graph is acyclic [6]. The acyclicity criterion is the sharpest connection to this paper's subject: in an algebra built from a graph, regularity fails exactly when cycles exist, and the re-entry loop is precisely a cycle. If one models a re-entry computation's transition structure as an algebra over its loop graph, [6] indicates that the algebraic fingerprint of the loop is a loss of regularity, suggesting that loop-containing computations resist the flat-module algebraic techniques that work for acyclic (feed-forward, straight-line) computations.

**Embeddings, amenability, and tractability of verification.** For tracial von Neumann algebras, self-tracial stability holds if and only if the algebra is amenable, under the Connes Embedding Problem; amenability is defined by every derivation being inner, hyperfiniteness by expression as the $\sigma$-weak closure of an increasing union of finite-dimensional subalgebras, and the tracial ultraproduct construction with microstates — tuples of matrices approximating operators in many moments — makes embeddings into $R^{\mathcal{U}}$ tractable, since satisfying the Connes Embedding Problem is equivalent to "having sufficiently many microstates" [7]. This bears on the re-entry program as a tractability caveat: certifying that a candidate Hamiltonian loop behaves as modeled is an embedding-and-approximation problem of the microstate type, and [7] shows that the corresponding stability properties collapse to amenability, a strong hypothesis not guaranteed for physical loop dynamics.

**Spectral theory of the averaging operator.** For an ergodic semigroup of linear normal positive unital maps on a von Neumann algebra, the eigenvectors are either multiples of a partial isometry, linear combinations of two partial isometries, or multiples of a unitary operator; and by examples, mere positivity of the maps is not sufficient for the Frobenius theory that holds for completely positive maps, in which the point spectrum of an ergodic semigroup forms a group with one-dimensional eigenspaces spanned by unitaries [8]. The fixed-point space $M_1$ of the semigroup — the eigenspace at eigenvalue $1$ — is where an averaged, time-independent description of a repeatedly re-entering system would live [8]. The warning for the re-entry model is concrete: if the per-pass evolution is merely positive rather than completely positive, the clean convergence-to-a-unique-average picture can fail, with eigenspaces of dimension greater than one, so the assumption that repeated re-entries average to a well-defined steady behavior is a spectral hypothesis, not a formality.

**Rigidity of observable subdynamics.** A countable discrete group $\Gamma$ satisfies the invariant von Neumann subalgebras rigidity (ISR) property if every $\Gamma$-invariant von Neumann subalgebra $\mathcal{M}$ in $L(\Gamma)$ is of the form $L(\Lambda)$ for some normal subgroup $\Lambda \lhd \Gamma$; the property is proved for torsion-free non-amenable hyperbolic groups, using the trace-preserving conditional expectation $\mathbb{E}_{\mathcal{M}}$ and Fourier-coefficient equations [9]. The structural moral for re-entry computation is that the sub-dynamics of a large dynamical system that an observer can actually isolate are rigidly constrained: which intermediate algebras exist inside the full system algebra determines which re-entry loops are even definable as separate computations, and [9] shows this can be a severe restriction in negatively curved systems.

**The prior cost analysis.** The immediate predecessor of this paper constructs the two-model comparison in full: an explicit-controller model with per-operation cost $c_{\mathrm{sw}} = k_{\mathrm{acc}} t_{\mathrm{mem}} + t_{\mathrm{alu}}$ and an autonomous re-entry model with $c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}}$, reporting under the assumptions $k_{\mathrm{acc}} = 4$, $t_{\mathrm{mem}} = 16$, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$ the results $c_{\mathrm{sw}} = 65$, $c_{\mathrm{re}} = 5$, overhead fractions $64/65$ and $0.2$, total-time ratio $13.0$ for $N_{\mathrm{op}} = 10^6$, break-even $t_{\mathrm{mem}}^{*} = 1$, and robustness to $t_{\mathrm{re}}^{*} = 61$. Its discussion already flags the central weakness: if effective memory time drops to $t_{\mathrm{mem}}^{\mathrm{eff}} = 1$ time unit through caching, the models tie exactly at $c_{\mathrm{sw}} = 4 \times 1 + 1 = 5 = c_{\mathrm{re}}$, so the headline ratio holds only in the memory-bound regime. This paper takes that model as given, re-derives its numbers with the arithmetic shown, and extends it where the prior analysis stopped: at the cache.

## 3. Methods

### 3.1 The two cost models

The formalism is adopted from the prior analysis and restated for completeness.

**Von Neumann switching model.** A stored-program machine executes a program of $N_{\mathrm{op}}$ logical operations. Each operation requires $k_{\mathrm{acc}}$ memory accesses (instruction fetch plus data load/store) before the logical work is done. Let $t_{\mathrm{mem}}$ be the effective time per memory access and $t_{\mathrm{alu}}$ the time for the logical work itself. The per-operation cost is

$$c_{\mathrm{sw}} = k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}},$$

and the total cost is

$$T_{\mathrm{sw}} = N_{\mathrm{op}} \left( k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}} \right).$$

The switching overhead per operation is $k_{\mathrm{acc}}\, t_{\mathrm{mem}}$, with overhead fraction

$$f_{\mathrm{sw}} = \frac{k_{\mathrm{acc}}\, t_{\mathrm{mem}}}{k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}}}.$$

**Hamiltonian re-entry model.** The machine state is a point $x_t$ in phase space evolving under a Hamiltonian $H$. A computation of $N_{\mathrm{op}}$ logical steps corresponds to $N_{\mathrm{op}}$ re-entries of the trajectory into a designated operating region $\mathcal{R} \subset \Omega$. Let $t_{\mathrm{dyn}}$ be the mean time for the trajectory to traverse one useful dynamical segment, and $t_{\mathrm{re}}$ the mean re-entry overhead: the extra time spent steering the trajectory back into $\mathcal{R}$ after each useful segment, including any classical control intervention. The per-re-entry cost is

$$c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}},$$

with total $T_{\mathrm{re}} = N_{\mathrm{op}} (t_{\mathrm{dyn}} + t_{\mathrm{re}})$ and overhead fraction

$$f_{\mathrm{re}} = \frac{t_{\mathrm{re}}}{t_{\mathrm{dyn}} + t_{\mathrm{re}}}.$$

### 3.2 Comparison criterion

The re-entry model beats the switching model on total time when $T_{\mathrm{re}} < T_{\mathrm{sw}}$, i.e. when

$$t_{\mathrm{dyn}} + t_{\mathrm{re}} < k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}}.$$

### 3.3 New methodological elements introduced here

**Cache-aware effective memory time.** To relax the uncached assumption (A2 below), we introduce a two-level memory model. A fraction $h$ (the hit rate) of memory accesses is served by a cache in time $t_{\mathrm{hit}}$; the remaining fraction $1 - h$ is served by main memory in time $t_{\mathrm{mem}}$. The effective memory time is

$$t_{\mathrm{mem}}^{\mathrm{eff}} = h\, t_{\mathrm{hit}} + (1 - h)\, t_{\mathrm{mem}} = t_{\mathrm{mem}} - h\,(t_{\mathrm{mem}} - t_{\mathrm{hit}}),$$

and the cache-aware comparison replaces $t_{\mathrm{mem}}$ by $t_{\mathrm{mem}}^{\mathrm{eff}}$ in $c_{\mathrm{sw}}$. The break-even hit rate $h^{*}$ is the value of $h$ at which $c_{\mathrm{sw}} = c_{\mathrm{re}}$.

**Cross-convention figure of merit.** The prior analysis reports the advantage under two conventions: a time-unit ratio $13.0$ and a cost-unit ratio $R = 3.125$ [10]. To combine them into one scale-free indicator we use the geometric mean $\sqrt{13.0 \times 3.125}$, which is insensitive to which convention is larger and penalizes disagreement between conventions.

**Entropy bookkeeping quantity.** Following the logarithmic form of the entropy functionals discussed in [3], we compute the dimensionless quantity

$$\eta = \ln\!\left(\frac{t_{\mathrm{re}} + t_{\mathrm{dyn}}}{t_{\mathrm{dyn}}}\right),$$

a model construct, not a thermodynamic entropy measurement.

### 3.4 Assumptions

(A1) Both machines perform the same $N_{\mathrm{op}}$ logical operations; the models differ only in update overhead. (A2) In the baseline model, memory accesses are serialized and no caching removes them; the cache-aware extension of Section 3.3 relaxes this with the stated two-level model. (A3) The re-entry overhead $t_{\mathrm{re}}$ is a fixed parameter, not derived from first principles; deriving it from the ergodic theory of the loop cocycle along the lines of [5] is left open. (A4) Mixing is adequate that the mean re-entry time exists; the spectral hypotheses behind such averaging are discussed via [8] in Section 6. (A5) All time and cost values are illustrative assumptions, stated in Section 4; none is a measurement.

## 4. Analysis

Every number in this section is derived from stated inputs. Inputs are of two kinds: structural integers of the model ($k_{\mathrm{acc}}$) and illustrative parameter values stated explicitly as assumptions. The baseline parameter set is taken from the prior analysis [10], which states the assumptions $k_{\mathrm{acc}} = 4$, $t_{\mathrm{mem}} = 16$, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$ and the results derived from them; no value is taken from measurement.

**Input 1 (structural).** $k_{\mathrm{acc}} = 4$ memory accesses per operation: one instruction fetch, one operand load, one store, one next-instruction prefetch. Source: model definition.

**Input 2 (assumed, labeled).** $t_{\mathrm{alu}} = 1$ time unit (normalization). $t_{\mathrm{mem}} = 16$ time units per access, representing a memory hierarchy much slower than the arithmetic unit. $t_{\mathrm{dyn}} = 4$ time units per useful dynamical segment. $t_{\mathrm{re}} = 1$ time unit per re-entry. Source: the prior analysis, where all are declared as illustrative assumptions.

**Derivation 1: switching cost per operation.**

$$c_{\mathrm{sw}} = k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}} = 4 \times 16 + 1 = 64 + 1 = 65 \text{ time units}.$$

**Derivation 2: switching overhead fraction.**

$$f_{\mathrm{sw}} = \frac{64}{65} = 0.9846153846\ldots$$

Under the assumed parameters, $100 \times f_{\mathrm{sw}} = 98.4615\ldots\%$ of the stored-program machine's per-operation time is switching overhead.

**Derivation 3: re-entry cost per operation.**

$$c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}} = 4 + 1 = 5 \text{ time units}.$$

**Derivation 4: re-entry overhead fraction.**

$$f_{\mathrm{re}} = \frac{1}{5} = 0.2000.$$

**Derivation 5: total-time comparison for $N_{\mathrm{op}} = 10^{6}$ operations.**

$$T_{\mathrm{sw}} = 10^{6} \times 65 = 6.5 \times 10^{7} \text{ time units},$$
$$T_{\mathrm{re}} = 10^{6} \times 5 = 5.0 \times 10^{6} \text{ time units}.$$

The ratio is

$$\frac{T_{\mathrm{sw}}}{T_{\mathrm{re}}} = \frac{65}{5} = 13.0.$$

**Derivation 6: the break-even memory time.** The re-entry model wins when $c_{\mathrm{re}} < c_{\mathrm{sw}}$. Solve for the memory time $t_{\mathrm{mem}}$ at equality, holding the other assumed values fixed:

$$k_{\mathrm{acc}}\, t_{\mathrm{mem}}^{*} = t_{\mathrm{dyn}} + t_{\mathrm{re}} - t_{\mathrm{alu}} = 4 + 1 - 1 = 4,$$
$$t_{\mathrm{mem}}^{*} = \frac{4}{4} = 1 \text{ time unit}.$$

So under these assumptions the re-entry model wins whenever $t_{\mathrm{mem}} > 1$ time unit, i.e. whenever memory is slower than the arithmetic unit at all.

**Derivation 7: sensitivity of the verdict to $t_{\mathrm{re}}$.** The comparison flips when the re-entry overhead grows. Setting $c_{\mathrm{re}} = c_{\mathrm{sw}} = 65$ and solving for $t_{\mathrm{re}}$, holding $t_{\mathrm{dyn}} = 4$ fixed:

$$t_{\mathrm{re}}^{*} = c_{\mathrm{sw}} - t_{\mathrm{dyn}} = 65 - 4 = 61 \text{ time units}.$$

Thus the re-entry model tolerates a re-entry overhead up to $61$ time units before losing to the switching model at the assumed $t_{\mathrm{mem}} = 16$. Expressed relative to the useful segment time, this is

$$\frac{t_{\mathrm{re}}^{*}}{t_{\mathrm{dyn}}} = \frac{61}{4} = 15.25,$$

so the modeled verdict survives a re-entry overhead $15.25$ times the useful dynamical segment time. This margin is a property of the assumed $t_{\mathrm{mem}} = 16$; it shrinks linearly as caching reduces the effective memory time.

**Derivation 8: cache-aware break-even hit rate.** This derivation is new to this paper. Insert the two-level memory model of Section 3.3 into $c_{\mathrm{sw}}$, with the assumed cache access time $t_{\mathrm{hit}} = 0.5$ time units (an assumption, labeled: it represents a cache an order of magnitude faster than main memory under the paper's normalization $t_{\mathrm{alu}} = 1$). The effective memory time is

$$t_{\mathrm{mem}}^{\mathrm{eff}} = h \times 0.5 + (1 - h) \times 16 = 16 - 15.5\,h,$$

and the cache-aware switching cost is

$$c_{\mathrm{sw}}(h) = 4\,(16 - 15.5\,h) + 1 = 65 - 62\,h.$$

The break-even hit rate $h^{*}$ solves $c_{\mathrm{sw}}(h^{*}) = c_{\mathrm{re}} = 5$:

$$65 - 62\,h^{*} = 5 \quad\Longrightarrow\quad 62\,h^{*} = 60 \quad\Longrightarrow\quad h^{*} = \frac{60}{62} = \frac{30}{31} = 0.967741935\ldots$$

Equivalently, and this is the form quoted in the Abstract, break-even occurs when the effective memory time itself reaches the tie value $t_{\mathrm{mem}}^{\mathrm{eff}} = 1$ of Derivation 6:

$$16 - 15.5\,h^{*} = 1 \quad\Longrightarrow\quad 15.5\,h^{*} = 15 \quad\Longrightarrow\quad h^{*} = \frac{15}{15.5} = 0.967741935\ldots$$

Both routes agree, as they must, since $62 = 4 \times 15.5$ and $60 = 4 \times 15$. The reading is stark: with a cache access costing half a time unit, the re-entry advantage survives only while the cache hit rate stays below $h^{*} = 0.967741\ldots$, i.e. while at least $1 - h^{*} = 1/31 = 0.032258\ldots$ of accesses miss to main memory. A workload whose hit rate exceeds $96.77\%$ erases the modeled advantage entirely, and any further improvement in hit rate makes the switching model win. This is the quantitative form of the concern the prior analysis raised qualitatively when it noted that $t_{\mathrm{mem}}^{\mathrm{eff}} = 1$ ties the models [10].

**Derivation 9: cross-convention figure of merit.** The prior analysis reports the advantage under two conventions: the time-unit ratio $13.0$ of Derivation 5 and a cost-unit ratio $R = 3.125$ derived under a separate parameterization (Derivation 11 below) [10]. To combine them into one scale-free indicator we take the geometric mean, which is symmetric in the two conventions and penalizes their disagreement:

$$\mathrm{FOM} = \sqrt{13.0 \times 3.125} = \sqrt{40.625} = 6.373774\ldots \approx 6.3738.$$

Arithmetic check: $13.0 \times 3.125 = 40.625$; $6.37^{2} = 40.5769$ and $6.38^{2} = 40.7044$, so the root lies between $6.37$ and $6.38$, and $6.3738^{2} = 40.62533\ldots$ confirms the value to four decimals. The figure of merit is a model construct: it summarizes the two parameterizations in one number and would fall toward $1$ if the two conventions disagreed, but it carries no independent physical content beyond its inputs.

**Derivation 10: entropy bookkeeping quantity.** Following the logarithmic form of the entropy functionals discussed in [3] — where Shannon's uncertainty measure is $H = -K\sum_{i=1}^{n}p_i \log p_i$ and von Neumann's statistical-operator entropy arises from a logarithmic ratio argument — we compute the dimensionless quantity

$$\eta = \ln\!\left(\frac{t_{\mathrm{re}} + t_{\mathrm{dyn}}}{t_{\mathrm{dyn}}}\right) = \ln\!\left(\frac{5}{4}\right) = \ln(1.25) = 0.223143\ldots \approx 0.2231.$$

This is a model construct, not a thermodynamic entropy measurement; its interpretation is deferred to Section 6.

**Derivation 11: alternative parameterization in cost units.** As a robustness check under a different convention, one may price switching in abstract cost units (cu), one per elementary act of redirecting state, in the spirit of the per-slot scheduling acts of the BvN switching literature [1]. With fetch $c_f = 1.0$, decode $c_d = 0.5$, execute $c_e = 1.0$ (all assumed):

$$C_{\mathrm{vN}} = c_f + c_d + c_e = 1.0 + 0.5 + 1.0 = 2.5\ \mathrm{cu}.$$

With a re-entry loop of $L = 4$ nodes and per-pass cost $c_p = 0.2\ \mathrm{cu}$ (assumed):

$$C_{\mathrm{re}} = L\,c_p = 4 \times 0.2 = 0.8\ \mathrm{cu}, \qquad R = \frac{2.5}{0.8} = 3.125.$$

Amortizing a setup cost $C_s = 10\ \mathrm{cu}$ over $n$ cycles of reuse, $C_{\mathrm{re}}(n) = 10/n + 0.8$; break-even solves $10/n + 0.8 = 2.5$, giving $10/n = 1.7$ and

$$n^{*} = \frac{10}{1.7} = 5.882352\ldots,$$

i.e. at least $6$ whole cycles of reuse. The advantage vanishes when $L\,c_p^{*} = C_{\mathrm{vN}}$, i.e. $c_p^{*} = 2.5/4 = 0.625\ \mathrm{cu}$, or equivalently at loop length $L^{*} = 2.5/0.2 = 12.5$ nodes for $c_p = 0.2$. These numbers follow a different cost convention than Derivations 1 through 10 and are reported separately; they enter this paper's headline only through the figure of merit of Derivation 9.

**Derivation 12: overhead-fraction crossover in $r = t_{\mathrm{mem}}/t_{\mathrm{alu}}$.** With $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$, and $t_{\mathrm{mem}} = r$, the switching overhead fraction is $f_{\mathrm{sw}}(r) = 4r/(4r+1)$ and the re-entry fraction is constant at $f_{\mathrm{re}} = 1/5 = 0.2$. Sample values: at $r = 4$, $f_{\mathrm{sw}} = 16/17 = 0.941176\ldots$; at $r = 16$, $f_{\mathrm{sw}} = 64/65 = 0.984615\ldots$, matching Derivation 2; at $r = 1$, $f_{\mathrm{sw}} = 4/5 = 0.8$. The fractions are equal when

$$\frac{4r}{4r+1} = \frac{1}{5} \quad\Longrightarrow\quad 20r = 4r + 1 \quad\Longrightarrow\quad 16r = 1 \quad\Longrightarrow\quad r = \frac{1}{16} = 0.0625.$$

For every $r > 0.0625$ the switching machine wastes a larger fraction of its per-operation time on overhead than the re-entry machine does under these assumptions.

## 5. Results

All results below are projections of the cost model of Section 3 under the assumptions of Section 4; none are empirical measurements. Each result cites the derivation that produces it.

- **R1 (per-operation costs).** Under the assumed parameters ($k_{\mathrm{acc}} = 4$, $t_{\mathrm{mem}} = 16$, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$): $c_{\mathrm{sw}} = 65$ time units, $c_{\mathrm{re}} = 5$ time units (Derivations 1, 3).
- **R2 (overhead fractions).** $f_{\mathrm{sw}} = 64/65 = 0.984615\ldots$; $f_{\mathrm{re}} = 0.2000$ (Derivations 2, 4).
- **R3 (total-time ratio).** For $N_{\mathrm{op}} = 10^{6}$: $T_{\mathrm{sw}} = 6.5 \times 10^{7}$, $T_{\mathrm{re}} = 5.0 \times 10^{6}$, ratio $13.0$ (Derivation 5).
- **R4 (break-even memory time).** The re-entry model wins whenever $t_{\mathrm{mem}} > t_{\mathrm{mem}}^{*} = 1$ time unit, under the fixed assumptions (Derivation 6).
- **R5 (robustness to re-entry overhead).** The verdict is unchanged for any $t_{\mathrm{re}} < t_{\mathrm{re}}^{*} = 61$ time units, i.e. up to $15.25$ times the useful segment time (Derivation 7).
- **R6 (cache-aware break-even).** With $t_{\mathrm{hit}} = 0.5$ time units, the advantage survives only for cache hit rates $h < h^{*} = 15/15.5 = 0.967741\ldots$; equivalently, the advantage requires at least a $1/31 = 0.032258\ldots$ miss rate to main memory (Derivation 8). This is the binding constraint on the headline result.
- **R7 (cross-convention figure of merit).** $\mathrm{FOM} = \sqrt{13.0 \times 3.125} = 6.3738\ldots$ (Derivation 9).
- **R8 (bookkeeping ratio).** $\eta = \ln(5/4) = 0.2231\ldots$, a dimensionless model quantity (Derivation 10).
- **R9 (alternative parameterization).** Under the cost-unit convention of Derivation 11: $C_{\mathrm{vN}} = 2.5\ \mathrm{cu}$, $C_{\mathrm{re}} = 0.8\ \mathrm{cu}$, ratio $R = 3.125$; break-even reuse $n^{*} = 5.882\ldots$ cycles; advantage thresholds $c_p^{*} = 0.625\ \mathrm{cu}$ and $L^{*} = 12.5$ nodes.
- **R10 (fraction crossover).** The switching machine's overhead fraction exceeds the re-entry machine's for all $r > 1/16 = 0.0625$; at $r = 16$ the fractions are $64/65 = 0.984615\ldots$ versus $0.2000$ (Derivation 12).

The qualitative reading, convergent across both parameterizations: in a memory-bound regime the stored-program organization spends nearly all of its per-operation time switching, and the re-entry organization wins by a large modeled margin and tolerates a wide range of re-entry overheads before the verdict reverses. The strength of this conclusion is conditional on the assumed parameters, and R6 identifies the single assumption — uncached, serialized memory — whose relaxation most directly attacks it.

## 6. Discussion

**What the comparison does and does not show.** The models compare switching effort per logical operation, not total system cost, accuracy, programmability, or verification cost. The ratio $13.0$ is a property of the assumed parameters, not of the architectures; its role is to isolate the parameters — $t_{\mathrm{mem}}^{\mathrm{eff}}$, $t_{\mathrm{re}}$, and in the alternative convention $c_p$, $L$, and $n$ — on which the re-entry proposal's economic case turns.

**The cache constraint is the first-order limitation.** Assumption (A2) in its baseline form — serialized, uncached memory — is the case most favorable to the re-entry verdict, and Derivation 8 quantifies exactly how favorable. Real hierarchies cache instructions and data aggressively; for regular workloads, hit rates at or above the break-even value $h^{*} = 0.967741\ldots$ are plausible, and at such hit rates the models tie or the switching model wins. The prior analysis already flagged the tie point $t_{\mathrm{mem}}^{\mathrm{eff}} = 1$ [10]; the new contribution here is the translation of that tie point into a hit-rate threshold under an explicit two-level model. The headline ratio of $13.0$ therefore holds only in the memory-bound regime and is not a general claim. A second, unmodeled effect pushes in the same direction: real fetch-decode-execute pipelines amortize fetch across superscalar issue, so the effective $c_{\mathrm{sw}}$ per operation can fall below the modeled value even at fixed hit rate.

**The re-entry overhead is assumed, not derived.** Assumption (A3) is the deepest physical limitation. We took $t_{\mathrm{re}} = 1$ time unit as an illustrative value; deriving it requires the long-time statistics of the loop's dynamical cocycle. The multiplicative ergodic theorem for von Neumann-algebra-valued cocycles shows that Lyapunov-type limit operators exist almost everywhere under a first-moment condition on the cocycle, and that in the finite-dimensional setting the limit operator $\Lambda(x) = \lim_{n \to \infty}[c(n,x)^{*}c(n,x)]^{1/2n}$ yields invariant exponents, while the proof technique requires uniform boundedness of the cocycle and delivers its conclusions via the pointwise ergodic theorem [5]. A physical re-entry loop would have to be verified against exactly such moment and boundedness conditions before a mean re-entry time $t_{\mathrm{re}}$ could be asserted. The robustness result R5 ($t_{\mathrm{re}}$ may reach $61$ time units) is generous within the model, but it is a projection, not evidence about real Hamiltonian devices.

**Averaging to a steady behavior is a spectral hypothesis.** The model treats $N_{\mathrm{op}}$ re-entries as statistically interchangeable, which presumes that repeated passes average to a well-defined steady behavior. The spectral theory of semigroups of positive maps on von Neumann algebras shows this is not automatic: for an ergodic semigroup of linear normal positive unital maps, eigenvectors are multiples of a partial isometry, linear combinations of two partial isometries, or multiples of a unitary operator, and mere positivity of the maps is not sufficient for the Frobenius theory that holds for completely positive maps, under which the point spectrum forms a group with one-dimensional eigenspaces spanned by unitaries [8]. If the per-pass evolution is merely positive rather than completely positive, eigenspaces of dimension greater than one can occur, and the fixed-point space $M_1$ need not consist of multiples of the identity. The assumption that repeated re-entries average cleanly is therefore a spectral hypothesis the model does not discharge.

**Verification may be structurally hard.** Certifying that a candidate Hamiltonian loop behaves as modeled is an approximation problem of microstate type. In the tracial von Neumann algebra setting, self-tracial stability holds if and only if the algebra is amenable, under the Connes Embedding Problem, where amenability means every derivation is inner and hyperfiniteness means expression as the $\sigma$-weak closure of an increasing union of finite-dimensional subalgebras [7]. Amenability is a strong hypothesis not guaranteed for physical loop dynamics, so the certification step the re-entry program needs is not a formality. A complementary structural restriction comes from rigidity: for torsion-free non-amenable hyperbolic groups, every invariant von Neumann subalgebra of $L(\Gamma)$ has the form $L(\Lambda)$ for a normal subgroup $\Lambda$ [9], which indicates that the observable sub-dynamics an observer can isolate inside a large dynamical system can be severely constrained — and only isolable sub-dynamics can serve as definable re-entry loops.

**Loop structure resists the standard algebraic toolkit.** If a re-entry computation's transition structure is modeled as an algebra over its loop graph, the regularity literature is a caution: Leavitt path algebras are von Neumann regular if and only if the defining graph is acyclic, and group rings are regular only under restrictive conditions (the group locally finite, finite-subgroup orders invertible), so regularity is a rare feature precisely where cycles exist [6]. The re-entry loop is a cycle; loop-containing computations therefore lack the flat-module algebraic regularity that acyclic (feed-forward, straight-line) computations enjoy, and techniques that depend on it do not transfer.

**Approximate certification can mislead.** Any attempt to certify a loop's cost or structure by a cheap spectral surrogate faces the topology-dependence demonstrated for graph entropies: experiments on path graphs, small-world random graphs, and real-world networks showed that the Laplacian and normalized Laplacian entropies capture related yet different structural patterns, that quadratic approximations fail to explain non-trivial structures for the Laplacian case, and that the quality of approximation depends on graph topology [4]. A re-entry structure is a graph of dynamical transitions, so an approximate entropy-style certification of it inherits exactly this failure mode.

**Readout, control, and entropy bookkeeping are unpriced.** The re-entry model charges no cost for reading results out of the dynamical core or for error handling; any classical control layer added for these purposes reintroduces controller-like switching costs of the kind the comparison is meant to avoid. The bookkeeping quantity $\eta = \ln(5/4) \approx 0.2231$ of Derivation 10 is a dimensionless model construct in the logarithmic currency that the entropy tradition makes meaningful — von Neumann associated an entropy to a statistical operator by a gedanken experiment on the ground of phenomenological thermodynamics, and Shannon's $H = -K\sum_{i=1}^{n}p_i \log p_i$ is the unique uncertainty measure satisfying three reasonable requirements [3] — but connecting $\eta$ to a genuine entropy production remains open.

**Failure modes.** If re-entry loops must be re-initialized every few cycles (small effective reuse), the amortization result of Derivation 11 flips the sign of the comparison: below $n^{*} = 5.882\ldots$ cycles of reuse, the explicit controller wins in the cost-unit convention. If the per-pass cost scales with system size (for example $c_p \propto L$ rather than constant), then $C_{\mathrm{re}} \propto L^{2}$ and the advantage disappears for any nontrivial loop. If the hit rate of the workload exceeds $h^{*} = 0.967741\ldots$, the time-convention advantage vanishes outright.

**What would falsify the claims.** The central claim — that re-entry can undercut von Neumann switching cost in the modeled regime — is falsified within the model if any one of three measurements lands adversely: (i) an effective cache hit rate at or above $h^{*} = 15/15.5 = 0.967741\ldots$ for the target workload with $t_{\mathrm{hit}} = 0.5$ time units, which ties or reverses the time-convention verdict (Derivation 8); (ii) a measured per-pass cost $c_p > 0.625\ \mathrm{cu}$ or a sustained reuse factor below $n^{*} = 5.882\ldots$ in the cost-unit convention (Derivation 11); (iii) a measured re-entry overhead $t_{\mathrm{re}} \geq 61$ time units at $t_{\mathrm{mem}} = 16$ (Derivation 7). It is falsified at the level of the framework if the cocycle of a concrete loop fails the moment or boundedness conditions under which a stable mean re-entry time exists [5], since the cost model's basic quantity $t_{\mathrm{re}}$ would then be undefined.

**Limitations list.** The result rests on the following assumptions, with sensitivity noted for each: (A1) identical logical work in both machines — the comparison is void if the re-entry loop performs a different computation per pass; the ratio scales linearly in any deviation. (A2) baseline serialized uncached memory — the most sensitive assumption; a hit-rate rise from $0$ to $h^{*} = 0.967741\ldots$ at $t_{\mathrm{hit}} = 0.5$ removes the entire $13.0$ margin (Derivation 8). (A3) fixed assumed $t_{\mathrm{re}} = 1$ — insensitive up to $61$ time units (Derivation 7), but no derivation bounds it from above in a real device. (A4) existence and stability of the mean re-entry time — unverified; failure is total, not partial [5]. (A5) all parameter values are illustrative — no number in the paper is a measurement, so the absolute values of every result inherit the status of their inputs. (A6) the cost-unit convention of Derivation 11 uses independently assumed values ($c_f$, $c_d$, $c_e$, $c_p$, $L$, $C_s$); its agreement with the time convention is qualitative, and the figure of merit of Derivation 9 inherits both conventions' assumptions.

**Open questions.** (i) Can $t_{\mathrm{re}}$ be derived from the ergodic theory of the loop cocycle under hypotheses a physical device can be verified against [5]? (ii) Does the per-pass evolution of a concrete loop satisfy the complete-positivity-like conditions under which clean averaging holds, or only mere positivity, where the Frobenius picture fails [8]? (iii) Is the certification of a loop's microstate-type approximation properties achievable for non-amenable dynamics [7]? (iv) Which re-entry loops are even definable as separate computations inside a given system algebra, given the rigidity of invariant subalgebras in negatively curved settings [9]? (v) Can the vicious-circle lock-in described by Backus — languages as isomorphic copies of the von Neumann machine [2] — be broken by a cost advantage of the modeled size, or does the lock-in dominate the economics?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are researchers proposing non-von Neumann substrates — dynamical-systems, neuromorphic, and related groups — and the reviewers and funders who evaluate them. For this group the result changes the form of the debate: instead of a qualitative argument about whether Hamiltonian re-entry "avoids the von Neumann bottleneck" in the sense of Backus's limited CPU-memory throughput and the intellectual bottleneck of planning word traffic through it [2], the claim reduces to four measurable quantities: the effective memory time $t_{\mathrm{mem}}^{\mathrm{eff}}$ (or equivalently the hit rate $h$ against the threshold $h^{*} = 0.967741\ldots$), the re-entry overhead $t_{\mathrm{re}}$ against the threshold $61$ time units, the per-pass cost $c_p$ against $0.625\ \mathrm{cu}$, and the reuse factor $n$ against $5.882\ldots$ cycles. A proposal that states its position on these four numbers can be accepted or rejected by measurement; one that does not cannot be evaluated at all. No commercial or deployment user can be named at this stage, and none should be: the work is foundational, supplying a parameter vocabulary rather than a device.

**(b) Readiness level.** Against the NASA Technology Readiness Level definitions, this work is TRL 1–2: it is purely analytical, has not been peer reviewed, and describes basic principles and a cost-model framework with no experimental validation of any parameter in a physical substrate. Analytical work of this kind cannot exceed TRL 3, and nothing here approaches it: no concept has been formulated to the point of a proof-of-concept demonstration, and no application scenario has been validated even in simulation on a concrete substrate.

**(c) The smallest next test.** The cheapest de-risking calculation is a workload hit-rate audit: take the workload class a re-entry proposal claims to accelerate, measure or simulate its cache miss rate on a conventional machine, and compare against $h^{*} = 15/15.5 = 0.967741\ldots$ at the assumed $t_{\mathrm{hit}} = 0.5$. If the miss rate falls at or below $1/31 = 0.032258\ldots$, the time-convention advantage is refuted for that workload class and the proposal must rest on the cost-unit convention instead. The smallest physical experiment beyond that is a single-loop demonstration in an analog or quantum-dynamical substrate in which three quantities are measured: the per-pass traversal time (estimating $t_{\mathrm{dyn}}$), the per-pass steering overhead (estimating $t_{\mathrm{re}}$), and the number of consecutive passes before re-initialization (estimating $n$). The outcome that refutes the framework is a reuse factor that does not stabilize across runs — the signature of a cocycle without a stable mean re-entry time in the sense of [5] — or a measured $t_{\mathrm{re}}$ exceeding $61$ time units in the paper's normalization.

**(d) Binding constraints.** In the order they would bind: first, memory hierarchy performance, since the entire time-convention margin lives between the assumed $t_{\mathrm{mem}} = 16$ and the tie at $t_{\mathrm{mem}}^{\mathrm{eff}} = 1$ (Derivations 6 and 8); second, control and readout coupling, because any classical layer reintroduces per-operation switching costs the model excludes, and the model prices none of it; third, verification data, since certifying a loop's long-time statistics requires the moment and boundedness evidence of the cocycle framework [5] and, for approximate certification, must avoid the topology-dependent failure of cheap spectral surrogates shown for graph entropies [4]; fourth, definability of the loop as an isolable sub-dynamics, which the rigidity results of [9] show can be severely constrained. Component supply, fabrication tolerances, and regulation do not bind at this stage and are listed as open questions rather than constraints, because no physical implementation concept exists yet from which they could be derived.

**(e) Order-of-magnitude bounds (projections).** Two bounds follow from derivations in Section 4 and are labeled projections with their assumptions. First, the admissible re-entry overhead budget is at most $t_{\mathrm{re}}^{*} = 61$ time units against a useful segment time of $t_{\mathrm{dyn}} = 4$, i.e. a steering-to-useful ratio below $15.25$, and this budget shrinks linearly with the effective memory time: at hit rate $h$, the budget is $c_{\mathrm{sw}}(h) - t_{\mathrm{dyn}} = (65 - 62h) - 4 = 61 - 62h$ time units, which reaches zero at $h = 61/62 = 0.983870\ldots$. Second, in the cost-unit convention, the per-pass cost must stay below $c_p^{*} = 0.625\ \mathrm{cu}$ for a four-node loop, and the setup cost must amortize over at least $n^{*} = 5.882\ldots$ cycles; both scale linearly in the assumed $C_{\mathrm{vN}} = 2.5\ \mathrm{cu}$. No energy, monetary, or market figures are derivable from the model and none are claimed.

**(f) Risks and misuse paths.** The main misuse is rhetorical: the ratio $13.0$ and the figure of merit $6.3738\ldots$ could be quoted without the memory-bound condition and the assumed parameters, presenting a parameter-dependent projection as an architecture-level result. A secondary risk is premature certification: declaring a loop validated on the basis of an approximate spectral surrogate whose topology-dependent failure is documented in the graph-entropy experiments [4]. Both risks are mitigated by the falsification criteria of Section 6, which are stated so that a single adverse measurement settles the question.

## 8. Conclusion

This paper re-derives, with fully shown arithmetic, the two-model switching-cost comparison between stored-program execution and Hamiltonian re-entry computation, and extends it in two directions the prior analysis left open [10]. Under the declared memory-bound assumptions ($k_{\mathrm{acc}} = 4$, $t_{\mathrm{mem}} = 16$, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$), the stored-program organization pays $c_{\mathrm{sw}} = 65$ time units per operation against $c_{\mathrm{re}} = 5$, a ratio of $13.0$, with $98.4615\ldots\%$ of its per-operation time spent on switching; the verdict tolerates re-entry overheads up to $61$ time units, $15.25$ times the useful segment time. The new cache-aware derivation converts the comparison's weakest assumption into a number: with a cache access costing $0.5$ time units, the advantage survives only below a hit rate of $h^{*} = 15/15.5 = 0.967741\ldots$, and a cross-convention figure of merit $\sqrt{13.0 \times 3.125} = 6.3738\ldots$ summarizes both parameterizations. The comparison is bounded by conditions the mathematical literature makes precise: the existence of a stable mean re-entry time requires ergodic-theoretic hypotheses on the loop cocycle [5], clean averaging over repeated passes is a spectral hypothesis that mere positivity does not guarantee [8], certification is an approximation problem whose stability collapses to amenability [7], and the loop's algebraic fingerprint — a cycle — is exactly where regularity fails [6]. The value of the exercise is that it converts a qualitative architecture debate into four measurable quantities with stated thresholds, so that a single adverse measurement — a hit rate at or above $0.967741\ldots$, a per-pass cost above $0.625\ \mathrm{cu}$, a reuse factor below $5.882\ldots$, or an unstable mean re-entry time — settles the re-entry proposal's economic case in the regime that matters.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 19 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Birkhoff-von-Neumann Switches with Deflection-Compensated Mechanism. arXiv:1308.4280v1. https://arxiv.org/abs/1308.4280v1
[2] On the notion of "von Neumann vicious circle" coined by John Backus. arXiv:1602.02715v2. https://arxiv.org/abs/1602.02715v2
[3] Entropy, von Neumann and the von Neumann entropy. arXiv:math-ph/0102013v1. https://arxiv.org/abs/math-ph/0102013v1
[4] On the Von Neumann Entropy of Graphs. arXiv:1809.07533v1. https://arxiv.org/abs/1809.07533v1
[5] A multiplicative ergodic theorem for von Neumann algebra valued cocycles. arXiv:2006.13293v2. https://arxiv.org/abs/2006.13293v2
[6] On von Neumann regularity of ample groupoid algebras. arXiv:2401.03308v3. https://arxiv.org/abs/2401.03308v3
[7] On ultraproduct embeddings and amenability for tracial von Neumann algebras. arXiv:1907.03359v3. https://arxiv.org/abs/1907.03359v3
[8] The eigenvectors of semigroups of positive maps on von Neumann algebras. arXiv:0911.4434v1. https://arxiv.org/abs/0911.4434v1
[9] On invariant von Neumann subalgebras rigidity property. arXiv:2205.10700v3. https://arxiv.org/abs/2205.10700v3
[10] QNFO: Re-Entry Dynamics as a Switching Process: Comparing Hamiltonian Re-Entry Computation to von Neumann Switching Costs
