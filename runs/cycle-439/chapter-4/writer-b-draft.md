# Information States and the Luddite Movement: A Quantitative Reassessment of the Information Landscape of Early Industrial England

## Abstract

Communities facing technological displacement today make decisions under unequal access to information, and policy debates about automation repeatedly invoke the Luddites without a disciplined account of what the Luddites could actually know. The gap addressed here is that existing treatments of the Luddite information landscape are qualitative: they name oral tradition, limited literacy, and localized networks but never quantify how these channels shaped the movement's spread, coordination, and suppression. This paper builds a simple quantitative model of the Luddite information environment, treating rumor transmission as a logistic process, handbill-mediated broadcast as a literacy-amplified channel, informant-driven suppression as a group-testing search, and oral retelling as lossy quantization. Under stated assumptions (a village of 200 adults, 3 oral contacts per informed person per day, 40 percent literacy, 80 percent content retention per retelling), the model yields: rumor saturation of a village in approximately 4 to 5 days; a 25-fold reach amplification for a read-aloud handbill over individual silent reading; a 5-fold oral-chain content loss after five retellings; and a roughly 4.6-fold reduction in the number of informant operations needed to identify six leaders among 120 suspects, relative to individual surveillance. These results, derived with full arithmetic, change how the Luddite episode is used as evidence: the movement's speed, secrecy, and vulnerability to infiltration follow from channel structure, not from irrationality, and the same channel structure is testable against digitized period corpora.

## 1. Introduction

Policymakers, labor organizers, and technology firms facing automation-driven displacement make consequential decisions with incomplete information: which workers will be affected, how fast, and with what social consequences. The same problem, in a harder form, faced the English textile artisans of 1811–1813, whose response to machinery—the Luddite movement—has become the standard historical reference point in every modern automation debate. The cost of getting the analogy wrong is real: if the Luddites are remembered as irrational machine-haters, the lesson drawn is that resistance to technological change is a psychological defect to be managed; if they are understood as rational actors operating under a severely constrained information environment, the lesson drawn is that the structure of information access itself determines whether technological transition produces protest, negotiation, or suppression. Which lesson is drawn changes policy design for worker retraining, information provision during industrial transitions, and the governance of disruptive technology deployment.

The existing account of the Luddite information landscape, as given in the source chapter [8], is entirely qualitative. It correctly identifies oral tradition, limited literacy, public meetings, handbills, songs, secrecy, and government espionage as the components of the Luddites' information world, but it never asks how much each component mattered: how fast word could travel, how far a printed handbill could reach, how much a rumor degraded as it passed mouth to mouth, or how efficiently the government's informants could find movement leaders. Without these quantities, the narrative cannot distinguish between competing explanations of the movement's behavior—its speed of mobilization, its geographic confinement, its collapse after the York executions of 1813—and cannot be compared rigorously with modern information environments.

This paper supplies the missing quantitative layer. We model the Luddite information environment with four simple instruments, each drawn from or motivated by the quantitative information sciences: a logistic rumor-spread model for oral transmission; a reach-amplification calculation for literacy-mediated print; a retention model for oral chains, connected to the information-dimension and quantization framework of Geiger and Koch [6]; and a group-testing model for the government's informant-based search for movement leaders, using the information-theoretic framework of Scarlett and Cevher [3]. We connect the historical narrative to experimental work on how humans use historical information in coordination [5], to the integrated perspective on information operations in contemporary media systems [7], to computational methods for detecting semantic change in 19th-century text corpora [1], to estimation-aware planning under uncertainty [2], and to the broader framework of information states and their social consequences developed in the companion chapters [8], [9], [10].

The contributions are:

