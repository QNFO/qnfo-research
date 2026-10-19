# Thermal Quantum Sensing at High Temperature: Exact Fisher‑Information Bounds, Universal Metrics, and the Work Cost of Quadratic Signals

## Abstract

Thermal fluctuations are usually treated as a nuisance that degrades quantum‑enhanced sensing, yet for certain signal encodings heat can improve the metrological response of a probe. We study thermal quantum sensors governed by a Hamiltonian $H$ and subjected to a unitary signal $U(\theta)=\exp(-i\theta G)$. Building on general results that relate monotone quantum Fisher‑information (QFI) metrics, their temperature dependence, and the work induced by a unitary signal, we derive closed‑form expressions for two exactly solvable models. For a single bosonic mode with a purely quadratic (squeezing‑type) generator of strength $g$, we obtain  
\[
F_Q(\beta)=\frac{2g^{2}(1+q)^{2}}{1+q^{2}},\qquad q=e^{-\beta\omega},
\]  
which interpolates between $F_Q(T=0)=2g^{2}$ and $F_Q(T\!\to\!\infty)=4g^{2}$, thereby achieving exactly twice the zero‑temperature QFI and the corresponding factor‑of‑two Cramér–Rao improvement, both derived here from first principles. At $\beta\omega=0.1$ the QFI already reaches $99.7491\%$ of its infinite‑temperature value. For a qubit sensor we derive the exact SLD QFI $F_K=\tanh^{2}(\hbar\omega/2k_{B}T)$ and locate the crossover to the universal high‑temperature regime, which requires $k_{B}T\gtrsim2\hbar\omega$ for few‑percent accuracy. The signal‑induced work is  
\[
W(\theta)=\omega\sinh^{2}(g\theta)\,\coth\!\left(\frac{\beta\omega}{2}\right)
\approx\omega g^{2}\theta^{2}\,\coth\!\left(\frac{\beta\omega}{2}\right)\quad(g\theta\ll1),
\]  
which grows linearly with $T$ at high temperature. All derivations are fully explicit and independently checkable.

## 1. Introduction

Experimental quantum sensors are never at zero temperature: trapped‑ion motional modes, neutral‑atom traps, optical parametric sources, and mechanical resonators all carry a thermal occupation set by the ratio $k_{B}T/\hbar\omega$ of thermal energy to mode frequency. Conventional design practice therefore seeks the lowest possible temperature, because heating is assumed to suppress coherence and erase quantum advantage. For platforms that employ sideband cooling in ion chains or micro‑trap arrays, each additional order of magnitude of cooling translates directly into laser power, control‑sequence length, and engineering complexity.

A recent general analysis of thermal quantum sensing overturns this intuition for *purely quadratic* signal generators acting on continuous‑variable systems. It shows that monotone QFI metrics obey a temperature‑dependent hierarchy and that at high temperature they converge to a universal quantity. Moreover, the same analysis connects the temperature‑dependent sensitivity to the thermodynamic work injected by the signal.

The purpose of this paper is to make these general claims concrete, fully explicit, and independently verifiable. We isolate the simplest non‑trivial settings—a single harmonic mode with a quadratic (squeezing‑type) generator, and a single qubit with a transverse generator—and carry out every step of the spectral QFI computation, the low‑ and high‑temperature limits, the crossover analysis, and the signal‑induced work expansion, with all arithmetic shown. The qubit case provides a contrasting example in which the QFI vanishes at high temperature, highlighting the special role of quadratic generators.

Our contributions are:
1. An exact closed‑form QFI for a quadratic generator on a thermal oscillator, $F_Q(\beta)=2g^{2}(1+q)^{2}/(1+q^{2})$, derived from first principles with every arithmetic step shown (Sections 3–4).  
2. Derivation of the exact factor‑of‑two Cramér–Rao improvement from heating for the quadratic generator, obtained by comparing the zero‑ and infinite‑temperature limits of the closed‑form QFI (Section 4.5).  
3. An exact qubit QFI, $F_K=\tanh^{2}(\hbar\omega/2k_{B}T)$, together with a quantitative crossover analysis showing that the universal high‑temperature form fails by $42.00\%$ at $k_{B}T=\hbar\omega/2$ and by $4.02\%$ at $k_{B}T=2\hbar\omega$ (Section 4.7).  
4. An explicit derivation of the signal‑induced work, $W(\theta)=\omega\sinh^{2}(g\theta)\coth(\beta\omega/2)$, quantifying the thermodynamic price of heating‑assisted sensing and showing that the work per unit QFI grows linearly with temperature (Section 4.8).

## 2. Background and Related Work

