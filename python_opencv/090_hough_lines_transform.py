"""OpenCV Practice: Hough Lines Transform"""

import cv2
import numpy as np


def make_line_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.line(img, (10, 50), (90, 50), 255, 2)
    cv2.line(img, (50, 10), (50, 90), 255, 2)
    return img


def detect_lines(img, threshold=60):
    return cv2.HoughLines(img, 1, np.pi / 180, threshold)


if __name__ == "__main__":
    image = make_line_image()
    lines = detect_lines(image)

    count = 0 if lines is None else len(lines)
    print("Lines detected:", count)
    if lines is not None:
        for rho, theta in lines[:5, 0]:
            print(f"rho={round(float(rho), 2)}, theta_deg={round(float(np.degrees(theta)), 2)}")
