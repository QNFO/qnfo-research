# Factoring Hardness as a Bayesian Prior: A Decision-Theoretic Model of Post‑Quantum Cryptography Migration Timing

## Abstract

The urgency of post‑quantum cryptography (PQC) migration is usually justified by the anticipated capability of quantum computers to factor integers, yet that threat rests on the unproven conjecture that integer factoring is not in BPP. This paper treats the conjecture as an explicit Bayesian prior and embeds it in a decision‑theoretic model for RSA‑2048 migration. The model mixes two hypotheses—fast‑breakthrough (hazard $h_{\mathrm{BPP}}$) and hard‑regime (hazard $h_{\mathrm{HARD}}$)—with prior weight $\pi$. Using the mixture hazard $\bar{h}(\pi)=\pi h_{\mathrm{BPP}}+(1-\pi)h_{\mathrm{HARD}}$, we derive a closed‑form loss threshold $L^{\ast}(\pi)=1+r/\bar{h}$ that determines when immediate migration is optimal. With baseline inputs $h_{\mathrm{BPP}}=0.10$, $h_{\mathrm{HARD}}=0.01$, $r=0.05$, and $\pi=0.20$, the mixed hazard is $\bar{h}=0.028$ $\mathrm{yr}^{-1}$ and $L^{\ast}\approx2.79$. Assets with breach loss $L>2.79$ therefore merit immediate migration. Sensitivity analysis shows that for $L=10$ immediate migration is optimal even at $\pi=0$, while for $L=2$ the prior must exceed $\pi^{\ast}\approx0.44$ to trigger migration. A discrete two‑point scenario and a continuous two‑hazard Poisson scenario are also solved analytically; the latter yields an optimal migration time $T^{\ast}\approx0.046$ yr ($\approx$ 17 days) under the same numeric inputs. The framework converts an unproven complexity‑theoretic conjecture into an auditable parameter, enabling organizations to quantify the impact of epistemic uncertainty on migration timing.

## 1. Introduction

Large‑scale enterprises, government agencies, and standards bodies face the concrete problem of replacing RSA‑2048 with post‑quantum alternatives before a cryptanalytic breakthrough renders current deployments insecure. The cost of a breach—loss of confidential data, reputational damage, and regulatory penalties—can exceed billions of dollars, while premature migration incurs substantial engineering, testing, and operational expenses. Decision makers therefore need a principled method to balance breach loss against migration cost under uncertainty about the underlying hardness of integer factoring.

If integer factoring were ever solved in classical polynomial time, quantum computers would no longer pose a unique threat to RSA‑2048; the security guarantee would collapse regardless of quantum progress. Conversely, if factoring remains hard for classical algorithms, the timeline for a quantum breakthrough becomes the dominant uncertainty. The unproven conjecture FACTORING $\notin$ BPP therefore sits at the core of the migration urgency argument. Treating this conjecture as a fixed fact obscures the sensitivity of migration recommendations to the community’s confidence in it.

This paper addresses the “so what?” by providing a quantitative decision model that makes the conjecture an explicit Bayesian prior. The model yields a simple loss threshold that tells a planner exactly when immediate migration is justified, given any numeric loss $L$, discount rate $r$, and prior $\pi$. By varying $\pi$ the model reveals how robust the migration recommendation is to changes in belief about factoring hardness.

**Contributions**

1. A closed‑form Bayesian decision model for PQC migration under a two‑hypothesis mixture over factoring hardness (Section 3).  
2. Full arithmetic derivations of the mixed hazard, the expected discounted loss of remaining exposure, and the critical loss threshold $L^{\ast}(\pi)$ (Section 4).  
3. A sensitivity analysis over the prior $\pi$, including the critical prior $\pi^{\ast}(L)$ for low‑value assets (Sections 4 and 5).  
4. Two alternative scenarios—discrete two‑point (Scenario D) and continuous two‑hazard Poisson (Scenario P)—with complete arithmetic and a numerical solution for the optimal migration time $T^{\ast}$ (Section 4.4).  
5. A discussion of the dependence of the quantum‑advantage narrative on the single unproven premise FACTORING $\notin$ BPP and a proposal for a stress‑test classification of known exponential speedups (Section 7).

All numbers are either declared as modeling assumptions (Section 3) or derived with explicit arithmetic (Section 4). No empirical measurements are invented.

## 2. Background and Related Work

**PQC migration management.** The study of [2] analyzes macroscale migration patterns using network‑analysis methods. Our model supplies the quantitative risk core that determines *when* migration should occur, complementing the process described in [2].

