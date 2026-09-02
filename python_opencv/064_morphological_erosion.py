"""OpenCV Practice: Morphological Erosion"""

import cv2
import numpy as np


def make_blob_image(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (16, 16), (48, 48), 255, -1)
    return img


def erode(img, ksize=5, iterations=1):
    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    return cv2.erode(img, kernel, iterations=iterations)


if __name__ == "__main__":
    image = make_blob_image()
    eroded_once = erode(image, iterations=1)
    eroded_thrice = erode(image, iterations=3)

    print("Original white pixels:", int(np.count_nonzero(image)))
    print("Eroded (1 iter) white pixels:", int(np.count_nonzero(eroded_once)))
    print("Eroded (3 iter) white pixels:", int(np.count_nonzero(eroded_thrice)))
