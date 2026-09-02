"""OpenCV Practice: cv2.kmeans Clustering on Synthetic 2D Points"""

import cv2
import numpy as np


def make_clusters(seed=0):
    rng = np.random.default_rng(seed)
    a = rng.normal((2, 2), 0.4, size=(30, 2))
    b = rng.normal((10, 10), 0.4, size=(30, 2))
    c = rng.normal((2, 10), 0.4, size=(30, 2))
    return np.vstack([a, b, c]).astype(np.float32)


def run_kmeans(points, k=3):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 1.0)
    compactness, labels, centers = cv2.kmeans(points, k, None, criteria, 5, cv2.KMEANS_PP_CENTERS)
    return compactness, labels.ravel(), centers


if __name__ == "__main__":
    points = make_clusters()
    compactness, labels, centers = run_kmeans(points, k=3)

    print("Points:", points.shape)
    print("Compactness:", round(float(compactness), 3))
    print("Cluster sizes:", [int((labels == i).sum()) for i in range(3)])
    print("Centers:\n", np.round(centers, 2))
