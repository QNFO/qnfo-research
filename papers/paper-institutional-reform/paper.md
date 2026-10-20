---
title: "Institutional Reform: Fixing the Epistemic Incentive Structure of Post-Classical Computing"
author: "Rowan Brad Quni-Gudzinas"
date: 2026-07-08
series: "The Qubit Delusion --- Phase V"
abstract: |
 The first four papers in this series established that quantum computing's failure
 is epistemic (Phase I), surveyed alternatives (Phase II), examined physical limits
 (Phase III), and proposed an investment portfolio (Phase IV). This paper addresses
 the institutional question: why did $35 billion of investment over two decades
 produce zero commercially viable quantum computers, and how do we prevent this from
 happening again? We diagnose the institutional incentive structure that rewards
 narrative production over falsifiable results --- the misalignment between venture
 capital fund horizons and quantum computing development timelines, the capture of
 government research agencies by private interests, the absence of independent
 verification protocols with enforcement mechanisms, and the regulatory vacuum in
 which quantum computing claims are made without consequence. We propose five
 institutional reforms: (1) an Advanced Computing Projects Agency modeled on
 DARPA's successful structure but restricted to post-classical computing; (2)
 mandatory independent verification for any quantum computing claim above a materiality
 threshold; (3) structural separation of quantum hardware R&D from quantum software
 and services; (4) reform of government procurement to require joules-per-solution
 metrics; and (5) creation of a public registry of claims with time-bound falsification
 criteria. We argue that without institutional reform, any technological advances in
 post-classical computing will be captured and distorted by the same incentive
 structures that produced the quantum computing bubble.
keywords:
 - institutional reform
 - quantum computing
 - venture capital
 - research policy
 - DARPA
 - independent verification
 - science policy
 - technology bubbles
---

# 1. Introduction: The Question No One Asks

Four papers have established a foundation. The qubit is a scaffold, not an
invariant. Alternative paradigms exist with greater ontological fidelity.
Physical limits impose honest boundaries. A diversified investment portfolio
is both available and defensible.

But none of these papers answer the question that anyone who has watched the
quantum computing industry over the past decade eventually confronts: **how
was this allowed to happen?**

How did $35 billion of global investment --- public and private, spanning two
dozen countries and hundreds of institutions --- produce zero commercially
viable quantum computers? How did D-Wave sell "quantum computers" to
Lockheed Martin and Google before independent benchmarking demonstrated no
speedup? How did Rigetti reach a $1.5 billion valuation via SPAC before its
stock declined over 90%? How did Microsoft claim evidence for Majorana zero
modes that was subsequently retracted, and suffer essentially no institutional
consequences?

The standard answers attribute these failures to the inherent difficulty of
the technology: quantum systems are fragile, decoherence is relentless, error
correction is expensive. This is true, but it is also *insufficient*. Many
technologies are difficult without producing systematic misinformation at
industrial scale. The difficulty of fusion energy has not produced a
comparable pattern of corporate claims repeatedly exceeding what independent
verification can support.

The difference is institutional. The quantum computing industry operates
within an incentive structure that systematically rewards the appearance of
progress over actual progress --- and that is what this paper analyzes and
proposes to reform.

## 1.1 The Institutional Question Restated

The question is not "why hasn't quantum computing succeeded?" The question is:
"given the institutional structure of quantum computing R&D, what outcome would
a rational observer have expected?"

Our answer: exactly the outcome we got. The institutional structure --- the mix
of venture capital, government grants, corporate R&D, and academic prestige
economy --- is configured to produce narrative assets, not computational ones.
The $35 billion was not "wasted" in the sense of being embezzled or
incompetently spent. It was efficiently allocated --- toward the production of
press releases, patent portfolios, academic publications, and startup
valuations that served the interests of the institutional actors involved.
That these narrative assets did not translate into computational assets is
not a bug in the system. It is a feature of the system's *selection
environment*: the incentives select for narrative production, and narrative
production is what we observe.

## 1.2 Structure of This Paper

Section 2 diagnoses the institutional incentive structure in detail. Section 3
examines the structural mismatch between venture capital and deep technology.
Section 4 analyzes the role of government research agencies. Section 5
proposes five institutional reforms. Section 6 addresses objections and
implementation challenges. Section 7 concludes.

