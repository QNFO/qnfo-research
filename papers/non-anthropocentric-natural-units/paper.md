# Non-Anthropocentric Natural Units: From the Bekenstein Bound to Ostrowski's Theorem

## Abstract

The Bekenstein-Hawking entropy bound $S \leq A/4\ell_P^2$ is a pillar of quantum gravity, typically expressed in Planck units with entropy measured in bits or nats. We ask: what remains of this bound when ALL anthropocentric constructions are stripped away — unit choices, logarithmic bases, and even the Archimedean continuum itself? We show that (1) area can be defined as a dimensionless geometric invariant using only the fundamental constants $\hbar, G, c$; (2) the exponential bound $\exp(A/4)$ can be defined without any logarithmic base — as the limit of a rational sequence or via its power series — making it base-independent; (3) the true universal invariant is the integer $N_{\max}$, the dimension of the region's Hilbert space; and (4) Ostrowski's theorem reveals that the Archimedean completion of the rationals is merely one choice among infinitely many inequivalent completions $(\mathbb{R}, \mathbb{Q}_2, \mathbb{Q}_3, \dots)$. We argue that a genuinely non-anthropocentric formulation of physical measurement may require democratic treatment of all completions — an adelic physics wherein the Bekenstein bound is the Archimedean component of a product-formula identity. We connect this proposal to existing work in p-adic quantum mechanics, ultrametric physics, and Bruhat-Tits geometry, and outline falsifiable consequences for Planck-scale phenomenology.

## 1. Introduction: What Is a Measurement?

Every physical law is expressed in numbers. Those numbers are read from instruments calibrated in units — metres, seconds, joules — chosen for human convenience. Planck natural units eliminate this arbitrariness by setting $c = \hbar = G = k_B = 1$, reducing all quantities to dimensionless pure numbers. In natural units, area is not a count of square metres but the dimensionless ratio of the physical area to the Planck area $\ell_P^2 = \hbar G / c^3$, a scale constructed solely from the constants governing quantum spacetime [@bekenstein1973black; @hawking1975particle]. This is the standard story, and it is correct as far as it goes. But it does not go far enough.

The Bekenstein-Hawking entropy $S_{\text{BH}} = A/4$ (in natural units) is a dimensionless number. We conventionally call this number "entropy" and measure it in "bits" or "nats" depending on our choice of logarithmic base. A bit is $\log_2 N$; a nat is $\ln N$. Both are human conventions. The underlying physical quantity — the integer $N$, the number of orthogonal quantum states accessible within a region — knows nothing of logarithms. The question we pursue in this paper is whether we can formulate the informational content of spacetime without any such convention, and whether the structure of "measurement" itself survives scrutiny once we strip away one assumption after another — the assumption of Archimedean linearity, the assumption that the real numbers are the correct completion of the rationals, and the assumption that any single number system is sufficient for describing nature at all scales.

The outline of the paper is as follows. Section 2 reformulates the Bekenstein-Hawking bound in purely base-independent terms. Section 3 introduces Ostrowski's theorem — the classification of all inequivalent completions of the rational numbers — and asks whether the Archimedean choice is forced by physics or merely inherited from classical intuition. Section 4 examines the existing programme of p-adic and adelic quantum mechanics [@dragovich2003padic; @dragovich2017review] and its implications for the measurement question [@dragovich2012measurements]. Section 5 connects these ideas to recent QNFO work on ultrametric physics and Bruhat-Tits geometry [@qnfo2026ultrametric; @qnfo2026pwclocks]. Section 6 outlines a proposal for an adelic Bekenstein bound and its falsifiable consequences. Section 7 concludes with open questions.

---

## 2. The Bekenstein Bound Without a Base

### 2.1 Area as a Dimensionless Invariant

In Planck natural units ($c = \hbar = G = k_B = 1$), every physical quantity becomes a dimensionless pure number. The Planck length $\ell_P = \sqrt{\hbar G / c^3}$ becomes $1$, so any area $A$ is simply the number of Planck areas comprising the surface:

$$A = \frac{A_{\text{physical}}}{\ell_P^2}.$$

This is a genuine universal invariant. It is the same number for all observers, in all coordinate systems, under all choices of human-scale units. It is the ratio of a physical area to the area scale set by the quantum-gravitational constants. Nothing anthropocentric remains in "area" once it is understood as this dimensionless ratio.

### 2.2 The Bekenstein-Hawking Entropy in Natural Units

