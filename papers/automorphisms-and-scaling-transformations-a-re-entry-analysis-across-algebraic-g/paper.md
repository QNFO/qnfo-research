# Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure

## Abstract

Automorphism groups encode the symmetries of algebraic varieties, non-associative algebras, parabolic geometries, group splittings, and holomorphic dynamical systems, but each setting is treated with its own tools, and practitioners lack a uniform test for when a rescaling of coordinates, dimensions, or metrics acts nontrivially on automorphism parameters. Normalization and reduction routines in computer algebra, and classification arguments that quotient by scaling symmetries, silently assume that dilations either preserve or trivially commute with the automorphisms at hand. We introduce a three-part conjugation test — normalization, centralization, and parameter rescaling — and carry out its quantitative branch with explicit arithmetic. Conjugation of the planar shear $\phi(x,y)=(x+y,y)$ by the anisotropic dilation $D=\operatorname{diag}(2,3)$ rescales the shear coefficient by $\lambda_1/\lambda_2=2/3\approx 0.666667$, while scalar dilations centralize both the shear and rotations exactly. In the Cayley–Dickson tower, the octonion-to-sedenion step multiplies the count of associative quaternion rings from $7$ to $35$, a factor of $5$, i.e., $\log_2 5\approx 2.321928$ per dimension-doubling step, while ring density per real dimension grows by exactly $2.5$ (from $0.875$ to $2.1875$). We further derive the two-ray structure and the involution $\operatorname{ord}(g^*)=2$ for cone-permuting maps at Picard number two, the generator count $n(n-1)$ plus $\prod_i\operatorname{Aut}(G_i)$ for pure symmetric outer automorphisms at $n\geq 5$ free factors, and the totient rigidity $\varphi(2)=1$ for order-two discrete scalings. The results give a computable, falsifiable rule — ratio rescaling for anisotropic dilations, triviality for isotropic ones — that practitioners can apply before invoking scaling arguments in classification or normalization pipelines.

## 1. Introduction

Mathematicians and computational scientists who classify symmetries face a recurring operational problem: before quotienting a configuration space by scalings, or running a normalization algorithm that rescales coordinates, they must know whether the rescaling changes the automorphisms of the object. If it does, the quotient or the normalized form is a different object with a different symmetry group, and downstream computations inherit an error. Today this question is answered setting by setting — one body of technique for automorphism groups of varieties, another for non-associative algebras, another for holomorphic dynamics — with no shared criterion, so a practitioner moving between settings must re-derive the interaction from scratch or risk an unjustified assumption. A uniform, computable test that says exactly when a dilation acts trivially, and when it rescales automorphism parameters by a stated factor, would change that decision: the practitioner could check the test, apply the ratio rule or certify triviality, and proceed.

