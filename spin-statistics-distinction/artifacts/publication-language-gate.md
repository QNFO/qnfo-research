# Publication Language Gate — QNFO.RES.009 (P5 pre-publication)

**Date:** 2026-08-14 · **Status:** PASS (0 violations)

## Scan results (scripted, state-machine pipe check v2)

| Check | Result | Detail |
|---|---|---|
| Mojibake (U+FFFD/U+FFFF) | PASS | 0 |
| Unicode math glyphs in source | PASS | 0 |
| `$` balance | PASS | 150 total (even); no unbalanced lines |
| Bare `\|` inside math | PASS | 4 real violations found + fixed: `(-1)^{|a||b|}` -> `(-1)^{\lvert a \rvert \lvert b \rvert}` (L71). Initial scanner v1 reported 10 false positives from table-cell separators between math spans; v2 state-machine distinguishes `$a\|b$` (violation) from `$a$ \| $b$` (legitimate cell separator). |
| INTERNAL-REF-1 (WBS codes, repo paths, skill refs, artifacts paths) | PASS | 0 matches |
| Banned weak-claim words (merely/obviously/of course/trivially/clearly) | PASS | 0 |
| Existential-claim patterns (KIF-62) | PASS | 0 unverified existential claims |
| MAP-TERRITORY-1 (strong claims near falsifiability condition) | PASS | F1/F2 within 4000 chars of every strong claim |
| TITLE-DUPLICATION-1 | PASS | YAML title not duplicated in body; 11 section H1s only |
| FILE-SLUG-1 | PASS | `spin-statistics-distinction.md` (slug-named) |

## KIF-60 labels used in the draft

[ESTABLISHED] — invariant relation, anyon generalization, ribbon identity (external-verified).
[textual finding] — monograph silent symmetric algebra (verifiable against monograph Appendix A).
[NOT YET EVIDENCE] — derivation program (pre-registered, unexecuted).
[RETRODICTION — not evidence] — invariant formulation (no predictive credit claimed).
[CONTESTED] — minimal-postulate sufficiency.

## Iteration record

- v1 scan: 10 violations (all false positives — regex spanning cell separators).
- Scanner hardened to per-line `$`-toggle state machine (v2).
- v2 scan: 4 REAL violations (bare `|` in `(-1)^{|a||b|}`) -> fixed with `\lvert\rvert`.
- v3 scan: PASS, 0 violations.

Evidence: script `lang_gate_009.py` logic documented in this file; scan rerunnable.
