# Re-Entry as a Binary Prohibition Law: Enumeration, Impossibility, and the Three-Outcome Completion

## Abstract

Self-referential constraints arise in hardware security, programmable logic, and symbolic execution tools, where a system must forbid a state while generating the very operation that enforces the prohibition. The open question is whether a re-entering form of the calculus of indications — a distinction taken inside its own indicational space — can simultaneously function as a binary prohibition law: a total rule on a two-element domain that forbids each of its own inputs. We adopt the strictest of three reconciled conventions, in which a prohibition law is a total self-map $f$ with $f(x) \neq x$ for all $x$, and re-derive with explicit arithmetic that exactly $1$ of $2^{2} = 4$ unary laws on the two-element Boole algebra satisfies it (the negation, density $0.25$), that this law has no fixed point and re-entry period $T_{2} = 2$, and that a settled binary prohibition re-entry is therefore impossible. Extending to a three-outcome space $S_{3} = \{m, u, v\}$, derangement arithmetic yields exactly $2$ prohibition laws of $3^{3} = 27$, both of period $3$; density falls by a factor $27/8 = 3.375$ at an entropy cost of $\log_{2} 3 - 1 = 0.5849625$ bits. A secondary forbidden-word model with the single forbidden pair $11$ leaves $a_{10} = 144$ of $1024$ length-$10$ sequences admissible (survival ratio $0.140625$) and reproduces the three-outcome capacity $\log_{2} 3 = 1.5849625$ bits at the pair level. All quantities follow from finite enumeration or closed-form evaluation; no empirical data are used. The result tells verification engineers that a binary self-prohibition cannot settle, and that guaranteeing prohibition requires either a third outcome or external monitoring.

## 1. Introduction

Systems that enforce a rule on themselves are common and hard to verify. Engineers who insert micropatches into compiled binaries must confirm that a patched function behaves identically to the original, and the tool cozy was built precisely to symbolically execute both versions and check that their observable behavior agrees [3]. Astronomers testing a catalog of binary black hole coalescences must check the sky distribution of events against enumerated reference constructions rather than intuition, as was done for the LIGO–Virgo O1–O2 detections by comparing an observed two-dimensional correlation function to references built from mock localization-error datasets [5]. In both cases a constraint is applied to a system that already contains the constraint's own output; the question of what happens when such a self-applied constraint is made exact and minimal is the question this paper formalizes.

The stakes are concrete. A microcontroller that must never assert a reset signal may be programmed with a self-modifying routine that toggles the reset line; if the routine settles, the prohibition fails, leading to costly failures or security breaches. Whether a self-referential binary constraint can be guaranteed to forbid its own input without external monitoring directly affects verification cost and system reliability. If the paper's central impossibility result holds, the design decision changes: a designer who today hopes to enforce a prohibition with a single self-applied binary rule must instead budget for perpetual oscillation, a third signal level, or an external watchdog.

The calculus of indications, in the tradition of Spencer-Brown, builds logic from a single primitive act: drawing a distinction and marking one of its sides. Its most delicate construction is re-entry, the operation by which the form of a distinction is taken as indicational content of the distinction itself. A prior reconciled analysis of three independent drafts asked whether a re-entering form can simultaneously function as a binary prohibition law and resolved the drafts' disagreement by adopting the strictest formal convention, deriving an impossibility result for the two-element case and a completion in three outcomes [7]. That analysis left two things undone: it did not connect the formal result to the applied settings in which self-referential constraints are actually verified, and it did not examine how the density of prohibition laws behaves as the state space grows. This paper does both, re-deriving every number with the arithmetic shown and reading the result against adjacent works that study two-state systems under constraints.

The contributions are:

1. A finite enumeration of all unary laws on the two-element Boole algebra, with the prohibition condition isolating exactly one law, the negation, at density $1/4 = 0.25$ (Section 4.1).
2. A re-entry analysis showing that this law has orbit period $T_{2} = 2$ and no fixed point, so a settled binary prohibition re-entry is impossible (Section 4.2).
3. A three-outcome extension in which derangement arithmetic shows exactly $2$ prohibition laws of $27$, both of period $3$ (Section 4.3).
4. Quantitative comparisons: density ratio $27/8 = 3.375$ and entropy increment $\log_{2} 3 - 1 = 0.5849625$ bits (Section 4.4).
5. A secondary forbidden-word model in which a single adjacent-pair prohibition leaves $a_{10} = 144$ admissible sequences of length $10$ out of $2^{10} = 1024$, with pair-level capacity $\log_{2} 3$ matching the three-outcome algebra (Section 4.6).
6. A reading of the formal result against applied self-referential validation, with explicit falsification conditions and the smallest next experiment (Sections 6 and 7).

