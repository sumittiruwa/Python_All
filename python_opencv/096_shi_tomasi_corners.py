"""OpenCV Practice: Shi-Tomasi Corner Detection (goodFeaturesToTrack)"""

import cv2
import numpy as np


def make_multi_shape_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (40, 40), 255, -1)
    cv2.rectangle(img, (60, 60), (90, 90), 255, -1)
    return img


def shi_tomasi_corners(img, max_corners=20, quality=0.01, min_dist=10):
    corners = cv2.goodFeaturesToTrack(img, max_corners, quality, min_dist)
    return corners


if __name__ == "__main__":
    image = make_multi_shape_image()
    corners = shi_tomasi_corners(image)

    count = 0 if corners is None else len(corners)
    print("Corners detected:", count)
    if corners is not None:
        for c in corners.reshape(-1, 2)[:8]:
            print("Corner:", (round(float(c[0]), 1), round(float(c[1]), 1)))
