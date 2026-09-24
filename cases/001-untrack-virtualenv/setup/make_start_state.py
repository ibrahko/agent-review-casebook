"""Recreate the starting state of case 001, identically on Windows, macOS and Linux.

Usage:
    python make_start_state.py [target_folder]      (default: ./case-001-workspace)

It creates a tiny Python web project whose virtual environment (venv/) was committed
to git by mistake, then a second ordinary commit on top. Nothing is downloaded.
"""

from __future__ import annotations

import subprocess
import sys
import venv
from pathlib import Path

FILES = {
    "app.py": '''"""Tiny demo app used as the starting point of a Casebook task."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))
''',
    "requirements.txt": "django>=5.0\n",
    "README.md": "# demo-app\n\nA tiny demo project.\n\n```\npython -m venv venv\npip install -r requirements.txt\n```\n",
    ".gitignore": "__pycache__/\n*.pyc\n",  # deliberately does NOT ignore venv/
}


def git(target: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=target, check=True, stdout=subprocess.DEVNULL)


def main() -> None:
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "case-001-workspace").resolve()
    if target.exists() and any(target.iterdir()):
        sys.exit(f"{target} already exists and is not empty: choose another folder.")
    target.mkdir(parents=True, exist_ok=True)

    for name, content in FILES.items():
        (target / name).write_text(content, encoding="utf-8")
    print("Creating venv/ (a few seconds)...")
    venv.create(target / "venv", with_pip=True)

    git(target, "init", "-q")
    git(target, "config", "user.name", "Casebook Setup")
    git(target, "config", "user.email", "casebook@example.invalid")
    git(target, "add", "-A")
    git(target, "commit", "-q", "-m", "Initial project")

    app = target / "app.py"
    app.write_text(app.read_text(encoding="utf-8").replace("Hello", "Hi"), encoding="utf-8")
    git(target, "commit", "-q", "-am", "Friendlier greeting")

    tracked = subprocess.run(
        ["git", "ls-files", "venv"], cwd=target, check=True, capture_output=True, text=True
    ).stdout.splitlines()
    print(f"Ready: {target}")
    print(f"{len(tracked)} files under venv/ are tracked by git, across 2 commits.")


if __name__ == "__main__":
    main()
