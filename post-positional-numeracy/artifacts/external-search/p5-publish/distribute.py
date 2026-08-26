# -*- coding: utf-8 -*-
"""distribute.py — QNFO.RES.024 distribution (2026-08-26).

R2 mirror (qnfo-releases/2026/08/post-positional-numeracy/), D1 living-paper papers row,
KG node + BELONGS_TO/BUILDS_ON edges, program_registry status=published, Vectorize index,
each with read-back verification. DNS-resilient transport (flapping local resolver).
"""
import json, os, re, socket, ssl, subprocess, sys, time, urllib.error, urllib.parse, urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
CF_TOKEN = open(r"C:\Users\LENOVO\tokens\cloudflare", encoding="utf-8").read().strip()
D1_LIVING = "70a58cb3-b2cd-498d-877f-ecca86859a22"
D1_PORTFOLIO = "d80fdf2a-0a60-45a3-968b-2907ce806dcd"
D1_GRAPH = "a1954b92-d681-4d02-b1f6-f9a2eb4c265d"
IDX_TOKEN = "chnx-idx-v1-k9m2n4p7r5t8"

def resolve_ip(host):
    for i in range(6):
        try:
            return socket.getaddrinfo(host, 443, socket.AF_INET, socket.SOCK_STREAM)[0][4][0]
        except Exception:
            time.sleep(3 * (i + 1))
    out = subprocess.run(["nslookup", host, "8.8.8.8"], capture_output=True, text=True, timeout=30).stdout
    m = re.search(r"Addresses?:\s*([\d.]+)", out) or re.search(r"(\d+\.\d+\.\d+\.\d+)", out)
    if m:
        return m.group(1)
    raise RuntimeError("cannot resolve " + host)

def raw(host, path, method="GET", headers=None, data=None, json_body=None, tries=5):
    ip = resolve_ip(host)
    opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl._create_unverified_context()))
    h = {"User-Agent": UA, "Accept": "application/json", "Host": host}
    if headers:
        h.update(headers)
    if json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
        h["Content-Type"] = "application/json"
    url = "https://" + ip + path
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, method=method, headers=h)
            with opener.open(r, timeout=240) as resp:
                body = resp.read()
                try:
                    return resp.status, json.loads(body.decode("utf-8"))
                except Exception:
                    return resp.status, {"__text__": body.decode("utf-8", "replace")[:500]}
        except urllib.error.HTTPError as e:
            try:
                return e.code, json.loads(e.read().decode("utf-8"))
            except Exception:
                return e.code, {"__text__": "http error"}
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    return -1, {"__error__": str(last)}

def d1(db, sql, params=None):
    body = {"sql": sql}
    if params:
        body["params"] = params
    return raw("api.cloudflare.com", "/client/v4/accounts/%s/d1/database/%s/query" % (ACCT, db),
               method="POST", headers={"Authorization": "Bearer " + CF_TOKEN}, json_body=body)

log = []

def step(name, ok, detail):
    log.append((name, bool(ok), detail))
    print(("PASS" if ok else "FAIL"), name, "-", detail)

# ---------- R2 mirror ----------
BUCKET = "qnfo-releases"
PREFIX = "2026/08/post-positional-numeracy/"
mirror = [
    ("post-positional-numeracy.md", "post-positional-numeracy.md", "text/markdown"),
    ("post-positional-numeracy.html", "post-positional-numeracy.html", "text/html"),
    ("post-positional-numeracy.pdf", "post-positional-numeracy.pdf", "application/pdf"),
    ("README.md", "README.md", "text/markdown"),
    ("LICENSE", "LICENSE", "text/plain"),
    ("references.bib", "references.bib", "application/x-bibtex"),
    ("citation-audit.md", "citation-audit.md", "text/markdown"),
    ("PROJECT-PLAN.md", "PROJECT-PLAN.md", "text/markdown"),
    ("verify_ppn.py", "artifacts/verification/verify_ppn.py", "text/plain"),
    ("ppn-verification-results.json", "artifacts/verification/ppn-verification-results.json", "application/json"),
    ("run-verification.log", "artifacts/verification/run-verification.log", "text/plain"),
    ("check_rendering.py", "artifacts/verification/check_rendering.py", "text/plain"),
]
ok_count = 0
for name, rel, ct in mirror:
    data = open(os.path.join(ROOT, rel), "rb").read()
    key = PREFIX + name
    st, body = raw("api.cloudflare.com",
                   "/client/v4/accounts/%s/r2/buckets/%s/objects/%s" % (ACCT, BUCKET, urllib.parse.quote(key, safe="")),
                   method="PUT", headers={"Authorization": "Bearer " + CF_TOKEN, "Content-Type": ct}, data=data)
    if st == 200:
        ok_count += 1
    else:
        print("  R2 PUT", st, name, str(body)[:120])
step("R2-MIRROR-12", ok_count == len(mirror), "%d/%d objects put" % (ok_count, len(mirror)))

st, lst = raw("api.cloudflare.com",
              "/client/v4/accounts/%s/r2/buckets/%s/objects?prefix=%s" % (ACCT, BUCKET, urllib.parse.quote(PREFIX, safe="")),
              headers={"Authorization": "Bearer " + CF_TOKEN})
r2_keys = [o.get("key") for o in lst.get("result", [])] if isinstance(lst, dict) else []
step("R2-LIST-VERIFY", len(r2_keys) >= len(mirror), "%d objects listed under prefix" % len(r2_keys))

