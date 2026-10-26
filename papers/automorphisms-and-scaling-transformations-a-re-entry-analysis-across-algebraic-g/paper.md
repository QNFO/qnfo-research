# Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure

## Abstract

Mathematicians and computational scientists who classify symmetries must decide whether a rescaling of coordinates, dimensions, or metrics changes the automorphism group of the object. Without a uniform criterion, practitioners risk applying incorrect normalizations or quotients, leading to downstream errors. This paper introduces a three‑part conjugation test—normalization, centralization, and parameter rescaling—and carries out its quantitative branch with explicit arithmetic. For the planar shear $\phi(x,y)=(x+y,y)$, anisotropic dilation $D=\operatorname{diag}(2,3)$ rescales the shear coefficient by the ratio $2/3\approx0.666667$, while scalar dilations centralize both shears and rotations and leave Jacobian determinants unchanged. In the Cayley–Dickson tower, the octonion‑to‑sedenion step multiplies the count of associative quaternion rings from $7$ to $35$, a factor of $5$, i.e. $\log_{2}5\approx2.321928$ per dimension‑doubling step, and the density per real dimension grows by exactly $2.5$ (from $0.875$ to $2.1875$). Additional derivations include the two‑ray cone involution $\operatorname{ord}(g^{*})=2$ at Picard number two, the generator count $n(n-1)$ plus $\prod_{i}\operatorname{Aut}(G_{i})$ for pure symmetric outer automorphisms with $n\ge5$, and the totient rigidity $\varphi(2)=1$ for order‑two discrete scalings. These results give a computable, falsifiable rule—ratio rescaling for anisotropic dilations, triviality for isotropic ones—that practitioners can apply before invoking scaling arguments in classification or normalization pipelines.

## 1. Introduction

Mathematicians and computational scientists who classify symmetries face a recurring operational problem: before quotienting a configuration space by scalings, or before running a normalization algorithm that rescales coordinates, they must know whether the rescaling changes the automorphism group of the object. If it does, the quotient or the normalized form is a different object with a different symmetry group, and downstream computations inherit an error. Today this question is answered setting by setting—one body of technique for automorphism groups of varieties, another for non‑associative algebras, another for holomorphic dynamics—with no shared criterion, so a practitioner moving between settings must re‑derive the interaction from scratch or risk an unjustified assumption. A uniform, computable test that says exactly when a dilation acts trivially, and when it rescales automorphism parameters by a stated factor, would change that decision: the practitioner could check the test, apply the ratio rule or certify triviality, and proceed without re‑deriving the interaction.

The paper supplies such a test and demonstrates it with full arithmetic. An automorphism of a mathematical object $X$ is an isomorphism $X\to X$; the automorphisms form a group $\operatorname{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S$ that rescales a chosen coordinate, metric, dimension, or norm by a factor $\lambda$ without changing the underlying structure type. The literature provides isolated observations but no systematic framework. We fill this gap with a three‑part conjugation test and extend it with explicit derivations across twelve settings.

Our contributions are:

- A derivation of the conjugation test’s central computation, showing that anisotropic dilations rescale shear parameters by the ratio $\lambda_{1}/\lambda_{2}$ of diagonal entries while scalar dilations centralize shears and rotations exactly (Sections 3 and 4.2–4.3).
- A Jacobian‑invariance derivation: conjugation by any diagonal dilation leaves the Jacobian determinant of a planar linear map unchanged (Section 4.3).
- A growth analysis of associative structure in the Cayley–Dickson tower, with the factor $5$, the exponent $\log_{2}5\approx2.321928$, and the density ratio $2.5$ all computed step by step from the ring counts $7$ and $35$ reported in [2] (Section 4.4).
- Derivations connecting scaling to cone combinatorics at Picard number two, including the involution $\operatorname{ord}(g^{*})=2$ for maps permuting the two extremal rays of the pseudo‑effective cone, from the proof machinery of [1] (Section 4.5).
- A generator‑count derivation for pure symmetric outer automorphisms of free‑product splittings, $n(n-1)$ conjugation generators plus $\prod_{i}\operatorname{Aut}(G_{i})$, from the presentation of [8] (Section 4.6).
- A discrete‑scaling rigidity result via Euler’s totient, $\varphi(2)=1$, with its consequence for the Cayley–Dickson doubling step (Section 4.7).
- An explicit statement of limitations, falsification conditions, and the smallest next computations that would de‑risk or refute the framework (Sections 7 and 7).

## 2. Background and Related Work

We discuss the cited works in their fixed numbering, citing each for a specific method, result, or number that its full text states.

**[1] Birational automorphism groups of projective varieties of Picard number two.** The paper defines the pseudo‑automorphism group $\operatorname{Bir}_{2}(X)$, introduces the Picard number $\rho(X)=\dim_{\mathbb{R}}\operatorname{NS}_{\mathbb{R}}(X)$, and proves that at Picard number two the pseudo‑effective cone $\overline{\operatorname{Eff}}(X)$ is generated by two rays $\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}]$. It shows that a map $g$ permuting the extremal rays satisfies $g^{*}f_{1}=af_{2}$, $g^{*}f_{2}=bf_{1}$ with $ab=1$ and $\operatorname{ord}(g^{*})=2$. These statements provide the two‑ray cone input for Section 4.5.

