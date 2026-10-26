#!/usr/bin/env python3
"""QNFO research provenance tool (standard library only, Python 3.9+).

One command line for the three things an auditor needs from this repository:

  verify     integrity, completeness and linkage checks over runs/, papers/ and the program directories
  backfill   write papers/<slug>/provenance.json, runs/**/ro-crate-metadata.json and provenance/known-gaps.json
  reproduce  re-execute a run's verification.py exactly the way the pipeline did and compare with the recorded output
  index      print the paper <-> run catalog as JSON lines

The standard it implements is docs/PROVENANCE-STANDARD.md. Nothing here reaches the network.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

TOOL_VERSION = "1.0.0"
PAPER_SCHEMA = "qnfo-paper-provenance/1"
GAPS_SCHEMA = "qnfo-known-gaps/1"
RUN_MANIFEST_V2 = "qnfo-run-manifest/2"

# Mirrors programFor() in qnfo-workers/qnfo-research-exec: where a deposited paper lives.
PROGRAM_DIRS = (
    "papers", "joules-per-compute-benchmark", "silent-radix", "alpha-pi-helix", "adelic-freedom",
    "arithmetic-quantum-thermodynamics", "margolus-levitin", "topological-spin", "jpcub-qec",
)
CRATE_FILE = "ro-crate-metadata.json"
CRATE_CONTEXT = "https://w3id.org/ro/crate/1.2/context"
CRATE_SPEC = "https://w3id.org/ro/crate/1.2"
PROCESS_RUN_PROFILE = "https://w3id.org/ro/wfrun/process/0.4"
QNFO_NS = "https://qnfo.org/ns/provenance#"
ORCID = "https://orcid.org/0009-0002-4317-5604"
AUTHOR_NAME = "Rowan Brad Quni-Gudzinas"
SIDECARS = {"MANIFEST.json", CRATE_FILE, ".gitkeep"}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
# Cloudflare Artifacts mirrors this repository and refuses a blob over 32 MB; stay well under it. A larger file lives
# in R2 under its sha256 and is committed as a <name>.pointer.json (docs/PROVENANCE-STANDARD.md, large files).
MAX_BLOB_BYTES = 25 * 1024 * 1024
POINTER_SUFFIX = ".pointer.json"


# --------------------------------------------------------------------------------------------- basics

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(p: Path) -> Tuple[Any, Optional[str]]:
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f), None
    except (OSError, ValueError) as e:
        return None, str(e)


def dump_json(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def write_if_changed(p: Path, text: str) -> bool:
    if p.exists() and p.read_text(encoding="utf-8") == text:
        return False
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return True


@dataclass
class Finding:
    level: str  # error | warn | info
    code: str
    path: str
    message: str

    def line(self) -> str:
        return f"{self.level.upper():5} {self.code:28} {self.path}: {self.message}"


def validate(instance: Any, schema: Dict[str, Any], path: str = "$") -> List[str]:
    """The JSON Schema subset the two schemas in schemas/ use: type, const, enum, required, properties,
    additionalProperties, items, pattern, minLength. The schema files stay the single source of truth."""
    errs: List[str] = []
    types = {"object": dict, "array": list, "string": str, "integer": int, "number": (int, float),
             "boolean": bool, "null": type(None)}
    if "const" in schema and instance != schema["const"]:
        errs.append(f"{path}: expected {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errs.append(f"{path}: {instance!r} not in {schema['enum']}")
    t = schema.get("type")
    if t is not None:
        ok = False
        for name in (t if isinstance(t, list) else [t]):
            if name in ("integer", "number") and isinstance(instance, bool):
                continue
            if isinstance(instance, types[name]):
                ok = True
        if not ok:
            errs.append(f"{path}: expected type {t}, got {type(instance).__name__}")
            return errs
    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errs.append(f"{path}: shorter than {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errs.append(f"{path}: does not match {schema['pattern']}")
    if isinstance(instance, dict):
        for k in schema.get("required", []):
            if k not in instance:
                errs.append(f"{path}: missing required '{k}'")
        props = schema.get("properties", {})
        for k, v in instance.items():
            if k in props:
                errs += validate(v, props[k], f"{path}.{k}")
            elif schema.get("additionalProperties") is False:
                errs.append(f"{path}: unexpected property '{k}'")
            elif isinstance(schema.get("additionalProperties"), dict):
                errs += validate(v, schema["additionalProperties"], f"{path}.{k}")
    if isinstance(instance, list) and "items" in schema:
        for i, v in enumerate(instance):
            errs += validate(v, schema["items"], f"{path}[{i}]")
    return errs


# ------------------------------------------------------------------------------------------- manifests

@dataclass
class Manifest:
    shape: str  # "A" cycle-1 pilot | "B" pipeline v1 | "V2" worker >= 0.35
    files: Dict[str, Dict[str, Any]]
    pipeline: Optional[str] = None
    raw: Dict[str, Any] = field(default_factory=dict)


def normalize_manifest(obj: Any) -> Optional[Manifest]:
    """Both historical manifest shapes and the v2 shape reduce to {relative path: {sha256, bytes?}}."""
    if not isinstance(obj, dict):
        return None
    files: Dict[str, Dict[str, Any]] = {}
    if "writers" in obj:  # shape A: the cycle-1 pilot, hashes only
        for w, wm in (obj.get("writers") or {}).items():
            for fn, h in ((wm or {}).get("files") or {}).items():
                files[f"{w}/{fn}"] = {"sha256": h}
        for fn, h in ((obj.get("reconciliation") or {}).get("files") or {}).items():
            files[fn] = {"sha256": h}
        if obj.get("shared_prompt_sha256"):
            files["SHARED-PROMPT.md"] = {"sha256": obj["shared_prompt_sha256"]}
        return Manifest("A", files, None, obj)
    if isinstance(obj.get("files"), dict):
        for fn, meta in obj["files"].items():
            if isinstance(meta, dict):
                files[fn] = {"sha256": meta.get("sha256"), "bytes": meta.get("bytes")}
        shape = "V2" if obj.get("schema") == RUN_MANIFEST_V2 else "B"
        return Manifest(shape, files, obj.get("pipeline"), obj)
    return None


ROLE_PATTERNS = [
    (re.compile(r"^SHARED-PROMPT\.md$"), "prompt"),
    (re.compile(r"^grounding\.md$"), "grounding"),
    (re.compile(r"^writer-[a-z]-draft\.md$|^writer-[a-z]/draft\.md$"), "draft"),
    (re.compile(r"^writer-[a-z]/(notes|claims)\.md$"), "draft-support"),
    (re.compile(r"^(reconciled-paper|RECONCILIATION|citation-audit)\.md$|^reconciled\.md$"), "reconciliation"),
    (re.compile(r"^review-report(-\d+)?\.md$"), "review"),
    (re.compile(r"^verification\.md$"), "verification-report"),
    (re.compile(r"^verification\.py$"), "verification-script"),
    (re.compile(r"^MANIFEST\.json$"), "manifest"),
]


def role_of(rel: str) -> str:
    for rx, role in ROLE_PATTERNS:
        if rx.search(rel):
            return role
    return "other"


def mime_of(rel: str) -> str:
    return {".md": "text/markdown", ".py": "text/x-python", ".json": "application/json",
            ".txt": "text/plain"}.get(os.path.splitext(rel)[1], "application/octet-stream")


# ------------------------------------------------------------------------------------------ repository

class Repo:
    def __init__(self, root: Path, use_git: bool = True):
        self.root = root.resolve()
        self.use_git = use_git and (self.root / ".git").exists()
        self._import: Optional[Dict[str, Any]] = None

    def rel(self, p: Path) -> str:
        return p.resolve().relative_to(self.root).as_posix()

    def git(self, *args: str) -> Optional[str]:
        if not self.use_git:
            return None
        try:
            r = subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, timeout=120)
        except (OSError, subprocess.TimeoutExpired):
            return None
        return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else None

    @property
    def import_info(self) -> Dict[str, Any]:
        if self._import is None:
            obj, _ = read_json(self.root / "provenance" / "IMPORT.json")
            self._import = obj if isinstance(obj, dict) else {}
        return self._import

    def legacy_adds(self) -> Dict[str, Tuple[str, str]]:
        """path (as it was in qnfo-ensemble-research) -> (commit, committer date) of the commit that added it.
        The subtree merge keeps the source history as the merge's second parent, so no outside clone is needed."""
        head = self.import_info.get("source_head")
        if not head:
            return {}
        out = self.git("log", head, "--reverse", "--diff-filter=A", "--name-only", "--format=@@%H %cI")
        adds: Dict[str, Tuple[str, str]] = {}
        cur: Optional[Tuple[str, str]] = None
        for line in (out or "").splitlines():
            if line.startswith("@@"):
                sha, _, date = line[2:].partition(" ")
                cur = (sha, date)
            elif line.strip() and cur and line not in adds:
                adds[line] = cur
        return adds

    def discover_runs(self) -> List[str]:
        """Run directories, relative to the root: runs/cycle-N (the cycle-1 pilot, one manifest for the cycle) and
        runs/cycle-N/<slug> for every other cycle, whether or not the manifest survived."""
        base = self.root / "runs"
        runs: List[str] = []
        if not base.is_dir():
            return runs
        for c in sorted((d for d in base.iterdir() if d.is_dir() and d.name.startswith("cycle-")),
                        key=lambda d: int(re.sub(r"\D", "", d.name) or 0)):
            if (c / "MANIFEST.json").is_file():
                runs.append(self.rel(c))
                continue
            for s in sorted(d for d in c.iterdir() if d.is_dir()):
                runs.append(self.rel(s))
        return runs

    def discover_papers(self) -> List[Tuple[str, str]]:
        """(program directory, slug) for every <program>/<slug>/paper.md."""
        out: List[Tuple[str, str]] = []
        for prog in PROGRAM_DIRS:
            d = self.root / prog
            if not d.is_dir():
                continue
            for s in sorted(x for x in d.iterdir() if x.is_dir()):
                if (s / "paper.md").is_file():
                    out.append((prog, s.name))
        return out


