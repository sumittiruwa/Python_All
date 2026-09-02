"""OpenCV Practice: BGR to YCrCb Conversion"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :] = (30, 120, 200)
    return image


def to_ycrcb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)


if __name__ == "__main__":
    image = make_sample_image()
    ycrcb = to_ycrcb(image)

    print("BGR pixel:", image[0, 0].tolist())
    print("YCrCb pixel:", ycrcb[0, 0].tolist())
    print("Y channel mean:", round(float(ycrcb[:, :, 0].mean()), 2))
