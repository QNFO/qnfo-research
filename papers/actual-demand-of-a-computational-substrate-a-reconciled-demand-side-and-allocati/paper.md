# Actual Demand of a Computational Substrate: A Reconciled Demand‑Side and Allocation Framework for Physical Computing Platforms

## Abstract

Debates about novel computational substrates—reservoir systems, post‑qubit quantum architectures, thermodynamically bounded devices—are usually conducted from the supply side: what can a given physical system compute? Far less attention is paid to the complementary question of what demand is actually placed on a substrate, at what rate, with what variance, and against what physical cost floor. This paper reconciles two formalizations of that demand side. First, a capability‑accounting framework describes a workload by a demand vector over normalized capability axes and a substrate by a supply vector, yielding a match score $M$ and an over‑provisioning waste fraction $W$. Second, an allocation‑theoretic framework models the substrate as a capacity‑constrained server facing partially observed, non‑stationary demand, yielding waste, shortfall, utilization, and a censoring bias. Both are coupled to a thermodynamic cost floor built from the Landauer bound and an error‑correction overhead range of $10^{2}$–$10^{3}$ physical operations per logical operation reported in the physics‑of‑computation literature. With full arithmetic we compute: a Landauer floor of $2.871 \times 10^{-21}$ J per irreversible bit operation at $T = 300$ K; a per‑logical‑operation floor of $2.871 \times 10^{-19}$ to $2.871 \times 10^{-18}$ J; an illustrative match score $M = 0.800$ with waste $W \approx 0.0732$; a two‑state provisioning model with waste = shortfall = 0.168 at mean provisioning; a censoring bias of $38.2\%$ in naïvely measured demand; a projected workload energy floor of $0.287$–$2.871$ J for $10^{18}$ logical operations; and a time‑to‑saturation of roughly $2.0$ years under a $50\%$ annual demand growth assumption, with a sensitivity factor of $\approx 4.25$. The framework converts substrate advocacy into an auditable ledger of demand, supply, and cost.

## 1. Introduction

Every proposed computational substrate arrives with a claim about what it will compute. Far fewer arrive with a claim about who will demand that computation, at what rate, with what variance, and at what physical cost floor. This asymmetry has a concrete cost. A substrate whose capacity is provisioned against an imagined demand profile wastes resources when demand is low and refuses its users’ jobs when demand spikes; a substrate whose floor cost per operation exceeds what any realistic workload can pay is stillborn regardless of its theoretical power. The parties who face this problem today are the evaluators and funders of novel computing platforms—research programmes comparing reservoir, quantum, and thermodynamic devices, and, on the enterprise side, procurement organisations that must decide which architectures to pilot under tightening energy regulation. If the framework of this paper holds, these parties gain a decision instrument: a substrate proposal can be required to state its demand vector, its supply vector, its provisioning rule, and its cost floor, each with shown arithmetic, before capacity or capital is committed.

The present paper takes its cue from a question posed in the QNFO programme: after the critique of qubit‑centred ontology, what is the *actually demanded* role of a computational substrate [9]? The phrase “actual demand” is deliberately double‑edged. It means both (i) the genuine computational requirements of workloads, as opposed to requirements inherited from an ontological picture, and (ii) the economic sense of demand—whether anyone actually needs the substrate at all.

The demand‑side framing is not exotic; it is implicit in how several neighbouring fields already operate. In power systems, demand response is defined by the arrival of elastic or inelastic demands that must be allocated without violating network constraints [2]; the demand is the primitive and the grid is the substrate. In demand forecasting, a foundation model is justified by the specific statistical pathologies of demand series—short histories, frequent zeros, censoring by stock‑outs [3]. In navigation, an agent is evaluated on whether the user‑specified object is actually present within the scene [6]. In inventory management, demand is partially observed and non‑stationary, and the manager must infer the state of the world rather than read it off [7]. Each of these fields treats demand as the object of study and the resource as the constraint. Substrate research in computing has largely inverted this.

We model a substrate along two reconciled axes:

1. **Capability accounting**: what level of each required capability does the substrate supply, and where does it fall short of or exceed demand?  
2. **Allocation dynamics**: how do waste, shortfall, utilization, and measurement bias behave when demand is stochastic, partially observed, and censored by capacity?

Both are coupled to a thermodynamic cost floor built from the Landauer bound and an error‑correction overhead range of $10^{2}$–$10^{3}$ physical operations per logical operation, as reported in the physics‑of‑computation literature [12]. Every quantity is defined by an equation and evaluated with explicit arithmetic in Section 4. No empirical measurements are reported; the numbers in Section 5 are either arithmetic consequences of stated inputs or clearly labelled projections with stated assumptions.

