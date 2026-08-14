# Formal Self-Reference Limits: Objectification, Anthropocentric Conventions, and the Partial Self-Knowledge of Formal Systems

**Author:** Rowan Brad Quni-Gudzinas
**Affiliation:** QNFO
**ORCID:** 0009-0002-4317-5604
**Date:** 2026-08-14
**Version:** v0.1-draft
**Status:** draft
**WBS:** QNFO.RES.007
**Repository:** https://github.com/QNFO/qnfo-research/tree/res/paper/formal-self-reference-limits

---

## Abstract

This paper answers the seed question: *why are our formal quantitative systems uncomfortable with self-reference when they are also inherently anthropocentric — from base-10 pentadactylity to the heartbeat-Hertz second and the body-scaled meter — and can we not truly see ourselves?* We defend the **objectification thesis**: the discomfort is a structural consequence of what formal systems are, not a defect of their anthropocentric origins. A formal system is a third-person map; it excludes the mapmaker at the foundation BY DESIGN, and a system that excludes the observer can represent itself only at the cost of incompleteness or inconsistency (Gödel, Tarski, Turing). The anthropocentric traces of our systems — decimal notation from ten fingers, the second near a heartbeat, the meter from body and Earth — are convention-layer residues that never enter the formal core; they are replaceable without changing any theorem. The two halves of the question therefore do not have one answer: the units are anthropocentric but superficial, the self-reference limits are structural but not anthropocentric. The corollary is a **partial-self-knowledge thesis**: we can see ourselves truly but never totally — a total self-model requires an outside, and the mapmaker remains in the map's blind spot.

---

## 1. Introduction: The Seed Question

The question that motivates this paper is deceptively simple:

> Why are our formal quantitative systems uncomfortable with self-reference when they are also inherently anthropocentric, from base-10 pentadactylity to length of time (heartbeat Hertz) and space? Can we not truly see ourselves?

The puzzle has two premises. First, our formal systems — mathematics, logic, computation — exhibit a well-documented *discomfort* with self-reference: the liar paradox, Russell's paradox, Gödel's incompleteness theorems, Tarski's undefinability of truth, the halting problem. Second, these systems are built by embodied, self-referential agents and carry unmistakable traces of that embodiment: decimal notation derived from ten fingers [1, 2], the second historically near a resting heartbeat (~1 Hz), the meter from the Earth's meridian and the human body. The naive expectation would be that systems built by self-referential beings should be *at home* with self-reference. The observed reality is that unrestricted self-reference destabilizes them.

We argue that this apparent tension dissolves under a single diagnosis: **formal systems are objectifications**. They are built to be third-person, context-free, observer-independent maps. The anthropocentrism lives at the *interface* (units, notation, conventions); the self-reference limits live at the *core* (truth, provability, decidability). Confusing the two layers produces the illusion that our systems should be self-inclusive because they are human-made. They cannot be self-inclusive *because they are maps*, and a map that includes its mapmaker completely is not a usable map [3, 4].

The paper is organized as follows. Section 2 examines the anthropocentrism premise and separates the convention layer from the formal core. Section 3 documents the self-reference limits and the classical results that make them structural. Section 4 states and defends the objectification thesis — the locked core claim. Section 5 develops the convention-layer distinction in detail. Section 6 states the partial-self-knowledge corollary and its corroborations. Section 7 runs the cross-domain consilience gate. Section 8 answers the seed question directly. Section 9 states disconfirmation conditions. Section 10 situates the work against related literature, and Section 11 concludes.

## 2. The Premise Examined: Anthropocentrism at the Convention Layer

### 2.1 Base-10 and pentadactyly

