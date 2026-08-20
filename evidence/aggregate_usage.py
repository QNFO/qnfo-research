#!/usr/bin/env python3
"""Aggregate DeepSeek usage_data zips: tokens, requests, cost by month/model.
Evidence pack file for the $1,032 Research Program (10.5281/zenodo.22028851)."""
import csv, glob, io, json, os, zipfile
from collections import defaultdict

SRC = r"D:\usage_data_*.zip"
OUT = os.path.dirname(os.path.abspath(__file__))

zips = sorted(glob.glob(SRC))
print(f"Found {len(zips)} zips")

monthly = {}
models = set()
grand = defaultdict(lambda: defaultdict(int))

for z in zips:
    month = os.path.basename(z).replace("usage_data_", "").replace(".zip", "")
    monthly[month] = {}
    with zipfile.ZipFile(z) as zf:
        names = zf.namelist()
        amount_name = next(n for n in names if n.startswith("amount-"))
        cost_name = next(n for n in names if n.startswith("cost-"))
        with zf.open(amount_name) as f:
            raw = f.read().decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(raw))
            for row in reader:
                model = row["model"]
                typ = row["type"]
                amt = float(row["amount"]) if row["amount"] else 0
                models.add(model)
                m = monthly[month].setdefault(model, defaultdict(float))
                m[typ] += amt
                grand[model][typ] += amt
        with zf.open(cost_name) as f:
            raw = f.read().decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(raw))
            for row in reader:
                model = row["model"]
                c = float(row["cost"])
                m = monthly[month].setdefault(model, defaultdict(float))
                m["cost"] += c
                grand[model]["cost"] += c

def fmt(n):
    if n >= 1e9: return f"{n/1e9:,.2f}B"
    if n >= 1e6: return f"{n/1e6:,.1f}M"
    if n >= 1e3: return f"{n/1e3:,.1f}K"
    return f"{n:,.0f}"

result = {"months": {}, "grand": {}}
print("\n" + "=" * 100)
print("MONTHLY SUMMARY")
print("=" * 100)
for month in sorted(monthly):
    mdata = monthly[month]
    tot_cost = sum(v.get("cost", 0) for v in mdata.values())
    tot_req = sum(v.get("request_count", 0) for v in mdata.values())
    tot_out = sum(v.get("output_tokens", 0) for v in mdata.values())
    tot_in_hit = sum(v.get("input_cache_hit_tokens", 0) for v in mdata.values())
    tot_in_miss = sum(v.get("input_cache_miss_tokens", 0) for v in mdata.values())
    tot_in = tot_in_hit + tot_in_miss
    result["months"][month] = dict(
        cost=round(tot_cost, 2), requests=int(tot_req),
        input_tokens=int(tot_in), output_tokens=int(tot_out),
        input_cache_hit=int(tot_in_hit), input_cache_miss=int(tot_in_miss))
    print(f"{month}: ${tot_cost:>10,.2f} | req {fmt(tot_req):>10} | in {fmt(tot_in):>12} (hit {fmt(tot_in_hit)}, miss {fmt(tot_in_miss)}) | out {fmt(tot_out):>10}")

print("\n" + "=" * 100)
print("GRAND TOTALS BY MODEL")
print("=" * 100)
for model in sorted(grand):
    d = grand[model]
    tot_in = d["input_cache_hit_tokens"] + d["input_cache_miss_tokens"]
    tot_out = d["output_tokens"]
    result["grand"][model] = dict(
        cost=round(d["cost"], 2), requests=int(d["request_count"]),
        input_tokens=int(tot_in), output_tokens=int(tot_out),
        input_cache_hit=int(d["input_cache_hit_tokens"]),
        input_cache_miss=int(d["input_cache_miss_tokens"]))
    print(f"{model}: ${d['cost']:>10,.2f} | req {fmt(d['request_count']):>10} | "
          f"in {fmt(tot_in):>12} (hit {fmt(d['input_cache_hit_tokens'])}) | out {fmt(tot_out):>10}")

tot = defaultdict(float)
for model, d in grand.items():
    for k, v in d.items():
        tot[k] += v
tot_in = tot["input_cache_hit_tokens"] + tot["input_cache_miss_tokens"]
result["grand"]["__TOTAL__"] = dict(
    cost=round(tot["cost"], 2), requests=int(tot["request_count"]),
    input_tokens=int(tot_in), output_tokens=int(tot["output_tokens"]),
    input_cache_hit=int(tot["input_cache_hit_tokens"]),
    input_cache_miss=int(tot["input_cache_miss_tokens"]))
print("\n" + "=" * 100)
print(f"TOTAL (all models, {len(zips)} months):")
print(f"  Cost:          ${tot['cost']:,.2f} USD")
print(f"  Requests:      {fmt(tot['request_count'])}")
print(f"  Input tokens:  {fmt(tot_in)}  (cache hit {fmt(tot['input_cache_hit_tokens'])}, miss {fmt(tot['input_cache_miss_tokens'])})")
print(f"  Output tokens: {fmt(tot['output_tokens'])}")
print(f"  Total tokens:  {fmt(tot_in + tot['output_tokens'])}")
print("=" * 100)

with open(os.path.join(OUT, "usage_summary.json"), "w") as f:
    json.dump(result, f, indent=2)
print(f"\nWrote usage_summary.json ({len(json.dumps(result))} bytes)")