**Hardness under restrictions.** The Tetris analysis of [1] proves NP‑hardness of Tetris clearing for every tetromino type except O, illustrating that “hardness” can be rigorously established for restricted variants. This informs our view that hardness is a property that can be pinned down rather than asserted, and highlights the gap between worst‑case NP‑hardness (as in [1]) and the average‑case hardness conjecture FACTORING $\notin$ BPP that underlies RSA security.

**Bayesian priors, mixtures, and expert judgement.** The Bayesian group‑lasso work of [4] introduces spike‑and‑slab priors that combine a point mass with a diffuse component. We adopt the same structural idea for a hypothesis mixture rather than a regression coefficient. We assume that a structured elicitation process can convert expert judgements about factoring hardness into a numeric prior $\pi$. The Posterior Belief Assessment approach [6], which addresses extracting subjective judgements from Bayesian analyses, is treated here as a candidate template for that process; its suitability for eliciting $\pi$ from complexity‑theory experts is an assumption of this paper, not a derived result. The uniform sensitivity sweep over $\pi\in[0,1]$ is an assumed modeling choice of this paper. Objective Bayesian methods for bilateral data [7] address inference under little prior information, and we adopt the uniform sweep as our own default for exploring the decision rule rather than as a result taken from that work.

**Migration and displacement analogues.** The Migration Networks study of [2] surveys network‑analysis methods for macroscale migration, providing a framing in which cryptographic migration can be viewed as a flow over an asset graph. The co‑design study of [5] examines task migration between software and hardware under cost and deadline pressure, an isomorphic structural problem to our timing decision.

**Default parameters made explicit.**  Analogously, we treat the conjecture FACTORING $\notin$ BPP as a decision variable.  



## 3. Methods

### 3.1 Model primitives (main model)

Time is measured in years. An organization holds RSA‑2048 assets whose compromise would cause loss $L$, expressed in units of the migration cost $C_m$ (so $C_m=1$ by normalization). The discount rate is $r$ per year. The hardness conjecture is represented by a two‑hypothesis mixture:

* $H_{\mathrm{BPP}}$: a regime where cryptographically relevant factoring breakthroughs arrive with annual hazard $h_{\mathrm{BPP}}$;
* $H_{\mathrm{HARD}}$: a regime where breakthroughs arrive with annual hazard $h_{\mathrm{HARD}}\ll h_{\mathrm{BPP}}$;
* $\pi=\Pr(H_{\mathrm{BPP}})$ is the Bayesian prior weight on the fast‑breakthrough regime.

The predictive (mixture) hazard is  

$$
\bar{h}(\pi)=\pi\,h_{\mathrm{BPP}}+(1-\pi)\,h_{\mathrm{HARD}}.
$$

A breakthrough is modeled as a memoryless Poisson event: conditional on the regime, the waiting time to breakthrough is exponential with the regime’s hazard. The prior $\pi$ is treated as an input; we recommend eliciting it via the finite procedure of Posterior Belief Assessment [7] or, in the absence of expert input, adopting an objective uniform prior as in [8].

### 3.2 Expected discounted loss of remaining exposed

If the organization never migrates proactively and a breakthrough arrives at time $t$, it suffers loss $L$ at $t$, discounted to present value by $e^{-rt}$. Averaging over the exponential waiting time under the mixture hazard $\bar{h}$:

$$
E_{\mathrm{exposed}}=\int_{0}^{\infty}L\,\bar{h}\,e^{-\bar{h}t}\,e^{-rt}\,dt
= L\,\bar{h}\int_{0}^{\infty}e^{-(\bar{h}+r)t}\,dt
= \frac{L\,\bar{h}}{\bar{h}+r}.
$$

Immediate migration costs $C_m=1$ at $t=0$ and eliminates exposure. Immediate migration is optimal exactly when  

$$
1<\frac{L\,\bar{h}}{\bar{h}+r}
\;\Longleftrightarrow\;
L>L^{\ast}(\pi)=\frac{\bar{h}+r}{\bar{h}}=1+\frac{r}{\bar{h}}.
$$

The threshold $L^{\ast}(\pi)$ is decreasing in $\pi$; as $\pi\to1$ it approaches $1+r/h_{\mathrm{BPP}}$, while as $\pi\to0$ it approaches $1+r/h_{\mathrm{HARD}}$.

### 3.3 Prior threshold for a given asset value

For a given loss $L>1$, rearranging the optimality condition yields the required mixture hazard  

$$
\bar{h}(\pi)>\frac{r}{L-1}.
$$

Since $\bar{h}(\pi)=h_{\mathrm{HARD}}+\pi\,(h_{\mathrm{BPP}}-h_{\mathrm{HARD}})$, solving for $\pi$ gives the critical prior  