The QNFO corpus has already established the contingency of decimal notation. The *Ten-Fingered Trap* documents that the dominance of base-10 stems not from mathematical superiority but from human anatomy — specifically the ten fingers available for counting [2]. Pentadactyly (ten digits) is demonstrably non-universal: early tetrapods such as *Acanthostega* had seven or eight digits per limb; horses stand on a single functional digit; pandas evolved a "false thumb" [2]. A civilization that counted lunar cycles (the ~29-day month) instead of fingers might have developed mathematics with a different intuitive texture from the outset [2]. The *Scaffolds and Invariants* audit (QUNSAI) extended this to a general epistemic-hygiene treatment of pi, number bases, and geometric centers, showing that our "natural" mathematical scaffolds are frequently artifacts of convention [5].

Yet the same corpus supplies the crucial counterweight: *Radix-Agnostic Detection of Discrete Scale Invariance* developed a certified, radix-agnostic three-stage protocol and found a NULL result on Planck 2018 — no physical signal privileges any radix, including $p$-adic bases 2, 3, 5, 7 [6]. And *Silent-Radix Cryptography* exploited the fact that a positional numeral cannot internally specify its own base — the "silent radix" — as a cryptographic primitive [7]. The silent radix is exactly the formal-core fact that underlies the convention-layer appearance: **the base is not part of the formal content of the numeral**. If the base never appears inside the numeral, then no theorem of arithmetic depends on which base we choose; only the *inscription* changes.

### 2.2 Heartbeat time and body space

The same separation holds for units. The second was once a fraction of the day and is roughly a resting heartbeat (~1 Hz); modern metrology defines it by $9{,}192{,}631{,}770$ oscillations of the caesium-133 hyperfine transition. The meter was once $1/10{,}000{,}000$ of a Paris meridian quadrant; it is now defined through the speed of light. The QNFO program has developed this trajectory explicitly: *From Decimal Fingers to Adelic Freedom* is a strategic roadmap from anthropocentric measurement conventions to observer-independent physics [8]; *The Decryption Key: Cognitive Architecture as the Hidden Radix of Physical Measurement* argues that human cognitive architecture functions as a hidden radix of measurement [9]; *Non-Anthropocentric Natural Units* moves from the Bekenstein bound to Ostrowski's theorem to exhibit unit systems that do not depend on any body or Earth [10]. The trajectory is consistent: units are replaced by constants, and the invariant structure of physics does not change.

### 2.3 The convention layer is not the formal core

The pattern across notation and units is identical. **Anthropocentric conventions sit at the representation boundary of our systems; they never enter the formal core.** Arithmetic in base 2 proves the same theorems as arithmetic in base 10; physics in SI seconds and meters makes the same predictions as physics in natural units. The convention layer is where the human body leaks into the map — and it is exactly the layer that can be peeled away without changing the map's content. This is the sense in which the seed question's first premise is *partially wrong*: our systems are not "inherently anthropocentric" in their formal content; they are anthropocentric only in their conventional dress.

## 3. The Discomfort Documented: Self-Reference Limits

### 3.1 The classical results

The discomfort is real and structural. The liar sentence ("this sentence is false") has no stable truth value in classical semantics. Russell's paradox [11] showed that unrestricted comprehension collapses set theory; the hierarchy of types was the surgical response [11]. Gödel [12] showed that any sufficiently strong, consistent, recursively axiomatizable system contains true-but-unprovable sentences — the system can *encode* "I am not provable" but cannot settle it [12]. Tarski [13] showed that a formal language cannot consistently define its own truth predicate [13]. Turing [14] showed that no program can decide the halting of all programs — self-application is where the diagonalization bites [14]. The 2020s have only sharpened these results: incompleteness has been extended to stably-computable and stably-consistent formal systems, i.e., systems not even computably enumerable, motivated explicitly as models of "the mathematical output of humanity" [15, 16]; and the Second Incompleteness Theorem can be derived from Tarski's undefinability theorem *without* self-reference at all [17]. The self-reference-free derivation is particularly important for our argument: it shows the limit is not an artifact of diagonal tricks but a property of any sufficiently expressive map that tries to describe its own truth.