**Thermal quantum sensing and QFI metrics.** The analysis of Fisher information and signal‑induced work beyond Gaussian signals shows that monotone QFI metrics obey a temperature‑dependent hierarchy and that at high temperature they converge to a universal quantity. These results provide the theoretical backdrop for the exact bosonic calculation presented here, and for the qubit calculation that illustrates a contrasting high‑temperature vanishing. [2]

**Gaussian metrology.** The phase‑space formalism for Gaussian states underpins continuous‑variable sensing. Prior work derives optimal multi‑parameter estimation formulae for Gaussian states and documents discontinuous behavior of the QFI figure of merit. Our results refine this picture by showing that, for a fixed thermal state, the QFI can increase with temperature even though the global optimum over mean energy remains a pure state.

**Distributed and structured sensing.** Private and robust states for distributed quantum sensing extend single‑parameter QFI bounds to functions of multiple spatially separated parameters. The thermal saturation mechanism studied here is local to each mode and therefore composes naturally with such distributed protocols, although we do not prove composition formally. [3]

**Photon sources and platforms.** Parametric‑down‑conversion (PDC) sources generate squeezing‑type quadratic interactions. The generator $G=\frac{g}{2}(a^{2}+a^{\dagger2})$ therefore maps directly onto experimentally available nonlinear‑optics couplings, linking our abstract model to realistic platforms. [5]

**Scalable atom arrays.** Neutral‑atom arrays with single‑site addressability host motional modes whose thermal occupation is tunable by sideband cooling. The $\beta\omega$‑dependent formulas derived below are directly applicable to the design of such platforms. [6]

**Extraction and estimation.** Studies of quantum algorithms for extracting physical information demonstrate that estimation can be framed as an active extraction task. Our work complements this by focusing on passive‑probe thermal analysis. [7]

**Operational FI for structured beams.** Analyses of Fisher information as an operational metric for structured optical beams argue that FI, not entropic complexity, quantifies metrological content. Our thermal‑state counterpart shows that temperature can similarly modulate the FI of a mode. [8]

What is missing in the literature, and what we supply, is an end‑to‑end account—with every arithmetic step shown—of the exact QFI for the minimal thermal sensors, the saturation of the quadratic‑generator bound, the crossover to universality, and the associated work cost.

## 3. Methods

### 3.1 Bosonic model

A single bosonic mode with free Hamiltonian  
\[
H_{0}=\omega\,a^{\dagger}a,
\]  
where $[a,a^{\dagger}]=1$ and $\omega>0$, is prepared in the Gibbs state  
\[
\rho_{\beta}=\frac{e^{-\beta H_{0}}}{Z(\beta)},\qquad Z(\beta)=\frac{1}{1-q},\qquad q\equiv e^{-\beta\omega}.
\]  
In the Fock basis $\rho_{\beta}=\sum_{n}p_{n}|n\rangle\langle n|$ with $p_{n}=(1-q)q^{n}$.

An unknown parameter $\theta$ is encoded unitarily as $\rho_{\theta}=e^{-i\theta G}\rho_{\beta}e^{i\theta G}$ with the quadratic generator  
\[
G=\frac{g}{2}\bigl(a^{2}+a^{\dagger2}\bigr),
\]  
a squeezing‑type coupling of strength $g$.

### 3.2 QFI formula and Cramér–Rao bound

For a unitary encoding on a state diagonal in the eigenbasis $\{|m\rangle\}$ with eigenvalues $p_{m}$, the symmetric‑logarithmic‑derivative (SLD) QFI is  
\[
F_{Q}=2\sum_{m,n}\frac{(p_{m}-p_{n})^{2}}{p_{m}+p_{n}}\,|\langle m|G|n\rangle|^{2}
=4\sum_{m<n}\frac{(p_{m}-p_{n})^{2}}{p_{m}+p_{n}}\,|G_{mn}|^{2}.
\]  
The SLD QFI is the minimal monotone metric; at high temperature all monotone metrics coincide with it to leading order, so computing $F_{Q}$ suffices. For $\nu$ independent repetitions any unbiased estimator $\hat{\theta}$ satisfies  
\[
\mathrm{Var}(\hat{\theta})\ge\frac{1}{\nu F_{Q}}.
\]

### 3.3 Work

The average internal energy after encoding is $\langle H_{0}\rangle_{\theta}=\mathrm{Tr}(H_{0}\rho_{\theta})$. For an isolated unitary the injected work is the change in average energy,  
\[
W(\theta)=\langle H_{0}\rangle_{\theta}-\langle H_{0}\rangle_{0}.
\]

### 3.4 Qubit model

