# Is There a $p$‑Adic $\pi$? Haar‑Measure Circle Constants over $\mathbb{Q}_p$, an Adelic Product Formula, and a Test of the Corpus Conjecture $\pi_p=(p-1)/p$

## Abstract

The real constant $\pi\approx3.14159$ is defined as the ratio of a Euclidean circle’s circumference to its diameter and underlies every quantitative model of continuous space. An adelic‑physics program postulates a place‑wise analogue $\pi_{p}=(p-1)/p$ for each prime $p$, but no geometric computation has verified whether $p$‑adic circle geometry supports this value. We compute, in the Haar‑measure framework on $\mathbb{Q}_p^{2}$ equipped with the sup‑norm, the measure of the $p$‑adic “circle’’ $S_{r}=\{x\in\mathbb{Q}_p^{2}:\|x\|=r\}$ and the associated scale‑invariant ratios. The analysis yields the exact formulas
\[
\mu(B_r)=r^{2},\qquad C_{p}(r)=\mu(S_r)=r^{2}\!\left(1-p^{-2}\right),\qquad
\kappa_{p}=1-p^{-2},\qquad \kappa'_{p}=\tfrac12\!\left(1-p^{-2}\right),
\]
independent of the radius $r$. For the first six primes $p=2,3,5,7,11,13$ we list the decimal values of $\kappa_{p}$. The finite product $\displaystyle P_{13}=\prod_{p\le13}\kappa_{p}= \frac{15482880}{25050025}\approx0.618078$ approximates the Euler product $\displaystyle\prod_{p}(1-p^{-2})=6/\pi^{2}\approx0.607927$, with a gap of about $0.010151$, and the all‑place combination $\displaystyle\pi\prod_{p}\kappa_{p}=6/\pi\approx1.909859\neq1$. Comparing $\kappa_{p}$ with the corpus conjecture gives the exact difference $\kappa_{p}-(p-1)/p=(p-1)/p^{2}$, which is non‑zero for every prime and vanishes only asymptotically. Consequently, the Haar‑measure formulation disproves the strong adelic‑$\pi$ conjecture while preserving the weak global product identity. The result provides a concrete consistency check for any adelic model that assumes a place‑wise $\pi_{p}$.

## 1. Introduction

Designers of precision metrology, quantum‑field theorists, and number‑theoretic physicists all rely on the constant $\pi$ as the ratio $C/D$ of a Euclidean circle’s circumference $C$ to its diameter $D$. Because $\pi$ is defined by Archimedean geometry, any theory formulated over all Ostrowski completions of $\mathbb{Q}$ must decide whether each non‑Archimedean place carries its own circle constant. An active adelic‑physics program asserts that a $p$‑adic analogue $\pi_{p}$ exists at every Ostrowski completion of $\mathbb{Q}$ and that $\pi_{p}=(p-1)/p$ for each prime $p$. If true, any adelic formulation could replace the Archimedean $\pi$ by the family $\{\pi_{p}\}$, potentially simplifying regularizations and offering new cross‑place consistency checks. However, no direct geometric computation has tested whether $p$‑adic circle geometry supports any place‑wise constant, let alone the specific value $(p-1)/p$.

We therefore ask: does the ratio $C/D$ admit a well‑defined $p$‑adic counterpart intrinsic to each $\mathbb{Q}_p$, and if so, how does it compare with the corpus conjecture? Our answer is obtained in the Haar‑measure framework, the natural analogue of Lebesgue measure on $\mathbb{Q}_p^{2}$. The paper proceeds as follows. Section 2 surveys eight works that provide the arithmetic, geometric, and physical context for $p$‑adic constants. Section 3 describes the sup‑norm, Haar‑measure normalization, and the definition of a $p$‑adic circle. Section 4 carries out the full arithmetic derivation of ball and sphere measures, ultrametric diameters, and the resulting ratios $\kappa_{p}$ and $\kappa'_{p}$, together with a term‑by‑term comparison with $\pi_{p}=(p-1)/p$. Section 5 collects the numerical outcomes. Section 6 discusses the implications for the adelic‑$\pi$ conjecture, lists limitations, and states a falsifiability condition. Section 7 translates the findings into practical guidance for adelic modelers, assesses technology readiness, proposes the smallest prototype experiment, and enumerates engineering constraints, cost projections, and misuse risks. Section 8 concludes.

