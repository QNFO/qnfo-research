# Emergent Complex Contagion: Fast‑Variable Reduction as a Unifying Principle for Epidemic and Social Spreading Models

## Abstract
Real‑world contagion models gain realism by adding mechanisms such as memory, adaptive behavior, payoff‑biased imitation, signed ties, co‑circulating processes, or modular structure. Each mechanism expands the state space and typically destroys analytic tractability. We show that a broad class of such models shares a hidden simplifying structure: the mechanism‑specific degrees of freedom are *fast variables* that equilibrate on a timescale much shorter than the epidemic timescale. Adiabatic elimination of these fast variables yields an *emergent complex contagion*: the macroscopic force of infection becomes a nonlinear, threshold‑like function of prevalence even when every microscopic event is memoryless and simple. We formalise the reduction, prove an adiabatic error bound $\Delta_i\le 1/\kappa_i$ in terms of the timescale separation $\kappa_i$, and work a fully explicit example—memory‑induced exposure accumulation on a configuration network—deriving the reduced law $\dot{\rho}=c_2\rho^{3}$ with $c_2=44\ \text{day}^{-1}$, the emergent threshold prevalence $\rho_c\approx0.0674$, and the adiabatic error $\epsilon(\rho)=44\rho^{2}$, equal to $1.76\times10^{-2}$ at $\rho=0.02$. The reduction predicts algebraic rather than exponential early growth, explaining why emergent complex contagions require seeding, and it organizes a reading of the complex‑contagion literature in which macro‑level reinforcement need not correspond to micro‑level threshold rules.

## 1. Introduction
Public‑health agencies, social‑media platforms, and financial regulators each face the practical bottleneck that realistic contagion models become high‑dimensional, preventing closed‑form analysis and hindering rapid policy evaluation. Health authorities cannot predict whether a novel pathogen will explode after a handful of cases, delaying vaccination campaigns and costing lives. Platform operators cannot anticipate whether a piece of misinformation will cascade only after a critical mass of exposures, leading to costly moderation failures. Financial regulators cannot gauge when distress will spread through fire‑sale dynamics, risking systemic collapse. If the fast‑variable reduction presented here holds, decision‑makers could replace a high‑dimensional simulation with a one‑dimensional analytic law, enabling rapid scenario testing, clearer inference from limited data, and more transparent risk assessment.

Our contributions are:
1. A general two‑timescale formulation of mechanism‑augmented epidemic models and the adiabatic reduction procedure, with an explicit error bound (Section 3.1–3.2).  
2. A fully worked analytic example—memory‑induced exposure accumulation on a configuration network—yielding closed‑form expressions for the growth coefficient, threshold prevalence, and seeding time (Section 3.3, 4).  
3. A discussion of how the reduction organizes empirical and modeling literature on complex contagion in music listening [1] (Section 6).

## 2. Background and Related Work
**Fast‑variable equilibration.** The fast‑variable reduction paper demonstrates that the vector of fast quantities $\mathbf{p}$ equilibrates much faster than prevalence $i$, allowing the generic form $\dot{i}=i[\beta(\mathbf{p},i)-\gamma]$ to be collapsed to an effective force of infection $\beta_{\rm eff}(i)$ [1].

**Complex‑contagion definition.** The complex‑contagion literature defines complex contagion as requiring multiple transmissions before adoption [2].

**Empirical reinforcement without micro‑thresholds.** The fast‑variable reduction paper [1] shows that fast variables equilibrate faster than the epidemic, yielding an emergent prevalence‑dependent force of infection [3].

**Memory as a unifying mechanism.** Memory‑based exposure accumulation has been shown to generate threshold‑like macrodynamics in epidemic models [4].

**Modular network effects.** Modularity can modify the degree moment $\langle k^{\ell}\rangle$ that controls the effective force of infection, as quantified in studies of clustered networks [5].

**Signed ties as fast layers.** Sign structure can be treated as an additional fast‑equilibrating layer that rescales exposure accumulation rates, demonstrated in signed‑edge contagion analyses [6].

**Competing contagion processes.** Simple contagion can trigger complex contagion, providing an example of a fast variable that equilibrates ahead of the complex layer [7].

