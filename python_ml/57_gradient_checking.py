"""ML Practice: Numerical Gradient Checking vs Analytic Gradient"""


def f(weights, x):
    return sum(w * xi for w, xi in zip(weights, x)) ** 2


def analytic_gradient(weights, x):
    dot = sum(w * xi for w, xi in zip(weights, x))
    return [2 * dot * xi for xi in x]


def numerical_gradient(weights, x, eps=1e-5):
    grad = []
    for i in range(len(weights)):
        plus = weights[:]
        minus = weights[:]
        plus[i] += eps
        minus[i] -= eps
        grad.append((f(plus, x) - f(minus, x)) / (2 * eps))
    return grad


def relative_error(a, b):
    return [abs(ai - bi) / max(1e-8, abs(ai) + abs(bi)) for ai, bi in zip(a, b)]


if __name__ == "__main__":
    weights = [0.5, -1.2, 2.0]
    x = [1.0, 2.0, 3.0]

    analytic = analytic_gradient(weights, x)
    numerical = numerical_gradient(weights, x)
    errors = relative_error(analytic, numerical)

    print("Analytic gradient: ", [round(g, 5) for g in analytic])
    print("Numerical gradient:", [round(g, 5) for g in numerical])
    print("Relative errors:   ", [round(e, 8) for e in errors])
    print("Gradient check passed:", all(e < 1e-4 for e in errors))