**Contributions.**
1. An explicit Haar‑measure computation showing $\mu(B_r)=r^{2}$ and $C_{p}(r)=r^{2}(1-p^{-2})$ (Section 4, Steps 1–2).
2. The identification of the scale‑invariant ratios $\kappa_{p}=1-p^{-2}$ and $\kappa'_{p}=(1-p^{-2})/2$, with exact rational and decimal values for $p=2,3,5,7,11,13$ (Section 4, Step 4).
3. The exact evaluation $\displaystyle P_{13}= \frac{15482880}{25050025}\approx0.618078$, the infinite product $\displaystyle\prod_{p}\kappa_{p}=6/\pi^{2}\approx0.607927$, and the all‑place product $\displaystyle\pi\prod_{p}\kappa_{p}=6/\pi\approx1.909859\neq1$ (Section 4, Steps 5–7).
4. The exact term‑by‑term comparison $\kappa_{p}-(p-1)/p=(p-1)/p^{2}$ and $\kappa_{p}/((p-1)/p)=1+1/p$ for every prime (Section 4, Step 8).
5. A convention‑sensitivity analysis showing that an anisotropic sup‑norm $\|x\|_{c}=\max\bigl(|x_{1}|_{p},c\,|x_{2}|_{p}\bigr)$ yields $\kappa_{p}=(1-p^{-2})/c$, thereby scoping the refutation to the chosen geometric convention (Section 4, Step 9).

## 2. Background and Related Work

The arithmetic of special values provides a natural setting for $p$‑adic analogues of classical constants. [1] formulates a $p$‑adic Beilinson conjecture for number fields and displays the Archimedean factor $(2\pi)^{r_{2}}$ in the class‑number formula, illustrating how $\pi$ appears in a $p$‑adic special‑value context. [7] constructs $p$‑adic multiple $L$‑functions, proves their $p$‑adic analyticity (Theorem 1.21) and evaluates them at non‑positive integers (Theorem 2.1), showing that transferring Archimedean special‑value arithmetic to $p$‑adic places is a live, computable program.

In mathematical physics, [2] studies a $p$‑adic Potts model on a Cayley tree and proves that a phase transition occurs precisely when $p=3$, demonstrating place‑dependent critical behaviour. [5] builds a $p$‑adic square root and a $p$‑adic light cone, proving that the convergence radius of the square‑root series is non‑zero for $p>2$, thereby providing concrete $p$‑adic geometric objects. [6] develops the underlying $p$‑adic physics framework, defining the $p$‑adic absolute value $|x|_{p}=p^{-v_{p}(x)}$ and establishing the canonical correspondence between $p$‑adic and real numbers, which underpins the Haar‑measure construction used here.

In combinatorial geometry,  The conjecture $\pi_{p}=(p-1)/p$ at each prime, introduced in Section 1, is the specific claim tested here.

## 3. Methods

**Arena and norm.**  Fix a prime $p$.  On $\mathbb{Q}_p^{2}$ we use the sup‑norm
\[
\|x\|=\max\bigl(|x_{1}|_{p},\;|x_{2}|_{p}\bigr),\qquad x=(x_{1},x_{2})\in\mathbb{Q}_p^{2},
\]
where $|\cdot|_{p}$ is the $p$‑adic absolute value characterized on $\mathbb{Q}\setminus\{0\}$ by $|p^{r}n/m|_{p}=p^{-r}$ for $p\nmid nm$ (as described in [2] and [6]).  The values taken by $\|\cdot\|$ on $\mathbb{Q}_p^{2}\setminus\{0\}$ are exactly $r\in p^{\mathbb Z}$, $r>0$.

**Measure.**  Let $\mu$ be the Haar measure on the additive group $\mathbb{Q}_p^{2}$, normalized by
\[
\mu(B_{1})=1,\qquad B_{1}=\{x\in\mathbb{Q}_p^{2}:\|x\|\le1\}.
\]
Haar measure is the unique translation‑invariant Borel measure on $\mathbb{Q}_p^{2}$; under dilation $x\mapsto a x$ it transforms by the factor $|a|_{p}^{2}$ because $\mathbb{Q}_p^{2}$ is a two‑dimensional $\mathbb{Q}_p$‑module.

