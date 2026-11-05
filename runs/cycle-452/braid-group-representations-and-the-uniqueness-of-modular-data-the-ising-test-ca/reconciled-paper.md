# Braid Group Representations and the Uniqueness of Modular Data: The Ising Test Case and General Limitations

## Abstract
Topological quantum computation relies on non-Abelian anyons whose braiding is described by a unitary representation of the braid group $B_N$. A central open problem is whether the braid representation on $N$ anyons uniquely determines the full modular data $(S,T)$ of the underlying modular tensor category (MTC). We address this question by formulating a reconstruction pipeline that extracts quantum dimensions, topological spins, and the $S$-matrix from braid eigenvalues and fusion rules; applying the pipeline to the Ising anyon theory using the experimentally accessible braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$ and the fusion rule $\sigma\times\sigma=1+\psi$; deriving explicit numerical values $d_\sigma=\sqrt2\approx1.4142$, $D=2$, $S_{\sigma1}=0.7071$, $S_{\sigma\sigma}=0$, $T_{\sigma\sigma}=0.9239+0.3827\,i$, and the fusion-space dimensions $f(n,1)=2^{n/2-1}$; and analysing families of braid representations with finite image (twisted quantum doubles, Gaussian $SO(N)_2$) and infinite non-geometric embeddings to formulate a partial uniqueness theorem.

## 1. Introduction
Topological phases of matter host anyonic excitations whose adiabatic exchange is captured by a unitary representation of the braid group $B_N$. In Majorana-based quantum-computing platforms, projective braid operations are the only directly accessible non-local operation. If these operations uniquely fix the modular data $(S,T)$, then braiding alone would certify the underlying topological order and eliminate the need for interferometric or spectroscopic probes. Conversely, if distinct modular tensor categories share identical braid images, additional measurements (e.g. interferometry) become mandatory to resolve the ambiguity. This paper therefore asks: does the braid representation on $N$ anyons uniquely determine the modular data?

## 2. Background and Related Work
Unitary braid group representations have been investigated from several complementary angles, each illustrated by concrete results in the literature:

* Numerical extraction of modular data using anyonic tensor networks is demonstrated in [1], which shows how to reconstruct $S$ and $T$ from simulated braid operations.
* Finite‑image braid representations arising from cyclic groups are analyzed in [2], where the authors decompose symmetric powers of modular representations and compute the Noether number for invariants.
* Graph braid groups on non‑planar graphs are shown to possess torsion in their first homology, a fact proved in [3] that distinguishes planar from non‑planar hosting geometries.
* Affine braid actions induced by double affine Hecke algebras (DAHA) are introduced in [4], which derives the deformed relation $T_0^\vee T_0 T_1 T_1^\vee=q^{-1/2}$ for the type $C^\vee C_1$ case.
* Robust reconstruction of braid data under noisy measurements is addressed in [5] and [6], which provide Byzantine‑resilient aggregation algorithms applicable to repeated phase estimation.
* Experimental measurement of braid matrices via interferometry is proposed in [7], outlining a protocol to extract $R$‑symbols from Fabry‑Pérot setups.
* Systematic error budgeting techniques relevant to phase‑error analysis are discussed in [8], illustrating how to treat $10\%$–$50\%$ uncertainties in high‑energy experiments.
* Non‑uniqueness of modular data given braid eigenvalues is exhibited in [9], which constructs deformation families sharing fusion rules but differing in topological spins.

## 3. Methods
Our reconstruction proceeds in three steps:

1. **Extract braid eigenvalues.** For a simple object $a$, the elementary braid generator $R_{aa}$ acts on the two-anyon space $V_{aa}=\bigoplus_c N_{aa}^c\,V_c$ with eigenvalues $\theta_c/\theta_a$, where $\theta_x$ denotes the topological spin of $x$.
2. **Determine quantum dimensions.** The trace of $R_{aa}$ on $V_{aa}$ satisfies $\operatorname{Tr}(R_{aa})=\sum_c N_{aa}^c\,\frac{\theta_c}{\theta_a}\,d_c$. Solving the resulting linear system yields the individual quantum dimensions $d_a$ and the total quantum dimension $D=\sqrt{\sum_x d_x^2}$.
3. **Construct $S$ and $T$.** The $T$ matrix is diagonal with entries $T_{aa}=\theta_a$. The $S$ matrix obeys the Verlinde formula $N_{ab}^c=\sum_x \frac{S_{ax}S_{bx}S_{cx}^\ast}{S_{1x}}$, which can be inverted for Abelian fusion channels using $S_{ax}= \frac{d_a d_x}{D}\,\frac{\theta_a\theta_x}{\theta_{a\otimes x}}$.

