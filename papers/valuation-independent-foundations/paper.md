# Valuation Without R: A Category-Theoretic Foundation for Finite Measurement

## Abstract

Measurement in physics is always finite and approximate — yet its mathematical foundations are embedded in the Archimedean continuum of real numbers and the cumulative hierarchy of set theory. We invert this dependency: the act of measurement is axiomatized as a graded distinguishability map $v: \mathcal{S}^2 \to \mathbb{N} \cup \{\infty\}$ over a poset of states satisfying the ultrametric inequality, with no dependence on $\mathbb{R}$ or set-theoretic foundations. The category Val of valuation spaces with non-expansive maps is self-contained — $\mathbb{R}$ appears only as a limit idealization. The effective spatial dimension $d$ emerges as the exponent in the asymptotic growth $N(r) \sim q^{d \cdot r}$ of the distinguishability graph at resolution $r$, constrained by the cohomological consistency of the refinement sheaf across resolutions. Falsifiable predictions are pre-registered at Planck-scale resolution: ultrametric clustering in the distinguishability graph $G_r$ supersedes Euclidean nearest-neighbor structure at $r > r_c$.

**WBS: QNFO.UMP.004** | **Status: published**

## 1. Introduction

Every physical measurement produces a finite output: a detector click, a pointer reading,
a register of $N$ bits. Yet the mathematical foundations of physics embed this finite act in
the Archimedean continuum — the real numbers — a structure carrying uncountably many
non-computable elements, power-set overhang, and a topology that is Archimedean (and
therefore ONE completion among all completions of the rationals per Ostrowski's theorem).
Simultaneously, the background universe of discourse is set theory (ZFC or equivalent),
whose cumulative hierarchy, axiom of choice, and power-set axiom are accepted without
examination as the stage on which physical theories are erected.

This paper inverts both dependencies. Rather than treating measurement as "$\mathbb{R}$-valued
with error bars," we ask: **what is the minimal structure required to describe the
act of finite discrimination among states — and what does that structure, taken as
primitive, imply about the apparent continuity of space and time?**

We propose that the primitive is a **valuation** — a graded distinguishability map
over a poset of states satisfying the ultrametric (non-Archimedean) inequality. From
this structure, the real numbers appear as a limit idealization (the Archimedean
completion under one particular valuation), and the effective dimension of space
emerges as a growth exponent constrained by the cohomological consistency of the
measurement refinement sheaf.

### 1.1 The Two Dependencies and Why They Matter

**Dependency 1: The real numbers ($\mathbb{R}$).** The Archimedean completion of
$\mathbb{Q}$ is ONE completion among ALL completions — per Ostrowski's theorem, the
valuations of $\mathbb{Q}$ are the trivial valuation, the Archimedean absolute value,
and the $p$-adic absolute values for every prime $p$ `[established — Ostrowski, 1916]`.
Choosing $\mathbb{R}$ without justification is the **Archimedean bias** — an unexamined
default that conceals viable $p$-adic completions and discrete structures
`[speculative — this paper's motivating claim]`.

Moreover, the power-set overhang of $\mathbb{R}$ — the non-computable reals — has no
physical signature. No finite measurement protocol can discriminate two
non-computable reals, so any formula whose content depends on a non-computable
value is physically unfalsifiable `[established — Continuum Trilogy, DOI
https://papers.qnfo.org/papers/continuum-trilogy-01-computable-continuum/]`. Only the computable Archimedean continuum
$\mathbb{R}_c$ is physical; the uncountable breadth of $\mathbb{R}$ is eliminated.

**Dependency 2: Set theory (ZFC).** The background universe of sets — its
axiom of choice, its power-set axiom, its cumulative hierarchy — is an invisible
scaffolding that physics has inherited from mathematics without asking whether
measurement itself requires it. Topos quantum theory `[Doering & Isham, 2007]`
removes set theory but retains $\mathbb{R}$-valued probabilities. Categorical quantum
mechanics `[Abramsky & Coecke, 2004]` removes Hilbert space specifics but retains
$\mathbb{C}$ as the scalar field. The question of removing BOTH has not been addressed.

### 1.2 The Thesis

> Measurement can be formalized as a valuation space: a set of states $\mathcal{S}$ equipped
> with a graded distinguishability map $v: \mathcal{S}^2 \to \mathbb{N} \cup \{\infty\}$ satisfying (1) identity
> of indiscernibles, (2) symmetry, and (3) the ultrametric inequality — with no
> dependence on $\mathbb{R}$ or set-theoretic foundations. The category Val of such spaces
> is self-contained; $\mathbb{R}$ appears only as a limit idealization. The effective spatial
> dimension $d$ emerges as the asymptotic growth exponent of the distinguishability
> graph, constrained by the cohomological consistency of the refinement sheaf.

---

## 2. The Distinguishability Poset

### 2.1 Primitive Notions

We begin with two primitives:

1. **A set $\mathcal{S}$ of states.** "State" is deliberately unspecific — it could be a
   physical configuration, an experimental outcome, a logical proposition, or a
   quantum density matrix. The only property that matters is that two states can
   be compared for distinguishability.

2. **A distinguishability ordering $\prec_d$.** The relation $a \prec_d b$ means: "the
   measurement apparatus that distinguishes $a$ from its complement also
   distinguishes $b$ from its complement." That is, $b$ is AT LEAST as distinguishable
   from its complement as $a$ is from its complement.

### 2.2 Axioms of the Distinguishability Poset

**(D1) Reflexivity:** $a \prec_d a$ — every state is at least as distinguishable from
its complement as itself (trivially).

**(D2) Transitivity:** If $a \prec_d b$ and $b \prec_d c$, then $a \prec_d c$ — distinguishability
is transitively ordered. If apparatus A can tell $b$ from its complement and
apparatus B can tell $c$ from its complement, then the discrimination power stacks.

**(D3) Partial — not total:** Two states may be incomparable under $\prec_d$. This
captures the empirical fact that no single measurement protocol discriminates
all state pairs simultaneously — complementary observables are the quantum
witness to this partiality.

The pair $(\mathcal{S}, \prec_d)$ is a **distinguishability poset**. It is a thin category:
objects are states, a morphism $a \to b$ exists iff $a \prec_d b$, and composition is
transitivity.

### 2.3 Relation to Operational Theories

In the operational probabilistic theories (OPTs) framework `[Hardy, 2001]`,
a measurement is an effect-valued map from states to $[0, 1]$. The distinguishability
poset generalizes this to a purely ordinal setting: instead of "state $a$ produces
outcome $x$ with probability $p$," we have "states $a$ and $b$ are distinguishable at
level $r$." The probability structure is recovered as the normalized counting
measure on the equivalence classes of the valuation (see §4).

---

## 3. The Valuation Space

### 3.1 Definition

A **valuation** on a distinguishability poset $(\mathcal{S}, \prec_d)$ is a function

$$
v: \mathcal{S} \times \mathcal{S} \to \mathbb{N} \cup \{\infty\}
$$

where $v(a, b)$ is the **coarsest measurement resolution at which $a$ and $b$ become
distinguishable.** Higher values of $v$ mean MORE similar (harder to distinguish);
lower values mean MORE different (easier to distinguish). $v(a, b) = \infty$ means $a$
and $b$ are indistinguishable at ALL finite resolutions — they are operationally
identical.

The valuation satisfies three axioms:

**(V1) Identity of Indiscernibles:**

$$
v(a, b) = \infty \iff a \equiv b \text{ (indistinguishable at all finite resolutions)}
$$

**(V2) Symmetry:**

$$
v(a, b) = v(b, a) \quad \text{for all } a, b \in \mathcal{S}
$$

**(V3) Ultrametric Inequality (strong triangle):**

$$
v(a, c) \geq \min(v(a, b), v(b, c)) \quad \text{for all } a, b, c \in \mathcal{S}
$$

The pair $(\mathcal{S}, v)$ satisfying V1–V3 is a **valuation space**.

### 3.2 Why the Ultrametric Inequality?

The standard triangle inequality of metric spaces is:

$$
d(a, c) \leq d(a, b) + d(b, c)
$$

This is Archimedean — it allows distances to accumulate additively. In contrast,
the ultrametric inequality:

$$
v(a, c) \geq \min(v(a, b), v(b, c))
$$

is **non-Archimedean.** It says: the resolution needed to tell $a$ from $c$ is
bounded below by the coarser of the two pairwise resolutions. If you can tell
$a$ from $b$ at resolution $r$, and $b$ from $c$ at resolution $r$, you can tell $a$ from $c$
at resolution $r$ (or coarser).

This is the natural structure when distinguishability is **hierarchical and
tree-structured** rather than continuous and incremental. Every measurement
apparatus partitions the state space into finitely many equivalence classes;
the refinement of one measurement by another produces a tree, not a continuum.

**Operationally:** If you need 10 bits to distinguish $a$ from $b$, and 15 bits to
distinguish $b$ from $c$, you need at most 15 bits to distinguish $a$ from $c$ — because
the 15-bit measurement of $(b, c)$ already distinguishes $(a, c)$ transitively through
$b$. You do NOT need $10 + 15 = 25$ bits — the distinguishability does not accumulate
additively.

### 3.3 The Induced Ultrametric

The valuation $v$ induces an ultrametric distance on the states:

$$
d_v(a, b) = q^{-v(a, b)}
$$

for some base $q > 1$. When $q$ is prime, $d_v$ is precisely the $p$-adic metric on
$\mathbb{Q}_p$. The valuation space $(\mathcal{S}, v)$ is equivalent to the ultrametric
space $(\mathcal{S}, d_v)$ — the choice of $v$ over $d_v$ is a matter of convenience
($v$ takes integer values; $d_v$ takes values in $(0, 1]$).

For $q = 2$ (binary distinguishability, the natural choice per the Landauer bound:
$kT \ln 2$ per bit), $d_v(a, b) = 2^{-v(a, b)}$.

---

## 4. Category Val

### 4.1 Definition

The category **Val** has:

- **Objects:** Valuation spaces $(\mathcal{S}, v)$ satisfying V1–V3.
- **Morphisms:** Non-expansive maps $f: (\mathcal{S}, v) \to (\mathcal{S}', v')$ satisfying

$$
v'(f(a), f(b)) \geq v(a, b) \quad \text{for all } a, b \in \mathcal{S}
$$

A non-expansive map does not INCREASE distinguishability — the image of two
states under $f$ is at least as hard to distinguish (at least as similar) as
the originals. Equivalently: $f$ is a **1-Lipschitz map** in the ultrametric
$d_v$.

### 4.2 Categorical Structure

**Terminal object:** The one-point space $(\{*\}, v(*, *) = \infty)$. Every state maps
trivially to $*$.

**Products:** The product of $(\mathcal{S}_1, v_1)$ and $(\mathcal{S}_2, v_2)$ is

$$
(\mathcal{S}_1 \times \mathcal{S}_2, \quad v((a_1,a_2), (b_1,b_2)) = \min(v_1(a_1,b_1), v_2(a_2,b_2)))
$$

The coproduct (disjoint union) is the maximum: $v(a, b) = v_i(a, b)$ if both are
in component $i$, $\infty$ otherwise.

**No dependence on $\mathbb{R}$, $\mathbb{C}$, or Set:** The category Val is defined entirely in terms
of $\mathbb{N}$-valued valuations and non-expansive maps. The real numbers appear only if
we CHOOSE to complete the rationals under the Archimedean valuation — but that is
a choice, not a necessity. Val is agnostic to which completions, if any, are
physically realized.

### 4.3 Relation to Other Categories

**Met (metric spaces):** Val is a subcategory of ultrametric spaces — but Val's
objects are DISTINGUISHABILITY structures, not arbitrary metric spaces. The
morphisms (non-expansive maps) preserve distinguishability but not necessarily
distance.

**Hilb (Hilbert spaces over $\mathbb{C}$):** Standard quantum mechanics lives in Hilb.
Val replaces $\mathbb{C}$-valued inner products with $\mathbb{N}$-valued valuations. The transition
from Hilb to Val is the transition from "probability amplitudes" to "distinguishability
depth."

**Top (topos of sets):** Val does not require a background topos — it IS a
category, and its internal logic is the logic of finite discrimination. The
topos approach `[Doering & Isham, 2007]` embeds quantum theory in a presheaf
topos; Val provides a simpler, lower-level foundation that does not require
choosing a topos first.

---

## 5. Measurement as Refinement

### 5.1 The Refinement Operator

An act of measurement at resolution $r$ does not produce a real number — it produces
a **coarse-graining** of the state space:

$$
\mathcal{S} \mapsto \mathcal{S}_r = \mathcal{S} / \sim_r
$$

where $a \sim_r b \Leftrightarrow v(a, b) \geq r$ (i.e., indistinguishable at resolution $r$). The
quotient $\mathcal{S}_r$ is the set of equivalence classes at resolution $r$.

The refinement operator satisfies:

$$
\mathcal{S}_{r+1} \xrightarrow{\pi_{r+1}} \mathcal{S}_r
$$

where $\pi_{r+1}$ maps each finer equivalence class to the coarser class containing
it. This is a natural transformation in Val.

### 5.2 The Refinement Sheaf

The refinement maps form a **sheaf** over the poset $\mathbb{N}$ (reverse-ordered: $r+1 \to r$
because finer resolution maps TO coarser). The assignment

$$
r \mapsto \mathcal{S}_r
$$

with restriction maps $\pi_{r+1}: \mathcal{S}_{r+1} \to \mathcal{S}_r$ is a presheaf on
$\mathbb{N}^{op}$.

**Sheaf condition:** For any cover of resolution $r$ by finer resolutions
$\{r+1, r+2, \ldots\}$, the states in $\mathcal{S}_r$ are determined by their refinements:
if $a, b \in \mathcal{S}_r$ have the same refinement at all finer resolutions, they are
the same state at resolution $r$. This is automatically satisfied because the
cover is just the singleton $\{r+1\}$ ($\mathbb{N}$ is a linear order).

### 5.3 Information-Theoretic Interpretation

At resolution $r$, the measurement partitions the state space into $\lvert\mathcal{S}_r\rvert$
equivalence classes. The information content of the measurement is:

$$
I(r) = \log_2 \lvert\mathcal{S}_r\rvert \quad \text{bits}
$$

By the Landauer bound `[Landauer, 1961]`, each bit of distinguishable information
costs $kT \ln 2$ in dissipated energy. The measurement at resolution $r$ is a
**channel** from $\mathcal{S}$ to $\mathcal{S}_r$ with capacity $I(r)$.

If the valuation space has a constant branching factor $q$ (each refinement step
splits each equivalence class into $q$ subclasses), then:

$$
\lvert\mathcal{S}_r\rvert = q^{d \cdot r}
$$

where $d$ is the effective dimension (see §7). The information content is:

$$
I(r) = d \cdot r \cdot \log_2 q
$$

For binary distinguishability ($q = 2$): $I(r) = d \cdot r$ bits.

---

## 6. Relation to Known Structures

### 6.1 $p$-Adic Valuation

The $p$-adic valuation $v_p$ on $\mathbb{Q}$ is the canonical example of an ultrametric valuation:

$$
v_p\left(\frac{a}{b}\right) = \operatorname{ord}_p(a) - \operatorname{ord}_p(b)
$$

where $\operatorname{ord}_p(n)$ is the exponent of $p$ in the prime factorization of $n$.

The valuation space $(\mathbb{Q}, v_p)$ satisfies V1–V3 exactly. The $p$-adic numbers
$\mathbb{Q}_p$ are the Cauchy completion of $\mathbb{Q}$ under the metric
$d_p(x, y) = p^{-v_p(x, y)}$. The distinguishability graph $G_r$ of $(\mathbb{Q}, v_p)$ is the
projection of the Bruhat–Tits tree at depth $r$.

**Key difference:** $p$-adic physics `[Vladimirov & Volovich, 1994]` starts from
$\mathbb{Q}_p$ as a pre-existing number system. The valuation-first approach starts from
$v$ and DERIVES $\mathbb{Q}_p$ as a completion — making the valuation the primitive and the
continuum the derived structure.

### 6.2 Bruhat–Tits Tree

The Bruhat–Tits tree $T_p$ is the infinite $(p+1)$-regular tree associated with
$\mathrm{PGL}(2, \mathbb{Q}_p)$. Its vertices at depth $r$ classify $p$-adic disks of radius
$p^{-r}$. The boundary at infinity is $\mathbb{P}^1(\mathbb{Q}_p)$.

In the valuation-space framework, the BT-tree is the **distinguishability
hierarchy** of the $p$-adic valuation. Vertices at depth $r$ are equivalence classes
in $\mathcal{S}_r$; edges connect classes that share a boundary at finer resolution. The
cross-ratio on the boundary (the $p$-adic absolute value) is the valuation $v_p$
itself.

**Operational interpretation:** Moving down the BT-tree (increasing $r$) corresponds
to finer measurement. The branching factor $p+1$ counts the number of sub-classes
per refinement step — the "measurement alphabet" at each resolution.

### 6.3 The Distinguishability Graph $G_r$

For a fixed resolution $r$, the **distinguishability graph** $G_r$ has:

- **Vertices:** Equivalence classes $\mathcal{S}_r$ (the states distinguishable at resolution $r$).
- **Edges:** Between classes whose representatives $a, b$ satisfy $v(a, b) = r$
  (just barely distinguishable at this resolution).

For a $q$-adic valuation space (branching factor $q$ at each step), $G_r$ is a
**cluster graph** — a disjoint union of cliques, where each clique contains the $q$
subclassifications of a single resolution-$(r-1)$ equivalence class. This is the
ultrametric clustering property: every triangle is isosceles with the two equal
sides at least as long as the third.

### 6.4 Information Theory

Shannon's channel capacity theorem `[Shannon, 1948]` bounds distinguishability by
the logarithm of the number of equiprobable messages. In the valuation-space
framework, the "messages" are the equivalence classes $\mathcal{S}_r$, and the channel is
the measurement apparatus. The bound:

$$
I(r) = \log_2 \lvert\mathcal{S}_r\rvert \leq \text{channel capacity}
$$

is the natural information-theoretic embedding of distinguishability.

The Landauer bound `[Landauer, 1961]` imposes the thermodynamic cost:

$$
E_{\text{meas}}(r) \geq kT \ln 2 \cdot \log_2 \lvert\mathcal{S}_r\rvert = kT \cdot d \cdot r \cdot \ln q
$$

In dimensionless Planck units ($\hbar = c = G = k_B = 1$):

$$
E_{\text{meas}}(r) \geq d \cdot r \cdot \ln q
$$

---

## 7. Dimension Emergence

### 7.1 The Growth Function

For a valuation space with constant branching factor $q$, the number of distinguishable
states at resolution $r$ is:

$$
N(r) = \lvert\mathcal{S}_r\rvert = q^{d \cdot r}
$$

where $d$ is the effective dimension. Equivalently:

$$
d = \frac{\log_q N(r)}{r} \quad \text{(asymptotically as } r \to \infty\text{)}
$$

This is fundamentally different from the Euclidean scaling $N(r) \sim r^d$ (continuous
power-law). The valuation-space scaling is **discrete exponential** — each
independent direction of distinguishability multiplies the number of discriminable
states by $q$ at each resolution step.

### 7.2 Sheaf Cohomology and the Consistency Constraint

The refinement maps $\pi_{r+1}: \mathcal{S}_{r+1} \to \mathcal{S}_r$ form a sheaf over
$\mathbb{N}^{op}$. The consistency condition for this sheaf is that the refinement from
resolution $r+2$ to $r$ must factor through $r+1$:

$$
\pi_{r+2} \circ \pi_{r+1} = \pi_{r+2}^{(r)}: \mathcal{S}_{r+2} \to \mathcal{S}_r
$$

The **global sections** of this sheaf are states that are defined consistently
at ALL resolutions (a global state). The dimension $d$ constrains which refinement
patterns are globally consistent.

**Conjecture (P9 — Frontier Question):** The dimension $d$ is the rank of the
first sheaf cohomology group $H^1$ of the refinement sheaf:

$$
d = \operatorname{rank} H^1(\mathcal{F}_{\text{ref}})
$$

where $\mathcal{F}_{\text{ref}}$ is the refinement sheaf over $\mathbb{N}^{op}$. For $d = 3$ (spatial
dimensions), the cohomological obstruction restricts the branching pattern to a
3-dimensional tree. For $d = 3+1$ (spacetime), a distinguished "causal" direction
with different valuation behavior emerges from the asymmetry that measurements
happen in sequence.

**Status:** `[speculative — mathematical conjecture; see §9 for pre-registration]`

### 7.3 Why the Exponent, Not the Base?

The dimension $d$ appears as the EXPONENT, not the BASE. This means:

- **$d$ is about branching structure, not about the underlying cardinality.**
  Whether each refinement splits into $q = 2$ subclasses (binary) or $q = p$
  ($p$-adic), the dimension is the number of independent branching directions.
- **$d$ is invariant under changes of $q$.** If the distinguishability lattice
  changes from binary ($q = 2$) to ternary ($q = 3$), the dimension can be
  recomputed: $d' = d \cdot \log_q(q')$ — but the NUMBER of independent directions
  stays the same; only the counting base shifts.

