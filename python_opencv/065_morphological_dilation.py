"""OpenCV Practice: Morphological Dilation"""

import cv2
import numpy as np


def make_blob_image(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (26, 26), (38, 38), 255, -1)
    return img


def dilate(img, ksize=5, iterations=1):
    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    return cv2.dilate(img, kernel, iterations=iterations)


if __name__ == "__main__":
    image = make_blob_image()
    dilated_once = dilate(image, iterations=1)
    dilated_thrice = dilate(image, iterations=3)

    print("Original white pixels:", int(np.count_nonzero(image)))
    print("Dilated (1 iter) white pixels:", int(np.count_nonzero(dilated_once)))
    print("Dilated (3 iter) white pixels:", int(np.count_nonzero(dilated_thrice)))
