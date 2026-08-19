# Critique-Validity Rubric — Governance Instrument (adopted from QNFO.RES.016)

**Origin:** "Five Objections, One Standard: An Evidence-Graded Adjudication of a Critique of Post-Quantum Synthesis" (DOI 10.5281/zenodo.22010489, concept 10.5281/zenodo.22009652), §10.
**Adopted into:** QNFO.RES.014 Evidence-Verification Corpus — 2026-08-19
**Status:** GOVERNANCE INSTRUMENT (field-tested in RES.016 pass-1/pass-2 adversarial audits)

---

## 1. Purpose

Standardized grading of ANY critique (AI-generated, peer, or informal) leveled at a QNFO research
claim, and — symmetrically — of any critique QNFO produces about external work. The instrument
converts "this critique says my work is unsubstantiated" into a per-premise ledger that separates
what must be answered from what can be dismissed with evidence.

## 2. The Four Grades

| Grade | Meaning | Required evidence |
|:------|:--------|:------------------|
| **Confirmed** | The objection's factual premises all verify against primary sources | Every premise traced to a primary text passage or live registry record |
| **Partially confirmed** | The objection's conclusion survives in weakened form, but material premises fail or are unverified | Mixed: some premises verified, some failed |
| **Unsupported** | The objection's premises are contradicted by verifiable literature or asserted without engagement | Counter-evidence cited from the literature the objection ignored |
| **Contradicted** | The objection's premise commits a documented reasoning error | Reference to the codified error (e.g., institutional-status reasoning, premise-asymmetry) |

## 3. The Five Steps (application protocol)

1. **Decompose the objection into premises.** Every objection is a set of factual premises plus a
   conclusion. Write the premises down before evaluating the conclusion.
2. **Verify each premise against a primary source.** A premise that cannot be traced to a primary
   text, a registry record, or a live metadata check is an unverified premise — and an objection
   built on unverified premises carries no weight against the framework it attacks.
3. **Apply the same standard to both sides.** If the objection demands falsifiability, predictive
   evidence, or engagement with prior art, the objection's own historical, empirical, and
   institutional premises face the same demands. Institutional status (venue, affiliation,
   peer-review history) is not evidence about content.
4. **Check the literature the objection ignores.** The strongest counter-evidence to an objection
   is often a literature the objection does not cite.
5. **Grade, don't polarize.** The four-grade scale preserves what is true in an objection while
   preventing true premises from laundering false ones.

## 4. Evidence classes (per grade)

- **Primary-text anchor:** exact passage quoted from the object of critique (with section
  reference), verified against the deposited/canonical body.
- **Live registry check:** DOI/author/venue verified against Crossref, OpenAlex, arXiv, or DataCite
  in-session; evidence file saved.
- **Prior-art DOI:** a resolvable DOI for the literature the objection ignored.
- **Archive capture:** archive.org CDX / Wayback capture for web-presence or date claims.
- **Codified-error reference:** a named, documented reasoning error (e.g., KIF-16 institution
  fallacy; premise-asymmetry as defined in RES.016 §8).

## 5. Symmetry requirement

The standard is symmetric by construction: the critique's premises are verified with the same
rigor the critique demands of the framework. **Premise-asymmetry** — demanding verification from
the target while asserting one's own premises without evidence — is itself a graded failure of the
critique (RES.016 §8: the pattern across all five objections examined).

## 6. Mandatory usage

1. Any QNFO response to an external critique of a QNFO claim MUST grade the critique with this
   rubric and record the grades in the project's artifacts (e.g., `artifacts/critique-grading.md`).
2. Any QNFO red-team review of an external work MUST apply the rubric symmetrically and record the
   grades.
3. Post-publication adversarial analyses (publish-then-audit loop) MUST use these four grades in
   their aggregated reports (canonical: RES.016 pass-1 → 5 HARD; pass-2 → 0 HARD).

## 7. Canonical case references

- RES.016 pass-1: 5 HARD findings (3 fabricated authors + misattribution + count error +
  unverified DOI) — all graded, all remediated in v1.1 (10.5281/zenodo.22010489).
- RES.016 pass-2: 0 HARD — remediation verified clean.
- RES.016 carry-forward audit: 2 HARD (fabricated pairing, missed obligation) — both remediated.