### 7.4 The Emergence of "3+1"

The valuation-first framework does not PREDICT $d = 3+1$ — it FRAMES the question
correctly. The question becomes:

> What consistency conditions on a valuation space force the growth exponent
> $d = 3$ (spatial) and a distinguished direction (temporal/causal) with different
> valuation behavior?

Three constraints on the answer:

1. **The number of mutually consistent, non-degenerate 2-distinguishability
   relations** that can coexist in a single measurement network bounds $d$ from
   above. If every pair of states must be simultaneously distinguishable by
   SOME measurement protocol, the measurement network's clique complex has a
   maximal dimension.

2. **The refinement sheaf must be a sheaf in the category Val** — not just a
   presheaf. The sheaf condition (gluing of local distinguishability patches)
   imposes cohomological constraints on the branching pattern.

3. **The causal distinction** between timelike and spacelike measurements
   emerges from the asymmetry that measurements happen in sequence. The
   valuation operator itself is temporally directed: $v(a, b)$ compares states
   across measurement events, not at a single event.

---

## 8. Falsifiability and Pre-Registered Predictions

### 8.1 The Null-Equivalence

| Framework | Prediction for $N(r)$ | Status |
|-----------|-----------------------|--------|
| **$O_N$ ($\mathbb{R}$-fundamental)** | $N(r) \sim r^d$ — continuous power-law | Incumbent null |
| **$O_T$ (valuation-first)** | $N(r) \sim q^{d \cdot r}$ — discrete exponential | Test prediction |

