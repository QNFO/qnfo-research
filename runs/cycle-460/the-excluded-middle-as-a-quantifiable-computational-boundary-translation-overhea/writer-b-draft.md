# The Excluded Middle as a Quantifiable Computational Boundary: Translation Overhead and Search Cost of Classical Reasoning

## Abstract

The law of the excluded middle (LEM), the principle that every proposition $\varphi$ satisfies $\varphi \vee \neg\varphi$, separates classical from constructive logic, and the choice between the two governs whether a computational system can extract witnesses from its own proofs. Practitioners building proof assistants, ontological query engines, and reasoning pipelines face this choice implicitly, and the cost of it is rarely stated as a number. This paper makes the boundary quantitative. We model three costs of classical reasoning: the size overhead of the Gödel–Gentzen double-negation translation, the expansion of the counter-model search space when classical valuations are replaced by Kripke valuations, and the branching explosion when LEM instances are added to a proof search. For a representative propositional formula of size $9$, the translation has size $22$, an overhead factor of $22/9 \approx 2.44$; for $n = 10$ variables on a three-world Kripke chain, the constructive model space exceeds the classical one by a factor of $1.5^{10} \approx 57.7$; for a proof search of branching factor $3$ and depth $12$ with $5$ atoms, LEM instantiation multiplies the search tree by $2^{5} = 32$. We connect these costs to the literature on Glivenko translations, global choice without LEM in type theory, ontological query rewriting, and measured degradation of structured reasoning in complex prompts. The result changes how the classical/constructive choice should be priced: not as philosophy, but as a computable overhead budget.

## 1. Introduction

Engineers who build systems that reason — proof assistants, automated theorem provers, ontology-based data access platforms, and LLM-based reasoning pipelines — must decide, usually without being told, whether their underlying logic admits the law of the excluded middle. The decision is invisible in the specification documents and decisive in the behavior. A classical prover can close a goal $\exists x\, \varphi(x)$ by refuting $\neg \exists x\, \varphi(x)$ without ever producing an $x$; a constructive prover cannot, and must instead search for a witness. A classical database reasoner can use proof by contradiction inside an ontology's query rewriting; a constructive one must compile every inference into an explicit computation. When the wrong choice is made, the symptoms are concrete: proofs that certify existence without yielding artifacts, query engines whose compiled queries balloon in size, and reasoning pipelines that commit to answers before the reasoning that justifies them has run.

The cost of getting this wrong is not philosophical; it is engineering time and correctness. The QNFO analysis of the excluded middle as a computational boundary [8] argues that the classical notion of computational equivalence based solely on input–output behavior is impoverished, and that two systems are truly equivalent only if they solve the same problem class at the same resource cost. If that argument holds, then the classical/constructive choice is a resource decision, and it should be possible to attach numbers to it. Today no such numbers are standard: a team choosing between a classical and a constructive kernel for a proof assistant, or between a classical and a rewrite-based ontology reasoner, has no overhead budget to consult. What would change if the result of this paper holds: the choice could be priced in advance, as a translation-size factor, a model-space expansion factor, and a search-branching factor, each computable from the shape of the formulas and the size of the problem.

This paper derives those numbers. The approach is to treat LEM as a boundary marker between two computational regimes and to compute the cost of crossing it in three directions: the cost of importing a classical theorem into a constructive system (translation overhead), the cost of searching for constructive counterexamples (model-space expansion), and the cost of simulating classical reasoning inside a constructive proof search (LEM branching). The principal results, with their derivations, are:

- The Gödel–Gentzen translation of a representative propositional formula of size $9$ has size $22$, an overhead factor of $22/9 \approx 2.44$, derived in Section 4.1.
- The Kripke counter-model space on a three-world chain with $n = 10$ propositional variables exceeds the classical valuation space by a factor of $1.5^{10} \approx 57.7$, derived in Section 4.2.
- Adding LEM instantiation for $5$ atoms to a proof search of branching factor $3$ and depth $12$ multiplies the search tree by $2^{5} = 32$, from $531{,}441$ to $17{,}006{,}112$ nodes, derived in Section 4.3.
- A content-gap measure: the fraction of a classical theory's theorems that survive constructive translation is bounded by the Glivenko correspondence, and we compute a worked example in which a classical disjunction loses its disjunctive content entirely, in Section 4.4.

