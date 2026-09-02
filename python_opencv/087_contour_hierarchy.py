"""OpenCV Practice: Contour Hierarchy with RETR_TREE"""

import cv2
import numpy as np


def make_nested_shapes(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (90, 90), 255, -1)
    cv2.rectangle(img, (30, 30), (70, 70), 0, -1)
    cv2.rectangle(img, (45, 45), (55, 55), 255, -1)
    return img


if __name__ == "__main__":
    image = make_nested_shapes()
    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print("Number of contours:", len(contours))
    for i, h in enumerate(hierarchy[0]):
        next_c, prev_c, child, parent = h
        print(f"Contour {i}: parent={parent}, first_child={child}, area={round(cv2.contourArea(contours[i]), 2)}")
