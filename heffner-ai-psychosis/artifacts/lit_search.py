import urllib.request, json, sys

q = "chatbot+AI+depression+mental+health+effects"
url = f"https://api.openalex.org/works?search={q}&mailto=alerts@qnfo.org&per_page=10"
req = urllib.request.Request(url, headers={"User-Agent": "QNFO/1.0 (mailto:alerts@qnfo.org)"})
r = urllib.request.urlopen(req)
data = json.loads(r.read())
for w in data.get("results", []):
    title = w.get("title", "N/A")
    doi = w.get("doi", "")
    year = w.get("publication_year", "")
    src = w.get("primary_location", {}).get("source", {}).get("display_name", "")
    print(f"[{year}] {title}")
    print(f"  DOI: {doi} | Source: {src}")
    print()
