# Position: Audited Ledgers as a Publication Unit for AI-Accelerated Science

**Submitted to AI for Meta-Science workshop (NeurIPS 2026)** — position track, single-blind (previously published work). Non-archival.

**Abstract.** Between December 1, 2025 and August 20, 2026, a solo researcher ran a personal research program on $1,032.08 of API credits: 50.11 billion tokens, 323,381 requests, 911 versioned records, a cost ratio of roughly sixty to one hundred ten times below a fully loaded postdoc for the same window. The ledger is public, primary-source, and failure-inclusive; the efficiency claim is explicitly supply-side, with a pre-registered demand-side kill criterion (zero external traction by August 2028 renders the claim hollow). This position paper argues from that field report that the scientific process is calibrated for scarcity and breaks at AI scale in three specific places — the unit of publication, the unit of review, and the incentive structure — and proposes three positions in response: audited primary-source ledgers as a first-class publication unit; review adapted to AI-scale output through verification-first and adversarial-sampling mechanisms; and incentives that price honesty, making falsifiability statements and failure disclosures part of the artifact rather than optional extras. The positions are stated with their falsifiers.

## 1. The field report

A research program spanning ultrametric physics, information theory, laws of form, quantum error correction, and the epistemology of AI-assisted research ran for 263 days (December 1, 2025 – August 20, 2026) on **$1,032.08** of DeepSeek API credits, with no lab, no grant, and no institutional budget. The verified ledger, from the platform's own usage exports and public registries:

- **50.11 billion tokens** (49.86B input + 248.4M output), **323,381 API requests** across 184 billed days — a mean of $5.61 per billed day
- **96.4% of input tokens were cache hits** (48.08B of 49.86B): the blended cost was **$20.60 per billion tokens**, and the cache arithmetic — $0.0036 per million for a hit versus $0.435 for a miss — is the economic engine
- Output inventory: **911 versioned Zenodo records** (~880 distinct works, 877 on ORCID), **1,646 paper nodes** in an internal knowledge graph, **114 GitHub repositories** (109 created in-window), **20 production Cloudflare Workers**, and four live public surfaces
- **Cost ratio: ~60× to ~110×** against a fully loaded postdoc for the same 8.7-month window ($65,000–$112,000); the ~880 registered works cost **about $1.18 each in machine time**
- Volume, flagged as such: 248.4M output tokens ≈ 186 million words of raw generation (mostly intermediate material — code, metadata, discarded drafts — not polished prose); genuinely new text read was 1.79B tokens

Two regimes are visible: December through March was single-threaded conversation (about $21 across four months); April onward was the agentic regime — subagents, parallel exploration, adversarial review, prompt caching as the economic engine — peaking at $440.16 in July (124.3K requests, one every ~11 seconds across a 12-hour working day).

Nothing in the ledger is external validation. Citations, peer acceptance, and correspondence were not purchasable and remain pending. The program's own rules require traction signals to be external only: the efficiency claim is a supply-side claim awaiting a demand-side verdict.

## 2. What the numbers mean

**Production became cheap; judgment became the entire job.** The machine drafts, codes, compiles, deploys, and checks in bulk. What it cannot do is decide what is true, what matters, and what deserves to survive. Every serious session ends the same way: a human holds a candidate output and makes a kill decision. The program's real inventions were instruments of that decision — citation audits that verify every reference against live registries, adversarial reviewers instructed to attack, publication gates that block known failure modes.

**AI errors are systematic, not random — so defenses must be gates, not intentions.** Across nine months the same failure classes recurred: fabricated citations (a hallucinated author list is a research-integrity violation, and it happened), internal reference keys leaking into published bodies, character-encoding corruption propagating from a single slip into PDFs and databases, phantom DOIs, drifting configuration files, files written to the wrong storage bucket. Each class, once seen, became a hard gate: scan before commit, verify before cite, check before publish. Intentions did not work; gates worked.

