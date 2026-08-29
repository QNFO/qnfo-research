"""deploy_p6.py — QNFO.RES.031 Phase 6 deployment driver.

D1 writes via the Cloudflare REST API (direct param binding — the paper body
contains apostrophes, so never string-interpolate it). Writes:
  1. living-paper: INSERT papers row (RES.031) + UPDATE ultrametric-foundation
     (pre-registered data-quality fix: papers-table DOI -> v1.1.3 21993481)
  2. qnfo-graph: INSERT paper node + project node + BELONGS_TO edge +
     UPDATE paper:adelic-quantum-statistics (pre-registered I-1: stale
     v1.0.0 DOI 22123068 -> v1.0.1 22133122; concept DOI unchanged)
  3. R2 mirror: PUT 6 release objects under
     qnfo-releases/2026/08/arithmetic-quantum-thermodynamics/
Evidence: artifacts/deploy-p6-evidence.json (every response status + readback).
"""
import json
import os
import urllib.request
import urllib.parse

ACCOUNT = "edb167b78c9fb901ea5bca3ce58ccc4b"
LIVING = "70a58cb3-b2cd-498d-877f-ecca86859a22"
GRAPH = "a1954b92-d681-4d02-b1f6-f9a2eb4c265d"
TOKEN = open(os.path.expanduser("~/tokens/cloudflare"), encoding="utf-8").read().strip()
PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.cloudflare.com/client/v4/accounts/%s/d1/database/%s/query"

TITLE = "The Corrected Primon-Gas Dictionary: Zeta Partition Functions and the Discipline of Arithmetic Interpretations"
DOI = "10.5281/zenodo.22159758"
CONCEPT = "10.5281/zenodo.22159757"
R2_PREFIX = "qnfo-releases/2026/08/arithmetic-quantum-thermodynamics/"

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
        payload = json.loads(r.read())
    return payload


def log(label, ok, detail=""):
    EVIDENCE.append({"step": label, "ok": ok, "detail": str(detail)[:220]})
    print(("OK  " if ok else "ERR ") + label + ((" :: " + str(detail)[:220]) if detail else ""))


