# PROJECT-PLAN: Consilient Gap Synthesis — QNFO/QWAV Portfolio Roadmap v1.0

**Author:** QNFO  
**Date:** 2026-07-29  
**License:** QNFO Unified License Agreement  
**Project Slug:** `consilient-gap-synthesis`  
**Branch:** `feature/phase0-scaffold`

---

## §1 Charter

### 1.1 Purpose

The QNFO/QWAV ecosystem has produced 95+ projects, 3109 KG nodes, 1502 edges, and
hundreds of publications. This scale creates a new problem: the gaps, deferred
publications, stalled phases, and unresolved research questions are themselves
distributed across multiple projects, memories, and infrastructure layers, with
no single source of truth for "what remains to be done, and in what order."

This project is the meta-synthesis: a consilient catalog of every known gap
across the entire portfolio, classified by domain, severity, and blocker type,
with a phased version roadmap that sequences remediation into deliverable
increments.

### 1.2 Core Claim (Locked)

> **[C1]:** The QNFO/QWAV research portfolio contains a finite, enumerable set
> of gaps that can be classified into ≤5 cross-domain structural categories
> (Infrastructure, Content, Physics Validation, Governance, Dissemination).
> Sequencing these gaps by blocker-dependency and expected value produces a
> Pareto-optimal roadmap where the first two phases (Infrastructure +
> Publication Remediation) resolve >60% of known blockers with <20% of total
> effort, because infrastructure gaps block content gaps, and content gaps
> block dissemination gaps — the dependency graph is predominantly a DAG
> with depth ≤3.

**[Falsifiability]:** This would be disconfirmed if (a) gap classification
fails to converge to ≤5 categories after Phase 2, (b) the dependency graph
contains cycles that make linear phase sequencing impossible, or (c) Phase
1-2 execution resolves <40% of known blockers.

**[Certainty]:** `[speculative]` — the 60%/20% claim is an informed prior
based on portfolio familiarity, not an empirically calibrated baseline.

### 1.3 Scope

**In scope:**
- All QNFO/QWAV research projects with active gaps (open items, soft gaps,
  hard blockers, deferred publications, unregistered Zenodo deposits,
  missing KG edges, missing R2 archives, unverified PDFs, stalled phases)
- Infrastructure gaps that block research (consistency engine, analytics wiring)
- Governance gaps (QNFO.GOV incomplete phases)
- Dissemination gaps (unposted Buffer items, missing SEO metadata)

**Out of scope:**
- ARCHIVED/DRAFT/DECOMMISSIONED projects per DEC-020
- Routine paper publication within existing pipelines
- New research questions not yet captured in any project
- Third-party infrastructure (Pinata, Filebase — per KIF-12 deprecation)

---

## §2 Portfolio State Summary (2026-07-29)

### 2.1 Ecosystem Scale

| Metric | Value |
|:-------|:------|
| Total KG nodes | 3,109 |
| Total KG edges | 1,502 |
| KG node labels | 39 |
| Total projects (KG) | 95 |
| Active projects | 12 |
| Published projects | 8 |
| DRAFT projects (DEC-020) | ~40 |
| ARCHIVED projects | ~35 |
| OpenItems (KG) | 25 |
| Papers in D1 living-paper | 931+ |

### 2.2 Active Projects and Their State