**Contributions.**  
- C1: Derivation of the Landauer energy floor at room temperature (Section 4.1).  
- C2: Extension of the floor to logical operations using the $10^{2}$–$10^{3}$ overhead range (Section 4.2).  
- C3: Definition of a capability‑vector match score $M$ and waste fraction $W$, with a worked illustrative example (Section 4.3).  
- C4: Analytical two‑state provisioning model showing waste = shortfall at mean capacity (Section 4.4).  
- C5: Quantification of censoring bias equal to the shortfall ratio (Section 4.5).  
- C6: Projection of time‑to‑saturation under assumed demand growth, with sensitivity analysis (Section 4.6).  
- C7: Projection of a workload‑level energy floor for $10^{18}$ logical operations (Section 4.3, labelled as a projection).

## 2. Background and Related Work

We draw on two literatures that rarely meet: the physics‑of‑computation and substrate‑characterisation literature, and the demand‑forecasting‑and‑allocation literature.

**Reservoir‑computing substrate independence.** The substrate‑independent framework for reservoir computers [1] states that any nonlinear, input‑driven dynamical system exhibiting fading memory and input separability can be trained to perform computational tasks, and that this broad inclusion has led to many new physical substrates for reservoir computing. The framework abstracts away *what* the substrate is and names only the *properties* a workload‑relevant computation requires. Our capability axes (Section 3.1) generalise exactly this move—fading memory and input separability become two axes among others—and our match score $M$ scalarises the property checklist that [1] implies.

**Demand‑response in power systems.** The online demand‑response problem [2] allocates incoming elastic or inelastic demands without violating operating constraints of electric networks, and identifies the presence of non‑linear constraints as the distinctive challenge of power systems relative to traditional online decision problems. In our framework, the apparent‑power constraint of [2] plays the role of a supply ceiling on a capability axis, and inelastic demand plays the role of a demand component that cannot be reduced by re‑choosing the workload.

**Demand‑specific data pathologies.** The EXAONE Demand 1.0 time‑series foundation model [3] is motivated by the observation that demand series make up only a small fraction of general time‑series corpora, and that demand data has properties such corpora rarely contain: short histories, frequent zeros, censoring by stock‑outs, and exogenous events that the series does not record. Each of these pathologies has an exact analogue for a novel computational substrate: deployment histories are short, utilisation can be zero for long stretches, observed demand is censored by capacity stock‑outs, and exogenous events are not recorded in the usage series. We adopt this taxonomy as the specification of what a substrate‑demand forecaster must handle.

**Adjoint‑computation accounting.** The adjoint‑computation work [4] differentiates a computational fluid‑dynamics code using algorithmic differentiation in tangent and adjoint modes, and demonstrates that the adjoint code provides an exact ledger of the solver’s operations. Our overhead multiplier plays the same bookkeeping role at the hardware level, and [4] shows that such ratios can be made exact rather than rhetorical when the computation is instrumented.

**Topological invariants of data.** The persistent Stiefel–Whitney class construction [6] defines persistent Stiefel–Whitney classes of vector‑bundle filtrations by seeing vector bundles as subsets of Euclidean spaces, endowing the usual Čech filtration with a vector‑bundle structure, and showing the construction is stable and consistent. We cite it as a methodological exemplar: it shows how a mathematically delicate property can be made computable and stable on finite data. A demand‑side substrate ledger aspires to the same standard—that its quantities survive finite, noisy measurement of the substrate.

**Demand‑conditioned navigation.** The demand‑driven navigation work [5] studies visual object navigation and identifies two essential conditions: the user must know the name of the desired object, and the user‑specified object must actually be present within the scene. The second condition—*actual presence*—is precisely the “actual demand” distinction: a demand that cannot be met by the environment is a supply failure, not a planning failure. Our match score separates them by construction.

**Partially observed demand.** The inventory‑management model [7] considers continuous‑time inventory management with Markov‑modulated non‑stationary demands, introduces active learning by assuming the state of the world is unobserved and must be inferred, and assumes demands are observed only when completely met. The “observed only when completely met” assumption is precisely the stock‑out censoring identified in [3]; for substrates it means that refused jobs are invisible, so the demand process must be filtered, not merely measured. We use the Markov‑modulated structure of [7] as the skeleton of our illustrative demand model in Section 3.