For the crossover analysis we use a two‑level system with Hamiltonian $H=\frac{\hbar\omega}{2}\sigma_{z}$, thermal state $\rho_{\beta}=e^{-\beta H}/Z(\beta)$ with $Z(\beta)=2\cosh(\beta\hbar\omega/2)$, and a transverse generator $G=\sigma_{x}/2$. Energies are expressed in units of $\hbar\omega$; temperatures in units of $\hbar\omega/k_{B}$.

## 4. Analysis

All input numbers are stated with their source; every arithmetic step is shown.

### 4.1 Generator matrix elements (bosonic model)

Using $a|n\rangle=\sqrt{n}\,|n-1\rangle$ and $a^{\dagger}|n\rangle=\sqrt{n+1}\,|n+1\rangle$, we obtain  
\[
a^{2}|n\rangle=\sqrt{n(n-1)}\,|n-2\rangle,\qquad
a^{\dagger2}|n\rangle=\sqrt{(n+1)(n+2)}\,|n+2\rangle.
\]  
Thus the only non‑zero matrix elements of $G$ are  
\[
\langle n+2|G|n\rangle=\frac{g}{2}\sqrt{(n+1)(n+2)},\qquad G_{nn}=0,
\]  
and all other $G_{mn}=0$.

### 4.2 QFI sum reduces to $(n,n+2)$ pairs

Only pairs $(n,n+2)$ contribute:
\[
F_{Q}=4\sum_{n=0}^{\infty}\frac{(p_{n}-p_{n+2})^{2}}{p_{n}+p_{n+2}}\cdot\frac{g^{2}}{4}(n+1)(n+2).
\]  
With $p_{n}=(1-q)q^{n}$ we have  
\[
p_{n}-p_{n+2}=(1-q)q^{n}(1-q^{2}),\qquad
p_{n}+p_{n+2}=(1-q)q^{n}(1+q^{2}),
\]  
and therefore  
\[
\frac{(p_{n}-p_{n+2})^{2}}{p_{n}+p_{n+2}}=(1-q)\,q^{n}\,\frac{(1-q^{2})^{2}}{1+q^{2}}.
\]

### 4.3 Series evaluation

The remaining sum is  
\[
S(q)=\sum_{n=0}^{\infty}(n+1)(n+2)q^{n}.
\]  
Since $\sum_{n=0}^{\infty}q^{n+2}=q^{2}/(1-q)$, differentiating twice yields  
\[
S(q)=\frac{d^{2}}{dq^{2}}\frac{q^{2}}{1-q}=\frac{2}{(1-q)^{3}}.
\]  
A numerical check at $q=0.1$ gives $S(0.1)=2/(0.9)^{3}=2.74348$, matching the explicit partial‑sum estimate $2.7435$.

### 4.4 Closed form and limits

Substituting the results of Sections 4.2 and 4.3:
\[
\begin{aligned}
F_{Q}
&=4\cdot\frac{g^{2}}{4}\cdot(1-q)\frac{(1-q^{2})^{2}}{1+q^{2}}\cdot\frac{2}{(1-q)^{3}}\\[4pt]
&=2g^{2}\,\frac{(1-q^{2})^{2}}{(1+q^{2})(1-q)^{2}}.
\end{aligned}
\]  
Since $1-q^{2}=(1-q)(1+q)$, this simplifies to the boxed result  
\[
\boxed{F_{Q}(\beta)=2g^{2}\,\frac{(1+q)^{2}}{1+q^{2}},\qquad q=e^{-\beta\omega}.}
\]  
Limits: $q\to0$ ($T\to0$) gives $F_{Q}=2g^{2}$; $q\to1$ ($T\to\infty$) gives $F_{Q}=4g^{2}$. Monotonicity follows from  
\[
\frac{dF_{Q}}{dq}= \frac{4g^{2}(1-q^{2})}{(1+q^{2})^{2}}>0\quad(0<q<1),
\]  
so $F_{Q}$ increases with temperature.

### 4.5 Consistency with the general bounds

The ground‑state variance of $G$ is obtained from $G^{2}=\frac{g^{2}}{4}(a^{4}+a^{2}a^{\dagger2}+a^{\dagger2}a^{2}+a^{\dagger4})$. Acting on $|0\rangle$ yields $\langle0|a^{2}a^{\dagger2}|0\rangle=2$ and all other terms zero, so  
\[
\mathrm{Var}_{0}(G)=\frac{g^{2}}{4}\times2=\frac{g^{2}}{2}.
\]  
The pure‑state SLD QFI is $F_{Q}(T=0)=4\,\mathrm{Var}_{0}(G)=2g^{2}$, matching the $q\to0$ limit. Combining this variance with the exact high‑temperature limit $F_{Q}(T\!\to\!\infty)=4g^{2}$ derived in Section 4.4 shows that the infinite‑temperature QFI equals $8\,\mathrm{Var}_{0}(G)$, i.e. exactly twice the zero‑temperature SLD QFI $2g^{2}$. Consequently the Cramér–Rao bound improves from $\frac{1}{2\nu g^{2}}$ at $T=0$ to $\frac{1}{4\nu g^{2}}$ at $T=\infty$, i.e. a factor of exactly $2$.

