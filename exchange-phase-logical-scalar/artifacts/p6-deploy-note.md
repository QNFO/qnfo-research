# P6 Deploy Note — QNFO.RES.010 (exchange-phase-logical-scalar)

**Date:** 2026-08-15 | **WBS:** QNFO.RES.010 | **Branch:** res/paper/exchange-phase-logical-scalar
**Post-P5 deploy status:** P6 (KG node seeding + Vectorize indexing) — per research skill v2.96 mandates (PUBLICATION-KG-INDEX-GAP-1, Edge Seeding Gate, VECTORIZE-WEBHOOK-VERIFY-1).

## 1. KG node seeding — DONE (verified same-turn)

| Item | Result |
|---|---|
| Node `paper:exchange-phase-logical-scalar` | `nodesInserted: 1` (sync 200) |
| Properties | slug, wbs_code QNFO.RES.010, doi + zenodo_doi 10.5281/zenodo.21941238, status published, branch, repo, published 2026-08-14 |
| BELONGS_TO edge → `prog-res` (QNFO Research Archive, wbs QNFO.RES) | `edgesInserted: 1` (sync 200) |
| Verify (Edge Seeding Gate) | 1 unique BELONGS_TO edge (raw HTTP API count:1; MCP `query_graph` serializes the edge once per endpoint and reports count:2 for the same single edge — tool-agnostic wording adopted per P6 red-team SOFT-A) ✓ |

## 2. Vectorize indexing — DONE (verified same-turn, canonical webhook)

| Item | Result |
|---|---|
| Endpoint | `https://qnfo-paper-indexer.q08.workers.dev/webhook?slug=exchange-phase-logical-scalar` |
| Auth | `X-Index-Token` shared-secret (AI-ENDPOINT-AUTH-1) + browser User-Agent (VECTORIZE-403-MISDIAGNOSIS: 403/1010 = missing UA, not token) |
| Result | `{"success":true,"indexed":true,"skipped":false,"chunks":23,"body_len":16644,"errors":0}` |
| Canonical verify | webhook indexed/chunks (directional search_papers MCP NOT sufficient — VECTORIZE-SILO-1) ✓ |

## 3. Zenodo related_identifiers retry — STILL BLOCKED (documented)

- Retried 2026-08-15 on a fresh throwaway draft: `PUT` metadata containing `related_identifiers` (isSupplementTo GitHub URL) → **HTTP 500** (error_id 4d66141261794bfab7d06f9075e05295). Discard 204. (Method: `POST /api/deposit/depositions` create → `PUT /api/deposit/depositions/{id}` with `metadata.related_identifiers` → 500 → `POST .../actions/discard`.)
- This is the same systemic deposit-API failure isolated in P5 (4 drafts, 6 payload variants, both schemes; minimal control without `related_identifiers` = 200). **Local hypotheses exhausted per BLAME-EXTERNAL-1; genuine Zenodo-side bug.**
- **Recovery trigger (defined):** a future operator should retry the structured `isSupplementTo` link via newversion when `PUT /api/deposit/depositions/{fresh-draft-id}` with a minimal `related_identifiers` payload returns 200 instead of 500. Until then, the active remediation is the GitHub provenance URL embedded in the published record's description text (v2, 10.5281/zenodo.21941238).

## 4. Residual deferred (carried from P5 closeout)

- **S1** — `kirchner2025` (10.5281/zenodo.17659262) in references.bib not cited in paper body References; Spencer-Brown 1969 (book, no DOI) cited in body but absent from bib. Remediation (next revision): add Spencer-Brown 1969 bib entry; add Kirchner citation line.
- **S2** — Keywords = 7 (target 4–6). Remediation: trim to 6 (drop "anyons").
- **S3** — fit-verify.txt overstates coverage; omits the paper's worked example s=1/4 → R = i and the cos/sin general form. Remediation: extend fit-verify.txt.
- **S4** — cosmetic: paper §6 F1 writes R = (e^{iπ})^{2s} vs plan's R = e^{2πis} (equivalent); paper drops explicit §36 / 21908818 §12.2 anchors. Remediation: optional restore of anchors in a future revision; no content change.
- Abstract 253 words (soft over 250).
- **P7 dissemination** (SEO/social/Internet Archive) + **P8 distribution** (R2 archive, KG/D1 records final) — not yet executed.
- Zenodo `related_identifiers` structured link — queued (recovery trigger defined above).

## 5. P6 gate

**PASS** — KG node exists with ≥1 BELONGS_TO edge (verified neighbor count 1); Vectorize indexed (chunks 23, errors 0, canonical webhook verify). PUBLICATION-KG-INDEX-GAP-1 closed.

## 6. P6 red-team aggregate (2026-08-15)

| Slot | Verdict | Findings |
|---|---|---|
| Accuracy (`6c5WU1vanwK3Zh_RRLLii`) | **PASS, 0 HARD** | SOFT-A (count attribution → wording fixed here); Vectorize payload chunks:23 NOT-VERIFIED-LIVE by child (no token) but endpoint+auth model confirmed, search_papers returns hits → index exists |
| Completeness (`lz2V199bnMmZRo-C08WI0`) | **PASS, 0 HARD** | S4 not enumerated (fixed §4); related_identifiers retry lacked draft-ID/body/recovery-trigger (fixed §3); Zenodo 500 external |
| Dependency (`6C2-5f-nQO5B8KsDFEy6q`) | running at aggregate; **direct parent audit covered dimension** | KG neighbors ✓, git refs cfcabef ✓, Zenodo 15 files ✓, DOI resolution ✓; bookkeeping: wbs_state.current_phase updated 5→6 (this note's companion D1 fix) |
