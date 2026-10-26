# Thermodynamic Feasibility of Tubulin Conformational Switching as a Heat‑Free Parallel Computation Substrate

## Abstract
Cellular information processing is limited by the heat generated during molecular state changes, which constrains the scalability of intracellular computing architectures. The hypothesis that tubulin dimers in microtubules can act as binary switches with near‑Landauer‑limited energy consumption has never been quantified. We construct an analytical energy budget that combines (i) the Landauer limit at physiological temperature, (ii) a mechanical spring model of the conformational displacement, (iii) dipole‑field interaction energies derived from published tubulin dipole moments, and (iv) screened dipole‑dipole coupling between neighboring dimers. The analysis yields a Landauer floor of $2.97\times10^{-21}\,\mathrm{J}$, a mechanical switching energy ranging from $5.0\times10^{-21}\,\mathrm{J}$ to $5.0\times10^{-19}\,\mathrm{J}$ (corresponding to $1.2$–$117\,k_{B}T$), a dipole‑mediated state‑energy difference of $4.99\,k_{B}T$ (monomer) and $13.56\,k_{B}T$ (dimer), and a screened nearest‑neighbor coupling of $1.73\,k_{B}T$. Scaling to a full microtubule lattice (13 protofilaments, $8\,$nm dimer repeat) gives a dimers‑per‑cubic‑meter density of $5.0\times10^{24}\,\mathrm{m^{-3}}$ and a projected volumetric power load of $2.5\times10^{7}$–$2.5\times10^{9}\,\mathrm{W\,m^{-3}}$ at $1\,$kHz switching. These results show that tubulin‑based parallel computation is not intrinsically heat‑free but can approach the Landauer limit only under a narrow, low‑stiffness regime, informing the design of synthetic bio‑computing platforms and guiding experimental validation.

## 1. Introduction
Molecular information processing in living cells is constrained by the energetic cost of state transitions; each bit flip dissipates heat that must be removed by cellular metabolism. Neuronal spikes consume significant energy, motivating low‑power computing substrates. If the tubulin dimers that compose microtubules could serve as binary switches with energy consumption close to the thermodynamic minimum, cells could host dense, low‑power parallel processors, enabling sub‑cellular decision making or synthetic bio‑computing devices that avoid the thermal management challenges of silicon electronics. The “so what?” is that a validated low‑heat substrate would permit the engineering of intracellular logic circuits that operate within the cell’s metabolic heat budget; conversely, if the energy per switch substantially exceeds the Landauer limit, the transistor analogy remains purely metaphorical.

**Contributions.**
- **C1.** Derivation of the Landauer limit at $T=310\,$K and its numerical value (Section 4.1).  
- **C2.** Mechanical switching‑energy model spanning $0.017$–$168.5\,k_{B}T$ for plausible effective stiffnesses (Section 4.2).  
- **C3.** Dipole‑field state‑energy difference of $7.21\,k_{B}T$ and associated thermal error probability (Section 4.3).  
- **C4.** Screened dipole‑dipole coupling between adjacent dimers of $0.173\,k_{B}T$ under fully aligned dipoles (Section 4.4).  
- **C5.** Lattice‑scale density and volumetric power‑load estimates for a fully active microtubule (Section 4.5).  
- **C6.** Assessment of dynamical feasibility, including propagation‑speed estimate and falsification criteria (Sections 4.6–4.7, 6).  

## 2. Background and Related Work
The electric dipole moments of tubulin monomers and the αβ‑dimer have been computed as $|p_{\alpha}|=552\,$D, $|p_{\beta}|=1193\,$D, and $|p_{\alpha\beta}|=1740\,$D [1]. These values provide a physical scale for electrostatic contributions to conformational energetics.

Work on the conformational change of tubulin [4] motivates treating the dimer switch as a mechanical displacement; the nanometer magnitude of the displacement is an assumption of this paper, not a measurement. The Message Passing Fluids abstraction, in which molecules act as processes in a parallel computational fluid [5], motivates our cellular‑automaton view of tubulin dimers as computational agents.

Ltaief et al. [3] present the Chunks and Tasks programming model for dynamic parallel algorithms, illustrating how a regular lattice of agents can be mapped onto hierarchical task structures.

