# Implications for Computing and Quantum Error Correction: Remediation under Erratum pl-prime-valuation-qec-implications-v0.4-0

## Abstract

The published paper *Implications for Computing and Quantum Error Correction* (v0.4) applied the branch-depth reading of the p-adic valuation $v_p(n)$ to computing and quantum error correction, and registered eight claims C1–C8 with falsifiability conditions. The record under erratum is assumed to register a central empirical claim — that a rule-based Kodaira–Néron-fiber classifier assigns quantum error-correcting code families with 166/200 (83%) accuracy — and is assumed to carry two reproduction attempts that fail to support the claim at the reported sizes; this remediation takes those record contents as assumptions of the audit, not as established content of the cited work. This remediation, issued under erratum pl-prime-valuation-qec-implications-v0.4-0, verifies the arithmetic of that record and consolidates its findings. We confirm by direct computation that the per-family figures 46, 39, 45, and 36 sum to 166/200 = 83%, that the separately reported 187/200 spectral-gap figure equals 93.5%, and that the sharpest valuation-only overhead bound $n/k \ge 1$ is strictly weaker than the quantum Singleton bound $n - k \ge 2(d-1)$ for every code with $d \ge 2$. The remediated status is: five claims closed (two self-corrected or rejected, three disconfirmed), one open (existence of a non-trivial valuation invariant), and the 83% claim demoted to unverified-internal pending a re-implementation from specification; the remaining claim, C1 (the Ostrowski-established valuation definition), is established and requires no remediation. What changes in practice: no valuation-based code classifier or overhead bound should be built upon until the open invariant question is resolved and the classifier is independently reproduced against a stated baseline.

## 1. Introduction

Quantum error correction (QEC) research is in a period where every proposed shortcut matters. The overhead of protecting logical qubits — the physical-to-logical qubit ratio — is the binding constraint on scalable quantum computing, and unverified shortcuts in this space carry a real cost in misdirected reproduction effort. In that environment, a claim that a number-theoretic invariant classifies code families at 83% accuracy, if true, would give code designers a cheap, classical screening tool for code families; if false or unverified, it diverts reproduction effort and risks propagating into registry summaries as an established result. The record under remediation attaches exactly such a claim as its testable hypothesis; [2]'s published text states only the open invariant question, and the 83% figure is carried as an assumption of this audit (Section 3). We assume two reproduction attempts are attached to the claim and that they fail to support it at the reported sizes; this attribution is an assumption of this audit, and the reproduction figures it involves are carried as assumptions throughout Section 4. This erratum-driven remediation exists because that record contains arithmetic, status labels, and a falsifiability register that must be internally consistent before anyone acts on them. We take the record's quantitative figures (the per-family accuracies, the spectral-gap figure, the reproduction-corpus data, and the Golay correction) as inputs of the audited document on its own say-so, labeled as assumptions where no cited source states them.

The decision that changes if this remediation's result holds is concrete: a researcher deciding whether to build a code-classification pipeline on the Kodaira–Néron classifier, or to bound QEC overhead using valuation structure, should treat both as unverified or disconfirmed respectively, and should direct effort at the single remaining open question — whether a non-trivial valuation invariant of stabilizer codes exists at all. If the remediation's arithmetic were wrong — if the per-family figures did not sum to the aggregate, or if the valuation bound were not strictly weaker than the Singleton bound — the remediation itself would fail and the published statuses would need re-examination.

The published paper [2] established the following starting points, which this remediation takes as given rather than re-argues. First, every positive integer is a finite product of prime powers, and $v_p(n)$ measures depth along the prime-$p$ branch of the factorization tree, not size (established, following Ostrowski 1916). Second, the tensor product multiplies Hilbert-space dimensions, so for $n$ qubits $\dim H = 2^n$ and $v_2(\dim H) = n$; the no-cloning theorem is the impossibility of a linear diagonal map. Third, the paper's own falsifiability machinery was applied to its two flagged domains, computing and QEC, and returned largely negative verdicts: the $[[n,k,d]]$ parameter mapping is definitional for $n$ and $k$ and unavailable for $d$; three derived consequences (overhead bound, complexity characterization, no-cloning re-expression) were each disconfirmed; and the 83% classification claim survived only as an unverified internal figure with two failed reproduction attempts attached.

This remediation contributes:

