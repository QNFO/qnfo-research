# FQ2 Outcome — Valuation-Based QEC Overhead Bound vs Quantum Singleton

**Project:** QNFO.RES.006 · *Implications for Computing and Quantum Error Correction*
**Date:** 2026-08-14
**Status:** ANSWERED — **DISCONFIRMED** (negative result)
**Registry link:** RESEARCH-CONTINUITY-REGISTRY.md §1 FQ2, §2 P4, §3 RQ2, §5 calibration

---

## 1. The question (FQ2 / claim C7 / prediction P4)

> **FQ2:** Is the QEC overhead (physical:logical qubits, n/k) bounded below by a
> valuation-structure function, and how does it compare to the quantum Singleton
> bound $n - k \ge 2(d-1)$?
>
> **C7 (hypothesis):** overhead is bounded by valuation structure.
>
> **P4 (prediction):** a valuation-based overhead bound is *tighter* than Singleton.
>
> **RQ2 (disconfirmation condition):** disconfirmed if the overhead bound is not
> tighter than or equivalent to the quantum Singleton bound.

This document is the concrete task the manuscript flagged as the test that would
"elevate this framing from metaphor to mathematics" (§5). It is now executed.

---

## 2. The derivation

### 2.1 What valuation data a stabilizer code actually has

Let $\mathcal{C} = [[n,k,d]]$ be a stabilizer code over qudits of dimension
$q = p^m$ (a prime power; qubit case $q=2$, $m=1$). The Hilbert space and
stabilizer give:

| Object | Value | Valuation |
|:-------|:------|:----------|
| total Hilbert space | $\dim H = q^n = p^{mn}$ | $v_p(\dim H) = mn$ |
| logical subspace | $\dim H_L = q^k = p^{mk}$ | $v_p(\dim H_L) = mk$ |
| stabilizer group | $\|S\| = q^{n-k} = p^{m(n-k)}$ | $v_p(\|S\|) = m(n-k)$ |

**Every one of these is a function of $(n, k, q)$ only.** None involves the code
distance $d$. The "valuation structure" of a stabilizer code — all that the
branch-depth vocabulary can compute from the Hilbert-space/stabilizer data — is
exhausted by the pair $(v_p(\dim H), v_p(\dim H_L)) = (mn, mk)$.

### 2.2 The quantum Singleton bound uses exactly the missing parameter

The quantum Singleton bound (Knill–Laflamme; Rains):

$$n - k \ge 2(d-1) \quad\Longleftrightarrow\quad \frac{n}{k} \ge \frac{n}{n - 2(d-1)}.$$

It constrains the overhead through $d$. The code distance $d$ is the minimum
Hamming weight of a non-trivial element of $N(S) \setminus S$ — a *weight*, not a
*depth*. The manuscript's claim **C3 already established that $d$ admits no
valuation reading (REJECTED)**. Therefore the Singleton input $d$ is precisely
the parameter the valuation vocabulary cannot express.

### 2.3 The candidate bound is vacuous / strictly weaker

A valuation-based overhead bound is a function of the valuation data alone:

$$\frac{n}{k} \ge f\big(v_p(\dim H), v_p(\dim H_L), q\big) = f(n, k, q).$$

Since $0 \le k \le n$, the sharpest such bound is

$$\frac{n}{k} \ge 1 \qquad (\text{i.e., } k \le n).$$

For any meaningful code ($d \ge 2$), the Singleton bound gives

$$\frac{n}{k} \ge \frac{n}{n - 2(d-1)} > 1,$$

strictly stronger. The non-cloneable-redundancy candidate of §5
($n \ge k+1$, i.e., $n/k \ge n/(n-1)$) is likewise weaker than Singleton, which
forces $n - k \ge 2(d-1) \ge 2$ for $d \ge 2$.

### 2.4 Qudit and hybrid generalization

- Qudits ($q = p^m$): the valuations become $mn, mk$ — still $(n,k,q)$-only.
- Hybrid/multi-prime codes ($\dim H = 2^a 3^b \cdots$): valuation data is the
  tuple $(a,b,\ldots)$ — still no $d$.
- In every case the conclusion is identical: valuation data underdetermines $d$.

---

## 3. Computational verification (2026-08-14, `fq2_check.py`)

- Singleton max distance $d_{\max} = \lfloor (n-k)/2 \rfloor + 1$ tabulated for
  $n \in [3,29]$, all $k$: the Singleton overhead bound $n/(n-2(d_{\max}-1))$
  exceeds 1 in every code with $d_{\max} \ge 2$.
- **378/378 codes with $d_{\max} \ge 2$ in the sample: the valuation-only bound
  ($n/k \ge 1$) is strictly weaker than Singleton.**
- Same-valuation, different-distance witness: $[[7,1,3]]$ (Steane) and
  $[[7,1,2]]$ have identical valuation data $(v_2(\dim H), v_2(\dim H_L)) = (7,1)$
  but different $d$ — valuation structure underdetermines $d$ by example.

---

## 4. Verdict

**FQ2 DISCONFIRMED** (per RQ2's condition): the valuation-based overhead bound is
not tighter than, nor equivalent to, the quantum Singleton bound — it is strictly
weaker. The obstruction is $d$: the code distance is a Hamming weight, which the
branch-depth vocabulary cannot express (consistent with C3, REJECTED).

**This is the predicted outcome of the paper's own self-correction program.** The
falsifiability register is now fully resolved: C2 self-corrected, C3 rejected,
C7 **disconfirmed by derivation**, C8 unverified-internal pending reproduction.

---

## 5. Boundary — what this does NOT close

This negative result is specific to *overhead bounds* (FQ2). It does **not** close:

- **FQ1** — whether a non-trivial valuation *invariant* exists with
  classification/predictive power over code *families* (the Kodaira–Néron 83%
  thread, REG-RES006-001). Classification is a different question from bounding;
  the valuation features may still separate code families even though they cannot
  bound $d$.
- **FQ3** — valuation-based complexity characterization of reversible/Clifford
  computation (promissory, untouched).
- **FQ4** — a checkable consequence of non-cloneable redundancy beyond the
  standard no-cloning statement (risk-high, untouched).

The live empirical thread remains the 83% classifier reproduction
(REG-RES006-001), still BLOCKED by NTOF source under-specification (Mahler target
function undefined; Cox-ring ideal $I_C$ unspecified).

---

## 6. Red-team notes (self-audit of this derivation)

| Check | Result |
|:------|:-------|
| Is the valuation data truly $(n,k,q)$-only? | Confirmed — $v_p(\dim H)$, $v_p(\dim H_L)$, $v_p(\|S\|)$ all reduce to $(mn, mk, m(n-k))$. |
| Could a valuation invariant of the *stabilizer generators* (e.g., generator-weight profile) enter? | Generator weight is Hamming weight, not valuation depth; any such bound is a locality/weight bound, not a valuation-structure bound, and would be a different claim than C7. Flagged for FQ1's classifier thread. |
| Does the disconfirmation depend on the bound being *tighter*? | RQ2 says "tighter or equivalent" — the derived bound is strictly weaker, so disconfirmation holds under either reading. |
| Known bound tightness | Singleton is tight for MDS codes ($[[n,n-2d+2,d]]$); no valuation-based bound could beat it for MDS codes since the valuation data gives no $d$. |
| Overclaim risk | Verdict is negative (disconfirmation), which the paper's framing already anticipated; no new positive claim is made. |

---

*This document completes FQ2 in the RESEARCH-CONTINUITY-REGISTRY. Companion
script: `fq2_check.py` (arithmetic verification, outputs logged in this record).*