# 2. The Anatomy of Institutional Failure

## 2.1 The Incentive Trilemma

Every institution funding quantum computing faces a trilemma:

1. **Honest evaluation.** The institution must be able to distinguish
 genuine progress from narrative production.
2. **Timely decisions.** The institution must allocate capital within
 timeframes consistent with its mandate (venture fund life, grant cycle,
 fiscal year).
3. **Competitive positioning.** In a multi-institution funding landscape,
 the institution must not be systematically disadvantaged relative to
 competitors who make more optimistic (and less honest) evaluations.

The trilemma arises because these three goals are in tension --- and, in the
current institutional landscape, they are in *direct conflict*. An institution
that attempts honest evaluation will be slower to fund than competitors who
accept narrative claims at face value. An institution that attempts timely
decisions will lack the technical depth to distinguish progress from hype.
An institution that prioritizes competitive positioning will --- rationally,
from its own perspective --- degrade its evaluation standards to match or
exceed competitors'.

The result is a **race to the bottom in evaluation rigor.** Each institution
has an individual incentive to lower its standards, and the equilibrium is a
funding environment where no institution performs rigorous independent
evaluation. The $35 billion outcome is the equilibrium of this game.

## 2.2 The Narrative Production Function

Narrative production in quantum computing follows a predictable pattern:

1. **Milestone claim.** A research group or company announces a milestone --- 
 "quantum supremacy," "quantum advantage," "error correction below
 threshold" --- accompanied by a preprint, a press release, and often a
 prestigious journal publication.

2. **Media amplification.** Science journalists, who lack the technical
 expertise to evaluate the claim independently, report the announcement as
 fact. Headlines amplify the claim: "Google Achieves Quantum Supremacy."

3. **Capital inflow.** Investors --- venture capitalists, corporate R&D
 budgets, government grant agencies --- allocate capital based on the
 amplified claim. The capital inflow validates the claim retroactively:
 "if sophisticated investors are funding this, it must be real."

4. **Milestone qualification.** Independent researchers --- typically
 academic groups without access to the proprietary hardware --- publish
 analyses that qualify, contextualize, or refute the original claim:
 "the classical simulation was not optimized," "the problem has no
 commercial relevance," "the result does not generalize."

5. **Institutional irrelevance of qualification.** The qualification
 arrives too late to affect the capital allocation. The money has been
 deployed. The press releases have been written. The academic papers
 have been published. The qualification circulates within the academic
 community but does not reach investors, journalists, or policymakers.
 The narrative has moved on to the next milestone.

6. **Milestone creep.** The next milestone is announced, further in the
 future and more ambitious than the last, restarting the cycle.

This cycle --- which we term the **Narrative Production Function (NPF)** --- 
operates on a timescale of months (announcement to capital inflow) while
independent verification operates on a timescale of years. The NPF is
structurally faster than verification, which means capital allocation is
always ahead of truth. This is not a failure of individual actors. It is
a structural feature of the information environment.

## 2.3 The Prestige Cascade

The NPF is reinforced by a prestige cascade within the academic community.
Publication in *Nature* or *Science* confers institutional prestige on the
authors, their departments, and their universities. This prestige translates
into funding, hiring, and promotion --- incentives that operate independently
of the long-term replicability of the published result.

A quantum computing claim that appears in *Nature* and is subsequently
qualified or refuted does not typically result in retraction. The authors
retain the publication, the citation count, and the institutional prestige.
The qualification appears in a lower-tier journal, reaches a smaller
audience, and does not affect the authors' careers.

The prestige cascade creates a **publication lottery:** the expected value
of publishing an ambitious claim --- even one that may not survive independent
scrutiny --- exceeds the expected value of publishing a careful, qualified
result. The rational academic, optimizing for career advancement, will
produce ambitious claims. The institutions that employ them will celebrate
those claims. The journals that publish them will benefit from the attention
they generate. The qualification and correction will be someone else's
problem.

## 2.4 The Regulatory Vacuum

Quantum computing claims are made in an essentially unregulated environment.
There is no equivalent of the FDA --- an agency with the authority to require
evidence of efficacy and safety before a product can be marketed. There is
no equivalent of the SEC --- an agency with the authority to penalize
materially misleading statements to investors. There is no equivalent of
the NTSB --- an agency that investigates failures and publishes findings
that affect future practice.

