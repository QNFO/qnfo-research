# Re-Entry Dynamics as a Switching Process: Comparing Hamiltonian Re-Entry Computation to von Neumann Switching Costs

## Abstract

The QNFO framework "Hamiltonian Dynamics as the Engine of Biological Computation" (DOI 10.5281/zenodo.18195888) proposes that computation can be carried by autonomous Hamiltonian trajectories that repeatedly re-enter the same phase-space region, closing dynamical loops that play the role of executed instructions. This paper asks a cost question about that proposal: how does the switching cost of re-entry-based computation compare with the switching cost of a von Neumann architecture, in which every logical operation is paid for by an explicit instruction fetch, decode, and execute cycle? We formalize both regimes as per-operation cost models over a common unit of switching effort. Under explicitly stated illustrative parameters, the von Neumann cycle costs $C_{\mathrm{vN}} = 2.5$ units per operation, while a re-entry loop of $L = 4$ nodes with per-pass cost $c_p = 0.2$ costs $C_{\mathrm{re}} = 0.8$ units per cycle, a ratio of $3.125$ in favor of re-entry; amortizing a setup cost of $10$ units gives a break-even of $n \approx 5.88$ cycles. A sensitivity analysis shows the advantage is fragile: the per-pass cost threshold at which the advantage vanishes is $c_p^{*} = 0.625$. We connect the model to the literature on Gibbs-von Neumann entropy, nonequilibrium statistical operators, mixing hardness, Koopman-von Neumann embeddings, Birkhoff-von Neumann switching, and the Backus critique, and we state the limits of the comparison.

## 1. Introduction

Every computing architecture pays a price for moving state from where it is stored to where it is transformed. In a von Neumann architecture this price appears as the fetch–decode–execute cycle: before any arithmetic happens, the machine must switch its control and data paths to bring an instruction into the processing unit. John Backus famously argued that this coupling runs deeper than hardware, coining the "von Neumann vicious circle": programming languages are isomorphic copies of the von Neumann machine, so non-von Neumann architectures cannot gain traction without non-von Neumann languages, and vice versa [11]. Any proposal for a fundamentally different computational substrate must therefore be evaluated not only for physical plausibility but for its switching economics.

This paper performs such an evaluation for the computational model proposed in the QNFO framework "Hamiltonian Dynamics as the Engine of Biological Computation" (DOI 10.5281/zenodo.18195888) [12]. The supplied record for [12] gives only the title and identifier and no further summary detail; our reading of the proposal is therefore restricted to what the title asserts, namely that Hamiltonian dynamics — the autonomous, energy-conserving motion of a physical system — can serve as the engine of computation, in the way biological systems appear to compute. We take the central mechanistic idea suggested by the title to be *re-entry*: a Hamiltonian trajectory that returns to a previously visited region of phase space, closing a loop, so that one act of dynamical setup is reused many times without an external controller re-issuing it. The word "re-entry" in the research prompt ("Re-entry from 10.5281/zenodo.18195888") indicates that this loop-closing mechanism is the object of comparison.

The comparison target is the switching cost of the von Neumann regime. We build both regimes as minimal per-operation cost models over a common abstract unit of switching effort, derive their relative cost with fully shown arithmetic, and probe the sensitivity of the result. The contributions are:

1. A two-model cost formalism: an explicit-controller model $C_{\mathrm{vN}}$ and an autonomous re-entry model $C_{\mathrm{re}}$, with all parameters stated as assumptions.
2. Exact arithmetic derivations of the per-operation costs, their ratio, an amortization break-even cycle count, and a sensitivity threshold.
3. A literature synthesis placing the comparison inside the Hamiltonian-statistical-mechanics tradition [1], [2], [5], [6], [7], [8], the dynamical-systems hardness literature [4], the embedding literature for quantum algorithms [3], and the architecture critique literature [9], [10], [11].
4. An explicit statement of what would falsify the claimed advantage.

We emphasize at the outset that no empirical measurements are reported here. Every number in Sections 4 and 5 is either (a) derived by shown arithmetic from parameters declared in Section 3 as illustrative assumptions, or (b) a projection whose assumptions and uncertainty are stated inline. The value of the exercise is structural: it converts a qualitative architecture debate into a small set of named parameters whose empirical measurement would settle the question.

