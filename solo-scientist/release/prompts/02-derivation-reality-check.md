# Prompt 2: Derivation with Reality Check

> *Use this when you need an equation derived from first principles — with built-in verification.*

```
Derive [RESULT] from [STARTING POINT], showing all steps. Use standard
notation and explain any non-obvious algebraic manipulations.

After the derivation, run a reality check:
(a) Does the result have the correct physical dimensions? Show the
    dimensional analysis explicitly.
(b) Does it reduce to known cases in appropriate limits? Test at least
    two limits (e.g., t → 0, N → ∞, m → 0) and confirm the result
    matches existing knowledge.
(c) Are there any divergences, singularities, or discontinuities?
    Identify and characterize each one.
(d) Implement the key expression in Python using SymPy. Verify
    numerically for 3-5 test cases spanning different regimes.

If anything fails the reality check, diagnose the error and correct
the derivation. If the error is in the starting assumptions, flag
this explicitly.
```

### When to Use

- Developing new theoretical models
- Reproducing a known result as a sanity check before extending it
- Writing a methods section where the derivation is central

### What to Watch For

- The LLM may produce a mathematically "clean" but physically wrong result. The reality check catches this.
- SymPy verification is your best friend — if the code doesn't match the algebra, something is wrong.
- The human should verify the dimensional analysis — LLMs sometimes fake this convincingly.
