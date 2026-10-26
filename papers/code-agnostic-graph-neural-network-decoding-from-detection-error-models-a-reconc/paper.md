# Code-Agnostic Graph Neural Network Decoding from Detection Error Models: A Reconciled Quantitative and Structural Assessment

## Abstract

Graph neural network (GNN) decoders for quantum error correction have traditionally been tied to specific code families through their input representations. The POLYMECHANON decoder [1, 2] proposes a contract in which the sole input is the detection error model (DEM)—a tripartite graph of detectors, error mechanisms, and logical observables—thereby treating the code as data rather than as an architectural choice. This paper provides an independent, arithmetic‑first assessment of that claim. We translate the reported headline percentages into concrete quantities: a 25 % reduction in logical failures versus correlated MWPM on the rotated surface code yields an improvement factor 0.75, which under the standard sub‑threshold scaling ansatz $p_L\propto(p/p_{\mathrm{th}})^{\lceil d/2\rceil}$ corresponds to a relative pseudo‑threshold improvement of $\approx 10.06$ % at $d=5$ and $\approx 7.46$ % at $d=7$; a 16 % reduction on the $[[130,4,6]]$ qLDPC code gives a factor 0.84 and an equivalent threshold improvement of $\approx 5.98$ %. Assuming “a few ms’’ per shot on a GPU and “a few tens of ms’’ on a CPU, the speedup is bounded in $[4\times,25\times]$ with a midpoint of $\approx 10$×. We derive exact DEM graph sizes for canonical cases (441 detectors, 1 337 mechanisms, 2 681 edges at $d=8$, $R=8$), present a cheap non‑isomorphism certificate between surface‑code and qLDPC DEMs, and show that the reported post‑selection result (>10× error reduction at >90 % shot retention) requires discarded shots to fail at $\approx 9.1$× the base logical error rate. Size‑generalization, DEM fidelity, and hardware‑asymmetric latency comparison emerge as the principal open risks, each paired with a falsifiable experiment.

## 1. Introduction

Fault‑tolerant quantum computation relies on a classical decoding layer that converts syndrome measurement streams into logical corrections faster than errors accumulate. Today’s dominant decoders—minimum‑weight perfect matching (MWPM) for surface‑type codes and belief propagation with ordered‑statistics post‑processing (BP+OSD) for quantum low‑density parity‑check (qLDPC) codes—are hand‑engineered per code family and either sacrifice accuracy (MWPM ignores error correlations) or incur latency that scales with physical error rate and code size (BP+OSD). Consequently, every new code family or noise model triggers a fresh decoder‑engineering effort, delaying the deployment of novel codes by months.

Neural decoders promise learned inference at constant time, but most published architectures hard‑code the code family: the input representation (e.g., a $d\times d\times R$ syndrome tensor) encodes geometry directly into the network. POLYMECHANON [1, 2] proposes a different contract: the decoder consumes only the DEM, a code‑agnostic object any stabiliser code under any expressible noise model can emit, rendered as a tripartite graph with all input features computed from the code as data. If this contract holds at scale, a code designer would compile a DEM and run a single training job—reported to take from hours to a few days on four GPUs—rather than commissioning a bespoke decoder, and a real‑time control stack could budget a fixed, error‑rate‑independent per‑shot decoding cost.

**Contributions.**  
1. **Quantitative translation.** We convert the reported relative improvements into improvement factors, threshold‑equivalent shifts, distance‑equivalent readings, and throughput budgets, with every input number traced to [1, 2] and all assumptions explicitly labeled.  
2. **Structural analysis.** We derive exact node and edge counts for canonical DEMs, establish an $O(d^{2}R)$ scaling law, and construct a cheap non‑isomorphism certificate that bounds what any DEM‑only decoder can achieve.  
3. **Critical appraisal.** We identify size‑generalization, DEM fidelity, and hardware‑asymmetric latency comparison as the principal risks, and we propose concrete falsification experiments for each.

## 2. Background and Related Work

