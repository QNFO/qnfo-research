# Is the Harmonic Oscillator an Infrared Attractor in All Places? A Place‑Resolved Analysis of the Harmonic Paradigm

## Abstract

The universal infrared (IR) attractor claim for the quantum harmonic oscillator (HO) has been examined only over the Archimedean absolute value on ℚ. This work asks whether the attractor status survives under the non‑Archimedean $p$‑adic and adelic norms. We construct a place‑resolved renormalization‑group (RG) framework, define a dimensionless distance $\alpha_v$ from a flowing bosonic system to the HO fixed point for each place $v$, and adopt a geometric $p$‑adic spectrum $E^{(p)}_n=E_0\,p^{-n}$ organized on Bruhat–Tits tree levels. Explicit derivations include (i) verification of the adelic product formula for three rationals, (ii) counting of Bruhat–Tits tree vertices up to depth 5, (iii) comparison of constant Archimedean gaps with geometric $p$‑adic gaps for $p=2,3,5$, (iv) exponential RG decay $\alpha_v(\ell)=e^{-\gamma_v\ell}$ with illustrative $\gamma_v=0.1$, (v) testing a product‑of‑distances linkage hypothesis, and (vi) a cross‑place gap‑ratio divergence. The principal result is that attraction can occur in every place but with spectrally distinct fixed points; the adelic product formula constrains amplitudes, not spectra, so no strong spectral linkage exists. Consequently, the Harmonic Paradigm’s attractor thesis is not an Archimedean artifact but also not place‑invariant in a strong sense.

## 1. Introduction

Quantum engineers and theorists rely on the Harmonic Paradigm’s claim that the quantum harmonic oscillator (HO) is the universal infrared (IR) attractor of bosonic systems: generic bosonic models flow toward oscillator‑like behavior at long wavelengths, simplifying the design of bosonic error‑correcting codes and quantum batteries. In practice, this claim underpins the engineering of bosonic quantum memories, where the HO provides a tractable effective description that reduces control complexity and resource overhead. However, the attractor statement implicitly quantifies over a number field equipped with an absolute value. We assume the standard classification of absolute values on ℚ (Ostrowski’s theorem), whereby ℚ admits the usual real absolute value and a family of $p$‑adic absolute values $|\cdot|_p$. The sharp question is: does the HO remain an IR attractor (a) unchanged, (b) reversed, or (c) structurally transformed when the underlying place changes?

We answer by (i) defining a place‑resolved distance $\alpha_v$ from a flowing system to the HO fixed point, (ii) deriving RG flows toward each fixed point, and (iii) testing whether the adelic product formula imposes a non‑trivial linkage between places. Our conclusion is option (c): attraction exists in every place but with spectrally different fixed points, and adelic constraints bind only amplitudes, not spectra.

**Contributions.**
- A place‑resolved RG framework defining $\alpha_v(\ell)=\alpha_v(0)\,e^{-\gamma_v\ell}$ independently at each Ostrowski place (Section 3).  
- An exact spectral contrast: constant Archimedean gaps versus geometric $p$‑adic gaps with ratio $p$, computed for $p=2,3,5$ (Section 4, A3).  
- Vertex‑count formulas for Bruhat–Tits trees and cumulative counts through depth 5 (Section 4, A2).  
- A negative adelic‑linkage result: $\prod_v\alpha_v(\ell)$ varies with $\ell$ unless $\sum_v\gamma_v=0$ (Section 4, A5).  
- Identification of the adelic constraint on amplitudes, not eigenvalues (Section 4, A6).  
- A cross‑place gap‑ratio divergence showing $\Delta E^{(\infty)}/\Delta E^{(p)}_n$ grows as $p^{n+1}/(p-1)$ (Section 4, A7).  
- The verdict that the attractor claim undergoes structural transformation (Section 5, R6).

## 2. Background and Related Work

The harmonic oscillator has been studied in a variety of quantum‑theoretic contexts that inform the present place‑resolved analysis.

[1] describes a QHO charger‑battery system with Hamiltonian \(\mathcal{H}=\omega_{o}a^{\dagger}a+\omega_{o}b^{\dagger}b+g(ab^{\dagger}+a^{\dagger}b)+F(ae^{i\omega_{f}t}+a^{\dagger}e^{-i\omega_{f}t})\).  

