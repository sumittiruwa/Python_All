"""OpenCV Practice: Bitwise XOR/NOT Masking"""

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

    xor_result = cv2.bitwise_xor(square, circle)
    not_result = cv2.bitwise_not(square)

    print("XOR white pixels:", int(np.count_nonzero(xor_result)))
    print("NOT of square white pixels:", int(np.count_nonzero(not_result)))
    print("Square white pixels:", int(np.count_nonzero(square)))
    print("Total pixels:", square.size)
