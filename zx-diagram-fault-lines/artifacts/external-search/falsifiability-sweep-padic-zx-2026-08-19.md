# Falsifiability Sweep: p-adic / Ultrametric ZX + D1 Fix Record (2026-08-19)

QNFO.RES.015 P9 extension cycle, second pass (CMD CONTINUE). Purpose: (a) execute the queued
D1 `identifier` re-point; (b) test the core claim's falsifiability condition Q5(a) — "the claim
is false in a world where a p-adic ZX calculus already exists in the literature" — by sweeping
the arXiv record and the QNFO corpus for p-adic/ultrametric ZX treatments; (c) close the arXiv
identity gap for paper 179.

## 1. D1 fix executed (readback-verified)

- Convention check (siblings): `signal-worker-boundary-confinement` doi=21974194, identifier=21931224 (concept);
  `non-archimedean-projective-perspective` doi=21979032, identifier=21969603 (concept).
  Canonical convention: `doi` = latest published version record; `identifier` = concept DOI.
- UPDATE executed via D1 REST (MCP tool is read-scoped; 403 on writes — D1-REST-PAYLOAD-1 path):
  `UPDATE papers SET identifier='10.5281/zenodo.21991895' WHERE slug='zx-diagram-fault-lines' AND identifier='10.5281/zenodo.21991896'`
  (optimistic lock; changes=1 row).
- READBACK: identifier=10.5281/zenodo.21991895 (concept), doi=10.5281/zenodo.21992118 (v0.3), status=published. PASS.
- KG node `paper:zx-diagram-fault-lines` doi=10.5281/zenodo.21992118 — already correct (no KG change needed).
- Cross-store parity now: D1 doi/KG/frontmatter = 21992118; D1 identifier/Zenodo concept = 21991895. CLOSED.

## 2. External falsifiability check (arXiv, 2026-08-19)

- arXiv search `"p-adic" AND "ZX"` → **0 results**.
- arXiv search `"ultrametric" AND "quantum error correction"` → **0 results**.
- Verdict: **no p-adic or ultrametric ZX calculus exists in the arXiv record as of 2026-08-19.**
  Seam 1 (p-adic/ultrametric ZX) remains externally unoccupied; the core claim survives this check.
  The 90-day re-sweep remains the standing falsification instrument.

## 3. Paper 179 verified — CORRECTION to qpl2026-zx-cluster evidence

- The QPL submission (non-final, qpl2026-paper179.pdf) is the extended abstract of
  **arXiv:2607.04015v1**, "The Delayed Stabilizer ZX-Calculus" (Cole Comfort, Giovanni de Felice;
  published 2026-07-04; quant-ph, cs.LO, math.CT, math.SG).
- The earlier evidence file recorded "arXiv: none claimed" for 179 — CORRECTED here.
- Substantive update: the QPL abstract states the completeness of the calculus as a CONJECTURE
  (generalised local complementation rule); arXiv v1 establishes **soundness, universality, and
  completeness** (generalised Euler decomposition + colour change rules; unique normal form via
  generalised local complementation and pivoting). The completeness gap closed between submission
  and arXiv v1.
- Paper 187 (three-way normal form): still no public arXiv ID located (the submission states the
  technical manuscript is attached to the submission). Remains UNVERIFIED for arXiv identity
  (VERIFY-FACT-1 — no ID asserted).

## 4. Adjacent find (Comfort author search)

- **arXiv:2601.08389v1** — "A dataflow programming framework for linear optical distributed quantum
  computing" (de Felice, Poór, Comfort, Yeh, Kupper, Cashman, Coecke; 2026-01-13). ZX + dataflow +
  linear optics with repeat-until-success fusion protocols. Executable-graphical substrate directly
  relevant to the DEM/PLT demo line (dataflow-typed ZX = a runnable compilation target).

## 5. QNFO-internal corpus hits (p-adic QEC formulation, limit=20)

The p-adic-QEC formulation surfaces QNFO's own records — the seam is internal-first:
- `zbw-majorana-tqc-p5-adelic-qec` — "Adelic Quantum Error Correction: Intrinsic Qubit Protection
  from Ostrowski" (QNFO). QNFO already HAS an adelic QEC record; no diagrammatic treatment in it.
- `ultrametric-foundations` — "Number-Theoretic Ultrametric Foundations: A Unified p-adic Framework
  for Error-Correcting Code Classification" (QNFO).
- `prime-valuation-qec-implications` — "Implications for Computing and Quantum Error Correction" (QNFO).
- Also adjacent: p-adic-anyon-fusion-braiding, p-adic-braid-groups-bruhat-tits, qec-darwinism-ultrametric.

**Refined seam statement (replaces the coarser one in the advancement map §4.1):** QNFO possesses
p-adic/adelic QEC records but no graphical/diagrammatic p-adic treatment; externally no p-adic or
ultrametric ZX calculus exists (0/0 arXiv). The bridge machinery is 179's delay calculus (finite
generating tableaus for infinite translation-invariant stabiliser processes) plus 174's Bruhat-Tits
tree synthesis. The open construction: extend the delayed stabiliser calculus to stabiliser groups
over p-adic rings of the Z[chi^-1] type (the exact setting of 174), or dualize 174's tree traversal
to code-space geometry per qec-darwinism-ultrametric.

## 6. New data-quality flags (queued to the data-layer pass; not fixed this turn)

- `zbw-majorana-tqc-p5-adelic-qec`: `identifier` = the SLUG itself with `identifier_type` = "arxiv"
  (S-W quirk class, mem-424c70fd precedent); `doi` = 21336099 vs `zenodo_doi` = 21214583 — version
  drift to verify via DataCite before re-pointing.
- `ultrametric-foundations`: D1 shell — doi/identifier/r2_key all NULL, status published (D1-shell class).
