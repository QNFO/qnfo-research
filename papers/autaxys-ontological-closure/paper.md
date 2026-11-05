# Autaxys Ontological Closure: When Is a Physical Quantity Computationally Real?

## Abstract

We propose an operational criterion for physical reality: a quantity is physically real only if there exists a finite Turing-machine protocol that approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions. This criterion is not a metaphysical claim about what "exists" — it is a boundary condition on measurability: if no finite computation can converge to a quantity's value, then no finite measurement protocol can distinguish that quantity from a nearby alternative, and the quantity is operationally indistinguishable from nonexistent. We show that standard physical quantities (mass, charge, spin, energy levels) satisfy the criterion, while continuum-valued fields at arbitrarily small scales, uncomputable real numbers as physical constants, and non-measurable sets fail it — and argue that this is a feature, not a bug. We decompose the criterion into eleven testable sub-claims spanning quantum foundations, cosmology, thermodynamics, information theory, and computability theory, and register dated, strength-weighted predictions for each.

## 1 Introduction

What does it mean for a physical quantity to be "real"? The question has divided physicists and philosophers for centuries. The realist position holds that quantities appearing in successful theories refer to entities that exist independently of measurement. The instrumentalist position holds that theories are computational devices for predicting measurement outcomes, and questions about "reality" are ill-posed. The operationalist position, associated with Bridgman [1], holds that the meaning of a quantity is exhausted by the operations used to measure it.

We propose a refinement of operationalism that leverages the theory of computation. The central insight is that measurement is a form of computation: a finite physical protocol that takes a system as input and produces a numerical output. If no finite protocol — not even in principle, with unlimited resources — can converge to a quantity's value, then that quantity cannot be measured. And if a quantity cannot be measured even in principle, it is operationally indistinguishable from a quantity that does not exist.

This paper formalizes this insight as an operational criterion — the Autaxys Ontological Closure (OC) criterion — and explores its consequences across eleven domains of physics and computation. The criterion is deliberately restrictive: it excludes more than it includes. We argue that this restrictiveness is a strength, not a weakness. A criterion that admits everything admits nothing.

### 1.1 Historical Context

The relationship between computation and physical reality has been explored from multiple directions. Landauer's principle [2] established that information is physical — erasing a bit costs $k_B T \ln 2$ in thermodynamic entropy; in dimensionless Planck units ($\hbar = c = G = k_B = 1$): $T \ln 2$, where both the energy and temperature are pure numbers — Archimedean norms of quantities whose completions exist at every place per Ostrowski's theorem. Wheeler's "it from bit" program [3] proposed that physical reality is intrinsically informational. Deutsch's constructor theory [4] reformulated physics in terms of which transformations are possible and which are forbidden, without reference to dynamics.

The OC criterion departs from these programs in its computational specificity. It does not claim that reality "is" computation — it claims that the boundary of measurability coincides with the boundary of computable approximability. This is a weaker and more testable claim.

## 2 The Operational Definition

### 2.1 Formal Statement

A quantity $Q$ associated with a physical system $S$ is *physically real* if and only if there exists:

1. A **finite Turing-machine protocol** $\mathcal{P}$ that, given a specification of the measurement apparatus and a desired precision $\varepsilon > 0$, halts after a finite number of steps and outputs a rational approximation $\tilde{Q}$ such that $|\tilde{Q} - Q| < \varepsilon$.
2. A **computable modulus of convergence** $\mu: \mathbb{N} \to \mathbb{N}$ such that for any desired precision $\varepsilon = 2^{-n}$, the protocol halts within $\mu(n)$ steps.
3. **Measurement-distinguishable predictions**: there exists at least one experimental configuration where the quantity $Q$ and any alternative quantity $Q'$ that also passes the criterion produce predictions that differ by more than the experimental uncertainty $\sigma$ at some finite $n$.

If no such protocol exists — even in principle, with unlimited computational resources — then $Q$ is not physically real.

### 2.2 What the Definition Does and Does Not Claim

**What it claims:** The boundary of physical measurability coincides with the boundary of computable approximability. If you cannot write a program that converges to a quantity's value with a guaranteed rate, you cannot build an apparatus that measures it.