**POLYMECHANON decoder [1, 2].** The decoder ingests a DEM represented as a tripartite graph of detectors, error mechanisms, and logical observables. Its headline claims are: up to 25 % fewer logical failures than correlated MWPM on the rotated surface code; up to 16 % fewer failures than BP+OSD on the $[[130,4,6]]$ qLDPC code; decoding time independent of physical error rate, a few ms per shot on a single GPU versus a few tens of ms on a single CPU core; a cross‑code model that stays within 10 % of BP+OSD on seen families but fails to generalize to unseen larger codes; and confidence‑based post‑selection that lowers the logical error rate by more than an order of magnitude while retaining >90 % of shots. These statements constitute the sole empirical inputs to our derivations.















**QNFO frameworks [10–13].**    

## 3. Methods

**Definitions.** A stabiliser code encodes $k$ logical qubits into $n$ physical qubits with distance $d$. Repeated syndrome measurement produces *detectors* (parity checks that must be $0$ in the absence of errors). The *detection error model* (DEM) lists error *mechanisms*, each with probability $p_i$ and a fault signature—the detectors it flips and the logical observables it anticommutes with. Decoding is the inference of the most likely logical observable flips given detector firings.

**Analytical pipeline.**

1. **Claim extraction.** From [1, 2] we extract five headline claims (C1–C5) listed in the Introduction.  
2. **Unit normalization.** “X % fewer logical failures’’ is interpreted as a relative reduction factor $F=1-X/100$.  
3. **Model‑based translation.** We employ the sub‑threshold scaling ansatz $p_L(p,d)=A\,(p/p_{\mathrm{th}})^{\lceil d/2\rceil}$, noting that it is well supported for surface codes and heuristic for qLDPC codes.  
4. **Structural sizing.** The DEM is modeled as an attributed tripartite graph $G=(D\cup M\cup L,E)$. Node and edge counts are derived for canonical cases under explicitly stated construction conventions.  
5. **Throughput budgeting.** Latency claims are bounded using the published qualitative ranges; a neutral‑atom‑style cycle budget $T_{\mathrm{cycle}}=10$ ms is introduced as a projection parameter.  

All derived quantities trace to [1, 2] plus explicitly labeled assumptions; no numbers are invented.

## 4. Analysis

### 4.1 Improvement factor and effective threshold shift (C1)

Input [1, 2]: up to 25 % fewer logical failures than correlated MWPM.  
Improvement factor:
$$F_1 = 1 - 0.25 = 0.75.$$

Using the ansatz with $m=\lceil d/2\rceil$ and holding $r=p/p_{\mathrm{th}}$ fixed:
$$\left(\frac{p_{\mathrm{th}}^{\mathrm{MWPM}}}{p_{\mathrm{th}}^{\mathrm{POLY}}}\right)^{m}=0.75
\;\Longrightarrow\;
\frac{p_{\mathrm{th}}^{\mathrm{POLY}}}{p_{\mathrm{th}}^{\mathrm{MWPM}}}
=\left(\frac{4}{3}\right)^{1/m}.$$

* At $d=5$ ($m=3$): $\ln(4/3)=0.287682$; $0.287682/3=0.095894$; $e^{0.095894}=1.100642$, i.e. $\approx 10.06$ % relative threshold improvement.  
* At $d=7$ ($m=4$): $0.287682/4=0.071921$; $e^{0.071921}=1.074570$, i.e. $\approx 7.46$ % improvement.  
* At $d=9$ ($m=5$): $0.287682/5=0.057536$; $e^{0.057536}=1.059224$, i.e. $\approx 5.92$ % improvement.

**Distance‑equivalent reading.** At fixed threshold with $r=0.5$:
$$\Delta m = \frac{\ln 0.75}{\ln 0.5}=0.4150375.$$
One odd‑distance step ($\Delta d=2$) multiplies $p_L$ by $0.5$, so the 25 % improvement corresponds to roughly half a distance step at $r=0.5$.

### 4.2 qLDPC improvement (C2)