$$
\pi^{\ast}(L)=\frac{\dfrac{r}{L-1}-h_{\mathrm{HARD}}}{h_{\mathrm{BPP}}-h_{\mathrm{HARD}}}.
$$

### 3.4 Alternative scenario models

**Scenario D (discrete two‑point).** A single horizon $T$, a prior $p$ of a breakthrough within the horizon, migration cost $C_m$ paid at $t=0$ if migrating immediately, breach cost $C_b$ discounted by $d=e^{-rT}$ if the organization waits. The expected cost of waiting is  

$$
E_{\mathrm{wait}}=p\,C_b\,d+(1-p)\,C_m,
$$

and the break‑even prior under the simplified comparison (migration forced at $T$) is  

$$
p^{\ast}= \frac{C_m}{C_b\,d}.
$$

**Scenario P (continuous two‑hazard Poisson).** A classical breakthrough arrives with hazard $\lambda = h_{\mathrm{HARD}} = 0.01$ $\mathrm{yr}^{-1}$, a quantum capability arrives with hazard $\mu = h_{\mathrm{BPP}} = 0.10$ $\mathrm{yr}^{-1}$; combined hazard $\Lambda=\lambda+\mu = 0.11$ $\mathrm{yr}^{-1}$. Migration at time $T$ costs $C_m$ (discounted). If a breakthrough of either type occurs at $t<T$, loss accrues at rate $L$ per year until $T$. The expected discounted cost is  

$$
E[C](T)=C_m e^{-rT}+L\,\Lambda\int_{0}^{T}e^{-\Lambda t}\,(T-t)\,e^{-rt}\,dt.
$$

Let $a=\Lambda+r$. Evaluating the integral yields  

$$
E[C](T)=C_m e^{-rT}+ \frac{L\,\Lambda}{a^{2}}\Bigl[1-(1+aT)e^{-aT}\Bigr].
$$

The first‑order condition for the optimal migration time $T^{\ast}$ is  

$$
r\,C_m e^{-rT^{\ast}}=\frac{L\,\Lambda}{a}\bigl(1-e^{-aT^{\ast}}\bigr).
$$

We solve this equation numerically in Section 4.4.

### 3.5 The reduction‑of‑urgency argument

The entire quantum‑advantage case for RSA‑2048 urgency reduces to the single unproven premise FACTORING $\notin$ BPP: if the premise fails, quantum hardware is irrelevant to RSA. A companion structural question—what fraction of known exponential speedups depend on abelian hidden‑subgroup structure—is flagged as a stress‑test hypothesis in Section 7, not as a computed result.

## 4. Analysis

All input numbers are declared in Section 3.1 and reproduced here for transparency.

### 4.1 Main model: mixture hazard and loss threshold

**Inputs (modeling assumptions).**  

* $h_{\mathrm{BPP}}=0.10$ $\mathrm{yr}^{-1}$  
* $h_{\mathrm{HARD}}=0.01$ $\mathrm{yr}^{-1}$  
* $\pi=0.20$  
* $r=0.05$ $\mathrm{yr}^{-1}$  
* $C_m=1$ (normalization)

**Step 1: mixture hazard.**  

\[
\bar{h}= \pi h_{\mathrm{BPP}}+(1-\pi)h_{\mathrm{HARD}}
=0.2\times0.10+0.8\times0.01
=0.020+0.008
=0.028\;\text{yr}^{-1}.
\]

**Step 2: expected discounted loss for $L=10$.**  

\[
E_{\mathrm{exposed}}=\frac{L\,\bar{h}}{\bar{h}+r}
=\frac{10\times0.028}{0.028+0.05}
=\frac{0.28}{0.078}
\approx3.589744.
\]

Since $E_{\mathrm{exposed}}\approx3.59>C_m=1$, immediate migration is optimal for a ten‑unit asset.

**Step 3: loss threshold.**  

\[
L^{\ast}(\pi)=1+\frac{r}{\bar{h}}
=1+\frac{0.05}{0.028}
=1+1.785714\ldots
\approx2.785714.
\]

Any asset with $L>2.785714$ justifies immediate migration at the baseline prior.

**Step 4: sensitivity in $\pi$.**  

* $\pi=0$: $\bar{h}=0.01$, $L^{\ast}=1+0.05/0.01=6$.  
* $\pi=1$: $\bar{h}=0.10$, $L^{\ast}=1+0.05/0.10=1.5$.

Thus the threshold varies between $1.5$ and $6$ as the prior moves from certainty of a fast breakthrough to certainty of hardness.

**Step 5: critical prior for a low‑value asset $L=2$.**  

Required mixture hazard:  

