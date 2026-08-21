# Representation Lab — Interactive Demo Plan (DEM-E0-T01 spec)

**Project:** QNFO.RES.019 — Visual Graphs vs Matrices: Epistemic Limits, Cognitive Preference, and
the Design of Understandable Computation (Zenodo 10.5281/zenodo.22034455, v1.1)
**Pipeline:** qwav-demo-kit (DEM-E0-T01..T05) · **Status:** SPEC (2026-08-21)

## Purpose (why a reader/practitioner should care)

The paper's central claim is that diagrams win over matrices because of bounded cognition, not
mathematics — and that where comprehension and optimality diverge, the field builds a two-layer
structure. A reader of the PDF must take that on faith. The demo makes it *executable*: the same
map shown as matrix, circuit, and ZX diagram side by side; rewrites applied live with the
difference visible; and the representation-size gap (4^n entries vs 3n-2 tokens) rendered as an
interactive slider. This is the practitioner embodiment of the paper's thesis and its
computational verification.

## Interactive core (DEM-E0-T01)

1. **Three-pane equivalence view:** the same 2-qubit map (CNOT∘H — the paper's verification
   example) simultaneously as (a) 4×4 matrix, (b) quantum circuit, (c) ZX diagram (SVG-drawn
   spiders and wires). Selecting a pane highlights the same semantic element in all three
   (matrix entry ↔ gate ↔ spider).
2. **Live rewrite diffs:** an animated spider fusion (α, β → α+β) with the intermediate steps;
   a "diff" toggle that flashes exactly what changed between rewrite steps (the locality of
   rewriting made visible).
3. **Visibility table (the paper's quantitative claim):** an n-qubit slider (n = 2..6) showing
   matrix entries (16..4096) vs diagram tokens (4..16 per the paper's 3n-2 count), with the
   gap ratio displayed. Reproduces Table §7 of the paper exactly.
4. **Golden-value checks:** two live verifier badges that recompute in the browser:
   - Spider fusion: max |Z(α)⊗Z(β) − Z(α+β)| deviation (paper's verify-claims.py CHECK 1,
     golden dev ≈ 1e-16)
   - Formal equivalence: max |circuit − ZX-contraction| (CHECK 2, ≈ 1.1e-16)
   Badges show PASS with the computed deviation; a FAIL badge is impossible unless the demo's
   own math is broken (which is the point).

## Design constraints (user mandates, hard)

- **Light theme only** (user mandate 2026-08-06 — no dark themes).
- **Every control wired to real computation** — no dead buttons; every button changes state.
- Self-explanatory: a first-time visitor understands the three panes in <30 s without a manual.

## Verification architecture (DEM-E0-T02..T03)

- The demo's numeric core mirrors `artifacts/verification/verify-claims.py` (deposited with the
  paper): the same constructions (CNOT = (I⊗H)CZ(I⊗H), fusion identities), same golden values.
- Automated tests: CDP `test-demo.py` (loads the page, asserts badge PASS states and the slider
  table numbers for n = 2..6) + Playwright click-everything suite (every interactive control
  clicked; assertions after each).
- Reproducibility: the demo page footer states the paper DOI + verification file it mirrors.

## Deploy (DEM-E0-T04..T05)

- Native `gh-pages` branch deploy under the qwav-demos repository (demo dir
  `representation-lab`), served at the established demos URL pattern.
- Same-turn anti-phantom verification: after deploy, fetch the deployed page and assert the
  badge elements + slider values render (no relying on the deploy command's own echo).

## Build checklist (the T01 → T05 handoff)

- [ ] DEM-E0-T01: this spec + repo skeleton (qwav-demos/representation-lab)
- [ ] DEM-E0-T02: golden-value math module (port of verify-claims.py) + unit tests
- [ ] DEM-E0-T03: three-pane UI + live rewrites + visibility slider (light theme)
- [ ] DEM-E0-T04: CDP test-demo.py + Playwright click-everything suite — all green
- [ ] DEM-E0-T05: gh-pages deploy + fetched-page verification + docs

## Status

Spec committed 2026-08-21 (this file). Build phases T02–T05 queued; the next CMD CONTINUE with
headroom executes T02 (math module + unit tests) as the first build increment.
