# Ultrametric p-Adic Arithmetic as Energy-Proportional Precision Computing: An Energy Model for Digit-Terminable Multiply-Accumulate

## Abstract

Fixed-width Archimedean floating-point arithmetic pays a constant energy cost per multiply-accumulate (MAC) regardless of the precision actually required by the computation. The gap this paper addresses is the absence of any explicit joules-per-operation model connecting non-Archimedean digit structure to CMOS switching energy: the p-adic literature establishes ultrametric hierarchies as mathematically natural, but no prior work quantifies what digit-terminable arithmetic would save in energy. We formalize a digit-serial p-adic MAC model with energy $E_p(k) = k^2 e_d + k\, e_a$ in the number of retained digits $k$, and compare it against reported floating-point MAC energies of $3.7$ pJ at 45 nm and $0.9$ pJ at 7 nm. Under a stated bit-cell energy assumption of $e_d = 0.01$ pJ and $e_a = 0.001$ pJ at 45 nm, we compute a break-even precision of $k^* = 19$ binary p-adic digits at 45 nm and $k^* = 9$ at 7 nm. For a quantization tolerance of $\varepsilon = 10^{-2}$, requiring $k = 7$ digits, the p-adic MAC costs $0.497$ pJ versus $3.7$ pJ, an $86.57\%$ saving at 45 nm and $44.78\%$ at 7 nm. A labeled projection for a heterogeneous $10^9$-MAC inference workload gives a $58.0\%$ total-energy saving, with computed sensitivity spanning $-25.5\%$ to $87.2\%$ over $e_d \in [0.003, 0.03]$ pJ. We state the sufficient condition for p-adic advantage, the falsifiers, and the engineering pathway from analytical model to measured digit-cell energy.

## 1. Introduction

Energy is now the binding constraint on large-scale computation: data movement, not arithmetic, dominates the joule budget of modern accelerators, and every operation pays the full width of its datapath whether or not the application needs that width. Floating-point MAC units are built to a worst-case precision — we assume a 24-bit mantissa for the binary32 baseline, an explicit modeling assumption stated in Section 3.2 — and their energy per operation is essentially independent of the numerical difficulty of the particular operands. This is an Archimedean assumption baked into hardware: the absolute value underlying IEEE arithmetic is the usual real absolute value, in which digits carry global position weights and no digit can be meaningfully final until carries from all less significant positions have resolved. The designers of accelerators for neural-network inference, scientific computing, and signal processing therefore face a fixed trade: pay full-width energy on every MAC, or accept the toolchain and range costs of narrower fixed-point formats. A hardware primitive whose energy scaled with the precision actually demanded would change that trade at its root, letting a single datapath serve both a $10^{-2}$-tolerant inference layer and a full-precision accumulation without re-synthesis.

The p-adic numbers $\mathbb{Q}_p$ offer a different topology. The p-adic absolute value $|\cdot|_p$ is ultrametric — it satisfies $|x+y|_p \le \max(|x|_p, |y|_p)$ — and p-adic digits are ordered by increasing significance in a way that makes truncation semantically clean: a p-adic integer known to $k$ digits is correct to within $p^{-k}$ in $|\cdot|_p$, and addition proceeds digit-by-digit from the least significant residue upward with carries moving only toward higher digits. A computation that needs only $k$ digits of accuracy can therefore stop after $k$ digit-slices, and the energy it consumed is a function of $k$, not of a fixed machine word length.

This paper takes seriously the conjecture that this structure enables energy-proportional precision computing: hardware that performs p-adic MAC can stop after $k$ digits, so its energy scales with the precision actually demanded, roughly as $O(k^2)$ for the convolution structure of multiplication, rather than as a constant full-width cost.

**Conjecture 1 (Energy-proportional precision).** There exist p-adic arithmetic architectures whose energy per MAC operation scales polynomially in the number of computed digits $k$, whereas an Archimedean floating-point MAC costs a fixed $E_f$ independent of $k$; consequently, for workloads whose required precision is heterogeneous and bounded, p-adic arithmetic achieves lower joules per compute.

Our contributions are:

1. A formal energy model $E_p(k) = k^2 e_d + k\, e_a$ for digit-serial p-adic MAC, with every coefficient stated as an explicit assumption, derived in Section 3 and evaluated with full arithmetic in Section 4.
2. A computed break-even analysis against reported floating-point MAC energies of $3.7$ pJ at 45 nm and $0.9$ pJ at 7 nm, yielding $k^*(45) = 19$ and $k^*(7) = 9$ (Section 4, restated in Section 5).
3. A precision-demand analysis mapping application error tolerances $\varepsilon$ to required digit counts $k(\varepsilon)$ and hence to energy, with a worked example at $\varepsilon = 10^{-2}$ giving $86.57\%$ and $44.78\%$ per-MAC savings (Section 4).
4. A labeled workload-level projection of $58.0\%$ total-energy saving for a heterogeneous $10^9$-MAC inference layer, with computed sensitivity bounds (Section 4.E), and a labeled projection for ultrametric tree-structured off-chip communication (Section 4.F).
5. A statement of the sufficient condition under which p-adic architectures beat Archimedean ones in joules per compute, together with the limitations, failure modes, and falsifiers of the model (Sections 5 and 6), and the practical pathway from this analytical model to measured hardware (Section 7).

We are explicit throughout about where the argument is conjectural: the energy coefficients are assumptions, the workload figures are projections, and the claim stands or falls on the stated inputs.

## 2. Background and Related Work

The p-adic literature relevant here spans pure number theory, mathematical physics, and data modeling; we review the works in their given numbering.

**[1] On the p-adic Beilinson conjecture for number fields.** This work formulates a conjectural p-adic analogue of Borel's theorem, relating regulators of higher $K$-groups of number fields to special values of the corresponding zeta-functions via syntomic regulators and p-adic $L$-functions, and states a conjecture about the precise relation between the p-adic and classical situations. Its relevance here is structural: it exemplifies how p-adic and Archimedean invariants come in parallel pairs — the same duality our energy model exploits when it pairs a p-adic digit-serial cost $E_p(k)$ with a floating-point fixed cost $E_f$.

**[2] From Data to the p-Adic or Ultrametric Model.** This paper models anomaly and change in data by embedding the data in an ultrametric space: Correspondence Analysis endows the information space with a Euclidean metric, and an induced ultrametric hierarchy is then used to read off changepoints or anomalous occurrences at a range of scales, demonstrated on a film script and on data from the Colombian civil strife. It shows that ultrametric structure is practically extractable from real sequential data, supporting our premise that hierarchical, tree-like organization — the precondition for digit-terminable computation — is natural for workloads, not merely a number-theoretic curiosity.

**[3] Application of p-adic analysis methods in describing Markov processes on ultrametric spaces.** The authors reduce the study of stationary Markov processes on ultrametric spaces isometrically embeddable in $\mathbb{Q}_p$ to processes on $\mathbb{Q}_p$ itself: the Cauchy problem for the Kolmogorov–Feller equation on such a space reduces to a pseudo-differential equation on $\mathbb{Q}_p$, importing the machinery of p-adic mathematical physics. For us this is a template for hierarchical state evolution: a computation whose state space is ultrametric can be processed level-by-level, exactly the digit-serial discipline our MAC model assumes.

**[4] On generalized Iwasawa main conjectures and p-adic Stark conjectures for Artin motives.** Given an odd prime $p$ and a $p$-stabilized Artin representation, this work introduces a family of $p$-adic Stark regulators, formulates an Iwasawa–Greenberg main conjecture and a $p$-adic Stark conjecture as an explicit strengthening of conjectures of Perrin-Riou and Benois, and proves an interpolation formula (Theorem A) for a generator of the characteristic ideal of the associated $\Lambda$-module. It illustrates the depth of p-adic analytic machinery available for controlling convergence and precision in p-adic settings — the mathematical counterpart of the precision-certification question (how many digits suffice?) that our energy model turns into a hardware parameter.

**[5] On Phase Transitions for P-Adic Potts Model with Competing Interactions on a Cayley Tree.** Reducing the description of $p$-adic Gibbs measures for a three-state Potts model with competing interactions on a Cayley tree of order two to a recursive equation, this paper proves that a phase transition occurs if and only if $p = 3$ for any nonzero interaction, and establishes uniqueness of the Gibbs measure otherwise. The Cayley tree is precisely the ultrametric hierarchy; the paper shows that recursive, level-by-level processes on such trees admit sharp, exactly solvable criteria — analogous to the sharp break-even criterion $k \le k^*$ we derive for energy.

**[6] p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound.** This paper introduces p-adic equiangular lines in $\mathbb{Q}_p^d$ — collections of unit vectors in a p-adic Hilbert space with constant mutual inner-product magnitude — and derives the first fundamental relation between common angle, dimension, and line count, the inequality $|n|^2 \le |d| \max\{|n|, \gamma^2\}$, which the authors call the p-adic van Lint–Seidel relative bound. Finite frames and signal representations over $\mathbb{Q}_p$ suggest that transform-style workloads (the consumers of MAC arrays) can be formulated intrinsically in p-adic inner-product spaces, which is the representational prerequisite for our architecture proposal.

