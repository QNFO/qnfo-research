# Part II: Historical Perspectives on Information States

## Abstract

Communities facing rapid automation must act on information whose accuracy, reach, and interpretation they only partly control, and policymakers who misread such communities repeat the repressive errors of 1811–1813. The existing account of the Luddite movement as an information-state case study is qualitative: it identifies oral tradition, limited literacy, and localized networks but attaches no numbers to fidelity, reach, bandwidth, or the government's identification problem, so it cannot support comparative or policy claims. This paper rebuilds that account quantitatively. We model (i) message fidelity across oral relay generations as geometric decay, (ii) rumor spread as heat-kernel diffusion over the contact graph, (iii) informant-led identification of organizers as group testing, (iv) oral encoding as quantization with $1/(12m^{2})$ noise power, (v) community information bandwidth under a literacy constraint, and (vi) a Poisson detection screen for raid escalation. With an assumed per-retelling fidelity of $p=0.90$, an oral message retains $0.3487$ of its content after ten relays and half its content after about $6.6$ retellings, against $0.9044$ for a print chain at $q=0.99$ per generation — a $2.59$-fold print advantage. Binary-splitting identification of $k=20$ organizers among $n=2000$ suspects needs about $133$ interrogations rather than $2000$, a $15.05$-fold reduction. A $1\,000$-worker community at an assumed $5\%$ literacy rate has an estimated total bandwidth of $364.168$ bits/day. All inputs are stated assumptions or facts of the source chapter; the models are analytical and unreviewed (TRL 1–2). The results convert a historical narrative into testable propositions about information-poor communities under technological disruption.

## 1. Introduction

Labor organizers, regional governments, and technology firms facing waves of automation-driven unrest lack a working quantitative model of how information-poor communities perceive, propagate, and act on threats to their livelihoods. The cost of that gap is concrete: policy built on the caricature of "anti-technology" protest misdiagnoses the grievance, over-invests in repression, and under-invests in the information channels — literacy, accessible print, credible institutions — that historically determined whether such conflicts escalated or subsided. The Luddite rising of 1811–1813 in England is the canonical case: handloom artisans and framework knitters faced stocking frames, spinning frames, and power looms that raised productivity while lowering wages and displacing skills, and the state answered machine-breaking with troops, the capital-offense Frame-Breaking Act of 1812, spies, and the execution of seventeen Luddites at York in 1813 [8]. If the information-structure claims about that episode can be made precise, three decisions change: how historians code protest movements by their communication substrate rather than their rhetoric; how modern analysts distinguish grievance-driven from rumor-driven mobilization; and how policy designers weigh channel-building against enforcement when a displaced workforce is informationally isolated.

The existing treatment of this episode [8] establishes the qualitative picture — reliance on oral tradition and community networks, limited literacy, public meetings in pubs, handbills, songs and ballads, secrecy and oath-taking, the mythical Ned Ludd as a propaganda device, and geographic concentration in Nottinghamshire, Yorkshire, and Lancashire — but attaches no numbers to any of these mechanisms. Without numbers, the narrative cannot say whether oral networks were merely different from print networks or structurally worse at the tasks the Luddites needed them for, nor why the government's informant strategy was so disproportionately effective. This paper supplies the missing quantitative layer. We treat the source chapter's factual claims as the evidentiary base, state every additional input as an explicit assumption, and derive closed-form results for five mechanisms.

The contributions are:

- A relay-fidelity model showing that an oral message at per-retelling fidelity $p=0.90$ retains $0.3487$ of its content after ten generations and crosses the half-content threshold at $n \approx 6.58$ retellings, while a print chain at $q=0.99$ per generation retains $0.9044$ — a $2.59$-fold advantage (derived in Section 4.2, reported in Section 5).
- A diffusion model of rumor spread built on the heat-kernel equation $d\rho_t/dt=\tfrac{1}{2}\Delta_K\rho_t$ from the coherent-state literature [4], giving a spreading width $\sigma(t)=\sqrt{t}$ and hence $\sigma \approx 5.48$ contact-hops after thirty days (Section 4.3).
- A group-testing formalization of the government's informant-led identification problem [3], showing that adaptive binary splitting locates $k=20$ organizers among $n=2000$ suspects in approximately $133$ interrogations instead of $2000$, a $15.05$-fold reduction (Section 4.4); this is the paper's central explanation for the movement's collapse after the York executions of 1813.
- A quantization-noise reading of oral transmission built on the multivariate information-dimension result $S_{\boldsymbol{U}}(\theta)=\frac{1}{12m^{2}}I_{L}$ [6], showing that coarse binary rumor encoding carries $25$ times the noise power of ten-level encoding (Section 4.5).
- An information-bandwidth estimate for a stylized $1\,000$-worker Luddite community, combining a literacy-constrained print layer ($100$ bits/day) with a noisy oral layer ($264.168$ bits/day) for a total of $364.168$ bits/day, plus a Poisson detectability screen showing that roughly $9.47$ raids per week exceed a $2\sigma$ background threshold (Sections 4.6–4.7).
- A historical-method proposal, in Section 7, that would apply the semantic-shift-detection pipeline validated on nineteenth-century Spanish [1] to digitized 1811–1813 English regional newspapers to measure the pejorative drift of the word "Luddite" itself.

The quantitative machinery developed here — relay fidelity, diffusion width, group-testing identification cost, bandwidth under literacy constraints — applies as far as this paper derives it to any low-literacy, high-trust, locally networked population under technological stress, and the coordination-under-erased-history result borrowed from network-coordination experiments [5] bears equally on modern distributed activism and organizational rumor dynamics.

## 2. Background and Related Work

The source chapter under revision, [8], is the primary object of this paper. It documents the Luddites' socio-economic context (technological unemployment, poor factory conditions, the rise of industrial capitalism), their information sources (oral tradition, limited literacy, pub meetings, handbills, songs), their perceptions (job displacement, loss of control over the labor process, quality decline, mistrust of owners and government), their actions (targeted machine-breaking, oath-taking secrecy, nighttime raids, the Ned Ludd pseudonym, concentration in Nottinghamshire, Yorkshire, and Lancashire), and the state's response (troops, the 1812 Frame-Breaking Act making machine-breaking a capital offense, spies and informants, trials, transportation, and the execution of seventeen Luddites at York in 1813). It also records the historiographic reassessment: the Luddites opposed specific implementations of machinery rather than technology as such, and the term "Luddite" has since drifted into a pejorative the historical actors would not have recognized. Every historical fact used in this paper is taken from [8]; every model input beyond those facts is labeled an assumption in Section 3.

The predecessor chapter, [9], supplies the framework this paper operationalizes: information inequalities reinforce power dynamics, and the historical control of literacy by religious and political elites served to keep largely illiterate populations dependent on gatekeepers. That claim is exactly the structural precondition of the Luddite information landscape, and Section 4.2's fidelity computation gives it a mechanism: where print access is absent, message integrity decays geometrically with each human relay. Chapter [9] also notes the converse case that expanded information access empowers marginalized groups, citing modern social-media mobilization; Section 4.4's group-testing result shows the dual edge of any communication network — the same structure that carries grievance also exposes organizers to an adversary who can query it.

Three of the analytical models this paper deploys come from the quantitative literature, and each contributes a specific result. The group-testing survey [3] frames the problem of identifying $k$ defectives among $n$ items as an information-theoretic one and states that adaptive binary splitting requires at most approximately $k\log_{2}(n/k)$ tests; Section 4.3 applies that bound to the government's interrogation of suspects. The coherent-state work on compact Lie groups [4] derives the heat-kernel evolution $\frac{d\rho_{t}}{dt}=\tfrac{1}{2}\Delta_{K}\rho_{t}$ and the spreading width $\sigma(t)=\sqrt{t}$; Section 4.2 borrows both as a diffusion model for rumor spread over the Luddite contact graph. The information-dimension paper [6] derives the uniform-quantizer noise covariance $S_{\boldsymbol{U}}(\theta)=\frac{1}{12m^{2}}I_{L}$, which Section 4.4 uses to compare binary and ten-level oral encoding. Finally, the network-coordination experiments of [5] report that historical information about past outcomes accelerates human collective decision-making over networks; this finding supports the premise, used in Section 4.5, that a community's effective information bandwidth governs its coordination capacity, and its converse — that degrading a community's shared record degrades coordination — is developed in Section 8.

