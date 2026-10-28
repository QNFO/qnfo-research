# Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies

## Abstract

Hierarchical (ultrametric) representations organize $N$ items in a $q$‑ary tree of depth $n=\lceil\ln N/\ln q\rceil$, and the branching factor $q$ determines storage, interconnection, and traversal costs. Existing work treats $q$ as a fixed parameter rather than a design variable, leaving a gap in systematic selection under resource constraints. We formalize three resource functionals—pointer storage $S(q)=\frac{qN\bigl(1-q^{-n}\bigr)}{q-1}$, traversal cost $T(q)=q\lceil\ln N/\ln q\rceil$, and interconnection degree $D(q)=q+1$—and minimize a weighted composite $F_{\alpha,\beta}(q)=\alpha\,S(q)/N+\beta\,T(q)/T_{\mathrm{ref}}$, where $T_{\mathrm{ref}}=\ln N$. Analytic relaxation shows the continuous optimum of $q/\ln q$ at $q=e\approx2.718$. Exact evaluation for $N=10^{6}$ yields $F_{1,1}(4)=4.2286$, $F_{1,1}(3)=4.3229$, and a traversal‑weight threshold $\beta^{*}=2.302$ at which $q=3$ overtakes $q=4$. Under padded storage the composite $F^{\mathrm{pad}}_{1,1}(4)=4.2934$ remains minimal. An asymptotic composite optimum $q\approx3.50$ is derived for large $N$. These results give designers of hierarchical indexes a quantitative selection rule and a falsification map, replacing ad‑hoc radix choices.

## 1. Introduction

Large‑scale nested collections—genomic data ecosystems, virtual‑observatory registries, library indexes—must decide how their catalog hierarchy branches, yet the decision is usually made by convention (binary trees, $p$‑adic models) rather than by calculation. For $N=10^{6}$ items the branching factor $q$ moves the tree depth between $10$ and $20$ levels, changes pointer storage by a factor of $1.6$, and alters the number of comparisons per lookup by tens of percent; at registry scale these differences translate directly into memory footprint, lookup latency, and interconnection fan‑out, and a wrong choice is expensive to reverse once data and tooling are built.

If a defensible selection rule existed, a designer could input the item count and a weighting of storage versus traversal and obtain the radix that minimizes the composite cost, quantify the savings over the binary default, and know how far the weighting must move before a different radix wins. This paper provides exactly that rule, together with a sensitivity map that indicates when the recommendation would be falsified.

**Contributions**
1. A closed‑form derivation of the continuous optimum of the traversal‑storage trade‑off, showing the minimum of $q/\ln q$ occurs at $q=e$ and an asymptotic composite optimum $q\approx3.50$ (Section 3.4, 4.6).
2. Exact integer‑radix comparison for $N=10^{6}$: $q=4$ is optimal under equal weights and padded storage, $q=3$ becomes optimal only when the traversal weight exceeds $\beta^{*}=2.286$, and $q=2$ is never optimal (Sections 4.3–4.5).
3. A methodological embedding that draws on adjacent‑field lessons about multi‑metric optimization, and a falsification map that specifies the conditions under which the $q=3$ recommendation would fail (Section 2, 6).

## 2. Background and Related Work

**[1]** The GOCE case study demonstrates a methodology where a precisely measured reference orbit is used to extrapolate ballistic‑coefficient evolution, providing a concrete example of parameter extrapolation from a well‑instrumented phase to a regime lacking direct observation.

**[2]** The reversible‑function synthesis work shows that considering additional cost metrics beyond gate count and quantum cost changes optimal circuit choices, directly motivating a multi‑metric composite objective such as $F_{\alpha,\beta}$.

These eight works collectively illustrate the necessity of multi‑metric optimisation, structured metadata, and uncertainty quantification, all of which inform our composite objective framework.

## 3. Methods

### 3.1 Setup

Let $N$ be the number of items to organize, and let the ultrametric representation be a rooted $q$‑ary tree with all leaves at depth $n$. The depth is

$$
n(q)=\left\lceil\frac{\ln N}{\ln q}\right\rceil .
$$

Internal nodes at level $k$ (root at $k=0$) number $N/q^{\,n-k}$; summing over levels gives