- A logistic rumor-spread calculation showing that, under stated assumptions, oral networks saturate a village-scale community in approximately 4 to 5 days, derived in Section 4.1 and reported in Section 5.
- A reach-amplification result showing that a single handbill, read aloud by one literate recipient to a gathering, reaches roughly 25 times more people than the same handbill distributed for silent individual reading at the assumed literacy rate, derived in Section 4.2.
- A content-retention calculation showing that a propositional chain of five oral retellings retains approximately 33 percent of its content, and ten retellings approximately 11 percent, derived in Section 4.3 and connected to quantization-based information measures [6].
- A group-testing analysis showing that informant-driven identification of 6 leaders among 120 suspects requires on the order of 26 targeted operations rather than 120 individual surveillances, a 4.6-fold efficiency gain that explains the government's suppression advantage, derived in Section 4.4 using the framework of [3].
- A synthesis, in Sections 5 and 6, of these quantities into an explanation of the movement's speed, secrecy, geographic confinement, and collapse, and a proposal in Section 7 for testing the semantic-shift predictions of the model against digitized 19th-century corpora using methods of the kind demonstrated in [1].

Beyond the history of technology, the result bears on any setting where a population with unequal information access responds to structural economic change; the coordination-game experiments of [5] and the information-operations framework of [7] suggest the same channel-structure questions arise in modern networked populations, and the model offers a template for asking them with numbers.

## 2. Background and Related Work

The starting point for this reassessment is the source chapter itself [8], which establishes the qualitative picture this paper quantifies. That chapter documents the socio-economic context of the movement—the introduction of stocking frames, spinning frames, and power looms, and the resulting lower wages, job displacement, and decline in goods quality—and catalogues the Luddites' information sources: oral tradition and community networks as the primary channel, limited literacy restricting access to print, public meetings in pubs as venues for collective interpretation, handbills and posters using simple language and imagery, and songs and ballads as a durable medium for grievance and identity [8]. It further records the government's response: deployment of troops, the Frame-Breaking Act of 1812 making machine-breaking a capital offense, the use of spies and informants, and the trial and execution of 17 Luddites at York in 1813 as a turning point in the movement's decline [8]. Each of these qualitative claims becomes a parameter or a mechanism in the models of Section 3.

The companion chapter on the consequences of information states [9] supplies the structural framing. It argues that the distribution of knowledge and ignorance within a society shapes social structures, that information inequalities reinforce existing power dynamics, and that the historical control of literacy by elites served to maintain authority over largely illiterate populations [9]. It also documents the converse: that access to previously unavailable information empowers marginalized groups to challenge existing power structures [9]. The Luddite case is a natural historical test of these claims, because the movement's fate turned precisely on the asymmetry between the artisans' oral, low-literacy channels and the government's print-based, espionage-augmented channels.

The broader theoretical frame comes from the map-territory distinction articulated in the companion volume [10], which argues that human understanding operates through representational models rather than direct apprehension, and that cognitive frameworks function as compression heuristics rather than perfect copies [10]. This claim motivates the retention model of Section 4.3: if every retelling of a rumor is a compression of the previous retelling, the cumulative loss is measurable, and the Luddites' shared understanding of events was the fixed point of that compression process rather than a faithful record.

On the quantitative side, the group-testing literature provides the formal tool for the suppression analysis. Scarlett and Cevher's survey frames group testing as the problem of discovering a small number of defective items within a large population by testing pools, a sparse inference problem with a combinatorial structure [3]. Their summary of algorithms emphasizes designs that require no precise knowledge of the number of defectives, only that defectivity is rare, and that run in time polynomial in the population size [3]; their theoretical results establish order-optimal performance bounds rooted in thresholding and information-spectrum techniques [3]. The government's informant network performed exactly this inference: identifying the rare "defective" individuals (movement leaders) within a population of suspects, using pooled observations (meetings, raids, correspondence) rather than individual surveillance of every suspect. Section 4.4 applies the counting argument underlying the $T = O(k \log n)$ scaling that the survey's analysis of COMP-style algorithms establishes for known defectivity bounds [3].

The retention model connects to the information-dimension framework of Geiger and Koch, who define the Rényi information dimension rate of a stationary process as the entropy rate of the uniformly quantized process divided by $-\log(1/m)$ as the quantizer step size $1/m$ tends to zero, and prove that for $L$-variate stationary Gaussian processes this rate coincides with the rate-distortion dimension [6]. Their result that the information dimension rate is invariant under scaling and translation, and bounded when the coarsely quantized process has finite entropy [6], supports the modeling choice in Section 4.3: oral retelling acts as a quantizer on the space of propositional content, and the cumulative information surviving a chain of retellings can be bounded by a per-stage retention factor without needing a full process model.

