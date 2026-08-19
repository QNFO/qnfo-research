---
title: "ZX Diagrams at the Seam: Spiders, Pauli Webs, Gadgets, and the Cafeteria Problem of Cross-Disciplinary Imports"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-19"
license: "CC BY-NC-SA 4.0"
doi: "10.5281/zenodo.22017723"
status: "published"
keywords: ["ZX calculus", "diagrammatic reasoning", "quantum computing", "map-territory", "epistemology", "import provenance"]
---

## Abstract

Diagrammatic languages are the most successful interface between quantum computing and the
human mind. The ZX calculus — with its spiders, Pauli webs, and gadgets — is taught as *the*
intuitive picture of quantum processes, and its completeness theorems are among the finest
results in the field. Yet the same diagrams are increasingly being loaded with imports from
disciplines that have nothing in common with a drawing plane: loop-quantum-gravity spin
networks, quantum groups, holographic entropy, and toy black holes. This paper performs a
fault-line audit of the three central constructs. It tables, for each construct, the exact
import provenance — which discipline it came from, what it silently carries — and audits the
mutual compatibility of those imports. The finding is precise: within the computational domain
(circuits, codes, compilation) the imports are demonstrably coherent, and the diagrams earn
every bit of their success; the fault lines appear exactly where 3+1-dimensional particle
physics and 1-dimensional thermodynamics are mixed into a 2-dimensional map without any
compatibility check. The paper then names the seam — the place where each diagram stops being a
map and starts being mistaken for territory — and generalizes the resulting "cafeteria problem":
siloed disciplines remain separate except when it is convenient to mix their imports, with no
regard for mutual compatibility. The conclusion is not that the diagrams are wrong; it is that
they are maps, and the discipline of using a map is knowing where it ends. Every claim here is
either an externally verified fact about the literature, or an explicitly marked argument; the
premises the argument rests on — that a formalism can be about a physical reality at all, that
unchecked import-mixing is epistemically risky, and that the distinction between a picture of
computation and a picture of reality is well-founded — are stated plainly in the final section,
where the paper's own map ends.

## 1. Introduction: the satisfaction of diagrams

There is a particular pleasure in watching a diagram close. A spreadsheet, a graph, a wiring
diagram: connections assemble, the structure clicks, and something that was formless becomes
shape. That satisfaction is real, and it is doing real work — in engineering, in teaching, in
communication. But the satisfaction is not evidence. A picture that feels right may still be a
picture of nothing in particular, and the tighter its internal logic, the easier it is to forget
that it is a picture at all.

This is the situation of the ZX calculus, the leading diagrammatic language of quantum
computing. ZX diagrams are the workhorse of modern circuit optimization, error correction, and
measurement-based computation. They are sound and complete for substantial fragments of quantum
mechanics — results proved rigorously, not intuited [1, 2, 3, 4]. Their success is beyond
dispute, and their utility is demonstrated daily in real compilers. Yet the same diagrams that
are so carefully proved to capture the algebra of quantum computation are increasingly shown
alongside objects that no proof in the calculus touches: spin networks from loop quantum
gravity [5], quantum groups [6], holographic codes with Rényi entropy and toy black holes [7],
lattice-surgery geometries [8]. Each of these imports arrives with its own rigorous story. What
is never supplied is a check of whether the stories are compatible with each other — or with
the 2-dimensional drawing plane on which they are all being told.

This paper is a fault-line audit. It takes the three named constructs of the ZX calculus —
spiders, Pauli webs, and gadgets — and asks, for each: where did you come from, what do you
silently carry, and where does the map end? It then audits the pairwise compatibility of the
imports, and generalizes the resulting pattern into a "cafeteria problem" that is not specific
to quantum computing at all: siloed disciplines remain separate except when it is convenient to
mix and match, and the mixing happens without regard for mutual compatibility or contradiction.

The paper is deliberately narrow in its claims. It does not dispute the mathematics of the ZX
calculus, which it imports and respects. It does not claim the diagrams are useless, or that
their use is necessarily misleading — within the computational domain they are exactly as good
as their theorems say. It claims one thing, precisely: that the physical bearing of the
diagrams — their status as pictures of quantum reality rather than pictures of computation — is
unestablished, that the published record shows imports from incompatible silos being loaded onto
the diagrams without compatibility checks, and that this pattern is a general failure mode of
cross-disciplinary borrowing. The evidence for the first two parts is in the literature and is
cited. The third part is an argument, and it is marked as one.

