# Bosonic Barrier Penetration and the Combinatorial Landscape of Cellular Automata Models for UV‑Mediated Cellular Communication

## Abstract
Biological membranes block macroscopic fermionic matter yet allow ultraviolet (UV) photons to pass, prompting speculation that bosonic statistics confer a signaling advantage. The gap is quantitative: no study has simultaneously evaluated (i) the transmission probability of UV photons through cellular barriers using a physically grounded absorption model, (ii) the tunneling probability of a representative fermion (proton) through the same barrier, and (iii) the size of the rule‑space in binary cellular automata (CA) that could abstract such transport. We adopt (a) Beer–Lambert attenuation for photon propagation with explicitly stated absorption coefficients, (b) the Wentzel–Kramers–Brillouin (WKB) formula for proton tunneling, and (c) combinatorial formulas for CA rule‑space and configuration‑space sizes. The analysis yields a membrane photon transmission $T_m=0.995$, a cytoplasmic transmission $T_c=4.54\times10^{-5}$, a total photon transmission $T_{\mathrm{tot}}=4.52\times10^{-5}$, a proton tunneling probability $T_p\approx10^{-953}$, and a bosonic–fermionic advantage ratio $\approx10^{953}$. In parallel, the full Moore‑neighbourhood rule‑space contains $2^{512}\approx1.35\times10^{154}$ rules, the isotropic subset $2^{102}\approx5.07\times10^{30}$, and a $61\times61$ binary lattice admits $2^{3721}\approx1.00\times10^{1120}$ configurations. These results show that exhaustive CA exploration is astronomically infeasible, while photon transmission across a membrane is high but cytoplasmic absorption severely limits signaling range. The work redirects modelers toward hypothesis‑driven CA rule selection and highlights the need for empirical measurement of intracellular UV absorption.

## 1. Introduction
Cellular membranes act as effective barriers to macroscopic fermionic particles such as ions and proteins; maintaining ion gradients across these barriers incurs a substantial energetic cost and underlies intracellular signaling regulation. Ultraviolet (UV) photons, by contrast, are routinely observed to traverse membranes, participating in DNA‑damage repair and hypothesized intercellular communication pathways. The practical problem is that existing biophysical models lack a quantitative transmission probability for UV photons, preventing designers of engineered photonic therapies from assessing whether UV channels can reliably convey signals over biologically relevant distances without inducing phototoxic damage. Simultaneously, researchers employing binary cellular automata (CA) as abstract substrates for cellular communication face a combinatorial explosion of possible rule‑sets, making exhaustive exploration of dynamics infeasible.

If bosonic UV photons indeed enjoy a transmission advantage over fermionic carriers, a quantitative model must (a) provide a non‑negligible transmission probability through typical lipid bilayers and cytoplasm, and (b) relate this advantage to the size of the CA rule‑space that could encode such transport. Demonstrating these points would enable synthetic‑tissue designers to embed UV‑transparent pathways and clinicians to calibrate UV‑based diagnostics with confidence in photon delivery.

**Contributions.**
- **C1.** Derivation of the membrane photon transmission $T_m=0.995$ using Beer–Lambert attenuation (Section 4.1).  
- **C2.** Derivation of the cytoplasmic photon transmission $T_c=4.54\times10^{-5}$ (Section 4.2).  
- **C3.** Computation of the total photon transmission $T_{\mathrm{tot}}=4.52\times10^{-5}$ (Section 4.3).  
- **C4.** WKB derivation of proton tunneling probability $T_p\approx10^{-953}$ and the bosonic–fermionic ratio $\approx10^{953}$ (Section 4.4–4.5).  
- **C5.** Derivation of the full Moore‑neighbourhood CA rule‑space $2^{512}\approx1.35\times10^{154}$ (Section 4.6).  
- **C6.** Computation of the isotropic rule‑space $2^{102}\approx5.07\times10^{30}$ (Section 4.7).  
- **C7.** Estimation of the binary configuration space for a $61\times61$ lattice $2^{3721}\approx1.00\times10^{1120}$ (Section 4.8).  
- **C8.** Identification of practical implications for CA‑based modelers and a minimal pilot experiment (Section 7).  

## 2. Background and Related Work
Cellular automata (CA) have long served as abstract models for spatially distributed processes, including biological signaling. The eight works below provide the quantitative foundations for our analysis.

