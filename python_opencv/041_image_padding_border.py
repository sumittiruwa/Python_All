"""OpenCV Practice: Image Padding with copyMakeBorder"""

import cv2
import numpy as np


def make_sample_image(size=30):
    return np.full((size, size, 3), (0, 128, 255), dtype=np.uint8)


def add_border(image, size, border_type, value=(0, 0, 0)):
    return cv2.copyMakeBorder(image, size, size, size, size, border_type, value=value)


if __name__ == "__main__":
    image = make_sample_image()

    constant = add_border(image, 5, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    reflect = add_border(image, 5, cv2.BORDER_REFLECT)
    replicate = add_border(image, 5, cv2.BORDER_REPLICATE)

    print("Original shape:", image.shape)
    print("Constant border shape:", constant.shape)
    print("Constant border corner pixel:", constant[0, 0].tolist())
    print("Reflect border shape:", reflect.shape)
    print("Replicate border corner pixel:", replicate[0, 0].tolist())