def slug_of_run(run_rel: str) -> Optional[str]:
    parts = run_rel.split("/")
    return parts[2] if len(parts) >= 3 else None


def cycle_of_run(run_rel: str) -> str:
    return run_rel.split("/")[1]


HEX_SUFFIX = re.compile(r"-[0-9a-f]{8}$")


def link_runs(paper_slugs: Iterable[str], run_rels: Iterable[str]) -> Tuple[Dict[str, List[Tuple[str, str]]], Dict[str, List[str]]]:
    """Join runs to deposited papers by slug. A slug is cut at 80 characters; when two cut slugs collide the pipeline
    replaces the tail with '-' + the first 8 hex characters of the research_queue row id, so a run and its paper can
    carry different tails of the same 71-character head (match = slug-collision-suffix). Returns
    ({paper slug: [(run, match)]}, {unlinked run slug: [run]})."""
    papers = set(paper_slugs)
    heads: Dict[str, List[str]] = {}
    for p in papers:
        if len(p) == 80:
            heads.setdefault(p[:71], []).append(p)
    linked: Dict[str, List[Tuple[str, str]]] = {}
    unlinked: Dict[str, List[str]] = {}
    for rp in run_rels:
        s = slug_of_run(rp)
        if not s:
            continue
        if s in papers:
            linked.setdefault(s, []).append((rp, "slug-exact"))
            continue
        cand = [p for p in heads.get(s[:71], []) if len(s) == 80 and (HEX_SUFFIX.search(p) or HEX_SUFFIX.search(s))]
        if len(cand) == 1:
            linked.setdefault(cand[0], []).append((rp, "slug-collision-suffix"))
        else:
            unlinked.setdefault(s, []).append(rp)
    return linked, unlinked


# ---------------------------------------------------------------------------------------- known gaps

def load_gaps(repo: Repo) -> Dict[str, Any]:
    obj, _ = read_json(repo.root / "provenance" / "known-gaps.json")
    return obj if isinstance(obj, dict) else {"schema": GAPS_SCHEMA, "as_of": "", "gaps": []}


def gap_id(prefix: str, path: str) -> str:
    """Stable and collision-free: the prefix names the kind, the hash pins the path (slug heads repeat across cycles)."""
    return f"GAP-{prefix}-{sha256_bytes(path.encode('utf-8'))[:10]}"


def gap_index(gaps: Dict[str, Any]) -> Dict[Tuple[str, str], Dict[str, Any]]:
    return {(g["kind"], g["path"]): g for g in gaps.get("gaps", []) if "kind" in g and "path" in g}


# --------------------------------------------------------------------------------------- verification

@dataclass
class Report:
    findings: List[Finding] = field(default_factory=list)
    stats: Dict[str, int] = field(default_factory=dict)

    def add(self, level: str, code: str, path: str, message: str) -> None:
        self.findings.append(Finding(level, code, path, message))

    def count(self, key: str, n: int = 1) -> None:
        self.stats[key] = self.stats.get(key, 0) + n

    def errors(self) -> List[Finding]:
        return [f for f in self.findings if f.level == "error"]

    def warnings(self) -> List[Finding]:
        return [f for f in self.findings if f.level == "warn"]