Throughout, "binary" is used in the two senses the literature itself uses indiscriminately: the two-element Boole algebra, and "binary" as in binary programs [3], binary star systems [4], and binary black hole coalescences [5]. In each case a two-state system is subject to a constraint, and the question is whether the constraint can be self-applied.

## 2. Background and Related Work

Seven works frame this analysis; each contributes a specific method, result, or structural analogy.

**[1] Marine size spectra stability.** This work presents a local stability analysis of the power-law steady state of marine size spectra, considering three dynamical systems describing organism abundance as a function of body mass and time: a jump-growth equation, a first-order approximation (the McKendrick–von Foerster equation), and a second-order approximation (the McKendrick–von Foerster equation with diffusion) [1]. Its discussion notes that, instead of nodes representing a finite number of species, the analysis uses a continuous weight range corresponding to an infinite number of "nodes", giving a continuous spectrum of eigenvalues, and that the predator search exponent $\alpha$ and steady state exponent $\gamma$ are set so that $\alpha = \gamma - 1$. The relevance is methodological: a steady state of a self-organizing system may look like a fixed point at one level of description while the exact dynamics differ — precisely the situation found here, where the re-entering prohibition law has no fixed point at all in the primary model.

**[2] Plankton biodiversity and the power law.** This work explains two features of unicellular plankton assemblages — high biodiversity and the power-law structure of abundance — through an allometric scaling of cell growth and mortality with cell size, demonstrated via a numerical study of a size-structured, multispecies, population-dynamic model with a single resource [2]. Its discussion reports that predator-prey dynamics can drive the assemblage toward a power-law relationship between cell mass and abundance, and that with enough species the near-power-law equilibrium can be an attractor. The structural analogue is that a simple local rule generates global structure without fine-tuning, just as a single local prohibition generates a global, exactly countable reshaping of sequence space in the secondary model of Section 4.6.

**[3] cozy: comparative symbolic execution for binary programs.** This work introduces cozy, a tool for analyzing and visualizing differences between two versions of a software binary, with the primary use case of validating micropatches — small binary or assembly-level patches inserted into existing compiled binaries — using the Python-based angr symbolic execution framework [3]. Its evaluation reports that cozy symbolically executes both functions, computes the set of compatible state pairs, and checks an assertion that the states agree in register and memory contents, with the agreement criterion depending on return type (for a 64-bit integer return, the full RAX contents must be equal; for 32-bit, only EAX). Its results state that cozy verifies the instrumentation code leaves each function's observable behavior unaffected, with per-function symbolic execution times ranging from $0.0092$ s to $16.0683$ s, and its discussion reports testing on DARPA Assured Micropatching challenge problems including a proposed micropatch for the Army MRZR platform. This is the applied cousin of the present question: verifying a constraint on a two-level structure (branch taken or not taken) that is itself part of the system being verified.

**[4] Evolutionary memory in binary systems.** This work shows that the degree of spin correlation between the components of binary stars is independent of the components' separation, extending previously established correlation results [4]. Its data section describes samples including artificial binaries created by shuffling components, and a visual-binary subset containing $33$ systems with known separation; its results state that spin correlation in visual binaries is present, that it does not depend on separation distance, and that memory of initial conditions in close binary systems is erased by tidal interaction, so the observed correlation in visual binaries should be due to other mechanisms possibly reflecting initial conditions. The relevance is correlation without a mediating coupling at the observed scale: a shared constraint whose enforcement cannot be located at any single point of the system — it lives in the orbit, not in a state, which is how the prohibition law of Section 4.2 behaves under re-entry.

**[5] Two-dimensional correlation function of binary black hole coalescences.** This work computes the two-dimensional correlation functions of the binary black hole coalescence detections in LIGO–Virgo's first and second observation runs, treating the sky localization error regions of the detections as probability density heat maps rescaled to NSIDE resolution $256$, corresponding to a pixel angular resolution of $\theta_{\text{pix}} \sim 0.23^{\circ}$ [5]. Its conclusions report that the distribution of O1–O2 binary black hole events in the sky was in agreement with a uniform distribution of sources, and that the power-law slope of the correlation function was found to be $\gamma = 2.24 \pm 0.33$, consistent with the upper bound of the power-law slope from galaxy surveys at low redshift. This work supplies the discipline this paper follows: testing a population of two-state events against enumerated reference constructions rather than intuition, which is what the exhaustive enumerations of Sections 4.1 and 4.3 do for prohibition laws.

