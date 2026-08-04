# Prompt 3: Code Prototyping

> *Use this to turn a research idea into a working, verified script — fast.*

```
Write a self-contained Python script that [TASK].

Requirements:
(a) Uses only the Python standard library plus numpy and scipy.
    Document any additional dependencies and justify them.
(b) Includes test cases that verify correctness. For each function,
    include at least one test the LLM can run to confirm it works.
(c) Saves results in a structured format (JSON or CSV) with timestamps
    and parameter metadata — so the output is self-documenting.
(d) Generates at least one publication-quality figure using matplotlib.
    Include axis labels, legend, and a descriptive title.
(e) Document all assumptions, parameter choices, and known limitations
    in comments at the top of the file.

After writing the script, run it and show the output. If it fails,
diagnose the error, fix it, and re-run until it succeeds.
```

### When to Use

- Prototyping a new analysis or simulation
- Generating figures for a paper
- Creating a reproducible pipeline for data processing

### What to Watch For

- The LLM will produce working code quickly — but may miss edge cases. The test cases requirement helps catch this.
- Check the generated figure for publication quality. The LLM often produces passable-but-ugly plots.
- If the script takes more than 3 iterations to debug, the task may be too ambitious. Simplify and iterate.
