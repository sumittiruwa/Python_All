"""OpenCV Practice: Gaussian Blur"""

import cv2
import numpy as np


def make_noisy_image(size=64, seed=1):
    rng = np.random.default_rng(seed)
    img = np.full((size, size, 3), 100, dtype=np.uint8)
    noise = rng.integers(-50, 50, img.shape, dtype=np.int16)
    return np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)


def gaussian_blur(img, ksize=5, sigma=0):
    return cv2.GaussianBlur(img, (ksize, ksize), sigma)


if __name__ == "__main__":
    image = make_noisy_image()

    for k in (3, 7, 11):
        blurred = gaussian_blur(image, ksize=k)
        print(f"ksize={k}: std={round(float(blurred.std()), 3)}")

    print("Original std:", round(float(image.std()), 3))