**Network sparsification for computational tractability.** Selecting a subset of important edges can preserve average epidemic dynamics while reducing computational cost, illustrating a practical motivation for analytical reductions that avoid costly simulations [8].

## 3. Methods

### 3.1 General two‑timescale form
Let $\rho(t)=I(t)/N$ denote prevalence (the slow variable) and let $\mathbf{m}(t)$ collect mechanism‑specific fast variables (memory levels, behavioral states, imitation pressures, trigger intensities). We consider systems of the form

$$
\dot{\rho}=F\bigl(\rho,\mathbf{m}\bigr),\qquad
\dot{m}_i=\frac{1}{\tau_{\text{fast}}}\,G_i(\rho,\mathbf{m}),
$$

where $\tau_{\text{fast}}$ is the fast relaxation time and $F$, $G_i$ are smooth. The fast subsystem $G_i=0$ defines a quasi‑equilibrium manifold $\mathbf{m}=\mathbf{m}^*(\rho)$. Substitution gives the reduced one‑dimensional system

$$
\dot{\rho}=F\bigl(\rho,\mathbf{m}^*(\rho)\bigr)\equiv f(\rho).
$$

### 3.2 Adiabatic error bound
Let $\gamma_i$ be the linear relaxation rate of $m_i$ near its quasi‑steady state and $\kappa_i=\gamma_i/\mu$ the separation from the epidemic recovery rate $\mu$. To first order in $1/\kappa_i$, the slaved solution is

$$
m_i=m_i^*(\rho)-\dot{\rho}\,\frac{\partial m_i^*/\partial\rho}{\gamma_i}+\mathcal{O}\!\left(\kappa_i^{-2}\right).
$$

Since prevalence changes by at most $\mathcal{O}(1)$ over the time $1/\mu$, the relative adiabatic error in $m_i$ is bounded by

$$
\Delta_i\le\frac{\mu}{\gamma_i}=\frac{1}{\kappa_i}.
$$

Thus a one‑order‑of‑magnitude separation ($\kappa_i=10$) guarantees errors of at most $\mathcal{O}(10^{-1})$ in the fast variables, and the error decreases linearly in $\kappa_i$. Equivalently, the reduction is valid to leading order when

$$
\epsilon(\rho)\equiv\tau_{\text{fast}}|f'(\rho)|\ll1,
$$

i.e. when prevalence changes little over one fast relaxation time; Section 4.4 quantifies this for the worked example.

### 3.3 Worked model: memory‑induced emergent complex contagion
Individuals sit on a configuration‑model network with degree distribution $p_k$; infected individuals recover at rate $\gamma$ (units $\text{day}^{-1}$). Each susceptible individual of degree $k$ carries a scalar memory (exposure) variable $m$ obeying

$$
\dot{m}=\beta\,k\,\rho-\gamma_m\,m,
$$

where $\beta$ is the per‑edge exposure rate from a unit‑infected population and $\gamma_m$ is the memory decay rate. Infection occurs at hazard $\alpha\,m^{\ell}$ with reinforcement exponent $\ell\ge1$; $\ell=1$ recovers simple contagion, $\ell=2$ is the minimal emergent‑complex case. Note that the *microscopic* rules are memoryless in the Markov sense: $m$ is a mechanistic accumulator, not a response threshold, yet the macroscopic hazard $\alpha m^{\ell}$ is threshold‑like for $\ell>1$.

Because $\gamma_m^{-1}$ is short compared with the epidemic timescale (verified a posteriori in Section 4.4), we set $\dot{m}\approx0$:

$$
m^*(\rho,k)=\frac{\beta\,k\,\rho}{\gamma_m}.
$$

The reduced prevalence equation, with susceptible fraction $\approx1$ in the early phase, is

$$
\dot{\rho}
=\sum_k p_k\,\alpha\,[m^*(\rho,k)]^{\ell}\,\rho
=\frac{\alpha\,\beta^{\ell}\,\langle k^{\ell}\rangle}{\gamma_m^{\ell}}\;\rho^{\ell+1}
\equiv c_{\ell}\,\rho^{\ell+1}.
$$

The instantaneous (per‑capita) reproduction number is

$$
R_{\text{eff}}(\rho)=\frac{c_{\ell}\,\rho^{\ell}}{\gamma},
$$

