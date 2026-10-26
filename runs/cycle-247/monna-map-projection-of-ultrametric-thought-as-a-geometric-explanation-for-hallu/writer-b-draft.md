# The Monna Map Projection of Ultrametric Thought: A Geometric Derivation of Information Loss in Token Generation and Its Relation to Hallucination

## Abstract

Large language models (LLMs) hallucinate: they emit fluent text that asserts content absent from, or contradicted by, their training evidence and their inputs. Mitigation today is largely empirical, and no accepted theory predicts which content will be lost before generation. This paper develops and quantifies a geometric hypothesis: token generation is a Monna-map-like projection from a hierarchical (ultrametric) embedding space onto a linear token stream, so that hallucination is the inevitable information loss of a many-to-one, order-reversing flattening, analogous to decoherence. We formalize the knowledge space as a rooted ultrametric tree of depth $L$ and branching $b$, define generation as digit truncation under the Monna map, and derive the distinguishable-fraction of source configurations, the mutual information between source and output, and a depth-dependent irrecoverable-content floor. For a binary tree of depth $L=20$ read through $k=10$ output digits, only $2^{k-L}=9.765625\times 10^{-4}$ of source leaf configurations remain distinguishable, $10$ bits are lost, and, under an assumed geometric depth distribution with parameter $q=0.7$, at least $1.92\times 10^{-2}$ of queried facts fall below the truncation depth and are structurally unrecoverable. The derivation predicts that deep-tree details become least significant output digits, gives a testable correlation between hallucination frequency and conceptual depth, and reframes existing mitigation results as partial increases of the effective digit budget $k$.

## 1. Introduction

Every production deployment of a large language model faces hallucination: the model produces fluent, confident output that asserts facts not supported by its training data or its prompt. The operators who face the problem daily are the teams running retrieval-augmented assistants, coding agents, and clinical or legal drafting tools; the cost is concrete — verification labor on every output, failed deployments in domains that demand citations, and user distrust that no amount of benchmark score removes. Current practice treats hallucination as a data or alignment problem: more instruction tuning, more retrieval, more post-hoc filtering. What is missing is a predictive account — a theory that says, before generation, which kinds of content a model must lose and why, so that mitigation can be targeted rather than uniform.

This paper argues that a candidate for such an account comes from a surprising corner of mathematics. If the internal representation of knowledge in an LLM is organized as an ultrametric tree — a hierarchy in which distance between concepts is the depth of their lowest common ancestor — then emitting a linear token stream is a projection of that tree onto a line. The canonical such projection is the Monna map, the digit-order-reversing map from the $p$-adic integers $\mathbb{Z}_p$ onto the unit interval $[0,1)$. A projection of a high-dimensional hierarchical structure onto a low-dimensional linear order is necessarily many-to-one: distinct configurations of the source collapse onto identical outputs. The claim examined here is that hallucination is, at least in part, exactly this collapse — the information that cannot survive the flattening, lost the way quantum coherence is lost under coarse-graining, not as noise but as structure.

If the claim holds, the practical consequence is a change in what mitigation can do. A geometric account predicts which content is lost: distinctions that live deep in the conceptual tree are mapped to the least significant digits of the output stream, so the deepest required detail is the first to go. It predicts a measurable correlation between hallucination frequency and the depth in a conceptual hierarchy of the fact being requested. And it converts mitigation into a resource-allocation question: how many effective output digits $k$ does a decoding strategy buy, and where in the tree should they be spent.

The idea originates in the QNFO corpus, which states the thesis qualitatively: communication is a Monna projection from an ultrametric tree of thought onto a linear timeline, and hallucinations are the inevitable information loss of this many-to-one map [9]. The present paper's contribution is to make the statement quantitative and falsifiable. The contributions are:

- A formal model of generation as Monna-map truncation on an ultrametric tree, with a proof-style derivation that deep-tree distinctions map to least significant output digits (Section 3 and Section 4.1).
- Closed-form computations of the distinguishable-fraction $f = b^{k-L}$, the mutual information $I(X;Y) = k\log_2 b$, and the information loss $\Delta I = (L-k)\log_2 b$, with worked numbers for binary and ternary trees (Section 4.2).
- A depth-dependent irrecoverable-content floor $P(\ell > k) = q^{k+1} - q^{L+1}$ under an assumed geometric depth distribution, computed as $1.92\times 10^{-2}$ for the reference parameters (Section 4.3).
- A positioning of this structural loss against the estimation-theoretic hallucination lower bounds of [4], the empirical ultrametricity of text found in [6], and the phase-wise and decomposition-based mitigation results of [5] and [2], yielding a unified reading and a proposed falsification experiment (Sections 5, 6, and 7).

