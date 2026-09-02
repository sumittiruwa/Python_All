"""OpenCV Practice: Image Translation"""

import cv2
import numpy as np


def make_sample_image(size=80):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(image, (10, 10), (30, 30), (255, 0, 0), -1)
    return image


def translate_image(image, dx, dy):
    h, w = image.shape[:2]
    matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    return cv2.warpAffine(image, matrix, (w, h))


if __name__ == "__main__":
    image = make_sample_image()
    shifted = translate_image(image, 20, 15)

    print("Original non-zero pixel count:", int(np.count_nonzero(image)))
    print("Shifted non-zero pixel count:", int(np.count_nonzero(shifted)))
    print("Original pixel at (20,20):", image[20, 20].tolist())
    print("Shifted pixel at (35,40):", shifted[35, 40].tolist())
