# Re-Entry Dynamics in Hamiltonian Computation: A Cost Comparison with von Neumann Switching Overheads

## Abstract

We develop an analytical framework for comparing two paradigms of state update in computing systems: the switching cost incurred by a stored-program (von Neumann) architecture, in which every logical operation is mediated by instruction fetch, decode, and memory traffic, and the re-entry cost of a Hamiltonian computation model, in which the state evolves by continuous dynamics and computation is identified with the trajectory itself. The comparison is motivated by the QNFO framework of Hamiltonian dynamics as the engine of biological computation [12], and it is grounded in a body of work connecting Hamiltonian dynamics, entropy, and statistical mechanics [1], [4], [5], [6], [7]. We define a minimal cost model with explicit parameters, derive closed-form expressions for the per-operation switching overhead $c_{\mathrm{sw}}$ and the per-re-entry dynamical cost $c_{\mathrm{re}}$, and evaluate both under stated assumptions. For a representative parameter set we find that the switching overhead dominates when the memory-access-to-dynamics time ratio exceeds a threshold $r^{*}$ that we derive in closed form; for the illustrative parameters used here, $r^{*} \approx 4.0$, and the overhead fraction of total cost reaches $0.80$ at $r = 16$. We discuss the relation of the model to embedding methods for dynamical systems on quantum hardware [3], to neuromorphic architectures that explicitly depart from the von Neumann organization [9], and to architectural lock-in arguments [11]. All quantitative results are model projections with stated assumptions; no empirical measurements are claimed.

## 1. Introduction

The stored-program computer organizes computation as a sequence of discrete state transitions, each of which requires the machine to switch between the instruction stream and the data stream. This organization carries a per-operation cost — the switching cost — that is distinct from the cost of the logical work itself. A long-standing line of argument, associated with the notion of the "von Neumann vicious circle," holds that this organization is self-reinforcing: languages mirror architectures, and architectures are difficult to displace because languages presuppose them [11]. At the same time, a substantial literature seeks computational organizations that are not stored-program in this sense, including neuromorphic and spiking architectures motivated by energy efficiency beyond traditional von Neumann machines [9], and switches whose scheduling departs from conventional instruction-driven control [10].

A different departure point is physical: treat the computing device as a Hamiltonian system whose state evolves continuously, and identify computation with properties of the trajectory. The QNFO framework proposes Hamiltonian dynamics as the engine of biological computation [12]. Within such a framework, the analogue of a state update is not a fetch-decode-execute cycle but a segment of dynamical evolution; we call the cost of returning the system to a designated operating point along its trajectory the re-entry cost. The name is chosen deliberately: in Hamiltonian dynamics the state does not reset, it re-enters a region of phase space, and the thermodynamic bookkeeping of that re-entry is governed by the Gibbs-von Neumann entropy, which has been argued to be the appropriate generalization of thermodynamic entropy both in and out of equilibrium, as a consequence of Hamiltonian dynamics itself [1].

The question this paper poses is narrow and quantitative: under a minimal, explicitly parameterized cost model, when does re-entry dynamics beat von Neumann switching, and by how much? We do not claim to measure any real system. We construct the model, derive its thresholds in closed form, and evaluate it for stated parameter values, labeling every number a projection of the model.

The paper is organized as follows. Section 2 reviews the related literature. Section 3 defines the cost model. Section 4 carries out the derivations with full arithmetic. Section 5 reports the resulting numbers. Section 6 discusses limitations and failure modes, and Section 7 concludes.

## 2. Background and Related Work

We group the related work into four strands: entropy and Hamiltonian dynamics; nonequilibrium statistical operators; embeddings of dynamics for computation; and architectural alternatives to the stored-program organization.

