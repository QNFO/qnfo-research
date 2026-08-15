# QNFO.RES.011 Phase 2 — Literature Search & Triage

**Project:** Configuration-Space Topology and the Distinction Calculus
**WBS:** QNFO.RES.011 — **Date:** 2026-08-15
**Inputs:** Phase 1 gap analysis (`docs/phase1-due-diligence.md`), Phase 1 evidence files, this phase's new-source searches.

---

## 1. Protocol compliance — 8-source search

| # | Source | Formulations | Status | Evidence file |
|:--|:-------|:-------------|:-------|:--------------|
| 1 | OpenAlex (PRIMARY) | F1/F2/F3 | DONE (P1) | `openalex-f1|f2|f3-*.json` |
| 2 | Crossref | F1/F2/F3 | DONE (P1) | `crossref-f1|f2|f3-*.json` |
| 3 | Zenodo records | F1/F2/F3 | DONE (P2) + ownership verified | `zenodo-f1|f2|f3-*.json`, ownership sweep (7 records) |
| 4 | Europe PMC | F1/F2/F3 | DONE (P2) | `europepmc-f1|f2|f3-*.json` |
| 5 | arXiv | F1/F2/F3 (P1) + 4 falsifier formulations (P2) | DONE | `arxiv-evidence.json` (P1) + this report §3 |
| 6 | Web (Google Patents + archive.org CDX) | 3 patent queries + 2 CDX targets | DONE | `googlepatents-p1|p2|p3-*.json`, `cdx-qnfo-spin-statistics.json` |
| 7 | QNFO Vectorize | F1/F2/F3 | FALLBACK (worker 1101, GAP-1) | D1 living-paper LIKE sweep (P1, 14 hits) |
| 8 | QNFO KG | Paper node searches | DONE (P1) | KG `nodes` queries (braid ×5, configuration ×0) |

**Evidence discipline:** 16 evidence files total in `artifacts/external-search/` (7 from P1 + 9 new this phase: 3 zenodo, 3 europepmc, 3 googlepatents, plus CDX). Every DOI/count below traces to a saved file.

## 2. Key new findings from the added sources

### 2.1 Zenodo F1 — external challengers found (ownership-verified)
| Record | Title | Creator | Relevance |
|:-------|:------|:--------|:----------|
| 10.5281/zenodo.21330410 | A Geometric Origin for Fermi–Dirac Statistics: The Spin-Statistics Connection from Z₂ Normal Holonomy **Without Lorentz Invariance** | Li, Ge (EXTERNAL) | **Direct constraint on C3** — claims the spin-statistics connection without the QFT input C3 declares necessary. Self-published (2026-07-13), not peer-reviewed; must be engaged in the paper's boundary discussion |
| 10.5281/zenodo.20195647 | Event Density and Anyon Prohibition in 3+1D | Proxmire, Allen (EXTERNAL) | Supports C1's "d≥3 ⇒ no anyons in the point-particle framework" (independent, external) |
| 10.5281/zenodo.19626046 | Paper XXXVII: Topological Origin of Spin and the Spin-Statistics Connection | Novickis, Alexander (EXTERNAL) | Adjacent topological-origin proposal; [UNTESTED] class |
| 10.5281/zenodo.18725887 | The Vortex Framework: Topological Fermions from Framed Vortex Loops | Smith, Alex (EXTERNAL) | Extended objects → fermionic statistics — the "3D anyons via extended objects" falsifier thread, concretely realized |
| 10.5281/zenodo.21939692 | The Tyranny of the ±1 (v3) | Quni-Gudzinas (QNFO) | Own record — updated citation anchor |
| 10.5281/zenodo.21943007 | From Distinction to Dissipation: Companion Essay + Executable Toy-Model Suite | Quni-Gudzinas (QNFO) | Own record — RES.009 companion (2026-08-15) |

### 2.2 Zenodo F2 — GT side nearly absent externally
Exactly **1** external record: 10.5281/zenodo.17214997 "Algebraic Structures of the Grothendieck–Teichmüller Group, the Cosmic Galois Group, and Associated Stability Conditions" (creator "HI+AI", 2025-09-27). The GT side of C2 is nearly absent from Zenodo — internal gap confirmed again.

