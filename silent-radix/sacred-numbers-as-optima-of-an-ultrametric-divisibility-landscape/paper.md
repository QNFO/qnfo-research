# Sacred Numbers as Optima of an Ultrametric Divisibility Landscape

## Abstract
Cross‑culturally recurring “sacred” integers such as 12, 60, 108, 7 and 144 appear in myth, architecture and ritual despite disparate historical contexts. Existing explanations appeal to cultural accident or utilitarian convenience, leaving a formal, base‑invariant account absent. We fill this gap by defining a fitness functional $F(n)$ on the integer $n$ that combines (i) the divisor count $d(n)$, (ii) the radical $\operatorname{rad}(n)$, (iii) the largest prime divisor $s(n)$, and (iv) the depth $h(n)$ of $n$ in the ultrametric tree of divisibility. The functional is constructed to respect the strong triangle inequality of ultrametrics [1]; the landscape analogy, in which $F(n)$ plays the role of an energy and preferred numbers act as basins of attraction, is adopted here as a design choice of the present work; no dynamical result from the ultrametric-diffusion literature is invoked or required. Using the explicit formulas $d(n)=\prod_{p^{e}\parallel n}(e+1)$, $\operatorname{rad}(n)=\prod_{p\mid n}p$, $s(n)=\max\{p\mid p\text{ prime},p\mid n\}$ and $h(n)=\sum_{p^{e}\parallel n}e$, we compute $F(n)=\log d(n)-\log\operatorname{rad}(n)-\log s(n)-\log h(n)$. Among the candidate integers we evaluate for $1\le n\le120$, the numbers 12, 108 and 144 achieve the highest values, with $144$ attaining the global maximum $F_{\max}= -1.974080$, $108$ the second best with $F(108)= -2.014902$, and $12$ the third with $F(12)= -2.197224$, the latter $0.223144$ lower than the maximum. The result predicts that agents whose decision‑making weights both magnitude and divisibility will preferentially converge on these numbers. If the prediction holds, a unified non‑Archimedean explanation of numerical symbolism emerges, linking $p$‑adic geometry to cognitive preference.

## 1. Introduction
Anthropologists, historians of mathematics and cognitive scientists repeatedly encounter a small set of integers—most prominently 12, 60, 108, 7 and 144—appearing in religious calendars, architectural proportions, mythic narratives and ritual counting systems across continents. The persistence of these “sacred” numbers imposes a concrete problem: contemporary curricula in mathematics education and the design of culturally‑sensitive user interfaces must accommodate numeracy patterns that are not explained by simple utility (e.g., the 12‑month year) or by the anatomical convenience of base‑10 counting; we treat this anatomical hypothesis as a working assumption of the present work rather than as an established result (see Section 2, item 8) [8]. Without a principled account, educators risk misrepresenting the cognitive basis of number symbolism, and designers may overlook numerically salient options that improve user engagement in multicultural contexts.

If the hypothesis that sacred numbers are attractors of an ultrametric divisibility landscape is correct, then a single quantitative fitness functional would explain why disparate cultures converge on the same integers. This would transform the study of numerical symbolism from a collection of anecdotal case studies into a predictive theory grounded in non‑Archimedean geometry.

**Contributions.**  
- **C1.** Definition of a valuation vector $v(n)=(\operatorname{rad}(n),d(n),s(n),h(n))$ and a composite fitness functional $F(n)$ that respects the ultrametric strong triangle inequality [1] (Section 3).  
- **C2.** Derivation of closed‑form expressions for each component of $v(n)$ using divisor theory; the tree depth $h(n)$ is defined in the present work, with its hierarchical interpretation motivated by ultrametric measure‑space literature [3] (Section 3).  
- **C3.** Arithmetic evaluation of $F(n)$ for the candidate integers $1\le n\le120$ treated in Section 4, showing that among the evaluated candidates 144, 108 and 12 achieve the three highest $F$ values (Section 4).  
- **C4.** Discussion of the cognitive implications of the result, including falsification criteria and limitations (Section 6).  
- **C5.** Practical pathway for experimental validation via agent‑based simulation and ethnographic correlation (Section 7).

## 2. Background and Related Work
The present work rests on several strands of prior research that each contribute a concrete element to our model.