The regulatory vacuum is not an accident. It reflects a deliberate policy
choice: "innovation" is prioritized over "consumer protection." The
assumption is that the market will sort out which claims are valid and which
are not --- that investors will perform due diligence, that journalists will
exercise skepticism, that the academic community will self-correct.

The evidence from two decades of quantum computing suggests that none of
these mechanisms are sufficient. The market does not sort; it amplifies.
Investors do not perform due diligence; they perform pattern-matching on
narrative features ("PhD founders," "Nature paper," "DARPA grant").
Journalists do not exercise skepticism; they amplify press releases. The
academic community does self-correct --- but on a timescale that is
structurally irrelevant to capital allocation.

# 3. Venture Capital and Deep Technology: A Structural Mismatch

## 3.1 The Fund Lifecycle Problem

Venture capital funds have a typical lifetime of 10 years: 3-5 years of
deployment, 5-7 years of harvesting. The fund must return capital to
limited partners within this window. This means that any investment must
plausibly produce liquidity (IPO, acquisition) within 7-10 years of the
initial investment.

Quantum computing --- even under the most optimistic scenarios --- does not
fit this timeline:

- **Hardware companies** (IBM, Google, Rigetti, IonQ, PsiQuantum): The
 development timeline for a fault-tolerant quantum computer of commercially
 useful scale is --- by the industry's own roadmaps --- 10-15 years from 2026.
 This means 20-25 years from the initial venture investments (circa 2015-2020).
 No VC fund has a 25-year horizon.

- **Software companies** (Zapata, QC Ware, 1QBit): The market for quantum
 software does not exist because the hardware does not exist. Selling
 "quantum-inspired" classical algorithms to enterprises is a consulting
 business, not a software business. The margins and growth rates of
 consulting businesses do not justify venture-scale returns.

- **SaaS plays** (quantum cloud access): IBM, Amazon, and Microsoft offer
 quantum computing as a cloud service. The revenue is negligible because
 the computational value is negligible. This is a marketing expense for
 the cloud providers, not a revenue-generating business.

The structural mismatch between VC timelines and quantum computing development
timelines means that VC-funded quantum computing companies must either:

1. **Go public before they have revenue** --- as Rigetti, IonQ, and D-Wave
 did via SPAC mergers. This transfers the risk from sophisticated
 venture investors to retail investors who cannot evaluate the technology.

2. **Pivot to a different business model** --- as many "quantum software"
 companies have done, becoming classical AI/optimization consultancies.

3. **Perpetually raise more capital** --- extending the timeline beyond the
 original fund's horizon through new funds, strategic investors, and
 government grants.

Option 1 is the most common and the most damaging: it creates publicly traded
companies with no revenue, no product, and no plausible path to either, whose
valuation is sustained by narrative rather than by fundamentals.

## 3.2 The Information Asymmetry Problem

Venture capitalists --- with rare exceptions --- cannot evaluate quantum
computing claims independently. They rely on:

- The prestige of the founding team (PhD from MIT, former IBM Quantum
 researcher).
- The prestige of the publication venue (*Nature*, *Science*, *Physical
 Review Letters*).
- The presence of other prestigious investors (if Sequoia or Andreessen
 Horowitz invested, it must be real).
- The narrative coherence of the pitch (does the story make sense to
 someone who does not understand quantum mechanics?).

None of these signals reliably predict technological success. They are
all proxies for prestige --- and prestige, in quantum computing, is
correlated with narrative production, not with computational output.

The information asymmetry between quantum computing entrepreneurs and
their investors is not just large --- it is essentially unbridgeable. A
VC partner with an MBA and an undergraduate engineering degree cannot,
in a 30-minute pitch meeting, evaluate whether a company's claims about
qubit coherence times, gate fidelities, and error-correction thresholds
are credible. They must rely on heuristics. And those heuristics --- 
prestige, affiliation, narrative coherence --- select for the best
storytellers, not the best physicists.

## 3.3 The Adverse Selection Cascade

