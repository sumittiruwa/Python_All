"""OpenCV Practice: Reduce Bit Depth / Intensity Levels"""

import cv2
import numpy as np


def make_gradient(size=100):
    row = np.linspace(0, 255, size, dtype=np.uint8)
    return np.tile(row, (size, 1))


def quantize(img, levels=4):
    step = 256 // levels
    quantized = (img // step) * step + step // 2
    return np.clip(quantized, 0, 255).astype(np.uint8)


if __name__ == "__main__":
    img = make_gradient()

    for levels in (2, 4, 8):
        result = quantize(img, levels)
        unique_values = np.unique(result)
        print(f"Levels={levels}: unique intensities={len(unique_values)} values={unique_values.tolist()}")
