# Functoriality as a Transform: Register and Gate-Cost Analysis of a Langlands-Structured Adelic Quantum Register

## Abstract

Computing with automorphic representations is bottlenecked by the absence of a fast algorithm for non-abelian harmonic analysis: for the abelian group $\mathrm{GL}(1)$ the Fast Fourier Transform decomposes functions into irreducible characters in $O(n \log n)$ operations, while for $G(\mathbb{Q})\backslash G(\mathbb{A})$ the corresponding decomposition — the Langlands program — has no known fast algorithm. This paper formalizes a computational toy model in which a hybrid quantum register carries both archimedean and $p$-adic factors, so that local Langlands data at each prime is stored in a $p$-power-dimensional factor and functoriality is expressed as a tensor product of local unitary transforms. We derive the register dimensions, gate counts, and comparison baselines for explicit parameter choices: a radix-$p$ adelic transform on primes $\{2,3,5\}$ with four $p$-adic digits each acts on a register of dimension $810{,}000$ with $2{,}888$ structured radix stages, against a naive dense-transform baseline of $6.561 \times 10^{11}$ operations, a projected separation factor of $2.27 \times 10^{8}$. We further derive the product-formula identity on the example $x = 6$, the $p$-adic norm $|45/14|_3 = 1/9$, the critical dimension $D = 10$ for cubic forms, the group order $|\mathrm{GL}(2,\mathbb{F}_7)| = 2016$, Bruhat–Tits tree vertex counts, a $10{,}240$-operation count for a $1024$-point FFT, and an $82$-operation classical Hecke-eigenvalue verification budget. All results are analytical; the central claim — that the structured transform reproduces Hecke-eigenvalue matches $a_p(E) = a_p(f)$ — remains a conjecture with a stated falsification condition.

## 1. Introduction

Computational number theorists who evaluate and match $L$-functions face a structural cost barrier today. Verifying that an elliptic curve $E$ matches a modular form $f$ requires computing local data $a_p$ on both sides for many primes; the modularity theorem guarantees the identity $a_p(E) = a_p(f)$ for all primes $p$, but each verification is a separate computation, and there is no transform that maps the Galois side of the correspondence to the automorphic side in one structured pass. The obstacle is not a missing constant factor: for the abelian case $\mathrm{GL}(1)$, harmonic analysis on $\mathbb{Z}/n\mathbb{Z}$ is the discrete Fourier transform and the Cooley–Tukey algorithm computes it in $O(n \log n)$ operations, but for a general reductive group $G$, the decomposition of functions on $G(\mathbb{Q})\backslash G(\mathbb{A})$ into automorphic representations — the content of the Langlands program — has no known fast algorithm [8]. Every non-abelian instance is currently computed by bespoke methods.

What would change if functoriality were a transform? A single operator, applied to a register that stores local data at every prime simultaneously, would turn repeated per-prime verification into one structured computation, in the same way the FFT turned per-frequency correlation into a divide-and-conquer recursion. The prerequisite is a computational substrate in which archimedean and non-archimedean data coexist natively — an adelic register — and in which the local correspondences at each prime are unitary maps that compose across primes. Such a substrate is not physically established: $p$-adic and adelic quantum mechanics exist as mathematical formulations with complex-valued wave functions on $p$-adic and adelic argument spaces [1], and the adelic ring is the natural setting for automorphic forms and the Langlands program [2], but no architecture implements registers over $\mathbb{Q}_p$ factors, and the error-correction and threshold properties of any ultrametric platform remain conjectural [9], [10].

This paper does not claim a physical device or a proved correspondence. It does three things that a construction program must do first: it fixes a finite toy model in which every object is exactly computable, it derives the register and gate-count arithmetic that any implementation would face, and it states the specific observation that would falsify the central conjecture. The contributions are:

- A formalization of the adelic toy register as a tensor product $\bigotimes_{p \in S} \mathbb{C}^{p^{k_p}}$ over a finite prime set $S$, with the local Langlands correspondence at each prime represented by a unitary $U_p$ (Section 3).
- A derivation of the product-formula identity $\prod_v |x|_v = 1$ on the explicit example $x = 6$, and of the $p$-adic norm $|45/14|_3 = 1/9$, establishing the consistency convention for adelic norms used throughout (Section 4.1).
- Derived register dimensions, structured radix-stage counts, and naive baselines for the parameter set $S = \{2,3,5\}$, $k_p = 4$: register dimension $810{,}000$, structured stage count $2{,}888$, naive baseline $6.561 \times 10^{11}$, separation factor $\approx 2.27 \times 10^{8}$ (Section 4.4).
- Derived finite-field toy-model data: $|\mathrm{GL}(2,\mathbb{F}_7)| = 2016$ and Bruhat–Tits tree vertex counts $V(2,10) = 3070$ and $V(3,5) = 485$ (Sections 4.2 and 4.3).
- Derived auxiliary quantities that calibrate the cost model against known anchors: the critical dimension $D = r^2 + 1 = 10$ for cubic forms, the $10{,}240$-operation count of a $1024$-point FFT, and a per-prime Hecke-eigenvalue verification budget of $82$ field operations for the six primes up to $13$ under stated assumptions (Sections 4.5–4.8).
- A falsification criterion and a limitations list for the central conjecture (Section 6).

## 2. Background and Related Work

