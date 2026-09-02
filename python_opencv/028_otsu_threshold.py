"""OpenCV Practice: Otsu's Threshold"""

import cv2
import numpy as np


def make_bimodal_image(size=100, seed=0):
    rng = np.random.default_rng(seed)
    dark = rng.normal(50, 10, (size, size // 2)).clip(0, 255)
    bright = rng.normal(200, 10, (size, size // 2)).clip(0, 255)
    return np.concatenate([dark, bright], axis=1).astype(np.uint8)


def otsu_threshold(gray):
    value, result = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return value, result


if __name__ == "__main__":
    gray = make_bimodal_image()
    value, result = otsu_threshold(gray)

    print("Otsu computed threshold:", round(float(value), 2))
    print("White pixel ratio:", round(float(np.count_nonzero(result)) / result.size, 3))
