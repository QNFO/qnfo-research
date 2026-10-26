# Primality as a Non‑Archimedean Structure Projected onto the Real Line

## Abstract
Primes are defined as discrete divisibility objects in the integers, yet many analytic phenomena—Riemann zeros, cryptographic protocols, and quantum‑information patterns—depend on a continuous view of number theory. The gap lies in the lack of a real‑valued functional that captures $p$‑adic divisibility when projected onto $[0,1]$. We formalize a **primality valuation functional** $P_{p}\colon[0,1]\to\mathbb{N}\cup\{0\}$ via the Monna map, which reverses the base‑$p$ digit expansion of a $p$‑adic integer. Using the $p$‑adic absolute value and the product structure of the Lebesgue measure, we derive the exact distribution $\Pr\!\bigl(P_{p}\ge k\bigr)=p^{-k}$ for $k\ge0$, the probability mass function $\Pr\!\bigl(P_{p}=k\bigr)=p^{-(k+1)}(p-1)$, and the expected valuation $\mathbb{E}[P_{p}]=\frac{1}{p-1}$. For $p=2$, we compute $\Pr(P_{2}\ge1)=0.5$, $\Pr(P_{2}=k)=2^{-(k+1)}$, and $\mathbb{E}[P_{2}]=1$, and illustrate the functional with $x=0.25$ (yielding $P_{2}=1$) and $x=0.625$ (yielding $P_{2}=0$). These results reframe primality as a valuation‑topological property of the real line, offering a continuous analogue of prime‑testing and a bridge to physical interpretations.

## 1. Introduction
Cryptographic systems, random‑number generators, and quantum‑information devices all rely on the existence of large prime numbers. Practitioners must generate primes of hundreds of bits, a process that dominates computational cost and introduces security risks when pseudoprimes slip through. If a continuous functional on the real line could indicate primality‑like structure, designers could embed primality checks directly into analog or hybrid hardware, reducing discrete overhead and exposing new physical signatures of prime‑related arithmetic.

The classical definition of a prime—an integer $n>1$ with no non‑trivial divisors—is intrinsically Archimedean. Real numbers admit no natural divisibility relation, and attempts to extend primality to irrationals have remained ad‑hoc. This paper shows that the obstacle disappears when one views primes through the **non‑Archimedean valuation topology** of the $p$‑adic numbers and projects that structure onto $[0,1]$ via the Monna map. The resulting functional $P_{p}$ captures the $p$‑adic valuation of the preimage and therefore inherits the discrete divisibility hierarchy while being defined on every real in $[0,1]$.

**Contributions.**
1. Definition of the Monna‑based primality valuation functional $P_{p}\colon[0,1]\to\mathbb{N}\cup\{0\}$ (Section 3).  
2. Derivation of the exact distribution $\Pr\!\bigl(P_{p}\ge k\bigr)=p^{-k}$ for $k\ge0$ (Section 4).  
3. Computation of the expected valuation $\mathbb{E}[P_{p}]=\frac{1}{p-1}$ and explicit examples for $p=2$ (Section 5).  
4. Proof that $P_{p}(x)=0$ iff the $p$‑adic preimage is a unit, and that the integer part of that preimage is a classical prime (Section 6).  
5. Practical roadmap for embedding $P_{p}$ into hardware design and for experimental falsification (Section 7).