**[6] Integral means, convolution, and univalent functions.** This work uses the Baernstein star-function to investigate questions about the integral means of the convolution of two analytic functions in the unit disc, with the theory of univalent functions playing a basic role [6]. Its introduction defines the Hadamard convolution $(f \star g)(z) = \sum_{n=0}^{\infty} a_{n} b_{n} z^{n}$ for $f(z) = \sum a_{n} z^{n}$ and $g(z) = \sum b_{n} z^{n}$, notes that the convolution operation makes the holomorphic functions into a commutative complex algebra with identity $I(z) = 1/(1-z)$, and its second section presents the star-function $u^{*}$ of a subharmonic function $u$, defined via a supremum over sets of given measure, as the tool for extremal integral-means problems. The structural analogy is direct: convolution combines a function with a transformed copy of another, and the re-entry of a prohibition law is formally a self-application of a constraint — the case where the two operands coincide.

**[7] The prior reconciled analysis.** This work asks whether the re-entry form of the calculus of indications can simultaneously function as a binary prohibition law, reconciling three independent analyses that produced different formal conventions by adopting the strictest as primary [7]. Its results section reports exactly the counts re-derived here: $1$ of $4$ unary laws satisfies the prohibition condition, the unique law has no fixed point and period $T_{2} = 2$, exactly $2$ of $27$ ternary laws satisfy it (the two $3$-cycles, each of period $3$), the density ratio is $27/8 = 3.375$, and the entropy increment is $\log_{2} 3 - 1 = 0.5849625$ bits. Its discussion states that the primary impossibility result is definitional, not empirical, and that a different reading of "prohibition law" changes the result class entirely, since the forbidden-word model admits settled configurations such as the all-zeros sequence. The present paper re-derives these numbers with every arithmetic step shown, adds the applied reading, and states the falsification conditions explicitly.

## 3. Methods

### 3.1 Formal objects (primary convention)

Let $B_{2} = \{0, 1\}$ denote the two-element Boole algebra, where $1$ is the marked state and $0$ the unmarked state. A **unary law** is a total function $f : B_{2} \to B_{2}$; there are

$$N_{2} = |B_{2}|^{|B_{2}|} = 2^{2} = 4.$$

A **binary prohibition law** (primary convention, following [7]) is a unary law satisfying

$$\forall x \in B_{2}: \quad f(x) \neq x. \tag{P}$$

That is, the law forbids each state as an output: no state is self-consistent under the law. A **re-entry** of $f$ is the discrete dynamical system generated by iterating $f$ from $x_{0} \in B_{2}$: the orbit $x_{n+1} = f(x_{n})$. The re-entry **settles** if the orbit reaches a fixed point $x^{*}$ with $f(x^{*}) = x^{*}$; otherwise it is periodic with period $T_{f} \geq 2$, where $T_{f}$ is the minimal positive integer with $f^{T_{f}}(x_{0}) = x_{0}$.

### 3.2 Three-outcome extension

Following the three-outcome completion of [7], extend the state space to

$$S_{3} = \{m, u, v\},$$

where $m$ is marked, $u$ unmarked, and $v$ the void/oscillating outcome. Per the convention adopted in [7], $v$ is **not a value**: it is an outcome of the dynamics, not a truth-value the law may output as a settled verdict. A ternary law is a total function $g : S_{3} \to S_{3}$; there are $N_{3} = |S_{3}|^{|S_{3}|} = 3^{3} = 27$. A ternary prohibition law satisfies (P) on $S_{3}$, i.e., $g$ is a derangement of $S_{3}$ (a permutation with no fixed point).

### 3.3 Secondary convention (forbidden-word model)

A second reading, retained in [7] as a clearly labeled secondary model, defines a prohibition law instead as a **forbidden-word constraint**: a set $P \subseteq B_{2}^{k}$ of forbidden words, with a sequence $s \in B_{2}^{n}$ admissible if no length-$k$ contiguous block lies in $P$. We retain this as a secondary model with the canonical single prohibition $P = \{11\}$ (order $k = 2$): the mark may not indicate itself in adjacent positions. The two conventions differ in kind: the primary one constrains functions, the secondary one constrains sequences.

