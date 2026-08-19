# WBS: QNFO.RES.017

# PROJECT-PLAN — Trapped-Ion Ultrametric Testbed Synthesis

**Program:** QNFO.RES (QNFO Research Archive) · **Repo:** QNFO/qnfo-research · **Branch:** res/paper/trapped-ion-ultrametric-synthesis
**Status:** Phase 0 (Init) — 2026-08-19

## Charter

Synthesize sixteen published QNFO records (2025-12-02 → 2026-08-18) into a single convergent
research program with one falsifiable core claim: **trapped-ion quantum simulators are the first
near-term platform on which ultrametric (p-adic/adelic) structure in quantum physics becomes an
experimentally testable hypothesis; passive, dissipation-structured hardware architectures are
the practitioner embodiment of that structure; and the methodology records supply the
falsifiability discipline that separates testable claims from reified ones.** The synthesis must
add a structural claim that exists in no single input record (Success Criterion SC1).

## Core Claim (P6 — LOCKED at Phase 0)

Sixteen records spanning nine months form one program, not sixteen papers. The program asserts:

1. **Testability movement.** Trapped-ion simulators can falsify ultrametric structure on
   near-term hardware: (i) the Page–Wootters ultrametricity protocol (8-week timeline, UVR
   observable: 0% for diagonal clock-rest coupling vs ~32% for nondiagonal;
   10.5281/zenodo.21120469); (ii) the 2-adic Zitterbewegung frequency deviation √2·2mc²/ħ
   (41.4% from the Archimedean value; 10.5281/zenodo.21600628); (iii) Bruhat–Tits hierarchical
   structure of local-Hamiltonian dynamics as the working explanation of tensor-network
   supremacy (10.5281/zenodo.21820137).
2. **Architectural movement.** The passive-design records (GKP autonomous dissipative
   stabilization, 10.5281/zenodo.17794233; Spin-Free Substrate, 10.5281/zenodo.20411697;
   Quantum Architectonics, 10.5281/zenodo.18522367) propose that hierarchical, reservoir-
   structured stabilization is the hardware embodiment of the same tree structure — the
   ultrametric reading of "passive path to scale."
3. **Methodological movement.** The falsifiability-crisis (10.5281/zenodo.21791457),
   reification (10.5281/zenodo.19605446), and Shor-as-artifact (10.5281/zenodo.21993655)
   records supply the discipline: every structural claim is MAP-labeled unless it carries a
   pre-registered falsifiability condition.

## Premise-Depth Disclosure (where the premises END)

