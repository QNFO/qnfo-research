# Level Legend for Corpus Sweeps (DPRF T-2)

Tag every corpus hit (paper, record, note) with at most two level tags plus one defect tag where
applicable. Report level coverage in the sweep summary.

| Tag | Meaning | Typical carriers |
|:----|:--------|:-----------------|
| `D0` | distinction as primitive; laws of form; cut/mark language | foundations, LoF lineage |
| `D1` | pre-arithmetic structure: order, hierarchy, partitions, ultrametricity | hierarchy/taxonomy papers, UMP.014 |
| `D2` | arithmetic: counting, composition, factorization, statistics of occupation | primon gas, RES.027–028 |
| `D3` | number theory: distribution, L-functions, prime patterns | analytic number theory |
| `D4` | valuation: norms, places, p-adic size | p-adic/adelic papers |
| `D5` | geometry: metrics, rigidity, relational form | ultrametric spaces, spectral geometry |
| `D6` | information: entropy, two-point functions, discrimination | information physics, RES.030 |
| `D7` | measurement: protocols, resolution, noise, calibration on data | spectroscopy, benchmarks |
| `D8` | physics: falsifiable claims about the world; nulls | empirical papers, H1 candidates |

Defect tags (audit-only, never applied silently):

| Tag | Meaning |
|:----|:--------|
| `LEAK-X-Y` | claim at level Y presented as if it were level X without declared bridges |
| `ONTIC-SMUGGLE` | methodological primitive used with ontic force, undeclared (G1) |
| `MAP-AS-TERRITORY` | isomorphism asserted as physical realization without protocol/null/falsifier (G2) |
| `OBJ-CONFLATE` | two objects of the same level conflated (e.g., primes vs zeros, D3) |

Sweep summary line format:

```
<source> | <count> hits | levels covered: D2,D3,D6 | defects: LEAK-2-8:1, MAP-AS-TERRITORY:2
```
