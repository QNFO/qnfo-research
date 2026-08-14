# FQ3 Outcome — Valuation-Based Complexity Characterization of Reversible/Clifford Computation

**Project:** QNFO.RES.006 · *Implications for Computing and Quantum Error Correction*
**Date:** 2026-08-14
**Status:** ANSWERED — **DISCONFIRMED** (negative result)
**Registry link:** RESEARCH-CONTINUITY-REGISTRY.md §1 FQ3, §3 RQ3, §5 calibration

---

## 1. The question (FQ3 / claim C5)

> **FQ3:** Is there a valuation-based complexity characterization of reversible/Clifford
> computation that differs from (or tightens) the standard one?
>
> **C5 (MAP):** computing = path-tracing, with valuation-based complexity content.
>
> **RQ3 (disconfirmation):** disconfirmed if no valuation-based complexity characterization
> is produced.

The paper's §4 frames computation as "path-tracing through the branch structure." This
document applies the branch-depth vocabulary to the two canonical reversible/Clifford
settings and asks whether any *new* complexity content emerges.

---

## 2. The derivation

### 2.1 What valuation data reversible/Clifford computation actually has

| Object | Cardinality | Valuation |
|:-------|:------------|:----------|
| n-qubit / n-bit state space | $\dim H = 2^n$ | $v_2(\dim H) = n$ |
| Clifford group (n qubits) | $\|Cl(n)\| = 2\prod_{k=1}^{n}4(4^k-1)$ | $v_2(\|Cl(n)\|) = 2n+1$ |
| Reversible function group | $\|S_{2^n}\| = (2^n)!$ | $v_2((2^n)!) = 2^n-1$ (Legendre) |

The first is the C2-style trivial count. The second and third are **genuine, non-trivial
valuation identities** (verified computationally, see §3): the 2-adic valuation of the
Clifford group order is exactly $2n+1$, and the 2-adic valuation of the reversible
function group order is exactly $2^n-1$.

### 2.2 Why these identities are complexity-VACUOUS

The existence of non-trivial valuation identities does not produce complexity content:

1. **Gottesman–Knill simulability is uniform.** Every Clifford circuit is classically
   simulable in $\mathcal{O}(n^2)$ per gate via the tableau method — uniformly in
   $v_2(|Cl(n)|)$. The group-order valuation carries zero information about simulation
   cost. A larger group (larger valuation) is not harder; the Clifford group is always
   efficiently simulable regardless of its order's p-adic profile.
2. **The actual complexity measures have no valuation reading.** Circuit *depth*
   (number of layers), circuit *size* (gate count), and *stabilizer rank* (number of
   stabilizer-state terms in a decomposition) are the quantities that carry complexity
   content. All three are Hamming-type **counts** — weights, not depths in the valuation
   sense — and admit no p-adic valuation reading. This is exactly the C3/FQ2 pattern:
   the code distance $d$ (a weight) had no valuation reading; circuit depth and gate
   count (weights) have none either.
3. **The vocabulary's reachable invariants are cardinalities.** The branch-depth reading
   can only reach $\dim$, group orders, and subspace dimensions. Complexity is a property
   of circuit *structure* (how gates are arranged), not of the cardinality of the
   configuration space those circuits permute.

### 2.3 Conclusion

No valuation-based complexity characterization differing from (or tightening) the standard
measures exists. The candidate valuation identities are genuine mathematics and genuine
*relabeling* — exactly the failure mode C2's falsifiability condition was designed to catch.

---

## 3. Computational verification (2026-08-14, `fq3_check.py`)

- $v_2(|Cl(n)|) = 2n+1$ for $n = 1..8$: **all match** (e.g., $|Cl(3)|$ has $v_2 = 7$).
- $v_2((2^n)!) = 2^n - 1$ for $n = 1..8$: **all match** (Legendre's formula
  $v_2(m!) = m - s_2(m)$ with $s_2(2^n) = 1$).
- $v_2(2^n) = n$: trivially confirmed.
- The vacuity argument is structural (uniform simulability + weight-type measures) and
  requires no further computation.

---

## 4. Verdict

**FQ3 DISCONFIRMED** (per RQ3): no valuation-based complexity characterization of
reversible/Clifford computation is produced by the branch-depth vocabulary. The identities
$v_2(|Cl(n)|) = 2n+1$ and $v_2((2^n)!) = 2^n-1$ are genuine but complexity-vacuous; the
measures that actually characterize complexity (depth, size, stabilizer rank) are
Hamming-type weights with no valuation reading (consistent with C3, REJECTED, and FQ2,
DISCONFIRMED).

This completes the paper's falsifiability program for C5.

---

## 5. Boundary — what this does NOT close

- **p-adic algorithmics** (Hensel codes, p-adic lifting, exact rational arithmetic) is a
  legitimate computer-algebra topic with real complexity results and its own literature.
  That is a claim about *arithmetic algorithms*, not about the branch-depth reading of
  reversible/Clifford *circuits*. It is out of scope here and unaffected by this
  disconfirmation.
- **Gottesman–Knill** and standard Clifford synthesis results are untouched.

---

## 6. Red-team notes (self-audit of this derivation)

| Check | Result |
|:------|:-------|
| Is $v_2(|Cl(n)|) = 2n+1$ correct? | Confirmed: $4^k - 1$ is odd for all $k \ge 1$, so each of the $n$ factors contributes $v_2 = 2$ (from the $4 = 2^2$), plus the leading factor 2 contributes 1; total $2n+1$. |
| Could a valuation of the reachable-state set after $t$ layers carry content? | The reachable set is a subset of a $2^n$-space, so $v_2 \le n$ — trivial, and layer-count $t$ is a weight with no valuation reading. |
| Does the disconfirmation depend on a too-narrow notion of "complexity characterization"? | No — the disconfirmation is against the *standard* measures (depth/size/rank), which the vocabulary cannot reach. Any definition of complexity that is valuation-reachable reduces to cardinality, which is complexity-vacuous. |
| Overclaim risk | Verdict is negative (disconfirmation), consistent with FQ2; no new positive claim is made. |

---

*This document completes FQ3 in the RESEARCH-CONTINUITY-REGISTRY. Companion script:
`fq3_check.py` (arithmetic verification, outputs logged in this record).*