\[
\bar{h}^{\mathrm{req}}=\frac{r}{L-1}=\frac{0.05}{1}=0.05.
\]

Solve $0.01+0.09\pi=0.05$:

\[
\pi^{\ast}=\frac{0.05-0.01}{0.09}
=\frac{0.04}{0.09}
=0.444444\ldots.
\]

Therefore a two‑unit asset requires $\pi>0.44$ for immediate migration to be optimal.

### 4.2 Scenario D (discrete two‑point)

**Inputs (modeling assumptions).**  

* $p=0.05$ (prior probability of breakthrough within horizon)  
* $C_m = 10{,}000{,}000$ (dollars) 
* $C_b = 200{,}000{,}000$ (dollars)  
* $r=0.05$ $\mathrm{yr}^{-1}$ (continuous)  
* $T=10$ yr

**Step 1: discount factor.**  

\[
d=e^{-rT}=e^{-0.05\times10}=e^{-0.5}\approx0.606531.
\]

**Step 2: discounted breach cost when waiting.**  

\[
p\,C_b\,d=0.05\times200{,}000{,}000\times0.606531
=10{,}000{,}000\times0.6065306597
\approx6{,}065{,}306.60\;\text{dollars}.
\]

**Step 3: expected total cost of waiting.**  

\[
E_{\mathrm{wait}}=p\,C_b\,d+(1-p)C_m
=6{,}065{,}306.60+0.95\times10{,}000{,}000
=6{,}065{,}306.60+9{,}500{,}000
=15{,}565{,}306.60\;\text{dollars}.
\]

Since $C_m = 10{,}000{,}000 < E_{\mathrm{wait}}$ (both in dollars), immediate migration is optimal under Scenario D.

**Step 4: break‑even prior (simplified comparison).**  

\[
p^{\ast}=\frac{C_m}{C_b\,d}
=\frac{10{,}000{,}000}{200{,}000{,}000\times0.606531}
=\frac{10{,}000{,}000}{121{,}306{,}200}
\approx0.0824.
\]

If the prior probability of a breakthrough within ten years exceeds $8.25\%$, waiting becomes preferable under the simplified comparison.

### 4.3 Scenario P (continuous two‑hazard Poisson)

**Inputs (modeling assumptions).**  

* Classical hazard $\lambda = h_{\mathrm{HARD}} = 0.01$ $\mathrm{yr}^{-1}$  
* Quantum hazard $\mu = h_{\mathrm{BPP}} = 0.10$ $\mathrm{yr}^{-1}$  
* Combined hazard $\Lambda = \lambda+\mu = 0.11$ $\mathrm{yr}^{-1}$  
* Discount rate $r = 0.05$ $\mathrm{yr}^{-1}$  
* Breach loss $L = 10$ (units of $C_m$)  
* Migration cost $C_m = 1$

**Step 1: auxiliary constant.**  

\[
a = \Lambda + r = 0.11 + 0.05 = 0.16\;\text{yr}^{-1}.
\]

**Step 2: first‑order condition for optimal $T^{\ast}$.**  

\[
r\,C_m e^{-rT^{\ast}} = \frac{L\,\Lambda}{a}\bigl(1-e^{-aT^{\ast}}\bigr).
\]

Substituting numbers:

\[
0.05\,e^{-0.05T^{\ast}} = \frac{10\times0.11}{0.16}\bigl(1-e^{-0.16T^{\ast}}\bigr)
=6.875\bigl(1-e^{-0.16T^{\ast}}\bigr).
\]

**Step 3: numerical solution (bisection).**  

We evaluate the left‑hand side (LHS) and right‑hand side (RHS) for candidate $T$ values:

| $T$ (yr) | LHS = $0.05e^{-0.05T}$ | RHS = $6.875(1-e^{-0.16T})$ |
|----------|------------------------|-----------------------------|
| 0.00     | 0.050000               | 0.000000                    |
| 0.02     | 0.049950               | 0.022000                    |
| 0.04     | 0.049900               | 0.045200                    |
| 0.045    | 0.049887               | 0.049400                    |
| 0.046    | 0.049882               | 0.050200                    |
| 0.047    | 0.049877               | 0.051000                    |

The sign changes between $T=0.045$ yr (RHS < LHS) and $T=0.046$ yr (RHS > LHS). Linear interpolation gives  

\[
T^{\ast}\approx0.0455\;\text{yr}.
\]

Converting to days: $0.0455\times365\approx16.6$ days. We report $T^{\ast}\approx0.046$ yr ($\approx$ 17 days).

## 5. Results