**[7] The p-adic analytic subgroup theorem revisited.** Revisiting the p-adic analogue of Wüstholz's analytic subgroup theorem — the theorem that an analytic subgroup of a commutative algebraic group contains a non-trivial algebraic point if and only if it contains a non-trivial algebraic subgroup — this paper proves the p-adic version by induction on $\dim G$, using $p$-adic exponential and logarithm maps over complete subfields of $\mathbb{C}_p$. It supplies the rigor culture — exact, valuation-based control of analytic objects — against which our engineering-level precision bounds ($|e|_p \le p^{-k}$) should be read as deliberately coarse but honest first approximations.

**[8] A p-Adic Model of DNA Sequence and Genetic Code.** Using basic properties of p-adic numbers, this work builds an ultrametric p-adic information space whose elements are nucleotides, codons, and genes, shows that a 5-adic model is appropriate for DNA sequence, and derives from 5-adic and 2-adic distances a classification of codons into quadruplets and doublets, yielding the principle that p-adically close codons correspond to the same amino acid. It is the clearest precedent in the literature reviewed here for the claim that discrete, hierarchical, symbolic-combinatorial data — the kind that dominates AI workloads — maps naturally onto small-prime p-adic digit hierarchies.

What is missing from all of these strands, and what this paper supplies, is an explicit joules-per-operation model connecting ultrametric digit structure to CMOS switching energy.

## 3. Methods

### 3.1 p-adic representation and digit-serial computation

Fix a prime $p$. Every $x \in \mathbb{Z}_p$ (the ring of p-adic integers) has a canonical expansion

$$x = \sum_{i=0}^{\infty} a_i p^{i}, \qquad a_i \in \{0, 1, \dots, p-1\},$$

and the p-adic absolute value satisfies $|x|_p = p^{-v_p(x)}$, where $v_p(x)$ is the p-adic valuation. The ultrametric inequality implies that arithmetic on residues modulo $p^k$ is self-contained:

$$\left( x \bmod p^k \right) \circ \left( y \bmod p^k \right) \equiv (x \circ y) \bmod p^k, \qquad \circ \in \{+, \times\},$$

and truncation error is bounded by $p^{-k}$:

$$\left| x - \sum_{i=0}^{k-1} a_i p^{i} \right|_p \le p^{-k}.$$

Multiplication of two $k$-digit truncations is a digit convolution: the product digit at position $j$ depends on digit pairs $(a_i, b_{j-i})$, so a full $k$-digit product requires $k^2$ digit-digit products, each over the finite alphabet of size $p$.

### 3.2 Energy model

We define the model inputs, each stated explicitly:

- $e_d$: energy of one digit-digit product-and-accumulate (a $\lceil \log_2 p \rceil \times \lceil \log_2 p \rceil$-bit multiply plus small add) in a digit-serial p-adic array. **Stated assumption:** $e_d = 0.01$ pJ at 45 nm, i.e., $1.0 \times 10^{-2}$ pJ, consistent in order of magnitude with bit-level CMOS multiply energies at that node; this is a modeling assumption, not a measurement.
- $e_a$: energy of one digit-position accumulation pass, **stated assumption** $e_a = 0.001$ pJ at 45 nm.
- $E_f(45) = 3.7$ pJ: energy of one full-width floating-point MAC at 45 nm (given input).
- $E_f(7) = 0.9$ pJ: energy of one full-width floating-point MAC at 7 nm (given input).
- $p = 2$ throughout the numeric analysis, so one p-adic digit carries $\log_2 p = 1$ bit of precision.
- $b_f = 24$: the mantissa width of the binary32 floating-point baseline. **Stated assumption:** we assume a 24-bit mantissa for binary32; this is a modeling assumption used only for the per-bit comparison in Section 4.D, not a measurement.

The energy of a $k$-digit p-adic MAC is then

$$E_p(k) = k^2 e_d + k\, e_a.$$

This is the $O(k^2)$ scaling of the conjecture: the quadratic term is the convolution structure of multiplication, the linear term the digit-serial accumulation. Early termination means the hardware computes only the first $k$ digits, where $k$ is set by the application's precision demand.

### 3.3 Precision demand from error tolerance

If an application tolerates relative error $\varepsilon$, truncation to $k$ digits suffices when $p^{-k} \le \varepsilon$, i.e.,

$$k(\varepsilon) = \left\lceil \frac{\ln(1/\varepsilon)}{\ln p} \right\rceil.$$

### 3.4 Break-even condition

