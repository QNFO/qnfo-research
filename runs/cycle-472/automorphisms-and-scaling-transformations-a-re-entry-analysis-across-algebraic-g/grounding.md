# Grounding block - source: rem-rev-e05f2312-b608-49c1-8607-834f35f998e5

## Research idea

Re-entry from 10.5281/zenodo.22758467: automorphisms relate to scaling transformations?

Post-publication revision of the published paper "Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure" (version 2.0.0). Write an improved version of the paper under revision: bring in the relevant work in the bibliography, especially newer work; strengthen the weakest arguments and derivations; correct every error; remove or qualify any claim the sources and derivations do not support; keep everything that is correct. The result is a complete paper, not a list of changes. The live version lists 9 references. Keep every reference you still rely on and add new ones; a revision that lists fewer than 7 references (70 percent of 9, rounded up) is rejected before publication, so drop a reference only when the claim it supports is removed or wrong.

Reported errors in the published version. Check each against the paper's own derivations and its sources; correct every one that holds and leave correct text unchanged:
1. The published text writes mathematical expressions as plain text outside $...$ delimiters, so the page renders raw symbols (render-health reports 3 defects for this page since 2026-10-14).

## Existing paper under revision (remediation only)

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


## Source material (fetched from arXiv)

(no arXiv source embedded in idea)

## Related literature (arXiv, real identifiers; full-text excerpts are in the Bibliography)

arXiv:1903.03080 | The conjugation action in completed group rings
arXiv:2003.06150 | The reciprocal character of the conjugation action
arXiv:1008.4086 | Invariant relationships deriving from classical scaling transformations
arXiv:2209.01897 | On the conjugation action for quantum general linear groups
arXiv:1110.1689 | Notes on partial conjugation
arXiv:patt-sol/9909001 | Approximate solutions and scaling transformations for quadratic solitons
arXiv:2110.01386 | Topological group actions by group automorphisms and Banach representations
arXiv:1506.01543 | A representation on the labeled rooted forests
arXiv:1109.1440 | Topological K-theory of the group C*-algebra of a semi-direct product Z^n rtimes Z/m for a free conjugation action
arXiv:2411.19512 | Topology-Preserving Scaling in Data Augmentation
arXiv:1209.0385 | Non-Associativity in the Clifford Bundle on the Parallelizable Torsion 7-Sphere

## QNFO corpus context (Vectorize)

QNFO: Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure | https://papers.qnfo.org/papers/automorphisms-and-scaling-transformations-a-re-entry-analysis-across-algebraic-g

## Bibliography (cite ONLY these; keep this exact order and numbering)