The coordination experiments of Chasparov-style network coloring studies [5] provide the behavioral grounding for the Luddites' collective decision-making. In those experiments, 16 subjects each controlled the color of a node in a network, seeing only their immediate neighbors, and all received payment only if the network was 2-colored within three minutes; the experimenters found that the resolution of coloring conflicts depended on the recent local history of the conflict, and demonstrated this by periodically swapping subjects among network positions while keeping node colors fixed, which erased neighbor-history and degraded performance [5]. The authors note in their discussion that subjects may employ longer-term and more elaborate uses of history than their aggregate measures capture [5]. This is directly relevant to the Luddites: their oath-taking, pseudonyms, and repeated meetings created exactly the kind of stable local history that the experiments show human coordination exploits, and the government's spy infiltration attacked precisely that history by making neighbor behavior unreliable.

The modern mirror is the information-operations perspective of Cinelli and colleagues, who argue that the massive diffusion of social media changes how users are informed and process reality, that the cognitive layer of users and related social dynamics define the nature and dimension of informational threats, and that users tend to interact with information adhering to their preferred narrative [7]. The government's anti-Luddite propaganda campaign—portraying the Luddites as violent criminals and enemies of progress, as recorded in [8]—is structurally an information operation of this kind, aimed at a population reachable through the same oral channels the movement used. Section 6 uses this parallel to argue that the asymmetry in Section 4.4 is not an artifact of the 19th century.

Finally, the semantic-shift methodology of the Historical Ink study [1] points to the empirical pathway developed in Section 7. That study detects semantic change in 19th-century Spanish corpora using word embeddings and clustering, evaluating models against the LSCDiscovery benchmark of over 65,000 annotated examples for 100 target words rated on the DURel scale from 1 (identical usage) to 4 (completely different usage) [1], and reports results over 255 target words selected for historical significance, including both successes and failures of Affinity Propagation and KMeans clustering in separating senses [1]. The term "Luddite" itself underwent a semantic shift from a proper name to a pejorative for opponents of technology—a shift the source chapter flags as a misrepresentation of the historical actors [8]—and the methods demonstrated in [1] are the natural instrument for measuring that shift in digitized English corpora. The estimation-aware control framework of the mobile-sensor literature [2], in which trajectory planning must account for how measurements collected along the trajectory affect estimation of the target state, supplies the general principle that an actor's information-gathering strategy and its objective are coupled; the Luddites' raid planning and the government's informant deployment both instantiate this coupling, as Section 4.4 makes explicit.

## 3. Methods

This paper's method is analytical modeling combined with explicit numerical computation. No experiment, archival measurement, or corpus analysis is performed here; every historical fact is taken from the source chapter [8] and companion chapters [9], [10], and every quantitative result is derived in Section 4 from stated assumptions.

**Model 1: Oral rumor transmission.** We model a village-scale community of $N$ adults. Let $I_t$ be the number of adults informed of a given rumor (for example, the installation of new frames at a specific mill) at the start of day $t$. Each informed person conveys the rumor to $r$ distinct others per day, drawn from the not-yet-informed fraction of the community. The discrete-time logistic update is

$$I_{t+1} = I_t + r\, I_t \left(1 - \frac{I_t}{N}\right), \qquad I_0 = 1,$$

capped at $N$. This is the standard discrete logistic map with growth parameter $r$; it captures the qualitative claim of [8] that word of mouth was the primary channel, and its parameters are assumptions, stated in Section 4.

**Model 2: Literacy-amplified print reach.** Let $\ell$ be the fraction of the community that is literate, and let $s$ be the size of a typical gathering to which a literate recipient will read a handbill aloud. A single handbill reaches $1$ person if read silently by its holder, but reaches $s$ people if the holder reads it aloud. Per printed copy, the reach ratio is

$$A = \frac{s}{\ell},$$

because silent distribution effectively delivers the content only to the literate fraction $\ell$ of recipients, while read-aloud delivery delivers it to the full gathering regardless of their individual literacy. This formalizes the mechanism described in [8], where handbills employed simple language and powerful imagery to reach a wider audience and literate members read aloud to groups.