The p-adic MAC beats the floating-point MAC when $E_p(k) < E_f$. With $e_a \ll e_d$ we use the leading term for the break-even digit count:

$$k^* = \left\lfloor \sqrt{\frac{E_f}{e_d}} \right\rfloor.$$

### 3.5 Workload-level energy

For a workload of $N$ MACs whose required precisions $k_1, \dots, k_N$ vary, total p-adic energy is $\sum_{n=1}^{N} (k_n^2 e_d + k_n e_a)$ versus $N \cdot E_f$ for fixed-width floating point. We evaluate a heterogeneous workload as a labeled projection in Section 4.

## 4. Analysis

Every number below is derived from the inputs stated in Section 3.2: $E_f(45) = 3.7$ pJ, $E_f(7) = 0.9$ pJ, $e_d = 0.01$ pJ, $e_a = 0.001$ pJ, $p = 2$.

**A. Break-even at 45 nm.** With $E_f(45) = 3.7$ pJ and $e_d = 0.01$ pJ:

$$k^*(45) = \left\lfloor \sqrt{\frac{3.7}{0.01}} \right\rfloor = \lfloor \sqrt{370} \rfloor.$$

Since $19^2 = 361$ and $20^2 = 400$, we get $\sqrt{370} \approx 19.24$, so

$$k^*(45) = 19.$$

A p-adic MAC of up to 19 binary p-adic digits costs less than the $3.7$ pJ floating-point MAC at 45 nm. Check at $k = 19$: $E_p(19) = 19^2 \times 0.01 + 19 \times 0.001 = 3.61 + 0.019 = 3.629$ pJ $< 3.7$ pJ. At $k = 20$: $E_p(20) = 4.00 + 0.020 = 4.020$ pJ $> 3.7$ pJ. The break-even is confirmed.

**B. Break-even at 7 nm.** With $E_f(7) = 0.9$ pJ:

$$k^*(7) = \left\lfloor \sqrt{\frac{0.9}{0.01}} \right\rfloor = \lfloor \sqrt{90} \rfloor.$$

Since $9^2 = 81$ and $10^2 = 100$, $\sqrt{90} \approx 9.49$, so

$$k^*(7) = 9.$$

Check: $E_p(9) = 81 \times 0.01 + 9 \times 0.001 = 0.81 + 0.009 = 0.819$ pJ $< 0.9$ pJ; $E_p(10) = 1.00 + 0.010 = 1.010$ pJ $> 0.9$ pJ.

**C. Worked example at $\varepsilon = 10^{-2}$, 45 nm.** From Section 3.3, for $p = 2$ and $\varepsilon = 10^{-2}$:

$$k(10^{-2}) = \left\lceil \frac{\ln(100)}{\ln 2} \right\rceil = \left\lceil \frac{4.60517}{0.693147} \right\rceil = \lceil 6.64386 \rceil = 7.$$

Then

$$E_p(7) = 7^2 \times 0.01 + 7 \times 0.001 = 49 \times 0.01 + 0.007 = 0.49 + 0.007 = 0.497 \text{ pJ}.$$

The saving per MAC against the 45 nm floating-point MAC is

$$\Delta E = 3.7 - 0.497 = 3.203 \text{ pJ},$$

a fractional saving of $3.203/3.7 = 0.8657$, i.e., $86.57\%$, computed exactly as

$$\frac{3.203}{3.7} = 0.8656756756756757 \approx 86.57\%.$$

At 7 nm the same $k = 7$ MAC costs $0.497$ pJ versus $0.9$ pJ, a saving of $0.9 - 0.497 = 0.403$ pJ, i.e., $0.403/0.9 = 0.4477777777777778 \approx 44.78\%$.

**D. Energy per bit of precision.** With $b = k \log_2 p = k$ bits for $p = 2$, the energy per delivered bit is

$$\frac{E_p(k)}{b} = \frac{k^2 e_d + k e_a}{k} = k e_d + e_a,$$

which is linear in $k$: $0.01 k + 0.001$ pJ/bit. At $k = 7$: $0.07 + 0.001 = 0.071$ pJ/bit. The floating-point MAC delivers the assumed $b_f = 24$ mantissa bits (Section 3.2 assumption) for $3.7$ pJ at 45 nm, i.e., $3.7/24 = 0.15416666666666667$ pJ/bit. The p-adic digit-serial unit at $k = 7$ delivers precision at a fraction $0.071/0.15416666666666667 = 0.4606$ of the floating-point per-bit cost, i.e., about $46.0\%$.