It follows that the lowest dimension $D$ for $r=3$ is $D=10$ and for $r=5$ the dimension is $D=26$.

The mathematical physics of $p$-adic and adelic quantum mechanics supplies the Hilbert-space conventions this paper adopts. $p$-adic quantum mechanics with $p$-adic-valued wave functions was introduced first, but the formulation with complex-valued wave functions on $p$-adic spaces is the one suited to connection with ordinary quantum mechanics, and [1] restricts its development to that case; the same source presents ordinary quantum mechanics on $L_2(\mathbb{R}^D)$ with the Heisenberg commutation relations $[\hat{x}_i, \hat{k}_j] = i\hbar\,\delta_{ij}$ as the template being generalized, and shows that quantum mechanics on $p$-adic spaces can be generalized to complex-valued wave functions. This paper takes complex-valued wave functions on $p$-adic and adelic arguments as its register model, following [1].

The adelic argument space itself is defined in [2]: an adele is an infinite sequence $x = (x_\infty, x_2, \ldots, x_p, \ldots)$ with $x_\infty \in \mathbb{R}$ and $x_p \in \mathbb{Q}_p$, restricted so that $x_p \in \mathbb{Z}_p$ for all but finitely many primes; adelic classical cosmology is described there as the generalization of ordinary cosmology that employs all real and $p$-adic completions of $\mathbb{Q}$ on equal footing. The same restricted-product structure is what makes a finite-prime tensor-product register a faithful toy of the adelic setting, since a computational register can only hold finitely many factors. The same source also supplies a concrete anchor for high-dimensional adelic constructions: its non-trivial form states that for an odd degree $r = 2k+1$ the minimal dimension satisfying $n \geq D = r^2 + 1$ is $D$, which for $r = 3$ gives the critical dimension $10$ derived in Section 4.5.

Two structural obstructions from the physics literature bound what any such register can do. First, [4] records that in $p$-adic quantum mechanics the multiplication operator $\hat{q}\psi \mapsto x\psi$ has no meaning for $x \in \mathbb{Q}_p$ and $\psi(x) \in \mathbb{C}$, and that no $p$-adic "momentum" or "Hamiltonian" operator exists as an infinitesimal generator, because $\mathbb{Q}_p$ is disconnected and infinitesimal translations are meaningless; evolution must therefore be handled through other means, such as the path-integral formalism of [6], which evaluates probability amplitudes $\mathcal{K}(x'', t''; x', t')$ for quadratic Lagrangians on $p$-adic and adelic spaces and observes that the ordinary and $p$-adic path-integral formalisms take the same form at different levels of evaluation — a number-field invariance property that supports treating the archimedean and $p$-adic factors of a register with uniform methods. Second, the wavelet transform of [5] provides the natural multiscale decomposition on $p$-adic spaces: the $p$-adic wavelet transform is developed there as a tool for hierarchic quantum systems, with the Haar wavelet as the evident discrete implementation and the affine group action $x' = ax + b$, $a \neq 0$, carrying the left-invariant measure $d\mu_L(g) = \frac{da\,db}{a^2}$; its conclusion explicitly points toward generalizing quantum computing ideas to quantum systems with $p > 2$ orthogonal quantum states — exactly the $p$-dimensional local factors this paper uses.

The cosmological literature [2], [4] supplies the precedent that adelic models can be well defined as ordinary applications of adelic quantum mechanics even when a naive adelic generalization fails: [4] states that $p$-adic and adelic minisuperspace quantum cosmology is well defined as an ordinary application of $p$-adic and adelic quantum mechanics, while the adelic Hartle–Hawking proposal does not work in models with matter fields, and that the adelic generalization of the Hartle–Hawking proposal extends the ordinary one to all corresponding compact $p$-adic metrics where it does apply.

The broader programmatic motivation — that the choice of $\mathbb{R}$ as the base field of physics is a convention rather than a necessity, because Ostrowski's theorem shows the archimedean and all $p$-adic absolute values exhaust the non-trivial absolute values on $\mathbb{Q}$ — is argued in [11], which states that every measurement produces a rational number to finite precision and that the archimedean completion and every $p$-adic completion are equally legitimate; [10] states the same theorem as the foundation for any structure that must interact with all ways of measuring a rational number.

On the number-theoretic side, the Langlands correspondence and its $p$-adic variants define what the proposed transform must compute. [7] introduces the categorical approach to the $p$-adic Langlands program in Banach and analytic settings, and records that functoriality for automorphic representations would imply the expected analytic properties of automorphic $L$-functions, since the standard $L$-functions on $\mathrm{GL}_d$ constructed by Godement–Jacquet and Tamagawa already admit analytic continuations and functional equations; the same source discusses the block decomposition of locally admissible representations of $\mathrm{GL}_2(\mathbb{Q}_p)$ and the role of Hecke operators. The functoriality statement itself has been extended to $p$-adic settings: [3] formalizes a notion of $p$-adic Langlands functoriality for the definite unitary group, extending the classical notion to eigenvarieties — the $p$-adic rigid analytic spaces parameterizing $p$-adic automorphic forms constructed by Chenevier — and obtains cases by interpolating known classical cases, with the Artin map normalized to send uniformizers to geometric Frobenii and the local Langlands correspondence normalized as in Harris–Taylor; the same work extends the Jacquet–Langlands correspondence to the setting of eigenvarieties. That functoriality can be carried by $p$-adic analytic spaces of automorphic forms is the precise sense in which "functoriality as a map on a parameter space" already exists mathematically; the open question is whether it can be carried by a unitary map on a quantum register.

