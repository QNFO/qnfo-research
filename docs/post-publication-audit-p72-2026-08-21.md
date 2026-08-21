# Post-Publication Audit — QNFO.RES.021 P7.2 (2026-08-21)

**Audited artifact:** the PUBLISHED record 10.5281/zenodo.22044379 (concept
10.5281/zenodo.22044217, version 1.0.1, 29 files) together with its metadata,
deposited files, and the distribution stores (R2, D1 living-paper, KG,
program_registry).
**Mode:** READ-ONLY (no audited artifact modified; this report is the P7.2
deliverable).
**Seed (UIA v1.0.1 Q15):** "Does the published record — Zenodo metadata, deposited
files, and the public draft — preserve the 'supported within the per-distinction
model' wording and the L3 conjecture grade through the publication pipeline, or
does any publish-time rewrite quietly promote it?"

---

## Method (all live, this session)

- `GET /api/records/22044379` — metadata, files, state.
- Download-back of the deposited `finite-distinction-quantum-mechanics.md` and
  `README.md`; byte-compare against the audited repo state (branch head
  13e1d97, tag v1.0.1-published-res021).
- DataCite state checks for record + concept DOIs (P8 cycle).
- D1 living-paper / KG / program_registry read-backs (this session).
- R2 download-back md5 (P8 cycle).

## Seed answer: YES — the conjecture grade and the model-status disclosure survived the pipeline intact.

1. **Metadata description** (Zenodo): "unitary evolution and superposition are
   **conjectured** to emerge as the large-distinction limit of an entropy-Hessian
   flow" — conjecture-grade verbatim; probes confirm no "verified"/"supported"
   overclaim in the metadata.
2. **Deposited paper** (byte-identical to the audited repo, 29,475 B):
   - frontmatter: `doi: 10.5281/zenodo.22044379`, `concept_doi: 10.5281/zenodo.22044217`,
     `status: published`, version 1.0.1 — correct self-DOI discipline.
   - grade language: 15 occurrences of "conjecture" in the paper body; the
     SOFT-1 fix is present ("The **conjecture** (F5)"); **no** "verified at finite
     N" phrasing anywhere in the paper body.
   - the §9 model-assumption admission is deposited verbatim ("the per-distinction
     rate structure is a MODEL assumption, not a derived claim: its physical
     status ... is open").
3. **Deposited PROJECT-PLAN.md** carries the locked claim with the v1.0.1
   restatement ("supported at finite N within the per-distinction model; the
   physical status of the per-distinction rate structure remains open") and the
   full lock-record chain — the "supported" wording is preserved where it
   belongs (the lock record), not promoted anywhere in the publication prose.
4. **README / README-paper**: header DOI 10.5281/zenodo.22044379; "Cite all
   versions" = the concept DOI 10.5281/zenodo.22044217 (ZENODO-CONCEPT-DOI-CITE-1
   satisfied); no stale 2204410x references.

## Findings

### HARD: none (0)

### SOFT
- **S-1 (known, accepted):** `license: null` on the public records-API view —
  ZENODO-LICENSE-RTYPE-MUTUAL-EXCLUSION-1 (the deposit-API metadata PUT stored
  the license; the records-API view drops it). The paper frontmatter and both
  READMEs carry CC-BY-4.0. Documented, no action.
- **S-2 (cosmetic):** `pids.doi` is empty in the records-API GET view; the
  record ID is the DOI suffix (10.5281/zenodo.22044379), DataCite holds the
  DOI metadata, both DOIs findable. No action.

### OPEN (deferred, coordinated)
- **Duplicate-record hygiene:** the concurrent session's publication
  10.5281/zenodo.22044107 (concept 22044106) remains public as an unlinked
  duplicate of this canonical record. Remediation registered: add
  `isIdenticalTo` related-identifier links both ways (their v1.0.2 newversion
  per handoff 28675 can carry their side; this record can carry its side in the
  next newversion cycle or via a metadata-only edit if the platform permits).
  Canonical designation recorded in D1/KG/registry/wbs_state/handoffs.

## Distribution-store consistency (all read-back verified this session)

| Store | State |
|---|---|
| R2 qnfo-releases/2026/08/finite-distinction-quantum-mechanics/ | 29/29, download-back md5 match |
| D1 living-paper papers | identifier/doi 22044379, zenodo_doi 22044217, r2_key/path qnfo-releases/..., zenodo_url ✓ |
| KG paper node | doi 22044379, zenodo_doi 22044217, distribution_status distributed, r2_path with bucket prefix ✓ |
| KG project node | published_doi 22044379, concept_doi 22044217, phase P8, status published ✓ |
| program_registry | zenodo_doi 22044379, current_version 1.0.1, phase P8, status published ✓ |

## Verdict

**0 HARD · 2 SOFT (known/accepted) · 1 OPEN (duplicate hygiene, deferred).**
The published record faithfully preserves the audited state: byte-identical
deposited paper, correct self-DOI/concept-DOI discipline, conjecture-grade
wording throughout the pipeline, the model-assumption admission verbatim, and
all distribution stores consistent on the canonical DOI. The P8 UIA Q15 seed is
answered: no publish-time rewrite promoted the grade.