def check_run(repo: Repo, run_rel: str, gaps: Dict[Tuple[str, str], Dict[str, Any]], rep: Report) -> None:
    run = repo.root / run_rel
    mpath = run / "MANIFEST.json"
    rep.count("runs")
    present = {p.relative_to(run).as_posix() for p in run.rglob("*") if p.is_file()}
    if not mpath.is_file():
        if ("run-without-manifest", run_rel) in gaps:
            rep.count("known_gap_runs_without_manifest")
            rep.add("info", "GAP_NO_MANIFEST", run_rel, "no MANIFEST.json (recorded in provenance/known-gaps.json)")
        else:
            rep.add("error", "NO_MANIFEST", run_rel, "run has no MANIFEST.json and no gap entry")
        return
    obj, err = read_json(mpath)
    man = normalize_manifest(obj) if err is None else None
    if man is None:
        rep.add("error", "MANIFEST_UNREADABLE", run_rel, err or "unrecognised manifest shape")
        return
    missing_known = (gaps.get(("manifest-file-missing", run_rel)) or {}).get("files", [])
    for fn, meta in sorted(man.files.items()):
        want = meta.get("sha256")
        fp = run / fn
        if not fp.is_file():
            if fn in missing_known:
                rep.count("known_gap_files_missing")
                continue
            rep.add("error", "LISTED_FILE_MISSING", f"{run_rel}/{fn}", "listed in MANIFEST.json, absent, no gap entry")
            continue
        if fn in missing_known:
            rep.add("warn", "GAP_RESOLVED", f"{run_rel}/{fn}", "file is present again; drop it from provenance/known-gaps.json")
        if not isinstance(want, str) or not SHA_RE.match(want):
            rep.add("error", "MANIFEST_BAD_HASH", f"{run_rel}/{fn}", f"not a sha256: {want!r}")
            continue
        if sha256_file(fp) != want:
            rep.add("error", "HASH_MISMATCH", f"{run_rel}/{fn}", "content differs from the hash frozen in MANIFEST.json")
        else:
            rep.count("files_verified")
            if man.shape == "V2" and meta.get("bytes") is not None and fp.stat().st_size != meta["bytes"]:
                rep.add("error", "SIZE_MISMATCH", f"{run_rel}/{fn}", "size differs from MANIFEST.json bytes")
            elif man.shape == "B" and meta.get("bytes") is not None and fp.stat().st_size != meta["bytes"]:
                rep.count("v1_bytes_is_char_count")  # v1 recorded a UTF-16 length, not bytes; the hash is the check
    unlisted = sorted(f for f in present - set(man.files) if os.path.basename(f) not in SIDECARS)
    for fn in unlisted:
        lvl = "error" if man.shape == "V2" else "warn"
        rep.add(lvl, "UNLISTED_FILE", f"{run_rel}/{fn}", "file in run directory is not in MANIFEST.json")
    crate = run / CRATE_FILE
    if crate.is_file():
        check_crate(repo, run_rel, crate, man, rep)
    elif (repo.root / "provenance" / "known-gaps.json").exists():
        rep.add("warn", "NO_CRATE", run_rel, f"{CRATE_FILE} missing; run `provenance.py backfill`")


def check_crate(repo: Repo, run_rel: str, crate: Path, man: Manifest, rep: Report) -> None:
    obj, err = read_json(crate)
    where = f"{run_rel}/{CRATE_FILE}"
    if err or not isinstance(obj, dict) or not isinstance(obj.get("@graph"), list):
        rep.add("error", "CRATE_UNREADABLE", where, err or "no @graph")
        return
    ents = {e.get("@id"): e for e in obj["@graph"] if isinstance(e, dict)}
    root = ents.get("./")
    if not root or "Dataset" not in (root.get("@type") if isinstance(root.get("@type"), list) else [root.get("@type")]):
        rep.add("error", "CRATE_NO_ROOT", where, "root data entity './' (Dataset) missing")
        return
    descr = ents.get(CRATE_FILE)
    if not descr or (descr.get("about") or {}).get("@id") != "./":
        rep.add("error", "CRATE_NO_DESCRIPTOR", where, "metadata descriptor missing or not about './'")
    run_dir = repo.root / run_rel
    for part in root.get("hasPart", []):
        pid = part.get("@id") if isinstance(part, dict) else None
        ent = ents.get(pid)
        if ent is None:
            rep.add("error", "CRATE_DANGLING", where, f"hasPart {pid!r} has no entity")
            continue
        fp = run_dir / str(pid)
        if not fp.is_file():
            rep.add("error", "CRATE_FILE_MISSING", f"{run_rel}/{pid}", "crate lists a file that is not in the run")
        elif ent.get("sha256") and sha256_file(fp) != ent["sha256"]:
            rep.add("error", "CRATE_HASH_MISMATCH", f"{run_rel}/{pid}", "crate sha256 differs from the file")
        elif pid in man.files and man.files[pid].get("sha256") != ent.get("sha256"):
            rep.add("error", "CRATE_MANIFEST_DISAGREE", f"{run_rel}/{pid}", "crate and MANIFEST.json hash differ")
        else:
            rep.count("crate_files_verified")
    for e in ents.values():
        for key in ("object", "result", "instrument"):
            v = e.get(key)
            for ref in (v if isinstance(v, list) else [v] if v else []):
                rid = ref.get("@id") if isinstance(ref, dict) else None
                if rid and rid not in ents and not rid.startswith("http"):
                    rep.add("error", "CRATE_DANGLING", where, f"{e.get('@id')}.{key} -> {rid!r} has no entity")


