"""OpenCV Practice: Composite Foreground over Background using Alpha"""

import cv2
import numpy as np


def make_background(size=100):
    return np.full((size, size, 3), (180, 180, 180), dtype=np.uint8)


def make_foreground_with_alpha(size=100):
    fg = np.zeros((size, size, 3), dtype=np.uint8)
    cv2.circle(fg, (size // 2, size // 2), size // 3, (0, 0, 255), -1)
    alpha = np.zeros((size, size), dtype=np.float32)
    cv2.circle(alpha, (size // 2, size // 2), size // 3, 0.7, -1)
    return fg, alpha


def alpha_composite(fg, bg, alpha):
    alpha3 = alpha[:, :, None]
    return (fg.astype(np.float32) * alpha3 + bg.astype(np.float32) * (1 - alpha3)).astype(np.uint8)


if __name__ == "__main__":
    bg = make_background()
    fg, alpha = make_foreground_with_alpha()
    composite = alpha_composite(fg, bg, alpha)

    print("Background mean:", bg.reshape(-1, 3).mean(axis=0).tolist())
    print("Foreground circle pixel:", fg[50, 50].tolist())
    print("Composite circle pixel:", composite[50, 50].tolist())
    print("Composite background-area pixel:", composite[2, 2].tolist())
