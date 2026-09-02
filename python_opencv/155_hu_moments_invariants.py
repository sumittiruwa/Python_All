"""OpenCV Practice: Hu Moments of a Contour"""

import cv2
import numpy as np


def make_triangle_image(size=200):
    img = np.zeros((size, size), dtype=np.uint8)
    pts = np.array([[100, 30], [40, 160], [160, 160]], dtype=np.int32)
    cv2.fillPoly(img, [pts], 255)
    return img


def largest_contour(binary_img):
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return max(contours, key=cv2.contourArea)


def hu_log_moments(contour):
    hu = cv2.HuMoments(cv2.moments(contour)).ravel()
    return -np.sign(hu) * np.log10(np.abs(hu) + 1e-30)


if __name__ == "__main__":
    img = make_triangle_image()
    contour = largest_contour(img)
    hu_log = hu_log_moments(contour)

    print("Contour points:", len(contour))
    print("Contour area:", cv2.contourArea(contour))
    print("Log-scaled Hu moments:", np.round(hu_log, 3))
