# Radix-Agnostic Detection of Discrete Scale Invariance: A Certified Three-Stage Protocol and a Null Result from Planck 2018

## Abstract

Discrete scale invariance (DSI) — invariance under a discrete set of
rescalings $x \to \lambda^n x$ — predicts log-periodic oscillations whose
angular frequency in the logarithmic coordinate $u = \ln x$ is
$\omega_0 = 2\pi/\ln\lambda$. When the scaling radix $\lambda$ is unknown,
a radix-locked search at assumed radices risks both false negatives (the
true radix was never probed) and multiplicity inflation (a continuum of
probed frequencies is scanned without correction). This work develops and
certifies a radix-agnostic detection protocol in three stages: (1) detrend
in log-space and locate the spectral peak by FFT or Lomb–Scargle
periodogram; (2) refine the peak with a bounded sinusoid fit on the
detrended residuals, yielding $\hat\lambda \pm \sigma_\lambda$; (3) test
candidate radices against the measured value. Certification is mandatory:
a max-statistic bootstrap null (already multiplicity-corrected), a
likelihood-ratio test ($\Delta\mathrm{BIC} > 10$), and three integrity
gates — resolvability ($\omega \ge 2\pi/u_{\rm span}$), amplitude
($\mathrm{SNR} \ge 1$), and radix precision
($\sigma_\lambda/\lambda < 10\%$). On synthetic data with a deliberately
non-prime radix $\lambda = 1.62$, the protocol recovers the radix to
$\le 0.02\%$ error and certifies the detection. Application to the Planck
2018 temperature power spectrum yields **no certified DSI at any
resolvable radix**, including the p-adic radices $\lambda \in \{2,3,5,7\}$
(probed at adequate resolution; fractional power $10^{-4}$–$10^{-3}$). A
model-subtraction variant is mandatory for non-power-law spectra: scanning
the $\Lambda$CDM-subtracted residuals yields a clean null
($p = 0.89$, $\Delta\mathrm{BIC} = -7.3$), consistent with the radix-locked
analyses. The protocol converts the p-adic radix hypothesis from an
assumption into a measurement.

## 1. Introduction

Discrete scale invariance is the symmetry of a system under a discrete
set of rescalings $x \to \lambda^n x$, $n \in \mathbb{Z}$, rather than
under continuous dilations. Its observable fingerprint is a
log-periodic modulation: in the coordinate $u = \ln x$, a DSI quantity
oscillates with angular frequency

$$\omega_0 = \frac{2\pi}{\ln\lambda},$$

so that the radix $\lambda$ is encoded in the frequency of a
logarithmic-domain oscillation. Log-periodic structure has been
documented in growth models [@huang1997dsi], fracture and earthquake
processes [@sornette1995earthquakes], ice-quake precursors
[@faillettaz2008icequakes], financial markets [@drozdz1999stock;
@geraskin2011lppl; @filimonov2013lppl], and physical systems including
ultraquantum topological materials [@wang2018lpo; @wang2019dsi].

A central methodological question concerns the scaling radix $\lambda$.
If a theory predicts a specific radix — for example, the p-adic
hypothesis, under which spacetime structure is valued over $\mathbb{Q}_p$
and DSI inherits the prime radix $\lambda = p$ [@schikhof1984ultrametric;
@avetisov2002padic] — a radix-locked search fixes
$\omega_p = 2\pi/\ln p$ and scans only those frequencies. This is a
legitimate and low-multiplicity confirmation instrument: earlier
radix-locked searches of the cosmic microwave background temperature
spectrum found no detection at global $p = 0.38$ [@qunical03], and the
p-adic two-point and bispectrum searches found consistent nulls
[@quni2026cmb].

But when the radix is unknown — or should not be assumed — the search
must be radix-agnostic: estimate $\omega$ continuously and let
$\lambda$ emerge as a *measured* quantity. This is the discovery
instrument. It pays a multiplicity price: probing a continuum of
frequencies requires correction for the effective number of independent
bins. The log-periodic power-law literature has long warned that joint
fits are over-parameterized [@geraskin2011lppl]; a robust calibration
scheme requires care [@filimonov2013lppl]. This work formalizes the
radix-agnostic protocol, adds a mandatory certification layer, and
demonstrates both a synthetic recovery and a definitive null on real
cosmological data.

## 2. Methods

### 2.1 The three-stage protocol

