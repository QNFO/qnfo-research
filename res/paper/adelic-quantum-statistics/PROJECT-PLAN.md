# PROJECT-PLAN — QNFO.RES.027

- **Title (working):** Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi–Dirac/Bose–Einstein Distinction
- **WBS:** QNFO.RES.027 (project, parent QNFO.RES, order 27)
- **Slug:** adelic-quantum-statistics
- **Repo/Branch:** QNFO/qnfo-research @ res/paper/adelic-quantum-statistics
- **Phase:** P0 (this plan) — roadmap P1 → P8 below
- **Registry:** portfolio-state.program_registry row inserted 2026-08-27 (phase P0, current_version v0.1-phase0)

## Core claim (LOCKED at P6 — 2026-08-27)

The two quantum statistics are the maximum-entropy occupation distributions of the finite-distinction reservoir (QNFO.RES.021) when the reservoir's multiplicities are constrained by the adelic product formula:

- **T1 (statistics):** restricting the integer reservoir to squarefree elements yields the Fermi–Dirac occupation distribution, and the unrestricted reservoir yields Bose–Einstein.
- **T2 (rate):** the per-distinction transition rate γ = 1/N — assumed in the prior papers of this sequence — follows from the N-fold degeneracy of a bath of indistinguishable alternatives cancelling the individual transition rates.
- **T3 (symplectic):** the symplectic (complex) structure J² = −1 of the large-N unitary limit (QNFO.RES.021) is selected in the Fermi case, where exclusion forces the skew-symmetric reversible generator, and is absent (symmetric/diffusive) in the Bose case.

## Falsifiers (locked with the claim)

- **F1 (stats):** `artifacts/verification/verify_stats.py` compares the occupation numbers obtained from the squarefree and unrestricted partition generating functions against the golden values 1/(e^x + 1) and 1/(e^x − 1) at sampled points x; any mismatch kills T1.
- **F2 (rate):** `artifacts/verification/verify_rate_gamma.py` runs a seeded Monte Carlo master equation over N degenerate bath alternatives; if the per-distinction rate does not scale as 1/N, T2 is dead.
- **F3 (symplectic):** `artifacts/verification/verify_symplectic.py` builds the Fisher metric g and the reversible generator L per the large-N construction and checks J² = −1 in the Fermi limit only; equal-strength skew emergence in the Bose case kills T3.
- **F4 (prior art):** the Phase 1 sweep (QNFO corpus + external literature) must precede any novelty assertion. If the squarefree/unrestricted identification already exists in print (primon-gas/Riemann-gas literature), the novel delta is scoped to exactly (product-formula normalization of the statistics + the γ = 1/N derivation + the Fermi-symplectic link) and never claimed de novo.

## SO-WHAT

This paper completes a four-paper arc with a single audit invariant. Paper 1 prices what correction costs (the Landauer floor, QNFO.JPC.003); Paper 2 shows how to compute exactly across places (finite-adele encoding, QNFO.RES.024); Paper 3 shows which number systems are complete (QNFO.RES.025); Paper 4 supplies the tier all three left assumed: why the two statistics exist at all, as the same product formula read against two lattice restrictions. An external reader gets (a) a derivation that closes the γ = 1/N gap the floor-pricing paper had to assume, and (b) a usable dichotomy: exclusion versus sharing as the two resource-allocation regimes of any finite-distinction system, with the product formula as the audit invariant.

## Premise depth

- **L0 (unanalyzable primitives):** the integers with unique prime factorization; the adelic product formula (imported theorem); the maximum-entropy principle (imported postulate).
- **L1 (derived):** the squarefree/unrestricted dichotomy and its occupation consequences; the degeneracy cancellation behind γ = 1/N; the large-N limit calculus (imported from QNFO.RES.021).
- **L2 (named imported inputs):** finite-distinction quantum mechanics (QNFO.RES.021, 10.5281/zenodo.22046458); the Landauer floor of QEC (QNFO.JPC.003, 10.5281/zenodo.22117282); finite-adele encoding (QNFO.RES.024, 10.5281/zenodo.22114495); completeness senses (QNFO.RES.025, 10.5281/zenodo.22109455); the composite-statistics rule (even/odd fermion parity → composite boson/fermion), imported from standard quantum mechanics per Obsidian `_26239072830.md`.
- **Where premises end:** the mapping hypothesis — quantum statistics ARE the maximum-entropy occupations of this reservoir — is a named input, not a theorem. It is tested by reproduction (F1–F3) and earns predictive status only through a novel falsifiable consequence, stated as an open problem: other lattice restrictions (partial exclusions) should yield parastatistical/anyonic intermediates, testable in the same framework. Dimensionality enters here, not in the core claim: in d = 2 the exchange group relaxes to the braid group (anyons), and the two-dimensional Bose gas condenses only quasi-long-range (BKT) — the 2D content of `_26239072830.md` feeds the intermediate-statistics open problem, where partial lattice exclusions are the proposed arithmetic analog of anyonic exchange phases.

## Practitioner relevance

A practitioner gets: (1) a regime classifier — given a reservoir's multiplicity structure (exclusive versus unrestricted occupation), the statistics and hence the per-distinction cost follow; this turns JPC.003's assumed rate into a derived quantity; (2) an implementable audit — the product-formula checksum, already demonstrated for exact rational arithmetic in QNFO.RES.024, extends to occupation-count verification in classical simulators of quantum statistics; (3) a design principle — distinct-part versus unrestricted-part partitions map to exclusive versus shared resource allocation in classical stochastic systems.

## Crosswalk / translations (CROSSWALK-TRANSLATION-1)