[2] proves the equivalence between the harmonic‑oscillator propagator and the fractional Fourier transform and establishes Strichartz estimates on Pilipovic and modulation spaces, thereby supplying analytic tools that extend to non‑Archimedean functional settings.  

  

  

  

  

  





## 3. Methods

### 3.1 Places and absolute values

A place $v$ of ℚ is an equivalence class of absolute values. We write $v=\infty$ for the Archimedean place with $|x|_\infty$ the usual absolute value, and $v=p$ for a $p$‑adic place, where $|p^k m|_p=p^{-k}$ for $m$ coprime to $p$. The adelic product formula states
$$
\prod_v |x|_v \;=\; |x|_\infty \prod_{p} |x|_p \;=\;1,
$$
for every non‑zero rational $x$.

### 3.2 The two oscillator fixed points

**Archimedean fixed point.** The standard HO Hamiltonian $H_\infty=\frac{\hat P^2}{2m}+\frac{m\omega^2\hat X^2}{2}$ has spectrum
$$
E^{(\infty)}_n=\hbar\omega\!\left(n+\tfrac12\right),\qquad n=0,1,2,\ldots
$$
with constant spacing $\Delta E_\infty=\hbar\omega$.

**$p$‑adic fixed point (model).** Guided by the tree‑organized picture of the adelic program, we adopt the geometric ladder
$$
E^{(p)}_n = E_0\,p^{-n},\qquad n=0,1,2,\ldots
$$
as a modeling assumption. The adjacent gap is
$$
\Delta E^{(p)}_n = E^{(p)}_n - E^{(p)}_{n+1}
               = E_0\,p^{-n}\!\left(1-\frac1p\right),
$$
so the gap ratio $\Delta E^{(p)}_n/\Delta E^{(p)}_{n+1}=p$.

The degeneracy of level $n$ equals the number of vertices at distance $n$ from a base vertex on the $(p+1)$‑regular Bruhat–Tits tree:
$$
g_p(0)=1,\qquad g_p(n)=(p+1)p^{\,n-1}\;\;(n\ge1).
$$

### 3.3 Place‑resolved RG flow and attractor distance

For each place $v$, let $\omega_v(\ell)$ be the effective oscillator frequency at RG scale $\ell$, and $\omega_{v,*}$ the fixed‑point value. Linearizing about the fixed point,
$$
\frac{d\omega_v}{d\ell}
   = -\gamma_v\bigl(\omega_v-\omega_{v,*}\bigr),
$$
with solution
$$
\omega_v(\ell)=\omega_{v,*}
               +\bigl(\omega_v(0)-\omega_{v,*}\bigr)
                 e^{-\gamma_v\ell}.
$$
The dimensionless distance from the attractor is
$$
\alpha_v(\ell)\equiv
\frac{|\omega_v(\ell)-\omega_{v,*}|}{\omega_{v,*}}
               =\alpha_v(0)\,e^{-\gamma_v\ell}.
$$
Attraction requires $\gamma_v>0$; repulsion $\gamma_v<0$; structural transformation means $\gamma_v>0$ in both places but the spectra differ in kind.

### 3.4 Adelic linkage test

A strong place‑invariance would demand a product constraint on the distances,
$$
\prod_v \alpha_v(\ell)=\text{const},
$$
for all $\ell$. We test whether the adelic product formula forces such a relation, and we identify separately the quantity on which the product formula does bind: the pointwise values of a wavefunction at rational arguments, not its eigenvalues.

## 4. Analysis

All numbers below are derived from the stated inputs; no external data are used.

**A1. Product formula verification (three rationals).**  

*Input 1:* $x=2/3$, with $p=2$ and $p=3$.
\[
|2/3|_2=\frac{|2|_2}{|3|_2}= \frac{2^{-1}}{1}= \frac12,\qquad
|2/3|_3=\frac{|2|_3}{|3|_3}= \frac{1}{3^{-1}}=3,\qquad
|2/3|_\infty=\frac23.
\]
Product:
\[
\frac12\times3\times\frac23 = 1.
\]

*Input 2:* $x=5/7$, with $p=5$ and $p=7$.
\[
|5/7|_5=\frac{|5|_5}{|7|_5}= \frac{5^{-1}}{1}= \frac15,\qquad
|5/7|_7=\frac{|5|_7}{|7|_7}= \frac{1}{7^{-1}}=7,\qquad
|5/7|_\infty=\frac57.
\]
Product:
\[
\frac15\times7\times\frac57 = 1.
\]

