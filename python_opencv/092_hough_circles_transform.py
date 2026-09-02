"""OpenCV Practice: Hough Circles Transform"""

import cv2
import numpy as np


def make_circles_image(size=150):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (40, 40), 15, 255, 2)
    cv2.circle(img, (110, 100), 20, 255, 2)
    return img


def detect_circles(img):
    blurred = cv2.GaussianBlur(img, (5, 5), 1.2)
    return cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=30, param1=50, param2=20, minRadius=5, maxRadius=40
    )


if __name__ == "__main__":
    image = make_circles_image()
    circles = detect_circles(image)

    count = 0 if circles is None else circles.shape[1]
    print("Circles detected:", count)
    if circles is not None:
        for x, y, r in circles[0]:
            print(f"center=({round(float(x),1)},{round(float(y),1)}), radius={round(float(r),1)}")
