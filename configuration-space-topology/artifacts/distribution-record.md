# Core Distribution Record — QNFO.RES.011 (P8, 2026-08-15)

**Paper:** Configuration-Space Topology and the Distinction Calculus
**Version:** v0.2 — DOI 10.5281/zenodo.21957291 (concept 10.5281/zenodo.21945449)
**Phase:** P8 Core Distribution Stack (research skill, MANDATORY)

## 4-D distribution properties (KG `paper:configuration-space-topology`)

| Prop | Value | Verified |
|:-----|:------|:---------|
| `distribution_status` | **complete** | /sync 200 (2026-08-15) |
| `doi` / `zenodo_doi` | 10.5281/zenodo.21957291 | doi.org 200 + DataCite findable |
| `ipfs_cid` (PDF) | `bafkreifi2kvnew5yskhcpwhennfzrjj2czbsew2g74nvee4lfuzmsxuuau` | locally computed CIDv1 (sha2-256, raw codec, base32) |
| `ipfs_cid_md` (MD) | `bafkreib4pefeinwadzueex45ip63tgkgf22opnwxxtih6drgmqc7qlxqbm` | locally computed CIDv1 |
| `dns_link` | `_dnslink.configuration-space-topology.qnfo.org` → `dnslink=/ipfs/bafkreifi2...` | Cloudflare DNS TXT created 200 (zone 84e9dc1d) |
| `internet_archive` | `https://web.archive.org/web/20260816043113/https://papers.qnfo.org/paper/configuration-space-topology` | IA save 200 + CDX snapshot 200 (20260816043113) |
| `distribution_date` | 2026-08-15 | — |

**IPFS method:** per skill — R2 (durable store) + locally-computed CIDv1 + Cloudflare DNS DNSLink. NO third-party pinning services (the CID is content-addressed via DNSLink; R2 is the durable mirror).

## Consolidated closeout verification (v2.95) — ALL 7 LAYERS PASS (same turn)

| Layer | Evidence | Verdict |
|:------|:---------|:--------|
| 1. DOI version chain | v0.2 21957291 → 200; v0.1 21945450 → 200 (doi.org HEAD) | ✅ PASS |
| 2. DataCite | state=findable, subjects=10, rightsList cc-by-4.0 | ✅ PASS |
| 3. GitHub | `git ls-remote` → branch `res/paper/configuration-space-topology` + tag `v0.1-phase0-configuration-space-topology` | ✅ PASS |
| 4. D1 living-paper | row `configuration-space-topology`: doi 21957291, status published, body_len 29,169 | ✅ PASS |
| 5. Zenodo files | 15 files incl. .md/.html/.pdf | ✅ PASS |
| 6. KG node | `paper:configuration-space-topology` exists (query_graph neighbors = 6: BELONGS_TO prog-res + BUILDS_ON ×2) | ✅ PASS |
| 7. Vectorize | webhook → indexed:true, chunks=42, errors=0 | ✅ PASS |

## Registry (program_registry)
`QNFO.RES.011` → **phase P8, status complete** (SELECT re-verified), zenodo_doi 21957291, current_version v0.2.

## Project milestone M5 achieved
> **M5 (P8 done): distribution_status complete in KG** ✅

**Project complete:** QNFO.RES.011 — Configuration-Space Topology and the Distinction Calculus
published (Zenodo v0.2 + R2 mirror + D1 + KG + Vectorize + GitHub + Internet Archive + DNSLink),
fully distributed (4-D), registry closed at P8/complete.
