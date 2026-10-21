# What a Fairness Audit Must Report When Demographic Labels Are Missing: Assumption‑Free Disparity Intervals, a Determinacy Rule, and a Disclosure Checklist

## Abstract

Fairness audits of machine‑learning systems publish group‑level rates such as selection rates, yet the protected labels required for those rates are often missing for a substantial fraction of the audited population, and no settled rule dictates what an audit must disclose in that case. The practical gap is that an oversight reader cannot determine from the published numbers whether the reported rate would survive, shrink, or reverse if the unlabeled records were labeled. This paper closes the gap with an assumption‑free worst‑case analysis. For any published rate we derive the exact interval  
\[
[\hat{p}(1-m),\ \hat{p}(1-m)+m]
\]  
containing the full‑population rate under any pattern of missingness, where \(\hat{p}\) is the labeled‑subset rate and \(m\) the missing‑label fraction; the interval width equals \(m\) exactly. For a two‑group disparity the assumption‑free interval has width \(m_{1}+m_{2}\), independent of the rates: a reported gap of \(0.10\) with missingness rates \(0.6\) and \(0.5\) is compatible with any true gap in \([-0.475,\ 0.625]\). We also derive a determinacy rule—certification of a threshold \(\delta_{\min}\) is impossible exactly when the shifted threshold \(\delta_{\min}+p_{B}\) lies inside \([p_{\min,A},\,p_{\max,A}]\), while \(m<\delta_{\min}\) guarantees that some certification is possible whatever the point estimate. In a mixed‑completeness example with \(n=1000\), \(k=800\), \(\hat{p}_{A}=0.30\) and a fully labeled comparison rate of \(0.35\), the rate interval is \([0.24,\ 0.44]\), the four‑fifths ratio interval is \([0.686,\ 1.257]\), the verdict is indeterminate, and under an expected‑case outcome‑rate assumption the label‑recovery target is \(134\) labels. The framework converts incomplete labels from an unstated caveat into a computed, reportable quantity with a concrete remediation target.

## 1. Introduction

Fairness audits are a key component of responsible machine‑learning deployment [1]; their basic currency is the group‑level rate (selection rate, false‑positive rate, referral rate, etc.) computed per protected group and compared across groups. Producing those rates requires knowing, for each person in the audited population, which protected group they belong to. In operational data that knowledge is routinely incomplete: most algorithmic‑fairness techniques require access to a sensitive attribute such as race, ethnicity, gender, or sexuality, yet such data is largely unavailable in practice, and collecting it carries privacy, misrepresentation, and consent risks [2]. Consequently a substantial fraction of audited records carries no usable group label, and the audit publishes a rate whose denominator is silently the labeled subset. The oversight reader therefore faces a decision—accept the audit, demand remediation, or halt deployment—with a number whose evidentiary value is unquantified. A system can pass an audit on labeled records while its behavior on unlabeled records is materially different, and no published number flags the possibility. Conversely, a model that appears unfair under the observed data may be acceptable once missing‑label uncertainty is accounted for.

If the gap were closed, the oversight reader would see, next to every published rate, an interval stating how far the true rate could deviate given the missing labels, together with a determinacy verdict: either the audit certifies that the disparity is (or is not) larger than a stated threshold of concern, or it reports that the missing labels make certification impossible and states how many labels would have to be recovered to change that. Audit teams would obtain a design rule—a minimum labeled fraction—before deployment rather than a discovery of indeterminacy after it.

The paper builds that disclosure rule from first principles and adopts a deliberately conservative stance. No assumption is made about the mechanism that causes labels to be missing—neither missing‑at‑random nor ignorable nor adversarial—because in the audit setting the missingness may be precisely what an adversarial or negligent process produces. Instead worst‑case bounds are computed over all assignments of the unlabeled records; the bounds depend only on two numbers the audit already has, the labeled fraction and the observed rate among labeled records. The worst case is tight, so the intervals reported are the narrowest any assumption‑free method can give; any narrower interval would smuggle in an assumption about missingness that the audit must then state and defend. The price of this conservatism is width, and a second contribution quantifies that price so an audit designer can decide when assumption‑free reporting is informative and when it is not.

