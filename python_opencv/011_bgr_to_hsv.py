"""OpenCV Practice: BGR to HSV Conversion"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :] = (0, 0, 255)
    return image


def to_hsv(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


if __name__ == "__main__":
    image = make_sample_image()
    hsv = to_hsv(image)

    print("BGR pixel:", image[0, 0].tolist())
    print("HSV pixel:", hsv[0, 0].tolist())
    print("HSV shape:", hsv.shape)
    print("Hue channel mean:", round(float(hsv[:, :, 0].mean()), 2))