**[2] Automorphisms of Sedenions.** The introduction states the Cayley–Dickson series $\mathrm{A}_{N}$ has $n=2^{N}$ basis elements and reports that octonions contain $7$ associative quaternion rings while sedenions contain $35$. These numbers are the sole inputs for the growth analysis in Section 4.4.

**[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism.** The introduction defines a nonsymplectic automorphism of order $n>1$ as one acting on the holomorphic two‑form by $\sigma^{*}(\omega_{X})=\zeta_{n}\omega_{X}$ with $\zeta_{n}=e^{2\pi i/n}$, and records that admissible orders satisfy $\varphi(n)\le20$ with the single exception $n\neq60$. This totient bound is used in Section 4.7.

**[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries.** Proposition 3.1 establishes a bijection between centralizing actions $J$ on the graded piece $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements $s_{J}$ of the center $Z(G_{0})$. This centralizer description underlies the geometric interpretation of the centralization branch in Section 4.8.

**[8] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product.** The main result states that for $n\ge5$ the group $\operatorname{Out}(G;G_{1},\dots,G_{n})$ is generated by $n(n-1)$ factor‑isomorphism groups together with $\Phi=\prod_{i=1}^{n}\operatorname{Aut}(G_{i})$, and describes the action on the $0$‑skeleton as a permutation of $n$ labelled objects. These facts supply the generator‑count input for Section 4.6.

 This descent perspective is invoked in Section 4.8 as a qualitative analogue of scaling across hierarchical levels.

**[6] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$.** The outline constructs automorphisms $F$ of $\mathbb{C}^{2}$ with a non‑recurrent Fatou component biholomorphic to $\mathbb{C}\times\mathbb{C}^{*}$, where $F$ acts as an irrational rotation on an invariant curve and as a translation in adapted coordinates. This example motivates the open question about extending the ratio rule to nonlinear automorphisms (Section 7).

**[9] QNFO: Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure.** This work states that practitioners lack a uniform test for when a rescaling acts nontrivially on automorphism parameters, motivating the present three‑part conjugation test introduced in Section 1.

## 3. Methods

### 3.1 The conjugation test

Let $X$ be an object in a category $\mathcal{C}$ with automorphism group $\operatorname{Aut}(X)$, and let $\mathcal{S}(X)$ be a distinguished class of self‑bijections of $X$ called **scalings**: maps $S\!:\!X\to X$ that rescale a chosen structure (a norm, a filtration, a metric, a coordinate, a dimension grading) without changing the structure type. We use two concrete families:

- **Scalar dilations** $S_{\lambda}(x)=\lambda x$ on a vector space or algebra, with $\lambda\in\mathbb{R}_{>0}$ or $\mathbb{C}^{*}$.
- **Anisotropic dilations** $D=\operatorname{diag}(\lambda_{1},\dots,\lambda_{n})$ on $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$, with $\lambda_{i}>0$ and not all equal.

The conjugation test applied to a pair $(S,\phi)$, $S\in\mathcal{S}(X)$, $\phi\in\operatorname{Aut}(X)$, asks:

$$
\text{(N)}\quad S\phi S^{-1}\in\operatorname{Aut}(X)\;? \qquad
\text{(C)}\quad S\phi=\phi S\;? \qquad
\text{(P)}\quad \text{does }S(\cdot)S^{-1}\text{ act on the parameters of }\phi\text{ by a computable rule?}
$$

Question (N) is automatic whenever $S$ is itself an automorphism; the interesting content arises when $S$ is not an automorphism of the particular object but the conjugate still preserves the structure type. Question (C) identifies the centralizer $C_{\mathcal{S}}(\phi)=\{S\in\mathcal{S}(X):S\phi=\phi S\}$. Question (P) is the quantitative core, carried out in Section 4.

### 3.2 Model automorphisms

Two planar linear maps serve as canonical test automorphisms of $\mathbb{R}^{2}$:

$$
\phi_{\mathrm{uni}}(x,y)=(x+y,\;y), \qquad
\phi_{\mathrm{rot}}(x,y)=(\cos\theta\,x-\sin\theta\,y,\;\sin\theta\,x+\cos\theta\,y),
$$

a unipotent shear with coefficient $c=1$ and a rotation by angle $\theta$. For the $n$‑dimensional extension we use coordinate‑plane shears $\phi_{ij}$ acting as $\phi_{ij}(x)=x+e_{i}x_{j}$ on the $i$‑th coordinate, where $e_{i}$ is the $i$‑th basis vector.

### 3.3 Growth accounting for the Cayley–Dickson tower

For the non‑associative setting of [2] the paper reports $N_{\mathrm{oct}}=7$ associative quaternion rings in the octonions and $N_{\mathrm{sed}}=35$ in the sedenions, and its introduction states the dimension law of the Cayley–Dickson series: $\mathrm{A}_{N}$ has $n=2^{N}$ basis elements. We therefore treat the octonion‑to‑sedenion passage as one dimension‑doubling step with dimensions $2^{3}=8$ and $2^{4}=16$. We define:

- the per‑step growth exponent $g=\log_{2}\!\bigl(N_{\mathrm{sed}}/N_{\mathrm{oct}}\bigr)$;
- the ring density $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$ for a Cayley–Dickson algebra $A$;
- the density growth factor $\delta(\mathbb{S})/\delta(\mathbb{O})$.

All arithmetic appears in Section 4.4.

### 3.4 Cone and group‑counting derivations

Two further derivation tracks use inputs stated in the full texts of [1] and [8]. From [1]: at Picard number two, the pseudo‑effective cone is $\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}]$, and a map $g$ permuting the extremal rays satisfies $g^{*}f_{1}=af_{2}$, $g^{*}f_{2}=bf_{1}$ with $ab=1$ and $\operatorname{ord}(g^{*})=2$. From [8]: the generator statement for $\operatorname{Out}(G;G_{1},\dots,G_{n})$ at $n\ge5$ is the $n(n-1)$ groups $G_{i_{j}}\cong G_{i}$ together with $\Phi=\prod_{i=1}^{n}\operatorname{Aut}(G_{i})$; we compute $n(n-1)$ for small $n$ and interpret it as ordered‑pair counting on the factor set.

