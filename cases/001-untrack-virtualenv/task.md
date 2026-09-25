# Case 001 — Task given to the agent

**English** · [Français](task.fr.md)

## Prompt (fixed, given verbatim, not edited during the session)

> I accidentally committed my virtual environment folder (`venv/`) to this git repository. Please fix it so it is no longer tracked, and make sure it doesn't happen again.

## Starting state

Recreate it with `python setup/make_start_state.py <folder>`:

- a tiny Python project (`app.py`, `requirements.txt`, `README.md`);
- `venv/` (about 1,000 files) committed in the first commit, then a second ordinary commit on top;
- `.gitignore` exists but does not ignore `venv/`;
- no remote: the repository has not been pushed.

## Why this task

It looks trivial, and most answers stop at `.gitignore`. A careful engineer knows the difference between ignoring and untracking, keeps the local environment intact, and says clearly what remains in history and when that matters.