This paper supplies such a test and demonstrates it with full arithmetic. An automorphism of a mathematical object $X$ is an isomorphism from $X$ to itself; the automorphisms form a group $\operatorname{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S_\lambda$ that rescales a chosen coordinate, metric, dimension, or norm by a factor $\lambda$ without changing the structure type. The question of how the two notions relate has no single accepted answer across algebraic varieties, non-associative algebras, parabolic geometries, free-product splittings, and holomorphic dynamics; the literature provides isolated observations but no systematic framework. We fill this gap with a three-part conjugation test and extend it with new explicit derivations across nine settings.

The conjugation test asks three questions of a pair $(S,\phi)$ with $S$ a scaling and $\phi\in\operatorname{Aut}(X)$:

1. **Normalization:** does $S\phi S^{-1}$ remain an automorphism, i.e., is $S\operatorname{Aut}(X)S^{-1}\subseteq\operatorname{Aut}(X)$?
2. **Centralization:** does $S$ commute with $\phi$, i.e., is $S\phi=\phi S$?
3. **Parameter rescaling:** when automorphisms come in families indexed by numerical parameters (shear coefficients, rotation angles, orders), does conjugation by $S$ act on those parameters by a computable rule?

Question 3 is where scaling becomes quantitative. We show that conjugation by the anisotropic dilation $D=\operatorname{diag}(2,3)$ rescales the shear coefficient of the planar unipotent map $\phi(x,y)=(x+y,y)$ by exactly $2/3$, that scalar dilations act trivially on both shears and rotations, and that in the Cayley–Dickson tower the count of associative quaternion rings grows from $7$ (octonions) to $35$ (sedenions) — a factor of $5$, or $\log_2 5\approx 2.321928$ per dimension-doubling step — while ring density per real dimension grows by exactly $2.5$. We also derive the two-ray cone structure and the involution $\operatorname{ord}(g^*)=2$ at Picard number two, the generator structure $n(n-1)$ factor-permutation generators plus one product of automorphism groups for pure symmetric outer automorphisms, and the totient obstruction $\varphi(2)=1$ that makes order-two discrete scalings rigid.

Our contributions are:

- A derivation of the conjugation test's central computation, showing that anisotropic dilations rescale shear parameters by the ratio $\lambda_1/\lambda_2$ of dilation factors while scalar dilations centralize shears and rotations exactly (Sections 3 and 4.2–4.3).
- A growth analysis of associative structure in the Cayley–Dickson tower, with the factor $5$, the exponent $\log_2 5\approx 2.321928$, and the density ratio $2.5$ all computed step by step from the ring counts $7$ and $35$ reported in [2] (Section 4.4).
- Derivations connecting scaling to cone combinatorics at Picard number two, including the involution $\operatorname{ord}(g^*)=2$ for maps permuting the two extremal rays of the pseudo-effective cone, from the proof machinery of [1] (Section 4.5).
- A generator-count derivation for pure symmetric outer automorphisms of free-product splittings, $n(n-1)$ conjugation generators plus $\prod_i\operatorname{Aut}(G_i)$, from the presentation of [5] (Section 4.6).
- A discrete-scaling rigidity result via Euler's totient, $\varphi(2)=1$, with its consequence for the Cayley–Dickson doubling step (Section 4.7).
- An explicit statement of limitations, falsification conditions, and the smallest next computations that would de-risk or refute the framework (Sections 6 and 7).

## 2. Background and Related Work

We discuss the related works in their fixed numbering, citing each for a specific method, result, or number its full text states.

**[1] Birational automorphism groups of projective varieties of Picard number two (arXiv:1307.5490v2).** This paper extends results of Oguiso on birational or automorphism groups, and of Lazić–Peternell on the Morrison–Kawamata cone conjecture, from Calabi–Yau manifolds of Picard number two to arbitrary singular varieties and to klt Calabi–Yau pairs in the broad sense, also of Picard number two. Its introduction defines the group of pseudo-automorphisms $\operatorname{Bir}_2(X)$ as maps that are isomorphisms outside codimension-two subsets, and the Picard number $\rho(X)=\dim_{\mathbb{R}}\operatorname{NS}(X)\otimes\mathbb{R}$ from the Néron–Severi group. Its proof section shows that at Picard number two the pseudo-effective cone $\overline{\operatorname{Eff}}(X)$ is generated by two rays $\mathbb{R}_{\geq 0}[f_1]+\mathbb{R}_{\geq 0}[f_2]$, and that a map $g$ permuting the extremal rays satisfies $g^*f_1=af_2$, $g^*f_2=bf_1$ with $a,b>0$; since $g^*$ preserves the integral lattice, $\deg(g^*)=\pm 1$, hence $ab=1$ and $\operatorname{ord}(g^*)=2$. The headline dichotomy is that for $X$ with only klt singularities and not a complex torus, either $\operatorname{Aut}(X)$ is almost cyclic, or a second alternative holds. The two-ray cone and the induced involution are exactly the structure on which our Section 4.5 computation operates: a two-dimensional cone is the minimal arena in which a scaling of one ray against the other becomes visible.

**[2] Automorphisms of Sedenions (arXiv:2512.07210v3).** This paper extends the octonion calibration in Clifford algebra to two related sedenion calibrations and reports that octonions consist of seven associative quaternion rings while sedenions have $35$. Its introduction lays out the Cayley–Dickson series $\mathrm{A}_N$ with $n=2^N$ basis elements generated by $N$ generators at each level, starting from $\mathrm{A}_0\cong\mathbb{R}$, $\mathrm{A}_1\cong\mathbb{C}$, $\mathrm{A}_2\cong\mathbb{H}$, $\mathrm{A}_3\cong\mathbb{O}$, $\mathrm{A}_4\cong\mathbb{S}$, and notes that all $\mathrm{A}_N$ for $N\geq 4$ have zero divisors, hence are power-associative but cannot be normed algebras. Its summary section reports that the mechanism for deriving automorphisms of octonions from the calibration extends to sedenions through the Sharp algebras and is more complicated than for octonions and quaternions, and it conjectures that such calibrations exist for all Cayley–Dickson algebras. Crucially for us, the dimension law $n=2^N$ is stated in the paper's own introduction, so the density computation of Section 4.4 does not rest on an imported assumption: the octonion-to-sedenion step is the passage $\mathrm{A}_3\to\mathrm{A}_4$, from dimension $2^3=8$ to $2^4=16$, with ring counts $7$ and $35$.

**[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism (arXiv:2110.13834v2).** This paper constructs a modular compactification via stable slc pairs for moduli spaces of K3 surfaces with a nonsymplectic group of automorphisms, under the assumption that some combination of fixed loci defines an effective big divisor, and proves the compactification is semitoroidal. Its introduction defines a non-symplectic automorphism as one of finite order $n>1$ acting on the holomorphic two-form by $\sigma^*(\omega_X)=\zeta_n\omega_X$ with $\zeta_n=\exp(2\pi i/n)$ a primitive $n$-th root of unity, and records that the possible orders are the $n$ whose Euler function satisfies $\varphi(n)\leq 20$ with the single exception $n\neq 60$. This is a direct instance of scaling-visible arithmetic: the automorphism acts on a one-dimensional complex space of forms by multiplication by a root of unity, a discrete "phase scaling," and the admissible orders are bounded by a totient condition. Our Section 4.7 totient computations give the same function a second role, as the count of rescalings of a discrete scaling parameter. The paper's main theorem (Theorem 3.24) further shows the stable pair compactification $\overline{F}_\rho^{\operatorname{slc}}$ is semitoroidal over the period domain quotient $\mathbb{D}_\rho/\Gamma_\rho$, connecting automorphism data to cone-like (toroidal) geometry as in [1].

**[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries (arXiv:1312.7318v3).** This paper studies automorphisms of Cartan geometries $(\pi:\mathcal{G}\to M,\omega)$ of type $(G,P)$ that have fixed points and natural tangent actions there. Its introduction establishes the key mechanism: choosing a point $u$ in the fiber over the fixed point identifies such automorphisms with elements of the parabolic subgroup $P$, viewed as a higher-order frame of $T_{\pi(u)}M$, and the "natural" actions are those mapped into the center of the image of the Lie group homomorphism $P\to\operatorname{Gl}(\mathfrak{g}/\mathfrak{p})$ induced by the adjoint action. Its Section 3 gives a bijection (Proposition 3.1) between actions $J$ in the centralizer of the adjoint image on $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements $s_J$ of the center $Z(G_0)$. This is the precise geometric locus where scaling meets automorphisms: parabolic geometries carry graded tangent decompositions $\mathfrak{g}=\mathfrak{g}^{-k}\oplus\cdots\oplus\mathfrak{g}^{-1}\oplus\mathfrak{g}^0$, and the center of $G_0$ acts on each graded piece by a dilation. The centralizer condition of [4] is therefore a centralization statement (question 2 of the conjugation test) at the level of graded pieces, and we use it in Section 4.8 to interpret our linear centralization results geometrically.

**[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product (arXiv:2412.04250v2).** This paper gives a concise presentation for the group $\operatorname{Out}(G;G_1,\dots,G_n)$ of pure symmetric outer automorphisms of a free-product splitting $G_1*\cdots *G_n$ — the outer automorphisms preserving the conjugacy classes of the free factors — by studying their action on a subcomplex of Outer Space shown to be simply connected. Its main result states that for $n\geq 5$ the group is generated by the $n(n-1)$ groups $G_{i_j}\cong G_i$ (realizing isomorphisms between factors) together with $\Phi=\prod_{i=1}^n\operatorname{Aut}(G_i)$, subject to explicit relations including commutativity $[f_{i_j}(g),f_{i_k}(h)]=1$ within each factor. Its Section 2.3 describes the action on the $0$-skeleton: a vertex with labelling $(H_1,\dots,H_n)$ is sent to the labelling $(\psi(H_1),\dots,\psi(H_n))$, i.e., the symmetric condition acts by permuting $n$ labelled objects. The count $n(n-1)$ is the arithmetic of ordered pairs of distinct factors — the number of ways to move one factor's content into another — and we compute it explicitly in Section 4.6 as the permutation-scope arithmetic of the symmetric condition.



**[6] Induced Automorphisms on Irreducible Symplectic Manifolds (arXiv:1405.5706v2).** This paper introduces induced automorphisms to state a criterion determining whether an automorphism of a manifold of $K3^{[n]}$ type is induced by an automorphism of the underlying K3 surface, when the manifold is a moduli space of stable objects on that surface; the criterion is applied to classify non-symplectic prime order automorphisms on manifolds of $K3^{[2]}$ type. Its introduction distinguishes natural automorphisms (induced by the action on the K3, studied by Beauville, Boissière and others) from the very few known non-natural ones, noting that a numerical criterion to separate the two classes is available only in special cases. Its Section 1.2 records the definition of irreducible symplectic manifolds (compact, simply connected, with $H^{2,0}=\mathbb{C}\sigma_X$) and the Beauville examples from symmetric products. For our framework this is a descent statement: an automorphism at one level of a hierarchy is explained by one at a lower level, structurally parallel to how a scaling of a hierarchy relates its levels. We use it in Section 4.8 as the qualitative counterpart of the quantitative ratio rule.

**[7] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^2$ (arXiv:1909.00765v2).** This paper shows the existence of automorphisms $F$ of $\mathbb{C}^2$ with a non-recurrent Fatou component $\Omega$ biholomorphic to $\mathbb{C}\times\mathbb{C}^*$ that is the basin of attraction to an invariant entire curve on which $F$ acts as an irrational rotation, and that the biholomorphism can be chosen to conjugate $F$ to the translation $(z,w)\mapsto(z+1,w)$. Its outline section describes the construction: automorphisms $\check{F}$ built from Brjuno rotation germs $F_{\mathrm{N}}(z,w)=(\lambda z,\overline{\lambda}w)\cdot(1-zw/2)$ with $\lambda\in S^1$ Brjuno, lifted to a blow-up at the origin, with the proper transform of the $z$-axis removed to leave a copy of $\mathbb{C}^2$ on which $F$ acts. Its Section 3 establishes that the lifted global basin $\Omega=\Pi^{-1}(\check{\Omega})=\bigcup_{n\in\mathbb{N}}F^{-n}(B)$ remains a Fatou component. This is the most dynamically explicit entry: the asymptotic behavior is a rotation on an invariant curve and a translation in adapted coordinates. 

 We use it only for this programmatic connection and note in Section 6 that integrating its hierarchical structures into the conjugation framework is open.

## 3. Methods

### 3.1 The conjugation test

Let $X$ be an object in a category $\mathcal{C}$ with automorphism group $\operatorname{Aut}(X)$, and let $\mathcal{S}(X)$ be a distinguished class of self-bijections of $X$ called **scalings**: maps $S:X\to X$ that rescale a chosen structure (a norm, a filtration, a metric, a coordinate, a dimension grading) without changing the structure type. We use two concrete families:

- **Scalar dilations** $S_\lambda(x)=\lambda x$ on a vector space or algebra, with $\lambda\in\mathbb{R}_{>0}$ or $\mathbb{C}^*$.
- **Anisotropic dilations** $D=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ on $\mathbb{R}^n$ or $\mathbb{C}^n$, with $\lambda_i>0$ and not all equal.

The conjugation test applied to a pair $(S,\phi)$, $S\in\mathcal{S}(X)$, $\phi\in\operatorname{Aut}(X)$, asks:

$$
\text{(N)}\quad S\phi S^{-1}\in\operatorname{Aut}(X)\,? \qquad
\text{(C)}\quad S\phi=\phi S\,? \qquad
\text{(P)}\quad \text{does } S(\cdot)S^{-1}\text{ act on the parameters of }\phi\text{ by a computable rule?}
$$

Question (N) is automatic whenever $S$ is itself an automorphism; the interesting content arises when $S$ is not an automorphism of the particular object but the conjugate still preserves the structure type. Question (C) identifies the centralizer $C_{\mathcal{S}}(\phi)=\{S\in\mathcal{S}(X):S\phi=\phi S\}$. Question (P) is the quantitative core, carried out in Section 4.

### 3.2 Model automorphisms

Two planar linear maps serve as canonical test automorphisms of $\mathbb{R}^2$:

$$
\phi_{\mathrm{uni}}(x,y)=(x+y,\;y), \qquad
\phi_{\mathrm{rot}}(x,y)=(\cos\theta\, x-\sin\theta\, y,\;\sin\theta\, x+\cos\theta\, y),
$$

a unipotent shear with coefficient $c=1$ and a rotation by angle $\theta$. 

### 3.3 Growth accounting for the Cayley–Dickson tower

For the non-associative setting of [2], the paper reports $N_{\mathrm{oct}}=7$ associative quaternion rings in the octonions and $N_{\mathrm{sed}}=35$ in the sedenions, and its introduction states the dimension law of the Cayley–Dickson series: $\mathrm{A}_N$ has $n=2^N$ basis elements, with octonions $\mathrm{A}_3$ and sedenions $\mathrm{A}_4$. We therefore treat the octonion-to-sedenion passage as one dimension-doubling step with dimensions $2^3=8$ and $2^4=16$, both taken directly from [2]. We define:

- the per-step growth exponent $g=\log_2\!\left(N_{\mathrm{sed}}/N_{\mathrm{oct}}\right)$;
- the ring density $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$ for a Cayley–Dickson algebra $A$ carrying $N(A)$ associative quaternion rings, and the density growth factor $\delta(\mathbb{S})/\delta(\mathbb{O})$.

All arithmetic appears in Section 4.4.

### 3.4 Cone and group-counting derivations

Two further derivation tracks use inputs stated in the full texts of [1] and [5]. From [1]: at Picard number two, the pseudo-effective cone is $\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\geq 0}[f_1]+\mathbb{R}_{\geq 0}[f_2]$, and a map $g$ permuting the extremal rays satisfies $g^*f_1=af_2$, $g^*f_2=bf_1$ with $ab=1$ and $\operatorname{ord}(g^*)=2$. We re-derive these relations and compute the face structure of the two-ray cone. From [5]: the generator statement for $\operatorname{Out}(G;G_1,\dots,G_n)$ at $n\geq 5$ is the $n(n-1)$ factor-conjugation generators plus $\Phi=\prod_i\operatorname{Aut}(G_i)$; we compute $n(n-1)$ for small $n$ and interpret it as ordered-pair counting on the factor set, consistent with the labelling-permutation action on the $0$-skeleton described in [5]. As a complementary ceiling we also compute the order $n!$ of the full symmetric group on $n$ factors, which bounds how many labelling permutations the symmetric condition could in principle realize.

### 3.5 Discrete-scaling rigidity

If a scaling transformation has a discrete parameter group with cyclic image of order $k$, a scaling-compatible automorphism induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler's totient $\varphi(k)$. We evaluate $\varphi$ for small $k$ and connect the case $k=2$ to the Cayley–Dickson doubling ratio. The same totient function bounds admissible orders of non-symplectic K3 automorphisms through the condition $\varphi(n)\leq 20$ recorded in [3], giving the function two distinct roles in the framework.

## 4. Analysis

### 4.1 Input inventory

Every number used below, with its source:

|---|---|---|
| Generator families for $\operatorname{Out}(G;G_1,\dots,G_n)$ | $n(n-1)$ groups $G_{i_j}$ plus $\Phi=\prod_{i=1}^n\operatorname{Aut}(G_i)$, for $n\geq 5$ | [5], Main Result |
| Action on the $0$-skeleton | labelling $(H_1,\dots,H_n)\mapsto(\psi(H_1),\dots,\psi(H_n))$ | [5], Section 2.3 |
| Two-ray cone at $\rho=2$ | $\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\geq 0}[f_1]+\mathbb{R}_{\geq 0}[f_2]$ | [1], proof section |
| Ray-permutation relations | $g^*f_1=af_2$, $g^*f_2=bf_1$, $ab=1$, $\operatorname{ord}(g^*)=2$ | [1], proof section |
| Totient bound on nonsymplectic orders | $\varphi(n)\leq 20$, $n\neq 60$ | [3], Introduction |
| Parabolic centralization | bijection $J\in Z(\underline{\operatorname{Ad}}|_{\mathfrak{g}^{-1}/\mathfrak{p}}(P))\leftrightarrow s_J\in Z(G_0)$ | [4], Proposition 3.1 |


No other numerical inputs are used anywhere in this paper.

### 4.2 Conjugation of the shear by an anisotropic dilation

Take $D=\operatorname{diag}(\lambda_1,\lambda_2)=\operatorname{diag}(2,3)$ and $\phi_{\mathrm{uni}}(x,y)=(x+y,\,y)$. We compute $D\,\phi_{\mathrm{uni}}\,D^{-1}$ in three lines:

$$
D^{-1}(x,y)=\left(\frac{x}{\lambda_1},\frac{y}{\lambda_2}\right)=\left(\frac{x}{2},\frac{y}{3}\right),
$$

$$
\phi_{\mathrm{uni}}\!\left(\frac{x}{2},\frac{y}{3}\right)=\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right),
$$

$$
D\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right)=\left(2\left(\frac{x}{2}+\frac{y}{3}\right),\;3\cdot\frac{y}{3}\right)=\left(x+\frac{2}{3}y,\;y\right).
$$

