# WBS: QNFO.UMP.004 — QEC-Darwinism Ultrametric Shadow

## Charter

**Research Question:** How does the QEC-Darwinism tradeoff (Maity et al., arXiv:2608.03944)
change when the information geometry is ultrametric rather than Archimedean?

**Core Claim:** The no-go theorem establishing `R(f) · F_L ≤ C` assumes standard
(Archimedean) code spaces. When QEC codewords are structured on the Bruhat–Tits tree
— the native ultrametric geometry for p-adic information — the redundancy concept
and the tradeoff constant `C` transform in ways that may admit new regimes of
simultaneous quantum protection and classical objectivity.

**Programs Crossed:** UMP (ultrametric code geometry) × RES (Quantum Darwinism /
Measurement Stratigraphy) × INM (information-theoretic no-go theorem)

## Program Routing

| Key | Value |
|:----|:------|
| Portfolio | QNFO |
| Program | UMP (Ultrametric Physics) |
| Project | 004 |
| WBS Code | QNFO.UMP.004 |
| GitHub Repo | QNFO/qec-darwinism-ultrametric |
| Branch | `ump/paper/qec-darwinism-ultrametric` |
| arXiv Target | 2608.03944 (Maity et al.) as the auditor target |

## Phases

| Phase | Status | Deliverable | Est. Date |
|:------|:-------|:------------|:----------|
| P0 — Init | ⬜ | Repo scaffold, claim lock, PROJECT-PLAN.md | Aug 5 |
| P1 — Due Diligence | ⬜ | KG/D1/Vectorize cross-ref, arXiv deep read, silo-cost table | Aug 6–8 |
| P1 — Consilience Gate | ⬜ | Cross-domain lexicon (UMP × RES × INM), KIF-29 gate | Aug 6–8 |
| P2 — Literature | ⬜ | p-adic code theory, ultrametric QEC, Darwinism foundations | Aug 9–12 |
| P3 — Citations | ⬜ | BibTeX extraction, verification against Crossref | Aug 12–13 |
| P4 — Core Derivation | ⬜ | Reformulate tradeoff in ultrametric geometry | Aug 14–21 |
| P5 — Publication | ⬜ | qec-darwinism-ultrametric.md, PDF build (pandoc→MathJax SVG→CDP), Zenodo DOI | Aug 22–27 |
| P6 — Deploy | ⬜ | D1 living-paper, papers-server verification | Aug 27–28 |
| P7 — Disseminate | ⬜ | SEO, Buffer social, papers.qnfo.org | Aug 28–30 |

## Milestones

| # | Date | Description | Gate |
|:--|:-----|:------------|:-----|
| M0 | Aug 5 | Repo created, scaffold complete | Branch pushed to GitHub |
| M1 | Aug 8 | Due diligence complete, consilience gate passed | KIF-29 record in artifacts/ |
| M2 | Aug 12 | Literature search complete, 8 sources queried | Evidence in artifacts/external-search/ |
| M3 | Aug 21 | Core derivation complete — tradeoff reformulated | qec-darwinism-ultrametric.md §§1-4 drafted |
| M4 | Aug 24 | **CWI Summer School begins** — present preliminary results at poster session Wed Aug 26 |
| M5 | Aug 27 | Paper published — arXiv, Zenodo DOI, D1 | All BP-1 through P5.FRESH gates |
| M6 | Aug 28 | Dissemination complete | Buffer posts confirmed |

## Reference Paper (Auditing Target)

- **Title:** Exact Tradeoff Between Quantum Error Correction and Quantum Darwinism:
  An Information-Theoretic No-Go Theorem
- **Authors:** Arghya Maity, Kelvin Onggadinata, Teck Seng Koh
- **arXiv:** 2608.03944v1 (submitted 2026-08-04)
- **Core Result:** `R(f) · F_L ≤ C` — exact tradeoff between Darwinistic redundancy and
  post-recovery logical fidelity; model-independent no-go theorem showing F_L above a
  critical threshold precludes redundant classical records
- **Model:** Block-environment model based on logical GHZ block of Shor [[9,1,3]] code,
  collectively coupled to N environment qubits
- **Key Quantities:** Logical fidelity, Holevo information, Darwinistic redundancy
- **Entry Point for QNFO:** All quantities are defined over Archimedean (Hamming/Lee)
  metrics. The ultrametric reformulation replaces these with p-adic distance measures
  on the Bruhat-Tits tree

## Key Questions (Open)

1. What does "redundancy" mean in an ultrametric? (Strong triangle inequality ⇒
   fragments are either identical or maximally distant)
2. Does the tradeoff constant C change under ultrametric metrics?
3. Can ultrametric QEC codes achieve both high logical fidelity AND high Darwinistic
   redundancy — that is, can the Archimedean no-go theorem be circumvented
   by changing the geometric substrate?
4. What would an experimental signature look like? (p-adic noise models vs.
   standard depolarizing/amplitude-damping channels)

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| The ultrametric reformulation yields the same tradeoff (null result) | Medium | High | The null result IS the finding — "the no-go theorem is Ostrowski-invariant" — publishable either way |
| CWI workshop velocity too fast to incorporate results | High | Low | Pre-draft §§1-2 before workshop; use feedback as §5 material |
| Literature on p-adic QEC codes is thin | Medium | Medium | The thinness IS the novelty signal; document honestly |
| Maity et al. paper revised during this project | Low | Medium | Pin arXiv v1; note any revisions in §1 footnotes |
