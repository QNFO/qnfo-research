# Import Provenance, Compatibility Audit, and Seam Catalog — QNFO.RES.015

WBS: `[QNFO.RES.015.P2]` · Branch: res/paper/zx-diagram-fault-lines · 2026-08-18
Evidence: `artifacts/external-search/corpus-sweep-2026-08-18.md` (arXiv records verified 2026-08-18)

---

## 1. Import-provenance tables

### 1.1 Spiders (ZX Z- and X-spiders)

| Column | Content |
|---|---|
| **Construct** | Green (Z) and red (X) spiders — generators of the ZX calculus: nodes with `n` inputs / `m` outputs carrying a phase `α`. |
| **Origin silo** | Categorical quantum mechanics / diagrammatic algebra (2D). Frobenius algebras as "interacting quantum observables" (Coecke–Duncan, 2008/2011). |
| **Canonical source** | Coecke & Duncan, "Interacting quantum observables: categorical algebra and diagrammatics" (New J. Phys. 13, 043016, 2011; arXiv:0906.4725). |
| **What it imports** | Dagger-special Frobenius algebra structure (Z-spider = copy/merge of Z-basis; X-spider = copy/merge of X-basis); fusion rule; bialgebra/complementarity law (the "π-commutation" at the heart of the calculus). |
| **What it silently carries** | The 2D diagrammatic topology of wires/planes; the completeness results (Backens; Jeandel–Perdrix–Vilmart; Wang) prove the *algebra* captures matrix equalities — nothing about spacetime. |
| **Seam (map ends)** | A spider is a *map* of a measurement basis, not a particle, not a worldline. Reading a spider as a physical process in 3+1D is map–territory confusion. The completeness theorems are about the map's expressive power, not the territory's shape. |
| **Cone of ignorance** | Whether any 3+1D physical process corresponds to the diagrammatic topology (the "2D tube" assumption from the seed note) is *unprobed by the calculus itself*. |

### 1.2 Pauli webs

| Column | Content |
|---|---|
| **Construct** | Tracked families of Pauli (X/Z) operators through a ZX diagram — used to read off stabilizer structure, logical operators, and error behavior of quantum-error-correcting codes. |
| **Origin silo** | Stabilizer formalism / quantum error correction (lattice surgery; surface codes). |
| **Canonical sources** | de Beaudrap & Horsman, "The ZX calculus is a language for surface code lattice surgery" (arXiv:1704.08670 — red/green spiders match rough/smooth merges); Wan, Price & Yao, "Holographic codes seen through ZX-calculus" (arXiv:2601.04467 — Pauli webs for holographic-code stabilizers, Rényi entropy, black-hole/wormhole toy models). |
| **What it imports** | Stabilizer group structure; code distance and error-correction semantics; lattice-surgery rough/smooth merge operations (2+1D: a 2D code over time); in the holographic application: AdS/CFT-entangled boundary structure, Rényi entropy, toy black holes. |
| **What it silently carries** | The QEC claims are *about the map of the code*, not about spacetime. The holographic loading (2601.04467) imports a 3+1D-ish gravity vocabulary (entropy, wormholes) into a 2D diagrammatic calculus. |
| **Seam (map ends)** | A Pauli web is a bookkeeping device for stabilizer structure. When a web is read as "the spacetime structure of the code" or as evidence about black holes, the 1D-entropy/3+1D-gravity imports are being mixed into a 2D map without a compatibility check. |
| **Cone of ignorance** | Whether the holographic dictionary (bulk-boundary correspondence) survives being expressed in ZX diagrams at all is an *import* from AdS/CFT — itself unprobed within the ZX setting. |

### 1.3 Gadgets

| Column | Content |
|---|---|
| **Construct** | Diagrammatic encodings of non-Clifford (typically T/H) operations as small graph gadgets — the "gadgetization of Hadamard gates"; phase gadgets in ZH-calculus. |
| **Origin silo** | Measurement-based quantum computation (MBQC) and circuit optimization / T-count reduction (compilation layer). |
| **Canonical sources** | Vandaele, "Qubit-count optimization using ZX-calculus" (arXiv:2407.10171 — gadgetization of Hadamard gates, Pauli Fusion, lattice surgery); Backens & Kissinger, "ZH: A Complete Graphical Calculus" (arXiv:1805.02175, phase gadgets); rooted in Raussendorf, Browne, and Briegel one-way quantum computer (arXiv:quant-ph/0108118). |
| **What it imports** | Graph-state resource structure; measurement-pattern semantics (MBQC); the T-count/optimization machinery of the compilation silo. |
| **What it silently carries** | The MBQC equivalence claims — a gadget is *a map of a computation*, validated by soundness of the diagrammatic rewrite system, not by any physical realization. |
| **Seam (map ends)** | A gadget is a diagrammatic encoding of a gate. Reading a gadget as a hardware component ("this is how the T gate is built") imports MBQC physicalization assumptions that the diagram itself does not carry. |
| **Cone of ignorance** | Whether the resource states that make gadgets efficient are physically preparable in a scalable way is a separate (largely open) question the diagrams do not probe. |

## 2. Pairwise compatibility audit

