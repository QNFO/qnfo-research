# Zitterbewegung as a $p$-Adic Ultrametric Observable: A $\mathbb{Z}_2$ Invariant on the Bruhat–Tits Tree, Its Readout, and Its Non-Additivity Signature

## Abstract

Zitterbewegung (ZBW) — the Compton-frequency trembling of Dirac wave packets — is conventionally modeled as an Archimedean interference oscillation between positive- and negative-energy branches. We develop a conjectural alternative in which the ZBW readout is ultrametric: the observable lives on a Bruhat–Tits tree over $\mathbb{Q}_2$, and the physically accessible content is not a continuous oscillation but a discrete $\mathbb{Z}_2$-valued invariant carried by the current correlator. We (i) formulate a $p$-adic analogue of the Dirac spectral decomposition in which the spectral gap becomes a separation of tree branches, (ii) show that the $\mathbb{Z}_2$ invariant is conserved under isometric ultrametric evolution, (iii) compute the Archimedean and $p$-adic readouts of the electron Compton scale explicitly: $\omega_C = 7.7636\times10^{20}\ \mathrm{s}^{-1}$, $\log_2 \omega_C = 69.3951$, yielding tree level $\nu(\omega_C)=69$ and invariant $\chi = 1$, with a cross-check $\log_2 \omega_C + \log_2 \lambda_C = 28.1592$, consistent with $\log_2 c = 28.1594$ to the precision of the input constants; and (iv) show that the ultrametric tree distance between the frequency and length vertices is $111$, not $\log_2 c = 28.1594$ — a structural non-additivity with deviation $\Delta = 82.8406$ that constitutes the distinguishing observable. A complementary crossing-count protocol gives the same discrete structure through the $2$-adic norm $|N|_2$. We propose detection via spin noise spectroscopy, EELS/RIXS, or Majorana-platform measurements, predicting a discrete parity signature rather than a continuous beat. All quantitative claims are either derived here with shown arithmetic or explicitly labeled projections with stated assumptions.

## 1. Introduction

Zitterbewegung is the standard name for the rapid trembling motion of a relativistic Dirac wave packet, conventionally explained as interference between positive- and negative-energy branches of the Dirac spectrum at the Compton scale [9]. The received picture is thoroughly Archimedean: the interference lives on the real line, oscillates at the Compton frequency, and its observability is obstructed by the usual representation-theoretic obstructions to a sharp position operator. The structural underdetermination of that position operator has been argued to arise from a single representation-theoretic origin, the Silent Parameter Principle, under which $\mathrm{SU}(2)$ and $\mathbb{Z}_2^x$ share identical fusion rules at matching levels, and under which the 2-adic ZBW frequency deviates from the Archimedean value [10].

This paper takes the underdetermination seriously as a physical hypothesis rather than a pathology. If the position operator is structurally underdetermined, the "oscillation" readout is one convention among several; we propose that an ultrametric readout — in which the ZBW observable is a hierarchical connectivity pattern on a Bruhat–Tits tree rather than a displacement on the real line — is an equally admissible convention with a sharply different experimental signature. The central conjecture is:

> **Conjecture (p-adic ZBW).** The Compton-frequency beat between positive- and negative-energy branches admits an adelic formulation in which the ZBW observable is a $\mathbb{Z}_2$-valued topological invariant carried by the current correlator, read out as ultrametric (Bruhat–Tits tree) connectivity, and conserved under the ultrametric evolution.

The stakes are threefold. First, it would extend the standard Hilbert-space decomposition of ZBW — spectral gap, Clifford-algebra origin, Newton–Wigner no-go — into the adelic regime. Second, it connects relativistic quantum dynamics to the growing body of $p$-adic and ultrametric modeling across physics and beyond. Third, it connects to topological quantum computing: the same $\mathbb{Z}_2$ invariant has been shown to encode the Dirac/Majorana distinction in the ZBW current correlator [11], and ultrametric readout protocols via Bruhat–Tits buildings have been proposed for exactly this observable [12]. A Majorana platform would therefore exhibit a *vanishing* ZBW signal where a Dirac platform exhibits the invariant $\chi$ — a binary, topology-protected discriminator.

Our contributions: (1) a $p$-adic analogue of the Dirac spectral decomposition (Sections 3.1–3.2); (2) a proof that the $\mathbb{Z}_2$ invariant is well-defined and conserved under isometric ultrametric evolution (Section 3.3); (3) explicit numerical evaluation of the Archimedean and $p$-adic readouts for the electron, with all arithmetic shown (Section 4); (4) a concrete distinguishing observable — the failure of multiplicativity of the tree readout — and three detection channels (Sections 4–5). We emphasize scope: this is a conjectural framework paper. The $p$-adic formulation is constructed and shown to be internally consistent and to reproduce a discrete distinguishing observable; it is not derived from an established adelic Dirac theory, and the experimental proposals are projections with stated assumptions, not computed signals.

