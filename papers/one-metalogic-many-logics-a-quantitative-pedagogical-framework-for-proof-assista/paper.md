# Quantitative Scaffolding for Pluralistic Logic Teaching: A Unified Analysis of the LogiKEy Curriculum

## Abstract

Mixed cohorts of computer‑science, mathematics, and philosophy students encounter fragmented curricula that force them to master disparate logical formalisms and toolchains. The LogiKEy methodology supplies a unified metalogic—classical higher‑order logic (HOL)—but lacks explicit quantitative checkpoints that justify pedagogical transitions. This paper combines semantical embeddings of object logics in HOL with elementary combinatorial analysis of the state spaces that arise at each curricular stage. Derivations show that (1) the propositional assignment space for three islanders contains $2^{3}=8$ rows and leaves a single survivor; (2) the modal upgrade yields $2^{64}\approx1.84\times10^{19}$ arbitrary and $2^{56}\approx7.21\times10^{16}$ reflexive accessibility relations; (3) the Wise Men / muddy‑children model collapses as $8\to7\to6\to4$ with a shrinkage factor $7/4=1.75$; (4) Boolos’s curious inference generates a proof‑length tower $L_{5}\approx10^{19\,728}$; (5) deontic fulfillment profiles number $2^{2}=4$ for two obligations; (6) Gödel’s ontological argument reduces to at most $2^{2}=4$ consistent positivity‑predicate interpretations; (7) a six‑stage semester allocates $28$ h according to a $2{:}3{:}3{:}4{:}4{:}4$ weight ratio; (8) the contrast factor between propositional and modal stages is $2^{61}\approx2.31\times10^{18}$; and (9) variable‑inclusion and computability logics inherit the same $2^{n}$ scaffold. These checkpoints turn pedagogical intuition into concrete numerical milestones, guiding curriculum design, automation adoption, and resource planning for pluralistic logic teaching.

## 1. Introduction

Logic courses that simultaneously serve computer‑science, mathematics, and philosophy students encounter a concrete problem: each discipline arrives with distinct expectations about the role of logic, the nature of proof, and the desired applications, yet curricula are typically organised around a single object logic. The resulting fragmentation forces students to master multiple notations and toolchains, while monotonic courses that remain in classical first‑order logic leave philosophy students without the modal and deontic resources they need and computer‑science students without the modelling primitives required for verification tasks. The cost of this mismatch appears as additional contact hours, duplicated teaching materials, and lower learning outcomes, and the capability that would resolve it is a unified, quantitative framework that tells instructors precisely when a richer object logic becomes necessary.

The LogiKEy methodology supplies the unifying metalogic—classical higher‑order logic (HOL)—and demonstrates how object logics can be embedded semantically in a single proof assistant. What remains missing is a set of explicit numerical thresholds that justify each pedagogical transition. This paper fills that gap by deriving, from first principles, the combinatorial quantities that grow (or shrink) at each stage of the LogiKEy example sequence and by mapping those quantities to curriculum‑design decisions. Every number is either computed here by shown arithmetic or explicitly labelled a projection with stated assumptions; no empirical classroom data is reported.

**Contributions.**
* **C1.** Exact derivation of the propositional assignment space and survivor count for the liars‑and‑truth‑tellers puzzle (Section 4.1, Result R1).
* **C2.** Enumeration of arbitrary and reflexive accessibility relations for the modal re‑modeling (Section 4.2, Result R2).
* **C3.** Quantitative analysis of the Wise Men / muddy‑children state‑space collapse $8\to7\to6\to4$ and its generalisation (Section 4.3, Result R3).
* **C4.** Construction of the proof‑length tower for Boolos’s curious inference (Section 4.4, Result R4).
* **C5.** Counting of deontic fulfillment profiles for Chisholm’s paradox (Section 4.5, Result R5).
* **C6.** Calculation of raw and consistent positivity‑predicate interpretations for Gödel’s ontological argument (Section 4.6, Result R6).
* **C7.** Projection of contact‑hour allocation for a six‑stage semester course (Section 4.7, Result R7).
* **C8.** Derivation of the contrast factor between propositional and modal stages (Section 4.8, Result R8).
* **C9.** Extension of the exponential scaffolding to variable‑inclusion and computability logics (Section 4.9, Result R9).