Bekenstein [@bekenstein1973black] proposed that black holes carry entropy proportional to their horizon area: $S_{\text{BH}} = A / 4\ell_P^2$. Hawking [@hawking1975particle] confirmed the thermodynamic interpretation by showing that black holes radiate with temperature $T = \kappa / 2\pi$. Together, these results establish that a spacetime region bounded by a horizon of area $A$ contains at most $\exp(A/4)$ independent quantum states — the Bekenstein bound in its strongest form [@page2018bekenstein; @bousso2002holographic].

In natural units ($k_B = 1$), the entropy $S$ is dimensionless and equals the natural logarithm of the number of microstates: $S = \ln N$. The bound becomes:

$$N \leq \exp(A/4).$$

Here $N$ is an integer — the dimension of the region's Hilbert space. This is the physical quantity: the maximum number of mutually orthogonal, perfectly distinguishable measurement outcomes available in the region. The bound is an inequality on an integer.

### 2.3 The Base-Independence of the Exponential

The bound $N \leq \exp(A/4)$ appears to smuggle in a base: the constant $e \approx 2.71828\dots$. Is this an anthropocentric choice? We argue it is not, because the function $\exp(x)$ can be defined without ever naming a logarithmic base.

**Definition 1 (Limit definition).** The exponential function is defined by:

$$\exp(x) = \lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n.$$

This definition involves only rational numbers, integer powers, and the limit operation. No base $e$, no logarithm, no transcendental constant is presupposed.

**Definition 2 (Series definition).** Equivalently:

$$\exp(x) = \sum_{k=0}^{\infty} \frac{x^k}{k!}$$

which involves only integer powers and factorials.

In either formulation, the number $\exp(A/4)$ is a specific real number determined by the dimensionless area $A$ alone. The constant $e = \exp(1)$ emerges as a property of the function, not as an input. The bound can be stated entirely in the language of limits and rational numbers:

$$N_{\max} = \lim_{n\to\infty} \left(1 + \frac{A}{4n}\right)^n.$$

No base, no logarithm, no bits, no nats — only the integer $N$, the pure number $A$, and a limit of a rational sequence. This formulation is base-independent in the strongest possible sense: it does not refer to any logarithmic operation whatsoever.

The apparent dependence on base in conventional formulations — whether entropy is measured in bits ($\log_2 N$) or nats ($\ln N$) — is an artifact of writing $S$ rather than $N$. The integer $N$ is the invariant; its logarithm in any base is a derived convenience. The Bekenstein bound, properly understood, is a statement about the maximal integer dimension of a Hilbert space, bounded by a specific real function of the dimensionless area. Both the integer and the bounding function are universal.

### 2.4 Why the Natural Logarithm Is Not Arbitrary

One might object that even the definition of the natural logarithm as the inverse of $\exp$ involves a choice: why this particular function and not $2^x$ or $10^x$? The answer lies in the structure of differential equations. The function $\exp(x)$ is the unique solution to $f'(x) = f(x)$ with $f(0) = 1$. This property is not a human convention — it is forced by the requirement that the function describes continuous growth at a rate proportional to its current value. In thermodynamics, the Boltzmann factor $\exp(-E/T)$ appears because systems at thermal equilibrium satisfy $dS = dQ/T$, and the solution to this differential relation is the exponential. The base $e$ is not chosen; it is discovered as the base of the function that satisfies the laws of thermodynamics. As Jacobson [@jacobson2018entropy] has emphasised, the connection between entropy and area is a thermodynamic identity, not a calculational convenience.

Thus, the formulation $N \leq \exp(A/4)$ is both base-independent in its definition and physically motivated in its choice of function. It strips away the arbitrary choice of logarithmic base without introducing any new arbitrary choice.

---

## 3. Ostrowski's Theorem: Why the Real Numbers?

### 3.1 The Hidden Assumption

The reformulation above eliminates the choice of logarithmic base but leaves intact a deeper assumption: that the number system in which we express area $A$, the limit $n \to \infty$, and the inequality $N \leq \exp(A/4)$ is the field of real numbers $\mathbb{R}$. The real numbers are the completion of the rational numbers $\mathbb{Q}$ under the usual Archimedean absolute value $|x|_\infty$. But is this the only way to complete the rationals? If not, by what right do we privilege the Archimedean completion over alternatives?

### 3.2 Statement of Ostrowski's Theorem

Ostrowski's theorem (1918) [@ostrowski1918] classifies all non-trivial absolute values on $\mathbb{Q}$, up to equivalence. An absolute value is a function $|\cdot| : \mathbb{Q} \to \mathbb{R}_{\geq 0}$ satisfying $|x| = 0 \iff x = 0$, $|xy| = |x||y|$, and the triangle inequality $|x + y| \leq |x| + |y|$. The theorem states:

