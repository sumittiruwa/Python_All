"""OpenCV Practice: Normalize Pixel Values to Zero Mean / Unit Variance"""

import cv2
import numpy as np


def make_image(size=100, seed=0):
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=(size, size, 3), dtype=np.uint8)


def standardize(img):
    img_f = img.astype(np.float32)
    mean = img_f.mean()
    std = img_f.std() or 1e-6
    return (img_f - mean) / std


def min_max_normalize(img):
    return cv2.normalize(img, None, 0.0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)


if __name__ == "__main__":
    img = make_image()
    standardized = standardize(img)
    normalized = min_max_normalize(img)

    print("Image shape:", img.shape)
    print("Standardized mean:", round(float(standardized.mean()), 5))
    print("Standardized std:", round(float(standardized.std()), 5))
    print("Min-max normalized range:", (round(float(normalized.min()), 3), round(float(normalized.max()), 3)))
