# Project Plan — The Revolutionary Beginner's Guide to Quantum Computing (v1.3.3)

WBS: QNFO.RES (consilience/archive) — QWAV guide artifact
Slug: the-revolutionary-beginners-guide-to-quantum-computing-why-we-dont-have-quantum-computers-yet-and-what-the-geometric-alt
Concept DOI: 10.5281/zenodo.20391554 · v1.1 record: 10.5281/zenodo.20391555
Repository: https://github.com/QNFO/revolutionary-quantum-guide

## Core claim (locked)

Two-part thesis: (1) the standard active-QEC paradigm faces a Carnot-limited
thermodynamic wall (20,000× cooling gap between 4 K and 20 mK stages); (2) the
ultrametric tree code (Bruhat-Tits) offers classically validated thresholds up
to 75× higher than surface codes with passive fault tolerance at ~4 K, testable
via three falsifiable predictions (E1-E3) for under $300,000 (E1+E2).

Premise-depth disclosure: derived — Carnot arithmetic, threshold ratios,
code-distance combinatorics; named imported inputs — the BTQP threshold values
(50.0%/75.0%/17.30%, from 10.5281/zenodo.20109835, classically simulated only),
the validation results (10.5281/zenodo.20134944), the 24 W per logical qubit
estimate (10× uncertainty band); unanalyzable primitives — the claim that the
Archimedean-vs-ultrametric choice is a physical question at all.

## v1.3.3 scope (2026-08-21) — post-publication audit remediation

Red-team (3 reviewers) found 2 HARD in v1.3.2: (1) two BEL control characters
(U+0007) corrupted \approx in Ch. 3 + Ch. 8 (heredoc backslash-collapse →
MathJax 'Math input error' in the HTML/PDF); (2) Part VI summary said Seven open
problems while Ch. 20 has eight. Also fixed: stray '#' before the E3-design
paragraph, stale (v1.2) headers in references.bib/citation-audit.md/PROJECT-PLAN,
stale README provenance footer, program-count line. Gates extended:
check_rendering.py now scans C0 control chars and heading-without-space lines
(10 checks); a browser-side merror check verifies zero MathJax errors.

## v1.3.2 scope (2026-08-21) — README restoration

v1.3/v1.3.1 shipped the repository blueprint as README.md (git-restore clobber).
v1.3.2 restores the deposit manifest and adds structural upload guards for BOTH
LICENSE (byte-size + CC header) and README (How-to-Cite marker) — LICENSE-CLOBBER-1
extended to README-CLOBBER-1.

## v1.3.1 scope (2026-08-21) — deposit-file correction

v1.3 shipped the repository license (QNFO-ULA, 505 B) as LICENSE by an automation
error; v1.3.1 restores the CC BY 4.0 legal code (18,657 B) and the full
rendering-check log. Structural guard added: the publish flow now asserts the
deposit LICENSE byte-size before upload (LICENSE-CLOBBER-1).

## v1.3 scope (2026-08-21) — substantive update (user mandate)

User correction accepted: v1.2.x was largely cosmetic. v1.3 incorporates the research
published since the May 2026 release: joules-per-solution benchmark section (Ch. 9,
qudit JPCUB 21880104 with its unvalidated-framework caveat), E3 hardware design
(trapped-ion falsifiability register 22025544, five pre-registered observables),
falsification exemplar (prime-valuation correction 21979060), calibrated displacement
assessment as open problem 8 (21747228), thermodynamic-successor evidence (17955898),
consolidated thesis references (21991899/21992229/21991953), QCA verification template
(22012694). Rendering fixes: all currency symbols escaped (false MathJax pairs
eliminated — 0 odd-$ lines), duplicated body abstract/date removed (YAML is the
single source).

## v1.2.1 scope (2026-08-21) — post-publication audit corrections

Red-team (3 reviewers, 0 HARD / 8 SOFT+DESIGN): "Six open problems" summary
corrected to seven (QEC–Darwinism added); LHC ratio marked ~100 (95× exact);
Appendix A correction #5 completed; citation-audit count corrected; open problem 7
now carries the F_L > 0.874 bound. No quantitative claims changed (verification log
unchanged, 35 PASS).

## v1.2 scope (2026-08-20)

1. Content corrections (5), each verified by artifacts/verification/
   verify_guide_claims.py (35 PASS / 0 FAIL):
   - Landauer limit at 20 mK: 2×10^-23 J → 1.9×10^-25 J
   - d=11 linear extrapolation: 2.4% → 2.6% (+ linear-model label, Λ=2.14 note)
   - "100× warmer" → 200× (4 K vs 20 mK)
   - "one-twentieth the qubit budget" → roughly one-sixth (241 vs ~40 at d=11)
   - dilution-refrigerator helium: "130 tons" (LHC figure) → closed He-3/He-4
     mixture; LHC 40 MW → "tens of megawatts"
2. New Appendix A: program update (external-facing; new records 22025544,
   21964674, 21979060, 21991953, 21991899; E1-E3 status unchanged).
3. New Appendix B: computational verification statement + golden-value table.
4. Frontmatter reconciliation: version v1.2, date 2026-08-20, license
   cc-by-4.0 (matches record), status published.
5. Deposit completeness: manuscript + HTML + PDF + references.bib +
   citation-audit.md + README.md + PROJECT-PLAN.md + docs/ignorance-audit.md +
   artifacts/verification/* + LICENSE.
6. Distribution: R2 mirror (qnfo-releases/2026/08/<slug>/), D1 papers row
   repair (authors, body_md, version, r2 paths, status), KG node repair
   (distribution_status, record_url, r2_path), Vectorize re-index.

## Why a reader should care

The guide is the program's most widely accessible entry point: it teaches the
standard curriculum honestly and then argues, with tagged confidence and
falsifiable predictions, that the field's bottleneck is thermodynamic and that
a different geometry deserves a test. The v1.2 update keeps the record honest
(five verified corrections) and current (new evidence records), so that the
one document a newcomer reads first is also the one that tells the truth about
what has and has not been demonstrated.

## Practitioner relevance

Practitioners get: (a) a decision framework — PQC migration now, quantum
sensing now, platform diversity for cloud experiments; (b) the E1/E2/E3
experiment specifications with costs, timelines, and kill-conditions — a
ready-made test plan any funded lab could execute; (c) the trapped-ion
falsifiability register (10.5281/zenodo.22025544) as the instrumentation
path; (d) the verification script as a template for checking any quantum
roadmap's arithmetic.

## Gates checklist (pre-publish)

- [x] ZENODO-INQUIRY-1 ignorance audit (docs/ignorance-audit.md)
- [x] DUE-DILIGENCE-DEPTH-1 corpus sweep (3 formulations × 2 topics + enriched)
- [x] P3.AUTHOR-GATE-EVERY-ENTRY-1 (16 external + 16 program entries verified live)
- [x] COMPUTATIONAL-VERIFICATION-1 (35 PASS / 0 FAIL, script + log deposited)
- [x] PRACTITIONER-RELEVANCE-1 (Ch. 18 blueprint + Appendix A)
- [x] SO-WHAT-GATE / premise-depth (this document + manuscript prose)
- [x] PUBLICATION-PROSE-GATE-1 / PAPERS-NO-NAVEL-GAZING-1 (appendices written
      for external readers; no pipeline vocabulary in publication text)
- [x] TITLE-DUPLICATION-1 (body H1 removed; headings normalized)
- [x] PDF-SUPERSCRIPT-UNICODE-1 (byte scan 0 U+FFFD/FFFF at build)