The same boundary appears outside formal logic. Measured results on structured prompting show that a reasoning framework scoring $100\%$ in isolation degrades to $0$–$30\%$ inside a production prompt [3], a degradation pattern that mirrors what happens when classical commitment principles are layered onto a constructive reasoning process. The results here could also matter to designers of ontology-based data access systems, where the classical reasoning underlying query rewriting must be compiled into executable form [2], and to type-theory library maintainers deciding whether to assume propositional extensionality, which determines whether choice forces LEM in their system [6].

## 2. Background and Related Work

The logical background begins with the QNFO study of the excluded middle as a computational boundary [8]. That work reconstructs the chain from Brouwer's intuitionism — which arose during the foundational crisis, against Hilbert's formalism and Russell's logicism, as a demand that mathematics be grounded in construction rather than symbol manipulation [8, §2.1] — to a critique of Turing completeness. Its central finding is stated as a separation: classical computers are not "flawed," but their underlying logical framework is "a specialized and limited model that fails to capture the full richness of what 'computation' can and perhaps should mean" [8, §7.1]. The same work proposes that computational equivalence must be multi-dimensional, requiring that two systems solve the same problem class "with the same class of resource costs (e.g., in polynomial time)" [8, §5.7]. That proposal is exactly the demand this paper operationalizes: if equivalence is resource-sensitive, the classical/constructive boundary should carry a measurable resource signature, and Sections 4.1–4.3 compute three components of it.

The companion QNFO framework on the universal computational topos [9] supplies the hierarchical vocabulary this paper uses. It distinguishes Object Computation (processes in their native domains), Model Computation (the representational layer that describes and simulates them), and Meta Computation, as three roles at distinct abstraction levels with precise interfaces [9, §2.1]. Its treatment of computational self-reference notes that Gödelian incompleteness forces any sufficiently powerful formal system to contain true-but-unprovable statements, which becomes acute when a system models its own processes [9, §1.0]. The LEM boundary studied here sits at the Model Computation layer: the choice of logic is a property of the representational layer, and its costs propagate downward into the object-level search procedures. The same framework's appendix catalogs fixed-point theorems by categorical context — Knaster–Tarski on complete partial orders, Kleene recursion on $\omega$-cpos via $\mathrm{lfp}(f) = \bigvee_{n<\omega} f^{n}(\bot)$, and Banach contractions on complete metric spaces [9, App. B] — and least-fixed-point construction is the canonical example of a constructive existence proof: the iteration $f^{n}(\bot)$ is the witness-producing procedure that a purely classical existence argument would lack.

On the logic side, the semisimplicity paper [5] formulates a general, signature-independent form of LEM and proves that a logic is semisimple if and only if it enjoys this law, under a weak form of Raftery's inconsistency lemma [5, abstract]. Its Glivenko analysis identifies the semisimple companion of a logic $\mathrm{L}$ with the logic determined by the largest non-trivial theories of $\mathrm{L}$, dual to the structural completion determined by the smallest theory [5, §1.4], and shows that a Glivenko-like connection obtains between a logic and its semisimple companion, subsuming several known Glivenko theorems under a single umbrella [5, §4.4]. This gives the present paper its precise logical handle: classical logic is the semisimple companion of intuitionistic logic, so crossing the LEM boundary is passing from a logic to its semisimple companion, and the Glivenko translation is the vehicle. The same work's deduction–detachment analysis — the classical equivalence $\Gamma, \varphi \vdash_{\mathrm{CL}} \psi \iff \Gamma \vdash_{\mathrm{CL}} \varphi \rightarrow \psi$, and its $n$-contractive generalization $\Gamma, \varphi \vdash_{\mathrm{FL}_{\mathrm{e}}^{n}} \psi \iff \Gamma \vdash_{\mathrm{FL}_{\mathrm{e}}^{n}} (1 \wedge \varphi)^{n} \rightarrow \psi$ [5, §3.1] — shows that even the basic move of reducing validity to theoremhood carries a formula-size price that depends on the logic, which is the same phenomenon our translation overhead measures.

