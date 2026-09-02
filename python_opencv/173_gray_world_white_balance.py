"""OpenCV Practice: Gray-World White Balance"""

import cv2
import numpy as np


def make_tinted_scene(size=100, seed=0):
    rng = np.random.default_rng(seed)
    base = rng.integers(60, 200, size=(size, size, 3), dtype=np.uint8)
    tint = np.array([1.3, 1.0, 0.7])
    return np.clip(base.astype(np.float32) * tint, 0, 255).astype(np.uint8)


def gray_world_balance(img):
    img_f = img.astype(np.float32)
    channel_means = img_f.mean(axis=(0, 1))
    gray_mean = channel_means.mean()
    scale = gray_mean / np.clip(channel_means, 1, None)
    balanced = np.clip(img_f * scale, 0, 255).astype(np.uint8)
    return balanced


if __name__ == "__main__":
    img = make_tinted_scene()
    balanced = gray_world_balance(img)

    print("Image shape:", img.shape)
    print("Original mean BGR:", np.round(img.reshape(-1, 3).mean(axis=0), 2))
    print("Balanced mean BGR:", np.round(balanced.reshape(-1, 3).mean(axis=0), 2))