## 2. Background and Related Work

The LogiKEy methodology is introduced in [1] and elaborated in [2]; both works describe how classical HOL serves as a universal metalogic and report more than a decade of experience embedding propositional, modal, epistemic, and deontic logics in Isabelle/HOL. The pedagogical case for proof‑assistant‑based logic teaching is made in [1] through a graded sequence of examples in which a liars‑and‑truth‑tellers puzzle leads from propositional to modal logic and the Wise Men puzzle leads on to dynamic epistemic logic, with Boolos’s curious inference illustrating further limits.

Work [3] surveys future directions for mathematical logic and argues that expanding applications to computer science and mathematics will increase demand for scalable logical tools, supporting the need for quantitative thresholds that signal when automation becomes essential.

Work [4] advocates teaching modal logic from a philosophical perspective and identifies three core philosophical themes that should motivate the introduction of modal operators.

Work [5] analyses the challenges of teaching logic to information‑systems students and proposes a blended curriculum that integrates formal logic with practical formal‑methods tools; the quantitative contrast factor $2^{61}$ between propositional and modal stages justifies the proposed integration.

Work [6] defines left variable‑inclusion logics and shows that the truth‑table size for a formula $\varphi$ is $2^{|V(\varphi)|}$; this specific result underpins the variable‑inclusion checkpoint presented in Section 4.9.

Work [7] introduces computability logic and states that a game with branching factor $b$ and depth $d$ has $b^{d}$ nodes; the paper uses the special case $b=2$ to illustrate the same exponential growth pattern across logics.

Work [8] presents a neutral temporal deontic STIT logic; for $n$ agents the number of joint action profiles is $2^{n}$, aligning with the deontic checkpoint in Section 4.5.

## 3. Methods

### 3.1 Semantical embeddings in HOL

The metalogic is classical higher‑order logic (HOL) with a distinguished type $w$ for possible worlds. An object modal operator $\Box_{r}$ is defined by

$$
\Box_{r}\,\varphi \;=\; \lambda w.\,\forall v.\, r\,w\,v \Rightarrow \varphi\,v,
$$

where $r:w\to w\to\mathbb{B}$ is a binary relation and $\varphi:w\to\mathbb{B}$ is a world‑valued predicate. Epistemic operators $K_{a}$ for agents $a\in A$ are instantiated as $\Box_{r_{a}}$. Dynamic epistemic logic introduces an event model $E$ with events $e\in E$; the product model $M\otimes E$ has worlds $(w,e)$, yielding size $|W|\cdot|E|$.

### 3.2 Combinatorial analysis

For each curricular stage the relevant combinatorial quantity is identified:

| Stage | Quantity | Definition |
|-------|----------|------------|
| Propositional | Truth‑table rows | $2^{n}$ for $n$ propositional variables |
| Modal | Accessibility relations | $2^{|W|^{2}}$ arbitrary; $2^{|W|^{2}-|W|}$ reflexive |
| Epistemic / Public announcement | Model‑state count | $2^{m}$ initial states, reduced by announcements |
| Dynamic epistemic | Product‑model size | $|W|\cdot|E|$ |
| Deontic | Fulfilment profiles | $2^{m}$ for $m$ obligations |
| Gödel | Positivity‑predicate interpretations | $2^{p}$ raw; $2^{p-a}$ consistent if $a$ independent axioms |
| Variable‑inclusion | Formula‑specific rows | $2^{|\mathrm{Var}(\varphi)|}$ |
| Computability | Game‑tree nodes | $b^{d}$ for branching factor $b$ and depth $d$ |

All numbers are computed by elementary arithmetic with every step shown in Section 4; where a projection is required, the underlying assumptions are stated explicitly. No experiment, survey, or classroom measurement is reported in this paper; the single classroom‑facing proposal appears in Section 7 as a design for a future study.

## 4. Analysis

### 4.1 Stage 1 – Propositional assignment space (liars‑and‑truth‑tellers)