**Contributions.**  
- An exact worst‑case interval \([\hat{r}_{g}(1-m_{g}),\ \hat{r}_{g}(1-m_{g})+m_{g}]\) containing any group’s full‑population rate given its labeled‑subset rate \(\hat{r}_{g}\) and missingness rate \(m_{g}\), with width exactly \(m_{g}\) (Section 4.1).  
- The result that the width of the assumption‑free interval on a two‑group disparity equals \(m_{1}+m_{2}\), independent of the rates, with the worked example \([-0.475,\ 0.625]\) for a reported gap of \(0.10\) (Section 4.2).  
- A determinacy rule—certification of a threshold \(\delta_{\min}\) is impossible exactly when \(\delta_{\min}+p_{B}\) lies inside \([p_{\min,A},\,p_{\max,A}]\), with \(m<\delta_{\min}\) sufficient for some certification whatever the point estimate—and a shortcut condition \(\hat{g}>m_{1}+m_{2}\) that guarantees a positive disparity (Section 4.3), together with the exact necessary‑and‑sufficient condition and a counter‑example showing the shortcut is not necessary (Section 4.4).  
- A worked numerical audit in the mixed‑completeness case: for \(n=1000\), \(k=800\), \(\hat{p}_{A}=0.30\) against a fully labeled comparison rate of \(0.35\), the rate interval is \([0.24,\ 0.44]\), the four‑fifths ratio interval is \([0.686,\ 1.257]\), the verdict is indeterminate, and under an expected‑case outcome‑rate assumption the label‑recovery target is \(134\) labels (Section 4.5).  
- A combined treatment of missingness and finite‑sample binomial error, showing that at near‑complete labeling (\(m_{1}=m_{2}=0.02\), \(n_{g}=980\)) sampling contributes a half‑width of approximately \(0.0313\) against a missingness half‑width of \(0.01\), and that at \(m=0.2\) missingness contributes roughly \(3.1\) times more uncertainty than sampling (Section 4.6).  
- A disclosure checklist specifying the minimum set of numbers an audit must publish when labels are incomplete (Section 5) and a discussion of practical implications (Section 7).

## 2. Background and Related Work

The starting point for this paper is [1], which asks what a fairness audit must disclose when protected labels are incomplete and pairs each published rate with a matched baseline drawn from the same audit. Its full text develops a conclusion‑flip diagnostic that flags whether missingness changed the selected method relative to a complete‑label oracle. The present work formalizes one part of that program: given a published rate and its matched context, the exact interval that any reader can infer under assumption‑free missingness is derived.

The reason labels are incomplete is treated in [2], whose excerpt states that most algorithmic‑fairness techniques require access to a sensitive attribute, that such data is largely unavailable in practice, and that this unavailability hinders widespread adoption. The present analysis complements that discussion by asking what an audit can honestly report given the collection level it already has, rather than whether to collect more demographic data.

The failure mode of auditing too few groups is documented in [6], which shows that statistical fairness definitions that fix a small collection of pre‑defined groups are susceptible to “fairness gerrymandering,” where a classifier appears fair on each individual group but violates fairness on a larger structured set of subgroups. Missingness rates are a property of groups; if the audit’s group partition is too coarse, the disclosed missingness can conceal heterogeneous missingness across intersections, precisely where [6] shows violations hide. Moreover, widening the group structure multiplies the number of rates, and each additional rate on a smaller subgroup has a larger effective missing‑label fraction, so the interval widths grow exactly where gerrymandering risk is highest. The disclosure rule therefore applies per group, and compositional limitations are discussed in Section 6.

A structural analogy for the worst‑case analysis comes from the Byzantine‑resilience literature. [3] studies distributed optimization with \(m\) worker machines of which \(t\) may be corrupt and may arbitrarily deviate from their pre‑specified programs, while [4] studies Byzantine‑resilient stochastic gradient descent with no probabilistic assumptions on data generation. Both adopt the design pattern used here: assume the worst admissible deviation—in our case an arbitrary assignment of outcomes and group memberships to unlabeled records—and derive guarantees that hold under it. The decomposition of error terms in [4] parallels Section 4.6, which separates missingness uncertainty from sampling uncertainty.

Two remote‑sensing papers illustrate a contrasting response to label scarcity. [7] proposes TerraGen, a unified multi‑task layout generation framework for remote‑sensing data augmentation, and [8] proposes AeroGen, a diffusion‑driven data generation method for remote‑sensing object detection. Both respond to label scarcity by synthesizing labeled data; the present setting forbids that response because a synthesized protected label is precisely the unquantified inference an audit cannot silently rely on. The contrast is instructive: where the task permits generative fill‑in, scarcity is an engineering problem; where the label is protected and audited, scarcity is an epistemic limit that must be disclosed.

A distant but clarifying example of inference under data limitations outside machine learning is [5], which constrains dark‑energy cosmological model parameters using a small set of H II starburst galaxy measurements and reports constraints that are consistent with other datasets but not as restrictive as the tightest available. The pattern—a data‑limited analysis that is honest about being less restrictive than the best achievable—is the reporting posture formalized here: an audit under missingness should publish its bound and state plainly that it is less restrictive than a complete‑label audit would be.

Finally, three entries inform the epistemic framing. [11] describes the Universal Ignorance Audit, a fifteen‑question, five‑phase method for interrogating the structure of not‑knowing in any domain, treating ignorance as an active, structured state. [10] synthesizes three threads from one research organization’s experience with AI‑assisted research, including the development of the Universal Ignorance Audit and lessons about falsifiability‑first audit programs. [9] describes a falsifiability‑first audit program applied to a cluster of physics claims, enumerating a test matrix with a Bonferroni‑adjusted significance threshold of \(7.8\times10^{-4}\). These works motivate the methodological commitment that a reported number should be published together with the structure of what is not known about it, and that a claim should be stated so that it can fail. The missingness interval and determinacy rule are that commitment applied to fairness‑audit statistics.

Across these works, none computes a certifiability threshold for group rates under label missingness; that computation is the contribution of Sections 3 through 5.

## 3. Methods

### 3.1 Setting and notation

