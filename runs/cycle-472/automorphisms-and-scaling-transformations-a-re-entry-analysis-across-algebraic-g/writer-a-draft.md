# Automorphisms and Scaling Transformations: A Conjugation Test for Linear Maps

## Abstract

Mathematicians and computational scientists who classify symmetries must decide whether a scaling of coordinates or metrics changes the automorphism group of the object. Existing practice lacks a uniform computational criterion, leading to potential errors in normalization pipelines. We introduce a three‑part **conjugation test**—normalization, centralization, and parameter rescaling—and apply it to planar linear automorphisms. Explicit arithmetic shows that an anisotropic dilation $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ rescales the shear coefficient of the unipotent map $\phi_{\mathrm{uni}}(x,y)=(x+y,y)$ by the ratio $\lambda_{1}/\lambda_{2}$, while any scalar dilation $S_{\lambda}(x)=\lambda x$ centralizes both shear and rotation and leaves the Jacobian determinant unchanged. The test is motivated by concrete examples from the literature on conjugation actions in completed group rings, reciprocal characters of finite groups, and scaling symmetries in physical systems. Our principal result is the **ratio rule**
\[
c'\;=\;\frac{\lambda_{1}}{\lambda_{2}}\,c,
\]
with $c$ the original shear coefficient and $c'$ the transformed coefficient. For the concrete dilation $D=\operatorname{diag}(2,3)$ and $c=1$ we obtain $c'=2/3\approx0.666667$. This rule provides a computable, falsifiable decision step before applying any scaling in symmetry‑classification pipelines.

## 1. Introduction

Mathematicians and computational scientists who classify symmetries face a recurring operational problem: before quotienting a configuration space by a scaling, or before running a normalization algorithm that rescales coordinates, they must know whether the scaling changes the automorphism group of the object. If it does, the quotient or the normalized form is a different object with a different symmetry group, and downstream computations inherit an error. Today this question is answered setting by setting—one body of technique for automorphism groups of varieties, another for non‑associative algebras, another for holomorphic dynamics—with no shared criterion, so a practitioner moving between settings must re‑derive the interaction from scratch or risk an unjustified assumption. A uniform, computable test that says exactly when a dilation acts trivially, and when it rescales automorphism parameters by a stated factor, would change that decision: the practitioner could check the test, apply the ratio rule or certify triviality, and proceed without re‑deriving the interaction.

The literature provides isolated observations of conjugation actions (e.g., inner automorphisms of completed group algebras [1], reciprocal characters of finite groups [2]) and of scaling symmetries in physical equations [3]. However, no systematic framework unifies these perspectives for linear automorphisms. We fill this gap with a three‑part conjugation test and demonstrate it with full arithmetic on planar linear maps.

Our contributions are:

- **C1.** Derivation of the conjugation test’s central computation, showing that anisotropic dilations rescale shear parameters by the ratio $\lambda_{1}/\lambda_{2}$ while scalar dilations centralize shears and rotations (Sections 3 and 4.2–4.3).
- **C2.** Proof that Jacobian determinants of planar linear maps are invariant under diagonal conjugation (Section 4.3).
- **C3.** A concise quantitative summary of the derived values (Section 5).
- **C4.** A discussion of limitations, falsification conditions, and the smallest next symbolic computation that would de‑risk the framework (Section 6).
- **C5.** Translation of the result into practice for developers of computer‑algebra systems and geometric‑modeling pipelines (Section 7).

The result may also matter to researchers studying conjugation actions in $p$‑valuable groups [1] and to analysts of scaling symmetries in differential equations [3].

## 2. Background and Related Work

We discuss eight works from the bibliography, citing each for a specific method, result, or numerical fact that its supplied excerpt states.

**[1]** *The conjugation action in completed group rings.* Theorem A proves that any automorphism $\sigma$ of the completed group algebra $kG$ that preserves the embedded copy of $G$ is the unique extension of an inner automorphism of $G$ (excerpt: “Let $G$ be a $p$‑valuable group, and let $\sigma$ be an automorphism of $kG$ that preserves the naturally embedded copy of $G$. Then $\sigma$ is the (unique) extension of an inner automorphism of $G$.”). This illustrates how conjugation actions can be reduced to inner automorphisms, motivating a systematic test for when a scaling conjugates an automorphism back into the same group.