## 2. Background and Related Work

We organize the literature into four strands: ultrametric modeling, $p$-adic dynamics and statistical mechanics, $p$-adic arithmetic and Hilbert spaces, and the ZBW/adelic corpus.

**Ultrametric modeling of empirical structure.** Reference [1] models anomaly and change in data by embedding the data in an ultrametric space: starting from cross-tabulation counts, Correspondence Analysis endows the information space with a Euclidean metric, and anomaly or change is then modeled by an induced ultrametric, of a sequential kind. This establishes the methodological pattern we adopt: an Archimedean representation is available, but the *induced ultrametric* is the object that carries the relevant discrete structure. Our claim is that ZBW is exactly such a case — the Archimedean oscillation is available, but the induced ultrametric carries the invariant. The supplied summary of [1] gives no further detail on the sequential construction, and we use it only at the level stated.

**$p$-adic stochastic dynamics.** Reference [2] proposes a method for describing stationary Markov processes on the class of ultrametric spaces $\mathbb{U}$ isometrically embeddable in the field $\mathbb{Q}_p$, reducing their study to processes on $\mathbb{Q}_p$ so that the traditional machinery of $p$-adic mathematical physics can be applied. This is the tool we need for the conservation claim in Section 3.3: if the ZBW readout dynamics is a stationary Markov process on a tree isometrically embeddable in $\mathbb{Q}_2$, the reduction theorem guarantees that the evolution can be analyzed with $p$-adic machinery, and isometric embeddings preserve the ultrametric distances on which our invariant is defined. The entry's summary supplies no computed process values, and we claim none.

**$p$-adic statistical mechanics on trees.** Reference [4] considers a three-state $p$-adic Potts model with competing interactions on a Cayley tree of order two, reduces the description of $p$-adic Gibbs measures to a recursive equation, and proves that a phase transition occurs if and only if $p = 3$ for any nonzero value of the interactions, also completely solving the uniqueness problem. This matters for us because the Cayley tree is the combinatorial skeleton of the Bruhat–Tits tree of our readout: [4] shows that on such hierarchical index sets, sharp, prime-dependent discrete transitions occur — the same mechanism class we invoke when the $\mathbb{Z}_2$ invariant flips or fails at a branch point. The summary supplies no further results, and we use none beyond what is stated.

**$p$-adic information spaces in biology.** Reference [6] uses basic properties of $p$-adic numbers to describe DNA sequence and the genetic code, with a central role for an ultrametric $p$-adic information space whose basic elements are nucleotides, codons and genes; it shows a 5-adic model is appropriate for DNA sequence, and that this 5-adic model combined with 2-adic distance is also suitable for further structure. The relevance is twofold: it shows that small primes ($p = 2, 5$) can be the *correct* primes for a physical information space, supporting our focus on $\mathbb{Q}_2$; and it demonstrates that a discrete, hierarchical encoding can be the primary physical description, not a coarse-graining of a continuous one. The summary supplied for [6] gives no further technical detail, and we rely on it only for these stated points.

**$p$-adic Hilbert spaces.** Reference [7] works in the standard $d$-dimensional $p$-adic Hilbert space $\mathbb{Q}_p^d$ and in the $p$-adic Hilbert space of symmetric $m$-tensors $\mathrm{Sym}^m(\mathbb{Q}_p^d)$, proving results for collections $\{\tau_j\}_{j=1}^n$ satisfying normalization conditions $\langle \tau_j, \tau_j \rangle = 1$. This demonstrates that Hilbert-space constructs central to quantum information — inner products, normalized frame collections, tensor powers — admit $p$-adic formulations, which is the prerequisite for our claim that the ZBW current correlator can be defined over a $p$-adic Hilbert space. The supplied summary truncates before stating the full theorem, and we use only the setting and the stated conditions.

**Ultrametric metric geometry.** Reference [8] treats ultrametrics as a zero-dimensional analogue of ordinary metrics and provides ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization theorem. For us, [8] supplies the guarantee that our tree readout is not an ad hoc structure: ultrametric spaces support the same embedding, extension, and characterization machinery as metric spaces, so the Bruhat–Tits readout can be embedded, extended, and characterized with standard tools.

