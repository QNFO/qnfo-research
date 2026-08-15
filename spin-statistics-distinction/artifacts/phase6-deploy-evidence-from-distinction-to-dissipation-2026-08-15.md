# Phase 6 Deploy Evidence — from-distinction-to-dissipation (2026-08-15)

- **qa-ux-battery (research skill HARD gate):** `qa-ux-battery.py --urls https://papers.qnfo.org/papers/from-distinction-to-dissipation/` → **rc=0, 1/1 PASS** (HTTP 200, VRD PASS, 0 console errors, 0 page errors, 0 broken links, title/h1 present).
- **KG node:** `paper:from-distinction-to-dissipation` seeded via graph-api sync (nodesInserted 1) + `BELONGS_TO prog-qnfo-slb` (edgesInserted 1); verified via query_graph nodes search.
- **Vectorize:** `GET qnfo-paper-indexer.q08.workers.dev/index?slug=from-distinction-to-dissipation` (X-Index-Token + browser UA) triggered; verified `search_papers_enriched` returns the suite as the top hit (score 0.659) and `/webhook?slug=` reports indexed state.
- **D1 body_md** synced to the v1.3 essay (frontmatter doi 10.5281/zenodo.21941150); read-back verified.