### 3.4 Measures

We compare settings by: (i) **density of prohibition laws**, $\rho_{2}$ and $\rho_{3}$, as fractions of all laws satisfying (P); (ii) **orbit period** $T_{f}$; (iii) **uniform outcome entropy**, $H_{k} = \log_{2} k = \ln k / \ln 2$ bits for $k$ equiprobable outcomes; (iv) for the secondary model, **survival ratio** $\rho_{n} = |A_{n}| / 2^{n}$ and capacity $C_{n} = \log_{2} |A_{n}|$, where $A_{n}$ is the set of admissible sequences of length $n$.

All computations are finite enumerations or closed-form evaluations. No simulation and no empirical data are used.

## 4. Analysis

Every input number is either a definition (Sections 3.1–3.3), an initial condition stated below, or a standard closed-form constant computed from its defining expression.

### 4.1 Enumeration of unary laws on $B_{2}$

Every unary law is determined by the pair $(f(0), f(1))$, each entry in $\{0, 1\}$, giving $N_{2} = 2^{2} = 4$ laws:

$$
\begin{aligned}
f_{\text{id}} &: (0, 1) \quad \text{(identity)}, \\
f_{\text{not}} &: (1, 0) \quad \text{(negation)}, \\
f_{\text{c0}} &: (0, 0) \quad \text{(constant } 0\text{)}, \\
f_{\text{c1}} &: (1, 1) \quad \text{(constant } 1\text{)}.
\end{aligned}
$$

Apply (P), $f(x) \neq x$ for all $x \in \{0, 1\}$:

- $f_{\text{id}}$: $f_{\text{id}}(0) = 0$ — fails at $x = 0$.
- $f_{\text{not}}$: $f_{\text{not}}(0) = 1 \neq 0$ and $f_{\text{not}}(1) = 0 \neq 1$ — **passes**.
- $f_{\text{c0}}$: $f_{\text{c0}}(0) = 0$ — fails at $x = 0$.
- $f_{\text{c1}}$: $f_{\text{c1}}(1) = 1$ — fails at $x = 1$.

**Result 4.1.** Exactly $1$ of $4$ unary laws is a binary prohibition law: $\rho_{2} = 1/4 = 0.25$, and it is the negation.

### 4.2 Re-entry of the prohibition law

Iterating $f_{\text{not}}$ from $x_{0} = 0$: $x_{1} = 1$, $x_{2} = 0$, $x_{3} = 1$, and so on. From $x_{0} = 1$ the same cycle is traversed in reverse phase. Fixed points require $f_{\text{not}}(x) = x$, i.e., $1 - x = x$, i.e., $2x = 1$ over $\{0, 1\}$: no solution, since $2 \cdot 0 = 0 \neq 1$ and $2 \cdot 1 = 2 \neq 1$. The orbit period is

$$T_{\text{not}} = 2.$$

For contrast, count fixed points across all four laws: $f_{\text{id}}$ has $2$, $f_{\text{c0}}$ has $1$, $f_{\text{c1}}$ has $1$, $f_{\text{not}}$ has $0$; the total is $2 + 1 + 1 + 0 = 4$, averaging $4/4 = 1$ fixed point per law. The prohibition law is the unique law with zero.

**Result 4.2.** The unique binary prohibition law, under re-entry, has no fixed point and period $T_{2} = 2$. A settled binary prohibition re-entry is impossible on $B_{2}$: the prohibition is enforced only by perpetual oscillation, and the moment the form settles it ceases to prohibit.

### 4.3 Three-outcome prohibition laws

On $S_{3} = \{m, u, v\}$, a law satisfying (P) must map each of the $3$ elements to one of the $2$ others; such a map is necessarily a bijection (a derangement), since if two elements shared an image the pigeonhole principle would force some element to map to itself. The number of derangements of a $3$-set is

$$!3 = 3! \sum_{k=0}^{3} \frac{(-1)^{k}}{k!} = 6 \left(1 - 1 + \frac{1}{2} - \frac{1}{6}\right).$$

Step by step: $1 - 1 = 0$; $0 + \frac{1}{2} = \frac{1}{2}$; $\frac{1}{2} - \frac{1}{6} = \frac{3}{6} - \frac{1}{6} = \frac{2}{6} = \frac{1}{3}$; $6 \cdot \frac{1}{3} = 2$. The two derangements are the two $3$-cycles:

$$g_{+} = (m \to u \to v \to m), \qquad g_{-} = (m \to v \to u \to m).$$

Both have orbit period $T_{3} = 3$ for every initial state, and neither has a fixed point.

**Result 4.3.** Exactly $2$ of $27$ ternary laws are prohibition laws: $\rho_{3} = 2/27 \approx 7.41 \times 10^{-2}$. Prohibition remains unsatisfiable as a settled state — every prohibition law is a cycle — but it is now generically realized as dynamics: every initial state lies on the prohibition orbit.

### 4.4 Comparative measures

**Density ratio.**

$$\frac{\rho_{2}}{\rho_{3}} = \frac{1/4}{2/27} = \frac{1}{4} \cdot \frac{27}{2} = \frac{27}{8} = 3.375.$$

Admitting the void as a non-valued outcome makes prohibition laws $3.375$-fold sparser among all laws, but makes every state subject to prohibition as dynamics.

**Entropy.** For a uniform distribution over the two values of $B_{2}$:

$$H_{2} = \log_{2} 2 = \frac{\ln 2}{\ln 2} = 1 \text{ bit}.$$

Over the three outcomes of $S_{3}$, using $\ln 3 = 1.0986123$ and $\ln 2 = 0.6931472$:

$$H_{3} = \log_{2} 3 = \frac{1.0986123}{0.6931472} = 1.5849625 \text{ bits}.$$

The entropy increment is

$$\Delta H = H_{3} - H_{2} = 1.5849625 - 1 = 0.5849625 \text{ bits}.$$

This is the informational price of the third outcome that makes prohibition dynamically coherent.

**Period growth.** The minimal prohibition orbit grows from $T_{2} = 2$ to $T_{3} = 3$, a factor $3/2 = 1.5$.

### 4.5 Summary of inputs for the primary model

The derivation chain uses only: $|B_{2}| = 2$ and $|S_{3}| = 3$ (definitional); the condition (P) (definitional); the derangement formula and entropy formula (closed-form). No empirical, simulated, or externally sourced number enters the chain, as the prior reconciled analysis also records [7].

### 4.6 Secondary model: forbidden-word prohibition $P = \{11\}$

**Inputs.** Initial conditions $a_{1} = 2$, $a_{2} = 3$ (of the four length-2 words $\{00, 01, 10, 11\}$, the word $11$ is forbidden, leaving $3$); recurrence from partitioning admissible sequences by their final symbol gives $a_{n} = a_{n-1} + a_{n-2}$ (the Fibonacci recurrence).

**Step 1: iterate the recurrence.**

$$a_{3} = 3 + 2 = 5, \quad a_{4} = 5 + 3 = 8, \quad a_{5} = 8 + 5 = 13, \quad a_{6} = 13 + 8 = 21,$$
$$a_{7} = 21 + 13 = 34, \quad a_{8} = 34 + 21 = 55, \quad a_{9} = 55 + 34 = 89, \quad a_{10} = 89 + 55 = 144.$$

**Step 2: survival ratio.** Raw states: $2^{10} = 1024$. Therefore

$$\rho_{10} = \frac{144}{1024} = 0.140625.$$

**Step 3: capacity under uniform coding.** With $144 = 12^{2}$ and $\ln 4 = 1.3862944$, $\ln 3 = 1.0986123$:

$$\ln 144 = 2 \ln 12 = 2(\ln 4 + \ln 3) = 2(1.3862944 + 1.0986123) = 4.9698134,$$
$$C_{10} = \frac{4.9698134}{0.6931472} = 7.1699250 \text{ bits}, \qquad \Delta C_{10} = 10 - 7.1699250 = 2.8300750 \text{ bits}.$$

**Step 4: asymptotic capacity.** The characteristic equation $x^{2} - x - 1 = 0$ has roots $\varphi = (1 + \sqrt{5})/2$ and $\psi = (1 - \sqrt{5})/2$. With $\sqrt{5} \approx 2.2360680$: $\varphi = 1.6180340$, $\psi = -0.6180340$. Since $a_{n} \sim c\,\varphi^{n}$, the asymptotic per-symbol capacity is

$$c_{\infty} = \log_{2} \varphi = \frac{\ln 1.6180340}{0.6931472} = \frac{0.4812118}{0.6931472} = 0.6942419 \text{ bits per symbol},$$

