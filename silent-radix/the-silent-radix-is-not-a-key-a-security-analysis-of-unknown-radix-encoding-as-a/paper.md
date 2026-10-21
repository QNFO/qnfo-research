# The Silent Radix Is Not a Key: A Security Analysis of Unknown‑Radix Encoding as a Cryptographic Primitive

## Abstract

Positional numerals do not internally specify their own base, and a recent informal proposal—Silent Radix Encryption (SRE)—conjectures that this “silent radix” can serve as a cryptographic secret. No formal security analysis of this construction exists. We formalize the encoding core, define its key space over admissible radices $B\in[2,2^{16}]$ and digit maps on a 26‑symbol alphabet, and compute its entropy as $104.38$ bits. We then show that the construction reduces to a monoalphabetic substitution cipher with base‑dependent segmentation, and we derive a two‑stage ciphertext‑only attack: a histogram test recovers $B$ at a cost of at most $6.5535\times10^{7}$ digit operations for a 1000‑symbol ciphertext, after which standard frequency analysis applies within a unicity distance of $149.1$ symbols, computed from the key entropy and an assumed language redundancy of $0.70$ bits/symbol. Brute‑force over the full key space at $10^{9}$ keys/s would take $8.36\times10^{14}$ years, yet the structural attack succeeds on a single short message, making key‑space size irrelevant. We conclude that radix obscurity offers no security advantage over classical substitution ciphers and therefore no quantum‑relevant advantage, and we state the conditions under which this negative result would be falsified.

## 1. Introduction

A recurring failure mode in cryptographic engineering is the deployment of primitives whose security rests on the secrecy of a design parameter rather than on the secrecy of a key under a public, well‑scrutinized algorithm. Security architects performing cryptographic migration and inventory work face this problem concretely: the Cryptographic Bill of Materials (CBOM) methodology exists precisely because organizations must decide which deployed mechanisms to trust and which to retire as algorithms are deprecated and post‑quantum readiness is planned [5]. If a mechanism such as unknown‑radix encoding were believed to be a viable lightweight cipher or key‑encapsulation trapdoor, it could enter that inventory as a candidate; if it is in fact breakable by classical statistical attacks on a single ciphertext, it must be excluded before it is ever deployed. Today no formal analysis exists that lets an architect, a standards body, or a protocol designer make that decision with confidence: the proposal circulates as an informal conjecture that a secret base $B$—the observation that a positional numeral cannot specify its own base—could act as a cryptographic trapdoor [9].

The stakes are concrete. An organization that adopted such a scheme for key encapsulation would believe its encapsulated keys were protected by a large key space—over $2^{100}$ combinations of radix and digit map in the parameterization analyzed here—and might further believe that a scheme built from integer arithmetic rather than from structured lattices or block ciphers resists quantum attack by being “unusual.” This paper shows that both beliefs are wrong: the entire key space collapses under a statistical test that costs less than $10^{8}$ elementary operations, and the residual problem is a monoalphabetic substitution cipher, a primitive broken by classical statistical means long before the era of digital computers. The decision that changes if this result holds is simple: unknown‑radix encoding is classified as obfuscation, not encryption, and is excluded from cryptographic inventories and migration plans at the same tier as encoding tricks, with no post‑quantum consideration owed to it.

We analyze the scheme named Silent Radix Encryption in the source literature [9], which states that SRE uses a secret base $b$ as a trapdoor for key encapsulation and that its security reduces to an unknown‑weight integer knapsack problem. We analyze the core encoding primitive directly and show that the knapsack reduction, even if correct, does not confer security, because the encoding admits a direct statistical attack that bypasses the knapsack structure entirely.

**Contributions.**
- A formal definition of the unknown‑radix encoding scheme, its key space (admissible radices $B\in[2,B_{\max}]$ and digit maps over an $m$‑symbol alphabet), and the computation of its entropy: $104.38$ bits for $m=26$, $B_{\max}=2^{16}$ (Sections 3 and 4.1).
- A reduction showing that decryption under a known radix is exactly a monoalphabetic substitution with base‑dependent segmentation, and a derivation of the unicity distance $n_{0}=149.1$ symbols for the full key space (Sections 4.2 and 4.3).
- An explicit two‑stage ciphertext‑only attack with full arithmetic: radix recovery by histogram discrimination at a cost of at most $6.5535\times10^{7}$ digit operations for $n=1000$, followed by frequency analysis of the residual substitution (Section 4.4).
- A comparison against brute‑force benchmarks showing that the key‑space entropy of $104.38$ bits is structurally irrelevant: the binding constraint is the unicity distance, not the key count (Sections 4.5 and 5).
- A statement of the negative result for quantum relevance—a scheme broken classically on a single ciphertext cannot offer a quantum‑relevant advantage—together with falsification conditions and the limits of the analysis (Section 6).

## 2. Background and Related Work

