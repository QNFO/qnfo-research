# Post-Publication Red-Team Report — RES.023 PDF (v2.1, 2026-08-24)

- **Audited artifact:** the v2.1 PDF build (10.5281/zenodo.22073307,
  concept 22071420, branch res/paper/ultrametric-program @ adcaae2).
- **Primary input:** user directive 2026-08-24 — "NOT ACCEPTABLE. PDF
  CONTAINS VISIBLE FORMATTING HEADER. MATH EXPRESSIONS SHOW IN PLAIN TEXT,
  NOT RENDERED PROPERLY. AUDIT AND FIX STYLE/FORMATTING/PAGINATION ISSUES
  PERMANENTLY/PERSISTENTLY."
- **Protocol:** CMD RED TEAM — 3 reviewer slots dispatched (Math+Style /
  Completeness / Dependency). Slots were mid-read at finalization; per
  REDTEAM-QUEUE-STALL-PATIENCE-1 the direct parent-agent audit is the
  authoritative fallback and was executed with committed-build evidence.
  READ-ONLY (no artifact modified during the audit).

## Aggregate verdict — user charge CONFIRMED (2 HARD, both reproducible)

**HARD-1: MATH RENDERS AS PLAIN TEXT.**
Direct evidence from the committed tree:
- `ultrametric-program.html`: **0 references to MathJax/KaTeX/mathjax/katex**
  — the HTML carries no math engine, so nothing can typeset.
- `ultrametric-program.md` source math is **plain ASCII**, not LaTeX:
  `d(x, z) <= max(d(x, y), d(y, z))` (L119) · `Q_p` (L123, L273-274,
  L382-383) · `sigma^2/n` (L236) · `tau ~ 1/n` / `tau ~ 1/n^2` (L287) ·
  `1/n^2` (L316). No `$...$` delimiters exist, so even a MathJax-enabled
  build would not know these are math.
- Build chain: `pandoc --standalone` (no `--mathjax`/`--katex`/`--webtex`)
  → Playwright `page.pdf(format="A4", ...)`.
- **Impact:** a physics/math reader sees ASCII approximations, not
  typeset equations — unprofessional for a paper whose §3/§5.2/§6/§7 carry
  mathematical claims (ultrametric inequality, CLT golden value, slopes).

**HARD-2: VISIBLE FORMATTING HEADER.**
Direct evidence:
- Build options: `display_header_footer=True`,
  `header_template="<div></div>"`, footer_template with page numbers.
- Chromium quirk: an EMPTY header template does NOT reliably suppress the
  default header — Chromium renders the document title + URL at the top
  of every page unless the template contains a non-empty element (known
  print-to-PDF behavior). The user sees that default header band.
- Also present: pandoc's standalone title-block (`<header
  id="title-block-header">`) as page-1 content (acceptable alone, but the
  running header on every page is the defect).

**HARD-3 (permanence): NO COMMITTED BUILD PIPELINE.**
The PDF was produced by ad-hoc commands from a temp tree; the repo
contains `pdf-style.css` but **no committed build/verify script** (no
pandoc invocation, no Playwright options, no MediaBox/FFFD/math-render
gates). The user's "fix permanently/persistently" requires a committed,
re-runnable pipeline with built-in gates.

## SOFT findings

1. Pagination hazards present in CSS but unverified at build time:
   `page-break-inside: avoid` on tables/rows, orphans/widows — no
   automated check.
2. No math-render gate exists (no assertion that equations typeset).
3. No header-absence gate exists (no check that pages carry no
   title/URL band).
4. The v2.1 MediaBox/FFFD gates exist only as ad-hoc pypdf commands, not
   as a committed script.

## Verified OK (unchanged from v2.1 audit)

- A4 MediaBox 595.28×841.89 pt (12 pages) · 2 cm margins · 0 U+FFFD ·
  frontmatter DOI/version consistent · all 37 files present · content
  matches the source .md.

## Remediation plan (executed as v2.2 per the new-versions directive)

1. **Convert source math to LaTeX** `$...$` in `ultrametric-program.md`
   (ultrametric inequality, Q_p, sigma^2/n, tau ~ 1/n, tau ~ 1/n^2, etc.).
2. **Committed permanent pipeline** `scripts/build-pdf.py`:
   pandoc `--mathjax` (tex-svg) → Playwright with
   `display_header_footer=False` (no header/footer artifacts) → pdf →
   pypdf gates (MediaBox A4, FFFD, math-render sanity, no-header check).
3. Rebuild HTML + PDF; verify math renders as SVG; verify no header.
4. Publish **v2.2 newversion** (concept 22071420), re-point stores,
   commit the pipeline + pack, tag, push.
