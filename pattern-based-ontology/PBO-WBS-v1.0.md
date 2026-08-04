# Pattern-Based Ontology — Work Breakdown Structure (WBS) v1.0

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-16 | **License:** QNFO-ULA
**Canonical Framework:** PBO-D-0.0 (10.5281/zenodo.21389579)

---

## WBS Overview

The Pattern-Based Ontology (PBO) research program is organized into a hierarchical Work Breakdown Structure. All project files follow a standard naming convention.

### WBS ID Convention

```
PBO-[TYPE]-[PILLAR].[DELIVERABLE]  →  PBO-D-0.0
                                       │   │  └─ Sub-version
                                       │   └──── Deliverable number (0=framework, 1=theses, 2=roadmap, 3=hierarchy, 4=wbs)
                                       └──────── Type: D=Deliverable, P=Project file, W=Working note
```

---

## Deliverable Registry

| WBS ID | Publication | Zenodo DOI | Zenodo Files | Provenance | Pillar |
|:-------|:------------|:-----------|:-------------|:-----------|:-------|
| **PBO-D-0.0** | Pattern-Based Ontology v1.0 | 10.5281/zenodo.21389579 | MD, PDF, ZIP, README | ✅ | P0: Framework |
| **PBO-D-1.0** | 42 Theses v3.0 | 10.5281/zenodo.21389470 | MD, PDF, ZIP, README | ✅ | P0: Foundation |
| **PBO-D-2.0** | PBO Research Roadmap v1.0 | 10.5281/zenodo.21389696 | MD, PDF | ⚠️ Pending | P0: Planning |
| **PBO-D-3.0** | Pattern Hierarchy v3.0 | 10.5281/zenodo.21389703 | MD, PDF | ⚠️ Pending | P0: Taxonomy |
| **PBO-D-4.0** | PBO WBS & Project Org v1.0 | PENDING | MD | N/A | P0: Admin |

---

## Pillar → Deliverable Mapping

| Pillar | ID | Description | Key Deliverables | Status |
|:-------|:----|:------------|:-----------------|:-------|
| **P0** | Framework Foundation | Canonical framework, WBS, project org, foundational publications | D-0.0 through D-4.0 | Active ✅ |
| **P1** | STC Formalization | Map STC normal forms to Standard Model particles | (Pending formalization) | Research |
| **P2** | Cosmological Signatures | CMB log-periodic oscillations, spacetime granularity tests | (Pending) | Research |
| **P3** | Ultrametric Quantum Computing | Passive geometric fault tolerance via Bruhat-Tits tree | (Pending) | Research |
| **P4** | Gravity Reformulation | Derive Einstein equations from pattern interaction graph | (Pending) | Conceptual |
| **P5** | Consciousness as Pattern | Self-referential distinction closure (S₇) | (Pending) | Conceptual |
| **P6** | Cross-Disciplinary Validation | Biology, neuroscience, sociology predictions | (Pending) | Future |

---

## File Naming Convention

```
PBO-[TYPE]-[PILLAR].[DELIVERABLE]_Descriptive-Title-vMAJOR.MINOR.ext

Examples:
  PBO-D-0.0_Pattern-Based-Ontology-v1.0.md
  PBO-D-1.0_42-Theses-v3.0.md
  PBO-D-2.0_Research-Roadmap-v1.0.md
  PBO-D-3.0_Pattern-Hierarchy-v3.0.pdf
  PBO-W-0.1_Bridge-Equation-Notes.md
  PBO-P-1.1_STC-Normal-Forms-v0.1.py
```

---

## Directory Structure

```
PBO/                              ← Project root (local: Desktop/PBO/)
├── README.md                     ← Master project README
├── PBO-WBS-v1.0.md               ← This document (PBO-D-4.0)
├── deliverables/                 ← Publication deliverables (PBO-D-*)
│   ├── PBO-D-0.0_Pattern-Based-Ontology-v1.0.md
│   ├── PBO-D-0.0_Pattern-Based-Ontology-v1.0.pdf
│   ├── PBO-D-0.0_PROVENANCE-BUNDLE.zip
│   ├── PBO-D-1.0_42-Theses-v3.0.md
│   ├── PBO-D-1.0_42-Theses-v3.0.pdf
│   ├── PBO-D-1.0_PROVENANCE-BUNDLE.zip
│   ├── PBO-D-2.0_Research-Roadmap-v1.0.md
│   ├── PBO-D-2.0_Research-Roadmap-v1.0.pdf
│   ├── PBO-D-2.0_PROVENANCE-BUNDLE.zip
│   ├── PBO-D-3.0_Pattern-Hierarchy-v3.0.md
│   ├── PBO-D-3.0_Pattern-Hierarchy-v3.0.pdf
│   └── PBO-D-3.0_PROVENANCE-BUNDLE.zip
├── working/                      ← Working notes and project files (PBO-W-*, PBO-P-*)
├── provenance/                   ← Extracted provenance bundles
│   ├── PBO-D-0.0/                ← PBO v1.0 provenance
│   ├── PBO-D-1.0/                ← 42 Theses v3.0 provenance
│   ├── PBO-D-2.0/                ← Roadmap provenance
│   └── PBO-D-3.0/                ← Hierarchy provenance
└── references/                   ← Non-WBS reference materials
```

---

## Remote Storage Map

| Storage | Path/URL | Contents | Status |
|:--------|:---------|:---------|:-------|
| **GitHub** | `rwnq8/pattern-based-ontology` | All deliverables + WBS + README | ⚠️ Create repo |
| **Zenodo** | Community: Autaxys and Autology | All PBO-D-* published (DOI) | ✅ Published |
| **Cloudflare R2** | `releases/2026/07/pbo/` | Canonical cloud copies | ⚠️ Push pending (R2 mount offline) |
| **Local** | `Desktop/PBO/` | Working directory | ✅ Organized |

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| v1.0 | 2026-07-16 | Initial WBS. 4 deliverables published. Naming conventions. Directory structure. |