Given data $(x_i, y_i)$ with $x_i > 0$, set $u_i = \ln x_i$ and
$f_i = \ln y_i$ (the protocol operates in log-space, where a DSI
modulation is sinusoidal).

**Stage 1 — detrend and spectral peak.** Subtract a smooth trend in
log-space (moving average or low-order polynomial), then compute the
power spectrum of the residuals. On uniformly sampled grids use the FFT;
on uneven grids use the Lomb–Scargle periodogram [@press1989lomb;
@zechmeister2009lomb; @vanderplas2018lomb]. The dominant non-DC peak at
$f_0$ cycles per unit $u$ gives $\omega_0 = 2\pi f_0$ and the coarse
estimate $\hat\lambda_0 = e^{2\pi/\omega_0}$.

**Stage 2 — bounded sinusoid refinement.** Fit
$r(u) = C\cos(\omega u + \phi)$ to the *detrended residuals only*, with
$\omega$ bounded to $\pm 5\%$ of the Stage-1 peak. The covariance of the
fit propagates to

$$\sigma_\lambda = \left|\frac{d\lambda}{d\omega}\right|\sigma_\omega
= \left|\frac{\lambda\ln\lambda}{\omega}\right|\sigma_\omega.$$

**Stage 3 — candidate-radix hypothesis test.** With
$\hat\lambda \pm \sigma_\lambda$ in hand, test candidate radices:
integer primes (the p-adic hypothesis), rationals, 5-smooth numbers, or
other theory-specified values. A match found *post hoc* is
retrodiction; the candidate set must be pre-registered before Stage 1
for evidential weight.

### 2.2 Certification

A detection claim is certified only when all of the following hold:

1. **Bootstrap null (max-statistic).** Shuffle the residuals and
   recompute the maximum spectral peak statistic; compare the observed
   maximum against the null distribution. The resulting $p$ is a
   *max-statistic* $p$ — it is already corrected for multiplicity over
   the probed frequency range. Applying a further Sidak correction
   double-counts the look-elsewhere penalty and is incorrect.
2. **Likelihood ratio.** Compare the pure baseline (in log-space, a
   linear model) against baseline plus log-periodic term; require
   $\Delta\mathrm{BIC} > 10$.
3. **Integrity gates.** All three must pass:
   - G1 *Resolvability*: $\omega \ge 2\pi/u_{\rm span}$ — at least one
     full log-periodic cycle must fit in the probed range; a peak below
     this is a trend artifact, not an oscillation.
   - G2 *Amplitude*: residual sinusoid $\mathrm{SNR} \ge 1$.
   - G3 *Radix precision*: $\sigma_\lambda/\lambda < 10\%$.

### 2.3 Model-subtraction mode (G4)

For non-power-law data (e.g. a spectrum with physical structure such as
the $\Lambda$CDM acoustic peaks), the pure-noise bootstrap null is
mis-specified: shuffling destroys real, non-DSI structure and inflates
significance. The correct protocol subtracts the physical model first:

$$r(u) = \ln y_{\rm data} - \ln y_{\rm model},$$

then scans the residuals directly (the detrend step is bypassed; the
residuals are mean-zero by construction). The bootstrap null is valid
because the residuals are noise if the model fits.

### 2.4 Reproducibility

The protocol is implemented in a public script with a built-in
self-test; all numerical claims below were reproduced with fresh random
seeds in the same session.

## 3. Results

### 3.1 Synthetic recovery of a non-prime radix

A synthetic signal with radix $\lambda = 1.62$ — deliberately *not* an
integer prime — was generated with a power-law trend, a
$30\%$ log-periodic modulation, and multiplicative noise at
$\sigma = 2\%$. Stage 1 (FFT) recovered $\lambda = 1.601$
($1.2\%$ error); Lomb–Scargle on a $40\%$-subsampled uneven grid
recovered $\lambda = 1.649$ ($1.8\%$ error). Stage 2 recovered
$\lambda = 1.620$ with $\sigma_\lambda = 0.0002$
($0.01\%$ relative) — an error of $\le 0.02\%$ across three seeds.
Certification passed: bootstrap $p = 0.0033$,
$\Delta\mathrm{BIC} = 24{,}810$, $p_F \approx 0$, and all three
integrity gates.

**A cautionary negative result.** The full six-parameter log-periodic
power-law fit with free $\omega$, even initialized at the true spectral
peak, converged to a degenerate solution ($\lambda \sim 10^9$). This
empirically confirms the over-parameterization warning
[@geraskin2011lppl]: stage separation is not optional.

