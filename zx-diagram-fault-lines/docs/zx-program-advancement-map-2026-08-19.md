# ZX at QPL 2026 — Program-Advancement Map for QNFO/QWAV (P9 extension of QNFO.RES.015)

Date: 2026-08-19. Scope: nine ZX-calculus papers from QPL 2026 (qplconference.org submissions),
mapped onto the QNFO/QWAV program portfolio. Existing project: QNFO.RES.015
(zx-diagram-fault-lines, DOI 10.5281/zenodo.21992118 / concept 21991895); Phase 0 scaffolding
skipped per the research skill (net-new only).

## 1. The core claim (locked for this cycle)

The QPL 2026 ZX cluster gives each major QNFO/QWAV program at least one concrete, verifiable
advancement path, and the paths are PARTIALLY OCCUPIED: two of the nine papers already sit on
QNFO-shaped ground (Bruhat-Tits buildings for gate synthesis; holographic/translation-invariant
codes), while the QNFO-distinctive seams — p-adic/ultrametric quantum error correction, the
exchange phase as diagram structure, and energy-per-solution as the invariant of fault-equivalent
rewriting — remain unoccupied by any paper in the cluster. Novelty is bounded by that occupancy:
the claim is not "ZX discovers QNFO" but "QNFO contributes where the cluster stops."

Premise-depth disclosure: the map below imports, as established, (a) the soundness/completeness
theorems of the ZX calculi as stated by their authors, (b) the QNFO corpus records cited, and (c)
the RES.015 fault-line audit's conclusion that the diagrams are maps, not territory. The argument
from those premises to "advancement path" is mine and is marked. The map itself is a map; where it
ends, the corresponding territory work (proofs, benchmarks, decoders) begins.

## 2. The nine papers, one line each

- **57 (Kuyanov-Kissinger, 2603.06764):** classical simulation of ZX-diagrams scales with
  *rank-width*; Õ(4^R); matches the 2^n state-vector and 2^{t/2} stabiliser baselines; in PyZX;
  orders-of-magnitude FLOP reductions vs Quimb.
- **56 (Rüsch-Kissinger-Rodatz, 2510.08477):** sound + complete rewrite set for *fault
  equivalence* of Clifford ZX diagrams — rewrites that provably preserve fault-tolerance
  properties; unique normal form under Pauli noise.
- **42 (Wan-Price-Yao, 2601.04467v2):** pentagon holographic code as one ZX-diagram; Pauli webs
  extract stabilisers/logicals/parity checks; new {4,5} dual-tessellation family; X-gauge-fixing
  + BP+OSD reaches near-optimal erasure threshold ≈1/2; toy black holes via Rényi entropy.
- **179 (Comfort-de Felice):** the *delay* generator turns finite ZX diagrams into compact
  descriptions of translation-invariant (infinite) stabiliser processes: convolutional codes,
  lattice codes, spin chains; polynomial-fraction semantics; finite generating tableaus for
  infinite stabiliser groups.
- **98 (Wang-East-Shaikh-Yeh-Poór-Coecke, 2511.06012):** Spin-ZX — Penrose/Yutsis spin networks
  embedded in mixed-dimensional ZX; symmetriser rewrite library; permutational QC amplitudes,
  SU(2)-equivariant barren plateaus, AKLT states, LQG volume-operator eigenvalues.
- **147 (Kissinger-van de Wetering, 2603.09580):** ZX-flow — a ZX-native determinism criterion
  via Pauli semiwebs, preserved by all Clifford rewrites; extracts measurement patterns or
  Clifford isometries + Pauli exponentials.
- **187 (Yeh-Huang-Kissinger-Meng Li-van de Wetering):** an *on-the-nose* normal form for ALL
  stabiliser codes (not just CSS, not up to local Cliffords); one-to-one dictionary between
  ZX-diagrams, encoder circuits, tableaus, and generalised Tanner graphs, with efficient
  interconversion algorithms.
- **104 (McDowall-Rose-Shaikh-Yeh, 2505.06212):** ZX as the common intermediate language for
  fermion-to-qubit mappings; ternary-tree mappings ARE linear encodings (Theorem 1); parity
  strings and locality trade-offs made visible as diagram structure.
