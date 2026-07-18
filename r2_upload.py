"""Upload all 10 core pillar files to R2 via r2-gateway Worker."""
import os, json, requests

CF_TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN", "")
GATEWAY = "https://r2-gateway.q08.workers.dev/write"
BUCKET = "qnfo-releases"

with open("releases/core-pillars/ipfs-cids.json") as f:
    cids = json.load(f)

uploaded = 0
for entry in cids:
    slug = entry["slug"]
    fname = entry["file"]
    
    # Map slug to directory
    dir_map = {
        "silent-radix": "silent-radix",
        "syntactic-primitive": "syntactic-primitive",
        "qubit-delusion": "qubit-delusion",
        "beyond-qubit": "beyond-qubit",
        "ultrametric": "ultrametric-foundations",
    }
    subdir = dir_map.get(slug, slug)
    
    local_path = f"releases/core-pillars/{subdir}/{fname}"
    r2_key = f"releases/2026/07/core-pillars/{slug}/{fname}"
    
    if not os.path.exists(local_path):
        print(f"MISSING: {local_path}")
        continue
    
    with open(local_path, "rb") as f:
        data = f.read()
    
    ext = os.path.splitext(fname)[1]
    content_type = "application/pdf" if ext == ".pdf" else "text/markdown"
    
    print(f"Uploading: {r2_key} ({len(data):,}B)...", end=" ", flush=True)
    
    try:
        r = requests.post(
            GATEWAY,
            params={"key": r2_key, "bucket": BUCKET},
            data=data,
            headers={
                "Content-Type": content_type,
                "X-Auth-Token": CF_TOKEN,
            },
            timeout=30,
        )
        if r.status_code in (200, 201):
            print(f"OK")
            uploaded += 1
        else:
            print(f"FAIL ({r.status_code}): {r.text[:200]}")
    except Exception as e:
        print(f"ERROR: {e}")

print(f"\nUploaded {uploaded}/{len(cids)} files to R2")
