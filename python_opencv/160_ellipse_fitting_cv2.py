"""OpenCV Practice: cv2.fitEllipse on a Contour"""

import cv2
import numpy as np


def make_ellipse_image(size=200):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.ellipse(img, (100, 100), (70, 35), 25, 0, 360, 255, -1)
    return img


def fit_ellipse_to_contour(binary_img):
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)
    (cx, cy), (major, minor), angle = cv2.fitEllipse(contour)
    return (cx, cy), (major, minor), angle


if __name__ == "__main__":
    img = make_ellipse_image()
    center, axes, angle = fit_ellipse_to_contour(img)

    print("Image shape:", img.shape)
    print("Fitted center:", tuple(round(v, 2) for v in center))
    print("Fitted axes (major, minor):", tuple(round(v, 2) for v in axes))
    print("Fitted angle:", round(angle, 2))
