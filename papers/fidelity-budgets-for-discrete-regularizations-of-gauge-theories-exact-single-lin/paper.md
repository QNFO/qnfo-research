# Fidelity Budgets for Discrete Regularizations of Gauge Theories: Exact Single-Link Computations, Scaling Laws, and the Limits of Heuristic Bounds

## Abstract

Discrete regularizations of gauge theories — finite-dimensional link Hilbert spaces in quantum link models, truncated electric bases on quantum registers, and tensor networks on Bruhat–Tits trees — all face the same structural question: when does the discrete object faithfully encode its continuum or infinite-dimensional target? We develop a unified fidelity-budget framework that decomposes a target accuracy $\epsilon = 10^{-4}$ into per-component truncation errors with explicit scaling laws. As a fully worked case study, we compute exactly, with all arithmetic shown, the truncation infidelity and energy bias of a single thermal $\mathrm{U}(1)$ link at dimensionless inverse temperature $\beta g^2 = 0.5$: the infidelity falls from $1.150 \times 10^{-2}$ at $n_{\max}=3$ to $7.242 \times 10^{-5}$ at $n_{\max}=5$ and $6.44 \times 10^{-8}$ at $n_{\max}=7$, while the register cost grows only from 3 to 4 qubits. We document, in an explicit divergence appendix, why a competing heuristic bound proposed in an independent draft fails algebraic scrutiny and was rejected.

## 1. Introduction

A gauge theory is not directly what an experiment builds. Whether the platform is a quantum simulator of synthetic matter, a gate-based quantum computer, or a tensor-network code, the theory must first be regularized: the continuum gauge field replaced by a finite-dimensional Hilbert space per link, the continuum geometry replaced by a discrete graph. The central fidelity question is then always the same. Given a discrete regularization $R$ of a target theory $T$, and a tolerance $\epsilon$, does the regularized dynamics agree with the target dynamics to within $\epsilon$ on the observables of interest — and if not, what exactly must be increased, and by how much?

This question has been posed independently in several communities. In quantum link models (QLMs) — gauge theories whose link Hilbert spaces are finite-dimensional representations rather than the infinite-dimensional Kogut–Susskind spaces — the question of when the genuine quantum-field-theory limit is reached has been analyzed for far-from-equilibrium dynamics [1]. In trapped-ion quantum computers, the recent observation of genuine $2+1$D string dynamics in a $\mathrm{U}(1)$ lattice gauge theory with a tunable plaquette term demonstrates that dynamical phenomena absent in one dimension can now be accessed, but only after the gauge field is truncated on every link [2]. A formalism for estimating truncation uncertainties against the Kogut–Susskind limit, leveraging Hilbert-space fragmentation to bound the excitation of large electric fields, has been developed precisely to make these errors quantitative [3]. In a different corner of the literature, holographic quantum error correction has been organized as renormalization-group (RG) flow on the Bruhat–Tits tree $\mathcal{T}_p$ — the $p$-adic analogue of anti-de Sitter space — with a conditional threshold analysis at accuracy $10^{-4}$ [9], building on the identification of the tree as a holographic geometry [11].

This paper is the reconciled product of three independent analyses of the same input corpus. The three drafts agreed on the framework's structure but diverged on the central quantitative object: one draft proposed a heuristic closed-form bound $\epsilon_{S,a} \le \frac{g^2 a^2}{2S+1}$ for spin-$S$ quantum link truncations; the other two performed exact or model-based computations whose assumptions are fully stated. As we show in Section 4 and document in Appendix A, the heuristic bound does not survive algebraic scrutiny — the derivation contains an unjustified step — and the reconciled paper therefore adopts the exact computations as its quantitative core, while retaining the heuristic as a documented, rejected alternative. The contribution that survives reconciliation is threefold:

1. **A fidelity-budget framework** (Section 3): a decomposition of total admissible error $\epsilon$ into per-component truncation errors, with scaling laws converting a budget into hardware requirements (truncation levels, qubit counts, tree depths).
2. **An exact single-link case study** (Sections 4.1–4.2): the truncation infidelity and energy bias of a thermal $\mathrm{U}(1)$ link, computed term by term with every input stated.
3. **Scaling laws and a tree application** (Sections 4.3–4.5): the logarithmic cost of multi-link propagation, the Gaussian-versus-Chebyshev gap, and Bruhat–Tits tree geometry at $p=2$, $L=10$.