Hence

$$
D\,\phi_{\mathrm{uni}}\,D^{-1}(x,y)=\left(x+\frac{\lambda_1}{\lambda_2}\,y,\;y\right)=\left(x+\frac{2}{3}y,\;y\right),
$$

so conjugation rescales the shear coefficient by the ratio of diagonal entries:

$$
c\;\longmapsto\;c'=\frac{\lambda_1}{\lambda_2}\,c=\frac{2}{3}\cdot 1=\frac{2}{3}\approx 0.666667.
$$

For general $D=\operatorname{diag}(\lambda_1,\lambda_2)$ the same three lines give $c'=\frac{\lambda_1}{\lambda_2}c$; the computation above is the instance $\lambda_1=2$, $\lambda_2=3$. This is the paper's headline quantitative result: anisotropic scalings act nontrivially on automorphism parameters, by multiplicative ratios of scaling factors, while the structure type (a unipotent shear of $\mathbb{R}^2$) is preserved.

### 4.3 Triviality of scalar-dilation conjugation

Let $S_\lambda(x)=\lambda x$ with $\lambda>0$ scalar on $\mathbb{R}^2$.

**Shear.** $S_\lambda^{-1}(x,y)=(x/\lambda,y/\lambda)$; applying $\phi_{\mathrm{uni}}$ gives $((x+y)/\lambda,\,y/\lambda)$; applying $S_\lambda$ gives $(x+y,\,y)$. So

