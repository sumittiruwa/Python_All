"""OpenCV Practice: Random Rotation Augmentation with Fixed Seed"""

import cv2
import numpy as np


def make_image(size=120):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (20, 40), (100, 80), (0, 200, 200), -1)
    return img


def random_rotate(img, rng, max_angle=30):
    angle = float(rng.uniform(-max_angle, max_angle))
    h, w = img.shape[:2]
    matrix = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1.0)
    rotated = cv2.warpAffine(img, matrix, (w, h))
    return rotated, angle


if __name__ == "__main__":
    img = make_image()
    rng = np.random.default_rng(7)

    for i in range(3):
        rotated, angle = random_rotate(img, rng)
        print(f"Rotation {i}: angle={round(angle, 2)}, mean={round(float(rotated.mean()), 2)}")
