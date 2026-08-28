---
title: "A Pre-Registered Falsification of Deterministic Measurement-Triggered Relaxation"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-20"
license: "CC BY-NC-SA 4.0"
doi: "10.5281/zenodo.22144215"
version: "1.1"
status: "published"
---

## Abstract

The hydrodynamic re-grounding of quantum mechanics proposes that measurement outcomes arise from a deterministic relaxation of a probability fluid into eigenstate basins, rather than from a discontinuous collapse. A prior adjudication of this program found its central weakness to be the absence of any concrete mechanism: no equation of motion was specified for the claimed relaxation. This paper reports a pre-registered computational test of the strongest available form of that proposal. A two-level system was evolved unitarily to a measurement time, then subjected to three candidate relaxation dynamics toward the eigenbasis, and outcome statistics were collected over $10^5$ shots per state across a fixed test set. The simulation code, parameter values, and analysis rules were fixed and checksummed before any result was produced. Every configuration failed: the maximum deviation from Born probabilities was $0.5$, fifty times the pre-registered tolerance of $10^{-2}$, because a deterministic map from a fixed initial state yields a degenerate outcome channel — measured probabilities take only the values $0$ or $1$. The reader should care because this converts a conceded gap into a demonstrated one: within the tested family, deterministic measurement-triggered relaxation cannot reproduce the Born rule; reproducing it requires an ensemble over initial states, stochasticity in the dynamics, or measurement-contextual variables, each of which corresponds to a distinct existing research program. Where the premises end: the falsification is scoped to deterministic, fixed-initial-state, threshold-terminated dynamics on two-level systems; it does not adjudicate stochastic, ensemble-based, or contextual alternatives, and it does not claim the hydrodynamic program is false in full — only that this mechanism, as specified, is falsified.

## 1. Introduction

A central unresolved question in quantum foundations is whether the probabilities of measurement outcomes can be derived from a deterministic underlying dynamics rather than assumed through the Born rule and the projection postulate. The hydrodynamic formulation of quantum mechanics — the Madelung equations — provides a continuous, deterministic description of the probability fluid that is mathematically equivalent to the Schrödinger equation, and a series of modern reconstructions have built rigorous measure-theoretic foundations on this picture. A recent adjudication of this research program examined five objections to it and confirmed one in substance: the program lacked any specification of how the probability fluid relaxes into discrete eigenstate configurations during measurement. The framework's own text conceded this gap explicitly.

That concession identifies the precise question worth testing: can a measurement-triggered relaxation dynamics toward eigenstate basins reproduce the Born statistics of a two-level system? The present work answers this question with a pre-registered simulation. The design, code, parameters, and analysis rules were fixed and checksummed before any result was produced. The outcome is negative and, by construction, unambiguous: within the tested deterministic family, the Born rule cannot be reproduced.

## 2. The Sealed Test Protocol

The test uses a two-level system with Hamiltonian $H = \frac{\omega}{2}\sigma_z$ (in natural units, $\omega = 1$), represented in Bloch coordinates $(x, y, z)$, where the density operator is $\rho = \frac{1}{2}(I + x\sigma_x + y\sigma_y + z\sigma_z)$ and the Born probability of the upper eigenstate is $p = (1+z_0)/2$ for an initial state with Bloch component $z_0$.

The protocol has three stages. First, the state evolves unitarily for a time $t_m$ (one hundred integration steps), with no relaxation active. Second, a relaxation operator is applied for a duration $\tau_m$ via fourth-order Runge–Kutta integration at a fixed step size, $\tau_m/500$. Third, a terminal rule assigns the outcome by the sign of the final $z$-coordinate: $z \geq 0$ yields the upper outcome, $z < 0$ the lower.

Three candidate relaxation dynamics were pre-specified, each of the form

$$\frac{d\rho}{dt} = -i[H, \rho] + \gamma\, L(\rho),$$

with the relaxation term $L$ active only during the measurement window:

- **Variant A** drives the transverse Bloch components to zero while preserving $z$ exactly: $L(\rho) = -\frac{1}{2}(x\,\sigma_x + y\,\sigma_y)$. This is the pure eigenbasis-attraction proposal, with the outcome determined by the preserved $z$.
- **Variant B** adds a generic dissipative coupling that perturbs $z$: the $z$-equation gains a term $-\alpha (x^2 + y^2) z$, representing apparatus back-reaction. The parameter $\alpha$ controls the strength of the perturbation.
- **Variant C** implements radial-basis basins: the relaxation drives the state toward a target $z$-value that is a fixed function of the pre-relaxation state, with no per-shot adaptive weights.

These three candidate equations are reconstructions authored for this test. They are not quoted from, and are not attributed to, the geometric or measure-theoretic reconstructions of the hydrodynamic picture (Reddiger 2017; Reddiger and Poirier 2023), which specify no measurement-triggered relaxation equation; the phrase "the strongest available form of that proposal" in the abstract refers to this authorial reconstruction, not to an equation stated in the reconstruction literature.