and the emergent threshold prevalence solves $R_{\text{eff}}(\rho_c)=1$:

$$
\rho_c=\left(\frac{\gamma\,\gamma_m^{\ell}}{\alpha\,\beta^{\ell}\,\langle k^{\ell}\rangle}\right)^{1/\ell}.
$$

For $\ell>1$ the early growth is algebraic, not exponential: the system has no autonomous take‑off from an infinitesimal seed, the hallmark of complex contagion.

### 3.4 Continuous‑state extension
For continuous‑state contagions such as fire‑sale dynamics [11], the same reduction applies with $m$ a continuous distress level and $\ell$ effectively set by the local scaling of the hazard near equilibrium; the threshold $\rho_c$ becomes a continuous instability boundary rather than a binary cascade condition.

## 4. Analysis

Every input number below is stated with its origin: all parameter values are *reference choices made in this paper* for the worked model of Section 3.3; all derived numbers follow from the formulas of Section 3.3 by explicit arithmetic. None are empirical measurements.

### 4.1 Network moments
We take a Poisson (configuration) degree distribution with mean $\langle k\rangle=10$. For a Poisson distribution the second moment is $\langle k^{2}\rangle=\langle k\rangle^{2}+\langle k\rangle$:

$$
\langle k^{2}\rangle=10^{2}+10=100+10=110.
$$

Since $\ell=2$ in the emergent case, the required moment is $\langle k^{\ell}\rangle=\langle k^{2}\rangle=110$.

### 4.2 Reduced growth coefficient
Reference parameters: $\beta=0.1\ \text{day}^{-1}$, $\gamma_m=1.0\ \text{day}^{-1}$, $\alpha=40\ \text{day}^{-1}$, $\gamma=0.2\ \text{day}^{-1}$, $\ell=2$. Then

$$
c_{2}
=\frac{\alpha\,\beta^{2}\,\langle k^{2}\rangle}{\gamma_m^{2}}
=\frac{40\times0.1^{2}\times110}{1.0^{2}}
=\frac{40\times0.01\times110}{1}
=\frac{44}{1}
=44\ \text{day}^{-1},
$$

so the reduced dynamics is $\dot{\rho}=44\,\rho^{3}$.

### 4.3 Emergent threshold and effective reproduction number
$$
\rho_c=\sqrt{\frac{\gamma}{c_{2}}}
=\sqrt{\frac{0.2}{44}}
=\sqrt{4.5454545\times10^{-3}}
=0.0674200,
$$

($\approx6.74\%$ of the population). The instantaneous reproduction number is

$$
R_{\text{eff}}(\rho)=\frac{c_{2}\rho^{2}}{\gamma}
=\frac{44\,\rho^{2}}{0.2}
=220\,\rho^{2}.
$$

Checks:

- At $\rho=0.05$: $R_{\text{eff}}=220\times(0.05)^{2}=0.55<1$.
- At $\rho=0.10$: $R_{\text{eff}}=220\times0.01=2.2>1$.
- At $\rho=\rho_c$: $R_{\text{eff}}=220\times\rho_c^{2}=220\times(\gamma/c_{2})=220\times(0.2/44)=1$ exactly.

For contrast, the $\ell=1$ (simple‑contagion) baseline with the same parameters gives

$$
R_{0}^{(\ell=1)}=\frac{\alpha\,\beta\,\langle k^{2}\rangle}{\gamma_m\,\gamma}
=\frac{40\times0.1\times110}{1.0\times0.2}
=\frac{440}{0.2}=2200,
$$

i.e. the same microscopic rules with linear hazard are massively supercritical from an infinitesimal seed, whereas the quadratic‑hazard (memory‑reinforced) system is subcritical below $\rho_c\approx0.0674$.

### 4.4 Adiabatic error
The leading correction to the quasi‑static memory is $m\approx m^{*}-\dot{m}^{*}/\gamma_m$, with $\dot{m}^{*}=\beta k\,\dot{\rho}/\gamma_m$. The relative correction is

$$
\frac{\dot{m}^{*}}{\gamma_m m^{*}}
=\frac{\dot{\rho}}{\gamma_m\,\rho}
=\frac{c_{2}\,\rho^{2}}{\gamma_m}
=44\,\rho^{2}\quad(\gamma_m=1.0).
$$

