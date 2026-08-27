# -*- coding: utf-8 -*-
"""post_publish_res027.py — QNFO.RES.027 P8 post-publish asserts + R2 mirror + Vectorize index (2026-08-27)."""
import json, os, time, urllib.request, urllib.error, urllib.parse

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
VER = os.path.join(PAPER, "artifacts", "verification")
EXT = os.path.join(PAPER, "artifacts", "external-search")
ART = os.path.join(PAPER, "artifacts")
REC = "22123068"
CONCEPT = "22123067"
DOI = "10.5281/zenodo.%s" % REC

CF_TOKEN = open(r"C:\Users\LENOVO\tokens\cloudflare", encoding="utf-8").read().strip()
CF_ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
R2_BUCKET = "qnfo-releases"
R2_BASE = "2026/08/adelic-quantum-statistics"
IDX_TOKEN = "chnx-idx-v1-k9m2n4p7r5t8"

def get(url, headers=None, tries=5):
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, headers=headers or {})
            with urllib.request.urlopen(r, timeout=60) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            last = (e.code, e.read())
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(3 + 4 * i)
                continue
            return e.code, last[1]
        except Exception as e:
            last = ("NET", str(e).encode())
            time.sleep(3 + 4 * i)
    return (0, last[1] if isinstance(last, tuple) else b"")

report = []
def log(s):
    report.append(s)
    print(s)

# 1. POST-PUBLISH-FRONTMATTER-ASSERT-1: download the deposited .md and check its frontmatter
st, body = get("https://zenodo.org/api/records/%s/files/adelic-quantum-statistics.md/content" % REC,
               headers={"User-Agent": UA})
if st == 200:
    txt = body.decode("utf-8", "replace")
    fm = txt.split("---", 2)[1]
    doi_ok = ('doi: "%s"' % DOI) in fm
    ver_ok = 'version: "1.0.0"' in fm
    log("POST-PUBLISH-FRONTMATTER: doi_ok=%s ver_ok=%s" % (doi_ok, ver_ok))
else:
    log("POST-PUBLISH-FRONTMATTER: DOWNLOAD-FAILED %s" % st)

# 2. METADATA-RELATIONS-ASSERT-1: published record carries related_identifiers
st, body = get("https://zenodo.org/api/records/%s" % REC, headers={"User-Agent": UA})
if st == 200:
    d = json.loads(body.decode())
    rel = d.get("metadata", {}).get("related_identifiers", [])
    log("METADATA-RELATIONS: rel_ids=%d state=%s" % (len(rel), d.get("state")))
else:
    log("METADATA-RELATIONS: GET-FAILED %s" % st)

# 3. R2 mirror (R2-MIRROR-AFTER-PUBLISH-1)
FILES = []
for d in (PAPER, VER, EXT, ART):
    for fn in os.listdir(d):
        p = os.path.join(d, fn)
        if os.path.isfile(p) and (fn.endswith((".md", ".html", ".pdf", ".bib", ".py", ".cjs", ".txt", ".json")) or fn == "LICENSE"):
            FILES.append(p)
# restrict to the deposit set: basename collisions impossible across dirs here; use basenames
seen = {}
for p in FILES:
    b = os.path.basename(p)
    if b not in seen:
        seen[b] = p
r2_ok = 0
for b, p in seen.items():
    key = "%s/%s" % (R2_BASE, b)
    url = ("https://api.cloudflare.com/client/v4/accounts/%s/r2/buckets/%s/objects/%s"
           % (CF_ACCT, R2_BUCKET, urllib.parse.quote(key, safe="/")))
    data = open(p, "rb").read()
    last = None
    for i in range(5):
        try:
            r = urllib.request.Request(url, data=data, method="PUT", headers={
                "Authorization": "Bearer " + CF_TOKEN,
                "Content-Type": "application/octet-stream",
            })
            with urllib.request.urlopen(r, timeout=90) as resp:
                j = json.loads(resp.read().decode())
                if j.get("success"):
                    r2_ok += 1
                else:
                    log("R2-FAIL %s: %s" % (b, str(j.get("errors"))[:120]))
                break
        except urllib.error.HTTPError as e:
            last = e.code
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(3 + 4 * i)
                continue
            log("R2-HTTP %s %s: %s" % (b, e.code, e.read().decode("utf-8", "replace")[:120]))
            break
        except Exception as e:
            last = str(e)
            time.sleep(3 + 4 * i)
    else:
        log("R2-NET %s: %s" % (b, last))
log("R2-MIRROR: %d/%d objects written" % (r2_ok, len(seen)))

# 4. Vectorize re-index via qnfo-paper-indexer
st, body = get("https://qnfo-paper-indexer.q08.workers.dev/index?slug=adelic-quantum-statistics",
               headers={"User-Agent": UA, "X-Index-Token": IDX_TOKEN})
try:
    j = json.loads(body.decode())
    log("VECTORIZE-INDEX: status=%s indexed=%s chunks=%s" % (st, j.get("indexed"), len(j.get("chunks", []))))
except Exception:
    log("VECTORIZE-INDEX: %s %s" % (st, body[:150]))

open(os.path.join(HERE, "post-publish-report.txt"), "w", encoding="utf-8").write("\n".join(report))
