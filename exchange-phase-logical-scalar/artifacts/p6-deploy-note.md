# P6 Deploy Note — QNFO.RES.010 (exchange-phase-logical-scalar)

**Date:** 2026-08-15 | **WBS:** QNFO.RES.010 | **Branch:** res/paper/exchange-phase-logical-scalar
**Post-P5 deploy status:** P6 (KG node seeding + Vectorize indexing) — per research skill v2.96 mandates (PUBLICATION-KG-INDEX-GAP-1, Edge Seeding Gate, VECTORIZE-WEBHOOK-VERIFY-1).

## 1. KG node seeding — DONE (verified same-turn)

| Item | Result |
|---|---|
| Node `paper:exchange-phase-logical-scalar` | `nodesInserted: 1` (sync 200) |
| Properties | slug, wbs_code QNFO.RES.010, doi + zenodo_doi 10.5281/zenodo.21941238, status published, branch, repo, published 2026-08-14 |
| BELONGS_TO edge → `prog-res` (QNFO Research Archive, wbs QNFO.RES) | `edgesInserted: 1` (sync 200) |
| Verify (Edge Seeding Gate) | `query_graph(neighbors)` count = **1**, outgoing BELONGS_TO ✓ |

## 2. Vectorize indexing — DONE (verified same-turn, canonical webhook)

| Item | Result |
|---|---|
| Endpoint | `https://qnfo-paper-indexer.q08.workers.dev/webhook?slug=exchange-phase-logical-scalar` |
| Auth | `X-Index-Token` shared-secret (AI-ENDPOINT-AUTH-1) + browser User-Agent (VECTORIZE-403-MISDIAGNOSIS: 403/1010 = missing UA, not token) |
| Result | `{"success":true,"indexed":true,"skipped":false,"chunks":23,"body_len":16644,"errors":0}` |
| Canonical verify | webhook indexed/chunks (directional search_papers MCP NOT sufficient — VECTORIZE-SILO-1) ✓ |

## 3. Zenodo related_identifiers retry — STILL BLOCKED (documented)

- Retried 2026-08-15 on a fresh throwaway draft: `PUT` metadata containing `related_identifiers` (isSupplementTo GitHub URL) → **HTTP 500** (error_id 4d66141261794bfab7d06f9075e05295). Discard 204.
- This is the same systemic deposit-API failure isolated in P5 (4 drafts, 6 payload variants, both schemes; minimal control without `related_identifiers` = 200). **Local hypotheses exhausted per BLAME-EXTERNAL-1; genuine Zenodo-side bug.**
- Active remediation: GitHub provenance URL embedded in the published record's description text (v2, 10.5281/zenodo.21941238). Structured `isSupplementTo` link queued for a future newversion once the API recovers.

## 4. Residual deferred (carried from P5 closeout)

- S1–S4 SOFT items (post-publication-audit.md): kirchner2025 bib/body, Spencer-Brown 1969 bib entry, keywords 7→6, fit-verify s=1/4 case.
- Abstract 253 words (soft over 250).
- P7 dissemination (SEO/social/Internet Archive) + P8 distribution (R2 archive, KG/D1 records final) — not yet executed.

## 5. P6 gate

**PASS** — KG node exists with ≥1 BELONGS_TO edge (verified neighbor count 1); Vectorize indexed (chunks 23, errors 0, canonical webhook verify). PUBLICATION-KG-INDEX-GAP-1 closed.
