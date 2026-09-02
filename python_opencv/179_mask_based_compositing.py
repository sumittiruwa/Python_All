"""OpenCV Practice: Composite Using a Binary Mask (copyTo-style)"""

import cv2
import numpy as np


def make_background(size=120):
    return np.full((size, size, 3), (40, 40, 40), dtype=np.uint8)


def make_foreground(size=120):
    return np.full((size, size, 3), (0, 255, 0), dtype=np.uint8)


def make_star_mask(size=120):
    mask = np.zeros((size, size), dtype=np.uint8)
    cv2.circle(mask, (size // 2, size // 2), size // 3, 255, -1)
    return mask


def copy_to(src, dst, mask):
    result = dst.copy()
    result[mask > 0] = src[mask > 0]
    return result


if __name__ == "__main__":
    bg = make_background()
    fg = make_foreground()
    mask = make_star_mask()

    result = copy_to(fg, bg, mask)

    print("Mask coverage:", int((mask > 0).sum()))
    print("Center pixel (masked-in):", result[60, 60].tolist())
    print("Corner pixel (masked-out):", result[2, 2].tolist())