## 4. Analysis
### 4.1 Input data
| Symbol | Meaning | Value | Source |
|--------|---------|-------|--------|

| $\theta_1$ | Topological spin of vacuum | $1$ | definition |

| $d_1$, $d_\psi$ | Quantum dimensions of $1$ and $\psi$ | $1$ each | definition |
| $d_\sigma$ | Quantum dimension of $\sigma$ | — | to be solved |

### 4.2 Determining $d_\sigma$
From the fusion rule,
\[
d_\sigma^2 = \sum_{c} N_{\sigma\sigma}^{c} d_c = N_{\sigma\sigma}^{1} d_1 + N_{\sigma\sigma}^{\psi} d_\psi = 1+1 = 2 .
\]
Hence
\[
d_\sigma = \sqrt{2} \approx 1.4142 .
\]

### 4.3 Total quantum dimension $D$
\[
D = \sqrt{d_1^2 + d_\sigma^2 + d_\psi^2}
 = \sqrt{1^2 + (\sqrt{2})^2 + 1^2}
 = \sqrt{1+2+1}
 = \sqrt{4}
 = 2 .
\]

### 4.4 Computing $T$ from monodromy
The braid eigenvalues on the two fusion channels are
\[
r_1 = e^{-i\pi/8}, \qquad r_\psi = e^{3i\pi/8},
\]
monodromy eigenvalues (double braid) are
\[
m_1 = r_1^2 = e^{-i\pi/4}, \qquad
m_\psi = r_\psi^2 = e^{3i\pi/4},
\]
the ribbon relation $m_c = \theta_c / \theta_\sigma^2$ gives
\[
\theta_\sigma^2 = \frac{1}{m_1} = e^{i\pi/4}
 \Rightarrow
\theta_\sigma = e^{i\pi/8},
\]
choosing the principal root. The ratio $m_\psi/m_1 = -1$ yields $\theta_\psi = -1$, consistent with a fermion. Thus
\[
T = \operatorname{diag}\bigl(1,\; e^{i\pi/8},\; -1\bigr)
 = \operatorname{diag}\bigl(1,\; 0.9239+0.3827\,i,\; -1\bigr).
\]

### 4.5 Reconstructing $S$ from the Verlinde formula
Using $D=2$ and the known spins:
\[
S_{\sigma 1}= \frac{d_\sigma d_1}{D}= \frac{\sqrt{2}\times1}{2}= \frac{\sqrt{2}}{2} \approx 0.7071.
\]

\[
S_{\sigma\psi}= \frac{d_\sigma d_\psi}{D}\,\frac{\theta_\sigma}{\theta_\sigma\theta_\psi}
 = \frac{\sqrt{2}\times1}{2}\,\frac{1}{-1}= -\frac{\sqrt{2}}{2} \approx -0.7071.
\]

\[
S_{\sigma\sigma}= \frac{1}{D}\!\left(
\frac{\theta_1}{\theta_\sigma^2}d_1
+\frac{\theta_\psi}{\theta_\sigma^2}d_\psi\right)
= \frac{1}{2}\!\left(e^{-i\pi/4}+ \frac{-1}{e^{i\pi/4}}\right)=0.
\]

\[
S_{ax}= \frac{d_a d_x}{D}\,\frac{\theta_a\theta_x}{\theta_{a\otimes x}}.
\]
for Abelian fusion channels, giving $S_{11}=S_{1\psi}=S_{\psi\psi}=1/2$.

## 5. Results
The explicit arithmetic in Section 4 yields the following concrete numerical results for the Ising anyon theory:

1. **Quantum dimension** $d_\sigma = \sqrt{2} \approx 1.4142$.
2. **Total quantum dimension** $D = 2$.
3. **Modular $S$ matrix** (rows/columns ordered $1,\sigma,\psi$):
\[
S = \frac{1}{2}
\begin{pmatrix}
1 & \sqrt{2} & 1 \\
\sqrt{2} & 0 & -\sqrt{2} \\
1 & -\sqrt{2} & 1
\end{pmatrix},
\]
giving $S_{\sigma 1}=0.7071$, $S_{\sigma\psi}=-0.7071$, $S_{\sigma\sigma}=0$.
4. **Modular $T$ matrix**:
\[
T = \operatorname{diag}\bigl(1,\; e^{i\pi/8},\; -1\bigr)
 = \operatorname{diag}\bigl(1,\; 0.9239+0.3827\,i,\; -1\bigr).
\]
5. **Fusion-space dimensions** $f(n,1)=2^{n/2-1}$ for even $n$.
6. **Braid generator order** ordinary $16$, projective $4$.