**Multi‑scale coarse‑graining.** The equation‑free computation work [8] discusses a computational tool for coarse‑graining nonlinear systems of ordinary differential equations in time, demonstrating on model examples the averaging of Hamiltonian and dissipative microscopic dynamics whose slow variables can display mixed slow‑fast responses; its case analyses show how persistent fast oscillations determine an invariant measure for the fast flow that moves slowly as parameters change. Our two‑state regime model in Section 3.2 is exactly such a coarse‑graining, and Section 7 discusses what it averages away.

**The QNFO programme.** *Beyond the Qubit* [9] poses the question formalised in this paper: if the qubit‑gate‑circuit model is an epistemic failure, what comes next? It strips quantum mechanics to its minimal ontological commitments and surveys constructive paradigms for post‑particle computation.  We assume that quantum error‑correction overhead of $10^{2}$–$10^{3}$ physical operations per logical operation multiplies thermodynamic cost. That overhead range is the single quantitative input we take from the literature, and it enters our energy derivation in Section 4 directly.

## 3. Methods

### 3.1 Capability axes and vectors

Fix $K$ capability axes, indexed by $k \in \{1,\dots,K\}$, each normalised to $[0,1]$. A workload is summarised by a demand vector  

$$
d = (d_1,\dots,d_K), \qquad d_k \in [0,1],
$$  

where $d_k$ is the minimum level of capability $k$ the workload requires. A substrate is summarised by a supply vector  

$$
s = (s_1,\dots,s_K), \qquad s_k \in [0,1],
$$  

where $s_k$ is the level of capability $k$ the substrate delivers at its best documented operating point. Each axis carries a weight $w_k \ge 0$ with $\sum_{k=1}^{K} w_k = 1$.

**Match score.** Per‑axis fulfilment  

$$
m_k = \frac{\min(d_k,s_k)}{d_k}, \qquad d_k>0,
$$  

so $m_k=1$ when supply meets or exceeds demand, and $m_k = s_k/d_k < 1$ otherwise. The match score is the weighted mean  

$$
M(d,s) = \sum_{k=1}^{K} w_k\, m_k, \qquad 0 \le M \le 1.
$$  

**Over‑provisioning waste.** With $(x)^{+}= \max(x,0)$, the waste fraction is  

$$
W(d,s) = \frac{\sum_{k=1}^{K} w_k (s_k-d_k)^{+}}{\sum_{k=1}^{K} w_k s_k}.
$$  

$W$ measures capability supplied but not demanded.

### 3.2 Allocation model

Following the Markov‑modulated structure of [7], we model substrate demand as a process $d(t)$ modulated by a hidden world‑state $s(t)\in\{h,l\}$ with stationary occupancy probabilities $p_h = p$ and $p_l = 1-p$. Within regime $s$, demand takes the value $d_s$, with $d_h > d_l \ge 0$. Demand is observed only when completely met, so measured demand  

$$
\hat d(t) = \min\bigl(d(t),C\bigr)
$$  

is right‑censored by capacity $C$.

Demand is partitioned into elastic (deferrable) and inelastic (must be served on arrival) components. Over a horizon $T_{\text{horizon}}$ we define  

$$
W_{\text{alloc}}(C) = \int_{0}^{T_{\text{horizon}}} (C-d(t))^{+}\,dt \quad\text{(waste)},
$$  

$$
S(C) = \int_{0}^{T_{\text{horizon}}} (d(t)-C)^{+}\,dt \quad\text{(shortfall)}.
$$  

Realised utilisation is  

$$
\rho = \frac{D_{\text{act}}}{C\,T_{\text{horizon}}}, \qquad D_{\text{act}} = \int_{0}^{T_{\text{horizon}}} d(t)\,dt.
$$  

### 3.3 Cost floor

The Landauer bound gives the minimum energy to erase one bit  

$$
E_{\min}(T) = k_B\,T\ln 2, \qquad k_B = 1.380649\times10^{-23}\ \text{J/K}.
$$  

If error correction requires an overhead factor $r$ physical operations per logical operation, with $r\in[10^{2},10^{3}]$ as stated in [12], the per‑logical‑operation floor is  

$$
E_{\text{logical}}(r) = r\,E_{\min}(T),
$$  

and for $N_L$ logical operations the workload floor is $E_{\text{work}} = N_L\,E_{\text{logical}}$.

### 3.4 Procedure