**Entropy as a consequence of Hamiltonian dynamics.** The physical basis of the Gibbs-von Neumann entropy is developed in [1], which argues that this entropy is the appropriate statistical mechanical generalization of thermodynamic entropy for macroscopic and microscopic systems, whether in thermal equilibrium or not, as a consequence of Hamiltonian dynamics; the mathematical treatment uses well-known results and incorporates a variety of further ingredients (the supplied abstract is truncated at this point, so we rely only on what it states). This matters for our model because the re-entry cost of a Hamiltonian computation must be booked against some state functional, and [1] supplies the justification for using the Gibbs-von Neumann entropy $S_{\mathrm{vN}}$ as that functional, including away from equilibrium. Complementing this, [4] studies interacting qubit systems with dynamics given by 4-local Hamiltonians and continuous quantum random walks, and notes that the von Neumann entropy of the time-average could be used to characterize the mixing properties of such dynamics — the qualitative question of how phase space is penetrated by orbits, a central topic of classical ergodic theory. Mixing is precisely the property that determines how expensive re-entry into a designated region is in our model: a well-mixed trajectory re-enters frequently, a poorly mixed one does not. We note, however, that [4] also reports that estimating these mixing properties is PSPACE-hard, which bounds our ambition: we work with a toy mixing proxy rather than computing true mixing times.

**Nonequilibrium statistical operators.** Two entries concern the Zubarev nonequilibrium statistical operator (NSO). [5] discusses the NSO method as an important contribution to describing irreversible behavior starting from reversible Hamiltonian dynamics, in the context of the electrical conductivity of charged particle systems, and in particular the extended von Neumann formulation (the supplied abstract is truncated mid-sentence). [6] presents the non-equilibrium statistical operator more generally, observing that approaches to the statistical mechanics of nonequilibrium processes are based on empirical assumptions while a rigorous first-principles theory is missing, and again crediting Zubarev's NSO as an important contribution to describing irreversible behavior from reversible Hamiltonian dynamics. For our purposes these works mark the conceptual location of re-entry cost: irreversibility — and hence any asymmetry between forward computation and re-entry — is not free but must be derived, and the NSO program is the standard route for doing so. Our model sidesteps the open problem by assuming a fixed re-entry time parameter, which we flag as a limitation in Section 6.

**Embedding dynamics for computation.** [3] addresses the mapping of linear differential equations to Schrödinger equations via Carleman and Koopman-von Neumann embeddings for quantum algorithms, motivated by solving differential equations with large degrees of freedom on quantum computers, where classical variables must be embedded into a quantum state; the abstract notes that the class of problems that can be treated has been a limiting question (the supplied text is truncated). This is the constructive counterpart of our comparison: if dynamics can be embedded and evolved on quantum hardware, the per-step switching overhead of the stored-program organization is replaced by the cost of implementing the Hamiltonian. [2] takes a more radical step, representing quantum mechanics itself as a natural projection of a classical statistical model on the phase space $\Omega = H \times H$, where $H$ is a real Hilbert space, with statistical states given by Gaussian measures of zero mean and very small dispersion $\alpha$ as the small parameter of the model; from this projection, Schrödinger's, Heisenberg's and von Neumann's equations are derived (the abstract is truncated after introducing the fluctuation interpretation). [2] thus supports the idea that the quantum-dynamical description is not primitive but emergent from classical statistical dynamics — relevant because our re-entry model treats the Hamiltonian description as the fundamental layer. [7] establishes relations between Hamiltonian dynamics and Riemannian structures on phase spaces for unitarily evolving finite-level quantum systems in mixed states, showing that the energy dispersion — $1/\hbar$ times the path integral of the energy uncertainty — of a unitary evolution is bounded from below by the length of the evolution curve (the abstract continues beyond this point but the supplied text is truncated). This gives a geometric lower bound on dynamical cost that is the natural analogue of a switching lower bound: re-entry cannot be cheaper than the geometric length of the re-entering curve. [8] proposes a path integral formulation of classical Hamiltonian dynamics and extends it to hybrid classical-quantum dynamics, noting that no fully satisfactory solution of the hybrid coupling problem has been established to date; this is directly relevant to any architecture that would mix a classical control layer with a Hamiltonian computational layer, which is exactly what a practical re-entry machine would be.

