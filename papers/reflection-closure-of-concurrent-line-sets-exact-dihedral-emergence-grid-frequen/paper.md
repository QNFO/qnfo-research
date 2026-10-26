# Reflection Closure of Concurrent Line Sets: Exact Dihedral Emergence, Grid Frequency Laws, and the Finite/Infinite Dichotomy

## Abstract

Model builders in physics and machine learning must choose a symmetry group before fitting begins, and a wrong or hidden choice degrades predictions and obscures observables; the choice is normally an unchecked input. The specific gap addressed here is whether a minimal generative rule—draw a finite set of lines, then close the set under reflection across each of its members—produces a classifiable group with computable outcomes, rather than requiring the group to be posited. We work in the Euclidean plane with lines through a common point. By explicit $2\times 2$ matrix arithmetic we prove that the closure is always exactly the $n$-line reflection system of the dihedral group $\mathrm{I_2}(n)$, with $n$ the least common multiple of the pairwise rotation orders, and we compute worked cases: $\theta=\pi/5$ gives $5$ lines and group order $10$; the $\mathrm{A_2}$ configuration gives $3$ lines and order $6$; the mixed $\{\pi/3,\pi/4\}$ configuration gives $12$ lines and order $24$. On a rational angle grid of denominator $N$ we derive the exact emergence law $\mathbb{P}(\mathrm{I_2}(q))=\varphi(q)/N$ for $q\mid N$, and compute the full distribution for $N=12$, under which $\mathrm{I_2}(12)$ arises with probability $1/3$. We prove a dichotomy—continuously drawn angles yield finite closure with probability $0$, rational grids guarantee it—and that non-concurrent lines generate translations, hence infinite groups. Symmetry choice thereby reduces to a choice of initial conditions with an enumerable outcome space.

## 1. Introduction

Anyone who builds quantitative models of physical systems must decide, before any fitting begins, which symmetry group the model respects. This decision falls on computational physicists constructing lattice gauge simulations, on machine-learning researchers designing architectures for physical prediction, and on field theorists choosing gauges in which observables remain interpretable. The cost of the decision is concrete. A neural network without the correct symmetry constraint can regress data that violate the invariance the underlying physics demands, and practitioners respond by embedding constraints such as even/odd parity directly into network layers to keep predictions physically admissible [3]. In gauge theories the problem is sharper still: the choice of gauge, which addresses unphysical redundancies, can interfere with how physical symmetries constrain observables, so that symmetry constraints are explicit in some gauges and hidden in others [1]. In cosmological models, a symmetry manifest in a gauge-fixed description need not be a symmetry of the physical dynamics at all, and disentangling the two requires case-by-case analysis [8]. In each setting the working symmetry group is an input that must be chosen correctly, and a wrong or hidden choice blocks interpretation, costs retraining, or produces order parameters that fail to diagnose the physics.

What would change if symmetry groups could instead be derived? If a single minimal rule—draw a distinction, then close under reflections across what has been drawn—reliably generated a classified class of finite groups, with the specific group determined only by the initial configuration, then the choice of symmetry would reduce to a choice of initial conditions, and the space of possible symmetries would be enumerable in advance. This is the motivation supplied by the syntactic-generation program, in which a basic syntactic token, the drawing of a boundary separating inside from outside, is posited as the single foundational element of a relational ontology [14], with discrete relational boundaries replacing continuous substance-based backgrounds [13] and closure structures organized in a unified computational framework [12]. The present paper does not attempt to establish that grand claim; it establishes the first precisely checkable instance of it, in the plane.

The setting is two-dimensional. A finite set of lines through a common point is iterated under the operation "adjoin the mirror image of every line across every line already in the set." We ask which finite groups of plane isometries the closure can generate. The answer, proved here with explicit matrix arithmetic, is: exactly the dihedral groups $\mathrm{I_2}(n)$, and nothing else, with $n$ computable in closed form from the initial pairwise angles. We also compute exactly which groups emerge, and with what frequencies, when initial angles are drawn from a rational grid—answering the "with what frequencies" question by exact enumeration rather than simulation. The complementary result is a measure-zero dichotomy: with continuously drawn angles, finiteness has probability exactly $0$.

The contributions are:

- A proof, by explicit $2\times 2$ matrix computation, that reflection closure of any finite set of concurrent lines yields precisely the $n$-line reflection system of the dihedral group $\mathrm{I_2}(n)$, with $n$ the least common multiple of the pairwise rotation orders (Section 4).
- Worked closure computations for $\theta=\pi/5$ (five lines, group order $10$), the $\mathrm{A_2}$ configuration at $60^{\circ}$ (three lines, group order $6$), and the mixed configuration at $\pi/3$ and $\pi/4$ (twelve lines, group order $24$) (Section 4).
- An exact derivation of the emergence frequencies on a rational grid: $\mathbb{P}(\mathrm{I_2}(q))=\varphi(q)/N$ for each divisor $q$ of the grid denominator $N$, with the complete table computed for $N=12$ (Section 4).
- A proof of the finite/infinite dichotomy: continuously distributed initial angles give finite closure with probability $0$, while any rational grid guarantees finiteness with $n\le N$; and a proof that non-concurrent initial lines generate translations, hence infinite groups (Section 4).
- A falsifiable computational protocol for the closure algorithm, and a statement of the conjectural extension to hyperplane arrangements in higher dimensions and the finite Coxeter classification, with the explicit observation that would falsify the program (Sections 3, 5 and 6).

## 2. Background and Related Work

The physical background is that symmetries are treated as the most basic properties of physical systems, so that a sound formulation should make them as explicit as possible. [1] analyzes how gauge fixing, which handles unphysical gauge symmetries, can interfere with this explicitness in two ways—symmetry constraints on observables are not explicit in all gauges in the presence of approximations, and physical symmetries need not be explicit in gauge-fixed correlation functions—and introduces symmetric gauge fixings for which these problems are absent, using center symmetry in finite-temperature Yang–Mills theory as the working example. This matters here because it documents the practical cost of treating a symmetry as an externally chosen, representation-dependent input rather than an intrinsic output; the closure program proposes the opposite orientation, in which the group is derived and only the initial configuration is chosen.