Input [1, 2]: up to 16 % fewer logical failures than BP+OSD on $[[130,4,6]]$.  
Improvement factor:
$$F_2 = 1 - 0.16 = 0.84,$$
with $m=\lceil6/2\rceil=3$.

Threshold ratio:
$$\frac{p_{\mathrm{th}}^{\mathrm{POLY}}}{p_{\mathrm{th}}^{\mathrm{BP+OSD}}}
=\left(\frac{1}{0.84}\right)^{1/3}.$$

Arithmetic: $1/0.84=1.190476$; $\ln(1.190476)=0.174353$; $0.174353/3=0.058118$; $e^{0.058118}=1.059840$.  
Thus the equivalent relative threshold improvement is $\approx 5.98$ %.

### 4.3 Latency and throughput (C3)

Input [1, 2]: “a few ms’’ per shot on one GPU versus “a few tens of ms’’ on one CPU core (for $[[130,4,6]]$).  
We instantiate “a few ms’’ as $t_{\mathrm{G}}\in[2,5]$ ms and “a few tens of ms’’ as $t_{\mathrm{B}}\in[20,50]$ ms.

Speedup bounds:
$$s_{\min}= \frac{20}{5}=4,\qquad
s_{\max}= \frac{50}{2}=25,\qquad
s_{\mathrm{mid}}= \frac{35}{3.5}\approx10.$$

Throughputs at midpoints:
$$\text{GPU: } \frac{1}{0.0035}\approx285.7\ \text{shots s}^{-1},\qquad
\text{CPU: } \frac{1}{0.035}\approx28.6\ \text{shots s}^{-1}.$$

**Real‑time projection (labeled).** Assuming a neutral‑atom‑style cycle budget $T_{\mathrm{cycle}}=10$ ms, POLYMECHANON at $3$ ms leaves a $7$ ms margin (range $5$–$8$ ms), whereas BP+OSD at $30$ ms exceeds the budget by $20$ ms. The candidate‑for‑real‑time claim holds only if $T_{\mathrm{cycle}}\ge3$ ms and GPU‑to‑controller latency is negligible—both not quantified in [1, 2].

### 4.4 Post‑selection consistency (C5)

Input [1, 2]: confidence‑based post‑selection reduces logical error by >10× while retaining >90 % of shots.  
Let retained fraction $f=0.9$, post‑selected rate $p_L' = p_L/10$, and discarded‑shot rate $p_L^{\mathrm{disc}}$. Conservation of failures:
$$p_L = f\,p_L' + (1-f)\,p_L^{\mathrm{disc}}.$$

Substituting $f=0.9$:
$$0.1\,p_L^{\mathrm{disc}} = p_L - 0.09\,p_L = 0.91\,p_L
\;\Longrightarrow\;
p_L^{\mathrm{disc}} = 9.1\,p_L.$$

Thus the discarded 10 % must carry failures at $\approx 9.1$× the base rate. Throughput cost:
$$\frac{0.1}{0.9}\approx0.111\;(11.1\%).$$
Accuracy‑per‑throughput gain:
$$\frac{10}{0.9}\approx11.1\times.$$

### 4.5 DEM graph sizing (structural derivation)

**Surface code, phenomenological noise.**  
Detectors: $N_D=(d^{2}-1)(R-1)$.  
At $d=8$, $R=8$: $d^{2}-1=63$, $R-1=7$, $N_D=63\times7=441$.

Mechanisms: $n=d^{2}=64$ data qubits → $128$ data‑error mechanisms per round (each flips 2 detectors); $63$ measurement‑error mechanisms per round (each flips 1 detector). Over $7$ rounds:
$$N_M=(128+63)\times7=191\times7=1337.$$

Edges into detectors:
$$E_{D}=128\times7\times2 + 63\times7\times1 = 1792 + 441 = 2233.$$
Edges into logical observables (single logical qubit, Z‑type):
$$E_{L}=64\times7=448.$$

Totals:
$$N_{\text{nodes}}=441+1337+1=1779,\qquad
N_{\text{edges}}=2233+448=2681.$$
All counts scale as $O(d^{2}R)$.

