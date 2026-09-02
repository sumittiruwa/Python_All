"""OpenCV Practice: PCA Compute on Synthetic 2D Points"""

import cv2
import numpy as np


def make_elongated_cloud(n=200, seed=0):
    rng = np.random.default_rng(seed)
    t = rng.normal(0, 5, size=n)
    noise = rng.normal(0, 0.5, size=n)
    x = t
    y = 0.5 * t + noise
    pts = np.stack([x, y], axis=1).astype(np.float32)
    return pts


def pca_axes(points):
    mean, eigenvectors, eigenvalues = cv2.PCACompute2(points, mean=None)
    return mean, eigenvectors, eigenvalues


if __name__ == "__main__":
    points = make_elongated_cloud()
    mean, eigenvectors, eigenvalues = pca_axes(points)

    print("Point cloud shape:", points.shape)
    print("Mean:", np.round(mean.ravel(), 3))
    print("Principal axis 1:", np.round(eigenvectors[0], 3))
    print("Principal axis 2:", np.round(eigenvectors[1], 3))
    print("Eigenvalues:", np.round(eigenvalues.ravel(), 3))
