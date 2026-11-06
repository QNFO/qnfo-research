# Adelic Quantum Error Correction: A Synthesis Across All Primes v1.0.0

## Abstract

The $p$-adic quantum error correction program has developed three independent but connected strands: a mathematical theory of $p$-adic stabilizer codes (Phase A), an experimental protocol to test for ultrametric error structure (Phase B), and a hardware co-design proposal for tree-structured qubit layouts (Phase C). These strands share a common origin in the ultrametric geometry of the $p$-adic numbers $\mathbb{Q}_p$, but they treat each prime $p$ in isolation. Number theory provides a deeper unification: the adele ring $\mathbb{A}$, which stitches together all completions of $\mathbb{Q}$ — the real numbers $\mathbb{R}$ (Archimedean) and all $p$-adic fields $\mathbb{Q}_p$ (non-Archimedean) — into a single locally compact topological ring. The adelic product formula $\prod_{p \leq \infty} |x|_p = 1$ implies that contributions from all primes are balanced: what is gained in one completion is lost in another. We propose that quantum error correction should be formulated on the adele ring rather than on any single completion. In this framework, a physical qubit lives in real (Archimedean) spacetime but its errors exhibit ultrametric structure across a hierarchy of primes. The adelic QEC program synthesizes Phases A–C into a unified architecture: $p$-adic codes at each prime protect against hierarchical errors, a real (Archimedean) surface code protects against local errors, and the adelic product formula governs the trade-off between them. We sketch the construction of adelic stabilizer codes over $\mathbb{A}^n$, formulate the adelic code distance as a function of the local distances at each completion, and discuss the physical interpretation: errors in quantum systems may span multiple primes, reflecting deeper arithmetic structure in quantum dynamics.

# 1. Introduction

The $p$-adic quantum error correction program has now reached a point where synthesis is possible. Phase A [Quni-Gudzinas, 2026a] developed the mathematical theory of $p$-adic stabilizer codes, proving that these codes have automatic hierarchical concatenation and deriving $p$-adic quantum bounds. Phase B [Quni-Gudzinas, 2026b] designed an experimental protocol to measure the ultrametricity index $\mathcal{U}_p$ on quantum hardware. Phase C [Quni-Gudzinas, 2026c] proposed $p$-adic qubit layouts — tree-structured connectivity graphs that are structurally matched to $p$-adic codes.

Each of these phases treats a single prime $p$. But number theory tells us that the rational numbers $\mathbb{Q}$ are not completed at a single prime — they are completed at all primes simultaneously. The **adele ring** $\mathbb{A}$ is the restricted direct product of all completions:

$$\mathbb{A} = \mathbb{R} \times \prod_{p \text{ prime}}' \mathbb{Q}_p$$

where the product is restricted: for all but finitely many primes, the component belongs to the $p$-adic integers $\mathbb{Z}_p$. The adele ring is a locally compact topological ring that encodes the behavior of rational numbers at every completion — real (Archimedean) and $p$-adic (non-Archimedean) — in a single object.

The central identity of adelic number theory is the **product formula**: for any nonzero $x \in \mathbb{Q}$,

$$\prod_{p \leq \infty} |x|_p = 1$$

where $|\cdot|_\infty$ is the ordinary real absolute value and $|\cdot|_p$ is the $p$-adic absolute value. This formula expresses a deep reciprocity: contributions from the Archimedean place and all non-Archimedean places exactly balance.

We propose that this balance has physical significance for quantum error correction. A physical qubit is embedded in real spacetime — its dynamics are described by real-time Schrödinger evolution, and its spatial layout is Archimedean. But its *errors* — the environmental interactions that cause decoherence — may carry ultrametric structure, as the metric mismatch hypothesis proposes. The adelic product formula suggests that these two aspects — the real dynamics and the $p$-adic error structure — are not independent. They are linked by an arithmetic reciprocity that constrains the allowable error patterns.

This paper develops the **adelic quantum error correction** framework. We construct adelic stabilizer codes over $\mathbb{A}^n$, define an adelic code distance that combines Archimedean and $p$-adic contributions, and propose an adelic concatenation scheme in which a real surface code protects against local Archimedean errors while $p$-adic codes at each prime protect against hierarchical ultrametric errors. The full architecture is speculative — it depends on the experimental confirmation of ultrametric error structure — but it provides a unified mathematical framework that connects the three independent strands of the $p$-adic QEC program.

