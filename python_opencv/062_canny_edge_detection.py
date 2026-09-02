"""OpenCV Practice: Canny Edge Detection"""

import cv2
import numpy as np


def make_shapes_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (40, 40), 255, -1)
    cv2.circle(img, (70, 70), 15, 255, -1)
    return img


def canny_edges(img, low=50, high=150):
    return cv2.Canny(img, low, high)


if __name__ == "__main__":
    image = make_shapes_image()
    edges = canny_edges(image)

    print("Image shape:", image.shape)
    print("Edge pixel count:", int(np.count_nonzero(edges)))
    print("Edge pixel ratio:", round(float(np.count_nonzero(edges) / edges.size), 4))
