"""OpenCV Practice: Watershed Segmentation on Synthetic Markers"""

import cv2
import numpy as np


def make_two_blob_image(size=100):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.circle(img, (30, 50), 20, (255, 255, 255), -1)
    cv2.circle(img, (70, 50), 20, (255, 255, 255), -1)
    return img


def watershed_segment(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    dist = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist, 0.5 * dist.max(), 255, 0)
    sure_fg = sure_fg.astype(np.uint8)

    num_markers, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[thresh == 0] = 0

    markers = cv2.watershed(img, markers)
    return markers, num_markers


if __name__ == "__main__":
    image = make_two_blob_image()
    markers, num_seed_labels = watershed_segment(image)

    unique_labels = np.unique(markers)
    print("Seed labels found:", num_seed_labels - 1)
    print("Unique watershed labels:", unique_labels.tolist())
    print("Boundary pixels (-1):", int(np.sum(markers == -1)))
