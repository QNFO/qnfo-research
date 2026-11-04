# Classification Rubric — Infomatics v2

**Protocol:** research v2.4 §Phase 0.3 | **Date:** 2026-07-19

---

## §1. Classification Tags

Every audited claim receives exactly ONE of the following five tags.

### [Established]

**Definition:** Supported by peer-reviewed experimental evidence and/or mathematical theorems with broad consensus in the relevant field.

**Criteria (ALL must be satisfied):**
- Published in a peer-reviewed journal or has a DOI with ≥5 external citations
- Experimental evidence exists (if a physical claim) OR theorem is proven (if mathematical)
- Consensus in the relevant scientific community (not a fringe position)
- Reproducible by independent groups

**Examples:**
- α = e²/(ħc) ≈ 1/137.036 — CODATA, measured to 0.15 ppb
- Dirac equation predicts ZBW as a mathematical feature
- Information IS physical (Landauer 1961) — experimentally confirmed

### [Open]

**Definition:** Active research question with competing hypotheses and no experimental or theoretical consensus.

**Criteria (ANY):**
- Multiple competing hypotheses exist, none definitively confirmed
- Experimental constraints exist but are insufficient to rule out candidates
- Active debate in the literature (recent review papers, conference proceedings)
- The question is framed testably but has not yet been resolved

**Examples:**
- Does ZBW exist for free electrons or only as a mathematical feature?
- Does the electron have internal structure below 10⁻¹⁸ m?
- Can quantum gravity be formulated information-theoretically?

### [Speculative]

**Definition:** Theoretical proposal without experimental evidence, or lacking peer-reviewed confirmation.

**Sub-tags:**
- [Speculative — mathematical proposal]: Purely formal/mathematical, no physical test proposed
- [Speculative — no experiment]: Physical claim but no experimental evidence
- [Speculative — arXiv only]: Preprint, not peer-reviewed

**Examples:**
- ZBW as a p-adic observable (QNFO, no external citations)
- Adelic Dirac equation (QNFO, no peer review)
- α predicted by vortex topology (QNFO α-π-Helix, no external validation)

### [Disconfirmed]

**Definition:** Contradicted by experimental evidence or established theorems.

**Examples:**
- Eddington's α⁻¹ = 136 (experimentally wrong)
- Classical electron radius r_e as physical size (QFT invalidates classical self-energy)
- Hidden-variable theories with local realism (Bell test violations)

### [QNFO-Internal]

**Definition:** Exists only within the QNFO research ecosystem. No external citations, no peer review in non-QNFO venues, no experimental validation by independent groups.

**Note:** [QNFO-Internal] is NOT a judgment of quality. It states external validation status only.

**Criteria (ALL that apply):**
- Published only on Zenodo under QNFO collective authorship
- Has <2 external citations from non-QNFO authors
- Cited only by other QNFO papers
- No independent experimental test by external groups

**Examples:**
- ZBW→Bruhat-Tits trees connection (P1-P7)
- Ostrowski-based quantum error correction
- Cross-ratio reframing of α as a novel physical insight

---

## §2. Decision Tree

```
Is there experimental evidence? 
├── YES → Is it independently reproduced? 
│        ├── YES → [Established]
│        └── NO  → [Open]
└── NO  → Is it published in peer-reviewed venue with ≥5 external citations?
          ├── YES → [Open]
          └── NO  → Is it contradicted by evidence/theorems?
                    ├── YES → [Disconfirmed]
                    └── NO  → Has it been cited outside QNFO?
                              ├── YES → [Speculative]
                              └── NO  → [QNFO-Internal]
```

---

## §3. Evidence Requirements

| Tag | Minimum Evidence Required |
|:----|:--------------------------|
| [Established] | ≥2 independent experimental confirmations OR ≥1 mathematical proof with consensus + DOI |
| [Open] | ≥3 external papers from different groups addressing the question |
| [Speculative] | The original paper/proposal + any external citations |
| [Disconfirmed] | The disconfirming evidence (paper, DOI) + the original claim |
| [QNFO-Internal] | The QNFO paper(s) making the claim + verification of zero/negligible external citations |

---

## §4. Citation Verification Protocol

Every cited paper in this project MUST:

1. **Have a resolvable identifier:** DOI, arXiv ID, or journal reference verified by API call
2. **Be read (abstract minimum):** The title and abstract must be verified against the actual source
3. **Not be LLM-recalled:** Zero tolerance for citations generated from training data without verification

**Verification methods (in priority order):**
1. arXiv API: `http://export.arxiv.org/api/query?id_list={arxiv_id}`
2. Semantic Scholar API: `/graph/v1/paper/{paper_id}`
3. DOI resolution: `https://doi.org/{doi}`
4. CrossRef API: `https://api.crossref.org/works/{doi}`
5. Publisher page (as last resort)