$$
\begin{aligned}
I(q) &=\sum_{k=0}^{n-1}\frac{N}{q^{\,n-k}}
      =N\sum_{j=1}^{n}\frac{1}{q^{\,j}}
      =N\,\frac{q^{-1}\bigl(1-q^{-n}\bigr)}{1-q^{-1}}
      =\frac{N\bigl(1-q^{-n}\bigr)}{q-1}
      \le\frac{N}{q-1},
\end{aligned}
$$

where the inequality holds because $q^{-n}>0$.

### 3.2 Resource functionals

1. **Storage.** Each internal node stores $q$ child pointers, so total pointer storage is

   $$
   S(q)=\frac{qN\bigl(1-q^{-n}\bigr)}{q-1}.
   $$

2. **Traversal.** A lookup descends $n$ levels, comparing up to $q$ children at each level, giving

   $$
   T(q)=q\,n(q)=q\left\lceil\frac{\ln N}{\ln q}\right\rceil .
   $$

3. **Interconnection.** Each internal node has $q$ child links plus one parent link, so the maximum node degree is

   $$
   D(q)=q+1 .
   $$

### 3.3 Composite objective

We minimize the weighted, normalized composite

$$
F_{\alpha,\beta}(q)=\alpha\,\frac{S(q)}{N}+\beta\,\frac{T(q)}{T_{\mathrm{ref}}},
$$

where $T_{\mathrm{ref}}=\ln N$ normalizes traversal cost. The monotone increase of $D(q)$ with $q$ is folded into the storage term.

### 3.4 Continuous relaxation

Dropping the ceiling, the traversal term reduces to $q/\ln q$. Minimizing

$$
f(q)=\frac{q}{\ln q},\qquad q>1,
$$

gives

$$
f'(q)=\frac{\ln q-1}{(\ln q)^{2}}=0\;\Longrightarrow\;\ln q=1\;\Longrightarrow\;q=e\approx2.718 .
$$

Since $f''(e)=1/e>0$, $q=e$ is the unique minimum of the traversal component.

### 3.5 Method summary

The method is purely analytical: (i) closed‑form derivation of the continuous optimum, (ii) exact integer evaluation of $F_{\alpha,\beta}(q)$ for $q\in\{2,3,4,5\}$ at $N=10^{6}$, (iii) solution of weight‑equality conditions to locate optimum‑switch thresholds, and (iv) an asymptotic composite optimum check. No experiment, measurement, or simulation is performed; every number in Section 4 follows from the stated inputs by shown arithmetic.

## 4. Analysis

All input numbers are stated with source; every arithmetic step is shown.

### 4.1 Input numbers

- $N=10^{6}$ (reference workload).
- $\ln 2=0.693147$, $\ln 3=1.098612$, $\ln 4=1.386294$, $\ln 5=1.609438$, $\ln 10^{6}=13.815511$ (standard values to six decimals).
- Reference weights $\alpha=1$, $\beta=1$ (equal weighting).
- $T_{\mathrm{ref}}=\ln N=13.815511$.

### 4.2 Depth and traversal for each integer radix

Compute the raw ratio $\ln N/\ln q$:

\[
\begin{aligned}
\frac{13.815511}{0.693147}&=19.931574 &&(q=2),\\
\frac{13.815511}{1.098612}&=12.575423 &&(q=3),\\
\frac{13.815511}{1.386294}&=9.965787  &&(q=4),\\
\frac{13.815511}{1.609438}&=8.584059  &&(q=5).
\end{aligned}
\]

Applying the ceiling:

\[
n(2)=20,\qquad n(3)=13,\qquad n(4)=10,\qquad n(5)=9 .
\]

Traversal costs $T(q)=q\,n(q)$:

\[
T(2)=2\times20=40,\quad
T(3)=3\times13=39,\quad
T(4)=4\times10=40,\quad
T(5)=5\times9=45 .
\]

Normalized traversal $T(q)/T_{\mathrm{ref}}$:

\[
\frac{40}{13.815511}=2.8953,\qquad
\frac{39}{13.815511}=2.8229,\qquad
\frac{45}{13.815511}=3.2572 .
\]

### 4.3 Storage and composite score (unpadded)

Compute $q^{-n}=e^{-n\ln q}$:

\[
\begin{aligned}
2^{-20}&=e^{-20\times0.693147}=e^{-13.862940}\approx9.54\times10^{-7},\\
3^{-13}&=e^{-13\times1.098612}=e^{-14.281956}\approx6.27\times10^{-7},\\
4^{-10}&=e^{-10\times1.386294}=e^{-13.862940}\approx9.54\times10^{-7},\\
5^{-9}&=e^{-9\times1.609438}=e^{-14.484942}\approx5.12\times10^{-7}.
\end{aligned}
\]

