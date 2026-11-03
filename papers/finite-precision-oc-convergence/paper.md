---
title: "Finite Specification, Ontological Indeterminism: The Gisin--Del Santo Program Converges with Autaxys Ontological Closure"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-07-28"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "PENDING-the QNFO archive"
status: "draft"
keywords: "finite-precision physics, ontological closure, indeterminism, real numbers, hidden variables, intuitionistic mathematics, constructive mathematics, D/R procedures, computable reals, creative time, consilience"
---

# Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure

## Abstract

We examine the Gisin--Del Santo program on finite-precision physics and its convergence with the Autaxys Ontological Closure (OC) framework. The Gisin--Del Santo program argues that (1) physical quantities contain only finite information, (2) real numbers are physically unreal --- they are *de facto* hidden variables of classical mechanics, (3) consequently, classical mechanics is ontologically indeterministic, and (4) this classical indeterminism explains many features traditionally attributed to quantum mechanics. We show that the OC framework, independently derived from D/R procedure operationalism, converges on identical structural conclusions: finite specification implies ontological openness, and real numbers beyond a computable modulus of convergence are not physically real. We identify seven convergent theses at certainty levels 3--5/5, note five critical caveats including the unresolved empirical equivalence problem, and present a cross-domain consilience analysis showing this finite-information principle is a structural invariant across physics, computer science, cognitive science, information theory, biology, and sociology. The paper is positioned as a contribution to the foundations of physics, emphasizing theoretical unification over novel empirical content.

## 1. Introduction

For centuries, the intimate symbiosis between mathematics and physics has driven scientific progress. But this relationship carries an implicit risk: mathematical structures developed independently of physics may, when applied to physical theories, introduce ontological commitments that nature does not honor. The real number system is the most consequential example. Formalized in the late nineteenth century by Dedekind, Cantor, and Weierstrass, the real numbers provide mathematics with a seamless continuum of infinite precision --- every real number contains an infinite sequence of digits, each fully determined. This formalism was adopted wholesale by physics, where physical quantities such as position, momentum, and energy are routinely modeled as real numbers.

In recent years, a growing body of work has challenged this assumption. Nicolas Gisin, Flavio Del Santo, and collaborators have argued that physical quantities cannot be infinitely precise --- that a finite region of spacetime cannot contain infinite information, that chaotic systems amplify inaccessible digits into macroscopically relevant effects, and that treating real numbers as "physically real" effectively makes them hidden variables that encode all future states [1--8]. Tein van der Lugt's Bachelor's thesis [9] synthesized this program, evaluated the prospects for using intuitionistic mathematics (Brouwer, Bishop) to formalize finite-precision physics, and proposed an alternative classical-mathematics formalism based on "domains of indeterminacy."

Independently, the Autaxys Ontological Closure (OC) framework has developed a parallel analysis from a different starting point: the operational definition of physical quantities via finite Determination/Resolution (D/R) procedures. OC holds that a quantity is physically real only if there exists a finite Turing-machine protocol that approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions [10]. This operationalizes the boundary between the *measurable* and the *imaginable* --- between what a finite procedure can actually produce and what mathematics can define but physics cannot access.

This paper documents the striking convergence between these two independently developed frameworks. We identify seven convergent theses, calibrate their certainty, present five critical caveats (including the unresolved empirical equivalence problem), and provide a cross-domain consilience analysis showing that the finite-information principle is a structural invariant across six disciplines.

The structure of this paper is as follows. Section 2 summarizes the Gisin--Del Santo program and the van der Lugt synthesis. Section 3 presents the OC framework in its operational formulation. Section 4 enumerates the seven convergent theses with evidence and certainty calibration. Section 5 presents the cross-domain consilience analysis. Section 6 documents critical caveats and the red-team audit findings. Section 7 concludes with open questions and research directions.

---

## 2. The Gisin--Del Santo Program

### 2.1 Real Numbers Are the Hidden Variables of Classical Mechanics

