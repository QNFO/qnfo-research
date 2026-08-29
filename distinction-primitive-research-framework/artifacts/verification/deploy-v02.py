"""deploy-v02.py — deploy refresh for QNFO.RES.032 v0.2 (reads deposit-info-v02.json).
Updates: KG node props (version/doi/zenodo_url), living-paper papers + paper_ids rows,
writes only where the v0.2 record DOI differs from v0.1. Verify by re-query.
"""
import json, os, time, urllib.request

ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
KG = "a1954b92-d681-4d02-b1f6-f9a2eb4c265d"
LP = "70a58cb3-b2cd-498d-877f-ecca86859a22"
TOKEN = os.environ["CLOUDFLARE_API_TOKEN"]
PROJ = r"C:\Users\LENOVO\qnfo\qnfo-research\distinction-primitive-research-framework"
SLUG = "distinction-primitive-research-framework"
KG_ID = f"paper:{SLUG}"

info = json.load(open(os.path.join(PROJ, "deposit-info-v02.json"), encoding="utf-8"))
DOI = info["record"]
ZEN_URL = f"https://zenodo.org/records/{DOI.split('/')[-1]}"
print("v0.2 record:", DOI, ZEN_URL)

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

# 1. KG node properties update
res = rows(KG, f"SELECT properties FROM nodes WHERE id = '{KG_ID}'")
if res:
    props = json.loads(res[0]["properties"])
    props.update({"version": "0.2", "doi": DOI, "zenodo_doi": DOI, "zenodo_url": ZEN_URL})
    r = q(KG, "UPDATE nodes SET properties = ?, updated_at = datetime('now') WHERE id = ?",
          params=[json.dumps(props), KG_ID])
    assert r.get("success"), r.get("errors")
    print("KG node updated")
print("KG verify:", rows(KG, f"SELECT properties FROM nodes WHERE id = '{KG_ID}'")[0]["properties"][:220])

# 2. living-paper papers row
paper_md = open(os.path.join(PROJ, "distinction-primitive-research-framework.md"), encoding="utf-8").read()
r = q(LP, "UPDATE papers SET version = ?, doi = ?, zenodo_doi = ?, zenodo_url = ?, body_md = ?, "
          "updated_at = datetime('now') WHERE slug = ?",
      params=["v0.2", DOI, DOI, ZEN_URL, paper_md, SLUG])
assert r.get("success"), r.get("errors")
print("papers row updated")
print("verify:", rows(LP, f"SELECT version, zenodo_doi, length(body_md) FROM papers WHERE slug = '{SLUG}'"))

# 3. paper_ids row
r = q(LP, "UPDATE paper_ids SET doi = ?, zenodo_url = ?, updated_at = datetime('now') WHERE slug = ?",
      params=[DOI, ZEN_URL, SLUG])
assert r.get("success"), r.get("errors")
print("paper_ids updated:", rows(LP, f"SELECT doi, zenodo_url FROM paper_ids WHERE slug = '{SLUG}'"))
print("DONE")