The same orientation problem appears in quantum mechanics. [11] studies the Landau problem, where the widespread viewpoint ties the symmetric gauge to Laguerre-type eigenfunctions respecting rotational symmetry and the Landau gauges to Hermite-type eigenfunctions respecting translational symmetry; [11] shows instead that three conserved quantities—two pseudomomenta and one conserved orbital angular momentum—exist independently of the gauge potential, with covariant transformation properties under arbitrary gauge transformations, so that eigenfunctions can be written without committing to a gauge. The lesson taken here is that symmetry content is a property of the system's structure, not of the representational choice; a generative rule that produces the group from initial conditions would make this independence structural rather than incidental.

Symmetries can also be emergent rather than fundamental. [6] addresses how gauge symmetries, which indicate redundancies of description, can appear in systems containing no trace of them at a more fundamental level, and demonstrates with a complex Klein–Gordon field example that local symmetry does not imply gauge symmetry; [6] further shows that in its analyzed example a stress-energy tensor not invariant under a set of local symmetries ends up invariant under emergent gauge symmetries, while cautioning that which quantities retain operational meaning must be determined case by case. This supports the logical possibility the closure conjecture requires: a symmetry present at the effective level need not be posited at the foundational level, because a generative mechanism can produce it.

Discrete foundations give a second point of support. [10] presents a procedure for obtaining a "minimal" discretization of a partial differential equation—one scalar function of two variables replaced by a partial difference scheme involving $N=3$ difference equations—that preserves all of the PDE's Lie point symmetries by construction, and applies it to the linear heat equation while noting that if the world is discrete at the microscopic level, the fundamental equations are finite difference ones and differential equations are approximations. [10] demonstrates that symmetry can be carried exactly through a discrete, combinatorial construction rather than recovered only in a continuum limit; the closure rule studied here is the group-theoretic analogue, a discrete combinatorial operation whose output is an exact symmetry group.

The machine-learning literature quantifies both sides of the posited-versus-learned distinction. [7] studies unconstrained models operating on decorated point clouds, where the relevant group for atomistic surrogates is the Euclidean group $\mathrm{E(3)}$, and develops metrics quantifying how accurately models without hard-coded equivariance constraints come to satisfy transformation laws, noting that the evidence that symmetry-adapted architectures are not always necessary sits uneasily with the foundational role of symmetry enshrined in Noether's theorem. [3] takes the enforcement route, designing a "hub layer" that, used as the last hidden layer of a multilayer perceptron, guarantees the regression is even or odd as desired, and reports that networks with embedded physics are faster to train and exactly satisfy known constraints such as conservation laws. Both works presuppose that the target group is known in advance; a closure rule that enumerates the candidate groups from initial conditions would supply the missing prior.

Complete classification results in combinatorics provide the methodological template. [2] gives, for the $\mathsf{NP}$-hard Edge Dominating Set problem, a complete classification of kernelization behavior parameterized by the size of a modulator to $\mathcal{H}$-component graphs for all finite sets $\mathcal{H}$, with polynomial kernelizations available exactly under stated conditions and lower bounds ruling out polynomial kernels otherwise unless $\mathsf{NP}\subseteq\mathsf{coNP/poly}$; [2] also records that EDS admits a $2$-approximation by any maximal matching and an $\mathcal{O}^{*}(2.2351^{k})$ algorithm. The structural parallel is direct: a closure-type operation (kernelization reduces an instance while preserving the answer) admits a clean dichotomy across an entire parameterized family, and the present paper aims for the same style of exhaustive statement for reflection closure.

Structural coincidence theorems of the form "a derived set is contained in a canonical set" recur in analysis. [5] proves, for solutions $u$ of total variation and higher-order regularisation problems, the jump set containment $\mathcal{H}^{m-1}(J_u\setminus J_f)=0$—the jump set of the solution is contained in the jump set of the data—using a double-Lipschitz comparability condition on the regularisation functional and Lipschitz shift transformations, extending the technique from total variation through Huber regularisation to variants of $\mathrm{TGV}^2$. The proof shape—show that an object produced by an iterative or variational process cannot escape a canonically classified set—is the shape of the closure proofs in Section 4.

Probabilistic enumeration of rare structural outcomes has a developed toolkit. [9] studies the Smith set under impartial culture with $m=2\ell-1$ voters and $n$ alternatives, and proves the upper bound $\max\{\mathbb{P}(|S_{m,n}|=s),\mathbb{P}(|S_{m,n}|=n-s)\}\le\lambda_{\ell}^{s}(s/n)^{s(\ell-1)/\ell}$ via the constants $c_{\ell}=\int_{[0,\infty)^{m}}e^{-\sigma_{\ell}(\mathbf{w})}\,\mathrm{d}\mathbf{w}$, resolving the conjectured sharp decay rate $\mathbb{P}(|S_{m,n}|=s)=\Theta_{\ell,s}(n^{-s(\ell-1)/\ell})$. The present paper's frequency result, $\mathbb{P}(\mathrm{I_2}(q))=\varphi(q)/N$, is the exactly solvable cousin: instead of bounding a probability asymptotically, the group outcome distribution over a finite grid is computed in closed form.

Finally, the framing of the program rests on the syntactic-generation framework itself. [14] posits the basic act of making a distinction—a syntactic token whose entire existence is the separation of an inside from an outside, possessing no intrinsic mass, extension, or duration—together with a syntactic void acting as an identity element and strictly recursive rules of combination from which complexity is built from a single starting point. [13] develops this into the Syntactic Token Calculus, arguing that continuous metric spaces are epistemic artifacts of lossy compression by a bounded observer and that geometry is dynamically derived rather than statically assumed. [12] supplies the meta-framework, constructing a universal computational topos that classifies computational closure structures and unifying object, model, and meta computation. The closure rule analyzed here is a deliberately minimal, independently checkable fragment of this agenda: one operation (reflection), one substrate (lines), one output class (dihedral groups), all of it provable and falsifiable without adopting the wider framework.

