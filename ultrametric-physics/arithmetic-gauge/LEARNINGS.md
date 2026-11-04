# LEARNINGS: Arithmetic Gauge

---

### L1: Cross-ratio reframing unlocks deep unification
- **Category:** METHODOLOGY
- **Issue:** The fine-structure constant appeared mysterious when treated as a coupling strength.
- **Solution:** Reframing alpha as a length ratio and then as a process cross-ratio revealed it as a projective invariant.
- **Prevention:** When a physical constant seems mysterious, ask what two quantities of the same system are being compared.
- **Cross-Project:** YES

### L2: Companion notes beat monolithic papers for complex topics
- **Category:** METHODOLOGY
- **Issue:** The Kapustin-Witten construction spans multiple deep mathematical domains.
- **Solution:** Separate companion notes made the material accessible and modular.
- **Prevention:** Decompose complex expositions into independent self-contained companion notes.
- **Cross-Project:** YES

### L3: The Archimedean assumption is invisible until challenged
- **Category:** METHODOLOGY
- **Issue:** Standard QM assumes C with the Archimedean norm so deeply that alternatives are unthinkable.
- **Solution:** The Ultrametric Synthesis critique reveals this as a hidden assumption.
- **Prevention:** For any foundational framework, ask what changes under a different norm.
- **Cross-Project:** YES

### L4: Projection creates apparent irregularity from deterministic structure
- **Category:** METHODOLOGY
- **Issue:** Primes appear random on the number line; the halting problem appears undecidable.
- **Solution:** The Monna map provides the precise arithmetic mechanism for this scrambling.
- **Prevention:** When encountering apparent irregularity, ask if it is a property of the system or of the viewpoint.
- **Cross-Project:** YES

### L5: Consolidation reduces redundancy without losing provenance
- **Category:** METHODOLOGY
- **Issue:** Four projects with parallel 7-file documentation created 28 doc files with overlapping content.
- **Solution:** Consolidate into unified project with source in subdirectories. One set of unified docs.
- **Prevention:** When lines of inquiry converge, consolidate documentation rather than maintaining parallel structures.
- **Cross-Project:** YES

### L6: Equivocation weakens convergence arguments
- **Category:** METHODOLOGY
- **Issue:** Word Cross-Ratio used "cross-ratio" in a different sense (statistical ratio vs. projective invariant).
- **Solution:** Excise the project. Stronger with 4 genuine convergences than 5 with an equivocation.
- **Prevention:** Audit terminology before claiming mathematical identity. Shared name != shared structure.
- **Cross-Project:** YES


### L7: Verify repo root on session start to catch isolation violations
- **Category:** GIT
- **Issue:** The `.git/` directory lived at the parent `projects/` level, meaning all sibling projects shared one git history. This violates project isolation — a branch switch for one project would affect all others.
- **Solution:** `git init` inside the project directory, committed all files on feature branch, and `git rm --cached` from parent. Now each project can have its own independent git history.
- **Prevention:** Always run `git rev-parse --show-toplevel` at session start. If it returns a parent directory, fix isolation before any file operations.
- **Cross-Project:** YES — all projects under `G:\My Drive\projects\` should have independent repos.

### L8: Retroactive framing can create the illusion of consilience
- **Category:** METHODOLOGY
- **Issue:** The convergence synthesis (0.1.md) claimed four projects independently converged on the cross-ratio. A source-document audit revealed that 3 of 4 projects (Kapustin-Witten, Ultrametric Synthesis, Undecidability) never used the term "cross-ratio." The convergence was retroactively imposed by the capstone author, not independently discovered.
- **Solution:** Before claiming consilience, audit the source documents for the claimed common vocabulary. If the unifying concept appears only in the synthesis document and not in the source projects, the convergence is a framing choice, not a discovery.
- **Prevention:** When synthesizing multiple projects into a unified framework, distinguish between (a) concepts that appear natively in the source documents and (b) concepts imposed by the synthesis. The former supports consilience claims; the latter supports only that the framework can be applied as an interpretive lens.
- **Cross-Project:** YES — any multi-project synthesis should include a source-document vocabulary audit before claiming convergence.

### L9: Salvage requires trading the grand claim for the honest signal
- **Category:** METHODOLOGY
- **Issue:** The reader test showed the convergence synthesis was a retroactive framing, not a genuine discovery. The project could have been abandoned entirely, but a systematic vocabulary audit revealed a different convergence signal (projective geometry, tree structures, Archimedean/non-Archimedean tension) that was genuinely present across source documents.
- **Solution:** Rather than defending the over-claim, rebuild from the data. The vocabulary audit provided an objective basis for identifying what actually converges vs. what was imposed. The salvage document (0.28.md) trades the grand consilience narrative for a smaller, sharper, testable research program.
- **Prevention:** When a project's central claim is undermined by evidence, don't abandon the project -- audit the source materials for what genuinely overlaps and rebuild from there. The signal may be different from what was claimed, but it may still be interesting.
- **Cross-Project:** YES -- any multi-project synthesis that fails reader testing should undergo vocabulary audit before being abandoned.

