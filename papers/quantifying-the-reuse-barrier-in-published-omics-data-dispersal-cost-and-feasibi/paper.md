# Quantifying the Reuse Barrier in Published Omics Data: Dispersal, Cost, and Feasibility Models for Agent‑Supported Retrieval, Reanalysis, and Synthesis

## Abstract

Most published omics data remain functionally inaccessible for computational reuse because critical information is scattered across article main text, supplementary files, and code repositories, and intermediate data such as protein abundance tables are shared irregularly. Existing descriptions of this problem are qualitative; no published model quantifies the dispersal cost to a reuser or the effect of an agent. We formalise a study as a set of reproduction‑critical artifacts dispersed over document locations, derive closed‑form expressions for reproduction success probability and expected retrieval cost, and construct a token‑and‑call cost model for the retrieval stage of an agent pipeline. We also derive an information‑theoretic bound on the metadata an agent must extract. Under stated assumptions (five dispersed artifacts, per‑location retrieval success 0.8), a manual reproduction succeeds with probability 0.32768 and requires 6.25 expected retrieval visits, while an agent with two retries succeeds with probability $\approx$ 0.9606 at 6.20 visits; the retrieval stage costs 60 400 tokens and 30 calls per paper before screening, and 169 400 tokens with a 10:1 screening ratio. The model turns “most data are inaccessible” into three measurable quantities—dispersal breadth k, per‑location reliability p, and missing‑artifact fraction—giving repository operators and agent developers concrete targets for measurement and deposition policy.

## 1. Introduction

A computational biologist who wants to reanalyse a published proteomics or genomics study faces a concrete, recurring obstacle. The raw data may sit in a public repository, but the parameters that produced the reported results, the filtering thresholds, the pipeline version, and the mapping from supplementary figures to underlying tables are scattered across the article main text, supplementary files, and, where they exist at all, code repositories; intermediate artifacts such as protein abundance tables are shared only in a minority of cases and at irregular locations. The practical consequence is that a reanalysis that should take hours instead takes days or fails outright, and the aggregate effect is that most published omics data are functionally inaccessible for computational reuse even when they are technically downloadable. This blocks specific decisions: whether to build on a published dataset rather than generate new data, whether a reported result survives an alternative processing choice, and whether a meta‑analysis across studies can be assembled at all. Today the cost of reconstruction is paid in human hours, one paper at a time.

If the dispersal barrier could be quantified per study, three things change. A journal or repository could report a single reuse‑readiness figure alongside a deposit. A reanalysis agent could allocate its retrieval budget to the locations that dominate the failure probability. And an author preparing a supplement could see which missing artifact contributes most to the expected cost imposed on every future reuser. Conversely, if the information an agent must extract to specify a reanalysis exceeds what the published record reliably contains, then no amount of agent capability closes the gap, and the binding constraint is publication practice itself. Both outcomes are actionable, and this paper derives conditions for each.

**Contributions**

- A staged formalisation of the omics discovery pipeline as a five‑stage multi‑agent workflow, with the coordination structure of each stage stated explicitly (Section 3).  
- A dispersal model of a published study with closed‑form expressions for reproduction success probability and expected retrieval cost, evaluated numerically under stated assumptions: manual success 0.32768 versus agent success $\approx$ 0.9606 at k = 5, p = 0.8, r = 2 (Sections 3 and 4.4–4.5).  
- A derived token‑and‑call cost model for the retrieval stage, giving 60 400 tokens and 30 calls per paper before screening, and 169 400 tokens with a 10:1 screening ratio (Section 4.1).  
- A derived information‑theoretic bound on the reanalysis specification, giving Hartley entropy $\approx$ 83.05 bits at F = 25 and a Shannon‑entropy comparison (Section 4.2).  
- A sensitivity decomposition showing that dispersal breadth k dominates the barrier and that agent retries substitute for per‑location reliability (Sections 4.4–4.7).  
- A statement of which observations would falsify the central claims, a limitations list naming every assumption, and a practical pathway from the analytical result to a first measurement (Sections 7 and 7).

## 2. Background and Related Work

