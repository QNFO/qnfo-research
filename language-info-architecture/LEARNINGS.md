# LEARNINGS: Language-Info-Architecture

---

### L11: Permutation tests detect structure that pairwise tests miss
- **Category:** METHODOLOGY
- **Issue:** Individual pairwise tests for mutual exclusion were mostly non-significant due to low base rates (e.g., only 2 languages have spatial obligation). A naive analysis would conclude "no significant mutual exclusion" — missing the global structure.
- **Solution:** The global permutation test aggregates across all pairs: 10 observed zero intersections vs. 3.7 expected under random assignment, $p < 0.0001$. The structure is real but requires a global test to detect because individual cells are sparsely populated.
- **Prevention:** For sparse contingency tables with structural constraints, use global permutation/distribution tests rather than pairwise tests. The signal may be in the pattern of zeros, not in any individual cell.
- **Cross-Project:** YES — applicable to any sparse typological/classification analysis.

### L12: Invariants come in different mathematical forms but share a conceptual role
- **Category:** METHODOLOGY
- **Issue:** The project was excluded from Cross-Ratio Convergence because the Zipfian cross-ratio $f_1/f_2$ is a sample statistic, not the projective invariant $(AC \cdot BD)/(BC \cdot AD)$. The algebraic forms are different.
- **Solution:** Shannon entropy $H = -\sum p_i \log_2 p_i$ is invariant under recoding — a different mathematical form but the same conceptual role: a dimensionless quantity that captures structural information and survives transformations of the representation. Invariants need not share algebraic form to share conceptual function.
- **Prevention:** When bridging domains, look for conceptual invariance (survives transformation, encodes structure) rather than algebraic identity (same formula). The concept is more transferable than the formula.
- **Cross-Project:** YES — critical for cross-domain synthesis.

### L13: Grammatical obligatoriness and register convention are additive, not competitive
- **Category:** METHODOLOGY
- **Issue:** Path B found that scientific registers increase epistemic load without reducing other mandatory loads — violating the mutual exclusion principle observed in Path A.
- **Solution:** Distinguish two types of mandatory information: grammatical obligatoriness (what the grammar forces, encoded morphosyntactically, competing for a finite structural budget) and register convention (what the discourse expects, encoded lexically, additive rather than competitive). The mutual exclusion principle applies to grammatical obligatoriness only.
- **Prevention:** When observing a pattern that holds at one level (grammar) but breaks at another (register), check whether the levels involve different encoding mechanisms. Grammar is structural; register is additive.
- **Cross-Project:** YES — relevant to any analysis spanning multiple levels of linguistic structure.

### L7: When the question is wrong, the apparatus may still be right
- **Category:** METHODOLOGY
- **Issue:** The Sapir-Whorf framing produced a null result that was predetermined by synthetic data independence — the question couldn't be answered with the data the pipeline generated.
- **Solution:** Rather than abandoning the project or forcing a positive result, we audited implicit assumptions, identified the deeper contribution, and reframed around Jakobson/Shannon/Grice/Greenberg. The same measurement apparatus, aimed at a better question, produced coherent and meaningful findings.
- **Prevention:** Before executing a study, ask "what can my data actually tell me?" not "what do I want my data to tell me?" The data from this project was always about information architecture — the Sapir-Whorf framing was imposed on it, not discovered in it.
- **Cross-Project:** YES — essential for any research project. The measurement apparatus is often more valuable than the initial hypothesis.

### L8: Mutual exclusion is a stronger signal than correlation
- **Category:** METHODOLOGY
- **Issue:** The Sapir-Whorf meta-regression looked for a positive correlation between frequency load and effect size and found none. The reframed analysis looked for co-occurrence patterns of mandatory categories and found a striking zero intersection.
- **Solution:** A zero cell in a contingency table (0 languages with both epistemic AND ontological obligation) is a stronger finding than a weak correlation coefficient. Absence of co-occurrence in a well-chosen sample is evidence for a universal constraint. Correlation analysis can miss structural relationships that contingency analysis reveals.
- **Prevention:** For cross-linguistic typology, always check for mutual exclusion patterns before running regressions. The design space of languages may be characterized more by what combinations are impossible than by what tendencies exist.
- **Cross-Project:** YES — applicable to any typological or comparative analysis.

