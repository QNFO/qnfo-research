# Corrected Condensation Indices and the Sixteen-Fold Way: A Quantitative Bulk-Boundary Dictionary for Ising-Type Anyon Condensates

## Abstract

A companion preprint (https://papers.qnfo.org/papers/a-two-index-framework-for-the-bulk-boundary-correspondence-of-anyon-condensation/) introduced computable indices for anyon condensation: the dimension ratio $\kappa = D_C^2/D_D^2$, the chirality-sensitive index $\mu = 2\,\Delta c$, and the non-Abelian fraction $f_{\mathrm{NA}}$. We correct an arithmetic error in that work's Case III, the condensation of $\text{Ising} \times \overline{\text{Ising}}$: the parent total quantum dimension satisfies $D_C^2 = 16$, not $14$, because the non-Abelian anyon $(\sigma,\bar\sigma)$ has quantum dimension $d_{(\sigma,\bar\sigma)} = \sqrt{2}\cdot\sqrt{2} = 2$, contributing $2^2 = 4$ to the sum. The condensing boson $(\psi,\bar\psi)$ fixes $(\sigma,\bar\sigma)$, which splits into two Abelian child anyons, so the child is the toric code with $D_D^2 = 4$, giving the normal condensate ratio $\kappa = 16/4 = 4$ and a child-side non-Abelian fraction $f_{\mathrm{NA}} = 0$, not $1/3$. We identify $\mu = 2\,\Delta c$ with Kitaev's sixteen-fold way label $\nu \bmod 16$, verify the identification at the anchor points $\nu = 0$ and $\nu = 1$, and show that $\kappa$ and $f_{\mathrm{NA}}$ are mirror-blind while $\mu$ alone is signed. We replace the heuristic boundary fusion rule "$\psi \sim 1$" with a module-category treatment over the condensate algebra, state a completeness conjecture for the index triple, and delimit what the indices cannot see: chirality enters only through $\mu$, and nothing in $(\kappa, \mu, f_{\mathrm{NA}})$ addresses operational control or readout, which for Ising anyons remain Clifford-only braiding and fusion-parity measurement.

## 1. Introduction

The bulk-boundary correspondence in $(2+1)$-dimensional topological phases states that the topological data of a bulk determine the physics of its boundary. In the setting of anyon condensation — the process by which a subset of bulk anyons is forced to condense, producing a new topological order — this correspondence is usually stated structurally: the child category is a quotient or module category of the parent category [2]. The companion work [10] proposed to make the correspondence quantitative by attaching computable numbers to a condensation: the dimension ratio $\kappa$, the chirality index $\mu = 2\,\Delta c$ (where $\Delta c$ is the change in chiral central charge across the condensation), and the non-Abelian fraction $f_{\mathrm{NA}}$.

That work contained an arithmetic error in its Case III, the condensation of the product theory $\text{Ising} \times \overline{\text{Ising}}$, which is the minimal setting for studying boundaries carrying Majorana zero modes (the $\sigma$ anyon of the Ising theory models a Majorana defect; experimental platforms pursuing Majorana physics are reviewed in [3], [4], [5]). The error propagated into the reported values $D_C^2 = 14$, $\kappa = 14/4$, and $f_{\mathrm{NA}} = 1/3$. In this paper we correct the case: the correct parent dimension is $D_C^2 = 16$, the child is the toric code with $D_D^2 = 4$, the condensate is normal with $\kappa = 4$, and the child-side non-Abelian fraction is $f_{\mathrm{NA}} = 0$. The correction is not merely cosmetic: it restores the interpretation of the condensate as a normal condensation and changes the classification statement that the indices support.

Beyond the correction, we make four contributions. First, we identify the chirality index $\mu = 2\,\Delta c$ with Kitaev's sixteen-fold way label $\nu \bmod 16$ and verify the identification at directly computable anchor points. Second, we argue that the heuristic boundary fusion rule "$\psi \sim 1$" used in [10] should be replaced by the module-category treatment of the condensate algebra. Third, we formulate a completeness conjecture — whenever $\mu > 0$ or $f_{\mathrm{NA}} > 0$, boundary defect fusion is multi-channel — and prove a restricted version of it within the sixteen-fold way series. Fourth, we delimit what the indices do not measure: chirality enters only through $\mu$, and nothing in $(\kappa, \mu, f_{\mathrm{NA}})$ speaks to operational questions of control and readout.

## 2. Background and Related Work

**Anyon condensation as a categorical bootstrap.** Bhardwaj–Schembera-type treatments of anyon condensation [2] work abstractly: a modular tensor category $\mathcal{D}$ is obtained from a parent $\mathcal{C}$ by condensing a connected étale (condensable) algebra $A \subset \mathcal{C}$, and a bootstrap analysis derives the relation between $\mathcal{C}$ and $\mathcal{D}$ from physical requirements of locality, unitarity, and positivity of dimensions. Our corrected Case III is exactly an instance of this framework: the condensate algebra is $A = \mathbf{1} \oplus (\psi,\bar\psi)$, and the child category is the category of local $A$-modules $\mathcal{C}_A^{\mathrm{loc}}$. The splitting of the fixed-point anyon $(\sigma,\bar\sigma)$ into Abelian child anyons is the standard fixed-point resolution required by the bootstrap, and we use this formalism to replace the heuristic "$\psi \sim 1$" boundary rule of [10].

**Bulk-boundary correspondence in SPT and response language.** The effective-field-theory treatment of bosonic symmetry-protected topological phases in [1] derives purely topological bulk response actions whose boundary physics is fixed by bulk invariants, including chiral central charge. Our program is the anyon-condensation analogue: find bulk topological invariants ($D_C^2$, $\Delta c$, fusion multiplicities) that quantitatively fix boundary data. The index $\mu = 2\,\Delta c$ is the condensation analogue of the chiral response mismatch tracked in [1]: it is the only one of our three indices that is signed and therefore orientation-sensitive.

**Anyon fundamentals and the toric code.** The pedagogical treatment of Abelian and non-Abelian anyons in [8] supplies the definitions we use throughout — topological spin $\theta_a$, quantum dimension $d_a$ (the asymptotic growth rate of fusion spaces, equal to $1$ exactly for Abelian anyons), total quantum dimension $D = \sqrt{\sum_a d_a^2}$, braid groups, and the toric code as the canonical exactly solvable model with Abelian excitations $\{1, e, m, \varepsilon\}$. The Ising anyon data $d_\sigma = \sqrt{2}$, $\sigma \times \sigma = 1 + \psi$, and the toric-code data $D^2 = 4$ are the numerical inputs to every computation in Section 4.

**Condensation analogies beyond topological matter.** Tachyon condensation in bosonic string theory [6] provides a structural analogy from a very different field: an unstable configuration condenses and the resulting vacuum has fewer effective degrees of freedom, with boundary-state formalism describing the process. We use this analogy only heuristically, to motivate the expectation that condensation reduces total quantum dimension by an integer ratio $\kappa$; the corrected Case III with $\kappa = 4$ conforms.

**Quantification methodology from adjacent fields.** The companion framework [10] belongs to a broader program of replacing structural statements with computable multi-index summaries. The fusion of statistics and network science for functional brain networks [7] is an adjacent-field example where a single structural descriptor was replaced by a battery of complementary indices; we borrow the methodological lesson that distinct indices must be checked for independence — here, chirality sensitivity. Similarly, the equivalence result between distance-based and RKHS-based statistics in [9] shows that apparently different summary statistics can coincide; our identification $\mu = \nu \bmod 16$ is an analogous statement, equating our index with an established classification label.

**Majorana experimental context.** The MAJORANA program [3], [4], [5] pursues neutrinoless double-beta decay with germanium detectors, targeting effective Majorana-neutrino mass sensitivity below $50\ \mathrm{meV}$ [4]. We cite this program not for its physics results but as the terminological anchor for "Majorana statistics" at boundaries: the boundary defects of the Ising theory carry Majorana zero modes, and the readout question we flag in Section 6 (fusion-channel parity measurement) is the topological-quantum-computing analogue of the parity measurements central to [3], [4], [5].

## 3. Methods

### 3.1 Definitions

Let $\mathcal{C}$ be a unitary modular tensor category (the parent) with simple objects $a$, quantum dimensions $d_a$, topological spins $\theta_a$, and total quantum dimension

$$D_C^2 = \sum_{a \in \mathcal{C}} d_a^2.$$

A condensation is specified by a connected étale algebra $A = \bigoplus_i n_i a_i$ in $\mathcal{C}$; the child category is $\mathcal{D} = \mathcal{C}_A^{\mathrm{loc}}$, the category of local $A$-modules [2]. Following [10], the indices are

$$\kappa = \frac{D_C^2}{D_D^2}, \qquad \mu = 2\,\Delta c, \qquad f_{\mathrm{NA}} = \frac{N_{\mathrm{NA}}^{\mathcal{D}}}{N_{\mathrm{tot}}^{\mathcal{D}}},$$

where $\Delta c = c_C - c_D$ is the difference of chiral central charges between parent and child, $N_{\mathrm{NA}}^{\mathcal{D}}$ counts non-Abelian simple objects of the child, and $N_{\mathrm{tot}}^{\mathcal{D}}$ the total number of child simples. A condensate is called **normal** when $\kappa$ is a positive integer.

### 3.2 The Ising theory and its conjugate

The Ising theory has simple objects $\{1, \sigma, \psi\}$ with

$$d_1 = 1, \qquad d_\sigma = \sqrt{2}, \qquad d_\psi = 1,$$

fusion $\sigma \times \sigma = 1 + \psi$, $\sigma \times \psi = \sigma$, $\psi \times \psi = 1$; spins $\theta_1 = 1$, $\theta_\psi = 1$ (so $\psi$ is an Abelian boson), $\theta_\sigma = e^{i\pi/8}$; and chiral central charge $c_{\mathrm{Ising}} = 1/2$. The conjugate theory $\overline{\mathrm{Ising}}$ has objects $\{1, \bar\sigma, \bar\psi\}$ with the same dimensions, spins $\theta_{\bar\sigma} = e^{-i\pi/8}$, and $c_{\overline{\mathrm{Ising}}} = -1/2$.

### 3.3 Computational procedure

For each case we: (i) list the parent simple objects and compute $D_C^2$ by direct summation; (ii) identify the condensate algebra $A$ and compute the orbits of the fusion action of $A$'s invertible components; (iii) resolve fixed-point orbits by splitting into simple child objects, checking consistency with $D_D^2$ and with the bootstrap requirements of [2]; (iv) compute $\kappa$, $\mu$, $f_{\mathrm{NA}}$ from the definitions. All arithmetic is shown explicitly in Section 4; no numerical simulation is used.

## 4. Analysis

Every input number below is stated with its source; every arithmetic step is shown.

### 4.1 Inputs

**Input 1** (standard Ising data [8]): $d_1 = 1$, $d_\sigma = \sqrt{2}$, $d_\psi = 1$; $\sigma \times \sigma = 1 + \psi$; $c_{\mathrm{Ising}} = 1/2$.

**Input 2** (standard toric-code data [8]): anyons $\{1, e, m, \varepsilon\}$, all Abelian with $d_a = 1$; fusion $e \times m = \varepsilon$.

**Input 3** (sixteen-fold way, Section 3.2 and [8]): odd-$\nu$ members have sectors $\{1, \psi, \sigma\}$ with $d_\sigma = \sqrt{2}$; even-$\nu$ members are Abelian; each unit of $\nu$ contributes $\Delta c = 1/2$, so $c = \nu/2 \pmod 8$.

### 4.2 Parent total quantum dimension: $D_C^2 = 16$

The parent is $\mathcal{C} = \text{Ising} \times \overline{\text{Ising}}$ with $3 \times 3 = 9$ simple objects $(a, \bar b)$, $a, b \in \{1, \sigma, \psi\}$. Quantum dimensions multiply across the product:

$$d_{(a,\bar b)} = d_a \cdot d_{\bar b}.$$

The nine anyons and their dimensions are:

$$
\begin{aligned}
&(1,1): 1, \quad (1,\bar\sigma): \sqrt{2}, \quad (1,\bar\psi): 1,\\
&(\sigma,1): \sqrt{2}, \quad (\sigma,\bar\sigma): 2, \quad (\sigma,\bar\psi): \sqrt{2},\\
&(\psi,1): 1, \quad (\psi,\bar\sigma): \sqrt{2}, \quad (\psi,\bar\psi): 1,
\end{aligned}
$$

using in particular $d_{(\sigma,\bar\sigma)} = \sqrt{2} \times \sqrt{2} = 2$. Then

$$D_C^2 = 1 + 2 + 1 + 2 + 4 + 2 + 1 + 2 + 1 = 16.$$

Equivalently, since total quantum dimension multiplies under products,

$$D_C^2 = D_{\mathrm{Ising}}^2 \cdot D_{\overline{\mathrm{Ising}}}^2 = \bigl(1^2 + (\sqrt{2})^2 + 1^2\bigr) \times \bigl(1^2 + (\sqrt{2})^2 + 1^2\bigr) = 4 \times 4 = 16.$$

The erroneous value $D_C^2 = 14$ in [10] arose from mis-evaluating $d_{(\sigma,\bar\sigma)}$: the correct value is $2$, whose square $2^2 = 4$ contributes $4$ to the sum, not $2$. The correct value is

$$\boxed{D_C^2 = 16.}$$

### 4.3 The condensate and the child category: $D_D^2 = 4$

The condensed algebra is $A = \mathbf{1} \oplus (\psi,\bar\psi)$, where $(\psi,\bar\psi)$ is an Abelian boson: $d_{(\psi,\bar\psi)} = 1 \times 1 = 1$ and $\theta_{(\psi,\bar\psi)} = \theta_\psi\,\theta_{\bar\psi} = 1 \cdot 1 = 1$. Since $\psi$ has trivial mutual braiding with every Ising anyon, no anyon is confined; the child is the orbifold of $\mathcal{C}$ by the fusion action of $(\psi,\bar\psi)$. The orbits are:

```
orbit 1: (1,1)             ~ (psi,psi-bar)        d = 1
orbit 2: (1,psi-bar)       ~ (psi,1)              d = 1
orbit 3: (1,sigma-bar)     ~ (psi,sigma-bar)      d = sqrt(2)
orbit 4: (sigma,1)         ~ (sigma,psi-bar)      d = sqrt(2)
orbit 5: (sigma,sigma-bar)  (fixed point)         d = 2
```

Orbits 3 and 4 have dimension $\sqrt{2}$, which cannot occur as a simple object of a consistent child; per the bootstrap of [2], the half-dimension orbits pair with the split components of the fixed-point orbit. The key computation is the square of the non-Abelian parent anyon, using $\sigma \times \sigma = 1 + \psi$ (Input 1) componentwise:

$$(\sigma, \bar\sigma) \times (\sigma, \bar\sigma) = (\sigma \times \sigma,\; \bar\sigma \times \bar\sigma) = (1 + \psi,\; 1 + \bar\psi),$$

which expands as

$$(1+\psi) \otimes (1+\bar\psi) = (1,1) \oplus (1,\bar\psi) \oplus (\psi,1) \oplus (\psi,\bar\psi).$$

All four summands are Abelian, each with $d = 1 \times 1 = 1$. The fixed-point anyon $(\sigma,\bar\sigma)$ of dimension $d = 2$ therefore splits into **two** Abelian child simple objects of dimension $1$ each (dimension bookkeeping: $2 = 1 + 1$), which together with the identifications of orbits 1 and 2 supply the four child anyons. The child is

$$\mathcal{D} = \{ \mathbf{1},\ e,\ m,\ \varepsilon \}, \qquad d_{\mathbf{1}} = d_e = d_m = d_\varepsilon = 1,$$

with the toric-code fusion rules $e \times m = \varepsilon$ (Input 2); this is the unique assignment consistent with the condensate being a boson with trivial monodromy. Hence

$$D_D^2 = 1^2 + 1^2 + 1^2 + 1^2 = 4.$$

### 4.4 The indices for Case III

$$\kappa = \frac{D_C^2}{D_D^2} = \frac{16}{4} = 4,$$

a positive integer, so the condensate is **normal**. The child-side non-Abelian fraction is

$$f_{\mathrm{NA}} = \frac{N_{\mathrm{NA}}^{\mathcal{D}}}{N_{\mathrm{tot}}^{\mathcal{D}}} = \frac{0}{4} = 0,$$

since all four child simples are Abelian. This corrects the prior claims of [10]; the value $1/3$ was an artifact of the erroneous $D_C^2 = 14$ combined with a miscount of child anyons. For reference, the **parent-side** non-Abelian weight fraction is

$$f_{\mathrm{NA}}^{(\mathrm{parent})} = \frac{(\sqrt{2})^2 + (\sqrt{2})^2 + 2^2}{16} = \frac{2 + 2 + 4}{16} = \frac{8}{16} = \frac{1}{2},$$

showing that all parent non-Abelian structure is absorbed by the condensate.

### 4.5 Chirality: $\mu$ for Case III

The parent central charge is $c_C = 1/2 + (-1/2) = 0$; the child (toric code) has $c_D = 0$. Hence

$$\Delta c = c_C - c_D = 0 - 0 = 0, \qquad \mu = 2\,\Delta c = 0.$$

Case III is chirality-neutral across the condensation, as it must be for a self-conjugate product parent condensing to a non-chiral child.

### 4.6 The sixteen-fold way identification

By Input 3, the $\nu$-th member of Kitaev's sixteen-fold way has $c = \nu/2 \pmod 8$. Taking $\Delta c = \nu/2$ for the representative with $0 \le \nu < 16$,

$$\mu = 2\,\Delta c = 2 \cdot \frac{\nu}{2} = \nu \pmod{16}.$$

Thus $\mu$ is exactly the sixteen-fold way label. We verify the two anchor points by direct computation:

- $\nu = 0$ (toric code): $c = 0$, so $\Delta c = 0$ and $\mu = 2 \cdot 0 = 0$. ✓
- $\nu = 1$ (Ising): $c = 1/2$, so $\Delta c = 1/2$ and $\mu = 2 \cdot \tfrac{1}{2} = 1$. ✓

For the Ising theory itself, the directly computed indices are

$$D_C^2 = 1^2 + (\sqrt{2})^2 + 1^2 = 1 + 2 + 1 = 4, \qquad f_{\mathrm{NA}}^{(\mathrm{parent})} = \frac{(\sqrt{2})^2}{4} = \frac{2}{4} = \frac{1}{2}.$$

### 4.7 Mirror-blindness of $\kappa$ and $f_{\mathrm{NA}}$

Conjugating a theory ($\mathcal{C} \to \overline{\mathcal{C}}$) sends $\theta_a \to \theta_a^{-1}$ and $c \to -c$ but leaves all $d_a$ invariant. Hence $D_C^2$, $\kappa$, and $f_{\mathrm{NA}}$ are invariant under conjugation: they are **mirror-blind**. This is verified for Case III: replacing Ising by $\overline{\mathrm{Ising}}$ and vice versa leaves $d_{(\sigma,\bar\sigma)} = 2$ and $D_C^2 = 16$ unchanged, while flipping the sign of each factor's central charge. Only $\mu = 2\,\Delta c$ is signed and chirality-sensitive.

### 4.8 Restricted completeness test

**Claim:** within the sixteen-fold way series, $\mu \neq 0$ (equivalently $\nu$ odd) implies multi-channel bulk fusion structure. **Proof from stated inputs:** if $\nu$ is odd, the theory contains $\sigma$ with $\sigma \times \sigma = 1 + \psi$ (Input 3, reducing to Input 1 at $\nu = 1$); this fusion has two channels ($1$ and $\psi$), hence is multi-channel. If $\nu$ is even, the theory is Abelian (Input 3), all fusions are single-channel, and $f_{\mathrm{NA}} = 0$ trivially since there are no non-Abelian anyons. $\blacksquare$

## 5. Results

**R1 (Corrected Case III).** For $\text{Ising} \times \overline{\text{Ising}} \to$ toric code (Sections 4.2–4.5):

$$D_C^2 = 16, \qquad D_D^2 = 4, \qquad \kappa = \frac{16}{4} = 4, \qquad \mu = 0, \qquad f_{\mathrm{NA}} = 0.$$

The parent-side non-Abelian weight fraction is $f_{\mathrm{NA}}^{(\mathrm{parent})} = 1/2$ (Section 4.4).

**R2 (Anchor points of the series).** Computed directly:

| theory | $D_C^2$ | $\Delta c$ | $\mu$ | $f_{\mathrm{NA}}$ |
|---|---|---|---|---|
| toric code ($\nu = 0$) | $4$ | $0$ | $0$ | $0$ |
| Ising ($\nu = 1$) | $4$ | $1/2$ | $1$ | $1/2$ (parent-side) |
| $\text{Ising} \times \overline{\text{Ising}}$ (Case III) | $16$ | $0$ | $0$ | $0$ (child-side) |

**R3 (Sixteen-fold way identification — labeled projection).** Under the standard assumption $\Delta c = \nu/2 \pmod 1$ for the sixteen-fold way representative with label $\nu$ (Input 3), we project $\mu = \nu \bmod 16$ for all $\nu \in \{0, \dots, 15\}$. This projection is verified only at $\nu = 0$ and $\nu = 1$ (R2); the remaining values inherit the uncertainty of the central-charge formula, which is exact for the sixteen-fold way but whose translation into $(\kappa, f_{\mathrm{NA}})$ requires case-by-case category data we have not summed here.

**R4 (Restricted completeness).** Within the sixteen-fold way series, the claim "$\mu \neq 0$ implies multi-channel fusion" is proved in Section 4.8 from Inputs 1 and 3. Outside this series the analogous statement is a conjecture supported only by the small sample of R1–R2; no counterexample was found among the cases examined.

## 6. Discussion

**Limitations of the correction.** The Case III correction rests on the splitting of the fixed-point anyon $(\sigma,\bar\sigma)$ into two Abelian child anyons. This splitting is forced by consistency with the bootstrap of [2] and by the dimension bookkeeping $16 = 4 \times 4$, but the identification of the child as the toric code (rather than some other four-anyon Abelian theory) relies on the fusion rules of the split components, which we fixed by requiring $e \times m = \varepsilon$ with toric-code spins. A different assignment of spins to $e, m$ would give a different Abelian child; we chose the toric code because it is the assignment consistent with the condensate being a boson with trivial monodromy.

**What would falsify the claims.** The identification $\mu = \nu \bmod 16$ (R3) would be falsified by any sixteen-fold way member whose chiral central charge deviates from $\nu/2 \bmod 8$ in a way that makes $2\,\Delta c \ne \nu \bmod 16$; more seriously, it would be falsified if the sixteen-fold way label were not determined by $\Delta c$ alone (e.g., if two members with the same $\Delta c$ carried different $\nu$). The completeness conjecture (R4, outside the series) would be falsified by a single condensate with $\mu > 0$ or $f_{\mathrm{NA}} > 0$ whose boundary defect fusion is single-channel; our evidence covers only the sixteen-fold way series and the three computed families, so the general claim should be treated as a conjecture. A concrete search strategy is: (1) enumerate all fermionic topological orders with $\nu \bmod 16 \neq 0$ from the sixteen-fold way; (2) construct all admissible condensate algebras using the formalism of [2]; (3) compute the resulting boundary defect fusion rules via the module-category approach.

**Failure modes of the index framework.** First, $\kappa$ and $f_{\mathrm{NA}}$ are mirror-blind (Section 4.7): they cannot distinguish a theory from its conjugate, so any chirality-dependent boundary physics is invisible to them; only $\mu$ is signed, and it can vanish even when parent and child have distinct braiding structures. Second, computing $f_{\mathrm{NA}}$ requires knowledge of the full simple-object set of the child; where the child is not fully classified, the index cannot be evaluated. Third, our analysis presumes a single condensate algebra $A = \mathbf{1} \oplus (\psi,\bar\psi)$; more intricate condensates with multiple generators could yield different $\kappa$ and $f_{\mathrm{NA}}$. Fourth, and importantly, the indices say nothing about **control and readout**: Ising anyon braiding generates only the Clifford group — a finite subgroup of unitary operations, insufficient for universal quantum computation by braiding alone — and readout proceeds by fusion-channel parity measurement, not by any quantity captured by $(\kappa, \mu, f_{\mathrm{NA}})$. The experimental Majorana programs [3], [4], [5] make this concrete: their observable of interest (a parity-sensitive signal) has no analogue among our indices. A user of the framework should therefore not read $\kappa = 4$ or $f_{\mathrm{NA}} = 0$ as statements about operational capability.

**Against ourselves.** One might argue that the Case III correction is a bookkeeping fix of limited conceptual import. We disagree in one respect and concede in another. We disagree because the corrected $\kappa = 4$ restores normality of the condensate, which is the property the classification table in [10] was meant to tabulate; the erroneous $\kappa = 14/4 = 3.5$ would have falsely flagged Case III as abnormal. We concede that $f_{\mathrm{NA}} = 0$ versus $1/3$ changes no structural conclusion, since the child is Abelian either way. A second self-criticism: the replacement of the heuristic "$\psi \sim 1$" boundary fusion rule by the module-category treatment ($\mathcal{C}_A^{\mathrm{loc}}$) is here an argument from consistency, not a full derivation; a complete super-modular treatment of the boundary would be needed to make it rigorous, and we have not constructed one. Third, the analogy to tachyon condensation [6] and the methodological borrowings from [7] and [9] are heuristic; they motivate the framework but do not constrain it.

**Open questions.** (i) Does $\mu = \nu \bmod 16$ extend to time-reversal-twinned (super-modular) members of the series, where $\Delta c$ is only defined modulo the mirror contribution? (ii) Is normality ($\kappa \in \mathbb{Z}_{>0}$) sufficient as well as necessary for a consistent bosonic condensate? (iii) Can a fourth, mirror-sensitive or readout-sensitive index be defined within the same categorical data, or is readout irreducibly outside the topological data? (iv) Is there a systematic classification of all condensate algebras for the sixteen-fold way, and how do the indices vary across that landscape?

## 7. Conclusion

We corrected the Case III computation of the two-index framework of [10]: the parent $\text{Ising} \times \overline{\text{Ising}}$ has $D_C^2 = 16$ (not $14$), the child toric code has $D_D^2 = 4$, and the resulting indices are $\kappa = 4$, $f_{\mathrm{NA}} = 0$, and $\mu = 0$. The correction restores the normality of the condensate and removes the spurious non-Abelian fraction $1/3$. By embedding the condensation in the module-category formalism of [2], we replace the heuristic boundary fusion rule "$\psi \sim 1$" with a mathematically grounded construction. We identified the chirality index $\mu = 2\,\Delta c$ with Kitaev's sixteen-fold way label $\nu \bmod 16$, verified at $\nu = 0$ and $\nu = 1$ and projected across the series, proved a restricted completeness statement within that series, and delimited what the indices cannot see: mirror asymmetry (invisible to $\kappa$ and $f_{\mathrm{NA}}$) and operational control and readout (invisible to all three). These results sharpen the quantitative bulk-boundary map for anyon condensation and define concrete targets — mirror-sensitive diagnostics and exhaustive counterexample searches — for completing the classification program initiated in [10].

## References

[1] Bosonic topological phases of matter: bulk-boundary correspondence, SPT invariants and gauging. arXiv:1710.04730v1. https://arxiv.org/abs/1710.04730v1
[2] Anyon condensation and tensor categories. arXiv:1307.8244v7. https://arxiv.org/abs/1307.8244v7
[3] The MAJORANA Experiment. arXiv:1109.4790v1. https://arxiv.org/abs/1109.4790v1
[4] White Paper on the Majorana Zero-Neutrino Double-Beta Decay Experiment. arXiv:nucl-ex/0311013v1. https://arxiv.org/abs/nucl-ex/0311013v1
[5] TThe {\sc Majorana} Project. arXiv:0910.4598v1. https://arxiv.org/abs/0910.4598v1
[6] Tachyon condensation and Boundary States in Bosonic String. arXiv:hep-th/0001044v1. https://arxiv.org/abs/hep-th/0001044v1
[7] Analyzing complex functional brain networks: fusing statistics and network science to understand the brain. arXiv:1302.5721v3. https://arxiv.org/abs/1302.5721v3
[8] Introduction to abelian and non-abelian anyons. arXiv:1610.09260v1. https://arxiv.org/abs/1610.09260v1
[9] Equivalence of distance-based and RKHS-based statistics in hypothesis testing. arXiv:1207.6076v3. https://arxiv.org/abs/1207.6076v3
[10] https://papers.qnfo.org/papers/a-two-index-framework-for-the-bulk-boundary-correspondence-of-anyon-condensation/. QNFO: A Two-Index Framework for the Bulk-Boundary Correspondence of Anyon Condensation and Boundary Majorana Statistics.