## 2. Background and Related Work

**Ultrametric spaces as a substrate for hierarchy.** An ultrametric is a metric $d$ satisfying the strong triangle inequality $d(x,y) \leq d(x,z) \lor d(z,y)$, where $\lor$ is the maximum operator [1]. The immediate geometric consequence, central to everything below, is that all triangles are isosceles with the two long sides equal, and points partition into perfectly nested, disjoint balls — precisely the structure of a hierarchical classification. [1] proves ultrametric versions of the Arens–Eells isometric embedding theorem, the Hausdorff extension theorem, and the Niemytzki–Tychonoff characterization of compactness, using a $0$-dimensional Michael continuous selection theorem in place of the classical paracompact-space selection theorem. For this paper, the embedding and extension results matter because they establish that representing a knowledge base as an ultrametric space is mathematically well-posed: ultrametrics on subsets extend to ultrametrics on the whole, and abstract ultrametric spaces embed isometrically, so the tree model of Section 3 loses nothing by being stated in ultrametric language.

**Ultrametric models of mind.** [3] models Ignacio Matte Blanco's principles of symmetric and asymmetric being through ultrametric topology, reviewing p-adic and m-adic models of cognitive processes in which, quoting Anashin and Khrennikov, "mental entities are modeled as partially ordered balls" and "mental topology is ultrametric." That work distinguishes the dendritic wiring of the brain from the "mental trees" of reasoning and proposes p-adic dynamical systems over hierarchical encodings as a model of the subconscious, with the conscious controlling the "gigantic dynamical system" of the subconscious. The present paper takes the representational claim — reasoning lives on a hierarchy — and asks what happens when that hierarchy is serially emitted. [6] supplies the empirical anchor: analyzing dream corpora and other text collections of about 1000 texts and over 1.3 million words, it counts ultrametric-respecting triplets among approximately 1,996,997 triangles per word (nearly two million), baselined against approximately 4000 million triangles in total, and finds "very stable ultrametricity quantifications of the text collections" across choices of the most frequent words used and across triplet sampling. Words tied to personally significant relations ("Derek", a former relationship of the dreamer) show high counts of ultrametric relationships while a mere co-worker ("Mabel") shows low counts in the full 2000-word context. This is direct evidence that natural text carries measurable hierarchical (ultrametric) organization, which is the premise the truncation model needs.

**The Monna map.** The Monna map $\varphi$ sends a $p$-adic integer $x = \sum_{n\geq 0} a_n p^n$ to the real number $\sum_{n\geq 0} a_n p^{-(n+1)}$ in $[0,1)$: it reverses the order of significance of digits. [7] uses exactly this map as a transference device: although sequences in the $p$-adic integers with Poissonian pair correlations were known to exist, "no explicit examples had been found so far," and [7] shows how to transfer real sequences with Poissonian pair correlations — such as $\{\sqrt{n}\}$ away from perfect squares, the famous explicit example — to the $p$-adic setting via the Monna map, analyzing "the interaction of the Monna map $\varphi$ and the p-adic absolute value." Two features of that result matter here. First, the Monna map is a measure-theoretically well-behaved bridge between the $p$-adic world and the real interval, so statistics can be transported across it. Second, the map is order-scrambling: it preserves distributional fine structure while destroying the natural order of the source, which is exactly the behavior a serial emitter exhibits toward a hierarchical state.

**Projection as lossy compression.** [8] studies large-scale optimal transport map estimation, "a well-known challenging problem owing to the curse of dimensionality," where existing methods approximate the large-scale map "by a series of one-dimensional OTM problems through iterative random projection" and "suffer from slow or none convergence in practice due to the nature of randomly selected" projections. The parallel is structural: reducing a high-dimensional object to one-dimensional problems is exactly what token generation does to a hierarchical state, and [8]'s convergence difficulties are a reminder that the price of such reductions is not merely computational but informational — the one-dimensional slices can fail to capture the source. [8] develops a principled alternative (the SAVE dimension-reduction direction, with column space given by $E[\Var(Z|R)-I_d]^2$ and error bounds of the form $C_2 r^4 d^{-1/2}\|\widehat{\Sigma}_{\mathrm{SAVE}}-\Sigma_{\mathrm{SAVE}}\|_{\mathrm{max}}$), illustrating that choosing the projection direction carefully, rather than at random, is where the recoverable information lives. Section 4 computes, for the Monna truncation, exactly how much is not recoverable at any choice of direction.

