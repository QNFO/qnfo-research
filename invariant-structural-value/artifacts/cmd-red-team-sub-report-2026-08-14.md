# CMD RED TEAM SUB — Remediation Addendum (v0.3)

**Date:** 2026-08-14 · **Record:** v0.3 = 10.5281/zenodo.21929902 (published, verified) · **Concept:** 10.5281/zenodo.21929478
**Supersedes:** v0.1 (21929479) → v0.2 (21929590) → **v0.3 (21929902)**

## Reviewer completion (delegations JuI9RScTqrb52_7k0824E / sdTNNRARwOSq6cVmHjfH9 / 29wXg7dBS-Y7lM7OkQsDS)

The three dispatched reviewers completed after an initial queue stall. Aggregate verdict on v0.2:

| Reviewer | Verdict | Findings |
|:---------|:--------|:---------|
| **Accuracy** | **NOT clean — 1 HARD + 2 SOFT** | **HARD-1:** deposited `.md` frontmatter carried stale v0.1 DOI (10.5281/zenodo.21929479) in the v0.2 record (byte-identical sha256 aec33d9bf037…). **SOFT-2:** internal gate tokens in body (`[KIF-18 discipline]`, `BP-1/BP-6/BP-10`, 2× `[MAP — context framing]`). **SOFT-3:** license string (file QNFO-ULA vs record cc-by-4.0 — platform authoritative). |
| **Completeness** | **CLEAN** | 14/14 provenance files, 0 missing/extra; git branch + tag verified; 23 evidence JSONs in external-search/. |
| **Dependency** | **CLEAN** | 42 unique bib entries, 0 dup keys, 0 synthetic DOIs; 33 DOIs verified (28×200 + 5×403-publisher-HEAD, all Crossref-confirmed); joyalstreet1993 + worrall1989 metadata match Crossref exactly. |

## Remediation executed (this cycle, READ-ONLY review → newversion fix)

**HARD-1 (frontmatter DOI):** newversion draft 21929902 created; local `.md` frontmatter updated `doi: 10.5281/zenodo.21929902`; files replaced (md/pdf/html); full metadata PUT (version v0.3, 11 keywords, cc-by-4.0, GitHub related_identifier); published → **10.5281/zenodo.21929902**.

**SOFT-2 (internal tokens):** removed from body — `[KIF-18 discipline]`, `BP-1/BP-6/BP-10`, 2× `[MAP — context framing]`. Retained: 4 `[TERRITORY]` labels (each carries its inline disconfirmation condition — required by MAP-TERRITORY-1; these are the paper's falsifiability machinery, not opaque process codes).

**SOFT-3 (license):** accepted as-is per corpus convention — file frontmatter carries the QNFO-ULA string (canonical YAML template across the corpus) while the platform record metadata (cc-by-4.0) is authoritative for distribution. Documented, not changed.

## v0.3 verification (same-turn, Tool-Call Execution Mandate)

- doi.org HEAD 10.5281/zenodo.21929902 → **200**
- DataCite → **200, state=findable, 11 subjects**
- Zenodo records API → **state=done, version v0.3, 14 files** (md size 14,573 B — corrected)
- Concept DOI 10.5281/zenodo.21929478 → **200** (resolves to latest = v0.3)
- Git: `a4373e1` branch + tag `invariant-structural-value-v0.3-published` → ls-remote verified

## Version history (publish-then-audit loop, complete)

| Version | DOI | Outcome |
|:--------|:----|:--------|
| v0.1 | 10.5281/zenodo.21929479 | Published; audit found synthetic DOI + year drift + audit-count issues (4 HARD + 3 SOFT) |
| v0.2 | 10.5281/zenodo.21929590 | Remediation of v0.1 findings (bib corrected, 42 entries); re-audit found HARD-1 frontmatter DOI + SOFT-2 tokens |
| **v0.3** | **10.5281/zenodo.21929902** | **HARD-1 + SOFT-2 remediated; verified live. Current version.** |

**Loop state: publish → audit → remediate → re-audit → remediate → verified. Never publish-and-forget.**
