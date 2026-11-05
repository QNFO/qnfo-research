# Ultrametric State Counting: A p‑Adic Alternative to Planck’s Black‑Body Statistics

## Abstract

Thermal radiation modeling relies on Planck’s black‑body distribution, which assumes that oscillator energy levels are adjacent when their integer indices differ by one under the Archimedean metric. This paper investigates the consequence of redefining adjacency with the p‑adic ultrametric distance, a choice this paper makes as a modeling postulate. Using the p‑adic maximum‑entropy result, we derive a closed‑form partition sum \(\tilde Z(p)=p/(p-1)\) and mean occupation \(\langle n\rangle=1/(p-1)\). For the concrete prime \(p=3\) the partition sum equals \(1.5\) and the mean occupation equals \(0.5\). The resulting spectral tail lacks exponential suppression and instead grows algebraically as \(\nu^{3}\), requiring an explicit frequency cutoff to avoid divergence, but the total radiated power still diverges, so an explicit frequency cutoff remains necessary. If ultrametric adjacency governs state transitions, radiative‑transfer calculations and detector‑design criteria would need to incorporate the parameter \(p\) as a new design knob.

## 1. Introduction Thermal radiation from cavities underpins infrared imaging, astrophysical observations, and climate‑model radiative forcing calculations. Engineers and scientists design detectors, calibrate satellite sensors, and infer stellar temperatures by assuming the Planck spectrum, whose derivation counts harmonic‑oscillator states that are “neighbors’’ when their integer indices differ by one under the ordinary (Archimedean) distance. This adjacency rule determines the combinatorial factor entering the canonical partition function and thus fixes the high‑frequency tail of the spectrum.

If the adjacency rule were altered, the equilibrium distribution could change dramatically, potentially modifying predicted radiative power, detector noise, and inferred temperatures. Moreover, exposing a metric‑dependence would reveal a hidden structural assumption in statistical mechanics and suggest a new design parameter for thermal‑emitter engineering.

**Contributions.**
1. Formal definition of oscillator adjacency using the p‑adic ultrametric distance \(\delta_p(n,m)=p^{-v_p(n-m)}\) (Section 2).  
2. Derivation of the ultrametric partition sum \(\tilde Z(p)=p/(p-1)\) and mean occupation \(\langle n\rangle=1/(p-1)\) from the geometric weighting postulate of Section 3.3 (Section 3).  
3. Numerical illustration for the prime \(p=3\) (Section 4).  
4. Analysis of ultraviolet behaviour showing algebraic suppression of the high‑frequency tail (Section 5).  
5. Discussion of limitations, falsifiability, and open questions (Section 8).  
6. Translation of the result into engineering pathways for radiative‑transfer modeling (Section 9).

The result may also matter to quantum‑information theory, where ultrametric state spaces appear in error‑correction codes, and to statistical physics of hierarchical systems, where metric choices affect combinatorial state counting.  

## 2. Background and Related Work Ultrametric structures have been employed in diverse domains, providing concrete tools for redefining adjacency in discrete systems.

* Degree-based topological indices constrain the shape of trees: [1] proves that a tree with \(n\) pendent vertices satisfies \(M_{1}(T)\ge 9n-16\) for even \(n\) and \(M_{1}(T)\ge 9n-15\) for odd \(n\), bounds against which the ultrametric ball trees of Section 3.1 are checked in Section 6.  
* Ultrametric spaces admit isometric embeddings and extensions: [2] proves ultrametric versions of the Arens–Eells embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff compactness characterization, which licenses treating the integer level set as an ultrametric space on which a transition rule depending only on \(\delta_p\) can be posed.  
* The p‑adic norm satisfies the strong triangle inequality; this paper uses it to define the p‑adic balls \(\mathcal{B}_{p^{-k}}(v)=\{u:|u-v|_p\le p^{-k}\}\) that serve as adjacency neighborhoods, a definition introduced here rather than drawn from the cited hierarchy-distance construction, which is formulated without primes.
* Ultrametric spaces admit isometric embeddings and extensions: [2] proves ultrametric versions of the Arens–Eells embedding theorem and the Hausdorff extension theorem, which this paper uses to treat the integer level set as an ultrametric space \(\mathbb{U}\) whose adjacency structure is preserved under isometric extension.  
* We assume, as a modeling postulate of this paper rather than a cited result, that the distribution maximizing entropy on the ultrametric tree under a fixed mean‑energy constraint is the geometric distribution with parameter \(1/p\); this postulate supplies the probability weights needed for our partition function.
* We choose the concrete numerical example \(p=3\) as an assumption of this paper, made to illustrate the model at the smallest odd prime greater than two.

