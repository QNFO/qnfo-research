# WBS: QNFO.RES.024

# Post-Positional Numeracy: Finite-Adele Encoding and Product-Formula-Verified Exact Rational Arithmetic

**WBS:** QNFO.RES.024 · **Slug:** post-positional-numeracy · **Branch:** res/paper/post-positional-numeracy
**Repo:** QNFO/qnfo-research · **Program:** QNFO Research Archive · **Status:** Phase 1 — core claim re-scoped to the verified delta (2026-08-26)

## 1. Charter

The QNFO corpus already publishes the conceptual line behind "post-positional numeracy": decimal notation is an anthropocentric, place-local convention (Ten-Fingered Trap; From Decimal Fingers to Adelic Freedom, 10.5281/zenodo.21428829), positional notation is natively an ultrametric tree (Nonlinear Tree-Based Numeration Systems, 10.5281/zenodo.21046213; THE SILENT RADIX, 10.5281/zenodo.21148596), numeral systems need multi-axis evaluation (NUMERATA, 10.5281/zenodo.21441847), and single-place exact arithmetic via Hensel codes is computation-ready (Exact Rational Arithmetic via p-adic Hensel Codes, 10.5281/zenodo.20754449 / 20756305 / 20756222). Phase 1 due diligence (2026-08-26) confirmed the thesis itself is published; the user directed this project to the ONE uncovered constructive leg: the **multi-place (finite-adele) formulation** — an encoding of Q across finitely many places, an injectivity window, and the adelic **product formula** used as a machine-checkable invariant of exact reconstruction — with computational verification and an executable demo. This paper extends the Hensel framework; it does not repeat it.

## 1.2 Core Claim (LOCKED — P6, re-scoped 2026-08-26)

**C1′.** Single-place p-adic exact arithmetic is published (Hensel framework, three versions). The uncovered step is multi-place: (a) the finite-adele encoding x ↦ (x mod p^k)_{p∈S} together with a two-sided Archimedean window is injective on the rationals: for M = ∏_{p∈S} p^k, a rational x = a/b with gcd(b, M) = 1, |a| ≤ B, and |b| ≤ B is uniquely determined by its multi-place image whenever 2B² < M (the Farey / Wang–Guy–Davenport reconstruction window; a lemma from the Chinese remainder theorem plus the Farey bound, stated and verified as a numeration theorem); (b) the adelic product formula ∏_{v∈S∪{∞}} |x|_v = 1 is a verification invariant for exact reconstruction — every correct multi-place encode/arithmetic/decode round-trip of S-smooth operands must satisfy it, and any violation localizes the failing place (for general operands the identity ∏_{v∈S∪{∞}} |x|_v = 1/∏_{p∉S} |x|_p applies); (c) both claims are computationally verified (golden values, 10^5 seeded trials) and shipped as an executable demo. The paper names the cross-domain bridge in its title and cites the published ancestors; it does not re-derive the conceptual thesis.

**Claim amendment (2026-08-26, Phase 1 red team):** the Phase-0 wording of the injectivity window used a one-sided bound (|x|_∞ ≤ ⌊M/2⌋), which is not injective — counterexample M = 30: x = 1/7 and x = 13 share the image 13 mod 30 and both satisfy |x| ≤ 15. The corrected two-sided Farey window is stated above. The v0.1-phase0-res024 tag documents the original wording; the correction precedes all computational work.

## 1.3 Premise-Depth Disclosure

