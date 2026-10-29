# Implications for Computing and Quantum Error Correction: Remediation under Erratum pl-prime-valuation-qec-implications-v0.4-0

## Abstract

The published paper *Implications for Computing and Quantum Error Correction* (v0.4) applied the branch-depth reading of the p-adic valuation $v_p(n)$ to computing and quantum error correction, and registered eight claims C1–C8 with falsifiability conditions. Its abstract recorded that two reproduction attempts of the central empirical claim — that a rule-based Kodaira–Néron-fiber classifier assigns quantum error-correcting code families with 166/200 (83%) accuracy — "both fail to support the claim at the reported sizes." This remediation, issued under erratum pl-prime-valuation-qec-implications-v0.4-0, verifies the arithmetic of that record and consolidates its findings. We confirm by direct computation that the per-family figures 46, 39, 45, and 36 sum to 166/200 = 83%, that the separately reported 187/200 spectral-gap figure equals 93.5%, and that the sharpest valuation-only overhead bound $n/k \ge 1$ is strictly weaker than the quantum Singleton bound $n - k \ge 2(d-1)$ for every code with $d \ge 2$. The remediated status is: five claims closed (two self-corrected or rejected, three disconfirmed), one open (existence of a non-trivial valuation invariant), and the 83% claim demoted to unverified-internal pending a re-implementation from specification. What changes in practice: no valuation-based code classifier or overhead bound should be built upon until the open invariant question is resolved and the classifier is independently reproduced against a stated baseline.

## 1. Introduction

Quantum error correction (QEC) research is in a period where every proposed shortcut matters. The overhead of protecting logical qubits — the physical-to-logical qubit ratio — is the binding constraint on scalable quantum computing, and the field's failure to deliver commercially viable hardware after roughly \$35 billion of investment has been argued to be an epistemic crisis rather than merely an engineering delay [3]. In that environment, a claim that a number-theoretic invariant classifies code families at 83% accuracy, if true, would give code designers a cheap, classical screening tool for code families; if false or unverified, it diverts reproduction effort and risks propagating into registry summaries as an established result. The published paper under remediation [2] carried exactly such a claim, sourced to an internal report, and its own abstract now records that "two attempts now exist... both failing to support the claim at the reported sizes." This erratum-driven remediation exists because that record contains arithmetic, status labels, and a falsifiability register that must be internally consistent before anyone acts on them.

The decision that changes if this remediation's result holds is concrete: a researcher deciding whether to build a code-classification pipeline on the Kodaira–Néron classifier, or to bound QEC overhead using valuation structure, should treat both as unverified or disconfirmed respectively, and should direct effort at the single remaining open question — whether a non-trivial valuation invariant of stabilizer codes exists at all. If the remediation's arithmetic were wrong — if the per-family figures did not sum to the aggregate, or if the valuation bound were not strictly weaker than the Singleton bound — the remediation itself would fail and the published statuses would need re-examination.

The published paper [2] established the following starting points, which this remediation takes as given rather than re-argues. First, every positive integer is a finite product of prime powers, and $v_p(n)$ measures depth along the prime-$p$ branch of the factorization tree, not size (established, following Ostrowski 1916). Second, the tensor product multiplies Hilbert-space dimensions, so for $n$ qubits $\dim H = 2^n$ and $v_2(\dim H) = n$; the no-cloning theorem is the impossibility of a linear diagonal map. Third, the paper's own falsifiability machinery was applied to its two flagged domains, computing and QEC, and returned largely negative verdicts: the $[[n,k,d]]$ parameter mapping is definitional for $n$ and $k$ and unavailable for $d$; three derived consequences (overhead bound, complexity characterization, no-cloning re-expression) were each disconfirmed; and the 83% classification claim survived only as an unverified internal figure with two failed reproduction attempts attached.

This remediation contributes:

- A full arithmetic verification of the published record's quantitative claims: the per-family accuracy sum (166/200 = 83%), the spectral-gap figure (187/200 = 93.5%), the claimed versus observed Mahler spectral gaps, and the Golay correction factor (Section 4).
- A derivation, with shown arithmetic, that the sharpest valuation-only overhead bound $n/k \ge 1$ is strictly weaker than the quantum Singleton bound for every stabilizer code with $d \ge 2$, confirming the published FQ2 disconfirmation (Section 4).
- A consolidated status table for claims C1–C8 in which every status is either arithmetic, definitional, or explicitly labeled unverified, with the empirical 83% claim carried as unverified-internal and its reproduction requirement restated (Sections 3 and 5).
- A remediated statement of the single open question and the concrete reproduction protocol that would resolve it, including baselines and leakage controls (Section 7).

