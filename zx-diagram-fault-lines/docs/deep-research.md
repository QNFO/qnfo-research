# Deep Research & Gap Analysis — QNFO.RES.015 (Phase 1, 2026-08-18)

WBS: `[QNFO.RES.015.P1]` · Evidence: `artifacts/external-search/corpus-sweep-2026-08-18.md`

## 1. What the corpus says (internal QNFO landscape)

The QNFO corpus contains **no prior treatment of the ZX calculus itself** (0 KG nodes; the only
empty semantic query in the sweep was the direct ZX formulation). What it DOES contain is the
full conceptual toolkit the fault-line audit needs, already developed in adjacent programs:

- **UMP.011 Conditional Truths and the Locale Framework** (10.5281/zenodo.21984929, versions
  21983324 → 21983659): "the pedagogical map is not the ontological territory" — every physical
  statement holds only within a locale; first-person observation inside a rendering interface
  cannot decide the substrate. *This is the precise vocabulary for the seam.*
- **UMP.012 Locale Framework Applied to Quantum Computing** (10.5281/zenodo.21991270): the
  practitioner-domain application — seams catalog, map-territory readings of quantum-computing
  innovations, joules-per-solution scale primitives. *This is the closest QNFO ancestor: the
  same critical move applied to quantum computing as a whole, not yet to the ZX calculus.*
- **RES.013 Electron Hook Treatise** (10.5281/zenodo.21975507): method for auditing load-bearing
  assumptions. The cafeteria audit is an instance of this method applied to a formalism.
- **Meta-Pattern of Reification in Physics** (KG paper:meta-pattern-of-reification-in-physics):
  the general reification pattern — maps becoming things. The ZX spiders are a concrete case.
- **Qubit Delusion / Beyond the Qubit**: particle-ontology critique of quantum computing —
  adjacent: notation-level ontology errors are a known QNFO theme.
- **SLB reentrant-distinctions**: QNFO's own diagrammatic calculus — an in-house proof that
  diagrammatic reasoning can be done with seam discipline, and a standing internal comparison.

## 2. What the external record says

The arXiv verification (14 records, evidence file) confirms:

1. **The ZX calculus is mathematically mature**: completeness for stabilizer, Clifford+T, and
   full pure-qubit QM (Backens 1602.08954; Jeandel–Perdrix–Vilmart 1903.06035; Wang 2209.14894;
   Ng–Wang 1706.09877). Internal validity is not in dispute — the claim explicitly preserves it.
2. **The import-mixing is real and accelerating**: the published record already shows ZX diagrams
   loaded with (a) lattice-surgery QEC imports (de Beaudrap–Horsman 1704.08670 — spiders ↔ rough/
   smooth merges), (b) holography/AdS-CFT imports including Rényi entropy and black-hole toy
   models (Wan–Price–Yao 2601.04467, via Pauli webs), (c) loop-quantum-gravity spin-network
   imports (East–Martin-Dussaud–Van de Wetering 2111.03114), (d) quantum-group imports (Majid
   2103.07264). Each import ships its own soundness story; **no published cross-silo
   compatibility audit was found** — the claim's designated falsifier (Q5 of the UIA) did not
   materialize in the sweep.
3. **Pauli webs and gadgets are precisely located**: Pauli webs = stabilizer-structure tracking
   inside ZX diagrams (QEC/lattice-surgery literature); gadgets = diagrammatic encodings of
   non-Clifford operations used in circuit optimization (Vandaele 2407.10171 "gadgetization").
   Both constructs are *compilation-layer* imports — exactly where a 2D map earns its keep —
   which sharpens the seam question: the seam is not inside the computational domain (where the
   map demonstrably works) but at the boundary where the diagrams are read as pictures of
   physical processes.

## 3. Gap analysis