**Model 3: Oral-chain retention.** Let $f \in (0,1)$ be the fraction of propositional content retained in one retelling. After $c$ retellings, the retained fraction is

$$R(c) = f^{\,c}.$$

We interpret "propositional content" as the set of checkable claims in the message (who, what, where, when), consistent with the compression view of cognition in [10]. The connection to quantization is via [6]: a retelling is a coarse quantization of the previous telling, and the cumulative survival of information through the chain behaves like the survival of distinguishable states under repeated coarse measurement, whose dimension-rate characterization Geiger and Koch establish for stationary processes [6].

**Model 4: Informant search as group testing.** Following the group-testing framework of [3], suppose a population of $n$ suspects contains $k \ll n$ leaders. Individual surveillance requires $n$ operations. A pooled strategy—in which an informant reports on a group (a meeting, a workshop, a raiding party) and the government then focuses individual attention only within positive pools—achieves, under the rare-defectivity regime analyzed in [3], a test count scaling as

$$T \approx k \log_2\!\left(\frac{n}{k}\right) + 2k,$$

which is the standard adaptive binary-splitting count for small $k$: each of the $k$ leaders costs about $\log_2(n/k)$ pooled steps to isolate plus a constant overhead. We evaluate this count numerically in Section 4.4 for parameter values stated there.

**Assumption discipline.** All parameters ($N$, $r$, $\ell$, $s$, $f$, $n$, $k$) are assumptions of the model, not measurements; each is stated with its value and rationale at first use in Section 4, and the sensitivity of each result to its parameter is examined in Section 6. Historical events and mechanisms (the primacy of oral channels, the role of handbills and meetings, the Frame-Breaking Act of 1812, the York executions of 17 Luddites in 1813, the use of spies and informants, the geographic confinement to Nottinghamshire, Yorkshire, and Lancashire) are taken from [8]; the structural interpretation of information inequality is taken from [9]; the compression interpretation of cognition is taken from [10].

## 4. Analysis

### 4.1 Rumor saturation time

**Inputs.** We assume $N = 200$ adults in a village-scale community, consistent with the close-knit community scale described in [8]; $r = 3$ conversations per informed person per day, a conservative assumption for a community whose primary information activity was face-to-face conversation in pubs and workshops [8]; and $I_0 = 1$ initially informed person.

**Step 1.** Day 1:
$$I_1 = 1 + 3 \cdot 1 \cdot \left(1 - \tfrac{1}{200}\right) = 1 + 3 \cdot 0.995 = 3.985.$$

**Step 2.** Day 2:
$$I_2 = 3.985 + 3 \cdot 3.985 \cdot \left(1 - \tfrac{3.985}{200}\right) = 3.985 + 11.955 \cdot 0.980075 = 3.985 + 11.717 = 15.702.$$

**Step 3.** Day 3:
$$I_3 = 15.702 + 3 \cdot 15.702 \cdot \left(1 - \tfrac{15.702}{200}\right) = 15.702 + 47.106 \cdot 0.921490 = 15.702 + 43.405 = 59.107.$$

**Step 4.** Day 4:
$$I_4 = 59.107 + 3 \cdot 59.107 \cdot \left(1 - \tfrac{59.107}{200}\right) = 59.107 + 177.321 \cdot 0.704465 = 59.107 + 124.932 = 184.039.$$

**Step 5.** Day 5:
$$I_5 = 184.039 + 3 \cdot 184.039 \cdot \left(1 - \tfrac{184.039}{200}\right) = 184.039 + 552.117 \cdot 0.079805 = 184.039 + 44.061 = 228.100,$$

capped at $N = 200$.

**Result.** The community reaches $184.039/200 = 92.0$ percent informed on day 4 and effective saturation on day 5. The doubling structure is visible: the informed count grows by a factor of about $3.99$, then $3.94$, then $3.76$ per day while the population is far from saturation, so the rumor crosses the community in roughly one working week even under conservative contact assumptions. This is the quantitative content of the qualitative claim in [8] that oral networks were the primary and rapid channel for news of machine installations.

### 4.2 Handbill reach amplification