def check_paper(repo: Repo, prog: str, slug: str, linked: Dict[str, List[Tuple[str, str]]], schema: Dict[str, Any],
                rep: Report) -> None:
    d = repo.root / prog / slug
    pj = d / "provenance.json"
    where = f"{prog}/{slug}"
    rep.count("papers")
    if not pj.is_file():
        rep.add("warn", "NO_PAPER_PROVENANCE", where, "no provenance.json; run `provenance.py backfill`")
        return
    obj, err = read_json(pj)
    if err:
        rep.add("error", "PAPER_PROVENANCE_UNREADABLE", where, err)
        return
    for e in validate(obj, schema):
        rep.add("error", "PAPER_SCHEMA", where, e)
    if not isinstance(obj, dict):
        return
    if obj.get("slug") != slug:
        rep.add("error", "PAPER_SLUG", where, f"record says {obj.get('slug')!r}")
    paper_rel = (obj.get("paper") or {}).get("path")
    if paper_rel != f"{prog}/{slug}/paper.md":
        rep.add("error", "PAPER_PATH", where, f"record points at {paper_rel!r}")
    snaps = obj.get("snapshots") or []
    have = sha256_file(d / "paper.md")
    if have not in {s.get("sha256") for s in snaps if isinstance(s, dict)}:
        rep.add("warn", "PAPER_REVISED_UNRECORDED", where, "paper.md hash is not among the recorded snapshots")
    recorded = {r.get("path") for r in obj.get("runs", []) if isinstance(r, dict)}
    for r in obj.get("runs", []):
        if isinstance(r, dict):
            rp = r.get("path", "")
            if not (repo.root / rp).is_dir():
                rep.add("error", "PAPER_RUN_MISSING", where, f"run {rp!r} not in the repository")
            elif slug_of_run(rp) != slug and r.get("match") == "slug-exact":
                rep.add("error", "PAPER_RUN_SLUG", where, f"run {rp!r} is for a different slug")
    for rp, _ in linked.get(slug, []):
        if rp not in recorded:
            rep.add("warn", "RUN_NOT_LINKED", where, f"run {rp} for this slug is not in provenance.json")


def check_blobs(repo: Repo, rep: Report) -> None:
    """No tracked file near the mirror's blob limit; every pointer file names its content-addressed object."""
    for top in ("runs", "provenance") + PROGRAM_DIRS:
        base = repo.root / top
        if not base.is_dir():
            continue
        for dirpath, _, names in os.walk(base):
            for n in names:
                fp = Path(dirpath) / n
                rel = repo.rel(fp)
                if fp.stat().st_size > MAX_BLOB_BYTES:
                    rep.add("error", "LARGE_BLOB", rel, f"{fp.stat().st_size} bytes exceeds {MAX_BLOB_BYTES}; store it in R2 and commit a {POINTER_SUFFIX}")
                if n.endswith(POINTER_SUFFIX):
                    obj, err = read_json(fp)
                    ok = isinstance(obj, dict) and isinstance(obj.get("sha256"), str) and SHA_RE.match(obj["sha256"]) \
                        and isinstance(obj.get("bytes"), int) and obj.get("store") == "r2" and isinstance(obj.get("key"), str)
                    if err or not ok:
                        rep.add("error", "BAD_POINTER", rel, err or "needs sha256, bytes, store='r2' and key")
                    else:
                        rep.count("pointers")


def verify(repo: Repo) -> Report:
    rep = Report()
    schema_dir = repo.root / "schemas"
    paper_schema, _ = read_json(schema_dir / "paper-provenance.schema.json")
    gaps_schema, _ = read_json(schema_dir / "known-gaps.schema.json")
    gaps_obj = load_gaps(repo)
    if gaps_schema and (repo.root / "provenance" / "known-gaps.json").is_file():
        for e in validate(gaps_obj, gaps_schema):
            rep.add("error", "GAPS_SCHEMA", "provenance/known-gaps.json", e)
    gaps = gap_index(gaps_obj)
    runs = repo.discover_runs()
    for run_rel in runs:
        check_run(repo, run_rel, gaps, rep)
    papers = repo.discover_papers()
    linked, unlinked = link_runs((s for _, s in papers), runs)
    for prog, slug in papers:
        if paper_schema:
            check_paper(repo, prog, slug, linked, paper_schema, rep)
    for slug, rl in sorted(unlinked.items()):
        if ("paper-text-not-in-repo", f"papers/{slug}") in gaps:
            rep.count("known_gap_paper_text_missing")
        else:
            rep.add("error", "PAPER_TEXT_NOT_IN_REPO", slug, f"{len(rl)} run(s) but no deposited paper.md and no gap entry")
    for (kind, path), g in sorted(gaps.items()):
        if kind in ("manifest-file-missing", "run-without-manifest") and not (repo.root / path).is_dir():
            rep.add("error", "GAP_STALE", path, f"{kind} gap for a directory that no longer exists")
    rep.count("gaps_recorded", len(gaps))
    check_blobs(repo, rep)
    return rep


# ------------------------------------------------------------------------------------------ reproduce

def _limits() -> None:  # POSIX only
    import resource
    resource.setrlimit(resource.RLIMIT_AS, (2 << 30, 2 << 30))
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    os.setsid()


def reexecute(code: str, seed: int = 0, timeout: int = 45) -> Dict[str, Any]:
    """Run a verification script the way the pipeline did: as a string (`python -c`, so `__file__` is undefined and
    tracebacks read File "<string>"), isolated (-I), in an empty directory, hash seed pinned, no network needed."""
    env = {"PYTHONHASHSEED": str(seed)}
    if os.name == "nt":
        env["SYSTEMROOT"] = os.environ.get("SYSTEMROOT", "")
    else:
        env["PATH"] = "/usr/bin:/bin"
    kw: Dict[str, Any] = {"preexec_fn": _limits} if os.name == "posix" else {}
    t0 = time.time()
    with tempfile.TemporaryDirectory() as td:
        try:
            p = subprocess.run([sys.executable, "-I", "-c", code], cwd=td, env=env, capture_output=True,
                               timeout=timeout, **kw)
        except subprocess.TimeoutExpired:
            return {"timeout": True, "python": platform.python_version(), "seed": seed}
    return {"exit": p.returncode, "stdout": p.stdout.decode("utf-8", "replace"),
            "stderr": p.stderr.decode("utf-8", "replace"), "python": platform.python_version(), "seed": seed,
            "seconds": round(time.time() - t0, 2)}


def recorded_output(md: str) -> Optional[str]:
    m = re.search(r"## Execution output\n```\n(.*?)\n```", md, re.S)
    return m.group(1) if m else None


def split_record(body: str) -> Tuple[str, str, Optional[int]]:
    ex = re.search(r"\n*\[exit (-?\d+)\]\s*$", body)
    code = int(ex.group(1)) if ex else None
    b = body[:ex.start()] if ex else body
    m = re.search(r"\n*\[stderr\]\n", b)
    out, err = (b[:m.start()], b[m.end():]) if m else (b, "")
    return out.rstrip("\n"), err.rstrip("\n"), code


def _exc_type(stderr: str) -> str:
    last = (stderr.strip().splitlines() or [""])[-1].strip()
    return last.split(":", 1)[0]


