"""OpenCV Practice: Image Resize"""

import cv2
import numpy as np


def make_sample_image(height=80, width=120):
    image = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.rectangle(image, (10, 10), (60, 40), (0, 255, 0), -1)
    return image


def resize_image(image, new_size, interpolation):
    return cv2.resize(image, new_size, interpolation=interpolation)


if __name__ == "__main__":
    image = make_sample_image()
    methods = {
        "nearest": cv2.INTER_NEAREST,
        "linear": cv2.INTER_LINEAR,
        "cubic": cv2.INTER_CUBIC,
        "area": cv2.INTER_AREA,
    }

    for name, method in methods.items():
        resized = resize_image(image, (60, 40), method)
        print(f"{name}: shape={resized.shape}, mean={resized.mean():.2f}")