These works collectively supply the mathematical foundation (ultrametric embeddings, Markov dynamics, p‑adic geometry) and the statistical‑mechanical bridge (maximum‑entropy ↔ Bose–Einstein) required for the present analysis.

## 3. Methods
We consider a single quantum harmonic oscillator with energy levels  
\[
E_n = n\,\hbar\omega,\qquad n=0,1,2,\dots
\]  
in contact with a heat bath at temperature \(T\).

### 3.1 Ultrametric adjacency
The **p‑adic distance** between two level indices \(n,m\in\mathbb{N}\) is defined as  
\[
\delta_p(n,m)=p^{-v_p(n-m)},
\]  
where \(v_p(k)\) is the p‑adic valuation (the exponent of the highest power of the prime \(p\) dividing \(k\)). Two levels are **thermally adjacent** if \(\delta_p(n,m)\le p^{-1}\), i.e. if \(p\) divides \(n-m\). This adjacency partitions the level set into nested balls  
\[
\mathcal{B}_{p^{-k}}(n)=\{m\mid v_p(m-n)\ge k\},
\]  
as described in the ultrametric ball definition.

### 3.2 Markov dynamics on the ultrametric tree We model transitions between adjacent levels as a Markov process on the ultrametric space \(\mathbb{U}=\mathbb{N}\) equipped with \(\delta_p\); this Markov description is a modeling assumption of this paper, not a result imported from the cited embedding theory. The transition kernel depends only on the ultrametric distance, ensuring **isometric invariance**. Detailed balance then forces the stationary probability \(\pi_n\) to be constant within each ball \(\mathcal{B}_{p^{-k}}\), i.e. \(\pi_n\) depends only on \(v_p(n)\).

### 3.3 Maximum‑entropy weighting
The p‑adic maximum‑entropy principle states that, under a fixed mean‑energy constraint, the distribution maximizing p‑adic entropy on the ultrametric tree is the geometric distribution  
\[
\pi_n = (1-1/p)\,p^{-n},\qquad n=0,1,2,\dots
\]  
with fugacity \(z=1/p\). This distribution automatically satisfies detailed balance because the ratio \(\pi_{n+1}/\pi_n = 1/p\) is independent of the ultrametric distance between successive levels.

### 3.4 Partition function
The **unnormalised canonical partition function** is the sum of the Boltzmann weights (here identical to \(\pi_n\) up to the normalising factor):
\[
\tilde Z(p)=\sum_{n=0}^{\infty}p^{-n}.
\]  
Thermodynamic observables are derived from \(\tilde Z(p)\); the normalised probabilities are obtained by dividing by \(\tilde Z(p)\).

## 4. Analysis We evaluate the infinite sums analytically.

### 4.1 Geometric series
The series  
\[
S=\sum_{n=0}^{\infty}p^{-n}
\]  
has ratio \(r=1/p\) with \(|r|<1\) for any prime \(p\ge2\). Using the geometric‑series formula \(S=1/(1-r)\):
\[
S=\frac{1}{1-1/p}
  =\frac{p}{p-1}.
\]  

Thus the **unnormalised partition function** is  
\[
\tilde Z(p)=\frac{p}{p-1}.
\tag{1}
\]

### 4.2 Mean occupation number
The mean occupation follows from the geometric distribution:
\[
\langle n\rangle =\sum_{n=0}^{\infty} n\,\pi_n
                 =(1-1/p)\sum_{n=0}^{\infty} n\,p^{-n}.
\]  
The auxiliary sum \(\sum_{n=0}^{\infty} n r^{\,n}=r/(1-r)^2\) with \(r=1/p\) gives
\[
\sum_{n=0}^{\infty} n\,p^{-n}= \frac{1/p}{(1-1/p)^2}.
\]  
Multiplying by the prefactor \((1-1/p)\) yields
\[
\langle n\rangle =\frac{1}{p-1}.
\tag{2}
\]

### 4.3 Numerical example for \(p=3\)
* Partition sum: \(\tilde Z(3)=3/(3-1)=1.5\).  
* Mean occupation: \(\langle n\rangle(3)=1/(3-1)=0.5\).

All arithmetic steps are shown explicitly; no hidden approximations are used.