def compare_record(recorded: Optional[str], res: Dict[str, Any]) -> str:
    """reproduced-exact | reproduced-equivalent | not-reproduced | no-recorded-output | timeout.
    Equivalent: identical stdout and exit code, same exception type; only the interpreter-version-dependent
    traceback layout or error suggestion differs."""
    if res.get("timeout"):
        return "timeout"
    if recorded is None:
        return "no-recorded-output"
    r_out, r_err, r_code = split_record(recorded)
    g_out, g_err = res["stdout"].rstrip("\n"), res["stderr"].rstrip("\n")
    if g_out == r_out and res["exit"] == r_code:
        if g_err == r_err:
            return "reproduced-exact"
        if _exc_type(g_err) == _exc_type(r_err):
            return "reproduced-equivalent"
    return "not-reproduced"


def reproduce_run(repo: Repo, run_rel: str, seeds: Iterable[int] = (0,)) -> Dict[str, Any]:
    """Re-execute a run's verification.py and compare it with the recorded output. With more than one seed the script
    is also run under each other seed and once more under the first: any difference in stdout or exit code marks it
    nondeterministic, and a nondeterministic script is never reported as reproduced."""
    run = repo.root / run_rel
    py, md = run / "verification.py", run / "verification.md"
    seeds = list(seeds) or [0]
    out: Dict[str, Any] = {"run": run_rel}
    if not py.is_file():
        out["verdict"] = "no-script"
        return out
    code = py.read_text(encoding="utf-8")
    rec = recorded_output(md.read_text(encoding="utf-8")) if md.is_file() else None
    res = reexecute(code, seeds[0])
    verdict = compare_record(rec, res)
    nondet = False
    if len(seeds) > 1 and not res.get("timeout"):
        sig = (res["stdout"], res["exit"])
        for s in seeds[1:] + [seeds[0]]:
            other = reexecute(code, s)
            if (other.get("stdout"), other.get("exit")) != sig:
                nondet = True
                break
    out.update(verdict="not-reproduced" if nondet else verdict, python=res.get("python"), exit=res.get("exit"),
               nondeterministic=nondet,
               stdout_sha256=None if nondet or res.get("timeout") else sha256_bytes(res["stdout"].encode("utf-8")),
               recorded_exit=split_record(rec)[2] if rec is not None else None)
    return out


# ---------------------------------------------------------------------------------- crate generation

ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})|arXiv:\s*(\d{4}\.\d{4,5})", re.I)
DOI_RE = re.compile(r"(?:doi\.org/|doi:\s*)(10\.\d{4,9}/[^\s)\]>\"'`,;]+)", re.I)


def sources_of(grounding: str) -> List[Dict[str, str]]:
    seen: Dict[str, Dict[str, str]] = {}
    for m in ARXIV_RE.finditer(grounding):
        aid = m.group(1) or m.group(2)
        seen.setdefault(f"https://arxiv.org/abs/{aid}", {"@id": f"https://arxiv.org/abs/{aid}", "@type": "ScholarlyArticle",
                                                       "identifier": f"arXiv:{aid}"})
    for m in DOI_RE.finditer(grounding):
        doi = m.group(1).rstrip(".")
        seen.setdefault(f"https://doi.org/{doi}", {"@id": f"https://doi.org/{doi}", "@type": "ScholarlyArticle",
                                                  "identifier": f"doi:{doi}"})
    return [seen[k] for k in sorted(seen)][:200]


def license_entity(repo: Repo) -> Dict[str, Any]:
    lic = repo.root / "LICENSE"
    name, spdx = "QNFO license", None
    if lic.is_file():
        head = lic.read_text(encoding="utf-8", errors="replace")[:600]
        name = head.splitlines()[0].strip() or name
        m = re.search(r"SPDX:\s*(\S+)", head)
        spdx = m.group(1) if m else None
    ent: Dict[str, Any] = {"@id": "https://qnfo.org/legal/license", "@type": "CreativeWork", "name": name}
    if spdx:
        ent["identifier"] = spdx
    return ent


