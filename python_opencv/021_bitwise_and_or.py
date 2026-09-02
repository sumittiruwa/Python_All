"""OpenCV Practice: Bitwise AND/OR Masking"""

import cv2
import numpy as np


def make_masks(size=60):
    square = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(square, (10, 10), (40, 40), 255, -1)

    circle = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(circle, (35, 35), 20, 255, -1)

    return square, circle


if __name__ == "__main__":
    square, circle = make_masks()

    and_result = cv2.bitwise_and(square, circle)
    or_result = cv2.bitwise_or(square, circle)

    print("Square white pixels:", int(np.count_nonzero(square)))
    print("Circle white pixels:", int(np.count_nonzero(circle)))
    print("AND white pixels:", int(np.count_nonzero(and_result)))
    print("OR white pixels:", int(np.count_nonzero(or_result)))