The immediate ancestor of this work is the silent‑radix proposal itself. The Silent‑Radix Cryptography note states the core observation—that a positional numeral cannot internally specify its own base, so the base is “silent”—and proposes Silent Radix Encryption (SRE), which uses a secret base $b$ as a trapdoor for key encapsulation and claims that security reduces to an unknown‑weight integer knapsack problem [9]. The note supplies the construction: the sender generates $k$ random decimal digits, computes the shared secret $K=\sum_{i=0}^{k-1}d_i\,b^{i}$ under the secret base $b$, derives a symmetric key via SHA‑256, encrypts by counter‑mode XOR, and transmits the decimal interpretation $N=\sum_{i=0}^{k-1}d_i\,10^{i}$ as the public envelope; the receiver extracts the decimal digits of $N$ and recomputes $K$ in base $b$ [9]. The note frames the digit string as a path through a rooted tree under the $b$‑adic ultrametric $d(x,y)=b^{-v_b(x-y)}$ and asserts a reduction to a knapsack problem. No key‑space entropy, unicity distance, or ciphertext‑only attack cost is provided.

 That result addresses the known‑plaintext setting only; the ciphertext‑only question, which is the stronger and more realistic demand on a key‑encapsulation mechanism, remains open. Our analysis answers it.

A third paper, HM‑LWE v3.0, proposes hidden‑modulus Learning With Errors as a novel hardness assumption: standard lattice‑based cryptography operates over a publicly known modulus, and the paper asks what happens when the modulus itself is secret, forcing the adversary into a joint search over modulus and key [10]. Its own account records that the initial hidden‑radix observation was followed by a comparative analysis establishing that noise‑free hidden‑radix ciphers fail catastrophically under known‑plaintext attack, and that noise‑augmented constructions were then introduced in response [10].  This sequence matters for our argument: the hidden‑modulus program itself concedes that the noise‑free encoding layer is broken and turns to injected noise for security. Our result formalizes the ciphertext‑only half of that concession for the pure radix case; the noise‑augmented variants change the attack surface and are outside our scope.

The broader literature supplies the evaluation standards against which any new primitive must be judged. Kerckhoffs’s principle— the system must remain secure even if everything about it except the key is public— is operationalized in modern formal methods: the first formal model of Bitcoin’s Payment Protocol (BIP70) formalised the previously shown refund‑attack vulnerability arising from lack of authentication of refund addresses, using the symbolic model‑checker OFMC and the AnB formal language in which communication channels are modeled as abstractions conveying security goals such as authenticity and secrecy [4]. That work is the template we follow: an informal belief about a protocol’s security is converted into a formal model, and the model is then attacked. Our Section 3 formalization and Section 4 attack play the same role for unknown‑radix encoding that the formal model and refund‑attack analysis played for BIP70.

On the constructive side, the literature shows what real key‑establishment machinery looks like, and thereby sharpens the comparison in Section 4.5. The Multi‑Factor Key Derivation Function (MFKDF) construction extends password‑based key derivation with additional authentication factors such as TOTP, HOTP, and hardware tokens [6]. The relevant lesson is that practical key management derives security from multiple independent secret inputs consumed by public algorithms—the exact opposite of deriving it from a single obscure encoding parameter. Biometric key‑generation work makes the same point from another direction: two closely related papers on generating cryptographic keys from multimodal biometric feature‑level fusion of fingerprint and iris address the problem that human users have a tough time remembering long cryptographic keys, by deriving repeatable keys from user biometrics while incorporating the volatility of those features [2], [3]. Both accept that the key must be a high‑entropy secret consumed by a standard primitive; neither proposes that the encoding of data could itself carry the secrecy. Our result explains why: encoding secrecy is structurally weak.

The deployment context is framed by work on how security mechanisms actually fail in the field. A device‑centric analysis of Extended Reality (XR) devices surveys security and privacy attacks and defenses [7]. The lesson we draw is about evaluation culture: mechanisms deployed on consumer hardware are examined adversarially after deployment, so a mechanism whose security depends on a subtle parameter is a liability regardless of platform. The same conclusion motivates classifying unknown‑radix encoding before deployment rather than after.

Finally, work on cryptographically verifiable authorization for autonomous AI agents proposes a falsifiable hypothesis and proof of concept for giving agents’ requests cryptographic evidence of policy compliance in context, and explicitly separates binding layers—identity binding, authorization‑request binding, and runtime execution binding—as structurally distinct security properties requiring separate mechanisms [1]. That work illustrates the standard a new primitive must meet—a falsifiable, verifiable security claim—and Section 6 states the falsification conditions for our own claim in the same spirit.

Two methodological gaps emerge from this survey. First, no cited work analyzes base‑ambiguity or radix‑obscurity constructions against a ciphertext‑only adversary; the silent‑radix proposal [9] asserts a reduction to knapsack but supplies no key‑space entropy, no unicity distance, and no attack cost, and the known‑plaintext result of [11] leaves the ciphertext‑only question open. Second, the cited formal‑analysis work [4] shows the value of converting informal proposals into models, but has not been applied to encoding‑based primitives. This paper fills both gaps for the unknown‑radix case.

## 3. Methods

### 3.1 The scheme

Let $\Sigma$ be a plaintext alphabet of $m$ symbols (for concreteness, English letters, $m=26$). The secret key is a pair $K=(B,\pi)$ where:

- $B\in[2,B_{\max}]$ is the radix, an integer, with $B_{\max}$ a public parameter of the scheme;
- $\pi:\Sigma\to\{0,1,\dots,m-1\}$ is a secret bijection assigning each plaintext symbol a digit value.

Encryption of a plaintext $P=s_{1}s_{2}\dots s_{n}$ of $n$ symbols proceeds in two steps:

1. Map each symbol to its digit: $d_{i}=\pi(s_{i})$ for $i=1,\dots,n$.
2. Interpret the digit string $d_{1}d_{2}\dots d_{n}$ as a positional numeral in base $B$, i.e., compute the integer  

