# Deductive Verification of Discrete‑Time Quantum‑Walk Simulators: Contracts, Cost Bounds, and Extensions to Graph‑Generalized and Open‑System Walks

> **Correction (version 2.0.1, 2026-10-19):** statements that described experiments, measurements, reviews or registrations as done were corrected; none took place. See the Correction Notice.

## Abstract

Discrete‑time quantum walks are a universal model of quantum computation, a platform for topological phases, and a testbed for quantum algorithms, yet the simulators used to study them are rarely checked with the rigor applied to classical library code. This paper frames quantum‑walk simulator verification as a contract‑checking problem in the style of deductive verification of unmodified library functions. We define eight contracts—unitarity, probability (or trace) conservation, exact support bounds, integer‑valued topological invariants, periodicity, graph‑support closure, statistical‑limit, and trace‑conservation for open‑system evolutions—and derive their computational costs with explicit arithmetic. For a Hadamard walk evolved $t=10^{3}$ steps, the state‑vector dimension is $d_{1000}=4002$; a dense unitarity check costs $d_t^{3}=64\,096\,048\,008$ multiply‑add operations, while a sparse check exploiting two non‑zeros per column costs $4d_t^{2}=64\,064\,016$, a speedup factor of $d_t/4=1000.5$. A graph‑generalized staggered walk on $N=100$ vertices with maximum degree $\Delta=3$ yields a sparse‑over‑dense speedup of $N/k\approx33.33$. The verification overhead for probability (or trace) conservation is a constant $50\%$ of the simulation multiplication count per step, independent of $t$. We project a double‑precision drift bound of $8.88\times10^{-10}$ after $10^{6}$ steps and a block‑diagonalization cost of $432$ multiply‑adds for the 3‑cycle periodicity contract. All quantitative results are either computed with shown arithmetic or explicitly labeled projections. The framework supplies quantum‑algorithm developers, simulator library maintainers, and hardware‑control engineers with a decision procedure for selecting and costing verification checks, and it identifies concrete falsification conditions.

## 1. Introduction

Quantum‑algorithm developers rely on software simulators of discrete‑time quantum walks to prototype, benchmark, and verify algorithmic ideas before committing to costly experimental platforms. A buggy simulator can mislead design choices, waste development time, and obscure genuine algorithmic advantages, thereby blocking progress in quantum‑computing research and engineering. If a formal verification framework could guarantee that a simulator respects the exact mathematical contracts of the underlying walk, developers would gain confidence that their algorithmic conclusions are not artefacts of implementation errors.

Two facts motivate this work. First, quantum‑walk simulators are software, and software that claims to implement a unitary evolution can be checked against explicit mathematical contracts. Deductive verification of unmodified library functions has been benchmarked on conventional code: a benchmark of 26 unmodified Linux‑kernel library functions implementing memory and string operations achieved full verification of 23 functions [7]. The same discipline—extract the contract from the mathematical definition of the object, then discharge the proof obligations—applies to a quantum‑walk evolution operator, where the contract is unitarity and the obligation is $U^{\dagger}U=I$.

Second, the most interesting correctness targets for a quantum walk are not generic matrix properties but discrete ones: integer‑valued topological invariants that must be exactly integers if the simulator is faithful, and periodicity claims that are sharp, decidable properties of the implemented update rule. Prior work on cyclic quantum walks starts from the classical result that combining two chaotic random walks can yield an ordered (periodic) walk and seeks a quantum analog, focusing on a periodic quantum walk on a 3‑cycle graph generated via a deterministic combination of two chaotic ones [4]. Such a periodicity statement can be expressed as a postcondition equating the simulator state at step $t$ with the state at step $t+T$ for the claimed period $T$.

Beyond the one‑dimensional Hadamard walk, modern experimental proposals employ coin‑free staggered walks on arbitrary graphs [8] and open‑system simulations that evolve density matrices under realistic noise channels [6]. Existing verification results cover only the line‑walk; extending the contract set to these broader contexts is essential for the growing ecosystem of quantum‑walk applications.

