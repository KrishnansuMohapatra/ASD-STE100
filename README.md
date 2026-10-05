# ASD-STE100

An experiment comparing three prompting styles for explaining gradient descent: a plain prompt, a beginner-focused prompt, and an ASD-STE100-inspired prompt. Tested across Claude and LM Arena to compare readability, technical depth, prompt compliance, and beginner-friendliness.

## The three prompts (used verbatim in every run)

1. `Explain gradient descent.`
2. `Explain gradient descent simply to a beginner.`
3. `Explain gradient descent using the principles of ASD-STE100 Simplified Technical English.` — plus a fixed audience (beginner who knows basic Python, no machine learning) and eight explicit requirements: short sentences, simple words, terms defined before use, direct sentences, no unnecessary jargon, one simple example, one common mistake, short summary at the end.

## Contents

| Report | Assistant | Highlights |
|---|---|---|
| [`lm_arena/readme.md`](lm_arena/readme.md) | Arena.ai Agent Mode | Full outputs, script-computed readability metrics (Flesch 41.3 → 82.0 → 87.0), 8-point requirement checklist (1.5/8 → 6/8 → 8/8), cross-experiment comparison |
| [`claude/claude_report.md`](claude/claude_report.md) | Claude (claude.ai free tier) | Full outputs with runnable Python example, Claude's own measurements (avg sentence units 8.9 → 8.0 → 6.0 words), key observation: "shorter does not necessarily mean simpler" |

## Shared conclusion

Both assistants show the same pattern: the bare prompt produces a jargon-heavy expert answer, "simply to a beginner" cuts jargon sharply, and the ASD-STE100 prompt with an explicit checklist produces the shortest sentences and the best requirement compliance. Explicit constraints beat adjectives — but they trade breadth and stylistic warmth for audience fit.
