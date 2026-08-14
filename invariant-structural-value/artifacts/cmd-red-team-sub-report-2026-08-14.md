# CMD RED TEAM SUB — Post-Publication Adversarial Analysis (QNFO.RES.007)

**Published record (current):** Zenodo v0.2 — DOI 10.5281/zenodo.21929590 (concept 10.5281/zenodo.21929478)
**Record history:** v0.1 = 10.5281/zenodo.21929479 (superseded; 4 HARD + 3 SOFT findings remediated via newversion → v0.2)
**Audit date:** 2026-08-14 · **Mode:** parallel reviewer dispatch + direct parent-agent fallback · **READ-ONLY**

## 1. Protocol execution

- `subagent_orchestrator` is not in the tool registry (SKILL-REGISTRY-GAP-1); equivalent `deepchat_subagents` (slotId=reviewer) used.
- **3 reviewer slots dispatched in parallel** (Accuracy / Completeness / Dependency): delegations `JuI9RScTqrb52_7k0824E`, `sdTNNRARwOSq6cVmHjfH9`, `29wXg7dBS-Y7lM7OkQsDS`.
- **All 3 stalled in queue** (~150 s, zero child sessions started) → **fallback executed per protocol**: direct parent-agent audit with live tool verification (never treat a stalled subagent as "review complete").

## 2. Direct audit findings (live, this cycle)

### ACCURACY — PASS
| Check | Result |
|:------|:-------|
| doi.org HEAD 10.5281/zenodo.21929590 | **200** |
| DataCite api.datacite.org/dois/10.5281/zenodo.21929590 | **200 — state=findable**, title correct, **11 subjects** |
| Zenodo records API 21929590 | **200 — state=done, 14 files, version v0.2, license cc-by-4.0** |
| Numeric claims vs fit-verify.txt | PASS (e series 2.718281828459; π Machin 1e-12; \|e^{iπ}+1\|=1.2e-16; periodicity 4–8e-16; f′=f <9e-9) — verified in prior cycle, artifact in deposit |
| [TERRITORY] labels carry disconfirmation | PASS (C1/C2/C3 + Formal-derivation block — inline conditions) |
| No internal refs in body / single title | PASS (language gate: 0 internal refs, 0 Unicode-math outside $, title-dup gate PASS) |

### COMPLETENESS — PASS
| Check | Result |
|:------|:-------|
| Deposit file set | **14/14 expected, 0 missing, 0 extra** (md/pdf/html + references.bib + citation-audit.md + PROJECT-PLAN.md + README.md + RESEARCH-CONTINUITY-REGISTRY.md + bp-gates + fit-verify + terminology + consilience + due-diligence + phase2 + registry) |
| Git branch + tag | ls-remote verified earlier cycle: branch `ef6d952…`, tags `invariant-structural-value-v0.1-phase0` + `-v0.1-published` |

### DEPENDENCY — PASS
| Check | Result |
|:------|:-------|
| Bib entry count / uniqueness | **42 entries, 42 unique, 0 duplicate keys** |
| Synthetic DOIs (doi == key) | **0** |
| DOI resolution (31 DOIs checked via doi.org HEAD) | 26 × **200**; 5 × **403 (doi.org WAF bot-block)** |
| WAF-blocked 5 re-verified via Crossref | **ALL real and correct**: Every Thing Must Go (Ladyman–Ross–Spurrett–Collier, 2007), Structural Realism/OBO (Ladyman, 2013), Z3-graded (Zhang–Hu–Zhang, 2026), Kapustin–Witten (2007), Peebles–Ratra (2003) — correct year/author/title |

## 3. Aggregate verdict

**No new HARD or SOFT findings on the current published record (v0.2).**
The 4 HARD + 3 SOFT findings from the v0.1 audit (synthetic Joyal–Street DOI, bib year drift 1986→1993, audit double-count, BP-10 count overstatement) were remediated in v0.2 and remain fixed.

**DESIGN findings (advisory, logged as kaizen candidates):**
1. **REDTEAM-QUEUE-STALL-1 (new):** reviewer subagents queued but never started (>150 s) — direct fallback required. Suggests a slot-capacity/queue issue in the orchestration layer; consider surfacing queue state earlier or auto-fallback timer.
2. **DOI-WAF-403-class:** doi.org HEAD returns 403 on some publisher DOIs (OUP/OBO/MDPI/CNTP/APS) under audit UA; Crossref API is the authoritative re-verification path — already documented pattern (ZENODO-BOT-403-1 class); recommend a scripted audit helper that auto-falls back to Crossref.

## 4. Publish-then-audit loop status

- v0.1 published → audited → **4 HARD + 3 SOFT** → remediated → **v0.2 newversion (21929590)** → re-audited → **CLEAN**.
- Concept DOI 10.5281/zenodo.21929478 resolves to the latest corrected version.
- Audit report committed to repo as `artifacts/post-publication-audit.md` (prior cycle) + this file; published artifact untouched (READ-ONLY).

**Loop: publish → audit → remediate (newversion) → re-audit → verify → log. Never publish-and-forget.**
