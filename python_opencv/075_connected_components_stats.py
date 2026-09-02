"""OpenCV Practice: Connected Components with Stats"""

import cv2
import numpy as np


def make_multi_blob_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (20, 20), 8, 255, -1)
    cv2.rectangle(img, (50, 10), (80, 30), 255, -1)
    cv2.circle(img, (30, 70), 15, 255, -1)
    return img


def label_with_stats(img):
    return cv2.connectedComponentsWithStats(img, connectivity=8)


if __name__ == "__main__":
    image = make_multi_blob_image()
    num_labels, labels, stats, centroids = label_with_stats(image)

    print("Foreground components:", num_labels - 1)
    for label in range(1, num_labels):
        x, y, w, h, area = stats[label]
        cx, cy = centroids[label]
        print(f"Component {label}: bbox=({x},{y},{w},{h}), area={area}, centroid=({round(cx,1)},{round(cy,1)})")
