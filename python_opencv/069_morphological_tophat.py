"""OpenCV Practice: Morphological Top Hat (Bright Detail Extraction)"""

import cv2
import numpy as np


def make_image_with_small_bumps(size=64):
    img = np.full((size, size), 50, dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (54, 54), 100, -1)
    cv2.rectangle(img, (5, 5), (10, 10), 220, -1)
    cv2.rectangle(img, (54, 54), (59, 59), 220, -1)
    return img


def tophat(img, ksize=9):
    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


if __name__ == "__main__":
    image = make_image_with_small_bumps()
    result = tophat(image)

    print("Image mean:", round(float(image.mean()), 3))
    print("Top hat mean:", round(float(result.mean()), 3))
    print("Top hat max:", int(result.max()))
    print("Bright-detail pixel count (>50):", int(np.sum(result > 50)))