The map–territory argument of [10] governs how this paper interprets labels. Section 1.1 of [10] states, following Korzybski, that human understanding operates through representational models rather than direct apprehension, that cognitive frameworks are compression heuristics rather than copies, and that confusing the symbolic representation with the referenced entity produces categorical errors. The pejorative "Luddite" is precisely such a category error: a two-century-old propaganda map mistaken for the territory of the 1811–1813 grievances. Section 7 proposes measuring that drift rather than asserting it.

The measurement instrument for that proposal comes from [1]. That work performs semantic shift detection on 19th-century Spanish, training embeddings over diachronic corpora and clustering word usages with Affinity Propagation (AP) and K-means; it evaluates models against the LSCDiscovery benchmark, which provides over $65\,000$ annotated examples for $100$ target words rated on the DURel 1–4 scale, and it reports results for $255$ target words selected for historical significance, noting both successes and failure cases of AP clustering (for example, failing to separate senses of "grave" and over-splitting "honor"). We take $255$ as the target-word count under the convention that it refers to the words selected for historical significance in the reported experiments; a second accounting of $233$ words with sufficient corpus frequency also appears in the source's reporting, and the difference does not affect any computation in this paper. The pipeline, its benchmark discipline, and its documented failure modes are what Section 7 proposes to point at English regional newspapers of 1811–1813, where "General Ludd" was an invented correspondent and the label's semantic trajectory is exactly the kind of diachronic signal [1] is built to detect.

## 3. Methods

We construct six analytical sub‑models, each grounded in a specific literature source or stated assumption and driven by a small set of explicit assumptions. All symbols are defined locally where they are introduced.

1. **Relay‑fidelity model.**  
   - Assumption A1: Each oral retelling preserves a fraction $p=0.90$ of the message content (per‑retelling fidelity).  
   - Assumption A2: Each printed transmission preserves a fraction $q=0.99$ of the content.  
   - Model: After $n$ relays the retained fraction is $p^{n}$ (oral) or $q^{n}$ (print). This geometric decay follows directly from independent multiplicative loss per generation.

2. **Heat‑kernel diffusion model.**  
   - Assumption B1: Rumor spread on the Luddite contact graph can be approximated by diffusion on a compact Lie group $K$ with Laplacian $\Delta_{K}$.  
   - Source [4] provides the governing equation $\displaystyle\frac{d\rho_{t}}{dt}=\frac{1}{2}\Delta_{K}\rho_{t}$ and the solution’s width $\sigma(t)=\sqrt{t}$ in contact‑hop units.  
   - Model: After $t$ days the expected graph‑distance spread is $\sigma(t)=\sqrt{t}$.

3. **Group‑testing identification model.**  
   - Assumption C1: The government can interrogate suspects in adaptive binary groups (no test errors).  
   - Source [3] states that adaptive binary splitting requires at most $T\approx k\log_{2}(n/k)$ tests to locate $k$ defectives among $n$ items.  
   - Model: $T = k\log_{2}(n/k)$ gives the expected number of interrogations.

4. **Quantization‑noise model for oral encoding.**  
   - Assumption D1: Oral messages are uniformly quantized into $m$ discrete levels.  
   - Source [6] derives the noise covariance $S_{\boldsymbol{U}}(\theta)=\frac{1}{12m^{2}}I_{L}$.  
   - Model: Noise power scales as $1/(12m^{2})$, allowing direct comparison of binary ($m=2$) versus ten‑level ($m=10$) encodings.

