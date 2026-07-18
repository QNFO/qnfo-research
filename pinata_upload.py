"""Pin all 5 core pillar papers (10 files: 5 MD + 5 PDF) to Pinata IPFS."""
import os, sys, json, requests

PINATA_KEY = os.environ["PINATA_API_KEY"]
PINATA_SECRET = os.environ["PINATA_API_SECRET"]
PINATA_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"

papers = [
    ("silent-radix", "releases/core-pillars/silent-radix/silent-radix-cryptography.pdf"),
    ("silent-radix", "releases/core-pillars/silent-radix/silent-radix-cryptography.md"),
    ("syntactic-primitive", "releases/core-pillars/syntactic-primitive/syntactic-generation-primitive-distinctions.pdf"),
    ("syntactic-primitive", "releases/core-pillars/syntactic-primitive/syntactic-generation-primitive-distinctions.md"),
    ("qubit-delusion", "releases/core-pillars/qubit-delusion/the-qubit-delusion.pdf"),
    ("qubit-delusion", "releases/core-pillars/qubit-delusion/the-qubit-delusion.md"),
    ("beyond-qubit", "releases/core-pillars/beyond-qubit/beyond-the-qubit.pdf"),
    ("beyond-qubit", "releases/core-pillars/beyond-qubit/beyond-the-qubit.md"),
    ("ultrametric", "releases/core-pillars/ultrametric-foundations/number-theoretic-ultrametric-foundations.pdf"),
    ("ultrametric", "releases/core-pillars/ultrametric-foundations/number-theoretic-ultrametric-foundations.md"),
]

results = []
for slug, fpath in papers:
    fname = os.path.basename(fpath)
    fsize = os.path.getsize(fpath)
    print(f"Uploading {fname} ({fsize:,} bytes)...", end=" ", flush=True)
    with open(fpath, "rb") as f:
        metadata = json.dumps({
            "name": f"{slug}/{fname}",
            "keyvalues": {"slug": slug, "date": "2026/07"},
        })
        r = requests.post(
            PINATA_URL,
            files={"file": (fname, f)},
            data={"pinataMetadata": metadata},
            headers={
                "pinata_api_key": PINATA_KEY,
                "pinata_secret_api_key": PINATA_SECRET,
            },
            timeout=120,
        )
        if r.status_code == 200:
            cid = r.json()["IpfsHash"]
            print(f"OK -> {cid}")
            results.append({"slug": slug, "file": fname, "cid": cid, "size": fsize})
        else:
            print(f"FAIL ({r.status_code}): {r.text[:200]}")

print()
print("=== RESULTS ===")
for r in results:
    print(f"  {r['slug']}/{r['file']} -> {r['cid']} ({r['size']:,}B)")

with open("releases/core-pillars/ipfs-cids.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved {len(results)} CIDs to releases/core-pillars/ipfs-cids.json")
