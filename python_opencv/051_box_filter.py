"""OpenCV Practice: Box Filter Averaging"""

import cv2
import numpy as np


def make_noisy_image(size=64, seed=0):
    rng = np.random.default_rng(seed)
    img = np.full((size, size, 3), 120, dtype=np.uint8)
    noise = rng.integers(-40, 40, img.shape, dtype=np.int16)
    return np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)


def apply_box_filter(img, ksize=5, normalize=True):
    return cv2.boxFilter(img, -1, (ksize, ksize), normalize=normalize)


if __name__ == "__main__":
    image = make_noisy_image()
    smoothed = apply_box_filter(image, ksize=5)

    print("Input shape:", image.shape)
    print("Input std:", round(float(image.std()), 3))
    print("Box-filtered std:", round(float(smoothed.std()), 3))
    print("Mean before:", round(float(image.mean()), 3), "after:", round(float(smoothed.mean()), 3))
