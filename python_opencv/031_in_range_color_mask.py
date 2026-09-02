"""OpenCV Practice: in_range Color Masking"""

import cv2
import numpy as np


def make_sample_image(size=80):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(image, (0, 0), (40, 80), (0, 255, 0), -1)
    cv2.rectangle(image, (40, 0), (80, 80), (0, 0, 255), -1)
    return image


def color_mask(image, lower, upper):
    return cv2.inRange(image, np.array(lower), np.array(upper))


if __name__ == "__main__":
    image = make_sample_image()
    green_mask = color_mask(image, (0, 200, 0), (50, 255, 50))

    print("Image shape:", image.shape)
    print("Green mask white pixels:", int(np.count_nonzero(green_mask)))
    print("Expected green region size:", 40 * 80)
    masked = cv2.bitwise_and(image, image, mask=green_mask)
    print("Masked mean (should be greenish):", masked.reshape(-1, 3).mean(axis=0).round(2).tolist())
