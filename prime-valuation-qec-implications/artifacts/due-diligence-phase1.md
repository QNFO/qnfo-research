# Due Diligence — Phase 1 (QNFO.RES.006)

**Project:** Implications for Computing and Quantum Error Correction
**WBS:** QNFO.RES.006 | **Slug:** prime-valuation-qec-implications
**Anchor:** QNFO.RES.005 Prime Valuation Depth (DOI 10.5281/zenodo.21918838)
**Date:** 2026-08-13
**Method:** KG (query_graph stats/nodes/query), D1 program_registry, Vectorize (search_papers_enriched), durable memory (recall), arXiv external search.

## 1. QNFO Cross-Reference (internal)

| Source | Entity | Relevance |
|:-------|:-------|:----------|
| D1 program_registry | QNFO.UF — "Ultrametric Foundations", desc: "p-adic valuations classify QEC codes at 83% accuracy" (DOI 10.5281/zenodo.21193487 — canonical 83% source; the D1 registry description row still carried the stale 21046993 at write time; corrected per CMD RED TEAM SUB 2026-08-13) | Anchor for the QEC leg; the 83% claim is the empirical gate (RQ3) |
| KG Paper | `paper:padic-qec-classifier` — "p-Adic QEC Classifier Verification: A Computational Methodology" | Methodological prior for reproducing the 83% claim |
| KG Paper | "Ultrametric Code Spaces: The Bruhat–Tits Tree as a QEC Geometry" (DOI 10.5281/zenodo.21824195) | Geometric substrate for the depth reading |
| KG Paper | "Toward p-adic QEC: The Metric Mismatch Hypothesis" | First explicit p-adic-metric QEC framing (Rowan 2026) |
| KG Paper | "Quantum Error Correction Is a Misnomer: From Metric Translation to Metric Resonance" | Framing prior |
| KG Paper | "How Geometry Creates Memory: The Threshold Principle from First Principles" | Threshold leg prior (hashing-bound note thread) |
| KG Project | `adelic-qec`, `adelic-qec-synthesis`, `toward-p-adic-qec` | Sibling QEC programs |
| KG ResearchQuestion | `rq-07-ostrowski-qec-superiority` — "Can Ostrowski-based QEC beat surface code thresholds?" | Directly overlaps RQ4 |
| KG Finding | `gap-emergence-theorem-unproven` — "GAP [HIGH]: central claim of adelic QEC (fault tolerance necessitates Ostrowski) is unproven" | Prior GAP that this project must not repeat |
| KG Correction | `correction-adelic-representation-theorem` — "Adelic Representation Theorem: CONJECTURE [UNPROVEN]" | Epistemic-hygiene precedent |
| Memory | qudit/p-adic QEC 4-phase roadmap (2026–2032), targeting JPCUB; platforms: molecular qudits, hBN, SiC | Program context |
| GitHub | `res/paper/ringbauer-qudit-due-diligence` (qnfo-research), `ump/paper/qwave-qudit-advantage` (ultrametric-physics) | Prior qudit work; R1 novelty risk source |

KG stats at due-diligence time: 8,270 nodes / 8,410 edges; 1,619 Paper nodes; 148 Project nodes.

## 2. External Literature (arXiv, 2026-08-13)

### Qudit QEC — established, rapidly moving external field
- Foliated QEC for Qudits (2607.13784, 2026) — prime-dimensional qudit foliation; qudit toric thresholds comparable to qubit version.
- QEC of Qudits Beyond Break-even (2409.15065, Yale GKP qutrit/ququart, gain 1.82/1.87).
- Qudit QEC codes from SU(d) irreps (2410.02407) — prime/odd d constructions.
- Qudit LDPC codes (2510.06495) — bivariate bicycle, hypergraph product, SHYPS, fiber bundles generalized to qudits.
- Review of Galois Qudits (2605.18981) — **direct external statement of "tensor-product structure is not intrinsic": a Galois qudit of dimension q=2^s is exactly s qubits, in Hilbert space, Pauli group, and Clifford hierarchy.**
- Qudit stabiliser codes for Z_N LGT with matter (2602.20661) — prime-dimension N.
- Qudit stabilizer learning (2607.15559), dynamical decoupling with SU(d) (2604.05871), spin-qudit QEC for practical hardware (2503.12142).

### p-adic / valuation QEC — external field essentially ABSENT
- No external hit for p-adic-valuation-based classification of QEC codes. Adjacent only: p-adic/adelic QM (Dragovich 2003/2006), p-adic equiangular lines + van Lint–Seidel bound (2408.00810, K. Mahesh Krishna).
- Conclusion: the p-adic-depth QEC framing is QNFO-internal; the valuation-as-depth vocabulary has no known external competitor. This is the novelty surface, and simultaneously a [CONFIRMATION-BIAS-RISK] flag: nearly all supporting evidence is internal.

## 3. Gap Analysis vs Locked Core Claim