**What it does NOT claim:**
- That the universe "is" a Turing machine. The criterion is about the *measurement* of quantities, not about the *ontology* of the universe.
- That uncomputable real numbers "don't exist." They exist as mathematical objects. They are simply not physically measurable — which is an uncontroversial claim: no experiment has ever measured an uncomputable real number.
- That every computable-approximable quantity is physically measurable in practice. Practical constraints (energy, time, materials) may make a computable quantity experimentally inaccessible. The criterion is about *in-principle* measurability.

### 2.3 Comparison with Existing Frameworks

| Framework | Core Claim | Difference from OC |
|:----------|:-----------|:-------------------|
| Operationalism (Bridgman) | Meaning = measurement operations | No computational bound on operations |
| Constructivism (Bishop) | Mathematical existence = constructive proof | Applied to mathematics, not physics |
| Deutsch's constructor theory | Physics = which transformations are possible | No explicit computability requirement |
| Wheeler's "it from bit" | Reality is intrinsically informational | Aspirational, no precise criterion |
| **Autaxys OC** | Physical reality = computable-approximable with modulus of convergence | Precise, testable, computational |

### 2.4 The Modulus of Convergence Requirement

Why require a computable modulus of convergence? Without it, the criterion would admit quantities that are computably approximable but with no guaranteed rate of convergence — a sequence that eventually gets within $\varepsilon$ but with no bound on how long "eventually" takes.

Such quantities are physically problematic. A measurement protocol that might take 1 second or $10^{100}$ years to reach the desired precision, with no way to know which, is not a measurement protocol — it is a gamble. The modulus of convergence guarantees that for any desired precision, you can compute an upper bound on the measurement time.

Standard physical quantities satisfy this requirement naturally. Measuring the mass of the electron to precision $2^{-n}$ requires a finite number of experimental runs whose count can be bounded as a function of $n$ (e.g., via the standard error scaling $\sigma/\sqrt{N}$). The bound may be impractical for large $n$, but it is computable.

## 3 What Survives: Quantities That Pass the Criterion

We demonstrate that the standard quantities of physics — the ones we actually measure — satisfy the OC criterion.

### 3.1 Mass, Charge, and Spin

**Mass.** The mass of a particle is measured by comparing its dynamical response to a known force against a reference mass. For any desired precision $\varepsilon$, $N \propto 1/\varepsilon^2$ independent measurements (bounded by the standard error of the mean) suffices. The protocol is: (1) prepare $N$ independent copies, (2) measure each, (3) report the sample mean. $\mu(n) \propto 2^{2n}$ for $\varepsilon = 2^{-n}$. The modulus is computable.

**Charge.** Millikan's oil-drop experiment [5] measures the elementary charge $e$ by balancing gravitational and electric forces on charged oil droplets. The protocol is finite: for $N$ droplets, the charge is estimated as the greatest common divisor of the measured charges. The modulus follows from the statistical uncertainty in each droplet measurement.

**Spin.** Spin components are measured via Stern–Gerlach apparati. The protocol is finite: prepare $N$ copies, measure each along the chosen axis, report the expectation value. The modulus is computable from the binomial distribution.

### 3.2 Energy Levels

Atomic and molecular energy levels are measured spectroscopically. The Rydberg constant $R_\infty$ is known to 12 significant figures [6] via laser spectroscopy of hydrogen. The protocol is: (1) excite the atom, (2) measure the emitted photon wavelength via interferometry, (3) compute the energy difference $\Delta E = hc/\lambda$. Each step is a finite computation.

### 3.3 Cross Sections and Decay Rates

Scattering cross sections and decay rates are measured by counting events. The protocol: (1) prepare $N$ initial states, (2) count the number of events $k$, (3) report $\hat{\sigma} = k/N$ (normalized by luminosity for cross sections). The modulus is computable from Poisson or binomial statistics.

### 3.4 The Pattern

Every quantity that physics actually measures passes the OC criterion. This is not a coincidence — it is the design principle behind the criterion. The criterion was reverse-engineered from the question: what do all physically measured quantities have in common? The answer: they are computably approximable with a known convergence rate.