**E. Workload projection (labeled projection).** Consider a neural-network inference layer with $N = 10^{9}$ MACs and a heterogeneous precision profile in which a fraction $f = 0.8$ of MACs need only $k = 7$ digits and a fraction $1 - f = 0.2$ need full $k = 24$ digits (comparable to binary32 mantissas). **Assumptions:** the $e_d$, $e_a$ values of Section 3.2 hold; precision demands are as stated; no overhead for precision scheduling. Then

$$E_{\text{total}} = N\left[ f\, E_p(7) + (1-f)\, E_p(24) \right].$$

$E_p(24) = 576 \times 0.01 + 24 \times 0.001 = 5.76 + 0.024 = 5.784$ pJ. So

$$E_{\text{total}} = 10^{9} \times \left[ 0.8 \times 0.497 + 0.2 \times 5.784 \right] = 10^{9} \times \left[ 0.3976 + 1.1568 \right] = 1.5544 \times 10^{9} \text{ pJ} = 1.5544 \text{ mJ}.$$

The floating-point baseline is $10^{9} \times 3.7$ pJ $= 3.7$ mJ. The projected saving is $(3.7 - 1.5544)/3.7 = 2.1456/3.7 = 0.580$, i.e., $58.0\%$, with the caveat that $E_p(24) > E_f(45)$: at 45 nm, full binary32-equivalent precision is more expensive in this p-adic model, so the saving comes entirely from the early-terminating majority.

Uncertainty (computed sensitivity, same projection assumptions): at $e_d = 0.003$ pJ, $E_p(7) = 49 \times 0.003 + 0.007 = 0.147 + 0.007 = 0.154$ pJ and $E_p(24) = 576 \times 0.003 + 0.024 = 1.728 + 0.024 = 1.752$ pJ, so the per-MAC cost is $0.8 \times 0.154 + 0.2 \times 1.752 = 0.1232 + 0.3504 = 0.4736$ pJ and the saving is $(3.7 - 0.4736)/3.7 = 3.2264/3.7 = 0.8720$, i.e., $87.2\%$. At $e_d = 0.03$ pJ, $E_p(7) = 49 \times 0.03 + 0.007 = 1.47 + 0.007 = 1.477$ pJ and $E_p(24) = 576 \times 0.03 + 0.024 = 17.28 + 0.024 = 17.304$ pJ, so the per-MAC cost is $0.8 \times 1.477 + 0.2 \times 17.304 = 1.1816 + 3.4608 = 4.6424$ pJ, exceeding $E_f(45) = 3.7$ pJ; the saving is $(3.7 - 4.6424)/3.7 = -0.9424/3.7 = -0.2547$, i.e., a $25.5\%$ loss. The projected saving therefore ranges over $-25.5\%$ to $87.2\%$ across $e_d \in [0.003, 0.03]$ pJ; we report the point value only under the stated $e_d = 0.01$ pJ.

**F. Off-chip communication (labeled projection).** We assume, as a projection input and not a measurement, that off-chip DRAM traffic dominates accelerator energy, with per-bit transport energies one to two orders of magnitude above on-chip arithmetic energies. Because p-adic digit hierarchies are trees (digits at level $i$ depend only on levels $\le i$), a precision-adaptive memory system could stream only the leading $k$ digits of weights and activations, cutting off-chip bit-traffic proportionally to $k$ rather than to full word width. As one illustrative projection with fully stated assumptions: if a workload moves $B = 100 \times 10^{9}$ bytes off-chip at $0.2$ nJ/byte, flat communication costs $0.2 \times 10^{11} = 2 \times 10^{10}$ nJ $= 20$ J; if tree-structured aggregation halves the moved volume (factor $f = 0.5$, assumed), the cost is $10$ J. We flag both the byte count, the per-byte energy, and the halving factor as assumptions, not measurements; no hardware prototype or trace supports them.

## 5. Results

All results are computed in Section 4 from the stated inputs ($E_f(45) = 3.7$ pJ, $E_f(7) = 0.9$ pJ, $e_d = 0.01$ pJ, $e_a = 0.001$ pJ, $p = 2$), except items 5 and 6, which are labeled projections.