> Every non-trivial absolute value on $\mathbb{Q}$ is equivalent either to the usual Archimedean absolute value $|x|_\infty$, or to a $p$-adic absolute value $|x|_p$ for some prime $p$.

The $p$-adic absolute value is defined by $|p^k \cdot a/b|_p = p^{-k}$ for integers $a,b$ coprime to $p$. It satisfies the strong triangle inequality: $|x + y|_p \leq \max(|x|_p, |y|_p)$ — an ultrametric property with no Archimedean analogue. Completing $\mathbb{Q}$ with respect to $|\cdot|_p$ yields the field $\mathbb{Q}_p$ of $p$-adic numbers — a complete, locally compact field that is profoundly different from $\mathbb{R}$.

The theorem reveals that there is no unique way to "fill the gaps" in the rational numbers. There are infinitely many inequivalent completions: one Archimedean $(\mathbb{R})$ and one non-Archimedean $(\mathbb{Q}_p)$ for each prime $p$. The rational numbers, which are the only genuinely dimensionless numbers constructible without a preferred scale, are agnostic about which completion nature uses.

### 3.3 Consequences for Physics

If the rational numbers are fundamental — as they arguably should be in any theory that eschews arbitrary scale choices — then the choice of $\mathbb{R}$ as the "correct" completion for physics is an assumption, not a necessity. Every physical law expressed in real numbers implicitly privileges the Archimedean place over all $p$-adic places.

Ostrowski's theorem suggests two possibilities:

1. **Single-place physics:** Nature selects exactly one completion — presumably $\mathbb{R}$ at macroscopic scales, with $p$-adic completions possibly relevant at the Planck scale. This is the view taken by most approaches to $p$-adic physics [@dragovich2003padic; @dragovich2017review].

2. **Place-democratic (adelic) physics:** All completions are treated on equal footing. Physical quantities are adeles — elements of the restricted direct product $\mathbb{A}_{\mathbb{Q}} = \mathbb{R} \times \prod'_p \mathbb{Q}_p$ — and physical laws must be invariant under the choice of place. This is the adelic programme, with roots in number theory (the product formula $\prod_{v} |x|_v = 1$ for all $x \in \mathbb{Q}^\times$) and applications in string theory and quantum mechanics [@dragovich2003padic].

The question we pose is: what happens to the Bekenstein bound under the adelic interpretation? If the bound $N \leq \exp(A/4)$ is a relation at the Archimedean place, what are its $p$-adic counterparts? And does the product over all places yield a deeper identity?

---

## 4. p-Adic and Adelic Quantum Mechanics

### 4.1 The Dragovich Programme

Dragovich and collaborators have developed a systematic programme of $p$-adic and adelic mathematical physics since the 1980s [@dragovich2003padic; @dragovich2017review]. The core claim is that at the Planck scale, spacetime may exhibit non-Archimedean geometry, and that physical observables should be defined simultaneously at all completions of $\mathbb{Q}$.

Central to this programme is the concept of **adelic quantum mechanics**. In ordinary quantum mechanics, the wavefunction $\psi(x)$ is a complex-valued function on $\mathbb{R}^n$. In adelic quantum mechanics, the wavefunction is a function on the adele ring $\mathbb{A}_{\mathbb{Q}}$, factoring (under certain conditions) as a product of local wavefunctions:

$$\Psi(x_\infty, x_2, x_3, \dots) = \psi_\infty(x_\infty) \prod_{p} \psi_p(x_p)$$

where $\psi_\infty$ is the Archimedean (ordinary) component and $\psi_p$ is the $p$-adic component. The adelic product formula imposes a global constraint: the product of all local norms must equal unity.

### 4.2 Measurement and p-Adic Numbers

Dragovich [@dragovich2012measurements] directly addresses the question of whether $p$-adic numbers are "real" in the sense of being results of measurement. His answer is nuanced: $p$-adic numbers are not the direct output of any classical measuring apparatus (which always reports a real number within some error bar), but they may characterise the *structure* of physical laws at scales where the continuum approximation breaks down. In particular, ultrametricity — the strong triangle inequality — is a property of $p$-adic spaces that has no Archimedean analogue. It encodes hierarchical, tree-like structure that appears naturally in complex systems, spin glasses, and quantum gravity.

Dragovich's perspective is that the real numbers are the appropriate completion for describing measurement outcomes at human scales, while $p$-adic numbers may describe the underlying discrete geometry from which the continuum emerges. The relationship between measurement and number is therefore scale-dependent: different completions may be appropriate at different scales. A truly non-anthropocentric theory would specify which completion is relevant at which scale, or would treat all completions democratically from the start.