# 2. The Adele Ring and Its Physical Interpretation

## 2.1 Mathematical Definition

The adele ring $\mathbb{A}$ is defined as:

$$\mathbb{A} = \left\{(x_\infty, x_2, x_3, x_5, \ldots) \,\middle|\, x_\infty \in \mathbb{R}, \; x_p \in \mathbb{Q}_p \text{ for all } p, \text{ and } x_p \in \mathbb{Z}_p \text{ for almost all } p \right\}$$

Addition and multiplication are component-wise. The topology is the restricted product topology: a basis of open sets is given by products $\prod_{p \leq \infty} U_p$ where each $U_p$ is open and $U_p = \mathbb{Z}_p$ for almost all $p$.

The **idele group** $\mathbb{A}^\times$ is the group of invertible adeles. The product formula $\prod |x|_p = 1$ is the statement that the map $x \mapsto \prod |x|_p$ is trivial on the principal ideles (the diagonal embedding of $\mathbb{Q}^\times$).

## 2.2 Physical Interpretation

We propose the following physical interpretation of the adelic structure:

| Mathematical Object | Physical Interpretation |
|:-------------------|:------------------------|
| $\mathbb{R}$ (Archimedean completion) | Real spacetime — the arena of Schrödinger evolution, gate operations, and local (Hamming) errors |
| $\mathbb{Q}_p$ ($p$-adic completion) | Ultrametric error space at prime $p$ — hierarchical structure of correlated errors |
| $\mathbb{Z}_p$ ($p$-adic integers) | The "integer" errors — regular, well-behaved errors within the $p$-adic hierarchy |
| $\mathbb{A}$ (adele ring) | The full error + dynamics space — a unified description of quantum behavior across all completions |
| Product formula | A reciprocity constraint: the total "error content" across all completions is conserved |

Under this interpretation, the product formula states that a quantum system cannot have arbitrary error structure at all primes simultaneously. If errors exhibit strong ultrametric structure at prime $p$ (large $|x|_p$), they must be compensated by either weaker structure at other primes or by reduced error rates in real spacetime ($|x|_\infty$). This is a *conservation law for error structure* — speculative, but mathematically natural in the adelic framework.

# 3. Adelic Hilbert Spaces

## 3.1 Local Hilbert Spaces

We define Hilbert spaces at each completion:

- **Archimedean Hilbert space:** $\mathcal{H}_\infty = L^2(\mathbb{R}^n, d^n x)$, the standard Hilbert space for $n$ continuous-variable quantum systems, or $\mathcal{H}_\infty = (\mathbb{C}^d)^{\otimes m}$ for $m$ qudits embedded in real spacetime.

- **$p$-adic Hilbert space:** $\mathcal{H}_p = L^2(\mathbb{Q}_p^n, d\mu_p)$, where $d\mu_p$ is the Haar measure on $\mathbb{Q}_p^n$, normalized so that $\mathbb{Z}_p^n$ has measure 1. For finite truncations, $\mathcal{H}_p \cong \mathbb{C}^{p^{kn}}$ for some $k$.

The local Hilbert space at completion $v$ (where $v \in \{\infty, 2, 3, 5, \ldots\}$) is denoted $\mathcal{H}_v$.

## 3.2 Adelic Hilbert Space

The **adelic Hilbert space** is the restricted tensor product:

$$\mathcal{H}_{\mathbb{A}} = \bigotimes_{v \leq \infty}' \mathcal{H}_v$$

where the restriction is with respect to a distinguished "vacuum vector" $\Omega_v \in \mathcal{H}_v$ at each completion. For almost all $v$, the state is in the vacuum: only finitely many completions carry nontrivial quantum information.

Physically, this means: a quantum computation involves qubits at finitely many primes. Most primes are "quiescent" — they carry no errors and no information. The restricted tensor product formalizes the idea that only a finite error hierarchy (finite tree depth) is active at any given time.

## 3.3 The Vacuum at Each Prime

The choice of vacuum $\Omega_v$ is physically significant:

- **At $\infty$:** $\Omega_\infty$ is the ground state of the physical qubit — the logical $|0\rangle$ state prepared by initialization.
- **At $p$:** $\Omega_p$ is the "no-error" state at that prime — the state in which no $p$-adic hierarchical errors have occurred.

