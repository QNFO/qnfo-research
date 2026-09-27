---
title: "Operating the Quniverse Fleet: Objectives, Successes, Failures, and Roadmap of an Autonomous Cloud Research System"
author: "Rowan Brad Quni-Gudzinas"
date: 2026-09-27
abstract: |
  The Quniverse is a self-maintaining research and publishing system running on
  the Cloudflare Workers platform: thirty-six deployed workers (thirty-eight at the session's
  start) sharing ten
  SQL databases, eight vector indexes, nineteen object-storage buckets, and a
  metered model gateway, operated by an autonomous agent under human direction,
  with no code written by the human operator. This paper answers four
  questions in order: what the system actually is; what it was built to do;
  where it has succeeded and where it has failed across roughly a year of
  operation; and what the roadmap is. The core findings: the system reliably
  produces and publishes research (905 paper records, 438 published, 53
  publication events in the last 30 days, 25,408 aggregate Zenodo views across
  298 deposited records), and its operating discipline - a versioned
  instruction set that encodes every observed failure as an enforceable gate -
  is its most durable asset; but its autonomy is incomplete (composite
  autonomy score 3.6/5 in the fleet's own assessment), its maintenance burden
  has repeatedly exceeded its self-healing capacity, and a September 2026
  consolidation wave that shrank the fleet from 57 to 38 workers retired at
  least one load-bearing function (social distribution) before it was
  restored. The roadmap is consolidation toward a smaller, more autonomous
  core: automated optimization, cost-routed model access, metric-integrity
  governance, and restoration of the publication-to-audience funnel. A
  forty-item failure ledger with root causes and remedies is included, because
  the system's most transferable output is not its code but its accumulated
  record of what breaks and why.
keywords:
  - autonomous systems
  - cloud infrastructure
  - self-healing systems
  - research infrastructure
  - operational lessons
---

# 1. What this system is

1.1 The Quniverse is a fleet of Cloudflare Workers operating inside a single
Cloudflare account. At the time of writing the account holds 36 deployed
worker scripts, 10 D1 (SQLite) databases totalling ~304 MB, 8 Vectorize
semantic indexes (the largest holding 34,657 research-document vectors), 19
R2 object-storage buckets, 4 KV namespaces, and 7 web-analytics sites. Model
access runs through an AI gateway with a spend cap of $150 per 30 days and
free-tier model fallbacks. The fleet's own census table (service registry)
agrees exactly with the deployed scripts at the time of writing: 36 live
rows against 36 live scripts, zero drift. The count moved from 38 to 36
during the writing session as a consolidation wave retired two services;
the census-drift class is recorded in Section 4.3.

1.2 The workers divide into layers. A control plane (one execution endpoint
through which all code and data operations run), a research gateway for
literature and reasoning, a publishing pipeline (paper indexing, revision,
PDF generation, Zenodo deposition), an operations layer (fleet control,
deploy locking, backlog draining, weekly digests), and an outreach layer
(email, calendar intake, social posting). A personal-knowledge twin is
firewalled from the research system. The account additionally runs D1
databases for research content, a knowledge graph, audit records, outreach,
and personal data, with vector search over research, notes, tasks, handoffs,
and query logs.

1.3 The human role is direction and ratification. The operator writes no
code: every worker, script, guard, and database is written and maintained by
the agent itself, under a versioned operating instruction set that has
accumulated more than twenty revisions, each adding constraints derived from
a specific, observed failure. This framing requires an honest correction to
the phrase "no-code": the system is not code-free - it is roughly a
quarter-million lines of JavaScript and Python - it is operator-code-free.
"No-code" describes the human's interface, not the system's substrate. The
agent runtime (a desktop client) and the Cloudflare platform are third-party
dependencies; the fleet is not literally no software.

1.4 The self-improvement loop is the system's defining property. Operations
follow a closed cycle: detect a defect, act to repair it, verify the repair,
then codify the failure class as a standing gate so it cannot recur
silently. The fleet maintains 1,889 recorded self-heal actions and 1,264
handoff records. Kaizen cycles distill each week's failures into durable
lessons, and every close-out of a task is itself audited and recorded, so
the audit trail is re-auditable.

1.5 Two design commitments shape everything else. First, every recurring
function runs in the cloud: the local machine is a thin front-end and a
credential vault, not an execution substrate. Second, every artifact is a
signal with an assigned evidential weight, and claims are tracked with
explicit evidence, confidence, and failure modes - the fleet's own writing
is subject to the same falsifiability discipline it applies to research.

# 2. Objectives

2.1 The ratified mission statement: every recurring function runs in the
cloud; the fleet operates, heals, audits, improves, publishes, and promotes
itself; the human role is as narrow as possible. The fleet tracks its own
progress against this with periodic autonomy scores under two frameworks
(viable-system-model and observe-orient-decide-act).

2.2 The objective function is explicit and weighted: a Self-Autonomy Index
combining 0.20 autonomy + 0.15 thinking + 0.15 decision + 0.15
self-improvement + 0.10 reliability + 0.10 integration + 0.10 external
impact. The most recent assessment (2026-09-24) scores the composite at 3.6
out of 5, with sub-scores of 4.8/5 for "inverted watchmaker" (recurring work
needing a human is approaching zero), 4.5/5 for control, 4.0/5 for
self-healing, and 4.2/5 for observe-orient-decide-act closure. The named
gaps are instructive: coordination is still time-triggered rather than
event-driven, deploy-class changes still take days, and novel failure
classes still require an agent session rather than a scripted repair.

2.3 Cost objectives are capped and metered. The AI gateway bills in cents,
a fact that was once misread by two orders of magnitude; the corrected
understanding is roughly $110/month of model spend against a $150 cap, with
free-tier models first in every routing cascade and a budget-cap fallback
that never terminates work while a free path exists.

2.4 The research objective is open science on the program's own terms: a
body of papers deposited on Zenodo (no journal submissions), a
knowledge-graph layer, and a benchmark program centered on
energy-per-correct-answer for computing substrates. Publications are
versioned: revisions ship as new Zenodo versions, never silent edits.

2.5 A return-on-spend objective ties the total infrastructure plus model
budget to measurable output, with pre-registered survival gates that are
required to be computed from authoritative sources at evaluation time,
never hardcoded.

2.6 The human-facing surfaces are part of the objectives: the owner can
steer the fleet by email (read verbs plus natural-language task passthrough
to the execution agent), and forwarded appointment emails become calendar
entries with reminders. Distribution matters: publications must reach an
audience, so every deposit is required to publicize its canonical page in
public metadata, and social amplification is a standing function.

# 3. What has worked

3.1 Publication throughput. The paper store holds 905 records, 438 with
status published, and 53 publication events in the last 30 days. The Zenodo
presence aggregates to 25,408 views and 13,307 downloads across 298 tracked
records.

3.2 Operating discipline. The instruction set's gate library is the
accumulated memory of the fleet's own failures. Each gate names the
canonical failure that produced it: authentication probes must carry
credentials; deploy locks must use epoch timestamps; cron estimates must not
multiply by 24; billing must be unit-audited before escalation; client-side
fixes must be mirrored in the guards that enforce them; a published body
must be swept for embedded model transcripts. This is the system's most
transferable asset: not the workers, but the practice of converting each
failure into a standing, machine-checked constraint. Twenty-one revisions of
that instruction set exist; each was triggered by a real incident and each
is enforced by scripts that exit non-zero on drift.

3.3 Cost routing. A layered stack - deterministic answers first, cache
second, capability gating third, free-model cascade fourth, paid tiers last
- keeps measured gateway cost near zero for routine traffic: the most recent
gateway log window shows 20 requests at $0.0074 total, with six of seven
model families in the window costing $0. Cost is measured per successful
task by class, not only per token.

3.4 Interface consolidation. After a period of proliferating model
identifiers (nineteen advertised on one endpoint at the worst point), each
AI endpoint now advertises exactly one model (verified live: the control
endpoint advertises ops, the research gateway qnfo, the personal twin
personal), and no endpoint rejects foreign model identifiers - every request resolves to the canonical model.
This removed an entire class of client-configuration failures, including
one where a streaming path silently billed the paid route while the
non-streaming path of the same endpoint used the free route.

3.5 Human-usable control surfaces. The email command surface is live and
exercised, with real traffic (314 sent, 10 replied, and a logged command
history). The email-to-calendar intake worker is deployed and healthy, but
no event email has been forwarded to it yet (zero intake rows), so that
route is built rather than proven; the shared calendar plane itself
carries 65 events, sourced from the personal twin. The intake includes
decline/cancel learning that suppresses reminders for cancelled events.

3.6 Registry-as-truth. The service registry is the single census authority,
reconciled against live deployments; drift is treated as a defect to be
cleared, not a metric to be observed. After the September consolidation the
registry was re-reconciled to the live worker set.

3.7 Self-healing volume. 1,889 self-heal action rows and 1,264 handoff rows
exist in the audit database; the fleet's weekly digest and watchtower run on
cloud crons, and the local machine carries zero enabled recurring jobs.

3.8 Publication integrity repair. When a published paper was found to embed
model transcripts, the remediation shipped as a new Zenodo version with a
content sweep gate added to the publish path - an example of the failure
loop closing, not simply the failure being noticed.

# 4. What has failed

The failures below are documented because each one became a gate. They are
listed honestly because the system's credibility rests on the failures
being as visible as the successes.

## 4.1 The failure ledger

Each entry is a real incident: what broke, why it broke, and what standing
constraint now prevents recurrence. The ledger is grouped by theme.

Theme A - publication integrity.

A1. A published paper shipped with 34 verbatim transcripts of model
conversation embedded in its body, live on the public site for weeks. Root
cause: no content sweep at publish. Remedy: mandatory transcript sweep
before publish; fixes ship as new Zenodo versions, never silent edits.

A2. A Zenodo deposit publicized the canonical site link only in an internal
notes field, so an audience of tens of thousands of record views had no
path to the project's own pages. Root cause: funnel link treated as
metadata noise. Remedy: the canonical link is appended to the public
description and related identifiers of every deposit.

A3. A paper edit was once shipped as a database-only change while the
deposited record stayed stale. Root cause: two copies of one truth. Remedy:
content changes flow through the version pipeline; database and deposit
converge on the same version string.

Theme B - measurement and money.

B1. Gateway billing denominated in cents was read as dollars, escalating a
"cost emergency" roughly 100 times larger than reality and nearly
triggering a pre-registered phase-1 shutdown. Root cause: no units audit.
Remedy: every cost claim requires a units audit against at least two
independent signals before escalation.

B2. A survival-gate metric was hardcoded as an undefined placeholder while a
dashboard rendered a day-over-day change of a rolling window as
"month-over-month growth", producing a false -0.7% where the true 30-day
figure was +410%. Root cause: gate metrics not computed from sources.
Remedy: survival-gate metrics are computed from authoritative sources at
evaluation time; a displayed zero is treated as worse than an explicit
undefined.

B3. A per-day cron estimate multiplied an hourly rate by 24 on an
already-per-day basis, inflating usage 24-fold and producing false
compliance alarms. Root cause: formula applied twice. Remedy: per-day
estimates are re-derived before any compliance breach is reported.

B4. A paid-provider budget cap once terminated work outright while free
models were available. Root cause: fallback designed for errors only, not
for quota exhaustion. Remedy: budget-cap exhaustion degrades to the free
tier; persistent auth errors on the paid path also fall back, while other
client errors stay fatal.

B5. A streaming path on an endpoint billed the paid gateway while the
non-streaming path used free models, so nearly all interactive traffic -
the bulk of usage - paid while the free path sat unused. Root cause: two
code paths, one cost policy missing. Remedy: one cost policy per endpoint,
free-first in both paths.

Theme C - state divergence.

C1. A fix applied to a client store was reverted by the guard that owned
the same state, because the guard still encoded the old value. Root cause:
client and guard as two sources of truth. Remedy: client-state changes are
mirrored into the enforcing guard in the same cycle, then converged, then
re-read.

C2. Guards continued to require model identifiers an endpoint had retired
after consolidation, manufacturing permanent false drift on a correct
client. Root cause: retirement not swept across enforcing surfaces.
Remedy: when a surface retires identifiers, every guard, script, and
accepted-id list is swept the same cycle.

C3. A client default model was pinned to a provider identifier that did not
exist in the client's runtime registry (zero of seventy-seven providers),
making the default unresolvable. Root cause: pinning without a registry
existence check. Remedy: a client default must name a model the runtime
registry actually resolves, verified before pinning.

C4. A drift-guard script false-reported three of five drifts because it
failed to parse single-quoted version constants and mis-selected fallback
variables. Root cause: a parser bug in the guard itself. Remedy: guard
parsers are fixed and the guard-script mirrors are compared byte-for-byte.

C5. Declared crons and live schedules diverged in both directions (eleven
drifts cleared in one wave). Root cause: two registries for one schedule.
Remedy: declared and live converge to one truth, preferring the worker's
own health self-description, verified by direct read and the next scan.

C6. A registry version field was fresh while its advertised model list was
stale, re-publishing retired identifiers on a discovery surface. Root
cause: partial reconciliation. Remedy: version and model list are
reconciled together from the live endpoint.

C7. The versioned instruction set's title line lagged its footer by several
revisions, and a parity guard that should have caught it was failing open
because its anchor check silently no-ops when the anchor format changes.
Root cause: a guard wired advisory-only, plus a fail-open anchor.
Remedy: parity guards are wired fatal into the gate that runs, and an
absent anchor is a failure, not a skip.

Theme D - concurrency and locking.

D1. Deploy-lock timestamps stored as ISO text sorted above numeric epochs
in SQLite, producing a lock that never expired and wedged deployments
across sessions. Root cause: type mismatch between writer and reaper.
Remedy: lock timestamps are numeric epochs, and the immortal row class is
detected and deleted.

D2. A deploy-guard advanced its own version ledger even when the wrapped
command failed, so the next deploy was refused with a version mismatch
while the live worker was unchanged. Root cause: optimistic ledger.
Remedy: on failure, the guard's believed version is resynchronized from a
live health read before retry.

D3. Two sessions sharing one platform token overwrote each other's worker
deploy between upload and verification. Root cause: last-write-wins with no
lock. Remedy: deploys acquire a distributed lock; a read-back version
without the expected content markers is treated as a clobber, not success;
the canonical object store is refreshed so auto-heal re-asserts the build.

D4. A deploy wrapper invoked a Node command that does not exist on Windows
(the cmd-suffixed variant is required), failing before the guard ran.
Root cause: platform assumption in the wrapper. Remedy: the wrapper uses
the platform-correct command form.

D5. A worker deploy shipped a call to a helper function that did not exist
in the file - syntax checks pass on undefined references - and the
semantic-cache path it guarded was inert with zero metrics for days.
Root cause: no symbol-closure check before deploy. Remedy: every deploy
asserts that every helper the changed code calls is defined in the same
file.

D6. A durable-object class was deployed with a storage backend guessed
rather than read from the live namespace, because the platform changed its
schema requirement. Root cause: guessing platform state. Remedy: storage
type is read from the live namespace before deploy.

D7. A syntax error in a git-sourced worker made every bundle fail, so the
repo-sourced redeploy cron could never carry it and live silently diverged
from main; conflict markers from a concurrent edit produced the same
class. Root cause: no build gate before push. Remedy: build verification
and conflict-marker sweep before push; the cron carries only a buildable
file.

D8. Vector-index writes were misread as broken because a fresh entry was
not immediately queryable (eventual consistency). Root cause: expecting
synchronous indexing. Remedy: re-probe after a short delay before
concluding a broken path.

Theme E - false alarms and false blockers.

E1. An authentication failure was concluded from a probe sent without the
credential, written to the ledger as a blocker, and handed to the human -
when the same call with the key already on disk returned success. Root
cause: treating an unauthenticated probe as a finding. Remedy: a blocker
must survive an explicit falsification attempt with credentials before it
is recorded; operational blockers are never handed to the user.

E2. A secret's local presence was once judged from the process environment
rather than the file store, producing a false "missing credential"
conclusion while the key sat in the environment file. Root cause: checking
the wrong surface. Remedy: secrets are read from their file stores.

E3. A health probe against an auth-gated route was once reported as an
outage before noticing the probe carried no credential. Root cause: same as
E1. Remedy: same as E1.

E4. A "missing" configuration was once declared from a cached snapshot
twelve hours old while the live state differed on multiple counts. Root
cause: trusting cache over live. Remedy: counts are cross-checked against a
live call before being trusted.

Theme F - consolidation and distribution.

F1. The September consolidation wave shrank the fleet from 57 to 38 workers
and retired the social-distribution worker while its queue was
load-bearing; distribution silently stopped and the audience-growth gate
decayed with it. Root cause: retirement judged by invocation counts, not
live consumers. Remedy: before retirement, prove no live consumer of the
flow; the worker was reinstated and is live and posting again.

F2. The same consolidation wave dropped workers that were still actively
consumed (hundreds of requests per week), because documentation suspicion
was treated as usage evidence. Root cause: doc-flagged superseded assumed
dead. Remedy: traffic analytics before retirement, always.

F3. The consolidation was itself the response to an audit verdict that
maintenance burden exceeded autonomy: hundreds of dynamic workers were
untracked and about to bill, and the system was not autonomous enough to
justify its size. Root cause: growth outpaced governance. Remedy:
consolidation toward a verified core, plus automated optimization so the
registry and topology maintain themselves.

Theme G - recurrence and closure.

G1. An issue closed without a passing re-probe recurred at a 26 percent
daily failure rate. Root cause: "closed" treated as "fixed". Remedy: every
closure carries a passing live re-probe or an owned deferral with a due
date; a backlog root-cause register tracks the pattern.

G2. A self-heal detector filed blank or misclassified rows forever because
it extracted tool names with a naive parser and matched recovery by the
wrong key. Root cause: detection without disposition plus lossy parsing.
Remedy: normalized name extraction, blank names skipped, and every register
has an owned disposition actor that closes or escalates each row.

G3. A weekly advisor filed the same model-degraded issue every cycle,
accepted its own verdict, and closed nothing. Root cause: filing mistaken
for fixing. Remedy: detection must trigger a verified action that closes;
re-filing is open-dedup only.

G4. A guard that existed but was not wired into the gate that runs produced
a clean exit code while the drift it guarded against was happening. Root
cause: advisory wiring. Remedy: a guard that is not wired into the gate
that runs is not a gate.

Theme H - local-operations lessons.

H1. Backup snapshot files (several GB each) leak on hard kills because
cleanup in a finally block never runs, and the daily purge cannot clean
same-day orphans. Root cause: cleanup tied to graceful exit. Remedy:
independent purge sweeps tolerant of same-day orphans, plus purge at the
start of each backup run.

H2. A skill registry gap left forty skills on disk against fifteen
registered, so dedicated skill documentation went unloaded during the exact
work it covered. Root cause: on-disk presence mistaken for registration.
Remedy: registry membership verified before reliance; the gap is tracked
until closed.

H3. A planned "duplicate" cleanup was a near-miss that would have deleted
live configuration, caught only by a junction-point check that proved the
"duplicates" were links. Root cause: dedupe before link check. Remedy:
junction/hardlink probes are mandatory before any dedupe deletion.

H4. A version-parity audit read the first occurrence of a version marker
instead of the last, reporting three false breaches. Root cause:
first-match scanning of an accumulating file. Remedy: parity audits read
the last occurrence.

H5. Editing a configuration file was reported as a runtime change while the
running app still held the old state, because the file is the source of
truth but only re-reads on restart. Root cause: file-vs-runtime confusion.
Remedy: runtime state is reconciled in-session; "restart the app" is never
handed to the user as a step the agent can execute itself.

Theme I - miscellany.

I1. A gateway reference to a model used a bare name or a route that did not
exist, producing failures on the agent path. Root cause: unverified
references. Remedy: every model reference is checked for provider-qualified
form and route existence before use.

I2. A reasoning model consumed the entire client token budget in thinking,
yielding an empty answer. Root cause: client cap below the reasoning floor.
Remedy: effective answer caps are floored in both chat and workflow paths.

I3. A partial update of a gateway configuration failed because the
platform requires the full object round-trip. Root cause: partial PUT.
Remedy: get-then-put with every non-read-only key.

I4. A schedule re-registration used the wrong body shape and was rejected.
Root cause: schema mismatch. Remedy: the platform's array shape is used on
every re-register.

I5. Secrets set through a shell redirection stored a trailing newline,
breaking constant-time comparisons. Root cause: stdin redirection
semantics. Remedy: exact-value secret writes.

I6. A global gate placed above a route table made every later route
unreachable to its own scoped credential, diagnosed only by identical 401
bodies on both methods. Root cause: route ordering. Remedy: scoped routes
sit above module-wide gates.

I7. Email command parsing failed on case-sensitive header matching and
mangled quoted-printable MIME, and the outreach scanner suppressed the
operator's own address. Root cause: fragile parsing plus over-broad
suppression. Remedy: case-insensitive MIME parsing, and owner/allowlisted
addresses are never suppressed.

I8. An automated optimizer once overwrote seven correct registry versions
from days-old probe bodies. Root cause: probe-derived evidence trusted over
live health. Remedy: versions fill only missing or non-semver values, from
live health first, with a semver gate on every write.

I9. Two concurrent sessions with a shared conversation applied identical
edits and left duplicate gate blocks and banners. Root cause: uncoordinated
writers. Remedy: idempotent patching (skip when the marker is present) plus
a post-write marker-count sweep.

I10. Content-addressed storage reads returned stale files because of
CDN caching, and local git refs lagged the remote, producing "the fix is
gone" conclusions that were false. Root cause: uncached verification
missing. Remedy: repository state is verified through the uncached API.

## 4.2 What the ledger shows

4.2.1 The dominant failure classes are not novel technical problems; they
are governance problems: two sources of truth for one state (Theme C,
Theme D), detection without disposition (Theme G), stale evidence trusted
over live probes (Theme E), and retirement without consumer proof (Theme
F). Roughly three-quarters of the ledger entries reduce to one of these
four.

4.2.2 The failures that caused real damage - the transcript leak, the cost
escalation, the distribution outage - all happened because a gate was
missing, not because a gate failed. The system's defense is therefore
breadth of codified lessons, which is why the instruction set grows by
roughly one revision per operating cycle.

4.2.3 The most dangerous failure was the one the system itself did not
notice: the distribution outage was invisible until an audience gate
decayed, because nothing monitored the queue the retired worker had been
draining. Monitoring the monitors remains an open gap.

## 4.3 Census drift (resolved). A dead live worker was unknown to the fleet
for an unknown period before its registry row was removed, and a
consolidation wave mid-session produced a transient count mismatch (38
live scripts against 39 live rows). Both were resolved the same day: the
census table and the deployed scripts now agree exactly at 36 rows and 36
scripts with zero drift. The class is tracked as a standing fleet
improvement (bookkeeping mis-reported fleet size); the lesson is that a
census is only authoritative when it is reconciled to the live platform on
every scan, which is what the registry exists to do.

# 5. Root-cause themes

5.1 Detection without disposition. The fleet is good at writing rows -
alerts, improvements, issues - and repeatedly failed to own the actor that
closes them. Detection is not remediation; a row in a table fixes nothing.

5.2 Guards that exist but are not wired into the gate that runs. Several
integrity checks existed and passed while the failure they guarded against
was happening, because nothing invoked them fatally.

5.3 Two sources of truth for one state. Client versus server, declared
versus live, file versus runtime - most divergence classes above are
two-truths problems. The durable fix is always to pick one authority and
reconcile the other to it.

5.4 Stale evidence. Cached snapshots, first-match version scans, CDN reads,
and days-old probe bodies were repeatedly trusted over a live call,
producing false drift, false compliance, and false blockers.

5.5 Cost asymmetry between paths. Whenever a feature had two code paths
(streaming versus non-streaming, paid versus free, cron versus manual),
one path silently carried a different cost or freshness policy.

5.6 Self-inflicted severity. The largest outages were consequences of the
fleet's own maintenance actions (consolidation retirement, guard edits,
cleanup plans), not of external platform failures. External platform errors
are extremely rare; the audit order is: change audit, differential proof,
revert, and only then external causes.