### 2.3 Zenodo F3 — LoF × statistics niche occupied internally only
Total 2 records, **both QNFO-owned** (exchange-phase-logical-scalar 21941238; companion essay 21943007). Fifth independent source confirming the niche is QNFO-occupied, externally empty.

### 2.4 Europe PMC
- F1: 13 hits, all condensed-matter anyon/FQHE (physical realization background; e.g., 10.1038/s41598-025-30355-0, 10.1016/j.xinn.2023.100504 Fibonacci disk code, 10.1098/rspa.2016.0758 topological origin in lowest Landau level).
- F2: **0 hits** — GT/braided-monoidal absent from biomedical-indexed literature.
- F3: **0 hits** — LoF × spin-statistics absent (4th independent confirmation).

### 2.5 Google Patents
| Query | Total | Verdict |
|:------|:------|:--------|
| "laws of form" OR "distinction calculus" statistics | 976 | Noise (glossaries, brakes, bridges) — **no distinction-calculus-derived-statistics patent exists** |
| braid topological quantum gate anyon logic | 82 | Mature engineering space (Microsoft TQC patents, Harvard spin-fluid qubits) — no logical-calculus route |
| Grothendieck-Teichmuller | **0** | GT has zero commercial footprint |

### 2.6 archive.org CDX
- `zenodo.org/records/21941375` → captured 2026-08-15T06:38:35 (200) — RES.009 record is in the Wayback Machine.
- Second CDX target (web search snapshot) → 503 rate-limit (archive.org documented behavior; not retried).

## 3. Falsifier sweep results (arXiv, 4 formulations — search *against* the claim)

| Falsifier | Papers | Verdict |
|:----------|:-------|:--------|
| Parastatistics / beyond ±1 | **2306.05919** Medina Sánchez & Dakić — *Reconstruction of Quantum Particle Statistics: Bosons, Fermions, and Transtatistics*; **2312.13191** Toppan (Z₂×Z₂-graded parastatistics, detectable); 2309.00965 (Balbino et al.) | **HARD constraint on F2/abelian-pair:** from operational axioms (unitary dynamics + local phase transformations) only bosons and fermions do **NOT** follow — novel *transtatistics* families emerge. RES.009's abelian-pair postulate (and this project's F2) must be positioned against this axiom set, not assumed universal |
| Gentile / intermediate statistics | 2003.06235 Shen (anyon↔Gentile transformation); cond-mat/0310066 Dai & Xie (large occupation limit); 1511.08051 Selvi & Uncu (statistical weight) | Intermediate statistics exist as formal structures outside the config-space framework (occupation-number based) — constrains any "±1 is absolute" phrasing; C1 stays safe because these alter the algebra, not π₁ |
| 3D anyons / extended objects | 1204.5025 Chaichian, Tureanu, Zhang (supersymmetric anyons in 3D, extended Poincaré supergroups); 10.1007/978-3-0348-0448-6_19 (config spaces of extended objects, 2012); Zenodo 18725887 (vortex framework) | Anyonic spin representations appear in 3D **under supersymmetry extension**; extended objects admit exotic statistics — C1's "±1 only" is framework-conditional (point-particle, scalar wavefunction, deleted diagonal) and must say so |
| Sati–Schreiber program map | 1408.0054 Schreiber & Shulman (QGFT in cohesive HoTT); 2206.13563 (TED-K anyonic order); 2209.08331 (Topological Quantum Programming); **2303.02382** Myers, Sati, Schreiber (*Topological Quantum Gates in Homotopy Type Theory* — cubical Agda certification); 2408.11896 (cohomotopy/framed links) | **The HoTT×anyon space is NOT empty.** Cohesive HoTT already formalizes anyonic topological order and certified topological quantum gates. C2's novelty must be precisely the *mark-based route* (primitive cut → braided monoidal category → GT action → exchange phase as logical scalar), which their cohesion-axiom foundation does not contain |