**Hallucination as structural, not incidental.** [4] formalizes hallucination as "failures to link an estimate to any plausible cause" and proves that "even loss-minimizing optimal estimators still hallucinate," with "a general high probability lower bound on hallucinate rate for generic data distributions." Its experiments — a synthetic coin-flipping problem showing persistent $\delta$-hallucination under likelihood objectives, extended to large-scale LLM and text-to-image settings — support the conclusion that "hallucination is a structural property of the estimation process itself rather than just a symptom of limited models or datasets," so that "no amount of model capacity or data can eliminate hallucinations." The Bayes-optimal quadratic estimator is the conditional mean $A^*(X) = \E_{A(X)}[A(X)]$, and [4] proves $\delta$-hallucination persists even for $L$-Lipschitz estimators under tilted inputs. The present paper is complementary rather than competing: [4] locates the inevitability in the mismatch between loss minimization and diverse correct answers; the Monna-truncation model locates an additional, geometrically explicit inevitability in the serial emission of hierarchical state, and predicts where in the conceptual hierarchy the losses concentrate.

**Mitigation practice and its reading under the model.** [2] proposes Pelican, which "decomposes the visual claim into a chain of sub-claims based on first predicates" and verifies each with a program of thought, reporting improvement over state-of-the-art hallucination benchmarks for large vision-language models, whose hallucinations it attributes to sources including limited training data, over-reliance on language priors, and a yes-bias tendency. Under the truncation model, claim decomposition is precisely a way to raise the effective digit budget $k$ per sub-claim: a deep fact verified in isolation is queried at shallow effective depth, where truncation loss is small. [5] introduces PSRD, a phase-wise self-rewarding framework that "significantly reduces the hallucination of LLaVA-1.5-7B by $50.0\%$, as measured by the CHAIR metric on AMBER," without fine-tuning, and reports that "visual hallucination exhibits phase-wise dynamic patterns, peaking at the onset of each semantic phase." Its discussion observes that "discrimination is structurally more tractable than generation." The phase-wise peak is a striking fit for the truncation picture: at the onset of a new semantic phase the emitter re-projects a fresh subtree, and it is exactly at re-projection boundaries that the collapsed deep distinctions would first manifest as errors. [10] supplies the generative primitive underlying the picture: a calculus in which "the single foundational element ... is a basic syntactic token," a boundary drawn within an undifferentiated void, with "strictly recursive" combination rules that "allow for the construction of infinite complexity from a single starting point" — a formal model of generation as successive distinction-drawing, which is the discrete process the Monna map in Section 3 acts on. [11] contributes the epistemic caution this paper adopts: it proves an underdetermination theorem that "no finite set of first-person visual observations ... can distinguish an Archimedean substrate from an ultrametric substrate," because both render into the same image space, and states "the honest converse" that this "does not show the world is ultrametric." Applied here: behavioral evidence that a model's outputs are hierarchically organized cannot, by itself, prove the internal substrate is ultrametric; the ultrametric organization is a modeling postulate whose consequences are what we test.

## 3. Methods

**The model.** We model a trained model's knowledge relevant to a query as a rooted ultrametric tree $\mathcal{T}$ of depth $L$ and uniform branching $b$. Each leaf $\ell$ is an atomic fact or configuration; the depth of the lowest common ancestor of two leaves is their conceptual distance. This is the standard identification of finite ultrametric spaces with rooted trees, justified by the nested-ball structure that the strong triangle inequality forces [1] and by the empirical ultrametricity of text [6]. We assume uniform branching for tractability and state the sensitivity to this assumption in Section 6.

**Generation as Monna-map truncation.** Fix a prime $p$ with $p = b$ (any branching factor is a digit alphabet size; $p$ prime is the classical setting of $\mathbb{Z}_p$ [7]). A source configuration is a $p$-adic integer

$$x = \sum_{n=0}^{L-1} a_n p^n, \qquad a_n \in \{0,\dots,p-1\},$$

where the digit $a_n$ encodes the choice made at level $n$ of the tree: $a_0$ is the top-level category, $a_{L-1}$ the deepest detail. The Monna map is

$$M_p(x) = \sum_{n=0}^{L-1} a_n p^{-(n+1)},$$

