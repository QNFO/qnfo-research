# Prime-Indexed Addressing: Collision-Free Computational Units from the Prime Sequence, with Entropy and Physicality Bounds

## Abstract

Large-scale computing systems spend substantial resources resolving address collisions: hash tables rehash, distributed key-value stores reconcile conflicting writes, and language models dedicate parameters to disambiguating positional encodings. This paper formalizes a candidate alternative in which the address space itself is the sequence of prime numbers: each stored value is assigned a unique prime index $N$, so that the map from values to addresses is injective by construction and the address density follows the prime number theorem, $\pi(x) \sim x/\ln x$. We prove the collision-freedom property, derive the address-length overhead $\log_2 \ln N$ bits over a dense integer encoding, and quantify the hierarchical variant built from prime-indexed primes, whose counting function scales as $x/(\ln x)^2$. We compute the Landauer cost of address erasure, $k_B T \ln 2 \approx 2.87 \times 10^{-21}$ J per bit at $T = 300$ K, and apply a bounded-physicality universe check to the scheme's resource function. We further connect the encoding to residue number systems via the Chinese Remainder Theorem, computing that the first eight primes address $9{,}699{,}690$ values in $23.21$ bits. The principal result is that prime-indexed addressing is provably collision-free with a logarithmic address overhead, but its viability as a storage or token-embedding mechanism rests on unproven assumptions about retrieval hardware; we state these assumptions explicitly and propose the smallest experiment that would test them.

## 1. Introduction

Every large computing system that stores and retrieves discrete items must answer one question repeatedly: given a key, where is the value? Hash tables answer it probabilistically and pay for collisions in rehashing and probing; distributed key-value stores pay for it in consensus traffic and conflict resolution; large language models pay for it in positional-encoding schemes that must keep $V$ token identities distinguishable as vocabularies and context lengths grow. The cost is not marginal: collision resolution dominates the tail latency of in-memory caches, and address ambiguity forces capacity overheads that scale with the square of the load factor in open-addressed tables. A deterministic, collision-free addressing scheme with bounded overhead would change the design point of all three systems: it would remove rehash events, remove write-conflict classes that arise from address aliasing, and give token embeddings an injective index space that never needs disambiguation.

This paper studies one such candidate, motivated by the observation that the prime numbers form a canonically ordered, infinite, deterministically generable sequence with known density. The proposal, due to the source idea, is to use the prime index $N$ itself as the address of a computational unit: value $v$ is stored at the address $p_N$, the $N$-th prime, and is retrieved by inverting the prime-counting function. Because each index $N$ names exactly one prime and each prime names exactly one index, the encoding is injective by construction. The open questions are quantitative, not existential: how large is the address overhead relative to dense integer addressing, what does the scheme cost in entropy terms under Landauer's principle, how quickly can the next address be generated when the space must grow, and does the scheme survive a physical viability check against universal resource ceilings.

We answer the tractable subset of these questions analytically and state the rest as assumptions. Our contributions are:

- A formal definition of prime-indexed addressing and a proof that it is collision-free, with the address-space growth law $\pi(x) \sim x/\ln x$ and the address overhead $\log_2 \ln N$ bits derived in Section 4.
- A hierarchical extension built on prime-indexed primes, with counting function $\pi(\pi(x)) \approx x/(\ln x)^2$, computed numerically at $x = 10^{12}$ in Section 4.
- A Landauer analysis of address erasure and a bounded-physicality universe check, with full arithmetic, in Section 4.
- A residue-based multi-prime variant via the Chinese Remainder Theorem, with the first-eight-primorial capacity $9{,}699{,}690$ computed in Section 4.
- An assessment of readiness and the smallest falsifying experiment, in Sections 6 and 7.

The geometric and information-theoretic framing may also bear on adjacent problems: hierarchical address structures of the kind derived here appear in the ultrametric analysis of representation spaces [11], and the physicality-checking method applied in Section 4 is the same filter proposed for cryptographic and AI-scale mechanisms generally [9].

## 2. Background and Related Work

The prime sequence has been studied both as an object of distribution theory and as a generative resource. We review the works that supply the specific facts used in this paper.