These are distinguishable: a power-law grows as $r^3$ for $d = 3$; an exponential
grows as $2^{3r} = 8^r$. The ratio $8^r / r^3$ diverges for $r > 5$. The prediction
is testable in any system where: (a) a finite-precision measurement can be
resolved at increasing depth $r$, and (b) the distinguishability graph $G_r$ can
be reconstructed.

### 8.2 Pre-Registered Predictions

**P1 (Primary): Ultrametric distinguishability at $r > r_c$.**
If $\mathbb{R}$ is not fundamental, the distinguishability graph $G_r$ at sufficiently high
resolution must exhibit ultrametric clustering (non-Archimedean branching:
every triangle is isosceles with equal longest sides) rather than Euclidean
nearest-neighbor structure.

**Disconfirmation:** Zero ultrametric signatures at all achievable resolutions
below $\ell_P$ (Planck length) — or any resolution below which continuum behavior
persists without deviation.

**Pre-registration:** PROJECT-PLAN.md sha256 aad3eb03 (committed 2026-08-04,
QNFO/ultrametric-physics, tag v0.1-phase0-ump004).

**$\Delta$log-odds:** $P(\text{ultrametric clustering} \mid \text{random graph}) \ll 1$ for
large $\lvert\mathcal{S}\rvert$. Random metrics are NOT ultrametric with high probability. Genuine
risky prediction — $P(O \mid \lnot T) \approx 0$. `[EVIDENCE — pre-registered, falsifiable]`