which places digit $a_n$ at the $(n+1)$-th fractional position of the output. The emitted token stream has finite resolution: it carries $k$ significant digits, $k \leq L$. Generation is therefore the composite

$$\pi_k \circ M_p : \mathbb{Z}_p \supset \{0,\dots,p^L-1\} \to [0,1), \qquad \pi_k(y) = p^k \lfloor y \, p^{-k} \rfloor \text{ truncated to } k \text{ digits},$$

i.e., the output retains $a_0, \dots, a_{k-1}$ and discards $a_k, \dots, a_{L-1}$.

**Why this is the right idealization.** Three properties are used and only these. (i) Many-to-one: $\pi_k \circ M_p$ maps $p^{L-k}$ source configurations to each output token sequence, so it is a many-to-one projection, as required by the hypothesis. (ii) Order reversal: the Monna map inverts significance — the deepest tree digit $a_{L-1}$, which carries $p$-adic magnitude $p^{-(L-1)}$ in the source, appears at the last fractional position of the output, the least significant digit. This is the precise sense in which "deep-tree details become least significant digits," and it is inherited directly from the digit-reversal action of $M_p$ whose interaction with the $p$-adic absolute value is the operative mechanism in [7]. (iii) Measure preservation in the limit: $M_p$ transports $p$-adic uniform measure to Lebesgue measure on $[0,1)$, which is what licenses the counting arguments of Section 4 and is the same property that lets [7] transfer Poissonian pair correlations between the two settings.

**What is computed.** Section 4 derives, in order: the digit-position correspondence (which tree regions collapse where); the distinguishable fraction $f$ and mutual information $I(X;Y)$ under uniform source; the irrecoverable-content floor under a non-uniform depth distribution; and the ternary case as a robustness check. All inputs are either structural parameters ($b$, $L$, $k$, $p$), stated with their assumed values, or the geometric depth parameter $q$, stated as an assumption. No empirical measurement is performed in this paper; the connection to measured hallucination rates is made through the cited results of [4], [5], and [2] and through the falsification experiment proposed in Section 7.

**Decoherence analogy, made precise.** The claim that hallucination is "the cognitive counterpart of decoherence" [9] is formalized as follows: coarse-graining a state space by a many-to-one map increases the entropy of the conditional distribution of the source given the output, exactly as coarse-graining environment degrees of freedom destroys phase relations. The quantity computed in Section 4.2, $H(X \mid Y) = (L-k)\log_2 b$, is the analogue of the coarse-grained entropy; it is nonzero for every $k < L$ and grows linearly in the truncated depth.

## 4. Analysis

### 4.1 Digit-position correspondence: which tree regions collapse where

**Input:** the Monna map definition (Section 3; the map and its role as a transfer device between $p$-adic and real settings are from [7]). Source digit $a_n$ sits at tree level $n$, with $n = 0$ the root split and $n = L-1$ the deepest detail. Under $M_p$, $a_n$ appears at fractional position $n+1$ of the output. The output stream carries $k$ digits, so:

- Positions $1$ through $k$ of the output (magnitudes $p^{-1}$ down to $p^{-k}$) carry tree levels $0$ through $k-1$: the coarse hierarchy survives.
- Tree levels $k$ through $L-1$ have no output position: they are collapsed.

**Derivation of the collapse set.** Two source configurations $x \neq x'$ agree in their first $k$ digits ($a_0, \dots, a_{k-1}$ identical) and differ first at some level $n \geq k$. Then

$$|M_p(x) - M_p(x')| = \left|\sum_{n \geq n_0} (a_n - a_n') p^{-(n+1)}\right| \leq \sum_{n=n_0}^{L-1} (p-1) p^{-(n+1)} = p^{-n_0} - p^{-L} < p^{-k},$$

using the geometric sum $\sum_{n=n_0}^{L-1} (p-1)p^{-(n+1)} = p^{-n_0}(1 - p^{-(L-n_0)})$. Since the output resolution is $p^{-k}$, this difference is below the output's least significant digit: $x$ and $x'$ receive identical token sequences. Conversely, if $x, x'$ first differ at level $n_0 < k$, the difference is at least $p^{-(n_0+1)} - (p^{-1}\cdot p^{-(n_0+1)} + \dots) = p^{-(n_0+1)} - \frac{p-1}{p}\cdot\frac{p^{-(n_0+1)} - p^{-L}}{1 - p^{-1}}$; for $n_0 + 1 \leq k$ this exceeds $p^{-k}$, so the outputs differ. Hence the collapse is exactly the subtree below level $k$: **the map deletes the bottom $L - k$ levels of the tree and maps them to the truncated tail of the output.** This is the formal content of the claim that deep-tree details become least significant digits — indeed they become *no* digits, which is stronger and worse: truncation does not degrade deep detail gracefully, it erases it.

