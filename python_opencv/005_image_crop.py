"""OpenCV Practice: Image Crop"""

import cv2
import numpy as np


def make_sample_image(height=100, width=100):
    image = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.circle(image, (50, 50), 30, (0, 0, 255), -1)
    return image


def crop_region(image, x, y, w, h):
    return image[y:y + h, x:x + w]


if __name__ == "__main__":
    image = make_sample_image()
    roi = crop_region(image, 20, 20, 40, 40)

    print("Original shape:", image.shape)
    print("Cropped shape:", roi.shape)
    print("Cropped mean:", round(float(roi.mean()), 2))
    print("Cropped center pixel:", roi[20, 20].tolist())
