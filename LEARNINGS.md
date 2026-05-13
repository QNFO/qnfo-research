# LEARNINGS — LLM Force Multiplier

> Project-specific lessons. Machine-readable format for kaizen engine.
> Cross-Project: YES lessons are candidates for `_shared/CROSS-PROJECT-LEARNINGS.md`.

---

### L1: Self-contained git repos prevent cross-project contamination
- **Category:** GIT
- **Issue:** Project was in a shared parent repo at `G:\My Drive\projects\.git`, mixing multiple projects on the same branches. Cross-project file deletions from Language-Info-Architecture were staged on the branch.
- **Solution:** Initialized standalone `.git` inside `G:\My Drive\projects\LLM Force Multiplier\`. Now fully isolated.
- **Prevention:** Agent startup checks `git rev-parse --show-toplevel` must equal project path.
- **Cross-Project:** YES (already documented as CPL L1)

### L2: The force-multiplier protocol is self-demonstrating
- **Category:** METHODOLOGY
- **Issue:** The meta-project's thesis ("one day of focused human direction") was proven by generating the playbook + mini-paper + derivation demo in a single session (~30 min).
- **Solution:** The project itself serves as evidence. Every future session should document its own amplification metrics.
- **Prevention:** Track time-to-output in every session as continuous validation of the methodology.
- **Cross-Project:** NO (specific to this meta-research project)

### L3: LLM self-correction on mathematical errors is possible but requires human steering
- **Category:** METHODOLOGY
- **Issue:** In the live derivation demo (0.1.3.md Part IV), the LLM initially produced a divergent vacuum energy expression ($p^{3p}$). The LLM self-corrected after noting the divergence but overcorrected to exponential suppression. The human then steered to the correct power-law regime.
- **Solution:** The LLM can detect inconsistencies but may not converge to the right answer without domain-expert human guidance. The verification cycle is essential.
- **Prevention:** Always include a "Reality Check" prompt after derivation prompts. The human must verify limits and physical dimensions.
- **Cross-Project:** YES (LLM mathematical hallucination is domain-independent)

### L4: Versioned file naming enables rapid iteration within a flat directory
- **Category:** FILE-MGMT
- **Issue:** The project uses versioned filenames (0.1.md, 0.1.1.md, 0.1.2.md, 0.1.3.md) within a single flat directory. This simplifies cross-referencing and preserves chronological order.
- **Solution:** Continue the convention. Next output files should be 0.2.0.md, etc.
- **Prevention:** Use Python to scan for next available version before creating any file.
- **Cross-Project:** YES (this is standardized in the system prompt)

### L5: Reader-testing catches contradictions invisible to the author
- **Category:** METHODOLOGY
- **Issue:** The manuscript's Section 5.2 specified an 8-hour experiment cap, while Section 5.4 used 200-hour effect size estimates. This logical contradiction was undetected through two rounds of self-review but immediately obvious to a reader who didn't know the case study's background.
- **Solution:** Run every manuscript through a blind reader test (fresh LLM with zero context). Catch contradictions before human readers do.
- **Prevention:** After every substantive manuscript edit, feed the document to a SELF-CLONE with targeted reader questions. Fix issues before declaring the document complete.
- **Cross-Project:** YES (applies to all document production)

### L6: Describe the architecture that WAS used, not the one you wish you'd used
- **Category:** METHODOLOGY
- **Issue:** The manuscript's Section 3 originally described a Docker/API/Overleaf stack that was never used to produce any results. The actual architecture—DeepChat conversation with integrated file I/O, Python execution, and git—was simpler, faster (zero setup vs. 15 minutes), and had already produced two published papers. Describing an aspirational stack as if it were the actual implementation undermines credibility and obscures the real methodological insight: all you need is an LLM interface that can read/write files and run code.
- **Solution:** Rewrote Section 3 to describe the real architecture. Kept the Docker specification in Appendix C labeled as aspirational/future deployment. Added the Language as Information Architecture paper [26] as a second validation case study confirming the same architecture worked in a completely different domain.
- **Prevention:** When documenting methodology, audit every architectural claim: "Did we actually use this, or did we only design it?" Only the former belongs in the main text. Aspirational designs go in appendices or Future Work.
- **Cross-Project:** YES (applies to all methodology papers and technical documentation)
