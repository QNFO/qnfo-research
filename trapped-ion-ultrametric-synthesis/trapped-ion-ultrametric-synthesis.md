---
title: "The Trapped-Ion Ultrametric Testbed: A Falsifiability Register for Testing p-Adic Structure in Quantum Dynamics"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-08-20"
version: "1.4"
license: "CC BY-NC-SA 4.0"
doi: "10.5281/zenodo.22025544"
status: "published"
keywords: ["trapped-ion quantum simulation", "ultrametric physics", "p-adic", "Bruhat-Tits", "zitterbewegung", "Page-Wootters", "dissipative stabilization", "falsifiability", "quantum error correction", "tensor networks"]
abstract: |
  Twenty-one published records from a single research program, spanning December 2025 to
  August 2026, are here organized into one testable claim: trapped-ion quantum simulators
  are the first near-term platform on which ultrametric (p-adic) structure in quantum
  dynamics can be accepted or rejected by measurement, and passive, dissipation-structured
  hardware is the engineering embodiment of that structure. The synthesis contributes a
  falsifiability register: five observables, each with a pre-registered prediction, a
  kill-condition, and an apparatus already demonstrated in the cited records. It also
  records what the program has already ruled out, including the finding that generic
  Page-Wootters clock-rest coupling violates ultrametricity at a 29-35 percent rate while
  diagonal coupling yields exact ultrametric structure -- the very asymmetry the trapped-ion
  protocol measures -- and the economic finding that trapped ions rank last among seventeen
  platforms on a joules-per-solution basis, making the ion trap a physics testbed rather
  than a production economics play. The program-level nulls the register must respect are
  kept on the same ledger: the cosmological log-periodic null, the biophoton anti-ultrametric
  null, and the ultrametric-QEC independent-error threshold. The paper states its assumptions
  explicitly: the falsifiable content rests on two named imported inputs, and the claims end
  where those inputs begin. A practitioner section specifies what can be built today without
  any new theory.
---

## 1. Introduction

Between December 2025 and August 2026, a research program published twenty-one records on
trapped-ion quantum computation, p-adic geometry, and the epistemology of physics. Read
individually, they look like three different projects: an experimental physics effort, a
mathematical physics effort, and a philosophy-of-science effort. This paper argues they are
one project, and that reading them as one project changes what a practitioner should do
next.

The unifying claim is structural, not metaphysical. A tree-shaped hierarchy -- the
Bruhat-Tits tree of p-adic geometry, the hierarchy of conditional quantum states under a
global constraint, the hierarchy of stabilizer and dissipative error correction, and the
hierarchy of claims ranked by evidential weight -- appears in all three movements
[@qnfo2026pwprotocol; @quni2026tnbt; @quni2025gkp; @quni2026falsifiability]. The claim made
here is that this appearance is testable on hardware that already exists, and that a set of
falsifiable observables with kill-conditions is the correct way to carry the claim forward.
This paper deliberately does NOT claim the tree structure has been confirmed. It claims
only that the structure is now testable, and it supplies the register by which it will be
tested.

Why a reader should care: near-term quantum hardware needs discriminating experiments, not
only gate-count benchmarks. A measurement that could rule out an entire class of
ultrametric interpretations of quantum dynamics -- or fail to rule it out -- is worth more
than another demonstration that a simulator can simulate. This paper hands an experimental
group a ready-to-run menu of such measurements, with predicted values, kill-conditions, and
the apparatus requirements already worked out in the cited records.

The paper's assumptions are stated at the end (Section 10); the derived
content of this paper is organizational: resource counts, predicted values, and the
register itself. Two named imported inputs carry the physical content: the Ultrametric
Bridge Theorem, which states that conditional quantum states under a global constraint
necessarily form ultrametric hierarchies [@quni2026bridge], and the Silent Parameter
Principle, which identifies the truncated SU(2) representation ring with the character ring
of the 2-adic units [@qnfo2026zbwadelic]. The premises END there: this paper neither
re-derives nor independently verifies those inputs, and no claim in this paper is stronger
than its inputs.

## 2. The Twenty-One Records: Three Movements

The twenty-one records sort into three movements.