5.7 Related work in the program corpus. This document is operational rather
than bibliographic, but it sits alongside a body of work that the described
pipeline produced. Three strands are directly related. First, the program's
methodological study of ignorance auditing and AI-generation detection in an
assisted research pipeline, the epistemic counterpart to the operational
ledger given here. Second, the physics-of-computation and problem-substrate
analyses (fundamental limits, and the honest matching of computational
problems to physical substrates), which are the program's representative
outputs and the kind of artifact this infrastructure exists to deposit and
distribute. Third, the adelic-physics synthesis and the p-adic
anyon-braiding work, which show the corpus's cross-linking depth. The
concrete deposited records are 10.5281/zenodo.22753170,
10.5281/zenodo.22753039, 10.5281/zenodo.22753022, 10.5281/zenodo.22741799,
and 10.5281/zenodo.22749803. The relationship is infrastructure to output:
this fleet's failure ledger is the operational complement to the corpus's
methodological claims.

# 6. Roadmap

6.1 Consolidate toward a smaller, verified core. Retirement decisions move
from invocation counts to live-consumer proof, and the registry returns to
exact parity with deployed scripts (the one-row gap found during this
writing is the immediate example).

6.2 Automate the optimization work itself. The fleet optimizer now runs
hourly: it derives the topology from binding truth, normalizes registry
versions from live health endpoints, and records verified self-heal actions
- the agent's manual optimization passes become supervision rather than
labor.