Our thesis: the gap between "the regularization is faithful" and "it is not" is logarithmic in the accuracy on the side of informed (dynamics-aware) bounds, and polynomial on the side of uninformed bounds — and every quantitative claim in between must carry shown arithmetic to be physics.

## 2. Background and Related Work

We review the twelve works of the bibliography, indicating how each enters the framework.

**[1] Achieving the quantum field theory limit in far-from-equilibrium quantum link models (arXiv:2112.04501v3).** This work asks when quantum link model realizations of gauge theories in quantum synthetic matter reach the genuine quantum-field-theory limit, with attention to far-from-equilibrium dynamics where naive adiabatic continuity arguments fail. It is the closest structural antecedent to our question: a finite-dimensional regularization must be shown to reproduce continuum observables. Our fidelity budget supplies the quantitative instrument such analyses need — a per-link error tolerance derived from a total budget, so that "reaching the limit" becomes a checkable inequality rather than a qualitative comparison.

**[2] Observation of genuine $2+1$D string dynamics in a U(1) lattice gauge theory with a tunable plaquette term on a trapped-ion quantum computer (arXiv:2604.07436v1).** This experiment demonstrates string dynamics relevant to hadronization in $2+1$ dimensions, where a plaquette term endows the gauge field with dynamics and enables photon-like propagation. The plaquette term is also the main new source of truncation sensitivity relative to $1+1$D: magnetic energy involves products of link operators around a loop, so truncation errors on different links coherently enter the same term. Our budget in Section 4.4 treats the 4-link plaquette as the coherence multiplier for magnetic-sector errors.

**[3] Truncation uncertainties for accurate quantum simulations of lattice gauge theories (arXiv:2508.00061v4).** This work develops a formalism for estimating truncation errors incurred when the gauge field's Hilbert space on each link is discretized, exploiting Hilbert-space fragmentation in the electric basis, which limits the excitation of large electric fields. This is the direct quantitative ancestor of our Section 4: we adopt its logic that dynamics-aware bounds on the reachable electric-flux sector convert into dramatically smaller required truncation levels, and we make the comparison against dynamics-unaware bounds explicit with shown arithmetic.

**[4] A change of perspective: switching quantum reference frames via a perspective-neutral framework (arXiv:1809.00556v4).** This work treats reference frames as quantum systems and relates descriptions relative to different quantum reference frames through a perspective-neutral framework. Its relevance is conceptual: the "target theory" $T$ of a regularization is only defined relative to a choice of frame, and a truncation that is harmless in one frame (e.g., the electric basis) may be nonlocal and severe in another. Our budget is therefore frame-dependent, a limitation we flag in Section 6.

**[5] An axiomatic approach to quantum gauge field theory (arXiv:hep-th/9511122v1).** This constructive proposal formulates Osterwalder–Schrader-like axioms for the characteristic functional of a measure on the space of generalized connections modulo gauge transformations. It supplies the continuum-side definition of the target $T$: a regularization is faithful if the pushforward of the regularized measure through the coarse-graining map converges to such a measure. Our budget is an operational, finite-$\epsilon$ version of this convergence requirement.

**[6] A groupoidal approach to quantum reference frames (arXiv:2608.14133v1).** This work develops groupoid-based relational quantum field theory on curved spacetimes, where global symmetry groups are absent or too small for the group-based quantum reference frame formalism. On curved or $p$-adic backgrounds [9, 11] there is no global gauge group with respect to which truncation errors can be gauge-averaged; the groupoidal perspective suggests that the budget must be assigned locally, per vertex or per edge, which is exactly how we proceed.

**[7] SU_q(n) Gauge Theory (arXiv:hep-th/9601033v2).** This work defines a field theory with local quantum-group $\mathrm{SU}_q(n)$ transformations on a classical spacetime, with gauge potentials in a quantum Lie algebra. It is a useful limiting case: the deformation parameter $q$ acts as a one-parameter family of regularizations of the classical gauge algebra, and the fidelity question becomes the $q \to 1$ limit. Our budget applies verbatim with $\epsilon$ measuring deviation of correlators from their $q=1$ values.

**[8] Quantum Energy Inequalities and Stability Conditions in Quantum Field Theory (arXiv:math-ph/0502002v1).** This review connects quantum energy inequalities (QEIs) to microscopic and mesoscopic stability of quantum field theory, bounding the magnitude and duration of negative energy excitations. QEIs bound the tail of the energy distribution that a truncation must capture — precisely the input our Gaussian model in Section 4.3 needs: a physically motivated bound on the flux variance $\sigma^2$, supplied by a stability condition on the target theory rather than by assumption alone.

