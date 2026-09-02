"""OpenCV Practice: Laplacian Edge Detector"""

import cv2
import numpy as np


def make_circle_image(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (size // 2, size // 2), 18, 255, -1)
    return img


def laplacian_edges(img, ksize=3):
    lap = cv2.Laplacian(img, cv2.CV_64F, ksize=ksize)
    return cv2.convertScaleAbs(lap)


if __name__ == "__main__":
    image = make_circle_image()
    edges = laplacian_edges(image)

    print("Image shape:", image.shape)
    print("Edge pixel count (>30):", int(np.sum(edges > 30)))
    print("Edge max value:", int(edges.max()))
    print("Edge mean value:", round(float(edges.mean()), 3))
