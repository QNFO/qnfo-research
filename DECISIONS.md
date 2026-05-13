# DECISIONS — Amplifying the Solo Scientist

> Architecture and design decisions with rationale. Recorded as they are made.

---

### D-001: Project structure — flat directory with versioned filenames
- **Date:** Pre-documentation (reflected in 0.1.x file series)
- **Decision:** All output files live in a single flat project directory with semantic versioned filenames (MAJOR.MINOR[.PATCH].ext). Descriptive filenames are prohibited for content/output files.
- **Rationale:** Version numbers encode chronological order and enable trivial cross-referencing between documents and their supporting assets (code, data, figures). In a flat directory where every file belongs to the same project, descriptive names provide no additional organizational benefit.
- **Implications:** Next output file is 0.2.0.md or 0.2.md. Supporting scripts share the version prefix (e.g., 0.2.py).

### D-002: Case study selection — ultrametric cosmology
- **Date:** Pre-documentation (see 0.1.2.md)
- **Decision:** Use the ultrametric (p-adic) quantum gravity / cosmological constant resolution project as the primary case study for the force-multiplier methodology.
- **Rationale:** (a) The physics project was already underway with rich LLM interaction logs. (b) Theoretical physics is a domain where solo researchers are at a particular disadvantage relative to teams. (c) The cosmological constant problem is a high-stakes, recognizable challenge.
- **Implications:** The methodology is demonstrated in physics first; generalization to other domains requires separate case studies (backlog items B-010 through B-012).

### D-003: Output format — Overleaf/Markdown + GitHub
- **Date:** Pre-documentation (see 0.1.2.md §3.1, 0.1.3.md Part I)
- **Decision:** Papers are drafted in Markdown with LaTeX math, versioned via Git, with an Overleaf bridge for LaTeX compilation and submission formatting.
- **Rationale:** Markdown is LLM-friendly; Git provides audit trail; Overleaf handles LaTeX compilation and journal formatting. This stack minimizes friction between human, LLM, and publication pipeline.
- **Implications:** The Solo-Research Stack (backlog B-005) should containerize this toolchain.

### D-004: Git repo isolation — standalone per project
- **Date:** 2026-05-13
- **Decision:** Initialize a standalone `.git` repository inside `Amplifying the Solo Scientist\` rather than using the shared parent repo at `G:\My Drive\projects\`.
- **Rationale:** Cross-Project Learning L1 documented that shared parent repos cause cross-project contamination (staged deletions from Language-Info-Architecture appeared on this branch). Each project needs its own git history.
- **Implications:** Git operations are now scoped to this project. The parent remains a container directory only.

### D-005: Documentation standard — 7 mandatory files
- **Date:** 2026-05-13
- **Decision:** Adopt the standardized 7-file documentation system: README.md, PROJECT STATE.md, SPRINT.md, CHANGELOG.md, BACKLOG.md, LEARNINGS.md, DECISIONS.md.
- **Rationale:** Enables agent handoff across sessions without requiring the human to re-explain context. Standardized format facilitates cross-project learning.
- **Implications:** These files are never versioned (fixed names). All other project files follow the MAJOR.MINOR.ext convention.
