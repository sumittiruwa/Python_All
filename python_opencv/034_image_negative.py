"""OpenCV Practice: Image Negative"""

import cv2
import numpy as np


def make_sample_image(size=40):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(image, (0, 0), (20, 40), (50, 100, 150), -1)
    return image


def invert_image(image):
    return cv2.bitwise_not(image)


if __name__ == "__main__":
    image = make_sample_image()
    negative = invert_image(image)

    print("Original pixel:", image[0, 0].tolist())
    print("Negative pixel:", negative[0, 0].tolist())
    print("Sum equals 255 per channel:", bool(np.all(image.astype(np.int32) + negative.astype(np.int32) == 255)))
