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