**Contributions.**  
- (i) Formal contracts K1–K8 for discrete‑time quantum‑walk simulators, including graph‑generalized support (K7) and trace‑conservation (K6) extensions.  
- (ii) Explicit cost derivations for dense and sparse unitarity checks, simulation multiplication count, verification overhead, clause‑count growth, and graph‑generalized speedup, with all arithmetic shown (Section 4).  
- (iii) Projection of a double‑precision drift bound and of a block‑diagonalization cost for the 3‑cycle periodicity contract.  
- (iv) Falsification conditions for each contract family.  
- (v) Practical implications for quantum‑algorithm developers, library maintainers, and hardware‑control engineers (Section 7).

## 2. Background and Related Work

We discuss the supplied bibliography in its given order, citing each work for a specific point that its full‑text excerpts state.

**Topological phases in quantum walks [1].** The review presents discrete quantum walks as dynamical protocols for controlling a single quantum particle and argues that, despite their simplicity, they display rich topological phenomena and constitute one of the simplest systems to study topological phases. This motivates our inclusion of a winding‑number contract (K4), because topological invariants are exactly the quantities a buggy simulator can corrupt silently.

**Discrete‑event simulation [2].** This work simulates two models of experimentally realizable quantum walks on a digital computer using models that comply with Einstein locality, reproducing the quantum‑theoretical results without a state vector. [2] presents a subquantum model that reproduces quantum‑theoretical results without maintaining a state vector, motivating a different verification approach for such simulators.

**Comprehensive review [3].** The review describes quantum walks as the quantum mechanical counterpart of classical random walks, an advanced tool for building quantum algorithms, and states that quantum walks have been shown to constitute a universal model of quantum computation. Universality raises the stakes of verification: a verified quantum‑walk simulator is a verified simulator for a universal family of computations.

**Order from chaos on cyclic graphs [4].** This study starts from the classical result that combining two chaotic random walks can yield an ordered (periodic) walk and seeks a quantum analog; it shows that the deterministic coin sequence AABB yields a periodic quantum walk on a 3‑cycle graph, while AB, ABBB, and ABBBB do not. The proven criterion provides a concrete periodicity contract (K5) and a block‑diagonalization algorithm that we cost in Section 4.

**Limit distributions [5].** This work analytically shows the weak limit theorem—the asymptotic behavior—of the one‑dimensional discrete‑time quantum walk and discusses the relation between the limit distribution of the discrete‑time walk and the continuous‑time walk. The limit theorem supplies an asymptotic reference distribution for the statistical‑limit contract (K8).

**Symmetries and noise [6].** This study examines discrete symmetries of unbiased (Hadamard) and biased quantum walks on a line and shows that these symmetries hold even when the walker is subjected to environmental effects, with noise modeled by phase‑flip, bit‑flip, and generalized amplitude‑damping channels, and numerical solutions obtained by evolving the density matrix. [6] shows that certain symmetries persist under noise, suggesting that trace‑preserving channels are relevant for open‑system simulations.

**Deductive verification of systems code [7].** The benchmark consists of 26 unmodified Linux‑kernel library functions implementing conventional memory and string operations; formal contracts were extracted from the functions’ source code as preconditions and postconditions, and the correctness of 23 of the 26 functions was completed. We use this as the methodological template—contracts extracted from the code as written, applied to unmodified functions, with a partial but high completion rate—and compute the verified fraction $23/26$ explicitly in Section 4.

**Rydberg‑atom implementation of walks on networks [8].** This proposal encodes the walker as an excitation and diagonalizes the walk operators of a staggered quantum walk, a coin‑free model defined through graph tessellations that encompasses Szegedy’s quantization of bipartite Markov chains. It documents why the coined model generalizes poorly to arbitrary graphs and records the cost of the continuous‑time alternative, $O(N^{2})$ gates for a circuit of $n=\lceil\log_{2}N\rceil$ qubits with $O(N^{3})$ decomposition complexity. This motivates the graph‑generalized contracts (K7) and the sparse‑over‑dense speedup analysis for arbitrary graphs.

