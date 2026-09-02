"""OpenCV Practice: Morphological Opening (Noise Removal)"""

import cv2
import numpy as np


def make_noisy_blob_image(size=64, seed=4):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (16, 16), (48, 48), 255, -1)
    rng = np.random.default_rng(seed)
    speckle_coords = rng.integers(0, size, size=(20, 2))
    for x, y in speckle_coords:
        img[y, x] = 255 if img[y, x] == 0 else img[y, x]
    for _ in range(15):
        x, y = rng.integers(0, size, size=2)
        img[y, x] = 255
    return img


def opening(img, ksize=3):
    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


if __name__ == "__main__":
    image = make_noisy_blob_image()
    opened = opening(image)

    print("Original white pixels:", int(np.count_nonzero(image)))
    print("Opened white pixels:", int(np.count_nonzero(opened)))
    print("Pixels removed:", int(np.count_nonzero(image) - np.count_nonzero(opened)))
