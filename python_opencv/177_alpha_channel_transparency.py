"""OpenCV Practice: Build and Use a BGRA Image with Alpha Channel"""

import cv2
import numpy as np


def make_bgra_image(size=100):
    bgr = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.circle(bgr, (size // 2, size // 2), size // 3, (0, 165, 255), -1)

    alpha = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(alpha, (size // 2, size // 2), size // 3, 255, -1)

    bgra = cv2.merge([bgr[:, :, 0], bgr[:, :, 1], bgr[:, :, 2], alpha])
    return bgra


if __name__ == "__main__":
    bgra = make_bgra_image()
    b, g, r, a = cv2.split(bgra)

    print("BGRA shape:", bgra.shape)
    print("Opaque pixel count:", int((a == 255).sum()))
    print("Transparent pixel count:", int((a == 0).sum()))
    print("Mean alpha:", round(float(a.mean()), 2))