### 4.2 Distinguishable fraction, mutual information, and information loss (uniform source)

**Inputs (assumptions, stated):** binary tree, $b = p = 2$; tree depth $L = 20$; output digit budget $k = 10$. Source distribution uniform over the $b^L$ leaves.

**Step 1: number of source configurations.**

$$|\mathcal{X}| = b^L = 2^{20} = 1{,}048{,}576.$$

**Step 2: number of distinguishable outputs.** The output carries $k$ binary digits:

$$|\mathcal{Y}| = b^k = 2^{10} = 1{,}024.$$

**Step 3: distinguishable fraction.** Each output value is the image of exactly $b^{L-k} = 2^{10} = 1{,}024$ source configurations (Section 4.1), so the fraction of source leaf-pairs that remain distinguishable is

$$f = \frac{b^k}{b^L} = b^{k-L} = 2^{-10} = \frac{1}{1{,}024} = 9.765625 \times 10^{-4}.$$

Equivalently, the fraction of *pairs* of distinct source configurations that collapse to the same output is $1 - f = 0.9990234375$: under the model, more than $99.9\%$ of pairwise distinctions in the source are invisible in the output.

**Step 4: entropies.** With $X$ uniform on $b^L$ leaves and $Y = \pi_k(M_p(X))$:

$$H(X) = \log_2 b^L = L \log_2 b = 20 \times 1 = 20 \text{ bits},$$
$$H(Y) = \log_2 b^k = k \log_2 b = 10 \text{ bits},$$
$$H(X \mid Y) = \log_2 b^{L-k} = (L-k)\log_2 b = 10 \text{ bits}.$$

**Step 5: mutual information.**

$$I(X;Y) = H(X) - H(X \mid Y) = 20 - 10 = 10 \text{ bits}.$$

The output preserves exactly the top $k$ levels of the hierarchy and is independent of everything below them; the information loss is

$$\Delta I = H(X\mid Y) = (L-k)\log_2 b = 10 \text{ bits},$$

which is the coarse-grained entropy of the decoherence analogy and is strictly positive for every $k < L$.

### 4.3 Irrecoverable-content floor under a geometric depth distribution

Uniform depth is unrealistic: most queried facts live at moderate depth, with a thin tail of deep details. We assume the depth $\ell$ of a randomly queried fact follows a geometric distribution truncated at $L$:

$$\Pr[\ell = n] = (1-q)\, q^{\,n}, \qquad n = 1, \dots, L,$$

with assumed parameter $q = 0.7$ (a stated modeling assumption, not a measurement; sensitivity is discussed in Section 6). A fact at depth $\ell > k$ requires distinctions below the truncation level and is structurally unrecoverable: no decoding strategy can restore digits that were never emitted. The irrecoverable-content floor is

$$P_{\mathrm{floor}} = \Pr[\ell > k] = \sum_{n=k+1}^{L} (1-q) q^{\,n} = q^{k+1} - q^{L+1}.$$

**Arithmetic.** With $q = 0.7$, $k = 10$, $L = 20$:

$$q^{11} = 0.7^{11}.$$
$$0.7^2 = 0.49; \quad 0.7^4 = 0.49^2 = 0.2401; \quad 0.7^8 = 0.2401^2 = 0.05764801;$$
$$0.7^{10} = 0.7^8 \times 0.7^2 = 0.05764801 \times 0.49 = 0.0282475249;$$
$$0.7^{11} = 0.0282475249 \times 0.7 = 0.01977326743.$$
$$0.7^{20} = (0.7^{10})^2 = 0.0282475249^2 = 0.000797922663;$$
$$0.7^{21} = 0.000797922663 \times 0.7 = 0.000558545864.$$

Therefore

$$P_{\mathrm{floor}} = 0.01977326743 - 0.000558545864 = 0.01921472157 \approx 1.92 \times 10^{-2}.$$

Under these assumptions, at least $1.92\%$ of queried facts are unrecoverable *regardless of model quality*, because the information needed to express them was discarded at the projection step. This floor is additive in character with, and mechan