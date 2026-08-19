# Cross-System ID Validation — QNFO.RES.016

**Date:** 2026-08-19 · **Method:** resolve_paper_id per corpus hit (slug → Vectorize ID → KG ID → DOI) per DUE-DILIGENCE-DEPTH-1.

## Verified records

| Slug | Title | DOI (record) | identifier | KG node | Status | Notes |
|:-----|:------|:-------------|:-----------|:--------|:-------|:------|
| `post-quantum-synthesis` | POST QUANTUM SYNTHESIS | 10.5281/zenodo.21993491 | qnfo-2025-09-post-quantum-synthesis (arxiv) | paper:post-quantum-synthesis ✓ | published | r2 qnfo/releases/2025/09/ |
| `hydrodynamic-stability-hypothesis` | Hydrodynamic Stability Hypothesis | 10.5281/zenodo.21993494 | qnfo-2025-11-hydrodynamic-stability-hypothesis | paper:hydrodynamic-stability-hypothesis ✓ | published | r2 qnfo/releases/2025/11/ |
| `pqs-ai-evaluation-audit` | PQS AI-Evaluation Audit | 10.5281/zenodo.21535491 | — | paper:pqs-ai-evaluation-audit ✓ | published | Prior audit record (2025) |
| `non-archimedean-syntactic-paradigm-for-physics` | Non-Archimedean Syntactic Paradigm for Physics | **null in D1** | qnfo-2026-04-... (arxiv) | — | published | OpenAlex: 10.5281/zenodo.19600685/86 (2026-04-16) — **DOI missing in D1 row = data-quality finding** |
| `measure-theoretic-artifacts-archimedean-place` | Measure-Theoretic Artifacts of the Archimedean Place | 10.5281/zenodo.21595214 | — | — | published | Direct topical match (Archimedean-vs-adelic probability) |
| `strange-loop-of-being` / `strange-loop-theory-of-physical-quantization` | Strange Loop Theory of Physical Quantization | 10.5281/zenodo.21993496 | — | — | published | SSRN 5821702 candidate (PQS family) |

## KG edges (query_graph neighbors, paper:post-quantum-synthesis)

- `paper:post-quantum-synthesis` —REFERENCES→ `paper:pqs-ai-evaluation-audit`
- `paper:hydrodynamic-stability-hypothesis` —RELATES_TO→ `paper:post-quantum-synthesis`

## Data-quality findings

1. **[D1-DOI-GAP]** `non-archimedean-syntactic-paradigm-for-physics` row in `papers` has `doi: null` although OpenAlex registers 10.5281/zenodo.19600685/86 (two versions, 2026-04-16). Cross-system inconsistency — flag for backfill (P5.OWNERSHIP-compliant, verify creator first).
2. **[SEED-NOTE-URL-GAP]** Seed note cites PhilPapers QUNTCI/QUNANS/QUNTUP + SSRN 5809662/5821702. OpenAlex confirms QUNANS's underlying paper (Non-Archimedean Syntactic Paradigm, Zenodo) and the corpus confirms QUNTCI's subject (Hydrodynamic Stability Hypothesis = Zenodo 21993494). Direct URL resolution blocked by bot-filter (403/CF) on both hosts — see external-search evidence files. CDX: **zero Wayback captures** for any of the five seed URLs (philpapers.org/rec/QUNTCI, QUNANS, QUNTUP; papers.ssrn.com 5809662, 5821702) — they exist in the live web but are unarchived.
3. **[DOI-STALENESS]** HSH deposited .md body self-reports DOI 10.5281/zenodo.17721008 (v1.0, 2025-11-26) while the record DOI is 10.5281/zenodo.21993494 — consistent with NEWVERSION-FRONTMATTER-CARRYOVER-1 class; the corpus copy is the later deposit. Not adjudicated further (out of scope; flag for P5.FRESH audit of that record).
4. **[SSRN-UNVERIFIED]** SSRN abstract IDs in the seed note could NOT be verified live (CF bot-wall on papers.ssrn.com, both Python and browser). They are consistent with the Zenodo corpus (same titles/claims) but remain `[UNVERIFIED]` as URL-level citations. Adjudication does not depend on them (corpus DOIs are the authoritative anchors).

## Conclusion

All adjudication-critical records resolve to stable corpus DOIs with published status. Zero ID mismatches that would invalidate a grade; two gaps logged for remediation (D1-DOI-GAP, DOI-staleness).
