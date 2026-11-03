---
title: "Non-Archimedean Projective Perspective: The Monna Map as a Visual Rendering Interface"
author: "Quni-Gudzinas, Rowan Brad"
orcid: "0009-0002-4317-5604"
affiliation: "QNFO"
date: "2026-08-16"
version: "v0.2"
license: "CC-BY-4.0"
doi: ""
status: "published"
keywords: ["non-Archimedean geometry", "ultrametric", "Monna map", "visual perception", "perspective", "projective geometry", "p-adic", "Ostrowski theorem", "ontology", "rendering interface"]
---

# Non-Archimedean Projective Perspective: The Monna Map as a Visual Rendering Interface

## Abstract

Things farther away appear smaller, and two-point linear perspective is taken to approximate the eye. That entire phenomenology is Archimedean geometry. This paper asks what changes if the metric of physical space were instead non-Archimedean and ultrametric — would we perceive the same thing, and what would that mean ontologically? **Why a reader should care:** the question converts a familiar visual fact into a decisive constraint on a live research program (p-adic and ultrametric physics [1,6,7,8]) — smooth perspective does not rule out a discrete world, it only rules out *direct* perception of one, and the distinction marks the exact boundary between physics and phenomenology. **Premise depth:** the underdetermination result rests on two imported premises — (i) perception is a constructed interface, not a direct reading of the substrate (Kantian interface premise, adopted from the corpus's Unified Theory of Non-Archimedean Ontology [1]); (ii) the Monna map, a surjective non-continuous map from the p-adics to the reals, exists (established mathematics [9]). Given (i) and (ii) the conclusion follows at theorem level; without them it is unfounded. The naive alternative — ultrametric perception *without* a rendering — is already falsified by the observed smoothness of perspective, which is recorded here as falsified hypotheses C3–C4 rather than silently avoided.

**v0.2 (2026-08-16).** Post-publication red-team corrections: the Monna-map discontinuity justification is corrected (§4 — the invalid "totally disconnected, hence discontinuous" shorthand is replaced by the digit argument, H1); the code-availability declaration is corrected and the verification script is deposited (H2); the §5 rendering maps coordinate-wise into $\mathbb{R}^3$; and Monna's original 1952 construction is now cited (ref 12). The underdetermination theorem, the falsifiability register, and the ontology claims are unchanged.

## 1. Introduction and Positioning

The originating question (Obsidian note `_26228180341.md`, 2026-08-16): *"Things that are farther away appear smaller, and 2 point linear perspective is thought to approximate our eyes — but what if instead of an Archimedean linear geometry, perspective is actually non-Archimedean and ultrametric? Would we perceive the same thing, and what would that actually mean ontologically?"*

The QNFO corpus already treats ultrametric geometry as the candidate substrate for physics and computation [1,2,3], the external p-adic-physics literature pursues the same substrate hypothesis at the Planck scale [6,7,8], the corpus treats the observer as a node inside the ultrametric tree [4], and names the Monna map as the ratio-based interface between p-adic structure and continuous experience [5]. What the corpus lacks — identified by the full-corpus due-diligence sweep of 2026-08-16 (995 living-paper records, evidence in `artifacts/external-search/corpus-sweep-evidence.json`) — is the worked example of *visual projective perspective*: vanishing points, apparent-size scaling, and the line of sight, analyzed from both the Archimedean and the ultrametric side. This paper supplies that worked example in four moves: (2) the Archimedean anatomy of perspective; (3) the ultrametric demolition of its ingredients; (4) the rendering lemma that restores the appearances; (5) the underdetermination theorem and its ontological consequences.

---

## 2. The Archimedean Anatomy of Perspective [TERRITORY]

Linear perspective rests on three Archimedean ingredients.

**(a) Similar triangles.** For an object of height $h$ at distance $d$ from an eye, the apparent size is governed by the subtended angle $\theta \approx h/d$ for $d \gg h$. The proportionality is the similar-triangles theorem of Euclidean geometry, and it requires two things: a well-defined ratio of lengths, and a well-defined angle.

**(b) Additive distance along geodesics.** The distance $d$ is accumulated along a straight line — a geodesic — and satisfies the Archimedean property: finitely many steps of any positive length can cross any finite gap. Distance is the sum of its parts, which is exactly what makes "farther" a continuous degree.

**(c) Projective closure.** Two-point perspective is projective geometry over $\mathbb{R}$: parallel lines are completed by ideal points — the vanishing points — on the line at infinity. The construction is algebraic over the reals and inherits the real field's order, completeness, and Archimedean valuation.

Every element of the familiar phenomenology — smooth shrinking, vanishing points, the horizon as a line — is Archimedean machinery.

---

## 3. The Ultrametric Demolition [TERRITORY]

Now suppose the metric is ultrametric: $d(x,z) \leq \max(d(x,y), d(y,z))$ for all $x, y, z$ — the strong triangle inequality. Four standard consequences [BACKGROUND — not from search; standard metric theory] dismantle §2 piece by piece.

**(a) Every triangle is isosceles** (the two longest sides are equal). The geometry has no "betweenness" in the Euclidean sense; detours never add distance.

**(b) Balls have no boundaries.** In an ultrametric space every point of a ball is a center of that ball, and balls are clopen — simultaneously open and closed. A "surface" of a ball is empty. There is no horizon *line*: the boundary the vanishing point would sit on does not exist.

**(c) The space is totally disconnected.** No two points are joined by a continuous path: any continuous map $f \colon [0,1] \to X$ from the connected interval into a totally disconnected space is constant. There are no continuous light rays, no lines of sight, no geodesic spray along which "farther" could accumulate.

**(d) Size, if imposed by fiat, is discrete.** In the p-adic model, with $\lvert \cdot \rvert_p$, distances take values in $\{p^n : n \in \mathbb{Z}\}$. An apparent-size law $\theta \propto 1/d$ would then jump by factors of $p$ — a digital staircase, not a smooth gradient.

So the direct answer to the originating question is: **no.** If perception were a direct reading of an ultrametric substrate, we would not perceive the same thing — we would perceive no continuous perspective at all, and the vanishing "point" would decompose into a tree of nested clopen cells.

But that is the naive answer, and it is already falsified by ordinary vision. The interesting question is not whether direct ultrametric perception survives — it does not — but whether a *rendered* one does. That is the next move.

---

## 4. The Rendering Lemma [MAP]

**Definition (rendering interface).** Let $X$ be the substrate metric space and $V \cong \mathbb{R}^3$ the experienced visual field. A rendering is a surjective map $R \colon X \to V$. Perception measures only quantities defined in $V$.

**The candidate map.** The Monna map $M \colon \mathbb{Q}_p \to \mathbb{R}$ is the classical surjection from the p-adics onto the reals [9], and it is discontinuous at every point. (A tempting shorthand — "totally disconnected domain, connected codomain, hence discontinuous" — is not a valid general principle: the Cantor function is a continuous surjection from a totally disconnected space onto $[0,1]$, and $\lvert \cdot \rvert_p \colon \mathbb{Q}_p \to \mathbb{R}$ is non-constant and continuous. The discontinuity follows from the map's digit definition instead: $-p^m \to 0$ p-adically while $M(-p^m) = p^{-m+1} \to \infty$ in $\mathbb{R}$.) Pitkänen's "canonical identification" of p-adic and real physics is the same construction [10,11], both descending from Monna's original transformation [12]. The corpus's Module 11 already proposes the Monna map as the ratio-based consciousness interface [5], and UNO states the interface premise directly: the mind "naturally smooths the discrete nature of reality into a continuous narrative" [1].

**Lemma (rendering).** Given premise (i) — perception is a rendering — the metric structure an observer experiences is the metric of the image space $V$, not the metric of $X$. In particular, a continuous-looking visual field is compatible with an ultrametric substrate whenever a surjective rendering exists. *Falsifiability C1: a no-go theorem ruling out surjective renderings of the required kind would kill the lemma.*

The Monna map is a *candidate*, not *the* map: it is non-injective and far from canonical (§8). What matters for the argument is existence, and existence is established [9].

---

## 5. The Underdetermination Theorem [MAP]

**Theorem (perceptual underdetermination).** Given premises (i) and (ii), no finite set of first-person visual observations — apparent sizes, parallax, vanishing-point convergence — can distinguish an Archimedean substrate from an ultrametric substrate.

*Proof sketch.* Both substrates render into the same image space $V$. For the Archimedean substrate, take $R$ to be the familiar similarity rendering. For the ultrametric substrate, compose a surjection $\pi \colon X \to \mathbb{Q}_p$ with the Monna map applied coordinate-wise to the three components of $V \cong \mathbb{R}^3$: $R = (M \circ \pi, M \circ \pi, M \circ \pi)$. Every measurement the observer can make lives in $V$; the two renderings differ only behind the interface, where no measurement reaches. Therefore the observation records are identical. $\square$

**Corollary.** "Would we perceive the same thing?" — yes, in principle: the same first-person world is compatible with both metrics.

**The honest converse.** This does not show the world is ultrametric. It shows the metric of the substrate is *not decidable from inside the interface*. The equivalence itself — not either disjunct — is the finding. And the naive converse fails too: smooth perspective does not establish an Archimedean world, because §4's rendering exists. Vision constrains the *interface*, not the world.

---

## 6. Ontological Consequences [MAP]

**(1) The continuum is demoted to an appearance.** Apparent continuity is evidence about the rendering, not about the substrate — Kant's forms-of-intuition thesis, sharpened by an explicit candidate geometry: the smoothness that makes linear perspective "look right" is the geometry we assumed before we drew.

**(2) Distance becomes a degree of isolation, not a gap.** In the corpus's informational ontology, substrate distance measures the degree of computational isolation between states [1]. "Far" is deep in the tree, not far along a line.

**(3) Identity becomes tree-based.** An object is a cluster in nested neighborhoods; individuation is partition-theoretic, not point-like.

**(4) Ostrowski's theorem turns the metric into a postulate.** The only nontrivial absolute values on $\mathbb{Q}$ are the real one and the p-adic ones [BACKGROUND — not from search; standard]. The Archimedean choice baked into every ruler, every eye, and every perspective diagram is therefore a genuine postulate, validated only by measurement — by how the physical universe responds — never by mathematics alone.

**(5) The interface can be studied from inside.** What we cannot decide, we can still probe: a rendering with structure leaks structure. The falsifiable probes are in §7.

---

## 7. Falsifiability Register

| # | Claim | Type | Falsifiability condition | Status |
|:--|:------|:-----|:--------------------------|:-------|
| C1 | A surjective rendering from an ultrametric model onto the visual field exists (rendering lemma) | MAP | a no-go theorem rules out surjective renderings of the required kind | OPEN |
| C2 | First-person observations cannot separate Archimedean from ultrametric substrates (underdetermination) | MAP | a first-person observable invariant across all Archimedean renderings but absent from all ultrametric renderings is found | OPEN |
| C3 | Direct (unrendered) ultrametric perception predicts discrete apparent-size jumps | naive model | smooth size–distance laws observed | **FALSIFIED** (ordinary vision); motivates §4 |
| C4 | Direct ultrametric perception predicts the absence of smooth parallax | naive model | smooth parallax observed | **FALSIFIED** (ordinary vision); motivates §4 |
| C5 | The interface, being a rendering of something, exhibits glitch-level discreteness | MAP-speculative | a worked Monna-map rendering (planned demo) reproduces all known smooth vision with no distinctive residue | OPEN, deferred to the P4 demo |

---

## 8. Mandatory Symmetry Template

### Where External Literature Supports the Claim

- **Dragovich (2003) [6], Zúñiga-Galindo (2023) [7], Zúñiga-Galindo & Mayes (2024) [8]** — p-adic quantum mechanics is a live, rigorous research program; the question "is the substrate non-Archimedean?" is not idle speculation, and [7] already shows p-adic models produce physical predictions (Planck-scale Einstein-causality violation).
- **Weiß (2024) [9]** — the Monna map is current mathematics, used to transfer real sequences with Poissonian pair correlations to the p-adic setting; the rendering map is a real object, not a metaphor.
- **UNO [1]** — the interface premise (the mind smooths the discrete into a continuous narrative) and the informational ontology of distance are stated corpus doctrine.

### Where External Literature Constrains or Contradicts the Claim

- **No external paper applies the Monna map to visual perception.** The rendering lemma (§4) is this paper's extrapolation; the corpus's M11 [5] proposes it internally but is not external validation. A reader should treat §4–§6 as interpretive proposal, not established result.
- **The p-adic program treats $\mathbb{Q}_p$ as quantum position space at the Planck scale** [6,7,8] — not as the metric of macroscopic visual space. The perceptual application here is a further step the cited literature does not take.
- **The Monna map is non-injective and non-canonical.** Many surjections onto $\mathbb{R}$ exist; the theorem needs only *one*, so its force survives, but the map cannot be recovered from the phenomenology — which is exactly the underdetermination conclusion.
- **The theorem's force comes entirely from premise (i),** which is philosophical. No experiment proposed in §7 distinguishes the interfaces; C5 is the only probe that bites, and it is deferred. [NO CONSTRAINING EVIDENCE FOUND] applies to the naive-model falsifications C3–C4: nothing in the literature rescues direct ultrametric perception.

---

## 9. Conclusion

Naive ultrametric perception is falsified by smooth vision — recorded, not avoided (C3–C4). Rendered ultrametric perception is indistinguishable from Archimedean perception (§5). Together: the world's metric is a postulate, validated only by interaction, and the only thing perception ever measures is the interface. The originating question's answer is therefore both — we would perceive the same thing, and the meaning of that fact is that the continuum is a rendering, not a fact about the rendered.

---

## Declarations

**Funding.** This work received no external funding.
**Competing interests.** The author declares no competing interests.
**Data availability.** No experimental data were generated. Evidence files for the due-diligence sweep and live API verifications are deposited (`artifacts/external-search/`).
**Code availability.** The field-level citation-verification script used to produce `citation-audit.md` is deposited as `citation-field-verify.py`; no other code was required.
**Ethics approval.** Not applicable.
**Preprint policy.** This manuscript is posted as a preprint; it has not been submitted to any journal.

---

## References

1. Quni-Gudzinas, Rowan Brad. *A Unified Theory of Non-Archimedean Ontology*. the QNFO archive, 2026. https://papers.qnfo.org/papers.
2. Quni-Gudzinas, Rowan Brad. *Ultrametric Intelligence: A Non-Archimedean Foundation for Artificial General Intelligence*. the QNFO archive, 2026. https://papers.qnfo.org/papers/ultrametric-intelligence/.
3. Quni-Gudzinas, Rowan Brad. *Ultrametric Cognition*. the QNFO archive, 2026. https://papers.qnfo.org/papers.
4. Quni-Gudzinas, Rowan Brad. *The Observer Inside the Tree: Can Self-Location in an Ultrametric Structure Resolve the Inside/Outside Schism?* the QNFO archive, 2026. https://papers.qnfo.org/papers/s10-observer/.
5. Quni-Gudzinas, Rowan Brad. *ULTRAMETRIC PHYSICS: Module 11: Monna Map as Ratio-Based Consciousness Interface*. the QNFO archive, 2026. https://papers.qnfo.org/papers.
6. B. Dragovich. *p-Adic and Adelic Quantum Mechanics*. arXiv:hep-th/0312046, 2003.
7. W. A. Zúñiga-Galindo. *p-Adic Quantum Mechanics, the Dirac Equation, and the violation of Einstein causality*. arXiv:2312.02744, 2023.
8. W. A. Zúñiga-Galindo and N. P. Mayes. *p-Adic quantum mechanics, infinite potential wells, and continuous-time quantum walks*. arXiv:2410.13048, 2024.
9. C. Weiß. *P-adic Poissonian Pair Correlations via the Monna Map*. arXiv:2406.13255, 2024.
10. M. Pitkänen. *p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone*. arXiv:hep-th/9410058, 1994.
11. M. Pitkänen. *p-Adic TGD: Mathematical Ideas*. arXiv:hep-th/9506097, 1995.
12. A. F. Monna. *Sur une transformation simple des nombres P-adiques en nombres réels*. Indagationes Mathematicae (Proceedings), 55:1–9, 1952. DOI 10.1016/s1385-7258(52)50001-5.
