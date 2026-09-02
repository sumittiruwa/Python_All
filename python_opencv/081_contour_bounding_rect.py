"""OpenCV Practice: Bounding Rectangle of a Contour"""

import cv2
import numpy as np


def make_rotated_shape(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    points = np.array([[50, 15], [80, 50], [50, 85], [20, 50]], dtype=np.int32)
    cv2.fillPoly(img, [points], 255)
    return img


if __name__ == "__main__":
    image = make_rotated_shape()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[0]

    x, y, w, h = cv2.boundingRect(contour)

    print("Number of contours:", len(contours))
    print(f"Bounding rect: x={x}, y={y}, w={w}, h={h}")
    print("Bounding rect area:", w * h)
    print("Contour area:", round(cv2.contourArea(contour), 2))
