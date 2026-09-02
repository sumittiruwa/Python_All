"""OpenCV Practice: cv2.undistort with Synthetic Distortion Coefficients"""

import cv2
import numpy as np


def make_grid_image(size=240, step=20):
    img = np.full((size, size, 3), 30, dtype=np.uint8)
    for x in range(0, size, step):
        cv2.line(img, (x, 0), (x, size), (255, 255, 255), 1)
    for y in range(0, size, step):
        cv2.line(img, (0, y), (size, y), (255, 255, 255), 1)
    return img


def undistort(img):
    h, w = img.shape[:2]
    camera_matrix = np.array([[w, 0, w / 2], [0, w, h / 2], [0, 0, 1]], dtype=np.float64)
    dist_coeffs = np.array([-0.35, 0.12, 0.0, 0.0, 0.0], dtype=np.float64)
    return cv2.undistort(img, camera_matrix, dist_coeffs)


if __name__ == "__main__":
    img = make_grid_image()
    result = undistort(img)

    print("Original shape:", img.shape)
    print("Undistorted shape:", result.shape)
    print("Original mean:", round(float(img.mean()), 2))
    print("Undistorted mean:", round(float(result.mean()), 2))