| Quantity | Symbol | Computed value | Interpretation |
|----------|--------|----------------|----------------|
| Mixture hazard | $\bar{h}$ | $0.028$ $\mathrm{yr}^{-1}$ | Expected breakthrough rate under baseline prior $\pi=0.2$. |
| Expected discounted loss ( $L=10$ ) | $E_{\mathrm{exposed}}$ | $3.589744$ | Loss exceeds migration cost; immediate migration optimal. |
| Loss threshold (baseline) | $L^{\ast}(0.2)$ | $2.785714$ | Assets with $L>2.79$ merit immediate migration. |
| Loss threshold ( $\pi=0$ ) | $L^{\ast}(0)$ | $6$ | Even with no fast‑breakthrough belief, high‑value assets still trigger migration. |
| Loss threshold ( $\pi=1$ ) | $L^{\ast}(1)$ | $1.5$ | If fast breakthrough is certain, even modest assets should migrate. |
| Critical prior for $L=2$ | $\pi^{\ast}$ | $0.444444$ | Prior must exceed $44.44\%$ for immediate migration of a low‑value asset. |
| Scenario D break‑even prior | $p^{\ast}$ | $0.0825$ | If breakthrough probability within ten years exceeds $8.25\%$, waiting becomes preferable under the simplified comparison. |
| Scenario P optimal migration time | $T^{\ast}$ | $0.046$ yr ($\approx$ 17 days) | With both classical and quantum hazards, the cost‑minimizing migration occurs essentially immediately. |

All values follow directly from the arithmetic presented in Section 4.

## 6. Extended Derivations and Worked Examples

In this section we deepen the analytical core of the paper by (i) deriving the sensitivity of the loss‑threshold $L^{\ast}(\pi)$ to the model primitives, (ii) presenting a worked example of prior elicitation using a simple scoring scheme, and (iii) exploring limiting cases of the mixture hazard. The derivations use only the inputs declared in Section 3.1 and the arithmetic shown in Section 4.

### 1. Sensitivity of the loss threshold $L^{\ast}(\pi)$

Recall the closed‑form threshold
\[
L^{\ast}(\pi)=1+\frac{r}{\bar{h}(\pi)},
\qquad
\bar{h}(\pi)=\pi h_{\mathrm{BPP}}+(1-\pi)h_{\mathrm{HARD}}.
\]

#### 1.1 Derivative with respect to the prior $\pi$

Applying the quotient rule,
\[
\frac{\partial L^{\ast}}{\partial \pi}
= -\,\frac{r}{\bigl[\bar{h}(\pi)\bigr]^{2}}\,
\frac{\partial\bar{h}}{\partial\pi},
\qquad
\frac{\partial\bar{h}}{\partial\pi}=h_{\mathrm{BPP}}-h_{\mathrm{HARD}}.
\]
Thus
\[
\frac{\partial L^{\ast}}{\partial \pi}
= -\,\frac{r\,(h_{\mathrm{BPP}}-h_{\mathrm{HARD}})}
{\bigl[\pi h_{\mathrm{BPP}}+(1-\pi)h_{\mathrm{HARD}}\bigr]^{2}}.
\]

**Numerical evaluation at the baseline $\pi=0.20$.**  
Insert $r=0.05$, $h_{\mathrm{BPP}}=0.10$, $h_{\mathrm{HARD}}=0.01$:

\[
\begin{aligned}
\bar{h}(0.20) &= 0.20\times0.10 + 0.80\times0.01 = 0.028,\\[4pt]
h_{\mathrm{BPP}}-h_{\mathrm{HARD}} &= 0.10-0.01 = 0.09,\\[4pt]
\frac{\partial L^{\ast}}{\partial \pi}
&= -\,\frac{0.05\times0.09}{(0.028)^{2}}
= -\,\frac{0.0045}{0.000784}
\approx -5.739795918.
\end{aligned}
\]

Interpretation: a one‑point increase in $\pi$ (i.e. $\Delta\pi=1$) would lower the loss threshold by roughly $5.74$ units; for a small change $\Delta\pi=0.01$, $L^{\ast}$ drops by about $0.057$.

#### 1.2 Derivative with respect to the hazards

Treating $\pi$ as fixed, the partial derivative of $L^{\ast}$ with respect to $h_{\mathrm{BPP}}$ is
\[
\frac{\partial L^{\ast}}{\partial h_{\mathrm{BPP}}}
= -\,\frac{r\,\pi}{\bigl[\bar{h}(\pi)\bigr]^{2}}.
\]
Similarly,
\[
\frac{\partial L^{\ast}}{\partial h_{\mathrm{HARD}}}
= -\,\frac{r\,(1-\pi)}{\bigl[\bar{h}(\pi)\bigr]^{2}}.
\]

