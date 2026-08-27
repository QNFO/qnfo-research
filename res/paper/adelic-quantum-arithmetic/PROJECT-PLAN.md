# PROJECT-PLAN — adelic-quantum-arithmetic (QNFO.RES.029)

WBS: QNFO.RES.029
Slug: adelic-quantum-arithmetic
Branch: res/paper/adelic-quantum-arithmetic
Repo: QNFO/qnfo-research
Phase: P0 (complete) — core claim locked 2026-08-27
Status: active

## Seed

Vault note _26239100148 (2026-08-27), "Adelic quantum arithmetic": a voice-level statement of the program's core thesis. This project renders that statement as a reader-facing synthesis with a practitioner crosswalk and a discipline ledger. It does not re-derive the published proofs; it maps, crosswalks, and disciplines.

## Positioning (anti-duplication)

- RES.027 (10.5281/zenodo.22123068) proves the statistics origin from the adelic product formula. This paper carries the proof; it does not redo it.
- RES.028 (arithmetic-anyon-contact, P8 published 2026-08-27) adjudicates the bounded-occupation/anyonic continuation. This paper points to it.
- RES.023 (10.5281/zenodo.22076816) carries the Ultrametric Program umbrella across seven domains. This paper is the arithmetic-flavored companion: one thesis, one dictionary, one ledger.
- The addition over all three: the practitioner-facing crosswalk "particles as prime factors" — an explicit term dictionary from arithmetic objects to statistical-mechanics and engineering quantities — plus the consolidated discipline ledger.

## Core claim (locked at P0; re-locked P6)

Standard quantum mechanics is the Archimedean readout of a larger arithmetic structure. Ostrowski's theorem classifies all completions of Q: the real completion plus one p-adic completion for every prime. Standard QM uses only the real completion — Hilbert space over C — because macroscopic measurement is Archimedean. The primes are the non-Archimedean places, which is why their structure is multiplicative (unique factorization), never additive. The multiplicative structure is the arithmetic origin of the particle-statistics binary: on one integer lattice, the unrestricted exponent rule gives the Riemann zeta function and Bose–Einstein occupation; the squarefree rule (each prime divides at most once) gives a ratio of two zeta values and Fermi–Dirac occupation. Both identifications are exact and computationally verified (RES.027; per-place identification RES.020). The register is structural throughout: isomorphisms of mathematical structure, no particle ontology.

## Hypothesis cards