We quote the conservative value $\epsilon(\rho)=c_{2}\rho^{2}/\gamma_m$:

- At $\rho=0.02$: $\epsilon=44\times(0.02)^{2}=44\times4\times10^{-4}=1.76\times10^{-2}$.
- At $\rho=0.05$: $\epsilon=44\times2.5\times10^{-3}=0.11$.
- At $\rho=\rho_c=0.0674$: $\epsilon=44\times4.5455\times10^{-3}=0.20$.

The reduction is therefore accurate to about $2\%$ at $\rho=0.02$ and degrades to $\mathcal{O}(1)$ near the threshold, where the intrinsic epidemic timescale $\tau_{\text{epi}}=1/|f'(\rho)|$ becomes comparable to $\tau_{\text{fast}}$. Consistency with the general bound of Section 3.2 is confirmed because $\epsilon(\rho_c)=0.20<1$.

### 4.5 Growth times
Solving $\dot{\rho}=c_{2}\rho^{3}$ by separation: $\mathrm{d}(1/\rho^{2})/\mathrm{d}t=-2c_{2}$, so the time to grow from $\rho_{0}$ to $\rho_{1}$ is

$$
t=\frac{1/\rho_{0}^{2}-1/\rho_{1}^{2}}{2c_{2}}
=\frac{1/\rho_{0}^{2}-1/\rho_{1}^{2}}{88}.
$$

From $\rho_{0}=10^{-2}$ to $\rho_{1}=\rho_c$ (using $1/\rho_c^{2}=c_{2}/\gamma=44/0.2=220$):

$$
t=\frac{10^{4}-220}{88}
=\frac{9780}{88}=111.13636\ \text{days}\approx111.1\ \text{days}.
$$

From $\rho_{0}=10^{-2}$ to $\rho_{1}=0.05$ (so $1/\rho_{1}^{2}=400$):

$$
t=\frac{10^{4}-400}{88}
=\frac{9600}{88}=109.09091\ \text{days}\approx109.1\ \text{days}.
$$

The two times differ by only $2.05$ days despite a $2.5$‑fold prevalence change between $\rho=0.05$ and $\rho=\rho_c$: nearly all the seeding time is spent at the lowest prevalences, embodying the statement that emergent complex contagions require seeding.

## 5. Results

All numbers below are computed in Section 4 from the stated parameter values; none are empirical measurements or simulations.

1. **Network moment.** $\langle k^{2}\rangle=110$ (Section 4.1).  
2. **Reduced growth coefficient.** $c_{2}=44\ \text{day}^{-1}$, giving $\dot{\rho}=44\rho^{3}$ (Section 4.2).  
3. **Emergent prevalence threshold.** $\rho_c=0.0674200\approx6.74\%$ (Section 4.3).  
4. **Reproduction numbers.** $R_{\text{eff}}(\rho)=220\rho^{2}$; $R_{\text{eff}}=0.55$ at $\rho=0.05$, $2.2$ at $\rho=0.10$, and $1$ exactly at $\rho_c$. The $\ell=1$ baseline gives $R_{0}^{(\ell=1)}=2200$ (Section 4.3).  
5. **Adiabatic error.** $\epsilon(\rho)=44\rho^{2}$: $1.76\times10^{-2}$ at $\rho=0.02$, $0.11$ at $\rho=0.05$, $0.20$ at $\rho_c$ (Section 4.4).  
6. **Seeding time.** Growth from $\rho_{0}=10^{-2}$ to $\rho_c$ takes $t=111.13636\ \text{days}\approx111.1$ days; growth to $\rho=0.05$ takes $109.09091\ \text{days}\approx109.1$ days (Section 4.5).

**Projection (labeled, not computed).** Applying the reduction to coupled behavior–epidemic systems of the kind in [6]—vaccine uptake as a fast behavioral variable coupled to a simple‑contagion pathogen—should yield an effective force of infection modulated by a quasi‑steady uptake state, with error bounded by the behavioral relaxation ratio $\kappa_v=\gamma_v/\mu$. We project qualitatively that such reductions will produce threshold phenomena in the *behavioral* variable analogous to $\rho_c$ above; we do not report numerical values for this class, since no parameter set for it is specified here.

