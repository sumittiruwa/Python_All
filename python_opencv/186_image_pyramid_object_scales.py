"""OpenCV Practice: Build an Image Pyramid to Simulate Multi-Scale Search"""

import cv2
import numpy as np


def make_image(size=256):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (80, 80), (176, 176), (0, 200, 0), -1)
    return img


def build_pyramid(img, levels=4):
    pyramid = [img]
    current = img
    for _ in range(levels - 1):
        current = cv2.pyrDown(current)
        pyramid.append(current)
    return pyramid


if __name__ == "__main__":
    img = make_image()
    pyramid = build_pyramid(img, levels=4)

    print("Original shape:", img.shape)
    for level, layer in enumerate(pyramid):
        print(f"Level {level}: shape={layer.shape}, mean={round(float(layer.mean()), 2)}")
