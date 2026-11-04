# Practical Applications Extension — Consilient Gap Synthesis

**Date:** 2026-07-31
**Stage:** 9 (MANDATORY, lighter scope — 3 application domains)

## Domain Mapping

This gap synthesis maps onto three concrete application domains:

| Candidate | Computation/Infrastructure | Research Management | Open Science |
|:----------|:---------------------------|:--------------------|:-------------|
| A (KG-D1 Sync) | ✅ Automated schema alignment | ✅ Cross-project discoverability | ✅ Linked-data export |
| B (NULL-DOI Resolution) | ✅ Batch publication pipeline | ✅ Citation completeness | ✅ DOI assignment |
| C (Infrastructure v2.0) | ✅ Worker health monitoring | ✅ Uptime SLA tracking | ✅ Public health dashboard |
| D (Automated Monitoring) | ✅ Cronjob watchdog | ✅ Alert routing | ✅ Status page |

---

## Domain 1: Computation/Infrastructure

### Operational Signature

**KG-D1 Sync:** The sync enables programmatic cross-project queries. Instead of
manually cross-referencing paper metadata across D1 and KG, an agent or researcher
can issue a single query — "find all papers that cite adelic methods AND have
unresolved gaps" — and receive results spanning both systems. This transforms
gap discovery from a manual audit (hours) to an automated query (seconds).

**Falsifiable claim:** By Q4 2026, a single SQL+Cypher query spanning D1 and KG
will return cross-system results in ≤5 seconds for the full 917-paper corpus.

### Operational Signature

**Infrastructure v2.0:** Worker health repair enables the public health dashboard
(worker-status.qnfo.org or equivalent) to show real-time status for all 7 Workers.
Today, the Lifecycle Worker returns HTTP 500 — any monitoring dashboard built on
top of it inherits that failure. Repairing I-02 is prerequisite to visibility.

**Falsifiable claim:** By Q4 2026, all 7 QNFO Workers will return HTTP 200 on
their /health or /status endpoints, verifiable via a single automated check.

---

## Domain 2: Research Management

### Operational Signature

**NULL-DOI Resolution:** A paper without a DOI is invisible to citation tracking.
The 30 NULL-DOI papers represent "dark matter" in the QNFO portfolio — they exist
in D1 and R2 but cannot be cited, tracked, or discovered via DOI-based search.
Resolving these assigns each paper a permanent, citable identifier, making the
entire portfolio citation-ready.

**Falsifiable claim:** By Q3 2026, every paper in the D1 living-paper database
with non-NULL `body_md` will have a Zenodo DOI, reducing the NULL-DOI count
from 30 to ≤15.

### Operational Signature

**Project Closeout Sweep:** Stalled projects with missing phase tags are not just
cosmetic — they prevent automated progress tracking. A cronjob that scans for
projects with `status = "in_progress"` and `last_commit > 90 days ago` cannot
distinguish "actively worked on but not tagged" from "abandoned." Structured
closeout makes automation possible.

**Falsifiable claim:** By Q4 2026, ≥80% of QNFO projects will have a complete
tag chain (v0.1-phase0 through their current phase) or an explicit "stalled"
status marker.

---

## Domain 3: Open Science

### Operational Signature

**Cross-Layer Verification:** The 4-layer verification (D1↔KG↔R2↔Workers) is
not just an internal audit tool — it is the basis for a public "portfolio health"
badge. When a reader visits papers.qnfo.org, a small badge could show: "917 papers
✓ | 887 DOIs ✓ | Health: GREEN." This signals transparency and rigor to the
open-science community.

**Falsifiable claim:** By 2027, papers.qnfo.org will display a public health badge
showing paper count, DOI coverage percentage, and Worker uptime, updated hourly.

### Operational Signature

**External Visibility:** The gap synthesis itself is a meta-research artifact —
research about research. Making it visible (SEO, Buffer, citation tracking) serves
the open-science goal of transparency: "Here is what we know we haven't done yet."
This is rare in research portfolios — most institutions do not publish their gap
registries.

**Falsifiable claim:** By Q1 2027, the consilient-gap-synthesis paper will be
cited by at least 2 external (non-QNFO) papers discussing portfolio-scale research
management or gap-driven research prioritization.

---

## Calibration Register Entries (Stage 9 supplements)

[CHECK: 2026-10-01] By Q3 2026 close, a cross-system D1+KG query (finding papers
with specific properties across both systems) will execute in ≤5 seconds.
Likelihood-Anchor: Calibrated Subjective
Strength: [WEAK]
Status: [PENDING]
Post-hoc risk: "The query was fast in tests but timed out under production load."

[CHECK: 2026-12-31] By Q4 2026 close, all 7 QNFO Workers will have healthy
/health or /status endpoints returning HTTP 200.
Likelihood-Anchor: Reference Class (worker repair velocity, 3 prior QNFO incidents resolved within 1 session each)
Strength: [STRONG]
Status: [PENDING]
Post-hoc risk: "Worker X was healthy when checked but regressed before the quarter closed."

[CHECK: 2027-03-31] By Q1 2027, papers.qnfo.org will display an auto-updating
portfolio health badge (paper count, DOI coverage, Worker uptime).
Likelihood-Anchor: Calibrated Subjective
Strength: [WEAK]
Status: [PENDING]
Post-hoc risk: "The health badge was built but not deployed to production."

## Cross-Domain Consilience Cross-Reference

The consilience gate (Phase 1, `artifacts/consilience-gate.md`) identified
structural isomorphisms between "gap registry" and concepts in biology (immune
system gap detection), sociology (institutional knowledge management), and
computer science (technical debt tracking). The operational signatures above
reinforce the CS-domain translation: gap resolution is analogous to technical
debt repayment — the interest compounds if left unaddressed (the 610-node KG
delta grows), and the principal must be paid down in prioritized tranches
(the v2.0–v2.4 roadmap).

