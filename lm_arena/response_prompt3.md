# Output 3 — Response to the full ASD-STE100 prompt

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

You want the model to learn the line y = 2x. The model starts with the parameter w = 0. For each data point it guesses y = w * x. The loss compares the guess with the real value. The model changes w by a small amount each time. After many steps, w is close to 2.

**One common mistake**

One common mistake is a learning rate that is too big. The steps are then too long. The loss goes up and down and never gets smaller. Start with a small learning rate.

**Summary**

Gradient descent changes the parameters of a model step by step. It does this to make the loss smaller. Small, steady steps work best.
