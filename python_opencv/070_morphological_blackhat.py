"""OpenCV Practice: Morphological Black Hat (Dark Detail Extraction)"""

import cv2
import numpy as np


def make_image_with_small_dips(size=64):
    img = np.full((size, size), 180, dtype=np.uint8)
    cv2.rectangle(img, (5, 5), (10, 10), 20, -1)
    cv2.rectangle(img, (54, 54), (59, 59), 20, -1)
    return img


def blackhat(img, ksize=9):
    kernel = np.ones((ksize, ksize), dtype=np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


if __name__ == "__main__":
    image = make_image_with_small_dips()
    result = blackhat(image)

    print("Image mean:", round(float(image.mean()), 3))
    print("Black hat mean:", round(float(result.mean()), 3))
    print("Black hat max:", int(result.max()))
    print("Dark-detail pixel count (>50):", int(np.sum(result > 50)))
