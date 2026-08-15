# T1/T2 Full Check — DiLL Exponentials and the Two Statistics

**WBS:** QNFO.RES.009.P1 · **Date:** 2026-08-14 · **Status:** COMPLETE (structural check, this cycle)
**Scope:** Full structural verification of tasks T1 and T2 of the paper's §5 derivation
program (DOI 10.5281/zenodo.21938971), including the linear-logic exponential laws
(dereliction, digging, promotion, Seely) for the two modal exponentials !_S and !_Λ,
the ribbon identity on a self-dual mark, and the n-particle character argument.
Labeling discipline: [ESTABLISHED] = standard result; [STANDARD] = textbook-level;
[PROJECT] = explicit synthesis performed for this program; [FINDING] = new sharpening
that changes a program statement; [OPEN] = unresolved.

## 0. Setup

Category: **Vect^Z2_C** — finite-dimensional Z/2-graded complex vector spaces,
symmetric monoidal with the graded braiding

σ_{A,B}(a⊗b) = (-1)^{|a||b|} b⊗a.

The two candidate exponentials on A = the mark space:

!_S(A) = Sym(A) = ⊕_{n≥0} S^n(A),   S^n = (A^⊗n)^{S_n} (ungraded-permutation coinvariants),
!_Λ(A) = Λ(A) = ⊕_{n≥0} Λ^n(A),     Λ^n = A^⊗n quotient by a∧a = 0 relations.

## 1. T1 — both constructions are DiLL exponentials

### 1.1 Dereliction and digging (comonad structure)

**Claim.** Sym is left adjoint to the forgetful functor CAlg → Vect; hence
T = U∘Sym is a comonad. [ESTABLISHED — free/forgetful adjunction.]
- **Dereliction** (counit) ε_A : Sym(A) → A = projection onto the n = 1 summand.
- **Digging** (comultiplication) δ_A : Sym(A) → Sym(Sym(A)) = the coalgebra map
  induced by the unit A ↪ Sym(A).

**Constructive form.** The coproduct of the cofree cocommutative coalgebra is the
partition formula [ESTABLISHED, e.g. Melliès 2009]:

Δ(x_1⋯x_n) = Σ_{S ⊆ [n]} x_S ⊗ x_{[n]\S},  x_S = ∏_{i∈S} x_i;

the digging δ_A iterates it into ordered partitions (P_1 | ⋯ | P_k) of [n]:

δ_A(x_1⋯x_n) = Σ_{(P_1|⋯|P_k)} (∏_{i∈P_1} x_i) ⊗ ⋯ ⊗ (∏_{i∈P_k} x_i).

**Verification of the three comonad equations** [STANDARD, verified for the record]:
- ε∘δ law 1: ε_{Sym(A)}∘δ_A = id — projecting the outermost block structure to
  single-block partitions recovers the input.
- ε∘δ law 2: Sym(ε_A)∘δ_A = id — ε_A kills every block of size ≠ 1; the surviving
  term is the single-block partition of singleton blocks.
- Coassociativity (the "digging rule" δ_{!A}∘δ_A = !δ_A∘δ_A): both sides refine a
  partition into sub-partitions; iterated partitions are partitions. ✓

The exterior case: Δ_Λ(a_1∧⋯∧a_n) = Σ_{S⊆[n]} ±(shuffle) a_S ⊗ a_{[n]\S} with the
Koszul sign of the (S, [n]\S) shuffle; coassociative and cocommutative **in the
graded sense** (Δ = σ∘Δ for the graded flip σ). Same three equations hold; the
adjunction Λ ⊣ U_{grCAlg} (free graded-commutative algebra) provides them. ✓

### 1.2 Contraction and weakening

c_A = Δ (deconcatenation), w_A = projection to degree 0. (Cocommutative,
coassociative, counital — the comonoid structure of the exponential.) ✓ [STANDARD]

### 1.3 Seely isomorphism

Sym(A⊕B) ≅ Sym(A)⊗Sym(B) (polynomial ring in disjoint variables). ✓
Λ(A⊕B) ≅ Λ(A)⊗̂ Λ(B) (exterior algebra of a direct sum is the graded tensor
product). ✓ [ESTABLISHED — Seely 1989 for the linear-logic reading.]

### 1.4 Promotion

For a coalgebra C and linear f : C → A, the promotion f^† : C → Sym(A) is the
unique coalgebra morphism extending f — exactly the cofree property (the
linear-logic !-introduction rule). Same for Λ. ✓ [STANDARD]

**T1 verdict: both !_S and !_Λ are legitimate exponentials of (differential)
linear logic — dereliction, digging, promotion, contraction, weakening, Seely all
verified.** [PROJECT — first explicit verification for this program.]

### 1.5 The parity identification (the core of T1)

