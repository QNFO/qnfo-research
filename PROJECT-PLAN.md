# PROJECT-PLAN — QNFO.RES.022

| Field | Value |
|:------|:------|
| WBS code | QNFO.RES.022 |
| Program | QNFO.RES — QNFO Research (Cross-Domain Consilience) |
| Title | The Consilience of the QNFO Keyword Taxonomy: Ultrametric Structure as a Testable Compression Prior |
| Slug | keyword-taxonomy-consilience |
| Repo / branch | QNFO/qnfo-research — res/paper/keyword-taxonomy-consilience |
| Phase | P0 (this plan) |
| Created | 2026-08-23 |
| Seed note | vault `_26235182116.md` (2026-08-23): synthesis + red-team critique + 15-question deep inquiry |
| Taxonomy source | `docs/QNFO-KEYWORD-TAXONOMY.md` (branch res/artifact/keyword-taxonomy, v1.0, 2026-08-05) |
| Predecessors | QNFO.CON.001 (WBS.6 Consilient Synthesis, 10.5281/zenodo.21547793), QNFO.CON.002 (Consilience Framework, 10.5281/zenodo.21804073) |

## Purpose

This project converts the QNFO program keyword taxonomy — seven program vocabularies
(UMP, SLB, INM, CFE, RES, PLT, DEM) totaling roughly 300 keywords — into a single
consilient thesis with an explicit premise chain and a set of falsifiable research
questions, then executes the due-diligence and gap analysis that a publication
requires.

## Core Claim (P6 — locked)

The seven QNFO program keyword taxonomies are not seven research agendas but seven
vocabularies for one structural object: a nested, hierarchical partition logic whose
local geometry is the p-adic/Bruhat-Tits tree, whose global synthesis is the adelic
product formula, and whose minimal act is Spencer-Brown's distinction. The program's
scientific content, however, is carried not by that identification but by three
testable hypotheses:

- **H1 (compression prior).** Ultrametric (non-Archimedean) structure functions as an
  effective compression and clustering prior for measurement data across physics,
  biology, and computation: on concrete retrieval and classification tasks over
  high-dimensional sparse data, ultrametric embeddings match or beat Euclidean/cosine
  baselines on at least two independent corpora.
- **H2 (Archimedean emergence).** Continuous Archimedean physics appears as the
  thermodynamic or ergodic average over the leaves of an underlying ultrametric
  hierarchy, in the same sense that smooth hydrodynamics is the average of discrete
  molecular dynamics.
- **H3 (non-Archimedean signature).** Non-Archimedean signatures are detectable in
  quantum-coherent systems: decoherence under structured noise scales as a p-adic
  (power-of-prime) hierarchy rather than as standard Markovian/Gaussian noise.

The claim deliberately does NOT assert that reality is ultrametric. It asserts that
ultrametric structure is a testable compression prior whose empirical superiority or
failure decides the program's scientific standing.

### Disconfirmation criteria

- H1 is disconfirmed if ultrametric embeddings fail to match cosine/Euclidean
  baselines on two independent corpora with pre-registered metrics.
- H2 is disconfirmed if no derivation shows an Archimedean limit theorem from an
  ultrametric base with the required averaging interpretation.
- H3 is disconfirmed if structured-noise decoherence measurements show no deviation
  from Markovian noise models at the precision of the proposed test.
- The strong form of the program (a physics-relevant non-Archimedean substrate) is
  falsified by 2028 if neither H1 nor H3 yields a positive result.

## Why a reader should care

- **For researchers:** the paper turns a diffuse program narrative into a small set
  of checkable claims with explicit disconfirmation criteria, and documents which
  claims are derived and which are imported premises.
- **For practitioners (engineers, retrieval/ML people):** it specifies a concrete
  artifact — a p-adic fingerprint index for content-addressed corpora — that can be
  benchmarked head-to-head against vector search (HNSW/cosine) today, without any
  commitment to the underlying physics.
- **For quantum-hardware engineers:** H3 names a concrete, falsifiable noise model
  (hierarchical/p-adic decoherence scaling) that is directly testable on
  trapped-ion and superconducting platforms.
- **For external readers navigating the corpus:** the consilience map is a genuine
  index into ~1,600 QNFO papers, organized by the structural invariant they share
  rather than by program labels.

## Premise-depth disclosure

Where the premises end (deepest to shallowest):

- **L0 — unanalyzable primitives (imported, not derived):** the act of distinction
  (Spencer-Brown's mark); the notion of observation/measurement; the rational
  numbers Q as a field. The paper derives nothing below this layer.
- **L1 — imported theorem:** Ostrowski's classification (every nontrivial absolute
  value on Q is Archimedean or p-adic). Proven elsewhere; used, not re-proven.