Gisin's core argument [1, 4] proceeds as follows. Consider a chaotic classical dynamical system. The equations of motion are deterministic, and the entire trajectory $\vec{x}(t), \vec{p}(t)$ is fully determined by the initial conditions $\vec{x}(0), \vec{p}(0)$. For chaotic systems, the leading digits of $\vec{x}(t)$ depend on digits far down the series of $\vec{x}(0)$. These far-down digits are *inaccessible* --- no measurement can determine them. Yet standard classical mechanics, by modeling initial conditions as real numbers, asserts they exist as fully determined physical quantities.

Gisin observes that this is structurally identical to hidden-variable theories: the real numbers encode all future states in their infinite digit sequences, exactly as hidden variables would. Since hidden variables are physically unreal, real numbers are physically unreal. Classical mechanics, properly understood, is indeterministic.

### 2.2 Physics Without Determinism

Del Santo and Gisin [2] develop this into a full alternative theory of classical mechanics. They propose *finite information quantities* (FIQs): at each point in time, a physical quantity is only determined up to finite precision. The digits beyond that precision are genuinely indeterminate --- not merely unknown, but ontologically undefined. When a chaotic system amplifies an undetermined digit into a macroscopically relevant one, that digit must become determinate through a process they identify as a *classical measurement problem*, structurally parallel to the quantum measurement problem.

The alternative theory makes precisely the same empirical predictions as standard classical mechanics. The difference is ontological: where standard theory treats all digits as determined *ab initio* (making God "play all dice at the big-bang" [1]), the FIQ theory treats undetermined digits as becoming determinate through time-developing processes. This distinction between *geometric time* (deterministic parametrization) and *creative time* (novel information creation) is developed further in [5].

### 2.3 Intuitionistic Mathematics and Physics

Gisin [8] and van der Lugt [9] explore whether intuitionistic mathematics --- Brouwer's constructive mathematics in which real numbers are time-developing choice sequences rather than completed infinite objects --- can provide the mathematical language for finite-precision physics. The appeal is clear: intuitionistic reals are processes that develop in time, with only finite information at each moment, matching the FIQ ontology.

Van der Lugt's analysis [9, Chapter 4] reaches a cautious negative conclusion. The key problem is that intuitionistic time --- the time of Brouwer's Creating Subject --- is fundamentally *human*-centered. It equates physical time with the temporal development of a mathematician's consciousness. This anthropocentrism blocks direct application to physics. Van der Lugt's Chapter 5 proposes an alternative: a classical-mathematics formalism using "domains of indeterminacy" --- open covers that represent the precision bound at each moment, with indeterminism arising from the choice of which open set a trajectory falls into when it crosses a domain boundary.

### 2.4 Quantum Features from Classical Indeterminism

The most recent development in the program [7] argues that many features traditionally attributed to quantum mechanics --- the measurement problem, Wigner's friend paradox, single-particle nonlocality, no-cloning --- have clear classical analogues in an indeterministic physics. What is uniquely quantum, they argue, reduces to phenomena involving $\hbar$, i.e., incompatible observables. This implies that classical and quantum indeterminism are manifestations of the same underlying principle: finite information in physical systems.

---

## 3. Autaxys Ontological Closure (OC)

### 3.1 Core Principle

The OC framework [10] provides an operational criterion for physical reality:

> A quantity is *physically real* only if there exists a finite Turing-machine protocol --- a Determination/Resolution (D/R) procedure --- that approximates it with a computable modulus of convergence, yielding measurement-distinguishable predictions.

This criterion operationalizes the boundary between the *measurable* (what a finite procedure can actually produce) and the *imaginable* (what mathematics can define but no finite procedure can access). It motivates the term "Ontological Closure": physical reality is *closed under* D/R procedures --- nothing that cannot be generated by a finite procedure can be physically real.

### 3.2 Key Consequences

1. **Finite specification.** Every physically real quantity is specifiable by a finite amount of information --- the description of the D/R procedure and its convergence modulus.

2. **Ontological indeterminism.** The digits of a physical quantity beyond the current modulus of convergence are ontologically indeterminate --- there is no "fact of the matter" about them. They become determinate only through D/R procedure execution.

3. **Classical math operationalism.** Unlike intuitionistic approaches, OC uses classical mathematics (Turing machines, computable analysis) to formalize finite precision. It does not require revising the foundations of mathematics.

4. **Processual ontology.** D/R procedure execution is a time-developing process. This provides a mathematical framework for "creative time" --- each computational step determines previously indeterminate information.

### 3.3 The measurable-vs-imaginable Project

The OC framework is part of a broader research program ("measurable-vs-imaginable") investigating computable reals as the physics/mathematics boundary. This program examines which mathematical objects survive the D/R procedure criterion and which are relegated to the imaginable --- mathematically well-defined but physically inaccessible.

---

## 4. Seven Convergent Theses

We now enumerate the seven points of convergence between the Gisin--Del Santo program and the OC framework, with certainty calibration on a 5-point scale (1 = speculative, 5 = robustly established).

### Thesis 1: Real Numbers Are Not Physically Real [5/5]

**Gisin [1]:** "Real numbers are the hidden variables of classical mechanics." The infinite digits of a real number encode all future states of a chaotic system, making them indistinguishable from hidden variables. Since hidden variables are physically unreal, real numbers are physically unreal.

**OC alignment:** This is precisely the OC boundary between measurable and imaginable. The real number $\sqrt{2}$ is mathematically well-defined (imaginable) but cannot be "measured" --- only approximated by a D/R procedure (measurable). The two frameworks identify the same ontological distinction.

**Evidence:** Gisin (1909.04514), van der Lugt (2108.05735), Del Santo & Gisin (1909.03697). The Bekenstein bound provides an independent physical constraint: a finite region of spacetime cannot contain infinite information.

**Certainty: 5/5.**

### Thesis 2: Finite Precision Entails Ontological Indeterminism [5/5]

**Core argument:** If initial conditions are only finitely precise, the future digits that chaotic dynamics amplifies are *indeterminate* until they become relevant. Classical mechanics becomes indeterministic --- not because of measurement limitations, but ontologically.

**OC alignment:** The OC modulus of convergence provides exactly this: at time $t$, only digits up to precision $\varepsilon(t)$ are physically determined. Digits beyond $\varepsilon(t)$ correspond to D/R procedures not yet executed --- they are indeterminate.

**Evidence:** Del Santo & Gisin (1909.03697), Gisin (1803.06824), Del Santo (2003.07411), Del Santo & Gisin (2101.04134, Relativity of Indeterminacy). Dowek (2013) provides the information-theoretic basis.

**Certainty: 5/5.**

### Thesis 3: The Classical Measurement Problem [4/5]

**Van der Lugt [9, S3.1.1]:** "The orthodox interpretation of classical mechanics suffers from a classical analogue of the measurement problem." In finite-precision physics, a measurement (or collapse-like process) is needed to determine the $n$th digit when it becomes macroscopically relevant.

**OC alignment:** The D/R procedure *is* the measurement protocol. The modulus of convergence determines *when* a measurement (computation) is needed. This operationalizes the classical measurement problem.

**Evidence:** Van der Lugt (2021), Del Santo & Gisin (2019). Kwok (2020, 2005.07079) provides a critical perspective --- the argument may have a loophole --- which we address in the caveats.

**Certainty: 4/5** (the existence of a classical analogue is clear; the mechanism --- collapse-like vs. epistemic --- is contested).

### Thesis 4: Intuitionistic Math Is Conceptually Blocked for Physics [3/5]

**Van der Lugt [9, Chapter 4]:** "Applying intuitionistic philosophy to physics is not straightforward and perhaps even impossible." The Creating Subject's time is human-centered --- it equates physical time with a mathematician's consciousness --- blocking direct physical application.

**OC alignment:** OC avoids this problem by using *classical mathematics* (Turing machines, computable analysis) to formalize finite precision, exactly as van der Lugt's Chapter 5 proposes.

**Evidence:** Van der Lugt (2021, S4.3), Ardourel (2012), Crosilla (2021), van Atten (2018, Brouwer-Kripke Schema).

