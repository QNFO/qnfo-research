import json, urllib.request, datetime, os

# Weekly OpenCitations COCI monitor for QNFO.RES.009 (playbook D5).
# Baseline (2026-08-14): 0 citations for concept 10.5281/zenodo.21938970 and v1.1 10.5281/zenodo.21939493.
# Run weekly (1st of month or any 7-day cadence). Prints new citations since baseline.

UA = {"User-Agent": "QNFO-coci-monitor/1.0 (mailto:rowan.quni@outlook.com)"}
DOIS = [
    ("concept", "10.5281/zenodo.21938970"),
    ("v1.1", "10.5281/zenodo.21939493"),
]
OUT = r"C:\Users\LENOVO\source\repos\QNFO\qnfo-research\spin-statistics-distinction\artifacts\external-search"

def coci(doi):
    url = f"https://opencitations.net/index/coci/api/v1/citations/{doi}"
    r = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e)}

def main():
    ts = datetime.datetime.now(datetime.UTC).isoformat() + "Z"
    result = {"timestamp": ts}
    for label, doi in DOIS:
        j = coci(doi)
        n = len(j) if isinstance(j, list) else 0
        result[label] = {"doi": doi, "citations": n, "raw": j if n <= 20 else j[:20]}
        print(f"[{label}] {doi}: {n} citations")
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "coci-monitor.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, default=str)
    print("saved:", path)

if __name__ == "__main__":
    main()
