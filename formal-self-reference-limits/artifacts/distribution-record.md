# Distribution Record — QNFO.RES.008 Formal Self-Reference Limits

**WBS:** QNFO.RES.008.P6 (Distribution)
**DOI:** 10.5281/zenodo.21929689
**Date:** 2026-08-14
**Paper URL:** https://papers.qnfo.org/papers/formal-self-reference-limits

## 4-D Distribution Status

| Channel | Status | Evidence | Notes |
|:--------|:-------|:---------|:------|
| **Zenodo** | ✅ DONE | doi.org HEAD 200 → zenodo.org/records/21929689 | 21 files, P5.FRESH PASS (Phase 5) |
| **GitHub** | ✅ DONE | branch res/paper/formal-self-reference-limits @ 2759d49, 6 tags | v0.1-phase0..v0.6-phase5 |
| **R2 archive** | ✅ DONE | rclone check 0 differences, 21 files | qnfo-releases/releases/2026/08/formal-self-reference-limits |
| **papers.qnfo.org** | ✅ DONE | HTTP 200, ScholarlyArticle JSON-LD | https://papers.qnfo.org/papers/formal-self-reference-limits |
| **D1 living-paper** | ✅ DONE | body 29,991 chars, status published | identifier formal-self-reference-limits |
| **Vectorize** | ✅ DONE | webhook dedup "unchanged" = presence | qnfo-paper-indexer |
| **KG node + edge** | ✅ DONE | paper:formal-self-reference-limits BELONGS_TO prog-res (1 edge) | verified via graph-api |
| **IndexNow** | ✅ DONE | HTTP 202 (accepted) | Bing/Yandex/Seznam/Naver; key fea6716717dc42059213070adcdf0e53 |
| **Internet Archive** | ✅ DONE | CDX capture 20260814073831, HTTP 200, 16,411 B | https://web.archive.org/web/20260814073831/https://papers.qnfo.org/papers/formal-self-reference-limits |
| **IPFS (Pinata)** | ⏸ DEFERRED | PINATA_API_KEY not configured on this machine | No CID minted; re-attempt when token available (RES.005 precedent: documented deferral) |
| **Arweave** | ⏸ DEFERRED | No wallet/token available | Re-attempt when infra available |
| **DNSLink** | ⏸ DEFERRED | Requires IPFS CID; script hardcodes core-pillar CIDs only | Re-attempt with minted CID |

## Verification Evidence

- **IndexNow:** `POST https://api.indexnow.org/indexnow` → HTTP 202 with host papers.qnfo.org, key fea6716717dc42059213070adcdf0e53, urlList [paper URL, /papers/, /]. (2026-08-14, same-turn)
- **Internet Archive:** `node internet-archive-submit.js <url>` → HTTP 200 snapshot request; CDX query via browser (load_url on web.archive.org/cdx/search/cdx) → single capture row `20260814073831, http 200, 16411 bytes`. Python CDX/availability APIs were 429/timeout (documented archive.org rate-limit pattern, research skill v2.102).
- **R2:** rclone check 0 differences / 21 matching files at qnfo-releases:qnfo-releases/releases/2026/08/formal-self-reference-limits.

## Deferred Items

1. IPFS pin (needs PINATA_API_KEY/PINATA_API_SECRET) → then DNSLink TXT `_dnslink.formal-self-reference-limits` → then Arweave (needs wallet).
2. Wayback deep-verification via browser if the capture needs re-confirmation.
3. Google discovery relies on robots.txt Sitemap + linked crawl (per indexnow-submit.py note) — no direct ping (legacy endpoints dead).
