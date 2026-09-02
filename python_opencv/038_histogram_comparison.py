"""OpenCV Practice: Histogram Comparison"""

import cv2
import numpy as np


def make_gray(size, seed):
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, (size, size), dtype=np.uint8)


def histogram(gray):
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    cv2.normalize(hist, hist)
    return hist


if __name__ == "__main__":
    similar_a = make_gray(50, seed=10)
    similar_b = make_gray(50, seed=10)
    different = make_gray(50, seed=99)

    hist_a = histogram(similar_a)
    hist_b = histogram(similar_b)
    hist_c = histogram(different)

    same_score = cv2.compareHist(hist_a, hist_b, cv2.HISTCMP_CORREL)
    diff_score = cv2.compareHist(hist_a, hist_c, cv2.HISTCMP_CORREL)

    print("Correlation of identical images:", round(float(same_score), 3))
    print("Correlation of different images:", round(float(diff_score), 3))