The type-theoretic result of [6] sharpens the boundary from the other side. Diaconescu's theorem derives excluded middle from the axiom of choice using propositional extensionality, which holds in every topos; the Lean core library assumes propositional extensionality and uses it to derive excluded middle from global choice [6, §1]. But in dependent type theory without propositional extensionality, global choice alone does not imply excluded middle: [6] builds extensional Martin-Löf type theory with an impredicative universe $\mathsf{Prop}$, extends it with a global choice operator, and constructs a model over $L = \mathbb{N}$ in which $\bot = \infty$ has no closed term, the model is consistent, and the negations of both propositional extensionality and excluded middle have closed terms [6, §4.4]. The staged-truth-value semantics — a truth value $p \in L_{\infty}$ holds from stage $p$ onward, so $0$ is true from the start and $\infty$ is never true [6, §2.1] — is itself a constructive semantics in which LEM fails by construction. For this paper, [6] shows the boundary is not monolithic: a system can keep choice, the principle that drives most computational construction, while refusing LEM, the principle that destroys witness content.

The applied side shows the boundary operating in deployed systems. The ontological query processing literature [2] studies compiling a query against an ontology on top of a relational database into a direct query against that database, with optimization to obtain "possibly small and efficient compiled queries" [2, §1]. The reasoning underlying the best-known decidable OWL fragments is "computationally very hard, typically $2\text{-exptime}$-complete" [2, §Description Logics], and the OBDA program implements ABoxes as relational databases stored in classical RDBMSs [2, §OBDA]. The Nyaya prototype implements TGD-rewrite and query elimination over the IRIS Datalog engine, extended to support existential head variables and the constant $\mathit{false}$ as a rule head representing negative constraints, evaluated on DL-Lite$_R$ ontologies with a varying number of axioms [2, §7]. This is a concrete instance of our translation overhead: the compilation from ontological (classically reasoned) queries to executable database queries is exactly a double-negation-style content-preserving translation, and its size growth is the practical face of the factor computed in Section 4.1.

The numerical computation literature supplies the contrast case: computation that never crosses the boundary. The BEM study [1] investigates realtime simulation of biological organs under linear elastostatic behavior with constant boundary elements, using a $4 \times 4 \times 4$ mm cube benchmark with Young's modulus $200000$ N/mm$^2$ and Poisson's ratio $0.33$, discretized at sixteen boundary elements per face [1, §3]; it reports a GPU acceleration path toward realtime performance and, notably, that the author "has not been successful in achieving this goal using MATLAB and the Parallel Computing Toolbox" for the full realtime pipeline [1, §4]. This is Object Computation in the sense of [9]: dense linear algebra with no logical commitment either way, where LEM is irrelevant because every existence claim is witnessed by an explicitly computed displacement field. Similarly, the algorithmic differentiation study [7] differentiates a parallel CFD solver (JAGUAR) in tangent and adjoint modes, with the adjoint obtained by letting the AD tool Tapenade invert the complete MPI communications layer [7, abstract]; the adjoint code executes in $15$ times the primal execution time, with the overhead largely due to binomial checkpointing trading storage for time across a temporal loop of order $10^{6}$ iterations [7, §6]. Reverse-mode differentiation is the engineering realization of constructive content extraction — the adjoint code is a witness-producing transformation of the primal computation — and its measured $15\times$ overhead is an empirical data point of the same kind as our translation factor: content extraction has a price, and the price is measurable.