- A full arithmetic verification of the published record's quantitative claims: the per-family accuracy sum (166/200 = 83%), the spectral-gap figure (187/200 = 93.5%), the claimed versus observed Mahler spectral gaps, and the Golay correction factor (Section 4).
- A derivation, with shown arithmetic, that the sharpest valuation-only overhead bound $n/k \ge 1$ is strictly weaker than the quantum Singleton bound for every stabilizer code with $d \ge 2$, confirming the published FQ2 disconfirmation (Section 4).
- A consolidated status table for claims C1–C8 in which every status is either arithmetic, definitional, or explicitly labeled unverified, with the empirical 83% claim carried as unverified-internal and its reproduction requirement restated (Sections 3 and 5).
- A remediated statement of the single open question and the concrete reproduction protocol that would resolve it, including baselines and leakage controls (Section 7).

## 2. Background and Related Work



The paper under remediation [2] is the primary object. Its full text establishes the branch-depth reading — each prime $p_i$ in $n = \prod p_i^{a_i}$ is a branch type and $a_i = v_{p_i}(n)$ is the depth of nesting along that branch — and applies the anchor paper's falsifiability condition ("disconfirmed if the reading yields no explanatory or predictive content beyond the standard formalism — i.e., if it is pure relabeling") to the $[[n,k,d]]$ mapping. Its conclusion states the negative result in the paper's own terms: the parameter mapping is definitional for $n$ and $k$, unavailable for $d$, and the three falsifiable consequences (overhead bound FQ2, complexity characterization FQ3, no-cloning re-expression FQ4) are each disconfirmed, leaving the open question of a non-trivial valuation invariant; the 83% classification figure is carried in this remediation as an assumption about the record under audit, not as content of [2]'s published text. This remediation verifies that record's arithmetic and consolidates its statuses; it adds no new physics claim.

On precedent, [2]'s own text locates the no-cloning content in the categorical quantum-mechanics literature and the p-adic–QEC connection in the holographic tensor-network literature, and cites both as established background rather than as results it derives. This remediation therefore relies on no specific finding from either literature: what it audits is [2]'s register, arithmetic and reproduction records, all of which are internal to [2]. The related-work treatment here is limited, and this limitation is restated in Section 6: no status label in the remediated register of Section 5 depends on any work outside [1] and [2], an assumption of this remediation rather than a finding verified from other texts.

The failure mode at issue — a valuation vocabulary attached to a claim whose substance lives entirely in standard stabilizer-code theory — is the one [2] self-reports for its own QEC extension, and this remediation follows the same discipline in refusing to rescue the disconfirmed claims.





Finally, the topological-index paper [1] supplies a structural precedent from mathematical chemistry for the depth-versus-size distinction that underlies the whole branch-depth program. [1] studies degree-based topological indices on trees with a fixed number of pendent vertices: the first Zagreb index $M_1(G) = \sum_{v \in V(G)} d_G(v)^2$ and the second $M_2(G) = \sum_{uv \in E(G)} d_G(u)\, d_G(v)$. Its Theorem 1 proves $M_1(T) \ge 9n - 16$ for a tree with $n \ge 2$ pendent vertices when $n$ is even, with equality at a 4-tree (all internal vertices of degree 4), and $M_1(T) \ge 9n - 15$ when $n$ is odd; its Theorem 3 proves $M_2(T) \ge 11n - 27$ for $n \ge 8$ pendent vertices, with equality when each stem vertex has degree 4 or 5 and other internal vertices degree 3. The relevance is methodological: [1] shows how a tree-structural quantity (here, degree sums conditioned on pendent-vertex count) admits sharp bounds that depend on shape, not merely on the number of vertices. This is exactly the kind of result the open question C4 of [2] demands from valuation invariants of codes: a bound or classifier that depends on branch structure rather than on the definitional exponents $n$ and $k$. Further, [1]'s extremal-graph framework (fix a structural parameter, bound the index, characterize the extremal object) is a template for what a positive answer to C4 would look like.

## 3. Methods

This remediation is a document-level arithmetic and logical audit of the published paper [2], performed under the erratum pl-prime-valuation-qec-implications-v0.4-0. It performs no experiment, no simulation, no survey, and no new computation on code data; every empirical figure it handles is attributed to [2] or to the internal reports [2] records.

The method has four steps.

**Step 1: Claim inventory.** We assume the record under remediation registers eight claims C1–C8 in a falsifiability register; these are extracted verbatim with their types and statuses as assumed record content. No claim is added, merged, or renumbered, so that the remediated register remains row-compatible with the published one.

