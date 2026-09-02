"""OpenCV Practice: Image Addition"""

import cv2
import numpy as np


def make_images(size=40):
    a = np.full((size, size, 3), 200, dtype=np.uint8)
    b = np.full((size, size, 3), 100, dtype=np.uint8)
    return a, b


if __name__ == "__main__":
    a, b = make_images()

    cv_sum = cv2.add(a, b)
    np_sum = a.astype(np.int32) + b.astype(np.int32)

    print("cv2.add pixel (saturated):", cv_sum[0, 0].tolist())
    print("numpy raw sum pixel:", np_sum[0, 0].tolist())
    print("cv2.add max value:", int(cv_sum.max()))
