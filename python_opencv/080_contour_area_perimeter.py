"""OpenCV Practice: Contour Area and Perimeter"""

import cv2
import numpy as np


def make_square_image(size=100, side=40):
    img = np.zeros((size, size), dtype=np.uint8)
    start = (size - side) // 2
    cv2.rectangle(img, (start, start), (start + side, start + side), 255, -1)
    return img, side


if __name__ == "__main__":
    image, side = make_square_image()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[0]

    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, closed=True)

    print("Expected side length:", side)
    print("Contour area:", round(area, 2))
    print("Contour perimeter:", round(perimeter, 2))
    print("Expected area approx:", side * side)