## 2. Background and Related Work

**Entropy from Hamiltonian dynamics.** Gemmer-style arguments for the physical basis of the Gibbs-von Neumann entropy are given in [1]: the authors develop the argument that the Gibbs-von Neumann entropy is the appropriate statistical-mechanical generalization of thermodynamic entropy, for macroscopic and microscopic systems, whether in thermal equilibrium or not, as a consequence of Hamiltonian dynamics, building on well-known results they cite internally. This matters for our comparison because it supplies the thermodynamic footing for attributing a physical cost to dynamical computation: if the Gibbs-von Neumann entropy is grounded in Hamiltonian dynamics itself, then a re-entry computation performed by Hamiltonian motion is not a parasitic overlay on physics but a process whose entropy bookkeeping is already of the standard kind. The entry for [1] is truncated mid-sentence after "incorporates a variety of"; we use only the claims stated up to that point.

**Quantum mechanics as a projection of classical statistics.** Work [2] shows that quantum mechanics can be represented as a natural projection of a classical statistical model on a phase space $\Omega = H \times H$, where $H$ is a real Hilbert space, with statistical states given by Gaussian measures of very small dispersion $\alpha$, interpreted as fluctuations; Schrödinger's, Heisenberg's and von Neumann's equations are derived in this picture. For our purposes this is a precedent for the QNFO strategy of deriving quantum-looking computational behavior from an underlying classical dynamical substrate: the direction of derivation in [2] runs from classical statistical dynamics up to the von Neumann equation, which is the same direction a "dynamics as engine" account of computation requires.

**Embedding classical dynamics for quantum algorithms.** Reference [3] studies how to map linear differential equations to Schrödinger equations via Carleman and Koopman-von Neumann embeddings for quantum algorithms, noting that solving differential equations with large degrees of freedom is an important scientific and industrial task and that embedding classical variables into a quantum state is necessary to solve such equations on a quantum computer. The Koopman-von Neumann construction lifts nonlinear classical dynamics into a linear Hilbert-space evolution; the entry states that the class of problems that can be treated has been limited so far (the sentence is truncated). This is the constructive counterpart of our cost question: embeddings make dynamical computation executable on quantum hardware, and the switching-cost comparison of this paper quantifies what such embeddings would save or spend.

**Hardness of assessing mixing.** Reference [4] considers interacting qubit systems with dynamics according to 4-local Hamiltonians and continuous quantum random walks, and states that for these systems one could use the von Neumann entropy of the time-average to characterize mixing properties; the title asserts that estimating these mixing properties is PSPACE-hard. This is a central caveat for re-entry computation: whether a Hamiltonian trajectory actually re-enters a useful region — whether the dynamics mixes well enough to revisit computationally relevant states — is in general exponentially hard to decide. Our cost models in Section 3 assume re-entry occurs with a given period; [4] tells us that verifying this assumption for a specific large Hamiltonian system is computationally intractable in general.

**Nonequilibrium statistical operators.** References [5] and [6] address the same foundational gap from the Zubarev tradition. Entry [5] states that the statistical mechanics of nonequilibrium processes is not rigorously solved, that D. N. Zubarev invented the nonequilibrium statistical operator (NSO) method to describe irreversible behavior starting from reversible Hamiltonian dynamics, and that the paper discusses this approach, in particular the extended variant (the entry truncates there). Entry [6] makes the same framing — irreversibility is not rigorously solved, approaches rest on empirical assumptions, and a rigorous first-principles theory is missing — and credits an important contribution to describing irreversible behavior from reversible dynamics (the entry truncates before naming the method in full, though the title identifies it as the Non-Equilibrium Statistical Operator). Re-entry computation lives exactly in this gap: it is an irreversible, dissipative-looking computational pattern realized by reversible Hamiltonian motion, so the NSO line of work is the natural statistical-mechanical language in which a rigorous cost accounting of re-entry would eventually have to be written.

**Geometry and time-energy cost of dynamics.** Reference [7] establishes relations between Hamiltonian dynamics and Riemannian structures on phase spaces for unitarily evolving finite-level quantum systems in mixed states, showing that the energy dispersion — defined as $1/\hbar$ times the path integral of the energy uncertainty — of a unitary evolution is bounded from below by the length of the evolution curve. This gives our cost model a physical lower-bound principle: a re-entry loop of a given geometric length in state space cannot be traversed without at least a corresponding integrated energy uncertainty. Any claim that re-entry is "cheap" must respect this bound; we use it qualitatively in Section 6.

