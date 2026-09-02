"""OpenCV Practice: Manual Average-Channel Grayscale"""

import cv2
import numpy as np


def make_sample_image(size=40):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :] = (30, 90, 210)
    return image


def average_grayscale(image):
    return image.astype(np.float32).mean(axis=2).astype(np.uint8)


if __name__ == "__main__":
    image = make_sample_image()
    manual_gray = average_grayscale(image)
    cv2_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    print("BGR pixel:", image[0, 0].tolist())
    print("Manual average gray value:", int(manual_gray[0, 0]))
    print("cv2 luminance-weighted gray value:", int(cv2_gray[0, 0]))