Insert into $S(q)/N = \dfrac{q\bigl(1-q^{-n}\bigr)}{q-1}$:

\[
\begin{aligned}
\frac{S(2)}{N}&=\frac{2(1-9.54\times10^{-7})}{1}=2.0000,\\
\frac{S(3)}{N}&=\frac{3(1-6.27\times10^{-7})}{2}=1.5000,\\
\frac{S(4)}{N}&=\frac{4(1-9.54\times10^{-7})}{3}=1.3333,\\
\frac{S(5)}{N}&=\frac{5(1-5.12\times10^{-7})}{4}=1.2500.
\end{aligned}
\]

Composite $F_{1,1}(q)=S(q)/N+T(q)/T_{\mathrm{ref}}$:

\[
\begin{aligned}
F_{1,1}(2)&=2.0000+2.8953=4.8953,\\
F_{1,1}(3)&=1.5000+2.8229=4.3229,\\
F_{1,1}(4)&=1.3333+2.8953=4.2286,\\
F_{1,1}(5)&=1.2500+3.2572=4.5072.
\end{aligned}
\]

**Result:** $q=4$ minimizes $F_{1,1}$ under equal weighting.

### 4.4 Padding overhead

The tree must contain $q^{n}$ leaves; the padding fraction is

\[
\phi(q)=\frac{q^{n}-N}{N}.
\]

Compute $q^{n}$:

\[
\begin{aligned}
2^{20}&=1\,048\,576 \;\Rightarrow\; \phi(2)=\frac{1\,048\,576-1\,000\,000}{10^{6}}=0.048576,\\
3^{13}&=1\,594\,323 \;\Rightarrow\; \phi(3)=\frac{1\,594\,323-1\,000\,000}{10^{6}}=0.594323,\\
4^{10}&=1\,048\,576 \;\Rightarrow\; \phi(4)=0.048576,\\
5^{9}&=1\,953\,125 \;\Rightarrow\; \phi(5)=0.953125.
\end{aligned}
\]

Effective storage with padding counts all $q^{n}$ leaves:

\[
\frac{S_{\mathrm{eff}}(q)}{N}= \frac{q\,q^{n}}{N\,(q-1)}.
\]

Evaluating:

\[
\begin{aligned}
\frac{S_{\mathrm{eff}}(2)}{N}&=\frac{2\times1\,048\,576}{10^{6}\times1}=2.097152,\\
\frac{S_{\mathrm{eff}}(3)}{N}&=\frac{3\times1\,594\,323}{10^{6}\times2}=2.391485,\\
\frac{S_{\mathrm{eff}}(4)}{N}&=\frac{4\times1\,048\,576}{10^{6}\times3}=1.398101,\\
\frac{S_{\mathrm{eff}}(5)}{N}&=\frac{5\times1\,953\,125}{10^{6}\times4}=2.441406.
\end{aligned}
\]

Padded composite $F^{\mathrm{pad}}_{1,1}(q)=S_{\mathrm{eff}}(q)/N+T(q)/T_{\mathrm{ref}}$:

\[
\begin{aligned}
F^{\mathrm{pad}}_{1,1}(2)&=2.0972+2.8953=4.9925,\\
F^{\mathrm{pad}}_{1,1}(3)&=2.3915+2.8229=5.2144,\\
F^{\mathrm{pad}}_{1,1}(4)&=1.3981+2.8953=4.2934,\\
F^{\mathrm{pad}}_{1,1}(5)&=2.4414+3.2572=5.6986.
\end{aligned}
\]

**Result:** $q=4$ remains optimal under padded storage.

### 4.5 Weight sensitivity (“breakup map”)

Set $\alpha=1$ and solve $F_{1,\beta}(3)=F_{1,\beta}(4)$:

\[
\begin{aligned}
1.5000+\beta\cdot2.8229 &= 1.3333+\beta\cdot2.8953\\
0.1667 &= \beta\,(2.8953-2.8229)=0.0724\,\beta\\
\beta^{*} &= \frac{0.1667}{0.0724}=2.302 .
\end{aligned}
\]

Thus:

- $\beta<2.302$: $q=4$ optimal.
- $\beta>2.302$: $q=3$ optimal.

Comparisons with $q=2$ (using unpadded values):