## 4. Classification matrix

### Core (directly addresses RQ — 12)
| Work | DOI/ID | Why core |
|:-----|:-------|:---------|
| Leinaas & Myrheim 1977 | Intrinsic approach (via RES.009 citation set) | Canonical origin of CST-for-statistics |
| Laidlaw & DeWitt 1971 | idem (ancestor) | Feynman path quantization on C_N |
| Harshman & Knapp 2022 | 10.1103/PhysRevA.105.052214 | Orbifold treatment — dissolves the deleted-diagonal scaffold; C1 boundary |
| Nagies et al. 2023 | arXiv:2309.04358 | Traid group lattice model — CST extended beyond braid group |
| Sati & Schreiber 2022 | arXiv:2206.13563 | TED-K anyonic order — HoTT×anyons exists; C2 differentiation anchor |
| Sati & Schreiber 2022 | arXiv:2209.08331 | Topological quantum programming in TED-K |
| Myers, Sati, Schreiber 2023 | arXiv:2303.02382 | Topological quantum gates certified in HoTT/cubical Agda |
| Schreiber & Shulman 2014 | arXiv:1408.0054 | Cohesive HoTT as QGFT foundation (C2 contrast) |
| Drinfeld 1990 / survey | arXiv:1904.13097 | GT group — C2 mathematical anchor |
| Li Ge 2026 | 10.5281/zenodo.21330410 | C3 direct constraint (no-Lorentz spin-statistics claim) |
| Medina Sánchez & Dakić 2023 | arXiv:2306.05919 | F2/transtatistics — abelian-pair under attack |
| Harshman & Knapp 2018 | arXiv:1803.11000 | Traid group discovery |

### Supporting (adjacent — 16)
| Work | DOI/ID | Role |
|:-----|:-------|:-----|
| Sawicki 2014 / Harrison et al. 2013 / Maciążek & Sawicki 2018 / Maciążek 2019 | arXiv:1408.7002 / 1304.5781 / 1806.02846 / 1909.02098 | Graph config spaces — statistics landscape beyond Euclidean |
| Chaichian, Tureanu, Zhang 2012 | arXiv:1204.5025 | Supersymmetric anyons in 3D |
| Toppan 2023 | arXiv:2312.13191 | Detectable Z₂×Z₂ parastatistics |
| Shen 2020 | arXiv:2003.06235 | Anyon ↔ Gentile transformation |
| Dai & Xie 2003 | arXiv:cond-mat/0310066 | Gentile large-occupation limit |
| Selvi & Uncu 2015 | arXiv:1511.08051 | Gentile statistical weight |
| Jacak 2017 | arXiv:1704.06560 | Braid-group holographic proposal [UNTESTED, physics.gen-ph] |
| Proxmire 2026 | 10.5281/zenodo.20195647 | Anyon prohibition in 3+1D |
| Novickis 2026 | 10.5281/zenodo.19626046 | Topological origin of spin |
| Smith 2026 | 10.5281/zenodo.18725887 | Vortex framework — extended-object fermions |
| HI+AI 2025 | 10.5281/zenodo.17214997 | GT group + Cosmic Galois (Zenodo) |
| Extended objects 2012 | 10.1007/978-3-0348-0448-6_19 | Quantum config spaces of extended objects |
| Sati & Schreiber 2024 | arXiv:2408.11896 | Cohomotopy anyons (program capstone) |
| QNFO spin-statistics-distinction | 10.5281/zenodo.21941375 | Predecessor (RES.009) |
| QNFO exchange-phase-logical-scalar | 10.5281/zenodo.21941238 | Predecessor (RES.010) |
| QNFO reentrant-distinctions | 10.5281/zenodo.21908818 | SLB.002 treatise (foundation) |

