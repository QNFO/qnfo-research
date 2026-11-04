# The Revolutionary Beginner's Guide to Quantum Computing

**Why We Don't Have Quantum Computers Yet — and What the Geometric Alternative Offers**

Rowan Brad Quni-Gudzinas (QNFO/QWAV) · v1.3.3 · 2026-08-21 · CC BY 4.0

A 20-chapter beginner's guide to quantum computing that starts with an honest
question — why don't we have quantum computers yet? The guide teaches the
standard curriculum accurately, explains why the standard approach faces a
thermodynamic wall (a 20,000-fold cooling gap that is Carnot-limited), and
introduces the ultrametric alternative: passive geometric fault tolerance on
Bruhat-Tits trees, with DOI-registered evidence, computationally validated
error thresholds 75 times higher than surface codes, and three falsifiable
predictions.

## How to cite

Cite all versions — you can use this DOI to cite the work and it will always
resolve to the most recent version:

**10.5281/zenodo.20391554**

Quni-Gudzinas, Rowan Brad. *The Revolutionary Beginner's Guide to Quantum
Computing: Why We Don't Have Quantum Computers Yet — and What the Geometric
Alternative Offers.* v1.3.3, Zenodo, 2026-08-21.
https://doi.org/10.5281/zenodo.20391554

## What changed in v1.3.3 (August 2026)

- Post-publication audit remediation: two corrupted TeX macros that rendered
  "Math input error" in the HTML/PDF are fixed; the Part VI summary now lists
  eight open problems (matching Chapter 20); a stray '#' before the E3-design
  paragraph is removed; stale version labels and the README provenance footer
  are corrected; the rendering gate now also scans control characters and
  heading-without-space lines (10 checks).

## What changed in v1.3.2 (August 2026)

- README.md restored to this deposit manifest (a project-blueprint README was
  attached in v1.3/v1.3.1 by an automation error). Structural guards now assert
  both the LICENSE and README contents before every upload. No content changes.

## What changed in v1.3.1 (August 2026)

- LICENSE file corrected to the full CC BY 4.0 International legal code (an
  automation error shipped the program's repository license in v1.3); the
  rendering-check log now carries the full per-check record. No content changes.

## What changed in v1.3 (August 2026)

- Substantive update: joules-per-solution benchmark section (Chapter 9), E3 hardware
  design with five pre-registered observables (Chapter 16), the program's published
  self-correction as a falsification exemplar (Chapter 15), the calibrated displacement
  assessment as open problem 8 (Chapter 20), and an extended evidence trail (2026
  thermodynamic-successor analysis, qudit benchmark, consolidated mathematical thesis,
  QCA verification template).
- Rendering and structure fixes: currency symbols escaped so no false math delimiters
  remain; duplicated abstract/date removed from the body (the YAML header is the single
  source).

## What changed in v1.2.2 (August 2026)

- Deposit files corrected: `LICENSE` now contains the full Creative Commons
  Attribution 4.0 International legal code (matching the record's license),
  and `README.md` is this deposit manifest (a project-blueprint README was
  attached in v1.2.1 by an automation error).

## What changed in v1.2.1 (August 2026)

- Post-publication audit corrections (three-reviewer red team, 0 HARD
  findings): Chapter 20's summary now lists seven open problems (added the
  QEC–Darwinism tradeoff); the LHC temperature comparison is marked
  approximate (95×, rounded to ~100); Appendix A correction #5 completed;
  the citation audit's internal-reference count corrected; open problem 7
  carries its numeric bound (F_L > 0.874). No quantitative claims changed.

## What changed in v1.2 (August 2026)

- Five quantitative corrections, each verified by independent computation
  (see Appendix A and B of the manuscript and
  `artifacts/verification/verification-log.txt`).
- New Appendix A: program update — new evidence records published since
  May 2026 (trapped-ion falsifiability register, QEC-Darwinism tradeoff
  audit, prime-valuation QEC correction, laws-of-form consolidation).
- New Appendix B: computational verification — every quantitative claim
  checked by a deposited script (35 checks, all passing).
- Complete source deposit: manuscript, HTML, PDF, references (BibTeX),
  citation audit, project plan, and verification artifacts.
- License reconciled to CC BY 4.0 (matching the published record).

## Files in this deposit

| File | Purpose |
|:-----|:--------|
| `The-Revolutionary-Beginners-Guide-to-Quantum-Computing.md` | Manuscript (v1.3.3) |
| `The-Revolutionary-Beginners-Guide-to-Quantum-Computing.html` | Rendered HTML |
| `The-Revolutionary-Beginners-Guide-to-Quantum-Computing.pdf` | Rendered PDF |
| `references.bib` | All references, BibTeX |
| `citation-audit.md` | Live citation verification report |
| `README.md` | This file |
| `PROJECT-PLAN.md` | Project plan and v1.2/v1.2.1 change record |
| `docs/ignorance-audit.md` | Ignorance audit of the core claims |
| `artifacts/verification/verify_guide_claims.py` | Verification script |
| `artifacts/verification/verification-log.txt` | Verification results (35 PASS) |
| `LICENSE` | CC BY 4.0 |

## Reproducing the verification

```
python artifacts/verification/verify_guide_claims.py
```

Requires Python 3.12, standard library only, deterministic. Writes
`artifacts/verification/verification-log.txt`; exit code 0 = all checks pass.

## Provenance

- Source repository: https://github.com/QNFO/revolutionary-quantum-guide
- This version: v1.3.3 record 10.5281/zenodo.22043966 · v1.3.2: 10.5281/zenodo.22040750 · v1.3.1: 10.5281/zenodo.22040708 · v1.3: 10.5281/zenodo.22040426 · v1.2.2: 10.5281/zenodo.22038733 · v1.2.1: 10.5281/zenodo.22038672 · v1.2: 10.5281/zenodo.22036025 · Prior version: v1.1 (2026-05-26), record 10.5281/zenodo.20391555
- v1.2.1: 10.5281/zenodo.22038672 · v1.2: 10.5281/zenodo.22036025 ·
  Prior version: v1.1 (2026-05-26), record 10.5281/zenodo.20391555
- Author: Rowan Brad Quni-Gudzinas — ORCID 0009-0002-4317-5604
- Part of the QWAV research program (QNFO)
