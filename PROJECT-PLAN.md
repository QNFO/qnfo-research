# PROJECT-PLAN — QNFO.RES.023

| Field | Value |
|:------|:------|
| WBS code | QNFO.RES.023 |
| Program | QNFO.RES — QNFO Research (Cross-Domain Consilience) |
| Title | The Ultrametric Program: One Structural Object Across Seven Research Domains, and Its Falsifiable Tests |
| Slug | ultrametric-program |
| Repo / branch | QNFO/qnfo-research — res/paper/ultrametric-program |
| Phase | P0 (this plan) |
| Created | 2026-08-23 |
| Seed note | vault `_26235205331.md` (2026-08-23): the program thesis + H1/H2/H3 |
| Predecessor | QNFO.RES.022 (10.5281/zenodo.22071421) — keyword-taxonomy audit = the evidence base; this paper is the thesis statement the P8 audit found missing |
| User directive | 2026-08-23: "WHAT'S THE THESIS AND BROADER THEME? EXPAND THIS AND STOP BEING SO MYOPIC" (P8 post-publication red team) |

## Purpose

RES.022 audited the program's keyword taxonomy and found it strictly
partitional (334/335 keywords program-local). The P8 post-publication red
team (2026-08-23) confirmed the user's charge: the published record never
states the program's thesis as its own position, never names the mission,
and frames an internal instrument as the subject. THIS paper is the thesis
statement: the seven domains share one structural object, the hierarchy is
the invariant, and the program's scientific standing is decided by three
falsifiable hypotheses with a 2028 decision point. The RES.022 audit result
(consilience is semantic, not lexical) becomes evidence here, not the
headline.

## Core Claim (P6 — locked, verbatim from the seed note)

**Structural identification.** The program's domains share a structural
object — nested hierarchical partition logic — and that object is
empirically productive. The shared structure is a family of nested-partition
structures: the ultrametric inequality and its strict hierarchy of nested
balls. The specific arithmetic (p-adic valuation, adelic product formula) is
one realization; the hierarchy is the invariant.

**H1 — compression prior.** Ultrametric structure is an effective
compression and clustering prior for high-dimensional sparse measurement
data.

**H2 — Archimedean emergence.** Continuous Archimedean physics appears as
the thermodynamic or ergodic average over the leaves of an underlying
ultrametric hierarchy.

**H3 — non-Archimedean signature.** Quantum-coherent systems under
structured hierarchical noise exhibit decoherence scaling that deviates
from the standard Markovian prediction in a p-adic pattern (power-of-prime
hierarchy).

### Disconfirmation criteria

- H1 is disconfirmed if the ultrametric index does not match a cosine
  baseline on two pre-specified corpora with metrics, primes, and hashes
  committed before measurement. (Current state per RES.022: exact match on
  the synthetic corpus; −0.042 at p@10 on the title-only corpus; the
  abstract-and-embedding corpus is the adjudicator.)
- H2 is disconfirmed if no derivation exhibits the averaging operation —
  ergodic mean over leaves or renormalization limit — producing an
  Archimedean limit theory.
- H3 is disconfirmed if structured-noise decoherence measurements show no
  deviation from Markovian models at the precision of the stated protocol.
- **2028 decision point:** the strong form of the program (a physics-
  relevant non-Archimedean substrate) is falsified by 2028 if neither H1
  nor H3 yields a positive result.

## Why a reader should care (SO-WHAT)

1. **The thesis is the answer to "one program or seven?"** — stated plainly
   and testably, with the hierarchy as the invariant and the arithmetic as
   one realization. An external reader learns what the program claims, why
   it is not vacuous, and exactly what would falsify it.
2. **The program's mission connection:** the ultrametric program serves the
   energy-efficiency benchmark for quantum computing (JPCUB — "what does a
   correct quantum answer cost in energy?"). The bound family (Landauer,
   Bremermann, Margolus-Levitin) is the direct link between the hierarchy
   invariant and the mission.
3. **A testable physics program:** H2/H3 anchor in the Parisi RSB
   ultrametricity literature (measured in random lasers; cavity-QED spin
   glass as the nearest experiment) and confront the Newman-Stein
   finite-dimensional controversy.

## Premise-depth disclosure

- **L0 — unanalyzable primitives:** the act of distinction (the mark); the
  notion of observation/measurement; the rational numbers as a field.
- **L1 — imported theorem:** Ostrowski's classification (Archimedean or
  p-adic). Used, not re-proven.
- **L2 — structural bridge (named input):** measurement hierarchies
  identified with ultrametric valuation structure. A modeling choice
  supported by prior records (RES.022 corpus links), not a theorem.
- **L3–L5 — hypotheses H1, H2, H3:** empirical claims decided by the
  disconfirmation criteria.

The thesis is as deep as L2; L2 is a premise, not a result. The paper does
not assert that reality is ultrametric — it asserts a testable compression
prior and a falsifiable physics program.

## Practitioner relevance

- **Deliverable 1:** the data-derived ultrametric index (single-linkage
  recoding), benchmarked against cosine on two pinned corpora; the p-adic
  hash variant as encoding control. Usable as a retrieval tool independent
  of the physics.
- **Deliverable 2:** the structured-noise decoherence protocol (H3): noise
  model, pulse sequence, expected scaling (p-adic power-of-prime vs 1/n^2
  Markovian), significance threshold, trapped-ion/superconducting platform
  notes.
- **Deliverable 3:** the machine-readable consilience map (RES.022 graph:
  342 nodes, 336 edges) as the vocabulary index.
- **Mission deliverable:** JPCUB link — the bound family's role in the
  energy benchmark stated in engineering terms.

## Computational verification plan (COMPUTATIONAL-VERIFICATION-1)

- Reuse and extend the RES.022 suite (rq1–rq5, seed 20260823, deterministic,
  pure stdlib) — all artifacts are inherited as the evidence base.
- H2 numeric: ultrametric inequality violations = 0; CLT golden variance of
  leaf mean vs sigma^2/n within 5%; Gaussianity (already PASS in RES.022).
- H3 numeric: Markovian slope −2.0000 vs p-adic slope −0.9881, separation
  1.012, exact arithmetic 0.0 rel. err, MC sanity (already PASS).
- Every number in this paper reproduced by deposited scripts;
  reproducibility statement (runtime/seed/versions) included.

## Publication-language constraints (binding)

Plain scholarly prose for external readers (PUBLICATION-PROSE-GATE-1,
PUBLICATION-BRAND-LANGUAGE-1, PUBLICATION-META-PROSE-1,
PAPERS-NO-NAVEL-GAZING-1). No register/ledger branding; no internal pipeline
status in publication prose; the thesis leads, the audit is evidence.

## Phase plan

- P0 (this plan): WBS allocation, branch, core-claim lock.
- P1: full-corpus due diligence + gap analysis (thesis-focused sweep).
- P2: draft paper (thesis-led structure: thesis → mission → evidence →
  hypotheses → deliverables).
- P3: computational verification integration + reproducibility.
- P4: red-team review + remediation.
- P5: Zenodo deposit (TITLE-EXISTENCE-PRE-PUBLISH-1, PUBLISH-LOCK-1,
  PUBLICATION-SOURCE-COMPLETENESS-1).
- P6: dissemination (R2 mirror, D1, KG, Vectorize, registry re-point).
- P7: publication + post-publication adversarial audit.