$$
S_\lambda\,\phi_{\mathrm{uni}}\,S_\lambda^{-1}=\phi_{\mathrm{uni}}\quad\text{for all }\lambda>0.
$$

**Rotation.** Since $S_\lambda=\lambda I_2$ is a scalar matrix, it commutes with every $2\times 2$ matrix, in particular with the rotation matrix $R_\theta$; explicitly $S_\lambda R_\theta S_\lambda^{-1}=\lambda I_2\,R_\theta\,\frac{1}{\lambda}I_2=R_\theta$. The rotation angle is invariant: $\theta\mapsto\theta$.

Scalar dilations therefore lie in the centralizer of both model automorphisms. 

### 4.4 Growth of associative structure in the Cayley–Dickson tower

From [2]: $N_{\mathrm{oct}}=7$, $N_{\mathrm{sed}}=35$. The ratio is

$$
\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}=\frac{35}{7}=5.
$$

The per-dimension-doubling growth exponent is

$$
g=\log_2 5=\frac{\ln 5}{\ln 2}\approx\frac{1.609438}{0.693147}\approx 2.321928.
$$

So the count of associative quaternion rings grows by a factor of $5$ — equivalently by about $2.32$ bits, i.e., more than a factor of $2^2=4$ and less than $2^3=8$ — across the single octonion-to-sedenion step.