The test set comprised nine canonical Bloch states (the $\pm x$, $\pm y$, $\pm z$ poles and three equal-weight superpositions) plus fifty uniformly random states, for fifty-nine states in total. Each state was sampled $10^5$ times. The pre-registered tolerance was $\varepsilon = 10^{-2}$ on the maximum absolute deviation between measured and Born probabilities over the full test set. The parameter ranges were fixed: $\gamma \tau_m \in \{0.5, 5, 50\}$ for the rate–duration product, and $\alpha \tau_m \in \{0.01, 0.1, 1.0\}$ for the coupling.

The implementation, parameter ledger, and analysis rules were committed and checksummed before any simulation was executed; the checksum recorded at sealing matched the file that was run. Two pre-result amendments were made and documented: a portability fix for the matrix-exponential routine required by the local numerical library, and an equivalence-preserving restatement of the shot loop justified by the determinism of the dynamics (see Section 3). Neither amendment changed any parameter, dynamics, or analysis rule.

## 3. Results

All seven configurations — three rate–duration settings for Variant A, three coupling settings for Variant B, and Variant C — produced the same verdict: **FAIL**, with a maximum deviation of $0.5$ against the tolerance of $10^{-2}$.

Measured probabilities took only the values $0$ or $1$ for every state in every configuration. This is the signature of a degenerate outcome channel: a deterministic map from a fixed initial state always produces the same trajectory, hence the same outcome, on every shot. No statistical spread is available to realize a fractional probability.

The structure of the deviations is instructive. For the two polar eigenstates, the deterministic outcome coincides with the Born value, and the deviation is zero. For equatorial states, where the Born probability is $0.5$ and the terminal rule must break the symmetry, the deviation is $0.5$. For mixed states the deviation is intermediate, ranging from $0.08$ to $0.47$, scaling with the distance of the Born probability from the deterministic assignment. In no case does the deterministic channel approximate the Born value within the tolerance.

The result is robust across the entire parameter range examined: increasing the relaxation rate $\gamma$ from $0.5$ to $50$ changes nothing, because the relaxation only removes the transverse components and the terminal outcome is fixed by the invariant $z$; the perturbation $\alpha$ likewise cannot rescue the statistics, because any deterministic perturbation still yields a single outcome per initial state; and Variant C's fixed target function does not introduce the required spread. The failure is structural, not parametric.

## 4. Why Determinism Forces Degeneracy

The mechanism behind the negative result is elementary and general. A deterministic dynamics assigns exactly one trajectory to each initial condition. In an experiment that prepares the same state repeatedly, every shot follows that same trajectory, so every shot yields the same outcome. A fractional outcome probability therefore requires one of three ingredients:

1. **An ensemble over initial states.** If the preparation is not a fixed state but a distribution over states, the outcome probabilities reflect the distribution (the de Broglie–Bohm program makes the Born rule the equilibrium distribution over configurations — the quantum equilibrium hypothesis).
2. **Stochasticity in the dynamics.** If the evolution contains a noise term, different shots take different trajectories and outcomes acquire nontrivial frequencies (the dynamical-reduction and stochastic-Schrödinger families).
3. **Measurement-contextual hidden variables.** If the outcome depends on unobserved contextual degrees of freedom of the measurement device, the statistics over those degrees of freedom can reproduce the Born rule (the hidden-measurement program).

Each of these ingredients corresponds to a substantial existing research program, and each is logically distinct from the deterministic, fixed-state, threshold-terminated family tested here. The present result therefore does not say that hydrodynamic realism is impossible; it says that the specific mechanism — measurement-triggered deterministic relaxation of a fixed initial state into eigenstate basins, with a threshold terminal rule — cannot produce the Born statistics it was invoked to explain. Any hydrodynamic account must import one of the three ingredients above, at which point its explanatory burden shifts to that ingredient.

## 5. Relation to Prior Work

The prior literature contains several programs that produce Born-like probabilities from relaxation-like dynamics, and the present result sharpens their mutual relationship rather than contradicting them.

The subquantum H-theorem program proposes that relaxation to quantum equilibrium occurs dynamically within de Broglie–Bohm-type theories; explicit simulations of relaxation to the Born rule were given for such theories, and timescale analyses of the relaxation were provided. These programs differ from the present test in their most load-bearing premise: they work in configuration space, with the equilibrium distribution over initial configurations supplying the statistics. They are ensemble-based (ingredient 1 above), not fixed-state dynamics.