**[9] Holographic Quantum Error Correction as AdS/CFT Renormalization-Group Flow on Bruhat–Tits Trees: A Conditional Threshold Analysis at $10^{-4}$ (https://papers.qnfo.org/papers/holographic-quantum-error-correction-as-ads-cft-renormalization-group-flow-on-br/).** This work analyzes quantum error correction organized as RG flow on the Bruhat–Tits tree $\mathcal{T}_p$, with the encoding map of a holographic code literally an RG trajectory, and states a conditional threshold at accuracy $10^{-4}$. We adopt the same target accuracy and, in Section 4.5, compute the tree-geometry quantities (boundary vertex counts, edge counts, qubit-equivalent costs) that such a threshold analysis requires as inputs.

**[10] The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing $p$-Adic Structure in Quantum Dynamics (https://papers.qnfo.org/papers/trapped-ion-ultrametric-synthesis/).** This register organizes sixteen published records from a single research program into one testable claim: that trapped-ion quantum simulators are the first near-term platform on which ultrametric ($p$-adic) structure in quantum dynamics can be accepted or rejected by measurement. It supplies the experimental side of our framework: the fidelity budget is exactly the kind of pre-registered, auditable numerical structure that a falsifiability register needs, and the platform overlap with [2] makes a combined test realistic.

**[11] Holographic QEC as AdS/CFT RG Flow on Bruhat–Tits Trees (DOI pending).** This work completes a trilogy by showing that the Bruhat–Tits tree $\mathcal{T}_p$ is the $p$-adic analog of anti-de Sitter space and that tensor networks on $\mathcal{T}_p$ are holographic. It provides the geometric identification that makes our tree-count computations in Section 4.5 physically meaningful rather than merely combinatorial.

**[12] The Adelic Cross-Domain Program: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees (https://papers.qnfo.org/papers/adelic-cross-domain/).** This program connects fine-structure constants and Standard Model mass ratios through Bruhat–Tits tree structures, with a documented v3.2 correction pass in which arithmetic errors in mass-ratio triplets were corrected (5 of 9 verified independently) and an "honest structural correspondence" standard was adopted. Its methodological lesson directly shapes this paper: every quantitative claim must carry shown arithmetic and an explicit verification status, which is the standard we enforce in Sections 4 and 5 — and which, as Appendix A documents, is the standard by which one draft's heuristic bound was rejected.

## 3. Methods

### 3.1 The fidelity budget

Let $R$ be a discrete regularization of a target theory $T$, and let $\mathcal{O}$ be a set of observables on which agreement is demanded. We define the fidelity budget as the constraint

$$
\Delta_R(T;\mathcal{O}) \;=\; \sup_{O \in \mathcal{O}} \big| \langle O \rangle_R - \langle O \rangle_T \big| \;\le\; \epsilon,
$$

where $\epsilon$ is the target accuracy. We take $\epsilon = 10^{-4}$ throughout, matching the conditional threshold of [9]. The budget is decomposed as

$$
\epsilon \;=\; \epsilon_{\text{trunc}} + \epsilon_{\text{dyn}} + \epsilon_{\text{impl}},
$$

where $\epsilon_{\text{trunc}}$ is the error from finite link Hilbert spaces (or finite tree depth), $\epsilon_{\text{dyn}}$ the error from finite evolution time or finite RG depth, and $\epsilon_{\text{impl}}$ the implementation error (gate noise, readout). This paper isolates $\epsilon_{\text{trunc}}$; the other terms are reserved for future work and are not assigned numbers here.

### 3.2 Truncation model for the electric sector

On each link, the electric basis $\{|\ell\rangle\}_{\ell \in \mathbb{Z}}$ carries flux quanta with electric energy $E(\ell) = \tfrac{g^2}{2}\ell^2$ (Kogut–Susskind convention). A truncation keeps $|\ell| \le \ell_{\max}$, i.e., $n_{\text{states}} = 2\ell_{\max}+1$ states per link, encoded in

$$
q \;=\; \left\lceil \log_2\!\left(2\ell_{\max}+1\right) \right\rceil
$$

qubits per link. The truncation error is the total probability weight outside the kept sector,

$$
\epsilon_{\text{link}} \;=\; \sum_{|\ell| > \ell_{\max}} P(\ell),
$$

where $P(\ell)$ is the electric-flux distribution of the state being simulated.

### 3.3 Two models for $P(\ell)$

**Model G (Gaussian).** If the electric flux is approximately Gaussian with variance $\sigma^2$ — motivated by QEI-type stability conditions on the target theory [8] — then the two-sided tail is

$$
\epsilon_{\text{link}} \;\approx\; 2\,\exp\!\left(-\frac{\ell_{\max}^2}{2\sigma^2}\right).
$$

**Model C (Chebyshev, distribution-free).** With only the variance known,

$$
\epsilon_{\text{link}} \;\le\; \frac{\sigma^2}{\ell_{\max}^2}.
$$

Model C is the correct bound if nothing is known about the dynamics; Model G is the correct bound if the dynamics is locally stable and mixing in the electric sector. The gap between them is the quantitative value of dynamical information such as fragmentation [3].

### 3.4 Propagation over links

For $N_L$ independent links with per-link error $\epsilon_{\text{link}}$ each, a union bound gives $\epsilon_{\text{trunc}} \le N_L\,\epsilon_{\text{link}}$, so a total budget $\epsilon_{\text{trunc}} \le \epsilon$ requires $\epsilon_{\text{link}} \le \epsilon / N_L$. For coherent (magnetic/plaquette) errors the multiplier is the loop length rather than the link count; we treat the 4-link plaquette of [2] as the smallest such multiplier.

### 3.5 Exact thermal case study

To exhibit what a fully audited budget looks like, we compute the truncation error of a single $\mathrm{U}(1)$ link in the Gibbs state of the electric Hamiltonian

$$
H_{\mathrm{el}} = \frac{g^2}{2} \hat{E}^2, \qquad \hat{E} |n\rangle = n |n\rangle, \quad n \in \mathbb{Z},
$$

at dimensionless inverse temperature $\beta g^2 = 0.5$ (a hot, strongly fluctuating regime chosen so that truncation errors are non-negligible and the budget is informative):

$$
\rho_\beta = \frac{1}{Z}\sum_{n=-\infty}^{\infty} e^{-\frac{\beta g^2}{2} n^2} |n\rangle\langle n|, \qquad Z = \sum_{n=-\infty}^{\infty} e^{-\frac{\beta g^2}{2} n^2}.
$$

With $\beta g^2 = 0.5$ the Boltzmann factor is $e^{-0.25\, n^2}$. We define two metrics for truncation at level $n_{\max}$:

1. **State infidelity** $\epsilon_{\mathrm{tr}}(n_{\max}) = \frac{1}{Z}\sum_{|n| > n_{\max}} e^{-0.25\, n^2}$.
2. **Relative energy bias** $\delta_{\mathrm{E}}(n_{\max}) = \frac{\sum_{|n|>n_{\max}} n^2 e^{-0.25 n^2}}{\sum_{n=-\infty}^{\infty} n^2 e^{-0.25 n^2}}$.

Both are dimensionless and independent of $g$; the temperature enters only through the fixed product $\beta g^2 = 0.5$.

### 3.6 Tree-geometry model for the $p$-adic holographic code

Following [9, 11], the encoding is an RG trajectory on the Bruhat–Tits tree $\mathcal{T}_p$ toward the boundary. At depth $L$ the tree has boundary vertices

$$
N_{\partial}(L) \;=\; (p+1)\,p^{L-1},
$$

total edges

$$
N_{\text{edge}}(L) \;=\; 1 + (p+1)\,\frac{p^L - 1}{p - 1},
$$

and the boundary requires $\lceil \log_2 N_{\partial}(L) \rceil$ qubits if each boundary vertex is addressed by a binary index.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Exact thermal single-link computation

**Inputs.** Boltzmann exponent coefficient $0.25$ per $n^2$, from the stated choice $\beta g^2 = 0.5$ (Section 3.5); truncation levels $n_{\max} \in \{3, 5, 7\}$ (chosen to span register sizes of $q = 3, 4$ qubits).

**Step 1: Partition function.** $Z = 1 + 2\sum_{n=1}^{\infty} e^{-0.25 n^2}$. Term by term (values of $e^{-x}$):

- $n=1$: $e^{-0.25} = 0.778801$
- $n=2$: $e^{-1.00} = 0.367879$
- $n=3$: $e^{-2.25} = 0.105399$
- $n=4$: $e^{-4.00} = 0.018316$
- $n=5$: $e^{-6.25} = 0.001930$
- $n=6$: $e^{-9.00} = 1.23410 \times 10^{-4}$
- $n=7$: $e^{-12.25} = 4.78512 \times 10^{-6}$
- $n=8$: $e^{-16.00} = 1.12535 \times 10^{-7}$

Inner sum through $n=8$: $0.778801 + 0.367879 + 0.105399 + 0.018316 + 0.001930 + 0.00012341 + 0.0000047851 + 0.000000113 = 1.272454$. The $n=9$ term is $e^{-20.25} = 1.60523 \times 10^{-9}$, so the remainder is below $2 \times 10^{-9}$ and negligible. Thus

$$
Z = 1 + 2(1.272454) = 3.544908.
$$

**Step 2: State infidelity.** $\epsilon_{\mathrm{tr}}(n_{\max}) = 2\sum_{n=n_{\max}+1}^{\infty} e^{-0.25 n^2} / Z$.

- $n_{\max}=3$: tail sum $n \ge 4$: $0.018316 + 0.001930 + 0.00012341 + 0.0000047851 + 0.000000113 = 0.020374$. Then
$$
\epsilon_{\mathrm{tr}}(3) = \frac{2 \times 0.020374}{3.544908} = \frac{0.040748}{3.544908} = 1.150 \times 10^{-2}.
$$
- $n_{\max}=5$: tail $n \ge 6$: $0.00012341 + 0.0000047851 + 0.000000113 = 0.00012831$. Then
$$
\epsilon_{\mathrm{tr}}(5) = \frac{2 \times 0.00012831}{3.544908} = \frac{0.00025662}{3.544908} = 7.242 \times 10^{-5}.
$$
- $n_{\max}=7$: tail $n \ge 8$: $e^{-16.00}=1.12535 \times 10^{-7}$ and $e^{-20.25}=1.60523 \times 10^{-9}$, sum $1.14140 \times 10^{-7}$. Then
$$
\epsilon_{\mathrm{tr}}(7) = \frac{2 \times 1.14140 \times 10^{-7}}{3.544908} = \frac{2.28280 \times 10^{-7}}{3.544908} \approx 6.44 \times 10^{-8}.
$$

**Step 3: Energy bias.** Denominator $S = 2\sum_{n=1}^{\infty} n^2 e^{-0.25 n^2}$:

- $n=1$: $1 \times 0.778801 = 0.778801$
- $n=2

## References

[1] Achieving the quantum field theory limit in far-from-equilibrium quantum link models. arXiv:2112.04501v3. https://arxiv.org/abs/2112.04501v3
[2] Observation of genuine $2+1$D string dynamics in a U$(1)$ lattice gauge theory with a tunable plaquette term on a trapped-ion quantum computer. arXiv:2604.07436v1. https://arxiv.org/abs/2604.07436v1
[3] Truncation uncertainties for accurate quantum simulations of lattice gauge theories. arXiv:2508.00061v4. https://arxiv.org/abs/2508.00061v4
[4] A change of perspective: switching quantum reference frames via a perspective-neutral framework. arXiv:1809.00556v4. https://arxiv.org/abs/1809.00556v4
[5] An axiomatic approach to quantum gauge field theory. arXiv:hep-th/9511122v1. https://arxiv.org/abs/hep-th/9511122v1
[6] A groupoidal approach to quantum reference frames. arXiv:2608.14133v1. https://arxiv.org/abs/2608.14133v1
[7] SU_q(n) Gauge Theory. arXiv:hep-th/9601033v2. https://arxiv.org/abs/hep-th/9601033v2
[8] Quantum Energy Inequalities and Stability Conditions in Quantum Field Theory. arXiv:math-ph/0502002v1. https://arxiv.org/abs/math-ph/0502002v1
[9] https://papers.qnfo.org/papers/holographic-quantum-error-correction-as-ads-cft-renormalization-group-flow-on-br/. QNFO: Holographic Quantum Error Correction as AdS/CFT Renormalization-Group Flow on Bruhat–Tits Trees: A Conditional Threshold Analysis at 10⁻⁴.
[10] https://papers.qnfo.org/papers/trapped-ion-ultrametric-synthesis/. QNFO: The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics.
[11] DOI pending. QNFO: Holographic QEC as AdS/CFT RG Flow on Bruhat–Tits Trees.
[12] https://papers.qnfo.org/papers/adelic-cross-domain/. QNFO: The Adelic Cross-Domain Program: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees.