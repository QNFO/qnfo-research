# Archimedean Constants as Measure-Theoretic Artifacts of the Infinite Place: A Reconciled Derivation of the Local Status of $\pi$

## Abstract

Ostrowski's theorem partitions the non-trivial completions of $\mathbb{Q}$ into exactly one Archimedean place ($\mathbb{R}$) and countably many non-Archimedean places ($\mathbb{Q}_p$). Mainstream physics is formulated exclusively at the Archimedean place, and its most ubiquitous transcendental constant, $\pi$, enters through constructions — the Gaussian integral, $\Gamma(1/2)$, circular Haar measure — that exist only there. We ask whether such constants are fundamental or artifacts of restricting to the $\infty$-place. Working from Tate's thesis and Dragovich's adelic quantum mechanics as templates, we show with fully displayed arithmetic: (i) the adelic product formula holds exactly for $x = 2$ and $x = 12$, with no transcendental number appearing anywhere; (ii) the classical Gaussian integral yields $\sqrt{\pi} \approx 1.7724539$ only because the polar-coordinate change of variables imports the Haar measure of the Archimedean circle group, $\mathrm{vol}(S^1) = 2\pi$, while the radial factor contributes the rational value $1/2$; (iii) the $p$-adic local zeta integral $Z_p(s) = (1 - p^{-1})/(1 - p^{-(s+1)})$ is a rational function of $p$ and $p^{-s}$, e.g. $Z_2(2) = 4/7$; and (iv) the completed zeta functional equation check $\Lambda(2) = \Lambda(-1) = \pi/6 \approx 0.5235988$ localizes all transcendental content in the Archimedean factor $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)$. We argue that in an adelic formulation measurement is an Archimedean projection, so $\pi$-dependent terms appear only at the projection step, and we state falsifiable structural predictions with explicit failure modes.

## 1. Introduction

Every non-trivial absolute value on $\mathbb{Q}$ is, by Ostrowski's theorem, equivalent either to the usual real absolute value $|\cdot|_{\infty}$ or to a $p$-adic absolute value $|\cdot|_p$ for some prime $p$ [9], [11]. The completions $\mathbb{R}$ and $\mathbb{Q}_p$ are mutually singular: no sequence of rationals converges simultaneously in two distinct places unless it is eventually constant. Physics, however, is written in the language of $\mathbb{R}$: Hilbert spaces over $\mathbb{C} \cong \mathbb{R}^2$, path integrals over real configuration space, and spectra built on Gaussian integrals. The constants that populate physical formulas — $\pi$ above all — arise from real-place analytic constructions whose non-Archimedean analogs either do not exist or have a different, algebraic character.

This paper advances and partially substantiates a conjecture: **constants that arise only from Archimedean constructions are measure-theoretic artifacts of the $\infty$-place, not fundamental invariants of nature.** A fully adelic formulation of a physical theory should factorize into local dynamics at each place, with transcendental constants appearing only in the Archimedean projection that corresponds to measurement.

Our strategy is constructive rather than philosophical. We select constants with canonical physical roles ($\pi$ via the Gaussian integral and $\Gamma(1/2)$; the normalization of the Riemann zeta functional equation), derive each with fully shown arithmetic from its Archimedean construction, exhibit the corresponding $p$-adic object where one exists, and identify precisely where the transcendental content enters. The punchline, anticipated by Tate's thesis and visible in the adelic dynamics literature [1], [6], is that global adelic statements (functional equations, product formulas, reciprocity laws) are built from algebraic or number-theoretic local data at every finite place, with the transcendental factor concentrated at $\infty$. Quadratic reciprocity — a statement about finite fields with no transcendental content — then serves as the model for what "replaces $\pi$" in the global theory.

We do not claim a completed adelic reformulation of physics. We claim a precise, checkable structural observation: in every canonical example we analyze, $\pi$ enters through the Archimedean local factor alone, and the finite-place factors are rational or algebraic. This is the sense in which $\pi$ is derivative.

## 2. Background and Related Work

**Adelic physics.** Dragovich's review [5] surveys applications of non-Archimedean geometry, $p$-adic numbers, and adeles in mathematical physics, including $p$-adic and adelic quantum mechanics, $p$-adic string amplitudes, and adelic path integrals. It establishes the key technical fact on which we build: quantum amplitudes can be constructed as products of local factors, one per place, with the Archimedean factor recovering ordinary quantum mechanics. Our claim that $\pi$-terms concentrate in the Archimedean factor is a refinement of exactly this product structure.

**The artifact taxonomy.** The QNFO taxonomy [9] and its v2.0 extension [11] catalogue "measure-theoretic artifacts" of the Archimedean place across several categories and document completion failures — structures that exist at $\infty$ but not at any $p$-place — providing the conceptual vocabulary (artifact, completion failure, place-restriction) that we make precise here for $\pi$ specifically. The place-theoretic treatment of Ostrowski's theorem in [10] supplies the formal backdrop for this vocabulary: it recasts the classification of absolute values on $\mathbb{Q}$ as an arithmetic of places, which is the framework in which "artifact of the $\infty$-place" acquires a precise meaning. The natural-units program of [12] strips anthropocentric content from physical bounds and observes that Ostrowski's theorem exposes the Archimedean completion as one choice among many; our treatment of $\pi$ as a place-dependent constant is the spectral/integral counterpart of that unit-independence argument.

**Adelic equidistribution.** Baker–Rumely and Favre–Rivera–Letelier proved the arithmetic equidistribution theorem for points of small height on the Berkovich projective line with respect to adelic measures, with a more general curve version due to Chambert-Loir [1]. This is the strongest existing template for "global adelic measure with local projections": a single global object whose place-wise projections each carry their own Haar-type measure theory. Favre and Rivera-Letelier's companion characterization [6] determines when equidistribution with moving targets holds for rational functions over any complete field, in any characteristic; its place-agnostic formulation confirms that the equidistribution machinery does not privilege $\infty$, supporting our thesis that Archimedean-specific constants cannot be fundamental to the global theory.

**Adelic line bundles and rigidity.** Yuan's arithmetic Hodge index theorem for adelic line bundles [2] extends from number fields to finitely generated fields and yields rigidity of preperiodic points of polarizable dynamical systems. The adelic line-bundle formalism — metrized at every place, with the Archimedean metric analytic and the non-Archimedean metrics algebraic — is exactly the geometric scaffolding in which "transcendental at $\infty$, algebraic elsewhere" becomes a theorem-shaped statement.

**Adelic tori.** The theorem that finite-dimensional protori (compact connected abelian groups) are adelic tori, with a complete Lie theory built on an adelic exponential [3], is directly relevant to the status of $e$ and $\pi$: the classical exponential map and the $2\pi$-periodicity of the circle are Archimedean Lie-theoretic phenomena, while [3] shows the adelic category carries its own, structurally different exponential with no $2\pi$-periodicity. This is precisely the kind of "replacement" our conjecture predicts for transcendental constants.

**Local-field root counts.** The adelic Tau conjecture literature [7] bounds the number of non-degenerate roots of fewnomial systems over any local field $L$, with bounds depending on $n$, $k$, and $L$. Notably, the "fixed phase" condition in the root-counting problem is an Archimedean notion (phases live in the circle group); over $\mathbb{Q}_p$ the analogous structure is the group of roots of unity, which is finite. This concretely illustrates how circle-group phenomena — the source of $\pi$ — have no direct $p$-adic counterpart.

**Terminology caution.** The "Archimedean copulas" of statistics [4] share a name but not a mathematical mechanism with our Archimedean place; we cite [4] only to flag this terminology collision and note that its spline-generator machinery is unrelated to valuation theory.

**Projection artifacts in engineering.** The study of upsampling artifacts in neural audio synthesis [8] offers a heuristic analogy: checkerboard-pattern distortions arise when a signal valid on one grid is projected onto another, and the artifact pattern is a fingerprint of the projection operator, not of the underlying signal. We use this as a model for "constants that appear only after Archimedean projection."

## 3. Methods

### 3.1 Framework: places, Haar measures, and local zeta integrals

Let $S = \{\infty, 2, 3, 5, \dots\}$ denote the set of places of $\mathbb{Q}$. For each place $v$, let $\mathbb{Q}_v$ be the completion ($\mathbb{R}$ or $\mathbb{Q}_p$) with absolute value $|\cdot|_v$, normalized so that $|p|_p = p^{-1}$ and $|\cdot|_{\infty}$ is the usual absolute value. Each $\mathbb{Q}_v$ carries a Haar measure $dx_v$, normalized by $\mathrm{vol}_{dx_{\infty}}([0,1]) = 1$ and $\mathrm{vol}_{dx_p}(\mathbb{Z}_p) = 1$. The adelic ring is the restricted product $\mathbb{A}_{\mathbb{Q}} = \prod_v' \mathbb{Q}_v$. The foundational identity we exploit is the **product formula**: for every $x \in \mathbb{Q}^{\times}$,

$$\prod_{v} |x|_v = 1.$$

Following Tate's thesis (as surveyed in the adelic-physics context of [5]), the local zeta integral attached to the character $\chi_v(x) = |x|_v^s$ is

$$Z_v(s) = \int_{\mathbb{Q}_v^{\times}} |x|_v^s \, \mathbf{1}_{\mathcal{O}_v}(x)\, dx_v,$$

where $\mathcal{O}_p = \mathbb{Z}_p$; the global object is the restricted product $Z_{\mathrm{ad}}(s) = \prod_v Z_v(s)$, convergent for $\mathrm{Re}(s) > 1$.

### 3.2 Diagnostic criterion for "artifact of the $\infty$-place"

We declare a constant $c$ an *Archimedean artifact* if it satisfies both:

- **(A1)** $c$ appears in the Archimedean local factor or in the Haar-measure normalization of an Archimedean Lie group appearing in physical formulas; and
- **(A2)** no $p$-adic local factor contains $c$; the $p$-adic contributions are rational functions of $p$ and $p^{-s}$.

The conjecture under test is that all "fundamental-looking" appearances of $\pi$ in quantum mechanics satisfy (A1)–(A2), and that global adelic identities are governed instead by product formulas (e.g., quadratic reciprocity in the form $\prod_v (a,b)_v = 1$ for the Hilbert symbol).

### 3.3 Test structures

We analyze: (S1) the Gaussian integral $\int_{\mathbb{R}} e^{-x^2}\,dx$ and $\Gamma(1/2) = \sqrt{\pi}$; (S2) the completed zeta factorization $\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$ and its functional equation; (S3) the factorization of adelic quantum mechanics into local dynamics with Archimedean measurement, following the adelic path-integral template of [5]. For (S3) we give the structural derivation and state the computational verification program (adelic harmonic oscillator, adelic CFT partition functions in the style of the equidistribution framework of [1], [6]) as a labeled projection with stated assumptions, not as a completed computation.

### 3.4 Adelic factorization of quantum mechanics

Following [5], we postulate that a physical amplitude is an adelic object $\mathcal{A}_{\mathrm{ad}} = \prod_v \mathcal{A}_v$ with $\mathcal{A}_v : \mathbb{Q}_v \to \mathbb{C}$ (the target $\mathbb{C}$ itself being an Archimedean choice — a caveat we return to in Section 6). Measurement is modeled as the Archimedean projection $\mathcal{A}_{\mathrm{ad}} \mapsto \mathcal{A}_{\infty}$. The structural test is whether the dynamics at each $v \neq \infty$ can be written without $\pi$, with $\pi$-terms appearing only in $\mathcal{A}_{\infty}$ and in the projection functional.

## 4. Analysis

### 4.1 The product formula: two worked examples

**Input 1:** $x = 2$ (elementary arithmetic). Local absolute values: $|2|_{\infty} = 2$; $|2|_2 = 2^{-v_2(2)} = 2^{-1} = 0.5$; $|2|_p = p^{-v_p(2)} = p^0 = 1$ for every odd prime $p$ (since $2$ is a $p$-adic unit). Then

$$\prod_v |2|_v = 2 \times 0.5 \times \prod_{p \neq 2} 1 = 1.$$

**Input 2:** $x = 12 = 2^2 \cdot 3$. Then $|12|_{\infty} = 12$, $|12|_2 = 2^{-2} = 0.25$, $|12|_3 = 3^{-1} = 1/3$, $|12|_p = 1$ otherwise. Product:

$$12 \times 0.25 \times \frac{1}{3} = \frac{12}{12} = 1.$$

The product formula holds with **no transcendental number appearing anywhere**: it is a purely arithmetic identity, the prototype of a global adelic law with zero Archimedean transcendence.

### 4.2 Where $\pi$ enters the Gaussian integral (S1)

Define $I_1 = \int_{\mathbb{R}} e^{-x^2}\, dx$. Since the integrand is even and positive, $I_1 > 0$, and

$$I_1^2 = \left(\int_{\mathbb{R}} e^{-x^2}\,dx\right)\left(\int_{\mathbb{R}} e^{-y^2}\,dy\right) = \int_{\mathbb{R}^2} e^{-(x^2 + y^2)}\, dx\, dy.$$

Apply the polar-coordinate map $(x, y) = (r\cos\theta, r\sin\theta)$. The Jacobian determinant is

$$\det \frac{\partial(x,y)}{\partial(r,\theta)} = \det \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = r\cos^2\theta + r\sin^2\theta = r.$$

Hence

$$I_1^2 = \int_0^{2\pi} \!\! \int_0^{\infty} e^{-r^2}\, r \, dr \, d\theta.$$

The angular integral is the Haar measure of the circle group $S^1$, $\int_0^{2\pi} d\theta = 2\pi$; the radial integral is, with substitution $u = r^2$, $du = 2r\,dr$:

$$\int_0^{\infty} e^{-r^2} r\, dr = \frac{1}{2}\int_0^{\infty} e^{-u}\, du = \frac{1}{2}.$$

Therefore

$$I_1^2 = 2\pi \cdot \frac{1}{2} = \pi, \qquad I_1 = \sqrt{\pi}.$$

Numerically, $\pi \approx 3.1415926536$; a check: $1.7724539^2 = 1.7724539 \times 1.7724539 \approx 3.1415927$, so

$$I_1 = \sqrt{\pi} \approx 1.7724539.$$

**Diagnosis.** The integrand $e^{-x^2}$ is place-agnostic in spirit; the constant $\pi$ enters *exclusively* through the factor $\mathrm{vol}(S^1) = 2\pi$, i.e., through the Haar measure of the Archimedean rotation group. The radial factor contributed the rational value $1/2$. Over $\mathbb{Q}_p$ the analogous "rotation group" — the orthogonal group of a quadratic form over $\mathbb{Q}_p$ — is a totally disconnected $p$-adic Lie group whose Haar measure contributes only rational factors in $p$ (Section 4.3). This establishes (A1) for $\sqrt{\pi}$ via the Gaussian.

The same mechanism gives $\Gamma(1/2) = \sqrt{\pi}$: from $\Gamma(1/2)^2 = B(1/2, 1/2)\,\Gamma(1)$ and $B(1/2, 1/2) = \int_0^1 \frac{dt}{\sqrt{t(1-t)}}$, substituting $t = \sin^2\theta$ (so $dt = 2\sin\theta\cos\theta\,d\theta$ and $\sqrt{t(1-t)} = \sin\theta\cos\theta$ on $(0, \pi/2)$) gives $B(1/2,1/2) = \int_0^{\pi/2} 2\,d\theta = \pi$. Again the transcendence enters through the angular substitution — the circle again.

### 4.3 The $p$-adic local integral contains no $\pi$ (A2 check)

Compute $Z_p(s) = \int_{\mathbb{Z}_p} |x|_p^s\, dx_p$ with $\mathrm{vol}(\mathbb{Z}_p) = 1$. Partition $\mathbb{Z}_p$ into shells: $\mathbb{Z}_p = \{0\} \cup \bigsqcup_{k \geq 0} p^k\mathbb{Z}_p^{\times}$, where $|x|_p = p^{-k}$ on $p^k\mathbb{Z}_p^{\times}$ and

$$\mathrm{vol}(p^k\mathbb{Z}_p^{\times}) = \mathrm{vol}(p^k\mathbb{Z}_p) - \mathrm{vol}(p^{k+1}\mathbb{Z}_p) = p^{-k} - p^{-(k+1)} = p^{-k}(1 - p^{-1}).$$

Then

$$Z_p(s) = \sum_{k=0}^{\infty} p^{-ks} \cdot p^{-k}(1 - p^{-1}) = (1 - p^{-1}) \sum_{k=0}^{\infty} p^{-k(s+1)} = \frac{1 - p^{-1}}{1 - p^{-(s+1)}}.$$

This is a rational function of $p$ and $p^{-s}$: **no $\pi$ appears at any prime place**, confirming (A2). Concrete instance at $s = 2$, $p = 2$:

$$Z_2(2) = \frac{1 - \frac{1}{2}}{1 - 2^{-3}} = \frac{\frac{1}{2}}{1 - \frac{1}{8}} = \frac{\frac{1}{2}}{\frac{7}{8}} = \frac{4}{7} \approx 0.5714286.$$

Arithmetic check: $1 - 2^{-3} = 1 - 0.125 = 0.875 = 7/8$; $(1/2) \div (7/8) = (1/2)(8/7) = 4/7$.

A related, differently normalized object is the $p$-adic Gaussian integral with the additive character $\chi_p(x) = e^{2\pi i \{x\}_p}$, where $\{x\}_p \in \mathbb{Q} \cap [0,1)$ is the fractional part of the $p$-adic expansion. For $x \in \mathbb{Z}_p$ one has $\{x\}_p = 0$ (integers have zero fractional part), so with $\mathrm{vol}(\mathbb{Z}_p) = 1$,

$$G_p = \int_{\mathbb{Z}_p} \chi_p(x)\, dx_p = \int_{\mathbb{Z}_p} 1\, dx_p = 1 \quad \text{exactly, for every } p.$$

**Comparison:**

$$G_{\infty} = \sqrt{\pi} \approx 1.7724539 \ \text{(transcendental)}, \qquad G_p = 1 \ \text{(rational, for all } p\text{)}.$$

The transcendence of the Gaussian integral is entirely an $\infty$-place phenomenon; the finite-place Gaussians are unity. (The two normalizations $Z_p$ and $G_p$ are documented as a convention divergence in Appendix A.)

### 4.4 The completed zeta function: transcendental content is local to $\infty$ (S2)

The completed Riemann zeta function is

$$\Lambda(s) = \pi^{-s/2}\,\Gamma\!\left(\frac{s}{2}\right)\,\zeta(s),$$

the product of the Archimedean local factor $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)$ with the Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$, whose factors are the $p$-adic local zeta integrals up to normalization. It satisfies $\Lambda(s) = \Lambda(1 - s)$.

**Explicit two-sided verification at $s = 2$ and $s = -1$.**

*Side 1, $s = 2$.* Inputs: $\zeta(2) = \pi^2/6$ (Euler's Basel value); $\Gamma(1) = 1$. Then

$$\Lambda(2) = \pi^{-1}\,\Gamma(1)\,\frac{\pi^2}{6} = \pi^{-1} \cdot 1 \cdot \frac{\pi^2}{6} = \frac{\pi}{6} \approx 0.5235988,$$

using $\pi^{-1} \approx 0.3183099$ and $\pi^2/6 \approx 1.6449341$: $0.3183099 \times 1.6449341 \approx 0.5235988$.

*Side 2, $s = -1$.* Inputs: $\zeta(-1) = -1/12$ (standard zeta-regularization value); $\Gamma(-1/2)$ from the recurrence $\Gamma(z+1) = z\,\Gamma(z)$ with $z = -1/2$: $\Gamma(1/2) = -\frac{1}{2}\Gamma(-1/2)$, so $\Gamma(-1/2) = -2\,\Gamma(1/2) = -2\sqrt{\pi} \approx -3.5449077$. Then

$$\Lambda(-1) = \pi^{1/2}\,\Gamma\!\left(-\frac{1}{2}\right)\,\zeta(-1) = \sqrt{\pi} \cdot (-2\sqrt{\pi}) \cdot \left(-\frac{1}{12}\right).$$

Step by step: $\sqrt{\pi} \cdot (-2\sqrt{\pi}) = -2\pi$; $(-2\pi) \cdot (-1/12) = \frac{2\pi}{12} = \frac{\pi}{6} \approx 0.5235988$.

Both sides agree: $\Lambda(2) = \Lambda(-1) = \pi/6 \approx 0.5235988$. The functional equation holds, and the *only* place where a transcendental constant enters either evaluation is the factor $\Gamma_{\mathbb{R}}$: the $p$-adic side of $\zeta(2)$, namely $\prod_p (1 - p^{-2})^{-1}$, is a product of rational numbers, and $\zeta(-1) = -1/12$ is rational.

**Partial Euler product at $s = 2$.** Finite factors for $p = 2, 3, 5$:

$$\zeta_2(2) = \frac{1}{1 - 2^{-2}} = \frac{1}{1 - 0.25} = \frac{4}{3}, \qquad \zeta_3(2) = \frac{1}{1 - 3^{-2}} = \frac{9}{8}, \qquad \zeta_5(2) = \frac{1}{1 - 5^{-2}} = \frac{25}{24}.$$

Partial Euler product over $p \leq 5$:

$$P_5 = \frac{4}{3} \times \frac{9}{8} \times \frac{25}{24} = \frac{4 \times 9 \times 25}{3 \times 8 \times 24} = \frac{900}{576} = 1.5625 \quad \text{(exact)}.$$

Combined with the Archimedean factor $\zeta_{\infty}(2) = \pi^{-1}\Gamma(1) = 1/\pi \approx 0.3183099$:

$$\zeta_{\infty}(2) \times P_5 \approx 0.3183099 \times 1.5625 \approx 0.4973592.$$

For reference, the full value $\zeta(2) = \pi^2/6 \approx 1.6449341$ (with $\pi^2 = 3.1415926536^2 \approx 9.8696044$, computed as $3 \times 3.1415926536 = 9.4247779608$ plus $0.1415926536 \times 3.1415926536 \approx 0.4448264403$). The residual factor from primes $p > 5$ is $1.6449341 / 0.4973592 \approx 3.307$, consistent with $\prod_{p > 5}(1 - p^{-2})^{-1} > 1$.

**Structural reading:** every finite-place factor is rational ($\frac{4}{3}, \frac{9}{8}, \frac{25}{24}$); the transcendence of $\zeta(2) = \pi^2/6$ is carried by $\Gamma_{\mathbb{R}}(2) = 1/\pi$ together with the infinite product's limit, which is a number-theoretic (reciprocity-type) object.

### 4.5 Quadratic reciprocity as the $\pi$-replacement

The number of solutions to $x^2 \equiv a \pmod{p}$ for $p \nmid a$ is $1 + \left(\frac{a}{p}\right)$, where $\left(\frac{a}{p}\right) \in \{\pm 1\}$ is the Legendre symbol — a purely algebraic invariant. **Worked example:** $a = 2$, $p = 7$. By the supplementary law, $\left(\frac{2}{p}\right) = 1$ iff $p \equiv \pm 1 \pmod{8}$. Since $7 \equiv -1 \pmod{8}$, $\left(\frac{2}{7}\right) = 1$. Direct check: $3^2 = 9 \equiv 2 \pmod{7}$, so $x = 3, 4$ are the two solutions, and $1 + \left(\frac{2}{7}\right) = 2$.

The supplementary laws $\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2}$ and $\left(\frac{2}{p}\right) = (-1)^{(p^2-1)/8}$ are the finite-place analogs of what the Archimedean theory encodes through angles and $\pi$: counting solutions to quadratic equations globally requires no transcendental constant at any finite place. In the adelic functional equation, the global intertwining of $\zeta(s)$ and $\zeta(1-s)$ is mediated at finite places by these algebraic symbols and at $\infty$ by $\pi^{-s/2}\Gamma(s/2)$ — i.e., by the Gamma-function reflection formula, whose $\pi$ is again the circle period.

### 4.6 Adelic quantum mechanics: structural result and labeled projections (S3)

Following [5], the Hilbert space of adelic QM is a restricted tensor product $\mathcal{H}_{\mathrm{ad}} = \hat{\otimes}_v \mathcal{H}_v$; time evolution factorizes, $U_{\mathrm{ad}}(t) = \prod_v U_v(t)$, because the Hamiltonian is a sum of place-local terms; and every *measurement outcome* is a real number, hence a homomorphism from the adelic configuration space to $\mathbb{R}$ — an Archimedean projection $\pi_{\infty}$. Consequently, any $\pi$-dependent normalization of amplitudes (Gaussian wave packets, Fresnel phases, $\Gamma(1/2) = \sqrt{\pi}$) appears only in $\mathcal{A}_{\infty}$ or in the projection postulate, never in the $p$-adic factors. The adelic exponential theory of [3] makes this precise at the group level: the adelic torus carries its own exponential with no $2\pi$-periodicity, so the circle-group origin of $\pi$ (Section 4.2) is absent from the adelic Lie theory. Likewise, the "phase" of a complex number is an Archimedean notion with no $p$-adic analog beyond finite roots of unity, as reflected in the fixed-phase hypothesis of local-field root-counting [7].

**Verification program (labeled projections, not completed computations).**

- **(V1) Adelic harmonic oscillator.** Assumption: the $p$-adic harmonic oscillator path integral of [5] produces local eigenvalue products $E_p$ that are rational functions of $p$ and of the frequency parameter, while $E_{\infty} \propto \hbar\omega(n + 1/2)$ carries the Archimedean structure (the $1/2$ tracing to the Gaussian ground state of Section 4.2). Projection: the global spectrum is $\prod_v E_v$, and $\pi$ appears only through $\Gamma_{\mathbb{R}}$-type factors at $\infty$. Uncertainty: this is a structural prediction from the factorization ansatz; a full computation requires evaluating the $p$-adic oscillator spectra, which we have not performed here.
- **(V2) Adelic CFT partition functions.** Assumption: partition functions in the equidistribution framework of [1], [6] admit adelic measures whose place-wise projections are computed by the arithmetic equidistribution theorem. Projection: the global partition function's functional equation is governed by reciprocity invariants (Hilbert-symbol product formula $\prod_v (a,b)_v = 1$), with transcendental constants confined to the $\infty$-factor, in analogy with the $\Lambda(s)$ factorization verified in Section 4.4. Uncertainty: the analogy with [2]'s adelic line bundles suggests but does not prove the factorization for CFT data.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are simulated or measured.

