"""OpenCV Practice: Draw a Coordinate Grid + Labels on an Image"""

import cv2
import numpy as np


def make_canvas(size=200):
    return np.full((size, size, 3), 255, dtype=np.uint8)


def draw_grid(img, step=40, color=(200, 200, 200)):
    h, w = img.shape[:2]
    for x in range(0, w, step):
        cv2.line(img, (x, 0), (x, h), color, 1)
    for y in range(0, h, step):
        cv2.line(img, (0, y), (w, y), color, 1)
    return img


def label_intersections(img, step=40, color=(0, 0, 0)):
    h, w = img.shape[:2]
    count = 0
    for x in range(0, w, step):
        for y in range(0, h, step):
            cv2.putText(img, f"{x},{y}", (x + 2, y + 12), cv2.FONT_HERSHEY_PLAIN, 0.7, color, 1)
            count += 1
    return img, count


if __name__ == "__main__":
    img = make_canvas()
    img = draw_grid(img)
    img, label_count = label_intersections(img)

    print("Canvas shape:", img.shape)
    print("Labels drawn:", label_count)
    print("Non-white pixels:", int(np.any(img != 255, axis=2).sum()))