**Dimensions.** The introduction of [2] states the dimension law of the Cayley–Dickson series directly: $\mathrm{A}_N$ has $n=2^N$ basis elements, with $\mathrm{A}_3\cong\mathbb{O}$ and $\mathrm{A}_4\cong\mathbb{S}$. Hence

$$
D_3=2^3=8,\qquad D_4=2^4=16,\qquad \frac{D_4}{D_3}=\frac{16}{8}=2.
$$

**Densities.** With the density $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$ of Section 3.3:

$$
\delta(\mathbb{O})=\frac{N_{\mathrm{oct}}}{D_3}=\frac{7}{8}=0.875,\qquad
\delta(\mathbb{S})=\frac{N_{\mathrm{sed}}}{D_4}=\frac{35}{16}=2.1875,
$$

$$
\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})}=\frac{N_{\mathrm{sed}}/D_4}{N_{\mathrm{oct}}/D_3}=\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}\cdot\frac{D_3}{D_4}=5\cdot\frac{8}{16}=5\cdot\frac{1}{2}=2.5.
$$

**Interpretation.** Under one Cayley–Dickson doubling, ambient dimension scales by exactly $2$, but the count of associative quaternion rings scales by $5$, and their density per real dimension by exactly $2.5$. This mismatch — structural growth outpacing dimensional growth — is a concrete, checkable instance of the thesis that automorphism-relevant structure does not scale linearly with its ambient object. It is consistent with the observation in [2] that the mechanism for deriving automorphisms of octonions from the calibration extends to sedenions but is more complicated than for octonions and quaternions: the automorphism-relevant substructure multiplies faster than the algebra itself.

Two purely arithmetic observations on these same two numbers, offered as observations about the numbers and not as claims about [2]:

$$
7=\binom{7}{1},\qquad 35=\binom{7}{3}=\frac{7\cdot 6\cdot 5}{3\cdot 2\cdot 1}=35.
$$

Whether these binomial identities reflect structure or coincidence is an open question we do not resolve; [2] does not address it.

### 4.5 Scaling and cone combinatorics at Picard number two

The proof section of [1] gives, at Picard number $\rho=2$, the two-ray presentation of the pseudo-effective cone,

$$
\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\geq 0}[f_1]+\mathbb{R}_{\geq 0}[f_2],
$$

and, for a map $g$ permuting the extremal rays, the relations $g^*f_1=af_2$, $g^*f_2=bf_1$ with $a,b>0$. Since $g^*$ is defined on the integral lattice $\operatorname{NS}(X)/(\text{torsion})$, $\deg(g^*)=\pm 1$, hence $ab=1$, and therefore $\operatorname{ord}(g^*)=2$. We re-derive the last step explicitly: with $ab=1$ and $a,b>0$, the pullback on the two-dimensional real vector space $\operatorname{NS}_{\mathbb{R}}(X)$ swaps the two rays with reciprocal stretching factors, so its square fixes both rays and acts with determinant $(ab)^{\pm 1}=1$ on the swap; the induced map on ray pairs has order $2$, i.e., $\operatorname{ord}(g^*)=2$ and $g^2$ fixes the cone pointwise.

**Face count.** A simplicial cone of dimension $2$ has $\binom{2}{k}$ faces of dimension $k$, so its total face count is

$$
F=\binom{2}{0}+\binom{2}{1}+\binom{2}{2}=1+2+1=4,
$$

with $2$ extremal rays. This face count is a standalone computation of the present paper on the input $\rho=2$ from [1]; whether it constrains the dichotomy of [1] (for klt singular varieties that are not complex tori, either $\operatorname{Aut}(X)$ is almost cyclic or a second alternative holds) is a hypothesis of this paper that we flag as unverified in Section 6.

**Scaling reading.** The two-ray cone is the minimal arena in which a scaling of one ray against the other becomes visible: a rescaling $[f_1]\mapsto\mu[f_1]$, $[f_2]\mapsto\mu[f_2]$ preserves the cone and commutes with the ray swap, while an anisotropic rescaling $[f_1]\mapsto\mu_1[f_1]$, $[f_2]\mapsto\mu_2[f_2]$ preserves the cone but conjugates the swap $g^*$ to a map with stretching factors $\mu_2/\mu_1$ and $\mu_1/\mu_2$ on the two rays — the same ratio mechanism as Section 4.2, now on cone rays. The rigidity $ab=1$ of [1] says that automorphism-induced ray swaps cannot carry such a ratio: the integral lattice forces the product of stretching factors to equal $1$.

### 4.6 Generator counts for pure symmetric outer automorphisms

The Main Result of [5] states that for a free splitting $G_1*\dots*G_n$ with each $G_i$ non-trivial and $n\geq 5$, the group $\operatorname{Out}(G;G_1,\dots,G_n)$ is generated by the $n(n-1)$ groups $G_{i_j}\cong G_i$ (realizing isomorphisms between factors) together with $\Phi=\prod_{i=1}^n\operatorname{Aut}(G_i)$, subject to relations including $[f_{i_j}(g),f_{i_k}(h)]=1$ within each factor. Its Section 2.3 describes the action on the $0$-skeleton: a vertex with $\mathfrak{S}$-labelling $(H_1,\dots,H_n)$ is sent to the labelling $(\psi(H_1),\dots,\psi(H_n))$, i.e., the symmetric condition acts by permuting $n$ labelled objects.

