"""OpenCV Practice: Sepia Tone Filter"""

import cv2
import numpy as np


def make_sample_image(size=40):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :20] = (200, 150, 100)
    image[:, 20:] = (50, 80, 120)
    return image


def apply_sepia(image):
    kernel = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189],
    ])
    sepia = cv2.transform(image, kernel)
    return np.clip(sepia, 0, 255).astype(np.uint8)


if __name__ == "__main__":
    image = make_sample_image()
    sepia = apply_sepia(image)

    print("Original pixel:", image[0, 0].tolist())
    print("Sepia pixel:", sepia[0, 0].tolist())
    print("Sepia dtype:", sepia.dtype, "shape:", sepia.shape)
