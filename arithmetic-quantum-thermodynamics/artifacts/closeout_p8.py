"""closeout_p8.py — QNFO.RES.031 Phase 8 distribution closeout driver.

Writes (all via D1 REST with param binding):
  1. qnfo-graph: project node phase P6 -> P8, tags += v1.0-phase6/7 + v1.0-published
  2. qnfo-audit.handoffs: INSERT closeout row
  3. qnfo-audit.wbs_state: UPSERT (8/8 phases, DOI, tags, verdicts)
Evidence: artifacts/closeout-p8-evidence.json.
"""
import json
import os
import urllib.request

ACCOUNT = "edb167b78c9fb901ea5bca3ce58ccc4b"
GRAPH = "a1954b92-d681-4d02-b1f6-f9a2eb4c265d"
AUDIT = "35e2e573-92f3-46ac-83c6-22f6429fc5e5"
TOKEN = open(os.path.expanduser("~/tokens/cloudflare"), encoding="utf-8").read().strip()
PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.cloudflare.com/client/v4/accounts/%s/d1/database/%s/query"
SESSION = "w3NojrHWdFAZyw7rBUfbw"
DOI = "10.5281/zenodo.22159758"

EVIDENCE = []


def d1(db, sql, params=None):
    body = {"sql": sql}
    if params is not None:
        body["params"] = params
    req = urllib.request.Request(
        API % (ACCOUNT, db),
        data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def log(label, ok, detail=""):
    EVIDENCE.append({"step": label, "ok": ok, "detail": str(detail)[:200]})
    print(("OK  " if ok else "ERR ") + label + (" :: " + str(detail)[:200] if detail else ""))


TAGS = ["v0.1-phase0-res031", "v0.2-phase1-res031", "v0.3-phase2-res031",
        "v0.4-phase2-res031", "v0.5-phase3-res031", "v0.6-phase4-res031",
        "v1.0-phase5-res031", "v1.0-phase6-res031", "v1.0-phase7-res031",
        "v1.0-published-res031"]


def main():
    # 1. KG project node -> P8, full tag set
    props = json.dumps({
        "wbs": "QNFO.RES.031",
        "slug": "arithmetic-quantum-thermodynamics",
        "github_repo": "QNFO/qnfo-research",
        "branch": "res/paper/arithmetic-quantum-thermodynamics",
        "phase": "P8",
        "status": "published",
        "published_doi": DOI,
        "concept_doi": "10.5281/zenodo.22159757",
        "created": "2026-08-29",
        "tags": TAGS,
        "version": "1.0",
        "verdicts": {"C1": "verified", "C2": "verified", "C3": "verified", "C4": "verified"},
    }, separators=(",", ":"))
    try:
        r = d1(GRAPH, "UPDATE nodes SET properties=?, updated_at=datetime('now') WHERE id=?",
               [props, "project:arithmetic-quantum-thermodynamics"])
        ok = r.get("success") and r.get("result", [{}])[0].get("success")
        log("KG project node -> P8", bool(ok), r.get("errors") or "")
    except Exception as e:
        log("KG project node -> P8", False, e)

    # 2. handoffs row
    summary = (
        "QNFO.RES.031 'The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the "
        "Discipline of Arithmetic Interpretations' COMPLETE P0-P8. Published 10.5281/zenodo.22159758 "
        "(concept 22159757), 25 files, live-verified (DataCite findable, records-API 25/25). "
        "Core: C1 exact dictionary, C2 five-level ladder (L2!=L4, L3-only bridge), C3 correction "
        "ledger (11 rows), C4 negative discipline — all code-verified (52 checks: 18/18 + 34/34). "
        "Anchors adjudicated: beta^2/(beta-1)^2=312.1 analytic, exact 311.9, legacy 316.3 = "
        "finite-difference artifact; RES.030 zero-cache quantified as coarse (max err 0.38). "
        "Deployed: D1 living-paper row, KG paper+project nodes+BELONGS_TO prog-res, R2 6/6, "
        "papers-server /papers/arithmetic-quantum-thermodynamics 200 + valid JSON-LD; data-quality "
        "fixes (RES.027 KG node v1.0.1, ultrametric-foundation papers-table v1.1.3). "
        "Disseminated: IndexNow, LinkedIn+Twitter (Buffer), IA web/20260829150403."
    )
    pending = (
        "Vectorize D1-queue auto-index pending (indexer token rotated, RES.030-class documented "
        "deferral; 3 semantic probes no-hit). Re-check at next distribution sweep."
    )
    try:
        r = d1(AUDIT,
               "INSERT INTO handoffs (session_id, project_id, phase_completed, summary, pending_work, next_action, r2_handoff_path, timestamp, wbs_code) VALUES (?,?,?,?,?,?,?,?,?)",
               [SESSION, "arithmetic-quantum-thermodynamics", "P8", summary, pending,
                "None (P0-P8 complete)", "qnfo-releases/2026/08/arithmetic-quantum-thermodynamics/",
                "2026-08-29", "QNFO.RES.031"])
        ok = r.get("success") and r.get("result", [{}])[0].get("success")
        log("qnfo-audit.handoffs INSERT", bool(ok), r.get("errors") or "")
    except Exception as e:
        log("qnfo-audit.handoffs INSERT", False, e)

    # 3. wbs_state upsert
    phase_data = json.dumps({
        "doi": DOI, "concept_doi": "10.5281/zenodo.22159757",
        "tags": TAGS, "status": "published", "version": "1.0",
        "phases_complete": 8,
    })
    try:
        r = d1(AUDIT,
               "INSERT OR REPLACE INTO wbs_state (project_id, current_phase, total_phases, phase_data, last_updated, session_id) VALUES (?,?,?,?,?,?)",
               ["arithmetic-quantum-thermodynamics", "P8", 8, phase_data, "2026-08-29", SESSION])
        ok = r.get("success") and r.get("result", [{}])[0].get("success")
        log("qnfo-audit.wbs_state UPSERT", bool(ok), r.get("errors") or "")
    except Exception as e:
        log("qnfo-audit.wbs_state UPSERT", False, e)

    json.dump(EVIDENCE, open(os.path.join(PROJ, "artifacts", "closeout-p8-evidence.json"), "w"), indent=2)
    print("EVIDENCE saved;", sum(1 for e in EVIDENCE if e["ok"]), "of", len(EVIDENCE), "steps OK")


if __name__ == "__main__":
    main()
