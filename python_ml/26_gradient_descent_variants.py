"""ML Practice: Batch, Stochastic, and Mini-Batch Gradient Descent"""

import random


def compute_gradient(x_batch, y_batch, m, b):
    n = len(x_batch)
    y_pred = [m * x_batch[i] + b for i in range(n)]
    dm = (-2 / n) * sum(x_batch[i] * (y_batch[i] - y_pred[i]) for i in range(n))
    db = (-2 / n) * sum(y_batch[i] - y_pred[i] for i in range(n))
    return dm, db


def batch_gradient_descent(x, y, lr=0.01, epochs=200):
    m, b = 0.0, 0.0
    for _ in range(epochs):
        dm, db = compute_gradient(x, y, m, b)
        m -= lr * dm
        b -= lr * db
    return m, b


def stochastic_gradient_descent(x, y, lr=0.01, epochs=200, seed=1):
    random.seed(seed)
    m, b = 0.0, 0.0
    for _ in range(epochs):
        i = random.randint(0, len(x) - 1)
        dm, db = compute_gradient([x[i]], [y[i]], m, b)
        m -= lr * dm
        b -= lr * db
    return m, b


def mini_batch_gradient_descent(x, y, lr=0.01, epochs=200, batch_size=2, seed=1):
    random.seed(seed)
    m, b = 0.0, 0.0
    n = len(x)
    for _ in range(epochs):
        indices = random.sample(range(n), min(batch_size, n))
        x_batch = [x[i] for i in indices]
        y_batch = [y[i] for i in indices]
        dm, db = compute_gradient(x_batch, y_batch, m, b)
        m -= lr * dm
        b -= lr * db
    return m, b


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [3, 5, 7, 9, 11]

    print("Batch GD:", tuple(round(v, 3) for v in batch_gradient_descent(x, y)))
    print("Stochastic GD:", tuple(round(v, 3) for v in stochastic_gradient_descent(x, y)))
    print("Mini-Batch GD:", tuple(round(v, 3) for v in mini_batch_gradient_descent(x, y)))