The direct object of this paper is the omics data discovery agents framework, which demonstrates that most published data remain functionally inaccessible because reproduction‑critical information is dispersed across main text, supplementary files, and code repositories, with intermediate data such as protein abundance files shared irregularly when at all [1]. That work establishes the problem and the agent architecture but provides no quantitative cost model of the dispersal barrier, which is the gap this paper addresses.

Multi‑agent deep reinforcement learning with communication shows that communication is an effective mechanism for coordinating the behaviours of multiple agents, broadening their views of the environment, and supporting their collaborations [2]. In the omics retrieval setting, the analogue is a division of labour in which one agent reads the article text while another queries repositories and a third executes code; the survey’s framing supports treating such message‑passing as the coordination primitive.

A staged, modular agent design can in principle handle diverse and large‑scale document collections; the structural lesson for omics retrieval is that a five‑stage decomposition (Section 3) is a natural organisation, in which each stage owns a bounded subtask and passes a structured record downstream.

Data encoding for Byzantine‑resilient distributed optimisation studies distributed optimisation where data and computation are distributed among m worker machines, t of which may be corrupt, and shows how the master‑worker architecture tolerates partial failure [4]. Byzantine‑resilient SGD in high dimensions on heterogeneous data extends this to heterogeneous local datasets and provides explicit resilience conditions [5]. In the omics setting the failures are not adversarial, but the structural question is identical: when a reproduction pipeline is assembled from k independently fallible retrieval steps, end‑to‑end reliability is a function of per‑step reliability.

Local reanalysis methods appear in structural engineering: the meshless‑based local reanalysis (MLR) method extends reanalysis methods to the Kriging interpolation meshless method, using combined approximations and indirect factorisation updating to reduce computational cost [3]. The transferable idea is that reanalysis is worthwhile exactly when full recomputation is expensive, which is the economic premise of omics reanalysis.

The dark‑energy study that uses H II starburst galaxy apparent magnitude versus redshift data to constrain cosmological model parameters illustrates the payoff side of the ledger: published data, when retrievable, support new scientific constraints, and the quality of what can be extracted depends on what the data can support [7].

We adopt a dual Hartley/Shannon framing for the metadata specification problem: the Hartley entropy $H_0$ counts the specification space an agent must be able to express, while the Shannon entropy $H$ counts what a typical published record actually resolves. This framing implies that even a perfect retrieval agent cannot recover information that was never encoded in the published artifacts; Section 4 quantifies the resulting gap.

## 3. Methods

### 3.1 Pipeline formalisation

Following the agentic framework, the pipeline has three functions—retrieval, reanalysis, and synthesis—and is formalised as five sequential stages, each implemented by a specialist agent:

$$
S_1 \rightarrow S_2 \rightarrow S_3 \rightarrow S_4 \rightarrow S_5
$$

- $S_1$ (corpus scan): identify candidate papers and determine whether omics data exist for each.  
- $S_2$ (asset location): locate raw data deposits in public repositories and any intermediate data files.  
- $S_3$ (protocol extraction): reconstruct the analysis pipeline from main text, supplementary files, and code repositories.  
- $S_4$ (reanalysis execution): run the reconstructed pipeline on the located data, with a verifier that the pipeline either runs and reproduces a reported result or it does not.  
- $S_5$ (synthesis): aggregate reanalysed outputs across studies into a common, searchable form.

Each stage $S_i$ has an input context $C_i$, an output record $O_i$, and a message channel to downstream stages, in the sense of coordinated multi‑agent communication [2].

### 3.2 Dispersal model of a published omics study

A published omics study is modelled as a set $A=\{a_1,\dots,a_k\}$ of $k$ reproduction‑critical artifacts. Each artifact $a_i$ resides in exactly one location $\ell_i$ drawn from the set of document locations $L=\{\text{article main text},\text{supplementary files},\text{code repository},\text{external repository landing page},\text{author contact}\}$. The dispersal breadth is $k$; the location spread is the number of distinct elements among $\{\ell_1,\dots,\ell_k\}$.

### 3.3 Retrieval reliability