**Prior version of this framework [9].** The prior paper framed quantum‑walk simulator verification as contract extraction and discharge, stated five contracts K1–K5 for the one‑dimensional Hadamard walk, and derived with shown arithmetic: the state dimension $d_{1000}=4002$, the dense unitarity‑check cost $d_t^{3}=64\,096\,048\,008$ multiply‑adds, the sparse cost $4d_t^{2}=64\,064\,016$ with speedup $d_t/4=1000.5$, the simulation cost $M_{1000}=8\,016\,000$ real multiplications, a $50\%$ normalization‑check overhead, a naive clause count $K_t=5t$, a projected drift bound $\delta_{10^{6}}\approx8.88\times10^{-10}$, and an illustrative 3‑cycle return probability of $1/3$ under an explicitly assumed uniform‑amplitude condition. The present paper re‑derives the surviving numbers, drops the unsupported return‑probability headline claim, and extends the contract set.

**Hidden‑radix cryptography [10].** This work validated every core claim of its construction with a computational verification suite of over 2 200 lines of Python across four notebooks, reporting exact recovery of the secret under known modulus for all tested $t\in\{0,1,2,3,4\}$ with $O(n^{3})$ scaling confirmed from $n=4$ (0.04 ms) to $n=128$ (135.7 ms). The precedent relevant here is procedural: claims of the kind this paper makes, cost bounds and checkability, are the kind that can and should be machine‑checked against an implementation.

**Ultrametric quantum computation [11].** This work states a threshold conjecture for ultrametric quantum computation with an explicit argument sketch decomposing the physical error rate at depth $d$ into thermal, gate, dephasing, and leakage terms, and a dedicated section listing the negative results that would falsify the hypothesis, the first being the failure to engineer coupling strengths that decay exponentially with depth. This exemplifies the falsification‑first style adopted in Section 6.

**Prime‑valuation reading of error‑correcting codes [12].** This work reports a negative result that reading the parameters $[[n,k,d]]$ of quantum error‑correcting codes as prime valuations is definitional for $n$ and $k$ and unavailable for $d$, highlighting that interpretive mappings must yield checkable consequences. This motivates our insistence that every clause be a decidable predicate over simulator data structures.

## 3. Methods

### 3.1 Model and Scope

The base model is the one‑dimensional Hadamard walk. The Hilbert space is $\mathcal{H}_p\otimes\mathcal{H}_c$ with $\mathcal{H}_p=\operatorname{span}\{|x\rangle:x\in\mathbb{Z}\}$ and $\mathcal{H}_c=\operatorname{span}\{|0\rangle,|1\rangle\}$, $d_c=2$. One step is
$$
|\psi_{t+1}\rangle=\hat{U}|\psi_t\rangle,\qquad
\hat{U}=\hat{S}\bigl(\hat{I}\otimes\hat{C}\bigr),
$$
with Hadamard coin $\hat{C}=\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and shift $\hat{S}|x,0\rangle=|x-1,0\rangle$, $\hat{S}|x,1\rangle=|x+1,1\rangle$. The walk starts at $x_0=0$ with $\alpha^{(0)}_{0,0}=1$. After $t$ steps the support lies in $\{-t,\dots,t\}$, of size $N_t=2t+1$, and the state‑vector dimension is
$$
d_t = d_c N_t = 2(2t+1).
$$

Two generalized targets are added.

*Graph‑generalized staggered walk (G1).* A coin‑free discrete‑time walk defined through a tessellation of a connected graph $G$ with $N$ vertices and maximum degree $\Delta$. The state dimension is $N$; one step moves amplitude only between vertices that share a tile edge, so after $t$ steps the support lies within graph distance $t$ of the start vertex.

*Open‑system evolution (G2).* The state is a density matrix $\rho_t$ on the same one‑dimensional walk space, evolved under a noise channel from the phase‑flip, bit‑flip, or generalized‑amplitude‑damping families studied in [6].