6.3 Complete the cost-routing stack and measure cost per successful task by
class, so budget decisions are made from task economics rather than raw
token spend, and the free-first policy is uniform across every path.

6.4 Make governance metrics real. Survival-gate metrics must be computed
from authoritative sources at evaluation time; a gate whose metric is
undefined or mis-defined fires wrongly, and a displayed zero is worse than
an explicit undefined.

6.5 Restore the funnel. Every deposit publicizes its canonical page in
public metadata, social distribution stays load-bearing and monitored, and
the publication-to-audience path is watched end to end so a silent
distribution death is impossible again.

6.6 Close the named autonomy gaps: event-driven coordination (currently
time-triggered only), faster deploy-class action latency (currently days),
and verified probe coverage - the three items the fleet's own scorecard
lists between its current state and its mission.

6.7 Keep the discipline cheap. The gate library is the moat; the roadmap
must keep each new gate machine-enforced and self-verifying, or the library
becomes documentation rather than defense.

6.8 The endpoint: a watchmaker index at or near zero - no recurring
operation that requires a human - with the human role reduced to direction,
ratification, and identity-bound actions that cannot be delegated.

# 7. Failure modes of this document

7.1 All quantitative claims are same-day probes (2026-09-27) against the
live account and its databases, except the Zenodo aggregates, which come
from the fleet's periodic stats table rather than a live Zenodo API walk.