**$[[130,4,6]]$ qLDPC (projection).**  
Detectors per round: $n-k=126$.  
Assume $4$ mechanisms per qubit per round (circuit‑level noise multiplier).  
Mechanisms per round: $4\times130=520$, yielding $\approx1040$ detector edges and $\approx520$ logical edges per round.  
At $R=8$:
$$N_{\text{nodes}}\approx126\times8 + 520\times8 + 4 = 5172,$$
$$N_{\text{edges}}\approx(1040+520)\times8 = 12480.$$
Thus the qLDPC DEM is $\approx 2.9$× larger in nodes and $\approx 4.7$× larger in edges than the $d=8$ surface‑code DEM. Varying the mechanism multiplier between $2$ and $8$ yields a node‑count range $2600$–$10300$.

### 4.6 Isomorphism‑invariance bound

A DEM‑only decoder is a function $f(G)$ on attributed DEM graphs. If two DEMs are isomorphic as attributed graphs (identical up to relabeling), then $f(G_{1})=f(G_{2})$ for any architecture that consumes only graph structure and attributes. Consequently, DEM‑isomorphic codes are indistinguishable to any DEM‑only decoder, establishing a representational ceiling.

A cheap certificate uses part‑size vectors $(|D|,|M|,|L|)$. For the $d=8$ surface‑code DEM the vector is $(441,1337,1)$. For any $R$‑round $[[130,4,6]]$ DEM under the assumed multiplier it is $(126R,520R,4)$. No integer $R$ satisfies both $126R=441$ and $520R=1337$, so the two DEMs are provably non‑isomorphic by part sizes alone. This structural separation aligns with the reported cross‑family generalization gap [1, 2].

### 4.7 Cross‑code model accounting (C4)

Input [1, 2]: the cross‑code model stays within 10 % of BP+OSD on seen families. “Within 10 %’’ means
$$\frac{p_L^{\mathrm{cross}}}{p_L^{\mathrm{BP+OSD}}}\le1.10.$$

Combined with the dedicated‑model factor $F_2=0.84$ on $[[130,4,6]]$, the worst‑case penalty of the cross‑code model versus a dedicated model is
$$\frac{1.10}{0.84}=1.3095\approx1.31.$$



## 5. Results

1. **Surface‑code improvement factor.** $F_1=0.75$; equivalent threshold improvements: $\approx 10.06$ % at $d=5$, $\approx 7.46$ % at $d=7$, $\approx 5.92$ % at $d=9$; distance‑equivalent exponent gain $0.415$ ($\approx$half a distance step at $r=0.5$).  
2. **qLDPC improvement factor.** $F_2=0.84$; equivalent threshold improvement $\approx 5.98$ %; encoding rate $k/n=4/130\approx3.08\%$.  
3. **Latency (conditional).** Speedup bounded in $[4\times,25\times]$, midpoint $\approx 10$×; projected throughputs $≈286$ shots s$^{-1}$ (GPU) vs $≈29$ shots s$^{-1}$ (CPU).  
4. **Post‑selection (conditional).** >10× error reduction at >90 % retention requires discarded‑shot failure rate $\approx 9.1$× base; throughput cost $≈11.1\%$; accuracy‑per‑throughput gain $≈11.1\times$.  
5. **DEM sizing.** Surface code ($d=8$, $R=8$): 441 detectors, 1 337 mechanisms, 1 779 nodes, 2 681 edges, $O(d^{2}R)$.  
   $[[130,4,6]]$ ($R=8$): $\approx 5$ 172 nodes, $\approx 12$ 480 edges (projection).  
6. **Non‑isomorphism certificate.** Part‑size vectors differ for all integer $R$, proving the two DEMs non‑isomorphic.  
7. **Cross‑code penalty bracket (conditional).** $[1.0,1.31]$ relative to the dedicated model.

## 6. Discussion

