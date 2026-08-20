# Figure Plan for v0.5 (2026-08-19)

User directive (2026-08-19): research publications should include diagrams and graphics to
increase understanding and comprehension. Operationalized as a standing gate (see below); the
first figure set ships with RES.015 v0.5.

## Standing gate (FIGURES-COMPREHENSION-1, user directive 2026-08-19)

1. Every QNFO publication includes at least one explanatory figure where a figure aids
   comprehension. A text-only publication requires an explicit justification in the
   PROJECT-PLAN (e.g., "content is pure argument with no structural/spatial referent").
2. Figure format: handcrafted or programmatically generated SVG source committed to
   `figures/` — the pandoc→CDP pipeline inlines SVG natively, and SVG survives
   mojibake/unicode-math gates (no unicode-math glyphs inside figure text).
3. Figures carry an in-figure caption line ("Figure N. ...") so the SVG is self-contained.
4. Print-friendly light theme (white background, dark text) per the standing light-theme mandate.
5. Figure content obeys the same gates as prose: no internal references, no pipeline vocabulary,
   plain scholarly labels.

## v0.5 figure set

| Fig | File | Content | Status |
|---|---|---|---|
| 1 | `figures/fig1-spider-fusion.svg` | Spider fusion rewrite (two Z-spiders → one) illustrating "the satisfaction of diagrams" (§1) | **WIRED into paper body (2026-08-20, commit 5bf1e99)** |
| 2 | `figures/fig2-seam-diagram.svg` | The seam: 3+1D physics and 1D thermodynamics imported onto the 2D map plane | **WIRED into paper body (§6, commit 5bf1e99)** |
| 3 | `figures/fig3-qpl-cluster-map.svg` | Nine-paper QPL 2026 cluster positioned on the program map (UMP/SLB/INM/CFE/DEM/RES) with the four unoccupied seams | planned |
| 4 | `figures/fig4-bt-tree-synthesis.svg` | Bruhat-Tits tree with a path traversal labeled as gate synthesis (appendix, Clifford+R row) | planned |

S5 (figure wiring) CLOSED 2026-08-20: markdown image refs added at §1 (fusion) and §6 (seam);
html/pdf rebuilt (226,337 B, 11 pages). Note: the binary U+FFFF scan false-positived once on the
figure-bearing PDF (raw-bytes hit inside a compressed stream); the authoritative scans
(decompressed per-page content + extracted text) are CLEAN — kaizen candidate: for
figure-bearing builds the gate should report the semantic scans, or scan decompressed streams.

## Pipeline integration

- References in the .md body: `![Figure 1 caption](figures/fig1-spider-fusion.svg)` — pandoc
  inlines SVG into the standalone HTML; the CDP render then rasterizes it. No changes to
  build-pdf.py needed.
- Deposit: figure files upload as regular keys under `figures/` (subdirectory keys already
  proven on this backend: `docs/`, `artifacts/` keys upload fine).
- v0.4 ships text-only (the increment was the post-publication appendix; it was already
  mid-publish when the directive landed). v0.5 = figures + in-room answers (Coecke, Shaikh/Yeh,
  Mosca/Yard/Deaconu) + the D1 shell dedup pass.

## Kaizen queue

- research skill: add FIGURES-COMPREHENSION-1 to Phase 5 Pre-Publication Requirements in the
  next CMD SKILLS UPDATE cycle (mirrors the user directive; owner = research skill).
- No skill_manage unilateral install — per the standing skills-update protocol.
