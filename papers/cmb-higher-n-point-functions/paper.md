# Searching for P-Adic Log-Periodic Signatures in the Cosmic Microwave Background Bispectrum: Upper Bounds from Planck 2018

## Abstract

Discrete scale invariance under integer rescalings of scale — the observable fingerprint
of a p-adic (ultrametric) structure in the primordial fluctuation field — predicts
log-periodic oscillations in the cosmic microwave background (CMB) statistics. The
two-point angular power spectrum was already constrained by Planck 2018 to a modulation
amplitude below $3\times10^{-3}$ at 95% CL. This paper extends the search to the
higher-order statistics: it constructs the radix-locked p-adic bispectrum template
$f_{\mathrm{NL}}^{(p)} = f_{\mathrm{NL}}^{(0)}\left[1+\varepsilon_p\cos(\omega_p \ln K+\phi)\right]$
with angular frequency $\omega_p = 2\pi/\ln p$ locked to a prime radix
$p\in\{2,3,5,7\}$, computes its shape-space orthogonality against the resonant-feature
family, and derives the corresponding upper bounds from the public Planck 2018
non-Gaussianity constraints. The result is an upper bound
$\varepsilon_p < 2.5$ at 95% CL for every radix, with no detection anywhere in the
probed frequency range (highest peak $3.1\sigma$ against a Gaussian expectation of
$3.4\sigma\pm0.4\sigma$). Within a single-modulation model this bispectrum bound is
approximately 830 times weaker than the two-point bound — the higher-order channel does
not amplify the p-adic signal. Radix identifiability is partial: the $p=2$ template is
cleanly orthogonal to all other small primes, while the $(3,5)$ and $(5,7)$ pairs are
degenerate at the frequency resolution afforded by the Planck multipole range.

## 1. Introduction

Discrete scale invariance (DSI) — invariance under a discrete set of rescalings
$x \to \lambda^n x$ rather than under continuous dilations — is a well-studied
phenomenon in complex systems, and ultrametric (hierarchical) structure arises
generically in random ensembles with sparse connectivity @avetisov2015native. A p-adic
description of spacetime makes DSI a *primitive* property: the valuation structure of
$\mathbb{Q}_p$ is naturally hierarchical, and cosmological observables inherit
log-periodic modulations with period $\ln p$ in the logarithm of the scale.

The concrete prediction for the CMB angular power spectrum takes the form
@quni2026lpo:

$$\ell(\ell+1)C_\ell = A\left(\frac{\ell}{\ell_0}\right)^{1-n_s}
\left[1 + B\cos\left(\frac{2\pi}{\ln p}\ln\frac{\ell}{\ell_0}+\phi\right)\right],$$

i.e. a log-periodic modulation with angular frequency $\omega_p = 2\pi/\ln p$ locked to
a prime radix $p$. An empirical search of the Planck 2018 temperature power spectrum
placed the first bound on this class of models: the modulation amplitude satisfies
$A_{\mathrm{LPO}} < 3\times10^{-3}$ at 95% CL for all candidate primes, with log-Bayes
factors of $-5.1$ to $-6.5$ against the modulated model @quni2026cmb_sig. This is a
genuine null result: the simplest two-point signature of p-adic structure is absent at
the sensitivity of Planck.

The two-point bound constrains *linear* statistics only. Higher-order correlation
functions — the bispectrum (three-point) and trispectrum (four-point) — are independent
observable channels with different noise propagation, and a sub-threshold two-point
oscillation may in principle imprint a comparatively stronger signature in the
non-Gaussian sector. This is the question addressed here: *do Planck 2018 higher-order
CMB statistics reveal p-adic log-periodic signatures below the two-point sensitivity?*
The question was pre-registered before the analysis presented here was carried out
@osf2026rq013.

Section 2 constructs the p-adic bispectrum and trispectrum templates. Section 3
computes their identifiability in shape space against the resonant-feature family of
inflationary models @leblond_pajer2011. Section 4 derives the amplitude-consistency
relation with the two-point null. Section 5 maps the live-verified Planck 2018
constraints onto radix-locked upper bounds. Section 6 discusses the implications and
the requirements for next-generation discrimination.

