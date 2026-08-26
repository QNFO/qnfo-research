# -*- coding: utf-8 -*-
"""replace3.py — QNFO.RES.024: finish v1.0.1 replacement (3 remaining targets) + uploads + publish.

Deposit-API deletes via links.self (404 = already gone, tolerated). Uploads via deposit-API
multipart. Full-metadata PUT with version 1.0.1. Publish.
"""
import json, os, sys, time, urllib.error, urllib.request

BASE = "https://zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
DRAFT = 22114495

def req(method, path, body=None, ctype=None, raw=None, tries=5):
    h = {"User-Agent": UA, "Accept": "application/json",
         "Accept-Language": "en-US,en;q=0.9", "Referer": BASE + "/", "Origin": BASE,
         "Authorization": "Bearer " + TOKEN}
    if ctype:
        h["Content-Type"] = ctype
    data = raw if raw is not None else (json.dumps(body).encode("utf-8") if body is not None else None)
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(BASE + path, data=data, method=method, headers=h)
            with urllib.request.urlopen(r, timeout=240) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode("utf-8") if e.fp else b"{}")
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise last

# 1. delete remaining targets via deposit-API links.self
st, fl = req("GET", "/api/deposit/depositions/%s/files" % DRAFT)
TARGETS = {"post-positional-numeracy.md", "post-positional-numeracy.html", "post-positional-numeracy.pdf"}
deleted = 0
for f in (fl if isinstance(fl, list) else []):
    name = f.get("filename") or f.get("key")
    if name in TARGETS:
        st2, _ = req("DELETE", f["links"]["self"], raw=b"")
        print("DELETE", st2, name)
        deleted += 1 if st2 == 204 else 0
print("DELETED", deleted, "of", len(TARGETS))
if deleted != len(TARGETS):
    print("DELETE COUNT MISMATCH")
    sys.exit(1)

# 2. uploads
def upload(name, relpath):
    fpath = os.path.join(ROOT, relpath)
    with open(fpath, "rb") as f:
        content = f.read()
    boundary = "----qnfo%x" % int(time.time() * 1000)
    body = b""
    body += ("--%s\r\n" % boundary).encode()
    body += ('Content-Disposition: form-data; name="name"\r\n\r\n%s\r\n' % name).encode()
    body += ("--%s\r\n" % boundary).encode()
    body += ('Content-Disposition: form-data; name="file"; filename="%s"\r\n' % name).encode()
    body += b"Content-Type: application/octet-stream\r\n\r\n"
    body += content + b"\r\n"
    body += ("--%s--\r\n" % boundary).encode()
    return req("POST", "/api/deposit/depositions/%s/files" % DRAFT,
               raw=body, ctype="multipart/form-data; boundary=%s" % boundary)

uploads = [
    ("README.md", "README.md"),
    ("post-positional-numeracy.md", "post-positional-numeracy.md"),
    ("post-positional-numeracy.html", "post-positional-numeracy.html"),
    ("post-positional-numeracy.pdf", "post-positional-numeracy.pdf"),
    ("upload-publish.log", "artifacts/external-search/p5-publish/upload-publish.log"),
    ("publish-response.json", "artifacts/external-search/p5-publish/publish-response.json"),
    ("verify-newversion.json", "artifacts/external-search/p5-publish/verify-newversion.json"),
    ("verify-newversion.log", "artifacts/external-search/p5-publish/verify-newversion.log"),
    ("upload-publish.py", "artifacts/external-search/p5-publish/upload-publish.py"),
    ("verify-and-newversion.py", "artifacts/external-search/p5-publish/verify-and-newversion.py"),
    ("replace-publish-v101.py", "artifacts/external-search/p5-publish/replace-publish-v101.py"),
    ("replace2.py", "artifacts/external-search/p5-publish/replace2.py"),
    ("replace3.py", "artifacts/external-search/p5-publish/replace3.py"),
    ("deldiag2.py", "artifacts/external-search/p5-publish/deldiag2.py"),
]
for name, rel in uploads:
    st3, b3 = upload(name, rel)
    print("UPLOAD", st3, name)
    if st3 not in (200, 201):
        print(json.dumps(b3)[:400])
        sys.exit(1)
    time.sleep(0.4)

# 3. metadata PUT v1.0.1 (full object — PARTIAL-PUT-CLEARS-FIELDS-1)
desc = json.load(open(os.path.join(ROOT, "artifacts/external-search/p5-publish/deposit-create.json"), encoding="utf-8"))["body"]["metadata"]["description"]
metadata = {
    "title": "Post-Positional Numeracy: Finite-Adele Encoding and Product-Formula-Verified Exact Rational Arithmetic",
    "upload_type": "publication",
    "publication_type": "preprint",
    "publication_date": "2026-08-26",
    "description": desc,
    "access_right": "open",
    "license": "CC-BY-4.0",
    "creators": [{"name": "Quni-Gudzinas, Rowan Brad", "affiliation": "QNFO"}],
    "keywords": [
        "finite adeles", "Hensel codes", "product formula", "exact rational arithmetic",
        "Ostrowski's theorem", "rational reconstruction", "non-Archimedean", "numeration",
    ],
    "related_identifiers": [
        {"scheme": "url", "relation": "isSupplementTo",
         "identifier": "https://github.com/QNFO/qnfo-research/tree/res/paper/post-positional-numeracy"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.5281/zenodo.20756222"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.5281/zenodo.21148596"},
        {"scheme": "doi", "relation": "cites", "identifier": "10.1016/j.jsc.2025.102481"},
    ],
    "version": "1.0.1",
}
st4, m4 = req("PUT", "/api/deposit/depositions/%s" % DRAFT, body={"metadata": metadata})
print("METADATA PUT", st4, "version:", m4.get("metadata", {}).get("version") if isinstance(m4, dict) else m4)

# 4. publish
st5, p5 = req("POST", "/api/deposit/depositions/%s/actions/publish" % DRAFT, raw=b"")
print("PUBLISH", st5, "doi:", p5.get("doi"))
with open(os.path.join(HERE, "publish-v101-response.json"), "w", encoding="utf-8") as f:
    json.dump({"status": st5, "body": p5}, f, indent=1, ensure_ascii=False)
