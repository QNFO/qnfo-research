# P2 — Consilience Map & RQ5 Load-Bearing Keyword Analysis

- **Project:** QNFO.RES.022 (keyword-taxonomy-consilience)
- **Phase:** P2 — consilience map + RQ5 keyword analysis (computationally verified)
- **Date:** 2026-08-23
- **Verification:** `artifacts/verification/rq5_keyword_load.py` → `rq5_run.log`
  (EXIT=0) → `rq5_results.json`; machine-readable graph
  `artifacts/p2-consilience-map.json` (schema consilience-map-v2; 342 nodes =
  7 programs + 335 keywords; 335 OWNS edges).
- **Source:** `docs/QNFO-KEYWORD-TAXONOMY.md` v1.0 (2026-08-05), fetched
  byte-identical (12,684 B) from `res/artifact/keyword-taxonomy` into
  `artifacts/verification/keyword-taxonomy-source.md`.

## 1. The computational result (RQ5, honest verdict)

Research question RQ5 asked: *which keywords are load-bearing for the
consilience (shared by ≥3 programs), and does the load-bearing core coincide
with the ultrametric bridge vocabulary?*

**The data answer is NO — the taxonomy has no shared-keyword core.**
The verification script (deterministic, pure stdlib, Fisher exact test)
reports:

| Layer | Result |
|:------|:-------|
| L1 string level | 335 distinct keywords; **334 program-local (99.7%)**; exactly **1 keyword shared by 2 programs** (`complexity-measure`, INM∩RES); **0 keywords shared by ≥3**; bridge-vocabulary enrichment: precision 0.000, recall 0.000, Fisher p = 1.000 → **NOT SUPPORTED** |
| L2 family level | bridge families as sets: `valuation` → UMP only (21 kws); `hierarchy` → **SLB·RES·DEM** (8 kws); `distinction` → SLB only (14 kws); `bound` → INM only (10 kws) → **PARTIAL** (only the hierarchy family spans ≥3 programs) |
| L3 bridge subsections | the taxonomy's own bridge sections (UMP Bridge Concepts, RES Cross-Domain Methodology/Bridges/Measurement Stratigraphy) are program-local anchors — 29 keywords total, all resolving to their home program only |
| L4 cross-cutting themes | the taxonomy's explicit cross-cutting sections are the real cross-program mechanism: Agentic AI (5 keywords also in PLT: MCP family), 4-D Distribution (5 also in PLT: Zenodo/IPFS), Measurement Stratigraphy (4 also in RES) |

**Verdict:** RQ5 as originally phrased is **disconfirmed at the string
level**. The keyword taxonomy is strictly partitional by construction — it was
built as a GitHub-search scoping tool, with each program assigned its own
vocabulary. The consilience the paper claims is NOT a lexical fact of the
taxonomy; it is carried by (a) the bridge *families* as semantic sets (of
which only `hierarchy` genuinely spans programs), (b) the taxonomy's explicit
cross-cutting sections, and (c) the corpus-level semantic bridges found in
Phase 1 (measurement-stratigraphy, consilience-framework,
valuation-independent-foundations, consilience-physics-numtheory...).

## 2. What this means for the paper

1. **The claim must be restated at the semantic level.** The consilience is
   a claim about concepts and corpus structure, not about keyword strings.
   The paper will state plainly that the taxonomy contains no shared-keyword
   core (99.7% program-local), and that the consilience evidence lives in
   (i) the bridge-family correspondences, (ii) the corpus semantic bridges,
   (iii) the cross-cutting themes.
2. **UIA Q15 convergence (plural radices).** The only literal cross-program
   keyword in the whole taxonomy is `complexity-measure` (INM∩RES). The
   single-radix reading is NOT lexically visible; the `hierarchy` family is
   the only bridge family spanning ≥3 programs — consistent with UIA Q6/Q15:
   the invariant is hierarchical partition logic, and the specific
   arithmetic (p-adic/adelic) is one realization localized in UMP.
3. **CFE gap persists.** CFE (48 keywords) contains no bridge-family
   vocabulary at all (bridge_share 0.000) and shares no keywords with any
   other program. The paper's consilience table must either build the CFE
   bridge explicitly (learning-curve/forecast keywords → hierarchy over
   paradigms) or mark CFE as the weakest documented link (Phase-1 gap G6).
4. **RQ5 re-scoped.** The revised RQ5 for the paper: *"Is the load-bearing
   structure of the QNFO program portfolio carried by bridge-family
   correspondences and corpus-level semantic links rather than by shared
   keyword vocabulary?"* — answerable by this analysis + Phase-1 corpus
   findings, both computationally evidenced.

## 3. The consilience map (machine-readable)

`artifacts/p2-consilience-map.json` (consilience-map-v2):
- **Nodes:** 7 Program nodes + 335 Keyword nodes (with `programs`,
  `load_bearing`, `bridge_family` attributes).
- **Edges:** 335 OWNS edges program → keyword.
- **Bridge families present in the graph:** valuation (21 kws, UMP),
  hierarchy (8 kws, SLB/RES/DEM), distinction (14 kws, SLB), bound (10 kws,
  INM).

The map is the P2 deliverable for Deliverable 3 (map) of the PROJECT-PLAN:
a machine-readable program × keyword × bridge index of the portfolio
vocabulary, ready for KG ingestion at P6/P7.

## 4. Verification notes

- Script: `artifacts/verification/rq5_keyword_load.py` — deterministic
  (no randomness), pure Python stdlib, assertion-guarded parsing
  (7/7 programs, per-program keyword counts ≥ 10).
- Run log: `artifacts/verification/rq5_run.log` (EXIT=0, three debug-fix
  iterations: phantom-key default-dict bug caught by graph KeyError; L2
  program-coverage condition corrected from "any family keyword exists
  anywhere" to "program contains a family keyword"; exact counts 335).
- Reproducibility: `python rq5_keyword_load.py` from repo root regenerates
  both JSON artifacts byte-deterministically.
- The two L1/L2 bugs found during verification were real logic errors in
  the check itself (VERIFY-FIX-RERUN-1): the corrected script is the
  deposited evidence, not the buggy intermediate.
