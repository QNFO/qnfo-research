---
title: "Conditional Truths and the Locale Framework: Map, Territory, and the Rendering Interface"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-17"
license: "CC BY-NC-SA 4.0"
doi: ""
status: "published"
abstract: "Every physical statement is a conditional truth: it holds only within a locale --- a specified vacuum or symmetry sector, background geometry, medium, energy scale, or observer frame. This paper formalizes the resulting locale framework in four moves. First, a catalog of conditional truths (photon mass, spin, energy conservation, the second law, the electron's charge and mass, the vacuum) shows that the interesting physics lives at the seams where a rule fails to transfer. Second, the map-territory distinction: pedagogical maps fail at seams, and the ontological territory is the invariant relational structure --- the transformation law, the commutation algebra, the gauge-invariant observable --- that transfers across locales; ontic structural realism is engaged as a named imported premise, with its critics. Third, the rendering interface: an observer constrained to first-person observations inside a rendering experiences the metric of the image space, not the substrate; no finite set of such observations decides whether the substrate metric is Archimedean or ultrametric (the Monna-map underdetermination, generalized beyond the visual case); what cannot be decided can still be probed --- a rendering with structure leaks structure. Fourth, scale primitives: stripped of anthropocentric units, frequency is a recurrence count, the fine-structure constant is a ratio, and temperature is a derivative; by Ostrowski's theorem the Archimedean real line is one completion of the rationals among many. Why a reader should care: the framework turns 'conditional truth' from a footnote into a first-class epistemic category with a falsifiable core (the metric of the substrate is not decidable from inside the interface) and identifies what survives --- counts, ratios, and structure leaks. Premise-depth disclosure: 'locale' and 'interface' are unanalyzable primitives; the structural-realist ontology is imported (Ladyman-Ross), not derived; the completion-to-background isomorphism is a pedagogical unification, not a discovery; the paper proposes no dynamical theory of seams."
---

# Conditional Truths and the Locale Framework: Map, Territory, and the Rendering Interface

## Abstract

