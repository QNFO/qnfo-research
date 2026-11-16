# Automorphisms and Scaling Transformations: A Conjugation Test for Linear and Nonlinear Maps, with Growth Accounting for Associative Structure

## Abstract

Mathematicians and computational scientists who classify symmetries must decide, before quotienting a configuration space by scalings or before running a normalization pipeline that rescales coordinates, whether the rescaling changes the automorphism group of the object. The literature treats this question setting by setting—conjugation actions in completed group rings, character-theoretic invariants of finite groups, quantum matrix invariants, scaling symmetries in Lagrangian dynamics, stability bounds in data augmentation—with no shared computable criterion, so a practitioner moving between settings must re-derive the interaction or risk an unjustified assumption. This paper supplies a three-part conjugation test—normalization, centralization, parameter rescaling—and carries out its quantitative branch with explicit arithmetic. For the planar shear $\phi(x,y)=(x+y,y)$, the anisotropic dilation $D=\operatorname{diag}(2,3)$ rescales the shear coefficient to $c'=2/3\approx0.666667$, while scalar dilations centralize shears and rotations exactly and leave Jacobian determinants unchanged; conjugation by $D$ multiplies a translation coefficient of a nonlinear automorphism of $\mathbb{C}^{2}$ by $\lambda_{1}$. For the Cayley–Dickson tower, the octonion-to-sedenion step multiplies the count of associative quaternion rings from $7$ to $35$, a factor of $5$, i.e. $\log_{2}5\approx2.321928$ per dimension-doubling step, and the ring density per real dimension grows by exactly $2.5$ (from $0.875$ to $2.1875$). The result is a computable, falsifiable rule—ratio rescaling for anisotropic dilations, triviality for isotropic ones—that practitioners can apply before invoking scaling arguments in classification or normalization pipelines.

## 1. Introduction

Mathematicians and computational scientists who classify symmetries face a recurring operational problem: before quotienting a configuration space by scalings, or before running a normalization algorithm that rescales coordinates, they must know whether the rescaling changes the automorphism group of the object. If it does, the quotient or the normalized form is a different object with a different symmetry group, and downstream computations inherit an error. Today this question is answered setting by setting—one body of technique for conjugation actions on completed group rings, another for character-theoretic invariants of finite groups, another for quantum matrix invariants, another for the scaling stability of data-augmentation pipelines—with no shared criterion, so a practitioner moving between settings must re-derive the interaction from scratch or risk an unjustified assumption. A uniform, computable test that says exactly when a dilation acts trivially, and when it rescales automorphism parameters by a stated factor, would change that decision: the practitioner could check the test, apply the ratio rule or certify triviality, and proceed without re-deriving the interaction.

Throughout, an automorphism of a mathematical object $X$ is an isomorphism $X\to X$; the automorphisms form a group $\operatorname{Aut}(X)$ under composition. A scaling transformation (dilation) is a map $S$ that rescales a chosen coordinate, metric, dimension, or norm by a factor $\lambda$ without changing the underlying structure type. The literature provides isolated observations of the interaction but no systematic framework: [1] proves that automorphisms of a completed group ring preserving the group are induced from inner automorphisms of the group itself; [2] studies the smallest integer $e(G)$ that makes the reciprocal of the conjugation-action character a generalized character; [4] shows that the invariants of the conjugation action of a quantum general linear group form a commutative polynomial algebra; [10] bounds how far non-uniform scaling can move persistence diagrams. We fill the gap between such isolated results with a three-part conjugation test and demonstrate it with full arithmetic on planar linear maps, on a nonlinear translation, and on the counting structure of the Cayley–Dickson tower.

Our contributions are:

- **C1.** A derivation of the conjugation test's central computation, showing that anisotropic dilations rescale shear parameters by the ratio $\lambda_{1}/\lambda_{2}$ of diagonal entries while scalar dilations centralize shears and rotations exactly (Sections 3, 4.2 and 4.3).
- **C2.** A Jacobian-invariance derivation: conjugation by any diagonal dilation leaves the Jacobian determinant of a planar linear map unchanged (Section 4.3).
- **C3.** A translation-parameter derivation for nonlinear automorphisms of $\mathbb{C}^{2}$: conjugation by $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ multiplies a translation coefficient by $\lambda_{1}$ (Section 4.4).
- **C4.** A growth analysis of associative structure in the Cayley–Dickson tower, with the factor $5$, the exponent $\log_{2}5\approx2.321928$, and the density ratio $2.5$ all computed step by step from the ring counts $7$ and $35$ reported in the prior version [12] (Section 4.5).
- **C5.** A scaling-stability reading of the conjugation test, connecting the ratio rule to the persistence-diagram bound $\delta=(s_{\max}-s_{\min})\cdot\operatorname{diam}(X)$ of [10] with a worked numerical example under stated assumptions (Section 4.6).
- **C6.** A discrete-scaling rigidity observation via Euler's totient, $\varphi(2)=1$, with its consequence for order-two discrete scalings (Section 4.7).
- **C7.** An explicit statement of limitations, falsification conditions, and the smallest next computations that would de-risk or refute the framework (Section 6), and a translation into practice for developers of computer-algebra systems and geometric-modeling pipelines (Section 7).