| Project | Status | Phase | Key Gaps |
|:--------|:-------|:------|:---------|
| **measurable-vs-imaginable** | Published | v1.3-distribute | 4 soft gaps resolved; papers-server live |
| **biophoton-ultrametric-consilience** | Published | v0.5-phase4-deep | Missing: GitHub remote, KG link, Vectorize, calibration, PW validation, external lit |
| **qnfo-unified-plan** | Active | Phase 4 complete | All 4 sub-claims [established]; Zenodo DOI 10.5281/zenodo.21664651 published; R2 synced; closeout pending |
| **continuum-trilogy** | Published | v1.0.0 / Phase 4-7 partial | Zenodo DOI 10.5281/zenodo.21672990; 3 papers (26pp); D1+R2 deployed; 5 falsifiable predictions; Phase 4 Stages 0-2 complete |
| **adelic-epistemological-foundations** | Published | Phase 8 complete | Zenodo DOI 10.5281/zenodo.21685479; 56-paper meta-survey; 9 PDFs (main + 8 collateral); papers.qnfo.org live |
| **CFPE Paradigm Forecast** | Active | 7/8 phases | 1 pending: Arweave; quarterly calibration register |
| **QNFO.GOV** | Active | 3/6 phases | 17 tasks remaining; priority CRITICAL |
| **numerata** | Active | Phases 0-5 done | Distribution complete; Zenodo DOI live |
| **kepler-program** | Active | Program-level | Sub-projects need individual Phase 0 audits |
| **silent-radix-convergent-synthesis** | Active | Published | R2 path confirmed |
| **radix-uw-bt-synthesis** | Active | Phase 3 | Sufficient Condition Theorem proven |
| **rtaq (Room-Temp Adelic Qubit)** | Published | Complete | DOI 10.5281/zenodo.21304671 |
| **Infomatics** | RECOVERY | — | GitHub lost; 12 files in R2 only; needs rebuild |
| **ultrametric-well-analysis** | DRAFT | PUBLICATION_BLOCKED | Hardware requirements exceed local capacity |

### 2.3 Critical OpenItems (from KG, non-DRAFT)

| ID | Item | Priority | Status | Domain |
|:---|:-----|:---------|:-------|:-------|
| OI-003 | Consistency Engine | HIGH | STUB | Infrastructure |
| OI-001 | Agent Swarm Architecture | MEDIUM | STUB | Infrastructure |
| OI-002 | Automated Peer Review | MEDIUM | STUB | Infrastructure |
| OI-006 | Reproducibility as Code | MEDIUM | STUB | Infrastructure |
| OI-004 | Portfolio API | IN-PROGRESS | V2 operational | Infrastructure |
| OI-012 | Archive Migration | IN-PROGRESS | Discovery Index rebuilt | Infrastructure |
| task-analytics-03 | Wire analytics to lifecycle cron | P1 | pending | Infrastructure |
| task-knowing-03 | Pattern documentation | P1 | UNBLOCKED | Content |

---

## §3 Cross-Domain Gap Classification

### 3.1 The Five Gap Categories

Every gap in the QNFO/QWAV portfolio maps to one of five structural categories.
This classification is itself a hypothesis — to be tested in Phase 2.

| Category | Definition | Examples | Est. Gap Count |
|:---------|:-----------|:---------|:---------------|
| **Infrastructure (I)** | Missing or broken technical systems | Consistency engine (OI-003), analytics wiring, archive migration, Infomatics recovery | ~15 |
| **Content/Publication (C)** | Papers with incomplete publication status | Missing KG edges, deferred Zenodo uploads, unbuilt PDFs, missing Vectorize indices | ~20 |
| **Physics Validation (P)** | Unvalidated scientific claims | Calibration training, PW clock extrapolation, external literature gap | ~8 |
| **Governance (G)** | Incomplete policy/procedure | QNFO.GOV 17 remaining tasks, missing program-level Phase 0 audits | ~10 |
| **Dissemination (D)** | Unpublished or unposted artifacts | Buffer queue items, missing SEO metadata, DNSLink gaps | ~5 |

### 3.2 Dependency Graph (Preliminary)

```
Infrastructure (I) ──┬──► Content/Publication (C) ──► Dissemination (D)
                      │
                      ├──► Governance (G) ──► Content/Publication (C)
                      │
                      └──► Physics Validation (P) ──► Content/Publication (C)
```

**Key insight:** Infrastructure gaps are the root blockers. Without the
consistency engine (OI-003), we cannot systematically verify that all
publications have KG edges, R2 archives, and correct DOIs. Without that
verification, Content gaps are found ad hoc rather than systematically.
Fixing I-gaps enables systematic C-gap resolution, which enables D-gaps.

