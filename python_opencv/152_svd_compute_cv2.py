"""OpenCV Practice: SVD Decompose a Small Matrix"""

import cv2
import numpy as np


def decompose(matrix):
    w, u, vt = cv2.SVDecomp(matrix)
    return w, u, vt


def reconstruct(w, u, vt):
    return u @ np.diagflat(w) @ vt


if __name__ == "__main__":
    A = np.array([[3, 1, 1], [-1, 3, 1]], dtype=np.float32)

    singular_values, u, vt = decompose(A)
    rebuilt = reconstruct(singular_values.ravel(), u, vt)

    print("Matrix A:\n", A)
    print("Singular values:", np.round(singular_values.ravel(), 3))
    print("U shape:", u.shape, "Vt shape:", vt.shape)
    print("Reconstruction error:", round(float(np.abs(A - rebuilt).max()), 5))
