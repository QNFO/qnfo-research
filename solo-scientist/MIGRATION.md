# MIGRATION — Physics Execution Artifacts

> **Date:** 2026-05-14
> **From:** `G:\My Drive\projects\Amplifying the Solo Scientist\`
> **To:** `G:\My Drive\projects\ultrametric-physics-sprint\`
> **Reason:** Sprint 3 execution artifacts belong in a dedicated physics-execution project, not the methodology/PoC project.

## Files to Migrate

### Execution Scripts (2 files)
| Source | Destination | Purpose |
|:-------|:------------|:--------|
| `0.6.py` | `0.1.py` | Monte Carlo p-value assessment (Sprint 3.1) |
| `0.7.py` | `0.2.py` | Extended scale ratio scan (Sprint 3.2) |

### Analysis & Documentation (2 files)
| Source | Destination | Purpose |
|:-------|:------------|:--------|
| `0.8.md` | `0.3.md` | Consolidated statistical analysis (Sprint 3.3) |
| `sprint_log.md` | `sprint_log.md` | Sprint 3 execution log with amplification metrics |

### Output Data (4 files)
| Source | Destination | Purpose |
|:-------|:------------|:--------|
| `outputs/mc_results.json` | `outputs/mc_results.json` | Monte Carlo results (p=0.000589) |
| `outputs/mc_histogram.png` | `outputs/mc_histogram.png` | Histogram + survival function plot |
| `outputs/scales.json` | `outputs/scales.json` | 102-scale physics library |
| `outputs/scan_results.json` | `outputs/scan_results.json` | 5,151 pairwise ratios |

### Sprint Plans (2 files — recommended)
| Source | Destination | Purpose |
|:-------|:------------|:--------|
| `0.5.1.md` | `0.0.1.md` | 2-day sprint plan (concise) |
| `0.5.2.md` | `0.0.2.md` | 2-day sprint plan (detailed) |

## Git Commands (PowerShell)

```powershell
# 1. Create destination project
New-Item -ItemType Directory -Path "G:\My Drive\projects\ultrametric-physics-sprint" -Force
Set-Location "G:\My Drive\projects\ultrametric-physics-sprint"
git init

# 2. Create output directory
New-Item -ItemType Directory -Path "outputs" -Force

# 3. Copy files from source to destination
$src = "G:\My Drive\projects\Amplifying the Solo Scientist"

Copy-Item "$src\0.6.py" "0.1.py"
Copy-Item "$src\0.7.py" "0.2.py"
Copy-Item "$src\0.8.md" "0.3.md"
Copy-Item "$src\sprint_log.md" "sprint_log.md"
Copy-Item "$src\outputs\mc_results.json" "outputs\mc_results.json"
Copy-Item "$src\outputs\mc_histogram.png" "outputs\mc_histogram.png"
Copy-Item "$src\outputs\scales.json" "outputs\scales.json"
Copy-Item "$src\outputs\scan_results.json" "outputs\scan_results.json"

# Optional: sprint plans
Copy-Item "$src\0.5.1.md" "0.0.1.md"
Copy-Item "$src\0.5.2.md" "0.0.2.md"

# 4. Bootstrap documentation in new project
# (Create README.md, SPRINT.md, etc. per Section 0.7 standards)

# 5. Commit in new project
git add -A
git commit -m "Initial commit: physics execution artifacts migrated from Amplifying the Solo Scientist"

# 6. Remove from source project (ONLY after confirming destination is correct)
Set-Location "G:\My Drive\projects\Amplifying the Solo Scientist"
git rm 0.6.py 0.7.py 0.8.md sprint_log.md
git rm outputs/mc_results.json outputs/mc_histogram.png outputs/scales.json outputs/scan_results.json
# Optional: also remove sprint plans if migrated
# git rm 0.5.1.md 0.5.2.md
git commit -m "ACTION:DELETE FILES: 0.6.py, 0.7.py, 0.8.md, sprint_log.md, outputs/ RATIONALE:Migrated physics execution artifacts to ultrametric-physics-sprint project"
```

## Post-Migration Checklist

- [ ] Destination project created and files copied
- [ ] Destination committed (verify with `git log --oneline`)
- [ ] Source files removed and committed
- [ ] Source `SPRINT.md` updated (Sprint 3 migration note already present)
- [ ] Source `PROJECT STATE.md` updated (outputs table cleaned up)
- [ ] Source `outputs/` directory removed (if empty after migration)

## What Stays in the Methodology Project

These files are the project's permanent content and should NOT be migrated:

| File | Why It Stays |
|:-----|:-------------|
| `0.9.md` | Force-Multiplier Playbook — the primary deliverable |
| `0.2.md` / `0.3.md` | Journal manuscript and clean publication version |
| `0.1.md` / `0.1.1.md` | Physics case study — reference evidence for the methodology |
| `0.1.3.md` | Original playbook/mini-paper brainstorm |
| `0.4.md` / `0.5.md` | Intermediate manuscript drafts |
| All 7× infrastructure docs | Project management (Section 0.7) |
