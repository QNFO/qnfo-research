"""deploy-framework.py — KG node + edges + living-paper papers row + paper_ids row for
QNFO.RES.032 (DOI 10.5281/zenodo.22159888), check-then-insert, verify by re-query.
"""
import json, os, time, urllib.request

ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
KG = "a1954b92-d681-4d02-b1f6-f9a2eb4c265d"
LP = "70a58cb3-b2cd-498d-877f-ecca86859a22"
TOKEN = os.environ["CLOUDFLARE_API_TOKEN"]
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"

SLUG = "distinction-primitive-research-framework"
KG_ID = f"paper:{SLUG}"
DOI = "10.5281/zenodo.22159888"
ZEN_URL = "https://zenodo.org/records/22159888"
R2_PATH = f"qnfo-releases/2026/08/{SLUG}/"
TITLE = "Distinction, Number, and the Empirical Filter: The Pre-Arithmetic Research Framework"

def q(db, sql, params=None):
    body = {"sql": sql}
    if params is not None:
        body["params"] = params
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCT}/d1/database/{db}/query",
        data=data, method="POST",
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"})
    for i in range(5):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=60).read())
        except Exception:
            time.sleep(2 + i * 2)

def rows(db, sql):
    r = q(db, sql)
    if not r.get("success"):
        raise RuntimeError(r.get("errors"))
    return r["result"][0]["results"]

paper_md = open(os.path.join(PROJ, "distinction-primitive-research-framework.md"),
                encoding="utf-8").read()
abstract = ("The QNFO arithmetic-physics program connects number-theoretic structure to "
            "statistical mechanics: prime-indexed modes with logarithmic energies yield partition "
            "functions that are exactly zeta objects, and hierarchy distance is a "
            "realization-independent ultrametric. This record states the methodological discipline "
            "those results share, as a reusable framework: a nine-level construction ladder from "
            "the primitive of distinction to the empirical filter of physics; two boundary rules "
            "(no uncommitted reification of the primitive; no isomorphism passes as a physical "
            "realization without a stated measurement protocol, null model, and falsification "
            "condition); and a compact claim record with mechanical demotion rules. The framework "
            "makes no empirical claims of its own and states its one claim - ladder coverage of "
            "the published lineage - together with its falsification protocol.")

# 1. KG node (check-then-insert)
if rows(KG, f"SELECT id FROM nodes WHERE id = '{KG_ID}'"):
    print("KG node exists already")
else:
    props = json.dumps({
        "slug": SLUG, "title": TITLE, "doi": DOI, "zenodo_doi": DOI,
        "zenodo_url": ZEN_URL, "distribution_status": "distributed",
        "r2_path": R2_PATH, "version": "0.1", "wbs": "QNFO.RES.032",
        "published": "2026-08-29", "status": "published"})
    r = q(KG, f"INSERT INTO nodes (id, label, name, properties) VALUES ('{KG_ID}', 'Paper', '{SLUG}', '{props}')")
    assert r.get("success"), r.get("errors")
    print("KG node inserted")
print("verify:", rows(KG, f"SELECT id, label FROM nodes WHERE id = '{KG_ID}'"))

# 2. KG edge BELONGS_TO prog-res
if rows(KG, f"SELECT id FROM edges WHERE source_id = '{KG_ID}' AND relationship_type = 'BELONGS_TO'"):
    print("KG edge exists")
else:
    import uuid
    r = q(KG, f"INSERT INTO edges (id, source_id, target_id, relationship_type, properties) "
              f"VALUES ('{uuid.uuid4()}', '{KG_ID}', 'prog-res', 'BELONGS_TO', '{{}}')")
    assert r.get("success"), r.get("errors")
    print("KG edge inserted")
print("verify:", rows(KG, f"SELECT source_id, target_id, relationship_type FROM edges WHERE source_id = '{KG_ID}'"))

# 3. living-paper papers row
if rows(LP, f"SELECT identifier FROM papers WHERE slug = '{SLUG}'"):
    print("papers row exists")
else:
    sql = ("INSERT INTO papers (identifier, title, authors, abstract, published, doi, version, "
           "zenodo_doi, zenodo_url, body_md, status, slug, r2_path, kg_node_id, identifier_type) "
           "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
    params = [SLUG, TITLE, json.dumps(["Rowan Brad Quni-Gudzinas"]), abstract,
              "2026-08-29", DOI, "v0.1", DOI, ZEN_URL, paper_md, "published",
              SLUG, R2_PATH, KG_ID, "qnfo"]
    r = q(LP, sql, params=params)
    assert r.get("success"), r.get("errors")
    print("papers row inserted")
print("verify:", rows(LP, f"SELECT slug, zenodo_doi, r2_path, kg_node_id, status, length(body_md) FROM papers WHERE slug = '{SLUG}'"))

# 4. paper_ids row
if rows(LP, f"SELECT slug FROM paper_ids WHERE slug = '{SLUG}'"):
    print("paper_ids row exists")
else:
    r = q(LP, f"INSERT INTO paper_ids (slug, vectorize_id, kg_id, doi, r2_path, zenodo_url) "
              f"VALUES ('{SLUG}', '{KG_ID}:0', '{KG_ID}', '{DOI}', '{R2_PATH}', '{ZEN_URL}')")
    assert r.get("success"), r.get("errors")
    print("paper_ids row inserted")
print("verify:", rows(LP, f"SELECT * FROM paper_ids WHERE slug = '{SLUG}'"))
print("DONE")