### L9: Shannon entropy per morpheme is a more stable cross-linguistic metric than entropy per word
- **Category:** METHODOLOGY
- **Issue:** Entropy per word-form conflates morphological complexity with information density. Polysynthetic languages have high word-level entropy because each "word" is a clause, not because they carry more information per linguistic unit.
- **Solution:** Normalizing by estimated morphemes per word produces a per-morpheme entropy measure that reverses the gradient: isolating languages carry 5.90 bits/morpheme vs. polysynthetic at 1.70 bits/morpheme. This makes theoretical sense — each morpheme in an isolating language must carry more information because there are fewer morphemes per word.
- **Prevention:** Always normalize cross-linguistic measures by a linguistically meaningful denominator. "Per word" is a writing-system artifact, not a linguistic universal.
- **Cross-Project:** YES — critical for any cross-linguistic quantitative analysis.

### L10: The Jakobson framing solves problems the Sapir-Whorf framing creates
- **Category:** METHODOLOGY
- **Issue:** Three fundamental problems with the original framing: (1) it reversed causal direction (frequency is a symptom of obligatoriness, not a cause of cognition), (2) it violated Zipf's own logic (high frequency = low information, the opposite of what the hypothesis needed), and (3) it required cross-domain commensurability that doesn't exist.
- **Solution:** Jakobson's mandatory/optional distinction provides a theoretically coherent framework: languages differ in what they MUST encode, and measuring that is informative about communication architecture regardless of cognitive effects. Shannon entropy provides a language-independent metric. Gricean surplus quantifies forced over-informativeness. Greenbergian universals provide testable predictions about co-occurrence constraints.
- **Prevention:** When a theoretical framework produces internal contradictions (like assuming high frequency = high importance while using a law that states the opposite), the framework needs replacement, not patching.
- **Cross-Project:** YES — the Jakobson/Shannon/Grice/Greenberg framework is a reusable template for cross-linguistic information-theoretic analysis.

### L6: Null results are scientifically important output
- **Category:** METHODOLOGY
- **Issue:** The meta-regression found no relationship between Whorfian frequency load and effect size.
- **Solution:** Report the null result transparently and interpret it substantively.
- **Prevention:** Pre-register evaluation criteria and commit to reporting results regardless of outcome.
- **Cross-Project:** YES.

### L5: Crossed-effects models require careful scope management
- **Category:** METHODOLOGY
- **Issue:** The original plan proposed a hierarchical model with language family as the sole grouping variable, but hypotheses were about morphological type.
- **Solution:** Use a crossed-effects model with both morphological type and language family as partially pooled factors.
- **Prevention:** Verify that grouping variables in the model match grouping variables in the hypotheses.
- **Cross-Project:** YES.

### L4: Log-normal likelihood is sufficient for Zipfian MCMC
- **Category:** PYTHON
- **Issue:** Dirichlet-multinomial likelihood is numerically unstable for 200 categories.
- **Solution:** Log-normal approximation is numerically stable and computationally efficient.
- **Prevention:** For compositional data with many categories, prefer normal approximations for general-purpose MCMC.
- **Cross-Project:** YES.

### L3: Python-based frequency simulation is more rigorous than LLM word-list generation
- **Category:** METHODOLOGY
- **Issue:** Generating 200 words × 22 languages via LLM was impractical and non-reproducible.
- **Solution:** Python-simulated frequency vectors from typologically informed Zipf parameters.
- **Prevention:** Distinguish what the LLM should generate (qualitative knowledge) from what code should generate (quantitative data).
- **Cross-Project:** YES.

### L2: The cross-ratio concept bridges linguistics and physics
- **Category:** METHODOLOGY
- **Issue:** The term cross-ratio was ambiguous between Zipfian and geometric meanings.
- **Solution:** Clarify the distinction while noting the deep analogy.
- **Prevention:** Define ambiguous terms explicitly at first use.
- **Cross-Project:** YES.

### L1: LLMs have usable parametric knowledge of word frequencies
- **Category:** METHODOLOGY
- **Issue:** Can an LLM generate realistic cross-linguistic word-frequency data?
- **Solution:** LLM parametric knowledge as a proxy — but must be validated against external sources.
- **Prevention:** Always validate LLM-generated quantitative data when possible.
- **Cross-Project:** YES.