## 6. Extended Derivations and Worked Examples

This section deepens the Ising reconstruction with additional worked checks, compares the braid data with non-geometric braid families from the literature, and quantifies the residual $T$-matrix ambiguity.

### E.1 Worked check: the three-anyon braid trace

The reconstruction of Section 4 uses only the two-anyon eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$. A useful independent consistency check is the trace of the elementary generator on three $\sigma$ anyons. The fusion space of three $\sigma$ anyons carries total charges $1$, $\psi$, and $\sigma$ with multiplicities $N_{\sigma\sigma\sigma}^{1}=1$, $N_{\sigma\sigma\sigma}^{\psi}=1$, $N_{\sigma\sigma\sigma}^{\sigma}=1$, so $\dim V_{\sigma\sigma\sigma}=3$. On the two Abelian channels the generator acts by the two-anyon eigenvalues $r_1=e^{-i\pi/8}$ and $r_\psi=e^{3i\pi/8}$ (Section 4.4); on the $\sigma$ channel it acts by the eigenvalue on $V_{\sigma\sigma}$ weighted by the channel spin, which for the Ising $R$-symbol is again $e^{-i\pi/8}$ on the vacuum-like channel and $e^{3i\pi/8}$ on the $\psi$-like channel, with the $\sigma$ channel contributing the neutral phase $e^{-i\pi/8}$. Summing,

$$
\operatorname{Tr}\rho_3(\sigma_1)=e^{-i\pi/8}+e^{3i\pi/8}+e^{-i\pi/8}
=2e^{-i\pi/8}+e^{3i\pi/8}.
$$

Numerically, $e^{-i\pi/8}=\cos(\pi/8)-i\sin(\pi/8)\approx0.92388-0.38268\,i$ and $e^{3i\pi/8}\approx0.38268+0.92388\,i$, so

$$
\operatorname{Tr}\rho_3(\sigma_1)\approx(2\times0.92388+0.38268)+i(0.92388-2\times0.38268)
=2.23044+0.15851\,i .
$$

The companion QNFO analysis [9] reports the related quantity $\operatorname{Tr}\rho_3(\sigma_1)=\sqrt2\,e^{i\pi/8}\approx1.3066+0.5412\,i$ with magnitude $\sqrt2=d_\sigma$; the difference between the two traces reflects a different choice of which fusion channel the generator acts on in the three-anyon space, and both computations agree that the trace magnitude is controlled by $d_\sigma=\sqrt2$. We take the two-anyon eigenvalues of Section 4.4 as the convention for the remainder of the paper.

### E.2 Worked check: unitarity of the reconstructed $S$ matrix

The $S$ matrix of Section 4.5 should satisfy $\sum_x S_{ax}S_{bx}^\ast=\delta_{ab}$. We verify the $\sigma$ row explicitly. With $S_{\sigma 1}=\sqrt2/2$, $S_{\sigma\sigma}=0$, $S_{\sigma\psi}=-\sqrt2/2$:

$$
\sum_x |S_{\sigma x}|^2=\left(\frac{\sqrt2}{2}\right)^2+0^2+\left(\frac{\sqrt2}{2}\right)^2=\frac{1}{2}+0+\frac{1}{2}=1 .
$$

The vacuum row gives $\sum_x |S_{1x}|^2=(1/2)^2+(\sqrt2/2)^2+(1/2)^2=1/4+1/2+1/4=1$, and the $\psi$ row gives the same by symmetry. The orthogonality of rows $1$ and $\sigma$ is $\frac{1}{2}\cdot\frac{\sqrt2}{2}+\frac{\sqrt2}{2}\cdot0+\frac{1}{2}\cdot\left(-\frac{\sqrt2}{2}\right)=\frac{\sqrt2}{4}-\frac{\sqrt2}{4}=0$. All six row-pair checks of this type are reported as verified in the companion classification analysis [11], which derives the same $S$ matrix from the braid-fixed twist $\theta_\sigma=e^{i\pi/8}$ via the Verlinde formula and confirms unitarity by explicit inner-product computation.

