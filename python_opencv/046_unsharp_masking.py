"""OpenCV Practice: Unsharp Masking"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.circle(image, (30, 30), 20, (0, 180, 255), -1)
    return image


def unsharp_mask(image, sigma=2.0, amount=1.5):
    blurred = cv2.GaussianBlur(image, (0, 0), sigma)
    sharpened = cv2.addWeighted(image, 1 + amount, blurred, -amount, 0)
    return sharpened


if __name__ == "__main__":
    image = make_sample_image()
    result = unsharp_mask(image)

    print("Original mean:", round(float(image.mean()), 2))
    print("Unsharp result mean:", round(float(result.mean()), 2))
    print("Original std:", round(float(image.std()), 2))
    print("Unsharp result std:", round(float(result.std()), 2))
