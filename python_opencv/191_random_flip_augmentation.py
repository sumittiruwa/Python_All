"""OpenCV Practice: Random Flip Augmentation with Fixed Seed"""

import cv2
import numpy as np


def make_image(size=100):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (40, 40), (255, 255, 255), -1)
    return img


def random_flip(img, rng):
    choice = int(rng.integers(0, 3))
    flip_code = {0: 1, 1: 0, 2: -1}[choice]
    label = {0: "horizontal", 1: "vertical", 2: "both"}[choice]
    return cv2.flip(img, flip_code), label


if __name__ == "__main__":
    img = make_image()
    rng = np.random.default_rng(3)

    for i in range(4):
        flipped, label = random_flip(img, rng)
        corner = flipped[5, 5].tolist()
        print(f"Flip {i}: type={label}, top-left corner pixel={corner}")
