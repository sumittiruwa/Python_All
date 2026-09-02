"""OpenCV Practice: Bilateral Filter Edge-Preserving Smoothing"""

import cv2
import numpy as np


def make_stepped_image(size=64, seed=3):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    img[:, : size // 2] = 60
    img[:, size // 2 :] = 200
    rng = np.random.default_rng(seed)
    noise = rng.integers(-15, 15, img.shape, dtype=np.int16)
    return np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)


def bilateral_smooth(img, d=9, sigma_color=75, sigma_space=75):
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)


if __name__ == "__main__":
    image = make_stepped_image()
    smoothed = bilateral_smooth(image)

    edge_col = 32
    edge_diff_before = abs(int(image[32, edge_col - 1, 0]) - int(image[32, edge_col + 1, 0]))
    edge_diff_after = abs(int(smoothed[32, edge_col - 1, 0]) - int(smoothed[32, edge_col + 1, 0]))

    print("Std before:", round(float(image.std()), 3))
    print("Std after:", round(float(smoothed.std()), 3))
    print("Edge contrast before:", edge_diff_before, "after:", edge_diff_after)