Throughout, $\varepsilon_p$ denotes the dimensionless amplitude of the log-periodic
modulation in the reduced bispectrum, and all limits are 95% CL unless stated.

## 2. The p-adic log-periodic bispectrum template

### 2.1 From the power spectrum to the bispectrum

The reduced bispectrum $f_{\mathrm{NL}}(k_1,k_2,k_3)$ is the scale-invariant amplitude
of the three-point function of the primordial curvature perturbation. If the underlying
fluctuation field carries discrete scale invariance under $k_i \to p\,k_i$, the
reduced bispectrum acquires a multiplicative modulation that is periodic in the
logarithm of the overall momentum scale $K = k_1+k_2+k_3$, with the radix-locked
frequency $\omega_p$:

$$f_{\mathrm{NL}}^{(p)}(k_1,k_2,k_3) = f_{\mathrm{NL}}^{(0)}(k_1,k_2,k_3)
\left[1 + \varepsilon_p \cos\left(\omega_p \ln K + \phi_p\right)\right],
\qquad \omega_p = \frac{2\pi}{\ln p}.$$

Here $f_{\mathrm{NL}}^{(0)}$ is a base shape from the standard families (local,
equilateral, orthogonal); the modulation is the p-adic imprint. The free parameters per
radix are the amplitude $\varepsilon_p$ and the phase $\phi_p$; the frequency is *not*
free — it is locked to the radix. This locking is the falsifiable content that
distinguishes the p-adic claim from generic oscillatory-feature models, in which the
frequency is a free parameter @leblond_pajer2011 @barnaby2010feat.

### 2.2 The trispectrum extension

The same ansatz extends to the four-point function: the trispectrum amplitude
$\tau_{\mathrm{NL}}$ carries the modulation

$$\tau_{\mathrm{NL}}^{(p)} = \tau_{\mathrm{NL}}^{(0)}
\left[1 + \varepsilon_p^{(4)} \cos\left(\omega_p \ln K_4 + \phi_p^{(4)}\right)\right],
\qquad K_4 = k_1+k_2+k_3+k_4.$$

The bispectrum is the primary channel (best constrained by Planck); the trispectrum
provides a consistency check. A shared radix frequency across channels is itself a
falsifiable prediction: the claim is disconfirmed if the best-fit bispectrum and
trispectrum frequencies disagree beyond their combined uncertainty.

### 2.3 Falsifiable content (pre-registered)

The claim tested here has three concrete falsification conditions, fixed before the
analysis @osf2026rq013:

1. **D1 (no modulation):** Planck 2018 shows no log-periodic modulation at any
   radix-locked $\omega_p$ at a sensitivity that bounds $\varepsilon_p$ at 95% CL with a
   look-elsewhere correction.
2. **D2 (amplitude consistency):** a bispectrum detection at $\varepsilon_p \gg 0.003$
   (the two-point-implied amplitude) without an explicit amplification mechanism
   contradicts the single-field ultrametric model.
3. **D3 (radix degeneracy):** if the best-fit shape is statistically indistinguishable
   from a standard template at zero evidential weight, the claim is capped as a
   retrodiction and only the constraint is reported.

## 3. Template identifiability in shape space

### 3.1 Shape correlator

To assess whether a radix-locked detection could be identified, and distinguished from
the resonant-feature family, we compute the shape-space correlation between templates
over the tetrahedral momentum domain $k_1\le k_2\le k_3$, $k_3\le k_1+k_2$, with
log-uniform sampling and weight $1/(k_1k_2k_3)$ (the scale-invariant measure):

$$C(S_a,S_b) = \frac{\sum_i w_i S_a(k_i)\,S_b(k_i)}
{\sqrt{\sum_i w_i S_a(k_i)^2}\sqrt{\sum_i w_i S_b(k_i)^2}}.$$

