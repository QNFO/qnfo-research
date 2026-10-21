# The Adele Analogy for Epistemic Boundaries: Local Models, a Restricted Product of Representations, and a Quantified Validity Radius

## Abstract

Scientific and engineering practice routinely deploys models outside the domains in which they were validated, leading to costly failures that are discovered only after deployment. Existing treatments of epistemic uncertainty flag that a prediction is uncertain but do not specify where a validated model stops being valid or which of its contents survive a change of representation. This paper formalizes an adele‑like framework in which each validated model is a “local completion” of an underlying phenomenon, carries an explicit validity boundary, and the robust core of a model class is exactly the set of quantities invariant under admissible changes of representation. Models are defined as local charts with validation domains, combined in a restricted product over representations, and the framework is tested on the Poisson‑to‑Gaussian max‑entropy bridge. With full arithmetic we show that at λ = 100 the Gaussian local model reproduces Poisson probabilities to within 3.3 % in log‑space at one standard deviation but underestimates the right‑tail by a factor of 1.30 at three standard deviations. The 5 % log‑tolerance validity radius lies between 2σ and 2.5σ, and linear‑interpolation and cubic‑law projections give a radius of approximately 2.1σ. The leading non‑invariant quantity is the standardized skewness 1/$\sqrt{λ}$ = 0.1. The result turns “we do not know” into a measured radius, applicable to out‑of‑distribution risk assessment in clinical‑ML, safety‑critical cyber‑physical systems, belief‑aggregation architectures, and language‑model policy pipelines.

## 1. Introduction

  The cost of not drawing a model’s validity boundary is twofold. First, a team must either apply costly manual review everywhere or accept unquantified risk. Second, autonomous reasoning systems that aggregate scientific claims need to know when a well‑supported local consensus stops supporting a global conclusion, a need already recognized. If the framework proposed here holds, every model would carry a machine‑readable validity boundary expressed as a radius in a deviation coordinate, calibrated by explicit arithmetic (Section 4). Incompatibilities between well‑validated models would be classified as structured edges of ignorance rather than defects, and the robust content of a model class would be identified by an invariance test: what survives a change of representation is what one may safely extrapolate.

**Contributions.**  
- Formal definitions: models as local charts with explicit validation domains, a compatibility relation, and an adele‑like restricted product over representations (Section 3).  
- Invariance criterion: the invariant core of a model class is the set of quantities unchanged under admissible representation changes, with the first non‑invariant term computable as a cumulant ratio (Section 4).  
- Quantified validity radius for the Poisson‑to‑Gaussian max‑entropy bridge: log‑probability discrepancies of 0.0325 nats at 1σ, 0.0296 nats at 2σ, 0.1197 nats at 2.5σ, and a factor 1.30 underestimate at 3σ; the 5 % log‑tolerance radius is bracketed by 2σ < R < 2.5σ and projected to $\approx$ 2.1σ (Sections 4–5).  
- Mapping of the framework onto existing epistemic‑uncertainty practice, technology‑readiness assessment, and the smallest falsifying experiment (Sections 6–7).

## 2. Background and Related Work

 

 This provides an empirical analogue of the boundary concept that the present framework formalises.

 This directly motivates the need for a quantified validity radius.

 This illustrates why a formal boundary, rather than a naïve data‑quantity heuristic, is essential.

 This supports the adele‑like restricted product idea, where each local chart contributes coherent evidence.

The combinatorial one‑cocycle work constructs a 1‑cocycle in a moduli space of knots, providing a concrete example of an invariant structure that survives representation changes [2]. This motivates the invariant‑core notion.

The work classifies unitary elements of C*‑algebras [3]. This parallels the identification of invariant quantities across model representations.

Improving problem solving by exploiting symmetry demonstrates that changing the representation of a problem (via symmetry transformations) can preserve solution structure while exposing non‑invariant aspects [6]. This illustrates the relevance of representation change to epistemic boundaries.

The Annotation Scarcity Paradox surveys how evaluation bottlenecks limit epistemic confidence in low‑resource NLP, highlighting a structural limitation on what can be known [9]. This underscores the practical importance of formally delineating knowledge boundaries.