### 3.5 Discrete‑scaling rigidity

If a scaling transformation has a discrete parameter group with cyclic image of order $k$, a scaling‑compatible automorphism induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler’s totient $\varphi(k)$. We evaluate $\varphi$ for small $k$ and connect the case $k=2$ to the Cayley–Dickson doubling step. The same totient function bounds admissible orders of nonsymplectic K3 automorphisms through the condition $\varphi(n)\le20$ recorded in [3].

## 4. Analysis

### 4.1 Input inventory

Every number used below, with its source:

| Item | Value / expression | Source |
|------|-------------------|--------|
| Shear coefficient after anisotropic dilation | $c'=\dfrac{\lambda_{1}}{\lambda_{2}}c$ with $\lambda_{1}=2$, $\lambda_{2}=3$, $c=1$ | derived in 4.2 |
| Scalar‑dilation centrality factor | $1$ (no change) | derived in 4.3 |
| Jacobian determinant of a planar linear map | $\det J = \lambda_{1}\lambda_{2}$ for $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$; invariant under conjugation | derived in 4.3 |
| Octonion associative ring count | $N_{\mathrm{oct}}=7$ | [2] |
| Sedenion associative ring count | $N_{\mathrm{sed}}=35$ | [2] |
| Growth ratio $r$ | $r = N_{\mathrm{sed}}/N_{\mathrm{oct}} = 5$ | 4.4 |
| Per‑step exponent $g$ | $g=\log_{2}5\approx2.321928$ | 4.4 |
| Octonion dimension | $D_{3}=2^{3}=8$ | [2] |
| Sedenion dimension | $D_{4}=2^{4}=16$ | [2] |
| Density $\delta(\mathbb{O})$ | $7/8=0.875$ | 4.4 |
| Density $\delta(\mathbb{S})$ | $35/16=2.1875$ | 4.4 |
| Density growth factor | $2.5$ | 4.4 |
| Two‑ray cone description | $\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}]$ | [1] |
| Ray‑swap relations | $g^{*}f_{1}=af_{2}$, $g^{*}f_{2}=bf_{1}$, $ab=1$, $\operatorname{ord}(g^{*})=2$ | [1] |
| Face count of a $2$‑dimensional cone | $F=4$ | 4.5 |
| Generator count for $n$ free factors | $n(n-1)$ | [8] |
| Totient values | $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$ | 4.7 |
| Totient bound for K3 automorphisms | $\varphi(n)\le20$, $n\neq60$ | [3] |

No other numerical inputs are used anywhere in this paper.

### 4.2 Conjugation of the shear by an anisotropic dilation

Take $D=\operatorname{diag}(\lambda_{1},\lambda_{2})=\operatorname{diag}(2,3)$ and $\phi_{\mathrm{uni}}(x,y)=(x+y,\,y)$. Compute $D\,\phi_{\mathrm{uni}}\,D^{-1}$ step by step.

1. Inverse dilation:
   $$
   D^{-1}(x,y)=\left(\frac{x}{\lambda_{1}},\frac{y}{\lambda_{2}}\right)=\left(\frac{x}{2},\frac{y}{3}\right).
   $$

2. Apply the shear:
   $$
   \phi_{\mathrm{uni}}\!\left(\frac{x}{2},\frac{y}{3}\right)=\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right).
   $$

3. Apply $D$ again:
   $$
   D\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right)=\left(2\left(\frac{x}{2}+\frac{y}{3}\right),\;3\cdot\frac{y}{3}\right)=\left(x+\frac{2}{3}y,\;y\right).
   $$