### 3.2 Controlled self-reference

It is essential to be precise about "uncomfortable." Formal systems are not allergic to self-reference per se; they are allergic to *uncontrolled* self-reference. A rich toolkit manages self-reference productively: recursive functions with base cases; Gödel numbering (the system "sees" its own syntax as arithmetic); quines in computation (programs printing their own source); fixed-point combinators in the lambda calculus; Tarski's hierarchy of meta-languages; Russell's type theory; non-well-founded set theory (hypersets) [18]; and paraconsistent logics that tolerate local contradictions [19]. The QNFO corpus has its own extensive treatment: *The Universal Computational Topos and Strange Loops* unifies computational self-reference through the Computational Trinity Principle (Object/Model/Meta computation) and topos theory, proving that strange loops are essential features rather than pathological exceptions, with fixed-point spectra as the productive management tool [20]. *The Void Is Not False* recovers the unmarked state in logic from the calculus of indications [21]. The point is that self-reference becomes "comfortable" only when it is *stratified* — when the system that speaks is not the system spoken about. The cost of stratification is precisely that no single level contains the whole truth about itself.

## 4. The Objectification Thesis (Core Claim P6)

**P6 (locked core claim):** *The discomfort of formal quantitative systems with self-reference is a structural consequence of objectification, not a defect of anthropocentric origin: a formal system is a third-person map, and it can represent itself only at the cost of incompleteness or inconsistency (Gödel, Tarski), while its anthropocentric traces (base-10 notation, heartbeat-second, body-meter) are convention-layer residues that never enter the formal core. Consequently, "truly seeing ourselves" is possible only as partial self-representation through meta-levels — true but never total, consistent only when stratified.*

The thesis has three components.

**(A) Formal systems are objectifications.** To formalize is to take the third-person stance: to write down a finite set of rules that manipulate tokens without reference to who reads them. The mapmaker is not an axiom. This is not an oversight; it is the design that gives formal systems their objectivity — the same theorems hold for every agent, every base, every body. Objectification buys objectivity.

**(B) Self-reference limits are the price of that exclusion.** A system that excludes the observer can include the observer's *objectified image* — via Gödel numbering, a program as data, a description as an object — but the act of inclusion is always one level up. The system can point at its own blind spot ("I am not provable") but cannot see past it. The residual gap is not a failure of the map but the definition of the map: something must remain outside for the map to be about anything [3, 4].

**(C) The anthropocentric traces are not the cause.** If the discomfort were caused by anthropocentrism, then de-anthropocentrizing the units (natural units, adelic freedom [8]) should remove it. It does not: physics in natural units still cannot decide its own truth predicate; arithmetic in binary still has Gödel sentences. The two phenomena are orthogonal, and the seed question's conjunction — "uncomfortable *when also* anthropocentric" — is the very confusion the thesis diagnoses: it treats convention-layer residue as if it were formal-core content.

This diagnosis is *not* the mere truism "the map is not the territory" (MAP-TERRITORY-1 discipline [3, 4]). The map–territory distinction says a description differs from what it describes. The objectification thesis says something stronger and more specific: **the exclusion of the mapmaker is a design choice, and every structural limit of self-representation (incompleteness, undefinability, undecidability) is the ledger entry for that choice.** A map is not merely different from its territory; a map cannot contain a complete map of its mapmaker, because the mapmaker is the thing drawing.

## 5. The Convention-Layer Distinction

Section 2 established the phenomenology; here we sharpen the principle.

**Definition (convention layer).** A feature $F$ of a formal system $S$ is a *convention-layer residue* iff there exists a translation $T$ of $S$ — a change of notation, base, unit, or coordinate convention — such that (i) the theorems of $T(S)$ correspond bijectively to the theorems of $S$, and (ii) $F$ is not invariant under $T$.

