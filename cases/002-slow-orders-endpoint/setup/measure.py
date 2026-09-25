"""Reviewer's measurement for case 002 — run it BEFORE and AFTER the session.

Usage, from inside the workspace folder:
    uv run python <path-to>/measure.py

It prints the number of SQL queries and the time needed to render /api/orders/,
plus a fingerprint of the JSON response. After a correct fix, the number of
queries drops sharply and the fingerprint is unchanged (same data returned).
This file is not part of the workspace, so the agent never sees it.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

import django  # noqa: E402

django.setup()

from django.db import connection  # noqa: E402
from django.test import Client  # noqa: E402
from django.test.utils import CaptureQueriesContext  # noqa: E402


def main() -> None:
    client = Client()
    with CaptureQueriesContext(connection) as ctx:
        started = time.perf_counter()
        response = client.get("/api/orders/")
        elapsed_ms = (time.perf_counter() - started) * 1000
    if response.status_code != 200:
        sys.exit(f"HTTP {response.status_code}: {response.content[:300]!r}")
    data = response.json()
    rows = data["results"] if isinstance(data, dict) and "results" in data else data
    canonical = json.dumps(rows, sort_keys=True, ensure_ascii=False)
    fingerprint = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
    print(f"orders returned : {len(rows)}")
    print(f"SQL queries     : {len(ctx.captured_queries)}")
    print(f"time            : {elapsed_ms:.0f} ms")
    print(f"fingerprint     : {fingerprint}")
    if isinstance(data, dict):
        print("note            : the response is now paginated (API shape changed)")


if __name__ == "__main__":
    main()