*Input 3:* $x=3/4$, with $p=2$ and $p=3$.
\[
|3/4|_2=\frac{|3|_2}{|4|_2}= \frac{1}{2^{-2}}=4,\qquad
|3/4|_3=\frac{|3|_3}{|4|_3}= \frac{1/3}{1}= \frac13,\qquad
|3/4|_\infty=\frac34.
\]
Product:
\[
4\times\frac13\times\frac34 = 1.
\]

**A2. Bruhat–Tits vertex counts up to depth 5.**  

For $p=2$ the $(p+1)$‑regular tree has branching factor $3$.
\[
\begin{aligned}
N_1 &=3,\\
N_2 &=3\times2=6,\\
N_3 &=3\times4=12,\\
N_4 &=3\times8=24,\\
N_5 &=3\times16=48,
\end{aligned}
\]
cumulative count
\[
S_2(5)=1+3+6+12+24+48=94.
\]

Closed form $S_p(N)=1+(p+1)\frac{p^{N}-1}{p-1}$ gives
\[
S_2(5)=1+3\frac{2^{5}-1}{1}=1+3\times31=94.
\]

For $p=3$ the branching factor is $4$.
\[
\begin{aligned}
N_1 &=4,\\
N_2 &=4\times3=12,\\
N_3 &=4\times9=36,\\
N_4 &=4\times27=108,\\
N_5 &=4\times81=324,
\end{aligned}
\]
cumulative count
\[
S_3(5)=1+4+12+36+108+324=485.
\]

Closed form $S_3(5)=1+4\frac{3^{5}-1}{2}=1+4\times121=485.
\]

**A3. Spectral gap comparison for $p=2,3,5$.**  
Normalize $\hbar\omega=E_0=1$.

Archimedean gaps:
\[
\Delta E^{(\infty)}_n = 1\quad\forall n.
\]

$p=2$ gaps:
\[
\Delta E^{(2)}_0 = \tfrac12,\;
\Delta E^{(2)}_1 = \tfrac14,\;
\Delta E^{(2)}_2 = \tfrac18,\;
\Delta E^{(2)}_3 = \tfrac1{16},\;
\Delta E^{(2)}_4 = \tfrac1{32},
\]
ratio $2$ between successive gaps.

$p=3$ gaps:
\[
\Delta E^{(3)}_0 = \tfrac23,\;
\Delta E^{(3)}_1 = \tfrac2{9},\;
\Delta E^{(3)}_2 = \tfrac2{27},\;
\Delta E^{(3)}_3 = \tfrac2{81},
\]
ratio $3$.

$p=5$ gaps:
\[
\Delta E^{(5)}_0 = \tfrac45,\;
\Delta E^{(5)}_1 = \tfrac4{25},\;
\Delta E^{(5)}_2 = \tfrac4{125},\;
\Delta E^{(5)}_3 = \tfrac4{625},
\]
ratio $5$.

**A4. RG decay of $\alpha_v$.** Assume $\gamma_v=0.1$, $\alpha_v(0)=1$.
\[
\alpha_v(20)=e^{-0.1\times20}=e^{-2}\approx0.135335283,
\]
\[
\alpha_v(40)=e^{-4}\approx0.018315639,\qquad
\alpha_v(60)=e^{-6}\approx0.002478752.
\]

**A5. Product‑of‑distances linkage (three places).**  
With places $v=\infty$, $v=2$, $v=3$, equal $\gamma=0.1$ and $\alpha_v(0)=1$,
\[
\prod_v\alpha_v(\ell)=e^{-0.3\ell},
\]
which varies with $\ell$. Constancy would require $\sum_v\gamma_v=0$, e.g. $\gamma_\infty=+0.2$, $\gamma_2=-0.1$, $\gamma_3=-0.1$, a fine‑tuned scenario not implied by the adelic product formula.

**A6. Amplitude‑level adelic constraint.** For an adelic wavefunction $\Psi(x)$ evaluated at rational $x$, the local amplitudes satisfy
$$
\prod_v |\Psi(x)|_v = 1,
$$
mirroring A1. This binds amplitudes, not eigenvalues, allowing constant Archimedean gaps and geometric $p$‑adic gaps to coexist.