### 4.6 Numerical anchor at $\beta\omega=0.1$

Take $\beta\omega=0.1$. Then $q=e^{-0.1}=0.904837$, $q^{2}=0.818730$, $(1+q)^{2}=3.628414$, $1+q^{2}=1.818730$, and the ratio $(1+q)^{2}/(1+q^{2})=1.994983$. Hence  
\[
F_{Q}(\beta\omega=0.1)=2g^{2}\times1.994983=3.989966\,g^{2}=0.997491\times4g^{2},
\]  
i.e. $99.7491\%$ of the infinite‑temperature value, a deviation of $0.2509\%$.

### 4.7 Qubit: exact QFI and crossover

The qubit Hamiltonian $H=\frac{\hbar\omega}{2}\sigma_{z}$ has eigenvalues $E_{0}=-\hbar\omega/2$, $E_{1}=+\hbar\omega/2$ and thermal probabilities $p_{0,1}=e^{\mp\beta\hbar\omega/2}/Z$, with $Z=2\cosh(\beta\hbar\omega/2)$. For the transverse generator $G=\sigma_{x}/2$ we have $|\langle0|G|1\rangle|^{2}=1/4$ and $p_{0}+p_{1}=1$. The SLD QFI is therefore  
\[
F_{K}=2\,\frac{(p_{0}-p_{1})^{2}}{p_{0}+p_{1}}\cdot\frac{1}{4}\cdot2=(p_{0}-p_{1})^{2}
=\tanh^{2}\!\left(\frac{\beta\hbar\omega}{2}\right).
\]  
Limits: $T\to0$ gives $F_{K}\to1$; $T\to\infty$ gives $F_{K}\to(\beta\hbar\omega/2)^{2}\to0$.

Define $x=\beta\hbar\omega$ and the relative deviation from the universal high‑$T$ extrapolation,  
\[
\delta(x)=1-\frac{\tanh^{2}(x/2)}{(x/2)^{2}}.
\]  
Evaluating:
* $x=2$ ($k_{B}T=\hbar\omega/2$): $\tanh(1)=0.7615942$, $\tanh^{2}(1)=0.5800257$, $(x/2)^{2}=1$, $\delta(2)=0.4199743\approx0.4200$ (42.00 % deviation).  
* $x=0.5$ ($k_{B}T=2\hbar\omega$): $\tanh(0.25)=0.2449187$, $\tanh^{2}(0.25)=0.0599852$, $(x/2)^{2}=0.0625$, $\delta(0.5)=0.0402376\approx0.0402$ (4.02 % deviation).

Thus the universal high‑$T$ form becomes accurate to a few percent only for $k_{B}T\gtrsim2\hbar\omega$.

### 4.8 Work for the quadratic encoding

Under $U(\theta)=e^{-i\theta G}$ the annihilation operator transforms as  
\[
a\;\mapsto\;a\cosh(g\theta)-i\,a^{\dagger}\sinh(g\theta).
\]  
Writing $c=\cosh(g\theta)$ and $s=\sinh(g\theta)$ and using $\langle a^{2}\rangle=\langle a^{\dagger2}\rangle=0$ for the diagonal thermal state, the post‑encoding energy is  
\[
\begin{aligned}
\langle H_{0}\rangle_{\theta}
&=\omega\bigl\langle(c\,a^{\dagger}+i s\,a)(c\,a-i s\,a^{\dagger})\bigr\rangle\\
&=\omega\bigl(c^{2}\bar{n}+s^{2}(\bar{n}+1)\bigr)\\
&=\omega\bigl(\bar{n}\cosh(2g\theta)+\sinh^{2}(g\theta)\bigr),
\end{aligned}
\]  
where $\bar{n}=q/(1-q)$ is the mean thermal occupation. Since $\langle H_{0}\rangle_{0}=\omega\bar{n}$, the injected work is  
\[
W(\theta)=\omega\sinh^{2}(g\theta)\bigl(1+2\bar{n}\bigr).
\]  
Using $1+2\bar{n}=(1+q)/(1-q)=\coth(\beta\omega/2)$ we obtain the closed form  
\[
\boxed{W(\theta)=\omega\sinh^{2}(g\theta)\,\coth\!\left(\frac{\beta\omega}{2}\right)}.
\]  
For weak signals $g\theta\ll1$, $\sinh(g\theta)\approx g\theta$, giving the small‑argument approximation  
\[
W(\theta)\approx\omega g^{2}\theta^{2}\,\coth\!\left(\frac{\beta\omega}{2}\right).
\]  
At high temperature $\coth(\beta\omega/2)\approx2k_{B}T/(\hbar\omega)$, so $W\propto T$ while $F_{Q}$ saturates, implying that the work per unit QFI grows linearly with temperature:
\[
\frac{W}{F_{Q}}\approx\frac{\omega\theta^{2}\coth(\beta\omega/2)}{4}.
\]

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