The criterion is not a restriction on physics — it is a *description* of physics as actually practiced. Physicists already restrict their attention to quantities they can measure. The OC criterion makes this restriction explicit and connects it to a precise mathematical boundary — the computable numbers with computable moduli of convergence.

## 4 What Fails: Quantities That Do Not Pass

The criterion's value lies in what it excludes. We identify three classes of quantities that fail the criterion — and argue that these exclusions are features, not bugs.

### 4.1 Uncomputable Real Numbers as Physical Constants

Consider a hypothetical physical constant $c_\Omega$ whose binary expansion is given by Chaitin's halting probability $\Omega$ [7]. No Turing machine can compute more than finitely many bits of $\Omega$ — the sequence is algorithmically random.

If a theory predicted that $c_\Omega$ had a specific value, no finite measurement protocol could verify this prediction beyond a finite number of bits. For sufficiently high precision, the prediction would be indistinguishable from any other uncomputable constant within the same precision bounds. The quantity would be unmeasurable in principle — and therefore, by the OC criterion, not physically real.

This is not a loss. No physical theory currently predicts an uncomputable constant, and if one did, the OC criterion would correctly identify it as physically vacuous — it makes predictions that cannot be verified by any finite protocol.

### 4.2 Continuum Fields at Arbitrarily Small Scales

Consider a classical field $\phi(x)$ defined for every real number $x \in \mathbb{R}$. To fully specify the field's value requires specifying an uncountable infinity of real numbers — one for each point in the continuum. No Turing machine can output an uncountable infinity of values, and no measurement apparatus can resolve structure at arbitrarily small length scales (Planck-scale limitations guarantee this).

The OC criterion does not claim that fields "don't exist." It claims that the *pointwise* value of a field at a specific real coordinate is not a physically real quantity — it cannot be measured at arbitrarily high precision. This is not only a computational observation; it follows from thermodynamics. The Bekenstein bound [12] states that the information content $\mathcal{I}$ of any bounded physical system, expressed in dimensionless Planck units ($\hbar = c = G = k_B = 1$), satisfies $\mathcal{I} \leq 2\pi R E / \ln 2$, where $R \equiv R_{\text{phys}}/\ell_P$ (spatial extent in Planck lengths $\ell_P \equiv \sqrt{\hbar G / c^3}$) and $E \equiv E_{\text{phys}}/E_P$ (total energy in Planck energies $E_P \equiv \sqrt{\hbar c^5 / G}$). The bound's quantities are pure numbers; as such they do not assume the Archimedean completion implicit in dimensional formulations. For a measurement apparatus of fixed size $R$, resolving a field value to precision $\varepsilon$ requires $\log_2(1/\varepsilon)$ bits — and as $\varepsilon \to 0$, this diverges. The Bekenstein bound forces the apparatus's energy density to diverge in response, and at sufficiently high density the apparatus collapses into a black hole before the measurement completes [13]. The thermodynamic bound and the OC criterion's computability bound are isomorphic in this regime: both exclude the pointwise value as physically inaccessible. What IS physically real is the field's value *integrated over a finite region*, which is computably approximable (via lattice regularization and finite-difference methods).

This maps cleanly onto the effective field theory paradigm [8], where theories are understood to be valid only above a cutoff scale $\Lambda$, and pointwise field values below $\Lambda^{-1}$ are not physically meaningful. The OC criterion provides a computational justification for this paradigm.

### 4.3 Non-Measurable Sets

In standard quantum mechanics, the state space is a Hilbert space, and observables are self-adjoint operators whose spectral projections define measurable subsets of the real line. But the real line contains non-measurable sets (assuming the Axiom of Choice), and a self-adjoint operator could in principle have a spectral projection onto a non-measurable set.

Such an operator would define an "observable" whose measurement outcomes cannot be assigned probabilities in the standard sense — the Born rule would not apply. The OC criterion excludes such observables: if a spectral projection lands on a non-measurable set, the corresponding "quantity" cannot be measured even in principle, because no finite protocol can distinguish membership in a non-measurable set.

This is consistent with the Solèr–Piron–Holland theorem [9], which shows that the standard Hilbert-space formulation of quantum mechanics over $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$ is effectively forced if one requires infinite-dimensional orthomodular spaces with certain regularity conditions. The OC criterion adds a computational regularity condition: observables must correspond to measurable sets, which is already implicit in the Born rule.

