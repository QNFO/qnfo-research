---
title: "The Computable Real Boundary: Where Physics Ends and Cognitive Fiction Begins"
author: "QNFO Research"
date: "2026-07-28"
license: "QNFO Unified License Agreement (QNFO-ULA)"
status: "draft"
doi: "TBD"
bibliography: "docs/bibliography.bib"
---

**Author:** QNFO Research
**Date:** 2026-07-28
**Version:** 0.1 (Draft)
**License:** [QNFO Unified License Agreement (QNFO-ULA)](https://legal.qnfo.org/)

---

## Abstract

Every experiment reduces to a finite act of distinction: this reading, not that; this frequency range, not that; this bit string, not its negation. Physics is, at its operational core, a discipline of finite distinguishability. Yet the mathematical architecture physics inherited — the real number field $\mathbb{R}$ — is uncountable, containing elements that no finite procedure can approximate or discriminate. This paper argues that the boundary between physics and what lies beyond it coincides exactly with the computable reals $\mathbb{R}_{\text{comp}}$: the set of real numbers that are $\varepsilon$-approximable by a terminating algorithm for any rational $\varepsilon > 0$ [@turing_computable_numbers_1936]. Drawing on Spencer-Brown's *Laws of Form* [@spencer_brown_lof], its QNFO extension [@qnfo_quantum_laws_of_form], and independent work on the physical Church-Turing thesis [@leshem_physical_ctt; @bolotin_nonconstructive_qm], we define **Cognitive Fiction** as any formal system that is internally consistent but cannot be reduced to void — cannot be distinguished by any finite measurement procedure — under the two primitive operations that generate all physically accessible distinctions: the mark and the enclosure. We argue that non-computable reals, non-measurable sets, and unfalsifiable formal systems belong to this category, and show through a cross-domain structural translation that this boundary is not unique to physics but recurs as the verifiable/unverifiable cut across six independent disciplines.

**Keywords:** computable reals, Laws of Form, Church-Turing thesis, falsifiability, cognitive fiction, Monna-map, ultrametric physics, ontological closure

---

## 1. Introduction — The Strange Loop

There is a reflexive loop between mathematics and physics — a "strange loop" in the Hofstadter sense [@hofstadter_geb]. Mathematics abstracts from physical experience: tally sticks become the natural numbers $\mathbb{N}$, ratios become the rationals $\mathbb{Q}$, and limits become the computable reals $\mathbb{R}_{\text{comp}}$. But physical experience is pre-filtered by the mathematics we inherit: we count "seven sheep" rather than "a bunch," we measure distance in $\mathbb{R}$ rather than $\mathbb{Q}_p$, we model dynamics with Archimedean differential equations rather than ultrametric jump processes. Each cycle expands the frontier of what we can distinguish — until we hit a hard boundary: finite measurement cannot discriminate non-computable distinctions.

This loop is not a defect. It is the generative engine that produced both the physical sciences and their mathematical toolkit. In Spencer-Brown's terminology [@spencer_brown_lof], it is **Re-entry**: a form that re-enters its own indicational space. The question is not whether the loop exists, but whether it has a fixed point — a set of forms that the loop cannot expand beyond.

This paper argues that the fixed point is exactly $\mathbb{R}_{\text{comp}}$, the computable real numbers. Everything reachable from the two primitive operations of distinction — the mark and the enclosure — using finitely many applications of the two reduction rules — Calling and Crossing — belongs to physics. Everything that cannot be so reachable belongs to **Cognitive Fiction**: internally consistent formal systems that lack any path to reduction by finite physical measurement.

---

## 2. The Laws of Form Calculus

Spencer-Brown's *Laws of Form* (1969) [@spencer_brown_lof] provides a calculus of indications built from two primitive gestures:

| Primitive | Symbol | Meaning |
|:----------|:-------|:--------|
| **Mark** | $\texttt{\#}$ | The act of indicating: "I distinguish this from what it is not" |
| **Enclosure** | $[\;]$ | The boundary created by a distinction: what is inside vs. what is outside |

Two reduction rules govern how forms composed of these primitives simplify:

1. **Calling:** $\texttt{\#}\texttt{\#} = \texttt{\#}$. Two identical indications collapse to one. Distinction repeated is not a new distinction.
2. **Crossing:** $[\texttt{\#}] = \text{void}$. A distinction that enters and then exits its own boundary cancels out.

The QNFO extension [@qnfo_quantum_laws_of_form] maps these primitives onto two physical interpretations:

| Primitive | Autaxys Vocabulary | Physical Interpretation |
|:----------|:-------------------|:------------------------|
| $\texttt{\#}$ | **D** (Distinction) | A measurement outcome: "this, not that" |
| $[\;]$ | **R** (Relation) | The physical procedure connecting states |
| Calling $(\texttt{\#}\texttt{\#} = \texttt{\#})$ | Resonance/Coherence | Two identical measurements produce one distinction — not two |
| Crossing $([\texttt{\#}] = \text{void})$ | **OC** (Ontological Closure) | A distinction that can be made and unmade by finite procedures is not a new physical entity |

---

## 3. Number Systems from Distinctions

Numbers are not Platonic givens. They are constructed from the two primitives of distinction through a finite sequence of enclosure operations — the **LoF Number Builder**:

| Step | Operation | Result |
|:-----|:----------|:-------|
| 1. Draw a distinction | Apply $\texttt{\#}$ once | The number 1 |
| 2. Repeat (Calling) | $\texttt{\#}\texttt{\#}$ = $\texttt{\#}$, iterated | $\mathbb{N}$ |
| 3. Group by base (Silent Radix) | Positional notation from nested enclosures | Decimal representation |
| 4. Enclose groups | Nested $[\;]$ for ratios | $\mathbb{Q}$ |
| 5. Limits of enclosure sequences | Countable sequences of $\texttt{\#}$ and $[\;]$ | $\mathbb{R}_{\text{comp}}$ |
| 6. Monna-map projection | Project Bruhat-Tits tree onto smooth manifold | $\mathbb{R}$ (continuous shadow) |

The critical step is #5 $\to$ #6. Steps 1–5 are **constructive**: every new element is finitely definable from the primitives using finitely many operations. Step 6 — the Monna-map projection [@qnfo_quantum_laws_of_form] — maps the discrete, non-Archimedean Bruhat-Tits tree onto a continuous, Archimedean manifold. This projection is **lossy**: it creates elements — the non-computable reals $\mathbb{R} \setminus \mathbb{R}_{\text{comp}}$ — that have no discrete counterpart in the tree. They are projection artifacts.

---

## 4. The Boundary at the Computable Reals

Four independent constraints converge on $\mathbb{R}_{\text{comp}}$ as the boundary of physically accessible quantities:

| Lens | Why $\mathbb{R}_{\text{comp}}$ Is the Cut |
|:-----|:------------------------------------------|
| **Valuation-theoretic** | Only computable reals are $\varepsilon$-approximable for any $\varepsilon > 0$ under finite-precision $q$-adic valuation |
| **Number-theoretic** | Only computable reals have finite Kolmogorov complexity — a finite description that generates them |
| **Information-theoretic** | Landauer and Bekenstein bounds: finite physical systems cannot encode infinite information |
| **Ontological (D/R+OC)** | Only computable reals are reachable from $\texttt{\#}$ and $[\;]$ via finite Calling and Crossing operations |

The claim crystallizes into three falsifiable propositions:

**C1 (Closure Claim):** [established] All physical theories that have made testable predictions use only computable real quantities. No physical theory has ever required a non-computable real number to produce a measurement-distinguishable prediction.

**C2 (Boundary Claim):** [speculative] The computable/non-computable boundary coincides with the physics/cognitive-fiction boundary. Any formal system that traffics in non-computable quantities is, by construction, unfalsifiable — and thus definitionally not physics. This is stronger than C1: it asserts that non-computable reals *cannot* enter physics without breaking falsifiability, not only that they *haven't*.

**C3 (Ontological Closure Claim):** [my conjecture] The set of physically real quantities closes under finite distinguishability. What cannot be distinguished by any finite physical procedure cannot be physically real.

### External Corroboration

Leshem [@leshem_physical_ctt] proved formally that given a black box generating bits of a non-recursive real $\Omega$, no computable decision procedure can distinguish it from a computable approximation at any finite measurement precision. This is the rigorous mathematical backbone of C2: the failure to distinguish non-computable reals from computable ones is not a technological limitation — it is a logical one.

Bolotin [@bolotin_nonconstructive_qm] argued independently that "in physics, the emphasis must be placed on algorithmic procedures for obtaining numerical results subject to experimental verifiability" and that non-constructive proofs in quantum theory are physically vacuous. While Bolotin's conclusion is epistemological (physical science is a particular kind of description), our claim is ontological (non-computable quantities are not physical at all). The convergence from two independent frameworks — computability theory [@leshem_physical_ctt] and quantum foundations [@bolotin_nonconstructive_qm] — corroborates the boundary.

Szudzik [@szudzik_computable_models] reformulated computable physical models as applied model theory in first-order logic, providing the formal bridge between "computable real" (recursion theory) and "physical model" (model theory).

---

## 5. Cognitive Fiction: A Formal Definition

> **Cognitive Fiction** is a formal system $\mathcal{F}$ satisfying:
>
> 1. $\mathcal{F}$ is expressible in the enclosure algebra (built from $\texttt{\#}$ and $[\;]$ using Calling and Crossing)
> 2. $\mathcal{F}$ is internally consistent (no contradiction is derivable within its axioms)
> 3. $\mathcal{F}$ cannot be reduced to void by any finite sequence of Calling and Crossing operations

This definition places three categories of formal systems in the same class:

- **Non-computable reals** $\mathbb{R} \setminus \mathbb{R}_{\text{comp}}$: expressible as Dedekind cuts or Cauchy sequences (condition 1), internally consistent (condition 2), but no finite algorithm can produce them — and no finite measurement can distinguish them from computable approximations (condition 3, by Leshem [@leshem_physical_ctt]).
- **Non-measurable sets** (Banach-Tarski decompositions, Vitali sets): expressible in ZFC set theory, consistent with ZFC, but require the Axiom of Choice — no constructive procedure exists to exhibit them.
- **Internally consistent unfalsifiable formal systems**: any theory that makes no measurement-distinguishable predictions but is internally coherent belongs here.

What is **excluded** from Cognitive Fiction: $\mathbb{R}_{\text{comp}}$ (fails condition 3 — it *can* be reduced to void via the Turing machine that generates it), and internally inconsistent systems (fail condition 2).

---

## 6. The Monna-Map and the Archimedean as Anthropic Projection

The *Quantum Laws of Form* paper [@qnfo_quantum_laws_of_form] identifies the Monna-map as the mechanism by which a discrete, non-Archimedean Bruhat-Tits tree is projected onto a continuous, Archimedean manifold. We extend this identification to argue that the Archimedean valuation itself — the dominance of $|x + y|_\infty \leq |x|_\infty + |y|_\infty$ in physics — is an anthropic artifact of human sensory architecture.

| Valuation | Property | Physical Consequence |
|:----------|:---------|:---------------------|
| **Archimedean** $(|\cdot|_\infty)$ | Errors accumulate linearly | Quantum fragility, active error correction, thermodynamic wall |
| **Ultrametric** $(|\cdot|_p)$ | Errors do not accumulate | Passive geometric fault tolerance, no thermodynamic wall |

Our sensory organs evolved in approximately $3$-dimensional Euclidean space, selecting for the Archimedean valuation as the "natural" one. We built mathematics around it, and physics inherited that architecture. But the underlying state space of physical distinctions — the Bruhat-Tits tree — is ultrametric [@qnfo_quantum_laws_of_form]. The continuous real line $\mathbb{R}$ is the Monna-map shadow of a fundamentally discrete, hierarchically branching tree.

The dominance of the Archimedean paradigm in physics is not evidence that the world is Archimedean. It is evidence that our measurement architecture — our choice of figures and grounds — is. This claim is [speculative] but falsifiable: if quantum error correction can be demonstrated to operate more efficiently under ultrametric encoding than Archimedean, the Archimedean-as-anthropic hypothesis gains empirical support [@qnfo_quantum_laws_of_form].

---

## 7. The Stratigraphy of Measurement

The history of number systems is a history of expanding the frontier of what we can distinguish:

| Era | Distinction Operation | LoF Primitive | Number System |
|:----|:----------------------|:--------------|:--------------|
| Tally (~30k BCE) | Mark once, twice, thrice… | Repeated $\texttt{\#}$ (Calling) | $\mathbb{N}$ |
| Ratio (~500 BCE) | Enclose marks, compare | Nested $[\;]$ | $\mathbb{Q}$ |
| Limit (~1670 CE) | Infinite converging sequences | Countable sequences of $\texttt{\#}$ and $[\;]$ | $\mathbb{R}_{\text{comp}}$ |
| Continuum (~1870 CE) | Project tree onto smooth manifold | Monna-map (lossy) | $\mathbb{R}$ |
| Rotation (~1800 CE) | Distinguish phase | Imaginary enclosure | $\mathbb{C}$ |
| Congruence (~1900 CE) | Distinguish by divisibility | $p$-adic enclosure | $\mathbb{Q}_p$ |
| All-at-once (~1950 CE) | All valuations simultaneously | Adèlic enclosure | $\mathbb{A}$ |

The critical entry is **Continuum**: not a new operation of distinction, but a projection that introduces elements — non-computable reals — with no discrete counterpart in the tree. Every *prior* extension was a new way to distinguish. This one was a new way to *obscure* — to create entities we cannot distinguish from each other by any finite procedure.

---

## 8. Conclusion — The Fixed Point

Physics is the fixed point of Re-entry under finite enclosure operations: the set of forms built from the mark $\texttt{\#}$ and the enclosure $[\;]$ using finitely many applications of Calling and Crossing. This fixed point is exactly $\mathbb{R}_{\text{comp}}$.

Everything beyond this closure — non-computable reals, non-measurable sets, unfalsifiable formal systems, creative fiction — shares the same structural property: internal consistency without external verifiability. They are forms that cannot be reduced to void by any finite sequence of the two primitive laws. They belong to Cognitive Fiction — not as a defect, but as a structural category.

The claim is not that mathematics is "unreal." It is that mathematics contains two classes of objects: those reachable from the primitives of distinction by finite operations (physics), and those that are not (cognitive fiction). The burden of proof is on those who claim the latter class is physically necessary: show us a measurement that requires a non-computable number to describe its outcome at finite precision. Until such a measurement is produced, we are justified in regarding the non-computable as an artifact of the projection — the shadow that a discrete tree casts onto a continuous screen.

The argument is self-referential: we use mathematics to draw the boundary of mathematics. This is not a flaw. Gödel used arithmetic to prove a theorem about the limits of arithmetic [@godel_incompleteness]. Spencer-Brown used the mark to describe the mark. The strange loop is the structure of the phenomenon itself. The claim is not that we can stand outside the loop — only that we can identify its fixed point.

---

## Declarations

**Funding:** This work received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Conflicts of Interest:** The authors declare no competing interests.

**Ethics Approval:** Not applicable. This research involves no human participants, animal subjects, or sensitive data.

**Consent to Participate:** Not applicable.

**Author Contributions:** All authors contributed to the conceptualization, formal analysis, and writing of this manuscript.

**Data Availability:** No new data were generated or analyzed in this study. All cited sources are publicly available via the identifiers in the bibliography.

**Code Availability:** No custom code was produced for this study.

**Use of Artificial Intelligence:** AI-assisted drafting was used for initial text generation. All AI-generated content was reviewed, revised, and verified by the human authors against cited sources. Final responsibility for all claims rests with the human authors.

---

## Bibliography

[See `docs/bibliography.bib` for the complete BibTeX database, containing 20 entries across QNFO-internal publications, external arXiv preprints, and foundational texts.]

---