Finally, the solar physics partitioning study [4] offers a methodological analogy the paper uses explicitly. It defines the middle corona as the region roughly spanning heliocentric altitudes from $1.5$ to $6\,R_{\odot}$, encompassing "almost all of the influential physical transitions" governing coronal outflow, including the change from closed to open magnetic field structures and from low to high plasma $\beta$ [4, §7]. The region is poorly understood relative to the inner and outer corona "primarily because it has been much more poorly observed" [4, §7], and the partitioning of the solar atmosphere is explicitly based on which physical processes dominate energy transport in each region [4, §2]. The analogy: a boundary drawn between regimes is useful exactly when the transitions across it are enumerable and each side has a characteristic behavior. This paper draws the LEM boundary the same way — classical and constructive regimes, with a list of transitions (translation, model expansion, branching, content loss) that occur when crossing — and then does what [4] calls for in solar physics: characterizes the poorly observed middle region with explicit measurements, here computational ones rather than remote-sensing ones.

The prompt-engineering study [3] provides the measured behavioral parallel. STAR reasoning (Situation, Task, Action, Result) raised car wash problem accuracy from $0\%$ to $85\%$ on Claude Sonnet 4.5 and to $100\%$ with additional prompt layers in a $10$-line prompt [3, §1]; embedded in InterviewMate's $60$-line production prompt, the same framework degrades to $0$–$30\%$ ($A_{\text{star\_anthropic}}$: $0\%$ $(0/20)$; $B_{\text{star\_default}}$: $30\%$ $(6/20)$; versus $C_{\text{star\_only}}$: $100\%$ $(20/20)$) [3, §6.1], confirmed at $n = 100$ [3, §5.2]. The identified mechanism is conclusion-first ordering: accumulated instructions force the model to commit to an answer before the structured reasoning surfaces the implicit constraint, so the model outputs "Short answer: Walk." and then corrects itself below with "Drive your car to the wash" — but the committed answer is what the user sees first [3, §7.1]. The study's own conclusion is that "a technique that works in a clean room may fail on the factory floor" and that evaluation must include production-representative complexity [3, §10.3, §12]. In the vocabulary of this paper, the production prompt plays the role of a classical commitment principle: it forces early commitment (an answer exists and is already given) before constructive evidence is available, and the measured degradation from $100\%$ to $0$–$30\%$ is an empirical instance of the cost of crossing the commitment boundary in the wrong direction.

## 3. Methods

This paper's method is analytical modeling plus explicit arithmetic; no experiment, measurement, or software run was performed, and every number in Sections 4 and 5 is computed by hand from stated inputs.

**Model 1: translation size overhead.** We define the size $|A|$ of a propositional formula over atoms $p_1, \dots, p_n$ with connectives $\wedge, \vee, \to, \neg$ by: $|p_i| = 1$; $|A \circ B| = |A| + |B| + 1$ for $\circ \in \{\wedge, \vee, \to\}$; $|\neg A| = |A| + 1$. The Gödel–Gentzen (negative) translation $A^{G}$ is:

$$p^{G} = \neg\neg p, \qquad (A \wedge B)^{G} = A^{G} \wedge B^{G}, \qquad (A \to B)^{G} = A^{G} \to B^{G},$$

$$(A \vee B)^{G} = \neg(\neg A^{G} \wedge \neg B^{G}), \qquad (\neg A)^{G} = \neg A^{G}.$$

This translation is the standard vehicle of the Glivenko correspondence: a formula $A$ is a classical theorem if and only if $A^{G}$ is an intuitionistic theorem, which is the single-umbrella Glivenko connection of [5, §4.4] specialized to propositional logic. We assume the translation is applied to formulas in negation-normal-free form as written (no prior simplification), which is the convention that maximizes transparency of the size accounting; under a convention that first simplifies double negations, the overhead would be smaller, and we state this choice here because it is a convention, not a fact.