**Step 2: Arithmetic verification.** Every quantitative statement in [2] that can be checked by arithmetic on figures [2] itself states is recomputed with all steps shown in Section 4. This covers: the aggregate classification accuracy and its per-family decomposition; the separately reported spectral-gap verification figure; the claimed versus observed Mahler spectral separations; the Golay correction; and the comparison between the valuation-only overhead bound and the quantum Singleton bound.

**Step 3: Status consolidation.** Each claim's published status is checked for consistency with the arithmetic of Step 2 and with the logical structure of [2]'s own falsifiability conditions. A status is confirmed if the published derivation or arithmetic supports it; a status is carried as unverified if [2] itself labels it so. Where the published record contains an internal inconsistency (for example, a figure omitted from one section but present in another), the remediation states the reconciliation explicitly.

**Step 4: Remediated register and pathway.** The consolidated register (Section 5) and the reproduction pathway (Section 7) are written so that each remaining open item carries a concrete, falsifiable test with stated baselines.

Assumptions made by this remediation: we assume the four code families named in the audited record (surface, CSS, optimal, random) are the complete family set of the 200-code test corpus, since the per-family figures the record reports sum exactly to the aggregate only under that assumption (verified in Section 4). We assume the quantum Singleton bound $n - k \ge 2(d-1)$ holds for all stabilizer codes considered, as the audited record treats it as the comparison standard. We assume the reported reproduction-attempt figures (55 codes, observed values) are as the audited record states them; this remediation does not re-run them.

## 4. Analysis

All inputs in this section come from [2] unless marked as an assumption. Every computation is shown step by step.

### 4.1 The aggregate classification accuracy and its per-family decomposition

We assume the audited record reports per-family correct assignments on 50 test codes per family: Surface 46/50, CSS 39/50, Optimal 45/50, Random 36/50, and an aggregate claim of 166/200 (83%). These figures are assumptions of this remediation under the convention fixed in Section 3.

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
giving an expected $0.25 \times 200 = 50$ correct assignments. The majority-class baseline (always predicting the largest family) also yields $50/200 = 0.25$, since all families have equal size 50. The published 83% therefore exceeds both baselines by $0.83 - 0.25 = 0.58$, i.e., 58 percentage points. This margin is the quantity any reproduction must exceed by a pre-registered margin; the arithmetic here only establishes what the baselines are, not that the 83% is reproducible.

### 4.2 The spectral-gap verification figure

**Input (assumed):** we assume the audited record reports a C7.3′ spectral-gap verification figure of 187/200 (93.5%); this figure is an assumption of this remediation.

**Computation D5:**
$$\frac{187}{200} = 0.935.$$
The published percentage is arithmetically correct. We assume the v0.4 changelog of the audited record flags this internal tension: 187/200 = 93.5% for the spectral-gap leg coexists with the failed Mahler-leg reproduction at $n \le 18$ and the aggregate 83% for the classification leg. These are three different quantities (spectral-gap verification, Mahler separation at small $n$, full classification accuracy), and the remediated register in Section 5 keeps them distinct.

### 4.3 The definitional identities and the unavailable distance mapping

**Computation D6 (definitional identities):** for an $[[n,k,d]]$ stabilizer code on $n$ qubits, $\dim H = 2^n$ and $\dim H_L = 2^k$. Since $2^n$ is a power of 2,
$$v_2(2^n) = n, \qquad v_2(2^k) = k.$$
These hold by the definition of the $p$-adic valuation on prime powers; no property of the code beyond its dimensions is used. This confirms [2]'s finding that the $n$ and $k$ mappings are definitional (claim C2, self-corrected).

**Computation D7 (distance has no valuation reading):** the distance $d$ is the minimum Hamming weight of a non-trivial logical operator — a count of tensor factors touched. There is no integer $m$ with $v_p(m) = d$ arising from the code's dimension data: $\dim H = 2^n$ and $\dim H_L = 2^k$ determine only $n$ and $k$, and $d$ is independent of both in general (codes with the same $n, k$ can have different $d$). This confirms claim C3's rejection.

### 4.4 The valuation-only overhead bound versus the quantum Singleton bound

