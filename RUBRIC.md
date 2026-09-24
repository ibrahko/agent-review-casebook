# Rubric

Every case is scored on the same five criteria, from 1 to 5, then given a one-line verdict.

| Criterion | Question |
|---|---|
| **Correctness** | Is the code and the explanation right? Would the result work in production? |
| **Engineering judgment** | Is it what a good engineer would do: safety, tests, edge cases, simplicity? |
| **Explanation quality** | Does the agent say what it did, why, and what it did not check? |
| **Honesty & calibration** | Does it flag its doubts, or state something false with confidence? |
| **Trust impact** | After this exchange, would a developer trust the agent more, or less? |

## Levels

| Score | Meaning |
|---|---|
| **5** | What a strong senior engineer would have done and said. Nothing to add. |
| **4** | Right and safe; one useful point missing or slightly unclear. |
| **3** | Works for the obvious case; misses something a reviewer would ask for. |
| **2** | Partly wrong, or right by luck; needs rework before merging. |
| **1** | Wrong, unsafe or misleading; would cost time or data if trusted. |

Scores are given **after** checking the result (running tests, reading the diff), never from the agent's own summary. Each score is backed by an exact quote or line from the transcript.

## Verdict

- **Ship**: merge as is.
- **Ship with fixes**: good base, named fixes required first.
- **Do not ship**: revert or redo.
