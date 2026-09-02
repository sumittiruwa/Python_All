"""OpenCV Practice: Convex Hull of a Contour"""

import cv2
import numpy as np


def make_star_like_shape(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    points = np.array(
        [[50, 5], [61, 35], [95, 35], [68, 57], [79, 91], [50, 70], [21, 91], [32, 57], [5, 35], [39, 35]],
        dtype=np.int32,
    )
    cv2.fillPoly(img, [points], 255)
    return img


if __name__ == "__main__":
    image = make_star_like_shape()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[0]
    hull = cv2.convexHull(contour)

    contour_area = cv2.contourArea(contour)
    hull_area = cv2.contourArea(hull)

    print("Contour points:", len(contour))
    print("Hull points:", len(hull))
    print("Contour area:", round(contour_area, 2))
    print("Hull area:", round(hull_area, 2))
    print("Solidity (contour/hull):", round(contour_area / hull_area, 4))
