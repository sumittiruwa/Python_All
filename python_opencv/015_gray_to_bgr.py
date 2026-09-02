"""OpenCV Practice: Grayscale to BGR"""

import cv2
import numpy as np


def make_sample_gray(size=60):
    gray = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(gray, (30, 30), 15, 200, -1)
    return gray


def gray_to_bgr(gray):
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


if __name__ == "__main__":
    gray = make_sample_gray()
    bgr = gray_to_bgr(gray)

    print("Gray shape:", gray.shape)
    print("BGR shape:", bgr.shape)
    print("Gray pixel at center:", int(gray[30, 30]))
    print("BGR pixel at center:", bgr[30, 30].tolist())
