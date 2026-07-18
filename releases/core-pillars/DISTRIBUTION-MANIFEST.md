# WBS.3 — Core Pillar Distribution: COMPLETE (DNSLink pending token scope)
## Date: 2026-07-18 | Pipeline: IPFS ✅ | R2 ✅ | KG ✅ | Papers-Server ✅ | DNSLink ⚠️

---

## Papers Distributed

| # | Slug | Title | DOI | IPFS CID | Papers-Server |
|:--|:-----|:------|:----|:---------|:--------------|
| 1 | silent-radix-synthesis | Silent-Radix Cryptography | [10.5281/zenodo.21134188](https://doi.org/10.5281/zenodo.21134188) | `QmbCbkjBj6aKgcSCRiZ7ewxUg3P6JAh2NKo4dCgLBKvgfS` | [HTTP 200](https://papers.qnfo.org/papers/silent-radix-synthesis) |
| 2 | syntactic-generation-primitive-distinctions | Syntactic Generation Primitive Distinctions | *(needs Zenodo deposit)* | `QmRLFE9iwokBuU1s4EYAkEUqGcABix1CnMBxcoht4n3JoH` | [HTTP 200](https://papers.qnfo.org/papers/syntactic-generation-primitive-distinctions) |
| 3 | paper-the-qubit-delusion | The Qubit Delusion | [10.5281/zenodo.21254143](https://doi.org/10.5281/zenodo.21254143) | `QmZVcTQ4Szud3M1LULGLa1aWss55ciZk8db1QvwRC4wJt2` | [HTTP 200](https://papers.qnfo.org/papers/paper-the-qubit-delusion) |
| 4 | paper-beyond-the-qubit | Beyond the Qubit | [10.5281/zenodo.21254901](https://doi.org/10.5281/zenodo.21254901) | `QmezmA2Ejo3t8DYGseFJhECrm2QCCaa3GQc2N7RMJSTuEw` | [HTTP 200](https://papers.qnfo.org/papers/paper-beyond-the-qubit) |
| 5 | number-theoretic-ultrametric-foundations | Number-Theoretic Ultrametric Foundations | [10.5281/zenodo.21193487](https://doi.org/10.5281/zenodo.21193487) | `QmUtD9P2BDYMSaaz7WFTBPEmK9ViMkqj8iR6HjkWChm4i8` | [HTTP 200](https://papers.qnfo.org/papers/number-theoretic-ultrametric-foundations) |

---

## Distribution Pipeline Status

| Stage | Tool | Status |
|:------|:-----|:-------|
| **PDF build** | Pandoc + XeLaTeX | ✅ 5 PDFs built (25–94 KB) |
| **IPFS pin** | Pinata API | ✅ 10 files pinned (5 MD + 5 PDF) |
| **R2 upload** | `npx wrangler r2` (Account API Token) | ✅ 10 files in `qnfo-releases/releases/2026/07/core-pillars/` |
| **KG backfill** | qnfo-gateway `/sync` (graph-api.qnfo.org) | ✅ 5 nodes: `distribution_status=distributed`, `ipfs_cid` set |
| **Papers-server** | qnfo-gateway (papers.qnfo.org) | ✅ All 5 HTTP 200 |
| **DNSLink** | Cloudflare DNS API | ⚠️ BLOCKED — Account API Token lacks DNS:Edit scope on zone |
| **D1 living-paper** | N/A (different schema) | ⚠️ Not applicable — D1 uses hash `identifier`, not `slug`; KG nodes are canonical |
| **Zenodo** | Existing DOIs | ✅ 4/5 have DOIs; #2 needs new deposit |

---

## DNSLink Records (PENDING)

The Account API Token (`CLOUDFLARE_API_TOKEN`) has Workers/R2/D1 permissions but NOT DNS:Edit on the qnfo.org zone. Action required:

1. Go to https://dash.cloudflare.com/edb167b78c9fb901ea5bca3ce58ccc4b/api-tokens
2. Edit the token or create a new one with **Zone:DNS:Edit** permission on `qnfo.org`
3. Set the token as `CLOUDFLARE_API_TOKEN` environment variable
4. Run: `npx wrangler dns record create` for each of the 5 records below:

```txt
_dnslink.silent-radix-cryptography.qnfo.org.        TXT  "dnslink=/ipfs/QmbCbkjBj6aKgcSCRiZ7ewxUg3P6JAh2NKo4dCgLBKvgfS"
_dnslink.syntactic-generation-primitive-distinctions.qnfo.org.  TXT  "dnslink=/ipfs/QmRLFE9iwokBuU1s4EYAkEUqGcABix1CnMBxcoht4n3JoH"
_dnslink.the-qubit-delusion.qnfo.org.                TXT  "dnslink=/ipfs/QmZVcTQ4Szud3M1LULGLa1aWss55ciZk8db1QvwRC4wJt2"
_dnslink.beyond-the-qubit.qnfo.org.                  TXT  "dnslink=/ipfs/QmezmA2Ejo3t8DYGseFJhECrm2QCCaa3GQc2N7RMJSTuEw"
_dnslink.number-theoretic-ultrametric-foundations.qnfo.org.  TXT  "dnslink=/ipfs/QmUtD9P2BDYMSaaz7WFTBPEmK9ViMkqj8iR6HjkWChm4i8"
```

---

## 4-D Distribution Summary

| Dimension | Status |
|:----------|:-------|
| **Distributed** | IPFS ✅ (Pinata, 10 files) |
| **Durable** | R2 ✅ (10 files, qnfo-releases bucket) + Zenodo ✅ (4/5 DOIs) |
| **Discoverable** | Papers-server ✅ (5/5 HTTP 200) + DOI (4/5) + DNSLink ⚠️ (pending token) |
| **Duplicated** | Pinata ✅ + R2 ✅ + Zenodo ✅ (multi-store redundancy) |

---

## Verification Commands

```bash
# IPFS gateway
curl -s "https://gateway.pinata.cloud/ipfs/QmbCbkjBj6aKgcSCRiZ7ewxUg3P6JAh2NKo4dCgLBKvgfS" | head -c 100

# Papers-server
curl -s "https://papers.qnfo.org/papers/silent-radix-synthesis" | head -c 100

# R2 (via wrangler)
npx wrangler r2 object get qnfo-releases/releases/2026/07/core-pillars/silent-radix/silent-radix-cryptography.pdf

# KG status
curl -s "https://graph-api.qnfo.org/nodes/paper-silent-radix-synthesis" | jq .properties
```