## 2. Background and Related Work

This section discusses the five works available for citation. Because the citation base for this remediation is five works rather than eight or more, the literature treatment is correspondingly narrow; this limitation is recorded in Section 6.

The paper under remediation [2] is the primary object. Its full text establishes the branch-depth reading — each prime $p_i$ in $n = \prod p_i^{a_i}$ is a branch type and $a_i = v_{p_i}(n)$ is the depth of nesting along that branch — and applies the anchor paper's falsifiability condition ("disconfirmed if the reading yields no explanatory or predictive content beyond the standard formalism — i.e., if it is pure relabeling") to the $[[n,k,d]]$ mapping. Its conclusion states the negative result in the paper's own terms: the parameter mapping is definitional for $n$ and $k$, unavailable for $d$, and the three falsifiable consequences (overhead bound FQ2, complexity characterization FQ3, no-cloning re-expression FQ4) are each disconfirmed, leaving the open question of a non-trivial valuation invariant with the 83% classification claim as its testable hypothesis. This remediation verifies that record's arithmetic and consolidates its statuses; it adds no new physics claim.

The categorical and p-adic precedent that [2] invokes is not separately citable here beyond what [2] itself states: [2] records that the no-cloning content is established in the categorical quantum mechanics literature (Abramsky & Coecke 2004; Abramsky 2009; Coecke 2009; Coecke & Duncan 2011) and that the connection between p-adic geometry and QEC is established in the holographic tensor-network literature (Heydeman, Marcolli, Saberi & Stoica 2018; Bhattacharyya, Hung, Lei & Li 2018; Gubser & Knaute 2017). Those works are listed in [2]'s own reference list but are not entries in this remediation's citation base, so no claim about their content is made here beyond [2]'s attribution.

The ACRP-07 audit [3] provides the external-landscape context and an instructive precedent for this remediation's method. [3] examines whether the Qubit Delusion's critique of the qubit-gate-circuit model — that it imports a particle ontology inconsistent with quantum field theory, and that the field's failure to deliver commercially viable hardware after \$35 billion of investment is an epistemic crisis — connects to the Adelic Core Research Program's non-Archimedean framework. Its kernel-membership audit assigns the Qubit Delusion a grade of NONE (uses none of the four kernel elements: valuation, tree boundary, Ostrowski, adeles), and its conclusion argues that at every candidate junction "the valuation kernel is aesthetic, not load-bearing": the particle-ontology critique does not require tree geometry, and "the error-correction overhead wall is a fact about stabilizer codes rather than about Archimedean geometry." This is the same failure mode that [2] self-reports for its own QEC extension — a valuation vocabulary attached to a claim whose substance lives entirely in standard stabilizer-code theory. [3]'s finding that forcing a load-bearing connection would itself be map-territory confusion is the precedent for this remediation's refusal to rescue the disconfirmed claims.

The QEC-Darwinism tradeoff paper [4] supplies the sharpest external no-go result in the citation base and a model for what a genuine ultrametric consequence would look like. [4] summarizes the theorem of Maity et al. (arXiv:2608.03944, 2026): if $F_{\text{bare}} > H_2^{-1}[(1-\delta)\ln 2]$, then no environment fragment can satisfy the Darwinism criterion, so $R_\delta = 0$ regardless of microscopic Hamiltonian — a model-independent tradeoff between QEC and Quantum Darwinism, with the threshold reported as $F_L > 0.874$. The proof chain [4] gives is a sequence of information inequalities, $(1-\delta)\ln 2 \le \chi(F) \le \chi(E) \le S(\rho_E) = S(\rho_B) \le H_2(F_{\text{bare}})$, all Archimedean. [4] then asks whether the tradeoff is Ostrowski-invariant and derives that in an ultrametric (Bruhat–Tits tree) setting the strong triangle inequality forces a discrete, quantized redundancy staircase in place of the continuous redundancy function $R_\delta$. Two points matter for this remediation. First, [4] demonstrates the standard this program must meet: a quantitative, theorem-backed consequence, not a vocabulary. Second, [4]'s §6.2 states that if the Archimedean bound is universal across all $p$-adic places, the result is a deep null result constraining the place-democracy thesis — the same logical shape as [2]'s disconfirmations: a null result that constrains the program honestly.

