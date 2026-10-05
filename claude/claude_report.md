# Claude — Gradient Descent Prompt Experiment

## Prompt 1 — Plain prompt

**Prompt:**

```text
Explain gradient descent.
```

### Output 1

Gradient descent is an optimization algorithm. It finds the input values that make a function as small as possible. In machine learning, that function is usually the loss function, which measures how wrong a model's predictions are.

**Core idea**

Suppose a model has parameters θ and a loss L(θ). The gradient ∇L(θ) is the vector of partial derivatives of the loss. It points in the direction where the loss increases fastest. To reduce the loss, move in the opposite direction:

θ ← θ − η ∇L(θ)

Here η is the learning rate, a hyperparameter that sets the step size. Repeat until the loss stops improving.

**Variants**

- Batch gradient descent computes the gradient on the full dataset. It is stable but slow on large data.
- Stochastic gradient descent (SGD) uses one example per step. It is fast and noisy.
- Mini-batch gradient descent uses small batches. It is the usual default.
- Momentum, RMSProp and Adam adapt the updates to speed up convergence.

**Practical issues**

If η is too large, the updates overshoot and may diverge. If it is too small, training is slow. On non-convex losses, the algorithm can settle in local minima or stall at saddle points. Feature scaling and learning-rate schedules help.

**Convergence**

For convex functions with a suitable learning rate, gradient descent converges to the global minimum. For the non-convex losses of deep networks, it usually finds a good minimum, not a guaranteed best one.

---

# Prompt 2 — "Simply, to a beginner"

**Prompt:**

```text
Explain gradient descent simply to a beginner.
```

### Output 2

Imagine you are standing on a hill in thick fog. You want to reach the bottom, but you cannot see it. What do you do?

You feel the ground with your feet. You find which way slopes down. You take a small step that way. Then you check again and repeat. Step by step, you walk down the hill.

That is gradient descent.

In machine learning, the "hill" is the model's error. A high spot means many mistakes. A low spot means few mistakes. The computer wants to reach the lowest spot.

The "slope" is called the gradient. It tells the computer which way to change the model's numbers to make the error smaller. The size of each step is called the learning rate.

Tiny example: you want to find the lowest point of y = x². Start at x = 10. The slope there is 20, so you move left a bit. Now x = 8. Repeat. You get closer to 0, the bottom.

Watch out: if your steps are too big, you can jump over the bottom and end up higher up. If they are too small, you walk forever.

In short: gradient descent = feel the slope, step downhill, repeat.

---

# Prompt 3 — ASD-STE100 + Requirements

**Prompt:**

```text
Explain gradient descent using the principles of ASD-STE100 Simplified Technical English.

Audience:
A beginner who knows basic Python but does not know machine learning.

Requirements:

- Use short sentences.
- Use simple words where possible.
- Define technical terms before using them.
- Use direct sentences.
- Avoid unnecessary jargon.
- Give one simple example.
- Explain one common mistake.
- End with a short summary.
```

### Output 3

## Terms

A **function** is a rule. It takes a number and gives a number.

A **parameter** is a number that a model can change.

The **loss** is a number. It shows how wrong a model is. A low loss is good.

The **gradient** is the slope of the loss. It shows which direction makes the loss larger.

The **learning rate** is the size of each step. It is a small number, for example 0.1.

## What gradient descent does

Gradient descent is a method. It changes parameters to make the loss smaller.

Use these steps:

1. Start with a guess for the parameter.
2. Calculate the gradient.
3. Subtract the gradient, multiplied by the learning rate, from the parameter.
4. Do steps 2 and 3 again.
5. Stop when the loss does not become smaller.

The formula is `x = x - learning_rate * gradient`.

## Example

Find the x that makes f(x) = x * x as small as possible. The gradient of this function is 2 * x.

```python
x = 10.0
learning_rate = 0.1

for step in range(5):
    gradient = 2 * x
    x = x - learning_rate * gradient
    print(step, x)
```

The values of x are about 8.0, 6.4, 5.12, 4.096, and 3.277. The value of x moves toward 0. At x = 0, the function has its smallest value.

## Common mistake

Do not use a learning rate that is too large. Assume the learning rate is 1.1. Then x goes from 10 to -12, and then to 14.4. The value moves away from 0. The loss becomes larger. Use a smaller learning rate, for example 0.1.

## Summary

Gradient descent changes a parameter in small steps. Each step goes against the gradient. The loss becomes smaller. Choose a small learning rate.

---

# Claude — Measured Results

| Metric | R1 (plain) | R2 (beginner) | R3 (STE + requirements) |
|---|---:|---:|---:|
| Words (excluding code) | 241 | 199 | 266 |
| Sentence units | 27 | 25 | 44 |
| Average words per unit | 8.9 | 8.0 | **6.0** |
| Longest unit | 19 | 19 | **17** |
| Units over 20 words | 0 | 0 | 0 |
| Jargon keyword hits | 24 | **0** | **0** |

## Claude's observed result

**R1:** Most technically complete.

**R2:** Shortest and strongest intuitive explanation.

**R3:** Longest by word count, but shortest average sentence length and the strongest match to the explicit requirements.

The key observation is that **shorter does not necessarily mean simpler**. R3 contained more words than R2, but used shorter sentence units and followed more explicit constraints.

---

> **Model name note (added by the workspace):** These outputs are labelled as produced by **Claude** on claude.ai's **free tier**. According to 2026 sources, the free plan's default model is **Claude Sonnet 5** (default since July 2026; earlier in 2026 the free default was Claude Sonnet 4.5). Exact model per session can vary.