**Claim C1 (convention-layer non-invariance).** Base-10 notation, the SI second, and the meter are convention-layer residues: base-2 arithmetic is theorem-preserving (the same facts hold, only the inscriptions differ [7]); unit systems are mutually convertible by constants; and the radix-agnostic DSI null shows no physical observable privileges any radix [6].

**Claim C2 (formal-core non-anthropocentrism).** No anthropocentric convention appears in the axioms of a standard formalization of arithmetic, set theory, or computation. The axioms are about successor, membership, and symbol manipulation — not about fingers, heartbeats, or bodies. The formal core is anthropocentric only in the trivial sense that it was *discovered* by anthropocentric agents.

**Claim C3 (orthogonality).** Self-reference limits persist under every convention-layer translation: Gödel sentences, Tarski undefinability, and the halting problem are invariant under base and unit change. Therefore the limits are properties of the formal core, and the core's limits are not anthropocentric. (This is the falsifiable content of the thesis — see Section 9.)

## 6. The Partial Self-Knowledge Corollary

**Corollary (partial self-knowledge).** *We can truly see ourselves, but never totally: a complete, consistent self-model from inside is impossible; self-knowledge is real and partial, delivered through meta-levels, mirrors, and stratification — true at every level, total at none.*

The corollary follows from P6 plus the classical results. A Gödel sentence is *true* — we see it from outside the system — and *unprovable inside* — the system cannot see it from within. That is the structure of genuine but partial self-knowledge: the truth is available, the totality is not. Tarski's hierarchy is the same structure generalized: every truth predicate lives one level up, and no level contains the truth about all levels. Hofstadter's strange loops are the same structure aestheticized: the loop of self-reference is real, but its "resolution" always requires the reader outside the system [20, 22].

Two independent corroborations from the QNFO corpus strengthen the corollary.

**(i) The S10 result (residual external perspective).** *The Observer Inside the Tree* tested whether embedding the observer as a node in an ultrametric TREE can eliminate the inside/outside schism. The verdict: the "observer = node" resolution survives scrutiny in a limited but genuine sense, yet the DIST function requires a global TREE topology not locally computable — *"it relocates the problem to the global topology of TREE, which is itself an external structure not derivable from any single node's perspective"* [23]. This is the partial-self-knowledge corollary in a different vocabulary: the node sees itself truly (calibration map C is well-defined internally) but not totally (the global topology remains external). The claim to "eliminate" the external perspective is an overstatement; the external perspective is relocated, never removed [23].

**(ii) The Bootstrap Theorem (self-referential calibration).** The *29-Schisms Synthesis* formalizes physics as a self-referential calibration problem and proves a Bootstrap Theorem: any theory that must calibrate its own measurement apparatus from within the system it describes converges to a unique self-consistent fixed point determined by the valuation structure of the agent's state space [24]. A unique fixed point of self-calibration is exactly "true but not total": the calibration closes, but it closes *to a fixed point*, not to a complete self-description.

Together with the quantum-measurement observer literature (S10 inside/outside; RQM/QBism comparisons in [23]) and the intuitionistic-time anthropocentrism analysis of van der Lugt as applied in the finite-precision program [25], the corollary is consilient across logic, computation, and measurement: every attempt to draw the mapmaker into the map produces a residual outside.

## 7. Cross-Domain Consilience (KIF-29)

Following the research pipeline's consilience gate, we map the thesis across five evidence-selected domains.

| Domain | Fragment | Structure found |
|:-------|:---------|:----------------|
| Logic | Gödel incompleteness; Tarski undefinability | A consistent system cannot define its own truth → structural blind spot [12, 13] |
| Computation | Halting problem; quines; stably-computable incompleteness | No universal decider of self-behavior; same diagonal structure [14, 15, 16] |
| Quantum measurement / physics | S10 observer inside/outside | Residual external perspective relocates, never eliminates [23] |
| Embodied cognition | Pentadactyly; heartbeat-second; body-meter | Convention-layer residues, replaceable without theorem change [2, 5, 8, 10] |
| Epistemology | Map/territory; MAP-TERRITORY-1 | The mapmaker cannot fully draw the mapmaker into the map [3, 4] |

