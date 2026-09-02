"""OpenCV Practice: warpPerspective to Align a Synthetic Pair"""

import cv2
import numpy as np


def make_checker(size=200):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    step = 25
    for y in range(0, size, step):
        for x in range(0, size, step):
            if (x // step + y // step) % 2 == 0:
                cv2.rectangle(img, (x, y), (x + step, y + step), (200, 200, 200), -1)
    return img


def homography_from_points():
    src = np.array([[0, 0], [199, 0], [199, 199], [0, 199]], dtype=np.float32)
    dst = np.array([[10, 20], [190, 5], [199, 199], [5, 180]], dtype=np.float32)
    return cv2.getPerspectiveTransform(src, dst)


if __name__ == "__main__":
    base = make_checker()
    H = homography_from_points()
    warped = cv2.warpPerspective(base, H, (base.shape[1], base.shape[0]))

    print("Base shape:", base.shape)
    print("Homography matrix:\n", np.round(H, 3))
    print("Warped shape:", warped.shape)
    print("Warped mean pixel value:", round(float(warped.mean()), 2))