Derived layer (this paper's arithmetic): protocol resource counts, fidelity arithmetic
(6 Mølmer–Sørensen gates/simulated-second at 96.9%), d_eff Monte-Carlo extractions, ZBW
frequency algebra. Named imported inputs (cited, not re-derived):
- (a) Sufficient Condition Theorem / Bridge Theorem: diagonal clock-rest coupling ⇒ exact
  ultrametric conditional-state overlaps; connects Page–Wootters states to Bruhat–Tits
  buildings [MAP — imported from 10.5281/zenodo.21120469 + its antecedents];
- (b) Silent Parameter Principle: truncated SU(2) representation ring ≅ Z₂ˣ character ring
  [MAP — imported from 10.5281/zenodo.21600628];
- (c) Ostrowski place-democracy applied to local-Hamiltonian dynamics [MAP];
- (d) Fisher's Posner hypothesis [external input, 10.5281/zenodo.20411697].
The synthesis claim itself is structural: the three movements are the SAME tree-shaped
hierarchy seen from experiment, engineering, and methodology. That identity claim is labeled
[TERRITORY] only where a falsifiability condition is stated (below); elsewhere [MAP].

## Falsifiability Conditions

1. UVR measurement contradicting 0%/32% split (would falsify the Sufficient Condition
   Theorem's experimental bearing).
2. Measured ZBW frequency ratio ≠ √2 within error (falsifies the 2-adic observable claim).
3. d_eff(p) scaling failing to grow with p (falsifies the fractal-trap reading).
4. GKP passive stabilization failing to reach break-even where the cooling/heating ratio
   exceeds π (falsifies the dissipative-architecture claim).
5. Tensor-network advantage persisting under nonlocal perturbations of the Hamiltonian
   (falsifies the Bruhat–Tits reading).

## Phases (WBS) and Milestones

| Phase | Content | Gate | Milestone |
|:------|:--------|:-----|:----------|
| P0 | Init: branch, scaffold, plan, core-claim lock | Pre-Flight P1–P11 | M0 (this commit, tag v0.1-phase0) |
| P1 | Due diligence: DUE-DILIGENCE-DEPTH-1 full-corpus sweep; KIF-29 consilience; KIF-60 Bayesian weight | artifacts/consilience-gate.md + artifacts/bayesian-evidential-weight.md + external-search evidence files | M1 |
| P2 | Literature: 8 sources, dedup, KIF-18 symmetry template | Mandatory Symmetry Template both sides | M1 |
| P3 | Citations: BibTeX verified live (P3.AUTHOR-GATE) | artifacts/citation-audit.md | M1 |
| P4 | Deep research: structured forecast, gap analysis, SO-WHAT prose, premise-depth, practitioner section | SO-WHAT-GATE-1 + PRACTITIONER-RELEVANCE-1 | M2 |
| P5 | Publication: slug-named .md/.html/.pdf, BP gates, Zenodo deposit | doi.org HEAD 200 + DataCite findable; placeholder-DOI file check | M3 |
| P6 | Deployment: D1 living-paper row, KG node, Vectorize index | resolve_paper_id + chunks>0 | M4 |
| P7 | Dissemination: Buffer, SEO, papers.qnfo.org | post-ID verification | M4 |
| P8 | Core Distribution: R2 mirror (qnfo-releases), GitHub tag, closeout verification, post-publication adversarial analysis | R2 bucket listing + red-team aggregate | M4 |

## Deliverable Registry

trapped-ion-ultrametric-synthesis.md/.html/.pdf · references.bib · citation-audit.md ·
PROJECT-PLAN.md · README.md · docs/deep-research.md · artifacts/consilience-gate.md ·
artifacts/bayesian-evidential-weight.md · artifacts/uia-ignorance-audit.md ·
artifacts/external-search/* (all evidence files) · GitHub provenance via related_identifiers.

## Risk Register

| ID | Risk | Mitigation |
|:---|:-----|:-----------|
| R1 | Synthesis degenerates into a record listing (no new thesis) | Single-thesis structure mandated; every section serves the core claim; SC1 |
| R2 | Imported theorems over-claimed as derived | Premise-depth disclosure; MAP/TERRITORY labels; check-map-territory.py build gate |
| R3 | Vectorize 1101 at limit>=20 | Retry at limit<=16 (VECTORIZE-TOP-K-50-1); 12/12 formulations |
| R4 | Zenodo API 403 bot detection | Full Chrome UA + Accept-Language + Referer (ZENODO-BOT-403-1); browser-context fallback |
| R5 | WBS collision with concurrent session | RES.017 row inserted atomically (check-then-insert, changes=1 verified) |
| R6 | Corpus registration gap for the 16 source records | Synthesize from published DOIs (live-verified); register inputs as citation set, not D1 rows |
| R7 | Subagent red-team stall | REDTEAM-QUEUE-STALL-PATIENCE-1: wait ~15 min, then direct parent-agent audit |

## Success Criteria

- SC1: One non-trivial structural synthesis claim absent from any single input record.
- SC2: Every cross-domain correspondence MAP/TERRITORY-labeled; zero unlabeled identity claims (scripted gate exit 0).
- SC3: Practitioner section names ≥1 implementable artifact (demo/SDK/benchmark/spec-sheet/decision tool).
- SC4: Full provenance set in Zenodo deposit + R2 mirror (qnfo-releases) + GitHub related_identifier.
- SC5: Post-publication adversarial analysis executed; HARD findings remediated or logged.
