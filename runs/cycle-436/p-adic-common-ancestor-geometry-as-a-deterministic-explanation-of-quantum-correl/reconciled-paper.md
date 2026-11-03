# p-Adic Common-Ancestor Geometry as a Candidate Deterministic Account of Quantum Correlations: Corrected Derivation and Retracted Overclaims

## Abstract

Bell-inequality violations rule out all local deterministic models that assign pre-existing outcomes to each measurement setting, yet a fully locally causal account of entanglement remains the goal of a persistent research program. A specific gap in earlier versions of this work was the claim that a $p$-adic ultrametric tree model "demonstrates" quantum-like correlations: the correlation derivation was not rigorous, an undefined function $\exp_p$ appeared, and the CHSH value $S_{\max}=2\sqrt{2}$ was asserted without intermediate steps while the paper's own sign convention yields $S=0$. This corrected version removes $\exp_p$, restates the correlation function $E(\mathbf{a},\mathbf{b})=\cos(\theta_a-\theta_b)$ as an explicit assumption rather than a derived result, and supplies every arithmetic step of the CHSH evaluation. With the standard CHSH combination $S=\bigl|E(a,b)-E(a,b')+E(a',b)+E(a',b')\bigr|$ and angles $a=0$, $a'=\pi/2$, $b=\pi/4$, $b'=3\pi/4$, the four correlations are $\pm\sqrt{2}/2$ and $S=2\sqrt{2}\approx2.8284$; the earlier convention with $b'=-\pi/4$ gives $S=0$, a sign-and-angle error now documented. Supporting computations give $\bigl|12/5\bigr|_3=1/3$, $P=1/3$ for the correlation-relevant ball, and $4.418064\times10^{17}$ s for an assumed $14\times10^{9}$-year span. The conclusion is retracted to a conditional: the model is consistent with the Tsirelson value if the cosine correlation is granted; deriving that cosine from ultrametric geometry remains open.

## 1. Introduction

We take as given, as the framing assumption of this work, that laboratory Bell tests violate the CHSH bound $|S|\le2$ that every local deterministic model satisfies, and that the observed values cluster near the Tsirelson bound $2\sqrt{2}\approx2.8284$. This forces working physicists in quantum foundations and quantum-communication engineering to choose among non-local hidden variables, many-worlds branching, or superdeterminism, and that choice is not merely interpretational: we further take as given that certification protocols for entanglement-based key distribution and device-independent randomness expansion are built on the assumption that no local deterministic description reproduces the observed statistics. If a deterministic, locally causal model could reproduce the quantum correlations, protocol designers would gain a constructive causal picture of what the certified non-locality consists of, and the interpretational debate would become an engineering question with a concrete model object to simulate. Conversely, if the candidate model class can be shown incapable of reaching $S>2$ without postulates imported from quantum theory, that negative result sharpens the case that the correlations are genuinely non-classical.

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

The choice $p=3$ is motivated by two facts established in Section 2. First, $\mathcal{T}_3$ is $4$-regular, and the degree-$4$ tree is exactly the extremal tree that attains the tight lower bound $M_1(T)\ge9n-16$ for the first Zagreb index over trees with an even number $n$ of pendent vertices [1], so the homogeneous branching degree of $\mathcal{T}_3$ is variational-optimal among small degrees for a standard tree index. Second, the maximum-entropy $p$-adic distribution at $p=3$ has the simplest nontrivial tail structure, as computed in Section 4.2. The earlier version's motivation via a phase transition occurring iff $p=3$ in a Potts model is retracted in this version, because the source of that result is not among the works this version rests on.

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
|12/5|_3=3^{-k}=3^{-1}=\frac{1}{3}\approx0.333333.
$$

The ultrametric inequality of [2] is consistent with this value: $|12|_3=3^{-1}=1/3$ and $|5|_3=3^{0}=1$, and indeed $|12/5|_3=|12|_3/|5|_3=(1/3)/1=1/3$, as multiplicativity requires.

### 4.2 The correlation-relevant ball probability

Under A1, the hidden variable $\lambda$ is Haar-uniform on $B(0,1)$. The unit ball decomposes into $p$ disjoint sub-balls of radius $p^{-1}$, each of equal Haar measure, because multiplication by any element of $3\mathbb{Z}_3$ maps one sub-ball onto another and the Haar measure is translation-invariant. For $p=3$,

$$
B(0,1)=\bigsqcup_{j=0}^{2}\bigl(j+3\mathbb{Z}_3\bigr),
$$

so each sub-ball has measure $1/3$ of the total. The correlation-relevant ball is the sub-ball of radius $1/3$, hence

$$
P\bigl(|\lambda|_3\le\tfrac{1}{3}\bigr)=\frac{1}{3}\approx0.333333.
$$

Cross-check against the maximum-entropy distribution of [3]. That work gives $P(v_p(X)=k)=(1-1/p)\,p^{-k}$ for $k=0,1,2,\ldots$. For $p=3$:

1. $P(v_3=0)=(1-\tfrac{1}{3})\cdot3^{0}=\tfrac{2}{3}$.
2. The event $|\lambda|_3\le1/3$ is exactly the event $v_3(\lambda)\ge1$.
3. Therefore $P(v_3\ge1)=1-P(v_3=0)=1-\tfrac{2}{3}=\tfrac{1}{3}$.

The two independent routes — Haar measure on the ball and the maximum-entropy valuation distribution of [3] — agree on $P=1/3$, so the uniform-ball assumption and the max-entropy distribution coincide on the single number the model extracts. For reference, the same work reports the conditional squarefree probability $P(v_p=1\mid\text{squarefree})=1/(p+1)$, which for $p=3$ gives $1/4$; this number is not used by the model but is recorded to show that other $p$-adic valuation statistics differ from the uniform-ball value and could distinguish distributional assumptions in future work.

### 4.3 Illustrative unit conversion: an assumed $14\times10^{9}$-year span

The span of $14\times10^{9}$ years is an assumption of this computation, not a cited measurement. Convert to seconds:

1. One year $\approx365.25$ days (Julian year).
2. One day $=24$ h; one hour $=3600$ s.
3. Seconds per year:

$$
365.25\times24\times3600=365.25\times86\,400=31\,557\,600\ \text{s}.
$$

4. Multiply by $14\times10^{9}$:

$$
31\,557\,600\times14\times10^{9}=31\,557\,600\times1.4\times10^{10}=4.418064\times10^{17}\ \text{s}.
$$

The result, $4.418064\times10^{17}$ s, is exact given the two stated inputs ($365.25$ d/yr and $14\times10^{9}$ yr); it carries no physical claim beyond the assumption stated.

### 4.4 The deterministic sign rule cannot produce the cosine postulate

The outcome rule of Section 3.2 evaluates $\cos(\pi d/2)$ at integer tree distances $d=d_p(V,\lambda)$. Compute the two cases:

$$
\cos\!\left(\frac{\pi d}{2}\right)=
\begin{cases}
+1, & d\equiv 0 \pmod 4,\\
0, & d\equiv 1,3 \pmod 4,\\
-1, & d\equiv 2 \pmod 4.
\end{cases}
$$

Because $d_p(V,\lambda)$ is an integer for every pair of tree vertices, the argument $\pi d/2$ takes only the values $0,\pm\pi/2,\pm\pi,\pm3\pi/2,\ldots$, and the cosine takes only the values in the table above. The sign function then gives

$$
X(\mathbf{a},\lambda)\in\{-1,0,+1\},
$$

and the value $0$ occurs whenever $d_p(A,\lambda)$ is odd. Two consequences follow immediately.

First, the outcome rule as written does not even produce a binary outcome on all of $B(0,1)$: a fraction of the hidden-variable space — namely the set of $\lambda$ at odd tree distance from $A$ — yields the degenerate outcome $0$. Under the Haar measure of A1, the sub-ball $j+3\mathbb{Z}_3$ containing $A$ contributes the even-distance cases, and the two adjacent sub-balls contribute odd distances; since each sub-ball has measure $1/3$ (Section 4.2), the degenerate outcome has measure at least $2/3$ under any encoding in which $A$ lies in one sub-ball and its neighbors in the others. A model that outputs $0$ on two-thirds of its hidden-variable space is not a model of binary measurements without an additional rule for reassigning the degenerate cases.

Second, even after any repair that maps the degenerate cases to $\pm1$, the correlation $E(\mathbf{a},\mathbf{b})=\langle XY\rangle_\lambda$ is an average of products of numbers in $\{-1,0,+1\}$, so after repair it is an average of numbers in $\{-1,+1\}$ and hence lies in $[-1,1]$ — but the point that matters for the CHSH evaluation is finer: the sign rule produces correlations that are piecewise-constant functions of the tree distances, taking values in a discrete set determined by the sub-ball decomposition. The postulated cosine $E=\cos(\theta_a-\theta_b)$ takes the value $\sqrt{2}/2\approx0.707107$ at the Tsirelson-optimal settings, and no average of $\pm1$-valued products over the three sub-balls of Section 4.2 can equal $\sqrt{2}/2$, because any such average is a rational combination of $1$, $-1$ and $0$ with denominators dividing $3$, hence a rational number, while $\sqrt{2}/2$ is irrational. This is the precise sense in which A3 conflicts with the deterministic rule of Section 3.2: the postulate is not derivable from the tree geometry, and at the optimal settings it is provably unreachable by any deterministic $\pm1$ assignment that depends on $\lambda$ only through the sub-ball structure. The model therefore does not explain the cosine; it assumes it.

### 4.5 The CHSH evaluation with fully shown arithmetic

Under A3 and A4, the correlation function is $E(\mathbf{a},\mathbf{b})=\cos(\theta_a-\theta_b)$ and the CHSH combination is

$$
S=\bigl|E(a,b)-E(a,b')+E(a',b)+E(a',b')\bigr|.
$$

Choose the Tsirelson-optimal angles

$$
a=0,\qquad a'=\frac{\pi}{2},\qquad b=\frac{\pi}{4},\qquad b'=\frac{3\pi}{4}.
$$

Compute each correlation from $E=\cos(\theta_a-\theta_b)$:

1. $E(a,b)=\cos(0-\pi/4)=\cos(-\pi/4)=\sqrt{2}/2$.
2. $E(a,b')=\cos(0-3\pi/4)=\cos(-3\pi/4)=-\sqrt{2}/2$.
3. $E(a',b)=\cos(\pi/2-\pi/4)=\cos(\pi/4)=\sqrt{2}/2$.
4. $E(a',b')=\cos(\pi/2-3\pi/4)=\cos(-\pi/4)=\sqrt{2}/2$.

Insert into the CHSH combination:

$$
\begin{aligned}
S&=\left|\frac{\sqrt{2}}{2}-\left(-\frac{\sqrt{2}}{2}\right)+\frac{\sqrt{2}}{2}+\frac{\sqrt{2}}{2}\right|\\[4pt]
&=\left|4\cdot\frac{\sqrt{2}}{2}\right|\\[4pt]
&=2\sqrt{2}\approx2.828427.
\end{aligned}
$$

For the local bound, the standard argument is re-derived here for self-containment. For any four correlations $E_1,E_2,E_3,E_4\in[-1,1]$ produced by a deterministic assignment $X(a,\lambda),X(a',\lambda),Y(b,\lambda),Y(b',\lambda)\in\{\pm1\}$ at each fixed $\lambda$, the CHSH combination at that $\lambda$ is

$$
s(\lambda)=X(a,\lambda)\bigl[Y(b,\lambda)+Y(b',\lambda)\bigr]+X(a',\lambda)\bigl[Y(b,\lambda)-Y(b',\lambda)\bigr].
$$

Since $Y(b,\lambda)+Y(b',\lambda)$ and $Y(b,\lambda)-Y(b',\lambda)$ cannot both be nonzero (one is $0$ whenever the other is $\pm2$), $|s(\lambda)|=2$ for every $\lambda$. Averaging over $\lambda$ and using $|E_1-E_2+E_3+E_4|\le\langle|s(\lambda)|\rangle=2$ gives the local bound $|S|\le2$; the model value $2\sqrt{2}\approx2.828427$ exceeds it by $2\sqrt{2}-2\approx0.828427$, exactly as quantum mechanics does.

**Diagnosis of the earlier convention.** The earlier version used the combination $S=\bigl|E(a,b)-E(a,b')\bigr|+\bigl|E(a',b)+E(a',b')\bigr|$ with $b'=-\pi/4$. With the same cosine postulate:

1. $E(a,b)=\sqrt{2}/2$, $E(a,b')=\cos(\pi/4)=\sqrt{2}/2$, $E(a',b)=\sqrt{2}/2$, $E(a',b')=\cos(3\pi/4)=-\sqrt{2}/2$.
2. First term: $\bigl|\sqrt{2}/2-\sqrt{2}/2\bigr|=0$.
3. Second term: $\bigl|\sqrt{2}/2+(-\sqrt{2}/2)\bigr|=0$.
4. Total: $S=0+0=0$.

The zero is a convention-and-angle artifact: the angle $b'=-\pi/4$ places $b'$ symmetrically opposite to $b$ relative to $a$, forcing exact cancellation in both absolute-value groups, and the split combination $|E_1-E_2|+|E_3+E_4|$ is not the standard CHSH form. Under the standard combination A4 and the angle $b'=3\pi/4$, the same cosine postulate gives $S=2\sqrt{2}$ with no scaling factor. The ad hoc factor $\kappa=\sqrt{2}$ of the earlier version is retracted: it was introduced to repair a cancellation created by the nonstandard convention, and with the corrected convention it is unnecessary. The corrected result is conditional: the model reaches the Tsirelson value if and only if the cosine postulate A3 is granted, and Section 4.4 shows that A3 is not derivable from the tree.

## 5. Results

The results of this paper, each computed in Section 4 with every arithmetic step shown, are:

1. The $3$-adic norm of $12/5$ is $\bigl|12/5\bigr|_3=1/3\approx0.333333$ (Section 4.1).
2. The probability that a Haar-uniform hidden variable $\lambda\in B(0,1)\subset\mathbb{Q}_3$ lies in the correlation-relevant sub-ball of radius $1/3$ is $P=1/3\approx0.333333$, and this value is independently reproduced by the maximum-entropy valuation distribution of [3] via $P(v_3\ge1)=1-P(v_3=0)=1-2/3=1/3$ (Section 4.2).
3. An assumed span of $14\times10^{9}$ years equals $4.418064\times10^{17}$ s at $365.25$ days per year; the input is an assumption of the computation, not a cited measurement (Section 4.3).
4. The deterministic sign rule of Section 3.2 cannot produce the postulated cosine correlation at the Tsirelson-optimal settings: the rule yields outcomes in $\{-1,0,+1\}$ with the degenerate value on at least $2/3$ of the hidden-variable space, and any repaired $\pm1$ rule produces correlations that are rational combinations over the three sub-balls, which cannot equal the irrational value $\sqrt{2}/2$ (Section 4.4).
5. Under the standard CHSH convention A4 and the cosine postulate A3, the model gives $S=2\sqrt{2}\approx2.828427$ at the angles $a=0$, $a'=\pi/2$, $b=\pi/4$, $b'=3\pi/4$, exceeding the re-derived local bound $|S|\le2$ by $0.828427$; the earlier convention with $b'=-\pi/4$ gives $S=0$, and the scaling factor $\kappa=\sqrt{2}$ is retracted as unnecessary (Section 4.5).

The central claim is accordingly downgraded: the model is *consistent with* the Tsirelson value conditional on an explicitly postulated cosine correlation; it does not *derive* that correlation, and Section 4.4 proves the postulate conflicts with the model's own deterministic outcome rule at the optimal settings.

## 6. Discussion

### 6.1 Limitations

- **The correlation postulate is unproven and provably non-derivable at the optimal settings.** The result $S=2\sqrt{2}$ rests entirely on A3. Section 4.4 shows that the deterministic sign rule produces only rational correlations over the sub-ball decomposition, so the irrational value $\sqrt{2}/2$ is unreachable from the tree geometry as formulated. Any future derivation of the cosine must modify either the outcome rule, the measure A1, or the encoding A2.
- **Degenerate outcomes.** The sign rule outputs $0$ on odd-distance hidden variables; the repair that maps these to $\pm1$ is unspecified, and different repairs give different correlations.
- **Discrete encoding.** The mapping from measurement settings to tree vertices is assumed arbitrarily refinable (A2); a physical or computational implementation imposes a minimal discretization, and the effect of a finite digit budget on $E$ is not computed here.
- **Single prime.** The analysis fixes $p=3$; the adelic setting of [5] treats all primes simultaneously, and nothing in this paper shows that the $p=3$ construction extends to, or is consistent with, the product formula $\prod|x|_p=1$ on principal ideles stated in [5].
- **Uniformity assumption.** The Haar measure A1 is an assumption; the agreement with the maximum-entropy distribution of [3] holds only on the single number $P=1/3$, and other distributional assumptions (for example the squarefree restriction of [3], which gives $P(v_p=1\mid\text{squarefree})=1/(p+1)=1/4$ at $p=3$) would change the extracted probability.
- **No decoherence.** Environmental interactions that could modify the hidden label $\lambda$ are ignored; the model addresses ideal measurements only.
- **Narrow literature base.** This paper rests on only 5 available works, and its literature treatment is correspondingly narrow; no survey of the Bell-inequality or hidden-variable literature beyond these works is attempted, and the framing assumptions of Section 1 are not sourced from the works cited here.
- **Motivation for $p=3$ is weak.** The variational motivation via the Zagreb bound $M_1(T)\ge9n-16$ of [1] is a degree-counting fact about finite trees, not a physical argument; it motivates $p=3$ only in the loose sense that $\mathcal{T}_3$ is $4$-regular and degree-$4$ trees attain the bound of [1].

### 6.2 What would falsify the claims

The main conditional result — that the model with A3 and A4 gives $S=2\sqrt{2}$ — is a mathematical identity given the assumptions, so it is falsified only by attacking the assumptions. The observation that would falsify the *program* is a completed derivation, from the tree geometry alone, of a correlation function $E(\theta_a,\theta_b)$ that is provably not of cosine form at fine encoding; conversely, a derivation of $E=\cos(\theta_a-\theta_b)$ from a modified outcome rule would overturn the central negative finding of Section 4.4. A concrete computational falsifier of the model as a whole is the Monte-Carlo test of Section 7.3: if the simulated hidden-variable rule with any natural repair of the degenerate outcomes yields $S_{\text{sim}}<2$ at all tested encodings, the model class cannot reproduce even the classical violation threshold, and the cosine postulate would stand exposed as an import from quantum theory with no ultrametric origin. On the empirical side, the prediction of [5] that improving local gate fidelity makes ultrametric error structure more visible is a testable companion claim; a null result at high gate fidelity would remove the nearest experimental hook for the model class.

### 6.3 Open questions

- Can a modified outcome rule — for example one that assigns outcomes by sub-ball membership rather than by the sign of $\cos(\pi d/2)$ — reproduce the cosine exactly, or is the cosine provably out of reach for any deterministic rule on $\mathcal{T}_3$ with a translation-invariant measure?
- Does the conflict found in Section 4.4 persist at other primes, or does the $(p+1)$-regular branching of $\mathcal{T}_p$ for larger $p$ change the rationality obstruction?
- How would a complete account lift the single-prime analysis to the adele ring of [5], and what role would the archimedean readout emphasized in [2] play in the measurement step?
- Can the maximum-entropy and Fermi–Dirac valuation statistics of [3] be used to derive outcome probabilities rather than postulate them?

## 7. Practical Implications and Engineering Pathways

### 7.1 Who would use the result and what changes

Researchers in quantum foundations and engineers building deterministic simulators of Bell-test experiments are the named users. If the conditional result holds and the cosine postulate is eventually derived from the tree, simulator designers could replace stochastic hidden-variable sampling with a concrete ultrametric architecture, and certification protocols for entanglement-based key distribution would gain a constructive causal picture of what the certified non-locality consists of. If the negative result of Section 4.4 stands, protocol designers gain the assurance that this ultrametric model class cannot undermine device-independent certification without importing quantum postulates. Until the postulate is derived, the result changes no engineering practice; it is foundational work whose value is the sharpened statement of what must be derived.

### 7.2 Technology readiness

This work is purely analytical and has not been peer reviewed. Against the NASA Technology Readiness Level definitions it resides at TRL 1–2: basic principles are stated and the arithmetic is shown, but no proof-of-concept application exists. Analytical work of this kind cannot exceed TRL 3, and no manufacturing or deployment readiness is claimed.

### 7.3 The smallest next test

The smallest de-risking calculation is a Monte-Carlo simulation of the hidden-variable rule of Section 3.2 for $p=3$ on a finite-depth tree (depth $5$), written as a proposal: the simulation would sample $\lambda$ uniformly from a discretized $B(0,1)$, apply the outcome rule with a stated repair of the degenerate cases, and compute the empirical CHSH value $S_{\text{sim}}$ as the sample size $N$ grows. The outcome $S_{\text{sim}}\approx2.828$ would support the cosine postulate as emergent; the outcome $S_{\text{sim}}<2$ at all tested encodings would falsify the model class as a reproduction of quantum correlations. Given the rationality obstruction of Section 4.4, the expected outcome is the falsifier, which is itself informative: it would confirm that the cosine must come from elsewhere.

### 7.4 Engineering constraints that would bind first

- **Encoding precision.** Mapping continuous angles to discrete $p$-adic integers must preserve the intended ultrametric distances; the digit budget bounds the achievable angular resolution and is the first binding constraint in any simulation.
- **Randomness source.** Uniform sampling of ancestor nodes $\lambda$ requires a high-quality pseudo-random generator; bias in the sampler would distort $E$ in ways that could mimic or mask a violation.
- **Software.** A $p$-adic arithmetic library capable of evaluating norms, ball decompositions and characters for large ensembles is required; the undefined $\exp_p$ of the earlier version must not reappear.
- **Tree depth versus compute.** Deeper trees refine the distance resolution but increase the sample cost linearly in depth and the encoding precision requirement exponentially; the trade-off is unquantified here and is an open question.

### 7.5 Projected cost bounds (projection)

As a projection with stated assumptions: assuming a standard workstation at approximately $2\times10^{3}$ USD, open-source $p$-adic libraries, no specialized hardware, and a sample size $N=10^{6}$, the statistical uncertainty on $S_{\text{sim}}$ scales as $1/\sqrt{N}\approx10^{-3}$, and the projected cost of the simulation pilot is below $10^{4}$ USD. These figures assume the workstation cost and the sample size as inputs; they are not derived from the model.

### 7.6 Risks and misuse

If the deterministic claim is misread as evidence that quantum randomness is illusory, it could prompt premature abandonment of stochastic methods in quantum cryptography. The corrected paper mitigates this by stating the result conditionally: the model reproduces the Tsirelson value only if a cosine postulate is granted, and that postulate is shown to conflict with the model's own outcome rule. Any reuse of the earlier version's numbers should note the corrections documented here, in particular the $S=0$ artifact of the earlier convention.

## 8. Conclusion

This paper corrected four defects in an earlier claim that a $p$-adic common-ancestor hidden-variable model demonstrates quantum-like correlations. The undefined function $\exp_p$ is removed; the correlation function $E(\mathbf{a},\mathbf{b})=\cos(\theta_a-\theta_b)$ is restated as an explicit postulate rather than a derived result; the CHSH evaluation is supplied with every arithmetic step, giving $S=2\sqrt{2}\approx2.828427$ under the standard convention and angles, and documenting that the earlier convention with $b'=-\pi/4$ yields $S=0$; and the ad hoc scaling factor $\kappa=\sqrt{2}$ is retracted as a repair of that convention artifact. The corrected conclusion is conditional: the model is consistent with the Tsirelson value if the cosine postulate is granted, and the postulate is shown to be unreachable from the model's own deterministic outcome rule at the optimal settings, since the rule produces only rational correlations over the sub-ball decomposition while $\sqrt{2}/2$ is irrational. Deriving the cosine from ultrametric geometry — or proving it cannot be done — is the central open problem of this program, and the Monte-Carlo test proposed in Section 7.3 is the smallest next step that would settle which branch holds.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.3). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 9 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[2] https://papers.qnfo.org/papers/tate-adelic-template. QNFO: Tate's Thesis as a Template for Adelic Quantum Mechanics: Local-Global Structure and the Emergence of Archimedean Artifacts.
[3] https://papers.qnfo.org/papers/self-referential-scalar-family. QNFO: The Self-Referential Scalar Family: e, the Half-Turn, and the Unification of Information Theory, Statistics, Thermodynamics, and QND Measurement in the Adelic Picture.
[4] https://papers.qnfo.org/papers/ultrametric-p-adic-metrology. QNFO: Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology.
[5] https://papers.qnfo.org/papers/adelic-quantum-error-correction-a-synthesis-across-all-primes-v1-0-0. QNFO: Adelic Quantum Error Correction: A Synthesis Across All Primes v1.0.0.