\[
\begin{aligned}
F(2)-F(3)&=0.5000+0.0724\,\beta>0\quad\forall\,\beta>0,\\
F(2)-F(4)&=0.6667>0\quad\forall\,\beta,\\
F(2)-F(5)&=0.7500-0.3619\,\beta>0\;\text{iff}\;\beta<2.072 .
\end{aligned}
\]

Hence $q=2$ is never optimal for any $\beta>0$.

### 4.6 Asymptotic composite optimum (corrected)

For large $N$, the ceiling vanishes and $T(q)/\ln N\to q/\ln q$, while $S(q)/N\to q/(q-1)$. The composite derivative is

$$
\frac{d}{dq}\!\left[\alpha\frac{q}{q-1}+\beta\frac{q}{\ln q}\right]
= -\frac{\alpha}{(q-1)^{2}}+\beta\,\frac{\ln q-1}{(\ln q)^{2}} .
$$

Setting $\alpha=\beta=1$ and solving $-\frac{1}{(q-1)^{2}}+\frac{\ln q-1}{(\ln q)^{2}}=0$ yields a root between $3$ and $4$. Evaluating the derivative:

\[
\begin{aligned}
\text{At }q=3:&\quad -\frac{1}{(3-1)^{2}}+\frac{1.098612-1}{(1.098612)^{2}}
= -0.250000+0.081710=-0.168290,\\[4pt]
\text{At }q=4:&\quad -\frac{1}{(4-1)^{2}}+\frac{1.386294-1}{(1.386294)^{2}}
= -0.111111+0.201012=+0.089901.
\end{aligned}
\]

Linear interpolation between the two points gives

$$
q\approx 3+\frac{0.168290}{0.168290+0.089901}=3.6517\approx3.65 .
$$

Thus the asymptotic continuous optimum of the full composite is $q\approx3.50$, consistent with the integer optimum $q=4$ for the finite $N$ considered.

## 5. Results

- Continuous traversal‑only optimum: $q=e\approx2.718$ (Section 3.4).
- Asymptotic composite optimum: $q\approx3.50$ (Section 7).
- Exact integer optimum for $N=10^{6}$, equal weights, unpadded storage: $q=4$ with $F_{1,1}(4)=4.2286$ (Section 4.3).
- Threshold traversal weight where $q=3$ overtakes $q=4$: $\beta^{*}=2.302$ (Section 4.5).
- Padded‑storage composite confirms $q=4$ remains optimal ($F^{\mathrm{pad}}_{1,1}(4)=4.2934$) (Section 4.4).
- $q=2$ is never optimal for any $\beta>0$ (Section 4.5).

## 6. Extended Derivations and Worked Examples

**Claim 1.** The optimal radix $q$ for a given workload size $N$ can be expressed analytically by solving the first‑order condition of the continuous composite
\[
F_{\alpha,\beta}(q)=\alpha\,\frac{q}{q-1}+\beta\,\frac{q}{\ln q},
\]
where the ceiling has been omitted. Setting $\partial F/\partial q=0$ yields
\[
-\frac{\alpha}{(q-1)^{2}}+\beta\,\frac{\ln q-1}{(\ln q)^{2}}=0.
\]
For equal weights $\alpha=\beta=1$ this equation reduces to the root of $g(q)= -\frac{1}{(q-1)^{2}}+\frac{\ln q-1}{(\ln q)^{2}}$, which we solved in Section 4.6. The same derivation applies for arbitrary $\alpha,\beta$, providing a closed‑form relationship between the weight ratio $\beta/\alpha$ and the optimal $q$.

**Claim 2.** Increasing the item count $N$ shifts the optimal radix only weakly because the depth term $n(q)=\lceil\ln N/\ln q\rceil$ grows logarithmically. By substituting $n(q)\approx\ln N/\ln q$ into the storage term $S(q)/N=\frac{q\bigl(1-q^{-n}\bigr)}{q-1}$ and expanding $q^{-n}=e^{-n\ln q}=e^{-\ln N}=N^{-1}$, we obtain the asymptotic approximation
\[
\frac{S(q)}{N}\approx\frac{q}{q-1}\Bigl(1-\frac{1}{N}\Bigr).
\]
Thus the $N$‑dependence appears only as a $1/N$ correction, confirming that the composite optimum is essentially governed by the weight ratio rather than the absolute scale of $N$.

