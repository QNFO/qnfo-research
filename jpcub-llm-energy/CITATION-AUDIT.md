# Citation Audit — jpcub-llm-energy (QNFO.JPC.002)

**Date:** 2026-08-15
**Status:** PASS — 25/25 references verified, 0 unresolved

## 1. Verification Methods

| Method | Coverage | Result |
|:-------|:---------|:-------|
| Authoritative arXiv export (`export_citations`, arXiv metadata, never model-generated) | 19 arXiv refs | 19/19 success, keys/titles/authors/year verified |
| DataCite API (`api.datacite.org/dois/{doi}`) | 3 JPCUB Zenodo refs | 3/3 resolve with correct titles/creators |
| Crossref API (`api.crossref.org/works/{doi}`) | 3 neuroenergetics journal refs | 3/3 resolve with correct titles/journals/years/pages |

## 2. Reference-by-Reference Status

### arXiv (19/19) — keys per refs.bib
niu2025tokenpowerbench (2512.03024) · chung2026where (2601.22076) · liu2026position (2605.11733) · wilhelm2026beyond (2603.20224) · cao2026taskspecific (2603.21389) · parakhin2026token (2603.15183) · kim2025toward (2511.17179) · faiz2023llmcarbon (2309.14393) · jiang2026llmspace (2605.05615) · shah2026crop (2604.14214) · lian2026quantization (2606.25519) · lin2025sleeptime (2504.13171) · wen2025budgetthinker (2508.17196) · miyamoto2026aligning (2602.09574) · wang2026conformal (2602.03814) · han2024tokenbudgetaware (2412.18547) · alomrani2025reasoning (2507.02076) · desislavov2021compute (2109.05472) · patterson2021carbon (2104.10350) — all exist, metadata authoritative.

### Zenodo (3/3) — DataCite-verified
| Key | DOI | DataCite title match | Publisher | Year |
|:----|:----|:---------------------|:----------|:-----|
| qnfo2026joules | 10.5281/zenodo.21637028 | PASS (P0) | Zenodo | 2026 |
| qnfo2026jpcubcl | 10.5281/zenodo.21821767 | PASS (Competitive Landscape v2.0) | Zenodo | 2026 |
| qnfo2026qudit | 10.5281/zenodo.21880104 | PASS (Qudit Advantage) | QNFO | 2026 |

### Journal (3/3) — Crossref-verified
| Key | DOI | Title match | Venue | Year |
|:----|:----|:------------|:------|:-----|
| kety1948nitrous | 10.1172/JCI101994 | PASS | J. Clin. Invest. 27(4):476–483 | 1948 |
| raichle2006brain | 10.1146/annurev.neuro.29.051605.112819 | PASS (Brain Work and Brain Imaging) | Annu. Rev. Neurosci. 29 | 2006 |
| herculano2009human | 10.3389/neuro.09.031.2009 | PASS (The human brain in numbers) | Front. Hum. Neurosci. 3:31 | 2009 |

## 3. Findings

- **SOFT (KG hygiene):** the KG `nodes` row for `qwave-qudit-advantage` carries `zenodo_doi: 10.5281/zenodo.21827737` while the authoritative `doi` field and DataCite both confirm **10.5281/zenodo.21880104** as the live record. Consistent with the known title-mismatch history on 21827737 (system prompt canonical case). refs.bib cites 21880104 — correct. Recommend KG field correction in a follow-up cycle.
- **No HARD findings.** No hallucinated authors, wrong years, wrong venues, or fabricated IDs.
