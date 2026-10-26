"""Tests for tools/provenance.py. Run: python3 -m unittest discover -s tools -p 'test_*.py'

Every test builds a throwaway repository in a temp directory; nothing touches the real one and nothing needs git."""
import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import provenance as pv  # noqa: E402

REAL_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = 'import math\nprint("CLAIM Q1: computed=%.2e expected=1.0e0 match=yes" % math.exp(0))\n'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def write(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(text.encode("utf-8") if isinstance(text, str) else text)


def verification_md(code, stdout, stderr="", exit_code=0):
    body = stdout.rstrip("\n")
    if stderr:
        body += "\n\n[stderr]\n" + stderr.rstrip("\n")
    body += f"\n\n[exit {exit_code}]"
    return f"# Verification report\n\n## Script\n```python\n{code}\n```\n\n## Execution output\n```\n{body}\n```\n"


def make_repo(root, slug="alpha-paper", with_paper=True, manifest_extra=None):
    """A minimal repository: schemas, one pipeline run (v1 manifest shape) and, optionally, its deposited paper."""
    (root / "schemas").mkdir(parents=True)
    for n in ("paper-provenance.schema.json", "known-gaps.schema.json"):
        shutil.copy(REAL_ROOT / "schemas" / n, root / "schemas" / n)
    write(root / "LICENSE", "QNFO Unified License Agreement v2.1\n\nSPDX: LicenseRef-QNFO-ULA-2.1\n")
    run = root / "runs" / "cycle-2" / slug
    files = {
        "grounding.md": "# Grounding\nSee https://arxiv.org/abs/2401.00001 and doi:10.1000/xyz123.\n",
        "writer-a-draft.md": "# Draft A\n",
        "verification.py": SCRIPT,
        "verification.md": verification_md(SCRIPT, "CLAIM Q1: computed=1.00e+00 expected=1.0e0 match=yes"),
    }
    for fn, text in files.items():
        write(run / fn, text)
    man = {"pipeline": "0.8.0-artifact-deposit",
           "files": {fn: {"sha256": sha(t.encode()), "bytes": len(t)} for fn, t in files.items()}}
    man.update(manifest_extra or {})
    write(run / "MANIFEST.json", json.dumps(man, indent=2))
    if with_paper:
        write(root / "papers" / slug / "paper.md", "# Alpha Paper\n\n**Version:** 2.0.0\n\nBody.\n")
        write(root / "papers" / slug / "README.md", "# Alpha Paper\n\nDOI: 10.5281/zenodo.123456\nLicense: CC BY 4.0\n")
    return root


class Base(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        self.addCleanup(self._td.cleanup)

    def repo(self):
        return pv.Repo(self.root, use_git=False)

    def codes(self, rep, level=None):
        return sorted(f.code for f in rep.findings if level is None or f.level == level)


class TestManifestAndSchema(unittest.TestCase):
    def test_shapes(self):
        a = pv.normalize_manifest({"writers": {"writer-a": {"files": {"draft.md": "a" * 64}}},
                                   "reconciliation": {"files": {"RECONCILIATION.md": "b" * 64}},
                                   "shared_prompt_sha256": "c" * 64})
        self.assertEqual(a.shape, "A")
        self.assertEqual(set(a.files), {"writer-a/draft.md", "RECONCILIATION.md", "SHARED-PROMPT.md"})
        b = pv.normalize_manifest({"pipeline": "p", "files": {"x.md": {"sha256": "a" * 64, "bytes": 3}}})
        self.assertEqual((b.shape, b.pipeline), ("B", "p"))
        v2 = pv.normalize_manifest({"schema": pv.RUN_MANIFEST_V2, "files": {"x.md": {"sha256": "a" * 64, "bytes": 3}}})
        self.assertEqual(v2.shape, "V2")
        self.assertIsNone(pv.normalize_manifest([1, 2]))
        self.assertIsNone(pv.normalize_manifest({"nothing": 1}))

    def test_validator_subset(self):
        schema = {"type": "object", "required": ["a"], "additionalProperties": False,
                  "properties": {"a": {"type": "integer"}, "b": {"enum": ["x", "y"]}, "c": {"type": ["string", "null"], "pattern": "^z"}}}
        self.assertEqual(pv.validate({"a": 1, "b": "x", "c": None}, schema), [])
        self.assertTrue(pv.validate({}, schema))
        self.assertTrue(pv.validate({"a": True}, schema), "bool is not an integer")
        self.assertTrue(pv.validate({"a": 1, "b": "q"}, schema))
        self.assertTrue(pv.validate({"a": 1, "c": "nope"}, schema))
        self.assertTrue(pv.validate({"a": 1, "extra": 1}, schema))

    def test_roles(self):
        self.assertEqual(pv.role_of("writer-b-draft.md"), "draft")
        self.assertEqual(pv.role_of("writer-c/notes.md"), "draft-support")
        self.assertEqual(pv.role_of("review-report.md"), "review")
        self.assertEqual(pv.role_of("verification.py"), "verification-script")
        self.assertEqual(pv.role_of("zzz.bin"), "other")


class TestLinking(unittest.TestCase):
    def test_exact_suffix_and_unlinked(self):
        head = "braid-group-representations-modular-data-and-the-classification-of-majo"  # 71 chars
        self.assertEqual(len(head), 71)
        paper = head + "rana-zero"  # 80 chars, no suffix
        run_a = "runs/cycle-5/" + head + "-5099abb8"
        run_b = "runs/cycle-6/other-paper"
        linked, unlinked = pv.link_runs([paper, "other-paper"], [run_a, run_b, "runs/cycle-7/lonely-paper"])
        self.assertEqual(linked[paper], [(run_a, "slug-collision-suffix")])
        self.assertEqual(linked["other-paper"], [(run_b, "slug-exact")])
        self.assertEqual(unlinked, {"lonely-paper": ["runs/cycle-7/lonely-paper"]})

    def test_no_suffix_no_link(self):
        head = "x" * 71
        linked, unlinked = pv.link_runs([head + "-aaaa-bbbb"], ["runs/cycle-1/" + head + "-cccc-dddd"])
        self.assertEqual(linked, {})
        self.assertEqual(len(unlinked), 1)


class TestVerify(Base):
    def test_clean_repo_after_backfill(self):
        make_repo(self.root)
        changed = pv.backfill(self.repo(), "2026-10-26")
        self.assertEqual(changed["crates"], 1)
        self.assertEqual(changed["papers"], 1)
        rep = pv.verify(self.repo())
        self.assertEqual(self.codes(rep, "error"), [], [f.line() for f in rep.errors()])
        self.assertEqual(rep.stats["files_verified"], 4)
        self.assertGreaterEqual(rep.stats["crate_files_verified"], 5)

    def test_backfill_keeps_an_unchanged_reexecution_across_days_and_interpreters(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        cp = self.root / "runs/cycle-2/alpha-paper" / pv.CRATE_FILE
        before = cp.read_text()
        crate = json.loads(before)
        # the earlier observation was made on another interpreter
        for e in crate["@graph"]:
            if e.get("@id", "").startswith("#cpython-3"):
                e["@id"], e["version"] = "#cpython-3.12.1", "3.12.1"
            if e.get("@id") == "#verification-reexecution":
                e["instrument"] = {"@id": "#cpython-3.12.1"}
        cp.write_text(pv.dump_json(crate))
        edited = cp.read_text()
        self.assertEqual(pv.backfill(self.repo(), "2026-11-30"), {"crates": 0, "papers": 0, "gaps": 0})
        self.assertEqual(cp.read_text(), edited, "a later day on a newer interpreter does not rewrite the record")

    def test_a_changed_outcome_replaces_the_record(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        run = self.root / "runs/cycle-2/alpha-paper"
        (run / "verification.md").write_text((run / "verification.md").read_text().replace("computed=1.00e+00", "computed=2.00e+00"))
        # the manifest hash no longer matches; the re-execution verdict is what this test is about
        pv.backfill(self.repo(), "2026-11-30")
        crate = json.loads((run / pv.CRATE_FILE).read_text())
        act = next(e for e in crate["@graph"] if e["@id"] == "#verification-reexecution")
        self.assertEqual(act["qnfo:comparison"], "not-reproduced")
        self.assertEqual(act["endTime"], "2026-11-30")

    def test_backfill_is_idempotent(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        again = pv.backfill(self.repo(), "2026-10-26")
        self.assertEqual(again, {"crates": 0, "papers": 0, "gaps": 0})

    def test_hash_mismatch_is_never_tolerated(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        write(self.root / "runs/cycle-2/alpha-paper/writer-a-draft.md", "# Draft A, edited after collection\n")
        rep = pv.verify(self.repo())
        self.assertIn("HASH_MISMATCH", self.codes(rep, "error"))

    def test_missing_file_needs_a_gap_entry(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        (self.root / "runs/cycle-2/alpha-paper/writer-a-draft.md").unlink()
        self.assertIn("LISTED_FILE_MISSING", self.codes(pv.verify(self.repo()), "error"))
        pv.backfill(self.repo(), "2026-10-26", reproduce_runs=False)  # records the gap
        gaps = pv.load_gaps(self.repo())["gaps"]
        self.assertEqual([g["kind"] for g in gaps], ["manifest-file-missing"])
        self.assertIn("writer-a-draft.md", gaps[0]["expected_sha256"])
        rep = pv.verify(self.repo())
        self.assertEqual(self.codes(rep, "error"), [])
        self.assertEqual(rep.stats["known_gap_files_missing"], 1)

    def test_resolved_gap_is_flagged(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        run = self.root / "runs/cycle-2/alpha-paper"
        keep = (run / "writer-a-draft.md").read_text()
        (run / "writer-a-draft.md").unlink()
        pv.backfill(self.repo(), "2026-10-26", reproduce_runs=False)
        (run / "writer-a-draft.md").write_text(keep)
        rep = pv.verify(self.repo())
        self.assertIn("GAP_RESOLVED", self.codes(rep, "warn"))

    def test_run_without_manifest(self):
        make_repo(self.root)
        (self.root / "runs/cycle-2/alpha-paper/MANIFEST.json").unlink()
        self.assertIn("NO_MANIFEST", self.codes(pv.verify(self.repo()), "error"))

    def test_unlisted_file_error_only_for_v2(self):
        make_repo(self.root)
        write(self.root / "runs/cycle-2/alpha-paper/stray.md", "x")
        self.assertIn("UNLISTED_FILE", self.codes(pv.verify(self.repo()), "warn"))
        make_repo(self.root.parent / (self.root.name + "-v2"), manifest_extra={"schema": pv.RUN_MANIFEST_V2})
        v2root = self.root.parent / (self.root.name + "-v2")
        self.addCleanup(shutil.rmtree, v2root, True)
        write(v2root / "runs/cycle-2/alpha-paper/stray.md", "x")
        self.assertIn("UNLISTED_FILE", self.codes(pv.verify(pv.Repo(v2root, use_git=False)), "error"))

    def test_paper_text_missing_needs_gap_entry(self):
        make_repo(self.root, with_paper=False)
        self.assertIn("PAPER_TEXT_NOT_IN_REPO", self.codes(pv.verify(self.repo()), "error"))
        pv.backfill(self.repo(), "2026-10-26", reproduce_runs=False)
        rep = pv.verify(self.repo())
        self.assertEqual(self.codes(rep, "error"), [])
        self.assertEqual(rep.stats["known_gap_paper_text_missing"], 1)

    def test_paper_record_schema_and_snapshot_checks(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        pj = self.root / "papers/alpha-paper/provenance.json"
        rec = json.loads(pj.read_text())
        self.assertEqual(rec["declared"]["version"], "2.0.0")
        self.assertEqual(rec["declared"]["dois"][0], {"doi": "10.5281/zenodo.123456", "source": "README.md"})
        self.assertEqual(rec["declared"]["license"], "CC BY 4.0")
        self.assertEqual(rec["runs"][0]["match"], "slug-exact")
        rec["slug"] = 5
        pj.write_text(json.dumps(rec))
        self.assertIn("PAPER_SCHEMA", self.codes(pv.verify(self.repo()), "error"))
        rec["slug"] = "alpha-paper"
        pj.write_text(json.dumps(rec))
        write(self.root / "papers/alpha-paper/paper.md", "# Alpha Paper\n\nRevised body.\n")
        rep = pv.verify(self.repo())
        self.assertIn("PAPER_REVISED_UNRECORDED", self.codes(rep, "warn"))
        self.assertEqual(self.codes(rep, "error"), [])

    def test_backfill_keeps_old_snapshots(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        write(self.root / "papers/alpha-paper/paper.md", "# Alpha Paper\n\nRevised body.\n")
        pv.backfill(self.repo(), "2026-10-27")
        snaps = json.loads((self.root / "papers/alpha-paper/provenance.json").read_text())["snapshots"]
        self.assertEqual([s["recorded_at"] for s in snaps], ["2026-10-26", "2026-10-27"])


class TestCrate(Base):
    def crate(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        return json.loads((self.root / "runs/cycle-2/alpha-paper" / pv.CRATE_FILE).read_text())

    def test_structure_follows_the_profile(self):
        c = self.crate()
        g = {e["@id"]: e for e in c["@graph"]}
        self.assertEqual(c["@context"][0], pv.CRATE_CONTEXT)
        self.assertEqual(g[pv.CRATE_FILE]["conformsTo"]["@id"], pv.CRATE_SPEC)
        self.assertEqual(g["./"]["conformsTo"], [{"@id": pv.PROCESS_RUN_PROFILE}])
        self.assertEqual(g["./"]["author"]["@id"], pv.ORCID)
        self.assertEqual(g["grounding.md"]["sha256"], sha(b"# Grounding\nSee https://arxiv.org/abs/2401.00001 and doi:10.1000/xyz123.\n"))
        for aid in ("#grounding", "#drafting", "#verification-original", "#verification-reexecution"):
            self.assertEqual(g[aid]["@type"], "CreateAction", aid)
        self.assertEqual(g["#verification-reexecution"]["qnfo:comparison"], "reproduced-exact")
        self.assertEqual({o["@id"] for o in g["#grounding"]["object"]},
                         {"https://arxiv.org/abs/2401.00001", "https://doi.org/10.1000/xyz123"})

    def test_missing_listed_file_is_a_contextual_entity_not_a_part(self):
        make_repo(self.root)
        (self.root / "runs/cycle-2/alpha-paper/writer-a-draft.md").unlink()
        pv.backfill(self.repo(), "2026-10-26", reproduce_runs=False)
        c = json.loads((self.root / "runs/cycle-2/alpha-paper" / pv.CRATE_FILE).read_text())
        g = {e["@id"]: e for e in c["@graph"]}
        self.assertNotIn({"@id": "writer-a-draft.md"}, g["./"]["hasPart"])
        self.assertEqual(g["#missing/writer-a-draft.md"]["qnfo:status"], "listed-in-manifest-absent-from-repository")

    def test_crate_tampering_is_caught(self):
        self.crate()
        cp = self.root / "runs/cycle-2/alpha-paper" / pv.CRATE_FILE
        c = json.loads(cp.read_text())
        for e in c["@graph"]:
            if e["@id"] == "grounding.md":
                e["sha256"] = "0" * 64
        cp.write_text(json.dumps(c))
        self.assertIn("CRATE_HASH_MISMATCH", self.codes(pv.verify(self.repo()), "error"))

    def test_dangling_reference_is_caught(self):
        self.crate()
        cp = self.root / "runs/cycle-2/alpha-paper" / pv.CRATE_FILE
        c = json.loads(cp.read_text())
        c["@graph"][-1]["result"] = [{"@id": "no-such-file.md"}]
        cp.write_text(json.dumps(c))
        self.assertIn("CRATE_DANGLING", self.codes(pv.verify(self.repo()), "error"))

    def test_sources_regex(self):
        text = "arXiv:2401.00001, https://arxiv.org/pdf/hep-th/9901001 and https://doi.org/10.1103/PhysRevA.1.2."
        ids = {s["@id"] for s in pv.sources_of(text)}
        self.assertEqual(ids, {"https://arxiv.org/abs/2401.00001", "https://arxiv.org/abs/hep-th/9901001",
                               "https://doi.org/10.1103/PhysRevA.1.2"})


class TestBlobs(Base):
    def test_large_blob_and_pointer_rules(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        big = self.root / "papers/alpha-paper/big.bin"
        with open(big, "wb") as f:
            f.truncate(pv.MAX_BLOB_BYTES + 1)
        self.assertIn("LARGE_BLOB", self.codes(pv.verify(self.repo()), "error"))
        big.unlink()
        write(self.root / "runs/cycle-2/alpha-paper/figure.png.pointer.json", json.dumps({"sha256": "a" * 64, "bytes": 10, "store": "r2", "key": "sha256/aa/" + "a" * 62}))
        rep = pv.verify(self.repo())
        self.assertNotIn("BAD_POINTER", self.codes(rep, "error"))
        self.assertEqual(rep.stats["pointers"], 1)
        write(self.root / "runs/cycle-2/alpha-paper/other.pointer.json", json.dumps({"sha256": "nope"}))
        self.assertIn("BAD_POINTER", self.codes(pv.verify(self.repo()), "error"))


class TestReproduceAll(Base):
    def test_regression_is_reported(self):
        make_repo(self.root)
        pv.backfill(self.repo(), "2026-10-26")
        self.assertEqual(pv.reproduce_all(self.repo(), [0, 1]), 0)
        run = self.root / "runs/cycle-2/alpha-paper"
        md = (run / "verification.md").read_text().replace("computed=1.00e+00", "computed=2.00e+00")
        (run / "verification.md").write_text(md)
        self.assertEqual(pv.reproduce_all(self.repo(), [0, 1]), 1)


class TestReproduce(unittest.TestCase):
    def test_exec_string_mode_matches_the_pipeline(self):
        res = pv.reexecute("print(__file__)")
        self.assertEqual(res["exit"], 1)
        self.assertIn('File "<string>"', res["stderr"])
        self.assertIn("NameError", res["stderr"])

    def test_verdicts(self):
        ok = pv.reexecute("print('a')")
        self.assertEqual(pv.compare_record("a\n\n[exit 0]", ok), "reproduced-exact")
        self.assertEqual(pv.compare_record("b\n\n[exit 0]", ok), "not-reproduced")
        self.assertEqual(pv.compare_record(None, ok), "no-recorded-output")
        bad = pv.reexecute("import math\nmath.log(-1)")
        rec = "\n[stderr]\nTraceback (most recent call last):\n  File \"<string>\", line 2, in <module>\nValueError: math domain error\n\n[exit 1]"
        self.assertEqual(pv.compare_record(rec, bad), "reproduced-equivalent",
                         "an interpreter-version traceback layout difference is not a failure to reproduce")
        self.assertEqual(pv.compare_record(rec.replace("ValueError", "KeyError"), bad), "not-reproduced")
        self.assertEqual(pv.compare_record("x", {"timeout": True}), "timeout")

    def test_split_record(self):
        out, err, code = pv.split_record("line1\nline2\n\n[stderr]\nboom\n\n[exit 3]")
        self.assertEqual((out, err, code), ("line1\nline2", "boom", 3))
        self.assertEqual(pv.recorded_output("## Execution output\n```\nhi\n\n[exit 0]\n```\n"), "hi\n\n[exit 0]")

    def test_nondeterminism_is_detected(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        run = root / "runs" / "cycle-1" / "flaky"
        code = "import os\nprint(os.urandom(4).hex())\n"
        write(run / "verification.py", code)
        write(run / "verification.md", verification_md(code, "deadbeef"))
        out = pv.reproduce_run(pv.Repo(root, use_git=False), "runs/cycle-1/flaky", (0, 1, 2))
        self.assertTrue(out["nondeterministic"])
        self.assertEqual(out["verdict"], "not-reproduced")
        self.assertIsNone(out["stdout_sha256"])

    def test_reproduce_run_on_a_good_script(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = make_repo(Path(td.name))
        out = pv.reproduce_run(pv.Repo(root, use_git=False), "runs/cycle-2/alpha-paper", (0, 1, 2))
        self.assertEqual(out["verdict"], "reproduced-exact")
        self.assertFalse(out["nondeterministic"])
        self.assertEqual(len(out["stdout_sha256"]), 64)


class TestParity(unittest.TestCase):
    """tools/testdata/parity is shared byte-for-byte with qnfo-workers/qnfo-research-exec/testdata/parity. The JavaScript deposit
    (repo-deposit.mjs) wrote MANIFEST.json and the goldens' JS twins; this suite proves the Python builders produce the same
    bytes, so a backfill after a worker deposit rewrites nothing. To regenerate after a deliberate format change, run both
    builders on the fixture, compare, copy the output over golden/ here and in qnfo-workers, and bump the format version."""
    FIX = Path(__file__).resolve().parent / "testdata" / "parity"
    RUN = "runs/cycle-7/parity-paper"

    def test_crate_and_record_are_byte_identical_to_the_golden(self):
        repo = pv.Repo(self.FIX / "repo", use_git=False)
        man = pv.normalize_manifest(pv.read_json(repo.root / self.RUN / "MANIFEST.json")[0])
        crate = pv.build_crate(repo, self.RUN, man, (None, "2026-10-26T05:11:45+01:00"), None, "2026-10-26", "Parity Paper", None)
        self.assertEqual(pv.dump_json(crate), (self.FIX / "golden" / "ro-crate-metadata.json").read_text(encoding="utf-8"))
        rec = pv.build_paper_record(repo, "papers", "parity-paper", [(self.RUN, "slug-exact")], "2026-10-26", None)
        self.assertEqual(pv.dump_json(rec), (self.FIX / "golden" / "provenance.json").read_text(encoding="utf-8"))

    def test_a_worker_written_run_passes_verify(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            shutil.copytree(self.FIX / "repo", root)
            shutil.copy(self.FIX / "golden" / "ro-crate-metadata.json", root / self.RUN / pv.CRATE_FILE)
            shutil.copy(self.FIX / "golden" / "provenance.json", root / "papers" / "parity-paper" / "provenance.json")
            shutil.copytree(REAL_ROOT / "schemas", root / "schemas")
            rep = pv.verify(pv.Repo(root, use_git=False))
            self.assertEqual([f.line() for f in rep.errors()], [])
            self.assertEqual(rep.stats["files_verified"], 7)


class TestRealRepository(unittest.TestCase):
    """The committed repository must verify clean: this is the same check CI runs."""

    @unittest.skipUnless((REAL_ROOT / "provenance" / "known-gaps.json").exists(), "no ledger in this checkout")
    def test_committed_repository_verifies(self):
        rep = pv.verify(pv.Repo(REAL_ROOT, use_git=False))
        self.assertEqual([f.line() for f in rep.errors()][:5], [])


if __name__ == "__main__":
    unittest.main()
