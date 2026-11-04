# Risk Register — Infomatics v2

| ID | Risk | Likelihood | Impact | Mitigation | Status |
|:---|:-----|:-----------|:-------|:-----------|:-------|
| R1 | API rate-limiting (arXiv, S2) blocks external searches | Medium | Medium | Stagger queries; cache results; prioritize arXiv over S2; fall back to web search | Active |
| R2 | QNFO-internal claims have zero external citations — survey finds nothing established | High | Low | This IS a finding. Tag as [QNFO-Internal] and document the gap | Active |
| R3 | Scope exceeds available evidence — some domains have no literature | Medium | Medium | Narrow scope to domains with ≥5 external papers; mark empty domains as gaps | Active |
| R4 | LLM recall contaminates bibliography | Medium | CRITICAL | Every citation MUST be verified against API, DOI, or publisher page before inclusion. Zero tolerance for unverified citations | Active |
| R5 | Git operations fail due to temp-directory race condition (INFOMATICS-FALSE-CLAIM-2026-07-19) | Medium | CRITICAL | ALL git operations from persistent working directory. NO temp-dir batch git with cleanup. NEVER `git push --force` without verification | Active |
| R6 | v1 content contaminates v2 through shared dependencies or copy-paste | Low | Medium | Separate repo (rwnq8/infomatics-v2). v1 repo marked as deprecated in README | Active |
| R7 | Classification system is too coarse and misses nuance | Low | Low | Allow sub-tags within [Speculative] (e.g., [Speculative — no experiment] vs [Speculative — mathematical proposal]) | Active |
