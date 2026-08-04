# The Force-Multiplier Playbook

## How One Scientist + One LLM Can Match a Research Team

> *A structured protocol turns the LLM from a chatbot into a force multiplier.*

**DOI:** [10.5281/zenodo.20154578](https://doi.org/10.5281/zenodo.20154578)
**License:** [CC BY 4.0](LICENSE.txt)

---

### The Problem

Modern science rewards big teams. The ATLAS collaboration has 3,000+ scientists. The average biomedical paper lists 6.5 authors. The solo scientist — once the default mode of discovery — is at a structural disadvantage, not because they lack ideas, but because they lack **throughput**: literature review, code prototyping, equation derivation, drafting.

### The Shift

LLMs crossed a threshold. They can now synthesize literature, derive and verify equations, generate and run code, and draft technical prose — all in a single conversation with file access and code execution.

### The Claim

A single researcher, following a structured five-phase protocol with an LLM, can reproduce the output of a small research team. Our preliminary self-experiments suggest speedups of $25\times$ to $90\times$ across two domains (theoretical physics, computational linguistics).

### The Stack (4 components — that's it)

| Component | Why |
|:----------|:----|
| **LLM Interface** | The brain |
| **File I/O** | Persistent state across turns |
| **Code Execution** | All quantitative claims verified |
| **Git** | Audit trail, reproducibility |

No Docker. No API keys. No multi-agent frameworks. A single conversation thread with file access and code execution is the entire architecture.

### The 5-Phase Protocol

| Phase | What Happens | Who Leads |
|:------|:-------------|:----------|
| **1. Define** | Frame the question, set success criteria | Human |
| **2. Delegate** | Issue structured prompts | Human → LLM |
| **3. Execute & Iterate** | LLM produces; human reviews; repeat | LLM + Human |
| **4. Verify** | Code checks, limit tests, reader test, human review | LLM + Human |
| **5. Synthesize** | Assemble final output | LLM |

### The 5 Prompts

Five reusable prompt patterns cover the full pipeline: Literature Synthesis, Derivation with Reality Check, Code Prototyping, Section Drafting, Verification Audit. → See [`prompts/`](prompts/)

### Try It Today

1. **Pick a research question** — something you'd normally budget a week for.
2. **Open an LLM conversation** with file access and code execution.
3. **Follow the five phases** (total: ~5 hours of focused time).
4. **Measure your speedup.** Compare against how long it would have taken alone.
5. **Report back.** → See [`CONTRIBUTING.md`](CONTRIBUTING.md)

### Read the Full Whitepaper

→ **[PLAYBOOK.md](PLAYBOOK.md)** — complete methodology, case studies, verification protocol, limitations, and call to action.

---

> *The bottleneck to scientific productivity could shift from team size to human creativity and LLM-fluency. The solo scientist is back.*