| # | Gap | Status | Who could fill it / where |
|---|---|---|---|
| G1 | No QNFO treatment of ZX calculus as epistemic object | **Open — this project** | RES.015 |
| G2 | No cross-silo compatibility audit of ZX imports (2D categorical / 3+1D QFT / 1D thermo) exists externally | **Open — this project's core contribution** | arXiv sweep found none |
| G3 | UMP.011/012 stop at the practitioner-application level; the *notation layer* (diagrammatic language itself) is unaudited | **Open** — RES.015 extends the locale framework INTO the notation | Bridge: UMP.012 → RES.015 |
| G4 | The cafeteria problem is named in the seed note but has no general articulation in the corpus | **Open** — RES.015 §generalization | Cross-ref: there-are-no-theories, meta-pattern-of-reification |
| G5 | Internal QNFO risk: the critique's own lens (locale framework) is itself an import | **Acknowledged** — UIA Q10 held; premise-depth disclosure in PROJECT-PLAN §2 | Red-team P4 |
| G6 | Corpus data-quality: duplicate Paper nodes for Meta-Pattern of Reification (3 node IDs) | **Noted** — KG hygiene, not a blocker | kaizen/KG maintenance |

**Positioning:** RES.015 is not a rival to the ZX completeness literature (which it imports and
respects) and not a repeat of UMP.012 (which audits applications, not notation). It is the
**notation-layer extension of the locale framework**: apply map/territory + seam discipline to
the diagrammatic language itself, decompose the three named constructs by import provenance,
audit cross-silo compatibility, and generalize the cafeteria problem.

## 4. SO-WHAT-GATE

**Why a reader should care (final prose form):**

> ZX diagrams are the fastest-growing language in quantum computing — the workhorse of circuit
> optimization, error correction, and measurement-based computation — and they are taught as
> *the* intuitive picture of quantum processes. The published record now shows the same diagrams
> being loaded with imports from lattice surgery, holography, loop quantum gravity, and quantum
> groups, each carrying its own internal guarantees and none audited against the others. A
> practitioner who reads a spider as a physical process, a Pauli web as a picture of a code's
> spacetime structure, or a gadget as a piece of hardware is using a 2D map whose seam is
> nowhere marked on the diagram. This paper names the seam, tables the import provenance of the
> three constructs, and gives the map-aware discipline for keeping the diagrams without
> mistaking them for the territory — with the cafeteria problem generalized as a standing risk
> of every siloed discipline that mixes imports when convenient.

**Premise-depth disclosure:** as tabled in PROJECT-PLAN §2 — imported primitives (ZX math,
stabilizer formalism, MBQC) vs named inputs (UMP.011/012, RES.013, RES.002 UIA) vs derived work
(provenance tables, compatibility audit, seam map, generalization) vs unanalyzable floor (the
representational stance itself; the epistemic-risk premise about unchecked mixing). The paper's
prose will state this boundary, not name the gates.

## 5. Next steps (WBS-coded)

- `[QNFO.RES.015.P2]` Import-provenance tables for spiders / Pauli webs / gadgets + pairwise
  compatibility audit + seam catalog (`docs/import-provenance.md`).
- `[QNFO.RES.015.P3]` Bibliography: 14 arXiv records + QNFO internal refs, verified
  (P3.AUTHOR-GATE), `references.bib` + `citation-audit.md`.
- `[QNFO.RES.015.P4]` Fault-line synthesis + red-team (accuracy/completeness/dependency) +
  calibration register; re-run UIA Q15 seed (aesthetic-criterion question).
- `[QNFO.RES.015.P5]` Publication: plain scholarly prose (PUBLICATION-PROSE-GATE-1), md/html/pdf,
  Zenodo with full source set.
- `[QNFO.RES.015.P6]` Deploy: D1 living-paper + papers-server; claim locked.
- `[QNFO.RES.015.P7]` Dissemination (user-gated).
- `[QNFO.RES.015.P8]` Distribute: R2 mirror to `qnfo-releases/2026/08/zx-diagram-fault-lines/`,
  KG distribution_status, concept-DOI cite block.