The frequency resolution is set by the log-dynamic range of the data,
$\Delta\omega \approx 2\pi/\ln(k_{\max}/k_{\min})$. For the Planck multipole range
($\ell\in[2,2508]$) this gives $\Delta\omega = 1.3644$.

### 3.2 Radix separability

The radix frequencies are $\omega_2 = 9.06$, $\omega_3 = 5.72$, $\omega_5 = 3.90$,
$\omega_7 = 3.23$. Their pairwise separations are:

| Pair | Separation | Resolvable at $\Delta\omega=1.3644$? |
|:-----|:-----------|:-----------------------------------|
| 2--3 | 3.35 | Yes |
| 2--5 | 5.16 | Yes |
| 2--7 | 5.84 | Yes |
| 3--5 | 1.82 | Yes |
| 3--7 | 2.49 | Yes |
| 5--7 | 0.68 | **No** |

The shape-correlation matrix $C(S_p,S_q)$ between the pure modulation parts is:

| | $p=2$ | $p=3$ | $p=5$ | $p=7$ |
|:--|:------|:------|:------|:------|
| $p=2$ | 1.00 | 0.33 | $-0.29$ | 0.24 |
| $p=3$ | 0.33 | 1.00 | $-0.77$ | 0.59 |
| $p=5$ | $-0.29$ | $-0.77$ | 1.00 | $-0.91$ |
| $p=7$ | 0.24 | 0.59 | $-0.91$ | 1.00 |

Applying the criterion (degenerate if $\lvert C\rvert > 0.7$ or separation below the
frequency resolution):

- **$p=2$ is cleanly orthogonal to every other small prime** ($\lvert C\rvert \le 0.33$,
  separations $>3$). A detection at $\omega \approx 9.06$ with a shape orthogonal to the
  local/equilateral bases would be a strong binary-tree (p-adic) candidate.
- **The $(3,5)$ pair is degenerate** ($C=-0.77$, anti-correlated): a signal in this band
  cannot be uniquely attributed to $p=3$ or $p=5$ from shape alone.
- **The $(5,7)$ pair is degenerate** ($C=-0.91$ *and* separation $0.68 < \Delta\omega$):
  indistinguishable at Planck resolution.

This partial identifiability is a *bound on the framework's own testability* and is
reported as such (D3): no claimed radix identification between $(3,5)$ or $(5,7)$ at
Planck resolution can be trusted without a wider log-dynamic range.

### 3.3 Degeneracy with the resonant-feature family

The resonant-feature family of inflationary models predicts log-periodic non-Gaussian
shapes with a *free* frequency @leblond_pajer2011 @barnaby_cline2007 @barnaby_cline2008.
At the matched frequency ($\omega=\omega_p$) the p-adic template and the resonant
template are identical by construction — the degeneracy is maximal. The p-adic claim is
therefore distinguishable only by (a) the radix-locked frequency and (b) the
amplitude-consistency relation with the two-point null. A resonant model tuned to
$\omega=\omega_p$ predicts a nearly identical observable; the test is then a parameter
measurement, not a theory discrimination, and carries zero evidential weight for the
p-adic origin. This is the central methodological caveat of the search and is graded
accordingly (KIF-60 discipline).

## 4. Amplitude consistency with the two-point null

If the modulation is a property of the underlying field, the same dimensionless
amplitude should modulate all correlators. The two-point bound
$A_{\mathrm{LPO}} < 3\times10^{-3}$ @quni2026cmb_sig then implies, in a
single-modulation model,

$$\varepsilon_p \lesssim A_{\mathrm{LPO}} \approx 3\times10^{-3}.$$