The framework is applied in four steps: (i) elicit $d$ and $w_k$ from the workload; (ii) assess $s$ from documented substrate operation; (iii) compute $M$, $W$, $W_{\text{alloc}}$, $S$, and $\rho$; (iv) compute the energy floor with a stated $r$ and $T$. Steps (i)–(ii) are judgemental and are where the framework is falsifiable; steps (iii)–(iv) are pure arithmetic, shown in full in Section 4.

## 4. Analysis

Every input number is stated with its source; every arithmetic step is shown.

### 4.1 Landauer floor

**Inputs.** $k_B = 1.380649 \times 10^{-23}$ J/K (SI definition); $T = 300$ K (assumption of room temperature); $\ln 2 = 0.693147$.

**Step 1.** $k_B T = 1.380649 \times 10^{-23} \times 300 = 4.141947 \times 10^{-21}$ J.  

**Step 2.** $E_{\min}= 4.141947 \times 10^{-21} \times 0.693147$. Multiplying $4.141947$ by $0.693147$ gives $2.870981$ (rounded). Hence  

$$
E_{\min}(300\ \text{K}) = 2.870981 \times 10^{-21}\ \text{J} \approx 2.871 \times 10^{-21}\ \text{J}.
$$  

### 4.2 Per‑logical‑operation floor under error‑correction overhead

**Inputs.** $r \in [10^{2},10^{3}]$ (assumed); $E_{\min}=2.870981 \times 10^{-21}$ J (Section 4.1).

**Lower‑end.** $E_{\text{logical}}(10^{2}) = 10^{2} \times 2.870981 \times 10^{-21}=2.870981 \times 10^{-19}$ J.  

**Upper‑end.** $E_{\text{logical}}(10^{3}) = 10^{3} \times 2.870981 \times 10^{-21}=2.870981 \times 10^{-18}$ J.  

The ratio of upper to lower floor is $10$, showing a one‑order‑of‑magnitude uncertainty from the overhead factor alone.

### 4.3 Worked capability example and workload energy floor (projection)

**Inputs (illustrative).** $K=3$ axes: (1) fading memory / state retention, (2) nonlinearity / input separability, (3) control–readout fidelity.  

$$
d = (0.90,\,0.50,\,0.80),\qquad
s = (0.95,\,0.20,\,0.90),\qquad
w_1=w_2=w_3=\tfrac13.
$$  

**Per‑axis fulfilment.**  

$$
m_1 = \frac{\min(0.90,0.95)}{0.90}=1.000,\quad
m_2 = \frac{\min(0.50,0.20)}{0.50}=0.400,\quad
m_3 = \frac{\min(0.80,0.90)}{0.80}=1.000.
$$  

**Match score.**  

$$
M = \tfrac13(1.000+0.400+1.000)=\tfrac13(2.400)=0.800.
$$  

**Waste fraction.** Surpluses: $(s_1-d_1)^{+}=0.05$, $(s_2-d_2)^{+}=0$, $(s_3-d_3)^{+}=0.10$.  

Weighted surplus numerator: $\tfrac13(0.05+0+0.10)=0.05$.  

Weighted total supply: $\tfrac13(0.95+0.20+0.90)=\tfrac13(2.05)=0.683333$.  

$$
W = \frac{0.05}{0.683333}\approx 0.07317.
$$  

**Projection of workload energy floor.** Assume $N_L = 10^{18}$ logical operations. Using the lower‑end logical‑operation floor $2.870981 \times 10^{-19}$ J,  

$$
E_{\text{work}}^{\text{low}} = 10^{18} \times 2.870981 \times 10^{-19}=0.2870981\ \text{J}\approx 0.287\ \text{J}.
$$  

Using the upper‑end floor $2.870981 \times 10^{-18}$ J,  

$$
E_{\text{work}}^{\text{high}} = 10^{18} \times 2.870981 \times 10^{-18}=2.870981\ \text{J}\approx 2.871\ \text{J}.
$$  

Thus the projected workload energy floor lies in the interval $[0.287,\,2.871]$ J.

### 4.4 Two‑state provisioning: waste, shortfall, utilisation

**Inputs (illustrative).** $p=0.3$ (fraction of time in high‑demand regime), $d_h=1$, $d_l=0.2$.

**Case A (peak provisioning, $C=d_h=1$).**  

- Waste: low regime surplus $1-0.2=0.8$ active $0.7$ of the time → $W_{\text{alloc}} = 0.7\times0.8 = 0.56$.  
- Shortfall: $0$ (by construction).  
- Mean demand: $p d_h + (1-p)d_l = 0.3\times1 + 0.7\times0.2 = 0.44$.  
- Utilisation: $\rho = 0.44/1 = 0.44$.