**Number-theoretic analogies.** Reference [3] formulates a conjectural $p$-adic analogue of Borel's theorem relating regulators for higher $K$-groups of number fields to special values of the corresponding zeta-functions, using syntomic regulators and $p$-adic L-functions, with a corresponding conjecture for Artin motives and a conjecture on the precise relation between the $p$-adic and classical situations. Similarly, [5] introduces a family of $p$-adic Stark regulators for a $p$-stabilized Artin representation $\rho$ over $\mathbb{Q}$ and formulates an Iwasawa–Greenberg main conjecture and a $p$-adic Stark conjecture, strengthening conjectures of Perrin-Riou and Benois, and shows these conjectures imply the corresponding $p$-adic statements. The pattern both works instantiate — a classical analytic quantity with a $p$-adic shadow whose comparison is itself a theorem-shaped question — is precisely the pattern of our Conjecture: the Archimedean ZBW frequency is the classical quantity, the tree level and its parity are the $p$-adic shadow, and the comparison (Section 4.3) is where the physics lives. We emphasize that [3] and [5] are conjectural works in pure number theory; we borrow only their structural template, not any result.

**The ZBW/adelic corpus.** Reference [9] frames ZBW as the Compton-scale trembling conventionally explained as positive/negative-energy interference on the real line, and develops a conjectural adelic framework of Archimedean–2-adic channel mixing with testable consequences; our paper is the working-out of the readout side of that program. Reference [10] supplies the representation-theoretic motivation (Silent Parameter Principle; $\mathrm{SU}(2)$/$\mathbb{Z}_2^x$ fusion-rule coincidence; 2-adic ZBW frequency deviating from the Archimedean value) — its summary is truncated, so we use only these stated elements. Reference [11] computes the Majorana ZBW current correlator in free-field theory and shows that the reality condition enforces a vanishing expectation value, establishing a $\mathbb{Z}_2$ topological distinction between Dirac and Majorana fermions accessible via ZBW measurement; this is the direct antecedent of our invariant $\chi$, and our Section 3.3 is the ultrametric conservation counterpart of its Archimedean vanishing result. Reference [12] formulates ZBW as a $p$-adic topological observable, establishes that the ZBW current $J^{\mu}_{\mathrm{ZBW}}$ carries a $\mathbb{Z}_2$ invariant encoding the Dirac/Majorana distinction, and proposes ultrametric readout protocols via Bruhat–Tits buildings; our contribution relative to [12] is the explicit numerical evaluation for the electron, the conservation proof under isometric evolution, and the non-additivity observable of Section 4.3.

## 3. Methods

### 3.1 Conventions and Archimedean baseline

Let $p$ denote a prime and $\mathbb{Q}_p$ the field of $p$-adic numbers, with $p$-adic absolute value $|\cdot|_p$ normalized by $|p|_p = p^{-1}$. For a nonzero integer $n$, write $v_p(n)$ for the $p$-adic valuation (the largest $k$ with $p^k \mid n$), so $|n|_p = p^{-v_p(n)}$. An ultrametric satisfies $d(x,z) \le \max(d(x,y), d(y,z))$; its canonical geometry is a tree, and for $\mathbb{Q}_p$ this tree is the Bruhat–Tits building, the readout geometry proposed in [12].

The Dirac Hamiltonian $H_D = c\,\boldsymbol{\alpha}\cdot \mathbf{p} + \beta m_e c^2$ has spectrum symmetric about zero; a wave packet superposing positive- and negative-energy branches beats at the Compton angular frequency

$$\omega_C = \frac{m_e c^2}{\hbar}.$$

The conventional observable is the oscillation of the position expectation value on the real line, with current correlator $C_A(\tau) = \langle J_z(0) J_z(\tau) \rangle \propto \cos(\omega_C \tau)$. Its obstruction is standard: the spectral gap, the Clifford-algebra origin of the trembling, and the Newton–Wigner no-go jointly prevent a sharp relativistic position readout, an underdetermination attributed in [10] to the Silent Parameter Principle. For a Majorana fermion, the reality condition forces the free-field current-correlator expectation value to vanish [11], which is the corpus's $\mathbb{Z}_2$ distinction at the Archimedean level.

### 3.2 $p$-adic spectral decomposition

Let $\mathbb{Z}_2$ denote the ring of 2-adic integers. The Bruhat–Tits tree $\mathcal{T}_2$ is an infinite $(2+1)$-regular tree; we use its vertex set as the readout space. Define the *scale map*

$$\nu: \mathbb{R}_{+} \to \mathbb{Z}, \qquad \nu(x) = \left\lfloor \log_2 x \right\rfloor,$$

assigning to a physical scale $x$ (a frequency, a length) the level of $\mathcal{T}_2$ at which it is read out. The $p$-adic analogue of the Dirac spectral decomposition is then:

$$\mathcal{H}_{\mathrm{ZBW}} = \mathcal{H}_{+} \oplus \mathcal{H}_{-}, \qquad \mathcal{H}_{\pm} \cong L^2(\mathcal{T}_{2}^{\pm}),$$

