"""OpenCV Practice: Image Moments and Centroid of a Binary Blob"""

import cv2
import numpy as np


def make_blob_image(size=200):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (70, 130), 40, 255, -1)
    return img


def centroid_from_moments(binary_img):
    m = cv2.moments(binary_img, binaryImage=True)
    cx = m["m10"] / m["m00"]
    cy = m["m01"] / m["m00"]
    return cx, cy, m


if __name__ == "__main__":
    img = make_blob_image()
    cx, cy, moments = centroid_from_moments(img)

    print("Image shape:", img.shape)
    print("Area (m00):", moments["m00"])
    print("Centroid:", (round(cx, 2), round(cy, 2)))
    print("Central moment mu20:", round(moments["mu20"], 2))