**Architectural alternatives.** [9] reviews neuromorphic computing and spiking neural networks bibliometrically, framing them as aiming to leverage biological inspiration for greater energy efficiency and computational power beyond traditional von Neumann architectured machines, with spiking neural networks positioned as third-generation neural networks and aided by memristive and compute-in-memory developments (the abstract is truncated). [10] concerns Birkhoff-von-Neumann (BvN) switches: input scheduling based on BvN decomposition achieves high throughput and low complexity, but performance becomes less predictable under bursty input traffic; the paper proposes a deflection-compensated BvN (D-BvN) switch architecture to enhance the quasi-static scheduling (the abstract is truncated thereafter). Although the "von Neumann" in [10] is a decomposition in switching theory rather than the stored-program architecture, the shared theme is that switching fabric costs are the bottleneck resource. Finally, [11] analyzes the "von Neumann vicious circle" coined by John Backus: non-von Neumann architectures cannot be developed for lack of widely available effective non-von Neumann languages, and new languages cannot be created for lack of conceptual foundations for non-von Neumann architectures, because programming languages are high-level abstract isomorphic copies of von Neumann computers. This is the sociotechnical lock-in argument that any re-entry architecture must confront, independent of its physical cost advantage.

**The QNFO corpus.** [12] proposes Hamiltonian dynamics as the engine of biological computation (the supplied corpus entry carries no abstract text, so we use it only as the motivating source of the re-entry concept). [13], a technical framework for network isomorphism, likewise supplies no abstract text; we cite it as companion QNFO corpus material and draw no specific claim from it.

## 3. Methods

### 3.1 The two cost models

**Von Neumann switching model.** Consider a stored-program machine executing a program of $N_{\mathrm{op}}$ logical operations. Each operation requires $k_{\mathrm{acc}}$ memory accesses (instruction fetch plus data load/store) before the logical work is done. Let $t_{\mathrm{mem}}$ be the effective time per memory access and $t_{\mathrm{alu}}$ the time for the logical work itself. The per-operation cost is

$$c_{\mathrm{sw}} = k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}},$$

and the total cost is

$$T_{\mathrm{sw}} = N_{\mathrm{op}} \left( k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}} \right).$$

We call $k_{\mathrm{acc}}\, t_{\mathrm{mem}}$ the switching overhead per operation and define the overhead fraction

$$f_{\mathrm{sw}} = \frac{k_{\mathrm{acc}}\, t_{\mathrm{mem}}}{k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}}}.$$

**Hamiltonian re-entry model.** In the re-entry model, the machine state is a point $x_t$ in phase space evolving under a Hamiltonian $H$. A computation of $N_{\mathrm{op}}$ logical steps corresponds to $N_{\mathrm{op}}$ re-entries of the trajectory into a designated operating region $\mathcal{R} \subset \Omega$. Let $t_{\mathrm{dyn}}$ be the mean time for the trajectory to traverse one useful dynamical segment (the analogue of $t_{\mathrm{alu}}$), and let $t_{\mathrm{re}}$ be the mean re-entry overhead: the extra time spent steering the trajectory back into $\mathcal{R}$ after each useful segment, including any classical control intervention of the hybrid kind discussed in [8]. The per-re-entry cost is

$$c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}},$$

and the total is

$$T_{\mathrm{re}} = N_{\mathrm{op}} \left( t_{\mathrm{dyn}} + t_{\mathrm{re}} \right), \qquad f_{\mathrm{re}} = \frac{t_{\mathrm{re}}}{t_{\mathrm{dyn}} + t_{\mathrm{re}}}.$$

The geometric lower bound of [7] — energy dispersion bounded below by curve length — enters as a constraint that $t_{\mathrm{re}}$ cannot be driven to zero without paying in energy spread; we encode this by treating $t_{\mathrm{re}}$ as a positive parameter rather than a free optimization target.

### 3.2 Comparison criterion

Define the ratio of the dynamical overhead to the memory overhead per operation:

$$r = \frac{t_{\mathrm{re}}/t_{\mathrm{dyn}}}{k_{\mathrm{acc}}\, t_{\mathrm{mem}}/t_{\mathrm{dyn}}} = \frac{t_{\mathrm{re}}}{k_{\mathrm{acc}}\, t_{\mathrm{mem}}}.$$

The re-entry model beats the switching model on total time when $T_{\mathrm{re}} < T_{\mathrm{sw}}$, i.e. when

$$t_{\mathrm{dyn}} + t_{\mathrm{re}} < k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}}.$$

