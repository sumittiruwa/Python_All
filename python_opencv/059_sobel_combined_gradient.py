"""OpenCV Practice: Combined Sobel Gradient Magnitude"""

import cv2
import numpy as np


def make_box_image(size=64):
    img = np.zeros((size, size), dtype=np.uint8)
    cv2.rectangle(img, (16, 16), (48, 48), 255, -1)
    return img


def sobel_magnitude(img, ksize=3):
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=ksize)
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=ksize)
    magnitude = cv2.magnitude(gx, gy)
    return cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


if __name__ == "__main__":
    image = make_box_image()
    magnitude = sobel_magnitude(image)

    print("Image shape:", image.shape)
    print("Magnitude dtype:", magnitude.dtype)
    print("Magnitude max:", int(magnitude.max()))
    print("Edge pixel count (>50):", int(np.sum(magnitude > 50)))
