"""OpenCV Practice: Histogram Back-Projection"""

import cv2
import numpy as np


def make_sample_image(size=80):
    image = np.zeros((size, size, 3), dtype=np.uint8)
    image[:, :] = (60, 120, 180)
    cv2.rectangle(image, (10, 10), (30, 30), (0, 200, 0), -1)
    return image


def back_projection(image, roi):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [30, 32], [0, 180, 0, 256])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

    return cv2.calcBackProject([hsv_image], [0, 1], roi_hist, [0, 180, 0, 256], 1)


if __name__ == "__main__":
    image = make_sample_image()
    roi = image[10:30, 10:30]

    result = back_projection(image, roi)

    print("Image shape:", image.shape)
    print("Back-projection shape:", result.shape)
    print("Max response inside ROI region:", int(result[10:30, 10:30].max()))
