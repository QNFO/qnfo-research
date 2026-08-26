# Future Research Topics — Noted for Investigation

**Collected:** 2026-08-26 during QNFO.JPC.003 Phase 0–3 (user directive: note other research topics for future investigation).
**Provenance:** CWI synthesis draft (_cwi-synthesis-draft-2026-08-26.md), JPC.003 due diligence (artifacts/due-diligence-phase1.md), H2 simulation results, cross-event QPL+CWI theme notes (2026-08-24.md).

## A. Opened by JPC.003 (this paper's own tail topics)

| # | Topic | One-line | Home |
|---|-------|----------|------|
| A1 | **Industrial flash test** | Run the §7 protocol with real tree/product LDPC constructions (two-bit per-group detection; erasure-correcting trees) against LDPC baselines on an open NAND workload. The H2 keystone at industrial scale. | QNFO.JPC |
| A2 | **QEC-Darwinism energy dimension** | Extend the QEC-Darwinism tradeoff (10.5281/zenodo.21964674) with the erasure-floor axis: does the ultrametric tradeoff surface get steeper or flatter under Equation (1)? | QNFO.QEC.001 |
| A3 | **Capital/operating crossover curve** | JPC.002 computes the protection-vs-QEC crossover for platforms; specialize it to correction: energy-landscape scaffold cost vs per-round erasure bill, parameterized by error rate and temperature. | QNFO.JPC.002 |
| A4 | **p-adic entropy of the erasure hierarchy** | Q1.4 from the keyword-taxonomy synthesis: is the correct entropy for a non-Archimedean (tree-valued) erasure hierarchy ℚ_p-valued, and does it bound correction costs tighter than Shannon entropy? | QNFO.ADL.002 |
| A5 | **Autonomous-QEC energy accounting** | The scope boundary of JPC.003 as its own paper: the continuous driving/dissipation bill of cat-qubit and GKP stabilization, priced in the same system-level currency. | QNFO.QEC |
| A6 | **Map-territory of stabilizer measurement** | "Reality is a syndrome; we probe it, never read it" — stabilizer measurement as a formal model of probing without a global vantage; the epistemology-QEC crosswalk (candidate #6 from the CWI synthesis). | QNFO.RES |
| A7 | **Vedral–Landi modernization** | A review/extension of the 1999–2019 QEC-thermodynamics line updated with quantum LDPC families, decoder energetics, and cryogenic realities. | QNFO.JPC |

## B. From the CWI synthesis pull (candidates not yet started)

| # | Topic | One-line | Home |
|---|-------|----------|------|
| B1 | **Post-positional numeracy** | The Hindu-Arabic decimal system as a "convenient lie"; Ostrowski's theorem + the adele ring as the post-positional foundation; local-global simultaneity. Thesis drafted in Obsidian (_26238100931.md, _26238083140.md, 2026-08-26). | QNFO.UMP |
| B2 | **Tree-structured QEC code construction** | The construction side of JPC.003's §7: nested-ball/ultrametric code families with hierarchical decoding, stronger than the toy (per-group CRC detection, RS erasure layers). | QNFO.UMP/QEC |
| B3 | **Silent-radix operationalization** | "What is the silent radix of the Ruliad?" — the keyword-taxonomy synthesis's 30 leveled RQs (Q0.1–Q6.4) made testable; Part C of the synthesis note prescribes the operationalization pass. (RES.022 published the consilience claim; the operationalized tests are open.) | QNFO.RES.022 |
| B4 | **Thermodynamics-only physics** | "The only physics is thermodynamics; a 1D gradient is the only dimension required for unification" — INM-program thesis needing formal grounding (_26232223244.md, _26232224820.md). | QNFO.INM |
| B5 | **Pattern-based ontology** | Why accelerator field patterns/frequencies get mistaken for Newtonian particles (_26236083406.md) — the PBO/Autaxys empirical case. | QNFO.PBO |
| B6 | **Cross-event metascience paper** | The six QPL+CWI themes (tautological self-definition, calculation-over-understanding, unpriced physical cost, design-choice-as-law, silo partition, observer-internal blind spot) as a metascience/epistemology record. | QNFO.RES |

## C. Adjacent-domain bridges discovered in JPC.003 Phase 1 (register as KG BRIDGES edges at publish)

- QEC syndrome reset ↔ bit erasure (information theory) — exact.
- Correction work ↔ Otto-cycle heat rejection (Landi et al. 2019) — exact.
- Structural protection ↔ protein energy landscapes (quantum biology) — good.
- Scaffold maintenance ↔ capital depreciation — metaphor, flagged.
- JPCUB ↔ NAND energy-per-corrected-bit — exact for classical storage.

**Standing rule:** when any of these becomes a project, it claims the next WBS slot in its home program (atomic insert, UNIQUE constraint), and the H2-style hypothesis-card pattern (claim + prediction + falsifier + surprisal, pre-registered) applies from Phase 0.