**Hybrid and generalized dynamics.** Reference [8] describes a path-integral formulation of classical Hamiltonian dynamics and, building on it, a new attempt at hybrid dynamics coupling classical and quantum degrees of freedom directly, noting that no fully satisfactory solution of the hybrid problem has been established to date. The entry is truncated after "Related aspects"; we use only the stated claims. Hybrid dynamics is relevant because a re-entry computer would inevitably couple an autonomous Hamiltonian core to a classical readout and control layer, and [8] indicates that this coupling is an open foundational problem, not a solved engineering detail.

**Beyond von Neumann: neuromorphic and switching hardware.** Reference [9] is a bibliometric review of neuromorphic computing and spiking neural networks, stating that these fields aim to leverage biological inspiration to achieve greater energy efficiency and computational power beyond traditional von Neumann architectured machines, that spiking neural networks hold potential as the basis of third-generation neural networks, and that developments in memristive and compute-in-(memory) technologies aid this program (entry truncated). This locates the QNFO re-entry proposal inside an existing research current that already measures itself against von Neumann energy costs. Reference [10] concerns the hardware switching layer directly: it notes that input scheduling based on Birkhoff-von-Neumann (BvN) decomposition achieves high throughput and low complexity, but that the BvN switch becomes less predictable under bursty input traffic, and proposes a deflection-compensated BvN (D-BvN) switch architecture to enhance quasi-static scheduling based on BvN decomposition (entry truncated). BvN decomposition — writing a doubly stochastic routing matrix as a mixture of permutation matrices — is the canonical formalization of "switching cost" in interconnection networks, and we borrow its spirit: a switch schedule is a sequence of permutations, and each permutation application is one switching event.

**The architecture trap.** Finally, [11] analyzes the "von Neumann vicious circle" coined by John Backus: non-von Neumann architectures cannot be developed because of the lack of widely available effective non-von Neumann languages, and new languages cannot be created for lack of conceptual foundations for non-von Neumann architectures, the reason being that programming languages are high-level abstract isomorphic copies of von Neumann computers. This is the socio-technical reason a re-entry architecture needs an explicit cost comparison stated in architecture-neutral terms, as we attempt here.

**The QNFO corpus.** The supplied record for [12], "Hamiltonian Dynamics as the Engine of Biological Computation" (DOI 10.5281/zenodo.18195888), contains only the title and identifier; the summary field is empty, so no internal claims, methods, or numbers of that paper can be quoted here. The same holds for [13], "Comprehensive Technical Framework for Network Isomorphism" (DOI 10.5281/zenodo.18199940). We therefore treat [12] as the proposal under revision — its title licenses the reading that Hamiltonian dynamics performs computation, and the research prompt supplies the re-entry framing — and we note that [13], by title, concerns isomorphism testing between networks, which would be the natural tool for checking whether two re-entry loop structures implement the same computation; beyond that title-level remark we make no claim about its content.

## 3. Methods

### 3.1 Common cost currency

We define an abstract unit of switching effort, $1$ cost unit (cu), representing one elementary act of redirecting state along a path: in a network switch this is one permutation application in the sense of BvN scheduling [10]; in a stored-program machine it is one micro-operations-level transfer of an instruction or datum. All costs below are in cu. The currency is deliberately architecture-neutral to avoid the isomorphism trap of [11].

### 3.2 Model V: explicit-controller (von Neumann) cost

Each logical operation in an explicit-controller machine requires three sequential switching acts:

$$
C_{\mathrm{vN}} = c_f + c_d + c_e,
$$

where $c_f$ is the fetch cost, $c_d$ the decode/dispatch cost, and $c_e$ the execute cost. We assume the illustrative values

$$
c_f = 1.0\ \mathrm{cu}, \qquad c_d = 0.5\ \mathrm{cu}, \qquad c_e = 1.0\ \mathrm{cu}.
$$