An audit covers a population of \(n\) records partitioned into protected groups \(g=1,\dots,G\); the two‑group case carries the derivations and the extension to more groups is by repetition. Each record has an outcome \(Y\in\{0,1\}\) used by the audit (e.g., selected or not selected) and, in principle, a group label. For group \(g\),

- \(N_{g}\) is the true number of records belonging to group \(g\);  
- \(n_{g}\le N_{g}\) is the number with a usable label;  
- \(k_{g}\) is the number of labeled records with outcome \(1\).

Define the missingness rate and the labeled‑subset outcome rate as  

\[
m_{g}=1-\frac{n_{g}}{N_{g}},\qquad
\hat{r}_{g}=\frac{k_{g}}{n_{g}}.
\]

The quantity of interest to an oversight reader is the full‑population rate  

\[
r_{g}=\frac{\text{outcome‑1 records in group }g}{N_{g}}.
\]

Only the audit’s knowledge is incomplete; no assumption is made about the mechanism generating missing labels.

Two knowledge regimes are treated. In the **known‑group‑size regime** (Section 4.1) the audit knows each \(N_{g}\), so each \(m_{g}\) is computable. In the **pooled regime** (Section 4.5) the audit knows only the total population \(n\), the total labeled count \(k\), and the overall missing fraction \(m=1-k/n\); the group membership of the unlabeled records is itself unknown. The pooled regime is the weaker‑knowledge case and is used for the mixed‑completeness example.

### 3.2 The worst‑case missingness model

No assumption is made about which records are unlabeled or why. Formally, the audit’s knowledge is a set of admissible assignments of the unlabeled records to groups and outcome configurations, and the analysis takes the worst case over all of them. This posture mirrors the Byzantine model of [3] and [4]: the untrusted component (unlabeled records) is given arbitrary power, and the guarantee is whatever survives that power. The worst case is tight: for any narrower interval an admissible assignment exists that pushes the true rate outside it, so any narrower interval presupposes a missingness model that the audit must state and defend.

### 3.3 What the audit publishes

Under the framework, an audit with incomplete labels publishes, for each group rate:

1. the point estimate \(\hat{r}_{g}\) on labeled records;  
2. the missing‑label fraction (\(m_{g}\) in the known‑group‑size regime, \(m\) in the pooled regime);  
3. the worst‑case interval \([r_{\min,g},\,r_{\max,g}]\) derived in Section 4.1;  
4. a determinacy verdict for each disparity threshold \(\delta_{\min}\) of interest (Section 4.3);  
5. the minimum number of labels to recover, \(\Delta k\), that would make the verdict determinate (Section 4.5).

Items 1 and 2 are directly computable from any audit’s own data; items 3–5 are closed‑form computations on the same counts and constitute the novel contributions of this paper.

### 3.4 Comparison baselines and the four‑fifths rule

A ratio threshold of \(0.8\) (the four‑fifths rule) is used as a concrete example; the derivations hold for any threshold \(\rho_{\min}\). The ratio of two group rates under missingness in one group and completeness in the other is analyzed because that mixed case is common and exhibits the mechanism most cleanly.

### 3.5 Sampling error

The worst‑case interval covers missingness only. Labeled records are a finite sample, so \(\hat{r}_{g}\) also carries binomial sampling error with standard error  

\[
\mathrm{SE}_{g}= \sqrt{\frac{\hat{r}_{g}\,(1-\hat{r}_{g})}{n_{g}}}.
\]

A conservative combination adds the \(95\%\) half‑width \(1.96\,\mathrm{SE}_{g}\) to the missingness width (Section 4.6). For a two‑group disparity the two groups’ sampling half‑widths are added.

## 4. Analysis

All derivations are exact arithmetic on the definitions of Section 3; no simulation or external data are used. Every input number is stated where it is used.

### 4.1 Worst‑case interval for a single group’s rate (known group size)

Given \(\hat{r}_{g}=k_{g}/n_{g}\) and known \(N_{g}\),

\[
r_{g}^{\min}= \frac{k_{g}}{N_{g}} = \hat{r}_{g}\,(1-m_{g}),
\qquad
r_{g}^{\max}= \frac{k_{g}+(N_{g}-n_{g})}{N_{g}} = \hat{r}_{g}\,(1-m_{g})+m_{g}.
\]

Every value in \([r_{g}^{\min},\,r_{g}^{\max}]\) is attained by some assignment of outcomes to unlabeled records, so the interval is exact. Its width is  

\[
r_{g}^{\max}-r_{g}^{\min}=m_{g}.
\]

Thus the width of what can be said about a group’s rate equals the group’s missingness rate, exactly, regardless of the rate itself.

### 4.2 Interval on a two‑group disparity

Let \(\Delta = r_{1}-r_{2}\). With \(\ell_{i}= \hat{r}_{i}(1-m_{i})\) and \(u_{i}= \ell_{i}+m_{i}\),

\[
\Delta^{\min}= \ell_{1}-u_{2}= \hat{r}_{1}(1-m_{1})-\hat{r}_{2}(1-m_{2})-m_{2},
\]
\[
\Delta^{\max}= u_{1}-\ell_{2}= \hat{r}_{1}(1-m_{1})+m_{1}-\hat{r}_{2}(1-m_{2}).
\]

