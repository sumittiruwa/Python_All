"""OpenCV Practice: Sobel X Gradient"""

import cv2
import numpy as np


def make_vertical_edge_image(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    img[:, size // 2 :] = 255
    return img


def sobel_x(img, ksize=3):
    return cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=ksize)


if __name__ == "__main__":
    image = make_vertical_edge_image()
    grad_x = sobel_x(image)

    print("Image shape:", image.shape)
    print("Gradient dtype:", grad_x.dtype)
    print("Max abs gradient:", round(float(np.abs(grad_x).max()), 3))
    print("Nonzero gradient columns:", int(np.count_nonzero(np.abs(grad_x).sum(axis=0))))