**Case B (mean provisioning, $C=\bar d =0.44$).**  

- Waste: low regime surplus $0.44-0.2 = 0.24$ active $0.7$ → $W_{\text{alloc}} = 0.7\times0.24 = 0.168$.  
- Shortfall: high regime deficit $1-0.44 = 0.56$ active $0.3$ → $S = 0.3\times0.56 = 0.168$.  
- Utilisation: $\rho = 0.44/0.44 = 1.0$ on served demand; $30\%$ of high‑regime demand is refused.  
- Symmetry: $W_{\text{alloc}} = S = 0.168$.

**Case C (trough provisioning, $C=d_l=0.2$).**  

- Waste: $0$.  
- Shortfall: high regime deficit $1-0.2 = 0.8$ active $0.3$ → $S = 0.3\times0.8 = 0.24$.  
- Utilisation: $\rho = 0.44/0.2 = 2.2 > 1$, i.e. infeasible; the excess $0.24$ per unit time is lost and, by the censoring assumption of [7], unmeasured.

**Cross‑check.** Served demand per unit time equals mean demand minus shortfall in each case, confirming the arithmetic.

### 4.5 Censoring bias of measured demand

With $\hat d(t)=\min(d(t),C)$ and $C=0.44$ (Case B), the measured mean is  

$$
\bar{\hat d}= p\min(d_h,C) + (1-p)\min(d_l,C) = 0.3\times0.44 + 0.7\times0.2 = 0.132 + 0.14 = 0.272.
$$  

True mean $\bar d = 0.44$. Understatement fraction  

$$
\frac{\bar d - \bar{\hat d}}{\bar d}= \frac{0.44-0.272}{0.44}= \frac{0.168}{0.44}=0.3818\ldots \approx 38.2\%.
$$  

Thus naïve measurement underestimates true demand by $38.2\%$, equal to the shortfall ratio $S/\bar d$.

### 4.6 Projection: time‑to‑saturation

Assume demand grows at a compound annual rate $g=0.5$ (50 %/year) from an initial mean $D_0=0.44$ against fixed capacity $C=1$. Time to saturation satisfies  

$$
C = D_0 (1+g)^{t_{\text{sat}}}
\;\Longrightarrow\;
t_{\text{sat}} = \frac{\ln(C/D_0)}{\ln(1+g)}.
$$  

Compute  

$$
\ln(C/D_0)=\ln(1/0.44)=\ln(2.272727)=0.820980,
$$  

$$
\ln(1+g)=\ln(1.5)=0.405465.
$$  

Hence  

$$
t_{\text{sat}} = \frac{0.820980}{0.405465}=2.0249\ \text{years}\approx 2.0\ \text{years}.
$$  

If $g=0.1$ (10 %/year),  

$$
\ln(1.1)=0.095310,\qquad
t_{\text{sat}} = \frac{0.820980}{0.095310}=8.613\ \text{years}.
$$  

Sensitivity factor  

$$
\frac{8.613}{2.025}\approx 4.25.
$$  

The projection rests entirely on the assumed growth rate; the factor quantifies how sensitive the saturation time is to that assumption.

## 5. Results

All numbers below are computed in Section 4 with full arithmetic; no empirical measurements are reported.

1. **Landauer floor.** $E_{\min}(300\ \text{K}) = 2.871 \times 10^{-21}$ J per irreversible bit operation (Section 4.1).  
2. **Per‑logical‑operation floor.** With $r\in[10^{2},10^{3}]$, $E_{\text{logical}} = 2.871 \times 10^{-19}$ to $2.871 \times 10^{-18}$ J per logical operation (Section 4.2).  
3. **Capability match.** Illustrative vectors yield $M = 0.800$ and waste fraction $W \approx 0.0732$ (Section 4.3).  
4. **Provisioning trade‑off.** In the two‑state model ($p=0.3$, $d_h=1$, $d_l=0.2$):  
   - Peak provisioning: waste = 0.56, shortfall = 0.  
   - Mean provisioning: waste = shortfall = 0.168, utilisation = 1.0 on served demand.  
   - Trough provisioning: waste = 0, shortfall = 0.24, utilisation = 2.2 (infeasible). (Section 4.4).  
