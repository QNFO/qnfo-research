# Visual Graphs vs Matrices: Epistemic Limits, Cognitive Preference, and the Design of Understandable Computation

*Extended abstract (anonymized for review — no author names, affiliations, or acknowledgements).*

## 1. The observation

The ZX calculus and the matrices of linear algebra denote exactly the same linear maps, yet the quantum computing community has converged, unmistakably, on the pictures. The convergence is visible in the field's canon: the standard working reference is a diagrammatic survey; the recent conference program is dominated by graphical languages, normal forms, and the tools that manipulate them; and the phrase "representation engineering" describes what much of the field actually does. This convergence is usually treated as a matter of taste — a pedagogical preference, or the convenience of a community that grew up on tensor networks. We argue it is a matter of epistemology.

## 2. The claim

A representation determines what a bounded reasoner can see. Diagrams win over matrices for the same reason a map wins over a coordinate table: they chunk, their rewrites are locally auditable, they draw the interfaces that index bookkeeping buries, and they exploit pre-attentive visual features at near-zero cognitive cost. None of these advantages exists in the mathematics — the maps are the same. The preference is a fact about bounded cognition, not about the formalism.

The same boundedness has a second, less noticed consequence. Where comprehension and optimality diverge — minimal gate counts, depths, and widths are computationally hard — the field has not chosen between the human-auditable picture and the machine-optimized one. It has split the difference into a **two-layer structure**: a human-auditable canonical fragment (normal forms, rewrite systems, graphical calculi) and an automated optimizer over it, joined at a declared interface. The optimizer does what it is good at; the canonical fragment keeps the artifact checkable. This structure is not a quirk of ZX. It is what any field does when comprehension and optimality diverge, and it is the pattern this paper identifies, documents, and makes falsifiable.

## 3. Evidence

The evidence base is the 2026 conference program of the quantum logic community, read as a natural experiment:

- **Flow criteria and determinism** — graphical criteria that make the condition for deterministic computation visible, preserved under all Clifford rewrites.
- **On-the-nose normal forms** — one-to-one correspondence between graphical diagrams, encoder circuits, tableaus, and Tanner graphs for stabilizer codes, with efficient interconversion — the canonical fragment, made canonical.
- **Fault-equivalence rewriting** — sound and complete rewrite theories that provably preserve fault-tolerance properties — rewrites that carry their own correctness proof.
- **Exact synthesis by buildings** — gate synthesis reduced to path traversal on a Bruhat-Tits building, with the p-adic valuation appearing as the smallest denominator exponent — optimization made geometrically transparent.
- **Classical simulation by rank-width** — a structural parameter that bounds classical simulation cost, implemented in open software — the optimizer's performance made computable rather than rhetorical.

Every quantitative claim in this paper is computationally verified: the formal equivalence of circuit, diagram, and matrix encodings of the same map (deviation at machine precision), the spider-fusion identities the diagrammatic calculus rests on (golden values), and the visibility table — the same two-qubit map requires sixteen matrix entries against a handful of diagram tokens, and the gap grows as the fourth power of the qubit count against linear growth. The verification scripts and outputs are deposited with the paper.

## 4. Falsifiability

The claim is pre-registered as a hypothesis card with three explicit falsifiers:

1. **A mature field whose standard representation is less comprehensible than a viable alternative** — if such a field exists and persists, the convergence law is false.
2. **Diagrammatic reasoning enabling predictions unavailable through the equivalent matrix formalism** — if diagrams track ontic structure rather than cognitive affordance, the epistemic account is incomplete.
3. **An automated optimizer whose output is more auditable than human design at scale** — if the two-layer split dissolves because the optimizer's layer becomes the legible one, the divergence claim fails.

None of the three holds in the surveyed evidence; all three are checkable in the published record.

## 5. The design principle

The structure licenses the principle the field already practices: we design systems that design algorithms that optimize themselves and other systems, with legibility as a first-class constraint. The human-auditable fragment is not a concession to be automated away; it is the interface at which audit remains possible, and its preservation is a design requirement, not a performance tax.

## 6. Conclusion

Pictures won because bounded minds need them — and the same boundedness explains why the field now organizes itself as a legible core plus an optimizing machine. The law is testable, the evidence is deposited, and the design principle is actionable: when comprehension and optimality diverge, split the difference, and keep the interface where audit remains possible.

## References (selected)

- Y. Wang, R. D. P. East, R. A. Shaikh, L. Yeh, B. Poór, B. Coecke, *Beyond Penrose tensor diagrams with the ZX calculus*, arXiv:2511.06012.
- L. Yeh, J. Huang, A. Kissinger, S. M. Li, J. van de Wetering, *A Three-Way Normal Form for Stabiliser Codes across ZX Diagrams, Circuits, and Tableaus*, QPL 2026.
- M. Rüsch, A. Kissinger, B. Rodatz, *Completeness for Fault Equivalence of Clifford ZX Diagrams*, arXiv:2510.08477.
- M. Deaconu, N. Gargava, A. R. Kalra, M. Mosca, J. Yard, *Buildings for Synthesis with Clifford+R*, arXiv:2510.11526.
- F. Kuyanov, A. Kissinger, *Efficient Classical Simulation of Low-Rank-Width Quantum Circuits Using ZX-Calculus*, arXiv:2603.06764.
- J. H. Larkin, H. A. Simon, *Why a Diagram is (Sometimes) Worth Ten Thousand Words*, Cognitive Science 11 (1987).
- T. R. G. Green, M. Petre, *Usability Analysis of Visual Programming Environments: A 'Cognitive Dimensions' Framework*, JVLC 7 (1996).
- J. van de Wetering, *ZX-calculus for the working quantum computer scientist*, arXiv:2012.13966.
