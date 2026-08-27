# -*- coding: utf-8 -*-
"""d1_kg_distribute.py — QNFO.RES.027 P8: D1 + KG + registry distribution (2026-08-27)."""
import json, os, time, urllib.request, urllib.error

CF_TOKEN = open(r"C:\Users\LENOVO\tokens\cloudflare", encoding="utf-8").read().strip()
CF_ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
DB_PAPERS = "70a58cb3-b2cd-498d-877f-ecca86859a22"
DB_PORT = "d80fdf2a-0a60-45a3-968b-2907ce806dcd"
DB_GRAPH = "a1954b92-d681-4d02-b1f6-f9a2eb4c265d"
HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.normpath(os.path.join(HERE, "..", "..", ".."))

DOI = "10.5281/zenodo.22123068"
CONCEPT = "10.5281/zenodo.22123067"
R2P = "qnfo-releases/2026/08/adelic-quantum-statistics/"

def d1(db, sql, params=None):
    body = {"sql": sql}
    if params:
        body["params"] = params
    data = json.dumps(body).encode("utf-8")
    last = None
    for i in range(5):
        try:
            r = urllib.request.Request(
                "https://api.cloudflare.com/client/v4/accounts/%s/d1/database/%s/query" % (CF_ACCT, db),
                data=data, method="POST", headers={
                    "Authorization": "Bearer " + CF_TOKEN,
                    "Content-Type": "application/json",
                })
            with urllib.request.urlopen(r, timeout=60) as resp:
                j = json.loads(resp.read().decode())
            if not j.get("success"):
                last = j.get("errors")
                raise RuntimeError(str(j.get("errors"))[:200])
            return j
        except urllib.error.HTTPError as e:
            last = e.read().decode("utf-8", "replace")[:200]
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(3 + 4 * i)
                continue
            raise RuntimeError("HTTP %s %s" % (e.code, last))
        except RuntimeError:
            raise
        except Exception as e:
            last = str(e)
            time.sleep(3 + 4 * i)
    raise RuntimeError("D1-NET %s" % last)

report = []
def log(s):
    report.append(s)
    print(s)

md_text = open(os.path.join(PAPER, "adelic-quantum-statistics.md"), encoding="utf-8").read()
title = "Quantum Statistics from the Adelic Product Formula: The Squarefree Origin of the Fermi-Dirac/Bose-Einstein Distinction"
abstract = ("The Bose-Einstein and Fermi-Dirac occupation distributions are read as the maximum-entropy solutions of one "
            "lattice with two multiplicity rules: the unrestricted integer lattice (Dirichlet series the Riemann zeta "
            "function) and the squarefree restriction (a ratio of two zeta values). The paper supplies the per-distinction "
            "rate gamma = 1/N from bath degeneracy, the complex structure as the sign-normalized generator selected by "
            "exclusion, the Moebius-parity dictionary of composite statistics, and the bounded-occupation interpolation "
            "family that anyonic statistics must contact. Register: isomorphisms of mathematical structure; no particle "
            "ontology.")

# 1. papers row
d1(DB_PAPERS, """
INSERT INTO papers (identifier, title, authors, abstract, published, r2_key, doi, version, identifier_type,
                    zenodo_doi, body_md, zenodo_url, status, language, license, slug, r2_path)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", ["adelic-quantum-statistics", title, '["Rowan Brad Quni-Gudzinas"]', abstract,
      "2026-08-27", R2P, DOI, "1.0.0", "qnfo", DOI, md_text,
      "https://zenodo.org/records/22123068", "published", "eng", "cc-by-4.0",
      "adelic-quantum-statistics", R2P])
log("papers row inserted")

# 2. paper_ids row
d1(DB_PAPERS, """
INSERT INTO paper_ids (slug, vectorize_id, kg_id, doi, r2_path, zenodo_url)
VALUES (?, ?, ?, ?, ?, ?)
""", ["adelic-quantum-statistics", "paper:adelic-quantum-statistics:0",
      "paper:adelic-quantum-statistics", DOI, R2P, "https://zenodo.org/records/22123068"])
log("paper_ids row inserted")

# 3. KG nodes
paper_props = json.dumps({
    "slug": "adelic-quantum-statistics", "title": title, "doi": DOI, "zenodo_doi": CONCEPT,
    "zenodo_url": "https://zenodo.org/records/22123068", "distribution_status": "distributed",
    "r2_path": R2P, "version": "1.0.0", "wbs": "QNFO.RES.027",
    "published": "2026-08-27", "status": "published"})
proj_props = json.dumps({
    "wbs": "QNFO.RES.027", "slug": "adelic-quantum-statistics",
    "github_repo": "QNFO/qnfo-research", "branch": "res/paper/adelic-quantum-statistics",
    "phase": "P8", "status": "distributed", "published_doi": DOI, "concept_doi": CONCEPT,
    "created": "2026-08-27", "tags": ["v0.1-phase0-res027"]})
d1(DB_GRAPH, "INSERT INTO nodes (id, label, name, properties) VALUES (?,?,?,?)",
   ["paper:adelic-quantum-statistics", "Paper", "adelic-quantum-statistics", paper_props])
d1(DB_GRAPH, "INSERT INTO nodes (id, label, name, properties) VALUES (?,?,?,?)",
   ["project:adelic-quantum-statistics", "Project", "adelic-quantum-statistics", proj_props])
log("KG nodes inserted")

# 4. KG edges (SEMANTIC LINKS ARE BUILT)
edges = [
    ("paper:adelic-quantum-statistics", "prog-res", "BELONGS_TO"),
    ("paper:adelic-quantum-statistics", "project:adelic-quantum-statistics", "BELONGS_TO"),
    ("paper:adelic-quantum-statistics", "paper:finite-distinction-quantum-mechanics", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:self-referential-scalar-family", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:adelic-shannon-theory", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:spin-statistics-distinction", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:exchange-phase-logical-scalar", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:tyranny-of-the-plus-minus-one", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:jpcub-qec-landauer", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:pattern-particle-unification", "BRIDGES"),
    ("paper:adelic-quantum-statistics", "paper:signal-worker-boundary-confinement", "BRIDGES"),
]
for s, t, r in edges:
    d1(DB_GRAPH, "INSERT INTO edges (source_id, target_id, relationship_type) VALUES (?,?,?)", [s, t, r])
log("KG edges inserted: %d" % len(edges))

# 5. program_registry re-point (PUBLISH-CHECKLIST-PORTFOLIO-REPOINT-1)
d1(DB_PORT, """
UPDATE program_registry SET zenodo_doi = ?, current_version = ?, phase = 'P8', status = 'published'
WHERE wbs_code = 'QNFO.RES.027'
""", [DOI, "1.0.0"])
log("program_registry re-pointed")

open(os.path.join(HERE, "d1-kg-distribution-report.txt"), "w", encoding="utf-8").write("\n".join(report))
print("DISTRIBUTION COMPLETE")
