---
title: "Completeness Senses and the Levi-Civita Field: Ordered Non-Archimedean Number Systems Beyond Ostrowski's Classification"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-26"
version: "1.1.1"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "10.5281/zenodo.22109361"
status: "published"
bibliography: references.bib
abstract: |
  Ostrowski's theorem classifies every nontrivial rank-1 absolute value on the rationals: the Archimedean absolute value and, for each prime p, a p-adic absolute value. Their completions are the real numbers and the p-adic fields. This classification is often read as closing the question of what a complete number system can be. It does not. The theorem governs completions of the rationals under multiplicative sizes; it says nothing about ordered field extensions of the reals that carry infinitesimals, about stronger non-Archimedean notions of completeness, or about valuations of higher rank. This paper separates those questions, distinguishes three senses of completeness — Dedekind, Cauchy, and spherical — and exhibits the Levi-Civita field as a genuine counterexample to the claim that the reals are the unique complete ordered field: it is Cauchy-complete, ordered, real-closed, and non-Archimedean at once. The standard decimal identity 0.999... = 1 survives by transfer in every ordered field containing the reals; the divergent case appears only for nonstandard-indexed decimals. Higher-rank valuations occur only in function fields of transcendence degree at least two. The aim is not to displace the reals, which remain the unique Dedekind-complete ordered field, but to make the completeness question precise enough that "the reals are the complete number system" and "there are many complete number systems" can both be stated without equivocation.
---

# Completeness Senses and the Levi-Civita Field: Ordered Non-Archimedean Number Systems Beyond Ostrowski's Classification

The question "which number system is complete?" recurs across the foundations of physics and computation, where the reals are usually taken as the default field for measurement, dynamics, and state spaces. A precise answer requires first disambiguating the word *complete*, which names at least three distinct properties. Once the senses are separated, a family of ordered number systems emerges that the standard classification does not name. One member of that family — the Levi-Civita field — is ordered, complete in a metric sense, real-closed, and non-Archimedean, and therefore serves as a concrete counterexample to the claim that the reals are the unique complete ordered field. The significance is practical as well as structural: any physical theory that needs an ordered field with infinitesimal resolution, or any computation that needs exact arithmetic with a distinguished scale, has an alternative to the Archimedean continuum that is already a field rather than a ring.

## 1. The scope of Ostrowski's theorem

Ostrowski's theorem (1916) classifies every nontrivial absolute value on the rational numbers: it is equivalent either to the Archimedean absolute value or to a p-adic absolute value for some prime p [@ostrowski1916]. Completing the rationals under these absolute values produces the real numbers and the p-adic fields. Two scope limits are frequently overlooked.

First, the theorem concerns *rank-one* valuations — those whose value group embeds into the positive reals. It says nothing about valuations of higher rank, whose value groups are ordered groups of larger dimension.

Second, the theorem concerns *completions of the rationals*. Ordered field extensions of the reals that contain infinitesimals are not completions of the rationals in Ostrowski's sense; they lie entirely outside the classification. The reals themselves are one Archimedean completion; the p-adic fields are non-Archimedean completions; ordered fields with infinitesimals form a third family the theorem never addresses.

## 2. Three senses of completeness

The word *complete* is used for at least three distinct properties, and each assigns a different answer to "which number systems are complete?"

**Dedekind completeness.** Every nonempty set with an upper bound has a least upper bound. Among ordered fields, only the reals are Dedekind complete, and Dedekind completeness implies the Archimedean property. The statement "the reals are the unique Dedekind-complete ordered field" therefore needs no qualifier.

**Cauchy completeness.** Every Cauchy sequence converges. This holds for the reals, every p-adic field, the Levi-Civita field, and the formal Laurent series over the reals. It does not hold for the hyperreals or the surreals. The reals are not unique in this sense.

**Spherical completeness.** A strictly stronger non-Archimedean notion in which every nested sequence of closed balls has nonempty intersection. The p-adic fields, the formal Laurent series over the reals, and Hahn series fields are spherically complete; the reals are not.

| Sense | Definition | Held by | Reals unique? |
|---|---|---|---|
| Dedekind | least-upper-bound property | reals alone among ordered fields | yes, unconditionally |
| Cauchy | every Cauchy sequence converges | reals, every Q_p, Levi-Civita, R((t)) | no |
| Spherical | nested closed balls intersect | Q_p, R((t)), Hahn fields | no |

The reals are unique for Dedekind completeness and for no other sense. Every claim that the reals are "the" complete number system therefore depends on which sense is meant, and the default reading — the Cauchy one — is the sense in which the reals are *not* unique.

## 3. The Levi-Civita field

The Levi-Civita field consists of formal series with real coefficients, rational exponents, and left-finite support: each series has only finitely many terms below any given exponent [@shamseddineberz2003]. It is an ordered field, with the sign of a series determined by its lowest-order coefficient; it is real-closed; it is non-Archimedean, since the element $t$ with unit coefficient at exponent one is positive yet smaller than $1/n$ for every natural number $n$; and it is Cauchy-complete in its natural valuation topology.