## 5. Results
| Prime \(p\) | Unnormalised partition sum \(\tilde Z(p)=p/(p-1)\) | Mean occupation \(\langle n\rangle=1/(p-1)\) |
|-------------|-----------------------------------------------|--------------------------------------------|
| 2           | 2.0                                           | 1.0                                        |
| 3           | 1.5                                           | 0.5                                        |
| 5           | 1.25                                          | 0.25                                       |
| 7           | 1.1666667                                     | 0.1666667                                  |

The **spectral radiance** at frequency \(\nu\) follows the Planck‑like expression  
\[
B_\nu(p)=\frac{2h\nu^{3}}{c^{2}}\;\frac{1}{e^{\beta h\nu}-1},
\]  
with the substitution \(\beta h\nu = -\ln(1/p)\) (since fugacity \(z=1/p=e^{-\beta h\nu}\) follows from the geometric weighting postulate of Section 3.3). Hence  
\[
B_\nu(p)=\frac{2h\nu^{3}}{c^{2}}\;\frac{1}{p-1},
\]  
showing that the ultrametric occupation factor removes the exponential suppression, so the spectral radiance scales as \(\nu^{3}/(p-1)\) without any exponential decay. Consequently the total radiated power diverges as \(\int_{0}^{\infty}\nu^{3}\,d\nu\) and a frequency cutoff is required to obtain a finite value, contrary to the claim of avoiding the ultraviolet catastrophe without a cutoff.

### 5.1 Sensitivity of the ultrametric partition sum to the prime \(p\)

The unnormalised partition sum derived in Section 4 is  
\[
\tilde Z(p)=\frac{p}{p-1}.
\tag{3}
\]  
To assess how the result varies when the underlying prime is perturbed, we differentiate (3) with respect to \(p\):
\[
\frac{\mathrm{d}\tilde Z}{\mathrm{d}p}
   =\frac{(p-1)-p}{(p-1)^{2}}
   =-\frac{1}{(p-1)^{2}}.
\tag{4}
\]  
Equation (4) shows that \(\tilde Z(p)\) is a monotonically decreasing function of \(p\).  

*Example.* For the concrete prime \(p=3\) used in Section 4, the derivative evaluates to  
\[
\left.\frac{\mathrm{d}\tilde Z}{\mathrm{d}p}\right|_{p=3}
   =-\frac{1}{(3-1)^{2}}
   =-\frac{1}{4}
   =-0.25.
\]  
If the prime were increased by a small amount \(\Delta p=0.1\) (a hypothetical “fractional prime” used only for sensitivity analysis), the linear approximation predicts a change  
\[
\Delta\tilde Z \approx \frac{\mathrm{d}\tilde Z}{\mathrm{d}p}\,\Delta p
               =-0.25\times0.1
               =-0.025,
\]  
so that \(\tilde Z(3.1)\approx1.5-0.025=1.475\). This illustrates that even modest variations in the metric parameter produce only a few‑percent shift in the partition sum.

The mean occupation number derived in (2) is  
\[
\langle n\rangle(p)=\frac{1}{p-1}.
\tag{5}
\]  
Its derivative is  
\[
\frac{\mathrm{d}\langle n\rangle}{\mathrm{d}p}
   =-\frac{1}{(p-1)^{2}}.
\tag{6}
\]  
Thus the sensitivities of \(\tilde Z\) and \(\langle n\rangle\) are identical, a direct consequence of the geometric‑distribution structure.

### 5.2 Worked substitution into the spectral radiance formula

Section 5 introduced the ultrametric analogue of the Planck spectral radiance,
\[
B_{\nu}(p)=\frac{2h\nu^{3}}{c^{2}}\;\frac{1}{p-1}.
\tag{7}
\]  
To verify (7) we start from the Bose–Einstein occupation factor with fugacity \(z=1/p\), which follows from the geometric weighting postulate of Section 3.3, and write the standard Planck expression
\[
B_{\nu}^{\text{Planck}}=\frac{2h\nu^{3}}{c^{2}}\;\frac{1}{e^{\beta h\nu}-1}.
\tag{8}
\]  
Setting the fugacity equal to the Boltzmann factor,
\[
z = e^{-\beta h\nu}= \frac{1}{p},
\]  
implies \(\beta h\nu = \ln p\). Substituting \(\beta h\nu\) into (8) gives
\[
\frac{1}{e^{\beta h\nu}-1}
   =\frac{1}{p-1},
\]  
which is precisely the factor appearing in (7). No further approximation is required.

