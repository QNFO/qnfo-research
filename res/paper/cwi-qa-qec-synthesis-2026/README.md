# The Unpriced Column

A slide-level synthesis of the CWI Summer School on Quantum Algorithms and Quantum Error Correction (Amsterdam, 24–28 August 2026): what the 2026 QEC curriculum prices and what it does not.

## Files

- `cwi-qa-qec-synthesis-2026.md` — the paper (source)
- `cwi-qa-qec-synthesis-2026.html` / `cwi-qa-qec-synthesis-2026.pdf` — rendered versions
- `PROJECT-PLAN.md` — research plan with locked claim and falsifiers
- `OUTLINE.md` — phase-2 skeleton
- `DUE-DILIGENCE.md` — phase-1 full-corpus due diligence
- `citation-audit.md` + `references.bib` — verified bibliography (10/10)
- `artifacts/cwi-slide-audit.md` — slide-to-quote evidence map
- `artifacts/verification/` — energy scan + quote trace + rendering gate (scripts, evidence, outputs)

## Reproduce the verification

Requires CPython 3.12 + pypdf. The seven decks come from the organizers' share (see the paper's Reproducibility section):

```
python artifacts_verification_energy_scan.py --decks-dir <decks>
python artifacts_verification_quote_trace.py --decks-dir <decks> --paper cwi-qa-qec-synthesis-2026.md
python artifacts_verification_check_rendering.py cwi-qa-qec-synthesis-2026.md
```

## How to cite

Cite all versions: 10.5281/zenodo.22121556 (concept; this first version has the same identifier).
This version: 10.5281/zenodo.22121556.