---

## §4 Work Breakdown Structure

### Phase 0: Scaffold + Portfolio Discovery (CURRENT)
- [x] F0.1: Create repo and directory scaffold
- [x] F0.2: Write PROJECT-PLAN.md with charter, WBS, risk register
- [x] F0.3: Write README.md
- [x] F0.4: Query KG for portfolio state (OpenItems, Projects, Papers)
- [x] F0.5: Query memories for known soft gaps
- [ ] F0.6: Write `.gitignore`
- [ ] F0.7: Commit + tag `v0.1-phase0`

### Phase 1: Due Diligence — Full Cross-Reference
- [ ] P1.1: For each ACTIVE project, read PROJECT-PLAN.md / HANDOFF.md for explicit gap lists
- [ ] P1.2: Query R2 for orphan project artifacts (projects with R2 presence but no KG node)
- [ ] P1.3: Query D1 living-paper for papers with status != "published" or missing DOI
- [ ] P1.4: Cross-reference KG Paper nodes against D1 (KIF-23: 257/887 were missing — recheck)
- [ ] P1.5: Run Cross-Domain Consilience Gate (KIF-29) — produce `artifacts/consilience-gate.md`
- [ ] P1.6: Commit + tag `v0.2-phase1-dd`

### Phase 2: Gap Catalog — Complete Enumeration and Classification
- [ ] P2.1: Compile master gap list from all Phase 1 sources
- [ ] P2.2: Classify each gap into the 5-category system (I/C/P/G/D)
- [ ] P2.3: Assign severity: BLOCKING / HIGH / MEDIUM / LOW
- [ ] P2.4: Map blocker dependencies (gap A blocks gap B)
- [ ] P2.5: Assign estimated effort (S/M/L/XL) per gap
- [ ] P2.6: Produce `artifacts/gap-registry.md` — the complete catalog
- [ ] P2.7: Commit + tag `v0.3-phase2-gaps`

### Phase 3: Version Roadmap — Phased Sequencing
- [ ] P3.1: Topological sort of gap dependency graph into phases
- [ ] P3.2: Assign version targets: `v2.0` (Infrastructure), `v2.1` (Content Remediation), `v2.2` (Governance), `v2.3` (Physics Validation), `v2.4` (Dissemination)
- [ ] P3.3: Estimate completion windows per version
- [ ] P3.4: Produce `docs/version-roadmap.md`
- [ ] P3.5: Commit + tag `v0.4-phase3-roadmap`

### Phase 4: Deep Research — Bayesian Cascade (IF TRIGGERED)
- [ ] P4.1: Stage -1: Likelihood Calibration Protocol (KIF-31)
- [ ] P4.2: Stage 0-8: Full Bayesian cascade on highest-EV gap resolution strategies
- [ ] P4.3: Produce `artifacts/bayesian-cascade.md`
- [ ] P4.4: Commit + tag `v0.5-phase4-deep`

### Phase 5: Publication — Synthesis Paper
- [ ] P5.1: Write synthesis paper (`paper.md`) with full gap catalog and roadmap
- [ ] P5.2: Build PDF via `research/scripts/build-paper.py`
- [ ] P5.3: Verify PDF (zero U+FFFD/U+FFFF)
- [ ] P5.4: Build PROVENANCE-BUNDLE.zip
- [ ] P5.5: Zenodo upload with DOI
- [ ] P5.6: Commit + tag `v1.0`

### Phase 6: Deployment
- [ ] P6.1: D1 living-paper insert
- [ ] P6.2: Papers-server verification (HTTP 200)
- [ ] P6.3: R2 archive sync
- [ ] P6.4: KG Paper node + edges
- [ ] P6.5: Commit + tag `v1.1-deploy`

### Phase 7: Dissemination
- [ ] P7.1: SEO audit (robots.txt, sitemap, llms.txt, meta tags)
- [ ] P7.2: Buffer post (3 channels: Twitter, LinkedIn, Bluesky)
- [ ] P7.3: Internet Archive snapshot
- [ ] P7.4: Commit + tag `v1.2-disseminate`

