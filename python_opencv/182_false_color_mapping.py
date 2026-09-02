"""OpenCV Practice: Map Grayscale to a Custom False-Color Palette"""

import cv2
import numpy as np


def make_gradient(size=64):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    return np.tile(row, (size, 1))


def build_custom_palette():
    lut = np.zeros((256, 1, 3), dtype=np.uint8)
    for i in range(256):
        t = i / 255.0
        lut[i, 0] = (int(255 * (1 - t)), int(255 * abs(0.5 - t) * 2), int(255 * t))
    return lut


def apply_false_color(gray_img, lut):
    bgr = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
    return cv2.LUT(bgr, lut)


if __name__ == "__main__":
    gray = make_gradient()
    palette = build_custom_palette()
    colored = apply_false_color(gray, palette)

    print("Gray image shape:", gray.shape)
    print("Colored image shape:", colored.shape)
    print("Low-intensity pixel color:", colored[0, 0].tolist())
    print("High-intensity pixel color:", colored[0, -1].tolist())