## 2. The calculus and its constructs

The ZX calculus was introduced by Coecke and Duncan as a diagrammatic language for
"interacting quantum observables" [9]. Its grammar is deceptively simple: two kinds of nodes —
green spiders and red spiders — connected by wires, with angles attached to the nodes. A green
spider represents the copying and merging of computational-basis information; a red spider the
same operation in the Hadamard-rotated basis. The rewrite rules of the calculus — fusion,
bialgebra, and their kin — let a practitioner transform one diagram into another while
preserving the represented linear map exactly. Completeness, proved in stages by Backens [2],
Jeandel, Perdrix, and Vilmart [1], and Wang [3], means that every matrix equality in the
relevant fragment is provable diagrammatically: nothing is lost by working in the picture.
Van de Wetering's survey [10] is the standard working reference.

Three constructs do most of the work in modern applications.

**Spiders.** The generators themselves. A spider is a node with any number of inputs and
outputs, carrying a phase. Its algebraic meaning is fixed: it is a special dagger Frobenius
algebra — a structure that says "copy, then merge, coherently." Spiders are what make the
calculus a calculus: the fusion rule lets adjacent spiders combine, and the complementarity
(bialgebra) rule captures the Z/X interplay that is the heart of quantum mechanics' two
non-commuting bases.

**Pauli webs.** When a ZX diagram is used to analyze a quantum error-correcting code, the
stabilizer structure of the code can be tracked through the diagram as a "web" of Pauli
operators — families of X/Z strings that commute with the code's logical operations and whose
behavior under the diagram's rewrites reveals the code's error properties. De Beaudrap and
Horsman proved that the operations of the ZX calculus match the operations of surface-code
lattice surgery exactly: red and green spiders correspond to rough and smooth merges and
splits [8]. Pauli webs have since become a standard tool for reading stabilizer structure
off diagrams, most strikingly in the holographic setting [7]. The calculus has also been
extended to the infinite, translation-invariant codes that dominate modern error-correction
proposals — lattice codes, convolutional codes — through the delayed stabilizer ZX-calculus,
which adds a single delay generator feeding data between time steps [17].

**Gadgets.** Non-Clifford operations are the expensive part of quantum computation, and the
diagrammatic community has developed "gadgets": small diagrammatic patterns that encode a
non-Clifford gate — the Hadamard gadget, the phase gadget — so that circuits can be optimized
by rewriting around them. The machinery descends from the one-way quantum computer of
Raussendorf, Browne, and Briegel [11], where computation proceeds by measuring entangled
resource states, and it reaches its diagrammatic form in the ZH calculus of Backens and
Kissinger [12], whose arity-generalized Hadamard nodes admit compact encodings of non-linear
classical functions. Vandaele's qubit-count optimization work [13] is a recent example of
gadgetization in action: reversing the gadgetization of Hadamard gates to save qubits, with
NP-hardness results and practical algorithms.

## 3. Import provenance: the cafeteria table

Every construct imports more than its definition. The following table gives, for each
construct, its home discipline, its canonical sources, and — critically — what it silently
carries that its users may not notice.

| Construct | Home silo | What it imports | What it silently carries |
|---|---|---|---|
| Spiders | Categorical quantum mechanics (2D diagrammatic algebra) | Dagger-special Frobenius algebra structure; fusion; complementarity [9, 1, 2, 3] | The 2D topology of wires and planes; the completeness theorems prove facts about the *algebra*, nothing about spacetime |
| Pauli webs | Stabilizer formalism / quantum error correction (lattice surgery, surface codes) | Stabilizer group structure; code distance and correction semantics; rough/smooth merge operations [8, 7] | A 2+1D code-over-time picture; in the holographic application, an AdS/CFT vocabulary of entropy, wormholes, and black holes [7] |
| Gadgets | Measurement-based computation / circuit optimization (compilation layer) | Graph-state resources; measurement-pattern semantics; T-count machinery [11, 12, 13] | The MBQC equivalence claims — a gadget is a map of a computation, validated by rewrite soundness, not by any physical realization |