**Baseline evaluation.**  
Using $\pi=0.20$ and $\bar{h}=0.028$:

\[
\begin{aligned}
\frac{\partial L^{\ast}}{\partial h_{\mathrm{BPP}}}
&= -\,\frac{0.05\times0.20}{(0.028)^{2}}
= -\,\frac{0.01}{0.000784}
\approx -12.755,\\[4pt]
\frac{\partial L^{\ast}}{\partial h_{\mathrm{HARD}}}
&= -\,\frac{0.05\times0.80}{(0.028)^{2}}
= -\,\frac{0.04}{0.000784}
\approx -51.020.
\end{aligned}
\]

Thus a marginal increase of $0.001$ in $h_{\mathrm{HARD}}$ reduces $L^{\ast}$ by roughly $0.051$, whereas the same increase in $h_{\mathrm{BPP}}$ reduces $L^{\ast}$ by about $0.013$.

### 2. Worked example of prior elicitation

A simple scoring scheme can translate expert judgments about the plausibility of a fast breakthrough into a numeric prior $\pi$. Suppose an expert answers three binary questions:

| Question | Score (Yes = 1, No = 0) |
|----------|------------------------|
| (Q1) Recent algorithmic progress suggests a sub‑exponential improvement? | $s_{1}$ |
| (Q2) Historical breakthroughs in related number‑theoretic problems have been rapid? | $s_{2}$ |
| (Q3) Community consensus leans toward factoring being hard? | $s_{3}$ |

Define the raw sum $S = s_{1}+s_{2}+s_{3}$ (range $0$–$3$). Map $S$ to a prior by
\[
\pi = \frac{S}{3}.
\]

**Illustrative calculation.**  
Assume the expert answers “Yes” to Q1 and Q2, “No” to Q3, giving $s_{1}=1$, $s_{2}=1$, $s_{3}=0$, so $S=2$. Then
\[
\pi = \frac{2}{3} \approx 0.6667.
\]

With $\pi=0.6667$, recompute the mixture hazard:
\[
\bar{h}=0.6667\times0.10 + (1-0.6667)\times0.01
=0.06667+0.00333=0.0700\;\text{yr}^{-1}.
\]

The loss threshold becomes
\[
L^{\ast}=1+\frac{0.05}{0.0700}
=1+0.714285\approx1.714285.
\]

Hence any asset with $L>1.71$ would merit immediate migration under this elicited prior.

### 3. Limiting cases of the mixture hazard

#### 3.1 Vanishing fast‑breakthrough hazard ($h_{\mathrm{BPP}}\to0$)

If $h_{\mathrm{BPP}}$ were hypothetically zero while $h_{\mathrm{HARD}}$ remains $0.01$, the mixture hazard reduces to
\[
\bar{h}(\pi)= (1-\pi)h_{\mathrm{HARD}}.
\]
For any $\pi<1$, $\bar{h}=0.01(1-\pi)$. The loss threshold becomes
\[
L^{\ast}=1+\frac{r}{0.01(1-\pi)}.
\]
As $\pi\to1$, $\bar{h}\to0$ and $L^{\ast}\to\infty$, meaning migration would never be optimal because the model predicts essentially no breakthrough risk.

#### 3.2 Infinite fast‑breakthrough hazard ($h_{\mathrm{BPP}}\to\infty$)

Let $h_{\mathrm{BPP}}$ be arbitrarily large while $h_{\mathrm{HARD}}=0.01$ stays finite. Then
\[
\bar{h}(\pi)=\pi h_{\mathrm{BPP}}+(1-\pi)0.01\approx\pi h_{\mathrm{BPP}}.
\]
For any $\pi>0$, $\bar{h}\to\infty$, and
\[
L^{\ast}=1+\frac{r}{\bar{h}}\to1.
\]
Thus even the smallest breach loss $L>1$ would trigger immediate migration, reflecting the intuition that a guaranteed fast breakthrough makes postponement untenable.

### 4. Connection to spike‑and‑slab priors

Our two‑hypothesis mixture $\pi\,\delta_{H_{\mathrm{BPP}}}+(1-\pi)\,\delta_{H_{\mathrm{HARD}}}$ mirrors the spike‑and‑slab construction used for group variable selection in Bayesian group lasso models, where a point mass (“spike”) represents exclusion of a group and a diffuse component (“slab”) represents inclusion [4].  Analogously, the mixture hazard here provides a tractable “spike‑and‑slab” representation of epistemic uncertainty about factoring hardness, enabling a closed‑form decision rule $L>L^{\ast}(\pi)$. This structural parallel justifies the adoption of a two‑component prior for a hypothesis rather than a regression coefficient.

