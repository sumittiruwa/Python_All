"""OpenCV Practice: Image Multiply"""

import cv2
import numpy as np


def make_images(size=40):
    a = np.full((size, size, 3), 100, dtype=np.uint8)
    mask = np.zeros((size, size, 3), dtype=np.float64)
    mask[:, :20] = 1.0
    return a, mask


if __name__ == "__main__":
    a, mask = make_images()

    result = cv2.multiply(a.astype(np.float64), mask)

    print("Left half pixel:", result[0, 0].tolist())
    print("Right half pixel:", result[0, 30].tolist())
    print("Result dtype:", result.dtype)