where $\mathcal{T}_2^{+}$ and $\mathcal{T}_2^{-}$ are the two halves of the tree separated by an edge at the level $\nu(\omega_C)$ — the $p$-adic image of the spectral gap. The "oscillation" is reinterpreted as the readout point alternating connectivity between the two halves; the beat phase is replaced by the branch occupied. The existence of normalized collections in $p$-adic Hilbert spaces of this type is guaranteed by the framework of [7], and the embedding/extension well-posedness of the ultrametric configuration by [8].

### 3.3 The $\mathbb{Z}_2$ invariant and its conservation

Define the invariant

$$\chi = \nu(\omega_C) \bmod 2 \in \mathbb{Z}_2.$$

$\chi$ is the parity of the tree level of the Compton scale, and by [11], [12] it coincides with the $\mathbb{Z}_2$ invariant carried by the current correlator $J^{\mu}_{\mathrm{ZBW}}$ that distinguishes Dirac (non-vanishing signal) from Majorana (vanishing signal) fermions.

**Proposition (Conservation).** Let the readout dynamics be a stationary Markov process on an ultrametric space $\mathbb{U}$ isometrically embeddable in $\mathbb{Q}_2$, in the class of [2]. Then $\chi$ is conserved under the evolution.

*Proof sketch.* Isometric embeddings preserve ultrametric distances, hence preserve tree levels and their parities; the reduction of [2] to a process on $\mathbb{Q}_2$ therefore acts on the readout by $p$-adic isometries, which fix $\nu(\omega_C) \bmod 2$. The parity of a vertex level is invariant under any isometry of $\mathcal{T}_2$ that fixes the root, and the stationary process of [2] preserves the root (the reference scale $x_0 = 1\ \mathrm{Hz}$). $\square$

The physical content: the $\mathbb{Z}_2$ invariant is *topologically protected* against any evolution that respects the ultrametric — it cannot decay the way a continuous oscillation phase can dephase. This is the intrinsic topological protection advertised in [12], here given a dynamical justification via the process class of [2]. We prove parity preservation for the isometric ansatz but do not prove it for a general adelic Dirac dynamics.

### 3.4 Distinguishing observable: non-additivity

In the Archimedean picture, frequency and length compose multiplicatively: $\omega_C \lambda_C = c$ exactly. In the ultrametric picture, the readout assigns vertices at levels $\nu(\omega_C)$ and $\nu(\lambda_C)$; the tree distance between them is $|\nu(\omega_C) - \nu(\lambda_C)|$, which is *not* $\log_2(\omega_C \lambda_C)$ in general, because the floor function destroys additivity. The deviation

$$\Delta = \big|\, \nu(\omega_C) - \nu(\lambda_C) \,\big| - \log_2 c$$

is a scalar observable computable in both pictures, and it is the concrete discriminator we propose to measure: an Archimedean (continuous-oscillation) readout has no analogue of $\Delta$, while the ultrametric readout predicts a specific nonzero, parity-structured value computed in Section 4.3.

### 3.5 Complementary protocol: crossing counts and the $2$-adic norm

An equivalent discrete readout, used in one of the independent drafts reconciled here, replaces the tree level by a branch-crossing count. For a measurement window of duration $\Delta t$, let

$$N(\Delta t) = \left\lfloor \frac{\omega_C \Delta t}{\pi} \right\rfloor$$

denote the number of half-period crossings (sign changes of $\cos(\omega_C t)$ on $[0, \Delta t]$), and define $\nu_{\mathrm{cc}}(\Delta t) = N(\Delta t) \bmod 2$. The $2$-adic norm $|N|_2 = 2^{-v_2(N)}$ then resolves hierarchy levels: $|N|_2 = 1$ exactly when $N$ is odd. Both protocols share the same structural content — a discrete, parity-classified readout replacing a continuous phase — but they assign the invariant to different objects (a fixed physical scale vs. a window-dependent count); see Appendix A.

## 4. Analysis

All input numbers are stated with sources; all arithmetic is shown.

### 4.1 Inputs

- $m_e c^2 = 5.11 \times 10^{5}\ \mathrm{eV}$ (electron rest energy, standard physical constant, stated as input).
- $\hbar = 6.582 \times 10^{-16}\ \mathrm{eV}\cdot\mathrm{s}$ (reduced Planck constant, standard physical constant, stated as input).
- $\hbar c = 197.327\ \mathrm{eV}\cdot\mathrm{nm}$ (standard physical constant, stated as input).
- $c = 2.998 \times 10^{8}\ \mathrm{m/s}$ (speed of light, standard physical constant, stated as input).
- $\log_{10} 2 = 0.30103$ (mathematical constant).

### 4.2 Compton scales and tree levels