1. **Break-even precision at 45 nm:** $k^*(45) = 19$ binary p-adic digits; verified by $E_p(19) = 3.629$ pJ $< 3.7$ pJ and $E_p(20) = 4.020$ pJ $> 3.7$ pJ.
2. **Break-even precision at 7 nm:** $k^*(7) = 9$ digits; verified by $E_p(9) = 0.819$ pJ $< 0.9$ pJ and $E_p(10) = 1.010$ pJ $> 0.9$ pJ.
3. **Energy at $\varepsilon = 10^{-2}$ tolerance ($k = 7$):** $E_p(7) = 0.497$ pJ, saving $3.203$ pJ ($86.57\%$) versus 45 nm floating point and $0.403$ pJ ($44.78\%$) versus 7 nm floating point.
4. **Energy per precision bit:** $k e_d + e_a = 0.071$ pJ/bit at $k = 7$, versus $3.7/24 = 0.15416666666666667$ pJ/bit for binary32 at 45 nm — a ratio of $0.071/0.15416666666666667 = 0.4606$, i.e., about $46.0\%$ of the floating-point per-bit cost.
5. **Projected workload saving (projection, assumptions in Section 4.E):** for $N = 10^{9}$ MACs with $f = 0.8$ at $k = 7$ and $1 - f = 0.2$ at $k = 24$, p-adic total $1.5544$ mJ versus floating-point $3.7$ mJ, a $58.0\%$ saving at 45 nm; computed sensitivity to $e_d \in [0.003, 0.03]$ pJ spans $-25.5\%$ (a loss) to $87.2\%$, as derived in Section 4.E.
6. **Off-chip traffic reduction (projection):** under the stated assumptions of Section 4.F, flat communication costs $20$ J versus $10$ J under an assumed halving factor; hypothesis-level, with no measured support.

The sufficient condition for p-adic advantage follows from the model: the application's precision demand $k(\varepsilon)$ must satisfy $k(\varepsilon) \le k^* = \lfloor \sqrt{E_f/e_d} \rfloor$, and the precision-weighted fraction of MACs meeting this condition must be large enough that the aggregate saving $\sum_n \left[ E_f - E_p(k_n) \right]$ is positive. Both clauses are checkable against a workload's precision profile and a measured $e_d$.

## 6. Discussion

**Limitations of the energy model.** The coefficient $e_d = 0.01$ pJ is an assumption, not a measurement or a synthesis-tool extraction, and every headline number in Sections 4 and 5 inherits that assumption linearly or quadratically. Real digit-serial arrays pay costs the model omits: digit scheduling and control, precision-adaptive sequencing logic, p-adic-to-Archimedean conversion at I/O boundaries, and the non-ideal scaling of small-integer multipliers at advanced nodes. The $O(k^2)$ convolution count is the algorithmic minimum for a one-shot product; a streaming MAC that reuses digit-products across accumulation steps could approach $O(k)$ energy per operation, which would only strengthen the conclusions, while a naive design could pay unmodeled $O(k^2)$ control overheads. The node-to-node comparison is also internally inconsistent as stated: $e_d$ should shrink with the node alongside $E_f$. If $e_d$ scaled from 45 nm to 7 nm by the same factor as $E_f$, i.e., $e_d \to 0.01 \times 0.9/3.7 = 0.00243$ pJ, then $k^*(7) = \lfloor \sqrt{0.9/0.00243} \rfloor = \lfloor \sqrt{370.37} \rfloor = 19$, restoring parity in break-even precision while lowering absolute energies; the computed $k^*(7) = 9$ therefore reflects holding $e_d$ fixed, and we flag that convention explicitly.

**Failure modes.** (i) Workloads requiring uniformly high precision ($k \ge k^*$) gain nothing; the advantage is entirely an early-termination effect, and the sensitivity bound at $e_d = 0.03$ pJ shows the sign of the saving can flip. (ii) The p-adic absolute value is not the Archimedean one: real-relative error tolerances ($|e|/|x| \le \varepsilon$ over $\mathbb{R}$) do not translate directly to $|\cdot|_p$ bounds without an embedding convention; the step $p^{-k} \le \varepsilon$ assumes the quantity of interest has $|x|_p \le 1$, which fails for quantities with negative p-adic valuation, where more digits are needed. (iii) Algorithms with cancellation or division behave differently ultrametrically; neural-network MAC is favorable precisely because it is division-free and its accumulation is tolerant in the ultrametric sense. (iv) Off-chip memory systems are not precision-adaptive today; digit-terminable streaming is a systems problem at least as hard as the arithmetic one.

**What would falsify the claims.** A silicon or RTL-level demonstration showing that a digit-serial p-adic MAC's measured energy per operation does not fall below the fixed-width floating-point MAC for any $k \le k^*$ would falsify the core conjecture under the stated assumptions. A second falsifier: showing that realistic inference workloads rarely tolerate $k < k^*$, i.e., that precision demands sit uniformly at or above binary32 level, which would erase the savings even if the arithmetic model holds. A third: demonstrating that precision-scheduling overhead (control, conversion, irregular memory access) exceeds the computed per-MAC saving of $3.203$ pJ at 45 nm.

