# Adelic Quantum Arithmetic: Particles as Prime Factors

Rowan Brad Quni-Gudzinas — QNFO — 2026-08-27 — CC BY 4.0

Record DOI: https://doi.org/10.5281/zenodo.22133707
Concept DOI: https://doi.org/10.5281/zenodo.22133706

## How to cite

Quni-Gudzinas, Rowan Brad (2026). *Adelic Quantum Arithmetic: Particles as Prime Factors.* QNFO. https://doi.org/10.5281/zenodo.22133707

Cite all versions: https://doi.org/10.5281/zenodo.22133706 — always resolves to the latest version.

## What this record is

A reader-facing synthesis of the adelic-quantum-arithmetic thesis: standard quantum mechanics as the Archimedean readout of a larger arithmetic structure (Ostrowski's classification of places), primes as the non-Archimedean places, and the multiplicative structure of the integers (unique factorization) as the origin of the Bose–Einstein/Fermi–Dirac binary. The proofs are carried from the published records (10.5281/zenodo.22123068, 10.5281/zenodo.22124744, 10.5281/zenodo.22035210), not redone; the paper adds the practitioner-facing crosswalk ("particles as prime factors") and the proved/conjectured/disconfirmed separation. The register is structural: the claims are isomorphisms of mathematical structure, no physical particle is implied, and the premises end where the identification of a physical temperature at the p-adic place begins.

## Contents (all at the deposit top level)

- adelic-quantum-arithmetic.md / .html / .pdf — the paper
- references.bib + citation-audit.md — 20 entries, machine-generated from live metadata (DataCite, Zenodo records API, Crossref, arXiv API), every entry verified on 2026-08-27
- sim-adelic-quantum-arithmetic-verification.py + verification-output.json + README-verification.md — verification suite, 18/18 checks pass, deterministic, Python stdlib only
- check_rendering.py — the pre-publish rendering gate (dollar parity, banned words, Unicode superscripts, frontmatter duplication, citation integrity)
- PROJECT-PLAN.md + UIA-ADELIC-QUANTUM-ARITHMETIC.md — Phase 0 artifacts (locked core claim; 15-question Universal Ignorance Audit)
- due-diligence-res029.md — Phase 1 due-diligence report (full-corpus sweep, cross-system ID validation, adjacent-domain scan, gap analysis with binding amendments)
- red-team-p4-2026-08-27.md — Phase 4 red-team report (0 HARD / 5 SOFT, all remediated)
- corpus-sweep-2026-08-27.json, arxiv-evidence-2026-08-27.json, resolve-paper-id-evidence-2026-08-27.json, citation-verification-2026-08-27.json — Phase 1 evidence files

## Reproduce the verification

    python sim-adelic-quantum-arithmetic-verification.py

Writes verification-output.json beside the script. Deterministic (no random seeds); Python 3 standard library only; runtime ~1.8 s on consumer hardware. The same command runs unchanged from the repository branch.

## Provenance

- GitHub: https://github.com/QNFO/qnfo-research/tree/res/paper/adelic-quantum-arithmetic
- Pipeline tags: v0.1-phase0-res029 (P0 plan + UIA), v0.2-phase1-res029 (P1 due diligence), v0.3-phase2-res029 (P2 draft), v0.4-phase3-res029 (P3 citations + verification), v0.5-phase4-res029 (P4 red-team), v1.0-phase5-res029 (P5 publication).
- Every quantitative statement in the paper is reproduced by the deposited verification suite; the reference list is rendered from references.bib.
- Discipline: the Adelic Representation Theorem is an unproven conjecture and is labeled as such; disconfirmation criteria are written in the paper; the disconfirming findings of the program are cited alongside the proved results.