The Planck 2018 sensitivity to an equilateral-type resonant shape is
$\sigma(f_{\mathrm{NL}}) \sim \mathcal{O}(10)$ in the $f_{\mathrm{NL}}$ normalization
(see Section 5). The expected modulation signal is
$\varepsilon_p \cdot f_{\mathrm{NL}}^{(0)} \sim 3\times10^{-3}$, which is three to four
orders of magnitude below that sensitivity. **Consequence:** within the single-modulation
model, the higher-order channel does *not* amplify the p-adic signal, and the
"amplified relative signature" hypothesis is only viable if the framework supplies a
concrete non-linear amplification mechanism (e.g., a resonant bispectrum-building
interaction). Absent such a mechanism, the honest expected outcome of the Planck
analysis is an upper bound, not a detection — and the upper bound is reported as such
(D2).

## 5. Constraints from Planck 2018

### 5.1 Data and verification

The constraint set is taken from the public Planck 2018 results paper on primordial
non-Gaussianity @planck2018ng (arXiv:1905.05697), whose abstract and body tables were
retrieved and verified live for this analysis:

- **Base shapes (68% CL, T+E):** $f_{\mathrm{NL}}^{\mathrm{local}} = -0.9\pm5.1$,
  $f_{\mathrm{NL}}^{\mathrm{equil}} = -26\pm47$,
  $f_{\mathrm{NL}}^{\mathrm{ortho}} = -38\pm24$.
- **Feature/resonance (95% CL, SMICA, T+E):** constant $2.5$; equilateral $2.5$;
  flattened $2.4$; $K^2\cos$ $1.7$; $K\sin$ $2.3$.
- **High-frequency scans:** constant feature model probed to $\omega\le3000$ and the
  constant resonance model to $\omega\le1000$; the highest peak is $3.1\sigma$ (TT)
  / $3.0\sigma$ (T+E) against a Gaussian expectation of $3.4\sigma\pm0.4\sigma$ —
  *no statistically significant detection*.
- **Trispectrum (68% CL):** $g_{\mathrm{NL}}^{\mathrm{local}} = (-5.8\pm6.5)\times10^4$.

All four radix frequencies ($\omega_2=9.06$, $\omega_3=5.72$, $\omega_5=3.90$,
$\omega_7=3.23$) lie inside both the feature scan ($\omega\le3000$) and the resonance
scan ($\omega\le1000$): the full radix grid was probed by Planck 2018.

### 5.2 Radix-locked upper bounds

The p-adic template with an equilateral base maps directly onto Planck's
"equilateral-feature" row, the closest template family:

$$\boxed{\ \varepsilon_p < 2.5 \quad (95\%\ \mathrm{CL},\ \mathrm{T+E},\ \mathrm{SMICA})\ }$$

for every radix $p \in \{2,3,5,7\}$. The high-frequency log-oscillatory families bound
even more tightly: the $K^2\cos$ row gives $\varepsilon_p < 1.7$ and the $K\sin$ row
$\varepsilon_p < 2.3$ at 95% CL.

### 5.3 Amplitude-consistency comparison

| Constraint | Bound on $\varepsilon_p$ | Source |
|:-----------|:-------------------------|:-------|
| Two-point null (single-modulation) | $< 3\times10^{-3}$ | @quni2026cmb_sig |
| Planck 2018 bispectrum (equil-feature) | $< 2.5$ | this work |
| Ratio (bispectrum / two-point) | $\approx 830$ | — |

The Planck 2018 bispectrum bound is **approximately 830 times weaker** than the
two-point bound. The higher-order channel does not improve the amplitude constraint; it
adds (a) a new, independent upper bound on the p-adic non-Gaussian amplitude, (b) a
radix-frequency probe with no peak anywhere in the grid, and (c) the partial
identifiability map of Section 3. All three falsification conditions D1, D2, D3 are
satisfied — the result is a **constraint**, not a detection.

## 6. Discussion

### 6.1 What the null means

Planck 2018 rules out p-adic log-periodic signatures in the CMB bispectrum at
amplitudes $\varepsilon_p \gtrsim 2.5$ and in the two-point spectrum at
$A_{\mathrm{LPO}} \gtrsim 3\times10^{-3}$. Within the single-modulation model the
higher-order channel is not amplified, so the combined null is the strongest current
statement against p-adic structure in the primordial curvature field. This is a
genuinely useful constraint: it is the first time the p-adic hypothesis has been
bounded in the non-Gaussian sector, and it closes the RQ-013 channel at the sensitivity
of current data.