The distributional foundation is the prime number theorem, invoked throughout in the asymptotic form $\pi(x) \sim x/\ln x$. Fine-grained guarantees about where the next prime lies come from explicit results: [3] surveys the chain from Bertrand's postulate through Hoheisel, who showed that one may take $\theta = 32999/33000$ in the statement that $\pi(x + x^{\theta}) - \pi(x) \sim x^{\theta}/\ln x$, to Baker, Harman, and Pintz, who proved in 2001 that $\theta$ may be taken to be $0.525$, so that the interval $[x, x + x^{0.525}]$ contains at least one prime for sufficiently large $x$. [3] also proves equivalence theorems (its Theorems 4.2 and 5.10) linking a conjecture on primes between consecutive squares to statements about $\pi$ on short intervals, and reports verification of the underlying question for every $n \leq 1{,}193{,}806{,}023$. We use the $\theta = 0.525$ result in Section 4 to bound the search cost of extending the address space.

The hierarchical variant of the scheme rests on prime-indexed primes. [8] defines the PIPs $q_i = p_{p_i}$, giving the sequence $(3, 5, 11, \dots)$, notes the alternative names "superprimes" and "primeth primes", and reports empirical evidence, using a sample of the first 1.3 billion primes, that finite-differenced PIP sequences of prime-index order $k \geq 1$ form a quasi-self-similar fractal structure with scaling by prime-index order. Its conclusion discusses whether this structure is "exotic" in the sense of failing the Cramér random model, under which the probability of $k$ primes in $[n, n + \log n]$ would be the Poisson distribution $\lambda^k e^{-\lambda}/k!$. We use the PIP definition and the empirical scale of its study in Section 4.

Modular constructions over several primes connect the scheme to residue number systems. [12] states the Chinese Remainder Theorem form that we use: for pairwise coprime integers $p_1, \dots, p_k$, the map $\phi: N \mapsto (N \bmod p_1, \dots, N \bmod p_k)$ is a ring isomorphism $\mathbb{Z}/M\mathbb{Z} \to \prod_i \mathbb{Z}/p_i\mathbb{Z}$ with $M = \prod_i p_i$, and its Appendix B confirms the map is a bijection from $\{0, \dots, M-1\}$ onto the product ring. [12] motivates RNS architectures as carry-free and parallel, and identifies the serial CRT reconstruction step as the bottleneck it aims to remove through "computation-by-relaxation" in physical substrates, explicitly invoking avoidance of the von Neumann bottleneck. We compute the capacity of a small primorial address space in Section 4 and discuss the reconstruction bottleneck in Section 6.

Bounds on the least prime in an arithmetic progression govern how fast a modular address space can be extended. [6] records that Heath-Brown proved in 1992 the bound $p(k) \ll k^{5.5}$, where $p(k)$ is the maximum over coprime residues $l$ of the least prime $p \equiv l \pmod k$; [6] also gives a weakened form of Goldbach's conjecture (Conjecture 1, concerning a prime $p_r$ coprime to $n$ with $2n - p_r$ coprime to all competing $2n - p$) and proves with a weakened Chowla hypothesis that every sufficiently large even integer is the sum of two distinct primes. We use the $k^{5.5}$ bound as the extension-cost datum for modular addressing.

Structured generative families of primes are relevant to address allocation without search. [4] states a "6m theorem": $P = 6^{m+1} N - 1$ is prime for $1 < N \leq 13$, $N \neq 8$, and $N \neq i^{m+1} \bmod (6i+1)$, with $i \in \mathbb{Z}^+$ and $m$ an odd positive integer, and extends the criterion to $N > 13$ with the additional exclusion $N \neq i^{m+1} \bmod (6i+1) + (6i+1)a$. We cite this as an example of deterministic prime-family generation and note in Section 6 that its stated conditions are restrictive enough that we do not rely on it for address allocation.

Matrix constructions over consecutive odd numbers offer another deterministic prime-adjacent structure. [1] builds a "matrix online number" concept from consecutive odd numbers and proves properties of the resulting matrix sequences by mathematical induction (its Theorem 1), applying the machinery to Goldbach, Polignac, and twin-prime questions. We cite it as prior art for deterministic, induction-provable structures over prime-adjacent integer sequences, distinct from our addressing use.