Define the **graded** symmetric algebra Sym_gr(A) = ⊕ (A^⊗n)_{σ}^{S_n}, where S_n
acts through the graded braiding (permutations with Koszul signs). Then:
- A even: Sym_gr(A) = Sym(A). [STANDARD]
- **A odd: Sym_gr(A) ≅ Λ(A).** Proof: the graded flip on a⊗a is -1, so the
  symmetrizer (1+σ)/2 kills a⊗a, i.e. a·a = 0 in Sym_gr; the defining relations
  for odd generators are a∧b = -b∧a and a∧a = 0 — precisely the exterior
  relations. [ESTABLISHED superalgebra; this is the Koszul sign rule.]

**Consequence [PROJECT]:** the two exponentials are the two branches of ONE
construction — the free commutative algebra in the graded category — evaluated at
A even (braiding sign +1 on A⊗A) and A odd (braiding sign -1). The boson/fermion
split is the parity of the mark, i.e. the value of the braiding on A⊗A. The
monograph's silent adoption of the symmetric algebra (paper §4) is the silent
adoption of "A even."

### 1.6 Exchange projectors

On A⊗A, P = σ_{A,A} with P² = 1; the projectors are P_sym = (1+P)/2 (range = the
+1 eigenspace) and P_asym = (1-P)/2 (range = the -1 eigenspace). For **A odd**,
P(a⊗b) = -b⊗a, hence:
- (1+P)/2 · (a⊗b) = (a⊗b - b⊗a)/2 → the **+1** eigenspace is span{a⊗b - b⊗a} = Λ²(A);
- (1-P)/2 · (a⊗b) = (a⊗b + b⊗a)/2 → the **-1** eigenspace is span{a⊗b + b⊗a} = S²(A).
So for an odd mark the projector built from (1+P) lands on the **exterior** square
and the projector built from (1-P) lands on the **symmetric** square — the
projector *names* and their *ranges* are parity-swapped relative to the even
case. The parity of the mark decides which eigenspace is which; T4 toy-model
verified the even (unmarked-flip) case at matrix level: idempotence/complement/
orthogonality all True, eigenvalues ±1 emerged from P alone. [The T4 notebook's
"2-token" block corresponds to A even; the odd-mark swap above is the graded
case and is the correct reading for the fermionic mark.]

## 2. T2 — braiding of two marks and the ribbon identity

Setup: compact closed (rigid) category [Kassel 1995]. The mark M is required to be
**self-dual** (M ≅ M*). [POSTULATE P1 — recorded.]

### 2.1 The scalar-braid gap (sharpening of the paper's sketch)

The sketch says "the exchange map σ_{M,M} is a scalar η·id." That does **not**
follow from M simple: End(M) = C·id constrains endomorphisms of M, not of M⊗M.
What forces σ_{M,M} = η·id is **M abelian: M⊗M ≅ simple object** (a single fusion
channel — the pair has one joint state up to phase). [FINDING — the paper's §5
T2 sketch under-specifies this postulate; the honest postulate set must include
"abelian pair."] Example where it holds: in Vect^Z2_C, the odd line L = C^{0|1}
has L⊗L ≅ C^{1|0} (even line), so σ_{L,L} = -id — the fermion sign. ✓

### 2.2 Ribbon identity ⇒ twist = exchange phase

In a ribbon category, the twist of M is

θ_M = (ev_M ⊗ id_M)(id_{M*} ⊗ c_{M,M})(coev_M ⊗ id_M)

[ESTABLISHED — Joyal–Street 1993, Shum 1994]. With c_{M,M} = η·id_{M⊗M}, the
duality equations give **θ_M = η·id_M**: the twist (topological spin) equals the
exchange phase. ✓ This is the categorical spin–statistics relation
R = e^{2πis} at the level of the mark.

### 2.3 Symmetry forces η = ±1

In a **symmetric** monoidal category c² = 1, so η² = 1, η = ±1 — boson/fermion.
In a merely braided category η is free — anyons. [ESTABLISHED; reproduces the
paper's §3 dimensional table and the T4 3D-collapse / 2D-anyon checks.]

### 2.4 The mark-calculus reading

η = +1 ↔ Calling (idempotence: (+)² = +); η = -1 ↔ Crossing (involution:
(-1)² = +1 — the boundary crossed twice returns to the unmarked state). The sign
η = e^{iπ} is the monograph's half-turn phase. [This is a structural READING, not
a derivation — labeled as such in the paper §5; repeated here to keep the
register honest.]

## 3. n-particle characters (P3 / F2 sharpening)

**Claim.** If the exchange of any pair acts by a scalar, the admissible
S_n-representations are exactly the trivial and sign characters.

