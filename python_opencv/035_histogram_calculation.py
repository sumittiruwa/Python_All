"""OpenCV Practice: Histogram Calculation"""

import cv2
import numpy as np


def make_sample_gray(size=64, seed=1):
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, (size, size), dtype=np.uint8)


def calc_histogram(gray, bins=256):
    return cv2.calcHist([gray], [0], None, [bins], [0, 256])


if __name__ == "__main__":
    gray = make_sample_gray()
    hist = calc_histogram(gray)

    print("Histogram shape:", hist.shape)
    print("Total pixel count from hist:", int(hist.sum()))
    print("Image size:", gray.size)
    print("Most common bin:", int(hist.argmax()))