**TERRITORY claim** (v_2(dim H) = n counts qubit tensor factors; v_p(dim H) counts p-dimensional factors): ESTABLISHED, inherited from RES.005. External literature corroborates the algebraic content independently (Galois qudit review is effectively a statement of this for q=2^s). — no gap.

**BRIDGE claim** ([[n,k,d]] ↔ branch-depth reading): PARTIALLY ANTICIPATED externally. Standard qudit stabilizer theory already parameterizes codes by physical/logical dimensions; the mapping n=v_2(dim H), k=v_2(dim H_L), d=branch-crossing weight is at risk of being a PURE RELABELING. The claim's own falsifiability condition is the correct gate: it survives ONLY if it yields (a) a new invariant, (b) a new classification of code families, or (c) a new bound. Gap: none of these is yet derived. — ACTION: P4 must target RQ2/RQ5 (valuation-based taxonomy of CSS/surface/toric/colour/subsystem codes) FIRST; the mapping alone is not publishable.

**EXTENSION claim** (classification invariant connecting to QNFO.UF 83%; no-cloning sets fundamental QEC limits): HIGHEST NOVELTY POTENTIAL. Two independent risks: (i) the UF 83% result is internal and unverified externally — RQ3 reproduction on a fresh test set is the make-or-break empirical gate; (ii) `gap-emergence-theorem-unproven` records a prior QNFO failure mode (unproven "necessitates Ostrowski" claim) that this project must explicitly avoid. — ACTION: P4 must reproduce-or-refute the 83% claim with a written protocol BEFORE any classification-invariant claim.

**Computing leg** (RQ1, RQ6 — path-tracing through multiplicative branch structure; valuation-based invariant of reversible circuits): LEAST DEVELOPED, no internal or external prior found that uses valuation-depth for circuit invariants. Highest-risk/highest-reward open target. — ACTION: keep as speculative; gate on P2 literature check of circuit-complexity invariants.

## 4. Novelty Verdict

The project is novel in the **vocabulary and framing** (valuation-as-depth applied to QC/QEC), NOT in the algebraic substrate (qudit stabilizer theory is external and mature). The publishable contribution must therefore be one of:
1. a verified valuation-based taxonomy/invariant of code families (RQ5), or
2. a reproduced-and-clarified statement of the UF 83% classification (RQ3), or
3. a new bound relating branch depth to achievable code distance (RQ4).

A paper that only re-derives standard qudit stabilizer theory in new words fails the bridge claim's own falsifiability condition and must not be published.

## 5. Phase 1 Consilience Gate (KIF-29 — abbreviated, scope: single-project)

- **Domains selected:** Quantum information (stabilizer codes), Number theory (valuation/Ostrowski), Category theory (monoidal-not-Cartesian), Computation (circuit model). Rationale: each domain appears in the locked core claim's derivation chain.
- **Minimum viable finding:** the multiplicative-branch structure (tensor product multiplies dimension; valuation adds depth) is the shared invariant across the four domains — v_p(dim H) = depth is well-defined in all four translations. [Satisfied]
- **Silo cost table:** Number-theory↔QI silo is the one the anchor paper already bridged (RES.005); the QEC↔valuation silo is bridged only by the internal 83% result (unverified externally) — this is the highest-cost silo and the priority P4 target.
- **Synthesis:** one meta-principle — "depth, not size" (valuation measures branch depth; QEC measures protected depth). Frontier question: does a valuation-based invariant of QEC code families exist that is NOT a relabeling of stabilizer parameters?

## 6. Evidence Files

- arXiv qudit QEC search: 15 results (2024–2026), saved this session.
- arXiv p-adic QEC search: 15 results, all irrelevant to valuation-based QEC (saved for provenance).
- KG cross-reference: nodes/edges queries this session (graph-api.qnfo.org/query).
- D1 program_registry rows: RES.001–RES.006 (portfolio-state).

## 7. Post-Audit Provenance Note (direct red-team, 2026-08-13)

SOFT finding: the UF anchor record (DOI 10.5281/zenodo.21046993) is titled
"Ultrametric Quantum Computing: Tree-Topology Error Correction" — the phrase
"p-adic valuations classify QEC codes at 83% accuracy" is the QNFO.UF program
DESCRIPTION in D1 program_registry, not the record title. P4/RQ3 must pin the
exact section/table inside the record where the 83% number appears before any
reproduction attempt.

## 8. Companion Report (concurrent session)

This report complements `due-diligence.md` (commit 021f07f, concurrent session),
which carries the full QNFO-internal DOI corpus for p-adic QEC and p-adic
computing. Split of labor: due-diligence.md = internal corpus cross-reference;
due-diligence-phase1.md = external arXiv novelty check + gap analysis + consilience
gate summary. RQ3 provenance note: the 83% claim is attributed to DOI
10.5281/zenodo.21046993 in the registry but to 10.5281/zenodo.21193487 in
due-diligence.md — see red-team-phase1.md, SOFT finding (open).