- **L0 — named imported inputs:** Ostrowski's theorem (1916, Acta Math. 41:271–284, DOI 10.1007/BF02422947); the Hensel-code construction (Krishnamurthy–Rao–Subramanian 1975; Gregory–Krishnamurthy 1984); the Chinese remainder theorem; the rational-reconstruction bound (Wang–Guy–Davenport 1982, SIGSAM Bull. 16(2):2–3; Dixon 1982); the definition of the finite adeles as the truncation frame. These are imported, not re-derived.
- **L1 — derived in the paper:** the product formula ∏_v |x|_v = 1 for x ∈ Q^× (proved in an appendix from the unique factorization of x, and verified numerically); the injectivity window lemma (derived from CRT + the reconstruction bound); the product-formula check as a failure-localization invariant (an argument over the derived formula); the reference implementation and demo (constructions).
- **Where the premises END:** at the five L0 imports. Everything beyond them is derived, constructed, or computationally demonstrated. The paper does not claim the full adele ring is computable — it works with finite truncations, and says so.

## 1.4 Why a reader should care

1. **Exact-computation practitioners:** a reference implementation, test suite, and demo of multi-place exact rational arithmetic whose global integrity is machine-checkable through one invariant — the product formula — rather than through per-operation assertions alone.
2. **Number theory / arithmetic geometry readers:** a tangible "numeracy" reading of the adelic product formula: the same identity that ties the places together becomes a runnable checksum for exact arithmetic.
3. **Notation/epistemology readers:** the concrete artifact behind the published thesis — what a number looks like when no single place is privileged, executed in code rather than asserted in prose.
4. **QNFO thread:** completes the numeral-systems line with the multi-place layer none of the published records implement (verified by deposit audit, 2026-08-26).

## 1.5 Practitioner relevance

A practitioner can, from this paper's reference algorithm and deposited source: encode a rational x by its residues at a chosen prime set S and precision k, perform +, −, ×, ÷ componentwise, and reconstruct x exactly from the multi-place image plus a magnitude bound — with the product formula checked at every round-trip as the global invariant that localizes any failing place. The deliverable is a small dependency-free exact-arithmetic module (Python; BigInt JavaScript port for the demo), its test suite, and the demo — written in plain engineering language ("place" = a choice of metric on the rationals; "adele" = the bookkeeping that carries every chosen place at once; "product formula" = the conservation law every correct encoding must satisfy).

## 2. Phases (WBS-gated)

| Phase | Gate criteria |
|---|---|
| P0 Init | Branch + scaffold + PROJECT-PLAN + core claim locked; commit/tag/push verified (DONE, tag v0.1-phase0-res024) |
| P1 Due Diligence | Full-corpus sweep; adjudication: thesis published, delta = multi-place/product-formula leg; Hensel deposit audit; external sweeps; gap analysis; consilience gate; UIA + addendum (DONE this cycle) |
| P2 Literature | Ancestor line + Hensel-code literature (Krishnamurthy; Wang et al.; modular-methods line) + Ostrowski numeration disambiguation (DONE 2026-08-26: references.bib seed + docs/literature.md) |
| P3 Citations | BibTeX verified (P3.AUTHOR-GATE-EVERY-ENTRY-1); every ancestor DOI live-verified |
| P4 Research | Injectivity lemma proof; product-formula derivation; implementation; H-PPN execution; map-territory check |
| P5 Publication | .md/.html/.pdf (CDP pipeline), COMPUTATIONAL-VERIFICATION-1, rendering gates, Zenodo deposit (full source set incl. verification artifacts) |
| P6 Deployment | D1 living-paper + Vectorize index + papers.qnfo.org + R2 mirror |
| P7 Dissemination | Social posts, outreach per EMAIL-COMPOSER-PROACTIVE-1 rails |
| P8 Distribution | Tag, registry re-point, KG node + BUILDS_ON edges to the Hensel framework + BELONGS_TO the numeral-systems line |

## 3. Hypothesis Cards (pre-registered)