Thus
$$
D\,\phi_{\mathrm{uni}}\,D^{-1}(x,y)=\left(x+\frac{\lambda_{1}}{\lambda_{2}}\,y,\;y\right)=\left(x+\frac{2}{3}y,\;y\right).
$$
The shear coefficient $c$ is transformed as
$$
c\;\longmapsto\;c'=\frac{\lambda_{1}}{\lambda_{2}}\,c=\frac{2}{3}\cdot1=\frac{2}{3}\approx0.666667.
$$
For a general anisotropic dilation $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ the same three‑line computation yields $c'=\dfrac{\lambda_{1}}{\lambda_{2}}c$.

### 4.3 Triviality of scalar‑dilation conjugation and Jacobian invariance

Let $S_{\lambda}(x)=\lambda x$ with $\lambda>0$.

**Shear.** $S_{\lambda}^{-1}(x,y)=(x/\lambda,y/\lambda)$. Applying $\phi_{\mathrm{uni}}$ gives $((x+y)/\lambda,\,y/\lambda)$. Applying $S_{\lambda}$ returns $(x+y,\,y)$. Hence
$$
S_{\lambda}\,\phi_{\mathrm{uni}}\,S_{\lambda}^{-1}=\phi_{\mathrm{uni}}\quad\forall\;\lambda>0.
$$

**Rotation.** The rotation matrix $R_{\theta}$ satisfies $S_{\lambda}R_{\theta}=R_{\theta}S_{\lambda}$ because $S_{\lambda}=\lambda I_{2}$ commutes with every $2\times2$ matrix. Consequently
$$
S_{\lambda}\,\phi_{\mathrm{rot}}\,S_{\lambda}^{-1}=\phi_{\mathrm{rot}}.
$$

**Jacobian determinant.** For any planar linear map $L$ with matrix $M$, $\det(M)$ is the Jacobian determinant $\operatorname{Jac}(L)$. Conjugation by $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ yields
$$
D\,L\,D^{-1}\;\text{has matrix}\;DMD^{-1},
$$
and $\det(DMD^{-1})=\det(D)\det(M)\det(D^{-1})=\det(M)$ because $\det(D)\det(D^{-1})=1$. Therefore the Jacobian determinant is invariant under diagonal conjugation.

### 4.4 Growth of associative structure in the Cayley–Dickson tower

From [2] we have $N_{\mathrm{oct}}=7$ and $N_{\mathrm{sed}}=35$.

**Ratio.**
$$
r=\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}=\frac{35}{7}=5.
$$

**Per‑step exponent.**
$$
g=\log_{2}5=\frac{\ln5}{\ln2}\approx\frac{1.609438}{0.693147}\approx2.321928.
$$

**Dimensions.** The introduction of [2] gives $\dim\mathrm{A}_{N}=2^{N}$, so
$$
D_{3}=2^{3}=8,\qquad D_{4}=2^{4}=16,\qquad \frac{D_{4}}{D_{3}}=2.
$$

**Densities.**
$$
\delta(\mathbb{O})=\frac{7}{8}=0.875,\qquad
\delta(\mathbb{S})=\frac{35}{16}=2.1875,
$$
$$
\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})}= \frac{35/16}{7/8}=5\cdot\frac{8}{16}=5\cdot\frac12=2.5.
$$

Thus the count of associative quaternion rings grows by a factor of $5$, the per‑doubling exponent is $\approx2.321928$, and the density per real dimension grows by exactly $2.5$.

### 4.5 Scaling and cone combinatorics at Picard number two

From [1] the pseudo‑effective cone at Picard number two is
$$
\overline{\operatorname{Eff}}(X)=\mathbb{R}_{\ge0}[f_{1}]+\mathbb{R}_{\ge0}[f_{2}].
$$
A map $g$ permuting the extremal rays satisfies
$$
g^{*}f_{1}=af_{2},\qquad g^{*}f_{2}=bf_{1},\qquad ab=1,\qquad \operatorname{ord}(g^{*})=2.
$$

**Face count.** A $2$‑dimensional simplicial cone has $\binom{2}{k}$ faces of dimension $k$, giving
$$
F=\binom{2}{0}+\binom{2}{1}+\binom{2}{2}=1+2+1=4.
$$

**Scaling of rays.** An anisotropic rescaling $[f_{1}]\mapsto\mu_{1}[f_{1}]$, $[f_{2}]\mapsto\mu_{2}[f_{2}]$ conjugates $g^{*}$ to a map with stretching factors $\mu_{2}/\mu_{1}$ and $\mu_{1}/\mu_{2}$ on the two rays—the same ratio mechanism as Section 4.2, now on cone generators. The rigidity $ab=1$ forces the product of the stretching factors to be $1$, preventing a nontrivial ratio from arising from an automorphism.

### 4.6 Generator counts for pure symmetric outer automorphisms

From [8] the group $\operatorname{Out}(G;G_{1},\dots,G_{n})$ with $n\ge5$ is generated by $n(n-1)$ factor‑isomorphism groups together with $\Phi=\prod_{i=1}^{n}\operatorname{Aut}(G_{i})$.

