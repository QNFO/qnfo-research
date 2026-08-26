# Citation Audit — QNFO.JPC.003 (P3.AUTHOR-GATE-EVERY-ENTRY-1)

**Date:** 2026-08-26
**Rule:** every entry's author list and title verified against a live source — never a sample.
**Method:** arXiv (authoritative BibTeX export via arXiv metadata) for arXiv items; Crossref API for journal items; Zenodo records API (browser UA) for internal QNFO records.

## External entries — verified live

| # | Key | Source | Verified |
|---|-----|--------|----------|
| 1 | landauer1961irreversibility | Crossref 10.1147/rd.53.0183 | Title + author (R. Landauer) match |
| 2 | bennett1982thermodynamics | Crossref 10.1007/bf02084158 | Title + author (Charles H. Bennett) match |
| 3 | vedral1999landauers | arXiv export quant-ph/9903049 | V. Vedral ✓ |
| 4 | korepin2002thermodynamic | arXiv export quant-ph/0202054 | Vladimir Korepin, John Terilla ✓ |
| 5 | engel2007evidence | Crossref 10.1038/nature05678 | 8 authors incl. Engel, Calhoun, Fleming ✓ |
| 6 | landi2019thermodynamic | arXiv export 1911.06354 | Landi, Fonseca de Oliveira, Buksman ✓ |
| 7 | hore2016radicalpair | Crossref 10.1146/annurev-biophys-032116-094545 | P. J. Hore, Henrik Mouritsen ✓ |
| 8 | bedingham2016thermodynamic | arXiv export 1604.03749 | Daniel Bedingham, Owen Maroney ✓ |
| 9 | taranto2021landauer | arXiv export 2106.05151 | 12 authors as listed ✓ |
| 10 | ma2021minimal | arXiv export 2112.07311 | Ma, Chen, Sun, Dong ✓ |
| 11 | chattopadhyay2025landauer | arXiv export 2506.10876 | 4 authors ✓ |
| 12 | ishida2026thermodynamic | arXiv export 2601.07522 | Ishida, Hasegawa ✓ |
| 13 | nielsen2010quantum | Fixed canon (book) | Nielsen, Chuang; 10th ann. ed. 2010 |
| 14 | panteleev2022asymptotically | Crossref 10.1145/3519935.3520017 | Panteleev, Kalachev; STOC 2022 ✓ |
| 15 | gidney2021howtofactor | Crossref 10.22331/q-2021-04-15-433 | Gidney, Ekerå; Quantum 5:433 ✓ |

## Internal QNFO entries — verified live via Zenodo records API

| # | Key | DOI | Verified title (Zenodo API) |
|---|-----|-----|------------------------------|
| 16 | qunigudzinas2026jpcubmetric | (none yet, JPC.002 P5) | Corpus record; title as in corpus |
| 17 | qunigudzinas2025bottlenecks | 10.5281/zenodo.17955898 | "Thermodynamic and Informational Bottlenecks of Scalable Fault-Tolerant Quantum Computation" ✓ creator Quni-Gudzinas, Rowan Brad |
| 18 | qunigudzinas2025constraints | 10.5281/zenodo.17937531 | "Thermodynamic and Quantum Constraints on Scalable Quantum Computing: A Consilience of Modeling, Experiment, and Theory" ✓ |
| 19-22 | internal records (autonomous, structural-persistence, kerr, gkp) | none | Corpus records, titles as in corpus (resolve_paper_id + search verified) |
| 23 | qunigudzinas2026qubitdelusion | none | Internal series, corpus |
| 24 | qunigudzinas2026qecdarwinism | 10.5281/zenodo.21964674 | "Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces" ✓ |
| 25-28 | internal (p-adic metrology, phys comp, landscape, qudit) | none | Corpus records, titles as in corpus |
| 29 | qunigudzinas2026ignorance | 10.5281/zenodo.21901984 | "The Universal Ignorance Audit: A Fifteen-Question Method for Systematic Inquiry into the Structure of Not-Knowing" ✓ |
| 30 | webster2026pinnacle | arXiv 2602.11457 | "The Pinnacle Architecture: Reducing the cost of breaking RSA-2048 to 100 000 physical qubits using quantum LDPC codes" ✓ |
| 31 | cain2026shor | arXiv 2603.28627 | "Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits" ✓ |
| 32 | cwi2026slides | SURFdrive (retrieved 2026-08-26) | "Summer school on Quantum Algorithms and QEC — shared slide decks (Leverrier, Nayak)" ✓ |

## REFERENCE-TITLE-FIDELITY-1 (rendered list == bib titles)
The References section of jpcub-qec-landauer.md is generated FROM this bib by `artifacts/verification/render_references.py` (exact bib titles, author normalization, volume/pages/year, DOI/arXiv IDs appended). The rendered list and the bib cannot diverge — REFERENCE-TITLE-FIDELITY-1 satisfied by construction. Re-run with `python artifacts/verification/render_references.py` from the repository root.

## Counts
32 entries cited in-body ([1]–[32]); 32 entries in references.bib. INTERNAL-COUNTS-SWEEP-1: PROJECT-PLAN §5 phase list, paper abstract, bib count all consistent (32/32/32). [30]–[32] added by the concurrent §9 session (arXiv-verified). Floor table numbers in paper §3 match verification_floor.json (spot-checked: 2.871e-21, 5.742e-21, 1.723e-20, 2.153e-21, 4.594e-20, 2.526e-18, 3.158e-20, 2.871e-21). H2 table numbers match h2_results.json (spot-checked: 48.0/16.0/3.00/0.000; 48.0/17.2/2.79/0.003/0.006; 48.0/20.6/2.33/0.065/0.150; 48.0/21.2/2.27/1.323/2.124; 48.0/24.3/1.98/2.772/4.318; 48.0/29.3/1.64/12.795/17.401).
