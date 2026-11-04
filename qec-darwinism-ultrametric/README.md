# Archimedean Shadows — QEC-Darwinism Ultrametric Tradeoff

**QNFO.UMP.004** | UMP × RES × INM bridge paper

## Research Question

How does the QEC-Darwinism tradeoff (Maity et al., arXiv:2608.03944) change when
the information geometry is ultrametric rather than Archimedean?

## The Idea

Maity et al. proved: QEC (protecting logical qubits) and Quantum Darwinism
(producing classical records) are in tension — you can't have both at maximum.
Their no-go theorem says: logical fidelity above a critical threshold precludes
redundant classical records entirely. **But the theorem assumes Archimedean
(Hamming/Lee) metrics.** The Bruhat-Tits tree — the native geometry for p-adic
information — has a fundamentally different distance structure. In an ultrametric,
fragments are either identical or maximally distant; there is no "partial" overlap.
This may change the tradeoff.

## Status

| Phase | Status |
|:------|:-------|
| P0 — Init | 🟢 Repo created, scaffold complete |
| P1 — Due Diligence | ⬜ |
| P2 — Literature | ⬜ |
| P4 — Core Derivation | ⬜ |
| P5 — Publication | 🟢 DOI 10.5281/zenodo.21810015 |

## Files

| File | Description |
|:-----|:------------|
| `PROJECT-PLAN.md` | Full WBS plan, milestones, risk register |
| `paper/qec-darwinism-ultrametric.md` | Paper draft with section outline |
| `artifacts/` | Due diligence, consilience gate, search evidence |
| `docs/` | Supplementary documentation |
| `notebooks/` | Computational notebooks |
| `releases/` | Published PDFs and archives |

## References

- Maity et al., arXiv:2608.03944v1 (2026-08-04) — the auditing target
- Continuum Trilogy Paper I, DOI: 10.5281/zenodo.21672990
- Adelic Shannon Theory, DOI: 10.5281/zenodo.21698976
- Five Pillars audit (Measurement Stratigraphy)

## CWI Connection

This paper is a companion to the CWI QEC Summer School poster (Aug 24–28, 2026).
The poster asks: *"What falsifies the QEC roadmap?"* — this paper answers with a
specific, falsifiable claim: the tradeoff between protected quantum information
and emergent classicality depends on which number system you build your codes in.
- **2026-08-16 — v1.11 so-what remediation** (DOI 10.5281/zenodo.21964674): new Section 2 "So What? Why Should a Reader Care About This Research?" (global so-what mandate; QEC engineering stakes, three ultrametric transformations, falsifiable predictions, practical-utility-in-both-outcomes, premises-depth ladder); P5.FRESH frontmatter DOI fix (v1.10 had shipped stale v1.9 DOI 21819152); sections renumbered 2-6 -> 3-7 with cross-refs updated; provenance files added to the deposit (README, PROJECT-PLAN, artifacts incl. bt-tree simulation evidence).
