"""OpenCV Practice: Adaptive Gaussian Threshold"""

import cv2
import numpy as np


def make_gradient_image(size=100):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    return np.tile(row, (size, 1))


def adaptive_gaussian_threshold(gray, block_size=11, c=2):
    return cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, c
    )


if __name__ == "__main__":
    gray = make_gradient_image()
    mean_result = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )
    gaussian_result = adaptive_gaussian_threshold(gray)

    print("Mean white ratio:", round(float(np.count_nonzero(mean_result)) / mean_result.size, 3))
    print("Gaussian white ratio:", round(float(np.count_nonzero(gaussian_result)) / gaussian_result.size, 3))
    print("Results differ:", bool(not np.array_equal(mean_result, gaussian_result)))
