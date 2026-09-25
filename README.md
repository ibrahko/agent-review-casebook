# Agent Review Casebook

**English** · [Français](README.fr.md)

> **Work in progress — v0.1.** Rubric, template and case 001.

How good is an AI coding agent's answer, really? This casebook judges real sessions with Claude Code, Cursor and OpenAI Codex on realistic Python back-end tasks, the way a senior engineer reviews a pull request: is it right, is it misleading, and which of two answers is better, with evidence.

## How to read it (3 minutes)

1. The [rubric](RUBRIC.md): five criteria scored 1 to 5, and a verdict (*Ship / Ship with fixes / Do not ship*).
2. Any case below: 400 to 700 words, every score backed by a quote from the transcript.

## Cases

| # | Task | Tool | Verdict |
|---|---|---|---|
| [001](cases/001-untrack-virtualenv/case.md) | Untrack a committed virtualenv | Claude Code (`claude-opus-5-5`) | **Ship** |
| [002](cases/002-slow-orders-endpoint/case.md) | Slow orders endpoint (N+1 queries) | — | *in progress* |

## Method

- Every task starts from a known state that anyone can recreate (`setup/` script in each case).
- The prompt is written **before** the session and never edited afterwards.
- Comparisons use the same prompt, the same starting state and the **first attempt** of each tool (no best-of-three).
- Scores are given after checking the result (tests run, diff read), not from the agent's own summary.
- No client code, no real data, no secrets. Brands are not ranked: answers are.

Every document exists in English and French; case files are written in English first, then translated.

## Author

**Ibrahima Koné** — backend Python & AI engineer, Bamako, Mali  
[GitHub](https://github.com/ibrahko) · [LinkedIn](https://www.linkedin.com/in/ibrahima-koné-632006a1)

## License

Text: CC BY 4.0 · Code: MIT — © 2026 Ibrahima Koné
