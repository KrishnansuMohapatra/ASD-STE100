# Chat Experiment Report — Three Prompts on Gradient Descent

**Date:** 2026-10-05 · **Method:** All three prompts were run verbatim (no changes) against the same
assistant in the same session. Outputs were then scored against one fixed rubric, and readability
metrics were computed programmatically (`metrics.py`) to keep the evaluation objective.

---

## 1. Prompts (verbatim, unchanged)

**Prompt 1**
> Explain gradient descent.

**Prompt 2**
> Explain gradient descent simply to a beginner.

**Prompt 3**
> Explain gradient descent using the principles of ASD-STE100 Simplified Technical English.
>
> Audience:
> A beginner who knows basic Python but does not know machine learning.
>
> Requirements:
> - Use short sentences.
> - Use simple words where possible.
> - Define technical terms before using them.
> - Use direct sentences.
> - Avoid unnecessary jargon.
> - Give one simple example.
> - Explain one common mistake.
> - End with a short summary.

---

## 2. Outputs (verbatim)

### Output 1 — from Prompt 1

Gradient descent is a first-order iterative optimization algorithm for minimizing a differentiable
objective function. In machine learning, that objective is usually a loss function L(θ) that measures
how far a model's predictions are from the training data, and θ denotes the model's parameters
(weights and biases).

The core idea: at the current point θ, the gradient ∇L(θ) points in the direction of steepest
increase of L. To decrease the loss, you move in the opposite direction:

θ ← θ − η∇L(θ)

where η > 0 is the learning rate, which controls the step size. This update is repeated until
convergence, i.e., until the gradient is close to zero or the loss stops improving significantly.

Main variants:

- Batch gradient descent: computes the gradient using the entire dataset. Stable, but slow and
  memory-heavy for large datasets.
- Stochastic gradient descent (SGD): computes the gradient from a single randomly chosen sample.
  Noisy, but cheap per step and can escape shallow local minima.
- Mini-batch gradient descent: uses a small batch of samples per step. This is the practical default
  in deep learning because it balances noise and efficiency and maps well onto GPUs.
- Adaptive methods such as Momentum, RMSProp, and Adam adjust step sizes per parameter using history
  of past gradients, usually converging faster with less tuning.

Key practical points:

- If the learning rate is too large, updates overshoot the minimum and can diverge; if it is too
  small, training is very slow and can stall in flat regions.
- For non-convex loss surfaces (e.g., neural networks), gradient descent finds a local minimum rather
  than a guaranteed global minimum; in practice this is usually good enough.
- Feature scaling and normalization make the loss surface more isotropic, so the gradient points more
  directly at the minimum and convergence is faster.
- Learning-rate schedules and early stopping are commonly used to improve convergence and
  generalization.

In short, gradient descent repeatedly takes small steps in the direction that reduces the loss,
tuning the model's parameters until predictions improve.

### Output 2 — from Prompt 2

Think of gradient descent like walking down a foggy hill.

You are standing on the hill, and the fog is so thick that you cannot see the bottom. All you can
feel is the slope of the ground under your feet. So you take a small step in the direction that feels
steepest downhill. Then you feel the slope again, and take another step. You repeat this until you
reach flat ground at the bottom.

Machine learning works the same way. A model starts with a bunch of numbers, called weights. It makes
a prediction, then checks how wrong it was. That "how wrong" score is called the loss. The model then
figures out which way to nudge its weights to make the loss a little smaller, nudges them, and tries
again.

Each step has a size, called the learning rate. Big steps get you downhill faster, but you might trip
and overshoot the bottom. Small steps are safer, but slower.

After many small adjustments, the loss gets small, which means the model's predictions have gotten
good. That is all gradient descent really is: repeatedly nudging numbers in the direction that
reduces the error.

### Output 3 — from Prompt 3

Gradient descent is a method to find good numbers for a model.

**Words you must know**

- A **model** is a program that makes guesses from data.
- A **parameter** is a number inside the model. The model can change this number.
- The **loss** is a number that shows how bad the guesses are. A low loss is good.
- The **gradient** shows the direction in which the loss goes up.
- The **learning rate** sets the size of each step.

**How it works**

