"""OpenCV Practice: Distance Transform"""

import cv2
import numpy as np


def make_blob_image(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (32, 32), 25, 255, -1)
    return img


def distance_transform(img):
    return cv2.distanceTransform(img, cv2.DIST_L2, 5)


if __name__ == "__main__":
    image = make_blob_image()
    dist = distance_transform(image)

    max_loc = np.unravel_index(np.argmax(dist), dist.shape)
    print("Image shape:", image.shape)
    print("Max distance value:", round(float(dist.max()), 3))
    print("Max distance location (row, col):", max_loc)
    print("Mean distance (nonzero region):", round(float(dist[dist > 0].mean()), 3))