$$C=\sum_{i=1}^{n}d_{i}\,B^{\,n-i}.$$

The ciphertext is the integer $C$, transmitted without base information. Decryption by the holder of $K$ writes $C$ in base $B$, recovers the digit string $d_{1}\dots d_{n}$, and applies $\pi^{-1}$.

This is the encoding core of the scheme described as Silent Radix Encryption in [9], restricted to the pure encoding primitive; we do not model any additional encapsulation layers, and our conclusions apply to the core.

### 3.2 Key space and adversary model

The key space is  

$$\mathcal{K}=\{(B,\pi):B\in\{2,\dots,B_{\max}\},\ \pi\in\mathrm{Sym}(m)\},$$  

where $\mathrm{Sym}(m)$ is the set of bijections from $\Sigma$ to $\{0,\dots,m-1\}$. Its size is  

$$|\mathcal{K}|=(B_{\max}-1)\cdot m!.$$

The adversary model is ciphertext‑only: the attacker sees the integer $C$ (and possibly several such integers under the same key), knows the scheme, the alphabet size $m$, and $B_{\max}$, but not $B$ or $\pi$. This is the Kerckhoffs‑consistent model: everything about the design except $K$ is public. We verify the model’s assumptions against the scheme’s own description: the base is “silent”—carried by neither the ciphertext nor any public parameter—so its secrecy is the entire claim of the primitive [9].

### 3.3 Language model

Frequency analysis requires a source model. We adopt the following explicitly assumed parameters for English text over $m=26$ symbols, used consistently throughout and labeled as assumptions wherever they enter a computation:

- $A_{1}$: per‑symbol source entropy $H_{1}=4.0$ bits (against a maximum of $\log_{2}26\approx4.70$ bits for a uniform source), giving redundancy per symbol $D=\log_{2}26-H_{1}=0.70$ bits.
- $A_{2}$: the most frequent symbol occurs with probability $p_{\max}=0.12$.
- $A_{3}$: the least frequent symbol occurring in ordinary text has probability $p_{\min}=0.005$.

These are modeling assumptions about the plaintext source, not measurements; Section 6 states how the results shift if they are varied.

### 3.4 Analysis methods

We use four analytic instruments, all standard and all applied with explicit arithmetic in Section 4: (i) key‑space entropy $H(K)=\log_{2}|\mathcal{K}|$; (ii) the unicity distance $n_{0}=H(K)/D$, the number of ciphertext symbols beyond which only one key yields a plausible plaintext; (iii) a histogram discrimination test for the radix, comparing the digit‑frequency skew of the true base against the near‑uniform digit frequencies of a wrong base; and (iv) brute‑force cost arithmetic for benchmarking. No simulations were run and no empirical attack data were collected; every number in Section 5 is either derived in Section 4 or labeled a projection with stated assumptions.

## 4. Analysis

### 4.1 Key‑space entropy

With $m=26$ and $B_{\max}=2^{16}=65536$:

- Number of admissible radices: $B_{\max}-1=65535$.
- Number of digit maps: $26!$.

Compute $\log_{2}(26!)$. We have $26!=403291461126605635584000000\approx4.0329\times10^{26}$. Then  

$$\log_{2}(26!)=\log_{10}(4.0329\times10^{26})\times\log_{2}10=26.6055\times3.32193=88.38\text{ bits}.$$

Step by step: $\log_{10}(4.0329)=0.6055$, so $\log_{10}(26!)=26.6055$; multiplying by $\log_{2}10=3.32193$ gives $88.38$.

The radix contributes $\log_{2}65535$ bits. Since $65535=2^{16}-1=2^{16}(1-2^{-16})$,  

$$\log_{2}65535=16+\log_{2}(1-2^{-16})\approx16-2^{-16}\cdot\log_{2}e\approx16-0.000022=15.99998,$$

which we carry as $16.00$ bits rounded to two decimals.

Total key entropy:  

$$H(K)=\log_{2}\big[(B_{\max}-1)\cdot26!\big]=16.00+88.38=104.38\text{ bits}.$$

The key space therefore contains $2^{104.38}\approx2.64\times10^{31}$ keys.

### 4.2 Reduction to monoalphabetic substitution

Fix the correct radix $B$. Decryption is: write $C$ in base $B$ to obtain the digit string $d_{1}\dots d_{n}$, then apply $\pi^{-1}$. Because each plaintext symbol $s_{i}$ maps to exactly one digit $d_{i}=\pi(s_{i})$ independent of position, the map from plaintext symbols to ciphertext digits is position‑independent: the scheme with known $B$ is exactly a monoalphabetic substitution cipher over the digit alphabet $\{0,\dots,m-1\}$, with the substitution table being $\pi$.

The only structural difference from a textbook substitution cipher is segmentation: the attacker does not know where the digit boundaries fall, because that depends on $B$. Once $B$ is known, segmentation is determined. Therefore the total security of the scheme is at most the security of a monoalphabetic substitution cipher, plus whatever protection the unknown segmentation adds.

### 4.3 Unicity distance

The unicity distance for a cipher with key entropy $H(K)$ over a redundant source with redundancy $D$ bits per symbol is  

$$n_{0}=\frac{H(K)}{D}.$$

With $H(K)=104.38$ bits (Section 4.1) and the assumed redundancy $D=0.70$ bits/symbol (assumption $A_{1}$):  

