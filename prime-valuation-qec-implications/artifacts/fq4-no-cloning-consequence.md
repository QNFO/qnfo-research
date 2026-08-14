# FQ4 Outcome — No-Cloning Re-Expression and Checkable QEC Consequences

**Project:** QNFO.RES.006 · *Implications for Computing and Quantum Error Correction*
**Date:** 2026-08-14
**Status:** ANSWERED — **DISCONFIRMED** (negative result)
**Registry link:** RESEARCH-CONTINUITY-REGISTRY.md §1 FQ4, §3 RQ4, §5 calibration

---

## 1. The question (FQ4 / claim C6)

> **FQ4:** Does the no-cloning re-expression (non-cloneable redundancy) yield a checkable
> consequence for QEC limits beyond the standard no-cloning statement?
>
> **C6 (re-expression):** no-cloning re-expressed as non-cloneable redundancy.
>
> **RQ4 (disconfirmation):** disconfirmed if the no-cloning re-expression yields no new
> checkable consequence.

---

## 2. The analysis

### 2.1 The re-expression is Abramsky's result

The paper's §5 frames no-cloning as the impossibility of a linear diagonal map
$\Delta: A \to A \otimes A$ — the monoidal-not-Cartesian reading. This is
**content-identical** to the established categorical quantum mechanics of Abramsky (2009)
*No-Cloning in Categorical Quantum Mechanics* and Coecke (2009) *Quantum Pictorialism*;
the paper's own §8 already credits this ("the no-cloning content of §5 is theirs; this
paper adds only vocabulary"). The re-expression is therefore correct but not novel.

### 2.2 The standard consequences (established, unaffected)

No-cloning's QEC-relevant consequences are well known and remain valid:
1. **No perfect quantum repetition codes** — an unknown quantum state cannot be cloned,
   so classical-style triple-modular redundancy is impossible for quantum information.
2. **QEC requires non-orthogonal / entangled encodings** — the stabilizer/CSS structure
   exists precisely because simple duplication is unavailable.
3. No-cloning ↔ no-deleting duality (Pati–Braunstein); QKD security.

### 2.3 Quantitative QEC limits are already covered by known bounds

The quantitative limits of error correction are given by the established bounds:
quantum Singleton $n - k \ge 2(d-1)$, quantum Hamming bound, quantum
Gilbert–Varshamov bound. The strongest no-cloning-only consequence derivable is the
trivial $n \ge k+1$ (any non-trivial encoding needs redundancy), which is **strictly
weaker** than Singleton for every code with $d \ge 2$.

Critically, **FQ2 (2026-08-14) already established** that the vocabulary's own
invariant — the valuation structure — produces NO bound tighter than Singleton. There is
therefore no route from "non-cloneable redundancy" to a new quantitative QEC limit: the
valuation content is exhausted (FQ2), and the no-cloning content is the standard theorem
plus its standard consequences.

### 2.4 Conclusion

The re-expression yields the standard consequences and **no new checkable consequence**.
Per RQ4's falsifiability condition, C6 is disconfirmed: the "non-cloneable redundancy"
framing is a relabeling of known categorical-QM + standard-QEC content.

---

## 3. Verdict

**FQ4 DISCONFIRMED** (per RQ4): the no-cloning re-expression adds no new checkable
consequence for QEC limits beyond the standard no-cloning statement. The re-expression is
relabeling (of Abramsky's categorical result); the only new-looking content in the
proposal — a valuation-based overhead bound — was already disconfirmed by FQ2.

---

## 4. Boundary — what this does NOT close

- The **no-cloning theorem itself** is established mathematics and is untouched.
- Standard applications (QKD security, quantum teleportation, no-deleting) are unaffected.
- The impossibility of perfect quantum repetition codes and the entanglement requirement
  for QEC remain true — they are simply *standard* consequences, not new ones.

---

## 5. Red-team notes (self-audit of this analysis)

| Check | Result |
|:------|:-------|
| Steelman: could non-cloneable redundancy imply a NEW lower bound on overhead? | The best bound derivable from no-cloning alone is $n \ge k+1$, strictly weaker than Singleton ($n-k \ge 2(d-1)$) for $d \ge 2$. No new quantitative content. |
| Is the disconfirmation consistent with FQ2? | Yes — FQ2 disconfirmed the valuation-based overhead bound; FQ4 disconfirms the no-cloning-framing consequence. Both negative, mutually consistent, both already anticipated by the paper's self-correction framing. |
| Does the re-expression itself fail? | No — it correctly re-expresses no-cloning (as Abramsky does). What fails is the RISK-HIGH part: a *new* checkable consequence. |
| Overclaim risk | Negative verdict; no new positive claim. |

---

*This document completes FQ4 in the RESEARCH-CONTINUITY-REGISTRY.*
