"""Build orchestrator for the comp.lang.cobol pipeline.

Runs generators in dependency order and skips any whose output is newer
than all its source files.  thread.py runs first (indexes link to its
output); the remaining index generators run in parallel.

Usage:
    python build.py              # rebuild only what's stale
    python build.py --force      # rebuild everything unconditionally
    python build.py --dry-run    # print what would run without running it
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
OUT = PROJECT_DIR / "markdown"

# Changing either of these invalidates every generator's output.
COMMON_DEPS = [PROJECT_DIR / s for s in ("archive.py", "spam.py")]

# thread.py has no single output file, so we track completion via a stamp.
THREAD_STAMP = OUT / "threads" / ".stamp"

# (script, output_sentinel, extra_sources_beyond_common_and_script_itself)
THREAD_SPEC = ("thread.py", THREAD_STAMP, ["topics.py"])

INDEX_SPECS: list[tuple[str, Path, list[str]]] = [
    ("subjects.py", OUT / "subjects.md", []),
    ("topics.py",   OUT / "topics.md",   []),
    ("years.py",    OUT / "years.md",    []),
    ("authors.py",  OUT / "authors.md",  []),
    ("stats.py",    OUT / "stats.md",    []),
    ("links.py",    OUT / "links.md",    []),
    ("search_index.py", OUT / "search-index.json", []),
]


def _sources(script: str, extras: list[str]) -> list[Path]:
    return COMMON_DEPS + [PROJECT_DIR / script] + [PROJECT_DIR / e for e in extras]


def _stale(output: Path, sources: list[Path]) -> bool:
    if not output.exists():
        return True
    t = output.stat().st_mtime
    for s in sources:
        if not s.exists():
            print(f"  [warn] declared source not found: {s}", file=sys.stderr)
            continue
        if s.stat().st_mtime > t:
            return True
    return False


def _run(script: str, dry_run: bool) -> int:
    if dry_run:
        print(f"  [dry-run] python {script}")
        return 0
    return subprocess.run([sys.executable, script], cwd=PROJECT_DIR).returncode


def build(force: bool, dry_run: bool) -> int:
    # --- thread.py first ---
    script, stamp, extras = THREAD_SPEC
    if force or _stale(stamp, _sources(script, extras)):
        print(f"Running {script}...")
        rc = _run(script, dry_run)
        if rc != 0:
            print(f"ERROR: {script} exited {rc}", file=sys.stderr)
            return rc
        if not dry_run:
            stamp.touch()
    else:
        print(f"Up to date: {script}")

    # --- index generators in parallel ---
    to_run = []
    for script, output, extras in INDEX_SPECS:
        if force or _stale(output, _sources(script, extras)):
            to_run.append(script)
        else:
            print(f"Up to date: {script}")

    if not to_run:
        return 0

    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=len(to_run)) as pool:
        futures = {pool.submit(_run, s, dry_run): s for s in to_run}
        for fut in as_completed(futures):
            s = futures[fut]
            rc = fut.result()
            if rc != 0:
                errors.append(f"{s} exited {rc}")
            elif not dry_run:
                print(f"Done: {s}")

    for err in errors:
        print(f"ERROR: {err}", file=sys.stderr)
    return 1 if errors else 0


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Build the comp.lang.cobol markdown archive, skipping up-to-date outputs."
    )
    ap.add_argument("--force", action="store_true",
                    help="Rebuild all outputs even if up to date.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print what would run without running anything.")
    args = ap.parse_args()
    sys.exit(build(args.force, args.dry_run))


if __name__ == "__main__":
    main()
