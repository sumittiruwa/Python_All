"""OpenCV Practice: Image Flip"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(image, (0, 0), (20, 20), (255, 255, 255), -1)
    return image


def flip_image(image, mode):
    return cv2.flip(image, mode)


if __name__ == "__main__":
    image = make_sample_image()
    horizontal = flip_image(image, 1)
    vertical = flip_image(image, 0)
    both = flip_image(image, -1)

    print("Original top-left pixel:", image[5, 5].tolist())
    print("Horizontal flip top-right pixel:", horizontal[5, 54].tolist())
    print("Vertical flip bottom-left pixel:", vertical[54, 5].tolist())
    print("Both flip bottom-right pixel:", both[54, 54].tolist())
