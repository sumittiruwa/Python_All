"""OpenCV Practice: Brightness/Contrast Adjustment"""

import cv2
import numpy as np


def make_sample_image(size=40):
    return np.full((size, size, 3), 100, dtype=np.uint8)


def adjust_brightness_contrast(image, alpha=1.0, beta=0):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


if __name__ == "__main__":
    image = make_sample_image()

    brighter = adjust_brightness_contrast(image, alpha=1.0, beta=50)
    darker = adjust_brightness_contrast(image, alpha=1.0, beta=-50)
    higher_contrast = adjust_brightness_contrast(image, alpha=1.5, beta=0)

    print("Original pixel:", image[0, 0].tolist())
    print("Brighter pixel:", brighter[0, 0].tolist())
    print("Darker pixel:", darker[0, 0].tolist())
    print("Higher contrast pixel:", higher_contrast[0, 0].tolist())