### 3.2 Null on the Planck 2018 temperature spectrum

The protocol was applied to the Planck 2018 unbinned TT power spectrum
(2507 rows, $\ell \in [2, 2508]$, $D_\ell$ in $\mu\mathrm{K}^2$),
restricted to $\ell \ge 30$ ($N = 2446$, $u_{\rm span} = 4.43$). The
naive raw-spectrum scan produced a low-frequency peak at
$\omega = 0.60$–$0.66$ rad — *below* the minimum resolvable frequency
$2\pi/u_{\rm span} = 1.42$ rad — with $\sigma_\lambda/\lambda$ of
$985$–$1762\%$ and $\mathrm{SNR} = 0.15$. All three integrity gates
rejected it as a trend artifact.

The p-adic radices $\lambda \in \{2,3,5,7\}$, corresponding to
$\omega \in \{9.07, 5.72, 3.90, 3.23\}$ rad, are all resolvable in the
probed range (2.3–6.4 cycles available) and were probed at adequate FFT
resolution ($0.078$ rad). Their fractional spectral power is
$2 \times 10^{-4}$ to $5 \times 10^{-4}$ — a genuine null, in agreement
with the radix-locked searches [@qunical03; @quni2026cmb].

### 3.3 Model-subtraction null

The binned TT spectrum was scanned against the embedded best-fit
$\Lambda$CDM column (83 points, same grid; log-residuals with mean
$-0.004$ and standard deviation $0.040$). The residual scan returned
bootstrap $p = 0.89$ (the observed peak lies *below* the null mean),
$\Delta\mathrm{BIC} = -7.3$ (the sinusoid model is worse than pure
noise), and zero of three gates. This is the definitive null: no
log-periodic structure survives $\Lambda$CDM subtraction at any
resolvable radix.

## 4. Discussion

The contrast between the raw-spectrum artifact and the model-subtraction
null is the central methodological lesson: on non-power-law data,
radix-agnostic scanning requires physical-model subtraction first and
resolvability enforcement. Without these, the detector flags its own
artifact — exactly the look-elsewhere failure mode the integrity layer is
designed to catch.

The multiplicity analysis quantifies the cost of the discovery
instrument: the radix-agnostic scan over the Planck multipole range
carries $N_{\rm eff} \approx 3000$ independent bins, so a nominal
single-bin $p = 10^{-4}$ becomes $p_{\rm global} = 0.26$ after Sidak
correction. The radix-locked search over four primes carries four
hypotheses ($p_{\rm global} \approx 4 \times 10^{-4}$). Radix-locked
confirmation and radix-agnostic discovery are complementary instruments;
the p-adic hypothesis is now constrained by the full continuous radix
coverage, not only by the four locked primes.

The null result is consistent with, and extends, the earlier
radix-locked analyses: no log-periodic signature is found in the Planck
2018 temperature spectrum beyond the $\Lambda$CDM expectation. This is
reported as a null, not as a disconfirmation of the p-adic framework;
the framework's falsifiable content is exactly the class of signature
this protocol is built to detect.

## 5. Conclusion

A certified radix-agnostic protocol for the detection of discrete scale
invariance has been developed, verified on synthetic data with a
non-prime radix, and applied to the Planck 2018 temperature spectrum.
The protocol's certification layer — max-statistic bootstrap null,
likelihood-ratio test, and resolvability/amplitude/precision gates —
distinguishes genuine log-periodic structure from trend artifacts and
model mis-specification. The empirical result is a null: no certified
DSI at any resolvable radix, including the p-adic radices. The method
turns the radix hypothesis from an assumption into a measurement, and is
ready for application to other complex systems where DSI may appear.

## Declarations

**Funding:** No external funding.

**Competing interests:** The author declares no competing interests.

**Data availability:** Planck 2018 TT spectrum is public
(IRSA release 3 ancillary data). Synthetic data are reproducible from
the public implementation's self-test.

**Code availability:** The detector is implemented in a public
repository (see the project's artifact registry).

**Pre-registration:** The p-adic radix-locked search program was
pre-registered at OSF [@quni2026osf].

**Use of artificial intelligence:** The author used an AI assistant for
analysis, drafting, and verification. All numerical results were
independently reproduced with fresh random seeds.

## References
