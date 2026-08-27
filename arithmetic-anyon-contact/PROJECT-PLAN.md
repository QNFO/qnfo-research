# WBS: QNFO.RES.028

# Project Plan — Arithmetic Anyons: The Bounded-Occupation Family, Gentile Statistics, and the Roots of Unity That Carry Braid Phases

## Charter

Quantum statistics in three dimensions admit exactly two exchange phases. The companion record *Quantum Statistics from the Adelic Product Formula* (QNFO.RES.027, 10.5281/zenodo.22123068) reads those two statistics as maximum-entropy occupations of one integer lattice under two multiplicity rules, and closes its program with an open correspondence: the bounded-occupation family ζ(s)/ζ((m+1)s) "interpolates from the fermionic case at m = 1 to the bosonic case as m → ∞ and provides the arithmetic object that intermediate (anyonic) statistics must contact." The paper explicitly leaves unproven whether any intermediate m reproduces any known anyonic observable.

This project adjudicates that correspondence. Two bodies of evidence make the adjudication non-trivial rather than speculative. First, the corpus already carries a roots-of-unity reading of anyonic phases: the p-adic anyon braiding records (quantum groups at roots of unity, 10.5281/zenodo.21208491) and the pattern-particle table, which names "the p-adic braid phases of abelian anyons" as an input on ramified branches (10.5281/zenodo.22024856). Second, the condensed-matter literature has already established the precise relation between exclusion-type occupation constraints and braid phases: Haldane fractional exclusion statistics coincides with braid statistics only in special regimes (incompressible Hall liquids with edge structure), and fails in general. The bounded-occupation family is the partition function of Gentile intermediate statistics (occupation capped at m per mode), a counting constraint with a real-valued generating function. A counting constraint changes how many states a mode can hold; a braid phase changes what happens when two particles are exchanged. Whether the first can carry the second is the question.

## Core Claim (locked at Phase 0)

**C1 (primary).** The bounded-occupation family ζ(s)/ζ((m+1)s) is the partition function of Gentile intermediate statistics with occupation cap m. As a carrier of braid-group exchange phases it fails: for no m does it reproduce the fractional exchange phase e^{iπ/m} of Laughlin-type anyons at filling ν = 1/m, the braid data of any known non-abelian model, or the Haldane-g thermodynamic signatures outside the regimes where Haldane exclusion statistics is already known to coincide with braid statistics. Occupation truncation is a counting constraint on a real generating function and cannot carry a phase; the RES.027 §6 "must contact" wording overstates the correspondence.

**C2 (secondary).** The arithmetic objects that do carry exchange phases are multiplicative characters evaluated at roots of unity: the quantum-group braid data of the p-adic anyon records and the root-of-unity phases on ramified branches named in the pattern-particle table. The character model reproduces the established abelian anyon exchange phase, and the m-family does not.

**H2 (hypothesis card, later phase).** The prime-gap density of states of the Riemann gas (mode energies ln p over primes) produces a specific-heat deviation from the smooth-density-of-states ideal gas — the minimal computable observable that separates the arithmetic origin of the two statistics from the standard statistical-mechanics derivation.

### Disconfirmation criteria

- **D1.** Exhibit an m-family statistic (occupation distribution, thermodynamic potential, or correlation) that matches a known anyonic exchange datum — Laughlin phase e^{iπ/m}, a Haldane-g observable with g = 1/(m+1), or a Fibonacci-model fusion/brading datum — that the character model does not reproduce. D1 disconfirms C1 and C2.
- **D2.** Exhibit a known abelian anyon phase (or its thermodynamic consequence) that the roots-of-unity character model fails to reproduce. D2 disconfirms C2 only.
- **D3.** Show that the prime-gap correction to the Riemann-gas specific heat is identically zero, or indistinguishable from a smooth density-of-states model at every temperature. D3 disconfirms H2.

