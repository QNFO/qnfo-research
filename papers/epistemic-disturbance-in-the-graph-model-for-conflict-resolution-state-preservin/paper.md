# Epistemic Disturbance in the Graph Model for Conflict Resolution: State-Preserving Actions, Four-Valued Assessments, and the Distinction between Capability and Intention

## Abstract

In the graph model for conflict resolution (GMCR), a decision maker (DM) either moves the conflict to another state or does nothing, and every action that leaves the state unchanged is silently classified as inaction. Yet announcements, exercises of rights, leaks, and selective disclosures leave the physical state unchanged while changing what other DMs believe about which moves are available (capability) and which moves others would want to make (intention). We formalize such state-preserving actions by augmenting each state with the DMs' epistemic states: a physical move changes the physical state, a state-preserving action changes only the epistemic state, and inaction is the absence of any transition. Actions generate evidence through observer-specific interpretation maps evaluated in a four-valued logic separating evidence for and against each move. We prove three structural results: evidence for a move can only enable perceived moves and evidence against can only disable them; two of the four canonical reduction operators discard one kind of evidence entirely; and contradictory assessments are absorbing under monotone accumulation, with $37/64 = 0.578125$ of a three-move observer's epistemic space absorbing. A fully computed four-state model in the style of the 1995 DVD format negotiation shows general metarationality collapsing all four states into one stability class while sequential stability separates them, and a single state-preserving action expanding the sequentially stable set from $3$ to $4$ states.

## 1. Introduction

The graph model for conflict resolution (GMCR) represents a conflict as a directed graph whose vertices are states and whose colored, directed arcs are the moves available to each decision maker (DM) [1], [2]. In the basic definitions, a DM's action set at a state consists of the arcs leaving that state in the DM's color, together with the implicit option of doing nothing. This convention is elegant but hides an assumption: that every action which leaves the state unchanged *is* doing nothing.

The assumption fails for a large and strategically important class of actions. When a firm announces that it will support a format, when a patent holder exercises a licensing right, when a document is leaked, or when a party selectively discloses part of its position, the physical state of the conflict does not change. But no reasonable analyst would call these inaction: they change what other DMs believe about which moves are available (capability) and which moves others would want to make (intention). We call these **state-preserving actions**, or **epistemic disturbances**: transitions that leave the physical state fixed and alter only the epistemic state.

Modeling such actions requires three distinctions that standard GMCR does not draw. First, the distinction between a physical move, a state-preserving action, and genuine inaction. Second, the distinction between evidence for a claim and evidence against it, carried over from the four-valued Quasi-Closed World Graph Model (QCW-GMCR) [3] and from four-valued state definitions for conflict analysis [6]. Third, the distinction between an observer's assessment of what another DM *can* do and what that DM *would want* to do; we show these two assessment types propagate differently through the stability definitions.

The paper's contributions are:

1. A formal augmentation of GMCR states with epistemic components, in which state-preserving actions are first-class transitions and inaction is the absence of a transition (Section 3).
2. Structural results on evidence flow: polarity confinement (evidence for only enables, evidence against only disables), the evidence-blindness of two of the four canonical reduction operators, and the absorbing character of contradiction under monotone accumulation, with an explicit count of the absorbing fraction of the epistemic state space (Section 4).
3. A capability/intention separation: capability assessments affect all sanction-based stability concepts (general metarationality, symmetric metarationality, sequential stability) and, on the assessing DM's own side, Nash stability; intention assessments affect only sequential stability (Sections 4 and 5).
4. A fully computed four-state model in the style of the 1995 DVD format negotiation, in which general metarationality cannot distinguish the negotiation's phases because the computer industry group could always sanction, while sequential stability, which asks whether it *would*, can; and in which a single state-preserving action expands the sequentially stable set from $3$ to $4$ states (Sections 4 and 5).

## 2. Background and Related Work

**The graph model and its epistemic gap.** The point of departure for this paper is the recent observation [1], [2] that the basic GMCR definitions leave inaction implicit, so that every action leaving the state unchanged is treated as doing nothing. That work proposes augmenting states with the DMs' epistemic states so that a physical move changes the physical state, a state-preserving action changes only the epistemic state, and inaction is the absence of a transition, with actions generating evidence through observer-specific interpretation maps. It further establishes the two polarity properties we reuse here: evidence for a move can only enable perceived moves, and evidence against can only disable them. We adopt this framework and supply what it does not: explicit derivations of its counting consequences, its reduction-operator taxonomy, and its stability-monotonicity results on a fully worked model.

