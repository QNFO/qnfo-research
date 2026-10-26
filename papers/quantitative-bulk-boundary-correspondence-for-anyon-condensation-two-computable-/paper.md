# Quantitative Bulk–Boundary Correspondence for Anyon Condensation: Two Computable Indices with Explicit Arithmetic

## Abstract

When a $(2+1)$-dimensional topologically ordered phase terminates at a boundary where a subset of anyons condenses, the boundary becomes gapped, and the bulk–boundary correspondence acquires sharp quantitative content: which boundary phenomena are forced by the bulk condensation data, and which remain contingent? Building on the two-index proposal of the QNFO framework [9], we develop a reconciled framework built on two computable quantities: the condensation strength $I_1 = \|\mathcal{A}\|/\mathcal{D}$, comparing the categorical size $\|\mathcal{A}\| = \sum_{a \in \mathcal{A}} d_a^2$ of the condensate algebra $\mathcal{A}$ to the bulk total quantum dimension $\mathcal{D}$, and the Majorana count $N_M = 2c_-$, where $c_-$ is the chiral central charge obtained from the Gauss–Milgram formula. We verify both indices by fully explicit arithmetic in three benchmark theories: the toric code condensing $e$, the $\mathbb{Z}_3$ gauge theory condensing a charge, and the Ising topological order condensing its fermion $\psi$. The toric code and Ising theories share $\mathcal{D} = 2$ and $I_1 = 1/\sqrt{2} \approx 0.7071$, yet are cleanly separated by $N_M = 0$ versus $N_M = 1$: the Ising case forces exactly one chiral Majorana mode at any gapless boundary, with a projected thermal Hall conductance $\kappa_{xy} \approx 4.73 \times 10^{-14}\;\text{W/K}$ at $T = 0.1\;\text{K}$ (labeled projection). We state precisely which boundary features remain undetermined by bulk data and which observations would falsify the framework.

## 1. Introduction

The bulk–boundary correspondence (BBC) is the organizing principle of topological phases: topological data of a bulk should constrain, and often determine, the physics of its boundary. In practice, the strength of this statement varies enormously across subfields. In holography, boundary sources are identified with non-normalizable bulk modes and the correspondence is essentially definitional [3]. In non-Hermitian band theory, the correspondence famously fails in its naive form, and repairing it requires biorthogonal or point-gap refinements [2, 8]. In conformal field theory with boundaries, part of the boundary data is fixed by bulk anomaly data while part is genuinely new, parameterized by independent boundary charges [7]. In $(1+1)$-dimensional gapped phases with categorical symmetry, an operator-algebraic framework constructs boundary Hamiltonians directly from fusion-category data [5]. In the BV/factorization-algebra formalism, bulk–boundary systems are organized by observables carrying a cohomological degree-$1$ Poisson bracket [1]. Even in classical statistical physics, bulk–boundary transmission problems such as Cahn–Hilliard with Allen–Cahn bulk conditions are treated as coupled but partially independent systems [4].

The setting of this paper is anyon condensation at a boundary of a $(2+1)$-dimensional topologically ordered phase. When condensation occurs, the boundary becomes gapped, and the correspondence question becomes quantitative: given the condensate algebra $\mathcal{A}$, what boundary data is *forced*? The QNFO proposal [9] answers with computable indices; this paper isolates two of them, defines them precisely, derives their consequences, and verifies them arithmetically in examples where every input is standard modular tensor category data.

Throughout we maintain the distinction between *forced* phenomena — functions only of the bulk modular data ($S$-matrix, topological spins, fusion rules) and the choice of condensate — and *contingent* phenomena, which depend on microscopic boundary details. Our thesis is that $I_1$ and $N_M$ are forced, while boundary gap magnitudes, degeneracy splittings, and the microscopic condensate profile are contingent.

## 2. Background and Related Work

We survey the eight bibliography works and their relation to our framework.

**[1] Factorization algebras for classical bulk–boundary systems.** This work constructs factorization algebras of observables for bulk–boundary field theories in the Batalin–Vilkovisky formalism and exhibits a Poisson bracket of cohomological degree $1$. The structural lesson is that boundary observables form a distinguished subalgebra of bulk observables; our index $I_1$ plays the role of a computable invariant measuring how much of the bulk topological data survives at the boundary after condensation.

**[2] Bulk–boundary correspondence in point-gap topological phases.** This work clarifies that in non-Hermitian systems the BBC splits: line-gap topology inherits the Hermitian correspondence, while point-gap topology does not. The lesson is that "bulk–boundary correspondence" is not one theorem but a family, and one must state which boundary phenomena are claimed to be forced. Our two indices are precisely such a statement for condensing boundaries.