The information asymmetry creates an adverse selection problem: the
entrepreneurs most likely to raise venture capital are not the ones most
likely to build a working quantum computer, but the ones most skilled at
navigating the prestige-heuristic evaluation process.

This selects for:

- Founders who are comfortable making ambitious claims without
 falsification criteria.
- Founders who have prestigious affiliations (which they may have
 acquired through the same narrative-production skills).
- Founders who can construct a compelling narrative that appeals to
 investors' pattern-matching heuristics.

Over time, the pool of VC-funded quantum computing entrepreneurs is
enriched for narrative skill and depleted for technical caution. The
adverse selection cascade ensures that the companies that raise the
most capital are the ones least likely to deliver on their claims --- 
because delivering on claims requires acknowledging uncertainty,
qualifying timelines, and stating falsification criteria, all of which
are penalized in the VC fundraising environment.

# 4. The Role of Government: What Works and What Doesn't

## 4.1 DARPA: The Gold Standard

The Defense Advanced Research Projects Agency (DARPA) is widely --- and
correctly --- regarded as the most successful government research funding
agency in history. Its achievements include the internet (ARPANET), GPS,
stealth technology, and the mRNA vaccine platform. DARPA's success is not
accidental. It is a product of specific institutional design features:

- **Program managers with technical expertise and bounded terms.**
 DARPA program managers are typically active researchers who serve for
 3-5 years. They have the expertise to evaluate proposals technically
 and the limited tenure to avoid capture by the programs they fund.

- **Falsifiable milestones with go/no-go decisions.** DARPA programs are
 structured around concrete, time-bound milestones. Programs that fail
 to meet milestones are terminated --- not extended, not refunded, not
 rebranded. This creates a hard selection pressure for honest evaluation.

- **Independence from commercial pressure.** DARPA funds research that is
 "DARPA-hard" --- too risky for industry, too applied for basic science.
 Because DARPA does not seek commercial returns, it can fund research
 that a venture capitalist would reject.

- **Willingness to terminate.** DARPA kills programs. This is its most
 important feature and the one most absent from other funding
 institutions. The willingness to terminate creates the incentive for
 honest evaluation: if you know your program will be killed when it
 fails, you have an incentive to define failure clearly and to report
 results honestly.

**Why DARPA has not prevented the quantum computing bubble:** DARPA's
quantum computing investments are small relative to the total --- perhaps
$200-300 million over two decades, compared to $35 billion globally.
DARPA can fund rigorous research programs, but it cannot counterbalance
the enormous capital flows from venture capital, corporate R&D, and
international government programs that lack DARPA's institutional
discipline.

## 4.2 The NSF and DOE: Dilution Without Discipline

The National Science Foundation (NSF) and Department of Energy (DOE) fund
quantum computing research at a larger scale than DARPA --- approximately
$1-2 billion cumulatively through the National Quantum Initiative and
related programs. These agencies operate on a different model:

- **Peer review by the same community being funded.** NSF and DOE proposals
 are reviewed by panels of academic researchers --- the same researchers
 who submit proposals. This creates a reciprocity dynamic: if I approve
 your proposal, you'll approve mine. The result is a high approval rate
 and low discrimination between proposals of varying quality.

- **No mechanism for post-award evaluation.** NSF and DOE grants are
 evaluated based on the proposal, not on the results. Once a grant is
 awarded, there is no systematic mechanism for determining whether the
 research delivered on its promises. Failed grants do not affect future
 funding. Successful grants are not distinguished from unsuccessful ones.

- **Diffuse responsibility.** The NSF funds thousands of individual
 investigators across hundreds of institutions. No single program
 manager is responsible for the overall portfolio's performance.
 Diffusion of responsibility eliminates the incentive for honest
 evaluation.

The result is that NSF and DOE funding for quantum computing has
sustained a large academic research community without producing
commercially relevant computational output. This is not a failure of
individual researchers --- many of whom produce excellent science. It is
a failure of the institutional design, which does not aggregate
individual scientific contributions into a coherent program with
falsifiable milestones.

## 4.3 International Comparison: The Chinese Model

China is the world's largest public investor in quantum computing, with
estimated cumulative investment of $10-15 billion through national and
provincial programs. The Chinese model has different strengths and
weaknesses:

**Strengths:**
- Centralized coordination enables rapid scaling of successful approaches.
- Long time horizons (15-20 year national strategies) avoid the VC
 timeline mismatch.
- Integration of research and manufacturing in state-owned enterprises
 enables technology transfer that is difficult in market economies.

**Weaknesses:**
- Centralized coordination amplifies errors: if the central authority
 backs the wrong technical approach, the entire national program follows.
- Absence of independent verification and public criticism: Chinese
 quantum computing claims are not subject to the same adversarial
 scrutiny as Western claims, making it difficult to distinguish genuine
 progress from narrative production.
- Political pressure to demonstrate success: program managers have
 incentives to report progress that may not reflect technical reality.

The Chinese model illustrates that government dominance of quantum
computing R&D does not automatically solve the incentive problem. It
changes the nature of the problem --- from market-driven narrative
production to politically-driven narrative production --- but does not
eliminate it.

# 5. Five Institutional Reforms

We propose five institutional reforms designed to align the incentive
structure of post-classical computing R&D with the goal of producing
actual computational output, not narrative assets.

## 5.1 Reform 1: An Advanced Computing Projects Agency (ACPA)

**What:** A new government agency modeled on DARPA but focused exclusively
on post-classical computing --- quantum, thermodynamic, neuromorphic,
optical, reversible. The ACPA would have DARPA's institutional features:
expert program managers with bounded terms, falsifiable milestones with
go/no-go decisions, independence from commercial pressure, and a
willingness to terminate failed programs.

**Why DARPA itself is insufficient:** DARPA's mandate spans all of
defense technology. Quantum computing competes for attention with
hypersonics, AI, biotech, and space. A dedicated agency would ensure
sustained focus and expertise.

**Budget:** We estimate that an ACPA with an annual budget of $500
million --- roughly the size of DARPA's information technology office --- 
could fund a diversified portfolio of post-classical computing research
at a scale sufficient to explore the entire Problem-Substrate Mapping
from Phase IV.

**Key design features:**
- Program managers serve 3-5 year terms and are recruited from active
 researchers in relevant fields. They cannot serve consecutive terms.
- Every program has written, time-bound, falsifiable milestones.
- Programs that miss milestones are terminated. There is no appeal.
- All results --- positive and negative --- are published within 6 months
 of program completion. Negative results are celebrated as valuable
 contributions to knowledge.
- The ACPA does not commercialize technology. It funds research to the
 point of technology readiness, then transitions to industry or other
 government agencies for deployment.

## 5.2 Reform 2: Mandatory Independent Verification

**What:** Any claim of quantum computational advantage above a materiality
threshold --- defined as (a) claimed commercial relevance, or (b) funding
above $10 million from government sources, or (c) public claims of
"quantum supremacy" or "quantum advantage" --- must be independently
verified by a qualified third party that does not have a financial
interest in the outcome.

**Independent verification protocol:**
1. The claimant provides the independent verifier with access to the
 hardware (or, if hardware access is not feasible, with sufficient data
 and simulation specifications to reproduce the result classically).
2. The independent verifier conducts their own analysis and publishes
 their findings --- including any qualifications, limitations, or
 refutations --- within 6 months.
3. The independent verification report is linked to the original claim
 in a public registry.
4. Claims that are not submitted for independent verification within
 12 months of the initial announcement are flagged as "unverified" in
 the registry.

**Funding:** Independent verification should be funded by a small levy
on quantum computing research grants and investments (0.5% of total
funding), pooled into an Independent Verification Fund administered by
the ACPA or an equivalent institution.

**Enforcement:** For publicly funded research, compliance with independent
verification is a condition of funding. For privately funded research,
non-compliance is noted in the public registry. The market --- investors,
customers, partners --- can then decide whether to engage with unverified
claims.

## 5.3 Reform 3: Structural Separation of Hardware and Software

**What:** Break the vertical integration of quantum computing companies,
which control hardware, software, and cloud access. Require that any
company receiving above $50 million in government quantum computing
funding divest either its hardware or its software/services division.

**Rationale:** Vertical integration creates a conflict of interest: the
company that builds the hardware also evaluates the hardware's
performance, develops the software that runs on it, and markets the
cloud service that sells access to it. There is no point in this chain
where independent evaluation can intervene. Structural separation creates
a market for independent evaluation and benchmarking.

