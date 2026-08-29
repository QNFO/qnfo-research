---
title: "Distinction, Number, and the Empirical Filter: The Pre-Arithmetic Research Framework"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-29"
doi: "10.5281/zenodo.22159888"
license: "CC BY 4.0"
status: "published"
version: "0.2"
---

## Abstract

Several research lines in mathematical physics begin from identities between arithmetic
objects and partition functions, or between hierarchical structure and ultrametric geometry,
and ask whether any physical system realizes the resulting structure. Each such line must
answer the same two questions, and most failures in the literature come from answering them
carelessly: which of these structures is being claimed as real, and what observation would
show the claim false. This paper states the discipline once, as a reusable framework. It
constructs a nine-level ladder from the primitive of distinction to the empirical filter of
physics, with one construction operation between each pair of levels; it states two boundary
rules governing any movement up the ladder — a rule against uncommitted reification of the
primitive, and a rule that no mathematical isomorphism passes as a physical realization
without a stated measurement protocol, a null model, and a falsification condition; and it
defines a compact claim record that any research claim can carry, together with mechanical
demotion rules for claims that violate the boundary rules. The framework makes no empirical
claims of its own. It systematizes discipline that is currently distributed across seven
published records of the QNFO program [@umporr014; @res021; @res027; @res028; @res029; @res030; @res031], and it states the one claim it does make — that the
ladder covers the published lineage without remainder — together with a falsification
protocol, so the framework itself can be checked the way it asks everything else to be
checked.

## 1. Introduction and scope

The arithmetic-statistics program at QNFO has published, during 2026, a sequence of records
connecting number-theoretic structure to statistical mechanics. A gas whose modes are
indexed by primes, with logarithmic single-particle energies, has partition functions that
are exactly zeta objects: unrestricted occupation reproduces the Riemann zeta function, and
squarefree occupation reproduces the ratio of zeta functions at argument and double
argument [@res027]:

$$ Z_{\mathrm{B}}(\beta)=\prod_p \left(1-p^{-\beta}\right)^{-1}=\zeta(\beta),\qquad
Z_{\mathrm{F}}(\beta)=\prod_p \left(1+p^{-\beta}\right)=\frac{\zeta(\beta)}{\zeta(2\beta)},\qquad
\ln Z_{\mathrm{MB}}(\beta)=\sum_p p^{-\beta}=P(\beta). $$

Here $Z_{\mathrm{B}}$, $Z_{\mathrm{F}}$, and $Z_{\mathrm{MB}}$ are the partition functions under
unrestricted, squarefree, and Boltzmann occupation respectively, and $P$ denotes the prime zeta
function. Bounded-occupation generalizations form a continuous family between the two
[@res028]. A companion record consolidated the correspondence and its practitioner-facing
reading [@res029], and a computational study then adjudicated whether the arithmetic cut can
be distinguished from non-arithmetic alternatives with matched level density [@res030].
Parallel work on hierarchy distance established that the number of distinctions required to
separate two objects is an ultrametric that does not depend on the realization — taxonomy,
p-adic digits, or Laurent coefficients — and that this distance is the canonical finite
distance of the program [@umporr014].

Each of these records had to solve, independently, the same methodological problem: where a
mathematical identity ends and a claim about the physical world begins. The present
framework is the extracted common discipline. It is a methodological scaffold, not an
empirical result: it makes no claim about what the world is like, and none of its nine
levels asserts anything ontic on its own.

The framework is motivated by a simple failure mode. Two extreme positions repeatedly
appear in work of this kind. One treats a combinatorial identity — a partition function
equal to a zeta function — as if it were already a statement about bosons or fermions. The
other treats all such identities as content-free. Both positions lose the same thing: the
controlled passage from a formal structure to an empirical claim, which is the only place
where the correspondence acquires content. The framework fixes what that passage requires,
in advance, for every claim in the program. A reader of any QNFO record can locate each of
its claims on the ladder, see the declared commitment level of each, and read exactly what
observation would refute it. This is the framework's purpose: to make the map-territory
boundary of an arithmetic-physics program legible, and its empirical commitments auditable,
without requiring every paper to rebuild the discipline from scratch.

## 2. The nine-level construction ladder

