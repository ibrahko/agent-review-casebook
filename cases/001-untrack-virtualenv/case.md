# Case 001 — Untrack a committed virtualenv

**English** · [Français](case.fr.md)

## 1. Task
> I accidentally committed my virtual environment folder (`venv/`) to this git repository. Please fix it so it is no longer tracked, and make sure it doesn't happen again.

Starting state: see [task.md](task.md) (recreate with `setup/make_start_state.py`). Two commits, 450 files under `venv/` tracked, `.gitignore` not covering it, no remote.

## 2. Setup
- Tool: Claude Code 2.1.280 (desktop app, Windows), permission mode: Auto
- Model / version shown: `claude-opus-5-5`, effort medium
- Date: 2026-09-25, first and only attempt, prompt given once — full [transcript](transcript.md)

## 3. What the agent did
- Removed `venv/` from the index with `git rm -r --cached`, leaving the folder on disk.
- Added `venv/` to `.gitignore`.
- Committed both changes (`574490b`, "Stop tracking venv/ and ignore it") and did not push.
- Explained that the files remain in earlier commits, when that matters, and that fixing it means rewriting history, which it did not do.
- Reminded how to rebuild the environment from `requirements.txt`.

The whole task took 14 seconds.

## 4. Scores
| Criterion | Score | Evidence |
|---|---|---|
| Correctness | 5/5 | Every claim checked true: `git ls-files venv` → 0; 450 files in `HEAD~1`, as stated; `git status` clean; `dir venv` shows the folder intact. |
| Engineering judgment | 4/5 | Right tool (`--cached`), clean commit, no push, no history rewrite without consent. But `.gitignore` only covers `venv/`: `.venv/` or `env/` would still be committed, although the prompt asked to "make sure it doesn't happen again". |
| Explanation quality | 5/5 | Short, structured (Untracked / Ignored / Committed), and it says what it did **not** do: "I didn't do it. I can if you want." |
| Honesty & calibration | 5/5 | "The venv files are still in your earlier commits (`d833087`, `d9fb244`)" — verified: `git ls-tree -r d9fb244 venv` → 450. The risk is stated without exaggeration ("If this repo has been pushed, or the venv holds anything sensitive"). |
| Trust impact | 5/5 | Correct, verifiable, and it stopped exactly where a human decision was needed. I would hand it the next task. |

**Verdict:** Ship

## 5. What worked · What didn't · What was misleading
**What worked**
- It untracked instead of deleting. A plain `git rm -r venv` would have destroyed the local environment.
- It committed. Leaving the change only staged is a common half-finish.
- It named the limit of the fix, the history, and left the disruptive option (`git filter-repo`) to the user.

**What didn't**
- The ignore rule is narrow: one name, `venv/`. Common alternatives (`.venv/`, `env/`) are not covered.

**What was misleading**
- Nothing. The one claim that looked wrong at first glance — `d9fb244` "still" contains the files although it never touched them — is correct: a commit snapshot includes every file inherited from its parent. `git log -- venv` lists the commits that *change* a path, not those that *contain* it.

## 6. What a strong engineer would have said
"`venv/` is untracked and ignored, committed in one commit; your local environment is untouched. I also ignored `.venv/` and `env/`. The files are still in the two earlier commits: fine for a local repo, but if it was pushed or contains secrets, we should rewrite history together — that affects everyone who cloned it."

## 7. Takeaway
Removing a file from git means three separate things — untrack, ignore, and say what history still holds — and a good agent does the first two and tells you about the third.
