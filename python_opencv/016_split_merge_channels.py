"""OpenCV Practice: Split and Merge Channels"""

import cv2
import numpy as np


def make_sample_image(size=50):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :, 0] = 40
    image[:, :, 1] = 90
    image[:, :, 2] = 200
    return image


def split_channels(image):
    return cv2.split(image)


def merge_channels(b, g, r):
    return cv2.merge((b, g, r))


if __name__ == "__main__":
    image = make_sample_image()
    b, g, r = split_channels(image)

    print("B mean:", float(b.mean()), "G mean:", float(g.mean()), "R mean:", float(r.mean()))

    swapped = merge_channels(r, g, b)
    print("Original pixel:", image[0, 0].tolist())
    print("Swapped pixel:", swapped[0, 0].tolist())