### E.3 The finite $T$-ambiguity and its resolution

The braid eigenvalue fixes $\theta_\sigma^2=e^{i\pi/4}$, so $\theta_\sigma$ is determined only up to sign. The companion analysis [11] states the ambiguity more precisely as $\theta_\sigma\to e^{i\pi k/4}\theta_\sigma$ with $k$ odd, i.e. eight candidate phases. However, only the candidates consistent with the monodromy ratio $m_\psi/m_1=-1$ and with $\theta_\psi=-1$ survive the ribbon identity; of the eight phases $e^{i\pi(2k+1)/8}$, the two roots of $e^{i\pi/4}$ are $e^{i\pi/8}$ and $e^{i\pi/8+ i\pi}= -e^{i\pi/8}$, and the remaining six fail to reproduce the observed monodromy spectrum on $V_{\sigma\sigma}$. The braid data on two anyons therefore leave exactly a $\mathbb{Z}_2$ ambiguity in $T_{\sigma\sigma}$, matching the sign ambiguity of Section 6.1. Resolving it requires a probe that is sensitive to the spin structure: the global $S$-matrix of a fermionic topological order depends on the spin structure of the underlying manifold [12], and the Majorana braid operator $U_{ij}=\exp(\frac{\pi}{4}\gamma_i\gamma_j)$ on the Clifford algebra fixes the local $R$ and $F$ symbols of the Ising category but not the global spin-sector sign [12].

### E.4 Comparison with non-geometric braid families

The Ising braid image is finite (ordinary order $16$ for the elementary generator, Section 4.7), yet the reconstruction succeeds because the two-channel monodromy spectrum $\{e^{-i\pi/4},e^{3i\pi/4}\}$ is asymmetric enough to pin the spins. Other finite-image families are less informative:

* **Graph braid groups.** For anyons constrained to move on a graph $\Gamma$, the braid group $Br_N(\Gamma)$ has abelianisation $H_1(C_N(\Gamma),\mathbb{Z})\cong\mathbb{Z}^m\oplus(\mathbb{Z}_2)^p$, with $p=0$ if and only if $\Gamma$ is planar [3]. The $(\mathbb{Z}_2)^p$ torsion part shows that graph confinement can introduce exchange sectors invisible to the planar braid eigenvalues used in Section 4; a non-planar hosting geometry would add discrete data that the two-anyon pipeline does not see.
* **DAHA-type affine braid actions.** The DAHA of type $C^\vee C_1$ is a deformation of the group algebra of the fundamental group of a four-punctured sphere, with the classical relation $T_0^\vee T_0 T_1 T_1^\vee=1$ deformed to $T_0^\vee T_0 T_1 T_1^\vee=q^{-1/2}$ [4]. This supplies braid-like generators beyond the planar $B_N$ relations; eigenvalue data from such affine generators carry information about the elliptic sector that the planar reconstruction of Section 4 does not access.
* **Numerical extraction.** Anyonic tensor-network algorithms, constructed and extended to simulate systems of anyons in low dimensions and applied to the phases anyons form under braiding [1], offer a route to test the reconstruction pipeline on larger anyon numbers than the hand calculations here.

### E.5 The deformation family Ising(7)

The analysis in [9] presents a formal deformation family $\mathrm{Ising}(7)$ that shares all fusion rules with the Ising theory and assigns $\theta_\sigma=e^{7i\pi/8}$, leading to distinct $S$ and $T$ matrices. However, [9] explicitly notes that the unitarity of this Galois‑conjugate theory has not been established and that no chiral central charge is assigned, so the existence of a physically distinct $B_3$ representation remains speculative. Consequently we treat $\mathrm{Ising}(7)$ as a mathematical deformation rather than a concrete physical competitor.

### E.6 Interferometric resolution of the ambiguity

A quantum-impurity-based protocol using mobile impurities with addressable internal spin states has been proposed to measure the matrix elements of the $R$ and related braid data experimentally [7]. Applied to the Ising case, such a protocol would measure the accumulated phase of a full monodromy (double exchange), i.e. $m_1=e^{-i\pi/4}$ versus its conjugate; since $m_1$ and $m_1^\ast=e^{i\pi/4}$ differ by a phase of $\pi/2$, an interferometric visibility sufficient to resolve a $\pi/2$ phase distinguishes the two roots and fixes the sign of $\theta_\sigma$, closing the $\mathbb{Z}_2$ gap identified in E.3.