The ratio rule and its triviality certificate also bear on problems outside pure classification: the stability of topological descriptors under non-uniform rescaling in data-augmentation pipelines [10], and the role of scaling symmetries that are not variational symmetries in Lagrangian dynamics [3].

## 2. Background and Related Work

We discuss the cited works in their fixed numbering, citing each for a specific method, result, or number that its text states.

**[1] The conjugation action in completed group rings.** For a $p$-valuable group $G$ and its completed group algebra $kG$ (an Iwasawa algebra), Theorem A states that every automorphism $\sigma$ of $kG$ that preserves the naturally embedded copy of $G$ is the unique extension of an inner automorphism of $G$. The proof analyzes the conjugation action of $G$ on itself, writing an inner automorphism of $kG$ as $\sigma(r)=ara^{-1}$ and decomposing coefficients over a transversal $T$ to a characteristic uniform open subgroup $N$; Theorem C studies the fixed rings of $kG$ under the conjugation action of a closed subgroup $\Gamma$, with $H$ the centraliser of $\Gamma$ in $G$. This is a rigidity statement of exactly the kind our centralization branch formalizes: conjugation-induced maps are controlled by the group's own inner automorphisms, and the centralizer $H$ is the object that measures triviality of the action.

**[2] The reciprocal character of the conjugation action.** For a finite group $G$, the conjugation action on itself determines the permutation character $\pi$ with $\pi(g)=|\mathrm{C}_{G}(g)|$; the paper studies the reciprocal class function $\tilde{\pi}(g)=|\mathrm{C}_{G}(g)|^{-1}$ and the smallest positive integer $e(G)$ such that $e(G)|G|\tilde{\pi}$ is a generalized character. Proposition 1(i) proves that $e(G)$ divides $|G:\mathrm{Z}(G)|$, so the integrability index of the reciprocal conjugation character is controlled by the index of the center; the examples exhibit non-trivial groups with $e'(G)=1$ built from $A\cong C_{9}^{4}$, $B\cong C_{25}^{2}$ and $C\cong C_{15}$. This quantifies how the size of the centralizer—the quantity our test's question (C) asks about—feeds into a global arithmetic invariant of the conjugation action.

**[3] Invariant relationships deriving from classical scaling transformations.** The paper establishes that scaling symmetries of the Euler–Lagrange equations are generally not variational symmetries of the action, and extends Noether's theorem so that such transformations still yield Noether identities and evolutionary equations. For scaling symmetries specifically, the evolutionary equation connects linearly the kinematic and dynamic parts of the Lagrangian; for nonrelativistic systems with inverse-power law potentials it is a generalized virial law, and for barotropic hydrostatic systems it is a linear relation between local gravitational and internal energies. This is a physics-side instance of our theme: a scaling acts nontrivially on parameters (here, on the relation between kinetic and potential terms) even when it is not a symmetry of the primitive structure, which motivates the parameter-rescaling branch of the test.

**[4] On the conjugation action for quantum general linear groups.** For the coordinate algebra of a quantised general linear group $G(n)$ at an arbitrary nonzero parameter $q$, the paper proves that the algebra of polynomial invariants for the conjugation action is a commutative polynomial algebra, recovering and extending the result of Domokos and Lenagan at $q$ not a root of unity; Theorem 7.4 describes a $(C(G),G)$-module filtration of the coordinate algebra $k[G]$, an analogue of results of Richardson and Kostant. The invariant algebra being freely generated shows that the conjugation action, though nontrivial, has a maximally simple invariant ring—a structural outcome our test's normalization question (N) is designed to detect before such a computation is attempted.

**[5] Notes on partial conjugation.** The paper exposits partial conjugation actions of parabolic subgroups $W_{J}$ of Coxeter groups, including the $\delta$-twisted action $w\cdot_{\delta}w'=\delta(w)w'w^{-1}$, and applies the method to Lusztig's $G$-stable pieces, which biject with twisted conjugacy classes of a Levi factor. Theorem 1.1 classifies the orbits as $W=\sqcup_{w\in W^{J}}W_{J}\cdot_{\delta}(wW_{I(J,w,\delta)})$, where $I(J,w,\delta)$ is a subgroup determined by which simple reflections commute past $w$. Partial conjugation is a conjugation action restricted to a subgroup—the same object our test manipulates when a scaling acts only on part of a structure—so its orbit classification is a model for what question (C) must resolve in the presence of partial actions.

**[6] Approximate solutions and scaling transformations for quadratic solitons.** The paper obtains almost exact analytical solutions for quadratic bright solitons in $\chi^{(2)}$ media by choosing trial functions to match the scaling properties of the solitons, and reports quantitative accuracy: in a wide region of mismatch values $\alpha>1$, the relative errors are smaller than $0.7\%$ for the total power and $0.3\%$ for other characteristics, with the concluding remarks attributing the precision directly to the scaling-matched trial functions. This is an applied demonstration that identifying the correct scaling behaviour of a family of objects converts into numerical accuracy in downstream computation—the practical payoff our ratio rule targets in algebraic settings.

