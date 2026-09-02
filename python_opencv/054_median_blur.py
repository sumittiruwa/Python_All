"""OpenCV Practice: Median Blur for Salt-and-Pepper Noise"""

import cv2
import numpy as np


def add_salt_and_pepper(img, amount=0.05, seed=2):
    rng = np.random.default_rng(seed)
    noisy = img.copy()
    mask = rng.random(img.shape[:2])
    noisy[mask < amount / 2] = 0
    noisy[mask > 1 - amount / 2] = 255
    return noisy


if __name__ == "__main__":
    base = np.full((64, 64, 3), 128, dtype=np.uint8)
    noisy = add_salt_and_pepper(base)
    cleaned = cv2.medianBlur(noisy, 5)

    salt_pepper_pixels = np.sum((noisy == 0) | (noisy == 255))
    cleaned_extreme_pixels = np.sum((cleaned == 0) | (cleaned == 255))

    print("Noisy extreme pixel count:", int(salt_pepper_pixels))
    print("Cleaned extreme pixel count:", int(cleaned_extreme_pixels))
    print("Noisy std:", round(float(noisy.std()), 3))
    print("Cleaned std:", round(float(cleaned.std()), 3))