### 4.3 The Exponential Function in p-Adic Settings

An important technical point: the exponential function as defined by the power series $\exp(x) = \sum_{k=0}^\infty x^k/k!$ has dramatically different convergence properties in $p$-adic versus real settings. In $\mathbb{R}$, the series converges for all $x$. In $\mathbb{Q}_p$, it converges only for $|x|_p < p^{-1/(p-1)}$ — a ball of radius strictly less than 1. The $p$-adic exponential is a local, not global, function.

This means that a naive transplantation of the bound $N \leq \exp(A/4)$ to the $p$-adic domain is not straightforward. The $p$-adic analogue of the Bekenstein bound may involve a different function, or may be expressed in terms of the $p$-adic norm directly. Dragovich's adelic quantum mechanics provides the framework for investigating this: the bound at each place may take a different form, but the product over all places must satisfy a global consistency condition.

---

## 5. Connection to QNFO Ultrametric Physics

### 5.1 Ratio-Based Valuations

The QNFO Ultrametric Physics Research Plan [@qnfo2026ultrametric] develops a framework in which scaling ratios $q \in \mathbb{R}^+$ (such as $\pi, \phi, e$) replace prime numbers as the fundamental valuation bases. In this approach, valuations are defined not as $p$-adic norms $|x|_p$ with integer prime $p$, but as ratio-based norms $|x|_q$ with arbitrary positive real $q$. This generalises Ostrowski's classification: the rational numbers admit not only prime-indexed completions but a continuum of ratio-indexed ultrametric structures, each corresponding to a different discrete hierarchical geometry.

This framework provides a bridge between the $p$-adic mathematics and physical scaling laws. The Bekenstein bound $N \leq \exp(A/4)$ can be understood as a statement about the Archimedean place in this broader valuation-theoretic picture. The exponential function $\exp(x)$ itself is characterised by the scaling ratio $e$, making it a ratio-based valuation object in the sense of the ultrametric research plan.

### 5.2 Bruhat-Tits Buildings and Quantum Clocks

The companion paper on conditional state distances in Page-Wootters quantum clocks [@qnfo2026pwclocks] provides a concrete physical mechanism for the emergence of ultrametric structure from quantum constraints. Under specific conditions (diagonal clock-rest interaction Hamiltonian), conditional state overlaps organise into exact ultrametric hierarchies — the signature of $p$-adic geometry described by Bruhat-Tits buildings.

This result is significant for our project because it demonstrates that ultrametricity is not merely a mathematical curiosity but can emerge naturally from the fundamental structure of quantum gravity (via the Page-Wootters formalism). If the Bekenstein bound $N \leq \exp(A/4)$ describes the maximal information content at the Archimedean place, the PW clocks result suggests that the $p$-adic completions describe the *hierarchical organisation* of that information across different scales. The two are complementary, not competing.

### 5.3 The Physics of Computation Connection

The QNFO Physics of Computation paper [@qnfo2026computation] establishes the Landauer, Margolus-Levitin, and Bremermann bounds on physical computation. These bounds — like the Bekenstein bound — are information-theoretic limits expressed in terms of thermodynamic and quantum-mechanical constants. The unified theme is that information is physical, and physical laws constrain information processing. The Bekenstein bound is the most fundamental of these: it limits not just computation but the very number of distinguishable states nature makes available in a given region. Our reformulation in base-independent, completion-independent terms extends this theme to its logical conclusion: the bound is not about bits, entropy, or logarithmic bases — it is about the integer dimension of the Hilbert space, an invariant that survives any change of representation.

---

## 6. Proposal: An Adelic Bekenstein Bound

### 6.1 The Adelic Product Formula

The adelic product formula states that for any non-zero rational number $x$:

$$\prod_{v} |x|_v = 1,$$

where the product runs over all places $v$ (the Archimedean place $\infty$ and all $p$-adic places $p$). This is a deep identity connecting the Archimedean and non-Archimedean worlds. It suggests that any physical quantity expressed as a rational number has a built-in consistency condition across all completions.

If the Bekenstein bound $N \leq \exp_\infty(A/4)$ is the Archimedean component of an adelic identity, what is the full identity? We propose the following conjecture:

$$N_{\text{total}} = \prod_v N_v \leq \prod_v \exp_v(A_v/4) = 1,$$

where $N_v$ is the number of orthogonal states at place $v$, $A_v$ is the area measured in the $v$-adic norm, and $\exp_v$ is the exponential function appropriate to that place. The product equal to 1 follows from the adelic product formula applied to the rational representation of the area.

