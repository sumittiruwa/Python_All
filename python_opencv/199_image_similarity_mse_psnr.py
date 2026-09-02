"""OpenCV Practice: MSE and PSNR Between Two Images"""

import cv2
import numpy as np


def make_base_image(size=100):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (20, 20), (80, 80), (0, 180, 0), -1)
    return img


def add_noise(img, sigma, seed=0):
    rng = np.random.default_rng(seed)
    noisy = img.astype(np.float32) + rng.normal(0, sigma, img.shape)
    return np.clip(noisy, 0, 255).astype(np.uint8)


def mse(img1, img2):
    diff = img1.astype(np.float64) - img2.astype(np.float64)
    return float(np.mean(diff ** 2))


def psnr(img1, img2):
    error = mse(img1, img2)
    if error == 0:
        return float("inf")
    return 20 * np.log10(255.0) - 10 * np.log10(error)


if __name__ == "__main__":
    base = make_base_image()
    mild = add_noise(base, sigma=10)
    strong = add_noise(base, sigma=50)

    print("Base vs itself: MSE=%.4f PSNR=%s" % (mse(base, base), psnr(base, base)))
    print("Base vs mild noise: MSE=%.4f PSNR=%.4f" % (mse(base, mild), psnr(base, mild)))
    print("Base vs strong noise: MSE=%.4f PSNR=%.4f" % (mse(base, strong), psnr(base, strong)))