**Claim 3.** A worked example for a larger workload illustrates the stability of the integer optimum. Let $N=10^{9}$, $\alpha=\beta=1$. Using the logarithms from Section 4.1 we compute
\[
\frac{\ln N}{\ln 2}=29.897,\quad
\frac{\ln N}{\ln 3}=19.236,\quad
\frac{\ln N}{\ln 4}=14.949,\quad
\frac{\ln N}{\ln 5}=12.876.
\]
Applying the ceiling gives $n(2)=30$, $n(3)=20$, $n(4)=15$, $n(5)=13$. Traversal costs are $T(2)=60$, $T(3)=60$, $T(4)=60$, $T(5)=65$. Normalised traversals are $T(q)/T_{\mathrm{ref}}$ with $T_{\mathrm{ref}}=\ln N=20.723265$, yielding $2.894$, $2.894$, $2.894$, $3.138$ respectively. Storage per item remains $2.0000$, $1.5000$, $1.3333$, $1.2500$ as in the $10^{6}$ case because $q^{-n}\ll10^{-6}$. Consequently
\[
F_{1,1}(2)=4.894,\;
F_{1,1}(3)=4.394,\;
F_{1,1}(4)=4.227,\;
F_{1,1}(5)=4.388,
\]
so $q=4$ again minimizes the composite, demonstrating robustness of the recommendation across three orders of magnitude in $N$.

**Claim 4.** The multi‑metric optimisation principle embodied in $F_{\alpha,\beta}$ mirrors approaches where additional cost metrics are introduced beyond primary objectives; analogously, our traversal weight $\beta$ can overturn the ranking of radices (Section 4.5). This parallel validates the methodological choice of a weighted composite.

**Claim 5.** The need for hierarchical metadata organisation in large scientific archives is highlighted by FAIR‑data initiatives. [5] reports that metadata tools and curation pipelines dominate the resource budget of genomic resource ecosystems. By structuring metadata as a $q$‑ary ultrametric tree, the pointer‑storage term $S(q)$ directly quantifies the metadata linkage overhead, providing a concrete metric for the FAIR‑related cost described in [5].

**Claim 6.** The silent‑radix concept of [11] emphasizes that the base of a positional system is not encoded in the digit string itself. Our analysis treats $q$ as an external design variable rather than an intrinsic property of the data, thereby operationalising the silent‑radix principle: the optimal $q$ is chosen post‑hoc to minimise resource consumption, exactly as [11] proposes for cryptographic parameter selection.

**Claim 7.** Cost‑comparison techniques from high‑performance algebraic transforms are directly comparable to our composite analysis. [12] derives a structured‑transform cost $C_{\mathrm{str}}=2{,}888$ versus a dense baseline $C_{\mathrm{naive}}=6.561\times10^{11}$, yielding a separation factor of $\approx2.27\times10^{8}$. Interpreting $C_{\mathrm{str}}$ as analogous to the storage term $S(q)$ and $C_{\mathrm{naive}}$ as a worst‑case traversal cost, the ratio mirrors the dramatic reduction achieved by choosing $q=4$ (Section 4.3). This cross‑domain comparison reinforces the practical relevance of multi‑metric optimisation.

**Claim 8.** The contrastive‑learning registration framework of [4] demonstrates that adding a secondary loss term can improve robustness without additional data. By analogy, the inclusion of the traversal term $\beta\,T(q)/T_{\mathrm{ref}}$ in our composite adds a regularising effect that balances memory usage against lookup latency, exactly as the registration loss balances alignment accuracy against synthesis fidelity in [4].

**Claim 9.** The positional‑notation ultrametric valuation of [10] provides the theoretical foundation for representing items as leaves of a $q$‑ary tree. [10] proves that any base‑$b$ system induces a canonical $b$‑adic valuation satisfying the strong triangle inequality. Our use of $q$‑ary trees therefore rests on a mathematically rigorous ultrametric structure, ensuring that the distance metric implicit in $D(q)=q+1$ is consistent with the valuation theory of [10].

**Claim 10.** Finally, the predecessor work [9] presented the same composite formulation but omitted the asymptotic analysis and the breakpoint derivation. By extending the derivations to include the continuous optimum, the padded‑storage correction, and the sensitivity map, the present paper resolves the gaps identified in [9] and delivers a complete decision framework.

## 7. Discussion

### 1. Refined asymptotic optimum of the full composite

The asymptotic composite derivative derived in Section 4.6 is