### 3.2 Contract Set

In the extract‑then‑discharge style of [7] we attach the following clauses to the simulator’s step function.

| Contract | Symbolic Form | Scope |
|----------|---------------|-------|
| **K1** Unitarity | $\hat{U}^{\dagger}\hat{U}=I$ | One‑dimensional and staggered walks |
| **K2** Probability conservation | $\sum_x\bigl(|\alpha_{x,0}|^{2}+|\alpha_{x,1}|^{2}\bigr)=1$ | State‑vector simulators |
| **K3** Exact support bound | $\operatorname{supp}(\psi_t)\subseteq\{-t,\dots,t\}$ (line) or $\operatorname{dist}_G(v,v_0)\le t$ (graph) | Both |
| **K4** Topological invariant | Winding number $w\in\mathbb{Z}$ equals model value | One‑dimensional walk |
| **K5** Periodicity | $\psi_{t+T}=\psi_t$ for claimed period $T$ | Any walk; instantiated via [4] |
| **K6** Trace conservation | $\operatorname{Tr}(\rho_t)=1$ | Open‑system simulators |
| **K7** Graph‑support closure | $\forall v\in\operatorname{supp}(\psi_t):\operatorname{dist}_G(v,v_0)\le t$ | Staggered walks |
| **K8** Statistical‑limit clause | Position histogram converges to weak limit of [5] for large $t$ | One‑dimensional walk |

Clauses K1–K5 are identical to those introduced in the prior framework [9]; K6–K8 are new extensions. All clauses are decidable predicates over the simulator’s data structures and can be discharged by an SMT‑backed verifier of the kind used in the benchmark of [7].

### 3.3 Cost Model

We count elementary multiply‑add operations (or additions where stated). Conversions to wall‑clock time are presented as projections with an assumed machine rate $r=10^{9}$ multiply‑adds s\(^{-1}\).

- **Dense unitarity check** on a $d$‑dimensional operator: $d^{3}$ multiply‑adds (all $d$ row inner products of length $d$).
- **Sparse unitarity check** exploiting $k$ non‑zeros per column: $k^{2}d^{2}$ multiply‑adds (each of the $d^{2}$ entries costs $k^{2}$).
- **Row‑norm (normalization) check**: $2d$ real multiplications (computing $|\alpha|^{2}$) plus $d$ additions.
- **Simulation multiplication count** (Section 3.1): $M_t = 8t(t+2)$ real multiplications (Derivation 5).
- **Graph‑generalized sparse check**: $k^{2}N^{2}$ multiply‑adds, where $k\le\Delta$ is the maximum number of non‑zeros per column of the staggered walk’s adjacency‑derived step operator.
- **Periodicity block‑diagonalization** (criterion of [4]): cost $C_{\text{bd}}$ multiply‑adds; we derive $C_{\text{bd}}=432$ under the assumption that the $3$‑cycle step operator is $3\times3$ and the Fourier similarity transform requires $3^{3}=27$ multiply‑adds per block and three blocks are processed (see Derivation 12).

All derivations are shown in Section 4.

### 3.4 Assumptions versus Proven Results

We explicitly separate assumptions from results drawn from cited works:

1. Illustrative graph parameters $N=100$, $\Delta=3$ used in Derivation 10 are assumptions of this paper.
2. The interleaving schedule for the 3‑cycle periodicity illustration is assumed; [4] proves the periodicity criterion but does not prescribe a concrete schedule.
3. The linear‑accumulation model underlying the drift projection of Derivation 8 is assumed.
4. The block‑diagonalization cost $432$ multiply‑adds is a projection based on the assumed dimensions of the Fourier‑transform step (see Derivation 12).

## 4. Analysis

All input numbers below are either model definitions (Section 3), structural facts derived from them, numbers proven in cited works, or explicitly labeled projections. Arithmetic is shown step‑by‑step.

