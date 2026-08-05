import urllib.request, json

# Key DOIs to verify
dois = [
    "10.1176/appi.books.9780890425596",  # DSM-5
    "10.1016/S0140-6736(18)30142-9",     # Cacioppo Lancet
    "10.1177/1745691614568352",          # Holt-Lunstad
    "10.1145/3571730",                   # Ji et al. hallucination survey
    "10.1145/365153.365168",             # Weizenbaum ELIZA
]

for doi in dois:
    try:
        url = f"https://api.crossref.org/works/{doi}"
        req = urllib.request.Request(url, headers={"User-Agent": "QNFO/1.0 (mailto:alerts@qnfo.org)"})
        r = urllib.request.urlopen(req)
        data = json.loads(r.read())
        msg = data.get("message", {})
        title = msg.get("title", ["N/A"])[0] if msg.get("title") else "N/A"
        authors = [f"{a.get('family','')}, {a.get('given','')}" for a in msg.get("author", [])]
        year = msg.get("issued", {}).get("date-parts", [[0]])[0][0]
        print(f"DOI: {doi}")
        print(f"  Title: {title[:100]}...")
        print(f"  Year: {year}")
        print(f"  Authors: {', '.join(authors[:3])}{'...' if len(authors)>3 else ''}")
        print()
    except Exception as e:
        print(f"DOI: {doi} -> ERROR: {e}")
        print()