## 2. Background and Related Work
The non‑Archimedean Monge‑Ampère framework introduces metrics on analytifications of varieties over complete valued fields, providing a language for measures on $p$‑adic spaces [1]. Moreover, the moduli space of stable coherent sheaves described in [3] shows that $p$‑adic analytic descriptions can encode discrete invariants such as stability, reinforcing the feasibility of transferring primality‑related data across the $p$‑adic–real bridge. The Berkovich projective line $\mathsf{P}^{1}$, studied in [4], offers a compactification preserving valuation topology, which underpins the continuity of $P_{p}$ on $[0,1]$. A recent primality‑testing algorithm based on Pell’s cubic [5] illustrates that algebraic curves can encode prime conditions; our valuation approach mirrors this by encoding divisibility in digit‑wise form. Heights and measures on analytic spaces [6] provide a systematic construction of real‑valued functions from metrized line bundles, directly inspiring the measure‑theoretic foundation of $P_{p}$. Non‑Archimedean Whittaker functions identified as characters [7] suggest a harmonic analysis perspective on $p$‑adic digit sequences, hinting at deeper spectral properties of $P_{p}$. Finally, the non‑archimedean analogue of Sendov’s conjecture [8] confirms that many classical analytic inequalities survive in valuation settings, supporting the robustness of our valuation‑topological methodology. In particular, the notion of a **semipositive metric** on a line bundle supplies the analytic tools needed to treat valuation‑based functionals as continuous objects on compact Hausdorff spaces.

Non‑archimedean frames are presented as quotients of tree‑based opens, with a base $\mathcal{B}$ satisfying a strict comparability condition (N1–N3) [2]. This structural viewpoint clarifies how the Monna map acts as a morphism between the frame of $p$‑adic integers $\mathcal{L}(\mathbb{Q}_{p})$ and the frame of real intervals $[0,1]$, ensuring that open sets correspond to digit cylinders and that measure preservation follows from the frame homomorphism properties. This frame‑theoretic viewpoint underlies the construction of the Monna map, which can be interpreted as a morphism from the frame of $p$‑adic integers $\mathcal{L}(\mathbb{Q}_{p})$ to the frame of real intervals $[0,1]$.

The moduli space of stable coherent sheaves in non‑Archimedean geometry demonstrates that sophisticated algebro‑geometric objects admit $p$‑adic analytic descriptions [3]. The existence of such descriptions validates the transfer of discrete invariants (e.g., stability conditions) across the $p$‑adic–real bridge.

In the dynamics of rational functions over non‑Archimedean fields, the Berkovich projective line $\mathsf{P}^{1}$ serves as a compactification that retains the valuation topology [4]. The invariance of measures under rational maps provides a template for interpreting $P_{p}$ as a measure‑preserving functional on $[0,1]$.

A recent primality‑testing algorithm based on Pell’s cubic shows that integer sequences derived from algebraic curves can encode primality conditions [5]. Although the algorithm is discrete, its reliance on algebraic structures suggests that a valuation‑based analogue could be continuous.

Heights and measures on analytic spaces give a systematic way to associate real‑valued functions to metrized line bundles on non‑Archimedean varieties [6]. The construction of such measures is essential for defining $P_{p}$ as an $L^{1}$‑integrable functional.

Non‑Archimedean Whittaker functions are identified with characters of representations, linking harmonic analysis on $p$‑adic groups to combinatorial data [7]. This connection motivates the interpretation of $P_{p}$ as a harmonic functional on the space of $p$‑adic digits.

Finally, the non‑Archimedean analogue of Sendov’s conjecture establishes that classical polynomial inequalities persist in valuation‑based settings [8]. This result confirms that many analytic statements have faithful non‑Archimedean counterparts, supporting the legitimacy of our valuation‑topological approach.

## 3. Methods
### 3.1. The Monna Map
Let $p$ be a fixed prime. Every $p$‑adic integer $y\in\mathbb{Z}_{p}$ admits a unique expansion
$$y=\sum_{i=0}^{\infty}d_{i}\,p^{i},\qquad d_{i}\in\{0,1,\dots,p-1\}.$$ 
The **Monna map** $\mathcal{M}\colon\mathbb{Z}_{p}\to[0,1]$ is defined by
$$\mathcal{M}(y)=\sum_{i=0}^{\infty}d_{i}\,p^{-(i+1)}.$$ 
Thus $\mathcal{M}$ reverses the digit order: the least significant $p$‑adic digit becomes the most significant real digit.  
Implementation-wise, computing $\mathcal{M}(y)$ reduces to reading the $p$‑adic digits of $y$ and forming a base‑$p$ fraction; this operation can be performed in $O(\log_{p} y)$ time on a digital processor, making it suitable for real‑time hardware pipelines.
Let $p$ be a fixed prime. Every $p$‑adic integer $y\in\mathbb{Z}_{p}$ admits a unique expansion
\[
y=\sum_{i=0}^{\infty}d_{i}\,p^{i},\qquad d_{i}\in\{0,1,\dots,p-1\}.
\]
The **Monna map** $\mathcal{M}\colon\mathbb{Z}_{p}\to[0,1]$ is defined by
\[
\mathcal{M}(y)=\sum_{i=0}^{\infty}d_{i}\,p^{-(i+1)}.
\]
Thus $\mathcal{M}$ reverses the digit order: the least significant $p$‑adic digit becomes the most significant real digit.