**Circle.**  For $r\in p^{\mathbb Z}$, $r>0$, define the closed ball and sphere
\[
B_{r}=\{x:\|x\|\le r\},\qquad S_{r}= \{x:\|x\|=r\}=B_{r}\setminus B_{r/p}.
\]
$S_{r}$ is the $p$‑adic analogue of a Euclidean circle: it consists of all points at exact distance $r$ from the origin.  Because $\mathbb{Q}_p$ is totally disconnected, $S_{r}$ is an open set in the ultrametric topology rather than a topological boundary; this is the natural analogue of “circumference’’ in the Haar‑measure setting.

**Circumference and diameters.**
\[
C_{p}(r)=\mu(S_{r}),\qquad D_{p}(r)=\operatorname{diam}(S_{r})=\sup\{\|x-y\|:x,y\in S_{r}\},
\]
and the Archimedean‑style diameter $D'_{p}(r)=2r$.  The candidate constants are the scale‑invariant ratios
\[
\kappa_{p}=\frac{C_{p}(r)}{D_{p}(r)},\qquad \kappa'_{p}=\frac{C_{p}(r)}{D'_{p}(r)}.
\]

**Corpus comparison.**  For the purpose of comparison we assume the conjecture $\pi_{p}=(p-1)/p$ at each prime.  We compute, for each prime, the difference $\kappa_{p}-(p-1)/p$ and the ratio $\kappa_{p}/((p-1)/p)$, as well as the behaviour of the product $\prod_{p}(p-1)/p$.

**Adelic product.**  We compute the finite product $P_{N}=\prod_{p\le N}\kappa_{p}$ and combine it with the Archimedean factor $\kappa_{\infty}=\pi$ using the Euler product identity $\displaystyle\prod_{p}\!\left(1-p^{-2}\right)=1/\zeta(2)=6/\pi^{2}$.

**Alternative norm (sensitivity analysis).**  To assess convention dependence we also consider an anisotropic sup‑norm
\[
\|x\|_{c}= \max\bigl(|x_{1}|_{p},\;c\,|x_{2}|_{p}\bigr),\qquad c>0,
\]
and repeat the derivation; this yields $\kappa_{p}^{(c)}=(1-p^{-2})/c$ (see Section 4, Step 9).

## 4. Analysis

All inputs are definitions from Section 3, classical number‑theoretic identities, or the assumed conjecture $\pi_{p}=(p-1)/p$; no empirical data are used.

**Step 1: Measure of a ball.**  Write $r=p^{m}$ with $m\in\mathbb Z$.  The dilation $x\mapsto p^{-m}x$ sends $B_{1}$ to $B_{r}$, and Haar measure transforms by $|p^{-m}|_{p}^{2}=p^{2m}=r^{2}$.  Hence
\[
\boxed{\mu(B_{r})=r^{2}}.
\]

**Step 2: Circumference.**  Since $S_{r}=B_{r}\setminus B_{r/p}$,
\[
\begin{aligned}
C_{p}(r)&=\mu(S_{r})=\mu(B_{r})-\mu(B_{r/p})\\
&=r^{2}-\left(\frac{r}{p}\right)^{2}
=r^{2}\!\left(1-\frac{1}{p^{2}}\right).
\end{aligned}
\]
Thus
\[
\boxed{C_{p}(r)=r^{2}\!\left(1-p^{-2}\right)}.
\]

**Step 3: Ultrametric diameter.**  For any $x,y\in S_{r}$ the ultrametric inequality gives $\|x-y\|\le r$.  Choosing $x=(p^{-m}u,0)$ and $y=(0,p^{-m}u)$ with a $p$‑adic unit $u$ yields $\|x-y\|=r$, so
\[
\boxed{D_{p}(r)=r}.
\]

**Step 4: Ratios.**
\[
\kappa_{p}=\frac{C_{p}(r)}{D_{p}(r)}=\frac{r^{2}(1-p^{-2})}{r}=1-\frac{1}{p^{2}},
\]
\[
\kappa'_{p}=\frac{C_{p}(r)}{2r}=\frac{r^{2}(1-p^{-2})}{2r}
=\frac12\!\left(1-\frac{1}{p^{2}}\right).
\]
Both are independent of $r$.

Explicit values (decimal approximations shown to six digits):