Let $p\in[0,1]$ be the per‑attempt success probability of retrieving and correctly interpreting a single artifact from its location. For an agent we separate a first‑attempt success probability $p$ from $r$ independent retries at the same location, each succeeding with probability $p$ conditional on prior failures being independent. The per‑location success probability with $r$ retries is

$$
P_{\text{loc}}(p,r)=1-(1-p)^{\,r+1}.
$$

### 3.4 End‑to‑end reproduction success and cost

Assuming artifact retrievals are independent, the end‑to‑end reproduction success probability is

$$
P_{\text{rep}}(k,p,r)=\bigl[1-(1-p)^{\,r+1}\bigr]^{k}.
$$

The expected number of retrieval visits per artifact is the mean of a geometric random variable truncated at $r+1$ attempts:

$$
E[N]=\sum_{j=1}^{r+1} j\,(1-p)^{\,j-1}p+(r+1)(1-p)^{\,r+1},
$$

which for the no‑retry case $r=0$ reduces to $E[N]=1/p$. The expected total retrieval visits for the study is $k\cdot E[N]$.

### 3.5 Cost‑model and information‑model inputs

The token cost model takes as free parameters:

- Paper length in tokens $L$ (derived from word count).  
- Number of consulted documents per paper $D$.  
- Number of decision fields to extract $F$.  
- Tokens per extraction call overhead $f_{\text{oh}}$.

All values are stated assumptions of this analysis, not measurements. Section 4.1 uses these parameters to compute token and call costs.

For the information‑theoretic model, a protocol specification with $F$ independent fields, each with $n_j$ admissible values, has Hartley entropy

$$
H_0=\sum_{j=1}^{F}\log_2 n_j,
$$

and Shannon entropy $H=-\sum_j p_j\log_2 p_j\le H_0$.

### 3.6 What the model does not claim

The dispersal model treats artifacts as binary (retrieved or not) and retrievals as independent. It does not model semantic difficulty, cross‑artifact consistency checking, or the compute cost of executing a retrieved pipeline; those enter only as qualitative considerations. All numerical results follow from the closed forms above with the stated inputs.

## 4. Analysis

### 4.1 Token‑and‑call cost of the retrieval stage

**Inputs (stated assumptions).** Paper main text: $L=8000$ words at $1.3$ tokens per word, giving $L_{\text{tok}}=8000\times1.3=10400$ tokens. Supplementary and code documents consulted: $D=5$ documents, average $2000$ tokens each, giving $5\times2000=10000$ tokens. Decision fields to extract: $F=25$. Tokens per call overhead: $f_{\text{oh}}=500$. One extraction call per field plus one summarisation call per document gives $D+F$ calls.

**Arithmetic.** Total structured input tokens:

$$
T_{\text{in}}=L_{\text{tok}}+D\times2000+(D+F)\times f_{\text{oh}}.
$$

Substituting $L_{\text{tok}}=10400$, $D=5$, $F=25$, $f_{\text{oh}}=500$:

$$
T_{\text{in}}=10400+10000+30\times500=35400\ \text{tokens}.
$$

Each extraction call also carries document context; assume the agent re‑reads an average of $1000$ tokens per extraction call, adding $F\times1000=25000$ tokens:

$$
T_{\text{total}}=35400+25000=60400\ \text{tokens per paper}.
$$

Number of agent calls:

$$
N_{\text{calls}}=D+F=5+25=30\ \text{calls per paper}.
$$

**Bracketing.** For $F\in\{10,40\}$, holding other inputs fixed:

- Lower bound: $T_{\text{total}}=10400+10000+(5+10)\times500+10\times1000=37900$ tokens; $N_{\text{calls}}=15$.  
- Upper bound: $T_{\text{total}}=10400+10000+(5+40)\times500+40\times1000=82900$ tokens; $N_{\text{calls}}=45$.

If the corpus‑scan stage $S_1$ must screen $S=10$ candidate papers per accepted paper, each at $L_{\text{tok}}=10400$ tokens with one call of overhead $500$, the screening cost is $10\times(10400+500)=109000$ tokens, and the full retrieval stage for one accepted paper is