- H1 [ESTABLISHED, carried] The two statistics are the maximum-entropy occupations of one lattice under two multiplicity rules. Proof: RES.027. This paper restates and crosswalks.
- H2 [This paper's claim] The "particle species ↔ prime factor" dictionary is load-bearing for practitioners: additive quantum numbers (energy, momentum) and multiplicative quantum numbers (species labels, idelic characters) separate cleanly under the dictionary. Disconfirmation: if connecting any practitioner-measurable quantity requires auxiliary assumptions beyond the published isomorphisms, the dictionary is a renaming and H2 fails; the paper then records that failure.
- H3 [CONJECTURE, labeled] The Adelic Representation Theorem. Zero formal proof. Carried only as a conjecture with its disconfirmation criteria; not used to derive anything here.

## Premise chain (where the premises end)

- L0 [ESTABLISHED MATH] The rationals Q, Ostrowski's classification of places, unique factorization. Taken as given.
- L1 [ESTABLISHED MATH] The adele ring and the product formula: the product of all absolute values over all places equals 1 for every nonzero rational.
- L2 [ESTABLISHED METHOD] Maximum-entropy occupation distributions on a lattice of modes.
- L3 [EXACT, VERIFIED] Bose–Einstein ↔ unrestricted exponents (Riemann zeta), Fermi–Dirac ↔ squarefree restriction (ratio of two zeta values). RES.027, computationally verified. Also RES.020: the p-adic maximum-entropy distribution is Bose–Einstein at fugacity 1/p.
- L4 [PROPOSED DICTIONARY] Attaching physical labels to the distributions — inverse temperature ln p at the p-adic place, species ↔ primes. THE PREMISES END HERE. The algebra is exact; the dictionary is proposed; the falsification conditions are written.
- Named imported inputs: the spin-statistics theorem (Pauli 1940) as the physical target; RES.020/RES.027 as the published base; the disconfirming findings as standing constraints.

## SO-WHAT (why a reader should care)

A reader gets, in one record: (1) a single readable map of a line of research otherwise scattered across records — "quantum as arithmetic"; (2) the exact published proofs with every premise marked, so the proved parts and the proposed parts are separable at a glance; (3) a crosswalk that lets a statistical-mechanics or quantum-engineering practitioner use the arithmetic objects without number-theory jargon; (4) the discipline ledger separating proved, conjectured, and disconfirmed — the layer that lets a skeptical reader grade the program without reading thirty records.

## Practitioner deliverables

- D1: The crosswalk dictionary (arithmetic ↔ physical/engineering terms), as a table in the paper.
- D2: The multiplicity-rule recipe: any system whose mode labels carry unique factorization admits zeta-function partition readings (unrestricted → zeta; squarefree → ratio of zeta values) — usable by statistical-mechanics practitioners directly.
- D3: The Bruhat–Tits qudit reading: the p-adic norm inequality is passive error protection; p-adic = noise-protected, Archimedean = readout. Engineering embodiment of the non-Archimedean structure.
- D4: The bounded-occupation family as the interpolation that engineered-statistics platforms must contact (ties to RES.028).

## Crosswalk (no-jargon dictionary)

| Arithmetic object | Physical / engineering reading |
|---|---|
| place / valuation | a way of measuring size |
| prime | an independent multiplicative quantum number / species label |
| squarefreeness | Pauli exclusion (occupation at most once) |
| unrestricted exponents | Bose aggregation (unbounded occupation) |
| product formula | the constraint linking all scales |
| adele ring | all measurement scales in one object |
| idele characters | conserved multiplicative quantum numbers |
| Möbius parity | bookkeeping of composite (intermediate) statistics |
| Bruhat–Tits tree | hierarchical (tree-structured) state space |
| p-adic norm inequality | passive error protection |

## Discipline ledger

- Register: isomorphisms of mathematical structure; no particle ontology.
- Adelic Representation Theorem: [CONJECTURE — UNPROVEN], zero formal proof; always labeled.
- Disconfirming findings that travel with the program: FMO coupling anti-ultrametric (cophenetic 0.426, p = 0.984); PW-WDW-Ultra spectrum hypothesis falsified; CMB shows no log-periodic oscillations above 0.3%; FMO exact clustering null (p = 0.598); D = 4 diagonal refinement insufficient without tree-structured clock spectrum.

## Verification plan (COMPUTATIONAL-VERIFICATION-1)

Every quantitative statement reproduced by deposited scripts: Euler-factor expansion of the zeta function and the squarefree ratio; Bose–Einstein and Fermi–Dirac occupation golden values from the canonical derivative; squarefree density 6/π²; bounded-occupation family evaluations; Möbius parity bookkeeping. Reproducibility statement (runtime, seed, versions) in the paper; scripts and outputs in artifacts/verification/ and included in the deposit.

## Publication checklist (gates at P5/P6)

check_rendering.py (odd-$, currency, frontmatter duplication, glyph checks); reference lists rendered from the citation-audited bib (REFERENCE-TITLE-FIDELITY-1); no browser chrome in the PDF (PDF-NO-BROWSER-CHROME-1); slug-named files (SLUG-FILE-NAMING-1); title-existence and publish-lock before publish; source completeness (references.bib, citation-audit.md, evidence files); deposit integrity gates (relations non-empty, layout verification, frontmatter self-DOI); R2 mirror + D1 + KG + Vectorize re-index (with slug-rename orphan guard if the slug changes).

## UIA — Universal Ignorance Audit (ZENODO-INQUIRY-1)

Committed in UIA-ADELIC-QUANTUM-ARITHMETIC.md (15 questions, 5 phases, core claim as target).

## Phase roadmap

P0 complete (this plan + UIA, tag v0.1-phase0-res029). P1 due diligence (pre-armed: corpus sweep + external verification executed 2026-08-27; evidence files to be materialized). P2 literature/draft. P3 verification integration. P4 red-team. P5 Zenodo deposit. P6 distribution (R2/D1/KG/Vectorize). P7 dissemination. P8 closeout.
