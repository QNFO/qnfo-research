# WBS: QNFO.RES.002

# Project: Human Perception of AI-Generated Writing

**Charter:** Synthesize the empirical literature on how humans perceive AI-generated writing — where the generative text is itself a statistical re-composition of human writing (LLM training = distributional synthesis of human corpora). The project (1) maps the perception evidence (detection, label effects, algorithm aversion/appreciation, uncanny-valley transfer), (2) identifies the *synthesis-from-human-writing* framing as the under-modeled gap, (3) connects the evidence to QNFO's AI-QUALITY-GATE-1 / disclosure strategy, and (4) produces a falsifiable, pre-registered account of *perceived humanness vs. statistical proximity to human training distribution*.

**Program:** QNFO.RES (QNFO Research Archive) — resolved live from D1 `program_registry` (QNFO.RES.001 = Bayesian Synthesis Methodology is the prior project).

---

## Phase 0 Deliverables (this commit)

| ID | Deliverable | Status |
|---|---|---|
| D0.1 | PROJECT-PLAN.md (this file) | ✅ |
| D0.2 | README.md | ✅ |
| D0.3 | .gitignore | ✅ |
| D0.4 | Branch `res/paper/ai-text-perception` pushed | ✅ |
| D0.5 | Tag `v0.1-phase0` | ✅ |

---

## Core Claim (LOCKED at Phase 0, P6)

**C1 (structural):** AI-generated writing is a *distributional re-composition of human writing* — an LLM's output is a sample from a distribution learned over human text, so reader perception of AI text is perception of human text viewed through a statistical mirror.

**C2 (empirical, pre-registered):** Perceived humanness of a text correlates with its *statistical proximity* to the human-training distribution: texts closer to the training manifold read as more human; texts that approximate-but-miss the manifold trigger the uncanny/detrust response (the "human-like but not human" pattern the user identified); texts detectably outside the manifold are judged synthetic.

**Falsifiability (KIF-60):** If, in a controlled reader experiment, perceived-humanness ratings do NOT track measured distributional proximity (holding topic/style constant), C2 is falsified. Pre-registration + falsifiability condition + surprise accounting to be produced in Phase 4.

---

## Phases with WBS

| Phase | WBS | Deliverable | Gate |
|---|---|---|---|
| 0 | QNFO.RES.002.P0 | Project init (this commit) | P1–P11 HARD pass |
| 1 | QNFO.RES.002.P1 | Due diligence: KG + D1 + Vectorize + external cross-ref | `artifacts/consilience-gate.md` with Silo Cost table (KIF-29) |
| 2 | QNFO.RES.002.P2 | Literature: 8-source sweep (post-2023 wave + detection + authorship) | Mandatory Symmetry Template both sections present (KIF-18) |
| 3 | QNFO.RES.002.P3 | Citations: P3.AUTHOR-GATE verify every DOI | `artifacts/citation-audit.md`, zero fabricated entries |
| 4 | QNFO.RES.002.P4 | Deep research: pre-registered C2 test design + calibration register | KIF-60 Δlog-odds ≥ 0 with pre-registration evidence |
| 5 | QNFO.RES.002.P5 | Publication: `<slug>.md` + PDF (CDP pipeline) + Zenodo DOI | AI-QUALITY-GATE-1 + TITLE-DUPLICATION-1 + P5 gates |
| 6 | QNFO.RES.002.P6 | Deploy: D1 living-paper + papers-server + MCP verification | `papers.qnfo.org/papers/<slug>/` HTTP 200 |
| 7 | QNFO.RES.002.P7 | Disseminate: journal submission + outreach + PhilPapers keywords | Journal shortlist + outreach log |
| 8 | QNFO.RES.002.P8 | Distribute: GitHub tag + Zenodo newversion + R2 archive + D1/KG records | All 4 core layers verified |

---

## Milestones

| Milestone | Criteria |
|---|---|
| M0 (this commit) | Branch pushed, PROJECT-PLAN.md committed, tag v0.1-phase0 |
| M1 | Consilience gate passed — silo-cost table shows perception-vs-NLP silo cost ≥ 8 yr |
| M2 | 8-source sweep complete; ≥ 20 unique sources; post-2023 wave covered |
| M3 | All citations live-verified; 0 fabrication flags |
| M4 | C2 pre-registered with falsifiability condition + surprise accounting |
| M5 | Paper published with DOI; AI-QUALITY-GATE-1 cleared |

---

## Deliverable Registry

| ID | Deliverable | Path | Owner |
|---|---|---|---|
| R1 | Project plan | `PROJECT-PLAN.md` | agent |
| R2 | Consilience gate record | `artifacts/consilience-gate.md` | agent |
| R3 | External search evidence | `artifacts/external-search/*.json` | agent |
| R4 | Citation audit | `artifacts/citation-audit.md` | agent |
| R5 | Paper markdown | `ai-text-perception.md` | agent |
| R6 | Paper PDF | `ai-text-perception.pdf` | agent |
| R7 | Research-continuity registry | `artifacts/RESEARCH-CONTINUITY-REGISTRY.md` | agent |

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Literature already covers "AI text perception" densely | HIGH | MED | Novelty rests on the *synthesis-from-human-writing* framing + C2 proximity prediction, not on re-verifying known label effects |
| No direct empirical study of uncanny valley in long-form prose | MED | LOW | State explicitly; nearest evidence (poetry/abstracts/chatbots) is the honest boundary |
| P3.AUTHOR-GATE fabrication risk (author/DOI hallucination) | MED | HIGH | Live Crossref/OpenAlex verification per entry; three-count audit |
| Confirmation bias from QNFO-internal hits | MED | MED | Vectorize disclosure `[CONFIRMATION-BIAS-RISK]` if all hits internal; external search mandatory |
| Köbis-style misattribution (label vs content) | MED | HIGH | Red-team claim-to-evidence pass at P4 (canonical lesson from this session) |

---

## Success Criteria

1. Paper published with DOI (Zenodo), files slug-named, AI-QUALITY-GATE-1 cleared.
2. ≥ 20 verified external sources; every DOI live-verified.
3. C2 pre-registered with falsifiability condition; Δlog-odds computed.
4. QNFO corpus anchor (*Strange Loop of Being* — "digital uncanny") integrated as internal evidence.
5. Research-continuity registry populated with frontier questions.