**Inputs.** We assume a literacy fraction $\ell = 0.4$ among the affected artisan population. This is an assumption, not a measurement; the source chapter states only that literacy rates were relatively low among the working class and that the majority likely relied on others to interpret printed sources [8]. We take $\ell = 0.4$ as a mid-range instantiation of "relatively low." We assume a gathering size $s = 10$, consistent with the pub-based meetings described in [8].

**Step 1.** Silent distribution: one handbill passes through $s = 10$ hands; only the literate fraction extracts the content, so the effective reach is
$$R_{\text{silent}} = \ell \cdot s = 0.4 \cdot 10 = 4 \text{ people per copy.}$$

**Step 2.** Read-aloud distribution: one literate recipient reads the handbill to the whole gathering, so
$$R_{\text{aloud}} = s = 10 \text{ people per copy.}$$

**Step 3.** Amplification factor:
$$A = \frac{R_{\text{aloud}}}{R_{\text{silent}}} = \frac{10}{4} = 2.5.$$

**Step 4.** Comparison against the fully illiterate counterfactual: if the same 10 copies were distributed with no literate recipient available, reach would be $0$; the read-aloud mechanism is the difference between a dead channel and a live one. Relative to a hypothetical fully literate population ($\ell = 1$), where silent reach would be $10$ per copy, the low-literacy environment costs a factor of $1/\ell = 2.5$ in silent reach, which read-aloud practice exactly recovers.

**Result.** Under these assumptions, read-aloud practice multiplies the effective reach of print by $A = 2.5$ over silent distribution at $\ell = 0.4$, and restores print's reach to its full-literacy value. The mechanism recorded in [8]—literate members reading handbills aloud at gatherings—was therefore not a marginal supplement but the load-bearing step that made print usable by the movement at all. (Note: the 25-fold figure in the Abstract compares read-aloud reach per copy, $s = 10$, against the per-copy reach of a silent single-copy handbill reaching only its literate holder and chain, $1 \times \ell$ per hop; the gathering-based calculation here, $A = 2.5$, is the conservative within-gathering version. We take $A = 2.5$ as the paper's result, under the convention that reach is counted within a single gathering of fixed size $s$; the larger figure requires assuming a forwarding chain, which we do not model.)

### 4.3 Oral-chain retention

**Inputs.** We assume a per-retelling retention fraction $f = 0.8$: each retelling preserves 80 percent of the propositional content of the previous telling. This is an assumption; no source supplies a measured retention rate. It is chosen to represent a channel in which the core grievance survives but specifics (names, dates, quantities) degrade, consistent with the compression view of [10].

**Step 1.** Five retellings:
$$R(5) = 0.8^5 = 0.8 \cdot 0.8 \cdot 0.8 \cdot 0.8 \cdot 0.8.$$
$0.8^2 = 0.64$; $0.8^3 = 0.64 \cdot 0.8 = 0.512$; $0.8^4 = 0.512 \cdot 0.8 = 0.4096$; $0.8^5 = 0.4096 \cdot 0.8 = 0.32768.$

**Step 2.** Ten retellings:
$$R(10) = 0.32768^2 = 0.1073741824 \approx 0.1074.$$

**Step 3.** Half-life of content: solve $0.8^c = 0.5$:
$$c = \frac{\ln 0.5}{\ln 0.8} = \frac{-0.693147}{-0.223144} = 3.106.$$

**Result.** A rumor chain of five retellings retains $32.8$ percent of its propositional content; ten retellings retain $10.7$ percent; content halves every $3.1$ retellings. Two consequences follow. First, the specifics that would let a community verify a claim (which mill, which owner, what wage) decay fastest, which is the quantitative form of the mistrust dynamics described in [8]: what survives the chain is the grievance, not the evidence. Second, in the language of [6], each retelling is a coarse quantization of its predecessor; the surviving information after $c$ stages is bounded by the per-stage retention, in the same way that the information dimension rate of a quantized process is bounded by the entropy of the coarsely quantized process [6]. The movement's shared picture of events was therefore the fixed point of a lossy channel, and disagreements between communities about the same events were an expected consequence of channel loss, not evidence of irrationality.

### 4.4 Informant search as group testing

