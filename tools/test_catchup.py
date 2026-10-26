"""Tests for tools/ensemble_catchup.sh. Run: python3 -m unittest discover -s tools -p 'test_*.py'

Each test builds a throwaway legacy repository and a throwaway squash-imported copy of it in a temp directory (this needs git and bash)."""
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "ensemble_catchup.sh"
ENV = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.invalid", GIT_COMMITTER_NAME="t",
           GIT_COMMITTER_EMAIL="t@example.invalid", GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)


def git(cwd, *args, check=True):
    r = subprocess.run(["git", *args], cwd=cwd, env=ENV, capture_output=True, text=True)
    if check and r.returncode:
        raise AssertionError(f"git {' '.join(args)} failed: {r.stderr}")
    return r.stdout.strip()


def put(root, rel, text):
    p = Path(root, rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def commit(root, msg):
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", msg)
    return git(root, "rev-parse", "HEAD")


@unittest.skipUnless(shutil.which("git") and shutil.which("bash"), "needs git and bash")
class TestCatchup(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.legacy = Path(self.tmp, "legacy")
        self.repo = Path(self.tmp, "research")
        for d in (self.legacy, self.repo):
            d.mkdir()
            git(d, "init", "-q", "-b", "main")
        # The legacy repository as imported: its root files and one cycle.
        put(self.legacy, "README.md", "# ensemble pilot\n")
        put(self.legacy, "LICENSE", "license\n")
        put(self.legacy, "PROVENANCE.md", "old provenance\n")
        put(self.legacy, "cycle-1/alpha/grounding.md", "grounding\n")
        self.src = commit(self.legacy, "import point")
        # The squash merge: the same files under runs/, no ancestry, the legacy root replaced by this repository's own index.
        put(self.repo, "runs/README.md", "# runs index of this repository\n")
        put(self.repo, "runs/cycle-1/alpha/grounding.md", "grounding\n")
        put(self.repo, "provenance/IMPORT.json", json.dumps({"source_head": self.src}))
        commit(self.repo, "squash import")

    def legacy_gains(self, **files):
        for rel, text in files.items():
            put(self.legacy, rel.replace("__", "/"), text)
        return commit(self.legacy, "legacy moves on")

    def catchup(self, leg):
        git(self.repo, "fetch", "-q", str(self.legacy), leg)
        return subprocess.run(["bash", str(SCRIPT), leg], cwd=self.repo, env=ENV, capture_output=True, text=True)

    def is_ancestor(self, sha):
        return subprocess.run(["git", "merge-base", "--is-ancestor", sha, "HEAD"], cwd=self.repo, env=ENV).returncode == 0

    def test_links_history_and_takes_new_cycle_despite_readme_notice(self):
        # What happened on 2026-10-26: the legacy README became a notice while runs/README.md here is an index.
        leg = self.legacy_gains(**{"README.md": "# MOVED to qnfo-research\n", "cycle-2__beta__grounding.md": "new\n"})
        r = self.catchup(leg)
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        self.assertTrue(self.is_ancestor(self.src) and self.is_ancestor(leg))
        self.assertEqual((self.repo / "runs/README.md").read_text(), "# runs index of this repository\n")
        self.assertEqual((self.repo / "runs/cycle-2/beta/grounding.md").read_text(), "new\n")
        self.assertEqual(git(self.repo, "status", "--porcelain"), "")

    def test_link_changes_no_file(self):
        before = git(self.repo, "rev-parse", "HEAD^{tree}")
        r = self.catchup(self.src)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(self.is_ancestor(self.src))
        self.assertEqual(git(self.repo, "rev-parse", "HEAD^{tree}"), before)

    def test_second_run_is_a_noop(self):
        leg = self.legacy_gains(**{"README.md": "# MOVED\n", "cycle-2__beta__grounding.md": "new\n"})
        self.assertEqual(self.catchup(leg).returncode, 0)
        head = git(self.repo, "rev-parse", "HEAD")
        self.assertEqual(self.catchup(leg).returncode, 0)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), head)

    def test_a_root_file_this_repository_dropped_stays_dropped(self):
        leg = self.legacy_gains(**{"PROVENANCE.md": "legacy edit\n"})
        r = self.catchup(leg)
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        self.assertFalse((self.repo / "runs/PROVENANCE.md").exists())
        self.assertTrue(self.is_ancestor(leg))

    def test_a_conflict_inside_a_run_stops(self):
        put(self.repo, "runs/cycle-1/alpha/grounding.md", "edited here\n")
        commit(self.repo, "edit a run")
        leg = self.legacy_gains(**{"cycle-1__alpha__grounding.md": "edited there\n"})
        r = self.catchup(leg)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("conflict inside a run: runs/cycle-1/alpha/grounding.md", r.stderr)


if __name__ == "__main__":
    unittest.main()
