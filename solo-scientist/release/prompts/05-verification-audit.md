# Prompt 5: Verification Audit

> *Use this before declaring any document complete. It catches what you and the LLM both missed.*

```
Audit this document for:

(a) Quantitative claims without evidence — flag every number, percentage,
    or comparison that isn't backed by a cited source or reproducible
    computation. For each, state what evidence is missing.
(b) Missing references — flag every claim that would need a citation
    in a peer-reviewed paper. Suggest a reference type (review, landmark
    paper, dataset) even if you can't name the specific paper.
(c) Internal contradictions — flag any two statements that cannot
    simultaneously be true. Quote both statements and explain the
    conflict.
(d) Ambiguous statements — flag any sentence that could be interpreted
    in more than one way. Explain the ambiguity and suggest a clearer
    formulation.
(e) Assumptions presented as facts — flag any statement that assumes
    something unproven but phrases it as established knowledge.

For each issue found:
1. Quote the problematic passage.
2. State what's wrong.
3. Suggest a specific fix (rewrite, add citation, qualify, delete).
```

### When to Use

- Before sharing a draft with collaborators
- Before submitting to a journal or posting to a preprint server
- As the final step in any force-multiplier session

### What to Watch For

- This prompt works best when the LLM hasn't seen the document before (use a fresh conversation).
- The LLM will flag things that aren't actually problems. Use judgment — you're the final arbiter.
- If the audit finds zero issues, something is wrong. Run it again with a different LLM instance.