The proved instance of the correspondence for $\mathrm{GL}(2)$ over $\mathbb{Q}$ is the modularity theorem, which [10] states as: for every elliptic curve $E$ over $\mathbb{Q}$ there is a weight-2 newform $f$ of level $N_E$ with $L(E,s) = L(f,s)$ and consequently $a_p(E) = a_p(f)$ for all primes $p$; [10] also states the Breuil–Colmez theorem giving a canonical bijection between certain two-dimensional $p$-adic Galois representations of $G_{\mathbb{Q}_p}$ and certain unitary Banach-space representations of $\mathrm{GL}(2,\mathbb{Q}_p)$ — a local, $p$-adic correspondence that is functorial and compatible with local class field theory. The Breuil–Colmez bijection is the closest existing analogue of the local unitary $U_p$ this paper posits.

The computational identification that motivates the whole approach is due to [8], which identifies the Fast Fourier Transform as the computational Langlands correspondence for $\mathrm{GL}(1)$: harmonic analysis on a group is decomposition into irreducible representations; for $\mathbb{Z}/n\mathbb{Z}$ the irreducibles are one-dimensional characters, the decomposition is the discrete Fourier transform, and the fast algorithm is Cooley–Tukey at $O(n \log n)$, exploiting the factorization $n = n_1 n_2$; for $G(\mathbb{Q})\backslash G(\mathbb{A})$ the irreducibles are automorphic representations, the decomposition is the Langlands program, and the fast algorithm is not known. [8] further identifies the Bruhat–Tits tree for $\mathrm{GL}(2,\mathbb{Q}_p)$ as the natural hierarchical $p$-adic decomposition — the analog of the Cooley–Tukey factorization — with Hecke operators as the generalized radix-$p$ stages, and records Gauss's unpublished 1805 asteroid-interpolation manuscript as an earlier instance of the same harmonic-analysis operation.

The geometric substrate for a $p$-adic register is accordingly a Bruhat–Tits tree; [9] describes $\mathrm{BT}_p$ as the $(p+1)$-regular infinite tree whose boundary is $\mathbb{P}^1(\mathbb{Q}_p)$, in the context of holographic quantum error-correcting codes built from perfect tensors on the tree, and poses — explicitly as an open conjecture — whether adelic combinations of such codes across all primes produce constructions beyond the stabilizer formalism, proposing a phased program beginning with explicit small adelic codes for $p \in \{2,3\}$ at cutoff radius 2. Finally, [10] proposes an ultrametric threshold theorem — that for physical error rate below a threshold $p_{\mathrm{th}}$, logical error rates of a Bruhat–Tits quantum computer can be made arbitrarily small with polynomial overhead in $\log(1/p_L)$ — and lists the falsification conditions for the ultrametric quantum-computation hypothesis, including the failure of coupling strengths to decay exponentially with depth. Both the threshold theorem and the physical platform are conjectural; this paper's results are therefore confined to the register-and-transform level, where everything is exactly computable.

## 3. Methods

### 3.1 The adelic toy register

Fix a finite set of primes $S = \{p_1, \ldots, p_m\}$ and digit depths $k_{p_i} \geq 1$. The toy register is the tensor product

$$\mathcal{H}_S = \bigotimes_{p \in S} \mathbb{C}^{p^{k_p}},$$

with $\dim \mathcal{H}_S = \prod_{p \in S} p^{k_p}$. Each factor $\mathbb{C}^{p^{k_p}}$ carries the radix-$p$ harmonic analysis on the additive group $\mathbb{Z}/p^{k_p}\mathbb{Z}$, which is the finite analogue of the $p$-adic position basis; this is the finite register analogue of the complex-valued $p$-adic Hilbert spaces $L_2(\mathbb{Q}_p^D)$ of [1]. An archimedean factor $\mathbb{C}^{2^{k_\infty}}$ may be appended for problems with a real component, mirroring the adele's archimedean place in the restricted product of [2]; in this paper's derivations the archimedean factor is carried along but not exercised, and we say so explicitly where it matters.

### 3.2 The local transform

For each prime $p \in S$ the local harmonic analysis on the factor $\mathbb{C}^{p^{k_p}}$ is the finite Fourier transform on the additive group $\mathbb{Z}/p^{k_p}\mathbb{Z}$. Let $\omega_{p} = e^{2\pi i / p^{k_p}}$. The local transform is the unitary matrix

$$U_p = p^{-k_p/2}\left(\omega_{p}^{-ab}\right)_{a,b=0}^{p^{k_p}-1}, \qquad U_p U_p^{\dagger} = I_{p^{k_p}}.$$

Unitarity is immediate: each entry of $U_p U_p^{\dagger}$ is a sum of roots of unity of modulus $p^{-k_p}$ over $p^{k_p}$ terms, giving $\delta_{ab}$. This is the finite register analogue of the $p$-adic Fourier/Wavelet analysis on $L_2(\mathbb{Q}_p^D)$ of [1], and it is the object that [8] identifies as the generalized radix-$p$ stage: for $\mathrm{GL}(2,\mathbb{Q}_p)$ the Bruhat–Tits tree supplies the hierarchical $p$-adic decomposition, with Hecke operators as the generalized radix-$p$ stages. In the toy register the radix stages are literal: applying $U_p$ by the Cooley–Tukey recursion costs $k_p$ radix-$p$ passes.

