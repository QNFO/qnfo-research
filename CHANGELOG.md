# CHANGELOG — LLM Force Multiplier

> Chronological versioned change log. One entry per session.

---

## 2026-05-13 — Session: arXiv Preparation & Backlog Cleanup (Sprint 2)

**What Changed:**
- **BACKLOG.md:** 12 items marked DONE (B-003, B-004, B-006, B-008, B-020, etc.), 6 new items added (B-018-B-022), priorities recalculated
- **SPRINT.md:** Sprint 2 defined and completed — arXiv metadata, submission checklist (10 items verified), standalone abstract
- **0.2.md:** arXiv metadata header added (title, authors, abstract char count, subjects, license, repository placeholder)
- **0.2_abstract.md:** Standalone abstract created for arXiv submission form
- **0.2_cover_letter.md:** Journal cover letter template created
- **PROJECT STATE.md:** Updated to reflect Sprint 2 completion

**Files Changed:**
- `BACKLOG.md` — EDIT (comprehensive cleanup)
- `SPRINT.md` — EDIT (Sprint 2 defined and completed)
- `0.2.md` — EDIT (arXiv metadata header)
- `0.2_abstract.md` — CREATE (standalone abstract)
- `0.2_cover_letter.md` — CREATE (cover letter template)
- `CHANGELOG.md` — EDIT (this entry)
- `PROJECT STATE.md` — EDIT (updated status)

**Submission Readiness:**
- All 10 checklist items verified ✅
- Manuscript: 23 pages, 26 references, 3 appendices
- Two independent case studies (physics + linguistics)
- Math formatting scan: PASS
- LLM disclosure: explicit in Acknowledgments

**Git:**
- Branch: `feature/expand-manuscript`
- Commits: 2 (Sprint 2 setup + completion)

---

## 2026-05-13 — Session: Architecture Correction (Post Reader-Test)

**What Changed:**
- **Section 3 complete rewrite:** Replaced aspirational Docker/API/Overleaf stack with actual architecture (unified conversation environment)
- **Section 4.5 added:** Language as Information Architecture as independent second validation case study [26]
- **Section 7.2:** Added "Aspirational Architecture Description" limitation
- **Appendix C:** Renamed to "Dockerfile (Aspirational)" with disclaimer
- **Abstract & Conclusion:** Updated to reference real architecture
- **LEARNINGS.md:** Added L5 (reader-testing) and L6 (describe-real-architecture)

**Root cause:** The original manuscript described a Docker/API/Overleaf toolchain that was never used. The actual production architecture — DeepChat conversation with integrated file I/O, Python execution, and git — was simpler and had already produced two published papers.

**Files Changed:**
- `0.2.md` — EDIT (Sections 3, 4.5, 7.2, 8, Abstract, Appendix C, References)
- `LEARNINGS.md` — EDIT (L5, L6 added)
- `CHANGELOG.md` — EDIT
- `PROJECT STATE.md` — EDIT

**Git:**
- Branch: `feature/expand-manuscript`
- Commit: `278352c`

---

## 2026-05-13 — Session: Reader Test Fixes

**What Changed:**
- Fixed 4 issues found by blind reader test:
  1. Removed 8h experiment cap (contradicted 200h power analysis)
  2. Added sensitivity analysis to power calculations (σ = 40/80/120h)
  3. Harmonized speedup numbers (25× case study, 17× power analysis)
  4. Strengthened n-of-1 self-experiment language

**Files Changed:**
- `0.2.md` — EDIT (Sections 4.4, 5.2, 5.4, 7.2)

**Git:**
- Branch: `feature/expand-manuscript`
- Commit: `21ee39b`

---

## 2026-05-13 — Session: Expand Mini-Paper (Sprint 1)

**What Changed:**
- Created expanded manuscript `0.2.md` (789 lines, ~47K chars)
- Created supporting SymPy script `0.2.py`
- Updated SPRINT.md, PROJECT STATE.md, CHANGELOG.md

**New Content in 0.2.md:**
- §1 Introduction with literature review (14 references)
- §2 Force-Multiplier Framework (task decomposition, verification cycle, prompt engineering)
- §3 Solo-Research Stack (4-layer architecture — later corrected)
- §4 Case Study (hour-by-hour physics walkthrough, speedup table)
- §5 Controlled Experiment Design (3-condition between-subjects, power analysis $[CODE-EXECUTED]$)
- §6 Cross-Domain Generalisation (comp bio, pure math, philosophy)
- §7 Discussion (shifting bottleneck, limitations, ethics)
- §8 Conclusion
- Appendix A: Prompt Library (5 core templates)
- Appendix B: SymPy Derivation (0.2.py standalone)
- Appendix C: Solo-Research Stack (Dockerfile — later corrected to aspirational)
- References (25 citations, expanded to 26)

**Statistical Results $[CODE-EXECUTED]$:**
- Cohen's $f = 1.92$ (very large effect)
- Required $n = 4$ per group for $>99\%$ power
- Speedup factor: $16.7\times$ (Force-Multiplier vs. Solo)

**Files Changed:**
- `0.2.md` — CREATE
- `0.2.py` — CREATE
- `SPRINT.md` — EDIT
- `PROJECT STATE.md` — EDIT
- `CHANGELOG.md` — EDIT

**Git:**
- Branch: `feature/expand-manuscript`
- Commits: 3 (0.2.md, 0.2.py, docs)

---

## 2026-05-13 — Session: Project Documentation Bootstrapping (Sprint 0)

**What Changed:**
- Initialized standalone git repository inside project directory
- Created `feature/init-project-docs` branch
- Created 7 mandatory project documentation files
- Added existing output files to version control

**Files Changed:**
- `README.md` — CREATE
- `PROJECT STATE.md` — CREATE
- `SPRINT.md` — CREATE
- `CHANGELOG.md` — CREATE (this file)
- `BACKLOG.md` — CREATE
- `LEARNINGS.md` — CREATE
- `DECISIONS.md` — CREATE

**Git:** Branch `feature/init-project-docs`, standalone repo

**Pre-existing files (from prior session, now tracked):**
- `0.1.md`, `0.1.1.md`, `0.1.2.md`, `0.1.3.md`

---

## Prior Sessions (Pre-Documentation)

Output files 0.1.md through 0.1.3.md were generated in one or more prior sessions before the standardized 7-file documentation system was applied. Content preserved as-is.