**Four-valued extensions.** The QCW-GMCR [3] extends GMCR with Belnap's four-valued logic, in which each proposition carries independent evidence for and against, yielding the values true ($T$), false ($F$), both ($B$, contradiction), and neither ($N$, ignorance). That work pairs the framework with a machine-checked Lean 4 formalization, verifying compositional propagation of four-valued option assignments and establishing that the core definitions are internally consistent. Our epistemic states and reduction operators are the move-level analogue of its option-level machinery, and the Lean formalization suggests the present extension is similarly mechanizable. The state-definition problem for four-valued conflict analysis is treated in [6], which argues that describing a state purely as the outcome of a strategy combination is insufficient for a functioning decision framework when DMs hold uncertain or partial descriptions; our augmentation of physical states with epistemic assessments is a direct answer to that critique at the level of moves rather than options.

**Adjacent formal literatures.** Several works in the source corpus are methodologically adjacent rather than substantively overlapping, and we cite them to delimit scope. The study of continuous quantum semigroup actions on finite quantum spaces [4] shows that such actions preserving a faithful state factor through the quantum Bohr compactification; the structural lesson we borrow is that a family of state-preserving transformations can be analyzed through the invariant structure it preserves — here, the physical state is the invariant and the epistemic state is what the semigroup of announcements and disclosures acts upon. No technical result transfers. The G-CSEA algorithm [5] extracts conflict sets causing infeasibility in pseudo-Boolean workforce-scheduling models via constraint-interaction graphs; its discipline of isolating minimal conflicting subsets parallels our reduction operators, which isolate which evidence items actually bear on a perceived move, and suggests a future integration in which epistemic rather than physical infeasibility sources are diagnosed. The generalized Turán paper [7] develops counting tools $\mathrm{ex}(n, T, F)$ for clique counts in $F$-free graphs; we use counting of the same flavor, though at elementary scale, when we enumerate epistemic profiles as a product over perceived moves. The 3D graph drawing paper [8] proves bend and angle bounds for low-degree graphs; it is a reminder that representation choices for graph models — here, augmenting vertices with epistemic labels rather than thickening edges — carry provable consequences for what is readable.

**Scope note on the corpus.** The available bibliography for this preprint contains thirteen works, [1]–[13]. Of these, [1]–[8] are substantively or methodologically discussed above; entries [9]–[13] (adjacent motivational literatures on epistemic repair, agent failure modes, cognitive linearity, and mechanistic ethics) are not cited in this paper because their content does not bear directly on the formal results, and this is a stated limitation of the present corpus coverage.

## 3. Methods

### 3.1 Base model

A graph model [1] is a tuple $G = (S, \{A_i\}_{i \in N}, \{\succ_i\}_{i \in N})$ where $S$ is a finite state set, $N$ is the finite DM set, $A_i \subseteq S \times S$ is DM $i$'s move relation, and $\succ_i$ is DM $i$'s strict preference order on $S$. Write $R_i(s) = \{s' \in S : (s, s') \in A_i\}$ for the successors reachable by $i$ from $s$.

### 3.2 Epistemic augmentation

Fix an observer DM $o$. For each opponent $j \neq o$ and each potential move $m$ of $j$, the observer maintains a four-valued assessment

$$a_o(m) \in \{T, F, N, B\},$$

where $T$ means supported, $F$ refuted, $N$ undecided, and $B$ both (contradictory evidence). Each assessment splits into a capability component $a_o^{c}(m)$ (is the move available?) and an intention component $a_o^{w}(m)$ (would $j$ want to make it?). The observer's perceived move set is

