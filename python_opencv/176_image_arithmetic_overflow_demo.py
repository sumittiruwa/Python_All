"""OpenCV Practice: Saturated vs Wraparound Arithmetic"""

import cv2
import numpy as np


def make_bright_image(size=10, value=200):
    return np.full((size, size), value, dtype=np.uint8)


def saturated_add(img, delta):
    return cv2.add(img, np.full(img.shape, delta, dtype=np.uint8))


def wraparound_add(img, delta):
    return img + np.uint8(delta)


if __name__ == "__main__":
    img = make_bright_image(value=200)
    delta = 100

    saturated = saturated_add(img, delta)
    wrapped = wraparound_add(img, delta)

    print("Base value:", int(img[0, 0]), "+ delta:", delta)
    print("cv2.add (saturated) result:", int(saturated[0, 0]))
    print("numpy + (wraparound) result:", int(wrapped[0, 0]))