against $1$ bit per symbol unconstrained; asymptotic loss $1 - 0.6942419 = 0.3057581$ bits per symbol. Consistency check: the finite-$n$ per-symbol capacity $C_{10}/10 = 0.7169925$ exceeds $c_{\infty} = 0.6942419$, as expected since boundary effects relax the constraint at small $n$.

**Step 5: pair-level coincidence.** The prohibition removes one of the four length-2 configurations, leaving $3$ admissible pairs, with per-pair capacity

$$\log_{2} 3 = \frac{1.0986123}{0.6931472} = 1.5849625 \text{ bits},$$

identical to $H_{3}$ of the three-outcome algebra. This is the secondary model's central observation, recorded in [7]: the three-outcome re-entry algebra and the pair-level survival count under $P = \{11\}$ both assign $\log_{2} 3$ bits to one act of distinction.

**Step 6: generalization to $j$ forbidden pairs.** With $j$ of the $4$ pairs forbidden, pair-level capacity is $\log_{2}(4 - j)$: $j = 1$ gives $\log_{2} 3 = 1.5850$; $j = 2$ gives $\log_{2} 2 = 1$; $j = 3$ gives $\log_{2} 1 = 0$; $j = 4$ is undefined (no admissible pairs). A prohibition law that forbids everything permits nothing.

## 5. Results

All numbers below are exactly those computed with shown arithmetic in Section 4; none are empirical, simulated, or projected.

- **R1 (Section 4.1).** Exactly $1$ of the $N_{2} = 4$ unary laws on $B_{2}$ satisfies the prohibition condition (P): the negation. Density $\rho_{2} = 1/4 = 0.25$.
- **R2 (Section 4.2).** The unique binary prohibition law has no fixed point ($2x = 1$ has no solution in $\{0, 1\}$) and orbit period $T_{2} = 2$. A settled binary prohibition re-entry is impossible on $B_{2}$.
- **R3 (Section 4.3).** Exactly $2$ of the $N_{3} = 27$ ternary laws on $S_{3}$ satisfy (P): the two $3$-cycles $g_{+}$ and $g_{-}$, each of period $T_{3} = 3$ for every initial state. Density $\rho_{3} = 2/27 \approx 7.41 \times 10^{-2}$.
- **R4 (Section 4.4).** Density ratio $\rho_{2}/\rho_{3} = 27/8 = 3.375$; entropy increment $\Delta H = 0.5849625$ bits; period growth factor $3/2 = 1.5$.
- **R5 (Section 4.6).** Forbidden-word model with $P = \{11\}$: $a_{10} = 144$, survival ratio $\rho_{10} = 0.140625$, capacity $C_{10} = 7.1699250$ bits, capacity deficit $\Delta C_{10} = 2.8300750$ bits, asymptotic capacity $c_{\infty} = 0.6942419$ bits per symbol, and pair-level capacity $\log_{2} 3 = 1.5849625$ bits, identical to $H_{3}$.
- **R6 (Section 4.6, Step 6).** With $j$ forbidden pairs, pair-level capacity is $\log_{2}(4 - j)$, decreasing from $1.5850$ bits ($j = 1$) to $0$ ($j = 3$).

## 6. Discussion

**The result is definitional, not empirical.** The impossibility result R2 follows from the strict convention (P) and the size of $B_{2}$; as the prior reconciled analysis states, a different reading of "prohibition law" changes the result class entirely, since the forbidden-word model admits settled configurations such as the all-zeros sequence [7]. The three-outcome extension treats $v$ as a non-valued void per the convention of [7]; if $v$ were admitted as a truth-value, the interpretation of R3 would change, though the combinatorial count $!3 = 2$ remains.

**Limitations.** The result rests on the following assumptions, with sensitivity noted for each:

1. **The derangement convention (P).** The entire impossibility claim is definitional; under the forbidden-word convention, settled admissible configurations exist (e.g., $000\ldots$), so R2 does not transfer. Sensitivity: total.
2. **Two-element state space.** On $B_{2}$ exactly one law satisfies (P). On larger binary domains ($|B| = n \geq 2$) derangements exist for all $n \geq 2$ and none has a fixed point, so the no-settlement property generalizes, but the uniqueness claim does not.
3. **The void $v$ as non-valued.** If $v$ is a value, R3's interpretation as "prohibition as dynamics" weakens; the count $!3 = 2$ is unaffected.
4. **Single forbidden pair in the secondary model.** Additional forbidden pairs change the capacity per R6; the coincidence $\log_{2} 3 = H_{3}$ holds only for $j = 1$.
5. **Uniform outcome entropy.** $\Delta H = 0.5849625$ bits assumes equiprobable outcomes; non-uniform distributions give different increments.
6. **No empirical component.** No measurement, simulation, or external dataset enters any derivation; the work is purely analytical.