def build_crate(repo: Repo, run_rel: str, man: Optional[Manifest], deposit: Optional[Tuple[Optional[str], str]],
                repro: Optional[Dict[str, Any]], observed_at: str, title: Optional[str],
                paper_slug: Optional[str] = None, preserve: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """`preserve` is the previous crate: its independent re-execution (action, interpreter, tool) is copied unchanged, so a later
    backfill on another day or another Python does not rewrite an observation whose outcome has not changed."""
    run = repo.root / run_rel
    slug, cycle = slug_of_run(run_rel), cycle_of_run(run_rel)
    present = sorted(p.relative_to(run).as_posix() for p in run.rglob("*")
                     if p.is_file() and p.name not in (CRATE_FILE, ".gitkeep"))
    listed = man.files if man else {}
    lic = license_entity(repo)
    paper_url = f"https://papers.qnfo.org/papers/{paper_slug or slug}" if slug else None
    graph: List[Dict[str, Any]] = [
        {"@id": CRATE_FILE, "@type": "CreativeWork", "about": {"@id": "./"}, "conformsTo": {"@id": CRATE_SPEC}},
    ]
    root: Dict[str, Any] = {
        "@id": "./", "@type": "Dataset",
        "name": f"QNFO research run {cycle}" + (f": {title or slug}" if slug else " (pilot)"),
        "description": ("Interim and final artifacts of one run of the QNFO automated research pipeline, kept as deposited. "
                        "MANIFEST.json is the pipeline's own record and is never rewritten; this crate adds the standard "
                        "packaging, per-file fixity and the stage structure of the run."),
        "author": {"@id": ORCID}, "license": {"@id": lic["@id"]},
        "conformsTo": [{"@id": PROCESS_RUN_PROFILE}],
        "qnfo:cycle": cycle, "qnfo:runPath": run_rel,
    }
    if slug:
        root["qnfo:slug"] = slug
    if man and man.pipeline:
        root["qnfo:pipelineVersion"] = man.pipeline
    if deposit:
        root["datePublished"] = deposit[1]
        if deposit[0]:
            root["qnfo:depositCommit"] = deposit[0]
    if paper_url:
        root["about"] = {"@id": paper_url}
    parts: List[Dict[str, str]] = []
    file_ents: List[Dict[str, Any]] = []
    roles: Dict[str, List[str]] = {}
    for rel in present:
        fp = run / rel
        sha = sha256_file(fp)
        role = role_of(rel)
        ent: Dict[str, Any] = {"@id": rel, "@type": "File", "name": rel, "encodingFormat": mime_of(rel),
                               "contentSize": str(fp.stat().st_size), "sha256": sha, "qnfo:role": role,
                               "qnfo:listedInManifest": rel in listed or rel == "MANIFEST.json"}
        file_ents.append(ent)
        parts.append({"@id": rel})
        roles.setdefault(role, []).append(rel)
    missing = sorted(set(listed) - set(present))
    missing_ents = [{"@id": f"#missing/{fn}", "@type": "CreativeWork", "name": fn,
                     "sha256": listed[fn].get("sha256"), "qnfo:status": "listed-in-manifest-absent-from-repository"}
                    for fn in missing]
    if missing_ents:
        root["qnfo:missingParts"] = [{"@id": m["@id"]} for m in missing_ents]
    root["hasPart"] = parts
    cp = {"@id": "#cpython", "@type": "SoftwareApplication", "name": "CPython",
          "description": "Interpreter that ran verification.py in the pipeline; its version was not recorded."}
    pipeline_app = {"@id": "#pipeline", "@type": "SoftwareApplication", "name": "qnfo-research-exec",
                    "url": "https://github.com/QNFO/qnfo-workers/tree/main/qnfo-research-exec"}
    if man and man.pipeline:
        pipeline_app["version"] = man.pipeline
    actions: List[Dict[str, Any]] = []

    def ref(rels: Iterable[str]) -> List[Dict[str, str]]:
        return [{"@id": r} for r in rels]

    prev: List[str] = []
    stage_defs = [("#grounding", "Literature grounding", ["prompt", "grounding"]),
                  ("#drafting", "Independent drafting", ["draft", "draft-support"]),
                  ("#reconciliation", "Reconciliation and citation audit", ["reconciliation"]),
                  ("#review", "Adversarial review", ["review"])]
    for aid, name, rls in stage_defs:
        out = [r for role in rls for r in roles.get(role, [])]
        if not out:
            continue
        act: Dict[str, Any] = {"@id": aid, "@type": "CreateAction", "name": name, "instrument": {"@id": "#pipeline"},
                               "result": ref(out), "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"},
                               "qnfo:basis": "inferred-from-procedure"}
        if prev:
            act["object"] = ref(prev)
        actions.append(act)
        prev = out
    graph_src: List[Dict[str, Any]] = []
    if "grounding" in roles:
        g = (run / roles["grounding"][0]).read_text(encoding="utf-8", errors="replace")
        srcs = sources_of(g)
        if srcs:
            for a in actions:
                if a["@id"] == "#grounding":
                    a["object"] = [{"@id": s["@id"]} for s in srcs]
                    a["qnfo:sourcesBasis"] = "extracted-by-regex-from-grounding.md"
            graph_src = srcs
    vscript, vreport = roles.get("verification-script", []), roles.get("verification-report", [])
    if vscript:
        rec = recorded_output((run / vreport[0]).read_text(encoding="utf-8", errors="replace")) if vreport else None
        r_code = split_record(rec)[2] if rec is not None else None
        orig: Dict[str, Any] = {"@id": "#verification-original", "@type": "CreateAction",
                                "name": "verification.py as run by the pipeline", "instrument": {"@id": "#cpython"},
                                "object": ref(vscript), "result": ref(vreport) or ref(vscript),
                                "actionStatus": {"@id": "http://schema.org/FailedActionStatus" if r_code else
                                                 "http://schema.org/CompletedActionStatus"},
                                "qnfo:basis": "recorded-in-verification.md"}
        if r_code is not None:
            orig["qnfo:exitCode"] = r_code
        if deposit:
            orig["endTime"] = deposit[1]
            orig["description"] = "endTime is the deposit time; the execution time itself was not recorded."
        actions.append(orig)
        prior_graph = (preserve or {}).get("@graph") or []
        kept = next((e for e in prior_graph if e.get("@id") == "#verification-reexecution"), None) if not repro else None
        if kept:
            for ref_id in ((kept.get("instrument") or {}).get("@id"), (kept.get("agent") or {}).get("@id")):
                ent = next((e for e in prior_graph if e.get("@id") == ref_id), None)
                if ent:
                    graph.append(ent)
            actions.append(kept)
        if repro and repro.get("verdict"):
            cpv = {"@id": f"#cpython-{repro['python']}", "@type": "SoftwareApplication", "name": "CPython",
                   "version": repro["python"]}
            graph.append(cpv)
            re_act: Dict[str, Any] = {"@id": "#verification-reexecution", "@type": "CreateAction",
                                      "name": "Independent re-execution of verification.py",
                                      "instrument": {"@id": cpv["@id"]}, "object": ref(vscript),
                                      "endTime": observed_at, "agent": {"@id": "#provenance-tool"},
                                      "actionStatus": {"@id": "http://schema.org/CompletedActionStatus"},
                                      "qnfo:comparison": repro["verdict"],
                                      "qnfo:method": "python -I -c <script>, empty cwd, PYTHONHASHSEED=0",
                                      "qnfo:exitCode": repro.get("exit")}
            if repro.get("stdout_sha256"):
                re_act["qnfo:stdoutSha256"] = repro["stdout_sha256"]
            if repro.get("nondeterministic"):
                re_act["qnfo:nondeterministic"] = True
            actions.append(re_act)
            graph.append({"@id": "#provenance-tool", "@type": "SoftwareApplication", "name": "tools/provenance.py",
                          "version": TOOL_VERSION})
    root["mentions"] = [{"@id": a["@id"]} for a in actions]
    graph.append(root)
    graph += [lic, {"@id": PROCESS_RUN_PROFILE, "@type": "CreativeWork", "name": "Process Run Crate", "version": "0.4"},
              {"@id": ORCID, "@type": "Person", "name": AUTHOR_NAME}, cp, pipeline_app]
    if paper_url:
        graph.append({"@id": paper_url, "@type": ["CreativeWork", "ScholarlyArticle"], "name": title or slug,
                      "url": paper_url})
    graph += graph_src + file_ents + missing_ents + actions
    return {"@context": [CRATE_CONTEXT, {"qnfo": QNFO_NS}], "@graph": graph}


# ------------------------------------------------------------------------------------ paper records

def _first(rx: str, text: str, flags: int = 0) -> Optional[str]:
    m = re.search(rx, text, flags)
    return m.group(1).strip() if m else None