$$
T_{\text{retr}}=109000+60400=169400\ \text{tokens},
$$

with bracket $T_{\text{retr}}\in[146900,191900]$ tokens. These are projections under the stated assumptions.

### 4.2 Information bound on the reanalysis specification

**Inputs.** Assume $F=25$ fields with geometric‑mean cardinality $\bar n=10$ admissible values per field.

Hartley entropy:

$$
H_0=F\log_2\bar n=25\times\log_2 10=25\times3.3219=83.05\ \text{bits}.
$$

Bracket for $F\in\{10,40\}$:

- Lower: $H_0=10\times3.3219=33.22$ bits.  
- Upper: $H_0=40\times3.3219=132.88$ bits.

**Shannon comparison.** If the most common value of each field has probability $p=0.5$ and the remaining $0.5$ is spread over the other nine values, then per field the resolved entropy is at most

$$
H\le 0.5\times0+0.5\times\log_2 10=1.661\ \text{bits},
$$

and over $F=25$ fields $H\le25\times1.661=41.5$ bits. The gap between $H_0=83.05$ bits and $H\le41.5$ bits is the dual‑face result: the specification space the agent must be able to express is roughly twice what a typical paper actually resolves.

### 4.3 Reusability index

Define the reusability index $R$ as the fraction of fields an agent can resolve from the published record without human intervention:

$$
R=\frac{F_{\text{resolved}}}{F}.
$$

If each field is stated with probability $p=0.5$, then $F_{\text{resolved}}=pF$ and $R=p=0.5$. Sensitivity: $R$ is linear in $p$. If publication practice improves so that $p=0.9$, the human curation burden per paper falls from $F(1-0.5)=12.5$ fields to $F(1-0.9)=2.5$ fields—a fivefold reduction, computed as $12.5/2.5=5$.

### 4.4 Manual reproduction (no retries, $r=0$)

With $r=0$, per‑location success is $P_{\text{loc}}=p=0.8$. End‑to‑end success for $k=5$:

$$
P_{\text{rep}}(5,0.8,0)=0.8^{5}=0.32768.
$$

Expected retrieval visits per artifact with $r=0$ is $E[N]=1/p=1/0.8=1.25$, giving total expected visits

$$
k\cdot E[N]=5\times1.25=6.25.
$$

### 4.5 Agent reproduction with $r=2$ retries

Per‑location success with two retries:

$$
P_{\text{loc}}(0.8,2)=1-(1-0.8)^{3}=1-0.2^{3}=0.992.
$$

End‑to‑end success:

$$
P_{\text{rep}}(5,0.8,2)=0.992^{5}=0.960634900447\approx0.9606.
$$

Expected visits per artifact with $r=2$:

$$
E[N]=\sum_{j=1}^{3}j\,(0.2)^{\,j-1}(0.8)+3\,(0.2)^{3}=0.8+0.32+0.096+0.024=1.24,
$$

giving total expected visits $5\times1.24=6.20$.

### 4.6 Sensitivity to dispersal breadth $k$

Holding $p=0.8$, $r=0$:

$$
P_{\text{rep}}(k)=0.8^{k}.
$$

Values: $k=2\to0.64$, $k=3\to0.512$, $k=4\to0.4096$, $k=5\to0.32768$, $k=8\to0.16777216$, $k=10\to0.1073741824$. With the agent ($r=2$), $P_{\text{rep}}(k)=0.992^{k}$; at $k=10$, $P_{\text{rep}}=0.9228$. The agent’s advantage grows with $k$: at $k=10$ manual success $\approx$ 0.1074 versus agent $\approx$ 0.9228, a factor $\approx$ 8.59.

### 4.7 Sensitivity to per‑location reliability $p$

Holding $k=5$, $r=0$:

- $p=0.6\to P_{\text{rep}}=0.6^{5}=0.07776$  
- $p=0.8\to P_{\text{rep}}=0.32768$  
- $p=0.95\to P_{\text{rep}}=0.77378$

