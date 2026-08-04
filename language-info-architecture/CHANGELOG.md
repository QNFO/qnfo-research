# CHANGELOG: Language-Info-Architecture

---

## 2026-05-12 (Session 9) — Project Rename

**What Changed:**
- Renamed project from "Word Cross-Ratio" to "Language-Info-Architecture"
- `git mv "Word Cross-Ratio" "Language-Info-Architecture"` — all 23 tracked files migrated
- Updated all internal path references in Python pipelines (0.3.py, 0.5.0.py, 0.7.0.py)
- Updated repository paths in preprint (0.12.0.md) and README.md
- Updated all 7 documentation file headers to reflect new name
- Historical references in CHANGELOG and DECISIONS preserved (documenting actions under the original name)

**Rationale:** The project is no longer primarily about word-frequency ratios; it is an investigation of language as information architecture. The name should describe what the project became, not what it started as.

**Git:** feature/consolidate-cross-ratio-convergence

---

## 2026-05-12 (Session 7) — Standalone Preprint

**What Changed:**
- Created `0.12.0.md`: Full-text standalone academic preprint (~8,000 words, 12 sections including appendix)
- Synthesizes entire project trajectory: Sapir-Whorf reframing → information architecture → 6 RQs → mutual exclusion → cross-project bridge
- Structured as publishable preprint: Abstract, Introduction, Theoretical Framework, Methods, Results (6 subsections), Discussion, Conclusion, References, Appendix
- Honest about synthetic data limitations; methodological contribution emphasized over empirical claims
- Updated PROJECT STATE.md and SPRINT.md

**Key Sections:**
- §1: Introduction — the problem with frequency-based relativity, the reframing
- §2: Theoretical Framework — Jakobson, Shannon, Grice, Greenberg
- §3: Methods — 22 languages, synthetic data, 8 domains, PCA, permutation tests
- §4: Results — entropy gradient, mandatory architecture, compression-tax trade-off, mutual exclusion ($p<0.0001$), scientific register, design space mapping
- §5: Discussion — candidate universal, substitution vs. complementarity, register additivity, limitations
- §6: Conclusion
- Appendix: Cross-Project Bridge — Shannon entropy as invariant under recoding

**Git:** feature/consolidate-cross-ratio-convergence

**What Changed:**
- Created `0.11.0.md`: Project Retrospective — full arc from Sapir-Whorf to Cross-Ratio Convergence
- Rewrote `README.md` to reflect final state
- Updated PROJECT STATE.md to mark COMPLETE
- Updated SPRINT.md (Task 6: Capstone DONE, Task 5: DEFERRED)
- Updated CHANGELOG.md (this entry)
- **Project is complete.** Branch `feature/consolidate-cross-ratio-convergence` ready for review and merge.

**Key Points:**
- 3 phases: Sapir-Whorf (null) → Information Architecture (6 findings) → Paths A+B+C (deepening, extension, bridge)
- 14 versioned files, 7 documentation files
- All findings depend on synthetic data — methodology is sound, numbers are illustrative
- Real-data validation (WALS, corpora) is the necessary next step
- Cross-project bridge established: Shannon entropy as invariant under recoding

**Git:** feature/consolidate-cross-ratio-convergence → Ready for merge

---

## 2026-05-12 (Session 5) — Paths A+B+C: Deepening, Extension, Cross-Project Synthesis

**What Changed:**
- Created `0.7.0.py`: Combined Path A+B pipeline — mutual exclusion + scientific register
- Created `0.7.0_results.json`: Path A+B results
- Created `0.8.0.md`: Path A writeup — The Mutual Exclusion Principle (10 zero pairs, $p<0.0001$, 4 mandatory clusters)
- Created `0.9.0.md`: Path B writeup — Scientific Register Comparison (epistemic convergence 8.8x, no entropy convergence)
- Created `0.10.0.md`: Path C writeup — Cross-Project Synthesis (Shannon entropy as invariant under recoding, bridge to Cross-Ratio Convergence)
- Updated PROJECT STATE.md, SPRINT.md, CHANGELOG.md, DECISIONS.md, LEARNINGS.md

