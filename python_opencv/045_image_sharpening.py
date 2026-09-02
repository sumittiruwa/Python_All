"""OpenCV Practice: Image Sharpening via Kernel Filter"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(image, (15, 15), (45, 45), (100, 150, 200), -1)
    return cv2.GaussianBlur(image, (5, 5), 0)


def sharpen(image):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ])
    return cv2.filter2D(image, -1, kernel)


if __name__ == "__main__":
    image = make_sample_image()
    sharpened = sharpen(image)

    print("Original std:", round(float(image.std()), 2))
    print("Sharpened std:", round(float(sharpened.std()), 2))
    print("Shapes match:", image.shape == sharpened.shape)