7.2 The autonomy scores are the fleet's own self-assessment, not an
external audit; they inherit its blind spots, and the probe-coverage gap
they name applies to this document too.

7.3 The success/failure classification is judgment. A hostile reader could
reclassify several items (for example, the consolidation itself as
prudence rather than over-reach).

7.4 The account changes daily; specific counts (workers, records, spend)
will drift from the values quoted here.

7.5 The instruction set that documents these failures is written by the
same agent that caused them; a reader should treat the failure list as
lower-bounded, not complete, and the "remedy" column as applied-practice
claims that deserve independent verification.

7.6 This document's own publish path - direct deposit, database insert,
site verification - is simpler than the fleet's full research pipeline and
does not exercise every gate that pipeline enforces; the process proof is
narrower than the claims about process.

# Appendix A. Evidence snapshot (2026-09-27)

All values read live during the writing session.

- Workers deployed: 36 scripts; registry: 36 live rows; drift 0. The count
  moved 38->36 during the session (a consolidation wave retired
  qnfo-goal-author and qnfo-skills-mcp).
- AI endpoints advertise one model each (verified live: ops / qnfo /
  personal).
- Email surface: 714 messages total (314 sent, 10 replied, 254 spam).
- Calendar: 65 events on the shared plane; the email-to-calendar intake has
  0 ingested events to date.
