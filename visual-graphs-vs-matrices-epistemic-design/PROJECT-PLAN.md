# PROJECT-PLAN — QNFO.RES.019: Visual Graphs vs Matrices: Epistemic Limits, Cognitive Preference, and the Design of Understandable Computation

WBS: **QNFO.RES.019** · Branch: `res/paper/visual-graphs-vs-matrices-epistemic-design`
Seed: vault `_26232092415` (2026-08-20) + thesis brief `_visual-graphs-vs-matrices-epistemic-design-2026-08-20.md` (status: active-thesis)

## 1. Core claim (LOCKED, P6)

Mature technical fields converge on the maximally comprehensible representation for humans —
diagrams over mathematically equivalent matrices — because the preference is a fact about
bounded cognition (chunking, locality of rewriting, visible interfaces), not about the
mathematics. Optimization is outsourced to machines exactly where comprehension and optimality
diverge (NP-hard minimization), producing a two-layer structure: a human-auditable canonical
fragment plus an automated optimizer over it. The design principle that follows: we design
systems that design algorithms that optimize themselves and other systems, with legibility as
a first-class constraint.

**Premise-depth disclosure:** premises are (a) the ZX calculus's completeness theorems
(imported, established); (b) cognitive-science results on diagrammatic reasoning (Larkin &
Simon 1987; the cognitive-dimensions-of-notations literature — Phase 1 verifies); (c) the
observed convergence at QPL 2026 (the canonical text is *Picturing Quantum Software*;
representation engineering is the field's main activity). The argument from those premises to
convergence plus the two-layer structure is this paper's contribution and is marked as such.
Depth is about two steps. The map ends at the interface: whether diagrammatic preference
tracks ontic structure is a falsifiability condition, not an assumption.

## 2. Milestones (P0–P9 with gate criteria)

| Phase | Gate |
|---|---|
| P0 | WBS claim + branch + core-claim lock + UIA (this commit) |
| P1 | Due diligence: full-corpus sweep (3+ formulations, limit ≥20), cross-system ID validation, ≥2 adjacent WBS domains (SLB/CFE/UMP/PLT), external verification (Larkin & Simon; cognitive dimensions; any prior graphs-vs-matrices theses), gap analysis + SO-WHAT + premise-depth in prose |
| P2–P3 | Literature assembly + citation audit (every entry verified live) |
| P4 | Deep research: the two-layer theorem sketch; QPL evidence table; the tie-in synthesis (§3) |
| P5 | Publication gates: PANDOC-SAFE, BP, mojibake, language, FIGURES-COMPREHENSION-1 (figures planned: the interface diagram; the cluster map), PRACTITIONER-RELEVANCE-1, SO-WHAT in prose |
| P6 | Deploy: D1/KG/Vectorize |
| P7 | Dissemination (§5; email outreach approval-gated) |
| P8 | Distribute: R2 mirror + tags |
| P9 | Extension: tie-ins, re-audits |

## 3. Tie-in scope (user directive 2026-08-20, note _26232101434)

Connect to spin statistics, standard-model/condensed-matter unification, information theory,
statistics, thermodynamics, QND quantum mechanics/quantum information, the self-reference of
e, and patterns of distinction (re-entry). Tie-in vehicles: the adelic Shannon record
(10.5281/zenodo.22024240) and the exchange-phase thread (RES.010/RES.011, the
spin-statistics-distinction branch). P1/P4 scope: the statistics axis — where representation
choice meets the statistics/thermodynamics/information seam; graphs as the interface that
makes the exchange phase visible (cf. the fermion-to-qubit parity-string structures, QPL 2026
paper 104, already in the RES.015 appendix).

## 4. Risk register

| Risk | Mitigation |
|---|---|
| Claim pre-empted (cognitive-diagrams literature already argues it) | P1 sweep; reframe as synthesis with citation |
| H-VISUAL falsified (diagrams track ontic structure) | Scope to the ergonomics account only (already a stated falsifier) |
| Over-claiming convergence from one field | P1 breadth check (Feynman diagrams, chemistry, LoF injunction calculus) |
| WBS collision | Atomic claim done (registry row verified) |

## 5. Dissemination strategy (preliminary; Phase 7 executes; user directive 2026-08-20, note _26232125031)

- **Conferences (the thesis is talk-shaped):** QIP27 Singapore (abstract deadline
  2026-10-05); IS4SI Summit 2027; LoF28 Cambridge (2028-08-07..11); DICE2026 Castiglioncello
  (2026-10-05..09); QPL 2027.
- **Essays:** Aeon / Noema (whole-person format; outranks extra conference slots when energy
  is scarce).
- **Records + amplification:** Zenodo record (concept-DOI chain) + community inclusion
  requests (advancedtheoreticalphysicsandmathematics, fbt-framework); papers.qnfo.org; the
  96-account social registry (social-media-management skill).
- **Journalists/influencers:** approval-gated outreach (no autonomous email sends — standing
  mandate).

## 6. H-VISUAL card (pre-registered 2026-08-20, vault _visual-graphs-vs-matrices-epistemic-design-2026-08-20.md)

- **Claim:** convergence on the maximally comprehensible representation; optimization
  outsourced where comprehension and optimality diverge.
- **Falsifiers:** (a) a mature field whose standard representation is LESS comprehensible than
  viable alternatives; (b) diagrammatic reasoning enabling predictions unavailable via
  matrices (ontic tracking); (c) an optimizer whose output is MORE auditable than human design
  at scale.
- **Testable prediction:** fields with hard optimization subproblems develop the two-layer
  structure (human-auditable normal forms + automated optimizer). QPL Day 4 exhibits: Yeh
  normal forms + synthesis/T-count optimizers.
- **Surprisal:** HIGH (standard accounts are ontic or computational; a cognitive-ergonomics
  account is rarely stated).

## 7. QNFO program mapping (thesis brief §5)

- **SLB:** Laws of Form = the original visual calculus; ZX = its industrialized descendant —
  external validation of the SLB program.
- **PLT:** the platform mandate IS meta-design (systems that design algorithms that optimize
  themselves and other systems).
- **CFE:** representation choice is the engineering act; paradigm-engineering = choosing the
  lens.
- **UMP:** trees are the most visualizable geometry (Bruhat–Tits tree); visual-tree reasoning
  is the p-adic native mode.
- **RES:** if the invariant across formalisms is the human interface, the invariant is
  cognitive, not ontic — consilience via ergonomics.

## 8. Open questions (thesis brief §7)

- At what scale does audit break (when does a synthesized circuit stop being checkable)?
- Does the cognitive optimum track the *interface* (compositional structure) rather than the
  objects?
- Is the visual preference species-specific or universal to bounded reasoners?