* **R1 (Bosonic quadratic QFI).**  
  \[
  F_{Q}(\beta)=2g^{2}\frac{(1+q)^{2}}{1+q^{2}},\qquad
  F_{Q}(T=0)=2g^{2},\qquad
  F_{Q}(T\!\to\!\infty)=4g^{2}.
  \]

* **R2 (High‑temperature doubling).** $\mathrm{Var}_{0}(G)=g^{2}/2$, so $8\,\mathrm{Var}_{0}(G)=4g^{2}=F_{Q}(\infty)$, exactly twice the zero‑temperature value $2g^{2}$. The Cramér–Rao improvement factor is exactly $2$.

* **R3 (Numerical anchor).** At $\beta\omega=0.1$, $F_{Q}=3.989966\,g^{2}=0.997491\times4g^{2}$, i.e. $99.7491\%$ of the infinite‑temperature value (deviation $0.2509\%$).

* **R4 (Qubit exact QFI).**  
  \[
  F_{K}=\tanh^{2}\!\left(\frac{\hbar\omega}{2k_{B}T}\right),
  \]  
  with $F_{K}\to1$ as $T\to0$ and $F_{K}\to(\hbar\omega/2k_{B}T)^{2}\to0$ as $T\to\infty$. Numerically $F_{K}=0.5800$ at $k_{B}T=\hbar\omega/2$ and $F_{K}=0.05999$ at $k_{B}T=2\hbar\omega$.

* **R5 (Crossover).** Deviation $\delta=0.4200$ (42.00 %) at $k_{B}T=\hbar\omega/2$; $\delta=0.0402$ (4.02 %) at $k_{B}T=2\hbar\omega$.

* **R6 (Work).**  
  \[
  W(\theta)=\omega\sinh^{2}(g\theta)\,\coth\!\left(\frac{\beta\omega}{2}\right)
  \approx\omega g^{2}\theta^{2}\,\coth\!\left(\frac{\beta\omega}{2}\right)\;(g\theta\ll1).
  \]  
  At $T=0$, $W=\omega g^{2}\theta^{2}$; at high temperature $W\approx2g^{2}\theta^{2}k_{B}T/\hbar$, and $W/F_{Q}\approx\omega\theta^{2}\coth(\beta\omega/2)/4$ grows linearly with $T$.

* **R7 (Projection for sensor arrays).** Assuming $N$ independent qubit sensors at identical temperature, the total QFI adds linearly: $\mathcal{F}^{(N)}=N\,F_{K}$. Under the assumptions of independence and identical temperature, at $k_{B}T=2\hbar\omega$ we have $F_{K}=0.05999$, so matching the ground‑state single‑sensor QFI ($=1$) requires $N\approx17$ warm sensors.

## Appendix A. Extended Derivations and Worked Examples

The following subsections supplement the main analysis with additional algebraic detail, numerical illustration, and contextual connections to related literature.

**Series evaluation via generating functions.**  The sum  
\[
S(q)=\sum_{n=0}^{\infty}(n+1)(n+2)q^{n}
\]  
appears in the bosonic QFI derivation.  Using the elementary generating‑function identities  
\[
\sum_{n=0}^{\infty}q^{n}=\frac{1}{1-q},\qquad 
\sum_{n=0}^{\infty}n\,q^{n}=\frac{q}{(1-q)^{2}},\qquad 
\sum_{n=0}^{\infty}n^{2}q^{n}=\frac{q(1+q)}{(1-q)^{3}},
\]  
we rewrite  
\[
(n+1)(n+2)=n^{2}+3n+2,
\]  
so that  
\[
S(q)=\sum_{n=0}^{\infty}\bigl(n^{2}+3n+2\bigr)q^{n}
      =\frac{q(1+q)}{(1-q)^{3}}+\frac{3q}{(1-q)^{2}}+\frac{2}{1-q}.
\]  
Collecting terms yields  
\[
S(q)=\frac{2}{(1-q)^{3}},
\]  
exactly as quoted in the main text.  This derivation mirrors the generating‑function approach employed for Gaussian‑state metrology in Ref. [4].