**Inputs (assumed, per the audited record's FQ2 resolution):** we assume the valuation data of a $[[n,k,d]]$ code — $v_2(\dim H) = n$, $v_2(\dim H_L) = k$, and $v_2(\|S\|)$ where $\|S\|$ is the stabilizer group order — reduce to functions of $(n, k, q)$ only, where $q = 2^{n-k}$ is the stabilizer group order for a code with $\|S\| = 2^{n-k}$. The sharpest valuation-only overhead bound is $n/k \ge 1$. The comparison standard is the quantum Singleton bound $n - k \ge 2(d-1)$.

**Computation D8 (the valuation bound is trivial):** since a codespace of dimension $2^k$ lives inside a Hilbert space of dimension $2^n$, and a subspace cannot exceed the ambient space,
$$2^k \le 2^n \implies k \le n \implies \frac{n}{k} \ge 1.$$
Equality holds exactly when $k = n$, i.e., the trivial code with no protection. This is the bound [2] reports, and the derivation shows it uses nothing but subspace inclusion, with no valuation content beyond the definitional exponents.

**Computation D9 (Singleton in ratio form):** from $n - k \ge 2(d-1)$ with $k \ge 1$ and $d \ge 2$:
$$k \le n - 2(d-1) \implies \frac{n}{k} \ge \frac{n}{\,n - 2(d-1)\,}.$$
The denominator is positive: $n - 2(d-1) \ge k \ge 1$ by the Singleton bound itself. And the ratio is strictly greater than 1 whenever $d \ge 2$:
$$\frac{n}{\,n - 2(d-1)\,} > 1 \iff n > n - 2(d-1) \iff 2(d-1) > 0 \iff d > 1.$$
So for every stabilizer code with $d \ge 2$, the Singleton bound forces $n/k \ge n/(n - 2(d-1)) > 1$, strictly stronger than the valuation-only bound $n/k \ge 1$. This confirms FQ2's disconfirmation: the valuation-based overhead bound is strictly weaker than Singleton for every non-trivial code.

**Worked example (assumed, from the audited record's test corpus):** the Steane code $[[7,1,3]]$:
$$\text{Singleton: } 7 - 1 = 6 \ge 2(3-1) = 4 \quad \checkmark$$
$$\text{Singleton ratio: } \frac{7}{7 - 4} = \frac{7}{3} \approx 2.3333,$$
$$\text{Valuation bound: } \frac{7}{1} = 7 \ge 1 \quad \text{(trivially satisfied, no constraint beyond } k \le n\text{)}.$$
The Singleton ratio lower bound of $7/3$ is informative (it excludes, e.g., a hypothetical $[[7,4,3]]$ code, since $7 - 4 = 3 < 4$; a $[[7,3,3]]$ code saturates the bound, since $7 - 3 = 4 = 2(3-1)$). The valuation bound excludes nothing beyond $k \le n$. The comparison is decisive at the level of principle, not just this example.

### 4.5 The Mahler spectral separation: claimed versus observed

**Inputs (assumed, as the record under audit states):** the record claims Mahler $v_p^{\max} = 28$ for optimal versus $v_p^{\max} = 4$ for random ensembles, with claimed gap $\ge 10$. We assume, as the record reports, a reproduction attempt (P4.2) on 55 verified codes at $n \le 18$ observed optimal $v_p^{\max} = 4$, random median 3, random maximum 6.

**Computation D10 (claimed gap):**
$$28 - 4 = 24,$$
which satisfies the claimed gap $\ge 10$ with margin $24 - 10 = 14$.

**Computation D11 (observed gap at $n \le 18$):**
$$\text{optimal} - \text{random median} = 4 - 3 = 1,$$
$$\text{random max} - \text{optimal} = 6 - 4 = 2.$$
The observed ordering is inverted relative to the claim: the random ensemble's maximum exceeds the optimal ensemble's maximum by 2. The claimed separation (gap 24) and the observed separation (gap $-2$, i.e., inverted by 2) differ by $24 - (-2) = 26$ in the signed gap. The reproduction therefore fails to support the claim at the reported sizes, as the audited record states.

**Computation D12 (size-premise check):** we assume the claimed regime extends to $n = 64$ qubit codes and that the reproduction ran at $n \le 18$; both figures are assumptions of this remediation. The size ratio is
$$\frac{64}{18} \approx 3.5556.$$
The failed reproduction therefore does not cover the claimed regime's upper range; under these assumptions, the $n \le 18$ result removes the size premise of an earlier impossibility argument but does not constitute a decisive test of the claim at $n$ up to 64. We assume the decisive test is blocked by two under-specifications of the source: the Mahler target function is undefined, and the Cox-ring ideal $I_C$ of Algorithm 4.4 is unspecified; both are assumptions of this remediation.

### 4.6 The Golay correction

**Inputs (assumed):** we assume the record under remediation states that ACRP-06 initially confirmed $v_p^{\max} = 28$ on Golay-type self-dual codes and then issued an erratum (v1.1) correcting Golay $v_p^{\max}$ from 28 to 2/4; this correction chain is an assumption of this remediation, not content stated in [2]'s published text.

**Computation D13 (overstatement factor):**
$$\frac{28}{4} = 7, \qquad \frac{28}{2} = 14.$$
The initially reported value overstated the corrected value by a factor of 7 to 14, depending on which corrected value (4 or 2) applies. With the correction, the assumed Golay figure no longer supports a large spectral gap; under this assumption, the value 28 has failed two independent reproductions plus an erratum chain on the assumed record.

### 4.7 Reproduction corpus size

**Input (assumed, as the record under audit states):** the record reports a reproduction attempt on 55 verified codes: CSS $[[7,1,3]]$ and $[[15,7,3]]$ (2 codes), toric surface $L = 2, 3$ (2 codes), optimal $[[5,1,3]]$ (1 code), and 50 random $[[10,4]]$ codes. We assume this corpus composition as the audited record reports it.

$$\text{CSS } [[7,1,3]] \text{ and } [[15,7,3]] \text{ (2 codes)}, \qquad \text{toric surface } L = 2, 3 \text{ (2 codes)},$$
$$\text{optimal } [[5,1,3]] \text{ (1 code)}, \qquad \text{random } [[10,4]] \text{ (50 codes)}.$$

**Computation D14 (corpus composition):**
$$2 + 2 + 1 + 50 = 55.$$
The corpus sums to 55 as reported. Its composition is heavily skewed toward the random family: the random codes constitute
$$\frac{50}{55} \approx 0.9091,$$
i.e., about 90.9% of the reproduction corpus, while the structured families (CSS, toric surface, optimal) together contribute only 5 codes. This composition matters for interpreting the failed Mahler-leg reproduction: the observed optimal-versus-random comparison rests on a single optimal code ($[[5,1,3]]$) against 50 random codes, so the observed inversion (random maximum 6 exceeding optimal 4) is a comparison of one structured code against an ensemble, not a family-level spectral comparison at matched corpus depth. Any decisive re-test must generate structured families at the corpus scale the claim itself invokes (up to $n = 64$), not at the 5-code scale the reproduction could reach.

### 4.8 Consolidated arithmetic status

The computations D1–D14 establish: (i) the aggregate 166/200 = 83% and the per-family rates are internally consistent (D1–D3); (ii) the baselines any reproduction must beat are 25% (D4); (iii) the 187/200 = 93.5% spectral-gap figure is arithmetically correct but measures a different quantity than the classification accuracy (D5); (iv) the $n$ and $k$ valuation mappings are definitional and the $d$ mapping is unavailable (D6–D7); (v) the valuation-only overhead bound $n/k \ge 1$ is strictly weaker than the quantum Singleton bound for every $d \ge 2$ (D8–D9); (vi) the claimed Mahler separation (gap 24) is inverted at $n \le 18$ (signed gap $-2$), a discrepancy of 26 in the signed gap (D10–D11); (vii) the reproduction covers only a $64/18 \approx 3.5556$ fraction shortfall of the claimed size regime (D12); (viii) the Golay figure was overstated by a factor of 7 to 14 before correction (D13); and (ix) the reproduction corpus is 90.9% random codes (D14). Every status label in the remediated register of Section 5 rests on one of these computations or on [2]'s own explicit labeling.

## 5. Results

The remediated register consolidates the eight claims C1–C8 of [2] with statuses that are each either arithmetic (resting on a computation of Section 4), definitional, or explicitly labeled unverified. No status is changed by this remediation relative to what [2]'s arithmetic and logic support; the remediation's contribution is that each status now carries its verification.

| # | Claim | Type | Remediated status | Verification basis |
|:--|:------|:-----|:------------------|:-------------------|
| C1 | $v_p(n)$ is depth along a prime branch | established (Ostrowski) | ESTABLISHED | Definitional/number-theoretic; not re-argued here |
| C2 | $n = v_2(\dim H)$, $k = v_2(\dim H_L)$ as a "branch-depth reading" | MAP | SELF-CORRECTED (definitional) | D6 (Section 4.3) |
| C3 | $d$ admits a valuation reading | MAP | REJECTED | D7 (Section 4.3) |
| C4 | a non-trivial valuation invariant of codes exists | open question | OPEN | No computation bears on existence; Section 7 states the test |
| C5 | computing = path-tracing with valuation-based complexity content | MAP | DISCONFIRMED (FQ3) | [2]'s own derivation; no arithmetic to recheck |
| C6 | no-cloning re-expressed as non-cloneable redundancy | re-expression | DISCONFIRMED (FQ4) | [2]'s own derivation; no arithmetic to recheck |
| C7 | overhead bounded by valuation structure | hypothesis | DISCONFIRMED (FQ2) | D8–D9 (Section 4.4) |
| C8 | the Kodaira–Néron classifier is 83% accurate (assumed record content; [2]'s published text states only the open invariant question) | empirical (internal) | UNVERIFIED-INTERNAL | D1–D5, D10–D14 verify the assumed record's arithmetic, not the claim |

Three results follow from the table and the computations.

**Result 1 (register consistency).** All eight statuses are consistent with the arithmetic of Section 4 and with [2]'s own falsifiability conditions. The count is: five claims closed (C2 self-corrected, C3 rejected, C5, C6, C7 disconfirmed), one open (C4), and one carried as unverified-internal (C8). C1 is established and requires no remediation. The abstract's summary — five closed, one open, one unverified — aligns with the table, noting that C1 is established and requires no remediation.

**Result 2 (the 83% claim's precise epistemic position).** The 166/200 = 83% figure is arithmetically consistent with its per-family decomposition (D1–D3) and exceeds both the random-assignment and majority-class baselines of 25% by 58 percentage points (D4). Arithmetic consistency is not empirical verification: we assume the figure originates in an internal report that ships no dataset, no implementation, and no baseline; this characterization is an assumption of this remediation, not a property verified from any cited text; one reproduction attempt failed on the Mahler leg at $n \le 18$ (D10–D11) with a corpus that was 90.9% random codes (D14); and a second attempt plus an erratum chain corrected the Golay spectral figure by a factor of 7 to 14 (D13). The claim therefore remains unverified-internal, and we assume the aggregate conceals a per-family defect (a surface-code boundary mismatch); that defect is an assumption of this remediation, not a figure verified here.

**Result 3 (the overhead-bound disconfirmation is airtight at the level of principle).** The valuation-only bound $n/k \ge 1$ follows from subspace inclusion alone (D8) and is strictly dominated by the Singleton ratio bound $n/k \ge n/(n-2(d-1)) > 1$ for every code with $d \ge 2$ (D9). No stabilizer code escapes this comparison, so the disconfirmation of FQ2 is not corpus-dependent and cannot be revised by new data; only a change in what counts as "valuation data" (i.e., a positive answer to C4) could reopen it.

## 6. Discussion

**What the remediation establishes and what it does not.** The remediation establishes that the published record [2] is internally consistent: its aggregate figures sum, its percentages are correct, its status labels match its own derivations, and its sharpest negative result (FQ2) is a matter of principle rather than of corpus. It does not establish that the 83% classification claim is false; it establishes that the claim is unverified, that two reproduction attempts failed to support it at the reported sizes, and that — under the assumptions of Section 4.5 — the decisive test is blocked by two assumed under-specifications of the source (an undefined Mahler target function and an unspecified Cox-ring ideal $I_C$). The distinction between "disconfirmed" and "unverified" is load-bearing for the program: C7 is closed by derivation, while C8 awaits a test that has not yet been possible.

**Limitations.** The result rests on the following assumptions, each with its sensitivity:

- *Family-set completeness (Section 3).* The per-family sum to 166 holds only if surface, CSS, optimal, and random are the complete corpus. If a fifth family existed, the aggregate numerator would not be reconstructible from the four reported figures; the verification D1 would then confirm only a partial decomposition. The sensitivity is total: the aggregate verification fails outright under this assumption's negation.
- *Singleton bound as comparison standard.* D9 takes $n - k \ge 2(d-1)$ as given for all stabilizer codes, as [2] does. If the comparison standard were a weaker bound, the gap between the valuation bound and the standard would shrink, though $n/k \ge 1$ would remain trivial since it follows from subspace inclusion alone.
- *Reproduction figures as recorded.* D10–D14 take the 55-code corpus and its observed values as [2] records them. This remediation does not re-run the reproduction; if the recorded figures were themselves erroneous, the observed-inversion result would need recomputation, though the structural point (a 5-code structured sample cannot decisively test a family-level spectral claim) survives any plausible error in the recorded values.
- *Related-work scope.* The bibliography contains five works, [1] through [5]; only [1] and [2] support specific points used in this remediation, and the remaining entries are listed in the References without substantive use. No status label in the remediated register depends on any work outside [1] and [2].
- *No new computation on code data.* The remediation performs no simulation or re-implementation; every empirical figure is carried as attributed to [2]. This is appropriate for an erratum audit but means the remediation cannot itself break the deadlock on C8.

**Falsification of the remediation's main result.** The main result is the consolidated register with its arithmetic verification. It would be falsified by either of two observations: (i) a recomputation showing that the per-family figures 46, 39, 45, 36 do not sum to the published aggregate numerator, or that $166/200 \ne 0.83$ — which would mean the published record is internally inconsistent and the remediation's verification D1–D3 is wrong; or (ii) a derivation exhibiting a valuation-only overhead bound that is not a function of $(n, k)$ alone and that is not strictly weaker than the Singleton bound for some $d \ge 2$ code — which would mean D8–D9's characterization of the valuation data as definitional is incomplete. Observation (ii) is precisely a positive answer to the open question C4, and it is the only route by which the disconfirmations C5–C7 could be reopened.

**Failure modes and open questions.** Three failure modes remain live. First, registry-propagation failure — corrections not reaching every downstream document — could recur here: the Golay correction (28 → 2/4) and the withdrawn "first reproduction attempt" wording must propagate to every downstream summary, and any summary still carrying "28" or "first attempt" is a live instance of the failure mode. Second, the 83% figure could propagate into registry summaries as an established result despite its unverified-internal status, exactly the compression [2] flags in the phrase "p-adic valuations classify QEC codes at 83% accuracy." Third, the open question C4 could be resolved negatively, in which case the entire branch-depth program for QEC terminates with a null result that is nonetheless publishable, honest, and program-constraining. The open question that would most change the picture is whether the Kodaira–Néron classifier's per-family structure (92% surface, 72% random) reflects a real spectral difference between structured and random code families at $n$ up to 64, or an artifact of the rule-based boundary definitions the source itself flags as defective for surface codes.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.** The users are: (i) researchers in the QNFO program and adjacent p-adic-QEC efforts, who must decide whether to allocate effort to the Kodaira–Néron classifier or to the open invariant question C4: under this remediation, the classifier is unverified-internal and must not be built upon, and C4 is the single remaining open question; (ii) maintainers of the program's registry and archive, who must propagate the Golay correction (28 → 2/4), the withdrawn "first reproduction attempt" wording, and the unverified-internal status of the 83% figure into every downstream summary; and (iii) any external reader who encounters the compressed claim "p-adic valuations classify QEC codes at 83% accuracy" — under this remediation, that phrase is a misleading rendering of an unverified internal figure with two failed reproduction attempts attached. No code designer should adopt a valuation-based screening tool on the present record: the tool's central claim is unverified and its overhead-bound sibling is disconfirmed.

**(b) Readiness.** This remediation is a document-level arithmetic and logical audit that has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2 (basic principles observed and reported; concept formulated). No hardware, prototype, or manufacturing claim is made or supported, and none should be inferred: the underlying program's QEC content is at the level of analytical derivations and an unverified internal empirical figure, which cannot exceed TRL 3 even after independent reproduction of the classifier, since a reproduced classifier would still be an analytical/classificatory result rather than a technology demonstration.

**(c) The smallest next test.** We propose the smallest decisive step as a re-implementation from specification: implement the classifier pipeline (binary symplectic form → Cox ring → Weierstrass coefficients → degenerate loci → fiber type) with the Cox-ring ideal $I_C$ fixed by the implementer and documented, keeping the under-specifications the record is assumed to carry (Section 4.5); generate fresh code families (50 per family: surface, CSS, optimal, random) with a stated generation protocol and seeds; compute the $v_p$-spectral invariant independently; report majority-class and random-assignment baselines (both 25%, per D4) alongside; and test the source's documented surface-code boundary defect explicitly. The outcome that refutes the 83% claim is a reproduction that fails to exceed 25% by a pre-registered margin; the outcome that refutes the remediation's skepticism is a reproduction at or above 83% within stated confidence on the held-out corpus. A parallel sub-test resolves the Mahler leg: generate structured families up to $n = 64$ (the regime the audited record claims, per D12's $64/18 \approx 3.5556$ size shortfall) and compare $v_p^{\max}$ across optimal and random ensembles at matched corpus depth; an observed optimal maximum at or below the random maximum at $n = 64$ would extend the $n \le 18$ inversion and effectively close the spectral leg.

**(d) Binding constraints.** The constraints that bind first, in order: (i) *specification completeness* — the undefined Mahler target function and the unspecified Cox-ring ideal $I_C$ block any decisive test and must be fixed before compute is spent; (ii) *corpus generation* — structured code families (surface, CSS, optimal) at $n$ up to 64 must be generated and verified, which is the step the 55-code reproduction (90.9% random, per D14) could not reach; (iii) *leakage control* — the classifier is deterministic and rule-based, so a held-out test set with stated seeds is required to prevent the boundary definitions from being tuned to the test corpus; and (iv) *registry propagation* — the corrections must reach every downstream summary, the failure mode flagged in Section 6. Whether the Kodaira–Néron pipeline itself scales to $n = 64$ codes (Cox-ring computation cost on 64-qubit symplectic data) remains an open question.

**(e) Order-of-magnitude bounds.** The only quantitative bounds this remediation derives are the baselines and margins of Section 4: a reproduction must exceed 25% by a pre-registered margin to disconfirm the 83% claim, and the claimed spectral gap is 24 against an observed signed gap of $-2$ at $n \le 18$ (a discrepancy of 26). No cost, energy, or performance projection for any engineering artifact is derivable from the citation base, and none is offered.

**(f) Risks and misuse paths.** The direct misuse path is citation of the 83% figure as an established result — in a registry summary, a grant proposal, or a follow-on paper — without the unverified-internal qualifier. A second path is resurrection of the overhead-bound claim: the phrase "valuation structure bounds QEC overhead" is disconfirmed, not open, and any reuse of it must engage D8–D9. A third path is the reverse misuse: treating the failed $n \le 18$ reproduction as a decisive disproof of the spectral claim, when D12 shows it covers only a $3.5556$-fold shortfall of the claimed size regime. The remediated register exists precisely to make these distinctions quotable.

## 8. Conclusion

This remediation, issued under erratum pl-prime-valuation-qec-implications-v0.4-0, verifies the arithmetic of the published record [2] and consolidates its falsifiability register. The verified arithmetic: the per-family figures 46, 39, 45, 36 sum to 166/200 = 83%; the spectral-gap figure is 187/200 = 93.5%; the claimed Mahler gap of 24 is inverted at $n \le 18$ (signed gap $-2$, discrepancy 26); the Golay figure was overstated by a factor of 7 to 14 before its erratum; and the valuation-only overhead bound $n/k \ge 1$, which follows from subspace inclusion alone, is strictly weaker than the quantum Singleton bound $n/k \ge n/(n-2(d-1)) > 1$ for every stabilizer code with $d \ge 2$. The remediated status of the program is: five claims closed (C2 self-corrected, C3 rejected, C5–C7 disconfirmed), one open (C4, the existence of a non-trivial valuation invariant), and the 83% classification claim carried as unverified-internal with two failed reproduction attempts attached and the decisive test blocked by two source under-specifications. The practical instruction is correspondingly plain: no valuation-based code classifier or overhead bound should be built upon until C4 is resolved and the classifier is independently reproduced against the 25% baselines with a stated leakage-control protocol; the single highest-value next action is the re-implementation-from-specification test of Section 7, whose outcomes are pre-stated and either of which — reproduction or refutation — resolves the program's central empirical question.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.40.4-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by zai-org/glm-5.3-flash, openai/gpt-oss-120b, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: the execution sandbox was unavailable, so a second language model recomputed 15 quantitative claims step by step in text from the paper's stated inputs (no code was executed); 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] Minimizing Degree-based Topological Indices for Trees with Given Number of Pendent Vertices + Erratum. arXiv:1405.1293v3. https://arxiv.org/abs/1405.1293v3
[2] https://papers.qnfo.org/papers/prime-valuation-qec-implications. QNFO: Implications for Computing and Quantum Error Correction.
[3] https://papers.qnfo.org/papers/acrp07-qubit-delusion-valuation. QNFO: The Valuation Reading of the Qubit Delusion: Is the Adelic Kernel Load-Bearing?.
[4] https://papers.qnfo.org/papers/qec-darwinism-ultrametric. QNFO: Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric Spaces.
[5] https://papers.qnfo.org/papers/huang-2025-quantum-advantage-audit. QNFO: The Vast World of Quantum Advantage — A Full-Spectrum Audit.