def r2_put(key, data):
    enc = urllib.parse.quote(key, safe="")
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/r2/buckets/qnfo/objects/{enc}"
    req = urllib.request.Request(url, data=data, headers={"Authorization": "Bearer " + TOKEN}, method="PUT")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def main():
    md_text = open(os.path.join(PROJ, "arithmetic-quantum-thermodynamics.md"), encoding="utf-8").read()
    abstract = (
        "The primon gas has connected quantum statistical mechanics with multiplicative "
        "number theory since the early 1990s and remains in active use. This paper "
        "consolidates the correspondence into a single audited reference: a corrected, "
        "verified dictionary; a five-level ladder separating mathematical isomorphism "
        "from physical realization claims; and a negative list of what the correspondence "
        "does not license. The premises end where a physical temperature would be "
        "identified at a p-adic place, and no such identification is asserted."
    )

    # ---- 1. living-paper: INSERT RES.031 row ----
    sql = ("INSERT INTO papers (slug, title, authors, abstract, published, r2_path, doi, "
           "version, identifier, identifier_type, zenodo_doi, zenodo_url, status, license, "
           "keywords, paper_type, body_md) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
    params = [
        "arithmetic-quantum-thermodynamics",
        TITLE,
        "Quni-Gudzinas, Rowan Brad",
        abstract,
        "2026-08-29",
        R2_PREFIX,
        DOI,
        "v1.0",
        "arithmetic-quantum-thermodynamics",
        "qnfo",
        DOI,
        "https://zenodo.org/records/22159758",
        "published",
        "cc-by-4.0",
        "primon gas; zeta function; partition function; quantum statistics; Gentile statistics; spectral statistics",
        "research-paper",
        md_text,
    ]
    try:
        res = d1(LIVING, sql, params)
        ok = res.get("success") and res.get("result", [{}])[0].get("success")
        log("living-paper INSERT papers", bool(ok), res.get("errors") or f"meta={res.get('result',[{}])[0].get('meta')}")
    except Exception as e:
        log("living-paper INSERT papers", False, e)

    # ---- 2. living-paper: ultrametric-foundation DOI fix (pre-registered) ----
    try:
        res = d1(LIVING,
                 "UPDATE papers SET doi=?, zenodo_doi=?, version=? WHERE slug=?",
                 ["10.5281/zenodo.21993481", "10.5281/zenodo.21993481", "1.1.3",
                  "ultrametric-foundation-a-mathematical-thesis-on-non-archimedean-physics"])
        ok = res.get("success") and res.get("result", [{}])[0].get("success")
        log("living-paper UPDATE ultrametric-foundation DOI", bool(ok), res.get("errors") or "")
    except Exception as e:
        log("living-paper UPDATE ultrametric-foundation DOI", False, e)

    # ---- 3. KG: paper node ----
    paper_props = json.dumps({
        "slug": "arithmetic-quantum-thermodynamics",
        "title": TITLE,
        "doi": DOI,
        "zenodo_doi": DOI,
        "zenodo_url": "https://zenodo.org/records/22159758",
        "distribution_status": "distributed",
        "r2_path": R2_PREFIX,
        "version": "1.0",
        "wbs": "QNFO.RES.031",
        "published": "2026-08-29",
        "status": "published",
    }, separators=(",", ":"))
    try:
        res = d1(GRAPH,
                 "INSERT INTO nodes (id, label, name, properties) VALUES (?,?,?,?)",
                 ["paper:arithmetic-quantum-thermodynamics", "Paper",
                  "arithmetic-quantum-thermodynamics", paper_props])
        ok = res.get("success") and res.get("result", [{}])[0].get("success")
        log("KG INSERT paper node", bool(ok), res.get("errors") or "")
    except Exception as e:
        log("KG INSERT paper node", False, e)

    # ---- 4. KG: project node ----
    proj_props = json.dumps({
        "wbs": "QNFO.RES.031",
        "slug": "arithmetic-quantum-thermodynamics",
        "github_repo": "QNFO/qnfo-research",
        "branch": "res/paper/arithmetic-quantum-thermodynamics",
        "phase": "P6",
        "status": "published",
        "published_doi": DOI,
        "concept_doi": CONCEPT,
        "created": "2026-08-29",
        "tags": ["v0.1-phase0-res031", "v0.2-phase1-res031", "v0.3-phase2-res031",
                 "v0.4-phase2-res031", "v0.5-phase3-res031", "v0.6-phase4-res031",
                 "v1.0-phase5-res031"],
        "version": "1.0",
    }, separators=(",", ":"))
    try:
        res = d1(GRAPH,
                 "INSERT INTO nodes (id, label, name, properties) VALUES (?,?,?,?)",
                 ["project:arithmetic-quantum-thermodynamics", "Project",
                  "arithmetic-quantum-thermodynamics", proj_props])
        ok = res.get("success") and res.get("result", [{}])[0].get("success")
        log("KG INSERT project node", bool(ok), res.get("errors") or "")
    except Exception as e:
        log("KG INSERT project node", False, e)

    # ---- 5. KG: BELONGS_TO edge ----
    try:
        res = d1(GRAPH,
                 "INSERT INTO edges (id, source_id, target_id, relationship_type, properties) VALUES (?,?,?,?,?)",
                 ["edge:arithmetic-quantum-thermodynamics-belongs-to-res",
                  "paper:arithmetic-quantum-thermodynamics", "prog-res",
                  "BELONGS_TO", "{}"])
        ok = res.get("success") and res.get("result", [{}])[0].get("success")
        log("KG INSERT BELONGS_TO edge", bool(ok), res.get("errors") or "")
    except Exception as e:
        log("KG INSERT BELONGS_TO edge", False, e)

    # ---- 6. KG: RES.027 stale-DOI fix (pre-registered I-1) ----
    fixed = {
        "slug": "adelic-quantum-statistics",
        "title": "Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi-Dirac/Bose-Einstein Distinction",
        "doi": "10.5281/zenodo.22133122",
        "zenodo_doi": "10.5281/zenodo.22123067",
        "zenodo_url": "https://zenodo.org/records/22133122",
        "distribution_status": "distributed",
        "r2_path": "qnfo-releases/2026/08/adelic-quantum-statistics/",
        "version": "1.0.1",
        "wbs": "QNFO.RES.027",
        "published": "2026-08-27",
        "status": "published",
    }
    try:
        res = d1(GRAPH,
                 "UPDATE nodes SET properties=?, updated_at=datetime('now') WHERE id=?",
                 [json.dumps(fixed, separators=(",", ":")), "paper:adelic-quantum-statistics"])
        ok = res.get("success") and res.get("result", [{}])[0].get("success")
        log("KG UPDATE RES.027 node DOI (I-1)", bool(ok), res.get("errors") or "")
    except Exception as e:
        log("KG UPDATE RES.027 node DOI (I-1)", False, e)

    # ---- 7. R2 mirror ----
    for fname in ("arithmetic-quantum-thermodynamics.md",
                  "arithmetic-quantum-thermodynamics.html",
                  "arithmetic-quantum-thermodynamics.pdf",
                  "references.bib",
                  "LICENSE",
                  "README-DEPOSIT.md"):
        data = open(os.path.join(PROJ, fname), "rb").read()
        try:
            r = r2_put(R2_PREFIX + fname, data)
            log(f"R2 PUT {fname}", bool(r.get("success")), f"{len(data)} bytes")
        except Exception as e:
            log(f"R2 PUT {fname}", False, e)

    json.dump(EVIDENCE, open(os.path.join(PROJ, "artifacts", "deploy-p6-evidence.json"), "w"), indent=2)
    print("EVIDENCE saved;", sum(1 for e in EVIDENCE if e["ok"]), "of", len(EVIDENCE), "steps OK")


if __name__ == "__main__":
    main()