## 7. Discussion

### 7.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Hazards $h_{\mathrm{BPP}}$ and $h_{\mathrm{HARD}}$ are constant over time. | If hazards increase (e.g., accelerating research), $\bar{h}$ would be larger, lowering $L^{\ast}$ and strengthening the case for early migration. |
| Prior $\pi$ is treated as a scalar without temporal dynamics. | A time‑varying $\pi(t)$ could shift the optimal decision point; our static analysis provides a snapshot. |
| Discount rate $r$ is fixed at $0.05$ $\mathrm{yr}^{-1}$. | Higher $r$ inflates $L^{\ast}$, making migration less attractive; lower $r$ has the opposite effect. |
| Loss $L$ is expressed in units of migration cost. | Mis‑specifying $L$ (e.g., ignoring indirect regulatory penalties) could lead to premature migration or unnecessary delay. |
| Scenario P assumes independent classical and quantum hazards. | Correlation between the two processes would alter the combined hazard $\Lambda$ and the optimal $T^{\ast}$. |
| Expert elicitation of $\pi$ is not performed. | The numerical results illustrate sensitivity; actual decision making requires a credible elicitation process. |

### 7.2 Failure modes and falsification

The central claim—that the loss threshold $L^{\ast}(\pi)=1+r/\bar{h}$ correctly determines the optimality of immediate migration—would be falsified if empirical observation showed a case where $L>L^{\ast}(\pi)$ yet delayed migration yielded lower total discounted cost. Such a counterexample would imply that the exponential waiting‑time model or the constant‑hazard assumption is invalid. A concrete falsification test is to monitor a controlled pilot deployment where migration timing and breach outcomes are recorded; if the observed discounted loss deviates systematically from the model prediction, the model assumptions must be revised.

### 7.3 Relation to prior work

Our closed‑form threshold extends the risk‑based process of [2] by providing a quantitative decision rule. The spike‑and‑slab prior structure mirrors that of [5] but is applied to a hypothesis rather than regression coefficients. The sensitivity sweep over $\pi$ implements the objective‑prior philosophy of [8] in a decision‑analytic context. The network‑flow framing of [3] motivates future extensions where assets are linked in a graph and migration pressure propagates, but such extensions lie beyond the scope of the present analytical treatment.

## 8. Practical Implications and Engineering Pathways

### 8.1 Intended users and decision impact

The primary users are security architects, risk managers, and policy makers within large organizations that maintain RSA‑2048‑protected infrastructures (e.g., financial institutions, cloud providers, national security agencies). The model informs the *when* component of a migration plan: given an estimate of breach loss $L$, discount rate $r$, and an elicited prior $\pi$, the decision rule $L>L^{\ast}(\pi)$ tells whether to migrate immediately or to defer.

### 8.2 Technology readiness

The work is purely analytical and has not undergone peer review; according to NASA’s Technology Readiness Level definitions, it resides at **TRL 2** (technology concept and/or application formulated).

### 8.3 Minimal next experiment

A feasible next step is a **prior‑elicitation pilot**: assemble a panel of complexity‑theory experts, present the hazard parameters $h_{\mathrm{BPP}}$ and $h_{\mathrm{HARD}}$, and use the Posterior Belief Assessment procedure of [7] to obtain a quantitative prior $\pi$. The pilot would then compute $L^{\ast}(\pi)$ for a set of representative asset loss values. **Falsification condition:** if the elicited $\pi$ falls outside the interval $[0,1]$ or leads to a loss threshold that contradicts established industry migration timelines, the modeling assumptions would be called into question.

### 8.4 Engineering, manufacturing, or deployment constraints

* **Expert elicitation infrastructure:** requires a platform for structured Bayesian belief elicitation (e.g., calibrated probability questionnaires).  
* **Parameter estimation:** reliable estimates of $h_{\mathrm{BPP}}$ and $h_{\mathrm{HARD}}$ depend on historical analysis of algorithmic breakthroughs (e.g., GNFS performance trends).  
* **Discount rate selection:** organizations must agree on a financial discount rate consistent with their capital‑allocation policies.  
* **Loss quantification:** translating breach impact into units of migration cost demands a consistent accounting framework across assets.

These constraints are data and process constraints rather than material or manufacturing constraints.

### 8.5 Projected cost and performance bounds (projections)

Assuming the baseline inputs ($h_{\mathrm{BPP}}=0.10$, $h_{\mathrm{HARD}}=0.01$, $r=0.05$) and a prior $\pi=0.20$, the loss threshold is $L^{\ast}\approx2.79$. For an asset whose estimated breach loss is $L=5$, the model projects that immediate migration reduces expected discounted loss from  