1. The model makes a guess.
2. The loss shows how wrong the guess is.
3. The gradient shows which way the loss goes up.
4. The model moves the parameters the other way. This makes the loss smaller.
5. The model repeats these steps many times.

**Example**

You want the model to learn the line y = 2x. The model starts with the parameter w = 0. For each data
point it guesses y = w * x. The loss compares the guess with the real value. The model changes w by a
small amount each time. After many steps, w is close to 2.

**One common mistake**

One common mistake is a learning rate that is too big. The steps are then too long. The loss goes up
and down and never gets smaller. Start with a small learning rate.

**Summary**

Gradient descent changes the parameters of a model step by step. It does this to make the loss
smaller. Small, steady steps work best.

---

## 3. Quantitative metrics (measured, not judged)

| Metric | P1 bare | P2 simple | P3 STE+constraints |
|---|---:|---:|---:|
| Words | 320 | 194 | 238 |
| Sentences | 17 | 16 | 27 |
| Avg sentence length (words) | 18.8 | 12.1 | **8.8** |
| Longest sentence (words) | 32 | 23 | **14** |
| Sentences over 20 words (STE limit) | 7 | 1 | **0** |
| Flesch Reading Ease (higher = easier) | 41.3 (difficult) | 82.0 (easy) | **87.0** (very easy) |
| Technical-term hits | 29 | 3 | 3 |

Reading-ease bands: 0–30 college graduate, 30–50 fairly difficult, 60–70 plain English, 80+ easy.

---

## 4. Requirements compliance (rubric applied identically to all three)

Legend: ✅ yes · 🟡 partial · ❌ no

| Requirement | P1 bare | P2 simple | P3 STE |
|---|:---:|:---:|:---:|
| Short sentences | ❌ | ✅ | ✅ |
| Simple words where possible | ❌ | ✅ | ✅ |
| Technical terms defined before use | ❌ | 🟡 (loss, weights, learning rate defined inline; "gradient" never defined) | ✅ (glossary first) |
| Direct sentences | 🟡 (some passive voice) | ✅ | ✅ |
| Avoid unnecessary jargon | ❌ | ✅ | ✅ |
| One simple example | ❌ | 🟡 (hill analogy, not a worked example) | ✅ (y = 2x line fit) |
| One common mistake explained | 🟡 (learning-rate pitfall listed, not framed as a mistake) | 🟡 (overshoot risk mentioned, not framed as a mistake) | ✅ (dedicated section) |
| Ends with a short summary | ✅ | ✅ | ✅ |
| **Score (✅=1, 🟡=0.5)** | **1.5 / 8** | **6.0 / 8** | **8 / 8** |

Audience fit (beginner who knows basic Python, no ML): Output 1 would lose this reader. Output 2 is
comfortable to read but contains no code-flavoured example. Output 3's example reads like Python
assignment (`y = w * x`), which matches the audience, though it does not use real Python syntax.

---

## 5. Per-prompt findings

**Prompt 1 — "Explain gradient descent."**
- Strengths: technically complete and accurate; covers the update rule, variants (batch/SGD/mini-batch/Adam),
  and practical caveats; dense with information for a technical reader.
- Weaknesses: for the stated beginner audience it fails 6 of 8 requirements. 29 technical terms,
  several introduced without definition ("differentiable", "isotropic", "non-convex"); a 32-word sentence;
  Flesch score 41.3 = "difficult" reading level.
- Verdict: a good *reference* answer, a poor *beginner* answer. The bare prompt gives the model no
  reason to optimize for anything but completeness.

**Prompt 2 — "Explain gradient descent simply to a beginner."**
- Strengths: the foggy-hill analogy is accurate and memorable; reading ease 82.0; most terms
  ("weights", "loss", "learning rate") are explained in context.
- Weaknesses: "gradient" itself is never actually defined; the overshoot problem is hinted at but not
  framed as a common mistake; one sentence still runs 23 words; no worked example.
- Verdict: a large jump in accessibility from one added clause ("simply to a beginner"), but soft
  wording only produces soft compliance.

**Prompt 3 — STE prompt with explicit constraints**
- Strengths: satisfies all 8 requirements. Glossary before first use, longest sentence 14 words,
  zero sentences over the STE 20-word limit, Flesch 87.0, numbered procedure, concrete example,
  labelled mistake, labelled summary.