An error is a transition away from the vacuum at one or more primes. A *local* error (bit flip, phase flip) is a transition at $\infty$ only. A *hierarchical* error is a transition at some $p$ (or multiple primes). A *mixed* error involves both $\infty$ and non-Archimedean primes.

# 4. Adelic Stabilizer Codes

## 4.1 Product Structure

An **adelic stabilizer code** is defined by specifying a stabilizer group $\mathcal{S}_v$ at each completion $v \leq \infty$, with the adelic stabilizer being the restricted direct product:

$$\mathcal{S}_{\mathbb{A}} = \prod_{v \leq \infty}' \mathcal{S}_v$$

The code subspace is:

$$\mathcal{C}_{\mathbb{A}} = \{\psi \in \mathcal{H}_{\mathbb{A}} : S\psi = \psi \text{ for all } S \in \mathcal{S}_{\mathbb{A}}\}$$

For almost all $v$, $\mathcal{S}_v$ is trivial (no encoding at that prime). For the active primes, $\mathcal{S}_v$ is a $p$-adic stabilizer group as defined in Phase A.

## 4.2 Adelic Code Distance

The **adelic code distance** $\Delta$ is a function of the local distances at each completion. We define:

$$\Delta = \min_{L \in \mathcal{N}(\mathcal{S}_{\mathbb{A}})\setminus\mathcal{S}_{\mathbb{A}}} \prod_{v \leq \infty} \|L_v\|_v$$

where $\mathcal{N}(\cdot)$ is the normalizer, $L_v$ is the component of the logical operator $L$ at completion $v$, and $\|\cdot\|_v$ is the appropriate norm:

- $v = \infty$: Hamming weight (standard code distance $d$)
- $v = p$: $p$-adic weight $\|P\|_p = \max(|a|_p, |b|_p)$ as defined in Phase A

The product structure reflects the adelic philosophy: protection must be provided at ALL active completions simultaneously. A code is only as strong as its weakest completion.

## 4.3 Adelic Product Bound

In analogy with the product formula, we conjecture an **adelic quantum bound**:

$$\prod_{v \leq \infty} \left(\frac{\dim \mathcal{C}_v}{p_v^{n_v}}\right) \leq \text{constant}$$

where $\dim \mathcal{C}_v$ is the logical dimension at completion $v$, $p_v$ is the local qudit dimension, and $n_v$ is the number of physical registers. This bound would express a trade-off: you cannot maximally encode at all primes simultaneously; increasing the encoding rate at one prime forces a decrease at another.

This is `[my conjecture]`. It has not been proven, but it is the natural adelic generalization of the quantum Singleton bound.

# 5. Adelic Concatenation

## 5.1 Two-Level Architecture

We propose a practical **two-level adelic architecture**:

- **Level 1 (Archimedean — real spacetime):** A conventional surface code or LDPC code protects against local, Hamming-weight errors. This is the "outer code" operating in real time on physical qubits in Euclidean space.

- **Level 2 (Non-Archimedean — adelic primes):** $p$-adic stabilizer codes at finitely many primes protect against hierarchical, ultrametric errors. These are the "inner codes" operating on the $p$-adic completions of the error space.

The two levels are concatenated: the logical qubits of the $p$-adic inner codes become the physical qubits of the Archimedean outer code. This is the **adelic concatenation**.

## 5.2 Which Primes?

Which primes should be active in an adelic QEC architecture? The answer is empirical — determined by Phase B measurements of $\mathcal{U}_p$:

- If $\mathcal{U}_p > 0$ is significant for prime $p$, that prime is **active**: the hardware exhibits ultrametric error structure at that $p$, and a $p$-adic inner code is warranted.
- If $\mathcal{U}_p \approx 0$ for all $p$, only the Archimedean level is needed — the architecture reduces to conventional QEC.
- If $\mathcal{U}_p > 0$ for multiple primes, the architecture activates multiple $p$-adic inner codes, one at each active prime.

The adelic product formula suggests that the $\mathcal{U}_p$ values across different primes are not independent. If $\mathcal{U}_2$ is large, $\mathcal{U}_3$ may be constrained to be smaller, and vice versa. Testing this prediction requires measuring $\mathcal{U}_p$ for multiple primes on the same hardware — an extension of the Phase B protocol.

## 5.3 Physical Realization

In practice, the adelic architecture operates as follows:

1. **Physical qubits** are laid out in a $p$-adic tree structure (Phase C). The tree provides the hardware connectivity for $p$-adic inner codes.
2. **Syndrome extraction** proceeds hierarchically within each $p$-adic tree, generating syndrome data for the inner codes.
3. **The $p$-adic decoder** (Phase A, §6) corrects hierarchical errors, producing clean logical qubits at the root of each tree.
4. **These clean logical qubits** are then used as the physical qubits for an Archimedean surface code, which provides additional protection against any remaining local (Hamming-weight) errors.

The surface code operates on the *output* of the $p$-adic inner codes. This inverts the usual concatenation order (where inner codes are deeper) — a distinctive feature of adelic QEC.

# 6. The Feynman-Shor Program in Adelic Perspective

The Phase A paper [Quni-Gudzinas, 2026a] identified a bifurcation: Feynman's vision (quantum simulation) vs. Shor's application (cryptanalysis). The adelic framework clarifies this distinction.

Quantum simulation tasks — simulating lattice gauge theories, quantum chemistry, or condensed matter systems — naturally involve hierarchical (renormalization-group) structure. The simulated systems have dynamics at multiple length scales, which correspond to multiple adelic primes. In the adelic picture, these are tasks where **multiple primes are active**, and the natural error structure of the hardware (ultrametric, multi-prime) is *matched* to the computational task. The overhead of adelic QEC is amortized by the structure of the computation.

Cryptanalytic tasks — factoring integers with Shor's algorithm, computing discrete logarithms — are "flat" in the adelic sense: they involve only the Archimedean completion (real-time modular arithmetic on a flat circuit). There is no natural hierarchical structure. In the adelic picture, these tasks **activate only the Archimedean prime**, and the ultrametric error structure of the hardware is *mismatched* to the computation. The adelic overhead is not amortized — it becomes pure cost.

This provides a mathematical rationale for the Feynman-Shor bifurcation: simulation tasks match the hardware's adelic profile; cryptanalytic tasks do not. The first useful quantum computer will run simulation not because of engineering preference, but because of arithmetic necessity.

# 7. Adelic Product Formula as an Error Budget

We now explore the most speculative consequence of the adelic framework: the interpretation of the product formula as an **error budget constraint**.

## 7.1 Statement

For a quantum system with $m$ physical qubits, define the **error content** at completion $v$ as:

$$\mathcal{E}_v = -\log \|E_v\|_v$$

where $E_v$ is the error operator at completion $v$ and $\|E_v\|_v$ is its norm. Then, for any error process that respects the arithmetic structure of $\mathbb{Q}$ (a hypothesis requiring physical justification), the adelic product formula implies:

$$\sum_{v \leq \infty} \mathcal{E}_v = 0$$

In other words: if an error has nonzero ultrametric content at some prime $p$ ($\mathcal{E}_p > 0$), it must have negative Archimedean content ($\mathcal{E}_\infty < 0$), meaning that the Archimedean (local) error rate is *reduced*. Conversely, suppressing local errors (making $\mathcal{E}_\infty$ more negative) forces hierarchical errors to become more prominent (increasing $\mathcal{E}_p$ for some $p$).

## 7.2 Testable Prediction

This interpretation makes a strong, testable prediction: **improving local gate fidelity should increase the ultrametricity index $\mathcal{U}_p$.** If you reduce the depolarizing error rate per gate (suppressing Archimedean errors), the hierarchical ultrametric error structure should become *more* visible — because the product formula requires that the total error content be conserved.

This prediction can be tested by repeating the Phase B protocol on the same hardware at different gate fidelities (e.g., by varying pulse optimization or operating temperature) and measuring $\mathcal{U}_p$ as a function of physical error rate. If $\mathcal{U}_p$ increases as $p_{\text{phys}}$ decreases, the adelic product formula interpretation is supported.

This would be disconfirmed if $\mathcal{U}_p$ is independent of physical error rate, or if it decreases with improved fidelity.

# 8. Discussion

## 8.1 Status of the Program

The $p$-adic QEC program now spans theory, experiment, hardware, and synthesis:

| Phase | Domain | Key Result | Status |
|:------|:-------|:-----------|:-------|
| A | Theory | $p$-adic stabilizer codes, concatenation theorem, bounds | Published |
| B | Experiment | Ultrametricity index protocol, power analysis | Protocol published; awaiting hardware data |
| C | Hardware | Bruhat-Tits tree layouts, platform implementations | Published |
| D | Synthesis | Adelic QEC framework, product formula constraint | Published (this paper) |

