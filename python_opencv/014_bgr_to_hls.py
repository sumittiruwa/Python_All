"""OpenCV Practice: BGR to HLS Conversion"""

import cv2
import numpy as np


def make_sample_image(size=60):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :] = (200, 100, 50)
    return image


def to_hls(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2HLS)


if __name__ == "__main__":
    image = make_sample_image()
    hls = to_hls(image)

    print("BGR pixel:", image[0, 0].tolist())
    print("HLS pixel:", hls[0, 0].tolist())
    print("Lightness channel mean:", round(float(hls[:, :, 1].mean()), 2))
