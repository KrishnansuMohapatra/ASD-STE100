# Output 1 — Response to: "Explain gradient descent."

Gradient descent is a first-order iterative optimization algorithm for minimizing a differentiable objective function. In machine learning, that objective is usually a loss function L(θ) that measures how far a model's predictions are from the training data, and θ denotes the model's parameters (weights and biases).

The core idea: at the current point θ, the gradient ∇L(θ) points in the direction of steepest increase of L. To decrease the loss, you move in the opposite direction:

θ ← θ − η∇L(θ)

where η > 0 is the learning rate, which controls the step size. This update is repeated until convergence, i.e., until the gradient is close to zero or the loss stops improving significantly.

Main variants:

- Batch gradient descent: computes the gradient using the entire dataset. Stable, but slow and memory-heavy for large datasets.
- Stochastic gradient descent (SGD): computes the gradient from a single randomly chosen sample. Noisy, but cheap per step and can escape shallow local minima.
- Mini-batch gradient descent: uses a small batch of samples per step. This is the practical default in deep learning because it balances noise and efficiency and maps well onto GPUs.
- Adaptive methods such as Momentum, RMSProp, and Adam adjust step sizes per parameter using history of past gradients, usually converging faster with less tuning.

Key practical points:

- If the learning rate is too large, updates overshoot the minimum and can diverge; if it is too small, training is very slow and can stall in flat regions.
- For non-convex loss surfaces (e.g., neural networks), gradient descent finds a local minimum rather than a guaranteed global minimum; in practice this is usually good enough.
- Feature scaling and normalization make the loss surface more isotropic, so the gradient points more directly at the minimum and convergence is faster.
- Learning-rate schedules and early stopping are commonly used to improve convergence and generalization.

In short, gradient descent repeatedly takes small steps in the direction that reduces the loss, tuning the model's parameters until predictions improve.