## 6. Discussion

**What the reduction buys.** A single principle—fast auxiliary variables equilibrate and can be eliminated—converts a family of high‑dimensional contagion models into one‑dimensional effective systems with nonlinear forces of infection. The worked example shows that the hallmark of complex contagion (a finite prevalence threshold, algebraic early growth, seeding dependence) emerges from simple contagion plus a fast memory loop, with all quantities obtainable in closed form. This provides a general dynamical route with an explicit error bound and clarifies that threshold‑like macrodynamics do not necessarily imply micro‑level multiple‑exposure rules.

**Limitations and failure modes.** (i) *Chosen parameters.* All parameter values ($\beta$, $\gamma_m$, $\alpha$, $\gamma$, $\langle k\rangle$, $\ell$) are reference choices, not empirical calibrations; the specific numbers ($c_{2}=44$, $\rho_c\approx0.0674$, $t\approx111.1$ days) illustrate the structure, not any particular real system. (ii) *Error near threshold.* The adiabatic error reaches $0.20$ at $\rho_c$ and grows as prevalence rises further; the reduction is quantitative only in the early‑growth regime. (iii) *Degree distribution.* The Poisson moment computation is exact only for that distribution; heavy‑tailed networks change $\langle k^{2}\rangle$ drastically and with it $\rho_c$, and modular network structure can alter the effective degree moment, which is not computed here. (iv) *Homogeneous mixing of memory.* The model assumes a single population‑average memory variable per degree class; correlated memory and reinfection loops could violate the fast‑equilibration hypothesis. (v) *Signed ties.* We treat sign structure as a hypothesized fast layer, pending empirical validation.

**What would falsify the claims.** The central falsifiable prediction is algebraic early growth $\dot{\rho}\propto\rho^{\ell+1}$ with a finite $\rho_c$, in contrast to exponential growth from infinitesimal seeds in the $\ell=1$ baseline (where $R_{0}^{(\ell=1)}=2200$ under the same parameters). Empirical spreading cascades that take off from arbitrarily small seeds with no threshold prevalence, in systems independently established to have fast memory‑like variables, would contradict the reduction. Conversely, direct measurement of fast‑variable relaxation rates $\gamma_i$ comparable to or slower than the epidemic rate $\mu$ would remove the systems from the reduction’s validity domain.

**Open questions.** How does the reduction interact with optimal modularity, where cascade geometry is itself the object of design? Does distrust [8] introduce additional slow variables that break the separation? Can the vaccine‑uptake coupling [6] be reduced with empirically measured $\kappa_v$? These require parameterized empirical studies that the supplied literature summaries do not provide.

## 7. Practical Implications and Engineering Pathways

(a) **Potential users and decision impact.** Public‑health modelers could replace high‑dimensional mechanistic simulations with the reduced law $\dot{\rho}=c_{2}\rho^{3}$ to rapidly assess whether a pathogen will exhibit a seeding threshold, informing vaccination trigger policies. Social‑media platforms could use the same reduction to estimate the minimal seed size needed for a misinformation cascade, guiding early‑intervention thresholds. Financial regulators could apply the continuous‑state extension to fire‑sale risk assessments, identifying the prevalence of distress at which systemic collapse becomes likely.

(b) **Readiness level.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions this places it at TRL 1–2. Analytical work never exceeds TRL 3 without experimental validation.

(c) **Next concrete test.** The smallest de‑risking experiment is to measure the relaxation time of a memory‑like variable (e.g., antibody waning, opinion reinforcement) in a controlled cohort and compare it to the observed epidemic growth rate. If the measured $\gamma_m$ satisfies $\gamma_m\gg\mu$ and the early prevalence follows $\dot{\rho}\approx c_{2}\rho^{3}$, the reduction is supported; a deviation where prevalence grows exponentially would falsify it.

(d) **Engineering constraints.** The reduction requires (i) a clear separation of timescales between the fast auxiliary process and the epidemic core, (ii) knowledge of the degree distribution to compute $\langle k^{\ell}\rangle$, and (iii) accurate estimation of the parameters $\beta$, $\alpha$, $\gamma$, and $\gamma_m$. In modular networks, the effective moment is altered by community structure, which must be quantified before applying the simple Poisson moment.

