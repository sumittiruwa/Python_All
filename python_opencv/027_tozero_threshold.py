"""OpenCV Practice: To-Zero Threshold"""

import cv2
import numpy as np


def make_gradient(size=100):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    return np.tile(row, (size, 1))


def tozero_threshold(gray, thresh=127):
    _, result = cv2.threshold(gray, thresh, 255, cv2.THRESH_TOZERO)
    return result


if __name__ == "__main__":
    gray = make_gradient()
    result = tozero_threshold(gray)

    print("Pixels below threshold set to zero:", bool(np.all(result[gray <= 127] == 0)))
    print("Pixels above threshold unchanged:", bool(np.array_equal(result[gray > 127], gray[gray > 127])))
    print("Result max:", int(result.max()))