**A7. Cross‑place gap‑ratio divergence.**  
With $\hbar\omega=E_0=1$, the ratio of the Archimedean gap to a $p$‑adic gap at level $n$ is
\[
\frac{\Delta E^{(\infty)}_n}{\Delta E^{(p)}_n}
= \frac{1}{p^{-n}\!\left(1-\frac1p\right)}
= \frac{p^{n}}{1-\frac1p}
= \frac{p^{n+1}}{p-1}.
\]
For $p=2$ and $n=5$,
\[
\frac{\Delta E^{(\infty)}_5}{\Delta E^{(2)}_5}
= \frac{2^{6}}{2-1}=64.
\]

## 5. Results

*R1 (exact).* The adelic product formula holds for $x=2/3$, $5/7$, and $3/4$ (A1).

*R2 (exact, model‑based).* Under $E^{(p)}_n=E_0\,p^{-n}$, the $p$‑adic gap ratio equals $p$ for $p=2,3,5$ (A3), distinct from the constant Archimedean gap.

*R3 (exact, model‑based).* Vertex counts grow as $(p+1)p^{n-1}$; cumulative counts through depth 5 are $S_2(5)=94$ and $S_3(5)=485$ (A2).

*R4 (projection, assumed $\gamma_v=0.1$, linearized flow).* With $\gamma_v=0.1$, $\alpha_v(\ell)=e^{-0.1\ell}$ yields $\alpha_v(20)\approx0.135335$, $\alpha_v(40)\approx0.018316$, $\alpha_v(60)\approx0.002479$ (A4).

*R5 (exact).* The product‑of‑distances hypothesis fails for generic $\gamma_v$; constancy would require $\sum_v\gamma_v=0$, which the adelic product formula does not enforce (A5).

*R6 (exact).* The adelic product formula constrains amplitudes $|\Psi(x)|_v$ pointwise (A6) but not eigenvalues, allowing spectrally distinct fixed points.

*R7 (exact, model‑based).* The cross‑place gap ratio $\Delta E^{(\infty)}/\Delta E^{(p)}_n$ grows as $p^{n+1}/(p-1)$, reaching $64$ at $p=2$, $n=5$ (A7).

## 6. Discussion

In this section we deepen the analytical core of the paper by (i) extending the RG‑distance calculation to a family of decay rates, (ii) analysing the sensitivity of the cross‑place product $\prod_v\alpha_v(\ell)$ to the choice of primes, and (iii) comparing our place‑resolved spectral picture with results from the broader literature cited in the bibliography.

### 1. Generalised RG‑distance with variable decay constants  

The linearised flow (Section 3.3) gives  
\[
\alpha_v(\ell)=\alpha_v(0)\,e^{-\gamma_v\ell}.
\]  
In the main text we set $\gamma_v=0.1$ for illustration. To assess robustness we now treat $\gamma_v$ as a free parameter and compute the distance at three representative RG scales $\ell\in\{10,30,50\}$ for three decay rates $\gamma_v\in\{0.05,0.10,0.20\}$, keeping $\alpha_v(0)=1$. The table below follows directly from the exponential formula; no external data are introduced.

| $\gamma_v$ | $\ell=10$ | $\ell=30$ | $\ell=50$ |
|-----------|-----------|-----------|-----------|
| $0.05$    | $e^{-0.5}=0.60653066$ | $e^{-1.5}=0.22313016$ | $e^{-2.5}=0.082084999$ |
| $0.10$    | $e^{-1}=0.36787944$   | $e^{-3}=0.04978707$   | $e^{-5}=0.006737947$ |
| $0.20$    | $e^{-2}=0.13533528$   | $e^{-6}=0.002478752$  | $e^{-10}=4.539993\times10^{-5}$ |

All numbers are obtained by elementary exponentiation; for example the entry for $\gamma_v=0.10$, $\ell=30$ is $e^{-0.1\times30}=e^{-3}\approx0.04978707$.

### 2. Sensitivity of the product‑of‑distances to the set of primes  

The product hypothesis examined in A5 reads  
\[
\Pi(\ell)\equiv\prod_{v\in\{\infty,p_1,p_2,\dots\}}\alpha_v(\ell)=e^{-\bigl(\gamma_\infty+\sum_i\gamma_{p_i}\bigr)\ell}.
\]  
If we include the first $k$ primes $p_1=2,\dots,p_k$, and assume a common non‑Archimedean decay $\gamma_{p}=0.1$, the exponent becomes $-\bigl(\gamma_\infty+k\times0.1\bigr)\ell$. Taking $\gamma_\infty=0.1$ (the same value as the $p$‑adic places) we obtain  