**[7] Topological group actions by group automorphisms and Banach representations.** The paper studies which actions of a topological group $G$ on a topological group $X$ by automorphisms can be represented on low-complexity Banach spaces, and records that the conjugation action $G_{c}$ is Banach representable for every topological group $G$, via the Roelcke compactification. It also proves negative results: the conjugation action need not be reflexively representable even for natural matrix groups, in particular for $\operatorname{SL}_{2}(\mathbb{R})$ (Theorem 3.3, via Grothendieck's double limit criterion), and $G_{c}$ for $G=\operatorname{SL}_{n}(\mathbb{R})$ is not Asplund representable for every $n\geq4$ (Theorem 3.10). These results show that the complexity of representing a conjugation action depends sharply on the group, so a certificate of when a conjugation-type action is trivial or controlled has representational consequences.

**[8] A representation on the labeled rooted forests.** The paper considers the conjugation action of the symmetric group on the partial transformation semigroup $\mathcal{P}_{n}$ and develops machinery for character formulas and multiplicities, determining nilpotent matrices whose orbits afford the sign representation, with applications to rook theory. Its forest combinatorics uses Cayley's theorem in the form of $n^{n-1}$ labeled rooted trees on $n$ vertices and $(n+1)^{n-1}$ labeled rooted forests on $n$ vertices. This supplies a combinatorial setting in which a conjugation action acts on objects whose counts grow by explicit exponential laws—the same counting pattern our Cayley–Dickson growth analysis isolates.

**[9] Topological K-theory of the group C*-algebra of a semi-direct product $\mathbb{Z}^{n}\rtimes\mathbb{Z}/m$ for a free conjugation action.** For an extension $1\to\mathbb{Z}^{n}\to\Gamma\to\mathbb{Z}/m\to1$ whose conjugation action of $\mathbb{Z}/m$ on $\mathbb{Z}^{n}$ is free outside the origin, Theorem 0.1 computes the topological $K$-theory of $C^{*}_{r}(\Gamma)$, giving isomorphisms between $K_{1}(C^{*}_{r}(\Gamma))$ and $K_{1}(\underline{B}\Gamma)$ and expressing the answer with exterior powers $\Lambda^{i}\mathbb{Z}^{n}$ and Tate cohomology $\widehat{H}^{*}(G;M)$; in the prime case $m=p$, the module decomposes as $\mathbb{Z}^{n}_{\rho}\otimes_{\mathbb{Z}}\mathbb{Q}\cong_{\mathbb{Q}[\mathbb{Z}/p]}\mathbb{Q}[\zeta_{p}]^{k}$ with $n=(p-1)\cdot k$. This is a case study in which the freeness of a conjugation action—an extreme form of the centralization question—directly determines the computability of an invariant.

**[10] Topology-Preserving Scaling in Data Augmentation.** The paper proposes a normalization framework for data-augmentation pipelines under non-uniform scaling with factors $s_{1},\dots,s_{n}>0$. Theorem 1 bounds the bottleneck distance between persistence diagrams before and after scaling by $\delta=\delta'\cdot\operatorname{diam}(X)=(s_{\max}-s_{\min})\cdot\operatorname{diam}(X)$; Theorem 2 extends the bound to $k$-th homology with $\delta_{k}=(s_{\max}-s_{\min})\cdot\operatorname{diam}_{k}(X)$; Theorem 3 proves the analogous Wasserstein bound $W_{p}(D,D_{S})\leq\delta$; Theorem 4 treats iterative sequences of scalings. This is the closest applied analogue of our test: it gives a computable, quantitative certificate of how much a rescaling can move a structural invariant, exactly the service our ratio rule performs for automorphism parameters.

**[11] Non-Associativity in the Clifford Bundle on the Parallelizable Torsion 7-Sphere.** The paper studies non-associative structures on $S^{7}$ arising from generalized octonionic products in the Clifford algebra $C\ell_{0,7}$, defining $X$-products $A\circ_{X}B:=(A\circ X)\circ(\bar{X}\circ B)$ for unit octonions $X,Y\in S^{7}$ and deriving the structure-constant identity $[\delta_{i},\delta_{j}]=2T_{ijk}(X)\delta_{k}$, where $T_{ijk}(X)$ is the parallelizing torsion. This shows that non-associative algebra carries a family of products parametrized by a point $X$ of $S^{7}$—a parameterized family of structures of the kind our parameter-rescaling branch is designed to compare, and the non-associative backdrop for the Cayley–Dickson growth analysis.

**[12] The prior version of this paper.** The published version states the three-part conjugation test and reports its quantitative outcomes: the shear coefficient $c'=2/3\approx0.666667$ after anisotropic dilation $D=\operatorname{diag}(2,3)$; exact invariance of the Jacobian determinant under diagonal conjugation; the associative-ring-count growth ratio $5$; the per-step exponent $2.321928$; the density growth factor $2.5$; the face count $4$ of the two-ray cone; generator counts $20,30,42$ for $n=5,6,7$ free factors; and the totient values $1,2,2,4,2$ for $\varphi(2),\dots,\varphi(6)$. Its discussion extends the test to translation parameters rescaled by $\lambda_{1}$ and to central elements of an abstract scaling monoid acting trivially. We take the reported counts as inputs for the growth analysis in Section 4.5 and re-derive every consequence with the arithmetic shown.

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

a unipotent shear with coefficient $c=1$ and a rotation by angle $\theta$. For the $n$-dimensional extension we use coordinate-plane shears $\phi_{ij}$ acting as $\phi_{ij}(x)=x+e_{i}x_{j}$ on the $i$-th coordinate, where $e_{i}$ is the $i$-th basis vector. A third model, nonlinear, is the translation $T(z,w)=(z+1,w)$ of $\mathbb{C}^{2}$, treated in Section 4.4.

### 3.3 Growth accounting for the Cayley–Dickson tower

For the non-associative setting, the prior version [12] reports $N_{\mathrm{oct}}=7$ associative quaternion rings in the octonions and $N_{\mathrm{sed}}=35$ in the sedenions, together with the dimension law of the Cayley–Dickson series: the $N$-th algebra $\mathrm{A}_{N}$ has $n=2^{N}$ basis elements. We treat the octonion-to-sedenion passage as one dimension-doubling step with dimensions $2^{3}=8$ and $2^{4}=16$. We define:

- the per-step growth exponent $g=\log_{2}\!\bigl(N_{\mathrm{sed}}/N_{\mathrm{oct}}\bigr)$;
- the ring density $\delta(A)=N(A)/\dim_{\mathbb{R}}(A)$ for a Cayley–Dickson algebra $A$;
- the density growth factor $\delta(\mathbb{S})/\delta(\mathbb{O})$.

All arithmetic appears in Section 4.5. The non-associative background for these algebras—the way octonionic non-associativity organizes into parameterized families of products—is documented in [11], which derives the torsion structure constants $T_{ijk}(X)$ on $S^{7}$; we use [11] only as this structural backdrop, not as a source of the counts.

### 3.4 Scaling-stability accounting

To compare the ratio rule with an applied stability certificate, we use the bounds of [10]: for a finite metric space $X\subset\mathbb{R}^{n}$ scaled by factors $s_{1},\dots,s_{n}>0$, the bottleneck distance between persistence diagrams satisfies $d_{B}(D,D_{S})\leq(s_{\max}-s_{\min})\cdot\operatorname{diam}(X)$, with the analogous bound $\delta_{k}=(s_{\max}-s_{\min})\cdot\operatorname{diam}_{k}(X)$ in homology degree $k$ and $W_{p}(D,D_{S})\leq\delta$ in Wasserstein distance. We evaluate these bounds for stated numerical assumptions in Section 4.6.

### 3.5 Discrete-scaling rigidity

If a scaling transformation has a discrete parameter group with cyclic image of order $k$, a scaling-compatible automorphism induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler's totient $\varphi(k)$. We evaluate $\varphi$ for small $k$ and interpret the case $k=2$ as a rigidity statement for order-two discrete scalings.

### 3.6 Computational conventions

All arithmetic is performed with exact rational numbers; intermediate results are kept as fractions and only final decimal approximations are displayed where required. No numerical rounding is introduced before the final step.

## 4. Analysis

### 4.1 Input inventory

Every number used below, with its source:

| Item | Value / expression | Source |
|------|-------------------|--------|
| Shear coefficient $c$ | $1$ (definition of $\phi_{\mathrm{uni}}$) | Section 3.2 |
| Anisotropic dilation entries | $\lambda_{1}=2$, $\lambda_{2}=3$ (chosen example) | Assumption |
| Scalar-dilation centrality factor | $1$ (no change) | derived in 4.3 |
| Jacobian determinant of a planar linear map | $\det J=\det(M)$; invariant under conjugation | derived in 4.3 |
| Translation coefficient after dilation | $1\mapsto\lambda_{1}$ | derived in 4.4 |
| Octonion associative ring count | $N_{\mathrm{oct}}=7$ | [12] |
| Sedenion associative ring count | $N_{\mathrm{sed}}=35$ | [12] |
| Growth ratio $r$ | $r=N_{\mathrm{sed}}/N_{\mathrm{oct}}=5$ | 4.5 |
| Per-step exponent $g$ | $g=\log_{2}5\approx2.321928$ | 4.5 |
| Octonion dimension | $D_{3}=2^{3}=8$ | [12] |
| Sedenion dimension | $D_{4}=2^{4}=16$ | [12] |
| Density $\delta(\mathbb{O})$ | $7/8=0.875$ | 4.5 |
| Density $\delta(\mathbb{S})$ | $35/16=2.1875$ | 4.5 |
| Density growth factor | $2.5$ | 4.5 |
| Stability bound inputs (assumption) | $s_{\max}-s_{\min}=1$, $\operatorname{diam}(X)=10$ | assumed, 4.6 |
| Totient values | $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$ | 4.7 |
| Face count of a $2$-dimensional simplicial cone | $F=4$ | 4.8 |

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

For a general anisotropic dilation $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ the same three-line computation yields the **ratio rule** $c'=\dfrac{\lambda_{1}}{\lambda_{2}}c$.

### 4.3 Triviality of scalar-dilation conjugation and Jacobian invariance

Let $S_{\lambda}(x)=\lambda x$ with $\lambda>0$.

**Shear.** $S_{\lambda}^{-1}(x,y)=(x/\lambda,y/\lambda)$. Applying $\phi_{\mathrm{uni}}$ gives $\bigl((x+y)/\lambda,\,y/\lambda\bigr)$. Applying $S_{\lambda}$ returns $(x+y,\,y)$. Hence
$$
S_{\lambda}\,\phi_{\mathrm{uni}}\,S_{\lambda}^{-1}=\phi_{\mathrm{uni}}\quad\forall\;\lambda>0.
$$

**Rotation.** The rotation matrix $R_{\theta}$ satisfies $S_{\lambda}R_{\theta}=R_{\theta}S_{\lambda}$ because $S_{\lambda}=\lambda I_{2}$ commutes with every $2\times2$ matrix. Consequently
$$
S_{\lambda}\,\phi_{\mathrm{rot}}\,S_{\lambda}^{-1}=\phi_{\mathrm{rot}}.
$$

**Jacobian determinant.** For any planar linear map $L$ with matrix $M$, $\det(M)$ is the Jacobian determinant $\operatorname{Jac}(L)$. Conjugation by $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ yields matrix $DMD^{-1}$, and
$$
\det(DMD^{-1})=\det(D)\det(M)\det(D^{-1})=\det(M),
$$
because $\det(D)\det(D^{-1})=1$. Therefore the Jacobian determinant is invariant under diagonal conjugation.

### 4.4 Translation parameters under anisotropic conjugation

Let $T(z,w)=(z+1,w)$ on $\mathbb{C}^{2}$ and $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$. Compute $D\,T\,D^{-1}$:

$$
D^{-1}(z,w)=\left(\frac{z}{\lambda_{1}},\frac{w}{\lambda_{2}}\right),\qquad
T\!\left(\frac{z}{\lambda_{1}},\frac{w}{\lambda_{2}}\right)=\left(\frac{z}{\lambda_{1}}+1,\;\frac{w}{\lambda_{2}}\right),
$$

$$
D\!\left(\frac{z}{\lambda_{1}}+1,\;\frac{w}{\lambda_{2}}\right)
=\left(\lambda_{1}\left(\frac{z}{\lambda_{1}}+1\right),\;\lambda_{2}\cdot\frac{w}{\lambda_{2}}\right)
=\left(z+\lambda_{1},\;w\right).
$$

Thus
$$
D\,T\,D^{-1}(z,w)=(z+\lambda_{1},\;w),
$$
and the translation coefficient $t=1$ is transformed as
$$
t\;\longmapsto\;t'=\lambda_{1}\,t=\lambda_{1}.
$$
The rule is analogous to the shear rule of Section 4.2, with the ratio $\lambda_{1}/\lambda_{2}$ replaced by the single factor $\lambda_{1}$, because the translation acts only on the first coordinate. With $\lambda_{1}=2$ the coefficient becomes $t'=2$; with $\lambda_{1}=1/2$ it becomes $t'=1/2$. The computation uses only the definition of $D$ and the explicit form of $T$; no additional data are introduced.

### 4.5 Growth of associative structure in the Cayley–Dickson tower

From [12] we take $N_{\mathrm{oct}}=7$ and $N_{\mathrm{sed}}=35$.

**Ratio.**
$$
r=\frac{N_{\mathrm{sed}}}{N_{\mathrm{oct}}}=\frac{35}{7}=5.
$$

**Per-step exponent.** One dimension-doubling step carries the algebra from dimension $2^{3}$ to dimension $2^{4}$, so the exponent per step is
$$
g=\log_{2}r=\log_{2}5=\frac{\ln 5}{\ln 2}\approx\frac{1.6094379}{0.6931472}\approx2.321928.
$$
The division gives $1.6094379/0.6931472=2.32192809\ldots$, rounded to six decimals as $2.321928$.

**Dimensions.** The dimension law of the Cayley–Dickson series, $\dim_{\mathbb{R}}\mathrm{A}_{N}=2^{N}$, gives
$$
D_{3}=2^{3}=8,\qquad D_{4}=2^{4}=16,\qquad \frac{D_{4}}{D_{3}}=2.
$$

**Densities.**
$$
\delta(\mathbb{O})=\frac{N_{\mathrm{oct}}}{D_{3}}=\frac{7}{8}=0.875,\qquad
\delta(\mathbb{S})=\frac{N_{\mathrm{sed}}}{D_{4}}=\frac{35}{16}=2.1875.
$$

**Density growth factor.**
$$
\frac{\delta(\mathbb{S})}{\delta(\mathbb{O})}
=\frac{35/16}{7/8}
=\frac{35}{7}\cdot\frac{8}{16}
=5\cdot\frac{1}{2}
=2.5.
$$

Thus the count of associative quaternion rings grows by a factor of $5$ across the octonion-to-sedenion step, the per-doubling exponent is $g\approx2.321928$, and the ring density per real dimension grows by exactly $2.5$, from $0.875$ to $2.1875$. All three numbers follow from the two counts $7$ and $35$ and the dimension law; no further input is used. The non-associative backdrop for these algebras—the organization of octonionic non-associativity into families of products parametrized by a point of $S^{7}$, with structure constants $[\delta_{i},\delta_{j}]=2T_{ijk}(X)\delta_{k}$—is documented in [11]; we use [11] only as this structural context, not as a source of the counts.

### 4.6 Scaling-stability accounting with a worked example

The bounds of [10] give a computable certificate for how far a non-uniform rescaling can move a topological descriptor: for scaling factors $s_{1},\dots,s_{n}>0$,
$$
d_{B}(D,D_{S})\leq\delta=(s_{\max}-s_{\min})\cdot\operatorname{diam}(X),
$$
with the homological extension $\delta_{k}=(s_{\max}-s_{\min})\cdot\operatorname{diam}_{k}(X)$ and the Wasserstein bound $W_{p}(D,D_{S})\leq\delta$.

**Worked example under stated assumptions.** We assume a dataset with $\operatorname{diam}(X)=10$ and scaling factors $s_{1}=1$, $s_{2}=2$, so that $s_{\max}-s_{\min}=2-1=1$. Then
$$
\delta=(s_{\max}-s_{\min})\cdot\operatorname{diam}(X)=1\cdot10=10.
$$
If instead the scaling is isotropic, $s_{1}=s_{2}=s$, then $s_{\max}-s_{\min}=0$ and
$$
\delta=0\cdot\operatorname{diam}(X)=0,
$$
so the bound certifies that the rescaling cannot move the persistence diagram at all. This is the persistence-diagram analogue of the conjugation test's triviality branch: anisotropy, measured by $s_{\max}-s_{\min}$, is exactly the quantity that converts a geometric scale ($\operatorname{diam}(X)$) into a bound on structural change. The ratio rule of Section 4.2 plays the same role for automorphism parameters, with $\lambda_{1}/\lambda_{2}$ replacing $s_{\max}/s_{\min}$ as the anisotropy measure; both frameworks certify triviality precisely in the isotropic case.

### 4.7 Discrete-scaling rigidity via Euler's totient

If a scaling transformation has a discrete parameter group with cyclic image of order $k$, a scaling-compatible automorphism induces multiplication by a unit of $\mathbb{Z}/k\mathbb{Z}$; the number of such units is Euler's totient $\varphi(k)$. Direct evaluation for small $k$:

- $\varphi(2)$: the units of $\mathbb{Z}/2\mathbb{Z}$ are $\{1\}$, so $\varphi(2)=1$.
- $\varphi(3)$: the units of $\mathbb{Z}/3\mathbb{Z}$ are $\{1,2\}$, so $\varphi(3)=2$.
- $\varphi(4)$: the units of $\mathbb{Z}/4\mathbb{Z}$ are $\{1,3\}$, so $\varphi(4)=2$.
- $\varphi(5)$: the units of $\mathbb{Z}/5\mathbb{Z}$ are $\{1,2,3,4\}$, so $\varphi(5)=4$.
- $\varphi(6)$: the units of $\mathbb{Z}/6\mathbb{Z}$ are $\{1,5\}$, so $\varphi(6)=2$.

Thus $\varphi(2)=1,\ \varphi(3)=2,\ \varphi(4)=2,\ \varphi(5)=4,\ \varphi(6)=2$. The case $k=2$ is a rigidity statement: a discrete scaling of order $2$ admits no nontrivial rescaling of its own parameter, because the only unit is the identity. Any automorphism compatible with an order-two discrete scaling is therefore forced to act trivially on the scaling parameter, a certificate of the form our test's centralization branch produces.

### 4.8 Face count of the two-ray cone

A $2$-dimensional simplicial cone has $\binom{2}{k}$ faces of dimension $k$, giving
$$
F=\binom{2}{0}+\binom{2}{1}+\binom{2}{2}=1+2+1=4.
$$
This count is the combinatorial fixed data of the two-ray configuration: the cone itself, its two rays, and the apex. It is the setting in which a ray-permuting automorphism acts, and the count is independent of any metric or scaling choice, which is why it survives the conjugation test unchanged.

## 5. Results

The explicit computations of Section 4 yield the following quantitative outcomes:

| Quantity | Value | Section |
|----------|-------|---------|
| Shear coefficient after anisotropic dilation $D=\operatorname{diag}(2,3)$ | $c'=\dfrac{2}{3}\approx0.666667$ | 4.2 |
| General shear rule under $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ | $c'=\dfrac{\lambda_{1}}{\lambda_{2}}\,c$ | 4.2 |
| Scalar-dilation effect on shear and rotation | No change (factor $1$) | 4.3 |
| Jacobian determinant under diagonal conjugation | Exact invariance (factor $1$) | 4.3 |
| Translation coefficient under $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ | $t'=\lambda_{1}\,t$ | 4.4 |
| Associative ring count growth ratio | $5$ | 4.5 |
| Per-step exponent $g$ | $2.321928$ (rounded to six decimals) | 4.5 |
| Density growth factor | $2.5$ (from $0.875$ to $2.1875$) | 4.5 |
| Stability bound, assumed $\operatorname{diam}(X)=10$, $s_{\max}-s_{\min}=1$ | $\delta=10$; $\delta=0$ if isotropic | 4.6 |
| Totient values $\varphi(2),\varphi(3),\varphi(4),\varphi(5),\varphi(6)$ | $1,2,2,4,2$ | 4.7 |
| Face count of the two-ray cone | $4$ | 4.8 |

Every number in the table is derived in the cited subsection from the inputs listed in Section 4.1, with the arithmetic shown. The stability bound of Section 4.6 is a worked evaluation of the theorem of [10] under stated assumptions, not a measurement.

## 6. Discussion

The conjugation test separates cleanly into two regimes, and the derivations of Section 4 show where the boundary lies. For linear planar maps, anisotropic dilations act by the ratio $\lambda_{1}/\lambda_{2}$ on shear coefficients and by $\lambda_{1}$ on translation coefficients, while scalar dilations act trivially; the Jacobian determinant is invariant under both. The boundary is therefore anisotropy itself, not linearity: the nonlinear translation of Section 4.4 obeys a parameter rule of the same character as the linear shear. What the derivations do not establish is any behavior beyond diagonal dilations and the specific model maps, and the limitations below name that boundary precisely.

**Limitations.** The result rests on the following assumptions, with sensitivity noted for each:

1. **Linear-map restriction.** The ratio rule is proved for the unipotent shear, the rotation, and the translation of $\mathbb{C}^{2}$ only. Polynomial automorphisms of higher degree are untouched; a degree-$2$ map could mix coordinates so that conjugation produces cross-terms rather than a clean parameter rescaling. The central claims are insensitive to this limitation as stated, but their scope is exactly the model maps.
2. **Two-dimensional anisotropy.** The explicit derivation uses a $2\times2$ diagonal matrix. In $n$ dimensions a coordinate-plane shear $\phi_{ij}$ should rescale by $\lambda_{i}/\lambda_{j}$ by the same three-line argument, but this is a projection, not a derivation here; the framework's sensitivity to higher-dimensional effects is untested.
3. **Two reported counts.** The growth analysis of Section 4.5 rests on $N_{\mathrm{oct}}=7$ and $N_{\mathrm{sed}}=35$ from [12]. Any revision of those counts changes the factor $5$, the exponent $2.321928$, and the density factor $2.5$ proportionally; the derivation itself is exact arithmetic on the inputs, so its correctness is independent of the counts' provenance, but its empirical content is not.
4. **Two levels of the tower.** The density growth factor $2.5$ is computed from exactly one step. Whether the factor persists at further doublings is an unverified hypothesis; no count at the $32$-dimensional level is available to us.
5. **Stability example is assumed, not measured.** The values $\operatorname{diam}(X)=10$ and $s_{\max}-s_{\min}=1$ in Section 4.6 are assumptions used to evaluate the bound of [10]; no dataset was involved.
6. **Discrete scalings of small order.** The totient analysis covers $k\le6$; larger cyclic groups introduce no new mechanism in the derivation, but their interpretation for specific structures is not worked out.

**Falsification conditions.** The main result is falsified by direct computation in three ways. First, if a recomputation of $D\,\phi_{\mathrm{uni}}\,D^{-1}$ for $D=\operatorname{diag}(2,3)$ produced a shear coefficient other than $2/3$, the ratio rule would be false. Second, if a diagonal conjugation changed the Jacobian determinant of a planar linear map, the invariance claim of Section 4.3 would be false. Third, if $35/7$ were not $5$ or $(35/16)/(7/8)$ were not $2.5$, the growth accounting would fail—but these are exact rational computations, so failure would indicate an input error, not an arithmetic one. An observation that a scalar dilation $S_{\lambda}$ failed to commute with a rotation would falsify the triviality branch.

**Open questions.** Does the ratio rule extend to polynomial automorphisms of degree $\geq2$, and if so, does the rule become a matrix of ratios over the jet coordinates? Can the anisotropy-to-bound mechanism of Section 4.6 be dualized, giving a lower bound on structural change from a given anisotropy? What is the combinatorial meaning of the counts $7=\binom{7}{1}$ and $35=\binom{7}{3}$, if any beyond coincidence? How does the centralization picture interact with conjugation actions whose representational complexity is known to be high, as in the negative representability results for $\operatorname{SL}_{2}(\mathbb{R})$ and $\operatorname{SL}_{n}(\mathbb{R})$, $n\geq4$, of [7]?

## 7. Practical Implications and Engineering Pathways

**(a) Users and decisions.** The primary users are implementers of normalization and reduction routines in computer-algebra systems, and mathematicians running classification arguments that quotient configuration spaces by scalings. The decision that changes: before quotienting by dilations or rescaling coordinates in a pipeline, the practitioner applies the three-question test of Section 3.1—check normalization, check centralization, and if the automorphism family is parameterized, apply the ratio rule $c'=(\lambda_{1}/\lambda_{2})\,c$ or certify triviality. A correct certification prevents downstream computations from inheriting a changed symmetry group; an incorrect one silently corrupts every subsequent invariant.

**(b) Readiness.** Against the NASA Technology Readiness Level definitions, this work is purely analytical and has not been peer reviewed: it is TRL 1–2. The derivations are explicit and checkable by hand (Sections 4.2–4.8), which supports the lower end of that band; no implementation, prototype, or empirical validation exists, and analytical work of this kind does not exceed TRL 3.

**(c) Smallest next test.** The smallest next computation that would de-risk or falsify the framework is a symbolic verification of the ratio rule beyond dimension two: compute $D\,\phi\,D^{-1}$ for $D=\operatorname{diag}(\lambda_{1},\lambda_{2},\lambda_{3})$ and a unipotent shear on a chosen coordinate plane, and for a unipotent with two independent shear coefficients, checking whether each coefficient rescales by the ratio of the corresponding dilation pair. The outcome that refutes the generalization is a conjugated coefficient that is not a monomial in the $\lambda_{i}$; the outcome that de-risks it is a full ratio table matching $c'_{ij}=(\lambda_{i}/\lambda_{j})\,c_{ij}$.

**(d) Binding constraints.** For any eventual software implementation, the binding constraints are, in order: symbolic exactness (the ratio $2/3$ must be carried as a rational, not a float, or the certification loses its proof status); the scope limit that the proved rule covers only the model maps of Section 3.2, so any application to higher-degree polynomial automorphisms is an extrapolation; and the data constraint that the growth claims rest on the two counts reported in [12], with no counts at further levels of the tower available to us. Whether the centralization branch extends to settings where conjugation actions resist low-complexity representation, as in the negative results of [7], is an open question, not a constraint we can quantify.

**(e) Order-of-magnitude projection (labeled).** Under the stated assumption P1—that the per-step factor $5$ persists at the next dimension doubling—the next hypothetical level would have $N=35\cdot5=175$ associative quaternion rings at dimension $2^{5}=32$, with density $175/32=5.46875$. This projection inherits P1's unverified persistence assumption and carries no error bar; it is stated only to mark what a future count would test.

**(f) Risks and misuse paths.** The main misuse is overextension: citing the ratio rule as if it applied to nonlinear or infinite-dimensional automorphism families, or citing the density growth $2.5$ as a general law of non-associative structure, when it is computed from exactly two levels. A second misuse is reading the identity $7=\binom{7}{1}$, $35=\binom{7}{3}$ as a structural theorem; it is an arithmetic observation about two numbers. Documentation of any implementation should state the proved scope explicitly.

## 8. Conclusion

We have introduced a three-part conjugation test that determines when a scaling transformation normalizes, centralizes, or rescales the parameters of an automorphism, and we have carried out its quantitative branch with explicit arithmetic. Anisotropic dilations rescale shear coefficients by the ratio of diagonal entries ($c'=2/3$ for $D=\operatorname{diag}(2,3)$) and translation coefficients by $\lambda_{1}$; scalar dilations act trivially on shears and rotations; Jacobian determinants are invariant under diagonal conjugation. In the Cayley–Dickson tower, the count of associative quaternion rings grows by a factor of $5$ across the octonion-to-sedenion step, with per-doubling exponent $\log_{2}5\approx2.321928$ and density growth factor exactly $2.5$. The stability reading connects the same anisotropy mechanism to the persistence-diagram bound of [10], and the totient value $\varphi(2)=1$ certifies rigidity for order-two discrete scalings. The framework is limited to the model maps treated here and to two levels of the tower, and its predictions are falsifiable by direct symbolic computation. Future work should test the ratio rule in higher dimensions, seek counts at further Cayley–Dickson levels, and integrate the test as an automated check in symbolic-computation pipelines.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.55.14). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 10 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] The conjugation action in completed group rings. arXiv:1903.03080. https://arxiv.org/abs/1903.03080
[2] The reciprocal character of the conjugation action. arXiv:2003.06150. https://arxiv.org/abs/2003.06150
[3] Invariant relationships deriving from classical scaling transformations. arXiv:1008.4086. https://arxiv.org/abs/1008.4086
[4] On the conjugation action for quantum general linear groups. arXiv:2209.01897. https://arxiv.org/abs/2209.01897
[5] Notes on partial conjugation. arXiv:1110.1689. https://arxiv.org/abs/1110.1689
[6] Approximate solutions and scaling transformations for quadratic solitons. arXiv:patt-sol/9909001. https://arxiv.org/abs/patt-sol/9909001
[7] Topological group actions by group automorphisms and Banach representations. arXiv:2110.01386. https://arxiv.org/abs/2110.01386
[8] A representation on the labeled rooted forests. arXiv:1506.01543. https://arxiv.org/abs/1506.01543
[9] Topological K-theory of the group C*-algebra of a semi-direct product Z^n rtimes Z/m for a free conjugation action. arXiv:1109.1440. https://arxiv.org/abs/1109.1440
[10] Topology-Preserving Scaling in Data Augmentation. arXiv:2411.19512. https://arxiv.org/abs/2411.19512
[11] Non-Associativity in the Clifford Bundle on the Parallelizable Torsion 7-Sphere. arXiv:1209.0385. https://arxiv.org/abs/1209.0385
[12] https://papers.qnfo.org/papers/automorphisms-and-scaling-transformations-a-re-entry-analysis-across-algebraic-g. QNFO: Automorphisms and Scaling Transformations: Conjugation Action, Parameter Rescaling, and Growth of Associative Structure.
