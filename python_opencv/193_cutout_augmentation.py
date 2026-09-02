"""OpenCV Practice: Cutout / Random Erasing Augmentation"""

import cv2
import numpy as np


def make_image(size=100):
    img = np.full((size, size, 3), (0, 150, 0), dtype=np.uint8)
    return img


def cutout(img, rng, patch_size=25, fill=0):
    h, w = img.shape[:2]
    y0 = int(rng.integers(0, h - patch_size + 1))
    x0 = int(rng.integers(0, w - patch_size + 1))
    result = img.copy()
    result[y0:y0 + patch_size, x0:x0 + patch_size] = fill
    return result, (x0, y0, patch_size, patch_size)


if __name__ == "__main__":
    img = make_image()
    rng = np.random.default_rng(5)

    erased, box = cutout(img, rng)
    print("Image shape:", img.shape)
    print("Cutout box (x, y, w, h):", box)
    print("Original mean:", round(float(img.mean()), 2))
    print("After cutout mean:", round(float(erased.mean()), 2))
    print("Erased pixels count:", int(np.all(erased == 0, axis=2).sum()))