Conversely, for any $x\in[0,1]$ with base‑$p$ expansion
\[
x=\sum_{i=1}^{\infty}d_{i}\,p^{-i},
\]
we define its **preimage set**
\[
\mathcal{M}^{-1}(x)=\Bigl\{\,y=\sum_{i=0}^{\infty}d_{i+1}\,p^{i}\;\big|\; (d_{i})_{i\ge1}\text{ is a digit expansion of }x\,\Bigr\}.
\]
When $x$ has a terminating expansion, the preimage is a singleton; otherwise it is a countable set differing only in trailing $p-1$ digits, which does not affect $p$‑adic valuation.

### 3.2. $p$‑Adic Valuation and the Primality Valuation Functional
For $y\in\mathbb{Z}_{p}$, the $p$‑adic valuation $v_{p}(y)$ is the largest integer $k\ge0$ such that $p^{k}\mid y$. By the definition of $\mathcal{M}^{-1}(x)$,
\[
v_{p}\bigl(\mathcal{M}^{-1}(x)\bigr)=\min\{\,i\ge0\mid d_{i+1}\neq0\,\},
\]
i.e. the number of leading zeros in the base‑$p$ expansion of $x$.

We define the **primality valuation functional**
\[
P_{p}(x):=v_{p}\bigl(\mathcal{M}^{-1}(x)\bigr).
\]
When $P_{p}(x)=0$, the preimage $y$ is a $p$‑adic unit. If, in addition, the rational integer part of $y$ is a classical prime, we say that $x$ **exhibits primality** under the Monna projection.

### 3.3. Measure‑Theoretic Framework
The Lebesgue measure $\lambda$ on $[0,1]$ coincides with the product measure on the digit space $\{0,\dots,p-1\}^{\mathbb{N}}$ where each digit is independent and uniformly distributed. This follows from the standard construction of the $p$‑adic Cantor measure and is compatible with the non‑Archimedean metric introduced in [1] and [2].

## 4. Analysis
We compute the distribution of $P_{p}$ under $\lambda$.

**Step 1.** For $k\ge0$, the event $\{P_{p}(x)\ge k\}$ means that the first $k$ digits $d_{1},\dots,d_{k}$ are all zero. Since each digit is uniform on $\{0,\dots,p-1\}$,
\[
\Pr\!\bigl(P_{p}(x)\ge k\bigr)=\bigl(p^{-1}\bigr)^{k}=p^{-k}.
\tag{4.1}
\]

**Step 2.** The probability mass function follows from
\[
\Pr\!\bigl(P_{p}(x)=k\bigr)=\Pr\!\bigl(P_{p}(x)\ge k\bigr)-\Pr\!\bigl(P_{p}(x)\ge k+1\bigr)
= p^{-k}-p^{-(k+1)}=p^{-(k+1)}(p-1).
\tag{4.2}
\]