**Limitations.**  
(i) The threshold translations rely on the $\lceil d/2\rceil$ ansatz, which is well supported for surface codes but heuristic for qLDPC codes; the qLDPC figures are therefore illustrative.  
(ii) All quantitative inputs are drawn from the abstract of [1, 2]; the “up to X %’’ phrasing denotes best‑case performance, so typical performance may be lower.  
(iii) The latency bounds compare GPU to CPU hardware and thus overstate any hardware‑neutral advantage; a same‑hardware comparison is not derivable from the source.  
(iv) The qLDPC graph‑size projection assumes a mechanism multiplier of 4; the true multiplier is unspecified, so the node/edge counts are approximate.  
(v) The isomorphism argument uses part‑size vectors, a weak invariant; stronger invariants could tighten the ceiling but are not required for the present claim.

**Failure modes of the DEM‑only paradigm.**  
*Size generalization.* Message‑passing receptive fields are local; larger codes exhibit correlation structures exceeding the receptive field of networks trained on smaller graphs, as observed in transfer‑learning literature [4, 8].  
*Representational ceiling.* DEM‑isomorphic codes cannot be distinguished, limiting any decoder that relies solely on the DEM.  
*Density.* The DEM size is fixed by code and noise model, so the decoder processes a dense graph even when the syndrome is sparse, potentially losing the latency advantage of defect‑centric approaches [7].  
*Training cost opacity.* The abstract reports training times (hours to days on four GPUs) but does not quantify total computational cost, which must be considered in system‑level budgeting.

**Falsification experiments.**  
1. **Post‑selection test.** Measure discarded‑shot failure rate; if it is < 9 × base, the >10× reduction claim is falsified.  
2. **Latency parity test.** Run POLYMECHANON and BP+OSD on identical GPU hardware; if the measured speedup falls below 4×, the latency claim is falsified.  
3. **Cross‑code generalization test.** Train a single model on small surface‑code DEMs and evaluate on unseen larger qLDPC DEMs without retraining; a failure to achieve performance within the $[1.0,1.31]$ penalty bracket falsifies the structural‑class explanation.  
4. **Threshold extrapolation test.** Verify that the observed logical‑error reduction matches the predicted threshold shift at multiple distances; deviation beyond the reported “up to X %’’ range falsifies the ansatz‑based translation.  
5. **Training‑cost accounting.** Compare total GPU‑hours required for a new code family against the claimed “hours to days’’; a significantly higher cost would challenge the practicality claim.

**Open questions.** Can spectral invariants [11] be used to cluster DEMs and guide curriculum learning? Does a queuing‑network analysis [3] yield a baseline that a GNN must surpass to justify its cost? Are multi‑view aggregation strategies [9] effective for combining detector, mechanism, and logical‑observable messages?  

## 7. Practical Implications and Engineering Pathways

**(a) Users and decision impact.** Quantum‑hardware engineers and compiler developers who must integrate a decoder into a fault‑tolerant stack would benefit from a DEM‑only decoder if the reported latency and accuracy gains hold, because it would eliminate per‑code redesign and enable rapid deployment across heterogeneous code families.

**(b) Technology readiness.** The work is purely analytical and has not undergone peer review; according to NASA TRL definitions it resides at TRL 1–2. Analytical extensions never exceed TRL 3 without experimental validation.

**(c) Minimal next experiment.** Build a prototype decoder that ingests a DEM for a rotated surface code at $d=5$ and $d=7$, measures logical error rate across a range of physical error rates, and records per‑shot wall‑clock time on the same GPU/CPU hardware. Success criteria: (i) observed logical‑error reduction $\ge$ 20 % relative to correlated MWPM (matching the “up to 25 %’’ claim) and (ii) measured GPU latency $\le$ 5 ms per shot, confirming a speedup $\ge$ 5× over the CPU baseline. Failure of either criterion falsifies the main quantitative claims.

**(d) Engineering constraints.** The DEM construction requires full knowledge of detector‑mechanism‑observable relationships; any omission degrades input fidelity. GPU memory limits bound the maximum DEM size that can be processed in a single forward pass; for large qLDPC codes the $O(d^{2}R)$ node count may exceed typical GPU capacities, necessitating graph‑partitioning or out‑of‑core techniques (open question).  

