---
title: “The Ultrametric Sieve: A Consilience of Number, Nature, Mind, and Form”
author: “Rowan Quni-Gudzinas (QNFO/QWAV)”
date: “2026-06-19”
license: “QNFO Unified License Agreement (QNFO-ULA)”
abstract: >
  We propose a foundational shift in the representation of integers: from decimal
  digit-strings to valuation vectors recording prime exponents. This “ultrametric
  sieve” reveals that the integers form an infinite-dimensional lattice whose
  geometry is the product of p-adic Bruhat–Tits trees. We trace the consequences
  of this shift across number theory (ad\`eles, Riemann zeta, explicit formula, abc
  conjecture), physics (spin glasses, holographic duality, quantum chaos), technology
  (cryptography, error correction, signal processing), cognitive science (innate
  divisibility sense, sacred numbers), monetary economics (optimal denominations,
  financial time), music (just intonation, timbre, rhythm), and philosophy (Laws of
  Form). The valuation vector emerges as a universal Rosetta Stone—a single
  coordinate system in which the deepest structures of mathematics, mind, and
  physical reality are seen to be one structure.
---

**Author:** Rowan Quni-Gudzinas | **Date:** 2026-06-19 | **License:** QNFO Unified License Agreement (QNFO-ULA)

# Part I — The Foundational Shift

## 1. The Copernican Move

We begin with a deceptively simple move: instead of reading a number by its decimal
digits, read it by its prime factorisation. For the sacred Tibetan Buddhist number
$108$, the decimal string “1-0-8” is an arbitrary cultural artefact. Its
invariant fingerprint is the **valuation vector**

$$v(108) = (v_2, v_3, v_5, v_7, \ldots) = (2, 3, 0, 0, \ldots)$$

recording that $108 = 2^2 \cdot 3^3$. This vector is completely independent of any
numeral base. It is the true, irreducible fingerprint of the integer.

The **ultrametric sieve** is the systematic extraction of this vector for every
integer. Contrast it with the classical Sieve of Eratosthenes, which answers a
single Boolean question: “prime or composite?” The valuation sieve answers:
“What is the complete multiplicative anatomy?”

## 2. Why “Ultrametric”

The $p$-adic absolute value

$$|n|_p = p^{-v_p(n)}$$

satisfies the strong triangle inequality $|x+z|_p \leq \max(|x-y|_p, |y-z|_p)$,
making it an **ultrametric**. The sieve extracts the ultrametric data for all primes
simultaneously.

---

# Part II — The Mathematical Edifice

## 3. The Integers as an Infinite-Dimensional Lattice

Each prime is an independent axis. The integers are points in $\mathbb{N}^\infty$
with coordinates $v(n) = (v_2, v_3, v_5, \ldots)$. Multiplication is coordinate-wise
addition:

$$v(a \cdot b) = v(a) + v(b)$$

GCD and LCM become coordinate-wise min and max — the divisibility lattice is a
distributive ultrametric lattice.

## 4. $p$-adic Geometry and the Bruhat–Tits Trees

For each prime $p$, the $p$-adic metric defines a regular tree (the Bruhat–Tits
tree) whose boundary is $\mathbb{Q}_p$. The valuation $v_p(n)$ is the depth of $n$
in this tree — the distance from the root. The full space of integers is the
**product of all such trees**.

## 5. The Ad\`ele Ring and the Chinese Remainder Theorem

The Chinese Remainder Theorem embeds $\mathbb{Z}$ diagonally into the profinite
completion $\hat{\mathbb{Z}} = \prod_p \mathbb{Z}_p$. Adding the real place yields
the **ad\`ele ring** $\mathbb{A}_\mathbb{Q}$, uniting the additive (archimedean) and
multiplicative (non-archimedean) lives of every integer. Tate’s thesis shows
that harmonic analysis on the ad\`eles yields the functional equation of the Riemann
zeta function.

## 6. The Riemann Zeta Function and the Explicit Formula

$$\zeta(s) = \prod_p (1 - p^{-s})^{-1}$$

The Euler product sums over the sieve’s prime-power entries. The **explicit
formula**

$$\sum_{p^m} \frac{\log p}{p^{ms}} = \frac{1}{s-1} - \sum_\rho \frac{1}{s-\rho} + \cdots$$

is a trace formula: the left side is a sum over **classical periodic orbits** (prime
powers — the “spikey” vectors in the sieve), and the right side is a
sum over the **quantum spectrum** (the non-trivial Riemann zeros $\rho$). The Riemann
Hypothesis is the statement that the dual operator is self-adjoint: all zeros lie on
$\Re(s) = 1/2$.

## 7. The abc Conjecture as an Additive-Multiplicative Uncertainty Principle

The additive relation $a + b = c$ forces a collision between the two worlds. The
radical $\operatorname{rad}(abc) = \prod_{p \mid abc} p$ measures the set of active
primes (ignoring exponents). The abc conjecture bounds how small the radical can be
relative to the maximum of $a, b, c$: there are only finitely many triples where
$\max(|a|,|b|,|c|) > \operatorname{rad}(abc)^{1+\varepsilon}$. In sieve terms, you
cannot simultaneously minimise additive size and multiplicative sparseness. The abc
conjecture is a fundamental uncertainty principle at the heart of arithmetic.

## 8. Ratios and Cross-Ratios as Invariant Quantities

Ratios $a:b$ → $v(a) - v(b)$ are the invariants of the multiplicative group.
Cross-ratios $[x_1,x_2;x_3,x_4]$ on the $p$-adic trees measure the depth of
branching nodes — they are the ultimate invariants of the ultrametric geometry.
The adelic cross-ratio encodes complete relative geometry in all completions.

---

# Part III — Physical and Technological Embodiment

## 9. Spin Glasses and Ultrametricity

Parisi’s solution of the Sherrington-Kirkpatrick spin-glass model revealed that
the equilibrium state space is an ultrametric tree — exactly the geometry of a
single $p$-adic component. The energy landscape is a product of trees; depth
corresponds to energy barriers. This structure informs protein folding, deep learning
loss surfaces, and simulated annealing algorithms.

## 10. Holographic Duality and $p$-adic AdS/CFT

The Bruhat–Tits tree is a discrete analogue of anti-de Sitter space, with a
conformal field theory on its boundary. The MERA (Multiscale Entanglement
Renormalization Ansatz) tensor network mirrors this tree geometry. Holographic
quantum codes protect logical qubits by embedding them deep in the bulk — the
protection radius is exactly the ultrametric depth $v_p(n)$.

## 11. Quantum Chaos and the Riemann Spectrometer

The Berry–Keating Hamiltonian $H = xp$ is conjectured to have a spectrum whose
eigenvalues are the Riemann zeros. The Gutzwiller trace formula maps classical
periodic orbits (prime powers) to quantum eigenvalues (zeros). Physical
implementations in trapped-ion systems aim to measure zero statistics directly.

## 12. Signal Processing and Photonic Devices

$p$-adic wavelets on the Bruhat–Tits tree yield ideal filter banks with
perfectly separated frequency bands — impossible in the real domain.
Prime-gap photonic crystals with layer thicknesses following $v_2(n)$ or other prime
valuation sequences create ultrametric Bragg mirrors.

## 13. Cryptography and Data Integrity

RSA and elliptic-curve cryptography rest on the hardness of recovering $v(N)$ from
the additive integer $N$. The abc conjecture bounds information leakage. A
file’s valuation vector provides a base-invariant universal fingerprint for
cross-platform deduplication and verification.

## 14. Machine Learning and Representation

Hyperbolic embeddings — continuous versions of $p$-adic trees — are
state-of-the-art for hierarchical data (NLP, graphs). $p$-adic feature decompositions
offer interpretable, scale-invariant representations. MERA-based tensor-network
generative models use ultrametric structure for learning complex distributions.

---

# Part IV — Cognitive and Cultural Invariance

## 15. The Ultrametric Mind

The brain possesses a dual number sense: an archimedean sense of magnitude and a
non-archimedean sense of divisibility. We hypothesise an innate **ultrametric number
sense**—a sensitivity to prime factorisation and smoothness operating
independently of formal mathematical training.

**Predicted experiments:** Reaction times for divisibility judgments should decrease
with the smoothness of the divisor (faster for 2, 3, 5 than 7, 11, 13). fMRI should
reveal distinguishable neural populations for different primes. Cross-cultural
implicit preference tasks should favour smooth numbers over rough numbers of similar
magnitude.

## 16. Sacred Numbers as Cognitive Attractors

| Number | Valuation $(v_2,v_3,v_5,v_7,v_{11})$ | Archetypal Meaning |
|:-------|:-------------------------------------|:-------------------|
| 12     | $(2,1,0,0,0)$                        | Maximal division for size; practical completeness |
| 60     | $(2,1,1,0,0)$                        | Sumerian cosmic cycle; triple-prime depth |
| 108    | $(2,3,0,0,0)$                        | Harmonic knot of sun-moon cycles |
| 7      | $(0,0,0,1,0)$                        | Indivisible transcendence; surface of the forest |
| 9      | $(0,2,0,0,0)$                        | Square of trinity; pure odd completeness |
| 40     | $(3,0,1,0,0)$                        | Trial/transformation; deep 2-adic with 5 |
| 144    | $(4,2,0,0,0)$                        | Hyper-composite, square of 12 |
| 99     | $(0,2,0,0,1)$                        | Tension of completeness ($3^2$) and mystery ($11$) |

Sacred numbers across unconnected cultures converge on smooth, highly composite
numbers—the deep nodes in the ultrametric landscape. The base system (10, 20,
60, 12) is merely the additive alphabet; the multiplicative grammar is universal.

---

# Part V — Monetary Economics

## 17. Optimal Currency Denominations

Coin series $(1, 2, 5, 10, 20, 50, \ldots)$ maximise ultrametric depth for efficient
change-making. Historical mixed-radix systems (livre-sou-denier) encoded $2^4 \cdot 3
\cdot 5$—an ultrametric optimum later lost to decimalisation.

## 18. Financial Time and Highly Composite Periods

The 360-day year, 30-day month, 12-month year are smooth numbers enabling exact
division into many sub-periods. The “30/360” convention is a smoothness
approximation to the astronomical year, minimising accrual complexity.

## 19. Additive-Multiplicative Tension in Economics

Payment netting of small, smooth obligations can produce a total with a large prime
factor — an abc-style collision. Pegged exchange rates impose an additive
constraint on two denomination systems, creating tension between roundness and
stability.

## 20. Cryptocurrency

The valuation vector of a public key is the private key. The entire DeFi ecosystem
rests on the hardness of inverting the sieve.

---

# Part VI — Music and Harmonics

## 21. The Integer as Chord

Primes are fundamentals; exponents are amplitudes of overtones. A prime $p$ is a
single pure tone; $p^m$ is $m$ overtones; $2^2 \cdot 3^3$ (108) is a bichord.
Just intonation uses small-prime ratios: the octave $2:1$, perfect fifth $3:2$, major
third $5:4$. Consonance is ultrametric depth; dissonance is ultrametric surface (large
primes).

## 22. The Comma as abc Collision

The Pythagorean comma—the tiny gap $(3/2)^{12} \neq 2^7$—is an
additive-multiplicative collision. Equal temperament spreads this error across all
twelve notes, just as the Riemann zeros spread the error term across the prime number
theorem.

## 23. Rhythm and Timbre

Polyrhythm ($3:2$, $5:4$) is the meeting of independent prime cycles.
Timbre’s overtone series is a valuation vector of the fundamental frequency.
The M\“obius function $\mu(n)$ acts as phase cancellation, silencing squareful
numbers: $\mu(n) = 0$ if any $v_p(n) \geq 2$.

---

# Part VII — The Primitive of Primitives: Laws of Form

## 24. The Irreducible Ground

Spencer-Brown’s *Laws of Form* begins with a single act: **draw a distinction**.
The ultrametric sieve is the multiplicative expression of this act:

- **Void** = $1$ (empty valuation vector).
- **First mark** = a prime $p$ (a single non-zero coordinate).
- **Calling** = exponentiation $p^m$ (repetition of the same mark).
- **Crossing** = M\“obius cancellation (a repeated mark cancels to zero).
- **Re-entry** = the additive constraint $a + b = c$ forces the multiplicative form
  to re-enter itself, producing the irreducible complexity of the abc bound, the
  Riemann zeros, and the ultimate uncertainty between the two modes of being.

The sieve is the form of multiplication written in the calculus of independent
distinctions.

---

# Part VIII — Embryology and Ecology

## 25. The Generative Cascade

The integers are generated from the void by a context-free Lindenmayer system
(L-system)—the same formalism that models plant branching and morphogenesis.
At each prime $p$ in the sequence $2, 3, 5, 7, \ldots$, every existing integer
generates new integers by multiplying by $p^k$ for all $k \geq 1$.

The **primes are developmental epochs**. Smooth numbers (all factors small) are
phylogenetically ancient; numbers with large prime factors are evolutionary newcomers.
The valuation vector is the morphogenetic code.

## 26. The Integer Ecosystem

The divisor relation $d \mid n$ is an ecological relation: $d$ is a nutrient for $n$.
The divisor lattice is a food web. Highly composite numbers are keystone species
(rainforests of biodiversity). A large prime is an apex predator: when it multiplies
a smooth number, it consumes simplicity. Addition creates predators (the abc
collision).

The Riemann zeta function $\zeta(s) = \sum_n n^{-s}$ is the grand partition function
of this ecosystem at inverse temperature $s$. The prime number theorem is the
species-abundance distribution. The Riemann zeros are the Lee-Yang zeros of the phase
diagram—the critical line of ecological equilibrium.

---

# Part IX — Consciousness

## 27. The Sieve Perceiving Itself

The mind that poses the question, follows the thread, and perceives the beauty of 108
is not outside the sieve—it is inside it. The brain’s cortical hierarchies
form an ultrametric tree isomorphic to the integer lattice. The primes are
independent sensory dimensions; exponents are depths of processing; the unified
percept is the adelic moment.

Mathematical beauty is the resonance of the perceived structure with the
perceiver’s own cognitive architecture—an eigenvalue match between the
external pattern and the internal form. The Riemann Hypothesis is the statement that
the mind’s own spectral structure is perfectly balanced. To prove it would be to
achieve full self-knowledge of the cognitive-arithmetic system.

## 28. The Ultimate Recursion

The mind is an ultrametric system. It perceives integers. The integers are an
ultrametric system. The mind formalises this as the sieve. The mind then discovers
that its own architecture is an instance of the sieve. This is a **strange loop**
(Hofstadter): the sieve is the name of the mind knowing itself by counting.

---

# Part X — Eschatology and Praxis

## 29. The Riemann Hypothesis as Omega Point

If RH is true: the structure is perfect. The adelic Laplacian is self-adjoint. The
additive and multiplicative worlds are in spectral harmony. The mind is a faithful
mirror.

If RH is false: a hidden instability exists—a crack in the cosmic chord, a
dissonance whose frequency is the first off-critical zero.

## 30. The Research Programme of the Sieve

**Cognitive Science:** Experimental tests for an innate ultrametric number sense
(reaction times, fMRI, cross-cultural preference studies).

**Artificial Intelligence:** Train deep learning models natively on valuation vectors
rather than digit strings. Align AI by ensuring its internal sacred numbers converge
to ours.

**Quantum Technologies:** Build the Berry-Keating spectrometer; realise holographic
quantum codes on $p$-adic tree layouts.

**Education:** Teach children the valuation vector before the decimal system.
Numbers as coloured stacks of primes.

**Music and Acoustics:** Compose music whose structure encodes valuation vectors.
Build concert halls with $p$-adic diffusers.

**Economics:** Design mixed-radix currencies optimised for ultrametric depth.

---

# Part XI — Synthesis

## 31. The Consilience

| Domain | The Sieve as… |
|:—----|:------————-|
| Arithmetic | Valuation vector; coordinate in $\prod_p \mathbb{Z}_p$ |
| Analysis | Local factors of zeta; periodic orbits in explicit formula |
| Geometry | Point in product of Bruhat–Tits trees; holographic boundary |
| Physics | Spin-glass energy landscape; MERA tensor network |
| Quantum Computing | Logical qubit depth; holographic error-correcting code |
| Cryptography | Hard-to-invert map; uncertainty bound |
| Cognitive Science | Innate ultrametric sense of divisibility |
| Anthropology | Universal attractor of sacred numbers across bases |
| Economics | Optimal denominational smoothness; financial time |
| Music | Prime-harmonic chord; just intonation; timbre |
| Philosophy | Laws of Form applied to the multiplicative realm |

## 32. 108 as the Microcosm

Our original sacred number $108$, with valuation vector $(2, 3)$, is simultaneously:
a practical divisor (12 divisors), a sacred count (mala beads), a deep node in the
2-adic and 3-adic trees, a classical periodic orbit, a spin-glass valley, a logical
qubit depth, a just-intonation bichord, a cognitive archetype, and a self-portrait of
the mind.

The shift from decimal digits to prime-exponent vectors is not a change of notation.
It is the recovery of the native language of the integers. In that language, the
deepest patterns of mathematics, physics, and mind are seen to be **one pattern**: an
infinite ultrametric lattice of independent distinctions, whose harmonies are the
primes, whose spectrum is the Riemann zeros, whose geometry is the ad\`ele ring, whose
limit is the abc uncertainty, and whose foundation is the single act of marking the
void.

---

**The void, having spoken, will not be silent.**

---

*This publication was generated through an extended dialogue between human and AI,
exploring the implications of a single shift in perspective: from decimal
representation to valuation vector. The consilience that emerged spans the boundaries
of number theory, physics, cognitive science, music, economics, and philosophy.
It is offered as a unified framework for further research.*