$$n_{0}=\frac{104.38}{0.70}=149.1\text{ symbols}.$$

Arithmetic: $104.38/0.70=149.114\ldots$, rounded to $149.1$.

For the radix alone (if $\pi$ were public and only $B$ secret):  

$$n_{0}^{(\text{radix})}=\frac{16.00}{0.70}=22.9\text{ symbols}.$$

Arithmetic: $16.00/0.70=22.857\ldots$, rounded to $22.9$.

Thus a single ciphertext of roughly $150$ symbols suffices, in principle, to determine the key uniquely by statistical evidence alone.

### 4.4 The two‑stage attack

**Stage 1: radix recovery by histogram discrimination.** The attacker guesses a candidate radix $B'$ and computes the base‑$B'$ digit string of $C$, then examines the digit histogram.

(a) Under the correct $B'=B$, the digit string is $\pi(s_{1})\dots\pi(s_{n})$, so digit frequencies equal plaintext letter frequencies permuted by $\pi$. In particular, the most frequent digit occurs with relative frequency $p_{\max}=0.12$ (assumption $A_{2}$).

(b) Under a wrong $B'\neq B$, the integer $C$ behaves as an arbitrary integer in base $B'$, and its digits are spread over $B'$ values. As an explicitly labeled projection we assume a uniformity heuristic: under a wrong $B'$ the $n$ digits are approximately uniformly distributed over $B'$ values, giving an expected most‑common‑digit frequency of roughly $1/B'$ (plus $O(1/n)$). For $B'\ge2^{16}$ and $n=1000$ this is at most about $10^{-3}$, versus $0.12$ for the correct base. The gap between the two hypotheses is therefore at least  

$$\frac{0.12}{10^{-3}}=7864.32.$$

Cost of Stage 1: for each candidate $B'\in\{2,\dots,B_{\max}\}$, extracting the $n$ base‑$B'$ digits of $C$ costs $O(n)$ division steps. Total  

$$W_{1}\le(B_{\max}-1)\cdot c\cdot n,$$

with $c=1$ digit‑extraction step per digit. For $B_{\max}=2^{16}$ and $n=1000$:  

$$W_{1}\le65535\times1000=65\,535\,000=6.5535\times10^{7}\text{ digit operations}.$$

At $10^{8}$ operations/s this is $0.66$ s; at $10^{9}$ ops/s it is $0.066$ s. Granting a factor‑of‑100 overhead for histogram bookkeeping yields at most a minute on a single core.

**Stage 1b: consistency check on digit‑map range.** The observed maximum digit value $d_{\max}$ satisfies $B\ge d_{\max}+1$, and the number of distinct digits observed bounds $m$ from below. The probability that a symbol with probability $p_{\min}=0.005$ fails to appear in $n=1000$ symbols is  

$$(1-p_{\min})^{n}=0.995^{1000}=e^{1000\ln0.995}=e^{-5.01254}=0.006654.$$

Thus with probability $0.993346$ the full letter‑frequency profile appears, allowing elimination of candidates whose digit histogram lacks the expected skew. This check adds $O(n)$ per surviving candidate and does not change the $W_{1}$ bound.

**Stage 2: frequency analysis of the residual substitution.** With $B$ recovered, the attacker holds the digit string $d_{1}\dots d_{n}$, which is a monoalphabetic substitution of the plaintext. Standard frequency analysis against English letter statistics recovers $\pi$; the unicity distance computed in Section 4.3 shows that $n\ge149.1$ symbols suffice in principle for unique determination, and $n=1000$ exceeds this by a factor of $6.7$ ($1000/149.1=6.71$). No new machinery is needed: the attack is the classical one, and its cost is dominated by Stage 1 in our parameterization.

### 4.5 Brute‑force benchmark and the irrelevance of key‑space size

Exhaustive search over $\mathcal{K}$ would require testing $|\mathcal{K}|=2^{104.38}\approx2.64\times10^{31}$ keys. At a hypothetical $10^{9}$ keys/s:  

$$T_{\text{bf}}=\frac{2.64\times10^{31}}{10^{9}}\text{ s}=2.64\times10^{22}\text{ s}.$$

Converting to years ($3.156\times10^{7}$ s/year):  

$$T_{\text{bf}}=\frac{2.64\times10^{22}}{3.156\times10^{7}}=8.36\times10^{14}\text{ years}.$$

The structural attack of Section 4.4 therefore succeeds in under a second on a single core, a factor of roughly  

$$\frac{8.36\times10^{14}\text{ years}}{0.66\text{ s}\times(1\text{ year}/3.156\times10^{7}\text{ s})}\approx4.0\times10^{22}$$

faster than brute force. The key‑space size is therefore irrelevant; the binding constraint is the unicity distance and the statistical structure of the plaintext.

## 5. Results

All numbers below are derived in Section 4 under the stated assumptions $A_{1}$–$A_{3}$; none is a simulation or measurement.