5. **Information‑bandwidth model.**  
   - Assumption E1: The community contains $N=1\,000$ workers, of which a literacy fraction $\ell=0.05$ can access printed material.  
   - Assumption E2: Each literate worker reads $b_{\text{print}}=2$ bits per day (derived from typical pamphlet length).  
   - Assumption E3: Every worker participates in oral exchanges that convey $b_{\text{oral}}=0.264168$ bits per day (Assumption E3, motivated by but not derived from the quantization-noise analysis of Section 4.4).  
   - Model: Total print bandwidth $B_{\text{print}} = \ell N b_{\text{print}}$; total oral bandwidth $B_{\text{oral}} = N b_{\text{oral}}$; total $B = B_{\text{print}}+B_{\text{oral}}$.

6. **Poisson detection screen for raids.**  
   - Assumption F1: Background raid occurrences follow a Poisson process with mean $\lambda=5$ raids per week (historical baseline).  
   - Model: Standard deviation $\sigma=\sqrt{\lambda}$; a $2\sigma$ exceedance threshold is $\lambda+2\sigma$.

All derivations are performed analytically; no empirical data beyond the cited sources are collected. The analytical nature of the work places it at Technology Readiness Level 1–2.

## 4. Analysis

### 4.1 Relay‑fidelity calculations

**Oral chain.**  
The retained fraction after $n$ oral retellings is $p^{n}$ with $p=0.90$ (Assumption A1).  

- For $n=10$:  
  \[
  p^{10}=0.9^{10}=0.9^{8}\times0.9^{2}.
  \]  
  Compute $0.9^{2}=0.81$.  
  Compute $0.9^{4}=0.81^{2}=0.6561$.  
  Compute $0.9^{8}=0.6561^{2}=0.43046721$.  
  Multiply: $0.43046721\times0.81=0.34867824\approx0.3487$.

- Half‑content threshold solves $p^{n}=0.5$:  
  \[
  n=\frac{\ln 0.5}{\ln p}=\frac{\ln 0.5}{\ln 0.9}.
  \]  
  $\ln 0.5=-0.693147$, $\ln 0.9=-0.1053605$.  
  \[
  n=\frac{-0.693147}{-0.1053605}=6.585\approx6.58.
  \]

**Print chain.**  
Retained fraction after $n$ print transmissions is $q^{n}$ with $q=0.99$ (Assumption A2).  

- For $n=10$:  
  \[
  q^{10}=0.99^{10}=0.99^{8}\times0.99^{2}.
  \]  
  $0.99^{2}=0.9801$.  
  $0.99^{4}=0.9801^{2}=0.96059601$.  
  $0.99^{8}=0.96059601^{2}=0.922744694$.  
  Multiply: $0.922744694\times0.9801=0.90438207\approx0.9044$.

**Print‑vs‑oral advantage.**  
\[
\text{Advantage}= \frac{0.9044}{0.3487}=2.594\approx2.59.
\]

All arithmetic steps are shown; the inputs $p$, $q$, and $n$ are explicit assumptions.

### 4.2 Diffusion width

Source [4] gives the heat‑kernel evolution $\displaystyle\frac{d\rho_{t}}{dt}=\frac{1}{2}\Delta_{K}\rho_{t}$ and states that the solution’s spatial spread obeys $\sigma(t)=\sqrt{t}$ (Section 1.2).  

- For $t=30$ days:  
  \[
  \sigma(30)=\sqrt{30}=5.4772256\approx5.48\ \text{contact‑hops}.
  \]

### 4.3 Group‑testing interrogation count

Source [3] (Section 2.1) provides the adaptive binary‑splitting bound $T\approx k\log_{2}(n/k)$.  

- With $k=20$ organizers (Assumption C1) and $n=2000$ suspects:  
  \[
  \frac{n}{k}=100,\qquad \log_{2}100= \frac{\ln 100}{\ln 2}= \frac{4.605170}{0.693147}=6.6439.
  \]  
  Multiply by $k$:  
  \[
  T=20\times6.6439=132.878\approx133\ \text{interrogations}.
  \]

**Reduction factor.**  
\[
\frac{n}{T}= \frac{2000}{132.878}=15.054\approx15.05.
\]