The pattern is already visible in this table. The three constructs come from three different
disciplines — categorical algebra, error correction, and compilation — and in the computational
domain they cooperate flawlessly, because they are all maps of the same algebraic object: a
linear map between qubits. The cooperation is proved where it matters (soundness and
completeness), and the compiler industry runs on it.

But the table also shows where the imports have started to outgrow the map. Spin networks from
loop quantum gravity have been embedded into the ZXH calculus [5]. Braided ZX calculi have been
built on the quantum group u_q(sl_2) [6]. Holographic codes have been analyzed through Pauli
webs, with Rényi entropy and toy black-hole/wormhole models computed diagrammatically [7].
These are imports from 3+1-dimensional particle physics and 1-dimensional thermodynamics —
statistical mechanics, entropy, gravity — arriving on a 2-dimensional drawing plane.

## 4. Compatibility audit: where the map is coherent, and where it is not

The audit asks, for each pair of imports: are these two structures known to be mutually
compatible, in the sense that the semantics they assign to the same diagram agree?

**Within the computational domain, the answer is yes, with proof.** Spiders and Pauli webs are
coherent because the stabilizer fragment of the ZX calculus is complete [2, 14, 15]: every
stabilizer equality is provable diagrammatically, the rule set has been shown minimal in the
sense that no rewrite rule is redundant [18], and the lattice-surgery correspondence is an
exact match, not an analogy [8]. Spiders and gadgets are coherent because gadgetization
preserves circuit semantics — the ZH calculus is complete for universal quantum computation
[12], and qubit-count optimization via gadget reversal preserves the number of non-Clifford
gates [13]. Pauli webs and gadgets are coherent because both are compile-layer tools on the
same stabilizer structure: the Pauli Fusion computational model, which can represent lattice
surgery operations, is natively depictable in ZX [13]. Within this domain, the diagrams are
doing exactly what their theorems say they are doing. This is not in dispute, and the claim of
this paper does not touch it.

**At the boundary of the physical imports, the answer is: unchecked.** Three specific fault
lines emerge from the literature:

1. **The 2D-to-3+1D fault line.** Spin networks are structures of 3+1-dimensional quantum
   gravity — SU(2) representation theory carrying angular-momentum data [5]. Quantum groups
   carry deformation parameters that encode physical symmetry deformations [6]. When these are
   embedded in a 2-dimensional diagrammatic calculus, no published work checks whether the
   dimensional semantics of the source theory survive the embedding. The completeness theorems
   of the host calculus are theorems about its own algebra; they say nothing about the imported
   structures' physical claims.

2. **The 2D-to-1D fault line.** Holographic codes compute Rényi entropies and model black
   holes and wormholes through Pauli webs [7]. Entropy is a 1-dimensional thermodynamic
   concept — a number attached to a statistical ensemble — and the holographic dictionary that
   connects it to geometry is itself one of the most contested constructions in physics. The
   ZX diagrams import the vocabulary (entropy, wormholes, the AdS/CFT correspondence) without
   any demonstrated compatibility with the diagrammatic semantics. The same fault line
   appears one step earlier, in the diagrammatic treatment of probability itself: the
   decohered ZX-calculus extends the language to classical probability distributions over
   classical bits [16], and that classical-statistical fragment is routinely mixed with the
   quantum one without a boundary being drawn. The diagrams are not wrong to track
   stabilizers; they are unvetted as carriers of thermodynamic and statistical claims.

3. **The 3+1D-to-1D fault line inside the same diagram.** When spin networks [5] and
   holographic entropy [7] appear in the same diagrammatic tradition, the two physical imports
   are being combined without any argument that their respective physics is mutually
   consistent — the exact scenario the originating question named: imports from 3+1D particle
   physics and 1D thermodynamics mixed in a 2D picture.

A search of the literature for a published compatibility audit — a paper checking, across the
silos, whether the imported semantics agree — found none as of August 2026. This absence is
itself the finding: the fault lines are not disputed territory; they are unvisited territory.
The negative claim is bounded by the search and by its stated falsifier: a published
compatibility audit that establishes mutual consistency of the physical imports — for example,
a demonstrated agreement between the holographic dictionary and the 2D diagrammatic semantics —
would falsify the "unchecked" component of the claim, and the claim is written to be revised
if one appears.

