"""OpenCV Practice: Truncate Threshold"""

import cv2
import numpy as np


def make_gradient(size=100):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    return np.tile(row, (size, 1))


def trunc_threshold(gray, thresh=127):
    _, result = cv2.threshold(gray, thresh, 255, cv2.THRESH_TRUNC)
    return result


if __name__ == "__main__":
    gray = make_gradient()
    result = trunc_threshold(gray)

    print("Gray max:", int(gray.max()))
    print("Truncated max:", int(result.max()))
    print("Unique values above threshold:", sorted(np.unique(result[gray > 127]).tolist())[:3])
