"""OpenCV Practice: Polygon Approximation with approxPolyDP"""

import cv2
import numpy as np


def make_noisy_polygon(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    points = np.array([[50, 10], [90, 50], [50, 90], [10, 50]], dtype=np.int32)
    cv2.fillPoly(img, [points], 255)
    return img


if __name__ == "__main__":
    image = make_noisy_polygon()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contour = contours[0]

    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    print("Raw contour points:", len(contour))
    print("Approximated polygon points:", len(approx))
    print("Approximated vertices:", approx.reshape(-1, 2).tolist())
