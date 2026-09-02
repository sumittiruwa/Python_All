"""OpenCV Practice: Basic Contour Detection"""

import cv2
import numpy as np


def make_shapes_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (35, 35), 255, -1)
    cv2.circle(img, (70, 70), 15, 255, -1)
    return img


def find_all_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours, hierarchy


if __name__ == "__main__":
    image = make_shapes_image()
    contours, hierarchy = find_all_contours(image)

    print("Number of contours found:", len(contours))
    for i, c in enumerate(contours):
        print(f"Contour {i}: points={len(c)}, area={round(cv2.contourArea(c), 2)}")
