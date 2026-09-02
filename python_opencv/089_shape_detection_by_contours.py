"""OpenCV Practice: Shape Classification by Contour Approximation"""

import cv2
import numpy as np


def make_shapes_image(size=150):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (40, 40), 255, -1)
    triangle = np.array([[80, 10], [110, 40], [50, 40]], dtype=np.int32)
    cv2.fillPoly(img, [triangle], 255)
    cv2.circle(img, (100, 100), 20, 255, -1)
    square = np.array([[10, 90], [40, 90], [40, 120], [10, 120]], dtype=np.int32)
    cv2.fillPoly(img, [square], 255)
    return img


def classify_shape(contour):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    vertices = len(approx)

    if vertices == 3:
        return "triangle"
    if vertices == 4:
        x, y, w, h = cv2.boundingRect(approx)
        ratio = w / float(h)
        return "square" if 0.9 <= ratio <= 1.1 else "rectangle"
    if vertices > 6:
        return "circle"
    return f"polygon-{vertices}"


if __name__ == "__main__":
    image = make_shapes_image()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("Number of shapes found:", len(contours))
    for c in sorted(contours, key=cv2.contourArea):
        shape = classify_shape(c)
        area = round(cv2.contourArea(c), 1)
        print(f"Shape: {shape}, area: {area}")
