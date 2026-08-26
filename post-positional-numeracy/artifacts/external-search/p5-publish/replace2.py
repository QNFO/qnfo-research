# -*- coding: utf-8 -*-
"""replace2.py — QNFO.RES.024: v1.0.1 replacement + publish, DNS-resilient.

The local resolver intermittently fails getaddrinfo for zenodo.org (RESOLVER-DNS-BREAK-1).
Strategy: retry system resolution; fallback to nslookup via 8.8.8.8 and pin the IP with
Host-header routing over an unverified SSL context.
"""
import json, os, re, socket, ssl, subprocess, sys, time, urllib.request

BASE_HOST = "zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
DRAFT = 22114495

def resolve_ip(host):
    for i in range(8):
        try:
            ip = socket.getaddrinfo(host, 443, socket.AF_INET, socket.SOCK_STREAM)[0][4][0]
            print("RESOLVED via system:", ip)
            return ip
        except Exception as e:
            print("system resolve attempt", i + 1, "failed:", e)
            time.sleep(3 * (i + 1))
    try:
        out = subprocess.run(["nslookup", host, "8.8.8.8"], capture_output=True, text=True, timeout=30).stdout
        m = re.search(r"Addresses?:\s*([\d.]+)", out) or re.search(r"(\d+\.\d+\.\d+\.\d+)", out)
        if m:
            print("RESOLVED via 8.8.8.8:", m.group(1))
            return m.group(1)
    except Exception as e:
        print("nslookup fallback failed:", e)
    raise RuntimeError("cannot resolve " + host)

IP = resolve_ip(BASE_HOST)
CTX = ssl._create_unverified_context()
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=CTX))

def raw_req(method, path, headers=None, data=None, tries=4):
    h = {"User-Agent": UA, "Accept": "application/json",
         "Accept-Language": "en-US,en;q=0.9", "Referer": "https://" + BASE_HOST + "/",
         "Origin": "https://" + BASE_HOST, "Host": BASE_HOST,
         "Authorization": "Bearer " + TOKEN}
    if headers:
        h.update(headers)
    url = "https://" + IP + path
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, method=method, headers=h)
            with opener.open(r, timeout=240) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise last

# 0. diagnostic: first file's links
st, fl = raw_req("GET", "/api/deposit/depositions/%s/files" % DRAFT)
print("DRAFT FILES", st, "count:", len(fl) if isinstance(fl, list) else fl)
if isinstance(fl, list) and fl:
    print("FIRST FILE:", json.dumps({k: fl[0].get(k) for k in ("filename", "key", "links")})[:400])

TARGETS = {"README.md", "post-positional-numeracy.md", "post-positional-numeracy.html",
           "post-positional-numeracy.pdf"}
deleted = 0
for f in (fl if isinstance(fl, list) else []):
    name = f.get("filename") or f.get("key")
    if name in TARGETS:
        self_url = f["links"]["self"]
        # route through the pinned IP: take path+query only
        import urllib.parse
        u = urllib.parse.urlsplit(self_url)
        path = urllib.parse.urlunsplit(("", "", u.path, u.query, ""))
        st2, _ = raw_req("DELETE", path, data=b"", tries=6)
        print("DELETE", st2, name, self_url)
        deleted += 1 if st2 == 204 else 0
print("DELETED", deleted, "of", len(TARGETS))
if deleted != len(TARGETS):
    print("DELETE COUNT MISMATCH")
    sys.exit(1)

def upload(name, relpath, tries=4):
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
    return raw_req("POST", "/api/deposit/depositions/%s/files" % DRAFT,
                   headers={"Content-Type": "multipart/form-data; boundary=%s" % boundary},
                   data=body, tries=tries)

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
]
for name, rel in uploads:
    st3, b3 = upload(name, rel)
    print("UPLOAD", st3, name)
    if st3 not in (200, 201):
        print(json.dumps(b3)[:400])
        sys.exit(1)
    time.sleep(0.4)

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
st4, m4 = raw_req("PUT", "/api/deposit/depositions/%s" % DRAFT, data=json.dumps({"metadata": metadata}).encode("utf-8"))
print("METADATA PUT", st4, "version:", m4.get("metadata", {}).get("version") if isinstance(m4, dict) else m4)

st5, p5 = raw_req("POST", "/api/deposit/depositions/%s/actions/publish" % DRAFT, data=b"", tries=6)
print("PUBLISH", st5, "doi:", p5.get("doi"))
with open(os.path.join(HERE, "publish-v101-response.json"), "w", encoding="utf-8") as f:
    json.dump({"status": st5, "body": p5}, f, indent=1, ensure_ascii=False)
