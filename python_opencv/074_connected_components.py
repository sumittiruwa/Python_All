"""OpenCV Practice: Connected Components Labeling"""

import cv2
import numpy as np


def make_multi_blob_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(img, (20, 20), 10, 255, -1)
    cv2.circle(img, (70, 20), 10, 255, -1)
    cv2.rectangle(img, (40, 60), (60, 80), 255, -1)
    return img


def label_components(img):
    num_labels, labels = cv2.connectedComponents(img)
    return num_labels, labels


if __name__ == "__main__":
    image = make_multi_blob_image()
    num_labels, labels = label_components(image)

    print("Number of labels (including background):", num_labels)
    print("Foreground components:", num_labels - 1)
    for label in range(1, num_labels):
        print(f"Component {label} pixel count:", int(np.sum(labels == label)))
