"""OpenCV Practice: Channel Swap Effect"""

import cv2
import numpy as np


def make_sample_image(size=30):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :] = (10, 80, 200)
    return image


def swap_channels(image, order):
    b, g, r = cv2.split(image)
    channels = {"b": b, "g": g, "r": r}
    return cv2.merge([channels[c] for c in order])


if __name__ == "__main__":
    image = make_sample_image()
    rgb_effect = swap_channels(image, "rgb")
    grb_effect = swap_channels(image, "grb")

    print("Original BGR pixel:", image[0, 0].tolist())
    print("Swapped to RGB order pixel:", rgb_effect[0, 0].tolist())
    print("Swapped to GRB order pixel:", grb_effect[0, 0].tolist())