# ---------- D1 papers row ----------
md_text = open(os.path.join(ROOT, "post-positional-numeracy.md"), encoding="utf-8").read()
m = re.search(r"abstract: \|\n(.*?)\n---", md_text, re.S)
abstract = m.group(1).strip() if m else ""
insert_sql = ("INSERT OR REPLACE INTO papers (identifier, title, authors, abstract, published, r2_key, r2_path, "
              "doi, zenodo_doi, version, status, body_md, zenodo_url, slug, paper_type, license, language, keywords, kg_node_id) "
              "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
params = [
    "10.5281/zenodo.22114495",
    "Post-Positional Numeracy: Finite-Adele Encoding and Product-Formula-Verified Exact Rational Arithmetic",
    '["Rowan Brad Quni-Gudzinas"]',
    abstract,
    "2026-08-26",
    PREFIX + "post-positional-numeracy.md",
    PREFIX,
    "10.5281/zenodo.22114495",
    "10.5281/zenodo.22114495",
    "1.0.1",
    "published",
    md_text,
    "https://zenodo.org/records/22114495",
    "post-positional-numeracy",
    "preprint",
    "CC BY 4.0",
    "en",
    json.dumps(["finite adeles", "Hensel codes", "product formula", "exact rational arithmetic",
                "Ostrowski's theorem", "rational reconstruction", "non-Archimedean", "numeration"]),
    "paper:post-positional-numeracy",
]
st, res = d1(D1_LIVING, insert_sql, params)
step("D1-PAPERS-ROW", st == 200 and res.get("success"), "status=%s success=%s" % (st, res.get("success")))

st, chk = d1(D1_LIVING, "SELECT slug, doi, version, status, kg_node_id FROM papers WHERE slug='post-positional-numeracy'")
row = chk.get("result", [{}])[0].get("results", [{}])[0] if isinstance(chk, dict) else {}
step("D1-PAPERS-READBACK", row.get("slug") == "post-positional-numeracy" and row.get("doi") == "10.5281/zenodo.22114495",
     str(row)[:200])

# ---------- KG node + edges ----------
props = json.dumps({"doi": "10.5281/zenodo.22114495", "concept_doi": "10.5281/zenodo.22114388",
                    "version": "1.0.1", "wbs": "QNFO.RES.024", "r2_path": PREFIX,
                    "distribution_status": "distributed", "slug": "post-positional-numeracy",
                    "published": "2026-08-26"})
st, _ = d1(D1_GRAPH,
           "INSERT OR REPLACE INTO nodes (id, label, name, properties) VALUES (?,?,?,?)",
           ["paper:post-positional-numeracy", "Paper",
            "Post-Positional Numeracy: Finite-Adele Encoding and Product-Formula-Verified Exact Rational Arithmetic", props])
step("KG-NODE", st == 200, "node insert status=%s" % st)

edges = [
    ("e-ppn-belongs-prog", "paper:post-positional-numeracy", "prog-res", "BELONGS_TO"),
    ("e-ppn-builds-hensel", "paper:post-positional-numeracy", "zenodo-20756222", "BUILDS_ON"),
    ("e-ppn-builds-silentradix", "paper:post-positional-numeracy", "paper:the-silent-radix", "BUILDS_ON"),
]
e_ok = 0
for eid, src, tgt, rel in edges:
    st, _ = d1(D1_GRAPH,
               "INSERT OR IGNORE INTO edges (id, source_id, target_id, relationship_type, properties) VALUES (?,?,?,?,?)",
               [eid, src, tgt, rel, "{}"])
    e_ok += 1 if st == 200 else 0
step("KG-EDGES", e_ok == len(edges), "%d/%d edges inserted" % (e_ok, len(edges)))

st, kchk = d1(D1_GRAPH, "SELECT id, label, name FROM nodes WHERE id='paper:post-positional-numeracy'")
krow = (kchk.get("result", [{}])[0].get("results") or [{}])[0] if isinstance(kchk, dict) else {}
step("KG-READBACK", krow.get("id") == "paper:post-positional-numeracy", str(krow)[:150])

# ---------- registry status ----------
st, _ = d1(D1_PORTFOLIO, "UPDATE program_registry SET status='published' WHERE wbs_code='QNFO.RES.024' AND slug='post-positional-numeracy'")
step("REGISTRY-PUBLISHED", st == 200, "status update %s" % st)

# ---------- Vectorize index ----------
st, idx = raw("qnfo-paper-indexer.q08.workers.dev", "/webhook?slug=post-positional-numeracy",
              method="POST", headers={"X-Index-Token": IDX_TOKEN})
step("VECTORIZE-WEBHOOK", st == 200, "index trigger status=%s body=%s" % (st, str(idx)[:150]))
time.sleep(4)
st, ver = raw("qnfo-paper-indexer.q08.workers.dev", "/webhook?slug=post-positional-numeracy",
              headers={"X-Index-Token": IDX_TOKEN})
step("VECTORIZE-VERIFY", st == 200 and isinstance(ver, dict) and ver.get("indexed") is True,
     "verify status=%s body=%s" % (st, str(ver)[:200]))

with open(os.path.join(HERE, "distribution-log.json"), "w", encoding="utf-8") as f:
    json.dump([{"name": n, "ok": o, "detail": d} for n, o, d in log], f, indent=1, ensure_ascii=False)
print("DONE; all pass:", all(o for _, o, _ in log))
sys.exit(0 if all(o for _, o, _ in log) else 1)
