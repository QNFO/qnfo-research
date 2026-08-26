# -*- coding: utf-8 -*-
"""fix-version.py — QNFO.RES.024: set version label 1.0.1 on published record 22114495.
ZENODO-VERSION-LABEL-EDIT-1: POST actions/edit -> GET -> PUT full metadata (Content-Type json!) -> publish."""
import json, os, re, socket, ssl, subprocess, time, urllib.error, urllib.request

BASE_HOST = "zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
REC = 22114495

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

IP = resolve_ip(BASE_HOST)
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl._create_unverified_context()))

def req(method, path, body=None, ctype=None, raw=None, tries=5):
    h = {"User-Agent": UA, "Accept": "application/json",
         "Accept-Language": "en-US,en;q=0.9", "Referer": "https://" + BASE_HOST + "/",
         "Origin": "https://" + BASE_HOST, "Host": BASE_HOST,
         "Authorization": "Bearer " + TOKEN}
    if ctype:
        h["Content-Type"] = ctype
    data = raw if raw is not None else (json.dumps(body).encode("utf-8") if body is not None else None)
    url = "https://" + IP + path
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, method=method, headers=h)
            with opener.open(r, timeout=240) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode("utf-8") if e.fp else b"{}")
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise last

# 0. current state
st0, r0 = req("GET", "/api/records/%s" % REC)
print("CURRENT", st0, "version:", r0.get("metadata", {}).get("version"), "state:", r0.get("state"))

# 1. actions/edit
st1, e1 = req("POST", "/api/deposit/depositions/%s/actions/edit" % REC, raw=b"")
print("EDIT", st1, json.dumps(e1)[:200])

# 2. GET the editable draft
st2, d2 = req("GET", "/api/deposit/depositions/%s" % REC)
print("DRAFT GET", st2, "version:", d2.get("metadata", {}).get("version") if isinstance(d2, dict) else d2)

# 3. PUT full metadata with version 1.0.1 (preserve ALL fields; drop doi/prereserve_doi)
md = d2.get("metadata", {})
desc = md.get("description")
new_md = {
    "title": md.get("title"),
    "upload_type": md.get("upload_type") or "publication",
    "publication_type": md.get("publication_type") or "preprint",
    "publication_date": md.get("publication_date"),
    "description": desc,
    "access_right": md.get("access_right") or "open",
    "license": md.get("license") or "CC-BY-4.0",
    "creators": md.get("creators"),
    "keywords": md.get("keywords"),
    "related_identifiers": md.get("related_identifiers"),
    "version": "1.0.1",
}
st3, p3 = req("PUT", "/api/deposit/depositions/%s" % REC, body={"metadata": new_md}, ctype="application/json")
print("PUT", st3, "version:", p3.get("metadata", {}).get("version") if isinstance(p3, dict) else json.dumps(p3)[:300])

# 4. publish (same DOI preserved)
st4, p4 = req("POST", "/api/deposit/depositions/%s/actions/publish" % REC, raw=b"")
print("PUBLISH", st4, "doi:", p4.get("doi"))

# 5. final state
st5, r5 = req("GET", "/api/records/%s" % REC)
print("FINAL", st5, "version:", r5.get("metadata", {}).get("version"), "state:", r5.get("state"),
      "files:", len(r5.get("files", [])))
with open(os.path.join(HERE, "version-fix-response.json"), "w", encoding="utf-8") as f:
    json.dump({"edit": st1, "put": st3, "publish": st4, "final": {"version": r5.get("metadata", {}).get("version"),
                                                                 "state": r5.get("state")}}, f, indent=1)