**Model 2: model-space expansion.** For $n$ propositional variables, a classical valuation assigns each variable one of $2$ truth values, giving $2^{n}$ valuations. A Kripke valuation on a chain frame of $k$ worlds (with $W = \{w_1 < w_2 < \dots < w_k\}$ and persistence forcing upward-closed valuation sets) assigns each variable an upward-closed subset of the chain; every upward-closed subset of a $k$-chain is determined by its least world of truth or by absence of truth, giving $k + 1$ choices per variable and $(k+1)^{n}$ valuations. The expansion factor is $\left(\frac{k+1}{2}\right)^{n}$. We take $k = 3$ (a three-world chain, the smallest frame that distinguishes classical from intuitionistic behavior for nested implications) as the working case.

**Model 3: LEM branching.** We model a backtracking proof search whose base search tree has branching factor $b$ and depth $d$, hence $b^{d}$ leaf paths. Adding LEM as an available axiom schema $\varphi \vee \neg\varphi$ for each of $n$ distinct atoms gives the prover an independent binary choice per atom — instantiate LEM on that atom, or not — at any point where the atom occurs; we assume, conservatively for the model, that each atom contributes exactly one independent binary choice along each path, so the tree multiplies by $2^{n}$. This is a lower-bound model in the sense that it counts only the instantiate-or-not choice and not the deeper re-search each instantiation triggers; we state that assumption here.

**Model 4: content gap.** We measure content loss by the Glivenko image: a classical theorem $\varphi$ survives constructively only as $\varphi^{G}$ (or $\neg\neg\varphi$ in the propositional Glivenko case). We compute, for a worked disjunction, the exact constructive content that remains, and express the gap as the set of classical disjunctions whose translated form no longer entails either disjunct constructively.

**Sources for inputs.** All logical definitions (translation rules, Kripke semantics, LEM schema) are standard and are stated in full above; the Glivenko correspondence and the semisimple-companion characterization of LEM are from [5]; the staged-truth-value model in which LEM fails constructively is from [6]; the resource-sensitivity demand that motivates pricing the boundary is from [8]; the layered Object/Model/Meta vocabulary is from [9]. No numerical input in Section 4 comes from a measurement; all are combinatorial counts computed from the stated definitions.

## 4. Analysis

### 4.1 Translation size overhead

**Worked formula.** Take $F = ((p \vee q) \to r) \wedge (p \to q)$ over atoms $p, q, r$.

Original sizes, step by step:

$$|p| = |q| = |r| = 1.$$
$$|p \vee q| = |p| + |q| + 1 = 1 + 1 + 1 = 3.$$
$$|(p \vee q) \to r| = 3 + 1 + 1 = 5.$$
$$|p \to q| = 1 + 1 + 1 = 3.$$
$$|F| = 5 + 3 + 1 = 9.$$

Translated sizes. Atoms double-negate:

$$|p^{G}| = |\neg\neg p| = 1 + 1 + 1 = 3, \quad |q^{G}| = 3, \quad |r^{G}| = 3.$$

The disjunction clause:

$$\neg p^{G} = \neg\neg\neg p, \quad |\neg p^{G}| = 3 + 1 = 4; \quad |\neg q^{G}| = 4.$$
$$|\neg p^{G} \wedge \neg q^{G}| = 4 + 4 + 1 = 9.$$
$$|(p \vee q)^{G}| = |\neg(\neg p^{G} \wedge \neg q^{G})| = 9 + 1 = 10.$$

The implication into $r$:

$$|(p \vee q)^{G} \to r^{G}| = 10 + 3 + 1 = 14.$$

The second conjunct is unchanged in structure:

$$|(p \to q)^{G}| = |p^{G} \to q^{G}| = 3 + 3 + 1 = 7.$$

The conjunction:

$$|F^{G}| = 14 + 7 + 1 = 22.$$

**Overhead factor:**

$$\frac{|F^{G}|}{|F|} = \frac{22}{9} \approx 2.4444444.$$