1. **Classification of elementary CA.** The authors enumerate eight specific rules belonging to Class I (e.g., 0, 8, 32, 40, 128, 136, 160, 168) [1]. This demonstrates that even low‑dimensional CA admit a finite, countable set of behaviours.

2. **The X‑rule and rule‑space size.** For a binary 2‑D CA with a Moore neighbourhood (9 neighbours), the full lookup‑table contains $2^{9}=512$ output bits, yielding a rule‑space of $2^{512}$ possible rules; restricting to isotropic rules reduces the effective space to $2^{102}$ [2].

3. **Isotropic iso‑rule paradigm.** The authors formalise the rule‑table size $S$ and show that for binary isotropic CA the rule‑space size follows $v^{S}$ with $v=2$; they confirm that isotropic rule‑spaces are dramatically smaller than full rule‑spaces [3].

4. **Decidability of CA properties.** Sutner’s result on the decidability of first‑order properties of the phase‑space $\mathcal{S}_{\mathcal{A}}$ underscores that certain global questions about CA dynamics are algorithmically tractable, yet the sheer number of possible rules remains a practical obstacle [4].

5. **Human body blockage model for mmWave.** The paper reports that millimeter‑wave frequencies up to $60\ \text{GHz}$ support data rates exceeding $50\ \text{Gbps}$, illustrating how physical propagation models can be parameterised by frequency, bandwidth, and path loss [5].

6. **Asynchronous CA updating schemes.** The authors define a probability $\alpha$ for a cell to update at each time step, providing a stochastic framework that can be mapped onto photon‑absorption probabilities in a probabilistic CA model of UV transmission [6].

7. **Stochastic CA decomposition.** The work introduces a state set $\mathcal{S}$ of size $N>1$ and a cell count $M$, establishing that the configuration space size is $N^{M}$; for binary states ($N=2$) and a $61\times61$ lattice ($M=3721$), the space size is $2^{3721}$ [7].

8. **Probabilistic CA for granular media.** The authors implement a $61\times61$ grid to simulate sandpile dynamics, confirming that such grid sizes are computationally tractable for visualisation while still representing astronomically large state spaces [8].

These works collectively supply rule‑table sizes, neighbourhood counts, lattice dimensions, and stochastic update concepts that we employ to quantify the combinatorial landscape relevant to UV‑photon CA models.

## 3. Methods
Our approach consists of three analytical components.

1. **Photon attenuation model.** We treat each biological layer as a homogeneous absorber of thickness $d$ with absorption coefficient $\mu$ (units $\text{cm}^{-1}$). The Beer–Lambert law gives the transmission
   $$
   T(d)=e^{-\mu d}.
   $$
   The membrane and cytoplasm are modeled as two absorbers in series, so the total transmission is the product $T_{\mathrm{tot}}=T_m\,T_c$.

2. **Fermionic tunneling model.** For a proton of mass $m_p$ encountering a rectangular potential barrier of height $V>E$ and width $d$, the Wentzel–Kramers–Brillouin (WKB) approximation yields
   $$
   T_f = e^{-2\kappa d},\qquad
   \kappa = \frac{\sqrt{2m_p\,(V-E)}}{\hbar}.
   $$

3. **Cellular‑automaton abstraction.** We map the transport problem onto a binary CA where each cell encodes photon presence (1) or absorption (0). Three rule‑space regimes are considered:
   - **Full rule‑space:** $2^{512}$ binary rules for a Moore neighbourhood.
   - **Isotropic rule‑space:** $2^{102}$ rules respecting rotational symmetry.
   - **Finite lattice space:** $2^{M}$ configurations on a $61\times61$ lattice ($M=3721$).

All calculations are performed analytically; no simulations or experiments are conducted. Assumptions that are not taken from the cited literature are listed explicitly in Section 3.4.

### 3.4 Assumption register
- $A_1$: membrane absorption coefficient $\mu_m = 10^{4}\ \text{cm}^{-1}$ at $\lambda=280\ \text{nm}$ (conservative estimate).  
- $A_2$: cytoplasmic absorption coefficient $\mu_c = 10^{4}\ \text{cm}^{-1}$ at $\lambda=280\ \text{nm}$.  
- $A_3$: membrane thickness $d_m = 5\ \text{nm}=5\times10^{-7}\ \text{cm}$.  
- $A_4$: cytoplasmic path length $d_c = 10\ \mu\text{m}=10^{-3}\ \text{cm}$.  
- $A_5$: proton barrier height excess $\Delta E = V-E = 1\ \text{eV}=1.602\times10^{-19}\ \text{J}$.  
- $A_6$: proton mass $m_p = 1.6726\times10^{-27}\ \text{kg}$.  
- $A_7$: reduced Planck constant $\hbar = 1.0546\times10^{-34}\ \text{J·s}$.  