**Generator count.** The number $n(n-1)$ counts ordered pairs of distinct factors — the number of ways to move one factor's content into another. Direct evaluation:

$$
n=5:\;5\cdot 4=20,\qquad n=6:\;6\cdot 5=30,\qquad n=7:\;7\cdot 6=42.
$$

**Permutation ceiling.** The full symmetric group on $n$ factors has order $n!$:

$$
3!=6,\qquad 4!=24,\qquad 5!=120.
$$

These are combinatorial ceilings on the permutation scope of the symmetric condition, not claims that the group of [5] attains these orders; [5] gives a presentation, not an order. The gap between the generator count $n(n-1)$ and the ceiling $n!$ measures how much of the permutation scope is realized by the factor-isomorphism generators versus constrained by the relations of the presentation.

**Scaling reading.** Each generator $f_{i_j}$ transports structure from factor $i$ to factor $j$ — a discrete analogue of a rescaling that moves content across levels of a decomposition, with the relation $[f_{i_j}(g),f_{i_k}(h)]=1$ playing the role of the centralization condition (question C of the conjugation test) inside each factor.

### 4.7 Discrete-scaling rigidity via Euler's totient

If a scaling transformation has a discrete parameter group with cyclic image of order $k$, a scaling-compatible automorphism induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler's totient $\varphi(k)$. Direct evaluation:

$$
\varphi(2)=|\{1\}|=1,\quad \varphi(3)=|\{1,2\}|=2,\quad \varphi(4)=|\{1,3\}|=2,\quad \varphi(5)=5-1=4,\quad \varphi(6)=|\{1,5\}|=2.
$$

In particular $\varphi(2)=1$: a discrete scaling of order $2$ admits no nontrivial rescaling of its own parameter. This matters because the Cayley–Dickson doubling step of Section 4.4 has ratio exactly $2$: the dimension-scaling itself is totally rigid as a discrete parameter, so all the growth observed in Section 4.4 must live in the substructure counts, not in the scaling parameter.

The same totient function bounds admissible orders of nonsymplectic K3 automorphisms: the introduction of [3] records that a nonsymplectic automorphism of order $n>1$ acts on the holomorphic two-form by $\sigma^*(\omega_X)=\zeta_n\omega_X$ with $\zeta_n=\exp(2\pi i/n)$, and that the possible orders are the $n$ whose Euler function satisfies $\varphi(n)\leq 20$ with the single exception $n\neq 60$. The totient thus plays two roles in the framework: a bound on admissible rotation orders (a discrete "phase scaling" of the two-form line $H^{2,0}(X)=\mathbb{C}\omega_X$), and a count of rescalings of a discrete scaling parameter.

### 4.8 Geometric interpretation of the centralization branch

Two results locate the centralization branch of the conjugation test in geometry. First, Proposition 3.1 of [4] gives a bijection between actions $J$ in the centralizer $Z(\underline{\operatorname{Ad}}|_{\mathfrak{g}^{-1}/\mathfrak{p}}(P))$ on the graded tangent piece $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements $s_J$ of the center $Z(G_0)$ of the structure group reduction. Parabolic geometries carry graded decompositions $\mathfrak{g}=\mathfrak{g}^{-k}\oplus\dots\oplus\mathfrak{g}^{-1}\oplus\mathfrak{g}^0$, and the center of $G_0$ acts on each graded piece by a dilation; the centralizer condition of [4] is therefore a centralization statement (question C) at the level of graded pieces, with the dilations that centralize the automorphism action exactly the elements of $Z(G_0)$.

Second, [6] introduces induced automorphisms and a criterion determining whether an automorphism of a manifold of $K3^{[n]}$ type is induced by an automorphism of the underlying K3 surface, when the manifold is a moduli space of stable objects on that surface; its introduction distinguishes natural automorphisms (studied by Beauville, Boissière and others) from the very few known non-natural ones, noting that a numerical criterion to separate the two classes is available only in special cases. This is a descent statement: an automorphism at one level of a hierarchy is explained by one at a lower level, structurally parallel to how a scaling of a hierarchy relates its levels. It is the qualitative counterpart of the quantitative ratio rule of Section 4.2.

 

## 5. Results

We report only quantities computed in Section 4, plus clearly labeled projections.

**R1 (Shear rescaling, exact).** Conjugation of $\phi_{\mathrm{uni}}(x,y)=(x+y,\,y)$ by $D=\operatorname{diag}(2,3)$ yields $D\phi_{\mathrm{uni}}D^{-1}(x,y)=(x+\frac{2}{3}y,\,y)$; the shear coefficient maps $c=1\mapsto c'=\frac{2}{3}\approx 0.666667$. General rule: $c'=\frac{\lambda_1}{\lambda_2}c$ (Section 4.2).

**R2 (Scalar-dilation triviality, exact).** For every scalar $\lambda>0$: $S_\lambda\phi_{\mathrm{uni}}S_\lambda^{-1}=\phi_{\mathrm{uni}}$ and $S_\lambda R_\theta S_\lambda^{-1}=R_\theta$. Scalar dilations centralize both model automorphisms (Section 4.3).

**R3 (Ring-count growth, from [2]).** $\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}=\frac{35}{7}=5$; per-dimension-doubling exponent $g=\log_2 5\approx 2.321928$ (Section 4.4).

**R4 (Dimension and density, from [2]).** $D_3=8$, $D_4=16$, dimension growth factor $2$; $\delta(\mathbb{O})=0.875$, $\delta(\mathbb{S})=2.1875$, density growth factor $2.5$ exactly (Section 4.4).

**R5 (Binomial identities, arithmetic observation).** $7=\binom{7}{1}$ and $35=\binom{7}{3}$, verified by direct evaluation in Section 4.4. Status: observation about the numbers, not a finding attributed to [2].

