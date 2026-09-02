"""OpenCV Practice: Inverse Binary Threshold"""

import cv2
import numpy as np


def make_gradient(size=100):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    return np.tile(row, (size, 1))


def inverse_binary_threshold(gray, thresh=127):
    _, result = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY_INV)
    return result


if __name__ == "__main__":
    gray = make_gradient()
    normal = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    inverse = inverse_binary_threshold(gray)

    print("Normal white ratio:", round(float(np.count_nonzero(normal)) / normal.size, 3))
    print("Inverse white ratio:", round(float(np.count_nonzero(inverse)) / inverse.size, 3))
    print("Sum equals total:", bool(np.array_equal(normal + inverse, np.full_like(normal, 255))))