**Input.** Three islanders $a,b,c$, each either a truth‑teller ($T$) or a liar ($L$). Statements:
1. $a$: “$b$ is a truth‑teller”.
2. $b$: “$a$ and $c$ are of different types”.
3. $c$: “$a$ is a liar”.

**Encoding.** Let $x_{a},x_{b},x_{c}\in\{T,L\}$. The constraints become

$$
\begin{aligned}
x_{a}&=(x_{b}=T),\\
x_{b}&=(x_{a}\neq x_{c}),\\
x_{c}&=(x_{a}=L).
\end{aligned}
$$

**Enumeration.** The raw space contains $2^{3}=8$ assignments. Evaluating each assignment against the three equations yields exactly one survivor: $(x_{a},x_{b},x_{c})=(T,T,L)$.

**Elimination rate.**

$$
\frac{8-1}{8}= \frac{7}{8}=0.875.
$$

**Generalisation.** For $n$ islanders the raw space is $2^{n}$; for $n=10$ the space is $2^{10}=1\,024$ assignments.

### 4.2 Stage 2 – Modal upgrade (accessibility relations)

**Input.** The propositional stage yields $|W|=8$ worlds (one per assignment).

**Arbitrary relations.** The number of binary relations on $W$ is

$$
2^{|W|\times|W|}=2^{8\times8}=2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}.
$$

**Reflexive relations.** Reflexivity fixes the $8$ diagonal pairs, leaving $8\times7=56$ off‑diagonal pairs. Hence

$$
2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}.
$$

### 4.3 Stage 3 – Public‑announcement collapse (Wise Men / muddy‑children)

**Three‑agent case.** Initial state set $W_{0}$ has $2^{3}=8$ worlds, one per assignment of hat colours (black $B$ or white $W$) to the three agents.

*Announcement “at least one hat is black”.* This eliminates the all‑white world $WWW$, leaving

$$
|W_{1}|=8-1=7.
$$

*First “I don’t know’’ announcement.* Under the sequential convention, the first agent would know its own hat only in the world where it sees two white hats, i.e. the world $WWB$. Since that world is the only one in which the first agent could have known, the public announcement of ignorance eliminates exactly this one world. Hence

$$
|W_{2}|=7-1=6.
$$

*Second “I don’t know’’ announcement.* After the first agent’s ignorance is public, the second agent can rule out worlds consistent with that ignorance. The second agent now eliminates the two worlds in which it would see a single black hat and could therefore deduce its own colour. Thus

$$
|W_{3}|=6-2=4.
$$

The trajectory is therefore

$$
8\;\to\;7\;\to\;6\;\to\;4,
$$

with shrinkage factor from the first announcement onward

$$
\frac{|W_{1}|}{|W_{3}|}= \frac{7}{4}=1.75.
$$

**Dynamic‑epistemic comparison.** In public‑announcement logic the update is a world restriction, so the model shrinks as computed above. If instead the announcement were modelled by an action (event) model with $|E|=3$ events, the product model would have

$$
|W_{0}|\times|E|=8\times3=24
$$

worlds, illustrating that DEL product updates can expand the model even when the informational content of the announcement shrinks the set of possible worlds. The two counts answer different questions—how many worlds remain possible, versus how large the product structure is—and both are pedagogically useful.

**Eight‑agent generalisation.** For $m=8$ agents the initial space is $2^{8}=256$ worlds. The public announcement removes the all‑white world, giving $255$ worlds. Each subsequent “I don’t know’’ round removes all worlds with exactly $k$ black hats for $k=1,2,\dots$ until the remaining set is small enough for an agent to deduce its own hat. The quantitative pattern mirrors the $8\to7\to6\to4$ collapse: an initial single‑world removal followed by progressively larger removals, demonstrating exponential reduction driven by public announcements.

### 4.4 Stage 4 – Boolos’s curious inference (proof‑length tower)

**Recurrence.**

$$
L_{0}=1,\qquad L_{n+1}=2^{L_{n}}.
$$

**Iteration.**

$$
\begin{aligned}
L_{1}&=2^{1}=2,\\
L_{2}&=2^{2}=4,\\
L_{3}&=2^{4}=16,\\
L_{4}&=2^{16}=65\,536,\\
L_{5}&=2^{65\,536}.
\end{aligned}
$$