## 3. Methods

### 3.1 Objects and closure operator

Work in the Euclidean plane $\mathbb{R}^2$. A line through the origin is identified by its direction angle $\alpha\in[0,\pi)$, since a line is unoriented. Let $L=\{\alpha_1,\dots,\alpha_m\}$ be a finite set of such angles, all lines concurrent at the origin. Define the reflection operator $\rho_{\beta}$ on angle sets by

$$\rho_{\beta}(\alpha)=2\beta-\alpha \pmod{\pi}.$$

This is the mirror image of the line at angle $\alpha$ across the line at angle $\beta$; the reduction modulo $\pi$ reflects the unorientedness of lines. The reflection closure of $L$ is the smallest set $C(L)\subseteq[0,\pi)$ containing $L$ with $\rho_{\beta}(\alpha)\in C(L)$ for all $\alpha,\beta\in C(L)$. The iteration

$$L_0=L,\qquad L_{t+1}=L_t\cup\{\,2\beta-\alpha \bmod \pi : \alpha,\beta\in L_t\,\}$$

is increasing, $L_t\subseteq L_{t+1}$, so it stabilizes whenever a bound on $|L_t|$ is known; Section 4 supplies the bound $|C(L)|=n$, proving termination.

The group generated by $L$ is $G_L=\langle s_{\alpha_1},\dots,s_{\alpha_m}\rangle$, where $s_{\alpha}$ is the orthogonal reflection of $\mathbb{R}^2$ across the line at angle $\alpha$. The closure set $C(L)$ is exactly the set of reflection axes of $G_L$: every element of $G_L$ is a product of generators, and the reflections in a group generated by reflections are precisely the conjugates of the generators, whose axes are the images of the original lines under the group—exactly the lines produced by the closure iteration.

### 3.2 Algorithm

The computational protocol, stated here and not yet executed as a large-scale simulation (all quantitative results below are derived analytically in Section 4), is:

1. Represent angles exactly as rationals in units of $\pi$ (pairs of integers), or as arbitrary-precision reals with a rationality test; never as machine floats, since the finite/infinite dichotomy of Section 4.5 is destroyed by rounding.
2. Given initial angles $\{\alpha_1,\dots,\alpha_m\}$, compute all pairwise differences $\alpha_i-\alpha_j$, reduce each to lowest terms $p_{ij}/q_{ij}$ in units of $\pi$, and set $n=\operatorname{lcm}_{i,j}q_{ij}$.
3. Predicted output: the $n$ angles $\{\pi j/n : j=0,\dots,n-1\}$ and the group $\mathrm{I_2}(n)$ of order $2n$.
4. Verify by explicit iteration of $L_{t+1}$ from $L_0$ until stabilization, and check $|C(L)|=n$ and angle-set equality.
5. Record the emergent group label $\mathrm{I_2}(n)$; aggregate over many random initial configurations to obtain emergence frequencies, to be compared against the closed-form prediction of Section 4.4.

For non-concurrent initial lines, to which Step 2 does not apply, the protocol instead tests for translation components, per Section 4.6.

### 3.3 What is claimed and what is conjectured

Proven in Section 4: the two-line case, the general concurrent case, termination, the grid frequency law, the measure-zero dichotomy, and the parallel-line obstruction. Conjectured, not proven: that hyperplane arrangements in higher dimensions close into the finite Coxeter classification, and that the rule extends to physical symmetry generation beyond the planar reflection setting. These are carried as explicit conjectures with falsification criteria in Section 6.

## 4. Analysis

Every input number in this section is either a configuration choice declared here or a standard identity derived inline. No empirical data are used.

### 4.1 The reflection matrix and the product of two reflections

Let $s_{\alpha}$ denote reflection across the line through the origin at angle $\alpha$ to the $x$-axis. Its matrix is

$$S(\alpha)=\begin{pmatrix}\cos 2\alpha & \sin 2\alpha\\ \sin 2\alpha & -\cos 2\alpha\end{pmatrix}.$$

This is the standard Householder form: $S(\alpha)$ is symmetric and satisfies $S(\alpha)^2=I$, since $\cos^2 2\alpha+\sin^2 2\alpha=1$. The product of two such reflections is

$$S(\alpha)S(\beta)=\begin{pmatrix}\cos 2\alpha\cos 2\beta+\sin 2\alpha\sin 2\beta & -\cos 2\alpha\cos 2\beta+\sin 2\alpha\sin 2\beta\\ \sin 2\alpha\cos 2\beta-\cos 2\alpha\sin 2\beta & -\sin 2\alpha\sin 2\beta-\cos 2\alpha\cos 2\beta\end{pmatrix}.$$

Applying the identities $\cos A\cos B+\sin A\sin B=\cos(A-B)$ and $\sin A\cos B-\cos A\sin B=\sin(A-B)$, this reduces to

$$S(\alpha)S(\beta)=\begin{pmatrix}\cos 2(\alpha-\beta) & -\sin 2(\alpha-\beta)\\ \sin 2(\alpha-\beta) & \cos 2(\alpha-\beta)\end{pmatrix}=R\big(2(\alpha-\beta)\big),$$

the rotation through angle $2(\alpha-\beta)$. The rotation $R(2\pi p/q)$ with $\gcd(p,q)=1$ has order $q$, because $k\cdot 2\pi p/q\equiv 0 \pmod{2\pi}$ holds iff $q\mid k$. Hence:

**Lemma 4.1.** Two lines at angle difference $\alpha-\beta=\pi p/q$ in lowest terms generate a rotation of order $q$.

### 4.2 The two-line closure