**The testability movement** asks whether p-adic structure is measurable on trapped-ion
hardware. A protocol for testing ultrametricity via a Page-Wootters clock experiment
specifies a single trapped ion, laser-driven carrier and sideband transitions, conditional
state tomography, and an eight-week timeline on existing apparatus [@qnfo2026pwprotocol].
A companion analysis of 8,000 simulated Wheeler-DeWitt systems establishes the prediction
the protocol measures: generic clock-rest coupling violates the Parisi ultrametricity
condition at a 29-35 percent rate, while coupling diagonal in the clock eigenbasis yields
exact ultrametric structure [@quni2026pwdistances]. The Zitterbewegung is re-read as an
adelic observable with a 2-adic frequency of $\sqrt{2} \cdot 2mc^2/\hbar$, a 41.4 percent
deviation from the Archimedean value, and a single-ion timeline of 2028-2032
[@qnfo2026zbwadelic]. The oscillatory motion itself arises in the
Dirac equation [@dirac1928]. Two feasibility studies examine whether a vortex-enhanced
amplification mechanism can lift the sub-Compton-scale signal above the noise floor, and
conclude the question is open pending signal-to-noise work [@quni2026vortexD;
@quni2026vortexI]. A due-diligence assessment of the Innsbruck qudit program verifies the
measured light-shift gate fidelities (99.6 to 93.7 percent for dimensions 2 through 5) that
such experiments would inherit [@quni2026ringbauer; @ringbauer2022; @ringbauer2023;
@ringbauer2024]. A Monte-Carlo study extracts effective transient dimensions of 6.2 and 7.9
for diffusion on p-regular trees with p equal to 2 and 3, against the integer-line baseline
of 1.0 [@quni2026padicdiffusion]. An audit of a tunable quantum neural network demonstrates
the program's testing discipline: the strongest claim survives and the advantage claims do
not [@qnfo2026bqnnaudit].

**The architectural movement** asks what hardware built on the same structure looks like.
A room-temperature trapped-ion architecture stabilizes Gottesman-Kitaev-Preskill states
autonomously through engineered dissipation, converging to the GKP manifold when the
cooling rate exceeds the heating rate by more than $\pi$ [@quni2025gkp]. The Spin-Free
Substrate protocol simulates Posner-molecule nuclear spin dynamics with six global
Molmer-Sorensen gates per simulated second at 96.9 percent circuit fidelity, and names the
design principle connecting Kane-type, Posner-type, and trapped-ion architectures
[@quni2026spinfreeA; @quni2026spinfreeB; @fisher2015]. Quantum Architectonics argues the passive path --
letting structure suppress error -- against the active-correction path that fights the
second law [@quni2026architectonics]. A p-adic metrology proposal claims sub-shot-noise
sensing from hierarchical noise correlations on a room-temperature photonic platform with
roughly ten entangled photons [@quni2026metrology]. A dimensionless reformulation of
fifty-three physics equations in Planck units supplies the place-democratic bookkeeping the
movement uses [@quni2026ostrowski]. Four QEC-geometry records complete the movement. The
tree-topology error-correction record gives the program's QEC architecture its earliest
published form (December 2025) and carries the constraint that the independent-error
threshold of ultrametric qudit codes sits near $2.0\times10^{-4}$, roughly fifty-five times
below the surface-code threshold [@ultrametricquantum2025]. The QEC-Darwinism record engages
an external no-go theorem -- quantum error correction and Quantum Darwinism cannot coexist
above a critical logical fidelity $F_L > 0.874$ [@maity2026exact] -- and shows that the
theorem's proof chain assumes Archimedean geometry (Shannon entropy, additive collective
couplings), with the ultrametric reading as the loophole the theorem does not close
[@archimedeanshadows2026]. A prime-valuation assessment of the same QEC structure applies
the program's testing discipline inward, reading the branch-depth structure as mostly
relabeling and flagging its own 83 percent classifier result as unverified-internal
[@primevaluation2026]. One Table, Two Regimes assembles the standard-model particle table
and the condensed-matter excitation zoo into a single pattern table on the Bruhat-Tits
tree, with statistics read as a tree-automorphism phase [@onetable2026].

**The methodological movement** supplies the discipline. The Falsifiability Crisis record
diagnoses five structural patterns by which contemporary high-energy physics and cosmology have become
effectively unfalsifiable, and proposes the Bayesian delta-log-odds gate as the remedy
[@quni2026falsifiability]. The Reification record names the failure mode the other two
movements must avoid: mistaking a mathematical model for a mind-independent object
[@quni2026reification]. The Foundations record argues that Shor's algorithm is a
theoretical artifact defined under unrealizable conditions, and that error correction fails
to suppress errors beyond current scales due to correlated failures [@quni2026foundations].
An evidence-graded adjudication of five objections to the post-quantum synthesis completes
the movement: each objection is graded on evidence, none overturns the standard, and the
adjudication is published rather than answered privately [@fiveobjections2026].

The program's own archive is imperfect, and this paper records the imperfections rather
than hiding them. Two pairs of records are duplicate or near-duplicate deposits rather than
clean version chains (the Spin-Free Substrate pair [@quni2026spinfreeA; @quni2026spinfreeB]
and the vortex-feasibility pair [@quni2026vortexD; @quni2026vortexI]); version labels across
the set are inconsistent; and the archive's internal identifier table carries missing and
cross-wired DOI fields for several records (Section 12). A converged program should have a
converged archive; the disorder is disclosed here as a data-quality finding.

## 3. Lineage: How the Register Descends from Earlier Work

The twenty-one records did not appear from nowhere. Each movement is the latest link in a
published chain, and the chain is the evidence that this paper is a continuation rather
than a restart. A reader can follow the citations backward from any register entry to
its oldest published premise.

**The audit lineage.** The critique of quantum-computing claims began with the
reassessment of quantum computation's foundations [@quni2026foundations], proceeded
through the energy-accounting benchmarks of the competitive landscape
[@qnfo2026jpcubcl], the qudit extension [@quni2026quditadv], and the
quantum-neural-network audit [@qnfo2026bqnnaudit], and reaches the trapped-ion
due-diligence record cited in this paper [@quni2026ringbauer]. The register's energy
discipline is inherited from this chain.

**The ultrametric lineage.** The claim that p-adic structure is physically testable
descends from the number-theoretic classification of error-correcting codes
[@qnfo2026uf], the ultrametric bridge theorem [@quni2026bridge], and the
conditional-state analysis that turned the theorem into a measurable prediction
[@quni2026pwdistances] before the trapped-ion protocol existed [@qnfo2026pwprotocol].
The Zitterbewegung entry of the register [@qnfo2026zbwadelic] continues the earlier
analysis of the effect's ultrametric readout and its bridge to anyon braiding [@quni2026zbwp1]. The
anomalous-diffusion entry [@quni2026padicdiffusion] descends from the dimensionless
reformulation program [@quni2026ostrowski; @ostrowski1916], the non-anthropocentric
units reformulation [@quni2026nonanthro], and the continuum analysis that bounds which
real-number structures carry physical content [@quni2026continuum1], and the
Monte-Carlo framework itself continues the Riemann-spectrum asymptotics program
[@berrykeating1999].

**The architectural lineage.** The passive-design claim descends from the
architectonics critique of active error correction [@quni2026architectonics], the
spin-free substrate protocol [@quni2026spinfreeA], and the autonomous GKP
stabilization proposal [@quni2025gkp], and is corroborated by the ultrametric
metrology proposal [@quni2026metrology]. The QEC-geometry line is anchored by the
tree-topology error-correction record [@ultrametricquantum2025], continues through
the prime-valuation assessment [@primevaluation2026] and the Archimedean-Shadows
engagement with the QEC-Darwinism no-go theorem [@archimedeanshadows2026; @maity2026exact],
and extends to the particle-pattern table on the Bruhat-Tits tree [@onetable2026].
The dissipation-first reading of the tree hierarchy is this paper's own synthesis of
those published claims; the chain is cited so each link can be audited.

**The methodological lineage.** The falsifiability discipline applied here descends
from the falsifiability-crisis analysis [@quni2026falsifiability], the reification
analysis [@quni2026reification], the falsifiability protocol for discrete-continuum
signatures [@quni2026qfund], the fifteen-question ignorance audit with its
companion case study [@uia2026; @iaps2026], and the objection-adjudication record
[@fiveobjections2026]. The register's kill-conditions are that
method applied to the program's own claims.

**The consilience lineage.** The synthesis of number theory and physics into one
tree-shaped structure was published in the five-pillar consilience paper
[@fivepillars2026] and the adelic core synthesis [@adeliccore2026]. The present paper
extends that line from structure to instrumentation: where the predecessor papers
established the shared geometry, this paper supplies the devices that measure it.

What the chain shows: the three movements share a published ancestry, and each
movement's latest record cites the earlier links. The chain of reasoning from the
oldest premise (the completions of the rationals [@ostrowski1916]) to the newest
instrument (a register of five kill-conditions, Section 4) runs through every one of
the twenty-one records.

## 4. The Testability Movement: A Register of Five Falsifiable Observables

The register is the paper's core artifact. Each entry states the observable, the
pre-registered prediction, the kill-condition, and the apparatus.