- **L2 — structural bridge (named input, partially supported by prior QNFO work):**
  the identification of measurement hierarchies with ultrametric valuation
  structure. Prior QNFO records support this as a correspondence (e.g., the
  p-adic QEC classification in QNFO.UF), but it is a modeling choice, not a theorem.
- **L3–L5 — hypotheses H1, H2, H3:** empirical claims whose status is decided by
  the disconfirmation criteria above.

The paper's depth is therefore bounded: the "logical origin" story stops at L0; the
bridge at L2 is a named input; everything deeper is testable hypothesis. The
thesis is as deep as L2, and L2 is a premise, not a result.

## Research questions (hardened, falsifiable)

Each question below states a measurable observable and a pre-registered comparison.

1. **RQ1 (H1).** Given a corpus of high-dimensional sparse documents (scientific
   abstracts), does retrieval precision-at-k under an ultrametric (p-adic hash
   prefix) index match or beat a cosine/HNSW baseline at equal build cost?
   *Observable:* precision-at-k and latency on two corpora.
2. **RQ2 (H1).** Do cross-domain consilience links (papers in different programs
   that solve the same research problem) share p-adic prefixes (valuation depth)
   more often than they share cosine similarity above threshold?
3. **RQ3 (H2).** Can an Archimedean (Euclidean/Lorentzian) geometry be derived as
   the thermodynamic average of an ultrametric base model, with the averaging
   explicitly specified (ergodic mean over leaves / renormalization limit)?
4. **RQ4 (H3).** For a qubit coupled to structured hierarchical noise, does the
   measured decoherence time scale as a power-of-prime hierarchy (p-adic pattern)
   versus the standard 1/n^2 Markovian prediction, at a specified significance?
5. **RQ5 (structure).** Which keywords in the taxonomy are load-bearing for the
   consilience (shared by >=3 programs) versus program-local, and does the
   load-bearing core coincide with the ultrametric bridge vocabulary (valuation,
   hierarchy, distinction, bound)?

## Practitioner relevance

- **Deliverable 1 (software):** a p-adic fingerprint index (`p-adic distance`
  endpoint over SHA-256 hashes modulo p^k) benchmarked against HNSW/cosine
  retrieval on two public corpora. This is usable today as a retrieval tool
  independent of any physics interpretation.
- **Deliverable 2 (hardware test specification):** a concrete measurement protocol
  for RQ4 (structured-noise decoherence on trapped-ion or superconducting qubits),
  written in engineering terms (noise model, pulse sequence, expected scaling,
  significance threshold).
- **Deliverable 3 (map):** the consilience map as a machine-readable graph
  (program × keyword × bridge) that indexes the published corpus for external
  readers.

## Computational verification plan (COMPUTATIONAL-VERIFICATION-1)

- RQ1/RQ2: benchmark scripts with fixed seeds and pinned corpora; every number in
  the paper reproduced by `artifacts/verification/` scripts deposited with the paper.
- RQ3: numeric check of the averaging limit on a toy ultrametric model (exact
  state-vector or Monte Carlo), with golden values committed before prose.
- RQ4: analytic scaling check in code (symbolic/numeric) plus a seeded simulation
  of the noise model.
- All claims a computer can check are checked in code before assertion
  (VERIFY-IN-CODE-1); reproducibility statement (runtime, seed, versions) included
  at publication.

## Publication-language constraints (binding)

- Plain scholarly prose for external readers; no internal gate names, WBS codes as
  section headers, register/ledger branding, or meta-commentary about publication
  acts (PUBLICATION-PROSE-GATE-1, PUBLICATION-BRAND-LANGUAGE-1,
  PUBLICATION-META-PROSE-1, PAPERS-NO-NAVEL-GAZING-1).
- Internal pipeline status (phases, audits, corpus bookkeeping) stays out of the
  paper; the paper speaks to an external reader.

## Phase plan

- P0 (this plan): WBS allocation, branch, core-claim lock. **Done when committed.**
- P1: full-corpus due diligence (>=3 query formulations per topic, cross-system ID
  validation, adjacent-domain sweep, external verification) + gap analysis.
- P2: consilience map + load-bearing keyword analysis (RQ5) with computational
  verification.
- P3: draft paper (plain prose, external-reader framing).
- P4: computational verification suite for RQ1-RQ4.
- P5: red-team review + remediation.
- P6: Zenodo deposit (all source files; pre-publish gates).
- P7: dissemination (registry, KG, R2 mirror, D1 living-paper, Vectorize index).
- P8: publication + post-publication adversarial audit.
