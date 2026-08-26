# WBS: QNFO.RES.024

# Post-Positional Numeracy: Ostrowski's Theorem, the Adele Ring, and the Decimal System as a Convenient Lie

**WBS:** QNFO.RES.024 · **Slug:** post-positional-numeracy · **Branch:** res/paper/post-positional-numeracy
**Repo:** QNFO/qnfo-research · **Program:** QNFO Research Archive · **Status:** Phase 0 — core claim locked (2026-08-26)

## 1. Charter

The Hindu-Arabic positional number system is routinely described as the completed, "perfect" numerical notation. This project subjects that claim to the valuation theory of the rationals: by Ostrowski's theorem, the Archimedean place is one of infinitely many inequivalent absolute values on Q, and positional uniqueness is a theorem only within a single place. The adele ring A_Q, which carries every completion simultaneously, supplies the rigorous setting for a post-positional numeracy — local-global simultaneity in place of the "tyranny of uniqueness." The project extends the QNFO numeral-systems line (NUMERATA, 10.5281/zenodo.21441847; THE SILENT RADIX, 10.5281/zenodo.21148596) with the valuation-theoretic backbone those papers gesture at, and delivers a constructively implementable finite-adele numeracy.

## 1.2 Core Claim (LOCKED — P6)

**C1.** Positional notation is not a structural optimum of numerical representation. Its uniqueness, completeness, and closure properties are valid within a single fixed place of Q; Ostrowski's theorem shows the full valuation structure of Q consists of the Archimedean place together with all p-adic places. Consequently the "perfection" attributed to the Hindu-Arabic system is a place-local convenience elevated to a false absolute, and the adele ring A_Q — which carries every completion simultaneously — is the rigorous foundation for a post-positional numeracy in which local-global simultaneity (the product formula) replaces the tyranny of uniqueness.

## 1.3 Premise-Depth Disclosure

- **L0 — unanalyzable primitives / named imported inputs:** Ostrowski's theorem (1916; every nontrivial absolute value on Q is equivalent to |·|_p or |·|_∞); the definition of the adele ring A_Q as the restricted product of completions; the definition of absolute value/valuation. These are imported, not re-derived.
- **L1 — derived in the paper:** the product formula ∏_v |x|_v = 1 for x ∈ Q^× (derived and computationally verified); the claim that "perfection" of positional notation is a value judgment, not a theorem (historical/argumentative); p-adic digit expansion (Hensel codes) as the natural numeration at a non-Archimedean place; the constructive finite-adele representation (truncate each local component at precision; injective on a window) — an implementation, not a theorem.
- **Where the premises END:** at Ostrowski's theorem plus the definitions of the adele ring and valuations. Every claim beyond L0 is either derived, constructed, or argued with citations. The cultural claim (notation as epistemic authority) is argument, flagged as such, and does not carry mathematical weight.

## 1.4 Why a reader should care

1. **Number theory / arithmetic geometry:** a tangible "numeracy" reading of the adele ring — how a number's simultaneous local representations cohere through the product formula — usable in teaching and in exact-arithmetic software.
2. **Numerical analysis / exact computation:** p-adic (Hensel-code) arithmetic is a working technology for exact rational computation; the paper gives the design argument for multi-place (adelic) exact arithmetic and a reference implementation.
3. **Epistemology of mathematics:** a worked case study in how a notation's contingent optimization becomes a false absolute — with the mathematical machinery (Ostrowski) that exposes it.
4. **QNFO thread:** completes the Silent Radix / NUMERATA line with the missing valuation-theoretic backbone and a title-visible cross-domain bridge (number theory × numeration systems × exact computation).

## 1.5 Practitioner relevance

A practitioner (numerical analyst, algebra-system engineer, cryptography engineer) can: implement finite-adele rational arithmetic from the paper's reference algorithm — represent x ∈ Q by its residues/digits at a finite set of places, define + and × componentwise, recover the rational via the product-formula-constrained reconstruction — and run the accompanying demo (qwav-demo-kit, DEM-E0-T01..T05) that verifies the product formula and the injectivity window in code. The artifact is a small exact-arithmetic library plus its test suite, in plain engineering language (no niche-terminology dead-ends: "place" = "choice of metric on the rationals", "adele" = "the bookkeeping that carries all choices at once").

