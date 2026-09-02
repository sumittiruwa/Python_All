"""OpenCV Practice: Image Divide"""

import cv2
import numpy as np


def make_images(size=40):
    a = np.full((size, size, 3), 200, dtype=np.uint8)
    b = np.full((size, size, 3), 4, dtype=np.uint8)
    return a, b


if __name__ == "__main__":
    a, b = make_images()

    result = cv2.divide(a, b)

    print("a pixel:", a[0, 0].tolist())
    print("b pixel:", b[0, 0].tolist())
    print("a / b pixel:", result[0, 0].tolist())
    print("result dtype:", result.dtype)