**Against ourselves.** The strongest counterargument is that mixed-precision and block-floating-point formats already deliver energy-proportional precision with mature toolchains; the p-adic proposal must beat those adaptive baselines, not fixed-width binary32, and this paper makes that comparison only qualitatively. The ultrametric topology means p-adic "closeness" is divisibility-closeness, which matches some workloads — [2] demonstrates ultrametric hierarchies extracted from real sequential data, and [8] shows p-adically close codons correspond to the same amino acid — but is alien to others; the applicability boundary is an empirical question this paper does not settle. A further structural point is Ostrowski's theorem, taken here as a standard result: every nontrivial absolute value on $\mathbb{Q}$ is equivalent either to the Archimedean one or to some $|\cdot|_p$. That theorem cuts both ways for us — it guarantees that any naturally ultrametric structure lives in a p-adic field for some prime $p$, but it also means workloads lacking tree structure have no p-adic representation to exploit. Finally, the mathematical works [1], [4], and [7] supply exact, valuation-based control of p-adic analytic objects, against which our engineering-level bound $|e|_p \le p^{-k}$ should be read as deliberately coarse; [5]'s sharp phase-transition criterion ($p = 3$ exactly, on a Cayley tree of order two) is a reminder that ultrametric systems can admit exact thresholds, of which our $k^*$ is the energy analogue.

**Open questions.** What is the measured $e_d$ for a $p = 2$ digit cell at 7 nm and at 45 nm? Can ultrametric tree-structured addressing reduce cache-tile and DRAM row-activation energy in practice? Do p-adic frames in the sense of [6], whose van Lint–Seidel relative bound $|n|^2 \le |d| \max\{|n|, \gamma^2\}$ constrains line counts in $\mathbb{Q}_p^d$, admit fast transforms with sub-$k^*$ precision? Under what conditions does a joint use of both Ostrowski places — the adelic viewpoint — yield savings beyond either place alone? Does the level-by-level reduction of [3], which turns Markov processes on ultrametric spaces into pseudo-differential equations on $\mathbb{Q}_p$, extend to a theory of precision-adaptive stochastic computation whose energy cost is itself ultrametrically stratified?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The prospective users are accelerator architects and physical-design engineers building inference datapaths for neural networks, and compiler/toolchain teams that assign numeric formats per layer. If the result holds, the design parameter that changes is the precision-energy coupling: instead of choosing among discrete fixed-width formats (int8, fp16, binary32), a designer would allocate a digit budget $k$ per layer from the tolerance $\varepsilon$ via $k(\varepsilon) = \lceil \ln(1/\varepsilon)/\ln p \rceil$, and the datapath's energy would follow that allocation rather than a fixed word width. The policy that changes on the toolchain side is precision assignment: a p-adic backend makes fine-grained, per-tensor precision a first-class compile-time parameter with a continuous energy cost curve $E_p(k)$, rather than a step function over format choices. No user can act on this result today, because no digit-serial p-adic MAC has been built and measured; at the present stage the work is foundational, supplying the cost model against which any such build would be justified.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is analytical: it derives a model, computes break-even points from stated assumptions, and proposes no hardware. Unreviewed analytical work sits at TRL 1–2, and analytical work cannot exceed TRL 3; this paper is TRL 2 — the concept and its cost model are formulated, but the enabling digit-cell energy $e_d$ is assumed, not measured, and no proof-of-concept hardware exists.

**(c) The smallest next experiment.** The minimal de-risking step is a synthesis-and-extraction study, not a tape-out: describe a $p = 2$ digit cell (a $1 \times 1$-bit multiply with a small accumulate) in a hardware description language, synthesize it at a 45 nm-class library, and extract switching energy per digit-product and per accumulation pass. The outcome that refutes the model is an extracted $e_d$ above $0.01$ pJ by enough that $k^* = \lfloor \sqrt{E_f/e_d} \rfloor$ falls below the digit counts that inference tolerances actually demand — for example, $e_d > 3.7/49 \approx 0.0755$ pJ would push $k^*$ below $k = 7$ at 45 nm and eliminate the worked example's saving. A second, complementary step is a workload trace study: instrument an existing inference model to record the per-layer error tolerance actually needed under a task-level metric, and check whether the fraction of MACs with $k(\varepsilon) \le k^*$ is large enough for a positive aggregate saving under Section 5's sufficient condition.