- **174 (Deaconu-Gargava-Kalra-Mosca-Yard, 2510.11526):** qutrit Clifford+R exact synthesis; the
  Bruhat-Tits building of U3(Z[χ^-1]) is a TREE; synthesis = path traversal on the tree;
  arithmeticity re-proven; the p-adic (π-adic) valuation IS the "smallest denominator exponent".

## 3. Program-advancement map

| Program | Advancing paper(s) | The seam | What QNFO contributes (unoccupied) |
|---|---|---|---|
| **UMP** ultrametric physics | 174, 42, 179 | Bruhat-Tits buildings/trees as the geometry of *exact gate synthesis* (174); hyperbolic tessellation codes (42); translation-invariant codes (179) | 174 gives the valuation-theoretic quantity ("denominator exponent") an engineering home — QNFO's BT-tree QEC geometry (qec-darwinism-ultrametric) and ballistic-transport picture can now be *tested* against a working synthesis algorithm: path traversal on the tree. The unoccupied ground: p-adic/ultrametric QEC codes — neither 42 (hyperbolic, Archimedean-continuous) nor 179 (translation-invariant, polynomial) uses a p-adic metric; QNFO's ultrametric QEC is the missing synthesis of the two. |
| **SLB** laws of form | 98, 104, 187 | Spin-ZX's symmetriser rewrite library (projector/sliding/invariance identities) is a distinction-calculus-flavoured algebra; 187's four-way normal-form dictionary is "form is invariant" made algorithmic; 104 makes the exchange phase visible as parity-string structure | RES.010 derived R = e^(2πis) as a logical scalar from the re-entrant calculus; 104's fermion mappings encode exactly that exchange structure in diagrams — a concrete bridge from boundary algebra to quantum compilers. Unoccupied: nobody in the cluster connects diagram rewrite completeness to the laws of calling/crossing; QNFO's reentrant-distinctions + syntactic-token-calculus are the only extant candidates. |
| **INM** infomatics | 56, 147, 187, 57 | Fault equivalence (56) = noise-as-information; normal forms (187) = canonical representation; ZX-flow (147) = determinism as graph property; rank-width (57) = the honest complexity metric | QNFO's "energy per solution" (locale-framework-quantum-applications, 21991270) is exactly the quantity fault-equivalent rewrites conserve: a QNFO-stated invariant can be *tested* against a complete rewrite theory. Unoccupied: no cluster paper quantifies energy cost per rewrite. |
| **CFE** forecasting | 57, 56 | The classical-simulability frontier stated in rank-width terms is the falsification instrument QNFO's advantage claims (JPCUB, Qudit Advantage, structural-vs-driven coherence) have been missing | Every QNFO advantage claim should be re-stated with a rank-width/t-count budget; 57's PyZX implementation makes the boundary computable, not rhetorical. |
| **DEM** demos | 57, 187, 98, 174 | All four have runnable substrates (PyZX; interconversion algorithms; symmetriser library; tree-traversal synthesis) | The deferred "ZX bridge demo" flagship is now directly buildable via qwav-demo-kit: (a) BT-tree path synthesis for Clifford+R qutrits, (b) the {4,5} holographic code family with BP+OSD decoding, (c) rank-width contraction benchmarks, (d) Spin-ZX symmetriser rewrites. |
| **RES** archive | all nine | RES.015's P1 external record (lattice surgery 1704.08670; holography 2601.04467; LQG spin networks 2111.03114; quantum groups 2103.07264) now has 2026 QPL continuations — post-publication evidence for the fault-line audit | Next deliverable: RES.015 v0.2 (or companion) with the nine-paper evidence table; plus the D1 identifier re-point (21991896 → 21992118) flagged in the evidence file. |

## 4. Gap analysis (what the cluster does NOT cover)

1. **Ultrametric/p-adic QEC** — no ZX treatment exists. The user's own QPL-week search confirmed
   "ultrametric QEC" is not standard terminology in the field. This is QNFO's single cleanest
   opening: qec-darwinism-ultrametric + the delayed-stabiliser machinery (179) + hyperbolic codes
   (42) are three legs of a four-leg table; the p-adic leg is QNFO's to build.
