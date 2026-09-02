"""OpenCV Practice: Image Rotate"""

import cv2
import numpy as np


def make_sample_image(size=100):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(image, (40, 10), (60, 30), (0, 255, 255), -1)
    return image


def rotate_image(image, angle, scale=1.0):
    h, w = image.shape[:2]
    center = (w / 2, h / 2)
    matrix = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, matrix, (w, h))


if __name__ == "__main__":
    image = make_sample_image()

    for angle in (45, 90, 180):
        rotated = rotate_image(image, angle)
        print(f"angle={angle}: shape={rotated.shape}, non-zero={int(np.count_nonzero(rotated))}")