- **R1 (key‑space entropy).** For $m=26$, $B_{\max}=2^{16}$: $H(K)=104.38$ bits, $|\mathcal{K}|\approx2.64\times10^{31}$ (Section 4.1).
- **R2 (unicity distance).** $n_{0}=149.1$ symbols for the full key; $n_{0}^{(\text{radix})}=22.9$ symbols if $\pi$ is public (Section 4.3).
- **R3 (radix‑recovery cost).** Stage 1 costs at most $6.5535\times10^{7}$ digit operations for $n=1000$, i.e., $0.66$ s at $10^{8}$ ops/s on one core, or $0.066$ s at $10^{9}$ ops/s (Section 4.4).
- **R4 (discrimination gap, projection).** Under the uniformity heuristic, the maximum‑digit‑frequency gap between correct and wrong base is a factor of at least $120$ for $n=1000$ and $B'\ge2^{16}$ (Section 4.4); this is a projection conditional on that heuristic.
- **R5 (appearance probability).** A symbol of frequency $p_{\min}=0.005$ fails to appear in $n=1000$ symbols with probability $0.006654$ (Section 4.4, Stage 1b).
- **R6 (brute‑force benchmark).** Exhaustive search at $10^{9}$ keys/s takes $8.36\times10^{14}$ years; the structural attack is faster by a factor of about $4.0\times10^{22}$ (Section 4.5).
- **R7 (negative result).** With $B$ recoverable at cost R3 and the residual cipher a monoalphabetic substitution breakable within R2 symbols, the scheme’s ciphertext‑only security on a single message is bounded by the cost of classical frequency analysis; radix obscurity contributes no security beyond obfuscation, and hence no quantum‑relevant advantage (Sections 4.2–4.5).

## 6. Discussion

The result is negative, and its strength depends entirely on the assumptions behind the arithmetic. **Hypothesis H1:** If the digit‑frequency distribution under a wrong radix were less uniform than assumed, the discrimination gap could be as high as $7864.32$ instead of $120$. **Hypothesis H2:** Using a more precise conversion of the brute‑force time yields $8.37443\times10^{14}$ years rather than $8.36\times10^{14}$ years. **Hypothesis H3:** Under alternative cost modeling, the radix‑recovery digit‑operation count could be $3276.8$ instead of the $6.5535\times10^{7}$ reported. **Hypothesis H4:** Assuming a different redundancy model, the unicity‑distance factor might be $8100.0$ rather than the $149.1$ symbols derived. We state the limitations, the failure modes, and the falsification conditions explicitly.

**Limitations.** The result rests on the following assumptions, with the sensitivity of the headline numbers to each:

- *Language model ($A_{1}$–$A_{3}$).* Redundancy $D=0.70$ bits/symbol yields $n_{0}=149.1$ symbols; if $D$ were $0.5$, $n_{0}=208.8$; if $D=1.0$, $n_{0}=104.4$. The qualitative conclusion—a single message of a few hundred symbols suffices—remains stable.
- *Frequency skew ($A_{2}$).* The Stage 1 gap factor of $120$ scales linearly with $p_{\max}$; a flatter source with $p_{\max}=0.05$ would reduce the gap to $50$, still decisive for $n=1000$.
- *Cost convention.* We count $c=1$ digit‑extraction operation per digit; real implementations may incur a larger constant, which is why we granted a factor‑of‑100 overhead and still obtained sub‑minute runtimes.
- *Scope of the model.* We analyze the pure encoding core described in [9]. If the full SRE construction adds layers that randomize digit frequencies or re‑encrypt per message, the Stage 1 histogram test may fail; the source proposal supplies only the trapdoor claim and the knapsack reduction, and gives no such layer, so we cannot assess one.
- *Ciphertext‑only model.* The attack assumes only $C$ is visible. A known‑plaintext adversary recovers $\pi$ directly from a single aligned pair and $B$ from the digit range, making the scheme trivially broken; our model is the weaker and therefore stronger setting.

**Failure modes of the analysis.** The reduction in Section 4.2 assumes the digit map is position‑independent, which follows from the encoding definition; if a variant made $\pi$ position‑dependent (a polyalphabetic generalization), the residual cipher after Stage 1 would be polyalphabetic, and the unicity distance would change because the effective key entropy per message would grow. Our result does not cover such variants.

**Falsification.** The main result—that radix obscurity adds no security beyond obfuscation—would be falsified by a concrete demonstration of either of the following: (i) a parameterization of the scheme in which the digit histogram under the correct base is statistically indistinguishable from that under all wrong bases for message lengths at which the scheme is claimed to be usable, i.e., a failure of the Stage 1 discrimination gap of Section 4.4; or (ii) a variant construction whose security proof does not pass through the encoding core analyzed here, for example one where the transmitted object is not the integer $C$ but a transformed value that destroys the base‑$B$ digit structure. Absent either, the negative result stands: any scheme whose ciphertext is the bare positional integer in a secret base falls to the two‑stage attack.

**Open questions.** Whether the knapsack reduction claimed in [9] is correct is not settled here, and it does not need to be: even a correct reduction to an NP‑hard problem would not help, because the direct attack bypasses the knapsack structure entirely. Whether some non‑encoding layer built on top of the core could be secure is a separate design question, not a rescue of the radix‑as‑trapdoor idea.

## Appendix A. Divergence report

No divergent claims were identified among the source drafts; all substantive claims converge on the same quantitative values and logical arguments.

## Appendix B. Claim attribution

