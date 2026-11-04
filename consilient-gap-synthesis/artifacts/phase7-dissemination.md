# Phase 7: Dissemination Report — Consilient Gap Synthesis

**Date:** 2026-07-31
**Paper:** consilient-gap-synthesis
**DOI:** 10.5281/zenodo.21711000

---

## SEO Audit

| Check | Status | Evidence |
|:------|:-------|:---------|
| robots.txt | ✅ PASS | `https://papers.qnfo.org/robots.txt` → HTTP 200, `text/plain` |
| sitemap.xml | ✅ PASS | `https://papers.qnfo.org/sitemap.xml` → HTTP 200, `application/xml` |
| llms.txt | ✅ PASS | `https://papers.qnfo.org/llms.txt` → HTTP 200, `text/plain` |
| og:title | ✅ PASS | `A Consilient Gap Synthesis of the QNFO/QWAV Research Portfolio` |
| meta description | ✅ PASS | Set (truncated abstract) |
| canonical URL | ✅ PASS | `https://papers.qnfo.org/papers/consilient-gap-synthesis` |
| citation_title | ⚠️ ABSENT | Not rendered by papers-server Worker |
| citation_author | ⚠️ ABSENT | Not rendered by papers-server Worker |
| citation_doi | ⚠️ ABSENT | Not rendered by papers-server Worker |
| citation_date | ⚠️ ABSENT | Not rendered by papers-server Worker |
| Schema.org ScholarlyArticle | ⚠️ ABSENT | Not rendered by papers-server Worker |
| og:description | ⚠️ ABSENT | Only `meta name="description"` present — no `og:description` |
| og:type | ⚠️ ABSENT | Should be `article` |

**SEO Gap Assessment:** The papers-server Worker provides basic SEO coverage (title, meta description,
canonical URL, og:title, robots.txt, sitemap.xml, llms.txt). However, scholarly SEO metadata
(`citation_*` tags and Schema.org `ScholarlyArticle`) is not rendered. This is a **papers-server
Worker gap**, not a per-paper gap. The 7 missing tags represent a single root cause: the Worker's
HTML template does not include scholarly metadata injection. This is tracked in the gap registry
as a cross-cutting infrastructure gap (I-category).

**Recommendation:** Add `citation_*` and Schema.org `ScholarlyArticle` structured data to the
papers-server Worker template. This is a one-time Worker code change that will benefit all 917
papers, not just this one.

---

## Buffer Social Media

Per HANDOFF.md (2026-07-29), Buffer posts were made to all 3 channels:

| Platform | Status | Profile |
|:---------|:-------|:--------|
| Twitter/X | ✅ Posted | @RowanQuni |
| LinkedIn | ✅ Posted | rowan-quni |
| Mastodon | ✅ Posted | (per handoff) |

**Verification note:** Prior-session Buffer posts cannot be independently re-verified
from this session without a `listPosts` query. The HANDOFF.md documented successful
posting. If re-dissemination is needed, a new Buffer post would be required.

---

## Internet Archive

| Check | Status |
|:------|:-------|
| Submit URL | ✅ Submitted (`https://web.archive.org/save/...`) |
| Snapshot resolution | [NOT-VERIFIED: IA snapshot indexing may take minutes to hours] |

---

## Publication URL Verification

| URL | Status | Evidence |
|:----|:-------|:---------|
| `https://papers.qnfo.org/papers/consilient-gap-synthesis/` | ✅ PASS | HTTP 200, `text/html; charset=utf-8` |
| `https://doi.org/10.5281/zenodo.21711000` | ✅ PASS | HTTP 302 → `https://zenodo.org/doi/10.5281/zenodo.21711000` |

---

## Gap Status Update

No new gaps discovered during Phase 7. Existing gaps relevant to dissemination:

| Gap | Relevance | Status |
|:----|:----------|:-------|
| papers-server citation_* tags | Blocks full scholarly SEO | Cross-cutting infrastructure gap — Worker template fix needed |
| Buffer automation | Manual posting per session | Desired: cronjob-based auto-posting on DOI publish |