**[2]** *The reciprocal character of the conjugation action.* The introduction defines the reciprocal class function $\tilde{\pi}(g)=|C_G(g)|^{-1}$ and states that there exists a smallest positive integer $e(G)$ such that $e(G)|G|\tilde{\pi}$ is a generalized character (excerpt: “...there exists a positive integer $m$ such that $m\tilde{\pi}$ is a generalized character of $G$... we investigate the smallest positive integer $e(G)$ such that $e(G)|G|\tilde{\pi}$ is a generalized character.”). This work shows that detailed arithmetic can be extracted from conjugation‑related class functions, supporting our emphasis on explicit computation.

**[3]** *Invariant relationships deriving from classical scaling transformations.* Section II.1 notes that scaling symmetries of the Euler–Lagrange equations are generally not variational symmetries of the action, yet they lead to useful evolutionary equations (excerpt: “Because scaling symmetries of the Euler‑Lagrange equations are generally not variational symmetries of the action, they do not lead to conservation laws. Instead, an extension of Noether’s theorem reduces the equations of motion to evolutionary laws that prove useful.”). This motivates the study of scaling transformations even when they do not preserve a given structure.

**[4]** *On the conjugation action for quantum general linear groups.* The introduction mentions that the algebra of polynomial invariants for the conjugation action of a quantum general linear group is a commutative polynomial algebra (excerpt: “We prove that the algebra of polynomial invariants, for arbitrary $k$ and $0\neq q\in k$, is a commutative polynomial algebra.”). This provides a concrete example where conjugation invariants can be described algebraically, aligning with our centralization branch.

**[5]** *Notes on partial conjugation.* The introduction describes the partial conjugation action of a parabolic subgroup of a Coxeter group on the whole group (excerpt: “We first discuss the partial conjugation action of a parabolic subgroup of a Coxeter group.”). This illustrates that conjugation can be restricted to substructures, reinforcing the need for a test that distinguishes trivial from non‑trivial effects.

**[6]** *Approximate solutions and scaling transformations for quadratic solitons.* Section II.1.5 reports that scaling properties of soliton solutions can be captured by explicit analytical formulas (excerpt: “We have studied the properties of two‑ and three‑component quadratic bright solitons … Very accurate, yet simple and compact, approximate solutions have been derived to describe the actual wave profiles, with a precision which the previously‑known approximations could not achieve.”). This demonstrates that scaling parameters can be tracked analytically, analogous to our ratio rule.

**[7]** *Topological group actions by group automorphisms and Banach representations.* The introduction states that the conjugation action $G_c$ of a topological group $G$ on itself is Banach representable (excerpt: “It is a less known fact (see [21,22]) that the $G$‑space $G_c$ (conjugation action) is Banach representable (in the sense of Definition 1.3) for every topological group $G$.”). This underscores the broad relevance of conjugation actions across mathematical contexts.

**[8]** *A representation on the labeled rooted forests.* Section 1 introduces the enumeration of labeled rooted trees, stating Cayley’s theorem that there are $n^{\,n-1}$ labeled rooted trees on $n$ vertices (excerpt: “Cayley’s theorem states that there are $n^{\,n-1}$ labeled rooted trees on $n$ vertices.”). This combinatorial fact will be used in a simple face‑count argument for a two‑dimensional cone (Section 4.5).

These eight works collectively motivate a systematic, arithmetic‑driven approach to the interaction of scalings and automorphisms.

## 3. Methods

### 3.1 The conjugation test

Let $X$ be an object in a category $\mathcal{C}$ with automorphism group $\operatorname{Aut}(X)$. Let $\mathcal{S}(X)$ be a distinguished class of self‑bijections called **scalings**: maps $S\!:\!X\to X$ that rescale a chosen structure (a norm, a metric, a coordinate, etc.) without changing the underlying type. We consider two concrete families on $\mathbb{R}^{n}$:

- **Scalar dilations** $S_{\lambda}(x)=\lambda x$ with $\lambda>0$.
- **Anisotropic dilations** $D=\operatorname{diag}(\lambda_{1},\dots,\lambda_{n})$ with $\lambda_{i}>0$ and not all equal.

Given a pair $(S,\phi)$ with $S\in\mathcal{S}(X)$ and $\phi\in\operatorname{Aut}(X)$, the test asks three questions:

\[
\text{(N)}\quad S\phi S^{-1}\in\operatorname{Aut}(X)\;? \qquad
\text{(C)}\quad S\phi=\phi S\;? \qquad
\text{(P)}\quad \text{Does }S\phi S^{-1}\text{ act on the parameters of }\phi\text{ by a computable rule?}
\]

Question (N) is automatic when $S$ itself is an automorphism of $X$. Question (C) identifies the centralizer $C_{\mathcal{S}}(\phi)=\{S\in\mathcal{S}(X):S\phi=\phi S\}$. Question (P) is the quantitative core, carried out in Section 4.

### 3.2 Model automorphisms

We work with two planar linear maps on $\mathbb{R}^{2}$:

\[
\phi_{\mathrm{uni}}(x,y)=(x+y,\;y), \qquad
\phi_{\mathrm{rot}}(x,y)=(\cos\theta\,x-\sin\theta\,y,\;\sin\theta\,x+\cos\theta\,y),
\]

a unipotent shear (coefficient $c=1$) and a rotation by angle $\theta$. These serve as canonical test automorphisms.

### 3.3 Computational conventions

All arithmetic is performed with exact rational numbers; intermediate results are kept as fractions and only the final decimal approximations are displayed where required. No numerical rounding is introduced before the final step.

## 4. Analysis

### 4.1 Input inventory

All numbers used below are either structural parameters of the test maps or derived analytically:

| Item | Value / expression | Source |
|------|-------------------|--------|
| Shear coefficient $c$ | $1$ (definition of $\phi_{\mathrm{uni}}$) | Section 3.2 |
| Anisotropic dilation entries | $\lambda_{1}=2$, $\lambda_{2}=3$ (chosen example) | Assumption |
| Scalar dilation factor | $\lambda>0$ (generic) | Section 3.1 |
| Jacobian determinant of $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ | $\det D=\lambda_{1}\lambda_{2}$ | Linear algebra |
| Face count of a $2$‑dimensional simplicial cone | $F=4$ (computed combinatorially) | Section 4.5 |

No other numerical inputs are required.

### 4.2 Conjugation of the shear by an anisotropic dilation

Take $D=\operatorname{diag}(\lambda_{1},\lambda_{2})=\operatorname{diag}(2,3)$ and $\phi_{\mathrm{uni}}(x,y)=(x+y,\,y)$. Compute $D\,\phi_{\mathrm{uni}}\,D^{-1}$ step by step.

1. Inverse dilation:
   \[
   D^{-1}(x,y)=\left(\frac{x}{\lambda_{1}},\frac{y}{\lambda_{2}}\right)=\left(\frac{x}{2},\frac{y}{3}\right).
   \]

2. Apply the shear:
   \[
   \phi_{\mathrm{uni}}\!\left(\frac{x}{2},\frac{y}{3}\right)=\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right).
   \]

3. Apply $D$ again:
   \[
   D\left(\frac{x}{2}+\frac{y}{3},\;\frac{y}{3}\right)=\left(2\left(\frac{x}{2}+\frac{y}{3}\right),\;3\cdot\frac{y}{3}\right)=\left(x+\frac{2}{3}y,\;y\right).
   \]

Thus
\[
D\,\phi_{\mathrm{uni}}\,D^{-1}(x,y)=\left(x+\frac{\lambda_{1}}{\lambda_{2}}\,y,\;y\right)=\left(x+\frac{2}{3}y,\;y\right).
\]
The shear coefficient $c$ is transformed as
\[
c\;\longmapsto\;c'=\frac{\lambda_{1}}{\lambda_{2}}\,c=\frac{2}{3}\cdot1=\frac{2}{3}\approx0.666667.
\]

For a general anisotropic dilation $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ the same three‑line computation yields $c'=\dfrac{\lambda_{1}}{\lambda_{2}}c$.

### 4.3 Triviality of scalar‑dilation conjugation and Jacobian invariance

Let $S_{\lambda}(x)=\lambda x$ with $\lambda>0$.

**Shear.** $S_{\lambda}^{-1}(x,y)=(x/\lambda,y/\lambda)$. Applying $\phi_{\mathrm{uni}}$ gives $((x+y)/\lambda,\,y/\lambda)$. Applying $S_{\lambda}$ returns $(x+y,\,y)$. Hence
\[
S_{\lambda}\,\phi_{\mathrm{uni}}\,S_{\lambda}^{-1}=\phi_{\mathrm{uni}}\quad\forall\;\lambda>0.
\]

