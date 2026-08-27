# -*- coding: utf-8 -*-
"""upload_res027_files.py — QNFO.RES.027 P8: upload the flat deposit file set (2026-08-27).

Bucket PUT per file, application/octet-stream + access_token (ZENODO-BUCKET-PUT-415-1);
flat basename keys (the deposit layout is flat; scripts are layout-agnostic).
"""
import json, os, time, urllib.request, urllib.error

TOKEN = os.environ.get("ZENODO_TOKEN") or open(r"C:\Users\LENOVO\tokens\zenodo", encoding="utf-8").read().strip()
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
VER = os.path.join(PAPER, "artifacts", "verification")
EXT = os.path.join(PAPER, "artifacts", "external-search")
PUB = os.path.join(EXT, "p5-publish")
ART = os.path.join(PAPER, "artifacts")

FILES = [
    "adelic-quantum-statistics.md", "adelic-quantum-statistics.html", "adelic-quantum-statistics.pdf",
    "references.bib", "citation-audit.md", "PROJECT-PLAN.md", "DUE-DILIGENCE.md", "OUTLINE.md",
    "README.md", "LICENSE",
    "verify_stats.py", "verify_product_formula.py", "verify_parastats.py",
    "verify_rate_gamma.py", "verify_symplectic.py", "verify_maxent.py",
    "check_rendering.py", "render-pdf.cjs", "external_verify.py",
    "verify_stats_run-2026-08-27.txt", "verify_product_formula_run-2026-08-27.txt",
    "verify_parastats_run-2026-08-27.txt", "verify_rate_gamma_run-2026-08-27.txt",
    "verify_symplectic_run-2026-08-27.txt", "verify_maxent_run-2026-08-27.txt",
    "verify_stats_results.json", "verify_product_formula_results.json",
    "verify_parastats_results.json", "verify_rate_gamma_results.json",
    "verify_symplectic_results.json", "verify_maxent_results.json",
    "f4-differential-primon-gas-audit.py", "f4-differential-primon-gas-audit.json",
    "external-verify-2026-08-27.txt", "crossref-verify-2026-08-27.txt", "doi-check-2026-08-27.txt",
    "ignorance-audit.md", "red-team-2026-08-27.md",
    "deposit-create.json", "deposit-reserve-doi.json", "deposit-summary.json", "run_create.txt",
]

def locate(basename):
    for d in (PAPER, VER, EXT, PUB, ART):
        p = os.path.join(d, basename)
        if os.path.exists(p):
            return p
    return None

def put(url, data, tries=6):
    last = None
    for i in range(tries):
        try:
            r = urllib.request.Request(url, data=data, method="PUT", headers={
                "User-Agent": UA, "Content-Type": "application/octet-stream",
            })
            with urllib.request.urlopen(r, timeout=120) as resp:
                return resp.status, resp.read().decode("utf-8", "replace")[:120]
        except urllib.error.HTTPError as e:
            last = (e.code, e.read().decode("utf-8", "replace")[:200])
            if e.code in (415, 429, 500, 502, 503, 504):
                time.sleep(3 + 4 * i)
                continue
            return e.code, last[1]
        except Exception as e:
            last = ("NET", str(e))
            time.sleep(3 + 4 * i)
    return (0, last)

dep = json.load(open(os.path.join(PUB, "deposit-create.json"), encoding="utf-8"))["body"]
bucket = dep["links"]["bucket"]

results = []
ok = 0
for fn in FILES:
    p = locate(fn)
    if p is None:
        results.append({"file": fn, "status": "MISSING", "detail": ""})
        continue
    data = open(p, "rb").read()
    url = "%s/%s?access_token=%s" % (bucket, fn, TOKEN)
    st, detail = put(url, data)
    results.append({"file": fn, "status": st, "detail": detail})
    if st in (200, 201):
        ok += 1
    print("%s -> %s" % (fn, st))

summary = {"uploaded": ok, "total": len(FILES), "results": results}
json.dump(summary, open(os.path.join(PUB, "upload-summary.json"), "w"), indent=1, ensure_ascii=False)
print("UPLOADED %d/%d" % (ok, len(FILES)))