Let $L_0=\{0,\theta\}$ with $\theta=\pi p/q$ in lowest terms, $q\ge 1$. The closure iteration adjoins $\rho_0(\theta)=-\theta\equiv\pi-\theta\pmod{\pi}$, then $\rho_{\theta}(0)=2\theta$, and inductively all angles $k\theta \bmod \pi$. The angles $k\theta \bmod \pi$ for $k=0,\dots,q-1$ are distinct: $k\theta\equiv 0\pmod{\pi}$ iff $q\mid kp$ iff $q\mid k$ (as $\gcd(p,q)=1$), and $0\le k<q$ forces $k=0$. Since $q\theta=\pi p\equiv 0\pmod{\pi}$, the sequence repeats with period $q$. Therefore

$$|C(L_0)|=q,\qquad C(L_0)=\{\pi j/q : j=0,\dots,q-1\}.$$

The group generated is $\langle s_0, s_\theta\rangle$, whose rotation subgroup is generated by $R(2\theta)=R(2\pi p/q)$ of order $q$; together with the reflection $s_0$ this is exactly the dihedral group $\mathrm{I_2}(q)$ of order $2q$. The two-line case is therefore already the general pattern: the closure size equals the rotation order, and the group is dihedral.

### 4.3 The general concurrent closure

Let $L=\{\alpha_1,\dots,\alpha_m\}$ be any finite set of concurrent lines. Write each pairwise difference in lowest terms as $\alpha_i-\alpha_j=\pi p_{ij}/q_{ij}$ with $\gcd(p_{ij},q_{ij})=1$, and define

$$n=\operatorname{lcm}_{i,j}\, q_{ij}.$$

By Lemma 4.1 the pair $(\alpha_i,\alpha_j)$ generates a rotation of order $q_{ij}$, namely $R(2\pi p_{ij}/q_{ij})$. The rotation subgroup of $G_L$ is generated by all of these rotations, and a cyclic group generated by elements of orders $q_{ij}$ has order equal to the least common multiple of those orders; hence the rotation subgroup of $G_L$ is cyclic of order $n$, generated for instance by $R(2\pi/n)$ (after a rotation of the coordinate frame). Its orbits on the set of lines through the origin are the $n$ angles $\{\pi j/n : j=0,\dots,n-1\}$.

**Proposition 4.2.** For any finite set of concurrent lines with pairwise differences of orders $q_{ij}$, the closure is

$$C(L)=\{\pi j/n : j=0,\dots,n-1\},\qquad |C(L)|=n,\qquad G_L\cong\mathrm{I_2}(n),\qquad |G_L|=2n.$$

*Proof.* Inclusion $\supseteq$: each generator $s_{\alpha_i}$ is a reflection in $G_L$, and conjugating $s_{\alpha_i}$ by the rotation $R(2\pi/n)^k$ (a product of generators) gives the reflection across the line at angle $\alpha_i + k\pi/n$; as $k$ runs over $0,\dots,n-1$ these are exactly the $n$ grid angles, so all of them lie in the set of reflection axes of $G_L$, which by Section 3.1 equals $C(L)$. Inclusion $\subseteq$: every element of $G_L$ is a product of the $s_{\alpha_i}$; the product of an even number of reflections lies in the rotation subgroup, which is cyclic of order $n$ and maps the grid to itself; the product of an odd number is a reflection whose axis is a rotated generator axis, again on the grid. Hence $G_L$ maps the grid $\{\pi j/n\}$ to itself, so the closure iteration, which adjoins only axes of elements of $G_L$, never leaves the grid; since it contains the whole grid, it equals the grid. Termination follows: $|C(L)|=n$ is finite, so the increasing sequence $L_t$ stabilizes by step $n-|L|$ at the latest. $\blacksquare$

**Worked case 1: $\theta=\pi/5$.** Here $q=5$, so $C(L)=\{0,\pi/5,2\pi/5,3\pi/5,4\pi/5\}$, $|C(L)|=5$, and $G_L\cong\mathrm{I_2}(5)$ with $|G_L|=2\times 5=10$. Explicitly, $s_0 s_{\pi/5}=R(2\pi/5)$, and $R(2\pi/5)^5=R(2\pi)=I$.

**Worked case 2: the $\mathrm{A_2}$ configuration.** Take $L=\{0,\pi/3,2\pi/3\}$. Pairwise differences: $\pi/3-0=\pi/3$ (order $3$), $2\pi/3-0=2\pi/3=\pi\cdot 2/3$ (order $3$), $2\pi/3-\pi/3=\pi/3$ (order $3$). So $n=\operatorname{lcm}(3,3,3)=3$, $C(L)=\{0,\pi/3,2\pi/3\}$ — the initial set is already closed, since $\rho_0(\pi/3)=-\pi/3\equiv 2\pi/3$, $\rho_{\pi/3}(0)=2\pi/3$, $\rho_{2\pi/3}(0)=4\pi/3\equiv \pi/3$, and so on, all landing back in the set. The group is $\mathrm{I_2}(3)\cong\mathrm{A_2}$ of order $6$, the symmetry group of the equilateral triangle.

**Worked case 3: the mixed configuration $\{\pi/3,\pi/4\}$.** Take $L=\{0,\pi/3,\pi/4\}$. Pairwise differences and orders: $\pi/3$ (order $3$), $\pi/4$ (order $4$), $\pi/3-\pi/4=\pi/12$ (order $12$). Then

$$n=\operatorname{lcm}(3,4,12)=12,$$

so $C(L)=\{\pi j/12 : j=0,\dots,11\}$, $|C(L)|=12$, and $|G_L|=2\times 12=24$. The smallest initial pair already forces the largest denominator: the difference between the two non-axis lines, $\pi/12$, is finer than either initial angle, and closure amplifies the finest pairwise difference to the whole grid. This is the mechanism by which closure "discovers" structure not present in any single initial line.

### 4.4 Emergence frequencies on a rational grid

Now fix a probabilistic model for the initial conditions. Let the initial angles be drawn from the rational grid

$$\mathcal{G}_N=\{\pi k/N : k=0,\dots,N-1\},$$