**Minimum-viable-findings (one per domain):** logic — the blind spot is structural (Sections 3.1); computation — the blind spot is invariant under model of computation [15]; measurement — the blind spot relocates to global topology [23]; embodiment — the conventions are removable without changing formal content (Section 5); epistemology — total self-inclusion is impossible by construction [3, 4].

**Silo cost table:** treating "anthropocentric units" (RES/embodiment) and "self-reference limits" (logic/computation) as unrelated topics costs the unifying diagnosis — the objectification thesis — and reproduces the seed question's confusion at the meta-level. Each silo owns a fragment; none owns the link.

**Meta-principle (synthesis):** *Objectification buys objectivity at the price of self-totality* — the third-person stance that makes formal systems universally shareable is the same stance that makes them unable to contain their own complete truth.

**Frontier question (deferred):** Can the self-knowledge bound of a formal system be characterized uniformly — Gödel-numbering style — across logic, computation, and measurement as a single invariant, in the way that depth unified valuation (RES.005) [26]?

## 8. Answering the Seed Question

**Why are our formal quantitative systems uncomfortable with self-reference when they are also inherently anthropocentric?**

Because the two clauses point at different layers. The anthropocentrism is real but superficial — it lives in notation and units (base-10 from fingers, the second from a heartbeat, the meter from the body), and it is exactly the layer we have already peeled away in metrology and can peel away in mathematics [2, 5, 6, 8, 10]. The discomfort is real but structural — it lives in the formal core, where any sufficiently expressive map that tries to describe its own truth or behavior must be incomplete, undefinable, or undecidable [12, 13, 14]. The systems are not "uncomfortable with self-reference because they are anthropocentric"; they are uncomfortable with *uncontrolled* self-reference because they are *objectifications* — third-person maps that exclude the mapmaker by design [3, 4, 20].

**Can we not truly see ourselves?**

We can — truly, but not totally. Gödel's sentence is true even though the system cannot prove it: the truth is visible from the meta-level, which is exactly how self-knowledge works. We see ourselves through mirrors and meta-levels — each showing truth, none showing totality [20, 22, 23]. A total self-model would require an outside that does not exist, or a fixed point that closes the loop [24]. The seed note's answer, preserved as provenance, states it best: *we can truly see ourselves, but only as finite mapmakers, never as complete self-transparent maps; the mapmaker is in the map's blind spot* [1].

## 9. Falsifiability and Disconfirmation

Per the locked core claim, the thesis is falsifiable on two independent conditions:

1. **Truth-predicate disconfirmation (against C3/P6):** exhibit a sufficiently strong, consistent, recursively axiomatizable formal system that defines its own truth predicate and proves all its own true statements. This contradicts Tarski and Gödel and would be a landmark result; its absence is not evidence of our cleverness but of the structure's stability (extended recently to non-computably-enumerable systems [15, 16, 17]).

2. **Convention-dependence disconfirmation (against C1):** exhibit an anthropocentric convention whose change alters a formal *theorem* rather than only its representation — e.g., arithmetic whose theorems depend on base choice. The silent-radix result [7] and the radix-agnostic DSI null [6] are direct negative evidence: the base is invisible to the numeral, and no physical radix is privileged.

Neither condition is met by any known system; both are stated so that a single counterexample disconfirms the corresponding component.

## 10. Related Work

