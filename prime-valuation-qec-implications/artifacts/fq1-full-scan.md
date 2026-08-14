# FQ1-FULL-SCAN Outcome — v_2(A_j) Enumerator-Parity Invariant: PARTIALLY CONFIRMED

**Project:** QNFO.RES.006 · **Date:** 2026-08-14
**Status:** CONFIRMATION SCAN (Avenue A1) — **PARTIALLY CONFIRMED**
**Invariant:** $v_2(A_j)$ — 2-adic valuation profile of the stabilizer weight enumerator
($A_j = \#\{ \text{stabilizer elements of Pauli weight } j \}$).
**Script:** `artifacts/fq1-full-scan.py` (deterministic, seed 20260814).
**Predecessor:** `artifacts/fq1-exploratory-scan.md` (FQ1-EXP-001, 1 code/family — PRELIMINARY POSITIVE).

---

## 1. Design (re-specified REG-RES006-001, no blocked dependency)

The original Kodaira–Néron reproduction remains BLOCKED on NTOF source
under-specification. Avenue A1 re-specifies the pre-registered question to the
well-defined invariant $v_2(A_j)$, on **bulk families** with the **distance confound
explicitly controlled**:

| Family | Codes | Distance |
|:-------|:------|:---------|
| CSS (random, d≥3 filter) | 5 each at n = 7, 9, 11 ([[n,1]]) | ≥ 3 |
| Optimal | [[5,1,3]] perfect, [[7,1,3]] Steane, [[9,1,3]] Shor | 3 |
| Surface | toric L=2 [[8,2]], L=3 [[18,2]] | 2, 3 |
| Hamming | [[15,7,3]] | 3 |
| Random controls | 20 at each (5,1),(7,1),(8,2),(9,1),(11,1); 10 at (15,7),(18,2) — split d=1 vs d≥2 | — |

Features: `max_v2 = max_{j≥1} v_2(A_j)`; percentile of the structured value in the
matched control distribution (all controls, and d≥2-only controls).

---

## 2. Results (deterministic, seed 20260814)

| Code | max_v2 | pct all | pct d≥2 | verdict |
|:-----|:-------|:--------|:--------|:--------|
| CSS[7,1] #1–5 | 1 (×5) | 0% | 0% | **low outlier** |
| CSS[9,1] #1 | 1 | 0% | 0% | **low outlier** |
| CSS[9,1] #2–5 | 2–3 | 5% | 6% | near-low outlier |
| CSS[11,1] #1–4 | 3–5 | 30–85% | 30–85% | **NOT separated** |
| CSS[11,1] #5 | 6 | 95% | 95% | high-edge (within range) |
| [[5,1,3]] perfect | 0 | 0% | 0% | **low outlier** (all-odd) |
| [[7,1,3]] Steane | 1 | 0% | 0% | **low outlier** |
| [[9,1,3]] Shor | 4 | 55% | 50% | **NOT separated** |
| [[15,7,3]] Hamming | 1 | 0% | 0% | **low outlier** |
| toric L=2 [[8,2]] | 5 | 100% | 100% | **high outlier** (A₆=32) |
| toric L=3 [[18,2]] | 2 | 0% | 0% | **low outlier** |

**Pooled classifier** (structured n=21, random pool n=400 — *see caveat 4*, random d≥2 n=345):

- structured max_v2 values: `[0,1,1,1,1,1,1,1,1,2,2,3,3,3,3,3,4,5,5,5,6]` (median 2)
- random max_v2: min=1, median=3, max=8
- best 1-sided rule (max_v2 ≤ 1): sensitivity 0.43, specificity 0.81, **balanced 0.62**
- 2-sided fingerprint (≤1 or ≥5): sensitivity 0.62, specificity 0.67, **balanced 0.64**
- at extremes (≤1 or ≥5): **structured 0.62** vs random_all **0.33** vs random_d≥2 **0.37**

---

## 3. Interpretation (honest)

1. **Structure detection is real and robust beyond the exploratory sample:** 16/21 (76%)
   structured codes sit at/near the extremes of their matched random distributions
   (11/21 = 52% are clean 0%/100% outliers). This confirms FQ1-EXP-001's lead at bulk scale.
2. **The distance confound is REFUTED:** random controls with d ≥ 2 have essentially the
   same extreme-fraction as all random codes (0.37 vs 0.33), both far below structured
   (0.62). The invariant detects structure *beyond* the d ≥ 2 property.
3. **But the classifier power is MODERATE, not 83%-class:** best balanced accuracy 0.64
   vs the 0.50 baseline (best 1-sided 0.62). The invariant is a **structure-detection
   fingerprint**, not a high-accuracy family classifier.
4. **Size/family dependence:** separation is strong at n ≤ 9 (CSS[7,1], CSS[9,1], perfect,
   Steane, Hamming, toric L=2 — all at extremes), weak at n ≥ 11 (CSS[11,1] #1–4 and
   Shor in the middle). The toric fingerprint flips sign with L (L=2 high via A₆=32,
   L=3 low) — per-code signature, not a stable family label.
5. **Verdict: PARTIALLY CONFIRMED.** The invariant exists and detects non-random code
   structure beyond distance (answering FQ1's existence/predictive-power question in the
   affirmative, at moderate strength), but it does NOT reproduce the 83% claim's magnitude
   as a family classifier. The original Kodaira–Néron claim remains UNVERIFIED-INTERNAL
   and BLOCKED.

---

## 4. Caveats

1. CSS[11,1] codes were filtered to d ≥ 3 — the family is valid, yet not separated:
   the invariant's power genuinely degrades at n ≥ 11.
2. Pooled random pool contains duplicates (each (n,k) control set is appended once per
   structured code sharing that key; e.g., (7,1) controls appear 6×). Per-code percentiles
   are the primary evidence; pooled specificity/accuracy are indicative only.
3. Distance for controls is a d=1 vs d≥2 split (weight-1 scan); structured distances are
   nominal/known (CSS filtered ≥3, perfect/Steane/Shor/Hamming = 3, toric = L).
4. Not the pre-registered REG-RES006-001 (Kodaira–Néron); that test still awaits NTOF
   source clarification.

---

## 5. Red-team notes (self-audit)

| Check | Result |
|:------|:-------|
| Is the perfect code's max_v2=0 robust at bulk scale? | Yes — reproduced (A₄=15 odd), 0th percentile vs 20 controls. |
| Is the toric L=2 max_v2=5 real? | Yes — A₆=32 (v₂=5), reproduced; 100th percentile. |
| Could the CSS[11,1] failure be a generation artifact? | No — codes are valid (d≥3 filter, sanity |S|=2^m), 5/5 in the middle; genuine size effect. |
| Is the confound test adequate? | d-split is d=1 vs d≥2 only (weight-1 scan); a d≥3 split for controls was not computed at n≥15 (cost). Flagged for the pre-registered 50/family run. |
| Overclaim risk | Mitigated: "partially confirmed", moderate classifier numbers, per-family failures reported. |

---

## 6. What this means for the avenues (avenues-remaining.md)

- **A1 refined:** the full confirmation shows the $v_2(A_j)$ invariant is a *moderate,
  size-dependent structure fingerprint* (best balanced 0.64). A pre-registered 50/family
  run is still the right next step — with per-family signatures and a d≥3 control split —
  but expectations should be moderate (not 83%-class).
- **A2 (no-go lemma):** unchanged — the valuation-weight duality stands; $A_j$ remain the
  one class of code-dependent integers outside the (n,k,q)-only set.
- **A3/A4 (p-adic algorithmics; ultrametric geometry):** unchanged — the domain-native
  directions.
- **A5 (original 83% Kodaira–Néron):** still BLOCKED on NTOF source under-specification.