These are assumptions, not measurements; they encode the qualitative fact that fetch and execute each move a full instruction or datum, while decode is a smaller control-path act. The energy analogue is $E_{\mathrm{vN}} = k\,E_{\mathrm{sw}}$ with $k$ switching events per logical operation; we take $k = 3$ (one event per phase) and unit switching energy $E_{\mathrm{sw}} = 1$ in arbitrary energy units.

### 3.3 Model R: autonomous re-entry cost

In the re-entry regime, a Hamiltonian trajectory of loop length $L$ nodes is set up once and then traversed autonomously. Per traversal (one re-entry cycle), the cost is the per-pass cost of moving state through the loop:

$$
C_{\mathrm{re}} = L\,c_p,
$$

with illustrative $L = 4$ nodes and $c_p = 0.2\ \mathrm{cu}$ per node pass. The per-pass cost is small relative to $c_f$ because no instruction is fetched or decoded: the dynamics itself is the program, consistent with the entropy grounding of Hamiltonian motion in [1] and subject to the geometric lower bound of [7]. Setup (preparing the initial state and the Hamiltonian coupling that closes the loop) costs $C_s = 10\ \mathrm{cu}$ once, amortized over $n$ cycles:

$$
C_{\mathrm{re}}(n) = \frac{C_s}{n} + L\,c_p.
$$

The energy analogue is $E_{\mathrm{re}} = E_{\mathrm{sw}}$ per cycle (one autonomous pass, no controller events), i.e. $k = 1$.

### 3.4 Comparison quantities

We derive four quantities: (i) the per-operation ratio $R = C_{\mathrm{vN}} / C_{\mathrm{re}}$; (ii) the amortized ratio $R(n) = C_{\mathrm{vN}} / C_{\mathrm{re}}(n)$; (iii) the break-even cycle count $n^{*}$ solving $C_{\mathrm{re}}(n^{*}) = C_{\mathrm{vN}}$; (iv) the sensitivity threshold $c_p^{*}$ solving $L\,c_p^{*} = C_{\mathrm{vN}}$. All arithmetic is shown in Section 4.

## 4. Analysis

Every input number below is an assumption declared in Section 3; no number originates from measurement or from the cited literature.

**Step 1: von Neumann per-operation cost.** With $c_f = 1.0$, $c_d = 0.5$, $c_e = 1.0$:

$$
C_{\mathrm{vN}} = c_f + c_d + c_e = 1.0 + 0.5 + 1.0 = 2.5\ \mathrm{cu}.
$$

**Step 2: re-entry per-cycle cost.** With $L = 4$ and $c_p = 0.2$:

$$
C_{\mathrm{re}} = L\,c_p = 4 \times 0.2 = 0.8\ \mathrm{cu}.
$$

**Step 3: per-cycle cost ratio.**

$$
R = \frac{C_{\mathrm{vN}}}{C_{\mathrm{re}}} = \frac{2.5}{0.8} = 3.125.
$$

So under these assumptions one re-entry cycle replaces one von Neumann operation at $0.8/2.5 = 0.32$, i.e. $32\%$, of the switching cost.

**Step 4: amortized re-entry cost.** With $C_s = 10$:

$$
C_{\mathrm{re}}(n) = \frac{10}{n} + 0.8.
$$

At $n = 1$: $C_{\mathrm{re}}(1) = 10 + 0.8 = 10.8\ \mathrm{cu}$, which is $10.8/2.5 = 4.32$ times the von Neumann cost — re-entry is worse for a single use. At $n = 10$: $C_{\mathrm{re}}(10) = 10/10 + 0.8 = 1.0 + 0.8 = 1.8\ \mathrm{cu}$, ratio $2.5/1.8 \approx 1.389$.

**Step 5: break-even cycle count.** Solve $C_s/n + L c_p = C_{\mathrm{vN}}$:

$$
\frac{10}{n} + 0.8 = 2.5 \;\Rightarrow\; \frac{10}{n} = 1.7 \;\Rightarrow\; n^{*} = \frac{10}{1.7} \approx 5.882.
$$

Thus re-entry must be reused at least $n \geq 6$ (rounding up to whole cycles) to beat the explicit controller.

**Step 6: sensitivity threshold in $c_p$.** Solve $L\,c_p^{*} = C_{\mathrm{vN}}$:

$$
c_p^{*} = \frac{2.5}{4} = 0.625\ \mathrm{cu}.
$$

