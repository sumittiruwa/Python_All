"""OpenCV Practice: Auto-Computed Canny Thresholds from Median"""

import cv2
import numpy as np


def make_shapes_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (15, 15), (45, 45), 255, -1)
    cv2.circle(img, (70, 70), 18, 200, -1)
    return img


def auto_canny(img, sigma=0.33):
    median = float(np.median(img))
    lower = int(max(0, (1.0 - sigma) * median))
    upper = int(min(255, (1.0 + sigma) * median))
    return cv2.Canny(img, lower, upper), lower, upper


if __name__ == "__main__":
    image = make_shapes_image()
    edges, low, high = auto_canny(image)

    print("Median intensity:", round(float(np.median(image)), 3))
    print("Auto thresholds: low={}, high={}".format(low, high))
    print("Edge pixel count:", int(np.count_nonzero(edges)))