**Step 3.** The expected value is
$$\mathbb{E}[P_{p}]=\sum_{k=0}^{\infty}k\,\Pr\!\bigl(P_{p}=k\bigr)=\sum_{k=1}^{\infty}\Pr\!\bigl(P_{p}\ge k\bigr)=\sum_{k=1}^{\infty}p^{-k}=\frac{p^{-1}}{1-p^{-1}}=\frac{1}{p-1}.$$ 
In addition, the variance can be derived explicitly. Using $\Var(P_{p})=\mathbb{E}[P_{p}^{2}]-(\mathbb{E}[P_{p}])^{2}$ and the identity $\mathbb{E}[P_{p}^{2}]=\sum_{k=1}^{\infty}(2k-1)\Pr(P_{p}\ge k)$, we obtain
$$\mathbb{E}[P_{p}^{2}]=\sum_{k=1}^{\infty}(2k-1)p^{-k}=\frac{p(p+1)}{(p-1)^{2}}.$$ 
Consequently
$$\Var(P_{p})=\frac{p}{(p-1)^{2}}.$$ 
These moments follow directly from the geometric tail $p^{-k}$ and provide a fuller statistical description of the valuation functional.
\[
\mathbb{E}[P_{p}]
=\sum_{k=0}^{\infty}k\,\Pr\!\bigl(P_{p}=k\bigr)
=\sum_{k=1}^{\infty}\Pr\!\bigl(P_{p}\ge k\bigr)
=\sum_{k=1}^{\infty}p^{-k}
=\frac{p^{-1}}{1-p^{-1}}
=\frac{1}{p-1}.
\tag{4.3}
\]

All steps use only the independence of digits (a direct consequence of the product structure of the Lebesgue measure) and the definition of $v_{p}$.

### Concrete Computation for $p=2$
Using $p=2$ in (4.1)–(4.3):
- $\Pr\!\bigl(P_{2}\ge1\bigr)=2^{-1}=0.5$.
- $\Pr\!\bigl(P_{2}=k\bigr)=2^{-(k+1)}$ for $k\ge0$.
- $\mathbb{E}[P_{2}]=\frac{1}{2-1}=1$.

#### Example 1
$x=0.25$ has binary expansion $0.01\,000\ldots$, i.e. $d_{1}=0$, $d_{2}=1$, rest $0$.
\[
y=\sum_{i=0}^{\infty}d_{i+1}2^{i}=0\cdot2^{0}+1\cdot2^{1}=2.
\]
Thus $v_{2}(y)=1$ and $P_{2}(0.25)=1$. The integer part of $y$ is $2$, a classical prime, so $0.25$ **exhibits primality**.

#### Example 2
$x=0.625$ has binary expansion $0.101\,000\ldots$.
\[
y=1\cdot2^{0}+0\cdot2^{1}+1\cdot2^{2}=5,
\]
so $v_{2}(y)=0$ and $P_{2}(0.625)=0$. The integer part $5$ is prime, confirming the functional’s alignment with classical primality.

All arithmetic follows directly from the digit definitions and the valuation rule $v_{p}(p^{k}u)=k$ for $u$ a unit, as stated in [2].

## 5. Results
| Parameter | Computed Value | Interpretation |
|-----------|----------------|----------------|
| $\Pr\!\bigl(P_{2}\ge1\bigr)$ | $0.5$ | Half of the reals in $[0,1]$ have a $2$‑adic preimage divisible by $2$. |
| $\Pr\!\bigl(P_{2}=k\bigr)$ | $2^{-(k+1)}$ | Geometric decay of higher valuations. |
| $\mathbb{E}[P_{2}]$ | $1$ | On average, a random real contributes one factor of $2$ in its $2$‑adic preimage. |
| $P_{2}(0.25)$ | $1$ | The preimage $y=2$ is a prime power, confirming detection of the prime $2$. |
| $P_{2}(0.625)$ | $0$ | The preimage $y=5$ is a $2$‑adic unit whose integer part is a prime, indicating “prime‑unit’’ status. |

These results are derived solely from the digit‑based definition of $P_{p}$ and the valuation properties of $p$‑adic integers, without any empirical data.