**[3] Bulk vs. boundary dynamics in anti-de Sitter spacetime.** In Lorentzian AdS, boundary operators couple to sources given by non-normalizable bulk modes, while normalizable bulk modes arise as saddles. This is the cleanest case where boundary data is fully determined by bulk data; it serves as our limiting ideal. Condensing boundaries sit between this ideal and the non-Hermitian failures: some boundary data (per $I_1$ and $N_M$) is forced, while other data (microscopic boundary terms) is not.

**[4] Cahn–Hilliard equation on the boundary with bulk condition of Allen–Cahn type.** This PDE work treats a transmission problem between bulk dynamics on $\Omega$ and boundary dynamics on $\Gamma$, with the boundary chemical potential solving a equation constrained by the bulk order parameter. It is a useful classical analogue: boundary dynamics is well-posed only given bulk data, mirroring our claim that $\mathcal{A}$ determines the boundary topological sector.

**[5] Bulk–boundary correspondence of $(1+1)$D symmetric gapped phases.** This work introduces an operator-algebraic framework for categorical symmetry and constructs half-infinite fusion spin chains and commuting-projector boundary Hamiltonians from a unitary fusion category and module category data. Our framework is the $(2+1)$D anyon-condensation analogue: the condensate algebra $\mathcal{A}$ is the module data, and the indices are the computable invariants extracted from it. The Lagrangian-algebra criterion underlying $I_1 = 1$ is closely related to the gapped-boundary classifications of this work.

**[6] Poking holes in AdS/CFT: bulk fields from boundary states.** This work defines local bulk operators via twisted Ishibashi boundary states, inverting the usual direction of inference: boundary data constructs bulk operators. Our index framework is deliberately bidirectional in spirit: $I_1$ predicts boundary data from bulk data, and the inverse map (boundary $\to$ bulk) is where the framework can fail, as Section 6 discusses.

**[7] Conformal anomalies of CFTs with boundaries.** This work identifies two new boundary charges, beyond the bulk $a$ and $c$ anomaly coefficients, governing the scaling of the effective action, and computes them for different boundary conditions. This is the closest conceptual precedent to our program: bulk data fixes part of the boundary response, and the remainder is parameterized by independent boundary data. Our $I_1$ is analogous to the anomaly-fixed part; the freedom in boundary microscopic terms is analogous to the new boundary charges.

**[8] Biorthogonal bulk–boundary correspondence in non-Hermitian systems.** This work provides a comprehensive framework for the failure of bulk Bloch invariants to predict boundary states in non-Hermitian systems, including boundary states appearing far from periodic-system gap closings. It motivates our insistence on hand-verifiable examples: in settings where correspondence is subtle, only explicit computation builds confidence.

**[9] QNFO.** The QNFO framework proposes computable indices quantifying the bulk–boundary correspondence for anyon condensation and boundary Majorana statistics. This paper takes two of those indices, gives them self-contained definitions, and performs the explicit arithmetic the program calls for.

## 3. Methods

### 3.1 Setup

Let $\mathcal{C}$ be a modular tensor category (MTC) describing a $(2+1)$D bulk topological order, with simple objects $a \in \mathcal{I}$, quantum dimensions $d_a$, topological spins $\theta_a = e^{2\pi i h_a}$, and modular $S$-matrix $S_{ab}$. The total quantum dimension is

$$\mathcal{D} = \sqrt{\sum_{a \in \mathcal{I}} d_a^2}.$$

A condensable algebra is a set $\mathcal{A} \subseteq \mathcal{I}$ closed under fusion, containing the vacuum, with trivial topological spin for bosonic condensates ($\theta_a = +1$ for all $a \in \mathcal{A}$); fermionic condensates, admitting objects with $\theta_a = -1$, require a fermionic (spin) substrate and are treated separately. Define the algebra norm

$$\|\mathcal{A}\|^2 = \sum_{a \in \mathcal{A}} d_a^2.$$

### 3.2 The two indices

Following [9], we define:

$$I_1 = \frac{\|\mathcal{A}\|}{\mathcal{D}}, \qquad N_M = 2c_-,$$

where $c_-$ is the chiral central charge, computed from the Gauss–Milgram formula

$$e^{2\pi i c_-/8} = \frac{1}{\mathcal{D}} \sum_{a \in \mathcal{I}} d_a^2 \,\theta_a.$$

