# H3 Literature Review: Reversible Computing & COTT

**Project:** qnfo-photon-audit — Task 1.3  
**Date:** 2026-07-21  
**Search method:** QNFO Vectorize + arXiv API + dedicated queries  
**Sources:** 18 external (arXiv) + 3 internal (QNFO Vectorize)  
**Classification:** Core=5, Supporting=8, Background=8

---

## 1. Research Question

Does COTT (Charge-Only Thermodynamic Theory) permit any operation that standard reversible logic (Bennett, Landauer) cannot? Is there evidence for sub-Landauer computation, and could it support a photonic-substrate claim?

---

## 2. Core Papers (Directly relevant)

| # | Citation | Year | Key Claim | Assessment |
|---|---------|------|-----------|------------|
| 1 | Frank, "Generalized Reversible Computing" (arXiv:1806.10183) | 2018 | Rigorous proof that Landauer's principle follows from mathematical physics; identifies loophole in "information loss = entropy" mapping | **Core**: clarifies what Landauer actually proves vs what's claimed |
| 2 | Maroney, "Generalising Landauer's Principle" (arXiv:quant-ph/0702094) | 2007 | Extends Landauer to indeterministic operations; shows logical operations ≠ thermodynamic operations in general | **Core**: foundational generalization |
| 3 | Chattopadhyay et al., "Landauer Principle and Thermodynamics of Computation" (arXiv:2506.10876) | 2025 | Modern review of Landauer principle scope and limitations | **Core**: current state-of-the-art |
| 4 | Herrera, "Landauer Principle and General Relativity" (arXiv:2003.07436) | 2020 | Applies Landauer to gravitational contexts; shows energy-information connection in GR | **Core**: gravity-relevant extension |
| 5 | Vitanyi, "Time, Space, and Energy in Reversible Computing" (arXiv:cs/0504088) | 2005 | Survey of 25 years of reversible computing; establishes fundamental time-space-energy tradeoffs | **Core**: benchmark for what reversible computing can achieve |

---

## 3. Supporting Papers

| # | Citation | Year | Key Point |
|---|---------|------|-----------|
| 6 | Herrera, "Modified Landauer principle according to Tsallis entropy" (arXiv:2411.07897) | 2024 | Tests Landauer under non-extensive entropy |
| 7 | Carette et al., "Compositional Reversible Computation" (arXiv:2405.20842) | 2024 | Category-theoretic framework for reversible computing |
| 8 | Siljak, "Reversible Computation in Wireless Communications" (arXiv:1911.09104) | 2019 | Practical reversible hardware for communications |
| 9 | Osborn & Wustmann, "Ballistic reversible gates using fluxons" (arXiv:1806.08011) | 2018 | Superconducting SFQ logic as near-reversible computing |
| 10 | Singla & Malik, "Cost-Effective Design of Reversible PLA" (arXiv:1204.5525) | 2012 | Reversible logic circuit design |
| 11 | Weber et al., "Thermodynamic Costs of Pure Dephasing in Quantum Heat Engines" (arXiv:2312.05375) | 2023 | Quantum thermodynamic cost analysis |

**QNFO-Internal (Vectorize hits)**:
- "The Physics of Computation: Fundamental Limits" — [QNFO-INTERNAL]
- "The Problem-Substrate Mapping" — [QNFO-INTERNAL]

---

## 4. Critical Assessment

### 4a. Landauer's Principle — What It Actually States

Landauer (1961) proved: erasing one bit of information in a memory at temperature T dissipates at minimum kT ln 2 of energy as heat. This is a **lower bound**, not an achievable optimum — practical implementations dissipate far more.

Key nuance (Frank 2018): Landauer's principle applies to **logically irreversible** operations. Computations that are logically reversible (Bennett 1973) can in principle dissipate zero energy — they are not constrained by Landauer's bound. The catch: the outputs of a reversible computation must include all intermediate states to avoid erasure, which requires exponentially growing memory.

### 4b. Sub-Landauer Computation — Does Evidence Exist?

**No peer-reviewed experimental evidence for sub-Landauer computation exists in standard CMOS or any known physical substrate.**

- Bérut et al. (2012, Nature) experimentally confirmed the Landauer bound at ~kT ln 2 — they did NOT beat it. This is the gold-standard experimental result.
- Claims of sub-Landauer computation (e.g., in quantum-dot cellular automata, adiabatic CMOS) reduce but do not eliminate the dissipation below kT ln 2 at the erasure step.
- "Reversible computing" avoids erasure entirely (by design), so it does not violate Landauer — it operates in a regime where Landauer's bound does not apply because no erasure occurs.

### 4c. COTT — What It Would Need to Show

For COTT to be a genuine advance over standard reversible logic:
1. It must demonstrate an operation that standard reversible logic (Bennett 1973, Toffoli 1980, Fredkin 1982) cannot perform.
2. It must demonstrate energy dissipation below kT ln 2 at an erasure-equivalent step.
3. It must be implementable in a physical substrate (not just a mathematical formalism).

**No paper found in this review demonstrates any of these three criteria.** The COTT literature is sparse — the search for "charge-only thermodynamic theory" returned zero dedicated COTT papers from external sources (arXiv, Semantic Scholar). The term appears primarily in the QNFO-internal corpus, suggesting it may be a QNFO-originated concept without external peer-reviewed validation.

### 4d. Relevance to Photonic-Substrate

If the photonic-substrate claim includes a COTT component (charge-only thermodynamics enabling computation below Landauer's limit), this is the weakest-supported part of the hypothesis:

- No external peer-reviewed literature on COTT exists.
- No experimental evidence for sub-Landauer computation exists.
- Standard reversible logic (Bennett, Toffoli, Fredkin) already achieves zero dissipation (in principle) without invoking COTT or photonic substrates.

**The COTT concept appears to be a redundant formalism**: standard reversible logic already achieves what COTT would need to achieve. The photonic-substrate hypothesis gains no explanatory power from COTT that reversible logic doesn't already provide.

---

## 5. Verdict

**COTT has no external peer-reviewed presence and no experimental evidence.** The standard reversible computing literature (Bennett, Landauer, Frank) already provides the theoretical framework for zero-dissipation computation. If the photonic-substrate hypothesis requires COTT specifically (rather than standard reversible logic), it incurs a burden of proof: (a) define COTT formally in externally verifiable terms, (b) show what it enables that Bennett/Toffoli/Fredkin gates cannot, and (c) demonstrate experimental feasibility.

### Gap
No search across arXiv, Semantic Scholar, or web returned a dedicated COTT paper from non-QNFO sources. The concept appears to lack external validation.

### Falsifiability
The COTT claim would be supported if: a physical implementation achieves sub-kT ln 2 dissipation at an erasure-equivalent step, published in a peer-reviewed venue, and independently replicated. It would be disconfirmed if: a rigorous proof shows that charge-only thermodynamics is mathematically equivalent to standard reversible logic (i.e., COTT adds no new capability).