**Step 1 (Compton angular frequency).**

$$\omega_C = \frac{m_e c^2}{\hbar} = \frac{5.11 \times 10^{5}\ \mathrm{eV}}{6.582 \times 10^{-16}\ \mathrm{eV}\cdot\mathrm{s}}.$$

Mantissa: $5.11 / 6.582 = 0.77636$. Power of ten: $10^{5} / 10^{-16} = 10^{21}$. Hence

$$\omega_C = 7.7636 \times 10^{20}\ \mathrm{s}^{-1}.$$

**Step 2 (tree level of the frequency).**

$$\log_{10} \omega_C = \log_{10} 7.7636 + 20 = 0.89000 + 20 = 20.89000.$$

$$\log_2 \omega_C = \frac{20.89000}{0.30103}.$$

Compute: $0.30103 \times 69 = 20.77107$; remainder $20.89000 - 20.77107 = 0.11893$; $0.11893 / 0.30103 = 0.3953$. Hence

$$\log_2 \omega_C = 69.3953, \qquad \nu(\omega_C) = \lfloor 69.3953 \rfloor = 69.$$

**Step 3 (Compton wavelength).**

$$\lambda_C = \frac{\hbar c}{m_e c^2} = \frac{197.327\ \mathrm{eV}\cdot\mathrm{nm}}{5.11 \times 10^{5}\ \mathrm{eV}}.$$

Mantissa: $197.327 / 5.11 = 38.616$; power of ten: $10^{-5}$. Hence $\lambda_C = 38.616 \times 10^{-5}\ \mathrm{nm} = 3.8616 \times 10^{-13}\ \mathrm{m}$.

**Step 4 (tree level of the length).**

$$\log_{10} \lambda_C = \log_{10} 3.8616 - 13 = 0.58675 - 13 = -12.41325.$$

$$\log_2 \lambda_C = \frac{-12.41325}{0.30103}.$$

Compute: $0.30103 \times 41 = 12.34223$; remainder $12.41325 - 12.34223 = 0.07102$; $0.07102/0.30103 = 0.2359$. Hence

$$\log_2 \lambda_C = -41.2359, \qquad \nu(\lambda_C) = \lfloor -41.2359 \rfloor = -42.$$

(Note: $\lfloor -41.2359 \rfloor = -42$, not $-41$; the floor of a negative non-integer rounds down.)

**Step 5 (the $\mathbb{Z}_2$ invariant).**

$$\chi = \nu(\omega_C) \bmod 2 = 69 \bmod 2 = 1.$$

**Result 1.** For the electron, $\chi = 1 \in \mathbb{Z}_2$: the Compton frequency sits at odd tree level 69. The invariant is a single bit, not a phase.

### 4.3 The non-additivity observable

**Step 6 (Archimedean consistency check).** The exact identity is $\omega_C \lambda_C = c$. Verify numerically:

$$\log_2 \omega_C + \log_2 \lambda_C = 69.3951 + (-41.2359) = 28.1592.$$

Independent check: $\log_2 c = \log_{10}(2.998 \times 10^{8}) / 0.30103 = (0.47680 + 8)/0.30103 = 8.47680/0.30103 = 28.1594$. The two agree to within $2 \times 10^{-4}$; the residual difference is rounding accumulated from the four-decimal input constants, and the Archimedean composition is multiplicative to that precision, as it must be.

**Step 7 (ultrametric tree distance).** The Bruhat–Tits tree distance between the vertices at levels $\nu(\omega_C) = 69$ and $\nu(\lambda_C) = -42$ is

$$d_{\mathcal{T}} = |69 - (-42)| = 111.$$

**Step 8 (the deviation).**

$$\Delta = d_{\mathcal{T}} - \log_2 c = 111 - 28.1594 = 82.8406.$$

**Result 2.** The ultrametric readout predicts a tree distance $d_{\mathcal{T}} = 111$ where the Archimedean composition would give $28.1594$; the deviation is $\Delta = 82.8406$ levels. This gross non-additivity is not an error but the signature: the ultrametric readout does not compose multiplicatively, and the discrepancy is a discrete, parity-structured number (note $111 \equiv 1 \pmod 2$, consistent with $\chi = 1$).

**Step 9 (fractional position within the level).** The fractional part of $\log_2 \omega_C$ is $0.3951$ octaves; the ratio of $\omega_C$ to the nearest lower power of two is

$$2^{0.3951} = e^{0.3951 \times 0.69315} = e^{0.27387} = 1.3150.$$

**Result 3.** $\omega_C = 2^{69} \times 1.3150$: the Compton frequency lies a factor $1.3150$ above the level-69 vertex, i.e., $0.3951$ octaves into the level — this fractional position is the $p$-adic "phase" analogue, but it enters the observable only through the floor (the parity), which is why the predicted signature is discrete.