### Phase 8: Core Distribution
- [ ] P8.1: GitHub push + tag `v1.3-distribute`
- [ ] P8.2: Zenodo new-version (if applicable)
- [ ] P8.3: Full stack verification (GitHub+Zenodo+R2+D1/KG)

---

## §5 Deliverable Registry

| ID | Deliverable | Path | Phase | Format | Archival |
|:---|:------------|:-----|:------|:-------|:---------|
| D-01 | PROJECT-PLAN.md | root | 0 | Markdown | R2 + GitHub |
| D-02 | README.md | root | 0 | Markdown | R2 + GitHub |
| D-03 | consilience-gate.md | artifacts/ | 1 | Markdown | R2 + GitHub |
| D-04 | gap-registry.md | artifacts/ | 2 | Markdown | R2 + GitHub |
| D-05 | version-roadmap.md | docs/ | 3 | Markdown | R2 + GitHub |
| D-06 | bayesian-cascade.md | artifacts/ | 4 | Markdown | R2 + GitHub |
| D-07 | paper.md | root | 5 | Markdown | R2 + GitHub + Zenodo |
| D-08 | paper.pdf | root | 5 | PDF | R2 + GitHub + Zenodo |
| D-09 | PROVENANCE-BUNDLE.zip | root | 5 | ZIP | R2 + Zenodo |
| D-10 | Zenodo DOI | — | 5 | DOI | Zenodo |
| D-11 | D1 living-paper entry | — | 6 | SQL | D1 |
| D-12 | KG Paper node | — | 6 | Graph | KG |

---

## §6 Risk Register

| ID | Risk | Probability | Impact | Mitigation |
|:---|:-----|:-----------|:-------|:-----------|
| R-01 | Gap classification fails to converge to ≤5 categories, invalidating the structural hypothesis | Low | High | Accept broader taxonomy if evidence demands it; the classification itself is falsifiable |
| R-02 | Dependency graph contains cycles making linear phase sequencing impossible | Medium | Medium | Handle cycles by bundling dependent gaps into the same phase |
| R-03 | Phase 1 due diligence reveals 100+ gaps, exceeding single-session scope | High | Medium | Prioritize by severity; defer LOW gaps to a Phase 2.1 addendum |
| R-04 | Zenodo file API still down at Phase 5, blocking publication upload | Medium | High | Defer upload per KIF-44 protocol; publish metadata and mark as `[ZENODO-UPLOAD-DEFERRED]` |
| R-05 | Buffer token stale at Phase 7 (KIF-45) | Medium | Low | Run `buffer-token-check.py` pre-flight; signal `[BUFFER-TOKEN-STALE]` if needed |
| R-06 | Mid-turn workspace volatility (KIF-29) loses project artifacts before R2 upload | Medium | High | R2-upload each artifact immediately after creation per KIF-41 |
| R-07 | KG Paper-D1 desync (KIF-23) persists — papers missing from KG despite D1 presence | High | Medium | Reconcile as part of Phase 1 due diligence; flag as known systemic drift |

---

## §7 Version History

| Version | Date | Description |
|:--------|:-----|:------------|
| v0.1-phase0 | 2026-07-29 | Phase 0: Scaffold + Portfolio Discovery |

---

## §8 Success Criteria

1. **Gap catalog completeness:** ≥95% of known gaps captured from KG OpenItems,
   project HANDOFF.md files, D1 paper status, and memory records.
2. **Classification convergence:** All gaps assigned to one of the 5 categories
   (I/C/P/G/D) with <5% "unclassified" remainder.
3. **Version roadmap:** ≤6 version targets sequenced by dependency, with
   estimated effort windows per version.
4. **Publication quality:** Synthesis paper passes all QNFO publication gates
   (Physics Writing Standards, Professional Publication Standards, PDF
   verification).
5. **Actionability:** Each version target maps to concrete, executable tasks
   that can be picked up by any agent from cold start.