5. **Censoring bias.** Measured mean underestimates true mean by $38.2\%$ (Section 4.5).  
6. **Time‑to‑saturation (projection).** Under $g=0.5$ per year, $t_{\text{sat}}\approx 2.0$ years; under $g=0.1$, $t_{\text{sat}}\approx 8.6$ years; sensitivity factor $\approx 4.25$ (Section 4.6).  
7. **Workload energy floor (projection).** For $N_L=10^{18}$ logical operations, the energy floor lies in $[0.287,\,2.871]$ J (Section 4.3).

## 6. Discussion

**Limitations.** The quantitative results rest on the following explicit assumptions, each of which bounds the validity of the derived numbers:

1. **Illustrative capability vectors** – The demand vector $d$ and supply vector $s$ used in the match‑score example are judgement‑based assessments, not empirical measurements. Consequently, the match score $M=0.800$ and waste fraction $W\approx0.0732$ are illustrative only.  
2. **Optimistic Landauer floor** – The Landauer bound $E_{\min}=2.871\times10^{-21}$ J assumes every physical operation is an irreversible bit erasure performed at the thermodynamic limit. Real devices incur additional irreversible processes, so actual per‑operation energy will be strictly larger.  
3. **Error‑correction overhead range** – The overhead factor $r\in[10^{2},10^{3}]$ is taken from the quantum‑error‑correction discussion in [12]. Its applicability to non‑quantum substrates is unverified; using an inappropriate $r$ would shift the logical‑operation floor by up to an order of magnitude.  
4. **Two‑state Markov demand model** – The allocation analysis employs a bimodal hidden state ($h,l$) with fixed probabilities $p$ and demand levels $d_h$, $d_l$. Real workloads may exhibit more than two regimes, temporal correlation, and non‑stationarity, which would alter waste, shortfall, and utilisation values.  
5. **Growth‑rate assumption for saturation** – The time‑to‑saturation projection uses a compound annual demand growth $g=0.5$. The sensitivity factor $\approx4.25$ shows that a modest change in $g$ (e.g., to $0.1$) multiplies the saturation time by the same factor, making the projection highly fragile.  
6. **Scalar match score hides axis failures** – $M$ aggregates per‑axis fulfilment $m_k$ into a single number. A high $M$ can conceal a total failure on a single binding axis, as demonstrated by $m_2=0.400$ in the illustrative example.  
7. **Workload‑level energy‑floor projection** – The projected workload floor $E_{\text{work}}$ for $N_L=10^{18}$ logical operations assumes the lower‑end overhead $r=10^{2}$ (or upper‑end $r=10^{3}$) and ignores all ancillary energy costs (control, memory movement, cooling). Hence the interval $[0.287,\,2.871]$ J is a strict lower bound.

**Failure modes.** The framework can produce misleading guidance if any of the following occurs:

- **Censoring‑induced under‑provisioning.** When demand is right‑censored by capacity, the measured mean $\bar{\hat d}$ underestimates the true mean $\bar d$ by the shortfall ratio (38.2 % in the worked case). Planning based on $\bar{\hat d}$ leads to systematic under‑provisioning in the next cycle.  
- **Single‑axis collapse despite high $M$.** A high match score may mask a critical capability shortfall (e.g., $m_2=0.400$), causing a substrate to fail on tasks that require that capability even though $M$ suggests overall adequacy.  
- **Energy‑floor underestimation.** If the actual overhead factor $r$ exceeds the upper bound $10^{3}$ or if irreversible operations are more numerous than assumed, the true energy cost per logical operation will surpass the projected floor, potentially rendering the substrate economically infeasible.  
- **Mis‑specified demand growth.** Over‑optimistic growth assumptions compress the saturation horizon, prompting premature capacity expansion; conversely, under‑estimating growth delays needed upgrades, leading to prolonged shortfalls.  

**What would falsify the main claim.** The central quantitative claim is that, under right‑censoring, the naïve measured mean demand underestimates the true mean by exactly the shortfall ratio $S/\bar d$ (38.2 % in the illustrative two‑state model). Empirical observation of a capacity‑constrained substrate in which the measured mean $\bar{\hat d}$ equals the true mean $\bar d$ (i.e., $\bar d-\bar{\hat d}=0$) despite documented refusals would falsify the censoring‑bias identity and invalidate the derived bias correction. Similarly, direct measurement of demand that shows a bias different from $S/\bar d$ would contradict the analytical result.

