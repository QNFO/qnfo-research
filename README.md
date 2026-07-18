# qnfo-research

Shared research artifacts, distribution scripts, and one-off project tooling
for QNFO research projects that don't warrant a dedicated repository.

**This repository is for research/project content — never skill definitions.**
See [`QNFO/qnfo-skills`](https://github.com/QNFO/qnfo-skills) for the skill
system (ADR-026), and this repo's own scope boundary below (ADR-027).

## Scope

| Belongs here | Does NOT belong here |
|---|---|
| Research papers (`.md`, `.pdf`) not yet graduated to a dedicated repo | Skill definitions (`SKILL.md`, skill `scripts/`) — those go in `qnfo-skills` |
| One-off distribution/provenance scripts (Pinata, R2, DNSLink, D1 backfill) | Reusable skill tooling — skill scripts are generic/parameterized; these are hardcoded to specific papers/CIDs/DOIs |
| WBS plans, distribution manifests for shared/small projects | Long-lived program content once it outgrows this repo (see "Graduation" below) |
| Session debug/verification scripts (`test_cf_api.py`, `verify_tokens*.py`) | Anything belonging to `qnfo-skills`' own tag/release namespace |

## Current Contents

- `releases/core-pillars/` — 5 Core Pillar papers (MD + PDF), distribution manifest
- `paper1-decryption-key.md`, `paper2-anthropometric-fossils.md`,
  `whitepaper-adelic-freedom.md` — standalone publications
- `alpha-pi-helix/v1.1/computation/neutrino-mass-vortex.md` — supporting
  computation note (main project lives in dedicated repo `QNFO/alpha-pi-helix`
  where scale justified graduation — see "Graduation" below)
- `d1_backfill.py`, `d1_dns_backfill*.py`, `dnslink_create.py`,
  `distribute_core_pillars.py`, `pinata_upload.py`, `r2_upload*.py` —
  one-off distribution scripts for the Core Pillar papers (hardcoded CIDs/
  DOIs/paper titles; NOT reusable skill tooling — see distinction below)
- `test_cf_api.py`, `verify_tokens.py`, `verify_tokens_v2.py` — session
  debug/verification scripts used during Cloudflare API token setup

## Skill Scripts vs. Research Scripts (How to Tell Them Apart)

A recurring point of confusion: both `qnfo-skills` and `qnfo-research` contain
scripts that pin files to IPFS, upload to R2, or create DNSLink records. They
are NOT duplicates and NOT misplaced — they serve different purposes:

| | `qnfo-skills/<skill>/scripts/*.js` | `qnfo-research/*.py` |
|---|---|---|
| **Reusability** | Generic — takes file path, CID, bucket name as CLI args | Hardcoded — specific paper titles, DOIs, CIDs baked into the script body |
| **Language** | JavaScript (Node, matches skill script convention) | Python (matches this repo's convention) |
| **Lifecycle** | Long-lived, called by any future skill invocation | One-off, written for a single distribution event, kept for provenance/audit trail |
| **Where it belongs** | `qnfo-skills` (ADR-026) | `qnfo-research` or a dedicated project repo (ADR-027) |

If you find yourself writing a script that could be reused for ANY future
paper/project with different arguments — it's a skill script, and belongs in
`qnfo-skills/<skill>/scripts/`. If it's hardcoded to one specific
publication/distribution event — it belongs here.

## Graduation (Growing Into a Dedicated Repo)

Projects MAY start here and graduate to `QNFO/<project-name>` once file count/
complexity justifies isolation (ADR-027). This is a normal evolution — no ADR
update required, just a note in the project's own README pointing to its new
location. Example: `alpha-pi-helix` has both a supporting file here AND its
own dedicated repo (`QNFO/alpha-pi-helix`) for the main body of work.

## Tags and Releases

Unlike `qnfo-skills` (where tags/Releases are prohibited entirely — see
ADR-026), this repo MAY use tags/Releases for actual publication milestones
(e.g. a Zenodo DOI announcement release). **Before creating any tag/release
in ANY repo, always run `git remote -v` first** to confirm you are operating
on the intended repo — this is the single check that would have prevented
[ADR-026 Incident 3](https://github.com/QNFO/qnfo-skills/blob/master/ADR-026-skills-only.md),
where research-phase tags and a Zenodo-DOI Release were mistakenly created
inside `qnfo-skills` instead of a project repo.

## Related Policy

- [ADR-026](https://github.com/QNFO/qnfo-skills/blob/master/ADR-026-skills-only.md) — qnfo-skills is skills-only
- [ADR-027](https://github.com/QNFO/qnfo-skills/blob/master/ADR-027-research-separation.md) — research/skills separation, two approved patterns