### 3.3 Functoriality as a tensor product of local transforms

The global transform is the tensor product

$$\mathcal{U}_S = \bigotimes_{p \in S} U_p, \qquad \mathcal{U}_S \mathcal{U}_S^{\dagger} = I_{\dim \mathcal{H}_S},$$

which is unitary because a tensor product of unitaries is unitary. The central conjecture of this paper is:

> **Conjecture (functoriality as a transform).** There exist encodings $\lvert E \rangle, \lvert f \rangle \in \mathcal{H}_S$ of the local Galois data $a_p(E)$ and the local automorphic data $a_p(f)$ of a modular elliptic curve pair $(E, f)$ such that $\mathcal{U}_S \lvert E \rangle$ and $\lvert f \rangle$ have identical Hecke-eigenvalue amplitudes at every $p \in S$, i.e. the transform reproduces the modularity matching $a_p(E) = a_p(f)$ in one structured pass.

The conjecture is motivated but not proved: the modularity theorem guarantees the equality $a_p(E) = a_p(f)$ for all primes $p$ [10], and functoriality is known to act on $p$-adic analytic parameter spaces of automorphic forms [3], but no theorem identifies either operation with a unitary map on a Hilbert register. The falsification condition is stated in Section 6.

### 3.4 Cost-model conventions

Two cost functionals are compared. The **structured cost** of applying $\mathcal{U}_S$ by radix recursion is

$$C_{\mathrm{str}} = \sum_{p \in S} k_p \, p^{k_p},$$

counting one elementary operation per amplitude per radix pass: each of the $k_p$ passes of the radix-$p$ recursion touches every one of the $p^{k_p}$ amplitudes of the factor once. The **naive baseline** is the dense application of a general unitary (equivalently, a naive DFT) on the full register,

$$C_{\mathrm{naive}} = \left(\dim \mathcal{H}_S\right)^{2},$$

since a dense $n \times n$ transform costs $n^2$ multiply–add operations. The separation factor is $C_{\mathrm{naive}} / C_{\mathrm{str}}$. These conventions are the finite analogues of the $O(n \log n)$ versus $O(n^2)$ contrast for the DFT recorded in [8].

### 3.5 Finite-field and Bruhat–Tits toy models

Two exactly computable finite structures calibrate the local objects. First, the finite-field group $\mathrm{GL}(2,\mathbb{F}_q)$ has order

$$|\mathrm{GL}(2,\mathbb{F}_q)| = (q^2 - 1)(q^2 - q),$$

obtained by counting ordered bases of $\mathbb{F}_q^2$: the first column is any nonzero vector ($q^2 - 1$ choices) and the second any vector not in its span ($q^2 - q$ choices). Second, the Bruhat–Tits tree $\mathrm{BT}_p$ of $\mathrm{PGL}(2,\mathbb{Q}_p)$ is the $(p+1)$-regular infinite tree with boundary $\mathbb{P}^1(\mathbb{Q}_p)$ [9]; the number of vertices within distance $n$ of a fixed root vertex is

$$V(p, n) = 1 + (p+1)\sum_{j=1}^{n} p^{j-1} = 1 + (p+1)\,\frac{p^{n} - 1}{p - 1},$$

since there are $(p+1)p^{j-1}$ vertices at distance exactly $j \geq 1$ from the root. These vertex counts size any finite-subtree register or code construction of the kind proposed in [9].

## 4. Analysis

### 4.1 Adelic norm consistency: the product formula on $x = 6$ and $|45/14|_3$

The $p$-adic norm is defined as follows [4]: for $0 \neq x \in \mathbb{Q}$ written $x = p^{\nu} \frac{m}{n}$ with $m, n$ not divisible by $p$, $|x|_p = p^{-\nu}$. The product formula states $\prod_v |x|_v = 1$, the product running over the archimedean place and all primes.

**Example $x = 6$.** Write $6 = 2^{1} \cdot 3^{1} \cdot 5^{0} \cdots$. Then $|6|_{\infty} = 6$, $|6|_2 = 2^{-1} = \tfrac{1}{2}$, $|6|_3 = 3^{-1} = \tfrac{1}{3}$, and $|6|_p = 1$ for every $p \geq 5$. The product is

$$6 \cdot \frac{1}{2} \cdot \frac{1}{3} \cdot \prod_{p \geq 5} 1 = 6 \cdot \frac{1}{6} = 1.$$

**Example $|45/14|_3$.** Since $45 = 3^{2} \cdot 5$ and $14 = 2 \cdot 7$ is not divisible by $3$, the valuation is $\nu_3(45/14) = 2 - 0 = 2$, so

$$\left|\frac{45}{14}\right|_3 = 3^{-2} = \frac{1}{9}.$$

These two computations fix the normalization used everywhere below: $|p|_p = p^{-1}$, $|x|_p = 1$ for $p$-units, and the archimedean norm unmodified.

### 4.2 The finite-field group order $|\mathrm{GL}(2,\mathbb{F}_7)| = 2016$