$$R_j^{o}(s) = \{m = (s, s') : a_o^{c}(m) \in \{T, B\}\}.$$

A state of the augmented model is a pair $\sigma = (s, \mathbf{a}_o)$ with $s \in S$ and $\mathbf{a}_o$ the profile of assessments. Transitions come in three kinds:

1. **Physical move** by DM $i$: $(s, \mathbf{a}_o) \to (s', \mathbf{a}_o)$ with $(s, s') \in A_i$; the epistemic component is unchanged.
2. **State-preserving action** by DM $i$: $(s, \mathbf{a}_o) \to (s, \mathbf{a}_o')$ with $\mathbf{a}_o' \neq \mathbf{a}_o$; only the epistemic component changes.
3. **Inaction**: no transition in either component.

An **interpretation map** $\iota_o$ assigns to each evidence item $e$ in a global evidence stream the bits it supplies to observer $o$; the same $e$ may supply a $T$-bit to one observer and an $F$-bit to another.

### 3.3 Accumulation and reduction

Assessments update by monotone accumulation: each observer accumulates evidence bits per move, with $T$-bits and $F$-bits counted separately as $(p_m, n_m)$ for move $m$; counts never decrease. A **reduction operator** $\rho$ maps $(p_m, n_m)$ to a four-valued assessment. The four canonical operators are:

$$\rho_1(p_m, n_m) = \begin{cases} T & p_m > 0,\ n_m = 0 \\ F & p_m = 0,\ n_m > 0 \\ B & p_m > 0,\ n_m > 0 \\ N & p_m = 0,\ n_m = 0 \end{cases}$$

(uses both kinds); $\rho_2(p_m, n_m) = T$ if $p_m > 0$ else $N$ (ignores evidence against); $\rho_3(p_m, n_m) = F$ if $n_m > 0$ else $N$ (ignores evidence for); and $\rho_4(p_m, n_m) = N$ always (ignores both). Thus two of the four operators, $\rho_2$ and $\rho_3$, ignore one kind of evidence entirely, and $\rho_4$ ignores both.

A **perceived-verdict operator** maps an assessment to a binary availability verdict; the standard choice is $\rho_{\mathrm{for}}(v) = 1$ iff $v \in \{T, B\}$, so contradiction counts as enabled.

### 3.4 Stability concepts

For DM $o$ at physical state $s$ with perceived move sets $\{R_j^{o}\}$:

- **Nash stability** [1]: $s$ is Nash stable for $o$ if no move $o$ herself can make leads to a state $o$ prefers.
- **General metarationality (GMR)** [1]: $s$ is GMR-stable for $o$ if for every improving move $o$ can make to $s'$, some opponent $j$ has a response from $s'$ to a state $o$ likes less than $s$ (a sanction).
- **Sequential stability (SEQ)** [1]: as GMR, but the sanctioning response must itself be credible — formally, it must terminate in a state that is stable for the opponent. SEQ asks not merely whether a sanction *could* occur but whether it *would*.

## 4. Analysis

### 4.1 Input numbers

| Symbol | Meaning | Value | Source |
|--------|---------|-------|--------|
| $k$ | Number of perceived candidate moves tracked by the observer | $3$ | model definition (Section 4.2) |
| $|\mathcal{V}|$ | Size of the four-valued assessment set | $4$ | definition of $\{T,F,N,B\}$ |
| $|S|$ | States in the worked model | $4$ | model definition (Section 4.3) |
| $\succ_1$ | DM 1's ranking | $s_4 \succ_1 s_1 \succ_1 s_2 \succ_1 s_3$ | definition |
| $\succ_2$ | DM 2's ranking | $s_3 \succ_2 s_2 \succ_2 s_4 \succ_2 s_1$ | definition |
| $A_1$ | DM 1's moves | $\{(s_1,s_2),(s_2,s_1)\}$ | definition |
| $A_2$ | DM 2's moves | $\{(s_1,s_3),(s_3,s_1),(s_2,s_4),(s_4,s_2)\}$ | definition |

### 4.2 Counting epistemic profiles and the absorbing fraction

An observer tracking $k = 3$ perceived candidate moves of a single opponent, each independently in $\{T, F, N, B\}$ under $\rho_1$, has

$$|\{T, F, N, B\}|^{k} = 4^{3} = 64$$

reachable epistemic profiles. Contradiction-free profiles restrict each coordinate to $\{T, F, N\}$, giving $3^{3} = 27$; hence the profiles containing a contradiction on at least one move — the absorbing states of Proposition 2 — number

$$4^{3} - 3^{3} = 64 - 27 = 37,$$

and the absorbing fraction is

$$\frac{37}{64} = 0.578125.$$

Thus a majority of the observer's possible epistemic conditions are terminal once contradiction is admitted.

**Projection (stated assumptions).** For $k$ perceived candidate moves with independent per-move accumulation, the absorbing fraction is

$$f(k) = \frac{4^{k} - 3^{k}}{4^{k}} = 1 - \left(\frac{3}{4}\right)^{k}.$$

For $k = 3$ this reproduces the computed value: $1 - 27/64 = 0.578125$. For $k = 10$: $3^{10} = 59049$, $4^{10} = 1048576$, so $(3/4)^{10} = 59049/1048576 \approx 0.0563138$ and

$$f(10) = 1 - \frac{59049}{1048576} = \frac{989527}{1048576} \approx 0.9436865.$$

The projection assumes independence of per-move evidence streams; correlated evidence would alter it. (An earlier draft stated $f(10) \approx 0.9424$; recomputation above gives $f(10) = 989527/1048576 \approx 0.9436865$; see Appendix A.)

### 4.3 Reduction operators collapse profiles onto move sets

Under any reduction operator, the observer's perceived move set for the opponent is determined option-by-option, so the number of distinct perceived move sets is at most $2^{k} = 2^{3} = 8$. Since there are $4^{3} = 64$ assessment profiles, the average number of profiles collapsing onto each perceived move set is

$$\frac{4^{3}}{2^{3}} = \frac{64}{8} = 8.$$

For the polarity-blind operators the collapse is exact and uniform: $\rho_2$ identifies $B$ with $T$ and $N$ with $F$ (it discards the opposing evidence inside $B$), and $\rho_3$ identifies $B$ with $F$ and $T$ with $N$ (it discards the supporting evidence inside $B$). Each of the $8$ move sets then has exactly $2^{3} = 8$ preimage profiles, each option contributing $2$ of its $4$ values to one verdict. This is the precise sense in which two of the four operators ignore one kind of evidence.

### 4.4 Polarity confinement

**Proposition 1 (enable/disable directionality).** Under accumulation with any operator $\rho \in \{\rho_1, \rho_2, \rho_3\}$, adding a $T$-bit for move $m$ can only change $a_o^{c}(m)$ from $\{N, F\}$ toward $\{T, B\}$, never the reverse; adding an $F$-bit can only change it toward $\{F, B\}$, never toward $\{T, N\}$.

*Proof.* By inspection of the operator definitions in Section 3.3: for $\rho_1$, the assessment moves monotonically in the lattice $N \prec T, F \prec B$ as $p_m$ or $n_m$ crosses $0$; increasing $p_m$ never decreases the $T$-component and increasing $n_m$ never decreases the $F$-component. For $\rho_2$ the assessment depends only on $p_m$, so $F$-bits leave it unchanged and $T$-bits can only move $N \to T$; symmetrically for $\rho_3$. Since $R_j^{o}(s)$ includes $m$ iff $a_o^{c}(m) \in \{T, B\}$, and the $T$-component is monotone in $p_m$, evidence for $m$ can only grow $R_j^{o}$ and evidence against can only shrink it. $\square$

### 4.5 Absorption of contradiction

**Proposition 2 (absorption).** Under $\rho_1$ with monotone accumulation, any move $m$ for which both a $T$-bit and an $F$-bit arrive has $a_o(m) = B$ at that moment and forever after.

*Proof.* Once $p_m \geq 1$ and $n_m \geq 1$, monotonicity gives $p_m \geq 1$ and $n_m \geq 1$ at all later times, and $\rho_1(p_m, n_m) = B$ whenever both counts are positive. $\square$

### 4.6 Worked stability model

We construct a minimal model in the style of the 1995 DVD format negotiation [1], with two DMs: DM 1 (a technology alliance) and DM 2 (the computer industry group). States $S = \{s_1, s_2, s_3, s_4\}$; moves and preferences as in Section 4.1.

**Nash stability for DM 1.** From $s_1$, DM 1's only move is to $s_2$, and $s_1 \succ_1 s_2$, so no improving move: $s_1$ is Nash stable. From $s_2$, DM 1 can move to $s_1 \succ_1 s_2$: not stable. From $s_3$ and $s_4$, DM 1 has no moves in $A_1$: stable by vacuity. Hence

$$\mathrm{Nash}_1 = \{s_1, s_3, s_4\}, \qquad |\mathrm{Nash}_1| = 0 + 1 + 1 + 1 = 3.$$

**GMR for DM 1.** From $s_2$, DM 1's move to $s_1$ can be sanctioned: DM 2 responds $(s_1, s_3) \in A_2$, and $s_3$ is DM 1's worst state, so the sanction hurts DM 1; $s_2$ is GMR-stable. From $s_1$: no improving move, stable. From $s_3, s_4$: no moves, stable. Therefore

$$\mathrm{GMR}_1 = \{s_1, s_2, s_3, s_4\}, \qquad |\mathrm{GMR}_1| = 4.$$

GMR collapses all four states into one stability class: DM 2 can always sanction, so every unilateral departure by DM 1 is deterred in the GMR sense. This is the formal content of the observation in [1] that general metarationality cannot distinguish the phases of the DVD negotiation, since the computer industry group could always sanction.

**SEQ for DM 1.** The sanction at $s_2$ requires DM 2 to move $(s_1, s_3)$. Is $s_3$ a credible terminal for DM 2? At $s_3$, DM 2's only move is $(s_3, s_1)$, and $s_3 \succ_2 s_1$, so DM 2 has no improving move from $s_3$; $s_3$ is Nash stable for DM 2, hence treated as sequentially stable (this Nash-terminal credibility test is our stated convention; see Appendix A). The sanction is therefore credible, and $s_2$ is **not** SEQ-stable for DM 1:

$$\mathrm{SEQ}_1 = \{s_1, s_3, s_4\}, \qquad |\mathrm{SEQ}_1| = 3.$$

Sequential stability, which asks whether the computer industry group *would* sanction rather than merely whether it *could*, separates the phases that GMR merges.

### 4.7 Epistemic disturbance on the worked model

Let a state-preserving action by DM 2 — a public statement casting doubt on its willingness to fight — generate, for observer DM 1, an $F$-bit against the capability of DM 2's sanctioning move $m^{\ast} = (s_1, s_3)$. By Proposition 1, this can only disable $m^{\ast}$ in DM 1's perceived model: $R_2^{1}(s_1)$ shrinks from $\{(s_1, s_3)\}$ to $\varnothing$. Recomputing SEQ for DM 1 in the perceived model: from $s_2$, the move to $s_1$ now meets no available sanction, so $s_2$ becomes SEQ-stable:

$$\mathrm{SEQ}_1^{\text{post}} = \{s_1, s_2, s_3, s_4\}, \qquad |\mathrm{SEQ}_1^{\text{post}}| = 4.$$

The expansion is $|\mathrm{SEQ}_1^{\text{post}}| - |\mathrm{SEQ}_1| = 4 - 3 = 1$ state, a relative increase of

$$\frac{1}{3} \approx 0.333.$$

Conversely, an action generating a $T$-bit for $m^{\ast}$ (an exercise demonstrating capability) can only confirm the sanction; in this model it holds the stable set at $3$, since $s_2$ was already excluded.

### 4.8 Capability versus intention

The disturbance in Section 4.7 was a **capability** assessment: it removed a move from $R_2^{1}$ and thereby removed a sanction from consideration, affecting the sanction-based concepts GMR and SEQ alike (had the $F$-bit arrived before GMR was evaluated, $s_2$ would have been GMR-unstable too, since the only sanctioning response would have been unavailable). An **intention** assessment — evidence about whether DM 2 *would want* to play an available $m^{\ast}$ — leaves $R_2^{1}$ intact and therefore leaves GMR untouched, but changes SEQ, whose credibility test consults the opponent's willingness. Under the verdict operator $\rho_{\mathrm{for}}$, the counter-move is perceived credible iff the intention value lies in $\{T, B\}$, which is $2$ of the $4$ values, so the fraction of intention-assessment values that flip the SEQ verdict relative to GMR is

$$\frac{|\{T, B\}|}{|\mathcal{V}|} = \frac{2}{4} = 0.5.$$

Capability assessments thus affect all sanction-based stability concepts, and on the DM's own side also Nash stability (evidence about one's own available moves changes one's own move set); intention assessments affect only sequential stability.

## 5. Results

All numbers below are computed in Section 4 with shown arithmetic; none are empirical measurements.

- **R1 (Epistemic state space).** With $k = 3$ perceived candidate moves and four-valued assessments, the observer's epistemic state space has $4^{3} = 64$ profiles, of which $64 - 27 = 37$ are absorbing contradictory profiles under monotone accumulation with $\rho_1$; the absorbing fraction is $37/64 = 0.578125$.
- **R2 (Profile collapse).** The $64$ assessment profiles collapse onto at most $2^{3} = 8$ perceived move sets, with $64/8 = 8$ profiles per move set on average, and exactly $8$ preimages per move set for each polarity-blind operator ($\rho_2$, $\rho_3$).
- **R3 (Operator blindness).** Of the four canonical reduction operators, exactly two ($\rho_2$, $\rho_3$) ignore one kind of evidence and one ($\rho_4$) ignores both; only $\rho_1$ is evidence-complete.
- **R4 (Polarity confinement and absorption).** Supporting evidence can only enable perceived moves; opposing evidence can only disable them; $B$ is absorbing under monotone accumulation (Propositions 1 and 2, proved).
- **R5 (Stability separation on the worked model).** For DM 1, $\mathrm{GMR}_1 = \{s_1, s_2, s_3, s_4\}$ with $|\mathrm{GMR}_1| = 4$, while $\mathrm{SEQ}_1 = \{s_1, s_3, s_4\}$ with $|\mathrm{SEQ}_1| = 3$: general metarationality merges all four states into one stability class and sequential stability separates them, a difference of $4 - 3 = 1$ state.
- **R6 (Epistemic disturbance effect).** A single state-preserving action generating an $F$-bit against the capability of the sanctioning move $m^{\ast} = (s_1, s_3)$ expands the sequentially stable set from $|\mathrm{SEQ}_1| = 3$ to $|\mathrm{SEQ}_1^{\text{post}}| = 4$ states, an absolute increase of $1$ state and a relative increase of $1/3 \approx 0.333$.
- **R7 (Capability/intention asymmetry).** Under the verdict operator $\rho_{\mathrm{for}}$, the fraction of four-valued intention assessments that flip the SEQ verdict relative to GMR is $|\{T, B\}|/|\mathcal{V}| = 2/4 = 0.5$; capability assessments affect GMR, SEQ, and (on the assessing DM's own side) Nash stability, while intention assessments affect only SEQ.

## 6. Discussion

**Limitations.** The counting results of Sections 4.2 and 4.3 rest on an independence assumption: each of the $k = 3$ perceived candidate moves accumulates evidence from an independent stream. Correlated evidence — a single leaked document bearing on several moves at once — breaks the product structure $4^{k}$, and the absorbing fraction $f(k) = 1 - (3/4)^{k}$ becomes a projection valid only under independence; the $k = 10$ value $f(10) = 989527/1048576 \approx 0.9436865$ is likewise a projection, not a measurement. The worked model of Section 4.6 is a stylized four-state, two-DM reduction of the 1995 DVD format negotiation, not a faithful reconstruction of that negotiation's option table; its purpose is to exhibit the GMR/SEQ separation mechanism, not to reproduce historical stability findings. The credibility test used in the SEQ computation — treating a Nash-stable terminal for the sanctioning opponent as credible — is a stated convention (Appendix A); other credibility conventions (for example, requiring the terminal to be sequentially stable for the opponent under full SEQ recursion) could change $\mathrm{SEQ}_1$.

**Failure modes.** Three are visible. First, contradiction flooding: since $37/64 = 0.578125$ of the three-move epistemic space is absorbing under $\rho_1$, a realistic evidence stream that occasionally supplies both a $T$-bit and an $F$-bit for the same move will drive the observer into $B$ and freeze the perceived model; a practitioner using $\rho_1$ needs a contradiction-repair mechanism, which this framework deliberately does not supply. Second, operator choice masquerading as analysis: an analyst using $\rho_2$ or $\rho_3$ discards one kind of evidence entirely (Section 4.3), so two analysts with identical evidence streams can report disjoint perceived move sets while each believes the analysis is complete. Third, capability/intention conflation: if an analyst feeds intention evidence into the capability channel, the perceived move set $R_j^{o}(s)$ changes and every sanction-based stability concept shifts, even though no availability fact changed; the $0.5$ flip fraction of R7 quantifies how exposed SEQ is to this misrouting.

**Falsifiability.** The structural claims are falsifiable within the formalism. Proposition 1 fails if some reduction operator maps increased $p_m$ to a decrease in the $T$-component; Proposition 2 fails if accumulation is non-monotone (for example, evidence decay or retraction), in which case $B$ need not absorb. The GMR/SEQ separation on the worked model fails if a credibility convention renders the sanction at $s_2$ non-credible, collapsing $\mathrm{SEQ}_1$ to $\mathrm{GMR}_1$. The disturbance result fails if state-preserving actions are modeled as physical moves to a distinct state — then the expansion from $3$ to $4$ stable states is an artifact of the epistemic augmentation rather than a consequence of evidence flow. Empirically, the claim that state-preserving actions matter would be falsified by a real negotiation dataset in which re-annotating announcements and disclosures as inaction leaves all stability classifications unchanged.

**Open questions.** Does the absorbing fraction $f(k) = 1 - (3/4)^{k}$ admit a useful lower bound under bounded correlation between evidence streams? Can the reduction-operator taxonomy be extended to operators that are evidence-complete but non-monotone, and do any such operators preserve Proposition 1? Is there a stability concept intermediate between GMR and SEQ that responds to intention assessments without requiring full sequential recursion? Finally, the corpus limitation noted in Section 2 stands: entries [9]–[13] of the available bibliography were not substantively engaged, and a broader survey of epistemic-repair and agent-failure literatures might supply the contradiction-repair mechanism this framework lacks.

## 7. Conclusion

We augmented the graph model for conflict resolution with epistemic states so that state-preserving actions — announcements, exercises of rights, leaks, selective disclosures — are first-class transitions distinct from both physical moves and inaction. Evidence flows through observer-specific interpretation maps into four-valued assessments that separate capability from intention. Three structural results organize the framework: polarity confinement (evidence for a move can only enable it in the observer's perceived model, evidence against can only disable it), the evidence-blindness of two of the four canonical reduction operators, and the absorption of contradiction under monotone accumulation, with $37/64 = 0.578125$ of a three-move observer's epistemic space absorbing. On a fully computed four-state model in the style of the 1995 DVD format negotiation, general metarationality merges all four states into one stability class while sequential stability separates them, and a single state-preserving action — one $F$-bit against the sanction's capability — expands the sequentially stable set from $3$ to $4$ states, a relative increase of $1/3 \approx 0.333$. The capability/intention distinction is not decorative: capability assessments move every sanction-based stability concept, intention assessments move only sequential stability, and misrouting between the two channels is quantitatively exposed, with $2/4 = 0.5$ of intention values flipping the SEQ verdict. The framework is mechanizable in the same spirit as the Lean 4 formalization of the QCW-GMCR, and its counting consequences are elementary enough to audit by hand.

## References

[1] TITLE: arXiv Query: search_query=&amp;id_list=2610.11690&amp;start=0&amp;max_results=1
[2] Epistemic Disturbance in the Graph Model for Conflict Resolution: State-Preserving Actions, Four-Valued Assessments, and the Distinction between Capability and Intention. arXiv:2610.11690v1. https://arxiv.org/abs/2610.11690v1
[3] A Four-Valued Graph Model for Conflict Resolution: Core Framework and a Machine-Checked Formalization in Lean 4. arXiv:2609.11174v2. https://arxiv.org/abs/2609.11174v2
[4] On quantum semigroup actions on finite quantum spaces. arXiv:0810.0596v3. https://arxiv.org/abs/0810.0596v3
[5] G-CSEA: A Graph-Based Conflict Set Extraction Algorithm for Identifying Infeasibility in Pseudo-Boolean Models. arXiv:2509.13203v1. https://arxiv.org/abs/2509.13203v1
[6] State Definition for Conflict Analysis with Four-valued Logic. arXiv:2207.11733v1. https://arxiv.org/abs/2207.11733v1
[7] Counting cliques without generalized theta graphs. arXiv:2311.15289v2. https://arxiv.org/abs/2311.15289v2
[8] Optimal 3D Angular Resolution for Low-Degree Graphs. arXiv:1009.0045v1. https://arxiv.org/abs/1009.0045v1
[9] Measurement of the Flux of Ultrahigh Energy Cosmic Rays from Monocular Observations by the High Resolution Fly's Eye Experiment. arXiv:astro-ph/0208243v7. https://arxiv.org/abs/astro-ph/0208243v7
[13] https://papers.qnfo.org/papers/mechanistic-ethics-and-the-biology-of-meaning/. QNFO: Mechanistic-Ethics.