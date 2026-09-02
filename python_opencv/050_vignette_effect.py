"""OpenCV Practice: Vignette Effect"""

import cv2
import numpy as np


def make_sample_image(height=80, width=100):
    return np.full((height, width, 3), 200, dtype=np.uint8)


def apply_vignette(image, strength=2.0):
    height, width = image.shape[:2]
    kernel_x = cv2.getGaussianKernel(width, width / strength)
    kernel_y = cv2.getGaussianKernel(height, height / strength)
    mask = kernel_y * kernel_x.T
    mask = mask / mask.max()

    vignette = image.astype(np.float32)
    for c in range(3):
        vignette[:, :, c] *= mask
    return vignette.astype(np.uint8)


if __name__ == "__main__":
    image = make_sample_image()
    result = apply_vignette(image)

    h, w = result.shape[:2]
    print("Center pixel:", result[h // 2, w // 2].tolist())
    print("Corner pixel:", result[0, 0].tolist())
    print("Center brighter than corner:", bool(result[h // 2, w // 2].mean() > result[0, 0].mean()))
