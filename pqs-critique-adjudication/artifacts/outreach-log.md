# Outreach / Dissemination Evidence Log — QNFO.RES.016

**Project:** Post-Quantum Synthesis Critique Adjudication · DOI 10.5281/zenodo.22010489 (concept 10.5281/zenodo.22009652)
**Phase 7 dissemination executed:** 2026-08-19 · **Log discipline:** Tool-Call Execution Mandate — every send's API response IS the proof.

---

## 1. Buffer social posts (all 3 channels, queued)

| Channel | Post ID | Status | Evidence |
|:--------|:--------|:-------|:---------|
| LinkedIn (Rowan Brad Quni-Gudzinas, `6a170337…`) | `6a85acd8ae66772154dd5450` | scheduled | createPost → PostActionSuccess |
| X (RowanQuni, `685cd2c2…`) | `6a85acd9ae66772154dd5472` | scheduled | createPost → PostActionSuccess |
| Mastodon (QNFO, `6a660e1b…`) | `6a85acd972f1f87674af9564` | scheduled | createPost → PostActionSuccess |

Post text (per channel, same core): *"New paper: 'Five Objections, One Standard' — an evidence-graded adjudication of a five-point critique of the Post-Quantum Synthesis framework. Each objection was tested against primary sources; two fail verification of their own premises, one (the missing measurement mechanism) is confirmed in substance. Reusable four-grade critique rubric included. DOI: 10.5281/zenodo.22010489"* — plain scholarly prose, SO-WHAT + premise-depth in prose (PUBLICATION-PROSE-GATE-1 compliant; no spam tokens).

## 2. Zenodo community inclusion requests (curator-gated)

| Community | Request ID | Status | Evidence |
|:----------|:-----------|:-------|:---------|
| advancedtheoreticalphysicsandmathematics (1004 rec) | `7be12518-6b2a-44cb-8a3f-4aae9528c8d8` | submitted | POST /records/22010489/communities → 200 |
| tp-a-m-c (745 rec) | `a9726f22-b0a7-4aeb-b05e-6c8b5b8b697c` | submitted | POST → 200 |
| fbt-framework (366 rec, geometric foundations of QT) | `ced3c30f-2dfe-43e1-a1ce-72609d718219` | submitted | POST → 200 |

Acceptance is curator-gated (ZENODO-COMMUNITY-INCLUSION-REQUEST-1); membership pending. Verify via `GET /api/requests?q=topic.record:22010489` (3 submitted as of 2026-08-19 13:30 UTC).

## 3. Internet Archive save

- URL: `https://web.archive.org/save/https://papers.qnfo.org/papers/pqs-critique-adjudication/`
- Result: HTTP 200, captured `https://web.archive.org/web/20260819131759/https://papers.qnfo.org/papers/pqs-critique-adjudication/`

## 4. PhilPapers discoverability — keyword amendment (in-place metadata edit)

- Before: 10 keywords, 1 philosophy-domain (`philosophy of physics`) — below PhilPapers ≥3 threshold.
- Action: deposit-API edit cycle (actions/edit → full-metadata PUT → publish), added `foundations of quantum mechanics`, `philosophy of science`, `philosophy of mathematics`.
- After: 13 keywords, 4 philosophy-domain. DataCite verified: 13 subjects, version 1.1 preserved, GitHub provenance `isSupplementTo` intact (PARTIAL-PUT-CLEARS-FIELDS-1 discipline).
- Same DOI; no file changes.

## 5. SEO audit (papers.qnfo.org)

| Leg | Result |
|:----|:-------|
| robots.txt | HTTP 200, Sitemap line present |
| sitemap.xml | HTTP 200 (160,640 B), slug `pqs-critique-adjudication` present |
| llms.txt | HTTP 200 (38,979 B), slug present |
| Paper page | HTTP 200; JSON-LD valid (ScholarlyArticle, DOI 22010489); citation_doi/citation_title/citation_author/citation_publication_date/citation_publisher + og:title/type/url/description **added via gateway bundle patch + redeploy** (version 62167995) |

**SEO remediation note (2026-08-19):** the local canonical gateway bundle lacked `citation_*` Scholar metas that the previously-deployed (JSON-LD-broken) bundle carried; the fix-branch source also lacked them. Patched `C:\Users\LENOVO\.deepchat\gateway-deploy\qnfo-gateway.js` (added `citationAuthorsMeta` helper + meta block), redeployed (62167995), verified live: JSON-LD valid + all 6 citation metas + og tags present. Site-wide improvement (all paper pages).

## 6. Email outreach

**NONE — not executed.** Per EMAIL & OUTREACH DETECTION-ONLY MANDATE (2026-08-13): no outreach emails without explicit user approval. This log records only autonomous non-email dissemination.

---

## Status summary

| Leg | Status |
|:----|:-------|
| Buffer (3 channels) | ✅ scheduled |
| Zenodo communities (3) | ✅ submitted (curator-gated) |
| Internet Archive | ✅ saved |
| PhilPapers keywords | ✅ 13 (4 philosophy-domain) |
| SEO | ✅ full pass + gateway meta remediation |
| Email outreach | ⛔ not executed (detection-only mandate) |
