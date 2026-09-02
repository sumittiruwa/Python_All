"""OpenCV Practice: Morphological Gradient (Outline Extraction)"""

import cv2
import numpy as np


def make_blob_image(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (32, 32), 20, 255, -1)
    return img


def morphological_gradient(img, ksize=3):
    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


if __name__ == "__main__":
    image = make_blob_image()
    gradient = morphological_gradient(image)

    print("Filled blob pixels:", int(np.count_nonzero(image)))
    print("Gradient (outline) pixels:", int(np.count_nonzero(gradient)))
    print("Outline ratio:", round(float(np.count_nonzero(gradient) / np.count_nonzero(image)), 4))