**Publish, then audit — every time.** The program's standing rule is that every published artifact receives an adversarial audit after publication. The first audit of the flagship pair surfaced 13 hard findings — unresolvable citations, title mismatches, missing deposits — and each finding became the next cycle's remediation item. Publication is a checkpoint in a loop, never an endpoint.

**Most failures were self-inflicted.** When the email pipeline failed on every address of one domain while ten sibling domains worked, the cause was the platform's own routing rules added days earlier; when a publication mirror landed in the wrong bucket, it was the script. The single most useful diagnostic habit: ask "what did I change?" before asking "is the platform down?"

**Architecture is what makes tokens cheap.** Fifty billion tokens for a thousand dollars is not a pricing accident; it is an engineering result — byte-identical prompt stores, canonical registries, a knowledge graph that makes context retrievable instead of re-explained, bounded subagents that demand evidence. The discipline is unglamorous and it is the entire margin.

## 3. The problem: publication and review are calibrated for scarcity

The scientific process assumes scarcity in three places, and each assumption breaks at AI scale.

**The unit of publication is the finished paper.** A claim becomes citable only after it has been shaped into a standalone manuscript. At a production rate of ~880 works in 263 days, the "finish and submit" pipeline becomes the bottleneck — not because the work is missing, but because the artifact class (a claim plus its receipts) has no canonical home between the raw ledger and the polished paper. The program's methodologically central results were themselves published as records: the *Universal Ignorance Audit* (10.5281/zenodo.21901984) and *Knowing What We Do Not Know* (10.5281/zenodo.21901983) — fifteen-question instruments for auditing what is not known — alongside a public essay, *Tyranny of the ±1* (10.5281/zenodo.21939595), that turned the program's red-team audits into method. But the ledger itself — the primary-source record that makes all of it checkable — is not an artifact the current system knows how to cite, review, or reward.

**The unit of review is the submitted manuscript.** Peer review as currently practiced reads each submission as a finished argument. When outputs arrive at volume, either the review queue collapses or the reviews become rubber stamps. Neither outcome serves the ecosystem: the first produces fake scarcity, the second fake quality.

**The incentive is novelty, priced per artifact.** A system that rewards "new results" without requiring "checkable results" rewards production over audit. The field report's most valuable artifacts — the ignorance audits, the failure history, the kill criterion — are precisely the artifacts a novelty-only incentive structure would never price.

## 4. Position one: audited ledgers as a publication unit

The first position: **the audited primary-source ledger should be a first-class publication unit**, with the same claim to citability as a paper, and a defined review treatment.

A ledger-unit publication consists of: (a) a falsifiable claim; (b) the primary-source receipts for every figure (usage exports, registry queries, live API checks — the essay's provenance appendix is the template, a per-claim table mapping every number to its source); (c) a documented failure history; and (d) a pre-registered kill criterion. This is not a substitute for the paper; it is the substrate that makes the paper's claims checkable. The *Universal Ignorance Audit* already provides the method: a research system that only produced papers would be a paper mill; one that produces an audited map of its own unknowns is an instrument.

Why this position survives scrutiny: the ledger converts "trust me" into "check me." Every number in the field report can be recomputed from public sources in an afternoon; the provenance table says exactly how. Falsifiability is only possible when the claim ships with its receipts.

## 5. Position two: review adapted to AI-scale output

The second position: **review of AI-scale output should be verification-first and adversarial by design, not manuscript-shaped.**

Concretely: (a) *verification-first review* — the primary reviewer obligation is recomputing or re-checking the artifact's claims against its receipts, not refereeing prose; (b) *adversarial sampling* — at volume, review shifts from "every artifact" to "every artifact class plus pre-registered adversarial samples," with the sample drawn by the reviewer, not the author; (c) *publish-then-audit as an institutional mechanism* — publication as a checkpoint in a loop (the program's own standing rule), with post-publication audits feeding remediation rather than retraction theater; (d) *rigorous negative results and replications as first-class submissions* — the workshop's own welcome, and the natural complement to a production regime that otherwise only surfaces positives.

