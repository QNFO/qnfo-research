---
title: "The Informational Universe: A Synthesis of Holographic Bounds, Thermodynamic Gravity, and Finite-Dimensional Quantum Constraints"
author: "QNFO Research"
date: "2026-07-21"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "10.5281/zenodo.21480126"
status: "draft"
bibliography: artifacts/refs.bib
---

**Author:** QNFO Research | **Date:** 2026-07-21 | **License:** QNFO-ULA: https://legal.qnfo.org/

---

## Abstract

We present a synthesis of three established research programs — the holographic entropy bound, thermodynamic gravity, and the finite-dimensional Hilbert space constraint — into a unified informational framework for physical law. The framework's core claim is that entanglement entropy in any finite spacetime region is bounded by the region's boundary area (in Planck units), and that this bound constrains not merely the description of physical states but the admissible form of physical law. We organize the synthesis around three tiers of decreasing empirical support: (1) the Bekenstein-Jacobson thermodynamic derivation of gravitational dynamics from entropy constraints, which has [mainstream interpretation] status; (2) the conjecture that entanglement entropy constitutes spacetime geometry beyond AdS/CFT, which remains [speculative]; and (3) the ontological claim that information is the fundamental substrate of physical reality, which we flag as [PHILOSOPHY] when departing from physics. We provide a calibration register of five falsifiable predictions with target check dates from 2028–2035, and a worked example: the derivation of the Einstein field equations from the entanglement first law in the Jacobson formalism. The framework's primary contribution is not a new physical theory but a logical structure that makes explicit the dependency chain between premises whose conjunction implies informational universe claims — enabling future experimental and theoretical work to target the weakest links with precision.

---

## 1. Introduction: What Would It Mean for Information to Be Fundamental?

### 1.1 Three Interpretations of "Informational Universe"

The phrase "the universe is informational" admits at least three distinct interpretations, which the literature frequently conflates [@wheeler1989information; @zeilinger1999foundational; @chiribella2011informational]:

1. **Epistemic**: Physical theories are models constructed from information we can access. This is Wheeler's "it from bit" as methodological principle — true but not novel [PHILOSOPHY].

2. **Nomological**: The laws of physics take a form constrained by information-theoretic bounds (Bekenstein bound, holographic principle). This is the interpretation we defend in this paper — it is [mainstream interpretation] for some sub-claims and [speculative] for others.

3. **Ontological**: Information IS what exists; matter, spacetime, and fields are epiphenomena of information processing. This is the strongest claim and the least supported — we flag all such claims [PHILOSOPHY].

This paper adopts interpretation (2) as its core framework and treats (3) as a speculative extension explicitly separated from the physics. The contribution is not to assert either claim but to organize the evidential basis so that the logical dependency chain is transparent: which assumptions must hold for which conclusions to follow.

### 1.2 The Reformulated Core Claim

Following the Phase 0 reformulation from the parent project "Correlated Universe 1.0" [PROJECT-PLAN.md, 2026-07-21], the core claim under evaluation is:

> "Entanglement entropy in any finite region of spacetime is fully determined by a finite-dimensional Hilbert space whose dimension is bounded by $\exp(A/4\ell_{P}^{2})$, where $A$ is the region's boundary area. No physical observable requires more than this many independent bits — and physical laws governing those observables are constrained by this bound."

**Falsification condition:** If entanglement entropy in a region of boundary area $A$ is measured (or theoretically derived) to EXCEED $A/4\ell_{P}^{2}$ in Planck units, the core claim is falsified. This condition is [speculative] in that no experiment currently probes the Planck scale, but it is logically precise.

### 1.3 Structure of This Paper

| Section | Topic | Paradigm Candidate | Certainty |
|:--------|:------|:-------------------|:----------|
| §2 | Holographic bounds: Bekenstein, Bousso, Page | PS-F | [established] / [mainstream interpretation] |
| §3 | Thermodynamic gravity: Jacobson, Padmanabhan | PS-F | [mainstream interpretation] |
| §4 | Entanglement as spacetime geometry | PS-E | [speculative] |
| §5 | Finite-dimensional Hilbert space constraint | PS-A | [speculative] |
| §6 | Information-theoretic foundations of QM: Chiribella, Hardy | PS-D | [mainstream interpretation] |
| §7 | Ontological implications | PS-C | [PHILOSOPHY] |
| §8 | Calibration register, limitations, falsifiability | Hedge | — |

---

## 2. The Holographic Foundation

### 2.1 Bekenstein's Bound and Black Hole Thermodynamics

The empirical anchor of the informational-universe framework is black hole thermodynamics. Bekenstein [@bekenstein1973black] proposed that black holes carry entropy proportional to their horizon area: $S_{BH} = A/4\ell_{P}^2$. Hawking [@hawking1975particle] showed that black holes radiate with a temperature $T = \kappa/2\pi$, confirming the thermodynamic interpretation. Together, these results establish that a region of spacetime bounded by a horizon of area $A$ contains at most $\exp(A/4\ell_{P}^2)$ independent quantum states — the Bekenstein bound in its strongest form [@page2018bekenstein; @bousso2002holographic].

**Certainty:** [established]. Black hole thermodynamics is among the most secure results in theoretical physics, resting on the intersection of general relativity and quantum field theory.

**What this implies:** If the Bekenstein-Hawking entropy is truly a count of microstates, then quantum gravity must operate in a Hilbert space whose dimension is set by boundary area. This is the logical bridge to the finite-dimensional constraint (§5).

### 2.2 The Generalized Covariant Entropy Bound

Bousso [@bousso2002holographic] generalized the Bekenstein bound to arbitrary spacetimes via light-sheet techniques. The covariant entropy bound states that the entropy flux through any light-sheet is bounded by the area difference of its initial and final surfaces, in Planck units. This result is:

- **Proven** for weakly gravitating systems (the "Bekenstein bound" regime) [established]
- **Conjectured** for strongly gravitating, dynamical spacetimes [speculative]

The bound has survived numerous attempted counterexamples [@bousso2002holographic]. No physically reasonable system has been shown to violate it by more than an $O(1)$ factor.

**What this implies:** If the covariant entropy bound holds universally, then the holographic principle is not an AdS/CFT-specific property — it is a general feature of any quantum theory of gravity. The map/territory distinction is important: the bound constrains *how much* a physical system can be described with $N$ bits; it does not assert that those bits ARE the physical system. That latter claim belongs to §7 and is flagged [PHILOSOPHY].

### 2.3 AdS/CFT: A Concrete Realization

Maldacena's AdS/CFT correspondence [@maldacena1999large] provides the most rigorous realization of the holographic principle: a $(d+1)$-dimensional theory of quantum gravity in anti-de Sitter space is exactly equivalent to a $d$-dimensional conformal field theory on its boundary. This is a mathematical duality — not merely a bound but an identity. However:

**Limitation [debated]:** AdS/CFT is proven for AdS geometries, which have negative cosmological constant. Our universe has a positive cosmological constant. Whether holography extends to de Sitter space is an open question [@witten2001quantum; @strominger2001ds].

**What the informational-universe framework adds:** Nothing — we do not claim to solve the dS/CFT problem. We claim only that the covariant entropy bound AND the Jacobson thermodynamic derivation (§3) provide independent, model-agnostic evidence for holographic constraints, without requiring AdS/CFT's full mathematical machinery. The burden of proof is on the skeptic to show why these constraints would hold in AdS but fail in our universe.

---

## 3. Thermodynamic Gravity: Einstein Equations from Entropy

### 3.1 Jacobson's Derivation

In a remarkable 1995 paper, Jacobson [@jacobson1995thermodynamics] showed that the Einstein field equations follow from the proportionality of entropy to horizon area, together with the Clausius relation $\delta Q = T dS$, applied to local Rindler horizons. The derivation requires only:

1. The entropy of any local Rindler horizon is proportional to its area (Bekenstein's insight, generalized)
2. Energy flux across the horizon obeys thermodynamic relations
3. Spacetime is described by a Lorentzian metric

From these premises, Jacobson derived $R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu} = 8\pi G T_{\mu\nu}$ — the full Einstein equations. The cosmological constant emerges as an integration constant.

**Certainty:** [mainstream interpretation]. The derivation is mathematically sound. The interpretive question is whether this shows that gravity IS thermodynamic (emergent), or merely that Einstein's equations CAN BE expressed in thermodynamic language (descriptive). We take no position on this interpretive question — the framework works either way.

### 3.2 The Entanglement First Law Extension

The Jacobson derivation has been extended via the entanglement first law [@blanco2013entanglement; @lin2014entanglement]. For any spatial region, the variation of entanglement entropy satisfies:

$$\delta S_{EE} = \delta \langle H_{mod} \rangle$$

where $H_{mod}$ is the modular Hamiltonian. In the semi-classical limit, this becomes the gravitational first law, and Einstein's equations emerge as the consistency condition. This connects the entanglement-based picture of §4 with the thermodynamic derivation.

### 3.3 Padmanabhan's Perspective: Gravity as an Emergent Phenomenon

Padmanabhan [@padmanabhan2010thermodynamical] has extensively developed the thermodynamic/emergent gravity program, showing that:

- The gravitational field equations can be derived from the equipartition of energy among microscopic degrees of freedom at the horizon
- The number of degrees of freedom scales as area (not volume), consistent with holography
- The dynamics of spacetime arise from the difference between surface and bulk degrees of freedom

**Limitation:** Padmanabhan's framework requires the existence of a yet-unknown microscopic theory of the "atoms of spacetime." The informational-universe hypothesis does not supply this theory — it identifies the constraints any such theory must satisfy.

### 3.4 What Jacobson Does NOT Show

Jacobson's derivation establishes that IF entropy is proportional to area AND thermodynamic relations hold, THEN Einstein's equations follow. It does NOT show:

1. That gravity is emergent rather than fundamental (interpretation-dependent)
2. That the derivation works for higher-curvature corrections or non-metric theories [speculative]
3. That information is ontologically prior to spacetime [PHILOSOPHY]

The informational-universe framework takes Jacobson's result as evidence for tier (2) of the hypothesis: physical laws are constrained by information-theoretic bounds. Whether those constraints imply emergence or fundamentality is a separate question.

---

## 4. Entanglement as Spacetime Geometry

### 4.1 Ryu-Takayanagi and Holographic Entanglement Entropy

Ryu and Takayanagi [@ryu2006holographic] proposed that in AdS/CFT, the entanglement entropy of a boundary region equals the area of a minimal surface in the bulk:

$$S_{EE}(A) = \frac{\text{Area}(\gamma_A)}{4G_N}$$

where $\gamma_A$ is the minimal surface homologous to region $A$ on the boundary. This formula, later proven by Lewkowycz and Maldacena, establishes a precise, quantitative relationship between entanglement on the boundary and geometry in the bulk.

**Certainty:** [established] within AdS/CFT. The formula has passed numerous consistency checks and reproduces known results.

### 4.2 Van Raamsdonk: Building Spacetime from Entanglement

Van Raamsdonk [@vanraamsdonk2010building] posed the question: what happens to the bulk geometry when boundary entanglement is removed? Using the Ryu-Takayanagi formula, he showed that reducing entanglement between two boundary regions increases the proper distance between them in the bulk — in the limit of zero entanglement, the bulk spacetime disconnects. His provocative conclusion: "Entanglement is the glue that holds spacetime together."

**Certainty:** [speculative] as a general principle, but [mainstream interpretation] within AdS/CFT. The result assumes AdS/CFT duality, which is not proven to generalize.

### 4.3 Swingle's Tensor Network Picture

Swingle [@swingle2012entanglement] proposed that the AdS/CFT correspondence can be understood in terms of tensor networks, specifically the Multiscale Entanglement Renormalization Ansatz (MERA). In this picture:

- The MERA network, which efficiently represents ground states of critical systems, has the geometry of a spatial slice of AdS space
- Entanglement renormalization group flow naturally produces a holographic dimension
- The Ryu-Takayanagi formula emerges from the minimal cut through the tensor network

This provides an information-theoretic explanation of holography: the "bulk" dimension is an efficient representation of boundary entanglement patterns. **If** this generalizes beyond MERA-expressible states, it would constitute a derivation of spacetime from entanglement — not merely a dictionary between them.

### 4.4 ER = EPR and Quantum Error Correction

Maldacena and Susskind [@maldacena2013cool] conjectured that Einstein-Rosen bridges (wormholes) are equivalent to Einstein-Podolsky-Rosen entangled pairs: ER = EPR. In the AdS/CFT context, this means that any entangled state corresponds to a connected geometry. The AdS/CFT realization of this idea as quantum error correction [@almheiri2015bulk; @pastawski2015holographic] has provided a mathematically precise framework: the bulk spacetime is the code subspace of a boundary quantum error-correcting code.

**Certainty:** The QEC framework is [established] in AdS/CFT. ER=EPR as a general conjecture is [speculative].

**What this contributes:** The QEC-as-spacetime program is the strongest evidence for tier (2) of the informational-universe hypothesis — it shows that under specific (AdS) conditions, bulk geometry is literally constructed from boundary information. The open question is universality.

---

## 5. The Finite-Dimensional Hilbert Space Constraint

### 5.1 Bao-Carroll-Singh: "Locally Finite-Dimensional"

In a bold conjecture, Bao, Carroll, and Singh [@bao2017hilbert] argued that the Hilbert space of quantum gravity is locally finite-dimensional — in any finite region of spacetime, the dimension of the Hilbert space is finite and bounded by $\exp(A/4G\hbar)$. Their key arguments:

1. **Bekenstein bound**: Any region of area $A$ has at most $\sim\exp(A/4\ell_{P}^{2})$ independent quantum states
2. **No infinite entanglement**: In local quantum field theory, entanglement entropy between a region and its complement diverges (the "UV catastrophe") — but with a short-distance cutoff at Planck scale, this divergence is regulated
3. **Black hole complementarity**: The black hole interior is not an independent region of Hilbert space — it is encoded in the exterior's degrees of freedom

**Certainty:** [speculative]. The conjecture is logically motivated but not derived from a complete theory.

### 5.2 Contra: The QFT Case for Infinite Dimensions

The standard framework of quantum field theory in curved spacetime [@birrell1984quantum] assumes an infinite-dimensional Hilbert space. The Unruh effect (accelerated observers see a thermal bath), Hawking radiation, and inflationary perturbations are all derived in this framework and have passed empirical tests. If the Hilbert space dimension is finite, QFT in curved spacetime must be an effective description valid only below the cutoff — but WHERE the cutoff lies matters enormously.

**The challenge:** If the cutoff is at the Planck scale ($\sim 10^{19}$ GeV), QFT's predictions are effectively unchanged for all experimentally accessible energies. The finite-dimensional constraint becomes operationally vacuous. The constraint becomes meaningful only if:
- (a) The cutoff is lower than expected (e.g., at TeV scale, as in some large-extra-dimension scenarios), OR
- (b) The finite-dimensional structure generates specific, observable deviations from QFT predictions

Neither condition is currently met. **The informational-universe framework must explicitly own this limitation.**

### 5.3 Page's Bekenstein Bound Analysis

Page [@page2018bekenstein] provides an authoritative review of the Bekenstein bound: $S \le 2\pi RE/\hbar c$. He emphasizes that the bound is a "loose" inequality — saturating it requires extreme conditions (black holes). For ordinary matter, the actual entropy is far below the bound. This means the finite-dimensional constraint, while logically valid, does not constrain most physical systems in a computationally meaningful way.

**Nevertheless:** The existence of the bound, even if loose, is a structural constraint on the theory. It tells us that physical Hilbert space is NOT the full infinite-dimensional space that naive QFT would suggest. The finite dimension is enormous — but "enormous but finite" and "infinite" are different types, with different mathematical properties. This type distinction matters for the ultimate theory of quantum gravity.

---

## 6. Information-Theoretic Foundations of Quantum Mechanics

### 6.1 Chiribella-D'Ariano-Perinotti: QM from Information Principles

Chiribella, D'Ariano, and Perinotti [@chiribella2011informational] derived the mathematical structure of quantum mechanics from five information-theoretic postulates:

1. **Causality**: No signaling from future to past
2. **Perfect distinguishability**: Orthogonal states are perfectly distinguishable
3. **Local distinguishability**: States of composite systems are determined by local measurements
4. **Pure compression**: There exists a pure state that maximizes measurement information
5. **Atomicity of composition**: The composition of two atomic systems is atomic

From these postulates, they derived: the Hilbert space structure, complex amplitudes, the Born rule, and unitary evolution. This is an axiomatic reconstruction of QM from purely information-theoretic principles.

**Certainty:** [mainstream interpretation]. The derivation is mathematically rigorous. It shows that QM's mathematical structure follows from information-theoretic constraints — not that it had to follow from them (there may be alternative sets of axioms).

### 6.2 Hardy's Axiomatic Approach

Hardy [@hardy2001quantum; @hardy2011operational] independently derived QM from operational axioms. His "five reasonable axioms" similarly produce QM's structure from information-theoretic and probabilistic constraints. The convergence of multiple independent derivations strengthens the case that QM has an information-theoretic character.

### 6.3 The Gap: From QM to GR

The Chiribella and Hardy derivations reconstruct QUANTUM MECHANICS from information principles. They do NOT reconstruct general relativity, quantum field theory, or the standard model. The leap from "QM follows from information constraints" to "all of physics follows from information constraints" is enormous and unjustified by current results.

**The informational-universe framework acknowledges this gap explicitly.** The Chiribella/Hardy work establishes that the quantum part of physics has an information-theoretic foundation. Whether gravity and particle physics admit similar reconstructions remains an open question — this is the research program, not an accomplished fact.

### 6.4 Toward an Informational Derivation of Gravity

If the Jacobson-thermodynamic program (§3) is correct, gravity is constrained by thermodynamics and entropy bounds. If the Chiribella program is correct, quantum mechanics is constrained by information-theoretic axioms. The logical next step is to ask whether a unified set of information-theoretic principles can constrain BOTH quantum dynamics and gravitational dynamics simultaneously.

**Candidate principles for a unified framework:**
1. The Hilbert space dimension of any region is $\exp(A/4\ell_{P}^2)$ (holographic bound)
2. Quantum evolution is unitary (probability conservation)
3. Local observers experience approximately Minkowski spacetime (equivalence principle)
4. Entropy satisfies the second law (thermodynamic consistency)

Whether these principles suffice to derive the form of physical law — or whether new principles are needed — is the central open question of the informational-universe research program.

---

## 7. Ontological Implications [PHILOSOPHY]

[PHILOSOPHY] This section departs from physics and enters philosophical territory. The claims below are not empirically testable with current methods. The reader may skip this section without loss of physical content.

### 7.1 The Map/Territory Distinction

A persistent ambiguity in the holographic/informational literature is whether the holographic description is a *representation* of reality or reality itself. The map/territory distinction [@korzybski1933science] is essential:

- **Map (description):** The holographic encoding provides an efficient, possibly complete, description of physical states
- **Territory (reality):** The holographic degrees of freedom ARE what exists — there is no deeper substrate

Most holographic results are about the map: AdS/CFT provides a *dictionary*, Jacobsonian gravity provides a *derivation* of field equations, and Ryu-Takayanagi provides a *formula* for entanglement entropy. None of these results assert that the boundary description IS reality rather than DESCRIBES it.

The ontological informational-universe claim crosses from map to territory. We find this crossing unjustified by current evidence but logically coherent — it is a philosophical position, not a scientific finding. Flagging it as [PHILOSOPHY] rather than physics is essential to prevent the conflation that has plagued the "it from bit" literature.

### 7.2 Ontic Structural Realism

Esfeld [@esfeld2014how] and others have proposed ontic structural realism (OSR) as the appropriate ontology for quantum physics: what exists is not objects with intrinsic properties, but structures and relations. Entanglement, in this view, is not a relation between pre-existing objects — entanglement IS the structure, and the "objects" are derivative.

The informational-universe hypothesis is compatible with OSR but goes further: it identifies the relevant structure as *information-theoretic* specifically. The universe is not merely structural — it is a structure of constraints on what information can be encoded where, with physical law emerging from those constraints.

**We do not defend this position.** We merely note that it is (a) logically coherent, (b) philosophically defensible via OSR, and (c) not empirically distinguishable from instrumentalism at currently accessible scales.

### 7.3 Why Philosophy Matters (and Why It Must Be Flagged)

Philosophical clarity is not an academic luxury — the "it from bit" literature is rife with conflation of map and territory, speculation presented as fact, and promissory claims without operational definitions. By explicitly separating the physics (§2–§6) from the philosophy (§7), we aim to model the standard that the field should adopt: physical claims with [certainty] labels and falsification conditions; philosophical claims flagged [PHILOSOPHY] with no empirical warrant claimed.

---

## 8. Calibration Register, Limitations, and Falsifiability

### 8.1 Calibration Register (MANDATORY)

The following predictions are dated and logged. Each has a target check date and a falsification condition. The purpose is to prevent post-hoc rationalization: if, by the check date, the prediction has not been confirmed, the relevant claim is weakened.

| ID | Prediction | Registered | Check Date | Falsification Criterion | Status |
|:---|:----------|:-----------|:-----------|:------------------------|:-------|
| CR-1 | At least one independent derivation of Einstein equations from entanglement first law will be published for non-AdS (including de Sitter or asymptotically flat) spacetimes | 2026-07-21 | 2030-07-21 | Zero such derivations → PS-F generalization claim weakened | PENDING |
| CR-2 | The Bao-Carroll-Singh conjecture on locally finite-dimensional Hilbert space will have ≥5 independent citations in quantum gravity literature (excluding self-citations and QNFO-affiliated papers) | 2026-07-21 | 2032-07-21 | <5 citations → finite-dim Hilbert space program not gaining traction | PENDING |
| CR-3 | No experiment will demonstrate a violation of the Bekenstein bound by a factor ≥2 in any system | 2026-07-21 | 2028-07-21 | Violation found → core anchor of framework destroyed | PENDING |
| CR-4 | The Jacobson thermodynamic gravity program will have published a derivation of cosmological perturbation spectra (analogous to inflationary predictions) from entropy constraints alone | 2026-07-21 | 2028-07-21 | No such derivation → PS-F explanatory power limited to GR, not cosmology | PENDING |
| CR-5 | The term "informational universe" or closely related concepts ("information-first physics," "holographic ontology") will appear in ≥3 independent review papers on quantum gravity foundations NOT authored by QNFO-affiliated researchers | 2026-07-21 | 2035-07-21 | <3 mentions → framework not achieving community recognition | PENDING |

### 8.2 Limitations

This paper has significant limitations that we document explicitly:

1. **No empirical test at currently accessible scales.** All five calibration register predictions require theoretical advances (CR-1, CR-2, CR-4), community adoption (CR-5), or experiments at energy scales far beyond current capability (CR-3). The framework is [not yet falsifiable] by any experiment that could be conducted in the next 5 years.

2. **AdS/CFT dependence.** Much of the rigorous evidence for holography (§2.3, §4) comes from AdS/CFT, which describes a universe with negative cosmological constant. Extrapolation to our de Sitter universe is conjectural.

3. **No unification of forces.** The framework provides no mechanism for deriving the specific gauge groups, coupling constants, or particle spectrum of the Standard Model. It constrains the *form* of physical law but does not supply the *content*.

4. **Descriptive vs. explanatory ambiguity.** Jacobson's derivation shows that Einstein's equations *can be derived* from thermodynamic constraints — not that they *must be*. The framework is consistent with both emergent gravity and fundamental gravity + thermodynamic description.

5. **Finite-dim constraint is operationally vacuous.** The Hilbert space dimension $\sim\exp(10^{122})$ for the observable universe is finite but so large that no computation can distinguish it from infinite. The constraint matters structurally but not computationally.

6. **Self-citation risk.** Much of the QNFO literature on which this paper builds remains internal (Vectorize-confined corpus). This is a [CONFIRMATION-BIAS-RISK] — the framework's logical coherence has been demonstrated only within its own ecosystem, not validated by the broader physics community (see CR-5).

### 8.3 Falsifiability Hierarchy

| Tier | Claim | Falsification Method | Currently Testable? |
|:-----|:------|:---------------------|:-------------------|
| 1 | Bekenstein bound holds universally (§2) | Measure S > A/4 in any system | Yes (but at inaccessible scales) |
| 2 | Einstein equations derivable from thermodynamics (§3) | Already done by Jacobson — not a prediction | Confirmed (interpretation-dependent) |
| 3 | Entanglement builds spacetime beyond AdS/CFT (§4) | Derive Ryu-Takayanagi analog for de Sitter | No — requires dS/CFT solution |
| 4 | Hilbert space is locally finite-dimensional (§5) | Detect QFT violation at low cutoff | No — requires TeV-scale gravity |
| 5 | All physical law from information constraints (§6) | Derive Standard Model from information axioms | No — extremely distant |

This hierarchy makes clear which claims are science and which are research program: tiers 1-2 are scientific claims; tiers 3-4 are research program; tier 5 is aspiration. The informational-universe framework is valuable precisely because it makes these distinctions explicit.

---

## 9. Conclusion

The informational-universe hypothesis, properly constrained, asserts that physical law is bounded and shaped by information-theoretic constraints — the Bekenstein bound, the holographic principle, and thermodynamic entropy relations. This is a defensible [mainstream interpretation] in its weaker forms and a promising [speculative] research program in its stronger forms.

The framework's primary contributions are:

1. **A dependency chain** that maps which premises imply which conclusions, enabling targeted falsification (Figure 1, §2.3 of parent project [PHASE-4])
2. **A calibration register** of five testable predictions with 2028–2035 check dates (§8.1)
3. **Explicit separation** of physics from philosophy, with [PHILOSOPHY] tags on all ontological claims (§7)
4. **A bibliography** of 47 key papers spanning holography, thermodynamic gravity, entanglement geometry, finite-dimensional QG, and information-theoretic foundations (refs.bib)

The most important open question is: can the Jacobson thermodynamic derivation be extended to yield predictions that differ from general relativity in observable regimes? If the answer is yes, the informational-universe framework becomes empirically testable. If no, it remains a logically coherent interpretive framework — valuable for clarity, but not a new physical theory.

---

## Acknowledgments

This synthesis builds on work by J. D. Bekenstein, S. W. Hawking, T. Jacobson, J. Maldacena, L. Susskind, S. Ryu, T. Takayanagi, M. Van Raamsdonk, B. Swingle, R. Bousso, D. N. Page, N. Bao, S. M. Carroll, A. Singh, T. Padmanabhan, G. Chiribella, G. M. D'Ariano, P. Perinotti, L. Hardy, C. Rovelli, M. Esfeld, and many others. All errors of synthesis, overextension, and philosophical overreach are ours alone.

---

**Bibliography:** See `artifacts/refs.bib` (47 entries: 21 foundational + 26 Core arXiv papers from the INFO-UNIVERSE Phase 2 literature search).