[1] arXiv:1903.03080 | The conjugation action in completed group rings
  Let $k = \mathbb{F}_p$ or $\mathbb{Z}_p$ (or finite extensions of these). Let $G$ be a $p$-valuable group, and form its completed group algebra $kG$. By analysing the conjugation action of $G$ on itself, we prove two structural results. Firstly, we show that all inner automorphisms of $kG$ that preserve $G$ are induced from inner automorphisms of $G$. Secondly, for a closed subgroup $Γ$ of $G$, we
  Full text (https://arxiv.org/html/1903.03080), excerpts of its own sections:
  § Introduction: Throughout this paper, $p$ will denote a fixed prime number, and $\mathbb{Z}_{p}$ will be the ring (or additive group) of $p$ -adic integers. Our main objects of study are the completed group rings $kG$ of compact $p$ -adic analytic groups $G$ over certain profinite rings $k$ (usually $\mathbb{F}_{p}$ or $\mathbb{Z}_{p}$ ). The rings $kG$ are often known as Iwasawa algebras in the literature, and play an important role in modern number theory. Compact $p$ -adic analytic groups (also known as compact $p$ -adic Lie groups) may be most simply defined as closed subgroups of the topological group $GL_{n}(\mathbb{Z}_{p})$ : see e.g. [ 6 , 13 ] for references. In studying these groups, it is common first to study a smaller subclass consisting of particularly nice groups: common choices include uniform [ 6 , §4] groups, or the slightly more general $p$ -valuable [ 13 , III, 3.1.6–7] groups. Both $p$ -valuable and uniform groups are torsion-free pro- $p$ groups of finite rank with well-behaved filtrations, which makes them easier to study. [...]
  § 0.1 Inner automorphisms: Our first results concern automorphisms of $kG$ . Theorem A. Let $G$ be a $p$ -valuable group, and let $\sigma$ be an automorphism of $kG$ that preserves the naturally embedded copy of $G$ . Then $\sigma$ is the (unique) extension of an inner automorphism of $G$ .∎ The importance of this result stems from an analysis of the behaviour of skew power series rings $R[[x;\sigma,\delta]]$ (see [ 21 , 15 , 28 ] for the definition and basic properties of these rings in the Iwasawa context). Forthcoming joint work of the current author and Adam Jones shows that the behaviour of $R[[x;\sigma,\delta]]$ varies depending on whether $\sigma$ is inner or outer. A similar dichotomy has also been observed in the world of skew polynomial rings $R[x;\sigma,\delta]$ , e.g. [ 14 , Theorem 3.6] . If $G$ is a $p$ -valuable group and $H$ is a closed normal subgroup such that $G/H\cong\mathbb{Z}_{p}$ , choose an arbitrary topological generator $gH$ for $\mathbb{Z}_{p}$ : that is, choose an element $g\in G$ such that $G=\overline{\langle H,g\rangle}$ . [...]
  § 0.2 Fixed rings: Next, we turn our attention to subrings of $kG$ fixed under the conjugation action of a closed subgroup $\Gamma\leq G$ . Theorem C. Let $G$ be a $p$ -valuable group, $\Gamma$ an arbitrary closed subgroup which we consider acting on $G$ by conjugation, and $H$ the centraliser in $G$ of $\Gamma$ . [...]
  § 2.2 The general result: Now let $G$ be a $p$ -valuable group. The argument below is an extension of a standard argument for finite $p$ -groups. Proof of Theorem A. $G$ contains a characteristic uniform open subgroup $N$ [ 6 , Corollary 4.3] , and so we may write $kG=kN*F$ (a crossed product in the sense of [ 17 ] ), where $F$ is a finite $p$ -group. Suppose that $\sigma$ is an inner automorphism of $kG$ which preserves $G$ , say there exists $a\in kG^{\times}$ such that $\sigma(r)=ara^{-1}$ for all $r\in kG$ . This time, a slightly different notation will be convenient. Let $T$ be a transversal to $N$ in $G$ , and for each $x\in G$ , write $n_{x}$ and $t_{x}$ for the unique elements $n_{x}\in N$ and $t_{x}\in T$ satisfying $n_{x}t_{x}=x$ . We will also index the coefficients of $a$ using the cosets, i.e. we will write $a=\sum_{x\in T}a_{xN}\cdot x,$ for some coefficients $a_{xN}\in kN$ . In particular, if $T^{\prime}$ is any (perhaps different) transversal, we still have $a=\sum_{x\in T}a_{xN}\cdot t_{x}=\sum_{y\in T^{\prime}}a_{yN}\cdot t_{y}. [...]
[2] arXiv:2003.06150 | The reciprocal character of the conjugation action
  For a finite group $G$ we investigate the smallest positive integer $e(G)$ such that the map sending $g\in G$ to $e(G)|G:C_G(g)|$ is a generalized character of $G$. It turns out that $e(G)$ is strongly influenced by local data, but behaves irregularly for non-abelian simple groups. We interpret $e(G)$ as an elementary divisor of a certain non-negative integral matrix related to the character table
  Full text (https://arxiv.org/html/2003.06150), excerpts of its own sections:
  § 1 Introduction: The conjugation action of a finite group $G$ on itself determines a permutation character $\pi$ such that $\pi(g)=|\mathrm{C}_{G}(g)|$ for $g\in G$ . Many authors have studied the decomposition of $\pi$ into irreducible complex characters (see [ 1 , 2 , 4 , 5 , 6 , 7 , 10 , 15 , 16 , 17 ] ). In the present paper we study the reciprocal class function $\tilde{\pi}$ defined by $\tilde{\pi}(g)\mathrel{\mathop{\mathchar 58\relax}}=|\mathrm{C}_{G}(g)|^{-1}$ for $g\in G$ . By a result of Knörr (see [ 12 , Problem 1.3(c)] or Proposition 1 below), there exists a positive integer $m$ such that $m\tilde{\pi}$ is a generalized character of $G$ . Since $\pi(1)=|G|$ , it is obvious that $|G|$ divides $m$ . If also $n\tilde{\pi}$ is a generalized character, then so is $\gcd(m,n)\tilde{\pi}$ by Euclidean division. We investigate the smallest positive integer $e(G)$ such that $e(G)|G|\tilde{\pi}$ is a generalized character. [...]
  § 2 Ordinary characters: Our notation follows mostly Navarro’s books [ 11 , 12 ] . In particular, the set of algebraic integers in $\mathbb{C}$ is denoted by $\mathbf{R}$ . The set of $p$ -elements (resp. $p^{\prime}$ -elements) of $G$ is denoted by $G_{p}$ (resp. $G_{p^{\prime}}$ , deviating from [ 11 ] ). The usual scalar product of class functions $\chi$ , $\psi$ of $G$ is denoted by $[\chi,\psi]=\frac{1}{|G|}\sum_{g\in G}\chi(g)\overline{\psi(g)}$ . For any real generalized character $\rho$ and any $\chi\in\operatorname{Irr}(G)$ we will often use the fact $[\rho,\chi]=[\rho,\overline{\chi}]$ without further reference. Proposition 1 . For every finite group $G$ the following holds: (i) $e(G)$ divides $|G\mathrel{\mathop{\mathchar 58\relax}}\mathrm{Z}(G)|$ . In particular, $e^{\prime}(G)$ is an integer divisible by $|\mathrm{Z}(G)|$ . (ii) If $|G|$ is even, so is $e^{\prime}(G)$ . Proof. (i) Let $Z\mathrel{\mathop{\mathchar 58\relax}}=\mathrm{Z}(G)$ . We need to check that $|G||G\mathrel{\mathop{\mathchar 58\relax}}Z|[\tilde{\pi},\chi]$ is an integer for every $\chi\in\operatorname{Irr}(G)$ . [...]
  § 3 Examples: Proposition 9 . There exist non-trivial groups $G$ such that $e^{\prime}(G)=1$ . Proof. By Proposition 1 and Theorem 5 we need a group of odd order such that $\mathrm{Z}(G/\mathrm{O}_{p^{\prime}}(G))=1$ for every prime $p$ . Let $A\mathrel{\mathop{\mathchar 58\relax}}=\langle a_{1},\ldots,a_{4}\rangle\cong C_{9}^{4}$ , $B\mathrel{\mathop{\mathchar 58\relax}}=\langle b_{1},b_{2}\rangle\cong C_{25}^{2}$ and $C\mathrel{\mathop{\mathchar 58\relax}}=\langle c\rangle\cong C_{15}$ . We define an action of $C$ on $A\times B$ via $\displaystyle a_{1}^{c}$ $\displaystyle=a_{2}^{4},$ $\displaystyle a_{2}^{c}$ $\displaystyle=a_{3}^{4},$ $\displaystyle a_{3}^{c}$ $\displaystyle=a_{4}^{4},$ $\displaystyle a_{4}^{c}$ $\displaystyle=(a_{1}a_{2}a_{3}a_{4})^{-4},$ $\displaystyle b_{1}^{c}$ $\displaystyle=b_{2}^{6},$ $\displaystyle b_{2}^{c}$ $\displaystyle=(b_{1}b_{2})^{-6}.$ Note that the action of $c$ on $A$ is the composition of the companion matrix of $X^{4}+X^{3}+X^{2}+X+1$ and the power map $a\mapsto a^{4}$ . In particular, $c^{5}$ induces an automorphism of order $3$ on $A$ . [...]
  § 4 Brauer characters: For a given prime $p$ , the restriction of our permutation character $\pi$ to the set of $p^{\prime}$ -elements $G_{p^{\prime}}$ yields a Brauer character $\pi^{0}$ of $G$ . Since $e(G)|G|\tilde{\pi}$ is a generalized character, there exists a smallest positive integer $f_{p}(G)$ such that $f_{p}(G)|G|\tilde{\pi}^{0}$ is a generalized Brauer character of $G$ . Clearly, $f_{p}(G)$ divides $e(G)$ . [...]
[3] arXiv:1008.4086 | Invariant relationships deriving from classical scaling transformations
  Because scaling symmetries of the Euler-Lagrange equations are generally not variational symmetries of the action, they do not lead to conservation laws. Instead, an extension of Noether's theorem reduces the equations of motion to evolutionary laws that prove useful, even if the transformations are not generalized symmetries of the equations of motion. In the case of scaling, symmetry leads to a 
  Full text (https://arxiv.org/html/1008.4086), excerpts of its own sections:
  § I SCALING SYMMETRY NOT GENERALLY A SYMMETRY OF THE ACTION: Action principles dominate physical theories because they admit transformations among dynamical variables and exhibit common structural analogies across different systems. If these transformations are symmetries of the action, then by Noether’s theorem, they give rise to conservations laws that reduce the number of degrees of freedom. This relationship between symmetries of the action (variational symmetries) and conservation laws is central to Lagrangian dynamics. But, even if these transformations are not symmetries of the action, they nonetheless lead to useful Noether’s identities . Although equations of motion do not require Lagrangian expression, we apply this identity to transformations that are not variational symmetries; in particular, to scaling symmetry, which is generally a generalized symmetry only of the equations of motion (Section II). Variational symmetries and generalized symmetries both reduce the equations of motion to first order, but in different ways: $\bullet$ Variational symmetries imply conservation laws , first integrals of the equations of motion. [...]
  § II.1 Noether’s Identity Implies Either Conservation Laws or Evolutionary Equations: We start with a system of particles described by the Lagrangian $\mathcal{L}(t,q_{i},\dot{q_{i}})$ and action $S=\int{\mathcal{L}(t,q_{i},\dot{q_{i}})}dt$ , where the dot designates the partial derivative $\partial/\partial t$ with respect to the independent variable and the Einstein summation convention is assumed. Under an infinitesimal point transformation $\delta(t,q_{i}),\delta q_{j}(t,q_{i})$ generated by $\delta t\cdot\partial/\partial t+\delta q_{i}\cdot\partial/\partial q_{i}$ , velocities and Lagrangian transform locally as $\displaystyle\delta\dot{q_{i}}=\frac{d\delta q_{i}}{dt}-\dot{q_{i}}\frac{d\delta t}{dt}\quad,$ $\displaystyle\delta\mathcal{L}=[\delta t\cdot\partial/\partial t+\delta q_{i}\cdot\partial/\partial q_{i}+\delta\dot{q_{i}}\cdot\partial/\partial\dot{q_{i}}]\mathcal{L}=\dot{\mathcal{L}}\delta t+(\partial\mathcal{L}/\partial q_{i})\delta q_{i}+(\partial\mathcal{L}/\partial\dot{q_{i}})\Bigl[\frac{d\delta q_{i}}{dt}-\dot{q_{i}}\frac{d\delta t}{dt}\Bigr]\quad,$ (1) where $d/dt\equiv\partial/\partial t+\dot{q_{i}}\cdot\partial/\partial [...]
  § V CONCLUSIONS: We have extended Noether’s Equation connecting variational symmetries to conservation laws to generalized transformations of the Euler-Lagrange equations. The resultant evolutionary equations are useful, even when the transformations are not generalized symmetries. But, when they are generalized symmetries, they reduce the Euler-Lagrange equations to first-order equations between invariants. For scaling symmetries, the evolutionary equation takes a special form connecting linearly the kinematic and dynamic parts of the Lagrangian. For nonrelativistic systems with inverse-power law potentials, the scaling evolutionary equation is a generalized virial law, linearly relating the kinetic and potential energies. For hydrostatic systems obeying barotropic equations of state, the scaling analogous evolutionary equation is a linear relation between the local gravitational and internal energies. From this scaling evolutionary equation, in the following article  [ 1 ] , we derive all the properties of polytropes.
[4] arXiv:2209.01897 | On the conjugation action for quantum general linear groups
  We consider the conjugation action of a quantum group over an arbitrary field. In particular we consider the coordinate algebra of a quantised general linear group G(n), at an arbitrary nonzero parameter q, and give analogues of results of Kostant and Richardson
  Full text (https://arxiv.org/html/2209.01897), excerpts of its own sections:
  § 1 Introduction: Domokos and Lenagan, [ 6 ] , show that the algebra of polynomial invariants for the conjugation action of a quantum general linear group on quantum matrices of degree $n$ , over a field of characteristic $0$ at parameter $q$ not a root of unity, is a commutative polynomial algebra in $n$ variables. Further results are given in [ 7 ] . We consider this situation and also other aspects of the conjugation representation of a quantum linear group, as constructed in [ 5 ] . We prove that the algebra of polynomial invariants, for arbitrary $k$ and $0\neq q\in k$ , is a commutative polynomial algebra. We consider the full algebra of invariants $C(G)$ of the coordinate algebra of a quantum general linear group $G$ and describe, Theorem 7.4, a $(C(G),G)$ -module filtration of the coordinate algebra $k[G]$ . This is an analogue of the main result of [ 13 ] (which is itself an analogue of results of Richardson, [ 27 , Theorem A] and Kostant, [ 24 , Theorem 0.13] ). [...]
  § 2 Constrained algebras: Let $k$ be a field. We write $\dim_{k}V$ , or simply $\dim V$ , for the dimension of a finite dimensional vector space $V$ over $k$ . Let $S$ be a finite dimensional $k$ -algebra which we assume to be split (or Schurian), i.e., that ${\rm End}_{S}(L)=k$ , for every simple $S$ -module $L$ . We write ${\rm{mod}}(S)$ for the category of finite dimensional left $S$ -modules and write $V\in{\rm{mod}}(S)$ to indicate that $V$ is a finite dimensional left $S$ -module. An $S$ -module will be assumed to be a left module and finite dimensional if no other indication is given. We write $J(S)$ for the Jacobson radical of $S$ and write $[S,S]$ for the $k$ -span of all commutators $[x,y]=xy-yx$ , $x,y\in S$ . Definition 2.1 . We say that $S$ is (radically) constrained if $J(S)\subseteq[S,S]$ . Note that if $S$ is a constrained algebra and $I$ is an ideal of $S$ then $J(S/I)=(J(S)+I)/I\subseteq([S,S]+I)/I=[S/I,S/I]$ and so: (1)  A factor algebra of a constrained algebra is constrained. We write $V^{*}$ for the linear dual of a vector space $V$ . [...]
  § 3 Relative Constraint: We now consider a relative version of constraint. Let $R$ be a subalgebra of the finite dimensional split $k$ -algebra $S$ . We define $C(S,R)$ to be the subspace of the linear dual $S^{*}$ of $S$ consisting of all elements $f$ such that $f(rs)=f(sr)$ , for all $r\in R$ , $s\in S$ . Thus $C(S,R)$ consists of all elements that vanish on the space $[R,S]$ , spanned by all commutators $rs-sr$ , $r\in R$ , $s\in S$ , and $\dim C(S,R)=\dim\,(S/[R,S])^{*}=\dim H_{0}(R,S).$ Some of the elements of $C(S,R)$ may be accounted for representation theoretically (analogously to the trace functions on $S$ considered in Section 2) in the following way. Let $V$ be a finite dimensional left $S$ -module affording the representation $\rho:S\to{\rm End}_{k}(V)$ and let $\theta$ be an element of ${\rm End}_{R}(V)$ . We write $\chi_{\theta}$ or $\chi_{\theta,V}$ for the “twisted trace function”, i.e., the element of $S^{*}$ defined by $\chi_{\theta}(s)={\rm trace}(\theta\rho(s))$ , $s\in S$ . It follows from the fact that $\theta$ commutes with the action of $R$ that $\chi_{\theta}\in C(S,R)$ . [...]
  § 4 Quasi-hereditary algebras: Let $S$ be finite dimensional algebra over the field $k$ . By abuse of notation we shall use the expression “ $S$ is a quasi-hereditary algebra” to indicate that, with respect to some labelling $L(\lambda)$ , $\lambda\in\Lambda$ , of a complete set of pairwise inequivalent irreducible left $S$ -modules, and some partial order $\leq$ on $\Lambda$ , the category of finite [...]
[5] arXiv:1110.1689 | Notes on partial conjugation
  In this notes, we will give an exposition of some results on the method of partial conjugation action. We first discuss the partial conjugation action of a parabolic subgroup of a Coxeter group. We then discuss some applications to Lusztig's $G$-stable pieces and its affine generalization. We also discuss some recent work on the $\s$-conjugacy classes of loop groups and affine Deligne-Lusztig vari
  Full text (https://arxiv.org/html/1110.1689), excerpts of its own sections:
  § Introduction: Let $G$ be a connected reductive algebraic group over an algebraically closed field $\Bbbk$ . Let $X$ be a “nice” $G\times G$ -variety (e.g., a wonderful compactification of an adjoint group). In [ L1 ] , Lusztig introduced a partition of $X$ into finitely many locally closed subvarieties, which are stable under the diagonal $G$ -action. These subvarieties are called $G$ -stable pieces. Each $G$ -stable pieces is a union of orbits for the diagonal action of $G$ and there is a natural bijection between these $G$ -orbits and twisted conjugacy classes of a Levi factor of $G$ . The partition of $X$ into $G$ -stable pieces is central to Lusztig’s work on parabolic character sheaves and the work of Evens and Lu [ EL ] on Poisson geometry. More recently, Pink, Wedhorn and Ziegler [ PWZ ] used $G$ -stable pieces to study some problems in arithmetic algebraic geometry. The notion of $G$ -stable pieces is relative new and a little hard to penetrate as the statements are fairly technical. [...]
  § 1.1.: We first recall the definition of Coxeter groups. Let $S$ be a finite set and $(m_{ij})_{i,j\in S}$ be a matrix with entries in $\mathbb{N}\cup\{\infty\}$ such that $m_{ii}=1$ and $m_{ij}=m_{ji}\geqslant 2$ for all $i\neq j$ . Let $W$ be a group defined by the generators $s_{i}$ for $i\in I$ and the relations $(s_{i}s_{j})^{m_{ij}}=1$ for $i,j\in I$ with $m_{ij} Coxeter group . Sometimes we just call $W$ itself a Coxeter group. We denote by $\ell$ the length function and $\leqslant$ the Bruhat order. For $J\subset S$ , we denote by $W_{J}$ the standard parabolic subgroup of $W$ generated by $J$ and by $W^{J}$ (resp. ${}^{J}W$ ) the set of minimal coset representatives in $W/W_{J}$ (resp. $W_{J}\backslash W$ ). For $J,K\subset I$ , we simply write $W^{J}\cap{}^{K}W$ as ${}^{K}W^{J}$ .
  § 1.2.: Let $J,J^{\prime}\subset S$ and $\delta:W_{J}\to W_{J^{\prime}}$ such that $\delta(J)=J^{\prime}$ . Now we consider the $\delta$ -twisted partial conjugation of $W_{J}$ on $W$ defined by $w\cdot_{\delta}w^{\prime}=\delta(w)w^{\prime}w^{-1}.$ If $J=J^{\prime}$ and $\delta$ is the identity map, then we simply write $\cdot$ for $\cdot_{\delta}$ . For any subset $V$ of $W$ , we set $W_{J}\cdot_{\delta}V=\{\delta(w)w^{\prime}w^{-1};w\in W_{J},w^{\prime}\in V\}.$ The classification of $W_{J}$ -orbits on $W$ for this twisted partial conjugation action is as follows. See [ H3 , Section 2] . Theorem 1.1 . For any $w\in W^{J}$ , set $I(J,w,\delta)=\max\{K\subset J;\forall k\in K,\exists k^{\prime}\in\delta(K),ws_{k}=s_{k^{\prime}}w\}.$ Then (1) $W=\sqcup_{w\in W^{J}}W_{J}\cdot_{\delta}(wW_{I(J,w,\delta)})$ . (2) The inclusion $W_{I(J,w,\delta)}\to W_{J}\cdot_{\delta}(wW_{I(J,w,\delta)})$ induces a natural bijection between the $\text{\rm Ad}(w)^{-1}\circ\delta$ -twisted conjugacy classes on $W_{I(J,w,\delta)}$ and the $W_{J}$ -orbits on $W_{J}\cdot_{\delta}(wW_{I(J,w,\delta)})$ . [...]
  § 1.3.: In particular, we have a map $\pi_{J,\delta}:W\to W^{J},W_{J}\cdot_{\delta}(wW_{I(J,w,\delta)})\mapsto w$ that is constant on each orbit for the $\delta$ -twisted partial conjugation action of $W_{J}$ . Below are two examples. Here red color for the elements in $W^{J}$ and blue color for the elements in $W_{J}$ . Example 1.2 . $W=S_{4}$ , $J=J^{\prime}=\{1,2\}$ and $\delta$ is the identity map. The image of $w=s_{2}s_{3}s_{2}s_{1}s_{2}$ is obtained as follows. $\displaystyle{\color[rgb]{1,0,0}s_{2}s_{3}}{\color[rgb]{0,0,1}s_{2}s_{1}s_{2}}$ $\displaystyle\xrightarrow{\text{ conj. [...]
[6] arXiv:patt-sol/9909001 | Approximate solutions and scaling transformations for quadratic solitons
  We study quadratic solitons supported by two- and three-wave parametric interactions in chi-2 nonlinear media. Both planar and two-dimensional cases are considered. We obtain very accurate, 'almost exact', explicit analytical solutions, matching the actual bright soliton profiles, with the help of a specially-developed approach, based on analysis of the scaling properties. Additionally, we use the
  Full text (https://arxiv.org/html/patt-sol/9909001), excerpts of its own sections:
  § I Introduction: One of the rapidly expanding areas of research is the physics of solitons – wave packets, or self-trapped beams, that propagate with their profiles remaining undistorted. In particular, parametric solitons , composed of mutually trapped fundamental and harmonic waves, attract interest of researchers due to a wide range of possible applications. In optics, for example, such solitons were observed in media with quadratic (or $\chi^{(2)}$ ) nonlinearity, and their unique features can be utilized for the creation of all-optical information processing devices [ 1 ] . In general, parametric solitons may form in different media which possess resonant quadratic nonlinearities, such as plasma, organic superlattices [ 2 ] , Bose-Einstein condensate [ 3 ] , etc. Many papers have been devoted to a theoretical analysis of quadratic solitons [ 4 ] . It was shown that bright solitons can be stable, and hence are of most interest for practical applications, on the other hand parametric dark solitons often exhibit modulation instability. [...]
  § II.1.1 Basic equations and their properties: Parametric interaction between the fundamental frequency (FF) wave and its second harmonic (SH) in the (1+1) dimensional case can be described by a set of coupled equations for slowly varying complex amplitudes of the wave packets [ 7 ] (see also [ 4 , 8 ] ). [...]
  § II.1.5 Comparison with numerical results: In order to determine deviations between the approximate and exact solutions, we solved Eqs. ( 3 ) numerically. The corresponding dependencies of the peak amplitudes, total power, and Hamiltonian on the detuning parameter $\alpha$ are presented in Fig.  2 (left graphs) for the case of spatial solitons ( $\sigma=2$ ). As a matter of fact, the numerical and analytical results on these plots are not distinguishable , and that is why we show them differently, by continuous curves and asterisks. Plots on the right give corresponding relative deviations with solid lines, and dashed lines demonstrate the errors for the variational solution with Gaussian profiles (SGP) [ 16 , 17 ] . We see that the analytical solution ( 13 )-( 14 ) describes the key soliton parameters extremely accurately . In a wide region of mismatch values, $\alpha>1$ , the relative errors are smaller than 0.7% for the total power, and 0.3% for other characteristics. [...]
  § IV Concluding remarks: We have studied the properties of two- and three-component quadratic bright solitons in planar waveguides and in bulk media. Very accurate, yet simple and compact, approximate solutions have been derived to describe the actual wave profiles, with a precision which the previously-known approximations could not achieve. Such amazingly good results have been obtained because the trial functions were chosen to correspond to the scaling properties of the solitons. With the help of a specially-developed approach, the optimal values of fitting parameters have been found in a simple explicit form, which wouldn’t be possible with the variational method. In particular, an ’almost exact’ solution has been derived which describes a whole family of two-wave planar solitons , accounting for all the key properties. It not only provides perfect estimations for integral characteristics (power and Hamiltonian), but also closely matches the envelope profiles of both components for any mismatch. [...]
[7] arXiv:2110.01386 | Topological group actions by group automorphisms and Banach representations
  We study Banach representability for actions of topological groups on groups by automorphisms (in particular, actions of groups on itself by conjugations). Every such action is Banach representable on some Banach space. The natural question is to examine when we can find representations on low complexity Banach spaces. In contrast to the standard left action of a locally compact second countable g
  Full text (https://arxiv.org/html/2110.01386), excerpts of its own sections:
  § 1.1. Main question: To every Banach space $V$ one may associate the topological group $\operatorname{Iso}(V)$ of linear isometries (in its strong operator topology) and its canonical dual action on the weak-star compact unit ball $B_{V^{*}}$ of the dual Banach space $V^{*}$ . The main idea of the present work is to study which actions $G\times X\to X$ by automorphisms on topological groups $X$ can be obtained as a “subaction” of $\operatorname{Iso}(V)\times B_{V^{*}}\to B_{V^{*}}$ Question 1.1 . Which actions of a topological group $G$ on a topological group $X$ by group automorphisms can be represented on low complexity Banach spaces $V$ (e.g., Hilbert, reflexive, Asplund, Rosenthal)? In particular, what about the actions of groups on itself by conjugations? This is a particular case of a question about general actions which leads to an interesting hierarchy of topological groups and their actions. For some concrete results in this direction we refer to [ 23 , 24 , 8 , 9 , 10 , 11 , 15 , 12 ] .
  § 1.2. Preliminaries: All topological spaces are assumed to be Tychonoff. $X$ is a $G$ - space will mean that we have a continuous action $G\times X\to X$ of a topological group $G$ on a topological space $X$ . The dual $V^{*}$ of a Banach space $V$ is the Banach space of all continuous linear functionals on $V$ . Remark 1.2 . The topological group $G:=\operatorname{Iso}(V)$ of linear isometries acts naturally on the dual space $V^{*}$ as follows: $\operatorname{Iso}(V)\times V^{*}\to V^{*},\ \ ((gu^{*})(v)=u^{*}(g^{-1}v))\ \ \ g\in G,v\in V,u^{*}\in V^{*}.$ Moreover, the induced action on every norm bounded $G$ -invariant subset $Y$ of $V^{*}$ (e.g., on the unit ball $B_{V^{*}}$ of $V^{*}$ ) is continuous where $Y$ is endowed with the weak-star topology. Definition 1.3 . [ 23 , 10 ] A representation of a $G$ -space $X$ on a Banach space $V$ is an equivariant continuous pair $(h,\alpha)$ , where $h\colon G\to\operatorname{Iso}(V)$ is a continuous homomorphism and $\alpha\colon X\to V^{*}$ is a weak-star continuous bounded $G$ -equivariant map. [...]
  § 1.3. Main results and some open questions: It is a less known fact (see [ 21 , 22 ] ) that the $G$ -space $G_{c}$ (conjugation action) is Banach representable (in the sense of Definition 1.3 ) for every topological group $G$ . By Fact 1.4 , it is equivalent to say that $G_{c}$ is $G$ -compactifiable. More precisely, the Roelcke compactification is a (proper) $G$ -compactification of $G_{c}$ (Corollary 2.3 ). The significance of Roelcke compactification is now well understood due to several papers of V. Uspenskij [ 37 , 36 ] and many other authors. In contrast to the standard left action of a locally compact second countable group $G$ on itself, the conjugation action need not be reflexively representable even for natural matrix groups. This happens among others for the special linear group $\operatorname{SL}_{2}({\mathbb{R}})$ ; see Theorem 3.3 which uses Grothendieck’s double limit criterion . Moreover, by Theorem 3.10 the $G$ -space $G_{c}$ for $G:=\operatorname{SL}_{n}({\mathbb{R}})$ is not Asplund representable for every $n\geq 4$ . Here we use the weak mixing argument by S.G. Dani and S. [...]
  § Compactifiability: Let $\alpha\colon G\times X\to X$ be a continuous action of a topological group $G$ on $X$ . A topologically compatible uniform structure ${\mathcal{U}}$ on $X$ is said to be bounded (see [ 3 , 38 , 39 , 30 ] ) if for every entourage ${\varepsilon}\in{\mathcal{U}}$ there exists a neighbourhood $U\in N_{e}(G)$ such that $(x,ux)\in{\varepsilon}$ for every $u\in U$ and every $x\in [...]
[8] arXiv:1506.01543 | A representation on the labeled rooted forests
  We consider conjugation action of symmetric group on the semigroup of all partial functions and develop a machinery to investigate character formulas and multiplicities. In particular, we determine nilpotent matrices whose orbit under symmetric group afford the sign representation. Applications to rook theory are offered.
  Full text (https://arxiv.org/html/1506.01543), excerpts of its own sections:
  § 1 Introduction: Our goal in this paper is to contribute to the general field of combinatorial representation theory by using some ideas from semigroup theory, rook theory, as well as graph theory. Classical rook theory is concerned with the enumerative properties of file and rook numbers in relation with other objects of mathematics [ 3 ] . In particular, enumeration of functions satisfying various constraints falls into the scope of rook theory. Here, we focus on partial functions , also known as partial transformations, on $[n]:=\{1,\dots,n\}$ with the property that the associated graph of the function is a labeled rooted forest. There is an obvious associative product on the set of all partial transformations on $[n]$ ; the composition $f\circ g$ of two partial transformations $f$ and $g$ is defined when the domain of $f$ intersects the range of $g$ . The underlying semigroup, denoted by $\mathcal{P}_{n}$ is called the partial transformation semigroup [ 6 ] . Of course, the identity map on $[n]$ is a partial transformation whence $\mathcal{P}_{n}$ is a monoid. [...]
  § 2.1 Terminology of forests: A rooted tree $\sigma$ is a finite collection of vertices such that there exists a designated vertex, called the root (or the ancestor ), and the remaining vertices are partitioned into a finite set of disjoint non-empty subsets $\sigma_{1},\dots,\sigma_{m}$ , each of which is a tree itself. We depict a tree by putting its root at the top so that the following terminology is logical: if a vertex $a$ is connected by an edge to another vertex $b$ that is directly above $a$ , then $a$ is called a child of $b$ . Any collection of rooted trees is called a rooted forest. In particular, a tree is a forest. The elements of the set $[n]=\{1,\dots,n\}$ are often referred to as labels . Cayley’s theorem states that there are $n^{n-1}$ labeled rooted trees on $n$ vertices. Since adding a new vertex to a forest on $n$ vertices results in a tree on $n+1$ vertices (by connecting the roots to the new vertex), and vice versa, Cayley’s theorem is equivalent to the statement that there are $(n+1)^{n-1}$ labeled rooted forests on $n$ vertices.
  § 2.2 Basic character theory: It is well-known that the irreducible representations of $S_{n}$ are indexed by partitions of $n$ . If $\lambda$ is a partition of $n$ (so we write $\lambda\vdash n$ ), then the corresponding irreducible representation is denoted by $V_{\lambda}$ . Let $R^{0}$ denote the ring of integers ${\mathbb{Z}}$ and let $R^{n}$ , $n=1,2,\dots$ denote the ${\mathbb{Z}}$ -module spanned by irreducible characters of $S_{n}$ . We set $R=\bigoplus_{n\geq 0}R^{n}$ . In a similar fashion, let $\Lambda$ denote the direct sum $\bigoplus_{n\geq 0}\Lambda^{n}$ , where $\Lambda^{n}$ is the ${\mathbb{Z}}$ -module spanned by homogenous symmetric functions of degree $n$ , and $\Lambda^{0}={\mathbb{Z}}$ . Both of these ${\mathbb{Z}}$ -modules are in fact ${\mathbb{Z}}$ -algebras, and the Frobenius characteristic map $R\ni\chi\mapsto\text{ch}(\chi)=\sum_{\rho\vdash n}z_{\rho}^{-1}\chi_{\rho}p_{\rho}\in\Lambda$ is a ${\mathbb{Z}}$ -algebra isomorphism. [...]
  § 2.3 Symmetric functions and plethysm: The plethysm of the Schur functions $s_{\lambda}\circ s_{\mu}$ is the symmetric function obtained from $s_{\lambda}$ by substituting the monomials of $s_{\mu}$ for the variables of $s_{\lambda}$ . To spell this out more precisely we follow [ 20 ] . The plethysm operator on symmetric functions is the unique map $\circ:\ \Lambda\times\Lambda\rightarrow\Lambda$ satisfying the following three axioms: P1. [...]
[9] arXiv:1109.1440 | Topological K-theory of the group C*-algebra of a semi-direct product Z^n rtimes Z/m for a free conjugation action
  We compute the topological K-theory of the group C*-algebra C*_r(G) for a group extension Z^n-&gt;G-&gt;Z/m provided that the conjugation action of Z/m on Z^n is free outside the origin.
  Full text (https://arxiv.org/html/1109.1440), excerpts of its own sections:
  § Introduction: Throughout this paper let $1\to\mathbb{Z}^{n}\to\Gamma\to\mathbb{Z}/m\to 1$ be a group extension such that conjugation action of $\mathbb{Z}/m$ on $\mathbb{Z}^{n}$ is free outside the origin. Our main goal is to compute the topological $K$ -theory of the group $C^{*}$ -algebra $C^{*}_{r}(\Gamma)$ . This generalizes results of Davis-Lück  [ 7 ] , where $m$ was assumed to be a prime. Except ideas from that paper, the proof of a Conjecture due to Adem-Ge-Pan-Petrosyan in Langer-Lück  [ 11 ] is a key ingredient. The calculation and its result are surprisingly complicated. It will play an important role in a forthcoming paper by Li-Lück  [ 12 ] . There the computation of the topological $K$ -theory of a $C^{*}$ -algebra associated to the ring of integers in an algebraic number field will be carried out in general, thus generalizing the work of Cuntz and Li  [ 6 ] who had to assume that $+1$ and $-1$ are the only roots of unity.
  § 0.1. Main Result: Our main result is the following theorem. In the sequel $C^{*}_{r}(G)$ is the reduced group $C^{*}$ -algebra of a group $G$ . We denote by $\underline{E}G$ the classifying space of proper actions of a group $G$ and by $\underline{B}G$ its quotient space $G\backslash\underline{E}G$ . Let $\widehat{H}^{*}(G;M)$ be the Tate cohomology of a group $G$ with coefficients in a $\mathbb{Z}G$ -module $M$ . Denote by $\Lambda^{i}\mathbb{Z}^{n}$ the $i$ -th exterior power. Theorem 0.1 (Computation of the topological $K$ -theory) . Consider the extension of groups $1\to\mathbb{Z}^{n}\to\Gamma\to\mathbb{Z}/m\to 1$ such that the conjugation action of $\mathbb{Z}/m$ on $\mathbb{Z}^{n}$ is free outside the origin $0\in\mathbb{Z}^{n}$ . Let $\mathcal{M}$ be the set of conjugacy classes of maximal finite subgroups of $\Gamma$ . (i) We obtain an isomorphism $\omega_{1}\colon K_{1}(C^{*}_{r}(\Gamma))\xrightarrow{\cong}K_{1}(\underline{B}\Gamma). [...]
  § 0.2. Organization of the paper: We will compute $K_{*}(C^{*}_{r}(G))$ in a more general setting in Section  1 , where we consider groups $G$ for which each non-trivial finite subgroup is contained in a unique maximal finite subgroup. In Section  2 we consider the special case where we additionally assume that the normalizer of every maximal finite subgroup is the maximal finite subgroup itself. The groups $\Gamma$ appearing in Theorem  0.1 will satisfy this assumption. In Sections  3 and  4 we deal with the cohomology and the topological $K$ -theory of the spaces $B\Gamma$ and $\underline{B}\Gamma$ , and, finally complete the proof of Theorem  0.1 . The rest of the paper is devoted to the computation of the numbers $s_{i}$ appearing in Theorem  0.1 . Recall that $\mathbb{Z}^{n}$ becomes a $\mathbb{Z}[\mathbb{Z}/m]$ -module by the conjugation action. Sometimes we write $\mathbb{Z}^{n}_{\rho}$ instead of $\mathbb{Z}^{n}$ to emphasize the $\mathbb{Z}[\mathbb{Z}/m]$ -module structure. [...]
  § 0.3. $m$ is a prime: Suppose that $m=p$ for a prime number $p$ . We have $\mathbb{Z}^{n}_{\rho}\otimes_{\mathbb{Z}}\mathbb{Q}\cong_{\mathbb{Q}[\mathbb{Z}/p]}\mathbb{Q}[\zeta_{p}]^{k}$ for $\zeta_{p}=\exp(2\pi i/p)$ and some natural number $k$ . The natural number $k$ is determined by the property $n=(p-1)\cdot k$ . All non-trivial finite subgroups of $\Gamma$ are cyclic of order $p$ and are maximal finite. [...]
  § 0.4. $m$ is a prime power $p^{r}$ for $r\geq 2$: Next we consider the case, where $m$ is a prime power, let us say $m=p^{r}$ . Since we have treated the case $r=1$ already in Example  0.3 , we will assume in the sequel $r\geq 2$ . [...]
[10] arXiv:2411.19512 | Topology-Preserving Scaling in Data Augmentation
  We propose an algorithmic framework for dataset normalization in data augmentation pipelines that preserves topological stability under non-uniform scaling transformations. Given a finite metric space \( X \subset \mathbb{R}^n \) with Euclidean distance \( d_X \), we consider scaling transformations defined by scaling factors \( s_1, s_2, \ldots, s_n &gt; 0 \). Specifically, we define a scaling fu
  Full text (https://arxiv.org/html/2411.19512), excerpts of its own sections:
  § 4.3 Theorem 1 (Stability of Persistence Diagrams Under Scaling): The bottleneck distance between the persistence diagrams $D$ and $D_{S}$ satisfies: $d_{B}(D,D_{S})\leq\delta=\delta^{\prime}\cdot\operatorname{diam}(X)=(s_{\max}-s_{\min})\cdot\operatorname{diam}(X).$ This demonstrates that $d_{B}(D,D_{S})\leq\delta=\Delta_{s}\cdot\operatorname{diam}(X)$ . The result establishes a direct relationship between $\Delta_{s}$ and topological stability under bottleneck distance. It links metric bounds to persistence diagrams. Proof. Our goal is to bound the bottleneck distance $d_{B}(D,D_{S})$ between the persistence diagrams computed from the original dataset $X$ and the scaled dataset $S(X)$ . Recall that the stability theorem for persistence diagrams [ 5 ] states that for two tame Lipschitz functions $f,g:X\to\mathbb{R}$ , the bottleneck distance between their corresponding persistence diagrams $D_{f}$ and $D_{g}$ satisfies $d_{B}(D_{f},D_{g})\leq\|f-g\|_{\infty},$ where $\|f-g\|_{\infty}=\sup_{x\in X}|f(x)-g(x)|. [...]
  § 4.5 Theorem 2 (Extension to Higher Homology Dimensions): Let $D^{k}$ and $D_{S}^{k}$ denote the persistence diagrams corresponding to the $k$ -th homology group $H_{k}$ before and after scaling. Then: $d_{B}(D^{k},D_{S}^{k})\leq\delta_{k}=(s_{\max}-s_{\min})\cdot\operatorname{diam}_{k}(X),$ where $\operatorname{diam}_{k}(X)$ is the maximum diameter among all $(k+1)$ -tuples in $X$ . This extends Theorem 1 to higher homology groups $H_{k}$ , proving $d_{B}(D^{k},D_{S}^{k})\leq\delta_{k}=\Delta_{s}\cdot\operatorname{diam}_{k}(X)$ . It generalizes stability bounds to $k$ -simplices and higher-dimensional features. Proof. Our goal is to establish that the bottleneck distance between the $k$ -th persistence diagrams $D^{k}$ and $D_{S}^{k}$ satisfies $d_{B}(D^{k},D_{S}^{k})\leq\delta_{k}=(s_{\max}-s_{\min})\cdot\operatorname{diam}_{k}(X).$ To achieve this, we need to analyze how the scaling transformation $S$ affects the distances relevant to $k$ -dimensional homology features. In persistent homology, $k$ -simplices are formed from $(k+1)$ -tuples of points in $X$ . [...]
  § 4.6 Theorem 3 (Stability Under Wasserstein Distance): For the $p$ -Wasserstein distance $W_{p}(D,D_{S})$ between the persistence diagrams $D$ and $D_{S}$ , we have: $W_{p}(D,D_{S})\leq\delta,$ where $\delta=(s_{\max}-s_{\min})\cdot\operatorname{diam}(X)$ . This proves $W_{p}(D,D_{S})\leq\delta$ and links $W_{p}$ -stability to $\Delta_{s}\cdot\operatorname{diam}(X)$ . It establishes robustness across alternative metrics for comparing persistence diagrams. Proof. Our goal is to show that the $p$ -Wasserstein distance between the persistence diagrams before and after scaling is bounded by $\delta$ . First, we recall the definitions: The bottleneck distance $d_{B}(D,D_{S})$ between two persistence diagrams $D$ and $D_{S}$ is defined as: $d_{B}(D,D_{S})=\inf_{\gamma}\sup_{x\in D}\|x-\gamma(x)\|_{\infty},$ where $\gamma:D\to D_{S}$ ranges over all bijections (including matching points to the diagonal). The $p$ - Wasserstein distance $W_{p}(D,D_{S})$ is defined as: $W_{p}(D,D_{S})=\left(\inf_{\gamma}\sum_{x\in D}\|x-\gamma(x)\|_{\infty}^{p}\right)^{1/p},$ where $\gamma$ is as above, and $p\geq 1$ . [...]
  § 4.7 Theorem 4 (Iterative Scaling Transformations): Suppose we apply a sequence of scaling transformations $S^{(1)},S^{(2)},\ldots,S^{(m)}$ , where each $S^{(j)}$ is defined by scaling factors $s_{i}^{(j)}>0$ for $i=1,2,\ldots,n$ . [...]
[11] arXiv:1209.0385 | Non-Associativity in the Clifford Bundle on the Parallelizable Torsion 7-Sphere
  In this paper we discuss generalized properties of non-associativity in Clifford bundles on the 7-sphere S7. Novel and prominent properties inherited from the non-associative structure of the Clifford bundle on S7 are demonstrated. They naturally lead to general transformations of the spinor fields on S7 and have dramatic consequences for the associated Kac-Moody current algebras. All additional p
  Full text (https://arxiv.org/html/1209.0385), excerpts of its own sections:
  § 1. Introduction: The main goal of this paper is provide a general class of non-associative structures on $S^{7}$ in the Clifford algebra formulation of generalized octonionic products. After briefly revisiting previous results [ 1 , 2 ] , an octonionic product is defined in the Clifford algebra $C\kern-1.00006pt\ell_{0,7}$ [ 3 ] which is closely related to the $S^{7}$ sphere [ 8 ] . Using this formalism, certain new identities are derived in a generalized octonionic algebra. See, for example, [ 9 ] for details as well as [ 7 , 10 , 11 ] for some prominent applications. Although there is a great variety of new octonionic products that may be defined, we restrict our formalism to a generalization of the results presented in [ 4 , 6 ] . First, just to fix our notation, original non-associative deformed products between octonions presented in [ 1 , 4 , 6 ] are briefly reviewed. Then, we discuss extended octonionic products between octonions and Clifford multivectors, and also among the Clifford multivectors, in the light of [ 1 , 4 ] . [...]
  § 2. Preliminaries: Let $V$ be an $n$ -dimensional real vector space and let $V^{*}$ denote its dual. We consider the tensor algebra $\bigoplus_{i=0}^{\infty}T^{i}(V)$ from which we restrict our attention to the space $\bigwedge V=\bigoplus_{k=0}^{n}\bigwedge^{k}V$ of multivectors over $V$ . $\bigwedge^{k}V$ denotes the space of the antisymmetric $k$ -tensors which is isomorphic to the vector space of $k$ -forms. Given $\psi\in\bigwedge^{k}V$ , $\tilde{\psi}$ denotes the reversion , an algebra anti-automorphism given by $\tilde{\psi}=(-1)^{[k/2]}\psi$ ([ $k$ ] denotes the integer part of $k$ ). $\hat{\psi}$ denotes the main automorphism or grade involution , given by $\hat{\psi}=(-1)^{k}\psi$ . The conjugation is defined as the reversion followed by the main automorphism. If $V$ is endowed with a non-degenerate, symmetric, bilinear map $g:V^{*}\times V^{*}\rightarrow\mathbb{R}$ , it is possible to extend $g$ to $\bigwedge V$ . The Clifford product between ${\bf w}\in V$ and $\psi\in\bigwedge V$ is given by ${\bf w}\psi={\bf w}\wedge\psi+{\bf w}\,\rfloor\,\psi$ . [...]
  § 3. The $\bullet$ -product and the $\odot$ -product on $S^{7}$: Given $X,Y\in\mathbb{R}\oplus\mathbb{R}^{0,7}$ fixed but arbitrary such that $X\bar{X}=\bar{X}X=1=\bar{Y}Y=Y\bar{Y}$ ( $X,Y\in S^{7}$ ), the $X$ -product is defined by [ 6 , 4 ] $A\circ_{X}B:=(A\circ X)\circ(\bar{X}\circ B). [...]
  § 5. Concluding remarks and outlook: The parameter $A\circ_{X}B=(A\circ X)\circ(\bar{X}\circ B)=\bar{X}\circ((X\circ A)\circ B)$ is twice the parallelizing torsion whose components are given by $\displaystyle T_{ijk}(X)=[(\bar{{\bf e}}_{i}\circ\bar{X})\circ(X\circ{{\bf e}_{j}})]\circ{\bf e}_{k}.$ (5.1) The right-hand-side of ( 5.1 ) is exactly the $\bar{X}$ -product between $\bar{{\bf e}}_{i}$ and ${\bf e}_{j}$ . So, the $S^{7}$ algebra can be written as $[\delta_{i},\delta_{j}]=2T_{ijk}(X)\delta_{k}$ where $\delta_{A}X=X\circ A$ , and the variation $\delta$ denotes the parallelizing covariant derivative [ 4 ] . By means of the $\odot$ -product, all subsequent octonionic products are regarded as the $\odot$ -product involving the Clifford multivector associated with the given octonionic product as defined in ( 3.6 ), ( 3.7 ), and ( 3.17 ). Thus, the arbitrary number of octonionic products can be encoded in a unique product – the $\odot$ -product. It is not quite a straightforward task to consider the reversed non-associative products. [...]
[12] QNFO: Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure | https://papers.qnfo.org/papers/automorphisms-and-scaling-transformations-a-re-entry-analysis-across-algebraic-g
  Mathematicians and computational scientists who classify symmetries must decide whether a rescaling of coordinates, dimensions, or metrics changes the automorphism group of the object. Without a uniform criterion, practitioners risk applying incorrect normalizations or quotients, leading to downstream errors. This paper introduces a three‑part conjugation test—normalization, centralization, and pa
  Full text (https://papers.qnfo.org/papers/automorphisms-and-scaling-transformations-a-re-entry-analysis-across-algebraic-g), excerpts of its own sections:
  § 5. Results: The explicit computations from Section 4 yield the following quantitative outcomes: | Quantity | Value | Section | |----------|-------|---------| | Shear coefficient after anisotropic dilation $D=\operatorname{diag}(2,3)$ | $c'=\dfrac{2}{3}\approx0.666667$ | 4.2 | | Scalar‑dilation effect on shear and rotation | No change (factor $1$) | 4.3 | | Jacobian determinant invariance under diagonal conjugation | Exact invariance (factor $1$) | 4.3 | | Associative ring count growth ratio | $5$ | 4.4 | | Per‑step exponent $g$ | $2.321928$ (rounded to six decimals) | 4.4 | | Density growth factor | $2.5$ | 4.4 | | Face count of the two‑ray cone | $4$ | 4.5 | | Generator count for $n=5,6,7$ free factors | $20$, $30$, $42$ respectively | 4.6 | | Totient values $\varphi(2),\varphi(3),\varphi(4),\varphi(5),\varphi(6)$ | $1,2,2,4,2$ | 4.7 | | Totient bound for K3 automorphisms | $\varphi(n)\le20$, $n\neq60$ | 4.7 | All numbers are derived directly from the inputs listed in Table 4.1 and the arithmetic shown in the subsections.
  § 6. Discussion: In this section we deepen the quantitative core of the conjugation test by applying it to three concrete families that appear in the literature but were not treated in the main analysis.  Each example is worked out step‑by‑step, using only the numerical or structural inputs that the cited sources provide.
  § 6.  Summary of extended derivations: | Example | Source | Result | |---------|--------|--------| | Translation parameter rescales by \(\lambda_{1}\) | [7] (construction of \(F\) conjugate to (1)) | Equation (3) | | Aperiodic automorphisms have infinite order → totient count inapplicable | [5] (classification of aperiodic automorphisms) | Section 6 limitation refined | | Central elements of scaling monoid act trivially | [10] (definition of scaling monoid) | Equation (4) | | Ratio \(2/3\) is base‑invariant | [11] (ratio‑centric paradigm) & [12] (base‑invariant scaling symmetries) | Conceptual justification | | Factor‑isomorphism generators central under diagonal scaling | [5] (presentation of \(\operatorname{Out}\)) | Equation (6) | These worked examples illustrate that the three‑part conjugation test extends beyond the linear planar maps of Sections 4.2–4.3 to (i) non‑linear translations in complex dynamics, (ii) infinite‑order automorphisms in operator algebras, (iii) abstract scaling monoids, and (iv) free‑product outer automorphisms. [...]
  § 9. Conclusion: **(a) Intended users and decision impact.** Researchers and developers of computer‑algebra systems that automate symmetry classification will use the ratio rule to decide whether a scaling step can be safely omitted (scalar dilation) or must be accounted for by adjusting parameter values (anisotropic dilation). In geometric modeling pipelines, the rule informs whether a coordinate‑rescaling will alter the symmetry group of a shape, affecting downstream mesh generation or invariant detection. **(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 2 (formulation of concept and analytical proof‑of‑concept). **(c) Smallest next experiment.** Implement a prototype module in a symbolic‑computation system that automatically applies the conjugation test to a user‑supplied linear automorphism and a diagonal scaling. The module should compute the transformed parameters and verify that the Jacobian determinant remains unchanged. [...]