**Falsification conditions.** R2 would be falsified by exhibiting a total function $f : B_{2} \to B_{2}$ with $f(x) \neq x$ for all $x$ that possesses a fixed point under iteration; such a function cannot exist on a two-element set, so the claim is robust within its convention. R3 would be falsified by finding a third derangement of $S_{3}$; the pigeonhole argument guarantees exactly two. R5 would be falsified by enumerating length-$10$ binary strings avoiding $11$ and obtaining a count different from $144$; the Fibonacci recurrence with the stated initial conditions determines the count exactly. The observation that would falsify the main result in practice is a hardware or software implementation of a self-applied binary prohibition that reaches a stable output without external intervention while still satisfying (P) — since (P) forbids any fixed point on $B_{2}$, such an implementation would show that the implemented rule is not the law $f_{\text{not}}$, i.e., that the convention was violated, which is itself the practical point of the result.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result, and what changes.** The result is foundational: it is a statement about a two-element formal system, and no named engineering team today builds a product around the calculus of indications. Three user groups nevertheless have decisions it bears on. First, verification engineers who validate self-modifying code — the setting of cozy, which symbolically executes an original and an instrumented binary and asserts that register and memory contents agree across compatible state pairs [3] — currently treat "the patched function settles into the same behavior" as the success criterion. If the paper's R2 holds, a rule that forbids its own input on a two-element domain cannot settle at all, so a verification target that is genuinely self-prohibiting must be specified as an orbit property (period $T_{2} = 2$, no fixed point) rather than a stable output; the acceptance criterion in the verification harness changes from a fixed-point check to a cycle check. Second, designers of watchdog or monitor circuits who hope to enforce a prohibition with a single self-applied binary rule learn from R2 and R3 that either a third signal level (the $S_{3}$ completion, at density $2/27$ and entropy cost $\Delta H = 0.5849625$ bits) or an external monitor outside the prohibited subsystem is required; the design parameter that changes is the state-space size budgeted for the enforcement mechanism. Third, formal-methods researchers studying re-entering or self-referential definitions gain an exact density figure ($\rho_{2} = 0.25$ versus $\rho_{3} = 2/27 \approx 7.41 \times 10^{-2}$) to use as a baseline when counting how rare self-forbidding laws are as the state space grows.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is purely analytical, has not been peer reviewed, and uses no empirical data: it sits at TRL 1 (basic principles observed and reported) with elements of TRL 2 (technology concept formulated) insofar as the three-outcome completion suggests a concrete design alternative. Analytical work of this kind cannot exceed TRL 3, and nothing in this paper has been exercised in hardware, simulation, or even prototype software; no claim of implementation readiness is made.

**(c) The smallest next experiment.** The cheapest de-risking step is a software one: implement the two-element law $f_{\text{not}}$ and the two ternary cycles $g_{+}$ and $g_{-}$ as explicit transition tables, iterate them from every initial state, and assert (i) no fixed point is ever reached and (ii) the observed periods are exactly $T_{2} = 2$ and $T_{3} = 3$. This is a finite check over $2 + 3 = 5$ initial states and would falsify R2 or R3 if any orbit settled or any period differed. The outcome that refutes the framework is an orbit that settles while the transition table still satisfies $f(x) \neq x$ for all $x$; since Section 4.2 shows the fixed-point equation $2x = 1$ has no solution on $\{0, 1\}$, such an outcome would indicate an implementation error rather than a genuine counterexample, which is itself the diagnostic value of the result. A second, slightly larger step is to encode the forbidden-word constraint $P = \{11\}$ in a model checker and confirm by exhaustive search over all $2^{10} = 1024$ length-$10$ sequences that exactly $a_{10} = 144$ are admissible, matching the Fibonacci recurrence of Section 4.6.