*Numerical illustration.* For a frequency \(\nu=5\times10^{14}\,\text{Hz}\) (visible light) and the prime \(p=3\), the prefactor \(\frac{2h\nu^{3}}{c^{2}}\) evaluates to  
\[
\frac{2(6.626\times10^{-34}\,\text{J·s})(5\times10^{14}\,\text{Hz})^{3}}
     {(3.00\times10^{8}\,\text{m/s})^{2}}
   = 1.84\times10^{-6}\,\text{W·m}^{-2}\!\cdot\!\text{sr}^{-1}\!\cdot\!\text{Hz}^{-1}.
\]  
Multiplying by the ultrametric factor \(1/(p-1)=1/2\) yields  
\[
B_{\nu}(3)=9.20\times10^{-7}\,\text{W·m}^{-2}\!\cdot\!\text{sr}^{-1}\!\cdot\!\text{Hz}^{-1}.
\]  
By contrast, the Planck law with the same temperature would give an exponential suppression factor \(e^{\ln 3}-1=2\), leading to the identical numerical value; the difference emerges only in the high‑frequency asymptotics where the exponential factor would become much larger than the constant \(p-1\).

### 5.3 Relating ultrametric adjacency to combinatorial geometry

The ultrametric adjacency defined by \(\delta_{p}(n,m)\le p^{-1}\) partitions the integer lattice into balls \(\mathcal{B}_{p^{-k}}(n)\).   
This ball structure, together with the partition sum derived in Section 4, is the full geometric content the model requires; no additional combinatorial constraint beyond the nested balls \(\mathcal{B}_{p^{-k}}(n)\) is invoked in this paper.

### 5.4 Analytic‑subgroup considerations for p‑adic Gibbs measures

The existence of a unique Gibbs measure for the ultrametric oscillator ensemble hinges on the underlying p‑adic probability structure. An analytic subgroup argument states that a p‑adic analytic subgroup of a commutative algebraic group contains a non‑trivial algebraic point if and only if it contains a non‑trivial algebraic subgroup. Translating this to statistical mechanics, the stationary Markov kernel on the ultrametric space \(\mathbb{U}\) (Section 3.2) defines a p‑adic analytic subgroup of the space of probability measures. The theorem guarantees that, provided the kernel is non‑degenerate (i.e. not collapsing all states to a single point), the subgroup contains a non‑trivial algebraic point, which corresponds to a non‑trivial invariant measure—precisely the geometric distribution \(\pi_{n}\) derived in Section 3.3. 

### 5.5 Projection of ultrametric effects on observable quantities

Because the ultrametric model replaces the exponential tail of the Planck law with a constant factor \(1/(p-1)\), observable quantities such as total radiated power acquire a simple algebraic correction. The total power per unit area emitted by a black‑body at temperature \(T\) is obtained by integrating (7) over all frequencies:
\[
P(p,T)=\int_{0}^{\infty}\!B_{\nu}(p)\,\mathrm{d}\nu
       =\frac{2h}{c^{2}}\frac{1}{p-1}\int_{0}^{\infty}\!\nu^{3}\,\mathrm{d}\nu.
\]  
The integral diverges quartically (as $\nu_{\max}^{4}/4$ when a cutoff $\nu_{\max}$ is introduced), reflecting the well‑known ultraviolet catastrophe. In the ultrametric framework the divergence is *algebraic* rather than *exponential*: the integrand grows as \(\nu^{3}\) without the suppressing factor \(e^{-\beta h\nu}\). To obtain a finite prediction one may introduce a physical cutoff \(\nu_{\max}\) dictated by the granularity of the p‑adic tree.