The framework organizes every research object by the level at which it is constructed. The
levels are ordered; each is built from the one below by a single named operation, and the
ordering is strict in the sense that skipping levels is not permitted without declaring
every intermediate step.

1. **Distinction.** A cut separating inside from outside. The minimal unit of structure;
   the framework takes it as a primitive. Following the Laws of Form lineage
   [@spencerbrown1969], a system is constituted by the distinctions that define it. Nothing
   is asserted here about what the world is made of: the cut is a construction primitive of
   the language, not a claimed constituent of reality.
2. **Pre-arithmetic structure.** Structure without number: order, hierarchy, partition,
   adjacency. The distinction-count distance between two leaves of a rooted tree — the
   number of cuts needed to separate them — is defined at this level: with $d(a,b)$ the
   number of distinctions required to separate leaves $a$ and $b$, the strong triangle
   inequality $d(a,c)\le\max\{d(a,b),\,d(b,c)\}$ holds, so the structure is an ultrametric
   before any prime or valuation appears [@umporr014]. Ultrametric structure is
   therefore pre-arithmetic: it exists whether or not counting exists.
3. **Arithmetic.** Counting and composition of distinctions. Concatenation of cuts gives
   addition; iteration across independent cut-families gives multiplication; irreducible
   multiplicative distinctions are the primes; unique factorization is the composition law.
   The construction operation of this level is counting.
4. **Number theory.** Patterns of the composition: the distribution of irreducibles,
   factorization statistics, and the generating functions of the composition, including
   L-functions. The operation is pattern discernment on the output of counting.
5. **Valuation.** Assigning size to distinctions: norms and absolute values. By
   Ostrowski's theorem there is one Archimedean place and one p-adic place per prime; the
   p-adic valuation is one realization of hierarchy distance — not its ground, which lives
   at level 2. The operation is sizing.
6. **Geometry.** The resulting relational form: metric and ultrametric spaces as the form
   taken by valued distinctions, including their rigidity properties. The operation is
   taking form.
7. **Information.** Distinction made operational: counting distinctions as bits, entropy,
   and the localization of distinctions in two-point statistics rather than one-point
   thermodynamic functions [@res030]. The operation is operationalization.
8. **Measurement.** The finite-resolution application of valuation to observation: which
   observable, on which system, with which instrument, at which resolution and noise
   budget — what a finite observer can actually distinguish. The operation is finite
   resolution.
9. **Physics.** The empirical filter: falsification decides which of the structures are
   real. The operation is filtering by observation.

The ladder is a translation device as much as a construction: each level corresponds to a
recognizable disciplinary home, which makes the framework legible outside its program of
origin.

| Ladder level | Standard disciplinary term |
|:-------------|:---------------------------|
| Distinction | boundary, cut (Laws of Form) |
| Pre-arithmetic | hierarchy, order theory, cladistics |
| Arithmetic | counting, factorization |
| Number theory | distribution of irreducibles, L-functions |
| Valuation | norms, places (valuation theory) |
| Geometry | metric and ultrametric spaces |
| Information | entropy, two-point statistics |
| Measurement | metrology: protocol, resolution, noise |
| Physics | falsifiability, empirical adequacy |

Three structural rules complete the ladder. First, every claim, model, and interpretation
declares its level or its span of levels; a claim that cannot state its level is not yet a
claim. Second, work within a level is the default and needs no justification, while every
cross-level move requires a declared bridge. Third, movement downward is interpretation,
not derivation: a physical result may reinterpret an arithmetic object, but it does not
derive it. Violations of these rules — particularly conflating two objects that live at
different levels, such as prime-gap statistics and zero statistics [@res030] — are the
framework's primary defect class, and are adjudicated case by case in the records cited.

## 3. The two boundary rules

The ladder says where objects live; two boundary rules say what may be claimed about them.

### 3.1 Committed reification only

The primitive of distinction is methodological by default. Treating it — or anything built
on it — as a constituent of the world is a further commitment, and the framework requires
that commitment to be explicit, made per claim, made in advance, and accompanied by the
full realization requirements of Section 3.2. A commitment made after a null result has no
force; the discipline exists so that ontology is never smuggled into formalism
retroactively. The framework itself commits to nothing ontic anywhere on the ladder.

### 3.2 From isomorphism to realization