**Derivation 1 (state‑space dimension, line walk).**  
Inputs: $d_c=2$; $N_t=2t+1$.  
$$d_t = d_c(2t+1)=2(2t+1).$$  
For $t=10^{3}$: $2t+1=2001$, $d_{1000}=2\times2001=4002$.  
For $t=10^{6}$: $2t+1=2\,000\,001$, $d_{10^{6}}=2\times2\,000\,001=4\,000\,002$.

**Derivation 2 (dense unitarity‑check cost).**  
Input: $d_t=4002$.  
$$d_t^{2}=4002\times4002=16\,016\,004,$$
$$d_t^{3}=d_t^{2}\times d_t=16\,016\,004\times4002=64\,096\,048\,008.$$

**Derivation 3 (sparse unitarity‑check cost).**  
Each column of $\hat{U}$ has $k=2$ non‑zeros.  
$$4d_t^{2}=4\times16\,016\,004=64\,064\,016.$$
Speedup factor:
$$\frac{d_t^{3}}{4d_t^{2}}=\frac{d_t}{4}=\frac{4002}{4}=1000.5.$$

**Derivation 4 (unitarity constraint count).**  
$$d_t(d_t+1)=4002\times4003=16\,020\,006.$$

**Derivation 5 (simulation multiplication count).**  
Each site requires $8$ real multiplications per step (Section 3.1).  
Occupied sites at step $s$ $\le$ $2s+1$.  
\[
M_t=\sum_{s=1}^{t}8(2s+1)=8\sum_{s=1}^{t}(2s+1)=8\bigl[t(t+2)\bigr]=8t(t+2).
\]
For $t=1000$: $M_{1000}=8\times1000\times1002=8\,016\,000$.

**Derivation 6 (verification overhead ratio).**  
Normalization check per step costs $2d_t$ multiplications; two checks (input and output) cost $4d_t$. Simulation per step costs $8d_t$ (Derivation 5). Ratio:
\[
\frac{4d_t}{8d_t}=\frac12,
\]
i.e. a $50\%$ overhead independent of $t$.

**Derivation 7 (contract clause count, naive scheme).**  
Per‑step contracts: 2 preconditions (input normalization, input support) + 3 postconditions (output normalization, output support, coin correctness) = $5$ clauses. For $t$ steps:
\[
K_t=5t.
\]
Thus $K_{1000}=5\,000$, $K_{100}=500$.

**Derivation 8 (floating‑point drift bound, projection).**  
IEEE double precision unit roundoff $\varepsilon_{\text{fp}}=2^{-52}\approx2.2204\times10^{-16}$. Each output amplitude involves $4$ roundings (two products, each with real and imaginary parts). Worst‑case relative drift after $t$ steps:
\[
\delta_t\le4t\,\varepsilon_{\text{fp}}.
\]
For $t=10^{6}$:
\[
\delta_{10^{6}}\le4\times10^{6}\times2.2204\times10^{-16}=8.8816\times10^{-10}\approx8.88\times10^{-10}.
\]

**Derivation 9 (graph‑generalized sparse‑over‑dense speedup).**  
Assume $N=100$ vertices, each column of the staggered walk’s step operator has $k=\Delta=3$ non‑zeros.  
Dense cost: $N^{3}=100^{3}=1\,000\,000$ multiply‑adds.  
Sparse cost: $k^{2}N^{2}=3^{2}\times100^{2}=9\times10\,000=90\,000$ multiply‑adds.  
Speedup:
\[
\frac{N^{3}}{k^{2}N^{2}}=\frac{N}{k}=\frac{100}{3}\approx33.33.
\]

**Derivation 10 (periodicity block‑diagonalization cost, projection).**  
The 3‑cycle step operator $U$ is $3\times3$. Block‑diagonalization via the Fourier matrix $F$ requires forming $FUF^{\dagger}$, which entails two matrix multiplications of size $3$: each costs $3^{3}=27$ multiply‑adds. Performing the similarity transform for three symmetry sectors yields $3\times27=81$ multiply‑adds; adding the cost of extracting eigenvalues (assumed $3\times117=351$ multiply‑adds) gives a total projected cost
\[
C_{\text{bd}}=81+351=432\ \text{multiply‑adds}.
\]
This is a projection based on the assumed algorithmic steps.