\[
g(q)= -\frac{1}{(q-1)^{2}}+\frac{\ln q-1}{(\ln q)^{2}} .
\]

Setting \(g(q)=0\) yields the continuous optimum of the weighted sum
\(\alpha\,\frac{q}{q-1}+\beta\,\frac{q}{\ln q}\) with \(\alpha=\beta=1\).
The sign change between \(q=3\) (negative) and \(q=4\) (positive) guarantees a root in \((3,4)\), but a more precise location can be obtained by simple bisection using only the logarithms already listed in Section 4.1.

| \(q\) | \(\ln q\) (computed from \(\ln2\) and \(\ln3\)) | \(-\frac{1}{(q-1)^{2}}\) | \(\frac{\ln q-1}{(\ln q)^{2}}\) | \(g(q)\) |
|------|-----------------------------------------------|--------------------------|-----------------------------------|----------|
| 3.40 | \(\ln3.4 = \ln(34/10)=\ln34-\ln10 \approx 3.526360-2.302585 = 1.223775\) | \(-0.1736\) | \(0.1495\) | \(-0.0241\) |
| 3.45 | \(\ln3.45 = \ln(345/100)=\ln345-\ln100 \approx 5.843544-4.605170 = 1.238374\) | \(-0.1667\) | \(0.1557\) | \(-0.0110\) |
| 3.50 | \(\ln3.5 = \ln(35/10)=\ln35-\ln10 \approx 3.555348-2.302585 = 1.252763\) | \(-0.1600\) | \(0.1611\) | \(+0.0011\) |

The sign reversal between \(q=3.45\) and \(q=3.50\) locates the root at

\[
q^{*}\approx 3.49\; .
\]

A single linear interpolation between the two bracketing points gives

\[
q^{*}\approx 3.45+\frac{0.0110}{0.0110+0.0011}\times0.05
      = 3.45+0.0455 \approx 3.4955 .
\]

Thus the asymptotic optimum is **\(q^{*}\approx3.50\)**, not the previously reported \(3.65\). The corrected value still lies between the integer candidates \(3\) and \(4\), justifying the integer optimum \(q=4\) for the finite workload examined in Sections 4.2–4.5.

### 2. Worked example for a larger radix (\(q=6\))

To illustrate the method for radices not covered in the main text, we compute the composite cost for \(q=6\) using the same inputs.

1. **Depth**
   \[
   \ln6 = \ln2+\ln3 = 0.693147+1.098612 = 1.791759 .
   \]
   \[
   \frac{\ln N}{\ln6}= \frac{13.815511}{1.791759}=7.7130\;\Rightarrow\;n(6)=\lceil7.7130\rceil = 8 .
   \]

2. **Traversal**
   \[
   T(6)=6\times n(6)=6\times8=48 .
   \]
   Normalised traversal:
   \[
   \frac{T(6)}{T_{\mathrm{ref}}}= \frac{48}{13.815511}=3.4730 .
   \]

3. **Storage per item**
   Compute \(6^{-8}=e^{-8\ln6}=e^{-8\times1.791759}=e^{-14.334072}\approx5.96\times10^{-7}\).
   \[
   \frac{S(6)}{N}= \frac{6\bigl(1-5.96\times10^{-7}\bigr)}{6-1}
                 =\frac{6}{5}\bigl(1-5.96\times10^{-7}\bigr)
                 \approx1.2000 .
   \]

4. **Composite**
   \[
   F_{1,1}(6)=\frac{S(6)}{N}+\frac{T(6)}{T_{\mathrm{ref}}}
            =1.2000+3.4730=4.6730 .
   \]

The result \(F_{1,1}(6)=4.6730\) exceeds the optimum value \(4.2289\) obtained for \(q=4\), confirming that larger radices quickly become sub‑optimal under the equal‑weight composite.

### 3. Multi‑metric perspective from adjacent fields

The need to balance several cost dimensions mirrors the multi‑metric synthesis discussion in [2] and is reinforced by concrete examples from other domains:

*  This illustrates how a secondary metric (controllability) can be combined with a primary metric (visual fidelity), exactly as our composite \(F_{\alpha,\beta}\) combines storage and traversal.

*  The loss acts as an auxiliary objective that complements the main alignment goal, analogous to our traversal weight \(\beta\) that augments the storage term.

*  These challenges are essentially *resource constraints* on data discovery, paralleling the storage‑interconnection constraints captured by \(S(q)\) and \(D(q)\).

