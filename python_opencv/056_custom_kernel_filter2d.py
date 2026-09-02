"""OpenCV Practice: Custom Convolution Kernel via filter2D"""

import cv2
import numpy as np


def make_test_image(size=64):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (20, 20), (44, 44), (255, 255, 255), -1)
    return img


def sharpen(img):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
    return cv2.filter2D(img, -1, kernel)


def emboss(img):
    kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32)
    return cv2.filter2D(img, -1, kernel)


if __name__ == "__main__":
    image = make_test_image()
    sharpened = sharpen(image)
    embossed = emboss(image)

    print("Original mean:", round(float(image.mean()), 3))
    print("Sharpened mean:", round(float(sharpened.mean()), 3))
    print("Embossed mean:", round(float(embossed.mean()), 3))
    print("Sharpened shape:", sharpened.shape, "dtype:", sharpened.dtype)
