# PROJECT-PLAN.md — The Informational Universe

**Project Code:** INFO-UNIVERSE  
**Version:** v0.1-phase0  
**Last Updated:** 2026-07-21  
**Protocol:** research v2.4

---

## §1. Charter

### 1.1 Mission
To rigorously develop and evaluate the hypothesis that information is the fundamental substrate of physical reality — that spacetime geometry, quantum fields, and particle phenomenology are emergent epiphenomena of deeper information-theoretic constraints, not primitive ontological entities.

### 1.2 Core Claim (LOCKED)

**Original claim (from "Correlated Universe 1.0," 2025-04-05):**
The universe is fundamentally informational. Physical law, particles, fields, and geometry are epiphenomena of deeper information-processing constraints.

**Reformulated for falsifiability (Phase 0 lock):**
> "Entanglement entropy in any finite region of spacetime is fully determined by a finite-dimensional Hilbert space whose dimension is set by the region's boundary area, with no additional 'bulk' degrees of freedom beyond those encoded in the boundary information. Every physical observable — mass, charge, spin, metric — can be derived (not merely described) from information-theoretic constraints without introducing primitive material ontological commitments."

**Falsification condition:** If there exists a physical observable that demonstrably cannot be reduced to a finite information-theoretic encoding — i.e., a measurement whose outcome requires an unbounded number of bits independent of boundary area — the core claim is falsified.

### 1.3 Scope

| In Scope | Out of Scope |
|---|---|
| Information-theoretic emergence of spacetime | Empirical cosmology requiring new instruments |
| Boundary-bulk information encoding (holographic principle variants) | String theory landscape surveys |
| Finite-dimensional Hilbert space constraints | Quantum gravity phenomenology requiring collider data |
| Literature synthesis across information theory, quantum foundations, and GR | Building physical prototypes or experiments |
| Formalization of information-first ontology | Philosophical debates without formal models |

---

## §2. Phases and WBS

| Phase | Name | Tasks | Status |
|---|---|---|---|
| 0 | Project Initialization | 5 | **IN PROGRESS** |
| 1 | Due Diligence | 4 | pending |
| 2 | Literature Search & Triage | 6 | pending |
| 3 | Citation Management | 4 | pending |
| 4 | Deep Research (Bayesian Cascade) | 8 | pending |
| 5 | Publication | 6 | pending |
| 6 | Deployment | 4 | pending |
| 7 | Dissemination | 4 | pending |
| 8 | Core Distribution | 4 | pending |
| **Total** | | **45** | **5/45** |

### Phase 0 WBS (this phase)

| Task ID | Task | Status |
|---|---|---|
| T-0.1 | Create GitHub repo + local scaffold | ✅ Complete |
| T-0.2 | Write PROJECT-PLAN.md (charter, WBS, claim lock) | ✅ Complete |
| T-0.3 | Write README.md | ✅ Complete |
| T-0.4 | Write .gitignore + directory scaffold | ✅ Complete |
| T-0.5 | KG seed + pre-flight checklist + commit/tag/push | ⏳ In Progress |

---

## §3. Milestones and Gate Criteria

| Milestone | Phase | Gate Criteria |
|---|---|---|
| M-0 | 0 | Repo created, scaffold complete, PROJECT-PLAN.md locked, P1-P11 pre-flight checklist passing |
| M-1 | 1 | KG + D1 + 2+ external sources queried; gap analysis report complete; no DUPLICATE-WARNING |
| M-2 | 2 | ≥10 core papers classified; all deduped; classification matrix populated |
| M-3 | 3 | Citation audit passes (all paper cites matched to BibTeX entries; no invented citations) |
| M-4 | 4 | 9-stage Bayesian cascade complete; calibration register seeded; strategic memo written |
| M-5 | 5 | paper.md passes Publication Language Gate; PDF builds without Unicode errors (Pandoc+XeLaTeX) |
| M-6 | 6 | D1 living-paper INSERT; papers-server HTTP 200 verified; R2 archive uploaded |
| M-7 | 7 | SEO audit passes (robots.txt, sitemap, llms.txt); Buffer posts queued |
| M-8 | 8 | GitHub + Zenodo + R2 + D1/KG all verified; DOI resolves |

