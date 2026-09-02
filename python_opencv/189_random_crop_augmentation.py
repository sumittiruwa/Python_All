"""OpenCV Practice: Random Crop Augmentation with Fixed Seed"""

import cv2
import numpy as np


def make_image(size=150):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (0, 0), (size, size // 2), (255, 0, 0), -1)
    cv2.rectangle(img, (0, size // 2), (size, size), (0, 0, 255), -1)
    return img


def random_crop(img, crop_h, crop_w, rng):
    h, w = img.shape[:2]
    y0 = int(rng.integers(0, h - crop_h + 1))
    x0 = int(rng.integers(0, w - crop_w + 1))
    return img[y0:y0 + crop_h, x0:x0 + crop_w], (x0, y0)


if __name__ == "__main__":
    img = make_image()
    rng = np.random.default_rng(42)

    for i in range(3):
        crop, origin = random_crop(img, 60, 60, rng)
        print(f"Crop {i}: origin={origin}, shape={crop.shape}, mean={round(float(crop.mean()), 2)}")