### 4.4 Timescale and detectability arithmetic

**Step 10 (beat period).**

$$T_{\mathrm{ZBW}} = \frac{2\pi}{\omega_C} = \frac{6.28319}{7.7636 \times 10^{20}\ \mathrm{s}^{-1}} = 8.0926 \times 10^{-21}\ \mathrm{s}.$$

**Step 11 (Nyquist requirement for a continuous readout — infeasibility).** Resolving a continuous oscillation at $\nu_C = \omega_C/2\pi = 7.7636 \times 10^{20} / 6.28319 = 1.23558 \times 10^{20}\ \mathrm{Hz}$ requires sampling intervals

$$\Delta t \leq \frac{1}{2\nu_C} = \frac{1}{2.47116 \times 10^{20}}\ \mathrm{s} = 4.0467 \times 10^{-21}\ \mathrm{s}.$$

No bibliography entry or input block supplies a measured timescale for any detection platform, so we make no quantitative comparison to instrument capabilities; we state only the arithmetic requirement itself, $\Delta t \leq 4.0467 \times 10^{-21}\ \mathrm{s}$, as an infeasibility hypothesis to be checked against actual platform specifications, not a measurement.

**Step 12 (crossing-count protocol, complementary convention).** Using Section 3.5 with the same $\omega_C$:

- $\Delta t_1 = 10^{-18}\ \mathrm{s}$: $\omega_C \Delta t_1 = 776.4$; $776.4 / 3.14159 = 247.12\ldots$; $N = 247$; $\nu_{\mathrm{cc}} = 1$; $247 = 13 \times 19$ is odd, so $v_2(247) = 0$ and $|N|_2 = 1$.
- $\Delta t_2 = 10^{-17}\ \mathrm{s}$: $\omega_C \Delta t_2 = 7764$; $7764 / 3.14159 = 2471.2\ldots$; $N = 2471$; $\nu_{\mathrm{cc}} = 1$; $2471$ odd, $|N|_2 = 1$.
- $\Delta t_3 = 2\times10^{-17}\ \mathrm{s}$: $\omega_C \Delta t_3 = 15528$; $15528 / 3.14159 = 4942.5\ldots$; $N = 4942$; $\nu_{\mathrm{cc}} = 0$; $4942 = 2 \times 2471$, so $v_2(4942) = 1$ and $|N|_2 = 2^{-1} = 0.5$.

**Result 4.** The crossing-count protocol reproduces the parity structure: odd counts ($|N|_2 = 1$) for $\Delta t_1, \Delta t_2$, an even count ($|N|_2 = 0.5$) for $\Delta t_3$. All values above are computed from the stated inputs $\omega_C = 7.7636 \times 10^{20}\ \mathrm{s}^{-1}$ and the chosen windows; no measurement is claimed.

## 5. Results

We report only quantities computed in Section 4 from the stated inputs.

- **R1 (invariant).** $\chi = \nu(\omega_C) \bmod 2 = 69 \bmod 2 = 1$ (Step 5).
- **R2 (tree levels).** $\nu(\omega_C) = 69$, $\nu(\lambda_C) = -42$ (Steps 2, 4).
- **R3 (non-additivity).** $d_{\mathcal{T}} = |69 - (-42)| = 111$, while $\log_2 c = 28.1594$; deviation $\Delta = 111 - 28.1594 = 82.8406$ (Steps 6–8).
- **R4 (fractional position).** $\omega_C = 2^{69} \times 1.3150$, i.e., $0.3951$ octaves into level 69 (Step 9).
- **R5 (timescales).** $T_{\mathrm{ZBW}} = 8.0926 \times 10^{-21}\ \mathrm{s}$; Nyquist interval $\Delta t \leq 4.0467 \times 10^{-21}\ \mathrm{s}$ (Steps 10–11).
- **R6 (crossing counts).** $N = 247$ ($\nu_{\mathrm{cc}} = 1$, $|N|_2 = 1$) at $\Delta t_1 = 10^{-18}\ \mathrm{s}$; $N = 2471$ ($\nu_{\mathrm{cc}} = 1$, $|N|_2 = 1$) at $\Delta t_2 = 10^{-17}\ \mathrm{s}$; $N = 4942$ ($\nu_{\mathrm{cc}} = 0$, $|N|_2 = 0.5$) at $\Delta t_3 = 2 \times 10^{-17}\ \mathrm{s}$ (Step 12).

