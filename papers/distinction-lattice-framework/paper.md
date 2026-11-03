---
title: "Distinction-Lattice Framework: Eigenforms, Bisimulation, and the Realizability Boundary of Self-Reference"
author: "Rowan Brad Quni-Gudzinas"
date: 2026-09-26
abstract: |
  A conservative formal version of the Distinction-Lattice Framework (DLF):
  stable entities are bisimulation classes of observational behaviour, certified
  coinductively, with realizability separated from fixed-point existence. This
  version (v0.2.0, superseding v0.1.1) narrows novelty claims, corrects the
  JPCUB/Landauer bridge, and records the QNFO archive as not yet assigned.
keywords:
  - distinction
  - realizability
  - bisimulation
  - coalgebra
  - eigenform
  - fixed point
  - self-reference
  - Lawvere diagonal argument
---

# Distinction-Lattice Framework: Eigenforms, Bisimulation, and the Realizability Boundary of Self-Reference

## Abstract

A conservative formal version of the Distinction-Lattice Framework (DLF): stable entities are bisimulation classes of observational behaviour, certified coinductively, with realizability separated from fixed-point existence. This version (v0.2.0, superseding v0.1.1) narrows novelty claims, corrects the JPCUB/Landauer bridge, and records the QNFO archive as not yet assigned.

# 1. Scope and Status

This document is the formal statement of the Distinction-Lattice Framework (DLF),
and it is deliberately conservative. It makes one structural proposal, one
definitional commitment, and one conjecture with explicit falsification
conditions. It does not claim a solved theorem where a conjecture stands, and it
does not bridge to physical claims beyond what the referenced programs
independently support.

The central proposal is this: **distinction precedes number, behavior precedes
proof, and the Lawvere diagonal is the invariant boundary of all self-referential
notation.** The framework's technical content is the formalization of that
sentence.

# 2. The Substrate: Distinctions and the Realizability Filter

Let the primitive act be not the element $x \in S$ but the **distinction**
$\delta = (A \mid A^{\complement})$: a partition of a state space $S$ into what
an observer can tell apart and what it cannot.

**Definition (Distinction).** Let $\mathcal{S}$ be a state space. A distinction
on $\mathcal{S}$ is an equivalence relation $\sim$ on $\mathcal{S}$; the class of
$A$ under $\sim$ is what the distinction counts as *the same*, and its complement
is what the distinction counts as *other*.

**Definition (Realizability filter).** Let $R \subseteq \mathcal{P}(\mathcal{S})$
be a family of subsets that is closed upward (if $A \in R$ and $A \subseteq B$
then $B \in R$) and closed under finite intersection (if $A, B \in R$ then
$A \cap B \in R$). Call $R$ a **realizability filter**. A distinction $\delta$ is
$R$-realized when its realized side lies in $R$.

The filter is the framework's definitional commitment (axiom D5 in the program's
internal numbering): *a distinction is real if it can be the output of an
observation.* Closure under finite intersection is the formal shape of
"observations compose"; upward closure is the shape of "if something is
observable, anything it entails is at least as observable."

# 3. Stable Entities as Bisimulation Classes

The DLF identifies *entity* with *stable observational behavior*.

**Definition (Behavioral functor).** Let $F$ be an endofunctor on a category of
states and observations, with the intended reading that an $F$-coalgebra
$\delta \to F\delta$ is one step of observed behavior from a distinction.

**Definition (Realizability as behavioral fixed point).** A distinction $\delta$
is realized, written $R(\delta)$, if and only if $\delta$ is a fixed point of the
behavioral functor $F$ **up to bisimulation**:

$$R(\delta) \iff \delta \text{ is } F\text{-bisimilar to } F\delta .$$

**Proposition (Lambek).** If $F$ admits a final coalgebra, then the final
coalgebra $\Omega$ satisfies $\Omega \cong F\Omega$ (Lambek's lemma). The space
$\Omega$ is then the space of all observable behaviors; every realized
distinction is, up to bisimulation, a point of $\Omega$.

Consequently, a stable entity is a **bisimulation class** of observational
behavior — an equivalence class of states that no observation within the filter
can separate. The framework's structural claim is that this is what "being the
same thing" means operationally, and that set-theoretic identity is the special
case in which the filter is total.

# 4. Eigenforms: Objects as Fixed Points of Their Own Observation

Kauffman's eigenform formulation reads an object as a solution of

$$x = F(x),$$

where $F$ is the operation of the object's own observation (Kauffman,
arXiv:1102.2048). The DLF adopts this reading and places it in the coalgebraic
setting of Section 3: an eigenform is a fixed point of the behavioral functor,
and the final coalgebra $\Omega \cong F\Omega$ is the universal eigenform.

