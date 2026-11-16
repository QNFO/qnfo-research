# Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure

## Abstract

Mathematicians and computational scientists who classify symmetries must decide, before quotienting a configuration space by scalings or normalizing coordinates in a pipeline, whether a rescaling changes the automorphism group of the object. The literature treats this question setting by setting—conjugation actions in group rings, character theory, quantum groups, soliton physics, persistent homology—with no shared computable criterion, so a practitioner moving between settings must re-derive the interaction or risk an unjustified assumption. This paper supplies a three-part conjugation test—normalization, centralization, parameter rescaling—and carries out its quantitative branch with explicit arithmetic. For the planar shear $\phi(x,y)=(x+y,y)$, the anisotropic dilation $D=\operatorname{diag}(2,3)$ rescales the shear coefficient by $2/3\approx0.666667$, while scalar dilations centralize shears and rotations exactly and leave Jacobian determinants unchanged. For the Cayley–Dickson tower, the octonion-to-sedenion step multiplies the count of associative quaternion rings from $7$ to $35$, a factor of $5$, i.e. $\log_{2}5\approx2.321928$ per dimension-doubling step, and the density per real dimension grows by exactly $2.5$ (from $0.875$ to $2.1875$). The framework is connected to conjugation-action results across group rings, character theory, quantum groups, Coxeter groups, Banach representations, and scaling-stability bounds in data augmentation. The result is a computable, falsifiable rule—ratio rescaling for anisotropic dilations, triviality for isotropic ones—that practitioners can apply before invoking scaling arguments in classification or normalization pipelines.

## 1. Introduction

Mathematicians and computational scientists who classify symmetries face a recurring operational problem: before quotienting a configuration space by scalings, or before running a normalization algorithm that rescales coordinates, they must know whether the rescaling changes the automorphism group of the object. If it does, the quotient or the normalized form is a different object with a different symmetry group, and downstream computations inherit an error. Today this question is answered setting by setting—one body of technique for conjugation actions on completed group rings, another for character-theoretic invariants of finite groups, another for quantum matrix invariants, another for the scaling stability of data-augmentation pipelines—with no shared criterion, so a practitioner moving between settings must re-derive the interaction from scratch or risk an unjustified assumption. A uniform, computable test that says exactly when a dilation acts trivially, and when it rescales automorphism parameters by a stated factor, would change that decision: the practitioner could check the test, apply the ratio rule or certify triviality, and proceed without re-deriving the interaction.