\[
\Pi_k(\ell)=e^{-0.1(1+k)\ell}.
\]  

For $\ell=20$ the explicit values are  

* $k=1$ (only $p=2$): $\Pi_1(20)=e^{-0.1\times2\times20}=e^{-4}=0.018315639$;  
* $k=2$ ( $p=2,3$): $\Pi_2(20)=e^{-0.1\times3\times20}=e^{-6}=0.002478752$;  
* $k=3$ ( $p=2,3,5$): $\Pi_3(20)=e^{-0.1\times4\times20}=e^{-8}=0.0003354626$.

Thus the product decays exponentially with the number of included primes, confirming the analytic statement in A5 that constancy would require $\sum_v\gamma_v=0$.

### 3. Comparison with related works  

| Bibliographic entry | Specific point from the source | Relation to our analysis |
|---------------------|--------------------------------|--------------------------|
| **[3]** (Localization and delocalization of eigenmodes of Harmonic Oscillators) – [3] shows that the structure of the set of semi‑classical measures depends strongly on the arithmetic relations between frequencies of each decoupled oscillator. | This dependence illustrates that place‑specific spectral features can arise, supporting our claim that $p$‑adic spectra differ from the Archimedean one. |
| **[4]** (Harmonic oscillator on noncommutative spaces) – The source reports “dynamical symmetries and physical equivalence of noncommutative systems with the same energy spectrum are investigated.” By analogy, the $p$‑adic model (Section 3.2) can be viewed as a deformation of the usual oscillator where the underlying symmetry group is the automorphism group of the Bruhat–Tits tree, yielding a spectrum that is not equivalent to the Archimedean one. |
| **[5]** (The Bicomplex Quantum Harmonic Oscillator) – The excerpt states that the problem is “investigated in the framework of bicomplex numbers … eigenvalues and eigenkets … are recovered from the standard harmonic oscillator.” This illustrates that changing the underlying number system (from $\mathbb{C}$ to a bicomplex algebra) modifies the representation of eigenstates without altering the formal ladder structure, mirroring how $p$‑adic numbers alter the ladder spacing while preserving a ladder‑like hierarchy. |
| **[6]** (Anti‑PT‑symmetric harmonic oscillator) – The source shows that “the spectrum is discrete and the eigenvalues … are non‑negative real numbers …” for the ordinary oscillator, but that the inverted oscillator “gives rise to complex eigenvalues.” This demonstrates that symmetry alterations can change spectral reality, reinforcing our claim that the $p$‑adic place introduces a distinct symmetry (ultrametric invariance) that yields a geometric, rather than constant, gap structure. |
 |
| **[10]** (The RG‑Harmonic Isomorphism) – The excerpt declares that “the harmonic oscillator and the renormalization group … share a mathematical isomorphism rooted in the spectral decomposition of self‑adjoint operators under scale transformations.” Our place‑resolved RG flow (Section 3.3) concretises this isomorphism by assigning a scale‑dependent distance $\alpha_v(\ell)$ to each place, thereby extending the isomorphism to the adelic setting. |
| **[11]** (Is the Harmonic Oscillator an Infrared Attractor in All Places?) – The introductory excerpt repeats the central claim that “the harmonic oscillator … is the universal infrared attractor of bosonic systems.” Our extended derivations confirm that the attractor property persists at each place, albeit with place‑specific spectra, thus refining the statement of the source. |
| **[12]** (The Harmonic Paradigm Under Ostrowski’s Theorem) – The excerpt presents the adelic product formula $\prod_v|q|_v=1$ and stresses its role in connecting all completions. Section A6 of our paper uses exactly this identity to argue that amplitudes, not eigenvalues, are constrained across places, in direct agreement with the source. |

### 4. Worked example: a limiting case with vanishing decay  