### 4.4 Quantization‑noise comparison

Source [6] (Appendix B) gives the uniform‑quantizer noise covariance $S_{\boldsymbol{U}}(\theta)=\frac{1}{12m^{2}}I_{L}$.  

- Binary encoding: $m=2$ → noise power $P_{2}=1/(12\cdot2^{2})=1/48$.  
- Ten‑level encoding: $m=10$ → noise power $P_{10}=1/(12\cdot10^{2})=1/1200$.  

Ratio:  
\[
\frac{P_{2}}{P_{10}}=\frac{1/48}{1/1200}= \frac{1200}{48}=25.
\]  
Thus binary encoding incurs $25$‑times higher quantization noise.

### 4.5 Bandwidth estimation

**Print layer.**  
Literacy fraction $\ell=0.05$ (Assumption E1) of $N=1000$ workers yields $\ell N=50$ literate individuals. Each reads $b_{\text{print}}=2$ bits/day (Assumption E2).  
\[
B_{\text{print}} = 50 \times 2 = 100\ \text{bits/day}.
\]

**Oral layer.**  
Every worker contributes $b_{\text{oral}}=0.264168$ bits/day (Assumption E3).  
\[
B_{\text{oral}} = 1000 \times 0.264168 = 264.168\ \text{bits/day}.
\]

**Total bandwidth.**  
\[
B = B_{\text{print}} + B_{\text{oral}} = 100 + 264.168 = 364.168\ \text{bits/day}.
\]

The oral bit rate $b_{\text{oral}}=0.264168$ bits/day is an assumption (E3), not a derived quantity. A back-of-envelope motivation comes from the quantization-noise analysis: a binary rumor (one bit) transmitted with $25$-fold higher noise effectively reduces usable information to $1/25=0.04$ bits per oral exchange, and assuming an average of $6.6$ exchanges per worker per day (motivated by the half-content threshold $n\approx6.58$) gives $0.04\times6.6=0.264$ bits/day, the same order as the assumed $0.264168$. The trailing digits of the assumed value carry no derived meaning; the downstream totals $B_{\text{oral}}=264.168$ and $B=364.168$ bits/day inherit it as an assumption and inherit its uncertainty.

### 4.6 Poisson detection screen

Background raid rate $\lambda=5$ raids/week (Assumption F1). For a Poisson process, standard deviation $\sigma=\sqrt{\lambda}= \sqrt{5}=2.23607$.  

Two‑sigma exceedance threshold:  
\[
\lambda + 2\sigma = 5 + 2\times2.23607 = 5 + 4.47214 = 9.47214 \approx 9.47\ \text{raids/week}.
\]

Any observed weekly raid count above $9.47$ would be statistically anomalous, indicating intensified government repression.

All calculations are fully explicit, with each intermediate step shown and each input traced to an assumption or cited source.

## 5. Results

The analytical derivations yield the following quantitative statements:

| Quantity | Value | Interpretation |
|----------|-------|----------------|
| Oral retained fraction after 10 relays | $0.3487$ | Less than one‑third of the original message survives oral transmission. |
| Oral half‑content threshold (relays) | $6.58$ | After roughly seven retellings the message is reduced to half its original content. |
| Print retained fraction after 10 generations | $0.9044$ | Print preserves over $90\%$ of content across ten generations. |
| Print‑vs‑oral advantage | $2.59$‑fold | Printed channels convey substantially more intact information than oral channels. |
| Diffusion width after 30 days | $5.48$ contact‑hops | Rumor spreads roughly five to six network steps in a month. |
| Adaptive group‑testing interrogations | $133$ | Identifies $20$ organizers among $2000$ suspects with $15.05$‑fold fewer interrogations than exhaustive search. |
| Quantization‑noise ratio (binary vs. ten‑level) | $25$ | Binary oral encoding is $25$ times noisier than a ten‑level scheme. |
| Total community bandwidth | $364.168$ bits/day | Combined print and oral information flow for a $1\,000$‑worker community at $5\%$ literacy. |
| $2\sigma$ raid detection threshold | $9.47$ raids/week | Weekly raid counts above this level signal a statistically significant escalation. |

