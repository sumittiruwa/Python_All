"""OpenCV Practice: Flood Fill"""

import cv2
import numpy as np


def make_bounded_region(size=64):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (50, 50), (255, 255, 255), 2)
    return img


def flood_fill_from(img, seed_point, fill_color=(0, 200, 0)):
    filled = img.copy()
    h, w = img.shape[:2]
    mask = np.zeros((h + 2, w + 2), dtype=np.uint8)
    cv2.floodFill(filled, mask, seed_point, fill_color)
    return filled


if __name__ == "__main__":
    image = make_bounded_region()
    filled_inside = flood_fill_from(image, (30, 30))
    filled_outside = flood_fill_from(image, (0, 0))

    green_inside = int(np.sum(np.all(filled_inside == (0, 200, 0), axis=-1)))
    green_outside = int(np.sum(np.all(filled_outside == (0, 200, 0), axis=-1)))

    print("Filled pixels from inside seed:", green_inside)
    print("Filled pixels from outside seed:", green_outside)