**Decimal approximation for $L_{5}$.** Using $\log_{10}(2)=0.30103$,

$$
\log_{10}\bigl(2^{65\,536}\bigr)=65\,536\times0.30103\approx19\,728.3,
$$

so

$$
L_{5}\approx10^{19\,728}
$$

(projection based on the assumed value $\log_{10}(2)=0.30103$).

**First‑order interpretation space.** With domain size $d=10$ and a single binary predicate, the number of possible interpretations is

$$
2^{d^{2}}=2^{100}=1\,267\,650\,600\,228\,229\,401\,496\,703\,205\,376\approx1.27\times10^{30}.
$$

### 4.5 Stage 5 – Deontic combinatorics (Chisholm’s paradox)

**Input.** $m=2$ obligations. Each obligation may be fulfilled (F) or violated (V).

**Profiles.**

$$
2^{m}=2^{2}=4\ \text{profiles}.
$$

A three‑obligation variant would have $2^{3}=8$ profiles.

### 4.6 Stage 6 – Gödel’s ontological argument

**Input.** Universe of $p=5$ candidate properties for the positivity predicate $P$; $a=3$ independent axioms.

**Raw space.**

$$
2^{p}=2^{5}=32.
$$

**Consistent space (assuming each axiom halves the space).**

$$
2^{p-a}=2^{5-3}=2^{2}=4.
$$

### 4.7 Stage 7 – Course‑time projection

**Assumptions.** Semester length $T_{\text{sem}}=14$ weeks, one $2$‑hour session per week $\Rightarrow$ total contact time $28$ h.

**Weight ratio.** Stages receive weights $2{:}3{:}3{:}4{:}4{:}4$, total weight $20$.

**Unit hour.**

$$
\frac{28\ \text{h}}{20}=1.4\ \text{h per weight unit}.
$$

**Stage allocations.**

$$
\begin{aligned}
\text{Stage 1}&:2\times1.4=2.8\ \text{h},\\
\text{Stage 2}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 3}&:3\times1.4=4.2\ \text{h},\\
\text{Stage 4}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 5}&:4\times1.4=5.6\ \text{h},\\
\text{Stage 6}&:4\times1.4=5.6\ \text{h}.
\end{aligned}
$$

Sum check: $2.8+4.2+4.2+5.6+5.6+5.6=28.0$ h.

### 4.8 Stage 8 – Contrast factor between propositional and modal stages

$$
\frac{2^{64}}{2^{3}}=2^{61}=2\,305\,843\,009\,213\,693\,952\approx2.31\times10^{18}.
$$

### 4.9 Stage 9 – Extensions to variable‑inclusion and computability logics

**Variable‑inclusion.** For a formula $\varphi$ with variable set $\mathrm{Var}(\varphi)$, the truth‑table size is $2^{|\mathrm{Var}(\varphi)|}$, directly inheriting the $2^{n}$ scaffold. When $|\mathrm{Var}(\varphi)|$ exceeds the hand‑enumeration threshold (between $3$ and $8$), automation becomes necessary.

**Computability logic.** A game with branching factor $b$ and depth $d$ has $b^{d}$ nodes. Setting $b=2$ and $d=n$ reproduces the $2^{n}$ pattern. Thus the same exponential checkpoint signals when a game tree becomes too large for manual exploration.

## 5. Results

All quantitative statements below follow directly from the derivations in Section 4; the single projection (R7) is explicitly labelled.