All three disconfirmations are computable with the deposited scripts; the negative results (C1's failure being *confirmed*, i.e., the m-family failing as a phase carrier) are the expected and publishable outcome of the project's primary leg.

### Premise depth (where the premises end)

- **L0 — unanalyzable primitives:** the integers with unique factorization; the braid group and its standard representations; the maximum-entropy principle as a selection rule; the canonical ensemble.
- **L1 — named imported inputs:** the identity ζ(s)/ζ((m+1)s) = ∏_p (1 + p^{-s} + ... + p^{-ms}) (classical); Gentile intermediate statistics (Gentile 1940); Haldane fractional exclusion statistics and its g-form (Haldane 1991); the established HES–braid relation results (Chen–Ng 1994; Ye–Marchetti–Su–Yu 2015); the corpus roots-of-unity braiding records.
- **L2 — derived in-project:** the no-m phase-reproduction statement (C1, computational); the character-model reproduction of abelian phases (C2, computational); the prime-gap thermodynamic correction (H2, computational).
- The claims are as deep as L2. Nothing here derives the spin-statistics connection; that boundary, conceded in the configuration-space-topology record (QNFO.RES.011, 10.5281/zenodo.21962450), stands.

### Why a reader should care

A practitioner building an arithmetic encoding of anyonic phases — or auditing one — needs to know which arithmetic object corresponds to braiding. If occupation caps cannot carry phases, engineering an m-cap register does not engineer an anyon, and the correct design target is character-theoretic (roots of unity). This project supplies the adjudication table and the reusable verification scripts, and it closes the last open seam of the arithmetic-statistics chain (RES.020 → RES.021 → RES.027) with a falsifiable yes/no rather than an open correspondence.

## Phases (WBS-coded)

| Phase | Code | Deliverable | Gate |
|---|---|---|---|
| P0 | QNFO.RES.028.P0 | Branch, plan, core-claim lock, UIA, commit/tag/push | P1–P11 pre-flight |
| P1 | QNFO.RES.028.P1 | Due diligence: full-corpus sweep (4 domains: UMP/RES/SLB/INM), cross-system ID validation, external verification (Haldane/HES↔braid/Gentile/primon-gas literature), gap analysis | Due-diligence + consilience artifacts |
| P2 | QNFO.RES.028.P2 | Literature: 8 sources, dedup, Mandatory Symmetry Template | Citation set |
| P3 | QNFO.RES.028.P3 | Citations: verified BibTeX, author-gate every entry | P3.AUTHOR-GATE |
| P4 | QNFO.RES.028.P4 | Research: computational adjudication — m-family vs Laughlin/Haldane/Fibonacci (C1), character braid matrices at roots of unity (C2), prime-gap specific heat (H2); hypothesis-card reconciliation | COMPUTATIONAL-VERIFICATION-1; 100% reproducible tables |
| P5 | QNFO.RES.028.P5 | Publication: paper md/html/pdf, Zenodo deposit, publication gates | PUBLICATION-SOURCE-COMPLETENESS-1 |
| P6 | QNFO.RES.028.P6 | Deploy: D1 living-paper, R2 mirror, Vectorize, registry re-point | Distribution checks |
| P7 | QNFO.RES.028.P7 | Dissemination: post-publication adversarial audit, outreach | Audit report |
| P8 | QNFO.RES.028.P8 | Distribute: GitHub tag, R2 archive, KG distribution_status | Closeout |

## Milestones

1. **M1 (P0):** Branch + core claim locked, Phase 0 tagged and pushed.
2. **M2 (P4):** C1 verdict computed: m-family phase-reproduction table complete (expected: no m matches any braid datum).
3. **M3 (P4):** C2 verdict computed: character model reproduces the abelian phase e^{iπ/m}; H2 prime-gap correction quantified.
4. **M4 (P5):** Zenodo deposit published with verification suite (COMPUTATIONAL-VERIFICATION-1).
5. **M5 (P8):** Distributed (R2/D1/KG/Vectorize), audit clean.

## Deliverable Registry

- `arithmetic-anyon-contact.md` (+ .html/.pdf) — the paper.
- `references.bib`, `citation-audit.md`.
- `artifacts/verification/` — verify_m_anyon.py, verify_braid_characters.py, verify_prime_gap_thermo.py + outputs.
- `artifacts/universal-ignorance-audit.md`, `artifacts/due-diligence-p1.md`, `artifacts/consilience-gate.md`.
- `artifacts/external-search/` — API evidence files.
- Practitioner section: adjudication table + the rule "occupation-cap engineering ≠ braid-phase engineering; the carrier is character-theoretic."

## Risk Register

| Risk | Mitigation |
|---|---|
| C1 verdict is a null match in both directions (m-family fails, character model also fails a datum) | Reframe to the characterization question: which arithmetic objects carry which phases; negative results remain publishable per the falsifiability register |
| Haldane-g ↔ m-family mapping is regime-dependent and muddies C1 | Pin the g = 1/(m+1) correspondence regime precisely in P4; restrict claims to the regimes where HES is established (Chen–Ng; Ye et al.) |
| Prime-gap specific heat turns out unobservable (primon gas is not a 3D physical gas) | State H2 as internal to the Riemann-gas model; its value is as the minimal distinguishing observable, not a laboratory prediction |
| Roots-of-unity braid data in-corpus is stated as named input, not derived | C2 claims reproduction, not derivation; cite the record's own input status |

## Success Criteria

- **Minimum:** C1 adjudicated with a complete computational table; verification suite deposited; publication P5 complete.
- **Target:** C1 + C2 both computed; the character model demonstrably carries the abelian phase where the m-family cannot.
- **Stretch:** H2 quantified with a non-zero prime-gap specific-heat correction; a practitioner-facing design rule published.

## Repositories & Branch

- Repo: QNFO/qnfo-research
- Branch: res/paper/arithmetic-anyon-contact
- Slug: arithmetic-anyon-contact
