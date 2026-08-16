# Adversarial Review Addendum — QNFO.RES.012 (research-purpose-utility)

Independent CMD RED TEAM SUB reviewer · delegation 4KwZv0azENID5z_J9531D · 2026-08-16 · Verdict: **PASS (0 HARD)**
Complements the in-deposit `red-team.md` (P4.5) and `post-publication-audit.md` (concurrent session, 1db8fbc).

## Verified (all live, 2026-08-16)
- Zenodo `records/21964824`: state=done, status=published, exact title, creator Rowan Brad Quni-Gudzinas ORCID 0009-0002-4317-5604 (QNFO Research Foundation).
- **15/15 files present** (md5 checksums; total 2,637,042 B).
- `doi.org/10.5281/zenodo.21964565` HEAD 200 → resolves to LATEST (21964824). DataCite both DOIs state=findable.
- Deposited `.md`: frontmatter `doi: "10.5281/zenodo.21964824"` (own DOI, NEWVERSION-FRONTMATTER-CARRYOVER-1 clean), status published, **no `<RESERVED>` placeholder** (ZENODO-PLACEHOLDER-DOI-1 clean).
- **Byte-parity:** GitHub raw md sha256 `dad3827f…` == Zenodo deposited md sha256.
- `related_identifiers` carries `isSupplementTo` → GitHub branch URL (resolves 200; DESIGN note: branch `res` doesn't exist literally — GitHub longest-branch-match resolves `res/paper/research-purpose-utility`; fragile if a literal `res` branch is created).
- R2 mirror `papers.qnfo.org/papers/research-purpose-utility/` 200 with ScholarlyArticle JSON-LD; KG resolve → slug research-purpose-utility, status published, r2_key correct. R2-MIRROR-AFTER-PUBLISH-1 satisfied.
- **Broadcast:** Bluesky post `at://did:plc:vad2yeqflg5uznmp557zge5c/app.bsky.feed.post/3mt72gu23sb2d` verified LIVE via public API (2026-08-16T11:10:23Z). Copy claims map 1:1 to the abstract (falsifiable test = F1–F3; live grounding path = G1; declared premise chain = G2/L0–L2; no silo legitimacy = G3). **No overclaim** — copy does not claim a theorem/proof.
- `references.bib` = 29 entries, AUTHOR-GATE consistent.

## SOFT findings (deferred — fix in a consolidated v3 newversion; none blocking)
1. **Deposited README.md is STALE (priority):** says "Zenodo preprint (draft)" + "Publication status: Draft (P5 artifacts built; P6 Zenodo deposit + R2 mirror pending)" on a PUBLISHED record. Fix wording to published status.
2. **Zenodo metadata `license: null`** while .md frontmatter declares QNFO-ULA. Landing page shows no license. (QNFO-ULA is not a Zenodo registry license id — decide canonical license before v3.)
3. **No How-to-Cite block** in README.md or .md (ZENODO-CONCEPT-DOI-CITE-1 not violated — no block exists at all; must add concept-DOI cite block in v3).
4. `metadata.version: null` — set a semantic version in v3.
5. GitHub branch has 3 files NOT in the deposit: `artifacts/dissemination-posts.md` (broadcast source — arguably should be deposited per PUBLICATION-SOURCE-COMPLETENESS-1 "when in doubt include everything"), `artifacts/post-publication-audit.md`, `artifacts/zenodo-remediation-pending.md` (post-publication; fine to remain out).

## Non-blocking risks (documented)
- Buffer scheduled posts (LinkedIn/X/Mastodon) unverifiable via API from this session — dispatch responses recorded in `dissemination-posts.md` (post ids 6a819aa1…, 6a819aa1…, 6a819aa2…).
- KG `distribution_status` flag not directly queryable from this session's tooling; KG node properties confirm distributed via query_graph.

## Verdict
**PASS — 0 HARD.** Record is publication-clean on accuracy, completeness, dependency, and dissemination integrity. SOFT items queued for a consolidated v3 polish newversion (README status + license + How-to-Cite + version + optional dissemination-posts.md deposit).
