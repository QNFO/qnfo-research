# CMD RED TEAM — 5-Adversary Direct Audit Report (QNFO.RES.007)

**Date:** 2026-08-14 · **Mode:** READ-ONLY audit → findings → remediation (permanent)
**Scope:** Vectorize indexing + all session issues/errors (indexer 403, IndexNow keyfile, frontmatter DOI, D1/registry consistency, version chain)
**Adversaries:** Accuracy · Completeness · Dependency · Novelty · Status

---

## VERDICT: 4 HARD findings → all remediated. 2 SOFT → 1 fixed, 1 documented.

---

## Accuracy

| # | Finding | Severity | Status |
|:--|:--------|:---------|:-------|
| A1 | **Vectorize "403/token-rotated" claim was FALSE.** Root cause: default Python urllib User-Agent triggers Cloudflare Browser Integrity Check (error 1010). Token `chnx-idx-v1-k9m2n4p7r5t8` is valid; with browser UA the webhook returns `200 {success:true, skipped:true, reason:"unchanged"}` = paper indexed with CURRENT content. | HARD | ✅ FIXED — corrected memory (VECTORIZE-403-MISDIAGNOSIS) + verified 200 with UA |
| A2 | D1 body_md == repo manuscript exactly (14,545 chars, 0 diff opcodes) — no drift. | PASS | ✅ verified |
| A3 | fit-verify numbers match BP-1 claims (e series 2.718281828459, Machin π 3.141592653590, Euler 1.225e-16). Reviewer cross-checked all 29 DOIs live. | PASS | ✅ verified |

## Completeness

| # | Finding | Severity | Status |
|:--|:--------|:---------|:-------|
| C1 | IndexNow keyfile at `papers.qnfo.org/{key}.txt` served **SPA HTML** instead of raw key → Bing/Yandex key validation would fail despite HTTP 202. | HARD | ✅ FIXED — deployed `qnfo-indexnow-key` worker + exact-match route; keyfile now `text/plain` raw key (200, verified) |
| C2 | Vectorize content completeness: all 7 manuscript sections present in indexed content (C3 derivation, Picard, kernel 2πℤ, falsifiability). | PASS | ✅ verified (21 chunks, 0 errors) |
| C3 | Zenodo deposit file sets: v0.3 has all 14 files (md/pdf/html + bib + audit + bp-gates + registry + evidence). | PASS | ✅ verified |

## Dependency

| # | Finding | Severity | Status |
|:--|:--------|:---------|:-------|
| D1 | **Race-condition phantom DOI**: commit a4373e1 set frontmatter DOI to 21929902 while it was still an unsubmitted draft (public API 404); my audit fix b3619e0 then set 21929590 (v0.2) — but the concurrent session PUBLISHED v0.3 (21929902) mid-audit, making the v0.2 DOI stale. | HARD | ✅ FIXED — commit 5379ec8 syncs repo manuscript byte-identical to the v0.3 deposit (frontmatter 21929902); D1 + program_registry updated to v0.3 (verified by re-query) |
| D2 | Indexer worker exists (`qnfo-paper-indexer` in account), route `papers.qnfo.org/*` → `qnfo-gateway`; deployed gateway ≠ local source (stale local) — do NOT deploy from local. | PASS | ✅ documented |
| D3 | Zenodo version chain: v0.1 (21929479) → v0.2 (21929590) → v0.3 (21929902), all resolve 200, concept 21929478. | PASS | ✅ verified |

## Novelty

| # | Finding | Severity | Status |
|:--|:--------|:---------|:-------|
| N1 | No new scientific claims introduced by this cycle's fixes — all changes are provenance/metadata/plumbing corrections. C3 `[UNIQUE-CLAIM]` burden unchanged (constructive derivation in manuscript). | PASS | ✅ n/a |

## Status

| # | Finding | Severity | Status |
|:--|:--------|:---------|:-------|
| S1 | All layers now agree on v0.3/21929902: Zenodo latest, GitHub 5379ec8, D1 living-paper (v0.3, body 14,545), program_registry (v0.3-published, P8), KG (published), Vectorize (indexed, unchanged), R2 (7 files, rclone 0 diff), papers-server 200. | PASS | ✅ verified 7/8 earlier → 8/8 after UA fix (the single earlier FAIL was the same 403 misdiagnosis) |
| S2 | Working tree clean, local == remote (5379ec8). | PASS | ✅ verified |
| S3 | SOFT: dissemination-log.md/journal-strategy reference v0.2 (21929590) — historical record of the dissemination action, not a defect; next update cycle will reference v0.3. | SOFT | 📋 documented |

## Root-cause chain (why these happened)

1. **VECTORIZE-403-MISDIAGNOSIS** — earlier session called the indexer without a browser UA → 1010 BIC → concluded "token rotated" without testing UA hypothesis (BLAME-EXTERNAL-1 discipline gap). Fix: documented UA requirement + corrected memory; skill kaizen pending.
2. **IndexNow keyfile HTML** — papers.qnfo.org SPA fallback serves index.html for unknown paths; keyfile route never existed. Fix: dedicated worker + exact route (non-destructive to gateway).
3. **Race-condition DOI** — two sessions concurrently remediating the same manuscript; draft DOI in frontmatter before publish, then published mid-audit. Fix: byte-sync from the published deposit as the canonical source; registry + D1 re-verified.

## Remediation commits
- `5379ec8` — manuscript + registry reconciled to v0.3 (21929902); D1 + program_registry updated (verified)
- `b3619e0` — intermediate frontmatter fix (superseded by 5379ec8)
- Worker `qnfo-indexnow-key` deployed + route added (8353174fc929496dbe9fbae72d3b6efa)

## Residual / follow-up
- Research skill VECTORIZE-WEBHOOK-VERIFY-1: add browser-User-Agent requirement (kaizen item).
- dissemination-log references v0.2 DOI (historical, correct for its date).
- No other open findings.