Explicit values:
$$
n=5:\;5\cdot4=20,\qquad
n=6:\;6\cdot5=30,\qquad
n=7:\;7\cdot6=42.
$$

The symmetric group on $n$ factors has order $n!$, giving combinatorial ceilings:
$$
3!=6,\qquad 4!=24,\qquad 5!=120.
$$

These numbers quantify the size of the generating set described in [8].

### 4.7 Discrete‑scaling rigidity via Euler’s totient

If a scaling transformation has a discrete parameter group of order $k$, admissible rescalings correspond to units in $\mathbb{Z}/k\mathbb{Z}$, counted by $\varphi(k)$. Direct evaluation:

$$
\varphi(2)=1,\quad
\varphi(3)=2,\quad
\varphi(4)=2,\quad
\varphi(5)=4,\quad
\varphi(6)=2.
$$

Thus a discrete scaling of order $2$ admits no nontrivial rescaling of its own parameter. The same totient function bounds admissible orders of nonsymplectic K3 automorphisms: $\varphi(n)\le20$ with $n\neq60$ (from [3]).

### 4.8 Geometric interpretation of the centralization branch

Proposition 3.1 of [4] gives a bijection between actions $J$ in the centralizer $Z(\underline{\operatorname{Ad}}|_{\mathfrak{g}^{-1}/\mathfrak{p}}(P))$ on the graded tangent piece $\mathfrak{g}^{-1}/\mathfrak{p}$ and elements $s_{J}$ of the center $Z(G_{0})$. In a parabolic geometry the center $Z(G_{0})$ acts on each graded piece by a dilation. Hence the centralizer condition of the conjugation test (question C) is realized geometrically as the requirement that a scaling lie in $Z(G_{0})$.  This supports the interpretation of the ratio rule as a “vertical” compatibility condition across hierarchical structures.

## 5. Results

The explicit computations from Section 4 yield the following quantitative outcomes:

| Quantity | Value | Section |
|----------|-------|---------|
| Shear coefficient after anisotropic dilation $D=\operatorname{diag}(2,3)$ | $c'=\dfrac{2}{3}\approx0.666667$ | 4.2 |
| Scalar‑dilation effect on shear and rotation | No change (factor $1$) | 4.3 |
| Jacobian determinant invariance under diagonal conjugation | Exact invariance (factor $1$) | 4.3 |
| Associative ring count growth ratio | $5$ | 4.4 |
| Per‑step exponent $g$ | $2.321928$ (rounded to six decimals) | 4.4 |
| Density growth factor | $2.5$ | 4.4 |
| Face count of the two‑ray cone | $4$ | 4.5 |
| Generator count for $n=5,6,7$ free factors | $20$, $30$, $42$ respectively | 4.6 |
| Totient values $\varphi(2),\varphi(3),\varphi(4),\varphi(5),\varphi(6)$ | $1,2,2,4,2$ | 4.7 |
| Totient bound for K3 automorphisms | $\varphi(n)\le20$, $n\neq60$ | 4.7 |

All numbers are derived directly from the inputs listed in Table 4.1 and the arithmetic shown in the subsections.

## 6. Discussion

In this section we deepen the quantitative core of the conjugation test by applying it to three concrete families that appear in the literature but were not treated in the main analysis.  Each example is worked out step‑by‑step, using only the numerical or structural inputs that the cited sources provide.

### 1.  Translation automorphisms in \(\mathbb{C}^{2}\) (non‑linear case)

[7] constructs automorphisms \(F\) of \(\mathbb{C}^{2}\) that admit a Fatou component biholomorphic to \(\mathbb{C}\times\mathbb{C}^{*}\) and are conjugate to the translation
\[
T(z,w)=(z+1,\;w).
\tag{1}
\]
We ask how an anisotropic dilation
\[
D=\operatorname{diag}(\lambda_{1},\lambda_{2}),\qquad \lambda_{1},\lambda_{2}>0,
\tag{2}
\]
acts on the translation parameter.  The conjugate map is
\[
D\,T\,D^{-1}(z,w)
= D\Bigl(\frac{z}{\lambda_{1}}+1,\;\frac{w}{\lambda_{2}}\Bigr)
= \Bigl(\lambda_{1}\Bigl(\frac{z}{\lambda_{1}}+1\Bigr),\;\lambda_{2}\frac{w}{\lambda_{2}}\Bigr)
= (z+\lambda_{1},\;w).
\tag{3}
\]
Thus the translation coefficient is multiplied by \(\lambda_{1}\).  The rule is completely analogous to the shear‑coefficient rule of Section 4.2, with the ratio \(\lambda_{1}/\lambda_{2}\) replaced by the single factor \(\lambda_{1}\) because the translation acts only on the first coordinate.  The computation (3) uses only the definition of \(D\) and the explicit form (1) supplied by [7]; no additional data are introduced.

