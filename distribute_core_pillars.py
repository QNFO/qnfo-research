#!/usr/bin/env python3
"""Distribute 5 core pillar papers: IPFS (Pinata) + R2 + DNSLink prep.

PAPERS:
  1. silent-radix-cryptography      DOI: 10.5281/zenodo.21134188
  2. syntactic-primitive-distinctions DOI: (none yet)
  3. the-qubit-delusion             DOI: 10.5281/zenodo.21254143
  4. beyond-the-qubit               DOI: 10.5281/zenodo.21254901
  5. number-theoretic-ultrametric   DOI: 10.5281/zenodo.21193487

Requirements: pip install requests boto3 pyperclip
Env: PINATA_API_KEY, PINATA_API_SECRET, CLOUDFLARE_API_TOKEN
"""

import os
import sys
import json
import hashlib
import requests
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent
PAPERS = [
    {
        "slug": "silent-radix-cryptography",
        "dir": "silent-radix",
        "title": "Silent-Radix Cryptography",
        "doi": "10.5281/zenodo.21134188",
        "files": ["silent-radix-cryptography.md", "silent-radix-cryptography.pdf"],
    },
    {
        "slug": "syntactic-generation-primitive-distinctions",
        "dir": "syntactic-primitive",
        "title": "Syntactic Generation Primitive Distinctions",
        "doi": None,
        "files": ["syntactic-generation-primitive-distinctions.md", "syntactic-generation-primitive-distinctions.pdf"],
    },
    {
        "slug": "the-qubit-delusion",
        "dir": "qubit-delusion",
        "title": "The Qubit Delusion",
        "doi": "10.5281/zenodo.21254143",
        "files": ["the-qubit-delusion.md", "the-qubit-delusion.pdf"],
    },
    {
        "slug": "beyond-the-qubit",
        "dir": "beyond-qubit",
        "title": "Beyond the Qubit",
        "doi": "10.5281/zenodo.21254901",
        "files": ["beyond-the-qubit.md", "beyond-the-qubit.pdf"],
    },
    {
        "slug": "number-theoretic-ultrametric-foundations",
        "dir": "ultrametric-foundations",
        "title": "Number-Theoretic Ultrametric Foundations",
        "doi": "10.5281/zenodo.21193487",
        "files": ["number-theoretic-ultrametric-foundations.md", "number-theoretic-ultrametric-foundations.pdf"],
    },
]

PINATA_KEY = os.environ.get("PINATA_API_KEY", "")
PINATA_SECRET = os.environ.get("PINATA_API_SECRET", "")
CF_TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN", "")
PINATA_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"
PINATA_LIST = "https://api.pinata.cloud/data/pinList"
DATE = datetime.now().strftime("%Y/%m")


def pin_to_ipfs(filepath: Path, slug: str) -> dict | None:
    """Upload a single file to Pinata IPFS."""
    if not PINATA_KEY:
        print(f"  SKIP (no PINATA_API_KEY): {filepath.name}")
        return None
    try:
        with open(filepath, "rb") as f:
            files = {"file": (filepath.name, f)}
            metadata = json.dumps({
                "name": f"{slug}/{filepath.name}",
                "keyvalues": {
                    "slug": slug,
                    "type": filepath.suffix.replace(".", ""),
                    "date": DATE,
                }
            })
            headers = {
                "pinata_api_key": PINATA_KEY,
                "pinata_secret_api_key": PINATA_SECRET,
            }
            resp = requests.post(
                PINATA_URL,
                files=files,
                data={"pinataMetadata": metadata},
                headers=headers,
                timeout=60,
            )
            if resp.status_code == 200:
                data = resp.json()
                cid = data.get("IpfsHash", "")
                print(f"  PINNED: {filepath.name} → {cid}")
                return {"cid": cid, "size": filepath.stat().st_size}
            else:
                print(f"  FAIL ({resp.status_code}): {resp.text[:200]}")
                return None
    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def upload_to_r2(filepath: Path, slug: str) -> bool:
    """Upload file to Cloudflare R2 bucket 'qnfo'."""
    if not CF_TOKEN:
        print(f"  SKIP (no CLOUDFLARE_API_TOKEN): {filepath.name}")
        return False
    # R2 endpoint via Workers or direct S3 API
    # For now, try S3-compatible API
    try:
        import boto3
        s3 = boto3.client(
            "s3",
            endpoint_url="https://<account>.r2.cloudflarestorage.com",
            aws_access_key_id=os.environ.get("R2_ACCESS_KEY_ID", ""),
            aws_secret_access_key=os.environ.get("R2_SECRET_ACCESS_KEY", ""),
        )
        key = f"releases/{DATE}/core-pillars/{slug}/{filepath.name}"
        s3.upload_file(str(filepath), "qnfo", key)
        print(f"  R2: {key}")
        return True
    except Exception as e:
        print(f"  R2 SKIP (no R2 creds or error): {e}")
        return False


def main():
    print(f"DISTRIBUTION PIPELINE — {datetime.now().isoformat()}")
    print(f"Pinata key: {'✓' if PINATA_KEY else '✗ MISSING'}")
    print(f"CF token:   {'✓' if CF_TOKEN else '✗ MISSING'}")
    print()

    results = []

    for p in PAPERS:
        print(f"--- {p['title']} ---")
        print(f"  Slug: {p['slug']}")
        print(f"  DOI:  {p['doi'] or '(none)'}")

        paper_dir = BASE / "releases" / "core-pillars" / p["dir"]
        if not paper_dir.exists():
            print(f"  SKIP: directory not found: {paper_dir}")
            continue

        ipfs_cids = {}
        for fname in p["files"]:
            fpath = paper_dir / fname
            if not fpath.exists():
                print(f"  MISSING: {fname}")
                continue
            print(f"  File: {fname} ({fpath.stat().st_size:,} bytes)")
            result = pin_to_ipfs(fpath, p["slug"])
            if result:
                ipfs_cids[fname] = result["cid"]

            # R2 upload
            upload_to_r2(fpath, p["slug"])

        results.append({
            "slug": p["slug"],
            "title": p["title"],
            "doi": p["doi"],
            "ipfs_cids": ipfs_cids,
        })
        print()

    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for r in results:
        print(f"\n{r['title']}")
        print(f"  DOI: {r['doi'] or '(needs Zenodo deposit)'}")
        for fname, cid in r["ipfs_cids"].items():
            print(f"  IPFS: {cid} → {fname}")
            if fname.endswith(".pdf"):
                print(f"  URL:  https://gateway.pinata.cloud/ipfs/{cid}")
                print(f"  DNSLink: _dnslink.{r['slug']}.qnfo.org TXT \"dnslink=/ipfs/{cid}\"")

    # Save results for next step
    outpath = BASE / "releases" / "core-pillars" / "distribution-results.json"
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {outpath}")


if __name__ == "__main__":
    main()
