"""OpenCV Practice: Harris Corner Detection"""

import cv2
import numpy as np


def make_square_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (25, 25), (75, 75), 255, -1)
    return img


def harris_corners(img, block_size=2, ksize=3, k=0.04):
    gray = np.float32(img)
    response = cv2.cornerHarris(gray, block_size, ksize, k)
    return response


if __name__ == "__main__":
    image = make_square_image()
    response = harris_corners(image)

    threshold = 0.01 * response.max()
    corner_pixels = np.argwhere(response > threshold)

    print("Image shape:", image.shape)
    print("Max corner response:", round(float(response.max()), 6))
    print("Strong corner pixel count:", len(corner_pixels))