The stochastic program — dynamical reduction models, continuous spontaneous localization, and quantum-state-diffusion equations — introduces noise explicitly into the dynamics. These models are stochastic (ingredient 2), with experimental bounds that have been mapped in detail. The present test's Variant B is a deterministic caricature of their coupling structure, and its failure to reproduce the Born rule is precisely the sense in which stochasticity is not optional for that coupling class.

The hidden-measurement program resolves the measurement problem by treating measurement interactions as involving hidden variables whose statistics reproduce the Born rule; it is contextual (ingredient 3). It is likewise outside the deterministic family tested here.

The geometric and measure-theoretic reconstructions of the hydrodynamic picture — the work on the Madelung equations and on probability-based quantum theory — are kinematical in the relevant sense: they rigorously define random variables within an externally supplied unitary dynamics, and they address the projection postulate through conditional probabilities rather than through a relaxation mechanism. The present result is consistent with that literature: it falsifies a mechanism that the reconstruction literature never supplied. The author has confirmed in correspondence with M. Reddiger (26 August 2026) that the candidate equations of Section 2 appear nowhere in that published work; the measurement question raised here is treated in the forthcoming Part III of the reconstruction program.

The empirical anchor for strong-field hydrodynamic trajectories — quantitative reproduction of high-harmonic spectra by Bohmian trajectories — is not affected by this result. That work demonstrates the predictive power of trajectory ensembles within the unitary dynamics; it does not provide a measurement-triggered relaxation producing the Born rule, which is the claim tested here.

## 6. Implications for the Hydrodynamic Program

The adjudication that motivated this work found the hydrodynamic program's mechanism gap to be real but conceded, not demonstrated. This paper closes that gap in the direction of falsification: for the strongest available deterministic specification, the mechanism cannot work. The program's proponents must therefore either

1. adopt an ensemble over initial states, importing the quantum-equilibrium assumption (in which case the measurement problem is solved by the equilibrium distribution, not by relaxation dynamics), or
2. introduce stochasticity into the relaxation, in which case the framework converges on the dynamical-reduction family and inherits its experimental bounds, or
3. invoke contextual hidden variables, in which case the framework converges on the hidden-measurement program.

Each path is a well-defined research direction with existing literature, constraints, and experimental programs. The contribution of the present work is to rule out the naive path — deterministic relaxation with a fixed initial state — and to make the required ingredient precise.

## 7. What a Practitioner Can Do With This Result

The deliverable is a reusable, audit-proof falsification package for claims of the form "a deterministic relaxation reproduces the Born rule":

1. **Reproduce the verdict.** The simulation code, parameter ledger, and analysis rules are committed with a recorded checksum; running the code reproduces the reported maximum deviation of $0.5$ and the degenerate outcome channel. A practitioner can verify the claim in minutes without trusting the authors.
2. **Reuse the template.** The protocol — fixed Hamiltonian, sealed test set, pre-registered tolerance, checksummed code, threshold terminal rule — transfers to any proposed relaxation dynamics. Swap the dynamics family, keep the test.
3. **Screen foundation claims.** Grant reviewers and due-diligence analysts evaluating hydrodynamic or relaxation-based accounts of measurement can apply the three-ingredient test: if a proposal specifies a deterministic map from a fixed initial state to an outcome, it cannot reproduce the Born rule, regardless of the details; the proposal must name its ensemble, stochastic, or contextual ingredient.
4. **Bound the design space.** The result quantifies how much of each ingredient is needed (the minimal-noise boundary for stochastic extensions is the natural next measurement), giving implementers a concrete target rather than a philosophical debate.

The template is framework-agnostic: it requires only a state space, a dynamics, a terminal rule, and a tolerance — four items any proposal of this class already specifies.

## 8. Conclusion

A pre-registered simulation tested whether deterministic measurement-triggered relaxation toward eigenstate basins can reproduce the Born probabilities of a two-level system. It cannot: the maximum deviation from the Born rule was $0.5$ across all seven configurations and all fifty-nine states, fifty times the pre-registered tolerance, because a deterministic map from a fixed initial state yields a degenerate outcome channel. The falsification is structural, not parametric, and it identifies exactly what a hydrodynamic account of measurement must add: an ensemble over initial states, stochastic dynamics, or contextual hidden variables. The result is offered as a legitimate negative result — the outcome the pre-registration was designed to deliver.

## Declarations

**Funding:** This research received no external funding.

**Conflicts of interest:** The author is the author of the framework whose mechanism is falsified here; this conflict is disclosed and the test was pre-registered before any result was produced, with code, parameters, and analysis rules fixed in advance.

**Data availability:** The full evidence trail — simulation code, parameter ledger, pre-registration record, raw per-state results, and the checksum chain — is deposited with this paper and in the version-controlled project repository.

**AI assistance disclosure:** This paper was written with AI assistance (drafting, verification orchestration, simulation implementation). All computational results were produced by the checksum-sealed code; AI involvement is disclosed as a quality signal per the author's standing disclosure policy.