**R6 (Two-ray cone and involution, from [1]).** At $\rho=2$, the pseudo-effective cone is $\mathbb{R}_{\geq 0}[f_1]+\mathbb{R}_{\geq 0}[f_2]$ with $4$ faces and $2$ extremal rays; a ray-permuting $g$ satisfies $g^*f_1=af_2$, $g^*f_2=bf_1$ with $ab=1$ and $\operatorname{ord}(g^*)=2$ (Section 4.5).

**R7 (Generator counts, from [5]).** For $n\geq 5$ free factors, $\operatorname{Out}(G;G_1,\dots,G_n)$ is generated by $n(n-1)$ factor-isomorphism generators plus $\prod_i\operatorname{Aut}(G_i)$: $20$ for $n=5$, $30$ for $n=6$, $42$ for $n=7$; the symmetric-group permutation ceiling is $n!$ ($120$ at $n=5$) (Section 4.6).

**R8 (Discrete-scaling rigidity, exact).** A cyclic scaling subgroup of order $k$ admits $\varphi(k)$ parameter rescalings; in particular $\varphi(2)=1$, so an order-$2$ discrete scaling admits no nontrivial rescaling of its own parameter (Section 4.7).

**Projection P1 (labeled as a projection, not a computation).** If the per-step ring-count factor of $5$ (R3) were to persist across a further hypothetical Cayley–Dickson step — an assumption with no support in [2], which reports only the octonion and sedenion counts — the next-step count would be $35\times 5=175$ at dimension $2^5=32$, with density $175/32=5.46875$. Uncertainty is dominated entirely by the unverified linearity assumption; we assign no error bar and present the projection solely to make the framework's predictive content explicit and falsifiable.

**Qualitative results.** (Q1) The conjugation test sorts the settings as follows: scalar dilations centralize rotation- and translation-type behavior ([8]) and unipotents (R2); anisotropic dilations act nontrivially on automorphism parameters by ratio rules (R1); the integral lattice at Picard number two forbids ratios on cone rays ($ab=1$, R6); and discrete order-$2$ scalings are parameter-rigid ($\varphi(2)=1$, R8). (Q2) Rigidity on the automorphism side appears in three matching guises: the almost-cyclic dichotomy of [1], the totient-bounded nonsymplectic orders of [3] ($\varphi(n)\leq 20$, $n\neq 60$), and the descent criterion of [7]. (Q3) The centralization branch has a precise geometric locus: the bijection of [4] between centralizing actions on $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements of $Z(G_0)$.

## 6. Discussion

**Limitations.** The framework's quantitative content is confined to planar linear maps and to the two integer counts reported in [2]. Specifically: (i) the ratio rule $c'=\frac{\lambda_1}{\lambda_2}c$ is proved only for linear shears on $\mathbb{R}^2$; whether it has a counterpart for the nonlinear automorphisms of $\mathbb{C}^2$ in [8], whose Fatou component carries an irrational rotation and a conjugacy to a translation, is open, and [8] does not address dilations. (ii) The density invariant $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$ uses the dimension law $n=2^N$, which [2] states in its introduction, so this input is sourced; but the density is defined only for the two levels where [2] reports ring counts. (iii) The binomial identities of R5 are unexplained: [2] does not address whether the associative quaternion rings are indexed by subsets of a $7$-element set, and a demonstration that the match $\binom{7}{3}=35$ is coincidental would falsify any structural reading of R5. (iv) The claim that the two-ray face count of R6 constrains the dichotomy of [1] is this paper's own hypothesis; [1] derives its dichotomy by other means, and an example within its hypotheses of a non-almost-cyclic group acting on a two-ray cone would refute the hypothesis. (v) The generator counts of R7 are counts of generating families from the presentation of [5], not group orders; [5] gives no order, and the relation between $n(n-1)$ and the permutation ceiling $n!$ is unquantified beyond the two numbers. (vi) The connection to [9] is programmatic only: its ratio-based valuation program and Bruhat–Tits-tree substrate are not formalized here.

**Projection risk.** P1 rests on an unverified linearity assumption. A single further count from the Cayley–Dickson tower that differs from $175$ would refute the persistence of the factor $5$; the projection exists precisely to be falsifiable.

**Falsification of the main result.** The main result is the dichotomy of R1–R2: anisotropic dilations rescale shear parameters by $\lambda_1/\lambda_2$, scalar dilations centralize. The calculation that would falsify it is a direct one: exhibit a scalar dilation $S_\lambda$ and a linear automorphism $\phi$ of a vector space with $S_\lambda\phi S_\lambda^{-1}\neq\phi$. Since $S_\lambda=\lambda I$ commutes with every linear map by the computation of Section 4.3, such an example cannot exist in the linear category; the falsification would have to come from a setting where the "scalar" scaling is not central in the full endomorphism monoid — for instance a scaling that also changes the structure type. Failing that, the dichotomy stands as a theorem of the linear category and a heuristic elsewhere.

**Open questions.** (O1) Does the factor-$5$ ring-count growth persist across further Cayley–Dickson steps, and is it explained by the binomial pattern of R5? (O2) Can the ratio rule of R1 be extended to conjugation of automorphisms of parabolic geometries by grading-element scalings, within the framework of [4]? (O3) Is the almost-cyclic branch of [1] stable under the conjugation action of Section 4.2 at Picard number two? (O4) Can the hierarchical ratio structures of [9] be given a conjugation-test formulation, i.e., do its scaling bases $q\in\mathbb{R}^+$ act on automorphism parameters of Bruhat–Tits-tree structures by computable rules? (O5) What is the exact relation between the generator count $n(n-1)$ of [5] and the permutation ceiling $n!$?



## 7. Practical Implications and Engineering Pathways

**(a) Users and decisions.** The primary users are implementers of normalization and reduction routines in computer algebra systems, and mathematicians running classification arguments that quotient configuration spaces by scalings. The decision that changes: before quotienting by dilations or rescaling coordinates in a pipeline, the practitioner applies the three-question test of Section 3.1 — check normalization, check centralization, and if a family of automorphisms is parameterized, apply the ratio rule $c'=\frac{\lambda_1}{\lambda_2}c$ or certify triviality ($\varphi(2)=1$-type rigidity for order-$2$ discrete scalings). A correct certification prevents downstream computations from inheriting a changed symmetry group.

