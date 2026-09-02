"""OpenCV Practice: Minimum Area Rectangle of a Contour"""

import cv2
import numpy as np


def make_rotated_rectangle(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    rect = ((50, 50), (40, 20), 30)
    box = cv2.boxPoints(rect).astype(np.int32)
    cv2.fillPoly(img, [box], 255)
    return img


if __name__ == "__main__":
    image = make_rotated_rectangle()
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[0]

    (cx, cy), (w, h), angle = cv2.minAreaRect(contour)

    print("Min area rect center:", (round(cx, 2), round(cy, 2)))
    print("Min area rect size:", (round(w, 2), round(h, 2)))
    print("Min area rect angle:", round(angle, 2))
    print("Min area rect area:", round(w * h, 2))