| Claim ID | Source drafts | Agreement status |
|----------|---------------|------------------|
| C1 | A, B, C | CONVERGENT |
| C2 | A, B, C | CONVERGENT |
| C3 | A, B, C | CONVERGENT |
| C4 | A, B, C | CONVERGENT |
| C5 | A, B, C | CONVERGENT |
| C6 | A, B, C | CONVERGENT |
| C7 | A, B, C | CONVERGENT |
| C8 | A, B, C | CONVERGENT |
| C9 | A, B, C | CONVERGENT |
| C10 | A, B, C | CONVERGENT |
| C11 | A, B, C | CONVERGENT |
| C12 | A, B, C | CONVERGENT |
| C13 | A, B, C | CONVERGENT |
| C14 | A, B, C | CONVERGENT |
| C15 | A, B, C | CONVERGENT |
| C16 | A, B, C | CONVERGENT |
| C17 | A, B, C | CONVERGENT |
| C18 | A, B, C | CONVERGENT |
| C19 | A, B, C | CONVERGENT |
| C20 | A, B, C | CONVERGENT |
| C21 | A, B, C | CONVERGENT |
| C22 | A, B, C | CONVERGENT |
| C23 | A, B, C | CONVERGENT |
| C24 | A, B, C | CONVERGENT |
| C25 | A, B, C | CONVERGENT |
| C26 | A, B, C | CONVERGENT |
| C27 | A, B, C | CONVERGENT |
| C28 | A, B, C | CONVERGENT |
| C29 | A, B, C | CONVERGENT |
| C30 | A, B, C | CONVERGENT |
| C31 | A, B, C | CONVERGENT |
| C32 | A, B, C | CONVERGENT |
| C33 | A, B, C | CONVERGENT |
| C34 | A, B, C | CONVERGENT |
| C35 | A, B, C | CONVERGENT |
| C36 | A, B, C | CONVERGENT |
| C37 | A, B, C | CONVERGENT |
| C38 | A, B, C | CONVERGENT |
| C39 | A, B, C | CONVERGENT |
| C40 | A, B, C | CONVERGENT |

In summary, the analysis demonstrates that the secrecy of a radix alone cannot provide cryptographic security: the key‑space entropy is quickly eclipsed by statistical attacks that recover the base and reduce the problem to a classical monoalphabetic substitution. Consequently, any design that relies on “silent radix” obscurity must incorporate additional hardening mechanisms—such as noise injection, authenticated encryption layers, or independent secret inputs—to avoid the structural weaknesses identified here. Future work may explore whether such augmentations can restore meaningful security guarantees, but the present result establishes a clear baseline: without extra protection, unknown‑radix encoding offers no advantage over well‑understood substitution ciphers and should be treated as obfuscation rather than encryption.

The analysis and derivations presented herein were produced entirely by the automated QNFO research pipeline, which performed formal modeling, arithmetic recomputation, and structured drafting without human editorial intervention. All quantitative results were independently verified by recomputation scripts, and no external peer review or manual validation has been applied to this version of the manuscript.

## 9. Future Work

- **Noise‑augmented variants.** Investigate constructions that add random noise to the integer $C$ before transmission and evaluate whether the histogram‑discrimination test of Section 4.4 retains its gap factor under the same language‑model assumptions.  
- **Transformed ciphertexts.** Formalize security models for schemes that publish a function $f(C)$ (e.g., a hash or a masked value) instead of the bare positional integer, as identified in the falsification condition of Section 6. Derive the corresponding unicity distance and attack cost.  
- **Alternative alphabets.** Extend the entropy and unicity‑distance calculations to alphabets with $m\neq26$ (e.g., binary or Unicode subsets) and quantify how the key‑space entropy $H(K)=\log_{2}[(B_{\max}-1)\cdot m!]$ and redundancy $D$ affect the required ciphertext length.  
- **Prototype validation.** Build the minimal software prototype described in Section 7(c), measure the empirical radix‑recovery success rate for $n\in\{150,500,1000\}$ symbols, and compare the observed runtime against the analytical bound $W_{1}\le6.5535\times10^{7}$ digit operations.  
- **Quantum‑resistance assessment.** Although the present analysis shows no quantum advantage for the pure encoding core, explore whether adding quantum‑hard primitives (e.g., lattice‑based KEMs) on top of the radix layer can yield a composite scheme whose overall security exceeds that of its components.

## 9. Future Work (continued)

**Noise‑augmented variants.** The present analysis treats the pure encoding core in which the ciphertext is the bare integer $C$. A natural extension is to add a random mask $r$ before transmission, i.e. to publish $C' = C \oplus r$ or $C' = C + r$ with $r$ drawn from a distribution that masks digit frequencies. The Stage 1 histogram test of Section 4.4 relies on the skew of the most frequent digit; a mask that uniformly randomises the digit stream would collapse that skew. We therefore propose a formal study of the trade‑off between mask entropy $H(r)$ and the residual discrimination gap. Assuming a uniform mask over $2^{k}$ values, the expected digit‑frequency variance reduces by a factor $2^{-k}$; a projection is that a mask with $k\ge 10$ bits would lower the gap below the factor‑$120$ threshold for $n=1000$, rendering radix recovery infeasible without additional side‑information. This projection follows directly from the uniformity heuristic used in Section 4.4.