**Key Findings:**
- **Path A:** Expanded from 4 to 8 mandatory domains. 10 of 28 pairs empty. Global permutation test $p < 0.0001$. Four mutually exclusive mandatory clusters identified: reference-tracking, source-tracking, categorical-judgment, spatial-coordinate.
- **Path B:** Scientific registers across 8 languages show epistemic convergence (all ~2.5%) but no entropy convergence. Epistemic load increases 8.8x in scientific register. Total mandatory load rises additively — register convention does not respect grammatical mutual exclusion.
- **Path C:** Shannon entropy is invariant under recoding, structurally analogous to the geometric cross-ratio (invariant under projective transformations). Mutual exclusion principle is a linguistic no-go theorem. Design space boundaries are linguistic phase boundaries. Proposal: re-include Word Cross-Ratio in Cross-Ratio Convergence synthesis.

**Git:** feature/consolidate-cross-ratio-convergence

---

## 2026-05-12 (Session 4) — Complete Reframing: Language as Information Architecture

**What Changed:**
- Created `0.5.0.md`: Reframed research plan — Jakobson/Shannon/Grice/Greenberg framework
- Created `0.5.0.py`: Reframed analysis pipeline — entropy, mandatory architecture, design space
- Created `0.5.0_results.json`: Reframed results — machine-readable
- Created `0.6.0.md`: Comprehensive results writeup with 6 key findings
- Updated PROJECT STATE.md, SPRINT.md, CHANGELOG.md, DECISIONS.md, LEARNINGS.md

**Theoretical Shift:**
- From: Sapir-Whorf (psychology: "does frequency cause cognitive effects?")
- To: Jakobson/Shannon/Grice/Greenberg (communication: "what mandatory information do languages force into the channel?")

**Key Findings:**
1. Entropy gradient: isolating (6.48 bits) → polysynthetic (6.80 bits/word)
2. Compression-tax trade-off: r = -0.484 (richer morphology → lower mandatory loads)
3. Mutual exclusion: 0 languages with both obligatory epistemic AND ontological marking
4. Design space: PCA maps 2 empty quadrants — genuine typological constraints
5. Gricean surplus: German (+4.8%), Arabic (+4.6%), Russian (+4.3%) most over-informative
6. Per-morpheme entropy reverses: isolating (5.90 bits/morpheme) > polysynthetic (1.70 bits/morpheme)

**Git:** feature/consolidate-cross-ratio-convergence

---

## 2026-05-12 (Session 3) — Simulation Executed & Results Documented

**What Changed:**
- Created `0.3.py`: 7-phase Bayesian simulation pipeline (~44K Python)
- Created `0.3_results.json`: Full machine-readable results (~206K JSON)
- Created `0.4.md`: Comprehensive results writeup (~22K words)

**Key Findings:**
- All 22 languages analysed; MCMC convergence perfect (all R-hat < 1.05)
- Morphological type explains 39% of Zipf exponent variance
- Crossed-effects model: P(agglutinative < fusional) = 0.80
- Meta-regression null result: beta1 = -0.020, HDI [-0.158, 0.108]
- 4/8 pre-registered evaluation criteria passed

**Git:** feature/consolidate-cross-ratio-convergence

---

## 2026-05-12 (Session 2) — State Cleanup & Plan Refinement

**What Changed:**
- Fixed branch discrepancy in PROJECT STATE.md
- Created `0.1.2.md`: Refined research plan addressing all 13 gaps
- Added Quechua & Tibetan to language sample (22 languages)

**Git:** feature/consolidate-cross-ratio-convergence

---

## 2026-05-12 — Documentation Bootstrap

**What Changed:** Created all 7 standard project documentation files.
**Git:** feature/root-cleanup-and-agenda-review

---

## Pre-2026-05-11 — Research Plan

**What Changed:**
- `0.1.md` created: Initial inquiry with extensive LLM web search
- `0.1.1.md` created: Formal Bayesian cross-linguistic research plan
