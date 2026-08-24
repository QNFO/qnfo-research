#!/usr/bin/env python3
"""validate_seed_vs_published.py — reproduce the published RQ5 L1 numbers
and the family-bridge contingency from 10.5281/zenodo.22071421 using the
parsed qnfo_domains.json.

Published expectations (rq5_results.json):
  total_distinct_keywords == 335
  program_local_count     == 334
  shared_by_two           == {'complexity-measure': ['INM', 'RES']}
  load_bearing_core       == {}
  contingency bridge x load-bearing (>=3 programs):
      bridge_and_load_bearing 0, bridge_and_local 53,
      non_bridge_and_load_bearing 0, non_bridge_and_local 282
      fisher_one_sided_p == 1.0
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from terminology_silos import fisher_one_sided  # noqa: E402

DATA = json.loads(Path("artifacts/external-search/qnfo_domains.json").read_text(encoding="utf-8"))
domains = DATA["domains"]
families = {k: set(v) for k, v in DATA["bridge_families"].items()}
bridge_norms = set().union(*families.values())

# coverage: normalized keyword -> set of programs
cov: dict[str, set[str]] = {}
for code, kws in domains.items():
    for kw in kws:
        cov.setdefault(kw, set()).add(code)

total = len(cov)
local = {kw for kw, ds in cov.items() if len(ds) == 1}
core = {kw for kw, ds in cov.items() if len(ds) >= 3}
shared2 = {kw: sorted(ds) for kw, ds in cov.items() if len(ds) == 2}
not_load_bearing = set(cov) - core   # published contingency 'local' = <3 programs

# family-bridge contingency (published definition: bridge = in the four families,
# load-bearing = >=3 programs; 'local' column = not load-bearing, which includes
# the single shared-by-two keyword)
a = len(bridge_norms & core)
b = len(bridge_norms & not_load_bearing)
c = len((set(cov) - bridge_norms) & core)
d = len((set(cov) - bridge_norms) & not_load_bearing)
fe = fisher_one_sided([[a, b], [c, d]])

ok = True
checks = [
    ("total_distinct_keywords == 335", total == 335, total),
    ("program_local_count == 334", len(local) == 334, len(local)),
    ("shared_by_two == {complexity-measure}", shared2 == {"complexitymeasure": ["INM", "RES"]}, shared2),
    ("load_bearing_core == 0", len(core) == 0, sorted(core)),
    ("bridge_and_load_bearing == 0", a == 0, a),
    ("bridge_and_local == 53", b == 53, b),
    ("non_bridge_and_load_bearing == 0", c == 0, c),
    ("non_bridge_and_local == 282", d == 282, d),
    ("fisher_one_sided_p == 1.0", abs(fe["p_one_sided_greater"] - 1.0) < 1e-9, fe["p_one_sided_greater"]),
]
for name, passed, got in checks:
    print(f"{'PASS' if passed else 'FAIL'}: {name}  (got {got})")
    ok = ok and passed

print(f"\nRESULT: {'VALIDATED — seed reproduces published audit' if ok else 'MISMATCH'}")
sys.exit(0 if ok else 1)