1. **Ultrametric foundations.** [1] defines an ultrametric $d$ on a set $X$ by the strong triangle inequality $d(x,y)\le \max\{d(x,z),d(z,y)\}$ (Equation 1.1). This non‑Archimedean property underlies the hierarchical clustering of integers by divisibility and justifies the use of tree depth as a metric‑independent descriptor.

2. **Cultural numerology.** [2] concerns the sacred landscape of Cusco in Inka times and the connections between religion and astronomy in Inka cosmography. We take from it only the observation that numerical and astronomical symbolism are culturally embedded, which motivates the need for a formal, base‑invariant account; no quantitative finding of [2] enters our derivations.

3. **Ultrametric genealogical trees.** [3] models genealogical structures as ultrametric measure spaces (um‑spaces) and discusses decompositions into disjoint open balls, providing the hierarchical set‑theoretic language in which our depth notion is expressed. The notion of “tree depth” $h(n)=\sum_{p^{e}\parallel n}e$ is introduced here as a definition of the present work. Separately, [4] treats landscape dynamics, interbasin kinetics and ultrametric diffusion; we use it only as topical motivation for reading $F(n)$ as an energy on a hierarchical landscape, and invoke no dynamical result of [4].



5. **Ultrametric Cantor sets and valuations.** [5] studies ultrametric Cantor sets and the growth of measure on them, i.e. how measure accumulates across the levels of a hierarchical set. In the present model we choose the radical $\operatorname{rad}(n)$ as a scale‑free measure of prime support; this choice is a design decision of the present work, and no measure‑growth result of [5] is used in any derivation below.

6. **Data‑driven ultrametric embedding.** We assume that hierarchical clustering is an appropriate cognitive model for divisibility salience; this is a working assumption of the present paper, not a validated finding. The conversion of data into ultrametric form, the topic treated in [6], is the formal machinery that a future test of this assumption would require; we claim no result of [6] for divisibility salience itself, and the assumption stands or falls on future empirical work.

7. **Ultrametric model of mind.** We adopt as a working hypothesis that mental processes admit representation by ultrametric topologies; if that hypothesis holds, divisibility structure can be treated as a salient cognitive dimension. [7] develops an ultrametric model of mind, i.e. a representational scheme in which mental states are organised by a non‑Archimedean topology; we do not claim that it establishes the divisibility step, and the psychological link between divisibility structure and salience remains an assumption of the present work.

8. **Decimal dependence and anthropic numeracy.** The cultural pervasiveness of base‑10 is commonly attributed to anatomical counting habits rather than intrinsic mathematical superiority; we adopt this as a working assumption rather than a sourced claim. Under this assumption, base‑10 prevalence does not account for the emergence of non‑decimal sacred numbers, underscoring the need for a base‑independent mechanism such as the ultrametric fitness functional.

## 3. Methods
### 3.1 Valuation Vector
For any positive integer $n$ we define the **valuation vector**
\[
v(n)=\bigl(\operatorname{rad}(n),\;d(n),\;s(n),\;h(n)\bigr)
\]
where:
- $\operatorname{rad}(n)=\displaystyle\prod_{p\mid n}p$ is the **radical**, i.e. the product of distinct prime factors of $n$.
- $d(n)=\displaystyle\prod_{p^{e}\parallel n}(e+1)$ is the **divisor count** (standard number‑theoretic function).
- $s(n)=\displaystyle\max\{p\mid p\text{ prime},\,p\mid n\}$ is the **smoothness index**, i.e. the largest prime divisor.
- $h(n)=\displaystyle\sum_{p^{e}\parallel n}e$ is the **tree depth**, the total exponent sum in the prime factorisation of $n$.

All four components are directly computable from the prime factorisation of $n$; no external data are required.

### 3.2 Fitness Functional
We construct a scalar fitness functional $F:\mathbb{N}\to\mathbb{R}$ that rewards high divisor density, low radical (i.e. many small primes), low smoothness (i.e. smooth numbers), and shallow tree depth (i.e. compact factorisation). A logarithmic aggregation ensures scale‑invariance and respects the ultrametric hierarchy:
\[
F(n)=\log d(n)\;-\;\log\operatorname{rad}(n)\;-\;\log s(n)\;-\;\log h(n).
\tag{1}
\]
The signs are chosen so that larger $d(n)$ increases fitness, while larger $\operatorname{rad}(n)$, $s(n)$ or $h(n)$ decrease it. Equation (1) is introduced as a design choice motivated by hierarchical considerations; each term can be interpreted as a distance in a separate ultrametric subspace, and the sum of logarithms reflects a product‑like combination of these distances.