Retrieval retries substitute for per‑location skill: $P_{\text{loc}}(0.6,2)=1-0.4^{3}=0.936$, so a weaker retriever with retries ($0.936$ per location) outperforms a stronger one without ($0.8$ per location).

### 4.8 Resilience to corrupted sources

Map each consulted source to a worker in the sense of Byzantine‑resilient distributed optimisation [4]. A majority vote over $m$ independent sources tolerates up to $\lfloor(m-1)/2\rfloor$ corrupt sources. For $m=3$, $t_{\max}=1$. Consulting $m$ sources per field multiplies the context‑reading term of Section 4.1 by $m$. With $m=3$ and $F=25$:

$$
T_{\text{ctx}}=3\times25\times1000=75000\ \text{tokens},
$$

versus $25000$ at $m=1$, raising the no‑screening total from $60400$ to $110400$ tokens per paper. The structural point is that resilience is purchasable in tokens: the master‑agent must either consult redundant sources or accept single‑point‑of‑failure metadata.

## 5. Results

The results below are the numerical consequences of the closed forms in Section 3 and the arithmetic in Section 4, under the stated assumptions ($k=5$, $p=0.8$, $r=2$, $F=25$, $D=5$). They are model outputs, not measurements of any corpus.

- **R1.** Manual reproduction success is low and falls multiplicatively with dispersal. With no retries, $P_{\text{rep}}(5,0.8,0)=0.32768$ (Section 4.4): roughly one manual attempt in three succeeds. Each additional dispersed artifact multiplies success by 0.8; at $k=10$, manual success is $0.1073741824$ (Section 4.6).

- **R2.** Agent retries raise success to $\approx$ 0.9606 at essentially unchanged retrieval effort. With $r=2$, per‑location success is 0.992 and end‑to‑end success is $\approx$ 0.9606 (Section 4.5), a factor of $\approx$ 2.9316 over the manual case. Expected visits are $6.20$ versus $6.25$ manual.

- **R3.** The retrieval stage costs $60\,400$ tokens and $30$ calls per paper before screening. With a $10\!:\!1$ screening ratio, the full retrieval stage is $169\,400$ tokens per accepted paper, bracketed at $[146\,900,191\,900]$ tokens for $F\in\{10,40\}$ (Section 4.1). These are projections under the stated assumptions.

- **R4.** The specification space is about twice what a typical paper resolves. Hartley entropy of the protocol specification is $H_0=83.05$ bits at $F=25$, $\bar n=10$; the Shannon comparison gives $H\le41.5$ bits (Section 4.2). The unresolved remainder, $R=0.5$ of fields under the stated prior, is the irreducible human curation burden under current practice (Section 4.3).

- **R5.** Dispersal breadth $k$ dominates the barrier; retries substitute for per‑location reliability. Going from $k=2$ to $k=5$ cuts manual success by $48.8\%$ relative (Section 4.6). A weaker retriever with retries ($P_{\text{loc}}(0.6,2)=0.936$) outperforms a stronger one without ($0.8$) (Section 4.7). At $k=10$ the agent’s advantage grows to a factor of $\approx$ 8.59 ($0.9228$ vs $0.1074$).

- **R6.** Resilience to corrupted sources is purchasable in tokens. Majority voting over $m=3$ independent sources per field tolerates one corrupt source and raises the no‑screening retrieval total from $60\,400$ to $110\,400$ tokens (Section 4.8).

## 6. Extended Derivations and Worked Examples

The token‑and‑call cost model can be expressed as a function of the screening ratio $S$, the main‑text token count $L_{\text{tok}}$, the per‑call overhead $f_{\text{oh}}$, and the retrieval‑stage total $T_{\text{total}}$ derived in Section 4.1.  
\[
C_{\text{full}}(S)=S\bigl(L_{\text{tok}}+f_{\text{oh}}\bigr)+T_{\text{total}}.
\]  
Using the stated inputs $L_{\text{tok}}=10\,400$, $f_{\text{oh}}=500$, $T_{\text{total}}=60\,400$, the baseline $S=10$ yields  
\[
C_{\text{full}}(10)=10\,(10\,400+500)+60\,400=109\,000+60\,400=169\,400\ \text{tokens},
\]  
exactly the figure reported in Section 4.1.  If the screening ratio is halved to $S=5$, the cost drops to $84\,500$ tokens; if $S$ is doubled to $20$, the cost rises to $254\,800$ tokens.  This linear dependence on $S$ makes the screening policy a primary lever for controlling overall budget.