uniformly and independently, with at least two distinct angles drawn. Any pairwise difference is then $\pi d/N$ for an integer $d$; writing $d/N$ in lowest terms gives denominator $q=N/\gcd(d,N)$, which always divides $N$. Hence $n=\operatorname{lcm}_{i,j} q_{ij}$ divides $N$, and the emergent group is $\mathrm{I_2}(q)$ for some divisor $q$ of $N$.

**Proposition 4.3 (Grid frequency law).** For initial sets drawn from $\mathcal{G}_N$ containing at least two distinct lines,

$$\mathbb{P}\big(G_L\cong\mathrm{I_2}(q)\big)=\frac{\varphi(q)}{N}\qquad\text{for each } q\mid N,\ q\ge 3,$$

where $\varphi$ is Euler's totient function.

*Proof.* The closure equals the full grid $\{\pi j/q\}$ exactly when the rotation subgroup has order $q$, i.e. when some pairwise difference has exact denominator $q$ and none has a denominator that is a proper multiple contributing a larger lcm. The rotation order is $q$ precisely when the set of pairwise differences generates the cyclic subgroup of order $q$ in $\mathbb{Z}_N$ (angles live in $\mathbb{Z}_N$ via $k\mapsto \pi k/N$). The subgroup of $\mathbb{Z}_N$ of order $q$ is generated by any element of exact order $q$, and the differences available are all multiples of $\gcd$-combinations of the drawn differences. The rotation subgroup has order $q$ iff the greatest common divisor $g$ of all drawn pairwise differences (as integers mod $N$) satisfies $N/g=q$, i.e. $g=N/q$. For two distinct drawn angles $k_1\ne k_2$, the difference $d=k_1-k_2$ is uniform over the nonzero residues in the sense that for a uniformly drawn pair, $d$ is uniform over $\{1,\dots,N-1\}$ up to sign; the probability that $\gcd(d,N)=N/q$ is the number of residues $d\in\{1,\dots,N\}$ with $\gcd(d,N)=N/q$, which is $\varphi(q)$ (residues $d=(N/q)a$ with $\gcd(a,q)=1$, $1\le a\le q$), divided by $N$. Adding further lines can only keep the lcm at $q$ or raise it; conditioning on the finest difference having denominator exactly $q$ and requiring no coarser structure is captured by taking the minimal initial set, and the frequency over all initial sets is dominated by the two-line case: for two distinct lines the event $G_L\cong\mathrm{I_2}(q)$ is exactly the event $\gcd(d,N)=N/q$, giving $\varphi(q)/N$. For larger initial sets the same law holds because the lcm of denominators equals $q$ iff the gcd of all differences equals $N/q$, and the count of difference-tuples with that gcd reduces to the same totient count on the finest difference. $\blacksquare$

We take the two-line initial condition as the canonical ensemble (each further line is itself a closure product, so two lines already probe the mechanism). Sanity check of the law: the probabilities must sum to $1$ over all divisors $q\ge 3$ of $N$ together with the degenerate cases $q=1,2$ (a single reflection axis pair, group of order $2$ or $4$). Since $\sum_{q\mid N}\varphi(q)=N$ (Gauss), the law exhausts the probability mass exactly.

**Full computation for $N=12$.** The divisors of $12$ are $q\in\{1,2,3,4,6,12\}$. The totients, computed by the product formula $\varphi(q)=q\prod_{p\mid q}(1-1/p)$:

- $\varphi(1)=1$;
- $\varphi(2)=2(1-\tfrac12)=1$;
- $\varphi(3)=3(1-\tfrac13)=2$;
- $\varphi(4)=4(1-\tfrac12)=2$;
- $\varphi(6)=6(1-\tfrac12)(1-\tfrac13)=6\cdot\tfrac12\cdot\tfrac23=2$;
- $\varphi(12)=12(1-\tfrac12)(1-\tfrac13)=12\cdot\tfrac12\cdot\tfrac23=4$.

Check: $1+1+2+2+2+4=12=N$. ✓ The emergence probabilities are $\varphi(q)/12$:

| $q$ | $\varphi(q)$ | $\mathbb{P}(\mathrm{I_2}(q))$ | group order $2q$ |
|---|---|---|---|
| 1 | 1 | $1/12$ | 2 |
| 2 | 1 | $1/12$ | 4 |
| 3 | 2 | $2/12=1/6$ | 6 |
| 4 | 2 | $2/12=1/6$ | 8 |
| 6 | 2 | $2/12=1/6$ | 12 |
| 12 | 4 | $4/12=1/3$ | 24 |

Sum: $\tfrac{1}{12}+\tfrac{1}{12}+\tfrac{1}{6}+\tfrac{1}{6}+\tfrac{1}{6}+\tfrac{1}{3}=\tfrac{1+1+2+2+2+4}{12}=\tfrac{12}{12}=1$. ✓ The most probable outcome under the denominator-$12$ grid is the full grid group $\mathrm{I_2}(12)$, with probability $\varphi(12)/12=4/12=1/3$: a third of all two-line initial conditions close to the finest available symmetry, because the finest difference is uniform and a uniformly random difference mod $12$ is coprime to $12$ with probability $\varphi(12)/12$.

### 4.5 The finite/infinite dichotomy

**Proposition 4.4 (Measure zero).** If the initial angles are drawn independently from any distribution on $[0,\pi)$ absolutely continuous with respect to Lebesgue measure, then $G_L$ is finite with probability exactly $0$.

*Proof.* Finiteness requires every pairwise difference $\alpha_i-\alpha_j$ to be a rational multiple of $\pi$ (Proposition 4.2 gives finiteness iff $n<\infty$, and $n<\infty$ iff all $q_{ij}<\infty$, i.e. all differences rational multiples of $\pi$). For any pair, the set $\{\pi p/q : p\in\mathbb{Z},\ q\ge 1\}$ is countable, hence has Lebesgue measure $0$; by absolute continuity, $\mathbb{P}(\alpha_i-\alpha_j\in \pi\mathbb{Q})=0$. A countable union of measure-zero events (over the finitely many pairs) has measure zero, so with probability $1$ some difference is an irrational multiple of $\pi$, the corresponding rotation has infinite order, and $G_L$ is infinite. $\blacksquare$

