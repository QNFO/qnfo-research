# PBO-W-2.1: Cosmological Signatures — CMB Log-Periodic Oscillations

**WBS:** PBO-P2.D1 | **Pillar:** P2 (Cosmological Signatures) | **Date:** 2026-07-16
**Framework:** PBO-D-0.0 (10.5281/zenodo.21389579)

---

## 1. Research Objective

Derive observable cosmological signatures from the PBO framework, specifically log-periodic oscillations in the Cosmic Microwave Background (CMB) power spectrum arising from the ultrametric (Bruhat-Tits tree) structure of distinction space.

## 2. Core Hypothesis

If physical spacetime emerges from the Bruhat-Tits tree structure of recursive distinctions, then the tree's discrete branching structure should leave an imprint on cosmological observables. Specifically, the tree's self-similar scaling under p-adic dilation should produce:

1. **Log-periodic oscillations** in the CMB power spectrum
2. **Discrete scale invariance** rather than continuous scale invariance
3. **Preferred scales** corresponding to tree branching levels

## 3. Mathematical Framework

### 3.1 Bruhat-Tits Tree and Spacetime

The Bruhat-Tits tree $\mathcal{T}_p$ for a p-adic field $\mathbb{Q}_p$ is an infinite regular tree where each vertex has $p+1$ neighbors. In the PBO framework, this tree represents the hierarchical structure of nested distinctions.

The emergent spacetime metric is related to the tree distance $d_T$ by:

$$ds^2 = f(d_T) \cdot \eta_{\mu\nu} dx^\mu dx^\nu$$

where $f$ is a function that maps tree distances to physical scale factors.

### 3.2 Log-Periodic Power Spectrum

If the tree structure imposes discrete scale invariance, the primordial power spectrum should exhibit log-periodic modulation:

$$P(k) = P_0(k) \cdot [1 + A \cos(\omega \ln(k/k_0) + \phi)]$$

where:
- $P_0(k)$ is the standard nearly scale-invariant spectrum
- $A$ is the oscillation amplitude
- $\omega$ is the log-frequency (determined by the tree's p-adic parameter $p$)
- $k_0$ is a reference scale
- $\phi$ is a phase offset

### 3.3 Tree Parameters → Observable Predictions

| Tree Parameter | Observable | Predicted Value | Current Constraint |
|:---------------|:-----------|:----------------|:-------------------|
| Prime $p$ | Oscillation period $\omega$ | $\omega = 2\pi/\ln(p)$ | TBD from CMB data |
| Branching level $n$ | Preferred scale $k_n$ | $k_n = k_0 \cdot p^{-n}$ | Compare to CMB features |
| Tree depth | Maximum log-period | Finite number of oscillations | Bounded by horizon |
| Boundary at infinity | Late-time ISW effect | Correlation with tree boundary structure | Cross-correlation tests |

## 4. Specific Predictions

### 4.1 CMB Temperature Power Spectrum

The CMB TT power spectrum $C_\ell^{TT}$ should exhibit log-periodic oscillations with:

$$\Delta C_\ell / C_\ell \sim A \cdot \cos(\omega \ln(\ell) + \phi)$$

**Prediction:** Oscillations with period $\Delta \ln(\ell) \approx 2\pi/\ln(p)$ for small prime $p$ (2, 3, or 5 are natural candidates for p-adic formulations).

### 4.2 CMB Polarization

Similar oscillations should appear in the E-mode polarization power spectrum $C_\ell^{EE}$ and the TE cross-spectrum with correlated phases.

### 4.3 Matter Power Spectrum

Galaxy surveys (DESI, Euclid) should show corresponding log-periodic features in $P(k)$ at late times, imprinted from the primordial spectrum.

### 4.4 Non-Gaussianity

The tree's discrete structure may produce specific non-Gaussian signatures beyond the standard local, equilateral, and orthogonal templates.

## 5. Comparison to Existing Anomalies

Several observed CMB anomalies may be naturally explained by the tree structure:

| Anomaly | Tree Explanation |
|:--------|:-----------------|
| Low-$\ell$ power deficit | Boundary effect from finite tree depth |
| Hemispherical asymmetry | Tree boundary at infinity asymmetry |
| Cold spot | Deep tree branch anomaly |
| Parity asymmetry | Tree orientation preference |
| ALENS anomaly | Tree structure lensing signature |

## 6. Falsification Criteria

The hypothesis is falsifiable:

1. **Null log-periodic signal**: If a dedicated search finds no log-periodic oscillations with amplitude $A > A_{\text{threshold}}$ at any plausible $p$, the tree-emergence model is ruled out.
2. **Wrong oscillation pattern**: If oscillations are found but with a period incompatible with any prime $p$, the specific tree model is ruled out.
3. **Non-tree non-Gaussianity**: Detection of non-Gaussianity inconsistent with tree-generated templates.

## 7. Data Analysis Strategy

1. **Bayesian search** for log-periodic oscillations in Planck/ACT/SPT CMB data
2. **Template fitting** using tree-derived oscillation templates for $p = 2, 3, 5, 7$
3. **Cross-correlation** of oscillation phase between TT, EE, and TE spectra
4. **Simulation-based inference** on tree parameters from mock CMB skies

## 8. Next Steps

1. Develop CMB analysis pipeline for log-periodic oscillation search
2. Derive oscillation templates for $p=2,3,5$ from the Bruhat-Tits tree
3. Apply to Planck 2018 legacy data
4. Prepare predictions for CMB-S4 and Simons Observatory

## 9. Deliverables

| WBS ID | Deliverable | Target |
|:-------|:------------|:-------|
| PBO-D-2.1 | CMB Oscillation Analysis Pipeline | Python code + documentation |
| PBO-D-2.2 | Planck Data Analysis Results | Log-periodic search report |
| PBO-D-2.3 | Cosmological Signatures Paper | Full research paper |
