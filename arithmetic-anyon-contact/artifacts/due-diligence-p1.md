# Phase 1 Due Diligence — QNFO.RES.028 (corpus + external evidence, 2026-08-27)

## Corpus sweep

Corpus size at sweep: 8,332 nodes (5,616 Note, 1,667 Paper, 157 Project), 8,523 edges.
Queries run: (1) "quantum statistics adelic product formula squarefree Fermi Bose", (2) "anyon braid fractional exchange statistics bounded occupation", (3) "spin-statistics theorem composite fermion boson Möbius", (4) "primon gas Riemann gas zeta Bost-Connes", (5) "unique factorization domain Gaussian integers function field statistics", (6) "anyon braiding fractional exchange phase topological quantum computing" — 6 formulations across search_papers_enriched (limit ≥ 12) + qnfo-memory-mcp (limit 16) + query_graph nodes (Paper: anyon; Project: adelic).

### Directly relevant records (cross-system ID validation clean for all resolved)

| Record | DOI | Relevance |
|---|---|---|
| Quantum Statistics from the Adelic Product Formula (RES.027) | 10.5281/zenodo.22123068 | Parent; supplies §6 open correspondence |
| The Self-Referential Scalar Family (RES.020) | 10.5281/zenodo.22035210 | Per-place identifications at z = 1/p |
| Finite-Distinction Quantum Mechanics (RES.021) | 10.5281/zenodo.22046458 | γ = 1/N assumption; large-N unitary limit |
| p-Adic Anyon Fusion and Braiding: Quantum Groups at Roots of Unity | 10.5281/zenodo.21208491 | C2 carrier candidate (character/quantum-group braid data) |
| Adelic Synthesis: The Pattern-Particle Correspondence and the Complete Arithmetic Theory of Anyons | 10.5281/zenodo.21208568 | Roots-of-unity anyon dictionary |
| Zitterbewegung as the Physical Realization of p-Adic Anyon Braiding | 10.5281/zenodo.21336087 | Physical-realization leg of the braiding program |
| One Table, Two Regimes: Patterns on the Bruhat-Tits Tree | 10.5281/zenodo.22024856 | Names "p-adic braid phases of abelian anyons" as input; root-of-unity phases on ramified branches |
| Configuration-Space Topology and the Distinction Calculus (RES.011) | 10.5281/zenodo.21962450 | Concedes the spin-statistics boundary; braid group B_N in d = 2 |
| The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant | 10.5281/zenodo.21964598 | R = e^{2πis} [ESTABLISHED]; dimension quantizes s |
| The Exchange Phase as a Logical Scalar | 10.5281/zenodo.21964104 | Exchange phase from the re-entrant mark |
| Operationalizing Generalized Symmetries (anyon halos, FCI moiré) | 10.5281/zenodo.18199396 | Experimental anyon contact (STM/transport protocols) |
| Ultrametric Relaxation Dynamics in Topological Quantum Memory | (KG) | TQ-memory platform context |
| Ultrametric Quantum Computation and the Langlands Program | 10.5281/zenodo.20036379 | Hecke/bruhat-tits substrate context |
| Adelic Shannon Theory (ADL.001) | 10.5281/zenodo.22024240 | p-adic max-ent distribution (the L1 anchor of the chain) |

Adjacent WBS domains: UMP (p-adic anyon braiding, pattern-particle, Bruhat–Tits), RES (RES.020/021/027 chain), SLB (exchange-phase logical scalar, laws of form), INM (max-entropy, adelic Shannon theory). Gap in corpus: **no record adjudicates the m-family against known anyon observables; no record computes a prime-gap thermodynamic signature.** The two live legs (C1/C2 adjudication; H2 prediction) are corpus-novel.

`[CONFIRMATION-BIAS-RISK]`: the corroborating records are overwhelmingly QNFO-internal. External adjudication is therefore load-bearing and is listed below.

## External verification (independent literature)

