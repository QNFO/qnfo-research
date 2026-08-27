# S10 — Differential Primon-Gas Audit (F4 executable artifact)

QNFO.RES.027 · artifacts/external-search/primon-gas-differential-audit-2026-08-27.md
Date: 2026-08-27. Purpose: the executable F4 falsifier — the exact novel delta of
RES.027 against the published primon-gas / Riemann-gas lineage, stated so the F4
claim ("the delta is not already published") is a checkable statement, not an
assertion.

## The lineage (verified on-topic, wave 2; arXiv IDs confirmed via get_abstract + OpenAlex)

| Work | Content | Overlap with RES.027 |
|---|---|---|
| Julia (1990); Spector (1990) — primon / Riemann gas | primes as modes with energies log p; zeta(s) as the bosonic partition function | unrestricted → bosonic identification (T1b) — PUBLISHED PRIOR ART |
| Bakas–Bowick (1991) and successors | fermionic primon gas; squarefree ↔ zeta(s)/zeta(2s) | squarefree → fermionic identification (T1a) — PUBLISHED PRIOR ART |
| Hartnoll–Yang (arXiv:2502.02661) — Conformal Primon Gas | conformal extension of the primon gas | mode-energy frame — adjacent, not the delta |
| Baytaş–Rodrigues–Yokomizo (arXiv:2602.11927) | bosonic/fermionic statistics in nonperturbative QG | statistics from constraints — adjacent |
| Zhou–Chen–Chen–Shen–Zhang–Dai (arXiv:2505.17361) | 3D exclusivity bound | exclusion-bound family — adjacent to F6, not T1–T3 |
| Medina Sánchez–Dakić (arXiv:2306.05919) — transtatistics | interpolation between statistics | adjacent to H-PARASTATS-INTERMEDIATE |
| Wang–Hazzard (arXiv:2308.05203) — parastatistics | bounded-occupation S_N representations | adjacent to F6 |
| Combescot–Dubin–Dupertuis (arXiv:0903.2664) | composite bosons | adjacent to H-COMPOSITE-PARITY |
| Timberlake–Tucker (arXiv:0708.2567); Huang (hep-th/0308095); Sanchis-Lozano et al. (arXiv:1201.6541); Matthews et al. (arXiv:1106.1166) | spin–statistics adjacent results | adjacent |

## Published-prior-art correction (F4 re-scope, 2026-08-27)

The per-place identifications R1/R2 — p-adic maximum-entropy distribution equals
Bose–Einstein occupation at z = 1/p (β_p = ln p); squarefree restriction equals
Fermi–Dirac occupation at the same β_p — are PUBLISHED in QNFO.RES.020 v1.3.0
(10.5281/zenodo.22035210). The development note
`_adelic-statistics-thermo-qnd-synthesis-2026-08-20.md` is RES.020's source
artifact; its run carries one FAIL entry (born_degeneracy, max_deviation 0.5 vs
tolerance 0.01), which is flagged and never inherited. T1's per-place
identifications are therefore corpus prior art, and RES.027's delta is scoped to
exactly six items:

1. **T1-general:** publication-grade generalization of R1/R2 — arbitrary
   (β, μ, p) golden occupations (F1d) plus the global lattice identities
   (F1a/F1b/F1c: squarefree/unrestricted Dirichlet series vs zeta(s)/zeta(2s)).
2. **T2:** the γ = 1/N degeneracy derivation — the rate RES.021 section 9 left
   open ("which heat bath, and which spectral measure, would supply a rate
   proportional to 1/N is open"). Mechanism: the N-fold degeneracy of a bath of
   indistinguishable alternatives cancels the individual transition rates
   (verify_rate_gamma.py, F2 + S2 degeneracy guard, 15/15 PASS, seed 20260827).
3. **T3:** the symplectic emergence as the large-N Fermi limit — J² = −1
   selected in the Fermi case only, absent (symmetric/diffusive) in the Bose
   case (verify_symplectic.py, F3, 34/34 PASS: J² = −sin²θ finite-N honesty,
   sign-normalized H² = −1, Bose-side real-spectrum contrast).
4. **F5:** the composite-parity/Möbius bridge (H-COMPOSITE-PARITY, three legs).
5. **F6:** the anyonic/intermediate-statistics program (predictive card with
   named observable targets — Laughlin phases, MZM/Ising, Fibonacci,
   Wang–Hazzard parastatistics).
6. The crosswalk table + practitioner content.

## Verdict

The F4 delta holds against every verified lineage member: no published work
derives γ = 1/N from bath degeneracy in the primon-gas frame, and no published
work links the Fermi-selected symplectic structure J² = −1 to the squarefree
restriction. The two headline identifications (squarefree ↔ Fermi–Dirac,
unrestricted ↔ Bose–Einstein) are cited prior art in every claim — never
asserted de novo. The F4 gate remains falsifiable: any newly surfaced record
containing the T2 mechanism or the T3 Fermi-symplectic link is added to the
table and the delta re-scoped in the next cycle.