- Weaknesses (real trade-offs): the restricted vocabulary makes the prose clipped and slightly
  mechanical ("guesses" instead of "predictions"); depth is sacrificed — no mention of variants
  (SGD/mini-batch) or of gradients as slopes of a curve; STE-style text can feel repetitive.
- Verdict: the only output that fully matches the spec, at the cost of breadth and stylistic warmth.

---

## 6. Overall conclusion

1. **Prompt specificity drives output fit.** Compliance rose monotonically with prompt constraint:
   1.5/8 → 6/8 → 8/8. The bare prompt produced a generic expert-level answer; each layer of
   instruction measurably reshaped the output.
2. **Readability improved measurably, not just perceptibly:** Flesch 41.3 → 82.0 → 87.0; average
   sentence length 18.8 → 12.1 → 8.8 words.
3. **There is no universally "best" prompt.** Output 1 is the best answer for an engineer refreshing
   their memory; Output 3 is the best answer for the stated audience. Output quality is fitness for
   purpose, and purpose must be stated in the prompt.
4. **Explicit checklists beat adjectives.** "Simply to a beginner" (adjective) got partial compliance;
   enumerated requirements got full compliance.

---

## 7. Bias controls and limitations

- All three outputs came from the same assistant in one session, so differences are attributable to
  prompt wording, not to different models — but they are also attributable to this one model's habits;
  results may vary with another model.
- The same assistant produced and graded the outputs. To limit self-grading bias, the rubric was fixed
  before grading, and all numbers in §3 were computed by script, not by judgment.
- Flesch Reading Ease is a heuristic; syllable counting was approximate.
- "Accuracy" was checked qualitatively; all three outputs are factually correct about gradient descent.

---

## 8. Model name

The user asked for the model name. Per Arena.ai policy, this assistant identifies as a **helpful
agent on Arena.ai** and does not disclose the specific underlying model powering this session.
Arena.ai's Agent Mode runs on many different models — including, but not limited to, Claude, ChatGPT,
Gemini, Grok, Qwen, and Kimi.

---

## 9. Companion experiment: Claude (claude.ai free tier)

The same three prompts were also run on **Claude** (free tier; claude.ai's free default is
Claude Sonnet 5 since July 2026, previously Claude Sonnet 4.5). Full transcript and Claude's own
measurements are in [`../claude/claude_report.md`](../claude/claude_report.md).

Claude's headline numbers (self-measured, different counting method from §3):

| Metric | C1 plain | C2 beginner | C3 STE+reqs |
|---|---:|---:|---:|
| Words (excl. code) | 241 | 199 | 266 |
| Avg words per sentence unit | 8.9 | 8.0 | 6.0 |
| Units over 20 words | 0 | 0 | 0 |
| Jargon keyword hits | 24 | 0 | 0 |

Cross-experiment observations (where both experiments agree):

- Both assistants: the bare prompt produced a jargon-heavy technical answer; adding
  "simply to a beginner" sharply reduced jargon; the STE prompt with an explicit checklist
  produced the shortest sentences and best requirement compliance.
- Both: plain-prompt output was the most complete but least audience-fit; compliance rose
  monotonically with prompt constraint.
- Differences worth noting: Claude's plain-prompt output was already written in short sentences
  (avg 8.9 words, no unit over 20), while this workspace's plain output used long sentences
  (avg 18.8, 7 over 20). Claude's STE output included runnable Python code, directly matching
  the "knows basic Python" audience; this workspace's used pseudo-code prose instead. Claude
  concluded "shorter does not necessarily mean simpler" (R3 had more words than R2 but shorter
  sentences) — consistent with this report's finding that constraints trade breadth for fit.

Caveat: the two reports used different measurement scripts, so numbers are not directly
comparable; only directional conclusions should be compared.

---

## Files

- `response_prompt1.md`, `response_prompt2.md`, `response_prompt3.md` — raw outputs
- `metrics.py` — script that produced the numbers in §3
- `../claude/claude_report.md` — companion experiment run on Claude (free tier), with Claude's own measurements
