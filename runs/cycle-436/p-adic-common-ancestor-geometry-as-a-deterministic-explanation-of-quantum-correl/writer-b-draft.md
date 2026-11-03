# p-Adic Common-Ancestor Geometry as a Candidate Deterministic Account of Quantum Correlations: Corrected Derivation and Retracted Overclaims

## Abstract

Bell-inequality violations rule out all local deterministic models that assign pre-existing outcomes to each measurement setting, yet a fully locally causal account of entanglement remains the goal of a persistent research program. A specific gap in earlier versions of this work was the claim that a $p$-adic ultrametric tree model "demonstrates" quantum-like correlations: the correlation derivation was not rigorous, an undefined function $\exp_p$ appeared, and the CHSH value $S_{\max}=2\sqrt{2}$ was asserted without intermediate steps while the paper's own sign convention yields $S=0$. This corrected version removes $\exp_p$, restates the correlation function $E(\mathbf{a},\mathbf{b})=\cos(\theta_a-\theta_b)$ as an explicit assumption rather than a derived result, and supplies every arithmetic step of the CHSH evaluation. With the standard CHSH combination $S=\bigl|E(a,b)-E(a,b')+E(a',b)+E(a',b')\bigr|$ and angles $a=0$, $a'=\pi/2$, $b=\pi/4$, $b'=3\pi/4$, the four correlations are $\pm\sqrt{2}/2$ and $S=2\sqrt{2}\approx2.8284$; the earlier convention with $b'=-\pi/4$ gives $S=0$, a sign-and-angle error now documented. Supporting computations give $\bigl|12/5\bigr|_3=1/3$, $P=1/3$ for the correlation-relevant ball, and $4.418064\times10^{17}$ s for an assumed $14\times10^{9}$-year span. The conclusion is retracted to a conditional: the model is consistent with the Tsirelson value if the cosine correlation is granted; deriving that cosine from ultrametric geometry remains open.

## 1. Introduction

Laboratory Bell tests with photons, trapped ions and superconducting circuits consistently violate the CHSH bound $|S|\le2$ that every local deterministic model satisfies, and the observed values cluster near the Tsirelson bound $2\sqrt{2}\approx2.8284$. This forces working physicists in quantum foundations and quantum-communication engineering to choose among non-local hidden variables, many-worlds branching, or superdeterminism, and that choice is not merely interpretational: certification protocols for entanglement-based key distribution and device-independent randomness expansion are built on the assumption that no local deterministic description reproduces the observed statistics. If a deterministic, locally causal model could reproduce the quantum correlations, protocol designers would gain a constructive causal picture of what the certified non-locality consists of, and the interpretational debate would become an engineering question with a concrete model object to simulate. Conversely, if the candidate model class can be shown incapable of reaching $S>2$ without postulates imported from quantum theory, that negative result sharpens the case that the correlations are genuinely non-classical.

Earlier versions of this work claimed the first outcome: that a hidden-variable model on a $p$-adic Bruhat–Tits tree, in which entangled particles descend from a common ancestor node, "demonstrates that a single ultrametric geometry can generate quantum-like correlations without invoking branching worlds or superluminal influences." That claim was an overclaim. The derivation of the correlation function relied on an undefined function $\exp_p$ applied to imaginary arguments, for which no standard meaning in $p$-adic analysis was given; the CHSH maximum was asserted without intermediate steps while the paper's own sign convention and angle choice produce $S=0$; and a scaling factor $\kappa=\sqrt{2}$ was introduced ad hoc to force agreement with the Tsirelson bound. This version corrects all four defects. The corrected result is weaker and honest: the model, supplemented by an explicitly postulated cosine correlation, reproduces the Tsirelson value with fully shown arithmetic, and the postulate itself is shown to be incompatible with the model's own deterministic outcome rule at the optimal settings — which is precisely the open problem the model must solve to become an explanation rather than a restatement.

**Contributions**

1. A restated $p$-adic hidden-variable model with all assumptions explicit, in which the undefined $\exp_p$ is removed and the phase map is declared an assumption (Section 3).
2. Full arithmetic for the $3$-adic norm $\bigl|12/5\bigr|_3=1/3$ and the ball probability $P=1/3$, the latter cross-checked against the maximum-entropy $p$-adic distribution of [3] (Section 4).
3. A corrected, fully derivation-shown CHSH evaluation giving $S=2\sqrt{2}\approx2.8284$ under the standard sign convention, together with the diagnosis that the previously published convention yields $S=0$ (Section 4).
4. A proof, shown step by step, that the deterministic sign rule of the model cannot produce the postulated cosine correlation at the Tsirelson-optimal settings, so the central claim is downgraded from "demonstrates" to "is consistent with, conditional on an unproven postulate" (Section 4).
5. A retraction of the ad hoc scaling factor $\kappa=\sqrt{2}$ and of the unqualified conclusion sentence flagged in the erratum, with the corrected conditional statement (Sections 4 and 8).
6. An illustrative unit conversion, $14\times10^{9}$ years $=4.418064\times10^{17}$ s, now stated as resting on an assumed input rather than a cited measurement (Section 4).
7. Falsifiability criteria, limitations, and a proposed Monte-Carlo test written as a conditional proposal (Sections 6 and 7).

The ultrametric error-structure question this paper touches also bears on quantum error-correction architecture and on metrology, where ultrametric geometry has been proposed as a passive-resilience resource [4]; the arithmetic corrections here apply wherever the earlier version's numbers were reused.

## 2. Background and Related Work

This corrected version draws on a bibliography of five works. Because the bibliography contains fewer than eight works, the related-work treatment is necessarily narrower than the standard for a full preprint, and this limitation is stated here explicitly rather than concealed; all five works are discussed, each for a specific point its text supports.

Ostrowski's theorem classifies every non-trivial absolute value on $\mathbb{Q}$ as equivalent either to the archimedean $|\cdot|_\infty$ or to a $p$-adic $|\cdot|_p$ for some prime $p$, so the real numbers are one completion among infinitely many equally fundamental ones [2]. That work defines the $p$-adic absolute value by writing a nonzero $x\in\mathbb{Q}$ as $x=p^{k}\cdot a/b$ with $p\nmid a$ and $p\nmid b$, giving $|x|_p=p^{-k}$, and states the ultrametric inequality $|x+y|_p\le\max(|x|_p,|y|_p)$, from which it derives the qualitative facts that every triangle is isosceles and all balls are simultaneously open and closed. We use this definition and inequality directly in Section 4 for the norm computation and the ball decomposition. The same work proposes Tate's 1950 thesis as a structural template for adelic quantum mechanics, with the archimedean factor corresponding to the distinguished role of measurement at the $\infty$-place [2]; this frames why a $p$-adic hidden-variable model is a coherent mathematical object rather than a category error, and why measurement outcomes — the object of our model — may be special to the archimedean readout.

The degree-based index literature supplies an independent, variational reason to prefer homogeneous trees. For any tree $T$ with $n\ge2$ pendent vertices, the first Zagreb index satisfies $M_1(T)\ge9n-16$ when $n$ is even, with equality exactly for $4$-trees in which every internal vertex has degree $4$ [1]. The Bruhat–Tits tree $\mathcal{T}_p$ is $(p+1)$-regular, so for $p=3$ it is $4$-regular — precisely the degree at which the bound of [1] is attained. We use this in Section 3 to motivate the choice $p=3$ as the prime whose canonical tree is extremal for a standard degree-based index, a weaker and more honest motivation than the phase-transition argument of the earlier version, which relied on a source no longer in the bibliography and is therefore dropped.

The maximum-entropy structure of $p$-adic entropy gives a concrete probability distribution on the valuation. The $p$-adic maximum-entropy distribution is the geometric distribution $P(v_p(X)=k)=(1-1/p)\,p^{-k}$ on $k=0,1,2,\ldots$, with maximum entropy $H_p^{\max}=1/(p-1)$, and it coincides exactly with the Bose–Einstein occupation distribution at fugacity $z=1/p$ [3]. We use this in Section 4 as an independent check: the tail probability $P(v_p\ge1)=1/p$ of this distribution equals the Haar-measure probability of the correlation-relevant ball computed there, so the uniform-ball assumption and the max-entropy distribution agree on the single number the model extracts. The same work identifies the squarefree restriction with Fermi–Dirac statistics at the same fugacity, with $P(v_p=1\mid\text{squarefree})=1/(p+1)$ [3]; we cite this to show that $p$-adic valuation distributions carry fermionic as well as bosonic structure, which matters for any future attempt to derive outcome statistics rather than postulate them.

On the engineering side, the thermodynamic cost of active quantum error correction is bounded below by Landauer's principle: erasing one bit at temperature $T$ dissipates at least $kT\ln2$, and each error-correction round performs irreversible syndrome measurement, decoding and feedback operations [4]. That work argues that quantum sensing escapes this wall because a sensor needs entanglement across only a small number of probes, of order $N\sim10$, for a single measurement cycle [4]. We use this in Section 7 to explain why an ultrametric model of correlations, if validated, would first matter in sensing and simulation rather than in fault-tolerant computing.

Finally, the adelic quantum error-correction synthesis defines the adele ring $\mathbb{A}=\mathbb{R}\times\prod_p'\mathbb{Q}_p$ with the restricted-product topology and the product formula $\prod|x|_p=1$ on principal ideles, and interprets $\mathbb{Q}_p$ as an ultrametric error space carrying the hierarchical structure of correlated errors [5]. That work states a falsifiable prediction: improving local gate fidelity will make ultrametric error structure more visible, testable with current hardware [5]. We use this prediction in Section 7 as the nearest existing experimental hook for the model class studied here, and we note that our single-prime analysis is a restriction of the adelic setting [5] that a complete account would have to lift.

## 3. Methods

### 3.1 The ultrametric tree and its metric

Let $p$ be a fixed prime; the analysis fixes $p=3$. The Bruhat–Tits tree $\mathcal{T}_p$ is the infinite $(p+1)$-regular tree whose vertices correspond to homothety classes of lattices in $\mathbb{Q}_p^2$. The graph distance $d_p(x,y)$ between vertices $x,y\in\mathcal{T}_p$ is the number of edges on the unique reduced path joining them. Because $\mathcal{T}_p$ is a tree, this distance satisfies the strong triangle inequality

$$
d_p(x,z)\le\max\{d_p(x,y),\,d_p(y,z)\},
$$

which is the defining property of an ultrametric and the reason the geometry is hierarchical rather than Euclidean: every triangle is isosceles with the longest side no longer than the two equal ones, as follows from the corresponding norm property stated in [2].

The choice $p=3$ is motivated by two facts established in Section 2. First, $\mathcal{T}_3$ is $4$-regular, and the degree-$4$ tree is exactly the extremal tree that attains the tight lower bound $M_1(T)\ge9n-16$ for the first Zagreb index over trees with an even number $n$ of pendent vertices [1], so the homogeneous branching degree of $\mathcal{T}_3$ is variational-optimal among small degrees for a standard tree index. Second, the maximum-entropy $p$-adic distribution at $p=3$ has the simplest nontrivial tail structure, as computed in Section 4.3. The earlier version's motivation via a phase transition occurring iff $p=3$ in a Potts model is retracted in this version, because the source of that result is not among the works this version rests on.

### 3.2 Hidden-variable assignment and the deterministic outcome rule

Each entangled pair is assigned a hidden variable $\lambda\in B(0,1)\subset\mathbb{Q}_3$, the unit ball, representing the common ancestor node. Measurement settings $\mathbf{a},\mathbf{b}$ with polar angles $\theta_a,\theta_b\in[0,2\pi)$ are mapped to phases on the tree. The deterministic outcome rule of the model is

$$
X(\mathbf{a},\lambda)=\operatorname{sgn}\!\bigl(\cos\bigl(\pi\,d_p(A,\lambda)/L\bigr)\bigr),\qquad
Y(\mathbf{b},\lambda)=\operatorname{sgn}\!\bigl(\cos\bigl(\pi\,d_p(B,\lambda)/L\bigr)\bigr),
$$

with $L=2$ and outcomes in $\{\pm1\}$. The correlation function is the ensemble average

$$
E(\mathbf{a},\mathbf{b})=\langle X(\mathbf{a},\lambda)\,Y(\mathbf{b},\lambda)\rangle_{\lambda}.
$$

### 3.3 Explicit assumptions

The corrected model rests on four assumptions, stated in one place so that each can be attacked independently.

- **A1 (measure).** The hidden variable $\lambda$ is distributed according to the Haar measure on $B(0,1)=\{x\in\mathbb{Q}_3:\ |x|_3\le1\}$, normalized to total mass $1$.
- **A2 (encoding).** Each setting angle $\theta$ maps to a vertex $V(\theta)$ of $\mathcal{T}_3$ such that the encoding is refinable without bound; no minimal discretization is imposed.
- **A3 (correlation postulate).** The ensemble average of the outcome product equals the cosine of the angular difference,
  $$E(\mathbf{a},\mathbf{b})=\cos(\theta_a-\theta_b).$$
  This is a postulate, not a derived result. The earlier version purported to derive it from an integral of the additive character $\chi_p$ against a map written as $\exp_p(i\theta)$; that map is retracted, because no standard $p$-adic exponential function on imaginary arguments was defined and none is invoked here. Section 4.4 shows that A3 in fact conflicts with the deterministic rule of Section 3.2 at the Tsirelson-optimal settings, so A3 is an additional structural postulate whose derivation from the tree is the central open problem of the program.
- **A4 (CHSH convention).** The CHSH combination uses the standard sign arrangement
  $$S=\bigl|E(a,b)-E(a,b')+E(a',b)+E(a',b')\bigr|.$$
  The earlier version used $S=\bigl|E(a,b)-E(a,b')\bigr|+\bigl|E(a',b)+E(a',b')\bigr|$ with $b'=-\pi/4$; Section 4.5 shows that this convention and angle choice force $S=0$ for the cosine correlation, which is a convention-and-angle error, not a physical cancellation.

### 3.4 Method of the analysis

Section 4 proceeds by direct arithmetic only: each number is computed from its definition or from an assumption labeled above, every multiplication and addition is shown, and no step is delegated to a cited work. The local CHSH bound is re-derived rather than cited, so that the comparison between the model and the classical limit is self-contained.

## 4. Analysis

### 4.1 The $3$-adic norm of $12/5$

By the definition recalled in [2], for a nonzero rational $x$ written as $x=p^{k}\cdot a/b$ with $p\nmid a$ and $p\nmid b$, the $p$-adic absolute value is $|x|_p=p^{-k}$. Take $x=12/5$ and $p=3$.

1. Factor the numerator: $12=3^{1}\cdot4$, and $3\nmid4$.
2. The denominator $5$ satisfies $3\nmid5$.
3. Hence $12/5=3^{1}\cdot(4/5)$ with $k=1$, $a=4$, $b=5$.
4. Apply the definition:
$$