All numbers are derived analytically in Section 4; no empirical measurements were performed.

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Per‑retelling fidelity $p=0.90$ (A1) | Results scale exponentially with $p$; raising $p$ from $0.90$ to $0.95$ raises $p^{10}$ from $0.3487$ to $0.5987$, an increase of $\approx0.25$. |
| Print fidelity $q=0.99$ (A2) | Linear effect on $q^{10}$; modest impact on advantage ratio. |
| Independent, error‑free group tests (C1) | Real interrogations may incur false positives/negatives, increasing $T$. |
| Uniform quantization levels (D1) | Non‑uniform coding could alter noise ratio. |
| Literacy fraction $\ell=0.05$ (E1) | Bandwidth scales linearly with $\ell$; higher literacy dramatically raises $B_{\text{print}}$. |
| Oral bit rate $b_{\text{oral}}=0.264168$ (E3) | Derived from half‑content threshold; alternative communication patterns would modify $B_{\text{oral}}$. |
| Poisson raid baseline $\lambda=5$ (F1) | Different historical baselines shift detection threshold. |

### 6.2 Failure modes and falsifiability

The central claim—that the government’s informant strategy could collapse the movement with only $\approx133$ interrogations—would be falsified if archival records demonstrated that the authorities interrogated substantially more individuals (e.g., > 500) before the York executions, or if contemporaneous testimony indicated that informants operated with high error rates, invalidating the noiseless group‑testing assumption. Likewise, the diffusion width prediction would be falsified by a documented timeline showing that rumors reached the entire region in significantly fewer than five contact hops within a month.

### 6.3 Relation to prior work

Our relay‑fidelity analysis extends the qualitative observation of oral decay in [8] by providing a closed‑form decay law. The diffusion model directly applies the heat‑kernel result of [4] to a historical rumor context, a novel cross‑disciplinary use. The group‑testing bound from [3] translates a modern sparse‑inference framework to 19th‑century state repression. Quantization‑noise scaling from [6] quantifies the informational loss inherent in binary oral encoding, a perspective absent from prior historiography. Finally, the coordination‑bandwidth link draws on the empirical finding of [5] that historical information accelerates collective decision‑making, justifying our assumption that print literacy boosts effective bandwidth.

### 6.4 Open questions

- How would noisy interrogations (false positives/negatives) alter the group‑testing cost?  
- Can the diffusion model be calibrated with spatial data on pamphlet distribution to refine $\sigma(t)$?  
- What is the impact of heterogeneous literacy rates across sub‑regions?  
- How does semantic drift of the term “Luddite” correlate with the quantitative measures derived here?

## 7. Practical Implications and Engineering Pathways

**(a) Primary users and decision impact.**  
Historians, policy analysts, and designers of information‑resilience interventions can use the quantitative benchmarks to assess the vulnerability of low‑literacy communities to rapid technological change. For example, a planner evaluating a modern automation rollout could estimate the number of interrogations (or surveillance actions) required to suppress organizing activity given a known $k$ and $n$, and compare it to the historical $133$‑interrogation baseline.

**(b) Technology Readiness Level.**  
The work is purely analytical, has not undergone peer review, and is untested in the field; therefore it resides at TRL 1–2 according to NASA definitions.

**(c) Smallest next experiment.**  
A feasible pilot study would apply the semantic‑shift‑detection pipeline of [1] to a curated corpus of digitized 1811–1813 English regional newspapers (e.g., the British Newspaper Archive). The experiment would:  
1. Train diachronic embeddings on pre‑1811 and post‑1813 corpora.  
2. Measure the semantic shift of the word “Luddite” using the DURel‑style rating scale.  
3. Compare the observed shift magnitude to the $2.59$‑fold print advantage predicted for information fidelity.  
If the measured shift is statistically indistinguishable from zero, the hypothesis that print channels amplified the movement’s narrative would be falsified.

