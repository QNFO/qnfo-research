# Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi–Dirac/Bose–Einstein Distinction

**Author:** Rowan Brad Quni-Gudzinas · **DOI:** 10.5281/zenodo.22123068 · **Concept DOI:** 10.5281/zenodo.22123067 · **License:** CC BY 4.0 · **Status:** published v1.0.0 (2026-08-27)

## How to cite

Cite all versions (always resolves to the latest one):

> Quni-Gudzinas, Rowan Brad. *Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi–Dirac/Bose–Einstein Distinction*. Zenodo. https://doi.org/10.5281/zenodo.22123067

Cite this version specifically:

> Quni-Gudzinas, Rowan Brad. *Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi–Dirac/Bose–Einstein Distinction*. Zenodo, version 1.0.0, 2026-08-27. https://doi.org/10.5281/zenodo.22123068

## Abstract

Why are there two quantum statistics, and only two, in three spatial dimensions? This paper reads the Bose–Einstein and Fermi–Dirac occupation distributions as the maximum-entropy solutions of one lattice with two multiplicity rules: the unrestricted integer lattice carries the Bose side (Dirichlet series the Riemann zeta function) and the squarefree restriction carries the Fermi side (the ratio of two zeta values). The per-place identifications at fugacity z = 1/p were established elsewhere; this paper supplies the tiers those records leave open: the per-distinction rate gamma = 1/N from bath degeneracy, the complex structure as the sign-normalized generator selected by exclusion, the Möbius-parity dictionary of composite statistics, and the bounded-occupation family that interpolates between the two statistics. The register is structural: no physical particle is implied; the claims are isomorphisms of mathematical structure, and the physical labels attach at the level of statistical distributions.

## Reproduce the verification

The deposit is flat: every script below sits in this directory and writes its results JSON next to itself. Standard-library Python only, seeded, deterministic; runtimes on the order of seconds.

```
python verify_stats.py
python verify_product_formula.py
python verify_parastats.py
python verify_rate_gamma.py
python verify_symplectic.py
python verify_maxent.py
```

Expected: 163/163 checks passing in total (65 + 17 + 16 + 15 + 34 + 16). The rendered reference list (33 entries) is rebuilt with:

```
pandoc adelic-quantum-statistics.md -s --citeproc --bibliography=references.bib --mathjax -o adelic-quantum-statistics.html
python check_rendering.py
node render-pdf.cjs
```

The F4 prior-art scoping is executable:

```
python f4-differential-primon-gas-audit.py
```

## Files

- `adelic-quantum-statistics.md` / `.html` / `.pdf` — the paper (v1.0.0).
- `references.bib` — 33 entries, every one verified against Crossref/arXiv/Zenodo (see `citation-audit.md`).
- `citation-audit.md`, `PROJECT-PLAN.md`, `DUE-DILIGENCE.md`, `OUTLINE.md` — provenance and planning.
- `ignorance-audit.md`, `red-team-2026-08-27.md` — the ZENODO-INQUIRY-1 audit and the two red-team rounds.
- `verify_*.py` + `verify_*_run-2026-08-27.txt` + `verify_*_results.json` — the 163-check verification fleet.
- `check_rendering.py`, `render-pdf.cjs` — the rendering gates.
- `f4-differential-primon-gas-audit.py` + evidence files — the prior-art differential audit.
- `external-verify-2026-08-27.txt`, `crossref-verify-2026-08-27.txt`, `doi-check-2026-08-27.txt` — external verification evidence.
- `deposit-create.json`, `deposit-reserve-doi.json`, `deposit-summary.json` — publication evidence.

## Source

https://github.com/QNFO/qnfo-research/tree/res/paper/adelic-quantum-statistics