## 5. The seam: where the map ends

A map is not wrong when it omits things; it is wrong when its users forget it omits things.
Every construct has a seam — the place where the map stops being a reliable picture — and the
seam is unmarked on the diagrams themselves.

- **The spider's seam.** A spider is a copy/merge operation on a measurement basis. It is not
  a particle; its wires are not worldlines; the drawing plane is not spacetime. The
  completeness theorems guarantee that every matrix equality is provable in the picture — they
  guarantee nothing about whether the topology of the picture corresponds to the topology of
  any physical process. When a reader sees a spider as a physical event, they have crossed the
  seam.

- **The Pauli web's seam.** A Pauli web is bookkeeping for stabilizer structure. Its QEC
  semantics — code distance, correction — are map-internal and sound. When a web is read as
  "the spacetime structure of the code," or as evidence about black holes, the holographic
  vocabulary has been imported across the seam without a visa check.

- **The gadget's seam.** A gadget is a diagrammatic encoding of a gate. Its MBQC equivalence
  claims are map-internal and proved. When a gadget is read as a hardware component — "this is
  how the T gate is built" — the physicalization assumptions of MBQC have been imported without
  the resource states being demonstrated.

Why does this matter? Because the cone of ignorance of a map — the region the map cannot
probe, since its questions are answerable only inside the picture — is unknown by
construction: a simplified map does not probe outside its own locality. The ZX calculus cannot
tell you whether the 2D topology of its diagrams is the topology of quantum reality, because
every question it can answer is answered inside the 2D picture. The seam is exactly where the
map's questions stop — and no theorem of the map can see past it.

## 6. The cafeteria problem

The pattern in the ZX literature is not local. Siloed disciplines — categorical algebra,
stabilizer theory, measurement-based computation, particle physics, thermodynamics — remain
separate in their journals, their vocabulary, and their standards of evidence. They come
together only when it is convenient: when a diagram needs an entropy, a graviton, or a
resource count, the import is fetched from the nearest silo and used without checking whether
the silos' claims are mutually compatible. The ZX calculus is a worked example of this
cafeteria problem, but the mechanism is general:

1. **A map gains users because it is internally valid.** The better the map, the louder the
   silence about its edges.
2. **The seam is unmarked on the map.** Nothing on a ZX diagram tells you where the
   computational guarantee ends and the physical claim begins.
3. **Imports arrive unvetted.** The published record shows the mixing; no published record
   shows the compatibility check.
4. **The cone of ignorance is unknown.** Because the map never probes outside its own
   locality, nobody can say how much the map is missing — which is precisely the situation in
   which confident misuse thrives.

The cafeteria problem is a failure mode of *borrowing*, not of *building*. It is what happens
when a successful notation travels faster than its caveats.

## 7. Map-aware practice

The remedy is not to abandon the diagrams. It is to use them as maps, with the seam declared:

- **Name the import provenance.** For every construct, know the home silo and what the import
  silently carries. The table in Section 3 is the template.
- **Mark the seam.** In any use of a ZX diagram that carries a physical claim — a particle, an
  entropy, a black hole — state where the diagram's guarantees end.
- **Audit compatibility at the boundary.** When imports from different silos meet in one
  diagram, ask whether any published result establishes their mutual consistency. If not, say
  so.
- **Probe beyond the locality.** The map's cone of ignorance is not probed by the map. It is
  probed by experiments and by formal arguments that connect the diagrammatic semantics to
  physical processes — the kinds of arguments that, as of this writing, the literature has not
  yet supplied for the physical imports.

None of this is anti-diagram. It is pro-honesty about what the diagram is.

## 8. Conclusion: where this paper's map ends

The ZX calculus is one of the great successes of modern quantum computing — a rigorous, elegant,
and genuinely useful picture of computation. Its spiders, Pauli webs, and gadgets are maps, and
excellent ones, within their domain. This paper has argued that the physical bearing of those
maps is unestablished, that the literature shows imports from 3+1D particle physics and 1D
thermodynamics being loaded onto the 2D diagrams without compatibility checks, and that this
cafeteria pattern is a general risk of cross-disciplinary borrowing. The argument is evidence-
based where it cites the literature, and plainly argumentative where it generalizes.

