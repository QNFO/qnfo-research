# -*- coding: utf-8 -*-
"""deldiag3.py — probe delete state: are targets present? what do 404 bodies say? test records-API key-form DELETE."""
import json, os, re, socket, ssl, subprocess, time, urllib.error, urllib.parse, urllib.request

BASE_HOST = "zenodo.org"
TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))

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
    raise RuntimeError("cannot resolve")

IP = resolve_ip(BASE_HOST)
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl._create_unverified_context()))

def req(method, path, raw=None, tries=4):
    h = {"User-Agent": UA, "Accept": "application/json",
         "Accept-Language": "en-US,en;q=0.9", "Referer": "https://" + BASE_HOST + "/",
         "Origin": "https://" + BASE_HOST, "Host": BASE_HOST,
         "Authorization": "Bearer " + TOKEN}
    url = "https://" + IP + path
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=raw, method=method, headers=h)
            with opener.open(r, timeout=120) as resp:
                return resp.status, json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode("utf-8") if e.fp else b"{}")
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    return -1, {"__error__": str(last)}

st, fl = req("GET", "/api/deposit/depositions/22114495/files")
names = [f.get("filename") or f.get("key") for f in fl] if isinstance(fl, list) else fl
print("DEPOSIT LIST count:", len(names) if isinstance(names, list) else names)
for t in ("post-positional-numeracy.md", "post-positional-numeracy.html", "post-positional-numeracy.pdf", "README.md"):
    print("  present?", t, t in names if isinstance(names, list) else "?")

# deposit-API delete one target, show body
if isinstance(fl, list):
    for f in fl:
        name = f.get("filename") or f.get("key")
        if name == "post-positional-numeracy.md":
            st2, b2 = req("DELETE", f["links"]["self"].replace("https://" + BASE_HOST, ""), raw=b"")
            print("DEPOSIT-DELETE md:", st2, json.dumps(b2)[:300])
            break

# records-API key-form delete test on post-positional-numeracy.md
st3, b3 = req("DELETE", "/api/records/22114495/draft/files/post-positional-numeracy.md", raw=b"")
print("RECORDS-DELETE md:", st3, json.dumps(b3)[:300] if b3 else b3)

# re-list both
st4, fl4 = req("GET", "/api/deposit/depositions/22114495/files")
n4 = [f.get("filename") or f.get("key") for f in fl4] if isinstance(fl4, list) else fl4
print("DEPOSIT LIST after:", len(n4) if isinstance(n4, list) else n4)
print("  md present?", "post-positional-numeracy.md" in n4 if isinstance(n4, list) else "?")