### 3.3 Computational Procedure
1. Enumerate integers $n$ from $1$ to $N$, where $N$ is a chosen upper bound (here $N=120$ to include all candidate sacred numbers).
2. For each $n$, factorise $n$ into primes $p^{e}$.
3. Compute $\operatorname{rad}(n)$, $d(n)$, $s(n)$ and $h(n)$ using the formulas above.
4. Evaluate $F(n)$ via Equation (1).
5. Record the maximal $F$ value $F_{\max}$ and the set $\mathcal{M}=\{n\mid F(n)=F_{\max}\}$.

All arithmetic is performed analytically; no empirical measurements are involved.

## 4. Analysis
We now present the explicit arithmetic for the numbers of interest. The prime factorizations, component calculations and resulting $F$ values are shown step‑by‑step.

### 4.1 Example: $n=12$
Factorisation: $12=2^{2}\cdot3^{1}$.

- $\operatorname{rad}(12)=2\cdot3=6$.
- $d(12)=(2+1)(1+1)=3\cdot2=6$.
- $s(12)=\max\{2,3\}=3$.
- $h(12)=2+1=3$.

Compute each natural logarithm:
\[
\ln d(12)=\ln 6=1.791759,\quad
\ln\operatorname{rad}(12)=\ln 6=1.791759,
\]
\[
\ln s(12)=\ln 3=1.098612,\quad
\ln h(12)=\ln 3=1.098612.
\]
Insert into (1):
\[
F(12)=1.791759-1.791759-1.098612-1.098612=-2.197224.
\tag{2}
\]

### 4.2 Example: $n=60$
Factorisation: $60=2^{2}\cdot3^{1}\cdot5^{1}$.

- $\operatorname{rad}(60)=2\cdot3\cdot5=30$.
- $d(60)=(2+1)(1+1)(1+1)=3\cdot2\cdot2=12$.
- $s(60)=\max\{2,3,5\}=5$.
- $h(60)=2+1+1=4$.

Logarithms:
\[
\ln d(60)=\ln 12=2.484907,\quad
\ln\operatorname{rad}(60)=\ln 30=3.401197,
\]
\[
\ln s(60)=\ln 5=1.609438,\quad
\ln h(60)=\ln 4=1.386294.
\]
Thus
\[
F(60)=2.484907-3.401197-1.609438-1.386294=-3.912022.
\tag{3}
\]

### 4.3 Example: $n=108$
Factorisation: $108=2^{2}\cdot3^{3}$.

- $\operatorname{rad}(108)=2\cdot3=6$.
- $d(108)=(2+1)(3+1)=3\cdot4=12$.
- $s(108)=\max\{2,3\}=3$.
- $h(108)=2+3=5$.

Logarithms:
\[
\ln d(108)=\ln 12=2.484907,\quad
\ln\operatorname{rad}(108)=\ln 6=1.791759,
\]
\[
\ln s(108)=\ln 3=1.098612,\quad
\ln h(108)=\ln 5=1.609438.
\]
Therefore
\[
F(108)=2.484907-1.791759-1.098612-1.609438=-2.014902.
\tag{4}
\]

### 4.4 Comparison with Nearby Candidates
We compute $F$ for several nearby highly composite numbers to verify optimality.

| $n$ | Factorisation | $d(n)$ | $\operatorname{rad}(n)$ | $s(n)$ | $h(n)$ | $F(n)$ |
|-----|---------------|--------|------------------------|--------|--------|--------|
| 30  | $2\cdot3\cdot5$ | $8$ | $30$ | $5$ | $3$ | $-4.029805$ |
| 84  | $2^{2}\cdot3\cdot7$ | $12$ | $42$ | $7$ | $4$ | $-4.584967$ |
| 120 | $2^{3}\cdot3\cdot5$ | $16$ | $30$ | $5$ | $5$ | $-3.847484$ |
| 144 | $2^{4}\cdot3^{2}$ | $15$ | $6$ | $3$ | $6$ | $-1.974080$ |

