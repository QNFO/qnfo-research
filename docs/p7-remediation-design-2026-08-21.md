# P7-Remediation Design — QNFO.RES.021 (2026-08-21)

Deferred-work handoff from session `hP2uBoAeyXicuV25947MO` closeout. The P7 audit
(`docs/red-team-report-p7-2026-08-21.md`, head 17e1d36) left **2 HARD + 6 SOFT** to
remediate before P8 publish. This note captures the design analysis completed during
the cut-off remediation turn so the next session does not re-derive it — including a
non-obvious trap in the V5 rewrite (two candidate constructions FAIL; only the third
design works).

---

## H-1 — §5 "2-norm and complex structure" test promise → add V7

Draft §5 promises a computational test of the 2-norm/complex-structure selection; no
check tests it. **V7 design (executable, stdlib-only):**

- **Generator:** the reversible (cyclic-shift) generator L on the N-amplitude space,
  `(L ψ)_i = (ψ_{i+1} − ψ_{i−1})/2` (indices mod N). Skew-symmetric by construction.
- **V7a (2-norm selection):** at a seeded concentrated ψ (e.g. ψ_i = √p0_i),
  assert `|ψᵀLψ| < 1e-14` (skew ⇒ d‖ψ‖₂²/dt = 2ψᵀLψ = 0 exactly — the 2-norm is
  conserved); assert `Σ sign(ψ_i)(Lψ)_i > 1e-6` and `3Σ ψ_i|ψ_i|(Lψ)_i > 1e-6`
  (the L1 and L3 norms of the amplitude vector DRIFT — only p = 2 is selected).
- **V7b (complex structure via the spectrum):** DFT of L — golden values
  `λ_k = i·sin(2πk/N)` (purely imaginary). Assert `max_k |Re λ_k| < 1e-12` and
  `max_k |Im λ_k − sin(2πk/N)| < 1e-12` for N = 2² … 2⁸ (O(N²) manual DFT).
- **§5 sentence rescope (draft edit, not the locked claim):** the parenthetical
  "(to be tested computationally in the verification program)" becomes: "the 2-norm
  invariance of the reversible dynamics and the purely imaginary spectrum of its
  generator are verified computationally (V7); the selection of the complex
  structure as the physical algebra remains the theoretical target delimited by
  Hardy [27] and Aaronson [28]."
- Add a V7 row to the §9 table + the V7 numbers to the §9 results block.

## H-2 — V5 does not implement the §9 row → rewrite (trap analysis inside)

**The trap (both naive rewrites FAIL — do not re-try them):**
The flow model (V3/V4: E_i = i/N, β ≈ 0 ⇒ p* ≈ U uniform, cyclic shift + γ(p* − p)
with γ = 1/N, dt = 0.05) has TWO competing timescales that cancel at large N:
- (a) **Fixed-window average:** a window of M samples covers only a PARTIAL shift
  orbit when N > 2M (orbit period = N) — the partial-orbit average does NOT
  converge to the uniform measure; the concentrated initial mass keeps the
  deviation D ≈ 0.5 at large N. **FAILS "deviation shrinks with N".**
- (b) **Full-cycle window (M = N):** the orbit average over a full cycle is exactly
  U, but the relaxation residual survives at O(1): the decay factor over one cycle
  is e^{−N·dt·γ} = e^{−0.05} ≈ 0.95 independent of N, so the relaxation does not
  clean up the window. **FAILS** — deviation is O(0.05), N-independent.
- (c) **Stationary-point check:** p = shift(p) + dt·γ(p* − p) has the unique fixed
  point p_∞ = p* (Fourier argument: (1 − e^{2πik/N} + dt·γ)δ_k = 0 ⇒ δ_k = 0 for
  k ≠ 0). D = 0 identically — **VACUOUS** (the degenerate-construction trap the P5
  red-team already flagged for V3/V4).

**Final design (recommended, satisfies the §9 row honestly):**
- **V5a (equilibrium identity):** run the flow from the concentrated p0 for
  T = 100N steps (relaxation time = 20N; e^{−5} ≈ 0.0067 residual), N = 2⁴ … 2⁸
  (N = 256 ⇒ 25,600 steps — OK in pure Python; larger N covered by the analytic
  fixed-point argument above, stated in the README). Assert ‖p_T − p*‖₁ < 1e-6.
  This verifies the flow's equilibrium IS the maximum-entropy state — the model
  content of H-BORN.