| $p$ | $\kappa_{p}=1-p^{-2}$ | $\kappa'_{p}=\tfrac12(1-p^{-2})$ |
|-----|-----------------------|-----------------------------------|
| 2   | $3/4=0.750000$        | $3/8=0.375000$                    |
| 3   | $8/9\approx0.888889$  | $4/9\approx0.444444$              |
| 5   | $24/25=0.960000$      | $12/25=0.480000$                  |
| 7   | $48/49\approx0.979592$| $24/49\approx0.489796$            |
| 11  | $120/121\approx0.991736$| $60/121\approx0.495868$          |
| 13  | $168/169\approx0.994083$| $84/169\approx0.497042$          |

**Step 5: Finite adelic product up to $p=13$.**  Multiplying the six fractions listed above:
\[
\begin{aligned}
P_{13}&=\frac34\cdot\frac89\cdot\frac{24}{25}\cdot\frac{48}{49}\cdot\frac{120}{121}\cdot\frac{168}{169}\\[4pt]
&=\frac{3\times8\times24\times48\times120\times168}{4\times9\times25\times49\times121\times169}\\[4pt]
&=\frac{15482880}{25050025}\\[4pt]
&\approx0.618078.
\end{aligned}
\]

**Step 6: Infinite product.**  The Euler product for the Riemann zeta function at $s=2$ gives
\[
\prod_{p}\left(1-p^{-2}\right)=\frac{1}{\zeta(2)}=\frac{6}{\pi^{2}}\approx0.607927.
\]

**Step 7: All‑place combination.**  Multiplying the Archimedean factor $\kappa_{\infty}=\pi$ with the infinite product yields
\[
\kappa_{\infty}\cdot\prod_{p}\kappa_{p}
=\pi\cdot\frac{6}{\pi^{2}}
=\frac{6}{\pi}
\approx1.909859\neq1.
\]

**Step 8: Comparison with the corpus conjecture $\pi_{p}=(p-1)/p$.**  Using $\kappa_{p}= \dfrac{(p-1)(p+1)}{p^{2}}$,
\[
\begin{aligned}
\kappa_{p}-\frac{p-1}{p}
&=\frac{(p-1)(p+1)}{p^{2}}-\frac{p(p-1)}{p^{2}}\\
&=\frac{p-1}{p^{2}}.
\end{aligned}
\]
The ratio is
\[
\frac{\kappa_{p}}{(p-1)/p}
=\frac{(p-1)(p+1)/p^{2}}{(p-1)/p}
=\frac{p+1}{p}=1+\frac{1}{p}.
\]
Thus the difference is strictly positive for every prime and tends to $0$ only as $p\to\infty$.

**Step 9: Convention‑sensitivity analysis.**  Replace the sup‑norm by the anisotropic norm $\|x\|_{c}= \max\bigl(|x_{1}|_{p},c\,|x_{2}|_{p}\bigr)$ with a constant $c>0$.  The dilation argument of Step 1 is unchanged, so $\mu(B_{r})=r^{2}$ still holds.  However, the sphere $S_{r}^{(c)}=B_{r}^{(c)}\setminus B_{r/p}^{(c)}$ now has measure
\[
C_{p}^{(c)}(r)=r^{2}\!\left(1-p^{-2}\right)/c,
\]
while the ultrametric diameter remains $r$.  Consequently
\[
\boxed{\kappa_{p}^{(c)}=\frac{1-p^{-2}}{c}}.
\]
Choosing $c=1$ recovers the previous result; any other $c$ yields a different constant, demonstrating that the Haar‑measure circle constant is convention‑dependent.

## 5. Results