**QNFO-internal anchors** (all cited and verified): Ten-Fingered Trap [2]; QUNSAI Scaffolds and Invariants [5]; Radix-Agnostic DSI Detection [6]; Silent-Radix Cryptography [7]; From Decimal Fingers to Adelic Freedom [8]; The Decryption Key [9]; Non-Anthropocentric Natural Units [10]; map-is-not-the-universe / Math is NOT the Universe [3]; A Map is Not the Universe (companion cartography discipline) [4]; Universal Computational Topos [20]; Void Is Not False [21]; Strange Loop of Being [22]; Observer Inside the Tree [23]; 29-Schisms Synthesis [24]; finite-precision/OC convergence (Gisin–Del Santo, van der Lugt application) [25]; Prime Valuation Depth (RES.005) [26]; Universal Ignorance Audit (RES.002) [27]; Knowing What We Do Not Know (RES.003) [28].

**External canon:** Russell's theory of types [11]; Gödel 1931 [12]; Tarski 1936 [13]; Turing 1936 [14]; Savelyev stably-computable incompleteness [15]; Savelyev stably-consistent incompleteness [16]; Visser Tarski→Gödel self-reference-free [17]; Aczel non-well-founded sets [18]; Priest paraconsistent logic [19]; Hofstadter GEB [22]; van der Lugt intuitionistic anthropocentric time [25]; Ifrah history of numbers (base contingency) [29].

**Novelty statement.** The fragments are classical (self-reference limits) or internal (anthropocentric conventions). The synthesis is new: the objectification thesis (P6) unifies them by locating the anthropocentrism at the convention layer and the self-reference limits at the formal core, and derives the partial-self-knowledge corollary. No external work connects convention-layer anthropocentrism to the structural self-reference limits of objectified formal systems with this corollary (evidence: OpenAlex/Crossref/Zenodo/arXiv sweeps, saved in artifacts/external-search/).

## 11. Conclusion

Formal systems are maps, and maps exclude their mapmakers by design. The anthropocentrism of our units and notation is the body leaking into the convention layer — real, but removable without changing a single theorem. The discomfort with self-reference is the formal core's price for that exclusion — structural, invariant under every convention, and the same in logic, computation, and measurement. We can see ourselves truly, because the meta-levels work; we cannot see ourselves totally, because a complete self-including map is impossible or unstable. The seed question is answered: yes, we can truly see ourselves — but only as finite mapmakers, never as complete self-transparent maps. The mapmaker is in the map's blind spot.

---

## References