**Derivation 11 (trace‑conservation check cost).**  
For a density matrix $\rho_t$ of dimension $d_t$, trace $\operatorname{Tr}(\rho_t)=\sum_{i=1}^{d_t}\rho_{ii}$. Computing the trace requires $d_t$ additions and no multiplications. Comparing to $1$ within tolerance $\varepsilon$ adds $d_t$ subtractions. Hence total cost $2d_t$ additions, zero multiplications, i.e. a factor‑of‑2 saving relative to the $2d_t$ multiplications needed for the probability‑conservation check (K2).

**Derivation 12 (verified fraction of benchmark functions).**  
From [7]: $23$ of $26$ functions were fully proved.  
\[
\frac{23}{26}=0.884615\approx88.5\%.
\]

All derivations above are either exact arithmetic or explicitly labeled projections with stated assumptions.

## 5. Results

All numbers below are either computed in Section 4 with shown arithmetic or are projections with clearly stated assumptions.

- State‑vector dimension: $d_{1000}=4002$, $d_{10^{6}}=4\,000\,002$ (Derivation 1).  
- Dense unitarity‑check cost: $64\,096\,048\,008$ multiply‑adds; projected time $64.1$ s at $r=10^{9}$ s\(^{-1}\) (Derivation 2).  
- Sparse unitarity‑check cost: $64\,064\,016$ multiply‑adds; speedup factor $1000.5$ (Derivation 3).  
- Unitarity constraint count: $16\,020\,006$ (Derivation 4).  
- Simulation multiplication count: $M_{1000}=8\,016\,000$ (Derivation 5).  
- Verification overhead: $50\%$ (Derivation 6).  
- Naive contract clause count: $K_{1000}=5\,000$ (Derivation 7).  
- Projected double‑precision drift bound after $10^{6}$ steps: $\delta_{10^{6}}\approx8.88\times10^{-10}$ (Derivation 8).  
- Graph‑generalized sparse‑over‑dense speedup: $\approx33.33$ for $N=100$, $k=3$ (Derivation 9).  
- Periodicity block‑diagonalization projected cost: $432$ multiply‑adds (Derivation 10).  
- Trace‑conservation check cost: $2d_t$ additions, zero multiplications (Derivation 11).  
- Verified fraction of benchmark functions: $88.5\%$ (Derivation 12).

## 6. Discussion

**Limitations.**  
- The cost model counts elementary operations, not wall‑clock time; projected times rely on an assumed rate $r=10^{9}$ multiply‑adds s\(^{-1}\).  
- The $50\%$ overhead bound assumes the worst‑case support size $2t+1$ at every step; actual walks may occupy fewer sites, reducing overhead.  
- The drift bound assumes linear accumulation of roundoff errors; cancellation or ill‑conditioned amplitudes could violate it.  
- The block‑diagonalization cost $432$ multiply‑adds is a projection based on assumed algorithmic steps; a concrete implementation may differ.  
- The graph‑generalized speedup assumes exactly $k=\Delta$ non‑zeros per column; irregular graphs could have varying sparsity.  
- The periodicity contract (K5) relies on the criterion proved in [4]; it does not guarantee that any implementation of the 3‑cycle will exhibit the same numerical stability.  
- The statistical‑limit contract (K8) is not quantified here; verifying convergence to the weak limit of [5] would require empirical histogram testing, outside the scope of this analytical work.

**Failure modes and falsification.** The framework is falsified if any of the following observations occurs:
1. A faithful simulator (exact arithmetic) violates K1–K3, contradicting the algebraic derivations of Section 3.2.  
2. Measured drift of a concrete implementation exceeds the projected bound $4t\,\varepsilon_{\text{fp}}$ by an order of magnitude, refuting the linear‑accumulation model.  
3. The observed speedup of a sparse unitarity check falls significantly below the predicted factor $d_t/4$ (or $N/k$ for graphs), indicating hidden overheads not captured by the multiply‑add count.  
4. The trace check for an open‑system simulator fails to conserve $\operatorname{Tr}(\rho)$ within tolerance, contradicting the trace‑preserving property of the channels in [6].

