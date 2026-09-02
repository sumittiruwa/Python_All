"""OpenCV Practice: Image Shear"""

import cv2
import numpy as np


def make_sample_image(size=100):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(image, (30, 30), (70, 70), (0, 200, 0), -1)
    return image


def shear_image(image, shear_x=0.0, shear_y=0.0):
    h, w = image.shape[:2]
    matrix = np.float32([[1, shear_x, 0], [shear_y, 1, 0]])
    new_w = int(w + abs(shear_x) * h)
    new_h = int(h + abs(shear_y) * w)
    return cv2.warpAffine(image, matrix, (new_w, new_h))


if __name__ == "__main__":
    image = make_sample_image()
    sheared = shear_image(image, shear_x=0.3)

    print("Original shape:", image.shape)
    print("Sheared shape:", sheared.shape)
    print("Sheared non-zero pixels:", int(np.count_nonzero(sheared)))