2. **Exchange phase as diagram structure** — 104 makes parity strings visual but does not connect
   them to spin-statistics logic; the RES.010/RES.012 thread (exchange scalar, parastatistics
   boundary) has no ZX counterpart.
3. **Energy per rewrite** — fault equivalence (56) proves rewrites preserve noise-tolerance
   properties, but no cluster paper attaches an energy cost to a rewrite sequence; QNFO's
   energy-budget discipline is the natural invariant to add.
4. **Map-territory discipline inside the cluster** — RES.015's audit applies with full force to
   papers 42 and 98 (holographic and LQG imports on a 2-dimensional drawing plane); the QPL
   versions contain no compatibility check of the kind RES.015 demands. This is a citation-ready
   finding, not a defect of the papers' mathematics.

## 5. Universal Ignorance Audit (condensed 15-question pass, ZENODO-INQUIRY-1)

Target: the core claim in §1. Answers written; no resolution during the pass.

1. **What is the claim about?** Nine QPL 2026 ZX papers → QNFO/QWAV program advancement paths.
2. **What do I know?** Primary PDFs read (all nine, full text extracted); RES.015 body read; corpus swept (3 formulations); arXiv verified for 7/9; DataCite live for the RES.015 DOI set.
3. **What do I not know?** Whether the two unverified papers (179, 187) have arXiv versions or prior art I have not seen; whether decoder numbers (42) reproduce outside the authors' simulator; whether Mosca/Yard/Deaconu consider the BT-tree synthesis complete for all of PU(3).
4. **What am I assuming?** That QNFO's valuation-theoretic vocabulary (denominator exponents, BT trees) maps one-to-one onto the number theory 174 actually uses. It does for the π-adic valuation, but I have not checked the QNFO-specific claims in qec-darwinism-ultrametric against 174's definitions — pending.
5. **Falsifiability (Q5):** the claim is false in a world where (a) a p-adic ZX calculus already exists in the literature, or (b) the QPL cluster's own authors close seams 1-4 in their final versions. Both are checkable within 90 days by re-sweeping the corpus and the arXiv listings.
6. **Sources of ignorance — literature:** arXiv searches were title/author-scoped; a full-text sweep for "p-adic ZX" and "ultrametric ZX" is not done. Rank: medium.
7. **Sources of ignorance — scale:** the delayed-stabiliser semantics (179) is stated for odd-prime dimensions; whether QNFO's p=2 lattice-code thread (Golay/Leech/Mahler) transfers is unchecked. Rank: medium.
8. **Sources of ignorance — instruments:** all decoder/benchmark numbers are simulator outputs; no hardware run exists. Rank: low (not needed for the map claim).
9. **Sources of ignorance — people:** the in-room opportunity (Coecke Wed 10:15; Mosca/Yard Thu 15:45; Shaikh/Yeh Wed 16:15) is itself the remedy; unanswered questions = the five scripted ones from the attendance plan, now sharpened in §7.
10. **Epistemic depth:** the map's premises end at the imported completeness theorems + RES.015's map-territory conclusion. Depth = 2 steps. Claim bounded accordingly.
11. **Blind spot — self-confirmation:** the map was built to find seams; the audit must force the null. The null is: "the cluster already covers QNFO's ground, leaving nothing." Two papers (174, 42) partially confirm the null on their home turf — which is exactly why the claim is bounded to the four unoccupied seams.
12. **Blind spot — adjacent literature:** quantum convolutional codes have a mature non-ZX literature (Ollivier-Tillich etc.); the delayed-stabiliser calculus is new, but its *targets* are not. The gap is the p-adic metric, not the codes.
13. **What would disconfirm each program row:** UMP row dies if a p-adic ZX calculus appears; SLB row dies if someone maps LoF to diagram rewriting first (currently no candidate); INM row dies if a fault-equivalence energy bound appears; CFE row dies if rank-width simulability is absorbed into standard benchmark suites without QNFO involvement.
14. **Silence (allow after Q14):** what the audit does not know: whether the user's energy budget even permits a new ZX research line this quarter. That is the user's call, not the audit's.
15. **Q15 — what audits this audit?** The RES.015 fault-line audit itself: this map re-uses its conclusion as a premise (marked in §1). If RES.015's map-territory conclusion were wrong, this map's premise-depth disclosure would be wrong with it. Next audit: re-run RES.015's fault-line check on this very document after the conference.