The Levi-Civita field is therefore a genuine counterexample to the unqualified claim that the reals are the unique complete ordered field. The reals are the unique *Dedekind*-complete ordered field. They are not the unique *Cauchy*-complete ordered field. The Levi-Civita field keeps everything the reals have — order, field structure, real-closedness, metric completeness — and adds what the reals cannot have: infinitesimal resolution.

## 4. The decimal identity and nonstandard indices

The identity $0.999\ldots = 1$ holds in the reals, and it survives by transfer in every ordered field containing the reals as an ordered subfield [@robinson1966]: the partial sums $1 - 10^{-n}$ converge to $1$ in the order topology of each. The apparent counterexample appears only when the decimal is given *nonstandard indices*. The extension of the sequence $1 - 10^{-n}$ to an infinite hypernatural $H$ equals $1 - 10^{-H}$, which differs from $1$ by a positive infinitesimal [@lightstone1972; @katz2010].

The identity is pinned to the Archimedean place value in a precise sense. The geometric series $\sum_{k \ge 1} 9t^k$ equals $9t/(1-t)$, and $9t/(1-t) = 1$ if and only if $t = 1/10$. Replace the place value by an infinitesimal and the same-looking decimal is infinitesimal rather than equal to one. The identity $0.999\ldots = 1$ is a property of the Archimedean decimal place, not of decimals as such.

## 5. Higher-rank valuations

Number fields admit only rank-one valuations: Ostrowski's classification applies to them without remainder. Higher-rank (Krull) valuations occur only in function fields of transcendence degree at least two — for example $\mathbb{Q}(x,y)$ or $\mathbb{C}(x,y)$ — and are constrained by Abhyankar's inequality, which bounds the rank of a valuation by the transcendence degree of the field [@krull1932; @aminiiriarte2022]. The field $\mathbb{C}(x)$ admits no higher-rank valuations at all: because $\mathbb{C}$ is algebraically closed, every valuation on $\mathbb{C}(x)$ trivial on $\mathbb{C}$ is a discrete rank-one place of the projective line.

## 6. Computational verification

The claims above were verified computationally with exact rational arithmetic; no floating-point approximation was used. The geometric-series identity was confirmed: $\sum_{k \ge 1} 9t^k = 9t/(1-t)$, and $9t/(1-t) = 1$ if and only if $t = 1/10$, for exact rational values of $t$ across ten orders of magnitude. The non-orderability of $\mathbb{Q}_5$ was confirmed by Hensel lifting a square root of $-1$ to $5^8$ precision: the lift is $x = 280182$, and $x^2 + 1$ is divisible by $5^8$. Since an ordered field cannot contain a square root of $-1$, $\mathbb{Q}_5$ admits no order; the same argument applies to every $\mathbb{Q}_p$ with $p \equiv 1 \pmod 4$, and the general case follows because $-1$ is a sum of squares in every $\mathbb{Q}_p$. The claim that the adele ring is not a field was confirmed by exhibiting two nonzero adeles whose product is zero.

| Check | Result |
|---|---|
| $\sum_{k\ge1} 9t^k = 9t/(1-t)$; equals 1 iff $t = 1/10$ | exact, all tested t |
| Hensel lift of $\sqrt{-1}$ in $\mathbb{Z}_5$, $5^8$ precision | $x = 280182$, $x^2+1 \equiv 0 \pmod{5^8}$ |
| $\mathbb{Q}_5$ admits no order | confirmed (contains $\sqrt{-1}$) |
| Adele ring has zero divisors | confirmed ($ab = 0$, $a, b \neq 0$) |

The verification script and its exact output are included with this record. Reproducibility: Python 3.13, standard library only; the computation is deterministic and seed-free.

## 7. Relation to prior work

The completeness decomposition given here refines the three-axis framework of the Continuum Trilogy, which distinguishes depth (Archimedean completeness), breadth (set-theoretic uncountability), and valuation (ultrametric completions of the rationals) [@continuumtrilogyiii; @continuumtrilogyi]. The present trichotomy — Dedekind, Cauchy, spherical — is a refinement of the depth axis and adds the Levi-Civita field as a concrete ordered non-Archimedean completion, a candidate the Trilogy does not name. The treatment of positional notation as an ultrametric tree and the adelic program's use of Ostrowski's theorem provide the surrounding structure in which this refinement sits [@nonlineartreebased; @tateadelic]. The relation to those records is refinement and precision, not replacement: the reals remain the unique Dedekind-complete ordered field, and the completeness question remains open in exactly the senses where a single answer would have been convenient.

## 8. Conclusion

"More perfect" is a fitness function, not an absolute. On the axis of Dedekind completeness the reals are uniquely perfect. On the axis of Cauchy completeness they are not: the Levi-Civita field is ordered, complete, real-closed, and non-Archimedean, carrying infinitesimals the reals cannot admit. On the axis of maximality the surreals are the largest ordered field, at the price of being a proper class rather than a set [@conway1976; @ehrlich2012]. On the axis of spherical completeness the p-adic fields and Hahn fields win, at the price of order. The useful output of the completeness trichotomy is not a single winner but a map: each number system is perfect for a precisely named job, and the word *complete* no longer smuggles a conclusion.

## References