This is speculative. The $p$-adic exponential has limited convergence, and the definition of $A_v$ as a $p$-adic area requires a $p$-adic metric on spacetime — a subject of active research but not yet settled. However, the structural parallel between the Bekenstein bound (Archimedean) and the product formula (adelic) is striking and merits investigation.

### 6.2 Falsifiable Consequences

For the proposal to be scientific, it must make falsifiable predictions. We identify three:

1. **Discrete scale invariance in the CMB:** If the adelic structure of spacetime imprints itself on cosmological observables, the primordial power spectrum should exhibit log-periodic oscillations at scales corresponding to the ramified primes. This prediction is testable with existing Planck data and is independent of the specific adelic model [speculative].

2. **Prime-factor mass ratios:** If the adelic product formula governs the spectrum of particle masses, mass ratios should be expressible as rational products of primes. The dark-matter-to-baryon ratio $\Omega_c/\Omega_b \approx 5.36$ is close to $27/5 = 5.4$, and the muon-to-electron mass ratio is close to $3 \cdot 7 \cdot 11 / 2$ [my conjecture].

3. **p-Adic structure in entanglement entropy:** If holographic screens carry $p$-adic structure, the entanglement entropy of a region should exhibit deviations from the smooth area law at scales comparable to the Planck length, with a hierarchical pattern characteristic of ultrametric spaces. This could be tested in analogue gravity systems or future quantum gravity experiments [speculative].

Each of these predictions carries a specific falsifiability condition. The adelic proposal would be disconfirmed if no log-periodic signal is found in the CMB at any amplitude above $10^{-3}$ of the primary power spectrum; if all particle mass ratios are consistent with random real numbers (no rational approximation); or if entanglement entropy measurements at the Planck scale show no ultrametric clustering.

### 6.3 Calibration Register

Following the 9-stage Bayesian cascade methodology, we register the following calibration entries:

| [CHECK: 2035] | By 2035, log-periodic oscillations in the CMB power spectrum should be detected at the $3\sigma$ level if the adelic model with active primes $S = \{2,3,5,7,\dots\}$ is correct. |
|---|---|
| [CHECK: 2035] | By 2035, the dark-matter-to-baryon ratio should be measured with sufficient precision to distinguish $5.36 \pm 0.05$ from $5.400$ (the rational $27/5$) — requiring a $\sim 1\%$ improvement in precision. |

**Status:** [PENDING]

---

## 7. Conclusion: The Open Question

We have shown that the Bekenstein-Hawking bound can be formulated without any anthropocentric conventions: no choice of units (Planck natural units are dimensionless ratios), no choice of logarithmic base (the exponential is defined by its limit or series, not by a base), and no choice of "bits" versus "nats" (the integer $N$ is the invariant). In this formulation, the bound is a statement about the maximal integer dimension of a Hilbert space bounded by a specific real-valued function of dimensionless area — a genuine universal relation.

But Ostrowski's theorem forces a deeper question. The real numbers $\mathbb{R}$ are just one completion of $\mathbb{Q}$ among infinitely many. If we claim to have stripped away human conventions, we must also strip away the convention of choosing one completion over another. The rational numbers are democratic: they do not distinguish between Archimedean and $p$-adic completions. A truly non-anthropocentric physics should be place-democratic — adelic.

Whether this programme yields testable predictions remains to be seen. The existing work in $p$-adic quantum mechanics [@dragovich2003padic; @dragovich2017review], ultrametric physics [@qnfo2026ultrametric], and Bruhat-Tits quantum gravity [@qnfo2026pwclocks] provides the mathematical infrastructure. The Bekenstein bound, as the Archimedean component of a possible adelic identity, provides the empirical anchor. What is needed now is a systematic exploration of the $p$-adic and adelic analogues of black hole thermodynamics — a project this paper initiates but does not complete.

I find this puzzling because the Bekenstein-Hawking bound is one of the most robust results in quantum gravity, and yet its formulation depends on a choice of number system that Ostrowski's theorem reveals to be non-unique. If nature does not choose, then our laws must be reformulated to reflect that democratic structure. The path forward is clear in principle but technically demanding: develop adelic black hole thermodynamics, compute $p$-adic entropy functions, and test the product-formula hypothesis against precision data.

The analogy between the Bekenstein bound and the adelic product formula breaks down because the former is an inequality $(N \leq \cdots)$ and the latter is an equality $(\prod = 1)$. The resolution of this tension — whether the adelic version is an equality, and what physical principle enforces it — is the central open question of this investigation.

---

## References