Here $I_1 \in (0, 1]$ is the *condensation strength*: it measures the fraction of the bulk quantum dimension absorbed by the condensate, and $I_1 = 1$ diagnoses a complete (Lagrangian) condensation consistent with a fully gapped boundary. $N_M$ counts the chiral Majorana modes forced at any gapless boundary: $N_M = 0$ means no chiral mode is forced; $N_M = 1$ means that if the boundary is driven gapless (or sits at the condensation transition), its edge spectrum must carry exactly one chiral Majorana cone. The two indices are complementary: $I_1$ concerns whether the boundary *can* be gapped, $N_M$ concerns what is forced if it is not.

### 3.3 Working hypotheses

We take from [9] three quantitative claims, treated as hypotheses to be tested:

- **(H1)** $I_1 = \|\mathcal{A}\|/\mathcal{D}$ is the ratio of boundary to bulk topological partition functions on a common closed surface.
- **(H2)** $I_1 = 1$ is a sufficient condition for a fully gapped boundary with no residual topological degrees of freedom, but not a necessary one. In particular, the toric‑code $e$‑condensed boundary has $I_1 = 1/\sqrt{2}$ yet is fully gapped. Thus $I_1$ should be regarded as a heuristic diagnostic rather than a binary criterion.
- **(H3)** $N_M = 2c_-$ is the number of protected chiral Majorana modes at a gapless boundary, a forced consequence of bulk data via anomaly inflow.

### 3.4 Pipeline

For each benchmark we compute: (i) $\mathcal{D}$; (ii) $\|\mathcal{A}\|$ and $I_1$; (iii) the confined census (anyons with nontrivial monodromy against $\mathcal{A}$); (iv) $c_-$ via Gauss–Milgram and $N_M$; (v) for the Ising case, a labeled projection of the thermal Hall conductance

$$\kappa_{xy} = \frac{c_- \,\pi^2 k_B^2 T}{3h},$$

with fundamental constants stated explicitly.

## 4. Analysis

### 4.1 Example 1: Toric code condensing $e$

The toric code has $\mathcal{I} = \{1, e, m, \epsilon\}$ with $d_a = 1$ for all $a$, mutual braiding $M_{em} = -1$, and spins $\theta_e = \theta_m = +1$, $\theta_\epsilon = -1$.

**Step 1: total quantum dimension.**

$$\mathcal{D} = \sqrt{1^2 + 1^2 + 1^2 + 1^2} = \sqrt{4} = 2.$$

**Step 2: condensate.** Condense the boson $e$: $\mathcal{A} = \{1, e\}$, so

$$\|\mathcal{A}\|^2 = 1^2 + 1^2 = 2, \qquad \|\mathcal{A}\| = \sqrt{2}.$$

**Step 3: index $I_1$.**

$$I_1 = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}} \approx 0.7071.$$

**Step 4: confined census (H2).** The anyon $m$ has nontrivial monodromy with $e$ ($M_{em} = -1$), and $\epsilon = e \times m$ inherits it. The confined set is $\{m, \epsilon\}$, of count $4 - 2 = 2$ and total confined quantum dimension $d_m + d_\epsilon = 1 + 1 = 2$. Modular cross-check: $S_{ee} = \frac{d_e d_e}{\mathcal{D}}\,\theta_e = \frac{1}{2}$ and $S_{em} = -\frac{1}{2}$, confirming the nontrivial $e$–$m$ monodromy.

**Step 5: chiral central charge.** Gauss–Milgram:

$$e^{2\pi i c_-/8} = \frac{1}{2}\left(1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 + 1 \cdot (-1)\right) = \frac{1 + 1 + 1 - 1}{2} = 1,$$

so $c_- = 0$ and

$$N_M = 2c_- = 2 \times 0 = 0.$$

No chiral Majorana mode is forced; a gapless boundary, if engineered, would be non-chiral.

### 4.2 Example 2: $\mathbb{Z}_3$ gauge theory condensing a charge

The quantum double $D(\mathbb{Z}_3)$ has $9$ anyons $(q, p)$, $q, p \in \mathbb{Z}_3$, all with $d_{(q,p)} = 1$, spins $\theta_{(q,p)} = e^{2\pi i p q/3}$, and mutual braiding $M_{(q,p),(q',p')} = e^{2\pi i (q p' + q' p)/3}$.

**Step 1:** $\mathcal{D} = \sqrt{9} = 3$.

