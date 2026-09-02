"""OpenCV Practice: Color Quantization with cv2.kmeans"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :30] = (0, 0, 255)
    image[:, 30:] = (0, 255, 0)
    return image


def quantize_colors(image, k=2):
    data = image.reshape((-1, 3)).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(data, k, None, criteria, 5, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()].reshape(image.shape)
    return quantized, centers


if __name__ == "__main__":
    image = make_sample_image()
    quantized, centers = quantize_colors(image, k=2)

    print("Original unique colors:", len(np.unique(image.reshape(-1, 3), axis=0)))
    print("Quantized unique colors:", len(np.unique(quantized.reshape(-1, 3), axis=0)))
    print("Cluster centers:", centers.tolist())
