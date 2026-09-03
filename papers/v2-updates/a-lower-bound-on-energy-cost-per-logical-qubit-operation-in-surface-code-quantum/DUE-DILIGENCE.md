# Due diligence log (2026-09-03)

- Corpus check: qnfo-memory-mcp / QWAV semantic search over the living-paper index for 'surface code energy per logical qubit operation'; positioned against the closest QNFO records instead of duplicating them.
- External check: the cited arXiv identifiers were fetched live from the arXiv API (export endpoint) on 2026-09-03; every identifier resolves to the cited paper.
- Literature positioning: [1]-[4] (or [1]-[5]) define the classical floors and the constant-overhead counterpoint; this record adds a convention-explicit, script-verified computation rather than a new physical claim.
- Computational verification: every table and ratio in the paper is produced by the deposited script jpcub_nv_verify.py (see the paper's Verification section and the deposited output).
- Erratum note: v2.0.0 (2026-09-03) printed the scaling check with a mislabeled pair; the correct identity is N_g(15)/N_g(9) = (15/9)^3 = 4.6296 (and N_g(21)/N_g(9) = (21/9)^3 = 12.7037). This version (2.0.1) corrects the label in the abstract, the scaling-check line, and the Verification section.

Deposit: 10.5281/zenodo.22278600