The topological description of Legendrian contact homology is presented in [10]. This exemplifies the invariant‑core principle.

Exact reduction under a stated constraint shows that a stationary scalar correlation energy admits an exact one‑mode terminal representation only under a stationarity constraint [11]. The constraint is the validity boundary of the reduced representation, mirroring the Poisson‑to‑Gaussian bridge.

The prior version of this framework defined local charts, the restricted product, and the invariant core, and reported the Poisson‑to‑Gaussian arithmetic summarized in its Results [12]. The present paper carries that arithmetic forward in full, strengthens the connection between the invariant core and the boundary failure, and maps the framework onto current practice.

Self‑declared validity domains propose an epistemology that explicitly separates ontological territory from epistemic maps and declares its own domain of validity [13]. The present work differs by making the boundary quantitative rather than declarative.

The validation metric problem identifies the lack of objective validation mechanisms for non‑empirical contributions [14]. The present framework contributes a computable validity radius, addressing that gap.

## 3. Methods

### 3.1 Local charts and validation domains

Fix a phenomenon Φ and a space X of observable outcomes. A local model is a pair  

$$M = (f_M, D_M),$$  

where $f_M : X \to Y_M$ is a predictive map into an output space $Y_M$ and $D_M \subseteq X$ is the validation domain: the set of inputs on which $f_M$ has been checked against Φ under a stated protocol and tolerance. The pair $(f_M, D_M)$ is the epistemic analogue of a chart in a manifold atlas: $f_M$ is the coordinate map and $D_M$ is the chart’s open set. A model is validated on $D_M$ and silent on $X \setminus D_M$.

The validation protocol is part of the model. Two models with the same $f_M$ but different $D_M$ are different epistemic objects because the boundary is the object of study. This bookkeeping requirement is not decorative: [5] shows that more data can degrade scientific conclusions, so only an externally stated domain can carry the information that internal behavior does not.

### 3.2 Compatibility and the restricted product

Let $\mathcal{R}$ be a set of representations (radix, metric, observer frame, discretization, etc.). For each $r \in \mathcal{R}$ there is a family of local models $\{M_{r,i}\}_i$ validated in that representation.

Two local models $M$ and $M'$ are compatible on an overlap $U \subseteq D_M \cap D_{M'}$ if their predictions agree within a tolerance $\epsilon$:  