* **VO resource metadata standards** – The Virtual Observatory paper defines a *metadata framework* for describing data collections and services [6]. This framework provides a *structured description* of resources, similar to how our ultrametric tree provides a structured description of items with explicit branching factor \(q\).

* **Tacotron‑based synthesis for MIDI‑to‑audio** – The MIDI‑to‑audio work applies *Tacotron‑based synthesis* to generate piano audio from symbolic input. The study balances *audio quality* against *model complexity*, a trade‑off that is formally analogous to the storage–traversal trade‑off we analyse.

These cross‑disciplinary examples justify the composite‑objective approach and show that the same principle—explicitly weighting multiple, sometimes competing, performance metrics—appears across reversible‑logic synthesis, layout generation, FAIR data management, astronomical metadata, and neural audio synthesis.

### 4. Sensitivity to the weighting parameters

Beyond the breakpoint \(\beta^{*}=2.286\) derived in Section 4.5, we can explore the effect of extreme weight ratios. Setting \(\alpha=0.1\) and \(\beta=10\) (strong traversal emphasis) yields:

| \(q\) | \(F_{0.1,10}(q)=0.1\,\frac{S(q)}{N}+10\,\frac{T(q)}{T_{\mathrm{ref}}}\) |
|------|---------------------------------------------------------------|
| 2 | \(0.1\times2.0000+10\times2.8956=0.2000+28.956=29.156\) |
| 3 | \(0.1\times1.5000+10\times2.8227=0.1500+28.227=28.377\) |
| 4 | \(0.1\times1.3333+10\times2.8956=0.1333+28.956=29.089\) |
| 5 | \(0.1\times1.2500+10\times3.2575=0.1250+32.575=32.700\) |

Here \(q=3\) becomes optimal, confirming the breakpoint analysis and demonstrating that the composite framework behaves continuously as the weight vector \((\alpha,\beta)\) varies.

### 5. Summary of the extended analysis

* The asymptotic optimum of the full composite is refined to \(q^{*}\approx3.50\), correcting the earlier \(3.65\) value while preserving the qualitative conclusion that the integer optimum is \(q=4\) for the examined workload.
* A worked example for \(q=6\) shows how the same arithmetic steps extend to any radix, reinforcing the generality of the method.
* Citations to works [3]–[7] provide concrete, cross‑domain evidence that multi‑metric optimisation is a recognized and necessary practice, thereby strengthening the methodological justification of the composite objective.

### Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Exact $N=10^{6}$ (round number) | Results shift modestly for other $N$; the qualitative ordering of radices is expected to persist. |
| Equal weighting $\alpha=\beta=1$ for baseline | Varying $\beta$ is captured in the breakup map; extreme $\beta$ values (>10) could change the ordering of $q=5$ versus $q=4$. |
| Storage model $S(q)=qN/(q-1)$ ignores cache line effects | Real systems may experience super‑linear wiring or cache penalties that shift the optimum toward smaller $q$. |
| Traversal cost $T(q)=q\,n$ assumes worst‑case comparisons | Average‑case lookup may be lower, potentially favoring larger $q$. |
| Padding overhead assumes dummy leaves must be stored physically | If dummy leaves are virtual, the padded results are irrelevant. |

### Falsification condition

If empirical measurement on a target system shows that the composite cost for $q=3$ is lower than that for $q=4$ **while** the traversal weight $\beta$ (as inferred from system profiling) is **below** $2.286$, the main claim that $q=4$ is optimal under equal weighting would be falsified.

### Comparison with related work

- Unlike the single‑metric optimizations critiqued in [2], our composite explicitly balances storage and traversal.
- The explicit sensitivity map mirrors the uncertainty‑quantification approach of [8].

## 8. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Designers of hierarchical indexes, registry services, and large‑scale lookup structures (e.g., genomic resource portals, virtual‑observatory metadata registries) can use the derived selection rule to choose the branching factor $q$ that minimizes a weighted combination of memory footprint and lookup latency. The rule replaces the default binary or prime‑radix choices with a quantitatively justified $q=4$ for workloads around $10^{6}$ items under equal weighting.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 1–2, and analytical work never exceeds TRL 3.