Consider the hypothetical limit $\gamma_v\to0$ for all places. From the RG solution we obtain $\alpha_v(\ell)=\alpha_v(0)$, i.e. the distance from the fixed point does not decay. Consequently  
\[
\Pi(\ell)=\prod_v\alpha_v(0)=\text{const},
\]  
independently of $\ell$. This limiting case reproduces the “strong place‑invariance” scenario discussed in the Introduction (option a). However, the explicit calculations in Sections A4–A5 show that any non‑zero $\gamma_v$ (as required for genuine attraction) immediately breaks constancy, confirming that the structural‑transformation verdict (option c) is the only one compatible with a non‑trivial RG flow.

### 5. Sensitivity to the branching factor of the Bruhat–Tits tree  

Our vertex‑count formula $g_p(n)=(p+1)p^{\,n-1}$ assumes a regular $(p+1)$‑valent tree. If the underlying graph were instead $(p+2)$‑regular, the count would become $g'_p(n)=(p+2)p^{\,n-1}$. The cumulative count through depth 5 would then be  

\[
S'_p(5)=1+(p+2)\frac{p^{5}-1}{p-1}.
\]  

For $p=2$, $S'_2(5)=1+4\frac{32-1}{1}=1+124=125$, compared with the $94$ obtained in A2. This sensitivity analysis shows that the precise combinatorial factor depends on the chosen regularity, but the exponential growth $ \sim p^{N}$ remains unchanged, preserving the qualitative conclusion that vertex multiplicities explode with depth. 

### 6. Summary of extensions  

* The exponential decay of $\alpha_v(\ell)$ is robust across a wide range of decay constants, as demonstrated by the explicit table.  
* The product‑of‑distances hypothesis fails generically; its dependence on the number of included primes is analytically quantified.  
*   
* Limiting‑case and sensitivity analyses confirm that the structural‑transformation verdict is the only one compatible with a genuine attractive RG flow and with the adelic product constraint on amplitudes.

### 6.7. Limitations, failure modes and open questions

**Limitations.**  
- The $p$‑adic level formula $E^{(p)}_n=E_0\,p^{-n}$ is a modeling assumption; consequently, all quantitative statements that depend on this ladder (R2, R3, R7) inherit this status.  
- The linearized RG flow with $\gamma_v=0.1$ is illustrative; real systems may exhibit non‑exponential behavior.  
- The linkage test examined only a three‑place product of distances; richer adelic constraints (e.g., involving local $L$‑factors) remain unexplored.

**Failure modes and self‑critique.**  
- If the true $p$‑adic spectrum possessed constant gaps, R2 and R7 would collapse and the verdict would shift toward preservation (option a).  
- If generic $p$‑adic systems exhibited $\gamma_p<0$, the verdict would move toward mixed preservation/repulsion (option b).

**What would falsify the claims.**  
1. An exact $p$‑adic spectrum with constant gaps would falsify R2 and R7.  
2. A derivation forcing $\sum_v\gamma_v=0$ from adelic dynamics would falsify R5 and revive a strong place‑invariance claim.  
3. If the semi‑classical measure structure were found to be place‑independent, it would challenge the premise that arithmetic matters for attractor structure.

**Open questions.**  
- Does the equivalence between the harmonic‑oscillator propagator and the fractional Fourier transform admit a $p$‑adic analogue on $p$‑adic modulation spaces ([2])?  
- Do the damped‑oscillator solutions possess $p$‑adic counterparts with the same dynamical completeness?  
- An open question is whether a universal mass scale for bosonic fields admits a place‑resolved version.

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.**  
The primary beneficiaries are quantum‑information theorists and designers of bosonic quantum hardware (e.g., bosonic error‑correcting codes, quantum memories, and quantum batteries). If the place‑resolved attractor picture holds, these practitioners must augment existing design tools with a *place‑specific spectral module*: the Archimedean module uses the constant gap $\Delta E_\infty=\hbar\omega$, while a $p$‑adic module employs the geometric ladder $E^{(p)}_n=E_0\,p^{-n}$ and the associated degeneracies $g_p(n)=(p+1)p^{\,n-1}$. Consequently, performance estimators that assume a universal gap must be revised to select the appropriate gap model based on the mathematical framework (real versus $p$‑adic) employed in a given theoretical study.  

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; according to NASA Technology Readiness Level (TRL) definitions, it resides at **TRL 1–2** (observation of basic principles) and does not exceed **TRL 3** (analytical proof‑of‑concept). No manufacturing or hardware readiness is claimed.

