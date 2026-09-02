"""OpenCV Practice: cv2.LUT Custom Tone Curve"""

import cv2
import numpy as np


def make_gradient_image(size=100):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    img = np.tile(row, (size, 1))
    return cv2.merge([img, img, img])


def build_gamma_lut(gamma=2.2):
    x = np.arange(256, dtype=np.float32) / 255.0
    lut = np.clip((x ** (1.0 / gamma)) * 255.0, 0, 255).astype(np.uint8)
    return lut


if __name__ == "__main__":
    img = make_gradient_image()
    lut = build_gamma_lut(gamma=2.2)
    result = cv2.LUT(img, lut)

    print("Image shape:", img.shape)
    print("LUT sample [0, 64, 128, 192, 255]:", lut[[0, 64, 128, 192, 255]].tolist())
    print("Original mean:", round(float(img.mean()), 2))
    print("Tone-mapped mean:", round(float(result.mean()), 2))