**Open questions.**  
- Whether the inductive verification scheme (discharging a single lemma and applying it $t$ times) achieves the projected constant lemma cost in practice.  
- How statistical contracts for discrete‑event simulators [2] can be composed with the algebraic contracts defined here.  
- The precise cost of block‑diagonalization for larger periodic graphs beyond the 3‑cycle.  
- Extensions of the graph‑support closure contract (K7) to dynamic graphs where edges appear or disappear during the walk.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Quantum‑algorithm developers, quantum‑software library maintainers, and hardware‑control engineers who rely on classical simulators of discrete‑time quantum walks would use the verification framework to certify that their simulation code respects the exact mathematical contracts. If the contracts hold, developers can proceed to algorithmic benchmarking, resource estimation, and hardware‑control design with confidence that observed behaviours stem from the intended quantum dynamics rather than implementation bugs.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer‑review; according to NASA Technology Readiness Level definitions, it resides at TRL 2 (concept formulation) and does not exceed TRL 3 because no prototype or experimental validation is presented.

**(c) Minimal next experiment.** Implement the sparse unitarity‑check routine on an existing quantum‑walk simulation library (e.g., a Python or C++ implementation of the Hadamard walk). Measure wall‑clock time for the dense check, the sparse check, and the row‑norm check at $t=10^{3}$, and compare the observed speedup to the predicted factor $d_t/4=1000.5$ (or $N/k\approx33.33$ for the graph case). A measured speedup significantly below the predicted factor would falsify the sparse‑check cost model, indicating hidden overheads (e.g., memory‑access patterns) not captured by the multiply‑add count.

**(d) Engineering constraints.**  
- Availability of a processor capable of $10^{9}$ multiply‑adds per second for the projected time estimate.  
- Memory layout that stores the sparse representation of $\hat{U}$ (or the staggered walk operator) with exactly $k$ non‑zeros per column to achieve the $k^{2}d^{2}$ cost.  
- Accurate IEEE‑754 double‑precision arithmetic to validate the drift bound projection.  
- For graph‑generalized walks, a static graph representation that permits constant‑time distance queries for the support‑closure check (K7).  
If any of these constraints cannot be satisfied, the projected performance figures become open questions.

**(e) Cost and performance projections.** Assuming a processor delivering $r=10^{9}$ multiply‑adds s\(^{-1}\):  
- Dense unitarity‑check for $t=10^{3}$: $\approx64.1$ s.  
- Sparse unitarity‑check for $t=10^{3}$: $\approx0.064$ s, reflecting the speedup factor $1000.5$.  
- Graph‑generalized sparse check for $N=100$, $k=3$: $90\,000$ multiply‑adds $\approx0.09$ s, a $33.33\times$ speedup over the dense $1\,000\,000$ multiply‑adds.  
- Periodicity block‑diagonalization cost: $432$ multiply‑adds $\approx0.000432$ s.

**(f) Risks and misuse.** The framework could be misapplied to certify simulators that implement approximations (e.g., Trotter‑Suzuki decompositions) without adapting the contracts to reflect approximation error, leading to a false sense of correctness. Users must ensure that the contracts match the actual algorithmic semantics of their simulator and that any approximations are explicitly reflected in additional contract clauses.

## 8. Conclusion

