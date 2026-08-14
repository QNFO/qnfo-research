# What Remains: Avenues After the FQ2/FQ3/FQ4 Disconfirmations — and What Works

**Project:** QNFO.RES.006 · **Date:** 2026-08-14
**Companions:** `artifacts/fq2-overhead-bound.md`, `artifacts/fq3-complexity-characterization.md`,
`artifacts/fq4-no-cloning-consequence.md`, `artifacts/fq1-exploratory-scan.md`

---

## 1. What the negative results establish (the structural finding)

The five negative resolutions (C2 relabeling, C3 d-inexpressibility, FQ2, FQ3, FQ4) share
one structural root:

> **The branch-depth vocabulary reaches cardinality/dimension invariants — v_p of
> dimensions and group orders. The information-carrying quantities of its target domains
> are weights/counts — Hamming weights (code distance d, circuit depth, gate count,
> stabilizer rank) — which admit no p-adic valuation reading.**

Call this the **valuation-weight duality**. It is a *positive* characterization of the
vocabulary's scope, and it converts five negative results into one clean boundary statement:

**Lemma (valuation-weight duality for stabilizer codes — essentially proven by FQ2/FQ3).**
Every valuation-reachable invariant of a $[[n,k,d]]$ stabilizer code over $q = p^m$ —
every $v_p$ of a quantity determined by the Hilbert-space/stabilizer cardinalities
($\dim H$, $\dim H_L$, $|S|$) — is a function of $(n, k, q)$ only. In particular, no such
invariant is sensitive to the code distance $d$. (Proof: $\dim H = q^n$, $\dim H_L = q^k$,
$|S| = q^{n-k}$; further invariants would involve weights, which are not valuations.)
Corollary for computing: no valuation-reachable invariant of reversible/Clifford
computation is sensitive to circuit depth, size, or stabilizer rank.

---

## 2. What DOES work — the first positive lead (this session)

The FQ1 exploratory scan (**FQ1-EXP-001**, `artifacts/fq1-exploratory-scan.md`) produced
the first positive result in the FQ series:

> **The 2-adic valuation profile of the stabilizer weight enumerator, $v_2(A_j)$, detects
> structure: 4/4 structured families are outliers against same-parameter random controls
> (max_v2 percentiles 0%, 5%, 100%, 0%).** The perfect code is the cleanest
> (all-odd enumerator, $A_4 = 15$, strictly below all 20 controls).

Why it survives the no-go lemma: the $A_j$ coefficients are **code-dependent integers**
(determined by the full stabilizer group), *outside* the $(n,k,q)$-only set. The invariant
is a structural *fingerprint* (family-dependent sign: perfect/Hamming at the low extreme,
toric at the high extreme via $A_6 = 32$), not a single-threshold classifier.
Status: **preliminary positive** — small sample (1 per family); needs the fresh 50/family
generation to confirm.

---

## 3. Avenues ranked by promise × executability

| # | Avenue | Promise | Executable now? | Notes |
|:--|:-------|:--------|:----------------|:------|
| **A1** | **FQ1 full confirmation** — re-specify REG-RES006-001 to the well-defined $v_2(A_j)$ invariant (fresh 50/family, seeded, distance-confound control) | **HIGH** — first positive lead; no blocked dependency if re-specified | **YES** (re-specification decision) or after NTOF blocker clears | The strongest concrete next research step |
| **A2** | Formalize the no-go lemma (valuation-weight duality) into a publishable appendix | MEDIUM — converts 5 negatives into 1 theorem | YES (write-up; derivation done) | Strengthens the paper's self-correction contribution |
| **A3** | **p-adic algorithmics** (Hensel codes, p-adic lifting, exact rational arithmetic) — where valuation has NATIVE teeth | **HIGH** — domain-native content | New paper territory (corpus has related papers) | The negative results point here: the vocabulary's content lives in arithmetic, not combinatorial code/circuit invariants |
| **A4** | **Ultrametric geometry strand** (Bruhat–Tits trees as QEC geometry — Heydeman–Marcolli–Saberi–Stoica; corpus qec-darwinism) | **HIGH** (external precedent) | New paper territory | Untouched by the FQ disconfirmations (different structure than branch-depth) |
| **A5** | **REG-RES006-001 original** (83% Kodaira–Néron reproduction) | MEDIUM (the claim is real-or-not) | **BLOCKED** (NTOF source under-specification) | Resume on source clarification; protocol + script ready |

---

## 4. Recommendation

1. **Immediate:** re-specify **REG-RES006-001** to the $v_2(A_j)$ invariant (A1) and run the
   fresh 50/family generation with the distance-confound control. This is the single most
   promising executable path and needs no external blocker.
2. **Riding along:** formalize the no-go lemma (A2) as the paper's positive structural
   contribution.
3. **Next papers:** the vocabulary's native teeth are in **arithmetic** (A3, Hensel codes)
   and **ultrametric geometry** (A4, Bruhat–Tits) — the directions the negative results
   point toward. The branch-depth reading is relabeling in combinatorial QEC/computing but
   has genuine content where p-adic structure is intrinsic.
4. **On the blocker:** A5 resumes the moment the NTOF source clarifies (Mahler target
   function, Cox-ring ideal I_C).

---

*This document is the honest answer to "what remains / what works" after the FQ2/FQ3/FQ4
disconfirmations: the vocabulary's scope is now bounded (valuation-weight duality), one
positive invariant lead exists (enumerator-parity $v_2(A_j)$), and the domain-native
directions (p-adic algorithmics, ultrametric geometry) are where the real content lives.*
