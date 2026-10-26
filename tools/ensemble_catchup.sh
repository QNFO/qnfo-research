#!/usr/bin/env bash
# Links the history of QNFO/qnfo-ensemble-research into the checked-out branch and merges what that repository gained since.
# Run from the repository root with a git identity set; $1 is the legacy head, already fetched (the workflow passes FETCH_HEAD's sha).
# Nothing is rewritten: the link is a content-neutral merge (-s ours), the catch-up a subtree merge under runs/.
set -euo pipefail

LEG=${1:?usage: ensemble_catchup.sh <legacy head sha>}
SRC=$(python3 -c "import json;print(json.load(open('provenance/IMPORT.json'))['source_head'])")

# The repository merges squash-only, so the pull request that imported runs/ carried the files but dropped the imported commits.
# Record them as a parent of main without touching any file, then merge what the legacy repository gained since.
if ! git merge-base --is-ancestor "$SRC" HEAD; then
  git merge -s ours --allow-unrelated-histories --no-edit -m "Link the ensemble history (the import was squash-merged)" "$SRC"
fi

if ! git merge-base --is-ancestor "$LEG" HEAD; then
  if ! git merge -Xsubtree=runs --no-edit -m "Catch up runs/ with qnfo-ensemble-research (history kept)" "$LEG"; then
    # A conflict outside a cycle is the legacy repository's own root (its README, since 2026-10-26 a notice that points here; LICENSE,
    # PROVENANCE.md, RESEARCH-PROCEDURE.md) against what this repository replaced it with: this side wins, and a file it dropped stays dropped.
    # A conflict inside a cycle is a real divergence of a run's record and stops the catch-up.
    while IFS= read -r f; do
      [ -n "$f" ] || continue
      case "$f" in
        runs/cycle-*) echo "conflict inside a run: $f" >&2; exit 1 ;;
      esac
      if git cat-file -e "HEAD:$f" 2>/dev/null; then
        git checkout --ours -- "$f"
        git add -- "$f"
      else
        git rm -q -- "$f"
      fi
    done < <(git diff --name-only --diff-filter=U)
    git commit --no-edit
  fi
fi