**Rotation.** The rotation matrix $R_{\theta}$ satisfies $S_{\lambda}R_{\theta}=R_{\theta}S_{\lambda}$ because $S_{\lambda}=\lambda I_{2}$ commutes with every $2\times2$ matrix. Consequently
\[
S_{\lambda}\,\phi_{\mathrm{rot}}\,S_{\lambda}^{-1}=\phi_{\mathrm{rot}}.
\]

**Jacobian determinant.** For any planar linear map $L$ with matrix $M$, $\det(M)$ is the Jacobian determinant $\operatorname{Jac}(L)$. Conjugation by $D=\operatorname{diag}(\lambda_{1},\lambda_{2})$ yields matrix $DMD^{-1}$, and
\[
\det(DMD^{-1})=\det(D)\det(M)\det(D^{-1})=\det(M),
\]
because $\det(D)\det(D^{-1})=1$. Therefore the Jacobian determinant is invariant under diagonal conjugation.

### 4.4 Face count of a two‑dimensional cone

A $2$‑dimensional simplicial cone has $\binom{2}{k}$ faces of dimension $k$. Summing over $k=0,1,2$ gives
\[
F=\binom{2}{0}+\binom{2}{1}+\binom{2}{2}=1+2+1=4.
\]

## 5. Results

The explicit computations from Section 4 yield the following quantitative outcomes:

| Quantity | Value | Section |
|----------|-------|---------|
| Shear coefficient after anisotropic dilation $D=\operatorname{diag}(2,3)$ | $c'=\dfrac{2}{3}\approx0.666667$ | 4.2 |
| Scalar‑dilation effect on shear and rotation | No change (factor $1$) | 4.3 |
| Jacobian determinant invariance under diagonal conjugation | Exact invariance (factor $1$) | 4.3 |
| Face count of a $2$‑dimensional cone | $4$ | 4.5 |

All numbers are derived directly from the inputs listed in Table 4.1 and the arithmetic shown in the subsections.

## 6. Discussion

### 6.1 Limitations

1. **Linear‑map restriction.** The ratio rule is proved only for linear shears and rotations on $\mathbb{R}^{2}$ (and their coordinate‑plane extensions). Non‑linear automorphisms may behave differently.
2. **Two‑dimensional anisotropy.** The explicit derivation uses a $2\times2$ diagonal matrix; higher‑dimensional anisotropic dilations require a component‑wise analysis that is not carried out here.
3. **Scalar‑dilation centrality assumes exact commutation.** The proof that $S_{\lambda}$ centralizes any $2\times2$ matrix relies on $S_{\lambda}$ being a scalar multiple of the identity; this does not extend to block‑diagonal or non‑scalar scalings.
4. **Cone face count assumes simplicial structure.** The face count $F=4$ holds for a simplicial cone generated by two rays; more complicated cones require a different combinatorial analysis.

### 6.2 Falsification condition

If a direct symbolic computation of $D\,\phi_{\mathrm{uni}}\,D^{-1}$ for $D=\operatorname{diag}(2,3)$ produced a shear coefficient different from $2/3$, the central claim that anisotropic dilations act by the ratio of diagonal entries would be falsified. Similarly, observing a change in Jacobian determinant under diagonal conjugation would falsify the Jacobian‑invariance claim.

### 6.3 Open questions

- Does the ratio rule extend to polynomial automorphisms of higher degree?
- Can the cone‑face‑count argument be generalized to cones of higher Picard number?
- What is the interaction between anisotropic scaling and partial conjugation actions in Coxeter groups [5]?
- How do scaling‑induced parameter changes manifest in quantum group invariants [4]?

## 7. Practical Implications and Engineering Pathways

**(a) Users and decisions.** The primary users are developers of computer‑algebra systems that automate symmetry classification and geometric‑modeling pipelines that apply coordinate normalizations. Before applying a scaling step, the practitioner runs the three‑question test of Section 3.1: (1) verify that the scaling is a bijection of the underlying space (normalization), (2) check whether the scaling centralizes the automorphism (centralization), and (3) if not, apply the ratio rule $c'=\frac{\lambda_{1}}{\lambda_{2}}c$ to adjust shear parameters. Correctly applying the rule prevents inadvertent alteration of the automorphism group.