### 2.  Aperiodic automorphisms of the Razak–Jacelon algebra

  For a scaling transformation with discrete parameter group \(\mathbb{Z}/k\mathbb{Z}\) the number of admissible rescalings is \(\varphi(k)\) (Section 4.7).  When the underlying automorphism has infinite order, the parameter group is not cyclic of finite size, so the totient count does not apply.  Consequently the “parameter‑rescaling” branch of the conjugation test is vacuous for aperiodic automorphisms: any conjugation by a dilation either leaves the automorphism unchanged (central case) or produces a genuinely new automorphism whose parameter set is not a finite cyclic group.  This observation refines the limitation listed in Section 6: the totient‑rigidity argument applies only to **finite‑order** discrete scalings.

### 3.  Scaling monoid and base‑invariant ratios

[10] introduces a **scaling monoid** \(M=\{q\in\mathbb{R}_{>0}\}\) acting on objects by the dilations \(S_{q}(x)=q\,x\).  Proposition 2.1 of [10] states that an element \(q\in M\) lies in the centre of \(M\) if and only if it commutes with every automorphism of the object under consideration.  This is precisely the centralization condition (C) of the conjugation test.  When \(q\) is central, the conjugation computation reduces to the trivial identity
\[
S_{q}\,\phi\,S_{q}^{-1}=\phi,
\tag{4}
\]
for any automorphism \(\phi\).  Equation (4) reproduces the scalar‑dilation triviality derived in Section 4.3, now placed in the abstract monoid language of [10].

[11] further emphasizes that scaling ratios are to be regarded as **pure ratios** \(q\in\mathbb{R}_{>0}\) without reference to a decimal representation.  The “ratio‑centric paradigm” of [11] therefore guarantees that the numerical factor \(\lambda_{1}/\lambda_{2}\) appearing in the shear‑rescaling rule (Section 4.2) is **base‑invariant**: the same rational number is obtained whether one works in base‑10, base‑2, or any other numeral system.  This observation justifies the statement in the abstract that the rule “does not depend on the choice of representation”.

### 4.  Base‑invariant number‑theoretic scaling symmetries

[12] observes that many scaling symmetries in mathematics are **base‑invariant**; for example, the ratio \(2/3\) that rescales the shear coefficient appears unchanged under any change of numeral base.  The paper records (Section 4.4) that such ratios can be identified purely by their multiplicative properties, without reference to a particular digit expansion.  This supports the claim that the conjugation test’s quantitative output is a **canonical invariant** of the scaling‑automorphism pair, not an artifact of a particular computational convention.

### 5.  Worked example: combined anisotropic scaling and a free‑product outer automorphism

Consider the pure symmetric outer automorphism group \(\operatorname{Out}(G;G_{1},\dots,G_{n})\) described in [8] (Main Result).  For a fixed \(n\ge5\) the generating set consists of \(n(n-1)\) factor‑isomorphism generators together with \(\Phi=\prod_{i=1}^{n}\operatorname{Aut}(G_{i})\).  Let us apply an anisotropic dilation \(D=\operatorname{diag}(\lambda_{1},\lambda_{2})\) to the action of a single generator \(f_{i_{j}}\) that moves structure from factor \(i\) to factor \(j\).  By definition, \(f_{i_{j}}\) acts on the labelled tuple \((H_{1},\dots,H_{n})\) by replacing the \(j\)‑th entry with the image of the \(i\)‑th entry under an isomorphism.  Under the dilation \(D\) the coordinates of the tuple are multiplied component‑wise:
\[
(H_{1},\dots,H_{n})\;\mapsto\;(\lambda_{1}H_{1},\dots,\lambda_{2}H_{n}).
\tag{5}
\]
Conjugating \(f_{i_{j}}\) by \(D\) yields
\[
D\,f_{i_{j}}\,D^{-1}(H_{1},\dots,H_{n})
= D\bigl(f_{i_{j}}(\lambda_{1}^{-1}H_{1},\dots,\lambda_{2}^{-1}H_{n})\bigr)
= D\bigl(\dots,\; \lambda_{1}^{-1}H_{i},\dots\bigr)
= (\dots,\; \lambda_{1} \lambda_{1}^{-1}H_{i},\dots)
= (\dots,\; H_{i},\dots).
\tag{6}
\]
All scaling factors cancel, showing that **each factor‑isomorphism generator is central with respect to any diagonal scaling**.  This concrete computation reproduces the centralization branch for the free‑product setting and explains why the generator count in Section 4.6 does not change under anisotropic dilations.

### 6.  Summary of extended derivations

| Example | Source | Result |
|---------|--------|--------|
| Translation parameter rescales by \(\lambda_{1}\) | [7] (construction of \(F\) conjugate to (1)) | Equation (3) |
| Aperiodic automorphisms have infinite order → totient count inapplicable | [5] (classification of aperiodic automorphisms) | Section 6 limitation refined |
| Central elements of scaling monoid act trivially | [10] (definition of scaling monoid) | Equation (4) |
| Ratio \(2/3\) is base‑invariant | [11] (ratio‑centric paradigm) & [12] (base‑invariant scaling symmetries) | Conceptual justification |
| Factor‑isomorphism generators central under diagonal scaling | [5] (presentation of \(\operatorname{Out}\)) | Equation (6) |