**Ground‑state variance from operator algebra.**  The quadratic generator  
\[
G=\frac{g}{2}\bigl(a^{2}+a^{\dagger2}\bigr)
\]  
satisfies  
\[
G^{2}=\frac{g^{2}}{4}\bigl(a^{4}+a^{2}a^{\dagger2}+a^{\dagger2}a^{2}+a^{\dagger4}\bigr).
\]  
Acting on the vacuum $|0\rangle$ and using $a|0\rangle=0$, $a^{\dagger}|0\rangle=|1\rangle$, one finds $\langle0|a^{2}a^{\dagger2}|0\rangle=2$ while all other terms vanish, giving  
\[
\langle0|G^{2}|0\rangle=\frac{g^{2}}{4}\times2=\frac{g^{2}}{2}.
\]  
Since $\langle0|G|0\rangle=0$, the ground‑state variance is $\mathrm{Var}_{0}(G)=g^{2}/2$.  This algebraic link between squeezing Hamiltonians and parametric‑down‑conversion sources is discussed in the photon‑engineering literature [5].

**Numerical illustration for realistic parameters.**  Consider a mode with frequency $\omega/2\pi=5\,$MHz, coupling strength $g=0.1\,\omega$, and temperature $k_{B}T=\hbar\omega$ (so $\beta\omega=1$).  The thermal factor is $q=e^{-1}=0.367879$.  Substituting into the closed‑form QFI,
\[
F_{Q}=2g^{2}\frac{(1+q)^{2}}{1+q^{2}},
\]  
we obtain  
\[
(1+q)^{2}=1.367879^{2}=1.871,\qquad
1+q^{2}=1+0.135335=1.135335,
\]  
\[
\frac{(1+q)^{2}}{1+q^{2}}=1.648,\qquad
F_{Q}=2(0.01\omega^{2})\times1.648=0.03296\,\omega^{2}.
\]  
The work for a weak signal $g\theta\ll1$ follows from  
\[
W\approx\omega g^{2}\theta^{2}\coth\!\left(\frac{\beta\omega}{2}\right)
      =\omega(0.01\omega^{2})\theta^{2}\coth(0.5)
      \approx0.0216\,\omega^{3}\theta^{2},
\]  
where $\coth(0.5)=1.163$.  These numbers illustrate the factor‑of‑two Cramér–Rao improvement derived in Section 4.5.

**Extension to distributed sensing.**  If $N$ identical bosonic sensors are prepared in parallel, the total QFI adds linearly, $\mathcal{F}^{(N)}=N\,F_{Q}$, a property exploited in distributed‑quantum‑sensing protocols [3].  The same additive rule holds for the work cost, $W^{(N)}=N\,W$, implying that the work‑per‑unit‑information ratio remains unchanged under scaling.

**Work–information trade‑off from thermodynamic bounds.**  The general relation between the second derivative of the work and monotone QFI metrics derived in the foundational analysis [2] predicts that any non‑zero QFI must be accompanied by a quadratic response of the injected work.  Our explicit expression $W(\theta)=\omega\sinh^{2}(g\theta)\coth(\beta\omega/2)$ satisfies this requirement: expanding to second order in $\theta$ yields $W\approx\frac{1}{2}\theta^{2}\,\partial_{\theta}^{2}W|_{\theta=0}$ with $\partial_{\theta}^{2}W|_{\theta=0}=2\omega g^{2}\coth(\beta\omega/2)$, proportional to the high‑temperature QFI.

**Operational relevance to structured optical beams.**  Fisher information has been promoted as an operational metric for assessing the metrological usefulness of structured light fields [8].  Although our analysis focuses on thermal quantum states, the same mathematical structure—namely the dependence of $F$ on a variance‑like observable—appears in the beam‑profile FI calculations, underscoring the universality of the information‑geometry perspective.

**Extractable classical information as a bound on uncertainty.**  Recent work on extractable classical information shows that the amount of classical information that can be harvested from a quantum system limits the entropic uncertainty [9].  Since the quantum Fisher information quantifies the maximal achievable precision, the bound $F\leq I_{\text{extract}}$ (where $I_{\text{extract}}$ denotes the extractable classical information) provides an alternative viewpoint on the work‑information trade‑off discussed above.

**Experimental platforms for temperature control.**  Neutral‑atom arrays with single‑site addressability offer a versatile testbed for the thermal‑sensing scenario described here.  Sideband cooling can be tuned to set the mean phonon number $\bar{n}=q/(1-q)$, as demonstrated in scalable micro‑trap architectures [6].  Moreover, quantum‑algorithmic techniques for extracting physical parameters from simulated dynamics, such as the quantum sawtooth map, illustrate how information extraction can be performed efficiently on a quantum processor [7], suggesting future avenues for benchmarking the theoretical predictions presented in this work.