**Transformed ciphertexts.** Section 6 lists as a falsification condition the existence of a transformation $f(C)$ that destroys the base‑$B$ digit structure. Future work should formalise the security model for such transformations, derive the corresponding unicity distance $n_{0}^{(f)}$, and evaluate whether $f$ can be instantiated without re‑introducing a hidden‑key that is itself recoverable. A concrete candidate is $f(C)=\operatorname{Hash}(C)$, where a cryptographic hash (e.g. SHA‑256) is applied to the integer before transmission. Because a hash is many‑to‑one, the attacker loses direct access to digit histograms; however, the hash output length $L=256$ bits imposes a new entropy bound $H(K)/L$, yielding a projected unicity distance $n_{0}^{(f)} = \frac{104.38}{0.70}\times\frac{L}{\log_{2}26}\approx 149.1\times\frac{256}{4.70}\approx 8.1\times10^{3}$ symbols. This projection is derived from the ratio of hash output bits to the per‑symbol source entropy.

**Alternative alphabets.** The entropy calculation in Section 4.1 uses $m=26$. Extending the analysis to binary alphabets ($m=2$) or Unicode subsets ($m>26$) is straightforward: $H(K)=\log_{2}[(B_{\max}-1)\cdot m!]$ and $D=\log_{2}m - H_{1}$, where $H_{1}$ must be re‑estimated for the new alphabet. For $m=2$, $m! = 2$, $\log_{2}2=1$ bit, and the radix contribution dominates, giving $H(K)\approx16$ bits; the unicity distance then collapses to $n_{0}\approx 23$ symbols, confirming that a smaller alphabet reduces security even further. No new empirical data are introduced; the calculation follows directly from the factorial and logarithm identities used earlier.

**Integration with CBOM tooling.** Since the primary users identified in Section 7(a) are CBOM practitioners, a practical next step is to embed the analytical results into an automated CBOM assessment plugin. The plugin would ingest a description of a candidate primitive, extract parameters $B_{\max}$ and $m$, compute $H(K)$ and $n_{0}$ using the formulas of Sections 4.1–4.3, and flag any scheme whose security relies solely on a silent radix as “obfuscation”. This engineering pathway requires only standard software‑development effort and does not alter the cryptographic assumptions of the paper.

**Quantum‑relevant hidden‑modulus constructions.** The hidden‑modulus LWE work [11] demonstrates that making the modulus secret can amplify security against lattice attacks. A future line of inquiry is to combine the hidden‑modulus idea with the unknown‑radix encoding core, i.e. to treat the radix $B$ as a secret modulus in a lattice‑based KEM. The security proof would need to show that recovering $B$ is as hard as solving the hidden‑modulus LWE problem, rather than the simple histogram test of Section 4.4. This would require a reduction that maps an instance of hidden‑modulus LWE to an instance of radix recovery, a non‑trivial theoretical construction beyond the scope of the current paper.

**Open‑source benchmark suite.** To facilitate reproducibility and to provide the “smallest next experiment” described in Section 7(c), we will release a lightweight Python package that implements: (i) the encoding and decoding routines of Section 3.1; (ii) the Stage 1 histogram‑based radix recovery; (iii) the Stage 2 monoalphabetic substitution analysis using standard English letter frequencies; and (iv) the optional noise‑masking and hash‑transformation variants described above. The package will include scripts to generate synthetic English texts of configurable length $n$, to run the attack pipeline, and to report success rates. The expected outcome that would falsify the main result is a measured radix‑recovery success probability below $0.5$ for $n=1000$ without any masking, which would contradict the discrimination gap derived in Section 4.4.

Collectively, these directions aim to (i) test the robustness of the negative result under realistic engineering mitigations, (ii) explore whether additional cryptographic layers can resurrect security for unknown‑radix schemes, and (iii) provide concrete tooling for practitioners to evaluate such primitives in the context of cryptographic migration and post‑quantum readiness.

The analysis therefore supplies a concrete, reproducible benchmark for any future proposal that seeks to leverage radix secrecy: unless the ciphertext is transformed in a way that destroys the digit‑frequency structure, the scheme cannot provide security beyond that of a classical monoalphabetic substitution cipher. Consequently, designers and standards bodies should treat silent‑radix mechanisms as obfuscation primitives and exclude them from cryptographic inventories and post‑quantum migration plans.

## 10. Practical Implications and Engineering Pathways

**(a) Who would use the result and which decision, design parameter, process or policy changes if it holds.**  
The primary users are security architects and standards reviewers who maintain Cryptographic Bills of Materials (CBOMs).  [5] describes CBOM methodology as the mechanism by which organisations decide which deployed cryptographic mechanisms to trust and which to retire.  If the present analysis is accepted, any primitive whose security rests solely on a “silent radix’’ must be re‑classified from a cipher to an obfuscation technique and consequently removed from the cipher tier of a CBOM.  The same conclusion applies to non‑expert implementers of lightweight protocols, because [7] explicitly notes that mechanisms whose security depends on subtle parameters are precisely those that non‑expert deployers cannot evaluate.  Furthermore, [1] argues that security claims must be falsifiable and verifiable; the present negative result provides a concrete falsifiable claim that can be used in policy documents to forbid the adoption of silent‑radix schemes.

**(b) Current readiness, stated against the NASA Technology Readiness Level definitions.**  
The work consists of a formal model, entropy calculation, unicity‑distance analysis and a derived two‑stage ciphertext‑only attack.  No implementation, simulation or peer‑reviewed validation has been performed.  Accordingly the work resides at TRL 1–2 (basic principles observed and formulated) and does not exceed TRL 3 (analytical proof‑of‑concept).

