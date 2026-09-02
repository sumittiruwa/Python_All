"""OpenCV Practice: Adaptive Mean Threshold"""

import cv2
import numpy as np


def make_gradient_image(size=100):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    return np.tile(row, (size, 1))


def adaptive_mean_threshold(gray, block_size=11, c=2):
    return cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c
    )


if __name__ == "__main__":
    gray = make_gradient_image()
    result = adaptive_mean_threshold(gray)

    print("Gray shape:", gray.shape)
    print("Result unique values:", sorted(np.unique(result).tolist()))
    print("White pixel ratio:", round(float(np.count_nonzero(result)) / result.size, 3))
