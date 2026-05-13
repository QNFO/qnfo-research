# CHANGELOG — LLM Force Multiplier

> Chronological versioned change log. One entry per session.

---

## 2026-05-13 — Session: Architecture Correction (Post Reader-Test)

**What Changed:**
- **Section 3 complete rewrite:** Replaced aspirational Docker/API/Overleaf stack with actual architecture (unified conversation environment — LLM + file I/O + Python + git)
- **Section 4.5 added:** Language as Information Architecture as independent second validation case study [26]
- **Section 7.2:** Added "Aspirational Architecture Description" limitation
- **Appendix C:** Renamed to "Dockerfile (Aspirational)" with disclaimer
- **Abstract & Conclusion:** Updated to reference real architecture, harmonized speedup numbers (25× case study, 17× power analysis)
- **LEARNINGS.md:** Added L5 (reader-testing) and L6 (describe-real-architecture)
- **Reference [26]:** Added Language as Information Architecture Zenodo preprint

**Root cause:** The original manuscript described a Docker/API/Overleaf toolchain that was never used. The actual production architecture — DeepChat conversation with integrated file I/O, Python execution, and git — was simpler, faster, and had already produced two published papers (this one + Language as Information Architecture). This correction was triggered by human review pointing out the discrepancy.

**Files Changed:**
- `0.2.md` — EDIT (Sections 3, 4.5, 7.2, 8, Abstract, Appendix C, References)
- `LEARNINGS.md` — EDIT (L5, L6 added)
- `CHANGELOG.md` — EDIT (this entry)
- `PROJECT STATE.md` — EDIT (updated architecture description)

**Git:**
- Branch: `feature/expand-manuscript`
- Commit: `278352c`

---

## 2026-05-13 — Session: Reader Test Fixes

**What Changed:**
- Created expanded manuscript `0.2.md` — comprehensive journal-ready paper (789 lines, ~47K chars)
- Created supporting SymPy script `0.2.py` — standalone verification of vacuum energy derivation
- Updated SPRINT.md, PROJECT STATE.md, CHANGELOG.md

**New Content in 0.2.md:**
- §1 Introduction with literature review (14 references)
- §2 Force-Multiplier Framework (task decomposition, verification cycle, prompt engineering)
- §3 Solo-Research Stack (4-layer architecture, 15-min setup, cost comparison)
- §4 Case Study (hour-by-hour physics walkthrough, speedup table)
- §5 Controlled Experiment Design (3-condition between-subjects, statistical power analysis $[CODE-EXECUTED]$, hypotheses)
- §6 Cross-Domain Generalisation (comp bio, pure math, philosophy)
- §7 Discussion (shifting bottleneck, limitations, ethics, future directions)
- §8 Conclusion
- Appendix A: Prompt Library (5 core templates)
- Appendix B: SymPy Derivation (0.2.py standalone)
- Appendix C: Solo-Research Stack (Dockerfile + docker-compose.yml)
- References (25 citations)

**Statistical Results $[CODE-EXECUTED]$:**
- Cohen's $f = 1.92$ (very large effect)
- Required $n = 4$ per group for $>99\%$ power
- Speedup factor: $16.7\times$ (Force-Multiplier vs. Solo)

**Files Changed:**
- `0.2.md` — CREATE (manuscript)
- `0.2.py` — CREATE (supporting script)
- `SPRINT.md` — EDIT (Sprint 1 tasks marked complete)
- `PROJECT STATE.md` — EDIT (updated deliverable status and metrics)
- `CHANGELOG.md` — EDIT (this file)

**Git:**
- Branch: `feature/expand-manuscript`
- Commits: 3 (0.2.md, 0.2.py, documentation updates)

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
