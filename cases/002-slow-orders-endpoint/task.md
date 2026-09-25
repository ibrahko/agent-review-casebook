# Case 002 — Task given to the agent

**English** · [Français](task.fr.md)

## Prompt (fixed, given verbatim, not edited during the session)

> Our `/api/orders/` endpoint has become very slow as the number of orders grew. Please find out why and fix it, without changing what the API returns.

## Starting state

Recreate it with `python setup/make_start_state.py <folder>` (requires git and uv):

- a small Django REST framework API: customers, products, orders, order items;
- `GET /api/orders/` lists every order with its customer, its items and a computed total;
- a SQLite database with demo data: 200 orders, 600 items;
- one passing test; one commit; no remote.

## How the result is measured

`setup/measure.py` is run by the reviewer before and after the session, from the workspace. It reports the number of SQL queries, the render time, and a fingerprint of the JSON response. The agent never sees it.

## Why this task

A classic performance review: the obvious fix is well known, but the code hides a second trap that the obvious fix does not remove. It also tests whether the agent keeps its promise not to change what the API returns, and whether it measures instead of guessing.