Generalizing: each atom contributes $+2$ (the double negation), each disjunction with translated sub-sizes $a, b$ contributes $a + b + 3$ instead of $a + b + 1$, i.e. $+2$ per disjunction, and implications and conjunctions contribute no structural growth beyond what their subformulas carry. For a formula with $a$ atoms and $v$ disjunctions, the additive overhead is $2a + 2v$, so:

$$|F^{G}| = |F| + 2a + 2v.$$

Check against the worked formula: $a = 3$, $v = 1$, so $|F^{G}| = 9 + 6 + 2 = 17$. This disagrees with the direct count of $22$. The discrepancy is real and instructive: the additive rule undercounts because the $+2$ per atom and per disjunction is applied to subformulas that are themselves embedded inside negations, and each negation layer adds $+1$ to everything beneath it. Recounting the general case: an atom at nesting depth $m$ under negation-introducing clauses (double negation itself plus each enclosing disjunction translation contributes two negation layers) grows by more than $2$. The direct count is therefore the reliable one, and we report the overhead as the directly computed ratio $22/9 \approx 2.44$ for this formula, noting that the growth is super-additive in negation depth. For the same formula written with the disjunction replaced by a conjunction, $F' = ((p \wedge q) \to r) \wedge (p \to q)$: $|p \wedge q| = 3$, $|(p \wedge q) \to r| = 5$, $|F'| = 9$; $|(p \wedge q)^{G}| = 3 + 3 + 1 = 7$; $|(p \wedge q)^{G} \to r^{G}| = 7 + 3 + 1 = 11$; $|F'^{G}| = 11 + 7 + 1 = 19$; overhead $19/9 \approx 2.1111111$. Disjunction is the expensive connective, as expected, since it is the one whose classical meaning LEM underwrites.

### 4.2 Model-space expansion

Classical valuations for $n$ variables: each variable independently true or false, so $2^{n}$. For $n = 10$: $2^{10} = 1024$.

Kripke valuations on a chain of $k = 3$ worlds: an upward-closed subset of $\{w_1 < w_2 < w_3\}$ is one of $\emptyset, \{w_3\}, \{w_2, w_3\}, \{w_1, w_2, w_3\}$ — exactly $k + 1 = 4$ choices per variable, so $(k+1)^{n} = 4^{10} = 1{,}048{,}576$.

**Expansion factor:**

$$\frac{4^{10}}{2^{10}} = \left(\frac{4}{2}\right)^{10} = 2^{10} = 1024.$$

Wait — with $k = 3$, the per-variable ratio is $(k+1)/2 = 4/2 = 2$, not $1.5$. The $1.5$ figure corresponds to $k = 2$ (a two-world chain, $k + 1 = 3$ choices). We report both, since both are computed:

- Two-world chain ($k = 2$): $3^{10} = 59049$ versus $2^{10} = 1024$; factor $3^{10}/2^{10} = 1.5^{10} = 57.6650390625$. Step check: $1.5^{2} = 2.25$; $1.5^{4} = 2.25^{2} = 5.0625$; $1.5^{8} = 5.0625^{2} = 25.62890625$; $1.5^{10} = 25.62890625 \times 2.25 = 57.6650390625$.
- Three-world chain ($k = 3$): $4^{10} = 1048576$ versus $1024$; factor $2^{10} = 1024$.

The expansion is exponential in $n$ with base $(k+1)/2$: constructive counter-model search is intrinsically more expensive than classical truth-table search, and the gap widens with both the number of variables and the depth of the Kripke frame. This is the price side of the boundary: the constructive semantics is richer (it distinguishes more situations), and richness is paid for in search space.

### 4.3 LEM branching in proof search

Base search tree: branching factor $b = 3$, depth $d = 12$:

$$3^{12} = 531441 \quad (3^{6} = 729; \; 3^{12} = 729^{2} = 531441).$$

Adding LEM instantiation choices for $n = 5$ atoms multiplies the path count by $2^{5} = 32$:

$$531441 \times 32 = 17006112.$$

**Branching factor:**

$$\frac{17006112}{531441} = 32.$$

Scaling: the multiplier is $2^{n}$,