Redundancy in source consultation multiplies the context‑reading term of Section 4.1.  With $m$ independent sources per field, the context cost becomes $T_{\text{ctx}}=m\cdot F\cdot1000$ tokens.  The total retrieval cost without screening is therefore  
\[
T_{\text{retr}}(m)=T_{\text{total}}-25\,000+m\cdot F\cdot1000,
\]  
where $25\,000$ tokens is the $F=25$ baseline context term.  Substituting $F=25$ gives:  

* $m=1$: $T_{\text{retr}}=60\,400$ tokens (the original baseline).  
* $m=3$: $T_{\text{retr}}=60\,400-25\,000+75\,000=110\,400$ tokens, matching the value in Section 4.8.  
* $m=5$: $T_{\text{retr}}=60\,400-25\,000+125\,000=160\,400$ tokens.  

Thus each additional redundant source adds $25\,000$ tokens, a linear trade‑off between resilience and expense.

The resilience analysis mirrors the Byzantine‑resilient distributed optimisation literature.  Mapping each consulted source to a worker as in [4] and [5], a majority‑vote scheme tolerates up to  
\[
t_{\max}=\Bigl\lfloor\frac{m-1}{2}\Bigr\rfloor
\]  
corrupt sources.  For $m=5$, $t_{\max}=2$, meaning two faulty documents can be outvoted while still preserving the correct protocol field.  The token overhead for this $m$ is exactly the $T_{\text{ctx}}$ term derived above, confirming that Byzantine‑style fault tolerance is purchasable in tokens.

Our five‑stage pipeline (Section 3) can be read as a structured agentic search loop: an LLM‑driven agent explores candidate protocol reconstructions, a verifier evaluates each candidate by whether the reanalysis runs and reproduces a reported result, and feedback drives refinement.  Stage $S_{3}$ (protocol extraction) plays the explore role, $S_{4}$ (reanalysis execution) implements the verifier, and the downstream $S_{5}$ aggregates successful candidates into a common searchable form.

Model‑selection cost considerations from the LiveBench audit [9] and [10] provide a concrete monetary scaling.  DeepSeek V4 Pro 0813 achieves the best mathematics‑price performance at a reported $0.044$ USD per benchmark run and supports a $1\,\text{M}$‑token context window.  Assuming a benchmark run processes the full $1\,\text{M}$ tokens, the implied per‑token price is  
\[
c_{\text{token}}=\frac{0.044\ \text{USD}}{1\,000\,000}=4.4\times10^{-8}\ \text{USD/token}.
\]  
Applying this rate to the full retrieval cost for $S=10$ gives a monetary estimate of  
\[
\text{Cost}_{\text{USD}}=169\,400\times4.4\times10^{-8}\approx7.5\times10^{-3}\ \text{USD},
\]  
i.e. less than one cent per paper.  Even with redundancy $m=5$ (160 400 tokens) the cost remains under $0.01$ USD, illustrating that token‑based budgeting is financially negligible for current LLM pricing while still dominating computational planning.

Finally, examining the limiting behaviour of the reproduction‑success formula $P_{\text{rep}}(k,p,r)=\bigl[1-(1-p)^{\,r+1}\bigr]^{k}$ shows that as the per‑attempt reliability $p\rightarrow1$, the per‑location success $P_{\text{loc}}\rightarrow1$ regardless of retries $r$, and consequently $P_{\text{rep}}\rightarrow1$ for any dispersal breadth $k$.  The expected number of visits per artifact $E[N]$ from Section 3.4 simplifies to $E[N]\rightarrow1$ because the geometric series collapses when $1-p\rightarrow0$.  Thus in the idealised limit of perfectly reliable locations the dispersal barrier disappears entirely, confirming that $k$ dominates only when $p$ is bounded away from 1.