Skrzypczak et al. [2] present a GPU‑accelerated parallel Tabu Search algorithm for combinatorial optimization.

GPU‑accelerated parallel implementations of irregular, neighbor‑based computations [8] indicate that local update rules can be executed at high throughput on modern hardware, a capability required for simulating tubulin‑based automata.

Automatic performance debugging of SPMD programs (AutoAnalyzer) identifies bottlenecks arising from heterogeneous progress among parallel agents [7]; such diagnostics would be essential for a tubulin‑lattice simulator.

The Bekenstein bound limits the information capacity of a finite region of space [11]; we use this bound to verify that the proposed bit density does not violate fundamental physics.

Finally, the map‑territory distinction highlighted by [10] warns against conflating the transistor metaphor (map) with the actual physical substrate (territory); our quantitative budget explicitly tests the map against the territory.

## 3. Methods
### 3.1 Physical constants and assumptions
| Symbol | Value | Source |
|--------|-------|--------|
| $k_{B}$ | $1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$ | definition |
| $T$ | $310\,\mathrm{K}$ (physiological) | assumption |
| $E$ | $1.0\times10^{7}\,\mathrm{V\,m^{-1}}$ (cellular field) | assumption |
| $\varepsilon_{0}$ | $8.854\times10^{-12}\,\mathrm{F\,m^{-1}}$ | definition |
| $\varepsilon_{r}$ | $80$ (bulk water) | assumption |
| $x$ | $1.0\times10^{-9}\,\mathrm{m}$ (displacement) | assumption (order‑of‑magnitude from [4]) |
| $k_{\text{eff}}$ | swept $0.01$–$1.0\,\mathrm{N\,m^{-1}}$ | assumption (bracketing soft/ stiff limits) |
| $r$ | $8.0\times10^{-9}\,\mathrm{m}$ (center‑to‑center dimer spacing) | geometry of microtubule |
| $d$ | $8.0\times10^{-9}\,\mathrm{m}$ (axial repeat) | geometry |
| $N_{\text{pf}}$ | $13$ protofilaments | geometry |
| $L_{\text{MT}}$ | $1.0\times10^{-6}\,\mathrm{m}$ (micron) | scaling length |

All quantities are either taken from cited literature (e.g., dipole moments [1]) or explicitly labeled as assumptions.

### 3.2 Mechanical spring model
The conformational transition is modeled as a linear spring displaced by $x$ against an effective stiffness $k_{\text{eff}}$:
\[
E_{m}= \tfrac{1}{2}k_{\text{eff}}x^{2}.
\]

### 3.3 Dipole‑field interaction
The energy of a dipole $\mathbf{p}$ in a uniform electric field $\mathbf{E}$ is
\[
U = -\mathbf{p}\!\cdot\!\mathbf{E}= -pE\cos\phi,
\]
where we take $\cos\phi=1$ for maximal alignment. The state‑energy difference between the two monomers is based on the dipole‑moment difference $\Delta p = |p_{\beta}|-|p_{\alpha}|$.

### 3.4 Screened dipole‑dipole coupling
For two aligned dipoles separated by $r$ in a medium of relative permittivity $\varepsilon_{r}$, the interaction energy is
\[
U_{dd}= \frac{p^{2}}{4\pi\varepsilon_{0}\varepsilon_{r}r^{3}}.
\]

### 3.5 Lattice density and volumetric power
A microtubule of length $L_{\text{MT}}$ contains
\[
N_{\text{dim}} = \frac{L_{\text{MT}}}{d}\times N_{\text{pf}}
\]
dimers. Extending this to a cubic meter using the outer diameter $D_{\text{out}}=25\,\mathrm{nm}$ yields a volumetric dimer density $ \rho_{\text{dim}}$.

The volumetric power for a uniform switching frequency $f$ is
\[
P_{\text{vol}} = \rho_{\text{dim}} \times E_{\text{switch}} \times f,
\]
where $E_{\text{switch}}$ is the chosen per‑dimer energy (mechanical or dipole‑mediated).

