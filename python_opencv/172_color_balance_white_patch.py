"""OpenCV Practice: White-Patch Color Balancing"""

import cv2
import numpy as np


def make_tinted_image(size=100):
    base = np.full((size, size, 3), (100, 140, 180), dtype=np.uint8)
    cv2.rectangle(base, (5, 5), (25, 25), (150, 190, 210), -1)
    return base


def white_patch_balance(img):
    img_f = img.astype(np.float32)
    max_per_channel = img_f.max(axis=(0, 1))
    scale = 255.0 / np.clip(max_per_channel, 1, None)
    balanced = np.clip(img_f * scale, 0, 255).astype(np.uint8)
    return balanced


if __name__ == "__main__":
    img = make_tinted_image()
    balanced = white_patch_balance(img)

    print("Image shape:", img.shape)
    print("Original mean BGR:", np.round(img.reshape(-1, 3).mean(axis=0), 2))
    print("Balanced mean BGR:", np.round(balanced.reshape(-1, 3).mean(axis=0), 2))
    print("Balanced max BGR:", balanced.reshape(-1, 3).max(axis=0).tolist())