Check the neighborhood: at $c_p = 0.5$, $C_{\mathrm{re}} = 4 \times 0.5 = 2.0$, ratio $2.5/2.0 = 1.25$ (advantage survives). At $c_p = 0.8$, $C_{\mathrm{re}} = 4 \times 0.8 = 3.2$, ratio $2.5/3.2 = 0.78125$ (advantage lost). The advantage therefore hinges on the per-pass cost staying below $0.625\ \mathrm{cu}$, i.e. below $25\%$ of $C_{\mathrm{vN}}$.

**Step 7: sensitivity threshold in $L$.** Solve $L^{*} c_p = C_{\mathrm{vN}}$ with $c_p = 0.2$:

$$
L^{*} = \frac{2.5}{0.2} = 12.5.
$$

Loops longer than $12$ nodes (rounding down to whole nodes for advantage) erase the per-cycle advantage at this $c_p$.

**Step 8: energy ratio.** With $E_{\mathrm{vN}} = k E_{\mathrm{sw}}$, $k = 3$, and $E_{\mathrm{re}} = 1 \cdot E_{\mathrm{sw}}$:

$$
\frac{E_{\mathrm{vN}}}{E_{\mathrm{re}}} = \frac{3\,E_{\mathrm{sw}}}{1\,E_{\mathrm{sw}}} = 3.
$$

**Step 9: uncertainty of the headline ratio.** The ratio $R = C_{\mathrm{vN}}/(L c_p)$ propagates parameter uncertainty as $R \propto 1/c_p$ and $R \propto 1/L$. If $c_p$ is uncertain by a factor $f$ (i.e. $c_p \in [0.2/f,\, 0.2f]$), then $R$ lies in $[3.125/f,\, 3.125 f]$. For $f = 2$, $R \in [1.5625,\, 6.25]$; the qualitative conclusion (advantage $> 1$) survives only if $f < 3.125$, since $R = 1$ at $c_p = c_p^{*} = 0.625$.

## 5. Results

All results follow from the derivations of Section 4; none are empirical.

- **R1 (per-cycle cost ratio).** Under the stated assumptions ($c_f = 1.0$, $c_d = 0.5$, $c_e = 1.0$, $L = 4$, $c_p = 0.2$), the re-entry cycle costs $C_{\mathrm{re}} = 0.8\ \mathrm{cu}$ against $C_{\mathrm{vN}} = 2.5\ \mathrm{cu}$, a ratio $R = 3.125$ in favor of re-entry.
- **R2 (amortization).** With setup cost $C_s = 10\ \mathrm{cu}$, re-entry is worse than the von Neumann cycle for a single use ($C_{\mathrm{re}}(1) = 10.8\ \mathrm{cu}$, ratio $4.32$ against re-entry), reaches parity at $n^{*} = 10/1.7 \approx 5.88$ cycles, and at $n = 10$ cycles costs $1.8\ \mathrm{cu}$ (ratio $\approx 1.389$ in favor of re-entry).
- **R3 (sensitivity).** The advantage vanishes when the per-pass cost exceeds $c_p^{*} = 0.625\ \mathrm{cu}$ (checked: $c_p = 0.5$ gives ratio $1.25$; $c_p = 0.8$ gives ratio $0.78125$), or when the loop length exceeds $L^{*} = 12.5$ nodes at $c_p = 0.2$.
- **R4 (energy projection).** Labeled projection with stated assumptions: if the von Neumann cycle requires $k = 3$ switching events per logical operation and a re-entry pass requires one, the switching-energy ratio is $3$, with uncertainty inherited from $k$; if $k$ were $2$, the ratio would be $2$, and if $k$ were $5$, it would be $5$.
- **R5 (uncertainty band).** A twofold uncertainty in $c_p$ maps to $R \in [1.5625,\, 6.25]$; the sign of the advantage is robust only while $c_p < 0.625\ \mathrm{cu}$.

## 6. Discussion

**What the comparison does and does not show.** The models compare switching effort per logical operation, not total system cost, accuracy, programmability, or verification cost. The ratio $R = 3.125$ is a property of the assumed parameters, not of the architectures; its role is to isolate the single parameter, $c_p$, on which the re-entry proposal's economic case turns.