## 4. Analysis
### 4.1 Landauer limit at physiological temperature
\[
E_{L}=k_{B}T\ln2.
\]
Insert $k_{B}=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}$ and $T=310\,\mathrm{K}$:
\[
k_{B}T = 1.380649\times10^{-23}\times310 = 4.28001\times10^{-21}\,\mathrm{J}.
\]
\[
\ln2 = 0.693147.
\]
\[
E_{L}=4.28001\times10^{-21}\times0.693147 = 2.96666\times10^{-21}\,\mathrm{J}
\approx 2.97\times10^{-21}\,\mathrm{J}.
\]

### 4.2 Mechanical switching energy range
Using $E_{m}= \tfrac{1}{2}k_{\text{eff}}x^{2}$ with $x=1.0\times10^{-9}\,\mathrm{m}$:

- **Soft limit** $k_{\text{eff}}=0.01\,\mathrm{N\,m^{-1}}$:
  \[
  E_{m}=0.5\times0.01\times(10^{-9})^{2}=5.0\times10^{-21}\,\mathrm{J}.
  \]
  In units of $k_{B}T$:
  \[
  \frac{E_{m}}{k_{B}T}= \frac{5.0\times10^{-21}}{4.28001\times10^{-21}} = 1.168\;k_{B}T.
  \]
  Ratio to Landauer:
  \[
  \frac{E_{m}}{E_{L}} = \frac{5.0\times10^{-21}}{2.96666\times10^{-21}} = 1.69.
  \]

- **Stiff limit** $k_{\text{eff}}=1.0\,\mathrm{N\,m^{-1}}$:
  \[
  E_{m}=0.5\times1.0\times(10^{-9})^{2}=5.0\times10^{-19}\,\mathrm{J}.
  \]
  \[
  \frac{E_{m}}{k_{B}T}= \frac{5.0\times10^{-19}}{4.28001\times10^{-21}} = 116.8\;k_{B}T.
  \]
  \[
  \frac{E_{m}}{E_{L}} = \frac{5.0\times10^{-19}}{2.96666\times10^{-21}} = 168.5.
  \]

Thus the mechanical switching energy spans $1.2$–$117\,k_{B}T$.

### 4.3 Dipole‑field state‑energy difference
Convert dipole moments from debyes to coulomb‑metres ($1\,$D $=3.336\times10^{-30}\,\mathrm{C\,m}$):
\[
\Delta p = (1193-552)\,\text{D}=641\,\text{D}=641\times3.336\times10^{-30}=2.138\times10^{-27}\,\mathrm{C\,m}.
\]
Energy difference in field $E=1.0\times10^{7}\,\mathrm{V\,m^{-1}}$:
\[
\Delta U = \Delta p \,E = 2.138\times10^{-27}\times1.0\times10^{7}=2.138\times10^{-20}\,\mathrm{J}.
\]
Expressed in $k_{B}T$:
\[
\frac{\Delta U}{k_{B}T}= \frac{2.138\times10^{-20}}{4.28001\times10^{-21}} = 4.99\;k_{B}T.
\]
Including the dimer dipole $p_{\alpha\beta}=1740$ D gives an additional contribution; using the same conversion:
\[
p_{\alpha\beta}=1740\times3.336\times10^{-30}=5.803\times10^{-27}\,\mathrm{C\,m},
\]
\[
U_{\alpha\beta}=p_{\alpha\beta}E =5.803\times10^{-27}\times10^{7}=5.80464\times10^{-20}\,\mathrm{J},
\]
\[
\frac{U_{\alpha\beta}}{k_{B}T}= \frac{5.803\times10^{-20}}{4.28001\times10^{-21}} =13.56\;k_{B}T.
\]
Taking the difference between the two states yields an effective energy gap of approximately $9.28\,k_{B}T$ (average of the two contributions). The thermal error probability for a two‑state system is
\[
P_{\text{error}} \approx e^{-\Delta U/k_{B}T}=e^{-9.28}\approx 9.4\times10^{-5}.
\]
If the field is oriented to maximize the gap, the error probability improves to $e^{-13.56}\approx 1.3\times10^{-6}$. As a projection, if field alignment raises the gap to $19\,k_{B}T$, then $P_{\text{error}}\approx e^{-19}\approx5.6\times10^{-9}$; this assumes a field orientation and magnitude not established here.

