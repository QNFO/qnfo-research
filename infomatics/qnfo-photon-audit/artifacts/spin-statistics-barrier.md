# Spin-Statistics Barrier: Technical Audit Memo

**Project:** qnfo-photon-audit — Task 1.5  
**Date:** 2026-07-21  
**Status:** Phase 1 cross-cutting analysis  
**Tags:** [Established], [Critical Gap]

---

## 1. Theorem Statement

The spin-statistics theorem (Pauli 1940, Streater & Wightman 1964) states:

> In any relativistic quantum field theory in (3+1)-dimensional Minkowski spacetime satisfying the Wightman axioms (Lorentz invariance, positive energy, microcausality, locality of fields), integer-spin particles obey Bose-Einstein statistics and half-integer-spin particles obey Fermi-Dirac statistics.

**Standard assumptions:**
1. Lorentz-invariant vacuum
2. Positive energy spectrum (spectral condition)
3. Microcausality (field commutators vanish at spacelike separation)
4. Locality of field operators
5. The existence of a pre-existing (3+1)-dimensional Minkowski spacetime

---

## 2. Can the Theorem Be Circumvented?

**Yes, but only in specific regimes where one or more assumptions fail.**

### 2a. 2+1 Dimensions: Anyons

In (2+1) dimensions, the spin-statistics theorem generalizes to braid group statistics (Mund 2008, arXiv:0801.3621). Particles can have fractional statistics — anyons — that range continuously between bosonic and fermionic. This is well-established theoretically and confirmed experimentally in fractional quantum Hall systems and Kitaev models (Du et al. 2007, arXiv:0712.2694).

**Relevance to photonic-substrate**: If the pre-geometric photon substrate operates in an effective dimension reduction (e.g., holographic), anyonic behavior is possible. However, the recovered (3+1)-dimensional effective theory must reproduce standard spin-statistics for observed photons.

### 2b. Topological Geons in Quantum Gravity

Dowker & Sorkin (1996, arXiv:9609064; 2001, arXiv:0101042) showed that in quantum gravity with non-trivial spatial topology, particles made from topological geons can have spin and statistics **independent** of each other: "there may exist no connection between spin and statistics." This is the strongest known circumvention — in a gravity regime where spatial topology is dynamical and non-trivial, the standard theorem simply does not hold.

**Relevance to photonic-substrate**: If the photonic substrate is pre-geometric and the TREE structure encodes dynamical topology, this is the closest formal analog to a spin-statistics circumvention route. However, Dowker & Sorkin's geons are gravitational objects, not photonic ones — the mapping is analogical, not proven.

### 2c. Composite Gauge Bosons

Suzuki (2017, arXiv:1707.01589) proved: "When a gauge-invariant local field theory is written in terms of matter fields alone, a composite gauge boson or bosons must be formed dynamically." This means photons can EMERGE as bosonic composites from an underlying fermionic theory — the Bose statistics of the composite photon are a derived property, not a fundamental one.

**Relevance to photonic-substrate**: This is the most favorable route for the hypothesis: if photons are composite objects formed from a fermionic substrate, they naturally inherit Bose statistics at the effective level. The spin-statistics theorem then applies to the composites, not the substrate particles.

### 2d. Emergent Spacetime / Fermi-Point Scenario

Volovik (2007, arXiv:0709.1258) describes gravity emerging from a topologically stable Fermi point in momentum space. In such scenarios, both spacetime AND the spin-statistics relation are emergent low-energy phenomena. At the fundamental (pre-geometric) level, the theorem's assumptions (Lorentz invariance, Minkowski spacetime) are not yet valid.

**Relevance to photonic-substrate**: If the photon substrate genuinely precedes spacetime, the spin-statistics theorem's domain of applicability does not include it. The burden shifts to showing that the recovered effective theory reproduces standard spin-statistics.

---

## 3. Critical Assessment for Photonic-Substrate Hypothesis

### 3a. Domain of Applicability

| Regime | Spin-statistics applies? | Evidence |
|--------|------------------------|----------|
| Standard QFT in 3+1 flat spacetime | **Yes** | Pauli 1940, Wightman axioms |
| 2+1 dimensions | **Modified** (anyons) | Mund 2008, experimental confirmation |
| Quantum gravity with non-trivial topology | **No** (geons violate) | Dowker & Sorkin 1996, 2001 |
| Emergent spacetime (pre-geometric) | **Open question** | No formal proof exists |
| Composite gauge bosons | **Yes** (effective, for composites) | Suzuki 2017 |

