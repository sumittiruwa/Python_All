"""OpenCV Practice: Simplified Structural Similarity (SSIM), numpy-based"""

import cv2
import numpy as np


def make_base_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (50, 50), 30, 200, -1)
    return img


def add_noise(img, sigma, seed=0):
    rng = np.random.default_rng(seed)
    noisy = img.astype(np.float32) + rng.normal(0, sigma, img.shape)
    return np.clip(noisy, 0, 255).astype(np.uint8)


def simple_ssim(img1, img2, C1=6.5025, C2=58.5225):
    a = img1.astype(np.float64)
    b = img2.astype(np.float64)
    mu1, mu2 = a.mean(), b.mean()
    var1, var2 = a.var(), b.var()
    covar = ((a - mu1) * (b - mu2)).mean()

    numerator = (2 * mu1 * mu2 + C1) * (2 * covar + C2)
    denominator = (mu1 ** 2 + mu2 ** 2 + C1) * (var1 + var2 + C2)
    return numerator / denominator


if __name__ == "__main__":
    base = make_base_image()
    slightly_noisy = add_noise(base, sigma=5)
    very_noisy = add_noise(base, sigma=60)

    print("SSIM base vs itself:", round(simple_ssim(base, base), 4))
    print("SSIM base vs slightly noisy:", round(simple_ssim(base, slightly_noisy), 4))
    print("SSIM base vs very noisy:", round(simple_ssim(base, very_noisy), 4))