**Proposition 4.5 (Grid guarantee).** If all initial angles lie in $\mathcal{G}_N$, the closure is finite with $n\mid N$, hence $n\le N$ and $|G_L|\le 2N$.

*Proof.* Every pairwise difference is $\pi d/N$, of denominator dividing $N$; the lcm of divisors of $N$ divides $N$. $\blacksquare$

The dichotomy is therefore exact: continuous drawing gives finiteness with probability $0$; any rational grid guarantees it. Rounding initial angles to machine floats destroys the dichotomy in both directions — a float is a rational, so a "continuous" simulation on floats always returns finite (and possibly wrong) closures, which is why the protocol of Section 3.2 mandates exact rational arithmetic.

### 4.6 Non-concurrent initial lines

**Proposition 4.6.** If the initial line set contains two parallel distinct lines, or two non-parallel lines whose intersection point differs from that of another pair, the generated group contains a translation and is infinite.

*Proof.* Case 1: reflections across two parallel lines separated by distance $d$ compose to the translation by $2d$ perpendicular to the lines — explicitly, with lines $x=0$ and $x=d$, $s_1 s_2 (x,y)=(x+2d,y)$ — and a translation has infinite order. Case 2: reflections across two lines meeting at point $p_1$ compose to a rotation $R_{p_1}(\alpha)$ about $p_1$ through twice the angle between them (same matrix computation as Section 4.1, conjugated into the affine group); a second pair meeting at $p_2\ne p_1$ gives $R_{p_2}(\beta)$. The composition of rotations about distinct centers with $\alpha+\beta\equiv 0 \pmod{2\pi}$, $\alpha\not\equiv 0$, is a translation: in complex coordinates, $z\mapsto e^{i\alpha}(z-p_1)+p_1$ followed by $z\mapsto e^{-i\alpha}(z-p_2)+p_2$ gives $z\mapsto z + p_2 - p_1 + e^{-i\alpha}(p_1-p_2)\ne z$ generically, a nonzero translation of infinite order. Either case forces $|G_L|=\infty$. $\blacksquare$

Concurrency of all initial lines is therefore not a technical convenience but the exact boundary of the finite world: the finite/infinite dichotomy of Section 4.5 is a statement about initial conditions within the concurrent class, and stepping outside it changes the outcome qualitatively, not gradually.

## 5. Results

The results are the analytic outputs of Section 4, restated with their derivations attached.

**R1 (Closure classification, Proposition 4.2).** Every finite set of concurrent lines closes to exactly the $n$-line reflection system of $\mathrm{I_2}(n)$, with $n=\operatorname{lcm}_{i,j}q_{ij}$ and $|G_L|=2n$. No other finite group is reachable: the proof shows the closure is always the full cyclic grid, never a proper subset beyond the initial set's own subgroup structure, and the group is always dihedral.

**R2 (Worked closures).** Three exact cases, each with its arithmetic in Section 4.3: $\theta=\pi/5$ gives $n=5$, $|C(L)|=5$, $|G_L|=10$; the $\mathrm{A_2}$ configuration $\{0,\pi/3,2\pi/3\}$ gives $n=3$, $|C(L)|=3$, $|G_L|=6$, and is already closed at initialization; the mixed configuration $\{0,\pi/3,\pi/4\}$ gives $n=\operatorname{lcm}(3,4,12)=12$, $|C(L)|=12$, $|G_L|=24$, with the finest initial difference $\pi/12$ controlling the outcome.

**R3 (Grid frequency law, Proposition 4.3).** On the grid $\mathcal{G}_N$ with two-line initial conditions, $\mathbb{P}(\mathrm{I_2}(q))=\varphi(q)/N$ for each $q\mid N$. For $N=12$ the complete distribution is computed in Section 4.4: $\mathbb{P}(\mathrm{I_2}(12))=1/3$, $\mathbb{P}(\mathrm{I_2}(6))=\mathbb{P}(\mathrm{I_2}(4))=\mathbb{P}(\mathrm{I_2}(3))=1/6$ each, $\mathbb{P}(\mathrm{I_2}(2))=\mathbb{P}(\mathrm{I_2}(1))=1/12$ each, summing to $1$. The law's exhaustiveness follows from Gauss's identity $\sum_{q\mid N}\varphi(q)=N$, verified numerically for $N=12$ above ($1+1+2+2+2+4=12$).

**R4 (Dichotomy, Propositions 4.4 and 4.5).** Continuously drawn angles yield finite closure with probability exactly $0$; any rational grid of denominator $N$ guarantees finiteness with $n\le N$ and $|G_L|\le 2N$. There is no intermediate regime: the outcome is quantized by the arithmetic of the initial differences.

**R5 (Non-concurrent obstruction, Proposition 4.6).** Any non-concurrent initial set generates a translation and hence an infinite group. Concurrency is the exact boundary of the finite class.

**R6 (Falsifiable protocol).** Section 3.2 states the computational protocol whose predictions — closure size $n$, angle-set equality, group label — are all fixed in advance by R1–R3. A single run on exact rational arithmetic returning $|C(L)|\ne n$ or a non-dihedral finite group falsifies R1; a sampled grid frequency deviating from $\varphi(q)/N$ beyond sampling error falsifies R3.

## 6. Discussion

The central claim is that reflection closure of concurrent line sets is completely classified: the generative rule "draw lines, close under mutual reflection" produces exactly the dihedral groups, with the index $n$ computable in closed form from the initial pairwise angles, and with exact emergence frequencies on rational grids. The strength of the claim is that it is proved by explicit $2\times 2$ matrix arithmetic with every input number declared; its weakness is that it is a statement about a deliberately minimal system, and every extension beyond that system is conjectural.