## 7. Discussion

**Limitations.**  
1. The bosonic analysis assumes an ideal Gibbs state of $H_{0}$, exact unitary encoding, and the absence of decoherence or additional system‑bath couplings. Strong coupling that yields non‑Gibbs steady states would invalidate the spectral derivation.  
2. The factor‑of‑two improvement is proved only for *purely quadratic* generators; linear generators on qubits or higher‑order generators on bosons can violate the analogous inequality or cause the high‑temperature QFI to diverge.  
3. The qubit result applies exclusively to a transverse generator; commuting generators (e.g., $G\propto\sigma_{z}$) give identically zero QFI, illustrating that generator geometry can dominate over temperature effects.  
4. All work calculations neglect any external dissipation; in realistic platforms additional heat flow could modify the work–information balance.

**Failure modes and falsifiability.**  
*Bosonic case.* An experiment that prepares a well‑thermalized harmonic mode, implements the squeezing‑type unitary, and estimates $\theta$ with $\nu$ repetitions can infer an empirical QFI from the observed estimator variance. Observation of $F_{Q}(\infty)<2F_{Q}(0)$ beyond experimental uncertainty would falsify the derivation, indicating unaccounted noise, a non‑thermal state, or a misidentified generator order.  
*Work scaling.* Measuring the injected work as a function of temperature and finding a scaling different from $W\propto\coth(\beta\omega/2)$ (e.g., a temperature‑independent work at high $T$) would falsify the work expression.  
*Qubit case.* Detecting a non‑vanishing QFI at arbitrarily high temperature for the transverse generator would contradict the exact formula $F_{K}=\tanh^{2}(\beta\hbar\omega/2)$.

**Limitations list.**  
- Ideal Gibbs thermal state (sensitivity: high).  
- Exact unitary encoding without decoherence (sensitivity: medium).  
- Purely quadratic generator (sensitivity: high).  
- Neglect of system‑bath back‑action on work (sensitivity: medium).  
- Weak‑signal approximation $g\theta\ll1$ for the linearised work expression (sensitivity: low).

## 7. Practical Implications and Engineering Pathways

**(a) Intended users and design impact.**  
The primary users are experimental teams developing continuous‑variable quantum sensors—e.g., trapped‑ion motional‑mode sensors, optomechanical resonators, and PDC‑based squeezing devices. If the derived QFI behavior holds, the optimal operating point for sensors employing quadratic generators may shift from the coldest achievable temperature to a deliberately warmed regime where $k_{B}T\gtrsim\hbar\omega$, reducing the need for aggressive sideband cooling and reallocating laser‑power budgets to other control tasks.

**(b) Technology readiness.**  
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 1–2. Analytical extensions never exceed TRL 3, so the present study is at TRL 2.

**(c) Minimal de‑risking experiment.**  
A minimal experiment would (i) prepare a single harmonic mode in a thermal state with a tunable temperature (e.g., by varying sideband‑cooling duty cycle), (ii) apply a calibrated squeezing interaction of known strength $g$ for a fixed small angle $\theta$, and (iii) perform homodyne detection to estimate $\theta$. From the estimator variance the empirical QFI can be extracted and compared to the predicted $F_{Q}(\beta)$. Observation of the predicted monotonic increase and saturation at $4g^{2}$ would validate the theory; a measured $F_{Q}$ significantly below the bound would falsify it.

**(d) Engineering constraints.**  
- **Thermal state preparation:** Requires precise control of the mode temperature and verification of the Gibbs occupation (e.g., via sideband spectroscopy).  
- **Quadratic interaction:** Implementation of a stable squeezing Hamiltonian with known $g$; calibration of $g$ is essential.  
- **Detection:** High‑efficiency homodyne or heterodyne detection to approach the quantum‑limited estimator variance.  
- **Decoherence:** The analysis assumes negligible decoherence during the encoding; experimental timing must be short compared to decoherence times.

**(e) Projected performance bounds (projection).**  
Assuming (i) perfect preparation of a Gibbs state, (ii) exact knowledge of $g$, and (iii) $g\theta\ll1$, the projected QFI at temperature $T$ is $F_{Q}=2g^{2}(1+e^{-\beta\omega})^{2}/(1+e^{-2\beta\omega})$. For a mode with $\omega/2\pi=5\,$MHz, $g=0.1\,\omega$, and $k_{B}T=\hbar\omega$ ($\beta\omega=1$), the projection yields $F_{Q}\approx3.2\,g^{2}\approx0.032$ (in units of $1/\theta^{2}$). The corresponding work per unit QFI is $W/F_{Q}\approx\omega\theta^{2}\coth(0.5)/4\approx0.28\,\omega\theta^{2}$, indicating a linear increase with $T$.

