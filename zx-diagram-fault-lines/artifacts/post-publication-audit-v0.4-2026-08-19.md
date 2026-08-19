# Post-Publication Adversarial Audit — RES.015 v0.4 (2026-08-19)

Audited artifact: the v0.4 newversion content (post-publication appendix "Post-publication
evidence from QPL 2026", rebuilt paper, references.bib, citation-audit v0.4 addendum,
figures 1-2 + figure plan). Audit ran pre-publish against the pipeline milestone (the Zenodo
draft 22010380 is blocked on Zenodo's file service; the audit is valid for the milestone and
will be re-confirmed post-publish). READ-ONLY: no artifact file was modified by the audit.

Reviewer slots (CMD RED TEAM, 3-slot dispatch, all completed without stall):
- Accuracy (c2E_DOyJK_N4S5O-O6w5Q): CLEAN — 0 HARD / 2 SOFT.
- Completeness (dVtbL7a4HTjtZ9X44c8M6): 1 HARD / 3 SOFT.
- Dependency (qcX_EjOmkAcodIxPDHk2M): 2 HARD / 2 SOFT.

## Aggregate: 3 HARD / 7 SOFT

### HARD findings (remediation items R1-R3 — next cycle, before the publish retry)

- **HARD-1 (Completeness) — implementation-status over-claim in the practitioner paragraph.**
  "a code-design tool that runs today" (three-way normal form, paper 187) and "Each of these is
  working software" assert runnable software for papers whose QPL texts state algorithms, not
  implementations. Only paper 57's rank-width routine is documented as implemented (PyZX — the
  claim is verified in the paper's own text: "Our tensor contraction routine is implemented in
  PyZX"; the arXiv abstract alone does not state it). Violates the paper's own Abstract standard
  ("every claim is either an externally verified fact about the literature, or an explicitly
  marked argument").
  Fix: reword to "interconversion algorithms stated in the paper, implementable today" and
  "each of these is implementable with today's tools; the rank-width routine ships in PyZX".

- **HARD-2 (Dependency) — duplicate citation key `wan2026holographic` in references.bib.**
  Defined twice (same title/eprint 2601.04467; author variant "H. C. W. Price" vs
  "Henry C. W. Price"). Bib parsers silently keep the last definition — must dedupe to one key
  consistent with the paper's own reference list ([7] K. H. Wan, H. C. W. Price, Q. Yao).

- **HARD-3 (Dependency) — same paper under two keys: `comfort2026the` and `comfort2026delayed`**
  (Comfort/de Felice, arXiv:2607.04015). 28 @misc entries = 26 unique papers. Keep one key
  (prefer the v0.3-era key `comfort2026the`; no in-text cites use keys — the paper uses [n]
  numbering).

### SOFT findings (S1-S6)

- S1 (Dependency): stale bib header comment ("18 entries: 17 verified...") — update to
  28 entries / 26 unique with the v0.4 addendum note.
- S2 (Dependency): the GitHub provenance URL appears nowhere in the release set
  (publish-state records "related_identifiers isSupplementTo" without the literal link) —
  add the URL to README + publish-state record.
- S3 (Completeness): add arXiv:2601.08389 (dataflow/linear-optics, verified real by the
  reviewer) to the qpl2026-zx-cluster evidence-file table; add the PyZX-implementation
  primary-source citation (paper 57 PDF text) to the evidence file.
- S4 (Completeness): the negative claim "None of the nine performs the compatibility check"
  has no per-paper content trace in the evidence record — add a per-paper pointer to the
  import-provenance audit.
- S5 (Completeness): figures exist but are not wired into the .md body — planned for v0.5;
  do NOT publish v0.5 without adding the markdown image references.
- S6 (Accuracy): "Bearing on the audit" glosses are interpretive (acceptable framing, marked
  as such); "implemented in PyZX" claim is verified from the primary PDF (see HARD-1 note).

### Reviewer residual risks (resolved or accepted by parent)

- DOI 10.5281/zenodo.22010380: reserved via the API this session (reserve 201); draft state
  unsubmitted (blocked) — resolution to be re-verified at publish.
- QPL 2026 framing ("23rd", official submission URLs): verified this session from
  qplconference.org PDFs (primary sources).
- 2607.04015 evidence-file "none claimed" note: superseded by the falsifiability-sweep file
  (the correction is on record); the appendix cites the ID correctly.

## Disposition

Remediation items R1-R3 + S1-S4 fold into the next cycle (the publish retry of draft 22010380)
BEFORE the Zenodo publish, per the publish-then-audit loop. No artifact was modified by this
audit (READ-ONLY gate honored).