- D1: 10 databases, ~304 MB; largest: audit ~202 MB, living-paper ~40 MB.
- Vectorize: 8 indexes; research index 34,657 vectors; personal 154,734.
- R2: 19 buckets; KV: 4 namespaces; web-analytics sites: 7.
- AI gateway: spend cap $150/30d (sliding); recent log window: 20 requests,
  $0.0074; six of seven model families at $0.
- Papers: 905 rows, 438 published; publication events last 30 days: 53.
- Zenodo stats (fleet table): 298 records, 25,408 views, 13,307 downloads.
- Social posting: active; threads posted same day (2026-09-27 11:10 UTC).
- Audit database: ~250 tables; self-heal actions 1,889; handoffs 1,264.
- Autonomy scorecard (2026-09-24): composite 3.6/5; watchmaker 4.8/5;
  control 4.5/5; OODA closure 4.2/5; coordination 4.0/5; self-healing 4.0/5.

# Appendix B. Worker census by layer (2026-09-27)

Control plane: one execution endpoint. Research: research gateway,
calibration, search. Publishing: paper indexer, paper reviser, research
executor (Zenodo depositor), PDF, archive. Operations: fleet control,
deploy guard, fleet dashboard, backlog executor, cloud ops, kaizen,
lifecycle, infrastructure, observability, goal author, skill sync, tools
MCP, skills MCP, memory MCP, agent orchestrator, containers pilot, signal
engine, fleet exec. Outreach and intake: email, outreach, social,
subscribers, calendar API, idea hub. Personal: personal API, personal
companion. Gateways: gateway, AI endpoints.

# Appendix C. The corrected numbers that matter

The September consolidation audit that nearly triggered a shutdown was
built on two measurement errors: gateway billing read as dollars (actual
September invoice $188.34; auto top-ups $10.50 each) and a growth metric
rendered as -0.7% month-over-month when the true 30-day figure was +410%.
Both were corrected before any phase-1 action executed. The episode is the
strongest single argument for the governance-metric rule in Section 2.5:
thresholds must be evaluated on measured reality, and a metric that cannot
be computed must read as undefined, never as zero.

# References

The evidence for this paper is operational rather than bibliographic. All
counts, scores, and states cited above were read directly from the live
Cloudflare account, its D1 databases, its deployed worker versions, and its
fleet ledger during the 2026-09-27 session; the canonical operating
instruction set and the 2026-09-25 and 2026-09-26 kaizen cycles provide the
failure histories. The canonical page for this document and its updates is
https://papers.qnfo.org/papers/quniverse-fleet-lessons/ .