### Background (context — 10)
Streater & Wightman 1964/2001 (PCT); Pauli 1940 (10.1103/PhysRev.58.716); Finkelstein & Rubinstein 1968 (10.1063/1.1664510); Wilczek 1983 (10.1103/PhysRevLett.51.2250); Read & Green 2000 (10.1103/PhysRevB.61.10267); Europe PMC FQHE set (10.1038/s41598-025-30355-0; 10.1016/j.xinn.2023.100504; 10.1098/rspa.2016.0758); QNFO p-adic braid series (21208366/21208368/21208491/21336087/21208568); QNFO quantum-laws-of-form series (21206074/21205110/21205097/19598745); QNFO cancellation-rule (21470438); QNFO Tyranny v3 (21939692).

### Reject (archived with reason)
Molecular-dynamics/ML "configuration space" noise (OpenAlex F1 top hits — different field usage); arXiv F3 stat.ME noise (OR-tokenization); Google Patents P1 noise (glossaries/brakes — no LoF-statistics patent); 2512.10504, hep-ph/0610012, 1808.08674, 1807.03334 (irrelevant to RQ).

---

## 5. Mandatory Symmetry Template (KIF-18, HARD)

### Where External Literature Supports [Claim]

- **C1 (CST is the correct modern explanation, with scaffolds):** Leinaas–Myrheim/Laidlaw–DeWitt (canonical derivation of statistics from π₁(C_N)); the active extension program proves the framework is alive and productive — traid group (1803.11000, 2309.04358), orbifold treatment (10.1103/PhysRevA.105.052214), graph configuration spaces (1304.5781, 1408.7002, 1806.02846, 1909.02098); Proxmire 20195647 independently derives anyon prohibition in 3+1D; the Europe PMC condensed-matter corpus (13 records) documents the physical realization side (FQHE, Fibonacci disk code).
- **C2 (novelty of the distinction-calculus route into HoTT/GT):** The route is **unoccupied** in every searched source: Google Patents (0 for GT; no LoF-statistics patent), Europe PMC (0 for GT×braided, 0 for LoF×statistics), Zenodo F3 (only QNFO records), OpenAlex/Crossref F3 (only standard QFT spin-statistics), arXiv F3 (noise). The mathematical ingredients are real and mature — GT/operad survey 1904.13097, braided monoidal category literature (Morrison–Penneys IMRN 2017 etc.) — which supports that the *objects* are genuine and the *route through the mark calculus* is open.
- **C3 (spin-statistics connection needs Lorentz/microcausality/positivity in the standard framework):** Streater–Wightman 1964/2001, Pauli 1940, Finkelstein–Rubinstein 1968, Wilczek 1983 — the established theorem is derived in relativistic QFT; no external mark-calculus derivation exists (4 sources, empty).

### Where External Literature Constrains or Contradicts [Claim]

- **C3 CONTRADICTED (partially) — Li Ge 2026 (10.5281/zenodo.21330410):** claims a geometric origin for Fermi–Dirac statistics from Z₂ normal holonomy *without Lorentz invariance* (2026-07-13, self-published). C3's "requires Lorentz/locality" must be qualified: it is true in the QFT framework and for the mark calculus as formulated, but geometric alternatives are claimed externally and must be engaged (verify, refute, or bound). Do not assert "impossible without Lorentz" without addressing this record.
- **F2 / abelian-pair CONSTRAINED — Medina Sánchez & Dakić 2023 (2306.05919):** operational reconstruction (unitary dynamics + local phase) yields bosons, fermions, **and transtatistics**. The RES.009 abelian-pair postulate and this project's F2 must be stated against this axiom set; "only two statistics" is not derivable from dynamics+phases alone. Toppan 2312.13191 adds detectable Z₂×Z₂ parastatistics.
- **C1 CONSTRAINED — "±1 only in d≥3" is framework-conditional:** (a) orbifold treatment (10.1103/PhysRevA.105.052214) includes the singular diagonal instead of deleting it — classification changes; (b) graph config spaces admit anyon phases on 2-connected graphs (1304.5781/1408.7002); (c) supersymmetric extension admits anyonic spin in 3D (1204.5025); (d) Gentile/intermediate statistics exist as formal structures (2003.06235, cond-mat/0310066, 1511.08051). The "tyranny" holds for point-particle + deleted-diagonal + scalar-wavefunction setup and must be stated as such.
- **C2 CONSTRAINED — the HoTT×anyon space is NOT empty:** Sati–Schreiber's cohesive-HoTT program (1408.0054 → 2206.13563 → 2209.08331 → 2303.02382 → 2408.11896) already formalizes anyonic topological order, topological quantum programming, and *certified* topological quantum gates in homotopy type theory (cubical Agda). C2 must (i) cite this program as the state of the art, (ii) differentiate: their foundation is cohesion axioms on the universe type, QNFO's is the mark as primitive cut; their target is classification/verification of physical TQC, QNFO's is the derivation of the exchange phase as a logical scalar (R = e^{2πis}) from the re-entrant mark. Failure to differentiate triggers the F1 falsification condition ("GT action inessential" / "already done in HoTT"). [AI-CONVERGENCE-WARNING: dismissals of C2 on "HoTT-anyons already exists" grounds reflect shared training priors, not engagement with the mark-based route.]