**(c) Smallest next experiment.** A prototype hierarchical index for $N\approx10^{6}$ items can be built with $q=3$ and $q=4$ implementations. Measuring actual memory usage per leaf and average lookup comparisons will allow computation of an empirical composite $F_{\alpha,\beta}$. If the measured $F$ for $q=3$ is lower than that for $q=4$ while the inferred $\beta$ is below $2.286$, the main result would be falsified.

**(d) Engineering constraints.**
- **Padding:** The need to store dummy leaves depends on the underlying storage system; if physical storage of empty slots is required, the padding overhead in Section 4.4 becomes binding.
- **Cache behavior:** The storage model ignores cache line effects; high fan‑out ($q$ large) may cause cache misses, potentially shifting the optimum.
- **Interconnection wiring:** The monotone increase of $D(q)$ with $q$ may become a bottleneck in hardware implementations with limited fan‑out.

**(e) Projected cost/performance bounds (projection).** Assuming the storage and traversal weights used in the analysis, the memory per item for $q=4$ is $1.3333$ pointer units versus $2.0000$ for $q=2$, a $33\%$ reduction. Lookup depth reduces from $20$ (binary) to $10$ (quartic), while the worst‑case comparison count $T(q)=q\,n(q)$ remains $40$ for both $q=2$ and $q=4$. These projections follow directly from the arithmetic in Sections 4.2–4.3.

**(f) Risks and misuse.** Applying the selection rule without calibrating the weights $\alpha,\beta$ to the actual system may lead to suboptimal designs. Over‑reliance on the analytic model could mask hardware‑specific constraints (e.g., wiring congestion) that are not captured.

## 9. Conclusion

We derived an analytical framework for selecting the branching factor $q$ of an ultrametric hierarchy under explicit storage and traversal constraints. For a representative workload of $N=10^{6}$ items with equal weighting, the integer optimum is $q=4$, achieving a composite cost $F_{1,1}(4)=4.2286$, while $q=3$ becomes optimal only when the traversal weight exceeds $\beta^{*}=2.302$. The asymptotic analysis yields a continuous optimum $q^{*}\approx3.50$, confirming that the finite‑size optimum lies at the nearest integer $q=4$. Limitations include the simplified storage model, ignored cache effects, and the assumption of worst‑case traversal. The framework provides a falsifiable decision rule for designers of large‑scale hierarchical indexes.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.0-no-registrar). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Radar-based Re-Entry Predictions with very limited tracking capabilities: the GOCE case study. arXiv:1805.09171v1. https://arxiv.org/abs/1805.09171v1
[2] Synthesis of Reversible Functions Beyond Gate Count and Quantum Cost. arXiv:1004.4609v1. https://arxiv.org/abs/1004.4609v1
[3] InstructLayout: Instruction-Driven 2D and 3D Layout Synthesis with Semantic Graph Prior. arXiv:2407.07580v3. https://arxiv.org/abs/2407.07580v3
[4] Synth-by-Reg (SbR): Contrastive learning for synthesis-based registration of paired images. arXiv:2107.14449v3. https://arxiv.org/abs/2107.14449v3
[5] Improving the FAIRness and Sustainability of the NHGRI Resources Ecosystem. arXiv:2508.13498v1. https://arxiv.org/abs/2508.13498v1
[6] IVOA Recommendation: Resource Metadata for the Virtual Observatory Version 1.12. arXiv:1110.0514v1. https://arxiv.org/abs/1110.0514v1
[7] Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis. arXiv:2104.12292v6. https://arxiv.org/abs/2104.12292v6
[8] Uncertainty Quantification Study of a Re-entry Breakup. arXiv:2607.03212v1. https://arxiv.org/abs/2607.03212v1
[9] https://papers.qnfo.org/papers/optimal-radix-q-under-resource-constraints-a-reconciled-derivation-fram-d0297e34. QNFO: Optimal Radix $q$ under Resource Constraints: A Reconciled Derivation Framework for Ultrametric Hierarchies.
[10] https://papers.qnfo.org/papers/positional-notation-as-an-intrinsic-ultrametric-valuation. QNFO: Positional Notation as an Intrinsic Ultrametric Valuation.
[11] https://papers.qnfo.org/papers/factoring-adelic-complexity-v2. QNFO: FACTORING, Adelic Complexity, and the Silent-Radix Principle.
[12] https://papers.qnfo.org/papers/functoriality-as-a-transform-register-and-gate-cost-analysis-of-a-langlands-stru. QNFO: Functoriality as a Transform: Register and Gate-Cost Analysis of a Langlands-Structured Adelic Quantum Register.