## 4. Analysis
### 4.1 Membrane photon transmission
Using $A_1$ and $A_3$:
\[
\mu_m d_m = (10^{4}\ \text{cm}^{-1})(5\times10^{-7}\ \text{cm}) = 5\times10^{-3}.
\]
\[
T_m = e^{-5\times10^{-3}}.
\]
Expanding the exponential to three terms:
\[
e^{-0.005}=1-0.005+\frac{0.005^{2}}{2}=1-0.005+0.0000125=0.9950125.
\]
Thus
\[
T_m \approx 0.995.
\]

### 4.2 Cytoplasmic photon transmission
Using $A_2$ and $A_4$:
\[
\mu_c d_c = (10^{4}\ \text{cm}^{-1})(10^{-3}\ \text{cm}) = 10.
\]
\[
T_c = e^{-10}.
\]
Since $e^{10}=22026.4658$, we obtain
\[
T_c = \frac{1}{22026.4658}=4.539993\times10^{-5}.
\]

### 4.3 Total photon transmission
\[
T_{\mathrm{tot}} = T_m \times T_c = 0.9950125 \times 4.539993\times10^{-5}.
\]
Multiplying:
\[
0.9950125 \times 4.539993 = 4.517350 \quad (\text{to six decimal places}),
\]
so
\[
T_{\mathrm{tot}} = 4.517350\times10^{-5}\approx4.52\times10^{-5}.
\]

### 4.4 Proton tunneling through the membrane
From $A_5$–$A_7$ and $A_3$ (converted to meters: $d_m=5\times10^{-9}\ \text{m}$):
\[
2m_p\Delta E = 2(1.6726\times10^{-27}\ \text{kg})(1.602\times10^{-19}\ \text{J})
=5.3591\times10^{-46}\ \text{kg·J}.
\]
\[
\sqrt{2m_p\Delta E}= \sqrt{5.3591\times10^{-46}} = 2.3150\times10^{-23}\ \text{kg}^{1/2}\!\text{J}^{1/2}.
\]
\[
\kappa = \frac{2.3150\times10^{-23}}{1.0546\times10^{-34}} = 2.1951\times10^{11}\ \text{m}^{-1}.
\]
\[
2\kappa d_m = 2(2.1951\times10^{11})(5\times10^{-9}) = 2.1951\times10^{3}.
\]
\[
T_f = e^{-2195.1}.
\]
Converting to base‑10:
\[
\log_{10} T_f = \frac{-2195.1}{\ln 10}= \frac{-2195.1}{2.302585}= -953.3,
\]
so
\[
T_f \approx 10^{-953}.
\]

### 4.5 Bosonic–fermionic transmission ratio
\[
\frac{T_m}{T_f} = \frac{0.995}{10^{-953.3}} = 10^{953.3}\times0.995 \approx 10^{953}.
\]
The photon crosses the membrane roughly $10^{953}$ times more likely than the proton.

### 4.6 Full CA rule‑space size
A Moore neighbourhood has $9$ cells, giving $2^{9}=512$ possible neighbourhood configurations. Each configuration maps to a binary output, so the lookup‑table contains $512$ bits. The number of distinct rules is
\[
\text{Full rule‑space}=2^{512}.
\]
Using $\log_{10}2=0.30103$:
\[
\log_{10}(2^{512}) = 512\times0.30103 = 154.13,
\]
\[
2^{512}=10^{154.13}\approx1.35\times10^{154}.
\]

### 4.7 Isotropic rule‑space size
Isotropy reduces the effective neighbourhood configurations to $102$ (as reported in [2]). Hence
\[
\text{Isotropic rule‑space}=2^{102}.
\]
\[
\log_{10}(2^{102}) = 102\times0.30103 = 30.71,
\]
\[
2^{102}=10^{30.71}\approx5.07\times10^{30}.
\]