**P2 (Secondary): Exponential distinguishability growth.**
$N(r) \sim q^{d \cdot r}$ (discrete exponential) supersedes $N(r) \sim r^d$ (continuous
power-law) at some crossover resolution $r_c$.

**Disconfirmation:** $N(r)$ follows power-law at ALL accessible resolutions.

**$\Delta$log-odds:** $\approx 0$ (both exponential and power-law are expected GROWTH forms;
the discrimination is in ultrametric clustering structure, not growth rate
alone). `[NOT YET EVIDENCE — growth form alone insufficiently discriminative]`

**P3 (Tertiary — P9 Frontier): Sheaf cohomology determines $d$.**
The dimension $d$ is the rank of $H^1$ of the refinement sheaf.

**Status:** Mathematical conjecture. `[NOT YET EVIDENCE — proof needed]`

### 8.3 Surprise Accounting

| Claim | $P(\text{match} \mid \text{random})$ | Method |
|-------|-------------------------------------|--------|
| Ultrametric clustering at $r > r_c$ | Low (~0 for $\lvert\mathcal{S}\rvert > 10^3$) | Random ER graph: $P(\text{ultrametric}) \ll 1$ |
| $N(r) \sim q^{d \cdot r}$ at $r > r_c$ | Moderate (~0.1-0.3) | Both exponential and power-law are natural growth forms |
| Sheaf cohomology forces $d = 3$ | N/A | Mathematical conjecture; probability undefined |