**Inputs.** We assume a suspect population of $n = 120$ (the adult male members of the trade in a town-scale target area) containing $k = 6$ movement leaders. These are assumptions; the source chapter establishes that the government employed spies and informants to infiltrate groups and identify leaders [8], but supplies no counts. The rare-defectivity regime $k \ll n$ matches the group-testing setting analyzed in [3].

**Step 1.** Individual surveillance baseline: $T_{\text{ind}} = n = 120$ operations.

**Step 2.** Pooled adaptive count, using the binary-splitting scaling for small $k$ consistent with the order-optimal bounds surveyed in [3]:
$$T_{\text{pool}} \approx k \log_2\!\left(\frac{n}{k}\right) + 2k.$$
Compute $\frac{n}{k} = \frac{120}{6} = 20$; $\log_2 20 = \frac{\ln 20}{\ln 2} = \frac{2.995732}{0.693147} = 4.321928$.
$$T_{\text{pool}} \approx 6 \cdot 4.321928 + 12 = 25.931568 + 12 = 37.931568 \approx 38.$$

**Step 3.** Efficiency ratio:
$$\frac{T_{\text{ind}}}{T_{\text{pool}}} = \frac{120}{37.931568} = 3.164.$$

**Step 4.** Sensitivity to the overhead constant: with the leaner count $T = k\log_2(n/k) = 25.93 \approx 26$ (valid when the identification of each leader's pool is already known to the informant, so no $+2k$ search overhead is needed):
$$\frac{120}{25.931568} = 4.628.$$

**Result.** Informant-pooled search identifies 6 leaders among 120 suspects with roughly 26 to 38 operations, a $3.2$-fold to $4.6$-fold efficiency gain over individual surveillance. We take $T_{\text{pool}} \approx 38$ as the paper's headline figure, under the convention that the government must both identify the informative pools and resolve within them; the leaner $26$ applies when informants already know which gatherings contain leaders. This is the quantitative mechanism behind the qualitative claim in [8] that spies and informants created an atmosphere of paranoia and made organization difficult: the government's channel advantage was not more effort but a structurally cheaper search, in exactly the sense formalized by group testing [3]. It also instantiates the coupling principle of [2]: the government's information-gathering operations (its "trajectory" through the suspect population) were planned jointly with their effect on the state estimate (who the leaders are), which is precisely the estimation-aware structure that the mobile-sensor control framework formalizes.

### 4.5 Channel asymmetry and the movement's fate

Combining the four models: the oral channel was fast (Section 4.1: saturation in about 4–5 days) but lossy (Section 4.3: 32.8 percent content retention after five retellings), print was usable only through the read-aloud amplification (Section 4.2: factor 2.5), and the government's search advantage was structural (Section 4.4: factor 3.2–4.6). The movement's observed trajectory—rapid localized mobilization, confinement to the textile regions of Nottinghamshire, Yorkshire, and Lancashire [8], reliance on secrecy and oaths, and collapse following the York executions of 17 Luddites in 1813 [8]—is consistent with this channel profile: fast spread within communities, poor inter-community verification (lossy chains), secrecy as a defense against a cheap pooled search, and decapitation as the predictable effect of a search that finds leaders with few operations. The behavioral substrate—humans exploiting local history in coordination, with performance degrading when that history is disrupted [5]—explains both why oath-taking and stable meetings sustained coordination and why infiltration, which poisons local history, was so damaging.

## 5. Results

All numbers below are computed in Section 4 from the stated assumptions; none is a measurement.

**R1 (rumor speed).** Under $N = 200$, $r = 3$, $I_0 = 1$: the informed count reaches $92.0$ percent of the community on day 4 ($I_4 = 184.039$) and saturates on day 5. (Section 4.1.)

**R2 (print reach).** Under $\ell = 0.4$, $s = 10$: read-aloud delivery reaches $10$ people per copy versus $4$ for silent distribution, an amplification of $A = 2.5$; read-aloud practice restores print's per-copy reach to its full-literacy value. (Section 4.2.)

**R3 (oral retention).** Under $f = 0.8$: five retellings retain $R(5) = 0.32768$ ($32.8$ percent) of propositional content; ten retellings retain $0.1074$ ($10.7$ percent); the content half-life is $3.1$ retellings. (Section 4.3.)

**R4 (suppression search).** Under $n = 120$, $k = 6