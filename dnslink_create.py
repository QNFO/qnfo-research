"""Create DNSLink TXT records for 5 core pillar papers via Cloudflare API."""
import os, requests

CF_TOKEN = os.environ["CLOUDFLARE_API_TOKEN"]
ZONE_ID = "d6d1e08f7e9405a9cfa3d8f4630c9b0c"  # qnfo.org

records = [
    ("_dnslink.silent-radix-cryptography", "QmbCbkjBj6aKgcSCRiZ7ewxUg3P6JAh2NKo4dCgLBKvgfS"),
    ("_dnslink.syntactic-generation-primitive-distinctions", "QmRLFE9iwokBuU1s4EYAkEUqGcABix1CnMBxcoht4n3JoH"),
    ("_dnslink.the-qubit-delusion", "QmZVcTQ4Szud3M1LULGLa1aWss55ciZk8db1QvwRC4wJt2"),
    ("_dnslink.beyond-the-qubit", "QmezmA2Ejo3t8DYGseFJhECrm2QCCaa3GQc2N7RMJSTuEw"),
    ("_dnslink.number-theoretic-ultrametric-foundations", "QmUtD9P2BDYMSaaz7WFTBPEmK9ViMkqj8iR6HjkWChm4i8"),
]

headers = {
    "Authorization": f"Bearer {CF_TOKEN}",
    "Content-Type": "application/json",
}

for name, cid in records:
    dnslink = f"dnslink=/ipfs/{cid}"
    print(f"Creating: {name}.qnfo.org -> {dnslink}...", end=" ", flush=True)
    
    r = requests.post(
        f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records",
        headers=headers,
        json={
            "type": "TXT",
            "name": name,
            "content": dnslink,
            "ttl": 3600,
            "comment": "Core pillar paper — WBS.3",
        },
        timeout=15,
    )
    data = r.json()
    if data.get("success"):
        rec_id = data["result"]["id"]
        print(f"OK (id: {rec_id})")
    else:
        errors = data.get("errors", [])
        if any("already exists" in str(e.get("message", "")) for e in errors):
            print("SKIP (already exists)")
        else:
            print(f"FAIL: {errors}")

print("\nDone.")