## 5 The Eleven Sub-Papers

The OC criterion decomposes naturally into eleven testable sub-claims, each of which could form the basis of a standalone paper. We enumerate them here as a structured research program.

### 5.1 Core Formalisms

| # | Sub-Paper | Domain | Core Claim | Falsifiability |
|:--|:----------|:-------|:-----------|:---------------|
| 1 | **OC-1: The Criterion** | Metatheory | The OC criterion is logically consistent and non-vacuous — it admits standard quantities and excludes pathological ones. | Find a physically measured quantity that cannot be computably approximated with a known modulus. |
| 2 | **OC-2: Computability of Physical Constants** | Metrology | All dimensionless physical constants (fine-structure constant $\alpha$, proton-to-electron mass ratio $\mu$, etc.) have computable binary expansions with computable moduli of convergence. | Exhibit a dimensionless constant whose $n$-th bit cannot be computed by any finite protocol for some finite $n$. |
| 3 | **OC-3: The Modulus Requirement** | Computability | The modulus of convergence requirement is necessary — there exist computably approximable quantities without computable moduli whose "measurement" would require unboundedly long protocols. | Construct a physical quantity that is computably approximable but not measurably approximable — i.e., where the absence of a modulus makes experimental verification impossible. |

### 5.2 Quantum Foundations

| # | Sub-Paper | Domain | Core Claim | Falsifiability |
|:--|:----------|:-------|:-----------|:---------------|
| 4 | **OC-4: Spectral Measurability** | Quantum foundations | Every physically real observable has a spectral measure supported on a measurable subset of $\mathbb{R}$. Operators with non-measurable spectral projections do not correspond to physical observables. | Construct a self-adjoint operator on a separable Hilbert space whose spectral measure is non-measurable, and show that it CAN be measured. |
| 5 | **OC-5: The Born Rule as Computable Convergence** | Quantum foundations | The Born rule's frequency interpretation — $p(a) = \lim_{N \to \infty} N_a/N$ — is a computable modulus of convergence for quantum probabilities. | Find a quantum system where measurement frequencies do not converge computably. |
| 6 | **OC-6: Spin Networks and Computable Geometry** | Quantum gravity | Loop quantum gravity's spin network states have computable geometric spectra (area, volume) with computable moduli — they satisfy the OC criterion. | Show that a spin network geometric observable has an uncomputable spectrum. |

### 5.3 Cosmology and Thermodynamics

| # | Sub-Paper | Domain | Core Claim | Falsifiability |
|:--|:----------|:-------|:-----------|:---------------|
| 7 | **OC-7: Cosmological Observables** | Cosmology | Cosmological parameters ($H_0$, $\Omega_\Lambda$, etc.) are computably approximable with known moduli (cosmic-variance-limited). The multiverse "measure" problem is an OC violation — the measure is not computably approximable. | Exhibit a cosmological parameter whose value cannot be bounded by any finite measurement protocol. |
| 8 | **OC-8: Thermodynamic Computability** | Thermodynamics | Thermodynamic quantities (temperature, pressure, entropy) are computably approximable in the thermodynamic limit via finite-system scaling with computable convergence rates. The thermodynamic limit itself is an OC-compliant idealization. | Find a thermodynamic quantity whose infinite-system limit is not computably approximable from finite systems. |

### 5.4 Information and Computation

| # | Sub-Paper | Domain | Core Claim | Falsifiability |
|:--|:----------|:-------|:-----------|:---------------|
| 9 | **OC-9: Landauer's Principle as OC Instance** | Information theory | Landauer's principle — $E \geq k_B T \ln 2$ per erased bit; $E \geq T \ln 2$ in Planck units ($\hbar = c = G = k_B = 1$) — is an OC instance: the computational cost of measurement is physical and finite, and the protocol halts. | Show that a measurement protocol can extract information without a finite thermodynamic cost. |
| 10 | **OC-10: Oracle Machines and Hypercomputation** | Computability | Oracle machines (Turing machines with access to uncomputable oracles) do not correspond to physical measurement protocols — they violate OC. Hypercomputation is physically unrealizable. | Construct a physical system whose measurement outcome depends on an uncomputable oracle and verify the prediction. |
| 11 | **OC-11: The Church–Turing–Deutsch Principle as OC Corollary** | Metatheory | The Church–Turing–Deutsch principle — every finitely realizable physical system can be perfectly simulated by a universal Turing machine — is a corollary of OC: if a system's behavior were not computably approximable, its predictions would be unmeasurable. | Construct a physical system whose observable behavior cannot be simulated by any Turing machine. |

