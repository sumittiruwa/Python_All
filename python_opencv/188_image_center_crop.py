"""OpenCV Practice: Crop the Center Region to a Target Size"""

import cv2
import numpy as np


def make_image(size=200):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.circle(img, (size // 2, size // 2), size // 4, (0, 255, 255), -1)
    return img


def center_crop(img, target_h, target_w):
    h, w = img.shape[:2]
    y0 = (h - target_h) // 2
    x0 = (w - target_w) // 2
    return img[y0:y0 + target_h, x0:x0 + target_w]


if __name__ == "__main__":
    img = make_image()
    cropped = center_crop(img, 80, 80)

    print("Original shape:", img.shape)
    print("Cropped shape:", cropped.shape)
    print("Cropped center pixel:", cropped[40, 40].tolist())
    print("Cropped mean pixel value:", round(float(cropped.mean()), 2))