- **Gentile intermediate statistics:** G. Gentile (1940), "Osservazioni sopra le statistiche intermedie" — the m-capped occupation family is prior art as a *statistical* object. The m-family is its partition function.
- **Haldane fractional exclusion statistics:** F. D. M. Haldane (1991), PRL 67, 937 — the g-form; occupation constraint as a statistical interaction.
- **HES ↔ braid statistics relation (pre-adjudication):** Chen & Ng, "Fractional Exclusion Statistics and Anyons", cond-mat/9411008 (perturbative coincidence via anyon–anti-anyon statistical interaction); Ye, Marchetti, Su & Yu, "Hall effect, edge states and Haldane exclusion statistics in two-dimensional space", arXiv:1512.01783 (non-perturbative: HES holds for incompressible anyon liquids with Hall edge — a special regime, not general). Consequence: exclusion-type constraints coincide with braid phases only in special regimes; the general relation is already known to be non-identity. This is the external anchor for C1.
- **Primon/Riemann gas prior art:** Julia (1990, bosonic primon gas); Spector (1990, supersymmetry and Möbius); Bakas–Bowick (1991); Dueñas & Svaiter, "Thermodynamics of the Bosonic Randomized Riemann Gas", arXiv:1401.8190; Hartnoll & Yang, "The Conformal Primon Gas at the End of Time", arXiv:2502.02661 (the @hartnoll2025 cited by RES.027); Makhaldiani, "Supersymmetric dynamics and zeta-functions", arXiv:1802.01971 ("fermion factorization of the bosonic statistical sum" — the ζ(s)/ζ(2s) squarefree↔fermion factorization is external prior art).
- **Anyon observables for the C1 adjudication:** Laughlin phase e^{iπ/m} at ν = 1/m; Rosenow & Halperin, "Braids and Beams", arXiv:2510.04319 (anyon-collider cross-correlations); Heiblum et al., "Partitioning of Diluted Anyons Reveals their Braiding Statistics", arXiv:2209.15461 (experimental braid-phase measurement); Nagies et al., "Beyond braid statistics", arXiv:2309.04358 (1D exchange statistics beyond the braid group).
- **Bost–Connes (H2 singularity constraint):** Bost & Connes (1995), "Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory" — the KMS/Hagedorn point the specific-heat computation must respect.

## Gap analysis (vs the note's proposed program)

The note (Obsidian _26239094600.md) proposes seven questions (Q1–Q7) and six phases. Corpus + external adjudication:

| Question | Status |
|---|---|
| Q1 isomorphism (empty relabeling?) | Covered by RES.027 §9 register + external Riemann-gas prior art; not a new project |
| Q2 γ = 1/N under heterogeneous degeneracy | Partially covered (RES.027 §3 F2c guard states the κ_i qualification); full characterization of degeneracy structures remains open — follow-on of RES.021 program, not this project |
| Q3 complex-structure selection | Covered (RES.027 §4 + RES.021); open-status "artifact vs principle" belongs to the unitary-limit program |
| Q4 anyonic contact of the m-family | **OPEN — this project (C1/C2)** |
| Q5 spin-statistics boundary | Covered (RES.011 boundary map + pre-registered derivation program T1–T3; the boundary is principled, not to be re-opened) |
| Q6 Möbius parity | Covered (RES.027 §5, published today) |
| Q7 predictive signature | **OPEN — this project (H2)** |

The note's 60-month program is thereby compressed: the corpus has absorbed Q1/Q5/Q6, and the two live legs are the C1/C2 adjudication and the H2 prediction — both computable in-session (Phase 4 of this project).

## ID-validation notes

- `adelic-quantum-statistics` resolves slug → Vectorize (f2b94924…) → KG `paper:adelic-quantum-statistics` → DOI 10.5281/zenodo.22123068; KG zenodo_doi carries the CONCEPT DOI (…067) while D1 doi carries the record DOI (…068) — cross-store discrepancy in the PARENT record's metadata (data-quality finding, flagged for the RES.027 closeout sweep, not blocking this project).
- Duplicate slug rows for `adelic-quantum-statistics` (3) and `self-referential-scalar-family` (3) in Vectorize chunks are per-chunk embeddings, not records (title/DOI identical) — no action.
- Registry (portfolio-state D1) confirms RES.027 is the current highest RES allocation; RES.028 is next.