### 4.8 Binary lattice configuration space
For a binary CA on a lattice with $M$ cells, the configuration space size is $2^{M}$ [7]. With a $61\times61$ grid:
\[
M = 61\times61 = 3721,
\]
\[
\text{Configuration space}=2^{3721}.
\]
\[
\log_{10}(2^{3721}) = 3721\times0.30103 = 1120.03,
\]
\[
2^{3721}=10^{1120.03}\approx1.00\times10^{1120}.
\]

All arithmetic steps are shown explicitly, and each input number is sourced from the assumption register or the cited bibliography.

## 5. Results
| Quantity | Computed Value | Source |
|----------|----------------|--------|
| Membrane photon transmission $T_m$ | $0.995$ (dimensionless) | Section 4.1 (assumptions $A_1$, $A_3$) |
| Cytoplasmic photon transmission $T_c$ | $4.54\times10^{-5}$ | Section 4.2 (assumptions $A_2$, $A_4$) |
| Total photon transmission $T_{\mathrm{tot}}$ | $4.52\times10^{-5}$ | Section 4.3 |
| Proton tunneling probability $T_f$ | $10^{-953}$ (dimensionless) | Section 4.4 (assumptions $A_5$–$A_7$, $A_3$) |
| Bosonic–fermionic ratio $T_m/T_f$ | $10^{953}$ (dimensionless) | Section 4.5 |
| Full CA rule‑space $2^{512}$ | $1.35\times10^{154}$ | Section 4.6 (derived from [2]) |
| Isotropic CA rule‑space $2^{102}$ | $5.07\times10^{30}$ | Section 4.7 (derived from [2]) |
| Binary lattice configuration space $2^{3721}$ | $1.35\times10^{1120}$ | Section 4.8 (derived from [7]) |

These numbers illustrate that (i) photon transmission across a membrane is high but cytoplasmic absorption reduces the overall probability to the order of $10^{-5}$, (ii) a proton is astronomically unlikely to tunnel the same barrier, and (iii) the combinatorial CA spaces are many orders of magnitude larger than any feasible exhaustive search.

## 6. Discussion
### 6.1 Limitations
- **L1.** Absorption coefficients $\mu_m$ and $\mu_c$ are assumed to be $10^{4}\ \text{cm}^{-1}$ in the absence of measured values; a sensitivity analysis of $T_{\mathrm{tot}}$ against $\mu_c d_c$ is given in Section 6.2.
- **L2.** The proton tunneling model assumes a rectangular barrier of height $1\ \text{eV}$ and width equal to membrane thickness; real ion channels present more complex potentials.
- **L3.** The CA abstraction treats photon presence as a binary state, ignoring polarization, phase, and coherence effects that could influence transport.
- **L4.** The isotropy reduction to $102$ configurations presumes perfect rotational symmetry, which may be broken by membrane proteins or anisotropic scattering.

### 6.2 Sensitivity
Varying $\mu_c$ over $10^{3}$–$10^{5}\ \text{cm}^{-1}$ changes $\mu_c d_c$ from $1$ to $100$, yielding $T_c$ from $e^{-1}=0.368$ down to $e^{-100}\approx3.7\times10^{-44}$. Consequently, $T_{\mathrm{tot}}$ spans approximately $0.366$ down to $3.7\times10^{-44}$, confirming that cytoplasmic absorption dominates the overall photon budget.

### 6.3 Falsifiability
A falsification of the main claim—that the combinatorial CA space precludes exhaustive modeling of UV‑mediated signaling—would occur if an empirical study identified a biologically plausible subset of rules smaller than $10^{12}$ and demonstrated that this subset can be exhaustively enumerated with current computational resources. Conversely, measuring membrane transmission significantly higher than $e^{-5\times10^{-3}}$ (e.g., $>0.999$) would falsify the assumed $\mu_m$ value and require revision of the photon budget.

### 6.4 Open Questions
- How can specific CA rules be mapped onto measurable biophysical parameters such as absorption probability $\alpha$ (cf. [6])?
- What is the minimal lattice resolution that captures sub‑cellular UV gradients without inflating the configuration space beyond tractability?
- Can stochastic updating schemes with $\alpha$ calibrated to $T_{\mathrm{tot}}$ reproduce observed intracellular photon fluence patterns?

## 7. Practical Implications and Engineering Pathways
### 7.1 Intended Users and Decision Impact
Researchers developing abstract models of intercellular UV communication—particularly those employing binary CA frameworks—will use the quantitative benchmarks derived here to decide between exhaustive rule‑space sweeps and targeted hypothesis‑driven rule selection. Modelers can now justify focusing on isotropic rule families ($\sim10^{30}$ rules) rather than the full $10^{154}$ space.