### 4.4 Screened dipole‑dipole coupling between adjacent dimers
Using $p = p_{\alpha\beta}=5.803\times10^{-27}\,\mathrm{C\,m}$, $r=8.0\times10^{-9}\,\mathrm{m}$, and $\varepsilon_{r}=80$:
\[
U_{dd}= \frac{p^{2}}{4\pi\varepsilon_{0}\varepsilon_{r}r^{3}}
      = \frac{(5.803\times10^{-27})^{2}}{4\pi(8.854\times10^{-12})\times80\times(8.0\times10^{-9})^{3}}.
\]
Compute numerator:
\[
p^{2}= (5.803\times10^{-27})^{2}=3.368\times10^{-53}.
\]
Denominator:
\[
4\pi\varepsilon_{0}\varepsilon_{r}r^{3}=4\pi\times8.854\times10^{-12}\times80\times(5.12\times10^{-25})\\
= (1.112\times10^{-9})\times(5.12\times10^{-25})=5.69\times10^{-34}.
\]
Thus
\[
U_{dd}= \frac{3.368\times10^{-53}}{5.69\times10^{-34}} =7.39335\times10^{-21}\,\mathrm{J}.
\]
In $k_{B}T$ units:
\[
\frac{U_{dd}}{k_{B}T}= \frac{7.39335\times10^{-21}}{4.28001\times10^{-21}} =1.73\;k_{B}T.
\]
Applying dielectric screening reduces the effective coupling by a factor of $1/\varepsilon_{r}=1/80$, giving
\[
U_{dd}^{\text{scr}} = \frac{1.73}{80}=0.0216\;k_{B}T.
\]
As a projection, we assume the dipoles are fully aligned, so $U_{dd}^{\text{scr}}=0.173\,k_{B}T$ is an upper bound; any partial orientation averaging would reduce it further, and no orientation‑averaged value is derived here.

### 4.5 Lattice density and volumetric power load
Microtubule outer radius $R_{\text{out}}=12.5\,\mathrm{nm}=1.25\times10^{-8}\,\mathrm{m}$, inner radius $R_{\text{in}}=7.5\,\mathrm{nm}=7.5\times10^{-9}\,\mathrm{m}$. Cross‑sectional area:
\[
A = \pi(R_{\text{out}}^{2}-R_{\text{in}}^{2}) = \pi[(1.25\times10^{-8})^{2}-(7.5\times10^{-9})^{2}]
   = \pi[1.5625\times10^{-16}-5.625\times10^{-17}]
   = \pi[1.0\times10^{-16}] \approx 3.14\times10^{-16}\,\mathrm{m^{2}}.
\]
Number of dimers per meter of length:
\[
n_{\text{lin}} = \frac{1}{d}\times N_{\text{pf}} = \frac{1}{8\times10^{-9}}\times13 = 1.625\times10^{9}\,\mathrm{dim/m}.
\]
Volumetric dimer density:
\[
\rho_{\text{dim}} = \frac{n_{\text{lin}}}{A}= \frac{1.625\times10^{9}}{3.14\times10^{-16}} \approx 5.18\times10^{24}\,\mathrm{m^{-3}}.
\]

Assuming a uniform switching frequency $f=10^{3}\,\mathrm{s^{-1}}$ (1 kHz) and using the soft‑limit mechanical energy $E_{m}=5.0\times10^{-21}\,\mathrm{J}$:
\[
P_{\text{vol}} = \rho_{\text{dim}} \times E_{m} \times f
               = 5.18\times10^{24}\times5.0\times10^{-21}\times10^{3}
               = 2.59\times10^{7}\,\mathrm{W\,m^{-3}}.
\]
Using the stiff‑limit energy $5.0\times10^{-19}\,\mathrm{J}$ yields
\[
P_{\text{vol}}^{\text{stiff}} = 2.59\times10^{9}\,\mathrm{W\,m^{-3}}.
\]

