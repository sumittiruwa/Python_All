"""OpenCV Practice: Histogram Equalization"""

import cv2
import numpy as np


def make_low_contrast_gray(size=80, seed=2):
    rng = np.random.default_rng(seed)
    return rng.integers(100, 150, (size, size), dtype=np.uint8)


def equalize(gray):
    return cv2.equalizeHist(gray)


if __name__ == "__main__":
    gray = make_low_contrast_gray()
    equalized = equalize(gray)

    print("Original std:", round(float(gray.std()), 2))
    print("Equalized std:", round(float(equalized.std()), 2))
    print("Original range:", int(gray.min()), "-", int(gray.max()))
    print("Equalized range:", int(equalized.min()), "-", int(equalized.max()))
