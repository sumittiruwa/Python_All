"""OpenCV Practice: cv2.fitLine on Synthetic Noisy Points"""

import cv2
import numpy as np


def make_noisy_line_points(n=60, seed=0):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 100, n)
    y = 2.0 * x + 5.0 + rng.normal(0, 3.0, size=n)
    return np.stack([x, y], axis=1).astype(np.float32)


def fit_line(points):
    vx, vy, x0, y0 = cv2.fitLine(points, cv2.DIST_L2, 0, 0.01, 0.01).ravel()
    slope = vy / vx
    intercept = y0 - slope * x0
    return float(slope), float(intercept)


if __name__ == "__main__":
    points = make_noisy_line_points()
    slope, intercept = fit_line(points)

    print("Points:", points.shape)
    print("Fitted slope:", round(slope, 3))
    print("Fitted intercept:", round(intercept, 3))
    print("Predicted y at x=50:", round(slope * 50 + intercept, 3))