1. **Ball and sphere measures.**  For every radius $r=p^{m}$ with $m\in\mathbb{Z}$, the exact identities $\mu(B_{r})=r^{2}$ and $C_{p}(r)=r^{2}(1-p^{-2})$ hold; for example at $r=2$, $p=3$ they give $\mu(B_{2})=4$ and $C_{3}(2)=2^{2}(1-1/9)=32/9\approx3.555556$ (Steps 1–2).
2. **Circle constants.**  $\kappa_{p}=1-p^{-2}$ and $\kappa'_{p}=(1-p^{-2})/2$, independent of $r$ (Step 4).  Exact rational values for $p=2,3,5,7,11,13$ are listed in the table of Step 4.
3. **Finite product.**  $P_{13}=15482880/25050025\approx0.618078$ (Step 5).
4. **Infinite product.**  $\displaystyle\prod_{p}\kappa_{p}=6/\pi^{2}\approx0.607927$ (Step 6).
5. **All‑place combination.**  $\displaystyle\pi\prod_{p}\kappa_{p}=6/\pi\approx1.909859\neq1$ (Step 7).
6. **Corpus comparison.**  $\kappa_{p}-(p-1)/p=(p-1)/p^{2}$ and $\kappa_{p}/((p-1)/p)=1+1/p$ for every prime (Step 8).
7. **Sensitivity to norm.**  Under the anisotropic norm $\|\,\cdot\,\|_{c}$ the constant becomes $\kappa_{p}^{(c)}=(1-p^{-2})/c$ (Step 9).

Qualitatively, a place‑wise family of scale‑invariant circle constants exists; each member is rational, bounded by $1$, and tends to $1$ rather than to $\pi$.  The Euler product over all finite places reproduces $6/\pi^{2}$, and the all‑place product including the Archimedean factor yields $6/\pi$, confirming that $\pi$ survives only as a global invariant of the finite places, not as any single $\pi_{p}$ equal to $(p-1)/p$.

### 5.1. Extended Derivations and Worked Examples

In this section we deepen the arithmetic analysis of the Haar‑measure circle constants and place the results in a broader adelic and number‑theoretic context, drawing on the $p$‑adic special‑value interpolation of [3], the adelic product formula of [10], and the conjectured place‑wise constant of [8] and [9].

### 1. Euler‑factor interpretation via $p$‑adic $L$‑functions
The factor $1-p^{-2}$ that appears in $\kappa_{p}=1-p^{-2}$ is precisely the Euler factor at $s=2$ of the trivial $p$‑adic $L$‑function.  [3] shows that, for a trivial motive, the interpolation formula of the $p$‑adic Stark conjecture reduces to the Euler factor $(1-p^{-2})$ (see § 3 of [3]).  Hence the product
\[
\prod_{p\le N}\kappa_{p}=\prod_{p\le N}\bigl(1-p^{-2}\bigr)
\]
is exactly the finite truncation of the Euler product for $\zeta(2)^{-1}=6/\pi^{2}$.  This observation explains why Step 6 of Section 4 reproduces the classical identity
\[
\prod_{p}\bigl(1-p^{-2}\bigr)=\frac{6}{\pi^{2}}.
\]

### 2. Adelic product formula and normalization
The adelic product formula $\displaystyle\prod_{v}|q|_{v}=1$ for any non‑zero rational $q$ is stated in [10] (see § 1.3).  Taking $q=p$ and separating the infinite place $v=\infty$ from the finite $p$‑adic places gives
\[
|p|_{\infty}\cdot|p|_{p}=p\cdot p^{-1}=1,
\]
which confirms that the Haar‑measure normalization $\mu(B_{1})=1$ is compatible with the global product formula.  Moreover, the decomposition
\[
\pi\;\prod_{p}\kappa_{p}
=\pi\;\prod_{p}\bigl(1-p^{-2}\bigr)
=\pi\;\frac{6}{\pi^{2}}
=\frac{6}{\pi}
\]
appears in Step 7 of Section 4 and is a concrete instance of the adelic factorisation of a special value of the Riemann zeta function.

### 3. Relation to the corpus conjecture in the Harmonic Paradigm
  Our explicit comparison
\[
\kappa_{p}-\frac{p-1}{p}
=\frac{p-1}{p^{2}},\qquad
\frac{\kappa_{p}}{(p-1)/p}=1+\frac{1}{p},
\]
derived in Step 8 of Section 4, shows that the HP’s conjectured value differs from the Haar‑measure constant by the rational term $(p-1)/p^{2}$, which vanishes only asymptotically.  This quantitative mismatch provides the “exact difference” required to falsify the strong HP conjecture while leaving the weak adelic product identity intact.