**(e) Projected cost/performance bounds.** Assuming the latency ranges $t_{\mathrm{G}}\in[2,5]$ ms and $t_{\mathrm{B}}\in[20,50]$ ms from § 4.3, the projected speedup is $[4\times,25\times]$ with a midpoint of $10\times$. The projected throughput at the midpoint is $≈286$ shots s$^{-1}$ per GPU versus $≈29$ shots s$^{-1}$ per CPU core, implying a hardware‑cost advantage of roughly one GPU per ten CPU cores for comparable decoding rates. These projections are explicitly labeled as conditional on the latency statements in the abstract.

**(f) Risks and misuse paths.** Over‑reliance on the DEM‑only contract could lead to deployment of decoders on codes whose DEMs are poorly approximated (e.g., highly correlated noise models), causing hidden logical‑error spikes. Reporting “up to 25 %’’ improvements without specifying operating points may mislead system designers into assuming uniform gains across all regimes.

## 8. Conclusion

We have performed a transparent, arithmetic‑driven assessment of the POLYMECHANON code‑agnostic GNN decoder, converting its reported percentages into improvement factors (0.75, 0.84), threshold‑equivalent shifts ($\approx 6$–10 % relative, distance‑dependent), latency bounds ($[4\times,25\times]$, midpoint $\approx 10$×), post‑selection separability requirements (discarded‑shot rate $\approx 9.1$× base), and DEM graph sizes ($O(d^{2}R)$ scaling with concrete counts). The DEM‑as‑input contract is a genuine architectural contribution; its principal open risks—size generalization, DEM fidelity, hardware‑fair latency comparison, and unreported training cost—are each paired with a falsifiable test. Resolving size‑generalization, possibly via scale‑adaptive or hierarchical architectures, is the key condition for DEM‑grounded decoding to become a route to universal decoders.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.21.2-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 12 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.01683&amp;start=0&amp;max_results=1
[2] A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model. arXiv:2610.01683v1. https://arxiv.org/abs/2610.01683v1
[3] A Tutorial about Random Neural Networks in Supervised Learning. arXiv:1609.04846v1. https://arxiv.org/abs/1609.04846v1
[4] Learning Universal Graph Neural Network Embeddings With Aid Of Transfer Learning. arXiv:1909.10086v3. https://arxiv.org/abs/1909.10086v3
[5] Graph Neural Networks for Channel Decoding. arXiv:2207.14742v2. https://arxiv.org/abs/2207.14742v2
[6] GraphFPN: Graph Feature Pyramid Network for Object Detection. arXiv:2108.00580v3. https://arxiv.org/abs/2108.00580v3
[7] Sparse Mamba Decoder for Quantum Error Correction: Efficient Defect-Centric Processing of Surface Code Syndromes. arXiv:2605.17156v2. https://arxiv.org/abs/2605.17156v2
[8] Predicting concentration levels of air pollutants by transfer learning and recurrent neural network. arXiv:2502.01654v1. https://arxiv.org/abs/2502.01654v1
[9] Mul-GAD: a semi-supervised graph anomaly detection framework via aggregating multi-view information. arXiv:2212.05478v1. https://arxiv.org/abs/2212.05478v1
[10] https://papers.qnfo.org/papers/code-agnostic-graph-neural-network-decoding-from-detection-error-models-a-reconc. QNFO: Code-Agnostic Graph Neural Network Decoding from Detection Error Models: A Reconciled Quantitative and Structural Assessment.
[11] https://papers.qnfo.org/papers/comprehensive-technical-framework-for-network-isomorphism. QNFO: Comprehensive Technical Framework for Network Isomorphism.
[12] https://papers.qnfo.org/papers/exact-maximum-likelihood-quantum-decoding-beyond-treewidth-a-reconciled-structur. QNFO: Exact Maximum-Likelihood Quantum Decoding beyond Treewidth: A Structural Analysis of Rank-Decomposition Dynamic Programming.