- **R1 (Product formula, exact).** $\prod_v |2|_v = 1$ and $\prod_v |12|_v = 1$, both verified exactly (Section 4.1). Global adelic laws can be entirely transcendental-free.
- **R2 (Gaussian split, exact + numeric).** $I_1^2 = 2\pi \cdot \frac{1}{2} = \pi$, so $G_{\infty} = \sqrt{\pi} \approx 1.7724539$; the angular factor contributes $2\pi$ (transcendental), the radial factor $\frac{1}{2}$ (rational). For every prime $p$, the character-normalized $p$-adic Gaussian is $G_p = 1$ exactly (Section 4.3).
- **R3 ($p$-adic local integral).** $Z_p(s) = \dfrac{1 - p^{-1}}{1 - p^{-(s+1)}}$, a rational function of $p$ and $p^{-s}$; at $s = 2$, $p = 2$: $Z_2(2) = 4/7 \approx 0.5714286$ (Section 4.3). No $\pi$ at any prime place.
- **R4 (Functional-equation check).** $\Lambda(2) = \pi^{-1}\Gamma(1)\zeta(2) = \pi/6 \approx 0.5235988$ and $\Lambda(-1) = \sqrt{\pi}\,(-2\sqrt{\pi})(-1/12) = \pi/6 \approx 0.5235988$; the two independent evaluations agree, and the transcendental content is entirely in the Archimedean factor $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)$ (Section 4.4).
- **R5 (Partial Euler product).** $\zeta_2(2) = \frac{4}{3}$, $\zeta_3(2) = \frac{9}{8}$, $\zeta_5(2) = \frac{25}{24}$; $P_5 = \frac{900}{576} = 1.5625$ exactly; $\zeta_{\infty}(2) \times P_5 \approx 0.4973592$; full $\zeta(2) = \pi^2/6 \approx 1.6449341$; the residual factor from primes $p > 5$ is $\zeta(2)/(\zeta_{\infty}(2)\,P_5) \approx 1.6449341/0.4973592 \approx 3.307$, consistent with $\prod_{p > 5}(1 - p^{-2})^{-1} > 1$ (Section 4.4). Every finite-place factor is rational; the transcendence of $\zeta(2)$ is carried by the Archimedean factor $\Gamma_{\mathbb{R}}(2) = 1/\pi$ together with the number-theoretic limit of the Euler product.

## 6. Discussion

**Limitations.** (i) The target space of adelic amplitudes, $\mathbb{C} \cong \mathbb{R}^2$, is itself an Archimedean object; a fully place-agnostic formulation would require a target without a distinguished Archimedean structure, and we have not constructed one. (ii) Our results are structural identities on canonical examples (Sections 4.1-4.5), not a reformulation of any physical theory; the verification program of Section 4.6 is a labeled projection with stated assumptions, not a completed computation. (iii) The diagnosis that $\pi$ enters 'only' through $\mathrm{vol}(S^1) = 2\pi$ presupposes the polar-coordinate factorization; other derivations of the Gaussian integral may obscure, though not remove, the circle-group origin of the constant.

**Failure modes and falsifiability.** The central claim - that $\pi$-content is confined to the $\infty$-place - would be falsified by any of: (F1) a $p$-adic local factor of a canonical physical amplitude containing $\pi$ or $\Gamma$-values at a finite place (e.g., a $p$-adic oscillator spectrum with eigenvalues involving $\pi$); (F2) a global adelic identity whose finite-place part requires a transcendental normalization; (F3) a completed adelic CFT partition function (V2) whose functional equation fails to factorize into algebraic finite-place data plus the Archimedean factor $\Gamma_{\mathbb{R}}(s) = \pi^{-s/2}\Gamma(s/2)$. Conversely, confirmation of (V1)-(V2) with rational finite-place factors would strengthen, though not prove, the conjecture.

**Open questions.** Does the adelic exponential of [3] admit a global 'period' replacing $2\pi$? Is the residual factor $\approx 3.307$ of Section 4.4 expressible through reciprocity invariants alone? Can measurement be modeled as an Archimedean projection without importing $\mathbb{C}$ as the target?

## 7. Conclusion

We exhibited, with fully displayed arithmetic, that in four canonical settings - the product formula, the Gaussian integral, the $p$-adic local zeta integral, and the completed zeta functional equation - transcendental content ($\pi$, $\sqrt{\pi}$) appears exclusively in Archimedean factors, while every finite-place factor is rational in $p$ and $p^{-s}$ ($Z_2(2) = 4/7$, $P_5 = 1.5625$, $G_p = 1$). This supports the conjecture that $\pi$ is a measure-theoretic artifact of the $\infty$-place: in an adelic formulation, measurement is an Archimedean projection, and $\pi$-dependent terms enter only at that projection. The claim is falsifiable through the failure modes (F1)-(F3), and the verification program (V1)-(V2) is stated with explicit assumptions and uncertainty.

## References

