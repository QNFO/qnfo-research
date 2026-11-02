# CEI Invariance: Architectures as Equivalence Classes of Causal Density and Energy Fidelity

## Abstract

Computational architectures are today chosen for a substrate by benchmarking, an expensive process that must be repeated for every substrate-architecture pair and gives no guidance before hardware exists. No existing framework predicts, from thermodynamics alone, which architecture classes a physical substrate can sustain. We propose the Causal-Energy Invariant (CEI): for a given substrate, the product of causal density $\rho_t$ (dependent operations per volume-time) and energy fidelity $\eta_e$ (energy per transition in units of $kT\ln 2$) is bounded by a substrate constant $\kappa$, derived from Landauer's principle, a substrate power-density limit, and causal-cone bounds on operation rates. Architectures with equal $\rho_t\eta_e$ form genuine equivalence classes, and the bound predicts that substrates favor architectures whose product approaches $\kappa$. We derive $\kappa = 3.483\times 10^{29}\ \mathrm{m^{-3}\,s^{-1}}$ for silicon under an assumed areal power limit of $100\ \mathrm{W\,cm^{-2}}$ and a $1\ \mathrm{mm}$ active depth, show the causal-cone bound exceeds this by a factor $\approx 8.6\times 10^{13}$ (so power, not relativity, binds silicon), and classify two assumed architecture profiles: a pipelined CMOS-like profile saturating $3.0\%$ of $\kappa$ and a gate-based error-corrected profile with $\eta_e \geq 100$ from published thermodynamic floors. Confirmation would replace per-pair benchmarking with a thermodynamic substrate-architecture map; falsification would localize where the tradeoff breaks.

## 1. Introduction

Cloud providers, defense laboratories, and embedded-systems designers face a recurring and costly decision: which computational architecture to build for which physical substrate. The workloads they care most about — combinatorial optimization, privacy-preserving computation, large-scale inference — are dominated by hardware whose cost scales with the number of discrete operations executed, and special-purpose accelerators, neuromorphic chips, and optical processors are today evaluated by qubit or transistor counts rather than by any physical measure of fit between machine and medium [13]. Every candidate architecture must be designed, fabricated, and benchmarked against every candidate substrate before a selection can be made. A failed pairing costs a fabrication cycle and years of engineering effort; the decision would change qualitatively if a substrate could be characterized once, by a small number of physical constants, and each architecture classified against it on paper before any hardware is built.

The gap this paper addresses is the absence of a thermodynamic quantity that (i) is a property of the substrate alone, (ii) is a property of the architecture alone, and (iii) constrains their combination. Energy-per-operation measures and operation-rate measures exist separately, and Landauer's principle gives a floor for the former [13], but no published framework composes them into a single invariant that partitions architectures into equivalence classes per substrate. This paper proposes such a quantity, the Causal-Energy Invariant (CEI), defined as the product

$$\Pi \;=\; \rho_t\,\eta_e,$$

where $\rho_t$ is the causal density — the number of mutually dependent operations executed per unit volume per unit time — and $\eta_e$ is the energy fidelity — the energy dissipated per elementary transition divided by the Landauer limit $kT\ln 2$. The central claim is that for a substrate with a finite power-density budget, $\rho_t\eta_e$ cannot exceed a substrate constant $\kappa$, and that architectures saturating or approaching $\kappa$ on the same substrate form an equivalence class of thermodynamically equivalent designs. The claim is deliberately stated so that it can be falsified: if measured platforms at their power limits show products differing by more than an order of magnitude on the same substrate, the invariant fails, and the failure localizes which assumption (Landauer floor, power budget, or causal cone) is responsible.

The claim matters beyond computer engineering. Equivalence-class methods have organized models in knot theory, statistics, graph polynomials, and signal processing; a thermodynamic equivalence relation over architectures would give physical computing a comparable classification tool, and the same product form could be tested on biological and engineered systems whose equivalence has been argued on categorical grounds [12].

The contributions of this paper are:

- A derivation of the CEI bound $\kappa$ from Landauer's principle, a substrate power-density limit, and causal-cone bounds on operation rates, with all arithmetic shown (Section 4).
- A proof that the relation "equal $\rho_t\eta_e$" is a genuine equivalence relation and that its classes are the orbits of a one-parameter partition, following the methodological standard for equivalence-class constructions (Section 4).
- A worked numerical classification for silicon under explicitly stated assumptions, giving $\kappa = 3.483\times 10^{29}\ \mathrm{m^{-3}\,s^{-1}}$, a causal-to-power bound ratio of $8.607\times 10^{13}$, and two architecture placements at $3.0\%$ and below $10^{-18}$ of $\kappa$ (Section 5).
- A mismatch-penalty projection for running an architecture on a substrate whose $\kappa$ is smaller than the architecture's product, and explicit falsification criteria with the observations that would refute the main result (Sections 5 and 6).

