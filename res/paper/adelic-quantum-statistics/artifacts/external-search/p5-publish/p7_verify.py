# -*- coding: utf-8 -*-
"""p7_verify.py — fetch the qnfo-email API key + verify target addresses from arXiv sources."""
import json, os, re, tarfile, gzip, io, urllib.request, time

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
CF_TOKEN = open(r"C:\Users\LENOVO\tokens\cloudflare", encoding="utf-8").read().strip()
CF_ACCT = "edb167b78c9fb901ea5bca3ce58ccc4b"
OUT = r"C:\Users\LENOVO\Projects\qnfo-research\res\paper\adelic-quantum-statistics\artifacts\external-search\p5-publish"

def get(url, headers, tries=5):
    for i in range(tries):
        try:
            r = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(r, timeout=60) as resp:
                return resp.status, resp.read()
        except Exception as e:
            time.sleep(3 + 4 * i)
    return (0, b"")

# 1. API key from bindings
st, body = get(
    "https://api.cloudflare.com/client/v4/accounts/%s/workers/scripts/qnfo-email/bindings" % CF_ACCT,
    {"Authorization": "Bearer " + CF_TOKEN, "Content-Type": "application/json"})
key = None
if st == 200:
    j = json.loads(body.decode())
    for b in j.get("result", []):
        if b.get("name") == "API_KEY" and b.get("type") == "secret_text":
            key = b.get("text") or b.get("value")
print("BINDINGS", st, "key found:", bool(key), "key tail:", (key[-14:] if key else None))
if key:
    open(os.path.join(OUT, "send-api-key.txt"), "w").write(key)
    # sanity: /health with the key
    st2, b2 = get("https://qnfo-email.q08.workers.dev/health", {"Authorization": "Bearer " + key, "User-Agent": UA})
    print("HEALTH", st2, b2[:120])

# 2. arXiv e-print sources: grep for emails
EMAIL_RE = re.compile(rb"[\w.+-]+@[\w.-]+\.[a-z]{2,}")
for aid in ("2306.05919", "2502.02661", "2308.05203", "2505.17361"):
    st, raw = get("https://arxiv.org/e-print/%s" % aid, {"User-Agent": UA})
    emails = set()
    text = ""
    try:
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tf:
            for m in tf.getmembers():
                f = tf.extractfile(m)
                if f:
                    text += f.read().decode("utf-8", "replace")
    except Exception:
        try:
            text = gzip.decompress(raw).decode("utf-8", "replace")
        except Exception:
            try:
                text = raw.decode("utf-8", "replace")
            except Exception:
                text = ""
    for e in EMAIL_RE.findall(text.encode("utf-8", "replace")):
        s = e.decode()
        if any(d in s for d in ("example", "invalid", "email.com", "arxiv", "domain.com", "correspondence@", "submission@", "perl", "sphinx")):
            continue
        emails.add(s)
    print("EPRINT", aid, "status", st, "emails:", sorted(emails)[:8])