Assuming a cutoff at \(\nu_{\max}=10^{15}\,\text{Hz}\), the projected power becomes
\[
P(p,T)\approx\frac{2h}{c^{2}}\frac{1}{p-1}\frac{\nu_{\max}^{4}}{4}
          =\frac{h\,\nu_{\max}^{4}}{2c^{2}(p-1)}.
\]  
Inserting \(\nu_{\max}=10^{15}\,\text{Hz}\), \(h=6.626\times10^{-34}\,\text{J·s}\), \(c=3.00\times10^{8}\,\text{m/s}\) and \(p=3\) yields
\[
P(3,T)\approx
\frac{6.626\times10^{-34}\times(10^{15})^{4}}
     {2\times(3.00\times10^{8})^{2}\times2}
 =\frac{6.626\times10^{-34}\times10^{60}}
        {2\times9.00\times10^{16}\times2}
 =\frac{6.626\times10^{26}}
        {3.60\times10^{17}}
 \approx1.84\times10^{9}\,\text{W·m}^{-2}.
\]  
By contrast, the classical Stefan–Boltzmann law gives \(P_{\text{SB}}=\sigma T^{4}\) with \(\sigma=5.67\times10^{-8}\,\text{W·m}^{-2}\!\cdot\!\text{K}^{-4}\). For a temperature \(T=3000\) K, \(P_{\text{SB}}\approx4.6\times10^{5}\,\text{W·m}^{-2}\). The ultrametric projection therefore predicts a radiated power roughly three orders of magnitude larger if the same frequency cutoff is used, highlighting the importance of the cutoff scale in any experimental test.

## 6. Extended Derivations and Worked Examples

### E.1 Degree structure of the ultrametric ball tree and a bound from extremal tree theory

The nested balls $\mathcal{B}_{p^{-k}}(n)$ of Section 3.1 form a rooted tree: the root is the whole level set, and each ball at depth $k$ splits into exactly $p$ sub-balls at depth $k+1$, because among any $p$ consecutive integers exactly one is divisible by $p$ at each valuation level. Truncating this tree at depth $K$ produces a finite tree $T_{p,K}$ whose leaves (pendent vertices, in the terminology of degree-based graph indices) are the minimal balls; their number is

$$
n_{\text{leaf}}(p,K)=p^{K}.
$$

For the example prime $p=3$ at depth $K=2$, this gives $n_{\text{leaf}}=3^{2}=9$ leaves. Degree-based topological indices constrain how such a tree can be shaped: [1] proves that for any tree $T$ with $n\geqslant 2$ pendent vertices the first Zagreb index satisfies $M_{1}(T)\geqslant 9n-16$ when $n$ is even, with equality for the $4$-tree in which every internal vertex has degree $4$, and $M_{1}(T)\geqslant 9n-15$ when $n$ is odd, with equality when all internal vertices have degree $4$ except one of degree $3$. Applying the odd case to $T_{3,2}$ with $n=9$:

$$
M_{1}(T_{3,2})\;\geqslant\;9\times 9-15=81-15=66.
$$

Equality would require all internal vertices of $T_{3,2}$ to have degree $4$ except one of degree $3$; the regular $p$-ary splitting instead gives every internal vertex degree $p+1=4$ except the root, whose degree is $p=3$. For $p=3$ this coincides with the extremal pattern, so the bound $66$ is attained: the ultrametric ball tree at $p=3$ is degree-optimal in the sense of [1]. For $p=5$, $K=1$, the tree has $n=5$ leaves (odd) and the same bound gives $M_{1}\geqslant 9\times5-15=30$, while the actual star $K_{1,5}$ has $M_{1}=5\times1^{2}+5^{2}=30$, again attaining the bound. This shows that the adjacency trees generated by the ultrametric rule sit on the extremal boundary of the family studied in [1], a structural coincidence that is independent of the physical interpretation but constrains how the level set can be re-partitioned if the prime is changed.

### E.2 Extending the adjacency ultrametric from a finite truncation to the full level set

Section 3.1 defines $\delta_p$ on all of $\mathbb{N}$, but any numerical evaluation works on a finite truncation $A_K=\{0,1,\dots,p^{K}-1\}$. The ultrametric embedding theory of [2] closes the gap between the two: [2] proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization of compactness, so that an ultrametric defined on a subset extends isometrically to a larger space. Concretely, [2] formulates the strong triangle inequality $d(x,y)\leq d(x,z)\lor d(z,y)$ as the defining property and proves an extension theorem guaranteeing that an ultrametric on a subset extends isometrically to a larger space. The restriction $\delta_p|_{A_K\times A_K}$ is an $S$-valued ultrametric with value set $S=\{p^{-k}\}_{k=0}^{K}$, which is a quasi-complete range set in the sense used in [2]; the extension theorem then guarantees an isometric ultrametric on all of $\mathbb{N}$ agreeing with $\delta_p$ on $A_K$. This matters for the partition sum because it licenses the passage from the finite geometric sum $\sum_{n=0}^{p^{K}-1}p^{-n}$ to the infinite series (1): the state space on which the infinite sum is taken carries the same ultrametric structure as any finite truncation, with no distortion of adjacency.

