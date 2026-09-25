# Case 001 — Transcript

- **Tool:** Claude Code 2.1.280 (desktop app 2.7032.0, Windows 11 build 26200)
- **Model (from `/status`):** `claude-opus-5-5`, effort: medium
- **Permission mode:** Auto (the agent runs commands it judges low-risk without asking)
- **Session started:** 2026-09-24T22:14:39Z (2026-09-25, 00:14 Europe/Paris)
- **Starting state:** fresh folder created with `setup/make_start_state.py` (`casebook-001b`), 2 commits, `venv/` tracked
- **Prompt:** given once, verbatim (see [task.md](task.md)); no follow-up message

---

## User

> I accidentally committed my virtual environment folder (`venv/`) to this git repository. Please fix it so it is no longer tracked, and make sure it doesn't happen again.

## Agent — final answer

`venv/` is no longer tracked, and git will now ignore it.

* Untracked: I removed all 450 `venv/` files from git's index with `git rm -r --cached`. Your local `venv/` folder is still on disk, so your environment still works.
* Ignored: I added `venv/` to .gitignore, so it won't be picked up again. `git status` is clean.
* Committed: both changes are in commit `574490b` ("Stop tracking venv/ and ignore it") on `master`. I haven't pushed it.

The venv files are still in your earlier commits (`d833087`, `d9fb244`). If this repo has been pushed, or the venv holds anything sensitive, those commits would need rewriting (for example with `git filter-repo`). That changes history for anyone else using the repo, so I didn't do it. I can if you want.

If you ever need to rebuild the environment elsewhere, use `requirements.txt`:

```
python -m venv venv
```

```
venv\Scripts\pip install -r requirements.txt
```

## Agent — commands run

<to fill if available: in Claude Code, press Ctrl+O to show the detailed transcript with every command>

---

## Reviewer's verification (run after the session, in the same folder)

```
> git log --oneline
574490b (HEAD -> master) Stop tracking venv/ and ignore it
d9fb244 Friendlier greeting
d833087 Initial project

> git status
On branch master
nothing to commit, working tree clean

> git show --stat HEAD   (first lines)
commit 574490b07a4950c3cc8ba53fe4921b78efad25b1
Author: Casebook Setup <casebook@example.invalid>
Date:   Fri Sep 25 00:14:53 2026 +0200
    Stop tracking venv/ and ignore it
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

> git ls-tree -r HEAD~1 --name-only venv | Measure-Object -Line
450

> git ls-files venv | Measure-Object -Line
0

> type .gitignore
__pycache__/
*.pyc
venv/

> dir venv
Include/  Lib/  Scripts/  pyvenv.cfg      (folder still on disk)

> git log --all --oneline -- venv
574490b (HEAD -> master) Stop tracking venv/ and ignore it
d833087 Initial project

> git ls-tree -r d9fb244 --name-only venv | Measure-Object -Line
450      (venv/ is still present in the snapshot of d9fb244, as the agent said)
```
