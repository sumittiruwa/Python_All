"""OpenCV Practice: Gamma Correction via Lookup Table"""

import cv2
import numpy as np


def build_gamma_lut(gamma):
    table = np.array([((i / 255.0) ** (1.0 / gamma)) * 255 for i in range(256)], dtype=np.uint8)
    return table


def apply_gamma(image, gamma):
    lut = build_gamma_lut(gamma)
    return cv2.LUT(image, lut)


if __name__ == "__main__":
    image = np.full((50, 50, 3), 100, dtype=np.uint8)

    bright = apply_gamma(image, 2.0)
    dark = apply_gamma(image, 0.5)

    print("Original pixel:", image[0, 0].tolist())
    print("Gamma 2.0 (brighter) pixel:", bright[0, 0].tolist())
    print("Gamma 0.5 (darker) pixel:", dark[0, 0].tolist())