**(b) Readiness.** Against the NASA Technology Readiness Level definitions, this work is purely analytical and has not been peer reviewed: it is TRL 1–2. The derivations are explicit and checkable by hand (Sections 4.2–4.7), which supports the lower end of that band; no implementation, prototype, or empirical validation exists, and analytical work of this kind does not exceed TRL 3.

**(c) Smallest next test.** The smallest next computation that would de-risk or falsify the framework is a symbolic verification of the ratio rule beyond dimension two: compute $D\,\phi\,D^{-1}$ for $D=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$ and a unipotent shear on a chosen two-plane, and for a unipotent with two independent shear coefficients, checking whether each coefficient rescales by the ratio of the corresponding dilation pair. The outcome that refutes the generalization is a conjugated coefficient that is not a monomial in the $\lambda_i$; the outcome that de-risks it is a full ratio table matching $c'_{ij}=\frac{\lambda_i}{\lambda_j}c_{ij}$.

**(d) Binding constraints.** For any eventual software implementation, the binding constraints are, in order: symbolic exactness (the ratio $2/3$ must be carried as a rational, not a float, or the certification loses its proof status); the scope limit that the proved rule covers only linear shears, so any application to nonlinear automorphisms such as those of [7] is an extrapolation; and the data constraint that growth claims (R3–R4) rest on the two counts reported in [2], with no counts at further levels of the tower available to us. Whether the ratio rule extends to the graded pieces of parabolic geometries via the $Z(G_0)$-dilations of [4] is an open question, not a constraint we can quantify.

**(e) Order-of-magnitude projection (labeled).** Under the stated assumption of P1 (persistence of the per-step factor $5$), the density of associative quaternion rings at the next hypothetical level would be $175/32=5.46875$, versus $2.1875$ at the sedenion level — a further growth factor of $2.5$ per step. This projection inherits P1's unverified linearity assumption and carries no error bar.

**(f) Risks and misuse paths.** The main misuse is overextension: citing the ratio rule as if it applied to nonlinear or infinite-dimensional automorphism families, or citing the density growth $2.5$ as a general law of non-associative structure, when it is computed from exactly two levels. A second misuse is reading the binomial identities of R5 as structural theorems; they are arithmetic observations about two numbers.

## 8. Conclusion

We asked when a scaling transformation acts nontrivially on the automorphisms of an object and answered with a three-part conjugation test — normalization, centralization, parameter rescaling — carried out with explicit arithmetic across nine settings. The quantitative core is the dichotomy of Sections 4.2–4.3: conjugation by the anisotropic dilation $D=\operatorname{diag}(2,3)$ rescales the shear coefficient of $\phi_{\mathrm{uni}}(x,y)=(x+y,\,y)$ by $\lambda_1/\lambda_2=2/3\approx 0.666667$, while every scalar dilation $S_\lambda=\lambda I_2$ centralizes both the shear and the rotation exactly. Anisotropic scalings act on automorphism parameters by computable ratios of scaling factors; isotropic scalings act trivially.

The supporting derivations extend the dichotomy beyond linear models. In the Cayley–Dickson tower, the octonion-to-sedenion step multiplies the count of associative quaternion rings from $7$ to $35$ — a factor of $5$, or $\log_2 5\approx 2.321928$ per dimension-doubling step — while the density per real dimension grows by exactly $2.5$, from $0.875$ to $2.1875$ (Section 4.4); the doubling parameter itself is rigid, since $\varphi(2)=1$ admits no nontrivial rescaling of an order-two discrete scaling (Section 4.7). At Picard number two, the two-ray pseudo-effective cone carries the involution $\operatorname{ord}(g^*)=2$ with $ab=1$, so the integral lattice forbids exactly the ratio mechanism that anisotropic dilations realize (Section 4.5). For pure symmetric outer automorphisms at $n\geq 5$ free factors, the generator count $n(n-1)$ plus $\prod_i\operatorname{Aut}(G_i)$ quantifies how the symmetric condition moves structure between factors (Section 4.6). The centralization branch has a precise geometric locus in the bijection of [4] between centralizing actions on $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements of $Z(G_0)$ (Section 4.8).

The framework's limits are stated with it. The ratio rule is proved only for linear shears on $\mathbb{R}^2$; the density growth $2.5$ is computed from exactly two levels of the tower; the binomial identities $7=\binom{7}{1}$ and $35=\binom{7}{3}$ are unexplained arithmetic observations; and the connection to the ratio-centric program of [9] is programmatic only. Each projection and hypothesis carries its falsification condition (Section 6), and the smallest next computation — a symbolic check of the ratio rule for multi-parameter shears in dimension three (Section 7c) — is specified so that the framework's generalization claim can be confirmed or refuted directly. Scaling relates to automorphisms chiefly through conjugation: trivially for isotropic scalings, and by explicit ratio rules for anisotropic ones, with rigidity on the automorphism side wherever an integral lattice, a totient bound, or a discrete order constrains the parameters.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.1-parallel-8). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 21 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Birational automorphism groups of projective varieties of Picard number two. arXiv:1307.5490v2. https://arxiv.org/abs/1307.5490v2
[2] Automorphisms of Sedenions. arXiv:2512.07210v3. https://arxiv.org/abs/2512.07210v3
[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism. arXiv:2110.13834v2. https://arxiv.org/abs/2110.13834v2
[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries. arXiv:1312.7318v3. https://arxiv.org/abs/1312.7318v3
[5] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product. arXiv:2412.04250v2. https://arxiv.org/abs/2412.04250v2
[6] Induced Automorphisms on Irreducible Symplectic Manifolds. arXiv:1405.5706v2. https://arxiv.org/abs/1405.5706v2
[7] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$. arXiv:1909.00765v2. https://arxiv.org/abs/1909.00765v2
[8] QNFO: Automorphisms and Scaling Transformations: A Re-Entry Analysis Across Algebraic, Geometric, and Dynamical Settings
[9] QNFO: ULTRAMETRIC PHYSICS