| Import pair | Domains | Compatibility status | Verdict |
|---|---|---|---|
| Spiders ↔ Pauli webs | 2D categorical QM ↔ 2+1D stabilizer QEC | **Coherent within the computational domain** — de Beaudrap–Horsman (1704.08670) proves the spider axioms match lattice-surgery operations exactly; Backens completeness for stabilizer ZX is the shared algebraic foundation. | Compatible *as maps* of circuits/codes. |
| Spiders ↔ Gadgets | 2D categorical QM ↔ MBQC/compilation | **Coherent within the computational domain** — gadgetization preserves circuit semantics (Vandaele 2407.10171); ZH phase gadgets are provably equivalent to ZX diagrams. | Compatible *as maps* of computations. |
| Pauli webs ↔ Gadgets | Stabilizer QEC ↔ MBQC | **Coherent within the computational domain** — both are compile-layer tools on the same stabilizer structure (Pauli Fusion model covers lattice surgery per Vandaele). | Compatible *as maps*. |
| 2D diagrammatic core ↔ 3+1D particle-physics imports (spin networks, quantum groups) | Diagrammatic calculus ↔ LQG / quantum groups | **UNCHECKED cross-silo mixing** — East–Martin-Dussaud–Van de Wetering (2111.03114) embed SU(2) spin networks into ZXH; Majid (2103.07264) builds braided ZX on u_q(sl_2). Each ships its own soundness story; **no published compatibility audit** of the mixed imports was found in the Phase-1 sweep. | **The fault line.** |
| 2D diagrammatic core ↔ 1D thermodynamic/entropic imports (Rényi entropy, holography) | Diagrammatic calculus ↔ AdS/CFT / statistical mechanics | **UNCHECKED cross-silo mixing** — Wan–Price–Yao (2601.04467) compute Rényi entropy and black-hole toy models via Pauli webs in ZX diagrams. The 1D-entropy vocabulary is imported into a 2D map with no dimensional-compatibility argument. | **The fault line.** |
| 3+1D imports ↔ 1D imports (gravity ↔ entropy) | LQG/QG ↔ thermodynamics | Both arrive *inside the same diagrams* (2111.03114 + 2601.04467) with no demonstrated mutual consistency — the seed note's exact scenario ("imports from 3D+1 particle physics and 1D thermodynamics/entropy"). | **Unchecked by construction.** |

**Bottom line of the audit:** within the computational domain (circuits, codes, compilation) the
imports are demonstrably coherent — this is where the map is doing its job. The fault lines are
exactly where the *physical* imports (3+1D particle physics, 1D thermodynamics) are loaded onto
the 2D diagrammatic map: there, mutual compatibility is **unchecked by the literature** (the
claim's falsifier — a passing cross-silo compatibility audit — did not appear in the Phase-1
external sweep). The claim is scoped to this: *unestablished* bearing, not *false* bearing.

## 3. Seam catalog (map / territory per construct)

| Construct | Map (what it is) | Territory (what it is not) | Seam (where the map ends) | Probe (what would cross the seam) |
|---|---|---|---|---|
| Spider | Linear-algebraic gadget: copy/merge of a measurement basis with phase | A particle, a worldline, a physical process in 3+1D | The completeness theorems (map-level) do not touch physical bearing | A demonstration that spider topology corresponds to a physical process (e.g., a braiding/statistics argument that respects 3+1D) |
| Pauli web | Stabilizer-structure bookkeeping | Spacetime structure of a code; black-hole geometry | The QEC semantics (2+1D code-over-time) are map-internal; gravity vocabulary is imported | A compatibility check of the AdS/CFT dictionary expressed in ZX diagrams against the 2D topology |
| Gadget | Diagrammatic encoding of a non-Clifford gate | Hardware component; a physical construction of T/H | MBQC equivalence is map-internal; physicalization assumptions are external | A scalable physical realization of the resource states the gadgets presuppose |

## 4. Generalization: the cafeteria problem

The seed note's claim: siloed disciplines "remain separate except when convenient to mix and
match." ZX diagrams are the worked example: a 2D map whose internal validity is beyond dispute
(soundness + completeness theorems, real compiler utility) and whose physical bearing is
unestablished — while the published record shows imports from 3+1D (spin networks, quantum
groups) and 1D (entropy, holography) being loaded onto the same diagrams without compatibility
checks. The pattern generalizes to any notation that travels faster than its caveats:
(1) a map gains users because it is *internally* valid; (2) the seam is unmarked on the map;
(3) imports from other silos arrive unvetted; (4) the cone of ignorance is unknown because the
map never probes outside its own locality. The remedy is map-aware use: declare the seam,
audit import provenance, and probe beyond the map's locality before asserting physical bearing.

## 5. WBS next steps

- `[QNFO.RES.015.P3]` references.bib + citation-audit.md from the 14 verified arXiv records + QNFO internal refs.
- `[QNFO.RES.015.P4]` Fault-line synthesis (plain scholarly prose), red-team, calibration register; UIA Q15 seed (aesthetic-criterion question) re-run.
- `[QNFO.RES.015.P5]` Publication gates + Zenodo deposit (full source set).
- `[QNFO.RES.015.P6/P8]` Deploy + distribute (D1, R2 `qnfo-releases`, KG).
