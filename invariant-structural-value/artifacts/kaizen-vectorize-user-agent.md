# Kaizen Artifact — KIF: VECTORIZE-WEBHOOK-VERIFY-1 User-Agent Requirement

**Date:** 2026-08-14 · **Source:** CMD RED TEAM 5-adversary audit, QNFO.RES.007 (session FJ4ZYy6OEfAnpu8mq30OZ)
**Target skill:** `research` (SKILL.md on disk; NOT in skill registry — SKILL-REGISTRY-GAP-1)
**Status:** PROPOSED — requires user approval before install (kaizen protocol, Mandate 4)

## Finding

The research skill's `VECTORIZE-WEBHOOK-VERIFY-1` section documents the
qnfo-paper-indexer call as:

```
GET https://qnfo-paper-indexer.q08.workers.dev/webhook?slug=<slug>
with X-Index-Token: chnx-idx-v1-k9m2n4p7r5t8
```

It does NOT document the **User-Agent requirement**. Python's default urllib
UA triggers Cloudflare Browser Integrity Check (BIC) → HTTP 403 error 1010
for ALL paths on the worker, even with the correct token. This caused a
session to misdiagnose the failure as "token rotated" (VECTORIZE-403-MISDIAGNOSIS)
and record a false claim in memory/logs.

**Verified live (2026-08-14):** with `User-Agent: Mozilla/5.0 ...` the same
endpoint returns `200 {"success":true,"indexed":false,"skipped":true,"reason":"unchanged"}`
— the paper IS indexed with current content.

## Proposed change (one paragraph addition to VECTORIZE-WEBHOOK-VERIFY-1)

> **User-Agent requirement (2026-08-14, VECTORIZE-403-MISDIAGNOSIS):** all
> calls to `qnfo-paper-indexer.q08.workers.dev` (and any Cloudflare-worker
> HTTP call from Python) MUST send a browser-like
> `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...`
> header. The default Python urllib UA triggers Cloudflare Browser Integrity
> Check (error 1010) → HTTP 403 on every path regardless of token validity.
> A 403 from this worker is a UA problem, NOT a token problem — test the UA
> hypothesis before diagnosing token rotation (BLAME-EXTERNAL-1 discipline).
> Canonical case: QNFO.RES.007 2026-08-14 — "token-rotated" was a misdiagnosis;
> token `chnx-idx-v1-k9m2n4p7r5t8` remained valid throughout.

## Cross-reference

- Memory: `mem-8zgB6kYO4t75` (VECTORIZE-403-MISDIAGNOSIS anti-pattern)
- Audit report: `invariant-structural-value/artifacts/cmd-red-team-2026-08-14.md`
- IndexNow keyfile fix (same audit): worker `qnfo-indexnow-key` + route
  `papers.qnfo.org/fea6716717dc42059213070adcdf0e53.txt` → text/plain key

## Install path

Per Mandate 4 / kaizen protocol: this artifact must be reviewed and explicitly
approved before the research skill's SKILL.md is edited. Until approved, the
correct behavior is captured in durable memory.
