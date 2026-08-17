# Dissemination Record — QNFO.INM.001 v0.3 (P7, 2026-08-17)

**DOI:** 10.5281/zenodo.21974194 (concept 10.5281/zenodo.21931224) · **Branch:** res/paper/signal-worker-boundary-confinement @ 711d5e5

---

## 1. Zenodo Community Inclusion Requests (D3 — verified open for third-party REQUEST; curator-gated per ZENODO-COMMUNITY-INCLUSION-REQUEST-1)

| Community | Records | Submitted | Request created | Status |
|:----------|--------:|:---------:|:----------------|:-------|
| `fbt-framework` (Geometric Foundations of Quantum Theory and Gravity — direct UMP/RES match ★) | 366 | ✅ HTTP 200 | 2026-08-17T07:11:16 | submitted (curator-gated) |
| `tp-a-m-c` (Theoretical/Applied/Mathematical/Computational) | 745 | ✅ HTTP 200 | 2026-08-17T07:11:21 | submitted (curator-gated) |
| `advancedtheoreticalphysicsandmathematics` | 1004 | ✅ HTTP 200 | 2026-08-17T07:11:24 | submitted (curator-gated) |

Report confirms: 3 REQUEST entries (submitted), 0 MEMBER yet. Acceptance = community curators (out of our control; check via `report`).

## 2. Social Broadcast (D7 — so-what-first copy per user mandate; QNFO-owned handles only, TEST-SEND-EXTERNAL-1 compliant)

| Platform | Status | Evidence |
|:---------|:-------|:---------|
| **Bluesky** (@qnfo.bsky.social) | ✅ **POSTED** | `at://did:plc:vad2yeqflg5uznmp557zge5c/app.bsky.feed.post/3mtbkxtyiri2s` — 290 graphemes |
| Mastodon | ⏭ SKIPPED | No credentials found (env/keys.json/~/.mastodon_creds.json/.env all absent) |
| X / LinkedIn (Buffer) | ⏳ PENDING | Buffer MCP token valid (mcp-settings.json + env `BUFFER_TOKEN` match); `npx mcp-remote` raw-stdio path times out in this session; REST API rejects MCP token (401, deprecated 2027-02-01). Scheduling requires a session with the Buffer MCP tools exposed (RES.011 precedent). |

**Bluesky copy (so-what first):** "Corrected surface-vs-bulk ontology: 'electrons confined to the boundary' holds for topological insulators, QH & NHSE - but is a category error for Meissner & skin effect. That distinction decides which boundary phenomena carry quantized transport. 3 pre-registered predictions. https://doi.org/10.5281/zenodo.21974194 #OpenScience #TopologicalInsulators #NonHermitianPhysics"

## 3. Indexing Verification (playbook D4)

| Index | Status | Evidence |
|:------|:-------|:---------|
| **OpenAIRE EXPLORE** | ✅ **INDEXED** | total=1 (live query 2026-08-17) — confirmed indexer for QNFO corpus |
| DataCite | ✅ findable v0.3 | api.datacite.org state=findable, registered 2026-08-17T05:43:19Z |
| CrossRef | ⏳ async | 404 on publish-day — Zenodo→DataCite→CrossRef propagation is days-to-weeks; PhilPapers crawls CrossRef (re-check in ~1-2 weeks) |
| Semantic Scholar | ❌ known gap | S2-ZENODO-GAP-1: S2 does not index 10.5281/zenodo.* DOIs at all (engine-wide) — do NOT retry |

## 4. Next actions

- Re-run `zenodo-communities.py report --doi 10.5281/zenodo.21974194` after ~1 week to check curator acceptance.
- Schedule X/LinkedIn Buffer posts from a session with Buffer MCP tools exposed (copy prepared above, so-what-first).
- Re-check CrossRef/PhilPapers in ~2 weeks (crawl cycle days-to-weeks).
