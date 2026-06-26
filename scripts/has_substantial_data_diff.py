#!/usr/bin/env python3
"""Detect whether synced OpenCC data changed in a publish-worthy way.

OpenCC's resource zip manifest records a sha256 for each resource before local
headers are added. Prefer those hashes for data/config files and fall back to a
direct HEAD comparison for files outside the upstream resource zip.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys


DEFAULT_MANIFEST = ".opencc-resource-manifest.json"
DEFAULT_FALLBACK_ROOTS = ("test-data",)


def git_tracked_files(root: str) -> set[pathlib.Path]:
    output = subprocess.check_output(["git", "ls-files", root], text=True)
    return {pathlib.Path(line) for line in output.splitlines() if line}


def git_head_bytes(path: pathlib.Path) -> bytes | None:
    result = subprocess.run(
        ["git", "show", f"HEAD:{path.as_posix()}"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def working_files(root: str) -> set[pathlib.Path]:
    root_path = pathlib.Path(root)
    if not root_path.exists():
        return set()
    return {p for p in root_path.rglob("*") if p.is_file()}


def manifest_entry_hashes(content: bytes | None) -> dict[str, str] | None:
    if content is None:
        return None
    manifest = json.loads(content.decode("utf-8"))
    entries = manifest.get("entries", {})
    return {
        name: entry.get("sha256", "")
        for name, entry in entries.items()
        if isinstance(entry, dict)
    }


def manifest_changes(manifest_path: pathlib.Path) -> list[str]:
    old = manifest_entry_hashes(git_head_bytes(manifest_path))
    new = manifest_entry_hashes(manifest_path.read_bytes() if manifest_path.exists() else None)

    if old is None and new is None:
        return []
    if old is None:
        return [f"{manifest_path.as_posix()} (new manifest baseline)"]
    if new is None:
        return [f"{manifest_path.as_posix()} (manifest removed)"]

    changed = []
    for name in sorted(set(old) | set(new)):
        if old.get(name) != new.get(name):
            changed.append(name)
    return changed


def fallback_changes(roots: list[str]) -> list[str]:
    changed = []
    paths = set()
    for root in roots:
        paths |= git_tracked_files(root)
        paths |= working_files(root)

    for path in sorted(paths):
        old = git_head_bytes(path)
        new = path.read_bytes() if path.exists() else None
        if old != new:
            changed.append(path.as_posix())
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    parser.add_argument("fallback_roots", nargs="*", default=list(DEFAULT_FALLBACK_ROOTS))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    changed = manifest_changes(pathlib.Path(args.manifest))
    changed += fallback_changes(args.fallback_roots)

    if changed:
        print("\n".join(changed))
        return 0

    print("No substantial data diff.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