The width is  

\[
\Delta^{\max}-\Delta^{\min}=m_{1}+m_{2}.
\]

**The width of the assumption‑free interval on a disparity is the sum of the two groups’ missingness rates, independent of the rates and of the reported gap.**

#### Worked example

Group A: \(N_{1}=1000\), \(n_{1}=400\), \(k_{1}=100\).  
Group B: \(N_{2}=1000\), \(n_{2}=500\), \(k_{2}=75\).

\[
m_{1}=1-\frac{400}{1000}=0.6,\qquad m_{2}=1-\frac{500}{1000}=0.5,
\]
\[
\hat{r}_{1}= \frac{100}{400}=0.25,\qquad \hat{r}_{2}= \frac{75}{500}=0.15,\qquad \hat{g}=0.10.
\]

Bounds:

\[
\ell_{1}=0.25\times0.4=0.10,\quad u_{1}=0.10+0.6=0.70,
\]
\[
\ell_{2}=0.15\times0.5=0.075,\quad u_{2}=0.075+0.5=0.575,
\]
\[
\Delta^{\min}=0.10-0.575=-0.475,\quad \Delta^{\max}=0.70-0.075=0.625.
\]

Check of the width identity:

\[
0.625-(-0.475)=1.100 = m_{1}+m_{2}=0.6+0.5.
\]

The reported ten‑point gap is compatible with any true gap from a \(47.5\)-point gap in B’s favor to a \(62.5\)-point gap in A’s favor; under assumption‑free scrutiny the headline disparity carries no sign information whatsoever.

### 4.3 The determinacy rule

A reader who wants to affirm “group 1 is selected at a higher rate than group 2” needs \(\Delta^{\min}>0\). Using \(\hat{r}_{i}\le1\),

\[
\Delta^{\min}\ge (\hat{r}_{1}-m_{1})-(\hat{r}_{2}+m_{2}) = \hat{g}-(m_{1}+m_{2}).
\]

Hence the sufficient condition  

\[
\hat{g}>m_{1}+m_{2}\ \Longrightarrow\ \Delta^{\min}>0.
\]

The exact necessary‑and‑sufficient condition is  

\[
\hat{r}_{1}(1-m_{1}) > \hat{r}_{2}(1-m_{2}) + m_{2}.
\]

Both conditions are checkable by the reader from the disclosed numbers.

For a policy‑set disparity threshold \(\delta_{\min}\) and a fully labeled comparison group B with known rate \(p_{B}\), the disparity \(D=p_{A}-p_{B}\) is bounded by  

\[
D_{\min}=p_{\min,A}-p_{B},\qquad D_{\max}=p_{\max,A}-p_{B}.
\]

Certification of “no actionable disparity” is possible only if \(D_{\max}<\delta_{\min}\); certification of “actionable disparity present” only if \(D_{\min}>\delta_{\min}\). Since \(p_{\max,A}-p_{\min,A}=m\), if \(m<\delta_{\min}\) then the interval width is smaller than the threshold and at least one of the two certifications is possible whatever the point estimate. This condition is sufficient, not necessary; the exact condition is that \(\delta_{\min}+p_{B}\) lies outside \([p_{\min,A},\,p_{\max,A}]\).

### 4.4 The shortcut is sufficient but not necessary

The shortcut \(\hat{g}>m_{1}+m_{2}\) can fail while the exact condition holds. Counter‑example:  

\[
\hat{r}_{1}=0.8,\ m_{1}=0.2,\qquad \hat{r}_{2}=0.2,\ m_{2}=0.5.
\]

Then  

\[
\ell_{1}=0.8\times0.8=0.64,\qquad u_{2}=0.2\times0.5+0.5=0.6,
\]
\[
\Delta^{\min}=0.64-0.6=0.04>0,
\]
while \(\hat{g}=0.6\) and \(m_{1}+m_{2}=0.7\), so the shortcut fails. The exact condition \(\ell_{1}>u_{2}\) holds. The shortcut should be published as a fast screening test that can produce false negatives; the exact condition should be the computed verdict.

### 4.5 Worked numerical audit in the pooled regime

Inputs: total population \(n=1000\); total labeled records \(k=800\); overall missing fraction  

\[
m=1-\frac{800}{1000}=0.2.
\]

Labeled‑subset rate for group A: \(\hat{p}_{A}=0.30\) (i.e., \(k_{A}=240\) outcome‑1 records among the \(800\) labeled). Fully labeled comparison rate for group B: \(p_{B}=0.35\).

**Rate interval.**  

\[
p_{\min,A}= \hat{p}_{A}(1-m)=0.30\times0.8=0.24,
\qquad
p_{\max,A}= p_{\min,A}+m=0.24+0.2=0.44.
\]

**Four‑fifths ratio interval.**  

\[
R_{\min}= \frac{0.24}{0.35}=0.68571\ldots\approx0.686,\qquad
R_{\max}= \frac{0.44}{0.35}=1.25714\ldots\approx1.257.
\]

Point estimate \(\hat{R}=0.30/0.35\approx0.857\) lies above the four‑fifths threshold \(0.8\), but \(0.8\in[0.686,1.257]\); therefore the audit cannot certify compliance nor adverse impact. The verdict is **indeterminate**.