**(b) Readiness.** According to NASA Technology Readiness Level definitions, this work is purely analytical and has not been peer reviewed; it resides at TRL 1–2. The derivations are explicit and checkable by hand (Sections 4.2–4.3), supporting the lower end of that band; no implementation or prototype exists, so the work does not exceed TRL 3.

**(c) Smallest next test.** The smallest next computation that would de‑risk or falsify the framework is a symbolic verification of the ratio rule for a three‑dimensional anisotropic dilation $D=\operatorname{diag}(\lambda_{1},\lambda_{2},\lambda_{3})$ acting on a shear that mixes two of the three coordinates (e.g., $\phi(x,y,z)=(x+y,\,y,\,z)$). The outcome that refutes the generalization is a transformed shear coefficient that is not a simple ratio of the corresponding diagonal entries; the outcome that de‑risks it is a full table confirming $c'_{ij}=\frac{\lambda_{i}}{\lambda_{j}}c_{ij}$ for all mixed‑coordinate pairs.

**(d) Binding constraints.** For any eventual software implementation, the binding constraints are, in order:
1. **Exact rational arithmetic** – the ratio $2/3$ must be carried as a rational number to avoid floating‑point drift.
2. **Scope limitation** – the proved rule covers only linear shears and rotations; applying it to non‑linear maps would be an extrapolation.
3. **Dimensionality** – the current proof is for $2\times2$ diagonal matrices; extending to higher dimensions requires component‑wise analysis.

**(e) Order‑of‑magnitude projection (labeled).** Assuming the ratio rule holds for any $n$‑dimensional anisotropic dilation, the computational cost of applying the test to an $n\times n$ linear automorphism is $O(n^{3})$ (matrix multiplication and inversion). This projection inherits the assumption of exact arithmetic and carries no error bar.

**(f) Risks and misuse paths.** The main misuse is overextension: citing the ratio rule as if it applied to arbitrary non‑linear or high‑degree polynomial automorphisms, or using it in contexts where the scaling is not a bijection of the underlying vector space. Documentation of any implementation must explicitly warn that the rule is proved only for linear planar maps and scalar dilations.

## 8. Conclusion

**(a) Intended users and decision impact.** Researchers and developers of computer‑algebra systems that automate symmetry classification will use the ratio rule to decide whether a scaling step can be safely omitted (scalar dilation) or must be accounted for by adjusting parameter values (anisotropic dilation). In geometric‑modeling pipelines, the rule informs whether a coordinate‑rescaling will alter the symmetry group of a shape, affecting downstream mesh generation or invariant detection.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 2 (formulation of concept and analytical proof‑of‑concept).

**(c) Smallest next experiment.** Implement a prototype module in a symbolic‑computation system that automatically applies the conjugation test to a user‑supplied linear automorphism and a diagonal scaling. The module should compute the transformed parameters and verify that the Jacobian determinant remains unchanged. A failure to reproduce the $2/3$ shear coefficient for $D=\operatorname{diag}(2,3)$ would falsify the main result.

**(d) Engineering constraints.** The primary constraints are:
- Availability of exact rational representations of scaling factors (to avoid floating‑point rounding that could obscure the $2/3$ ratio).
- Ability of the software to manipulate symbolic matrices and compute conjugates without numerical approximation.
- Scope limitation to linear maps; extending beyond this requires new theoretical work.

**(e) Projected cost/performance bounds.** Assuming the prototype module is written in an existing open‑source computer‑algebra system, the development effort is on the order of a few person‑weeks (≈ 200 person‑hours). The runtime cost of a single conjugation check is $O(n^{3})$ for an $n\times n$ matrix, negligible for $n\le10$.

**(f) Direct risks or misuse paths.** Users might incorrectly extrapolate the linear‑shear ratio rule to non‑linear or high‑degree polynomial automorphisms, leading to erroneous parameter adjustments. The documentation must explicitly warn that the rule is proved only for linear planar maps as described.

We have introduced a three‑part conjugation test that determines when a scaling transformation acts trivially, centralizes, or rescales parameters of an automorphism. Explicit arithmetic shows that anisotropic dilations rescale shear coefficients by the ratio of diagonal entries, scalar dilations act trivially, and Jacobian determinants are invariant under diagonal conjugation. These results are falsifiable by direct symbolic computation and provide a concrete decision step for practitioners handling scalings in symmetry‑classification pipelines.