**R1 -- Ultrametricity violation rate in a Page-Wootters clock.** Observable: the Parisi
ultrametricity violation rate (UVR) of conditional state overlaps, measured by conditional
state tomography on a single trapped ion with electronic states as the clock and motional
Fock states as the rest. Prediction: UVR equal to zero for diagonal clock-rest coupling;
UVR in the 29-35 percent band for nondiagonal coupling [@qnfo2026pwprotocol;
@quni2026pwdistances]. The sharpening behind the prediction is verified in the source
analysis: a p-adic clock spectrum alone is insufficient -- interaction terms generically
destroy hierarchical structure -- while coupling diagonal in the clock eigenbasis forces
exact ultrametric form; the protocol must also avoid degenerate equidistant clock spectra,
whose zero violation rate is an equidistant-sampling artifact rather than genuine hierarchy
[@quni2026pwdistances]. The conditional-state dynamics inherit the ultrametric
fading-ergodicity universality class, in which local observables thermalize on timescales
shorter than the Heisenberg time [@swietek2026fading]. Kill-condition: a measured UVR
indistinguishable between the two coupling classes -- the theory predicts the split, and
the split is what is tested. Apparatus: existing trapped-ion capability; estimated eight
weeks of beam time.

**R2 -- The 2-adic Zitterbewegung frequency.** Observable: the Zitterbewegung frequency
ratio in a Dirac-simulator implementation. Prediction: $\sqrt{2} \cdot 2mc^2/\hbar$, a
41.4 percent deviation from the Archimedean value [@qnfo2026zbwadelic]. Kill-condition: a
measured ratio consistent with 1 within error. Open constraint: the vanishing-signal
question -- whether the ZBW signal is observable at all in the Foldy-Wouthuysen frame --
and the amplification-feasibility question remain unresolved in the source records
[@quni2026vortexD; @quni2026vortexI]; R2 is therefore registered as a measurement whose
SNR budget must be closed before the experiment is meaningful, not as a settled test.

**R3 -- Effective transient dimension on p-regular trees.** Observable: the return
probability decay of a random walk on p-adic trees, extractable in simulation and, in
principle, in engineered hierarchical coupling graphs. Prediction: effective transient
dimensions near 6.2 (p=2) and 7.9 (p=3), against the Archimedean baseline near 1
[@quni2026padicdiffusion]. The analytic counterpart is the continuous-time quantum walk on
ultrametric spaces, which localizes for any location [@konno2006continuoustime]; p-adic
quantum-mechanical constructions realize the same walks as confinement in p-adic balls,
with limiting distributions computable against classical counterparts
[@zunigagalindo2024padic; @zunigagalindo2025continuoustime]. Kill-condition: dimension
growth that flattens with p. This is the register's simulation-first entry: it is
executable today, with the code already deposited with the source record.

**R4 -- Dissipative break-even.** Observable: logical bit-flip suppression of an
autonomously stabilized GKP state as a function of the cooling-to-heating rate ratio.
Prediction: convergence to the GKP manifold with exponential bit-flip suppression once the
ratio exceeds $\pi$ [@quni2025gkp]. Kill-condition: no break-even at the predicted ratio in
any ion species. Constraint: break-even on one mode is not a logical qubit; the
fault-tolerance step remains unclaimed. The constraint is quantified by the record's own
threshold analysis: under independent errors the ultrametric qudit threshold is roughly
fifty-five times worse than surface codes [@ultrametricquantum2025]. Constructive external
work on p-adic qubits and p-adic Hilbert-space tensor products supplies the mathematical
scaffolding for what a logical ultrametric qubit would require [@svampa2021an;
@aniello2025the].

**R5 -- Tensor-network collapse under nonlocal perturbations.** Observable: whether the
classical simulation advantage of tensor networks for local Hamiltonian dynamics persists
when the Hamiltonian acquires controlled nonlocal terms. The tensor-network record reads
the recent tensor-network simulation results as evidence that local-Hamiltonian dynamics
are ultrametric, because local structure is exactly where the Bruhat-Tits hierarchy lives
[@quni2026tnbt]. This is the register's retrodiction entry, graded honestly in the
Bayesian accounting (Section 6): the standard area-law explanation predicts the same
success, so R5 is registered as a discriminating test rather than credited as evidence.
Prediction under the ultrametric reading: the advantage degrades under nonlocal
perturbation faster than area-law extrapolation would predict. Kill-condition: advantage
persists at area-law-predicted levels. This entry exists precisely because the
tensor-network reading currently carries zero independent evidential weight and needs a
test to earn any.