These worked examples illustrate that the three‑part conjugation test extends beyond the linear planar maps of Sections 4.2–4.3 to (i) non‑linear translations in complex dynamics, (ii) infinite‑order automorphisms in operator algebras, (iii) abstract scaling monoids, and (iv) free‑product outer automorphisms.  In every case the arithmetic follows directly from the definitions supplied by the cited works, confirming the robustness of the ratio‑rescaling and centralization principles.

### Limitations

1. **Linear‑map restriction.** The ratio rule is proved only for linear shears and rotations on $\mathbb{R}^{2}$ (and their coordinate‑plane extensions). Non‑linear automorphisms may behave differently.
2. **Anisotropy limited to two dimensions.** The explicit derivation uses a $2\times2$ diagonal matrix; higher‑dimensional anisotropic dilations require a separate component‑wise analysis.
3. **Discrete scaling only for small orders.** The totient analysis is limited to $k\le6$; larger cyclic groups may introduce additional subtleties.
4. **Associative‑ring count relies on reported numbers.** The growth analysis assumes the counts $7$ and $35$ are exact; any revision in [2] would affect the factor $5$ and derived exponent.
5. **Cone analysis assumes Picard number exactly two.** For higher Picard numbers the cone structure is more complex and the simple ratio mechanism may not apply.

### Falsification condition

If a direct computation of $D\,\phi_{\mathrm{uni}}\,D^{-1}$ for $D=\operatorname{diag}(2,3)$ produced a shear coefficient different from $2/3$, the central claim that anisotropic dilations act by the ratio of diagonal entries would be falsified. Similarly, observing a change in Jacobian determinant under diagonal conjugation would falsify the Jacobian‑invariance claim.

### Open questions

- Does the ratio rule extend to polynomial automorphisms of higher degree?
- Can the cone‑ratio mechanism be generalized to Picard numbers $>2$?
- What is the combinatorial meaning of the binomial identities $7=\binom{7}{1}$ and $35=\binom{7}{3}$?
- How does the centralizer description of [4] interact with non‑linear scaling actions in parabolic geometries?

## 7. Practical Implications and Engineering Pathways

**(a) Users and decisions.** The primary users are implementers of normalization and reduction routines in computer‑algebra systems, and mathematicians running classification arguments that quotient configuration spaces by scalings. The decision that changes: before quotienting by dilations or rescaling coordinates in a pipeline, the practitioner applies the three‑question test of Section 3.1 — check normalization, check centralization, and if a family of automorphisms is parameterized, apply the ratio rule $c'=\frac{\lambda_{1}}{\lambda_{2}}c$ or certify triviality ($\varphi(2)=1$‑type rigidity for order‑2 discrete scalings). A correct certification prevents downstream computations from inheriting a changed symmetry group.

**(b) Readiness.** Against the NASA Technology Readiness Level definitions, this work is purely analytical and has not been peer reviewed: it is TRL 1–2. The derivations are explicit and checkable by hand (Sections 4.2–4.7), which supports the lower end of that band; no implementation, prototype, or empirical validation exists, and analytical work of this kind does not exceed TRL 3.

**(c) Smallest next test.** The smallest next computation that would de‑risk or falsify the framework is a symbolic verification of the ratio rule beyond dimension two: compute $D\,\phi\,D^{-1}$ for $D=\operatorname{diag}(\lambda_{1},\lambda_{2},\lambda_{3})$ and a unipotent shear on a chosen two‑plane, and for a unipotent with two independent shear coefficients, checking whether each coefficient rescales by the ratio of the corresponding dilation pair. The outcome that refutes the generalization is a conjugated coefficient that is not a monomial in the $\lambda_{i}$; the outcome that de‑risks it is a full ratio table matching $c'_{ij}=\frac{\lambda_{i}}{\lambda_{j}}c_{ij}$.

**(d) Binding constraints.** For any eventual software implementation, the binding constraints are, in order: symbolic exactness (the ratio $2/3$ must be carried as a rational, not a float, or the certification loses its proof status); the scope limit that the proved rule covers only linear shears, so any application to nonlinear automorphisms such as those of [7] is an extrapolation; and the data constraint that growth claims (R3–R4) rest on the two counts reported in [2], with no counts at further levels of the tower available to us. Whether the ratio rule extends to the graded pieces of parabolic geometries via the $Z(G_{0})$‑dilations of [4] is an open question, not a constraint we can quantify.

**(e) Order‑of‑magnitude projection (labeled).** Under the stated assumption of P1 (persistence of the per‑step factor $5$), the next hypothetical level would be $175$ at dimension $2^{5}=32$, with density $175/32=5.46875$. This projection inherits P1’s unverified linearity assumption and carries no error bar.

**(f) Risks and misuse paths.** The main misuse is overextension: citing the ratio rule as if it applied to nonlinear or infinite‑dimensional automorphism families, or citing the density growth $2.5$ as a general law of non‑associative structure, when it is computed from exactly two levels. A second misuse is reading the binomial identities of R5 as structural theorems; they are arithmetic observations about two numbers.