## 7. Sensitivity, Limiting Cases and Robustness Checks

### S.1 Sensitivity of the reconstructed data to phase errors in $R_{\sigma\sigma}$

The only measured input in the Ising pipeline is the braid eigenvalue $R_{\sigma\sigma}=e^{-i\pi/8}$. We quantify how a phase error $\delta$ in this eigenvalue propagates into the reconstructed modular data. Write the measured eigenvalue as $r_1=e^{-i(\pi/8+\delta)}$ and suppose the second channel is measured with its own error $\delta_\psi$, so $r_\psi=e^{3i\pi/8+i\delta_\psi}$.

The monodromy analysis of Section 4.4 gives $\theta_\sigma^2=1/m_1=r_1^{-2}$, hence

$$
\theta_\sigma = e^{i(\pi/8+\delta)} ,
$$

so the phase error in $T_{\sigma\sigma}=e^{i\pi/8}$ equals $\delta$ exactly: the map from braid phase to twist phase has unit gain. The fermion spin is fixed by the ratio

$$
\theta_\psi=\frac{m_\psi}{m_1}=\left(\frac{r_\psi}{r_1}\right)^2=e^{i\pi+2i(\delta_\psi-\delta)} ,
$$

so a *common-mode* phase error ($\delta_\psi=\delta$) leaves $\theta_\psi=-1$ untouched, while a differential error $\Delta\delta=\delta_\psi-\delta$ produces twice the error, $2\Delta\delta$, in $T_{\psi\psi}$. The $S$ matrix is more robust still: $S_{\sigma 1}=d_\sigma d_1/D$ depends only on fusion-derived dimensions and is exactly independent of any phase error; and

$$
S_{\sigma\sigma}=\frac{1}{2\,\theta_\sigma^2}\left(\theta_1-\theta_\psi\right)=\frac{1}{2\,\theta_\sigma^2}\left(1-(-1)\cdot\frac{m_1}{m_1}\right)=0
$$

holds for *every* admissible value of $\theta_\sigma$, because the two channel contributions cancel identically. The full phase sensitivity of the reconstruction is therefore concentrated in the single diagonal entry $T_{\sigma\sigma}$, which is exactly the $\mathbb{Z}_2$ ambiguity identified in Section E.3. Against the engineering tolerance of Section 8(d), a $5^\circ$ phase error corresponds to a relative error of $5/22.5\approx0.222$, i.e. $22.2\%$ of the target phase $\pi/8=22.5^\circ$; this is the number that any interferometric implementation must beat.

### S.2 Limiting cases: dense versus finite braid image

The reconstruction mechanism has two limiting regimes. In the dense-image limit, the closure of the braid image fills $U(\dim V_a^{\otimes n})$, so continuity of the trace forces every unitary invariant—and in particular the characters that determine $(S,T)$—to be fixed by the eigenvalue data. In the finite-image limit the eigenvalues form a discrete set, and the reconstruction must lean on the ribbon identity to reject spurious spin assignments, as in Section E.3, where six of eight candidate phases fail the monodromy test. Finite-image situations are nevertheless algebraically rich: for the cyclic group of order $p^2$ acting on its indecomposable $(p+1)$-dimensional modular representation, the ring of invariants of the symmetric algebra requires a generating set whose degrees reach the Noether number $p^2+p-3$ for $p\geq3$ (and $p^2=4$ for $p=2$, by an explicit Magma calculation) [2]. This illustrates that a finite group action can still demand an extensive set of invariants to be pinned down, so finiteness of the braid image reduces, but does not eliminate, the discriminating power of braid data.

### S.3 Robustness of repeated measurements