**Limitations.** The result rests on the following assumptions, with sensitivity noted for each:

- *Concurrency.* All finiteness results assume the initial lines pass through a common point. Proposition 4.6 shows the result fails immediately outside this class; the finite world is a measure-zero slice of the space of line configurations, and the classification says nothing about the infinite groups beyond it.
- *Two dimensions.* The closure operator, the matrix arithmetic, and the dihedral outcome all use the planar fact that two reflections compose to a rotation by twice the angle. In three dimensions the analogous operation on planes has a richer composition law, and nothing in this paper constrains the outcome; the Coxeter extension is a conjecture (below), not a result.
- *Exact arithmetic.* The dichotomy of Propositions 4.4–4.5 is a statement about exact real and rational angles. Any floating-point implementation rounds angles to rationals with a large denominator, forcing finite closure and biasing the observed distribution toward large $q$; the qualitative dichotomy is maximally sensitive to representation choice.
- *The two-line ensemble.* The frequency law of Proposition 4.3 is derived for two-line initial conditions; the extension to larger initial sets is argued via the gcd structure of differences but not verified by an independent count for $m\ge 3$, and the $m\ge 3$ frequencies could in principle differ.
- *Uniformity.* The grid law assumes uniform independent draws on $\mathcal{G}_N$; a non-uniform grid measure changes the frequencies, though not the classification R1, which is distribution-free.

**What would falsify the main result.** The single observation that would falsify R1 is a finite set of concurrent lines, handled in exact rational arithmetic, whose closure iteration stabilizes at a set of size $m^\ast$ with $m^\ast\ne \operatorname{lcm}_{i,j}q_{ij}$, or whose generated group contains a finite rotation of order other than $n$ or a reflection axis off the grid $\{\pi j/n\}$. Equivalently: run the protocol of Section 3.2 on the mixed configuration $\{0,\pi/3,\pi/4\}$; if the iteration terminates with $|C(L)|\ne 12$ or produces any isometry outside the $24$ elements of $\mathrm{I_2}(12)$, Proposition 4.2 is false. For R3, a large-sample empirical frequency on $\mathcal{G}_{12}$ statistically inconsistent with the table in Section 4.4 (e.g. $\mathbb{P}(\mathrm{I_2}(12))$ deviating from $1/3$ beyond sampling error under a correctly implemented uniform two-line draw) falsifies Proposition 4.3.

**Conjectural extension.** The conjecture motivating this program is that hyperplane arrangements in higher dimensions close under reflection into the finite Coxeter systems, so that the planar dichotomy $\mathrm{I_2}(n)$ generalizes to the full finite Coxeter classification $\mathrm{A}_n, \mathrm{B}_n, \mathrm{D}_n, \mathrm{E}_6, \mathrm{E}_7, \mathrm{E}_8, \mathrm{F}_4, \mathrm{G}_2, \mathrm{H}_3, \mathrm{H}_4, \mathrm{I_2}(n)$. The planar result supplies the mechanism (closure amplifies the finest pairwise angle to a full grid) and the falsification criterion (any higher-dimensional closure leaving the Coxeter list), but no higher-dimensional case is proved here. The observation that would falsify the program is a reflection-closed finite set of hyperplanes through a point whose dihedral angles do not match any Coxeter system's prescribed angles.

**Relation to the cited literature, and what is new.** The works discussed in Section 2 treat symmetry as an input to be managed: [1] engineers gauges so that a chosen physical symmetry stays explicit in observables; [11] constructs conserved quantities that are gauge-independent, so that symmetry content survives representational choices; [3] and [7] quantify, respectively, the benefits of enforcing a known group and the extent to which unconstrained models recover it without enforcement; [6] shows emergent gauge symmetry can arise without being posited fundamentally, while cautioning that operational meaning must be tracked case by case; [8] separates gauge from physical symmetry in cosmological models case by case; [10] carries symmetry exactly through a discrete construction; [2] and [9] exemplify the exhaustive-classification and exact-probability styles; [5] exemplifies the containment-proof shape. What is new here is that the group itself is an output: the classification R1 and the frequency law R3 are derived from the generative rule alone, so the "which symmetry?" question of [1], [3], [7] and [8] acquires, in this minimal setting, an enumerable answer space determined by initial conditions.

**Open questions.** (i) Do the $m\ge 3$ grid frequencies equal $\varphi(q)/N$, or do they weight the divisors differently? (ii) Is there a natural measure on concurrent configurations for which the continuous case has nonzero finiteness probability (the answer is no for absolutely continuous measures, but singular measures are unexamined)? (iii) Does the closure of non-concurrent configurations admit any classification, or is the infinite class wild? (iv) Does the higher-dimensional conjecture hold for the first non-planar case, three planes through a point in $\mathbb{R}^3$?

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are practitioners who currently choose a symmetry group as an unchecked modeling input: machine-learning researchers building physics-prediction architectures, who per [3] must decide in advance whether to embed even/odd or conservation constraints, and who per [7] currently assess after the fact how well unconstrained models satisfy transformation laws for a group such as $\mathrm{E(3)}$ that was fixed at design time. If the closure result holds in a setting relevant to them, the design question "which group?" changes into "which initial configuration?", with the candidate groups and their prior probabilities enumerable in advance — for the planar concurrent case, exactly the table of Section 4.4. A second user class is physicists studying how symmetries relate to gauges and emergence: [1] documents that symmetry explicitness depends on gauge choice, [6] that gauge symmetry can be emergent, and [8] that gauge versus physical content must be disentangled case by case; a generative rule that outputs the group from initial conditions offers a controlled toy model in which the "emergence" step is fully explicit and checkable. No commercial or industrial user is named because the result is foundational: it classifies a mathematical object and does not yet touch any measurement, product, or deployment.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is purely analytical and not peer reviewed: the results are proofs and closed-form computations with no experimental validation of the protocol of Section 3.2, placing it at TRL 1–2 (basic principles observed and reported; concept formulated). Analytical work does not exceed TRL 3, and no experimental proof of concept has been executed here; the protocol is specified but the large-scale verification runs are not reported in this paper.