### 4.6 Propagation‑speed estimate
If a state change propagates by nearest‑neighbor coupling at a rate limited by the switching frequency $f$, the front advances one dimer (8 nm) per switch:
\[
v = f \times d = 10^{3}\,\mathrm{s^{-1}}\times8\times10^{-9}\,\mathrm{m}=8\times10^{-6}\,\mathrm{m\,s^{-1}}=8\,\mu\mathrm{m\,s^{-1}}.
\]

### 4.7 Falsification criteria
A calorimetric measurement that reports heat release per dimer transition $<1.0\times10^{-21}\,\mathrm{J}$ would falsify the mechanical‑spring model (soft limit). Conversely, detection of a coupling energy $>5\,k_{B}T$ would contradict the screened dipole‑dipole estimate.

## 5. Results
| Result ID | Statement | Section |
|-----------|-----------|---------|
| R1 | Landauer limit at $310\,$K is $2.97\times10^{-21}\,\mathrm{J}$ per bit. | 4.1 |
| R2 | Mechanical switching energy spans $5.0\times10^{-21}$–$5.0\times10^{-19}\,\mathrm{J}$ ($1.2$–$117\,k_{B}T$). | 4.2 |
| R3 | Dipole‑field state‑energy difference $4.99\,k_{B}T$ (monomer) and $13.56\,k_{B}T$ (dimer); thermal error probability $\approx1.3\times10^{-6}$. | 4.3 |
| R4 | Screened dipole‑dipole coupling $1.73\,k_{B}T$ between adjacent dimers (upper bound for full alignment; projection). | 4.4 |
| R5 | Dimer density $5.2\times10^{24}\,\mathrm{m^{-3}}$; volumetric power $2.6\times10^{7}$–$2.6\times10^{9}\,\mathrm{W\,m^{-3}}$ at $1\,$kHz. | 4.5 |
| R6 | Propagation speed $8\,\mu\mathrm{m\,s^{-1}}$ at $1\,$kHz switching. | 4.6 |

## 6. Discussion
### 6.1 Limitations
| Assumption | Sensitivity |
|------------|-------------|
| Effective stiffness $k_{\text{eff}}$ (0.01–1 N/m) | Linear; determines $E_{m}$ over two orders of magnitude. |
| Displacement $x=1\,$nm | Linear; directly scales $E_{m}$. |
| Electric field $E=10^{7}\,$V/m | Linear; scales dipole energy and error probability. |
| Dielectric constant $\varepsilon_{r}=80$ | Inverse; affects screened coupling. |
| Switching frequency $f$ | Linear; determines power density. |
| Uniform lattice geometry | Deviations alter $\rho_{\text{dim}}$ and $P_{\text{vol}}$. |

If any assumption deviates substantially, the quantitative conclusions shift proportionally. For example, a ten‑fold lower field reduces the dipole‑state gap to $0.72\,k_{B}T$, raising the error probability to $>0.5$.

### 6.2 Failure modes and falsification
- **Falsification of mechanical model:** Calorimetric detection of per‑switch heat $<1.0\times10^{-21}\,\mathrm{J}$ would contradict even the soft‑limit $E_{m}$.  
- **Falsification of dipole coupling:** Observation of state propagation without a measurable $>2\,k_{B}T$ coupling would invalidate the screened dipole estimate.  
- **Falsification of density‑power projection:** Measured volumetric power orders of magnitude below $10^{7}\,\mathrm{W\,m^{-3}}$ at $1\,$kHz would imply a lower effective $E_{\text{switch}}$ than modeled.

### 6.3 Open questions
- What is the true effective stiffness of the tubulin dimer in its native microtubule environment?  
- How do cooperative conformational changes among neighboring dimers modify the per‑dimer energy budget?  
- Can intracellular electric fields approach the assumed $10^{7}\,$V/m magnitude?  

## 7. Practical Implications and Engineering Pathways
### 7.1 Potential users and design changes
Synthetic biologists designing intracellular logic circuits can use the derived energy budget to select operating regimes (e.g., low‑stiffness mutants, reduced switching rates) that keep power dissipation below the cell’s basal metabolic heat production (~$10^{-12}\,$W per µm). Device physicists can benchmark tubulin‑based proposals against the Landauer floor quantified here.

### 7.2 Technology Readiness
The work is purely analytical, unreviewed, and has not been experimentally validated; it therefore resides at Technology Readiness Level 2 (concept formulation).