The product invariant, if confirmed on measured platforms, would also bear on the classification of biological computation, where energy management and information processing are already argued to be isomorphic across domains [12], and on network-level comparisons of computing systems, where equivalence is currently assessed across separate structural and dynamic layers rather than by a single composed quantity [14].

## 2. Background and Related Work

Equivalence classes are a mature organizing device across mathematics and its applications, and the present paper imports their methodological standards into the thermodynamics of computing. This section reviews the specific results of the cited works that the construction relies on.

Nahas [1] studies equivalence classes of Fox $m$-colorings of link diagrams, where a coloring assigns integers modulo $m$ to arcs subject to the crossing relation $2b - a$, and defines classes as orbits of coloring automorphisms — permutations $f$ satisfying $f(a\ast b) = f(a)\ast f(b)$ for the dihedral quandle operation $x\ast y = 2y - x \pmod m$. Its Proposition 3.1 gives a closed count: a link with $p$-nullity $n$ for odd prime $p$ has $(p^{n-1}-1)/(p-1)$ equivalence classes of $p$-colorings. The lesson imported here is that an equivalence class construction is complete only when the classes can be counted or parameterized by an invariant; Section 4 parameterizes CEI classes by the single scalar $\Pi$ in the same spirit.

Gosper, Smith and collaborators on staged trees [2] characterize statistical equivalence classes of chain event graphs by a shared polynomial description: two staged trees are statistically equivalent when their parametrization rules — products of transition probabilities along root-to-leaf paths — parametrize the same model. Their discussion notes that a polynomial equivalence class contains $2^{\#\mathrm{twins}}$ elements from naive swaps, of which only a small fraction correspond to staged trees (in their worked example, $2^5 = 32$ naive representations of which only four are staged). This warns that a class defined by an invariant may contain many members that are not admissible instances of the structure; Section 6 carries the same caution over to architectures that share a $\Pi$ value but are not physically realizable on the target substrate.

Aiken and Ng on independence equivalence of cycles [3] and of paths [6], and Brown and Alikhani on domination equivalence of paths [10], solve the analogous problem for graph polynomials: two graphs are equivalent when they share the same independence or domination polynomial, and the works determine exactly which non-isomorphic graphs share a polynomial. [3] records that the roots of $I(C_n,x)$ are $c_i = -1/(2 + 2\cos((2i-1)\pi/n))$, and [6] gives the corresponding roots $p_i = -1/(2+2\cos(2i\pi/(n+2)))$ for paths, showing that equivalence classes can be read off a factorization of the defining invariant. The structural moral — that the invariant's factorization determines the class membership — motivates Section 4's factorization of $\Pi$ into a substrate factor and an architecture factor.

Harrison and Lescanne-style formalization of quotients [4] treats the computational content of equivalence classes: defining a function on a quotient requires proving the result independent of the chosen representative, a proof obligation that users of theorem provers avoid by preferring canonical representatives such as de Bruijn variables for $\alpha$-equivalence. Section 4 discharges the analogous obligation for CEI by showing that the mismatch penalty of Section 5 depends only on the product $\Pi$, not on the separate factors.

Pigolotti, Roldán and collaborators on large deviations [5] define an equivalence relation on stochastic dynamics under which dynamics in the same class share the same large-deviation properties; dynamics factor into an equilibrium part (common to the class) and a nonequilibrium part carrying the affinities, decomposed through the operators $E_{ij}[P] = \sqrt{P_{ij}P_{ji}}$ and a chord-based $Z(\boldsymbol{\mu})$. This is the closest structural precedent to CEI: a thermodynamic quantity (the large-deviation rate function) is constant across an equivalence class of physical processes. CEI applies the same pattern with the product $\rho_t\eta_e$ in place of the rate function.

Calimani and collaborators on Cayley graphs [9] characterize weak equivalence of Cayley graphs $C(\mathcal{A},\Omega)$ by the existence of a group automorphism $\alpha$ with $\alpha(\Omega) = \Omega'$, and count weak equivalence classes as orbits of the $\mathrm{Aut}(\mathcal{A})$ action on generator sets. The orbit-counting technique — classes as orbits of a symmetry group acting on the objects — is the formal template Section 4 uses when it observes that rescaling $(\rho_t, \eta_e)$ by $(s, 1/s)$ leaves $\Pi$ fixed, so classes are orbits of a one-parameter rescaling action.

Segarra and Marques on graph Fourier transforms [8] define isomorphic and Jordan equivalence classes over which a spectral projector-based graph Fourier transform is identical, showing that the transform can be computed once per class rather than once per graph, with Jordan classes permitting identical transforms over graphs of nonidentical topology. This is the practical payoff pattern CEI aims at: computation done once per equivalence class instead of once per instance — here, substrate characterization done once instead of benchmarking per architecture-substrate pair.

Among works directly on physical computation, the QNFO categorical-equivalence paper [12] argues that biological and engineered computational systems implement categorically equivalent architectures through mathematical isomorphisms in energy management, information processing, and topological protection, and proposes multi-tiered experimental validation including two-dimensional electronic spectroscopy and neuromorphic benchmarking against conventional architectures. CEI supplies a candidate quantitative invariant that such a validation program could measure; the two programs are complementary, with [12] asserting the equivalence exists and CEI specifying a scalar to test it on.

The Hamiltonian-isomorphism taxonomy [13] is the nearest quantitative predecessor. It defines Hamiltonian isomorphism as an equivalence relation between a problem's cost structure and a substrate's energy function, proves it reflexive, symmetric, and transitive, and derives thermodynamic floors with all arithmetic shown: a single-bit erasure floor of $2.871\times 10^{-21}\ \mathrm{J}$ at $300\ \mathrm{K}$ from $kT\ln 2$; a gate-based logical-operation floor of $2.871\times 10^{-19}$ to $2.871\times 10^{-18}\ \mathrm{J}$ for error-correction overheads $N_{\mathrm{ec}} \in [10^2, 10^3]$; a single-relaxation machine floor of $6.029\times 10^{-20}\ \mathrm{J}$ for $n_{\mathrm{out}} = 20$; and an energy ratio of $4.762\times 10^{6}$ for a $10^6$-gate instance against a $10^2$-overhead gate machine. Its discussion also catalogs the costs its floor assumption omits: analog implementation dissipation, Hamiltonian programming cost, and readout noise forcing repetition. CEI adopts its Landauer arithmetic and its floor-not-devices discipline, and extends the classification from problem-substrate pairs to architecture-substrate classes.

Finally, the network-isomorphism framework [14] argues that equivalence between complex systems cannot be captured by a single measure but must be assessed progressively across layers — topological structure, functional architecture, and dynamic behavior — formalized as an L1-L2-L3 hierarchy with an Abstract Network Object as the comparison tool. CEI is deliberately a single-layer, single-scalar proposal; Section 6 discusses what the L1-L2-L3 lesson implies, namely that a one-scalar invariant will miss equivalences and inequivalences that only appear at the dynamic layer.

## 3. Methods

This paper is analytical: it defines a model of substrate-architecture interaction, derives the CEI bound from three physical inputs, proves the associated relation is an equivalence relation, and computes numerical classifications under explicitly stated assumptions. No experiment, measurement, or simulation on hardware was performed; every number is either derived in Section 4 with shown arithmetic, adopted from a cited work with attribution, or labeled an assumption.

**Model.** A computational substrate is a physical medium with (i) an areal power-dissipation limit $p_{\max}$ in $\mathrm{W\,m^{-2}}$, (ii) an active depth $\ell$ in $\mathrm{m}$ over which dissipation occurs, (iii) a minimum feature length $L$ in $\mathrm{m}$, and (iv) an operating temperature $T$. An architecture on that substrate is characterized by two numbers: the causal density

$$\rho_t \;=\; \frac{\text{number of mutually dependent operations}}{\text{volume}\times \text{time}} \quad [\mathrm{m^{-3}\,s^{-1}}],$$

and the energy fidelity

$$\eta_e \;=\; \frac{E_{\mathrm{tr}}}{kT\ln 2} \quad [\text{dimensionless}],$$

where $E_{\mathrm{tr}}$ is the mean energy dissipated per elementary transition. Dependent operations are those that cannot begin before their predecessors complete, so $\rho_t$ counts only causally coupled computation; independent parallel lanes do not increase $\rho_t$ beyond the dependency-limited rate.

**Assumptions.** We assume: (A1) every elementary transition dissipates at least the Landauer limit $kT\ln 2$, the standard thermodynamic floor for irreversible state change, consistent with the $2.871\times 10^{-21}\ \mathrm{J}$ floor at $300\ \mathrm{K}$ derived in [13]; (A2) the substrate cannot sustainably dissipate more than $p_{\max}$ per unit area, so the volumetric budget is $p_{\max}/\ell$; (A3) no causal density can exceed the relativistic bound set by the feature length, $\rho_t \leq c/L^4$, because a dependent operation needs at least one signal traversal of length $L$ (time $\geq L/c$) within a volume of at least $L^3$; (A4) for the worked silicon example, $p_{\max} = 100\ \mathrm{W\,cm^{-2}}$, $\ell = 1\ \mathrm{mm}$, $L = 10\ \mathrm{nm}$, $T = 300\ \mathrm{K}$ — these are stated assumptions standing in for measured platform data, chosen as round representative values, not measurements.

**Derivation and computation plan.** Section 4 proceeds in four steps: (1) derive the power-budget bound on $\rho_t\eta_e$; (2) derive the causal bound and compare; (3) prove the equal-product relation is an equivalence relation and identify its classes as orbits of a rescaling action; (4) place two assumed architecture profiles on the silicon scale and derive the mismatch penalty for a throttled architecture. Section 5 reports only these computed values and clearly labeled projections.

## 4. Analysis

### 4.1 The Landauer constant

Input: Boltzmann constant $k = 1.380649\times 10^{-23}\ \mathrm{J\,K^{-1}}$; $T = 300\ \mathrm{K}$ (Assumption A4); $\ln 2 = 0.6931472$.

$$kT \;=\; (1.380649\times 10^{-23})\times 300 \;=\; 4.141947\times 10^{-21}\ \mathrm{J},$$

$$kT\ln 2 \;=\; (4.141947\times 10^{-21})\times 0.6931472 \;=\; 2.871\times 10^{-21}\ \mathrm{J}.$$

This reproduces the single-bit erasure floor derived in [13], which states the same value $2.871\times 10^{-21}\ \mathrm{J}$ at $300\ \mathrm{K}$, computed from $kT\ln 2$. We denote $\varepsilon_L = 2.871\times 10^{-21}\ \mathrm{J}$.

### 4.2 The power-budget bound on $\rho_t\eta_e$

By Assumption A1, each transition dissipates $E_{\mathrm{tr}} = \eta_e\,\varepsilon_L$. The volumetric rate of transitions is $\rho_t$, so the volumetric dissipated power is

$$P_V \;=\; \rho_t\, E_{\mathrm{tr}} \;=\; \rho_t\,\eta_e\,\varepsilon_L.$$

By Assumption A2, sustainability requires $P_V \leq p_{\max}/\ell$. Therefore

$$\rho_t\,\eta_e \;\leq\; \frac{p_{\max}}{\ell\,\varepsilon_L} \;\equiv\; \kappa.$$

The product $\Pi = \rho_t\eta_e$ is bounded by a constant $\kappa$ that depends only on substrate quantities ($p_{\max}$, $\ell$) and the operating temperature (through $\varepsilon_L$). This is the CEI bound. Its units check: $[\mathrm{W\,m^{-2}}]/([\mathrm{m}][\mathrm{J}]) = \mathrm{m^{-3}\,s^{-1}}$, matching the units of $\rho_t$ with $\eta_e$ dimensionless.

### 4.3 The causal-cone bound and which constraint binds

By Assumption A3, a dependent operation occupies at least a volume $L^3$ and at least a time $L/c$, so

$$\rho_t^{\mathrm{causal}} \;=\; \frac{c}{L^4}.$$

With $c = 2.998\times 10^{8}\ \mathrm{m\,s^{-1}}$ and $L = 10\ \mathrm{nm} = 1.0\times 10^{-8}\ \mathrm{m}$ (Assumption A4):

$$L^4 = (1.0\times 10^{-8})^4 = 1.0\times 10^{-32}\ \mathrm{m^4},$$

$$\rho_t^{\mathrm{causal}} = \frac{2.998\times 10^{8}}{1.0\times 10^{-32}} = 2.998\times 10^{40}\ \mathrm{m^{-3}\,s^{-1}}.$$

The ratio of the causal bound to the power bound:

$$\frac{\rho_t^{\mathrm{causal}}}{\kappa} \;=\; \frac{2.998\times 10^{40}}{3.483\times 10^{29}} \;=\; 8.607\times 10^{13},$$

where $\kappa$ is computed in Section 4.5 below. The causal bound exceeds the power bound by a factor of approximately $8.6\times 10^{13}$: for silicon at the assumed parameters, the power budget, not special relativity, is the binding constraint by roughly fourteen orders of magnitude. The CEI bound is therefore the operative invariant on this substrate, and the causal cone enters only as a far upper ceiling.

### 4.4 Equivalence classes

Define on the set of architecture profiles $(\rho_t, \eta_e)$ the relation

$$(\rho_t, \eta_e) \sim (\rho_t', \eta_e') \quad \Longleftrightarrow \quad \rho_t\,\eta_e = \rho_t'\,\eta_e'.$$

Reflexivity: $\rho_t\eta_e = \rho_t\eta_e$. Symmetry: equality of reals is symmetric. Transitivity: $\rho_t\eta_e = \rho_t'\eta_e'$ and $\rho_t'\eta_e' = \rho_t''\eta_e''$ imply $\rho_t\eta_e = \rho_t''\eta_e''$. Hence $\sim$ is an equivalence relation, and the classes are genuine equivalence classes in the sense required by the methodological standard that a foundational relation be a true equivalence relation, the same standard the Hamiltonian-isomorphism taxonomy verifies for its own relation [13].

The classes admit an orbit description. For $s > 0$ define the rescaling action $s\cdot(\rho_t, \eta_e) = (s\,\rho_t, \eta_e/s)$. Then $\rho_t\eta_e$ is invariant under the action, and conversely any two profiles with the same product are related by $s = \rho_t'/\rho_t$. The equivalence classes are exactly the orbits of this one-parameter action, parameterized by the scalar $\Pi \in (0, \kappa]$. This mirrors the orbit-counting structure of Cayley-graph equivalence, where classes are orbits of the automorphism group acting on generator sets [9], and the coloring-class construction, where classes are orbits of coloring automorphisms [1].

The quotient obligation of [4] — that a function on classes be independent of the representative — is discharged for the mismatch penalty of Section 4.6: the penalty depends only on the ratio $\Pi/\kappa$, which is constant on each class, so any representative of a class receives the same penalty.

### 4.5 Numerical value of $\kappa$ for silicon

Inputs (Assumption A4): $p_{\max} = 100\ \mathrm{W\,cm^{-2}} = 100/(10^{-4})\ \mathrm{W\,m^{-2}} = 1.000\times 10^{6}\ \mathrm{W\,m^{-2}}$; $\ell = 1\ \mathrm{mm} = 1.0\times 10^{-3}\ \mathrm{m}$; $\varepsilon_L = 2.871\times 10^{-21}\ \mathrm{J}$ from Section 4.1.

Volumetric power budget:

$$\frac{p_{\max}}{\ell} = \frac{1.000\times 10^{6}}{1.0\times 10^{-3}} = 1.000\times 10^{9}\ \mathrm{W\,m^{-3}}.$$

CEI constant:

$$\kappa \;=\; \frac{1.000\times 10^{9}}{2.871\times 10^{-21}} \;=\; 3.483\times 10^{29}\ \mathrm{m^{-3}\,s^{-1}}.$$

### 4.6 Placement of two architecture profiles

**Profile S (pipelined CMOS-like).** Assumptions: device density $n_d = 1.0\times 10^{15}\ \mathrm{m^{-3}}$, clock frequency $f = 3.0\times 10^{9}\ \mathrm{s^{-1}}$, activity factor $\alpha = 0.10$, mean energy per transition $E_{\mathrm{tr}} = 1.0\times 10^{-16}\ \mathrm{J}$. All four are stated assumptions, not measurements.

$$\rho_t^{(S)} = n_d\, f\, \alpha = (1.0\times 10^{15})\times(3.0\times 10^{9})\times 0.10 = 3.0\times 10^{23}\ \mathrm{m^{-3}\,s^{-1}},$$

$$\eta_e^{(S)} = \frac{1.0\times 10^{-16}}{2.871\times 10^{-21}} = 3.483\times 10^{4},$$

$$\Pi_S = (3.0\times 10^{23})\times(3.483\times 10^{4}) = 1.045\times 10^{28}\ \mathrm{m^{-3}\,s^{-1}}.$$

Fraction of the bound:

$$\frac{\Pi_S}{\kappa} = \frac{1.045\times 10^{28}}{3.483\times 10^{29}} = 0.0300.$$

Profile S saturates $3.0\%$ of the silicon CEI bound. Consistency check against the power budget: $\rho_t^{(S)} E_{\mathrm{tr}} = (3.0\times 10^{23})\times(1.0\times 10^{-16}) = 3.0