The ultrametric reading of tensor-network structure is not a post-hoc invention of this
program. A decade of external work constructs Bruhat-Tits tensor networks as holographic
quantum error-correcting codes. The p-adic AdS/CFT correspondence places the Bruhat-Tits
tree as the bulk dual of p-adic boundary CFTs, with correlation functions computed on the
tree [@gubser2016padic]; tensor-network realizations of the correspondence reproduce bulk
operator reconstruction and boundary correlators [@bhattacharyya2017tensor]; p-adic CFTs
are proven equivalent to holographic tensor networks on the tree [@hung2019padic];
geodesics on the tree reproduce quantum-error-correcting reconstruction [@heydeman2016tensor];
holographic codes have been constructed on Bruhat-Tits buildings and Drinfeld symmetric
spaces [@marcolli2018holographic]; and the Bethe-lattice renormalization group supplies the
statistical-mechanics analogue, with p-adic boundary spin correlations reproduced by tree
networks [@okunishi2023statistical]. What that literature does NOT supply is experimental
evidence about local-Hamiltonian dynamics on Archimedean hardware: those constructions are
mathematical equivalences between boundary CFT data and bulk tree data, not measurements of
whether real local Hamiltonians organize hierarchically. The zero-weight grading of
experimental evidential status therefore stands; the external literature raises the prior
that the tree structure is mathematically natural [@gubser2017geodesic], and the
discriminating test remains necessary to earn any evidential weight.

## 5. Negative Results the Register Must Respect

A testable program is one that keeps its negative results. Five are load-bearing here, and
three more are kept on the same ledger with explicit scope rules.

First, generic clock-rest coupling does NOT produce ultrametricity. The 8,000-system study
found a 29-35 percent violation rate in the generic case [@quni2026pwdistances]. This
matters because an earlier, naive version of the program's expectation -- that
ultrametricity would emerge generically from any Page-Wootters construction -- is thereby
ruled out. The surviving claim is the sharp sufficient condition: diagonal coupling. The
trapped-ion protocol is designed around exactly that surviving claim. A reader who only
sees the positive claim without the ruled-out generic case would misprice the theory.

Second, trapped ions are the wrong economics play. The joules-per-solution competitive
landscape ranks trapped ions last among seventeen platforms (8.5-16.3 J/sol) because
50-100 microsecond gate times overwhelm their room-temperature power advantage
[@qnfo2026jpcubcl]. The testbed movement is therefore a physics claim, not a production
claim; the architectural movement (passive stabilization) exists in part to attack the
gate-time problem that produces this ranking. The qudit extension projects roughly
$10^{-5}$ J/sol for a p-adic-coded qudit platform and pre-registers its own disconfirmation
condition [@quni2026quditadv] -- a projection, not a measurement.

Third, the ZBW signal may not be observable at all in the natural readout frames, and the
amplification question is open. R2 is registered with this constraint attached, not buried.

Fourth, the audit discipline has produced verdicts against the program's own preferred
direction before: the quantum-neural-network audit sustained the methodology claim and
rejected the advantage claim [@qnfo2026bqnnaudit]. The register inherits that willingness.
The prime-valuation assessment repeats the pattern in the QEC domain: the branch-depth
reading is judged mostly relabeling, and its classifier result is flagged
unverified-internal [@primevaluation2026].

Fifth, error correction at scale is diagnosed as failing beyond current scales due to
correlated failures rather than independent noise [@quni2026foundations] -- the constraint
that motivates the passive path in the first place.

Sixth, the program's own cosmology prediction is null at the 0.3 percent level. The
certified three-stage radix-agnostic detection protocol finds no discrete-scale-invariance
(log-periodic) oscillations in Planck 2018 CMB data above roughly 0.3 percent amplitude
[@radixdsi2026], a null against the prediction registered in the earlier proposal letter
[@cmblogperiodic2026]. Scope note: this is a program-level null in cosmology, not a register
observable; the register's observables are quantum-dynamics measurements, and the CMB result
constrains the discrete-scale-invariance signature family at the cosmological scale.

Seventh, the biophoton record finds an empirical quantum-transport system that is
ANTI-ultrametric: the FMO coupling matrix violates ultrametric ordering (cophenetic
correlation 0.426, p=0.984) and its exact-clustering test is null (p=0.598)
[@biophoton2026]. Generic ultrametricity is thereby contradicted by a real biological
system, sharpening the surviving claim to the named sufficient conditions rather than to a
generic expectation.