**License:** CC BY-NC-SA 4.0.

**Acknowledgements:** The author thanks Dr. Maik Reddiger for a clarifying correspondence (26 August 2026) confirming that the candidate relaxation equations of Section 2 do not appear in his published work with B. Poirier, and for noting that the measurement question is addressed in the forthcoming Part III of the reconstruction program.

**Version:** 1.1 (this version).

**Changelog:**
- **v1.1 (2026-08-28)** — attribution clarification. Added an explicit statement in Sections 2 and 5 that the three candidate relaxation equations are the author's own reconstructions and are not quoted from Reddiger & Poirier (2023) or Reddiger (2017); added an acknowledgement of the clarifying correspondence with M. Reddiger (26 August 2026). No scientific result, equation, data, or conclusion was changed.
- **v1.0 (2026-08-20)** — first published version.

## References

Bassi, A., and G. Ghirardi. 2003. "Dynamical reduction models." *Physics Reports* 379 (5–6): 257–426. doi:10.1016/s0370-1573(03)00103-0.

Colin, S., and W. Struyve. 2010. "Quantum non-equilibrium and relaxation to equilibrium for a class of de Broglie–Bohm-type theories." *New Journal of Physics* 12: 043008. doi:10.1088/1367-2630/12/4/043008.

Drezet, A. 2021. "Justifying Born's Rule $P_\alpha = \lvert\Psi_\alpha\rvert^2$ Using Deterministic Chaos, Decoherence, and the de Broglie–Bohm Quantum Theory." *Entropy* 23 (11): 1371. doi:10.3390/e23111371.

Ghirardi, G. C., A. Rimini, and T. Weber. 1986. "Unified dynamics for microscopic and macroscopic systems." *Physical Review D* 34: 470. doi:10.1103/physrevd.34.470.

Hacohen-Gourgy, S., and L. S. Martin. 2020. "Continuous measurements for control of superconducting quantum circuits." *Advances in Physics: X* 5: 1813626. doi:10.1080/23746149.2020.1813626.

Hardel, V., P.-A. Hervieux, and G. Manfredi. 2023. "Relaxation to Quantum Equilibrium and the Born Rule in Nelson's Stochastic Dynamics." *Foundations of Physics* 53: 64. doi:10.1007/s10701-023-00730-w.

Madelung, E. 1927. "Quantentheorie in hydrodynamischer Form." *Zeitschrift für Physik* 40 (3): 322–326. doi:10.1007/bf01400372.

Pearle, P. 1989. "Path integrals for the continuous spontaneous localization theory." *Foundations of Physics* 19: 995–1010. doi:10.1007/bf00692673.

Reddiger, M. 2017. "The Madelung Picture as a Foundation of Geometric Quantum Theory." *Foundations of Physics* 47: 1317–1367. doi:10.1007/s10701-017-0112-5.

Reddiger, M. 2026. "A solution of the quantum time of arrival problem via mathematical probability theory." *Philosophical Magazine*. doi:10.1080/14786435.2026.2627725.

Reddiger, M., and B. Poirier. 2023. "Towards a mathematical theory of the Madelung equations: Takabayasi's quantization condition, quantum quasi-irrotationality, variational formulations, and the Wallstrom phenomenon." *Journal of Physics A* 56: 195202. doi:10.1088/1751-8121/acc7db.

't Hooft, G. 2020. "Deterministic Quantum Mechanics: The Mathematical Equations." *Frontiers in Physics* 8: 253. doi:10.3389/fphy.2020.00253.

Towler, M. D., N. J. Russell, and A. Valentini. 2012. "Time scales for dynamical relaxation to the Born rule." *Proceedings of the Royal Society A* 468: 990–1013. doi:10.1098/rspa.2011.0598.

Valentini, A. 1991. "Signal-locality, uncertainty, and the subquantum H-theorem. I." *Physics Letters A* 156: 5–11. doi:10.1016/0375-9601(91)90116-p.

Valentini, A. 1991. "Signal-locality, uncertainty, and the subquantum H-theorem. II." *Physics Letters A* 158: 1–8. doi:10.1016/0375-9601(91)90330-b.

Valentini, A., and H. Westman. 2005. "Dynamical Origin of Quantum Probabilities." *Proceedings of the Royal Society A* 461: 253–272. arXiv:1007.3842.

von Neumann, J. 1932. *Mathematische Grundlagen der Quantenmechanik*. Berlin: Springer.

Wiseman, H. M. 2016. "Quantum State Effusion." arXiv:1609.06572.

Wu, J., B. B. Augstein, and C. Figueira de Morisson Faria. 2013. "Local dynamics in high-order-harmonic generation using Bohmian trajectories." *Physical Review A* 88: 023415. doi:10.1103/physreva.88.023415.
