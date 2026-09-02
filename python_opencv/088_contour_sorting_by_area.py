"""OpenCV Practice: Sorting Contours by Area"""

import cv2
import numpy as np


def make_varied_size_shapes(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (15, 15), 8, 255, -1)
    cv2.circle(img, (50, 50), 20, 255, -1)
    cv2.circle(img, (85, 15), 4, 255, -1)
    return img


def sort_contours_by_area(contours, descending=True):
    return sorted(contours, key=cv2.contourArea, reverse=descending)


if __name__ == "__main__":
    image = make_varied_size_shapes()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    sorted_contours = sort_contours_by_area(contours)

    print("Number of contours:", len(contours))
    areas = [round(cv2.contourArea(c), 2) for c in sorted_contours]
    print("Areas sorted descending:", areas)
    print("Largest contour area:", areas[0])