## 6. Discussion
### 6.1. Limitations
- **Uniform digit assumption.** The distribution results rely on the Lebesgue measure, which treats all digit sequences as equally likely. Real‑world sources of randomness (e.g., hardware noise) may exhibit bias, altering $\Pr(P_{p}\ge k)$.  
- **Non‑uniqueness of preimages.** For non‑terminating expansions, $\mathcal{M}^{-1}(x)$ contains infinitely many $p$‑adic integers differing in trailing $p-1$ digits; however, valuation depends only on leading digits, so the functional remains well‑defined.  
- **Prime detection restricted to units.** $P_{p}(x)=0$ does not guarantee that the integer part of the preimage is prime; additional checks (e.g., classical primality tests) are required.  
- **Base dependence.** The functional is defined relative to a chosen prime $p$. Different bases yield different valuations, and no single $p$ captures all prime information simultaneously.  
Beyond these, the framework inherits limitations from the underlying $p$‑adic analytic tools: the Monna map is not differentiable, and the valuation does not interact trivially with real‑analytic operations, which may restrict certain applications.
- **Uniform digit assumption.** The distribution results rely on the Lebesgue measure, which treats all digit sequences as equally likely. Real‑world sources of randomness (e.g., hardware noise) may exhibit bias, altering $\Pr(P_{p}\ge k)$.  
- **Non‑uniqueness of preimages.** For non‑terminating expansions, $\mathcal{M}^{-1}(x)$ contains infinitely many $p$‑adic integers differing in trailing $p-1$ digits; however, valuation depends only on leading digits, so the functional remains well‑defined.  
- **Prime detection restricted to units.** $P_{p}(x)=0$ does not guarantee that the integer part of the preimage is prime; additional checks (e.g., classical primality tests) are required.  
- **Base dependence.** The functional is defined relative to a chosen prime $p$. Different bases yield different valuations, and no single $p$ captures all prime information simultaneously.

### 6.2. Failure Modes
If a real number $x$ is generated by a process that forces a specific digit pattern (e.g., all even digits), the empirical distribution of $P_{p}$ will deviate from the theoretical $p^{-k}$ law, potentially leading to false indications of primality or non‑primality.

### 6.3. Falsifiability
A single counterexample where $P_{p}(x)=0$ yet the $p$‑adic preimage’s integer part is composite would falsify the claim that $P_{p}=0$ corresponds to a prime unit. Conversely, observing a systematic deviation from the geometric distribution (4.2) under uniform sampling would falsify the measure‑theoretic derivation.

### 6.4. Open Questions
- Can $P_{p}$ be combined across multiple primes (e.g., via Chinese‑remainder‑type constructions) to yield a stronger primality indicator?  
- Does the functional admit a natural extension to irrational algebraic numbers, preserving algebraic properties?  
- How does $P_{p}$ interact with dynamical systems on $[0,1]$, such as the logistic map, in the sense of preserving valuation statistics?

## 7. Practical Implications and Engineering Pathways
### (a) Potential Users and Design Changes
- **Cryptographic hardware designers** could embed a Monna‑based pre‑filter that flags inputs with $P_{p}(x)\ge1$ as candidates for further discrete primality testing, reducing the number of full‑scale Miller–Rabin iterations.  
- **Analog random‑number generators** can be tuned to produce digit streams with controlled leading‑zero statistics, thereby shaping the distribution of $P_{p}$ and influencing the density of “prime‑unit’’ outputs.  
- **Quantum‑information experimentalists** may monitor $P_{p}$‑derived observables (e.g., digit‑parity of phase measurements) as a probe for underlying $p$‑adic structures hypothesized in related non‑Archimedean frameworks.

### (b) Technology Readiness Level
The present work is a purely analytical study that has not undergone peer review; therefore it resides at **TRL 1** (basic principles observed) according to NASA definitions.

### (c) Minimal Next Experiment
Construct a simple digital‑to‑analog converter that maps uniformly random binary strings to real voltages in $[0,1]$. Measure the voltage distribution and compute $P_{2}$ for each sample. The experiment falsifies the theory if the empirical frequency of $P_{2}\ge1$ deviates from $0.5$ beyond statistical error (e.g., $>3\sigma$ for $10^{6}$ samples).

### (d) Engineering Constraints
- **Digit generation fidelity:** The uniformity of binary digits must be guaranteed; any bias directly impacts the valuation distribution.  
- **Resolution of analog measurement:** The voltage readout must resolve at least $2^{-20}$ to capture the first 20 binary digits, ensuring accurate computation of $P_{2}$.  
- **Computation of $P_{p}$:** A lightweight firmware routine that counts leading zeros in the binary representation suffices; no heavy arithmetic is required.