The paper supplies such a test and demonstrates it with full arithmetic. An automorphism of a mathematical object $X$ is an isomorphism $X\to X$; the automorphisms form a group $\operatorname{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S$ that rescales a chosen coordinate, metric, dimension, or norm by a factor $\lambda$ without changing the underlying structure type. The literature provides isolated observations but no systematic framework: [1] proves that inner automorphisms of a completed group ring that preserve the group are induced from inner automorphisms of the group itself; [2] studies the smallest integer $e(G)$ that makes the reciprocal of the conjugation-action character a generalized character; [4] shows that the invariants of the conjugation action of a quantum general linear group form a commutative polynomial algebra; [10] bounds how far non-uniform scaling can move persistence diagrams. We fill the gap between such isolated results with a three-part conjugation test and extend it with explicit derivations across several settings.

Our contributions are:

- A derivation of the conjugation test's central computation, showing that anisotropic dilations rescale shear parameters by the ratio $\lambda_{1}/\lambda_{2}$ of diagonal entries while scalar dilations centralize shears and rotations exactly (Sections 3, 4.2 and 4.3).
- A Jacobian-invariance derivation: conjugation by any diagonal dilation leaves the Jacobian determinant of a planar linear map unchanged (Section 4.3).
- A growth analysis of associative structure in the Cayley–Dickson tower, with the factor $5$, the exponent $\log_{2}5\approx2.321928$, and the density ratio $2.5$ all computed step by step from the ring counts $7$ and $35$ reported in the prior version [12] (Section 4.4).
- A translation-parameter derivation for nonlinear automorphisms of $\mathbb{C}^{2}$: conjugation by $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ multiplies a translation coefficient by $\lambda_{1}$ (Section 4.8).
- A scaling-stability reading of the conjugation test, connecting the ratio rule to the persistence-diagram bound $\delta=(s_{\max}-s_{\min})\cdot\operatorname{diam}(X)$ of [10] with a worked numerical example (Section 4.6).
- A discrete-scaling rigidity result via Euler's totient, $\varphi(2)=1$, with its consequence for order-two discrete scalings (Section 4.7).
- An explicit statement of limitations, falsification conditions, and the smallest next computations that would de-risk or refute the framework (Sections 6 and 7).

The ratio rule and its triviality certificate also bear on problems outside pure classification: the stability of topological descriptors under non-uniform rescaling in data-augmentation pipelines [10], and the role of scaling symmetries that are not variational symmetries in Lagrangian dynamics [3].

## 2. Background and Related Work

We discuss the cited works in their fixed numbering, citing each for a specific method, result, or number that its text states.

**[1] The conjugation action in completed group rings.** For a $p$-valuable group $G$ and its completed group algebra $kG$ (an Iwasawa algebra), Theorem A states that every automorphism $\sigma$ of $kG$ that preserves the naturally embedded copy of $G$ is the unique extension of an inner automorphism of $G$. The proof analyzes the conjugation action of $G$ on itself, writing an inner automorphism of $kG$ as $\sigma(r)=ara^{-1}$ and decomposing coefficients over a transversal $T$ to a characteristic uniform open subgroup $N$. Theorem C studies the fixed rings $kG$ under the conjugation action of a closed subgroup $\Gamma$, with $H$ the centraliser of $\Gamma$ in $G$. This is a rigidity statement of exactly the kind our centralization branch formalizes: conjugation-induced maps are controlled by the group's own inner automorphisms, and the centralizer $H$ is the object that measures triviality of the action.

**[2] The reciprocal character of the conjugation action.** For a finite group $G$, the conjugation action on itself determines the permutation character $\pi$ with $\pi(g)=|\mathrm{C}_{G}(g)|$; the paper studies the reciprocal class function $\tilde{\pi}(g)=|\mathrm{C}_{G}(g)|^{-1}$ and the smallest positive integer $e(G)$ such that $e(G)|G|\tilde{\pi}$ is a generalized character. Proposition 1(i) proves that $e(G)$ divides $|G:\mathrm{Z}(G)|$, so the integrability index of the reciprocal conjugation character is controlled by the index of the center. The paper also shows, in its examples, non-trivial groups with $e'(G)=1$ built from $A\cong C_{9}^{4}$, $B\cong C_{25}^{2}$ and $C\cong C_{15}$. This quantifies how the size of the centralizer—the quantity our test's question (C) asks about—feeds into a global arithmetic invariant of the conjugation action.

**[3] Invariant relationships deriving from classical scaling transformations.** The paper establishes that scaling symmetries of the Euler–Lagrange equations are generally not variational symmetries of the action, and extends Noether's theorem so that such transformations still yield Noether identities and evolutionary equations. For scaling symmetries specifically, the evolutionary equation connects linearly the kinematic and dynamic parts of the Lagrangian; for nonrelativistic systems with inverse-power law potentials it is a generalized virial law, and for barotropic hydrostatic systems it is a linear relation between local gravitational and internal energies. This is a physics-side instance of our theme: a scaling acts nontrivially on parameters (here, on the relation between kinetic and potential terms) even when it is not a symmetry of the primitive structure, which motivates the parameter-rescaling branch of the test.

**[4] On the conjugation action for quantum general linear groups.** For the coordinate algebra of a quantised general linear group $G(n)$ at an arbitrary nonzero parameter $q$, the paper proves that the algebra of polynomial invariants for the conjugation action is a commutative polynomial algebra, recovering and extending the result of Domokos and Lenagan at $q$ not a root of unity. Theorem 7.4 describes a $(C(G),G)$-module filtration of the coordinate algebra $k[G]$, an analogue of results of Richardson and Kostant. The invariant algebra being freely generated shows that the conjugation action, though nontrivial, has a maximally simple invariant ring—a structural outcome our test's normalization question (N) is designed to detect before such a computation is attempted.

**[5] Notes on partial conjugation.** The paper exposits partial conjugation actions of parabolic subgroups $W_{J}$ of Coxeter groups, including the $\delta$-twisted action $w\cdot_{\delta}w'=\delta(w)w'w^{-1}$, and applies the method to Lusztig's $G$-stable pieces, which biject with twisted conjugacy classes of a Levi factor. Theorem 1.1 classifies the orbits: $W=\sqcup_{w\in W^{J}}W_{J}\cdot_{\delta}(wW_{I(J,w,\delta)})$, where $I(J,w,\delta)$ is a subgroup determined by which simple reflections commute past $w$. Partial conjugation is a conjugation action restricted to a subgroup—the same object our test manipulates when a scaling acts only on part of a structure—so its orbit classification is a model for what question (C) must resolve in the presence of partial actions.

**[6] Approximate solutions and scaling transformations for quadratic solitons.** The paper obtains almost exact analytical solutions for quadratic bright solitons in $\chi^{(2)}$ media by choosing trial functions to match the scaling properties of the solitons, and reports quantitative accuracy: in a wide region of mismatch values $\alpha>1$, the relative errors are smaller than $0.7\%$ for the total power and $0.3\%$ for other characteristics. Its concluding remarks attribute the precision directly to the scaling-matched trial functions. This is an applied demonstration that identifying the correct scaling behaviour of a family of objects (here, soliton profiles) converts into numerical accuracy in downstream computation—the practical payoff our ratio rule targets in algebraic settings.

**[7] Topological group actions by group automorphisms and Banach representations.** The paper studies which actions of a topological group $G$ on a topological group $X$ by automorphisms can be represented on low-complexity Banach spaces, and records that the conjugation action $G_{c}$ is Banach representable for every topological group $G$, via the Roelcke compactification. It also proves negative results: the conjugation action need not be reflexively representable even for natural matrix groups, in particular for $\operatorname{SL}_{2}(\mathbb{R})$ (Theorem 3.3, via Grothendieck's double limit criterion), and $G_{c}$ for $G=\operatorname{SL}_{n}(\mathbb{R})$ is not Asplund representable for every $n\geq4$ (Theorem 3.10). These results show that the complexity of representing a conjugation action depends sharply on the group, so a certificate of when a conjugation-type action is trivial or controlled has representational consequences.

**[8] A representation on the labeled rooted forests.** The paper considers the conjugation action of the symmetric group on the partial transformation semigroup $\mathcal{P}_{n}$ and develops machinery for character formulas and multiplicities, determining nilpotent matrices whose orbits afford the sign representation, with applications to rook theory. Its forest combinatorics uses Cayley's theorem in the form of $n^{n-1}$ labeled rooted trees on $n$ vertices and $(n+1)^{n-1}$ labeled rooted forests on $n$ vertices. This supplies a combinatorial setting in which a conjugation action (of $S_{n}$ on $\mathcal{P}_{n}$) acts on objects whose counts grow by explicit exponential laws—the same counting pattern our Cayley–Dickson growth analysis isolates.

**[9] Topological K-theory of the group C*-algebra of a semi-direct product $\mathbb{Z}^{n}\rtimes\mathbb{Z}/m$ for a free conjugation action.** For an extension $1\to\mathbb{Z}^{n}\to\Gamma\to\mathbb{Z}/m\to1$ whose conjugation action of $\mathbb{Z}/m$ on $\mathbb{Z}^{n}$ is free outside the origin, Theorem 0.1 computes the topological $K$-theory of $C^{*}_{r}(\Gamma)$, giving isomorphisms between $K_{1}(C^{*}_{r}(\Gamma))$ and $K_{1}(\underline{B}\Gamma)$ and expressing the answer with exterior powers $\Lambda^{i}\mathbb{Z}^{n}$ and Tate cohomology $\widehat{H}^{*}(G;M)$. In the prime case $m=p$, the module decomposes as $\mathbb{Z}^{n}_{\rho}\otimes_{\mathbb{Z}}\mathbb{Q}\cong_{\mathbb{Q}[\mathbb{Z}/p]}\mathbb{Q}[\zeta_{p}]^{k}$ with $n=(p-1)\cdot k$. This is a case study in which the freeness of a conjugation action—an extreme form of the centralization question—directly determines the computability of an invariant.

**[10] Topology-Preserving Scaling in Data Augmentation.** The paper proposes a normalization framework for data-augmentation pipelines under non-uniform scaling with factors $s_{1},\dots,s_{n}>0$. Theorem 1 bounds the bottleneck distance between persistence diagrams before and after scaling by $\delta=\delta'\cdot\operatorname{diam}(X)=(s_{\max}-s_{\min})\cdot\operatorname{diam}(X)$; Theorem 2 extends the bound to $k$-th homology with $\delta_{k}=(s_{\max}-s_{\min})\cdot\operatorname{diam}_{k}(X)$; Theorem 3 proves the analogous Wasserstein bound $W_{p}(D,D_{S})\leq\delta$; Theorem 4 treats iterative sequences of scalings. This is the closest applied analogue of our test: it gives a computable, quantitative certificate of how much a rescaling can move a structural invariant, exactly the service our ratio rule performs for automorphism parameters.

**[11] Non-Associativity in the Clifford Bundle on the Parallelizable Torsion 7-Sphere.** The paper studies non-associative structures on $S^{7}$ arising from generalized octonionic products in the Clifford algebra $C\ell_{0,7}$, defining $X$-products $A\circ_{X}B:=(A\circ X)\circ(\bar{X}\circ B)$ for unit octonions $X,Y\in S^{7}$ and deriving the structure-constant identity $[\delta_{i},\delta_{j}]=2T_{ijk}(X)\delta_{k}$, where $T_{ijk}(X)$ is the parallelizing torsion. This shows that non-associative algebra carries a family of products parametrized by a point $X$ of $S^{7}$—a parameterized family of structures of the kind our parameter-rescaling branch is designed to compare, and the non-associative backdrop for the Cayley–Dickson growth analysis.

**[12] The prior version of this paper.** The published version states the three-part conjugation test and reports its quantitative outcomes: the shear coefficient $c'=2/3\approx0.666667$ after anisotropic dilation $D=\operatorname{diag}(2,3)$; exact invariance of the Jacobian determinant under diagonal conjugation; the associative-ring-count growth ratio $5$; the per-step exponent $2.321928$; the density growth factor $2.5$; the face count $4$ of the two-ray cone; generator counts $20,30,42$ for $n=5,6,7$ free factors; and the totient values $1,2,2,4,2$ for $\varphi(2),\dots,\varphi(6)$. Its discussion extends the test to translation parameters rescaled by $\lambda_{1}$ and to central elements of an abstract scaling monoid acting trivially. We take these reported counts as the inputs for the growth analysis in Section 4.4 and re-derive every consequence with the arithmetic shown.

## 3. Methods

### 3.1 The conjugation test

Let $X$ be an object in a category $\mathcal{C}$ with automorphism group $\operatorname{Aut}(X)$, and let $\mathcal{S}(X)$ be a distinguished class of self-bijections of $X$ called **scalings**: maps $S\!:\!X\to X$ that rescale a chosen structure (a norm, a filtration, a metric, a coordinate, a dimension grading) without changing the structure type. We use two concrete families:

- **Scalar dilations** $S_{\lambda}(x)=\lambda x$ on a vector space or algebra, with $\lambda\in\mathbb{R}_{>0}$ or $\mathbb{C}^{*}$.
- **Anisotropic dilations** $D=\operatorname{diag}(\lambda_{1},\dots,\lambda_{n})$ on $\mathbb{R}^{n}$ or $\mathbb{C}^{n}$, with $\lambda_{i}>0$ and not all equal.

The conjugation test applied to a pair $(S,\phi)$, $S\in\mathcal{S}(X)$, $\phi\in\operatorname{Aut}(X)$, asks:

$$
\text{(N)}\quad S\phi S^{-1}\in\operatorname{Aut}(X)\;? \qquad
\text{(C)}\quad S\phi=\phi S\;? \qquad
\text{(P)}\quad \text{does }S(\cdot)S^{-1}\text{ act on the parameters of }\phi\text{ by a computable rule?}
$$

Question (N) is automatic whenever $S$ is itself an automorphism; the interesting content arises when $S$ is not an automorphism of the particular object but the conjugate still preserves the structure type. Question (C) identifies the centralizer $C_{\mathcal{S}}(\phi)=\{S\in\mathcal{S}(X):S\phi=\phi S\}$; the centralizer is the same quantity that controls the character-theoretic index of [2] (through $|\mathrm{C}_{G}(g)|$ and $|G:\mathrm{Z}(G)|$) and the fixed-ring description of [1] (through the centraliser $H$ of $\Gamma$). Question (P) is the quantitative core, carried out in Section 4.

### 3.2 Model automorphisms

Two planar linear maps serve as canonical test automorphisms of $\mathbb{R}^{2}$:

$$
\phi_{\mathrm{uni}}(x,y)=(x+y,\;y), \qquad
\phi_{\mathrm{rot}}(x,y)=(\cos\theta\,x-\sin\theta\,y,\;\sin\theta\,x+\cos\theta\,y),
$$

a unipotent shear with coefficient $c=1$ and a rotation by angle $\theta$. For the $n$-dimensional extension we use coordinate-plane shears $\phi_{ij}$ acting as $\phi_{ij}(x)=x+e_{i}x_{j}$ on the $i$-th coordinate, where $e_{i}$ is the $i$-th basis vector. A third model, nonlinear, is the translation $T(z,w)=(z+1,w)$ of $\mathbb{C}^{2}$, treated in Section 4.8.

### 3.3 Growth accounting for the Cayley–Dickson tower

For the non-associative setting, the prior version [12] reports $N_{\mathrm{oct}}=7$ associative quaternion rings in the octonions and $N_{\mathrm{sed}}=35$ in the sedenions, together with the dimension law of the Cayley–Dickson series: the $N$-th algebra $\mathrm{A}_{N}$ has $n=2^{N}$ basis elements. We treat the octonion-to-sedenion passage as one dimension-doubling step with dimensions $2^{3}=8$ and $2^{4}=16$. We define:

- the per-step growth exponent $g=\log_{2}\!\bigl(N_{\mathrm{sed}}/N_{\mathrm{oct}}\bigr)$;
- the ring density $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$ for a Cayley–Dickson algebra $A$;
- the density growth factor $\delta(\mathbb{S})/\delta(\mathbb{O})$.

All arithmetic appears in Section 4.4. The non-associative background for these algebras—the way octonionic non-associativity organizes into parameterized families of products—is documented in [11], which derives the torsion structure constants $T_{ijk}(X)$ on $S^{7}$; we use [11] only as this structural backdrop, not as a source of the counts.

### 3.4 Scaling-stability accounting

To compare the ratio rule with an applied stability certificate, we use the bounds of [10]: for a finite metric space $X\subset\mathbb{R}^{n}$ scaled by factors $s_{1},\dots,s_{n}>0$, the bottleneck distance between persistence diagrams satisfies $d_{B}(D,D_{S})\leq(s_{\max}-s_{\min})\cdot\operatorname{diam}(X)$, with the analogous bound $\delta_{k}=(s_{\max}-s_{\min})\cdot\operatorname{diam}_{k}(X)$ in homology degree $k$ and $W_{p}(D,D_{S})\leq\delta$ in Wasserstein distance. We evaluate these bounds for stated numerical assumptions in Section 4.6.

### 3.5 Discrete-scaling rigidity

If a scaling transformation has a discrete parameter group with cyclic image of order $k$, a scaling-compatible automorphism induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler's totient $\varphi(k)$. We evaluate $\varphi$ for small $k$ and interpret the case $k=2$ as a rigidity statement for order-two discrete scalings.

## 4. Analysis

### 4.1 Input inventory

Every number used below, with its source:

| Item | Value / expression | Source |
|------|-------------------|--------|
| Shear coefficient after anisotropic dilation | $c'=\dfrac{\lambda_{1}}{\lambda_{2}}c$ with $\lambda_{1}=2$, $\lambda_{2}=3$, $c=1$ | derived in 4.2 |
| Scalar-dilation centrality factor | $1$ (no change) | derived in 4.3 |
| Jacobian determinant of a planar linear map | $\det J=\det(M)$; invariant under conjugation | derived in 4.3 |
| Octonion associative ring count | $N_{\mathrm{oct}}=7$ | [12] |
| Sedenion associative ring count | $N_{\mathrm{sed}}=35$ | [12] |
| Growth ratio $r$ | $r=N_{\mathrm{sed}}/N_{\mathrm{oct}}=5$ | 4.4 |
| Per-step exponent $g$ | $g=\log_{2}5\approx2.321928$ | 4.4 |
| Octonion dimension | $D_{3}=2^{3}=8$ | [12] |
| Sedenion dimension | $D_{4}=2^{4}=16$ | [12] |
| Density $\delta(\mathbb{O})$ | $7/8=0.875$ | 4.4 |
| Density $\delta(\mathbb{S})$ | $35/16=2.1875$ | 4.4 |
| Density growth factor | $2.5$ | 4.4 |
| Translation coefficient after dilation | $1\mapsto\lambda_{1}$ | derived in 4.8 |
| Stability bound inputs (assumption) | $s_{\max}-s_{\min}=1$, $\operatorname{diam}(X)=10$ | assumed, 4.6 |
| Totient values | $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$ | 4.7 |

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
D\,\phi_{\mathrm{uni}}\,D^{-1}(x,y)=\left(x+\frac