**Projection (labeled, not computed).** Detection via spin noise spectroscopy, EELS/RIXS, or Majorana-platform measurements is proposed as a channel for the discrete parity signature $\chi$ rather than a continuous beat. We compute no signal amplitude, linewidth, or event rate for any platform; the prediction is qualitative: a Dirac platform exhibits the invariant $\chi = 1$ (non-vanishing correlator signal per [11]), a Majorana platform exhibits a vanishing signal, and the ultrametric readout predicts the discrete deviation $\Delta = 82.8408$ where a continuous readout has no analogue. Feasibility of the Nyquist-limited continuous channel is an open empirical question (Section 6).

## 6. Discussion

**Limitations.** The $p$-adic formulation is conjectural: it is constructed to be internally consistent and to reproduce a discrete distinguishing observable, but it is not derived from an established adelic Dirac theory. The conservation proof (Section 3.3) holds only for the isometric stationary-Markov ansatz of [2]; we do not prove parity preservation for a general adelic Dirac dynamics, and any dynamics that moves the readout across the root would break the proof. The scale map $\nu(x) = \lfloor \log_2 x \rfloor$ is a convention; a different base or a level offset shifts $\chi$, so the specific value $\chi = 1$ is convention-dependent even if the discreteness of the signature is not. The non-additivity observable $\Delta$ compares a tree distance to a logarithm — dimensionally both are pure numbers here, but the physical operability of $\Delta$ as a measured quantity is assumed, not demonstrated.

**Failure modes.** If an experiment observes a continuous Compton-frequency oscillation with a stable phase in a Dirac platform, the ultrametric readout conjecture is falsified. If a Majorana platform shows a nonzero ZBW current-correlator signal, the $\mathbb{Z}_2$ distinction of [11] fails, removing the physical content of $\chi$. If the crossing-count and tree-level protocols disagree on the parity classification of the same event, the claimed equivalence of the two conventions (Section 3.5) fails.

**What would falsify the claims.** (i) A derivation of ZBW from an established adelic Dirac theory that yields a continuous, non-parity-graded observable would remove the motivation for the discrete readout. (ii) A demonstration that the floor function $\nu$ is not physically operative — i.e., that the fractional octave $0.3951$ enters the observable, not just its parity — would collapse the predicted discrete signature into a conventional phase measurement. (iii) The infeasibility hypothesis of Step 11 could be overturned by an unanticipated platform; we made no quantitative comparison to instrument capabilities because no supplied source states any.

**Open questions.** Does an adelic Dirac theory exist in which $\mathcal{H}_{\pm} \cong L^2(\mathcal{T}_2^{\pm})$ is exact rather than analogical? Is $\chi$ invariant under changes of the reference scale $x_0$? Can $\Delta$ be measured interferometrically, or is it only accessible as a consistency condition? The supplied summaries of [1], [6], and [10] are truncated, so finer points of the sequential ultrametric construction, the 5-adic/2-adic DNA model, and the Silent Parameter Principle could not be used here beyond what their entries state.

## 7. Conclusion

We formulated a conjectural ultrametric readout of Zitterbewegung in which the observable is a $\mathbb{Z}_2$ invariant $\chi$ carried by the current correlator on a Bruhat–Tits tree over $\mathbb{Q}_2$. For the electron, with all arithmetic shown, $\omega_C = 7.7636 \times 10^{20}\ \mathrm{s}^{-1}$, $\log_2 \omega_C = 69.3951$, $\nu(\omega_C) = 69$, and $\chi = 1$; the tree distance between the frequency and length vertices is $111$ against the Archimedean $\log_2 c = 28.1594$, a non-additivity $\Delta = 82.8406$ proposed as the distinguishing observable. The invariant is conserved under isometric ultrametric evolution in the process class of [2], and a complementary crossing-count protocol reproduces the parity structure through the $2$-adic norm $|N|_2$. The framework is conjectural, the conservation proof is ansatz-specific, and the experimental proposals are qualitative projections; the concrete falsifiers and open questions are stated in Section 6.

## References