| This paper | Number theory | Quantum statistics | Stochastic thermodynamics | Information theory | QEC engineering |
|---|---|---|---|---|---|
| product formula | ∏_v \|x\|_v = 1 | normalization of occupations | global audit invariant | normalization constraint | checksum on readout/decoder arithmetic |
| squarefree restriction | distinct-part partitions | Fermi–Dirac (occupation 0/1) | exclusion regime | one-bit occupation per state | physical-qubit exclusivity |
| unrestricted lattice | unrestricted partitions | Bose–Einstein | sharing regime | unbounded occupation | mode sharing (cat/oscillator) |
| γ = 1/N | degeneracy factor | per-state rate | bath degeneracy cancellation | uniform prior over alternatives | per-round syndrome rate |
| composite statistics | even/odd fermion count | Möbius parity μ(n) | exchange sign ±1 | constituent-count rule | Cooper pairs, excitons, He-4/He-3 |

## Hypothesis cards (HYPOTHESIS-CARD-1)

- **H-STAT-FERMI:** squarefree multiplicity ⇒ occupation ⟨n⟩ = 1/(e^x + 1) at golden points. Falsifier F1a.
- **H-STAT-BOSE:** unrestricted multiplicity ⇒ occupation ⟨n⟩ = 1/(e^x − 1). Falsifier F1b.
- **H-RATE-GAMMA:** per-distinction rate ∝ 1/N under N-fold bath degeneracy. Falsifier F2.
- **H-SYMPLECTIC-FERMI:** J² = −1 emerges in the Fermi large-N limit only. Falsifier F3.
- **H-COMPOSITE-PARITY (from Obsidian `_26239072830.md`, 2026-08-27):** the composite-statistics rule — an even number of fermionic constituents gives a composite boson (+1 exchange sign), an odd number a composite fermion (−1) — is exactly the Möbius parity of the squarefree lattice: μ(n) = (−1)^(#prime factors). Prediction: every known composite matches μ-parity (Cooper pair +1 even ✓, exciton +1 even ✓, helium-4 +1 ✓, helium-3 −1 odd ✓, single electron −1 odd ✓); the exchange sign is Möbius parity of the constituent count, and the squarefree restriction (no repeated prime factor) is the exclusion signature itself. Falsifier F-HCP: any known composite whose exchange sign contradicts μ-parity, or the parity link shown to be an assertion rather than a structural consequence (the Q9 derivation-or-dictionary guard).
- **H-PRIOR-ART-DELTA:** the exact delta (product-formula normalization + γ derivation + Fermi-symplectic link) is not already published. Falsifier F4.

## Computational verification plan (COMPUTATIONAL-VERIFICATION-1)

Scripts in `artifacts/verification/`, deposited with the paper, with a reproducibility statement (runtime, seeds, dependency versions):

1. `verify_stats.py` — exact symbolic/numeric check of the squarefree and unrestricted generating functions against the Fermi/Bose golden values (F1).
2. `verify_rate_gamma.py` — seeded Monte Carlo master equation for the N-degenerate bath (F2).
3. `verify_symplectic.py` — Fisher metric g + reversible generator L; J² = −1 check in the Fermi limit; symmetric-generator check in the Bose limit (F3).
4. Golden values, edge cases (N → 1, N → ∞, x → 0), and seeded Monte Carlo throughout; every number in the paper reproducible from these scripts.

## Phase roadmap

- **P0 (this plan):** registry row, branch, PROJECT-PLAN, core claim + falsifiers locked, commit/tag/push. ZENODO-INQUIRY-1 ignorance audit on the core claim before P1.
- **P1:** full-corpus due diligence (DUE-DILIGENCE-DEPTH-1), adjacent-domain scan (JPC/ADL/INM/UMP), external verification (Riemann-gas literature, Euler partition identities, arXiv/OpenAlex/Crossref).
- **P2:** hypothesis-card reconciliation against executed tests; outline + draft.
- **P3:** draft with crosswalk section, practitioner section, premise-depth disclosure.
- **P4:** computational verification runs (F1–F3) — all PASS before prose finalizes.
- **P5:** title/abstract bridges (TERMINOLOGY-SILO-LESSONS-1), plain scholarly prose (PUBLICATION-PROSE-GATE-1, PUBLICATION-BRAND-LANGUAGE-1, ANTI-TELEGRAPH-1), rendering gates.
- **P6:** core claim re-verified against published results; ERRATA if drift.
- **P7:** outreach/dissemination planning (CAMPAIGNS-OUTREACH-1).
- **P8:** Zenodo deposit (PUBLICATION-SOURCE-COMPLETENESS-1), R2 mirror, D1/KG distribution, publish lock (PUBLISH-LOCK-1).

## Phase 1 due-diligence targets (preview)

- **Corpus formulations (≥3):** "quantum statistics from the adelic product formula"; "squarefree integers Fermi-Dirac partition statistics"; "primon gas Riemann gas bosons fermions"; "finite-distinction reservoir maximum entropy occupations".
- **Corpus records to reconcile:** QNFO.RES.020 (self-referential scalar family), QNFO.RES.021, QNFO.RES.009 (Boson/Fermion distinction, P0 — sibling scope), QNFO.RES.010 (exchange phase), adelic-core-synthesis, consilience-physics-numtheory, ADL.001–003, adelic-cross-domain-program (archived v5.1).
- **External:** Riemann gas / primon gas (Julia 1990; Spector 1990; Bakas–Bowick 1991 and successors); Euler's distinct-part partition identity; standard adelic product formula texts; any post-2020 arXiv work on statistics from adelic constructions.
- **Adjacent WBS domains:** QNFO.JPC (thermodynamics of computation), QNFO.ADL (adelic physics), QNFO.INM (information physics), QNFO.UMP (ultrametric partition lattices).