$$\sup_{x \in U} d_Y\bigl(f_M(x), f_{M'}(x)\bigr) \le \epsilon.$$

The adele‑like object is the restricted product  

$$\mathbb{M}_{\mathcal{R}} = \prod_{r \in \mathcal{R}}{}' \mathcal{M}_r,$$  

the set of tuples $(M_r)_{r \in \mathcal{R}}$ with $M_r$ a validated local model in representation $r$, such that $M_r$ is trivial (identical to a fixed reference model of that representation) for all but finitely many $r$. The restriction makes the product manageable, exactly as the restricted product over primes makes the adele ring locally compact.

A global statement about Φ is admissible if it is a property $P$ such that every compatible tuple in $\mathbb{M}_{\mathcal{R}}$ satisfies $P$ on the intersection of its validation domains. An incompatibility between two well‑validated models with overlapping domains is then a pair of charts that cannot be embedded in one compatible tuple. Under the central conjecture, such incompatibilities mark structured edges of ignorance: places where the missing global object would be required to reconcile the local truths, and therefore places where extrapolation is expected to fail.

### 3.3 The invariant core

Define an admissible change of representation as a map $g$ between representations that preserves the validation protocol. The invariant core of a model class $\mathcal{C}$ is  

$$\operatorname{Inv}(\mathcal{C}) = \bigcap_{g} \bigl\{ q \text{ of } \mathcal{C} : q(gM) = q(M) \text{ for all } M \in \mathcal{C} \bigr\}.$$

The framework’s second claim is that the robust known is exactly $\operatorname{Inv}(\mathcal{C})$: quantities invariant under representation change are those one may safely extrapolate beyond $D_M$, while the leading non‑invariant quantity measures the distance to the boundary. In homology theory the canonical isomorphism between singular and de Rham homology [10] states that the invariant core survives a change of chain representation exactly. In operator algebras the Cuntz semigroup classifies unitary elements of unital AF‑algebras completely [3]; the first step outside that domain the invariant demonstrably fails to determine the object. In reduced quantum descriptions the one‑mode representation of a stationary correlation energy is exact only under a stationarity constraint [11]; the constraint is the validity boundary. Section 4 computes both the invariant core and the leading non‑invariant quantity for the worked example.

### 3.4 Worked example: the Poisson‑to‑Gaussian max‑entropy bridge

The test case is the passage from a Poisson counting model to a Gaussian continuous model. Among distributions on $\mathbb{R}$ with fixed mean $\mu$ and variance $\sigma^2$, the Gaussian maximises differential entropy; among distributions on $\{0,1,2,\dots\}$ with fixed mean $\lambda$, the Poisson is the corresponding max‑entropy object. Setting $\mu = \sigma^2 = \lambda$ yields the Gaussian as the max‑entropy continuous representation of the Poisson counting model. The question is: over what region of outcome space does the Gaussian chart remain a valid representation of the Poisson chart, and what is the first quantity that fails to be invariant?

Throughout Section 4 the Poisson parameter is $\lambda = 100$, chosen so that all quantities are computable by hand with Stirling’s approximation  

$$\ln n! \approx n \ln n - n + \tfrac12 \ln(2\pi n) + \tfrac{1}{12n},$$  

whose relative error is $O\!\bigl(1/(360 n^3)\bigr)$, negligible at the digit level used here.

## 4. Analysis

Every input number in this section is either a definition (the Poisson parameter $\lambda = 100$, the tolerance levels), a standard mathematical constant, or computed below from the stated formulas. No empirical data are used.

### 4.1 Input constants

The following constants are used, each to at least seven significant figures:

$$\ln 100 = 4.605170,\quad \ln 110 = 4.700480,\quad \ln 120 = 4.787492,$$
$$\ln 125 = 4.828314,\quad \ln 130 = 4.867534,$$
$$\ln(2\pi) = 1.837877,\quad \ln e = 1.$$

Derived per‑case constant:  

$$0.5\ln(2\pi\lambda) = 0.5\bigl(\ln(2\pi) + \ln\lambda\bigr) = 0.5(1.837877 + 4.605170) = 3.221524.$$

### 4.2 Log‑probability of the Poisson model at four deviations

The Poisson probability mass is  

$$P(X = k) = e^{-\lambda}\lambda^k / k!,$$  

so  

$$\ln P(X = k) = -\lambda + k\ln\lambda - \ln k!.$$

The Gaussian density approximation at $k$ with $\mu = \sigma^2 = \lambda$ gives  

$$\ln p_{\mathrm{G}}(k) = -\tfrac12\ln(2\pi\lambda) - \frac{(k-\lambda)^2}{2\lambda}.$$

#### Case $k = 110$ ($x = 1$)

Stirling for $\ln 110!$:

- $110\ln110 = 110 \times 4.700480 = 517.0528$  
- $-110$ gives $407.0528$  
- $\tfrac12\ln(2\pi\cdot110) = \tfrac12(1.837877 + 4.700480) = 3.269179$  
- $\tfrac{1}{12\cdot110}=0.000758$

$$\ln 110! = 517.0528 - 110 + 3.269179 + 0.000758 = 410.3227.$$

Then  

$$\ln P_{\mathrm{Pois}}(110) = -100 + 110\times4.605170 - 410.3227 = -3.7540.$$

Gaussian:  

$$\ln p_{\mathrm{G}}(110) = -3.221524 - \frac{10^2}{200} = -3.721524.$$

Log‑difference  

$$\Delta_{1\sigma} = -3.7540 - (-3.721524) = -0.0325.$$

The Gaussian overestimates the Poisson log‑probability by 0.0325 nats, a relative error of $e^{0.0325}-1 = 0.0330$ (3.3 %).

#### Case $k = 120$ ($x = 2$)

- $120\ln120 = 120 \times 4.787492 = 574.4990$  
- $-120$ gives $454.4990$  
- $\tfrac12\ln(2\pi\cdot120) = \tfrac12(1.837877 + 4.787492) = 3.312685$  
- $1/(12\cdot120)=0.000694$

$$\ln 120! = 574.4990 - 120 + 3.312685 + 0.000694 = 457.8124.$$

$$\ln P_{\mathrm{Pois}}(120) = -100 + 120\times4.605170 - 457.8124 = -5.1920.$$

$$\ln p_{\mathrm{G}}(120) = -3.221524 - \frac{20^2}{200} = -5.221524.$$

$$\Delta_{2\sigma} = -5.1920 - (-5.221524) = +0.0296.$$

The Gaussian underestimates the Poisson log‑probability by 0.0296 nats ($\approx 3.0$ % relative error).

#### Case $k = 125$ ($x = 2.5$)

- $125\ln125 = 125 \times 4.828314 = 603.5393$  
- $-125$ gives $478.5393$  
- $\tfrac12\ln(2\pi\cdot125) = \tfrac12(1.837877 + 4.828314) = 3.333096$  
- $1/(12\cdot125)=0.000667$

$$\ln 125! = 603.5393 - 125 + 3.333096 + 0.000667 = 481.8731.$$

$$\ln P_{\mathrm{Pois}}(125) = -100 + 125\times4.605170 - 481.8731 = -6.2268.$$

$$\ln p_{\mathrm{G}}(125) = -3.221524 - \frac{25^2}{200} = -6.346524.$$

$$\Delta_{2.5\sigma} = -6.2268 - (-6.346524) = +0.1197.$$

Relative error $e^{0.1197}-1 = 0.127$ (12.7 %).

#### Case $k = 130$ ($x = 3$)

- $130\ln130 = 130 \times 4.867534 = 632.7794$  
- $-130$ gives $502.7794$  
- $\tfrac12\ln(2\pi\cdot130) = \tfrac12(1.837877 + 4.867534) = 3.352706$  
- $1/(12\cdot130)=0.000641$

$$\ln 130! = 632.7794 - 130 + 3.352706 + 0.000641 = 506.1328.$$

$$\ln P_{\mathrm{Pois}}(130) = -100 + 130\times4.605170 - 506.1328 = -7.4607.$$

$$\ln p_{\mathrm{G}}(130) = -3.221524 - \frac{30^2}{200} = -7.721524.$$

$$\Delta_{3\sigma} = -7.4607 - (-7.721524) = +0.2608.$$

Probability ratio $e^{0.2608}=1.298$, i.e. a factor 1.30 underestimate.

### 4.3 Leading‑order asymptotics and the residual pattern

Substituting $k = \lambda + x\sqrt{\lambda}$ into the Stirling‑based log‑probability and expanding yields  

$$\ln P_{\mathrm{Pois}}(k) = -\frac{x^2}{2} - \tfrac12\ln(2\pi\lambda) + \frac{x^3 - 3x}{6\sqrt{\lambda}} + O(\lambda^{-1}).$$  

The first two terms equal the Gaussian log‑density $\ln p_{\mathrm{G}}(k)$. Hence the leading discrepancy is  

$$\Delta(x) \approx \frac{x^3 - 3x}{6\sqrt{\lambda}} = \frac{x^3 - 3x}{60} \quad (\lambda=100).$$

Evaluating this cubic law at the four computed $x$ values gives the table below (all numbers in nats):

| $x$ | cubic prediction $(x^3-3x)/60$ | computed $\Delta$ | residual |
|---|---|---|---|
| $1$ | $-0.0333$ | $-0.0325$ | $0.0008$ |
| $2$ | $+0.0333$ | $+0.0296$ | $0.0037$ |
| $2.5$ | $+0.1354$ | $+0.1197$ | $0.0157$ |
| $3$ | $+0.3000$ | $+0.2608$ | $0.0392$ |

Residuals grow with $x$ because omitted $O(\lambda^{-1})$ terms are of order $x^4/\lambda$ and $x^6/\lambda^2$.

### 4.4 The invariant core: cumulants under the representation change

For the Poisson distribution with parameter $\lambda$, the cumulant generating function is $\ln E[e^{tX}] = \lambda(e^t - 1)$, so every cumulant equals $\lambda = 100$:

$$\kappa_1 = \kappa_2 = \kappa_3 = \kappa_4 = \dots = 100.$$

For the Gaussian $\mathcal{N}(\lambda,\lambda)$, the cumulant generating function is $\ln E[e^{tY}] = \lambda t + \lambda t^2/2$, giving  

$$\kappa_1 = 100,\quad \kappa_2 = 100,\quad \kappa_n = 0 \text{ for } n\ge 3.$$

Thus the representation‑invariant quantities are the mean and variance (both 100). The first non‑invariant quantity is the third cumulant, i.e. the skewness  

$$\gamma_1 = \frac{\kappa_3}{\kappa_2^{3/2}} = \frac{1}{\sqrt{\lambda}} = 0.1,$$

which is zero for the Gaussian. The excess kurtosis $1/\lambda = 0.01$ is the next excluded quantity. The coefficient $\gamma_1/6$ appears in the cubic discrepancy law, confirming that the leading non‑invariant cumulant predicts the shape and scale of the out‑of‑domain error.

### 4.5 The validity radius

Fix a log‑tolerance $\epsilon = 0.05$. The Gaussian chart is declared valid at deviation $x$ if $|\Delta(x)| \le \epsilon$. From the computed points:

- $|\Delta(1)| = 0.0325 \le 0.05$ (valid)  
- $|\Delta(2)| = 0.0296 \le 0.05$ (valid)  
- $|\Delta(2.5)| = 0.1197 > 0.05$ (invalid)

Hence the 5 % log‑tolerance radius lies strictly between $2\sigma$ and $2.5\sigma$. Two labeled projections refine the estimate.

**Projection 1 (linear interpolation).**  

$$x_{\epsilon} = 2 + 0.5 \times \frac{0.05 - 0.0296}{0.1197 - 0.0296}
= 2 + 0.5 \times \frac{0.0204}{0.0901}
= 2.113.$$

**Projection 2 (cubic law).** Solve $(x^3 - 3x)/60 = 0.05$, i.e. $x^3 - 3x - 3 = 0$. Linear interpolation between $x=2.10$ (value $-0.039$) and $x=2.11$ (value $+0.064$) yields  

$$x \approx 2.10 + 0.01 \times \frac{0.039}{0.103} = 2.104.$$

Both projections give $R \approx 2.1\sigma$, with the exact bracket $2\sigma < R_{0.05} < 2.5\sigma$ remaining rigorous.  

The cubic law predicts a scaling $R \propto \lambda^{1/6}$ for large $\lambda$; for $\lambda=100$ this gives $R\approx 1.44\sigma$, underestimating the true root because the $-3x$ term is non‑negligible. The asymptotic scaling also implies that a hundredfold increase in $\lambda$ widens the radius by a factor $100^{1/6}=2.154$.

## 5. Results

All numbers below are those computed with shown arithmetic in Section 4; the two interpolated radii are labeled projections with their assumptions stated in Section 4.5.

**R1. Log‑probability discrepancies ($\lambda=100$).**  
- $1\sigma$: $\Delta = -0.0325$ nats (Gaussian overestimates by factor $e^{0.0325}=1.033$).  
- $2\sigma$: $\Delta = +0.0296$ nats (Gaussian underestimates by factor $e^{0.0296}=1.030$).  
- $2.5\sigma$: $\Delta = +0.1197$ nats (relative error $12.7\%$).  
- $3\sigma$: $\Delta = +0.2608$ nats (factor 1.30 underestimate).

**R2. Deterministic cubic law.** The discrepancies follow $\Delta(x) \approx (x^3-3x)/(6\sqrt{\lambda})$ with residuals $0.0008$, $0.0037$, $0.0157$, $0.0392$ at $x=1,2,2.5,3$, consistent with the $O(\lambda^{-1})$ remainder.

**R3. Invariant core and first excluded quantity.** The invariant core consists of mean $\kappa_1=100$ and variance $\kappa_2=100$. The first non‑invariant quantity is the skewness $\gamma_1=0.1$, whose coefficient $\gamma_1/6$ appears in the cubic discrepancy law.

**R4. Validity radius.** The $5\%$ log‑tolerance radius is bracketed by $2\sigma < R_{0.05} < 2.5\sigma$. Linear interpolation gives $R_{0.05}=2.113\sigma$, the cubic law gives $R_{0.05}=2.104\sigma$, and both agree on $R \approx 2.1\sigma$. The scaling prediction $R \propto \lambda^{1/6}$ implies a hundredfold increase in $\lambda$ widens the radius by a factor $2.154$.

**R5. Shape of the failure.** The Gaussian chart underestimates right‑tail Poisson probabilities beyond $x\approx\sqrt{3}=1.732$, and the underestimate grows cubically, reaching a 30 % tail error at $3\sigma$.

## 6. Discussion

The worked example supports the framework's two operational claims in a limited and precisely circumscribed way. The invariant‑core claim survived its first test in the strong sense that the excluded quantity (skewness $0.1$) is not merely correlated with the boundary failure but is its leading coefficient: the cumulant computation done entirely inside the validation domain predicted the functional form of the out‑of‑domain error. The validity‑radius claim survived in the weaker sense that the radius was bracketed rather than computed exactly, and the fine value rests on interpolation.

**Limitations.** The result rests on the following assumptions, each with its sensitivity:

- **Stirling truncation.** All Poisson log‑probabilities use the Stirling series through the $1/(12n)$ term, whose next term is of order $1/(360 n^{3})$; at $n=110$ this is $1/(360\times1\,331\,000)\approx2.1\times10^{-9}$ nats, so it cannot move any reported digit. Sensitivity: negligible.  
- **Input log constants.** The logarithms in Section 4.1 are given to six decimal places; an error of $5\times10^{-7}$ in $\ln110$, multiplied by $110$ in $110\ln110$, contributes up to $6\times10^{-5}$ nats, an order of magnitude below the smallest reported discrepancy ($0.0008$ residual at $x=1$ is itself near this floor). Sensitivity: the $x=1$ residual is at the precision floor; the $x=2.5$ and $x=3$ residuals are far above it.  
- **Single parameter value.** All computations use $\lambda=100$. The cubic law and the $\lambda^{1/6}$ radius scaling are derived asymptotically but tested at only one point. Sensitivity: high; the framework's general claims stand or fall on whether the pattern repeats at other $\lambda$, which is the proposed next experiment (the relevant section).  
- **Interpolated radius.** The fine value $R_{0.05}\approx2.1\sigma$ is a projection from two interpolation schemes, not a computed point; the derived, interpolation‑free statement is only the bracket $2\sigma<R_{0.05}<2.5\sigma$. Sensitivity: moderate; the bracket is exact given the four computed points, the fine value could shift by a few hundredths of $\sigma$.  
- **Tolerance choice.** The radius depends on the chosen $\epsilon=0.05$; a different tolerance moves the radius along the cubic and changes it by construction, not by error. Sensitivity: definitional.  
- **Single worked example.** The identification of the first non‑invariant cumulant with the leading error coefficient is demonstrated for one representation change (Poisson → Gaussian). The framework's second claim asserts this is general; that generality is a conjecture supported by one instance, not a theorem. Sensitivity: this is the largest gap between what is derived and what is claimed.

**What would falsify the main result.** The main quantitative result is that the log‑probability discrepancy of the max‑entropy bridge is a deterministic cubic $\Delta(x)\approx(x^{3}-3x)/(6\sqrt{\lambda})$ whose coefficient is the excluded skewness $\gamma_{1}/6$, and that this yields a computable validity radius. Three observations would falsify it. First, evaluating $\Delta$ at a new point, for example $x=2.25$ ($k=122$ or $123$), and obtaining a value inconsistent with the cubic prediction $(11.39-6.75)/60=0.0773$ beyond the residual trend established at the four computed points would break the law. Second, computing the exact Poisson log‑probabilities with full‑precision arithmetic and finding discrepancies inconsistent with the hand values by more than the stated precision floor ($10^{-4}$ nats) would invalidate the derivations. Third, repeating the computation at a different $\lambda$, for example $\lambda=400$ where the cubic predicts $\Delta(3)=(27-9)/120=0.15$, and finding a discrepancy that does not scale as $1/\sqrt{\lambda}$ would falsify the claimed scaling and with it the identification of the skewness as the governing quantity. Each falsification test requires only arithmetic on a known distribution; none requires new data.

**Open questions.** Whether the restricted‑product structure of Section 3.2 supports a locality theorem analogous to local compactness, in a sense meaningful for model classes, is open. Whether incompatibilities between well‑validated models always mark recoverable global objects, rather than genuine inconsistency, is open and not addressed in the works cited here. Whether the invariant‑core criterion extends beyond cumulant‑based probes to models without a natural exponential‑family structure is open.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The immediate users are builders of model‑governance and uncertainty tooling, and clinical‑ML deployment teams, for whom [7] argues that local validity specifications are useful for safety‑critical systems. If the framework holds, the decision that changes is the review policy: instead of a binary “in distribution / out of distribution” flag, the deployed artifact carries a measured radius $R_\epsilon$ in a stated deviation coordinate, and manual review is triggered only when the operating point approaches $R_\epsilon$. A second user class is aggregation architectures for autonomous scientific reasoning: The framework proposes that belief could be operationalised as a dynamic, probabilistically coherent function over structured scientific claims, and a validity radius is exactly the kind of structured metadata such a function could consume, weighting a claim by the distance of the query from the validating chart. A third class is language‑model policy design: [6] discusses how exploiting symmetry can change problem representations while preserving solution structure, and the framework supplies a formal trigger condition for policy actions. For users that cannot yet be named, the work is foundational: the restricted‑product formalism and the invariant‑core criterion are definitions and one worked example, not yet a deployable estimator.

**(b) Current readiness.** Against the NASA Technology Readiness Level definitions, this work is analytical: the framework is defined, one quantitative example is computed by hand, and nothing has been peer reviewed or validated outside the worked example. This places it at TRL 1–2 (basic principles observed and formulated; concept and application stated without proof of feasibility beyond the toy case). Analytical work does not exceed TRL 3, and no claim of implementation, manufacturing, or deployment readiness is made.

**(c) The smallest next experiment.** The smallest falsifying calculation is a full‑precision evaluation of the Poisson and Gaussian log‑probabilities at $\lambda = 100$ and one new deviation, $x = 2.25$, plus one new parameter value, $\lambda = 400$ at $x = 3$. What is measured: the log‑probability discrepancy $\Delta$ at those points, compared against the cubic predictions $0.0773$ (at $\lambda = 100$, $x = 2.25$) and $0.15$ (at $\lambda = 400$, $x = 3$). The outcome that refutes the main result is a discrepancy inconsistent with the cubic law beyond the residual trend of Section 4.3, or a $\lambda$‑scaling that is not $1/\sqrt{\lambda}$. This requires only a scripting‑language one‑liner per point and no data collection.

**(d) Binding constraints.** For the framework itself, the first binding constraint is generality: the invariant‑core criterion is demonstrated only for exponential‑family cumulants, and extending it to neural models requires choosing a deviation coordinate and a representation set $\mathcal{R}$, which are design decisions with no canonical answer yet. For deployment in a clinical or governance setting, the binding constraints are, in likely order: (i) defining the deviation coordinate $x$ for real model classes, where the analogue of $(k - \lambda)/\sqrt{\lambda}$ is not given; (ii) calibrating the tolerance $\epsilon$ per application, which is a policy input, not a derivable one; (iii) data and compute for empirical calibration of $R_\epsilon$ on real validation sets; and (iv) regulatory acceptance of a radius‑based review trigger remains an open question not addressed in this work. Cost figures for these steps are not derived in this paper and are not projected here.

**(e) Order‑of‑magnitude performance bound (projection).** One performance projection is derivable from Section 4.5 under its stated assumptions: under the cubic law with the pure‑cubic regime $x^3 \gg 3x$ at the root, the validity radius scales as $R \propto \lambda^{1/6}$, so a hundredfold increase in the sample‑size‑like parameter $\lambda$ widens the radius by $100^{1/6} = 2.154$. Assumptions: large $\lambda$, fixed tolerance $\epsilon = 0.05$, exponential‑family setting. This is a statement about how slowly honest validity boundaries widen with data, and it is the framework’s most checkable general prediction.

**(f) Risks and misuse paths.** A quantified radius can be misused as a certificate: a team could report $R_{0.05} \approx 2.1\sigma$ as if it were an exact, validated boundary when it is an interpolation between four computed points at one parameter value, and could then operate up to the reported radius with less review than before. The radius is also tolerance‑relative, so choosing a looser $\epsilon$ manufactures a larger radius without any change in the model. Mitigation is disclosure: any deployed radius must carry its tolerance, its deviation coordinate, its parameter regime, and its interpolation status, in the machine‑readable form proposed in Section 3.

## 8. Conclusion

**Summary.** The paper introduced an adele‑like formalism that treats validated models as local charts with explicit validation domains and combines them via a restricted product over representations. Within this framework the invariant core of a model class consists of quantities unchanged under admissible representation changes, while the leading non‑invariant quantity predicts the shape of out‑of‑domain error. Applying the theory to the Poisson‑to‑Gaussian max‑entropy bridge yielded a deterministic cubic discrepancy law whose coefficient equals the excluded skewness $0.1$, and a quantified validity radius of approximately $2.1\sigma$ for a $5\%$ log‑tolerance. The analysis relied on hand‑computed Stirling approximations and explicit cumulant calculations. Limitations include reliance on a single parameter value, interpolation for the radius, and the untested generality of the invariant‑core claim beyond exponential‑family examples. Nevertheless, the results demonstrate how epistemic boundaries can be made operational and provide concrete targets for future empirical validation.

**Future directions.** Extending the adele‑like framework beyond the Poisson‑to‑Gaussian bridge to other exponential‑family pairs, to high‑dimensional neural surrogate models, and to real‑world clinical‑ML pipelines constitutes the next research agenda. A systematic study of how the invariant‑core criterion behaves under complex representations and how validity radii scale with increasing data volume will test the generality of the conjectures presented here. A minimal falsifying calculation—evaluating the log‑probability discrepancy at a new deviation point (e.g., $x=2.25$) or at a larger Poisson parameter (e.g., $\lambda=400$)—will provide an immediate empirical check of the cubic law and the $\lambda^{1/6}$ scaling prediction.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 2.0.0 (2026-10-21, from 1.0.1): rewritten in full through the research pipeline. references 11 -> 11. length 6698 -> 4717 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[2] A combinatorial one-cocycle in a moduli space of knots from the Vassiliev invariant of order 3. arXiv:2212.03778. https://arxiv.org/abs/2212.03778
[3] Towards a classification of unitary elements of C*-algebras. arXiv:2304.01761. https://arxiv.org/abs/2304.01761
[5] Stable but Wrong: When More Data Degrades Scientific Conclusions. arXiv:2602.05668. https://arxiv.org/abs/2602.05668
[6] Improving problem solving by exploiting the concept of symmetry. arXiv:1212.5776. https://arxiv.org/abs/1212.5776
[7] Position: Certifiable State Integrity Should Be Built from Local Validity, Not Global Scale. arXiv:2601.21249. https://arxiv.org/abs/2601.21249
[9] The Annotation Scarcity Paradox in Low-Resource NLP Evaluation: A Decade of Acceleration and Emerging Constraints. arXiv:2605.19066. https://arxiv.org/abs/2605.19066
[10] Toward a topological description of Legendrian contact homology of unit conormal bundles. arXiv:2212.13705. https://arxiv.org/abs/2212.13705
[11] Stationarity as a One-Mode Constraint on Quantum Correlation. arXiv:2610.02090. https://arxiv.org/abs/2610.02090
[12] https://papers.qnfo.org/papers/the-adele-analogy-for-epistemic-boundaries-local-models-a-restricted-product-of-. QNFO: The Adele Analogy for Epistemic Boundaries: Local Models, a Restricted Product of Representations, and a Quantified Validity Radius.
[13] https://papers.qnfo.org/papers/epistemic-cartography. QNFO: Epistemic Cut.
[14] https://papers.qnfo.org/papers/epistemic-dynamics. QNFO: Epistemic Dynamics.