**Precedent:** The structural separation of telecommunications (AT&T
breakup, 1984), banking (Glass-Steagall, 1933), and energy (PUHCA,
1935) demonstrates that structural separation can create competitive
markets where vertical integration produced stagnation and rent-seeking.

**Implementation:** Existing companies would have 3 years to divest.
New companies would be required to choose hardware or software from
incorporation. The threshold ($50 million in government funding) ensures
that small startups are not burdened while the dominant players are
restructured.

## 5.4 Reform 4: Joules-Per-Solution Procurement

**What:** All government procurement of computational services --- including
quantum computing --- must evaluate bids on a joules-per-solution basis for
the specific problem being procured. "Joules per solution" means the
total wall-plug energy consumed to deliver a verified, correct answer to
the specified problem at the specified scale.

**Rationale:** The current procurement model allows quantum computing
companies to sell "access" to hardware without demonstrating that the
hardware solves any commercially relevant problem. A joules-per-solution
requirement transforms procurement from a faith-based to an
evidence-based process.

**Implementation:** For any computational procurement above $1 million,
the procuring agency must:
1. Specify the problem class, scale, and accuracy requirement.
2. Solicit bids that state the total energy consumption to deliver the
 solution.
3. Evaluate bids based on total cost (energy + hardware + personnel),
 with energy weighted at the agency's internal carbon price.
4. Publish the winning bid and its joules-per-solution for public review.

## 5.5 Reform 5: A Public Registry of Computational Claims

**What:** A public, searchable, permanent registry of all claims of
computational advantage or milestone achievement in post-classical
computing, with mandatory time-bound falsification criteria.