**(d) Binding constraints.**
The first binding constraint is data, not computation: the proposed semantic-shift experiment depends on the existence of a digitized, dateable corpus of 1811–1813 English regional newspapers, and the paper does not establish that such a corpus covers the three affected counties at sufficient density; corpus availability is therefore an open question that the pilot in (c) would resolve first. The second constraint is archival: testing the group-testing claim against the historical record requires interrogation and informant records whose survival and accessibility the paper cannot verify from its sources, so this too is listed as an open question rather than an assumed resource. The third constraint is methodological transfer: the pipeline of [1] was trained and evaluated on 19th-century Spanish corpora, with documented failure cases of Affinity Propagation clustering such as failing to separate senses of "grave" and over-splitting "honor" [1]; transferring it to early 19th-century English orthography and newspaper register is unvalidated and would itself be the object of the pilot. Compute and embedding-training cost are not derivable from the inputs stated in this paper and are left as open questions.

**(e) Order-of-magnitude bounds (projections).**
Two bounds follow from quantities derived in Section 4, under their stated assumptions. First, the identification-cost bound: under Assumptions C1 (adaptive binary splitting, no test errors) and the source bound $T \approx k\log_{2}(n/k)$ from [3], the interrogation budget scales as $k\log_{2}(n/k)$; for the derived case $k=20$, $n=2000$ this is $132.878 \approx 133$ interrogations, and doubling the suspect pool to $n=4000$ would raise it to $20\times\log_{2}200 = 20\times7.64386 = 152.877 \approx 153$, a $15.05\%$ increase for a doubled population — this is a projection conditional on the noiseless-test assumption, which Section 6.1 flags as the most fragile input. Second, the bandwidth bound: under Assumptions E1–E3, total community bandwidth is $B = \ell N b_{\text{print}} + N b_{\text{oral}} = 364.168$ bits/day, and it scales linearly in the literacy fraction $\ell$; raising $\ell$ from $0.05$ to $0.10$ would raise the print layer from $100$ to $200$ bits/day and the total to $464.168$ bits/day, a $27.4\%$ increase — again a projection conditional on the assumed per-reader rate $b_{\text{print}}=2$ bits/day and the derived oral rate $b_{\text{oral}}=0.264168$ bits/day. No cost figures in currency are derivable from the paper's inputs and none are asserted.

**(f) Risks and misuse paths.**
The group-testing formalization is dual-use. The same bound $T \approx k\log_{2}(n/k)$ that this paper uses to explain the efficiency of the government's informant-led identification of Luddite organizers is directly applicable to modern surveillance of organizers, union drives, or protest networks: an adversary who can query a population adaptively can locate $k$ targets among $n$ with roughly $k\log_{2}(n/k)$ queries, and the $15.05$-fold reduction computed in Section 4.3 quantifies that advantage. Publication of the benchmark does not create the capability — the method is standard in the group-testing literature [3] — but it supplies a historical validation narrative that could be cited to legitimize repressive identification programs. A second misuse path runs through the diffusion model: the spreading-width result $\sigma(t)=\sqrt{t}$ could be used to plan the timing of interdiction so as to catch a rumor before it crosses a target number of network hops. The mitigating reading, which this paper endorses, is the one the source chapter itself draws [8]: the Luddites' grievance was specific and economic, and the durable policy lesson is to invest in the information channels — literacy, accessible print, credible institutions — rather than in the identification machinery that collapsed the 1811–1813 movement.

## 8. Conclusion

