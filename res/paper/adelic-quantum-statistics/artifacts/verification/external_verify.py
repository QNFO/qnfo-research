import json, time, socket, ssl, urllib.request, urllib.error

UA = {"User-Agent": "QNFO-Research/1.0 (mailto:rwnquni@outlook.com)"}

def get(url, tries=6):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(2 + 3 * i)
    return "ERROR: %r" % last

checks = [
    ("zenodo-record-21939596-concept", "https://zenodo.org/api/records/21939596"),
    ("zenodo-record-21964359-concept", "https://zenodo.org/api/records/21964359"),
    ("openalex-arxiv-2306.05919", "https://api.openalex.org/works/doi:10.48550/arXiv.2306.05919"),
    ("openalex-arxiv-2308.05203", "https://api.openalex.org/works/doi:10.48550/arXiv.2308.05203"),
    ("openalex-arxiv-2505.17361", "https://api.openalex.org/works/doi:10.48550/arXiv.2505.17361"),
    ("crossref-zenodo-21964598", "https://api.crossref.org/works/10.5281/zenodo.21964598"),
]

out = []
for name, url in checks:
    txt = get(url)
    out.append("=" * 80)
    out.append("CHECK: " + name + " | " + url)
    try:
        d = json.loads(txt)
        if name.startswith("zenodo-record"):
            out.append("  conceptrecid=%s | doi=%s | title=%s" % (
                d.get("conceptrecid"), d.get("doi"),
                (d.get("metadata", {}).get("title") or "?")[:90]))
        elif name.startswith("openalex"):
            w = d
            out.append("  title=%s | cited_by=%s | year=%s | type=%s" % (
                (w.get("title") or "?")[:100], w.get("cited_by_count"),
                w.get("publication_year"), w.get("type")))
        elif name.startswith("crossref"):
            m = d.get("message", {})
            out.append("  title=%s | container=%s | published=%s" % (
                (m.get("title") or ["?"])[0][:100],
                (m.get("container-title") or ["?"])[0][:60],
                m.get("published", {}).get("date-parts")))
    except Exception as e:
        out.append("  PARSE-ERROR %r | RAW: %s" % (e, txt[:200]))
    out.append("")

open(r"C:\Users\LENOVO\AppData\Local\Temp\res027_external_verify.txt", "w", encoding="utf-8").write("\n".join(out))
print("WROTE res027_external_verify.txt")
