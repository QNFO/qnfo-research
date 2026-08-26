# -*- coding: utf-8 -*-
"""verify-published.py — QNFO.RES.024 post-publish verification (POST-PUBLISH-FRONTMATTER-ASSERT-1 + layout)."""
import json, os, re, socket, ssl, subprocess, sys, time, urllib.error, urllib.request

BASE_HOST = "zenodo.org"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
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

def get_text(path, tries=4):
    h = {"User-Agent": UA, "Accept": "application/json",
         "Accept-Language": "en-US,en;q=0.9", "Host": BASE_HOST}
    url = "https://" + IP + path
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, headers=h)
            with opener.open(r, timeout=120) as resp:
                return resp.status, resp.read().decode("utf-8")
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    return -1, str(last)

def get_json(path, tries=4):
    st, txt = get_text(path, tries)
    try:
        return st, json.loads(txt)
    except Exception:
        return st, {"__raw__": txt[:200]}

fails = []

def check(name, ok, detail):
    print(("PASS" if ok else "FAIL"), name, "-", detail)
    if not ok:
        fails.append(name)

# 1. records state
st, rec = get_json("/api/records/%s" % REC)
check("RECORD-STATE", st == 200 and rec.get("state") == "done",
      "status=%s state=%s version=%s files=%d" % (st, rec.get("state"),
      rec.get("metadata", {}).get("version"), len(rec.get("files", []))))

# 2. DataCite findable
st, dc = get_json("https://api.datacite.org/dois/10.5281/zenodo.22114495".replace("https://api.datacite.org", "https://api.datacite.org"))
check("DATACITE-FINDABLE", st == 200 and dc.get("data", {}).get("attributes", {}).get("state") == "findable",
      "status=%s state=%s" % (st, dc.get("data", {}).get("attributes", {}).get("state")))

# 3. deposited .md frontmatter assert
st, md = get_text("/api/records/%s/files/post-positional-numeracy.md/content" % REC)
doi_ok = 'doi: "10.5281/zenodo.22114495"' in md
ver_ok = 'version: "1.0.1"' in md
status_ok = 'status: "published"' in md
check("FRONTMATTER-DOI", st == 200 and doi_ok, "md status=%s doi_match=%s" % (st, doi_ok))
check("FRONTMATTER-VERSION", ver_ok, "version 1.0.1 in deposited md")
check("FRONTMATTER-STATUS", status_ok, "status published in deposited md")

# 4. README reproduce + cite check
st, rm = get_text("/api/records/%s/files/README.md/content" % REC)
check("README-REPRODUCE", "python verify_ppn.py" in rm, "flat reproduce command present")
check("README-CONCEPT-CITE", "10.5281/zenodo.22114388" in rm, "concept DOI in How-to-cite")
check("README-RECORD-CITE", "10.5281/zenodo.22114495" in rm, "v1.0.1 record DOI in How-to-cite")

out = {"record": REC, "state": rec.get("state") if isinstance(rec, dict) else None,
       "version": rec.get("metadata", {}).get("version") if isinstance(rec, dict) else None,
       "nfiles": len(rec.get("files", [])) if isinstance(rec, dict) and isinstance(rec.get("files"), list) else None,
       "all_pass": not fails, "failures": fails}
with open(os.path.join(HERE, "verify-published.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print("ALL PASS" if not fails else "FAILURES: %s" % fails)
sys.exit(0 if not fails else 1)
