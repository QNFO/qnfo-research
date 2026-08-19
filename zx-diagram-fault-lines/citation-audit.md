# Citation Audit — QNFO.RES.015 (Phase 3, 2026-08-18)

WBS: `[QNFO.RES.015.P3]` · Method: P3.AUTHOR-GATE — every entry verified against authoritative
arXiv metadata (export_citations) or direct arXiv title search. Zero-context verification:
each entry is real, correctly attributed, and cited in a context the paper actually supports.

## Verification ledger

| Cite key | arXiv ID | Authors (verified) | Real? | Correctly attributed? | Context-supported? |
|---|---|---|---|---|---|
| wang2022completeness | 2209.14894 | Quanlong Wang | ✅ | ✅ | ✅ ZX full-qubit completeness via ZW translation |
| jeandel2019completeness | 1903.06035 | Jeandel, Perdrix, Vilmart | ✅ | ✅ | ✅ Clifford+T + full ZX completeness |
| backens2016completeness | 1602.08954 | Miriam Backens | ✅ | ✅ | ✅ stabilizer + Clifford+T completeness; Spekkens toy theory |
| backens2016a | 1602.04744 | Backens, Perdrix, Wang | ✅ | ✅ | ✅ simplified stabilizer ZX |
| backens2017towards | 1709.08903 | Backens, Perdrix, Wang | ✅ | ✅ | ✅ minimal stabilizer ZX (rule necessity) |
| ng2017a | 1706.09877 | Ng, Wang | ✅ | ✅ | ✅ universal completion via ZW |
| beaudrap2017the | 1704.08670 | de Beaudrap, Horsman | ✅ | ✅ | ✅ spiders = lattice-surgery rough/smooth merges (QEC import) |
| wan2026holographic | 2601.04467 | Wan, Price, Yao | ✅ | ✅ | ✅ Pauli webs in holographic codes; Rényi entropy; toy black holes |
| east2021spinnetworks | 2111.03114 | East, Martin-Dussaud, Van de Wetering | ✅ | ✅ | ✅ SU(2) spin networks / LQG embedded in ZXH (3+1D import) |
| vandaele2024qubitcount | 2407.10171 | Vivien Vandaele | ✅ | ✅ | ✅ gadgetization of Hadamard; Pauli Fusion; lattice surgery |
| majid2021quantum | 2103.07264 | Shahn Majid | ✅ | ✅ | ✅ braided ZX on u_q(sl_2) (quantum-group import) |
| carette2025the | 2508.04296 | Carette, Cojocaru, Vilmart | ✅ | ✅ | ✅ decohered ZX (classical/probabilistic fragment) |
| comfort2026the | 2607.04015 | Comfort, de Felice | ✅ | ✅ | ✅ delayed stabilizer ZX (lattice/translation-invariant codes) |
| stoltz2026minimality | 2606.12383 | Harry K. Stoltz | ✅ | ✅ | ✅ minimality of stabilizer ZX rules |
| coecke2009interacting | 0906.4725 | Coecke, Duncan | ✅ | ✅ | ✅ foundational: spiders as interacting observables |
| wetering2020zxcalculus | 2012.13966 | John van de Wetering | ✅ | ✅ | ✅ working practitioner survey (Pauli webs, gadgets, completeness) |
| raussendorf2001the | quant-ph/0108118 | Raussendorf, Browne, Briegel | ✅ | ✅ | ✅ one-way quantum computer (MBQC origin of gadget machinery) |
| backens2018zh | 1805.02175 | Backens, Kissinger | ✅ | ✅ | ✅ ZH calculus, phase gadgets (non-linear classical encodings) |

## Rejections and corrections

1. **1809.00745 REJECTED** — recalled as Backens–Kissinger ZH; authoritative export resolved it to
   *Babun et al., "IoTDots: A Digital Forensics Framework"* (cs.CR). NOT the intended work.
   Correct ID **1805.02175** obtained via arXiv title search `ti:"ZH" AND "complete graphical
   calculus"` and re-exported: title, authors (Backens, Kissinger), year (2018) all match intent.

## Internal references (QNFO corpus, cited in PROJECT-PLAN/premise disclosure only)

- UMP.011 Conditional Truths and the Locale Framework — 10.5281/zenodo.21984929 (v0.4 artifact of
  21983324→21983659 chain). Verified via resolve_paper_id (2026-08-18).
- UMP.012 Locale Framework Applied to Quantum Computing — 10.5281/zenodo.21991270. Verified.
- RES.002 Universal Ignorance Audit — 10.5281/zenodo.21901984. Verified (get_paper_context).
- RES.013 Electron Hook Treatise — 10.5281/zenodo.21975507. Registry-verified.

## Counts

- 18 external entries, all verified real + correctly attributed + context-supported: **18/18 PASS**
- 0 hallucinated authors, 0 wrong years, 0 fabricated venues, 0 version mismatches
- 1 ID-correction applied (documented above) — the P3.AUTHOR-GATE earned its keep.


## v0.4 addendum (2026-08-19)

Ten new bibliography entries added for the post-publication appendix (QPL 2026 cluster).
Verification: all ten checked against the arXiv API or the official QPL submission PDF on
2026-08-19; no fabricated metadata.

| Key | Source | Verification |
|---|---|---|
| deaconu2025buildings | arXiv:2510.11526 | arXiv API title/authors match |
| wang2025spin | arXiv:2511.06012 | arXiv API match |
| wan2026holographic | arXiv:2601.04467 | arXiv API match |
| comfort2026delayed | arXiv:2607.04015 | arXiv API match (also [17] in the published reference list) |
| kuyanov2026rankwidth | arXiv:2603.06764 | arXiv API match |
| ruesch2025fault | arXiv:2510.08477 | self-stated in QPL PDF; cross-cited by 2601.04467 |
| kissinger2026zxflow | arXiv:2603.09580 | arXiv API match |
| yeh2026threeway | QPL 2026 submission only | no public arXiv identifier located; flagged in the entry note field |
| mcdowallrose2025fermions | arXiv:2505.06212 | self-stated in QPL PDF |
| defelice2026dataflow | arXiv:2601.08389 | arXiv API match |

Zero fabricated entries; one entry (yeh2026threeway) deliberately carries no arXiv identifier
rather than an unverified one.
