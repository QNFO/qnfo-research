# Example Session — Cosmological Constant Case Study

> *Condensed walkthrough. Shows what each phase looks like in practice.*

---

## Phase 1: Define (Human, ~30 min)

**Human writes:**

> "I want to investigate whether ultrametric (p-adic) geometry can resolve the cosmological constant problem — the $10^{120}$ mismatch between QFT vacuum energy and observed dark energy. Success looks like: a clear explanation of how ultrametric spacetime suppresses vacuum energy, a working derivation with dimensional analysis, and a draft that could become a review paper section."

---

## Phase 2: Delegate (Human → LLM, ~15 min)

**Human issues Prompt 1 (Literature Synthesis).** LLM responds with a 3-page synthesis covering Archimedean vs. ultrametric geometry, the CC problem, p-adic string theory, hierarchical suppression, and key papers.

---

## Phase 3: Execute & Iterate (LLM + Human, ~3 hours)

**LLM produces** a derivation showing hierarchical suppression: vacuum energy integral over p-adic "disks" yields a far smaller result than the standard continuum integral.

**Reality check (SymPy):** Expression is dimensionally correct ($\text{GeV}^4$) and reduces to standard QFT in the Archimedean limit ($p \to \infty$).

**Human catches** an unphysical regime in the high-p limit. LLM overcorrects, then together they converge on the power-law regime. **3 iterations total.**

---

## Phase 4: Verify (LLM + Human, ~1 hour)

- **G1 (Code):** SymPy re-run. All tests pass.
- **G2 (Limits):** $p \to 1$, $p \to \infty$, $m \to 0$ — all match known physics.
- **G3 (Reader):** Fresh LLM flags a missing factor of 2 — found and fixed.
- **G4 (Human):** Full read. Tone and clarity checked. Solid.

---

## Phase 5: Synthesize (LLM, ~30 min)

**Output:** Complete draft paper, 12 pages with LaTeX math, ready for human polishing.

---

## Session Metrics

| Metric | Value |
|:-------|:------|
| Total human time | ~5 hours |
| LLM iterations | ~12 prompts |
| Errors caught by verification | 3 (2 math, 1 missing factor) |
| Errors caught by human | 1 (physical regime mismatch) |
| Traditional timeline | ~6 months (postdoc + PI) |
| **Estimated speedup** | **~$25\times$** (preliminary) |

---

> *Based on the actual session documented in the project files. Results vary by domain, LLM version, and protocol familiarity.*