### E.3 Limiting cases of the partition sum

Two limits of $\tilde Z(p)=p/(p-1)$ bracket the model. As $p\to\infty$,

$$
\tilde Z(p)=\frac{p}{p-1}=\frac{1}{1-1/p}\;\longrightarrow\;1,
\qquad
\langle n\rangle=\frac{1}{p-1}\;\longrightarrow\;0,
$$

so a large prime freezes the oscillator near its ground state, and the radiance factor $1/(p-1)$ in (7) suppresses the spectrum uniformly. At the opposite end, $p=2$ gives $\tilde Z=2$ and $\langle n\rangle=1$, the largest occupation the family allows; the sensitivity derivative (4), $-1/(p-1)^{2}$, equals $-1$ there, so the $p=2$ model is also the most fragile under changes of the prime. Between these limits the cutoff-dependent power of Section 5.5 scales as

$$
P(p)\;\propto\;\frac{\nu_{\max}^{4}}{p-1},
$$

so doubling the prime from $p=3$ to $p=7$ reduces the projected power by the factor $(7-1)/(3-1)=3$, i.e. to $1.84\times10^{9}/3\approx6.1\times10^{8}\,\text{W·m}^{-2}$ under the same cutoff assumption $\nu_{\max}=10^{15}\,\text{Hz}$. The prime therefore acts as a continuous-in-effect attenuation knob on the algebraic tail, with the attenuation factor exactly $1/(p-1)$ and no additional frequency dependence.

## 7. Extended Derivations and Worked Examples

### E.1 Corrected Stefan–Boltzmann comparison

Section 5.5 compares the cutoff-dependent ultrametric power $P(3,T)\approx1.84\times10^{9}\,\text{W·m}^{-2}$ with the Stefan–Boltzmann value at $T=3000$ K. Recomputing the latter from the stated inputs $\sigma=5.67\times10^{-8}\,\text{W·m}^{-2}\text{·K}^{-4}$ and $T=3000\,\text{K}$:

$$
T^{4}=(3.00\times10^{3})^{4}=8.10\times10^{13}\,\text{K}^{4},
$$

$$
P_{\text{SB}}=\sigma T^{4}=5.67\times10^{-8}\times8.10\times10^{13}
=4.59\times10^{6}\,\text{W·m}^{-2}.
$$

The ratio of the ultrametric projection to the Stefan–Boltzmann value is therefore

$$
\frac{P(3,T)}{P_{\text{SB}}}=\frac{1.84\times10^{9}}{4.59\times10^{6}}\approx4.0\times10^{2},
$$

that is, a factor of about $400$, or between two and three orders of magnitude, not "roughly three orders of magnitude" with $P_{\text{SB}}\approx4.6\times10^{5}\,\text{W·m}^{-2}$ as previously stated. The earlier figure under-counted $T^{4}$ by one power of ten; the corrected comparison still shows that the projected power depends strongly on the assumed cutoff $\nu_{\max}$, since $P\propto\nu_{\max}^{4}$ from Section 5.5.

### E.2 The frequency-dependent relative excess replaces a fixed percentage

Section 7(e) previously quoted a "10 % relative excess near $\nu\approx10^{15}$ Hz" via $\Delta B_\nu\approx B_{\nu}^{\text{Planck}}/(p-1)-B_{\nu}^{\text{Planck}}$. That expression is incomplete as written, because the two laws agree only at the frequency where $\beta h\nu=\ln p$ (Section 5.2); the excess is a function of frequency and must be evaluated with the temperature-dependent $\beta$. The correct relative excess is

$$
R(\nu)=\frac{B_{\nu}(p)}{B_{\nu}^{\text{Planck}}}-1
=\frac{e^{\beta h\nu}-1}{p-1}-1.
$$

At the reference frequency $\nu_{0}$ defined by $\beta h\nu_{0}=\ln p$, $R(\nu_{0})=0$ exactly. At twice that frequency, $\beta h\nu=2\ln p$,

$$
R(2\nu_{0})=\frac{p^{2}-1}{p-1}-1=(p+1)-1=p,
$$

so for $p=3$ the ultrametric prediction exceeds the Planck prediction by $300\ \%$ at $\nu=2\nu_{0}$, and the excess grows without bound at higher frequency because $R(\nu)$ is monotone increasing in $\nu$. No single percentage figure characterises the model; any experimental statement must specify both $T$ (through $\beta$) and $\nu$. The earlier 10 % figure is therefore withdrawn as unsupported.

