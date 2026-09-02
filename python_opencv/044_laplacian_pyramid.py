"""OpenCV Practice: Laplacian Pyramid"""

import cv2
import numpy as np


def make_sample_image(size=64):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(image, (10, 10), (54, 54), (0, 200, 200), -1)
    return image


def build_laplacian_pyramid(image, levels=3):
    gaussian = image.copy()
    gaussian_pyramid = [gaussian]
    for _ in range(levels):
        gaussian = cv2.pyrDown(gaussian)
        gaussian_pyramid.append(gaussian)

    laplacian_pyramid = []
    for i in range(levels):
        size = (gaussian_pyramid[i].shape[1], gaussian_pyramid[i].shape[0])
        expanded = cv2.pyrUp(gaussian_pyramid[i + 1], dstsize=size)
        laplacian = cv2.subtract(gaussian_pyramid[i], expanded)
        laplacian_pyramid.append(laplacian)

    return laplacian_pyramid


if __name__ == "__main__":
    image = make_sample_image()
    pyramid = build_laplacian_pyramid(image, levels=3)

    for i, level in enumerate(pyramid):
        print(f"laplacian level {i}: shape={level.shape}, mean={round(float(level.mean()), 2)}")