**Step 1 — Yang–Baxter forces uniformity [PROJECT derivation].** Let σ_i act by
η_i. The braid relation σ_1σ_2σ_1 = σ_2σ_1σ_2 acting on the joint state gives
η_1²η_2 = η_2²η_1, i.e. η_1η_2(η_1 - η_2) = 0; since η_i ≠ 0, **η_1 = η_2**.
Uniformity of the exchange phase across all pairs is not an extra postulate — it
is the Yang–Baxter equation. (T4 verified the matrix-level Yang–Baxter identity.)

**Step 2 — 3D collapse.** σ_i² = 1 ⇒ η² = 1 ⇒ η = ±1.

**Step 3 — only two characters.** A representation with σ_i ↦ η·id for all i is
the homomorphism S_n → {±1}, σ ↦ η^{ℓ(σ)} — the trivial character (η = +1) or
the sign character (η = -1). Any mixed Young symmetry would require pair
exchanges with non-uniform or non-scalar phases — excluded.

**The residual postulate.** Step 1 needs the pair exchange to be a scalar at all
— the **abelian-pair postulate** of §2.1. Without it, mixed symmetries
(parastatistics-class sectors) are not excluded. [FINDING — see §4.]

## 4. The FQ2 verdict — what is the minimal extra structure?

The registry asks whether the minimal extra structure is *exactly* Lorentz +
microcausality. The check gives a precise, two-half answer:

| Half | What is derived | Minimal extra postulates |
|---|---|---|
| Statistics (two eigenvalues) | ±1 phases, two characters | compact closure, **self-duality (P1)**, **abelian pair (P2)**, symmetric braiding (3D) |
| Spin–statistics connection (which eigenvalue ↔ which spin) | η = (-1)^{2s} | Lorentz (twist = 2π rotation of a Lorentz rep), microcausality, positive energy |

[FINDING] **The paper's §5 boundary statement needs one sharpening:** deriving
*statistics* does not require Lorentz, but it does require the abelian-pair
postulate, which in the physical setting is supplied by locality itself: in
3+1D, parastatistics is excluded by the Doplicher–Haag–Roberts analysis of
superselection sectors, and para-sectors reduce to ordinary boson/fermion
sectors with hidden multiplicity [Doplicher–Haag–Roberts 1971/1974;
Greenberg–Messiah 1965]. A purely mark-calculus derivation must therefore
either add the abelian-pair postulate or derive its own DHR-style exclusion —
which again lands on locality/microcausality. The boundary is real; it is one
postulate wider than the paper states.

**F2 consequence.** The pre-registered F2 ("from distinction + compact closure +
involutive braiding ALONE") is satisfied **if and only if** the abelian-pair
postulate is added to the admitted set. Without it, F2 would be disconfirmed by
the mere possibility of parastatistics-class sectors. Recommendation: amend the
registry's P3 postulate list to {distinction, compact closure, involutive
braiding, abelian pair} and re-state F2 accordingly in the next paper version.

## 5. Disconfirmation conditions (this artifact)

- If the braid relation did not force η_1 = η_2 (i.e., non-uniform scalar phases
  satisfy Yang–Baxter), Step 1 fails. [Verified: it forces uniformity.]
- If Λ(A⊕B) ≇ Λ(A)⊗̂Λ(B) or Sym(A⊕B) ≇ Sym(A)⊗Sym(B), the Seely step fails.
  [Verified: both hold.]
- If θ_M ≠ η·id_M under the ribbon identity, the twist-exchange link fails.
  [Verified: equality holds for abelian M.]

## References (notebook-level; verify against originals at publication)

- Spencer-Brown, G. (1969). Laws of Form. George Allen and Unwin.
- Joyal, A., Street, R. (1993). Braided tensor categories. Advances in Mathematics 102, 20–78.
- Shum, M.-C. (1994). Tortile tensor categories. Journal of Pure and Applied Algebra 93.
- Kassel, C. (1995). Quantum Groups. GTM 155, Springer.
- Seely, R. A. G. (1989). Linear logic, *-autonomous categories and cofree coalgebras. AMS Categories in CS and Logic.
- Melliès, P.-A. (2009). Categorical semantics of linear logic. Panoramas et Synthèses 27.
- Ehrhard, T., Regnier, L. (2003). The differential lambda-calculus. Theoretical Computer Science 309.
- Doplicher, S., Haag, R., Roberts, J. E. (1971/1974). Local observables and particle statistics I/II. Commun. Math. Phys. 23, 199–230 / 35, 49–85.
- Messiah, A. M. L., Greenberg, O. W. (1964). Symmetrization postulate and its experimental foundation. Physical Review 136, B248.
- Greenberg, O. W., Messiah, A. M. L. (1965). Selection rules for parafields and the absence of para particles in nature. Physical Review 138, B1155.
- Quni-Gudzinas, R. B. (2026). The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant. doi:10.5281/zenodo.21938971.