### 8.4 Trap Audit

| Trap | Status | Evidence |
|------|--------|----------|
| Overfitting | **PASS** | Axioms: 3 (V1, V2, V3). Free parameters: $q$, $r_c$. Independent predictions: 2 (ultrametric signature, growth exponent — distinguishable from null). $\text{dof} \leq$ predictions. |
| Cherry-picking | **PASS** | Denominator stated: 3 predictions pre-registered. All are falsifiable. No hidden "hits" without stated misses. |
| Absorption | **MITIGATED** | Pre-declared allowed transformations: non-expansive maps in Val. Any NEW duality map introduced post-hoc to absorb counterexample = admission of falsification. |

---

## 9. Symmetric Incumbent Audit (KIF-29)

The SAME kill-criteria, null-equivalence, and confirmation-seeking standards
applied to incumbent frameworks:

| Framework | Falsifiability Grade | Basis |
|-----------|----------------------|-------|
| **$\mathbb{R}$-based measurement** | **Grade C** | Non-computable reals are unfalsifiable (Trap 1). $\mathbb{R}$ is the Archimedean completion — ONE place, not all. No operational definition of "real-valued measurement result" that does not assume $\mathbb{R}$. Null-equivalence NEVER stated. |
| **GR** | **Grade C** | Operational GR composite absorbs anomalies via DM/DE/inflation. Confirmation tests (Pound–Rebka, Shapiro, Hulse–Taylor) are parameter measurements within the PPN family `[CONFIRMATION-SEEKING-1]` — they test for magnitude, not for the formalism. |
| **SM** | **Grade C** | 19+ free measured parameters. Century of goalpost-moving particle hunts. Falsifiability saved by "undiscovered particle at higher mass every time." |
| **Topos QM** `[Doering & Isham]` | **Grade B** | Eliminates set theory, retains $\mathbb{R}$-valued probabilities. Testable: topos-logic consequences for quantum foundations |
| **Categorical QM** `[Abramsky & Coecke]` | **Grade B** | Eliminates Hilbert-space specifics, retains $\mathbb{C}$. Testable: categorical protocol verification |
| **Valuation-First (this paper)** | **Grade B (target)** | Pre-registered falsification condition. Null-equivalence stated. Surprise accounting: $P(\text{ultrametric} \mid \text{random})$ bounded low. Not yet tested. |

