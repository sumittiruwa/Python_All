"""OpenCV Practice: Average Blur"""

import cv2
import numpy as np


def make_shapes_image(size=64):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (30, 30), (255, 255, 255), -1)
    cv2.circle(img, (45, 45), 10, (0, 255, 0), -1)
    return img


def average_blur(img, ksize=5):
    return cv2.blur(img, (ksize, ksize))


if __name__ == "__main__":
    image = make_shapes_image()
    blurred = average_blur(image, ksize=7)

    print("Input shape:", image.shape)
    print("Unique input colors:", len(np.unique(image.reshape(-1, 3), axis=0)))
    print("Unique blurred colors:", len(np.unique(blurred.reshape(-1, 3), axis=0)))
    print("Blurred mean:", round(float(blurred.mean()), 3))