- **H-PPN-1 (computable):** for every nonzero rational x whose numerator and denominator are S-smooth (all prime factors in S), the truncated product formula ∏_{v∈S∪{∞}} |x|_v = 1 holds to floating precision; for general x the identity ∏_{v∈S∪{∞}} |x|_v = 1/∏_{p∉S} |x|_p holds (both derived from unique factorization; verified numerically). Golden values (S = {2,3}): x = 6, 2/3, 12 → 1; boundary case x = 5/2 → 5 = 1/|5/2|_5; then 10^4 seeded random S-smooth trials over S = {2,3,5,7}.
- **H-PPN-2 (imported, instance-checked):** Ostrowski's theorem instance checks in code (2-adic and real absolute values behave as the classification requires on test values).
- **H-PPN-3 (falsifiable):** the finite-adele encoding x ↦ (x mod p^k)_{p∈S} is injective on the two-sided window W = {x = a/b : gcd(b, M) = 1, |a| ≤ B, |b| ≤ B}, with M = ∏_{p∈S} p^k and B = ⌊√(M/2)⌋ (so 2B² < M). Prediction: zero collisions over 10^5 seeded trials. **Disconfirmation criterion:** one verified collision of two distinct rationals in W.
- **H-PPN-4 (novelty, adjudicated):** no published record — internal or external — states AND computationally verifies the product-formula-constrained multi-place reconstruction. Evidence gathered 2026-08-26: Hensel framework v1.2.0 deposit audited (paper.md: zero occurrences of "product formula"/"adele"/"adelic"; benchmarks single-prime p=7, k=30; reconstruction cites Wang–Guy–Davenport); external modular-methods line (Boehm–Decker–Fieker–Pfister et al.) uses CRT + Farey bounds, not the product formula as invariant. Closest external work adjudicated: Abbondati–Guerrini–Lebreton (J. Symb. Comput. 132:102481, 2026, "Simultaneous rational number codes") — multi-prime decoding with multiplicity codes and bad primes, no product-formula invariant. Claim scope = that conjunction.
- **H-PPN-5 (lineage integrity):** the paper cites every ancestor with a live-verified DOI and states plainly which leg each ancestor covers.

## 4. Risk Register

- **Coverage-drift risk (highest):** the delta is narrow because the Hensel framework already ships implementation + tests + demo (single-place). The paper MUST NOT re-cover single-place ground; every section is audited against the Hensel deposit before publish.
- **Novelty risk (external):** modular rational reconstruction is classical (Wang 1981; Dixon 1982); the novel conjunction is the product-formula invariant + the numeration framing — H-PPN-4 scopes the claim to exactly that.
- **Prose risk:** internal pipeline vocabulary and the "convenient lie" rhetoric stay out of publication text (PUBLICATION-PROSE-GATE-1, ANTI-TELEGRAPH-1); the paper speaks to practitioners and adjacent-domain readers.
- **Terminology-collision risk:** "Ostrowski numeration systems" is established external terminology (Hieronymi–Terry 2014 et al., continued-fraction numeration — a different sense). The paper must disambiguate in its crosswalk section.
- **Registry risk:** WBS collision (WBS-COLLISION-2) → atomic check-then-insert done; re-verify row identity on every write.

## 5. Success Criteria

- Every quantitative claim computationally verified (COMPUTATIONAL-VERIFICATION-1): product-formula golden values + 10^4 trials, injectivity 10^5 trials, round-trip exactness; scripts + outputs in artifacts/verification/ and deposited.
- Gap analysis with the Hensel-deposit audit evidence; crosswalk naming the bridges; zero unexplained jargon (CROSSWALK-TRANSLATION-1).
- Published Zenodo record with full source deposit, R2 mirror, D1 + KG distribution (R2-MIRROR-AFTER-PUBLISH-1); KG BUILDS_ON edge to the Hensel framework.

## 6. Deliverable Registry

PROJECT-PLAN.md · docs/deep-research.md · docs/universal-ignorance-audit.md (+ re-scope addendum) · artifacts/consilience-gate.md · artifacts/bayesian-evidential-weight.md · artifacts/external-search/* (incl. Hensel v1.2.0 deposit audit) · artifacts/verification/* · post-positional-numeracy.md/.html/.pdf · references.bib · citation-audit.md · README.md · demo via qwav-demo-kit
