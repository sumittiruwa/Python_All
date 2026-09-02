"""OpenCV Practice: Create Blank Image"""

import cv2
import numpy as np


def create_blank_image(height, width, channels=3, color=(0, 0, 0)):
    if channels == 1:
        image = np.zeros((height, width), dtype=np.uint8)
        image[:] = color[0]
        return image
    image = np.zeros((height, width, channels), dtype=np.uint8)
    image[:] = color
    return image


def image_stats(image):
    return {
        "shape": image.shape,
        "dtype": str(image.dtype),
        "min": int(image.min()),
        "max": int(image.max()),
        "mean": round(float(image.mean()), 2),
    }


if __name__ == "__main__":
    black = create_blank_image(100, 200)
    blue = create_blank_image(100, 200, color=(255, 0, 0))
    gray = create_blank_image(100, 200, channels=1, color=(128,))

    print("Black image stats:", image_stats(black))
    print("Blue image stats:", image_stats(blue))
    print("Gray image stats:", image_stats(gray))
    print("cv2 version:", cv2.__version__)