**(d) Binding constraints.** For any eventual hardware realization of the three-outcome completion, the first constraint to bind is representational: a third signal level ($v$) requires a physical encoding that standard two-level logic does not provide, and the convention adopted here — that $v$ is an outcome and not a value — must be preserved by the encoding, or the interpretation of R3 collapses (Section 6, limitation 3). The second is verification-tooling capacity: symbolic execution of self-modifying code is already the cost driver in the cozy workflow, with per-function symbolic execution times reported from $0.0092$ s to $16.0683$ s [3]; adding a cycle-property acceptance criterion multiplies the states to explore, though the two-element and three-element cases here are small enough that exhaustive enumeration suffices. Whether larger state spaces remain exhaustively enumerable is an open question: the count of ternary laws is $N_{3} = 27$, but the count on a state space of size $k$ is $k^{k}$, which grows rapidly and would force sampling rather than enumeration. Regulatory or manufacturing constraints do not bind at this stage; the work has no hardware artifact.

**(e) Order-of-magnitude bounds.** No cost or performance projection is offered beyond what Section 4 derives, because the paper contains no empirical cost inputs. The only quantitative bounds available are the derived ones: the entropy overhead of the three-outcome completion is $\Delta H = 0.5849625$ bits per act of distinction (a $0.5849625/1 = 58.49625\%$ increase over the two-outcome channel under uniform coding), and the asymptotic capacity loss under the single-pair prohibition is $0.3057581$ bits per symbol (Section 4.6, Step 4). Any engineering cost figure (gates, latency, energy) would require a physical encoding of $v$ that does not yet exist and is listed as an open question.

**(f) Risks and misuse paths.** The main misuse is overclaiming: the impossibility R2 is definitional under the convention (P), and quoting it as an empirical statement about real systems that "cannot settle" would be wrong, since the forbidden-word convention of Section 3.3 admits settled configurations such as the all-zeros sequence. A second misuse is reading the pair-level identity $\log_{2} 3 = H_{3}$ as evidence of a shared mechanism; Section 6 records it as an observation, and Step 6 of Section 4.6 shows it is fragile (it fails already at $j = 2$ forbidden pairs).

## 8. Conclusion

Under the strictest reconciled convention, a binary prohibition law exists uniquely — the negation, $1$ of the $4$ unary laws on $B_{2}$, at density $\rho_{2} = 0.25$ — and under re-entry it can never settle: it enforces itself only as a period-$T_{2} = 2$ oscillation with no fixed point, so a settled binary prohibition re-entry is impossible on $B_{2}$. Admitting a third, non-valued outcome $v$ makes prohibition dynamically coherent — exactly $2$ of $27$ ternary laws satisfy the prohibition condition, both $3$-cycles of period $T_{3} = 3$ covering every initial state — at a density cost of a factor $27/8 = 3.375$ and an entropy cost of $\Delta H = 0.5849625$ bits. A secondary forbidden-word model with the single prohibition $P = \{11\}$ leaves $a_{10} = 144$ of $1024$ length-$10$ sequences admissible, at survival ratio $0.140625$ and asymptotic capacity $c_{\infty} = 0.6942419$ bits per symbol, and independently reproduces the three-outcome capacity $\log_{2} 3 = 1.5849625$ bits at the pair level. Every quantity is derived by explicit finite enumeration or closed-form evaluation with all arithmetic shown; the paper uses no empirical data. The practical reading is that a self-applied binary prohibition is guaranteed either to oscillate forever or to be something other than a prohibition law, and that guaranteeing prohibition as a settled outcome requires a third outcome or an external monitor — a conclusion that is exact within its convention, and whose limits the falsification conditions of Section 6 make precise.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 11 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] A stability analysis of the power-law steady state of marine size spectra. arXiv:1001.3826v3. https://arxiv.org/abs/1001.3826v3
[2] Plankton: the paradox and the power law. arXiv:1705.05327v1. https://arxiv.org/abs/1705.05327v1
[3] cozy: Comparative Symbolic Execution for Binary Programs. arXiv:2504.00151v1. https://arxiv.org/abs/2504.00151v1
[4] Evolutionary Memory in Binary Systems?. arXiv:astro-ph/0412185v1. https://arxiv.org/abs/astro-ph/0412185v1
[5] Two-dimensional correlation function of binary black hole coalescences. arXiv:2005.06004v2. https://arxiv.org/abs/2005.06004v2
[6] Integral means inequalities, convolution, and univalent functions. arXiv:1902.01595v1. https://arxiv.org/abs/1902.01595v1
[7] QNFO: Re-Entry as a Binary Prohibition Law: A Reconciled Formal Analysis of Two Conventions
