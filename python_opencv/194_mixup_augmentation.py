"""OpenCV Practice: Mixup Blend of Two Synthetic Images"""

import cv2
import numpy as np


def make_image_a(size=80):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (0, 0), (size, size), (200, 0, 0), -1)
    return img


def make_image_b(size=80):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (0, 0), (size, size), (0, 0, 200), -1)
    return img


def mixup(img_a, img_b, lam):
    blended = cv2.addWeighted(img_a, lam, img_b, 1 - lam, 0)
    return blended


if __name__ == "__main__":
    a = make_image_a()
    b = make_image_b()

    for lam in (0.9, 0.5, 0.1):
        mixed = mixup(a, b, lam)
        print(f"lambda={lam}: pixel={mixed[0, 0].tolist()}, mean={round(float(mixed.mean()), 2)}")