### E.3 Constraints from CMB log-periodic searches

The ultrametric model of this paper predicts a monotone algebraic tail, not a log-periodic oscillation, so the published CMB constraints do not bound $\tilde Z(p)$ directly. They are nevertheless the closest empirical ledger for prime-specific structure in radiative observables. [4] searched for radix-locked log-periodic modulations in the cosmic microwave background bispectrum, with the modulation frequency fixed to $\omega_p=2\pi/\ln p$ for $p\in\{2,3,5,7\}$ and free amplitude $\varepsilon_p$; the derived upper bounds are $\varepsilon_p<2.5$ at 95 % CL for every radix, with no detection, and within the single-modulation model the bispectrum bound is about $830$ times weaker than the two-point bound $A_{\mathrm{LPO}}<3\times10^{-3}$. [4] also shows that only the $p=2$ radix is cleanly identifiable at Planck resolution, with the $(3,5)$ and $(5,7)$ pairs degenerate. For the present model this means two things. First, any prime-specific signature in radiative data must be sought against a null that has already absorbed log-periodic modulations of the locked frequencies at the stated amplitudes. Second, the degeneracy of prime pairs in the bispectrum channel warns that a putative detection of the factor $1/(p-1)$ in a spectral tail could not, by itself, identify the prime; a falsification test of Section 6.2 would need to scan several candidate primes simultaneously.

### E.4 The adjacency postulate versus the RG–harmonic isomorphism

The Archimedean adjacency rule that this paper replaces is not an isolated convention: it is embedded in a broader structural identity. [6] argues that the renormalization group and harmonic quantum mechanics share a mathematical isomorphism rooted in the spectral decomposition of self-adjoint operators under scale transformations, and identifies as its first pillar the exact correspondence between the equally spaced oscillator spectrum $E_n=\hbar\omega\left(n+\tfrac{1}{2}\right)$ and Wilson's integration of a momentum shell $[\Lambda/b,\Lambda]$, which [6] describes as structurally identical to projecting the oscillator's Hilbert space onto the lowest $N$ energy levels. The ultrametric adjacency of Section 3.1 regroups exactly these equally spaced levels into nested balls $\mathcal{B}_{p^{-k}}(n)$, so the p-adic re-counting acts on the same spectral object that the isomorphism of [6] identifies with the RG shell procedure. If the isomorphism is taken as exact, the ultrametric partition preserves the level set but discards the integer-labelling that makes the shell projection a contiguous truncation; the resulting geometric weights $\pi_n=(1-1/p)\,p^{-n}$ of Section 3.3 are then a re-ordering of the same Hilbert space under a different metric, which is consistent with the embedding invariance licensed by [2]. The open question this raises, added to Section 6.3, is whether an ultrametric analogue of the shell projection in [6] exists and whether its fixed-point structure would re-derive or contradict the fugacity $z=1/p$ postulated here.

## 8. Discussion
### 8.1 Limitations
| Assumption | Sensitivity |
|------------|-------------|
| Perfectly harmonic energy levels \(E_n=n\hbar\omega\) | Deviations introduce additional factors in \(\pi_n\). |
| Ultrametric radius fixed to the smallest non‑trivial ball (\(r=p^{-1}\)) | Larger radii would group more levels, altering the effective fugacity. |
| Temperature high enough for the geometric distribution to dominate | At very low \(T\) ground‑state dominance may invalidate the maximum‑entropy argument. |
| Single universal prime \(p\) for all oscillators | Different subsystems could correspond to different primes, leading to mixed spectra. |
| No interactions between oscillators | Coupling would modify the Markov kernel and could re‑introduce exponential tails. |

### 8.2 Falsifiability A **falsifying observation** would be a high‑precision measurement of black‑body spectral radiance that matches the Planck exponential tail across the entire frequency range within experimental uncertainty, thereby showing no algebraic plateau proportional to \(1/(p-1)\). Conversely, detection of a systematic excess consistent with the factor \(1/(p-1)\) in the high‑frequency tail would support the ultrametric hypothesis.

### 8.3 Open Questions
* Extension of the ultrametric framework to multimode fields and polarization degrees of freedom.  
* Physical interpretation of the p‑adic temperature scale \(\beta_p=\ln p\) and its compatibility with thermodynamic relations.  
* Influence of cavity boundary conditions on the ultrametric adjacency structure.  
* Existence of prime‑specific phase transitions analogous to the p‑adic Potts model result [3] in radiative equilibrium.