- **V5b (±2σ tracking):** at p*, draw M = 200 seeded multinomial samples per N;
  empirical frequencies f̄; per-alternative z_i = |f̄_i − p*_i|/σ_i with
  σ_i = √(p*_i(1−p*_i)/M). Assert max_i z_i ≤ 2.5 at every N (the ±2σ band,
  computed and REPORTED — this is the criterion the P5 code never computed) and
  report the per-alternative tolerance σ_max ~ 1/√(NM), which shrinks with N (the
  resolution of the Born-vs-maxent comparison improves with the distinction count).
- **Falsifier-live control:** the same measurement against the concentrated initial
  state (f̄ = p0) — z_i explodes past the band at large N (deviation O(1) vs
  σ_i ~ 1/√N). This control FAILS the ±2σ band, proving the test is not vacuous.
- Update the §9 V5 row results + the README (6/6 checks with V7; V5 described as
  above).

## SOFT-6 — word-grade fix on the locked claim (PROJECT-PLAN §2)

"unitary evolution and superposition emerge as the large-distinction limit of the
entropy-Hessian gradient flow — **verified at finite N by the computational program**
(per-step entropy production exponent −0.88, symplecticity-defect exponent −1.00,
seed 20260821)" →
"... — **supported at finite N within the per-distinction model** (per-step entropy
production exponent −0.88, symplecticity-defect exponent −1.00, seed 20260821); the
physical status of the per-distinction rate structure remains open (draft §9)".

This is a MATERIAL change to the locked claim ⇒ per the lock rule: version bump +
UIA delta re-run. Add the lock-record entry: "P7-remediation restatement
(2026-08-21): 'verified at finite N' → 'supported at finite N within the
per-distinction model' — the program verifies the model family's behavior; the
physical status of the rate structure stays open (draft §9); audit H-3/S-6,
docs/red-team-report-p7-2026-08-21.md."

## S-1 / S-2 one-liners

- **S-1:** V1 add a seeded non-uniform point (e.g. p = (0.2, 0.3) at N = 3) —
  the identity is exact but the uniform-only test leaves a symmetry caveat.
- **S-2:** §9 V6 row wording: "relational-dynamics simulation" → "finite-resolution
  clock simulation" (the check is a discrete-time integrator-error test, not a
  Page–Wootters construction).

## v1.0.1 checklist (order matters)

1. Edit `artifacts/verification/finite-distinction-verification.py`: S-1, V5 rewrite,
   V7 addition. **Re-run** → 6/6 PASS (VERIFY-FIX-RERUN-1: deposit passing log only).
2. Update `artifacts/verification/README.md` (6/6, V7, new V5, v1.0.1 note) + run log
   + results JSON.
3. Edit draft: §5 rescope (H-1), §9 V6 row (S-2), §9 table + results (V7 row, new V5
   numbers), frontmatter `version: 1.0.1`, `locked: 2026-08-21 (P7-remediation; tag
   v1.0.1-phase7-res021)`.
4. Edit PROJECT-PLAN §2: SOFT-6 wording + lock-record entry + status line.
5. Hypothesis cards: P7-remediation gate entry (no falsifier triggered; V7 added; V5
   rewritten; S-6 restatement — grades unchanged, wording only).
6. UIA delta pass: `artifacts/universal-ignorance-audit-v101-2026-08-21.md` (compact
   delta vs P6: Q1 scaffolds unchanged; Q3 wobbles unchanged + V7 evidence; Q12/Q13
   the S-6 fix executed; Q15 seed for P8).
7. Commit, tag `v1.0.1-phase7-res021`, push, ls-remote verify.
8. Then P8 per handoff 28663 (pre-publish pass + Zenodo records-API deposit + R2/D1/KG
   distribution + program_registry re-point + P7.2 post-publish audit); create the
   paper README at P8 publish-prep (S-3, README-MISSING-ON-PUBLISH-1).

**S-3 remains open:** no paper-specific README (root README.md is the program-repo
aggregation readme) — P8 publish-prep item, not a draft modification.
