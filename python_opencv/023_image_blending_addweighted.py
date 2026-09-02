"""OpenCV Practice: Image Blending with addWeighted"""

import cv2
import numpy as np


def make_images(size=50):
    a = np.full((size, size, 3), (255, 0, 0), dtype=np.uint8)
    b = np.full((size, size, 3), (0, 0, 255), dtype=np.uint8)
    return a, b


def blend(image_a, image_b, alpha):
    return cv2.addWeighted(image_a, alpha, image_b, 1 - alpha, 0)


if __name__ == "__main__":
    a, b = make_images()

    for alpha in (0.0, 0.25, 0.5, 0.75, 1.0):
        blended = blend(a, b, alpha)
        print(f"alpha={alpha}: pixel={blended[0, 0].tolist()}")
