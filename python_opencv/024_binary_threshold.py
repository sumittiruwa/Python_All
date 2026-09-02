"""OpenCV Practice: Binary Threshold"""

import cv2
import numpy as np


def make_gradient(size=100):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    return np.tile(row, (size, 1))


def binary_threshold(gray, thresh=127):
    _, result = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    return result


if __name__ == "__main__":
    gray = make_gradient()
    result = binary_threshold(gray)

    print("Gray shape:", gray.shape)
    print("Unique values in result:", sorted(np.unique(result).tolist()))
    print("White pixel ratio:", round(float(np.count_nonzero(result)) / result.size, 3))