The quantum-advantage audit [5] contributes the epistemic-standard framework against which this remediation's honesty requirements are calibrated. [5] audits Huang, Choi, McClean & Preskill (2025, arXiv:2508.05720), whose Theorem 1 states that, assuming BPP $\ne$ BQP, the decision problem "does this specific quantum circuit outperform Pauli propagation classical simulation?" is in BQP but not in BPP — so detecting quantum advantage is itself classically hard. [5]'s revised vulnerability table is directly relevant: vulnerability V2, "QEC overhead qualitative," stands at HIGH severity because QNFO's critique has "no computed joules-per-solution threshold," and vulnerability V5 concerns missing self-falsification, upgraded to MODERATE because of an "active correction registry." [5] also records the systemic finding that "$\ge 3$ D1 papers truncated; corrections not propagated to source docs" — precisely the failure mode this erratum remediation exists to repair, since the v0.4 changelog of [2] records corrections (the withdrawn "first reproduction attempt" wording, the NTOF 187/200 figure) that must now be propagated consistently through the abstract, register, and conclusion. [5]'s conclusion that QNFO "practices self-falsification operationally" is the standard this remediation holds the 83% record to.

Finally, the topological-index paper [1] supplies a structural precedent from mathematical chemistry for the depth-versus-size distinction that underlies the whole branch-depth program. [1] studies degree-based topological indices on trees with a fixed number of pendent vertices: the first Zagreb index $M_1(G) = \sum_{v \in V(G)} d_G(v)^2$ and the second $M_2(G) = \sum_{uv \in E(G)} d_G(u)\, d_G(v)$. Its Theorem 1 proves $M_1(T) \ge 9n - 16$ for a tree with $n \ge 2$ pendent vertices when $n$ is even, with equality at a 4-tree (all internal vertices of degree 4), and $M_1(T) \ge 9n - 15$ when $n$ is odd; its Theorem 3 proves $M_2(T) \ge 11n - 27$ for $n \ge 8$ pendent vertices, with equality when each stem vertex has degree 4 or 5 and other internal vertices degree 3. The relevance is methodological: [1] shows how a tree-structural quantity (here, degree sums conditioned on pendent-vertex count) admits sharp bounds that depend on shape, not merely on the number of vertices. This is exactly the kind of result the open question C4 of [2] demands from valuation invariants of codes — a bound or classifier that depends on branch structure rather than on the definitional exponents $n$ and $k$ — and [1]'s extremal-graph framework (fix a structural parameter, bound the index, characterize the extremal object) is a template for what a positive answer to C4 would look like.

## 3. Methods

This remediation is a document-level arithmetic and logical audit of the published paper [2], performed under the erratum pl-prime-valuation-qec-implications-v0.4-0. It performs no experiment, no simulation, no survey, and no new computation on code data; every empirical figure it handles is attributed to [2] or to the internal reports [2] records.

The method has four steps.

**Step 1: Claim inventory.** All eight registered claims C1–C8 of [2]'s falsifiability register are extracted verbatim with their types and statuses. No claim is added, merged, or renumbered, so that the remediated register remains row-compatible with the published one.

**Step 2: Arithmetic verification.** Every quantitative statement in [2] that can be checked by arithmetic on figures [2] itself states is recomputed with all steps shown in Section 4. This covers: the aggregate classification accuracy and its per-family decomposition; the separately reported spectral-gap verification figure; the claimed versus observed Mahler spectral separations; the Golay correction; and the comparison between the valuation-only overhead bound and the quantum Singleton bound.

**Step 3: Status consolidation.** Each claim's published status is checked for consistency with the arithmetic of Step 2 and with the logical structure of [2]'s own falsifiability conditions. A status is confirmed if the published derivation or arithmetic supports it; a status is carried as unverified if [2] itself labels it so. Where the published record contains an internal inconsistency (for example, a figure omitted from one section but present in another), the remediation states the reconciliation explicitly.

**Step 4: Remediated register and pathway.** The consolidated register (Section 5) and the reproduction pathway (Section 7) are written so that each remaining open item carries a concrete, falsifiable test with stated baselines.

Assumptions made by this remediation, stated here because no source supplies them otherwise: we assume the four code families named in [2] (surface, CSS, optimal, random) are the complete family set of the 200-code test corpus, since the per-family figures [2] reports sum exactly to the aggregate only under that assumption (verified in Section 4). We assume the quantum Singleton bound $n - k \ge 2(d-1)$ holds for all stabilizer codes considered, as [2] treats it as the comparison standard. We assume the reported reproduction-attempt figures (55 codes, observed values) are as [2] records them; this remediation does not re-run them.

## 4. Analysis

All inputs in this section come from [2] unless marked as an assumption. Every computation is shown step by step.

### 4.1 The aggregate classification accuracy and its per-family decomposition