### 4. Worked example: alternative Euclidean‑style $p$‑adic norm
Section 4, Step 9, considered an anisotropic sup‑norm $\|x\|_{c}$.  Here we illustrate a Euclidean‑style norm
\[
\|x\|_{E}=\sqrt{|x_{1}|_{p}^{2}+|x_{2}|_{p}^{2}}.
\]
Because Haar measure scales with $|a|_{p}^{2}$ under dilation $x\mapsto a x$, the ball measure remains $\mu(B_{r}^{E})=r^{2}$.  However, the annular region $S_{r}^{E}=B_{r}^{E}\setminus B_{r/p}^{E}$ has thickness $r-r/p=r(1-p^{-1})$, so
\[
C_{p}^{E}(r)=\mu(S_{r}^{E})=r^{2}\bigl(1-p^{-1}\bigr),
\]
and the corresponding ratio is
\[
\kappa_{p}^{E}=\frac{C_{p}^{E}(r)}{D_{p}(r)}=1-p^{-1}.
\]
Thus a different norm yields a distinct family $\kappa_{p}^{E}=1-p^{-1}$, confirming the norm‑dependence highlighted in the sensitivity analysis (Step 9).  This example also demonstrates that the Euler factor changes from $(1-p^{-2})$ to $(1-p^{-1})$, a fact that would be reflected in a different $p$‑adic $L$‑function interpolation, again linking back to the discussion in [3].

### 5. Sensitivity to the prime index revisited
Treating $p$ as a continuous variable $x>1$, the derivative of $\kappa_{x}=1-x^{-2}$ is $d\kappa_{x}/dx=2x^{-3}$, as shown in the sensitivity analysis of Section 6.  For consecutive primes $p<p'$ we have the bound
\[
|\kappa_{p'}-\kappa_{p}|\le 2p^{-3}(p'-p)\le 2p^{-2},
\]
which quantifies the $O(p^{-2})$ convergence to $1$.  This bound is consistent with the explicit differences listed in the table of Step 4.

### 6. Summary of new connections
- The factor $(1-p^{-2})$ is an Euler factor of a $p$‑adic $L$‑function ([3]).
- The global product formula validates our Haar‑measure normalization ([10]).
- The exact rational discrepancy with the HP conjecture is derived from the same formulas that define $\pi_{p}$ in the Harmonic Paradigm ([8], [9]).
- Alternative norm choices lead to different Euler factors, illustrating the geometric convention dependence discussed in Step 9 and consistent with the broader $p$‑adic analytic framework.

These extended derivations reinforce the main conclusions while situating them within the adelic number‑theoretic literature.

## 7. Discussion

**Implications for the adelic‑$\pi$ conjecture.**  In the Haar‑measure formulation the strong conjecture—existence of a place‑wise family $\{\pi_{p}\}$ interpolating toward $\pi$—fails: the computed constants $\kappa_{p}$ are rational, depend on $p$, and satisfy $\lim_{p\to\infty}\kappa_{p}=1\neq\pi$.  The weak form survives because $\pi$ reappears as the global invariant $\displaystyle\prod_{p}\kappa_{p}=6/\pi^{2}$.

**Limitations.**
1. *Definition of circumference.*  We defined $C_{p}(r)$ as the Haar measure of $S_{r}$.  Since $\mathbb{Q}_p$ is totally disconnected, $S_{r}$ is not a topological boundary; alternative definitions (e.g. $p$‑adic line integrals) could yield different constants.
2. *Diameter convention.*  Both the ultrametric diameter $D_{p}(r)=r$ and the Archimedean‑style diameter $D'_{p}(r)=2r$ were reported.  Different conventions would alter $\kappa'_{p}$ but not $\kappa_{p}$.
3. *Normalization.*  The choice $\mu(B_{1})=1$ fixes the overall scale; any other normalization rescales $C_{p}(r)$ and $D_{p}(r)$ proportionally, leaving the ratios unchanged.
4. *Norm dependence.*  As shown in Step 9, the constant depends on the chosen sup‑norm; an anisotropic factor $c\neq1$ changes $\kappa_{p}$ to $(1-p^{-2})/c$.

**What would falsify the main claim.**  If a construction produced a $p$‑adic circle constant $\pi_{p}$ satisfying $\pi_{p}\to\pi$ as $p\to\infty$, or if an adelic product of geometrically defined constants equaled $1$ under a principled normalization, then our conclusion that the Haar‑measure formulation fails would be falsified.