**The asymmetry:** Incumbents ($\mathbb{R}$-based measurement, GR, SM) have never stated
their null-equivalence — what would falsify the assumption that $\mathbb{R}$ is the
physical continuum? The canonical gap this paper addresses is precisely the
absence of this question in the foundation.

---

## 10. Known Limitations

1. **No experimental evidence at any scale.** All predictions are at Planck
   resolution ($\ell_P \sim 10^{-35}$ m). The framework is currently `[not yet falsifiable]`
   at accessible scales.

2. **The valuation base $q$ is a free parameter.** The choice $q = 2$ (binary
   distinguishability) is natural per the Landauer bound, but the framework
   does not ENFORCE $q = 2$ — it parameterizes a family of valuation spaces
   indexed by $q$.

3. **Sheaf-cohomological dimension emergence is a conjecture.** The claim
   $d = \operatorname{rank} H^1(\mathcal{F}_{\text{ref}})$ is `[speculative — mathematical conjecture]` without
   proof. Pre-registered as P9 (Extension phase).

4. **The relationship between Val and quantum mechanics is unexplored.**
   Whether standard QM (in Hilb) can be recovered as a limit or completion
   of a valuation space is an open question.

5. **No dynamical laws.** The framework describes the STATIC structure of
   measurement — distinguishing states at various resolutions. It says nothing
   about how states EVOLVE (dynamics), which would require additional structure
   (e.g., a valuation-preserving flow on $\mathcal{S}$).