**Inputs (from [2], §6):** per-family correct assignments on 50 test codes per family: Surface 46/50, CSS 39/50, Optimal 45/50, Random 36/50; aggregate claim 166/200 (83%).

**Computation D1 (per-family sum):**
$$46 + 39 = 85,$$
$$85 + 45 = 130,$$
$$130 + 36 = 166.$$
The per-family figures sum to exactly 166, matching the published aggregate numerator.

**Computation D2 (aggregate rate):**
$$\frac{166}{200} = 0.83.$$
So the published 83% figure is arithmetically consistent with its per-family decomposition, under the assumption (Section 3) that these four families are the complete corpus.

**Computation D3 (family rates):**
$$\frac{46}{50} = 0.92, \qquad \frac{39}{50} = 0.78, \qquad \frac{45}{50} = 0.90, \qquad \frac{36}{50} = 0.72.$$
These reproduce [2]'s stated per-family percentages (92%, 78%, 90%, 72%).

**Computation D4 (chance and majority baselines):** with four families of 50 codes each, a random uniform assignment assigns each code correctly with probability $1/4$:
$$\frac{1}{4} = 0.25,$$
giving an expected $0.25 \times 200 = 50$ correct assignments. The majority-class baseline — always predicting the largest family — also yields $50/200 = 0.25$, since all families have equal size 50. The published 83% therefore exceeds both baselines by $0.83 - 0.25 = 0.58$, i.e., 58 percentage points. This margin is the quantity any reproduction must exceed by a pre-registered margin; the arithmetic here only establishes what the baselines are, not that the 83% is reproducible.

### 4.2 The spectral-gap verification figure

**Input (from [2], §6, v0.4 patch):** the source reports a C7.3′ spectral-gap verification figure of 187/200 (93.5%).

**Computation D5:**
$$\frac{187}{200} = 0.935.$$
The published percentage is arithmetically correct. Note the internal-tension this figure creates, which the v0.4 changelog of [2] itself flags: 187/200 = 93.5% for the spectral-gap leg coexists with the failed Mahler-leg reproduction at $n \le 18$ and the aggregate 83% for the classification leg. These are three different quantities (spectral-gap verification, Mahler separation at small $n$, full classification accuracy), and the remediated register in Section 5 keeps them distinct.

### 4.3 The definitional identities and the unavailable distance mapping

**Computation D6 (definitional identities):** for an $[[n,k,d]]$ stabilizer code on $n$ qubits, $\dim H = 2^n$ and $\dim H_L = 2^k$. Since $2^n$ is a power of 2,
$$v_2(2^n) = n, \qquad v_2(2^k) = k.$$
These hold by the definition of the $p$-adic valuation on prime powers; no property of the code beyond its dimensions is used. This confirms [2]'s finding that the $n$ and $k$ mappings are definitional (claim C2, self-corrected).

**Computation D7 (distance has no valuation reading):** the distance $d$ is the minimum Hamming weight of a non-trivial logical operator — a count of tensor factors touched. There is no integer $m$ with $v_p(m) = d$ arising from the code's dimension data: $\dim H = 2^n$ and $\dim H_L = 2^k$ determine only $n$ and $k$, and $d$ is independent of both in general (codes with the same $n, k$ can have different $d$). This confirms claim C3's rejection.

### 4.4 The valuation-only overhead bound versus the quantum Singleton bound

**Inputs (from [2], §5.2, FQ2 resolution):** the valuation data of a $[[n,k,d]]$ code — $v_2(\dim H) = n$, $v_2(\dim H_L) = k$, and $v_2(\|S\|)$ where $\|S\|$ is the stabilizer group order — reduce to functions of $(n, k, q)$ only, where $q = 2^{n-k}$ is the stabilizer group order for a code with $\|S\| = 2^{n-k}$. The sharpest valuation-only overhead bound is $n/k \ge 1$. The comparison standard is the quantum Singleton bound $n - k \ge 2(d-1)$.

**Computation D8 (the valuation bound is trivial):** since a codespace of dimension $2^k$ lives inside a Hilbert space of dimension $2^n$, and a subspace cannot exceed the ambient space,
$$2^k \le 2^n \implies k \le n \implies \frac{n}{k} \ge 1.$$
Equality holds exactly when $k = n$, i.e., the trivial code with no protection. This is the bound [2] reports, and the derivation shows it uses nothing but subspace inclusion — no valuation content beyond the definitional exponents.

