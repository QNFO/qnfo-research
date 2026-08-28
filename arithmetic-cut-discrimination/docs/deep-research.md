# Deep Research — QNFO.RES.030 P2: Literature Triage and Symmetry Template

Date: 2026-08-29. Scope: external literature classification for the arithmetic
cut discrimination, on top of the P1 due-diligence evidence
(`artifacts/external-search/phase1-*`). Full citation extraction and
verification runs at P5 per the PROJECT-PLAN phase table.

## 1. Sources

- **P1 external evidence (reused):** arXiv API (1401.8190 Dueñas–Svaiter;
  2502.02661 Hartnoll–Yang; 2411.15377 p-adic kernels), Crossref (Bakas–Bowick
  10.1063/1.529511; Julia 10.1007/978-3-642-75405-0_30, with the 1989 J. Phys.
  root 10.1051/jphys:0198900500120137100).
- **Inherited bibliographic anchors (from UMP.014 §9, re-verified in code at
  P3, not re-derived):** Montgomery 1973; Odlyzko 1987; Gallagher 1985;
  Berry 1985; Bogomolny–Keating 1995; Bost–Connes 1995; Dyson–Mehta (via
  Berry 1985); plus the QNFO register (RES.027–029, UMP.014, RES.023,
  radix-agnostic-dsi-detection, SVAT).
- **Cross-session intake (2026-08-29, UMP.014 red-team gates, session
  Fgxo-Bv4D7kU5BywLA2U6):** POKAZATEL counts corrected against the primary
  literature — 810,269 states / 5,745,071,340 transitions (MNRAS 480:2597,
  2018; MARVELised `.states.bz2` ≈ 6.3 MB). The seed note's "~4.7 million
  levels / 12.7 MB" is FALSE. **Amendment A7 status: CLOSED with evidence.**

## 2. Classification matrix

| Record | Class | Why |
|---|---|---|
| Julia 1989/1990 | **Supports** | Primon gas founded; zeta-function thermodynamics is a legitimate object; the cut generalizes a 35-year external line. |
| Bakas–Bowick 1991 | **Supports** | Arithmetic gases with exponential density of states; exactly solvable models; parafermion arithmetic analogs validate the multi-statistics variant family. |
| Spector 1990 | **Supports** | Bose/Fermi-supersymmetry duality of the zeta gas; the squarefree/Bose dichotomy predates QNFO. |
| Hartnoll–Yang 2025 | **Supports** (complicates D2) | L-function generalization; their averaging over chemical potentials is an ENSEMBLE average, distinct from RES.030's matched-density level-set nulls — the paper must name the difference. |
| p-adic kernels 2024 | **Constrains** | Finite p-base primon gas via large deviations (GREM): the finite-P_max crossover is expected to scale like a random-energy crossover; width ~1/ln P_max must be checked against this literature, not asserted. |
| Dueñas–Svaiter 2014 | **Constrains** | Ensemble averaging over Hamiltonians WASHES OUT the zeta pole (non-enumerable ensemble ⇒ no singularity). Rule: RES.030's C_V discrimination uses single realizations only; no ensemble averaging of the thermodynamic observable (aligns with construction rule B5). |
| Gallagher 1985 | **Constrains** | Primes are Poisson-like beyond the twin-gap hard core: at large P_max the level statistics approach Poisson, so the arithmetic signal lives in the hard core + two-point corrections, not in the mean spacing. D2 must be measured where the signal is, i.e. at small-to-moderate s. |
| Montgomery–Odlyzko | **Supports** (anchor) | The two-point signature of an arithmetic object (Riemann zeros) matches GUE; validated in code (P3). |
| Bogomolny–Keating 1995 | **Constrains** | Arithmetic corrections are subleading oscillations beyond the GUE bulk — detection needs statistical power and matched nulls, exactly RES.030's D1/D2 framing. |
| Bost–Connes 1995 | **Supports/Constrains** | Supports: Z(β)=ζ(β) with the β=1 transition is the reference system. Constrains: the transition exists only in the infinite-prime limit; at finite P_max it is a crossover (amendment A4). |
| prime-numbers-as-spectral-artifacts (2025, corpus) | **Contradicts (weakly, externally)** | Claims primes "emerge with logical necessity" from continuous substrates — stronger than the 2026 null-ledger supports; a caution, not an input. |

**No external record constructs matched-level-density non-arithmetic nulls for
the primon-gas observable** — gap G2 confirmed at the literature level. The
null class RES.030 introduces is new against BOTH the QNFO corpus and the
external primon-gas line.

## 3. KIF-18 Mandatory Symmetry Template

### Where external literature supports the claim
The primon gas is not a QNFO invention: Julia founded it, Bakas–Bowick and
Spector established the Bose/Fermi arithmetic dichotomy, and Hartnoll–Yang
still develop it in 2025. RES.027–029's identification (unrestricted
occupation ⇔ ζ(β) ⇔ Bose; squarefree ⇔ ζ(β)/ζ(2β) ⇔ Fermi) extends a
legitimate external object, and the specific-heat observable inherits the
Bost–Connes reference system. The D1 objects (partition functions, specific
heats, two-point statistics) are standard; the discrimination QUESTION is what
is new.

### Where external literature constrains or contradicts
- **Averaging kills the signal** (Dueñas–Svaiter): no ensemble averaging of
  C_V; single realizations only.
- **Asymptotic Poisson** (Gallagher): at large P_max the prime level statistics
  drift toward Poisson beyond the hard core; any discrimination claim must
  specify the s-range and the P_max at which the two-point signal is measured.
- **Finite-size crossover** (p-adic kernels/GREM; Bost–Connes): the β=1
  "transition" is a finite-P_max crossover with width ~1/ln P_max; the
  observable must be framed as a crossover (amendment A4), or the claim
  reduces to "a rounded bump that looks like the ghost of a transition."
- **The GOE/GUE distinction at correction order** (seed-cluster verdict
  11209): GOE bulk pair correlation equals GUE's, but at the arithmetic-
  correction level the ensemble matters — true GUE nulls are mandatory (A2/D-2).

### Where the two sides converge
The external primon-gas literature uses ensemble averages over Hamiltonians or
chemical potentials precisely because the single-system signature is subtle.
RES.030 inverts that choice: it holds the system fixed (the cut) and varies
the null ensemble (matched-density non-arithmetic spectra) — the complementary
design, and the one that answers the program's own red-team objection. This
convergence claim is the paper's positioning statement (P5 prose).
