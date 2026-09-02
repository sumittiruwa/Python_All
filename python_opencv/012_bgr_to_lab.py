"""OpenCV Practice: BGR to LAB Conversion"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :] = (60, 180, 30)
    return image


def to_lab(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2LAB)


if __name__ == "__main__":
    image = make_sample_image()
    lab = to_lab(image)

    print("BGR pixel:", image[0, 0].tolist())
    print("LAB pixel:", lab[0, 0].tolist())
    print("L channel mean:", round(float(lab[:, :, 0].mean()), 2))
    print("A channel mean:", round(float(lab[:, :, 1].mean()), 2))