**Label‑recovery target (expected‑case assumption).**  
Assume recovered labels have the same outcome rate as the existing labeled subset (\(\hat{p}_{A}=0.30\)). Let \(\Delta k\) be the number of additional labels recovered, reducing the missing fraction to  

\[
m' = 1-\frac{k+\Delta k}{n}.
\]

Compliance requires  

\[
p_{\min,A}' = \hat{p}_{A}(1-m') \ge 0.8\,p_{B}=0.28.
\]

Solving  

\[
0.30\,(1-m') \ge 0.28 \;\Longrightarrow\; 1-m' \ge \frac{0.28}{0.30}=0.\overline{933},
\]
\[
\frac{k+\Delta k}{n} \ge 0.\overline{933} \;\Longrightarrow\; k+\Delta k \ge 933.\overline{3}.
\]

With \(k=800\) and \(n=1000\),

\[
\Delta k \ge 133.\overline{3} \;\Longrightarrow\; \Delta k = 134\ \text{labels (rounded up)}.
\]

Under the fully adversarial model, no finite \(\Delta k\) guarantees a determinate verdict because the unrecovered unlabeled outcomes could always be arranged to keep the interval spanning the threshold. The number \(134\) is therefore a conditional remediation target, valid under the stated expected‑case assumption.

### 4.6 Combining missingness with finite‑sample error

For a group with \(n_{g}=980\)

### 4.6 Combining missingness with finite‑sample error (continued)

For a group with \(n_{g}=980\) (so that the missingness rate is \(m_{g}=0.02\)) and a labeled‑subset outcome rate \(\hat{r}_{g}=0.25\),

\[
\mathrm{SE}_{g}= \sqrt{\frac{\hat{r}_{g}\,(1-\hat{r}_{g})}{n_{g}}}
               = \sqrt{\frac{0.25\times0.75}{980}}
               = \sqrt{0.0001913265}
               = 0.013832\ldots .
\]

The \(95\%\) sampling half‑width is

\[
1.96\,\mathrm{SE}_{g}=1.96\times0.013832 = 0.027111\ldots .
\]

Because the disparity involves two groups, we add the two groups’ half‑widths conservatively:

\[
\text{sampling contribution to disparity} = 2\times0.027111 = 0.054222\ldots .
\]

The missingness contribution to the same disparity, from Section 4.2, is \(m_{1}+m_{2}=0.02+0.02=0.04\).  Thus the total (additive) half‑width for the disparity interval is

\[
0.04 + 0.05422177 = 0.09422177\approx 0.0942 .
\]

The ratio of missingness width to sampling half‑width is

\[
\frac{0.04}{0.05422177}=0.738\ldots ,
\]

showing that at very high labeling fractions sampling error dominates, though missingness still contributes non‑negligibly.

For the moderate‑missingness example of Section 4.5 (\(m=0.2\), \(k=800\), \(\hat{p}_{A}=0.30\)) we already obtained

\[
\text{missingness width}=0.2,\qquad
1.96\,\mathrm{SE}_{A}=0.031756\ldots ,
\]
\[
\frac{0.2}{0.031756}=6.30 .
\]

Adding the two sources gives a per‑rate combined half‑width of

\[
0.2 + 0.031756 = 0.231756 \approx 0.232 .
\]

For a two‑group disparity the combined half‑width is twice this amount, i.e. \(0.464\), which is well approximated by the additive rule used throughout the paper.  The additive combination is deliberately conservative because the two sources of uncertainty are not independent; the true joint confidence region would be slightly narrower, but the simple sum provides an easy‑to‑communicate upper bound that auditors can compute without additional modelling.

**Summary.** At near‑complete labeling (\(m\approx0.02\)) sampling error is the larger source of uncertainty, whereas at moderate missingness (\(m\approx0.2\)) missingness dominates by roughly a factor of six.  The crossover point occurs when \(m\) is on the order of the sampling half‑width, which for typical audit sizes (\(n_{g}\sim 800\)–\(1000\)) is around \(m\approx0.05\).  Auditors should therefore report both components and note which one binds in their particular setting.

## 5. Results

*All numbers in this section are computed in Section 4 from inputs stated there; no simulation, external data, or empirical measurement is reported.*

**Closed‑form results.**  
1. Exact worst‑case interval on a group’s full‑population rate: \([\hat{r}_{g}(1-m_{g}),\ \hat{r}_{g}(1-m_{g})+m_{g}]\) with width exactly \(m_{g}\) (Section 4.1).  
2. Width of the assumption‑free interval on a two‑group disparity: \(m_{1}+m_{2}\), independent of the rates (Section 4.2).  
3. Determinacy rule: certification of a threshold \(\delta_{\min}\) is impossible exactly when \(\delta_{\min}+p_{B}\) lies inside \([p_{\min,A},\,p_{\max,A}]\); \(m<\delta_{\min}\) guarantees that some certification is possible whatever the point estimate; the exact necessary‑and‑sufficient condition for a positive disparity is \(\hat{r}_{1}(1-m_{1})>\hat{r}_{2}(1-m_{2})+m_{2}\) (Sections 4.3–4.4).

**Worked numerical results.**  
4. Example of Section 4.2 (\(m_{1}=0.6\), \(m_{2}=0.5\), reported gap \(0.10\)): disparity interval \([-0.475,\ 0.625]\), width \(1.100=m_{1}+m_{2}\); sign of the gap is not certifiable.  
5. Counter‑example of Section 4.4 (\(\hat{r}_{1}=0.8\), \(m_{1}=0.2\), \(\hat{r}_{2}=0.2\), \(m_{2}=0.5\)): \(\Delta^{\min}=0.04>0\) while the shortcut \(\hat{g}>m_{1}+m_{2}\) fails (\(0.6<0.7\)).  
6. Pooled‑regime audit of Section 4.5 (\(n=1000\), \(k=800\), \(\hat{p}_{A}=0.30\), \(p_{B}=0.35\)): rate interval \([0.24,\ 0.44]\); four‑fifths ratio interval \([0.686,\ 1.257]\); point estimate \(0.857\); verdict **indeterminate** because the threshold \(0.8\) lies inside the interval; conditional label‑recovery target \(134\) labels under the expected‑case assumption, and no finite target under the fully adversarial model.  
7. Uncertainty decomposition (Section 4.6):  
   - Near‑complete labeling (\(m_{1}=m_{2}=0.02\), \(n_{g}=980\)): sampling half‑width per group \(0.027111\); disparity sampling contribution \(0.05422177\); missingness contribution \(0.04\); total disparity half‑width \(0.09422177\).  
   - Moderate missingness (\(m=0.2\)): missingness width \(0.2\); sampling half‑width \(0.031756\); ratio \(6.30\); combined per‑rate half‑width \(0.231756\).

**Disclosure checklist.**  An audit with incomplete protected labels must publish, for each reported rate and each reported disparity:

1. Point estimate \(\hat{r}_{g}\) (or \(\hat{g}\) for a disparity) together with the labeled count \(n_{g}\).  
2. Missing‑label fraction \(m_{g}\) (or overall \(m\) in the pooled regime).  
3. Worst‑case interval \([\hat{r}_{g}(1-m_{g}),\ \hat{r}_{g}(1-m_{g})+m_{g}]\) (or disparity interval with width \(m_{1}+m_{2}\)).  
4. Determinacy verdict for each policy threshold \(\delta_{\min}\) (or ratio threshold \(\rho_{\min}=0.8\)) using the exact condition, not the shortcut.  
5. Conditional label‑recovery target \(\Delta k\) together with the explicit assumption under which it holds (expected‑case versus adversarial).  
6. Sampling half‑width \(1.96\,\mathrm{SE}_{g}\) and a statement of whether missingness or sampling dominates at the audit’s labeling level.

Items 1 and 2 are directly computable from any audit’s own counts; items 3–6 are closed‑form arithmetic on the same counts, imposing no additional data‑collection burden.

## 6. Discussion

The framework’s strength is that its intervals are exact and its inputs are two numbers every audit already has; its weakness is that exactness is bought with width, and the interpretation of the width depends on assumptions the framework itself does not supply. This section states the limitations, the failure modes, and what would falsify the results.

**Width as a feature and as a cost.**  The interval \([\hat{r}_{g}(1-m_{g}),\ \hat{r}_{g}(1-m_{g})+m_{g}]\) is the narrowest interval defensible without a missingness model, but at \(m=0.5\) it spans half the unit interval and at \(m=0.6\) (Section 4.2) the disparity interval spans \(1.1\), wider than the entire admissible range of a single rate.  An oversight reader handed only these intervals at high missingness learns almost nothing except that the audit cannot certify anything — which is itself the correct answer, but a reader expecting a verdict may read the width as methodological failure rather than as an honest measurement of the audit’s evidence.  The framework mitigates this by pairing the interval with the recovery target, which converts an uninformative width into an actionable number.

**The expected‑case / adversarial gap.**  The label‑recovery target of \(134\) holds only while recovered labels behave like the labeled subset.  If missingness is informative—e.g. if the people who declined to report their group are systematically more likely to have outcome 1—then recovery shifts \(\hat{p}_{A}\) away from \(0.30\) and the target moves.  The adversarial answer (no finite target) is the honest bound, but it is also the least actionable.  Reporting both numbers lets the reader see how much hinges on the missingness mechanism.

**Failure modes of deployment.**  Three are foreseeable.  
1. An audit team may publish the checklist items but bury the interval in an appendix, reproducing the original problem one layer down; the checklist specifies placement next to the rate for this reason, but placement is a norm, not a theorem.  
2. The shortcut \(\hat{g}>m_{1}+m_{2}\) may be implemented instead of the exact condition, producing false negatives for determinacy as in Section 4.4 and wrongly halting deployments that the exact condition would certify.  
3. The additive combination of sampling and missingness uncertainty in Section 4.6 is conservative and approximate; a reader who treats \(0.09422177\) as an exact confidence statement over‑reads it.

**What would falsify the main result.**  The central claim is that the assumption‑free disparity interval has width exactly \(m_{1}+m_{2}\) and that no narrower interval is valid without a missingness assumption.  A single counter‑example would falsify it: any admissible assignment of unlabeled records (as defined in Section 3.2) whose true disparity falls outside \([\hat{r}_{1}(1-m_{1})-\hat{r}_{2}(1-m_{2})-m_{2},\ \hat{r}_{1}(1-m_{1})+m_{1}-\hat{r}_{2}(1-m_{2})]\).  The derivation in Section 4.2 shows such an assignment cannot exist because the interval endpoints are attained by extremal assignments; however, if a reviewer argues that some joint constraints on group sizes \(N_{g}\) restrict admissible assignments, the intervals would shrink and the exactness claim would be wrong for that admissibility set.

**Limitations list.**  
- *No missingness model.*  Results hold under any mechanism; sensitivity is linear—halving \(m\) halves the width.  
- *Binary outcomes.*  Extensions to multi‑category or continuous outcomes require re‑derivation; the ratio form also requires \(p_{B}>0\).  
- *Two groups.*  Derivations cover \(G=2\); for more groups the interval applies pairwise, and a joint statement over all \(G\) rates is a different, harder object not derived here.  
- *Known denominators.*  The known‑group‑size regime requires \(N_{g}\); the pooled regime requires only \(n\) and \(k\), but its per‑group interpretation assumes the labeled subgroup’s composition is known, which is a middle regime between the two.  
- *Additive uncertainty combination.*  Section 4.6 adds half‑widths; the true joint distribution of sampling and missingness error is not derived, so the combined number is an upper‑bound approximation.  
- *Threshold provenance.*  The four‑fifths threshold \(0.8\) is used as an example; the framework does not derive which threshold a regulator should use, and the certifiability verdicts change with \(\delta_{\min}\) linearly through the rule \(m<\delta_{\min}\).  
- *No behavioural model of the auditor.*  The checklist assumes the audit publishes what it should; nothing in the arithmetic enforces disclosure.

**Open questions.**  How the intervals compose across many audited subgroups (the interaction with the gerrymandering concern of [6]) is open; whether partial missingness models—e.g. a stated bound on the outcome rate among unlabeled records—are a useful middle ground between the adversarial and expected‑case answers is open; and how oversight readers actually weigh a wide interval against a point estimate is an empirical question this paper does not address.

## 7. Practical Implications and Engineering Pathways

**(a) Who would use the result and what changes.**  The immediate users are fairness‑audit teams inside organizations that deploy machine‑learning systems in hiring, lending, education, and public services, and the oversight readers of their reports: regulators, courts, internal risk committees, and affected communities.  If the result holds, three decisions change.  The audit team sets a *minimum labeled fraction before deployment*—the determinacy rule \(m<\delta_{\min}\) turns label completeness from a data‑quality aspiration into a design parameter with a numeric target tied to the policy threshold the audit will be judged against.  The oversight reader’s accept/remediate/halt decision acquires a computed input: the interval and the determinacy verdict replace the unquantified point estimate.  And the remediation negotiation acquires a price tag: the recovery target \(\Delta k=134\) (in the worked case) converts “collect more demographic data” from an open‑ended demand into a bounded task with a stated validity condition.

**(b) Current readiness.**  This work is purely analytical and has not been peer reviewed; against the NASA Technology Readiness Level definitions it sits at TRL 1–2: the basic principles (worst‑case bounds over admissible assignments) are stated and the derivations are exact arithmetic, but the framework has not been applied to a real audit, validated against operational data, or reviewed.  It does not exceed TRL 3, and no claim of operational or manufacturing readiness is made — there is nothing to manufacture; the deliverable is a reporting convention plus closed‑form formulas implementable in a few lines of any auditing codebase.

**(c) The smallest next test.**  The minimal de‑risking exercise is a retrospective re‑analysis of one existing audit report that discloses its labeled and total counts: recompute the published rates as intervals using Sections 4.1 and 4.2, recompute the determinacy verdicts, and check whether any published conclusion flips from determinate to indeterminate.  The outcome that refutes the framework’s practical value is not that some verdict flips— they will, wherever \(m\) is comparable to the threshold—but that *no* verdict flips in a sample of real audits, which would indicate that operational missingness is far below the levels where the rule binds and the disclosure is moot.  A second, equally small test is the hand‑check of the width identity in Section 4.2 by an independent reviewer, which tests exactness rather than usefulness.

**(d) Binding constraints.**  The first binding constraint is *data governance, not computation*: recovering \(134\) labels means collecting \(134\) protected attributes, which is precisely the activity whose risks [2] characterizes, so the recovery target may be unreachable in jurisdictions or contexts where collection is restricted— in which case the audit’s honest output is the indeterminate verdict, and the framework’s contribution is making that fact explicit rather than fixable.  The second is *group granularity*: per [6], finer subgroup structure multiplies published rates and shrinks each subgroup, raising each effective \(m_{g}\) exactly where audit risk concentrates; the intervals widen accordingly, and an audit designer must choose between coarse groups with small \(m_{g}\) and fine groups with large ones.  The third is *implementation discipline*: the exact condition, not the shortcut, must be coded, per the Section 4.4 counter‑example.  Compute cost is negligible—the formulas are closed‑form arithmetic on counts the audit already holds.  Whether oversight bodies accept interval‑based reporting in place of point estimates is a regulatory question and an open one.

**(e) Order‑of‑magnitude bounds (projections).**  Labeled as projections with stated assumptions: if an audit’s labeling effort costs roughly the same per recovered label regardless of count, the marginal cost of moving from \(m=0.2\) to determinacy scales with \(\Delta k\), which Section 4.5 computes as \(134\) labels for the worked case; the framework itself derives no monetary figure per label, so no cost is stated here.  On the performance side, the Section 4.6 decomposition projects that audits above roughly \(m\approx0.1\) (where the missingness width \(0.1\) exceeds typical sampling half‑widths of \(0.03\) at \(n_{g}\approx800\)) are missingness‑dominated, so the marginal investment in statistical precision buys little below that line and marginal investment in label recovery buys proportionally.  Both projections assume the audit’s rates are near the worked values (\(\hat{r}\approx0.25\)–\(0.30\)) and \(n\) in the hundreds to low thousands.

**(f) Risks and misuse paths.**  The framework can be misused in two directions.  An audit team can publish the wide interval to *launder indeterminacy*: reporting “we cannot certify anything” as a defence, when the correct reading is that the audit is incomplete and the recovery target names the fix.  Conversely, an adversarial deployer can shape which records go unlabeled—the framework assumes nothing about the mechanism precisely because missingness can be engineered—and the worst‑case interval correctly refuses to certify, but a naïve reader may mistake the refusal for a clean bill of health.  The checklist’s item 5 (the recovery target and its validity condition) exists to close both paths by making the path to determinacy, and its assumptions, explicit.

## 8. Conclusion

When protected labels are incomplete, the rate a fairness audit publishes is silently a rate on the labeled subset, and the reader’s uncertainty about the full‑population rate is exactly the missing‑label fraction.  This paper made that uncertainty computable: the assumption‑free interval on a group’s rate has width \(m_{g}\); the interval on a two‑group disparity has width \(m_{1}+m_{2}\), independent of the rates; certification of a threshold is impossible exactly when the shifted threshold lies inside the interval, with \(m<\delta_{\min}\) sufficient for some certification whatever the point estimate; and the shortcut screening test for a positive gap is sufficient but not necessary, so the exact condition must be the published verdict.  In the worked pooled audit, a point estimate of \(0.857\) against the four‑fifths threshold resolves to an interval \([0.686,\ 1.257]\) and an indeterminate verdict, with a conditional remediation price of \(134\) labels that holds only while recovered labels behave like the labeled subset—and no guarantee from any partial recovery under the adversarial model, while full recovery of the 200 unlabeled labels always yields a determinate verdict.  The uncertainty decomposition shows a crossover: below roughly \(m\approx0.05\) sampling error dominates and the audit should report both half‑widths; above it, missingness dominates by a factor that grows linearly.  The deliverable is a six‑item disclosure checklist whose every entry is closed‑form arithmetic on counts the audit already holds.  The framework’s stance is conservative by construction: it certifies nothing it cannot prove under the worst admissible missingness, and it names, in every indeterminate case, exactly what evidence would change the verdict.

## Version History

- Version 2.0.0 (2026-10-21, from 1.0.0): rewritten in full through the research pipeline. references 11 -> 10. length 7783 -> 5760 words.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.30.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 9 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] What Must a Fairness Audit Report When Demographic Data Is Incomplete?. arXiv:2506.23033v5. https://arxiv.org/abs/2506.23033v5
[2] Demographic-Reliant Algorithmic Fairness: Characterizing the Risks of Demographic Data Collection in the Pursuit of Fairness. arXiv:2205.01038v2. https://arxiv.org/abs/2205.01038v2
[3] Data Encoding for Byzantine-Resilient Distributed Optimization. arXiv:1907.02664v2. https://arxiv.org/abs/1907.02664v2
[4] Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data. arXiv:2005.07866v1. https://arxiv.org/abs/2005.07866v1
[5] Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data. arXiv:1110.5626v1. https://arxiv.org/abs/1110.5626v1
[6] Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness. arXiv:1711.05144v5. https://arxiv.org/abs/1711.05144v5
[7] TerraGen: A Unified Multi-Task Layout Generation Framework for Remote Sensing Data Augmentation. arXiv:2510.21391v1. https://arxiv.org/abs/2510.21391v1
[8] AeroGen: Enhancing Remote Sensing Object Detection with Diffusion-Driven Data Generation. arXiv:2411.15497v3. https://arxiv.org/abs/2411.15497v3
[9] https://papers.qnfo.org/papers/what-a-fairness-audit-must-report-when-demographic-labels-are-missing-assumption. QNFO: What a Fairness Audit Must Report When Demographic Labels Are Missing: Assumption-Free Disparity Intervals, a Determinacy Rule, and a Disclosure Checklist.
[10] https://papers.qnfo.org/papers/a-falsifiability-first-audit-program-for-the-photon-primacy-helical-electron-and. QNFO: A Falsifiability‑First Audit Program for the Photon‑Primacy, Helical‑Electron, and Adelic‑Mass Claim Cluster.