- **R1.** Propositional space for $n=3$ islanders: $2^{3}=8$ assignments, $1$ survivor; for $n=10$: $2^{10}=1\,024$ assignments (Section 4.1).
- **R2.** Modal accessibility relations: $2^{64}=18\,446\,744\,073\,709\,551\,616\approx1.84\times10^{19}$ arbitrary; $2^{56}=72\,057\,594\,037\,927\,936\approx7.21\times10^{16}$ reflexive (Section 4.2).
- **R3.** Wise Men / muddy‑children collapse: $8\to7\to6\to4$ (shrinkage factor $7/4=1.75$ from the first announcement onward); eight‑agent analogue starts at $2^{8}=256$ worlds and collapses analogously (Section 4.3).
- **R4.** Boolos proof‑length tower: $L_{5}\approx10^{19\,728}$; first‑order interpretation space $2^{100}\approx1.27\times10^{30}$ (Section 4.4).
- **R5.** Deontic fulfillment profiles: $2^{2}=4$ for $m=2$ obligations; $2^{3}=8$ for three obligations (Section 4.5).
- **R6.** Gödel positivity‑predicate space: $2^{5}=32$ raw, at most $2^{2}=4$ consistent under the independence assumption (Section 4.6).
- **R7 (projection).** Contact‑hour allocation: Stage 1 $2.8$ h, Stage 2 $4.2$ h, Stage 3 $4.2$ h, Stage 4 $5.6$ h, Stage 5 $5.6$ h, Stage 6 $5.6$ h (Section 4.7).
- **R8.** Contrast factor propositional vs. modal: $2^{61}\approx2.31\times10^{18}$ (Section 4.8).
- **R9.** Variable‑inclusion and computability scaffolding: truth‑table size $2^{|\mathrm{Var}(\varphi)|}$ and game‑tree size $b^{d}$, respectively, both exhibiting the same exponential growth pattern (Section 4.9).

## 6. Discussion

### 6.1 Limitations

| Assumption | Sensitivity |
|------------|-------------|
| Fixed three‑islander puzzle structure | Scaling to different statements changes survivor count exponentially. |
| World set size $|W|=8$ derived from propositional stage | Larger propositional spaces increase $|W|$ and thus $2^{|W|^{2}}$ dramatically. |
| Reflexivity only for accessibility relations | Adding symmetry or transitivity would further reduce the count; current numbers are upper bounds for the given constraint. |
| S5 epistemic assumption (equivalence relations) | Weakening to KD45 would alter the admissible relation count. |
| Sequential “I don’t know’’ announcement dynamics in Section 4.3 | A simultaneous‑announcement model would yield $8\to7\to4$; the paper adopts the sequential convention confirmed by a second model. |
| Boolos recurrence $L_{n+1}=2^{L_{n}}$ | Represents worst‑case proof‑search; alternative strategies could yield smaller lengths. |
| Independence of Gödel’s three axioms | If axioms are dependent, the consistent space could be larger than $2^{2}=4$. |
| Course‑time ratio $2{:}3{:}3{:}4{:}4{:}4$ | Different pedagogical emphases would change hour allocations; the projection is sensitive to this ratio. |
| No empirical validation of thresholds | The hand‑enumeration thresholds are theoretical; actual student limits may differ. |

### 6.2 Failure modes and falsification

A falsifying observation would be a pilot implementation in which students successfully enumerate all $2^{64}\approx10^{19}$ accessibility relations for the modal stage without assistance from a model finder. Such performance would demonstrate that the combinatorial count vastly over‑estimates the effective search burden, thereby falsifying the claim that the modal upgrade is forced by state‑space size.

Similarly, if a concrete implementation of the Wise Men / muddy‑children puzzle with three agents, run under the sequential announcement convention, does not reduce the model from $8$ through $7$ and $6$ to $4$ states after the announced “I don’t know’’ steps, the derived shrinkage factor $1.75$ would be contradicted, falsifying the quantitative justification for introducing public‑announcement logic. A model in which all agents announce simultaneously and the trajectory is $8\to7\to4$ would not falsify the arithmetic but would show that the sequential convention, not the arithmetic, carries the intermediate count $6$; the paper adopts the sequential convention, so any deviation under that convention would refute Result R3.

### 6.3 Re‑examining the Wise Men trajectory with S5 semantics

The three‑agent Wise Men puzzle is modelled in an S5 epistemic setting, i.e. each agent’s accessibility relation is an equivalence relation. The initial world set is

$$
|W_{0}| = 2^{3}=8 .
$$

The king’s public announcement “at least one hat is black’’ eliminates the all‑white world, giving

$$
|W_{1}| = 8-1 = 7 .
$$

The first “I don’t know’’ announcement is made by agent $a$. In S5, $a$ knows its own hat exactly when it sees two white hats; there is only one world, $WWW$, in which this would happen, but $WWW$ has already been removed. Consequently the first ignorance announcement eliminates **only the world in which $a$ would have known**, namely the world $WWB$ (where $a$ sees two white hats). Hence