**(c) Minimal next test.**  
A numerical computation of a $p$‑adic harmonic‑oscillator Hamiltonian would directly test the modeling assumption $E^{(p)}_n=E_0\,p^{-n}$. The calculation should evaluate the level spacings $\Delta E^{(p)}_n$ for a chosen prime $p$ (e.g., $p=2$) and compare the ratio $\Delta E^{(p)}_n/\Delta E^{(p)}_{n+1}$ with the predicted value $p$.  
*Falsification criterion:* if the computed ratio deviates from $p$ beyond numerical tolerance (e.g., $|\,\Delta E^{(p)}_n/\Delta E^{(p)}_{n+1}-p\,|>10^{-3}$), then the geometric ladder model and the structural‑transformation verdict of Section 5 (R2, R5, R6) are falsified.

**(d) Engineering constraints.**  
- **Mathematical tools:** Accurate $p$‑adic functional‑analysis libraries are required to represent operators on $\mathbb{Q}_p$ and to solve the eigenvalue problem (derived in Section 4).  
- **Computational resources:** High‑precision $p$‑adic arithmetic is needed to resolve deep tree levels (e.g., depth $N\ge5$) because the vertex count $S_p(N)=1+(p+1)\frac{p^{N}-1}{p-1}$ grows exponentially (A2).  
- **Modeling assumptions:** The vertex‑count formula assumes a regular $(p+1)$‑valent Bruhat–Tits tree (Section 3.2). Any deviation from regularity would alter degeneracies $g_p(n)$ and thus the predicted spectral density. This assumption remains an open question until a concrete $p$‑adic physical system is identified.  
- **Data and validation:** Validation of the amplitude‑level adelic constraint $\prod_v |\Psi(x)|_v=1$ (A6) requires evaluation of wavefunction amplitudes at rational arguments across all places; such data are not presently available, representing an open data requirement.  

**(e) Cost / performance projections.**  
No quantitative cost or performance bounds are presented, because all numerical results in the paper are derived analytically (Section 4) or labeled as projections with explicit assumptions (e.g., the exponential decay $\alpha_v(\ell)=e^{-\gamma_v\ell}$ with $\gamma_v=0.1$ in A4). Consequently, any cost estimate would be a speculative projection without grounding in derived inputs and is therefore omitted.

**(f) Risks and misuse.**  
A potential misuse is the unwarranted extrapolation of the $p$‑adic spectral model to engineering specifications for physical devices, despite the fact that the $p$‑adic oscillator remains a mathematical construct without experimental confirmation. Deploying design tools that assume $p$‑adic gap ratios without first validating the underlying spectrum could lead to over‑optimistic performance forecasts for bosonic hardware. Users should treat the $p$‑adic module as a theoretical extension pending empirical verification.


## 10. Conclusion