### 5.5 Research Program Architecture

The eleven sub-papers form a dependency lattice:

```
OC-1 (core criterion)
|-- OC-2 (physical constants) -- OC-3 (modulus necessity)
|-- OC-4 (spectral) -- OC-5 (Born rule) -- OC-6 (spin networks)
|-- OC-7 (cosmology) -- OC-8 (thermodynamics)
|-- OC-9 (Landauer) -- OC-10 (oracles)
+-- OC-11 (CTD principle)
```

OC-1 is the prerequisite for all others. OC-2 and OC-4 can proceed in parallel. OC-7 and OC-8 are independent of the quantum sub-papers. OC-11 synthesizes the program.

## 6 Judgment Sensitivity and Calibration

### 6.1 Sensitivity Analysis

The OC criterion's value depends on two judgments: (a) whether the computable/non-computable boundary is the RIGHT boundary for physical reality, and (b) whether the modulus-of-convergence requirement is necessary rather than only convenient.

**Pessimistic scenario.** If the computability requirement is relaxed (e.g., to "computably approximable without modulus"), the criterion admits more quantities but loses its sharp boundary on measurement time. The 11 sub-papers remain valid but OC-3 (modulus necessity) becomes OC-3 (modulus convenience).

**Optimistic scenario.** If a physical constant is demonstrated to be uncomputable (OC-2 falsified), the criterion gains an empirical anchor — it would be the only framework that PREDICTED the constant's unmeasurability at high precision. This is unlikely but would be a dramatic confirmation.

**Robustness:** The criterion is robust to the choice of computational model — Turing machines, lambda calculus, and register machines define the same set of computable functions. It is NOT robust to the choice between classical and quantum computation — a quantum computer can solve problems (e.g., factoring) that are believed to be classically hard. However, the set of computably approximable reals is the same for classical and quantum Turing machines, so the criterion's boundary is unchanged.

### 6.2 Calibration Register

We register the following dated, strength-weighted predictions.

**[CHECK: 2030-12] OC-2: No uncomputable constant.** No peer-reviewed publication will demonstrate that any dimensionless physical constant (fine-structure constant $\alpha$, proton-to-electron mass ratio $\mu$, etc.) has an uncomputable binary expansion at any finite bit position, where "uncomputable" means no Turing machine can output the $n$-th bit for some finite $n$. **Strength:** [STRONG] — anchored to the empirical base rate: zero physical constants have been shown uncomputable in the history of physics, despite the existence of uncomputable reals being known since Turing (1936). **Status:** [PENDING]. **Risk:** "This was always obvious — no one expected physical constants to be uncomputable."

**[CHECK: 2035-12] OC-10: No hypercomputation.** No peer-reviewed publication will demonstrate a physical system whose measurement outcome depends on an uncomputable oracle — i.e., no hypercomputational physical device will be experimentally verified. **Strength:** [STRONG] — anchored to the Church–Turing–Deutsch principle, which has held without exception since its formulation. **Status:** [PENDING]. **Risk:** "This was a null prediction — the absence of hypercomputation is the default, not a discovery."

**[CHECK: 2028-06] OC-9: Landauer bound holds.** No experiment will measure an energy cost below $k_B T \ln 2$ for erasing one bit of information in any system at temperature $T$. **Strength:** [STRONG] — anchored to extensive experimental confirmation of Landauer's principle [10]. **Status:** [PENDING]. **Risk:** "Landauer's principle was already well-established — this prediction added nothing new."