The honest objection: automated or sampled review can be gamed. Conceded — every gate can be gamed; the defense is adversarial verification plus external traction, not secrecy. A review regime that checks receipts and samples adversarially is strictly more game-resistant than one that reads polished prose, because the receipts are public and the sampling is the reviewer's.

## 6. Position three: incentives that price honesty

The third position: **the incentive structure should price honesty — falsifiability statements, cost disclosures, and failure disclosures — as part of the artifact.**

A paper that states its kill criterion in advance is a prediction; one that does not is a retrodiction wearing a lab coat. A program that publishes its 13 hard findings against itself is providing the epistemic public good that novelty-counting cannot see. The field report's falsifiable statement is registered in advance: **if, by August 2028, this corpus has produced no external citations, no substantive correspondence, and no venue acceptance, then the efficiency demonstrated was hollow — volume without a reader.** That sentence is the model: supply-side claims should ship with their demand-side verdicts attached.

Serious engagement with the strongest alternatives:

- *"Scale is not quality; ledgers are not peer review."* Conceded in full. The ledger is a supply-side artifact; the kill criterion is the admission that demand-side validation is outstanding. The position is not "ledgers replace review" but "ledgers make review possible at scale."
- *"This is n=1 self-report."* Conceded. The field report is an existence proof and a template, not a controlled study. That is precisely why the provenance appendix and the public receipts matter: n=1 with checkable receipts is the honest unit; n=1 with uncheckable prose is a testimonial.
- *"Cost ratios compare a machine's generation to a human's full effort."* Partly conceded: the human's judgment is the irreplaceable, unpriced input — the correct sentence is not "an AI did the work of a lab" but "one researcher's judgment, multiplied by a machine that never sleeps, at the cost of a laptop." The comparison is of the *machinery* line item, stated as such.

## 7. What would falsify this position

The position is a prediction, not a retrodiction. Three falsifiers:

1. **The ledger-unit fails on demand:** if by August 2028 the corpus has produced no external citations, no substantive correspondence, and no venue acceptance, the efficiency claim is hollow — volume without a reader — and the ledger-unit position loses its central exhibit.
2. **The units don't generalize:** if no second program adopts the ledger-unit, verification-first review, or kill-criterion practice within the same window, the positions remain a single-researcher idiosyncrasy rather than an institutional template.
3. **The incentives backfire:** if cost/failure disclosure measurably *reduces* artifact quality or candor (e.g., authors game their kill criteria), the honesty-pricing claim fails and should be abandoned.

## 8. AI-disclosure statement

This position paper was drafted with AI assistance under the author's direction, consistent with the workshop's encouragement to disclose the role of AI systems in producing submissions. Every figure traces to a primary record — the platform's usage exports and the public registries (Zenodo, ORCID, GitHub, the internal knowledge graph, the Cloudflare account) — and the provenance table in the underlying essay states each source. This paper is itself an artifact of the program it describes; the ledger it cites is the receipt.

## References

- Quni-Gudzinas, R. B. *The $1,032 Research Program: What Fifty Billion Tokens Taught Me About AI-Accelerated Science*. Zenodo, 10.5281/zenodo.22028851 (2026).
- Quni-Gudzinas, R. B. *The Universal Ignorance Audit: A Fifteen-Question Method for Systematic Inquiry into the Structure of Not-Knowing*. Zenodo, 10.5281/zenodo.21901984 (2026).
- Quni-Gudzinas, R. B. *Knowing What We Do Not Know: Ignorance Auditing, AI-Generation Detection, and the Epistemic Lessons of an AI-Assisted Research Pipeline*. Zenodo, 10.5281/zenodo.21901983 (2026).
- Quni-Gudzinas, R. B. *Tyranny of the ±1*. Zenodo, 10.5281/zenodo.21939595 (2026).
- AI for Meta-Science Workshop, NeurIPS 2026, Call for Papers. https://ai4metascience.org/cfp.html (verified 2026-08-20).