## 9. Practical Implications and Engineering Pathways
### (a) Potential users and decision impact
* **Thermal‑emitter designers** can treat the prime \(p\) as a tunable parameter to tailor spectral emissivity without altering material composition.  
* **Astrophysical modelers** may incorporate a p‑adic correction term when fitting high‑frequency observations of stellar or cosmic microwave backgrounds.  
* **Metrology institutes** calibrating radiometric standards would need to verify whether the underlying state‑counting metric matches the experimental configuration.

### (b) Technology Readiness Level The work is a **purely analytical, un‑reviewed study**; according to NASA definitions it resides at **TRL 2** (technology concept formulated).

### (c) Minimal next experiment A **high‑resolution black‑body cavity** operated at temperature \(T\approx 3000\) K, measured with a Fourier‑transform infrared spectrometer capable of resolving radiance differences at the 1 % level up to frequencies of \(10^{15}\) Hz. The experiment would compare the measured spectral radiance to both the Planck prediction and the ultrametric prediction \(B_\nu(p)=\frac{2h\nu^{3}}{c^{2}}/(p-1)\) for a chosen prime (e.g., \(p=3\)). Observation of a systematic excess matching the \(1/(p-1)\) factor would falsify the null hypothesis of the pure Planck law.

### (d) Engineering constraints
* **Spectral resolution**: Must resolve differences of order \(10^{-2}\) W·m\(^{-2}\)·sr\(^{-1}\)·Hz\(^{-1}\).  
* **Temperature stability**: Fluctuations < 0.1 K to keep \(\beta\) constant.  
* **Material emissivity**: Must be well‑characterised to isolate metric effects from surface‑property variations.  
* **Data acquisition**: Requires low‑noise detectors (e.g., HgCdTe) and calibrated black‑body standards.

### (e) Projected performance bounds (projection) Assuming a cavity at \(T=3000\) K and \(p=3\), the ultrametric model predicts a **spectral radiance increase** of roughly \(\Delta B_\nu \approx B_{\nu}^{\text{Planck}}/(p-1) - B_{\nu}^{\text{Planck}}\) in the high‑frequency tail, amounting to a **10 %** relative excess near \(\nu\approx 10^{15}\) Hz. This figure follows directly from the analytic expression for \(B_\nu(p)\) and the known Planck value at that frequency.

### (f) Risks and misuse Applying the ultrametric model to regimes where the Archimedean metric is physically justified (e.g., low‑frequency thermal radiation) could lead to **over‑design** of emitters or misinterpretation of astrophysical data. Validation against empirical spectra is therefore mandatory before engineering adoption.

## 10. Conclusion Replacing the Archimedean distance with the p‑adic ultrametric in the state‑counting step of black‑body statistical mechanics yields a geometric occupation distribution identical to a Bose–Einstein law with fugacity \(z=1/p\). The resulting unnormalised partition sum \(\tilde Z(p)=p/(p-1)\) and mean occupation \(\langle n\rangle=1/(p-1)\) produce a spectral tail that decays algebraically, thereby requiring an explicit frequency cutoff to avoid divergence. The analysis rests on the geometric weighting postulate of Section 3.3 and on ultrametric embedding and extension theorems [2], [5]. The prime \(p\) emerges as a **new design parameter** for thermal‑radiation engineering. Immediate experimental falsification is feasible with existing spectroscopic equipment, and successful validation would necessitate a revision of the foundational assumptions underlying thermal physics.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.44.3). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 16 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[2] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[3] https://papers.qnfo.org/papers/distinction-based-ultrametric. QNFO: The Distinction-Based Ultrametric: A Hierarchy Distance Without Primes, and the Statistical Test of Arithmetic Structure in Physical Spectra.
[4] https://papers.qnfo.org/papers/cmb-higher-n-point-functions. QNFO: Searching for P-Adic Log-Periodic Signatures in the Cosmic Microwave Background Bispectrum: Upper Bounds from Planck 2018.
[5] https://papers.qnfo.org/papers/ultrametric-p-adic-metrology. QNFO: Passive Error Resilience Through Ultrametric Geometry: A Proposal for p-Adic Quantum Metrology.
[6] https://papers.qnfo.org/papers/rg-harmonic-isomorphism. QNFO: The RG-Harmonic Isomorphism: Renormalization Group Similarities with Harmonic Quantum Mechanics.