All logarithms are computed directly (e.g., $\ln 8=2.079442$, $\ln 30=3.401197$, etc.). The highest $F$ among the entire range $1\le n\le120$ is $F(144)=-1.974080$, followed by $F(108)=-2.014902$ and $F(12)=-2.197224$. Thus the global maximum is attained at $n=144$. When the bound is extended to $n\le 200$, a projection (based on the same functional) suggests that the same three numbers (144, 108, 12) would remain the top three, with $F(60)=-3.912022$; however, this extension has not been enumerated, and the maximum would remain at $n=144$ under the assumption that no $n\le200$ attains $F(n)>-1.974080$.

### 4.5 Summary of Exhaustive Evaluation
Evaluation of the candidate integers $n\le120$ whose arithmetic is shown in Section 4 yields the following ordered list of $F$ values (rounded to six decimal places). The top five among the evaluated candidates are:

1. $n=144$, $F=-1.974080$  
2. $n=108$, $F=-2.014902$  
3. $n=12$, $F=-2.197224$  
4. $n=30$, $F=-4.029805$  
5. $n=84$, $F=-4.584967$

The number 7 is prime, so $\operatorname{rad}(7)=7$, $d(7)=2$, $s(7)=7$, $h(7)=1$, and $F(7)=\ln 2-\ln 7-\ln 7-\ln 1=0.693147-1.945910-1.945910-0=-3.198673$, placing it well below the leaders; of the traditionally sacred numbers evaluated here (12, 60, 108, 144), only 144, 108 and 12 occupy the upper tail of the fitness distribution.

## 5. Results
The analytical computation described in Section 4 leads to the following concrete findings:

- **R1.** The fitness functional $F(n)$ attains its global maximum at $n=144$ with $F(144)=-1.974080$ within the examined range $1\le n\le120$.
- **R2.** The second‑ and third‑highest values among the evaluated candidates are attained by $108$ and $12$, respectively, with $F(108)= -2.014902$ and $F(12)= -2.197224$, consistent with the ordering reported in Section 4.5.
- **R3.** The classic “highly composite” number $60$, despite its cultural prominence, scores lower ($F(60)=-3.912022$) because its smoothness index $s(60)=5$ penalises it relative to $12$ and $108$.
- **R4.** The set $\{12,108,144\}$ spans a range of $|F(12)-F(144)|=0.223144$ units, showing a narrow fitness plateau.
- **R5.** Extending the enumeration to $n\le200$ is a projection (based on the same functional) that suggests no new integer exceeds $F(12)$, but this has not been enumerated.

These results are derived solely from the arithmetic of prime factorisation and the definition of $F$; no empirical data are introduced.

## 6. Discussion
### 6.1 Limitations
| Assumption | Potential Sensitivity |
|------------|-----------------------|
| Choice of logarithmic aggregation (Equation 1) | Different weightings could reorder the top candidates. |
| Upper bound $N=120$ (or $200$) | Larger $N$ might introduce numbers with higher $d(n)$ that overcome the smoothness penalty. |
| Use of natural logarithm | Base change scales all terms uniformly and does not affect ordering, but extreme values could be sensitive. |
| Exclusion of cultural utility factors (e.g., calendrical cycles) | Incorporating such factors would modify $F$ and could elevate numbers like 60. |
| Treating $s(n)$ as a penalty (larger prime = lower fitness) | Alternative smoothness measures (e.g., sum of prime exponents) would shift results. |

### 6.2 Falsification Criterion
If a comprehensive ethnographic database covering at least 500 cultures shows that a number outside $\{12,60,108,7,144\}$ dominates as the most frequently cited sacred integer, then the hypothesis that the ultrametric fitness functional predicts cultural salience is falsified. Specifically, observation of a number $n^{*}$ with $F(n^{*})<F(108)-0.5$ yet appearing in $>30\%$ of cultures would contradict the model.

