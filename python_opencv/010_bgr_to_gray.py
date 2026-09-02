"""OpenCV Practice: BGR to Gray Conversion"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :, 2] = 200
    cv2.circle(image, (30, 30), 15, (0, 255, 0), -1)
    return image


def to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


if __name__ == "__main__":
    image = make_sample_image()
    gray = to_gray(image)

    print("Color shape:", image.shape)
    print("Gray shape:", gray.shape)
    print("Gray dtype:", gray.dtype)
    print("Gray mean:", round(float(gray.mean()), 2))