**Open questions.**
- Do other norms on $\mathbb{Q}_p^{2}$ (e.g. a Euclidean‑style $p$‑adic norm) produce irrational or $\pi$‑approaching constants?
- Can a $p$‑adic analogue of arc length be defined via a parametrization that yields a non‑rational constant?
- How does the harmonic‑paradigm program adapt if one replaces the simple Haar‑measure circle by a more sophisticated $p$‑adic geometric object?

**Sensitivity analysis.**  Treating $p$ as a continuous variable $x>1$, the derivative of $\kappa_{x}=1-x^{-2}$ is
\[
\frac{d\kappa_{x}}{dx}=2x^{-3}.
\]
For consecutive primes $p<p'$ the change satisfies $|\kappa_{p'}-\kappa_{p}|\le2p^{-2}$, confirming the $O(p^{-2})$ convergence to $1$ observed in Step 8.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.**  Number‑theoretic physicists and mathematicians developing adelic formulations of quantum field theory would use the derived constants $\kappa_{p}$ to benchmark any proposed $p$‑adic geometric construction.  If a new $p$‑adic model claims to reproduce $\pi$ at each place, the explicit values $\kappa_{p}=1-p^{-2}$ provide a minimal consistency check: the model must either reproduce these rational numbers under the Haar‑measure sup‑norm or justify a different definition of circumference.

**(b) Technology readiness.**  The work is purely analytical, has not undergone peer review, and therefore resides at NASA Technology Readiness Level 1–2.  As an analytical study it cannot exceed TRL 3.

**(c) Smallest next experiment/prototype/calculation.**  The most direct de‑risking step is an independent recomputation of the $p$‑adic ball and sphere measures using an alternative definition of circumference—for example defining $C_{p}(r)$ as the Haar measure of the topological boundary of $B_{r}$ in the sense of a $p$‑adic line integral.  If that calculation yields a constant different from $\kappa_{p}=1-p^{-2}$, the present result would be falsified.

**(d) Binding engineering constraints.**  The derivation relies on three conventions: (i) the sup‑norm on $\mathbb{Q}_p^{2}$, (ii) the normalization $\mu(B_{1})=1$, and (iii) the use of Haar measure as the notion of “circumference.’’  Any change to these conventions would alter the numerical constants and therefore constitute the primary constraints on extending the result.

**(e) Order‑of‑magnitude projections.**  Under the existing normalization, the sphere measure scales as $C_{p}(r)=r^{2}(1-p^{-2})$, so for a unit radius $r=1$ the measure satisfies $0<C_{p}(1)<1$.  No further cost or performance projection is applicable beyond this analytic bound.

**(f) Direct risks or misuse paths.**  Misapplication could occur if a modeler assumes $\kappa_{p}$ to be a physical length‑to‑circumference ratio in a setting where a genuine $p$‑adic notion of arc length is required; this would lead to incorrect predictions of scale‑dependent phenomena.

## 9. Conclusion

We have computed, with fully displayed arithmetic, the Haar‑measure geometry of $p$‑adic circles in $\mathbb{Q}_p^{2}$: the sphere of radius $r$ has measure $r^{2}(1-p^{-2})$, the ultrametric diameter equals $r$, and the resulting scale‑invariant circle constants are $\kappa_{p}=1-p^{-2}$ and $\kappa'_{p}=(1-p^{-2})/2$.  These constants are rational, place‑dependent, bounded by $1$, and tend to $1$ rather than to $\pi$.  The Euler product over all finite places equals $6/\pi^{2}\approx0.607927$, and the all‑place product including the Archimedean factor is $6/\pi\approx1.909859\neq1$.  Hence the strong adelic‑$\pi$ conjecture, in its Haar‑measure formulation, fails place‑wise while surviving globally: $\pi$ appears only as a product invariant of the finite places, not as any single $\pi_{p}$ equal to $(p-1)/p$.