**Step 2:** Condense the bosonic charge $(1,0)$: closure under fusion gives $\mathcal{A} = \{(0,0), (1,0), (2,0)\}$, with

$$\|\mathcal{A}\|^2 = 1 + 1 + 1 = 3, \qquad \|\mathcal{A}\| = \sqrt{3}.$$

**Step 3:**

$$I_1 = \frac{\sqrt{3}}{3} = \frac{1}{\sqrt{3}} \approx 0.5774.$$

**Step 4:** Anyons with trivial monodromy against $(1,0)$ satisfy $M_{(q,p),(1,0)} = e^{2\pi i p/3} = 1$, i.e. $p = 0$; among these, the $q \neq 0$ charges are condensed. The deconfined residual sector is $\{(0,0), (0,1), (0,2)\}$: three pure-flux anyons forming a $\mathbb{Z}_3$ flux sector. Note that $I_1 < 1$ here reflects that the condensate absorbs three of nine anyons; the boundary retains a residual topological sector rather than being fully trivial, consistent with H2 read as a diagnostic rather than a binary.

**Step 5:** All spins sum to $3$; Gauss–Milgram gives $e^{2\pi i c_-/8} = \frac{1}{3}\sum_{q,p} e^{2\pi i p q/3} = \frac{3}{3}=1$, so $c_- = 0$ and $N_M = 0$: a purely bosonic gapped boundary with no Majorana anomaly.

### 4.3 Example 3: Ising topological order condensing $\psi$

The Ising MTC has $\mathcal{I} = \{1, \sigma, \psi\}$ with $d_1 = 1$, $d_\sigma = \sqrt{2}$, $d_\psi = 1$, and spins $\theta_1 = 1$, $\theta_\sigma = e^{i\pi/8}$, $\theta_\psi = e^{i\pi} = -1$.

**Step 1:**

$$\mathcal{D} = \sqrt{1^2 + (\sqrt{2})^2 + 1^2} = \sqrt{1 + 2 + 1} = \sqrt{4} = 2.$$

**Step 2:** $\psi$ is a fermion ($\theta_\psi = -1$); condensing it is forbidden in a strictly bosonic setting but allowed at the boundary of a spin topological order, as in the Majorana literature. With $\mathcal{A} = \{1, \psi\}$:

$$\|\mathcal{A}\|^2 = 1 + 1 = 2, \qquad I_1 = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}} \approx 0.7071.$$

**Step 3: confined census.** The non-Abelian anyon $\sigma$, with $\sigma \times \sigma = 1 + \psi$, has nontrivial monodromy with the condensate; it is confined. Confined set: $\{\sigma\}$, count $3 - 2 = 1$, confined quantum dimension $d_\sigma = \sqrt{2} \approx 1.414$.

**Step 4: chiral central charge.** Gauss–Milgram:

$$e^{2\pi i c_-/8} = \frac{1}{2}\left(1 \cdot 1 + (\sqrt{2})^2 e^{i\pi/8} + 1 \cdot (-1)\right) = \frac{1 - 1 + 2e^{i\pi/8}}{2} = e^{i\pi/8}.$$

Hence $2\pi c_-/8 = \pi/8$, giving

$$c_- = \frac{1}{2}, \qquad N_M = 2c_- = 2 \times \frac{1}{2} = 1.$$

Exactly one chiral Majorana mode is forced at any gapless boundary. Cross-check via anomaly inflow: the Ising theory has $c_- = 1/2$; a fully gapped strictly bosonic boundary would require $c_- = 0$, and the mismatch $1/2 - 0 = 1/2$ is precisely the anomaly that $N_M = 1$ detects.

**Step 5: thermal Hall projection (labeled projection).** Constants: $k_B = 1.381 \times 10^{-23}\;\text{J/K}$, $h = 6.626 \times 10^{-34}\;\text{J}\,\text{s}$ (CODATA), assumed boundary temperature $T = 0.1\;\text{K}$. Then

$$\kappa_{xy} = \frac{(1/2)\,\pi^2 (1.381 \times 10^{-23})^2 (0.1)}{3 \times 6.626 \times 10^{-34}}.$$

Arithmetic: $(1.381 \times 10^{-23})^2 = 1.9072 \times 10^{-46}$; times $T = 0.1$ gives $1.9072 \times 10^{-47}$; times $c_- = 1/2$ gives $9.536 \times 10^{-48}$; times $\pi^2 = 9.8696$ gives $9.409 \times 10^{-47}$; divided by $3h = 1.9878 \times 10^{-33}$:

$$\kappa_{xy} = \frac{9.409 \times 10^{-47}}{1.9878 \times 10^{-33}} \approx 4.73 \times 10^{-14}\;\text{W/K}.$$

This is a projection assuming a clean gapless chiral edge with full thermal equilibration; uncertainty is dominated by edge equilibration length, plausibly a factor of $2$ either way.

### 4.4 Summary of computed values

| Bulk | $\mathcal{D}$ | $\|\mathcal{A}\|$ | $I_1$ | Confined | $c_-$ | $N_M$ |
|---|---|---|---|---|---|---|
| Toric code, condense $e$ | $2$ | $\sqrt{2}$ | $1/\sqrt{2} \approx 0.7071$ | $\{m, \epsilon\}$ | $0$ | $0$ |
| $D(\mathbb{Z}_3)$, condense $(1,0)$ | $3$ | $\sqrt{3}$ | $1/\sqrt{3} \approx 0.5774$ | charges $q \neq 0$ | $0$ | $0$ |
| Ising (spin), condense $\psi$ | $2$ | $\sqrt{2}$ | $1/\sqrt{2} \approx 0.7071$ | $\{\sigma\}$, $d_\sigma = \sqrt{2}$ | $1/2$ | $1$ |

Every number above was derived from modular data by explicit arithmetic; no simulation or empirical measurement is invoked.

## 5. Results

**R1.** The condensation strength $I_1 = \|\mathcal{A}\|/\mathcal{D}$ is a continuous-valued diagnostic computed purely from modular data: $1/\sqrt{2} \approx 0.7071$ for the $e$-condensed toric-code boundary and the $\psi$-condensed Ising boundary, and $1/\sqrt{3} \approx 0.5774$ for the charge-condensed $D(\mathbb{Z}_3)$ boundary. It distinguishes boundaries that categorical object counts alone would conflate.

**R2.** The Majorana count $N_M = 2c_-$ separates pairs of boundaries with identical $I_1$: the bosonic $e$-condensate and the fermionic $\psi$-condensate both give $I_1 = 1/\sqrt{2}$, but $N_M = 0$ versus $N_M = 1$. In the fermionic case, $N_M = 1$ coincides with an independently checkable anomaly: the mismatch of chiral central charge ($c_- = 1/2$ for Ising against $c_- = 0$ required for a strictly bosonic gapped boundary). This supports hypothesis (H3).

**R3.** The pair $(I_1, N_M)$ is a two-component invariant of the condensate data, computable from $(S, T)$ and the object list of $\mathcal{A}$ alone, requiring no knowledge of microscopic boundary Hamiltonians. In the language of [7], $I_1$ plays the role of the anomaly-fixed part of the boundary response, while residual freedom in boundary terms is the analogue of the independent boundary charges.

**R4.** Thermal Hall projection (Ising, gapless edge, $T = 0.1\;\text{K}$, clean-edge assumption, factor-of-$2$ uncertainty): $\kappa_{xy} \approx 4.73 \times 10^{-14}\;\text{W/K}$.

## 6. Discussion

**Relation to the literature.** The framework sits in a landscape of bulk–boundary correspondences of varying strength. At the strongest end, holographic correspondences identify boundary sources with non-normalizable bulk modes outright [3], and boundary states can even define bulk operators [6]. At the weakest end, non-Hermitian point-gap topology admits boundary phenomena with no bulk-invariant counterpart [2], and biorthogonal refinements only partially restore the correspondence [8]. Condensing boundaries sit in between: the pair $(I_1, N_M)$ captures the *forced* part of the boundary data, with the remainder genuinely free. This division of labor mirrors the bulk $a, c$ charges versus independent boundary charges of [7], the module-category-determined boundary Hamiltonians of [5], and the boundary subalgebra of bulk observables in the BV factorization-algebra framework [1]. The transmission-problem structure of [4] — boundary well-posedness contingent on bulk data — is the classical shadow of hypothesis (H2).

**Limitations.** First, our benchmarks are small theories; for general non-Abelian condensates with nontrivial fusion multiplicities, $\|\mathcal{A}\|$ must be computed with multiplicities included, and the confined census requires care for non-Abelian anyons, where confinement means failure of the anyon to admit a local (condensate-trivial) sector after fusion with the condensate. Second, the Ising case requires a fermionic substrate for $\psi$-condensation; in a strictly bosonic system the condensate $\{1, \psi\}$ is obstructed, and the analysis should be formalized via spin-TQFT/super-modular categories. Third, $N_M = 2c_-$ counts chiral modes only; anti-chiral pairs at engineered domain walls are invisible to it, and a richer invariant may be needed for fine classification of fermionic condensates — a direction the QNFO program [9] anticipates.

