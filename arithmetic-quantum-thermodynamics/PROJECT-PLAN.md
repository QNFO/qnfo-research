# WBS: QNFO.RES.031

# Project Plan — Arithmetic Quantum Thermodynamics

- **WBS:** QNFO.RES.031
- **Slug:** arithmetic-quantum-thermodynamics
- **Repo:** QNFO/qnfo-research · **Branch:** res/paper/arithmetic-quantum-thermodynamics
- **Program:** QNFO.RES (qnfo-research)
- **Predecessors:** QNFO.RES.027 adelic-quantum-statistics (10.5281/zenodo.22133122), QNFO.RES.028 arithmetic-anyon-contact (10.5281/zenodo.22124744), QNFO.RES.029 adelic-quantum-arithmetic (10.5281/zenodo.22142794), QNFO.RES.030 arithmetic-cut-discrimination (10.5281/zenodo.22152967), QNFO.UMP.014 distinction-based-ultrametric (10.5281/zenodo.22150472), QNFO.RES.021 finite-distinction-quantum-mechanics (10.5281/zenodo.22046458)
- **Prior claimants (build on, do not re-claim; red-team M-2, 2026-08-29):** QNFO.SLB.001 idempotent-core (10.5281/zenodo.21916939) and the LoF Number Builder Calling→N derivation (archive record `lof-number-builder-interactive-specification-v10`, R2 `qnfo/releases/2026/07/silent-radix/`, no DOI) already claim the pre-arithmetic cut and the counting construction (L0–L1, Part I); ultrametric-program v2.5.1 (10.5281/zenodo.22076816) defines the realization-independent structural object. RES.031 Part I and C2 L0–L1 are stated as building on these, never as new claims.
- **Seed provenance:** vault notes `D:\Obsidian\notes\v1\2026\08\29\` — `p-adic QM_2.md` (canonical export; stale strict-prefix snapshot `_stale-snapshot-p-adic QM_2(1).md` archived 2026-08-29), `_26241061202.md` (research agenda T1–T11, RQ1–RQn), `_26241061205.md`, `_26241061940.md` (five-level ladder; fragment, ends mid-sentence at T10), `_26241061955.md` (pre-arithmetic audit), `_26241062020.md` (dependency stack), `_26241085200.md` (Dictionary draft), `_26241090044.md` (treatise outline Ch. 3–17 + Appendices; Ch. 1–2 live in `p-adic QM_2.md`). P2 seeds (post-date the original set; red-team I-2, 2026-08-29): `Pre-arith.md` (treatise architecture, working title "Distinction, Number, and the Statistical Content of Physics"), `_26241092252.md` (framework directive — consistent with locked C2/C4), `_26241091602.md` (UIA process note, target-missing variant — superseded by `docs/uia-15q-res031.md` which states the target). Chat-log content is provenance, not registry — every quantitative claim reused here is verified against a DOI'd record before citation (QNFO-CHAT-PROVENANCE-1).
- **Phase 0 lock date:** 2026-08-29

## 1. Charter

The arithmetic-statistics line (RES.027–RES.030, UMP.014) has established, in
successive published records, the identification of exchange statistics with
exponent rules on one integer lattice, the bounded-occupation (Gentile)
continuation with its no-exchange-phase adjudication, the consolidated map,
and the computational discrimination of the arithmetic cut from
matched-density nulls (D1 CONFIRMED, D2 disconfirmed as pre-registered). The
line now possesses a substantial but informal "Dictionary of Arithmetic
Quantum Thermodynamics" — a term-by-term mapping between quantum
statistical mechanics and multiplicative number theory — drafted in the
provenance chats, alongside a treatise outline (Chapters 1–17) and an
interpretive architecture (a five-level ladder L0–L4, a channel taxonomy,
and a correction ledger).

That dictionary, as drafted, contains specific technical misstatements that
must not be allowed to propagate into the published literature: the
single-particle/many-body label conflation; the chemical-potential-vs-
Dirichlet-character conflation; an inconsistent Maxwell–Boltzmann row; a
specific-heat definition missing the −β² factor; an entropy formula with a
dimensionally wrong second term; the attribution of the 34σ small-spacing
exclusion to the Riemann zeros when it probes the primes; the claim that
analytic continuation is the thermodynamic limit; and the meta-lemma
"primes are energy eigenstates." Each is an audit-fixable, code-verifiable
error, and each is exactly the kind of error an adjacent-domain reader will
copy from an uncorrected dictionary.

This project converts the informal dictionary and interpretive architecture
into a single audited, corrected, computationally verified record: the exact
primon-gas correspondence (structure), the five-level interpretive ladder
with explicit inference rules (interpretation), the correction ledger with
each fix verified in code (correction), and the negative list stating what
the consilience does not imply (discipline). It adds no new empirical claims;
the empirical content of the line remains RES.030's adjudication. It exists
so that the correspondence can be cited, taught, and implemented from one
corrected source.

### 1.2 Core claim (P6 — LOCKED at Phase 0)

The object: the primon gas — single-particle modes indexed by primes p with
energies ε_p = ln p; many-body states indexed by integers n = ∏_p p^{a_p};
Hamiltonian = multiplication by ln n; inverse temperature β.

- **C1 (exact dictionary).** The grand canonical partition functions are
  exactly: Z_Bose(β) = ∏_p (1 − p^{−β})^{−1} = ζ(β) (unrestricted occupation
  a_p ∈ {0,1,2,…}); Z_Fermi(β) = ∏_p (1 + p^{−β}) = ζ(β)/ζ(2β) (squarefree,
  a_p ∈ {0,1}); ln Z_MB(β) = Σ_p p^{−β} = P(β) (prime zeta); and the Gentile
  family Z_m(β) = ∏_p (1 − p^{−(m+1)β})/(1 − p^{−β}) with m = 1 → Fermi,
  m → ∞ → Bose, and no exchange phase anywhere in the family. Prime-zeta
  expansions: ln Z_Bose = Σ_{k≥1} P(kβ)/k, ln Z_Fermi = Σ_{k≥1} (−1)^{k+1}
  P(kβ)/k. The correspondence is exact and model-specific: primes are the
  single-particle modes, integers the many-body states, the zeta function the
  partition function.
- **C2 (five-level ladder).** "Arithmetic structure in physics" claims
  stratify into L0 (distinction — the unanalyzable primitive), L1 (the
  distinction-based ultrametric — definitional, realization-independent),
  L2 (Euler products and zeta identities — exact mathematical isomorphism),
  L3 (physical spectra carry arithmetic correlations beyond universal
  random-matrix statistics — falsifiable distributional hypothesis), L4 (a
  specified system realizes the arithmetic partition function — physical
  instantiation). Inference rules: **L2 cannot imply L4**; **L3 is the only
  admissible bridge**; L4 requires a protocol (specified spectrum, specified
  counting rule, pre-registered null, pre-registered test).
- **C3 (correction ledger).** The following drafted-dictionary statements are
  errors and are corrected in this record, each with a code-verifiable fix:
  (a) ε_i ≡ ln n_i conflates single-particle modes (primes) with many-body
  states (integers); (b) chemical potential (fugacity z = e^{βμ}) is not a
  Dirichlet character — Z_μ = ∏_p (1 − z p^{−β})^{−1} is not an L-function;
  (c) the Maxwell–Boltzmann row "∏(1+x_p) with an extra N! label" is
  inconsistent with the unification rule ln Z_MB = P(β); (d) the specific-heat
  definition must be C_V = −β² ∂_β U (missing −β² factor in the draft);
  (e) the entropy's second term must carry β ln p: S = Σ_p [−ln(1−x_p) +
  β ln p · x_p/(1−x_p)], x_p = p^{−β}; (f) the 34σ small-spacing exclusion
  probes the primes (twin-gap hard core: first bin exactly zero), not the
  Riemann zeros — the zeros are GUE-like (Montgomery–Odlyzko), the primes
  Poisson-like beyond the hard core (Gallagher); (g) analytic continuation of
  ζ is not the thermodynamic limit — the finite-P_max cutoff is a smooth
  crossover, and β = 1.06 is an evaluation point, not a phase-transition
  temperature of any finite system; (h) "prime numbers are energy
  eigenstates" is wrong — the eigenstates of H = ln n are the integers;
  (i) the Hamiltonian is the multiplication operator by ln n, not the
  arithmetic derivative / von Mangoldt operator; (j) Dirichlet convolution is
  a formal parallel to interactions, not an interaction term, and ζ^k
  corresponds to k independent species, not k-body interactions; (k) the
  drafted "Theorem 2" conflates the specific-heat observable with the 34σ
  small-spacing test — they are different observables with different nulls.
- **C4 (negative discipline).** The consilience does NOT imply: a derivation
  of spin–statistics; a universe made of primes; an identification of Riemann
  zeros with measured energy levels; or evidence for Hilbert–Pólya. The zeros
  enter through the explicit formula as subleading oscillatory corrections to
  the smooth level count — fluctuations, not definitions.

Disconfirmation matrix (pre-registered): C1 is theorem-level — it fails if
any identity above is wrong, and each is recomputed in the verification
suite; C2 is methodological — it fails if an admissible L2 → L4 inference is
exhibited; C3 is audit-level — it fails if any stated correction is itself
wrong, and each fix is verified in code against exact truncated products and
recoverable anchors: β²/(β−1)² = 312.1 at β = 1.06 is the analytic anchor;
the exact recomputed total is 311.9 (parent-verified 2026-08-29: finite sum
to P_max = 1e7 = 78.49 + analytic tail 233.42); the twin-gap first bin is
exactly zero under its stated conditions (minimum prime gap 2 ⇒ minimum
unfolded spacing 2/ln p; bin width below that; primes ≥ 3); the legacy value
C_V(1.06) ≈ 316.3 carried by the published lineage is an adjudication target
(NOT a recoverable anchor — it is a finite-difference artifact, red-team
M-1, parent-reconfirmed). C4 is scope discipline, enforced by the negative
list in the published prose. The record adds no new empirical claims; the
empirical content remains RES.030's (D1 CONFIRMED, D2 disconfirmed as
pre-registered). The negative branch — a materially different corrected
dictionary after audit — is publishable per the program null-ledger.

**Interpretive structure (outside the locked claim; red-team M-4).** The
seed framework's channel taxonomy (geometric / spectral-statistical /
thermodynamic, `_26241061940.md` §3) organizes Part III but is an organizing
device, not a claim: it carries no truth value and is therefore outside
C1–C4. Where it appears in reports, it is cited as seed framework, not as a
locked claim.

## 2. Why a reader should care (SO-WHAT)

Anyone using the primon-gas / Bost–Connes / Riemann-gas correspondence —
number theorists, quantum-statistical-mechanics researchers, and the
random-matrix community — currently has no single corrected reference: the
published lineage itself carries two adjudicated quantitative errors (the
Dyson number-variance window pair; the 316.3 specific-heat attribution —
RES.030 D-1/D-4), and the sign/attribution errors catalogued in this
record's correction ledger would propagate into the literature if left
uncorrected. This record is the audited artifact: it fixes the recurring −β²
specific-heat factor, the entropy term, and the 34σ zeros/primes conflation,
and it states, in print, precisely what the correspondence licenses and what
it does not. (Red-team A-3/B-2 remediation 2026-08-29: the exposure claim is
scoped to the two published-lineage errors plus prevention — not to external
readers copying an internal draft.) For a spectroscopist or metrologist
evaluating an "arithmetic
spectrometer" (engineered log-prime spectra in superconducting registers,
optical lattices, or photonic arrays), the five-level ladder's central rule —
the mathematical isomorphism (L2) does not by itself license a physical
realization claim (L4); only a pre-registered statistical test at L3 does —
decides in advance what such an experiment could ever claim to have measured.
Both audiences get a map that is exact in the toy model and disciplined at
the physical boundary.

## 3. Phases with WBS

| Phase | WBS step | Content | Gate |
|---|---|---|---|
| P0 | RES.031.P0 | Init: WBS resolution (program_registry check-then-insert), branch, scaffold, PROJECT-PLAN, core-claim lock, stale-snapshot archive | commit/tag/push |
| P1 | RES.031.P1 | Due diligence: ZENODO-INQUIRY-1 UIA 15Q, DUE-DILIGENCE-DEPTH-1 corpus sweep, external verification, gap analysis | HARD |
| P2 | RES.031.P2 | Literature + corrected-dictionary construction (C3 ledger; SPECTRAL-ESTIMATOR-CONSTRUCTION-1 checklist where spectral quantities appear) | HARD |
| P3 | RES.031.P3 | Computational verification suite (VERIFY-IN-CODE-1): every C1 identity, every C3 correction, golden anchors, seeded checks | HARD |
| P4 | RES.031.P4 | Deep research + red team (5 adversary positions + UIA cross-check) | HARD |
| P5 | RES.031.P5 | Publish: Zenodo deposit, publication gates (PUBLICATION-PROSE-1, COMPUTATIONAL-VERIFICATION-1, PRACTITIONER-RELEVANCE-1, CROSSWALK-TRANSLATION-1) | HARD |
| P6 | RES.031.P6 | Deploy: D1 living-paper, KG node, Vectorize, R2 mirror | HARD |
| P7 | RES.031.P7 | Disseminate: SEO, Buffer, papers.qnfo.org, Internet Archive | SOFT |
| P8 | RES.031.P8 | Distribute: GitHub tag, closeout, registry re-point, memory log | HARD |

## 4. Milestones with gate criteria

- **M0** Phase 0 committed, tagged v0.1-phase0-res031, pushed, ls-remote
  verified; registry row active/P0 inserted check-then-insert and verified by
  re-query; stale snapshot archived. (HARD)
- **M1** UIA 15Q committed (instrument DOIs 10.5281/zenodo.21901984 +
  10.5281/zenodo.21901983); corpus sweep with ≥3 query formulations per topic,
  search_papers limit ≥20, resolve_paper_id per hit, ≥2 adjacent WBS domains
  (UMP, RES minimum; SLB/INM/CFE where the distinction content warrants),
  external verification (arXiv/OpenAlex/Crossref/Zenodo/CDX/Google Patents),
  every count with an evidence file in artifacts/external-search/. (HARD)
- **M2** Corrected dictionary complete; every C3 ledger row carries a
  computable fix; spectral quantities follow SPECTRAL-ESTIMATOR-
  CONSTRUCTION-1 (k-th-neighbor pair correlation, exact Li unfolding, full
  Dyson formula, no rank unfolding, Montgomery–Odlyzko on zeros / Gallagher
  on primes, form factor report-only at fixed τ). (HARD)
- **M3** Every quantitative claim reproduced by deposited deterministic
  scripts; anchors recovered per the annotated definition in §1.2 (analytic
  β²/(β−1)² = 312.1; exact total 311.9; twin-gap first bin zero under its
  stated conditions; exact truncated products for C1 identities). The legacy
  316.3 is treated as an adjudication target only. (HARD)
- **M4** Red team delivered; HARD findings remediated or pre-registered.
- **M5** Published with plain-prose abstract naming the bridge (primon gas /
  zeta partition functions / interpretive discipline), practitioner section,
  premise-boundary statement (premises end where a physical temperature would
  be identified at a p-adic place; no such identification is asserted), full
  source deposit. (HARD)
- **M6–M8** Distribution complete; registry re-pointed to published DOI.

## 5. Deliverable Registry

- DR1 Paper `<slug>.md/.html/.pdf` (never `paper.*`), **LEAN shape** (red-team
  B-1/B-2 remediation, 2026-08-29 — the seed's 17-chapter treatise is source
  material, NOT the deliverable): (1) the corrected dictionary as the
  centerpiece; (2) the five-level ladder with its inference rules; (3) the
  correction ledger C3(a)–(k); (4) the negative discipline list C4; (5) the
  practitioner section (PRACTITIONER-RELEVANCE-1); (6) the verification
  appendix (both suites + reproducibility). The pre-arithmetic cut (seed Part
  I) is credited in two paragraphs to SLB.001 / LoF Number Builder /
  ultrametric-program — not re-derived. The statistical channel (seed Part
  III) becomes a roadmap appendix: the real-data rows (NaH, H₂O POKAZATEL)
  and the 2028 H1 decision matrix are cited as RES.030/UMP.014 content and
  roadmap items, NOT as this record's claims (they are not reproduced by this
  record's suites — M3). The P5 title is constrained by the bridge vocabulary
  (primon gas / zeta partition functions / interpretive discipline) — it must
  not outrun the charter (UIA Q15 seeded question).
- DR2 Verification scripts + outputs in `artifacts/verification/` (deposited
  with the paper).
- DR3 Corrected-dictionary reference table (machine-readable, e.g. TSV/MD).
- DR4 UIA 15Q report + due-diligence report + red-team reports +
  external-search evidence + deep-research.md.
- DR5 Interactive demo via qwav-demo-kit (DEM-E0 flag, if flagship): the
  primon-gas partition-function identities as an interactive emulator.

## 6. Risk Register

- R1 Dictionary-correction errors of our own → C3 is itself code-verified
  (M3); any correction that fails verification is withdrawn in P4.
- R2 Conflating the mathematical correspondence with a physical claim → the
  C4 negative list and the L2-≠-L4 rule are enforced in the published prose;
  map–territory labels per KIF-60.
- R3 Redundancy with prior records (RES.027–030 overlap) → the charter
  positions this record as the audited consolidation + correction, not a new
  empirical result; title/abstract carry the bridge vocabulary (TERMINOLOGY-
  SILO-LESSONS-1).
- R4 Propagation of the stale chat snapshot → the stale file is archived at
  P0; all quantitative reuse is DOI-verified (QNFO-CHAT-PROVENANCE-1).
- R5 Premise overreach at the L3/L4 boundary → premise-depth disclosure
  states where the premises end; no physical temperature is identified at a
  p-adic place.
- R6 Scope blow-up → the LEAN DR1 shape is the published target (red-team
  B-1/B-3, 2026-08-29); the seed treatise architecture is source material
  only; the lean fallback is pre-authorized by §7 (Success Criteria do not
  require the treatise shape).
- R7 Demo deferral → DR5 ships only if the in-app E₁-tail correction is
  implemented (an interactive emulator truncated at interactive P_max
  otherwise displays values far from the verified anchors 311.9/312.1);
  otherwise deferred to post-P6. (Red-team B-3.)

## 7. Success Criteria (red-team I-4, 2026-08-29)

- The corrected dictionary (DR3) is complete and every C3 row carries a
  code-verified fix that passes the Phase 3 suite (M3).
- The published record states C1 (exactness of the correspondence), C2 (the
  ladder with its inference rules), C3 (the correction ledger), and C4 (the
  negative list) in prose readable by an adjacent-domain expert
  (CROSSWALK-TRANSLATION-1); the title/abstract name the bridge.
- The disconfirmation matrix is pre-registered, the negative branch remains
  publishable, and the empirical-content attribution (RES.030 D1/D2) is
  accurate in print.
- The correction ledger is complete enough that no twelfth uncorrected error
  is found by the Phase 4 re-audit (the pre-registered completeness check).
- P8 distribution state: registry phase P8/published, DOI live-verified, R2
  mirror complete, per the RES.030 closeout template.
