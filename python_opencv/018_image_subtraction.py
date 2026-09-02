"""OpenCV Practice: Image Subtraction"""

import cv2
import numpy as np


def make_images(size=40):
    a = np.full((size, size, 3), 60, dtype=np.uint8)
    b = np.full((size, size, 3), 100, dtype=np.uint8)
    return a, b


if __name__ == "__main__":
    a, b = make_images()

    diff_ab = cv2.subtract(a, b)
    diff_ba = cv2.subtract(b, a)

    print("a - b pixel (clamped to 0):", diff_ab[0, 0].tolist())
    print("b - a pixel:", diff_ba[0, 0].tolist())
    print("a - b max value:", int(diff_ab.max()))