def declared_of(d: Path) -> Dict[str, Any]:
    readme = (d / "README.md").read_text(encoding="utf-8", errors="replace") if (d / "README.md").is_file() else ""
    head = (d / "paper.md").read_text(encoding="utf-8", errors="replace")[:6000]
    dois: List[Dict[str, str]] = []
    seen = set()
    for src, text in (("README.md", readme), ("paper.md", head)):
        for m in re.finditer(r"(?:DOI:?\**\s*|doi\.org/)(10\.\d{4,9}/[^\s)\]>\"'*]+)", text, re.I):
            doi = m.group(1).rstrip(".,;")
            if (doi, src) not in seen:
                seen.add((doi, src))
                dois.append({"doi": doi, "source": src})
    lic = _first(r"^License:\s*(.+)$", readme, re.M)
    ver = _first(r"\*\*Version:\*\*\s*([0-9][^\s*]*)", head)
    return {"version": ver, "license": lic, "dois": dois}


def title_of(d: Path) -> Optional[str]:
    for line in (d / "paper.md").read_text(encoding="utf-8", errors="replace").splitlines()[:40]:
        if line.startswith("# "):
            return line[2:].strip()
    return None


def build_paper_record(repo: Repo, prog: str, slug: str, runs: List[Tuple[str, str]], observed_at: str,
                       prior: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    d = repo.root / prog / slug
    paper = d / "paper.md"
    sha, size = sha256_file(paper), paper.stat().st_size
    commit = (repo.git("log", "-1", "--format=%H", "--", f"{prog}/{slug}/paper.md") or "").strip() or None
    snaps = list((prior or {}).get("snapshots", []))
    if sha not in {s.get("sha256") for s in snaps}:
        snaps.append({"sha256": sha, "bytes": size, "recorded_at": observed_at, "basis": "backfill",
                      "version": declared_of(d)["version"], "git_commit": commit})
    run_recs = []
    for rp, match in runs:
        mp = repo.root / rp / "MANIFEST.json"
        run_recs.append({"path": rp, "relation": "produced-by", "match": match,
                         "manifest_sha256": sha256_file(mp) if mp.is_file() else None})
    rec: Dict[str, Any] = {
        "schema": PAPER_SCHEMA, "slug": slug,
        "paper": {"path": f"{prog}/{slug}/paper.md", "title": title_of(d), "url": f"https://papers.qnfo.org/papers/{slug}"},
        "declared": declared_of(d), "runs": run_recs,
        "identifiers": (prior or {}).get("identifiers", {"research_queue_ids": [], "living_paper_slug": slug}),
        "snapshots": snaps, "events": (prior or {}).get("events", []),
    }
    return rec


# --------------------------------------------------------------------------------------------- backfill

def unchanged_observation(prior_crate: Any, repro: Dict[str, Any]) -> bool:
    """True when the crate already holds a re-execution with the same verdict, exit code and determinism as `repro`."""
    if not isinstance(prior_crate, dict):
        return False
    act = next((e for e in prior_crate.get("@graph", []) if e.get("@id") == "#verification-reexecution"), None)
    return bool(act and act.get("qnfo:comparison") == repro.get("verdict") and act.get("qnfo:exitCode") == repro.get("exit")
                and bool(act.get("qnfo:nondeterministic")) == bool(repro.get("nondeterministic")))


def backfill(repo: Repo, observed_at: str, reproduce_runs: bool = True) -> Dict[str, int]:
    changed = {"crates": 0, "papers": 0, "gaps": 0}
    adds = repo.legacy_adds()
    runs = repo.discover_runs()
    papers = repo.discover_papers()
    linked, unlinked = link_runs((s for _, s in papers), runs)
    run_paper = {rp: ps for ps, rl in linked.items() for rp, _ in rl}
    titles = {s: title_of(repo.root / p / s) for p, s in papers}
    gaps: List[Dict[str, Any]] = []
    prior_rows = {(g.get("kind"), g.get("path")): g for g in load_gaps(repo).get("gaps", [])}
    for rp in runs:
        run = repo.root / rp
        mp = run / "MANIFEST.json"
        man = None
        if mp.is_file():
            obj, _ = read_json(mp)
            man = normalize_manifest(obj)
        legacy_prefix = rp[len("runs/"):]
        prior_crate, _ = read_json(run / CRATE_FILE) if (run / CRATE_FILE).is_file() else (None, None)
        dep = None
        for cand in ("MANIFEST.json", "verification.md", "grounding.md"):
            if f"{legacy_prefix}/{cand}" in adds:
                dep = adds[f"{legacy_prefix}/{cand}"]
                break
        if dep is None and adds:
            ds = [adds[k] for k in adds if k.startswith(legacy_prefix + "/")]
            dep = max(ds, key=lambda x: x[1]) if ds else None
        if dep is None and isinstance(prior_crate, dict):
            # the legacy history is not an ancestor yet (the import was squash-merged and not yet linked): keep what the crate recorded
            old_root = next((e for e in prior_crate.get("@graph", []) if e.get("@id") == "./"), None)
            if old_root and old_root.get("datePublished"):
                dep = (old_root.get("qnfo:depositCommit"), old_root["datePublished"])
        repro = reproduce_run(repo, rp, (0, 1, 2)) if reproduce_runs and (run / "verification.py").is_file() else None
        if repro and unchanged_observation(prior_crate, repro):
            repro = None   # same outcome as the recorded re-execution: keep that record (date, interpreter) as it is
        crate = build_crate(repo, rp, man, dep, repro, observed_at, titles.get(run_paper.get(rp) or slug_of_run(rp) or ""),
                            run_paper.get(rp), preserve=prior_crate if isinstance(prior_crate, dict) else None)
        if write_if_changed(run / CRATE_FILE, dump_json(crate)):
            changed["crates"] += 1
        present = {p.relative_to(run).as_posix() for p in run.rglob("*") if p.is_file()}
        if man is None:
            gaps.append({"id": gap_id("NOMAN", rp), "kind": "run-without-manifest",
                         "path": rp, "files": sorted(present - SIDECARS),
                         "cause": "the manifest was never written: the deposit stopped before MANIFEST.json (per-file PUT, HTTP 409 on a concurrent push; failure was logged as ok)",
                         "recovery": "none-recorded-only", "status": "unrecoverable"})
        else:
            miss = sorted(set(man.files) - present)
            if miss:
                row = {"id": gap_id("MISS", rp), "kind": "manifest-file-missing",
                       "path": rp, "files": miss,
                       "expected_sha256": {f: man.files[f]["sha256"] for f in miss if man.files[f].get("sha256")},
                       "cause": "partial deposit: the per-file contents PUT returned HTTP 409 for these files and the push was still logged as ok",
                       "recovery": "restore-from-r2-by-hash", "status": "open"}
                unrec = {f: why for f, why in ((prior_rows.get(("manifest-file-missing", rp)) or {}).get("unrecoverable") or {}).items() if f in miss}
                if unrec:
                    row["unrecoverable"] = unrec
                    if all(f in unrec for f in miss):
                        row["status"] = "unrecoverable"
                gaps.append(row)
        if repro:
            if repro.get("nondeterministic"):
                gaps.append({"id": gap_id("NONDET", rp), "kind": "nondeterministic-verification", "path": rp,
                             "cause": "verification.py prints different output on repeated runs, even under one fixed PYTHONHASHSEED (it orders objects by identity); the record cannot be reproduced bit-for-bit",
                             "recovery": "regenerate", "status": "open"})
            elif repro["verdict"] == "not-reproduced":
                gaps.append({"id": gap_id("REC", rp), "kind": "recorded-output-corrupt", "path": rp,
                             "cause": "the recorded Execution output in verification.md does not match what the deposited script prints (the record is truncated or carries a transport error)",
                             "recovery": "regenerate", "status": "open"})
    for slug, rl in sorted(unlinked.items()):
        gaps.append({"id": gap_id("PAPER", f"papers/{slug}"), "kind": "paper-text-not-in-repo", "path": f"papers/{slug}",
                     "files": [f"papers/{slug}/paper.md"], "runs": sorted(rl),
                     "cause": "the pipeline published this paper to papers.qnfo.org and deposited its run, but only the legacy publish path (publishV2) wrote papers/<slug>/paper.md",
                     "recovery": "restore-from-living-paper", "status": "open"})
    prior_gaps = load_gaps(repo)
    new_gaps = {"schema": GAPS_SCHEMA, "as_of": prior_gaps.get("as_of") or observed_at, "gaps": sorted(gaps, key=lambda g: g["id"])}
    if [g for g in prior_gaps.get("gaps", [])] != new_gaps["gaps"]:
        new_gaps["as_of"] = observed_at
    if write_if_changed(repo.root / "provenance" / "known-gaps.json", dump_json(new_gaps)):
        changed["gaps"] += 1
    for prog, slug in papers:
        pj = repo.root / prog / slug / "provenance.json"
        prior, _ = read_json(pj) if pj.is_file() else (None, None)
        rec = build_paper_record(repo, prog, slug, sorted(linked.get(slug, [])), observed_at,
                                 prior if isinstance(prior, dict) else None)
        if write_if_changed(pj, dump_json(rec)):
            changed["papers"] += 1
    return changed


GOOD = ("reproduced-exact", "reproduced-equivalent")


def reproduce_all(repo: Repo, seeds: List[int]) -> int:
    """Re-run every verification script. A run whose committed crate says it reproduced must still reproduce; a run
    already recorded as not reproducible is reported, not failed (it is in the gap ledger)."""
    tally: Dict[str, int] = {}
    regressions = 0
    for rp in repo.discover_runs():
        if not (repo.root / rp / "verification.py").is_file():
            continue
        res = reproduce_run(repo, rp, seeds)
        tally[res["verdict"]] = tally.get(res["verdict"], 0) + 1
        crate, _ = read_json(repo.root / rp / CRATE_FILE)
        before = None
        for e in (crate or {}).get("@graph", []):
            if e.get("@id") == "#verification-reexecution":
                before = e.get("qnfo:comparison")
        if before in GOOD and res["verdict"] not in GOOD:
            regressions += 1
            print(f"REGRESSION {rp}: was {before}, now {res['verdict']}")
    print(json.dumps(tally, sort_keys=True))
    print(f"regressions={regressions}")
    return 1 if regressions else 0


def index(repo: Repo) -> Iterable[Dict[str, Any]]:
    gaps = gap_index(load_gaps(repo))
    papers = repo.discover_papers()
    linked, unlinked = link_runs((s for _, s in papers), repo.discover_runs())
    for prog, slug in papers:
        rl = linked.get(slug, [])
        yield {"slug": slug, "paper": f"{prog}/{slug}/paper.md", "runs": [r for r, _ in rl],
               "kind": "pipeline" if rl else "legacy"}
    for slug, rl in sorted(unlinked.items()):
        yield {"slug": slug, "paper": None, "runs": rl, "kind": "pipeline",
               "gap": ("paper-text-not-in-repo", f"papers/{slug}") in gaps}


# ------------------------------------------------------------------------------------------------ CLI

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="provenance.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", default=".", help="repository root (default: current directory)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("verify", help="check integrity, completeness and linkage")
    v.add_argument("--strict", action="store_true", help="warnings fail too")
    v.add_argument("--json", metavar="FILE", help="also write the findings as JSON")
    b = sub.add_parser("backfill", help="write provenance records for everything in the repository")
    b.add_argument("--observed-at", default=time.strftime("%Y-%m-%d", time.gmtime()))
    b.add_argument("--no-reproduce", action="store_true", help="skip re-executing verification scripts")
    r = sub.add_parser("reproduce", help="re-execute a run's verification.py and compare with the record")
    r.add_argument("run", nargs="?", help="run directory, e.g. runs/cycle-396/<slug>")
    r.add_argument("--all", action="store_true", help="every run; fails on a verdict worse than the one in its crate")
    r.add_argument("--seeds", default="0,1,2", help="hash seeds to try (the first is the reference)")
    sub.add_parser("index", help="print the paper <-> run catalog as JSON lines")
    a = ap.parse_args(argv)
    repo = Repo(Path(a.root))
    if a.cmd == "verify":
        rep = verify(repo)
        for f in rep.findings:
            if f.level != "info":
                print(f.line())
        print("\n".join(f"{k}: {v}" for k, v in sorted(rep.stats.items())))
        print(f"errors={len(rep.errors())} warnings={len(rep.warnings())}")
        if a.json:
            Path(a.json).write_text(dump_json({"stats": rep.stats, "findings": [f.__dict__ for f in rep.findings]}), encoding="utf-8")
        return 1 if rep.errors() or (a.strict and rep.warnings()) else 0
    if a.cmd == "backfill":
        print(json.dumps(backfill(repo, a.observed_at, not a.no_reproduce)))
        return 0
    if a.cmd == "reproduce" and a.all:
        return reproduce_all(repo, [int(x) for x in a.seeds.split(",") if x != ""])
    if a.cmd == "reproduce":
        if not a.run:
            ap.error("a run directory or --all is required")
        res = reproduce_run(repo, a.run.rstrip("/"), [int(x) for x in a.seeds.split(",") if x != ""])
        print(json.dumps(res, indent=2))
        return 0 if res["verdict"] in ("reproduced-exact", "reproduced-equivalent") else 1
    if a.cmd == "index":
        for row in index(repo):
            print(json.dumps(row, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
