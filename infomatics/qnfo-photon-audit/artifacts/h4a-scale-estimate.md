# H4a Scale Estimate: Planck-Scale Ultrametricity to Rydberg Signal

**Project:** qnfo-photon-audit -- Task 1.6
**Date:** 2026-07-21
**Status:** Phase 1 cross-cutting analysis

---

## 1. Question

Can Planck-scale ultrametric structure produce a detectable signal at Rydberg atom energy/length scales, spanning approximately 25 orders of magnitude?

---

## 2. Scale Reference

| Quantity | Planck Scale | Rydberg Scale | Ratio |
|----------|-------------|---------------|-------|
| Length | l_P = 1.616e-35 m | a_0 = 5.292e-11 m | 3.3e24 |
| Energy | E_P = 1.221e19 GeV = 1.956e9 J | E_Ry = 13.606 eV = 2.180e-18 J | 9.0e26 |
| Time | t_P = 5.391e-44 s | tau_Ry = 2.42e-17 s | 4.5e26 |

---

## 3. Standard QFT Scaling

In standard QFT with Planck-scale suppressed operators, effects at E << E_P are suppressed by powers of E/E_P:

E_Ry / E_P = 1.1e-27

This is 27 orders below experimental sensitivity. Standard QG conclusion: undetectable.

---

## 4. Ultrametric Deviation

Ultrametric distance d(x,y) depends on LOWEST COMMON ANCESTOR level, not Euclidean separation.

### 4a. Tree Depth

Levels needed: N = log_p(l_Ry / l_P):

| Branching p | N |
|------------|---|
| p=2 | 82 |
| p=3 | 52 |
| p=10 | 25 |

Tree depth 25-82 levels is large but not absurd.

### 4b. Effective Energy at Mid-Tree (geometric mean)

E_mid = sqrt(E_P x E_Ry) = sqrt(1.956e9 x 2.180e-18) = 4.62e-5 eV = 11.2 GHz

This is in the Ku-band microwave regime -- experimentally accessible.

### 4c. Signal Propagation

If ultrametric metric f(k) is logarithmic in depth: E_eff ~ E_mid = 4.62e-5 eV
If f(k) is exponential: E_eff ~ E_P x exp(-D/2) -- much more suppressed
If f(k) follows standard QFT scaling: E_eff ~ E_Ry/E_P x E_P = E_Ry -- standard QFT

**No principle selects which metric applies.** This is the core problem.

---

## 5. Verdict

**Bin C-: Implausible under standard assumptions; only conceptually possible under specific ultrametric non-locality assumptions lacking independent motivation.**

### Key points:

1. Standard QFT: E_Ry/E_P = 1e-27 -- completely undetectable
2. Ultrametric geometric-mean: 4.62e-5 eV (11.2 GHz) -- testable with current microwave spectroscopy
3. Ultrametric exponential: highly suppressed but derivable only with ad-hoc metric choice
4. **No mechanism selects metric f(k)** -- the theory has zero predictive power at the H4a crossing

### Falsifiability

- A positive Rydberg microwave anomaly matching a derived (not fitted) frequency would support H4a
- A null result to 1e-13 eV precision across 1-100 GHz does NOT falsify H4a because f(k) is free
- **H4a is formally unfalsifiable in its current form**

### Recommendation

Bin C until: (1) tree metric f(k) derived from physical principles, (2) produces concrete falsifiable prediction, (3) different from QED within 3 sigma, (4) pre-registered experimental protocol.

---

## 6. Numerical Reference

l_P = 1.616255e-35 m
E_P = 1.220890e19 GeV  
a_0 = 5.291772e-11 m
E_Ry = 2.179872e-18 J = 13.605693 eV

Ratio (length): a_0 / l_P = 3.28e24
Ratio (energy): E_Ry / E_P = 1.11e-27
Geometric mean: sqrt(E_P x E_Ry) = 4.62e-5 eV = 11.2 GHz
Tree depth (p=3): log_3(3.28e24) = 51.3