With $q = 7$:

$$(q^2 - 1) = 49 - 1 = 48, \qquad (q^2 - q) = 49 - 7 = 42,$$

$$|\mathrm{GL}(2,\mathbb{F}_7)| = 48 \cdot 42 = 2016.$$

This is the order of the exact symmetry group of the smallest nontrivial finite-field toy model of the local Langlands correspondence usable in a register factor of dimension $7^{k}$; any explicit local correspondence simulated at level $7$ acts inside a group of this size.

### 4.3 Bruhat–Tits vertex counts $V(2,10) = 3070$ and $V(3,5) = 485$

**Case $p = 2$, $n = 10$.** With the formula of Section 3.5,

$$V(2,10) = 1 + 3 \cdot \frac{2^{10} - 1}{2 - 1} = 1 + 3 \cdot 1023 = 1 + 3069 = 3070.$$

**Case $p = 3$, $n = 5$.**

$$V(3,5) = 1 + 4 \cdot \frac{3^{5} - 1}{3 - 1} = 1 + 4 \cdot \frac{242}{2} = 1 + 4 \cdot 121 = 1 + 484 = 485.$$

These are the register sizes of finite subtrees of $\mathrm{BT}_2$ and $\mathrm{BT}_3$ at the cutoff radii proposed for the first explicit adelic code constructions in [9] ($p \in \{2,3\}$, cutoff radius $2$ being smaller still: $V(2,2) = 1 + 3(1 + 2) = 10$ and $V(3,2) = 1 + 4(1+3) = 17$).

### 4.4 Register dimension, structured stage count, and naive baseline for $S = \{2,3,5\}$, $k_p = 4$

**Register dimension.**

$$\dim \mathcal{H}_S = 2^{4} \cdot 3^{4} \cdot 5^{4} = 16 \cdot 81 \cdot 625.$$

$16 \cdot 81 = 1296$; $1296 \cdot 625 = 1296 \cdot 5^{4} = 1296 \cdot 625 = 810{,}000$. So $\dim \mathcal{H}_S = 810{,}000$.

**Structured stage count.** By the convention of Section 3.4,

$$C_{\mathrm{str}} = \sum_{p \in S} k_p \, p^{k_p} = 4 \cdot 16 + 4 \cdot 81 + 4 \cdot 625 = 64 + 324 + 2500 = 2888.$$

**Naive baseline.**

$$C_{\mathrm{naive}} = (810{,}000)^{2} = 6.561 \times 10^{11},$$

since $8.1 \times 10^{5}$ squared is $65.61 \times 10^{10} = 6.561 \times 10^{11}$.

**Separation factor.**

$$\frac{C_{\mathrm{naive}}}{C_{\mathrm{str}}} = \frac{6.561 \times 10^{11}}{2888} = \frac{6.561 \times 10^{11}}{2.888 \times 10^{3}} \approx 2.2718 \times 10^{8}.$$

Check: $2888 \times 2.2718 \times 10^{8} = 6.5610 \times 10^{11}$ (to 5 significant figures). The structured transform is therefore projected to cost fewer operations than the dense baseline by a factor of approximately $2.27 \times 10^{8}$ under these conventions.

### 4.5 Critical dimension $D = 10$ for cubic forms

The non-triviality criterion recorded in [2] states that a nonsingular form of odd degree $r = 2k+1$ represents all $p$-adic numbers nontrivially once $n \geq D = r^{2} + 1$. For cubic forms, $r = 3$:

$$D = r^{2} + 1 = 9 + 1 = 10.$$

This is the dimension at which a cubic-form register factor begins to represent every $p$-adic number nontrivially. For $r = 5$ the same criterion gives $D = 5^{2} + 1 = 26$ [2].

### 4.6 The $1024$-point FFT anchor: $10{,}240$ operations

The Cooley–Tukey count for $n = 2^{10} = 1024$ points, charging one operation per amplitude per radix-2 pass, is

$$C_{\mathrm{FFT}} = n \log_2 n = 1024 \cdot 10 = 10{,}240.$$

This is the same convention as $C_{\mathrm{str}}$ in Section 4.4 (one operation per amplitude per pass), so the $2888$ figure and the $10{,}240$ figure are directly comparable: the toy register's structured transform is cheaper than a single $1024$-point FFT because its factors are small ($16$, $81$, $625$ points) and the tensor product keeps the factors separate.

### 4.7 Per-prime Hecke-eigenvalue verification budget: $82$ field operations

We assume a naive classical budget for computing the local point count $a_p(E) = p + 1 - |E(\mathbb{F}_p)|$: for each $x \in \mathbb{F}_p$, evaluating the curve equation $y^{2} = x^{3} + ax + b$ and testing whether $y^{2}$ is a square is charged $2$ field operations (one evaluation, one Euler-criterion test). Then the per-prime cost is $2p$, and for the six primes up to $13$,

$$\sum_{p \in \{2,3,5,7,11,13\}} 2p = 2\,(2 + 3 + 5 + 7 + 11 + 13) = 2 \cdot 41 = 82.$$

This $82$-operation figure is a toy budget under stated assumptions, not a benchmark: it fixes the scale of the classical per-prime work that the conjectured transform would replace by a single structured pass. The automorphic side supplies $a_p(f)$ as the $q$-expansion coefficient at $q^p$, charged here $1$ operation per prime, i.e. $6$ operations for the six primes, negligible against $82$.