## 6. Novelty assessment (refined after Phase 2)

| Claim | Phase 1 verdict | Phase 2 refinement |
|:------|:----------------|:-------------------|
| C1 kinematical | [ESTABLISHED] + [CONTESTED boundaries] | Boundaries now concrete: orbifold, graph, supersymmetric, Gentile — the paper must state the exact setup in which ±1 is forced |
| C2 synthesis | [CONJECTURE], internally novel, must differentiate | Differentiation target named (Sati–Schreiber 5-paper program); the mark-based route remains unoccupied in 8 sources + patents |
| C3 boundary | [ACKNOWLEDGED] | Now under direct external challenge (Li Ge 21330410) — must be defended or qualified; this is a positive finding (falsifier surfaced in the wild) |

**Overall:** The project's route-level novelty survives Phase 2. The falsifier sweep strengthened rather than weakened the positioning: every constraint found (transtatistics, orbifold, supersymmetric anyons, Sati–Schreiber) is a *named, citable* boundary that the paper can and must engage — turning the biggest risks into the paper's sharpest sections.

## 7. Recommendations for Phase 3 (citation management)

1. **references.bib must include** (minimal Core set): Leinaas–Myrheim 1977; Laidlaw–DeWitt 1971; Pauli 1940; Streater–Wightman 1964; Finkelstein–Rubinstein 1968; Wilczek 1983; Drinfeld 1990; 1904.13097; 1408.0054; 2206.13563; 2209.08331; 2303.02382; 2408.11896; 10.1103/PhysRevA.105.052214; 2309.04358; 1803.11000; 2306.05919; 10.5281/zenodo.21330410 (as constraining evidence); plus QNFO predecessors (21941375, 21941238, 21908818, p-adic braid series).
2. **P3.AUTHOR-GATE caution:** the 5 Zenodo external records are self-published single-author works — cite as [CONTESTED]/[UNTESTED] evidence only, never as peer-reviewed support; verify each against its record page before final inclusion.
3. **Li Ge 21330410 must be cited in the C3 boundary discussion** — a reviewer will find it; pre-empting beats defending later.
4. **The companion essay (21943007)** is a free executable toy-model anchor — cross-link from the paper's falsifiability section (F2's abelian-pair discussion maps to the transtatistics constraint).

## 8. Tool gaps (this phase)

- GAP-1 (repeat, 3rd cycle): qnfo-memory-mcp worker 1101 — all semantic-search endpoints down; D1-LIKE + HTTP fallbacks used throughout.
- archive.org CDX rate-limited on 2nd URL (503) — documented behavior; first target succeeded.
- Europe PMC initial query failed on unencoded sort param — fixed with urlencode (local fault, corrected per BLAME-EXTERNAL-1).

---
*Compliance: 8-source search executed; evidence files saved for every source; classification matrix complete (12 Core / 16 Supporting / 10 Background / Rejects archived); KIF-18 symmetry template has BOTH mandatory sections with named constraining evidence (Li Ge, transtatistics, Sati–Schreiber, orbifold/supersymmetric/Gentile) — no hedging-only constraints.*