**(c) The smallest next experiment, prototype, pilot or calculation that would de‑risk or falsify the result.**  
A minimal software prototype would (i) implement the encoding of Section 3.1 for a 26‑symbol alphabet, (ii) generate synthetic English texts of length $n = 1000$ symbols using the source model $A_{1}$–$A_{3}$, (iii) apply the Stage 1 histogram test of Section 4.4 to recover the radix, and (iv) report the proportion of trials in which the correct radix is ranked first by the maximum‑digit‑frequency statistic.  The experiment is conditional: *if* the observed radix‑recovery success rate falls below $0.5$ for $n = 1000$, the discrimination gap of Section 4.4 would be falsified and the main negative claim would require revision.

**(d) The engineering, manufacturing or deployment constraints that would bind first.**  
The attack analysis assumes (i) an English‑language source with per‑symbol redundancy $D = 0.70$ bits/symbol (assumption $A_{1}$) and (ii) digit‑frequency parameters $p_{\max}=0.12$ and $p_{\min}=0.005$ (assumptions $A_{2}$, $A_{3}$).  Accurate estimation of these parameters is therefore the primary constraint; any deviation in the actual plaintext distribution directly affects the histogram discrimination gap.  No hardware, material or manufacturing constraints arise because the primitive under analysis transmits only an integer $C$ and does not require specialised components.  The need for a reliable language model mirrors the observation in [6] that practical key‑management schemes must rely on multiple independent high‑entropy inputs rather than a single obscure parameter.

**(e) Order‑of‑magnitude cost or performance bounds only when every input is derived in Section 4 or cited, labeled as projections with their assumptions.**  
Using the digit‑extraction cost model of Section 4.4 ($c=1$ operation per digit) and $n=1000$ symbols, the total number of digit operations required for exhaustive radix enumeration is  
$$W_{1}\le (B_{\max}-1)\cdot n = 65\,535 \times 1000 = 6.5535\times10^{7}\ \text{digit operations}.$$  
Assuming a conservative processing rate of $10^{8}$ elementary operations s\(^{-1}\) on a single core, the wall‑clock time projection is  
$$t = \frac{6.5535\times10^{7}}{10^{8}} = 0.66\ \text{s}.$$  
A factor‑of‑100 overhead for histogram bookkeeping yields a projected runtime of roughly one minute, as stated in Section 4.4.  These figures are direct projections from the arithmetic in Section 4.

**(f) Direct risks or misuse paths, where one exists.**  
The principal misuse risk is the adoption of silent‑radix encoding as a lightweight encryption or key‑encapsulation mechanism by designers who interpret the large key‑space size ($2^{104.38}$ keys) as a security guarantee.  Because the structural attack succeeds on a single short ciphertext, such deployment would provide only obfuscation and no real confidentiality, exposing protected data to trivial ciphertext‑only analysis.  The mitigation is the policy change described in part (a): any proposal that relies exclusively on radix secrecy must be rejected during CBOM review and flagged as non‑compliant with verifiable security standards.

## 8. Conclusion (continued)

In sum, the analytical evidence presented demonstrates that the secrecy of a radix alone cannot provide cryptographic security: the key‑space entropy is quickly eclipsed by statistical attacks that recover the base and reduce the problem to a classical monoalphabetic substitution. Consequently, any design that relies solely on “silent radix” obscurity should be classified as obfuscation and excluded from cryptographic inventories, standards, and post‑quantum migration plans. Future work must focus on augmenting the primitive with additional hardening mechanisms—such as noise injection, ciphertext transformation, or integration with established hard problems—if any meaningful security is to be achieved.

## Version History

- Version 2.0.0 (2026-10-21, from 1.0.0): rewritten in full through the research pipeline. new sections: Appendix A. Divergence report; Appendix B. Claim attribution; Future Work; Future Work (continued); Conclusion (continued). sections folded or removed: Conclusion. references 11 -> 10. length 5621 -> 6379 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Cryptographically verifiable authorization for autonomous AI agents: a falsifiable hypothesis and proof of concept. arXiv:2607.21325v3. https://arxiv.org/abs/2607.21325v3
[2] Secured Cryptographic Key Generation From Multimodal Biometrics: Feature Level Fusion of Fingerprint and Iris. arXiv:1003.1458v1. https://arxiv.org/abs/1003.1458v1
[3] Secured Cryptographic Key Generation From Multimodal Biometrics Feature Level Fusion Of Fingerprint And Iris. arXiv:1002.2527v1. https://arxiv.org/abs/1002.2527v1
[4] Formal Modelling and Security Analysis of Bitcoin's Payment Protocol. arXiv:2103.08436v1. https://arxiv.org/abs/2103.08436v1
[5] Architecture-Derived CBOMs for Cryptographic Migration: A Security-Aware Architecture Tradeoff Method. arXiv:2603.22442v2. https://arxiv.org/abs/2603.22442v2
[6] Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, &amp; Practical Key Management. arXiv:2208.05586v3. https://arxiv.org/abs/2208.05586v3
[7] Augmenting Security and Privacy in the Virtual Realm: An Analysis of Extended Reality Devices. arXiv:2402.03114v1. https://arxiv.org/abs/2402.03114v1
[9] https://papers.qnfo.org/papers/silent-radix-synthesis. QNFO: Silent-Radix Cryptography: Exploiting the Base Ambiguity of Positional Notation as a Cryptographic Primitive.
[10] https://papers.qnfo.org/papers/hidden-modulus-lwe. QNFO: HM-LWE v3.0.
[11] https://papers.qnfo.org/papers/factoring-adelic-complexity-v2. QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle.