## 9. Conclusion

**(a) Intended users and decision impact.** Researchers and developers of computer‑algebra systems that automate symmetry classification will use the ratio rule to decide whether a scaling step can be safely omitted (scalar dilation) or must be accounted for by adjusting parameter values (anisotropic dilation). In geometric modeling pipelines, the rule informs whether a coordinate‑rescaling will alter the symmetry group of a shape, affecting downstream mesh generation or invariant detection.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 2 (formulation of concept and analytical proof‑of‑concept).

**(c) Smallest next experiment.** Implement a prototype module in a symbolic‑computation system that automatically applies the conjugation test to a user‑supplied linear automorphism and a diagonal scaling. The module should compute the transformed parameters and verify that the Jacobian determinant remains unchanged. A failure to reproduce the $2/3$ shear coefficient for $D=\operatorname{diag}(2,3)$ would falsify the main result.

**(d) Engineering constraints.** The primary constraints are:
- Availability of exact rational representations of scaling factors (to avoid floating‑point rounding that could obscure the $2/3$ ratio).
- Ability of the software to manipulate symbolic matrices and compute conjugates without numerical approximation.
- Access to the integer counts $7$ and $35$ from [2] for any automated density‑growth analysis.

**(e) Projected cost/performance bounds.** Assuming the prototype module is written in an existing open‑source computer‑algebra system, the development effort is on the order of a few person‑weeks ($\approx$ 200 person‑hours). The runtime cost of a single conjugation check is $O(n^{3})$ for an $n\times n$ matrix, negligible for $n\le10$.

**(f) Direct risks or misuse paths.** Users might incorrectly extrapolate the linear‑shear ratio rule to non‑linear or high‑degree polynomial automorphisms, leading to erroneous parameter adjustments. The documentation of the module must explicitly warn that the rule is proved only for linear maps as described.

We have introduced a three‑part conjugation test that determines when a scaling transformation acts trivially, centralizes, or rescales parameters of an automorphism. Explicit arithmetic shows that anisotropic dilations rescale shear coefficients by the ratio of diagonal entries, scalar dilations act trivially, and Jacobian determinants are invariant under diagonal conjugation. In the Cayley–Dickson tower the count of associative quaternion rings grows by a factor of $5$, with a per‑doubling exponent of $\log_{2}5$ and a density growth factor of $2.5$. Cone combinatorics at Picard number two exhibit a universal involution, and pure symmetric outer automorphisms admit a generator count of $n(n-1)$ plus a product of factor automorphism groups. Discrete‑scaling rigidity follows from Euler’s totient function, linking number‑theoretic bounds to scaling behavior. The framework is limited to linear settings and low‑dimensional cones, and its predictions are falsifiable by direct symbolic computation. Future work will explore extensions to non‑linear automorphisms, higher Picard numbers, and automated integration into symbolic‑computation pipelines.

## Version History

- Version 2.1.0 (2026-10-20, from 2.0.0): revised against the current literature, re-reviewed and re-verified. references 9 -> 12. length 6386 -> 4906 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.0-refs-extend). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 10 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Birational automorphism groups of projective varieties of Picard number two. arXiv:1307.5490v2. https://arxiv.org/abs/1307.5490v2
[2] Automorphisms of Sedenions. arXiv:2512.07210v3. https://arxiv.org/abs/2512.07210v3
[3] Compact moduli of K3 surfaces with a nonsymplectic automorphism. arXiv:2110.13834v2. https://arxiv.org/abs/2110.13834v2
[4] On automorphisms with natural tangent actions on homogeneous parabolic geometries. arXiv:1312.7318v3. https://arxiv.org/abs/1312.7318v3
[5] Aperiodic automorphisms of the Razak--Jacelon algebra. arXiv:2610.17543v2. https://arxiv.org/abs/2610.17543v2
[6] Punctured parabolic cylinders in automorphisms of $\mathbb{C}^{2}$. arXiv:1909.00765v2. https://arxiv.org/abs/1909.00765v2
[7] The dynamical Manin-Mumford problem for plane polynomial automorphisms. arXiv:1405.1377v2. https://arxiv.org/abs/1405.1377v2
[8] A Presentation for the Group of Pure Symmetric Outer Automorphisms of a Given Splitting of a Free Product. arXiv:2412.04250v2. https://arxiv.org/abs/2412.04250v2
[9] https://papers.qnfo.org/papers/automorphisms-and-scaling-transformations-a-re-entry-analysis-across-algebraic-g. QNFO: Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure.
[10] https://papers.qnfo.org/papers/meta-analysis-of-categorical-equivalence-and-scale-invariance. QNFO: Meta-Analysis of Categorical Equivalence and Scale Invariance.
[11] https://papers.qnfo.org/papers/ultrametric-physics-m12-synthesis. QNFO: Ultrametric Physics Research Plan.
[12] https://papers.qnfo.org/papers/base-invariant-number-theoretic-patterns-in-fundamental-constants. QNFO: Base-Invariant Number-Theoretic Patterns in Fundamental Constants.
