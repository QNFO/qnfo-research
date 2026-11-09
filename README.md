# qnfo-research

QNFO/QWAV **research artifact repository**: the published papers, the pipeline runs that produced them, and the project
repositories merged earlier. Since 2026-10-26 it is the single home of all of it: `qnfo-ensemble-research` was folded
in with its full history (`git subtree`); the pipeline writes here from qnfo-research-exec 0.35.0.

| Where | What |
|---|---|
| `papers/<slug>/`, `<program>/<slug>/` | a published paper (`paper.md`, `README.md`) and its `provenance.json` |
| `runs/cycle-<N>/<slug>/` | the run that produced a paper: grounding, drafts, review, verification, `MANIFEST.json`, `ro-crate-metadata.json` |
| `provenance/` | `known-gaps.json` (the ratchet), `IMPORT.json` (where `runs/` came from) |
| `docs/` | `PROVENANCE-STANDARD.md`, `REPOSITORY-AUDIT-2026-10-26.md`, `RESEARCH-PROCEDURE.md` |
| `tools/provenance.py` | `verify`, `backfill`, `reproduce`, `index` (standard library only) |
| `schemas/` | JSON Schemas for the two record types |
| member directories | the eight project repositories merged on 2026-08-04 (table below) |

```
python3 tools/provenance.py verify                       # integrity, completeness, linkage: exit 1 on any error
python3 tools/provenance.py reproduce runs/cycle-396/<slug>
python3 tools/provenance.py reproduce --all
```

Cite the repository with `CITATION.cff`; cite a paper by its address `https://papers.qnfo.org/papers/<slug>`.

## Author

[Rowan Brad Quni-Gudzinas](https://rwnq8.github.io) is a systems researcher studying autonomous AI systems: how they
behave, fail and can be audited and governed. The pipeline that writes this repository is that kind of system in
production, an autonomous research system that drafts, referees, revises, publishes and corrects papers. Its
objectives, costs and failure record are published in
[Operating the Quniverse Fleet](https://doi.org/10.5281/zenodo.23079905).

## Member project repositories (merged 2026-08-04, each by `git subtree`, history preserved)

| Project repo | Subdirectory | Original URL |
|---|---|---|
| `measurable-vs-imaginable` | `measurable-vs-imaginable/` | [github.com/rwnq8/measurable-vs-imaginable](https://github.com/rwnq8/measurable-vs-imaginable) |
| `pattern-based-ontology` | `pattern-based-ontology/` | [github.com/rwnq8/pattern-based-ontology](https://github.com/rwnq8/pattern-based-ontology) |
| `silent-radix` | `silent-radix/` | [github.com/rwnq8/silent-radix](https://github.com/rwnq8/silent-radix) |
| `pqs-ai-evaluation-audit` | `pqs-ai-evaluation-audit/` | [github.com/rwnq8/pqs-ai-evaluation-audit](https://github.com/rwnq8/pqs-ai-evaluation-audit) |
| `joules-per-compute-benchmark` | `joules-per-compute-benchmark/` | [github.com/rwnq8/joules-per-compute-benchmark](https://github.com/rwnq8/joules-per-compute-benchmark) |
| `language-info-architecture` | `language-info-architecture/` | [github.com/rwnq8/language-info-architecture](https://github.com/rwnq8/language-info-architecture) |
| `solo-scientist` | `solo-scientist/` | [github.com/rwnq8/solo-scientist](https://github.com/rwnq8/solo-scientist) |
| `macroscopic-boundary-problem` | `macroscopic-boundary-problem/` | [github.com/rwnq8/macroscopic-boundary-problem](https://github.com/rwnq8/macroscopic-boundary-problem) |

## Provenance

[`docs/PROVENANCE-STANDARD.md`](docs/PROVENANCE-STANDARD.md) is the standard; [`PROVENANCE.md`](PROVENANCE.md) maps every
original repository to where it lives now (including DOIs); the audit that led to the consolidation, with its numbers, is
[`docs/REPOSITORY-AUDIT-2026-10-26.md`](docs/REPOSITORY-AUDIT-2026-10-26.md). Original repositories stay archived on
GitHub, not deleted.

## Research programs (folded 2026-11-04, history preserved)

Each program repository was merged by subtree into the directory of the same name; the original repositories are archived, not deleted.

| Directory | Original |
|---|---|
| `ultrametric-physics/` | QNFO/ultrametric-physics |
| `laws-of-form/` | QNFO/laws-of-form |
| `cfpe/` | QNFO/cfpe |
| `infomatics/` | QNFO/infomatics |
| `odr-thesis/` | QNFO/odr-thesis |
| `adelic-shannon-theory/` | QNFO/adelic-shannon-theory |
| `qec-darwinism-ultrametric/` | QNFO/qec-darwinism-ultrametric |
| `consilient-gap-synthesis/` | QNFO/consilient-gap-synthesis |
| `reentrant-distinctions/` | QNFO/reentrant-distinctions |
| `informational-universe/` | QNFO/informational-universe |
| `revolutionary-quantum-guide/` | QNFO/revolutionary-quantum-guide |
| `cwi-qec-poster-2026/` | QNFO/cwi-qec-poster-2026 |
