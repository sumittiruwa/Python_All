"""OpenCV Practice: Inspect Image Array Shape / Dtype / Channel Order Conversions"""

import cv2
import numpy as np


def make_bgr_image(size=64):
    img = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.rectangle(img, (0, 0), (size, size), (255, 0, 0), -1)
    return img


def to_chw_float(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    chw = np.transpose(rgb, (2, 0, 1)).astype(np.float32) / 255.0
    return chw


if __name__ == "__main__":
    img = make_bgr_image()
    chw = to_chw_float(img)

    print("BGR (HWC) shape/dtype:", img.shape, img.dtype)
    print("CHW float shape/dtype:", chw.shape, chw.dtype)
    print("BGR pixel at (0,0):", img[0, 0].tolist())
    print("Corresponding RGB channel-0 (red) value:", round(float(chw[0, 0, 0]), 3))