Eighth, the architectural movement's own threshold analysis is disclosed. Under independent
errors, ultrametric qudit codes show a threshold approximately fifty-five times worse than
surface codes (p_th near $2.0\times10^{-4}$ versus $1.1\times10^{-2}$)
[@ultrametricquantum2025]. The scope rule is explicit: the passive path targets the
correlated-failure regime diagnosed in the foundations record [@quni2026foundations]; the
independent-error regime is not where the architectural claim lives, and the number is
published here rather than hidden.

## 6. Evidential Weight: What Carries Weight and What Does Not

Under a Bayesian accounting, the register's entries carry unequal weight.

R1 and R2 are pre-registered predictions: their values were published before measurement
[@qnfo2026pwprotocol; @qnfo2026zbwadelic]. A measured match would be surprising under the
null hypothesis of no ultrametric structure, so both carry potential positive evidential
weight -- and none until measured. R4 is likewise pre-registered [@quni2025gkp]. R3 is
simulation evidence: it constrains the modeling claim, not the physics claim.

The tensor-network reading (R5's target) carries ZERO current evidential weight. The
area-law explanation of tensor-network success, originating in density-matrix
renormalization [@white1992], is the incumbent, and it predicts the
observed success with no reference to p-adic structure; the ultrametric reading was
formulated after the results it explains. It is labeled here as retrodiction, and it is
included in the register only as a test to be run, not as evidence in hand
[@quni2026tnbt]. The external Bruhat-Tits tensor-network literature (Section 4) raises the
mathematical prior without changing this grading: equivalence proofs between p-adic CFTs
and tree tensor networks are structural results, not measurements, and no structural result
can earn evidential weight for a claim about local-Hamiltonian dynamics.

The register maps onto the program's three-signature falsifiability roadmap [@quni2026qfund]:
R1 is an instance of the ultrametric-clustering signature; R2 is an instance of the
rational-alpha fingerprint signature, the predicted 2-adic frequency ratio being a
rational-valued fingerprint of the discrete-continuum structure; R3 supplies structural
evidence for the ultrametric-clustering signature in engineered hierarchies; R4 and R5 test
the architecture claims that would carry the signature family onto hardware. A reader who
accepts none of the program's physics can still read the register as three independently
testable signatures.

The falsifiability discipline applies symmetrically. The records that diagnose
unfalsifiability in incumbent frameworks [@quni2026falsifiability] are the same standard
under which the program's own claims are graded here: R5 is the demonstration that the
standard is applied inward.

## 7. The Architectural Movement: Passive Design as the Embodiment

The architectural claim is that the tree hierarchy is not only a geometry to be measured
but a design principle to be built. Eight records carry the argument, and its constraints
are published alongside it.

The GKP stabilization record replaces measurement-based feedback with engineered
dissipative reservoir dynamics: a mixed-species crystal couples the logical mode to a
coolant ion, exporting entropy continuously, with convergence to the GKP manifold when
cooling beats heating by more than $\pi$ [@quni2025gkp]. This is a hierarchy-respecting
design in a precise sense: stabilization is delegated to the environment's own structure
rather than imposed by an external controller -- the passive reading of the tree.

The Spin-Free Substrate protocol is the architectural bridge to simulation: it maps
Posner-molecule nuclear spin dynamics (J-couplings of 0.003-0.178 Hz; dipolar relaxation
treated as a Lindblad channel) onto 4-qubit trapped-ion circuits requiring six global
Molmer-Sorensen gates per simulated second at 96.9 percent fidelity [@quni2026spinfreeA].
The design principle named there -- the spin-free substrate -- is a MAP label: a design
pattern, not a new entity, and this paper keeps it at that status.

The metrology record extends the passive claim to sensing: hierarchical noise correlations
exploited for sub-shot-noise precision without active correction, claimed on a
room-temperature photonic demonstration [@quni2026metrology]. The demonstration claim is
reported as claimed by the source record; independent replication is not yet on record.

The architectonics record supplies the thermodynamic framing: active correction fights the
second law and pays energy for the fight; passive structure works with it
[@quni2026architectonics]. The dimensionless reformulation supplies the bookkeeping that
keeps the program's formulas place-democratic [@quni2026ostrowski].

The QEC-geometry records add the discipline and the constraint. The QEC-Darwinism record
engages the external no-go theorem directly: QEC and Quantum Darwinism cannot coexist
above $F_L > 0.874$, and the theorem's proof chain assumes Archimedean geometry -- Shannon
entropy, additive collective couplings -- so the ultrametric reading is the loophole the
theorem does not close [@archimedeanshadows2026; @maity2026exact]. The prime-valuation
assessment applies the same honesty inward, reading the branch-depth structure as mostly
relabeling and flagging its classifier result as unverified-internal [@primevaluation2026].
The particle-pattern table extends the tree geometry to the taxonomy of particles
themselves [@onetable2026]. The independent-error threshold constraint (Section 5, eighth
entry) is the movement's published boundary [@ultrametricquantum2025].

## 8. The Methodological Movement: Discipline as Infrastructure

The third movement is the reason the first two do not float away. Its four records name
the failure modes and the response: five structural patterns of unfalsifiability
[@quni2026falsifiability]; the reification pattern by which models become mistaken for
objects [@quni2026reification]; the theoretical-artifact pattern by which idealized
algorithms misdirect engineering programs [@quni2026foundations]; and the outward-facing
adjudication standard by which objections to the synthesis are graded on evidence rather
than answered privately [@fiveobjections2026].

Two instruments operationalize the discipline. The Bayesian delta-log-odds gate assigns
zero weight to explanations built after the observations they explain -- applied inward in
Section 6 to the program's own tensor-network reading. The joules-per-solution criterion
turns advantage claims into energy accounting, applied in the audit family
[@qnfo2026bqnnaudit; @qnfo2026jpcubcl; @quni2026quditadv]. A practitioner can adopt either
instrument without adopting any of the program's physics.

## 9. Practitioner Section: What Can Be Built Today

Nothing in this paper requires new theory to become useful. Five artifacts can be built by
an engineering team using the cited records alone.

**Artifact 1 -- The decision-tool register (spec-sheet).** Section 4 IS the spec-sheet.
An ion-trap team can take R1 directly to an experiment proposal: single ion, carrier and
sideband transitions, conditional state tomography, eight-week estimate, with the
predicted UVR split (0 percent diagonal versus 29-35 percent nondiagonal) as the
accept/reject criterion. The domain of validity is conditional: R1 holds for
clock-rest coupling engineered as specified; it says nothing about platforms without
clock structure. A superconducting team gains nothing from R1; a neutral-atom team might,
if a clock degree of freedom is available -- that is the conditional truth, stated plainly.

**Artifact 2 -- The SNR budget template for R2.** The ZBW test cannot be proposed until
the signal-to-noise question is closed. The two feasibility records contain the structure
of the budget (amplification mechanism, areal-rate observable, noise floor); a team can
turn them into a spreadsheet decision tool: parameterize amplification gain, measurement
time, and heating rate, and compute whether $\sqrt{2} \cdot 2mc^2/\hbar$ clears the floor
on available hardware [@quni2026vortexD; @quni2026vortexI]. The tool IS the deliverable;
the experiment is downstream of it.

**Artifact 3 -- The reproducible simulation kit.** R3 is executable today: the
Monte-Carlo code for anomalous diffusion on p-regular trees is deposited with the source
record [@quni2026padicdiffusion]. A team can re-run, extend to p equal to 5 and 7, and
publish the extended dimension table as a benchmark artifact. The ultrametric quantum-walk
literature supplies the analytic check: localization on the tree, and p-adic-well
realizations of the same walks, are published results a team can compare against
[@konno2006continuoustime; @zunigagalindo2024padic]. No hardware required.

**Artifact 4 -- The energy-audit template.** The joules-per-solution methodology is fully
specified across the competitive-landscape records [@qnfo2026jpcubcl; @quni2026quditadv].
Any hardware team can apply it to its own platform: the metric, the conservative-bound
discipline, and the published baseline values are all in the cited records. This artifact
works regardless of whether any ultrametric claim survives.

**Artifact 5 -- The QEC-Darwinism constraint checker.** The external no-go theorem
supplies a ready-made audit: for any candidate ultrametric architecture, compute the
logical-fidelity threshold against $F_L > 0.874$ and check which Archimedean assumptions
(Shannon entropy, additive collective couplings) the proof chain uses [@maity2026exact;
@archimedeanshadows2026]. A team can run this check before building: if the architecture's
claimed advantage survives only by violating an explicitly named Archimedean assumption,
the ultrametric reading is doing real work; if not, the claim is relabeling
[@primevaluation2026]. The independent-error threshold number (Section 5, eighth entry)
gives the same team the regime in which the claim is not expected to hold
[@ultrametricquantum2025].

The practitioner-facing summary is one sentence: the program hands out one ready
experiment (R1), one spreadsheet problem (R2), one benchmark (R3), and two audit templates
(Artifacts 4 and 5) -- each usable without subscribing to the interpretation that motivated
it.

## 10. Assumptions and Imported Inputs

The derived content of this paper is organizational and arithmetic: the register, the
resource counts, the predicted values, and the evidential-weight grading. The physical
content is imported, and the imports are named.

Import 1: the Ultrametric Bridge Theorem -- conditional quantum states under a global
constraint necessarily form ultrametric hierarchies, with hierarchy depth fixing the radix
[@quni2026bridge]. Import 2: the Silent Parameter Principle -- the truncated SU(2)
representation ring is isomorphic to the character ring of the 2-adic units, from which
the $\sqrt{2}$ Zitterbewegung frequency follows [@qnfo2026zbwadelic]. Supporting imports:
Ostrowski's theorem as the place-democracy frame [@ostrowski1916; @quni2026ostrowski], and
the Page-Wootters conditional-state formalism [@pagewootters1983].

Where the premises END: R1's predictions end at the Bridge Theorem's sufficient condition.
R2's predicted value ends at the Silent Parameter Principle. R5's reading ends at the
identification of local-Hamiltonian dynamics with tree structure -- a MAP claim, not a
derived one. R3 and R4 are simulation and engineering claims whose premises end at the
stated physical models (regular-tree random walks; Lindblad dissipative dynamics). R5's
external literature engagement (Section 4) is contextual citation, not an import: the
p-adic holography works are cited for the mathematical naturalness of tree tensor networks,
and none of R5's falsifiable content depends on them. No
claim in this paper reaches below these inputs. A reader who rejects Import 1 can discard
R1 without touching the rest of the register; a reader who rejects Import 2 can discard R2.
That separability is deliberate: the register is designed so that its entries fail
independently.

## 11. Falsifiability Conditions

Formally, the paper is disconfirmed by any of the following measurements:

1. UVR statistically indistinguishable between diagonal and nondiagonal clock-rest
   coupling (kills R1 and, with it, the testable bearing of the Bridge Theorem).
2. ZBW frequency ratio consistent with 1 (kills R2).
3. Effective transient dimension growth flattening with p (kills R3's fractal-trap
   reading).
4. No dissipative break-even at cooling-to-heating ratio exceeding $\pi$ in any ion
   species (kills R4).
5. Tensor-network advantage persisting at area-law-predicted levels under nonlocal
   perturbations (kills R5's ultrametric reading and confirms the incumbent).

A world in which all five conditions obtain is a world in which the twenty-one records are
interesting but disconnected engineering notes, and this paper's organizational claim --
that they are one program -- is the thing that fails. The paper asserts no stronger
consequence.

## 12. Data-Quality Findings

Cross-system identifier audit of the input records surfaced seven findings: the two
vortex-feasibility records are cross-wired in the archive's identifier table (each row
carrying the other's DOI); three records lack DOI fields entirely; one record carries a
generic internal title; and an identifier-type field is systematically mislabeled. The
duplicate-record pairs (Section 2) are the archive-level expression of the same disorder.
The v1.4 cycle adds three more findings. First, the QEC-Darwinism record's cross-system
identifiers drift: the paper_ids registry carries zenodo_doi 21819232 while the record and
concept are 21964674 and 21809888, and the living-paper store title ("Ultrametric Code
Spaces: The Bruhat-Tits Tree as a Geometry for Quantum Error Correction") differs from the
Zenodo v1.11 title ("Archimedean Shadows: The QEC-Darwinism Tradeoff in Ultrametric
Spaces") [@archimedeanshadows2026]. Second, the records added in this version continue the
version-label inconsistency documented above (v0.4, v1.1, v1.11, and unlabeled rows in the
same set). Third, the biophoton null numbers (cophenetic correlation 0.426, p=0.984) live
in the record's PDF rather than its machine-readable metadata, delaying machine
verification [@biophoton2026]. All ten
findings are published here so that the archive can be repaired, and because a
testable program that hides its bookkeeping errors invites the reification failure its own
methodology record diagnoses [@quni2026reification].

## 13. Conclusion

Twenty-one records, three movements, one testable structure. The contribution is not the
claim that ultrametric structure exists in quantum dynamics; it is the claim that the
structure is now cheap to test, and the register that makes the tests concrete. R1 is an
eight-week experiment on existing apparatus. R3 runs on a laptop. The architectural
movement gives the design language; the methodological movement gives the discipline; the
register gives the practitioners something to build, measure, or reject. If the register
fills with null results, the program has still contributed: five kill-conditions executed
is five pieces of knowledge gained, and the falsifiability discipline the records advocate
will have been demonstrated on their own claims.

## Cite this record

Cite all versions of this record via the concept DOI 10.5281/zenodo.22013263, which
always resolves to the latest version.

## References