The framework does not claim priority over the eigenform concept; it claims only
the specific reading that *bisimulation up to the realizability filter* is the
correct notion of solution for self-referential equations. The novelty statement
is correspondingly narrow: the contribution is the filter, not the fixed-point
equation.

# 5. The Self-Reference Boundary: The Lawvere Diagonal

Lawvere's diagonal argument shows, in categorical form, that a cartesian closed
category with an object $A$ admitting a fixed point for every endomap of $A$
cannot contain a surjective map $A \to Y^A$ (Lawvere, "Diagonal arguments and
cartesian closed categories"). Every self-referential construction — from
Cantor's theorem to Goedel-type incompleteness to fixed-point combinators — is a
special case of this diagonal.

The DLF's reading: self-referential notation always asks for a fixed point of an
endomap built from the notation itself. The diagonal is therefore the **invariant
boundary of self-referential notation**: where a notation can name itself, the
Lawvere diagonal delimits what that naming can achieve.

# 6. The Central Separation: Realizability Is Not Fixed-Point Existence

The framework's central conjecture separates two notions that are routinely
conflated:

> **Conjecture (Realizability boundary).** Fixed-point existence does not imply
> realizability. There exist distinctions $\delta$ such that the equation
> $\delta \cong F\delta$ has solutions in the ambient category, yet no solution
> lies in the realizability filter $R$ — and, conversely, there exist filters for
> which every realizable fixed point is a bisimulation class of the final
> coalgebra.

Falsification conditions (any one of these refutes the conjecture):

1. Exhibit a realizability filter $R$, a behavioral functor $F$ with a final
   coalgebra, and a fixed point $\delta \cong F\delta$ such that $\delta \in R$
   but $\delta$ is not a bisimulation class of $\Omega$.
2. Show that for every filter closed upward and under finite intersection, every
   fixed point is realized — i.e., that the filter never cuts.
3. Show that the diagonal boundary collapses: construct a notation that names
   itself through the Lawvere diagonal without leaving $R$.

The conjecture is falsifiable, and the author does not currently know whether it
holds in full generality; the framework's value is that it forces the question
into a form where the answer is checkable.

# 7. The JPCUB/Landauer Bridge (Corrected)

The program's thermodynamic bridge (internal reference QNFO.JPC.003) states a
falsifiable connection between the realizability filter and the Landauer bound:
*the minimal cost of realizing a distinction is bounded below by the information
the filter must discard.* Version v0.1.1 corrected this bridge: it is **not**
established that the filter's cost saturates the Landauer bound, and the bridge
is a conjecture to be tested against the JPCUB program's measurements, not a
derived result of this framework.

# 8. Open Problems

1. Find a natural class of categories and functors for which Conjecture 6 holds
   with proof (the author's current candidate: accessible categories with
   finitary behavioral functors).
2. Characterize the realizability filters that correspond to physical
   observations (which upward-closed, intersection-closed families arise from
   actual measurement apparatus?).
3. Sharpen the JPCUB/Landauer bridge into an inequality with explicit constants.
4. Determine whether the realizability boundary is computable: given $F$, $R$,
   and $\delta$, is $R(\delta)$ decidable?

# 9. References

- Kauffman, L. H. *Eigenform.* arXiv:1102.2048.
- Lambek, J. *A fixpoint theorem for complete categories.* Mathematische
  Zeitschrift 103 (1968) 151–161.
- Lawvere, F. W. *Diagonal arguments and cartesian closed categories.* In:
  Category Theory, Homology Theory and their Applications II, Lecture Notes in
  Mathematics 92 (1969), Springer, 134–145.
- QNFO.JPC.003 — internal program reference for the Landauer-bound bridge
  (conjectural, per Section 7).