### 7.2 Technology Readiness Level
The work is purely analytical and has not undergone peer review; it resides at **TRL 1–2**. No hardware prototype or experimental validation has been performed.

### 7.3 Minimal Next Experiment
A minimal pilot study would implement a binary CA on a $61\times61$ lattice using a single isotropic rule (chosen from the $2^{102}$ set) and couple it to a Monte‑Carlo photon‑transport simulation that employs the membrane transmission $T_m=0.995$ and cytoplasmic transmission $T_c=4.54\times10^{-5}$. The experiment would measure whether emergent spatiotemporal patterns correspond to known UV‑induced signaling pathways. Observation of a systematic mismatch would falsify the utility of the selected rule for modeling UV transport.

### 7.4 Engineering Constraints
- **Constraint C1.** Memory: storing the full $2^{512}$ lookup‑table is infeasible; even the isotropic rule‑space ($2^{102}\approx5.07\times10^{30}$ rules) exceeds the storage capacity of contemporary hardware, so only sampling or structured subsets can be materialised.
- **Constraint C2.** Temporal resolution: stochastic updating probability $\alpha$ (from [6]) must be calibrated to the photon survival probability per cell, which Section 4.2 gives as $T_c = 4.54\times10^{-5}$ per $10\ \mu\text{m}$ of cytoplasm.
- **Constraint C3.** Parameter acquisition: accurate $\mu_m$ and $\mu_c$ values for specific membrane compositions are needed; absent such data, the model remains a projection.

### 7.5 Projected Cost Bounds
 No quantitative cost bound can be derived from the available assumptions; therefore no cost projection is provided.

### 7.6 Risks and Misuse
A potential misuse is the over‑interpretation of the high membrane transmission ($\approx99.5\%$) as justification for unregulated UV exposure in clinical settings, ignoring phototoxicity and dose‑response considerations. The model explicitly excludes safety assessments; any application must incorporate independent toxicological evaluations.

## 8. Conclusion
We have quantified (i) the transmission probability of UV photons through a lipid membrane and cytoplasm using Beer–Lambert attenuation, (ii) the tunneling probability of a proton through the same membrane via the WKB approximation, and (iii) the combinatorial magnitude of binary CA rule‑spaces that could abstract such transport. Photon transmission across a membrane is high ($\approx99.5\%$) but cytoplasmic absorption reduces the overall probability to $\sim4.5\times10^{-5}$ over a $10\ \mu\text{m}$ path. Proton tunneling is astronomically suppressed ($\sim10^{-953}$), yielding a bosonic–fermionic advantage of $\sim10^{953}$ that stems from mass and charge differences rather than Bose statistics. The CA combinatorial analysis shows that even reduced isotropic rule‑spaces ($\sim10^{30}$) and lattice configuration spaces ($\sim10^{1120}$) are far beyond exhaustive exploration, directing future work toward hypothesis‑driven rule selection and stochastic updating schemes calibrated to measured absorption probabilities. The benchmarks presented here provide a concrete reference for modelers of UV‑mediated cellular communication and establish a foundation for subsequent experimental validation.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 3 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] A Note on Elementary Cellular Automata Classification. arXiv:1306.5577v2. https://arxiv.org/abs/1306.5577v2
[2] The X-rule: universal computation in a non-isotropic Life-like Cellular Automaton. arXiv:1504.01434v2. https://arxiv.org/abs/1504.01434v2
[3] Isotropic Cellular Automata: the DDLab iso-rule paradigm. arXiv:2008.11279v2. https://arxiv.org/abs/2008.11279v2
[4] On Decidability Properties of One-Dimensional Cellular Automata. arXiv:0903.4615v2. https://arxiv.org/abs/0903.4615v2
[5] A 3D Human Body Blockage Model for Outdoor Millimeter-Wave Cellular Communication. arXiv:1710.08147v1. https://arxiv.org/abs/1710.08147v1
[6] A guided tour of asynchronous cellular automata. arXiv:1406.0792v2. https://arxiv.org/abs/1406.0792v2
[7] On the decomposition of stochastic cellular automata. arXiv:1503.03318v2. https://arxiv.org/abs/1503.03318v2
[8] Probabilistic Cellular Automata for Granular Media in Video Games. arXiv:2008.06341v1. https://arxiv.org/abs/2008.06341v1