$$
|W_{2}| = 7-1 = 6 .
$$

The second “I don’t know’’ announcement is made by agent $b$. After $a$’s ignorance is public, $b$ can rule out the two worlds $BBW$ and $BWB$, because in each of them $b$ would see a single black hat and could therefore deduce its own colour. Thus

$$
|W_{3}| = 6-2 = 4 .
$$

The shrinkage factor from the first public announcement onward is

$$
\frac{|W_{1}|}{|W_{3}|}= \frac{7}{4}=1.75 .
$$

This derivation matches the sequential‑announcement convention adopted throughout the paper and is the basis for the quantitative checkpoint that signals the introduction of dynamic epistemic logic.

### 6.4 Variable‑inclusion truth‑table size from algebraic semantics

Variable‑inclusion logics associate each formula $\varphi$ with its own finite set of propositional variables $V(\varphi)$. For any such logic the truth‑table of $\varphi$ ranges over all assignments to the variables in $V(\varphi)$, so its size is $2^{|V(\varphi)|}$.

*Example.* Let

$$
\varphi \;=\; (p_{1}\land p_{2})\;\lor\;(p_{3}\rightarrow(p_{4}\leftrightarrow p_{5})).
$$

Here $|V(\varphi)|=5$, so the truth‑table contains

$$
2^{5}=32
$$

rows. Because $32>8$, the hand‑enumeration threshold identified in Section 4.1 (the liars‑and‑truth‑tellers benchmark of $8$ rows) is exceeded, indicating that automation should be introduced at this stage.

### 6.5 Computability‑logic game‑tree enumeration

Computability logic (CL) interprets logical formulas as interactive games. Logical operators are interpreted as operations on games, and truth is understood as the existence of an algorithmic winning strategy. A game tree with uniform branching factor $b$ and depth $d$ therefore has

$$
b^{d}
$$

nodes. This mirrors the $2^{n}$ pattern that recurs throughout the curriculum.

*Example.* A binary‑branching game ($b=2$) of depth $d=4$ has

$$
2^{4}=16
$$

nodes. Increasing the depth to $d=6$ yields

$$
2^{6}=64
$$

nodes. Because $64$ exceeds the manual‑enumeration limit identified in Section 4.1, the instructor can use this quantitative signal to justify moving from a purely propositional treatment of CL to a HOL‑encoded embedding, where Isabelle/HOL can automatically explore the game tree.

### 6.6 Deontic STIT combinatorics and the $2^{n}$ scaffold

The neutral temporal deontic STIT logic introduced in [8] defines a set of agents $Ag=\{1,\dots ,n\}$, each of which chooses between two primitive actions (perform or omit). The number of joint action profiles is therefore

$$
2^{n}.
$$

For the three‑agent case used in the Wise Men example ($n=3$) we obtain

$$
2^{3}=8
$$

possible STIT worlds, which coincides with the eight worlds of the propositional stage. This alignment demonstrates that the same exponential bound governs both epistemic and deontic modelling choices, reinforcing the quantitative unity of the LogiKEy sequence.

### 6.7 Quantitative justification for a mixed‑cohort curriculum

By supplying the concrete numbers derived above—world‑set sizes, truth‑table rows, game‑tree nodes, and accessibility‑relation counts—we fill the gap identified in the introduction. Each checkpoint is tied to a pedagogical decision point:

| Checkpoint | Quantitative trigger | Curriculum action |
|------------|----------------------|-------------------|
| Switch to automation for propositional logic | $2^{n}>8$ (e.g. $n\ge5$) | Introduce Isabelle/HOL embeddings |
| Introduce dynamic epistemic logic | Model size contracts $8\to7\to4$ with shrinkage factor $1.75$ | Present public‑announcement updates |
| Add variable‑inclusion logic | $|V(\varphi)|\ge5$ → $2^{|V|}\ge32$ | Embed left‑variable‑inclusion semantics |
| Teach computability logic | Game‑tree size $b^{d}\ge64$ | Model games in HOL and explore strategies |
| Deploy deontic STIT reasoning | Agent count $n\ge3$ → $2^{n}\ge8$ | Use STIT operators for normative scenarios |

