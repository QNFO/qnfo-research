# Red-Team Audit — QNFO.RES.004 Prime Valuation Depth (P4 Stage 3, 5-Adversary)

**Date:** 2026-08-13 · **Phase:** P4 · **Audited artifact:** `prime-valuation-depth.md` (v0.1-draft) + `artifacts/consilience-gate.md` + `RESEARCH-CONTINUITY-REGISTRY.md`
**Method:** 5 adversary positions against the draft's claims; every finding graded HARD/SOFT/DESIGN and adjudicated.

---

## A. Adversary Positions

### 1. Null-Hypothesis Defender
**Attack:** "The correspondence between the calculus of indications and the prime tree is a naming game. You map 'distinction' to 'prime branch type' and 'nesting' to 'exponent' by fiat, then claim two laws as shared. Every nested structure has a hierarchy law and an additive depth measure — trees, semilattices, hierarchies in general. Nothing distinguishes primes or distinctions."

**Adjudication:** ACCEPTED as a HARD constraint, mitigated in the draft (§3.2, Statement 2 falsifiability condition) and pre-registered (REG-RES004-001). The paper already concedes the correspondence is a reading with zero evidential weight until non-vacuity is demonstrated. **No draft change required** — the risk is documented; the non-vacuity test is the next research action (FQ1).

### 2. Methodology Skeptic
**Attack:** "Statement 4 (structural no-cloning) is retrodiction dressed as insight. The categorical fact — Hilb is monoidal, not Cartesian, so no natural diagonal — is published by Coecke–Duncan and Coecke–Paquette. You add 'p-adic depth of dimension' vocabulary and call it a reading, but the vocabulary tracks no new structure."

**Adjudication:** ACCEPTED. The draft states this explicitly (KIF-60 [RETRODICTION — not evidence] in §5.3 and §6.2), and the delta path (FQ2/FQ3) is pre-registered. The novelty claim is deliberately scoped to the vocabulary, not the theorem. **No change required** — the honest labeling is in place; the risk is that a reader still reads it as new physics. Consider strengthening the abstract wording that the categorical content is established. **SOFT finding → abstract revised to name the established categorical source explicitly.**

### 3. Better-Alternative Proposer
**Attack:** "The standard linearity proof of no-cloning is clearer than the branch-depth vocabulary. The categorical formulation is more rigorous. What does the p-adic reading buy you that these do not? Nothing, except a vocabulary that invites numerology (v_p of dimension) without a resource theory."

**Adjudication:** ACCEPTED as the central risk. The paper's honest answer: the reading buys heuristic unification (LoF + number theory + QM under one vocabulary) and an open frontier (FQ4, adelic). It buys no new theorem yet. This is already the paper's position (§7). **No change required** — but the abstract must not overclaim; verified the abstract says "vocabulary... rather than new physics." PASS.

### 4. Scaling Pessimist
**Attack:** "The p-adic dimension-depth reading does not scale: for a 6-dimensional system, v_2(6)=1 and v_3(6)=1; the 'depth' is a tuple, not a single number, and the diagonal argument works identically for any d>1. The prime factorization of dimension is irrelevant to the no-cloning theorem — the theorem holds for d=6 exactly as for d=4, and v_2(dim) has no role in the proof."

**Adjudication:** ACCEPTED, and it is precisely the paper's claim: the theorem does not depend on the valuation; the valuation provides a reading. The scaling pessimist's observation that v_p is a tuple for non-prime-power dimensions is a genuine gap in the draft — §4 and §5.3 use the qubit case (dim=2^n) exclusively. **HARD-ish SOFT finding → the draft must acknowledge that for general dimensions the branch-depth is a tuple (v_p(dim)) over all primes, and the diagonal argument holds independent of it.** Add one sentence in §4.

### 5. Resource Realist
**Attack:** "You call v_p(dim H) a resource ('counts tensor-branch depth'), but there is no conservation law, no bound, no operational meaning. A 'resource' in QI theory has a monotone under allowed operations; you provide none. The BEC bypass claim [@datta2022] you cite adversarially is unanalyzed — you cannot both cite it and dismiss it in one sentence."

**Adjudication:** ACCEPTED. The resource claim is overreach; the draft says "suggests a resource accounting" but the continuity registry does not yet define a monotone. Fix: (a) soften "resource-theoretic reading" to "branch-depth accounting" in §5.3 title, (b) commit to FQ3 to define a monotone or drop the term, (c) add one sentence acknowledging the BEC claim requires full analysis (already listed as FQ5). **SOFT findings → title softened; FQ3 wording tightened.**

---

## B. Consolidated Findings

| # | Severity | Finding | Adjudication |
|:--|:---------|:--------|:-------------|
| R1 | HARD (constraint, not draft defect) | Correspondence may be vacuous relabeling | Documented + pre-registered (REG-RES004-001); no draft change |
| R2 | SOFT | Abstract could be read as claiming novel physics | Abstract already labels vocabulary vs physics; verified PASS |
| R3 | SOFT | General-dimension branch-depth tuple not acknowledged | **Fix: add tuple acknowledgment in §4** |
| R4 | SOFT | "Resource-theoretic" overclaim without a monotone | **Fix: retitle §5.3 to branch-depth accounting; FQ3 tightens** |
| R5 | SOFT | BEC bypass claim cited but unanalyzed | FQ5 added to registry; add one-sentence acknowledgment |

## C. Fixes Applied (same session)

1. **§4 added:** "For a general finite-dimensional system of dimension $d = \prod_p p^{e_p}$, the branch-depth is the tuple $(v_p(d))_p$; the no-cloning diagonal argument holds for any $d > 1$ and does not depend on the valuation — the valuation provides the reading, not the proof."
2. **§5.3 retitled:** "The Branch-Depth Accounting" (was "The Resource-Theoretic Reading"); wording softened to "suggests a branch-depth accounting... a genuine resource monotone is left as an open question (FQ3)."
3. **Abstract:** explicitly names Coecke–Duncan / Coecke–Paquette for the categorical fact ("The categorical content of this statement is established in the literature" → "established by Coecke and Duncan and Coecke and Paquette").
4. **Registry:** FQ5 wording tightened to require either a monotone definition or explicit retirement of the term "resource."

## D. Gate Result

**5/5 adversary positions addressed. Zero HARD draft defects. 4 SOFT findings applied in-session.**
The red-team gate passes for v0.1-draft. The correspondence non-vacuity (R1) and the adelic delta (FQ4) remain open research items tracked in the continuity registry — not publication blockers for a paper that explicitly labels them as such.