**Registry fields:**
- Claim ID and date of announcement.
- Claimant institution and funding sources.
- Specific technical claim (not "quantum advantage" but "solving
 problem X of scale Y using Z joules in W seconds").
- Falsification criteria: what observation would constitute failure of
 the claim? By what date?
- Independent verification status (verified / refuted / qualified /
 unverified).
- Link to independent verification report.

**Effect:** The registry creates a permanent, public record that is
difficult to ignore. A company that claims "quantum advantage" in 2025
and fails to demonstrate it by 2027 has a permanent entry in the
registry noting the failure. This creates a reputational cost for failed
claims that currently does not exist.

# 6. Objections and Implementation

## 6.1 "This Will Kill Innovation"

**Objection:** Mandatory independent verification, structural separation,
and joules-per-solution procurement will stifle innovation by imposing
bureaucratic burdens on nimble startups.

**Response:** The current system is not producing innovation. It is
producing narrative assets. $35 billion over 20 years with zero
commercially viable output is not "innovation." It is capital destruction
dressed in the language of innovation.

Moreover, the reforms are designed to be light-touch for early-stage
research and progressive for later-stage commercialization. The
independent verification requirement applies only above a materiality
threshold. The structural separation applies only above $50 million in
government funding. The joules-per-solution procurement applies only above
$1 million in procurement value. A two-person startup in a university lab
would not be affected.

## 6.2 "The Market Will Sort It Out"

**Objection:** The market --- investors, customers, the academic community --- 
will eventually distinguish genuine progress from narrative production.
Government intervention is unnecessary and potentially harmful.

**Response:** The market has had 20 years and $35 billion. It has not
sorted it out. The information asymmetry between quantum computing
entrepreneurs and investors is structural, not temporary. The prestige
cascade in academic publishing is self-reinforcing. The regulatory
vacuum is deliberate. None of these features will self-correct.

The appropriate analogy is not "innovation" but "financial regulation."
Securities markets required the SEC because information asymmetry between
issuers and investors is structural. Drug markets required the FDA because
information asymmetry between manufacturers and patients is structural.
Quantum computing requires similar institutional infrastructure because
information asymmetry between claimants and funders is structural.

## 6.3 "International Competition"

**Objection:** If the United States imposes these reforms unilaterally,
China and Europe will gain a competitive advantage by operating without
regulatory burden.

**Response:** If the reforms prevent capital from flowing to narrative
production and redirect it toward actual computation, the United States
will GAIN a competitive advantage --- because its capital will be
productively deployed while competitors' capital will be consumed by
the narrative production function.

Moreover, the reforms should be pursued through international coordination
 --- through the OECD, the G7, and bilateral science and technology
agreements. The quantum computing bubble is a global phenomenon, and
its correction should be global.

# 7. Conclusion: Institutional Honesty

The first four papers in this series have argued that quantum computing's
failure is epistemic, that alternatives exist, that physical limits matter,
and that a diversified investment portfolio is the rational response. This
paper has argued that none of these insights will be acted upon without
institutional reform --- because the current institutional structure
systematically rewards narrative production over computational output.

The five reforms we propose --- an Advanced Computing Projects Agency,
mandatory independent verification, structural separation of hardware and
software, joules-per-solution procurement, and a public registry of
computational claims --- are designed to realign the incentive structure of
post-classical computing with the goal of producing actual computation, not
just press releases, patents, and valuations.

These reforms are not radical. They are modeled on institutions that already
exist and have proven effective: DARPA, the FDA, the SEC, the NIH clinical
trials registry. What is radical is only the proposal to *apply* these
institutional forms to a domain that has, so far, been exempt from the
ordinary requirements of evidence, verification, and accountability.

The alternative to institutional reform is not the status quo. The status
quo is a machine for converting public and private capital into narrative
assets. The alternative to reform is the continuation of this machine --- 
another $35 billion, another two decades, another round of "quantum
supremacy" announcements followed by quiet qualifications. The laws of
physics do not negotiate. Neither should the institutions that fund the
effort to understand them.

---

**References**

- @Mazzucato2013: M. Mazzucato, "The Entrepreneurial State: Debunking Public vs. Private Sector Myths" (Anthem Press, 2013).
- @Lerner2009: J. Lerner, "Boulevard of Broken Dreams: Why Public Efforts to Boost Entrepreneurship and Venture Capital Have Failed" (Princeton, 2009).
- @Ioannidis2005: J. P. A. Ioannidis, "Why Most Published Research Findings Are False," PLoS Med 2, e124 (2005).
- @Nosek2015: B. A. Nosek et al., "Estimating the Reproducibility of Psychological Science," Science 349, aac4716 (2015).
- @Hanson1995: R. Hanson, "Could Gambling Save Science? Encouraging an Honest Consensus," Soc. Epistemol. 9, 3 (1995).
- @Azoulay2019: P. Azoulay et al., "Funding Breakthrough Research: The DARPA Model," Nature 572, 294 (2019).
- @Gompers2016: P. Gompers et al., "Venture Capital, Reputation, and the Decision to Go Public," J. Financ. Econ. 119, 249 (2016).

## Prior Work and Related Literature

The earlier formal work on epistemic incentives established the analytic vocabulary this paper uses to explain the quantum computing bubble. In [Institutionalized Predictive Jeopardy: An Evolutionary-Game Demarcation Criterion for Knowledge Systems](https://papers.qnfo.org/papers/institutionalized-predictive-jeopardy-an-evolutionary-game-demarcation-criterion), I showed that institutional knowledge systems lack a formal criterion for distinguishing claims that carry prospective falsification risk from claims fitted to evidence after the fact, and modeled the choice as an evolutionary game between a falsifiable strategy and a post-hoc strategy. That paper derived the accuracy threshold \(p^{*}=(s+c)/(b+c)\), demonstrated that under a baseline incentive configuration post-hoc fitting dominates even for a forecaster who is right 60% of the time, and showed that a pre-registration-style reform raising the confirmed-prediction reward reverses the equilibrium. It also derived an antifragility condition under which registered failures raise system reliability and a reform timescale for the transition between equilibria. [Institutionalized Unfalsifiability as an Evolutionarily Stable Strategy in Scientific Incentive Landscapes](https://papers.qnfo.org/papers/institutionalized-unfalsifiability-as-an-evolutionarily-stable-strategy-in-scien) reached the same threshold and flip-point result from a complementary direction, treating unfalsifiability as an evolutionarily stable strategy and anchoring the payoff parameters in concrete numeric statements from the scientific literature. That paper identified the policy lever that follows from the model: raising the confirmed-prediction reward can make falsifiable practice


## Changelog

- v1.1.0: Added a Prior Work and Related Literature section that places this paper among 2 related QNFO papers.