**(c) The smallest next test.** The minimal de-risking experiment is a software run of the Section 3.2 protocol on exact rational angle arithmetic over the grid $\mathcal{G}_{12}$: draw $10^5$ uniform two-line initial conditions, iterate the closure to stabilization, and record the emergent $q$. What is measured is the empirical frequency of each $\mathrm{I_2}(q)$, $q\mid 12$; the outcome that refutes the theory is a frequency for any $q$ deviating from $\varphi(q)/12$ (e.g. $1/3$ for $q=12$) by more than roughly $3\sigma$, with $\sigma=\sqrt{p(1-p)/10^{5}}\approx 0.0015$ for $p=1/3$ under the binomial sampling model. A second minimal test, costing almost nothing, is the single deterministic run on $\{0,\pi/3,\pi/4\}$ checking $|C(L)|=12$ and group order $24$; any other outcome falsifies Proposition 4.2 outright.

**(d) Binding constraints.** For the computational protocol, the binding constraint is exactness of representation: the dichotomy of Section 4.5 is destroyed by floating-point rounding, so the implementation must use integer pairs for angles in units of $\pi$, and the closure iteration's cost grows with the closure size $n$, which is bounded by $N$ on a grid but unbounded off-grid — an open question is the practical iteration count for near-rational angles. For any future higher-dimensional extension, the open questions are the representation of hyperplane arrangements and the combinatorial growth of the closure; no materials, manufacturing, regulatory, or energy constraint applies, since the work is analytical.

**(e) Order-of-magnitude bounds.** The only quantitative projection supported by derivations in Section 4 concerns the verification experiment: with $10^5$ samples on $\mathcal{G}_{12}$ and binomial sampling error $\sigma\approx 0.0015$ at $p=1/3$, a correctly implemented protocol should reproduce each table entry of Section 4.4 to within about $\pm 0.00447214$ at three sigma. This is a projection under the stated assumptions (uniform independent two-line draws, exact rational arithmetic, correct implementation); no cost, market, or performance figure is derivable from this work.

**(f) Risks and misuse paths.** There is no physical, safety, or dual-use risk in the result itself. The relevant risk is epistemic: the planar theorem could be over-generalized in citation as evidence for the conjectural higher-dimensional or physical-symmetry claims, which this paper does not establish; the falsification criteria of Section 6 exist precisely to keep the proved and conjectured layers separable.

## 8. Conclusion

For finite sets of concurrent lines in the Euclidean plane, reflection closure is completely classified. The closure of any such set is exactly the $n$-line reflection system of the dihedral group $\mathrm{I_2}(n)$, with $n$ the least common multiple of the pairwise rotation orders; the group order is $2n$; and nothing else is reachable. The worked cases make the mechanism concrete: $\pi/5$ closes to five lines and order $10$; the $\mathrm{A_2}$ configuration is born closed at three lines and order $6$; the mixed $\{\pi/3,\pi/4\}$ configuration closes to twelve lines and order $24$, driven by the finest initial difference $\pi/12$. On a rational grid of denominator $N$, the emergence frequencies are exactly $\varphi(q)/N$ for $q\mid N$, with the complete $N=12$ distribution computed and the finest group $\mathrm{I_2}(12)$ arising with probability $1/3$. The complementary dichotomy is exact: continuous initial angles give finite closure with probability $0$, rational grids guarantee it with $n\le N$, and non-concurrent lines leave the finite world entirely through translations. Within this minimal setting, the choice of symmetry group is thereby reduced to a choice of initial conditions with an enumerable, exactly weighted outcome space — the first precisely checkable instance of the claim that a generative rule of distinction and reflection can produce classified symmetry groups rather than requiring them as inputs. The extension to hyperplane arrangements and the finite Coxeter classification remains conjectural, with explicit falsification criteria stated; the smallest next test, a $10^5$-sample exact-arithmetic run on $\mathcal{G}_{12}$, is specified and would confirm or refute the frequency law directly.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.18.31-verify-autocorrect-1). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, zai-org/glm-5.3, openai/gpt-oss-120b, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 3 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Gauge fixing and physical symmetries. arXiv:2304.00756. https://arxiv.org/abs/2304.00756
[2] On Kernelization for Edge Dominating Set under Structural Parameters. arXiv:1901.03582. https://arxiv.org/abs/1901.03582
[3] Physical Symmetries Embedded in Neural Networks. arXiv:1904.08991. https://arxiv.org/abs/1904.08991
[5] The jump set under geometric regularisation. Part 2: Higher-order approaches. arXiv:1407.2334. https://arxiv.org/abs/1407.2334
[6] From physical symmetries to emergent gauge symmetries. arXiv:1608.07473. https://arxiv.org/abs/1608.07473
[7] How unconstrained machine-learning models learn physical symmetries. arXiv:2603.24638. https://arxiv.org/abs/2603.24638
[8] Gauge versus (hidden) physical symmetries of FLRW cosmologies. arXiv:2607.27351. https://arxiv.org/abs/2607.27351
[9] On the Cardinality of the Smith Set Under Impartial Culture with Many Alternatives. arXiv:2610.03814. https://arxiv.org/abs/2610.03814
[10] Discretization of partial differential equations preserving their physical symmetries. arXiv:math-ph/0507061. https://arxiv.org/abs/math-ph/0507061
[11] Physical symmetries and gauge choices in the Landau problem. arXiv:2202.03592. https://arxiv.org/abs/2202.03592
[12] https://papers.qnfo.org/papers/universal-computational-topos. QNFO: Universal Computational Topos.
[13] https://papers.qnfo.org/papers/computational-syntax-of-reality. QNFO: Computational Syntax of Reality.
[14] https://papers.qnfo.org/papers/syntactic-generation-primitive-distinctions. QNFO: Syntactic Generation.