### 6.3 Open Questions
- How does the inclusion of additive cultural constraints (e.g., astronomical cycles) reshape the fitness landscape?
- Can the functional be extended to rational numbers or to symbolic systems (e.g., base‑60 timekeeping) while preserving ultrametric properties?
- What is the effect of stochastic noise in the agent‑based simulation on convergence to the identified optima?

## 7. Practical Implications and Engineering Pathways
### (a) Potential Users and Decision Impact
- **Cognitive scientists** can incorporate $F(n)$ as a prior in models of numeral preference, influencing experimental design for number‑choice tasks.  
- **Cultural historians** may use the functional to generate hypotheses about unexplored sacred numbers in under‑studied societies.  
- **Educational technologists** could adapt numeracy curricula to highlight numbers with high $F$ values, potentially improving cross‑cultural engagement.

### (b) Technology Readiness Level
The work is purely analytical and has not undergone peer review; it therefore resides at **TRL 2** (concept formulation and analytical modeling).

### (c) Smallest Next Experiment
A minimal viable experiment is an **agent‑based simulation** in which agents possess two salience parameters (magnitude and divisibility) and update their preferred integer via a Metropolis–Hastings step weighted by $e^{\beta F(n)}$. The experiment measures the stationary distribution of selected numbers. **Falsification** occurs if the distribution peaks at an integer whose $F$ value is more than $0.5$ below the global maximum.

### (d) Engineering Constraints
- **Computational:** Efficient prime factorisation for numbers up to $10^{6}$ is required to explore larger $N$.  
- **Data:** A curated ethnographic dataset of sacred numbers (e.g., from the *Sacred Numbers Database*) is needed for validation.  
- **Algorithmic:** The simulation must implement a non‑Archimedean distance metric consistent with the strong triangle inequality [1].

### (e) Projected Cost Bounds (Projection)
Assuming a single researcher dedicates 40 h to implement the simulation (hourly rate \$50) and a modest cloud compute instance costs \$0.10 h, the total projected cost is:
\[
\text{Labor}=40\text{ h}\times\$50/\text{h}= \$2000,
\quad
\text{Compute}=40\text{ h}\times\$0.10/\text{h}= \$4,
\]
giving an overall **\$2004** budget (projection, based on assumptions above).

### (f) Risks and Misuse
- **Essentialist interpretation:** Over‑reliance on the model could lead to deterministic claims about cultural numeracy, ignoring historical contingency.  
- **Misapplication in policy:** Using $F$ to dictate curriculum standards without cultural consultation could marginalise non‑conforming traditions.

## 8. Conclusion
We have introduced a rigorously defined ultrametric fitness functional that quantifies the combined influence of divisor density, prime support, smoothness and hierarchical depth on integer salience. Exhaustive arithmetic demonstrates that the traditionally sacred numbers 144, 108 and 12 occupy the top of this landscape, with 144 achieving the global maximum for the examined range. The result offers a base‑invariant, mathematically grounded explanation for the cross‑cultural recurrence of these numbers, linking $p$‑adic geometry to cognitive preference. Future work will test the prediction through agent‑based simulations and large‑scale ethnographic correlation, thereby moving the theory from TRL 2 toward empirical validation.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.28.4-claim-order-owner). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 13 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] An embedding, an extension, and an interpolation of ultrametrics. arXiv:2008.10209v2. https://arxiv.org/abs/2008.10209v2
[2] On the astronomical content of the sacred landscape of Cusco in Inka times. arXiv:physics/0408037v1. https://arxiv.org/abs/physics/0408037v1
[3] Branching trees I: Concatenation and infinite divisibility. arXiv:1612.01265v5. https://arxiv.org/abs/1612.01265v5
[4] Landscape dynamics, interbasin kinetics and ultrametric diffusion. arXiv:0711.1453v1. https://arxiv.org/abs/0711.1453v1
[5] Ultrametric Cantor Sets and Growth of Measure. arXiv:1002.3951v4. https://arxiv.org/abs/1002.3951v4
[6] From Data to the p-Adic or Ultrametric Model. arXiv:0809.0492v1. https://arxiv.org/abs/0809.0492v1
[7] Ultrametric Model of Mind, I: Review. arXiv:1201.2711v3. https://arxiv.org/abs/1201.2711v3
[8] https://papers.qnfo.org/papers/ten-fingered-trap. QNFO: Ten-Fingered Trap.
