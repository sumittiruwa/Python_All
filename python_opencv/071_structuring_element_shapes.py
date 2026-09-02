"""OpenCV Practice: Comparing Structuring Element Shapes"""

import cv2
import numpy as np


def make_plus_shaped_kernel_input(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (28, 10), (36, 54), 255, -1)
    cv2.rectangle(img, (10, 28), (54, 36), 255, -1)
    return img


def get_kernels(ksize=7):
    return {
        "rect": cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize)),
        "ellipse": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize)),
        "cross": cv2.getStructuringElement(cv2.MORPH_CROSS, (ksize, ksize)),
    }


if __name__ == "__main__":
    image = make_plus_shaped_kernel_input()
    kernels = get_kernels()

    for name, kernel in kernels.items():
        dilated = cv2.dilate(image, kernel)
        print(f"{name}: kernel_ones={int(kernel.sum())}, dilated_white={int(np.count_nonzero(dilated))}")
