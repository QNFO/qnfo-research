# Project Plan: PQS AI-Evaluation Audit

## 1. Charter

### 1.1 Purpose
Archive and publish the complete research record from a 2026-07-24 session investigating the Post-Quantum Synthesis (PQS) framework, spanning both a direct investigation of PQS claims and an analysis of how AI systems evaluate such claims.

### 1.2 Core Claim Lock
Two distinct, non-conflicting research questions were pursued:
1. **PQS Investigation**: What are the specific claims of the Post-Quantum Synthesis framework's four sub-pillars, and how do they relate to existing peer-reviewed physics and mathematics literature? (Neutral, non-editorializing investigation.)
2. **AI Gate-Check Analysis**: When two independent AI systems (Claude, Gemini) evaluate the same novel scientific framework in separate conversations, do they converge on similar assessments, and what does this reveal about AI-assisted scientific literacy? (A separate, valid research question — but one that emerged from and was initially conflated with question 1, requiring an explicit scope correction mid-session.)

## 2. Phases (WBS)

| Phase | Description | Status |
|:------|:-------------|:-------|
| 0 | Repo initialization, scaffold | Complete |
| 1 | Due diligence (KG query, QNFO cross-reference) | Complete |
| 2 | Literature search (48 arXiv papers, 25 Zenodo records) | Complete |
| 3 | Source extraction (4 SSRN abstracts + full 73pp PQS paper) | Complete |
| 4 | Investigation synthesis + red-team audit (8 findings, all fixed) | Complete |
| 5 | Publication (GitHub, R2, Zenodo) | In progress |
| 6 | Deployment (D1/KG) | Pending |
| 7 | Closeout | Pending |

## 3. Milestones

- **M1**: Corrected, red-team-passed PQS investigation document — Complete
- **M2**: Full source paper retrieved and archived — Complete
- **M3**: All 9 deliverables published to durable storage (GitHub + R2 + Zenodo) — In progress

## 4. Deliverable Registry

| Deliverable | Location | Type |
|:------------|:---------|:-----|
| PQS-Research-Investigation.md | docs/ | Investigation |
| PQS-Research-Investigation-RedTeam-Findings.md | docs/ | Audit |
| PQS-Full-Paper-Source.md | docs/ | Source material |
| AI-Comparison-Claude-vs-Gemini-PQS.md | artifacts/ | Analysis |
| Physics-Claims-Assessment-PQS-4K.md | artifacts/ | Assessment |
| Synthesized-Note-Rowan-PQS-Gate-Check.md | artifacts/ | Synthesis |
| Gate-Check-Publication-AI-Fringe-Claims.md | artifacts/ | Publication draft |
| Literature-Classification-LLM-Gate-Check.md | artifacts/ | Literature review |
| Deep-Research-LLM-Gate-Check-Bayesian-Cascade.md | artifacts/ | Deep research |

## 5. Risk Register

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|:-----------|:-------|:-----------|
| 1 | `artifacts/` documents use language/framing the author explicitly flagged as wrong-direction | High (realized) | Medium | Documented in README Scope Note; preserved for transparency, not endorsed as final analysis |
| 2 | Numerical claims in `artifacts/Physics-Claims-Assessment-PQS-4K.md` carried over from unverified AI transcript | High (realized) | Low-Medium | Flagged in `docs/PQS-Research-Investigation-RedTeam-Findings.md` Finding 5 |
| 3 | Zenodo DOI is permanent — cannot be un-published if scope issues are found later | Medium | High | New versions can be created via Zenodo version-chain API if corrections are needed |
| 4 | "Stergios Pellis dimensionless theory" citation in source PQS paper could not be independently verified | Confirmed | Low | Flagged inline in `docs/PQS-Research-Investigation.md` |
| 5 | GitHub repo created under personal account, not organization | Low | Low | Repo target verified via `git remote -v` before any tag/push |

## 6. Success Criteria

- All 9 files present in the published repository
- GitHub repo public, tagged, pushed
- R2 archive contains all files, verified via round-trip read
- Zenodo DOI resolves live (HTTP 200)
- README accurately discloses the scope distinction between `docs/` and `artifacts/`

## 7. Version History

- v1.0 (2026-07-24): Initial publication of complete research record