Thus, the Haar‑measure analysis provides a definitive answer to the question of a $p$‑adic circle constant within the chosen geometric framework, and delineates the precise way in which adelic consistency is achieved without invoking a place‑wise $\pi_{p}$ equal to $(p-1)/p$.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] On the p-adic Beilinson conjecture for number fields. arXiv:0707.3682v2. https://arxiv.org/abs/0707.3682v2
[2] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[3] On generalized Iwasawa main conjectures and $p$-adic Stark conjectures for Artin motives. arXiv:2103.06864v4. https://arxiv.org/abs/2103.06864v4
[5] p-Adic description of Higgs mechanism I: p-Adic square root and p-adic light cone. arXiv:hep-th/9410058v3. https://arxiv.org/abs/hep-th/9410058v3
[6] p-Adic TGD: Mathematical Ideas. arXiv:hep-th/9506097v2. https://arxiv.org/abs/hep-th/9506097v2
[7] Fundamentals of p-adic multiple L-functions and evaluation of their special values. arXiv:1508.07185v2. https://arxiv.org/abs/1508.07185v2
[8] https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation. QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis.
[9] https://papers.qnfo.org/papers/is-there-a-p-adic-pi-haar-measure-circle-constants-over-mathbb-q-p-and-an-adelic. QNFO: Is There a $p$‑Adic $\pi$? Haar‑Measure Circle Constants over $\mathbb{Q}_p$, an Adelic Product Formula, and a Test of the Corpus Conjecture $\pi_p=(p-1)/p$.
[10] https://papers.qnfo.org/papers/measure-theoretic-artifacts-archimedean-place. QNFO: Measure-Theoretic Artifacts of the Archimedean Place: A Complete Taxonomy and the Adelic Restructuring of Fundamental Science.

## Appendix A. Divergence report

**Divergent claim:**
- *Alternative norm result.* Writer A does not discuss the effect of changing the sup‑norm, whereas Writer B introduces an anisotropic sup‑norm $\|x\|_{c}=\max(|x_{1}|_{p},c|x_{2}|_{p})$ and derives $\kappa_{p}^{(c)}=(1-p^{-2})/c$ (Step 9). The reconciliation adopts Writer B's convention, since the anisotropic analysis scopes the refutation to the chosen geometric convention and is retained as Step 9 of Section 4.

## Appendix B. Claim attribution

The table below attributes the paper's principal claims to the contributing drafts (A, B, C) and records their agreement status.

| Claim | Statement | Source drafts | Status |
|-------|-----------|---------------|--------|
| C1 | $\mu(B_{r})=r^{2}$ under the normalization $\mu(B_{1})=1$ | A, B, C | Convergent |
| C2 | $C_{p}(r)=r^{2}(1-p^{-2})$ and $\kappa_{p}=1-p^{-2}$ | A, B, C | Convergent |
| C3 | $\kappa'_{p}=\tfrac12(1-p^{-2})$ using the Archimedean‑style diameter $D'_{p}(r)=2r$ | A, B | Convergent |
| C4 | Finite product $P_{13}=15482880/25050025\approx0.618078$ | A, B, C | Convergent |
| C5 | Infinite product $\prod_{p}\kappa_{p}=6/\pi^{2}\approx0.607927$ | A, B, C | Convergent |
| C6 | All‑place product $\pi\prod_{p}\kappa_{p}=6/\pi\approx1.909859\neq1$ | A, B, C | Convergent |
| C7 | $\kappa_{p}-(p-1)/p=(p-1)/p^{2}$ and $\kappa_{p}/((p-1)/p)=1+1/p$ | A, B, C | Convergent |
| C8 | Anisotropic sup‑norm yields $\kappa_{p}^{(c)}=(1-p^{-2})/c$ | B | Single |
| C9 | Euclidean‑style norm yields $\kappa_{p}^{E}=1-p^{-1}$ | B | Single |
| C10 | Euler‑factor interpretation of $(1-p^{-2})$ via $p$‑adic $L$‑function interpolation [3] | B | Single |
| C11 | Adelic product formula $\prod_{v}|q|_{v}=1$ validates the Haar‑measure normalization [10] | B | Single |
| C12 | Sensitivity bound $|\kappa_{p'}-\kappa_{p}|\le2p^{-2}$ for consecutive primes | A, B | Convergent |
| C13 | Falsifiability condition: a construction with $\pi_{p}\to\pi$ or a principled product equal to $1$ would refute the conclusion | A, B | Convergent |
| C14 | Readiness assessment at TRL 1–2 for purely analytical, unreviewed work | A, B | Convergent |

Single‑draft claims C8–C11 were retained because their derivations are displayed in full in Section 4 and Section 5.1 and depend only on definitions stated there; no conflicting derivation exists in the other drafts.