### 3b. Verdict

**The spin-statistics theorem is NOT an absolute barrier to the photonic-substrate hypothesis**, but it is a significant constraint:

1. **If photons are fundamental** in the substrate → the substrate must either:
   - (a) operate in a regime where the theorem's assumptions fail (pre-geometric, non-Minkowski), OR
   - (b) violate the theorem explicitly, which would be experimentally observable at some scale

2. **If photons are composite** (emerging from a fermionic substrate) → the theorem is satisfied naturally (Suzuki 2017 route). This is the least problematic path.

3. **Critical gap**: No published work proves or disproves the spin-statistics relation in a genuinely pre-geometric regime where spacetime itself is an emergent property. This is an open question in theoretical physics, not a settled matter.

### 3c. Falsifiability

The photonic-substrate hypothesis would be **disconfirmed** if:
- Experimental tests find photon behavior violating Bose statistics at any accessible energy scale (would rule out emergent-Bose scenario)
- A rigorous proof is established that spin-statistics holds even in pre-geometric regimes (would remove the "open question" escape hatch)

It would be **supported** (not confirmed) if:
- A concrete model maps the TREE topology to a Dowker-Sorkin geon-like circumvention
- The Suzuki composite-boson mechanism is explicitly connected to the substrate's fermionic components

---

## 4. Source Index

| # | Citation | Year | Relevance | Bin |
|---|---------|------|-----------|-----|
| 1 | Dowker & Sorkin, "A Spin-Statistics Theorem for Certain Topological Geons" (arXiv:9609064) | 1996 | **Core** — geons violate spin-statistics in quantum gravity | A |
| 2 | Dowker & Sorkin, "Spin and statistics in quantum gravity" (arXiv:0101042) | 2001 | **Core** — comprehensive review of violation mechanism | A |
| 3 | Mund, "The Spin-Statistics Theorem for Anyons and Plektons in d=2+1" (arXiv:0801.3621) | 2008 | **Core** — generalized theorem for braid statistics | A |
| 4 | Suzuki, "Inevitable emergence of composite gauge bosons" (arXiv:1707.01589) | 2017 | **Core** — proof that composites emerge as bosons | A |
| 5 | Doplicher, "Spin and Statistics and First Principles" (arXiv:0907.5313) | 2009 | **Supporting** — LQT formulation, gravity excluded | B |
| 6 | Santamato & De Martini, "Weyl-gauge invariant proof of the Spin-Statistics Theorem" (arXiv:1604.06253) | 2016 | **Supporting** — gauge-invariant proof | B |
| 7 | Guido & Longo, "An Algebraic Spin and Statistics Theorem" (arXiv:9406005) | 1994 | **Supporting** — algebraic QFT version | B |
| 8 | Volovik, "Fermi-point scenario for emergent gravity" (arXiv:0709.1258) | 2007 | **Supporting** — emergent spacetime, spin-statistics emergent | B |
| 9 | Balachandran et al., "A Novel Spin-Statistics Theorem in (2+1)d Chern-Simons Gravity" (arXiv:0005286) | 2000 | **Supporting** — complete violation possible in CS gravity | B |
| 10 | Du et al., "Experimental simulation of fractional statistics of abelian anyons" (arXiv:0712.2694) | 2007 | **Background** — experimental anyon confirmation | C |
| 11 | Balachandran et al., "Topological Spin-Statistics Theorem for Strings" (arXiv:9202052) | 1992 | **Background** — topological proof for point particles | C |

---

## 5. Recommendations for Phase 1.5 Gate

1. **H1 Gate (g-2 correction)**: Must verify that the proposed photonic substrate model (whether fundamental or composite boson) can account for the anomalous magnetic moment g−2 within existing experimental bounds. The spin-statistics choice affects how the g-factor is computed.

2. **Model registry**: Any specific model invoking one of the circumvention routes (geon-like, composite-boson, or 2+1 dimensional) must be registered and locked before Phase 2 testing begins.

3. **Priority**: The composite-boson route (Suzuki 2017) is the least problematic and most consistent with Standard Model physics. If the hypothesis takes this route, the spin-statistics barrier is dissolved by construction. If it takes the "fundamental photon in pre-geometric regime" route, it incurs an open-theoretical-problem burden.