**[CHECK: 2032-12] OC-4: No non-measurable observable.** No peer-reviewed publication will propose a physically realizable experiment whose measurement outcomes are governed by a self-adjoint operator with a non-measurable spectral projection, where "physically realizable" means a concrete experimental protocol with specified apparatus. **Strength:** [WEAK] — the non-measurability of such projections follows from the Axiom of Choice, and no physical experiment has ever invoked the Axiom of Choice in its predictions. **Status:** [PENDING]. **Risk:** "No physicist would propose such an experiment — the prediction is trivially safe."

**[CHECK: 2036-12] OC overall: Criterion survives.** By December 2036, no counterexample will have been published that satisfies ALL of: (a) the quantity is standard in physics (not a pathological construction), (b) the quantity has been physically measured to high precision, (c) the quantity cannot be computably approximated with a known modulus of convergence. **Strength:** [STRONG] — anchored to the absence of any known counterexample across all of physics. **Status:** [PENDING]. **Risk:** "The criterion was designed to be unfalsifiable — it defines away potential counterexamples as 'not physically measurable by definition.'"

## 7 Practical Applications

The OC criterion has immediate practical consequences for theory-building.

### 7.1 Theory Evaluation

A physical theory that predicts uncomputable quantities is operationally vacuous — it makes predictions that cannot be verified. The OC criterion provides a sharp filter: if a theory's observable predictions are not computably approximable, the theory is not testable. This applies particularly to multiverse theories that predict probability distributions over an uncomputable "measure" [11], and to certain approaches to quantum gravity that produce continuous spectra without computable eigenvalue approximations.

### 7.2 Experimental Design

The modulus-of-convergence requirement translates directly into experimental resource estimates. If measuring quantity $Q$ to precision $\varepsilon$ requires $\mu(-\log_2 \varepsilon)$ steps, and each step costs $E$ joules, then the total energy cost is $E \cdot \mu(n)$. This connects the computational criterion to thermodynamic resource bounds — a connection that OC-9 (Landauer) makes explicit.

### 7.3 Quantum Computing

Quantum computers expand the set of efficiently solvable problems (BQP) but do not expand the set of computably approximable reals. The OC criterion is unchanged by the quantum computing revolution — a reassuring consistency check. However, quantum computers DO change the modulus of convergence for certain quantities: a quantity that requires exponential classical time to approximate may require only polynomial quantum time. The OC criterion accommodates this naturally — the modulus is relative to the computational model, and "Turing machine" includes quantum Turing machines.

## 8 Counterfactual Backcasting

### 8.1 Tier 1 Fork (~1990s): OC Adopted as a Metatheoretic Principle

If the OC criterion had been formulated and adopted by the theoretical physics community in the 1990s, the following would be observable by 2026:

- **String theory landscape.** The landscape problem — the apparent existence of $10^{500}$ or more vacua with no computable selection principle — would have been identified as an OC violation. The response would have been either (a) to find a computable selection principle, or (b) to accept that the landscape is not a physically real quantity. The current impasse would have been short-circuited.
- **Multiverse measures.** The measure problem in eternal inflation would have been recognized as an OC violation — the measure over the multiverse is uncomputable. Cosmology would have focused on observables within a single Hubble volume.
- **Quantum foundations.** The measurement problem would have been reformulated as a computational question: which quantities survive the decoherence process with computable moduli of convergence?

This fork was not taken. Theoretical physics in the 1990s–2020s continued to treat uncomputable quantities (landscapes, measures, continuum fields at all scales) as physically meaningful.

### 8.2 Tier 2 Fork (~1970s): Computability Integrated into Physics Education

If Turing's 1936 work on computability had been integrated into the standard physics curriculum alongside calculus and linear algebra, a generation of physicists would have been trained to ask "is this quantity computable?" alongside "is this quantity conserved?" This would have produced:

- A standard textbook section titled "Computability of Physical Quantities" in graduate quantum mechanics
- At least one PhD thesis per year examining the computability status of a physical quantity
- The OC criterion as a standard topic in foundations of physics courses

This fork was not taken. Physics education continues to treat real numbers as unproblematic primitives, without examining which reals are physically accessible.

## 9 Conclusion

The Autaxys Ontological Closure criterion proposes a precise boundary for physical reality: a quantity is physically real if and only if it is computably approximable with a computable modulus of convergence, yielding measurement-distinguishable predictions.