**(d) Binding constraints.** In the order they would likely bind: first, the digit-cell energy $e_d$, since every result scales with it and the sensitivity range in Section 4.E shows the saving flips sign at $e_d = 0.03$ pJ under the projection's assumptions; second, precision-scheduling and control overhead, which the model omits and which the third falsifier bounds at $3.203$ pJ per MAC at 45 nm; third, p-adic-to-Archimedean conversion at I/O boundaries, whose cost is unmodeled and could consume the per-MAC saving for small-$k$ layers; fourth, memory-system adaptivity, since digit-terminable streaming requires precision-aware caches and DRAM controllers that do not exist. Whether ultrametric tree-structured addressing can reduce row-activation energy remains an open question; no grounding in this paper supports a number for it.

**(e) Order-of-magnitude bounds (projections).** Under the assumptions of Section 4.E ($e_d = 0.01$ pJ, $e_a = 0.001$ pJ, $f = 0.8$ at $k = 7$, $N = 10^{9}$ MACs), the projected per-inference-layer arithmetic energy is $1.5544$ mJ p-adic versus $3.7$ mJ floating-point, i.e., an order of a few millijoules per $10^9$-MAC layer at 45 nm, with the sensitivity band $-25.5\%$ to $87.2\%$ relative saving. Under the assumptions of Section 4.F ($B = 100 \times 10^{9}$ bytes at $0.2$ nJ/byte, halving factor $0.5$), the projected communication energy is $10$ J versus $20$ J flat — an order of joules, dominated by memory traffic, which is why the communication pathway matters more than the arithmetic one if both materialize. Both figures are projections from stated assumptions, not measurements.

**(f) Risks and misuse paths.** The principal misuse is quoting the headline savings ($86.57\%$, $58.0\%$) without the assumptions that generate them: the numbers are conditional on $e_d = 0.01$ pJ and the stated precision profile, and the sensitivity band includes a $25.5\%$ loss. A secondary risk is overclaiming numerical equivalence: a $p^{-k}$ bound in $|\cdot|_p$ is not a relative-error guarantee over $\mathbb{R}$, and any certification built on the model must restate tolerances in the appropriate metric before deployment decisions are made.

## 8. Conclusion

We formalized the conjecture that p-adic, ultrametric arithmetic enables energy-proportional precision computing. Under explicit assumptions ($e_d = 0.01$ pJ, $e_a = 0.001$ pJ at 45 nm, $p = 2$), a digit-serial p-adic MAC with energy $E_p(k) = k^2 e_d + k e_a$ beats a $3.7$ pJ floating-point MAC for up to $k^* = 19$ digits at 45 nm and a $0.9$ pJ MAC for up to $k^* = 9$ digits at 7 nm; at a $10^{-2}$ error tolerance ($k = 7$), the computed saving is $86.57\%$ at 45 nm and $44.78\%$ at 7 nm, and a labeled projection for a heterogeneous $10^9$-MAC workload gives a $58.0\%$ total-energy saving with a computed sensitivity band of $-25.5\%$ to $87.2\%$. The sufficient condition for p-adic advantage is an application precision demand below the break-even digit count, with a positive precision-weighted fraction of qualifying MACs. The result is a modeling contribution whose assumptions — especially $e_d$ and the realizability of digit-terminable memory streaming — define the empirical agenda: extracted digit-cell energies, precision profiles of real workloads, and prototype digit-serial arrays. If those confirm the model, ultrametric arithmetic offers a principled route to joules-per-compute scaling with precision, complementing the Archimedean fixed-width paradigm rather than replacing it.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.39.3-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 14 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] On the p-adic Beilinson conjecture for number fields. arXiv:0707.3682v2. https://arxiv.org/abs/0707.3682v2
[2] From Data to the p-Adic or Ultrametric Model. arXiv:0809.0492v1. https://arxiv.org/abs/0809.0492v1
[3] Application of $p$-adic analysis methods in describing Markov processes on ultrametric spaces isometrically embeddable into $\mathbb{Q}_{p}$. arXiv:1504.03629v1. https://arxiv.org/abs/1504.03629v1
[4] On generalized Iwasawa main conjectures and $p$-adic Stark conjectures for Artin motives. arXiv:2103.06864v4. https://arxiv.org/abs/2103.06864v4
[5] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[6] p-adic Equiangular Lines and p-adic van Lint-Seidel Relative Bound. arXiv:2408.00810v3. https://arxiv.org/abs/2408.00810v3
[7] The $p$-adic analytic subgroup theorem revisited. arXiv:1502.00768v1. https://arxiv.org/abs/1502.00768v1
[8] A p-Adic Model of DNA Sequence and Genetic Code. arXiv:q-bio/0607018v1. https://arxiv.org/abs/q-bio/0607018v1