A mathematical isomorphism — however exact — is a map, not a territory. No claim may pass
from one to the other without three items stated in advance. First, a measurement
protocol: which observable, on which system, with which instrument, at which resolution.
Second, a null model: what the data would look like if the structure were absent. The
canonical pattern in this program is the matched-level-density null, in which synthetic
spectra carry the same smoothed level density as the target but none of its arithmetic
structure [@res030]. Third, a falsification condition: the observation, specified before
data collection, that would refute the claim. The framework states these three items as
one requirement because a protocol without a null model cannot say what a positive result
means, and a null model without a falsification condition cannot end an inquiry.

Two reporting rules accompany the requirement. Quantitative claims report effect sizes,
not only significance levels: a large deviation in one spectral window can carry little
information about the rest of the spectrum, and the reportable object is the full
discriminating curve, not a single threshold crossing [@res030]. And claims whose
observables are derived from one underlying two-point function — pair correlation, spectral
form factor, number variance — are one channel, not three independent confirmations, and
are corrected accordingly.

### 3.3 The claim record

Every claim that follows the framework carries eight fields: its ladder level; its carrier
(whether it is definitional, formal, computational, empirical, or engineered); its ontic
commitment (methodological by default, heuristic, or ontic); its map-territory status (map,
bridge, or territory); and, whenever the claim reaches for physical reality, the protocol,
null model, and falsification condition of Section 3.2. Claims about the framework itself
are permitted and carry the same record with level marked as meta-level.

The record is made auditable by mechanical demotion rules. Any bridge or territory claim
missing one of the three mandatory items — protocol, null model, or falsification
condition — is demoted one step per missing item, from territory to bridge to map, and no
further than map. An ontic commitment without the full triple is demoted to heuristic.
Where two violations apply to one claim, both demotions apply and the lower status wins.
The rules are total: every claim state has exactly one outcome and every demotion
terminates, which makes the record's integrity checkable by machine — a property the
deposited verification suite exercises exhaustively.

## 4. Relationship to the published records

The framework restates none of the results it systematizes. The hierarchy distance and its
realization independence are established in [@umporr014]. The exact partition-function
correspondence — unrestricted occupation giving the zeta function, squarefree occupation
giving its double-argument ratio — is established in [@res027] and extended to bounded
occupation in [@res028]. The consolidated map and its practitioner-facing reading are given
in [@res029]. The computational adjudication of the arithmetic cut against matched-density
nulls, including the location of the arithmetic information in two-point statistics, is
given in [@res030]. The companion consolidation record [@res031] audits the
dictionary and its five-level interpretive ladder at paper level; the present framework
generalizes that ladder to the nine levels above, which re-partition its upper half rather
than extending it, and the two records are kept consistent on that point.

The framework's level assignments to the published lineage are stated in the accompanying
source archive. Two assignments that the first version flagged as provisional — the measurement-level
reading of [@res029] and the span assigned to [@res021] — have been adjudicated: the
measurement-level reading was withdrawn in favor of an operational reading, and the span
is stated with its declared bridges. The adjudications, with per-record evidence,
accompany this version.

## 5. Verification

The framework's quantitative and mechanical content is checked by a deposited script that
(1) verifies the Euler-product identity underlying level 3 numerically, including the
squarefree ratio and the bounded-occupation endpoint; (2) verifies the ultrametric
triangle for the distinction-count distance on random hierarchies; (3) exhaustively checks
that the demotion rules of Section 3.3 terminate and assign exactly one outcome to every
claim state; and (4) checks the integrity of the ladder and of the cross-level assignment
table. The script is deterministic, dependency-free, and re-runnable from the deposited
layout; its full output is deposited alongside this paper.

## 6. The framework's own claim

The framework makes exactly one claim: that the nine-level ladder covers the published
lineage of the program without remainder — that every published object assigns to at least
one level or declared span. The claim fails if a published object cannot be assigned to
any level or span; it fails in a second, independent way if a defect already adjudicated in
the lineage turns out not to be adjudicable by the two boundary rules, which would show a
third rule type is needed. Both failure modes are specified in advance, the level
assignments are listed record by record in the source archive, and the provisional
assignments are named above. The framework asks of itself only what it asks of every claim
that passes through it.

## References
