"""OpenCV Practice: Random Brightness Jitter with Fixed Seed"""

import cv2
import numpy as np


def make_image(size=80, value=120):
    return np.full((size, size, 3), value, dtype=np.uint8)


def random_brightness(img, rng, low=-40, high=40):
    delta = int(rng.integers(low, high + 1))
    if delta >= 0:
        return cv2.add(img, np.full(img.shape, delta, dtype=np.uint8)), delta
    return cv2.subtract(img, np.full(img.shape, -delta, dtype=np.uint8)), delta


if __name__ == "__main__":
    img = make_image()
    rng = np.random.default_rng(11)

    print("Base pixel value:", int(img[0, 0, 0]))
    for i in range(4):
        adjusted, delta = random_brightness(img, rng)
        print(f"Sample {i}: delta={delta}, resulting pixel={int(adjusted[0, 0, 0])}")