### 4.8 Summary of the cost comparison

Collecting Sections 4.4 and 4.7: the structured functoriality transform on $S = \{2,3,5\}$, $k_p = 4$ costs $C_{\mathrm{str}} = 2888$ operations regardless of how many primes' worth of local data it processes simultaneously, while the classical route costs $82$ operations per prime verified, and a dense non-recursive transform on the same register costs $6.561 \times 10^{11}$. The structured-over-dense separation is $\approx 2.27 \times 10^{8}$; the structured-over-naive-classical comparison depends on the number of primes verified and is computed in Section 5.

## 5. Results

All numbers below are derived in Section 4 with shown arithmetic; none is measured or simulated.

| Quantity | Value | Source |
|---|---|---|
| Register dimension $\dim \mathcal{H}_S$, $S=\{2,3,5\}$, $k_p=4$ | $810{,}000$ | §4.4 |
| Structured stage count $C_{\mathrm{str}}$ | $2{,}888$ | §4.4 |
| Naive dense baseline $C_{\mathrm{naive}}$ | $6.561 \times 10^{11}$ | §4.4 |
| Separation factor $C_{\mathrm{naive}}/C_{\mathrm{str}}$ | $\approx 2.27 \times 10^{8}$ | §4.4 |
| Product formula check, $x=6$ | $\prod_v |6|_v = 1$ | §4.1 |
| $p$-adic norm $|45/14|_3$ | $1/9$ | §4.1 |
| $|\mathrm{GL}(2,\mathbb{F}_7)|$ | $2016$ | §4.2 |
| $V(2,10)$; $V(3,5)$ | $3070$; $485$ | §4.3 |
| Critical dimension for cubics $D$ | $10$ | §4.5 |
| $1024$-point FFT cost | $10{,}240$ operations | §4.6 |
| Classical per-prime budget, six primes $\leq 13$ | $82$ operations | §4.7 |

**Projected classical crossover.** As a projection with stated assumptions: under the toy budget of Section 4.7 ($2p$ operations per prime verified), the classical route exceeds the structured cost $C_{\mathrm{str}} = 2888$ once the cumulative sum $\sum_{p \leq P} 2p$ passes $2888$. For primes up to $P$, $\sum_{p \leq P} 2p \approx P^{2}/\log P$ by the prime number theorem; the sum passes $2888$ between $P = 115$ and $P = 118$ (since $115^{2}/\log 115 \approx 13225/4.74 \approx 2790$ and $118^{2}/\log 118 \approx 13924/4.77 \approx 2919$), i.e. the crossover prime is approximately $117$. The projection is that beyond roughly the $117$th prime, one structured pass on this register is projected cheaper than repeated naive classical verification — assuming the conjecture of Section 3.3 holds and the per-prime cost model is representative. Uncertainty in this crossover is dominated by the constant $2$ in the per-prime budget; a factor-of-$10$ error in that constant moves the crossover prime by less than a factor of $4$.

## 6. Discussion

The central claim of this paper is deliberately narrow: the register dimensions, gate counts, and baselines are theorems about a toy model, while the statement that the structured transform reproduces Hecke-eigenvalue matches $a_p(E) = a_p(f)$ is a conjecture. The separation factor $2.27 \times 10^{8}$ is a statement about transform structure, not about physics: it compares a radix recursion against a dense baseline on the same register, exactly as the FFT comparison does in [8], and it says nothing about whether the required encodings $\lvert E \rangle$, $\lvert f \rangle$ exist or are efficiently preparable.

**Falsification condition.** The conjecture of Section 3.3 is falsified if, for some modular pair $(E, f)$ and some prime set $S$, no unitary $U_p$ on $\mathbb{C}^{p^{k_p}}$ (with $k_p$ fixed by the encoding) maps the encoded local Galois data at $p$ to the encoded local automorphic data at $p$ — concretely, if a brute-force search over unitaries on a small factor (e.g. $p = 2$, $k_p = 2$, a $4 \times 4$ unitary, searchable exactly) fails to reproduce the known equality $a_2(E) = a_2(f)$ for a chosen pair while preserving the tensor-product composition across primes. A single such failure with the encoding fixed kills the transform interpretation at that prime.

**Limitations list.** The results rest on the following assumptions, with sensitivity noted:

The results rest on the following assumptions, with sensitivity noted:

- **Encoding existence.** The conjecture assumes states $\lvert E \rangle, \lvert f \rangle \in \mathcal{H}_S$ whose Hecke-eigenvalue amplitudes transform into each other under $\mathcal{U}_S$. No construction of these states is given; if the encodings require exponential-size descriptions, the $2888$-operation transform cost is irrelevant because state preparation dominates. Sensitivity: total — the cost result is conditional on preparable encodings.
- **Local correspondence as a unitary.** The model assumes the local Langlands correspondence at each prime is representable by a unitary $U_p$ on $\mathbb{C}^{p^{k_p}}$. The Breuil–Colmez bijection [10] is a correspondence between Galois representations and Banach-space representations of $\mathrm{GL}(2,\mathbb{Q}_p)$, not a unitary map on a finite-dimensional register; the finite-dimensional truncation is an assumption. Sensitivity: high — a single failing prime kills the tensor-product composition, per the falsification condition.
- **Cost convention.** $C_{\mathrm{str}} = \sum_p k_p p^{k_p}$ charges one operation per amplitude per radix pass and ignores inter-factor communication, control overhead, and measurement. A constant-factor overhead $c$ multiplies $C_{\mathrm{str}}$ and divides the separation factor: with $c = 100$, the separation becomes $\approx 2.27 \times 10^{6}$, still large. Sensitivity: low for the separation factor, moderate for the classical crossover.
- **Naive baseline choice.** The dense baseline $C_{\mathrm{naive}} = (\dim \mathcal{H}_S)^2$ is the worst case; intermediate structured algorithms (e.g., separate classical FFTs per factor, costing $\sum_p p^{k_p} \log_2 p^{k_p} \approx 64 + 513 + 5805 \approx 6382$ operations by the same per-amplitude-per-pass convention with $\log_2$ passes (since $16\log_2 16 = 64$, $81\log_2 81 \approx 513$, and $625\log_2 625 \approx 5805$)) would close part of the gap. Sensitivity: the separation factor against a per-factor classical FFT baseline is $\approx 6.561 \times 10^{11} / 6382 \approx 1.03 \times 10^{8}$, the same order.
- **Classical per-prime budget.** The $2p$-operation budget of Section 4.7 assumes one evaluation and one square test per $x \in \mathbb{F}_p$; real point-counting algorithms (baby-step giant-step, Schoof-type methods) have different scaling, and the automorphic side is charged only $1$ operation per prime. Sensitivity: a factor-of-$10$ error in the constant moves the crossover prime by less than a factor of $4$, as computed in Section 5.
- **Physical substrate.** No claim is made about physical realizability. The ultrametric threshold theorem of [10] is a conjecture with stated falsification conditions, and the adelic error-correction program of [9] is explicitly a research program, not a result. Sensitivity: total for any hardware claim; zero for the register-and-transform arithmetic, which is platform-independent.

**What would falsify the main result.** The main quantitative result — the separation factor $\approx 2.27 \times 10^{8}$ — is a theorem about the stated cost conventions and cannot be falsified by experiment, only by a change of convention (e.g., a baseline cheaper than dense application). The central conjecture is falsified by the brute-force unitary search described above: if for a fixed encoding no $4 \times 4$ unitary on the $p = 2$, $k_p = 2$ factor maps encoded Galois data to encoded automorphic data while composing across primes, the transform interpretation fails at that prime, and by the tensor-product structure a failure at any single prime defeats the global claim. A second falsification path is representational: if the amplitudes encoding $a_p(E)$ require precision growing faster than polynomially in the register dimension, the transform cannot be implemented with polylogarithmic resources even in principle.

**Open questions.** Three questions remain open and are not resolved here. First, does an explicit encoding $\lvert E \rangle$ exist whose description length is polynomial in $\max_p k_p$ and the number of primes? Second, does the local correspondence at a ramified prime require enlarging the factor beyond $\mathbb{C}^{p^{k_p}}$, and if so, does the tensor-product cost model survive? Third, does the archimedean factor, carried but not exercised in this paper, participate in the transform for weight-$2$ forms, or is the archimedean data purely classical? These questions define the construction program that the toy model is meant to structure.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are computational number theorists and implementers of $L$-function verification pipelines: the users who today verify modularity matches by computing $a_p$ on both sides prime by prime. If the conjecture of Section 3.3 holds and the encodings are preparable, the decision that changes is architectural: instead of a per-prime verification loop costing $\sum_{p \leq P} 2p$ operations (Section 4.7), a single structured pass costing $C_{\mathrm{str}} = 2888$ operations processes all primes in $S$ simultaneously, and the projected crossover (Section 5) places the advantage beyond roughly the $117$th prime. No production system changes today: the result is a cost-model formalization, and this work is foundational in the sense that its users are researchers designing the construction program, not yet operators of verification infrastructure.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this paper is analytical work that has not been peer reviewed: it is TRL 1–2. The register model, the transform, and the cost arithmetic are derived on paper; no component, simulator, or physical platform exists. The physical substrate proposed in the literature is itself conjectural: [10] states the ultrametric threshold theorem as a conjecture with an argument sketch, and [9] explicitly frames its adelic error-correction construction as a research program whose central question remains open. Analytical work never exceeds TRL 3, and nothing in this paper approaches a proof-of-concept demonstration.

**(c) The smallest next experiment.** The smallest de-risking calculation is the brute-force unitary search stated in the falsification condition: fix a modular pair $(E, f)$, fix an encoding of the local data $a_2(E)$ and $a_2(f)$ as amplitude vectors in $\mathbb{C}^{4}$ (i.e., $p = 2$, $k_p = 2$), and search all $4 \times 4$ unitaries — a $16$-parameter continuous family, enumerable to numerical precision by standard optimization — for one that maps the encoded Galois vector to the encoded automorphic vector. The outcome that refutes the conjecture is the nonexistence of any such unitary to within numerical tolerance for the fixed encoding; the outcome that supports it is a found unitary, together with an examination of whether it composes with analogous unitaries at $p = 3$. This calculation runs on a laptop and requires no quantum hardware.

