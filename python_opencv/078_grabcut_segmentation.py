"""OpenCV Practice: GrabCut Segmentation on Synthetic Image"""

import cv2
import numpy as np


def make_foreground_image(size=100):
    img = np.full((size, size, 3), 40, dtype=np.uint8)
    cv2.rectangle(img, (30, 30), (70, 70), (200, 200, 200), -1)
    return img


def grabcut_segment(img, rect):
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    bgd_model = np.zeros((1, 65), dtype=np.float64)
    fgd_model = np.zeros((1, 65), dtype=np.float64)

    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    result_mask = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 1, 0).astype(np.uint8)
    return result_mask


if __name__ == "__main__":
    image = make_foreground_image()
    rect = (20, 20, 60, 60)
    mask = grabcut_segment(image, rect)

    print("Image shape:", image.shape)
    print("Foreground pixel count:", int(mask.sum()))
    print("Foreground ratio:", round(float(mask.sum() / mask.size), 4))