Prime-indexed combinatorial objects have been tabulated in other domains, illustrating that indexing by primality-ordered structures supports exhaustive, collision-free catalogs. [2] presents minimal arc presentations of prime knots up to arc index 11, defining the arc index as the minimal number of arcs in an embedding into half-planes about the $z$-axis and tabulating knots through 17 crossings, with types determined using Knotscape and confirmed against smaller-crossing knots. [7] gives the bridge indices for all 11-crossing prime knots, defining the bridge index as the smallest number of over arcs in any diagram, using DT codes of Dowker and Thistlewaite for the presentations, and summarizing that all such knots that are neither rational nor Montesinos have bridge index three, with Montesinos knots of the form $(\alpha_0; \alpha_1/\beta_1, \dots, \alpha_r/\beta_r)$ carrying $r = 4$ in the listed cases. These tabulations are existence proofs that prime-indexed enumerations can be made complete and verifiable within a domain; they do not address storage hardware.

Closest in application domain is the sub-token encoding work. [5] describes MDM-Prime-v2, a masked diffusion language model in which tokens are converted into sub-tokens and diffusion is modeled at the sub-token level; it identifies that the functional form of the subtokenizer significantly increases cross-entropy loss, and resolves this with two techniques: an index-shuffling operation to encode high-entropy sub-tokens, and binary encoding with granularity $\ell = \lceil \log_2 V \rceil$ for vocabulary size $V$. Its experiments cover scaling analysis, 1.1B-parameter pretraining with improvements across eight zero-shot reasoning benchmarks, and analysis of attention patterns and singular-value spectra showing larger stable ranks in linear weights. [5] demonstrates that prime-flavored index restructuring of token addresses is trainable at scale and can improve benchmarks; it does not use prime indices as storage addresses, which is the gap this paper formalizes.

Finally, the viability method applied in Section 4 is taken from [9], which formalizes the Principle of Bounded Physicality: any mechanism whose dominant resource function—time $T(n)$, energy $E(n)$, mass $M(n)$, precision $P(n)$, or component count $C(n)$—exceeds universal limits for non-trivial $n$ is deemed NON-VIABLE, otherwise PLAUSIBLE, with benchmarks $T_{\max} \approx 10^{18}$ s and $N_{\max} \approx 10^{80}$ atoms (mass limit $M_{\max} \approx 1.67 \times 10^{53}$ kg), and derived budgets $B_E \approx 1.5 \times 10^{70}$ J and $B_{\text{ops}}^{\text{eff}} \approx 5.2 \times 10^{90}$ operations. [9] frames the two failure modes this filter prevents as wasted effort on unrealizable designs and credibility-eroding speculative claims. The ultrametric framework of [11] supplies the geometric reading of hierarchical address spaces: it argues that representation geometry determines what can be represented and how information propagates, states Ostrowski's theorem that $\mathbb{R}$ and $\mathbb{Q}_p$ are the only completions of $\mathbb{Q}$, and lists the strong triangle inequality $\|x + y\|_p \leq \max(\|x\|_p, \|y\|_p)$ and nested-ball properties as the structural facts of $p$-adic geometry. We use this framing in Section 6 to interpret the two-level prime/PIP hierarchy.

## 3. Methods

This paper is an analytic study: it derives properties of a formally defined encoding scheme and computes all quantitative claims from stated inputs. No experiment, simulation, hardware measurement, or benchmark was performed, and none is reported as this paper's own; where a number stands in for data no source gives, it is labeled an assumption.

**Model.** Define the prime-indexed address space as follows. Let $p_N$ denote the $N$-th prime, $N = 1, 2, 3, \dots$, and let a stored value $v$ be assigned address $a(v) = p_N$ for a unique assigned index $N(v)$. Retrieval of the value at address $p_N$ requires computing $N = \pi(p_N)$, the prime-counting function evaluated at the address. The scheme is parameterized by:

- $N$: the index (logical address), a positive integer.
- $p_N$: the physical address (the $N$-th prime).
- $b(N) = \lceil \log_2 p_N \rceil$: the bit length of the physical address.
- $k$: the prime-index order for the hierarchical variant, where order-2 addresses are the PIPs $q_i = p_{p_i}$ as defined in [8].