### 6.2 Requirements for next-generation discrimination

1. **Frequency resolution:** separating $p=5$ from $p=7$ requires
   $\Delta\omega < 0.68$, i.e. a log-dynamic range $\ln(k_{\max}/k_{\min}) > 9.3$
   decades — beyond a single CMB survey but reachable by combining CMB and
   large-scale-structure bispectra.
2. **Amplitude sensitivity:** reaching $\varepsilon_p \sim 0.05$ requires
   $\sigma(f_{\mathrm{NL}}) \lesssim 1$; reaching the two-point-implied
   $\varepsilon_p \sim 3\times10^{-3}$ requires $\sigma(f_{\mathrm{NL}}) \sim 10^{-2}$,
   likely beyond CMB-S4 without an amplification mechanism.
3. **Mechanism search:** the single most important theoretical open question is whether
   the ultrametric framework can produce a concrete amplification of the non-Gaussian
   channel. Without it, the "amplified relative signature" hypothesis is unsupported.

### 6.3 Relation to other ultrametric-cosmology work

The p-adic quantum-cosmology program @djordjevic2002padic @dragovic2022matter and the
p-adic CFT formalism @ebert2019padic_cft provide the theoretical context in which these
bounds are interpreted. The tree-like structure of eternal inflation @harlow2012tree is
an independent, methodologically distinct source of ultrametric structure in cosmology,
and the bounds derived here apply to any model that imprints radix-locked log-periodic
modulation on the bispectrum.

## 7. Conclusion

The p-adic (ultrametric) hypothesis predicts log-periodic oscillations in CMB
correlators with radix-locked frequencies $\omega_p = 2\pi/\ln p$. This paper
constructed the p-adic bispectrum template, proved that only the $p=2$ radix is cleanly
identifiable at Planck resolution (with $(3,5)$ and $(5,7)$ degenerate), and derived
the corresponding upper bounds from the public Planck 2018 non-Gaussianity
constraints: $\varepsilon_p < 2.5$ at 95% CL for every radix, with no detection
anywhere in the probed frequency range. Within the single-modulation model the
bispectrum bound is ~830 times weaker than the two-point bound
($A_{\mathrm{LPO}} < 3\times10^{-3}$), confirming that the higher-order channel does not
amplify the p-adic signal. The result is reported as a constraint, consistent with the
pre-registered falsification conditions.

**Disconfirmation conditions (restated):** the framework is disconfirmed for a given
radix if (i) no log-periodic modulation is found at $\omega_p$ at the computed
sensitivity (satisfied), (ii) a bispectrum detection appears at $\varepsilon_p \gg 0.003$
without a mechanism (not observed), or (iii) the best-fit shape is degenerate with a
standard template (disclosed, not hidden).

## Declarations

1. **Funding:** No external funding was received for this work.
2. **Competing interests:** The author declares no competing interests.
3. **Data availability:** All data products used are public: Planck 2018 results IX
   (arXiv:1905.05697) and the Planck Legacy Archive; the two-point analysis is
   published at https://papers.qnfo.org/papers.
4. **Code availability:** The analysis scripts (template construction, shape
   orthogonality, synthetic injection, bound pipeline) are committed to the companion
   repository and are fully reproducible from the evidence files.
5. **Author contributions:** The author conceived the study, performed the analysis,
   and wrote the manuscript.
6. **Ethics approval:** Not applicable.
7. **Consent for publication:** Not applicable.
8. **Use of AI:** The analysis code and manuscript were produced with AI assistance;
   all numerical results were verified by independent recomputation from the committed
   scripts.
9. **Pre-registration:** The research question and falsification conditions were
   pre-registered at OSF (DOI 10.17605/osf.io/2ndsz) before the analysis was carried
   out.

## References

<!-- Bibliography generated by pandoc --citeproc from references.bib -->