---

## §4. Deliverable Registry

| ID | Deliverable | Phase | Format | Local Path | Archival Target | Status |
|---|---|---|---|---|---|---|
| D-0.1 | PROJECT-PLAN.md | 0 | Markdown | `PROJECT-PLAN.md` | GitHub | draft |
| D-0.2 | README.md | 0 | Markdown | `README.md` | GitHub | draft |
| D-0.3 | .gitignore | 0 | Text | `.gitignore` | GitHub | draft |
| D-1.1 | Due Diligence report | 1 | Markdown | `artifacts/due-diligence.md` | GitHub | pending |
| D-2.1 | Literature classification | 2 | Markdown | `artifacts/lit-review.md` | GitHub | pending |
| D-3.1 | Citation audit report | 3 | Markdown + BibTeX | `artifacts/citation-audit.md`, `references.bib` | GitHub | pending |
| D-4.1 | Strategic memo | 4 | Markdown | `artifacts/strategic-memo.md` | GitHub | pending |
| D-5.1 | Paper (markdown source) | 5 | Markdown | `informational-universe.md` | GitHub, Zenodo, R2 | pending |
| D-5.2 | Paper (PDF) | 5 | PDF | `informational-universe.pdf` | GitHub, Zenodo, R2 | pending |
| D-5.3 | Provenance bundle | 5 | ZIP | `PROVENANCE-BUNDLE.zip` | Zenodo | pending |
| D-6.1 | D1 living-paper record | 6 | SQL row | `living-paper.papers` | Cloudflare D1 | pending |
| D-6.2 | R2 archive copy | 6 | Files | `releases/2026/07/informational-universe/` | Cloudflare R2 | pending |
| D-7.1 | SEO artifacts | 7 | Various | -- | papers.qnfo.org | pending |
| D-7.2 | Social media posts | 7 | Buffer drafts | -- | Buffer | pending |
| D-8.1 | GitHub tag + release | 8 | Git tag | -- | GitHub | pending |
| D-8.2 | Zenodo DOI | 8 | DOI string | `.zenodo_versions.json` | Zenodo | pending |

---

## §5. Risk Register

| ID | Risk | Phase(s) | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|---|---|
| R-01 | Prior art already covers information-theoretic emergence (e.g., Wheeler's "it from bit," holographic principle, digital physics) | 1 | High | High | Mandatory Due Diligence Gate; gap analysis must demonstrate genuine novelty beyond existing frameworks | open |
| R-02 | Core claim cannot be made falsifiable without empirical access to Planck-scale physics | 0, 4 | Medium | High | Reformulate claim in terms of boundary-bulk encoding constraints testable via entanglement entropy bounds | open |
| R-03 | Source material locked in Obsidian vault (D:\Obsidian) — inaccessible via glob/read | 1, 2 | Medium | Medium | Request user copy relevant notes into `docs/` or grant Full Access with explicit cwd | open |
| R-04 | Literature search yields confirmation-bias risk (QNFO Vectorize returns only internal papers) | 2 | Medium | Medium | Vectorize Confirmation-Bias Disclosure mandated; must cross-reference with external arXiv/Semantic Scholar | open |
| R-05 | Project scope expands beyond information theory into full quantum gravity — becomes intractable | 0-8 | Medium | Low | WBS locked at 45 tasks; scope creep triggers Phase Closeout Protocol with WBS re-verification | open |

---

## §6. Success Criteria

1. **Phase 1:** Due diligence confirms no QNFO paper already covers the information-first emergence claim with the same formalization
2. **Phase 2:** ≥10 core papers classified and deep-read; gap in existing literature is confirmed
3. **Phase 4:** Assumption audit passes red-team adversarial challenge; calibration register has ≥5 dated predictions
4. **Phase 5:** Paper passes all Publication Language Gates; self-evaluation rubric ≥4.0 average
5. **Phase 8:** Full core distribution stack verified: GitHub + Zenodo + R2 + D1/KG

---

## §7. Version History

| Version | Tag | Date | Description |
|---|---|---|---|
| v0.1-phase0 | (pending) | 2026-07-21 | Phase 0: Repo scaffold, charter, claim lock, pre-flight checklist |