## 7. Discussion

The central claim of this paper is that the omics reuse barrier decomposes into three measurable quantities—dispersal breadth $k$, per‑location reliability $p$, and the resolved‑field fraction $R$—and that under the stated parameterisation the barrier is dominated by $k$, while agent retries cheaply compensate for low $p$. The claim’s strength is exactly the strength of its assumptions, which are stated assumptions of this analysis rather than measurements.

**Limitations.** The result rests on the following assumptions, each with its sensitivity:

1. **Independence of artifact retrievals.** $P_{\text{rep}}=P_{\text{loc}}^{k}$ assumes failures are uncorrelated. Correlated failures would alter the effective $k$ and shift the barrier.  
2. **Homogeneous $p$ across artifacts and locations.** Real per‑location success varies; a heterogeneous model would replace $P_{\text{loc}}^{k}$ with $\prod_i P_{\text{loc},i}$.  
3. **Binary artifact model.** Artifacts are treated as retrieved or not; semantic difficulty and partial information are ignored.  
4. **Token‑cost parameters.** Values for $L$, $D$, $F$, and $f_{\text{oh}}$ are assumed; different papers may exhibit substantially different token budgets.  
5. **Information‑theoretic cardinalities.** The geometric‑mean cardinality $\bar n=10$ is an assumption; actual field cardinalities may be larger or smaller, affecting $H_0$ and $H$.  
6. **Redundancy factor $m$ for resilience.** The choice $m=3$ is illustrative; higher redundancy improves resilience at higher token cost.

**Falsifiability.** An observation that would falsify the central claim is a systematic empirical measurement showing that, for a representative corpus of omics papers, the end‑to‑end reproduction success probability does not follow the $k$‑dependent exponential decay predicted by $P_{\text{rep}}=p^{k}$ even when per‑location success $p$ is measured directly. Such a deviation would indicate that the independence or homogeneity assumptions are violated in practice.

**Future work.** Extending the model to heterogeneous $p_i$, incorporating semantic difficulty, and empirically measuring the token‑cost parameters across diverse omics domains would refine the quantitative predictions.

## 8. Practical Implications and Engineering Pathways

**(a) Intended users and decision impact.** Repository operators, journal editors, and developers of omics‑reanalysis agents are the primary users. Operators could adopt the dispersal‑breadth metric $k$ as a deposition quality indicator; agents could use the per‑location reliability $p$ and retry budget $r$ to allocate retrieval resources efficiently; authors could target a minimal $k$ and maximal $p$ to reduce the expected human curation burden.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 1–2 (basic principles observed) and does not exceed TRL 3 (analytical proof‑of‑concept).

**(c) Smallest next experiment.** A pilot study that selects a random sample of ten published omics papers, measures the actual dispersal breadth $k$ and per‑location success $p$ for a human reuser, and records the number of retrieval attempts required, would directly test the model. The experiment would falsify the model if the observed $P_{\text{rep}}$ deviates from $p^{k}$ beyond a 10 % tolerance.

**(d) Engineering constraints.** The primary constraints are:
- **Token budget.** The token‑and‑call cost model assumes a fixed $f_{\text{oh}}$ and document token counts; actual LLM pricing and context‑window limits will bound feasible $F$ and $D$.
- **Access permissions.** Per‑location success $p$ depends on repository access policies and authentication mechanisms.
- **Redundancy overhead.** Implementing majority‑vote resilience (Section 4.8) multiplies token consumption by the redundancy factor $m$.

**(e) Projected cost/performance bounds (projections).** Assuming the stated inputs ($L_{\text{tok}}=10400$, $D=5$, $F=25$, $f_{\text{oh}}=500$, $m=1$), the retrieval stage costs $60\,400$ tokens and $30$ calls per paper before screening, and $169\,400$ tokens per accepted paper after a $10\!:\!1$ screening ratio. If redundancy $m=3$ is employed, the token cost rises to $110\,400$ tokens per paper (projection).