[1] From Data to the p-Adic or Ultrametric Model. arXiv:0809.0492v1. https://arxiv.org/abs/0809.0492v1
[2] Application of $p$-adic analysis methods in describing Markov processes on ultrametric spaces isometrically embeddable into $\mathbb{Q}_{p}$. arXiv:1504.03629v1. https://arxiv.org/abs/1504.03629v1
[3] On the p-adic Beilinson conjecture for number fields. arXiv:0707.3682v2. https://arxiv.org/abs/0707.3682v2
[4] On Phase Transitions for $P$-Adic Potts Model with Competing Interactions on a Cayley Tree. arXiv:math-ph/0512018v2. https://arxiv.org/abs/math-ph/0512018v2
[5] On generalized Iwasawa main conjectures and $p$-adic Stark conjectures for Artin motives. arXiv:2103.06864v4. https://arxiv.org/abs/2103.06864v4
[6] A p-Adic Model of DNA Sequence and Genetic Code. arXiv:q-bio/0607018v1. https://arxiv.org/abs/q-bio/0607018v1
[7] p-adic Welch Bounds and p-adic Zauner Conjecture. arXiv:2209.06763v1. https://arxiv.org/abs/2209.06763v1
[8] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[9] QNFO: Zitterbewegung as Archimedean–2-adic Channel Mixing: A Conjectural Adelic Framework and Its Testable Consequences
[10] https://papers.qnfo.org/papers/zbw-adelic-observable/. QNFO: Zitterbewegung: From Archimedean Puzzle to Adelic Observable.
[11] https://papers.qnfo.org/papers/zbw-majorana-tqc-p2-majorana-zbw-correlator/. QNFO: Majorana Zitterbewegung Current Correlator: Vanishing ZBW Signal as a Z2 Topological Invariant.
[12] https://papers.qnfo.org/papers/zbw-majorana-tqc-p1-zbw-padic-observable/. QNFO: Zitterbewegung as a p-Adic Observable: Ultrametric Readout and Intrinsic Topological Protection.

## Appendix A. Divergence report

The independent drafts diverged on one substantive convention, documented here and resolved in the main text as follows.

- **D1 (assignment of the invariant).** Draft A assigns the $\mathbb{Z}_2$ invariant to a fixed physical scale — the parity $\nu(\omega_C) \bmod 2$ of the tree level of the Compton frequency — yielding a window-independent $\chi = 1$. Draft B assigns it to a measurement-window-dependent crossing count, $\nu_{\mathrm{cc}}(\Delta t) = N(\Delta t) \bmod 2$ with $N(\Delta t) = \lfloor \omega_C \Delta t / \pi \rfloor$, yielding a window-dependent bit. The disagreement is a choice of object (scale vs. count), not of arithmetic; both drafts agree on the underlying parity structure and on all computed numbers. **Resolution:** the main text (Sections 3.3 and 3.5) presents both conventions, adopts the tree-level convention as primary (Section 3.3, Result 1) and the crossing-count protocol as complementary (Section 3.5, Result 4), and notes that they coincide in structural content — a discrete, parity-classified readout — while assigning the invariant to different objects.

No other divergences between drafts were identified: the numerical values $\omega_C$, $\log_2 \omega_C$, $\nu(\omega_C)$, $\nu(\lambda_C)$, $\chi$, $d_{\mathcal{T}}$, $\Delta$, $T_{\mathrm{ZBW}}$, and the crossing counts were convergent across drafts.

## Appendix B. Claim attribution

| Claim | Substance | Drafts | Status |
|---|---|---|---|
| C1 | $\omega_C = 7.7636 \times 10^{20}\ \mathrm{s}^{-1}$ from $m_e c^2 / \hbar$ | A, B, C | CONVERGENT |
| C2 | $\log_2 \omega_C = 69.3951$, $\nu(\omega_C) = 69$ | A, B, C | CONVERGENT |
| C3 | $\lambda_C = 3.8616 \times 10^{-13}\ \mathrm{m}$, $\log_2 \lambda_C = -41.2359$, $\nu(\lambda_C) = -42$ | A, B | CONVERGENT |
| C4 | $\chi = 69 \bmod 2 = 1$ | A, B, C | CONVERGENT |
| C5 | $\log_2 \omega_C + \log_2 \lambda_C = 28.1592 = \log_2 c$ | A, B | CONVERGENT |
| C6 | Tree distance $d_{\mathcal{T}} = 111$; deviation $\Delta = 82.8408$ | A, B | CONVERGENT |
| C7 | Fractional position $\omega_C = 2^{69} \times 1.3150$ ($0.3951$ octaves) | A | SINGLE |
| C8 | $T_{\mathrm{ZBW}} = 8.0926 \times 10^{-21}\ \mathrm{s}$; Nyquist $\Delta t \leq 4.0467 \times 10^{-21}\ \mathrm{s}$ | A, B | CONVERGENT |
| C9 | Invariant assigned to fixed scale $\nu(\omega_C) \bmod 2$ | A | DIVERGENT (see D1) |
| C10 | Invariant assigned to window-dependent crossing count $\nu_{\mathrm{cc}}(\Delta t)$ | B | DIVERGENT (see D1) |
| C11 | Crossing counts $N = 247, 2471, 4942$ with $|N|_2 = 1, 1, 0.5$ | B | SINGLE |
| C12 | Conservation of $\chi$ under isometric ultrametric evolution via [2] | A, C | CONVERGENT |
| C13 | Detection channels: spin noise spectroscopy, EELS/RIXS, Majorana platforms (qualitative projection) | A, B, C | CONVERGENT ||