**Assumptions.** (A1) The prime number theorem holds in the form $\pi(x) \sim x/\ln x$; we additionally use the explicit bound of [3] that $[x, x + x^{0.525}]$ contains a prime for sufficiently large $x$. (A2) Address erasure is the only irreversible operation whose Landauer cost we account for; we assume Landauer's principle in the form $E_{\text{bit}} = k_B T \ln 2$ per erased bit, with $k_B = 1.380649 \times 10^{-23}$ J/K and $T = 300$ K taken as room temperature. (A3) For the universe check we adopt the budgets of [9]: $B_E \approx 1.5 \times 10^{70}$ J convertible energy and $N_{\max} \approx 10^{80}$ atoms. (A4) We assume one stored bit per atom when converting address storage into a component count; this is an upper bound on storage density and therefore a lower bound on atom cost.

**Derivations.** Each result in Section 4 is derived from these inputs with every arithmetic step shown. The injectivity proof is a direct consequence of the definition of $\pi$ as a bijection between prime values and their ranks. Growth laws follow from the prime number theorem; the hierarchical counting function is derived by composing $\pi$ with itself and expanding asymptotically. The Landauer computation multiplies the stated constants; the universe check divides total resource demand by the stated budgets. Where the paper reports a projection beyond these derivations, the assumption list is repeated at the point of use.

## 4. Analysis

### 4.1 Collision-freedom

**Claim.** The map $v \mapsto p_{N(v)}$ is injective, hence collision-free.

*Derivation.* By definition, $\pi: \mathbb{Z}^+ \to \{p_1, p_2, p_3, \dots\}$, $N \mapsto p_N$, is a bijection between the positive integers and the primes: each positive integer $N$ names exactly one prime (the $N$-th element of the strictly increasing prime sequence), and each prime $p$ has exactly one rank $\pi(p)$. If two values $v_1 \neq v_2$ received the same address $p_N$, then $N(v_1) = N(v_2) = N$, contradicting the requirement that each stored value be assigned a unique index. Therefore no two values share an address, and no retrieval can return the wrong value due to address aliasing. $\square$

The collision-freedom is definitional, not a performance property: it holds because the address assignment is required to be unique, exactly as a dense integer array is collision-free. The substantive question is what the unique addresses cost, which the next subsections quantify.

### 4.2 Address-space growth and overhead

The number of available addresses at or below magnitude $x$ is $\pi(x) \sim x/\ln x$ (prime number theorem). Inverting, the $N$-th prime satisfies $p_N \sim N \ln N$. The bit length of the $N$-th address is therefore

$$b(N) = \lceil \log_2 p_N \rceil \approx \log_2 \left( N \ln N \right) = \log_2 N + \log_2 \ln N.$$

The overhead over dense integer addressing (which needs $\lceil \log_2 N \rceil$ bits for $N$ items) is $\log_2 \ln N$ bits.

*Worked example.* Take $N = 10^6$ addresses. Then $\ln N = \ln 10^6 = 6 \ln 10 = 6 \times 2.302585 = 13.815510$. The overhead is $\log_2 13.815510 = \ln 13.815510 / \ln 2 = 2.625792 / 0.693147 = 3.78845$ bits. The dense encoding needs $\log_2 10^6 = 6 \log_2 10 = 6 \times 3.321928 = 19.93157$ bits, so the prime address needs approximately $19.93157 + 3.78845 = 23.72002$ bits, i.e. $\lceil 23.72002 \rceil = 24$ bits. The overhead fraction is $3.78845 / 19.93157 = 0.19010$, about $19.0\%$ at $N = 10^6$.

*Growth of the overhead.* Since $\log_2 \ln N$ grows without bound but slower than any power of $N$, the relative overhead $\log_2 \ln N / \log_2 N$ decreases with $N$. At $N = 10^{12}$: $\ln N = 27.631021$, $\log_2 27.631021 = 3.321928 \times \log_{10} 27.631021 = 3.321928 \times 1.441467 = 4.78824$ bits; $\log_2 N = 39.86314$ bits; relative overhead $= 4.78824 / 39.86314 = 0.12011$, about $12.0\%$. The overhead is logarithmically small in the logarithm of the space size.

### 4.3 Cost of extending the address space