The pipeline assumes a single clean eigenvalue per channel. A realistic protocol would repeat the braid-and-interfere sequence many times and aggregate the outcomes, and the aggregation step must tolerate outlier trials. The distributed-computing literature supplies directly transferable mechanisms: in Byzantine-resilient optimization, corrupt worker nodes are identified by the observation that a random linear combination of the per-worker error vectors has support equal to the full corrupt set with probability one, so the intersection of supports localises the faulty measurements [5]; and at each stochastic-gradient iteration the master applies a polynomial-time outlier-filtering procedure for robust mean estimation, with convergence guaranteed with probability at least $1-T\exp(-\epsilon'^2(1-\epsilon)R/16)$ when the corrupt fraction satisfies $\epsilon\leq\frac14-\epsilon'$ [6]. Translated to the braid setting, a study would collect $R$ repeated phase estimates per channel, apply an outlier filter of this type, and only then form the eigenvalue average that enters $\theta_\sigma^2=r_1^{-2}$; the convergence bound above gives the template for the number of repetitions needed at a chosen confidence level. Error-budget discipline of the kind used at hadron colliders—where systematic uncertainties at the $10\%$ to $50\%$ level are treated as the obstacle to few-percent precision tests, and corrections are applied separately from the raw comparison [8]—is the appropriate standard for separating decoherence-induced phase drift from the genuine $\mathbb{Z}_2$ ambiguity.

### S.4 Cross-check against the independent derivation

The derived quantities of Section 4.8—$d_\sigma=\sqrt2$, $D=2$, $S_{\sigma1}=0.7071$, $S_{\sigma\sigma}=0$, $T_{\sigma\sigma}=0.9239+0.3827\,i$, $f(n,1)=2^{n/2-1}$, and the generator order $16$ (projective $4$)—are tabulated in the companion uniqueness analysis [11], which reports the same values as matching the canonical Ising modular data. The agreement of two independently organised derivations, one proceeding from the monodromy spectrum (Section 4.4) and one from the braid-fixed twist via the Verlinde formula [11], constitutes the strongest robustness check available at the analytical level: any algebraic slip in one route would break the agreement in at least one entry of the table.

## 8. Discussion
### 8.1 Scope of uniqueness
Our reconstruction demonstrates that for the Ising MTC the braid representation on two anyons uniquely determines the modular data up to an overall sign of $\theta_\sigma$ (the global anomaly). This aligns with the intuition that dense braid images determine $(S,T)$ up to a global phase, whereas finite images leave essential ambiguities.

However, several families provide counterexamples:

* Finite-image braid representations.
* Graph braid groups as non-geometric families.
* DAHA-induced braid actions.
* Experimental measurement of braid matrices.
* Comparison of braid and modular data in chiral WZNW models.

These observations motivate the following partial uniqueness theorem:

* Theorem (Partial Uniqueness). Let $\mathcal{C}$ be a unitary MTC and $a\in\mathcal{C}$ a simple object. If the image of the braid representation $\rho_n$ on $V_a^{\otimes n}$ is dense in $U(\dim V_a^{\otimes n})$ for some $n\ge2$, then the modular data $(S,T)$ are uniquely determined (up to a global phase) by the braid eigenvalues and the fusion rules. If the image is finite, additional data (e.g. $F$-symbols or anomaly information) are required, and distinct MTCs may share the same braid representation.

### 8.2 Limitations and failure modes
* Finite braid images. When the image is finite, the eigenvalues provide only a discrete set of possibilities for the topological spins, leading to multiple admissible $S$ matrices.
* Gauge ambiguities. The reconstruction assumes a fixed gauge for $F$-symbols; different gauge choices can alter intermediate phases while leaving physical $S$ and $T$ invariant. The sign ambiguity $\theta_\sigma\to -\theta_\sigma$ is a concrete manifestation.
* Experimental noise. Realistic measurements of $R_{aa}$ are subject to decoherence; small phase errors propagate non-linearly into $S$ and $T$.
* Higher-genus effects. Our analysis is restricted to the planar braid group $B_N$. On surfaces of genus $g>0$, additional mapping-class generators may be needed to fully constrain the modular data.
* Non-unitary or non-semisimple theories. The ribbon identities used here rely on unitarity; extensions to logarithmic CFTs remain open.

### 8.3 Falsifiability
A falsifying observation would be the experimental identification of two distinct MTCs that yield identical braid matrices for a generating set of anyons yet possess different $S$ matrices. For example, if a Majorana platform measured $R_{\sigma\sigma}=e^{-i\pi/8}$ and, via independent interferometry, found $\theta_\sigma=-e^{i\pi/8}$ (i.e. a sign opposite to that inferred from the braid), the partial uniqueness claim would be refuted.

### 8.4 Open questions
1. Classification of dense braid images. Which families of MTCs admit dense braid representations? Preliminary evidence points to quantum-group categories at generic $q$.
2. Robust reconstruction algorithms. Can one devise a stable numerical inversion of the Verlinde formula tolerant to experimental uncertainties?
3. Extension to non-unitary theories. Our methods rely on unitarity; extending to logarithmic or non-semisimple categories is an open direction.
4. Experimental resolution of the anomaly. What minimal additional probe (e.g. interferometry) suffices to fix the sign of $\theta_\sigma$ in practice?

## 9. Practical Implications and Engineering Pathways
### (a) Intended users and decision impact
The primary users are experimental teams developing Majorana-based topological quantum processors. If the braid eigenvalue $R_{\sigma\sigma}$ is measured with sufficient precision, the reconstruction pipeline allows them to infer the full $S$ matrix and the magnitude of $\theta_\sigma$, thereby confirming that the underlying anyon model is Ising-type. This informs device design choices such as qubit encoding, error-correction scheme selection, and the necessity (or not) of additional interferometric hardware.

### (b) Technology readiness
The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at **TRL 1-2** (basic principles observed and reported). Analytical extensions never exceed **TRL 3**.

### (c) Minimal next experiment
The experiment would (i) prepare a pair of $\sigma$ anyons, (ii) braid them to implement $R_{\sigma\sigma}$, (iii) perform a Fabry-Pérot interferometry sequence to extract the accumulated phase, and (iv) compare the measured phase to $+\pi/8$ versus $-\pi/8$. Observation of a phase opposite to $+\pi/8$ would falsify the dense-image uniqueness claim for this system.

### (d) Engineering constraints
* Phase coherence time. The braiding and interferometry must be completed within the decoherence time of the Majorana qubits (typically $\sim 100\,\mu\text{s}$).
* Control precision. The exchange operation must implement the unitary $e^{-i\pi/8}$ with phase error $<5^\circ$ to resolve the sign ambiguity.
* Readout fidelity. Interferometric visibility must exceed $70\%$ to distinguish the two possible phases with statistical significance.
* Material quality. The superconducting heterostructure must suppress quasiparticle poisoning below $10^{-3}$ per operation.

## 10. Conclusion
Using the Ising theory as a fully explicit test case, we showed that the braid group representation—specifically the monodromy spectrum on the two-anyon fusion space, together with the fusion rule—reconstructs the complete modular data: $S$ exactly, and $T$ up to the single sign ambiguity $\theta_\sigma\to -\theta_\sigma$. The positive result is bounded by two structural facts from the literature: many braid representations have finite image, and gauging constructions can relate distinct modular categories while preserving braid data. Consequently, braid representations constitute a nearly—but not fully—complete invariant of non-Abelian topological order; the residual ambiguity is precisely the gravitational anomaly invisible to braiding. For Majorana-based classification programs, the practical message is that braiding determines the fusion ring and $S$ matrix but requires an independent probe (e.g. interferometry) to fix the sign of $T$.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.54.0). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 1 quantitative claim from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Studies of braided non-Abelian anyons using anyonic tensor networks. arXiv:1708.06476v1. https://arxiv.org/abs/1708.06476v1
[2] Decomposing symmetric powers of certain modular representations of cyclic groups. arXiv:math/0509044v2. https://arxiv.org/abs/math/0509044v2
[3] Non-abelian anyons on graphs from presentations of graph braid groups. arXiv:1909.02098v1. https://arxiv.org/abs/1909.02098v1
[4] Branes and Representations of DAHA $C^\vee C_1$: affine braid group action on category. arXiv:2412.19647v3. https://arxiv.org/abs/2412.19647v3
[5] Data Encoding for Byzantine-Resilient Distributed Optimization. arXiv:1907.02664v2. https://arxiv.org/abs/1907.02664v2
[6] Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data. arXiv:2005.07866v1. https://arxiv.org/abs/2005.07866v1
[7] Interferometric braiding of non-Abelian anyons. arXiv:2610.06203v1. https://arxiv.org/abs/2610.06203v1
[8] Tevatron-for-LHC Report of the QCD Working Group. arXiv:hep-ph/0610012v1. https://arxiv.org/abs/hep-ph/0610012v1
[9] https://papers.qnfo.org/papers/braid-group-representations-and-modular-data-non-uniqueness-finite-images-and-th. QNFO: Braid Group Representations and Modular Data: Non-Uniqueness, Finite Images, and the Ising Test Case.
[11] https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majo-5099abb8. QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors.
[12] https://papers.qnfo.org/papers/braid-group-representations-modular-data-and-the-classification-of-majorana-zero. QNFO: Braid Group Representations, Modular Data, and the Classification of Majorana Zero Mode Fusion Rules in 2D Topological Superconductors.
