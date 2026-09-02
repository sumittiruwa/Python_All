"""OpenCV Practice: Sobel Y Gradient"""

import cv2
import numpy as np


def make_horizontal_edge_image(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    img[size // 2 :, :] = 255
    return img


def sobel_y(img, ksize=3):
    return cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=ksize)


if __name__ == "__main__":
    image = make_horizontal_edge_image()
    grad_y = sobel_y(image)

    print("Image shape:", image.shape)
    print("Gradient dtype:", grad_y.dtype)
    print("Max abs gradient:", round(float(np.abs(grad_y).max()), 3))
    print("Nonzero gradient rows:", int(np.count_nonzero(np.abs(grad_y).sum(axis=1))))
