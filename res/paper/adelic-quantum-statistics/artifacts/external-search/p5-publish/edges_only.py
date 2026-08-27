# -*- coding: utf-8 -*-
"""edges_only.py — insert the KG edges with the corrected JPC.003 target id."""
import hashlib, json, os, time, urllib.request

CF_TOKEN = open(r"C:\Users\LENOVO\tokens\cloudflare", encoding="utf-8").read().strip()
CF_ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
DB_GRAPH = "a1954b92-d681-4d02-b1f6-f9a2eb4c265d"

def d1(sql, params=None):
    body = {"sql": sql}
    if params:
        body["params"] = params
    data = json.dumps(body).encode("utf-8")
    for i in range(5):
        try:
            r = urllib.request.Request(
                "https://api.cloudflare.com/client/v4/accounts/%s/d1/database/%s/query" % (CF_ACCT, DB_GRAPH),
                data=data, method="POST", headers={
                    "Authorization": "Bearer " + CF_TOKEN,
                    "Content-Type": "application/json"})
            with urllib.request.urlopen(r, timeout=60) as resp:
                j = json.loads(resp.read().decode())
            if not j.get("success"):
                raise RuntimeError(str(j.get("errors"))[:200])
            return j
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(3 + 4 * i)
                continue
            raise RuntimeError("HTTP %s %s" % (e.code, e.read().decode("utf-8", "replace")[:200]))
        except RuntimeError:
            raise
        except Exception:
            time.sleep(3 + 4 * i)
    raise RuntimeError("NET")

edges = [
    ("paper:adelic-quantum-statistics", "prog-res", "BELONGS_TO"),
    ("paper:adelic-quantum-statistics", "project:adelic-quantum-statistics", "BELONGS_TO"),
    ("paper:adelic-quantum-statistics", "paper:finite-distinction-quantum-mechanics", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:self-referential-scalar-family", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:adelic-shannon-theory", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:spin-statistics-distinction", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:exchange-phase-logical-scalar", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:tyranny-of-the-plus-minus-one", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "QNFO.JPC.003", "BUILDS_ON"),
    ("paper:adelic-quantum-statistics", "paper:pattern-particle-unification", "BRIDGES"),
    ("paper:adelic-quantum-statistics", "paper:signal-worker-boundary-confinement", "BRIDGES"),
]
n = 0
for s, t, r in edges:
    eid = "e-" + hashlib.sha256(("%s|%s|%s" % (s, t, r)).encode("utf-8")).hexdigest()[:24]
    d1("INSERT OR IGNORE INTO edges (id, source_id, target_id, relationship_type) VALUES (?,?,?,?)", [eid, s, t, r])
    n += 1
    print("edge", n, s, "->", t, r)
print("EDGES DONE", n)