The criterion is neither radical nor novel. It formalizes what physicists already do: restrict attention to quantities they can measure. The contribution is making this restriction explicit and connecting it to the mathematical theory of computation, where the boundary between computable and uncomputable has been precisely characterized since Turing (1936).

The criterion's value is threefold. First, it provides a sharp filter for theory evaluation: if a theory's predictions are uncomputable, the theory is untestable. Second, it connects measurement protocols to computational resource bounds, making the thermodynamic cost of measurement explicit. Third, it decomposes into eleven testable sub-claims that span quantum foundations, cosmology, thermodynamics, and computability theory — a structured research program that can proceed in parallel across multiple domains.

The central prediction is conservative: no counterexample will be found. Every quantity that physics currently measures already satisfies the criterion, and no quantity that physics will measure in the future will violate it. The null hypothesis — that the computability boundary is the correct boundary for measurability — is the well-anchored prediction. The interesting outcome would be a counterexample: a physically measured quantity that cannot be computably approximated. That would refute the criterion and simultaneously reveal something deep about the relationship between computation and physical reality. We predict it will not happen.

## Declarations

**Funding:** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Conflicts of Interest:** The author has no financial or institutional conflicts of interest.

**Ethics Approval:** Not applicable — this is a theoretical assessment involving no human participants, animal subjects, or sensitive data.

**Consent to Participate:** Not applicable.

**Author Contributions:** R.B.Q.-G. is the sole author and performed all aspects of the research, analysis, and writing.

**Data Availability:** All source artifacts for this paper are archived at the GitHub repository `QNFO/autaxys-ontological-closure` and at papers.qnfo.org at the DOI listed in the frontmatter.

**Code Availability:** Not applicable — this paper contains no original code.

**Materials Availability:** Not applicable.

**Use of Artificial Intelligence:** A large language model (DeepSeek) was used as a research assistant for literature synthesis, structured analysis, and prose composition under the supervision and editorial direction of the human author, who is solely responsible for all claims, judgments, and conclusions.

## References

[1] P. W. Bridgman, *The Logic of Modern Physics*. Macmillan, 1927.

[2] R. Landauer, "Irreversibility and heat generation in the computing process," *IBM Journal of Research and Development*, vol. 5, no. 3, pp. 183–191, 1961.

[3] J. A. Wheeler, "Information, physics, quantum: The search for links," in *Proceedings of the 3rd International Symposium on Foundations of Quantum Mechanics*, Tokyo, 1989, pp. 354–368.

[4] D. Deutsch, "Constructor theory," *Synthese*, vol. 190, pp. 4331–4359, 2013.

[5] R. A. Millikan, "On the elementary electrical charge and the Avogadro constant," *Physical Review*, vol. 2, no. 2, pp. 109–143, 1913.

[6] CODATA, "Internationally recommended 2018 values of the fundamental physical constants," *Reviews of Modern Physics*, vol. 93, 2021.

[7] G. J. Chaitin, "A theory of program size formally identical to information theory," *Journal of the ACM*, vol. 22, no. 3, pp. 329–340, 1975.

[8] S. Weinberg, "Phenomenological Lagrangians," *Physica A*, vol. 96, pp. 327–340, 1979.

[9] M. P. Solèr, "Characterization of Hilbert spaces by orthomodular spaces," *Communications in Algebra*, vol. 23, pp. 219–243, 1995.

[10] A. Bérut et al., "Experimental verification of Landauer's principle linking information and thermodynamics," *Nature*, vol. 483, pp. 187–189, 2012.

[11] B. Freivogel, "Making predictions in the multiverse," *Classical and Quantum Gravity*, vol. 28, p. 204007, 2011.
[12] J.D. Bekenstein, "Universal upper bound on the entropy-to-energy ratio for bounded systems," Phys. Rev. D 23, 287–298 (1981). DOI: 10.1103/PhysRevD.23.287

[13] R. Bousso, "Localization of Negative Energy and the Bekenstein Bound," Phys. Rev. Lett. 111, 221601 (2013). DOI: 10.1103/PhysRevLett.111.221601