It remains to say where the premises end — where this paper's own map stops. Three things are
assumed rather than derived, and the reader should weigh them accordingly. First, the
representational stance: that a formalism can meaningfully be "about" a physical reality at
all, so that questions of physical bearing are well-formed. Second, the epistemic-risk
premise: that unchecked mixing of imports across silos is a real hazard, worth auditing,
rather than a harmless byproduct of interdisciplinary work. Third, the map-territory
distinction itself: that there is a difference between a picture of computation and a picture
of reality, and that the difference matters. The map-territory framing is not original to this
paper: it descends from the general tradition of semantic hygiene associated with Korzybski
and Bateson, and, in this research program, from the author's own locale framework, which
holds that physical statements are true only within a stated scope. These are the
unanalyzable primitives of this paper's frame — the ground it stands on without proving.
Everything else in the paper is either a verified fact about the literature or an argument
built on that ground, and the boundary between the two has been marked throughout.

The satisfaction of a closing diagram is real. So is the discipline of remembering that it
closed a map, not the world.


## Appendix: Post-publication evidence from QPL 2026 (added in version 0.4, 2026-08-19)

*Added in version 0.4 of this record (19 August 2026). arXiv identifiers were verified on the same date.*

Within a day of this paper's publication, the 23rd International Conference on Quantum Physics and Logic (QPL 2026) presented a cluster of nine ZX-calculus contributions. The cluster is direct evidence for the pattern this paper audited: the diagrams continue to be loaded with imports from adjoining disciplines, and the load continues to grow.

| Title | Authors | arXiv | Bearing on the audit |
|---|---|---|---|
| Buildings for Synthesis with Clifford+R | M. Deaconu, N. Gargava, A. R. Kalra, M. Mosca, J. Yard | 2510.11526 | Bruhat-Tits buildings as the geometry of exact gate synthesis; the valuation appears as the smallest denominator exponent |
| Beyond Penrose tensor diagrams with the ZX calculus | Q. Wang, R. D. P. East, R. A. Shaikh, L. Yeh, B. Poór, B. Coecke | 2511.06012 | Spin networks raised to a formal diagrammatic language |
| Holographic codes seen through ZX-calculus | K. H. Wan, H. C. W. Price, Q. Yao | 2601.04467 | Holographic codes as ZX-diagrams, with a new code family on hyperbolic tessellations |
| The Delayed Stabiliser ZX-Calculus | C. Comfort, G. de Felice | 2607.04015 | Finite diagrams for infinite translation-invariant stabiliser processes |
| Efficient Classical Simulation of Low-Rank-Width Quantum Circuits Using ZX-Calculus | F. Kuyanov, A. Kissinger | 2603.06764 | Classical simulation bounded by rank-width, implemented in PyZX |
| Completeness for Fault Equivalence of Clifford ZX Diagrams | M. Rüsch, A. Kissinger, B. Rodatz | 2510.08477 | Rewrites that provably preserve fault-tolerance properties |
| ZX-Flow: A Flexible Criterion for Deterministic Computation with ZX-Diagrams | A. Kissinger, J. van de Wetering | 2603.09580 | A ZX-native criterion for deterministic computation |
| A Three-Way Normal Form for Stabiliser Codes across ZX Diagrams, Circuits, and Tableaus | L. Yeh, J. Huang, A. Kissinger, S. M. Li, J. van de Wetering | none located | An on-the-nose normal form for all stabiliser codes |
| From Fermions to Qubits: A ZX-Calculus Perspective | H. McDowall-Rose, R. A. Shaikh, L. Yeh | 2505.06212 | Fermion-to-qubit mappings made visible as diagram structure |

A further contribution from the same community (G. de Felice, B. Poór, C. Comfort, L. Yeh, M. Kupper, W. Cashman, B. Coecke, arXiv:2601.08389) embeds the calculus in a dataflow framework for linear-optical distributed computing — the clearest sign yet that the diagrams are now treated as executable infrastructure.

