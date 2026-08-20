# Post-Publication Adversarial Analysis — The $1,032 Research Program (10.5281/zenodo.22028851)

**Audit date:** 2026-08-20 | **Gate:** POST-PUBLICATION ADVERSARIAL ANALYSIS GATE (READ-ONLY)
**Method:** 3-slot reviewer dispatch (Accuracy / Completeness / Dependency) + direct parent-agent 5-adversary audit (Accuracy / Completeness / Dependency / Novelty / Status). Accuracy reviewer completed CLEAN; Dependency + Completeness children failed/stalled (REDTEAM-CHILD-FAIL-1 / REDTEAM-QUEUE-STALL-PATIENCE-1) → direct audit authoritative for those dimensions.

## Findings

### Accuracy — CLEAN (0 HARD, 1 SOFT)
- All 20+ checks pass against live APIs: records API state=done, DataCite findable, 7 files byte-exact, creators/ORCID/license exact, README cites concept DOI (22028787) + version DOI (22028851), md frontmatter v1.1 DOI, no <RESERVED>.
- **SOFT-1:** PROVENANCE.md states the cache-hit components (48.08B hit / 1.79B miss) but not the literal "96.4%" — derivable (96.43%); README abstract and essay body state it. Remediation: add the percentage to PROVENANCE in v1.2.

### Completeness — 2 HARD, 1 SOFT, 1 DESIGN (remediation registered: v1.2 newversion)
Reviewer (live GitHub trees API, branch + main, 670 entries each, truncated: false) + direct audit agree:
- **HARD-1:** Evidence pack not deposited AND not in the isSupplementTo repo — aggregate_usage.py, usage_summary.json, verify_essay.py (the script, aggregated data, and 26-figure verification behind every §1 headline) are absent from both public locations; PROVENANCE.md describes the method but ships no script and never names verify_essay.py. Headline numbers are documentary-only, not re-executable from any public location.
- **HARD-2:** Dissemination package (strategy.md + 7 drafts) not in deposit — exists only in the GitHub related_identifier; gate says include everything.
- **SOFT-1:** PROVENANCE.md states cache-hit components (48.08B/1.79B) but not the literal "96.4%" (derivable 96.43%); README + essay body state it.
- **SOFT-2:** Raw usage CSVs (10 monthly exports) deliberately excluded (user_id + masked api_key) — privacy exclusion not yet documented in PROVENANCE; needs author confirmation as intentional.
- **DESIGN-1:** Neither public location is a complete source set — the supplement repo lacks the deposit-only files (html/pdf/references.bib/citation-audit.md).

### Dependency — CLEAN (script 404s were UA artifacts; verified with qnfo-audit UA + reviewer live evidence)
- related_identifiers isSupplementTo → GitHub branch URL (exact string) ✓; GitHub raw essay 200 ✓; papers.qnfo.org 200 + title ✓; GitHub Release 200 ✓; references.bib DOIs all DataCite findable ✓.

### Novelty — calibrated
- Novelty IN KIND (first operational audited ledger with receipts + kill criterion), not IN CONCEPT (AI-Scientist systems known: Sakana 2408.06292 <$15/paper, Jr 2511.04583, Beel/Kan/Baumgart 2502.14297, Luo/Kasirzadeh/Shah 2509.08713). Essay does not overclaim.

### Status — all distribution layers verified
Zenodo state=done · DataCite findable · R2 qnfo-releases/2026/08/ai-accelerated-research (7/7, rclone check PASS) · D1 living-paper row (doi v1.1, status published) · KG node zenodo-10-5281-zenodo-22028851 distribution_status=distributed · GitHub main 1371fee + tag v1.0-dissemination + Release · papers.qnfo.org 200.

## Remediation items (next cycle)
1. **v1.2 newversion** adding: evidence pack (aggregate_usage.py, usage_summary.json, verify_essay.py) + dissemination package (strategy.md + 7 drafts) + PROVENANCE updates (96.4% literal, script names, privacy-exclusion note for raw CSVs).
2. New gates installed this cycle: D1-QUOTED-RESERVED-COLS-1 (HARD), ZENODO-NEWVERSION-FILE-REPLACE-1 (HARD), CONCEPT-DOI-PRE-BUILD-1 (HARD), ESSAY-DEPOSIT-EVIDENCE-PACK-1 (SOFT), DOIDOT-403-BOT-1 (SOFT), GIT-MERGE-BRANCH-FETCH-1 (SOFT), R2-RCLONE-TEMP-CONFIG-1 (SOFT). Mirrors: system-prompt v3.58, kaizen v2.84, research v2.127, qnfo-core v1.34, cloudflare v3.58.