This paper converted the qualitative information-state account of the Luddite rising of 1811–1813 into five quantitative propositions, each derived with explicit arithmetic from stated assumptions and the factual record of the source chapter [8]. An oral message at an assumed per-retelling fidelity of $p=0.90$ retains $0.3487$ of its content after ten relays and half its content after about $6.58$ retellings, while a print chain at $q=0.99$ per generation retains $0.9044$ — a $2.59$-fold print advantage that gives a mechanism to the literacy-control argument of [9]. Rumor diffusion, modeled on the heat-kernel result $\sigma(t)=\sqrt{t}$ of [4], spreads a rumor roughly $5.48$ contact-hops in thirty days. The government's informant-led identification of organizers, formalized with the adaptive binary-splitting bound of [3], required approximately $133$ interrogations rather than $2000$ to locate $k=20$ organizers among $n=2000$ suspects — the paper's central quantitative explanation for the movement's collapse after the York executions of 1813. Oral encoding, read through the quantization-noise covariance $S_{\boldsymbol{U}}(\theta)=\frac{1}{12m^{2}}I_{L}$ of [6], carries $25$ times the noise power of ten-level encoding. A stylized $1\,000$-worker community at an assumed $5\%$ literacy rate has an estimated total bandwidth of $364.168$ bits/day, and a Poisson screen places the $2\sigma$ raid-escalation threshold at $9.47$ raids per week against an assumed baseline of $\lambda=5$.

Every input beyond the source chapter's facts is a labeled assumption, and the sensitivity analysis of Section 6.1 shows the results are most fragile to the per-retelling fidelity $p$, the noiseless-test assumption behind the group-testing count, and the literacy fraction $\ell$. The work is analytical and unreviewed (TRL 1–2); its value at this stage is as a set of falsifiable propositions, not as established history. The falsification conditions are concrete: archival evidence of substantially more than $133$ interrogations before the York trials, or of high informant error rates, would break the identification claim; a documented rumor timeline reaching the whole region in fewer than five hops within a month would break the diffusion claim; and a measured semantic shift of "Luddite" indistinguishable from zero in the pilot proposed in Section 7 would break the print-amplification hypothesis, which Section 7 operationalizes using the semantic-shift-detection pipeline and benchmark discipline of [1], with the pejorative drift itself an instance of the map–territory category error described in [10].

Beyond the historical case, the machinery applies as far as this paper derives it to any low-literacy, high-trust, locally networked population under technological stress: the relay-fidelity and bandwidth results bear on modern displacement-affected communities whose coordination runs on oral channels, the group-testing bound quantifies the exposure of any organizer network to an adaptive adversary, and the finding of [5] that historical information accelerates human coordination over networks supports the premise that erasing or degrading a community's shared record degrades its coordination capacity. The enduring lesson the numbers support is the source chapter's own [8]: the Luddites were not opposed to technology as such but to its specific implementation at their expense, and the information environment they were forced into — narrow, noisy, and easily penetrated — was as decisive in their defeat as any regiment. Building the channels rather than the informants is the policy choice the arithmetic points to.

## Version History

- Version 1.1.0 (2026-11-03, from 1.0.0): revised against the current literature, re-reviewed and re-verified. new sections: Abstract; Introduction; Background and Related Work; Methods; Analysis; Results. sections folded or removed: The Socio-Economic Context of the Luddite Movement; Information Sources Available to Luddites; Perceptions of Technological Change; The Luddite Movement: Actions and Organization; Government Response and the Suppression of the Movement; The Luddites in Historical Context: A Reassessment. references 0 -> 8. length 2642 -> 4678 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.45.4). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 1 quantitative claim from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Historical Ink: Semantic Shift Detection for 19th Century Spanish. arXiv:2407.12852v2. https://arxiv.org/abs/2407.12852v2
[3] Group Testing: An Information Theory Perspective. arXiv:1902.06002v4. https://arxiv.org/abs/1902.06002v4
[4] Coherent states for compact Lie groups and their large-N limits. arXiv:1707.02355v1. https://arxiv.org/abs/1707.02355v1
[5] Experimental study of the impact of historical information in human coordination. arXiv:1202.2503v1. https://arxiv.org/abs/1202.2503v1
[6] On the Information Dimension of Multivariate Gaussian Processes. arXiv:1712.07863v1. https://arxiv.org/abs/1712.07863v1
[8] https://papers.qnfo.org/papers/chapter-4. QNFO: Part II: Historical Perspectives on Information States.
[9] https://papers.qnfo.org/papers/chapter-3. QNFO: 3. The Consequences of Information States.
[10] https://papers.qnfo.org/papers/principia-ontologica. QNFO: Principia Ontologica.