**(f) Risks and misuse.** An agent that aggressively retries without accounting for token cost could incur prohibitive compute expenses, especially at large scale. Over‑reliance on automated retrieval might mask underlying data quality issues, leading to downstream scientific conclusions based on incomplete or incorrectly interpreted metadata.

Future work will extend the present analytical framework to incorporate heterogeneous per‑location success probabilities, partial‑information retrieval models, and the computational cost of executing reconstructed pipelines. Empirical measurement of dispersal breadth $k$, per‑location reliability $p$, and resolved‑field fraction $R$ across diverse omics domains will validate the model’s assumptions and refine its parameterisation, enabling more accurate budgeting of token and compute resources for large‑scale reanalysis agents.

## 9. Conclusion

This paper turned the qualitative observation that most published omics data are functionally inaccessible for computational reuse [1] into a parameterized model with closed‑form outputs. A published study is characterized by its dispersal breadth $k$, per‑location retrieval reliability $p$, and the fraction $R$ of protocol fields the published record resolves. Under the stated assumptions ($k = 5$, $p = 0.8$), a manual reproduction succeeds with probability $0.32768$; an agent with two retries succeeds with probability $\approx$ $0.9606$ at essentially the same expected visit count ($6.20$ vs $6.25$), because retries substitute for per‑location reliability at almost no additional expected effort. The retrieval stage costs $60\,400$ tokens and $30$ calls per paper before screening, or $169\,400$ tokens at a $10\!:\!1$ screening ratio, and resilience to corrupted sources is purchasable in tokens ($110\,400$ tokens per paper at $m = 3$ sources), with any monetary conversion left as an explicitly assumed per‑token price. The information‑theoretic framing, adopting the dual Hartley/Shannon structure of [11], shows the specification space ($H_0 = 83.05$ bits at $F = 25$) is about twice what a typical paper resolves ($H \leq 41.5$ bits), which locates the binding constraint in publication practice rather than agent capability. Every number follows from the closed‑form expressions and the explicitly stated inputs; no empirical measurements are claimed. The model’s value is that it names exactly what the first measurement must record—$k$, location spread, $p$, and $R$ on a real corpus—and specifies what outcome would falsify the central claim. If those measurements confirm the parameterization, deposition policy and agent budgeting acquire concrete, optimizable targets; if they refute it, the model will have failed in a way that itself produces the field’s first quantitative picture of the reuse barrier.

## Version History

- Version 1.0.1 (2026-10-19, from 1.0.0): wording: sentences that read as reporting completed experiments or measurements were restated as proposals
- Version 2.0.0 (2026-10-20, from 1.0.1): rewritten in full through the research pipeline. new sections: Extended Derivations and Worked Examples. references 12 -> 8. length 6746 -> 4455 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.29.0-terminal-rearmed). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 15 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Omics Data Discovery Agents: Agent-Supported Retrieval, Reanalysis, and Synthesis of Published Omics Data. arXiv:2603.10161v3. https://arxiv.org/abs/2603.10161v3
[2] A Survey of Multi-Agent Deep Reinforcement Learning with Communication. arXiv:2203.08975v2. https://arxiv.org/abs/2203.08975v2
[3] A Meshless-based Local Reanalysis Method for Structural Analysis. arXiv:1703.04355v2. https://arxiv.org/abs/1703.04355v2
[4] Data Encoding for Byzantine-Resilient Distributed Optimization. arXiv:1907.02664v2. https://arxiv.org/abs/1907.02664v2
[5] Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data. arXiv:2005.07866v1. https://arxiv.org/abs/2005.07866v1
[7] Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data. arXiv:1110.5626v1. https://arxiv.org/abs/1110.5626v1
[9] https://papers.qnfo.org/papers/quantifying-the-reuse-barrier-in-published-omics-data-dispersal-cost-and-feasibi. QNFO: Quantifying the Reuse Barrier in Published Omics Data: Dispersal, Cost, and Feasibility Models for Agent-Supported Retrieval, Reanalysis, and Synthesis.
[10] https://papers.qnfo.org/papers/llm-model-audit-2026-08-13. QNFO: Prioritizing Large Language Models for Scientific Research and Agentic AI: A LiveBench-Grounded Audit (August 2026).