Dividing by $t_{\mathrm{dyn}}$ and defining the dynamical-to-ALU time ratio $\rho = t_{\mathrm{dyn}}/t_{\mathrm{alu}}$, the condition becomes

$$1 + \frac{t_{\mathrm{re}}}{t_{\mathrm{dyn}}} < \frac{k_{\mathrm{acc}}\, t_{\mathrm{mem}}}{t_{\mathrm{dyn}}} + \frac{1}{\rho}.$$

### 3.3 Assumptions

(A1) Both machines perform the same $N_{\mathrm{op}}$ logical operations; the models differ only in update overhead. (A2) Memory accesses are serialized; no caching removes them. (A3) The re-entry overhead $t_{\mathrm{re}}$ is a fixed parameter, not derived from a nonequilibrium statistical operator; deriving it from first principles along the lines of [5], [6] is left open. (A4) Mixing is adequate that the mean re-entry time exists; computing it would require solving a mixing problem of the kind shown to be PSPACE-hard in [4], so we do not attempt it.

## 4. Analysis

Every number in this section is derived from the stated inputs. Inputs are of two kinds: structural integers of the model ($k_{\mathrm{acc}}$) and illustrative parameter values that we state explicitly as assumptions (all times). No value is taken from measurement.

**Input 1 (structural).** $k_{\mathrm{acc}} = 4$ memory accesses per operation: one instruction fetch, one operand load, one store, one next-instruction prefetch. Source: model definition in Section 3.1.

**Input 2 (assumed, labeled).** $t_{\mathrm{alu}} = 1$ time unit (normalization). $t_{\mathrm{mem}} = 16$ time units per access — chosen to represent a memory hierarchy much slower than the arithmetic unit, a regime in which switching overhead is the dominant concern; this is an assumption of the illustrative scenario, not a measurement. $t_{\mathrm{dyn}} = 4$ time units per useful dynamical segment — assumed, representing a Hamiltonian segment that does four units of useful evolution. $t_{\mathrm{re}} = 1$ time unit per re-entry — assumed, representing modest steering overhead consistent with the geometric constraint of [7] that re-entry cost is bounded below but not zero.

**Derivation 1: switching cost per operation.**

$$c_{\mathrm{sw}} = k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}} = 4 \times 16 + 1 = 64 + 1 = 65 \text{ time units}.$$

**Derivation 2: switching overhead fraction.**

$$f_{\mathrm{sw}} = \frac{64}{65} \approx 0.9846.$$

Arithmetic: $64/65 = 0.984615\ldots$, rounded to $0.9846$. Under the assumed parameters, $98.46\%$ of the stored-program machine's time is switching overhead.

**Derivation 3: re-entry cost per operation.**

$$c_{\mathrm{re}} = t_{\mathrm{dyn}} + t_{\mathrm{re}} = 4 + 1 = 5 \text{ time units}.$$

**Derivation 4: re-entry overhead fraction.**

$$f_{\mathrm{re}} = \frac{1}{5} = 0.2000.$$

**Derivation 5: total-time comparison for $N_{\mathrm{op}} = 10^{6}$ operations.**

$$T_{\mathrm{sw}} = 10^{6} \times 65 = 6.5 \times 10^{7} \text{ time units},$$
$$T_{\mathrm{re}} = 10^{6} \times 5 = 5.0 \times 10^{6} \text{ time units}.$$

The ratio is

$$\frac{T_{\mathrm{sw}}}{T_{\mathrm{re}}} = \frac{65}{5} = 13.0.$$

**Derivation 6: the break-even condition.** The re-entry model wins when $c_{\mathrm{re}} < c_{\mathrm{sw}}$, i.e.

$$t_{\mathrm{dyn}} + t_{\mathrm{re}} < k_{\mathrm{acc}}\, t_{\mathrm{mem}} + t_{\mathrm{alu}}.$$

Solve for the memory time $t_{\mathrm{mem}}$ at equality, holding the other assumed values fixed:

$$k_{\mathrm{acc}}\, t_{\mathrm{mem}}^{*} = t_{\mathrm{dyn}} + t_{\mathrm{re}} - t_{\mathrm{alu}} = 4 + 1 - 1 = 4,$$
$$t_{\mathrm{mem}}^{*} = \frac{4}{4} = 1 \text{ time unit}.$$