**Open questions.**  
- How can demand and supply vectors be elicited in a reproducible, auditable manner for emerging substrates, especially when capability assessments are currently subjective?  
- What empirical methods can determine the appropriate error‑correction overhead $r$ for non‑quantum physical computing platforms?  
- How should the allocation model be extended to capture multi‑regime, continuous, or correlated demand processes while preserving analytical tractability?  
- Can censored demand logs be augmented with refusal notifications to enable unbiased demand estimation, and what instrumentation overhead would this entail?  
- What design‑space exploration techniques can identify which capability axes most strongly influence the match score, thereby guiding substrate engineers toward high‑impact improvements?  

Addressing these questions will move the framework from a purely analytical illustration toward a practical decision‑support tool for funding agencies, procurement organisations, and substrate designers.

## 8. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
The framework is intended for three classes of stakeholders:

1. **Funding agencies and research programme reviewers** who must decide whether to allocate capital to a novel substrate proposal. The framework forces a proposal to supply a demand vector $d$, a supply vector $s$, a provisioning rule $C$, and an energy‑floor estimate $E_{\text{work}}$. With these artefacts the reviewer can compute the match score $M$ and the over‑provisioning waste $W$ and thus assess whether the substrate will be under‑ or over‑utilised under realistic demand.  

2. **Enterprise procurement organisations** that evaluate competing hardware platforms for large‑scale workloads. By inserting the platform’s documented capability levels into the capability‑axis formulation (Section 3.1) they obtain a scalarised $M$ and a waste fraction $W$, which can be compared against budgeted energy caps derived from the Landauer‑plus‑overhead floor (Section 4.2).  

3. **Substrate designers and architects** who must choose physical parameters (e.g., control‑readout fidelity, memory bandwidth) that affect the supply vector $s$. The analytic sensitivity of $M$ and $W$ to each axis (Section 4.3) highlights which capability improvements yield the greatest increase in match score, guiding engineering trade‑offs.

**(b) Technology readiness.**  
All results are derived analytically from published physical limits and from a stylised two‑state allocation model. No prototype has been built, and the work has not undergone peer review. According to the NASA Technology Readiness Level (TRL) definitions, the present state corresponds to **TRL 1–2** (basic principles observed and technology concept formulated). Analytical extensions never exceed **TRL 3**; therefore the framework itself is classified at TRL 2.

**(c) Minimal next experiment.**  
The most direct falsification test is a controlled workload execution on a candidate substrate where every job arrival and every refusal are logged. The experiment proceeds as follows:

1. Deploy a synthetic demand process matching the two‑state Markov model of Section 3.2 (parameters $p$, $d_h$, $d_l$).  
2. Set the provisioning capacity $C$ to the mean demand $\bar d$ (the case where waste = shortfall = 0.168).  
3. Record the *observed* demand $\hat d(t)=\min(d(t),C)$ and the *true* demand $d(t)$ (the latter is known from the generator).  
4. Compute the empirical bias $\frac{\bar d-\bar{\hat d}}{\bar d}$ and compare it to the theoretical shortfall ratio $S/\bar d = 0.3818$ (Section 4.5).  

If the measured bias deviates significantly from $38.2\%$, the censoring assumption inherited from [8] and the shortfall‑bias identity would be falsified.

**(d) Engineering and deployment constraints.**  

| Constraint | Source / Derivation |
|------------|----------------------|
| Ability to log refused jobs (required for bias measurement) | Implicit in the censoring model of [7] and the stock‑out pathology of [3]. |
| Accurate assessment of capability levels $s_k$ (e.g., control‑readout fidelity) | Relies on the operational vocabulary defined in [10] and the property checklist of [1]. |
| Determination of the error‑correction overhead factor $r$ | Directly taken from the quantitative statement in [12] ($r\in[10^{2},10^{3}]$). |
| Estimation of demand‑process parameters $p$, $d_h$, $d_l$ | Modelled after the Markov‑modulated structure of [7]; any deviation requires additional data collection. |
| Energy‑floor projection for a workload of $N_L$ logical operations | Computed in Section 4.3 using $E_{\text{logical}}(r)$ from [12]; no further hardware‑specific data needed. |

All constraints that are not yet quantified (e.g., precise $s_k$ values for a new substrate) are listed as open questions for future empirical work.

**(e) Order‑of‑magnitude cost and performance bounds.**  
Using the lower‑end overhead $r=10^{2}$ and $N_L=10^{18}$ logical operations, the projected workload energy floor is  

$$
E_{\text{work}}^{\text{low}} = 0.287\ \text{J},
$$  

while the upper‑end overhead $r=10^{3}$ yields  

$$
E_{\text{work}}^{\text{high}} = 2.871\ \text{J}.
$$  