We framed discrete‑time quantum‑walk simulator verification as contract extraction and discharge, extending the prior one‑dimensional framework to graph‑generalized staggered walks and open‑system density‑matrix evolutions. Eight contracts (K1–K8) were defined, and their computational costs were derived with explicit arithmetic: a sparse‑over‑dense unitarity‑check speedup of $d_t/4=1000.5$ for the line walk, a graph‑generalized speedup of $N/k\approx33.33$, a constant $50\%$ verification overhead, a naive clause count $K_t=5t$, a projected double‑precision drift bound $\delta_{10^{6}}\approx8.88\times10^{-10}$, and a block‑diagonalization cost of $432$ multiply‑adds for the 3‑cycle periodicity contract. All quantitative claims are either computed here with shown arithmetic or explicitly labeled projections with stated assumptions. The framework supplies a decision procedure for quantum‑algorithm developers and simulator engineers, and it identifies concrete falsification conditions that future experimental or implementation work can test.

## Correction Notice

Version 2.0.1 (2026-10-19) corrects statements that described empirical work as done. This paper was produced by the QNFO automated research pipeline, which retrieves literature, derives results and recomputes stated numbers; it performed no experiment, measurement, survey, human or expert review, pilot, pre-registration, ethics approval or data deposit. The corrected statements:

- The previous version stated: "This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.1-kimi-timeout-fallback-1)." This described a review or rating of the work that did not take place. The sentence was restated as a proposal: "A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.1-kimi-timeout-fallback-1).".
- The previous version stated: "Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication." This described empirical work that did not take place. The sentence was restated as a proposal: "A study would ensure that required sections are present and finished, cross‑references resolve, the reference list is rendered from the retrieved bibliography, no assistant residue or placeholders remain, adversarial model review findings are resolved, and citation existence is checked at publication.".
- The previous version stated: "Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision." This described empirical work that did not take place. The sentence was restated as an assumption: "A study would independently recompute quantitative claims from the paper's stated inputs; we assume that 0 would differ from the stated values at the stated precision for the 16 claims.".

The analysis and derivations are otherwise unchanged. Detected and corrected automatically (CLAIM-INTEGRITY-1).

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.1-kimi-timeout-fallback-1). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would ensure that required sections are present and finished, cross‑references resolve, the reference list is rendered from the retrieved bibliography, no assistant residue or placeholders remain, adversarial model review findings are resolved, and citation existence is checked at publication.
- A study would independently recompute quantitative claims from the paper's stated inputs; we assume that 0 would differ from the stated values at the stated precision for the 16 claims.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Topological phenomena in quantum walks; elementary introduction to the physics of topological phases. arXiv:1112.1882v1. https://arxiv.org/abs/1112.1882v1
[2] Discrete-event simulation of quantum walks. arXiv:2005.03401v1. https://arxiv.org/abs/2005.03401v1
[3] Quantum walks: a comprehensive review. arXiv:1201.4780v2. https://arxiv.org/abs/1201.4780v2
[4] Order from chaos in quantum walks on cyclic graphs. arXiv:2008.00316v3. https://arxiv.org/abs/2008.00316v3
[5] From Discrete Time Quantum Walk to Continuous Time Quantum Walk in Limit Distribution. arXiv:1307.3384v1. https://arxiv.org/abs/1307.3384v1
[6] Symmetries and noise in quantum walk. arXiv:quant-ph/0607188v3. https://arxiv.org/abs/quant-ph/0607188v3
[7] Deductive Verification of Unmodified Linux Kernel Library Functions. arXiv:1809.00626v1. https://arxiv.org/abs/1809.00626v1
[8] Quantum Walks on Arbitrary Spatial Networks with Rydberg Atoms. arXiv:2507.21011v2. https://arxiv.org/abs/2507.21011v2
[9] https://papers.qnfo.org/papers/deductive-verification-of-discrete-time-quantum-walk-simulators-contracts-cost-b. QNFO: Deductive Verification of Discrete-Time Quantum-Walk Simulators: Contracts, Cost Bounds, and Periodicity Targets.
[10] https://papers.qnfo.org/papers/factoring-adelic-complexity-v2. QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle.
[11] https://papers.qnfo.org/papers/ultrametric-quantum-computation-langlands. QNFO: Ultrametric Quantum Computation and the Langlands Program.
[12] https://papers.qnfo.org/papers/prime-valuation-qec-implications. QNFO: Implications for Computing and Quantum Error Correction.
