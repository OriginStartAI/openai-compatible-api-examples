from __future__ import annotations

import py_compile
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_python() -> int:
    failures = 0
    for path in sorted((ROOT / "examples" / "python").glob("*.py")):
        try:
            py_compile.compile(str(path), doraise=True)
            print(f"python ok: {path.relative_to(ROOT)}")
        except py_compile.PyCompileError as exc:
            failures += 1
            print(f"python failed: {path.relative_to(ROOT)}\n{exc}", file=sys.stderr)
    return failures


def check_node() -> int:
    node = shutil.which("node")
    if not node:
        print("node not found; skipping Node.js syntax checks")
        return 0

    failures = 0
    for path in sorted((ROOT / "examples" / "node").glob("*.mjs")):
        completed = subprocess.run([node, "--check", str(path)], check=False)
        if completed.returncode == 0:
            print(f"node ok: {path.relative_to(ROOT)}")
        else:
            failures += 1
            print(f"node failed: {path.relative_to(ROOT)}", file=sys.stderr)
    return failures


def main() -> None:
    failures = check_python() + check_node()
    if failures:
        raise SystemExit(f"syntax checks failed: {failures}")
    print("syntax checks passed")


if __name__ == "__main__":
    main()
