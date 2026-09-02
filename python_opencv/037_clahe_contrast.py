"""OpenCV Practice: CLAHE Adaptive Histogram Equalization"""

import cv2
import numpy as np


def make_low_contrast_gray(size=80, seed=3):
    rng = np.random.default_rng(seed)
    return rng.integers(100, 150, (size, size), dtype=np.uint8)


def apply_clahe(gray, clip_limit=2.0, tile_size=(8, 8)):
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_size)
    return clahe.apply(gray)


if __name__ == "__main__":
    gray = make_low_contrast_gray()
    result = apply_clahe(gray)

    print("Original std:", round(float(gray.std()), 2))
    print("CLAHE result std:", round(float(result.std()), 2))
    print("Result shape:", result.shape)