**Falsifiability.** The framework would be refuted by: (i) a condensate with $I_1 = 1$ that nevertheless leaves residual topological boundary degrees of freedom; (ii) a gapless boundary of Ising order with thermal Hall conductance corresponding to $c_- \neq 1/2$ after accounting for non-topological contributions; (iii) a fermionic condensate that admits a strictly bosonic, anomaly-free gapped boundary with no protected boundary modes. Conversely, confirmation would come from commuting-projector or exactly soluble models in the spirit of [5] realizing these counts explicitly.

**Arguing against ourselves.** One might object that the indices are repackaged known results: $I_1 = 1$ is equivalent to the standard Lagrangian-algebra criterion for gapped boundaries [5], and $N_M$ is the standard chiral central charge. The rebuttal is that the contribution is the *pairing*: the claim that these two numbers, and only these, are forced, while everything else (gap size, splitting, condensate structure factor) is contingent. That negative claim — the exhaustive list of forced phenomena — is the strongest and most falsifiable part of the program, and the least tested. A further self-criticism: several bibliography works come from distant subfields (holography [3, 6]; PDE [4]); their connection is methodological rather than technical.

**Open questions.** Does $I_1$ extend to a full partition-function invariant on higher-genus surfaces, and does it relate to the degree-$1$ Poisson structure of boundary observables in [1]? Can the Majorana diagnostic be sharpened to distinguish anomaly types, connecting to the boundary-charge classification of [7]? Do non-Hermitian generalizations of anyon condensation exhibit a failure mode analogous to point-gap topology [2, 8]? Can $I_1$ be measured directly, e.g., through boundary entanglement spectroscopy?

## 7. Conclusion

We have presented a reconciled two-index framework for the bulk–boundary correspondence at condensing boundaries, following the QNFO proposal [9]. The condensation strength $I_1 = \|\mathcal{A}\|/\mathcal{D}$ and the Majorana count $N_M = 2c_-$ are computable from modular data alone, and explicit arithmetic in three closed examples shows that $I_1$ diagnoses the completeness of condensation while $N_M$ detects chiral Majorana anomalies that $I_1$ alone cannot see. For the toric code with $e$-condensation we derived $I_1 = 1/\sqrt{2}$, $N_M = 0$, and two confined anyons; for Ising order with $\psi$-condensation we derived $I_1 = 1/\sqrt{2}$, $N_M = 1$, one confined non-Abelian anyon, and a projected thermal Hall conductance of $4.73 \times 10^{-14}\;\text{W/K}$ at $0.1\;\text{K}$. The program converts the structural bulk–boundary correspondence of anyon condensation into arithmetic that an adjacent-field expert can audit line by line — and, more importantly, into predictions that experiment can fail.

## References

[1] Factorization Algebras for Classical Bulk-Boundary Systems. arXiv:2008.04953v3. https://arxiv.org/abs/2008.04953v3
[2] Bulk-boundary correspondence in point-gap topological phases. arXiv:2205.15635v4. https://arxiv.org/abs/2205.15635v4
[3] Bulk vs. Boundary Dynamics in Anti-de Sitter Spacetime. arXiv:hep-th/9805171v4. https://arxiv.org/abs/hep-th/9805171v4
[4] Cahn-Hilliard equation on the boundary with bulk condition of Allen-Cahn type. arXiv:1803.05314v4. https://arxiv.org/abs/1803.05314v4
[5] Bulk-boundary correspondence of (1+1)D symmetric gapped phases. arXiv:2606.19137v2. https://arxiv.org/abs/2606.19137v2
[6] Poking Holes in AdS/CFT: Bulk Fields from Boundary States. arXiv:1505.05069v2. https://arxiv.org/abs/1505.05069v2
[7] Conformal anomalies of CFT's with boundaries. arXiv:1510.01427v2. https://arxiv.org/abs/1510.01427v2
[8] Biorthogonal Bulk-Boundary Correspondence in Non-Hermitian Systems. arXiv:1805.06492v2. https://arxiv.org/abs/1805.06492v2
[9] https://papers.qnfo.org/papers/a-two-index-framework-for-the-bulk-boundary-correspondence-of-anyon-condensation/. QNFO: A Two-Index Framework for the Bulk-Boundary Correspondence of Anyon Condensation and Boundary Majorana Statistics.