**Limitations.** First, the parameter set is illustrative. The QNFO record [12] supplies no quantitative data (its summary field is empty), so no parameter can be anchored to the source proposal; the entire quantitative content of this paper rests on the declared assumptions of Section 3. Second, the models assume the re-entry loop is *given*: as [4] shows, deciding whether a 4-local Hamiltonian's dynamics mixes so that the trajectory actually re-enters the useful region is PSPACE-hard, so the setup cost $C_s$ may in practice include an intractable verification step that our model does not price. Third, the per-pass cost $c_p$ is not free physics: by the bound of [7], traversing a loop of nonzero geometric length requires a path integral of energy uncertainty at least proportional to that length, so $c_p$ has a dynamical floor that our illustrative value of $0.2\ \mathrm{cu}$ may violate for long loops; this is precisely the regime ($L$ near $L^{*} = 12.5$) where the advantage collapses. Fourth, the von Neumann side is modeled generously: real fetch–decode–execute pipelines amortize fetch across superscalar issue, so effective $C_{\mathrm{vN}}$ per operation can be below $2.5\ \mathrm{cu}$, which lowers $c_p^{*}$ proportionally. Fifth, readout and error correction are unpriced in Model R; a hybrid classical–quantum coupling of the kind discussed in [8] would add controller-like costs back into the re-entry regime, eroding the distinction the comparison rests on.

**Failure modes.** If re-entry loops must be re-initialized every few cycles (small effective $n$), the amortization result R2 flips the sign of the comparison: below $n \approx 5.88$ cycles of reuse, the explicit controller wins. If the per-pass cost scales with system size (e.g. $c_p \propto L$ rather than constant), then $C_{\mathrm{re}} \propto L^2$ and the advantage disappears for any nontrivial loop.

**What would falsify the claims.** The central claim — that re-entry can undercut von Neumann switching cost — is falsified empirically if measured per-pass switching costs in any concrete Hamiltonian substrate exceed $c_p^{*} = 0.625$ of the corresponding fetch–decode–execute cost, or if practical reuse factors stay below $n^{*} \approx 5.88$. It is falsified theoretically if the geometric energy bound of [7] forces $c_p$ to grow linearly with $L$ in a way that violates the threshold for all useful loop lengths.

**Open questions.** (i) What is the true dynamical floor of $c_p$ for a given Hamiltonian loop, and can the NSO formalism of [5], [6] — which treats irreversibility emerging from reversible Hamiltonian dynamics — supply a first-principles value? (ii) Can Koopman-von Neumann embeddings [3] turn re-entry loops into executable quantum circuits, and does the embedding preserve the cost advantage or pay it back in state-preparation? (iii) Does the Gibbs-von Neumann entropy grounding of [1] constrain how much work a re-entry cycle can extract per pass, i.e. is there an entropy-based lower bound on $c_p$? (iv) Can network-isomorphism methods of the kind named in [13] certify equivalence of re-entry loop structures cheaply enough to keep $C_s$ bounded? (v) Does the Backus vicious circle of [11] apply to re-entry computation, i.e. is there any language in which re-entry programs can even be expressed without collapsing back to von Neumann semantics? The neuromorphic literature [9] suggests biological inspiration can be measured against von Neumann energy budgets; whether Hamiltonian re-entry can be so measured at all remains the gating question.

## 7. Conclusion

Framing the QNFO re-entry proposal [12] against von Neumann switching costs reduces the architecture debate to a small parameter set: per-pass cost $c_p$, loop length $L$, setup cost $C_s$, and reuse count $n$. With illustrative parameters, re-entry shows a per-cycle switching-cost advantage of $R = 3.125$, an amortization break-even at $n^{*} \approx 5.88$ cycles, and a fragility threshold at $c_p^{*} = 0.625\ \mathrm{cu}$ — a quarter of the modeled von Neumann per-operation cost. The advantage is real but conditional, and the conditions (cheap autonomous passes, long reuse, verifiable recurrence) are exactly where the hardest open problems lie, from the PSPACE-hardness of mixing [4] to the unresolved irreversibility gap [5], [6] and the hybrid-dynamics problem [8]. The contribution of this paper is not a verdict but a falsifiable parameterization: measuring $c_p$, $C_s$, and achievable $n$ in any concrete Hamiltonian substrate would settle the comparison this paper can only frame.

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

[10] arXiv:1308.4280v1