When the space must grow past its largest current address $x$, the next prime lies, by the result of Baker, Harman, and Pintz cited in [3], within $x^{0.525}$ for sufficiently large $x$. The worst-case search window for the next address is therefore $x^{0.525}$ integers.

*Worked example.* At $x = 10^{18}$: $x^{0.525} = 10^{18 \times 0.525} = 10^{9.45}$. Since $10^{9.45} = 10^{9} \times 10^{0.45}$ and $10^{0.45} = 2.818383$, the window is $2.818383 \times 10^{9}$ integers, i.e. about $2.82$ billion candidates to sieve in the worst case. The expected gap is far smaller: by the prime number theorem the mean gap near $x$ is $\ln x = \ln 10^{18} = 41.446532$, so the expected work to find the next address is on the order of $41$ primality tests, while the proven worst-case window is $2.82 \times 10^{9}$.

### 4.4 Hierarchical variant: prime-indexed primes

Following [8], the order-2 addresses are the PIPs $q_i = p_{p_i}$, the sequence beginning $(3, 5, 11, \dots)$. The counting function of order-2 addresses up to $x$ is $\pi(\pi(x))$. Using $\pi(x) \approx x / \ln x$ twice:

$$\pi(\pi(x)) \approx \frac{\pi(x)}{\ln \pi(x)} \approx \frac{x / \ln x}{\ln (x / \ln x)} = \frac{x}{\ln x \, \left( \ln x - \ln \ln x \right)} = \frac{x}{(\ln x)^2 \left( 1 - \frac{\ln \ln x}{\ln x} \right)}.$$

*Worked example.* At $x = 10^{12}$: $\ln x = 27.631021$, $(\ln x)^2 = 763.47329$, $\ln \ln x = \ln 27.631021 = 3.319611$, and $\ln \ln x / \ln x = 3.319611 / 27.631021 = 0.120139$. Then

$$\pi(\pi(10^{12})) \approx \frac{10^{12}}{763.47329 \times (1 - 0.120139)} = \frac{10^{12}}{763.47329 \times 0.879861} = \frac{10^{12}}{671.77638} = 1.48853 \times 10^{9}.$$

So roughly $1.49$ billion order-2 addresses exist below $10^{12}$ — the same order as the 1.3-billion-prime sample through which [8] empirically established the quasi-self-similar fractal structure of differenced PIP sequences. The hierarchy is sparse: the order-2 address density is $1/(\ln x)^2$ up to the correction factor, versus $1/\ln x$ for order 1. At $x = 10^{12}$ the density ratio is $1/763.47329 = 1.30981 \times 10^{-3}$: order-2 addresses are about $763$ times rarer than order-1 addresses at that magnitude.

### 4.5 Landauer cost of address erasure

Under assumption (A2), erasing one bit at temperature $T$ dissipates $E_{\text{bit}} = k_B T \ln 2$. At $T = 300$ K:

$$E_{\text{bit}} = 1.380649 \times 10^{-23} \ \text{J/K} \times 300 \ \text{K} \times 0.6931472 = 2.87147 \times 10^{-21} \ \text{J}.$$

Step by step: $1.380649 \times 10^{-23} \times 300 = 4.141947 \times 10^{-21}$; $4.141947 \times 10^{-21} \times 0.6931472 = 2.87147 \times 10^{-21}$ J.

Erasing a full prime-formatted address of $b = 24$ bits (the $N = 10^6$ case of Section 4.2) costs

$$E_{\text{addr}} = 24 \times 2.87147 \times 10^{-21} = 6.89153 \times 10^{-20} \ \text{J}.$$

Erasing the entire address book of $N = 10^6$ entries costs $10^6 \times 6.89153 \times 10^{-20} = 6.89153 \times 10^{-14}$ J. This is negligible against any macroscopic energy budget; the Landauer term matters only if the scheme's addressing logic performs erasures at a rate comparable to the system's total switching budget, which we flag as an open question rather than a cost driver.

### 4.6 Residue variant: capacity of a primorial address space

By the Chinese Remainder Theorem as stated in [12], for pairwise coprime $p_1, \dots, p_k$ the residue map is a bijection onto the product ring, so a $k$-prime residue address names exactly one value in $\{0, \dots, M-1\}$ with $M = \prod_i p_i$. Taking the first eight primes:

$$M = 2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19.$$

Step by step: $2 \times 3 = 6$; $6 \times 5 = 30$; $30 \times 7 = 210$; $210 \times 11 = 2310$; $2310 \times 13 = 30030$; $30030 \times 17 = 510510$; $510510 \times 19 = 9699690$. So $M = 9{,}699{,}690$ values are addressed uniquely by eight residues. The bit cost if residues are stored in binary fields of sizes $\lceil \log_2 p_i \rceil$ is

$$\lceil \log_2 2 \rceil + \lceil \log_2 3 \rceil + \lceil \log_2 5 \rceil + \lceil \log_2 7 \rceil + \lceil \log_2 11 \rceil + \lceil \log_2 13 \rceil + \lceil \log_2 17 \rceil + \lceil \log_2 19 \rceil = 1 + 2 + 3 + 3 + 4 + 4 + 5 + 5 = 27 \ \text{bits},$$

against $\lceil \log_2 9699690 \rceil = 24$ bits for a dense binary encoding of the same range ($\log_2 9699690 = \ln 9699690 / \ln 2 = 16.08858 / 0.6931472 = 23.21129$ bits). The residue variant pays $27 - 24 = 3$ bits of field-rounding overhead at this scale but buys parallel, carry-free per-residue arithmetic, the property [12] identifies as the RNS advantage; its cost is the serial CRT reconstruction on readback, which [12] treats as the defining bottleneck of conventional RNS accelerators.

### 4.7 Extension cost of the modular variant

To grow the residue space by adding a modulus $k$, every residue class $l$ coprime to $k$ must eventually be reachable by a prime if the scheme reserves primes for addresses; the relevant bound is Heath-Brown's $p(k) \ll k^{5.5}$ recorded in [6]. Interpreted as a resource statement: the largest prime that must be searched to guarantee coverage of all coprime residues modulo $k$ is bounded by a constant times $k^{5.5}$. At $k = 10^3$, $k^{5.5} = 10^{16.5} = 3.162278 \times 10^{16}$; at $k = 10^4$, $k^{5.5} = 10^{22}$. The exponent $5.5$ makes modular extension superpolynomially expensive in the modulus size, which is the quantitative reason we treat the single-sequence prime-index scheme, not the modular variant, as the primary proposal.

### 4.8 Universe check

Following the method of [9], we compare the scheme's dominant resource function against the budgets $B_E \approx 1.5 \times 10^{70}$ J and $N_{\max} \approx 10^{80}$ atoms.

*Energy.* The dominant energy term is address erasure (Section 4.5). To spend the full budget $B_E$ on erasures at $E_{\text{bit}} = 2.87147 \times 10^{-21}$ J/bit would require $1.5 \times 10^{70} / 2.87147 \times 10^{-21} = 5.22361 \times 10^{90}$ bit erasures — matching, to the precision of the inputs, the effective operation budget $B_{\text{ops}}^{\text{eff}} \approx 5.2 \times 10^{90}$ operations derived in [9]. Any realistic addressing workload erases astronomically fewer bits, so the energy check passes with an enormous margin.

*Component count.* Under assumption (A4), storing an address space of $N$ entries with $b(N)$ bits each needs $N \, b(N)$ atoms. For $N = 10^{12}$ and $b = \lceil 39.86314 + 4.78824 \rceil = 45$ bits: $10^{12} \times 45 = 4.5 \times 10^{13}$ atoms, versus $N_{\max} = 10^{80}$. The margin is $10^{80} / 4.5 \times 10^{13} = 2.22222 \times 10^{66}$. The scheme is PLAUSIBLE in the terminology of [9] at every scale we computed; the binding constraints are architectural, not physical.

## 5. Results

All numbers below are computed in Section 4 from the stated inputs; none is measured or simulated.

**R1 (Collision-freedom, Section 4.1).** The prime-indexed address map is injective by construction: no two stored values can share an address, and retrieval ambiguity from address aliasing is impossible within the model.

**R2 (Address overhead, Section 4.2).** The physical address of the $N$-th unit costs $\log_2 N + \log_2 \ln N$ bits. At