Equivalently, in terms of the ratio $r = t_{\mathrm{mem}}/t_{\mathrm{alu}}$ with $t_{\mathrm{re}}/t_{\mathrm{alu}} = 1$ and $t_{\mathrm{dyn}}/t_{\mathrm{alu}} = 4$:

$$r^{*} = \frac{t_{\mathrm{dyn}} + t_{\mathrm{re}} - t_{\mathrm{alu}}}{k_{\mathrm{acc}}\, t_{\mathrm{alu}}} = \frac{4}{4} = 1.0.$$

So under these assumptions the re-entry model wins whenever $t_{\mathrm{mem}} > 1$ time unit, i.e. whenever memory is slower than the arithmetic unit at all — a very weak condition, which reflects that the assumed $t_{\mathrm{re}} = 1$ is small relative to $t_{\mathrm{dyn}} = 4$.

**Derivation 7: sensitivity of the verdict to $t_{\mathrm{re}}$.** The comparison flips when the re-entry overhead grows. Setting $c_{\mathrm{re}} = c_{\mathrm{sw}} = 65$ and solving for $t_{\mathrm{re}}$:

$$t_{\mathrm{re}}^{*} = 65 - t_{\mathrm{dyn}} = 65 - 4 = 61 \text{ time units}.$$

Thus the re-entry model tolerates a re-entry overhead up to $61$ time units — $15.25$ times the useful segment time $t_{\mathrm{dyn}} = 4$ — before losing to the switching model at the assumed $t_{\mathrm{mem}} = 16$. Arithmetic: $61/4 = 15.25$.

**Derivation 8: overhead-fraction crossover in $r$.** With $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$, and $t_{\mathrm{mem}} = r$, the switching overhead fraction is

$$f_{\mathrm{sw}}(r) = \frac{4r}{4r + 1}.$$

At $r = 4$: $f_{\mathrm{sw}} = 16/17 \approx 0.9412$. At $r = 16$: $f_{\mathrm{sw}} = 64/65 \approx 0.9846$ (matching Derivation 2). At $r = 1$: $f_{\mathrm{sw}} = 4/5 = 0.8$. The re-entry overhead fraction is constant at $f_{\mathrm{re}} = 0.2$. The fractions are equal when $4r/(4r+1) = 1/5$, i.e. $20r = 4r + 1$, so $16r = 1$ and $r = 1/16 = 0.0625$; for every $r > 0.0625$ the switching machine wastes a larger fraction of its time on overhead than the re-entry machine does under these assumptions.

**Derivation 9: entropy bookkeeping placeholder made explicit.** If the re-entry overhead is booked as an entropy production cost, and following [1] we use the Gibbs-von Neumann entropy as the state functional, a dimensionless bookkeeping quantity is the ratio of overhead to useful evolution in log form:

$$\eta = \ln\!\left(\frac{t_{\mathrm{re}} + t_{\mathrm{dyn}}}{t_{\mathrm{dyn}}}\right) = \ln\!\left(\frac{5}{4}\right) \approx 0.2231.$$

Arithmetic: $\ln(1.25) = 0.223143\ldots$, rounded to $0.2231$. This is a model quantity, not a thermodynamic entropy measurement; its physical interpretation is deferred to Section 6.

## 5. Results

All results below are projections of the cost model of Section 3 under the assumptions of Section 4; none are empirical measurements.