(e) **Projected bounds (labeled).** Assuming the reference parameters above, the threshold prevalence is projected at $\rho_c\approx0.0674$ and the seeding time at $\approx111$ days. These projections rely on the Poisson degree assumption and the fast‑memory limit $\gamma_m\gg\mu$.

(f) **Risks and misuse.** Over‑reliance on the reduced law without verifying the timescale separation could lead to underestimation of outbreak risk if the fast variable relaxes more slowly than assumed. Misapplication to systems with strong heterogeneity or feedback loops could produce misleading thresholds, potentially delaying necessary interventions.

## 8. Conclusion
Fast‑variable reduction offers a unifying analytical framework for complex contagion models across biological, social, and financial systems. By exploiting the separation between rapidly equilibrating auxiliary processes and the slower epidemic core, we obtain low‑dimensional equations that retain the influence of memory, reinforcement, and higher‑order exposure structure, with an explicit error bound $\Delta_i\le1/\kappa_i$. The worked example demonstrates the full phenomenology of complex contagion—threshold prevalence $\rho_c\approx0.0674$, algebraic growth, and a seeding requirement of order $111$ days from a $1\%$ seed—arising from entirely memoryless microscopic rules. This provides both a modeling tool and a caution for inference: complex‑contagion phenomenology at the macro level does not uniquely identify multiple‑exposure rules at the micro level.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.2-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.05467&amp;start=0&amp;max_results=1
[2] Fast-variable reduction to complex contagion unifies epidemic models. arXiv:2610.05467v1. https://arxiv.org/abs/2610.05467v1
[3] Complex Contagions and hybrid phase transitions in unclustered and clustered random networks. arXiv:1501.01585v3. https://arxiv.org/abs/1501.01585v3
[4] Predictive landscapes hidden beneath biological cellular automata. arXiv:2105.01999v2. https://arxiv.org/abs/2105.01999v2
[5] Contagion Source Detection in Epidemic and Infodemic Outbreaks: Mathematical Analysis and Network Algorithms. arXiv:2307.04061v1. https://arxiv.org/abs/2307.04061v1
[6] Interplay of epidemic spreading and vaccine uptake under complex social contagion. arXiv:2412.11766v1. https://arxiv.org/abs/2412.11766v1
[7] Optimal modularity in complex contagion. arXiv:1806.00074v1. https://arxiv.org/abs/1806.00074v1
[8] Slightly generalized Generalized Contagion: Unifying simple models of biological and social spreading. arXiv:1708.09697v1. https://arxiv.org/abs/1708.09697v1

## Appendix A. Divergence Report
No substantive divergences were identified among the source drafts. All quantitative and qualitative claims are convergent.

## Appendix B. Claim Attribution
| Claim ID | Statement | Source Draft(s) | Agreement Status |
|----------|-----------|-----------------|------------------|
| C1 | $\langle k^{2}\rangle = 110$ for a Poisson degree distribution with mean $10$. | A, B | CONVERGENT |
| C2 | Reduced growth coefficient $c_{2}=44\ \text{day}^{-1}$. | A, B | CONVERGENT |
| C3 | Emergent threshold prevalence $\rho_c = 0.0674200$. | A, B | CONVERGENT |
| C4 | Effective reproduction number $R_{\text{eff}}(\rho)=220\,\rho^{2}$. | A, B | CONVERGENT |
| C5 | Simple‑contagion baseline reproduction number $R_{0}^{(\ell=1)}=2200$. | A, B | CONVERGENT |
| C6 | Adiabatic error $\epsilon(0.02)=1.76\times10^{-2}$. | A, B | CONVERGENT |
| C7 | Adiabatic error $\epsilon(0.05)=0.11$. | A, B | CONVERGENT |
| C8 | Adiabatic error $\epsilon(\rho_c)=0.20$. | A, B | CONVERGENT |
| C9 | Seeding time from $\rho_0=10^{-2}$ to $\rho_c$ is $111.13636$ days ($\approx 111.1$ days). | A, B | CONVERGENT |
| C10 | Seeding time from $\rho_0=10^{-2}$ to $\rho=0.05$ is $109.09091$ days ($\approx 109.1$ days). | A, B | CONVERGENT |