**Certainty: 3/5** (van der Lugt's own conclusion is cautious; alternative approaches may exist).

### Thesis 5: Creative Time vs. Geometric Time [4/5]

**Del Santo & Gisin [5]:** Two concepts of time --- *geometric time* (deterministic parametrization, block universe) and *creative time* (novel information created when indeterminate events become determinate). The present separates potential future from determined past.

**OC alignment:** D/R procedure execution is the *creative act* --- each computational step determines previously indeterminate digits. The modulus of convergence defines the temporal structure of becoming.

**Evidence:** Del Santo & Gisin (2024, 2404.06566), Gisin (2020, 2002.01653, Nature Physics), Del Santo & Gisin (2022, The Open Past), Gisin (2016, Time Really Passes).

**Certainty: 4/5.**

### Thesis 6: Quantum Indeterminism Is Classical Indeterminism Plus $\hbar$ [4/5]

**Del Santo & Gisin [7]:** "Which features of quantum physics are not fundamentally quantum but are due to indeterminism?" The measurement problem, Wigner's friend, no-cloning, and other "quantum" features have clear classical analogues in an indeterministic physics. What is uniquely quantum reduces to incompatible observables ($\hbar$).

**OC alignment:** If OC introduces indeterminism at the classical level via D/R procedure finiteness, quantum indeterminism is a manifestation of the same principle at a different scale --- not an additional mystery.

**Evidence:** Del Santo & Gisin (2024, 2409.10601), Fankhauser et al. (2024, Epistemic Horizons), \"Ottinger (2023, Stochastic bra-ket), Spekkens' toy theory precursor.

**Certainty: 4/5** (compelling argument for classical analogues; uniqueness of $\hbar$-dependent features is well-established).

### Thesis 7: Top-Down Causation and Strong Emergence [3/5]

**Drossel & Ellis [11--13]:** Top-down causation and strong emergence become possible in a finite-precision framework because the microscopic level is causally open to macroscopic context. Determinism at the micro-level precludes genuine emergence.

**OC alignment:** D/R procedures are inherently contextual --- the procedure that generates a physical quantity depends on the operational context. This provides a formal basis for top-down causation.

**Evidence:** Drossel (2019, Strong Emergence), Drossel (2023, Passage of Time), Drossel & Ellis (2018, Contextual Wavefunction Collapse).

**Certainty: 3/5** (compelling philosophical argument; formal operationalization via OC is early-stage).

---

## 5. Cross-Domain Consilience

The finite-information principle is not confined to physics. A structured cross-domain analysis (full details in `artifacts/consilience-gate.md`) reveals that the same structural dynamic --- finite specification $\rightarrow$ ontological openness $\rightarrow$ processual determination --- appears across six disciplines:

| Domain | Finite Specification | Indeterminism Mechanism | Time Character |
|:-------|:---------------------|:------------------------|:---------------|
| **Physics** | Bekenstein bound, FIQ | Chaotic amplification of unspecified digits | Creative time |
| **Computer Science** | Fixed-point arithmetic, program termination | Lazy evaluation, non-deterministic choice | Sequential execution |
| **Cognitive Science** | Just-noticeable-difference, bounded rationality | Perceptual filling-in, change blindness | Subjective Now |
| **Information Theory** | Channel capacity, rate-distortion | Equivocation, quantization noise | Sequential decoding |
| **Biology** | Genetic specification, canalization depth | Developmental noise, phenotypic plasticity | Developmental time |
| **Sociology** | Explicit rules, bureaucratic categories | Tacit knowledge, informal norms | Kairos vs chronos |

**Synthesis Meta-Principle:** All six domains exhibit an identical structural dynamic: *finite specification $\rightarrow$ ontological openness $\rightarrow$ processual determination*. The invariant is independent of substrate --- it appears in physical dynamics, computation, perception, information transmission, development, and social organization.

**Frontier Question:** If this principle is universal, does the OC framework imply that agency and free will are not philosophical problems but direct consequences of finite-precision physics?

---

## 6. Critical Caveats and Red-Team Findings

A formal red-team audit (`artifacts/red-team-audit.md`) applied the five-adversary challenge protocol (null-hypothesis defender, methodology skeptic, better-alternative proposer, scaling pessimist, resource realist). Five findings emerged:

### R1: Empirical Equivalence [5/5] [HIGH]

**Finding:** The Gisin--Del Santo program and the OC framework have not produced experimentally testable predictions distinct from standard physics. The finite-precision theory is *empirically equivalent* to standard real-numbered classical mechanics. By Popperian standards, this makes both frameworks unfalsifiable --- they are philosophy of physics, not physics.

**Response:** We acknowledge this limitation and position this paper as a contribution to the *foundations of physics*, where theoretical coherence, conceptual unification, and explanatory power are the relevant criteria. The empirical equivalence is not a bug --- it is a feature of any framework that aims to reinterpret existing physics rather than replace it. However, we note that an *experimentum crucis* would require measuring the "collapse" of an undetermined FIQ digit --- a challenge that may become addressable with advances in precision metrology.

### R2: Bibliographic Coverage [3/5] [MEDIUM]

**Finding:** The bibliography was generated from a ConnectedPapers graph, not a systematic literature review. Important critical or adjacent literature may be missing.

**Response:** We acknowledge this limitation. The ConnectedPapers graph for a well-cited seed paper (van der Lugt 2021, citing Gisin 2019) captures the core citation neighborhood. Additional search would supplement coverage; this is flagged as future work.

### R3: Alternative Frameworks [3/5] [MEDIUM]

**Finding:** Constructor theory (Deutsch), digital physics (Fredkin, Wolfram), causal set theory (Sorkin), and cellular automaton interpretations ('t Hooft) all share elements with the finite-information principle. The present paper does not compare against these alternatives.

**Response:** A comparative analysis against alternative finite-information frameworks is planned as a follow-up paper. The present paper's contribution is specifically the OC--Gisin/Del Santo convergence; broader comparison requires separate treatment.

### R4: Scaling Limitations [3/5] [MEDIUM]

**Finding:** Van der Lugt's Chapter 5 formalism treats a one-dimensional state space with discrete-time shift map. Generalizing to Hamiltonian mechanics on symplectic manifolds, relativistic field theory, or quantum field theory is an open problem.

**Response:** Acknowledged. The toy-model nature of the van der Lugt formalism is a limitation, not a failure. Generalization is active research.

### R5: No Experimental Predictions [5/5] [HIGH]

**Finding:** This is the strongest form of R1. Neither the Gisin--Del Santo program nor the OC framework has produced a *differential empirical prediction* --- something that would be observed if the framework is correct but not if standard physics is correct.

**Response:** Same as R1. We position this paper as foundations/philosophy of physics. The value proposition is theoretical unification and consilience across domains, not novel empirical content. We explicitly invite experimental proposals.

---

## 7. Conclusion and Open Questions

The Gisin--Del Santo program and the Autaxys OC framework converge on the principle that physical quantities contain only finite information, and that recognizing this principle yields ontological indeterminism, a processual conception of time, and a reinterpretation of quantum mechanics as classical indeterminism plus incompatible observables. The cross-domain consilience analysis shows this principle is a structural invariant across physics, computation, cognition, information theory, biology, and sociology.

### 7.1 Prioritized Open Questions

| # | Question | Priority |
|---|----------|----------|
| Q1 | Can FIQs be formalized as D/R procedures with computable modulus? | High |
| Q2 | Does the Bekenstein bound imply a universal modulus of convergence? | High |
| Q3 | Can van der Lugt's "domains of indeterminacy" be generalized to Hamiltonian phase space? | Medium |
| Q4 | Is there *any* experiment that could break the empirical equivalence? | High |
| Q5 | Does the epistemic horizons theorem (Fankhauser 2024) generalize to OC-framework agents? | Medium |
| Q6 | Can potentiality realism's propensities be expressed as probability measures over D/R outputs? | Medium |
| Q7 | Can collapse models (Gisin 2017) be reinterpreted as modulus-of-convergence transitions? | Speculative |
| Q8 | Which alternative approaches (constructor theory, digital physics, cellular automata) converge with or diverge from this analysis? | Medium |

### 7.2 Practical Applications

Despite the empirical equivalence limitation, the framework has practical implications:

1. **Numerical simulation bounds:** Every simulation has an inherent $\varepsilon$-bound determined by computational resources --- this is not an artifact but reflects ontology.
2. **Quantum computing resource estimation:** OC provides lower bounds on D/R procedures needed for specific computations.
3. **Chaotic system predictability:** The link between chaos and finite precision formalizes in-principle limits on long-range prediction.
4. **Measurement device design:** OC modulus of convergence specifies *when* a measurement must occur for a given precision.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Conflicts of Interest:** The author declares no competing interests.

**Ethics Approval:** Not applicable --- this research did not involve human participants, animal subjects, or sensitive data.

**Consent to Participate:** Not applicable.

**Author Contributions:** Sole author --- conceptualization, investigation, writing, analysis.

**Data Availability:** All cited papers are publicly available on arXiv. The bibliography (ConnectedPapers export) and synthesis document are available in the project repository.

**Materials Availability:** Not applicable.

**Code Availability:** Analysis scripts and the synthesis document are available at the project repository. The `build-paper.py` pipeline is part of the QNFO research skill (`research` v2.24).

**Use of Artificial Intelligence:** DeepChat (deepseek-v4-pro) was used as a research assistant for literature triage, synthesis document drafting, red-team audit, and cross-domain consilience analysis. All substantive claims, theses, and certainty calibrations were verified by the human author against primary sources.

---

## References

[1] N. Gisin, "Real Numbers are the Hidden Variables of Classical Mechanics," *Quantum Studies: Mathematics and Foundations* **7**, 197--201 (2019). arXiv:1909.04514.

[2] F. Del Santo and N. Gisin, "Physics without determinism: Alternative interpretations of classical physics," *Physical Review A* **100**, 062107 (2019). arXiv:1909.03697.

[3] N. Gisin, "Indeterminism in Physics, Classical Chaos and Bohmian Mechanics: Are Real Numbers Really Real?" *Erkenntnis* **86**, 1469--1481 (2019). arXiv:1803.06824.

[4] N. Gisin, "Indeterminism in physics and intuitionistic mathematics," *Synthese* **199**, 13345--13371 (2021). arXiv:2011.02348.

[5] F. Del Santo and N. Gisin, "Creative and geometric times in physics, mathematics, logic, and philosophy," arXiv:2404.06566 (2024).

[6] F. Del Santo and N. Gisin, "Potentiality realism: a realistic and indeterministic physics based on propensities," *European Journal for Philosophy of Science* **13** (2023). arXiv:2305.02429.

[7] F. Del Santo and N. Gisin, "Which features of quantum physics are not fundamentally quantum but are due to indeterminism?" arXiv:2409.10601 (2024).

[8] N. Gisin, "Classical and intuitionistic mathematical languages shape our understanding of time in physics," *Nature Physics* **16**, 114--116 (2020). arXiv:2002.01653.

[9] T. van der Lugt, "Indeterministic finite-precision physics and intuitionistic mathematics," Bachelor's thesis, Radboud University Nijmegen (2021). arXiv:2108.05735.

[10] R. B. Quni-Gudzinas, "Autaxys Ontological Closure," QNFO Research Program, working papers (2026). See `measurable-vs-imaginable` project.

[11] B. Drossel, "Strong Emergence in Condensed Matter Physics," arXiv:1909.01134 (2019).

[12] B. Drossel, "The passage of time and top-down causation," arXiv:2303.06352 (2023).

[13] B. Drossel and G. Ellis, "Contextual Wavefunction collapse: an integrated theory of quantum measurement," *New Journal of Physics* **20** (2018). arXiv:1807.08171.

[14] F. Del Santo and N. Gisin, "The Open Past in an Indeterministic Physics," *Foundations of Physics* **53** (2022). arXiv:2205.11547.

[15] F. Del Santo and N. Gisin, "The Relativity of Indeterminacy," *Entropy* **23**, 1326 (2021). arXiv:2101.04134.

[16] F. Del Santo, "Indeterminism, Causality and Information: Has Physics Ever Been Deterministic?" In *Undecidability, Uncomputability, and Unpredictability* (2020). arXiv:2003.07411.

[17] N. Gisin, "Collapse. What else," arXiv:1701.08300 (2017).

[18] N. Gisin, "Time Really Passes, Science Can't Deny That," arXiv:1602.01497 (2016).

[19] J. Fankhauser, T. Gonda, and G. De les Coves, "Epistemic Horizons From Deterministic Laws: Lessons From a Nomic Toy Theory," arXiv:2406.17581 (2024).

[20] A. Majhi, "Cauchy's Logico-Linguistic Slip, the Heisenberg Uncertainty Principle and a Semantic Dilemma Concerning 'Quantum Gravity'," *International Journal of Theoretical Physics* **61** (2022). arXiv:2204.00418.

[21] A. Majhi, "Resolving the Singularity by Looking at the Dot and Demonstrating the Undecidability of the Continuum Hypothesis," *Foundations of Science* **29**, 405--440 (2022).

[22] A. Majhi, "Logic, Philosophy and Physics: A Critical Commentary on the Dilemma of Categories," *Axiomathes* **32**, 1415--1431 (2021). arXiv:2110.11230.

[23] A. Majhi, "The undecidable charge gap and the oil drop experiment," *Pramana* (2024). arXiv:2401.05460.

[24] J. Lenchner, "A Finitist's Manifesto: Do we need to Reformulate the Foundations of Mathematics?" arXiv:2009.06485 (2020).

[25] W. Kwok, "A Loophole in an Argument for Interpreting Classical Physics Indeterministically," arXiv:2005.07079 (2020).

[26] G. Dowek, "Real Numbers, Chaos, and the Principle of a Bounded Density of Information," *LNCS* **7921**, 347--358 (2013).

[27] L. Crosilla, "Bishop's Mathematics: A Philosophical Perspective," (2021).

[28] M. van Atten, "The Creating Subject, the Brouwer-Kripke Schema, and infinite proofs," *Indagationes Mathematicae* **29**, 1565--1635 (2018). arXiv:1805.00404.

[29] H. C. \"Ottinger, "Stochastic bra-ket interpretation of quantum mechanics," *Journal of Physics Communications* (2023). arXiv:2309.03151.

[30] V. Ardourel, "La physique dans la recherche en math\'ematiques constructives," *Philosophia Scientiae* **16**(1), 65--84 (2012).

[31] M. E. Miller, "Worldly imprecision," *Philosophical Studies* **178**, 2895--2911 (2020).

[32] G. Ellis, K. Meissner, and H. Nicolai, "The physics of infinity," *Nature Physics* **14**, 770--772 (2018).

[33] N. Gisin, "The Multiverse Pandemic," arXiv:2210.05377 (2022).

[34] N. Gisin, "Propensities in a non-deterministic physics," *Synthese* **89**, 287--297 (1991).

[35] N. Gisin, "Propensities and the state-property structure of classical and quantum systems," *Journal of Mathematical Physics* **25**, 2260--2265 (1984).

[36] F. Del Santo, "Striving for Realism, not for Determinism: Historical Misconceptions on Einstein and Bohm," arXiv:1807.07656 (2018).

[37] B. Drossel, "On the Relation Between the Second Law of Thermodynamics and Classical and Quantum Mechanics," arXiv:1408.6358 (2014).

[38] K. Bong et al., "A strong no-go theorem on the Wigner's friend paradox," *Nature Physics* **16**, 1199--1205 (2019). arXiv:1907.05607.

[39] G. 't Hooft, "Interpreting Quantum Mechanics," (2016). doi:10.1007/978-3-319-41285-6_3.

[40] A. Majhi, "A Logico-Linguistic Inquiry into the Foundations of Physics: Part 1," *Axiomathes* (2021). arXiv:2110.03514.

[41] N. Gisin, "Mathematical languages shape our understanding of time in physics," *Nature Physics* **16**, 114--116 (2020). arXiv:2002.01653.