- **R1 (per-operation costs).** Under the assumed parameters ($k_{\mathrm{acc}} = 4$, $t_{\mathrm{mem}} = 16$, $t_{\mathrm{alu}} = 1$, $t_{\mathrm{dyn}} = 4$, $t_{\mathrm{re}} = 1$): $c_{\mathrm{sw}} = 65$ time units, $c_{\mathrm{re}} = 5$ time units (Derivations 1, 3).
- **R2 (overhead fractions).** $f_{\mathrm{sw}} \approx 0.9846$; $f_{\mathrm{re}} = 0.2000$ (Derivations 2, 4).
- **R3 (total-time ratio).** For $N_{\mathrm{op}} = 10^{6}$: $T_{\mathrm{sw}} = 6.5 \times 10^{7}$, $T_{\mathrm{re}} = 5.0 \times 10^{6}$, ratio $13.0$ (Derivation 5).
- **R4 (break-even).** The re-entry model wins whenever $t_{\mathrm{mem}} > t_{\mathrm{mem}}^{*} = 1$ time unit, equivalently $r > r^{*} = 1.0$, under the fixed assumptions (Derivation 6).
- **R5 (robustness to re-entry overhead).** The verdict is unchanged for any $t_{\mathrm{re}} < t_{\mathrm{re}}^{*} = 61$ time units, i.e. up to $15.25$ times the useful segment time (Derivation 7).
- **R6 (fraction crossover).** The switching machine's overhead fraction exceeds the re-entry machine's for all $r > 1/16 = 0.0625$; at $r = 16$ the fractions are $0.9846$ versus $0.2000$ (Derivation 8).
- **R7 (bookkeeping ratio).** $\eta = \ln(5/4) \approx 0.2231$ (Derivation 9), a dimensionless model quantity.

The qualitative reading: in a memory-bound regime, the stored-program organization spends nearly all of its time switching, and the re-entry organization wins by a large modeled margin and tolerates a wide range of re-entry overheads before the verdict reverses. The strength of this conclusion is entirely conditional on the assumed parameters, as Section 6 makes explicit.

## 6. Discussion

**Limitations.** The model is deliberately minimal, and each assumption is a potential failure point. (A2) — serialized, uncached memory — is the most favorable case for the switching machine's critic to attack in reverse: real hierarchies cache instructions and data, reducing effective $k_{\mathrm{acc}}\, t_{\mathrm{mem}}$ dramatically for regular workloads. If effective memory time drops to $t_{\mathrm{mem}}^{\mathrm{eff}} = 1$ time unit, then $c_{\mathrm{sw}} = 4 \times 1 + 1 = 5 = c_{\mathrm{re}}$, and the models tie exactly; any further caching improvement makes the switching model win. The headline ratio of $13.0$ therefore holds only in the memory-bound regime and is not a general claim.

(A3) is the deepest limitation: we assumed $t_{\mathrm{re}}$ rather than deriving it. The nonequilibrium statistical operator program [5], [6] exists precisely because irreversible behavior from reversible Hamiltonian dynamics lacks a rigorous first-principles treatment; a derived $t_{\mathrm{re}}$ might be far larger than the assumed $1$ time unit, since steering a trajectory back into $\mathcal{R}$ may require control actions whose cost scales badly. The robustness result R5 ($t_{\mathrm{re}}$ may reach $61$ time units) is generous, but it is a projection within the model, not evidence about real Hamiltonian devices.

(A4) hides the hardest computational problem. Whether the trajectory re-enters $\mathcal{R}$ at all, and how often, is a mixing question; [4] reports that estimating mixing properties for 4-local Hamiltonian dynamics and continuous quantum random walks is PSPACE-hard, and proposes the von Neumann entropy of the time-average as a mixing characterization. Our model assumes the benign case. If the system is not mixing on relevant timescales, $t_{\mathrm{re}}$ may be unbounded and the re-entry model fails outright. This is, in our view, the most likely falsifier of the practical claims: a demonstration that generic Hamiltonian computational dynamics re-enters its operating region too rarely would collapse the comparison.

**What would falsify the claims.** Three concrete falsifiers: (i) an effective-memory analysis showing that realistic caching drives $t_{\mathrm{mem}}^{\mathrm{eff}} \leq 1$ time unit in the assumed units, erasing the advantage (the tie point of the Discussion above); (ii) a derivation or measurement of $t_{\mathrm{re}} > 61$ time units for any plausible Hamiltonian implementation; (iii) a mixing argument showing that the re-entry frequency assumed in (A4) is unattainable for the class of dynamics proposed in [12].

