"""OpenCV Practice: Draw Basic Shapes"""

import cv2
import numpy as np


def draw_shapes(height=200, width=200):
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.rectangle(canvas, (20, 20), (90, 90), (0, 255, 0), 2)
    cv2.circle(canvas, (150, 50), 30, (255, 0, 0), -1)
    cv2.line(canvas, (10, 150), (190, 150), (0, 0, 255), 3)
    return canvas


def count_nonzero_pixels(image):
    return int(np.count_nonzero(image.sum(axis=2)))


if __name__ == "__main__":
    canvas = draw_shapes()
    print("Canvas shape:", canvas.shape)
    print("Non-zero pixels:", count_nonzero_pixels(canvas))
    print("Pixel at circle center:", canvas[50, 150].tolist())
    print("Pixel at rectangle border:", canvas[20, 50].tolist())