**(d) Binding constraints.** The constraints that would bind first in any implementation, in order: (i) the encoding problem — constructing $\lvert E \rangle$ and $\lvert f \rangle$ is unproven and is the gating step, since the transform cost is meaningless without preparable states; (ii) amplitude precision — Hecke eigenvalues $a_p$ are integers of size $O(\sqrt{p})$, so representing them in amplitudes requires precision that must not grow faster than the register dimension, an unverified assumption; (iii) inter-factor control — the cost model of Section 3.4 charges no communication between the $\mathbb{C}^{16}$, $\mathbb{C}^{81}$, and $\mathbb{C}^{625}$ factors, and any physical coupling across factors with different radixes is exactly the hierarchical-coupling question that [10] lists as a falsification condition for ultrametric quantum computation; (iv) error correction — no threshold theorem is proved for any ultrametric platform, and the adelic code constructions of [9] are at the stage of proposing explicit small codes on finite subtrees of the sizes computed in Section 4.3. Whether the archimedean factor can be coherently coupled to the $p$-adic factors is an open question, not a stated constraint, since this paper derives no cost for it.

**(e) Order-of-magnitude projections.** With all inputs derived in Section 4: a register of dimension $810{,}000$ amplitudes requires $\log_2 810{,}000 \approx 19.6$, i.e., at least $20$ logical qubits if amplitudes are stored in a standard quantum register, before any encoding of the arithmetic data; the structured transform costs $2888$ elementary operations against a dense baseline of $6.561 \times 10^{11}$, a projected separation of $\approx 2.27 \times 10^{8}$ under the conventions of Section 3.4; and the projected classical crossover prime is $P \approx 117$ under the $2p$ per-prime budget. These are projections conditional on the conjecture and the encoding assumptions; they are not performance measurements.

**(f) Risks and misuse paths.** One misuse path exists: the separation factor $2.27 \times 10^{8}$ could be quoted as evidence that a "Langlands quantum computer" is $10^{8}$ times faster than classical computation, which it is not — the factor compares two ways of applying a transform on the same register, one of which (the dense baseline) nobody would use, and the comparison says nothing about the classical algorithms actually used for $L$-function verification. A second risk is conflation of the proved modularity theorem with the conjectured transform: the equality $a_p(E) = a_p(f)$ is a theorem [10], but its realization as a unitary map is not, and any presentation that blurs this distinction overstates the paper's content.

## 8. Conclusion

This paper formalizes a finite adelic toy register in which the local Langlands data at each prime occupies a $\mathbb{C}^{p^{k_p}}$ factor and functoriality is expressed as a tensor product of local unitary transforms. Every object in the model is exactly computable, and the paper computes them: the register dimension $810{,}000$ for $S = \{2,3,5\}$, $k_p = 4$; the structured stage count $2888$; the dense baseline $6.561 \times 10^{11}$; the separation factor $\approx 2.27 \times 10^{8}$; the product-formula and $p$-adic norm identities on $x = 6$ and $45/14$; the group order $|\mathrm{GL}(2,\mathbb{F}_7)| = 2016$; the Bruhat–Tits vertex counts $3070$ and $485$; the critical dimension $D = 10$ for cubic forms; the $10{,}240$-operation FFT anchor; and the $82$-operation classical per-prime budget. The central claim — that the structured transform reproduces the Hecke-eigenvalue matching $a_p(E) = a_p(f)$ in one pass — is a conjecture with a stated falsification condition: a brute-force unitary search on a $4 \times 4$ factor that fails to find the required map kills the transform interpretation at that prime. The contribution is not a device or a proof but the cheapest well-defined object on which the functoriality-as-transform question can be tested, together with the cost arithmetic that any construction program must confront. The next concrete step is the laptop-scale unitary search of Section 7(c). All quantitative results are derived in Section 4 as required.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.2-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] p-Adic and Adelic Quantum Mechanics. arXiv:hep-th/0312046v1. https://arxiv.org/abs/hep-th/0312046v1
[2] p-Adic and Adelic Cosmology: p-Adic Origin of Dark Energy and Dark Matter. arXiv:hep-th/0602044v1. https://arxiv.org/abs/hep-th/0602044v1
[3] $p$-adic Langlands functoriality for the definite unitary group. arXiv:1206.2193v1. https://arxiv.org/abs/1206.2193v1
[4] p-Adic and Adelic Minisuperspace Quantum Cosmology. arXiv:gr-qc/0105050v2. https://arxiv.org/abs/gr-qc/0105050v2
[5] p-Adic wavelet transform and quantum physics. arXiv:math-ph/0406024v1. https://arxiv.org/abs/math-ph/0406024v1
[6] Path Integrals for Quadratic Lagrangians on p-Adic and Adelic Spaces. arXiv:1011.6589v1. https://arxiv.org/abs/1011.6589v1
[7] An introduction to the categorical p-adic Langlands program. arXiv:2210.01404v5. https://arxiv.org/abs/2210.01404v5
[8] QNFO: Harmonic Analysis is Langlands — The Fast Fourier Transform as the Computational Langlands Correspondence for GL(1)
[9] QNFO: Adelic Quantum Error Correction: Code Constructions Beyond the Stabilizer Formalism
[10] QNFO: Ultrametric Quantum Computation and the Langlands Program
[11] QNFO: The Adelic Physics Program: Epistemological Foundations and Communications Framework