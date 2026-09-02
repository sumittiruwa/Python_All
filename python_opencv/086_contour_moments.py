"""OpenCV Practice: Contour Moments and Centroid"""

import cv2
import numpy as np


def make_offset_circle(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (70, 30), 18, 255, -1)
    return img


if __name__ == "__main__":
    image = make_offset_circle()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[0]

    moments = cv2.moments(contour)
    cx = moments["m10"] / moments["m00"]
    cy = moments["m01"] / moments["m00"]

    print("m00 (area via moments):", round(moments["m00"], 2))
    print("Centroid (cx, cy):", (round(cx, 2), round(cy, 2)))
    print("contourArea for comparison:", round(cv2.contourArea(contour), 2))
