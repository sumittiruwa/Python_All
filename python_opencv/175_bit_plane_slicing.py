"""OpenCV Practice: Bit-Plane Slicing of a Grayscale Image"""

import cv2
import numpy as np


def make_pattern(size=64, seed=0):
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=(size, size), dtype=np.uint8)


def extract_bit_plane(img, bit):
    return ((img >> bit) & 1) * 255


if __name__ == "__main__":
    img = make_pattern()

    print("Image shape:", img.shape)
    for bit in range(8):
        plane = extract_bit_plane(img, bit)
        on_ratio = round(float((plane > 0).mean()), 3)
        print(f"Bit {bit}: fraction on = {on_ratio}")