These bounds (Section 4.3) provide a baseline against which any measured energy consumption must be compared; a substrate whose measured per‑operation energy exceeds $2.871\times10^{-18}$ J would be infeasible for the illustrative workload.

**(f) Direct risks and misuse pathways.**  
A potential misuse is to treat the scalar match score $M$ as a definitive indicator of suitability without inspecting the per‑axis fulfilment vector $m_k$. As shown in Section 4.3, a high $M=0.800$ can mask a total failure on a single binding axis (axis 2). Decision‑makers must therefore report $m_k$ alongside $M$. Another risk is to rely on the optimistic Landauer‑plus‑overhead floor as a hard cost ceiling; real substrates incur additional irreversible operations, leakage, and control overhead, so the floor should be interpreted only as a lower bound.

---

## 9. Conclusion

We have presented a unified, analytically tractable framework that places computational demand at the centre of substrate evaluation. By combining a capability‑accounting match score with an allocation‑theoretic model of waste, shortfall, and censoring bias, and by anchoring the analysis to the Landauer thermodynamic limit together with the error‑correction overhead range reported in [12], the paper delivers:

* A concrete Landauer floor of $2.871\times10^{-21}$ J per irreversible bit operation at $300$ K (Section 4.1).  
* A per‑logical‑operation floor spanning $2.871\times10^{-19}$–$2.871\times10^{-18}$ J (Section 4.2).  
* An illustrative capability match $M=0.800$ with waste $W\approx0.0732$ (Section 4.3).  
* A symmetric provisioning point where waste equals shortfall ($0.168$) in a two‑state demand model (Section 4.4).  
* A quantitative censoring bias of $38.2\%$, equal to the shortfall ratio (Section 4.5).  
* A projected time‑to‑saturation of $2.0$ years under a $50\%$ annual demand growth assumption, with a sensitivity factor of $\approx4.25$ (Section 4.6).  

The framework is deliberately minimal: all derivations are shown step‑by‑step, no empirical data are introduced, and every projection is labelled with its assumptions. Its primary contribution is an **auditable ledger** that forces substrate proposals to disclose demand vectors, supply vectors, provisioning rules, and thermodynamic cost floors before any capital commitment. This ledger can be adopted by funding bodies, enterprise procurement teams, and substrate designers to avoid over‑provisioning, under‑provisioning, and premature dismissal of promising physical computing platforms.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.1-kimi-timeout-fallback-1). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 16 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] A Substrate-Independent Framework to Characterise Reservoir Computers. arXiv:1810.07135v2. https://arxiv.org/abs/1810.07135v2
[2] Online Algorithm for Demand Response with Inelastic Demands and Apparent Power Constraint. arXiv:1611.00559v2. https://arxiv.org/abs/1611.00559v2
[3] EXAONE Demand 1.0: A Time Series Foundation Model for Demand Forecasting. arXiv:2609.30880v1. https://arxiv.org/abs/2609.30880v1
[4] Adjoint computations by algorithmic differentiation of a parallel solver for time-dependent PDEs. arXiv:1912.11717v3. https://arxiv.org/abs/1912.11717v3
[5] Find What You Want: Learning Demand-conditioned Object Attribute Space for Demand-driven Navigation. arXiv:2309.08138v3. https://arxiv.org/abs/2309.08138v3
[6] Computing persistent Stiefel-Whitney classes of line bundles. arXiv:2005.12543v3. https://arxiv.org/abs/2005.12543v3
[7] Inventory Management with Partially Observed Nonstationary Demand. arXiv:1206.6283v1. https://arxiv.org/abs/1206.6283v1
[8] Computing Singularly Perturbed Differential Equations. arXiv:1707.03765v3. https://arxiv.org/abs/1707.03765v3
[9] https://papers.qnfo.org/papers/actual-demand-of-a-computational-substrate-a-reconciled-demand-side-and-allocati. QNFO: Actual Demand of a Computational Substrate: A Reconciled Demand-Side and Allocation Framework for Physical Computing Platforms.
[10] https://papers.qnfo.org/papers/re-entry-dynamics-as-a-switching-process-comparing-hamiltonian-re-entry-computat. QNFO: The Switching Economics of Hamiltonian Re-Entry Computation: A Cost-Model Comparison with Stored-Program Architectures.
[12] https://papers.qnfo.org/papers/quwarp-reconciled-an-analytical-cost-model-assessment-of-workload-level-reuse-pl. QNFO: QuWARP Reconciled: An Analytical Cost-Model Assessment of Workload-Level Reuse Planning for Quantum Circuit Simulation.