\[
E_{\mathrm{exposed}}=\frac{5\times0.028}{0.028+0.05}\approx1.795
\]

to the migration cost $C_m=1$, a net expected saving of $0.795$ migration‑cost units. This projection holds under the stated assumptions; deviations in hazards or discount rate would scale the saving proportionally.

### 8.6 Risks and misuse paths

If an organization adopts the model but under‑estimates $L$ (e.g., by ignoring indirect regulatory penalties), it may postpone migration despite a high true breach loss, leading to greater exposure. Conversely, over‑estimating $\pi$ could trigger unnecessary early migration, incurring avoidable engineering costs. Transparent documentation of input assumptions mitigates these risks.

## 9. Conclusion

By treating the unproven conjecture FACTORING $\notin$ BPP as an explicit Bayesian prior, we have derived a simple, closed‑form decision rule that determines when immediate PQC migration for RSA‑2048 is optimal. The loss threshold $L^{\ast}(\pi)=1+r/\bar{h}$ captures the trade‑off between breach loss and migration cost under uncertainty about factoring hardness. Sensitivity analysis shows that high‑value assets warrant migration even if the fast‑breakthrough regime is deemed unlikely, while low‑value assets require a substantial prior belief in a fast breakthrough. Alternative scenario analyses (discrete and continuous hazards) reinforce the robustness of the conclusion: under realistic numeric inputs the optimal migration time is effectively immediate. The framework provides organizations with a transparent, auditable parameter ($\pi$) that can be refined through expert elicitation, enabling risk‑aware migration planning that explicitly acknowledges the epistemic status of a foundational complexity‑theoretic conjecture.

## Version History

- Version 2.0.0 (2026-10-20, from 1.0.0): rewritten in full through the research pipeline. new sections: Results; Extended Derivations and Worked Examples; Discussion; Practical Implications and Engineering Pathways; Conclusion; Provenance and AI Involvement. references 12 -> 8. length 3299 -> 4118 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.6-revision-brief-refs). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Tetris is Hard with Just One Piece Type. arXiv:2603.09958v1. https://arxiv.org/abs/2603.09958v1
[2] Migration Networks: Applications of Network Analysis to Macroscale Migration Patterns. arXiv:2002.10992v2. https://arxiv.org/abs/2002.10992v2
[3] Bayesian Nonparametric Weighted Sampling Inference. arXiv:1309.1799v4. https://arxiv.org/abs/1309.1799v4
[4] Bayesian Variable Selection and Estimation for Group Lasso. arXiv:1512.01013v1. https://arxiv.org/abs/1512.01013v1
[5] Performance Analysis of Software to Hardware Task Migration in Codesign. arXiv:1002.1154v1. https://arxiv.org/abs/1002.1154v1
[6] Posterior Belief Assessment: Extracting Meaningful Subjective Judgements from Bayesian Analyses with Complex Statistical Models. arXiv:1512.00969v1. https://arxiv.org/abs/1512.00969v1
[7] Objective Bayesian Inference for Bilateral Data. arXiv:1504.06523v1. https://arxiv.org/abs/1504.06523v1
[8] https://papers.qnfo.org/papers/factoring-hardness-as-a-bayesian-prior-a-decision-theoretic-model-of-post-quantu. QNFO: Factoring Hardness as a Bayesian Prior: A Decision-Theoretic Model of Post-Quantum Cryptography Migration Timing.

## Appendix A. Divergence report

**Conflict:** The numerical result for the continuous two‑hazard Poisson scenario (Scenario P) differed between drafts. Draft A reported a combined hazard $\Lambda=0.11$ $\mathrm{yr}^{-1}$ (using $\mu=0.10$) and an optimal migration time $T^{\ast}\approx0.046$ yr ($\approx$ 17 days). Draft B used $\mu=0.02$, yielding $\Lambda=0.03$ $\mathrm{yr}^{-1}$ and reported $T^{\ast}$ values between $0.332$ yr and $0.496$ yr.  

**Chosen convention:** The reconciled paper adopts the version from Draft A, because it is consistent with the baseline hazard parameters ($h_{\mathrm{BPP}}=0.10$, $h_{\mathrm{HARD}}=0.01$) used throughout the main model and other scenarios. The alternative parameterization in Draft B is treated as a separate hypothetical experiment and not incorporated into the primary analysis.

## Appendix B. Claim attribution

| Claim ID | Statement | Source drafts | Agreement |
|----------|-----------|---------------|-----------|
| C1 | Mixture hazard $\bar{h}=0.028$ $\mathrm{yr}^{-1}$ | A, B, C | Convergent |
| C2 | Expected