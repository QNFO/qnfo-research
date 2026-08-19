# Post-Publication Adversarial Analysis — PASS-2 AGGREGATED REPORT (QNFO.RES.016)

**Artifact audited:** "Five Objections, One Standard: An Evidence-Graded Adjudication of a Critique of Post-Quantum Synthesis" — v1.1, DOI 10.5281/zenodo.22010489 (concept 10.5281/zenodo.22009652)
**Date:** 2026-08-19 · **Gate:** POST-PUBLICATION ADVERSARIAL ANALYSIS (HARD) — pass-2 (post-remediation re-audit of the v1.1 newversion)
**Mode:** 3 reviewer slots (Accuracy / Completeness / Dependency) + direct parent-agent fallback audit · READ-ONLY on the published artifact

---

## 1. Verdict summary

| Auditor | Result | HARD | SOFT | DESIGN |
|:--------|:-------|:----:|:----:|:------:|
| Accuracy (UP8F2d9mJiYHMqEYUVm6b) | **PASS-2 CLEAN** | 0 | 5 | 2 |
| Completeness (M7WK0E6lMiUJW_zqwWcdG) | **PASS** | 0 | 1 | 1 |
| Dependency (X8Cwn4_i1cGEccrx_ZWX6) | **PASS** | 0 | 0 | 1 |
| Direct parent-agent fallback | **ALL 7 CHECKS PASS** | 0 | 0 | 0 |
| **TOTAL** | **CLEAN** | **0** | **6** | **4** |

**Zero HARD findings across all three dimensions.** All five pass-1 HARD defects (fabricated authors Caruana/Khodjaev, VVZ-1998 DOI misattribution, 780→790 works, unverified Hensen DOI) were verified **landed and live-verified** in v1.1. No new fabrication introduced.

## 2. Accuracy (pass-2) — findings

**Verified remediated (all 5 pass-1 HARD, live Crossref in pass-2):**
- H-1 → Budroni, Cabello, Gühne, Kleinmann, Larsson (RMP 94:045007) — body §3 + References + `budroni2022` in .bib
- H-2 → Aniello, Mancini, Parisi (Entropy 25(1):86) — body §6 + References + `aniello2022`
- H-3 → TMP 10 DOI anchored to Youngho Jang (1–69); VVZ re-anchored to 1994 World Scientific book — `jang1998` + `vvz1994`
- H-4 → "790 indexed works" (evidence meta.count=790)
- H-5 → Hensen 2015 Nature 526:682–686 live-verified; recorded in citation-audit.md

**SOFT (folded into repo for next version-bump batch — no newversion per reviewer recommendation):**
- S-1: §8 table "**Forty-year**" capitalized token (missed by pass-1 fix) → **FIXED in repo** (Four-decade)
- S-2: Garola 2006 in References but no in-text anchor → **FIXED in repo** (context-dependence account, §7)
- S-3: Quni-Gudzinas 2025c + 2026 in References uncited in body → **FIXED in repo** (§7 AI-audit anchor; §6 Bruhat–Tits anchor)
- S-4: Declarations "Version: 1.0" stale in v1.1 file → **FIXED in repo** (1.1)
- S-5: RESEARCH-CONTINUITY-REGISTRY SESSION LOG lacks v1.1 row → **FIXED in repo**

**DESIGN:** References ordering cosmetic (deferred); Zenodo↔clone byte-parity (parent's direct audit confirmed R2 0-diff 46 files + D1 v1.1 readback).

## 3. Completeness (pass-2) — findings

- 45/45 files present on the record; **44/45 md5-identical** to repo at v1.1 tag.
- Frontmatter PASS: deposited .md carries `doi: 10.5281/zenodo.22010489` + `status: published` (NEWVERSION-FRONTMATTER-CARRYOVER-1 PASS).
- Rebuilt artifacts PASS: deposited PDF = 190,600 B, sha256 `54822beb…` identical to local HEAD PDF (v1.0 blob was 189,033 B — proves v1.1 rebuild landed, not carryover).
- PUBLICATION-PROSE-GATE-1 PASS: zero internal-pipeline tokens (one descriptive "red-team" in abstract = legitimate prose).
- Registry content PASS: FQ1–3, P1–2, REG-RES016-001/002, calibration register all present.
- related_identifiers GitHub isSupplementTo PASS.

**SOFT-6 (only completeness finding):** the **deposited RESEARCH-CONTINUITY-REGISTRY.md is one session-log row stale** (4484 B = v1.0-era blob vs 4834 B repo HEAD; missing the "PUBLISH v1.0" log line added in commit fce7872). File-level carryover defect, no frontmatter/DOI impact. Reviewer options: v1.2 newversion replacing that file **OR accept the documented 1-line delta**.
**Decision (documented): ACCEPT the documented delta** — rationale: (a) the registry is a living internal document; its canonical copy is the repo (now updated); (b) the delta is one log row with zero substantive content (FQ/prediction/calibration items all present); (c) accuracy reviewer independently ruled "no newversion needed" for the SOFT set; (d) a v1.2 newversion for one internal-log line would churn all distribution layers for no reader-facing benefit. The next genuine content version bump will carry the corrected file.

**DESIGN:** deposit flattens directory structure (docs/artifacts/references/external-search → root) — no content loss (all md5-match); path provenance lost in record only.

## 4. Dependency (pass-2) — findings

All 8 layers PASS, live-verified:
1. DataCite: findable, version **1.1** (not None — pass-1 issue fixed), 10 subjects, 1 right (cc-by-nc-sa-4.0)
2. Zenodo: id 22010489, conceptrecid 22009652, version 1.1, 45 files
3. Concept chain (ZENODO-CONCEPT-DOI-CITE-1): concept DOI resolves to latest v1.1 via concept API + links.latest
4. Git: branch head == tag v1.1-published-res016 == 4221cd0 (4-way match)
5. GitHub provenance: isSupplementTo link present
6. Gateway/D1: papers.qnfo.org HTTP 200, JSON-LD `json.loads` PASS (pass-1 HARD confirmed fixed), DOI identifier 22010489
7. R2: 46 files (md/html/pdf + bib + artifacts/ + docs/ + external-search/ 34 JSON) — R2-MIRROR-AFTER-PUBLISH-1 PASS
8. KG: paper:pqs-critique-adjudication BELONGS_TO prog-res PASS

**DESIGN:** Zenodo records API 404s on concept-DOI URL form — use `/api/records/{conceptrecid}` or `versions/latest` (query-path artifact, not a defect).

## 5. Direct parent-agent fallback audit (all 7 checks PASS)

DataCite findable/version 1.1 · Zenodo 45 files/version 1.1 · concept chain 22009652→22010489 · .md probes (Caruana=0, Khodjaev=0, forty-year=0, 780=0; Budroni=2, Aniello=3, Jang=1, 790=1; frontmatter v1.1+published) · references.bib 24 entries (budroni/aniello/jang/vvz present; khodjaev/vladimirov1998 absent) · PDF 190,600 B match with deposit · papers.qnfo.org JSON-LD valid with v1.1 DOI.

## 6. Gate conclusion

**PASS — zero HARD findings.** The publish-then-audit loop is complete for v1.1: pass-1 HARD defects remediated and independently re-verified; residual items are 6 SOFT (5 fixed in repo; 1 documented delta) + 4 DESIGN (deferred, cosmetic). All distribution layers consistent. No v1.2 required. Next cycle: fold SOFT fixes into the next genuine version bump; continue tracking FQ1–3 per RESEARCH-CONTINUITY-REGISTRY.