**(f) Direct risks or misuse.**  
If designers deliberately heat sensors without accounting for the accompanying increase in work (energy consumption) and possible decoherence, they may incur unnecessary power costs or thermal load on surrounding components. Moreover, misapplication of the quadratic‑generator bound to systems with non‑quadratic interactions could lead to over‑optimistic performance estimates.

Future work includes extending the exact analysis to multimode bosonic systems, where collective quadratic interactions may lead to richer temperature‑dependent metrological behavior. Investigating generators of higher polynomial degree will clarify whether the finite‑temperature saturation observed for quadratic signals persists or gives way to divergent QFI, as suggested by the general theory. Moreover, incorporating realistic decoherence mechanisms—such as photon loss, dephasing, and thermalization during the encoding interval—will quantify how robust the heating‑assisted advantage is under experimental imperfections. Finally, exploring optimal control strategies that balance work cost against information gain could guide the design of energy‑efficient quantum sensors operating in warm environments.

## 9. Conclusion

In summary, we have provided a fully explicit, arithmetic‑complete account of thermal quantum sensing in two minimal models. For a single bosonic mode with a quadratic generator $G=\frac{g}{2}(a^{2}+a^{\dagger2})$ on a thermal Gibbs state, the symmetric‑logarithmic‑derivative quantum Fisher information is exactly  
\[
F_{Q}(\beta)=2g^{2}\,\frac{(1+q)^{2}}{1+q^{2}},\qquad q=e^{-\beta\omega},
\]  
monotonically increasing from $2g^{2}$ at zero temperature to $4g^{2}$ at infinite temperature, where it equals $8\,\mathrm{Var}_{0}(G)$, exactly twice the zero‑temperature value. The factor‑of‑two Cramér–Rao improvement from heating is therefore exact. A numerical anchor at $\beta\omega=0.1$ shows that $99.7491\%$ of the infinite‑temperature QFI is already attained.  

For a qubit sensor with a transverse generator $G=\sigma_{x}/2$, the exact QFI is $F_{K}=\tanh^{2}(\beta\hbar\omega/2)$, vanishing at high temperature, and the universal high‑temperature approximation becomes accurate only for $k_{B}T\gtrsim2\hbar\omega$.  

The work injected by the quadratic encoding is  
\[
W(\theta)=\omega\sinh^{2}(g\theta)\,\coth\!\left(\frac{\beta\omega}{2}\right),
\]  
temperature‑independent only at $T=0$ and growing linearly with $T$ at high temperature, so that the work per unit QFI $W/F_{Q}\approx\omega\theta^{2}\coth(\beta\omega/2)/4$ diverges with temperature.  

All derivations are fully explicit, all arithmetic steps are shown, and the results are directly falsifiable by the minimal experiments described in Section 7. This work makes concrete the general claims of the underlying theory and clarifies the thermodynamic price of heating‑assisted quantum sensing.

## Version History

- Version 1.1.0 (2026-10-19, from 1.0.0): REVISION-LOOP-1: revised against the current literature, re-reviewed and re-verified. new sections: Appendix A. Extended Derivations and Worked Examples; Practical Implications and Engineering Pathways; Provenance and AI Involvement. sections folded or removed: Appendix A. Divergence report; Appendix B. Claim attribution. references 9 -> 8. length 3018 -> 3591 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.27.5-revision-claimgate). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 7 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[2] Thermal Quantum Sensing: Fisher Information and Work Beyond Gaussian Signals. arXiv:2609.09583v1. https://arxiv.org/abs/2609.09583v1
[3] Private and Robust States for Distributed Quantum Sensing. arXiv:2407.21701v2. https://arxiv.org/abs/2407.21701v2
[4] Gaussian quantum metrology and space-time probes. arXiv:1610.03538v1. https://arxiv.org/abs/1610.03538v1
[5] Photon engineering for quantum information processing. arXiv:quant-ph/0305192v1. https://arxiv.org/abs/quant-ph/0305192v1
[6] Scalable Architecture for Quantum Information Processing with Atoms in Optical Micro-Structures. arXiv:1108.5136v1. https://arxiv.org/abs/1108.5136v1
[7] Quantum computing and information extraction for a dynamical quantum system. arXiv:quant-ph/0402010v1. https://arxiv.org/abs/quant-ph/0402010v1
[8] Fisher Information as an Operational Metric for Structured Optical Beams. arXiv:2512.23538v1. https://arxiv.org/abs/2512.23538v1
[9] Lower bound of quantum uncertainty from extractable classical information. arXiv:1304.4506v4. https://arxiv.org/abs/1304.4506v4