[1] QNFO Research Collective. *Formal Self-Reference Limits* (seed note, 2026-08-14). Provenance artifact, artifacts/seed-note-2026-08-14.md, QNFO/qnfo-research.
[2] QNFO Research. *Ten-Fingered Trap: How Our Decimal Dependence Constrains Scientific Advancement* (2025-01). R2: qnfo/releases/2025/00/Ten-Fingered Trap.md; identifier qnfo-2025-00-ten-fingered-trap.
[3] Quni-Gudzinas, R. B. *Math is NOT the Universe: A Map is Not the Universe: Understanding the Manifold, from Fractal Geometry to Deterministic Reality* (2025-09-11). DOI: 10.5281/zenodo.17099937.
[4] QNFO Research. *Map–Territory cartography discipline* (MAP-TERRITORY-1; qnfo-core). See PROJECT-PLAN.md §7.
[5] Quni-Gudzinas, R. B. *Scaffolds and Invariants: An Epistemic Hygiene Audit of pi, Number Bases, and Geometric Centers* (QUNSAI). DOI: 10.5281/zenodo.21255344.
[6] Quni-Gudzinas, R. B. *Radix-Agnostic Detection of Discrete Scale Invariance: A Certified Three-Stage Protocol and a Null Result from Planck 2018* (2026). DOI: 10.5281/zenodo.21902891.
[7] Quni-Gudzinas, R. B. *Silent-Radix Cryptography: Exploiting the Base Ambiguity of Positional Notation as a Cryptographic Primitive* (2026). DOI: 10.5281/zenodo.21046734.
[8] Quni-Gudzinas, R. B. *From Decimal Fingers to Adelic Freedom: A Strategic Roadmap for Observer-Independent Physics* (2026-07). DOI: 10.5281/zenodo.21428829.
[9] Quni-Gudzinas, R. B. *The Decryption Key: Cognitive Architecture as the Hidden Radix of Physical Measurement* (2026-07). DOI: 10.5281/zenodo.21428825.
[10] Quni, R. B. *Non-Anthropocentric Natural Units: From the Bekenstein Bound to Ostrowski's Theorem* (2026-07). DOI: 10.5281/zenodo.21480756.
[11] Russell, B. (1908). Mathematical logic as based on the theory of types. *American Journal of Mathematics*, 30(3), 222–262.
[12] Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik*, 38(1), 173–198.
[13] Tarski, A. (1936). Der Wahrheitsbegriff in den formalisierten Sprachen. *Studia Philosophica*, 1, 261–405.
[14] Turing, A. M. (1936–37). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society*, s2-42(1), 230–265.
[15] Savelyev, Y. (2022). Incompleteness for stably computable formal systems. arXiv:2208.04752.
[16] Savelyev, Y. (2020). Incompleteness for stably consistent formal systems. arXiv:2001.07592.
[17] Visser, A. (2018). From Tarski to Gödel. Or, how to derive the Second Incompleteness Theorem from the Undefinability of Truth without self-reference. arXiv:1803.03937.
[18] Aczel, P. (1988). *Non-Well-Founded Sets*. CSLI Lecture Notes 14. Stanford: CSLI Publications.
[19] Priest, G. (1979). The logic of paradox. *Journal of Philosophical Logic*, 8(1), 219–241.
[20] Quni-Gudzinas, R. B. *The Universal Computational Topos and Strange Loops: A Unified Framework for Computational Self-Reference* (2025-11-03). DOI: 10.5281/zenodo.17435331.
[21] Quni-Gudzinas, R. B. *The Void Is Not False: Recovering the Unmarked State in Logic from the Calculus of Indications* (2026). DOI: 10.5281/zenodo.21916970.
[22] Quni, R. B. *Strange Loop of Being* (2025-05). DOI: 10.5281/zenodo.15580769. (Also: Hofstadter, D. R. (1979). *Gödel, Escher, Bach*. Basic Books.)
[23] QNFO Research Collective. *The Observer Inside the Tree: Can Self-Location in an Ultrametric Structure Resolve the Inside/Outside Schism?* (2026-07-21). DOI: 10.5281/zenodo.21473899.
[24] QNFO Research. *The Hidden Fractures: Self-Referential Calibration and the 29 Schisms of Physics* (2026). DOI: 10.5281/zenodo.21458373.
[25] Quni-Gudzinas, R. B. *Finite Specification, Ontological Indeterminism: The Gisin–Del Santo Program Converges with Autaxys Ontological Closure* (2026-07-28). DOI: 10.5281/zenodo.21647362. (Anchoring van der Lugt (2021) on intuitionistic anthropocentric time.)
[26] Quni-Gudzinas, R. B. *Prime Valuation Depth* (RES.005, 2026-08-13). DOI: 10.5281/zenodo.21918838.
[27] Quni-Gudzinas, R. B. *The Universal Ignorance Audit: A Fifteen-Question Method* (RES.002, v0.3). DOI: 10.5281/zenodo.21901984.
[28] Quni-Gudzinas, R. B. *Knowing What We Do Not Know: Ignorance Auditing, AI-Generation Detection, and the Epistemic Lessons of an AI-Assisted Research Pipeline* (RES.003, v0.3). DOI: 10.5281/zenodo.21901983.
[29] Ifrah, G. (2000). *The Universal History of Numbers: From Prehistory to the Invention of the Computer*. New York: Wiley.

---

*Prepared under the research pipeline (QNFO.RES.007). All internal DOIs verified via resolve_paper_id / D1 (see citation-audit.md). External canon entries verified against arXiv/OpenAlex/Crossref evidence saved in artifacts/external-search/. Falsifiability conditions stated in §9.*