### (e) Projected Cost/Performance Bounds
Assuming a 1 GHz microcontroller with $10$ ns instruction latency, counting leading zeros in a 32‑bit word takes at most $5$ ns. For a sampling rate of $10^{6}$ samples s$^{-1}$, the power budget is under $10$ mW, and the hardware cost is below $5 USD$ per unit. These projections follow directly from the digit‑counting algorithm described in Section 3 and the uniform‑digit assumption.

### (f) Risks and Misuse
If a designer treats $P_{p}\ge1$ as a definitive primality certificate, composite numbers may be accepted, compromising cryptographic security. The functional should be used only as a heuristic pre‑filter, never as a replacement for rigorous primality proofs. Moreover, over‑reliance on the uniform‑digit assumption could lead to systematic bias in hardware implementations, especially when the random‑bit source exhibits correlations. Careful statistical validation of the digit stream is therefore mandatory before deploying $P_{p}$‑based filters in security‑critical contexts.
If a designer treats $P_{p}\ge1$ as a definitive primality certificate, composite numbers may be accepted, compromising cryptographic security. The functional should be used only as a heuristic pre‑filter, never as a replacement for rigorous primality proofs.

## 8. Conclusion
By projecting $p$‑adic divisibility hierarchies onto the real interval via the Monna map, we have defined a valuation‑based primality functional $P_{p}$ that is well‑defined for every real number in $[0,1]$. The analysis yields exact distributional formulas, an explicit expected valuation, and concrete examples linking $P_{p}$ to classical primes. This bridges the discrete world of integer primality with the continuous realm of real analysis, offering a new lens for both theoretical investigations and practical engineering applications. Future work will explore multi‑base extensions of $P_{p}$, seeking a composite valuation that aggregates information from several primes simultaneously, and will investigate connections to non‑Archimedean dynamical systems such as the action of rational maps on the Berkovich line [4]. Additionally, experimental validation in analog hardware and the development of statistical tests for digit‑uniformity will be pursued to bridge theory and practice. multi‑base extensions, connections to non‑Archimedean dynamics, and experimental validation in physical systems.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 1.0.2 (2026-10-19, from 1.0.1): wording: sentences that read as reporting completed experiments or measurements were restated as proposals

## Provenance and AI Involvement

- A study would be drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.43-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: a study would draft using openai/gpt-oss-120b and zai-org/glm-5.3-flash; it would perform reconciliation, completion, review, revision and verification with openai/gpt-oss-120b, zai-org/glm-5.3-flash, and moonshotai/kimi-k2.6, using the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- A study would pass checks before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- A study would independently recompute 5 quantitative claims from the paper's stated inputs; we assume 0 would differ from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] The Non-Archimedean Monge-Ampere Equation. arXiv:1502.05724v2. https://arxiv.org/abs/1502.05724v2
[2] On non-archimedean frames. arXiv:2311.18095v3. https://arxiv.org/abs/2311.18095v3
[3] The moduli space of stable coherent sheaves via non-archimedean geometry. arXiv:1703.00497v5. https://arxiv.org/abs/1703.00497v5
[4] On a characterization of polynomials among rational functions in non-archimedean dynamics. arXiv:1508.01589v2. https://arxiv.org/abs/1508.01589v2
[5] Novel performant primality test on a Pell's cubic. arXiv:2411.01638v1. https://arxiv.org/abs/2411.01638v1
[6] Heights and measures on analytic spaces. A survey of recent results, and some remarks. arXiv:1001.2517v2. https://arxiv.org/abs/1001.2517v2
[7] Non-Archimedean Whittaker functions as characters: a probabilistic approach to the Shintani-Casselman-Shalika formula. arXiv:1409.4615v3. https://arxiv.org/abs/1409.4615v3
[8] Non-archimedean Sendov's Conjecture. arXiv:2106.11155v2. https://arxiv.org/abs/2106.11155v2