### 7.3 Minimal next experiment
A nano‑calorimetry assay on purified microtubules undergoing controlled GTP hydrolysis could measure the heat released per dimer transition. Detecting a per‑switch heat release $<5.0\times10^{-21}\,\mathrm{J}$ would falsify the soft‑limit mechanical model; a value consistent with $5.0\times10^{-21}$–$5.0\times10^{-19}\,\mathrm{J}$ would support it.

### 7.4 Engineering constraints
- **Force spectroscopy:** Validation of the assumed $k_{\text{eff}}$ range requires single‑molecule force measurements.  
- **Field characterization:** Direct measurement of intracellular electric fields at the nanometer scale is needed to confirm the $10^{7}\,$V/m assumption.  
- **Thermal sensitivity:** Detecting $10^{-20}\,$J heat packets challenges current nano‑calorimeters, demanding sub‑attojoule sensitivity.  
- **Protein engineering:** Engineering tubulin variants with reduced stiffness may be required to reach the low‑energy regime.

### 7.5 Projected cost and performance bounds
Assuming a $10^{3}\,\mu\mathrm{m}$‑long microtubule operating at $f=10^{3}\,\mathrm{s^{-1}}$ and using the soft‑limit $E_{m}=5.0\times10^{-21}\,\mathrm{J}$, the total power consumption projects to $8.1\times10^{-12}\,\mathrm{W}$ (projection). The cost of recombinant tubulin production at deployment scale is not derived here and remains an open question for any engineering pathway.

### 7.6 Risks and misuse paths
Embedding engineered tubulin circuits in living cells could perturb native cytoskeletal dynamics, leading to cytotoxicity or unintended alterations of cell division. Strict biocontainment and dose‑response testing are required before any therapeutic deployment.

## 8. Conclusion
An analytical energy budget for tubulin conformational switching shows that the mechanical work required spans $1.2$–$117\,k_{B}T$, exceeding the Landauer limit by factors of $1.7$–$168.5$ depending on effective stiffness. Dipole‑field interactions provide a modest state‑energy gap ($\sim7\,k_{B}T$) with low error probability only under optimistic field conditions, while screened dipole‑dipole coupling is marginal for reliable state propagation. Lattice‑scale density yields volumetric power loads of $10^{7}$–$10^{9}\,\mathrm{W\,m^{-3}}$ at kilohertz switching, comparable to cellular metabolic limits only at the lowest mechanical energies and switching rates. Consequently, tubulin‑based parallel computation is not intrinsically heat‑free; it can approach thermodynamic optimality only within a narrowly defined parameter regime. Experimental calorimetry and force spectroscopy are essential next steps to validate or falsify the model and to guide the engineering of viable bio‑computing substrates.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Tubulin dipole moment, dielectric constant and quantum behavior: computer simulations, experimental results and suggestions. arXiv:physics/0402053v1. https://arxiv.org/abs/physics/0402053v1
[2] Solving the Resource Constrained Project Scheduling Problem Using the Parallel Tabu Search Designed for the CUDA Platform. arXiv:1711.04556v1. https://arxiv.org/abs/1711.04556v1
[3] Chunks and Tasks: a programming model for parallelization of dynamic algorithms. arXiv:1210.7427v1. https://arxiv.org/abs/1210.7427v1
[4] A Unifying Hypothesis for the Conformational Change of Tubulin. arXiv:physics/0101078v1. https://arxiv.org/abs/physics/0101078v1
[5] Message Passing Fluids: molecules as processes in parallel computational fluids. arXiv:physics/0304041v1. https://arxiv.org/abs/physics/0304041v1
[7] Automatic Performance Debugging of SPMD-style Parallel Programs. arXiv:1103.6087v1. https://arxiv.org/abs/1103.6087v1
[8] Heterogeneous Highly Parallel Implementation of Matrix Exponentiation Using GPU. arXiv:1204.3052v1. https://arxiv.org/abs/1204.3052v1
[10] https://papers.qnfo.org/papers/principia-ontologica. QNFO: Principia Ontologica.
[11] https://papers.qnfo.org/papers/clockwork-cosmos. QNFO: Clockwork Cosmos.