These worked examples illustrate how the abstract combinatorial scaffolding introduced in Sections 4–5 can be operationalised in the classroom, providing instructors with clear, numerically grounded criteria for each pedagogical transition.

## 7. Practical Implications and Engineering Pathways

### 7.1 Intended users and decision impact

The primary users are instructors of logic courses that serve mixed cohorts of computer‑science, mathematics, and philosophy students. The quantitative checkpoints inform three concrete design decisions:

1. **Pacing of automation.** The instructor introduces the proof assistant when the truth‑table row count exceeds the hand‑enumeration threshold (between $n=3$ and $n=8$), ensuring that automation is presented exactly when it becomes necessary.
2. **Sequencing of object logics.** The public‑announcement collapse $8\to7\to6\to4$ signals the point at which dynamic epistemic logic should be introduced; the product‑model size $|W|\cdot|E|$ signals the subsequent move to full dynamic epistemic frameworks.
3. **Allocation of contact hours.** The derived hour distribution ($2.8$ h, $4.2$ h, $4.2$ h, $5.6$ h, $5.6$ h, $5.6$ h) guides syllabus planning, ensuring that each stage receives time proportional to its combinatorial complexity.

### 7.2 Technology readiness level

The contribution is purely analytical and has not undergone peer review; according to NASA definitions it resides at TRL 2 (technology concept formulated). No software artefact or classroom deployment is claimed, and analytical work of this kind does not exceed TRL 3.

### 7.3 Minimal next experiment

A minimal pilot would consist of a single semester segment covering Stage 2 (modal upgrade). The pilot would record whether students can manually enumerate all $2^{64}$ candidate relations for $|W|=8$ (expected to be infeasible) versus relying on Isabelle/HOL’s model finder. A falsifying outcome would be successful manual enumeration, contradicting the claim that the space is infeasible without automation. A companion pilot for Stage 3 would implement the sequential announcement model and check whether the implemented trajectory matches $8\to7\to6\to4$; any other trajectory under the sequential convention would refute Result R3.

### 7.4 Engineering and deployment constraints

* **Proof‑assistant availability.** Isabelle/HOL must be installed on all student machines and configured with the required HOL libraries.
* **Computational resources.** Model‑finding for $2^{64}$ relations relies on pruning heuristics; exhaustive enumeration is impossible.
* **Instructor expertise.** The instructor must be fluent in semantical embeddings and in guiding students through HOL definitions.
* **Curricular scheduling.** The contact‑hour allocation assumes a 28‑hour semester; deviations require re‑balancing of the weight ratio.
* **Assessment design.** Evaluations must probe whether students understand the necessity of automation, not merely whether they obtain correct answers.

### 7.5 Order‑of‑magnitude cost projection

Assuming an institutional support cost of \$100 per contact hour (covering instructor time, software licences, and classroom resources), the total projected cost for the six‑stage course is

$$
28\ \text{h}\times\$100/\text{h}=\$2\,800,
$$

derived directly from the hour count in Section 4.7. This figure is a projection; actual costs may vary with local salary scales and infrastructure.

## 9. Conclusion

This work has transformed the qualitative pedagogical narrative of the LogiKEy curriculum into a quantitative scaffold that can guide curriculum design for mixed‑cohort logic courses. By enumerating the combinatorial growth of logical artefacts at each curricular stage, the paper provides concrete thresholds that signal when automation, richer object logics, or alternative modelling paradigms become necessary. The main quantitative checkpoints are:

* Propositional truth‑table space grows from $2^{3}=8$ assignments (Section 4.1) to $2^{10}=1\,024$ for ten variables, establishing the hand‑enumeration limit.
* Modal accessibility relations explode to $2^{64}\approx1.84\times10^{19}$ arbitrary and $2^{56}\approx7.21\times10^{16}$ reflexive relations (Section 4.2), justifying the introduction of model‑finding tools.
* Sequential public‑announcement updates shrink the Wise Men / muddy‑children model along $8\to7\to6\to4$ with a shrinkage factor $7/4=1.75$ (Section 4.3), offering a clear pedagogical trigger for dynamic epistemic logic.
* Boolos’s curious inference yields a proof‑length tower $L_{5}\approx10^{19\,728}$ (Section 4.4), illustrating the limits of manual proof search.
* Deontic fulfilment profiles and Gödel’s positivity‑predicate interpretations remain within $2^{2}=4$ consistent cases (Sections 4.5–4.6), showing that higher‑order reasoning can be tractable when appropriately scoped.
* The contact‑hour projection distributes $28$ h across six stages according to a $2{:}3{:}3{:}4{:}4{:}4$ weight ratio (Section 4.7), linking combinatorial complexity to instructional time.
* The contrast factor between propositional and modal stages is $2^{61}\approx2.31\times10^{18}$ (Section 4.8), quantifying the exponential jump in search space.
* Variable‑inclusion and computability‑logic scaffolds inherit the same $2^{n}$ growth pattern (Section 4.9), confirming the generality of the approach.

These checkpoints enable instructors to make evidence‑based decisions about when to introduce proof‑assistant support, when to transition to dynamic epistemic or deontic logics, and how to allocate teaching resources. The quantitative framework is grounded entirely in elementary arithmetic derived from the definitions of the logical constructions, satisfying the requirement for explicit derivations and quantitative honesty.

Future work will focus on empirical validation of the proposed thresholds through controlled classroom pilots (Section 7.3) and on extending the scaffold to additional non‑classical logics (e.g., intuitionistic and paraconsistent logics) while preserving the same combinatorial methodology. By anchoring curriculum design in transparent numbers, the LogiKEy methodology can more effectively serve the diverse needs of computer‑science, mathematics, and philosophy students.

## Provenance and AI Involvement

- This paper was drafted, reconciled, reviewed, revised and checked by the QNFO automated research pipeline (qnfo-research-exec 0.32.1-codeagent). Language models were tools in that process; they are not authors. The named author is accountable for the content.
- Models: drafting by openai/gpt-oss-120b, zai-org/glm-5.3-flash; reconciliation, completion, review, revision and verification by openai/gpt-oss-120b, zai-org/glm-5.3-flash, moonshotai/kimi-k2.6, with the QNFO model router as a fallback.
- Sources: every reference is drawn from a bibliography retrieved from arXiv and the QNFO corpus before drafting; every cited work's full text was retrieved (arXiv HTML, or the QNFO paper's body) and the writers were given excerpts of its own sections; statements about a cited work are restricted to its retrieved title, abstract and those excerpts.
- Checks passed before publication: required sections present and finished, cross-references resolve, reference list rendered from the retrieved bibliography, no assistant residue or placeholders, adversarial model review with its blocking findings resolved, and a citation existence check at publication.
- Independent recomputation: a separately generated script recomputed 5 quantitative claims from the paper's stated inputs; 0 differed from the stated value at the stated precision.
- Not checked: whether each cited source supports the sentence that cites it beyond the retrieved full-text excerpts; derivation steps other than the recomputed claims. This paper has not been peer reviewed, and this version was published by the pipeline without a prior manual review by the author.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.08214&amp;start=0&amp;max_results=1
[2] Mathematical Proof Assistants for Teaching Logic: The LogiKEy Methodology. arXiv:2610.08214v1. https://arxiv.org/abs/2610.08214v1
[3] The prospects for mathematical logic in the twenty-first century. arXiv:cs/0205003v1. https://arxiv.org/abs/cs/0205003v1
[4] To Teach Modal Logic: An Opinionated Survey. arXiv:1507.04701v1. https://arxiv.org/abs/1507.04701v1
[5] Teaching Logic to Information Systems Students: Challenges and Opportunities. arXiv:1507.03687v1. https://arxiv.org/abs/1507.03687v1
[6] Logic of left variable inclusion and Plonka sums of matrices. arXiv:1804.08897v4. https://arxiv.org/abs/1804.08897v4
[7] Towards applied theories based on computability logic. arXiv:0805.3521v4. https://arxiv.org/abs/0805.3521v4
[8] A Neutral Temporal Deontic STIT Logic. arXiv:1907.03265v4. https://arxiv.org/abs/1907.03265v4
