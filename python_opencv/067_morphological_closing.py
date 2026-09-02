"""OpenCV Practice: Morphological Closing (Hole Filling)"""

import cv2
import numpy as np


def make_blob_with_holes(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (14, 14), (50, 50), 255, -1)
    cv2.rectangle(img, (20, 20), (24, 24), 0, -1)
    cv2.rectangle(img, (35, 35), (39, 39), 0, -1)
    return img


def closing(img, ksize=9):
    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


if __name__ == "__main__":
    image = make_blob_with_holes()
    closed = closing(image)

    print("Original white pixels:", int(np.count_nonzero(image)))
    print("Closed white pixels:", int(np.count_nonzero(closed)))
    print("Holes filled (pixel delta):", int(np.count_nonzero(closed) - np.count_nonzero(image)))