## 6. SO-WHAT (why a reader should care)

QPL 2026 is the week the two communities are within handshake distance: the ZX cluster is
actively importing the exact structures QNFO has spent its corpus developing (Bruhat-Tits
trees, valuations as denominator exponents, spin networks, exchange phases, energy budgets) —
and the cluster stops precisely where QNFO's four unoccupied seams begin. A reader of the QPL
programme cannot see those seams; this map is the only document in either community that names
them. The concrete, date-stamped payoff: the QNFO principal is in the room with the authors this
week, which converts "gap analysis" into "questions to ask the people who own the territory."

## 7. Practitioner section (PRACTITIONER-RELEVANCE-1)

What a practitioner can DO with this, per program row, in engineering language:

- **Run the boundary, don't argue it:** 57's algorithm ships in PyZX. A practitioner can take any
  QNFO circuit family, compute its rank-width, and get a falsifiable statement of where classical
  simulation is feasible — a spec-sheet number for advantage claims, replaceable by no argument.
- **Certify rewrites under noise:** 56's fault-equivalence rules are a correctness-by-construction
  optimisation pass. A compiler engineer can adopt the rule set and stop worrying whether a
  rewrite silently breaks fault tolerance (hook errors).
- **Design codes in one language, export to three:** 187's interconversion algorithms (ZX ↔
  circuit ↔ tableau ↔ Tanner graph) are a code-design SDK; input a tableau, get an encoder
  circuit, and vice versa.
- **Exact synthesis on a tree:** 174's result means Clifford+R qutrit synthesis is a shortest-path
  problem on a known tree; the implementation path is concrete (lattice-chain models, residue
  fields F3) and demoable in a browser canvas.
- **The QNFO product embodiment:** the deferred ZX-bridge demo (qwav-demo-kit pipeline) with
  four tabs — BT-tree synthesis, holographic-code decoding, rank-width benchmarking, Spin-ZX
  symmetriser playground. Each tab is backed by an arXiv-verified paper; each control wired to
  real computation (no dead buttons).
- **Conditional-truth pairing:** every claim above holds only within its paper's stated domain
  (qubit Clifford for 56; qutrit Clifford+R for 174; stabiliser codes for 187; graph-like
  ZX-diagrams for 57). The domains are stated in the papers and repeated here rather than
  silently generalised.

## 8. In-room follow-ups (QPL week, sharpened)

- **Coecke / Spin-ZX (Wed 10:15):** does the symmetriser library have a completeness statement,
  and is the mixed-dimensional embedding's completeness inherited or re-proven for the spin
  fragment? (Bearings on the SLB row.)
- **Shaikh / Yeh / McDowall-Rose (Wed 16:15):** is the parity-string structure of 104 connected
  to the exchange phase as a logical scalar, or treated purely as a compilation artifact?
  (Bearings on the RES.010 bridge.)
- **Mosca / Yard / Deaconu (Thu 15:45):** the BT-building being a tree is proven for U3(Z[χ^-1]);
  does the same tree-lattice picture extend to the QEC side (stabiliser codes over the same
  ring), and would a p-adic metric on code words preserve the decoder thresholds of the
  holographic family? (Bearings on the UMP row — the single most valuable question of the week.)

## 9. Next-cycle items (queue)

1. D1 `identifier` re-point for zx-diagram-fault-lines: 21991896 → 21992118 (or concept 21991895). Data-layer fix, readback-verified.
2. Full-text sweep for "p-adic ZX" / "ultrametric ZX" / "valuations in gate synthesis" (ignorance row 6).
3. RES.015 v0.2 or companion paper: nine-paper evidence table + the four unoccupied seams + in-room answers.
4. ZX-bridge demo: Phase DEM-E0-T01 per qwav-demo-kit (four tabs, arXiv-verified backends).
5. Re-sweep 90 days out (falsifiability check, §5.5): does any cluster author close seam 1-4?
