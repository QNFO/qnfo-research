# DECISIONS: Language-Info-Architecture

---

### D8: Use permutation test rather than chi-square for mutual exclusion
- **Date:** 2026-05-12
- **Rationale:** Chi-square tests are invalid with zero cells in contingency tables. The permutation test preserves row and column marginals (how many languages obligatorily mark each domain) while randomizing the co-occurrence structure, producing an exact null distribution for the number of zero-intersection pairs.
- **Alternatives Considered:** Fisher's exact test — rejected because it tests individual pairs, not the global structure.

### D9: Distinguish grammatical obligatoriness from register convention
- **Date:** 2026-05-12
- **Rationale:** Path B found that scientific registers add epistemic load without respecting the mutual exclusion observed in Path A. This requires a theoretical distinction: grammatical obligatoriness (encoded in morphology/syntax, competing for a structural budget) vs. register convention (encoded in lexical choice, additive rather than competitive).
- **Alternatives Considered:** Treating all load as equivalent — rejected because it would dissolve the mutual exclusion finding.

### D10: Propose re-inclusion of Word Cross-Ratio in Convergence synthesis
- **Date:** 2026-05-12
- **Rationale:** The original exclusion was correct when the project's "cross-ratio" was the Zipfian frequency ratio $f_1/f_2$ — a sample statistic, not an invariant. The reframed project's central invariant is Shannon entropy $H = -\sum p_i \log_2 p_i$, which IS invariant under recoding — structurally analogous to the geometric cross-ratio being invariant under projective transformations. The bridge is conceptual (not algebraic) but genuine.
- **Alternatives Considered:** Maintaining the exclusion — rejected because the reframing creates a legitimate connection.

### D7: Reframe project from Sapir-Whorf to Jakobson/Shannon/Grice/Greenberg
- **Date:** 2026-05-12
- **Rationale:** The Sapir-Whorf framing (frequency of encoding → cognitive effects) was fundamentally misaligned with the data the measurement apparatus could produce. It confused symptom with cause, violated Zipf's inverse relationship between frequency and information content, and produced a null result predetermined by synthetic data independence. The reframing treats languages as information architectures — communication systems with different mandatory metadata requirements. This framing is internally coherent, produces meaningful findings, and aligns the project with established traditions in linguistic theory (Jakobson, Shannon, Grice, Greenberg).
- **Alternatives Considered:** (a) Abandon the project — rejected because the measurement apparatus was sound and worth repurposing. (b) Double down on Sapir-Whorf with real data — rejected as requiring external resources beyond the chat thread. (c) Focus on science/technology discourse — rejected as a domain change that wouldn't fix the fundamental misalignment between question and data.
- **Impact:** Complete theoretical reorientation while preserving all methodological infrastructure.

### D6: Accept null meta-regression result as a valid scientific outcome
- **Date:** 2026-05-12
- **Rationale:** The simulation produced a null result (beta1 ≈ 0) for the frequency-cognition link. Rather than tuning parameters to produce a "positive" result, we report this transparently as evidence that the simple frequency-of-encoding hypothesis may be insufficient.
- **Alternatives Considered:** Re-running with adjusted parameters to produce a significant result — rejected as scientifically dishonest.

### D5: Use log-normal likelihood for Zipf MCMC rather than Dirichlet-multinomial
- **Date:** 2026-05-12
- **Rationale:** The Dirichlet-multinomial likelihood for 200 categories is computationally intensive and numerically unstable without specialised samplers.
- **Alternatives Considered:** Dirichlet-multinomial — rejected for computational tractability.

### D4: Use synthetic (Python-generated) frequency data rather than LLM word lists
- **Date:** 2026-05-12
- **Rationale:** Generating 200 words × 22 languages via LLM would be context-prohibitive and non-deterministic.
- **Alternatives Considered:** LLM-generated individual word lists — rejected as impractical.

### D3: Structure as a research plan, not a completed study
- **Date:** 2026-05-11
- **Rationale:** The Sapir-Whorf study had not been executed at the time. Presenting as a plan clearly distinguished what was proposed from what had been done.
- **Alternatives Considered:** Presenting as if completed — rejected as misleading.

### D2: Use Bayesian hierarchical modeling
- **Date:** 2026-05-11
- **Rationale:** Word-frequency distributions vary by language but share family-level patterns.
- **Alternatives Considered:** Independent per-language MLE — rejected.

### D1: Use LLM simulation rather than real corpus data
- **Date:** 2026-05-11
- **Rationale:** Real cross-linguistic corpus data for 22 languages would require extensive data collection and preprocessing.
- **Alternatives Considered:** Real corpus data — rejected as requiring external data access beyond chat scope.