Every physical statement is a conditional truth: it holds only within a locale --- a specified vacuum or symmetry sector, background geometry, medium, energy scale, or observer frame. This paper formalizes the resulting locale framework in four moves. First, a catalog of conditional truths (photon mass, spin, energy conservation, the second law, the electron's charge and mass, the vacuum) shows that the interesting physics lives at the seams where a rule fails to transfer. Second, the map-territory distinction: pedagogical maps fail at seams, and the ontological territory is the invariant relational structure --- the transformation law, the commutation algebra, the gauge-invariant observable --- that transfers across locales; ontic structural realism is engaged as a named imported premise, with its critics. Third, the rendering interface: an observer constrained to first-person observations inside a rendering experiences the metric of the image space, not the substrate; no finite set of such observations decides whether the substrate metric is Archimedean or ultrametric (the Monna-map underdetermination, generalized beyond the visual case); what cannot be decided can still be probed --- a rendering with structure leaks structure. Fourth, scale primitives: stripped of anthropocentric units, frequency is a recurrence count, the fine-structure constant is a ratio, and temperature is a derivative; by Ostrowski's theorem the Archimedean real line is one completion of the rationals among many. Why a reader should care: the framework turns 'conditional truth' from a footnote into a first-class epistemic category with a falsifiable core (the metric of the substrate is not decidable from inside the interface) and identifies what survives --- counts, ratios, and structure leaks. Premise-depth disclosure: 'locale' and 'interface' are unanalyzable primitives; the structural-realist ontology is imported (Ladyman-Ross), not derived; the completion-to-background isomorphism is a pedagogical unification, not a discovery; the paper proposes no dynamical theory of seams.

## 1. Introduction: conditional truths and the locale

Physics pedagogy teaches statements as if they were unconditional: "the photon is massless," "energy is conserved," "spin is angular momentum," "the speed of light is constant," "entropy never decreases." Each of these statements is true, and each is true only inside a locale --- a domain of applicability specified by a vacuum or symmetry sector, a background geometry, a medium, an energy scale, or an observer frame. The vacuum photon is massless because gauge invariance requires it; inside a superconductor the Anderson--Higgs mechanism makes a massive vector excitation; in a plasma the longitudinal mode acquires a gap that functions as an effective mass; in a waveguide the cutoff does the same. The statement "the photon is massless" is a conditional truth: $\mathcal{L}_{\text{vac}} \vdash m_\gamma = 0$, with the locale made explicit.

This observation is not new; it is the working doctrine of effective field theory [4,5,28]. What this paper adds is the claim that the conditional structure is not a defect or a footnote but the shape of physics itself, and that three familiar distinctions --- conditional truth, the pedagogical map versus the ontological territory, and the interface between a substrate and an observer --- are the same distinction seen from three sides. The paper's core claim is deliberately bounded. Its sharpest, most falsifiable assertion is:

> **C3 (interface underdetermination).** An observer constrained to first-person observations inside a rendering interface experiences the metric of the image space, not the metric of the substrate. No finite set of such observations decides whether the substrate metric is Archimedean or ultrametric. The substrate metric is not decidable from inside the interface; yet what cannot be decided can still be probed, because a rendering with structure leaks structure.

The visual case of C3 was established in a companion record [6]; this paper generalizes it to arbitrary first-person observation channels and embeds it in a framework with three sibling claims (C1 locale-conditionality, C2 map-territory, C4 scale primitives) stated fully in Section 7. The framework's premises end at the primitives "locale" and "interface"; the ontology it favors is imported, not derived; and its evidential weight is concentrated in C3, with the honest accounting of the other claims given in Section 8.

## 2. The catalog of conditional truths

A locale is a specified domain of applicability: a choice of background, sector, scale window, medium, or frame such that within it a given physical statement holds. Write $\mathcal{L} \vdash \phi$ for "locale $\mathcal{L}$ supports statement $\phi$." The catalog below is representative, not exhaustive; each entry is a documented case where the statement is true in its home locale and fails or transforms across a seam.

**The photon mass.** In the vacuum locale, gauge invariance forces the massless photon: any explicit mass term breaks the unbroken U(1) symmetry and spoils renormalizability, and experiment bounds any residual mass by $m_\gamma < 10^{-18}$ eV. In the superconductor locale, the Anderson--Higgs mechanism produces a massive vector excitation; in the plasma locale the plasmon dispersion $\omega^2 = \omega_p^2 + c^2 k^2$ carries a gap interpretable as an effective mass, not Lorentz invariant and frame-dependent; in the waveguide locale the cutoff frequency plays the same role; in 2+1 spacetime a Chern--Simons term yields a topological mass without a Higgs field, though in 3+1 dimensions such a term is not gauge invariant. The word "photon" itself is locale-indexed: the vacuum quantum is one thing, the dressed collective excitation another. "The photon is massless" is the conditional truth $\mathcal{L}_{\text{vac}} \vdash m_\gamma = 0$; the interesting physics is at the seam where the mass label changes.

**Spin.** "Spin is angular momentum" is true only in the locale of Noether's theorem, where it is the conserved charge of rotational invariance. The pedagogical map --- a spinning charged sphere --- fails quantitatively (the surface velocity required for the observed magnetic moment exceeds $c$ for any radius below the classical electron radius; the gyromagnetic ratio $g = 2 + \alpha/\pi + \cdots$ disagrees with the classical prediction $g=1$) and structurally (the electron is pointlike to $10^{-19}$ m yet carries a fixed magnetic moment). The territory that transfers across locales is the commutation algebra $[S_i, S_j] = i\hbar\,\varepsilon_{ijk} S_k$ and its representation theory: the little-group classification of the Poincar\'e group, SU(2) for massive particles, E(2) helicity for massless ones. In the condensed-matter locale spin is not even conserved; it hybridizes with momentum in Rashba and Dresselhaus couplings and dissolves into spinons in spin liquids.

**Energy conservation.** Energy is conserved in time-translation-invariant backgrounds (Noether); in the cosmological locale the FLRW metric has no timelike Killing vector, and photon energy is drained by redshift without work. "Energy is conserved" is $\mathcal{L}_{\text{static}} \vdash \dot{E} = 0$.

**The second law.** Entropy never decreases for an isolated system; in open locales driven by external energy flow, subsystem entropy can decrease locally, and fluctuation theorems permit transient violations in small systems. The law is a statement about the total of a closed universe, not about every locale.

**Charge and mass.** The electron charge is constant only at fixed momentum transfer; the renormalized coupling runs with the energy scale of the probe, $\alpha \approx 1/137$ in the infrared Thomson locale and $\alpha \approx 1/128$ at the $Z$ scale; in the quantum Hall locale quasiparticles carry fractional charge. The electron rest mass is fixed in vacuum; the effective mass in a crystal locale can be $0.07 m_e$ or negative (holes); heavy-fermion locales renormalize it by orders of magnitude.

**The vacuum.** The classical "empty vacuum" is a fiction: the QED vacuum is a medium of virtual fluctuations (Lamb shift, Casimir effect), and the QCD vacuum is a condensate with nonzero expectation values. Even "empty" is locale-relative.

The lesson of the catalog is not skepticism but structure: every law carries an implicit locale, and the seams --- symmetry breakings, phase transitions, scale crossings, coarse-graining thresholds --- are where new physics lives [16]. The conditional-truth reading of laws has philosophical precursors [24,25]; effective field theory has made it operational [4,5,28]. What the catalog adds is the systematic form: a physics statement is a pair (locale, content), and physics is the study of how content transfers across seams.

## 3. Map and territory

The second move turns the catalog into an ontology. A pedagogical map is any image used to carry a law across a seam: the spinning sphere for spin, the little billiard balls for thermodynamics, the rubber sheet for gravity. Maps are not wrong; they are locale-bound. The territory is what actually transfers: the transformation law, the commutation algebra, the gauge-invariant observable, the equivalence class of configurations under the symmetries of the locale.

The spin case is the cleanest worked example. The map (spinning sphere) fails quantitatively and structurally; the territory is the projective representation of the rotation group --- the statement "under a 360-degree rotation the fermion wavefunction acquires a minus sign" --- together with the algebra that makes it testable. Every classical intuition about spin is a map; the transformation law is the territory. This is the map-territory discipline of the author's earlier methodology record [7], applied to the metric question in Section 4.

What is the territory, ontologically? Three answers are available. Platonism says the territory is pure mathematical structure existing independently; physicalism says it is substance beneath the relations; structural realism says it is the relations themselves. This paper takes the structural-realist answer as a **named imported premise**, not a derived conclusion [2], and engages its critics explicitly: the question whether there is a compelling argument for ontic structural realism [21], the defense of epistemic structural realism against it [22], and the assessment of OSR within quantum mechanics [20]. The framework's own contribution to this debate is the instantiation problem: if the territory were pure mathematical structure, all consistent structures would be equally real, yet the actualized locale selects one gauge group, one spacetime dimension, one set of couplings. The selection --- the "is instantiated" step --- is not captured by the mathematics alone. The territory is therefore best described as *invariant relational constraint*, actualized as process: the rulebook of how a system must transform when its locale shifts, enforced in measurement outcomes. Mathematics is the language of that rulebook, not the rulebook's existence.

Two qualifications keep this honest. First, the structural-realist reading is doing no evidential work in this paper; it is the interpretive gloss on C2, and the falsifiability of the framework does not depend on it (Section 8). Second, "invariant relational constraint" is itself a map: a philosopher of a different school can accept C1, C3, and C4 while rejecting C2's ontology. The framework is built so that its ontology is the most replaceable part.

## 4. The rendering interface

The third move is the paper's core. Consider a substrate space $X$ with a metric of unknown type, and a rendering map $R: X \to V$ into an image space $V$ whose metric the observer experiences. The observer's evidence is generated entirely inside $V$: apparent sizes, parallax, convergence, color, count --- whatever the rendering produces. The experienced metric is the metric of $V$, not the metric of $X$.

The canonical example of a discontinuous, structure-preserving-in-spite-of-discontinuity rendering is the Monna map [1]: the surjection from the $p$-adic numbers onto the reals obtained by reading the base-$p$ digits of a $p$-adic number as a real number in base $p$. The Monna map is discontinuous at every point; the discontinuity follows from the digit definition (a $p$-adically convergent sequence $-p^m \to 0$ maps to $M(-p^m) = p^{-m+1} \to \infty$), not from any general principle connecting disconnectedness to discontinuity --- the Cantor function is a continuous surjection from a totally disconnected space [18]. Pitk\"anen's canonical identification is the same construction [27]; the mathematics of Monna-type maps is an active external field [19].

The companion record [6] proved the visual case: an Archimedean substrate and an ultrametric substrate rendered through a Monna-map-like interface produce identical first-person appearances --- apparent size, vanishing-point convergence, and parallax are image-space quantities, and both substrates render into the same image space. The underdetermination is exact: **the metric of the substrate is not decidable from inside the interface.** This paper generalizes the claim from visual perspective to arbitrary first-person observation channels: any rendering that fixes the image-space metric and hides the substrate metric behind it leaves the substrate metric undecidable by any finite set of first-person observations, because all such observations are statements about $V$, and the fiber of $R$ over each observed point is nonempty in both metric classes.

Three consequences follow.

**Objects are clusters, not points.** If individuation is partition-theoretic --- an object is a cluster in nested neighborhoods --- then the objects of experience are image-space clusters, and their substrate identities are underdetermined by construction. The experienced world is a rendering of an inaccessible substrate, and "object" is a coarse-graining of the image space. This reframes the observer-self-location problem studied in a companion record [13]: the observer inside the tree cannot locate herself in the substrate, only in the image.

**The substrate question is not empty.** Underdetermination does not license indifference. The constructive lineage is explicit: a derivation of the continuum from distinction primitives produces the real line through a Monna-map-like projection as its final step, and that step is lossy --- it creates non-computable reals that are projection artifacts [9,14]. The continuum we experience may be exactly such an artifact: the image-space metric of an ultrametric substrate. The author's prior records on natural units [9], the Ostrowski reformulation [10], the physics-number-theory consilience [11], and the measure-theoretic artifacts of the Archimedean place [12] develop this lineage in detail.

**Structure leaks.** The interface cannot be decided, but it can be studied from inside. A rendering with structure leaks structure: discontinuities of the rendering map appear as seams in the image (the staircase in the visual case [6]); artifacts of the projection are detectable as non-computable residue [14]; the failure modes of a rendering are fingerprints of its construction. The probe principle is therefore: **what cannot be decided can still be probed** --- and the probes themselves are falsifiable predictions of the framework (Section 8). External ultrametric-modeling literature [23,26] suggests the probes are not merely mathematical: hierarchical structure in cognition and disease spread is already modeled with ultrametric metrics, and the framework predicts that such models and Archimedean models can be observationally equivalent at the level of first-person or coarse-grained data, differing only in their seams.

## 5. Scale primitives

The fourth move strips units. In natural units $c = \hbar = k_B = 1$, length and time have the same dimension and energy, frequency, inverse length, and temperature all become comparable. Three statements then have exact content.

**Frequency is a count.** A cycle is a dimensionless winding number; a frequency is a count of cycles per unit reference time, and in natural units the reference time is itself a count of reference cycles, so frequency is a ratio of counts --- a rational number. The Compton frequency $\omega_C = m$ (in natural units) is the Hamiltonian clock of a massive state, not a thermodynamic one: it persists at $T=0$ because it is a phase rate, $\psi \sim e^{-imt}$, whereas the thermal frequency $\omega_T = T$ vanishes at absolute zero. The distinction between the Hamiltonian clock and the thermal clock is not anthropocentric; it is the distinction between count and derivative.

**The fine-structure constant is a ratio.** $\alpha = e^2/(4\pi\epsilon_0 \hbar c)$ is dimensionless: a ratio of coupling strengths, expressible without meters or seconds. Like frequency, it is a number-theoretic object, a point in $\mathbb{Q}$ (or a finite extension), not a feature of any particular metric completion.

**Temperature is a derivative.** Entropy is the primary count: $S = \ln \Omega$ (or the von Neumann form); temperature is secondary: $1/T = \partial S / \partial E$. Absolute zero is not the absence of energy but the absence of thermal mixing, $\beta \to \infty$. The gravitational constant is likewise not primitive: in natural units $G = \ell_P^2$, and black-hole entropy $S_{BH} = A/4G$ is the statement "one bit of entropy per four Planck areas" --- a ratio, not a force constant.

Ostrowski's theorem [3] closes the argument: every nontrivial absolute value on $\mathbb{Q}$ is equivalent either to the Archimedean absolute value or to a $p$-adic absolute value for some prime $p$. The real line $\mathbb{R}$ is therefore **one completion among many**, the Archimedean place; the $p$-adic completions are equally valid metric completions. If the natural observables are counts and ratios --- elements of $\mathbb{Q}$ --- then writing them as real numbers is a choice of place, and the adelic ring $\mathbb{A}_\mathbb{Q}$ keeps all completions simultaneously. The physics is in dimensionless ratios ($L/\lambda_F$, $\lambda/\lambda_T$, $\alpha$, $N_{\text{cycles}}$), not in meters or seconds; the author's prior records derive exactly this conclusion from the Bekenstein bound [9] and compile its consequences across fundamental equations [10,11,12].

## 6. The locale framework

The four moves assemble into one doctrine. Physics is a field theory over a background (locale); its observable content is locale-relative; the pedagogical map is the image-space metric of a rendering interface whose substrate is underdetermined from inside; and the natural observables are counts and ratios, which live in $\mathbb{Q}$, which has many places. The Archimedean--ultrametric distinction is not a speculative alternative theory: it is the sharpest instance of the general locale structure that effective field theory already embodies --- the validity domain of an effective theory is a locale, and crossing a seam (decoupling, symmetry breaking, scale crossing) is the same operation as changing place.

The structural isomorphism between the EFT validity-domain hierarchy and the completion hierarchy must be labeled honestly. It is a **pedagogical unification**, not a discovery: the isomorphism was assembled after the fact from documented cases, carries no pre-registered prediction, and its evidential weight is therefore capped at retrodiction (Section 8). What it buys is not evidence but economy: one vocabulary --- locale, seam, rendering, place --- for phenomena that currently live in separate literatures.

Where the premises end: the framework takes "locale" (a specified domain of applicability) and "interface" (a map from substrate to image space) as unanalyzable primitives, defined ostensively. It does not propose a dynamical theory of seams --- it does not explain why locales change or which locales exist in nature. It does not claim the substrate *is* ultrametric; it claims the substrate metric is undecidable from inside the interface, and that the decision is not needed for the framework's testable content. It derives no new unit and no new completion. The novelty is bounded by the depth of these premises, no more.

## 7. The four claims

The framework is summarized in four claims, each with a falsification condition (Section 8):

**C1 (locale-conditionality).** Every physical statement is a conditional truth: it holds only relative to a specified locale, and the physics lives at the seams. *Status:* a synthesis of documented cases [4,5,24,25,28]; restatement, not discovery.

**C2 (map-territory).** The pedagogical map is never the ontological territory; the territory is the invariant relational structure that transfers across locale seams. *Status:* ontology imported from structural realism [2] with its critics engaged [20,21,22]; replaceable without loss to the framework.

**C3 (interface underdetermination).** First-person observation inside a rendering interface cannot decide the substrate metric --- Archimedean or ultrametric --- yet structure leaks, so the interface can be probed from inside. *Status:* visual case established [6]; generalization to arbitrary channels is this paper's net-new core.

**C4 (scale primitives).** Natural observables are counts and ratios; the Archimedean real line is one completion among many [3]; the physics is in dimensionless ratios. *Status:* restatement of standard metrology plus integration of prior records [9,10,11,12].

## 8. Falsifiability register

Every claim above carries a concrete disconfirmation condition. These are the framework's testable commitments, stated so that the framework can lose.

- **F1 (against C1).** Exhibit a physical statement that holds across all locale changes --- a law with no domain-of-applicability seam --- or show that some canonical conditional truth has conditions that cannot be specified even in principle. A background-independent quantum gravity in which "locale" cannot be articulated would stress C1 at its deepest seam.
- **F2 (against C2).** Exhibit an empirically accessible consequence of substance beyond relations --- an intrinsic, non-relational state with a measurable signature. No such signature is known; a confirmed one would refute the structural-realist gloss.
- **F3 (against C3).** Exhibit a finite first-person observation protocol that decides the substrate metric class from inside the interface: a perceptual probe that betrays a non-Archimedean substrate without any outside knowledge of the rendering map. The probe-design question is open; the framework's strongest commitment is that no such protocol exists, and the strongest known candidates (discrete apparent-size steps at exactly $p$-adic rationals; absent smooth parallax) remain unruled-out but unproven [6]. This is the claim's positive evidential weight, and it is the intended target of the next audit pass (Section 9).
- **F4 (against C4).** Exhibit a physical prediction that depends on the choice of units or the choice of completion --- a unit-dependent or place-dependent observable. A confirmed unit-dependent prediction would refute the claim that the physics is in dimensionless ratios.

The honesty register is explicit: C1 is a restatement; C2's ontology is imported; C4 is an integration; only C3 carries positive evidential weight, and it is bounded by the interface/rendering primitives. No cross-domain correspondence in this paper is claimed as independent evidence; the completion-to-background isomorphism of Section 6 is labeled retrodictive by construction.

## 9. The next question

The framework's recursive question, in the sense of the methodology record [7], is: **what would make the interface-underdetermination claim physics rather than epistemology --- a derivation from a Hamiltonian or measurement model of the rendering channel, rather than an argument from perception?** The next pass must either answer this question or explicitly refuse it. A measurement-model formulation would define a rendering channel as a stochastic map from substrate observables to image observables, characterize the fiber of observational equivalence over the two metric classes, and state the minimal probe that separates fibers --- turning F3 from an open question into a theorem or its refutation. The framework predicts the fiber is nonempty; it does not yet know its geometry.

## References

[1] A. F. Monna. "Sur une transformation simple des nombres P-adiques en nombres reels." *Indagationes Mathematicae* 55 (1952), 1--9. DOI 10.1016/s1385-7258(52)50001-5.

[2] J. Ladyman and D. Ross. *Every Thing Must Go: Metaphysics Naturalized.* Oxford University Press, 2007. DOI 10.1093/acprof:oso/9780199276196.001.0001.

[3] A. Ostrowski. "Über einige Lösungen der Funktionalgleichung $\psi(x)\cdot\psi(y) = \psi(xy)$." *Acta Mathematica* 41 (1916), 271--284. DOI 10.1007/BF02422947.

[4] C. P. Burgess. "Introduction to Effective Field Theory." arXiv:hep-th/0701053, 2007.

[5] H. Georgi. "Effective Field Theory, Past and Future." arXiv:0908.1964, 2009.

[6] R. B. Quni-Gudzinas. "Non-Archimedean Projective Perspective: The Monna Map as a Visual Rendering Interface." the QNFO archive, 2026. Concept https://papers.qnfo.org/papers (v0.3: https://papers.qnfo.org/papers/non-archimedean-projective-perspective/).

[7] R. B. Quni-Gudzinas. "The Universal Ignorance Audit: A Fifteen-Question Method for Systematic Inquiry into the Structure of Not-Knowing." the QNFO archive, 2026. https://papers.qnfo.org/papers/universal-ignorance-audit/.

[8] R. B. Quni-Gudzinas. "Knowing What We Do Not Know: Ignorance Auditing, AI-Generation Detection, and the Epistemic Lessons of an AI-Assisted Research Pipeline." the QNFO archive, 2026. https://papers.qnfo.org/papers.

[9] R. B. Quni-Gudzinas. "Non-Anthropocentric Natural Units: From the Bekenstein Bound to Ostrowski's Theorem." the QNFO archive, 2026. https://papers.qnfo.org/papers/non-anthropocentric-natural-units/.

[10] R. B. Quni-Gudzinas. "The Ostrowski Dimensionless Reformulation: A Systematic Compilation of Fundamental Physics Equations in Planck Units." the QNFO archive, 2026. https://papers.qnfo.org/papers/ostrowski-dimensionless-reformulation/.

[11] R. B. Quni-Gudzinas. "Consilience Between Physics and Number Theory: Convergent Theses from Ostrowski's Theorem." the QNFO archive, 2026. https://papers.qnfo.org/papers/consilience-physics-number-theory/.

[12] R. B. Quni-Gudzinas. "Measure-Theoretic Artifacts of the Archimedean Place: A Complete Taxonomy and the Adelic Reconstruction." the QNFO archive, 2026 (v2.0). https://papers.qnfo.org/papers/measure-theoretic-artifacts-adelic-completion/.

[13] R. B. Quni-Gudzinas. "The Observer Inside the Tree: Can Self-Location in an Ultrametric Structure Resolve the Inside/Outside Schism?" the QNFO archive, 2026. https://papers.qnfo.org/papers/s10-observer/.

[14] R. B. Quni-Gudzinas. "The Computable Real Boundary: Where Physics Ends and Cognitive Fiction Begins." the QNFO archive, 2026. https://papers.qnfo.org/papers/computable-real-boundary/.

[15] R. B. Quni-Gudzinas. "A Critical Treatise on the Load-Bearing Assumptions of Quantum Mechanics, Thermodynamics, and Computation." the QNFO archive, 2026. https://papers.qnfo.org/papers/electron-hook-treatise/.

[16] R. B. Quni-Gudzinas. "The Hidden Fractures: Self-Referential Calibration and the 29 Schisms of Physics." the QNFO archive, 2026. https://papers.qnfo.org/papers/29-schism-synthesis/.

[17] R. B. Quni-Gudzinas. "The Universe Category: A Single Functor Encoding Quantization, Stability, and Factorization." the QNFO archive, 2026. https://papers.qnfo.org/papers/universe-category-functor/.

[18] O. Dovgoshey, O. Martio, V. Ryazanov, and M. Vuorinen. "The Cantor function." *Expositiones Mathematicae* 24 (2006), 1--37. DOI 10.1016/j.exmath.2005.05.002.

[19] C. Weiß. "P-adic Poissonian pair correlations via the Monna map." *Indagationes Mathematicae*, 2024/2025. DOI 10.1016/j.indag.2024.09.012.

[20] M. Esfeld. "Ontic structural realism and the interpretation of quantum mechanics." *European Journal for Philosophy of Science*, 2012. DOI 10.1007/s13194-012-0054-x.

[21] M. Morganti. "Is There a Compelling Argument for Ontic Structural Realism?" *Philosophy of Science*, 2011. DOI 10.1086/662258.

[22] M. Morganti. "On the Preferability of Epistemic Structural Realism." *Synthese*, 2004. DOI 10.1023/b:synt.0000047712.39407.c3.

[23] A. Khrennikov. "Quantum-like modeling of cognition." *Frontiers in Physics*, 2015. DOI 10.3389/fphy.2015.00077.

[24] R. Nugayev. "The fundamental laws of physics can tell the truth." *International Studies in the Philosophy of Science*, 1991. DOI 10.1080/02698599108573379.

[25] P. P. Allport. "Are the laws of physics 'economical with the truth'?" *Synthese*, 1993. DOI 10.1007/bf01064340.

[26] A. Khrennikov and K. Oleschko. "An Ultrametric Random Walk Model for Disease Spread Taking into Account Social Clustering of the Population." *Entropy*, 2022. DOI 10.3390/e22090931.

[27] M. Pitkänen. "p-Adic TGD: Mathematical Ideas." arXiv:hep-th/9506097, 1995.

[28] J. D. Wells. "Effective Field Theories and the Role of Consistency in Theory Choice." arXiv:1211.0634, 2012.