[1] Quasi-adelic measures and equidistribution on $\mathbb{P}^1$. arXiv:1502.04660v3. https://arxiv.org/abs/1502.04660v3
[2] The arithmetic Hodge index theorem for adelic line bundles II. arXiv:1304.3539v2. https://arxiv.org/abs/1304.3539v2
[3] Finite-Dimensional Protori Are Adelic Tori. arXiv:2411.16000v44. https://arxiv.org/abs/2411.16000v44
[4] Spline approximations to conditional Archimedean copula. arXiv:1311.3888v1. https://arxiv.org/abs/1311.3888v1
[5] Non-Archimedean Geometry and Physics on Adelic Spaces. arXiv:math-ph/0306023v1. https://arxiv.org/abs/math-ph/0306023v1
[6] Adelic equidistribution, characterization of equidistribution, and a general equidistribution theorem in non-archimedean dynamics. arXiv:1302.4303v2. https://arxiv.org/abs/1302.4303v2
[7] Fewnomial Systems with Many Roots, and an Adelic Tau Conjecture. arXiv:1011.4128v5. https://arxiv.org/abs/1011.4128v5
[8] Upsampling artifacts in neural audio synthesis. arXiv:2010.14356v2. https://arxiv.org/abs/2010.14356v2
[9] https://papers.qnfo.org/papers/measure-theoretic-artifacts-archimedean-place/. QNFO: Measure-Theoretic Artifacts of the Archimedean Place: A Complete Taxonomy and the Adelic Restructuring of Fundamental Science.
[10] https://papers.qnfo.org/papers/consilience-framework/. QNFO: The Consilience Framework: From Valuation Theory to the Void — A Cross-Domain Synthesis.
[11] https://papers.qnfo.org/papers/measure-theoretic-artifacts-adelic-completion/. QNFO: Measure-Theoretic Artifacts of the Archimedean Place — v2.0: The Completion Problem, the Langlands Connection, and the Adelic Restructuring of Fundamental Physics.
[12] https://papers.qnfo.org/papers/non-anthropocentric-natural-units/. QNFO: Non-Anthropocentric Natural Units: From the Bekenstein Bound to Ostrowski's Theorem.

## Appendix A. Divergence report

One divergence was detected between drafts: the choice of the primary $p$-adic 'Gaussian-type' object. Draft A used the local zeta integral $Z_p(s) = \int_{\mathbb{Z}_p} |x|_p^s\,dx_p$ with the multiplicative character, yielding $Z_p(s) = (1 - p^{-1})/(1 - p^{-(s+1)})$; Draft B used the additive-character integral $G_p = \int_{\mathbb{Z}_p} e^{2\pi i\{x\}_p}\,dx_p$, yielding $G_p = 1$ exactly. Both are correct under the shared normalization $\mathrm{vol}(\mathbb{Z}_p) = 1$; the disagreement is a convention choice, not a mathematical conflict. Resolution: the main text (Section 4.3) reports both normalizations and marks the comparison $G_{\infty} = \sqrt{\pi} \approx 1.7724539$ versus $G_p = 1$ explicitly, with the convention divergence documented here. No other divergences were found: the product-formula examples (Section 4.1), the Gaussian split (Section 4.2), the functional-equation check (Section 4.4), and the reciprocity example (Section 4.5) were convergent across drafts.

## Appendix B. Claim attribution

| Claim | Source drafts | Status |
|---|---|---|
| C1: Product formula exact for $x = 2$ and $x = 12$ | A, B, C | CONVERGENT |
| C2: Gaussian split $I_1^2 = 2\pi \cdot \frac{1}{2} = \pi$, $G_{\infty} = \sqrt{\pi} \approx 1.7724539$ | A, B | CONVERGENT |
| C3: $G_p = 1$ exactly for every prime $p$ | B, C | CONVERGENT |
| C4: $Z_p(s) = (1 - p^{-1})/(1 - p^{-(s+1)})$; $Z_2(2) = 4/7 \approx 0.5714286$ | A, B | CONVERGENT |
| C5: $\Lambda(2) = \Lambda(-1) = \pi/6 \approx 0.5235988$ | A, B, C | CONVERGENT |
| C6: Partial Euler product $P_5 = 900/576 = 1.5625$; residual factor $\approx 3.307$ | A | SINGLE |
| C7: Quadratic reciprocity worked example $(2/7) = 1$, two solutions mod 7 | B, C | CONVERGENT |
| C8: Adelic QM factorization; measurement as Archimedean projection $\pi_{\infty}$ | A, B | CONVERGENT |
| C9: Verification program (V1)-(V2) as labeled projections with stated assumptions | A, C | CONVERGENT |
| C10: Choice of $Z_p(s)$ versus $G_p$ as the primary $p$-adic Gaussian-type object | A vs B | DIVERGENT (resolved: both reported; see Appendix A) |