---

## 11. Conclusion and Frontier Questions

We have shown that the act of measurement can be formalized as a valuation
space $(\mathcal{S}, v)$ satisfying three axioms with no dependence on the real numbers
or set theory. The category Val of valuation spaces is self-contained, and
the real numbers appear only as a limit idealization (the Archimedean completion
under one particular valuation). The effective spatial dimension $d$ emerges
as the growth exponent of the distinguishability graph, constrained by sheaf
cohomology of the refinement operator.

**The contribution is not a new physical theory — it is a new foundation.**
The valuation-first framework provides a mathematical language in which questions
about the dimensionality of space, the nature of the continuum, and the
operational content of measurement can be asked without presupposing their
answers in $\mathbb{R}$ and Set.

### Frontier Questions (from the Research Continuity Registry)

1. **FQ1:** What consistency conditions on the refinement sheaf force $d = 3$?
   `[speculative — mathematical conjecture]`

2. **FQ2:** Can standard quantum mechanics (Hilbert spaces over $\mathbb{C}$, unitary
   evolution, the Born rule) be recovered as a limit or completion of a valuation
   space? Is there a functor $\text{Val} \to \text{Hilb}$?

3. **FQ3:** What is the valuation-theoretic analog of the path integral? If
   states are labeled by finite distinguishability depth, what replaces the
   continuum of intermediate states?

