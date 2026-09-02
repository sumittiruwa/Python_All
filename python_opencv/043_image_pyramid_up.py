"""OpenCV Practice: Image Pyramid Up"""

import cv2
import numpy as np


def make_sample_image(size=16):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.circle(image, (size // 2, size // 2), size // 4, (255, 0, 0), -1)
    return image


def pyramid_up_levels(image, levels=3):
    results = [image]
    current = image
    for _ in range(levels):
        current = cv2.pyrUp(current)
        results.append(current)
    return results


if __name__ == "__main__":
    image = make_sample_image()
    levels = pyramid_up_levels(image, levels=3)

    for i, level in enumerate(levels):
        print(f"level {i}: shape={level.shape}")
