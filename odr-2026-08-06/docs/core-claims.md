# ODR 2026-08-06 — Core Claims Extracted from 13 Obsidian Notes
# QNFO.RES.003 Phase 0: Locked Claim Set

## C1: Bruhat-Tits Tree as Universal Information Substrate [speculative]
The combinatorial tree $T_{p}$ encoding the p-adic completions of $\mathbb{Q}$ (the Bruhat-Tits building for $\mathrm{PGL}(2,\mathbb{Q}_p)$) manifests as the natural state space for ultrametric quantum information. Each vertex at depth $r$ corresponds to a distinguishable state in a hierarchically organized Hilbert space. The information capacity $I(r) = \log_2|\mathcal{S}_r|$ grows logarithmically with depth — consistent with the observed efficiency of tensor-network shadow tomography on classical hardware (Simons/Flatiron 2026).
- **Source notes:** 83350 (BT Tree Expert), 83607 (Adelic Shannon), 83952 (Quantum Supremacy Rival)
- **Disconfirmation:** If tensor-network methods scale poorly beyond tree-level approximations where p-adic structure disappears → [FALSIFIED]

## C2: Tensor Networks = Classical BT-Tree Computation [speculative]
The Simons/Flatiron breakthrough — solving 100+ qubit quantum dynamics on a laptop using tensor networks — is NOT a defeat of quantum computing. It IS the empirical demonstration that tree-structured (matrix product state / PEPS) classical algorithms are instantiating the BT tree's computational geometry. The "surprise" that classical laptops beat quantum supremacy claims is naturally explained by ultrametric geometry: the correlation structure of local Hamiltonians is p-adically ultrametric, and tree-tensor networks exploit this directly.
- **Source note:** 83952 (Quantum Supremacy Rival)
- **Disconfirmation:** If tensor-network supremacy holds only for 1D/2D lattices and fails for all-to-all or non-local Hamiltonians → [PARTIALLY FALSIFIED — scope limited]

## C3: Quantum Readout = BT-Tree Branch Termination [speculative]
The quantum readout bottleneck — measurement is 100-1000× slower than gates, with fidelities lagging behind — is structural, not engineering. Readout constitutes a boundary traversal in the BT tree: moving from a superposition state (distributed across the tree) to a classical bit string (a single leaf). Per Ostrowski's theorem, this is a change of completion — from the superposition over places to the Archimedean classical result. The Landauer limit $E \geq T \ln 2$ applies at this boundary.
- **Source note:** 83929 (Quantum Readout Bottleneck)
- **Disconfirmation:** If readout speeds improve by 10× without ultrametric-aware encoding → [FALSIFIED]

## C4: Casimir/ZPE Constraints Are Source-Source Interactions [established]
Per Jaffe (2005), the Casimir force is expressible entirely in terms of relativistic source-source interactions — zero-point energy is not "harvestable" in Poincaré-invariant QFT. The cosmological constant is the sole observable of absolute ZPE. This constrains any "ultrametric energy extraction" claims to energy-difference computations, not absolute-vacuum claims.
- **Source note:** 83806 (Casimir ZPE Clarification)
- **Status:** [established — Jaffe 2005, DOI 10.1103/PhysRevD.72.021301]

## C5: General-Purpose Computation Resists Parallelization by Structure [established]
Sequential, branch-heavy, memory-intensive computation — the von Neumann model — resists parallelization and analog/quantum implementation because its control flow is fundamentally discrete and conditional. This is complementary to C2: specialized problems (local Hamiltonian dynamics) are tree-exploitable; general-purpose problems are not.
- **Source note:** 83854 (General-Purpose Sequential Computation), 83750 (Most Efficient Joules)
- **Status:** [mainstream interpretation — Amdahl's Law, memory wall]

## C6: Photic Sneeze / Photosynthesis as Phototransduction Coupling [speculative]
Both the photic sneeze reflex (ACHOO syndrome) and photosynthetic energy conversion are biological phototransduction cascades. The sneeze is a "crossed-wire" information error in the optic-trigeminal pathway; photosynthesis is an optimized quantum-coherent energy transfer. The structural parallel: a photon carries both energy and information (frequency, direction, polarization), and biological systems have evolved decoders that sometimes misroute the information (sneeze) or efficiently capture the energy (photosynthesis). This exemplifies the Landauer-constrained coupling of information and energy in physical systems.
- **Source note:** 84027 (Photic Sneeze Photosynthesis Synthesis)
- **Disconfirmation:** If photic sneeze is proven to have zero information-coupling component (purely mechanical) → [FALSIFIED for the information interpretation]

## Cross-Cutting Meta-Principle
**Each degree of freedom in a physical system costs $\ln 2$ of information capacity.** The BT tree is the geometric bookkeeping for this cost across Ostrowski's completions. Tensor networks, readout bottlenecks, Casimir constraints, and biological phototransduction are all manifestations of the same rule at different scales and substrates.

## Pre-Registered Predictions
1. **REG-ODR0601:** A tensor network with explicit BT-tree encoding will outperform the best current TN on at least one benchmark by ≥5% without increasing bond dimension. [CHECK: 2027]
2. **REG-ODR0602:** Readout fidelity in superconducting qubits will show a measurable p-adic ultrametric signature when qubits are arranged in a tree topology. [CHECK: 2028]
3. **REG-ODR0603:** The photic sneeze reflex latency will correlate with the information content (not just intensity) of the triggering light — supporting an information-processing interpretation. [CHECK: 2027]