## 2. Phases (WBS-gated)

| Phase | Gate criteria |
|---|---|
| P0 Init | Branch + scaffold + PROJECT-PLAN + core claim locked; commit/tag/push verified (THIS PHASE) |
| P1 Due Diligence | Full-corpus sweep (>=3 formulations), cross-system ID validation, >=2 adjacent domains, external verification, gap analysis; consilience gate (KIF-29) + Silo Cost Table; UIA on core claim |
| P2 Literature | 8 sources, dedup, symmetry template |
| P3 Citations | BibTeX verified (P3.AUTHOR-GATE-EVERY-ENTRY-1) |
| P4 Research | Derivations + hypothesis-card execution; check-map-territory; UIA re-pass |
| P5 Publication | .md/.html/.pdf (CDP pipeline), COMPUTATIONAL-VERIFICATION-1, rendering gates, Zenodo deposit (full source set) |
| P6 Deployment | D1 living-paper + Vectorize index + papers.qnfo.org + R2 mirror |
| P7 Dissemination | Social posts, outreach per EMAIL-COMPOSER-PROACTIVE-1 rails |
| P8 Distribution | Tag, registry re-point, KG node + BELONGS_TO/BUILDS_ON edges to Silent Radix + NUMERATA |

## 3. Hypothesis Cards (pre-registered)

- **H-PPN-1 (computable):** for every nonzero rational x with denominator within a fixed bound, the finite-place product formula ∏_{v ∈ S∪{∞}} |x|_v = 1 evaluates to 1 within floating precision. Golden values: x = 6 (2-adic 1/2 × 3-adic 1/3 × ∞-adic 6 = 1); x = 2/3; x = 12.
- **H-PPN-2 (imported theorem, instance-checked):** Ostrowski's theorem — instance checks in code, not a re-proof.
- **H-PPN-3 (falsifiable, pre-registered):** the finite-adele encoding map x ↦ (x mod p^k for p in S; sign/magnitude bound at ∞) is injective on Q restricted to a window (denominator coprime to ∏p^k, |x|_∞ ≤ B). Prediction: zero collisions over 10^5 seeded random trials. **Disconfirmation criterion:** a single verified collision with two distinct rationals in the window falsifies H-PPN-3 and weakens C1's constructive leg.
- **H-PPN-4 (novelty, pre-registered):** no prior publication states the conjunction "Ostrowski's theorem as the falsifier of positional-notation perfection + adele ring as post-positional numeracy + finite-adele exact arithmetic" (Phase 1 gap analysis adjudicates; the claim is retracted if such a record is found).

## 4. Risk Register

- **Novelty risk:** post-positional numeracy may overlap Hensel-code / p-adic exact-arithmetic literature → H-PPN-4 and the Phase 1 external sweep adjudicate; claim scope narrows to the conjunction.
- **Prose risk:** the "convenient lie" / epistemic-authority framing must stay scholarly (PUBLICATION-PROSE-GATE-1, ANTI-TELEGRAPH-1); the cultural argument carries no mathematical weight and is labeled as such.
- **Scope risk:** formalism drift to general global fields → the paper is bounded to Q; extensions noted as future work.
- **Registry risk:** WBS collision (WBS-COLLISION-2) → atomic check-then-insert + read-back verify.

## 5. Success Criteria

- Every quantitative claim computationally verified (COMPUTATIONAL-VERIFICATION-1): product-formula golden values, finite-adele injectivity (10^5 trials), Ostrowski instance checks; scripts + outputs in artifacts/verification/ and deposited.
- Gap analysis with external corroboration; zero unexplained jargon; crosswalk section naming the bridges (CROSSWALK-TRANSLATION-1).
- Published Zenodo record with full source deposit, R2 mirror, D1 + KG distribution (R2-MIRROR-AFTER-PUBLISH-1).

## 6. Deliverable Registry

PROJECT-PLAN.md · docs/deep-research.md · docs/universal-ignorance-audit.md · artifacts/consilience-gate.md · artifacts/bayesian-evidential-weight.md · artifacts/external-search/* · artifacts/verification/* · post-positional-numeracy.md/.html/.pdf · references.bib · citation-audit.md · README.md · demo via qwav-demo-kit
