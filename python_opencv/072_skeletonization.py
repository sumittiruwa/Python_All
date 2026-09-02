"""OpenCV Practice: Iterative Morphological Skeletonization"""

import cv2
import numpy as np


def make_thick_shape(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (16, 16), (48, 48), 255, -1)
    return img


def skeletonize(img):
    img = img.copy()
    skeleton = np.zeros(img.shape, dtype=np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    while True:
        eroded = cv2.erode(img, kernel)
        opened = cv2.dilate(eroded, kernel)
        temp = cv2.subtract(img, opened)
        skeleton = cv2.bitwise_or(skeleton, temp)
        img = eroded
        if cv2.countNonZero(img) == 0:
            break

    return skeleton


if __name__ == "__main__":
    image = make_thick_shape()
    skeleton = skeletonize(image)

    print("Original white pixels:", int(np.count_nonzero(image)))
    print("Skeleton white pixels:", int(np.count_nonzero(skeleton)))
    print("Skeleton reduction ratio:", round(float(np.count_nonzero(skeleton) / np.count_nonzero(image)), 4))