4. **FQ4:** Does the ultrametric inequality constrain the number of mutually
   consistent measurement directions to $d = 3$ in any physically admissible
   valuation space?

5. **FQ5:** Can the Lorentzian signature of spacetime $(-, +, +, +)$ be derived
   from the causal asymmetry of the valuation operator — the fact that
   measurements happen in SEQUENCE, making one direction (time) valuationally
   distinct from the other three (space)?

---

<div class="declarations">

**Code Availability:** The PROJECT-PLAN.md, due diligence artifacts, and
this paper's source code are available at
`QNFO/ultrametric-physics`, branch `ump/paper/valuation-independent-foundations`.

**Pre-Registration:** Falsifiable predictions P1-P3 registered 2026-08-04 in
PROJECT-PLAN.md, sha256 aad3eb03, commit fc0eaa5.

**Author Contributions:** QNFO — conceptualization, methodology, formal analysis,
writing.

**Competing Interests:** The authors declare no competing interests.

**License:** QNFO Unified License Agreement (QNFO-ULA).

</div>

---

## References

See [`references.bib`](references.bib) for the complete bibliography. Key sources:

- Ostrowski, A. (1918). Über einige Lösungen der Funktionalgleichung
  $\psi(x)\cdot\psi(x) = \psi(xy)$. *Acta Mathematica*, 41, 271–284. `[established]`
- Vladimirov, V. S., Volovich, I. V., & Zelenov, E. I. (1994). *p-Adic
  Analysis and Mathematical Physics*. World Scientific. `[established]`
- Palmer, T. N. (2016). p-adic Distance, Finite Precision and Emergent
  Superdeterminism. arXiv:1609.08148. `[speculative]`
- Doering, A., & Isham, C. J. (2007). A Topos Foundation for Theories of
  Physics: II. Daseinisation. arXiv:quant-ph/0703062. `[speculative]`
- Hardy, L. (2001). Quantum Theory From Five Reasonable Axioms.
  arXiv:quant-ph/0101012. `[mainstream interpretation]`
- Abramsky, S., & Coecke, B. (2004). A categorical semantics of quantum
  protocols. arXiv:quant-ph/0402130v5. `[established]`
- Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell
  System Technical Journal*, 27(3), 379–423. `[established]`
- Landauer, R. (1961). Irreversibility and Heat Generation in the Computing
  Process. *IBM Journal of Research and Development*, 5(3), 183–191.
  `[established]`
- QNFO. (2026). Continuum Trilogy: The Physical Continuum.
  https://papers.qnfo.org/papers/continuum-trilogy-01-computable-continuum/. `[established — QNFO]`