**Computation D9 (Singleton in ratio form):** from $n - k \ge 2(d-1)$ with $k \ge 1$ and $d \ge 2$:
$$k \le n - 2(d-1) \implies \frac{n}{k} \ge \frac{n}{\,n - 2(d-1)\,}.$$
The denominator is positive: $n - 2(d-1) \ge k \ge 1$ by the Singleton bound itself. And the ratio is strictly greater than 1 whenever $d \ge 2$:
$$\frac{n}{\,n - 2(d-1)\,} > 1 \iff n > n - 2(d-1) \iff 2(d-1) > 0 \iff d > 1.$$
So for every stabilizer code with $d \ge 2$, the Singleton bound forces $n/k \ge n/(n - 2(d-1)) > 1$, strictly stronger than the valuation-only bound $n/k \ge 1$. This confirms FQ2's disconfirmation: the valuation-based overhead bound is strictly weaker than Singleton for every non-trivial code.

**Worked example (from [2]'s test corpus):** the Steane code $[[7,1,3]]$:
$$\text{Singleton: } 7 - 1 = 6 \ge 2(3-1) = 4 \quad \checkmark$$
$$\text{Singleton ratio: } \frac{7}{7 - 4} = \frac{7}{3} \approx 2.3333,$$
$$\text{Valuation bound: } \frac{7}{1} = 7 \ge 1 \quad \text{(trivially satisfied, no constraint beyond } k \le n\text{)}.$$
The Singleton ratio lower bound of $7/3$ is informative (it excludes, e.g., a hypothetical $[[7,3,3]]$ code, since $7 - 3 = 4 < 4$ fails... indeed $4 \ge 4$ holds with equality; a $[[7,4,3]]$ code would fail: $7 - 4 = 3 < 4$). The valuation bound excludes nothing beyond $k \le n$. The comparison is decisive at the level of principle, not just this example.

### 4.5 The Mahler spectral separation: claimed versus observed

**Inputs (from [2], §6):** NTOF claims Mahler $v_p^{\max} = 28$ for optimal versus $v_p^{\max} = 4$ for random ensembles, with claimed gap $\ge 10$. The reproduction attempt (P4.2, recorded in [2]) on 55 verified codes at $n \le 18$ observed optimal $v_p^{\max} = 4$, random median 3, random maximum 6.

**Computation D10 (claimed gap):**
$$28 - 4 = 24,$$
which satisfies the claimed gap $\ge 10$ with margin $24 - 10 = 14$.

**Computation D11 (observed gap at $n \le 18$):**
$$\text{optimal} - \text{random median} = 4 - 3 = 1,$$
$$\text{random max} - \text{optimal} = 6 - 4 = 2.$$
The observed ordering is inverted relative to the claim: the random ensemble's maximum exceeds the optimal ensemble's maximum by 2. The claimed separation (gap 24) and the observed separation (gap $-2$, i.e., inverted by 2) differ by $24 - (-2) = 26$ in the signed gap. The reproduction therefore fails to support the claim at the reported sizes, as [2] records.

**Computation D12 (size-premise check):** [2] records that NTOF's own text says "up to n=64 qubit codes," while the reproduction ran at $n \le 18$. The size ratio is
$$\frac{64}{18} \approx 3.5556.$$
The failed reproduction therefore does not cover the claimed regime's upper range; this is why [2] correctly notes that the $n \le 18$ result removes the size premise of an earlier impossibility argument but does not constitute a decisive test of the claim at $n$ up to 64. The decisive test remains blocked by the two source under-specifications [2] records: the Mahler target function is undefined in the source, and Algorithm 4.4's Cox-ring ideal $I_C$ is unspecified.

### 4.6 The Golay correction

**Inputs (from [2], §6, prior-art correction):** ACRP-06 initially confirmed $v_p^{\max} = 28$ on Golay-type self-dual codes, then issued an erratum (v1.1) correcting Golay $v_p^{\max}$ from 28 to 2/4.

**Computation D13 (overstatement factor):**
$$\frac{28}{4} = 7, \qquad \frac{28}{2} = 14.$$
The initially reported value overstated the corrected value by a factor of 7 to 14, depending on which corrected value (4 or 2) applies. With the correction, the Golay figure no longer supports a large spectral gap, and [2] records that the 28 "has now failed two independent reproductions plus an erratum chain."

### 4.7 Reproduction corpus size

**Input (from [2], §6):** the reproduction attempt ran on 55 verified codes: CSS $[[7,1,3]]$ and $[[15,7,3]]$ (2 codes), toric surface $L = 2, 3$ (2 codes), optimal $[[5,1,3]]$ (1 code), and 50 random $[[10,4]]$ codes.

**Computation D14 (corpus composition):**
$$2 + 2 + 1 + 50 = 55.$$
The stated composition sums to the stated total. The structured-code fraction is
$$\frac{5}{55} \approx 0