The program is now complete as a theoretical edifice. The next steps are experimental: measure $\mathcal{U}_p$ on quantum hardware (Phase B), test the time-reversal test ($\mathcal{U}_p$ vs. $p_{\text{phys}}$), and if results are positive, build the 15-qubit $p$-adic prototype (Phase C).

## 8.2 Relationship to Other Approaches

- **Standard QEC:** The $\mathbb{R}$-only limit of adelic QEC. When $\mathcal{U}_p = 0$ for all $p$, the adelic framework reduces to conventional QEC on Archimedean spacetime.
- **Topological QEC:** The adelic framework is not opposed to topological codes. A surface code can serve as the Archimedean outer code in the adelic concatenation. The adelic framework adds *additional* protection against ultrametric errors at the non-Archimedean primes.
- **Holographic QEC:** The AdS/CFT correspondence relates gravitational theories in anti-de Sitter space to conformal field theories on the boundary. The adelic framework has a formal analogy: the real (Archimedean) boundary theory (the physical qubits) is dual to a $p$-adic bulk (the error hierarchy). The analogy is suggestive but `[not yet falsifiable]` in QEC.

## 8.3 Limitations and Open Questions

1. **Which primes are physically realized?** The adelic framework treats all primes symmetrically, but physics may select a finite subset. The primes $p=2$ (binary hierarchy) and $p=3$ (ternary) are the most natural candidates for near-term testing.

2. **Adelic dynamics:** We have described adelic *codes* but not adelic *dynamics* — the time evolution of quantum states in the adelic Hilbert space. Developing an adelic Schrödinger equation or adelic quantum circuit model is an open problem.

3. **Mathematical rigor:** The adelic code distance, product bound, and error budget constraint are `[my conjecture]`. Rigorous proofs require developing the full theory of adelic operator algebras and adelic quantum information theory.

4. **Experimental accessibility:** The adelic product formula prediction ($\mathcal{U}_p$ vs. $p_{\text{phys}}$) is falsifiable with current hardware. This is the most urgent experimental test of the framework.

# 9. Conclusion

We have synthesized the three independent strands of the $p$-adic QEC program into a unified adelic framework. The adele ring $\mathbb{A}$ provides the natural mathematical setting for quantum error correction when errors may carry ultrametric structure: it treats all completions of $\mathbb{Q}$ — Archimedean (real spacetime) and non-Archimedean ($p$-adic error hierarchies) — within a single locally compact topological ring.

The adelic product formula $\prod |x|_p = 1$ acquires physical significance as a constraint on error structure: the contributions from local (Archimedean) and hierarchical (non-Archimedean) errors must balance. This predicts that improving local gate fidelity will make ultrametric error structure MORE visible — a falsifiable prediction testable with current hardware.

The $p$-adic QEC program is now complete as a theoretical framework. Phases A through D form a coherent arc: from mathematical foundations, through experimental protocols and hardware co-design, to arithmetic synthesis. The structure is in place. The experimental tests — the ultrametricity measurements of Phase B — will determine whether this structure describes physical reality or remains a mathematical curiosity.

Either outcome is valuable. If $\mathcal{U}_p > 0$, quantum error correction must be reformulated on adelic foundations. If $\mathcal{U}_p \approx 0$, the Archimedean assumptions of conventional QEC are validated, and the adelic framework provides a rigorous bound on how non-Archimedean quantum errors *could* have been but are not.

---

*Certainty: The adele ring and product formula are `[established]` number theory. The physical interpretation is `[speculative]`. The adelic stabilizer code construction is `[my conjecture]`. The adelic product bound is `[my conjecture, not proven]`. The error budget constraint and its falsifiable prediction ($\mathcal{U}_p$ vs. $p_{\text{phys}}$) are `[my conjecture, falsifiable]`. The Feynman-Shor interpretation in adelic terms is `[speculative]`.*

---

*This paper completes Phase D of the $p$-adic Quantum Error Correction program. Phase A: Quni-Gudzinas (2026a), "Toward $p$-adic Quantum Error Correction." Phase B: Quni-Gudzinas (2026b), "Testing for Ultrametric Error Structure in Quantum Hardware." Phase C: Quni-Gudzinas (2026c), "$p$-adic Quantum Hardware: Qubit Layouts for Ultrametric Error Correction." Phase D: the present paper.*