The cluster strengthens this paper's computational-domain verdict. The imports audited here — spin networks, holographic entropy, lattice geometries, fault tolerance — all reappear in the 2026 record, now with new machinery: a complete rewrite theory for fault equivalence, an on-the-nose normal form for stabiliser codes, a calculus for infinite translation-invariant codes, and a Bruhat-Tits building theorem for exact gate synthesis. None of the nine performs the compatibility check this paper argued is missing; the fault lines remain where this paper located them.

The open-problem claim admits a stated disconfirmation: a p-adic or ultrametric graphical calculus for quantum codes. On 19 August 2026, an arXiv search pairing "p-adic" with "ZX" returns zero records, and "ultrametric" with "quantum error correction" likewise returns zero. No diagrammatic treatment of p-adic code geometry exists in the public record as of this writing. The nearest machinery stands at the two ends of one bridge: the delayed stabiliser calculus [17], which represents infinite translation-invariant stabiliser processes by finite tableaus, and the tree-traversal synthesis of the Clifford+R work, which runs on a Bruhat-Tits building. A delayed calculus over the p-adic rings used in exact synthesis remains unwritten.

For the practitioner the cluster is concrete in an unusual way. The three-way normal form interconverts any stabiliser tableau with an encoder circuit; the paper states the interconversion algorithms, which are implementable with today's toolchains. The rank-width simulator, implemented in PyZX, makes the classical-simulation boundary of a circuit family computable rather than rhetorical. The fault-equivalence rewrite set is a correctness-by-construction optimisation pass under noise. The delayed calculus makes lattice and convolutional codes finitely representable. Each of these results is implementable today — the rank-width routine as shipped software, the others as algorithms stated in their papers; together they form the substrate of an interactive exhibit of the seam this paper describes, and of the discipline of knowing where a map ends.

The author discussed these contributions with several of their authors during the conference week. Answers to the questions raised here will be folded into the next published version of this paper.

## References

[1] E. Jeandel, S. Perdrix, R. Vilmart, "Completeness of the ZX-Calculus," arXiv:1903.06035 (2019).
[2] M. Backens, "Completeness and the ZX-calculus," arXiv:1602.08954 (2016).
[3] Q. Wang, "Completeness of the ZX-calculus," arXiv:2209.14894 (2022).
[4] K. F. Ng, Q. Wang, "A universal completion of the ZX-calculus," arXiv:1706.09877 (2017).
[5] R. D. P. East, P. Martin-Dussaud, J. van de Wetering, "Spin-networks in the ZX-calculus," arXiv:2111.03114 (2021).
[6] S. Majid, "Quantum and braided ZX calculus," arXiv:2103.07264 (2021).
[7] K. H. Wan, H. C. W. Price, Q. Yao, "Holographic codes seen through ZX-calculus," arXiv:2601.04467 (2026).
[8] N. de Beaudrap, D. Horsman, "The ZX calculus is a language for surface code lattice surgery," arXiv:1704.08670 (2017).
[9] B. Coecke, R. Duncan, "Interacting Quantum Observables: Categorical Algebra and Diagrammatics," arXiv:0906.4725 (2009).
[10] J. van de Wetering, "ZX-calculus for the working quantum computer scientist," arXiv:2012.13966 (2020).
[11] R. Raussendorf, D. E. Browne, H. J. Briegel, "The one-way quantum computer — a non-network model of quantum computation," arXiv:quant-ph/0108118 (2001).
[12] M. Backens, A. Kissinger, "ZH: A Complete Graphical Calculus for Quantum Computations Involving Classical Non-linearity," arXiv:1805.02175 (2018).
[13] V. Vandaele, "Qubit-count optimization using ZX-calculus," arXiv:2407.10171 (2024).
[14] M. Backens, S. Perdrix, Q. Wang, "A Simplified Stabilizer ZX-calculus," arXiv:1602.04744 (2016).
[15] M. Backens, S. Perdrix, Q. Wang, "Towards a Minimal Stabilizer ZX-calculus," arXiv:1709.08903 (2017).
[16] T. Carette, D. Cojocaru, R. Vilmart, "The decohered ZX-calculus," arXiv:2508.04296 (2025).
[17] C. Comfort, G. de Felice, "The Delayed Stabilizer ZX-Calculus," arXiv:2607.04015 (2026).
[18] H. K. Stoltz, "Minimality of the Stabilizer ZX Calculus," arXiv:2606.12383 (2026).