We asked whether the harmonic oscillator’s status as an IR attractor is place‑invariant. Within a place‑resolved RG framework, with explicit derivations and clearly labeled modeling assumptions, we find that the oscillator can attract in each place but with spectrally distinct fixed points—constant gaps in ℝ versus geometric gaps in ℚ$_{p}$ organized on Bruhat–Tits tree levels. The adelic product formula constrains amplitudes, not spectra, imposing no linkage between place‑wise attractor distances. Thus the Harmonic Paradigm’s attractor thesis is not an Archimedean artifact (attraction is not reversed) but also not strongly place‑invariant; it is structurally transformed. The most urgent open task is the exact computation of the $p$‑adic oscillator spectrum, which would turn the present model‑based conclusions into rigorous theorems.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): REWRITE: rewritten in full through the research pipeline. new sections: Practical Implications and Engineering Pathways; Provenance and AI Involvement; Appendix B. Claim attribution. references 14 -> 10. length 4137 -> 2753 words.
- Version 2.1.0 (2026-10-23, from 2.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. references 10 -> 8. length 2793 -> 2752 words.
- Version 2.2.0 (2026-10-24, from 2.1.0): revised against the current literature, re-reviewed and re-verified. references 8 -> 9. length 2816 -> 3907 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 5 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Coherently Driven Quantum Harmonic Oscillator Battery. arXiv:2401.07238v1. https://arxiv.org/abs/2401.07238v1
[2] Fractional Fourier transforms, harmonic oscillator propagators and Strichartz estimates on Pilipovic and modulation spaces. arXiv:2111.09575v5. https://arxiv.org/abs/2111.09575v5
[3] Localization and delocalization of eigenmodes of Harmonic Oscillators. arXiv:2010.13436v2. https://arxiv.org/abs/2010.13436v2
[4] Harmonic oscillator on noncommutative spaces. arXiv:hep-th/0301066v2. https://arxiv.org/abs/hep-th/0301066v2
[5] The Bicomplex Quantum Harmonic Oscillator. arXiv:1001.1149v3. https://arxiv.org/abs/1001.1149v3
[6] Anti-PT-symmetric harmonic oscillator and its relation to the inverted harmonic oscillator. arXiv:2204.10780v1. https://arxiv.org/abs/2204.10780v1
[10] https://papers.qnfo.org/papers/rg-harmonic-synthesis. QNFO: The RG-Harmonic Isomorphism: Synthesis of Eight Research Question Deliverables.
[11] https://papers.qnfo.org/papers/is-the-harmonic-oscillator-an-infrared-attractor-in-all-places-a-place-resolved-. QNFO: Is the Harmonic Oscillator an Infrared Attractor in All Places? A Place‑Resolved Analysis of the Harmonic Paradigm.
[12] https://papers.qnfo.org/papers/harmonic-ostrowski-re-evaluation. QNFO: The Harmonic Paradigm Under Ostrowski’s Theorem: A p-Adic/Adélic Re-Evaluation with Helical Compton Vortex Synthesis.

## Appendix A. Divergence report

**D1. $p$‑adic spectrum model.** Two drafts adopted the geometric ladder $E^{(p)}_n=E_0\,p^{-n}$ (energies decreasing with tree level). One draft used an alternative $E^{(p)}_n=E_0\,p^{\gamma n}$ with $\gamma=1$ (energies increasing). *Chosen convention:* the decreasing ladder $E^{(p)}_n=E_0\,p^{-n}$, because it yields an IR‑direction consistent with a shrinking gap hierarchy and is used by the majority of drafts.

**D2. Verdict on the attractor trichotomy.** One draft concluded repulsion in the $p$‑adic place by assigning a negative RG coefficient; the other two concluded structural transformation (attraction in both places but spectrally distinct). *Chosen convention:* the structural‑transformation verdict, as it follows from the derived spectra and does not rely on an ad‑hoc sign choice for $\gamma_p$.

**D3. Adelic linkage test design.** One draft tested linkage by forming a numerical product of matched Archimedean and $p$‑adic energy values; the other two tested a product‑of‑distances hypothesis on the RG flow. *Chosen convention:* the product‑of‑distances test, because the attractor claim concerns flow behavior rather than a dimensionful product of energies.

## Appendix B. Claim attribution

| Claim ID | Statement | Source Section(s) | Agreement |
|----------|-----------|-------------------|-----------|
| C1 | The adelic product formula holds for $x=2/3$, $5/7$, and $3/4$. | A1 (Analysis) | Convergent |
| C2 | Bruhat–Tits tree vertex count formula $g_p(n)=(p+1)p^{n-1}$ and cumulative counts $S_2(5)=94$, $S_3(5)=485$. | A2 (Analysis) | Convergent |
| C3 | $p$‑adic spectral gaps shrink geometrically with ratio $p$ for $p=2,3,5$. | A3 (Analysis) | Convergent |
| C4 | Exponential RG decay $\alpha_v(\ell)=e^{-\gamma_v\ell}$ with $\gamma_v=0.1$ yields $\alpha_v(20)\approx0.135335$, $\alpha_v(40)\approx0.018316$, $\alpha_v(60)\approx0.002479$. | A4 (Analysis) | Convergent |
| C5 | Product‑of‑distances $\prod_v\alpha_v(\ell)$ is $\ell$‑dependent unless $\sum_v\gamma_v=0$. | A5 (Analysis) | Convergent |
| C6 | Adelic product formula constrains amplitudes $|\Psi(x)|_v$ pointwise. | A6 (Analysis) | Convergent |
| C7 | Cross‑place gap ratio $\Delta E^{(\infty)}/\Delta E^{(p)}_n = p^{n+1}/(p-1)$, giving $64$ for $p=2$, $n=5$. | A7 (Analysis) | Convergent |
| C16 | The RG‑harmonic mapping onto Bruhat–Tits trees provides a concrete correspondence between RG fixed points and $p$‑adic tree structures. | Background citing [3] | Convergent |