"""Recreate the starting state of case 002, identically on Windows, macOS and Linux.

Usage:
    python make_start_state.py [target_folder]      (default: ./case-002-workspace)

It copies a small Django REST framework order API into the target folder, commits it,
then installs dependencies with uv, creates the SQLite database and loads demo data
(50 customers, 30 products, 200 orders, 600 items). Requires git and uv.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent / "template"


def run(target: Path, *args: str) -> None:
    subprocess.run(list(args), cwd=target, check=True, stdout=subprocess.DEVNULL)


def main() -> None:
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "case-002-workspace").resolve()
    if target.exists() and any(target.iterdir()):
        sys.exit(f"{target} already exists and is not empty: choose another folder.")
    shutil.copytree(TEMPLATE, target, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", ".venv", "db.sqlite3"))

    run(target, "git", "init", "-q")
    run(target, "git", "config", "user.name", "Casebook Setup")
    run(target, "git", "config", "user.email", "casebook@example.invalid")
    run(target, "git", "add", "-A")
    run(target, "git", "commit", "-q", "-m", "Initial shop API")

    print("Installing dependencies with uv (first time: about a minute)...")
    run(target, "uv", "sync", "-q")
    run(target, "uv", "run", "python", "manage.py", "migrate", "-v", "0")
    run(target, "uv", "run", "python", "manage.py", "seed_demo")
    print(f"Ready: {target}")
    print("Open http://127.0.0.1:8000/api/orders/ after `uv run python manage.py runserver`.")


if __name__ == "__main__":
    main()
