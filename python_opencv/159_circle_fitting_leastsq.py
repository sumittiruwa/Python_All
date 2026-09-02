"""OpenCV Practice: Least-Squares Circle Fit to Noisy Points"""

import numpy as np


def make_noisy_circle_points(cx=5.0, cy=-3.0, r=10.0, n=80, seed=0):
    rng = np.random.default_rng(seed)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    noise = rng.normal(0, 0.2, size=n)
    x = cx + (r + noise) * np.cos(angles)
    y = cy + (r + noise) * np.sin(angles)
    return np.stack([x, y], axis=1)


def fit_circle(points):
    x, y = points[:, 0], points[:, 1]
    A = np.stack([2 * x, 2 * y, np.ones_like(x)], axis=1)
    b = x ** 2 + y ** 2
    sol, *_ = np.linalg.lstsq(A, b, rcond=None)
    cx, cy, c = sol
    r = np.sqrt(c + cx ** 2 + cy ** 2)
    return cx, cy, r


if __name__ == "__main__":
    points = make_noisy_circle_points()
    cx, cy, r = fit_circle(points)

    print("Points:", points.shape)
    print("Fitted center:", (round(float(cx), 3), round(float(cy), 3)))
    print("Fitted radius:", round(float(r), 3))
