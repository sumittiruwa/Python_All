"""OpenCV Practice: Scharr Operator Gradient"""

import cv2
import numpy as np


def make_diagonal_gradient_image(size=64):
    ramp = np.linspace(0, 255, size, dtype=np.uint8)
    img = np.tile(ramp, (size, 1))
    return img


def scharr_magnitude(img):
    gx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    gy = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    return cv2.magnitude(gx, gy)


if __name__ == "__main__":
    image = make_diagonal_gradient_image()
    magnitude = scharr_magnitude(image)

    print("Image shape:", image.shape)
    print("Magnitude mean:", round(float(magnitude.mean()), 3))
    print("Magnitude max:", round(float(magnitude.max()), 3))
    print("Magnitude std:", round(float(magnitude.std()), 3))
