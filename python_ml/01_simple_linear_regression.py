"""ML Practice: Simple Linear Regression using Gradient Descent"""


def train(x, y, lr=0.01, epochs=1000):
    m, b = 0.0, 0.0
    n = len(x)

    for _ in range(epochs):
        y_pred = [m * xi + b for xi in x]
        dm = (-2 / n) * sum(x[i] * (y[i] - y_pred[i]) for i in range(n))
        db = (-2 / n) * sum(y[i] - y_pred[i] for i in range(n))
        m -= lr * dm
        b -= lr * db

    return m, b


def predict(x, m, b):
    return [m * xi + b for xi in x]


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [3, 5, 7, 9, 11]

    m, b = train(x, y)
    print(f"Learned: y = {m:.3f}x + {b:.3f}")
    print("Predictions:", [round(p, 2) for p in predict(x, m, b)])
