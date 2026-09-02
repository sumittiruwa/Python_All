"""OpenCV Practice: Minimum Enclosing Circle of a Contour"""

import cv2
import numpy as np


def make_triangle_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    points = np.array([[50, 10], [90, 80], [10, 80]], dtype=np.int32)
    cv2.fillPoly(img, [points], 255)
    return img


if __name__ == "__main__":
    image = make_triangle_image()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[0]

    (x, y), radius = cv2.minEnclosingCircle(contour)

    print("Enclosing circle center:", (round(x, 2), round(y, 2)))
    print("Enclosing circle radius:", round(radius, 2))
    print("Enclosing circle area:", round(3.14159 * radius * radius, 2))
    print("Contour area:", round(cv2.contourArea(contour), 2))
