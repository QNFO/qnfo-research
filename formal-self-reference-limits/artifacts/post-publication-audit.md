# Post-Publication Audit — QNFO.RES.008 Formal Self-Reference Limits

**WBS:** QNFO.RES.008.P8 (Post-Publication Adversarial Analysis — HARD GATE, 2026-08-12)
**Published artifact:** DOI 10.5281/zenodo.21929689 (record 21929689), GitHub branch res/paper/formal-self-reference-limits @ 9bdb608 (later 69dd14e)
**Date:** 2026-08-14
**Mode:** READ-ONLY against the published artifact (no modifications)

## Method

1. Reviewer subagent dispatched (delegation 8s4Rs5NK52mxnzCRV3s0F, slot reviewer) against the PUBLISHED artifact with live HTTP verification instructions.
2. Direct parent-agent audit executed in parallel with live tool verification.
3. **Audit-the-auditor note (v1.1):** the direct audit's gate-6 check used string-presence (`'ScholarlyArticle' in text`) and PASSED; the reviewer's `json.loads` on the JSON-LD block FAILED. **The string-presence check was inadequate — JSON-LD validity requires a parse test, not a substring test.** Logged as kaizen item K-2.

## Findings (v1.1 — incorporates reviewer completion)

| # | Severity | Location | Finding | Evidence |
|:--|:---------|:---------|:--------|:---------|
| F1 | HARD | papers.qnfo.org serving layer (NOT the Zenodo artifact) | The papers.qnfo.org page does not serve valid ScholarlyArticle JSON-LD. The `<script type="application/ld+json">` block is invalid JSON: a complete 2128-char ScholarlyArticle object is immediately followed by `<\/script>` (escaped) and raw HTML (`<title>`, `<style>`, `<script>window.MathJax={...}`) inside the SAME script element, which only closes at the MathJax-config script's `</script>` (offset 13465). `json.loads` fails ("Extra data: line 1 column 2129"). Any standards-compliant consumer (Google, schema.org validators) must reject the block. Side effect: the swallowed MathJax config never executes (math may render with defaults). **SITE-WIDE template escaping bug** — independently re-verified on 3 pages (RES.008 paper, RES.005 prime-valuation-depth, UCT): all 3 serve invalid JSON-LD with identical structure. Zenodo deposit itself is CLEAN (DOI, metadata, files, P5.FRESH, byte-identical .md, citation integrity all PASS). | reviewer read_result (answerSha256 f4b10230...); independent re-verification script verify_hard_v2.py: 3/3 pages INVALID JSON, `escaped </script> literal present: True` |
| F2 | SOFT | §10 Novelty statement (char 24171) | Residual internal label "P6" in "the objectification thesis (P6) unifies them" — INTERNAL-REF-1 remnant missed by Phase 5 cleanup (cleaned §4/§6/§9 but not §10) | regex scan of deposited .md: `P6` 1 hit, `QNFO.RES` 0, `KIF-` 0, `MAP-TERRITORY` 0, `qnfo-core` 0, `WBS` 0 |
| — | HARD (artifact) | — | none found — the Zenodo publication artifact itself is clean | 16-check matrix below |

## Verification Matrix (16 checks, direct audit + reviewer)

| Check | Result |
|:------|:-------|
| doi.org HEAD -> 200 (zenodo.org/records/21929689) | PASS |
| Record title | PASS |
| License cc-by-nc-sa-4.0 | PASS |
| Version v0.1-draft | PASS |
| publication_date 2026-08-14 | PASS |
| Creators (Quni-Gudzinas) | PASS |
| 21 files | PASS |
| .md present | PASS |
| .html present | PASS |
| .pdf present (%PDF-1.4 valid) | PASS |
| Keywords >= 4 (12) | PASS |
| related_identifiers GitHub isSupplementTo | PASS |
| P5.FRESH (own DOI + status published in YAML) | PASS |
| deposited .md byte-identical to GitHub branch tip (sha256 c5f1112e...) | PASS |
| Text: body H1 = 0 (YAML title single) | PASS |
| Text: cited == listed == {1..29} | PASS |
| GitHub branch reachable @ 9bdb608/69dd14e | PASS |
| **papers.qnfo.org JSON-LD VALID (json.loads)** | **FAIL — HARD F1** |

## Verdict (v1.1)

**1 HARD (serving layer, site-wide) / 1 SOFT (paper text label) / 0 HARD on the Zenodo artifact.**
The publication artifact (Zenodo record + GitHub source) is integrity-clean. The HARD finding is a **deployment defect in the papers.qnfo.org gateway worker template** — it affects ALL papers on the site (not just this one) and predates this publication. Per the publish-then-audit loop, F1 becomes a kaizen/remediation item for the gateway worker (separate fix, does not touch the published record). The published artifact remains READ-ONLY.

## Kaizen / Remediation Items

1. **K-1 (HARD F1):** Fix the qnfo-gateway papers-page template: the JSON-LD block must be closed with a real `</script>` and the MathJax config must be its own script element. Site-wide fix (all papers). Deploy via wrangler to qnfo-gateway; verify with `json.loads` on 3+ pages.
2. **K-2 (audit-the-auditor):** P8 direct-audit gate 6 must validate JSON-LD with `json.loads`, not string-presence. (My initial check was inadequate; the reviewer caught it.)
3. **K-3 (SOFT F2):** remove `(P6)` from §10 in v0.2 newversion; add `P6\b` to the Phase 5 INTERNAL-REF scan pattern.
4. Carry over pre-publication reviewer items (0 HARD / 6 SOFT / 6 DESIGN from delegation 9zuk0tnuy7ikUgJBLwUUO): citation-audit "Cited in §" column, slob/GEB wording, evidence-trail wording, §1 cite [2,29], §3.1 Sigma1-soundness gloss, ref [4] resolvable identifier, [22] split, van der Lugt first-class, external-semantics sentence, author-name normalization, Turing year alignment.

## Evidence

- Reviewer handoff: decision "1 HARD finding - the papers.qnfo.org page for this paper does not serve valid ScholarlyArticle JSON-LD. All other gates pass." (read_result, 2026-08-14)
- Independent re-verification (verify_hard_v2.py, same-turn): RES.008 / RES.005 / UCT pages all HTTP 200 but JSON-LD block INVALID ("Extra data" at char 2128 / 811 / 513), `<\/script>` literal present, MathJax config swallowed.
- The reviewer additionally confirmed: deposited .md sha256 c5f1112e... matches GitHub branch tip; commit 9bdb608 exists (API 200); PDF valid %PDF-1.4.
- Live HTTP checks executed 2026-08-14 via script res008_p8audit.py + verify_hard_v2.py.