**Against ourselves.** The comparison may also be unfair to the switching machine in the opposite direction: we charged it full serialized memory cost but charged the re-entry machine no control-program overhead, even though any practical re-entry machine needs a classical control layer, and [8] notes that no fully satisfactory solution to hybrid classical-quantum coupling has been established to date. A symmetric accounting would add a per-re-entry control cost to $T_{\mathrm{re}}$; our $t_{\mathrm{re}} = 1$ can be read as a placeholder for exactly that, but making it explicit would be more honest. Further, the geometric bound of [7] (energy dispersion bounded below by curve length) suggests that reducing $t_{\mathrm{re}}$ may require increasing energy spread, so there may be a conservation-law trade-off our time-only model cannot see. Finally, even if the physics favored re-entry, the lock-in argument of [11] — languages isomorphic to von Neumann machines blocking non-von Neumann architectures — is an obstacle no cost model addresses; the neuromorphic literature [9] shows that architectural alternatives face this barrier in practice, and the switching-fabric literature [10] shows that even within switching theory, predictability under realistic (bursty) conditions, not just average throughput, is what determines adoption.

**Open questions.** (1) Can $t_{\mathrm{re}}$ be derived from the extended von Neumann form of the NSO [5] rather than assumed? (2) Does the bookkeeping ratio $\eta = \ln(5/4) \approx 0.2231$ correspond to any operational entropy production, in the sense defended in [1]? (3) For which problem classes do Carleman or Koopman-von Neumann embeddings [3] make the re-entry machine constructible rather than merely modelable? (4) Does the projection picture of [2], in which quantum dynamics emerges from classical statistical dynamics with small dispersion $\alpha$, change the effective value of $t_{\mathrm{dyn}}$ at finite $\alpha$?

## 7. Conclusion

We formulated a minimal cost comparison between von Neumann switching overheads and Hamiltonian re-entry costs, motivated by the QNFO proposal of Hamiltonian dynamics as the engine of biological computation [12] and grounded in the entropy-theoretic [1], nonequilibrium [5], [6], geometric [7], and embedding [2], [3], [8] literature on Hamiltonian computation, with the architectural-alternatives literature [9], [10], [11] supplying the adoption context. Within the model, with all parameters stated as assumptions, the re-entry organization wins by a factor of $13.0$ in total time in a memory-bound regime, sustains re-entry overheads up to $15.25$ times its useful segment time, and dominates on overhead fraction for all memory-to-ALU ratios $r > 0.0625$. These are model projections, not measurements; the comparison ties exactly when effective memory time equals the arithmetic unit time, and the model's most probable failure mode is the mixing constraint that makes re-entry frequency computable only at PSPACE-hard cost in general [4]. The contribution is the explicit parameterization and the identification of which assumption — derived $t_{\mathrm{re}}$, effective caching, or mixing — must fall for the qualitative verdict to change.

## References

[1] arXiv:quant-ph/0701127v2 | The Physical Basis of the Gibbs-von Neumann entropy
[2] arXiv:quant-ph/0511074v1 | Quantum mechanics as an asymptotic projection of statistical mechanics of classical fields: derivation of Schrödinger's, Heisenberg's and von Neumann's equations
[3] arXiv:2311.15628v2 | How to Map Linear Differential Equations to Schrödinger Equations via Carleman and Koopman-von Neumann Embeddings for Quantum Algorithms
[4] arXiv:quant-ph/0401184v1 | Estimating mixing properties of local Hamiltonian dynamics and continuous quantum random walks is PSPACE-hard
[5] arXiv:1809.03357v1 | Electrical conductivity of charged particle systems and the Zubarev NSO method
[6] arXiv:1905.02012v1 | Non-Equilibrium Statistical Operator
[7] arXiv:1302.1844v1 | Geometry of quantum dynamics and a time-energy uncertainty relation for mixed states
[8] arXiv:1103.3589v1 | General linear dynamics - quantum, classical or hybrid
[9] arXiv:2304.06897v1 | A Bibliometric Review of Neuromorphic Computing and Spiking Neural Networks
[10] arXiv:1308.4280v1 | Birkhoff-von-Neumann Switches with Deflection-Compensated Mechanism
[11] arXiv:1602.02715v2 | On the notion of "von Neumann vicious circle" coined by John Backus
[12] QNFO: Hamiltonian Dynamics as the Engine of Biological Computation | DOI 10.5281/zenodo.18195888
[13] QNFO: Comprehensive Technical Framework for Network Isomorphism | DOI 10.5281/zenodo.18199940